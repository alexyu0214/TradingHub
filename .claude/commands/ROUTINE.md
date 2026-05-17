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
tail -30 memory/TRADE-LOG.md    # Last EOD snapshot + recent trades
tail -50 memory/RESEARCH-LOG.md # Previous day's research + addendums

Parse strategy rules, review any open positions and their thesis, note any sector momentum from yesterday.

STEP 1b — Prior-Week Adjustment Audit (MONDAY ONLY — skip on Tue–Fri)
If today is Monday, also pull last weekly review's adjustments and check off implementation status. This is the operational accountability loop:

```
grep -A 100 "^### Adjustments for Next Week" memory/WEEKLY-REVIEW.md | tail -100
```

For each adjustment listed in that block, verify whether it's built into code:
- Workflows / cron schedules → check `ls .github/workflows/`
- Prompt-level changes → grep keywords in `.claude/commands/ROUTINE.md`
- Constraint changes → grep keywords in `memory/CONSTRAINTS.md` and `memory/TRADING-STRATEGY.md`
- Script changes → grep keywords in `scripts/run_workflow.py` and `scripts/send_report.py`

Add to today's research log entry an **"Adjustment Audit"** subsection:

```
### Adjustment Audit (from week-N weekly review)
- [adjustment text]: ✅ IMPLEMENTED — evidence: [file/line/grep result]
- [adjustment text]: ❌ NOT IMPLEMENTED — needs build
- [adjustment text]: 🟡 IMPLEMENTED IN CODE BUT NOT TRIGGERED — calibration issue, not missing feature
```

If any item is ❌, escalate by adding a "URGENT: build [adjustment]" line at top of today's research output so it surfaces in the daily PDF.

This forces the bot to confront reality once a week and prevents the loop where weekly reviews keep complaining about adjustments that already exist.

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

STEP 4 — Classify VIX Regime (NEW — Quant Layer)
Pull current VIX level (from research in STEP 3). Classify per TRADING-STRATEGY.md:
- VIX < 14 → Calm trending  (sizing 1.00×)
- VIX 14–22 → Normal       (sizing 1.00×)
- VIX 22–30 → Elevated     (sizing 0.75×, mean-reversion preferred)
- VIX > 30 → Crisis        (sizing 0.50× OR PAUSE — bot's choice)

Record this regime classification — it gates entry sizing for all ideas today.

STEP 5 — Universe Scan & Idea Generation (LONG + SHORT)
Scan both sides of the market:
- **Long candidates:** trending leaders with positive catalysts (Russell 1000 mid-caps, sector ETFs > $1B AUM, ADR mega-caps)
- **Short candidates** (Phase 1 enabled, conservative caps): mega-caps (mkt cap > $20B) and sector/index ETFs ONLY — failed leadership, broken support, negative catalyst. NO mid-caps, NO high-momentum names, NO recent IPOs.

All universe filters retained: mkt cap > $2B (longs) / $20B (shorts), ADV > 1M shares, price > $5.

Identify up to **3 long candidates** and up to **2 short candidates** with documented catalysts. For EACH candidate, run BOTH layers:

**Layer A — Catalyst + Trend Template checklist:**
- TICKER, intended direction (LONG or SHORT), sector
- Catalyst (specific reason for trade today)
- Sector posture matches direction (long: in momentum; short: rolling over)
- RSI(14) in zone (matches selected lane)
- Volume confirm (entry day vs 20-day avg)
- Stop level (7–10% from entry; long stop below, short stop above)
- Target (≥ 2:1 R:R) and computed **R_dollars / R_pct / target_R** per CONSTRAINTS.md
- **Minervini Trend Template passes** for the candidate's direction:
  - Pull extended bars: `bash scripts/alpaca.sh bars TICKER 210` (need 200-SMA + 1-month buffer)
  - Compute 50-day, 150-day, 200-day SMAs
  - Verify ALL trend template conditions (long or short version per TRADING-STRATEGY.md "Minervini Trend Template")
  - Compute distance from 52-week high and 52-week low
  - Compute 6-month return percentile (vs ~500 universe sample)
  - REJECT if any trend template condition fails

**Layer B — Quant checklist (TWO LANES — either qualifies):**
For each candidate, run:
```
bash scripts/alpaca.sh bars TICKER 25
```
From the returned closes, compute:
- mean_20 = average of last 20 closes
- stddev_20 = standard deviation of last 20 closes
- max_20 = max of last 20 closes (for breakout test)
- z_score = (current_price − mean_20) / stddev_20
- 50-day SMA and 200-day SMA (use additional bars call if needed: `bars TICKER 210`)

**Decide which lane to evaluate per candidate based on catalyst type:**
- "Panic selloff," "post-earnings overreaction," "deeply oversold" → **Mean-Reversion Lane**
- "Earnings beat + uptrend continuation," "breakout from base," "sector momentum" → **Momentum Lane**

**Lane 2a-LONG — Mean-Reversion Long:**
- Z ≤ −2.0 ✓ + RSI < 30 ✓ + volume ≥ 1.0× 20d avg ✓

**Lane 2a-SHORT — Mean-Reversion Short:**
- Z ≥ +2.0 ✓ + RSI > 70 ✓ + volume ≥ 1.0× 20d avg ✓

**Lane 2b-LONG — Momentum Long:**
- Z ≥ +1.0 ✓ + close > prior 20d high ✓ + RSI 50-70 ✓ + volume ≥ 1.5× 20d avg ✓ + 50d SMA > 200d SMA ✓
- **Pivot extension check:** intended limit ≤ pivot (20d high) × 1.05. Reject if chasing > 5% above pivot.

**Lane 2b-SHORT — Momentum Short:**
- Z ≤ −1.0 ✓ + close < prior 20d low ✓ + RSI 30-50 ✓ + volume ≥ 1.5× 20d avg ✓ + 50d SMA < 200d SMA ✓
- **Pivot extension check:** intended limit ≥ pivot (20d low) × 0.95. Reject if chasing > 5% below pivot.

**Then identify the sector PAIR** (e.g., XOM↔CVX, NVDA↔AVGO, JPM↔GS — see TRADING-STRATEGY.md "Quant Layer" §5 for the canonical pairs list, or pick best correlated peer if not listed). Run `bash scripts/alpaca.sh bars PAIR 25` and compute its z_score too.

**For the candidate to qualify Layer B:**
- One of Lane 2a OR Lane 2b passes — REQUIRED (record which one)
- Pair Z-Score divergence ≤ 1.5σ — REQUIRED
- VIX regime allows new entries — REQUIRED

If neither lane passes → SKIP that candidate. Log which lane was attempted and which check failed. Patience rule still applies — zero trades today is correct if nothing clears both layers.

**EVALUATE EACH CANDIDATE INDEPENDENTLY.** Do NOT write chain dependencies like "enter B only if A fills" or label ideas primary/secondary/tertiary. Every candidate stands on its own Layer A + Layer B result. The ONLY cross-position check is cash-headroom at execution time (see CONSTRAINTS.md "Conditional Gate Independence"). Historically, gating secondary names on XOM's fill is exactly why no non-XOM trade ever executed — each idea must be free to qualify on its own.

STEP 6 — Compute Position Sizing (Kelly + Regime)
For each surviving candidate (cleared both layers), compute size per CONSTRAINTS.md "Quant Sizing":
- Until ≥ 30 closed trades exist: default to 10% per position
- Apply VIX multiplier (1.00 / 0.75 / 0.50)
- Hard cap 20%, floor 5%

STEP 7 — Write Research Log Entry
Append a new dated entry to memory/RESEARCH-LOG.md:

## YYYY-MM-DD — Pre-market Research

### Account
- Equity: $X
- Cash: $X (X%)
- Buying power: $X
- Daytrade count: N/3

### Market Context
[paste research from Step 3, bulleted]

### VIX Regime
- Current VIX: X.X
- Regime: [Calm/Normal/Elevated/Crisis]
- Sizing multiplier: 1.00× / 0.75× / 0.50×

### Trade Ideas (Cleared Both Layers)
For each qualifying idea:
- TICKER | **DIRECTION (LONG/SHORT)** | Lane (2a-Long / 2a-Short / 2b-Long / 2b-Short) | Catalyst | Entry | Stop | Target | R:R
- Z-Score: X.XX (vs 20-day mean $X)
- Trend Template: PASS (list specific values: 50/150/200 SMAs, distance from 52w high/low, 6mo percentile)
- Pair: PAIR_TICKER | Pair Z-Score: X.XX | Divergence: X.Xσ
- Sized position: X% of equity ($X) — **shorts capped at 10% per position, 30% total short exposure**
- **R-Multiple:** R_dollars $XX (X.X% of equity) | Target R = X.XR | R:R verified ≥ 2:1
- Pivot extension (momentum lanes only): pivot $X.XX, limit $X.XX, extension X.X% (≤5% required)

### Skipped Candidates
List candidates that failed Layer A or Layer B with the specific failed check.

### Risk Factors
[any major risks today?]

### Decision
TRADE or HOLD

STEP 8 — Print Summary to User
Print the research log entry to stdout. Highlight any action items.

STEP 9 — Verify Files Updated
Confirm memory/RESEARCH-LOG.md has been appended. Git commit/push handled by workflow.
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
Place bracket LIMIT BUY orders at the bot's intended entry prices for each pre-market trade idea. Bracket includes attached stop-loss and take-profit. NEVER use market orders for entries. If price never reaches the limit, the order expires unfilled at session close — that's correct behavior.

STEP 1 — Read Today's Research
grep -A 200 "^## $(date +%Y-%m-%d)" memory/RESEARCH-LOG.md

Pull today's trade ideas (if any) and confirm DECISION was TRADE (not HOLD).
Extract for each idea: TICKER, intended limit price (research entry), stop_price, take_profit, sized_qty.

STEP 2 — Re-Validate with Live Quotes
For each planned trade from research:
bash scripts/alpaca.sh quote SYMBOL
bash scripts/alpaca.sh account  # Check current positions count, cash, daytrade count

- Verify SYMBOL hasn't been halted or delisted (quote returns valid)
- Note current price vs research limit (just informational — we're NOT chasing if it's gapped past)

STEP 3 — Run Buy-Side Gate on Each Planned Trade
Use memory/CONSTRAINTS.md checklist (Layer A 1-10 + Layer B 11-13):
- Total positions after fill ≤ 6
- Trades this week (including this) ≤ 3
- Position cost (qty × limit_price) ≤ Kelly-sized limit
- Position cost ≤ available cash
- PDT rules allow
- Catalyst still valid (re-read news if big news hit overnight)
- Z-Score still qualifies (re-pull bars if needed)
- VIX regime allows entry

If any check fails: Skip that trade. Log the reason and move on.

STEP 4 — Place Bracket Limit Orders (NOT MARKET ORDERS)
For each approved trade, construct bracket limit order matching the direction (long or short).

**LONG ENTRY** — buy-to-open with bracket:
- limit_price = research-derived intended entry
- stop_loss.stop_price = 7-10% BELOW limit (or technical support)
- take_profit.limit_price = research-derived target ABOVE limit
- side = "buy"

bash scripts/alpaca.sh order '{
  "symbol":"SYMBOL",
  "qty":"SHARES",
  "side":"buy",
  "type":"limit",
  "time_in_force":"day",
  "limit_price":"X.XX",
  "order_class":"bracket",
  "take_profit":{"limit_price":"Y.YY"},
  "stop_loss":{"stop_price":"Z.ZZ"}
}'

**SHORT ENTRY** — sell-to-open with bracket (Phase 1 enabled, capped at 10% position size):
- limit_price = research-derived intended entry (sell short here)
- stop_loss.stop_price = 7-10% ABOVE limit (covers the short if price rises)
- take_profit.limit_price = research-derived target BELOW limit (buy-to-close at profit)
- side = "sell"

bash scripts/alpaca.sh order '{
  "symbol":"SYMBOL",
  "qty":"SHARES",
  "side":"sell",
  "type":"limit",
  "time_in_force":"day",
  "limit_price":"X.XX",
  "order_class":"bracket",
  "take_profit":{"limit_price":"Y.YY (BELOW limit_price)"},
  "stop_loss":{"stop_price":"Z.ZZ (ABOVE limit_price)"}
}'

**Pre-flight check before placing any short:**
1. Confirm symbol is shortable: check `bash scripts/alpaca.sh quote SYMBOL` returns valid; if Alpaca rejects with `htb` (hard-to-borrow) → SKIP and log
2. Verify total short exposure after this fill ≤ 30% of equity
3. Verify this short ≤ 10% of equity (per-short cap)
4. Confirm no earnings within next 7 trading days (skip shorts through earnings)
5. Confirm candidate did NOT have a >5% gap-down in last 24h (squeeze risk)

Capture: order ID, status (should be "new" or "accepted"). If rejected: log reason, do NOT fall back to a market order.

STEP 5 — DO NOT Place Trailing Stop Yet
The bracket already has a fixed stop attached. Trailing-stop upgrade happens in midday/afternoon-scan workflows AFTER fill is confirmed. Don't try to place a separate trailing stop here — Alpaca will reject it as a duplicate.

STEP 6 — Log Each Order to memory/TRADE-LOG.md

### YYYY-MM-DD HH:MM — LIMIT [BUY/SELL-SHORT] ORDER PLACED: SYMBOL
**Direction:** LONG or SHORT
**Lane:** 2a-Long / 2a-Short / 2b-Long / 2b-Short
**Catalyst:** [from research]
**Limit Price:** $X.XX (SHARES shares, day order)
**Stop (bracket child):** $Z.ZZ ([below for long, above for short])
**Take-Profit (bracket child):** $Y.YY ([above for long, below for short])
**R-Multiple:** R_dollars $XX (X.X% equity) | Target R = X.XR
**R:R:** X.X:1 (must be ≥ 2.0)
**Trend Template:** PASS (50/150/200 SMA: $X/$Y/$Z aligned; 52w high $X distance Y%; 6mo pct Z)
**Thesis:** [copied from research log]
**Order ID:** [from Alpaca response]
**Status:** Placed (awaiting fill)

When the bracket fills (caught by midday or afternoon-scan workflow), append a separate entry:

### YYYY-MM-DD HH:MM — BRACKET FILLED: SYMBOL
**Fill Price:** $X.XX (SHARES shares)
**Stop now active:** $Z.ZZ
**Target now active:** $Y.YY
**Order ID:** [matches placement]

STEP 7 — Append to memory/DAILY-SUMMARY.md
Market-open orders placed:
- SYMBOL1: limit $X.XX (SHARES shares), stop $Z.ZZ, target $Y.YY
- SYMBOL2: limit $X.XX (SHARES shares), stop $Z.ZZ, target $Y.YY
(or "No orders placed")

STEP 8 — Print Summary
Market-Open Execution — YYYY-MM-DD

Bracket limit orders placed:
  SYMBOL1: $X.XX limit (qty N), stop $Z.ZZ, target $Y.YY
  SYMBOL2: $X.XX limit (qty N), stop $Z.ZZ, target $Y.YY

Skipped:
  SYMBOL3: Z-Score no longer qualifies after re-check
  SYMBOL4: Insufficient cash
  SYMBOL5: Catalyst invalidated overnight

These orders fill IF price reaches limit during today's session. Unfilled orders expire at close.

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

## 5b. MIDDAY-RESCAN (Spread-Normalization Check)

```
You are running the midday-rescan workflow for Alex's Alpaca trading bot.

**PURPOSE:** ~1 hour after market open, re-evaluate any candidates that were skipped at market-open due to wide spreads, gap-chase risk, or pre-open price stale. Spreads typically normalize within 30–60 minutes of the open.

**CRITICAL REMINDERS:**
1. REMOTE SETUP: git pull origin main at start
2. READ FIRST: memory/RESEARCH-LOG.md (today's entry — Trade Ideas + Skipped Candidates), memory/CONSTRAINTS.md, memory/TRADING-STRATEGY.md
3. API credentials: ALPACA_API_KEY, ALPACA_SECRET_KEY from environment variables ONLY
4. WRITE AT END: append to memory/RESEARCH-LOG.md (rescan addendum) and, if a trade fires, memory/TRADE-LOG.md
5. REMOTE CLEANUP: git add memory/ && git commit -m "chore: midday-rescan" && git push origin main

**WORKFLOW:**

STEP 1 — Pull Today's Research
grep -A 200 "^## $(date +%Y-%m-%d)" memory/RESEARCH-LOG.md

Extract:
- The "Skipped Candidates" list from this morning
- Why each was skipped (wide spread, gap-chase, stale price)
- VIX regime classification for today

STEP 2 — Pull Live Quotes for Each Skipped Candidate
For each skipped ticker:
bash scripts/alpaca.sh quote SYMBOL

Compute current bid/ask spread %.

STEP 3 — Re-check Quant Layer
For each ticker that now has acceptable spread (< 1% for liquids):
bash scripts/alpaca.sh bars SYMBOL 25

Recompute Z-Score with the latest current_price. Same gates:
- Z-Score |≥ 2.0|
- Pair Z-Score divergence ≤ 1.5σ
- VIX regime allows entry

STEP 4 — Re-check Catalyst (Quick)
- Catalyst from this morning still valid? (no offsetting news in last hour?)
- Sector still in momentum?
- Position count + weekly trade count still allow this trade?

STEP 5 — Execute If All Layers Re-Clear
If ALL of Layer A + Layer B re-clear:
1. Compute Kelly + VIX-adjusted size (CONSTRAINTS.md)
2. Place market buy order:
   bash scripts/alpaca.sh order '{"symbol":"SYM","qty":"N","side":"buy","type":"market","time_in_force":"day"}'
3. Wait for fill, capture fill price + order ID
4. Place 10% trailing stop GTC
5. Log to memory/TRADE-LOG.md with full thesis from morning research

STEP 6 — Append Rescan Addendum to memory/RESEARCH-LOG.md

### YYYY-MM-DD — Midday Rescan Addendum (HH:MM)

**Skipped at open, re-evaluated:**
- TICKER1: now spread X%, Z-Score Y.Y → [QUALIFIED / STILL SKIPPED + reason]
- TICKER2: ...

**Trades fired this rescan:**
- TICKER: bought N @ $X, stop $Y (or "none")

**Patience rule:** If nothing re-clears, this is correct. Do NOT lower entry gates to force a trade.

STEP 7 — Print Summary
Midday Rescan — YYYY-MM-DD HH:MM

Re-evaluated: N candidates from morning skip list
Qualified after re-check: N
Executed: N
Still skipped: N (reasons: ...)

Portfolio now: N positions, X% deployed

STEP 8 — Verify Files Updated
Confirm memory/RESEARCH-LOG.md addendum and (if trade fired) memory/TRADE-LOG.md updated.
```

---

## 5c. AFTERNOON-SCAN (Last-2-Hours Opportunity Check)

```
You are running the afternoon-scan workflow for Alex's Alpaca trading bot.

**PURPOSE:** ~2 hours before market close. Three jobs: (1) check if morning bracket limits filled, (2) upgrade fixed stops to trailing on profitable filled positions, (3) scan for last-2-hours setups (post-lunch momentum, late-day catalysts).

**CRITICAL REMINDERS:**
1. REMOTE SETUP: git pull origin main at start
2. READ FIRST: memory/RESEARCH-LOG.md (today's entry), memory/TRADE-LOG.md (today's orders), memory/CONSTRAINTS.md, memory/TRADING-STRATEGY.md
3. API credentials: ALPACA_API_KEY, ALPACA_SECRET_KEY from environment variables ONLY
4. WRITE AT END: append to memory/RESEARCH-LOG.md (afternoon addendum), memory/TRADE-LOG.md (any fills/upgrades)
5. REMOTE CLEANUP: git add memory/ && git commit -m "chore: afternoon-scan" && git push origin main

**WORKFLOW:**

STEP 1 — Pull Order & Position State
bash scripts/alpaca.sh orders all  # all orders today
bash scripts/alpaca.sh positions
bash scripts/alpaca.sh account

Compare against today's TRADE-LOG entries: which limit orders filled? Which still open?

STEP 2 — Trailing Stop Upgrades on Profitable Fills
For each filled position where unrealized_plpc > 0:
  - If position has a fixed stop_loss from the bracket: cancel it, replace with 10% trailing GTC
  - Use the existing midday tightening rules: at +15% tighten to 7%, at +20% tighten to 5%
  - Constraints from TRADING-STRATEGY.md still apply (never within 3% of current price, never move down)

For each filled position where unrealized_plpc ≤ 0: leave the bracket stop in place.

STEP 3 — Cancel Stale Unfilled Limits (Optional)
If a morning limit order has been sitting unfilled and the underlying catalyst has weakened (check via quick news scan):
  - Cancel: bash scripts/alpaca.sh cancel ORDER_ID
  - Log reason

If catalyst still valid → leave order alone, it expires at close anyway.

STEP 4 — Afternoon Opportunity Scan (Quant + Catalyst)
Look for late-day setups that emerged AFTER pre-market research:
  - Surprise news / earnings announcements during today's session
  - Sector rotation visible in afternoon tape
  - Tickers near key technical levels approaching close

For ANY candidate, run BOTH layers (catalyst + quant), same gates as pre-market:
  - bash scripts/alpaca.sh quote SYMBOL
  - bash scripts/alpaca.sh bars SYMBOL 25 (compute Z-Score)
  - identify pair, compute pair Z-Score
  - VIX still in allowed regime?

If a candidate clears Layer A + Layer B AND weekly trade count + position count allow:
  - Place bracket limit order (same structure as market-open STEP 4)
  - Limit price = current market or slightly below (afternoon entries typically don't get the same pullback room as morning)
  - Time-in-force = day (will fill before close or expire)

STEP 5 — Append to memory/RESEARCH-LOG.md

### YYYY-MM-DD — Afternoon Scan Addendum (HH:MM)

**Bracket fills today:** [list any limits that filled, with fill price]
**Stops upgraded:** [list trailing-stop replacements]
**Stale limits cancelled:** [list, with reasons]
**New afternoon entries:** [list new bracket orders placed, or "none"]
**Afternoon market context:** [1-2 lines on what shifted since morning]

STEP 6 — Append to memory/TRADE-LOG.md
For each new entry, fill, or stop upgrade, log per existing format (BRACKET FILLED, STOP UPGRADED, etc.).

STEP 7 — Print Summary
Afternoon Scan — YYYY-MM-DD HH:MM

Bracket fills since open: N
Trailing stops upgraded: N
Stale limits cancelled: N
New afternoon entries: N

Portfolio now: X positions, Y% deployed
Open bracket limits remaining: N

STEP 8 — Verify Files Updated
Confirm memory/RESEARCH-LOG.md addendum and memory/TRADE-LOG.md updates committed.
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

STEP 5 — Append EOD entry to memory/DAILY-SUMMARY.md (MANDATORY — DO NOT SKIP)

**THIS IS NOT OPTIONAL.** Append the entry below EVEN IF: no trades happened today, no positions are open, the market was closed, the workflow re-ran and an entry already exists, OR nothing notable occurred. The PDF report parser depends on this entry existing. If it's missing for today, tomorrow's daily PDF will show empty KPIs.

Format (use **exactly** this structure — the parser regex relies on it):

## YYYY-MM-DD — EOD

**Portfolio:** $X (±X% day, ±X% phase)
**Cash:** $X (X%)
**Deployed:** X%
**Daytrade count:** N/3

**Trades today:** [list with entry/exit prices or "none"]
**Open positions:** [SYM1 ±X%, SYM2 ±X%, etc. or "none"]
**Stops tightened:** [if any]
**Losers cut:** [if any]

**Notes:** [one-liner summary — required, even if just "Flat day, no activity, all rules clear."]

---

**Append-not-replace rule:** Use `>>` redirection or write_file with mode='a'. NEVER overwrite the entire file. Always append to the end so historical entries remain intact.

**Verify after writing:** Run `tail -5 memory/DAILY-SUMMARY.md` to confirm today's entry exists at the end of the file. If you see yesterday's date at the tail, something failed — retry the write.

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

STEP 1 — Read Memory (anchored greps so headings only, not text containing "##")
cat memory/TRADING-STRATEGY.md
cat memory/CONSTRAINTS.md
grep -A 500 "^## Week ending" memory/WEEKLY-REVIEW.md | head -120  # Last weekly review (full section)
grep -E "^### [0-9]{4}-[0-9]{2}-[0-9]{2}" memory/TRADE-LOG.md | tail -30  # This week's TRADE entries (### prefix)
grep -E "^### [A-Z][a-z]{2} [0-9]{1,2}" memory/TRADE-LOG.md | tail -10  # This week's EOD snapshots (### MMM DD prefix)
grep -E "^## 20[0-9]{2}-[0-9]{2}-[0-9]{2}" memory/RESEARCH-LOG.md | tail -20  # This week's research entries (## prefix)

Also pull the actual content of the latest TRADE-LOG entries (not just headers) so you can see fills, exits, P&L:
tail -200 memory/TRADE-LOG.md

And the latest research narrative:
tail -200 memory/RESEARCH-LOG.md

Understand the week's trades, research, and context. **Do not invent data — if a trade exit (e.g., XOM thesis-break) is in TRADE-LOG, it MUST appear in this weekly review.**

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

STEP 5a — Implementation Audit (every weekly review)
**Critical: before claiming an adjustment was "not implemented," VERIFY by reading actual code/config files.** The bot has historically generated false alarms (e.g., "midday re-scan was never built") when the workflow file objectively existed. To prevent this:

1. Read each prior-week adjustment from the previous weekly review section.
2. For each adjustment, perform a verification check by inspecting the codebase:
   - "Implement midday re-scan" → verify `.github/workflows/midday-rescan.yml` exists AND there's a "5b. MIDDAY-RESCAN" section in `.claude/commands/ROUTINE.md`. Use:
     `ls .github/workflows/ && grep -c "5b. MIDDAY-RESCAN" .claude/commands/ROUTINE.md`
   - "Pre-open live-quote check" → grep for "Re-Validate with Live Quotes" in market-open prompt
   - "Decoupled conditional gates" → grep "cash-headroom" in CONSTRAINTS.md
   - "Z-Score / Trend Template / R-multiple" → grep these terms in CONSTRAINTS.md and TRADING-STRATEGY.md
   - "Bracket limit orders" → grep "order_class.*bracket" in ROUTINE.md
   - "Shorts framework" → grep "Mean-Reversion Short" in TRADING-STRATEGY.md
   - For any other adjustment: grep relevant keywords in `.claude/commands/ROUTINE.md`, `memory/CONSTRAINTS.md`, `memory/TRADING-STRATEGY.md`, `.github/workflows/`, and `scripts/`

3. Append an **Implementation Audit** subsection BEFORE the "What Worked" section:

```
### Implementation Audit (auto-verified against codebase)

| Prior Adjustment | Built into code? | Evidence |
|------------------|------------------|----------|
| Midday re-scan | ✅ YES | .github/workflows/midday-rescan.yml exists; ROUTINE.md has section 5b |
| Pre-open quote check | ✅ YES | market-open prompt STEP 2 |
| Decoupled gates | ✅ YES | CONSTRAINTS.md gate 11 (4 lanes, no chain dependencies) |
| ... | | |

**False alarms this week:** [list any "What Didn't Work" / "Adjustments" items that referenced missing features that ACTUALLY exist in code. Be specific so the bot stops complaining about already-built features.]
```

4. **Important behavioral rule:** If an adjustment IS built into code but the BOT's behavior didn't reflect it (e.g., midday-rescan workflow exists but bot rejected all candidates inside it), classify the gap as a **decision/calibration issue**, not an "unimplemented" issue. Different problem class, different remedy.

5. After audit completes, the "What Didn't Work" and "Adjustments for Next Week" sections must reflect ONLY genuine unimplemented items or genuine new ideas — not falsely claim things are missing.

STEP 5b — Phase Review Check (Every 3 Weeks)
Read decisions/log.md and find the most recent "PHASE REVIEW" entry. If today's date is ≥ 21 days after that date (or no prior PHASE REVIEW exists and today is ≥ 21 days after Phase 1 launch on 2026-05-01), append a Phase Audit subsection to this week's review:

### Phase Audit (3-Week Review)

**Phase status:** Phase [N] active since [date]. Today is Day [N] of phase.

**1. Strategy efficacy:** Is the current quant + catalyst combo producing edge? (Win rate, profit factor, Sharpe vs S&P 500 over the 3-week window.)

**2. Backlog promotions:** What items in the strategy backlog should move to active development?

**3. Stale adjustments:** Which adjustments have appeared on weekly review lists 3+ times unimplemented? Promote each to a concrete coding task.

**4. Cost vs alpha:** Estimated API spend last 3 weeks vs realized P&L. Justified?

**5. Phase gate progress:** Distance to ≥30 closed trades · Sharpe ≥ 1.5 · max drawdown ≤ 15%.

**6. Recommended next-phase focus (1-2 items):** What one or two changes should we prioritize in the next 3-week window?

After writing the phase audit, append to decisions/log.md:
[YYYY-MM-DD] PHASE REVIEW: completed 3-week audit | KEY FINDING: <one-sentence summary> | NEXT REVIEW DUE: [today + 21 days]

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
