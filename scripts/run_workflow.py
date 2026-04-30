#!/usr/bin/env python3
"""Run a TradingHub workflow via Claude API with tool use.

Usage: python scripts/run_workflow.py <workflow-name>
Valid workflows: portfolio, pre-market, market-open, midday, daily-summary, weekly-review

Requires env vars: ANTHROPIC_API_KEY, ALPACA_API_KEY, ALPACA_SECRET_KEY
"""

import os
import re
import subprocess
import sys
import time
from pathlib import Path

ROUTINE_FILE = ".claude/commands/ROUTINE.md"
MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 16000
MAX_TURNS = 40  # safety cap on agentic loop iterations

WORKFLOW_SECTIONS = {
    "portfolio":       "1. PORTFOLIO SNAPSHOT",
    "pre-market":      "2. PRE-MARKET RESEARCH",
    "market-open":     "3. MARKET-OPEN EXECUTION",
    "trade":           "4. MANUAL TRADE",
    "midday":          "5. MIDDAY SCAN",
    "daily-summary":   "6. DAILY SUMMARY",
    "weekly-review":   "7. WEEKLY REVIEW",
}


# ---------------------------------------------------------------------------
# Prompt extraction
# ---------------------------------------------------------------------------

def extract_prompt(workflow: str) -> str:
    section = WORKFLOW_SECTIONS[workflow]
    text = Path(ROUTINE_FILE).read_text(encoding="utf-8")
    pattern = rf"## {re.escape(section)}.*?```\n(.*?)```"
    m = re.search(pattern, text, re.DOTALL)
    if not m:
        raise ValueError(
            f"Prompt for '{workflow}' not found under '## {section}' in {ROUTINE_FILE}"
        )
    return m.group(1).strip()


# ---------------------------------------------------------------------------
# Tool implementations
# ---------------------------------------------------------------------------

def tool_bash(command: str) -> str:
    print(f"    [bash] {command[:120]}")
    try:
        r = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=120,
            env=os.environ,
        )
        out = r.stdout.strip()
        err = r.stderr.strip()
        if r.returncode != 0 and err:
            out = out + f"\nSTDERR: {err}\nEXIT: {r.returncode}" if out else f"STDERR: {err}\nEXIT: {r.returncode}"
        return out or "(no output)"
    except subprocess.TimeoutExpired:
        return "ERROR: command timed out after 120s"
    except Exception as e:
        return f"ERROR running command: {e}"


def tool_write_file(path: str, content: str, mode: str = "a") -> str:
    print(f"    [write_file] {path} (mode={mode}, {len(content)} chars)")
    try:
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, mode, encoding="utf-8") as f:
            f.write(content)
        return f"OK: wrote {len(content)} chars to {path}"
    except Exception as e:
        return f"ERROR writing {path}: {e}"


# ---------------------------------------------------------------------------
# Gemini research (pre-computed before Claude's loop)
# ---------------------------------------------------------------------------

# Which workflows need research, and what queries to run.
# Pre-market is the heavy one. Weekly-review needs the S&P comparison.
# Other workflows do not need external research.
WORKFLOW_RESEARCH_QUERIES: dict[str, list[str]] = {
    "pre-market": [
        "WTI crude oil price today",
        "Brent crude oil price today",
        "S&P 500 futures premarket level today",
        "VIX level today",
        "Top stock market catalysts today (earnings, Fed, macro)",
        "Pre-market earnings reports today",
        "US economic calendar today (CPI, PPI, FOMC, jobs data)",
        "S&P 500 sector momentum year-to-date 2026",
    ],
    "weekly-review": [
        "S&P 500 weekly performance for the most recent trading week",
    ],
}


def gemini_research(queries: list[str]) -> str:
    """Run all research queries through Gemini with Google Search grounding.
    Returns a markdown summary, or an empty fallback string if Gemini fails."""
    print(f"    [gemini] researching {len(queries)} queries...")
    try:
        from google import genai
        from google.genai import types

        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            return "[Gemini research unavailable: GEMINI_API_KEY not set]"

        client = genai.Client(api_key=api_key)

        bullets = "\n".join(f"- {q}" for q in queries)
        prompt = (
            "You are a financial research assistant. Research each of the queries "
            "below using current web data and produce a concise, fact-dense markdown "
            "summary.\n\n"
            "Format:\n"
            "- One subsection per query, with a short ### heading.\n"
            "- Lead with concrete numbers (prices, percentages, levels) wherever possible.\n"
            "- Note today's date implicitly via the data freshness.\n"
            "- No fluff, no disclaimers. Just facts and key context.\n"
            "- Total length: 400-800 words.\n\n"
            f"Queries:\n{bullets}\n"
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                tools=[types.Tool(google_search=types.GoogleSearch())],
            ),
        )
        text = (response.text or "").strip()
        if not text:
            return "[Gemini returned empty research]"
        return text
    except Exception as e:
        return f"[Gemini research failed: {e}]"


# ---------------------------------------------------------------------------
# Tool definitions for Claude API
# ---------------------------------------------------------------------------

# Note: web_search is intentionally NOT in this list. Research is pre-computed
# by Gemini and injected into the prompt, which keeps Claude's per-turn input
# small enough to stay under tier-1 rate limits.
TOOLS = [
    {
        "name": "bash",
        "description": (
            "Execute a bash shell command and return stdout/stderr. "
            "Use for: bash scripts/alpaca.sh ..., cat/tail/grep on memory files, "
            "git pull/add/commit/push. Working dir is the repo root."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "command": {
                    "type": "string",
                    "description": "The shell command to run.",
                }
            },
            "required": ["command"],
        },
    },
    {
        "name": "write_file",
        "description": "Write or append text content to a file on disk.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Relative file path from repo root."},
                "content": {"type": "string", "description": "Text to write."},
                "mode": {
                    "type": "string",
                    "enum": ["a", "w"],
                    "description": "'a' to append (default), 'w' to overwrite.",
                },
            },
            "required": ["path", "content"],
        },
    },
]


# ---------------------------------------------------------------------------
# Agentic loop
# ---------------------------------------------------------------------------

def run_workflow(workflow: str) -> None:
    import anthropic  # local import so module loads without SDK installed at top level

    prompt = extract_prompt(workflow)

    # Pre-compute web research with Gemini for workflows that need it.
    # Result gets prepended to Claude's prompt so Claude does NOT need to
    # call web_search itself — keeps each Claude turn small and cheap.
    if workflow in WORKFLOW_RESEARCH_QUERIES:
        print(f"\n=== [{workflow}] Pre-computing research via Gemini ===")
        research = gemini_research(WORKFLOW_RESEARCH_QUERIES[workflow])
        print(f"    [gemini] received {len(research)} chars of research")
        prompt = (
            "## Pre-Computed Market Research\n\n"
            "The following research has already been gathered for you using a "
            "web-grounded search. Use it as the basis for your analysis below "
            "instead of trying to run additional web searches.\n\n"
            f"{research}\n\n"
            "---\n\n"
            f"{prompt}\n\n"
            "**IMPORTANT:** Do not attempt to run web searches. All required market "
            "context is in the 'Pre-Computed Market Research' section above. Use it directly."
        )

    # max_retries=10 → SDK auto-retries on 429 with exponential backoff up to ~60s,
    # which is enough to wait out the rolling-minute rate limit window on tier 1.
    client = anthropic.Anthropic(max_retries=10)

    # Mark the initial workflow prompt as a cache breakpoint. The prefix up to here
    # gets cached, so on every subsequent turn this large prompt costs 10% normal price
    # AND does not re-count toward the 30k input-tokens-per-minute limit on tier 1.
    messages: list[dict] = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt,
                    "cache_control": {"type": "ephemeral"},
                }
            ],
        }
    ]
    print(f"\n=== [{workflow}] Starting workflow ===\n")

    for turn in range(MAX_TURNS):
        response = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            tools=TOOLS,
            messages=messages,
        )

        # Add assistant response to history
        messages.append({"role": "assistant", "content": response.content})

        # Print any text blocks
        for block in response.content:
            if hasattr(block, "text") and block.text:
                print(block.text)

        if response.stop_reason == "end_turn":
            break

        if response.stop_reason == "tool_use":
            tool_results: list[dict] = []

            for block in response.content:
                if not hasattr(block, "type") or block.type != "tool_use":
                    continue

                name: str = block.name
                inp: dict = block.input

                if name == "bash":
                    result = tool_bash(inp["command"])
                elif name == "write_file":
                    result = tool_write_file(
                        inp["path"], inp["content"], inp.get("mode", "a")
                    )
                else:
                    result = f"Unknown tool '{name}' — skipped."

                tool_results.append(
                    {
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result,
                    }
                )

            if not tool_results:
                # No client-side tool calls in this response — defensive continue
                continue

            messages.append({"role": "user", "content": tool_results})

            # Throttle the loop: tier-1 limit is 30k input TPM; each turn carries
            # the full message history, so by mid-conversation a single call
            # approaches the cap. Sleeping 20s between turns lets the rolling
            # window drain enough that the next call fits.
            print(f"    [throttle] sleeping 20s before next turn")
            time.sleep(20)

        else:
            print(f"[{workflow}] Unexpected stop_reason: {response.stop_reason}")
            break

    print(f"\n=== [{workflow}] Done (turn {turn + 1}) ===\n")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in WORKFLOW_SECTIONS:
        valid = ", ".join(WORKFLOW_SECTIONS)
        print(f"Usage: python scripts/run_workflow.py <workflow>\nValid: {valid}")
        sys.exit(1)

    run_workflow(sys.argv[1])
