#!/usr/bin/env python3
"""Run a TradingHub workflow via Claude API with tool use.

Usage: python scripts/run_workflow.py <workflow-name>
Valid workflows: portfolio, pre-market, market-open, midday, daily-summary, weekly-review

Requires env vars: ANTHROPIC_API_KEY, ALPACA_API_KEY, ALPACA_SECRET_KEY
"""

import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request
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


def tool_web_search(query: str) -> str:
    print(f"    [web_search] {query[:100]}")
    try:
        url = (
            "https://api.duckduckgo.com/?"
            + urllib.parse.urlencode(
                {"q": query, "format": "json", "no_html": "1", "skip_disambig": "1"}
            )
        )
        req = urllib.request.Request(
            url, headers={"User-Agent": "TradingBot/1.0 (research)"}
        )
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read())

        parts: list[str] = []
        if data.get("AbstractText"):
            parts.append(data["AbstractText"])
        if data.get("Answer"):
            parts.append(f"Answer: {data['Answer']}")
        for topic in (data.get("RelatedTopics") or [])[:6]:
            if isinstance(topic, dict) and topic.get("Text"):
                parts.append(f"- {topic['Text']}")
        return "\n".join(parts) if parts else f"No direct results for: {query}"
    except Exception as e:
        return f"Search unavailable ({e}). Proceed without this data."


# ---------------------------------------------------------------------------
# Tool definitions for Claude API
# ---------------------------------------------------------------------------

TOOLS = [
    {
        "type": "web_search_20250305",
        "name": "web_search",
    },
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
                elif name == "web_search":
                    # web_search_20250305 is handled server-side by Anthropic.
                    # If it appears here as a client tool_use, run our fallback.
                    result = tool_web_search(inp.get("query", ""))
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
                # Only server-managed calls (e.g. web_search via Anthropic) — continue
                continue

            messages.append({"role": "user", "content": tool_results})

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
