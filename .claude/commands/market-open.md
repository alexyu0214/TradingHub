---
description: Market-open execution. Execute today's planned trades from research log, set stops.
---

# Market-Open Execution (Local)

Run shortly after market open. Execute any planned trades from this morning's research, validate with fresh quotes, set trailing stops.

---

## STEP 1 — Read Today's Research

```bash
grep -A 50 "## $(date +%Y-%m-%d)" memory/RESEARCH-LOG.md
```

Pull today's trade ideas (if any) and confirm DECISION was TRADE (not HOLD).

## STEP 2 — Re-Validate with Live Quotes

For each planned trade from research:

```bash
bash scripts/alpaca.sh quote SYMBOL
bash scripts/alpaca.sh account  # Check current positions count, daytrade count
```

- Check bid/ask spread (wide spread = halt signal)
- Verify SYMBOL hasn't been halted, delisted, or gapped past entry level
- Re-confirm daytrade count allows same-day sell (if needed)

## STEP 3 — Run Buy-Side Gate on Each Planned Trade

Use memory/CONSTRAINTS.md checklist:

- Total positions after fill ≤ 6
- Trades this week (including this) ≤ 3
- Position cost ≤ 20% equity
- Position cost ≤ available cash
- PDT rules allow
- **Catalyst still valid** (re-read news if big news hit overnight)

**If any trade fails:** Skip it. Log the reason and move on.

Example:
```
SPY: SKIPPED — daytrade_count at 3/3 (PDT limit reached)
```

## STEP 4 — Execute Approved Trades (Market Orders, Day TIF)

For each approved trade:

```bash
bash scripts/alpaca.sh order '{"symbol":"SYMBOL","qty":"SHARES","side":"buy","type":"market","time_in_force":"day"}'
```

Wait for fill. Capture: SYMBOL, fill price, fill quantity, order ID.

## STEP 5 — Immediately Place 10% Trailing Stop (GTC)

For each filled buy order:

```bash
bash scripts/alpaca.sh order '{"symbol":"SYMBOL","qty":"SHARES","side":"sell","type":"trailing_stop","trail_percent":"10","time_in_force":"gtc"}'
```

If rejected (PDT error):
1. Try fixed stop 10% below fill:
   ```bash
   bash scripts/alpaca.sh order '{"symbol":"SYMBOL","qty":"SHARES","side":"sell","type":"stop","stop_price":"X.XX","time_in_force":"gtc"}'
   ```
2. If also rejected: Note "PDT-blocked, set tomorrow morning" in TRADE-LOG

## STEP 6 — Log Each Trade to TRADE-LOG.md

Append entry with full thesis from research, entry price, stop, target, R:R:

```markdown
### YYYY-MM-DD HH:MM — BUY SYMBOL
**Catalyst:** [from research]
**Entry Price:** $X.XX (SHARES shares, filled at market)
**Stop:** $X.XX (-10% trailing) [or fixed stop if trailing rejected]
**Target:** $X.XX
**Risk:** $X (% of equity)
**Thesis:** [copied from research log]
**Trade ID:** [timestamp]
```

## STEP 7 — Notification

Append to DAILY-SUMMARY.md (local fallback):
```
Market-open executions:
- SYMBOL1: SHARES @ $X.XX, stop $X.XX
- SYMBOL2: SHARES @ $X.XX, stop $X.XX
(or "No trades executed")
```

## STEP 8 — Print Summary

List all executed trades:
```
Market-Open Execution — YYYY-MM-DD

Executed:
  SYMBOL1: SHARES @ $X.XX, 10% trail stop placed
  SYMBOL2: SHARES @ $X.XX, 10% trail stop placed

Skipped:
  SYMBOL3: Daytrade limit reached
  SYMBOL4: Insufficient cash

Portfolio now: N positions, X% deployed
```

## STEP 9 — No Commit (Local Testing Phase)

Do NOT git commit/push. Local testing only.

---

## Error Handling

- **Quote fails:** Assume halted/illiquid. Skip trade and log reason.
- **Order fills above/below expected:** Log actual fill price, re-validate R:R against actual entry.
- **Stop rejected but no fallback:** Queue for tomorrow morning with note in TRADE-LOG: "PDT-blocked, stop queued MM-DD HH:MM"
