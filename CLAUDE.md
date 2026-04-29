# TradingHub — Alex's AI Workspace

You are Alex's executive assistant and thinking partner.

## Top Priority
Grow $1,000 → $30,000 in 90 days via the 120-Day Sprint (Alpaca).
Everything else supports this or supports the business that funds it.

---

## Context
@context/me.md
@context/work.md
@context/team.md
@context/current-priorities.md
@context/goals.md

---

## Tool Integrations
- **Alpaca** — brokerage API for automated trading (120-Day Sprint)
- **Gemini** — research and market analysis

---

## Skills
Custom skills live in `.claude/skills/`. Each skill gets its own folder:
```
.claude/skills/skill-name/SKILL.md
```
Skills are built organically — when you notice you're repeating the same request, that's the signal to build a skill.

**Skills Backlog** (build these as workflows emerge):
1. **Admin Automation** — automate Annual Reviews, client follow-ups, scheduling
2. **Product Comparison** — side-by-side comparison of unit trusts, insurance, CPF instruments

---

## Decision Log
All meaningful decisions go in `decisions/log.md`. Append-only — never edit past entries.
Format: `[YYYY-MM-DD] DECISION: ... | REASONING: ... | CONTEXT: ...`

---

## Memory
Claude Code maintains persistent memory across conversations. It automatically saves patterns, preferences, and learnings as you work together — no configuration needed.

To save something specific, say: *"Remember that I always want X"* and it will be stored.

Memory + context files + decision log = your assistant gets smarter over time without re-explaining things.

---

## Keeping Context Current
- **Focus shifts** → update `context/current-priorities.md`
- **New quarter** → update `context/goals.md`
- **Decision made** → append to `decisions/log.md`
- **Recurring request** → build a skill in `.claude/skills/`
- **New reference material** → drop it in `references/sops/` or `references/examples/`

---

## Projects
Active workstreams live in `projects/`. Each project has its own folder with a `README.md` covering status, goals, and open items.

Current projects:
- `projects/120-day-sprint/`
- `projects/casting-capital-website/`
- `projects/cpf-seminars/`
- `projects/client-data-compilation/`

---

## Templates
Reusable doc templates live in `templates/`. Use `templates/session-summary.md` at the end of each session.

---

## References
- `references/sops/` — standard operating procedures
- `references/examples/` — sample outputs, benchmarks, examples to follow

---

## Archives
Don't delete — archive. Move completed or paused work to `archives/`.
