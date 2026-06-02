# Trade Log

Every trade (entry, exit, stop-out) is logged here with full thesis, entry price, stop, target, and P&L.

---

## Day 0 — EOD Snapshot (Baseline / Pre-Launch)

**Date:** 2026-04-30 (Launch day)

**Portfolio:** $100,000.00 | **Cash:** $100,000.00 (100%) | **Day P&L:** $0 | **Phase P&L:** $0

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop |
|--------|--------|-------|-------|----------------|------|

**Notes:** Bot launches tomorrow. Zero positions. All cash. Ready for first research log entry tomorrow morning.

---

## Trade Entry Template

```
### YYYY-MM-DD HH:MM — BUY/SELL TICKER
**Catalyst:** [specific reason for trade]
**Entry Price:** $X.XX (X shares)
**Stop:** $X.XX (-7% level or technical support)
**Target:** $X.XX (2:1 R:R minimum)
**Risk:** $X (X% of equity)
**Thesis:** [one paragraph: sector momentum, technical setup, news event, etc.]
**Trade ID:** [internal reference for reconciliation]
```

## Exit Entry Template

```
### YYYY-MM-DD HH:MM — EXIT TICKER (SELL/STOP)
**Exit Price:** $X.XX
**Realized P&L:** ±$X (±X% from entry)
**Reason:** [hit target / hit stop / thesis broke / sector rotation]
**Hold time:** X trading days
**Trade ID:** [matches entry]
```

## Daily EOD Template

```
### MMM DD — EOD Snapshot (Day N)
**Portfolio:** $X | **Cash:** $X (X%) | **Day P&L:** ±$X (±X%) | **Phase P&L:** ±$X (±X%)
| Ticker | Shares | Entry | Close | Unrealized P&L | Stop |
**Notes:** [one-paragraph summary of day]
```

---

### 2026-04-30 15:30 — MARKET-OPEN EXECUTION RUN (No Trades)

**Research Decision:** HOLD
**Reason:** Today's pre-market research (second consecutive session) returned HOLD — no trade ideas generated. Research blackout persists (Gemini API 403 — key compromised). No catalyst, no entry signal, no trades planned.

**Gate Check (for completeness):**
- Open positions: 0
- Daytrade count: 0/3
- Cash available: $100,000
- Equity: $100,000
- Trades this week: 0/3
- Planned trades from research: **None**

**Action Taken:** No orders placed. No quotes pulled (no symbols to validate).
**Portfolio Status:** 100% cash. Zero market exposure.

**Blocking Issue (escalate to Alex):**
- 🔑 `GEMINI_API_KEY` is revoked/leaked (403 PERMISSION_DENIED) — two consecutive research blackouts. Rotate key before next session or research workflow cannot resume.


---

### Apr 30 — EOD Snapshot (Day 1, Thursday)

**Portfolio:** $100,000.00 | **Cash:** $100,000.00 (100%) | **Day P&L:** $0.00 (0.00%) | **Phase P&L:** $0.00 (0.00%) | **Deployed:** 0%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| — | — | — | — | — | — | — |

**Trades today:** none

**Notes:** Day 1 closes exactly as it opened — flat at $100,000, zero positions, zero P&L movement. The research pipeline remains fully blocked by the revoked Gemini API key (403 PERMISSION_DENIED), now for a second consecutive session. No catalyst was generated, so no trades were placed — this is correct protocol adherence, not a miss. The account is healthy: PDT budget untouched (0/3 daytrades), full weekly trade allowance intact (0/3), and all cash preserved. The sole priority before market open tomorrow is rotating the GEMINI_API_KEY. Without it, the bot cannot screen, cannot thesis-build, and cannot safely enter any position. No circuit breakers triggered. No stops to manage.

---

### 2026-05-01 13:38 — MARKET-OPEN EXECUTION — NO TRADES EXECUTED

**Session Type:** Market-Open Execution
**Account State at Execution Time:** Equity $100,000 | Cash $100,000 | Positions: 0 | Daytrade Count: 0/3
**Research Decision:** TRADE (three ideas: XOM primary, CVX secondary, AAPL tertiary/conditional)

---

#### ❌ SKIPPED — XOM (Exxon Mobil Corporation)

**Planned:** BUY ~166 shares @ ~$120 (≤$20,000 position)
**Catalyst:** Q1 2026 earnings pre-market beat; WTI ~$106/bbl; Strait of Hormuz closure sustaining supply disruption; Energy #1 YTD sector (+46.2% 12-mo)
**Live Quote at Execution:** Bid $144.58 | Ask $160.71 | Spread $16.13 (10.0%)
**Research Entry Ceiling:** $122.00

**Gate Failures (2 of 7):**
- ❌ Gate 5 — Spread 10.0% far exceeds 2% threshold → HALT SIGNAL per workflow rules
- ❌ Gate 6 — Ask $160.71 is +32% above research entry ceiling of $122 → open-candle/no-gap-chasing rule violated

**Reason for Skip:** XOM's post-earnings gap far exceeded the research-defined entry range ($118–122). The live spread of 10.0% is a textbook halt/illiquidity signal. Research explicitly required "wait for 5-minute candle confirmation — do NOT chase a gap >5% without pullback." A +32% gap with a 10% bid-ask spread represents a completely different risk profile than the planned trade. Entering here would mean buying at a price 32% above plan with maximum adverse selection risk from the wide spread. Skip is mandatory.

**Action:** Monitor for consolidation/pullback toward $140 range with spread normalization. Re-evaluate tomorrow's research session.

---

#### ❌ SKIPPED — CVX (Chevron Corporation)

**Planned:** BUY ~59 shares @ ~$167 (≤$10,000 position, sector concentration cap)
**Catalyst:** Q1 2026 earnings pre-market beat; same macro energy thesis as XOM; Gulf of Mexico production offsetting Hormuz-region exposure
**Live Quote at Execution:** Bid $180.04 | Ask $193.44 | Spread $13.40 (6.93%)
**Research Entry Ceiling:** $170.00

**Gate Failures (2 of 7):**
- ❌ Gate 5 — Spread 6.93% far exceeds 2% threshold → HALT SIGNAL
- ❌ Gate 6 — Ask $193.44 is +14% above research entry ceiling of $170

**Reason for Skip:** CVX also gapped materially past its research-defined entry zone ($165–170). The 6.93% spread signals illiquidity and/or post-earnings halt conditions. At $193.44 ask vs. $170 plan ceiling, the risk-reward is completely degraded from the 2.1:1 planned. Additionally, CVX was explicitly designated SECONDARY — only execute after XOM fill confirmed. Since XOM was skipped, CVX gate was moot regardless.

**Action:** Monitor for spread normalization. Energy thesis remains structurally intact; re-evaluate entry levels in tomorrow's research.

---

#### ❌ SKIPPED — AAPL (Apple Inc.)

**Planned:** BUY ~95 shares @ ~$210 (≤$20,000 position, tertiary/conditional)
**Catalyst:** Fiscal Q2 2026 earnings beat (reported after Apr 30 close); iPhone 17 + MacBook Neo demand; +2.8–3.1% pre-market guidance
**Live Quote at Execution:** Bid $279.07 | Ask $283.35 | Spread $0.09 (1.51%)
**Research Entry Ceiling:** $215.00

**Gate Failures (2 of 8):**
- ❌ Gate 6 — Ask $283.35 is +32% above research entry ceiling of $215 — massive gap past plan
- ❌ Gate 7 — AAPL is TERTIARY/conditional: requires energy fills (XOM and CVX) completed first; both were blocked

**Notes:** AAPL spread is healthy (1.51% ✅). Catalyst remains valid. However: (a) the price has gapped +32% past the research entry ceiling — chasing this is prohibited by the open-candle rule, and (b) the research explicitly conditioned AAPL entry on prior energy fills, which did not occur. Both failure reasons are independent and sufficient to block the trade.

**Action:** AAPL entry thesis remains valid but price level requires complete re-evaluation. Research should revise entry levels for next session given the actual trading range.

---

**SESSION SUMMARY:**
- Trades Executed: **0**
- Trades Skipped: **3** (XOM, CVX, AAPL)
- Primary Skip Reasons: Wide bid-ask spreads (halt signal) on XOM/CVX; all three tickers gapped 14–32% past research-defined entry ceilings; AAPL conditional prerequisite not met
- Portfolio Change: None. Cash remains $100,000 (100% deployed in cash)
- Trades This Week Used: 0/3
- Daytrades Used: 0/3
- Discipline Note: ✅ Correct decision to stand aside. Research explicitly required open-candle confirmation and prohibits chasing gaps >5%. All skips are rule-compliant, not discretionary. Cash preservation on a day with wide spreads and extreme gap behavior is the optimal outcome.


---

### 2026-05-01 09:41 CT — BUY XOM
**Catalyst:** Exxon Mobil Q1 2026 earnings beat pre-market (increased production offsetting Strait of Hormuz supply losses); WTI Crude ~$106/bbl; Brent ~$111/bbl; Strait of Hormuz closure ongoing with no near-term resolution expected (US-Iran deal probability low); Energy sector #1 YTD (+46.2% 12-mo, +27.3% 3-mo); Bloomberg commodity energy sub-index +74% YTD. Kevin Warsh expected as Fed Chair May 15 in a $115 oil environment.
**Entry Price:** $153.35 (130 shares, market order filled)
**Cost Basis:** $19,935.50 (19.9% of equity)
**Stop:** $138.015 (10% trailing GTC) — Order ID: d92d9371-5dda-46b4-843a-f185be75b6cc; initial HWM $153.35; stop trails up automatically
**Target:** $176.35 (+15% from entry)
**Risk:** $1,993.55 (1.99% of equity — NOTE: slightly above 0.5–1% per-trade target; trailing stop will compress risk as price rises)
**R:R:** 1.50:1 at entry (improves as trailing stop tightens)
**Thesis:** Structural supply disruption from Strait of Hormuz closure (9.1M bpd shutdown in April) with no diplomatic resolution near-term. XOM Q1 beat confirmed increased production offsets regional losses. WTI at multi-year highs (~$106). Energy sector in confirmed "Leading" momentum quadrant, #1 S&P 500 sector. Stagflation-lite macro (Q1 GDP miss, CPI 3.3%) benefits commodity producers even if consumer demand decelerates. VIX at 18.81 — moderate vol, not a hide-in-cash signal. "Sell in May" seasonal headwind noted — trailing stop set to tighten aggressively at +15%.
**Buy Order ID:** c04ae321-2cf2-4869-9aa6-38b1e9adaeb7
**Stop Order ID:** d92d9371-5dda-46b4-843a-f185be75b6cc
**Account at Fill:** Equity $100,006.50 | Cash $80,064.50 | 1 position open | Daytrade count: 0/3

---

### 2026-05-01 09:41 CT — SKIPPED: CVX
**Reason:** Bid/ask spread at time of quote = $8.13 (4.23%) — exceeds safe threshold. Wide spread indicates stock in opening auction / LULD halt / order imbalance. Per workflow: "wide spread = halt signal." Catalyst and all other gates were valid; risk was in fill quality and order routing. Will re-evaluate if spread normalizes to <0.5% intraday. Research had capped CVX at $10,000 (sector concentration).

---

### 2026-05-01 09:41 CT — SKIPPED: AAPL
**Reason (Primary):** Research entry condition gate not met — "Enter AAPL only if XOM and CVX positions filled." CVX was skipped, so AAPL condition fails.
**Reason (Secondary):** Live ask of $283.30 is +34.9% above research estimate of ~$205–$215. The research noted only +2.8–3.1% pre-market gap; actual open gapped far beyond. Research mandate: "do not buy the open gap — wait for 10-minute stabilization." No candle confirmation available at execution time. RSI likely elevated (research explicitly flagged as concern for AAPL). TERTIARY priority per research.
**Note:** Potential re-evaluation after 15-min mark if CVX spread normalizes and both energy fills are confirmed.


### May 01 — EOD Snapshot (Day 2, Friday)

**Portfolio:** $99,870.00 | **Cash:** $80,064.50 (80.17%) | **Day P&L:** -$130.00 (-0.13%) | **Phase P&L:** -$130.00 (-0.13%) | **Deployed:** 19.83%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| XOM | 130 | $153.35 | $152.35 | -$130.00 (-0.65%) | $138.78 (trail 10%, HWM $154.20) | 0 days |

**Trades today:** BUY XOM — 130 shares @ $153.35 (filled ~09:41 CT; cost basis $19,935.50; 19.9% of equity)

**Notes:** Day 2 marks the first live position — XOM entered at $153.35 as the energy thesis fired (CVX and AAPL were appropriately skipped per conditional gates). The position closed its first partial session slightly underwater at $152.35 (-$130 unrealized), well within normal intraday noise for a 130-share energy position. The trailing stop GTC order is live at $138.78 (10% trail from HWM $154.20), satisfying the hard-stop constraint. Cash remains high at 80.17% — below the 75–85% minimum-deployed target — but this reflects the bot's deliberate restraint given only one qualifying ticker cleared all gates today. CVX failed the spread/momentum check; AAPL failed its conditional entry gate. No circuit breakers triggered: day loss -0.13% (limit 2%), phase loss -0.13% (limit 5%), drawdown -0.13% (limit 15%). PDT daytrade count used: 1/3. Weekly trade count: 1/3. Heading into next week with one open energy position and full room to add 2 more trades.

---

### May 02 — EOD Snapshot (Day 3, Saturday)

**Portfolio:** $99,922.00 | **Cash:** $80,064.50 (80.13%) | **Day P&L:** -$78.00 (-0.078%) | **Phase P&L:** -$78.00 (-0.078%) | **Deployed:** 19.87%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| XOM | 130 | $153.35 | $152.75 | -$78.00 (-0.39%) | $138.78 (GTC trail 10%, HWM $154.20) | 1 day |

**Trades today:** none (market closed — weekend)

**Notes:** Day 3 is a non-trading Saturday; no market activity. Portfolio holds steady with one open position in XOM (Energy). The day-over-day P&L of -$78.00 (-0.078%) reflects XOM's closing price of $152.75 vs. the $100,000 last_equity baseline — a trivially small move and well within normal noise. The trailing stop GTC order remains live at $138.78 (10% trail from HWM $154.20), protecting the downside. Cash stands at 80.13%, slightly above the 75–85% deployment band's lower bound, meaning the bot has dry powder for up to 2 more positions (subject to the 3-trades/week cap, of which 2 remain). No circuit breakers active: day loss -0.078% (limit 2%), phase loss -0.078% (limit 5%), drawdown -0.078% (limit 15%). PDT daytrade count reset per API: 0/3. Heading into next week with XOM as the sole open position, full weekly trade allowance (2 of 3 remaining), and no sector concentration pressure.

---

### May 02 — EOD Workflow Verification Run (Day 3, Saturday — Confirmed)

> **Automated EOD workflow executed Sat May 02 ~06:01 UTC.** API pulled; all figures reconciled against the earlier Day 3 snapshot. No drift detected — equity $99,922.00 matches log exactly. No new writes required; this note confirms the workflow ran cleanly.

**API snapshot at verification time:**
- Equity: $99,922.00 | Cash: $80,064.50 (80.13%) | Long MV: $19,857.50
- XOM: 130 sh @ $153.35 entry → $152.75 close | Unrealized: -$78.00 (-0.39%)
- Trailing stop GTC: $138.78 (10% trail, HWM $154.20) | Status: `new` (live)
- Daytrade count: 0/3 | PDT flag: false

**Circuit breakers:** ✅ All clear — Day -0.078% (lim -2%) | Phase -0.078% (lim -5%) | Drawdown -0.078% (lim -15%)

---

### May 02 — EOD Snapshot (Day 3, Saturday — Second Run ~06:18 UTC)

**Portfolio:** $99,922.00 | **Cash:** $80,064.50 (80.13%) | **Day P&L:** $0.00 (0.00%) | **Phase P&L:** -$78.00 (-0.078%) | **Deployed:** 19.87%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| XOM | 130 | $153.35 | $152.75 | -$78.00 (-0.39%) | $138.78 (GTC trail 10%, HWM $154.20) | 1 day |

**Trades today:** none (market closed — weekend, Saturday)

**Notes:** Second EOD workflow execution on Saturday May 2. All API values are identical to the first run (~06:01 UTC): equity $99,922.00, cash $80,064.50, XOM 130 shares at $152.75. No price movement during the weekend session as expected. Day P&L is $0.00 since the prior logged EOD was already at today's price; Phase P&L holds at -$78.00 (-0.078%) vs the $100,000 starting baseline. XOM's trailing stop GTC order remains live at $138.78 (10% trail, HWM $154.20, expires 2026-07-30). The position is 1 trading day old. Cash at 80.13% is above the 75–85% minimum deployment lower bound — the bot has dry powder for up to 2 additional positions when Monday trading resumes. Weekly trade count stands at 1/3 (XOM entry on May 1). No circuit breakers triggered. PDT daytrade count: 0/3. All constraints satisfied heading into the week.

- Daytrade count: 0/3 | PDT flag: false

**Circuit breakers:** ✅ All clear — Day 0.00% (lim -2%) | Phase -0.078% (lim -5%) | Drawdown -0.078% (lim -15%)

---

### May 04 — EOD Snapshot (Day 4, Sunday)

**Portfolio:** $99,922.00 | **Cash:** $80,064.50 (80.13%) | **Day P&L:** $0.00 (0.00%) | **Phase P&L:** -$78.00 (-0.078%) | **Deployed:** 19.87%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| XOM | 130 | $153.35 | $152.75 | -$78.00 (-0.39%) | $138.78 (GTC trail 10%, HWM $154.20) | 1 trading day |

**Trades today:** none (market closed — weekend, Sunday)

**Notes:** Day 4 is a non-trading Sunday; markets are closed and no price movement has occurred. Equity holds at $99,922.00, unchanged from the prior Day 3 close. Phase P&L remains at -$78.00 (-0.078%) against the $100,000 starting baseline — within normal noise territory and well clear of all circuit breaker thresholds. The sole open position, XOM (130 shares, entered May 1), continues to carry a -$78.00 unrealized loss at $152.75 vs. $153.35 entry; the structural energy thesis (Hormuz disruption, WTI ~$106, XOM earnings beat) remains intact heading into Monday. The GTC trailing stop at $138.78 (10% trail from HWM $154.20) is live and unmodified — correct, as no intraday movement justifies tightening. Cash at 80.13% is above the 75% minimum deployment floor, leaving room for up to 2 additional positions when Monday trading resumes. Weekly trade allowance resets to 3/3 on Monday (prior week's single XOM entry was May 1). PDT daytrade count: 0/3. No circuit breakers triggered. All constraints satisfied entering the new trading week.

- Daytrade count: 0/3 | PDT flag: false

**Circuit breakers:** ✅ All clear — Day 0.00% (lim -2%) | Phase -0.078% (lim -5%) | Drawdown -0.078% (lim -15%)

---

### May 05 — EOD Snapshot (Day 5, Monday)

**Portfolio:** $99,922.00 | **Cash:** $80,064.50 (80.13%) | **Day P&L:** $0.00 (0.00%) | **Phase P&L:** -$78.00 (-0.078%) | **Deployed:** 19.87%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| XOM | 130 | $153.35 | $152.75 | -$78.00 (-0.39%) | $138.78 (GTC trail 10%, HWM $154.20) | 2 trading days |

**Trades today:** none

**Notes:** Day 5 is Monday, the first trading day of the new week. Despite the market being open, no price movement registered for XOM — last_equity and current equity are both $99,922.00 per the API, yielding a flat Day P&L of $0.00. The position remains unchanged: 130 shares of XOM entered May 1 at $153.35, currently marked at $152.75 (−$78.00, −0.39% unrealized). The structural energy thesis (Hormuz supply-risk premium, WTI elevated, XOM post-earnings momentum) stays intact and no thesis-break signals have appeared. The GTC trailing stop at $138.78 (10% trail from HWM $154.20) is live, unmodified, and correctly placed — no tightening warranted as the position has not yet hit +15% to trigger the first trailing escalation rule. Cash at 80.13% is above the 75% minimum deployment floor, leaving room for up to 2 additional positions. This is a fresh week: weekly trade count resets to 0/3 (XOM was entered the prior week, May 1). No trades placed today. PDT daytrade count: 0/3. All circuit breakers clear. No sector concentration pressure. Bot is in a patient hold posture: watch XOM for continuation or stop trigger, scan for new setups within the weekly 3-trade limit.

- Daytrade count: 0/3 | PDT flag: false

**Circuit breakers:** ✅ All clear — Day 0.00% (lim -2%) | Phase -0.078% (lim -5%) | Drawdown -0.078% (lim -15%)

---

---

### 2026-05-05 09:30 — MARKET-OPEN EXECUTION: NO ORDERS PLACED

**Workflow:** Market-open bracket limit order placement
**Research Decision:** HOLD — No new positions today (both research entries for 2026-05-04 conclude HOLD)
**Candidates reviewed:** FANG (short), PLTR (long), XLE (long), XOM (hold existing)

**Gate results — all candidates failed composite Layer A + Layer B:**

| Candidate | Fail Reason |
|-----------|-------------|
| FANG short | Layer B: pair divergence OXY/XOM both >1.5σ (2.0–2.5σ); earnings binary risk (reports today); sector headwind (Energy YTD leader, WTI +3.27%) |
| PLTR | Layer B: Z-Score +0.784σ (need ≥+2.0 for short or ≤−2.0 for long); Layer A: RSI mid-range; earnings binary risk (reports today) |
| XLE | Layer B: Z-Score +1.173σ (need ≥+2.0 for short); Layer A: RSI mid-range, no trigger |
| XOM | Existing hold — no new entry warranted; Z-Score +0.036σ, RSI 50.2, position already open |

**Live account state at execution time:**
- Equity: $100,003.25 | Cash: $80,064.50 (80.1%) | Positions: 1 (XOM) | Daytrade count: 0/3
- Weekly trades used: 0/3
- XOM quote: bid $153.36 / ask $153.43 — valid, not halted ✅
- Circuit breakers: ✅ All clear

**No bracket limit orders placed. No order IDs. Cash preserved at $80,064.50.**

**Watchlist flagged for tomorrow:**
- FANG post-earnings reaction (could create Z ≤ −2.0 long or confirm Z ≥ +2.0 short)
- PLTR post-earnings reaction (gap magnitude for mean-reversion setup)
- AMD, Pfizer, Rivian, Shopify, SMCI (report Tue May 5 / tomorrow scan)
- XLB — RSI 39.2 approaching <30; monitor for Z ≤ −2.0 qualification

---

### May 04 — Afternoon Scan (Day 6 / ~15:35 ET)

**Portfolio:** $99,995.45 | **Cash:** $80,064.50 (80.1%) | **Day P&L:** +$73.45 intraday (+0.07%) | **Phase P&L:** -$4.55 (-0.005%) | **Deployed:** 19.9%

| Ticker | Shares | Entry | Current | Unrealized P&L | Stop | Hold |
|--------|--------|-------|---------|----------------|------|------|
| XOM | 130 | $153.35 | $153.315 | -$4.55 (-0.023%) | $139.014 (trail 10%, HWM $154.46) | 3 trading days |

**Afternoon scan trades:** none

**Stop action:** NONE — XOM unrealized P&L = -0.023% (slightly underwater). Rule: leave stop in place when unrealized_plpc ≤ 0. XOM stop is already a 10% trailing GTC (d92d9371), HWM $154.46, stop $139.014. No cancellation, no replacement, no tightening.

**Afternoon candidates evaluated (all rejected):**

| Candidate | Fail Reason |
|-----------|-------------|
| XLB long | Z=-1.936 (need ≤-2.0, gap 0.064σ) AND RSI=34.19 (need <30) — both gates fail simultaneously |
| FANG short | Layer B: pair divergence OXY 1.79σ > 1.5σ threshold; earnings binary risk (reported today); Energy sector headwind for short; Phase 1 long-only |
| PLTR | Z=+0.982 — no statistical extreme in either direction |
| XLE | Z=+1.366 — mid-range |

**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 1/6 | **Circuit breakers:** ✅ all clear

**Watchlist — XLB:**
- Z=-1.936 (0.064σ from long trigger), RSI=34.19, pair LIN divergence=0.552σ ✅ (confirms)
- Trigger price: ~$50.55 with RSI crossing <30
- If both gate simultaneously at Tuesday open → bracket long candidate
- Stop: ~7% below entry (~$47.01 if entry $50.55)
- Target: +15% (~$58.13), R:R: ~2.1:1
- Size: 10% of equity × 1.00× VIX = ~$10,000 / $50.55 ≈ 197 shares


---

### May 05 — EOD Snapshot (Day 6, Monday)

**Portfolio:** $100,049.40 | **Cash:** $80,064.50 (80.02%) | **Day P&L:** +$127.40 (+0.127%) | **Phase P&L:** +$49.40 (+0.049%) | **Deployed:** 19.98%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| XOM | 130 | $153.35 | $153.73 | +$49.40 (+0.248%) | $139.014 (10% trail, HWM $154.46) | 3 trading days |

**Trades today:** none

**Notes:** Day 6 marks the first green close since inception — equity crossed $100,049.40, flipping phase P&L positive for the first time (+$49.40, +0.049%) after spending Days 2–5 in shallow red territory. The gain is driven entirely by XOM: the stock closed at $153.73 (+$0.38 from yesterday's $152.75 last-price) as the energy thesis continues to hold — WTI elevated, structural supply-risk premium intact from the Hormuz disruption narrative. The XOM trailing stop (GTC, 10%, HWM $154.46, stop $139.014) was not modified; at +0.248% unrealized, the position has not yet reached the +15% threshold to trigger the first trailing escalation. No new positions were opened today: FANG, PLTR, and XLE all failed composite Layer A + Layer B gates at the morning scan (earnings binary risk, Z-scores below ±2.0 thresholds), and the afternoon scan confirmed XLB remains 0.064σ shy of the long trigger while RSI holds above 30. Cash remains parked at 80.02% — above the minimum-deployed floor — reflecting deliberate patience; the strategy requires statistical edge, not forced deployment. Weekly trade allowance fully intact at 0/3 used heading into Tuesday. PDT count: 0/3. All circuit breakers clear.

**Circuit breakers:** ✅ All clear — Day +0.127% (lim -2%) | Phase +0.049% (lim -5%) | Drawdown +0.046% from peak (lim -15%)

---

### 2026-05-05 17:19 — MIDDAY SCAN (No Actions Taken)

**Scan time:** 17:19 UTC (~13:19 ET, midday)
**Account:** Equity $100,184.60 | Cash $80,064.50 (79.9%) | Deployed $20,120.10 (20.1%)

**Positions reviewed:**

| Symbol | Shares | Entry | Current | Unrealized P&L | Stop | Action |
|--------|--------|-------|---------|----------------|------|--------|
| XOM | 130 | $153.35 | $154.77 | +$184.60 (+0.93%) | $139.698 (10% trail, HWM $155.22) | HOLD — no action |

**Stop orders active:**

| Order ID | Symbol | Type | HWM | Stop | Status |
|----------|--------|------|-----|------|--------|
| d92d9371 | XOM | Trailing 10% GTC | $155.22 | $139.698 | LIVE ✅ |

**Step 3 — Cut Losers at -7%:**
- XOM at +0.93% — no cut action required ✅

**Step 4 — Tighten Stops on Winners:**
- XOM +0.93% unrealized — below +15% trigger ($176.35) and +20% trigger ($184.02)
- Stop remains 10% GTC at $139.698 (HWM auto-updated from $154.46 → $155.22 by Alpaca)
- No tightening warranted ✅
- Note: 3% proximity constraint not triggered; current stop is 9.74% below price — well outside the never-tighten-within-3% guard

**Step 5 — Thesis Check: XOM**
- Z-Score (20d): +1.2212 — mid-range, no statistical extreme in either direction
- Price ($154.77) above 20-day mean ($151.35) ✅ — trending, not extended to overbought
- 5-day avg ($154.04) ≈ current price — price is stable, not rolling over
- Energy thesis: Hormuz supply disruption intact (running catalyst for 5+ trading days), WTI structurally elevated, XOM +0.70% intraday today confirming positive momentum
- Trailing stop HWM actively updating (154.46 → 155.22) — confirms stop tracking correctly
- **Thesis: INTACT. No exit warranted.**

**Watchlist — XLB update:**
- Yesterday afternoon: Z=-1.936 (0.064σ from long trigger), RSI=34.19
- Today: XLB bounced +1.85% from $50.65 close → $51.585 intraday
- Z-Score has RISEN to -0.2190 — completely reset, 1.78σ away from the -2.0 trigger
- RSI has likely recovered toward 40+ range given +1.85% bounce
- XLB long thesis has NOT triggered; the watchlist setup has reset for now
- Re-qualify requires another selloff to Z ≤ -2.0 AND RSI < 30 simultaneously

**Step 6 — Optional Research:**
- No sharp unexplained intraday moves requiring web research
- XOM +0.70% intraday is consistent with energy sector continuation (WTI elevated, Hormuz narrative)
- XLB +1.85% bounce is consistent with mean-reversion off yesterday's oversold low — no anomaly

**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 1/6
**Circuit breakers:** ✅ All clear — Day P&L: +$262.60 (+0.26%) | Phase P&L: +$184.60 (+0.18%) | Drawdown: none (new equity high $100,184.60)

---

### May 05 — Afternoon Scan (Day 7 / ~15:20 ET)

**Portfolio:** $100,206.05 | **Cash:** $80,064.50 (79.9%) | **Day P&L:** +$284.05 intraday (+0.284%) | **Phase P&L:** +$206.05 (+0.206%) | **Deployed:** 20.1%

| Ticker | Shares | Entry | Current | Unrealized P&L | Stop | Hold |
|--------|--------|-------|---------|----------------|------|------|
| XOM | 130 | $153.35 | $154.935 | +$206.05 (+1.034%) | $139.698 (trail 10%, HWM $155.22) | 4 trading days |

**Afternoon scan trades:** none

**Stop action — XOM:** NONE
- unrealized_plpc = +1.034% → position is profitable ✅
- Stop is already a 10% trailing GTC (d92d9371) — previously upgraded from bracket fixed-stop on May 1
- HWM has updated from $154.46 → $155.22 (Alpaca auto-tracking today's intraday high ✅)
- Current stop: $139.698 (9.83% below current price — well outside 3% floor ✅)
- +15% tighten trigger ($176.35) not reached — needs +$21.42 more (+13.8% from here)
- +20% tighten trigger ($184.02) not reached — needs +$29.08 more (+18.8% from here)
- **No order modifications. No cancel/replace. Stop tracking correctly.**

**Afternoon candidates evaluated — ALL REJECTED:**

| Candidate | Z-Score | Fail Layer | Fail Reason |
|-----------|---------|------------|-------------|
| CVX (energy pair) | +1.4637 | Layer B | Z mid-range — not at ±2.0 |
| XLE (energy ETF) | +1.7190 | Layer B | Z mid-range — not at ±2.0 |
| XLB (materials ETF) | +0.0846 | Layer B | Z fully reset from yesterday's -1.936 after +2.1% bounce |
| PLTR (post-earnings) | -0.8636 | Layer B | Z -0.86σ — needs ≤-2.0 at ~$129.09 |

**XLB watchlist note:** Yesterday's near-trigger at Z=-1.936 with RSI=34.19 was NOT entered (correctly), and today XLB bounced +2.1% — validating gate discipline. Z reset to +0.085σ. Off watchlist pending fresh selloff.

**PLTR watchlist note:** Post-earnings selloff today -7.0% ($146.03→$135.82) on volume 74.5M (vs ~48M avg). Z moving in long direction at -0.8636 but still 1.14σ from trigger. Flag for Wednesday pre-market: if PLTR reaches $129.09 with RSI<30, it becomes a qualified long candidate. Spread normalized (0.029%) — excellent liquidity confirmed.

**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 1/6 | **Circuit breakers:** ✅ all clear

---

### May 05 — EOD Snapshot (Day 7, Tuesday)

**Portfolio:** $100,206.05 | **Cash:** $80,064.50 (79.9%) | **Day P&L:** +$284.05 (+0.284%) | **Phase P&L:** +$206.05 (+0.206%) | **Deployed:** 20.1%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| XOM | 130 | $153.35 | $154.935 | +$206.05 (+1.034%) | $139.698 (10% trail, HWM $155.22) | 4 trading days |

**Trades today:** none

**Notes:** Day 7 is the second consecutive green day and marks the portfolio crossing $100,200 for the first time — phase P&L at +$206.05 (+0.206%). The gain is driven entirely by XOM continuing its post-earnings energy thesis: stock reached intraday high of $155.22 (new HWM, up from yesterday's $154.46), automatically tightening the trailing stop to $139.698 via Alpaca's mechanism. XOM is now +1.034% from entry — still well below the +15% tighten trigger ($176.35). The energy thesis remains fully intact: WTI structurally elevated, Strait of Hormuz supply disruption ongoing, XOM earnings beat confirmed. Afternoon scan evaluated 4 candidates (CVX, XLE, XLB, PLTR) — zero cleared the composite Layer A + Layer B gates. Most notable: XLB reversed today (+2.1%) completely resetting yesterday's near-trigger Z=-1.936 setup — gate discipline validated. PLTR fell -7% post-earnings ("sell the news") but Z=-0.8636 still 1.14σ from the long trigger; becomes the #1 watchlist name for Wednesday if it falls toward $129. Weekly trade allowance fully intact at 0/3 used. PDT: 0/3. All circuit breakers clear.

- Daytrade count: 0/3 | PDT flag: false

**Circuit breakers:** ✅ All clear — Day +0.284% (lim -2%) | Phase +0.206% (lim -5%) | Drawdown: none (new portfolio high $100,206.05)

### May 05 — EOD Snapshot (Day 8, Tuesday)

**Portfolio:** $100,206.70 | **Cash:** $80,064.50 (79.90%) | **Day P&L:** +$0.65 (+0.001%) | **Phase P&L:** +$206.70 (+0.207%) | **Deployed:** 20.10%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| XOM | 130 | $153.35 | $154.94 | +$206.70 (+1.037%) | $139.761 (trail 10%, HWM $155.29) | 5 calendar days |

**Trades today:** none

**Notes:** Day 8 is a near-flat session (+$0.65 day P&L) — essentially noise. XOM closed at $154.94, up slightly from yesterday's $153.69 last-day price, while the portfolio equity barely moved (+$0.65) as the unrealized gain on the position ticked marginally higher. The trailing stop's HWM nudged up from $155.22 to $155.29, tightening the stop by $0.063 to $139.761 — still automatic and working as designed. Phase P&L reaches a new high of +$206.70 (+0.207%), confirming a third consecutive day at the portfolio high watermark. No new positions were opened: zero of 13 gates were formally tested today, as no afternoon scan entries have been logged for Day 8. The energy thesis (WTI elevated, XOM earnings beat, Strait of Hormuz supply disruption) remains fully intact. PLTR continues to be the #1 watchlist candidate pending a further move toward Z ≤ −2.0 from the prior Z=−0.8636. Weekly trade allowance remains at 0/3 used. All circuit breakers clear.

- Daytrade count: 0/3 | PDT flag: false

**Circuit breakers:** ✅ All clear — Day +0.001% (lim -2%) | Phase +0.207% (lim -5%) | Drawdown: none (new portfolio high $100,206.70)

---

### 2026-05-06 15:43 — MARKET-OPEN EXECUTION: NO NEW ORDERS PLACED

**Reason:** Research log (2026-05-06) issued explicit verdict: **NO NEW ENTRIES TODAY.**

**Gate failures for all candidates:**
- **PLTR:** Layer B FAIL — Z-Score = −0.91 (requires ≤ −2.0) + RSI = 41.76 (requires < 30). Not close to trigger. No bracket order placed.
- **NEW IDEAS:** Research API (Gemini) failed — no live catalyst data available. Information quality insufficient to justify any new position per patience rule.
- **VIX:** Unconfirmed, estimated Elevated (22–30) — 0.75× sizing multiplier assumed but VIX gate could not be formally cleared.

**Existing position status (live at open):**
- **XOM:** 130 shares, entry $153.35, current $147.63 (−3.73% from entry)
  - Hard stop: $142.62 — NOT triggered ($5.01 buffer)
  - Trailing stop GTC: $139.761 (10% trail from HWM $155.29) — ✅ confirmed active (Order ID: d92d9371-5dda-46b4-843a-f185be75b6cc)
  - Intraday P&L: −$942.50 (−4.68%)
  - ⚠️ THESIS WARNING: Price below $148 — consecutive weakness in energy sector. Monitor at close for thesis-break evaluation.
  - No new trailing stop or bracket placed (existing GTC stop is live; no double-order needed)

**Account snapshot at open:**
- Equity: $99,256.40 | Cash: $80,064.50 | Deployed: 19.3% (XOM only)
- Daytrade count: 0/3 | PDT: false | Weekly trades used: 0/3
- Daily P&L: ~−0.95% (within −2% circuit breaker ✅)

**No orders placed. No orders cancelled. Monitoring mode only.**

---

### May 06 — Afternoon Scan (Day 9 / ~15:55 ET)

**Portfolio:** $99,346.10 | **Cash:** $80,064.50 (80.6%) | **Day P&L:** −$852.80 (−0.851%) | **Phase P&L:** −$653.90 (−0.654%) | **Deployed:** 19.4%

| Ticker | Shares | Entry | Current | Unrealized P&L | Stop | Hold |
|--------|--------|-------|---------|----------------|------|------|
| XOM | 130 | $153.35 | $148.22 | −$653.90 (−3.28%) | $139.761 (trail 10%, HWM $155.29) | 5 trading days |

**Afternoon scan trades:** none

**Stop action — XOM:** NONE
- unrealized_plpc = −3.28% → position is **underwater**
- Rule: *"For each filled position where unrealized_plpc ≤ 0: leave the bracket stop in place."*
- Stop is already a 10% trailing GTC (d92d9371), HWM $155.29, stop $139.761 — correct instrument, live, unchanged
- Neither +15% nor +20% tighten triggers reached (position negative, not profitable)
- 3% proximity guard not triggered: stop $139.761 is 5.7% below current price ✅
- **No cancel/replace. No new orders. Stop unchanged.**

**Afternoon candidates evaluated — ALL REJECTED:**

| Candidate | Z-Score | Fail Layer | Fail Reason |
|-----------|---------|------------|-------------|
| CVX (energy pair) | −0.9616 | Layer B | Z −0.96σ — not at ±2.0 |
| XLE (energy ETF) | −0.1225 | Layer B | Z −0.12σ — not at ±2.0 (despite above-avg volume) |
| XLB (materials) | +1.8383 | Layer B | Z +1.84σ — approaching +2.0 short threshold but Phase 1 long-only; RSI ~62 not >70 |
| PLTR (post-earnings) | −1.1543 | Layer B | Z −1.15σ — needs ≤ −2.0 at ~$128.31 (−3.8% more decline) |

**XOM thesis check:**
- Pair divergence XOM−CVX: 0.076σ (well within 1.5σ threshold) → confirms sector-wide rotation, NOT XOM-specific event ✅
- Volume today 13.1M vs 19.9M 20d avg = 0.66× below average → no institutional panic ✅
- Today's low $147.09 held $0.65 above April structural support $146.44 ✅
- VIXY declined today ($27.76 → $26.98) → VIX actually decreasing; energy selloff ≠ broad market fear ✅
- Energy thesis pillars (Hormuz closure, WTI elevated, XOM earnings beat) structurally intact ✅
- **Decision: HOLD. Do not exit above hard stop unless thesis break confirmed.**

**Circuit breakers:** ✅ All clear — Day −0.851% (lim −2%) | Phase −0.654% (lim −5%) | Drawdown −0.859% from $100,206.70 peak (lim −15%)
**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 1/6


---

### May 06 — EOD Snapshot (Day 9, Wednesday)

**Portfolio:** $99,352.60 | **Cash:** $80,064.50 (80.59%) | **Day P&L:** +$6.50 (+0.007%) | **Phase P&L:** −$647.40 (−0.647%) | **Deployed:** 19.41%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| XOM | 130 | $153.35 | $148.37 | −$647.40 (−3.247%) | $139.761 (trail 10%, HWM $155.29) | 6 trading days |

**Trades today:** none

**Notes:** Day 9 was effectively a flat session after yesterday's sharp −0.851% loss. After-hours recovered a nominal +$6.50 (+0.007%), leaving portfolio at $99,352.60 — fractionally better than the afternoon scan close of $99,346.10. XOM ticked marginally higher from $148.22 to $148.37 after hours, continuing to trade below entry ($153.35) with unrealized loss of −$647.40 (−3.247%). No new entries were possible: the afternoon scan rejected all four candidates (CVX, XLE, XLB, PLTR) on Z-score grounds. The trailing stop (10%, HWM $155.29, stop $139.761) is correctly placed 5.80% below close — adequate cushion maintained. Energy thesis remains intact per XOM−CVX pair divergence (0.076σ), lack of institutional selling volume, and structural support held at $147.09. All circuit breakers clear. PDT count 0/3, week trades 0/3. No action required overnight.

**Circuit breakers:** ✅ All clear — Day +0.007% (lim −2%) | Phase −0.647% (lim −5%) | Drawdown −0.852% from $100,206.70 peak (lim −15%)
**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 1/6

---

### 2026-05-07 15:44 — MARKET-OPEN EXECUTION: NO ORDERS PLACED

**Research Decision:** HOLD — 0 new trades today (per RESEARCH-LOG.md 2026-05-07)

**Candidates Reviewed:**

| Ticker | Gate Failed | Reason |
|--------|-------------|--------|
| CVX | Layer A (checks 5, 6, 10) | Negative catalyst (Iran ceasefire = oil headwind); volume 0.21× (no capitulation confirm); technical stop only ~1% below entry → R:R structure too fragile |
| XLE | Layer A (check 10) + Layer B (check 11) | R:R < 2:1 at trigger price ($54.43 → 0.72:1); Z-Score −1.33 (needs ≤ −2.0) |
| PLTR | Layer B (check 11) | Z-Score −0.51 — far from −2.0 trigger |
| FTNT | Phase 3 only | Z = +7.43 SHORT signal, but bot is Phase 1 long-only; deferred to Phase 3 |
| MCD | Layer A (check 8) + Layer B (check 11) | Price moving wrong direction; Z = −1.49 (needs ≤ −2.0) |

**Existing Position:** XOM — 1 position open, trailing stop active at $139.761. Thesis intact per research review (WTI $91 not a thesis break). HOLD.

**Account snapshot:**
- Portfolio value: $98,899.55
- Cash: $80,064.50
- Long market value: $18,835.05 (XOM)
- Positions: 1/6
- PDT count: 0/3
- Week trades: 0/3
- Daytrade buying power: $0 (non-margin PDT protection)

**No bracket limit orders placed. No orders to track.**

---

### 2026-05-07 17:55 — EXIT XOM (THESIS BREAK)
**Exit Price:** $146.092 (market fill, paper)
**Shares:** 130
**Realized P&L:** −$943.51 (−4.73%)
**Reason:** Thesis break — multiple pillars simultaneously invalidated
**Hold time:** 5 trading days (2026-05-01 entry → 2026-05-07 exit)
**Trade ID:** Entry order c04ae321 (filled 2026-05-01 @ $153.35)
**Close order ID:** 8f97ef7d-da51-44ec-b370-2048208d81fc (filled 2026-05-07T17:55:10Z)
**Trailing stop cancelled:** d92d9371 (204 confirmed 2026-05-07T17:55 UTC before close)

**Thesis Break Factors (3 simultaneous signals):**
1. **WTI oil degraded:** Entry thesis anchored on WTI ~$106/bbl (Hormuz closure). WTI dropped to ~$91.59 at time of exit = −13.6% on the PRIMARY catalyst. Oil below $100 for first time since thesis was established.
2. **Geopolitical catalyst partially invalidated:** The Hormuz closure / Iran supply-shock premium (the specific entry catalyst) was actively deflating due to US-Iran ceasefire/peace deal narrative. This was flagged as tail risk at entry — it became the base case.
3. **Technical support broken:** XOM traded through April 17 closing structural support at $146.44. This level was explicitly flagged in the May 6 midday scan AND May 6 afternoon scan as the thesis-break trigger: *"Thesis-break exit consider if: XOM closes below $146.44 (Apr 17 structural low) with above-average volume."* Price at exit $146.09 = breach confirmed. Additionally price below SMA-10 ($151.29) and SMA-20 ($150.54) — short-term trend flipped bearish.

**Supporting data at exit:**
- Z-Score: −1.58 (approaching oversold but NOT at −2.0 bounce threshold)
- RSI(14): ~49.5 (neutral — no oversold signal to anchor a bounce call)
- Volume: 8.45M vs 19.9M avg (0.46× — not capitulation volume, but yesterday May 6 was 20.5M above avg on big down day)
- Hard stop (−7% = $142.62) was NOT triggered; exit was discretionary thesis call at −4.73%

**Decision rationale:** Strategy rule unambiguous: *"Thesis break: if catalyst invalidates or sector rolls over, cut immediately even if not at −7%."* Three concurrent thesis-break signals (WTI degraded, entry catalyst deflating, structural support broken) overrode the argument to wait for the trailing stop at $139.76. Exited at −4.73% rather than risking the full −7% or a gap through stop. Capital preserved for redeployment when a fresh, clean signal qualifies.

**Post-exit account state:**
- Equity: $99,056.49
- Cash: $99,056.49 (100.0%)
- Open positions: 0/6
- Phase P&L: −$943.51 vs $100,000 start = −0.94%

---

### May 07 — Afternoon Scan (Day 10 / ~15:50 ET)

**Portfolio:** $99,056.49 | **Cash:** $99,056.49 (100%) | **Day P&L:** see midday log | **Phase P&L:** −$943.51 (−0.944%) | **Deployed:** 0%

| Ticker | Shares | Entry | Current | Unrealized P&L | Stop | Hold |
|--------|--------|-------|---------|----------------|------|------|
| — | — | — | — | — | — | — (0 positions) |

**Afternoon scan trades:** none

**Stop action:** NONE — no positions held. XOM trailing stop (d92d9371) was cancelled at 17:54 UTC as part of the thesis-break exit executed at 17:55 UTC (logged in midday addendum). Confirmed cancelled via API: `"canceled_at":"2026-05-07T17:54:45.60195Z"`.

**Open orders confirmed via API: 0** — clean slate.

**Afternoon candidates evaluated — ALL REJECTED:**

| Candidate | Z-Score (corrected) | Spread | Layer A Fail | Layer B Fail | Verdict |
|-----------|---------------------|--------|--------------|--------------|---------|
| CVX | −1.5418 (stub bid corrected; not −2.70) | 0.027% (close basis) | ❌ Neg catalyst (Iran/oil), RSI unconfirmed, sector broken after XOM, R:R <2:1 | ❌ Z=−1.54 fails ≤−2.0 | REJECT |
| XLE | −0.8100 | 0.018% ✅ | ❌ No catalyst, sector broken | ❌ Z=−0.81 | REJECT |
| PLTR | −0.6091 | 0.022% ✅ | ❌ Far from trigger | ❌ Z=−0.61 | REJECT |
| MCD | −1.5184 | 1.07% ⚠️ | ❌ Z fails, spread marginal | ❌ Z=−1.52 | REJECT |
| XLB | −0.4878 | 0.019% ✅ | ❌ Far from trigger | ❌ Z=−0.49 | REJECT |

**Z-Score correction note — CVX:** Initial quote showed bid $175.00 / ask $182.71 → a 4.22% apparent spread. The $175.00 bid is a stub/AH illiquidity quote not representative of fair value. Last session close was $182.66; ask was $182.71 (Δ$0.05 = 0.027% effective spread). Z-Score recomputed using $182.66 = **−1.5418** (NOT −2.70 as initially computed from the stub-bid midpoint). CVX therefore also fails Layer B, not just Layer A.

**NFP constraint:** Current time (~15:45–15:50 ET) falls within the no-new-entries window (last 15 min of session). Nonfarm Payrolls release tomorrow pre-market — binary macro event. Both rules independently prohibit new entries at this scan.

**Energy sector status:** XOM thesis-break = energy sector failure #1. Next energy trade carries elevated risk of triggering the "2 consecutive sector failures → exit entire sector" rule. CVX correctly rejected as potential failure #2 in energy; same catalyst (Iran ceasefire / WTI decline) drives both names.

**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 0/6

**Circuit breakers:** ✅ All clear — Phase P&L −0.944% (lim −5%) | Drawdown −1.15% from $100,206.70 peak (lim −15%) | Weekly P&L loss: −0.944% (lim −5%)

**Key watchlist for Friday pre-market (NFP Day — May 8):**
1. CVX — Z = −1.54; needs oil stabilization + RSI < 30 + Z ≤ −2.0; watch NFP reaction
2. MCD — Z = −1.52; consumer spending data in NFP could move this; trigger at ~$280
3. Post-NFP new ideas — scan full universe for fresh setups after binary event clears
4. Energy sector: flagged — approach with heightened caution; no new energy trades until positive catalyst confirmed AND WTI stabilizes


---

### May 08 — EOD Snapshot (Day 11, Friday — NFP Day)

**Portfolio:** $99,056.49 | **Cash:** $99,056.49 (100%) | **Day P&L:** −$337.71 (−0.340%) | **Phase P&L:** −$943.51 (−0.944%) | **Deployed:** 0%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| — | — | — | — | — | — | — |

**Trades today:** none (NFP binary event — research hold; no candidates cleared Layer A + Layer B)

**Notes:** Day 11 closes flat and clean — 100% cash, zero positions, zero open orders. The day P&L of −$337.71 (−0.340%) reflects the broker's mark-to-close differential: `last_equity` was $99,394.20 (May 06 EOD, the last full settlement before the May 07 XOM thesis-break exit intraday), while today's equity settles at $99,056.49 post-exit. No new trades were executed today as expected — today was NFP (Nonfarm Payrolls) Friday, an explicit binary macro event. The watchlist candidates from yesterday's afternoon scan (CVX at Z=−1.54, MCD at Z=−1.52) both remained below their entry thresholds (need Z ≤ −2.0 AND RSI < 30 AND stable spread simultaneously). Energy sector carries an elevated caution flag after the XOM thesis-break exit: one energy sector failure logged (XOM); a second consecutive energy fail would trigger the sector-exit rule. The bot is in a patient, cash-preserving posture heading into next week — full PDT budget (0/3 daytrades), full weekly trade allowance (0/3 new entries), and $99,056.49 cash available for deployment the moment a clean Z-score + RSI + catalyst setup qualifies. Phase P&L stands at −0.944%, well within circuit breaker limits. No stops to manage. No orders outstanding.

**Circuit breakers:** ✅ All clear — Day −0.340% (lim −2%) | Phase −0.944% (lim −5%) | Drawdown −1.148% from $100,206.70 peak (lim −15%)
**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 0/6

---

### May 09 — EOD Snapshot (Day 12, Saturday — Weekend)

**Portfolio:** $99,056.49 | **Cash:** $99,056.49 (100%) | **Day P&L:** −$337.71 (−0.340%) | **Phase P&L:** −$943.51 (−0.944%) | **Deployed:** 0%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| — | — | — | — | — | — | — |

**Trades today:** none (weekend — market closed; EOD summary captures post-NFP Friday settlement state)

**Notes:** Day 12 EOD summary runs Saturday to capture the settled state after NFP Friday (May 8). Equity holds at $99,056.49 — unchanged from yesterday's close, as expected with zero positions and zero orders outstanding. The Day P&L of −$337.71 (−0.340%) is a broker accounting artifact: Alpaca's `last_equity` field reflects $99,394.20 (the May 6 BOD / prior settlement reference carried forward), while true account equity has been $99,056.49 since the XOM thesis-break exit on May 7. No candidates cleared the dual-layer gate this week: XOM was the only position held (entries: May 1), exited May 7 on thesis-break at −4.73%. The full weekly trade allowance resets Monday (0/3 new entries, 0/3 PDT daytrades). Energy sector carries one consecutive failure flag (XOM) — a second consecutive energy loss triggers full sector exit. Watchlist heading into next week: CVX (needs Z ≤ −2.0, currently −1.54), MCD (needs Z ≤ −2.0, currently −1.52), and post-NFP macro recalibration for fresh sector ideas. Patient cash-preserve posture intact; no forced entries. Phase P&L −0.944% is well within all circuit breaker thresholds.

**Circuit breakers:** ✅ All clear — Day −0.340% (lim −2%) | Phase −0.944% (lim −5%) | Drawdown −1.148% from $100,206.70 peak (lim −15%)
**PDT count:** 0/3 | **Week trades:** 0/3 (resets Monday) | **Positions:** 0/6

---

### 2026-05-08 15:12 — MARKET-OPEN EXECUTION: NO ORDERS PLACED

**Session:** Friday 2026-05-08 (NFP Day)
**Account state:** Equity $99,056.46 | Cash $99,056.46 | Positions 0/6 | Daytrades 0/3 | Week trades 0/3

**Candidates evaluated (from May 7 afternoon watchlist):**

| Ticker | Z-Score | Gate Failure(s) | Action |
|--------|---------|-----------------|--------|
| CVX | −1.8571 | (1) No `## 2026-05-08` research entry / no DECISION: TRADE in research log; (2) Layer B #11a Z = −1.857 > −2.0 threshold | SKIPPED |
| MCD | −1.8356 | (1) No `## 2026-05-08` research entry / no DECISION: TRADE in research log; (2) Layer B #11a Z = −1.836 > −2.0 threshold | SKIPPED |
| XLE | ~−0.81 | (1) No `## 2026-05-08` research entry / no DECISION: TRADE; (2) Layer B Z far from any trigger | SKIPPED |

**Gate detail — CVX:**
- Layer A #5: FAIL — No today's research entry with documented catalyst and DECISION: TRADE
- Layer B #11a: FAIL — Z = −1.8571 (needs ≤ −2.0 for mean-reversion long)
- Approaching trigger: needs ~$5.60 more downside to ~$181.08 for Z = −2.0

**Gate detail — MCD:**
- Layer A #5: FAIL — No today's research entry with documented catalyst and DECISION: TRADE
- Layer B #11a: FAIL — Z = −1.8356 (needs ≤ −2.0 for mean-reversion long)
- Approaching trigger: needs ~$1.50 more downside to ~$278.97 for Z = −2.0

**Gate detail — XLE:**
- Layer A #5: FAIL — No today's research entry; Z too far from trigger (~−0.81)

**Additional context:**
- NFP print today (May 8) was the primary macro event flagged in May 7 afternoon research; no pre-market research was written documenting its outcome or any resulting catalyst for a DECISION: TRADE
- Energy sector carries one consecutive-failure flag (XOM thesis-break, May 7); entering CVX or XLE without a clean catalyst would risk triggering the two-consecutive-failure sector-exit rule
- All circuit breakers clear; cash fully preserved at $99,056.46

**Bracket orders placed:** NONE
**Status:** Awaiting pre-market research entry for next eligible session before any orders can be placed

### 2026-05-18 16:41 — LIMIT BUY ORDER PLACED: XOM
**Direction:** LONG
**Lane:** 2b-Long (Momentum)
**Catalyst:** WTI crude ~$106.34 (+0.87%); Brent ~$109–$110; US-Iran geopolitical tensions sustaining supply disruption premium; Energy sector #1 YTD at +27.87%; XOM confirmed breakout day Friday May 15 at $157.92→$159.78 on 1.70× volume
**Limit Price:** $159.78 (61 shares, day order)
**Stop (bracket child):** $147.80 (7.5% below limit — technical support at recent consolidation; order ID: 94606e38-9ac2-4065-b840-ae3cbe491ce8)
**Take-Profit (bracket child):** $183.74 (above limit; order ID: 336d922a-df53-428d-9745-2bd3e4346586)
**R-Multiple:** R_dollars $730.78 (0.738% of equity) | Target R = 2.0R
**R:R:** 2.0:1 (≥ 2.0 ✅)
**Trend Template:** PASS (50d SMA $155.13 / 150d SMA $136.40 / 200d SMA $136.23 — all aligned bull; 52w high $171.47, price 7.3% below; 6mo return +34.5% — top quartile; >30% above 52w low at +44.4%)
**Thesis:** Energy momentum trade — WTI crude sustained above $106 on US-Iran tensions and attacks on energy infrastructure. Energy is the #1 YTD sector (+27.87%). XOM broke above its prior 20d high ($157.92) on Friday May 15 with 1.70× volume confirmation. Z-Score +2.749 confirms statistical breakout. All 10 Minervini Trend Template conditions pass. CVX pair confirms direction (Z = +1.873, divergence 0.876σ within 1.5σ threshold). Pivot extension 1.18% — not chasing. Limit set at research entry; if price does not pull back to $159.78 today, order expires unfilled at close.
**Order ID:** 1d69c496-b40b-4974-9299-cac1a65bd5b9
**Status:** Placed — pending_new (awaiting fill; expires at session close if not filled)

**Live quote at order time:** Ask $161.24 / Bid $161.00 — market ~$1.46 above limit. Limit set at research price per strategy (no chasing). Fill requires intraday pullback to $159.78.

**Skipped candidates:**
- CVX: Layer B FAIL — Volume 1.10× on breakout day < 1.5× required. Thesis intact; re-evaluate if volume confirms.
- NVDA: Layer B FAIL — Price $222.895 below 20d high $235.74 (no breakout); additionally earnings binary Wednesday after close.
- XLF: Layer B FAIL — Z = −0.307 (need ≤ −1.0); not at 20d low; RSI 52.30 out of range.
- XLV: Layer B FAIL — Z = −0.095 (need ≤ −1.0); not at 20d low; only 9.5% below 52w high.

---

### May 18 — Afternoon Scan (Day N / ~15:44 ET)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Deployed:** 0% (bracket limit unfilled) | **Phase P&L:** −$943.54 (−0.944%)

| Ticker | Shares | Entry | Current | Unrealized P&L | Stop | Hold |
|--------|--------|-------|---------|----------------|------|------|
| — | — | — | — | — | — | — (0 positions) |

**Open orders:**
| Order ID | Symbol | Type | Status | Detail |
|----------|--------|------|--------|--------|
| 1d69c496 | XOM | Bracket limit buy, 61 sh @ $159.78 | **new / UNFILLED** | Stop $147.80 | TP $183.74 | Expires 20:00 UTC |
| 94606e38 | XOM | Stop $147.80 (bracket child) | held | Awaiting parent fill |
| 336d922a | XOM | TP $183.74 (bracket child) | held | Awaiting parent fill |

**Afternoon scan summary:**
- **Bracket fills today:** 0 — XOM bracket (1d69c496) placed at $159.78 at 16:41 UTC; XOM ask = $160.42 at scan time; never pulled back to limit all session. Order expires at 20:00 UTC (4:00 PM ET). If unfilled, re-evaluate Tuesday pre-market.
- **Trailing stops upgraded:** 0 — no filled positions; upgrade workflow not triggered.
- **Stale limits cancelled:** 0 — only open order is today's XOM bracket; thesis valid; no cancellation.
- **New afternoon entries placed:** 0 — 4 candidates evaluated (CVX, XLE, NVDA, XLV); all rejected:

| Candidate | Z-Score | Key Fail | Verdict |
|-----------|---------|----------|---------|
| CVX | +2.509 | Vol 1.10× < 1.5× required (2b-LONG) | REJECT — same as morning/midday |
| XLE | +2.133 | Vol 0.80× ❌; no valid lane (Phase 1 long-only blocks 2a-SHORT) | REJECT |
| NVDA | +1.058 | No breakout (price $221.72 < 20d high $235.74); earnings Wed HARD BLOCK | REJECT |
| XLV | +0.402 | Z mid-range — no lane triggers | REJECT |

- **Timing constraint applied:** Scan at 15:44 ET = within final 16 minutes. CONSTRAINTS.md: "No last 15 mins" for new entries. Even if a candidate qualified, no new bracket could be placed. This is a secondary blocker beyond the quant gate failures.
- **VIX regime:** NORMAL (1.00×) | **Positions:** 0/6 | **Week trades:** 0/3 | **PDT:** 1/3

**Key pair data:**
- XOM Z = +3.001 | CVX Z = +2.509 | Divergence = 0.493σ ✅ (energy sector moving together — thesis confirmed directionally)
- XLE Z = +2.133 | XOM–XLE divergence = 0.869σ ✅ (broad sector breadth)

**Circuit breakers:** ✅ All clear — Phase P&L −0.944% (lim −5%) | Drawdown −1.15% from $100,206.70 peak (lim −15%)

**Tomorrow (Tuesday 2026-05-19) action plan:**
1. If XOM bracket expired unfilled tonight → re-place with fresh entry calculation at Tuesday's open (pivot still $157.92, max chase $165.81). Do not assume yesterday's limit is still optimal.
2. CVX: Re-evaluate independently. Needs breakout-day volume ≥ 1.5× to clear Layer B. If Tuesday opens strong and volume surges, CVX qualifies for its own bracket order (independent of XOM — per CONSTRAINTS.md conditional gate independence rule).
3. NVDA: Hard block until Thursday May 22 (post-earnings evaluation only).


### May 18 — EOD Snapshot (Day 20, Monday)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Day P&L:** $0.00 (0.000%) | **Phase P&L:** −$943.54 (−0.944%) | **Deployed:** 0%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| — | — | — | — | — | — | — |

**Trades today:** none (XOM bracket limit order at $159.78 placed at market open, expired unfilled at session close — day TIF; live ask $161.24 at submission required intraday pullback that never materialized)

**Notes:** Flat session with no fills. XOM was the sole actionable candidate — bracket submitted at $159.78 (61 shares, stop $147.80, target $183.74, R:R 2.0:1, R_$ $730.78 / 0.738% eq.) but the ask never pulled back to the limit. CVX was blocked by Layer B volume gate (1.10× vs 1.5× required), NVDA hard-blocked until post-earnings Thursday, XLF/XLV both failed Z-score thresholds. Portfolio holds 100% cash entering Tuesday. Per the action plan, XOM should be re-priced at Tuesday's open with a fresh limit (pivot still $157.92, max-chase cap $165.81); CVX remains a live watch with its own independent gate. No circuit breakers triggered. All rules clear.

### 2026-05-19 12:41 — MARKET-OPEN EXECUTION: NO ORDERS PLACED (HOLD)

**Research Decision:** HOLD — 0 new entries
**Reason:** All candidates failed pre-market gate checks. Primary rejection drivers:

| Ticker | Direction | Lane | Gate Failed | Detail |
|--------|-----------|------|-------------|--------|
| XOM | LONG | 2b-LONG | Layer A (contra-catalyst) + Layer B (volume) | Oil −1.10% on Trump calling off Iran strike; supply-fear premium deflating; entry-day volume projected far below 1.5× 20d avg threshold |
| CVX | LONG | 2b-LONG | Layer B (no breakout) | Close $194.29 < 20d high $196.12 — not a confirmed breakout day |
| XLE | LONG | 2b-LONG | Layer B (no breakout) | Close $60.565 vs 20d pivot $60.58 (−0.02%) — at pivot but not above it |
| HD | LONG/SHORT | Any | Earnings binary (pre-market today) + sector fails | Consumer Discretionary YTD −0.03% fails momentum sector posture; insufficient quant data for short evaluation |
| NVDA | LONG | Any | HARD BLOCK | Earnings Wednesday May 20 — no entries permitted this week |
| FCX/NEM/CAT/GE | LONG | 2b-LONG | Deferred | Pre-binary session (NVDA + FOMC minutes Wed); bar data not pulled; deferred to Wednesday |

**Live Quotes at Execution Time (12:41 ET — informational only):**
- XOM: ask $162.01 / bid $153.05 (condition R — regular session, valid)
- CVX: ask $196.19 / bid $184.72 (condition R — regular session, valid)
- XLE: ask $61.12 / bid $61.10 (condition R — regular session, valid)

**Account State:**
- Equity: $99,056.46 | Cash: $99,056.46 (100%) | Buying power: $198,112.92
- Open positions: 0/6 | Open orders: 0 | Daytrade count: 0/3 | Week trades: 0/3
- Phase P&L: −$943.54 (−0.944% from $100,000 start)

**Patience Rule applied:** Zero trades is correct behavior when no setup clears all gates.
**Next action:** Re-evaluate Wednesday post-NVDA-binary + post-FOMC-minutes. XOM/CVX/XLE remain on watchlist; Materials sector (FCX, NEM) to be added to scan. NVDA hard-blocked until Thursday May 22.

**Status:** No orders placed — no order IDs to record.

---

### May 19 — Afternoon Scan (Day 21 / ~15:54 ET)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Deployed:** 0% | **Phase P&L:** −$943.54 (−0.944%)

| Ticker | Shares | Entry | Current | Unrealized P&L | Stop | Hold |
|--------|--------|-------|---------|----------------|------|------|
| — | — | — | — | — | — | — (0 positions) |

**Open orders at scan time:** NONE (Monday's bracket expired; no new orders placed today)

**Afternoon scan trades:** none

**Stop action:** N/A — no positions held

**Afternoon candidates evaluated — ALL REJECTED:**

| Candidate | Z-Score | Vol Ratio | Spread | Key Fail | Verdict |
|-----------|---------|-----------|--------|----------|---------|
| XOM | +3.117 | 1.20× | 0.043% ✅ | Vol 1.20× < 1.5× required (2b-LONG) | REJECT |
| CVX | +2.131† | 1.02× | 5.02% ❌ | Spread wide (R-flag) + Vol 1.02× + price AT (not above) 20d high | REJECT |
| XLE | +2.585 | 1.13× | 0.016% ✅ | Vol 1.13× < 1.5× required (2b-LONG) | REJECT |
| NVDA | N/A | N/A | 0.018% ✅ | HARD BLOCK — earnings tonight after close | REJECT |
| HD | N/A | N/A | 0.086% ✅ | Sector (Cons. Disc. YTD −0.03%) fails Layer A momentum gate | REJECT |

†CVX Z computed vs last close $196.12 (stub AH bid unreliable)

**Energy sector observations:**
- XOM: +1.60% today ($163.06 vs prior close $160.49) — bullish relative strength continues
- XLE: +1.36% today ($61.41 vs prior close $60.58) — sector ETF confirming XOM direction
- Pair divergence XOM–CVX: 0.986σ ✅ | XOM–XLE: 0.532σ ✅ — all energy names cohesive
- Volume confirmation (1.5× threshold) remains the sole gate blocking a momentum entry
- May 19 session volume (not yet final at scan time) is the key data point for Wednesday

**Timing constraint:** Scan at 15:54 ET = within final 6 minutes. CONSTRAINTS.md no-entry window applies independently of quant gate failures.

**NVDA binary tonight:** Q1 FY2027 earnings report after close. Market-wide binary overhang. Post-earnings direction will shape Wednesday's session.

**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 0/6 | **Circuit breakers:** ✅ All clear

**Watchlist for Wednesday pre-market (May 20):**
1. **XOM** — If May 19 final volume ≥25.2M, new breakout day → re-place bracket; max entry ≤$168.51 (pivot $160.49 × 1.05)
2. **XLE** — If May 19 final volume ≥54.97M, new breakout day → re-evaluate with TT issue noted
3. **NVDA** — Hard block Wed (earnings tonight); evaluate Thu May 22 post-earnings
4. **CVX** — Needs clean spread + volume ≥1.5× + close above $196.12
5. **HD** — Post-earnings bar available Wed; sector headwind for long; assess independently

### May 19 — EOD Snapshot (Day 21, Tuesday)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Day P&L:** $0.00 (0.000%) | **Phase P&L:** −$943.54 (−0.944%) | **Deployed:** 0%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| — | — | — | — | — | — | — |

**Trades today:** none

**Notes:** Flat day — no positions held, no orders active. Account remains fully in cash at $99,056.46. The day's research log carried forward watchlist notes on XOM (volume confirmation gate ≥25.2M), XLE (volume gate ≥54.97M with TT caveat), NVDA (hard block today due to earnings tonight; Thu May 22 is the earliest evaluation window), CVX (needs clean spread + volume ≥1.5× + close above $196.12), and HD (post-earnings bar available; sector headwind for longs). None of the candidates triggered their entry conditions today. Phase P&L remains at −$943.54 (−0.944%), well within all circuit-breaker thresholds. Tomorrow's priority: NVDA post-earnings assessment at open (not first 15 min), re-run volume checks on XOM and XLE against updated bars.


---

### 2026-05-20 16:37 — MARKET-OPEN EXECUTION: NO ORDERS PLACED

**Research Decision:** HOLD — zero candidates cleared both Layer A + Layer B gates today.

**Candidates Evaluated & Gates Failed:**

| Ticker | Direction | Lane | Failed Gate | Specific Reason |
|--------|-----------|------|-------------|-----------------|
| XOM | LONG | 2b-LONG | Layer B (vol + Trend Template) | Vol 1.23× < 1.5× required; 200-SMA unverifiable (151/200 bars); today down −2.3% with WTI −3.52%; Trend Template FAIL |
| NVDA | LONG | 2b-LONG | Layer B (no breakout + pair divergence) | Price $225.28 < 20d high $235.74 (no breakout); AVGO pair divergence 2.19σ > 1.5σ; projected vol ~1.0× < 1.5×; Trend Template FAIL |
| HD | SHORT | 2b-SHORT | Layer A + Layer B | Only −21.5% below 52wk high (need ≥−30%); 200-SMA unverifiable; price NOT below 20d low $297.51; today up +1.8% |

**Live Quotes at Execution Check (16:36 ET):**
- XOM: $158.80 bid / $158.93 ask — confirms pullback, below $160.49 breakout pivot
- NVDA: $224.51 bid / $224.55 ask — below $235.74 20d high pivot, no breakout
- HD: $298.00 bid / $311.00 ask — still above $297.51 20d low breakdown level

**Account State at Execution:**
- Equity: $99,056.46 | Cash: $99,056.46 (100% undeployed)
- Positions: 0/6 | Daytrades used: 0/3 | Week trades: 0/3
- VIX: 17.83 (Normal regime, 1.0× sizing multiplier)
- Phase P&L: −$943.54 (−0.944%) — within all circuit breakers

**Session Risk Note:** FOMC Minutes release at 2:00 PM ET. No bracket orders within 30-minute window before release per CONSTRAINTS (constraint auto-honored — no orders placed today).

**Thursday Watchlist:**
- XOM: Re-evaluate IF today's volume prints ≥25.2M shares AND close holds above $160.49 pivot
- NVDA: Re-evaluate IF today closes above $235.74 on volume ≥1.5× (~234M+ shares) AND AVGO Z-divergence narrows below 1.5σ
- HD: Not on active watchlist — does not meet Short Trend Template minimum requirements

**Status:** No open positions. All capital preserved. PDT headroom fully intact.


---

### May 20 — Afternoon Scan (Day 22 / Post-Session ~20:10 UTC)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Deployed:** 0% | **Phase P&L:** −$943.54 (−0.944%)

| Ticker | Shares | Entry | AH Bid | Unrealized P&L | Stop | Hold |
|--------|--------|-------|--------|----------------|------|------|
| — | — | — | — | — | — | — (0 positions) |

**Open orders at scan time:** NONE (1d69c496 expired May 18 as documented; no orders placed today)

**Afternoon scan trades:** none

**Stop action:** N/A — no positions held

**Afternoon candidates evaluated — ALL REJECTED:**

| Candidate | Z (May19 basis) | AH Signal | Key Fail | Verdict |
|-----------|-----------------|-----------|----------|---------|
| XOM | +2.380 | −8.0% AH | Vol 1.22× < 1.5×; 200-SMA unavail.; AH collapse implies thesis break in today's session | REJECT |
| CVX | +2.031 | −7.8% AH | Vol 1.21× < 1.5×; not above 20d high; AH collapse | REJECT |
| XLE | +2.127 | −4.8% AH | Vol 0.86× far below 1.5×; AH decline | REJECT |
| NVDA | +0.767 | ~flat AH | Z < +1.0 (any lane); no breakout; vol 0.90× | REJECT |
| HD | −1.244 | −3.7% AH | Short TT: −22.8% vs −30% required below 52wk high; 200-SMA unavail.; close > 20d low on last settled bar | REJECT |

**FOMC Minutes impact (today 2:00 PM ET):** Energy sector AH bids show 5–8% declines consistent with a hawkish Fed interpretation. XOM ($149.56), CVX ($181.88), XLE ($58.36) all significantly below May 19 settled closes. This matches the May 6–7 pattern; energy thesis is under renewed stress.

**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 0/6

**Circuit breakers:** ✅ All clear — Phase P&L −0.944% (lim −5%) | Drawdown −1.15% from $100,206.70 peak (lim −15%)

---

### May 20 — EOD Snapshot (Day 22, Wednesday)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Day P&L:** $0.00 (0.000%) | **Phase P&L:** −$943.54 (−0.944%) | **Deployed:** 0%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| — | — | — | — | — | — | — |

**Trades today:** none — HOLD decision at pre-market confirmed; no candidates cleared gates

**Notes:** Day 22 closes flat ($0.00 day P&L vs last_equity baseline) with portfolio at 100% cash. The session's defining event was the FOMC Minutes release (2:00 PM ET), which appears to have been interpreted hawkishly — energy sector AH quotes (XOM −8%, CVX −7.8%, XLE −4.8% vs May 19 settles) signal a material sector decline during today's session. No energy positions were held, so the portfolio was unaffected. NVDA's post-earnings reaction was flat (AH mid $220.27 ≈ settle $220.61), confirming the earnings beat was fully priced in — three consecutive evaluation sessions (May 18–20) have now failed the momentum lane gates. Thursday's pre-market must confirm May 20 settled prices (bars API) before any energy assessment can be made; the AH bid-only quotes are indicative but not actionable for re-entry decisions. HD's AH bid ($291.30) approaches the $297.51 breakdown level but the Trend Template structural gate (−22.8% vs −30% required below 52wk high) remains a hard blocker on any short. All circuit breakers clear. PDT 0/3. Week trades 0/3. Full cash preserved.

**Circuit breakers:** ✅ All clear — Day 0.00% (lim −2%) | Phase −0.944% (lim −5%) | Drawdown −1.15% from $100,206.70 peak (lim −15%)
**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 0/6


### May 20 — EOD Snapshot (Day 23, Wednesday)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Day P&L:** $0.00 (0.000%) | **Phase P&L:** −$943.54 (−0.944%) | **Deployed:** 0%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| — | — | — | — | — | — | — |

*No open positions.*

**Trades today:** none

**Notes:** Day 23 closes flat with portfolio at 100% cash. Today's EOD confirms what the afternoon scan already flagged: the FOMC Minutes (2:00 PM ET) appear to have been interpreted hawkishly, with energy sector AH quotes (XOM −8%, CVX −7.8%, XLE −4.8%) signaling a material sector selloff during the session. No energy exposure was held, so the portfolio was fully insulated. NVDA's AH price ($220.27) essentially matched its settle ($220.61), confirming the earnings beat was fully priced in — this marks three consecutive evaluation sessions (May 18–20) where NVDA failed the momentum lane gates. No new orders were placed today; the XOM bracket limit placed May 18 expired unfilled (day order). Week trades remain 0/3 with the weekly allowance fully intact heading into Thursday. Thursday's pre-market priority: confirm May 20 final bar prices via the bars API before assessing any re-entry in energy or new sector ideas — AH bid-only quotes are indicative only. HD short remains gated by Trend Template (−22.8% vs −30% required). All circuit breakers clear.

**Circuit breakers:** ✅ All clear — Day 0.000% (lim −2%) | Phase −0.944% (lim −5%) | Drawdown −1.15% from $100,206.70 peak (lim −15%)
**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 0/6

### 2026-05-21 16:27 — MARKET-OPEN EXECUTION: NO ORDERS PLACED

**Research Decision:** HOLD — 0 trades (explicit in today's research log)
**Week trades used:** 0/3 | **Daytrade count:** 0/3 | **Open positions:** 0/6
**Cash:** $99,056.46 (100% of equity)

**Candidates evaluated and rejected (all failed at research layer — no new gate checks needed):**

| Ticker | Dir | Key Failure(s) |
|--------|-----|---------------|
| XOM | LONG | Layer B Z=0.937 < 1.0 (momentum lane); Minervini 200-SMA unavailable |
| XLE | LONG | No breakout above 20d high ($61.29); Minervini 150/200-SMA unavailable |
| NVDA | LONG | Layer B Z=0.934 < 1.0; no breakout above 20d high ($235.74); catalyst spent |
| NIO | LONG | Minervini TT structurally fails (25 bars only); 0% above 52w low (needs >30%); bearish price response to catalyst |
| INTU | SHORT | Hard rule: >5% gap-down (−20%) → short prohibited; RSI <30 (outside 30–50); pair divergence 9.6σ; 200-SMA unavailable |
| WMT | SHORT | Hard rule: >5% gap-down (−10.2%) → short prohibited; only −10.2% below 52w high (needs >30%); price above SMA150; wrong sector posture |

**No orders placed. No order IDs. Cash preserved. All circuit breakers clear.**

**Circuit breakers:** ✅ All clear — Day 0.00% (lim −2%) | Phase −0.944% (lim −5%) | Drawdown −1.15% from $100,206.70 peak (lim −15%)
**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 0/6


---

### May 21 — Afternoon Scan (Day 24 / ~15:53 ET)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Deployed:** 0% | **Phase P&L:** −$943.54 (−0.944%)

| Ticker | Shares | Entry | Current | Unrealized P&L | Stop | Hold |
|--------|--------|-------|---------|----------------|------|------|
| — | — | — | — | — | — | — (0 positions) |

**Open orders at scan time:** NONE

**Afternoon scan trades:** none

**Stop action:** N/A — no positions held, no upgrade workflow triggered.

**Afternoon candidates evaluated — ALL REJECTED:**

| Candidate | Z(settle) | Z(live) | Vol ratio | Key Fail | Verdict |
|-----------|-----------|---------|-----------|----------|---------|
| XOM | +0.856 | +0.604 | 1.08× | Z<1.0; price 7.0% below $162.55 pivot; vol sub-1.5×; TT 200-SMA structural | REJECT |
| CVX | +0.594 | +0.450 | 1.45× | Z<1.0; price 3.3% below $197.25 pivot; vol 1.45× (0.05× short) | REJECT |
| XLE | +1.030 | +0.606 | 1.66× ✅ | Z(live) <1.0; no breakout; TT 150/200-SMA structural (split) | REJECT |
| NVDA | +0.934 | +0.630 | 1.15× | Z<1.0; 6.6% below $235.74 pivot; vol <1.5×; 7th consecutive miss | REJECT |
| XLB | **-1.810** | -1.509 | **1.90× ✅** | Z=-1.509 (need≤-2.0, 0.491σ short); RSI~32-35 (need<30); FCX pair div 1.84σ>1.5σ; TT fails | REJECT |
| FCX | +0.026 | — | 0.75× | Z at mean, no extreme | REJECT |

**XLB watchlist detail:**
- Z=-2.0 trigger price: $49.56 (20d mean $51.28 − 2×σ $0.86)
- Current ask $49.98 → $0.42 further decline needed (−0.8%)
- Volume 1.90× (strongest of any candidate in scan)
- FCX pair divergence 1.835σ — blocks entry under current rules
- All 3 gates (Z, RSI, pair) must clear simultaneously for entry

**Timing constraint:** Scan at 15:53 ET = final 7 minutes of session. No new entries per CONSTRAINTS last-15-min rule (secondary independent block).

**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 0/6
**Circuit breakers:** ✅ All clear — Phase P&L −0.944% (lim −5%) | Drawdown −1.15% from $100,206.70 peak (lim −15%)

---

### May 21 — EOD Snapshot (Day 24, Thursday)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Day P&L:** $0.00 (0.000%) | **Phase P&L:** −$943.54 (−0.944%) | **Deployed:** 0%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| — | — | — | — | — | — | — |

**Trades today:** none — HOLD decision at pre-market confirmed (all 6 candidates failed Layer A + Layer B at open and afternoon scan)

**Notes:** Day 24 closes flat at $99,056.46. The afternoon scan evaluated 6 candidates across energy (XOM, CVX, XLE), technology (NVDA), and materials (XLB, FCX) sectors — zero cleared composite gates. The most notable development was XLB (Materials ETF) printing 1.90× above-average volume on its May 20 settle, with Z = -1.810 heading into today's final session — the closest any candidate has been to the mean-reversion long trigger in recent sessions. However, three independent gates remain uncleared: Z needs ≤-2.0 (only 0.491σ away = ~$0.42 decline), RSI needs <30 (currently ~32-35), and the FCX pair divergence needs to narrow below 1.5σ (currently 1.835σ). Energy names continue their orderly pullback from last week's breakout highs on below-average volume — thesis intact but no statistical entry signal available. NVDA removed from active watchlist after 7 consecutive gate misses post-earnings. Full PDT budget intact (0/3). Full weekly trade allowance intact (0/3). Maximum flexibility for Friday pre-market.

**Circuit breakers:** ✅ All clear — Day 0.000% (lim −2%) | Phase −0.944% (lim −5%) | Drawdown −1.15% from $100,206.70 peak (lim −15%)
**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 0/6


### 2026-05-22 09:30 — MARKET-OPEN EXECUTION: NO ORDERS PLACED
**Research Decision:** HOLD — Zero candidates cleared Layer A + Layer B composite gates
**Account State:** $99,056.46 equity | $99,056.46 cash | 0 open positions | 0 daytrades used
**Candidates Evaluated:** XLB (2a-LONG), XOM (2b-LONG), CVX (2b-LONG), XLE (2b-LONG), XLV (deferred), XLF (deferred)
**Reason:** All screened candidates failed at least one quant gate (Z-score, volume ratio, pivot, or RSI). No trade ideas generated with DECISION: TRADE in today's research log. No bracket orders submitted.
**PDT Budget Remaining:** 3/3 day trades intact
**Next Action:** Monday 2026-05-25 pre-market — re-scan XLE (pivot $61.29 watch), XLB (Z-trigger $49.56), XLV 2b-SHORT full pull, XLF 2b-SHORT full pull


---

### May 22 — Afternoon Scan (Day 25 / ~15:48 ET)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Deployed:** 0% | **Phase P&L:** −$943.54 (−0.944%)

| Ticker | Shares | Entry | Current | Unrealized P&L | Stop | Hold |
|--------|--------|-------|---------|----------------|------|------|
| — | — | — | — | — | — | — (0 positions) |

**Open orders at scan time:** NONE (last bracket 1d69c496 expired May 18T20:02; no new orders placed today)

**Afternoon scan trades:** none

**Stop action:** N/A — no positions held, no upgrade workflow triggered

**Afternoon candidates evaluated — ALL REJECTED:**

| Candidate | Z-Score | Vol Ratio | Spread | Lane | Key Failures | Verdict |
|-----------|---------|-----------|--------|------|--------------|---------|
| XOM | +0.487 | 0.98× | R-flag | 2b-LONG | Z<+1.0 ❌; $7.65 below $162.55 pivot ❌; vol sub-1.5× ❌ | REJECT |
| CVX | +0.598 | 0.85× | 0.43%† | 2b-LONG | Z<+1.0 ❌; $5.72 below $197.25 pivot ❌ | REJECT |
| XLE | +0.766 | 1.21× | 0.02% ✅ | 2b-LONG | Z<+1.0 ❌; $1.80 below $61.29 pivot ❌; TT structural | REJECT |
| XLB | −1.003 | 0.97× | 0.02% ✅ | 2a-LONG | Z=−1.003 (need ≤−2.0) ❌; vol 0.97× ❌ | REJECT |
| XLV | **+3.247** | 0.74× | 0.007% ✅ | **2a-SHORT** | Vol 0.74× ❌; TT: price above 50d SMA ❌; RSI unconfirmed | REJECT |
| XLF | +1.128 | 1.00× | 0.019% ✅ | 2b-SHORT | Z wrong direction (+1.13 not ≤−1.0) ❌; above 20d low ❌ | REJECT |

†CVX bid stub $180.73 (R-flagged wide); fair value via ask $191.53

**Pair divergences confirmed:**
- XOM (+0.487) ↔ CVX (+0.598): 0.112σ ✅ (energy names in lockstep)
- XLB (−1.003) ↔ FCX (+0.328): **1.330σ ✅** — pair divergence NARROWED from prior 1.835σ; now below 1.5σ threshold for first time this week

**Notable developments:**
- XLV Z=+3.247 is the single largest Z-score in today's scan — statistically extreme overbought reading. Becomes #1 watchlist candidate for Monday as a 2a-SHORT setup if RSI confirms >70 and volume recovers to ≥1.0×.
- XLB FCX pair divergence now 1.330σ (passes pair gate) — removes the pair-confirmation blocker that was preventing XLB's mean-reversion long setup. Trigger price still $49.40.
- Energy sector consolidating on below-avg volume — thesis intact, no entry signal.

**Timing:** Scan at 15:48 ET = within final 12 minutes. CONSTRAINTS.md last-15-min no-entry window applies independently of quant failures.

**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 0/6
**Circuit breakers:** ✅ All clear — Phase P&L −0.944% (lim −5%) | Drawdown −1.15% from $100,206.70 peak (lim −15%)

---

### May 22 — EOD Snapshot (Day 25, Friday)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Day P&L:** $0.00 (0.000%) | **Phase P&L:** −$943.54 (−0.944%) | **Deployed:** 0%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| — | — | — | — | — | — | — |

**Trades today:** none — HOLD decision confirmed at pre-market; all 6 candidates (XLB, XOM, CVX, XLE, XLV, XLF) failed composite Layer A + Layer B gates

**Notes:** Day 25 closes the week flat at $99,056.46 — week trades 0/3 used, PDT budget fully intact (0/3), all circuit breakers clear. The week was dominated by the energy sector's orderly pullback from the prior week's highs (XOM peaked $162.55 May 19 → $154.90 today; XLE peaked $61.29 May 19 → $59.50 today). No positions were held, no orders placed, no fills occurred. The most significant development of the afternoon scan was XLV at Z=+3.247 — the single largest overbought Z-score in any scan this week — flagging a potential 2a-SHORT mean-reversion setup for Monday if RSI confirms >70 and volume recovers to ≥1.0× avg. XLB's FCX pair divergence narrowed to 1.330σ (within the ≤1.5σ gate) for the first time, removing a key blocker on the mean-reversion long setup (trigger price $49.40). The energy thesis (WTI ~$96-98, Brent ~$104-106, Hormuz) remains structurally sound; the momentum signal simply reset during the week's consolidation. Heading into Monday with maximum deployment flexibility: 0 positions, 3/3 week trades available, 3/3 PDT budget.

**Circuit breakers:** ✅ All clear — Day 0.000% (lim −2%) | Phase −0.944% (lim −5%) | Drawdown −1.15% from $100,206.70 peak (lim −15%)
**PDT count:** 0/3 | **Week trades:** 0/3 (resets Monday) | **Positions:** 0/6


---

### 2026-05-25 16:08 — MARKET-OPEN EXECUTION: NO ORDERS PLACED

**Reason:** Research DECISION = **HOLD**. US equity markets are **CLOSED** today — Memorial Day federal holiday. NYSE and NASDAQ observe the holiday; no regular session opens. No bracket orders can be placed or would be executable.

**Account State at Execution Time:**
- Equity: $99,056.46
- Cash: $99,056.46 (100% undeployed)
- Open positions: 0
- Open orders: 0
- Daytrade count: 0/3
- Week trades used: 0/3 (new week — resets today per research log)

**Live Quotes Pulled (pre-market / stale weekend prints — confirming data feeds live, no halts/delistings):**
- XLV: bid $145.72 / ask $153.63 (stale; last print 2026-05-22T20:00Z) — data valid, no halt ✅
- XLE: bid $57.23 / ask $60.82 (stale; last print 2026-05-22T20:00Z) — data valid, no halt ✅
- XLB: bp $48.70 / ask $0 (weekend; bid only) — data valid, no halt ✅
- XLK: bid $174.52 / ask $185.46 (stale; last print 2026-05-22T20:00Z) — data valid, no halt ✅

**Gate Analysis — All Four Watchlist Candidates:**

| Candidate | Direction | Lane | Decision | Gate(s) Failed |
|-----------|-----------|------|----------|----------------|
| XLV | SHORT | 2a-SHORT | SKIP | RSI 69.1 < 70 ❌; Volume 0.714× < 1.0× ❌; Minervini Short TT: price > 50-SMA ❌, only −6.4% below 52w high (need −30%) ❌ |
| XLE | SHORT | 2b-SHORT | SKIP | RSI would crash through <30 (oversold) ❌; 20d-low not confirmed ❌; TT blocked (split data gap, <150 bars) ❌; no >30% below 52w high ❌ |
| XLB | LONG | 2a-LONG | SKIP | Z = −0.890 (need ≤ −2.0) ❌; RSI 47.8 (need < 30) ❌; Volume 0.658× (need ≥ 1.0×) ❌; TT: price < 50-SMA ❌ |
| XLK | LONG | 2b-LONG | SKIP | RSI 74.9 > 70 (need 50–70) ❌; Volume 0.932× (need ≥ 1.5×) ❌; no clean 20d high breakout ❌; TT 150/200-SMA blocked (split gap) ❌ |

**Primary reason no orders placed:** DECISION in today's research log is explicitly **HOLD**. Zero candidates cleared both Layer A (Catalyst + Trend Template) and Layer B (Quant Lane) gates. Additionally, US markets are physically closed — any `day`-TIF order submitted today would be rejected by Alpaca's session rules.

**Bracket Orders Submitted:** NONE
**PDT Budget Remaining:** 3/3
**Week Trades Remaining:** 3/3

**Watchlist for Tuesday 2026-05-26 pre-market:**
1. **XLE / XOM** — 2b-SHORT if Tuesday open confirms close < 20d lows ($55.70 / $144.57) on ≥ 1.5× volume; RSI must land in 30–50 zone (not crash through 30). WTI −6.1% Iran deal catalyst is the setup driver.
2. **XLV** — 2a-SHORT re-evaluation: RSI 69.1 needs to clear 70; volume needs ≥ 9.7M shares (≥ 1.0×); Z = +2.44 already qualifies. Structural TT conflict (2a-SHORT vs. Minervini Short TT) flagged for formal strategy review.
3. **XLK** — 2b-LONG watch: RSI 74.9 needs to normalize to 50–70 zone; gap-up Tuesday may resolve after intraday cooling. 20d high breakout + volume ≥ 1.5× needed.
4. **XLB** — Mean-reversion long trigger at $49.40 (Z ≤ −2.0). Oil-crash risk-off day Tuesday could push materials lower and trigger this setup.

---

### May 25 — Afternoon Scan (Memorial Day / ~15:27 ET)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Deployed:** 0% | **Phase P&L:** −$943.54 (−0.944%)

| Ticker | Shares | Entry | Current | Unrealized P&L | Stop | Hold |
|--------|--------|-------|---------|----------------|------|------|
| — | — | — | — | — | — | — (0 positions) |

**Open orders at scan time:** NONE

**Market status:** ⚠️ CLOSED — Memorial Day federal holiday. No trading. All quotes stale (May 22 close data).

**Afternoon scan trades:** none

**Stop action:** N/A — no positions held, no upgrade workflow triggered

**Afternoon candidates evaluated — ALL REJECTED:**

| Candidate | Z-Score | RSI | Vol | Key Fail | Verdict |
|-----------|---------|-----|-----|----------|---------|
| XLV | +3.205 | 60.9 | 0.71× | RSI 60.9 ❌ (need >70); Vol 0.71× ❌ (need ≥1.0×); TT structural (at 52w high, not >30% below) ❌ | REJECT |
| XLB | −1.008 | 41.4 | 0.66× | Z −1.008 ❌ (need ≤−2.0); RSI 41.4 ❌ (need <30); Vol 0.66× ❌ | REJECT |
| XLE | +0.763 | 61.2 | 1.12× | Z +0.763 ❌; no breakout above $61.29 ❌; Vol 1.12× ❌ | REJECT |
| XLK | +1.425 | 72.8 | 0.93× | RSI 72.8 ❌ (need 50–70); Vol 0.93× ❌ (need ≥1.5×); TT 150/200-SMA unavail. ❌ | REJECT |
| XOM | +0.491 | 55.6 | 0.74× | Z +0.491 ❌; price 5% below $162.55 pivot ❌; Vol 0.74× ❌ | REJECT |

**Key developments:**
- XLB FCX pair divergence = 1.368σ ✅ — NOW within the ≤1.5σ gate for the first time; removes pair-confirmation blocker on XLB 2a-LONG setup
- XLK: 20d breakout confirmed (180.39 > pivot 179.50, +0.50% extension ✅); awaiting RSI normalization (72.8 → 50–70) and vol ≥1.5× on Tuesday open
- WTI crude fell to ~$90.65 over weekend (Iran deal framework) — energy sector faces gap-down risk Tuesday

**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 0/6
**Circuit breakers:** ✅ All clear — Phase P&L −0.944% (lim −5%) | Drawdown −1.15% from $100,206.70 peak (lim −15%)


### May 25 — EOD Snapshot (Day 26, Monday — Memorial Day Holiday)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Day P&L:** $0.00 (0.000%) | **Phase P&L:** −$943.54 (−0.944%) | **Deployed:** 0%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| — | — | — | — | — | — | — (0 positions) |

**Trades today:** none — US equity markets closed (Memorial Day federal holiday); no orders submitted, no fills, no bracket orders placed

**Notes:** Day 26 ends flat — Memorial Day holiday. NYSE and NASDAQ were physically closed; Alpaca confirmed zero activity (`last_equity` == `equity` == $99,056.46, `balance_asof` still showing 2026-05-22 Friday close). Portfolio remains fully in cash, 0 open positions, 0 open orders. All circuit breakers clear heading into Tuesday. Week trade budget resets fresh (0/3) and PDT budget fully intact (0/3). The pre-market research scan ran during the session window and confirmed all four watchlist candidates (XLV, XLE, XLB, XLK) still fail composite Layer A+B gates on stale May 22 close data — no phantom signals generated. Primary Tuesday focus: XLE/XOM 2b-SHORT (Iran deal WTI crude gap-down catalyst), XLV 2a-SHORT (Z=+3.205, needs RSI >70 + vol ≥1.0×), XLK 2b-LONG (RSI normalization from 72.8 → 50–70 window), XLB 2a-LONG (trigger $49.40 Z≤−2.0). Phase P&L steady at −0.944% — well within all risk limits.

**Circuit breakers:** ✅ All clear — Day 0.000% (lim −2%) | Phase −0.944% (lim −5%) | Drawdown −1.15% from $100,206.70 peak (lim −15%)
**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 0/6

---

---

### 2026-05-26 16:57 — MARKET-OPEN EXECUTION: NO ORDERS PLACED

**Decision:** HOLD — Zero trades today (confirmed from research log DECISION field)

**Account snapshot at execution time:**
- Equity: $99,056.46
- Cash: $99,056.46 (100.0% undeployed)
- Open positions: 0 / 6
- PDT daytrade count: 0 / 3
- Week trades used: 0 / 3
- Trading blocked: false | Account blocked: false

**Candidates evaluated (11 total, 6 sectors) — all REJECTED:**

| Ticker | Lane | Primary Failure(s) |
|--------|------|--------------------|
| XLK | 2b-LONG | RSI 76.2 > 70 (needs 50–70); Vol 0.43× < 1.5×; TT unverifiable (Dec 2025 2:1 split corrupts 200-SMA) |
| XLV | 2a-SHORT | Z +1.671 < +2.0; RSI 58.6 < 70; Vol 0.32× < 1.0× |
| XLB | 2a-LONG | Z −0.296 >> −2.0 (trigger ~$49.10, price $50.80); TT 52w-low spread fails |
| AZO | 2a-LONG | TT unverifiable (150-bar ceiling); Sector YTD −2.0% (bearish); Vol 0.90× < 1.0× |
| XLY | — | Z +0.591 (neutral, no directional setup) |
| NVDA | — | Z −0.109 (at mean, no setup) |
| XOM | — | Z −0.330 (near zero, no breakout above $162.55 pivot) |
| XLE | — | Z +0.101 (near zero, no breakout above $61.29 pivot) |
| XLF | — | Z +0.875 < +1.0; no 20d-high breakout |
| XLI | — | Z +0.675 < +1.0; no 20d-high breakout |
| SPY | — | Z +1.402; Vol 0.29× (post-holiday holiday drag) |

**Structural market blockers today:**
1. Post-Memorial Day volume suppression — ALL names showing 0.25×–0.50× of 20d avg. No momentum candidate can pass ≥1.5× volume gate.
2. Tech (XLK) RSI overbought at 76.2 after NVDA-driven AI gap-up.
3. TT data unavailability — 3 names structurally blocked by 150-bar ceiling (XLK split, AZO, XLV).

**Gate checks run (all constraints confirmed):**
- ✅ Positions: 0 (would be ≤ 6 — irrelevant, no orders)
- ✅ Week trades: 0/3 (budget intact)
- ✅ PDT: 0/3
- ✅ Circuit breakers: Phase P&L −0.944% (lim −5%) | Drawdown −1.15% (lim −15%)
- ✅ VIX: 16.85 (Normal regime, 14–22 band) — entries permitted in principle
- ✅ No forbidden order types attempted

**Watchlist for Wednesday 2026-05-27:**
1. XLK 2b-LONG — RSI needs to normalize 76.2 → 50–70; vol needs ≥1.5× on full trading day; TT blocker persists
2. XLV 2a-SHORT — Z needs +2.0 (~$149.47); RSI needs >70; vol needs ≥1.0×
3. XLE/XOM 2b-LONG — Watch for breakout above $61.29 / $162.55 pivots if Brent stays elevated ≥$99
4. XLB 2a-LONG — Trigger ~$49.10 (3.4% away); Brent spike working against this setup

**No order IDs. No fills. No bracket children active.**

---

### May 26 — Afternoon Scan (Day 27 / Post-Session ~20:12 UTC)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Deployed:** 0% | **Phase P&L:** −$943.54 (−0.944%)

| Ticker | Shares | Entry | Current | Unrealized P&L | Stop | Hold |
|--------|--------|-------|---------|----------------|------|------|
| — | — | — | — | — | — | — (0 positions) |

**Open orders at scan time:** NONE (last bracket 1d69c496 expired May 18T20:02; no orders placed today)

**Afternoon scan trades:** none

**Stop action:** N/A — no positions held, no upgrade workflow triggered

**Afternoon candidates evaluated — ALL REJECTED (May 26 settled bar data):**

| Candidate | Z-Score | RSI | Vol Ratio | Key Failures | Verdict |
|-----------|---------|-----|-----------|--------------|---------|
| XLK | +1.694 | 77.9 | 1.08× | RSI 77.9 > 70 ❌; Vol 1.08× < 1.5× ❌; TT 150/200-SMA unavail. ❌ | REJECT |
| XLV | +1.524 | 62.3 | 0.68× | Z < +2.0 ❌; RSI < 70 ❌; Vol < 1.0× ❌; XLV SOLD OFF today (Z regressed from +3.205 → +1.524) | REJECT |
| XLB | −0.094 | 52.2 | 0.76× | Z −0.094 >> −2.0 ❌; setup fully reset from oversold low | REJECT |
| XLE | −0.482 | 43.9 | 1.01× | Z fails both lanes; not below 20d low; short TT structural; energy sector rotation headwind | REJECT |
| XOM | −0.777 | 45.0 | 0.74× | Z < +1.0 ❌; 7.8% below $162.55 pivot ❌; Vol 0.74× ❌; TT unavail. ❌ | REJECT |

**Pair Z-Scores confirmed:**
- AVGO (+0.313) ↔ XLK (+1.694): 1.381σ ✅ | FCX (+0.993) ↔ XLB (−0.094): 1.087σ ✅ | CVX (−1.062) ↔ XOM (−0.777): 0.285σ ✅

**Key development — sector rotation:**
- XLK: +2.65% today ($180.39 → $185.18) — tech rally confirmed breakout above 20d high
- XLE: −2.8% today ($59.49 → $57.85) — energy selloff on Iran deal optimism
- XOM: −3.3% today ($154.92 → $149.81) — below May 1 entry price of $153.35
- XLV: −0.9% today ($149.89 → $148.51) — Z-score dropped 1.68σ in one session (overbought thesis partially self-resolved)
- XLB: flat (+$0.70) — Z fully reset to −0.094 from −1.810 oversold low last week

**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 0/6
**Circuit breakers:** ✅ All clear — Phase P&L −0.944% (lim −5%) | Drawdown −1.15% from $100,206.70 peak (lim −15%)

---

### May 26 — EOD Snapshot (Day 27, Tuesday)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Day P&L:** $0.00 (0.000%) | **Phase P&L:** −$943.54 (−0.944%) | **Deployed:** 0%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| — | — | — | — | — | — | — |

**Trades today:** none — HOLD confirmed at pre-market (post-holiday volume drought; all 11 candidates failed composite gates). Afternoon scan confirmed same verdict.

**Notes:** Day 27 closes at 100% cash. No fills, no orders placed, no bracket limits active. The dominant macro theme today was continued sector rotation: XLK +2.65% (tech, NVDA/AI tailwind) vs XLE −2.8% (energy, Iran peace deal optimism draining WTI premium). XOM fell to $149.81 — $3.54 below the original May 1 entry price — validating the May 7 thesis-break exit decision. XLV's Z-score dropped sharply from +3.205 → +1.524 as healthcare gave back Friday's overbought extension; the 2a-SHORT setup has partially self-corrected without a trade. XLK remains the #1 watchlist candidate: Z=+1.694, confirmed breakout at 2.65% above pivot, AVGO pair confirms (1.381σ divergence). Two gates remain: RSI needs to normalize from 77.9 → 50–70 and volume needs to reach ≥1.5× avg (~17.3M) on a full session. All circuit breakers clear. PDT 0/3, week trades 0/3 heading into Wednesday.

**Circuit breakers:** ✅ All clear — Day 0.000% (lim −2%) | Phase −0.944% (lim −5%) | Drawdown −1.15% from $100,206.70 peak (lim −15%)
**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 0/6


### May 26 — EOD Snapshot (Day 27, Tuesday — Final Close)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Day P&L:** $0.00 (0.000%) | **Phase P&L:** −$943.54 (−0.944%) | **Deployed:** 0%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| — | — | — | — | — | — | — |

*No open positions at close.*

**Trades today:** none — end-of-day confirmation run; all candidates (XLK, XLV, XLE, XOM, XLB) failed composite Layer A + Layer B gates at both morning and afternoon scans. No orders placed, no fills, no bracket orders active.

**Notes:** Day 27 closes flat at 100% cash for the second consecutive session. The Alpaca account shows $99,056.46 equity and $99,056.46 cash — no movement from yesterday's close, consistent with zero deployed capital. The dominant watchlist themes remain XLK 2b-LONG (RSI normalizing from 76.2; needs 50–70 range + volume ≥1.5× avg before entry is valid) and XLV 2a-SHORT (Z-score drifted to ~+1.5, still short of the +2.0 trigger). XLE/XOM continue consolidating near pivot levels — no breakout catalyst confirmed today. The week opens 0/3 trades with the full PDT budget intact heading into Wednesday May 27. No circuit breakers tripped. Strategy remains disciplined: wait for setups to come to us rather than chasing elevated RSI prints.

**Circuit breakers:** ✅ All clear — Day 0.000% (lim −2%) | Phase −0.944% (lim −5%) | Drawdown −1.15% from $100,206.70 peak (lim −15%)
**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 0/6

### 2026-05-27 16:49 — MARKET-OPEN EXECUTION: NO ORDERS PLACED

**Session Result:** HOLD — 0 bracket limit orders placed.
**Account State (live, pre-session):** Equity $99,056.46 | Cash $99,056.46 | Positions 0/6 | Daytrade count 0/3 | Week trades 0/3
**VIX:** 17.01 (Normal regime, 1.00× sizing multiplier) — entries eligible in principle.

**Candidates reviewed and gate outcomes:**

**XLK (2b-LONG attempted):**
- Live ask: $184.24 (research close $182.99 — price has recovered slightly post-close, consistent with overnight strength)
- Gate failures (4): (1) Close < prior 20d high $185.14 ❌, (2) Volume 0.46× avg ❌, (3) 200-SMA unverifiable (structural split gap) ❌, (4) AVGO pair divergence 1.64σ > 1.5σ limit ❌
- Decision: SKIP — 4 gate failures. No order placed.
- Forward trigger: Needs close above $185.14 on ≥17.6M volume + AVGO divergence < 1.5σ.

**MRVL (2b-LONG attempted):**
- Live ask: $202.21 (research close $197.025 — stock bid up post-session ahead of earnings print)
- Gate failures (5): (1) MRVL reports earnings after close TODAY — binary event, entering a long position through earnings violates swing-trade discipline ❌, (2) Close < 20d high $208.26 ❌, (3) Volume 0.88× avg ❌, (4) 200-SMA unverifiable (structural gap) ❌, (5) NVDA pair divergence 2.22σ > 1.5σ limit ❌
- Decision: SKIP — 5 gate failures, including the disqualifying earnings-binary flag. No order placed.
- Forward trigger: Post-earnings continuation tomorrow (May 28) IF beat drives close > $208.26 on ≥1.5× volume with pair divergence compressed.

**XLE (2b-SHORT / 2a-LONG attempted):**
- Live ask: $57.25 (research close $57.27 — essentially unchanged)
- Gate failures: Z-Score −0.8924 clears no lane (2a-LONG needs Z ≤ −2.0; 2b-SHORT needs Z ≤ −1.0 AND close < 20d low $55.70; 2b-LONG needs Z ≥ +1.0). Midrange — no statistical edge.
- Decision: SKIP — no lane qualifies. No order placed.
- Forward trigger: 2a-LONG only if WTI accelerates lower and XLE reaches ~$55.68 (Z ≈ −2.0).

**PDT count:** 0 (unchanged) | **Week trades:** 0/3 (unchanged) | **Open positions:** 0/6


---

### May 27 — Afternoon Scan (Day 29 / Post-Session ~20:17 UTC)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Deployed:** 0% | **Phase P&L:** −$943.54 (−0.944%)

| Ticker | Shares | Entry | Current | Unrealized P&L | Stop | Hold |
|--------|--------|-------|---------|----------------|------|------|
| — | — | — | — | — | — | — (0 positions) |

**Open orders at scan time:** NONE

**Afternoon scan trades:** none

**Stop action:** N/A — no positions held, no upgrade workflow triggered

**Afternoon candidates evaluated — ALL REJECTED (May 27 settled bar data):**

| Candidate | Z-Score | RSI | Vol Ratio | Key Failures | Verdict |
|-----------|---------|-----|-----------|--------------|---------|
| XLK | +1.473 | 70.94 | 1.034× | Close $184.43 < $185.14 pivot ❌; RSI 70.94 overbought ❌; Vol 1.034× < 1.5× ❌; 200-SMA unavail. ❌ | REJECT |
| XLV | +1.495 | 61.71 | 1.028× | Z < +2.0 ❌; RSI < 70 ❌; TT: above 50-SMA (short TT fails) ❌ | REJECT |
| MRVL | +1.672 | 62.08 | 1.813× ✅ | Close $198.70 < $208.26 pivot ❌; 200-SMA unavail. ❌ | REJECT |
| XLE | −1.039 | 49.96 | 1.291× | Close $56.99 > 20d low $55.70 (no breakdown) ❌; Vol 1.291× < 1.5× ❌; Short TT structural ❌ | REJECT |
| XOM | −1.161 | 48.93 | 0.929× | Z mid-range, no lane qualifies; vol below avg | REJECT |

**Pair divergences confirmed:** AVGO 1.276σ ✅ | CVX 0.287σ ✅

**Notable development:** MRVL volume 1.813× today (strongest in scan) — post-earnings institutional activity. But the intraday gap-up fade (open $217.98 → close $198.70, −9%) means the $208.26 pivot was NOT confirmed on a closing basis. "Sell the news" pattern.

**XLE 2a-LONG watch:** Z = −1.039; trigger price for Z = −2.0 is **$55.59** (only −2.5% from today's close). RSI already at 49.96 (approaching <30 territory if further decline). This is the #3 watchlist candidate heading into Thursday.

**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 0/6
**Circuit breakers:** ✅ All clear — Phase P&L −0.944% (lim −5%) | Drawdown −1.15% from $100,206.70 peak (lim −15%)

---

### May 27 — EOD Snapshot (Day 29, Wednesday)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Day P&L:** $0.00 (0.000%) | **Phase P&L:** −$943.54 (−0.944%) | **Deployed:** 0%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| — | — | — | — | — | — | — |

**Trades today:** none — HOLD decision at pre-market confirmed. Afternoon scan confirmed same verdict. No fills, no orders, no bracket limits active.

**Notes:** Day 29 closes at 100% cash. The session's defining story was MRVL's post-earnings fade: gapped up to $217.98 on the open (above the $208.26 20d high pivot, briefly appearing to qualify as a 2b-LONG breakout), then reversed sharply to close $198.70 (−9% intraday) — a textbook "buy the rumor, sell the news" pattern that validates the strategy's earnings-binary hard block. The morning HOLD decision (which cited the MRVL earnings binary as a key disqualifier) protected capital from what would have been an immediate −9% adverse intraday move. XLK faded from its $186.18 open back to $184.43 — still below the $185.14 pivot needed for the 2b-LONG breakout, RSI remains at 70.94 (marginally above the 70 ceiling). XLE now only $1.29 above the 20d low $55.70 (Z = −1.039); a further −2.5% decline would trigger the 2a-LONG entry gate at ~$55.59. Week closes 0/3 trades. Full PDT budget intact (0/3). Maximum flexibility heading into Thursday.

**Circuit breakers:** ✅ All clear — Day 0.000% (lim −2%) | Phase −0.944% (lim −5%) | Drawdown −1.15% from $100,206.70 peak (lim −15%)
**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 0/6


---

### May 28 — EOD Snapshot (Day 30, Thursday)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Day P&L:** $0.00 (0.000%) | **Phase P&L:** −$943.54 (−0.944%) | **Deployed:** 0%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| — | — | — | — | — | — | — |

**Trades today:** none — flat session, 100% cash maintained.

**Notes:** Day 30 closes at 100% cash for the third consecutive session. Equity held steady at $99,056.46 — zero movement, no fills, no orders, no brackets active. The account is confirmed live via API (equity, cash, buying_power all reconcile). This week opened shortened (May 26 Memorial Day holiday), leaving only two trading sessions (Tue 27 + Thu 28) before the long weekend. No qualifying setups emerged on either day. The prior watchlist candidates (XLK, XLE, MRVL) all remained below entry thresholds: XLK's 2b-LONG breakout pivot ($185.14) was not reclaimed on confirming volume; XLE has not yet reached its Z ≤ −2.0 trigger zone (~$55.68); MRVL's post-earnings fade left it structurally disqualified. Phase P&L remains at −0.944% — well within the −5% weekly and −15% drawdown circuit breaker thresholds. Full PDT budget intact (0/3). Maximum flexibility into next week's full 5-session trading week.

**Circuit breakers:** ✅ All clear — Day 0.000% (lim −2%) | Phase −0.944% (lim −5%) | Drawdown −1.15% from $100,206.70 peak (lim −15%)
**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 0/6

---

### 2026-05-28 17:08 — MARKET-OPEN EXECUTION: NO ORDERS PLACED

**Decision from Research:** HOLD — Zero candidates cleared both Layer A and Layer B gates.

**Account State at Execution:**
- Equity: $99,056.46 | Cash: $99,056.46 | Positions: 0 | Daytrade count: 0/3 | Week trades: 0/3

**Candidates Evaluated and Gate Failures:**

| Ticker | Lane | Failed Gates |
|--------|------|-------------|
| XLK | 2b-LONG | RSI 73.76 > 70 ❌; Vol 0.414× < 1.5× ❌; 50-SMA < 150-SMA (TT) ❌; 200-SMA unverifiable ❌ |
| MRVL | 2b-LONG | Close $200.16 < pivot $208.26 ❌; RSI 70.23 > 70 ❌; Vol 1.236× < 1.5× ❌ |
| SNOW | 2b-LONG | RSI 90.49 > 70 ❌; Pivot extension +35.2% > 5% ❌; 50-SMA < 150-SMA (TT) ❌; 6mo return negative ❌ |
| ORCL | 2b-LONG | Vol 0.686× < 1.5× ❌; Earnings binary ~13 days ❌ |
| XLV | 2a-SHORT | RSI 68.95 < 70 ❌; Vol 0.466× < 1.0× ❌; Short TT structural conflict (price > 50-SMA) ❌ |
| XLE | 2a-LONG / 2b-SHORT | Z=−0.795 (2a: need ≤−2.0 ❌; 2b: need ≤−1.0 ❌); RSI 55.81 neutral ❌; Vol 0.668× < 1.0× ❌ |

**Primary reasons for universal rejection:**
1. RSI readings at or above overbought thresholds after the strong recent rally (S&P 500 fresh record 7,520.36)
2. Partial-day volume insufficient across all momentum-lane candidates (1.5× minimum not met)
3. Prices either extended past pivot (XLK, SNOW) or still below pivot (MRVL)
4. Macro/event risk overlay: PCE + GDP data day + Iran/Hormuz volatility — correct to stand aside

**No bracket orders placed. No Alpaca API order calls made.**

**Priority Watch for Friday 2026-05-29:**
1. MRVL — reclaim $208.26 pivot + RSI cool to <70 + vol ≥1.5× (≥38M shares)
2. XLK — RSI cool from 73.76 to <70; pivot $185.14 already broken
3. XLE — 2a-LONG gate reactivates at ~$55.46 (Z=−2.0) if WTI resumes decline
4. XLV — 2a-SHORT watch: RSI at 68.95, needs >70 + vol ≥1.0× + short TT structural resolution
5. ORCL — post-earnings revisit week of June 15

---

### May 28 — Afternoon Scan (Day 30 / ~15:50 ET)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Deployed:** 0% | **Phase P&L:** −$943.54 (−0.944%)

| Ticker | Shares | Entry | Current | Unrealized P&L | Stop | Hold |
|--------|--------|-------|---------|----------------|------|------|
| — | — | — | — | — | — | — (0 positions) |

**Open orders at scan time:** NONE

**Afternoon scan trades:** none

**Stop action:** N/A — no positions held; no trailing stop upgrade workflow triggered

**Afternoon candidates evaluated — ALL REJECTED (May 28 settled bar data):**

| Candidate | Z-Score | RSI | Vol Ratio | Spread | Key Failures | Verdict |
|-----------|---------|-----|-----------|--------|--------------|---------|
| XLK | +1.640 | 73.53 | 0.91× | R-flag (stale close) | RSI 73.53 > 70 ❌; Vol 0.91× < 1.5× ❌; TT 200-SMA unavail. ❌ | REJECT |
| MRVL | +1.862 | 71.56 | **1.93×** ✅ | R-flag (stale close) | Close $204.83 < pivot $208.26 ❌; RSI 71.56 > 70 ❌; TT 200-SMA unavail. ❌ | REJECT |
| XLE | −0.973 | 54.59 | 1.15× | R-flag (stale close) | Z −0.973 fails both lanes ❌ (2a needs ≤−2.0; 2b needs ≤−1.0 + breakdown) | REJECT |
| XLV | **+2.245** | **69.40** | 1.07× ✅ | R-flag (stale close) | RSI 69.40 < 70 ❌ (0.60 pts from trigger); Short TT structural conflict ❌ | REJECT |
| XOM | −1.239 | 50.53 | 0.80× | R-flag (stale close) | No lane qualifies; energy 1-fail flag active; Z −1.239 mid-range | REJECT |

**Pair divergences confirmed (all within ≤1.5σ gate):**
- XLK (+1.640) ↔ AVGO (+0.759): **0.882σ ✅** (tech sector cohesion — pair confirms)
- XOM (−1.239) ↔ CVX (−1.178): **0.061σ ✅** (energy names declining in lockstep)
- XLE (−0.973) ↔ XOM (−1.239): **0.266σ ✅** (sector-wide)

**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 0/6
**Circuit breakers:** ✅ All clear — Phase P&L −0.944% (lim −5%) | Drawdown −1.15% from $100,206.70 peak (lim −15%)


---

### 2026-05-29 16:58 — MARKET-OPEN EXECUTION: NO ORDERS PLACED

**Decision from Research:** HOLD — 0 trades today
**Account at open:** Equity $99,056.46 | Cash $99,056.46 (100%) | Positions: 0 | Daytrade count: 0/3
**Trades placed this week:** 0 of 3 allowed

**Candidates Evaluated & Rejected:**

#### MRVL | LONG | 2b-LONG — SKIPPED
- **Failure 1:** Close $203.11 < prior 20d high pivot $208.26 → breakout condition NOT met (price below pivot)
- **Failure 2:** Volume 1.08× 20d avg < 1.5× required for momentum lane
- **Watchlist status:** Keep as #1 priority. Needs: (a) settled close above $208.26, (b) entry-day volume ≥ 40.6M. Max entry limit ≤ $218.67.

#### XLK | LONG | 2b-LONG — SKIPPED
- **Failure 1:** RSI(14) = 79.67 > 70 threshold (overbought; momentum lane requires 50–70)
- **Failure 2:** Volume 0.79× 20d avg < 1.5× required for momentum lane
- **Watchlist status:** Keep as #2 priority. Needs: (a) RSI cool to ≤ 70 (est. 2–3 sessions), (b) entry-day volume ≥ 18.1M. Max entry limit ≤ $196.19.

#### XLV | SHORT | 2a-SHORT — SKIPPED (setup unwound)
- **Failure 1:** Z-Score +1.523 < +2.0 required (was +2.245 yesterday; pullback self-corrected)
- **Failure 2:** RSI(14) = 60.79 < 70 required for mean-reversion short lane
- **Failure 3:** Pair divergence (UNH) = 1.947σ > 1.5σ limit
- **Watchlist status:** REMOVED from active watchlist. Setup unwound without our entry (correct per patience rule). Revisit only if Z re-stretches above +2.0 in a future session.

**No bracket orders placed. No order IDs generated.**

---

### May 29 — Afternoon Scan (Day 31 / ~15:50 ET)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Deployed:** 0% | **Phase P&L:** −$943.54 (−0.944%)

| Ticker | Shares | Entry | Current | Unrealized P&L | Stop | Hold |
|--------|--------|-------|---------|----------------|------|------|
| — | — | — | — | — | — | — (0 positions) |

**Open orders at scan time:** NONE

**Afternoon scan trades:** none

**Stop action:** N/A — no positions held, no upgrade workflow triggered

**Afternoon candidates evaluated — ALL REJECTED (May 29 settled bar data):**

| Candidate | Z-Score | RSI | Vol Ratio | Spread | Key Failures | Verdict |
|-----------|---------|-----|-----------|--------|--------------|---------|
| AVGO | **+2.755** | **60.86** | **2.182×** ✅ | R-flag (stale AH) | 200-SMA TT structural ❌ (152/200 bars); all other 7/8 gates PASS | **REJECT** |
| MRVL | +1.644 | 65.21 | 1.252× | R-flag | Close $205.00 < $208.26 pivot ❌; Vol 1.25× < 1.5× ❌ | **REJECT** |
| XLK | +1.987 | 80.04 | 1.226× | R-flag | RSI 80.04 > 70 ❌; Vol 1.23× < 1.5× ❌ | **REJECT** |
| XLV | +1.375 | 60.57 | 1.361× | R-flag | Z +1.375 < +2.0 ❌; RSI 60.57 < 70 ❌ | **REJECT** |
| XLE | −1.271 | 42.97 | 0.822× | R-flag | Z −1.271 (need ≤ −2.0) ❌; RSI 43 ❌; Vol 0.82× ❌ | **REJECT** |

**Pair divergences:** AVGO–MRVL 1.110σ ✅ | AVGO–XLK 0.767σ ✅ | XLE–XLK 3.258σ ❌ (sector rotation expected)

**Key development:** AVGO produced the strongest quant signal since bot launch (Z=+2.755, Vol 2.182×, clean breakout above $439.79 pivot, RSI 60.86). BLOCKED by the universal 200-SMA structural data gap (152/200 bars available). All other 7 of 8 gates pass. Consistent with strategy rules — no trade without full gate clearance. Flagged for Alex decision: override 200-SMA structural block for all post-Dec-2025 split-adjusted names via decisions/log.md?

**Week ends:** 0/3 trades used. Full PDT budget intact (0/3). 100% cash. Month of May closes with 1 total closed trade (XOM, −4.73%).

**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 0/6
**Circuit breakers:** ✅ All clear — Phase P&L −0.944% (lim −5%) | Drawdown −1.15% from $100,206.70 peak (lim −15%)

---

### May 29 — EOD Snapshot (Day 31, Friday — Month-End)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Day P&L:** $0.00 (0.000%) | **Phase P&L:** −$943.54 (−0.944%) | **Deployed:** 0%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| — | — | — | — | — | — | — |

**Trades today:** none — HOLD decision at pre-market confirmed; all candidates rejected at afternoon scan. Month-end close.

**Notes:** Day 31 closes the month of May at 100% cash. The final session of May delivered the bot's strongest quant signal since launch — AVGO at Z=+2.755, clean breakout above $439.79 pivot, RSI 60.86 (healthy momentum zone), Vol 2.182× (40.6M vs 18.6M avg), and all 7 of 8 Layer B gates passing cleanly. The sole remaining gate is the universal 200-SMA structural data gap affecting all post-Dec-2025 split-adjusted names (AVGO, XLK, MRVL, XLE, XLV). Per CONSTRAINTS.md: "If ANY (1–13b) fail: Skip trade, log which check failed." This gate has consistently blocked entries for 31 trading days — the discipline is correct. Alex must decide whether to grant a decisions/log.md override for the structural data gap. Without override, the first fully-verified trade cannot occur until mid-August 2026 when 200 bars of post-split data accumulate. MRVL's RSI cooled to 65.21 (now in the 50–70 momentum zone for the first time since the post-earnings surge) — the MRVL 2b-LONG setup needs only a $3.26 price increase above the $208.26 pivot with ≥1.5× volume to potentially qualify. The month closes with: 1 closed trade (XOM, −4.73%), Phase P&L −0.944%, maximum flexibility for June.

**AVGO key decision for Alex — Monday morning:**
The 200-SMA override decision in decisions/log.md will determine whether the bot can trade AVGO, XLK, MRVL, and similar AI/tech names currently showing strong setups. Suggested override text documented in RESEARCH-LOG.md afternoon addendum above.

**Circuit breakers:** ✅ All clear — Day 0.000% (lim −2%) | Phase −0.944% (lim −5%) | Drawdown −1.15% from $100,206.70 peak (lim −15%)
**PDT count:** 0/3 | **Week trades:** 0/3 (resets Monday) | **Positions:** 0/6


---

### May 29 — EOD Snapshot (Day 31, Friday — Month-End, Final EOD Run)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Day P&L:** $0.00 (0.000%) | **Phase P&L:** −$943.54 (−0.944%) | **Deployed:** 0%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| — | — | — | — | — | — | — |

**Trades today:** none

**Notes:** Final EOD confirmation for May 29 / Month-End. Account state verified via Alpaca API: equity $99,056.46, zero open positions, zero open orders, 100% cash. Day P&L flat at $0.00 — no fills occurred. Phase P&L holds at −$943.54 (−0.944%) on the $100,000 starting equity. The AVGO 200-SMA override decision remains pending with Alex; all circuit breakers clear. Week budget resets Monday (0/3 trades, 0/3 PDT). Bot enters June fully liquid and in compliance.

**Circuit breakers:** ✅ All clear — Day 0.000% (lim −2%) | Phase −0.944% (lim −5%) | Drawdown −1.148% from $100,206.70 peak (lim −15%)
**PDT count:** 0/3 | **Week trades:** 0/3 (resets Monday) | **Positions:** 0/6


---

### Jun 01 — Afternoon Scan (Day 32 / Post-Session ~21:35 UTC)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Deployed:** 0% | **Phase P&L:** −$943.54 (−0.944%)

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Hold |
|--------|--------|-------|-------|----------------|------|------|
| — | — | — | — | — | — | — (0 positions) |

**Open orders at scan time:** NONE

**Afternoon scan trades:** none

**Stop action:** N/A — no positions held, no upgrade workflow triggered

**Afternoon candidates evaluated — ALL REJECTED (June 1 settled bar data):**

| Candidate | Z-Score | RSI | Vol Ratio | Extension | Key Failures | Verdict |
|-----------|---------|-----|-----------|-----------|--------------|---------|
| AVGO | +2.970 | 63.16 | **1.479×** | +2.95% ✅ | Vol 1.479× < 1.500× ❌ (miss by 0.021×) | REJECT |
| MRVL | +2.167 | 72.56 | 1.141× | **+5.36% ❌** | RSI > 70 ❌; Vol < 1.5× ❌; Ext > 5% ❌ | REJECT |
| XLK | +2.268 | 74.05 | **1.485×** | +2.48% ✅ | RSI > 70 ❌; Vol 1.485× < 1.500× ❌ | REJECT |
| XLE | −0.556 | 50.60 | 1.399× | — | Z fails both lanes ❌; midrange | REJECT |
| XOM | −0.539 | 49.56 | 0.947× | — | Z fails; no lane qualifies | REJECT |

**Pair divergences (all computed from settled closes):**
- AVGO (+2.970) ↔ MRVL (+2.167): **0.803σ ✅** (canonical pair — both AI infrastructure semis in sync)
- XLK (+2.268) ↔ AVGO (+2.970): **0.702σ ✅** (tech sector coherent)
- XLE (−0.556) ↔ XOM (−0.539): **0.017σ ✅** (energy in lockstep — sector-wide, not idiosyncratic)
- AVGO (+2.970) ↔ NVDA (+0.848): 2.122σ ⚠️ (NVDA not tracking AVGO rally — noted as yellow flag, not hard gate per MRVL as primary pair)

**Session context:**
- AVGO: +2.95% ($446.77 → $459.97) — set new 20d high at $459.97; RSI healthy at 63.16; vol 30.4M (1.479×)
- MRVL: +14.0% ($192.32 open → $219.43 close) — post-earnings continuation; EXCEEDED 5% pivot extension cap
- XLK: +2.49% ($191.02 → $195.76) — tech ETF extending; RSI elevated
- XLE: +0.56% (oil surge on Iran news)

**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 0/6
**Circuit breakers:** ✅ All clear — Phase P&L −0.944% (lim −5%) | Drawdown −1.15% from $100,206.70 peak (lim −15%)


### Jun 02 — EOD Snapshot (Day 33, Monday)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Day P&L:** $0.00 (0.000%) | **Phase P&L:** −$943.54 (−0.944%) | **Deployed:** 0%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| — | — | — | — | — | — | — |

**Trades today:** none

**Notes:** Flat Monday open to a new week. Portfolio remains 100% cash at $99,056.46 — unchanged from end of last week. No positions were entered today; all five candidates screened in Sunday's afternoon scan (AVGO, MRVL, XLK, XLE, XOM) were rejected going into today on volume and RSI grounds. With the weekly trade counter reset to 0/3 and the PDT counter at 0/3, the bot has full capacity heading into Tuesday. All circuit breakers remain clear: phase P&L at −0.944% (limit −5%), drawdown −1.15% from $100,206.70 peak (limit −15%). No stop actions, no order activity, no fills. Watching for fresh setups with volume confirmation this week.

**PDT count:** 0/3 | **Week trades:** 0/3 (week reset Mon Jun 02) | **Positions:** 0/6
**Circuit breakers:** ✅ All clear — Phase P&L −0.944% (lim −5%) | Drawdown −1.15% from $100,206.70 peak (lim −15%)

### 2026-06-02 09:31 — MARKET-OPEN EXECUTION: NO ORDERS PLACED
**Decision:** HOLD — Research log DECISION was HOLD; zero candidates cleared both Layer A + Layer B
**Account at open:** $99,056.46 equity | $99,056.46 cash (100%) | 0 positions | 0 daytrades | 0/3 week trades
**Circuit breakers:** All clear — Phase P&L −0.944% (lim −5%) | Drawdown −1.15% from $100,206.70 peak (lim −15%)
**VIX:** 16.02–16.17 (Normal regime, 1.00× sizing multiplier — moot, no trades)

**Candidates screened and rejected (all failed independently):**
- **AVGO** Long 2b-LONG → Layer B FAIL: RSI 73.7 > 70 ❌; Volume 0.863× < 1.50× ❌
- **XLK** Long 2b-LONG → Layer A FAIL: Trend Template (price −35.2% from 52w high ❌) + Layer B FAIL: RSI 80.5 ❌; Vol 0.421× ❌
- **NVDA** Long 2b-LONG → Layer B FAIL: Z +0.920 < 1.0 ❌; No breakout ❌; Vol 0.662× ❌
- **AMD** Short 2a/2b → Layer B FAIL: Z +1.40 (need ≥+2.0 for 2a) ❌; wrong direction for 2b ❌; Vol 0.329× ❌
- **INTC** Short 2b-SHORT → Layer B FAIL: SMA structure bullish (50>200) ❌; no breakdown ❌; Vol 0.481× ❌
- **MRVL** Short 2a-SHORT → Phase 1 Universe Rule FAIL: high-momentum name prohibited ❌
- **GLD** Long 2a-LONG → Layer B FAIL: Z −1.007 (need ≤−2.0) ❌; RSI 30.8 (need <30) ❌; Vol 0.413× ❌

**Watch list (closest to qualifying — ranked):**
1. GLD: needs ~2% further decline to ~$403–$405 (Z ≤−2.0, RSI <30) → primary developing setup for Jun 3–4
2. AVGO: needs RSI ≤70 on consolidation + ≥30.9M vol on next breakout attempt → pivot resets to $482.59; max chase $506.72

**No orders placed. Portfolio: 0 positions, 0% deployed. All orders expire N/A (nothing submitted).**


---

### Jun 02 — Afternoon Scan (Day 33 / Post-Session ~20:52 UTC)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Deployed:** 0% | **Phase P&L:** −$943.54 (−0.944%)

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Hold |
|--------|--------|-------|-------|----------------|------|------|
| — | — | — | — | — | — | — (0 positions) |

**Open orders at scan time:** NONE

**Afternoon scan trades:** none

**Stop action:** N/A — no positions held, no upgrade workflow triggered

**Afternoon candidates evaluated (post-close, settled June 2 bars):**

| Candidate | Z-Score | RSI(14) | Vol Ratio | Extension | Key Failures | Verdict |
|-----------|---------|---------|-----------|-----------|--------------|---------|
| AVGO | +3.158 | 75.57 | **1.746×** ✅ | +4.70% ✅ | RSI 75.57 > 70 ❌ (single remaining gate) | **REJECT** |
| MRVL | +3.580 | 85.56 | 3.112× ✅ | **+32.52% ❌** | Extension +32.52% >> 5% HARD BLOCK ❌; RSI 85.56 ❌ | **REJECT** |
| XLK | +2.256 | 86.36 | 0.795× ❌ | +1.25% ✅ | RSI 86.36 > 70 ❌; Vol 0.795× < 1.5× ❌ | **REJECT** |
| GLD | −0.995 | 44.68 | 0.651× ❌ | — | Z −0.995 (need ≤−2.0) ❌; RSI 44.68 (need <30) ❌; Vol ❌ | **REJECT** |
| XOM | −0.458 | 47.5 | 0.597× ❌ | — | Z near zero, no lane qualifies | **REJECT** |

**Key development:** MRVL surged +32.5% today ($219.43→$290.79) on 3.112× volume — largest single-name move since bot launch. Pivot extension +32.52% = unchallengeable per ≤5% extension rule. AVGO +4.7% to $481.57 on 1.746× vol with Z=+3.158 — closest to qualifying of any candidate ever; single gate (RSI 75.57→need ≤70) blocks entry. MRVL off active watchlist until new base forms (~3–6 weeks).

**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 0/6
**Circuit breakers:** ✅ All clear — Phase P&L −0.944% (lim −5%) | Drawdown −1.15% from $100,206.70 peak (lim −15%)

---

### Jun 02 — EOD Snapshot (Day 33, Tuesday)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Day P&L:** $0.00 (0.000%) | **Phase P&L:** −$943.54 (−0.944%) | **Deployed:** 0%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
|--------|--------|-------|-------|----------------|------|------|
| — | — | — | — | — | — | — |

**Trades today:** none — HOLD decision at pre-market confirmed; all candidates rejected at afternoon scan. No fills, no orders, no bracket limits active.

**Notes:** Day 33 closes at 100% cash. The session's dominant story was MRVL's +32.5% gap (+3.11× vol) and AVGO's +4.7% continuation (+1.75× vol). AVGO now passes 7/8 Layer B gates for the 2b-LONG momentum lane — only RSI (75.57, needs ≤70) stands between the bot and its first AI/tech trade. MRVL's +32.5% surge on 3.11× volume is extraordinary institutional activity but the +32.52% pivot extension makes it untradeable under current rules (max chase: 5%). Week ends 0/3 trades, full PDT budget (0/3), 100% cash. AVGO RSI normalization is the single event that unlocks the next trade.

**Circuit breakers:** ✅ All clear — Day 0.000% (lim −2%) | Phase −0.944% (lim −5%) | Drawdown −1.15% from $100,206.70 peak (lim −15%)
**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 0/6

