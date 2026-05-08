# Trading Strategy & Rules

**Mission:** Beat S&P 500 on $100k Alpaca paper (Phase 1), then graduate to $1k live (Phase 2).

**Instruments:** Stocks ONLY. No options, no crypto, no forex.

**Horizon:** Swing trading (2–10 days typical). Not day-trading, not buy-and-hold.

---

## Capital & Position Constraints (Opus-Adapted)

- **Starting capital:** $100,000 (paper)
- **Max per position:** 20% of equity (~$20k)
- **Max open positions:** 5–6 at a time
- **Max deployed:** 75–85% of equity
- **Max trades per week:** 3 new positions
- **PDT rule:** 3 day trades per 5 rolling business days (sub-$25k account)

---

## Entry Signals (Trend + Mean-Reversion Hybrid)

**Qualify the universe first:**
- Market cap > $2B
- Average daily volume > 1M shares
- Price > $5
- Optional: S&P 500 / Nasdaq-100 names preferred

**Then apply signals:**
1. **Trend base:** 50-day SMA > 200-day SMA (long-bias) OR < (short-bias)
2. **Momentum:** 12-month return percentile vs universe in top quintile
3. **Entry trigger:** RSI(14) < 30 (in uptrend) for longs OR RSI > 70 (in downtrend) for shorts
4. **Volume confirm:** Entry day volume > 20-day average volume
5. **Catalyst:** Must have a documented reason TODAY (earnings, news, sector rotation, etc.)

---

## Stop & Target Rules

**Every position gets a real GTC stop-loss order placed at entry (not mental).**

- **Stop level:** 1 ATR or technical support/resistance, typically 7–10% below entry
- **Minimum:** Must have 2:1 risk/reward minimum
- **Target:** 2–3x ATR or technical resistance

---

## Exit Rules

**Mandatory stops:**
- **Hard stop at -7%:** Cut manually, no hope, no averaging down
- **Thesis break:** If catalyst invalidates or sector rolls over, cut immediately even if not at -7%

**Profit-taking (trailing):**
- At +15% unrealized: tighten trailing stop to 7%
- At +20% unrealized: tighten trailing stop to 5%
- Never tighten a stop within 3% of current price
- Never move a stop down (only closer to current price from above)

**Sector rotation:**
- Track consecutive failed trades per sector
- Exit entire sector if 2 consecutive trades fail in that sector
- Follow sector momentum; don't force a thesis into a rolling-over sector

**Patience rule:**
- A week with zero trades can be the right call
- Only trade when edge is present; else hold cash

---

## Trailing Stops (10% Standard)

Place a real 10% trailing_stop GTC order on Alpaca immediately after every entry fill.

If same-day stop rejection (PDT):
1. Try fixed stop (10% below entry)
2. If also blocked: queue for next morning

---

## Entry Checklist (Agent Documents All Before Placing)

Before every buy order, verify:
- ✓ What is the specific catalyst today?
- ✓ Is the sector in momentum (not rolling over)?
- ✓ What is the stop level (7–10% below entry)?
- ✓ What is the target (minimum 2:1 risk/reward)?
- ✓ Total positions after fill ≤ 6
- ✓ Trades this week (including this) ≤ 3
- ✓ Position cost ≤ 20% of equity
- ✓ Position cost ≤ available cash
- ✓ Daytrade count leaves room (PDT: 3/5 rolling days)
- ✓ Instrument is a stock (not an option, not a fund)

If any fail → skip trade, log reason.

---

## Research Cadence

**Pre-market (daily):**
- Oil (WTI / Brent)
- S&P 500 futures
- VIX level
- Top market catalysts
- Pre-market earnings
- Economic calendar (CPI, PPI, FOMC, jobs)
- Sector momentum (YTD, recent)
- News on held tickers

**Midday (conditional):**
- Thesis validation for open positions
- Major news on held names
- Intraday sector rotation signals

**Friday (weekly review):**
- Full week stats (win rate, profit factor, Sharpe)
- What worked, what didn't
- Adjustments for next week
- Performance vs S&P 500

---

## Phase Gate Criteria (Paper Validation)

Must pass all to advance to Phase 2 (live $1k account):
- Sharpe ratio ≥ 1.5
- Max drawdown ≤ 15%
- Positive expectancy (not just lucky win rate)
- ≥ 30 trading days of live data
- ≥ 30 closed trades

---

## Order Execution Strategy (Bracket Limit Orders)

**Default for all entries: bracket limit orders. NOT market orders.**

The bot does NOT chase the market. The bot identifies an intended entry price, places a LIMIT BUY at that price with attached stop-loss and take-profit (one bracket order), and lets Alpaca handle execution if/when the price reaches the limit.

**Why this matters:**
- Eliminates gap-chasing (limit just sits there if price gaps past it)
- Removes need for "did this fire yet" intraday polling
- Discipline: if price doesn't come to the limit, no trade. That's correct behavior.
- Stop-loss + take-profit are placed atomically with the entry, so risk is bounded the moment the order fills

**Order construction:**
```
Order class: bracket
Type: limit (buy)
Limit price: research-derived intended entry
Time in force: day (re-evaluate tomorrow if unfilled)
Take-profit (child): research-derived target (≥ 2:1 R:R)
Stop-loss (child): typically 7-10% below limit (or technical level)
```

**Lifecycle:**
1. Market-open workflow places bracket limit orders at intended entries
2. If price hits limit during the session → order fills, bracket activates (stop + target both live)
3. If price never hits limit → order expires at session close, no fill
4. Next morning's pre-market re-evaluates. If thesis still valid AND Z-Score still qualifies, re-place. Otherwise skip.

**When to use market orders instead:**
- Closing a stopped-out position (immediate exit)
- Closing on thesis-break (no time for limit)
- NEVER for fresh entries

**Trailing stop upgrade (post-fill):**
The bracket places a fixed stop. Once filled, on the next bot run (midday or afternoon-scan), if position is profitable, replace the fixed stop with a 10% trailing stop GTC per existing rules.

---

## Phase Review Cycle (Every 3 Weeks)

**Purpose:** Force structured improvement. Strategy must evolve based on actual performance, not stay frozen.

**Schedule:**
- **Phase 1 review:** 3 weeks after Phase 1 launch
- **Every 3 weeks thereafter:** structured retro of strategy, prompts, deployment, win rate

**What gets reviewed each cycle:**
1. Strategy efficacy — is the current approach producing edge?
2. Backlog items — what's queued for next phase?
3. Failed adjustments — what's been on the weekly list 3+ weeks unimplemented? Promote to a coding task.
4. Cost vs return — is API spend justified by alpha generated?
5. Phase gate progress — distance to ≥30 closed trades, Sharpe target, drawdown ceiling

**Where the schedule lives:**
- `decisions/log.md` — each phase review logs its outcome
- Friday's weekly review prompt checks: "Is today's date ≥ 3 weeks since last phase review? If so, append a Phase Audit subsection."

**Phase milestones:**
- Phase 1 (current): Quant layer (4 lanes) + bracket limits + Minervini Trend Template + R-multiples + ≤5% pivot extension + shorts (with conservative caps) + 6 daily workflows. Review 2026-05-24.
- Phase 2 backlog: VCP pattern detection (proper Minervini base recognition) + regime-aware sell-into-strength + live $1k account migration (after Phase 1 gate criteria met)
- Phase 3 backlog: Pairs trading (coordinated long+short same sector for hedged exposure)
- Phase 4 backlog: Conditional hourly monitor (cheap pre-filter triggers full agent only on signals)

---

## Quant Layer (Simons-Inspired Statistical Edge)

**Purpose:** Sit ON TOP of the catalyst checklist to widen the universe of qualifying setups WITHOUT lowering the bar. Both layers must clear for a trade to fire.

### 1. Universe Expansion

Daily scan covers (in priority order):
- S&P 500 + Nasdaq-100 (current default)
- Russell 1000 mid-caps with catalysts
- US-listed ETFs > $1B AUM in trending sectors
- ADR mega-caps (TSM, ASML, NVO, BABA, etc.)

All other filters retained: market cap > $2B, ADV > 1M shares, price > $5.

### 2. Z-Score Entry Confirmation (REQUIRED — Either Lane, Either Direction)

The bot evaluates **four distinct entry styles** — two lanes × two directions. ANY ONE lane must pass for the candidate to qualify (Layer A still must pass separately).

```
Z = (current_price − mean(close, 20)) / stddev(close, 20)
```

Bot pulls historical bars via: `bash scripts/alpaca.sh bars SYMBOL 25`

#### 2a-LONG. Mean-Reversion Long (oversold bounce)
ALL must hold:
- Z-Score ≤ −2.0 (statistically oversold, top 5% deviation)
- RSI(14) < 30
- Volume on entry day ≥ 1.0× 20-day average

#### 2a-SHORT. Mean-Reversion Short (overbought reversal — Phase 1 enabled)
ALL must hold:
- Z-Score ≥ +2.0
- RSI(14) > 70
- Volume ≥ 1.0× 20-day average

Catches "stretched too far in either direction, expect snap-back."

#### 2b-LONG. Momentum Long (trend continuation breakout)
ALL must hold:
- Z-Score ≥ +1.0 (price stretching upward, not at extreme)
- Current close > prior 20-day high (clean breakout from base)
- RSI(14) between 50 and 70
- Volume on breakout day ≥ 1.5× 20-day average
- 50-day SMA > 200-day SMA (uptrend regime confirmed)

#### 2b-SHORT. Momentum Short (downtrend breakdown — Phase 1 enabled)
ALL must hold:
- Z-Score ≤ −1.0 (price stretching downward, not at extreme)
- Current close < prior 20-day low (clean breakdown from base)
- RSI(14) between 30 and 50
- Volume on breakdown day ≥ 1.5× 20-day average
- 50-day SMA < 200-day SMA (downtrend regime confirmed)

Catches "broken-down weak stock with confirmed institutional distribution." Inverse of momentum long.

#### Lane selection logic

The bot picks the right lane based on catalyst type and price posture:
- "Panic selloff" / "post-earnings overreaction" + oversold → Mean-Reversion Long
- "Earnings beat + uptrend" / "breakout from base" → Momentum Long
- "Failed rally" / "post-earnings overheating" + overbought → Mean-Reversion Short
- "Failed support" / "broken leadership" + breakdown → Momentum Short

Reject if no lane qualifies.

---

## Minervini Trend Template (Layer A Enhancement — NEW)

In addition to the catalyst checklist, every candidate must pass the **Trend Template** for its intended direction. Filters universe to true leaders (longs) or true laggards (shorts) and rejects sideways/messy stocks.

### Long Trend Template (every long entry)

ALL must hold:
- Price > 50-day SMA, 150-day SMA, AND 200-day SMA (all three)
- 150-day SMA > 200-day SMA
- 200-day SMA trending up for ≥ 1 month (compare 200-SMA today vs 1 month ago)
- 50-day SMA > 150-day SMA AND > 200-day SMA
- Price > 30% above 52-week low
- Price within 25% of 52-week high
- 6-month return percentile ≥ 70th (top 30% of universe)

Bot pulls extended bars: `bash scripts/alpaca.sh bars SYMBOL 210` (covers 200-SMA + 1-month buffer for trend check).

### Short Trend Template (every short entry — Phase 1 enabled)

ALL must hold (inverse of long template):
- Price < 50-day SMA, 150-day SMA, AND 200-day SMA
- 150-day SMA < 200-day SMA
- 200-day SMA trending down for ≥ 1 month
- 50-day SMA < 150-day SMA AND < 200-day SMA
- Price > 30% below 52-week high
- Price within 25% of 52-week low
- 6-month return percentile ≤ 30th (bottom 30% — true laggards)

If a candidate fails its Trend Template → REJECT regardless of catalyst. No exceptions.

---

## Pivot Extension Rule (NEW — Minervini Discipline)

For Momentum Lane entries (long or short), the limit price must be **≤ 5% above the breakout pivot** (longs) or **≤ 5% below the breakdown pivot** (shorts).

**Pivot definition:**
- Long pivot = the 20-day high that was just broken
- Short pivot = the 20-day low that was just broken

**Rule:**
- If `(intended_limit / pivot − 1) > 0.05` for longs → REJECT (chasing extended breakout)
- If `(pivot / intended_limit − 1) > 0.05` for shorts → REJECT (chasing extended breakdown)

**Why:** Late-stage breakouts and breakdowns are where trend-followers blow up. Half of failed momentum trades are "chased" entries 8-15% extended from pivot. Forcing ≤5% extension means the bot waits for pullbacks to the pivot or skips the trade entirely.

For Mean-Reversion Lane entries: this rule does not apply (those are by definition stretched far from pivot — that's the entire point of the trade).

---

## R-Multiple Framework (Risk Sizing — NEW)

Every entry must be planned in terms of **R**, where 1R = the dollar amount of capital risked if the stop fires.

```
R_dollars = abs(entry_price − stop_price) × shares
R_pct     = R_dollars / equity   (as fraction of total account)
```

**Constraints:**
- R per trade target: 0.5% to 1.0% of equity (max 1.5% in high-conviction A+ setups)
- Take-profit must be ≥ 2R away from entry (target ≥ 2× the risk)
- Ideal target: 3R (gives margin even with 50% win rate)

**Trade log requires R-value** for every entry:
```
R_dollars: $XXX (Y.Y% of equity)
Target R-multiple: 2.5R (target $X.XX from entry)
```

**Why:** Standardizes risk regardless of share price. A 7% stop on a $10 stock vs $300 stock means nothing without R-context. Phase 1 → Phase 2 graduation requires positive expectancy in R-terms, not just dollar P&L.

---

## Short Position Caps (Phase 1 Conservative)

Shorts have asymmetric risk — a stock can rise infinitely. Phase 1 caps:

- **Max per short position:** 10% of equity (vs 20% for longs)
- **Max total short exposure:** 30% of equity (preserves net-long bias)
- **Universe:** liquid mega-caps (mkt cap > $20B) and sector/index ETFs ONLY — no mid-caps, no high-momentum names, no recent IPOs (< 6 months public)
- **No shorting through earnings** (any held short must be closed before its company's earnings date)
- **No shorting after a >5% gap-down day** on the candidate (capitulation often marks bottom; squeeze risk)
- **Hard borrow check:** if Alpaca returns `htb` flag or borrow rejection, skip and log
- **No averaging up shorts** (don't add to losing shorts — same as long discipline)

Caps relax in Phase 2 once Phase 1 data validates short execution.

### 3. Regime Filter (VIX-Based)

Pre-market workflow records VIX regime. Bot behavior:

| VIX | Regime | Sizing Multiplier | Strategy Bias |
|---|---|---|---|
| < 14 | Calm trending | 1.00× | Catalyst + momentum |
| 14–22 | Normal | 1.00× | All entry types OK |
| 22–30 | Elevated | 0.75× | Mean-reversion preferred, tighter stops |
| > 30 | Crisis | 0.50× OR PAUSE | Mean-reversion only |

If VIX > 30 → no new entries unless user override in `decisions/log.md`.

### 4. Kelly Criterion Position Sizing

Replace flat 20% sizing with dynamic Kelly:

```
kelly_pct = (win_rate × avg_win − loss_rate × avg_loss) / avg_win
position_pct = max(5%, min(20%, kelly_pct × 0.25))   # quarter-Kelly for safety
```

Apply VIX regime multiplier last.

**Cold start:** Until ≥ 30 closed trades exist for stats, default to 10% per position.

### 5. Pairs Awareness (Confirmation Only — NOT Hedged Trading)

For every long candidate, identify a sector pair (highly-correlated industry peer):
- XOM ↔ CVX, COP (integrated oil)
- NVDA ↔ AVGO, AMD (semis)
- JPM ↔ GS, BAC (large banks)
- AAPL ↔ MSFT (mega-cap tech)
- GLD ↔ NEM, GOLD (gold complex)

**Decision rules:**
- Pair moving same direction, similar Z-Score → CONFIRMS sector thesis. Trade qualifies.
- Pair diverging hard (Z-Score divergence > 1.5σ) → SKIP trade. Single-name risk too high.
- Pair confirmation does NOT replace catalyst — both still required.

**Note:** Long+short pair execution is deferred to Phase 3 (requires shorting workflow).

### 6. Composed Entry Decision

Every entry must clear ALL of:

**Layer A — Catalyst (existing):** documented catalyst, sector momentum, RSI trigger, volume, R:R ≥ 2:1, all checklist items.

**Layer B — Quant (new):** Z-Score |≥ 2.0|, VIX regime allows entry, pair confirms (or doesn't diverge >1.5σ).

If either layer fails → SKIP. Log which layer failed and why. Patience rule still applies: zero trades is still better than a forced trade.

---

## Strategy Backlog (Research, Don't Adopt Yet)

- Phase 2: VCP (Volatility Contraction Pattern) detection — proper Minervini base recognition (multi-contraction tightening + volume dry-up)
- Phase 2: Regime-aware sell-into-strength (partial exit at +20% in choppy regimes, hold-and-trail in confirmed uptrends)
- Phase 3: Pairs trading (coordinated long X, short Y same sector for hedged net-zero market exposure)
- Earnings drift / post-earnings momentum
- News-driven NLP sentiment overlay
- Hidden Markov regime detection (requires ML infra)

Each gets tested, graded, kept or killed based on performance.
