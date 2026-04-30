---
description: Manual trade helper with strategy-rule validation. Usage — /trade SYMBOL SHARES buy|sell
---

# Manual Trade Helper (Rule-Validated)

Execute a manual trade with full constraint validation. Refuses any trade that fails a rule.

**Usage:** `/trade SYMBOL SHARES buy|sell` 

Example: `/trade SPY 10 buy`

---

## STEP 1 — Parse Arguments

Args: SYMBOL, SHARES, SIDE (buy or sell). Require all three; ask if missing.

## STEP 2 — Pull Live State

```bash
bash scripts/alpaca.sh account
bash scripts/alpaca.sh positions
bash scripts/alpaca.sh quote SYMBOL  # Get bid/ask
```

Extract: equity, cash, current positions count, current positions per sector.

## STEP 3 — FOR BUY ORDERS — Validate All Rules

Run through memory/CONSTRAINTS.md buy-side gate. **Stop and refuse if ANY fail:**

- [ ] Total positions after fill ≤ 6
- [ ] Trades this week (including this one) ≤ 3
- [ ] Position cost (SHARES × ask_price) ≤ 20% of equity
- [ ] Position cost ≤ available cash
- [ ] Daytrade count < 3 (if same-day close intended)
- [ ] A specific catalyst is documented in today's RESEARCH-LOG.md
- [ ] SYMBOL is a stock (verify with quote, reject if OTC, delisted, or halted)
- [ ] Bid/ask spread is reasonable (< 1% for liquid names; flag if wide)

**If ANY fail:** Print the failed checks and **STOP**. Do NOT place order.

Example failure output:
```
TRADE REJECTED: 3 rule violations
- ✗ Trades this week: 3/3 (at limit)
- ✗ Cash available: $500 < required $2000
- ✗ No catalyst documented in RESEARCH-LOG
```

## STEP 4 — FOR SELL ORDERS — Basic Check

- [ ] Position exists with that ticker and has ≥ SHARES
- [ ] Otherwise pass through (simpler validation for exits)

## STEP 5 — Print Order Details & Ask Confirmation

Format the order JSON and show user:
```json
{
  "symbol": "SPY",
  "qty": "10",
  "side": "buy",
  "type": "market",
  "time_in_force": "day"
}
```

Print all passed checks:
```
✓ Total positions after: 2/6
✓ Trades this week: 1/3
✓ Position cost: 5% of equity
✓ Cash available: yes
✓ Catalyst documented: "Fed rate decision, risk-off to risk-on rotation"
✓ SYMBOL: SPY (liquid, spreads tight)

Execute? (y/n)
```

## STEP 6 — On Confirm (y) — Place Market Buy

```bash
bash scripts/alpaca.sh order '{"symbol":"SPY","qty":"10","side":"buy","type":"market","time_in_force":"day"}'
```

Wait for fill confirmation. Extract fill price and order ID.

## STEP 7 — For BUYs — Immediately Place 10% Trailing Stop (GTC)

```bash
bash scripts/alpaca.sh order '{"symbol":"SPY","qty":"10","side":"sell","type":"trailing_stop","trail_percent":"10","time_in_force":"gtc"}'
```

If Alpaca rejects with PDT error:
- Fall back to fixed stop 10% below fill price:
  ```bash
  bash scripts/alpaca.sh order '{"symbol":"SPY","qty":"10","side":"sell","type":"stop","stop_price":"X.XX","time_in_force":"gtc"}'
  ```
- If also rejected: Print "Stop queued for next trading day morning" and note in TRADE-LOG

## STEP 8 — Log to TRADE-LOG.md

Append new trade entry:
```markdown
### YYYY-MM-DD HH:MM — BUY SPY
**Catalyst:** Fed rate decision, risk-off to risk-on rotation
**Entry Price:** $X.XX (10 shares, filled at market)
**Stop:** $X.XX (-10% trailing)
**Target:** $X.XX (2:1 R:R)
**Risk:** $X (1% of equity)
**Thesis:** Fed signals easier policy ahead; SPY sector momentum confirming long bias from 50/200 SMA. Entry on RSI < 30 in uptrend. Volume confirmed.
**Trade ID:** [auto-generated timestamp]
```

## STEP 9 — Notification to DAILY-SUMMARY.md

Append one-line trade entry:
```
- SPY: 10 shares @ $X.XX, stop $X.XX, target $X.XX (2:1 R:R)
```

## STEP 10 — Print Confirmation

```
Trade executed.
SPY 10 @ $X.XX (fill ID: XXX)
10% trailing stop placed (GTC, order ID: YYY)
Logged to TRADE-LOG.md
```

---

## On Reject (n)

Cancel. Do not place any orders.

---

## Notes

- **No averaging down:** If position already open, reject any add to that position (enforce strict position limit).
- **Thesis required:** If RESEARCH-LOG has no entry for today OR no documented catalyst for this ticker, refuse the trade.
- **PDT careful:** On paper account, PDT rules still apply. If 3 day trades already used, trailing stop may be rejected (show fallback ladder).
