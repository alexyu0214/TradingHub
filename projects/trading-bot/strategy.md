# Strategy

Living document. Strategies live and die based on performance.

## v1 Candidate (to validate on paper)

**Hybrid: Trend-following with mean-reversion overlay on liquid US equities.**

### Universe
- US equities, market cap > $2B (avoid micro-cap manipulation)
- Average daily volume > 1M shares (liquidity for entries/exits)
- Price > $5 (avoids penny-stock noise and low-quality names)
- Optional tilt toward S&P 500 + Nasdaq-100 names

### Signals to test
- **Trend:** 50-day above 200-day SMA (long bias) or below (short bias)
- **Momentum:** 12-month return percentile vs universe (top quintile = long candidate)
- **Mean-reversion entry:** RSI(14) < 30 in a strong long uptrend; RSI > 70 in a downtrend for shorts
- **Volatility filter:** ATR-based — skip names with anomalous volatility spikes (earnings, news shocks)
- **Volume confirmation:** entry day volume > 20-day average

### Holding period
2–10 trading days typical. Exit on:
- Target hit (2–3x ATR)
- Stop hit (1 ATR or technical level break)
- Signal invalidation (trend flip, etc.)

## What this is NOT
- Not day-trading (PDT considerations + transaction cost drag)
- Not options (mandate is shares only)
- Not crypto, not forex (mandate is US equities)
- Not "buy and hold" — bot is active

## Strategy backlog (research before adopting)
- Pairs trading / stat arb on correlated equities
- Earnings drift / post-earnings momentum
- Sector rotation based on macro regime
- News-driven NLP sentiment overlay

## Performance tracking
Every strategy tracked separately. Kill any strategy that fails the gate criteria over a meaningful sample.
