---
description: Daily summary. Snapshot portfolio state, compute P&L, send daily recap.
---

# Daily Summary (End-of-Day)

Run after market close. Capture portfolio state, compute day P&L, log EOD snapshot, send recap.

---

## STEP 1 — Read Memory

```bash
tail -5 memory/TRADE-LOG.md  # Find yesterday's closing equity (needed for day P&L math)
cat memory/CONSTRAINTS.md     # Reference deployment targets
```

Extract yesterday's closing equity for day-over-day P&L calculation.

## STEP 2 — Pull Final Account State

```bash
bash scripts/alpaca.sh account
bash scripts/alpaca.sh positions
bash scripts/alpaca.sh orders
```

Capture: today's closing equity, cash, all positions with current prices.

## STEP 3 — Compute Metrics

**Day P&L:**
- Day P&L $ = today_equity - yesterday_equity
- Day P&L % = (Day P&L $) / yesterday_equity

**Phase cumulative P&L:**
- Phase P&L $ = today_equity - starting_equity ($100,000)
- Phase P&L % = (Phase P&L $) / starting_equity

**Trade counts:**
- Trades today = count today's entries in TRADE-LOG
- Trades this week = count Mon-today entries in TRADE-LOG

**Deployment:**
- Cash % = (cash / equity) × 100
- Deployed % = 100% - cash %

## STEP 4 — Append EOD Snapshot to TRADE-LOG.md

```markdown
### MMM DD — EOD Snapshot (Day N, Weekday)

**Portfolio:** $X | **Cash:** $X (X%) | **Day P&L:** ±$X (±X%) | **Phase P&L:** ±$X (±X%) | **Deployed:** X%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| SYM1 | N | $X | $X | ±$X (±X%) | $X | X days |
| SYM2 | N | $X | $X | ±$X (±X%) | $X | X days |

**Trades today:** [list or "none"]

**Notes:** [one-paragraph summary of day — what worked, what didn't, any learnings]
```

## STEP 5 — Append to DAILY-SUMMARY.md (Local Fallback)

Append daily recap (always, even on no-trade days):

```markdown
## YYYY-MM-DD — EOD

**Portfolio:** $X (±X% day, ±X% phase)
**Cash:** $X (X%)
**Deployed:** X%
**Daytrade count:** N/3

**Trades today:** [list with entry/exit prices or "none"]
**Open positions:** [SYM1 ±X%, SYM2 ±X%, etc. or "none"]
**Stops tightened:** [if any]
**Losers cut:** [if any]

**Notes:** [one-liner summary]

---
```

## STEP 6 — Print EOD Summary

```
Daily Summary — YYYY-MM-DD

Portfolio: $X | Cash: $X (X%) | Deployed: X%
Day P&L: ±$X (±X%)
Phase P&L: ±$X (±X%)

Trades today: [count or "none"]
Trades this week: N/3
Open positions: [count]

Largest position: SYM (±X%)
Largest risk: SYM (stop $X)

Circuit breaker status:
  Daily loss limit: ±X% (threshold 2%)
  Weekly loss limit: ±X% (threshold 5%)
  Max drawdown: ±X% (threshold 15%)
```

## STEP 7 — Notification

Send one ClickUp message (or append to DAILY-SUMMARY.md if local):

```
EOD YYYY-MM-DD

Portfolio: $X (±X% day, ±X% phase)
Cash: $X (X%)
Deployed: X%
Daytrade count: N/3

Trades today: [list or "none"]
Open: [list with stops or "none"]
Tomorrow: [one-line plan]
```

Keep it ≤ 15 lines. No fluff.

## STEP 8 — Circuit Breaker Check

- If day P&L ≤ -2% of equity: Log "Daily loss limit hit. No trading tomorrow."
- If phase P&L ≤ -5% of equity: Log "Weekly loss limit hit. Pause for review."
- If max drawdown ≥ -15% from peak: Log "Max drawdown hit. HALT. Manual restart only."

## STEP 9 — No Commit (Local Testing Phase)

Do NOT git commit/push. Local testing only.

---

## Notes

- **Mandatory daily:** Always write an EOD snapshot, even on no-trade days. Consistency builds discipline.
- **Circuit breaker:** These are **hard stops**. Don't trade tomorrow if daily limit hit. Don't continue if weekly limit hit.
- **One-liner notes:** Keep them short but informative. Examples:
  - "Strong sector rotation, few edges. Held cash."
  - "RSI oversold in 3 names, all hit targets. Good day."
  - "Lost 2 trades on fake breakouts. Tighten entry criteria."
