# Trading Strategy & Rules

**Mission:** Beat S&P 500 on $100k Alpaca paper (Phase 1), then graduate to $1k live (Phase 2).

**Instruments:** Stocks ONLY. No options, no crypto, no forex.

**Horizon:** Swing trading (2–10 days typical). Not day-trading, not buy-and-hold.

---

## Capital & Position Constraints (Opus-Adapted)

- **Starting capital:** $100,000 (paper)
- **Max per position:** 20% of equity (~$20k)
- **Max open positions:** 5–6 at a time
- **Max deployed:** 75–85% of equity
- **Max trades per week:** 3 new positions
- **PDT rule:** 3 day trades per 5 rolling business days (sub-$25k account)

---

## Entry Signals (Trend + Mean-Reversion Hybrid)

**Qualify the universe first:**
- Market cap > $2B
- Average daily volume > 1M shares
- Price > $5
- Optional: S&P 500 / Nasdaq-100 names preferred

**Then apply signals:**
1. **Trend base:** 50-day SMA > 200-day SMA (long-bias) OR < (short-bias)
2. **Momentum:** 12-month return percentile vs universe in top quintile
3. **Entry trigger:** RSI(14) < 30 (in uptrend) for longs OR RSI > 70 (in downtrend) for shorts
4. **Volume confirm:** Entry day volume > 20-day average volume
5. **Catalyst:** Must have a documented reason TODAY (earnings, news, sector rotation, etc.)

---

## Stop & Target Rules

**Every position gets a real GTC stop-loss order placed at entry (not mental).**

- **Stop level:** 1 ATR or technical support/resistance, typically 7–10% below entry
- **Minimum:** Must have 2:1 risk/reward minimum
- **Target:** 2–3x ATR or technical resistance

---

## Exit Rules

**Mandatory stops:**
- **Hard stop at -7%:** Cut manually, no hope, no averaging down
- **Thesis break:** If catalyst invalidates or sector rolls over, cut immediately even if not at -7%

**Profit-taking (trailing):**
- At +15% unrealized: tighten trailing stop to 7%
- At +20% unrealized: tighten trailing stop to 5%
- Never tighten a stop within 3% of current price
- Never move a stop down (only closer to current price from above)

**Sector rotation:**
- Track consecutive failed trades per sector
- Exit entire sector if 2 consecutive trades fail in that sector
- Follow sector momentum; don't force a thesis into a rolling-over sector

**Patience rule:**
- A week with zero trades can be the right call
- Only trade when edge is present; else hold cash

---

## Trailing Stops (10% Standard)

Place a real 10% trailing_stop GTC order on Alpaca immediately after every entry fill.

If same-day stop rejection (PDT):
1. Try fixed stop (10% below entry)
2. If also blocked: queue for next morning

---

## Entry Checklist (Agent Documents All Before Placing)

Before every buy order, verify:
- ✓ What is the specific catalyst today?
- ✓ Is the sector in momentum (not rolling over)?
- ✓ What is the stop level (7–10% below entry)?
- ✓ What is the target (minimum 2:1 risk/reward)?
- ✓ Total positions after fill ≤ 6
- ✓ Trades this week (including this) ≤ 3
- ✓ Position cost ≤ 20% of equity
- ✓ Position cost ≤ available cash
- ✓ Daytrade count leaves room (PDT: 3/5 rolling days)
- ✓ Instrument is a stock (not an option, not a fund)

If any fail → skip trade, log reason.

---

## Research Cadence

**Pre-market (daily):**
- Oil (WTI / Brent)
- S&P 500 futures
- VIX level
- Top market catalysts
- Pre-market earnings
- Economic calendar (CPI, PPI, FOMC, jobs)
- Sector momentum (YTD, recent)
- News on held tickers

**Midday (conditional):**
- Thesis validation for open positions
- Major news on held names
- Intraday sector rotation signals

**Friday (weekly review):**
- Full week stats (win rate, profit factor, Sharpe)
- What worked, what didn't
- Adjustments for next week
- Performance vs S&P 500

---

## Phase Gate Criteria (Paper Validation)

Must pass all to advance to Phase 2 (live $1k account):
- Sharpe ratio ≥ 1.5
- Max drawdown ≤ 15%
- Positive expectancy (not just lucky win rate)
- ≥ 30 trading days of live data
- ≥ 30 closed trades

---

## Strategy Backlog (Research, Don't Adopt Yet)

- Pairs trading / stat arb on correlated equities
- Earnings drift / post-earnings momentum
- Sector rotation based on macro regime
- News-driven NLP sentiment overlay

Each gets tested, graded, kept or killed based on performance.
