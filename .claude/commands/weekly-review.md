---
description: Friday weekly review. Stats, grading, adjustments for next week.
---

# Weekly Review (Friday)

Run Friday after market close. Compute week stats, grade performance, review strategy adjustments.

---

## STEP 1 — Read Memory

```bash
cat memory/TRADING-STRATEGY.md
cat memory/CONSTRAINTS.md
grep -A 500 "## Week ending" memory/WEEKLY-REVIEW.md | head -50  # Last week's review
grep "## [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]" memory/TRADE-LOG.md | tail -20  # This week's entries
grep "## [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]" memory/RESEARCH-LOG.md | tail -10  # This week's research
```

Understand the week's trades, research, and context.

## STEP 2 — Pull Week-End Account State

```bash
bash scripts/alpaca.sh account
bash scripts/alpaca.sh positions
```

Capture: ending equity, cash, open positions.

## STEP 3 — Compute Week Stats

**From TRADE-LOG:**
- Starting equity (Monday AM)
- Ending equity (Friday close)
- Week return $ and %
- All closed trades (entry, exit, P&L for each)
- Win count, loss count, open trade count
- Win rate (closed only)
- Best trade P&L
- Worst trade P&L
- Profit factor = (sum of wins) / |sum of losses|

**From market data (WebSearch):**
```bash
# Query: "S&P 500 weekly performance for week ending YYYY-MM-DD"
```

Extract S&P 500 week return %, then compute: Bot vs S&P = Week return % - S&P return %.

**Position data:**
- Max intraweek drawdown
- Current open positions + unrealized P&L

## STEP 4 — Append Full Review to WEEKLY-REVIEW.md

```markdown
## Week ending YYYY-MM-DD

### Stats
| Metric | Value |
|--------|-------|
| Starting portfolio | $X |
| Ending portfolio | $X |
| Week return | ±$X (±X%) |
| S&P 500 week | ±X% |
| Bot vs S&P 500 | ±X% |
| Trades executed | N |
| Wins | X |
| Losses | X |
| Open positions | X |
| Win rate | X% |
| Best trade | SYM +X% |
| Worst trade | SYM -X% |
| Profit factor | X.XX |
| Max intraweek drawdown | -X% |

### Closed Trades (This Week)
| Date | Ticker | Entry | Exit | P&L | Hold (days) | Notes |
|------|--------|-------|------|-----|-------------|-------|
| MM-DD | SYM1 | $X | $X | ±$X | X | [brief reason] |

### Open Positions at Week End
| Ticker | Entry | Close | Unrealized | Stop |
|--------|-------|-------|------------|------|
| SYM1 | $X | $X | ±$X (±X%) | $X |

### What Worked (3–5 bullets)
- [e.g., "50/200 SMA crossovers: 3 trades, 3 wins"]
- [e.g., "RSI < 30 in uptrend: high-probability entries"]
- [e.g., "Trailing stops: captured 60%+ of moves before cutting"]

### What Didn't Work (3–5 bullets)
- [e.g., "Fake earnings-driven breakouts: 2 trades, 0 wins"]
- [e.g., "Forced trades on low-volume names: slippage cost X%"]
- [e.g., "Sector rotation timing off: 3 days late on re-entry"]

### Key Lessons (2–3 bullets)
- [What will you apply to next week?]

### Adjustments for Next Week
- [Changes to universe, signals, risk sizing, etc.]

### Overall Grade: X (A–F)
[Justification]

---
```

**Grading:**
- **A:** Week return > S&P 500 by 2%+, perfect execution, no rules violations
- **B:** Week return in line with S&P 500, clean execution, maybe one small mistake
- **C:** Week return < S&P 500 by < 2%, trades happened, some turbulence but managed
- **D:** Week return significantly negative, execution issues, multiple lessons
- **F:** Major loss, rules violation, serious mistake (rare)

## STEP 5 — Strategy Adjustments (Conditional)

If a rule has worked consistently for 2+ weeks OR failed badly (significant losing streak in one signal):

- Update `memory/TRADING-STRATEGY.md` to reflect change
- Document the change in the weekly review ("Updated: RSI threshold from 30 to 35 based on 2-week trial")
- Log decision to `decisions/log.md` (if using git): `[YYYY-MM-DD] DECISION: update RSI threshold | REASONING: improved win rate | CONTEXT: 2-week backtest`

## STEP 6 — Send Weekly Recap

Append to DAILY-SUMMARY.md (local fallback):

```markdown
## WEEK ENDING YYYY-MM-DD — WEEKLY RECAP

**Portfolio:** $X (±X% week, ±X% phase)
vs S&P 500: ±X%

**Trades:** N (W:X / L:Y / open:Z)
**Win rate:** X% | **Best:** SYM +X% | **Worst:** SYM -X%

**Key win:** [one sentence on best strategy this week]
**Lesson learned:** [one sentence on adjustment for next week]
**Grade:** X

---
```

Keep it ≤ 15 lines.

## STEP 7 — Print Summary

```
Weekly Review — Week Ending YYYY-MM-DD

Portfolio: $X (±X% week, ±X% phase)
vs S&P 500: ±X%

Trades: N (W:X / L:Y / open:Z)
Win rate: X%
Best trade: SYM +X%
Worst trade: SYM -X%
Profit factor: X.XX

Max drawdown this week: -X%

Grade: X

Key lesson: [one-liner]
Next week: [one-liner plan]
```

## STEP 8 — No Commit (Local Testing Phase)

Do NOT git commit/push. Local testing only.

---

## Notes

- **Honest grading:** Don't inflate grades. Be harsh on yourself — that's how you improve.
- **Trend identification:** Watch for 2+ week patterns. If something is consistently working or failing, adjust it.
- **Comparison to S&P:** Always compare to S&P 500. If you're flat but S&P is down 2%, you won. If you're up 2% but S&P is up 5%, you lost.
- **Adjustment discipline:** Only change rules based on data, not emotion. 2+ week sample minimum.
