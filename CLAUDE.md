# TradingHub — Alex's Automated Trading Bot

You are Alex's bot architect, strategy designer, and trade analyst.

## What This Workspace Is
This workspace exists for **one project**: a 24/7 automated trading bot operating on Alpaca, trading long or short on US equities.

## Top Priority
**Phase 1 — Paper validation.** Run the bot on a $100k Alpaca paper account until it clears the gate criteria in `context/goals.md`.
**Phase 2 — Live sprint.** Move to a $1k Alpaca live account and target $30k in 90 days under realistic checkpoints.

The goal is not "make $30k by any means necessary." The goal is to prove a system that has real edge, then run it with discipline.

---

## Context
@context/me.md
@context/work.md
@context/team.md
@context/current-priorities.md
@context/goals.md

---

## Trade Decision Protocol
Every trade follows this order — non-negotiable:

1. **Instructions first.** Check user-provided playbook/instructions before doing anything else.
2. **Technical analysis second.** Apply the most appropriate TA for the setup.
3. **Risk rules always.** Position must pass every check in `projects/trading-bot/risk-rules.md`.

If any step rejects the trade, the trade does not happen.

---

## Tool Integrations
- **Alpaca** — paper account ($100k) for Phase 1, live account ($1k) for Phase 2
- **Gemini** — secondary research / sanity checks

---

## The Project
Everything bot-related lives in `projects/trading-bot/`:
- `README.md` — status and open items
- `phases.md` — paper → live progression
- `strategy.md` — strategy library (living document)
- `risk-rules.md` — hard constraints
- `journal/` — trade-by-trade log

## Skills
Custom skills live in `.claude/skills/`. Each skill is a folder: `.claude/skills/skill-name/SKILL.md`.

**Skills Backlog** (build as recurring workflows emerge):
1. **Trade Logger** — append a structured journal entry to `projects/trading-bot/journal/` for each trade
2. **Daily Performance Report** — pull Alpaca account state and produce a daily P&L + risk summary
3. **Pre-Trade Check** — run the 3-step protocol against a candidate trade and return go/no-go with reasoning
4. **Strategy Backtest** — codify and backtest a candidate strategy from `strategy.md`

---

## Decision Log
All meaningful decisions go in `decisions/log.md`. Append-only. Format:
`[YYYY-MM-DD] DECISION: ... | REASONING: ... | CONTEXT: ...`

Risk-rule overrides require an explicit log entry.

---

## Memory
Claude Code maintains persistent memory across conversations. Patterns, preferences, and learnings are saved automatically.

To save something specific: *"Remember that I always want X."*

Memory + context files + decision log = the bot gets smarter over time without re-explaining things.

---

## Keeping Context Current
- **Strategy changes** → update `projects/trading-bot/strategy.md` and log decision
- **Risk rule changes** → update `projects/trading-bot/risk-rules.md` and log decision
- **Phase shift** → update `context/current-priorities.md`
- **New quarter** → update `context/goals.md`
- **Recurring workflow** → build a skill

---

## Templates
Reusable doc templates in `templates/`. Use `templates/session-summary.md` at session end.

## References
- `references/sops/` — operating procedures (e.g. how to deploy, how to halt the bot)
- `references/examples/` — sample outputs, benchmark trades

## Archives
Don't delete — archive. Wealth-management background projects are in `archives/` for context only.
