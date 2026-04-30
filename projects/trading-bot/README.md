# Trading Bot

**Status:** Phase 1 — Paper Validation
**Account:** Alpaca paper, $100,000 starting equity
**Mandate:** 24/7 automated long/short equity bot. Swing horizon. Strategy at Claude's discretion within risk rules.

## Phases
See [phases.md](phases.md). Short version: validate on paper, then move to live $1k account for the 90-day sprint.

## Strategy
See [strategy.md](strategy.md). Living document — strategies will be added, tested, kept or killed.

## Risk Rules
See [risk-rules.md](risk-rules.md). Hard constraints. The bot does not violate these.

## Trade Decision Protocol
Every trade decision follows this order:
1. **Instructions** — check user-provided playbook/instructions first
2. **Technical analysis** — apply the most appropriate TA for the setup
3. **Risk rules** — must pass all checks in `risk-rules.md`

If any step says "no," the trade does not happen.

## Journal
Trade-by-trade log in `journal/`. Each entry: date, ticker, side, size, rationale, exit, P&L, lesson.

## Open Items
- [ ] Define v1 strategy (likely: trend-following + mean-reversion hybrid on liquid US equities)
- [ ] Lock down risk rules
- [ ] Build Alpaca API connection (paper)
- [ ] Build performance dashboard (Sharpe, drawdown, win rate, expectancy)
- [ ] First paper trade
- [ ] 30 trades / 30 days minimum before considering live cutover
