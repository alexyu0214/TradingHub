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

[2026-05-13] ROOT CAUSE FOUND: Entire bot dead since 2026-05-08 — pre-market, market-open, midday, midday-rescan, afternoon-scan all stopped producing commits | DIAGNOSIS: The 2026-05-08 Phase 1 expansion + self-assessment edits added NESTED triple-backtick code fences inside the pre-market and weekly-review prompt bodies in ROUTINE.md. scripts/run_workflow.py's extract_prompt() used a non-greedy regex that stopped at the FIRST nested fence, truncating the pre-market prompt from ~185 lines to ~22 lines (cut off mid-STEP-1b). The bot received an incomplete workflow with no STEP 2-9 and could not function — failed silently, committed nothing. NOT a rate-limit or timeout issue. | FIX: Rewrote extract_prompt() to bound each section at the next real `## <n>.` header and capture everything between the FIRST and LAST ``` within the section, preserving nested fences. Added a length sanity-check that raises if an extracted prompt is < 200 chars. Verified all 8 workflows now extract full-length prompts. | CONTEXT: 5 trading days of zero bot activity (May 8-13). No trades placed all week as a direct result.

[2026-05-10] DECISION: Audit + fix bot's self-assessment loop after May 8 weekly review generated demonstrably false data (claimed 0 trades + XOM unchanged when XOM was actually exited May 7 at -$943) | REASONING: Bot was reasoning over data its grep patterns didn't fully surface AND had no mechanism to verify which adjustments were already built into code, leading to repeated false-alarm requests for already-implemented features | CONTEXT: Four fixes applied: (1) anchored grep patterns in weekly-review STEP 1 with ^ and explicit heading levels (### for TRADE-LOG, ## for RESEARCH-LOG/WEEKLY-REVIEW), (2) added Implementation Audit step to weekly-review (STEP 5a) requiring bot to verify adjustments against codebase before claiming they're missing, (3) added Monday-only Adjustment Audit to pre-market (STEP 1b) for proactive accountability, (4) cleaned up WEEKLY-REVIEW.md duplicates (3× "Week ending 2026-05-01" entries collapsed to one + relabeled stale "2026-05-03" entry as "2026-05-08 [LEGACY — DATA STALE]" with explicit warning).
