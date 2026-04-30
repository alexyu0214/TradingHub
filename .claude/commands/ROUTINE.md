# Trading Bot Cron Prompts

These are standalone prompts for each workflow. Copy/paste into a fresh Claude Code session and run.

**REMOTE EXECUTION (GitHub Actions):**
These prompts now include git operations for 24/7 automated runs via GitHub Actions.
- At start: `git pull` to fetch latest memory files
- At end: `git add memory/ && git commit && git push` to update remote repo
- API credentials from environment variables (GitHub Secrets), not .env files

**LOCAL EXECUTION (Manual Claude Code):**
If running locally, skip git commands but still use environment variables.

---

## 1. PORTFOLIO SNAPSHOT

```
You are running the portfolio snapshot command for Alex's Alpaca trading bot.

**CRITICAL REMINDERS:**
- This is READ-ONLY (no file writes, no trades)
- API credentials come from environment variables: ALPACA_API_KEY, ALPACA_SECRET_KEY
- DO NOT read from .env or config files

**WORKFLOW:**
Pull live account state from Alpaca and print a clean snapshot table.

STEP 1 — Pull Live Account State
bash scripts/alpaca.sh account
bash scripts/alpaca.sh positions
bash scripts/alpaca.sh orders

STEP 2 — Parse & Format
Extract from the JSON:
- Equity, Cash, Buying Power, Daytrade count
- All open positions (ticker, qty, entry price, current price, unrealized P&L, P&L %)
- All open stop orders (ticker, order type, stop price / trail %, order ID)

STEP 3 — Print Summary Table
Portfolio Snapshot — YYYY-MM-DD HH:MM

Equity: $X | Cash: $X (X%) | Buying Power: $X
Daytrade count: N/3 | Positions: N open

Positions:
  SYM | qty | Entry $X → Now $X | Unrealized ±$X (±X%) | Stop $X | Status

Open Orders:
  ORDER_ID | SYM | Qty | Type (trail % / stop $) | Status

STEP 4 — Sanity Checks (No Commentary Except Warnings)
- If a position has no stop order → Flag: "WARNING: SYM has no stop"
- If a stop is below current price → Flag: "WARNING: SYM stop $X is below current price $Y"
- Otherwise: silent (no fluff)

STEP 5 — Exit
Print the table and stop. No file writes. No git commits.
```

---

## 2. PRE-MARKET RESEARCH

```
You are running the pre-market research workflow for Alex's Alpaca trading bot.

**CRITICAL REMINDERS:**
1. REMOTE SETUP: git pull origin main at start
2. READ FIRST: memory/TRADING-STRATEGY.md, memory/TRADE-LOG.md (tail -20), memory/RESEARCH-LOG.md (tail -5)
3. API credentials: ALPACA_API_KEY, ALPACA_SECRET_KEY, GEMINI_API_KEY from environment variables ONLY
4. WRITE AT END: Append new entry to memory/RESEARCH-LOG.md
5. REMOTE CLEANUP: git add memory/ && git commit -m "chore: pre-market research" && git push origin main

**WORKFLOW:**
Research the day ahead. Document catalysts, generate 2–3 trade ideas (or HOLD if no edge).

STEP 1 — Read Memory for Context
cat memory/TRADING-STRATEGY.md
tail -20 memory/TRADE-LOG.md    # Last EOD snapshot
tail -5 memory/RESEARCH-LOG.md  # Previous day's research

Parse strategy rules, review any open positions and their thesis, note any sector momentum from yesterday.

STEP 2 — Pull Live Account State
bash scripts/alpaca.sh account
bash scripts/alpaca.sh positions
bash scripts/alpaca.sh orders

Capture: equity, cash, buying power, daytrade count, open positions with entry prices.

STEP 3 — Research Market Context
Run Claude WebSearch (built-in tool) for each query:
- WTI and Brent oil prices today
- S&P 500 futures premarket
- VIX level today
- Top stock market catalysts today (earnings, news, Fed)
- Pre-market earnings reports
- Economic calendar (CPI, PPI, FOMC, jobs data)
- S&P 500 sector momentum year-to-date
- Any news on current held tickers (if positions open)

STEP 4 — Generate Trade Ideas
Using research + TRADING-STRATEGY.md signals, identify 2–3 actionable trade ideas (or 0 if no edge).

For each idea, document:
- TICKER
- Catalyst (specific reason for trade today)
- Sector momentum check (is this sector healthy?)
- Entry price/level (where to buy or short)
- Stop level (7–10% below entry, or technical support/resistance)
- Target price (minimum 2:1 risk/reward)

Entry signal checklist:
- 50/200 SMA trend direction confirmed?
- RSI(14) in the right zone (< 30 for long uptrend, > 70 for downtrend)?
- Volume confirmation (entry day > 20-day avg)?
- Catalyst documented?

Skip if: No edge. Default to HOLD.

STEP 5 — Write Research Log Entry
Append a new dated entry to memory/RESEARCH-LOG.md:

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

STEP 6 — Print Summary to User
Print the research log entry to stdout. Highlight any action items.

STEP 7 — Verify Files Updated
Confirm memory/RESEARCH-LOG.md has been appended. No git commits (local testing).
```

---

## 3. MARKET-OPEN EXECUTION

```
You are running the market-open execution workflow for Alex's Alpaca trading bot.

**CRITICAL REMINDERS:**
1. REMOTE SETUP: git pull origin main at start
2. READ FIRST: memory/RESEARCH-LOG.md (today's entry), memory/CONSTRAINTS.md
3. API credentials: ALPACA_API_KEY, ALPACA_SECRET_KEY from environment variables ONLY
4. WRITE AT END: Append to memory/TRADE-LOG.md, memory/DAILY-SUMMARY.md
5. REMOTE CLEANUP: git add memory/ && git commit -m "chore: market-open execution" && git push origin main

**WORKFLOW:**
Execute any planned trades from this morning's research. Validate with fresh quotes, set trailing stops.

STEP 1 — Read Today's Research
grep -A 50 "## $(date +%Y-%m-%d)" memory/RESEARCH-LOG.md

Pull today's trade ideas (if any) and confirm DECISION was TRADE (not HOLD).

STEP 2 — Re-Validate with Live Quotes
For each planned trade from research:
bash scripts/alpaca.sh quote SYMBOL
bash scripts/alpaca.sh account  # Check current positions count, daytrade count

- Check bid/ask spread (wide spread = halt signal)
- Verify SYMBOL hasn't been halted, delisted, or gapped past entry level
- Re-confirm daytrade count allows same-day sell (if needed)

STEP 3 — Run Buy-Side Gate on Each Planned Trade
Use memory/CONSTRAINTS.md checklist:
- Total positions after fill ≤ 6
- Trades this week (including this) ≤ 3
- Position cost ≤ 20% equity
- Position cost ≤ available cash
- PDT rules allow
- Catalyst still valid (re-read news if big news hit overnight)

If any trade fails: Skip it. Log the reason and move on.

STEP 4 — Execute Approved Trades
For each approved trade:
bash scripts/alpaca.sh order '{"symbol":"SYMBOL","qty":"SHARES","side":"buy","type":"market","time_in_force":"day"}'

Wait for fill. Capture: SYMBOL, fill price, fill quantity, order ID.

STEP 5 — Immediately Place 10% Trailing Stop (GTC)
For each filled buy order:
bash scripts/alpaca.sh order '{"symbol":"SYMBOL","qty":"SHARES","side":"sell","type":"trailing_stop","trail_percent":"10","time_in_force":"gtc"}'

If rejected (PDT error):
1. Try fixed stop 10% below fill:
   bash scripts/alpaca.sh order '{"symbol":"SYMBOL","qty":"SHARES","side":"sell","type":"stop","stop_price":"X.XX","time_in_force":"gtc"}'
2. If also rejected: Note "PDT-blocked, set tomorrow morning" in TRADE-LOG

STEP 6 — Log Each Trade to memory/TRADE-LOG.md
Append entry with full thesis from research, entry price, stop, target, R:R:

### YYYY-MM-DD HH:MM — BUY SYMBOL
**Catalyst:** [from research]
**Entry Price:** $X.XX (SHARES shares, filled at market)
**Stop:** $X.XX (-10% trailing) [or fixed stop if trailing rejected]
**Target:** $X.XX
**Risk:** $X (% of equity)
**Thesis:** [copied from research log]
**Trade ID:** [timestamp]

STEP 7 — Append to memory/DAILY-SUMMARY.md
Market-open executions:
- SYMBOL1: SHARES @ $X.XX, stop $X.XX
- SYMBOL2: SHARES @ $X.XX, stop $X.XX
(or "No trades executed")

STEP 8 — Print Summary
List all executed trades:
Market-Open Execution — YYYY-MM-DD

Executed:
  SYMBOL1: SHARES @ $X.XX, 10% trail stop placed
  SYMBOL2: SHARES @ $X.XX, 10% trail stop placed

Skipped:
  SYMBOL3: Daytrade limit reached
  SYMBOL4: Insufficient cash

Portfolio now: N positions, X% deployed

STEP 9 — Verify Files Updated
Confirm memory/TRADE-LOG.md and memory/DAILY-SUMMARY.md appended. No git commits.
```

---

## 4. MANUAL TRADE

```
You are running the manual trade command for Alex's Alpaca trading bot.

**USAGE:** Run with parameters: SYMBOL SHARES buy|sell
Example: /trade SPY 10 buy

**CRITICAL REMINDERS:**
1. REMOTE SETUP: git pull origin main at start (if running via remote)
2. READ FIRST: memory/CONSTRAINTS.md, memory/RESEARCH-LOG.md (today's entry), memory/TRADE-LOG.md
3. API credentials: ALPACA_API_KEY, ALPACA_SECRET_KEY from environment variables ONLY
4. WRITE AT END: Append to memory/TRADE-LOG.md, memory/DAILY-SUMMARY.md
5. REMOTE CLEANUP: git add memory/ && git commit -m "chore: manual trade SYMBOL" && git push origin main

**WORKFLOW:**
Execute a manual trade with full constraint validation. Refuse any trade that fails a rule.

STEP 1 — Parse Arguments
Args: SYMBOL, SHARES, SIDE (buy or sell). Require all three; ask if missing.

STEP 2 — Pull Live State
bash scripts/alpaca.sh account
bash scripts/alpaca.sh positions
bash scripts/alpaca.sh quote SYMBOL  # Get bid/ask

Extract: equity, cash, current positions count, current positions per sector.

STEP 3 — FOR BUY ORDERS — Validate All Rules
Run through memory/CONSTRAINTS.md buy-side gate. STOP and refuse if ANY fail:
- [ ] Total positions after fill ≤ 6
- [ ] Trades this week (including this one) ≤ 3
- [ ] Position cost (SHARES × ask_price) ≤ 20% of equity
- [ ] Position cost ≤ available cash
- [ ] Daytrade count < 3 (if same-day close intended)
- [ ] A specific catalyst is documented in today's RESEARCH-LOG.md
- [ ] SYMBOL is a stock (verify with quote, reject if OTC, delisted, or halted)
- [ ] Bid/ask spread is reasonable (< 1% for liquid names; flag if wide)

If ANY fail: Print the failed checks and STOP. Do NOT place order.

STEP 4 — FOR SELL ORDERS — Basic Check
- [ ] Position exists with that ticker and has ≥ SHARES
- [ ] Otherwise pass through (simpler validation for exits)

STEP 5 — Print Order Details & Ask Confirmation
Format the order JSON and show user:
{
  "symbol": "SPY",
  "qty": "10",
  "side": "buy",
  "type": "market",
  "time_in_force": "day"
}

Print all passed checks:
✓ Total positions after: 2/6
✓ Trades this week: 1/3
✓ Position cost: 5% of equity
✓ Cash available: yes
✓ Catalyst documented: "Fed rate decision, risk-off to risk-on rotation"
✓ SYMBOL: SPY (liquid, spreads tight)

Execute? (y/n)

STEP 6 — On Confirm (y) — Place Market Buy
bash scripts/alpaca.sh order '{"symbol":"SPY","qty":"10","side":"buy","type":"market","time_in_force":"day"}'

Wait for fill confirmation. Extract fill price and order ID.

STEP 7 — For BUYs — Immediately Place 10% Trailing Stop (GTC)
bash scripts/alpaca.sh order '{"symbol":"SPY","qty":"10","side":"sell","type":"trailing_stop","trail_percent":"10","time_in_force":"gtc"}'

If Alpaca rejects with PDT error:
- Fall back to fixed stop 10% below fill price
- If also rejected: Print "Stop queued for next trading day morning" and note in TRADE-LOG

STEP 8 — Log to memory/TRADE-LOG.md
Append new trade entry:
### YYYY-MM-DD HH:MM — BUY SPY
**Catalyst:** Fed rate decision, risk-off to risk-on rotation
**Entry Price:** $X.XX (10 shares, filled at market)
**Stop:** $X.XX (-10% trailing)
**Target:** $X.XX (2:1 R:R)
**Risk:** $X (1% of equity)
**Thesis:** Fed signals easier policy ahead; SPY sector momentum confirming long bias from 50/200 SMA. Entry on RSI < 30 in uptrend. Volume confirmed.
**Trade ID:** [auto-generated timestamp]

STEP 9 — Append to memory/DAILY-SUMMARY.md
- SPY: 10 shares @ $X.XX, stop $X.XX, target $X.XX (2:1 R:R)

STEP 10 — Print Confirmation
Trade executed.
SPY 10 @ $X.XX (fill ID: XXX)
10% trailing stop placed (GTC, order ID: YYY)
Logged to TRADE-LOG.md

STEP 11 — Verify Files Updated
Confirm memory/TRADE-LOG.md and memory/DAILY-SUMMARY.md appended. No git commits.
```

---

## 5. MIDDAY SCAN

```
You are running the midday scan workflow for Alex's Alpaca trading bot.

**CRITICAL REMINDERS:**
1. REMOTE SETUP: git pull origin main at start
2. READ FIRST: memory/TRADING-STRATEGY.md, memory/TRADE-LOG.md (tail -20), memory/RESEARCH-LOG.md
3. API credentials: ALPACA_API_KEY, ALPACA_SECRET_KEY from environment variables ONLY
4. WRITE AT END: Append to memory/TRADE-LOG.md, memory/DAILY-SUMMARY.md (only if actions taken)
5. REMOTE CLEANUP: git add memory/ && git commit -m "chore: midday scan" && git push origin main

**WORKFLOW:**
Scan open positions mid-trading day. Cut losses, tighten stops on winners, validate thesis.

STEP 1 — Read Memory
cat memory/TRADING-STRATEGY.md  # Exit rules
tail -20 memory/TRADE-LOG.md    # Recent trades + entries
cat memory/RESEARCH-LOG.md      # Today's research (any midday thesis check?)

Review entry theses and stop levels.

STEP 2 — Pull Live Positions
bash scripts/alpaca.sh positions
bash scripts/alpaca.sh orders
bash scripts/alpaca.sh account

For each open position: ticker, qty, entry, current price, unrealized P&L %, stop level.

STEP 3 — CUT LOSERS AT -7%
For each position where unrealized_plpc ≤ -0.07:

1. Close position:
   bash scripts/alpaca.sh close SYMBOL
2. Cancel its trailing stop:
   bash scripts/alpaca.sh cancel ORDER_ID
3. Log exit to memory/TRADE-LOG.md:
### YYYY-MM-DD HH:MM — EXIT SYMBOL (STOP)
**Exit Price:** $X.XX
**Realized P&L:** -$X (-7%)
**Reason:** Cut at -7% per rule
**Hold time:** X trading days
**Trade ID:** [matches original entry]

STEP 4 — TIGHTEN STOPS ON WINNERS
For each position where unrealized_plpc > 0:

- If up ≥ +20%: Tighten trail from 10% to 5%
  bash scripts/alpaca.sh cancel OLD_STOP_ORDER_ID
  bash scripts/alpaca.sh order '{"symbol":"SYMBOL","qty":"SHARES","side":"sell","type":"trailing_stop","trail_percent":"5","time_in_force":"gtc"}'
- If up ≥ +15% (but < +20%): Tighten trail from 10% to 7%
  bash scripts/alpaca.sh cancel OLD_STOP_ORDER_ID
  bash scripts/alpaca.sh order '{"symbol":"SYMBOL","qty":"SHARES","side":"sell","type":"trailing_stop","trail_percent":"7","time_in_force":"gtc"}'

Constraints:
- Never tighten within 3% of current price
- Never move a stop down (only closer from above)

Log each stop adjustment:
### YYYY-MM-DD HH:MM — STOP ADJUSTED SYMBOL
**Position:** SHARES @ $ENTRY (now $CURRENT, +X%)
**Old stop:** $X (-10%)
**New stop:** $X (-7%)
**Reason:** Up +15%, tighten per rule

STEP 5 — THESIS CHECK
For each remaining position, validate:
- Is the original catalyst still valid? (check news)
- Is the sector still in momentum or has it rolled over?
- Has technical setup changed (trend flip, support break)?

If thesis broken: Close position immediately, even if not at -7%. Log:
### YYYY-MM-DD HH:MM — EXIT SYMBOL (THESIS)
**Exit Price:** $X.XX
**Realized P&L:** ±$X (±X%)
**Reason:** Catalyst invalidated / sector rolling over / technical break
**Hold time:** X trading days
**Trade ID:** [matches original entry]

STEP 6 — OPTIONAL RESEARCH (Conditional)
If something is moving sharply intraday with no obvious cause, run one WebSearch:
"What is happening with [TICKER] stock today?"

Append findings to memory/RESEARCH-LOG.md as afternoon addendum if material.

STEP 7 — LOG ACTIONS
Update memory/TRADE-LOG.md with all actions (cuts, stop tightens, thesis exits).

STEP 8 — NOTIFICATION
Append to memory/DAILY-SUMMARY.md (local fallback) if ANY action taken:
Midday scan:
- Cut SYMBOL1 at -7% for -$X loss
- Tightened SYMBOL2 stop to 7% (up +18%)
- Thesis exit SYMBOL3 (sector rolling over) for +$X

If no action: silent (no entry needed).

STEP 9 — PORTFOLIO SNAPSHOT
Print current portfolio state:
Midday Portfolio — YYYY-MM-DD HH:MM

Positions: N open
Cash: $X (X%)
Deployed: X%

| SYM | Entry | Now | Unrealized | Stop |

STEP 10 — Verify Files Updated
Confirm memory/TRADE-LOG.md and memory/DAILY-SUMMARY.md appended (if actions taken). No git commits.
```

---

## 6. DAILY SUMMARY

```
You are running the daily summary (EOD) workflow for Alex's Alpaca trading bot.

**CRITICAL REMINDERS:**
1. REMOTE SETUP: git pull origin main at start
2. READ FIRST: memory/TRADE-LOG.md (tail -5 for yesterday's EOD), memory/CONSTRAINTS.md
3. API credentials: ALPACA_API_KEY, ALPACA_SECRET_KEY from environment variables ONLY
4. WRITE AT END: Append to memory/TRADE-LOG.md (EOD snapshot), memory/DAILY-SUMMARY.md
5. REMOTE CLEANUP: git add memory/ && git commit -m "chore: daily summary" && git push origin main

**WORKFLOW:**
Run after market close. Capture portfolio state, compute day P&L, log EOD snapshot, send recap.

STEP 1 — Read Memory
tail -5 memory/TRADE-LOG.md  # Find yesterday's closing equity (needed for day P&L math)
cat memory/CONSTRAINTS.md     # Reference deployment targets

Extract yesterday's closing equity for day-over-day P&L calculation.

STEP 2 — Pull Final Account State
bash scripts/alpaca.sh account
bash scripts/alpaca.sh positions
bash scripts/alpaca.sh orders

Capture: today's closing equity, cash, all positions with current prices.

STEP 3 — Compute Metrics
Day P&L:
- Day P&L $ = today_equity - yesterday_equity
- Day P&L % = (Day P&L $) / yesterday_equity

Phase cumulative P&L:
- Phase P&L $ = today_equity - starting_equity ($100,000)
- Phase P&L % = (Phase P&L $) / starting_equity

Trade counts:
- Trades today = count today's entries in TRADE-LOG
- Trades this week = count Mon-today entries in TRADE-LOG

Deployment:
- Cash % = (cash / equity) × 100
- Deployed % = 100% - cash %

STEP 4 — Append EOD Snapshot to memory/TRADE-LOG.md
### MMM DD — EOD Snapshot (Day N, Weekday)

**Portfolio:** $X | **Cash:** $X (X%) | **Day P&L:** ±$X (±X%) | **Phase P&L:** ±$X (±X%) | **Deployed:** X%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| SYM1 | N | $X | $X | ±$X (±X%) | $X | X days |
| SYM2 | N | $X | $X | ±$X (±X%) | $X | X days |

**Trades today:** [list or "none"]

**Notes:** [one-paragraph summary of day — what worked, what didn't, any learnings]

STEP 5 — Append to memory/DAILY-SUMMARY.md
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

STEP 6 — Print EOD Summary
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

STEP 7 — Circuit Breaker Check
- If day P&L ≤ -2% of equity: Log "Daily loss limit hit. No trading tomorrow."
- If phase P&L ≤ -5% of equity: Log "Weekly loss limit hit. Pause for review."
- If max drawdown ≥ -15% from peak: Log "Max drawdown hit. HALT. Manual restart only."

STEP 8 — Verify Files Updated
Confirm memory/TRADE-LOG.md and memory/DAILY-SUMMARY.md appended. No git commits (local testing).
```

---

## 7. WEEKLY REVIEW

```
You are running the weekly review workflow for Alex's Alpaca trading bot.

**CRITICAL REMINDERS:**
1. REMOTE SETUP: git pull origin main at start
2. READ FIRST: memory/TRADING-STRATEGY.md, memory/CONSTRAINTS.md, memory/TRADE-LOG.md, memory/RESEARCH-LOG.md, memory/WEEKLY-REVIEW.md
3. API credentials: None needed for WebSearch queries (Claude built-in)
4. WRITE AT END: Append to memory/WEEKLY-REVIEW.md, memory/DAILY-SUMMARY.md (recap)
5. REMOTE CLEANUP: git add memory/ && git commit -m "chore: weekly review" && git push origin main

**WORKFLOW:**
Run Friday after market close. Compute week stats, grade performance, review strategy adjustments.

STEP 1 — Read Memory
cat memory/TRADING-STRATEGY.md
cat memory/CONSTRAINTS.md
grep -A 500 "## Week ending" memory/WEEKLY-REVIEW.md | head -50  # Last week's review
grep "## [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]" memory/TRADE-LOG.md | tail -20  # This week's entries
grep "## [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]" memory/RESEARCH-LOG.md | tail -10  # This week's research

Understand the week's trades, research, and context.

STEP 2 — Pull Week-End Account State
bash scripts/alpaca.sh account
bash scripts/alpaca.sh positions

Capture: ending equity, cash, open positions.

STEP 3 — Compute Week Stats
From TRADE-LOG:
- Starting equity (Monday AM)
- Ending equity (Friday close)
- Week return $ and %
- All closed trades (entry, exit, P&L for each)
- Win count, loss count, open trade count
- Win rate (closed only)
- Best trade P&L
- Worst trade P&L
- Profit factor = (sum of wins) / |sum of losses|

From market data (WebSearch):
Query: "S&P 500 weekly performance for week ending YYYY-MM-DD"

Extract S&P 500 week return %, then compute: Bot vs S&P = Week return % - S&P return %.

Position data:
- Max intraweek drawdown
- Current open positions + unrealized P&L

STEP 4 — Append Full Review to memory/WEEKLY-REVIEW.md
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

STEP 5 — Strategy Adjustments (Conditional)
If a rule has worked consistently for 2+ weeks OR failed badly (significant losing streak in one signal):

- Update memory/TRADING-STRATEGY.md to reflect change
- Document the change in the weekly review ("Updated: RSI threshold from 30 to 35 based on 2-week trial")
- Log decision to decisions/log.md (if using git): [YYYY-MM-DD] DECISION: update RSI threshold | REASONING: improved win rate | CONTEXT: 2-week backtest

STEP 6 — Send Weekly Recap
Append to memory/DAILY-SUMMARY.md:

## WEEK ENDING YYYY-MM-DD — WEEKLY RECAP

**Portfolio:** $X (±X% week, ±X% phase)
vs S&P 500: ±X%

**Trades:** N (W:X / L:Y / open:Z)
**Win rate:** X% | **Best:** SYM +X% | **Worst:** SYM -X%

**Key win:** [one sentence on best strategy this week]
**Lesson learned:** [one sentence on adjustment for next week]
**Grade:** X

---

STEP 7 — Print Summary
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

STEP 8 — Verify Files Updated
Confirm memory/WEEKLY-REVIEW.md and memory/DAILY-SUMMARY.md appended. No git commits (local testing).
```

---

## Usage Notes

- Copy any prompt above and paste into a fresh Claude Code session
- Each prompt is self-contained (no prior context needed)
- Environment variables (ALPACA_API_KEY, ALPACA_SECRET_KEY, GEMINI_API_KEY) must be set before running
- All file writes use `memory/` paths (persistent across sessions)
- No `git commit` commands — local testing only
