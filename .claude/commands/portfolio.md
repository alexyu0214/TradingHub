---
description: Read-only snapshot of account, positions, and open stops
---

# Portfolio Snapshot (Read-Only)

Print a clean, instant view of account state. No trades placed. No memory written.

## STEP 1 — Pull Live Account State

```bash
bash scripts/alpaca.sh account
bash scripts/alpaca.sh positions
bash scripts/alpaca.sh orders
```

## STEP 2 — Parse & Format

Extract from the JSON:
- Equity, Cash, Buying Power, Daytrade count
- All open positions (ticker, qty, entry price, current price, unrealized P&L, P&L %)
- All open stop orders (ticker, order type, stop price / trail %, order ID)

## STEP 3 — Print Summary Table

```
Portfolio Snapshot — YYYY-MM-DD HH:MM

Equity: $X | Cash: $X (X%) | Buying Power: $X
Daytrade count: N/3 | Positions: N open

Positions:
  SYM | qty | Entry $X → Now $X | Unrealized ±$X (±X%) | Stop $X | Status

Open Orders:
  ORDER_ID | SYM | Qty | Type (trail % / stop $) | Status
```

## STEP 4 — Sanity Checks (No Commentary Except Warnings)

- If a position has **no stop order** → Flag: "WARNING: SYM has no stop"
- If a stop is **below current price** → Flag: "WARNING: SYM stop $X is below current price $Y"
- Otherwise: silent (no fluff)

## STEP 5 — Exit

Print the table and stop. No file writes. No git commits.
