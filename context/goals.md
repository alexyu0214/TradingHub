# Goals — Q2 2026

## Phase 1 — Paper Validation ($100k)
Goal: prove the bot has edge and acceptable risk profile before going live.

Minimum gate to advance to Phase 2:
- **Sharpe ratio ≥ 1.5** over the validation window
- **Max drawdown ≤ 15%**
- **Win rate × avg win / avg loss ≥ positive expectancy** (no relying on lucky outliers)
- **At least 30 trading days** of live paper data
- **At least 30 trades** for statistical signal

## Phase 2 — Live Sprint ($1k → $30k in 90 days)
Stretch target. Realistic sub-targets:
| Window | Conservative | Aggressive |
|---|---|---|
| Day 30 | $1.5k | $2.5k |
| Day 60 | $2.5k | $7k |
| Day 90 | $5k | $30k |

Hitting $30k in 90 days requires near-perfect execution and tailwinds. Hitting $5k+ is realistic and unlocks PDT capacity ($25k threshold) plus margin headroom.

## Operational
- Build the bot as a 24/7 service running against Alpaca's API
- Track every trade with rationale + outcome (journal in `projects/trading-bot/journal/`)
- Append every meaningful decision to `decisions/log.md`
