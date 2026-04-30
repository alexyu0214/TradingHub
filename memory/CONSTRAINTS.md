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

**Before placing any buy order:**
1. Total positions after fill ≤ 6
2. Trades this week (including this) ≤ 3
3. Position cost ≤ 20% equity
4. Position cost ≤ available cash
5. Catalyst documented in today's research log
6. Stock only (verified ticker)
7. PDT rules allow (daytrade_count < 3 if same-day close intended)

**If ANY fail:** Skip trade, log reason, move on.

---

## Stop Placement Fallback

1. Try 10% trailing stop (GTC)
2. If rejected (PDT): Use fixed stop 10% below entry (GTC)
3. If also rejected: Queue for next trading day morning

---

## Overrides

Only user (Alex) can override via explicit logged decision in `decisions/log.md`. Format:
```
[YYYY-MM-DD] OVERRIDE: <rule> | REASON: <why> | TRADE: <ticker/action> | CONTEXT: <details>
```

Bot itself cannot override any constraint.
