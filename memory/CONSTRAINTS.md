# Hard Constraints (Risk Rules)

**These gates are enforced programmatically before every order. No exceptions except via explicit user override logged in decisions/log.md.**

---

## Position Sizing

- **Max per position:** 20% of account equity
- **Max sector concentration:** No sector > 25% equity
- **Max open positions:** 5–6 at once
- **Min deployed:** 75–85% of equity (stay active, but not forced)
- **Per-trade risk:** 0.5–1% of equity (position size × stop distance / equity)

---

## Stops & Exits

- **Every position:** Real GTC stop-loss order placed at entry (not mental)
- **Hard stop:** Cut at -7% from entry, no hesitation
- **Thesis break:** Close immediately if catalyst invalidates, even if not at -7%
- **Stop placement:** ATR-based or technical level; typically 7–10% below entry
- **Trailing on winners:** 7% at +15%, 5% at +20%
- **Never within 3% of current price; never move stop down**

---

## Sector Discipline

- **Track consecutive fails:** Count failed trades per sector
- **Exit sector:** After 2 consecutive failed trades in same sector, exit all positions in that sector
- **Momentum check:** Don't force thesis if whole sector is rolling over

---

## Trade Frequency

- **Max per week:** 3 new positions
- **Max per day:** Determined by remaining weekly allowance + PDT rules
- **PDT compliance:** 3 day trades per 5 rolling business days (account < $25k)
- **No first 15 mins:** Avoid high volatility at session open
- **No last 15 mins:** Except to close existing positions

---

## Forbidden Behaviors

- NO options — ever
- NO martingale / averaging down
- NO revenge trades (1-hour cooldown after stop-out)
- NO trading through earnings on held positions (unless explicitly part of strategy)
- NO leverage beyond margin available
- NO positions without documented catalyst

---

## Circuit Breakers

- **Daily loss limit:** 2% of equity → stop trading for the day
- **Weekly loss limit:** 5% of equity → pause for review
- **Max drawdown:** 15% from peak → halt entirely, manual restart only

---

## Order Requirements

**Layer A — Catalyst (existing):**
1. Total positions after fill ≤ 6
2. Trades this week (including this) ≤ 3
3. Position cost ≤ Kelly-sized limit (see Quant Sizing below)
4. Position cost ≤ available cash
5. Catalyst documented in today's research log
6. Stock only (verified ticker)
7. PDT rules allow (daytrade_count < 3 if same-day close intended)
8. RSI(14) < 30 (long) or > 70 (short)
9. Sector in momentum (not rolling over per recent TRADE-LOG)
10. Risk/reward ≥ 2:1 with stop placed

**Layer B — Quant (new — see TRADING-STRATEGY.md "Quant Layer"):**
11. Z-Score |≥ 2.0| vs 20-day mean (long: ≤−2.0, short: ≥+2.0)
12. VIX regime allows new entries (must be ≤ 30 unless override)
13. Sector pair identified and either confirms direction OR diverges < 1.5σ

**If ANY (1–13) fail:** Skip trade, log which layer + which check failed. Move on.

---

## Quant Sizing (Kelly + Regime Multiplier)

```
kelly_pct  = (win_rate × avg_win − loss_rate × avg_loss) / avg_win
sized_pct  = max(5%, min(20%, kelly_pct × 0.25))   # quarter-Kelly, hard-bounded
final_pct  = sized_pct × vix_regime_multiplier
```

**VIX regime multiplier:**
- VIX < 22 → 1.00×
- VIX 22–30 → 0.75×
- VIX > 30 → 0.50× (or PAUSE all new entries — bot's choice based on conviction)

**Cold-start (< 30 closed trades):** Use flat 10% per position with VIX multiplier still applied.

---

## Z-Score Computation

Use Alpaca historical bars: `bash scripts/alpaca.sh bars SYMBOL 25` returns last 25 daily closes.

```
mean    = sum(closes[-20:]) / 20
stddev  = sqrt(sum((c − mean)² for c in closes[-20:]) / 20)
z_score = (current_price − mean) / stddev
```

If stddev < 0.01 → reject (illiquid or stale data).

---

## Order Type Mandate

**All entry orders MUST be bracket limit orders (not market orders).**

Required structure:
```json
{
  "symbol": "SYM",
  "qty": "N",
  "side": "buy",
  "type": "limit",
  "time_in_force": "day",
  "limit_price": "X.XX",
  "order_class": "bracket",
  "take_profit": {"limit_price": "Y.YY"},
  "stop_loss":   {"stop_price": "Z.ZZ"}
}
```

**Limit price rules:**
- Must equal the bot's research-derived intended entry (NOT current market)
- Must produce R:R ≥ 2:1 vs the stop_loss and take_profit
- If current market is already past the limit (gapped up), DO NOT chase — let order sit unfilled

**Time-in-force rules:**
- Default: `day` (cancels at session close, re-evaluate tomorrow)
- GTC only by explicit override in research log entry

**Market orders are ONLY allowed for:**
- Closing stopped-out positions
- Thesis-break exits
- Cancellations / position closes
- NEVER for fresh entries

## Stop Placement Fallback (Post-Fill)

After a bracket fill, the fixed stop_loss is active. If the position becomes profitable, the bot should upgrade the fixed stop to a trailing stop on the next monitoring run:

1. Cancel the bracket's child stop_loss order
2. Place 10% trailing stop GTC
3. If trailing rejected (PDT): keep the bracket's fixed stop in place

If the bracket itself is rejected by Alpaca (e.g., insufficient buying power, invalid prices):
1. Log the rejection reason
2. Skip the trade — do NOT fall back to a market order

---

## Overrides

Only user (Alex) can override via explicit logged decision in `decisions/log.md`. Format:
```
[YYYY-MM-DD] OVERRIDE: <rule> | REASON: <why> | TRADE: <ticker/action> | CONTEXT: <details>
```

Bot itself cannot override any constraint.
