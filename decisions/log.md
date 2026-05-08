# Decision Log

Append-only. When a meaningful decision is made, log it here.

Format: [YYYY-MM-DD] DECISION: ... | REASONING: ... | CONTEXT: ...

---

[2026-05-03] DECISION: Adopt Simons-inspired quant layer (Z-Score, VIX regime, Kelly sizing, pairs awareness) on top of existing catalyst checklist | REASONING: Two consecutive weeks of D-grade performance driven by underdeployment despite valid catalysts; need to widen the universe of qualifying setups without lowering quality bar | CONTEXT: Both layers must clear for entry. No forced trades. No lowered gates.

[2026-05-03] DECISION: Replace market orders with bracket limit orders for all entries | REASONING: Eliminates gap-chasing on earnings days; lets market come to bot's intended entry price; stop+target placed atomically with entry | CONTEXT: Day orders by default, expire unfilled at session close, re-evaluated next morning. Market orders only allowed for closing positions or thesis-break exits.

[2026-05-03] DECISION: Add afternoon-scan workflow at 2 PM ET (Option A) | REASONING: Catches last-2-hours setups, upgrades trailing stops on profitable fills, cancels stale unfilled limits if catalyst weakens | CONTEXT: Option B (conditional hourly monitor) archived to archives/phase-4-backlog.md for future activation after Phase 1 validation.

[2026-05-03] PHASE REVIEW: Phase 1 launched | KEY FINDING: Quant layer + bracket limits + 5b/5c workflows now active | NEXT REVIEW DUE: 2026-05-24

[2026-05-08] DECISION: Add Momentum Lane to quant layer (Option 2) | REASONING: After 1 week, mean-reversion-only Z|≥2.0| gate rejected 100% of candidates; bot is structurally blind to trend-continuation entries; Druckenmiller-style breakouts are missed by oversold gates | CONTEXT: Either Mean-Rev OR Momentum lane qualifies; both still gated by Layer A catalyst checks. No quality bar lowered.

[2026-05-08] DECISION: Adopt Minervini refinements (a)+(c)+(d) | REASONING: Trend Template tightens universe to true leaders; ≤5% pivot extension prevents chasing late breakouts; R-multiple framework standardizes risk reporting for Phase 1→2 graduation | CONTEXT: VCP detection (b) deferred to Phase 2; sell-into-strength (e) deferred to Phase 2.

[2026-05-08] DECISION: Promote shorts from Phase 3 to Phase 1 | REASONING: With Minervini Trend Template enabling rigorous identification of weak/laggard names AND bracket limits making short risk bounded by definition, short-side entries are now safely executable; bot was structurally net-long in any market direction | CONTEXT: Conservative caps applied — 10% per short position, 30% total short exposure, mega-caps + sector ETFs only, no shorting through earnings, no shorting after >5% gap-down. Caps relax in Phase 2 after data validates.

[2026-05-08] PHASE REORDER: VCP detection moved Phase 3 → Phase 2; Pairs trading moved Phase 3 → Phase 3 (unchanged) | KEY FINDING: Short-side execution promoted to Phase 1; VCP and sell-into-strength bundled into Phase 2 along with live $1k migration | NEXT REVIEW: 2026-05-24
