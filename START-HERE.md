# Quick Start — Trading Bot Phase 1 (Local Testing)

You now have a fully wired trading bot ready for local testing on Alpaca paper.

---

## Step 1 — Configure Alpaca Credentials (One-Time)

1. Go to [Alpaca Account Settings](https://app.alpaca.markets/paper/settings/api)
2. Copy your **API Key** and **Secret Key** (for paper trading)
3. Create a local `.env` file in the root directory:
   ```bash
   cp .env.template .env
   ```
4. Edit `.env` and paste your credentials:
   ```bash
   ALPACA_API_KEY=your_key_here
   ALPACA_SECRET_KEY=your_secret_here
   ```
5. **NEVER commit .env.** (It's in .gitignore. If you accidentally see it in a commit, rotate keys immediately.)

---

## Step 2 — Test the Alpaca Wrapper

```bash
bash scripts/alpaca.sh account
```

**Expected output:** JSON with your paper account details (equity, cash, buying_power, etc.)

If you get an error like `ALPACA_API_KEY not set in environment`, check that:
- `.env` file exists in the root directory
- Credentials are filled in (not placeholder text)
- No typos in the key names

Once this works, you're connected.

---

## Step 3 — Review Memory Files

Open and scan these in order:

1. **`memory/TRADING-STRATEGY.md`** — Your trading rules, entry signals, exit rules
2. **`memory/CONSTRAINTS.md`** — Hard constraints (position sizing, stops, circuit breakers)
3. **`memory/TRADE-LOG.md`** — Trade journal (starts at Day 0 baseline)
4. **`memory/RESEARCH-LOG.md`** — Daily research template

These are the "brain" of the bot. Every local command reads these first.

---

## Step 4 — Run Your First Workflow (No Real Trades)

### Morning: Pre-market Research

```bash
/pre-market
```

This will:
- Read your strategy and current positions
- Research the market (oil, S&P 500 futures, VIX, top catalysts, sector momentum)
- Generate 2–3 trade ideas (or 0 if no edge)
- Write a research log entry to `memory/RESEARCH-LOG.md`
- Print the research to the screen

**Example output:**
```
## 2026-05-01 — Pre-market Research

### Account
Equity: $100,000
Cash: $100,000 (100%)
...

### Trade Ideas
1. SPY — Fed dovish signal, RSI < 30 in uptrend...

### Decision
TRADE
```

---

### Market Open: Check Portfolio Status

```bash
/portfolio
```

Clean snapshot of account (no trades placed yet).

Expected:
```
Portfolio Snapshot — 2026-05-01

Equity: $100,000 | Cash: $100,000 (100%) | Daytrade count: 0/3

Positions: 0 open
Open Orders: none
```

---

### Market Open: Validate & Execute (If Edge Exists)

If `/pre-market` found a trade idea (TRADE decision), now validate it:

```bash
/trade SPY 10 buy
```

Replace `SPY` and `10` with your ticker and share count from the research.

**What happens:**
1. Bot validates all rules (position limit, cash, catalyst, etc.)
2. Prints the rule checks
3. Asks "Execute? (y/n)"
4. On `y`: places market order + 10% trailing stop
5. Logs trade to `memory/TRADE-LOG.md`

**Example:**
```
✓ Total positions after: 1/6
✓ Trades this week: 1/3
✓ Position cost: 5% of equity
✓ Cash available: yes
✓ Catalyst documented: yes

Execute? (y/n)
```

Type `y` to proceed, `n` to cancel.

---

### Midday: Scan Positions

```bash
/midday
```

If positions are open, this will:
- Cut any losers at -7%
- Tighten stops on winners (+15% → 7% trail, +20% → 5% trail)
- Check thesis validity

---

### Market Close: Daily Summary

```bash
/daily-summary
```

Snapshot your portfolio, compute day P&L, log EOD entry.

Appends to `memory/TRADE-LOG.md` and `DAILY-SUMMARY.md`.

---

### Friday: Weekly Review

```bash
/weekly-review
```

Compute weekly stats, grade performance, plan next week.

---

## Step 5 — Smoke Test Cycle (No Real Trades)

Do a full day without trading to validate the workflow:

1. **Morning:** `/pre-market` (research only, no trade ideas if you're conservative)
2. **9:40am:** `/portfolio` (snapshot)
3. **Noon:** `/midday` (no-op, no positions yet)
4. **3:30pm:** `/daily-summary` (EOD log)

**Expected:** All commands complete without errors. Memory files are readable. No trades placed (yet).

---

## Step 6 — First Real Trade (Conditional)

Once smoke test passes and `/pre-market` identifies a legitimate edge:

1. Run `/pre-market` and confirm DECISION is TRADE
2. Run `/trade TICKER SHARES buy` with small size (e.g., 5–10 shares)
3. Confirm rule validation passes
4. Execute (`y`)
5. Verify `/portfolio` shows the position + 10% stop
6. Run `/midday` to confirm stop is active
7. Monitor through market close
8. Run `/daily-summary` EOD

This validates the full end-to-end workflow with real money on paper account.

---

## Key Commands at a Glance

| Time | Command | What It Does |
|------|---------|--------------|
| Pre-market | `/pre-market` | Research + trade ideas |
| Market open | `/portfolio` | Account snapshot |
| Market open | `/trade TICKER SHARES buy` | Execute (with validation) |
| Midday | `/midday` | Scan + cut losers + tighten stops |
| Close | `/daily-summary` | EOD snapshot + P&L |
| Friday | `/weekly-review` | Stats + grade + plan |

---

## Troubleshooting

**"ALPACA_API_KEY not set"**
→ Check `.env` file exists and credentials are filled in (not placeholder text).

**"Quote for SPY failed"**
→ Market might be closed. SPY and other quotes only work during market hours (9:30am–4:00pm ET).

**Trade rejected: "Catalyst not documented"**
→ Your `/pre-market` research didn't run OR didn't document a catalyst. Run `/pre-market` first and make sure DECISION is TRADE with ideas listed.

**Stop order rejected: "PDT"**
→ Pattern-day-trader rule hit. Fallback: bot tries fixed stop. If also rejected: queued for next morning.

---

## What's Next?

1. **Test locally for 5–10 days:** Get comfortable with the workflow.
2. **Execute 3–5 real trades:** Validate order placement, stops, logging.
3. **Run for 30 days / 30 trades:** Gather data for Phase 1 gate (Sharpe ≥ 1.5, max drawdown ≤ 15%).
4. **Then: Phase 2 cloud routines** (automated scheduling via cron jobs).

---

## Questions?

Refer to:
- **Strategy details:** `memory/TRADING-STRATEGY.md`
- **Risk rules:** `memory/CONSTRAINTS.md`
- **Example trades:** `memory/TRADE-LOG.md` (as it fills)
- **Command docs:** `.claude/commands/*.md` (each has detailed step-by-step)

Good luck. Run disciplined. Log everything. Phase 1 is about validation, not profits.
