---
description: Midday scan. Cut losers, tighten stops on winners, thesis check.
---

# Midday Scan (Local)

Run mid-trading day to scan open positions, cut losses, tighten stops on winners, validate thesis.

---

## STEP 1 — Read Memory

```bash
cat memory/TRADING-STRATEGY.md  # Exit rules
tail -20 memory/TRADE-LOG.md    # Recent trades + entries
cat memory/RESEARCH-LOG.md      # Today's research (any midday thesis check?)
```

Review entry theses and stop levels.

## STEP 2 — Pull Live Positions

```bash
bash scripts/alpaca.sh positions
bash scripts/alpaca.sh orders
bash scripts/alpaca.sh account
```

For each open position: ticker, qty, entry, current price, unrealized P&L %, stop level.

## STEP 3 — CUT LOSERS AT -7%

For each position where unrealized_plpc ≤ -0.07:

1. Close position:
   ```bash
   bash scripts/alpaca.sh close SYMBOL
   ```
2. Cancel its trailing stop:
   ```bash
   bash scripts/alpaca.sh cancel ORDER_ID
   ```
3. Log exit to TRADE-LOG.md:
   ```markdown
   ### YYYY-MM-DD HH:MM — EXIT SYMBOL (STOP)
   **Exit Price:** $X.XX
   **Realized P&L:** -$X (-7%)
   **Reason:** Cut at -7% per rule
   **Hold time:** X trading days
   **Trade ID:** [matches original entry]
   ```

## STEP 4 — TIGHTEN STOPS ON WINNERS

For each position where unrealized_plpc > 0:

- If up ≥ +20%: Tighten trail from 10% to 5%
  ```bash
  bash scripts/alpaca.sh cancel OLD_STOP_ORDER_ID
  bash scripts/alpaca.sh order '{"symbol":"SYMBOL","qty":"SHARES","side":"sell","type":"trailing_stop","trail_percent":"5","time_in_force":"gtc"}'
  ```
- If up ≥ +15% (but < +20%): Tighten trail from 10% to 7%
  ```bash
  bash scripts/alpaca.sh cancel OLD_STOP_ORDER_ID
  bash scripts/alpaca.sh order '{"symbol":"SYMBOL","qty":"SHARES","side":"sell","type":"trailing_stop","trail_percent":"7","time_in_force":"gtc"}'
  ```

**Constraints:**
- Never tighten within 3% of current price
- Never move a stop down (only closer from above)

Log each stop adjustment:
```markdown
### YYYY-MM-DD HH:MM — STOP ADJUSTED SYMBOL
**Position:** SHARES @ $ENTRY (now $CURRENT, +X%)
**Old stop:** $X (-10%)
**New stop:** $X (-7%)
**Reason:** Up +15%, tighten per rule
```

## STEP 5 — THESIS CHECK

For each remaining position, validate:
- Is the original catalyst still valid? (check news)
- Is the sector still in momentum or has it rolled over?
- Has technical setup changed (trend flip, support break)?

**If thesis broken:** Close position immediately, even if not at -7%. Log:
```markdown
### YYYY-MM-DD HH:MM — EXIT SYMBOL (THESIS)
**Exit Price:** $X.XX
**Realized P&L:** ±$X (±X%)
**Reason:** Catalyst invalidated / sector rolling over / technical break
**Hold time:** X trading days
**Trade ID:** [matches original entry]
```

## STEP 6 — OPTIONAL RESEARCH (Conditional)

If something is moving sharply intraday with no obvious cause, run one WebSearch query:
- "What is happening with [TICKER] stock today?"

Append findings to RESEARCH-LOG.md as afternoon addendum if material.

## STEP 7 — LOG ACTIONS

Update TRADE-LOG.md with all actions (cuts, stop tightens, thesis exits).

## STEP 8 — NOTIFICATION

Append to DAILY-SUMMARY.md (local fallback) if ANY action taken:
```
Midday scan:
- Cut SYMBOL1 at -7% for -$X loss
- Tightened SYMBOL2 stop to 7% (up +18%)
- Thesis exit SYMBOL3 (sector rolling over) for +$X
```

If no action: silent (no entry needed).

## STEP 9 — PORTFOLIO SNAPSHOT

Print current portfolio state:
```
Midday Portfolio — YYYY-MM-DD HH:MM

Positions: N open
Cash: $X (X%)
Deployed: X%

| SYM | Entry | Now | Unrealized | Stop |
```

## STEP 10 — No Commit (Local Testing Phase)

Do NOT git commit/push. Local testing only.

---

## Notes

- **Sector discipline:** If this is the 2nd failed trade in a sector this week, exit ALL positions in that sector and note in TRADE-LOG.
- **No revenge trades:** After a -7% stop-out, do not immediately re-enter same ticker. 1-hour cooldown minimum.
- **Patience on winners:** Don't over-tighten stops and get shaken out. Respect the 3% rule (never within 3% of current price).
