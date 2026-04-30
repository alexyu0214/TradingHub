---
description: Daily pre-market research. Document catalysts, generate trade ideas, decide trade/hold.
---

# Pre-Market Research Workflow (Local)

Run this every morning before market open to research the day ahead.

## STEP 1 — Read Memory for Context

```bash
cat memory/TRADING-STRATEGY.md
tail -20 memory/TRADE-LOG.md    # Last EOD snapshot
tail -5 memory/RESEARCH-LOG.md  # Previous day's research
```

Parse strategy rules, review any open positions and their thesis, note any sector momentum from yesterday.

## STEP 2 — Pull Live Account State

```bash
bash scripts/alpaca.sh account
bash scripts/alpaca.sh positions
bash scripts/alpaca.sh orders
```

Capture: equity, cash, buying power, daytrade count, open positions with entry prices.

## STEP 3 — Research Market Context (WebSearch)

Run native Claude WebSearch for each query. Format as markdown with citations.

**Queries to run:**
- WTI and Brent oil prices today
- S&P 500 futures premarket
- VIX level today
- Top stock market catalysts today (earnings, news, Fed)
- Pre-market earnings reports
- Economic calendar (CPI, PPI, FOMC, jobs data)
- S&P 500 sector momentum year-to-date
- Any news on current held tickers (if positions open)

## STEP 4 — Generate Trade Ideas

Using research + TRADING-STRATEGY.md signals, identify **2–3 actionable trade ideas** (or 0 if no edge).

**For each idea, document:**
- TICKER
- Catalyst (specific reason for trade today)
- Sector momentum check (is this sector healthy?)
- Entry price/level (where to buy or short)
- Stop level (7–10% below entry, or technical support/resistance)
- Target price (minimum 2:1 risk/reward)

**Entry signal checklist:**
- 50/200 SMA trend direction confirmed?
- RSI(14) in the right zone (< 30 for long uptrend, > 70 for downtrend)?
- Volume confirmation (entry day > 20-day avg)?
- Catalyst documented?

**Skip if:** No edge. Default to HOLD.

## STEP 5 — Write Research Log Entry

Append a new dated entry to `memory/RESEARCH-LOG.md` with format from template:

```markdown
## YYYY-MM-DD — Pre-market Research

### Account
- Equity: $X
- Cash: $X (X%)
- Buying power: $X
- Daytrade count: N/3

### Market Context
[paste research from Step 3, bulleted]

### Trade Ideas
[list each idea with catalyst, entry, stop, target, R:R]

### Risk Factors
[any major risks today?]

### Decision
TRADE or HOLD
```

## STEP 6 — Print Summary to User

Print the research log entry to stdout. Highlight any action items.

## STEP 7 — No Commit (Local Testing Phase)

Do NOT run git commands. This is local-only testing. Memory persists in repo for next session, but no push yet.

---

## Notes

- **Patience rule:** If no edge exists, HOLD. A day with zero trades is better than a forced trade.
- **Sector check:** Don't trade a ticker in a sector that just failed 2 trades. Reference TRADE-LOG for sector history.
- **Earnings:** Don't take new positions through earnings on the underlying unless explicitly part of strategy.
