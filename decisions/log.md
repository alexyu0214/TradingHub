# Decision Log

Append-only. When a meaningful decision is made, log it here.

Format: [YYYY-MM-DD] DECISION: ... | REASONING: ... | CONTEXT: ...

---

[2026-05-03] DECISION: Adopt Simons-inspired quant layer (Z-Score, VIX regime, Kelly sizing, pairs awareness) on top of existing catalyst checklist | REASONING: Two consecutive weeks of D-grade performance driven by underdeployment despite valid catalysts; need to widen the universe of qualifying setups without lowering quality bar | CONTEXT: Both layers must clear for entry. No forced trades. No lowered gates.

[2026-05-03] DECISION: Replace market orders with bracket limit orders for all entries | REASONING: Eliminates gap-chasing on earnings days; lets market come to bot's intended entry price; stop+target placed atomically with entry | CONTEXT: Day orders by default, expire unfilled at session close, re-evaluated next morning. Market orders only allowed for closing positions or thesis-break exits.

[2026-05-03] DECISION: Add afternoon-scan workflow at 2 PM ET (Option A) | REASONING: Catches last-2-hours setups, upgrades trailing stops on profitable fills, cancels stale unfilled limits if catalyst weakens | CONTEXT: Option B (conditional hourly monitor) archived to archives/phase-4-backlog.md for future activation after Phase 1 validation.

[2026-05-03] PHASE REVIEW: Phase 1 launched | KEY FINDING: Quant layer + bracket limits + 5b/5c workflows now active | NEXT REVIEW DUE: 2026-05-24
