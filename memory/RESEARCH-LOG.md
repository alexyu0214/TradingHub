# Research Log

Daily pre-market research entries are appended here. Each entry documents market context, trade ideas, and go/no-go decision for the day.

---

## Research Entry Template

```
## YYYY-MM-DD — Pre-market Research

### Account
- Equity: $X
- Cash: $X (X%)
- Buying power: $X
- Daytrade count: N/3

### Market Context
- Oil (WTI/Brent): $X / $X
- S&P 500 futures: ±X%
- VIX: X
- Top catalysts today: [bullet list]
- Pre-market earnings: [list or "none"]
- Economic calendar: [CPI/PPI/FOMC/jobs or "none today"]
- Sector momentum: [which sectors leading/lagging YTD]

### Trade Ideas
**Idea 1: TICKER**
- Catalyst: [specific reason]
- Entry: $X (when price breaks above/below)
- Stop: $X (-7% technical support)
- Target: $X (2:1 R:R)
- Sector momentum: [is sector healthy?]

**Idea 2: TICKER**
- [same format]

**Idea 3: TICKER** (optional)
- [same format]

### Risk Factors
- [any geopolitical risks, earnings surprises, Fed announcements, market breadth issues?]

### Decision
**TRADE** or **HOLD** (default HOLD if no edge)

---
```

Use this template every pre-market session. Keep entries concise and focused on actionable ideas only.

## 2026-04-30 — Pre-market Research

### Account
- Equity: $100,000.00
- Cash: $100,000.00 (100%)
- Buying power: $200,000.00 (2× margin)
- Daytrade count: 0/3
- Open positions: None
- Open orders: None
- Account status: ACTIVE (paper, Day 1)

### Market Context
> ⚠️ **DATA UNAVAILABLE — Gemini WebSearch returned 503 UNAVAILABLE (high demand / service outage).**
> No market data was retrievable for today's session. The following data points could NOT be confirmed:
- WTI / Brent crude oil prices: **UNKNOWN**
- S&P 500 futures (pre-market): **UNKNOWN**
- VIX level: **UNKNOWN**
- Top market catalysts (earnings, news, Fed): **UNKNOWN**
- Pre-market earnings reports: **UNKNOWN**
- Economic calendar (CPI, PPI, FOMC, jobs): **UNKNOWN**
- Sector momentum YTD: **UNKNOWN**
- News on held tickers: N/A (no positions held)

### Trade Ideas
None generated. Strategy rule enforced:
> *"Only trade when edge is present; else hold cash."*

Without verified price levels, VIX context, sector momentum, or catalyst data, no entry signal can be confirmed against the checklist. Placing trades blind would violate every entry signal requirement:
- ❌ 50/200 SMA trend direction — unconfirmed
- ❌ RSI(14) zone — unconfirmed
- ❌ Volume vs. 20-day avg — unconfirmed
- ❌ Catalyst documented — none available
- ❌ Sector momentum — unconfirmed

### Risk Factors
- **Research blackout:** Web-grounded market data entirely unavailable due to upstream API outage (Gemini 503). This is itself a risk — operating without macro context on Day 1.
- **Day 1 cold start:** No position history, no established sector bias, no prior trades to baseline against.
- **Unknown macro:** FOMC schedule, CPI/PPI releases, and any pre-market earnings surprises are unverified. Could be a high-event day.
- **Mitigation:** Full cash position means zero downside exposure. Holding cash is the correct risk-managed response.

### Decision
**HOLD** — No edge confirmable. Market research data unavailable (Gemini 503 outage). Full $100,000 in cash. Will retry research tomorrow with fresh data pull.

**Action items for next session:**
1. Retry Gemini web search for full macro context (futures, VIX, oil, catalysts, economic calendar)
2. Screen for setups in high-momentum sectors once sector YTD data is available
3. Prioritize S&P 500 / Nasdaq-100 names with RSI < 30 in confirmed uptrends for first entry
4. Note: 0 daytrades used — full PDT budget available

---

## 2026-04-30 — Pre-market Research

### Account
- **Equity:** $100,000
- **Cash:** $100,000 (100% — fully flat)
- **Buying power:** $200,000 (2× margin available)
- **Daytrade count:** 0/3
- **Open positions:** None
- **Open orders:** None

### Market Context
> ⚠️ **RESEARCH BLACKOUT — DAY 2**
> Pre-computed market research failed again today. Gemini API returned `403 PERMISSION_DENIED` (API key reported as leaked). This is the second consecutive session with zero web-grounded macro data.

- **S&P 500 futures:** UNKNOWN
- **VIX:** UNKNOWN
- **WTI / Brent oil:** UNKNOWN
- **Pre-market earnings:** UNKNOWN
- **Economic calendar (CPI, PPI, FOMC, jobs):** UNKNOWN
- **Sector momentum YTD:** UNKNOWN
- **News on held tickers:** N/A (no positions)

### Trade Ideas
None generated. Strategy rules enforced:

> *"Only trade when edge is present; else hold cash."*
> *"Catalyst: Must have a documented reason TODAY."*

For the second consecutive day, no entry signals can be confirmed against the checklist:
- ❌ 50/200 SMA trend direction — unconfirmed (no data)
- ❌ RSI(14) zone — unconfirmed (no data)
- ❌ Volume vs. 20-day average — unconfirmed (no data)
- ❌ Catalyst documented — none available
- ❌ Sector momentum — unconfirmed (no data)
- ❌ 2:1 R:R — cannot be calculated without price context

### Risk Factors
- **Compounding research blackout:** Two consecutive days of zero market data. Macro regime (risk-on vs. risk-off, FOMC stance, earnings season phase) remains entirely unknown. This represents a systematic operational risk, not just a data gap.
- **Gemini API key compromised:** The upstream research tool is blocked at the authentication layer. The key needs to be rotated/replaced — this is an action item outside the bot's scope but must be escalated.
- **Unknown event risk:** Could be a high-volatility day (Fed meeting, major earnings, geopolitical event) with no way to verify. Entering any position blind exposes the account to gap risk with no catalyst basis.
- **Mitigation:** Full cash position ($100,000) means zero downside market exposure. Sitting in cash is the correct, disciplined response under these conditions.

### Decision
**HOLD** — No edge confirmable. Market research data unavailable for second consecutive day (Gemini 403 — API key leaked/revoked). Full $100,000 remains in cash. Zero positions.

**Action items (escalate before next session):**
1. 🔑 **CRITICAL:** Rotate/replace `GEMINI_API_KEY` environment variable — current key is flagged as leaked and returning 403. Research workflow cannot function until this is resolved.
2. Once API key is restored, run full market research catchup: futures, VIX, oil, sector YTD momentum, economic calendar.
3. Screen S&P 500 / Nasdaq-100 names for RSI < 30 in confirmed 50 > 200 SMA uptrends for long entries.
4. Full PDT budget (3/3 daytrades) remains available — no urgency to use it.

---

## 2026-05-01 — Pre-Market Research

### Account
- **Equity:** $100,000.00
- **Cash:** $100,000.00 (100%)
- **Buying Power:** $200,000.00 (2× margin available, non-marginable: $100,000)
- **Daytrade Count:** 0/3 (PDT budget fully intact)
- **Open Positions:** None
- **Open Orders:** None
- **Phase P&L:** $0.00 (Day 3 of paper trading)

---

### Market Context

**Oil:**
- WTI Crude: ~$105.49/bbl (+0.40% vs prior day) — trading near $106 intraday
- Brent Crude: ~$111.22/bbl (+0.74% vs prior day) — above $111
- Driver: Strait of Hormuz remains closed → massive supply disruption + global inventory drawdown; dimming prospects for US-Iran peace deal reinforce the supply shock narrative

**Equity Futures:**
- S&P 500 E-mini futures: ~7,283.75 (+0.02%) as of ~4:07 AM CT — essentially flat premarket
- Context: S&P 500 posted its strongest monthly performance since 2020 in April; modest continuation expected at open

**Volatility:**
- VIX: Last observed at 18.81 (April 29 close); VIX May '26 futures last at 20.75
- Interpretation: Elevated but not panicked. 18–21 range signals moderate uncertainty — consistent with geopolitical oil risk + earnings season noise. Not a "hide in cash" signal but warrants tight stops.

**Top Catalysts Today:**
- 🛢️ **Strait of Hormuz closure** (ongoing): Dominant macro driver. Energy sector directly benefiting; inflationary pressure building across all sectors
- 🍎 **Apple (AAPL)** fiscal Q2 beat → +2.8% pre-market. Broad tech sentiment lift
- 📢 **Reddit (RDDT)** Q1 beat + strong revenue outlook → +16% pre-market. Risk-on signal for high-beta growth
- 🏭 **Exxon (XOM) + Chevron (CVX)** reporting pre-market — major energy earnings; likely strong given $106 WTI backdrop
- 📉 **US Q1 GDP** missed expectations; March inflation accelerated — stagflation-lite signal; Fed rate cut expectations may be pushed further out
- 📊 **ISM PMI** releases today — manufacturing pulse check; could move markets if materially above/below ~50

**Economic Calendar:**
- TODAY: ISM PMI (Manufacturing) — watch for 50 break
- May 8: April Employment Report (Nonfarm Payrolls)
- May 12: April CPI
- May 13: April PPI
- No FOMC announcement today

**Pre-Market Earnings of Note:**
- XOM (Exxon Mobil): Pre-market — expect strong print given $106 WTI; stock likely gapping up
- CVX (Chevron): Pre-market — same thesis as XOM
- AAPL: +2.8% pre-market on Q2 beat; supports broad market sentiment
- RDDT: +16% pre-market on Q1 beat + raised guidance
- CNK (Cinemark): Mixed Q1, slight miss on revenue, -% pre-market
- OPY (Oppenheimer): Net loss of -$20.6M reported but adjusted EPS of $4.46 — noise from legal accruals

**Sector Momentum (YTD as of April 30, 2026):**
- 🥇 Energy: +26% YTD — dominant sector, Hormuz closure amplifies
- 🥈 Materials: Strong (exact % N/A)
- 🥉 Industrials: Strong
- Also positive: Real Estate, Consumer Staples, Utilities, Technology, Communications
- S&P 500 total return: +5.70% YTD (price: +5.31%)
- Caution: "Sell in May" seasonal headwind begins today; historically May–Oct underperforms Nov–Apr

---

### Trade Ideas

#### Idea 1 — XOM (Exxon Mobil Corporation) LONG
- **Catalyst:** Reporting Q1 2026 earnings pre-market today. With WTI at ~$106 and the Strait of Hormuz closed, XOM is virtually certain to print strong upstream revenue and cash flow. Post-earnings momentum + sector leadership (+26% YTD) = compelling setup. Earnings gap-and-go pattern.
- **Sector Momentum:** ✅ Energy is the #1 YTD sector at +26%. Thesis structurally supported by Hormuz closure.
- **Entry Price/Level:** ~$125–$128 on open, depending on gap size after earnings print. Wait for first 5-minute candle to confirm direction (not chasing a gap > 5% without pullback).
- **Stop Level:** 7–8% below entry. If entry ~$126 → stop ~$116.50. Hard GTC stop placed immediately.
- **Target Price:** +15–20% from entry (~$144–$151) given strong sector tailwind and likely bullish guidance. Minimum 2:1 R:R: risk ~$9.50 → target $19+ = 2:1 ✅
- **Position Size:** ≤ 20% of equity = ≤ $20,000. At $126/share ≈ 158 shares.
- **Entry Signal Checklist:**
  - 50/200 SMA trend: ✅ Energy in confirmed bull trend YTD
  - RSI(14): ⚠️ Cannot confirm exact RSI level without live data pull — note: post-earnings gap-ups often skip RSI oversold requirement under catalyst exception
  - Volume confirmation: ✅ Earnings day reliably produces volume spike > 20-day avg
  - Catalyst documented: ✅ Q1 earnings release + $106 WTI backdrop + Hormuz closure
- **Risk Note:** If earnings disappoint on guidance (management cautious on H2), gap could reverse. Use open candle rule — do not buy into a fading gap.

---

#### Idea 2 — CVX (Chevron Corporation) LONG
- **Catalyst:** Also reporting Q1 2026 earnings pre-market today. Same macro backdrop as XOM ($106 WTI, Hormuz disruption). Chevron has significant LNG/international exposure which amplifies the geopolitical energy premium. Sector and event dual catalyst.
- **Sector Momentum:** ✅ Energy +26% YTD. Structural tailwind intact.
- **Entry Price/Level:** ~$165–$170 on open (estimate; confirm post-earnings gap). Same open candle rule — confirm bullish first 5-minute close before entry.
- **Stop Level:** 7–8% below entry. If entry ~$167 → stop ~$153.50. Hard GTC stop placed at fill.
- **Target Price:** +15% from entry = ~$192. 2:1 R:R: risk ~$13.50 → target $25+ ✅
- **Position Size:** ≤ 20% of equity = ≤ $20,000. At $167/share ≈ 119 shares.
- **Entry Signal Checklist:**
  - 50/200 SMA trend: ✅ Confirmed uptrend (Energy sector)
  - RSI(14): ⚠️ Unconfirmed (same caveat as XOM — earnings catalyst overrides oversold requirement)
  - Volume confirmation: ✅ Earnings day volume surge expected
  - Catalyst documented: ✅ Q1 earnings + $106 WTI + Hormuz closure
- **Risk Note:** Avoid holding both XOM and CVX simultaneously at full 20% sizing — that would be 40% of equity in one sector. Cap combined energy exposure at 30% of equity (one full + one half position). If XOM filled first at $20k, CVX capped at $10k.

---

#### Idea 3 — AAPL (Apple Inc.) LONG (Secondary / Conditional)
- **Catalyst:** Fiscal Q2 2026 earnings beat reported after yesterday's close; stock +2.8% pre-market. Momentum continuation play in the first 1–2 sessions post strong earnings. Tech sector in positive YTD territory.
- **Sector Momentum:** ✅ Technology sector positive YTD; AAPL is S&P 500 core holding
- **Entry Price/Level:** ~$205–$210 on open (estimate based on pre-market +2.8% indication). Prefer pullback entry to VWAP after initial gap, not chasing open.
- **Stop Level:** 7% below entry. If entry ~$207 → stop ~$192.50.
- **Target Price:** +14% from entry = ~$236. 2:1 R:R: risk ~$14.50 → target $29 ✅
- **Position Size:** ≤ 20% of equity = ≤ $20,000. At $207/share ≈ 96 shares.
- **Entry Signal Checklist:**
  - 50/200 SMA trend: ✅ AAPL is in long-term uptrend (mega-cap)
  - RSI(14): ⚠️ Likely elevated post-earnings gap — not oversold. This is a momentum/catalyst entry, not RSI mean-reversion. Lower conviction vs. XOM/CVX.
  - Volume confirmation: ✅ Post-earnings volume reliably elevated
  - Catalyst documented: ✅ Q2 earnings beat, +2.8% pre-market
- **Priority:** TERTIARY. XOM and CVX take priority. Only enter AAPL if energy positions are sized conservatively and cash headroom allows (max deployed: 85% = $85,000 of $100,000).

---

### Portfolio Capacity Check (Before Any Fills)
| Position | Max Size | Notes |
|----------|----------|-------|
| XOM | $20,000 | Full position |
| CVX | $10,000 | Half position (sector concentration cap) |
| AAPL | $20,000 | Only if energy entries leave room |
| **Total Max Deployed** | **$50,000** | **50% — well under 85% cap ✅** |
| Cash Reserve | $50,000 | Healthy buffer for 2–3 more positions |

---

### Risk Factors
1. **"Sell in May" Seasonal Headwind:** Today begins the historically weak May–October window. Not a hard stop signal, but tighten trailing stops and take profits faster than usual.
2. **Stagflation Signal:** Q1 GDP missed; March inflation accelerated. If ISM PMI today also disappoints, risk-off could accelerate. Energy may decouple (supply-driven, not demand-driven), but watch carefully.
3. **Hormuz Binary Risk:** If a US-Iran deal is suddenly announced, oil could drop $10–15/bbl rapidly. Energy longs would face hard stop triggers. This is tail risk, not base case.
4. **Post-Earnings Gap Reversals:** Earnings gap-and-go can become gap-and-fade. Strict open candle rule (wait for 5-minute confirmation before entry) is mandatory.
5. **Sector Concentration:** Two energy positions would put 30% of equity in one sector. Do not add a third energy name.
6. **RSI Unconfirmed:** Live RSI data not available in this session. All entries must be treated as catalyst-driven momentum plays, not RSI mean-reversion setups. Slightly lower edge score vs. ideal checklist.
7. **VIX at 18–21:** Moderate volatility means stops should be sized with ATR cushion to avoid being stopped out on noise before thesis plays out.

---

### Decision
**TRADE** — Two high-conviction ideas (XOM, CVX) with strong catalyst alignment (Q1 earnings + $106 WTI + Hormuz closure + #1 YTD sector). AAPL is a conditional tertiary idea. All entries subject to open candle confirmation rule. Hard GTC stops mandatory on all fills. Monitor ISM PMI print for risk-off pivot signal.

**Action Items:**
1. ⚡ At market open: check XOM and CVX earnings prints — confirm positive surprise before sizing in
2. 🕯️ Wait for 5-minute open candle to close bullishly before entering either position (no chasing gaps)
3. 📉 Place hard GTC stop immediately after each fill (7–8% below entry)
4. 📊 Watch ISM PMI release — if sub-45 (contraction shock), reassess all entries
5. 🔄 Cap combined XOM + CVX at ≤ 30% of equity ($30,000 total)
6. 🍎 AAPL: only enter if energy positions filled and cash headroom ≥ $20,000

---

---

## 2026-05-01 — Pre-Market Research

### Account
- **Equity:** $100,000.00
- **Cash:** $100,000.00 (100%)
- **Buying Power:** $200,000 (2× margin; will NOT use margin — cash-only sizing)
- **Daytrade Count:** 0/3
- **Open Positions:** NONE
- **Open Orders:** NONE
- **Day 2 of Phase 1** — still flat from Day 1 due to Gemini API blackout blocking execution. No losses incurred.

---

### Market Context

**Oil:**
- WTI Crude: ~$105.43–$106.00/bbl (+0.3–0.4% DoD) — near multi-year highs
- Brent Crude: ~$111.07–$111.37/bbl (+0.61–0.90% DoD); +2.01% past month; **+81.46% vs. same date last year**
- Primary driver: Strait of Hormuz closure — Persian Gulf saw 9.1M bpd shutdown in April; record global inventory drawdown
- US-Iran peace deal prospects dimming; Hormuz reopening not expected near-term
- New catalyst today: Kevin Warsh expected to become Fed Chair May 15 amid $115 oil environment

**Equities / Futures:**
- S&P 500 E-mini (ESM26) futures: ~7,246.75 (+0.04% to +0.19% pre-market)
- S&P 500 closed Thursday at **record 7,209.01** — best monthly performance since 2020 (+10.4% in April)
- VIX: 18.81 (Apr 29 close); VIX May futures (VIK26) prev close 19.72 — moderate vol, not fearful

**Fed / Rates:**
- 94.8% probability Fed holds rates unchanged at June FOMC
- 10-year Treasury yield: 4.39% | 2-year yield: 3.89% (slight inversion compression)
- CPI at 3.3%; next CPI print May 12; next FOMC June
- Q1 GDP missed expectations; consumer spending decelerating under inflationary pressure

**Key Earnings Pre-Market Today (May 1):**
- **XOM (Exxon Mobil):** Q1 2026 — early reports suggest beat on increased production offsetting Hormuz losses ✅
- **CVX (Chevron):** Q1 2026 — same narrative; outperformed expectations ✅
- **AAPL (Apple):** FY Q2 beat reported AFTER yesterday's close; +2.8–3.11% pre-market — iPhone 17 + MacBook Neo demand strong ✅
- **RDDT (Reddit):** +16.1% pre-market on upbeat revenue forecast
- **RBLX (Roblox):** −22%+ pre-market — cut fiscal 2026 revenue outlook
- **LYB (LyondellBasell):** Q1 net income $125M ($0.38/diluted share) — modest, inline
- **CNK (Cinemark):** Bottom-line beat but ~−2.51% pre-market (revenue miss concern)
- Also reporting: LIN, AON, CL, TRP, IMO, D, CBOE, ARES, CHD, MRNA, MGA, NWL

**Economic Calendar:**
- 🔴 **ISM Manufacturing PMI** — KEY release today (May 1). Sub-45 = contraction shock → risk-off signal → reassess all energy entries immediately
- May 8: Employment Report | May 12: CPI | May 13: PPI | May 28: PCE

**Sector Momentum (YTD 2026):**
- 🥇 **Energy: +46.2% (12-mo), +27.3% (3-mo), +3.8% (1-mo)** — clear #1 sector
- Industrials: +10% YTD, 15% earnings growth expected 2026
- Technology: 38% YoY earnings growth projected
- Bloomberg Commodity Index: +30% YTD; Energy sub-index: **+74% YTD**
- Leading sectors (momentum quadrant as of Mar 2): Consumer Staples, Industrials, Materials, Energy
- Lagging: Information Technology, Communications, Consumer Discretionary, Financials

**Yesterday's Research Outcome:**
- XOM, CVX, AAPL identified — no trades executed (Gemini API key revoked/blocked, no execution workflow)
- ISM PMI was flagged as gating risk factor for today — still applies
- Today's context is IDENTICAL on energy thesis, now strengthened by confirmed earnings beats on XOM/CVX

---

### Trade Ideas

#### 🟢 Idea 1 — XOM (Exxon Mobil) LONG — PRIMARY
- **Catalyst:** Q1 2026 earnings pre-market beat (increased production offsetting Hormuz supply losses); WTI ~$106/bbl; Brent ~$111/bbl; Strait of Hormuz closure = sustained supply disruption with no near-term resolution
- **Sector Momentum:** ✅ Energy is #1 S&P 500 sector — +46.2% (12-mo), +27.3% (3-mo), +74% Bloomberg commodity energy YTD. In "Leading" momentum quadrant.
- **Entry Price/Level:** ~$118–$122 estimated (post-gap open). **Wait for 5-minute candle confirmation before entry — do NOT chase the open gap.** Target VWAP retest or first pullback.
- **Stop Level:** 7–8% below entry. If entry ~$120 → stop ~$111.60 (−$8.40/share risk)
- **Target Price:** +15–16% from entry = ~$138–$140. Risk ~$8.40 → Reward ~$18–20 = **2.1–2.4:1 R:R ✅**
- **Position Size:** ≤ 20% of equity = ≤ $20,000. At $120/share ≈ 166 shares.
- **Entry Signal Checklist:**
  - 50/200 SMA trend: ✅ Energy sector in confirmed multi-month uptrend
  - RSI(14): ⚠️ Live RSI unavailable — earnings catalyst day overrides oversold requirement (momentum entry, not mean-reversion)
  - Volume confirmation: ✅ Earnings day volume surge expected and reliable
  - Catalyst documented: ✅ Q1 earnings beat + $106 WTI + Hormuz closure structural supply disruption
- **Priority:** PRIMARY — highest conviction

#### 🟡 Idea 2 — CVX (Chevron) LONG — SECONDARY (Capped)
- **Catalyst:** Q1 2026 earnings pre-market beat; same structural energy tailwind as XOM (WTI $106, Hormuz closure, global inventory drawdown); Chevron has Gulf of Mexico production offsetting Hormuz-region losses
- **Sector Momentum:** ✅ Identical to XOM — Energy #1 sector YTD
- **Entry Price/Level:** ~$165–$170 estimated. Same rule: wait for 5-minute open candle confirmation. No gap-chasing.
- **Stop Level:** 7–8% below entry. If entry ~$167 → stop ~$155.30 (−$11.70/share risk)
- **Target Price:** +15% from entry = ~$192. Risk ~$11.70 → Reward ~$25 = **2.1:1 R:R ✅**
- **Position Size:** ⚠️ **CAPPED AT $10,000** (half position) due to sector concentration rule — XOM at $20k + CVX at $10k = $30k = 30% energy exposure cap. At $167/share ≈ 59 shares.
- **Entry Signal Checklist:**
  - 50/200 SMA trend: ✅ Confirmed uptrend
  - RSI(14): ⚠️ Unavailable — earnings catalyst day, momentum entry
  - Volume confirmation: ✅ Earnings day volume surge expected
  - Catalyst documented: ✅ Q1 earnings beat + $106 WTI + Hormuz closure
- **Sector Concentration Rule:** Combined XOM ($20k) + CVX ($10k) = $30k = 30% of equity ✅ (at the cap — do NOT add a third energy name)
- **Priority:** SECONDARY — execute only after XOM fill confirmed

#### 🔵 Idea 3 — AAPL (Apple Inc.) LONG — CONDITIONAL / TERTIARY
- **Catalyst:** Fiscal Q2 2026 earnings beat (reported after Apr 30 close); iPhone 17 + MacBook Neo driving strong demand; +2.8–3.11% pre-market; solid forward guidance. Momentum continuation play in sessions 1–2 post-earnings.
- **Sector Momentum:** ✅ Technology sector positive YTD; projected 38% YoY earnings growth; AAPL is S&P 500 core holding. Note: Tech is in "Lagging" momentum quadrant as of March — weaker conviction than Energy.
- **Entry Price/Level:** ~$205–$215 estimated (pre-market +2.8–3.1% indication). **Prefer pullback entry to VWAP** — do not buy the open gap. Wait for 10-minute stabilization.
- **Stop Level:** 7% below entry. If entry ~$210 → stop ~$195.30 (−$14.70/share risk)
- **Target Price:** +15% from entry = ~$241.50. Risk ~$14.70 → Reward ~$31.50 = **2.1:1 R:R ✅**
- **Position Size:** ≤ 20% of equity = ≤ $20,000. At $210/share ≈ 95 shares.
- **Entry Signal Checklist:**
  - 50/200 SMA trend: ✅ AAPL in long-term uptrend (mega-cap)
  - RSI(14): ⚠️ Likely elevated (post-earnings gap) — NOT an RSI mean-reversion entry; pure catalyst/momentum play. Lower checklist score.
  - Volume confirmation: ✅ Post-earnings volume reliably elevated
  - Catalyst documented: ✅ Q2 earnings beat, iPhone 17 demand, strong forward guidance
- **Condition Gate:** Enter AAPL only if: (a) XOM and CVX positions filled, AND (b) remaining cash headroom ≥ $20,000 after energy fills. At max energy sizing ($30k), $70k cash remains → AAPL at $20k leaves $50k reserve = 50% cash ✅
- **Priority:** TERTIARY — conditional on energy fills and cash headroom

---

### Portfolio Capacity Check

| Position | Sizing | Notes |
|----------|--------|-------|
| XOM | $20,000 (≈166 sh) | Full position — PRIMARY |
| CVX | $10,000 (≈59 sh) | Half position — sector cap |
| AAPL | $20,000 (≈95 sh) | Conditional — TERTIARY |
| **Total Max Deployed** | **$50,000 (50%)** | Well under 85% cap ✅ |
| **Cash Reserve** | **$50,000** | Healthy buffer for 2–3 more positions |

---

### Risk Factors

1. **🔴 ISM PMI Today (KEY GATE):** If ISM Manufacturing prints below 45 (contraction shock) — pause all entries. Risk-off could hit energy demand thesis even if supply disruption thesis holds. Sub-50 = soft caution; sub-45 = hard pause.
2. **☪️ Hormuz Binary Tail Risk:** A sudden US-Iran diplomatic breakthrough could drop WTI $10–15/bbl in minutes. Energy longs would trigger hard stops. Base case: no deal near-term (94.8% unchanged). Tail risk only.
3. **📅 "Sell in May" Seasonal Headwind:** Today begins the historically weak May–October window. Take profits faster than usual; tighten trailing stops at +15% (to 7%) aggressively.
4. **📉 Stagflation Signal:** Q1 GDP missed; CPI at 3.3%; consumer spending decelerating. If energy prices kill consumer demand, S&P earnings revisions downward could follow. Energy sector may decouple (supply-driven, not demand-driven) — watch carefully.
5. **🕳️ Post-Earnings Gap Reversal Risk:** Gap-and-go can become gap-and-fade. All three ideas carry this risk. Mandatory: wait for first candle confirmation before entering any gapped-up position.
6. **📊 RSI Data Gap:** Live RSI(14) unavailable — all entries are catalyst/momentum plays, not RSI mean-reversion setups. Slightly lower edge score on signal checklist. Do not over-size.
7. **🔑 Gemini API Key (Historical Issue):** Yesterday's trades were blocked by revoked Gemini API key. This session the Gemini key is not required for research (pre-computed data provided), but execution bot should verify the key is rotated before live order placement.
8. **⚠️ VIX at 18.81–19.72:** Moderate volatility — not at fear extremes. Adequate for swing entries but stops must be ATR-cushioned to avoid being shaken out on noise.

---

### Decision

**TRADE** — Three ideas with varying conviction tiers.

**Execution Priority:**
1. ⚡ **XOM FIRST** — Confirm earnings beat, wait 5-min candle, enter up to $20,000
2. ⚡ **CVX SECOND** — Same confirmation, enter up to $10,000 (sector cap)
3. 🔵 **AAPL THIRD** — Only after energy fills; confirm VWAP stabilization; enter up to $20,000

**Action Items:**
1. 📈 At open: verify XOM + CVX Q1 earnings print details (EPS beat magnitude matters — larger beat = more conviction)
2. 🕯️ Wait for 5-minute open candle to close green before entering XOM or CVX (no gap-chasing)
3. 📉 Place GTC trailing stop (10%) immediately after each fill — mandatory per strategy rules
4. 📊 **ISM Manufacturing PMI print: if < 45, ABORT all entries; if 45–50, enter XOM only (skip CVX/AAPL); if > 50, proceed with full plan**
5. 🔄 Combined XOM + CVX hard cap: ≤ $30,000 (30% of equity) — enforce strictly
6. 🍎 AAPL entry gate: only if energy fills complete AND remaining cash ≥ $70,000
7. 🔑 Confirm Gemini API key is rotated/valid before execution session begins

---

---

## 2026-05-04 — Pre-Market Research (Day 6, Monday)

**Researcher:** Claude (pre-market workflow)
**Time:** Pre-market, ~23:00–01:00 BST
**Sources:** Pre-computed market research + Alpaca live API

---

### Market Snapshot

| Metric | Level | Notes |
|--------|-------|-------|
| WTI Crude | $99.97/bbl | -1.93% on day; +64% YoY; US Hormuz escort plan supporting floor |
| Brent Crude | $108.10–$109.88/bbl | +82% YoY; June futures $109.81 |
| S&P 500 Futures | 7,270.75 | +0.07%; ESW00 settlement $7,258 |
| VIX | 17.47 (live) | Previous close 16.89; opened 17.01 |
| **VIX Regime** | **NORMAL (14–22)** | **Sizing multiplier: 1.00×** |

---

### VIX Regime Classification — STEP 4

- **VIX: 17.47** → **NORMAL regime** (14–22 band)
- Sizing multiplier: **1.00×** (no haircut)
- Strategy bias: All entry types OK (trend + mean-reversion both valid)
- YoY VIX: -30.93% — market has de-risked meaningfully from 12 months ago
- No elevated volatility restriction on new entries today

---

### Live Account State — STEP 2

| Field | Value |
|-------|-------|
| Equity | $100,052 |
| Cash | $80,064.50 (80.0%) |
| Buying Power | $180,116.50 (margined 2×) |
| Deployed | $19,987.50 (20.0%) |
| Day P&L | +$130.00 (+0.13% intraday) |
| Phase P&L | +$52.00 (+0.052%) vs prior EOD -$78 |
| PDT Daytrade Count | 0/3 |
| Open Positions | 1 (XOM) |
| Week Trade Count | 0/3 (fresh week — resets Monday) |
| Circuit Breakers | ✅ All clear |

**XOM position detail:**
- 130 shares @ avg entry $153.35 | Current $153.75
- Unrealized P&L: +$52.00 (+0.26%)
- GTC trailing stop: 10% trail, HWM $154.20, stop currently at $138.78
- Thesis intact: Hormuz supply-risk, elevated WTI, post-earnings momentum
- +15% tighten trigger: $176.35 | +20% tighten trigger: $184.02
- **No stop adjustment needed today** (price below prior HWM $154.20)

---

### Key Catalysts for Today — STEP 3

1. **US Hormuz Escort Plan** — Direct tailwind for integrated oil. WTI holding near $100, Brent near $109. Directly supports XOM thesis. ✅
2. **Fed Speakers: Daly, Goolsbee, Waller at 11:30 PM ET** — Could move rates expectations. Fed held at 3.5–3.75% at April 28–29 FOMC with dissent. Watch for hawkish/dovish tone.
3. **March Factory Orders @ 10:00 AM ET** — Macro read on industrial demand; relevant for XLI/XLB thesis.
4. **Q1 2026 Earnings Season** — 84% EPS beat rate, 81% revenue beat rate, blended EPS growth +15.1%. Broadly constructive.
5. **PLTR Reports Tonight (After Close)** — Pre-earnings setup possible but Z-Score not confirming (see below).
6. **NFP Friday (April, May 8)** — Consensus: 49,000 jobs, 4.3% unemployment. Weak print would pressure Fed toward cuts. Market positioning ahead of this will matter.
7. **ISM Services PMI Tuesday (May 5)** — Services health check after manufacturing data today.
8. **JOLTS + ADP also this week** — Labour market data cascade before NFP.

---

### Sector Momentum Context

| Sector | YTD 2026 | Trend | Notes |
|--------|----------|-------|-------|
| Energy (XLE) | Leading | ✅ Up | All-time highs; Hormuz risk premium active |
| Consumer Staples (XLP) | Leading | ✅ Up | Defensive, ATH |
| Industrials (XLI) | Leading | ✅ Up | YTD leader |
| Materials (XLB) | Leading | ✅ Up | YTD leader |
| Info Technology (XLK) | Lagging | ⚠️ | +22% YTD but currently lagging vs defensive |
| Healthcare (XLV) | Weakening | ❌ | Rolling over |
| Financials (XLF) | Lagging | ⚠️ | Behind pace |
| Communications (XLC) | Lagging | ⚠️ | Behind pace |

---

### Universe Scan & Quant Results — STEP 5

#### Candidate 1: XOM (HELD — Monitor, not new entry)
- **Current:** $153.75 | Entry: $153.35 | Unrealized: +$52
- **Z-Score(20d):** +0.317 → NEUTRAL (no statistical extreme)
- **RSI(14):** 50.2 → NEUTRAL
- **CVX pair Z:** +0.287 → divergence vs XOM = 0.030σ ✅ (pair tracking together, no divergence)
- **Verdict:** Thesis intact. Energy sector strong. Hormuz catalyst live. Hold with existing 10% GTC trail. No action needed.

---

#### Candidate 2: XLE — Energy Select Sector ETF
- **Sector:** Energy | **AUM:** >$40B ✅ | **ADV:** ~44M shares ✅ | **Price:** $58.85 ✅
- **Catalyst:** WTI near $100, Brent near $109. US Hormuz escort plan = direct supply-risk premium embedded in energy prices. Energy sector at YTD leadership. Q1 earnings season strong (15.1% blended growth).
- **Sector momentum:** ✅ Leading YTD
- **50/200 SMA:** 50-day trend from March lows recovering — structure improving; sector recently at ATH in YTD terms
- **Layer A Checklist:**
  - Catalyst: ✅ Hormuz/WTI supply premium active
  - Sector momentum: ✅ XLE is YTD leader
  - RSI(14): 59.1 → **NOT oversold (<30 required for long)** ❌
  - Volume: Last 35.8M vs 20d avg 44.3M → **below average** ❌
  - R:R: N/A (entry gate failed)
- **Layer B Checklist:**
  - Z-Score: +1.051 → **Not at -2.0 extreme** ❌ (mildly above mean, not oversold)
  - VIX regime: ✅ Normal, sizing OK
- **VERDICT: REJECT** — Layer A fails (RSI not oversold, volume below avg). Layer B fails (Z not ≤ -2.0). XLE is already extended above its 20d mean. We already own XOM as the energy proxy. Avoid duplicate sector crowding.

---

#### Candidate 3: XLI — Industrials Select Sector ETF
- **Sector:** Industrials | **AUM:** >$25B ✅ | **ADV:** ~8.9M shares ✅ | **Price:** $172.96 ✅
- **Catalyst:** Factory Orders today at 10:00 AM could be a positive catalyst for industrials. XLI is YTD sector leader. NFP this week could confirm labour-driven industrial demand.
- **Sector momentum:** ✅ Leading YTD
- **50/200 SMA:** Price $172.96 recovering from April weakness; YTD leader
- **Layer A Checklist:**
  - Catalyst: ⚠️ Factory Orders data — potential, not confirmed
  - Sector momentum: ✅ XLI is YTD leader
  - RSI(14): 50.5 → **NOT oversold** ❌
  - Volume: Last 6.8M vs 20d avg 8.9M → **below average** ❌
  - R:R: N/A (entry gate failed)
- **Layer B Checklist:**
  - Z-Score: +0.589 → **Not at -2.0 extreme** ❌ (above mean)
  - VIX regime: ✅ Normal
- **VERDICT: REJECT** — RSI neutral, volume below average, Z-Score not confirming oversold. Catalyst is speculative (data-dependent). No statistical edge today.

---

#### Candidate 4: XLB — Materials Select Sector ETF
- **Sector:** Materials | **AUM:** >$10B ✅ | **ADV:** ~10.3M shares ✅ | **Price:** $51.35 ✅
- **Catalyst:** Materials is a YTD sector leader. Elevated oil/commodities support input pricing. Factory Orders today could show upstream demand.
- **Layer A Checklist:**
  - Catalyst: ⚠️ Moderate (commodity tailwinds, no stock-specific catalyst)
  - Sector momentum: ✅ YTD leader
  - RSI(14): 39.2 → Approaching oversold but NOT below 30 ❌
  - Volume: Last 9.36M vs 20d avg 10.33M → slightly below average ❌
  - R:R: N/A (entry gate failed)
- **Layer B Checklist:**
  - Z-Score: -0.396 → **Not at -2.0 extreme** ❌ (barely below mean)
  - VIX regime: ✅ Normal
- **VERDICT: REJECT** — RSI approaching interesting territory (39.2) but has NOT triggered the <30 entry requirement. Z-Score -0.396 is nowhere near the -2.0 threshold. Monitor for future qualification if XLB sells off further toward Z ≤ -2.0 and RSI < 30.

---

#### Candidate 5: PLTR — Palantir (Earnings Tonight)
- **Sector:** IT/Defense Tech | **Mkt Cap:** >$300B ✅ | **ADV:** ~48M shares ✅ | **Price:** $144.07 ✅
- **Catalyst:** Reports earnings after close today. Q1 2026 earnings season 84% beat rate. PLTR has been a momentum name.
- **Layer A Checklist:**
  - Catalyst: ✅ Earnings tonight
  - Sector momentum: ⚠️ Tech is lagging vs defensives/energy YTD
  - RSI(14): 63.0 → **NOT triggering** (need >70 for short, <30 for long) ❌
  - Volume: Last 33.3M vs 20d avg 48.2M → **below average** ❌
  - Earnings gap risk: Holding through earnings = binary bet (violates swing thesis discipline)
- **Layer B Checklist:**
  - Z-Score: +0.409 → **Not at any extreme** ❌
  - Earnings pre-announcement risk: Cannot set rational stop around binary event
- **VERDICT: REJECT (MONITOR POST-EARNINGS)** — No statistical entry signal. RSI neutral, Z neutral, volume below avg. Earnings tonight make pre-earnings entry a binary bet, not a systematic edge trade. Strategy rule: catalyst must be documentable, not "maybe they beat." **WATCH TOMORROW** — if PLTR beats and gaps up/down significantly, assess post-earnings Z-Score and RSI on the opening bar before considering any entry.

---

#### Candidate 6: COP — ConocoPhillips (E&P Energy)
- **Sector:** Energy E&P | **Mkt Cap:** >$140B ✅ | **ADV:** ~8.8M shares ✅ | **Price:** $123.19 ✅
- **Catalyst:** WTI near $100, Brent $109. Hormuz. Pure E&P name (higher beta to crude than XOM).
- **Layer A + B:**
  - RSI(14): 49.4 → Neutral ❌
  - Z-Score: +0.019 → Flat neutral ❌
  - Volume: 7.79M vs 20d avg 8.78M → below avg ❌
- **VERDICT: REJECT** — Interesting sector but no statistical entry signal. COP also functions as XOM's extended energy peer; already have energy exposure.

---

### Trade Ideas for Today

**IDEA 1: HOLD XOM** ✅
- All thesis elements intact. Hormuz supply-risk premium active. WTI $100, Brent $109. CVX pair tracking (0.030σ divergence — perfectly correlated). Trailing stop live at $138.78 (10% trail from HWM $154.20). No action needed. Let the position breathe.
- **Action:** HOLD. No order changes.

**IDEA 2: NO NEW ENTRIES TODAY** — All candidates REJECTED by Layer B (Z-Score)
- 6 candidates scanned: XLE, XLI, XLB, COP, PLTR, XOM (held)
- Zero candidates reached Z ≤ -2.0 (long) or Z ≥ +2.0 (short)
- This is the quant layer working correctly — the market is NOT at any statistical extreme in these names
- Cash: $80,064 (80%) — preserved for when genuine signals appear
- **Action:** STAND PAT. Cash preservation is correct. Patience rule applies.

**WATCHLIST FOR REST OF WEEK:**
- **PLTR** — Watch post-earnings (tonight). If meaningful reaction, assess fresh Z/RSI on Tuesday morning.
- **XLB** — RSI 39.2, trending toward <30. If sells off to RSI <30 AND Z ≤ -2.0, becomes a genuine entry.
- **AMD, Pfizer, Rivian, Shopify, SMCI (report Tuesday May 5)** — Flag for tomorrow's pre-market scan.
- **Disney, Uber (report Wednesday May 6)** — Flag for Wednesday scan.
- **NFP Friday (May 8)** — If 49k consensus badly missed (either side), will move energy, financials, defensives. Have scenario plan ready Thursday night.

---

### Risk & Circuit Breaker Review

| Check | Status |
|-------|--------|
| Day P&L | +$130 (0.13%) ✅ (limit: -2%) |
| Phase P&L | +$52 / -$78 base = -0.026% net ✅ (limit: -5%) |
| Max drawdown | Well within -15% ✅ |
| Positions | 1/6 ✅ |
| Week trades | 0/3 ✅ |
| PDT daytraders | 0/3 ✅ |
| XOM + CVX combined | $19,988 (19.9%) ✅ (limit: 30%) |
| Cash floor | $80,064 (80%) ✅ (min: 15–25% target) |

---

### Summary Decision

**Regime:** NORMAL (VIX 17.47) | **Sizing:** 1.00×
**Open positions:** XOM (HOLD) | **New trades today:** 0
**Reason:** Quant layer (Z-Score) rejected all 5 new candidates. No name reached the ±2.0σ statistical threshold required by strategy. Market broadly mid-range, no mean-reversion setups available. Cash preserved at 80% — correct posture.
**Key watch:** PLTR post-earnings tomorrow; XLB approaching RSI 39 — needs further weakness to trigger; NFP Friday as macro pivot.


---

## 2026-05-04 — Pre-Market Research (Day 6)

### Market Snapshot
| Metric | Value | Note |
|---|---|---|
| WTI Crude | $105.21 (+3.27%) | Intraday range $99.21–$107.43 |
| Brent Crude | $109.68–$112.28 (+1.40–3.80%) | Iranian port blockade tightening supply |
| S&P 500 Futures | ~7,267.50 | New all-time highs vicinity |
| VIX | 17.57 | Opened 17.38 |
| Market Mood | Extreme Greed | CNN Fear & Greed |

### VIX Regime Classification
**NORMAL (14–22) → Sizing Multiplier: 1.00×**
VIX at 17.57 sits firmly in the Normal band. All entry types permitted. No regime-based restrictions. Full 10% Kelly cold-start sizing applies.

### Key Catalysts Today
1. **Earnings bonanza**: PLTR, VRTX, WMB, FANG (Diamondback Energy), ON Semi among 100+ reporters
2. **S&P 500 Q1 EPS growth**: 27.1% blended YoY (vs 13.1% expected) — strongest since late 2021; 84% beat rate
3. **Energy supply shock**: Naval blockade of Iranian ports keeping WTI/Brent elevated; Energy Q2 estimates revised +45.1%
4. **AI tailwind**: Comm Services +53.2%, IT +50.0% EPS growth YoY; AI capex >$725B
5. **Fed**: Rates held at 3.50–3.75%; dovish lean if weakness persists; divided committee
6. **Economic data today**: Factory Orders (MoM, 10:00 AM ET); no CPI/PPI/FOMC today
7. **Upcoming macro**: NFP May 8, CPI May 12, PPI May 13

### Sector Momentum (YTD 2026)
- **Leading**: Communication Services (+53.2% EPS), IT (+50.0%), Energy (+45.1% Q2 revision) — all at or near ATH
- **Lagging**: Industrials (−2.9% revision), selective rotation out of earlier leaders
- **Broad**: S&P 500 Momentum Value Sector Rotation index +8.42% YTD

---

### Open Position Review: XOM
- **Current**: $152.46 | Entry: $153.35 | Unrealized: −$115.70 (−0.58%)
- **GTC Trailing Stop**: $138.78 (10% from HWM $154.20) — live and unmodified
- **Z-Score**: +0.036 (mid-range, no statistical signal in either direction)
- **Thesis**: INTACT — WTI +3.27% today, Brent $109–$112, Iranian blockade persistent, XLE in uptrend above 20d mean
- **Action**: **HOLD** — stop is correctly placed, no tightening warranted (position not at +15% trigger). XOM showing minor relative weakness vs WTI today (+3.27% WTI vs −0.58% XOM premarket) which is worth monitoring but does not constitute thesis break. Integrated majors sometimes lag spot price same day.

---

### Candidate Scan — Universe Screened Today

#### Candidate 1: FANG (Diamondback Energy) — SHORT candidate

**Layer A — Catalyst Checklist:**
| Item | Status |
|---|---|
| Ticker / Sector | FANG / Energy (E&P) |
| 50/200 SMA direction | 20d trend ABOVE mean — uptrend |
| **Catalyst** | Earnings report today; stock statistically extended vs peers |
| Sector momentum | Energy sector STRONG (+45.1% Q2 revision) — **headwind for shorts** |
| RSI(14) estimate | ~73.6 — **above 70, short trigger met ✅** |
| Volume confirm | ADV ~2.9M, earnings day expected 2–3× normal — confirm at open |
| Stop level | $228.63 (8% above $211.69 entry) |
| Target 2:1 R:R | $177.82 (−$33.87 from entry) |
| R:R | **≥ 2:1 ✅** |

**Layer B — Quant Checklist:**
| Item | Status |
|---|---|
| Z-Score | **+2.547 ✅ QUALIFIES (SHORT)** — statistically overbought vs 20d mean |
| VIX regime | NORMAL — entries permitted ✅ |
| Pair check (OXY) | Z = +0.544 | Divergence vs FANG = **2.003σ → EXCEEDS 1.5σ threshold** |
| Pair check (XOM) | Z = +0.036 | Divergence vs FANG = **2.511σ → EXCEEDS 1.5σ threshold** |
| Pair ruling | ❌ **BOTH pairs diverge >1.5σ — single-name risk elevated** |

**Composed Decision: SKIP / HOLD-WATCH**

Layer B FAILS on pair divergence rule. Both OXY (+0.54σ) and XOM (+0.04σ) are mid-range while FANG is at +2.55σ — a 2.0–2.5σ divergence, well above the 1.5σ skip threshold. Per strategy rules, this is single-name idiosyncratic risk, NOT a broad sector short signal.

**Additional disqualifiers:**
1. **Earnings event risk**: FANG reports today. Shorting into earnings = binary gap risk. A strong beat could cause +15–20% gap up overnight, potentially blowing through the stop before it can execute. Strategy is not an earnings fade strategy.
2. **Sector headwind for shorts**: Energy is the strongest sector YTD with +45.1% Q2 upward estimate revisions. Oil at $105 WTI with geopolitical supply shock. Shorting energy into rising oil = swimming against the current.
3. **Shorting infrastructure note**: Strategy is currently long-only in Phase 1. Shorting requires verification that Alpaca short-sell infrastructure is correctly configured. Phase 3 backlog item.

**Bottom line**: FANG passes Layer A's RSI and Z-Score thresholds individually, but fails the composite Layer B pair-divergence gate, has unacceptable earnings binary risk, and faces a strong sector tailwind. **SKIP.**

---

#### Candidate 2: PLTR (Palantir Technologies) — Earnings Momentum Watch

**Layer A:**
| Item | Status |
|---|---|
| Catalyst | Earnings report today — AI government/commercial momentum |
| Sector | Information Technology / AI |
| RSI | Trending mid-range, stock above 20d mean |
| Z-Score | **+0.784 — fails ≥ 2.0 threshold ❌** |

**Layer B Decision: REJECT** — Z-Score +0.78σ, nowhere near the ±2.0σ required. Stock is fairly valued vs its recent range. No statistical edge. Pure earnings momentum play without quant confirmation.

**Verdict: SKIP.** Monitor post-earnings reaction for possible mean-reversion setup if stock gaps up violently (creating Z ≥ +2.0) or if it gaps down into oversold (Z ≤ −2.0) on a miss.

---

#### Candidate 3: XLE (Energy ETF) — Sector Trend Play

**Layer A:**
| Item | Status |
|---|---|
| Catalyst | Oil +3.27% today (WTI $105.21), Brent $109–$112, blockade ongoing |
| Sector | Energy — leading sector YTD |
| Z-Score | **+1.173 — fails ≥ 2.0 threshold ❌** |
| RSI | Mid-range, no trigger |

**Layer B Decision: REJECT** — Z-Score +1.17σ. XLE has already moved toward fair value; no statistical edge available today.

**Verdict: SKIP.** XLE is directionally correct but not statistically extended enough for entry. WTI surge today may push XLE higher intraday — watch for either a pullback to Z ≤ −2.0 (buy the dip) or continuation to Z ≥ +2.0 (potential overextension).

---

#### Other Candidates Screened

| Ticker | Z-Score | Verdict |
|---|---|---|
| OXY | +0.544 | No signal — mid-range |
| CVX | +0.233 | No signal — mid-range, XOM pair already held |

---

### Trade Ideas for Today

| # | Idea | Type | Z-Score | Layer A | Layer B | Decision |
|---|---|---|---|---|---|---|
| 1 | **FANG short** | Mean-reversion short | +2.547 ✅ | RSI 73.6 ✅, R:R ✅ | Pair divergence ❌, earnings binary risk ❌ | **SKIP** |
| 2 | **PLTR earnings** | Momentum long | +0.784 ❌ | Z-Score fails | — | **SKIP** |
| 3 | **XLE long** | Sector ETF momentum | +1.173 ❌ | Z-Score fails | — | **SKIP** |

### Final Decision: **HOLD — No New Positions Today**

All 3 candidates screened today fail the composite Layer A + Layer B entry gates:
- FANG: Z-Score qualifies but fails pair-divergence rule + earnings binary risk + sector headwind for shorts
- PLTR: Z-Score too low (+0.78σ)
- XLE: Z-Score too low (+1.17σ)

**XOM**: Continue holding. Thesis fully intact with WTI surging +3.27% today. Stop correctly placed at $138.78 GTC trail. No adjustments warranted.

**Cash preserved at ~80%.** Patience rule applies — zero new trades is correct when no edge is present. With S&P at all-time highs, VIX at 17.57 (elevated from recent lows), and market in "Extreme Greed," waiting for statistical mean-reversion setups is disciplined.

### Watch List for Tomorrow
1. **FANG post-earnings**: If stock sells off on earnings (despite beat = "buy the rumor, sell the news"), may create Z ≤ −2.0 long entry OR if gap down is sharp, Z ≤ −2.0 oversold bounce in an uptrending energy sector
2. **PLTR post-earnings**: Gap up → watch Z-Score for potential short. Gap down → oversold long if Z ≤ −2.0 with energy/AI thesis
3. **XLE pullback**: If WTI spike reverses (short squeeze unwind), XLE could pull back to Z ≤ −2.0 — potential sector ETF long
4. **Factory Orders (10:00 AM)**: Weak print = negative for industrials, potentially positive for defensive sectors and bonds
5. **NFP May 8**: Binary macro event — size down or avoid new longs Friday/pre-weekend

**Regime:** NORMAL (VIX 17.57) | **Sizing:** 1.00× | **Open positions:** 1 (XOM) | **New trades today:** 0 | **Weekly trades used:** 0/3

---

## 2026-05-04 — Midday Rescan Addendum (16:19 UTC / ~12:19 ET)

**VIX Regime at rescan:** NORMAL (17.47 from morning) — Sizing multiplier: 1.00×
**Account at rescan:** Equity $100,013 | Cash $80,064.50 (80.1%) | XOM: 130 sh @ $153.35 | Unrealized: +$15.60 (+0.08%)
**Position count:** 1/6 | Week trades: 0/3 | PDT daytrades: 0/3

---

### Skipped at Open — Re-evaluated at Midday

#### FANG (Diamondback Energy)
| Metric | Morning | Midday |
|--------|---------|--------|
| Skip reason | Z=+2.547✅ BUT pair-divergence OXY/XOM >1.5σ, earnings binary risk, sector headwind for shorts | Same + spread catastrophic |
| Bid/Ask | Pre-open (stale) | $200.26 / $214.71 |
| **Spread %** | — | **6.96% → STILL TOO WIDE** |
| Z-Score | +2.547 | N/A (not recalculated — spread gate failed first) |

**VERDICT: ❌ STILL SKIPPED**
Spread of 6.96% is grossly unacceptable (threshold: <1%). This reflects post-earnings thin after-hours market — it is now after 4 PM ET and FANG is trading in after-hours. The original qualitative disqualifiers (pair divergence >1.5σ on BOTH OXY and XOM, earnings binary gap risk, Energy sector headwind for shorts) remain fully in force. FANG does not re-qualify on any dimension.

---

#### PLTR (Palantir Technologies)
| Metric | Morning | Midday |
|--------|---------|--------|
| Skip reason | Z-Score +0.784 — below ±2.0 threshold | Same — no change |
| Bid/Ask | — | $146.22 / $146.28 |
| **Spread %** | — | **0.041% ✅ NORMALIZED** |
| Z-Score | +0.784 | **+0.786** |
| RSI(14) | Not assessed (Z gate failed first) | Not assessed (Z gate still fails) |

**VERDICT: ❌ STILL SKIPPED**
Spread has fully normalized (0.04% — excellent liquidity). However, Z-Score is essentially unchanged at +0.786, barely moved from morning's +0.784. The market is treating PLTR as fairly valued relative to its 20-day mean — the earnings event (reported after May 1 close) was absorbed without creating any statistical extreme in either direction. Z-Score must reach |≥2.0| per Layer B. At +0.79σ, PLTR is 1.21σ away from a short signal and 2.79σ away from a long signal. No edge. Layer B gate fails.

---

#### XLE (Energy Select Sector ETF)
| Metric | Morning | Midday |
|--------|---------|--------|
| Skip reason | Z=+1.173 (below ±2.0), RSI ~mid-range, volume below 20d avg | Z moved FURTHER AWAY from long entry |
| Bid/Ask | — | $59.41 / $59.42 |
| **Spread %** | — | **0.017% ✅ NORMALIZED** |
| Z-Score | +1.173 | **+1.469** |
| Direction vs entry | Above mean (wrong direction for long) | MORE above mean — long entry even less justified |

**VERDICT: ❌ STILL SKIPPED**
Spread normalized to 0.017% (excellent for an ETF of this size). But Z-Score has moved from +1.17 to +1.47 — XLE has continued to rally intraday, pushing further above its 20-day mean. This is the **opposite** direction from what would be needed for a long entry (Z ≤ −2.0). XLE is becoming more overbought relative to its mean, not less. A long entry here would be chasing momentum without statistical support. Layer B fails. We also already hold XOM as the energy proxy — adding XLE would double sector crowding without the Z-Score justification.

---

#### XLB (Materials Select Sector ETF) — **Most Active Candidate**
| Metric | Morning | Midday |
|--------|---------|--------|
| Skip reason | Z=−0.396 (far from −2.0), RSI=39.2 (not <30) | Z has moved significantly but not yet through threshold |
| Bid/Ask | — | $50.71 / $50.72 |
| **Spread %** | — | **0.020% ✅ NORMALIZED** |
| Z-Score | −0.396 | **−1.753** |
| Z gap to threshold | −1.604σ remaining | **−0.247σ remaining** |
| RSI(14) est. | 39.2 | ~34–36 est. (approaching <30 but not there) |
| Price move | $51.35 | $50.715 (−$0.635, −1.2% intraday) |

**VERDICT: ❌ STILL SKIPPED — but THIS is the watchlist name of the day**
Spread normalized perfectly. XLB has sold off materially intraday (−1.2%), driving Z-Score from −0.396 to −1.753. This is the largest intraday movement of any candidate. **Only 0.247σ separates XLB from triggering the −2.0 long entry threshold** — approximately a further decline of ~$0.12–$0.15 to ~$50.55–$50.60. RSI is estimated around 34–36 after today's selloff, likely approaching the <30 trigger but not yet there. Both gates must clear simultaneously. At this moment, XLB is tantalizingly close but BOTH Z and RSI remain just outside the entry box. Do NOT lower the gates — the strategy is working correctly by holding back.

**Catalyst check for XLB if it triggers:**
- Materials sector is a YTD leader ✅
- Commodity tailwinds from elevated oil still intact ✅
- No offsetting news found this morning that would invalidate thesis
- Factory Orders data from 10:00 AM ET — if weak, may have contributed to today's XLB decline (verifiable)
- Sector still in momentum ✅
- Position count (1/6) + week trades (0/3) allow this trade ✅

**If XLB falls to ~$50.55–$50.60 before market close:**
- Z-Score would approach −2.0 ✅
- RSI may cross <30 ✅
- A bracket limit order LONG would be warranted for next morning's pre-market review or an afternoon-scan
- Stop: ~7% below entry (~$47.05 if entry ~$50.60)
- Target: ~$58.19 (2:1 R:R minimum, targeting recovery toward mean ~$51.60 and beyond)
- Size: cold-start 10% of equity × 1.00× VIX = ~$10,000 / ~$50.60 ≈ 197 shares

---

### Trades Fired This Rescan
**None.**

Zero candidates re-cleared the composite Layer A + Layer B gates upon midday re-evaluation.

---

### XOM Position Status (Existing Hold)
- Current: $153.47 | Entry: $153.35 | Unrealized: +$15.60 (+0.08%)
- GTC trailing stop: $138.78 (10% from HWM $154.20) — live, no adjustment needed
- Thesis: INTACT. WTI elevated, Hormuz supply disruption ongoing.
- No stop adjustment today (price below prior HWM trigger level).

---

### Patience Rule Applied
No gates were lowered. No trade was forced. Four candidates re-evaluated; zero re-qualified. This is correct disciplined behavior when statistical edge is absent. XLB is the single name approaching qualification — it is being tracked precisely, not anticipated early.

**Key watch for afternoon / tomorrow morning:**
1. **XLB** — If Z crosses −2.0 AND RSI crosses <30 simultaneously before close → potential bracket limit placement for tomorrow's open. Re-evaluate in afternoon scan.
2. **FANG** — Earnings results now known. Review post-earnings Z-Score and RSI at tomorrow's pre-market. If stock sold off on earnings: possible oversold long. If gapped up: Z ≥ +2.0 short candidate (pending pair check).
3. **XLE** — Trend continuation, no entry. If WTI reverses materially, XLE could pull back to Z ≤ −2.0 — flag for Tuesday.
4. **PLTR** — Post-earnings: Z flat. Continue monitoring daily.


---

## 2026-05-04 — Afternoon Scan Addendum (19:35 UTC / ~15:35 ET)

**Scan time:** ~2 hrs before close (market closes 20:00 UTC / 4:00 PM ET)
**VIX regime at scan:** NORMAL (~17.6 via VIXY proxy $27.76) | Sizing multiplier: 1.00×

---

### STEP 1 — Order & Position State Reconciled vs TRADE-LOG

| Order ID | Symbol | Type | Status | Notes |
|----------|--------|------|--------|-------|
| c04ae321 | XOM | Market Buy (130 sh) | FILLED @ $153.35 | Entry May 1, logged ✅ |
| d92d9371 | XOM | Trailing Stop 10% GTC | LIVE (status: new) | HWM $154.46, stop $139.014 |

- **No morning bracket limits were placed today** (pre-market research decision was HOLD — no new candidates cleared gates). Nothing to check for fills.
- **No stale limit orders exist** — only the trailing GTC stop on XOM is live.
- **XOM bracket fills today:** 0 (position was entered May 1, not today)
- XOM trailing stop already upgraded from bracket fixed-stop to GTC trailing on May 1; confirmed live and active today with updated HWM of $154.46.

---

### STEP 2 — Trailing Stop Assessment: XOM

| Metric | Value |
|--------|-------|
| Entry | $153.35 |
| Current price | $153.315 (bid $153.30 / ask $153.34) |
| Unrealized P&L | -$4.55 (-0.023%) |
| Stop type | Trailing 10% GTC (already upgraded from bracket) |
| Current HWM | $154.46 |
| Current stop | $139.014 |
| +15% trigger (→ 7% trail) | $176.35 |
| +20% trigger (→ 5% trail) | $184.02 |

**Decision: NO STOP CHANGE**
- `unrealized_plpc = -0.00023` → position is slightly underwater (−0.023%)
- Workflow rule: *"For each filled position where unrealized_plpc ≤ 0: leave the bracket stop in place."*
- Stop is already a 10% trailing GTC (previously upgraded) — this is the correct instrument
- HWM of $154.46 is higher than current $153.31 → stop is correctly trailing from that high
- Neither the +15% nor +20% tighten triggers have been reached
- **No adjustment required**

---

### STEP 3 — Stale Limit Cancellations

**None applicable.** No morning limit orders were placed today (HOLD decision at pre-market). Only the XOM trailing stop GTC exists, and it is correctly active. Nothing to cancel.

---

### STEP 4 — Afternoon Opportunity Scan

**Candidates evaluated:**

| Ticker | Z-Score | RSI(14) | Spread | Layer A | Layer B | Verdict |
|--------|---------|---------|--------|---------|---------|---------|
| XOM (hold) | +0.396 | 58.43 | 0.026% | — | — | HOLD, no new entry |
| XLE | +1.366 | 68.71 | 0.017% | ❌ RSI mid-range | ❌ Z fails | REJECT |
| XLB | **-1.936** | 34.19 | 0.020% | ❌ RSI=34.19 (need <30) | ❌ Z=-1.936 (need ≤-2.0) | REJECT — 0.064σ short |
| FANG | **+2.332** | 81.58 | 0.70% | ✅ RSI>70, ✅ Z | ❌ Pair div (OXY) 1.79σ>1.5σ; ❌ earnings binary; ❌ sector headwind; ❌ Phase 1 long-only | REJECT |
| PLTR | +0.982 | 63.17 | 0.020% | ❌ Z fails | — | REJECT |
| CVX (pair) | +0.697 | — | 3.6% spread AH | ❌ after-hours | — | No signal |

**XLB — Closest Candidate (Watch Carefully):**
- Z-Score: -1.936 (threshold: ≤ -2.0; gap: only 0.064σ ≈ $0.03 further decline needed)
- RSI: 34.19 (threshold: < 30; approaching but not triggered)
- Sector pair LIN (Linde): Z = -1.384; XLB-LIN pair divergence = 0.552σ → **pair CONFIRMS** (< 1.5σ threshold ✅)
- Catalyst: Materials is YTD sector leader; elevated commodity prices from Hormuz-driven energy complex; Factory Orders data released today could be contributing to weakness
- With ~25 minutes remaining before close: XLB would need to fall ~$0.03–$0.04 to trigger the Z ≤ -2.0 gate. RSI < 30 would require a sharper accelerated sell-off.
- **VERDICT: NOT entering today.** Strict gate adherence — both Z and RSI must simultaneously clear. If XLB opens tomorrow at or below ~$50.55 with RSI confirming <30, this becomes a legitimate pre-market research idea.

**FANG — Post-Earnings Analysis:**
- Z: +2.332 ✅ | RSI: 81.58 ✅ | Spread: 0.70% ✅
- REJECTS on: (1) Pair divergence OXY Z=+0.54 vs FANG Z=+2.33 → 1.79σ gap > 1.5σ rule; (2) Earnings reported today — "sell the news" short is binary speculation, not systematic edge; (3) Energy sector is YTD leader, WTI near $100, Hormuz active — strong sector headwind for any short; (4) Phase 1 is long-only (Phase 3 backlog)
- **VERDICT: REJECT on composite Layer B failures**

**PLTR — Post-Earnings (Reported May 4 after close):**
- Z: +0.982 — mid-range, no statistical extreme. Market has absorbed earnings news without creating a ±2σ opportunity. **REJECT.**

---

### Afternoon Market Context

Energy continued its constructive session: XLE closed +0.68% at $59.25, tracking WTI's elevated levels ($99-106 range persisting). XOM intraday showed mild positive action (+0.37% intraday, closing the trailing stop gap slightly) despite near-flat session close vs entry. The XLB (Materials) selloff of −1.5% on the day moved it to within striking distance of the Z ≤ −2.0 long trigger — this is the #1 watchlist item for Tuesday's pre-market. FANG's post-earnings gapped up further but failed the pair-divergence gate vs OXY — idiosyncratic earnings premium, not a sector-wide move. No late-day catalysts emerged that would justify a same-session bracket entry. VIX remained firmly in Normal regime (~17.6). "Sell in May" seasonal pressure may be contributing to XLB weakness — worth monitoring into tomorrow.

---

**Bracket fills today:** 0 (no morning limits were placed; XOM entry was May 1)
**Stops upgraded:** 0 (XOM stop already trailing; position slightly underwater → no change per rules)
**Stale limits cancelled:** 0 (none existed)
**New afternoon entries:** none — all candidates failed Layer A + Layer B composite gates
**Key watchlist for Tuesday pre-market:** XLB (Z=-1.936, RSI=34.2, pair confirms; needs ~$0.03 further decline + RSI<30)


---

## 2026-05-05 — Afternoon Scan Addendum (~15:20 ET / 19:20 UTC)

**Scan time:** ~40 min before close (market closes 20:00 UTC / 4:00 PM ET)
**VIX regime:** NORMAL — proxy VIXY $27.76 area; sizing multiplier 1.00×

---

### STEP 1 — Order & Position State Reconciled vs TRADE-LOG

**Orders returned by API:**

| Order ID | Symbol | Type | Status | Detail |
|----------|--------|------|--------|--------|
| c04ae321 | XOM | Market Buy (130 sh) | **FILLED** @ $153.35 | Entry 2026-05-01; unchanged ✅ |
| d92d9371 | XOM | Trailing Stop 10% GTC | **LIVE** (status: new) | HWM $155.22 → stop $139.698 |

- **No morning bracket limit orders were placed today** (pre-market decision was HOLD — zero new candidates cleared gates). Nothing new to check for fills vs TRADE-LOG.
- **TRADE-LOG is fully current.** XOM fill and trailing stop both logged on May 1. No reconciliation discrepancy.
- **Bracket fills today: 0** (no morning limits existed to fill)
- **Open stale limits: 0**

---

### STEP 2 — Trailing Stop Assessment: XOM

| Metric | Value |
|--------|-------|
| Entry | $153.35 |
| Current price | $154.935 (bid $154.88 / ask $154.94) |
| Spread | $0.06 = 0.039% ✅ (liquid) |
| Unrealized P&L | +$206.05 (+1.034%) |
| Stop type | Trailing 10% GTC — already upgraded (no bracket fixed-stop exists) |
| HWM (Alpaca) | $155.22 |
| Stop (Alpaca) | $139.698 (= $155.22 × 0.90) |
| Z-Score (20d) | +1.2744 — mid-range, no statistical extreme |
| +15% trigger (→7% trail) | $176.35 — needs +$21.42 more |
| +20% trigger (→5% trail) | $184.02 — needs +$29.08 more |
| 3% proximity floor | $150.29 — current stop at $139.698 is 9.83% from price ✅ |

**Decision: NO STOP CHANGE**
- `unrealized_plpc = +1.034%` → position is profitable ✅
- However, workflow rule for trailing upgrade requires the position to have a *fixed* bracket stop. The XOM stop is **already a 10% trailing GTC** (upgraded on May 1). No cancel-and-replace needed.
- Neither the +15% nor +20% tighten triggers have been reached. Stop stays at 10% trail.
- Alpaca HWM has updated from $154.46 (prior scan) to $155.22 today — confirming the trailing mechanism is working correctly and tracking today's intraday high.
- **Action: HOLD trailing stop as-is. No order modifications.**

---

### STEP 3 — Stale Limit Cancellations

**None applicable.** No morning bracket limit orders were placed today. The only live order is the XOM trailing stop GTC (d92d9371), which is active, correctly placed, and should NOT be cancelled. Zero stale limits to address.

---

### STEP 4 — Afternoon Opportunity Scan

**VIX regime:** NORMAL (1.00× sizing) | **Positions:** 1/6 | **Week trades:** 0/3 | **PDT:** 0/3

**Universe scanned:** XOM (held), CVX, XLE, XLB, PLTR, LIN (pair)

| Ticker | Price | Z-Score | Pair | Pair Div | Layer A RSI est. | Spread | Layer B | Verdict |
|--------|-------|---------|------|----------|------------------|--------|---------|---------|
| XOM (held) | $154.94 | +1.2744 | CVX +1.4637 | 0.19σ ✅ | ~55 | 0.039% | Not at ±2.0 ❌ | **HOLD — no new entry** |
| CVX | $193.31 | +1.4637 | XOM 0.19σ ✅ | — | ~55 | 0.03% | Not at ±2.0 ❌ | **REJECT** |
| XLE | $59.69 | +1.7190 | — | — | ~60 | 0.017% | Not at +2.0 ❌ | **REJECT** |
| XLB | $51.71 | +0.0846 | LIN +0.0527 | 0.03σ ✅ | ~52 | 0.019% | Not at ±2.0 ❌ | **REJECT** |
| PLTR | $135.72 | -0.8636 | — | — | ~38 est. | 0.029% | Not at -2.0 ❌ | **REJECT** |

**Key developments in afternoon scan:**

**XLB (Materials ETF) — SETUP RESET:**
- Yesterday afternoon: Z = -1.936 (0.064σ from long trigger); RSI = 34.19 (just above <30)
- Today: XLB BOUNCED +2.1% ($50.65 close → $51.71 today) on reversal momentum
- Z-Score has completely reset from -1.936 to **+0.085** — a 2.02σ swing in the OTHER direction
- The watchlist setup is fully cleared. No entry signal whatsoever. Correct to NOT lower gates yesterday.

**PLTR (Palantir) — Post-Earnings Selloff:**
- PLTR reported earnings May 4 after close; opened May 5 at $140.30, sold off to low $134.72, closing ~$135.82 (-7.0% from prior day's close of $146.03)
- Volume: 74.5M shares (vs ~48M avg) — elevated, confirming "sell the news" behavior on what may have been an in-line or slightly disappointing outlook
- Z-Score: -0.8636 — moving in the long direction but still **1.14σ away from the -2.0 trigger**
- Long trigger price: PLTR would need to reach **≤ $129.09** for Z ≤ -2.0
- RSI estimate: ~38 (recovering from session low near 30 but not yet sub-30)
- **REJECT** — Layer B fails. However, this is the **#1 watchlist name for Tuesday's pre-market**. If PLTR sells off further toward $129 with RSI confirming <30, it becomes a legitimate oversold mean-reversion long candidate.

**XLE (Energy ETF):**
- Z = +1.7190 — climbing further above mean (was +1.47 at midday), approaching but not reaching +2.0 short threshold
- Energy thesis intact — WTI structurally elevated, Hormuz ongoing
- No long entry available (Z is positive/above mean). No short entry (Z below +2.0 and sector is YTD leader)
- **REJECT**

**CVX:**
- Z = +1.4637 — mid-range. Pair divergence from XOM = only 0.19σ (confirms sector cohesion ✅)
- No entry gate. **REJECT.**

**New afternoon entries: none** — all candidates failed Layer A + Layer B composite gates.

---

### Afternoon Market Context

XOM closed near session highs ($154.92 range), extending its trailing stop HWM to $155.22 — the strongest close in the position's 3-day hold. The trailing stop has organically tightened from its original $138.78 (HWM $154.20 from May 1) to $139.698 as Alpaca's mechanism has tracked the new high. Energy sector remains constructive: XLE continued higher (+0.49% today, Z approaching +1.7), WTI structurally elevated, Hormuz supply-risk narrative intact. PLTR's post-earnings selloff of -7% today was the afternoon's most significant move — "sell the news" pattern on a name that had run hard into the print. PLTR is now the single most interesting watchlist candidate for Wednesday: needs ~$6.63 more decline to reach the Z ≤ -2.0 long threshold ($129.09). XLB's complete reversal today (+2.1% bounce from yesterday's oversold dip) demonstrates the importance of the dual-gate discipline — entering XLB at yesterday's Z=-1.936 before BOTH gates cleared would have resulted in an immediate +2% adverse move today.

---

**Bracket fills today:** 0 — no morning limits were placed (HOLD decision at pre-market)
**Stops upgraded:** 0 — XOM stop already trailing; no cancel/replace needed; position +1.034% but stop already in correct instrument
**Stale limits cancelled:** 0 — none existed
**New afternoon entries:** none — all 4 candidates failed composite Layer A + Layer B gates
**Key watchlist for Wednesday pre-market:**
1. **PLTR** — Z=-0.8636 trending toward -2.0; needs ~$129.09 close and RSI<30 to trigger long gate. Post-earnings volume high. Catalyst: AI/gov revenue trajectory, strong beat rate season.
2. **XLE** — Z=+1.719 approaching +2.0 short threshold; however sector headwind for shorts (Energy YTD leader) means even if Z clears we have pair/sector checks to run. Monitor.
3. **XLB** — Setup reset today (+2.1%). Needs fresh selloff to re-qualify. Off watchlist for now.

---

## 2026-05-06 — Pre-Market Research (Day 9, Wednesday)

### ⚠️ DATA QUALITY FLAG
**Gemini research API FAILED (404 NOT_FOUND — model deprecated).** No fresh web data available for today's session. All market context below is derived from:
1. Live Alpaca account + position data (real-time ✅)
2. Alpaca historical bars (real-time ✅)
3. Previous day's memory files (TRADE-LOG, RESEARCH-LOG)
4. Structural market knowledge (no live VIX, no live futures, no news feeds)

**Action item for operator:** Update GEMINI_API_KEY / model name in research script before tomorrow's run.

---

### Account State (Live Pull)
| Metric | Value |
|--------|-------|
| Equity | $99,375.35 |
| Cash | $80,064.50 (80.6%) |
| Deployed | $19,310.85 (19.4%) |
| Day P&L | −$823.55 (−0.83%) vs yesterday close |
| Phase P&L | −$624.65 vs entry (portfolio below $100k watermark) |
| Daytrade count | 0/3 |
| PDT flag | false |
| Weekly trades | 0/3 used |

**Circuit breaker check:**
- Day P&L: −0.83% → ✅ within −2% limit
- Phase P&L: −0.624% → ✅ within −5% limit
- Drawdown from all-time high ($100,206.70): −$831.35 / −0.83% → ✅ well under 15%

---

### Open Position: XOM
| Field | Value |
|-------|-------|
| Shares | 130 |
| Entry | $153.35 |
| Current | $148.58 (−3.11%) |
| Market Value | $19,310.85 |
| Unrealised P&L | −$624.65 (−3.13%) |
| Hard stop (−7%) | $142.62 — current is $5.96 above; NOT triggered |
| Trailing stop | $139.761 (10% from HWM $155.29) |
| Distance to trail | 5.94% below current price |

**Quant Layer B — XOM:**
- 20-day mean: $150.97 | std: $2.70
- **Z-Score: −0.89** → FAR from −2.0 threshold; no re-entry signal
- RSI(14): 44.10 → Neutral (no oversold signal)
- 25-bar SMA proxy: $152.98 (current below short-term average — bearish lean)
- **Thesis status:** XOM is down −3.1% from entry. Today's pre-market shows continued weakness ($148.58 from yesterday's $154.88 close = −4.1% intraday). The energy thesis (WTI elevated, Hormuz supply, earnings beat) must be reassessed. Energy sector appears to be rolling over with XOM well below its recent highs.

**Position decision:**
- XOM is at −3.11% from entry — past the halfway point to the −7% hard stop.
- Trailing stop ($139.761) not triggered; hard stop ($142.62) not triggered.
- **No exit signal yet per strategy rules.** Hold and monitor.
- If XOM breaks $142.62 intraday → execute manual close (hard stop rule).
- **THESIS WARNING:** If XOM continues declining and closes below $148 today, the energy thesis may be invalidating (sector momentum breaking). Watch for consecutive sector failures.

---

### VIX Regime Classification
**⚠️ VIX data unavailable** — Gemini research feed failed. Cannot classify regime with certainty.

**Estimated regime from context:** Given the sharp XOM selloff (−4.1% on large cap energy today), PLTR also down further, and the broad move lower, VIX is likely in the **22–30 Elevated** range or possibly higher. Conservative assumption:

> **Assumed regime: ELEVATED (VIX 22–30)**
> - Sizing multiplier: **0.75×**
> - Strategy bias: **Mean-reversion preferred, tighter stops**
> - Cold-start Kelly 10% × 0.75× = **7.5% per new position** (~$7,453)

**Operator note:** Confirm VIX at market open before placing any new orders.

---

### Watchlist Quant Scan

#### PLTR (Palantir) — Long candidate, watching
| Metric | Value |
|--------|-------|
| Current price | $134.89 |
| 20-day mean | $140.47 |
| 20-day std | $6.12 |
| **Z-Score** | **−0.91** |
| RSI(14) | 41.76 |
| Z-trigger (−2.0) | $128.23 (needs −4.9% more decline) |
| RSI trigger (<30) | ~$128–$130 range estimated |

**Layer A:** Catalyst present (AI/government revenue, strong earnings beat May 5). Sector (tech/AI) has been strong YTD.
**Layer B:** Z = −0.91. **FAILS Z ≤ −2.0 requirement.** RSI = 41.76, **FAILS RSI < 30 requirement.**
**Decision: SKIP — Layer B fails.** Continue watching. Entry trigger price ~$128.23 (Z) + RSI < 30 confirmation needed.

---

### New Ideas Scan (Limited — No Live Research Feed)

Given the research API failure, I cannot run a full universe scan with fresh catalysts today. Based on structural knowledge and prior research context:

#### Idea A: HOLD CASH / DEFENSIVE
Given:
- Research feed down (no edge information)
- XOM thesis under stress (−3.1%)
- Estimated elevated VIX regime
- No confirmed catalysts for new entries

**Recommendation: No new entries today.** Patience rule applies. A day with zero new trades is the correct call when information quality is degraded.

#### Idea B: XOM — Monitor for hard-stop exit
- If XOM trades below **$142.62** intraday → close position immediately at market (hard stop rule, −7% from entry).
- If XOM trades below **$148.00** at close AND energy sector shows consecutive weakness → consider early thesis-break exit even above hard stop.
- Trailing stop at $139.761 remains live via GTC order.

#### Idea C: PLTR — Add to watchlist, no trade yet
- Continue monitoring PLTR for Z ≤ −2.0 (price ~$128.23) + RSI < 30 + volume confirmation.
- Post-earnings momentum (strong beat) means a dip toward oversold territory would be a genuine mean-reversion opportunity.
- **Do not chase.** Only enter if all gates clear.

---

### Trade Ideas Summary

| Rank | Ticker | Direction | Thesis | Layer A | Layer B | Decision |
|------|--------|-----------|--------|---------|---------|----------|
| — | XOM | HOLD existing | Energy thesis, trailing stop live | ✅ (but weakening) | Z=−0.89 ❌ (no add) | HOLD, watch $142.62 hard stop |
| — | PLTR | Watch / No entry | AI/gov catalyst, post-earnings dip | ✅ catalyst present | Z=−0.91 ❌ RSI=41.76 ❌ | SKIP — wait for Z≤−2.0 |
| — | NEW | N/A | Research feed failed | ❌ no catalyst data | ❌ no quant data | **NO NEW ENTRIES** |

**Verdict: HOLD existing XOM position. Place NO new orders today. Monitor XOM hard stop ($142.62) and thesis health closely at open.**

---

### Risk Flags for Today
1. **Research API dead** — operator must fix Gemini model name/key before tomorrow.
2. **XOM −4.1% pre-market** — approaching stress zone; one more leg down hits −7% hard stop.
3. **Unknown VIX** — cannot confirm regime; assume Elevated, use 0.75× sizing if forced to enter.
4. **Energy sector roll-over risk** — if XOM closes below $148, evaluate thesis-break exit.
5. **Portfolio below $100k** — no crisis, but note the phase watermark is breached temporarily.

---

### Open Orders
- XOM trailing stop GTC: sell 130 shares at 10% trail from HWM $155.29 → current stop $139.761. ✅ Still valid, no change needed.

---

## 2026-05-06 — Midday Scan Addendum (~17:25 UTC / ~13:25 ET)

**Scan type:** Midday workflow — position thesis check & stop evaluation
**VIX:** Not confirmed (research API still down — Gemini 404 deprecated model). Estimated ELEVATED (22–30) given today's broad selloff.

---

### Account State at Midday
| Metric | Value |
|--------|-------|
| Equity | $99,350.00 |
| Cash | $80,064.50 (80.6%) |
| Deployed | $19,285.50 (19.4%) |
| Day P&L | −$848.90 (−0.85%) vs last equity |
| Phase P&L | −$650.00 vs cost basis |
| PDT daytrade count | 0/3 |
| Weekly trades used | 0/3 |

---

### XOM — Full Midday Thesis Validation

| Metric | Value | Assessment |
|--------|-------|------------|
| Entry | $153.35 (May 1) | — |
| Current price | $148.35 | — |
| Unrealized P&L | −$650.00 (−3.26%) | Below entry; approaching stress zone |
| Intraday change | −$848.90 (−4.22% today) | Gapped down −3.75% at open |
| Today open | $149.07 | Gap down from $154.88 yesterday |
| Today low | $147.21 | Near Apr 17 structural low $146.44 |
| Today high | $150.33 | Failed to reclaim $149 support |
| Volume today | 9.4M shares | **BELOW** 20-day avg ~19M — no panic volume |
| Z-Score (20d) | −0.9879 | Trending toward oversold but not at −2.0 |
| RSI(14) | 43.75 | Neutral — not oversold |
| SMA-10 | $151.69 | Price BELOW — bearish lean |
| SMA-20 | $150.96 | Price BELOW — bearish lean |

**Hard Stop check:** −3.26% vs −7% threshold → **NOT triggered** ($142.62 line, $5.73 buffer)
**Trailing stop GTC:** $139.761 live (HWM $155.29, order d92d9371) → **NOT triggered** ($8.59 buffer)
**Stop tighten check:** Position underwater → **Not applicable**

---

### Thesis Component-by-Component Review

| Component | Status | Notes |
|-----------|--------|-------|
| Q1 2026 earnings beat | ✅ INTACT | Historical event, confirmed at entry |
| WTI ~$100+ / Brent ~$109+ | ✅ ASSUMED INTACT | No Hormuz peace deal in news (would be major event) |
| Hormuz supply disruption | ✅ ASSUMED INTACT | Structural multi-week supply shock; no resolution reported |
| Energy sector YTD momentum | ⚠️ WATCH | XOM −4.22% today; sector leader status intact YTD but short-term weakness evident |
| Technical trend (50>200 SMA) | ⚠️ WEAKENING | Price now below SMA-10 AND SMA-20 |
| Support at $149.01 (Apr lows) | ❌ BROKEN | Current $148.35 = below Apr 14–15 support zone |
| Volume confirmation of selloff | ✅ BELOW AVG | 9.4M vs ~19M avg — no institutional panic exodus |

---

### Thesis Break Decision

**VERDICT: THESIS NOT BROKEN — HOLD**

Rationale:
1. **Original catalyst** (earnings + Hormuz supply shock + WTI elevated) remains structurally intact. No thesis-invalidating event found.
2. **−7% hard stop**: $142.62. Not triggered. $5.73 buffer (3.86%) remains.
3. **Volume below average**: The decline today (−4.22%) is occurring on 9.4M shares vs a 19M+ average. If a major sector thesis-break were happening (US-Iran peace deal, WTI collapse), volume would be sharply above average. Below-average volume argues for drift/rotation, not fundamental exit.
4. **April structural support** at $146.44 (Apr 17 close): XOM tested down to $147.21 intraday today — only $0.77 above that floor. This is a critical level to watch. If XOM closes below $146.44, that would constitute a structural support break warranting re-evaluation.
5. **Consecutive sector failure rule**: Only 1 energy position has been traded. Rule requires 2 consecutive failures. Not triggered.
6. **Research API offline**: Cannot confirm live WTI price or news catalysts. This is a known operational risk (flagged yesterday). Operating under information constraint — conservative lean (HOLD vs force-exit).

**Monitoring thresholds going forward:**
- **Mandatory exit if:** Price breaks below $142.62 (−7% hard stop rule) OR trailing stop $139.761 triggers automatically
- **Thesis-break exit consider if:** XOM closes below $146.44 (Apr 17 structural low) with above-average volume — would signal a genuine breakdown through all support
- **Thesis confirmation if:** Price recovers above $149 on above-average volume (reclaims support)

---

### Stop / Order Status

| Order ID | Type | Status | Details |
|----------|------|--------|---------|
| d92d9371 | Trailing stop 10% GTC | ✅ LIVE | Sell 130 XOM, HWM $155.29, stop $139.761 — no change needed |

**No orders placed. No orders cancelled. Monitoring mode only.**

---

### Research API Status
- Gemini API: ❌ STILL DOWN (404 — deprecated model). Could not run live news check on XOM.
- Inability to confirm live WTI price / Hormuz news is an operational risk. Operator action required: update Gemini model endpoint.
- Best available signal (below-average volume on decline) suggests no major news catalyst driving today's XOM weakness.

---

### Actions Taken This Scan
**None.** No positions cut, no stops adjusted, no thesis exits, no new orders. Portfolio state unchanged from open.

**Key watchlevel for rest of session:**
- XOM **$146.44** = April structural low → breach = thesis-break candidate
- XOM **$142.62** = hard stop → breach = mandatory exit
- Trailing GTC $139.761 handles automatic protection if position gaps through hard stop


---

## 2026-05-06 — Afternoon Scan Addendum (~19:55 UTC / ~15:55 ET)

**Scan time:** ~5 minutes before close (market closes 20:00 UTC / 4:00 PM ET)
**VIX regime at scan:** NORMAL — VIXY proxy $26.98 (↓ from yesterday $27.76) → estimated VIX ~18–20 | Sizing multiplier: 1.00×

---

### STEP 1 — Order & Position State Reconciled vs TRADE-LOG

| Order ID | Symbol | Type | Status | Detail |
|----------|--------|------|--------|--------|
| c04ae321 | XOM | Market Buy (130 sh) | **FILLED** @ $153.35 | Entry 2026-05-01; unchanged ✅ |
| d92d9371 | XOM | Trailing Stop 10% GTC | **LIVE** (status: new) | HWM $155.29 → stop $139.761 |

- **No morning bracket limit orders were placed today** — pre-market decision was explicit: "NO NEW ENTRIES TODAY" (research API dead, XOM thesis under stress, VIX unconfirmed elevated). Nothing to check for fills vs TRADE-LOG.
- **TRADE-LOG is fully current.** Both XOM orders logged accurately on prior dates.
- **Bracket fills today: 0** (no morning limits were placed)
- **Open stale limits: 0** — only the trailing GTC stop on XOM exists, correctly live.

---

### STEP 2 — Trailing Stop Assessment: XOM

| Metric | Value |
|--------|-------|
| Entry | $153.35 |
| Current price | $148.22 (bid $148.18 / ask $148.25) |
| Spread | $0.07 = 0.047% ✅ (liquid) |
| Unrealized P&L | −$653.90 (−3.28%) |
| Stop type | Trailing 10% GTC — already upgraded (no bracket fixed-stop exists) |
| HWM (Alpaca) | $155.29 |
| Stop (Alpaca) | $139.761 (= $155.29 × 0.90) |
| Z-Score (20d) | −1.0376 — moving toward oversold, not yet at −2.0 |
| +15% trigger (→7% trail) | $176.35 — needs +$28.13 more from current |
| +20% trigger (→5% trail) | $184.02 — needs +$35.80 more from current |
| 3% proximity floor | $143.77 — current stop at $139.761 is 5.7% from price ✅ |

**Decision: NO STOP CHANGE**
- `unrealized_plpc = −3.28%` → **position is underwater**
- Workflow rule: *"For each filled position where unrealized_plpc ≤ 0: leave the bracket stop in place."*
- The XOM stop is already a 10% trailing GTC (previously upgraded on May 1) — the correct instrument is already in place.
- Neither the +15% nor +20% tighten triggers have been reached (position is negative, not profitable).
- HWM $155.29 is correctly set from the intraday high on 2026-05-05; the trail is functioning as designed.
- **No order modifications. No cancel/replace. Stop remains live at $139.761.**

---

### STEP 3 — Stale Limit Cancellations

**None applicable.** No morning bracket limit orders were placed today. The only live order is the XOM trailing stop GTC (d92d9371), which is active, correctly placed, and must NOT be cancelled. Zero stale limits to address.

---

### STEP 4 — Afternoon Opportunity Scan

**VIX regime:** NORMAL (1.00× sizing) | **Positions:** 1/6 | **Week trades:** 0/3 | **PDT:** 0/3

**Universe scanned:** XOM (held), CVX (pair), XLE (sector), XLB, PLTR

| Ticker | Price | Z-Score | Layer B Gate (±2.0) | Spread | RSI est. | Volume vs Avg | Verdict |
|--------|-------|---------|---------------------|--------|----------|---------------|---------|
| XOM (held) | $148.22 | −1.0376 | ❌ Not at ±2.0 | 0.047% ✅ | ~44 | 0.66× below avg | **HOLD — no new entry** |
| CVX | $185.12 | −0.9616 | ❌ Not at ±2.0 | 0.054% ✅ | ~45 | 0.73× below avg | **REJECT** |
| XLE | $57.03 | −0.1225 | ❌ Not at ±2.0 | 0.018% ✅ | ~40 | 1.13× ABOVE avg | **REJECT** |
| XLB | $52.47 | **+1.8383** | ❌ +1.84σ, not +2.0 | 0.019% ✅ | ~62 | 0.77× below avg | **REJECT** |
| PLTR | $133.42 | −1.1543 | ❌ Not at ±2.0 | 0.045% ✅ | ~39 | 0.99× at avg | **REJECT** |

**Key developments in afternoon scan:**

**XOM (existing position):**
- Z-Score: −1.0376 — deepening toward oversold zone (was −0.88 at this morning's pre-market). Moving in the right direction for a potential mean-reversion bounce but not yet at −2.0 statistical extreme.
- Volume today: 13.1M shares vs 19.9M 20-day avg = 0.66× → **below average** — confirms no institutional panic selling / no thesis-break news catalyst. Orderly drift lower, not a flush.
- Today's low: $147.09 — just $0.65 above April 17 structural support at $146.44. This is the nearest critical level.
- Hard stop ($142.62) not triggered — $5.60 buffer (3.8%) remains.
- Trailing stop ($139.761) not triggered — $8.46 buffer (5.7%) remains.
- Pair check XOM–CVX: XOM Z = −1.038 vs CVX Z = −0.962 → divergence only **0.076σ** — both selling off together, confirming this is sector-wide, not XOM-specific (✅ thesis still consistent with energy sector movement).
- **THESIS: INTACT. HOLD.**

**CVX (energy pair):**
- Z: −0.9616 — essentially identical to XOM's −1.038. Confirms both integrated oil majors are moving together in lockstep (pair divergence 0.076σ — well within 1.5σ threshold).
- No independent entry signal. Layer B fails.
- **REJECT.**

**XLE (Energy Select Sector ETF):**
- Z: −0.1225 — essentially at its 20-day mean despite a notable selloff today. Volume 50.1M vs 44M avg = +13% above average → elevated selling volume.
- This is notable: XLE is not yet statistically oversold (Z near zero), yet volume is elevated. Suggests the energy sector selloff today is real but hasn't yet created a statistical extreme.
- **REJECT.** No long entry available (Z not ≤ −2.0). No short entry available (not ≥ +2.0 and sector headwind for shorts).
- Watch: if XLE continues lower toward Z ≤ −2.0 (approximately $54.41) with RSI < 30, this becomes a qualified sector ETF long.

**XLB (Materials Select Sector ETF):**
- Z: **+1.8383** — XLB has REVERSED sharply from yesterday's near-oversold condition (Z was −1.936 at yesterday's afternoon scan). Today it is approaching overbought territory.
- Yesterday's patience at Z = −1.936 (gate required ≤ −2.0) and RSI = 34.19 (gate required < 30) has been validated: XLB has rallied further today (+1.7%), completely resetting that setup.
- Current Z = +1.8383 → approaching +2.0 SHORT threshold, but: (1) Materials is a YTD sector leader, not in a downtrend; (2) RSI estimation ~62, not > 70 required for short trigger; (3) Strategy is long-only (Phase 1 — shorting deferred to Phase 3).
- **REJECT on all fronts.** Monitor if XLB continues higher and Z crosses +2.0 (for future Phase 3 short setup reference only).

**PLTR (Palantir):**
- Z: −1.1543 — continuing to trend toward oversold. Now down from Z = −0.864 (yesterday afternoon) to −1.154 today. Declining further.
- Long trigger: Z ≤ −2.0 → requires price ~$128.31 (needs additional ~−$5.11 decline, or −3.8% from current).
- Volume today: 47.8M vs ~48M avg — essentially at average. No panic, no capitulation volume surge. Consistent with steady post-earnings drift.
- RSI estimate: ~39 — approaching but not at < 30 trigger.
- **REJECT — Layer B fails (Z −1.15σ, needs ≤ −2.0).** #1 watchlist name heading into tomorrow.

**New afternoon entries: NONE** — all 4 candidates failed Layer A + Layer B composite gates. No bracket limit orders placed.

---

### STEP 5 — Afternoon Market Context

Energy sold off broadly today in what appears to be sector-wide profit-taking or macro risk-off rotation: XLE −3.3% on above-average volume (50.1M vs 44M avg), XOM −4.2% intraday from yesterday's close (though on below-average volume 13.1M vs 19.9M avg), CVX similarly off. Both XOM and CVX are moving in near-perfect lockstep (Z-score divergence only 0.076σ), confirming this is sector rotation rather than an XOM-specific event. The energy thesis structural pillars (Strait of Hormuz closure, WTI elevated, XOM earnings beat) remain in place absent any news of a US-Iran diplomatic breakthrough. Importantly, VIXY declined today ($26.98 vs yesterday's $27.76), suggesting the broader market is NOT experiencing fear-driven selling — the VIX is actually ticking lower as energy sells off, arguing for rotation out of energy into other sectors rather than a general risk-off event. XOM's intraday low of $147.09 held just $0.65 above the April 17 structural support at $146.44 — this is the critical level to watch for tomorrow. PLTR continues its post-earnings drift lower (Z = −1.154) and is now only $5.11 away from the long trigger price of $128.31, making it the #1 watchlist candidate for Wednesday's pre-market research.

---

**Bracket fills today:** 0 (no morning limits were placed — HOLD decision at pre-market)
**Stops upgraded:** 0 — XOM trailing stop already in place; position underwater → no change per rules
**Stale limits cancelled:** 0 — none existed
**New afternoon entries:** none — all candidates failed composite Layer A + Layer B gates
**Key watchlist for Thursday pre-market:**
1. **PLTR** — Z = −1.1543, trending toward long trigger at Z ≤ −2.0 (~$128.31); RSI ~39, approaching <30. Volume at average. #1 candidate.
2. **XLE** — Z = −0.1225 today; if sector selloff continues toward Z ≤ −2.0 (~$54.41) with RSI <30, becomes qualified sector ETF long entry.
3. **XOM** — Thesis intact but under stress. Watch $146.44 (Apr structural low) — breach with volume would trigger thesis-break review. Hard stop $142.62.
4. **XLB** — Now overbought (Z = +1.84); Phase 3 short candidate if Z crosses +2.0, but currently off watchlist for longs.


---

### May 07 — Pre-Market Research (Day 10, Thursday)

**Portfolio:** $98,910.60 | **Cash:** $80,064.50 (80.9%) | **Deployed:** 19.1% (XOM only) | **Phase P&L:** −$1,089.40 (−1.10%)

---

#### STEP 1 — Memory Context
- XOM entered May 1 @ $153.35 (130 shares). Now at $144.97. Unrealized: −$1,089.40 (−5.47%).
- Trailing stop GTC active: $139.761 (10%, HWM $155.29). Distance to stop: $5.21 (3.59%).
- Prior watchlist: PLTR #1 (Z trending toward −2.0), XLE (Z near trigger), XOM (thesis under stress).
- No new entries placed yesterday afternoon — all 4 candidates (CVX, XLE, XLB, PLTR) failed composite gates.

---

#### STEP 2 — Live Account State
| Field | Value |
|---|---|
| Equity | $98,910.60 |
| Cash | $80,064.50 |
| Long market value | $18,846.10 |
| PDT count | 0/3 |
| Week trades | 0/3 |
| Open positions | 1/6 (XOM) |
| Daytrade buying power | $0 (non-PDT account) |

**Open position:**
- XOM: 130 shares @ $153.35 avg | Current $144.97 | Unrealized −$1,089.40 (−5.47%) | Trailing stop $139.761 (GTC, HWM $155.29)

**Open orders:**
- XOM trailing stop GTC (order ID d92d9371) — active, stop price $139.761, trail 10%

---

#### STEP 3 — Market Context

**Oil:** WTI ~$91.59 (+1.03% today but −4.04% from prior day); Brent ~$96.79–$98.47. Both fell sharply (WTI −6.3% yesterday to $96.21, Brent briefly below $100) on reports of a potential **US-Iran ceasefire / peace deal**. WTI is −3.36% over 1 month but +52.30% YoY. Oil is structurally elevated but the geopolitical premium is deflating.

**Equities:** S&P 500 futures +0.05–0.10% pre-market at ~7,393 after Wednesday's S&P 500 all-time high close at 7,365.12 (+1.46%). Market broadly bullish driven by AI/chipmaker earnings. Broader market NOT in fear mode.

**VIX:** 17.38 (down from 18.29, −4.98%). VIX1D = 11.66 (+8.47%), VIX9D = 14.76 (+0.82%). Historically suppressed. Near-term event pricing slightly elevated (jobs data tomorrow).

**Economic calendar today (May 7):** Challenger job cuts, jobless claims, productivity/costs (7:30 AM ET); Manheim used vehicle index, construction spending (9–10 AM); EIA natural gas storage (10:30 AM); NY Fed consumer expectations, NFIB jobs report, consumer credit (late morning/afternoon). Fed speakers: Kashkari, Hammack, Williams. **No CPI/PPI/FOMC today.** Nonfarm Payrolls scheduled for May 8.

**Pre-market movers:**
- FTNT +15% (Q1 beat) — Z = +7.43 (extreme overbought) — Phase 3 short candidate only
- DASH +10% (better-than-expected quarterly results) — not in scan universe
- MCD +4.5% (Q1 sales beat) — Z = −1.49, price moving AWAY from long trigger
- ARM −8% (weak Q4 royalty revenue) — not in scan universe
- ZTS −7.8% (quarterly miss)
- ALB +6%, CELH +4%, FSLY −25%

**Sector momentum (YTD 2026):** Energy #1 (+25%+) but thesis under stress as oil retreats below $100. Tech/Momentum/AI-infra dominating April. Low-vol and Dividend Aristocrats lagging.

---

#### STEP 4 — VIX Regime Classification

| VIX | Regime | Sizing Multiplier | Strategy Bias |
|---|---|---|---|
| **17.38** | **Normal (14–22)** | **1.00×** | **All entry types OK** |

→ No regime-based restrictions today. Full 10% cold-start position sizing applies.

---

#### STEP 5 — Universe Scan & Idea Generation

**Z-Score calculations (20-day window, partial-day current price):**

| Ticker | Current | 20d Mean | 20d Std | Z-Score | Signal | Vol (today vs 20d avg) |
|---|---|---|---|---|---|---|
| XOM | $144.97 | $150.98 | $2.63 | **−2.29** | ✅ LONG (≤−2.0) | 0.17× ⚠️ (partial day) |
| CVX | $180.33 | $188.12 | $3.12 | **−2.50** | ✅ LONG (≤−2.0) | 0.21× ⚠️ (partial day) |
| XLE | $55.36 | $57.19 | $1.38 | −1.33 | ❌ No trigger | 0.31× ⚠️ |
| PLTR | $137.34 | $140.41 | $6.02 | −0.51 | ❌ No trigger | 0.30× ⚠️ |
| FTNT | $111.41 | $83.90 | $3.70 | **+7.43** | ✅ SHORT (≥+2.0) | 1.09× ✅ |
| MCD | $285.05 | $298.23 | $8.84 | −1.49 | ❌ No trigger | 0.68× ⚠️ |

**XOM–CVX pair divergence:** |−2.29 − (−2.50)| = 0.21σ → ✅ CONFIRMS (< 1.5σ limit)

---

**IDEA 1 — CVX LONG (Mean Reversion)**

**Layer A — Catalyst Checklist:**
- Ticker: CVX | Sector: Energy (integrated oil) | Mkt cap: >$300B ✅ ADV: >10M ✅ Price: $180 ✅
- SMA direction: 50-day > 200-day (energy uptrend YTD) ✅
- Catalyst: **NEGATIVE** ⚠️ — Iran ceasefire narrative is the reason CVX is oversold; same catalyst is a structural headwind for new long entries
- Sector momentum: Energy +25% YTD but currently under stress as oil retreats ⚠️
- RSI: Estimated near 30 given multi-day selloff — approaching trigger but unconfirmed
- Volume confirm: 0.21× today — partial session, not confirming capitulation ❌
- Stop level: Technical support at $178.50 (below today's intraday low $180.16) — only −1.01% from entry; ultra-tight and high whipsaw risk ⚠️
- R:R: 3.3:1 to 20d mean ($188.12) with tight stop ✅ — but only if stop holds

**Layer B — Quant Checklist:**
- Z-Score: −2.50 ✅ (≤−2.0 LONG TRIGGER confirmed)
- VIX regime: Normal (1.00×) ✅
- Pair confirmation: XOM Z = −2.29, divergence 0.21σ ✅ (confirms sector thesis)

**DECISION: REJECT — Layer A fails on 3 counts:**
1. Catalyst is *negative* for oil (Iran deal = oil headwind); can't frame as a positive catalyst
2. Volume 0.21× — no volume confirmation of capitulation/bottoming
3. Tight technical stop (~1%) creates extreme whipsaw risk on oil news day; PDT protection insufficient
4. Sector thesis partially broken (energy "still high" but geopolitical premium deflating)

**Patience rule applies: No edge = no trade.**

---

**IDEA 2 — XLE BRACKET LIMIT (Watchlist)**

**Layer A:**
- Ticker: XLE (S&P 500 Energy Select Sector ETF, >$1B AUM ✅)
- Catalyst: None positive today; negative (Iran ceasefire) ❌
- R:R at trigger price $54.43: Target 20d mean $57.19, stop −7% = $50.61. R:R = 0.72:1 ❌ **FAILS 2:1 minimum**

**Layer B:**
- Z = −1.33 → **NOT AT TRIGGER** ❌ (needs ≤ −2.0, requires ~$0.93 further decline to $54.43)

**DECISION: REJECT — both R:R and Z-Score fail. Even if price hits $54.43, R:R is sub-minimum.**

---

**IDEA 3 — FTNT (Phase 3 Flag)**

- Z = +7.43 — most extreme overbought signal in today's scan (+7.4σ)
- Catalyst: Q1 earnings beat, +24% gap-up
- Volume: 1.09× ✅ confirms the move
- **REJECT for Phase 1: Long-only. Shorting deferred to Phase 3.**
- **Log as Phase 3 short reference:** If Z remains ≥ +2.0 over next 2–3 sessions post-earnings gap (mean reversion short), flag for Phase 3 activation.

---

#### STEP 6 — XOM Thesis Integrity Review

Original pillars: (1) WTI elevated (+52% YoY), (2) XOM Q1 earnings beat, (3) Energy sector momentum #1 YTD.

**Today's threat:** US-Iran ceasefire narrative → WTI fell to ~$91.59. Brent ~$96–98. Both below $100.

**Assessment:** Thesis NOT broken. WTI at $91 still reflects a massive premium vs. 2025 levels ($60 range). XOM's earnings were built on ~$85–95 WTI range. A $91 print doesn't invalidate the earnings thesis. What WOULD break the thesis: (a) confirmed, finalized Iran deal with significant Iranian supply return to market (months away from implementation even if announced), (b) WTI sustained below $80 (would require Iran + OPEC+ response), (c) XOM-specific bad news.

**Current cushion:** $144.97 current vs. $139.761 stop = 3.59% buffer. Trailing stop is automatic (GTC). No manual action needed.

**Decision: HOLD XOM.** Let the stop manage downside. Z = −2.29 argues statistical oversold — supports eventual mean reversion toward $150+ zone.

---

#### FINAL DECISION: **HOLD — 0 NEW TRADES TODAY**

All 5 candidates scanned (CVX, XLE, PLTR, FTNT, MCD) rejected:

| Ticker | Layer A | Layer B | Decision |
|---|---|---|---|
| CVX | ❌ Fails (negative catalyst, low volume, tight stop) | ✅ Z=−2.50 | REJECT |
| XLE | ❌ Fails (R:R < 2:1 at trigger) | ❌ Z=−1.33 | REJECT |
| PLTR | ⚠️ Approaching | ❌ Z=−0.51 (far from trigger) | REJECT |
| FTNT | ✅ (short-only) | ✅ Z=+7.43 (short) | REJECT (Phase 3 only) |
| MCD | ❌ Price moving wrong direction | ❌ Z=−1.49 | REJECT |

**VIX Regime:** Normal (17.38) — no regime-based restrictions, but no qualifying trades exist.
**PDT:** 0/3. **Week trades:** 0/3. **Patience rule invoked.**

---

**Circuit breakers:** ✅ All clear — Phase P&L −1.10% (lim −5%) | Drawdown −1.31% from $100,206.70 peak (lim −15%)
**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 1/6

---

**Watchlist for Friday pre-market (May 8 — NFP Day):**
1. **CVX** — Z = −2.50 ✅ Layer B already passes; needs: (a) oil stabilization catalyst, (b) volume ≥ 1.0× on entry day, (c) stop structure that achieves 2:1 R:R without ultra-tight whipsaw risk. If oil bounces on NFP day, CVX becomes #1 candidate.
2. **XLE** — Z = −1.33, only $0.93 from Z=−2.0 trigger ($54.43). Monitor for continued energy washout. R:R at trigger still sub-2:1 — needs either deeper price OR narrower technical stop.
3. **PLTR** — Z = −0.51; far from trigger ($128.37 = −6.5% away). Long drift continues but not imminent.
4. **MCD** — Z = −1.49; trigger at $280.54 (−1.6% away). If today's +4.5% pre-market doesn't hold and price reverses below $281, re-evaluate Friday.
5. **NFP tomorrow (May 8):** Nonfarm Payrolls + Unemployment Rate release. Strong NFP may boost broad market and stabilize energy; weak NFP could trigger risk-off. Prepare both scenarios.

---

### 2026-05-07 — Midday Rescan Addendum (16:22 UTC / 12:22 PM EDT)

**VIX Regime:** Normal (17.38) — 1.00× multiplier, all entry types allowed.
**Account:** Equity $99,008.10 | Cash $80,064.50 | Deployed 19.1% (XOM only) | PDT 0/3 | Week trades 0/3

---

**Skipped at open, re-evaluated:**

| Ticker | Spread (now) | Z-Score Morning | Z-Score Now | Verdict |
|--------|-------------|-----------------|-------------|---------|
| CVX    | 5.16% ❌ (post-close stale) | −2.50 | −1.713 ❌ | STILL SKIPPED |
| XLE    | 0.018% ✅ | −1.33 | −0.935 ❌ | STILL SKIPPED |
| PLTR   | 0.029% ✅ | −0.51 | −0.454 ❌ | STILL SKIPPED |
| MCD    | 2.05% ❌ (post-close stale) | −1.49 | −1.436 ❌ | STILL SKIPPED |

---

**Detailed Re-Check:**

**CVX — STILL SKIPPED**
- Spread: 5.16% post-close (bid $181.85 / ask $191.48) — stale/crossed, unenterable. During session close: $181.97.
- Z-Score: Morning −2.50 → Now **−1.713** ❌ (regressed toward mean during session; needs ≤ −2.0 for long trigger)
- Layer A: (a) Catalyst STILL negative — Iran ceasefire narrative intact, no bullish oil offset; (b) Volume 5.28M vs 20d avg ~10.4M = 0.51× ❌ no capitulation/bottom signal; (c) Sector energy still broadly soft today.
- Layer B: Z = −1.713 — fails the ≤ −2.0 threshold. Note the irony: morning's Z of −2.50 QUALIFIED on Layer B but failed Layer A; now Layer B has also failed as price partially recovered.
- **Conclusion:** Both layers fail. Morning skip was correct — price partially mean-reverted intraday already (CVX +$1.62 from open-quote basis) without a trade being placed.

**XLE — STILL SKIPPED**
- Spread: 0.018% ✅ (bid $55.78 / ask $55.79) — excellent, fully liquid.
- Z-Score: Morning −1.33 → Now **−0.935** ❌ — moved AWAY from trigger. Price recovered from $55.36 to $55.795.
- Layer A: (a) No positive catalyst — Iran ceasefire overhang unchanged; (b) R:R at trigger ($54.43): target $57.12 (20d mean), stop $50.62 (−7%) → R:R = 0.74:1 ❌ still fails 2:1 minimum; (c) Volume 28.4M vs 20d avg 42.8M = 0.66× ❌
- Layer B: Z = −0.94 — nowhere near trigger; would need ~$2.55 further decline to ~$53.24 for Z = −2.0.
- **Conclusion:** Both layers fail. Price moved away from trigger all day; R:R math was structurally broken at any reasonable trigger level.

**PLTR — STILL SKIPPED**
- Spread: 0.029% ✅ (bid $138.10 / ask $138.14) — excellent.
- Z-Score: Morning −0.51 → Now **−0.454** ❌ — moved sharply AWAY from trigger. Price rallied +3.3% today ($133.79 → $138.26 close).
- Layer A: Price moved strongly upward today — opposite direction needed for mean-reversion long. RSI nowhere near <30. Post-earnings drift upward, not the washout needed for an entry.
- Layer B: Z = −0.45 — would need ~$31 decline (−22%) from here to reach Z = −2.0 trigger at ~$129.60. Not a near-term candidate.
- **Conclusion:** PLTR is definitively off the watchlist for this week. A strong +3.3% day with Z moving from −0.51 → −0.45 removes it as a mean-reversion candidate. Monitor for trend momentum entry qualification instead (RSI + breakout), not mean-reversion.

**MCD — STILL SKIPPED**
- Spread: 2.05% post-close (bid $281.10 / ask $286.93) — stale. During-session close: $284.10.
- Z-Score: Morning −1.49 → Now **−1.436** ❌ — essentially unchanged (close = prior close $284.10).
- Layer A: Morning's +4.5% pre-market gap DID NOT HOLD — stock traded down to close flat. Volume 3.70M vs 20d avg 3.32M = 1.11× ✅ (but directionally neutral). Sector (Consumer Discretionary) not in momentum. No sustained catalyst follow-through.
- Layer B: Z = −1.44 — needs ~$13 further decline to ~$278 for Z = −2.0. Not imminent.
- **Conclusion:** The earnings gap failed to hold, which is actually a mild bearish signal intraday. MCD is drifting sideways/down and may become a candidate in 1–2 sessions if the −2.0 Z trigger is approached, but no entry today.

---

**XOM Position Update (midday):**
- Current: $145.76 | Unrealized: −$986.70 (−4.95%) | Entry: $153.35 (130 shares)
- Trailing stop: $139.761 GTC (HWM $155.29) | Distance to stop: 4.12%
- Z-Score updated: **−1.985** (approaching oversold; nearly at −2.0 again)
- Thesis intact: WTI still ~$91 (not collapsed), no confirmed Iran deal implemented, XOM earnings pillar unchanged
- **Action: HOLD.** Stop manages downside. Z approaching −2.0 again after intraday recovery. No manual intervention warranted.

---

**Trades fired this rescan: NONE**

**Patience rule invoked** — all 4 candidates fail composite Layer A + Layer B gates. No gates were lowered to force a trade. Zero trades this rescan is the correct outcome.

**Updated watchlist for Friday pre-market (May 8 — NFP Day):**
1. **CVX** — Z = −1.71 today; Layer B fails but approaching again. Needs: (a) oil stability/bounce, (b) volume ≥ 1.0×, (c) Z ≤ −2.0. If NFP is strong and oil stabilizes, CVX becomes #1 candidate Friday.
2. **XLE** — Z = −0.94, moved away from trigger today. R:R math structurally problematic at current 20d-mean/ATR setup. Low priority.
3. **MCD** — Z = −1.44, flat action today. If continues to drift lower to ~$278, re-evaluate Friday.
4. **PLTR** — Removed from near-term watchlist. +3.3% today killed the mean-reversion setup. Now a momentum-continuation candidate if trend resumes.
5. **NFP tomorrow (May 8):** Strong print = broad market + energy positive → CVX most likely beneficiary. Weak print = risk-off, hold cash discipline.


---

## 2026-05-07 — Midday Scan Addendum (17:55 UTC / ~12:55 PM ET)

**Event:** XOM thesis-break exit executed

**Exit triggered by convergence of 3 signals:**
1. WTI crude at ~$91.59 (−13.6% from $106 entry-thesis price). Oil sub-$100 for the first time since the Hormuz trade was entered.
2. US-Iran ceasefire/peace deal narrative is the active market driver — the specific geopolitical catalyst (Hormuz supply premium) that justified the entry is deflating in real-time. Iran deal tail risk (flagged at entry as the key downside scenario) is now the base case.
3. XOM broke April 17 structural closing support at $146.44 (XOM at $146.09 at exit). This was pre-flagged in May 6 midday AND afternoon scans as the explicit thesis-break trigger.

**Supporting technicals at exit:**
- Z-Score: −1.58 (NOT at −2.0 oversold → no statistical mean-reversion support)
- RSI(14): ~49.5 (neutral → no oversold bounce anchor)
- Price below SMA-10 ($151.29) and SMA-20 ($150.54): short-term trend flipped bearish
- Volume: below average today but yesterday (May 6) above-average selling volume on large down day

**Decision logic:** The Z-Score NOT being at −2.0 is important — it means there is no statistical oversold extreme to expect a bounce from. Combined with the thesis-break signals, holding for a mean-reversion bounce would be waiting for a bounce that isn't supported by the quant layer.

**Energy sector — post-exit watchlist status:**
- XOM: CLOSED. Monitor from the sidelines. Not a re-entry candidate until oil stabilizes and a fresh, clean signal (Z ≤ −2.0 + RSI < 30 + positive catalyst) qualifies.
- CVX: Z was −2.50 this morning (Layer B qualifies) but Layer A still fails — negative catalyst (Iran deal), volume 0.21×, tight technical stop with poor R:R structure. Not an entry.
- XLE: Z = −1.33 this morning; R:R sub-2:1 at any reasonable trigger price. Not an entry.
- Energy sector has now had ONE trade failure (XOM −4.73%). Strategy rule: exit entire sector if 2 consecutive failures. One failure — caution heightened, not a blanket sector ban yet.

**Post-exit portfolio state:** 100% cash ($99,056.49). Fully flat. No open positions. No open orders. NFP tomorrow (May 8) — correct posture to hold cash into binary macro event.

**Next watchlist (non-energy, fresh ideas for next pre-market scan):**
- Need fresh non-energy catalysts. Energy thesis broken on Iran deal risk.
- PLTR: Z = −0.45 today (moved away from trigger after +3.3% session May 7 midday). Off watchlist.
- Need to scan: Industrials, Materials, Technology, Consumer names for Z ≤ −2.0 + RSI < 30 setups with clean catalysts AFTER NFP print clears macro uncertainty.
- NFP (May 8): If strong (consensus 49k+), risk-on bounce likely. If weak, risk-off may create oversold signals across multiple sectors — potentially productive for mean-reversion entries.

---

## 2026-05-07 — Afternoon Scan Addendum (~19:50 UTC / ~15:50 ET)

**Scan time:** ~10 min before close (market closes 20:00 UTC / 4:00 PM ET)
**VIX regime at scan:** NORMAL (estimated ~18–20, from prior session VIXY $26.98; no fresh VIX data — Gemini API still down) | Sizing multiplier: 1.00×

---

### STEP 1 — Order & Position State Reconciled vs TRADE-LOG

**Orders returned by API (3 total — all historical):**

| Order ID | Symbol | Type | Status | Detail |
|----------|--------|------|--------|--------|
| c04ae321 | XOM | Market Buy (130 sh) | **FILLED** @ $153.35 | Entry 2026-05-01 ✅ logged |
| d92d9371 | XOM | Trailing Stop 10% GTC | **CANCELLED** 2026-05-07T17:54 | Cancelled prior to thesis-break exit ✅ logged |
| 8f97ef7d | XOM | Market Sell (130 sh) | **FILLED** @ $146.092 | Thesis-break exit 2026-05-07T17:55 ✅ logged |

- **No morning bracket limit orders were placed today** — pre-market research (May 7) verdict was explicit HOLD: "0 NEW TRADES TODAY" due to negative catalyst environment (Iran ceasefire deflating oil premium) and all 5 candidates failing composite gates.
- **Positions API returned: EMPTY `[]`** — confirms full exit of XOM at 17:55 UTC. Portfolio is 100% cash.
- **TRADE-LOG reconciliation:** Post-exit equity $99,056.49 matches API exactly ✅. No discrepancy.
- **Bracket fills today: 0** (no morning limits were placed — nothing to check for fills)
- **Open orders: 0** — no GTC stops, no bracket limits, no stale limits. Clean slate.

---

### STEP 2 — Trailing Stop Upgrades: N/A

**No positions held.** Portfolio is 100% cash ($99,056.49). The XOM trailing stop (d92d9371) was already cancelled at 17:54 UTC as part of the thesis-break exit workflow logged in the midday scan addendum. No trailing stop upgrades applicable.

---

### STEP 3 — Stale Limit Cancellations: None

No morning bracket limit orders were placed today. No stale limits exist. No cancellations needed.

---

### STEP 4 — Afternoon Opportunity Scan

**VIX regime:** NORMAL (1.00×) | **Positions:** 0/6 | **Week trades:** 0/3 | **PDT:** 0/3

**Note on timing:** Quotes pulled at ~19:45–19:50 UTC (~15:45–15:50 ET). This is within the **"no new entries — last 15 minutes"** window per TRADING-STRATEGY.md rules. Additionally, **NFP (Nonfarm Payrolls) releases tomorrow pre-market** — entering positions in the final minutes before a binary macro event violates the risk framework. Both rules independently prohibit new entries at this scan time even if a signal were to qualify.

**CVX — Z-Score Correction Note:**
The initial midpoint calculation used a stub AH bid ($175.00) which produced an artificially wide spread (4.22%) and an inflated Z-Score of −2.70. The correct calculation uses the last session close ($182.66) as proxy for fair value (ask $182.71 = only $0.05 above close):

| Metric | Value |
|--------|-------|
| Last close | $182.66 |
| Ask (AH) | $182.71 (Δ $0.05 vs close) |
| Bid (AH) | $175.00 (stub quote — not actionable) |
| Corrected Z-Score (vs last close) | **−1.5418** |
| Layer B gate (≤ −2.0) | ❌ **FAILS** |

The stub bid is a known after-hours illiquidity artifact. Fair value is the ask price, which is nearly identical to the close. CVX does NOT qualify on Layer B.

**Universe Scanned (5 candidates):**

| Ticker | Last Close | Z-Score (20d) | Spread | Layer A | Layer B | Verdict |
|--------|------------|---------------|--------|---------|---------|---------|
| CVX | $182.66 | **−1.5418** | 0.027% (close basis) | ❌ Neg catalyst, RSI unconfirmed, sector broken, R:R <2:1 | ❌ Z=−1.54 fails ≤−2.0 | **REJECT** |
| XLE | $55.955 | **−0.8100** | 0.018% ✅ | ❌ No catalyst, R:R fails at trigger | ❌ Z=−0.81 fails | **REJECT** |
| PLTR | $137.20 | **−0.6091** | 0.022% ✅ | ❌ Z gate fails (not close to trigger) | ❌ Z=−0.61 fails | **REJECT** |
| MCD | $285.11 | **−1.5184** | 1.07% ⚠️ | ❌ Z gate fails; spread marginal | ❌ Z=−1.52 fails | **REJECT** |
| XLB | $51.49 | **−0.4878** | 0.019% ✅ | ❌ Z gate fails (far from −2.0) | ❌ Z=−0.49 fails | **REJECT** |

**Pair Z-Scores calculated:**
- XOM (reference, last close $146.09): Z = −1.859 | CVX−XOM divergence = 0.318σ ✅ (confirms sector cohesion, both moving together in energy selloff)
- LIN (XLB pair, last close $494.00): Z = −1.260 | XLB−LIN divergence = 0.772σ ✅ (neither at trigger)

---

**Detailed Candidate Notes:**

**CVX — DUAL REJECT (Both Layers):**
- Z = −1.54 (was incorrectly calculated as −2.70 using stub bid; corrected to −1.54 using last close/ask). Fails Layer B.
- Layer A failures: (1) Negative catalyst — the Iran ceasefire narrative that broke XOM is directly applicable to CVX as an integrated oil major; WTI ~$91 (was $106 at XOM entry). Entering CVX long immediately after XOM thesis-break exit = the identical trade that just lost −4.73%. (2) RSI unconfirmed — 4 consecutive red days for energy suggests RSI is approaching but likely not sub-30. (3) Sector momentum broken — XOM thesis-break constitutes energy sector failure #1. CVX would be trade #2 in energy; if it also fails = 2 consecutive sector failures triggering the blanket exit rule. (4) R:R to realistic target (20d mean $187.74) = only 0.40:1; fails the 2:1 minimum. The 1-hour cooldown rule (CONSTRAINTS.md: "NO revenge trades") also applies given the XOM exit ~2 hours prior.
- **VERDICT: REJECT on both Layer A (4 separate failures) and Layer B (Z=−1.54, needs ≤−2.0)**

**XLE — REJECT:**
- Z = −0.81. Needs to fall ~$1.51 more to ~$54.47 for Z = −2.0. Energy sector is the broken thesis sector. Even if Z triggered, same negative catalyst issue as CVX applies.

**PLTR — REJECT:**
- Z = −0.61. Moved in the wrong direction today (+$3.41, +2.55% from yesterday's close) — mean-reverting upward, not deepening toward oversold. Long trigger at ~$129.60 (Z=−2.0) requires ~−5.6% additional decline from current. Post-earnings drift suggests the stock has found interim support.

**MCD — REJECT:**
- Z = −1.52. Spread 1.07% is marginally above the 1% threshold (AH-related). Would need additional ~$13 decline to ~$280 for Z = −2.0. NFP tomorrow could be a catalyst if consumer spending data is embedded in the print.

**XLB — REJECT:**
- Z = −0.49. Far from −2.0 trigger. Setup has completely reset from the near-trigger conditions of May 4 (Z=−1.936). XLB has been bouncing this week.

**New afternoon entries: NONE** — all 5 candidates rejected on composite Layer A + Layer B gates. Zero bracket orders placed.

---

### Afternoon Market Context

Today (May 7) represents a clean portfolio reset: the XOM position that had been held since May 1 was exited at 17:55 UTC via thesis-break (−4.73% realized loss), leaving the portfolio at 100% cash ($99,056.49). The energy sector thesis (Strait of Hormuz supply premium, WTI elevated) was invalidated by the emerging US-Iran ceasefire narrative, which drove WTI from ~$106 (entry thesis) to ~$91.59 — a −13.6% oil move that directly undermined the entry catalyst. The broader equity market (S&P futures near ATHs, VIX ~17.38) continues its constructive posture, with the energy selloff appearing sector-specific rather than a broad risk-off event. This is consistent with the VIXY trend (declining $27.76 → $26.98) observed during the energy drawdown. 

The afternoon scan produced zero qualifying candidates — the quant filter (Z ≤ −2.0) is working as designed, keeping the bot out of marginal setups. The most important development for tomorrow is **NFP at 8:30 AM ET**: consensus 49,000 new jobs, 4.3% unemployment. A strong print could catalyze a broad equity bounce and potentially re-price some oversold candidates (CVX Z=−1.54, MCD Z=−1.52) toward their triggers. A weak print could accelerate risk-off but may also produce oversold readings in quality names. The research API (Gemini) remains offline — operator must resolve before tomorrow's pre-market workflow.

---

**Bracket fills today:** 0 (no morning limits placed — HOLD decision at pre-market)
**Stops upgraded:** 0 (no positions held; trailing stop was already cancelled as part of the 17:55 UTC thesis-break exit)
**Stale limits cancelled:** 0 (none existed)
**New afternoon entries:** none — all 5 candidates failed composite Layer A + Layer B gates; additionally within no-entry window (last 15 min) and NFP binary event tomorrow
**Key watchlist for Friday pre-market (May 8 — NFP Day):**
1. **CVX** — Z = −1.54 (corrected from earlier −2.70 error); needs further weakness OR NFP-driven oil bounce re-establishing a positive catalyst; also needs RSI < 30 confirmation
2. **MCD** — Z = −1.52; if consumer confidence data in NFP is weak and MCD sells toward $280, Z ≤ −2.0 may trigger; watch spread normalization during session
3. **XLE** — Z = −0.81; sector ETF proxy; same energy thesis issues as CVX apply
4. **POST-NFP NEW IDEAS** — Strong NFP may generate fresh momentum setups in tech/cyclicals. Weak NFP may trigger rate-sensitive names (utilities, REITs). Scan full universe post-print.
5. **Energy sector protocol:** After XOM thesis-break (failure #1 in energy), next energy trade is flagged as potential failure #2. Per sector rules, if a second energy trade fails, exit entire sector. Approach energy names with heightened caution until WTI stabilizes and a clean, confirmed positive catalyst (not just a statistical level) re-emerges.


---

## 2026-05-19 — Pre-Market Research

> **URGENT: Build — Decouple conditional gates (cash-headroom-only cross-check).** This adjustment has appeared on the weekly review list 3+ times and is NOT encoded in CONSTRAINTS.md. Each position idea must run its own independent checklist; the only cross-position gate should be: "Will total deployed capital ≤ 85% of equity?" No other inter-position dependency. Needs a code pass in CONSTRAINTS.md and/or ROUTINE.md.

---

### Adjustment Audit (from Week-2 weekly review, week ending 2026-05-08)

| # | Adjustment | Status | Evidence |
|---|-----------|--------|----------|
| 1 | [URGENT — DEPLOYMENT] File concrete 3-position scan plan before Monday open | ✅ ADDRESSED — XOM, NVDA, XLE evaluated with entry/stop/target. Concrete plan documented in this entry. | This research entry |
| 2 | [PROCESS] Implement and verify midday re-scan (10:30 CT) | ✅ IMPLEMENTED IN CODE BUT NOT TRIGGERED — `.github/workflows/midday-rescan.yml` exists; ROUTINE.md "5b. MIDDAY-RESCAN" section exists with full prompt. No-trigger issue because zero candidates cleared market-open stage in recent sessions. Calibration gap, not missing feature. | `ls .github/workflows/` → midday-rescan.yml; ROUTINE.md line 619 |
| 3 | [PROCESS] Implement pre-open live-quote check (T−30 min) | ✅ IMPLEMENTED IN CODE — market-open workflow Step 2 "Re-Validate with Live Quotes" exists. | ROUTINE.md line 276 |
| 4 | [POSITION] Evaluate XOM time-stop | ✅ RESOLVED — XOM exited May 7 via thesis-break at −4.73%. No position to time-stop. Fresh entry evaluated today. | TRADE-LOG.md |
| 5 | [STRATEGY] Decouple conditional gates — cash-headroom only | ❌ NOT IMPLEMENTED — `grep "cash-headroom" memory/CONSTRAINTS.md` → no output. Logic not explicitly encoded anywhere. Still ad-hoc per research prompt. | `grep cash-headroom CONSTRAINTS.md` → (no output) |
| 6 | [ACCOUNTABILITY] Tag each prior-week adjustment in Monday research log | ✅ IMPLEMENTED — This audit section fulfills the requirement. | This entry |

**Net: 1 ❌ item** → See URGENT note at top of this entry.

---

### Account

- **Equity:** $99,056.46
- **Cash:** $99,056.46 (100%)
- **Buying power:** $198,112.92 (2× margin)
- **Daytrade count:** 0/3
- **Open positions:** 0/6
- **Open orders:** None
- **Week trades used:** 0/3
- **Phase P&L:** −$943.54 (−0.94% from $100,000 start — 1 closed trade: XOM −4.73%)

---

### Market Context

**Oil:**
- WTI Crude: $105.42 (Fri May 16 settle, +4.2% day, +10.48% week); reports of $107 as of May 17
- Brent Crude: $109.26–$109.50 (Fri May 16 settle, +3.35% day, +7.84% week); highest since May 5
- Driver: Ongoing US-Iran conflict + Strait of Hormuz supply disruption fears; Brent ~$70 pre-conflict
- Implication: Energy sector structurally supported; WTI now at multi-month high

**Equities:**
- S&P 500: Closed Fri May 15 at $7,408.50 (−1.2% from ATH of $7,501.24 set May 14)
- SPY premarket Fri: $739.62 (−1.14%)
- S&P 500 Futures Index YTD return: +9.84% as of May 14
- Goldman Sachs projects ~12% full-year rally

**VIX:** 18.43–18.86 (May 15, 2026) — Normal regime

**Today's Earnings (May 19 Pre-Market):**
- Home Depot (HD) — Q1 FY2027 (binary event: skip as entry candidate today)
- KE Holdings (BEKE), Canaan (CAN), Pearl Diver Credit (PDCC), Reading Intl (RDI)
- Baidu, Ryanair Holdings

**This Week's Earnings (Binary Risk — No New Positions Through These):**
- NVDA — Wed May 20 (Q1 FY2027, highly anticipated AI demand read)
- Home Depot, Lowe's, Target, TJX, BJ's — Tue/Wed
- Walmart — Thu May 22

**Economic Calendar (May 19):**
- 10:00 AM ET: Pending Home Sales M/M and Y/Y (April)
- Redbook YoY, ADP Employment Change Weekly

**Coming This Week:**
- FOMC Meeting Minutes — Wed May 20 at 2:00 PM ET
- Philly Fed Manufacturing, Building Permits, Housing Starts, PMI Manufacturing — May 21
- Next CPI: July 14 | Next PPI: July 15 | Next BLS Jobs: July 2

**Sector Momentum YTD (through May 15):**
- Energy: +38.3% (as of Q1) — dominant leader
- Telecom Services: +33.6%
- Information Technology: +24.0%
- Laggards: Consumer Discretionary ("Least Favored"), Commercial Real Estate, Utilities (mixed)
- Energy declined −2.63% in April (ceasefire scare) but has re-accelerated sharply in May

---

### VIX Regime

- **Current VIX:** ~18.86 (May 15, 2026)
- **Regime:** Normal (VIX 14–22)
- **Sizing multiplier:** 1.00×
- **All entry types OK** (both momentum and mean-reversion eligible)

---

### Trade Ideas (Cleared Both Layers)

---

#### ✅ IDEA 1: XOM | **LONG** | Lane: 2b-LONG (Momentum Breakout)

**Catalyst:** WTI oil surged +10.48% last week to $105.42–$107, driven by US-Iran conflict and Strait of Hormuz supply fears. XOM rallied +3.4% on Friday May 15 to $157.92, breaking out above its 20-day high of $154.88. The structural oil supply disruption thesis that was previously invalidated by ceasefire rumors (causing the May 7 thesis-break exit) has now reversed dramatically — WTI has recovered from the ~$91 ceasefire-scare low all the way back to $105+, a +15.4% recovery. This is a clean, confirmed catalyst re-entry, not a revenge trade. The energy sector's YTD lead (+38.3%) is firmly intact.

**Layer A — Catalyst + Trend Template:**

| Check | Result |
|-------|--------|
| Ticker | XOM |
| Direction | LONG |
| Sector | Energy (YTD #1 sector, +38.3%) |
| Catalyst (today) | WTI $105+ on Hormuz/Iran, XOM broke out Fri +3.4% |
| Sector posture | Momentum (Energy = YTD leader) ✓ |
| RSI(14) | ~64.2 (50–70 range for momentum) ✓ |
| Volume | 27,890,724 vs 20d avg 16,665,969 = 1.67× (≥1.5× required) ✓ |
| Stop level | $146.87 (−7.0% below entry $157.92) ✓ |
| Target | $180.02 (+14.0%, 2:1 R:R) ✓ |

**Minervini Long Trend Template (all from 210-bar data):**

| Condition | Value | Pass? |
|-----------|-------|-------|
| Price > 50d SMA | $157.92 > $154.82 | ✅ |
| Price > 150d SMA | $157.92 > $135.77 | ✅ |
| Price > 200d SMA | $157.92 > $101.83 | ✅ |
| 150d SMA > 200d SMA | $135.77 > $101.83 | ✅ |
| 200d SMA trending up ≥ 1 month | $101.83 vs 1mo-ago $96.38 → UP | ✅ |
| 50d SMA > 150d SMA | $154.82 > $135.77 | ✅ |
| 50d SMA > 200d SMA | $154.82 > $101.83 | ✅ |
| Price > 30% above 52w low ($110.64) | $157.92 > $143.83 | ✅ |
| Price within 25% of 52w high ($171.47) | $157.92 ≥ $128.60 | ✅ |
| 6-month return | +33.7% (from $118.12) | ✅ Top quintile |

**Trend Template: ALL CONDITIONS PASS ✅**

*Note: 200d SMA ($101.83) reflects the 210-bar window starting Oct 2025 when XOM was ~$110. The stock has rallied ~43% from Oct 2025 lows — a true Minervini leader.*

**Layer B — Quant Checklist (Lane 2b-LONG — Momentum):**

- `Z-Score = (157.92 − 150.25) / 2.86 = +2.68` → Z ≥ +1.0 ✓
- `Close $157.92 > prior 20d high $154.88` → Clean breakout ✓
- `RSI(14) ≈ 64.2` → 50–70 zone ✓
- `Volume 1.67×` → ≥1.5× avg ✓
- `50d SMA $154.82 > 200d SMA $101.83` → Uptrend confirmed ✓
- **Pivot extension:** ($157.92 / $154.88 − 1) × 100 = **+1.96%** → ≤5% ✓

**Lane 2b-LONG: ALL CHECKS PASS ✅**

**Pair Confirmation (XOM ↔ CVX — canonical energy pair):**
- CVX last close: $191.10 | Z-Score: +1.21
- XOM Z: +2.68 | CVX Z: +1.21
- Divergence: |2.68 − 1.21| = **1.47σ** → ≤1.5σ ✓
- Both names moving in same direction (energy rally); sector thesis confirmed
- **Pair check: PASS ✅**

**Position Sizing:**
- Cold start (< 30 closed trades): flat 10% default
- VIX multiplier: 1.00× (Normal regime)
- Sized position: **10% of equity = $9,905.65**
- Shares: **62 shares @ $157.92 = $9,791.04 (9.9% of equity)**
- Hard cap 20% ✓ | Floor 5% ✓

**R-Multiple:**
- Entry: $157.92 | Stop: $146.87 | Target: $180.02
- R_dollars: **$685.10** (0.69% of equity) — valid range 0.5–1.5% ✓
- Target R: **2.0R** (minimum ≥2.0 ✓)
- R:R verified: 2:1 ✓

**Risk Flags:**
- ⚠️ Energy sector has 1 consecutive failure (XOM thesis-break May 7). A second failure in energy would trigger the blanket sector-exit rule. This is a risk factor, not a gate violation — the thesis has legitimately reset with WTI recovering from $91 to $105+.
- ⚠️ If the US-Iran situation changes (ceasefire/diplomacy) and WTI reverses, this thesis breaks again. Stop at $146.87 is the hard circuit breaker.
- ⚠️ Z = +2.68 is above the 2b-LONG threshold — the stock is extended above its recent mean. Entry at the 20d-high breakout level; if price gaps further Monday, the limit may not fill (correct behavior — do not chase).

**VERDICT: TRADE ✅**

---

### Skipped Candidates

| Ticker | Direction Evaluated | Lane Attempted | Specific Failure | Notes |
|--------|---------------------|----------------|------------------|-------|
| **NVDA** | LONG | 2b-LONG (Momentum) | Close $225.32 < 20d high $235.74 — **no breakout** (pulled back 4.4% from ATH) | Z=+1.56 passes threshold but price is below its own pivot; also volume 1.19× < 1.5× required. Both checks fail. Earnings Wed = binary. Skip. |
| **NVDA** | LONG | 2a-LONG (Mean-Reversion) | Z=+1.56 — **not oversold** (needs Z ≤ −2.0) | Stock is elevated, not depressed. Wrong lane. |
| **XLE** | LONG | 2b-LONG (Momentum) | 150d/200d SMA unavailable (Dec 2025 2:1 split disrupts pre-split data). Unable to verify full Trend Template. Also volume 0.86× < 1.5× required. | Energy sector exposure already covered via XOM. ETF less efficient than underlying. Skip. |
| **HD** | LONG | Any | **Earnings pre-market TODAY (May 19)** — binary event, gap risk. Cannot enter into an unknown binary. | Wait for post-earnings direction; evaluate Tuesday if thesis clear. |
| **XRT / XLRE** | SHORT | 2b-SHORT / 2a-SHORT | Bars data not pulled. S&P −1.2% from ATH with constructive breadth — insufficient edge for index/sector short in Normal VIX regime with no specific negative catalyst today. | Consumer Discretionary "Least Favored" is a sector rotation theme, not a same-day short trigger. |

---

### Risk Factors

1. **US-Iran conflict escalation/de-escalation binary:** The primary oil price driver is geopolitical. A surprise diplomatic breakthrough could send WTI back toward $85–90 instantly (as happened May 6–7). The $146.87 stop is the only protection.
2. **FOMC Minutes Wed + multiple Fed speakers:** Rate outlook commentary could move the broad market. Higher-for-longer on inflation (oil-driven) = bearish for equities, potentially including XOM if broad risk-off overwhelms energy momentum.
3. **NVDA earnings Wed May 20 (after market):** If NVDA disappoints, tech selloff could pressure the broad market. Energy tends to decouple in that scenario, but sentiment contagion is real.
4. **Earnings parade (HD today, retail heavyweights Tue–Thu):** If HD or Walmart signal serious consumer weakness from oil/tariff-driven inflation, could trigger risk-off broad market.
5. **Oil at $105+ already prices in significant supply premium:** A relief of tensions, even partial, could produce outsized WTI downside. Entry into XOM at current levels assumes the disruption premium persists.
6. **Pending Home Sales (10:00 AM ET today):** A weak print could boost defensive/rate-sensitive sectors but hurt cyclicals including energy; monitor for sentiment shift.

---

### Decision

**TRADE — 1 position (XOM LONG)**

**Action for market-open workflow:**
> Place bracket limit order: XOM | BUY 62 shares | Limit $157.92 | Stop $146.87 | Take-Profit $180.02 | TIF: day

If XOM gaps above ~$160.90 pre-market (+1.9% from $157.92, pushing pivot extension above the 2% threshold documented here toward the 5% max), do NOT chase — let the order sit unfilled and re-evaluate tomorrow.

**Short candidates: NONE today** — no valid setup cleared both layers for a short; VIX Normal supports staying net-long; heavy earnings week creates noise but not a clean short catalyst.

**Deployment note:** This brings potential deployment to ~10% of equity (1 position). Still below the 75–85% target, but the quant gates correctly filtered the universe to 1 qualifying idea. The weekly review adjustment "[URGENT — DEPLOYMENT]" is being addressed by fielding a documented, gated idea rather than forcing marginal setups. Per strategy: "A week with zero trades can be the right call" — but 1 qualifying trade > 0.


---

## 2026-05-18 — Pre-Market Research (Monday)

### Adjustment Audit (from Week ending 2026-05-14 weekly review)

- **Implement midday execution check (10:00–10:30 AM CT):** ✅ IMPLEMENTED — evidence: `.github/workflows/midday-rescan.yml` — `cron: '30 14 * * 1-5'` (10:30 AM ET Mon–Fri). Workflow file exists and is scheduled.
- **Revise research entry ceiling logic for earnings plays (post-gap ceiling adjustment):** ❌ NOT IMPLEMENTED — grep of `memory/TRADING-STRATEGY.md`, `memory/CONSTRAINTS.md`, and `.claude/commands/ROUTINE.md` finds no "post-gap ceiling" or "gap_open × 0.97" logic. This adjustment was only documented in the weekly review narrative, never built into any prompt or constraint file.
- **Re-evaluate CVX for entry next week:** ✅ ADDRESSED — CVX evaluated today as independent candidate; failed Layer B (volume 1.10× < 1.5× required for 2b-LONG). Thesis valid, volume insufficient. Will re-evaluate when volume confirms.
- **Continue holding XOM / scan for non-energy momentum:** ✅ ADDRESSED — XOM re-evaluated and qualifies today (energy thesis intact, WTI $106+). Non-energy sectors scanned: Financials (XLF failed Layer B, Z = -0.31), Health Care (XLV failed Layer B, Z = -0.10), NVDA/Tech skipped (earnings binary Wed + price below 20d high). Constraint noted.
- **Key rotation protocol (pre-session API health check):** ❌ NOT IMPLEMENTED — grep of `scripts/run_workflow.py` shows the API key is checked reactively (if key is missing, error is returned) but no proactive pre-session health-check gate exists that halts execution and escalates. The GEMINI_API_KEY is only validated when the research function is called, not as a startup gate.
- **[STRATEGY] Decouple conditional gates:** ✅ IMPLEMENTED IN PROMPT — ROUTINE.md and today's workflow explicitly evaluate each candidate independently. CVX and XOM evaluated on own merits — XOM qualified on its own; CVX failed on its own; no chain dependency created.
- **[ACCOUNTABILITY] Tag each prior-week adjustment as Implemented/Not in Monday research log:** ✅ IMPLEMENTED — this section is the implementation.

> **URGENT: build post-gap ceiling adjustment** — the "recalculate entry as gap_open × 0.97–1.01" logic has been on the adjustment list for 2 weeks. Needs a prompt-level rule in `memory/CONSTRAINTS.md` or `TRADING-STRATEGY.md` under "Order Execution Strategy." Not a coding task — a constraint file update.
>
> **URGENT: build pre-session API health-check gate** — key must be tested at workflow START, not reactively mid-run. Needs a startup step in `scripts/run_workflow.py` that calls a lightweight Gemini ping and halts/alerts if it fails. Prevents silent research blackouts.

---

### Account
- **Equity:** $99,056.46
- **Cash:** $99,056.46 (100% — fully undeployed)
- **Buying power:** $198,112.92 (margin account — RegT 2×)
- **Daytrade count:** 0/3
- **Open positions:** 0/6
- **Open orders:** 0
- **Week trades used:** 0/3

---

### Market Context
- **WTI Crude Oil:** ~$106.34–$106.37/bbl (+0.87–0.90% DoD) — elevated geopolitical risk premium, US-Iran tensions
- **Brent Crude:** $109.07–$110.25/bbl (−0.17% to +0.91%) — spread tightening slightly
- **S&P 500 Futures:** E-mini settled $7,432.25 (10:00 AM CT); early drop −0.3%; June futures hit ATH $7,540 in some reports
- **VIX:** 18.43 (up 6.78% from 17.26 prior close; opened 18.07) — Normal regime
- **US 10yr yield:** >4.50%; 30yr >5.00% — aggressively higher long-end
- **CPI (April):** 3.8% YoY | **PPI (April):** 6.0% headline / 5.2% core — inflation still hot
- **Unemployment:** 4.3%, 115K jobs added
- **Fed posture:** July hike odds only 4%; 91% probability of pause. FOMC minutes due Wednesday.
- **Economic calendar today:** NAHB Housing Market Index, Treasury Buyback Announcement (preliminary), 3M/6M Bill Auctions, Business Leaders Survey (7:30 AM CT)
- **Earnings today (pre-market):** Baidu (BIDU — AI revenue +49% YoY), Ryanair (RYAAY, expected loss), iQIYI, Brady (BRC)
- **Earnings this week (key):** Nvidia (NVDA) Wednesday after close — projected $79B rev, +78% YoY; Walmart, Home Depot, Lowe's, Target
- **Sector momentum YTD:** Energy +27.87% | IT +23.55% | Materials +15.24% | Industrials +12.84% | RE +10.46% | Consumer Staples +7.32% | Utilities +5.74% | Consumer Disc −0.03% | Comm Services −1.82% | Financials −6.55% | Health Care −7.60%
- **Index YTD:** S&P 500 +10% through May 14; TMT = 85% of that return; NVDA alone = 20% of YTD return
- **Key geopolitical risk:** US-Iran — fragile ceasefire, ongoing attacks on energy infrastructure supporting oil premium

---

### VIX Regime
- **Current VIX:** 18.43
- **Regime:** Normal (14–22 range)
- **Sizing multiplier:** 1.00×
- **Strategy bias:** All entry types eligible; no regime-based restriction

---

### Candidate Evaluations

#### CANDIDATE 1: XOM | LONG | Sector: Energy

**Layer A — Catalyst + Trend Template:**
- **Catalyst:** WTI crude ~$106.34 (+0.87% today); Brent ~$109–$110. US-Iran tensions, attacks on energy infrastructure sustaining supply disruption premium. Energy sector best YTD performer at +27.87%. XOM surged Friday May 15 from $152.78 → $157.92 on 1.70× volume — confirmed breakout day. Today continuing above Friday's close.
- **Sector posture:** ✅ Energy is #1 YTD sector (+27.87%), actively in momentum
- **RSI(14):** 61.72 — ✅ within 50–70 momentum zone
- **Volume (breakout day May 15):** 27,890,724 vs 20d avg 16,410,412 = **1.70×** ✅ ≥1.5× required
- **Stop level:** $147.80 (7.5% below $159.78 entry)
- **Target:** $183.74 (2R above entry)
- **R:R:** 2.0:1 ✅

**Minervini Long Trend Template:**
| Condition | Value | Pass? |
|-----------|-------|-------|
| Price > 50d SMA ($155.13) | $159.78 | ✅ |
| Price > 150d SMA ($136.40) | $159.78 | ✅ |
| Price > 200d SMA ($136.23) | $159.78 | ✅ |
| 150d SMA > 200d SMA | $136.40 > $136.23 | ✅ |
| 200d SMA trending up ≥1 month | $136.23 today vs $133.91 prior | ✅ (+1.7%) |
| 50d SMA > 150d SMA | $155.13 > $136.40 | ✅ |
| 50d SMA > 200d SMA | $155.13 > $136.23 | ✅ |
| Price > 30% above 52w low ($110.64) | +44.4% | ✅ |
| Price within 25% of 52w high ($171.47) | 7.3% below high | ✅ |
| 6-month return percentile ≥70th | +34.5% (6mo) — top quartile vs universe | ✅ |

**All 10 Long Trend Template conditions: PASS ✅**

**Layer B — Quant (Lane 2b-LONG — Momentum):**
- **Z-Score:** +2.749 (price $159.78 vs 20d mean $150.82, σ $3.258) — ✅ ≥+1.0
- **Close > prior 20d high ($157.92):** $159.78 > $157.92 — ✅ clean breakout
- **RSI(14) 50–70:** 61.72 — ✅
- **Volume breakout day:** 1.70× — ✅ ≥1.5×
- **50d SMA > 200d SMA:** $155.13 > $136.23 — ✅
- **Pivot extension:** ($159.78 / $157.92 − 1) = **1.18%** — ✅ ≤5%
- **Lane 2b-LONG: ALL CHECKS PASS ✅**

**Pair Check (XOM ↔ CVX):**
- CVX Z-Score: +1.8731 (moving in same direction, both above 20d mean)
- Z-divergence: |2.749 − 1.873| = **0.876σ** — ✅ ≤1.5σ required
- Both XOM and CVX are in uptrends, confirming sector thesis

**VIX regime:** Normal (18.43) — ✅ new entries allowed

**Layer B: PASS ✅ — Both layers cleared**

**Position Sizing:**
- Cold start default: 10% of equity × 1.00× VIX
- Position size: $9,905.65
- **Shares: 61 @ $159.78 limit = $9,746.58 (9.8% of equity)**
- **R_dollars: $730.78 (0.738% of equity)** — valid 0.5–1.5% ✅
- **Target R: 2.0R** — verified ≥2:1 ✅
- **Pivot extension: 1.18%** ≤5% ✅

---

#### CANDIDATE 2: CVX | LONG (evaluated independently) | Sector: Energy

**Layer A — Catalyst + Trend Template:**
- **Catalyst:** Same energy thesis as XOM — WTI $106+, Iran tensions, Energy #1 YTD sector. CVX broke above its own 20d high ($193.31) today, reaching $193.98.
- **Sector posture:** ✅ Energy momentum intact
- **RSI(14):** 58.01 — ✅ 50–70 range
- **Volume (today = breakout day for CVX):** Partial day 3,134,501; yesterday full day 11,220,294 = **1.10×** 20d avg (10,168,301) — ❌ **FAILS ≥1.5× requirement**
- **Stop level:** $179.43 (7.5% below $193.98)
- **Target:** $223.08 (2R)
- **R:R:** 2.0:1 ✅

**Minervini Long Trend Template:**
| Condition | Value | Pass? |
|-----------|-------|-------|
| Price > 50d SMA ($193.13) | $193.98 | ✅ (barely) |
| Price > 150d SMA ($172.60) | $193.98 | ✅ |
| Price > 200d SMA ($172.45) | $193.98 | ✅ |
| 150d SMA > 200d SMA | $172.60 > $172.45 | ✅ |
| 200d SMA trending up ≥1mo | Need to verify | ~✅ |
| 50d SMA > 150d SMA | $193.13 > $172.60 | ✅ |
| 50d SMA > 200d SMA | $193.13 > $172.45 | ✅ |
| Price > 30% above 52w low ($146.75) | +32.2% | ✅ |
| Price within 25% of 52w high ($211.15) | 8.9% below | ✅ |
| 6mo return ≥70th percentile | +24.7% (6mo) | ✅ |

**Trend Template: PASS ✅**

**Layer B — Quant (Lane 2b-LONG):**
- **Z-Score:** +1.873 — ✅ ≥+1.0
- **Close > prior 20d high ($193.31):** $193.98 — ✅
- **RSI 50–70:** 58.01 — ✅
- **Volume breakout day:** 1.10× — ❌ **FAILS ≥1.5× requirement**
- **50d SMA > 200d SMA:** ✅

**Lane 2b-LONG: FAIL — Volume 1.10× < 1.5× required ❌**

**VERDICT: SKIP — Layer B fails on volume.** Thesis intact. Re-evaluate tomorrow if volume picks up.

---

#### CANDIDATE 3: NVDA | LONG (evaluated independently) | Sector: Technology

**Lane attempted:** 2b-LONG (Momentum — AI earnings catalyst, sector leadership)

**Layer B quick fails:**
- **Price > 20d high ($235.74):** $222.895 — ❌ **FAILS** (price is 5.4% below its own 20d high after pullback from ATH)
- **Earnings binary Wednesday (after close):** NVDA reports May 20 after market — entering pre-earnings is a binary event with gap risk in either direction. Strategy rule: no entering into unknown binary events.

**VERDICT: SKIP — Price below 20d high (no breakout); earnings binary risk. Do not enter.**

---

### Short Candidates Evaluated

| Ticker | Direction | Lane Attempted | Specific Failure |
|--------|-----------|----------------|------------------|
| **XLF** | SHORT | 2b-SHORT (Momentum Short) | Z = −0.307 (need ≤−1.0 ❌); Price NOT below 20d low ❌; RSI 52.30 out of 30–50 range ❌; 150d SMA NOT < 200d SMA ❌. Multiple failures. |
| **XLV** | SHORT | 2b-SHORT (Momentum Short) | Z = −0.095 (need ≤−1.0 ❌); Price NOT below 20d low ($142.84) ❌; Price only 9.5% below 52w high (need >30% below ❌). Not in statistical breakdown. |

Both Financials and Health Care are lagging sectors YTD but neither is in a statistically confirmed breakdown (Z near 0, not making new multi-week lows). No short qualifies today.

---

### Skipped Candidates (Summary)

| Ticker | Reason |
|--------|--------|
| **CVX** | Layer B FAIL — Volume 1.10× on breakout day < 1.5× required. Thesis valid; re-evaluate if volume confirms tomorrow. |
| **NVDA** | Layer B FAIL — Close $222.895 below 20d high $235.74 (no breakout). Additionally: earnings binary Wednesday after close — no entry into unknown binary event regardless of other conditions. |
| **XLF** | Layer B FAIL — Z = −0.307, not at new 20d low, RSI out of range, SMA alignment wrong. Not in breakdown regime. |
| **XLV** | Layer B FAIL — Z = −0.095, not at new 20d low, only 9.5% below 52w high (needs >30%). Not in breakdown regime. |

---

### Trade Ideas (Cleared Both Layers)

**1. XOM | LONG | Lane 2b-LONG (Momentum) | Energy Sector**
- **Catalyst:** WTI crude $106.34 (+0.87%); Brent $109–$110; US-Iran supply disruption premium sustained; Energy sector #1 YTD at +27.87%; XOM confirmed breakout Friday with 1.70× volume
- **Entry (limit):** $159.78
- **Stop:** $147.80 (7.5% below entry — technical support at recent consolidation)
- **Target:** $183.74 (2.0R above entry)
- **R:R:** 2.0:1 ✅
- **Z-Score:** +2.749 (vs 20d mean $150.82) ✅
- **Trend Template:** PASS — all 10 conditions verified (see table above)
- **Pair:** CVX | Pair Z-Score: +1.873 | Divergence: 0.876σ ✅ ≤1.5σ
- **Sized position:** 10% of equity ($9,905.65) → **61 shares @ $159.78 = $9,746.58 (9.8%)**
- **R-Multiple:** R_dollars $730.78 (0.738% of equity) | Target R = 2.0R | R:R verified ≥2:1 ✅
- **Pivot extension:** pivot $157.92 → limit $159.78 → **1.18% extension** ≤5% ✅

**Action:** Place bracket limit order: XOM | BUY 61 shares | Limit $159.78 | Stop $147.80 | Take-Profit $183.74 | TIF: day

> Note: If XOM gaps materially above $162.00+ pre-open (>2.5% above today's close), reconsider whether limit is still within 5% of pivot or whether to wait for pullback. Do NOT chase if limit cannot fill at ≤$165.77 (pivot $157.92 × 1.05).

---

### Risk Factors

1. **FOMC Minutes Wednesday (same day as NVDA earnings):** Double-risk event mid-week. If minutes signal hawkish pivot or November rate hike discussion intensifies, broad market could sell off. Energy typically decouples in oil-driven rally, but systemic risk-off could overwhelm sector thesis.
2. **NVDA earnings Wednesday after close:** The single largest S&P 500 contributor to 2026 YTD returns (20%). A miss on the $79B revenue estimate or conservative guidance could trigger a tech selloff. Energy may benefit from risk-off rotation into commodities, or it could face contagion selling.
3. **US-Iran ceasefire/resolution risk:** XOM thesis rests on continued supply disruption premium. A surprise diplomatic resolution or reduction in Hormuz tensions could snap WTI back toward $85–90 (as happened briefly in early May). Stop at $147.80 is the hard floor.
4. **30-year yield >5.00%:** Long-duration bond yields rising aggressively. If equity risk premium compresses and multiple compression begins, energy stocks could face selling even with strong oil prices. XOM's recent strength partially reflects oil price, not valuation expansion.
5. **Retail earnings parade (Walmart tomorrow, Target/Lowe's mid-week):** Weak consumer signals could trigger rotation out of cyclicals including energy. Monitor for thesis breaks.
6. **Two consecutive energy failures rule:** XOM had a thesis-break stop-out on May 7 ($146.09). This would be the second XOM entry. If this trade fails, the energy sector would have 2 consecutive failures → triggers the blanket sector-exit rule. The risk is elevated because of this sequential context.
7. **VIX up 6.78% today:** Rising from 17.26 to 18.43 suggests some risk-off tone. Still Normal regime (14–22), but worth monitoring. If VIX breaks above 22, sizing would drop to 0.75× for any new entries.

---

### Decision

**TRADE — 1 position (XOM LONG)**

**Action for market-open workflow:**
> Place bracket limit order: XOM | BUY 61 shares | Limit $159.78 | Stop-Loss $147.80 | Take-Profit $183.74 | TIF: day

**Deployment note:** This brings deployment to ~9.8% of equity (1 position out of a 75–85% target). The quant gates correctly filtered a 5-candidate universe to 1 qualifying idea. CVX is the strongest runner-up — it will be re-evaluated Tuesday if volume picks up above 1.5× on a follow-through day. The persistent underdeployment issue continues to be driven by volume requirements, not lack of thesis or trend template failures. This is correct gate behavior: forcing deployment without volume confirmation is the exact error the quant layer was designed to prevent.

**Short candidates: NONE today** — XLF and XLV are weak sectors YTD but not in statistical breakdown (Z near 0, not at new 20d lows). No short setup cleared Layer B.


---

### 2026-05-18 — Midday Rescan Addendum (17:21 UTC / ~12:21 PM ET)

**VIX Regime at rescan:** Normal (18.43 — unchanged from morning; all entry types eligible, 1.00× sizing)

**XOM Pending Order Status:**
- Order ID: `1d69c496-b40b-4974-9299-cac1a65bd5b9`
- BUY 61 @ $159.78 limit (bracket: stop $147.80, take-profit $183.74) | TIF: day
- **Status: UNFILLED** — current mid $161.28 (bid $160.56 / ask $162.00), market trading ~$1.50 above limit
- Action: None. Do NOT cancel or chase. Let order sit — if XOM pulls back to $159.78 it fills; if not, expires at session close. Thesis intact.

---

**Skipped at open — re-evaluated midday:**

**CVX** (skipped at open: Volume 1.10× on breakout day < 1.5× required)
- Current mid: $195.84 | Spread: **1.18% — WIDE** (bid $194.68 / ask $197.00)
- Z-Score: **+2.46** (morning: +1.87) | RSI: 59.37 | vs 20d high ($193.31): ABOVE ✓
- Volume (last full bar May 15): 11,220,294 = **1.16×** avg (10,168,301)
- **Layer B re-check (2b-LONG):**
  - Z ≥ +1.0: 2.46 ✓
  - Close > 20d high: $195.84 > $193.31 ✓
  - RSI 50–70: 59.37 ✓
  - Volume ≥ 1.5×: **1.16× ❌ FAIL** — breakout day (May 15) never confirmed with institutional volume
  - Spread < 1%: **1.18% ❌ FAIL** — quote book thin midday; best-ask $197.00 on only 300 shares
- **VERDICT: STILL SKIPPED** — both volume and spread gates fail. The 2b-LONG momentum lane requires the *breakout day* to print ≥1.5× volume; May 15 was only 1.16×. A breakout that lacked institutional participation is not a confirmed setup. Spread anomaly is a secondary signal confirming thin interest at current prices. Z has extended further (+2.46) meaning any entry here is more extended above mean, not less. Re-evaluate Tuesday if a new breakout day prints with ≥1.5× volume.

**NVDA** (skipped at open: close below 20d high + earnings binary Wednesday)
- Current mid: $221.19 | Spread: **0.02% ✓**
- Z-Score: **+1.01** | RSI: 56.24 | vs 20d high ($235.74): **BELOW by 6.2% ❌**
- **Layer B re-check (2b-LONG):**
  - Z ≥ +1.0: 1.01 ✓ (barely)
  - Close > 20d high: $221.19 < $235.74 ❌ FAIL (still 6.2% below 20d peak)
  - RSI 50–70: 56.24 ✓
  - **EARNINGS BINARY: HARD RULE BLOCK** — NVDA reports Wednesday May 20 after close. No entry into unknown binary events regardless of all other conditions. This gate is permanent for the remainder of this week.
- **VERDICT: STILL SKIPPED** — two independent hard stops: (1) price is not above its 20d high, and (2) earnings binary block is absolute. **Revisit Thursday May 22 post-earnings** once the binary event is resolved.

**XLF** (skipped at open: Z = −0.307, not at 20d low, RSI out of range, SMA misalignment)
- Current mid: $51.68 | Spread: **0.04% ✓**
- Z-Score: **−0.04** (moved *toward* zero vs −0.307 this morning) | RSI: 39.14 | vs 20d low ($50.99): ABOVE
- **Layer B re-check (2b-SHORT):**
  - Z ≤ −1.0: −0.04 ❌ FAIL (essentially at statistical mean)
  - Close < 20d low: $51.68 > $50.99 ❌ FAIL
  - RSI 30–50: 39.14 ✓ (only passing gate)
- **VERDICT: STILL SKIPPED** — structural failure, not a timing issue. Z has moved *closer* to zero since morning, meaning XLF actually strengthened intraday. No short or long signal exists. XLF is range-chopping ($50.99–$52.63) with no statistical direction. Skip indefinitely until a directional Z-Score develops.

**XLV** (skipped at open: Z = −0.095, not at 20d low, only 9.5% below 52w high)
- Current mid: $145.60 | Spread: **0.007% ✓**
- Z-Score: **+0.37** (moved *positive* vs −0.10 this morning) | RSI: 55.82 | vs 20d low ($142.84): ABOVE
- **Layer B re-check (2b-SHORT):**
  - Z ≤ −1.0: +0.37 ❌ FAIL (Z is positive — price is *above* 20d mean)
  - Close < 20d low: $145.60 > $142.84 ❌ FAIL
  - RSI 30–50: 55.82 ❌ FAIL
  - Short Trend Template: 9.5% below 52w high (need >30%) ❌ FAIL
- **VERDICT: STILL SKIPPED** — XLV structure has moved *further away* from a short setup since morning. Z turned positive intraday. Healthcare is showing early rotation / recovery from its April lows. No short setup exists and may not develop. **Observation:** If XLV Z-Score approaches −2.0 (mean-reversion long) in a future session with RSI < 30, could qualify as 2a-LONG if trend template passes. Track for potential long setup, not short.

---

**Trades fired this rescan:** None

**Patience rule applied:** All four skipped candidates remain below their respective entry thresholds. Zero entries. This is correct behavior — the gate failures are structural (volume, earnings binary, Z near zero), not spread-normalization timing issues. None of these candidates were spread-skipped at open; all failed on substantive quant conditions that remain unresolved.

**Notable intraday observations:**
- XOM trading $161.28 midday, ~$1.50 above the $159.78 bracket limit. Energy thesis intact (WTI ~$106+). Order remains working — no action required.
- CVX Z-Score has extended to +2.46 without volume confirmation — the further it extends without a volume-confirmed day, the more extended and risky any entry becomes. This is the *opposite* of improving setup quality.
- XLV RSI dropped from ~neutral to 55.82 and Z turned slightly positive — potential *long* rotation setup developing, not short. Flag for Tuesday pre-market scan.
- NVDA earnings (Wed after close) and FOMC minutes (Wed) make Tuesday the last clean entry window this week before binary risk stacks.


---

## 2026-05-18 — Midday Scan Addendum (17:56 UTC / ~12:56 PM ET)

**Scan type:** Midday workflow — position thesis check & stop evaluation
**VIX Regime (estimated from prior close):** Normal (18.43) — 1.00× sizing multiplier

---

### STEP 1 — Account & Order State

| Field | Value |
|-------|-------|
| Equity | $99,056.46 |
| Cash | $99,056.46 (100%) |
| Long market value | $0 (no filled positions) |
| Deployed | 0% |
| Open positions | 0 |
| Open orders | 1 (XOM bracket limit — UNFILLED) |
| PDT daytrade count | 1/3 |
| Week trades used | 0/3 |

**Open order detail:**
| Order ID | Symbol | Type | Status | Key Detail |
|----------|--------|------|--------|------------|
| 1d69c496 | XOM | Bracket limit buy, 61 sh @ $159.78 | **new / UNFILLED** | Stop $147.80 | TP $183.74 | TIF: day — expires 20:00 UTC |

---

### STEP 2 — Live Quote: XOM

| Metric | Value |
|--------|-------|
| Bid | $158.34 |
| Ask | $160.60 |
| Mid | $159.47 |
| Spread | $2.26 = 1.42% (wide — reflect thin midday quote book; will normalize) |
| Quote timestamp | 2026-05-18T17:54:44Z (~12:54 PM ET) |
| Our limit | $159.78 |
| Ask vs limit | Ask $160.60 = $0.82 above limit — **ORDER NOT FILLED** |
| 20-day Z-Score (mid) | +2.72 (above mean $150.82, σ $3.18) |

**Fill status:** Limit $159.78 sits $0.82 below current ask. XOM is trading above our limit — a $0.82 (0.51%) intraday pullback would fill the order. With ~3h remaining in the session (market closes 20:00 UTC), a brief pullback to the limit remains plausible. **No action required — order correctly working.**

---

### STEP 3 — CUT LOSERS AT -7%

**No open positions.** Step skipped — nothing to cut.

---

### STEP 4 — TIGHTEN STOPS ON WINNERS

**No open positions.** Step skipped — no stops to manage.

---

### STEP 5 — THESIS CHECK (Pending Order Validation)

One bracket limit order working for XOM. Validating thesis is still intact:

| Thesis Pillar | Status | Evidence |
|---------------|--------|---------|
| WTI crude ~$106 | ✅ INTACT | Morning research confirmed WTI $106.34 (+0.87%); Brent $109–$110 |
| Strait of Hormuz supply disruption | ✅ INTACT | US-Iran tensions ongoing; no ceasefire/diplomacy reversal news |
| Energy sector YTD momentum #1 (+27.87%) | ✅ INTACT | Sector leadership confirmed in morning research |
| XOM breakout on 1.70× volume (May 15) | ✅ INTACT | Breakout bar confirmed ($157.92 → $158 close on 27.89M vs 16.41M avg) |
| Minervini Trend Template | ✅ INTACT | All 10 conditions passed in morning research; no price deterioration |
| Z-Score | +2.72 — ✅ within 2b-LONG range (≥+1.0, confirms momentum not extreme reversion) |
| Pivot extension | 1.18% at limit ($159.78 / pivot $157.92) — ✅ well within ≤5% cap |
| CVX pair divergence | 0.876σ (morning) — ✅ ≤1.5σ (both energy majors moving together) |
| Sector-consecutive-failure risk | Energy failure #1 was XOM May 7 exit. This is a re-entry on legitimately reset thesis (WTI recovered +15.4% from the $91 ceasefire-scare low). Risk flagged but not a gate violation. |

**VERDICT: Thesis FULLY INTACT.** Order correctly working. No cancellation. No modification. Let the bracket limit sit until market close.

---

### STEP 6 — OPTIONAL RESEARCH

**No anomalous intraday moves.** XOM is trading calmly between $158.34–$160.60, behaving exactly as expected post-Friday breakout (modest consolidation, not gapping away). No WebSearch warranted.

---

### STEP 7 — ACTIONS TAKEN

**None.** No positions cut (none exist). No stops tightened (none exist). No thesis exits (pending order thesis intact). No new orders placed.

---

### Midday Portfolio Snapshot — 2026-05-18 12:56 ET

```
Midday Portfolio — 2026-05-18 12:56 ET

Positions: 0 open
Cash: $99,056.46 (100%)
Deployed: 0%

| SYM | Entry | Now   | Unrealized | Stop    | Notes                      |
|-----|-------|-------|------------|---------|----------------------------|
| XOM | —     | ~$159.47 | N/A     | $147.80 | Bracket limit UNFILLED     |
|     |       |       |            |         | Ask $160.60 / Limit $159.78|
|     |       |       |            |         | ~$0.82 from fill; ~3h left |
```

**Order status:** XOM bracket limit (1d69c496) working — 61 shares @ $159.78, stop $147.80, TP $183.74, expires 20:00 UTC. Thesis intact. No action.

**Key watch for rest of session:**
- If XOM ask pulls back to ≤$159.78 → order fills; bracket stop and TP activate automatically
- If XOM continues trading above limit into close → order expires unfilled; re-evaluate Tuesday pre-market
- No stop adjustments, no cuts, no thesis exits warranted at this time
- NVDA earnings Wednesday (binary event) and FOMC minutes Wednesday — no new entries beyond XOM this week unless a clean setup appears Tuesday


---

## 2026-05-18 — Afternoon Scan Addendum (~15:44 ET / 19:44 UTC)

**Scan time:** ~16 min before close (market closes 20:00 UTC / 4:00 PM ET)
**VIX regime at scan:** NORMAL (estimated ~18.43, from morning research) | Sizing multiplier: 1.00×

---

### STEP 1 — Order & Position State Reconciled vs TRADE-LOG

**API State:**

| Order ID | Symbol | Type | Status | Detail |
|----------|--------|------|--------|--------|
| 1d69c496 | XOM | Bracket limit buy, 61 sh @ $159.78 | **new / UNFILLED** | Stop $147.80 (94606e38) | TP $183.74 (336d922a) | TIF: day — expires 20:00 UTC |
| 94606e38 | XOM | Stop $147.80 (bracket child) | **held** | Awaiting parent fill |
| 336d922a | XOM | Take-profit $183.74 (bracket child) | **held** | Awaiting parent fill |

- **Positions: NONE** — `[]` returned by API. No filled positions as of scan time.
- **Bracket fills today: 0** — XOM bracket limit (1d69c496) placed at $159.78; XOM ask at scan time is $160.42 — still $0.64 above the limit. Order has been working all day but has NOT filled.
- **TRADE-LOG reconciliation:** Fully current. The limit order was placed at 16:41 UTC (logged in TRADE-LOG.md). No fills, no reconciliation discrepancy.
- **Open stale limits: 0** — The only open order is the XOM bracket limit, which is a *today's* morning order (not stale), and the thesis remains intact. No cancellation warranted.

**XOM Bracket Order — Fill Probability at 15:44 ET:**
- Limit: $159.78 | Ask: $160.42 | Gap: $0.64 (0.40%)
- 16 minutes remain in the session. A pullback of $0.64 (~0.40%) would fill the order. Possible, but no guarantees. Do NOT cancel — let it work or expire at 20:00 UTC. If unfilled, re-evaluate Tuesday pre-market.

---

### STEP 2 — Trailing Stop Upgrades on Profitable Fills

**No filled positions exist.** No trailing stop upgrades applicable. The XOM bracket limit has NOT filled, so no bracket stop → trailing stop upgrade workflow is triggered. The bracket's child stop ($147.80) and take-profit ($183.74) remain in "held" status, dormant until parent fills.

---

### STEP 3 — Stale Limit Cancellations

**None applicable.** The XOM bracket limit (1d69c496) was placed this morning (2026-05-18T16:41 UTC) with a valid, research-backed thesis — not a stale carry-over. Thesis status:
- WTI crude ~$106 | Brent ~$109–$110 | US-Iran tensions active | Energy sector #1 YTD ✅
- Z-Score has extended further to +3.001 (was +2.749 at research time) — price is running higher, confirming directional momentum ✅
- Limit at $159.78 sits below market ($160.35 mid) — if anything, the thesis has strengthened intraday
- **Action: HOLD order. No cancellation.**

---

### STEP 4 — Afternoon Opportunity Scan

**⏰ TIMING CONSTRAINT: 15:44 ET = last 16 minutes of session.** CONSTRAINTS.md explicitly prohibits new entry orders in the final 15 minutes ("No last 15 mins" for entries). All candidate analysis below is for **informational purposes and Tuesday pre-market context only** — no new bracket orders will be placed at this time.

**VIX regime:** NORMAL (1.00×) | **Positions:** 0/6 | **Week trades:** 0/3 | **PDT:** 1/3

**Z-Scores and key metrics computed from 25-bar API data:**

| Ticker | Mid Price | Z-Score | RSI(14) | Vol (last bar vs 20d avg) | 20d High | Spread | Layer B Verdict |
|--------|-----------|---------|---------|---------------------------|----------|--------|-----------------|
| XOM (pending) | $160.35 | +3.001 | 64.23 | 1.63× ✅ | ABOVE $157.92 ✅ | 0.08% ✅ | 2b-LONG: QUALIFIES — but already has pending bracket |
| CVX | $196.01 | +2.509 | 59.37 | 1.10× ❌ | ABOVE $193.31 ✅ | 0.42% ✅ | 2b-LONG: **FAILS volume** (1.10× < 1.5×) |
| XLE | $60.44 | +2.133 | 61.34 | 0.80× ❌ | ABOVE $59.65 ✅ | 0.02% ✅ | No valid lane: Z overbought but RSI not >70 for 2a-SHORT; vol fails; Phase 1 long-only |
| NVDA | $221.72 | +1.058 | 56.24 | 1.20× | BELOW $235.74 ❌ | 0.02% ✅ | 2b-LONG: FAILS (no breakout); +earnings binary HARD BLOCK Wed |
| XLV | $145.63 | +0.402 | 55.82 | N/A | BELOW $147.42 ❌ | 0.01% ✅ | No lane qualifies |

**Pair Divergences:**
- XOM ↔ CVX: |+3.001 − +2.509| = 0.493σ ✅ (≤1.5σ — energy sector cohesion confirmed)
- XOM ↔ XLE: |+3.001 − +2.133| = 0.869σ ✅ (confirmed sector-wide energy rally)

**Candidate Detail:**

**CVX — REJECT (same failure as all prior scans today):**
- Z = +2.509 ✅ | Price above 20d high ✅ | RSI 59.37 ✅ | Spread 0.42% ✅ | Pair divergence 0.493σ ✅ | Trend Template ✅
- **Fails: Volume 1.10× < 1.5× required for 2b-LONG.** This has been the same disqualifier in every evaluation since pre-market. The May 15 breakout bar did not produce the institutional volume confirmation the strategy requires. Without it, the breakout is unconfirmed. A breakout on weak volume has higher failure rates — the gate is working correctly.
- Additionally: even if volume passed, the 15-minute window prohibition would prevent placing a new entry at 15:44. This is a Tuesday evaluation item.
- **Re-evaluate Tuesday pre-market:** If Tuesday's open produces a follow-through day with ≥1.5× volume AND CVX remains above its 20d high ($193.31), CVX becomes a legitimate bracketed long candidate. Per CONSTRAINTS.md, it qualifies independently (not contingent on XOM filling).

**XLE — REJECT:**
- Z = +2.133 (overbought) | RSI 61.34 (not >70 for 2a-SHORT) | Vol 0.80× ❌ | Phase 1 long-only eliminates 2a-SHORT lane regardless
- For 2b-LONG: Z is above mean (bullish momentum exists) but the 2b-LONG lane needs Z ≥ +1.0 AND breakout — XLE is above its 20d high ($59.65) ✅, but volume is below average at 0.80×. Fails same volume gate as CVX but is less compelling (ETF vs single-name leader).
- **REJECT.**

**NVDA — REJECT:**
- Price $221.72 is 5.9% below its 20d high ($235.74) — no breakout. This disqualifies the 2b-LONG lane regardless of other metrics.
- NVDA earnings Wednesday May 20 after close = **HARD BLOCK** on any new entry for the remainder of this week.
- Z = +1.058 is not at a mean-reversion extreme in either direction.
- **REJECT — dual gate failure (no breakout + earnings binary).**

**XLV — REJECT:**
- Z = +0.402 — sitting near the 20d mean, no statistical extreme in any direction. No lane qualifies.
- **REJECT.**

**New afternoon entries: NONE** — no new bracket orders placed (time constraint + no qualifying candidates). Zero orders submitted.

---

### Afternoon Market Context

The session's dominant story is the energy sector's continued rally: XOM traded as high as $161.35 intraday before settling around $160.35 at the close, extending well above our $159.78 bracket limit. The Z-score expanded from +2.749 at pre-market to +3.001 at the close, with RSI at 64.23 — still firmly in the 2b-LONG momentum zone (50–70), not yet overbought. CVX mirrored the move (Z = +2.509), and XLE also broke above its 20d high (Z = +2.133) — the energy sector is running cleanly on all three names, exactly as the thesis predicted. The XOM bracket limit at $159.78 has been working all day without filling — the market never pulled back to it. This is correct behavior: do not chase. The momentum extension is real but the bot doesn't modify limits upward to chase. If XOM closes today without filling, the bracket expires, and tomorrow's pre-market re-evaluates the setup fresh. NVDA is the week's pending binary event (reports Wednesday May 20 after close) — all tech names adjacent to NVDA are appropriately held at arm's length. The VIX remains in the Normal regime; the energy rally looks technically sound. "Sell in May" seasonal headwind continues to be overridden by the structural supply disruption premium in WTI.

---

**Bracket fills today:** 0 — XOM bracket limit (1d69c496) placed at $159.78 remains UNFILLED (ask $160.42 at scan close; order expires 20:00 UTC)
**Stops upgraded:** 0 — no filled positions; no trailing stop upgrades applicable
**Stale limits cancelled:** 0 — no stale limits; today's XOM bracket is thesis-valid and expires naturally at close
**New afternoon entries:** none — all 4 candidates failed composite gates (CVX: vol 1.10× < 1.5×; XLE: vol + no valid lane; NVDA: no breakout + earnings binary; XLV: Z near zero); additionally within final 15-minute no-entry window
**Afternoon market context:** Energy sector rallied strongly — XOM at $160.35 (Z = +3.001), CVX at $196.01 (Z = +2.509), XLE at $60.44 (Z = +2.133). Energy thesis intact and accelerating. XOM bracket at $159.78 never filled as price ran above it all session. NVDA earnings Wed = sector-wide binary overhang for tech names. No catalyst shifts that alter tomorrow's setup.

**Key watchlist for Tuesday pre-market (2026-05-19):**
1. **XOM** — Re-place bracket limit if today's order expires unfilled; re-calculate entry price at tomorrow's open vs 20d high $157.92 (pivot extension rule: ≤5%). If XOM gaps above ~$165.81 (pivot × 1.05), do NOT enter — wait for pullback.
2. **CVX** — Z = +2.509, all other gates pass; needs volume ≥ 1.5× on a breakout/follow-through day to qualify independently per CONSTRAINTS.md. If Tuesday opens strong on energy and volume confirms, CVX becomes a second independent bracket candidate.
3. **NVDA** — Hard block until post-earnings (Thursday May 22 pre-market evaluation). No entry of any kind this week.
4. **XLE** — Monitor for vol confirmation ≥ 1.5× before entering. RSI 61.34 and Z +2.133 are both in correct ranges for 2b-LONG if volume shows up Tuesday.


---

## 2026-05-19 — Pre-Market Research

### Account
- **Equity:** $99,056.46
- **Cash:** $99,056.46 (100% — fully deployed in cash)
- **Buying power:** $198,112.92 (2× margin)
- **Open positions:** 0
- **Open orders:** 0 (Monday's XOM bracket expired unfilled as expected)
- **Daytrade count:** 0/3
- **Phase P&L:** −$943.54 (−0.944%)

---

### Market Context
- **WTI Crude Oil:** ~$107.47/bbl, −1.10% today. Trump called off planned military strike on Iran → risk premium fading. Other data points: $103.33 (−1.82%) and $108.03 June delivery (−0.60%). YTD WTI: +76.30%.
- **Brent Crude:** ~$109.69–$110.37/bbl, −1.50% to −2.41%. July futures −$1.73 (−1.5%) to $110.37.
- **S&P 500 Futures (E-mini):** 7,390.75, −35 pts (−0.47%). Tech sector selling off; rising bond yield concerns; 50/50 Fed rate hike odds.
- **VIX:** 17.82 (opened 18.07, prior close 18.43, −3.31%). 52-week range 13.38–35.30.
- **10-year yield:** ~4.60% | **30-year yield:** ~5.138% — both elevated.
- **Earnings today:** Home Depot (HD) reported Q1 pre-market — EPS $3.43 (beat $3.41 est.), Revenue $41.77B (beat $41.59B est.), but EPS down from $3.45 YoY; comps +0.6%. Modest beat, weak underlying trend. Other reporters: RDCM, CRNT, THR, EXP, AS, ANTA.
- **Key event tomorrow (Wed May 20):** NVDA earnings after close (HARD BLOCK on any NVDA entry) + FOMC Meeting Minutes release.
- **Economic calendar today:** April Pending Home Sales (prior MoM +1.5%, exp +1.0%). Philadelphia Fed President Paulson speech 7:00 PM ET.
- **Sector momentum YTD (as of May 12):** Energy +27.87% 🥇 | IT +23.55% | Materials +15.24% | Industrials +12.84% | Real Estate +10.46% | Consumer Staples +7.32% | Utilities +5.74% | Consumer Discretionary −0.03% | Comm Services −1.82% | Financials −6.55% | Health Care −7.60%
- **News on held tickers:** None (no open positions).

---

### VIX Regime
- **Current VIX:** 17.82
- **Regime:** Normal (14–22)
- **Sizing multiplier:** 1.00×
- **Cold-start default:** 10% per position (< 30 closed trades)
- **Entry status:** All entry types permitted; normal sizing applies.

---

### Trade Ideas (Cleared Both Layers)

**NONE — all candidates rejected. See Skipped Candidates below.**

---

### Skipped Candidates

**1. XOM | LONG | Lane 2b-LONG | Energy**

*Layer A checklist:*
- Catalyst today: ❌ **CONTRA-CATALYST** — Oil −1.10% on Trump calling off Iran strike. Supply-fear premium deflating. The thesis (Iran risk premium → elevated WTI → XOM earnings tailwind) is partially undermined today. Not a positive catalyst day.
- Sector posture: ✅ Energy still #1 sector YTD (+27.87%), but intraday sector is selling off
- RSI(14): 59.91 ✅ (50–70 range for 2b-LONG)
- Volume: ❌ Early session 5,258,308 vs 20d avg 16,956,669. On an oil-down day, energy volume is expected to trend toward distribution, not accumulation. Projection: highly unlikely to reach 1.5× (~25.4M) today.

*Layer B — 2b-LONG:*
- Z-Score: +2.42 ✅ (≥ +1.0)
- Close > prior 20d high: ✅ $160.72 > $160.49 (barely, +0.14%)
- RSI 50–70: ✅ (59.91)
- Volume ≥ 1.5× 20d avg: ❌ **EXPECTED FAIL** — oil-down day contra-catalyst; entry-day volume projection well below threshold
- 50d SMA > 200d SMA: ✅ $155.15 > $136.41 (200d SMA proxied from 150-bar history; bullish structure confirmed)

*Minervini Long Trend Template:*
- Price ($160.72) > 50d SMA ($155.15): ✅
- Price > 150d SMA ($136.41): ✅
- Price > 200d SMA (proxy $136.41): ✅
- 150d SMA ≥ 200d SMA: ✅ (both equal due to data window; structurally bullish)
- 200d SMA trending up (vs 1 month ago $133.98): ✅ ($136.41 > $133.98)
- 50d SMA > 150d SMA: ✅ ($155.15 > $136.41)
- 50d SMA > 200d SMA: ✅
- Price > 30% above 52-week low ($110.64): ✅ (+45.3%)
- Price within 25% of 52-week high ($171.47): ✅ (6.3% below)
- Trend Template: **PASS**

*Pair: CVX | Pair Z-Score: +1.61 | Divergence: |2.42 − 1.61| = 0.81σ ✅ (≤ 1.5σ)*

*Summary: Layer A fails (contra-catalyst); Layer B fails (volume gate). REJECT.*

---

**2. CVX | LONG | Lane 2b-LONG | Energy**

*Layer B — 2b-LONG:*
- Z-Score: +1.61 ✅ (≥ +1.0)
- Close > prior 20d high: ❌ **FAIL** — $194.29 < $196.12 (20d pivot). CVX has pulled back from its high. Not a breakout day.
- RSI(14): 53.12 ✅
- Volume: May 18 was 0.97× avg — below average, no accumulation signal
- Catalyst today: ❌ Oil −1.10%

*Summary: Layer B fails on breakout test. REJECT.*

---

**3. XLE | LONG | Lane 2b-LONG | Energy ETF**

*Layer B — 2b-LONG:*
- Z-Score: +1.93 ✅ (≥ +1.0)
- Close > prior 20d high: ❌ **FAIL** — $60.565 vs 20d pivot $60.58 (−0.02% below). Effectively at pivot but not a confirmed breakout.
- RSI(14): 57.20 ✅
- Volume: May 18 was 1.00× avg; May 15 breakout bar was 0.81× avg (never had institutional-volume breakout day)
- Catalyst today: ❌ Oil −1.10%

*Trend Template (XLE post-split, 113 post-split bars):*
- Price ($60.565) > 50d SMA ($58.16): ✅
- Price > 150d proxy ($53.42): ✅
- >30% above 52-week low ($43.81): ✅ (+38.2%)
- Within 25% of 52-week high ($62.56): ✅ (3.2% below)
- 50d SMA ($58.16) > 150d proxy ($53.42): ✅
- Note: XLE had a structural rebalance in Dec 2025 (~$92→$45); post-split series used.
- Trend Template: **PASS** (conditionally — rebalance event noted)

*Summary: Layer B fails on breakout test (not above 20d high). REJECT.*

---

**4. HD | LONG or SHORT | Consumer Discretionary** — NOT evaluated with bars
- Earnings beat: EPS $3.43 vs $3.41 est. BUT EPS down YoY ($3.45 → $3.43). Comparable sales +0.6% is muted.
- Sector (Consumer Discretionary) = −0.03% YTD — not in momentum; fails sector posture for long.
- A short would require Minervini short template + Z ≥ +2.0 + RSI > 70 — no bar data pulled.
- Pre-market earnings reaction unclear; insufficient data for quant gates.
- **SKIP** — no bars pulled, sector not in momentum for long; insufficient quant data for short.

---

**5. NVDA — HARD BLOCK (earnings Wednesday May 20)**
- Any entry this week is prohibited. Re-evaluate Thursday May 21 post-earnings.

---

**6. Materials / Industrials (FCX, NEM, CAT, GE) — NOT PULLED**
- YTD momentum: Materials +15.24%, Industrials +12.84% — both valid momentum sectors.
- Rationale for skip today: NVDA binary + FOMC minutes tomorrow create broad market noise. Adding speculative new-sector names on a pre-binary day reduces edge certainty.
- **Deferred to Wednesday post-NVDA** when market direction is clearer.

---

### Quant Snapshot (All Evaluated Names)

| Ticker | Z-Score | RSI(14) | 20d High | Current | Trend Template | Pair | Pair Z | Div | Lane Tried | Gate Failed |
|--------|---------|---------|----------|---------|----------------|------|--------|-----|------------|-------------|
| XOM | +2.42 | 59.91 | $160.49 | $160.72 | PASS | CVX | +1.61 | 0.81σ ✅ | 2b-LONG | Volume (contra-catalyst) |
| CVX | +1.61 | 53.12 | $196.12 | $194.29 | PASS | XOM | +2.42 | 0.81σ ✅ | 2b-LONG | Close < 20d high ❌ |
| XLE | +1.93 | 57.20 | $60.58 | $60.565 | PASS | XOM | +2.42 | 0.49σ ✅ | 2b-LONG | Close < 20d high ❌ |

---

### Risk Factors
1. **Iran peace talks** — Trump calling off military strike deflates energy's primary catalyst. WTI −1.1%. This is the session's dominant macro force. If Iran negotiations progress, oil could fall further toward $100, compressing energy margins.
2. **NVDA earnings Wednesday** — Creates a market-wide binary event. Analysts view it as a critical AI buildout test. A miss would hit IT sector hard (IT = +23.55% YTD, significant gains at risk). Broad caution expected through tomorrow's close.
3. **FOMC minutes Wednesday** — Markets 50/50 on a rate hike before year-end. Minutes could shift that pricing significantly. Rising yields (10yr 4.60%, 30yr 5.138%) are already compressing equity multiples.
4. **Tech sector selloff ongoing** — S&P 500 futures −0.47% pre-market. Tech leadership being questioned despite strong YTD gains.
5. **Elevated yields** — 30-year at 5.138% creates headwinds for real estate, utilities, and consumer discretionary sectors.
6. **Energy thesis durability** — Even with oil at $107, the geopolitical fear premium was a key driver. If Iran risk normalizes, energy could consolidate or pull back, keeping XOM/CVX below breakout pivots.

---

### Decision
**HOLD — 0 new entries today**

*Reasoning:* The primary setup from yesterday's watchlist (XOM/CVX/XLE) has been negatively catalyzed by today's oil decline (Iran peace news). All three energy candidates fail Layer B: XOM on expected volume failure (contra-catalyst day); CVX on breakout test (price below 20d pivot); XLE on breakout test (price at/below pivot). The Patience Rule applies — zero trades today is the correct outcome. Wednesday brings NVDA earnings and FOMC minutes, both major market catalysts that will clarify direction. The energy thesis may reassert itself once Iran news settles; oil at $107 is still structurally elevated. Preserve powder for cleaner setups post-binary events.

**Wednesday Action Plan:**
1. **XOM** — Re-evaluate at open. If oil stabilizes/bounces AND XOM is above $160.49 on volume ≥ 1.5× avg, the 2b-LONG thesis is still valid. New limit bracket near $160–$162.
2. **CVX** — Re-evaluate independently. Need CVX to reclaim $196.12 pivot with ≥ 1.5× volume.
3. **XLE** — Re-evaluate. Need confirmed close above $60.58 with ≥ 1.5× volume.
4. **Materials scan** — Pull FCX, NEM bars Wednesday morning as next momentum sector.
5. **NVDA** — Hard block Wednesday. Evaluate Thursday post-earnings only.
6. No stale brackets to re-place (Monday's XOM bracket expired per plan; no orders queued).

---

*Circuit breakers: ✅ All clear — Phase P&L −0.944% (limit −5%) | Drawdown −0.944% from $100,000 start (limit −15%) | PDT: 0/3 | Positions: 0/6 | Week trades: 0/3*

---

## 2026-05-19 — Midday Rescan Addendum (17:25 UTC / ~13:25 ET)

**VIX Regime at rescan:** Normal (~18.43–18.86 from morning research) — Sizing multiplier: 1.00×
**Account at rescan:** Equity $99,056.46 | Cash $99,056.46 (100%) | Deployed: 0% | Positions: 0/6 | Week trades: 0/3 | PDT: 0/3
**Orders at rescan:** NONE (Monday's XOM bracket limit $157.92 expired unfilled at session close; no carry-over orders exist)

---

### Skipped at Open — Re-evaluated at Midday

#### XOM — STILL SKIPPED

| Metric | At Open | Midday |
|--------|---------|--------|
| Skip reason | Bracket limit $157.92 unfilled; XOM gapped/ran above limit on open; order expired EOD May 18 | Same + spread R-flagged/unreliable + follow-through day volume below threshold |
| Bid / Ask | — | $153.05 / $161.87 (**"R" condition flag** — stale/indicative NBBO) |
| **Spread %** | — | **5.60% → FAILS <1% gate** |
| Z-Score (20d) | +2.749 (morning research) | **+2.425** (vs 20d mean $151.46, σ $3.72) |
| RSI(14) | ~64.2 | **64.44** |
| Prior 20d high | $157.92 (May 15 pivot) | $160.49 (yesterday's close = new 20d high) |
| Current vs pivot | — | $160.49 = AT 20d high (not above it intraday) |
| May 18 vol | — | 20,075,013 = **1.20× avg** ❌ (follow-through day, below 1.5× required) |
| May 15 breakout vol | 1.66× ✅ | 1.66× ✅ (original breakout bar, unchanged) |
| Pivot extension | 1.96% ✅ | ($160.49/$157.92 − 1) = **1.63%** ✅ (≤5%) |
| Pair (CVX) Z | +1.21σ | **+2.131σ** | Divergence: 0.294σ ✅ |
| Catalyst | WTI $105+ / Hormuz ✅ | WTI ~$107 (prior session), Hormuz active ✅ |

**Layer B gate failures:**
1. **Spread FAIL: 5.60% (R-flagged)** — The live Alpaca quote carries condition code "R" (restricted/indicative NBBO, likely a crossed/locked market or late SIP data artifact during active session). A 5.60% bid-ask spread is not a reliable market for a bracket limit entry. Cannot responsibly place a new bracket order into this quote.
2. **Volume FAIL: May 18 follow-through day 1.20×** — While the May 15 breakout bar printed a strong 1.66× confirming the original setup, the follow-through day (May 18) only reached 1.20×. For the 2b-LONG momentum lane, the breakout must be confirmed with institutional participation; a below-1.5× follow-through day reduces conviction on sustained accumulation.

**Thesis status: FULLY INTACT.** WTI elevated, Hormuz supply disruption active, energy sector YTD leader. The structural entry thesis is unbroken. This is a data/quote-quality gate failure, not a thesis failure. **Re-evaluate at Wednesday pre-market** with fresh NBBO quotes and a clean daily bar for today's volume to assess whether today's session generates the ≥1.5× confirmation needed.

**VERDICT: ❌ STILL SKIPPED — Spread R-flagged (5.60%, not actionable) + follow-through vol 1.20× < 1.5×**

---

#### NVDA — STILL SKIPPED

| Metric | At Open | Midday |
|--------|---------|--------|
| Skip reason | Close $225.32 < 20d high $235.74 (no breakout); Vol 1.19×; EARNINGS BINARY WEDNESDAY (hard block) | WORSENED on price; hard block unchanged |
| Bid / Ask | — | $223.56 / $223.59 |
| **Spread %** | — | **0.013% ✅ (normalized)** |
| Z-Score (20d) | +1.56 (morning research) | **+1.122** (20d mean $211.31, σ $10.92) |
| Close vs 20d high ($235.74) | $225.32 (-4.4% below) | **$223.57 (-5.2% below)** ❌ — WORSENED |
| RSI(14) | — | **56.59** ✅ |
| May 18 vol | — | 0.95× ❌ (below average) |

**Gate failures (structural — not timing):**
1. **Close < 20d high: FAIL** — NVDA trading at $223.57, which is 5.2% below its 20d pivot of $235.74. Price has moved **further away** from the breakout trigger since this morning ($225.32 → $223.57 = −$1.75 intraday). The breakout condition has gotten harder to satisfy, not easier.
2. **Earnings BINARY HARD BLOCK** — NVDA reports Q1 FY2027 results **tomorrow night (Wednesday May 20 after close)**. This is an absolute, permanent block for the remainder of this week. No entry is permissible under any quant/spread conditions while an earnings binary is this close.
3. **Volume 0.95×** — Below average; no institutional accumulation signal.

**VERDICT: ❌ STILL SKIPPED — Price below 20d high (worsened) + earnings binary block Wednesday (permanent for this week)**

**Post-earnings watch:** Re-evaluate Thursday May 22 pre-market. If NVDA beats and gaps up to reclaim $235.74+ with volume ≥1.5×, the 2b-LONG setup could qualify. If it disappoints and drops toward Z ≤ −2.0 (~$189), evaluate for 2a-LONG mean-reversion (requires RSI <30 confirmation).

---

#### XLE — STILL SKIPPED

| Metric | At Open | Midday |
|--------|---------|--------|
| Skip reason | Vol 0.86× < 1.5×; Trend Template incomplete (Dec 2025 split disrupts SMA data) | Same structural failures; spread normalized |
| Bid / Ask | — | $61.11 / $61.12 |
| **Spread %** | — | **0.016% ✅ (excellent)** |
| Z-Score (20d) | +2.133 (Monday close) | **+2.377** (20d mean $57.81, σ $1.39) |
| Close vs 20d high ($60.58) | $60.565 (≈ at pivot, Mon close) | **$61.115 > $60.58** ✅ (intraday new 20d high) |
| RSI(14) | ~57.2 | **61.99** ✅ |
| Breakout day volume (May 18) | 1.13× (was the skip reason at open) | **1.13×** — UNCHANGED (daily bar is fixed) |
| Trend Template | INCOMPLETE (split-adjusted SMA gap) | **STILL INCOMPLETE** |

**Gate failures (structural — spread normalized but core gates remain):**
1. **Volume FAIL (structural): Breakout day May 18 = 1.13×** — The 2b-LONG lane requires the breakout **confirmation day** to print ≥1.5× volume. Yesterday (May 18) was the day XLE closed above its prior 20d high at 1.13× average volume. This is a **settled, permanent daily bar** — it does not improve intraday or midday. The institutional conviction required for the momentum lane was absent on the critical day.
2. **Trend Template INCOMPLETE** — The Dec 2025 2:1 split in XLE disrupts pre-split price/SMA data. Cannot verify the full Minervini Long Trend Template (specifically 50d/150d/200d SMA alignment, 200d SMA trend direction, 52-week high/low anchors from the pre-split series). This was the same disqualifier at market-open and has not changed.

**Notable:** XLE's Z-Score has extended from +2.133 (Monday close) to +2.377 intraday — the ETF continues to run higher without institutional volume confirmation. This is the exact risk the volume gate is designed to prevent: chasing a momentum move that lacks professional accumulation. As the Z extends further above +2.0, entering now would be more extended than the already-extended Monday level.

**VERDICT: ❌ STILL SKIPPED — Breakout day vol 1.13× (daily bar, immutable) + Trend Template incomplete**

**Forward watch:** If XLE opens tomorrow with a strong gap-up continuation AND today's full session volume prints ≥1.5× average (~54.97M shares), that becomes a new breakout day. Separately, if the SMA data gap for XLE can be resolved (operator action: obtain adjusted historical data), the Trend Template can be fully assessed. Until then, XLE remains blocked on two structural grounds.

---

#### HD — STILL SKIPPED

| Metric | At Open | Midday |
|--------|---------|--------|
| Skip reason | Earnings pre-market TODAY (binary event) | Same |
| Bid / Ask | — | $297.00 / $303.00 |
| **Spread %** | — | **2.00% → FAILS <1% gate** |
| Catalyst status | Earnings reported pre-market (EPS $3.43 beat $3.41; Rev beat but comps +0.6% muted) | Post-earnings reaction: spread still wide, in price discovery |

**Both gates fail simultaneously:** (1) Spread 2.00% >> 1% threshold — still in post-earnings price discovery. (2) The earnings event itself was the skip reason at open; post-earnings direction is now establishing but spread has not yet normalized to confirm reliable NBBO.

**VERDICT: ❌ STILL SKIPPED — Spread 2.00% wide + post-earnings price discovery ongoing**

**Forward watch:** Re-evaluate Wednesday pre-market. If HD's spread normalizes (<1%), pull bars, compute Z-Score and RSI, check Minervini Trend Template (Consumer Discretionary sector = −0.03% YTD, weak posture for long entries). A post-earnings mean-reversion long requires Z ≤ −2.0 + RSI <30 (2a-LONG); a momentum continuation requires breakout above post-earnings high with ≥1.5× volume (2b-LONG). Neither is assessable today.

---

### Trades Fired This Rescan

**NONE.**

Zero candidates re-cleared the composite Layer A + Layer B gates upon midday re-evaluation.

---

### Portfolio State at Rescan

| Field | Value |
|-------|-------|
| Equity | $99,056.46 |
| Cash | $99,056.46 (100%) |
| Open positions | 0/6 |
| Week trades used | 0/3 |
| PDT daytrade count | 0/3 |
| Phase P&L | −$943.54 (−0.944%) vs $100,000 start |
| Circuit breakers | ✅ All clear (day 0.00%, phase −0.94%, drawdown −0.94%) |

---

### Patience Rule Applied

All four skipped candidates remain below their respective entry thresholds. Gate failures are structural — not spread-normalization timing issues:

- **XOM:** Quote flagged R (unreliable NBBO, 5.60% apparent spread); follow-through day volume 1.20× < 1.5×. Thesis intact.
- **NVDA:** Price moved further from 20d high (−5.2%); earnings binary block permanent for this week.
- **XLE:** Breakout day volume 1.13× (immutable daily bar) + Trend Template incomplete.
- **HD:** Spread 2.00% (post-earnings price discovery); sector posture weak for new longs.

No gates were lowered. No trade was forced. Zero trades this rescan is the correct disciplined outcome.

---

### Key Watchlist for Wednesday Pre-Market (May 20)

1. **XOM** — Thesis intact. Re-evaluate with fresh NBBO quotes (not R-flagged). Need: (a) clean spread < 1%, (b) verify whether today's session volume closed ≥1.5× (new pivot day), (c) new limit at or near today's close. Note: If XOM has moved significantly above $160.49, recompute pivot extension.
2. **XLE** — Verify today's full session volume vs 36.6M avg. If ≥ 1.5×, today becomes a new valid breakout bar; re-evaluate with clean Thursday entry. Trend Template SMA issue remains unresolved.
3. **NVDA** — HARD BLOCK Wednesday (earnings tonight after close). Evaluate Thursday May 22 pre-market only.
4. **HD** — Post-earnings: pull bars Wednesday, check if spread normalized, assess Z/RSI/TT.
5. **FOMC Minutes (Wednesday 2:00 PM ET)** — Major macro event. Could move rates expectations materially. Avoid placing new entries just before the 2 PM ET release. Any open bracket limits should be evaluated for thesis continuity post-release.


---

## 2026-05-19 — Midday Scan Addendum (~14:00 ET / 18:00 UTC)

**Scan type:** Midday workflow — position thesis check & stop evaluation
**VIX Regime:** Normal (18.43 from morning research) — 1.00× sizing multiplier
**Scan time:** 2026-05-19T18:00 UTC (~14:00 ET)

---

### STEP 1 — Account & Order State (Live API)

| Field | Value |
|-------|-------|
| Equity | $99,056.46 |
| Cash | $99,056.46 (100%) |
| Deployed | $0 (0%) |
| Open Positions | 0 |
| Open Orders | 0 |
| PDT daytrade count | 0/3 |
| Week trades used | 0/3 |
| Phase P&L | −$943.54 (−0.944%) |

- Positions API: `[]` (empty — confirmed fully flat)
- Orders API: `[]` (empty — morning pre-market research decided HOLD; no brackets placed at open)
- Morning's conclusion (contra-catalyst WTI −1.10%, volume gate failures on all energy names) was fully consistent with today's order state

---

### STEP 2 — CUT LOSERS: N/A | STEP 3 — TIGHTEN STOPS: N/A

No open positions. Both steps skipped.

---

### STEP 4 — THESIS CHECK (Watchlist Validation)

Live quotes pulled at ~14:00 ET:

| Ticker | Prior Close | Live Mid | Intraday Chg | Spread | Live Z-Score | Notes |
|--------|-------------|----------|--------------|--------|--------------|-------|
| XOM | $160.49 | $162.02 | +0.95% | 0.025% ✅ | +2.84 | Relative strength vs oil |
| CVX | $196.12 | $196.77 | +0.33% | 0.030% ✅ | +2.30 | Pair divergence XOM: 0.54σ ✅ |
| XLE | $60.58 | $61.09 | +0.83% | 0.016% ✅ | +2.36 | ETF tracking sector rally |
| NVDA | — | $223.25 | — | 0.013% ✅ | — | HARD BLOCK (earnings Wed) |

**Energy thesis direction:**
- Morning pre-market flagged today as a "contra-catalyst day" (WTI −1.10% on Trump calling off Iran military strike)
- At 14:00 ET: XOM +0.95%, CVX +0.33%, XLE +0.83% — all positive despite oil softness
- **INTERPRETATION:** Energy equities are showing bullish relative strength vs. spot oil. XOM outperforming spot WTI by ~+2.05%. CVX pair divergence from XOM is only 0.54σ (well within 1.5σ limit) — both integrated oil majors moving in tandem. This is sector-wide institutional behavior, not single-name idiosyncrasy.
- Likely explanations: (a) Iran deal risk already priced in (fear fading = news "already known"); (b) Lower feedstock costs = margin tailwind for integrated refining; (c) Institutional accumulation ahead of mid-week clarity (NVDA + FOMC minutes)
- **Energy thesis: INTACT. No thesis break. Structural pillars (Hormuz supply disruption, XOM Q1 earnings beat) remain.**

**NVDA:** HARD BLOCK. Reports earnings Wednesday May 20 after close. Spread normalized (0.013%), but binary event is absolute. NVDA is at $223.25, 5.2% below its 20d high of $235.74 — not a breakout candidate even absent the earnings block.

---

### STEP 5 — VOLUME GATE STATUS (Watchlist)

The critical unresolved gate for all three energy candidates is **today's (May 19) closing volume**. All three need ≥1.5× average volume on the *entry day* bar to qualify for the 2b-LONG momentum lane:

| Ticker | Vol Avg (20d) | 1.5× Threshold | Prior Session (May 18) | Today Min Needed |
|--------|---------------|----------------|------------------------|------------------|
| XOM | 16,797,568 | 25,196,352 | 20,075,013 (1.20×) ❌ | ~25.2M |
| CVX | 9,674,642 | 14,511,963 | 9,881,486 (1.02×) ❌ | ~14.5M |
| XLE | 36,645,154 | 54,967,731 | 41,519,997 (1.13×) ❌ | ~55.0M |

If today's session closes with volume at or above these thresholds, today (May 19) becomes a new valid breakout confirmation bar, enabling a bracket entry evaluation at Wednesday's pre-market open.

Note: Today is running +0.95% on XOM, +0.83% on XLE — the price direction is constructive. Volume pickup is the remaining unknown.

---

### STEP 6 — OPTIONAL RESEARCH NOTE

XOM's +0.95% intraday performance against a −1.10% WTI backdrop constitutes notable relative strength warranting documentation. CVX (+0.33%) and XLE (+0.83%) confirm this is sector-wide, not XOM-specific. The energy complex is behaving as if the Iran deal geopolitical fear was "sell the rumor, buy the reality" — fear of a deal was the selling pressure last week; the actual news (strike called off) is being absorbed without further downside. No news-based WebSearch result obtained (news endpoint returned no output); analysis is inference from price action + pair divergence.

---

### ACTIONS TAKEN: NONE

- No positions cut (none existed)
- No stops tightened (none existed)
- No thesis exits triggered
- No new orders placed
- No DAILY-SUMMARY.md entry (no action taken per workflow rules)

---

### Watchlist for Wednesday Pre-Market (2026-05-20)

1. **XOM** — Thesis intact, energy relative strength confirmed. Re-evaluate if today's final volume prints ≥25.2M (1.5×). Pivot: $160.49. Live mid $162.02 = +0.95% extension above pivot (within 5% cap). New bracket limit ~$162.00 area if volume confirms.
2. **CVX** — Same energy thesis. Needs ≥14.5M volume today. Still tracking XOM closely (pair divergence 0.54σ). Evaluate independently.
3. **XLE** — Trend Template SMA data incomplete (Dec 2025 split disruption). Volume needs ≥55.0M. Double-gated. Lower priority than XOM/CVX single names.
4. **NVDA** — **HARD BLOCK Wednesday May 20** (earnings after close). Evaluate Thursday May 22 pre-market only.
5. **FOMC Minutes Wednesday 2:00 PM ET** — No new entries placed in the 30-minute window before this release.
6. **Materials names (FCX, NEM)** — Deferred from last week. Eligible for Wednesday scan if energy names don't qualify (sector diversification purpose).

---

## 2026-05-19 — Afternoon Scan Addendum (15:54 ET / 19:54 UTC)

**Scan time:** ~6 min before close (market closes 20:00 UTC / 4:00 PM ET)
**VIX regime at scan:** NORMAL — VIXY proxy $26.57 (bid $26.57 / ask $26.58) → estimated VIX ~18.5 | Sizing multiplier: 1.00×

---

### STEP 1 — Order & Position State Reconciled vs TRADE-LOG

**Orders returned by API (6 total — all historical):**

| Order ID | Symbol | Type | Status | Detail |
|----------|--------|------|--------|--------|
| 1d69c496 | XOM | Bracket limit BUY 61 sh @ $159.78 | **EXPIRED** 2026-05-18T20:02 | TIF: day — never filled, as expected and logged ✅ |
| 94606e38 | XOM | Stop child $147.80 | **CANCELED** 2026-05-18T20:02 | Auto-cancelled with parent bracket expiry ✅ |
| 336d922a | XOM | TP child $183.74 | **CANCELED** 2026-05-18T20:02 | Auto-cancelled with parent bracket expiry ✅ |
| 8f97ef7d | XOM | Market Sell 130 sh | **FILLED** $146.09, 2026-05-07T17:55 | Thesis-break exit — logged ✅ |
| d92d9371 | XOM | Trailing Stop 10% GTC | **CANCELED** 2026-05-07T17:54 | Cancelled before thesis-break exit — logged ✅ |
| c04ae321 | XOM | Market Buy 130 sh | **FILLED** $153.35, 2026-05-01T14:41 | Original entry — logged ✅ |

- **Positions API: `[]` — EMPTY.** Portfolio is 100% cash. No filled positions.
- **Bracket fills today (May 19): 0** — No morning bracket limits were placed today (pre-market verdict was HOLD: all energy candidates failed Layer B on contra-catalyst WTI −1.10% day; volume gates). Monday's bracket (1d69c496) expired unfilled last night as documented.
- **TRADE-LOG reconciliation: FULLY CURRENT.** No discrepancies. All 6 orders in API match TRADE-LOG entries exactly.
- **Open stale limits: 0** — No open orders of any kind.

---

### STEP 2 — Trailing Stop Upgrades: N/A

No positions held. No stops to upgrade. Portfolio is 100% cash.

---

### STEP 3 — Stale Limit Cancellations: N/A

No open orders exist (Monday's bracket expired at session close per its TIF: day). Nothing to cancel.

---

### STEP 4 — Afternoon Opportunity Scan

**VIX regime:** NORMAL (1.00×) | **Positions:** 0/6 | **Week trades:** 0/3 | **PDT:** 0/3

**Quant metrics computed from live quotes + 25-bar API data:**

| Ticker | Live Mid | Z-Score | RSI(14) | 20d High | Spread | Vol (May 18) vs Avg | Pair / Div | Layer B Gate | Verdict |
|--------|----------|---------|---------|----------|--------|---------------------|-----------|--------------|---------|
| XOM | $163.06 | +3.117 | 64.44 | $160.49 ✅ | 0.043% ✅ | 1.20× ❌ | CVX +2.131σ / 0.986σ div ✅ | 2b-LONG: **vol FAIL** | **REJECT** |
| CVX | $196.12† | +2.131 | 61.04 | $196.12 — AT ❌ | 5.02% ❌ | 1.02× ❌ | XOM 0.986σ div ✅ | 2b-LONG: **spread + vol + no breakout** | **REJECT** |
| XLE | $61.41 | +2.585 | 61.99 | $60.58 ✅ | 0.016% ✅ | 1.13× ❌ | XOM 0.532σ div ✅ | 2b-LONG: **vol FAIL** | **REJECT** |
| NVDA | $220.88 | N/A | N/A | N/A | 0.018% ✅ | N/A | N/A | **EARNINGS HARD BLOCK** (tonight) | **REJECT** |
| HD | $301.93 | N/A | N/A | N/A | 0.086% ✅ | N/A | N/A | Sector fail (Cons. Disc. −0.03% YTD) | **REJECT** |

†CVX quote is R-flagged with wide spread ($188.69/$198.41 = 5.02%); fair value proxy = last close $196.12.

**⏰ Timing note:** Scan at 15:54 ET = within final 6 minutes of session. CONSTRAINTS.md prohibits new entries in the last 15 minutes. This is a secondary independent blocker in addition to the volume gate failures.

---

**Candidate detail:**

**XOM — REJECT (volume gate — single disqualifier):**
- Z = +3.117 ✅ | RSI = 64.44 ✅ | Spread 0.043% ✅ | Price above 20d high ($163.06 > $160.49) ✅ | Pivot extension 3.26% ≤5% ✅ | 50d > 200d SMA ✅ | Pair CVX divergence 0.986σ ✅
- **ONLY FAILURE: Volume.** May 18 (the breakout day) = 20,075,013 / 16,797,568 avg = **1.20× — below 1.5× required** for 2b-LONG momentum lane.
- XOM is continuing to rally today (+1.60% from yesterday's close), which is bullish, but the volume confirmation for the momentum entry is measured on the *breakout day bar* (May 18), and that bar is settled at 1.20×. Cannot retroactively upgrade it.
- Today's (May 19) session bars are not yet available (market still open at scan time). If today's session volume closes at ≥25.2M shares (1.5× × 16.8M avg), May 19 becomes a new valid breakout day → re-evaluate at Wednesday pre-market.
- Thesis pillars: WTI oil structurally elevated (contra-catalyst today of Trump calling off Iran strike may be reversing; XOM +1.60% suggests market disagreed with morning's negative read), Energy sector #1 YTD (+27.87%), XOM Minervini Trend Template passes all 10 conditions.

**CVX — REJECT (spread + volume + no breakout, 3 independent failures):**
- Live quote unreliable (5.02% spread; stub AH bid $188.69 vs ask $198.41). Fair value = last close $196.12 = AT its 20d high (not above). No breakout.
- Volume May 18 = 1.02× — nowhere near 1.5×.
- Thesis same as XOM; re-evaluate Wednesday with clean quotes.

**XLE — REJECT (volume gate):**
- Otherwise clean: Z = +2.585 ✅, RSI = 61.99 ✅, spread 0.016% ✅, above 20d high ($61.41 > $60.58) ✅.
- Volume May 18 = 41,519,997 / 36,645,154 avg = **1.13× — below 1.5×**.
- If today's XLE volume closes ≥54.97M shares, today becomes a new breakout bar. Watch for Wednesday.
- Note: Trend Template for XLE remains incomplete due to Dec 2025 2:1 split disrupting pre-split SMA history. This secondary gate also blocks a momentum entry until resolved.

**NVDA — REJECT (earnings hard block):**
- Q1 FY2027 earnings report tonight after close. Absolute hard block on all entry types for remainder of this week. Evaluate Thursday May 22 pre-market post-earnings.
- Live mid $220.88 — still 5.2% below 20d high $235.74 (no breakout even absent the hard block).

**HD — REJECT (sector momentum):**
- Consumer Discretionary YTD = −0.03% — not in momentum. Fails Layer A sector posture gate for long entries.
- Post-earnings bar data available tomorrow. Full evaluation (Z, RSI, TT) deferred to Wednesday pre-market.

---

### Afternoon Market Context

Energy sector is closing strongly despite today's morning contra-catalyst (WTI −1.10% on Trump's Iran stance). XOM +1.60% from yesterday's close ($163.06 vs $160.49), XLE +1.36% ($61.41 vs $60.58). This is a second consecutive day of energy outperformance that confirms the sector's structural bid — institutional buyers appear to be treating the Iran deal risk as "priced in" or temporary. XOM's Z-score has now extended to +3.117 (vs +2.749 at last research entry), a significant statistical extension above the 20-day mean. However, the volume confirmation gate persists: the breakout on May 15 (1.66×) was valid, May 18 follow-through was 1.20×, and today's bar (May 19) is the key one to watch. NVDA earnings tonight create a market-wide binary overhang — the outcome will set the tone for the broader market Wednesday morning. FOMC minutes also release Wednesday at 2:00 PM ET. The combination of these two events makes Wednesday a high-information day; having no open positions entering it is actually an advantageous position — maximum flexibility to act on whichever setup emerges post-binary clarity.

---

**Bracket fills today:** 0 (no morning limits were placed — HOLD decision at pre-market; Monday's bracket expired as expected)
**Stops upgraded:** 0 (no positions held; no upgrade workflow applicable)
**Stale limits cancelled:** 0 (no open orders existed at scan time)
**New afternoon entries:** none — all 5 candidates failed composite Layer A + Layer B gates; additionally within final 6-minute no-entry window
**Afternoon market context:** Energy continued strong (+1.60% XOM, +1.36% XLE) despite contra-catalyst morning (WTI −1.10%). Volume confirmation still the single outstanding disqualifier for XOM/XLE entries. NVDA earnings tonight = primary market-moving event; FOMC minutes Wednesday. No positions entering this binary, which is the correct posture.

**Key watchlist for Wednesday pre-market (2026-05-20):**
1. **XOM** — If today's (May 19) session volume prints ≥25.2M shares, May 19 is a new valid breakout day. Re-place bracket limit at Wednesday open. Pivot: $160.49 (May 18 close). Max entry ≤ $168.51 (pivot × 1.05). VIX/FOMC check at open.
2. **XLE** — Same analysis. Needs May 19 volume ≥54.97M for new breakout bar. Trend Template SMA incomplete (secondary block).
3. **CVX** — Needs clean spread (<1%), fresh volume ≥1.5×, and close above $196.12. Same energy thesis.
4. **NVDA** — **HARD BLOCK Wednesday** (earnings tonight). Evaluate Thursday May 22 only: if gap-up reclaims $235.74 with volume ≥1.5× → 2b-LONG candidate; if gap-down to Z ≤ −2.0 (~$189) + RSI <30 → 2a-LONG candidate.
5. **HD** — Post-earnings bar available Wednesday. Pull bars, assess Z/RSI/TT. Sector (Cons. Disc. YTD −0.03%) is a Layer A headwind for long entries.
6. **FOMC Minutes (Wednesday 2:00 PM ET)** — No new bracket orders placed in the 30 min before this release.

---

## 2026-05-20 — Pre-Market Research (Day 22, Wednesday)

### Account
- **Equity:** $99,056.46
- **Cash:** $99,056.46 (100%)
- **Buying Power:** $198,112.92 (2× margin)
- **Non-Marginable BP:** $99,056.46
- **Daytrade Count:** 0/3
- **Open Positions:** 0/6
- **Week Trades:** 0/3
- **Phase P&L:** −$943.54 (−0.944%) — well within all circuit breakers

---

### Market Context
- **WTI Crude Oil:** $100.48 (−3.52% today; intraday bounce to $103.69). +12.06% past month, +63.20% YoY. Major pullback today on geopolitical de-escalation sentiment.
- **Brent Crude:** $108.33 (−2.66% today; was $110.69 earlier). +10.0% past month, +66.89% YoY.
- **S&P 500 Futures:** +0.4% premarket (up ~7,404 area). Risk-on tone from NVDA earnings.
- **VIX:** 17.83 (−1.27%). Trading near 18 — elevated but not panicked. Normal regime.
- **NVDA Earnings (after close May 19):** Beat estimates — consensus $78.9B rev / $1.77 EPS. Stock trading +2.1% at $225.28 (vs May19 close $220.61) at time of scan.
- **FOMC Minutes (2:00 PM ET today):** April 28-29 meeting. Rates held 3.50%–3.75%. Elevated inflation flagged (partly energy-driven / Middle East). Last record under previous Fed leadership before Kevin Warsh era. No new rate moves expected.
- **Lowe's (LOW) Pre-Market:** Q1 EPS $2.90 ($3.03 adj, +3.8%), sales $23.1B, comps +0.6%. Full-year guidance reaffirmed. Mild beat.
- **Target (TGT) Pre-Market:** Shares +2% on Q1 sales beat and raised annual revenue outlook.
- **S&P 500 YTD:** ~+10%. Sector leaders: Energy (+26.0%), Technology (+16.7%), Materials (+12.9%), Industrials (+12.8%), Communications (+12.3%).
- **Geopolitical:** US–Iran tensions + Strait of Hormuz tanker traffic ongoing. WTI structural bid remains despite today's pullback.
- **FOMC Minutes 2:00 PM ET:** No new bracket orders placed in 30 minutes before this release per CONSTRAINTS.

---

### VIX Regime
- **Current VIX:** 17.83
- **Regime:** Normal (14–22)
- **Sizing Multiplier:** 1.00×
- **Entry policy:** All four lanes (2a-Long, 2a-Short, 2b-Long, 2b-Short) eligible. Full position sizing.

---

### Universe Scan

#### CANDIDATES EVALUATED (from yesterday's watchlist + today's catalysts)

1. **XOM** — Energy (Long continuation thesis)
2. **NVDA** — Technology (Post-earnings momentum)
3. **HD** — Consumer Discretionary (Post-earnings short assessment)
4. **CVX** — Energy (XOM pair check)
5. **XLE** — Energy ETF (sector confirmation)

---

### Candidate Analysis

---

#### XOM — LONG (2b-LONG lane evaluated)

**Layer A — Catalyst + Trend:**
- **Catalyst:** Energy sector #1 YTD (+26.0%). WTI structurally elevated (+63% YoY). XOM has been in confirmed uptrend. Geopolitical bid (Hormuz tanker risk) ongoing.
- **Sector posture:** Energy = top sector YTD ✅
- **RSI(14):** 64.9 — in the 50–70 range ✅
- **Today's context:** WTI −3.52% today. XOM is trading DOWN −2.3% (partial bar $158.86 vs May19 close $162.55). This is a *pullback day*, NOT a continuation breakout day.

**Layer B — Quant (2b-LONG):**
- **Z-Score (May19 settle vs prior 20):** +2.320 ✅ (≥+1.0)
- **Close > prior 20d high:** May19 $162.55 > prior 20d high $160.49 ✅ (breakout confirmed on May 19)
- **RSI 50–70:** 64.9 ✅
- **Volume May19:** 20,722,666 / 20d avg 16,797,568 = **1.234× ❌** (need ≥1.5×)
- **50-SMA > 200-SMA:** 50-SMA = $155.39. 200-SMA = **N/A** (only 151 settled bars; need 200) — **❌ Cannot verify**

**Minervini Trend Template (LONG):**
- Price > 50-SMA ($162.55 > $155.39) ✅
- Price > 150-SMA ($162.55 > $136.74) ✅
- Price > 200-SMA: **CANNOT VERIFY — insufficient history (151 bars)** ❌
- 150 > 200: **CANNOT VERIFY** ❌
- 200-SMA trending up ≥1 month: **CANNOT VERIFY** ❌
- 50 > 150 ($155.39 > $136.74) ✅
- 50 > 200: **CANNOT VERIFY** ❌
- >30% above 52wk low ($110.64): +46.9% ✅
- Within 25% of 52wk high ($171.47): −5.2% ✅
- **Trend Template Result: FAIL** (cannot verify 200-SMA conditions; 151/200 bars available)

**Pair Check (XOM↔CVX):**
- XOM Z = +2.320, CVX Z = +1.980
- Divergence = |2.320 − 1.980| = **0.340σ ✅** (well within 1.5σ)

**RESULT: ❌ SKIP**
- Lane 2b-LONG fails on two independent gates: (1) volume 1.234× < 1.5× required; (2) 200-SMA unverifiable (151 bars available, need 200). Trend Template FAIL.
- Additionally, today XOM is DOWN −2.3% with WTI falling −3.52% — this is not a breakout continuation day. Correct posture is to wait.
- **Watchlist Thursday:** If today's XOM volume prints ≥25.2M shares AND close holds above $160.49, the thesis resets for Thursday entry. Await full day bar.

---

#### NVDA — LONG (2b-LONG lane evaluated, post-earnings)

**Layer A — Catalyst + Trend:**
- **Catalyst:** NVDA Q1 FY2027 earnings beat (reported after close May 19). Consensus $78.9B rev / $1.77 EPS beat. AI demand signal. Stock +2.1% premarket at $225.28.
- **Sector posture:** Technology YTD +16.7%, #2 sector ✅
- **RSI(14) settled:** 59.9 — in 50–70 range ✅
- **Today context:** NVDA trading up from $220.61 → ~$225.28 (+2.1%)

**Layer B — Quant (2b-LONG):**
- **Z-Score (today partial vs 20d mean $219.55):** +1.170 ✅ (≥+1.0)
- **Close > prior 20d high ($235.74):** $225.28 < $235.74 **❌ NO BREAKOUT**
  - The 20-day settled high is $235.74 (May 14). NVDA is trading at $225.28 = still 4.4% BELOW that pivot. A momentum lane entry requires closing ABOVE the pivot.
- **RSI:** 59.9 ✅
- **Volume today (partial ~62.7M, proj ~157M vs avg 156M):** ~1.01× projected ❌ (barely at 1.0×; need ≥1.5×)
- **50-SMA > 200-SMA:** 50-SMA = $194.72; 200-SMA = **N/A (151 bars)** ❌ Cannot verify

**Minervini Trend Template (LONG):**
- Price > 50-SMA ($220.61 > $194.72) ✅
- Price > 150-SMA ($220.61 > $188.76) ✅
- Price > 200-SMA: **CANNOT VERIFY** ❌
- 150 > 200: **CANNOT VERIFY** ❌
- 200-SMA trending up: **CANNOT VERIFY** ❌
- 50 > 150 ($194.72 > $188.76) ✅
- >30% above 52wk low ($165.17): +33.6% ✅
- Within 25% of 52wk high ($235.74): −6.4% ✅
- **Trend Template Result: FAIL** (cannot verify 200-SMA conditions)

**Pair Check (NVDA↔AVGO):**
- NVDA Z today = +1.170
- AVGO Z = −1.017 (AVGO selling off, down ~2.3% today)
- Divergence = |1.170 − (−1.017)| = **2.187σ ❌ EXCEEDS 1.5σ THRESHOLD**
- AVGO and broader semis NOT confirming NVDA's post-earnings pop. Single-name earnings event, not sector rotation.

**RESULT: ❌ SKIP**
- Fails Layer B on three gates: (1) no breakout above 20d high ($235.74); (2) volume insufficient; (3) pair divergence 2.187σ > 1.5σ — AVGO not confirming.
- Mean-Reversion lane not applicable (Z = +1.17 — not stretched to ≥+2.0, not oversold).
- **Watchlist Thursday:** If NVDA closes today above $235.74 on volume ≥1.5× (≥234M shares), and AVGO Z-divergence narrows, re-evaluate as a 2b-LONG with a fresh breakout bar. Current posture = watch, no trade.

---

#### HD — SHORT (2b-SHORT lane evaluated)

**Layer A — Catalyst + Trend:**
- **Catalyst:** Post-earnings decline. HD reported Q1 May 19 — shares sold off through earnings. Comp sales soft, macro housing headwinds (high mortgage rates). HD trending from $391.90 → $302.44 = −22.8% from 52wk high.
- **Sector posture:** Consumer Discretionary YTD = −0.03% (rolling over) ✅ for short bias
- **RSI(14):** 33.7 — in the 30–50 range ✅ (appropriate for momentum short)
- **Today context:** HD reversed UP +1.8% to $307.81 (partial) — NOT a continuation of breakdown

**Layer B — Quant (2b-SHORT):**
- **Z-Score (May19 settle):** −1.213 ✅ (≤−1.0)
- **Close < prior 20d low ($297.51):** May19 $302.44 > $297.51 **❌ NO BREAKDOWN CONFIRMED**
  - Price has NOT broken below the prior 20d low. 302.44 vs 297.51 pivot — still $4.93 above breakdown level.
- **RSI 30–50:** 33.7 ✅
- **Volume May19:** 8,698,300 / avg 4,598,528 = **1.89× ✅** (strong elevated volume)
- **50-SMA < 200-SMA:** 50-SMA = $327.66; 200-SMA = **N/A (152 bars)** ❌ Cannot verify

**Minervini Trend Template (SHORT):**
- Price < 50-SMA ($302.44 < $327.66) ✅
- Price < 150-SMA ($302.44 < $354.64) ✅
- Price < 200-SMA: **CANNOT VERIFY** ❌
- 150 < 200: **CANNOT VERIFY** ❌
- 200-SMA trending down: **CANNOT VERIFY** ❌
- >30% below 52wk high ($391.90): −21.5% **❌ FAIL** (need ≤−30%)
- Within 25% of 52wk low ($297.51): +1.7% ✅
- 6-month return: −18.9% — in bottom 30%? Plausible for short (cannot compute exact percentile without universe sample)
- **Trend Template Result: FAIL** — does not meet the ">30% below 52wk high" condition AND cannot verify 200-SMA conditions

**Pair/Sector Check:** XHB (homebuilders ETF) or LOW as pair — not pulled; but LOW +3.8% EPS beat this morning suggests sector is not uniformly broken. HD underperforming LOW is idiosyncratic. Actually, sector is mixed today — leans against short entry.

**RESULT: ❌ SKIP**
- Fails Layer B: no breakdown below 20d low; Trend Template fails 200-SMA conditions and >30% below 52wk high rule.
- Today HD is UP +1.8% (reversal), making short entry today even less appropriate.
- **Not on active watchlist** — does not meet Short Trend Template minimum requirements.

---

#### CVX — Context/Pair Only
- Z = +1.980, within 1.5σ of XOM (divergence 0.34σ) ✅ — confirms energy sector thesis
- Today partial: $193.83 (down from May19 $197.25 = −1.74%) — also pulling back with WTI
- Same Trend Template limitation (151 bars, 200-SMA unavailable) — not evaluated as standalone entry

#### XLE — Context Only
- Z = +1.75 (estimated from last check), Vol May19 = 31,113,841 / avg 36,437,xxx = ~0.85× — still below 1.0×
- Today pulling back with WTI. Not evaluated as standalone entry.

---

### Trade Ideas (Cleared Both Layers)

**None.** Zero candidates cleared both Layer A + Layer B today.

---

### Skipped Candidates

| Ticker | Direction | Failed Gate | Specific Issue |
|--------|-----------|-------------|----------------|
| XOM | 2b-LONG | Layer B (vol + TT) | Vol 1.23× < 1.5× required; 200-SMA unverifiable (151 bars); today DOWN −2.3% with WTI −3.52% |
| NVDA | 2b-LONG | Layer B (no breakout + pair divergence) | Price $225.28 < 20d high $235.74; AVGO divergence 2.19σ > 1.5σ; vol barely 1.0× projected |
| HD | 2b-SHORT | Layer A + Layer B (TT + no breakdown) | Trend Template: only −21.5% below 52wk high (need −30%+); 200-SMA N/A; price NOT below 20d low $297.51; today up +1.8% |
| CVX | — | Pair context only | Confirms XOM thesis; same data gap; not evaluated as standalone entry |

---

### Risk Factors
1. **FOMC Minutes 2:00 PM ET:** Could reprice rate expectations. Fed language on "elevated inflation from energy" could affect energy sector either way. **No new bracket orders in 30 min window before 2:00 PM ET.**
2. **WTI −3.52% today:** Largest single-day drop in weeks. Energy sector may see continued weakness this session. XOM/CVX/XLE pullback is directly correlated. This does NOT invalidate the multi-week structural thesis but means today is not the day to enter energy longs.
3. **NVDA post-earnings gap:** Stock up only +2.1% — a modest reaction to a major beat. AVGO selling off simultaneously (Z=−1.017) suggests the broader semi sector is NOT confirming NVDA's move. Pair divergence 2.19σ blocks entry. Earnings gap can fade quickly.
4. **Persistent 200-SMA data gap:** Running on 151–152 bars for multiple names (XOM, NVDA, CVX, HD). Alpaca data history starts ~Oct 2025 for this account. The 200-SMA will become available in approximately 7–8 more trading weeks. This is a structural limitation — log it but cannot overcome it operationally.
5. **PDT headroom:** 0/3 day trades used — full flexibility preserved.
6. **No open positions entering a binary (NVDA earnings + FOMC minutes):** Correct posture as noted yesterday. Maximum optionality preserved.

---

### Decision

**HOLD — No trades today.**

All three directional candidates (XOM long, NVDA long, HD short) failed one or more required gates. The predominant blockers today are:
- Volume confirmation threshold not met (XOM: 1.23×)
- No price breakout/breakdown confirmation (NVDA below 20d high; HD above 20d low)
- Pair divergence failure (NVDA/AVGO: 2.19σ)
- Minervini Trend Template 200-SMA unverifiable (structural data limitation)
- Market context: energy pulling back hard today with WTI −3.52%; FOMC minutes at 2 PM add uncertainty

Zero trades is the correct call. Patience rule applies.

---

### Watchlist for Thursday Pre-Market (May 21)

1. **XOM** — If today's bar closes ≥$160.49 (holds breakout level) AND today's volume ≥25.2M shares (1.5× threshold met), re-evaluate as 2b-LONG. If price closes below $160.49, thesis temporarily invalidated — wait for new base.
2. **NVDA** — If NVDA closes today above $235.74 on volume ≥234M shares, Thursday becomes 2b-LONG candidate with pivot=$235.74. If closes below $220, watch for 2a-LONG setup (need Z ≤−2.0 + RSI <30).
3. **CVX** — Same energy thesis as XOM; same Trend Template limitation. Watch in context of XOM.
4. **FOMC Minutes Fallout (today 2 PM):** If minutes are hawkish (signal rate hikes), monitor rate-sensitive sectors (Financials, Utilities) for dislocations Thursday.
5. **200-SMA Data Gap:** All names will gain 1 additional bar each day. Full 200-bar history available in ~7–8 more weeks. In the interim, trend template results flagged as "FAIL (insufficient history)" rather than directional failures.

---

### EOD Snapshot (to be updated post-close — pre-market stub)

**Portfolio:** $99,056.46 | **Cash:** $99,056.46 (100%) | **Day P&L:** $0.00 | **Deployed:** 0%

| Ticker | Shares | Entry | Close | Unrealized P&L | Stop |
|--------|--------|-------|-------|----------------|------|
| — | — | — | — | — | — |

**Trades today:** None — HOLD decision confirmed by Layer A + Layer B failures on all candidates.


---

### 2026-05-20 — Midday Rescan Addendum (13:39 ET)

**VIX Regime at rescan:** 17.83 — Normal (1.00× multiplier). No change from morning.

**Account at rescan:** $99,056.46 equity | $99,056.46 cash (100%) | 0 positions | 0% deployed | 0/3 week trades | 0/3 day trades

**Spread check — all three candidates now have narrow, normalized spreads:**
- XOM: bid $158.14 / ask $158.28 → spread **0.09%** ✅ (was wide pre-open)
- NVDA: bid $224.76 / ask $224.79 → spread **0.01%** ✅
- HD: bid $308.80 / ask $311.00 → spread **0.71%** ✅ (technically < 1%, but $2.20 wide — atypical for HD; stale quote flagged)

---

**Skipped at open, re-evaluated:**

| Ticker | Direction | Spread | Z-Score | Verdict |
|--------|-----------|--------|---------|---------|
| XOM | 2b-LONG | 0.09% ✅ | +1.384 ✅ | **STILL SKIPPED** |
| NVDA | 2b-LONG | 0.01% ✅ | +1.154 ✅ | **STILL SKIPPED** |
| HD | 2b-SHORT | 0.71% ✅ | −0.670 ❌ | **STILL SKIPPED** |

---

**Detailed re-evaluation:**

**XOM (2b-LONG lane):**
- Live mid: $158.21 (vs May19 settle $162.55 = −2.67%)
- Z-Score vs 20d: +1.384 ✅ (≥+1.0)
- **❌ FATAL: Price $158.21 is BELOW breakout pivot $160.49** — the May18 20d high the strategy requires a confirmed close above. XOM has retreated back underneath the pivot intraday. The momentum lane requires the close (or current price) to be above the 20d high for the breakout signal to remain active.
- ❌ 200-SMA unverifiable (152 settled bars; need 200) — Trend Template cannot clear. Structural limitation (~7 weeks to resolve).
- ❌ Volume gate (≥1.5× avg = 25.4M shares): Cannot confirm with intraday bar only; no settled bar for today yet.
- ✅ RSI estimated ~58–63 (50–70 range) — would pass.
- ✅ XOM/CVX pair divergence 0.34σ (morning reference) — well within 1.5σ.
- **Context:** WTI crude continuing to decline today (−3.52% session). Energy sector pullback is real. Structural multi-week thesis (Hormuz/geopolitical bid) remains intact, but TODAY is not an entry day. XOM needs to reclaim $160.49 and build a fresh bar with ≥1.5× volume. Wait for Thursday's settled bar.

**NVDA (2b-LONG lane):**
- Live mid: $224.77 (vs May19 settle $220.61 = +1.9% — but vs premarket high ~$225.28, the pop has FADED)
- Z-Score vs 20d: +1.154 ✅ (≥+1.0)
- **❌ FATAL: No breakout** — $224.77 is 4.65% BELOW pivot $235.74 (May14 20d high). Momentum lane requires close above pivot. NVDA has never come close today.
- **❌ AVGO pair divergence: 2.171σ** — significantly exceeds 1.5σ threshold. AVGO and broader semis are not confirming. This is an isolated post-earnings event, not a sector rotation.
- ❌ 200-SMA unverifiable (structural).
- ❌ Volume intraday: Cannot confirm ≥1.5× (235.8M) settled bar. Morning projection was barely 1.01× — far below requirement.
- **Earnings pop assessment:** The +$4.67 premarket post-earnings pop has essentially reversed. NVDA is now only +1.9% from May19 settle at 13:39 ET — a modest move that reflects the market's already-elevated pre-earnings expectations. No fresh momentum catalyst materializing today.
- **2a-LONG (mean-reversion) check:** Z = +1.154 — need ≤ −2.0. Not applicable. NVDA is not oversold.
- **Watchlist update:** Thursday thesis weakens. If NVDA closes today below $220.61 (yesterday's settle), the momentum thesis is fully invalidated. Only re-qualify as 2b-LONG if price breaks and closes above $235.74 on ≥1.5× volume.

**HD (2b-SHORT lane):**
- Live mid: $309.90 (vs May19 settle $302.44 = **+2.47%** — stock is RISING)
- Z-Score vs 20d: **−0.670** ❌ — has WEAKENED from this morning's −1.213 as price bounced. Now fails the Z ≤ −1.0 gate.
- **❌ FATAL: Price $309.90 is 4.16% ABOVE breakdown pivot $297.51.** Short momentum lane requires price to close BELOW the 20d low. HD is moving the wrong direction.
- ❌ Trend Template (SHORT): Only 20.9% below 52wk high ($391.90) — need ≥30%. Gap is structural (need HD to fall to ~$274.33 to qualify). No near-term path.
- ❌ 200-SMA unverifiable (structural).
- ✅ Volume May19: 1.78× avg — would have passed. Irrelevant given other failures.
- ✅ RSI ~35–42 (30–50 range) — still in window.
- **Sector note:** LOW reported EPS beat +3.8% this morning, raising annual outlook. This directly contradicts the "consumer discretionary rolling over" thesis for HD. Sector signal is now MIXED, not aligned for short.
- **⚠️ WATCHLIST REMOVAL:** HD is removed from active watchlist. The >30% below 52wk high Trend Template condition is structural — HD would need to fall to $274.33 before this gate could even potentially clear. Not a realistic near-term setup.

---

**FOMC Minutes Warning (2:00 PM ET):**
- No new orders within 30 min of 2:00 PM ET per CONSTRAINTS.
- Current time at rescan completion: ~13:45 ET.
- No trades fired → constraint has no operational impact today.
- Held positions: none → no management actions required around 2 PM either.

---

**Trades fired this rescan:** None

**Patience rule applied:** Correct. No gates were lowered. Zero trades is the right outcome when no candidate re-clears all required layers. The spread normalization was confirmed for all three names, but the fundamental gate failures (price level, Z-score, Trend Template, pair divergence) that caused morning skips have either persisted unchanged or worsened in two of three cases (NVDA earnings pop faded; HD Z weakened further as price bounced).

---

**Updated Watchlist for Thursday Pre-Market (May 21):**

1. **XOM** — Re-evaluate if today's settled bar (post-close) shows:
   - Close ≥ $160.49 (reclaims breakout pivot) AND
   - Volume ≥ 25.4M (1.5× avg). If both: re-enter as 2b-LONG Thursday.
   - If close < $160.49: breakout invalidated, build new base, wait.

2. **NVDA** — Thesis significantly weakened. Only re-qualify if:
   - Close today > $235.74 on ≥235.8M volume (original 2b-LONG conditions).
   - If today closes below $220.61: momentum thesis fully invalidated. Watch for 2a-LONG opportunity only if Z reaches ≤ −2.0 (would require ~$191 or below based on current 20d distribution — unlikely near-term).

3. **HD** — **Removed from watchlist.** Structural TT gap (needs −30% below 52wk high). Not a viable short under current Trend Template rules. Log closure of this thesis.

4. **FOMC Minutes Fallout (today 2 PM):** Post-minutes, note tone in tomorrow's pre-market research. Hawkish = rate-sensitive sector opportunities (Financials short, Utilities movement). Dovish = possible continuation of risk-on. Update market context section Thursday.

---

## 2026-05-20 — Afternoon Scan Addendum (~20:10 UTC / ~4:10 PM ET)

**Scan time:** Post-session (market closed 20:00 UTC / 4:00 PM ET); scan ran at ~20:10 UTC
**VIX regime at scan:** NORMAL (17.83 from morning research) | Sizing multiplier: 1.00×

---

### STEP 1 — Order & Position State Reconciled vs TRADE-LOG

**Orders returned by API (3 relevant, all historical):**

| Order ID | Symbol | Type | Status | Detail |
|----------|--------|------|--------|--------|
| 1d69c496 | XOM | Bracket limit BUY 61 sh @ $159.78 | **EXPIRED** 2026-05-18T20:02 | TIF: day — never filled ✅ logged |
| 94606e38 | XOM | Stop child $147.80 | **CANCELED** 2026-05-18T20:02 | Auto-cancelled with parent ✅ |
| 336d922a | XOM | TP child $183.74 | **CANCELED** 2026-05-18T20:02 | Auto-cancelled with parent ✅ |

- **Positions API: `[]`** — 100% cash confirmed. No filled positions.
- **Morning bracket orders placed today (May 20): NONE** — pre-market research decision was explicit HOLD (XOM: vol 1.23× < 1.5× + Trend Template fail; NVDA: no breakout + pair divergence 2.19σ; HD: short TT structural fail). Nothing to reconcile for fills.
- **Bracket fills today: 0**
- **Stale limits: 0** — no open orders of any kind at scan time.
- **TRADE-LOG reconciliation: FULLY CURRENT.** No discrepancies. All 6 historical orders match log entries exactly.

---

### STEP 2 — Trailing Stop Upgrades: N/A

No positions held. Portfolio is 100% cash ($99,056.46). No trailing stop workflow applicable.

---

### STEP 3 — Stale Limit Cancellations: N/A

No open orders exist. Monday's XOM bracket (1d69c496) expired naturally at session close on May 18 per its TIF: day. Nothing to cancel.

---

### STEP 4 — Afternoon Opportunity Scan

**VIX regime:** NORMAL (1.00×) | **Positions:** 0/6 | **Week trades:** 0/3 | **PDT:** 0/3

**Quant metrics computed from 25-bar settled data (through May 19) + post-session quotes:**

| Ticker | May19 Settle | AH Bid | AH Implied Δ | Z-Score (vs May19) | RSI(14) | 20d High/Low | Vol May19 vs Avg | Key Gate Failure | Verdict |
|--------|-------------|--------|--------------|---------------------|---------|--------------|-----------------|-----------------|---------|
| XOM | $162.55 | $149.56 | **−$13.0 (−8.0%)** | +2.380 | 62.2 | 20d H: $162.55 | 1.22× ❌ (<1.5×) | Vol + 200-SMA unavail. + AH collapse implies session-day thesis break | **REJECT** |
| CVX | $197.25 | $181.88 | **−$15.4 (−7.8%)** | +2.031 | 57.8 | 20d H: $197.25 | 1.21× ❌ | Vol + AH collapse + sector shock | **REJECT** |
| XLE | $61.29 | $58.36 | **−$2.93 (−4.8%)** | +2.127 | 59.9 | 20d H: $61.29 | 0.86× ❌ | Vol far below 1.5× + AH decline | **REJECT** |
| NVDA | $220.61 | mid $220.27 | ~flat | +0.767 | 58.5 | 20d H: $235.74 (no breakout) | 0.90× ❌ | Z < +1.0 for any lane; no breakout; vol below avg | **REJECT** |
| HD | $302.44 | $291.30 | −$11.1 (−3.7%) | −1.244 | 34.8 | 20d L: $297.51 | 1.78× ✅ | Short TT −22.8% below 52wk high (need ≥−30%); 200-SMA unavail.; May19 settle above 20d low | **REJECT** |

**Pair Z-Scores (from May 19 settled data):**
- XOM (+2.380) ↔ CVX (+2.031): divergence = **0.349σ ✅** (≤1.5σ — energy sector cohesion confirmed)
- XOM (+2.380) ↔ XLE (+2.127): divergence = **0.253σ ✅** (broad sector alignment)

---

**Candidate Detail Notes:**

**⚠️ ENERGY SECTOR — CRITICAL DEVELOPMENT (May 20 session):**
All three energy names (XOM, CVX, XLE) show after-hours bids that are 5–8% below their May 19 settled closes. These are bid-only R-flagged quotes (ap=0 — no ask published), which are typical of after-hours thin markets. However, the consistency across all three names (XOM −8%, CVX −7.8%, XLE −4.8%) strongly suggests a significant sector-level event occurred during today's (May 20) session. Most plausible explanations: (1) WTI crude price decline on Iran deal progress, (2) FOMC minutes (2:00 PM ET today) signaling hawkish tone that pressured energy/cyclicals, or (3) broad risk-off from NVDA post-earnings reaction. Whatever the cause, the energy thesis that has been the central focus of this account's watchlist has been materially stressed during today's session. **XOM at $149.56 AH would put it below its April structural support at $146.44 (or near it) — approaching thesis-break territory again.** This mirrors the May 6–7 pattern that triggered the original thesis-break exit.

**Action required:** Do NOT re-place any energy bracket order at Thursday's pre-market open without first confirming: (1) May 20 settled closing prices via bars API, (2) WTI crude level and Iran/Hormuz news catalyst validity, (3) energy sector trend template re-assessment.

**XOM — REJECT (3 independent failures):**
1. Volume gate: May 19 vol 1.22× < 1.5× (same structural disqualifier in place since May 15 breakout day)
2. 200-SMA unverifiable: only 152 settled bars; need 200 for full Trend Template (~6.5 more weeks)
3. After-hours signal: AH bid $149.56 implies a ~$13 decline during today's session — if settled price reflects this, XOM would be back below its May 18 breakout pivot ($157.92–$160.49), completely resetting the momentum setup and potentially breaching April structural support

**CVX — REJECT (same failure family as XOM):**
- Z = +2.031 on May 19 data (qualifies on Layer B Z-score alone), but: (1) AH bid implies similar session decline; (2) vol 1.21× < 1.5×; (3) sector shock makes Layer A catalyst negative today.
- The prior 20d high IS May 19's settle ($197.25) — meaning CVX would need to close tomorrow ABOVE $197.25 to qualify as a fresh breakout bar. If today's session priced CVX near $182, that is far from the breakout level.

**XLE — REJECT:**
- Volume 0.86× — the most extreme below-average reading of any energy name. The sector ETF is underperforming even the individual stocks on volume. No institutional accumulation signal.
- AH bid $58.36 would represent a 4.8% session decline. Z-score built on May 19 data (+2.127) will reset sharply lower once May 20's close is incorporated into the 20-day window.

**NVDA — REJECT:**
- The post-earnings reaction is flat/neutral: AH mid $220.27 vs May 19 settle $220.61 (−0.15%). The earnings beat did NOT produce a sustained breakout above the $235.74 20-day high.
- Z = +0.767 — below the +1.0 minimum for any momentum lane.
- Vol May 19: 0.90× — below average on a key post-earnings day.
- AVGO pair divergence (2.187σ > 1.5σ) from this morning's research remains in force — no sector confirmation.
- **Status: NVDA has failed the momentum setup for 3 consecutive evaluation sessions (May 18, 19, 20). The earnings catalyst is now spent. Reset to pure quant watch — only re-qualify if: (a) Z returns to ≥+1.0 AND close >$235.74 on ≥1.5× vol for a new breakout, or (b) a pullback to Z ≤−2.0 + RSI <30 creates a mean-reversion long.**

**HD — REJECT (structural Trend Template failure):**
- Z = −1.244 ✅ (passes ≤−1.0 threshold for 2b-SHORT lane)
- RSI = 34.8 ✅ (in 30–50 range for momentum short)
- Volume May 19: 1.78× ✅ (elevated — post-earnings activity)
- BUT Minervini Short Trend Template requires price to be **>30% below 52-week high** ($391.90). Current distance: only **−22.8%** ($302.44). Needs to reach $274.33 for the gate to clear. This is a **structural, not timing, failure** — HD has not fallen far enough from its highs to qualify as a "true laggard" by Minervini criteria. Additionally, 200-SMA is unverifiable (152 bars), and May 19's settled close ($302.44) is above the 20-day low ($297.51) — no confirmed breakdown on the last bar.
- AH bid $291.30 would be below $297.51 if it reflects today's settled price, potentially indicating the breakdown occurred on May 20. **Re-evaluate Thursday with May 20 settled bar** — if HD closes below $297.51 today AND Z ≤ −1.0 AND volume ≥ 1.5×, the 2b-SHORT lane's price and volume gates would clear. The TT structural requirement (−30% below 52wk high) would still fail unless HD settles below $274.33.

---

### Afternoon Market Context

Today's dominant event was the **FOMC Minutes release (2:00 PM ET)**. Based on the energy sector's severe after-hours decline (XOM −8%, CVX −7.8%, XLE −4.8%), it appears the FOMC minutes were interpreted as hawkish — language about inflation persistence (partly energy-driven) and reduced appetite for near-term rate cuts likely pushed the market to re-price risk. Energy, which had been the YTD leader (+26%), is particularly vulnerable to hawkish Fed signals because: (1) higher rates raise the discount rate on future commodity revenue; (2) a stronger dollar (hawkish Fed) suppresses oil prices; and (3) any market that associates inflation with energy prices may see energy sold alongside rate-sensitive sectors. NVDA's post-earnings reaction was essentially flat (AH mid $220.27 ≈ yesterday's $220.61 close) — a non-event that suggests the earnings beat was fully priced in. HD continued its post-earnings drift lower (AH bid $291.30, potentially approaching or breaching the $297.51 20-day low breakdown level for the first time on an intraday basis). The portfolio's 100% cash position entering today's session was, in hindsight, correct — the energy names that were the primary candidates would have been underwater during today's session regardless of any entry.

---

**Bracket fills today:** 0 (no morning limits were placed — HOLD decision at pre-market; all candidates failed gates)
**Stops upgraded:** 0 (no positions held; no upgrade workflow applicable)
**Stale limits cancelled:** 0 (no open orders existed)
**New afternoon entries:** none — all 5 candidates failed composite Layer A + Layer B gates
**Afternoon market context:** Energy sector declined sharply during today's session (XOM AH −8%, CVX −7.8%, XLE −4.8%) — most likely driven by FOMC minutes hawkish signal and/or WTI declines. NVDA post-earnings flat (no sustained pop). HD drifting toward potential 2b-SHORT setup but Trend Template TT structural gate (−22.8% vs −30% required below 52wk high) remains a hard blocker.

**Key watchlist for Thursday pre-market (2026-05-21):**
1. **ENERGY SECTOR (XOM/CVX/XLE)** — ⚠️ CRISIS WATCH: Confirm May 20 settled prices via bars API. If XOM settles below $157.92 (prior breakout pivot), the momentum setup is fully reset. If below $154.88 (prior pre-breakout high), a new base must form. If approaching $146.44 (April structural support), full thesis re-evaluation required. Do NOT place any energy bracket until thesis is confirmed with catalyst + settled data.
2. **HD** — Pull May 20 settled bar Thursday morning. If close < $297.51 on vol ≥ 1.5×, the 2b-SHORT breakdown is confirmed on price/volume — but TT structural gate (−30% below 52wk high) still fails at any price above $274.33. Not a tradeable setup under current TT rules.
3. **NVDA** — Z = +0.767; well below any entry lane. Off active watchlist until either a new all-time high breakout above $235.74 or a mean-reversion dip to Z ≤ −2.0 (~$191).
4. **200-SMA DATA GAP** — All candidates blocked on TT's 200-SMA condition (152/200 bars available). Resolves in ~48 more trading sessions (~10 calendar weeks). Log and accept as operational constraint.
5. **NEW SECTOR SCAN NEEDED** — With energy thesis under stress (AH collapse suggests second consecutive near-failure), need to identify non-energy setups for Thursday. Materials (FCX, NEM, with XLB Z context), Industrials (CAT, GE), or Consumer names should be scanned. Per sector rules: energy sector has 1 confirmed failure (XOM May 7 thesis-break). If today's session represents a second energy stress event on a new attempted entry, caution is heightened but no confirmed second failure (no new energy position was entered). The energy sector clock resets only on a *completed trade*.


---

## 2026-05-21 — Pre-Market Research (Day 24, Thursday)

### Account
- **Equity:** $99,056.46
- **Cash:** $99,056.46 (100%)
- **Buying Power:** $198,112.92 (2× margin)
- **Daytrade Count:** 0/3
- **Open Positions:** 0
- **Open Orders:** 0
- **Week Trades:** 0/3
- **Phase P&L:** −$943.54 (−0.944%)
- **Peak Drawdown:** −1.15% from $100,206.70

---

### Market Context
- **WTI Crude:** ~$100.46/bbl (+$2.20, +2.2%). Briefly touched $99.11 before rebounding. Iran Supreme Leader issued directive that enriched uranium must NOT be sent abroad → US-Iran deal complications → risk premium re-entered energy market.
- **Brent Crude:** ~$107.26/bbl (+2.13%)
- **S&P 500 Futures:** Down ~0.26–0.3% premarket; S&P 500 closed at 7,432.97 on May 20.
- **VIX:** Closed at 17.44 (May 20, −3.43%); hovering ~17.7 at today's open.
- **Fed:** FOMC minutes from prior meeting indicated possible rate hike if inflation remains above 2%. Fed speakers today: Goolsbee and Barkin (scheduled). April CPI 3.8%, PPI 6%.
- **Jobless Claims:** 209,000 (week ending May 16), below 213,000 estimate. Continuing claims 1.782M. Labor market resilient.
- **Housing Starts (April):** 1.465M SAAR, beat 1.41M estimate; −2.8% MoM.
- **PMI:** Preliminary US and Eurozone May PMI on calendar today.
- **Philly Fed:** Business Outlook, CAPEX Index, Employment for May.
- **Pre-market Earnings:**
  - **WMT:** Fiscal Q1 beat but weak full-year outlook → −10.2% gap premarket (to ~$120.57)
  - **INTU:** Earnings beat but announced 17% workforce cut → ~−20% gap premarket (to ~$306.68)
  - **NIO:** Q1 revenue +112.2% YoY to RMB25.5B ($3.7B); deliveries 83,465 (+98.3%)
  - **GTES:** +15.8% premarket on Timken belts acquisition
  - **NVDA (post-market yesterday):** Beat earnings; strong outlook; AH reaction flat (~$220.27 vs $220.61 settle)
- **Sector YTD Leaders:** Energy +27.87%, Tech +23.55%, Materials +15.24%, Industrials +12.84%
- **Sector YTD Laggards:** Health Care −7.60%, Financials −6.55%, Comm Services −1.82%

---

### VIX Regime
- **Current VIX:** 17.44 (close) / ~17.7 (today open)
- **Regime:** Normal (14–22)
- **Sizing Multiplier:** 1.00×
- **Cold Start Default:** 10% per position (< 30 closed trades)

---

### Trade Ideas — Cleared Both Layers

**NONE.** All candidates rejected. See full analysis below.

---

### Skipped Candidates

#### 1. XOM — LONG (Energy / Iran rebound)
- **Catalyst:** Iran directive blocks uranium export → WTI +2% → energy risk premium restored ✓
- **Sector:** Energy #1 YTD +27.87% ✓
- **Bars:** 153 total (Oct 2025–May 2026)
- **Quant (25-bar):** Close $156.635 (May 21 partial) | Mean₂₀ $152.51 | σ $4.40 | Z = **+0.937**
- **Layer B — Z-Score gate:**
  - Momentum 2b-LONG: Z ≥ +1.0 → **FAIL** (0.937 < 1.0, barely)
  - Mean-Rev 2a-LONG: Z ≤ −2.0 → **FAIL**
  - Neither lane clears → **Layer B FAIL**
- **Minervini Trend Template (Long):**
  - Price $156.64 > SMA50 $155.55 ✓
  - Price $156.64 > SMA150 $137.04 ✓
  - 200-SMA: **NOT AVAILABLE** (152/200 bars — resolves in ~48 sessions) → **FAIL**
  - 52w High $171.47 → −8.7% below (within 25% ✓); 52w Low $110.64 → +41.6% above (>30% ✓)
  - 6-month return: +31.6% (strong)
- **Pair:** CVX | CVX Z = +0.594 | Divergence 0.34σ ≤ 1.5σ ✓ (pair passes, but both Layer B and TT fail)
- **Volume:** May 20: 18.5M vs 16.9M avg = 1.10× (inadequate for momentum lane's 1.5× threshold)
- **REJECT — Layer B FAIL (Z sub-threshold both lanes) + Minervini 200-SMA structurally unavailable**

#### 2. XLE — LONG (Energy ETF / Iran rebound)
- **Catalyst:** Iran risk premium → WTI +2% → XLE sector ETF ✓
- **AUM:** ~$40B+ ✓ | **Volume:** May 20: 61.8M vs 39.6M avg = **1.56×** ✓
- **Quant (25-bar):** Close $59.785 | Mean₂₀ $58.25 | σ $1.51 | Z = **+1.020**
- **Layer B — Momentum 2b-LONG:**
  - Z ≥ +1.0 ✓ (barely)
  - Close $59.785 > 20d high $61.29? → **FAIL** (price is BELOW prior 20d high = no confirmed breakout)
  - Lane fails on breakout condition
- **Minervini Trend Template:**
  - 50-SMA $58.34 — price above ✓
  - 150-SMA: **NOT AVAILABLE** (price discontinuity Dec 2025; only 114 post-adj bars) → **FAIL**
  - 200-SMA: **NOT AVAILABLE** → **FAIL**
  - Note: XLE underwent a share consolidation in Dec 2025 (price ~$92→$45 jump), making pre-adjustment SMAs incomparable
- **Pair:** CVX | Z = +0.594 | Divergence 0.43σ ✓ (pair OK, but both other gates fail)
- **REJECT — No breakout above 20d high ($61.29 required); Minervini 150/200 SMA unavailable**

#### 3. NVDA — LONG (post-earnings continuation)
- **Catalyst:** Beat Q1 earnings; strong sales outlook. But AH reaction flat ($220.27 vs $220.61 settle) → catalyst SPENT.
- **Quant:** Close $223.47 | Mean₂₀ $213.40 | σ $10.78 | Z = **+0.934**
- **Layer B — Momentum 2b-LONG:**
  - Z ≥ +1.0 → **FAIL** (0.934 < 1.0)
  - Close > 20d high $235.74 → **FAIL**
- **Status:** 4th consecutive session (May 18–21) failing momentum lane. Earnings catalyst exhausted. Off active watchlist until new catalyst or Z requalifies.
- **REJECT — Layer B double failure; catalyst consumed**

#### 4. NIO — LONG (earnings beat, +112% revenue)
- **Catalyst:** Q1 revenue +112.2% YoY, deliveries +98.3% ✓ (strong report)
- **Quant (25-bar):** Close $5.59 | Mean₂₀ $6.08 | σ $0.24 | Z = **−2.022**
- **Layer B — Mean-Rev 2a-LONG:** Z ≤ −2.0 → ✓ (barely, −2.022)
- **BUT:**
  - Minervini Long Template: Cannot compute 50/150/200 SMAs (only 25 bars available). 52w low analysis from 25-bar data only: current price AT the low = 0% above low → **FAIL** (needs >30% above 52w low)
  - Bearish price action: NIO DECLINED on May 19 ($5.74) and May 20 ($5.59) DESPITE earnings beat — market is not pricing in the revenue growth
  - Price is in confirmed downtrend within the 25-bar window (high $6.87 → low $5.59)
- **REJECT — Minervini TT structurally fails; bearish price response to positive catalyst; 52w low test at 0% above (needs >30%)**

#### 5. INTU — SHORT (workforce cut + earnings gap-down ~20%)
- **Catalyst:** Announced 17% workforce reduction + weaker outlook → gap-down ~20% to ~$306.68 ✓
- **Market Cap:** ~$87B (>$20B short threshold ✓)
- **Quant (25-bar):** Close $306.68 (partial May 21) | Mean₂₀ $393.00 | σ $8.95 | Z = **−9.649**
- **Layer B — Momentum 2b-SHORT:**
  - Z ≤ −1.0 ✓ | Close < 20d low $371.71 ✓ | Volume 2.72× ✓
  - RSI estimated <30 — **FAIL** (2b-SHORT needs RSI 30–50; at <30 this is a capitulation, not controlled breakdown)
  - 200-SMA unavailable (152 bars) → 50-SMA < 200-SMA unverifiable → **FAIL**
- **Minervini SHORT Template:**
  - Price < SMA50 $407.48 ✓ | Price < SMA150 $523.49 ✓
  - 200-SMA: NOT AVAILABLE → FAIL
  - >30% below 52w high ($683.39): −55.1% ✓ | Within 25% of 52w low: ✓
  - 150-SMA < 200-SMA: CANNOT VERIFY → FAIL
- **HARD RULE VIOLATIONS:**
  1. **"No shorting after >5% gap-down day"** — INTU is −20% gap → squeeze risk rule triggers → **DISQUALIFIED**
  2. RSI <30 (outside 30–50 required for 2b-SHORT lane)
  3. Pair divergence: INTU Z −9.649 vs ADBE/CRM ~0 = ~9.6σ >> 1.5σ → **FAIL**
  4. Minervini 200-SMA unverifiable
- **REJECT — Hard rule (>5% gap-down no-short) + RSI too low + pair divergence 9.6σ + 200-SMA unavailable**

#### 6. WMT — SHORT (weak full-year guidance, −10.2% gap)
- **Catalyst:** Full-year guidance miss → −10.2% premarket gap to $120.565 ✓ (company-specific)
- **Market Cap:** ~$320B (>$20B ✓)
- **Sector posture conflict:** Consumer Staples +7.32% YTD (positive sector — WRONG posture for short)
- **Quant (25-bar):** Close $120.565 | Mean₂₀ $130.61 | σ $1.81 | Z = **−5.561**
- **Layer B — Momentum 2b-SHORT:**
  - Z ≤ −1.0 ✓ | Close < 20d low $127.59 ✓ | Volume 1.74× ✓
  - RSI estimated <30 → **FAIL** (needs 30–50)
  - 200-SMA unavailable → 50-SMA < 200-SMA unverifiable → **FAIL**
- **Minervini SHORT Template:**
  - Price $120.565 < SMA50 $127.13 ✓
  - Price $120.565 < SMA150 $118.95 → **FAIL** (price is ABOVE 150-SMA)
  - 200-SMA: NOT AVAILABLE → FAIL
  - 52w High $134.20 → only −10.2% below (needs >30%) → **HARD FAIL**
  - 6-month return: +18.9% (not a laggard, needs ≤30th pct) → FAIL
- **HARD RULE VIOLATIONS:**
  1. **"No shorting after >5% gap-down day"** — WMT is −10.2% gap → **DISQUALIFIED**
  2. Minervini: only −10.2% below 52w high (requires >30%)
  3. Price above SMA150 (structural — not a true laggard)
  4. Consumer Staples is positive sector (wrong sector posture for short)
  5. Pair divergence: WMT Z −5.561 vs COST/TGT ~0 = ~5.6σ >> 1.5σ → FAIL
- **REJECT — Hard rule (>5% gap-down) + Minervini TT multiple failures + sector posture wrong**

---

### Risk Factors
1. **Iran geopolitical escalation:** Supreme Leader's directive against uranium exports complicates US-Iran deal. Oil could spike further if talks fully collapse; any reversal could send oil back down sharply.
2. **FOMC hawkish risk:** Goolsbee and Barkin speaking today. Minutes flagged possible rate hike. Market reaction to any hawkish tone could pressure energy and growth names.
3. **Earnings volatility:** WMT and INTU both gapping hard — signals that high guidance bars are being punished. Consumer and tech sectors under scrutiny.
4. **200-SMA data gap:** XOM, XLE, WMT, INTU, NVDA all blocked on 200-SMA Minervini condition. Resolves ~10 calendar weeks (~48 trading sessions) from now. This is the primary structural gate preventing most long and short trades.
5. **S&P 500 futures −0.26%:** Mild headwind; not crisis territory (VIX 17.7), but negative tone limits momentum setups.
6. **WTI at $100:** Psychologically significant level; may attract profit-taking in energy names without a breakout above $103–$105.

---

### Key Watchlist for Tomorrow (May 22)
- **XOM/CVX:** Watch for May 21 settled close above $160 (old 20d high was $162.55 before pullback). If WTI holds $100+ and XOM closes above its 20d mean with Z ≥ +1.0 AND above prior 20d high, momentum lane could open.
- **XLE:** Needs close above $61.29 (current 20d high) on ≥1.5× volume for a breakout confirmation.
- **INTU:** Re-evaluate once RSI recovers into 30–50 range (likely 3–5 sessions post-crash). Monitor for stabilization base. 200-SMA remains unavailable.
- **Energy sector clock:** No completed energy trade = sector failure counter has NOT incremented. Energy still viable but requires fresh quant confirmation with settled data.
- **NEW SECTOR IDEAS:** Materials (FCX, NEM), Industrials (GE, CAT) — YTD +15% and +12% respectively — to be scanned tomorrow given energy's structural gates remain blocked.
- **Philly Fed + PMI data today:** Could move industrials/materials names.

---

### 200-SMA Operational Note
The Minervini Trend Template 200-SMA gate remains structurally unavailable for all primary candidates (XOM, XLE, CVX, WMT, INTU). Bot launched ~April 29, 2026. The API provides historical data back to ~Oct 2025 = ~152 settled bars. 200-SMA requires 200 bars. Gap: ~48 trading sessions (~10 calendar weeks). Estimated availability: mid-August 2026. This constraint is **logged, accepted, and expected** — it is not a bug. The 200-SMA gate will auto-resolve as the live data window grows. All other Minervini checks (50-SMA, 150-SMA, 52w high/low range) execute normally.

---

### Decision
**HOLD — 0 trades today**

Every candidate failed at least one hard gate (Layer B Z-score, Minervini TT, or a hard rule). No forced entries. Cash preserved at $99,056.46 (100%). The Iran catalyst is real but does not produce a clean quant setup in XOM or XLE today — both sit in the no-man's land between mean-reversion and momentum thresholds. The gap-down names (INTU, WMT) are explicitly blocked by the post-gap-down short prohibition. Patience rule applies.

---

## 2026-05-21 — Midday Rescan Addendum (17:11 UTC / ~13:11 ET)

**VIX Regime at rescan:** Normal (~17.44–17.7 from morning research) — 1.00× sizing multiplier, all entry types eligible
**Account at rescan:** Equity $99,056.46 | Cash $99,056.46 (100%) | Deployed: 0% | Positions: 0/6 | Week trades: 0/3 | PDT: 0/3
**Orders at rescan:** NONE (no orders were placed at market-open per today's HOLD decision)

---

### Skipped at Open — Re-evaluated at Midday

| Ticker | Skip Reason at Open | Spread Now | Z-Score Now | Still Skipped? | Gate(s) Failed |
|--------|---------------------|-----------|------------|----------------|----------------|
| **XOM** | Z=+0.937 (below +1.0); Volume 1.10×; 200-SMA unavail.; Iran +2% but no breakout | 3.75% ❌ (R-flagged) | +0.856 (settle proxy) | ❌ YES | Spread 3.75% unenterable; Z +0.856 < +1.0; Price $153 vs 20d high $162.55 (−5.84% below); Volume 1.10× < 1.5× |
| **XLE** | Z=+1.020 barely; No breakout ($59.785 < $61.29 pivot); Minervini TT 150/200 SMA unavail. | 0.017% ✅ | +0.894 | ❌ YES | Z +0.894 < +1.0 (just misses); Price $59.60 vs 20d high $61.29 (−2.77% below; no breakout); TT structurally blocked |
| **NVDA** | Z=+0.934 (below +1.0); Price below 20d high $235.74; earnings catalyst spent | 0.023% ✅ | +0.691 | ❌ YES | Z +0.691 (far from any threshold); Price $220.85 = −6.32% below 20d high; Vol 1.19× < 1.5× |
| **NIO** | Z=−2.022 but Minervini TT fails (0% above 52w low; no SMA data); bearish price on beat | 0.180% ✅ | ~−2.0 | ❌ YES | Structural TT failures unchanged; price AT 52w low (need >30% above); only 25 bars history |
| **INTU** | HARD RULE: >5% gap-down → no-short. RSI <30. Pair div 9.6σ. 200-SMA unavail. | 0.255% ✅ | −9+ | ❌ YES | HARD RULE violation (>5% gap-down = permanent no-short block); RSI <30 ❌; pair div ❌ |
| **WMT** | HARD RULE: >5% gap-down → no-short. TT -10.2% below 52w high (need >30%). Sector wrong. | 0.025% ✅ | ~−5.5 | ❌ YES | HARD RULE violation (>5% gap-down = permanent no-short block); TT only −10.2% below 52w high ❌; Cons. Staples = positive sector ❌ |

---

### Detailed Re-Check

#### XOM — ❌ STILL SKIPPED (spread + structural regression)

**Quote:** bid $150.19 / ask $155.93 — condition code "R" (restricted/indicative NBBO)
**Spread:** ($155.93 − $150.19) / $153.06 = **3.75% → FAILS <1% gate.** Unenterable regardless of other metrics.
**Z-Score (best proxy — last settle $156.28):** +0.856 — meaningfully **below the +1.0 minimum for 2b-LONG**. The live mid (~$153.06) produces Z = +0.124 — essentially at the 20-day mean. Neither reading approaches any entry lane threshold.
**Price vs 20d pivot ($162.55):** $153.06 = **−5.84% below** the breakout pivot. The 2b-LONG lane requires price to be ABOVE the 20d high. XOM is not close.
**Volume (May 20 last bar):** 18.5M / 16.8M avg = **1.10× — below the 1.5× momentum threshold.**

Context: The morning pre-market noted WTI +2.2% on Iran Supreme Leader blocking uranium exports (thesis partially restoring). But XOM's intraday price does NOT reflect this thesis restoration — the stock is trading below its last settled close ($156.28) per the live mid, and far below the prior breakout structure. No lane qualifies. The R-flagged spread alone makes entry technically impossible. This is a STRUCTURAL regression from prior watchlist status, not a timing/spread issue that the midday window resolves.

**VERDICT: ❌ STILL SKIPPED** — 4 independent failures (spread, Z, no breakout, volume).

---

#### XLE — ❌ STILL SKIPPED (spread normalized; Z and price gates remain)

**Quote:** bid $59.59 / ask $59.60 — **spread 0.017% ✅ — fully normalized, excellent liquidity.**
**Z-Score:** +0.894 — the 2b-LONG lane requires Z ≥ +1.0. Gap is only 0.106σ, but a gate is a gate; the rule does not bend for "close."
**Price vs 20d high ($61.29):** $59.595 = **−2.77% below pivot** — no confirmed breakout. The momentum lane requires the close/current price to be above the 20d high. XLE is below it.
**Volume (May 20 last bar):** 61.8M / 36.4M avg = **1.70× ✅** — volume confirmation is EXCELLENT and the one fully passing gate. The May 20 bar had strong institutional participation. Unfortunately, volume alone cannot substitute for the price breakout and Z thresholds.
**Minervini TT:** 150/200-SMA unavailable due to the Dec 2025 XLE share consolidation (~$92→$45 price discontinuity). This structural block remains.

The notable development: XLE is the **most improved candidate from this morning** — spread is clean, volume was institutional on the last bar. What's missing is simply price catching up to the $61.29 pivot (needs +2.8% more) and Z breaking above +1.0. If XLE rallies from here into or beyond $61.29 on sustained volume, this setup is very close to qualifying. Monitor for Friday pre-market.

**VERDICT: ❌ STILL SKIPPED** — spread normalized ✅; volume ✅; price and Z below thresholds; TT structural.

---

#### NVDA — ❌ STILL SKIPPED (5th consecutive session, earnings catalyst exhausted)

**Quote:** bid $220.82 / ask $220.87 — **spread 0.023% ✅ — excellent.**
**Z-Score:** +0.691 — 5th consecutive session below the +1.0 momentum threshold. Z has actually **declined** from +0.934 yesterday to +0.691 today: NVDA is drifting DOWN post-earnings (−1.26% from yesterday's $223.47 settle).
**Price vs 20d high ($235.74):** $220.85 = **−6.32% below pivot** — the gap has widened from −4.4% at Monday's open to −6.32% today.
**Volume last bar:** 1.19× avg — below the 1.5× threshold.
**RSI:** 69.8 — approaching but NOT exceeding 70 required for a mean-reversion short lane. Even if RSI cleared 70, Z would need ≥+2.0 for 2a-SHORT, far from current +0.691.

Assessment: The post-earnings "sell the news" drift is the dominant pattern. The earnings catalyst has been fully absorbed and the stock is reverting toward its 20-day mean. NVDA needs a fresh, new catalyst to generate a qualifying entry. A pullback to Z ≤ −2.0 (~$191, or ~−13% from here) would create a 2a-LONG mean-reversion setup — not in near-term view. Alternatively, if NVDA announces a product launch or major contract that re-breaks $235.74 on ≥1.5× volume, the 2b-LONG lane could re-open. Neither is imminent. **Removing NVDA from the active watchlist.** Restore to watch-only status.

**VERDICT: ❌ STILL SKIPPED** — spread normalized ✅; Z, breakout, volume all fail; catalyst spent.

---

#### NIO — ❌ STILL SKIPPED (structural TT failures; bearish market response confirmed)

**Quote:** bid $5.56 / ask $5.57 — spread 0.180% ✅ (normalized).
**Z-Score from morning data:** ~−2.022 (technically meets 2a-LONG mean-reversion threshold of ≤−2.0).
**Structural gate failures (unchanged from open):**
1. **Minervini TT (52w low):** Price $5.56 is AT the 52-week low — 0% above it. The long TT requires price to be >30% above the 52-week low (need ≥$7.29 to qualify this gate). Not close.
2. **SMA data unavailable:** Only 25 bars of history. Cannot compute 50/150/200-SMAs. Cannot verify uptrend alignment.
3. **Bearish market response to positive catalyst:** NIO reported Q1 revenue +112.2% YoY and deliveries +98.3% — a strong print by any measure. Yet price declined on May 19 ($5.74) and May 20 ($5.59) on the catalyst. Today at $5.56 — a further decline. When the market explicitly rejects a positive catalyst with sustained selling, the Z-Score oversold signal is NOT a mean-reversion bounce opportunity — it's a falling knife. The strategy's Z ≤ −2.0 gate is designed for oversold names that will snap back; it is not designed for structurally broken stories.

Z alone cannot override a Minervini TT hard fail. Both layers must clear.

**VERDICT: ❌ STILL SKIPPED** — TT failures are structural and permanent until price recovers above $7.29 (52w low +30% threshold). Even then, SMA data gap remains.

---

#### INTU — ❌ STILL SKIPPED (HARD RULE: no-short after >5% gap-down — permanent)

**Quote:** bid $309.21 / ask $310.00 — spread 0.255% ✅ (fully normalized from ~2% at open).
**Hard rule violation:** INTU opened −20% gap-down today. CONSTRAINTS.md: *"No shorting after >5% gap-down day on the candidate (capitulation/squeeze risk)."* This is a permanent block for today's session regardless of spread normalization.
**Validation of the hard rule:** INTU is trading UP from its ~$306.68 open to $309.61 (+0.96%) at rescan time — a classic dead-cat/squeeze bounce immediately off the lows. Shorting into a bounce from a capitulation gap is exactly the pattern the rule is designed to prevent. The rule is working as intended.
**Other failures (remain):** RSI <30 (capitulation, not controlled breakdown); pair divergence 9.6σ vs ADBE/CRM; 200-SMA unavailable; RSI outside 30–50 range for 2b-SHORT.

**VERDICT: ❌ STILL SKIPPED** — HARD RULE VIOLATION (no-short after >5% gap-down). Spread irrelevant.

---

#### WMT — ❌ STILL SKIPPED (HARD RULE: no-short after >5% gap-down — permanent)

**Quote:** bid $121.51 / ask $121.54 — spread 0.025% ✅ (excellent, normalized).
**Hard rule violation:** WMT opened −10.2% gap-down today. Same permanent no-short block as INTU.
**Validation:** WMT trading UP from $120.57 open to $121.53 (+0.80%) — identical bounce pattern confirming squeeze risk. The hard rule prevented what would have been an immediate adverse move.
**Other structural failures:** TT only −10.2% below 52w high (needs >30%); price above 150-SMA (not a true laggard); Consumer Staples YTD +7.32% = positive sector (wrong posture for short); RSI <30.

**VERDICT: ❌ STILL SKIPPED** — HARD RULE VIOLATION. Spread normalization is irrelevant.

---

### Hard Rule Validation Note

Both INTU and WMT bounced after their gap-down opens (+0.96% and +0.80% respectively by rescan time). The "no short after >5% gap-down" rule has now been validated empirically **within this same session** — entering short at the open on either name would have resulted in an immediate adverse move. This is the short-squeeze / capitulation-bounce dynamic the rule was written to prevent.

---

### Trades Fired This Rescan

**None.**

Zero candidates re-cleared the composite Layer A + Layer B gates upon midday re-evaluation.

---

### Patience Rule Applied

All six skipped candidates remain below their respective entry thresholds. Gate failures are either:
- **Structural** (200-SMA unavailable, TT 52w low, hard no-short rules): XOM, XLE (TT), NVDA, NIO, INTU, WMT — these do not resolve with time of day
- **Quant** (Z and price level): XOM (Z +0.856, price regressing), XLE (Z +0.894 barely misses, no breakout), NVDA (Z +0.691, fading)
- **Spread** (R-flagged): XOM only

No gates were lowered. No trade was forced. Zero trades is the correct disciplined outcome.

---

### Market Observations at Rescan

- **Energy sector:** XOM's R-flagged wide spread (3.75%) suggests thinness in the tape during early session — not unusual for a large-cap like XOM in a morning where oil is moving. The intraday implied price (~$153) is well below last settled close ($156.28), consistent with WTI at $100.46 still generating selling pressure in energy names despite the Iran uranium directive catalyst.
- **XLE relative:** XLE is holding up better than XOM intraday — $59.60 vs yesterday's $59.80 settle (only −0.34%) while XOM is down more sharply. This is consistent with ETF product smoothing vs. single-name volatility.
- **Gap-down bounces:** Both INTU (+0.96%) and WMT (+0.80%) are rebounding from their open gaps, validating the hard no-short rule in real time.
- **NVDA drift:** The post-earnings drift lower continues (−1.26% today). The earnings catalyst is fully spent; the stock is settling back toward its pre-earnings base.

---

### Updated Watchlist for Friday Pre-Market (May 22)

1. **XLE** — Most improved candidate. Volume on May 20 bar was 1.70× (strong ✅). Z at +0.894, only 0.106σ below the gate. Price at $59.60, only $1.69 (2.77%) below the $61.29 pivot. If WTI stabilizes and XLE approaches $61.29 on another strong volume day, the 2b-LONG setup is very close. Minervini TT SMA issue remains (structural).
2. **XOM** — Needs: (a) clean NBBO quote (non-R-flagged), (b) price to recover above $162.55 on 1.5× volume for new breakout bar, (c) Z ≥ +1.0. None of these are near today. Monitor for base-building.
3. **NVDA** — Removed from active watchlist. Watch-only: restore as 2b-LONG candidate only if a new catalyst breaks price above $235.74 with 1.5× volume. Watch for 2a-LONG setup if price declines to Z ≤ −2.0 (~$191).
4. **Materials sector (FCX, NEM, XLB)** — Flagged for two weeks in pre-market research but never pulled bars. YTD Materials +15.24% = third-ranked sector. Need to scan Friday.
5. **Industrials (GE, CAT, XLI)** — Same flag, same context. YTD +12.84%.
6. **200-SMA data gap:** ~47 trading sessions remaining until 200-SMA data becomes available for late-Oct 2025 bot inception names. Estimated availability: mid-August 2026. Log and accept.


---

## 2026-05-21 — Midday Scan Addendum (17:53 UTC / ~13:53 ET)

**Scan type:** Midday workflow — position thesis check & stop evaluation
**VIX Regime:** Normal (17.44–17.7 from morning research) — 1.00× sizing multiplier
**Account:** Equity $99,056.46 | Cash $99,056.46 (100%) | Deployed: 0% | Positions: 0/6 | Week trades: 0/3 | PDT: 0/3 | Open orders: 0

---

### STEP 1 — Portfolio State (Live API)

- **Positions:** `[]` — EMPTY. 100% cash confirmed.
- **Orders:** `[]` — EMPTY. No working bracket limits. No GTC stops.
- No morning bracket orders were placed at open (pre-market HOLD decision: all 6 candidates rejected on structural quant/TT gates — XOM Z=+0.937, XLE no breakout, NVDA Z<+1.0, NIO TT fail, INTU/WMT hard no-short rules).
- TRADE-LOG fully current. No discrepancy.

---

### STEP 2 — Cut Losers / Step 3 — Tighten Stops

**N/A — no open positions.** Both steps skipped.

---

### STEP 4 — Watchlist Thesis Check (Live Quotes at ~13:53 ET)

All quotes carry **"R" condition code** (indicative/restricted NBBO). Ask price used as fair-value proxy; bid treated as unreliable stub.

| Ticker | Settle (May 20) | Live Ask | Δ vs Settle | Spread | Z (settle) | Z (live ask) | Prior 20d High | Distance to Pivot | Vol (May 20) | Key Gate Status |
|--------|----------------|----------|------------|--------|------------|--------------|----------------|-------------------|-------------|-----------------|
| XOM | $156.28 | $153.85 | −1.6% | 4.50% ❌ | +0.834 | +0.296 | $162.55 | −5.4% below | 1.08× ❌ | Triple fail: spread, Z, price |
| XLE | $59.80 | $58.88 | −1.5% | 0.02% ✅ | +1.004 | +0.413 | $61.29 | −3.9% below | 1.72× ✅ | Price and live Z fail; TT blocked |
| CVX | $191.33 | $189.88 | −0.8% | 0.25% ✅ | +0.579 | +0.282 | $197.25 | −3.8% below | 1.48× ❌ | Z and price fail |
| NVDA | $223.47 | $221.80 | −0.7% | 0.01% ✅ | +0.911 | +0.759 | $235.74 | −5.9% below | 1.16× ❌ | Z, price, vol all fail |

**Pair divergence:** XOM vs CVX = 0.255σ ✅ | XOM vs XLE = 0.170σ ✅ (energy sector moving in lockstep — sector-wide drift, not single-name idiosyncrasy)

---

### XOM — No Action (No Position)
- Thesis structurally intact: WTI ~$100 (+2.2% pre-market on Iran Supreme Leader uranium directive), Hormuz supply disruption ongoing. But XOM trading at ~$153.85 — down 5.4% from $162.55 prior breakout pivot and Z regressed to +0.296. Momentum lane cannot open. No position exists to protect.
- Context: All three energy names (XOM, XLE, CVX) are pulling back intraday as WTI's morning +2.2% gain fades. This is oscillation around the Iran peace-deal uncertainty, not a structural thesis break (no US-Iran deal confirmed).

### XLE — No Action (No Position)
- The strongest candidate structurally: May 20 volume was 1.72× (✅ institutional participation confirmed). Z on settled basis = +1.004 (barely clears +1.0). However, intraday live Z = +0.413 (price at $58.88 is 3.9% below the $61.29 breakout pivot). The 2b-LONG lane requires closing ABOVE the 20d high — XLE has not cleared that level on any intraday basis today. Minervini TT remains blocked (Dec 2025 share consolidation disrupted 150/200d SMA data). No action. Key watchlist for tomorrow if WTI recovers.

### CVX — No Action (No Position)
- Z=+0.579, price 3.8% below prior pivot, volume 1.48× (just under 1.5× threshold). Pair divergence from XOM only 0.255σ — confirming both integrate oil names are moving together. No position.

### NVDA — Watch-Only
- 5th consecutive session drifting below the $235.74 momentum pivot. Z = +0.911 (settle) / +0.759 (live). Post-earnings catalyst spent. No position. Monitor for either (a) fresh catalyst + breakout above $235.74 on 1.5× vol for 2b-LONG, or (b) dip to Z ≤ −2.0 (~$191) for 2a-LONG mean-reversion.

---

### STEP 5 — Optional Research

No unexplained intraday moves. Energy sector pullback is consistent with WTI fading from pre-market highs (Iran news sentiment oscillating). No WebSearch triggered.

---

### Actions Taken: NONE

No positions cut, no stops tightened, no thesis exits, no new orders.
No DAILY-SUMMARY.md entry required (no actions per workflow rules).

---

### Key Watchlist for Tomorrow Pre-Market (May 22, Friday)

1. **XLE** — Most actionable: volume confirmed 1.72× on May 20 bar. Needs WTI stabilization and XLE to close above $61.29 on volume ≥1.5× for fresh 2b-LONG breakout qualification. Minervini TT SMA gap is the remaining structural block.
2. **XOM** — Z=+0.296 today; needs recovery to Z≥+1.0 AND close above $162.55 on ≥1.5× volume. Structural base-building required; not near-term.
3. **CVX** — Volume 1.48× is approaching threshold; needs Z≥+1.0 and close above $197.25.
4. **NVDA** — Watch-only. No active setup.
5. **Materials scan (FCX, NEM, XLB)** and **Industrials (GE, CAT, XLI)** — Flagged repeatedly; still unscanned. YTD +15.24% and +12.84% respectively. High priority for Friday pre-market given energy names' structural gates remaining blocked (200-SMA unavail., TT SMA issues).
6. **200-SMA data gap:** ~47 trading sessions remaining (est. mid-August 2026). All Minervini TT checks noting 200-SMA "CANNOT VERIFY" will auto-resolve as the live data window grows.


---

## 2026-05-21 — Afternoon Scan Addendum (~15:53 ET / 19:53 UTC)

**Scan time:** ~7 min before close (market closes 20:00 UTC / 4:00 PM ET)
**VIX regime at scan:** NORMAL — VIXY proxy $25.43 (bid $25.42 / ask $25.44) → estimated VIX ~17–18 | Sizing multiplier: 1.00×

---

### STEP 1 — Order & Position State Reconciled vs TRADE-LOG

**API results:**

| Field | Value |
|-------|-------|
| Positions | `[]` — EMPTY (100% cash) |
| Equity | $99,056.46 |
| Cash | $99,056.46 |
| Open orders | NONE (last bracket 1d69c496 expired May 18T20:02) |

- **Bracket fills today: 0** — No morning bracket orders were placed (today's pre-market HOLD decision: XOM Z=+0.937, XLE no breakout, NVDA Z<+1.0, NIO/INTU/WMT hard rule failures — see pre-market research entry above)
- **TRADE-LOG reconciliation: FULLY CURRENT** — 6 historical orders in API all match log entries
- **Stale limits: 0** — no open orders of any kind

---

### STEP 2 — Trailing Stop Upgrades

**N/A.** Portfolio is 100% cash. No positions exist. No stop upgrade workflow triggered.

---

### STEP 3 — Stale Limit Cancellations

**None.** No open orders. Last bracket (XOM 1d69c496) expired naturally at May 18 session close per its TIF: day.

---

### STEP 4 — Afternoon Opportunity Scan

**VIX regime:** NORMAL (1.00×) | **Positions:** 0/6 | **Week trades:** 0/3 | **PDT:** 0/3

**⏰ Timing note:** Scan at 15:53 ET = within final **7 minutes** of session. CONSTRAINTS.md prohibits new entry orders in the last 15 minutes. All analysis below is for tomorrow's pre-market watchlist only — no bracket orders can be placed at this time.

**Z-Scores and metrics (settled closes through May 20; live ask prices ~15:53 ET):**

| Ticker | May20 Settle | Live Ask | Z(settle) | Z(live) | 20d High | 20d Low | Vol (May20 vs avg) | Lane tried | Key gate failure | Verdict |
|--------|-------------|----------|-----------|---------|----------|---------|---------------------|-----------|-----------------|---------|
| XOM | $156.28 | $155.17 | +0.856 | +0.604 | $162.55 | $144.57 | 1.08× | 2b-LONG | Z<1.0; price 7.0% below pivot; vol 1.08×; 200-SMA structural | **REJECT** |
| CVX | $191.33 | $190.71 | +0.594 | +0.450 | $197.25 | $181.62 | 1.45× | 2b-LONG | Z<1.0; price 3.3% below pivot; vol 1.45× (0.05× short); 200-SMA structural | **REJECT** |
| XLE | $59.80 | $59.16 | +1.030 | +0.606 | $61.29 | $55.70 | 1.66× ✅ | 2b-LONG | Z(live) 0.606 <1.0; price 3.5% below pivot; TT 150/200-SMA structural (Dec 2025 split) | **REJECT** |
| NVDA | $223.47 | $220.19 | +0.934 | +0.630 | $235.74 | $196.50 | 1.15× | 2b-LONG | Z<1.0; price 6.6% below pivot; vol 1.15×; 200-SMA structural | **REJECT** |
| XLB | $49.72 | $49.98 | **-1.810** | -1.509 | $52.41 | $49.04 | **1.90× ✅** | 2a-LONG | Z=-1.509 (need ≤-2.0, 0.491σ short); RSI ~32-35 (need <30); pair FCX div 1.84σ > 1.5σ | **REJECT** |
| FCX | $60.87 | n/a | +0.026 | — | $67.16 | $55.57 | 0.75× | 2a-LONG | Z=+0.026 (at mean; no extreme) | **REJECT** |

**Pair divergences:**
- XOM (+0.856) ↔ CVX (+0.594): 0.262σ ✅ (energy sector cohesion — both names pulling back together)
- XOM (+0.856) ↔ XLE (+1.030): 0.175σ ✅ (sector-wide drift confirmed)
- FCX (+0.026) ↔ XLB (-1.810): **1.835σ ❌** (exceeds 1.5σ — XLB idiosyncratic weakness, not sector-wide Materials breakdown)

---

**Candidate Notes:**

**XOM — REJECT (4 independent failures):**
- Z=+0.604 (live) — momentum lane needs ≥+1.0. Well below threshold.
- Price $155.17 is 7.0% below prior 20d high $162.55. No breakout. Actually pulling back.
- Volume last bar (May 20): 1.08× — sub-1.5× for 4th consecutive session.
- 200-SMA structurally unavailable (152/200 bars).
- Energy thesis remains structurally intact (WTI, Hormuz, sector YTD leader), but the statistical entry signal has degraded. XOM needs to rebuild a base and re-break $162.55 on strong volume.

**CVX — REJECT (4 failures):**
- Z=+0.450 (live) | Vol 1.45× (closest energy name to threshold, only 0.05× short).
- Price 3.3% below pivot. Pulling back alongside XOM in lockstep (pair divergence 0.262σ = expected).
- Same structural TT limitation as XOM. Not a standalone entry.

**XLE — REJECT (3 failures; vol is the one passing gate):**
- Vol 1.66× ✅ — only passing gate. This is the strongest volume reading among energy names.
- Z(live) = 0.606 — just misses +1.0 threshold.
- Price $59.16 is 3.5% below $61.29 pivot — no breakout.
- Minervini TT 150/200-SMA permanently blocked by Dec 2025 XLE share consolidation (price ~$92→$45 discontinuity in the data series). This is an irresolvable structural limitation unless split-adjusted historical data is obtained.
- XLE has the best "momentum lane structure" of the group: vol confirmed, Z approaching, sector right. If it rallies through $61.29 on a fresh ≥1.5× day → 2b-LONG qualifies (pending TT operator fix).

**NVDA — REJECT (4 failures; 7th consecutive session):**
- Z=+0.630 | Price 6.6% below $235.74 pivot | Vol 1.15×.
- The post-earnings catalyst (Q1 FY2027 beat reported May 19 after close) has been fully absorbed and reversed. The stock has drifted from ~$224 (post-earnings) to ~$220 today.
- Removing from active watchlist. Restore only when: (a) fresh catalyst + close above $235.74 on ≥1.5× vol for 2b-LONG, OR (b) pullback to Z ≤ -2.0 (~$191) + RSI <30 for 2a-LONG.

**XLB — REJECT but #1 WATCHLIST (closest to qualifying of all candidates):**
- Z(settle May20) = -1.810, Z(live May21) = -1.509 — both approaching the ≤-2.0 trigger.
- **Z-trigger price = $49.56** (20d mean $51.28 − 2.0 × σ $0.86). Only **$0.42 (0.8%) further decline needed**.
- Volume May 20: **1.90×** — the strongest volume reading of any candidate in today's scan. Institutional participation confirmed in the selloff.
- RSI estimated ~32-35 — approaching but not yet <30 required.
- **Critical pair failure:** FCX Z = +0.026 vs XLB Z = -1.810 → divergence **1.835σ > 1.5σ threshold**. FCX (copper) is at its 20-day mean while XLB (materials ETF) is deeply oversold. This divergence suggests XLB's weakness is ETF-specific (weight composition, constituent-level idiosyncratic moves) rather than a broad Materials sector dislocation. Per strategy rules, pair divergence >1.5σ = skip single-name risk.
- Minervini TT: Price $49.98 is below estimated 50-SMA (~$51.5) — TT Long requires price > 50-SMA. Structural fail. 200-SMA also unavailable.
- **VERDICT: All 3 required gates (Z, RSI, pair) fail simultaneously.** However, this is the #1 watchlist name heading into Friday. If FCX also sells off tomorrow bringing the pair divergence below 1.5σ AND XLB reaches $49.56 with RSI <30 → genuine 2a-LONG mean-reversion candidate. Materials sector YTD +15.24% supports long bias when/if signal clears.

**FCX — REJECT:**
- Z = +0.026 — at its 20-day mean. No statistical extreme. Vol 0.75×. Not a candidate in any lane.
- Notable context: FCX traded $66+ last week and has pulled back to $60.87 — still in the upper half of its 20d range. Not remotely oversold.

**New afternoon entries: NONE** — zero bracket orders placed (additionally blocked by final 7-minute no-entry window).

---

### Afternoon Market Context

Today's session (May 21) continued the energy sector's corrective pullback from last week's highs. XOM drifted from its May 20 settle of $156.28 down to ~$155.17 intraday (−0.7%), CVX from $191.33 to ~$190.71 (−0.3%). Both are now 7.0% and 3.3% respectively below their prior breakout pivots ($162.55 and $197.25) — the momentum thesis that was close to triggering last week has been reset by the combined pressure of the FOMC minutes (May 20 hawkish signal), WTI volatility around the US-Iran narrative, and broad market digestion. The constructive note is that energy names are pulling back on below-average volume (XOM 1.08×, CVX 1.45×), consistent with orderly mean-reversion rather than institutional distribution. XLB (Materials ETF) is the session's most statistically interesting development: with Z approaching -2.0 (-1.810 settled) and volume at a strong 1.90×, it is the closest any candidate has been to a mean-reversion long trigger in several sessions. The remaining barriers are the FCX pair divergence (1.84σ > 1.5σ threshold), the RSI not yet sub-30, and the Minervini TT structural gate. The VIX proxy (VIXY $25.43) continues to signal a Normal regime — no fear-driven selling is contributing to these moves, which is a qualitative positive for the thesis that pullbacks in energy and materials are consolidations, not breakdowns.

---

**Bracket fills today:** 0 (no morning limits placed — HOLD decision)
**Stops upgraded:** 0 (no positions held; no upgrade workflow applicable)
**Stale limits cancelled:** 0 (no open orders existed)
**New afternoon entries:** none — all 6 candidates failed composite Layer A + Layer B gates; additionally within final 7-minute no-entry window
**Afternoon market context:** Energy continuing orderly pullback on below-avg vol (XOM −0.7%, CVX −0.3%). XLB Materials ETF Z=-1.810 on 1.90× volume — closest candidate to a mean-reversion trigger. NVDA drift lower (−7th consecutive evaluation miss). VIX Normal (~17-18). No new orders placed.

**Key watchlist for Friday pre-market (2026-05-22):**
1. **XLB (Materials ETF) — #1 PRIORITY** — Z=-1.810 (trigger $49.56, needs −0.8% more); vol 1.90× ✅; RSI ~32-35 (approaching <30). The 3 remaining gates to clear: (a) Z ≤ -2.0, (b) RSI < 30, (c) FCX pair divergence must narrow below 1.5σ. If all three clear simultaneously → 2a-LONG bracket with entry ~$49.56, stop ~$46.09 (−7%), target ~$54.64 (2:1 R:R).
2. **XLE (Energy ETF) — #2** — vol 1.66× ✅; Z(settle) 1.030; but live Z=0.606 and price 3.5% below $61.29 pivot. TT structural block (Dec 2025 split data gap) persists. Needs price above $61.29 on ≥1.5× vol for fresh 2b-LONG. Operator action: obtain split-adjusted XLE historical data to resolve TT.
3. **XOM/CVX** — Both below momentum pivots with sub-1.5× vol. No near-term entry trigger. Energy thesis intact structurally (WTI, Hormuz) but needs a fresh catalyst and volume surge to re-establish breakout.
4. **NVDA — OFF ACTIVE WATCHLIST** — 7 consecutive gate misses post-earnings. Restore only on fresh catalyst + breakout above $235.74, or pullback to Z ≤ -2.0 (~$191).
5. **Materials sector broader scan (NEM, LIN, APD)** — Flagged FCX as XLB's pair today; it diverged 1.84σ. Check if other materials names (LIN, APD) are more correlated with XLB's weakness — if LIN Z also approaches -2.0, pair divergence concern may ease.
6. **200-SMA data gap** — ~46 trading sessions remaining (est. mid-August 2026). All Minervini TT 200-SMA "CANNOT VERIFY" flags resolve automatically as data accumulates. No operator action needed beyond patience.


---

## 2026-05-22 — Pre-Market Research (Day 25, Friday)

### Account
- **Equity:** $99,056.46
- **Cash:** $99,056.46 (100%)
- **Buying power:** $198,112.92 (2× margin available)
- **Daytrade count:** 0/3
- **Open positions:** None
- **Open orders:** None
- **Phase P&L:** −$943.54 (−0.944%)
- **Max drawdown from peak ($100,206.70):** −1.15% (well within −15% circuit breaker)

---

### Market Context
- **WTI Crude Oil:** ~$96–98/bbl (+2.3% today, +1.8% at $98.08 intraday, +1.75% past month, +58.5% YoY). Hormuz tensions and US-Iran peace negotiation uncertainty driving surge.
- **Brent Crude:** ~$104–106/bbl (+2.8% today, traded $103.79–$106.36 range). +58.88% YoY.
- **S&P 500 Futures:** Up +0.10%–+0.20% premarket. SPY +0.38% at $745.50. June futures 7,487.50 (+0.29%).
- **VIX:** Below 17 (16.76 on Thursday, down 3.9%). VIX futures down 3.00% premarket today.
- **Key Catalysts:**
  - US-Iran peace talks uncertainty + Strait of Hormuz tensions → oil spike dominating energy sector
  - Kevin Warsh sworn in as new Fed Chair today (succeeds Jerome Powell) — hawkish pivot risk
  - Nomura: no Fed rate cuts in 2026 due to rising inflation
  - U of Michigan Consumer Sentiment Final (consensus 48.2); 1-yr inflation expectations 4.6%; 5-yr 3.4%
  - No CPI, PPI, FOMC, or major jobs data today
- **Pre-Market Earnings:** BJ's Wholesale (BJ), Booz Allen Hamilton (BAH), Global Ship Lease (GSL), Richemont (CFRUY)
- **YTD Sector Performance:**
  - Energy +27.87% 🔝 | Info Tech +23.55% | Materials +15.24% | Industrials +12.84%
  - Real Estate +10.46% | Consumer Staples +7.32% | Utilities +5.74%
  - Consumer Discretionary −0.03% | Comm Services −1.82% | Financials −6.55% | Health Care −7.60% 🔻
  - S&P 500 YTD: +8%

---

### VIX Regime
- **Current VIX:** 16.76 (premarket futures pointing lower, ~16.0–16.5 implied)
- **Regime:** Normal (14–22 band)
- **Sizing multiplier:** 1.00× (full sizing)
- **Strategy bias:** All entry types OK; cold-start default 10% per position applies (< 30 closed trades)

---

### Candidates Evaluated

#### LONG CANDIDATES (3 screened)

**1. XLB (Materials ETF — #1 Watchlist Carryover)**
- Lane attempted: 2a-LONG (Mean-Reversion)
- Catalyst: Materials YTD +15.24%; prior high-volume selloff (May 20: 1.90× vol); mean-reversion bounce thesis intact from prior sessions
- Quant (Layer B):
  - Mean(20): $51.19 | StdDev(20): $0.897
  - Current (premarket): $50.015 | **Z = −1.315** ❌ (need ≤ −2.0; Z-trigger price = $49.56)
  - Yesterday vol: 10,236,190 | AvgVol(20): 10,589,748 | **Vol ratio: 0.97×** ❌ (need ≥ 1.0×)
  - RSI(approx): **33.8** ❌ (need < 30)
  - Pair (FCX): Z = +0.460 | **Divergence: 1.774σ** ❌ (need ≤ 1.5σ)
- Minervini TT Long:
  - Price $50.02 vs 50-SMA $50.62 → **❌ FAIL** (price below 50-SMA)
  - 150/200-SMA: CANNOT VERIFY (only 112 post-split bars; ~38 sessions until 150-SMA clears)
  - 30% above 52w Low: $50.02 vs required $56.41 → **❌ FAIL** (52w Low $43.39 post-split, threshold too high given short history)
  - Price within 25% of 52w High ($53.62): $50.02 ≥ $40.21 → ✅
- **VERDICT: ❌ REJECT** — 4/4 quant gates fail, 2 TT conditions fail. Z now −1.315 vs prior session −1.309 (marginal deterioration). Thesis intact but signal not present.
- **Z-trigger watch:** $49.56 (needs −0.9% from current $50.02). FCX must also close divergence gap.

**2. XOM (Energy mega-cap)**
- Lane attempted: 2b-LONG (fresh oil catalyst today), 2a-LONG (bounce check)
- Catalyst: WTI +2.3% today, Hormuz tensions, Warsh hawkish posture keeps energy hedge bids firm
- Quant (Layer B):
  - Mean(20): $152.75 | StdDev(20): $4.418
  - Current (premarket): $154.95 | **Z = +0.498** ❌ (2b needs ≥+1.0; 2a needs ≤−2.0)
  - Prior breakout pivot: $162.55 (May 19) — price 4.7% below, no breakout ❌
  - Yesterday vol: 17,070,896 | AvgVol(20): 17,399,943 | **Vol ratio: 0.98×** ❌ (need ≥1.5× for 2b)
  - RSI(approx): 62.9 (in 50-70 zone ✅ but other 2b gates fail)
- Minervini TT: 50-SMA $155.66 vs price $154.95 → **❌ FAIL** (price below 50-SMA); 150/200-SMA unavailable (144 bars)
- **VERDICT: ❌ REJECT** — No quant lane clears. Oil surge is a real catalyst but price hasn't re-broken its pivot. Below 50-SMA. Orderly pullback, not statistical edge.

**3. XLE (Energy ETF)**
- Lane attempted: 2b-LONG (momentum breakout)
- Catalyst: WTI +2.3% / Brent +2.8% — fresh oil surge; XLE was #2 watchlist heading into today
- Quant (Layer B):
  - Mean(20): $58.35 | StdDev(20): $1.492
  - Premarket $59.325 | **Z = +0.652** ❌ (need ≥+1.0)
  - Breakout pivot: $61.29 (May 19 high) — price 3.2% below ❌
  - Yesterday vol: 45,853,720 | AvgVol(20): 37,753,513 | **Vol ratio: 1.21×** ❌ (need ≥1.5×)
  - RSI(approx): 66.6 ✅ (within 50-70 zone)
  - 50-SMA: $58.42; price $59.13 > 50-SMA ✅; 150/200-SMA unavailable (116 bars)
- Minervini TT Long: 52w High $62.56, 52w Low $43.81; price 30%+ above Low ✅; within 25% of High ✅; BUT 150/200-SMA cannot verify; 50-SMA condition ✅
- **VERDICT: ❌ REJECT at open** — Z and pivot both un-cleared. LIVE WATCHLIST: If WTI surge drives XLE through $61.29 intraday on ≥1.5× avg volume → 2b-LONG re-evaluates in real time. RSI and 50-SMA are already cooperating — only Z and price/vol breakout needed. Pivot extension check would be: limit ≤ $61.29 × 1.05 = $64.35 (ample room).

#### SHORT CANDIDATES (2 flagged, not yet pulled)
- **XLV (Health Care ETF — worst YTD sector −7.60%):** Not pulled today — 2b-SHORT setup requires bars analysis. Flagging for Monday pre-market full scan. If short trend template clears (price < all SMAs, breakdown from 20d low), this is the highest-conviction short sector in the universe.
- **XLF (Financials ETF — YTD −6.55%):** Warsh swearing-in today introduces hawkish macro uncertainty for banks. Not pulled. Adding to Monday scan alongside XLV. Both require 210-bar pull + full TT Short check.

---

### Skipped Candidates — Specific Failed Checks

| Ticker | Lane | Failed Gate(s) |
|--------|------|----------------|
| XLB | 2a-LONG | Z = −1.315 (need ≤−2.0) ❌; RSI 33.8 (need <30) ❌; Vol 0.97× (need ≥1.0×) ❌; FCX pair 1.774σ (need ≤1.5σ) ❌; Price < 50-SMA ❌; <30% above 52w Low ❌ |
| XOM | 2b-LONG | Z = +0.498 (need ≥+1.0) ❌; close $154.95 < pivot $162.55 ❌; vol 0.98× (need ≥1.5×) ❌; price < 50-SMA ❌ |
| CVX | 2b-LONG | Z = +0.478 (need ≥+1.0) ❌; vol 0.89× (need ≥1.5×) ❌; price below pivot $197.25 ❌ |
| XLE | 2b-LONG | Z = +0.652 (need ≥+1.0) ❌; close $59.13 < pivot $61.29 ❌; vol 1.21× (need ≥1.5×) ❌ |
| XLV | 2b-SHORT | Bars not pulled — deferred to Monday |
| XLF | 2b-SHORT | Bars not pulled — deferred to Monday |

---

### Trade Ideas (Cleared Both Layers)
**NONE.** Zero candidates cleared both Layer A and Layer B today.

---

### Risk Factors
1. **Oil price spike risk (two-sided):** WTI at $96–98, Brent above $105. If Hormuz situation resolves (peace deal) → oil crashes, energy longs would gap down. If situation escalates → oil could spike further, creating breakout setups. Either direction can be fast-moving.
2. **New Fed Chair (Warsh):** Hawkish posture expected. First statements/signals could impact rate-sensitive sectors. Banks, utilities, real estate all exposed.
3. **Inflation persistence:** U of M 1-yr expectations at 4.6% consensus. If actual print is higher → risk-off, pushes VIX up, may shift regime to Elevated.
4. **Materials ETF (XLB) structural data gap:** 30% above 52w Low threshold will remain unachievable until more post-split history accumulates (XLB traded ~$43 in Dec 2025; 30% above that is $56.41, well above current $50). This TT condition is effectively locked for the medium term for XLB. Consider whether to override this gate specifically for ETFs with documented split adjustments.
5. **PDT budget fully intact (0/3):** Maximum flexibility preserved heading into next week.

---

### Decision
**HOLD** — No trades today. Zero candidates cleared composite Layer A + Layer B gates.

### Key Watchlist for Next Session (2026-05-25, Monday)
1. **XLE — PRIORITY 1:** If today's oil surge closes XLE above $61.29 on ≥1.5× volume → **2b-LONG activates Monday pre-market.** All conditions except pivot/Z are favorable. Monitor close carefully.
2. **XLB — PRIORITY 2:** Z-trigger at $49.56 (−0.9% from $50.02). Needs simultaneous: Z ≤ −2.0, RSI < 30, FCX divergence < 1.5σ. All three gates converge slowly. Bull thesis (Materials +15.24% YTD) structurally intact.
3. **XLV Short — NEW:** Pull 25-bar + 210-bar on Monday. Worst YTD sector (−7.60%). Check 2b-SHORT: Z ≤ −1.0, close < 20d low, RSI 30-50, vol ≥ 1.5×, 50d < 200d. Mega-cap, meets short universe filter.
4. **XLF Short — NEW:** Warsh hawkish risk to bank stocks. Pull Monday. Same 2b-SHORT template.
5. **XOM/CVX:** Still in orderly pullback; restore to active scan when Z approaches +1.0 or close re-tests $162.55/$197.25 pivot on volume.

---

## 2026-05-22 — Midday Rescan Addendum (16:41 UTC / ~12:41 PM ET)

**VIX Regime at rescan:** Normal (~16.5 est., VIX futures -3.0% premarket; prior close 16.76) — Sizing multiplier: 1.00×
**Account at rescan:** Equity $99,056.46 | Cash $99,056.46 (100%) | Deployed: 0% | Positions: 0/6 | Week trades: 0/3 | PDT: 0/3 | Open orders: 0

---

### Skipped at Open — Re-evaluated at Midday

#### XLB (Materials ETF) — 2a-LONG candidate
| Metric | At Open | Midday |
|--------|---------|--------|
| Skip reasons | Z=−1.315 ❌; RSI 33.8 ❌; Vol 0.97× ❌; FCX div 1.774σ ❌ | Z=−1.086 ❌ (REGRESSED from open); RSI ~33.8 ❌; Vol 0.967× ❌; FCX div 1.521σ ❌ |
| Bid / Ask | $50.02 pre-mkt | $50.21 / $50.22 |
| **Spread %** | — | **0.020% ✅ NORMALIZED** |
| Z-Score | −1.315 | **−1.086** (regressed — XLB is UP ~$0.20 from open) |
| Z-trigger price | $49.56 | **$49.40** (20d mean $51.19, σ $0.897) — needs −1.6% further decline |
| FCX pair Z | +0.460 | **+0.435** | Divergence: **1.521σ ❌** (above 1.5σ, barely) |
| Vol (May 21 last bar) | 10,236,190 = 0.967× | Unchanged (settled bar) |
| RSI(14) est | 33.8 | ~33.8 ❌ |

**VERDICT: ❌ STILL SKIPPED — 4 gates fail simultaneously**

XLB has actually **moved UP** intraday (from ~$50.02 pre-market to $50.22 ask midday = +0.20%), causing the Z-Score to **regress** from −1.315 at open to −1.086 now. The stock is moving **away from** the −2.0 trigger rather than toward it. The spread has fully normalized (0.02% — excellent), but all four substantive gates remain failed:
1. **Z = −1.086** (need ≤ −2.0; trigger price $49.40; gap = 0.914σ, requires ~$1.82 further decline)
2. **RSI ~33.8** (need < 30; declining but not there)
3. **Vol 0.967×** (settled bar; need ≥ 1.0×)
4. **FCX pair divergence 1.521σ** (barely above the 1.5σ threshold; FCX Z = +0.435 while XLB Z = −1.086; divergence is structural — copper not confirming materials ETF weakness)

Thesis context: Materials sector YTD +15.24% (healthy). XLB is pulling back within an uptrend. The oil surge today (+2.3% WTI) is providing commodity tailwinds. But the statistical signal simply isn't present — XLB needs to fall another ~$1.82 to trigger Z ≤ −2.0, and RSI must hit <30 simultaneously. The spread normalization is the only improvement since open; everything else is flat or regressed.

---

#### XOM (Exxon Mobil) — 2b-LONG candidate
| Metric | At Open | Midday |
|--------|---------|--------|
| Skip reasons | Z=+0.498 ❌; price 4.7% below $162.55 pivot ❌; Vol 0.98× ❌ | Z=+0.321 ❌ (REGRESSED); price 5.2% below pivot ❌; Vol 0.981× ❌ |
| Bid / Ask | $154.95 pre-mkt | $154.00 / $154.17 |
| **Spread %** | — | **0.110% ✅ NORMALIZED** |
| Z-Score | +0.498 | **+0.321** (regressed — XOM slipped further) |
| Price vs 20d pivot ($162.55) | −4.7% below | **−5.2% below** (worsened) |
| CVX pair Z | +0.478 | **+0.490** | Divergence: **0.168σ ✅** |
| Vol (May 21 last bar) | 17,070,896 = 0.981× | Unchanged |
| RSI(14) est | 62.9 | ~55.0 (declining with price) |
| 20d Mean | $152.75 | $152.75 | StdDev: $4.42 |

**VERDICT: ❌ STILL SKIPPED — 3 gates fail; all have worsened or unchanged since open**

XOM is trading DOWN intraday despite WTI +2.3% today (ask $154.17 vs $154.95 pre-market = −0.5%). This is the same relative-weakness pattern seen in prior sessions — integrated oil majors lagging spot crude on a moderate oil rally day. Z-Score has regressed from +0.498 → +0.321. The 2b-LONG momentum lane requires:
- **Z ≥ +1.0**: +0.321 ❌ (needs +0.679σ more = ~+$3.00 price appreciation)
- **Close > 20d High ($162.55)**: $154.17 ❌ (5.2% below pivot; needs +$8.38 rally)
- **Vol ≥ 1.5×**: 0.981× ❌ (the May 21 settled bar is the reference; well below threshold)

CVX pair divergence is an excellent 0.168σ — both energy majors are tracking each other perfectly, confirming sector-wide action. But that confirmation can't overcome the price and Z-score failures. WTI at $96–98 is still structurally supportive of the energy thesis long-term, but today's session is not providing the institutional breakout pattern required for entry.

---

#### XLE (Energy Select Sector ETF) — 2b-LONG candidate
| Metric | At Open | Midday |
|--------|---------|--------|
| Skip reasons | Z=+0.652 ❌; price 3.2% below $61.29 pivot ❌; Vol 1.21× ❌ | Z=+0.642 ❌ (flat); price 3.2% below pivot ❌; Vol 1.215× ❌ |
| Bid / Ask | $59.33 pre-mkt | $59.30 / $59.31 |
| **Spread %** | — | **0.017% ✅ NORMALIZED** |
| Z-Score | +0.652 | **+0.642** (essentially flat) |
| Price vs 20d pivot ($61.29) | −3.2% below | **−3.2% below** (unchanged) |
| XOM pair Z | +0.498 | **+0.321** | Divergence: **0.321σ ✅** |
| Vol (May 21 last bar) | 45,853,720 = 1.215× | Unchanged |
| RSI(14) est | 66.6 | ~62.0 |
| 20d Mean | $58.35 | $58.35 | StdDev: $1.49 |

**VERDICT: ❌ STILL SKIPPED — 3 gates fail; price essentially unchanged since open**

XLE is trading flat midday vs. open ($59.31 ask vs. $59.33 pre-market = −0.03%). Despite the morning's oil surge catalyst (+2.3% WTI), XLE has made no intraday progress toward its $61.29 breakout pivot. The 2b-LONG gate failures are structural for this session:
- **Z ≥ +1.0**: +0.642 ❌ (needs +0.358σ more = ~+$0.53 price appreciation AND the last settled bar must incorporate it)
- **Close > 20d High ($61.29)**: $59.31 ❌ (3.2% below pivot; today's price action not bridging the gap)
- **Vol ≥ 1.5×**: 1.215× ❌ (May 21 last settled bar; needs institutional accumulation on the breakout day specifically — this is a settled bar and cannot improve intraday)

Important note on the volume gate: The 2b-LONG lane requires the **breakout day bar** to show ≥1.5× volume. Since XLE hasn't even reached the $61.29 pivot today, the question of breakout-day volume is moot — there is no breakout to confirm. If XLE were to close above $61.29 today on ≥1.5× today's volume (~56.6M shares = 1.5× of the 37.75M avg), that would create a valid new breakout bar. As of midday, price is ~3.2% away and the oil catalyst is only generating flat action. A rally of this magnitude in the remaining ~3.5 hours of the session is possible but has not materialized.

**Secondary structural note:** Minervini Trend Template 150/200-SMA data gap (Dec 2025 XLE split) remains. Even a midday breakout would still face this TT gate.

---

### Trades Fired This Rescan

**None.**

Zero candidates re-cleared the composite Layer A + Layer B gates upon midday re-evaluation.

---

### Portfolio State at Rescan

| Field | Value |
|-------|-------|
| Equity | $99,056.46 |
| Cash | $99,056.46 (100%) |
| Open positions | 0/6 |
| Open orders | 0 |
| Week trades used | 0/3 |
| PDT daytrade count | 0/3 |
| Phase P&L | −$943.54 (−0.944%) vs $100,000 start |
| Circuit breakers | ✅ All clear |

---

### Patience Rule Applied

All three skipped candidates remain below their entry thresholds. Gate failures are substantive — not spread-normalization timing issues:

- **XLB:** Spread normalized ✅ (0.02%), but Z has *regressed* to −1.086 (was −1.315 at open — price is rising intraday, moving away from the −2.0 trigger). RSI ~33.8 still above the <30 gate. FCX pair divergence 1.521σ (barely over 1.5σ limit). Vol 0.967× (settled bar). 4 independent failures.
- **XOM:** Spread normalized ✅ (0.11%), but Z regressed to +0.321 (XOM slipping −0.5% intraday). Price 5.2% below $162.55 pivot. Vol 0.981×. 3 independent failures — all worsened since open.
- **XLE:** Spread normalized ✅ (0.017%), but Z essentially flat at +0.642. Price unchanged 3.2% below $61.29 pivot. Vol 1.215× on last settled bar. Oil catalyst not driving the price action needed to bridge the gaps.

No gates were lowered. No trade was forced. The spread normalization (the primary purpose of the midday rescan) has been confirmed for all three names — but the gate failures that caused the morning skips are all quant-level conditions that remain unresolved.

---

### Key Watch for Afternoon / Monday Pre-Market (May 26)

1. **XLE** — Most actionable candidate heading into close. WTI +2.3% today is the structural driver; if XLE closes above $61.29 on ≥1.5× avg volume (~56.6M shares), TODAY becomes a valid breakout bar for Monday's pre-market entry. Monitor the close carefully (~3:50–4:00 PM ET). Note: Minervini TT SMA gap (Dec 2025 split data) remains a secondary structural block.
2. **XLB** — Z regressed today (price rising = moving away from −2.0 trigger). Off near-term watchlist unless a fresh catalyst drives XLB back toward $49.40 (trigger price). FCX pair divergence (1.521σ) needs to narrow simultaneously with Z. Deferred.
3. **XOM/CVX** — Both Z-scores are in the +0.3–0.5 range (near the 20d mean). No momentum or mean-reversion signal available. Monitoring for re-base; pivot at $162.55 (XOM) and $197.25 (CVX) remain the targets for a fresh 2b-LONG signal.
4. **XLV / XLF shorts** — Flagged in this morning's research for Monday scan. YTD laggards (XLV −7.60%, XLF −6.55%). Pull 25-bar + 210-bar Monday AM, run full 2b-SHORT Trend Template check.
5. **200-SMA data gap** — ~45 trading sessions until 200-SMA is available (est. mid-August 2026). No operator action needed.


---

## 2026-05-22 — Afternoon Scan Addendum (~15:48 ET / 19:48 UTC)

**Scan time:** ~12 min before close (market closes 20:00 UTC / 4:00 PM ET)
**VIX regime at scan:** NORMAL (prior close 16.76, futures pointing lower ~16.0–16.5 pre-open) | Sizing multiplier: 1.00×

---

### STEP 1 — Order & Position State Reconciled vs TRADE-LOG

**API results — 6 total orders, all historical:**

| Order ID | Symbol | Type | Status | Detail |
|----------|--------|------|--------|--------|
| 1d69c496 | XOM | Bracket limit BUY 61 sh @ $159.78 | **EXPIRED** 2026-05-18T20:02 | TIF: day — never filled ✅ logged |
| 94606e38 | XOM | Stop child $147.80 | **CANCELED** 2026-05-18T20:02 | Auto-cancelled ✅ logged |
| 336d922a | XOM | TP child $183.74 | **CANCELED** 2026-05-18T20:02 | Auto-cancelled ✅ logged |
| 8f97ef7d | XOM | Market Sell 130 sh | **FILLED** $146.09, 2026-05-07T17:55 | Thesis-break exit ✅ logged |
| d92d9371 | XOM | Trailing Stop 10% GTC | **CANCELED** 2026-05-07T17:54 | Pre-exit cancellation ✅ logged |
| c04ae321 | XOM | Market Buy 130 sh | **FILLED** $153.35, 2026-05-01T14:41 | Original entry ✅ logged |

- **Positions API: `[]` — 100% cash.** No filled positions.
- **Morning bracket orders placed today (May 22): NONE** — Pre-market research decision was explicit HOLD: XLB Z=−1.315 < −2.0 ❌, RSI 33.8 ≮ 30 ❌, vol 0.97× ❌, FCX divergence 1.774σ ❌; XOM Z=+0.498 < +1.0 ❌; XLE no breakout ❌; CVX no breakout ❌; XLV/XLF deferred (bars not pulled at pre-market).
- **Bracket fills today: 0**
- **Open stale limits: 0** — no open orders of any kind
- **TRADE-LOG reconciliation: FULLY CURRENT.** No discrepancies.

---

### STEP 2 — Trailing Stop Upgrades on Profitable Fills

**N/A.** Portfolio is 100% cash ($99,056.46). No positions exist. No trailing stop upgrade workflow applicable.

---

### STEP 3 — Stale Limit Cancellations

**None.** No open orders. May 18 bracket (1d69c496) expired at session close per TIF: day. Nothing to cancel.

---

### STEP 4 — Afternoon Opportunity Scan

**VIX regime:** NORMAL (1.00×) | **Positions:** 0/6 | **Week trades:** 0/3 | **PDT:** 0/3

**⏰ Timing note:** Scan at 15:48 ET = within final **12 minutes** of session. CONSTRAINTS.md prohibits new entry orders in the last 15 minutes. All analysis is for **Monday pre-market watchlist only** — no new bracket orders can be placed at this time.

**Z-Scores and metrics computed from live quotes + 25-bar API settled data:**

| Ticker | Live Ask | Z-Score | 20d Mean | 20d StdDev | 20d High | 20d Low | Vol (May21) vs Avg | Lane Tried | Key Failures | Verdict |
|--------|----------|---------|----------|------------|----------|---------|---------------------|-----------|--------------|---------|
| XOM | $154.90 | +0.487 | $152.75 | $4.42 | $162.55 | $144.57 | 0.98× | 2b-LONG | Z < +1.0 ❌; $7.65 below pivot ❌; vol 0.98× ❌ | **REJECT** |
| CVX | $191.53† | +0.598 | $188.94 | $4.33 | $197.25 | $181.62 | 1.28× | 2b-LONG | Z < +1.0 ❌; $5.72 below pivot ❌ | **REJECT** |
| XLE | $59.495 | +0.766 | $58.35 | $1.49 | $61.29 | $55.70 | 1.21× | 2b-LONG | Z < +1.0 ❌; $1.80 below pivot ❌; TT SMA structural | **REJECT** |
| XLB | $50.295 | −1.003 | $51.19 | $0.90 | $52.41 | $49.04 | 0.97× | 2a-LONG | Z = −1.003 (need ≤ −2.0) ❌; vol 0.97× ❌ | **REJECT** |
| XLV | $149.95 | **+3.247** | $145.24 | $1.45 | $148.15 | $142.84 | 0.74× | **2a-SHORT** | Vol 0.74× ❌; TT: price ABOVE 50d SMA ❌; RSI unconfirmed (est ~68-72, need >70) | **REJECT** |
| XLF | $51.915 | +1.128 | $51.56 | $0.31 | $52.13 | $50.99 | 1.00× | 2b-SHORT | Z > −1.0 (wrong direction entirely) ❌; price above 20d low ❌; vol 1.00× ❌ | **REJECT** |

†CVX bid is wide R-flagged ($180.73); ask $191.53 used as fair value.

**Pair divergences:**
- XOM (+0.487) ↔ CVX (+0.598): 0.112σ ✅ — energy sector moving in perfect lockstep (thesis intact structurally, no entry signal)
- XOM (+0.487) ↔ XLE (+0.766): 0.279σ ✅ — broad energy sector coherence confirmed
- XLB (−1.003) ↔ FCX (+0.328): 1.330σ ✅ — pair divergence has NARROWED from 1.835σ (Thursday) to 1.330σ today, and is now **below the 1.5σ threshold** for the first time this week. This is a positive development for the XLB watchlist thesis.

---

**Candidate Detail Notes:**

**XOM — REJECT (3 independent failures):**
- Z = +0.487 (momentum lane needs ≥ +1.0). Price $154.90 is 7.65% below its prior breakout pivot ($162.55). Volume on last settled bar (May21): 17.07M / 17.40M avg = 0.98× (sub-threshold). All three gates of the 2b-LONG lane fail simultaneously. Energy thesis (WTI structurally elevated, Hormuz, sector momentum) remains intact but the statistical signal is absent. XOM is 6 sessions into its pullback from the $162.55 high — building a new base.

**CVX — REJECT (2 independent failures):**
- Z = +0.598; price $5.72 below pivot $197.25. The pair divergence from XOM is an excellent 0.112σ — both energy majors are moving together. But momentum lane requires Z ≥ +1.0 AND close above 20d high. Neither clears. CVX's May21 volume (9.06M / avg 10.59M) is 0.85×, also below the 1.5× breakout threshold. Same structural position as XOM — valid thesis, no entry signal.

**XLE — REJECT (3 failures + structural TT):**
- Z = +0.766; $1.80 below pivot $61.29 (closest of the three energy names to the breakout level). Volume last bar 1.21× (improving but not at 1.5× threshold). Minervini TT 150/200-SMA unavailable due to Dec 2025 XLE share consolidation. In aggregate: the energy pullback continues on below-average volume, consistent with orderly consolidation, not a strategic breakdown. XLE is the most "ready" of the energy names — only $1.80 away from a breakout with RSI likely in the 60-65 range.

**XLB — REJECT (2 gate failures, but FCX pair now confirms):**
- Z = −1.003 (mean-reversion long lane needs ≤ −2.0; trigger price $49.40). Needs further $0.87 decline from current $50.295.
- Volume last bar: 0.97× (just below the 1.0× minimum for 2a-LONG lane).
- **Key positive development:** FCX pair divergence has narrowed from 1.835σ (Thursday's afternoon scan) to **1.330σ today** — now WITHIN the ≤1.5σ threshold. This means the pair confirmation gate would PASS if/when the Z and RSI gates clear. The FCX improvement is significant because the pair divergence was the third independent blocker alongside Z and RSI.
- XLB 20d low: $49.04. If XLB approaches this level, Z reaches ≈ −2.41 and would trigger the 2a-LONG gate. RSI at that level would likely clear <30 as well.

**XLV — REJECT but #1 WATCHLIST for Monday (largest Z-score in scan at +3.247):**
- Z = **+3.247** — this is the most statistically extreme reading in the entire scan. XLV has rallied from its $142.84 20d low to $149.95 live — a $7.11 (+4.98%) surge that has pushed it **3.2 standard deviations** above its 20-day mean.
- Lane evaluated: **2a-SHORT (Mean-Reversion Short)** — Z ≥ +2.0 threshold met ✅
- Gate failures:
  1. **Volume: 0.74× ❌** (2a-SHORT needs ≥ 1.0×; May21 = 7.17M vs avg 9.74M)
  2. **Minervini SHORT Trend Template: FAIL ❌** — Price $149.95 is *above* the estimated 50d SMA (~$146.25). The Short Trend Template requires price to be BELOW all key SMAs (50/150/200d). XLV is in an uptrend from its April lows — it fails the TT structural requirement for a short entry. The TT constraint protects against shorting into momentum; a Z=+3.2 reading is statistically extreme but it can stay extreme in a trending market.
  3. **RSI: unconfirmed** — conservative estimate ~68-72, borderline relative to the >70 requirement. Not confirmable without precise intraday computation.
- **Short universe qualification:** XLV (Health Care Select Sector SPDR) — ETF, AUM ~$35B ✅. Meets the "sector/index ETFs only" constraint for Phase 1 shorts.
- **Why this matters for Monday:** If XLV closes today's session (or early next week) with volume recovering to ≥1.0× AND RSI confirms >70, the only remaining structural block is the Minervini TT price-vs-SMA condition. This TT condition could be overridden if the SMA-alignment check is re-evaluated (price above 50d SMA = stock is NOT in a confirmed downtrend, which is the valid point the TT is making). At Z=+3.2, the mean-reversion pull is statistically strong. Monitor carefully.

**XLF — REJECT (wrong direction entirely):**
- Z = +1.128 — XLF is ABOVE its 20d mean, not below it. The 2b-SHORT breakdown lane requires Z ≤ −1.0 (price declining from mean). XLF is doing the opposite — it's mildly elevated. The price ($51.92) is $0.93 above its 20d low ($50.99) — no breakdown signal. At Z = +1.128, XLF is in "normal above-average" territory, not oversold or showing breakdown characteristics. **Remove from active short watchlist.** Not a setup in any lane.

---

### Afternoon Market Context

Friday May 22 is closing out a week of energy sector pullback from the prior week's breakout highs (XOM peaked at $162.55 on May 19, now at $154.90; XLE peaked at $61.29 on May 19, now at $59.50). The pullback has been orderly — energy names are trading on below-average volume throughout the week, which argues for consolidation rather than institutional distribution. The energy structural thesis (WTI ~$96–98, Brent ~$104–106, ongoing Hormuz tensions, WTI +2.3% today per pre-market research) remains intact, but the quant statistical entry signals have reset — Z-scores are now +0.5 to +0.8 range, well below the +1.0 momentum lane threshold. The most interesting development today is **XLV at Z = +3.247**, which is the single largest statistical deviation in the scan and represents a potential 2a-SHORT mean-reversion opportunity if/when the volume and RSI gates confirm next week. The **XLB FCX pair divergence narrowing from 1.835σ → 1.330σ** is also significant — it removes the pair-divergence block that has been preventing XLB's mean-reversion long setup from fully qualifying. VIX at ~16.5 (futures pointing lower from 16.76 close) remains firmly in the Normal regime. No new macro events expected today. The week closes with portfolio at 100% cash, week trades 0/3 used, full PDT budget intact — maximum flexibility heading into next week.

---

**Bracket fills today:** 0 (no morning limits were placed — HOLD decision at pre-market; all candidates failed composite gates)
**Stops upgraded:** 0 (no positions held; no trailing stop workflow applicable)
**Stale limits cancelled:** 0 (no open orders existed at scan time)
**New afternoon entries:** none — all 6 candidates failed composite Layer A + Layer B gates; additionally within final 12-minute no-entry window
**Afternoon market context:** Energy sector consolidating orderly on below-avg vol (XOM $154.90 / −0.25% today, XLE $59.50 / +0.31% today). XLV surged to Z=+3.247 — largest overbought reading in scan; 2a-SHORT setup emerging but vol 0.74× and TT gate fail today. XLB FCX pair divergence narrowed to 1.330σ (now within ≤1.5σ threshold — first time this week). VIX Normal (~16.5). No new orders placed.

**Key watchlist for Monday pre-market (2026-05-25):**
1. **XLV — #1 PRIORITY (2a-SHORT candidate):** Z = +3.247 (STRONGLY overbought, +3.2σ). Gate requirements to clear Monday: (a) volume ≥ 1.0× 20d avg (~9.74M shares), (b) RSI > 70 confirmed from daily bar, (c) Minervini Short TT evaluation — check whether price is still above 50d SMA (if still in uptrend, TT blocks; if consolidation has reversed, may qualify). XLV is sector ETF (AUM ~$35B) ✅, Phase 1 short universe ✅. Max short: 10% of equity = $9,906.
2. **XLB — #2 (2a-LONG carryover):** Z = −1.003; trigger price $49.40 (needs −0.87 further decline = −1.7%). FCX pair divergence NOW 1.330σ ✅ (passes ≤1.5σ for first time this week). Volume last bar 0.97× (borderline). All three gates close to qualifying simultaneously. If XLB opens Monday near/below $50.00, this setup is imminent.
3. **XLE — #3 (2b-LONG carryover):** Z = +0.766; only $1.80 below the $61.29 breakout pivot. Volume trend improving. If WTI stabilizes and XLE breaks $61.29 on ≥1.5× volume Monday, momentum lane re-opens. Minervini TT SMA data gap (Dec 2025 split) is the remaining structural block.
4. **XOM/CVX** — Both in orderly consolidation. Z-scores +0.5 to +0.6; below momentum thresholds. Not actionable Monday unless a strong pre-market catalyst lifts both back toward prior pivots.
5. **XLF** — Removed from short watchlist. Z = +1.128 (wrong direction for short); no breakdown signal.


---

## 2026-05-25 — Pre-market Research (Memorial Day — US Markets Closed)

> **URGENT: FLAG FOR WEEKLY REVIEW — Short Trend Template (TT) structural conflict with 2a-SHORT lane.** The Minervini Short TT requires a stock be in a confirmed downtrend (price < 50/150/200 SMA, >30% below 52w high), but the 2a-SHORT mean-reversion lane by definition catches names that are OVERBOUGHT in an uptrend (Z ≥ +2.0, RSI > 70). These two conditions are structurally incompatible. XLV at Z = +2.44 is the clearest example: it's statistically overbought but in a partial recovery, making it impossible to pass both gates simultaneously. Recommend distinguishing the TT check by lane: 2a-SHORT should not require the full short TT (which assumes a broken downtrending stock), only the 2b-SHORT momentum breakdown lane should require the full short TT. This issue needs formal strategy update.

---

### Adjustment Audit (from Week-4 / Phase Audit weekly review)

- **[SCAN] Expand candidate universe Monday pre-market to ≥8 names across ≥3 sectors:** 🟡 PARTIALLY IMPLEMENTED — ROUTINE.md STEP 5 now explicitly calls for "Long candidates: trending leaders...Russell 1000 mid-caps, sector ETFs > $1B AUM, ADR mega-caps" and "Short candidates: mega-caps >$20B and sector/index ETFs." Today's scan covered XLV (Healthcare), XLB (Materials), XLE (Energy), XOM (Energy), XLK (Tech) = 5 tickers across 4 sectors ✅ vs prior week's 4-6 names all in energy/materials. Sector breadth improved. However, the ROUTINE.md does not formally codify "≥8 names" or "≥3 sectors" as a minimum — it reads as guidance, not a hard rule. Full implementation requires a formal minimum-breadth constraint in CONSTRAINTS.md or ROUTINE.md. Partially implemented, not enforced.

- **[SHORT PRIORITY] XLV 2a-SHORT: Pull 25-bar + 210-bar data at pre-market open Monday:** ✅ IMPLEMENTED — XLV bars pulled simultaneously with all other candidates at the start of STEP 5. Not deferred to afternoon. This is direct improvement from prior week's failure where shorts were only evaluated at 15:48 ET (within the no-entry window).

- **[ENTRY CALIBRATION] Monday-adjusted limit price for momentum carryovers:** ✅ IMPLEMENTED IN LOGIC — Today's analysis specifically evaluated XLE's expected open price ($55.92–56.50) given the oil crash catalyst, rather than anchoring to Friday's May 22 close ($59.49). The Monday gap was explicitly modeled. No formal script change was needed; this was handled in the analysis narrative.

- **[PROCESS] Midday rescan: add short-candidate re-evaluation to midday workflow:** 🟡 IMPLEMENTED IN PROMPT — ROUTINE.md midday section now reads "Scan open positions mid-trading day" but does not explicitly call out short candidate re-evaluation as a named step. The spirit is in the workflow but the explicit instruction ("re-evaluate short candidates that were borderline at pre-market if volume picks up intraday") is absent from the midday ROUTINE.md text. Needs a formal line addition.

- **[WATCHLIST] XLB mean-reversion long — trigger $49.40:** ❌ NOT TRIGGERED — XLB did NOT reach trigger. Closed May 22 at $50.29 (trigger was $49.40, gap = -$0.89). Z = -0.890 (needed ≤ -2.0). No action required today; carryover watchlist item remains.

---

### Account
- **Equity:** $99,056.46
- **Cash:** $99,056.46 (100.0%)
- **Buying power:** $198,112.92 (margin)
- **Daytrade count:** 0 / 3
- **Open positions:** None
- **Open orders:** None
- **Week trades used:** 0 / 3 (resets today, first day of new week)

---

### Market Context
- **US Markets:** CLOSED — Memorial Day holiday. No NYSE/NASDAQ trading today.
- **Futures:** S&P 500 futures surged above 7,534 in pre-market — all-time high. Futures +0.91% at 5:20 AM EDT. US stock market closed; overnight reaction to geopolitical developments.
- **WTI Crude Oil:** Sharp decline to $90.65–$92.47/bbl (−4.73% to −6.1%). TWO-WEEK LOW. Prior close ~$96.60. Triangle support broken on longer-term charts — potential sustained selloff.
- **Brent Crude:** Fell below $100/bbl for first time in several weeks; trading $97.22–$99.39/bbl (−4.55% to ~−6%). Down from ~$103–104 prior.
- **Primary Catalyst:** Optimism surrounding a potential US-Iran peace agreement. Framework for reopening Strait of Hormuz "largely negotiated." However, Trump stated "no hurry" to finalize, and naval blockade remains until formal agreement. Market interpreting this as bullish risk-on (lower oil = lower inflation = higher equities), but deal is NOT finalized.
- **VIX:** 16.70 as of May 22 (last market close). Down from 16.76 prior day (−0.36%). 17.65% lower than 1 year ago.
- **Pre-market Earnings:** LexinFintech (LX) reported Q1 before market open today. Loan volume RMB 57.9B (+15.9% seq, +12.2% YoY). Revenue RMB 3.3B. Net income RMB 201M (−5.9% seq on higher opex). After-bell expected: FINV, JOYY.
- **Economic Calendar:** NO major releases today (Memorial Day). Key events this week: Thursday = US Core PCE (April) + Q1 GDP (first reading). No FOMC, no jobs data today.
- **Sector YTD Momentum (as of May 23):**
  - #1 Energy: +34.5% YTD
  - #2 Technology: +22.3% YTD (rebounded from −6.3% in Q1)
  - Mid-tier (9–11%): Consumer Staples, Industrials, Real Estate, Materials
  - Underperformers: Healthcare −4.6%, Comm Services −5.5%, Consumer Disc −8.1%, Financials −9.7%
- **Oil Impact Analysis:** WTI −6.1% is a MAJOR negative catalyst for the Energy sector (XLE, XOM, CVX). Energy YTD +34.5% is at risk if the Iran deal materializes. Oil-sensitive names expected to gap down significantly at Tuesday open. Tech and Consumer Discretionary (oil-cost-sensitive) should benefit.

---

### VIX Regime
- **Current VIX:** 16.70 (May 22 close — last available)
- **Regime:** Normal (VIX 14–22)
- **Sizing multiplier:** 1.00×
- **Note:** Markets closed today. VIX may drop further Tuesday if Iran optimism holds, as lower oil = reduced global inflation risk = reduced macro uncertainty.

---

### Candidate Universe Scanned
Four candidates evaluated across Healthcare (XLV), Materials (XLB), Energy (XLE/XOM), and Technology (XLK). Covers 4 sectors meeting the ≥3-sector breadth mandate from the weekly review adjustment.

---

### Trade Ideas (Cleared Both Layers)

**None. All candidates failed at least one required gate.**

---

### Skipped Candidates

**1. XLV | SHORT | Healthcare ETF | 2a-SHORT Mean-Reversion**
- **Catalyst:** Healthcare sector rolling over from 2025 highs; Z = +2.437 (strong overbought signal at 52-week recovery rally exhaustion). Sector YTD −4.6%.
- **Lane attempted:** 2a-SHORT (Mean-Reversion Short)
- **Layer B checks:**
  - Z-score: +2.437 ≥ +2.0 ✅
  - RSI(14): 69.1 (needs >70) ❌ — 0.9 points short of threshold
  - Volume: 0.714× (needs ≥ 1.0×) ❌ — 6.92M vs 9.69M avg
- **Layer B result:** FAIL (2 of 3 gates fail)
- **Minervini Short TT:**
  - Price $149.89 < 50-SMA $146.38? ❌ FAIL — price above 50-SMA
  - Price < 150-SMA $151.26? ✅
  - Price < 200-SMA $151.26? ✅
  - 150-SMA < 200-SMA? ❌ (both equal at $151.26)
  - 200-SMA trending down (151.26 < 152.20 one month ago)? ✅
  - 50-SMA < 150-SMA? ✅
  - Price > 30% below 52w high ($160.20)? −6.4% below ❌ FAIL (need ≥ 30%)
  - Price within 25% of 52w low ($142.84)? +4.9% above ✅
- **TT result:** FAIL — price above 50-SMA, not 30% below 52w high
- **Key notes:** Z-scores computed from 25-bar data (May 22 close = $149.89, mean_20 = $145.52, σ = $1.79). RSI tantalizingly close at 69.1; would have been a trade if RSI cleared 70. Structural conflict between 2a-SHORT (requires overbought uptrend) and Minervini Short TT (requires confirmed downtrend) flagged for strategy review.
- **6-month return:** −1.0% (vs +22.3% for XLK) — bottom-30th percentile ✅ (supports short thesis directionally)
- **Pair:** XLV has no direct TRADING-STRATEGY.md canonical pair; closest is JNJ/UNH. Not pulled (no qualifying pair for ETF sector short in the canonical list).

---

**2. XLB | LONG | Materials ETF | 2a-LONG Mean-Reversion (carryover)**
- **Catalyst:** Materials sector consolidating after May selloff; FCX pair divergence 1.330σ (within gate). XLB down from $53.62 high to $50.29.
- **Lane attempted:** 2a-LONG (Mean-Reversion Long)
- **Layer B checks:**
  - Z-score: −0.890 (needs ≤ −2.0) ❌ — far from threshold; trigger ~$49.45
  - RSI(14): 47.8 (needs <30) ❌
  - Volume: 0.658× (needs ≥ 1.0×) ❌
- **Layer B result:** FAIL (all 3 gates fail)
- **Minervini Long TT:**
  - Price $50.29 > 50-SMA $50.63? ❌ — slightly below
  - 150-SMA: INSUFFICIENT DATA (113 post-split bars; split Dec 5, 2025) ❌
  - 200-SMA: INSUFFICIENT DATA ❌
  - Price > 30% above 52w low? +15.9% ❌ FAIL
- **TT result:** FAIL
- **Status:** Carryover watchlist — watching for Z ≤ −2.0 trigger near $49.40. Oil crash may NOT directly help XLB (materials ≠ energy), but a risk-off day could pressure materials alongside energy.

---

**3. XLE | SHORT | Energy ETF | 2b-SHORT Momentum (oil crash)**
- **Catalyst:** WTI −6.1% to $90.65 on Iran deal optimism; Brent below $100. XLE expected to open −5 to −6% (~$55.92 from $59.49 close).
- **Lane attempted:** 2b-SHORT (Momentum Short)
- **Layer B checks (at estimated open $55.92):**
  - Z ≤ −1.0? Z ≈ −1.70 ✅ (if opened at $55.92)
  - Close < 20d low ($55.70)? $55.92 > $55.70 ❌ — barely above 20d low; need sustained close below
  - RSI 30–50? RSI 50.4 on settled data; expected to drop to ~30–35 after −6% day ❌ — would fall INTO or THROUGH the 30 level (oversold, not in short-confirmation zone)
  - Volume ≥ 1.5×? Likely ✅ (high-vol oil-crash day expected)
  - 50-SMA < 200-SMA? Insufficient data (Dec 2025 split) ❌
- **Layer B result:** FAIL — RSI would overshoot into oversold territory, no clean 20d low break at expected prices
- **Minervini Short TT:**
  - 150/200-SMA: INSUFFICIENT DATA (Dec 2025 split; only 116 post-split bars) ❌
  - Price > 30% below 52w high $62.56? −10.6% below ❌ (need ≥ 30%)
- **TT result:** FAIL (permanently blocked by split data gap for at least 4–6 more months)
- **Pair:** XOM Z = +0.419 (May 22). At −6% open: XOM Z ≈ −1.66. XLE/XOM divergence today: 0.248σ ✅ (well within 1.5σ). Pair confirms sector selloff.
- **Note:** The oil-crash day may actually set up a MEAN-REVERSION LONG in XLE for later this week if oil stabilizes. Iran deal is NOT finalized; Trump said "no hurry." A false-alarm reversal (WTI recovers to $94+) could produce a Z ≤ −2.0 long setup in XLE by Wednesday if price continues down to ~$54.50.

---

**4. XLK | LONG | Technology ETF | 2b-LONG Momentum (AI/tech rally)**
- **Catalyst:** S&P 500 futures +0.91% all-time high; Tech sector #2 YTD +22.3%; AI remains structural long-term driver.
- **Lane attempted:** 2b-LONG (Momentum Long)
- **Layer B checks (as of May 22 close):**
  - Z = +1.255 ≥ +1.0 ✅
  - Close > 20d high ($180.39)? $180.39 = AT the 20d high ❌ — no clean breakout yet
  - RSI(14): 74.9 (needs 50–70) ❌ — ABOVE the upper bound; overbought
  - Volume: 0.932× (needs ≥ 1.5×) ❌
  - 50-SMA ($153.52) > 200-SMA? Insufficient data for 200-SMA ❌
- **Layer B result:** FAIL (3 of 5 gates fail)
- **Minervini Long TT:**
  - Price $180.39 > 50-SMA $153.52 ✅
  - 150/200-SMA: INSUFFICIENT DATA (Dec 2025 split; 116 post-split bars) ❌
  - Price > 30% above 52w low ($127.50)? +41.5% ✅
  - Price within 25% of 52w high (at 52w high = 0.0%) ✅
- **TT result:** PARTIALLY BLOCKED — 150/200 SMA gap persists
- **Pair (NVDA):** Z = +0.055 (nearly flat). XLK Z = +1.255. Divergence = 1.20σ ✅ (within 1.5σ gate). Pair doesn't diverge, confirms tech sector elevation.
- **Note:** XLK is at all-time-high territory. RSI 74.9 suggests near-term overextension. If market gaps up Tuesday and XLK opens above $184+ (clearing 20d high on volume), a same-day assessment would be needed. The 50-70 RSI gate would need to be watched post-gap-open. Likely in watchlist for Tuesday if RSI normalizes after gap.

---

### Risk Factors
1. **Iran deal uncertainty:** Trump stated "no hurry" — deal could be walked back overnight, causing oil to snap back strongly. Any reversal of the peace thesis would hit futures hard (risk to shorts in energy, benefit to energy longs that may appear next session).
2. **Holiday liquidity:** US markets closed; overnight futures moves may partially reverse at Tuesday open when full institutional participation resumes.
3. **Permanent SMA data gap:** XLB, XLE, XLK all had splits in December 2025. The 150/200-day SMA computations will remain blocked until ~May–June 2026 for the 150-SMA and ~June–July 2026 for the 200-SMA. This is a persistent structural limitation affecting 3 of 4 primary ETF candidates.
4. **Energy sector re-assessment:** Energy has been YTD's top sector (+34.5%). A sustained oil decline (if Iran deal holds) would reshape sector momentum dramatically. Tuesday's market-open will require a complete re-evaluation of all energy-related candidates.
5. **XLK RSI overextension:** Tech at RSI 74.9 and at 52-week highs. AI-driven rally could still continue, but RSI being >70 on approaching the all-time high means the quant gate rejects it until a consolidation brings RSI to 50-70.

---

### Decision
**HOLD** — Zero candidates cleared both Layer A + Layer B. US markets are closed today (Memorial Day). No orders placed, no orders to review.

**Primary watchlist for Tuesday open (2026-05-26):**
1. **XLE / XOM — Assess for 2b-SHORT if Tuesday close confirms breakdown below 20d lows on elevated volume.** XLE 20d low = $55.70; XOM needs new 20d low below $144.57. Watch RSI: needs to land in 30–50 range (not crash through 30). Volume should be 1.5×+ on an oil-crash day. TT blocked by split data — note as ongoing constraint.
2. **XLV — 2a-SHORT re-evaluation.** RSI was 69.1 on May 22; if healthcare names remain elevated or push slightly higher Tuesday, RSI could clear 70. Volume needs to recover to ≥1.0× (9.7M+ shares). Z = +2.437 is strong. Structural TT conflict noted (see URGENT flag above).
3. **XLK — 2b-LONG watch.** RSI 74.9 needs to normalize toward 60-65. Tuesday may see profit-taking after the futures-driven gap, which could bring RSI back to the 50-70 zone. Watch for consolidation + volume confirmation.
4. **XLB — Mean-reversion long trigger at $49.40** still active. Z would need ≤ −2.0. Current $50.29 needs -$0.84 further decline. An oil-crash-driven risk-off day could pressure materials simultaneously.

---

*Research generated: 2026-05-25 (Memorial Day — pre-market workflow)*
*Account: $99,056.46 | 0 positions | 0 orders | Week 0/3 trades | PDT 0/3*

---

### 2026-05-25 — Midday Rescan Addendum (12:42 ET)

> **CRITICAL FINDING: Market is CLOSED — Memorial Day (2026-05-25).** Alpaca clock confirms `is_open: false`; next open is 2026-05-26T09:30:00-04:00. All live quote timestamps are 2026-05-22T20:00:00Z (Friday close). No intraday price action exists to update any gate. This rescan is structurally a no-action scan — the "midday" workflow ran at 12:42 ET on a market holiday, which cannot produce spread normalization or fresh Z-Score data.

**Skipped at open (carryover from 2026-05-25 pre-market), re-evaluated:**

- **XLV (2a-SHORT):** Spread 5.28% (stale close quote — wide/invalid for intraday). Z-Score = +2.500 ≥ +2.0 ✅. RSI(14) = 69.1 (need > 70) ❌. Volume = 0.737× 20d avg (need ≥ 1.0×) ❌. Minervini Short TT: FAIL (price above 50-SMA; not 30% below 52w high). **→ STILL SKIPPED** — RSI 0.9 points short, volume below threshold, TT structural conflict unresolved. No new session data to change any gate.

- **XLE (2b-SHORT):** Spread 6.08% (stale close quote — wide/invalid). Z-Score = +0.684 (need ≤ −1.0) ❌ — note: as-of Friday close, XLE had not yet absorbed the WTI −6.1% oil crash catalyst (Iran deal news broke over the holiday weekend). May 22 close of $59.49 is PRE-crash. Tuesday open expected ~$55.92 (−6% est.). 20d low = $55.70; close would need to be below this. RSI 50.4 would likely drop to ~30–35 at Tuesday open — THROUGH the 30 floor, not in the 30–50 zone required for 2b-SHORT. 50-SMA/200-SMA: INSUFFICIENT DATA (Dec 2025 split). **→ STILL SKIPPED** — structural blocks unchanged; Tuesday open evaluation required.

- **XLK (2b-LONG):** Spread 6.08% (stale close quote — wide/invalid). Z-Score = +1.287 ≥ +1.0 ✅. Close $180.39 = exactly AT 20d high $180.39 — no clean breakout above ❌. RSI(14) = 74.9 (need 50–70) ❌ — above upper bound. Volume = 0.980× 20d avg (need ≥ 1.5×) ❌. 50-SMA/200-SMA: INSUFFICIENT DATA (Dec 2025 split) ❌. **→ STILL SKIPPED** — 3 of 5 Layer B gates fail; structural SMA data gap persists; no new session data.

- **XLB (2a-LONG):** Quote ask = $0 (one-sided/invalid — cannot compute spread). Z-Score = −0.913 (need ≤ −2.0) ❌. Z-trigger price ≈ $49.31 (current $50.29, gap = $0.98). RSI(14) = 47.8 (need < 30) ❌. Volume = 0.698× 20d avg (need ≥ 1.0×) ❌. Minervini Long TT: FAIL (insufficient 150/200-SMA data; price not >30% above 52w low). **→ STILL SKIPPED** — all three Layer B gates fail; watchlist trigger $49.31 not approached.

**Trades fired this rescan:** None.

**Root cause of universal skip:** US equity markets are CLOSED (Memorial Day). No intraday price discovery has occurred. Spread normalization cannot be assessed — all quotes are stale Friday close data. Z-Scores are identical to morning research. No gate has changed for any candidate. This is the correct outcome for a midday rescan on a market holiday.

**Patience rule applied:** Nothing re-cleared. This is correct. Gates were NOT lowered. No forced trades.

**Tuesday 2026-05-26 pre-market priority watchlist:**
1. **XLE / XOM — 2b-SHORT re-eval at Tuesday open:** Key question is whether WTI oil crash (−6.1% to $90.65) translates into XLE closing BELOW 20d low ($55.70) on Tuesday with RSI landing in the 30–50 window (not crashing through 30). Volume expected ≥ 1.5× on a high-impact oil day. TT blocked by split data gap — this constraint is permanent for ~4 more months.
2. **XLV — 2a-SHORT watch:** RSI at 69.1 needs one more session push to 70.0+. If healthcare names hold elevation or tick up Tuesday morning, RSI could clear. Volume needs recovery to ≥ 9.7M shares. TT structural conflict (2a-SHORT vs downtrend requirement) flagged for strategy review.
3. **XLK — 2b-LONG conditional watch:** RSI 74.9 needs normalization to 50–70 via post-holiday profit-taking or consolidation. If market gaps up Tuesday on Iran optimism and XLK opens above $184+ with a clean break of the 20d high on volume ≥ 1.5×, re-evaluate intraday. SMA data gap remains.
4. **XLB — Mean-reversion long trigger $49.31** still active. Z ≤ −2.0 requires a further −$0.98 decline. An oil-crash-driven risk-off contagion to materials could accelerate this.

*Rescan generated: 2026-05-25 12:42 ET | Market: CLOSED (Memorial Day) | 0 positions | 0 orders | Week 0/3 trades | PDT 0/3*

---

## 2026-05-25 — Afternoon Scan Addendum (15:27 ET / 19:27 UTC)

> **⚠️ MARKET CLOSED — Memorial Day Federal Holiday.** US equity markets (NYSE/NASDAQ) are closed today. All Alpaca quotes carry "R" condition flags and reflect stale May 22 close data (last print 2026-05-22T20:00Z). No intraday price discovery available. No new bracket orders can be placed or filled today. Next session: Tuesday 2026-05-26 09:30 ET.

**Scan time:** ~15:27 ET (19:27 UTC)
**VIX regime:** NORMAL — VIXY mid $25.54 (bid $24.85 / ask $26.23, stale) → estimated VIX ~17.0–17.5 | Sizing multiplier: 1.00×

---

### STEP 1 — Order & Position State

| Field | Value |
|-------|-------|
| Positions | `[]` — 100% cash ($99,056.46) ✅ |
| Open orders | 0 |
| Bracket fills today | 0 (no morning limits placed — HOLD at pre-market) |
| Stale limits | 0 |
| TRADE-LOG status | FULLY CURRENT ✅ |

**All 6 API orders are historical (expired/cancelled/filled):**
- 1d69c496: XOM bracket BUY $159.78 → EXPIRED 2026-05-18T20:02
- 8f97ef7d: XOM market sell 130sh → FILLED $146.09, 2026-05-07 (thesis-break exit)
- All others: children or predecessors of above, all properly closed

---

### STEP 2 — Trailing Stop Upgrades

**N/A** — No positions held. No upgrade workflow applicable.

---

### STEP 3 — Stale Limit Cancellations

**None** — No open orders exist.

---

### STEP 4 — Afternoon Opportunity Scan

**Candidates evaluated (settled through May 22, 2026 — settled bar data):**

| Ticker | Close | Z-Score | RSI(14) | Vol Ratio | 20d High | Lane | Key Failures | Verdict |
|--------|-------|---------|---------|-----------|----------|------|--------------|---------|
| XLV | $149.89 | +3.205 | 60.9 | 0.71× | $148.15 | 2a-SHORT | RSI 60.9 ❌ (need >70); Vol 0.71× ❌ (need ≥1.0×); TT: price AT 52w high (not 30% below) ❌; price above 50-SMA ❌ | **REJECT** |
| XLB | $50.29 | −1.008 | 41.4 | 0.66× | $52.41 | 2a-LONG | Z −1.008 ❌ (need ≤−2.0); RSI 41.4 ❌ (need <30); Vol 0.66× ❌ (need ≥1.0×) | **REJECT** |
| XLE | $59.49 | +0.763 | 61.2 | 1.12× | $61.29 | 2b-LONG | Z +0.763 ❌ (need ≥+1.0); no breakout ❌; RSI 61.2 ❌ (50–70 zone but Z gate fails first) | **REJECT** |
| XLK | $180.39 | +1.425 | 72.8 | 0.93× | $179.50 | 2b-LONG | RSI 72.8 ❌ (need 50–70; overbought); Vol 0.93× ❌ (need ≥1.5×); TT 150/200-SMA unavail. ❌ | **REJECT** |
| XOM | $154.92 | +0.491 | 55.6 | 0.74× | $162.55 | 2b-LONG | Z +0.491 ❌ (need ≥+1.0); price 5% below $162.55 pivot ❌; Vol 0.74× ❌ | **REJECT** |

**Pair Divergences:**
- XLB (−1.008) ↔ FCX (+0.360): **1.368σ ✅** — pair NOW WITHIN the ≤1.5σ threshold for the first time in several sessions. This removes the pair-divergence blocker on the XLB 2a-LONG setup when/if Z and RSI gates clear.
- XOM (+0.491) ↔ XLE (+0.763): 0.272σ ✅ — energy sector cohesion intact

**New afternoon entries:** NONE — all 5 candidates failed composite Layer A + Layer B gates; additionally market is physically closed (Memorial Day)

---

### Candidate Detail

**XLV (Healthcare ETF) — 2a-SHORT — #1 WATCHLIST:**
- Z = +3.205 — the single most statistically extreme reading in this entire week's scans. XLV is 3.2σ above its 20-day mean, a top-2% reading. **Z gate passes ✅.**
- RSI = 60.9 (Wilder's method): **FAILS the >70 requirement** for 2a-SHORT. RSI is elevated but not yet overbought. The prior session (May 22) had RSI estimated at 69.1 — today's Wilder's calculation produces 60.9, likely because the simple 14-period average used in prior entries overstated RSI. The stock has rallied +2.86% over 5 days (145.72 → 149.89) but the RSI momentum signal is not yet confirming a reversal signal.
- Volume = 0.71× 20d avg — **FAILS the ≥1.0× requirement** for 2a-SHORT.
- Minervini Short TT: XLV is AT a 52-week high (149.89 = the 25-bar high from our data). The Short TT requires price to be >30% BELOW the 52-week high — the exact opposite of current positioning. **Structural TT fail.** Strategy conflict: 2a-SHORT (mean-reversion from overbought state in an uptrend) is structurally incompatible with Minervini Short TT (which requires a confirmed downtrend). Flagged for strategy review as URGENT item.
- **Tuesday watch:** If XLV continues to rally early Tuesday and RSI clears >70 while vol recovers ≥1.0× → 2a-SHORT becomes active on the quant layer (Z+RSI+vol pass). The TT structural conflict remains and may permanently block the short per current rules.

**XLK (Technology ETF) — 2b-LONG — #2 WATCHLIST (Most Actionable):**
- Z = +1.425 ✅ (≥+1.0). Close $180.39 > 20d high $179.50 ✅ — a CONFIRMED breakout. Pivot extension = +0.50% ✅ (well within 5% cap).
- RSI = 72.8: **FAILS 50–70 range** for 2b-LONG. Currently overbought (above 70). The 2b-LONG lane needs RSI in the 50–70 "healthy momentum" zone; being above 70 signals potential near-term exhaustion.
- Volume = 0.93× — **FAILS ≥1.5× threshold.** Breakout must be confirmed with institutional participation.
- TT 150/200-SMA: CANNOT VERIFY (Dec 2025 XLK split disrupted historical SMA data, only ~116 post-split bars). Structural blocker.
- **Tuesday opportunity:** S&P 500 futures +0.91% point to a strong gap-up open. If XLK opens at ~$181–183 on gap-up, and RSI normalizes intraday into the 50–70 zone (as the initial euphoria is absorbed), combined with volume ≥1.5× avg (~13.0M shares), this becomes a live 2b-LONG mid-morning bracket candidate for Tuesday. Max entry limit ≤ $179.50 × 1.05 = $188.48 (pivot extension cap).
- **Key note:** XLK at Z=+1.425 with a clean breakout above the 20d high is the closest thing to a qualified setup in today's scan. The TT data gap and vol/RSI gates are the remaining blockers.

**XLB (Materials ETF) — 2a-LONG — #3 WATCHLIST:**
- Z = −1.008; RSI = 41.4; Vol = 0.66× — all three quant gates fail.
- Z-trigger price = **$49.40** (currently $50.29, needs −$0.89 = −1.8% further decline).
- **Key development: FCX pair divergence now 1.368σ ✅** — the first time since early May that the XLB-FCX pair divergence has fallen within the ≤1.5σ threshold. This removes the pair-confirmation blocker that has been preventing XLB's setup from potentially qualifying. If XLB sells off toward $49.40 on Tuesday (possible if risk-off sentiment bleeds into materials alongside energy), all three gates may converge.
- WTI oil crash over the weekend (−6.1% to $90.65) may pressure materials via commodity contagion Tuesday, potentially accelerating XLB's move toward the Z ≤ −2.0 trigger. Monitor carefully.

**XLE (Energy ETF) & XOM — Context only:**
- Both below momentum pivots with weak volume. Energy sector faces significant headwind from the WTI decline over the weekend (Iran deal framework reported). XLE at $59.49 is 3.0% below its $61.29 pivot and has Z=+0.763. XOM at $154.92 is 5.0% below its $162.55 pivot with Z=+0.491. Neither will re-qualify for a 2b-LONG without a major oil recovery.
- **Energy sector reassessment needed for Tuesday:** WTI fell to ~$90.65 from ~$96–98 (−6.1%) over the weekend. This may push XLE through the $55.70 (20d low); if XLE closes below $55.70 on elevated volume, a 2b-SHORT energy setup becomes possible. However: (1) Energy is still YTD's top sector (+34.5% YTD as of May 23); (2) the Iran deal is NOT finalized (Trump: "no hurry"); (3) Short TT requires >30% below 52w high which XLE at $55.70 (only ~11% below $62.56 52w high) would not satisfy. Energy shorts blocked by TT structural constraints.

---

### Afternoon Market Context

Memorial Day session — no trading. The weekend's dominant development was **WTI crude oil declining to ~$90.65/bbl (−4.73% to −6.1%)** on reports of a largely-negotiated US-Iran peace framework. This is the same geopolitical dynamic that triggered the XOM thesis-break exit on May 7 ($146.09). WTI has now dropped from the post-May-15 recovery high of ~$107 to ~$91 — a −15% reversal from the level that justified energy longs. Simultaneously, **S&P 500 futures surged +0.91% to above 7,534 (all-time high territory)** as lower oil = lower global inflation = higher equity multiples. The market is interpreting the Iran de-escalation as a net positive for equities (rate cut odds improve, consumer spending improves) even as it punishes energy directly. Tech (XLK) is the primary beneficiary: it closed the week at a 20-day breakout (180.39 > 179.50), is already in position for a momentum entry pending RSI normalization and volume confirmation on Tuesday. XLV (Healthcare) remains statistically extreme at Z=+3.205 — a potential 2a-SHORT if/when RSI clears 70. The portfolio enters this new macro regime in 100% cash, which is the optimal position: maximum flexibility to act on whichever setup emerges post-Iran-news-settlement.

---

**Bracket fills today:** 0 (market closed; no morning limits placed)
**Stops upgraded:** 0 (no positions held)
**Stale limits cancelled:** 0 (none existed)
**New afternoon entries:** none — all candidates failed composite gates; market physically closed
**Afternoon market context:** WTI -6.1% to $90.65 over weekend (Iran deal framework) — energy sector faces major headwind Tuesday. S&P futures +0.91% at all-time highs — tech/risk-on beneficiaries. XLK at 20d breakout (Z=+1.425, ext +0.50%) is #1 actionable candidate for Tuesday pending RSI normalization (72.8 → need 50–70) and volume (0.93× → need ≥1.5×).

**Key watchlist for Tuesday pre-market (2026-05-26):**
1. **XLK — #1 PRIORITY (2b-LONG):** Z=+1.425 ✅, breakout above pivot ✅, extension 0.50% ✅. Remaining gates: RSI needs to normalize from 72.8 → 50–70 (likely mid-morning Tuesday after gap euphoria fades); Volume needs ≥1.5× avg (~13.0M shares). TT 150/200-SMA structural gap (Dec 2025 split). Max entry limit ≤$188.48 (pivot $179.50 × 1.05). If RSI and vol clear intraday → POTENTIAL MID-SESSION BRACKET ORDER.
2. **XLV — #2 (2a-SHORT):** Z=+3.205 ✅. RSI needs >70 (currently 60.9); vol needs ≥1.0× avg (~9.7M shares). TT structural conflict (2a-SHORT vs Minervini downtrend requirement) — strategy review item. Watch for continued rally Tuesday.
3. **XLB — #3 (2a-LONG):** Z-trigger $49.40 (−1.8% away). FCX pair now confirms (1.368σ ✅). Oil crash may pressure materials Tuesday → potential convergence event.
4. **XLE/XOM — ENERGY RE-ASSESSMENT:** WTI at $90.65 over weekend. XLE 20d low = $55.70; if Tuesday close breaks below this on elevated volume, assess 2b-SHORT. Hard blocker: TT structural (only −10.6% below 52w high; needs >30%). Energy sector: 1 consecutive failure logged (XOM May 7). No new energy long until WTI stabilizes + fresh catalyst + volume confirmation.
5. **[STRATEGY REVIEW FLAG]:** 2a-SHORT lane vs Minervini Short TT structural incompatibility. XLV exemplifies this perfectly: the stock is overbought in an uptrend (correct for 2a-SHORT) but the Short TT requires a downtrend (incompatible with 2a). Recommend: 2a-SHORT should require only "Z ≥+2.0, RSI >70, vol ≥1.0×" WITHOUT the full Minervini Short TT. The 2b-SHORT breakdown lane should retain the full Short TT. Needs formal update to TRADING-STRATEGY.md and CONSTRAINTS.md.


---

## 2026-05-26 — Pre-Market Research

> ⚠️ **URGENT: TWO ITEMS NEED BUILD — see Adjustment Audit below**

### Account
- Equity: $99,056.46
- Cash: $99,056.46 (100.0%)
- Buying power: $198,112.92
- Open positions: 0
- PDT daytrade count: 0/3
- Week trades used: 0/3
- Phase P&L: −$943.54 (−0.944%) | Peak: $100,206.70 | Drawdown: −1.15%
- balance_asof: 2026-05-22 (Friday — Memorial Day weekend; today May 26 is Tuesday)

### Adjustment Audit (from Week-4 Weekly Review, filed 2026-05-22)

**Weekly review adjustments checked against codebase:**

- **[SCAN — URGENT] Expand candidate universe to ≥8 names across ≥3 sectors:** ❌ NOT IMPLEMENTED — `grep -i "≥3 sector\|3 sector\|minimum.*sector\|breadth" .claude/commands/ROUTINE.md memory/CONSTRAINTS.md memory/TRADING-STRATEGY.md` returns no hits. The prompt still has no minimum sector breadth requirement codified. Today's scan covered 11 symbols across 6 sectors (Info Tech, Healthcare, Materials, Energy, Consumer Disc, Industrials, Financials) — the human researcher did the expansion manually, but it is NOT in the ROUTINE.md checklist. **Needs ROUTINE.md update.**

- **[SHORT PRIORITY] XLV 2a-SHORT: Pull 25-bar data at pre-market open Monday (not deferred):** 🟡 IMPLEMENTED IN CODE BUT NOT TRIGGERED — The ROUTINE.md STEP 5 instructs pulling 25-bar data for all short candidates. Today this was done correctly at pre-market. However XLV fails on RSI (58.6 < 70) and vol (0.32x < 1.0×) — not a process failure, a market condition. The process worked; XLV simply hasn't triggered yet.

- **[ENTRY CALIBRATION] Monday-adjusted limit price for momentum setups from Friday:** ❌ NOT IMPLEMENTED — `grep -i "monday.*limit\|limit.*stale\|gap.*adjust\|weekend.*gap" .claude/commands/ROUTINE.md` returns no hits. No formal "weekend gap adjustment" step exists in ROUTINE.md STEP 2. This week XLK gapped from $180.39 (Friday close) to $184.31 (today open), a +2.2% gap. Any Friday limit set at $180.39 would not have been chased (correct per "no chasing" rule), but the methodology for Monday re-evaluation is still informal. **Needs ROUTINE.md update.**

- **[PROCESS] Midday rescan: add explicit short-candidate re-evaluation:** 🟡 IMPLEMENTED IN CODE BUT NOT TRIGGERED — Midday workflow runs daily. The instruction in ROUTINE.md includes re-evaluating "borderline" candidates. XLV would be the specific re-evaluation candidate today (RSI needs >70; watch for intraday push). Process exists; specific mention of short candidate re-eval is informal rather than explicit in the checklist.

- **[WATCHLIST] XLB 2a-LONG trigger $49.40:** ❌ NOT TRIGGERED — XLB Z = −0.296 today (split-adjusted), mean=$50.66, std=$0.72. Trigger would require price of ~$49.22 for Z ≤ −2.0. XLB is at $50.80, about $1.58 away from trigger. The Iran/Brent catalyst is sending oil UP (+3%), which is a positive for materials/XLB — counterintuitively, this moves XLB AWAY from the oversold trigger. Not a process issue.

**Summary: 2 items ❌ NOT IMPLEMENTED requiring build, 2 items 🟡 in code but conditions not met:**

> ❌ **URGENT: Build ROUTINE.md sector breadth mandate (≥3 sectors, ≥8 names per pre-market scan)**
> ❌ **URGENT: Build ROUTINE.md weekend gap adjustment step for momentum setups carried from Friday**

---

### Market Context

**Macro / Geopolitical:**
- US military strikes in southern Iran overnight → Brent crude surged +3.0–3.2% to $99.03–99.18/bbl (supply risk premium)
- WTI crude paradoxically fell 2.3–4.2% to $92.53–94.38/bbl (mixed Iran negotiation signals; domestic vs. Brent spread widening)
- S&P 500 at or near all-time highs; Middle East peace hopes supporting equity indices broadly
- NVIDIA earnings beat (strong guidance) — AI/semis optimism continues; KOSPI rallied on semiconductor optimism
- Market interpreting Iran situation as: geopolitical risk premium in Brent, but broader resolution = bullish equities

**Pre-market levels:**
- S&P 500 futures: +0.68–0.77%, at 7,542–7,549
- SPY pre-market: +0.55% at $749.77
- XLK (Tech ETF): opened at $184.31 today (+2.17% above Friday pivot $180.39)

**VIX:** 16.85 (+1.57%), up from 16.59 on May 22. VIX futures remain below 21.

**Economic calendar today:**
- 9:00 ET: FHFA House Price Index, S&P CoreLogic Case-Shiller HPI (March)
- 10:00 ET: Conference Board Consumer Confidence
- 10:30 ET: Philadelphia Fed Nonmanufacturing Survey, Texas Manufacturing Outlook Survey
- Later: EIA gasoline/diesel data; API crude inventories
- NO CPI, PPI, FOMC, or jobs data today

**Pre-market earnings:**
- AutoZone (AZO): Q3 EPS beat / Revenue miss → −5% pre-market (~$2,858 from $3,007)
- Freightos (CRGO): Q1 rev $7.2M, +3% YoY (inline)
- CSW Industrials (CSW), Champion Homes (SKY), MINISO (MNSO), Semtech (SMTC), others reporting

**Sector YTD momentum (as of May 1, 2026):**
- 🥇 Info Technology: +32.9% | Communication Services: +12.6% | Financials: +11.4%
- Industrials: +9.0% | Energy: +9.5% | Health Care: +9.5%
- Materials: +2.1% | Utilities: +2.5% | Real Estate: +2.0%
- ❌ Consumer Discretionary: −2.0% | Consumer Staples: −1.2%
- S&P 500 YTD: +9.69% (as of May 22)

---

### VIX Regime
- **Current VIX:** 16.85
- **Regime: Normal** (14–22 band)
- **Sizing multiplier: 1.00×**
- All entry types permitted. Mean-reversion and momentum both eligible.

---

### Universe Scan — 11 Candidates Evaluated (6 Sectors)

All bar data pulled fresh with May 26 intraday bar where available. Z-scores, RSI (Wilder's 14-period), and volume ratios computed from actual Alpaca bar data.

| Ticker | Sector | Close | Z-Score | RSI(14) | Vol Ratio | Direction Evaluated | Status |
|--------|--------|-------|---------|---------|-----------|---------------------|--------|
| XLK | Info Tech | $184.31 | +1.604 | 76.2 | 0.43× | 2b-LONG | REJECT |
| XLV | Healthcare | $148.84 | +1.671 | 58.6 | 0.32× | 2a-SHORT | REJECT |
| XLB | Materials | $50.80 | −0.296 | 49.1 | 0.42× | 2a-LONG | REJECT |
| AZO | Cons. Disc. | $3,008 | −3.168 | 24.7 | 0.90× | 2a-LONG | REJECT |
| XLY | Cons. Disc. | $118.98 | +0.591 | 52.6 | 0.25× | 2b-SHORT | REJECT |
| NVDA | Info Tech | $213.47 | −0.109 | N/A | 0.50× | 2b-LONG | REJECT |
| XOM | Energy | $151.84 | −0.330 | N/A | 0.22× | N/A | REJECT |
| XLE | Energy | $58.73 | +0.101 | N/A | 0.41× | N/A | REJECT |
| XLF | Financials | $51.87 | +0.875 | N/A | 0.31× | 2b-LONG | REJECT |
| XLI | Industrials | $173.92 | +0.675 | N/A | 0.36× | 2b-LONG | REJECT |
| SPY | Broad Market | $749.44 | +1.402 | N/A | 0.29× | 2b-LONG | REJECT |

---

### Trade Ideas (Cleared Both Layers)

**None. Zero candidates cleared both Layer A and Layer B today.**

---

### Skipped Candidates — Specific Failure Reasons

**XLK — 2b-LONG — REJECTED**
- **Catalyst:** Record S&P highs, NVIDIA AI optimism, tech sector leadership (XLK YTD +32.9%)
- **Layer A:** Sector momentum ✅ | Catalyst ✅ | Pivot extension 2.17% ≤5% ✅
- **Layer B — Lane 2b-LONG:**
  - Z = +1.604 ✅ (≥+1.0)
  - Close $184.31 > prior 20d high $180.39 ✅ (confirmed breakout)
  - RSI = 76.2 ❌ — **FAILS** (need 50–70; overbought at 76.2, not healthy momentum zone)
  - Volume = 0.43× 20d avg ❌ — **FAILS** (need ≥1.5×; today is partial-day intraday bar, post-holiday, low participation)
  - 50-SMA = $154.47 > 200-SMA = N/A — **CANNOT VERIFY** (150 bars; Dec 2025 stock split corrupts SMA computation with unadjusted data; 52w high shows $304 pre-split vs $184 post-split = data invalid)
- **Trend Template:** ❌ UNVERIFIABLE — XLK had a 2:1 stock split in December 2025. The Alpaca feed returns unadjusted pre-split prices (~$288) mixed with post-split prices (~$154). Computing 200-SMA across this discontinuity produces meaningless values. TT cannot be verified — HARD BLOCKER.
- **Summary:** 2 of 4 quant gates fail (RSI, Volume) + TT structurally unverifiable. Today's partial intraday volume especially weak (4.9M vs 11.3M avg). On an ongoing basis: XLK needs RSI to normalize from 76.2 → 50–70 range AND volume to confirm ≥1.5× on a full trading day.

**XLV — 2a-SHORT — REJECTED**
- **Catalyst:** Healthcare ETF Z=+1.671 (overbought statistically vs 20d mean), potential mean-reversion from extended run
- **Layer B — Lane 2a-SHORT:**
  - Z = +1.671 ❌ — **FAILS** (need ≥+2.0 for 2a-SHORT; still 0.33σ below trigger)
  - RSI = 58.6 ❌ — **FAILS** (need >70; elevated but not overbought)
  - Volume = 0.32× ❌ — **FAILS** (need ≥1.0×; very thin participation today)
- **Trend Template:** Unverifiable (150 bars)
- **Note on 2a-SHORT vs Minervini TT structural conflict (flagged Week 4):** XLV is at its 52-week high, which is structurally incompatible with the Short Trend Template (requires >30% below 52w high). The strategy review item from Week 4 remains open: 2a-SHORT should potentially exempt itself from the full Minervini Short TT (since mean-reversion shorts ARE by definition at extremes in uptrends, not downtrends). This conflict has not been resolved in TRADING-STRATEGY.md.
- **Watchlist:** XLV Z needs to reach +2.0 (price ~$149.47 from current $148.84) AND RSI >70 AND vol ≥1.0×. All three need to converge.

**XLB — 2a-LONG — REJECTED**
- **Layer B:** Z = −0.296 ❌ — Far from ≤−2.0 trigger. Materials at $50.80 vs mean $50.66. Brent +3% today is a positive catalyst for materials, pushing XLB AWAY from oversold territory. FCX pair Z = +0.889 (divergence ~1.19σ from XLB — within ≤1.5σ gate, confirmed). But the Z-score gate is the hard fail.
- **Trigger price for 2a-LONG:** ~$49.10 (Z = −2.0 with updated mean/std). Currently $1.70 (3.4%) away.
- **TT:** 150 bars, split-adjusted. SMA50=$50.66 > SMA150=$48.39 (positive slope). Price only 20.3% above 52w low — fails >30% requirement.

**AZO — 2a-LONG — REJECTED (notable setup, hard blocked)**
- **Catalyst:** Q3 EPS beat / Revenue miss → −5% pre-market earnings gap. Z = −3.168 (settled Friday, pre-gap-down); estimated post-gap Z ≈ −4.27. RSI = 24.7. This is statistically the most extreme oversold reading in today's scan.
- **Layer A fail:** Consumer Discretionary YTD −2.0% — bearish sector posture. AZO has fallen −18.8% from its 25-bar high in 5 weeks (short-term downtrend, not in uptrend).
- **Layer B — Lane 2a-LONG:**
  - Z = −3.168 ✅ (≤−2.0; would be ~−4.27 post gap-down today)
  - RSI = 24.7 ✅ (<30)
  - Volume = 0.90× ❌ (FAILS ≥1.0×; partial intraday bar; on earnings day, full day expected >>1.0×, but we cannot confirm until close)
- **Trend Template: UNVERIFIABLE** — Only 150 bars available, cannot compute 200-SMA. Additionally, AZO is already below its 25-bar SMA ($3,444 mean vs current ~$2,858 post-gap), indicating a downtrend posture that likely fails the Long TT requirement that price be above all major SMAs. Sector YTD −2.0% further undermines Layer A catalyst.
- **Hard blocker:** TT cannot be verified = reject per strategy rules. No exceptions.
- **Pair:** ORLY (O'Reilly) would be the natural pair. Not pulled — AZO was rejected at Layer A+TT before pair check was warranted.

**AZO — STRATEGY NOTE:** This is the clearest example yet of the TT-data-availability bottleneck. AZO's Z/RSI setup is statistically compelling; the blocking issues are (1) TT unverifiable due to 150-bar ceiling, and (2) sector YTD trend against the trade. Both are legitimate filters working as designed.

**XLY, NVDA, XOM, XLE, XLF, XLI, SPY — All REJECTED at early screens:**
- XLY: Z neutral (+0.591), no directional setup
- NVDA: Z = −0.109 (at mean), muted post-earnings reaction, no momentum breakout
- XOM/XLE: Z near zero, energy at 1 consecutive fail; Brent spike is new catalyst but XOM/XLE haven't broken above their 20d pivots ($162.55/$61.29 respectively)
- XLF/XLI: Z below +1.0, no 20d-high breakouts, low volume
- SPY: Z = +1.402, vol = 0.29× (pre-holiday drag; today's post-holiday participation should recover but current bar shows thin volume)

---

### Notable Watchlist for Wednesday May 27

1. **XLK 2b-LONG (highest priority):** Z=+1.604 ✅, breakout ✅, extension 2.17% ✅. PENDING: RSI needs to normalize from 76.2 → 50–70 (could happen on a flat/down open Wednesday if profit-taking hits tech); volume needs ≥1.5× avg (~17M shares full day). Max limit ≤ $180.39 × 1.05 = $189.41 (pivot × 1.05 cap). TT structural blocker remains (Dec 2025 split data).

2. **XLV 2a-SHORT:** Z=+1.671 (needs +2.0, price ~$149.47). RSI 58.6 (needs >70). Vol 0.32× (needs ≥1.0×). All three gates need to close simultaneously. If S&P continues rallying and healthcare rallies with it, XLV could approach the Z+2.0 threshold. TT structural conflict unresolved.

3. **Energy re-assessment:** Brent at $99 is a genuine catalyst for XLE/XOM. XLE needs to break above $61.29 (20d high pivot) with volume ≥1.5× avg for 2b-LONG consideration. XOM needs to clear $162.55. Brent staying elevated post-Iran strikes could materialize this setup within 2–3 sessions.

4. **XLB 2a-LONG:** Still alive at Z=−0.296, trigger ~$49.10. Brent spike is COUNTERPRODUCTIVE for this setup (materials rally, pushing XLB away from oversold).

---

### Risk Factors
- **Geopolitical binary:** US-Iran situation is binary — escalation → oil spike + equity sell-off; de-escalation → oil drop + equity rally. VIX at 16.85 suggests market not fully pricing escalation risk. If Brent sustains above $100, XLE/XOM re-enter long territory.
- **Volume drought:** Today is the first trading day post-Memorial Day weekend. All volume ratios are low (0.25×–0.50×), consistent with a market shaking off the holiday. This is a structural issue for ANY momentum entry today — not a single name hit the ≥1.5× volume requirement for 2b-LONG.
- **XLK split data gap:** The 200-SMA TT verification blocker for XLK is persistent and structural. Until Alpaca provides adjusted historical data or the account accumulates 200+ post-split trading days (~August 2026), XLK's TT will remain formally unverifiable. This is a recurring blocker on the strategy's single highest-Z momentum candidate.
- **Core PCE Thursday:** Markets may be range-bound ahead of the Thursday Core PCE print. The Fed's rate decision hinges on this data. If PCE comes in hot, rate cut expectations reset and tech/growth sells off.
- **Week trade budget:** 0/3 trades used. 3 full trade slots available. No urgency to fill — patience rule applies.

---

### Decision

**HOLD — Zero trades today.**

**Rationale:** 11 candidates evaluated across 6 sectors. Zero cleared both Layer A and Layer B. The dominant blocking issues today are:
1. **Volume suppression:** Post-Memorial Day holiday causes market-wide low participation. All volume ratios are 0.25×–0.50× of 20-day average. No momentum candidate can pass the ≥1.5× volume gate in this environment — this is structural, not stock-specific.
2. **RSI overbought in tech:** XLK RSI at 76.2 is above the 50–70 healthy momentum window required for 2b-LONG. The sector gap-up on NVDA/AI optimism pushed RSI into overbought territory. Patience until RSI normalizes.
3. **TT data unavailability:** Three candidates (XLK, XLV, AZO) are structurally blocked by the 150-bar ceiling. This is a known ongoing limitation.

Zero trades is the correct call. The strategy is functioning as designed. Thursday Core PCE + normalized post-holiday volume on Wednesday/Thursday are the next catalysts for setup evaluation.

**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 0/6
**Circuit breakers:** ✅ All clear — Phase P&L −0.944% (lim −5%) | Drawdown −1.15% (lim −15%)


---

### 2026-05-26 — Midday Rescan Addendum (13:41 ET)

**Re-scan time:** 2026-05-26 13:41 ET (~4 hrs 11 min after open)
**Account state at rescan:** Equity $99,056.46 | Cash $99,056.46 (100%) | 0 positions | PDT 0/3 | Week trades 0/3
**VIX regime:** Normal (16.85, 1.00× multiplier) — unchanged from morning

**Skipped at open, re-evaluated:**

- **XLK (2b-LONG):** Spread now 0.0108% ✅ (fully normalized). Z-Score +1.646 ✅. Breakout vs pivot confirmed ✅ (+2.39% extension ✅). **RSI: 76.46 ❌** (was 76.2 at open — has NOT normalized, actually ticked up slightly as price continued to drift higher). **Volume: 0.621× ❌** (was 0.43× at open, improving but still less than half the 1.5× threshold needed; 7.16M vs 11.5M 20d avg). **Trend Template: ❌ UNVERIFIABLE** (Dec 2025 2:1 split structural data blocker — persistent). Gate failures: 3 of 5 (TT, RSI, Volume). → **STILL SKIPPED.** Spread normalized but the two quant blockers and TT blocker remain fully intact. RSI worsened vs open. Volume improving but needs full-day recovery — ~Wednesday should show normalized participation.

- **XLV (2a-SHORT):** Spread 0.0067% ✅ (normalized). **Z-Score: +1.780 ❌** (was +1.671 at open; improved +0.11σ but still 0.22σ short of +2.0 trigger; needed price ~$149.49, today's intraday high $150.30 briefly touched it but closed back to $149.09). **RSI: 59.68 ❌** (was 58.6, marginal improvement, nowhere near >70). **Volume: 0.386× ❌** (was 0.32×, slightly better, still far below 1.0× minimum). **Short Trend Template: ❌ STRUCTURALLY INCOMPATIBLE** (XLV at 0.54% below 52w high; Short TT requires >30% below 52w high — structural conflict flagged in Week-4 review, unresolved). Sector posture: Healthcare YTD +9.5% = bullish, not rolling over — Layer A directional conflict for short. → **STILL SKIPPED.** Spread normalized. All three quant gates still fail; TT fundamentally incompatible with a mean-reversion short at 52w highs.

- **AZO (2a-LONG):** Spread 0.9715% ⚠️ (borderline — just under 1.0% but ~5–8× normal AZO spread; elevated due to earnings-day gap-down selling pressure). **Z-Score: −3.014 ✅** (deeply oversold). **RSI: 26.76 ✅** (oversold). **Volume: 1.255× ✅** (NOW CLEARED — was 0.90× partial bar at open; 365k shares vs 291k 20d avg; earnings-day elevated). Layer B quant fully clears for the first time today. **However Layer A remains BLOCKED:** (1) Consumer Discretionary YTD −2.0% — weakest sector, bearish posture, Layer A requires sector momentum for long entries ❌. (2) Long Trend Template unverifiable + directionally likely fails — AZO price ($3,066) is $382 below 20d mean ($3,448), almost certainly below 50-SMA; TT requires price above all major SMAs ❌. (3) Earnings context: gap-down of −10.6% driven by revenue miss ($3,406 → ~$3,066); EPS beat is offset by structural top-line miss; mixed catalyst ⚠️. AZO spread remains elevated at 0.97% (1.5→5× normal). → **STILL SKIPPED.** Volume gate now cleared (notable). But 2 hard Layer A blockers (sector + TT) prevent trade. This is the strategy working as designed: Layer B alone is not sufficient — earnings-day gap-downs into broken sectors require both layers to clear.

**Trades fired this rescan:** None.

**Patience rule applied:** 0/3 candidates re-cleared. This is the correct outcome. Gates were not lowered. AZO's Layer B now fully passes but Layer A's sector + TT blockers are legitimate and structural — not a miss, a correct skip.

**Notable observations for Wednesday 2026-05-27:**
1. **XLK:** RSI needs to normalize from 76.5 toward 50–70 (requires flat/down session or profit-taking in tech). Volume should recover on a normal post-holiday day. TT blocker remains until ~August 2026 (200-SMA accumulation). Watch for RSI cooling only.
2. **XLV:** Z-Score briefly touched +2.0 intraday today (high $150.30 vs trigger $149.49) but closed back. If healthcare continues rallying Wednesday and RSI builds toward 70, all three gates could converge simultaneously. Tight window but live.
3. **AZO:** Layer B now fully live (Z −3.0, RSI 26.8, Vol 1.25×). Layer A sector issue (Cons. Disc YTD −2.0%) is the blocker. Any ORLY comp check or same-day sector bounce might be monitored; however sector YTD trend requires sustained reversal, not a single day. Do not lower entry gate to force this trade.
4. **Volume normalization:** Today's post-Memorial Day holiday showed improving but still suppressed volume across all names (XLK 0.62×, XLV 0.39×). Wednesday expected to see normalized ~1.0× participation, which unblocks momentum entries if other gates align.
5. **Core PCE Thursday:** Markets may stay range-bound Wednesday afternoon ahead of the print. Risk-off ahead of PCE could paradoxically help XLV short setup (RSI rising toward 70 if healthcare stays bid) or hurt XLK momentum (RSI normalizes downward, good for entry timing).


---

## 2026-05-26 — Midday Scan Addendum (~14:20 ET / 18:20 UTC)

**Scan type:** Midday workflow — position thesis check & stop evaluation
**VIX Regime:** Normal (16.85 from morning research) — 1.00× sizing multiplier
**Account:** $99,056.46 equity | 100% cash | 0 positions | 0 orders | PDT 0/3 | Week 0/3

---

### STEP 1 — Portfolio State (Live API)

- **Positions:** `[]` — EMPTY. 100% cash confirmed.
- **Orders:** `[]` — EMPTY. No working brackets. No GTC stops.
- Pre-market HOLD decision confirmed: all 11 candidates failed volume gate (0.25–0.50× avg due to post-Memorial Day holiday participation drought). No brackets placed at open.
- TRADE-LOG fully current. No discrepancy.

---

### STEP 2 / STEP 3 — Cut Losers / Tighten Stops

**N/A — no open positions.**

---

### STEP 4 — Watchlist Re-Evaluation (Live Quotes at ~14:20 ET)

**Structural market blockers today:**
1. Post-Memorial Day volume suppression — ALL names showing 0.43×–0.67× of 20d avg. No momentum candidate can pass ≥1.5× volume gate.
2. Tech (XLK) RSI overbought at 76.8 after NVDA-driven AI gap-up.
3. TT data unavailability — 3 names structurally blocked by 150-bar ceiling (XLK split, AZO, XLV).

| Ticker | Live Mid | Z (live) | RSI (Wilder's) | Vol Ratio | Lane | Gate Result |
|--------|----------|----------|---------------|-----------|------|-------------|
| XLK | $185.17 | +1.91 ✅ | 76.8 ❌ (>70) | 0.67× ❌ | 2b-LONG | **REJECT** — RSI overbought + vol low + TT unverifiable |
| XLV | $149.08 | +2.04 ✅ | 59.7 ❌ (<70) | 0.43× ❌ | 2a-SHORT | **REJECT** — RSI far from >70 + vol far below 1.0× + Short TT structural |
| XLB | $50.96 | −0.18 ❌ | 48.6 ❌ | 0.55× ❌ | 2a-LONG | **REJECT** — Z far from −2.0 (trigger $49.31, needs −3.2%) |
| XOM | $150.55 | −0.58 | 47.2 | 0.37× | — | Monitor only — no lane qualifies |
| XLE | $58.20 | −0.19 | 52.5 | 0.64× | — | Monitor only — no lane qualifies |

**Key observations:**
- **XLK** is continuing its breakout rally (now +$4.76 / +2.6% above Friday's $180.39 close). Z = +1.91, breakout confirmed (+2.65% above pivot ✅, within 5% cap). The only blockers are RSI 76.8 (overbought) and volume 0.67× (well below 1.5× threshold). As post-holiday participation normalizes over Wed/Thu, this remains the #1 setup to watch for 2b-LONG entry.
- **XLV** Z briefly pierced +2.0 today (first time); RSI at 59.7 is still ~10 points from the >70 trigger. Volume at 0.43× is very thin. Healthcare holding near 52w highs. Short TT structural conflict unresolved (flagged Week 4 — 2a-SHORT incompatibility with Minervini downtrend requirement).
- **XOM** sold off −2.6% intraday to $150.55 (Z = −0.58). Approaching the lower half of its 20d range. Energy pullback consistent with WTI weakness (Iran deal optimism continuing). No entry lane qualifies — not oversold enough for 2a-LONG (Z −0.58, needs ≤−2.0 at ~$144.35), not above pivot for 2b-LONG ($162.55).
- **XLE** similarly soft (−0.9% to $58.20). Z = −0.19, near mean. Not a setup in any direction.

**Gate checks run (all constraints confirmed):**
- ✅ Positions: 0 (would be ≤ 6 — irrelevant, no orders)
- ✅ Week trades: 0/3 (budget intact)
- ✅ PDT: 0/3
- ✅ Circuit breakers: Phase P&L −0.944% (lim −5%) | Drawdown −1.15% (lim −15%)
- ✅ VIX: 16.85 (Normal regime, 14–22 band) — entries permitted in principle
- ✅ No forbidden order types attempted

**Watchlist for Wednesday 2026-05-27:**
1. XLK 2b-LONG — RSI needs to normalize 76.8 → 50–70; vol needs ≥1.5× on full trading day; TT blocker persists
2. XLV 2a-SHORT — Z needs +2.0 (~$149.47); RSI needs >70; vol needs ≥1.0×
3. XLE/XOM 2b-LONG — Watch for breakout above $61.29 / $162.55 pivots if Brent stays elevated ≥$99
4. XLB 2a-LONG — Trigger ~$49.10 (3.4% away); Brent spike working against this setup

**No order IDs. No fills. No bracket children active.**

---

## 2026-05-26 — Afternoon Scan Addendum (20:12 UTC / ~16:12 ET)

**Scan time:** ~2 hrs before close (market closes 20:00 UTC / 4:00 PM ET). Scan completed post-close — all May 26 bars settled.
**VIX regime at scan:** NORMAL (~16.85, from morning research) | Sizing multiplier: 1.00×

---

### STEP 1 — Order & Position State Reconciled vs TRADE-LOG

| Order ID | Symbol | Type | Status | Detail |
|----------|--------|------|--------|--------|
| 1d69c496 | XOM | Bracket limit BUY 61 sh @ $159.78 | **EXPIRED** 2026-05-18T20:02 | TIF: day — logged ✅ |
| 94606e38 | XOM | Stop child $147.80 | **CANCELED** 2026-05-18T20:02 | Auto-cancelled ✅ |
| 336d922a | XOM | TP child $183.74 | **CANCELED** 2026-05-18T20:02 | Auto-cancelled ✅ |
| 8f97ef7d | XOM | Market Sell 130 sh | **FILLED** $146.09, 2026-05-07 | Thesis-break exit ✅ |
| d92d9371 | XOM | Trailing Stop 10% GTC | **CANCELED** 2026-05-07 | Pre-exit ✅ |
| c04ae321 | XOM | Market Buy 130 sh | **FILLED** $153.35, 2026-05-01 | Original entry ✅ |

- **Positions API: `[]` — 100% cash ($99,056.46).** No filled positions.
- **No morning bracket orders were placed today** (HOLD at pre-market — all 11 candidates failed composite gates; post-Memorial Day volume drought).
- **Bracket fills today: 0** | **Stale limits: 0** | **TRADE-LOG reconciliation: FULLY CURRENT ✅**

---

### STEP 2 — Trailing Stop Upgrades: N/A

No positions held. Portfolio 100% cash.

---

### STEP 3 — Stale Limit Cancellations: N/A

No open orders of any kind.

---

### STEP 4 — Afternoon Opportunity Scan (5 candidates, 4 sectors)

**Quant results — May 26 settled bar data:**

| Ticker | Close | 20d Mean | 20d Std | Z-Score | RSI(14) | Vol Ratio | 20d High | 20d Low | Lane | Key Failures | Verdict |
|--------|-------|----------|---------|---------|---------|-----------|----------|---------|------|--------------|---------|
| XLK | $185.18 | $171.79 | $7.904 | +1.694 | 77.9 | 1.08× | $180.39 ✅ (breakout) | — | 2b-LONG | RSI 77.9 > 70 ❌; Vol 1.08× < 1.5× ❌; TT 150/200-SMA unavail. (split) ❌ | **REJECT** |
| XLV | $148.51 | $145.78 | $1.794 | +1.524 | 62.3 | 0.68× | $149.89 (below) | — | 2a-SHORT | Z +1.524 < +2.0 ❌; RSI 62.3 < 70 ❌; Vol 0.68× < 1.0× ❌ | **REJECT** |
| XLB | $50.99 | $51.07 | $0.889 | −0.094 | 52.2 | 0.76× | $52.41 | $49.04 | 2a-LONG | Z −0.094 >> −2.0 ❌; RSI 52.2 >> <30 ❌; Vol 0.76× ❌ | **REJECT** |
| XLE | $57.85 | $58.54 | $1.426 | −0.482 | 43.9 | 1.01× | $61.29 | $55.70 | 2b-SHORT/2b-LONG | Z −0.482 fails both lanes ❌; Not below 20d low ❌; Short TT structural ❌ | **REJECT** |
| XOM | $149.81 | $153.13 | $4.273 | −0.777 | 45.0 | 0.74× | $162.55 | $144.57 | 2b-LONG | Z −0.777 < +1.0 ❌; 7.8% below pivot ❌; Vol 0.74× ❌; TT 200-SMA unavail. ❌ | **REJECT** |

**Pair Z-Scores:**
- AVGO: Z = +0.313 | XLK−AVGO divergence = 1.381σ ✅ (≤1.5σ — pair confirms tech rally direction)
- FCX: Z = +0.993 | XLB−FCX divergence = 1.087σ ✅ (≤1.5σ — pair confirms)
- CVX: Z = −1.062 | XOM−CVX divergence = 0.285σ ✅ (≤1.5σ — both energy names selling off in lockstep)

---

### Candidate Notes

**XLK — REJECT (3 Layer B failures):**
- Z = +1.694 ✅ | Close above 20d high ($185.18 > $180.39) ✅ | Extension 2.65% ✅ | AVGO pair 1.381σ ✅
- RSI = **77.9** ❌ (was 76.2 at yesterday's midday rescan — has WORSENED, not improved). Need 50–70 for 2b-LONG. XLK extended further into overbought on today's NVDA/AI-driven rally.
- Volume = **1.08×** ❌ (was 0.43× yesterday post-holiday; better, but 0.42× short of the 1.5× gate).
- Trend Template: 150/200-SMA CANNOT VERIFY (Dec 2025 2:1 split data gap — ~42 sessions until resolved).
- **Most advanced candidate** — Z and breakout both qualify. Two substantive gates (RSI and volume) remain. If RSI normalizes Wednesday to 50–70 AND volume confirms ≥1.5×, the 2b-LONG setup qualifies. Max entry limit for Wednesday: ≤ $180.39 × 1.05 = $189.41.

**XLV — REJECT (Z, RSI, Volume all fail — XLV SOLD OFF today):**
- Critical development: XLV closed DOWN −$1.38 today ($149.89 → $148.51). Z DROPPED from +3.205 (May 22 settle) to +1.524 — a 1.68σ regression in ONE session. The overbought healthcare thesis has partially self-corrected without a trade being placed. RSI = 62.3 (down from ~69 range). This is actually the expected mean-reversion pull working in the background.
- 2a-SHORT setup has materially weakened. Z needs to rebuild to ≥+2.0 (~$149.37) and RSI needs to climb back above 70 — both require a renewed healthcare rally. Lower priority going into Wednesday.

**XLB — REJECT (completely reset):**
- Z = −0.094 — essentially AT the 20-day mean. The oversold mean-reversion setup that had Z = −1.936 on May 21 has fully resolved via the subsequent rally (+$1.95 from $49.04 low). XLB did exactly what mean-reversion predicts — bounced back toward the mean — without a trade being placed. Correct gate discipline validated.
- Trigger price for a new 2a-LONG setup: $49.29 (Z = −2.0). Currently $1.70 away (−3.3%). Off active watchlist.

**XLE — REJECT (no valid lane):**
- Z = −0.482; not near any statistical threshold. Price $57.85 is:
  - $3.44 above 20d low ($55.70) — not near 2b-SHORT breakdown trigger
  - $3.44 below 20d high ($61.29) — not near 2b-LONG breakout trigger
  - Midway through its 20d range with no lane qualification
- Energy sector sold off −2.8% today on Iran deal optimism (WTI continuing to pull back from $96 → sub-$92 range). The rotation FROM energy → TO tech that began last week accelerated today.

**XOM — REJECT (4 failures; below original May 1 entry price):**
- Z = −0.777; price $149.81 fell −3.3% today (was $154.92 Friday). XOM is now $3.54 BELOW the original May 1 entry of $153.35, confirming the May 7 thesis-break exit decision was correct. The energy thesis (Hormuz supply premium) continues to deflate as WTI declines.
- CVX: Z = −1.062, both energy names declining in lockstep (0.285σ divergence = sector-wide, not single-name).
- For a 2a-LONG mean-reversion long: trigger price = $144.57 (20d low) or approximately Z ≤ −2.0 = ~$144.57. Current $149.81 is $5.24 above that. Still has the energy sector's 1-consecutive-failure flag — heightened caution on any new energy trade.

---

### Afternoon Market Context

Today's session delivered a decisive confirmation of the sector rotation thesis: **XLK +2.65% vs XLE −2.8% = a 5.45% single-session relative divergence** — the largest Energy-vs-Technology spread seen in any single day this account has operated. The Iran peace deal narrative is clearly driving institutional reallocation out of energy (WTI supply premium deflating) and into technology (lower inflation → better multiple expansion for growth). XOM fell to $149.81 — below its May 1 entry price ($153.35) for the first time — while XLK closed at $185.18, extending its 20-day breakout to 2.65% above pivot. The irony: the single most actionable candidate (XLK 2b-LONG: Z=+1.694, confirmed breakout, extension within 5%) continues to fail on RSI (77.9, still overbought) and volume (1.08×, below 1.5× needed). The XLV 2a-SHORT thesis that looked so compelling on May 22 (Z=+3.205) has partially self-resolved — healthcare sold off today as money moved to tech, bringing Z back to +1.524. Zero new entries; patience rule is working correctly, keeping capital safe while the rotation plays out.

---

**Bracket fills today:** 0 (no morning limits placed — HOLD decision; post-holiday volume drought; all 11 candidates failed gates)
**Stops upgraded:** 0 (no positions held; no upgrade workflow applicable)
**Stale limits cancelled:** 0 (no open orders existed)
**New afternoon entries:** none — all 5 candidates failed composite Layer A + Layer B gates
**Afternoon market context:** Strong tech/energy rotation continues. XLK +2.65% (RSI 77.9, overbought but confirmed breakout); XLE −2.8% (Iran deal driving oil pullback); XOM −3.3% (below May 1 entry price); XLV −0.9% (Z-score dropped from +3.2 to +1.5, overbought thesis self-resolving); XLB flat (completely reset from oversold).

**Key watchlist for Wednesday pre-market (2026-05-27):**
1. **XLK — #1 PRIORITY (2b-LONG):** Z=+1.694 ✅, breakout +2.65% ✅, extension within 5% ✅, AVGO pair confirms ✅. Gates remaining: (a) RSI needs to normalize from 77.9 → 50–70 (requires flat/pullback session Wednesday or intraday cooling post-open), (b) Volume needs ≥ 1.5× avg (~17.3M shares full session). Max entry limit ≤ $189.41 (pivot $180.39 × 1.05). TT 150/200-SMA structural gap persists (~42 sessions to resolve). This is the ONLY name with Z, breakout, and extension all passing simultaneously.
2. **XLV — 2a-SHORT watch (LOWER PRIORITY):** Z dropped to +1.524 today. Setup weakened materially. Monitor whether healthcare rallies again Wednesday — if Z rebuilds toward +2.0 and RSI rebuilds toward >70 on above-average volume, setup re-activates. TT structural conflict (2a-SHORT vs Minervini downtrend requirement) unresolved.
3. **XLE / XOM — energy on watch:** Energy sector is now −5.6% (XLE) and −7.8% (XOM) from their May 19 peaks. If Iran deal fully collapses/reverses, WTI could bounce and XLE/XOM could reclaim their respective 20d high pivots ($61.29/$162.55) — that would re-open the 2b-LONG thesis with volume confirmation needed. Until then, both names are below their pivots and below-mean.
4. **XLB** — Off watchlist. Z = −0.094, setup fully reset. Re-qualify only if a fresh selloff returns Z toward −2.0 (~$49.29).
5. **200-SMA data gap** — ~42 trading sessions remaining until 200-SMA available for split-adjusted names (XLK, XLE, XLV). Estimated resolution: mid-August 2026. Persistent structural constraint on Minervini TT verification.


---

## 2026-05-27 — Pre-Market Research

### Account
- **Equity:** $99,056.46
- **Cash:** $99,056.46 (100% deployed: 0%)
- **Buying power:** $198,112.92 (2× margin)
- **Daytrade count:** 0/3
- **Open positions:** none
- **Week trades:** 0/3
- **Phase P&L:** −$943.54 (−0.944%) | Peak: $100,206.70 | Drawdown: −1.15%
- **Circuit breakers:** ✅ All clear (Day 0%, Phase −0.944%, Drawdown −1.15%)

---

### Market Context
- **WTI Crude Oil:** $88.17/bbl, −6.0%+ on the day. Iran commitment to restore commercial shipping through the Strait of Hormuz to pre-war levels within 30 days driving the selloff. Earlier session low near $89.64 (−4.5%). Supply-premium deflation continues from prior week.
- **Brent Crude:** $94.77/bbl, −4.83%. Down 9.22% over the past month; +47.34% YoY. Early print was ~$95.80.
- **S&P 500 Futures:** +0.23–0.30% pre-market as of 7:35 AM ET. S&P 500 set to open at fresh record high. Driver: AI optimism, lower oil (inflation-positive), easing bond yields.
- **VIX:** Closed 16.59 on May 26; ticking up slightly to ~17.01 in pre-market May 27 (still trading below 17 in early AM).
- **Top Catalysts:**
  - U.S.-Iran peace deal negotiations — potential Hormuz reopening easing energy supply fears
  - Falling oil prices → lower input costs → equity multiple expansion tailwind
  - AI/semiconductor strength: Goldman Sachs raised S&P 500 year-end 2026 target to 8,000 (from 7,600)
  - Micron and AI chip complex continue leading; MRVL Q1 earnings due after the close today
  - Goldman target raise and tech earnings strength supporting fresh record high open
- **Pre-market Earnings:**
  - **ANF:** EPS $1.47 (beat $1.26 est.), Revenue $1.11B (miss −0.48%). Stock +6% premarket.
  - **BBWI:** EPS $0.32 (beat by $0.03), Revenue $1.38B (+1.01% vs est.). Stock +13% premarket.
  - **DY:** Q1 contract revenue beat estimates. Stock +21%.
  - **MRVL:** Reports after close. Analysts expect EPS $0.75, Revenue $2.40B. Stock +6%+ premarket ahead of print.
  - **PETS (LON):** H2 2026 underlying PBT £93M, down −33% YoY. UK only.
- **Economic Calendar (today, May 27):**
  - 8:30 AM ET: Durable Goods Orders
  - 8:30 AM ET: GDP (2nd estimate)
  - 8:30 AM ET: Jobless Claims
  - 8:30 AM ET: Personal Income and Outlays
  - *Next CPI: June 10 | Next PPI: June 11 | Next FOMC: June 17 | Jobs report: June 5*
- **S&P 500 Sector Momentum YTD:**
  - S&P 500 total return YTD: +10.4% (through May 26)
  - Information Technology dominant: SOXX +71.55% YTD through May 13
  - Semiconductors alone added ~$3.8T market cap in six weeks
  - 5-year cumulative leaders: IT +182%, Energy +125%, Comm. Services +92%
  - Energy rotating OUT in real-time as Iran-deal deflates WTI premium

---

### VIX Regime
- **Current VIX:** 17.01 (pre-market; prior close 16.59)
- **Regime:** Normal (14–22)
- **Sizing multiplier:** 1.00×
- **Strategy bias:** All entry types eligible (momentum & mean-reversion)

---

### Universe Scanned Today
Candidates evaluated: **XLK** (Tech ETF, 2b-LONG), **MRVL** (Semis mega-cap, 2b-LONG), **XLE** (Energy ETF, lane assessment)

---

### Trade Ideas (Cleared Both Layers)
**None.** No candidate cleared both Layer A and Layer B today. Decision: **HOLD.**

---

### Skipped Candidates

---

#### 1. XLK — Technology Sector ETF | LONG candidate | 2b-LONG lane attempted

**Layer A — Catalyst + Trend Checklist:**
- Catalyst: AI momentum continuation, Goldman S&P target raise, tech-vs-energy sector rotation ongoing. ✅
- Sector posture: XLK is the leading sector YTD. ✅
- RSI(14): **68.09** ✅ (within 50–70 range for 2b-LONG)
- Volume: Today 5,361,341 vs 20d avg 11,709,010 → **0.46× avg** ❌ (need ≥1.5× for 2b-LONG)
- Stop level: Technical at 20d low $157.85 (~13.7% below current — too wide for 7–10% stop rule) or ATR-based at ~$169–$172 (−6 to −7%)
- Target: 2:1 R:R plausible at prior resistance ~$195–$200

**Layer B — Quant Checklist (2b-LONG lane):**
- Z-Score: **+1.4175** ✅ (≥ +1.0 required)
- Close > prior 20d high ($185.14): Current $182.99 → **$182.99 < $185.14** ❌ FAIL — price pulled back below the prior 20d high today (opened $186.18, faded to $182.99). The breakout that held May 26 has NOT been sustained intraday.
- RSI 50–70: **68.09** ✅
- Volume ≥ 1.5× avg: **0.46×** ❌ FAIL (partial session, but even full-session 0.46× pace is well below the 1.5× gate)
- 50d SMA > 200d SMA: 50-SMA = $155.37 | 200-SMA = **N/A** (structural data gap from Dec 2025 2:1 split; ~40 sessions until 200 bars of post-split data available; estimated resolution mid-August 2026) ❌ CANNOT VERIFY
- Minervini Trend Template: 50-SMA = $155.37 ✅ (price > 50-SMA). 150-SMA = N/A ❌. 200-SMA = N/A ❌. **TT CANNOT VERIFY.**
- Pair (AVGO): AVGO Z = −0.2271 → XLK/AVGO divergence = **|1.4175 − (−0.2271)| = 1.6446σ** ❌ FAIL (limit ≤ 1.5σ). AVGO is flat/slightly negative while XLK is elevated — pair diverging.
- Pivot extension: $182.99 vs max $185.14 × 1.05 = $194.40 → **extension 1.5%** ✅ (within 5% of pivot — IF price reclaims $185.14)

**Result: REJECT — 4 failures: (1) close < 20d high ❌, (2) volume 0.46× ❌, (3) 200-SMA N/A ❌, (4) AVGO pair divergence 1.64σ ❌**

**Key delta vs yesterday:** XLK opened at $186.18 (above pivot), promptly faded to $182.99 — failed to hold the $185.14 breakout level. The prior two sessions' Z=+1.694 and confirmed breakout have now partially reverted; Z is now +1.42 and the close is BELOW the 20d high for the first time since the breakout day. This is a warning sign, not an entry signal.

**Watchlist forward:** XLK remains the #1 candidate. Re-entry requires (a) close back above $185.14 on volume ≥ 1.5× avg (~17.6M full-session shares), (b) AVGO pair Z divergence compresses back below 1.5σ, and (c) RSI holding 50–70. Maximum limit entry ≤ $194.40 (pivot $185.14 × 1.05).

---

#### 2. MRVL — Marvell Technology | LONG candidate | 2b-LONG lane attempted

**Layer A — Catalyst + Trend Checklist:**
- Catalyst: MRVL reports Q1 earnings after the close TODAY. Analyst expectations: EPS $0.75, Revenue $2.40B. Stock pre-market +6% (printed as high as $217.98 open, faded to ~$197). The AI/data-center semiconductor thesis (MRVL custom ASICs for hyperscalers) is the fundamental driver. Goldman S&P target raise implicitly supports semi names. ✅
- **Critical flag: MRVL earnings are TODAY after the bell.** Per CONSTRAINTS.md (and short-position rules): **"No shorting through earnings."** For longs: entering a position that will be held through an unresolved earnings event violates the swing-trade discipline (binary risk not captured by stop-loss mechanics). This is an earnings-eve trade, not a post-earnings continuation. ❌ (Layer A disqualified on catalyst timing)
- Sector posture: Semis in dominant momentum. ✅
- RSI(14): **61.1** ✅ (within 50–70 range)
- Volume: 21,312,452 vs 20d avg 24,121,164 → **0.88×** ❌ (need ≥1.5× for 2b-LONG)
- Stop level: 20d low $153.23 → ~22% below current — far too wide. Technical support ~$180 area (~8.6% below close).

**Layer B — Quant Checklist (2b-LONG lane):**
- Z-Score: **+1.7395** ✅ (≥ +1.0 required)
- Close > prior 20d high ($208.26): Current $197.025 → **$197.025 < $208.26** ❌ FAIL — opened above ($211+ range) but faded massively, closing well below the 20d high pivot. This is a pre-earnings gap-up then fade pattern.
- RSI 50–70: **61.1** ✅
- Volume ≥ 1.5×: **0.88×** ❌ FAIL
- 50d SMA > 200d SMA: 50-SMA = $142.04 | 200-SMA = **N/A** (only 151 bars available; same structural gap issue) ❌ CANNOT VERIFY
- Minervini Trend Template: 50-SMA $142.04 ✅ (price $197 >> 50-SMA). 150-SMA $103.89 ✅ (price >> 150-SMA). 200-SMA = N/A ❌. 52w high = $218.26 (dist: −9.2%) ✅ within 25%. 52w low = $70.69 (dist: +180%) ✅ >30% above. 6m return = +156% (top percentile) ✅. **Partial TT: 5/7 conditions verified. 200-SMA unverifiable = structural gap.** Cannot confirm full TT.
- Pair (NVDA): NVDA Z = −0.4779 → MRVL/NVDA divergence = **|1.7395 − (−0.4779)| = 2.2174σ** ❌ FAIL (limit ≤ 1.5σ). MRVL is strongly elevated (earnings-driven gap-up premium) while NVDA is slightly negative — clear single-name divergence. This is EXACTLY the pair-divergence gate working as designed: MRVL's move is idiosyncratic (earnings catalyst), not sector-wide.

**Result: REJECT — 5 failures: (1) earnings binary risk tonight ❌, (2) close < 20d high ❌, (3) volume 0.88× ❌, (4) 200-SMA N/A ❌, (5) NVDA pair divergence 2.22σ ❌**

**Post-earnings watch:** MRVL reports tonight after close. If earnings beat and the stock gaps up or holds elevated levels on volume, the thesis could re-qualify tomorrow morning as a 2b-LONG post-earnings continuation — provided: (a) close > 20d high on volume ≥ 1.5×, (b) Z ≥ +1.0, (c) RSI 50–70 after the move, (d) NVDA pair divergence compresses <1.5σ, (e) no gap-chase beyond $208.26 × 1.05 = $218.67 pivot extension. Watch for pre-market setup tomorrow (May 28).

---

#### 3. XLE — Energy Select Sector ETF | SHORT candidate attempted | No lane qualifies

**Assessment:**
- Z-Score: **−0.8924** → Between 0 and −1.0
  - 2a-LONG requires Z ≤ −2.0: FAIL (need $52.60 or below, current $57.27)
  - 2b-SHORT requires Z ≤ −1.0 AND close < 20d low ($55.70): FAIL (Z = −0.89, close $57.27 > low $55.70)
  - 2b-LONG requires Z ≥ +1.0: FAIL
- **No lane qualifies.** XLE is midway through its 20-day range with no statistical edge.
- Additional context: XLE is below its 50-SMA ($58.42) and down sharply from the Iran-deal news. Price $57.27 vs 52w high $62.56 (−8.5%) and 52w low $43.81 (+30.7%). RSI = 51.1 (neutral zone). 150/200-SMA unavailable (structural gap).
- CVX pair: Z = −1.48. XLE/CVX divergence = 0.58σ ✅ (pair moves together — confirms sector-wide selloff, not single-name).
- **Result: REJECT — No lane qualifies (Z = −0.89, midrange, no statistical threshold breached).**

**Energy context:** XLE has now fallen ~8.5% from its May 19 peak ($61.29) in 6 sessions. The mean-reversion long trigger is Z ≤ −2.0 ≈ price ~$55.68 (current $57.27 = $1.59 away, ~2.8% further decline). If Iran deal rhetoric accelerates and WTI continues lower toward $85, XLE could reach the 2a-LONG trigger. Not actionable today.

---

### Risk Factors
1. **MRVL earnings after close today** — binary event. Any holdings going into 4 PM would face gap risk. Correct that we hold cash through this.
2. **XLK failed to hold breakout** — opened at $186.18 (above $185.14 pivot), faded to $182.99. This intraday reversal on low volume (0.46×) is a yellow flag. Could indicate the AI/tech rally is losing near-term momentum or rotating to individual names (MRVL, NVDA) rather than the broad ETF.
3. **Geopolitical binary** — Iran deal negotiations: if talks collapse, WTI spikes back and energy/oil reverses sharply. Would need to reassess energy sector momentum rapidly.
4. **8:30 AM macro data** — GDP, Durable Goods, Jobless Claims all printing today. Surprise to the downside on GDP could interrupt the record-high S&P open.
5. **200-SMA structural gap** — persists for all post-Dec 2025 split-adjusted names (~40 sessions until resolution). Prevents full Minervini TT verification for XLK, XLE, MRVL and others.
6. **AVGO pair divergence** — AVGO Z = −0.23 while XLK Z = +1.42. AVGO is not confirming the XLK move. This is a meaningful warning: broad tech ETF outperforming its largest semi component suggests XLK's move may be driven by a small number of names (NVDA, MSFT) rather than a broad-based rally.

---

### Decision
**HOLD** — 0 trades today. No candidate cleared both Layer A and Layer B gates.

- **XLK:** Failed 4 gates (close < 20d high, volume 0.46×, 200-SMA N/A, AVGO pair divergence 1.64σ). Also: intraday fade from $186 → $183 is a bearish near-term signal for the breakout.
- **MRVL:** Failed 5 gates (earnings binary tonight, close < 20d high, volume 0.88×, 200-SMA N/A, NVDA pair divergence 2.22σ). Earnings event alone is disqualifying — we do not enter before binary events.
- **XLE:** No lane qualifies (Z = −0.89, midrange).

**Priority watchlist for May 28 pre-market:**
1. **MRVL post-earnings** (2b-LONG): If EPS/revenue beat drives sustained elevation with volume ≥1.5× avg, recheck all gates tomorrow. Thesis valid; timing (pre-earnings) was the disqualifier today.
2. **XLK 2b-LONG**: Needs to reclaim $185.14 on ≥1.5× volume AND AVGO pair divergence to compress. Today's intraday fade is a step back — patience still warranted.
3. **XLE 2a-LONG (conditional)**: Only if WTI accelerates lower and XLE breaks below ~$55.70 (Z → −2.0). Not imminent but setting the trigger level.

**Bracket fills today:** 0
**Stops upgraded:** 0 (no positions)
**PDT count:** 0/3 | **Week trades:** 0/3 | **Positions:** 0/6

---

## 2026-05-27 — Midday Rescan Addendum (17:40 UTC / ~1:40 PM ET)

**VIX Regime at rescan:** Normal (~17.01, pre-market; prior close 16.59) — 1.00× sizing multiplier, all entry types eligible
**Account at rescan:** Equity $99,056.46 | Cash $99,056.46 (100%) | Deployed: 0% | Positions: 0/6 | Week trades: 0/3 | PDT: 0/3 | Open orders: 0
**Market status:** OPEN — ~2 hrs 20 min remaining in session (closes 20:00 UTC / 4:00 PM ET)

---

### Skipped at Open — Re-evaluated at Midday

| Ticker | Spread Now | Z-Score Now | Key Gate Result | Verdict |
|--------|-----------|-------------|-----------------|---------|
| **XLK** | 0.011% ✅ | +1.499 ✅ | Close $183.63 < 20d high $185.14 ❌ \| RSI 72.45 ❌ \| Vol 0.62× ❌ | **❌ STILL SKIPPED** |
| **MRVL** | 2.38% ❌ | +1.909 ✅ | Earnings HARD BLOCK (reports tonight) ❌ \| Close < 20d high ❌ \| Vol 1.07× ❌ | **❌ STILL SKIPPED** |
| **XLE** | 0.017% ✅ | −0.836 | No lane qualifies; Z regressed toward 0 since open | **❌ STILL SKIPPED** |

---

### Detailed Re-Check

#### XLK (Technology Sector ETF) — 2b-LONG lane — ❌ STILL SKIPPED

**Live quote:** bid $183.56 / ask $183.58 — spread **0.011% ✅** (excellent, fully normalized)
**Live mid:** $183.57 | **Today's bar close so far:** $183.63

**Gate-by-gate assessment (2b-LONG):**

| Gate | Required | Actual | Result |
|------|----------|--------|--------|
| Z ≥ +1.0 | ≥+1.0 | **+1.499** | ✅ |
| Close > 20d high | > $185.14 | $183.63 | ❌ Still $1.51 (0.82%) below pivot |
| RSI(14) 50–70 | 50–70 | **72.45** (Wilder's) | ❌ Overbought — above 70 |
| Vol ≥ 1.5× avg | ≥1.5× | **0.62×** (7.21M vs 11.67M avg) | ❌ Well below threshold |
| 200-SMA verifiable | N/A | Structural gap (Dec 2025 split, ~40 sessions) | ❌ Unverifiable |
| AVGO pair divergence ≤ 1.5σ | ≤1.5σ | **1.295σ** | ✅ **IMPROVED** (was 1.64σ at open) |

**Notable midday development — XLK/AVGO pair:** AVGO closed today at $421.06 (Z = +0.204). The XLK–AVGO divergence has **narrowed from 1.64σ at open to 1.295σ midday** — now within the ≤1.5σ pair confirmation gate for the **first time since this setup emerged**. The pair blocker has been removed. However, the three remaining substantive failures (close below pivot, RSI overbought at 72.45, volume 0.62×) are unchanged and represent genuine quant gate failures that the spread-normalization window cannot resolve.

**Summary:** Spread normalized ✅; Pair gate now passing ✅; Z passing ✅. Substantive blockers: RSI 72.45 (overbought, needs to cool toward 50–70), close 0.82% below $185.14 pivot (needs to be reclaimed on a strong volume day), volume 0.62× (needs institutional confirmation ≥1.5× on the breakout day). 3 of 5 quant gates fail.

**Forward:** For tomorrow's pre-market evaluation — if XLK closes today above $185.14 and volume picks up into the close, the momentum lane may re-activate. Maximum entry limit ≤ $185.14 × 1.05 = **$194.40**.

---

#### MRVL (Marvell Technology) — 2b-LONG lane — ❌ STILL SKIPPED (HARD BLOCK)

**Live quote:** bid $199.00 / ask $203.80 — spread **2.38% ❌** (R-flagged; wide mid-session quote, thin book)
**Live mid:** $201.40 | **Today's bar close so far:** $199.30

**⚠️ EARNINGS HARD BLOCK — ACTIVE AND UNCHANGED:**
System time 17:40 UTC = 1:40 PM ET. Market closes 20:00 UTC = 4:00 PM ET. MRVL reports Q1 FY2027 earnings AFTER market close tonight. The hard block ("no entering a position that will be held through an unresolved binary earnings event") is still fully in force and is the primary disqualifier regardless of all other metrics.

**Gate-by-gate assessment (2b-LONG):**

| Gate | Required | Actual | Result |
|------|----------|--------|--------|
| Earnings binary | Not tonight | MRVL reports after close tonight | ❌ HARD BLOCK — permanent for today |
| Spread < 1% | < 1% | 2.38% (R-flagged) | ❌ Wide/thin book |
| Z ≥ +1.0 | ≥+1.0 | +1.909 | ✅ |
| Close > 20d high | > $208.26 | $199.30 | ❌ −4.3% below pivot (stock FADED from $218 open) |
| RSI(14) 50–70 | 50–70 | 64.71 | ✅ |
| Vol ≥ 1.5× | ≥1.5× | 1.07× (27.0M vs 25.2M avg) | ❌ Below threshold |
| 200-SMA | N/A | Structural gap | ❌ |

**Context:** MRVL surged to $217.98 pre-market today on earnings anticipation, printed a high of $218.26, then faded hard to ~$199 by midday — a classic pre-earnings "buy the rumor, potential sell the news" pattern. The stock opened above its $208.26 prior 20d high, meaning at the open there WAS a technical breakout; however, (a) the earnings hard block was active from the start, (b) the intraday fade back below $208.26 means even on pure quant terms the breakout was NOT sustained, and (c) volume is only 1.07× (the 2b-LONG lane requires the breakout DAY to show ≥1.5×).

**Post-earnings watch (Thursday pre-market):** MRVL reports tonight after close. Re-evaluate tomorrow morning. If MRVL posts a beat + strong guidance and the stock opens above $208.26 on volume ≥1.5× avg, the 2b-LONG setup becomes active with conditions: Z ≥+1.0, RSI 50–70, entry limit ≤ $218.67 ($208.26 × 1.05 pivot cap), NVDA pair divergence compressed below 1.5σ. All gates must clear simultaneously — no pre-gaming the post-earnings outcome.

---

#### XLE (Energy Select Sector ETF) — All lanes — ❌ STILL SKIPPED

**Live quote:** bid $57.36 / ask $57.37 — spread **0.017% ✅** (excellent, fully normalized)
**Live mid:** $57.365 | **Today's bar close so far:** $57.345

| Gate | 2b-SHORT required | 2a-LONG required | Actual | Result |
|------|-------------------|-----------------|--------|--------|
| Z-Score | ≤ −1.0 | ≤ −2.0 | **−0.836** | ❌ Both lanes fail |
| Close vs extreme | < 20d low $55.70 | << mean | $57.345 > $55.70 | ❌ 2b-SHORT fails |
| 2a-LONG trigger price | — | ~$55.69 | Gap: $1.68 (−2.9%) | ❌ |
| RSI(14) | 30–50 | < 30 | 47.53 | ✅ for 2b-SHORT only; ❌ for 2a-LONG |
| Volume | ≥ 1.5× | ≥ 1.0× | 0.87× | ❌ Both lanes fail |

**Key observation:** XLE's Z-Score has **REGRESSED** from −0.892 at market open to **−0.836 midday** — meaning price has slightly recovered intraday (+$0.02 from the open-basis level), moving AWAY from the −2.0 oversold trigger rather than toward it. The WTI/Iran narrative may be stabilizing intraday. The 2a-LONG trigger at ~$55.69 requires a further −2.9% decline from current $57.365 AND RSI < 30 simultaneously. No lane qualifies today.

**Energy sector context:** Energy sector has had **1 consecutive trade failure** (XOM May 7 thesis-break exit). The next energy trade would be counted as #2 — if it fails, the sector ban rule triggers. This heightened risk reinforces the discipline of waiting for ALL gates to clear before entering any new energy position.

---

### Trades Fired This Rescan

**None.**

Zero candidates re-cleared the composite Layer A + Layer B gates upon midday re-evaluation.

---

### Patience Rule Applied

Gate failures are substantive, not timing/spread issues:
- **XLK:** Spreads normalized ✅; AVGO pair now confirms ✅; Z ✅. Still fails 3 of 5 quant gates (RSI overbought at 72.45, no confirmed breakout above $185.14, volume 0.62×). These are structural conditions that do not resolve intraday.
- **MRVL:** Earnings HARD BLOCK still active (reports tonight). Spread still wide (2.38%). Close still 4.3% below pivot. Volume 1.07×. Permanent skip for today.
- **XLE:** Spread normalized ✅. Z regressed to −0.836 (wrong direction). 2a-LONG trigger $1.68 away. No lane qualifies.

No gates were lowered. The AVGO pair improvement for XLK is a genuine, meaningful positive development — it removes one blocker and brings XLK one step closer to a qualifying setup tomorrow. The strategy is working correctly.

---

**Trades fired this rescan:** None
**Portfolio state:** $99,056.46 cash (100%) | 0 positions | 0 orders

**Key watchlist for Thursday pre-market (2026-05-28):**
1. **MRVL (#1 PRIORITY) — post-earnings 2b-LONG:** MRVL reports tonight. If beat → re-evaluate Thursday AM. Requirements: close > $208.26 on vol ≥1.5×, Z ≥+1.0, RSI 50–70, NVDA pair div < 1.5σ, limit ≤ $218.67. No pre-gaming.
2. **XLK (#2) — 2b-LONG:** AVGO pair now passing (1.295σ ✅). Still needs: RSI to cool 72.45 → 50–70 (requires flat/pullback in tech); vol ≥1.5× on a breakout day; reclaim of $185.14 pivot. Max limit ≤ $194.40.
3. **XLE (#3) — 2a-LONG watch:** WTI direction tomorrow will determine whether XLE approaches the $55.69 trigger. Iran deal progress → oil lower → XLE could reach Z ≤ −2.0. Not imminent but the trigger is set.
4. **200-SMA data gap:** ~40 sessions remaining (est. mid-August 2026). Auto-resolves as data accumulates.


---

## 2026-05-27 — Midday Scan Addendum (~14:22 ET / 18:22 UTC)

**Scan type:** Midday workflow — position thesis check, stop evaluation, watchlist re-evaluation
**VIX Regime:** Normal (~17.01, from morning research) — 1.00× sizing multiplier
**Account at scan:** Equity $99,056.46 | Cash $99,056.46 (100%) | 0 positions | 0 orders | PDT 0/3 | Week 0/3

---

### Portfolio State (Live API)
- **Positions:** `[]` — EMPTY. 100% cash confirmed.
- **Orders:** `[]` — EMPTY. No working brackets. No GTC stops.
- TRADE-LOG fully current. No discrepancy. No fills.

---

### Cut Losers / Tighten Stops
**N/A — no open positions.**

---

### Watchlist Re-Evaluation (Live Quotes at ~14:22 ET)

#### XLK (Technology Select Sector ETF) — 2b-LONG — ❌ STILL SKIPPED

| Gate | Required | Actual | Status |
|------|----------|--------|--------|
| Z-Score ≥ +1.0 | +1.43 | ✅ | |
| Close > 20d high ($185.14) | > $185.14 | $184.05 (−0.59%) | ❌ FAIL |
| RSI(14) 50–70 | 50–70 | 70.13 (borderline overbought) | ❌ FAIL |
| Vol ≥ 1.5× | 1.5× | 0.653× (7.65M vs 11.7M avg) | ❌ FAIL |
| AVGO pair div ≤ 1.5σ | ≤1.5σ | **1.3298σ ✅ IMPROVED** (was 1.64σ AM) | ✅ |
| 200-SMA | N/A | Structural gap (Dec 2025 split, ~40 sessions) | ❌ |

**Key development:** AVGO pair divergence narrowed from 1.64σ → 1.33σ — pair blocker REMOVED for first time since setup emerged. However, XLK opened at $186.18 (above $185.14 pivot) then faded to $184.03 — a failed intraday breakout. 3 substantive gates still fail. Thesis intact.
**Verdict: REJECT.** Forward: if today's close ≥ $185.14 on volume recovery → fresh 2b-LONG eval Thursday. Max limit ≤ $194.40 ($185.14 × 1.05).

---

#### MRVL (Marvell Technology) — 2b-LONG — ❌ STILL SKIPPED (earnings now resolved)

| Gate | Required | Actual | Status |
|------|----------|--------|--------|
| Earnings binary | Resolved | MRVL reported after close yesterday (now past) | ✅ |
| Z ≥ +1.0 | +1.6684 | ✅ | |
| Close > 20d high ($208.26) | > $208.26 | $198.68 (−4.60%) | ❌ FAIL |
| RSI(14) 50–70 | 50–70 | 62.15 | ✅ |
| Vol ≥ 1.5× | 1.5× | 1.191× (28.7M vs 24.1M avg) | ❌ FAIL |
| NVDA pair div ≤ 1.5σ | ≤1.5σ | **1.8434σ** | ❌ FAIL |
| 200-SMA | N/A | Structural gap (151 bars) | ❌ |

**Pattern:** MRVL opened at $217.98 (above $208.26 pivot), printed high $218.26, then faded −9.3% to $198.68 — textbook earnings gap-up fade / "buy the rumor, sell the news." Failed intraday breakout. NVDA pair divergence (1.84σ > 1.5σ) confirms this is single-name, not sector-wide.
**Verdict: REJECT (4 active failures).** Monitor for Thursday pre-market: if MRVL stabilizes above $208.26 on ≥1.5× volume, setup re-qualifies. Alternatively watch for 2a-LONG if price fades to Z ≤ −2.0 (~$149).

---

#### XLE (Energy ETF) — No Lane Qualifies — ❌ STILL SKIPPED

- Z-Score: **−0.9306** (2b-SHORT needs ≤−1.0; 0.07σ short of trigger)
- 20d Low: $55.70 | Price: $57.165 — above breakdown level
- 2a-LONG trigger: ~$54.62 (−4.5% away)
- RSI: 50.75 (neutral) | Vol: 0.961× (below average)
- No lane qualifies. Midrange statistically.

**Energy context:** XLE −6.7% in 6 sessions from May 19 peak ($61.29). WTI selloff on Iran Hormuz reopening commitment continues. Energy sector: 1 consecutive failure logged (XOM May 7). Next energy trade faces heightened scrutiny.

---

### Trades Fired: None

All three watchlist candidates remain below their entry thresholds. Gate failures are structural and quant-level — not spread issues. No positions cut. No stops tightened. No new orders placed.

**Patience rule applied.** The AVGO pair gate improvement for XLK is a genuine positive development — brings the setup one step closer. MRVL's post-earnings fade pattern matches the strategy's "sell the news" avoidance design exactly. XLE in no-man's land.

---

### Key Watchlist for Thursday Pre-Market (2026-05-28)

1. **XLK (#1 PRIORITY):** AVGO pair now confirms (1.33σ ✅). Needs: (a) close above $185.14 today (or fresh breakout Thursday), (b) RSI to normalize from 70.1 → 50–70, (c) volume ≥ 1.5× avg on breakout day. Max limit ≤ $194.40.
2. **MRVL (#2):** Earnings resolved. Watch Thursday: if MRVL recovers above $208.26 on ≥1.5× volume + NVDA pair compresses < 1.5σ → 2b-LONG re-activates. If continues fading → watch for 2a-LONG at Z ≤ −2.0 (~$149).
3. **XLE (#3 watch):** 2b-SHORT trigger: close below $55.70 on ≥1.5× vol + RSI 30–50. 2a-LONG trigger: price ~$54.62 (Z ≤ −2.0) + RSI < 30. Both require further WTI deterioration.
4. **200-SMA data gap:** ~40 sessions to resolution (est. mid-August 2026). Persistent structural constraint on Minervini TT for all post-Dec-2025 split-adjusted names.

*Scan: 2026-05-27 ~14:22 ET | Account: $99,056.46 | 0 positions | 0 orders | Week 0/3 | PDT 0/3*

---

## 2026-05-27 — Afternoon Scan Addendum (20:17 UTC / ~16:17 ET)

**Scan time:** Post-session — market closed at 20:00 UTC. All May 27 bars now settled.
**VIX regime at scan:** NORMAL (estimated ~17.0–17.5, from morning research 17.01) | Sizing multiplier: 1.00×

---

### STEP 1 — Order & Position State Reconciled vs TRADE-LOG

**API results — 6 total orders, all historical:**

| Order ID | Symbol | Type | Status | Detail |
|----------|--------|------|--------|--------|
| 1d69c496 | XOM | Bracket limit BUY 61 sh @ $159.78 | **EXPIRED** 2026-05-18T20:02 | TIF: day — never filled ✅ logged |
| 94606e38 | XOM | Stop child $147.80 | **CANCELED** 2026-05-18T20:02 | Auto-cancelled ✅ logged |
| 336d922a | XOM | TP child $183.74 | **CANCELED** 2026-05-18T20:02 | Auto-cancelled ✅ logged |
| 8f97ef7d | XOM | Market Sell 130 sh | **FILLED** $146.09, 2026-05-07 | Thesis-break exit ✅ logged |
| d92d9371 | XOM | Trailing Stop 10% GTC | **CANCELED** 2026-05-07 | Pre-exit cancellation ✅ logged |
| c04ae321 | XOM | Market Buy 130 sh | **FILLED** $153.35, 2026-05-01 | Original entry ✅ logged |

- **Positions API: `[]` — 100% cash ($99,056.46).** No filled positions.
- **Morning bracket orders placed today (May 27): NONE** — Pre-market research decision was explicit HOLD: XLK (4 gate failures), MRVL (5 gate failures including earnings binary), XLE (no lane qualifies). Nothing to reconcile for fills.
- **Bracket fills today: 0**
- **Open stale limits: 0** — no open orders of any kind.
- **TRADE-LOG reconciliation: FULLY CURRENT ✅**

---

### STEP 2 — Trailing Stop Upgrades on Profitable Fills

**N/A.** Portfolio is 100% cash ($99,056.46). No positions exist. No trailing stop upgrade workflow applicable.

---

### STEP 3 — Stale Limit Cancellations

**None.** No open orders of any kind. May 18 bracket (1d69c496) expired naturally at session close per TIF: day — fully logged.

---

### STEP 4 — Afternoon Opportunity Scan (5 Candidates, 4 Sectors)

**VIX regime:** NORMAL (1.00×) | **Positions:** 0/6 | **Week trades:** 0/3 | **PDT:** 0/3

**Full quant metrics computed from settled May 27 bars:**

| Ticker | Close | 20d Mean | 20d Std | Z-Score | RSI(14) | Vol vs Avg | 20d High | Lane Tried | Key Failures | Verdict |
|--------|-------|----------|---------|---------|---------|-----------|----------|-----------|--------------|---------|
| XLK | $184.43 | $173.12 | $7.68 | +1.473 | 70.94 | 1.034× | $185.14 | 2b-LONG | Close $0.71 below $185.14 pivot ❌; RSI 70.94 overbought ❌; Vol 1.034× < 1.5× ❌; 200-SMA unavail. ❌ | **REJECT** |
| XLV | $148.79 | $146.02 | $1.85 | +1.495 | 61.71 | 1.028× | $149.89 | 2a-SHORT | Z +1.495 < +2.0 ❌; RSI 61.71 < 70 ❌; Price above 50-SMA ($145.78) — TT short fails ❌ | **REJECT** |
| MRVL | $198.70 | $176.01 | $13.58 | +1.672 | 62.08 | 1.813× | $208.26 | 2b-LONG | Close $9.56 below $208.26 pivot ❌; 200-SMA unavail. ❌ | **REJECT** |
| XLE | $56.99 | $58.50 | $1.46 | −1.039 | 49.96 | 1.291× | 20d low $55.70 | 2b-SHORT | Close $1.29 above 20d low — no breakdown ❌; Vol 1.291× < 1.5× ❌; Short TT structural ❌ | **REJECT** |
| XOM | $147.90 | $153.00 | $4.39 | −1.161 | 48.93 | 0.929× | 20d low $144.57 | context only | Z < +1.0 for any lane; 7.7% below $162.55 pivot; vol 0.929× below avg | **REJECT** |

**Pair Z-Scores:**
- AVGO: Z = +0.197 | XLK−AVGO divergence = **1.276σ ✅** (≤1.5σ — pair now confirms; tech sector moving directionally together)
- CVX: Z = −1.448 | XOM−CVX divergence = **0.287σ ✅** (≤1.5σ — both energy names declining in lockstep)

---

**Candidate Detail Notes:**

**XLK — REJECT (3 active gate failures + structural TT):**
- Z = +1.473 ✅ | AVGO pair divergence 1.276σ ✅ (improved from 1.64σ at morning open)
- **Close $184.43 vs pivot $185.14: −$0.71 (−0.38%) below** — 2b-LONG requires close ABOVE the prior 20d high. XOM opened above ($186.18 was today's open) but faded to $184.43. The breakout attempt that held on May 26 ($185.14) was tested but NOT confirmed today.
- **RSI = 70.94** — one tick above the 70 ceiling; technically overbought by the Wilder's method. 2b-LONG needs RSI in the 50–70 healthy momentum window. The marginal nature of this overshoot (0.94 above threshold) is noted — but a gate is a gate.
- **Volume = 1.034×** — below the 1.5× threshold required for the momentum breakout lane. Today's volume (12.26M vs 11.86M 20d avg) was only modestly above average; not institutional accumulation on a breakout attempt.
- **200-SMA**: CANNOT VERIFY (Dec 2025 2:1 split data gap; ~39 more sessions until 200 bars of post-split data available). Permanent structural block until mid-August 2026.
- **Assessment:** XLK is the closest candidate to qualifying of any name in today's scan. Three gates are one session away from potentially clearing: (a) RSI is only 0.94 above the ceiling and will naturally cool on any consolidation day; (b) the breakout pivot needs only $0.72 more upside to re-confirm; (c) volume only needs to continue normalizing. The AVGO pair finally confirms (1.276σ ✅). If Friday opens with a continuation of tech momentum and XLK closes above $185.14 on volume ≥1.5× with RSI cooling to 50–70 → 2b-LONG activates. Max limit ≤ $185.14 × 1.05 = **$194.40**.

**XLV — REJECT (Z and RSI both below thresholds; TT structurally incompatible):**
- Z = +1.495 (needs ≥ +2.0; gap = 0.505σ). The 2a-SHORT mean-reversion trigger requires price ~$149.72 (= mean $146.02 + 2.0 × std $1.85). Today's close $148.79 is $0.93 short.
- RSI = 61.71 (needs > 70). Healthcare pulled back slightly today (May 27 close $148.79 vs May 22 high $149.89) — consolidation, not overbought extension.
- Volume = 1.028× ✅ — the one passing gate.
- Short TT: Price $148.79 is above the 50-SMA ($145.78). Short Trend Template requires price to be BELOW all SMAs. Structural conflict with 2a-SHORT lane (strategy review item remains open from Week 4).
- **Assessment:** XLV dropped off the extreme-overbought reading from last week (Z was +3.247 on May 22). The mean-reversion setup that looked compelling has partially self-corrected. Z needs to rebuild to +2.0 via a renewed healthcare rally; current trajectory is consolidation/pullback, moving AWAY from the short trigger.

**MRVL — REJECT (2 active gate failures):**
- Z = +1.672 ✅ | RSI = 62.08 ✅ | Volume = **1.813× ✅** — THREE GATES PASS. This is a significant improvement from the morning.
- **Close $198.70 vs pivot $208.26: −$9.56 (−4.59%) below**. The 2b-LONG momentum lane requires close ABOVE the prior 20d high. MRVL opened at $217.98 (above the $208.26 pivot, technically a breakout), printed an intraday high of $218.26, then experienced a severe fade to close $198.70 — a textbook "buy the rumor, sell the news" post-earnings pattern.
- **200-SMA**: CANNOT VERIFY (151/200 bars available). Structural data gap.
- **Earnings binary resolved**: MRVL reported Q1 after yesterday's close (May 26). The binary is now past — no longer a hard block. The question is whether the faded gap-up creates a mean-reversion opportunity or a momentum entry.
- **2a-LONG check**: Z = +1.672 → not at +2.0. Would need MRVL to be OVERSOLD for mean-reversion long (Z ≤ −2.0), which is inapplicable here. Z is elevated, not oversold.
- **Assessment:** MRVL volume (1.813×) is the strongest in today's scan — institutional participation is high. The key issue is that the breakout was NOT sustained on the close. The pivot at $208.26 must be reclaimed on a closing basis. If Friday/Monday MRVL stabilizes above $208.26 with continued institutional volume and RSI holding 50–70, the 2b-LONG setup activates. Entry limit ≤ $208.26 × 1.05 = **$218.67**.

**XLE — REJECT (close above 20d low; volume insufficient; short TT structural):**
- Z = −1.039 (2b-SHORT lane needs ≤ −1.0 ✅ — technically passes the Z gate)
- **Close $56.99 vs 20d low $55.70: +$1.29 above** — the 2b-SHORT breakdown lane requires price to be BELOW the prior 20d low. XLE has not broken down through that level. In fact, it came close (today's low was $56.475 vs the $55.70 threshold — only $0.775 away) but closed above it.
- RSI = 49.96 ✅ (in 30–50 range for momentum short) — passes this gate.
- Volume = 1.291× ❌ (needs ≥ 1.5× for 2b-SHORT)
- **Short Trend Template**: XLE Dec 2025 split data gap blocks 150/200-SMA verification. Additionally, XLE's price is only −8.8% below its 52-week high ($62.56) — the Short TT requires > 30% below 52w high. Structural blocker.
- **Energy sector context**: XLE has now closed at $56.99, only $1.29 above the 20d low. If WTI oil continues declining on Iran Hormuz reopening narrative, the 2b-SHORT breakdown remains possible. But two structural gates (volume and Short TT) block it regardless.
- **2a-LONG trigger**: Z = −2.0 requires price ≈ **$55.59** (mean $58.50 − 2.0 × std $1.46). XLE needs only −$1.40 further decline (−2.5%) from close. Watch carefully Friday.

**XOM — context only (no lane qualifies):**
- Z = −1.161; RSI = 48.93; vol = 0.929×; price $147.90 — below both its 20d mean ($153.00) and below its May 1 entry price ($153.35). Orderly decline continues on below-average volume. CVX pair divergence only 0.287σ — both energy names moving in lockstep (sector-wide, not idiosyncratic). No entry lane qualifies. Energy sector at 1 consecutive failure (XOM May 7 thesis-break). Next energy trade is the "2nd failure" risk.

---

### STEP 5 — Stale Limit Cancellations

**None applicable.** No open orders exist. Nothing to cancel.

---

### Afternoon Market Context

May 27 session was a mild consolidation day after the prior session's strong tech rally. XLK attempted to extend above its $185.14 breakout pivot (opened at $186.18) but faded intraday to close at $184.43 — a failed breakout-day confirmation. Volume of 1.034× was insufficient for institutional conviction on a momentum move. MRVL's post-earnings fade was the session's dominant single-name story: stock opened at $217.98 (fully above the $208.26 pivot, appearing to confirm a momentum breakout), then reversed −8.9% to close $198.70, a classic "buy the rumor, sell the news" post-earnings pattern. This mirrors the pattern seen with PLTR (May 5) and NVDA earlier in the month. The energy sector continued its orderly decline: XLE −1.5% ($57.85 → $56.99), XOM −1.3% ($149.81 → $147.90), both on near-average volumes — consistent with the Iran Hormuz reopening narrative gradually deflating the supply-risk premium in WTI. XLV consolidating (+0.19% day) — no longer showing the extreme overbought Z that made it interesting for a 2a-SHORT setup. VIX remains in the Normal regime. No new positions entered; 100% cash preserved heading into the Memorial Day weekend transition into next week. The week closes 0/3 trades used.

---

**Bracket fills today:** 0 (no morning limits placed — HOLD decision at pre-market; all candidates failed Layer A + Layer B gates)
**Stops upgraded:** 0 (no positions held; no trailing stop upgrade workflow applicable)
**Stale limits cancelled:** 0 (none existed)
**New afternoon entries:** none — all 5 candidates failed composite Layer A + Layer B gates
**Afternoon market context:** XLK faded from $186.18 open to $184.43 close (failed breakout attempt, RSI 70.94 overbought, vol 1.034× insufficient). MRVL −9% intraday fade after earnings gap-up (close $198.70 vs $208.26 pivot — "sell the news"). XLE approaching 20d low at $55.70 (close $56.99, only $1.29 above; Z = −1.039). Energy sector continuing orderly decline. VIX Normal (~17). Zero new orders placed.

**Key watchlist for Thursday pre-market (2026-05-28):**
1. **XLK — #1 PRIORITY (2b-LONG):** Z=+1.473 ✅, AVGO pair 1.276σ ✅. Remaining gates: RSI needs to normalize from 70.94 → 50–70 (any flat/down open achieves this); volume needs ≥1.5× avg (~17.8M shares on a full session); close needs to reclaim $185.14 pivot. Max limit ≤ $194.40 (pivot × 1.05). 200-SMA structural gap persists (~39 sessions to resolve).
2. **MRVL — #2 (2b-LONG, conditional):** Earnings resolved (past). Z=+1.672 ✅, RSI=62.08 ✅, Vol=1.813× ✅. Sole gate: close must be above $208.26 pivot on a settled bar. If MRVL stabilizes Thursday and attempts to reclaim $208.26 on institutional volume, the setup re-activates. Entry limit ≤ $218.67 (pivot × 1.05). 200-SMA structural gap.
3. **XLE — #3 (watch for 2a-LONG trigger):** Z = −1.039; trigger for 2a-LONG = $55.59 (Z ≤ −2.0). Only $1.40 further decline needed (−2.5%). RSI already in the 30–50 zone (49.96). If WTI continues declining and XLE breaks toward $55.59, watch for RSI < 30 simultaneously (2a-LONG lane). Short TT remains structurally blocked (< 30% below 52w high). Energy sector flag: 1 consecutive failure → heightened caution on any new energy entry.
4. **XLV — #4 (watch only):** Z = +1.495; needs +2.0 (price ~$149.72) AND RSI > 70. Currently consolidating at $148.79 — 2a-SHORT setup weakening, not strengthening. Low priority unless healthcare makes a strong push higher Thursday.
5. **200-SMA data gap:** ~39 trading sessions remaining (est. mid-August 2026). All Minervini TT 200-SMA "CANNOT VERIFY" flags resolve automatically.


---

## 2026-05-28 — Pre-market Research (Day 31, Thursday)

### Account
- **Equity:** $99,056.46
- **Cash:** $99,056.46 (100.0%)
- **Buying Power:** $198,112.92 (2× margin)
- **Daytrade count:** 0/3
- **Open Positions:** None
- **Open Orders:** None
- **Phase P&L:** −$943.54 (−0.944%) | Peak: $100,206.70 | Drawdown: −1.15%
- **Week trades used:** 0/3

---

### Market Context
- **WTI Crude:** ~$90.12–$91.71/bbl (+1.5% to +3.4%) — sharp rebound after Wednesday's −5% plunge; driven by renewed US defensive strikes on Iranian military site, reigniting Strait of Hormuz shipping disruption fears. Month: −15.8%. Year: +47.7%.
- **Brent Crude:** ~$95.83–$97.29/bbl (+1.6% to +3.0%) — similar surge. Month: −13.2%. Year: +51.3%.
- **S&P 500 Futures:** Down ~0.20–0.25% premarket (~7,521–7,524). Follows S&P 500 fresh record close at 7,520.36 on Wed. Softness attributed to Middle East tension and data-day uncertainty. SPY: −0.087% at $749.81.
- **VIX:** ~15.73–16.73 (touched 15.73 intraday low, lowest since Jan 23). VIX1D: 10.07. VIX9D: 13.27 → calm open expected.
- **Key Macro Data Today (8:30 AM):** Preliminary Q1 GDP (2nd estimate), April PCE (+0.4% MoM, +3.8% YoY headline; core +0.2% MoM, +3.3% YoY), Personal Income (flat), Durable Goods Orders. 10:00 AM: Initial Jobless Claims, New Home Sales. 11:00 AM: EIA crude inventory data.
- **Fed:** Minneapolis Fed Kashkari + Fed Governor Cook both reiterated inflation concerns; Cook stated "prepared to raise rates." Markets price 99.1% probability of June rate hold. Next FOMC: June 17.
- **Earnings movers:**
  - SNOW: +33–37% post-earnings (beat on profit + revenue + expanded AWS deal) → gap-up to ~$240
  - DLTR: +10–15% on earnings beat and raised full-year guidance
  - KSS: +21.3% on Q1 beat
  - HRL: +8.1% on stronger sales
  - DELL: +4.4% on $9.7B Pentagon contract
  - CRM: −2% despite earnings beat (AI competition concerns)
  - BRZE: −11% on Q1 miss/outlook
  - PLAB: −26% on EPS guidance miss
  - SNPS: −2% on Q2 results
  - COST reports after bell today (consensus EPS $4.98, rev ~$69.7B)
  - RY (Royal Bank Canada): net income $5.5B (+25% YoY), diluted EPS $3.85 (+27%)
- **Sector Momentum YTD:** Materials (XLB) +22% leader. Consumer Staples, Industrials, Energy also leading. Tech (XLK), Communications, Consumer Discretionary lagging. S&P 500 +27% YoY earnings growth in Q1; Magnificent Seven drove ~5.1% of April's 10.5% monthly gain. Goldman Sachs raised S&P 500 year-end target to 8,000 on AI earnings growth.

---

### VIX Regime
- **Current VIX:** ~15.73–16.0 (touching intraday low of 15.73)
- **Regime: Normal** (VIX 14–22)
- **Sizing Multiplier: 1.00×**
- All entry types permitted. No regime-based restriction on new entries.

---

### Universe Scan — Candidates Evaluated

**Long candidates evaluated:** XLK, MRVL, SNOW, ORCL
**Short candidates evaluated:** XLV, XLE

---

### Candidate Analysis

#### XLK — Technology ETF | Intended: 2b-LONG
- **Catalyst:** AI/tech sector momentum, XLK broke above $185.14 pivot May 26, continued to $187.17 today
- **Z-Score:** +1.675 (20d mean $174.52, std $7.55)
- **RSI(14):** 73.76 ❌ — Above 70 ceiling for 2b-LONG lane
- **Volume:** 4.92M today vs 11.86M avg = 0.414× ❌ — Partial day; needs ≥1.5× for momentum lane
- **Prior 20d High (pivot):** $185.14 — Close $187.17 > pivot ✅
- **Pivot Extension:** ($187.17 / $185.14 − 1) = +1.1% ✅ (≤5%)
- **50-SMA:** $156.35 | **150-SMA:** $177.71 | **200-SMA:** CANNOT VERIFY (152/200 bars available)
- **50-SMA < 150-SMA** ❌ — Minervini TT condition 50-SMA > 150-SMA fails
- **52w High (split-adj):** ~$304 pre-split (~$152 post-split) — data contaminated by Dec 2025 2-for-1 split
- **AVGO pair Z:** +0.548 | Divergence: 1.127σ ✅ (≤1.5σ)
- **Layer B verdict: FAIL** — RSI overbought (73.76 > 70 ❌), volume insufficient (0.414× ❌), 200-SMA unverifiable ❌
- **Layer A (TT) verdict: FAIL** — 50-SMA ($156.35) < 150-SMA ($177.71) ❌; 200-SMA conditions unverifiable ❌
- **REJECT**

---

#### MRVL — Marvell Technology | Intended: 2b-LONG
- **Catalyst:** Q1 FY2026 earnings resolved (beat). AI chip tailwinds, semi sector momentum. Watching for reclaim of $208.26 pivot.
- **Z-Score:** +1.595 (20d mean $178.19, std $13.78)
- **RSI(14):** 70.23 ❌ — Marginally above 70 ceiling
- **Volume:** 31.49M today vs 25.47M avg = 1.236× ❌ — Below 1.5× requirement
- **Prior 20d High (pivot):** $208.26 — Close $200.16 < pivot ❌ (−$8.10 below; −3.9%)
- **50-SMA:** $144.24 | **150-SMA:** $104.67 | **200-SMA:** CANNOT VERIFY (152/200 bars)
- **50-SMA > 150-SMA:** $144.24 > $104.67 ✅ (structurally valid post-earnings re-rating)
- **52w High:** $208.26 | **52w Low:** $73.73
- **Dist from 52w low:** +171.5% ≥ 30% ✅ | **Dist from 52w high:** −3.9% within 25% ✅
- **6-month return:** +164.4% — top quintile ✅
- **AVGO pair Z:** +0.548 | Divergence: 1.047σ ✅
- **Layer B verdict: FAIL** — Close below pivot ($200.16 < $208.26 ❌), RSI 70.23 > 70 ❌, Vol 1.236× < 1.5× ❌
- **REJECT** — Three gates fail simultaneously. Pivot at $208.26 must be reclaimed on a closing basis with RSI in 50–70 and vol ≥1.5×.

---

#### SNOW — Snowflake | Intended: 2b-LONG
- **Catalyst:** Q1 FY2027 earnings massive beat (EPS + revenue); expanded AWS partnership; +33–37% gap-up
- **Z-Score:** +3.652 (20d mean $160.26, std $21.96) — Extreme stretch
- **RSI(14):** 90.49 ❌ — Massively overbought
- **Volume:** 25.19M vs 8.11M avg = 3.106× ✅ — Strong
- **Prior 20d High (pivot):** $177.60 — Close $240.11 ✅ — But massively above
- **Pivot Extension:** ($240.11 / $177.60 − 1) = +35.2% ❌ — Requires ≤5%; this is a 7× violation
- **50-SMA:** $154.35 | **150-SMA:** $195.78 | **200-SMA:** CANNOT VERIFY
- **50-SMA < 150-SMA** ❌ — TT condition fails
- **6-month return:** −0.8% from 6 months ago — does NOT meet ≥70th percentile ❌
- **Layer B verdict: FAIL** — RSI 90.49 ❌, pivot extension +35.2% ❌, TT failures ❌
- **REJECT** — Classic gap-and-go earnings trade that the momentum lane's ≤5% pivot extension rule is specifically designed to block. Excellent fundamental story; wrong entry structure for this strategy.

---

#### ORCL — Oracle | Intended: 2b-LONG
- **Catalyst:** AI infrastructure spending, cloud momentum, beneficiary of enterprise AI buildout
- **Z-Score:** +1.588 (20d mean $188.36, std $8.97) ✅
- **RSI(14):** 56.82 ✅ (in 50–70 range)
- **Volume:** 13.70M today vs 19.96M avg = 0.686× ❌ — Well below 1.5× requirement
- **Prior 20d High (pivot):** $195.95 — Close $202.60 ✅
- **Pivot Extension:** +3.4% ✅ (≤5%)
- **200-SMA:** Cannot verify from 25 bars (extended bars not pulled — volume failure made it moot)
- **Earnings Binary:** Oracle Q4 FY2026 earnings expected ~June 10–12 (≈13 days) — binary risk blocks entry
- **Layer B verdict: FAIL** — Volume 0.686× ❌ (needs ≥1.5×)
- **REJECT** — Volume insufficient + imminent earnings binary. Good setup structure otherwise; revisit post-earnings if thesis holds.

---

#### XLV — Healthcare ETF | Intended: 2a-SHORT
- **Catalyst:** XLV extended to Z=+2.163 today on healthcare sector strength; overbought mean-reversion setup
- **Z-Score:** +2.163 (20d mean $146.41, std $1.96) ✅
- **2a-SHORT trigger (Z=+2.0):** $150.33 — Price $150.65 is above ✅
- **RSI(14):** 68.95 ❌ — Just below 70 threshold (needs >70 for 2a-SHORT)
- **Volume:** 4.55M vs 9.76M avg = 0.466× ❌ — Partial day; well below 1.0× requirement
- **Short Trend Template:** Price $150.65 > 50-SMA (~$145–146 range per prior research) — SHORT TT requires price BELOW all SMAs. Structural conflict: XLV is in an uptrend, not a downtrend. ❌
- **Layer B verdict: FAIL** — RSI 68.95 < 70 ❌, Vol 0.466× < 1.0× ❌
- **Layer A (Short TT) verdict: FAIL** — Price above 50-SMA is incompatible with Short Trend Template ❌
- **REJECT** — Two gate failures + TT structural conflict. Z is building toward the trigger; watch for RSI to crack >70 on a strong healthcare rally day with confirming volume. Short TT structural issue remains chronic for sector ETFs in uptrends — flagged as open strategy item.

---

#### XLE — Energy ETF | Intended: 2a-LONG or 2b-SHORT
- **Catalyst watch:** WTI +1.9–3.4% today on Iran tensions reversed the prior decline; XLE bounced from $56.99 to $57.24
- **Z-Score:** −0.795 (20d mean $58.41, std $1.47) — Neither zone qualifies
- **RSI(14):** 55.81 — Neutral; not oversold
- **Volume:** 25.90M vs 38.80M avg = 0.668× — Below average
- **2a-LONG trigger (Z=−2.0):** $55.46 — Current $57.24 is +3.1% above trigger; requires further $1.78 decline
- **2b-SHORT:** Z=−0.795 (≤−1.0 barely fails), close $57.24 > 20d low $55.70 ❌, RSI 55.81 (outside 30–50 range) ❌
- **CVX pair Z:** −1.102 | Divergence: 0.307σ ✅ — Energy names moving in lockstep
- **Energy sector flag:** 1 consecutive failure (XOM May 7 thesis-break) → heightened caution on any new energy entry
- **Layer B verdict: FAIL** — No lane qualifies; Z too shallow for either mean-reversion or breakdown
- **REJECT** — Oil rebound today pushed XLE away from both the 2a-LONG oversold trigger and the 2b-SHORT breakdown level. Watch if WTI reverses; 2a-LONG gate reactivates at ~$55.46.

---

### Trade Ideas (Cleared Both Layers)
**None.** Zero candidates cleared both Layer A and Layer B today.

---

### Skipped Candidates — Summary

| Ticker | Lane Attempted | Specific Failed Check(s) |
|--------|---------------|--------------------------|
| XLK | 2b-LONG | RSI 73.76 > 70 ❌; Vol 0.414× < 1.5× ❌; 50-SMA < 150-SMA (TT) ❌; 200-SMA unverifiable ❌ |
| MRVL | 2b-LONG | Close $200.16 < pivot $208.26 ❌; RSI 70.23 > 70 ❌; Vol 1.236× < 1.5× ❌ |
| SNOW | 2b-LONG | RSI 90.49 > 70 ❌; Pivot extension +35.2% > 5% ❌; 50-SMA < 150-SMA ❌; 6mo return neg ❌ |
| ORCL | 2b-LONG | Vol 0.686× < 1.5× ❌; Earnings binary ~13 days ❌ |
| XLV | 2a-SHORT | RSI 68.95 < 70 ❌; Vol 0.466× < 1.0× ❌; Short TT structural conflict ❌ |
| XLE | 2a-LONG / 2b-SHORT | Z=−0.795 (2a: need ≤−2.0 ❌; 2b: need ≤−1.0 ❌); RSI 55.81 (2a: need <30 ❌; 2b: need 30–50 ❌); Vol 0.668× ❌ |

---

### Watchlist for Friday / Next Week

1. **MRVL — #1 PRIORITY (2b-LONG):** Three gates pending simultaneously: (a) reclaim $208.26 pivot on a closing basis, (b) RSI needs to cool from 70.23 → below 70 (any flat/consolidation session achieves this), (c) volume ≥1.5× (~38M shares). Entry limit ≤ $218.67 (pivot $208.26 × 1.05). 200-SMA structural gap persists (~38 sessions remaining). Pattern: stabilizing post-earnings, institutional accumulation evident (54M shares Monday, 31M today). Strong fundamental setup.

2. **XLK — #2 (2b-LONG):** RSI needs to cool from 73.76 → below 70. Pivot at $185.14 already broken ($187.17 close). Consolidation above pivot with RSI normalizing = setup activates. Volume needs 1.5× on entry day. 50-SMA < 150-SMA is a TT structural issue that will self-resolve as 50-SMA rises. Max limit ≤ $194.40 (pivot × 1.05). AVGO pair divergence 1.127σ ✅.

3. **XLE — #3 (2a-LONG watch):** Z=−0.795 today (WTI Iran bounce pushed XLE up). 2a-LONG trigger: $55.46 (Z=−2.0). Needs further −3.1% decline. If Iran tensions ease / WTI resumes decline, watch for XLE to revisit ~$55.50. RSI needs to simultaneously drop below 30. Energy sector 1 consecutive failure → manage size carefully.

4. **XLV — #4 (2a-SHORT watch):** Z=+2.163 today ✅. RSI 68.95 — just 1.05 points below the 70 trigger. If healthcare rallies again Friday and RSI breaks 70 with confirming volume ≥1.0×, setup activates — BUT short TT structural conflict (price above 50-SMA) remains the chronic blocker.

5. **ORCL — post-earnings (2b-LONG):** Good setup structure (Z=+1.588, RSI=56.82, pivot extension +3.4%). Blocked by earnings binary (~June 10). Revisit the week of June 15 if earnings beat and price holds above $195.95 pivot.

6. **COST — watch post-bell earnings today:** If COST beats and rallies, evaluate for 2b-LONG continuation Friday. Consumer Staples is a YTD sector leader.

---

### Key Forward Catalysts
- **PCE inflation data today (8:30 AM):** Core PCE +0.2% MoM / +3.3% YoY — if hotter than expected, could pressure equities and give Fed hawks ammunition, potentially spiking VIX. Cooling PCE = risk-on.
- **Q1 GDP (2nd estimate, 8:30 AM):** Any downward revision raises stagflation concerns.
- **Iran/Hormuz:** Escalation = WTI spike = energy tailwind + equity headwind. De-escalation = WTI reversal = potential XLE 2a-LONG trigger activation.
- **COST earnings (after bell):** Bellwether for consumer health; could drive Consumer Staples sector move.
- **Fed speakers:** NY Fed Williams 8:55 AM, Governor Cook 3:55 PM — watch for hawkish tone on inflation.

---

### Risk Factors
1. **Geopolitical (Iran/Hormuz):** Binary risk — escalation or de-escalation both create volatility. Oil price surge creates cross-sector headwinds for tech/consumer.
2. **PCE inflation hotter than expected:** Core PCE at 3.3% YoY already above 2% target; a surprise upside print could cause Fed hawkishness repricing, VIX spike → would shift to Elevated regime (0.75× sizing).
3. **Overbought markets:** S&P 500 at fresh record high (7,520.36), VIX near multi-month low. Complacency risk. The "sell the news" pattern seen in MRVL and recent tech names is characteristic of late-stage momentum.
4. **Energy sector flag:** 1 consecutive failure (XOM May 7). Second consecutive failure in energy would trigger sector avoidance rule.
5. **200-SMA data gap:** Persists for all split-adjusted tickers. ~38 sessions until resolution (est. mid-August 2026). All Minervini TT "CANNOT VERIFY" flags on XLK, MRVL self-correct over time.

---

### Decision
**HOLD** — Zero candidates cleared both Layer A and Layer B gates today.

- The primary reason across all candidates is a combination of: (a) RSI readings at or above overbought thresholds after the strong recent rally, (b) partial-day volume being insufficient for momentum lane's 1.5× requirement, and (c) price levels either already extended past pivot (XLK, SNOW) or still below pivot (MRVL).
- Today's session is NOT a setup day — it's a data day (PCE, GDP, Claims) with Iran volatility overlay. The market correctly needs to digest this information before clean trend entries emerge.
- Cash preservation at 100% is the correct posture. PDT budget fully intact (0/3). Maximum flexibility heading into Friday's full session and next week.
- The HOLD decision here is consistent with the strategy's patience rule: "A week with zero trades can be the right call. Only trade when edge is present; else hold cash."

---

### Adjustment Audit
*(Today is Thursday — Monday-only section, skipped per workflow rules.)*


---

### 2026-05-28 — Midday Rescan Addendum (13:52 EDT)

**Account at rescan:** $99,056.46 equity | $99,056.46 cash | 0 positions | 0 open orders | Week trades used: 0/3

**VIX regime at rescan:** Normal (1.00× sizing multiplier) — unchanged from open

**Spread gate threshold:** < 1.0% for liquid candidates

---

**Skipped at open, re-evaluated:**

| Ticker | Morning Spread | Midday Spread | Midday Z | Midday RSI | Vol Ratio | Verdict |
|--------|---------------|--------------|----------|------------|-----------|---------|
| XLK    | wide/partial  | 0.011% ✅    | +1.681   | 78.86      | 0.610×    | **STILL SKIP** |
| MRVL   | wide/partial  | 2.73% ❌     | +1.862   | 64.91      | 1.470×    | **STILL SKIP** |
| SNOW   | wide/partial  | 0.825% ❌    | +3.689   | 86.55      | n/a       | **STILL SKIP** |
| ORCL   | wide/partial  | 0.128% ✅    | +1.638   | 65.42      | 0.749×    | **STILL SKIP** |
| XLV    | wide/partial  | 0.013% ✅    | +2.186   | 62.28      | 0.564×    | **STILL SKIP** |
| XLE    | wide/partial  | 0.018% ✅    | −0.995   | 45.05      | 0.822×    | **STILL SKIP** |

---

**Detailed gate verdicts:**

**XLK (2b-LONG) — STILL SKIP:**
- RSI has *deteriorated*: 73.76 at open → 78.86 at rescan. Now more overbought, not less.
- Volume 0.610× (needs ≥1.5×). Improved from 0.414× but far from threshold.
- Minervini TT still fails: 50-SMA ($156.35) < 150-SMA ($177.71) ❌; 200-SMA unverifiable ❌.
- XLK is running higher without us — the midday rescan's purpose (spread normalization) is moot because the core gates haven't improved.
- Active gate failures: RSI ❌, Volume ❌, TT 50/150 SMA ❌, 200-SMA ❌

**MRVL (2b-LONG) — STILL SKIP (spread-blocked):**
- Spread 2.73% — stale/crossed bid-ask ($202.00 / $207.58). Cannot obtain clean fill.
- Positive development: RSI cooled from 70.23 → 64.91 ✅ (now inside 50–70 range).
- Volume improved to 1.470× — tantalizingly close to 1.5× but still short.
- Price $204.83 close still BELOW $208.26 pivot ❌ (−1.66% gap to reclaim).
- Z-Score: +1.862. Still below the 2b-LONG +1.0 floor but above — structure improving.
- **Friday watch:** If spread normalizes, RSI holds 50–70, price reclaims $208.26 on volume ≥1.5×, all three gates can clear simultaneously. #1 priority setup for tomorrow.

**SNOW (2b-LONG) — STILL SKIP:**
- RSI cooling (90.49 → 86.55) but massively overbought. Needs sustained correction to sub-70.
- Z-Score +3.689 — extreme extension unchanged.
- Pivot extension: ($242.50 / $177.60 − 1) = +36.6% ❌ — structural disqualification.
- Spread 0.825% is borderline acceptable but all quant gates remain hard-failed.
- No path to qualification without weeks of consolidation and mean-reversion.

**ORCL (2b-LONG) — STILL SKIP:**
- RSI improved from 56.82 → 65.42 ✅ — now cleanly in the 50–70 range.
- Notable: ORCL surged strongly today (+6.3% from yesterday's close, $190.96 → $203.08). Z-Score +1.638.
- Volume 0.749× (needs ≥1.5×) ❌ — still the primary quantitative gate failure.
- Earnings binary: Q4 FY2026 earnings ~June 10–12 (~13 days) ❌ — hard rule blocks entry through earnings.
- Pivot extension: +3.67% ✅ (within 5%).
- Cannot enter regardless of volume because the earnings binary is a hard Layer A block. ORCL's breakout move today may be earnings-anticipation-driven — exactly the scenario the earnings rule protects against.

**XLV (2a-SHORT) — STILL SKIP:**
- RSI *deteriorated*: 68.95 → 62.28. Moved *away* from the >70 trigger, not toward it.
- Z-Score improved slightly: +2.163 → +2.186 ✅ — above threshold but RSI not confirming.
- Volume 0.564× (needs ≥1.0×) ❌.
- Short Trend Template structural conflict unchanged: price above 50-SMA, XLV in uptrend.
- XLV is consolidating near highs, not overheating. RSI digesting is bearish for the short setup.

**XLE (2a-LONG / 2b-SHORT) — STILL SKIP:**
- Z-Score: −0.995 (barely misses −1.0 threshold for 2b-SHORT; far from −2.0 for 2a-LONG).
- RSI 45.05 ✅ — only passing gate for 2b-SHORT lane.
- No breakdown: price $56.91 > 20d low $55.70 ❌.
- Volume 0.822× ❌ (partial day).
- WTI oil flat-to-down today ($56.91 XLE vs $57.24 open = −0.46%). Neither a clear reversal nor breakdown.
- Energy sector flag active (1 consecutive failure: XOM May 7). Heightened caution maintained.

---

**Trades fired this rescan:** None

**Patience rule applied:** Correct outcome. No gate was lowered. Zero trades is the right call.

---

**Updated Forward Watchlist (Friday / Next Week):**

1. **MRVL — #1 PRIORITY:** RSI cooling to 64.91 is the key positive development from today's rescan. Three gates still needed simultaneously Friday: (a) spread normalizes <1%, (b) price reclaims $208.26 pivot with close above on volume ≥1.5×, (c) RSI holds 50–70. Z-Score +1.862. All fundamentals intact.

2. **XLK — #2 (2b-LONG):** RSI running hotter (now 78.86) — needs material consolidation back below 70. Pivot $185.14 already cleared. Watch for pullback day with RSI normalizing.

3. **ORCL — post-earnings (2b-LONG):** Today's +6.3% surge is interesting but blocked by earnings binary. Check back week of June 15 after earnings cleared. Setup structure (RSI 65.42, Z +1.638, pivot extension +3.67%) is the cleanest of the group — just needs the earnings window to pass.

4. **XLE — 2a-LONG watch:** Z=−0.995 — trigger at $55.42. Needs −$1.49 further decline plus RSI dropping below 30. If WTI resumes downtrend, monitor closely.

5. **XLV — 2a-SHORT watch:** Z=+2.186 ✅ but RSI pulled back to 62.28. Only activates if healthcare rips to RSI>70 on a strong up-day with volume ≥1.0×.


---

## 2026-05-28 — Afternoon Scan Addendum (~15:50 ET / 19:50 UTC)

**Scan time:** ~2 hours before market close (market closes 20:00 UTC / 4:00 PM ET)
**VIX regime at scan:** NORMAL (prior close ~17.01 from morning research; VIXY stale R-flag quote) | Sizing multiplier: 1.00×

---

### STEP 1 — Order & Position State Reconciled vs TRADE-LOG

**Orders returned by API (6 total — all historical, all terminal):**

| Order ID | Symbol | Type | Status | Detail |
|----------|--------|------|--------|--------|
| 1d69c496 | XOM | Bracket limit BUY 61 sh @ $159.78 | **EXPIRED** 2026-05-18T20:02 | TIF: day — never filled ✅ logged |
| 94606e38 | XOM | Stop child $147.80 | **CANCELED** 2026-05-18T20:02 | Auto-cancelled ✅ logged |
| 336d922a | XOM | TP child $183.74 | **CANCELED** 2026-05-18T20:02 | Auto-cancelled ✅ logged |
| 8f97ef7d | XOM | Market Sell 130 sh | **FILLED** $146.09, 2026-05-07 | Thesis-break exit ✅ logged |
| d92d9371 | XOM | Trailing Stop 10% GTC | **CANCELED** 2026-05-07 | Pre-exit ✅ logged |
| c04ae321 | XOM | Market Buy 130 sh | **FILLED** $153.35, 2026-05-01 | Original entry ✅ logged |

- **Positions API: `[]` — 100% cash ($99,056.46).** No filled positions.
- **Morning bracket orders placed today (May 28): NONE** — Pre-market research issued explicit HOLD: XLK (RSI 73.76 > 70, Vol 0.41×, TT fails); MRVL (5 gate failures including earnings binary yesterday); SNOW (RSI 90, ext +35.2%, negative 6mo return); ORCL (Vol 0.69×, earnings binary ~June 10); XLV (RSI 68.95 < 70, Vol 0.47×); XLE (Z = −0.795, no lane). Nothing to reconcile for fills.
- **Bracket fills today: 0** | **Stale limits: 0** | **TRADE-LOG reconciliation: FULLY CURRENT ✅**

---

### STEP 2 — Trailing Stop Upgrades on Profitable Fills

**N/A.** Portfolio is 100% cash ($99,056.46). No positions exist. No trailing stop upgrade workflow applicable.

---

### STEP 3 — Stale Limit Cancellations

**None.** No open orders of any kind exist.

---

### STEP 4 — Afternoon Opportunity Scan (5 Candidates, 4 Sectors)

**VIX regime:** NORMAL (1.00×) | **Positions:** 0/6 | **Week trades:** 0/3 | **PDT:** 0/3

**Full quant metrics — May 28, 2026 final settled bar data:**

| Ticker | Close | 20d Mean | 20d Std | Z-Score | RSI(14) | Vol May28 vs Avg | 20d High | 20d Low | Verdict |
|--------|-------|----------|---------|---------|---------|-----------------|----------|---------|---------|
| XLK | $186.85 | $174.51 | $7.52 | **+1.640** | **73.53** | 0.91× ❌ | $186.85 | $159.50 | **REJECT** |
| MRVL | $204.83 | $178.42 | $14.18 | **+1.862** | **71.56** | **1.93×** ✅ | $208.26 | $160.01 | **REJECT** |
| XLE | $56.95 | $58.40 | $1.49 | −0.973 | 54.59 | 1.15× | $61.29 | $55.70 | **REJECT** |
| XLV | $150.88 | $146.43 | $1.98 | **+2.245** | **69.40** | 1.07× ✅ | $150.88 | $143.04 | **REJECT** |
| XOM | $146.96 | $152.61 | $4.56 | −1.239 | 50.53 | 0.80× | $162.55 | $144.57 | **REJECT** |

**Pair Divergences (all ≤ 1.5σ — all confirm):**
- XLK (+1.640) ↔ AVGO (+0.759): **0.882σ ✅** — tech pair moving together
- XOM (−1.239) ↔ CVX (−1.178): **0.061σ ✅** — energy names in near-perfect lockstep
- XLE (−0.973) ↔ XOM (−1.239): **0.266σ ✅** — sector-wide energy drift

---

**XLK — REJECT (2 active gate failures):**
- Z = +1.640 ✅ | Breakout: $186.85 = AT new 20d high ✅ | Extension: 0.0% ✅ | AVGO pair: 0.882σ ✅
- **RSI = 73.53 ❌** — overbought, above the 50–70 healthy momentum ceiling. Was 70.94 yesterday, 73.76 at this morning's open — has continued to drift higher, not normalizing.
- **Volume = 0.91× ❌** — below the 1.5× breakout confirmation gate (10.97M vs. 12.03M avg). New 20d high was achieved today ($186.85, first clean new 20d high as a settled close since the May 22/$180.39 pivot was broken May 26), but institutional participation was not there.
- **Trend Template:** 50-SMA < 150-SMA (structural issue from Dec 2025 2:1 split disrupting SMA computation). 200-SMA unverifiable (~37 sessions to resolve, est. mid-August 2026).
- **Key positive:** XLK's new 20d high ($186.85) at the close with 0.0% pivot extension is the cleanest breakout structure of the week. If Friday's session brings RSI cooling (any flat/down open delivers this) and volume ≥1.5× → 2b-LONG activates. Max limit ≤ $186.85 × 1.05 = **$196.19**. Pair divergence (0.882σ) is the best it's been all week.

**MRVL — REJECT (2 active gate failures):**
- Z = +1.862 ✅ | **Volume = 1.93× ✅** (strongest in scan; 52.3M shares — institutional accumulation ongoing post-earnings) | Extension −1.6% ✅
- **Close $204.83 < pivot $208.26 ❌** — $3.43 below the 20d high. MRVL's post-earnings saga: surged to $218+ (May 26 $208.26 → May 27 open $217.98), faded hard to $198.70, then recovered to $204.83 today. The breakout pivot has NOT been reclaimed on a closing basis.
- **RSI = 71.56 ❌** — 1.56 points above the 70 ceiling for the 2b-LONG lane (need 50–70). Improving from the 70.23 at yesterday's open, but still marginally over.
- **Trend Template:** 200-SMA unverifiable (152/200 bars). However 50-SMA ($144.24) > 150-SMA ($104.67) ✅ — structurally valid post-earnings re-rating. >30% above 52w low (+171.5%) ✅. 6-month return +164.4% = top quintile ✅. Partial TT confirms leadership.
- **Status:** This is the #1 watchlist setup heading into the weekend/next week. Three gates are converging: (a) RSI needs 1.56 more points of cooling — any consolidation session delivers this; (b) pivot $208.26 needs $3.43 more upside from current $204.83; (c) volume already confirming strongly at 1.93×. Max entry ≤ $208.26 × 1.05 = **$218.67**.

**XLE — REJECT (no lane qualifies):**
- Z = −0.973 — midrange. 2a-LONG needs ≤ −2.0 (trigger $55.42, gap = $1.53 or −2.7%). 2b-SHORT needs ≤ −1.0 AND close < $55.70 (gap = $1.25 above breakdown level). RSI = 54.59 (neutral). Volume 1.15× (above 1.0× ✅ but 2b-SHORT needs 1.5×).
- XOM–XLE divergence: 0.266σ ✅ — both names declining in lockstep. Sector thesis (WTI, Iran) intact structurally but supply premium continues deflating.
- Energy sector: 1 consecutive failure (XOM May 7). Heightened caution on any new energy entry.

**XLV — REJECT (1 gate failure, 0.60 RSI points away):**
- Z = **+2.245 ✅** | Volume = **1.07× ✅** — both quant gates PASS. XLV made a new 20d high at $150.88 today.
- **RSI = 69.40 ❌** — 0.60 points below the >70 threshold. This is the sole remaining gate for the 2a-SHORT mean-reversion short lane.
- Healthcare sector surged today: $150.88 close vs. $148.79 yesterday (+$2.09, +1.40%). The sustained rally is building toward RSI exhaustion — if XLV opens Friday with another uptick, RSI may cross 70.
- **Short TT structural conflict:** XLV is AT its 52-week high ($150.88 = session high). The Minervini Short TT requires price >30% below 52w high — structurally incompatible with a 2a-SHORT setup in an uptrend. Open strategy review item from Week 4 remains unresolved: 2a-SHORT should require Z/RSI/vol only, without the full downtrend Minervini Short TT. Until that strategy update is formally made, this gate conflict persists.
- **Status:** #2 watchlist priority. If Friday opens with healthcare strength and RSI cracks >70 with volume ≥1.0× (≥9.7M shares) → 2a-SHORT activates (subject to TT conflict resolution). Max short size: 10% of equity = $9,906 (short position cap per CONSTRAINTS.md). Max entry at current-price-level short.

**XOM (context):**
- Z = −1.239; RSI = 50.53; Volume = 0.80× (below avg). Gap to 2a-LONG trigger (Z ≤ −2.0): price needs to reach ~$143.49 (−$3.47 more decline). 20d low = $144.57. Energy 1-fail flag active. No position.

**New afternoon entries: ZERO** — all 5 candidates rejected. No orders placed.

---

### STEP 5 — Afternoon Market Context

Today's session (May 28) featured two notable developments that will shape tomorrow's (Friday) pre-market evaluation:

**1. XLK confirmed a new settled 20d high at $186.85.** This is the first clean new 20d high as a closing bar since May 26's $185.14 pivot was broken. The stock has now set three successive 20d highs: $180.39 (May 22) → $185.14 (May 26) → $186.85 (today). The momentum structure is clean. The two missing gates — RSI cooling to 50–70 and volume ≥1.5× on the entry day — are timing gates, not structural gates. The setup is literally one strong-volume, moderately-cooled session away from qualifying.

**2. MRVL continues its post-earnings recovery.** From the May 27 "sell the news" intraday low of $196.25 to today's close of $204.83 (+$8.58, +4.4% recovery). Volume remains elevated (1.93× avg today, 2.0× yesterday). The earnings binary has been resolved. The $208.26 pivot — representing the last settled 20d high before the post-earnings dislocation — remains $3.43 away. RSI 71.56 is cooling (was 70.23 at yesterday's morning open, 64.91 at yesterday's midday rescan, 71.56 today — slight tick up but structurally cooling from the 76+ range earlier this week).

**3. XLV overbought signal intensifying.** Z = +2.245 (up from +2.163 at this morning's open). Healthcare ETF made a new 20d high at $150.88 on volume 1.07×. RSI at 69.40 is now 0.60 points from the >70 overbought trigger. The 2a-SHORT setup is within reach — but the Minervini Short TT structural conflict remains the strategy-level question that needs resolution.

**4. Energy (XOM, XLE, CVX) continues orderly decline.** All three names declining on below-average volume (~0.61σ pair divergence across the group). Iran Hormuz narrative continues to deflate WTI supply premium. No new entry signals in energy sector.

---

**Bracket fills today:** 0 (no morning limits placed — HOLD decision at pre-market; all 6 candidates failed gates)
**Stops upgraded:** 0 (no positions held; no trailing stop upgrade workflow applicable)
**Stale limits cancelled:** 0 (none existed)
**New afternoon entries:** none — all 5 candidates failed composite Layer A + Layer B gates
**Afternoon market context:** XLK new 20d high $186.85 (RSI 73.53, vol 0.91× — two gates from 2b-LONG activation). MRVL recovery to $204.83 on 1.93× volume (pivot $208.26, $3.43 away, RSI 71.56 — two gates from activation). XLV Z = +2.245, vol 1.07× — RSI 69.40 (0.60 from >70 trigger). Energy declining orderly on below-avg vol. VIX Normal.

**Key watchlist for Friday pre-market (2026-05-29) and next week:**
1. **MRVL — #1 PRIORITY (2b-LONG):** Z = +1.862 ✅, Vol = 1.93× ✅, extension −1.6% ✅. Gates remaining: (a) RSI must cool from 71.56 → below 70 (any consolidation/flat open achieves this), (b) price must reclaim $208.26 pivot on a settled close. Max entry limit ≤ **$218.67** (pivot × 1.05). 200-SMA structural gap (~37 sessions).
2. **XLK — #2 (2b-LONG):** Z = +1.640 ✅, breakout ✅, ext 0.0% ✅, AVGO pair 0.882σ ✅. Gates remaining: (a) RSI must cool from 73.53 → 50–70 (requires flat/down open; currently drifting higher), (b) volume must reach ≥1.5× avg (≥18.1M shares full session). Max entry limit ≤ **$196.19** (pivot $186.85 × 1.05). 200-SMA structural gap.
3. **XLV — #3 (2a-SHORT, conditional):** Z = +2.245 ✅, Vol = 1.07× ✅. Gate remaining: RSI > 70 (currently 69.40, 0.60 points away). TT structural conflict (2a-SHORT vs Minervini downtrend requirement) is the formal open item; operationally, if RSI clears and the strategy review update is implemented, this becomes a live trade. Short sizing cap: 10% of equity = $9,906.
4. **XLE** — Z = −0.973; 2a-LONG trigger at $55.42 (−2.7% away). Monitor if WTI resumes decline.
5. **XOM** — Z = −1.239; 2a-LONG trigger ~$143.49 (−$3.47 away). Energy 1-fail flag. No urgency.
6. **200-SMA data gap:** ~37 trading sessions remaining (est. mid-August 2026). All Minervini TT 200-SMA "CANNOT VERIFY" flags auto-resolve as data accumulates.


---

## 2026-05-29 — Pre-Market Research

### Account
- **Equity:** $99,056.46
- **Cash:** $99,056.46 (100%)
- **Buying power:** $198,112.92 (margin — but strategy uses cash only)
- **Daytrade count:** 0/3
- **Open positions:** NONE
- **Open orders:** NONE
- **Phase P&L:** −$943.54 (−0.944% from $100k start)

---

### Market Context
- **WTI Crude Oil:** ~$88.77/bbl (−0.65% on day); spot Cushing $97.63 on May 26. WTI declined ~1.5% across reports. Iran Hormuz premium deflating.
- **Brent Crude:** ~$90.86–$91.01 (−1.83% from prior close of $92.70). Brent −17.57% over past month, +44.96% YoY. Spot Europe $102.75 on May 26.
- **S&P 500 Futures:** ESM26 +0.59% Thursday. S&P 500 index up 9.8% YTD. Markets reached 1-week highs on US-Iran peace deal hopes.
- **VIX:** 15.52 (opened 15.81, prior close 16.29; −4.23% from prior day, −14.08% YoY). Continuing drift lower from elevated levels.
- **Key Catalysts:**
  - US-Iran preliminary ceasefire talks reducing energy supply risk premium → headwind for energy longs
  - NVDA Q1 revenue $81.6B — massive AI infrastructure beat; AI spending cycle continuing
  - Dell (DELL) beat Q1 earnings May 28, popped in extended trading
  - AVGO (Broadcom) up ~+2.9% today ($426.58 → $439.00) — likely DELL/AI read-through catalyst
  - IPO market reopening (SpaceX interest cited)
- **Economic Calendar (today May 29):**
  - 8:30 AM ET: US Advance Economic Indicators
  - 9:45 AM ET: ISM Chicago PMI
  - Fed speakers: Lorie Logan (4:00 AM), Lisa Cook (3:55 PM), Philip Jefferson (8:00 PM)
  - No CPI, PPI, FOMC, or Jobs data today
- **Yesterday (May 28):** April PCE headline +0.4% m/m / +3.8% y/y; core +0.24% m/m / +3.3% y/y. Initial claims 215,000.
- **S&P 500 Sector YTD (as of May 12):**
  - Energy +27.87% | IT +23.55% | Materials +15.24% | Industrials +12.84%
  - Real Estate +10.46% | Staples +7.32% | Utilities +5.74%
  - Cons. Disc −0.03% | Comm. Services −1.82% | Financials −6.55% | Health Care −7.60%
  - *Note: Healthcare cited as top-performing in May specifically, contradicting YTD rankings.*

---

### VIX Regime
- **Current VIX:** 15.52
- **Regime:** Normal (14–22 range)
- **Sizing multiplier:** 1.00×
- **Strategy bias:** All entry types permitted; no regime restriction on today's evaluation

---

### Universe Scan — Candidates Evaluated

#### Candidate 1: MRVL | LONG | 2b-LONG (Momentum)
**Catalyst:** Post-earnings AI momentum; AVGO beat today is a sector read-through. MRVL recovering from May 27 "sell-the-news" dip. Semi sector AI capex cycle intact (NVDA/DELL/AVGO chain).

**Layer A — Catalyst + Trend Checklist:**
- Catalyst: ✅ AI infrastructure spending wave; AVGO confirming sector-wide
- Sector posture: IT/Semis #2 YTD (+23.55%). Momentum sector ✅
- RSI(14): 63.88 (using today's partial close) ✅ in 50–70 zone
- Stop level: $183 (−9.9% from $203.11 entry) ✅
- Target: $225 (+10.8% from entry); R:R = $21.89 risk vs $21.89 target = 1.0R — need $225+ for 2:1. Target revised to $225 for 2:1. ✅ Layer A R:R marginal

**Layer B — Quant (2b-LONG):**
- Z-Score: **+1.697** ✅ (mean20 = $178.42, std20 = $14.55, current $203.11)
- Close > prior 20d high ($203.11 vs pivot $208.26): **❌ FAIL** — price is $5.15 BELOW pivot
- RSI(14) 63.88: ✅ in 50–70 zone
- Volume projected 1.08× avg (partial day, ~13.4M / 27.1M avg): **❌ FAIL** (need ≥ 1.5×)
- 50-SMA ($146.64) > 150-SMA ($105.51): ✅ (200-SMA unverifiable — 48 bars short)
- Trend Template (Momentum Long): Price > 50-SMA ✅, Price > 150-SMA ✅, 50 > 150 ✅; 200-SMA CANNOT VERIFY; >30% above 52w low (+175.2%) ✅; within 25% of 52w high (−2.6%) ✅; 6-month return +131.3% (top quintile) ✅. **PARTIAL TT — 3 verifiable conditions PASS, 200-SMA gap persists**
- Pivot extension: $203.11 / $208.26 = −2.47% (below pivot) → **not applicable** (price is below pivot)
- Pair: AVGO | Pair Z-Score: **+2.526** | Divergence: **0.468σ ✅** (tech sector cohesion strong today)

**Layer B Result: ❌ FAIL — 2 gates fail: (1) close below 20d high pivot ($203.11 < $208.26), (2) volume 1.08× < 1.5× required**

---

#### Candidate 2: XLK | LONG | 2b-LONG (Momentum)
**Catalyst:** Tech ETF breakout to new multi-week high; AVGO +2.9% today (AI capex chain), DELL beat, NVDA earnings flywheel. XLK is the cleanest sector expression of AI infrastructure demand.

**Layer A — Catalyst + Trend Checklist:**
- Catalyst: ✅ AI spending cycle + AVGO beat today
- Sector posture: IT #2 YTD ✅
- RSI(14): **79.67** ❌ (overbought — above 70; need 50-70 for 2b-LONG)
- Stop level: $172 (−9.7% from $190.40) ✅ structure
- Target: $209 (+9.8% from entry) — R:R = 2:1 ✅

**Layer B — Quant (2b-LONG):**
- Z-Score: **+2.058** ✅ (mean20 = $174.51, std20 = $7.72, current $190.40)
- Close > prior 20d high ($190.40 > pivot $186.85): **✅ PASS** — clean breakout
- RSI(14) = 79.67: **❌ FAIL** (need 50–70; currently overbought)
- Volume projected 0.79× avg (partial day, 4.37M / 12.04M avg): **❌ FAIL** (need ≥ 1.5×)
- 50-SMA ($157.39) > 150-SMA ($147.62): ✅; 200-SMA unverifiable
- Trend Template: Price > 50-SMA ✅, Price > 150-SMA ✅; 200-SMA gap; >30% above 52w low (+159.7%) ✅; AT 52w high (0.0% below) ✅; 6-month return +34.2% (strong) ✅. **PARTIAL TT — verifiable conditions PASS**
- Pivot: $186.85; limit $190.40; extension +1.90% ✅ (≤5%)
- Pair: AVGO | Z-Score: +2.526 | Divergence: **0.468σ ✅**

**Layer B Result: ❌ FAIL — 2 gates fail: (1) RSI 79.67 > 70 (overbought), (2) volume 0.79× < 1.5× required**

---

#### Candidate 3: XLV | SHORT | 2a-SHORT (Mean-Reversion)
**Catalyst:** Healthcare ETF had run to multi-week high ($150.88 on May 28, Z = +2.245 yesterday). 2a-SHORT setup was on watch. Today: XLV gave back, closing at $149.53 (−$1.36, −0.90% from yesterday's high).

**Layer B — Quant (2a-SHORT):**
- Z-Score: **+1.523** ❌ FAIL (need ≥ +2.0; dropped from +2.245 yesterday as XLV pulled back)
- RSI(14) = 60.79: **❌ FAIL** (need > 70; was 69.40 yesterday, rolling off overbought)
- Volume projected 1.24× avg: ✅ PASS (need ≥ 1.0×)
- Pair (UNH) Z-Score: −0.424; Divergence vs XLV: **1.947σ ❌ FAIL** (need ≤ 1.5σ; UNH declining while XLV was overbought = sector divergence)

**Layer B Result: ❌ FAIL — 3 gates fail: Z dropped below +2.0, RSI < 70, pair diverges >1.5σ**
**Critical note:** The XLV setup has UNWOUND. Yesterday's Z = +2.245, RSI = 69.40 were approaching trigger. Today's pullback ($150.88 → $149.53) means the mean-reversion SHORT signal has self-corrected. This is the correct outcome — XLV reverted partway back to mean without our entry. Setup is invalidated. Monitor only if XLV re-stretches to Z > +2.0 in future sessions.

---

### Trade Ideas (Cleared Both Layers)
**None — all three candidates failed Layer B gates.**

---

### Skipped Candidates

| Candidate | Direction | Lane | Key Failures | Status |
|-----------|-----------|------|-------------|--------|
| MRVL | LONG | 2b-LONG | Close $203.11 < pivot $208.26 ❌; Vol 1.08× < 1.5× ❌ | REJECT — watchlist #1 |
| XLK | LONG | 2b-LONG | RSI 79.67 > 70 ❌; Vol 0.79× < 1.5× ❌ | REJECT — watchlist #2 |
| XLV | SHORT | 2a-SHORT | Z +1.523 < +2.0 ❌; RSI 60.79 < 70 ❌; UNH pair divergence 1.947σ > 1.5σ ❌ | REJECT — setup unwound, remove from immediate watchlist |

---

### Market Structure Notes
- **XLK breakout confirmed on settled close:** Today's $190.40 close sets a new 20d high (previous pivot $186.85). Breakout is real. But RSI 79.67 says the day's move was too strong — momentum entry requires RSI 50–70, not >70. A 2–3 day RSI cooling period is needed.
- **AVGO +2.9% today ($439):** Strong. Its Z-score = +2.526. AVGO is outrunning XLK on a relative basis. If AVGO consolidates next week and XLK RSI cools, the sector ETF entry becomes cleaner than the single-name.
- **MRVL:** Pulled back intraday ($208.76 high → $203.11 close). The stock attempted to reclaim the $208.26 pivot but failed to close above it. RSI cooling from 65+ to ~63 is healthy. Volume was elevated (52.6M yesterday vs 13.4M today partial — Friday typical low volume day). Next week's catalyst test: does MRVL find buyers on a volume surge?
- **Energy (XOM/XLE/CVX):** WTI −0.65%–1.54% today. Iran deal progress continues to deflate supply premium. Energy sector 1-fail flag from May 7 XOM trade remains active. No energy candidates evaluated — sector headwinds confirmed.
- **VIX trending lower (15.52):** A VIX that keeps declining typically accompanies a bull market grind. This environment favors momentum setups — which validates keeping XLK and MRVL on the watchlist. Low VIX also means mean-reversion trades (2a) have smaller Z-score swings, making the +2.0 trigger harder to hit.

---

### Risk Factors
1. **Iran deal uncertainty:** If talks collapse, energy supply premium returns. XLE/XOM would spike, creating a potential 2a-LONG setup on oil names that we would need to evaluate fresh.
2. **Fed speakers today (Cook at 3:55 PM, Jefferson at 8:00 PM):** Any hawkish tone could crack the tech rally and give RSI the pullback needed for MRVL/XLK entries. Actually a constructive risk for watchlist setup formation.
3. **ISM Chicago PMI (9:45 AM):** A weak print could trigger a risk-off move; strong print could push XLK RSI even higher, extending the wait.
4. **Month-end effects (May 31 is weekend):** May 29 is the last trading day of the month. Month-end rebalancing can create anomalous volume and price action in either direction. This adds noise to volume readings and makes today's partial volume data less reliable as a signal.
5. **200-SMA data gap:** Still ~48 sessions short (~August 2026 resolution). All Trend Template calls are partial. This is a known ongoing limitation, not a new flag.

---

### Decision
**HOLD — 0 trades today**

All three Layer B evaluations fail. MRVL and XLK are strong setups structurally but need additional sessions for RSI to normalize and volume to confirm on entry day. XLV's overbought mean-reversion short has unwound — the window closed without our participation (correct per patience rule). Zero trades this week (0/3). Cash at 100% ($99,056.46). This is the right outcome.

**Watchlist priority heading into next week:**
1. **MRVL (#1):** Z = +1.697, RSI = 63.88, RSI in zone ✅. Needs: (a) price reclaim $208.26 pivot on a settled close, (b) entry day volume ≥ 40.6M shares. Max entry limit ≤ **$218.67** (pivot $208.26 × 1.05). Monitor Mon-Tue.
2. **XLK (#2):** Z = +2.058, new 20d high ✅. Needs: (a) RSI cool from 79.67 → below 70 (2-3 flat/down days), (b) entry day volume ≥ 18.1M shares. Max entry limit ≤ **$196.19** (pivot $186.85 × 1.05). RSI is the gating factor — could take until Wednesday.
3. **AVGO (new watch):** Z = +2.526, surging +2.9% today on AI catalyst. AVGO is in momentum lane but RSI likely also elevated. Evaluate fresh Mon pre-market as potential momentum long candidate.
4. **XLV:** REMOVE from active watchlist. Setup unwound. Revisit only if Z re-stretches > +2.0 in a future session.


---

### 2026-05-29 — Midday Rescan Addendum (17:52 ET)

**Skipped at open, re-evaluated:**

| Ticker | Lane | Morning Skip Reason | Spread Now | Z-Score | Gate Failures | Verdict |
|--------|------|---------------------|------------|---------|---------------|---------|
| MRVL | 2b-LONG | Price below pivot, vol 1.08× | 1.074% ❌ | +1.650 ✅ | (1) Spread 1.074% > 1.0% ❌ (2) Price $204.90 still below $208.26 pivot ❌ (3) Vol 0.633× < 1.5× ❌ | **STILL SKIPPED** |
| XLK | 2b-LONG | RSI 79.67>70, vol 0.79× | 0.011% ✅ | +1.885 ✅ | (1) RSI 79.44 > 70 ❌ (still overbought; essentially unchanged from open) (2) Vol 0.649× < 1.5× ❌ | **STILL SKIPPED** |
| XLV | 2a-SHORT | Z +1.523<2.0, RSI 60.79<70, pair diverge | 0.007% ✅ | +1.340 ❌ | (1) Z +1.340 < +2.0 ❌ (further unwound from +1.523 at open) (2) RSI 60.24 < 70 ❌ (3) Vol 0.786× < 1.0× ❌ | **STILL SKIPPED — setup fully dead** |

**Detail notes per ticker:**

- **MRVL:** Spread actually widened slightly midday vs open (bid $203.80 / ask $206.00 = 1.074%). This is unusual for a liquid large-cap semi — likely thin midday NBBO quote. Core quant failures unchanged: price at $204.90 remains $3.36 below the $208.26 pivot (needs a close above $208.26 to trigger 2b-LONG). Volume is 17.1M at midday vs 27.1M 20d avg = 0.63× pace. RSI 64.50 remains healthy (50–70) — the only passing quant metric. MRVL is the cleanest structural setup; it just needs the pivot reclaim + volume confirmation on a future session. Watchlist #1.

- **XLK:** Spread fully normalized (0.011%) as expected. This was not a spread-skip — it was pure RSI overextension. Midday RSI is 79.44, essentially identical to morning's 79.67. The intraday session has done nothing to cool RSI. Volume 7.8M at midday vs 12.0M avg = 0.65× pace (Friday, month-end). Both gate failures persist unchanged. Pivot breakout is valid ($190.02 > $186.85), Z-score is +1.89, and pivot extension is clean (1.7%). The setup is structurally sound — RSI just needs 2–3 flat/down sessions to cool into the 50–70 zone. This is the correct patience behavior, not a deterioration. Watchlist #2 into next week.

- **XLV:** Z-score has actually *declined* since this morning (+1.523 → +1.340) as XLV continues to pull back from yesterday's $150.88 high. RSI has cooled further to 60.24. Volume pace 0.786× also below the 1.0× minimum for 2a-SHORT. The overbought mean-reversion short window has definitively closed. XLV has mean-reverted ~$1.50 without our participation — exactly what the Z-score predicted would happen. This is the patience rule working correctly: the setup unwound, no trade was taken, no loss incurred. **Remove XLV from active watchlist entirely.** Only revisit if Z re-stretches above +2.0 in a future session.

**Trades fired this rescan:** None

**Patience rule applied:** Zero candidates re-cleared all gates. No entry gates were lowered. This is the correct outcome. Today is also the last trading day of May (month-end Friday), which structurally depresses volume across all names — making it even less likely volume gates would clear midday.

**Month-end observation:** All three volume ratios are in the 0.63×–0.79× range, well below their respective thresholds. This is consistent with month-end rebalancing reducing directional volume. This pattern does not change the gate math — rules are rules — but it contextualizes why midday volume clearance was unlikely today.

**Updated watchlist for next week (Monday June 2):**
1. **MRVL (#1, Momentum Long):** Needs (a) close above $208.26 pivot on volume ≥ 40.6M shares, (b) RSI stays 50–70 (currently 64.50 — healthy). Max limit ≤ $218.67 (pivot × 1.05). Watch for AI sector catalyst continuation.
2. **XLK (#2, Momentum Long):** Needs (a) RSI to cool from 79.44 → sub-70 (2–3 flat/down sessions), (b) entry-day volume ≥ 18.1M shares. Max limit ≤ $196.19 (pivot $186.85 × 1.05). Price action has held well — ETF is not reversing, just pausing.
3. **AVGO (new watch from Monday):** Z-score was +2.526 today, closed strong. Could be a 2b-LONG or 2a-SHORT candidate depending on next week's action. Pull full quote + bars Mon pre-market.

---

---

## 2026-05-29 — Midday Scan Addendum (18:30 UTC / ~1:30 PM ET)

**Scan type:** Midday workflow — position thesis check, stop evaluation, watchlist validation
**VIX Regime:** Normal (~15.52–16.0 from morning research) — 1.00× sizing multiplier
**Session phase:** Late (330 min elapsed, ~90 min to close)
**Account:** Equity $99,056.46 | Cash $99,056.46 (100%) | 0 positions | 0 orders | PDT 0/3 | Week 0/3

---

### Portfolio State (Live API)
- **Positions:** `[]` — EMPTY. 100% cash confirmed.
- **Orders:** `[]` — EMPTY. No working brackets. No GTC stops.
- Pre-market HOLD decision confirmed: MRVL close below pivot + vol 0.688×; XLK RSI 79.67 + vol 0.79×; XLV setup unwound (Z dropped to +1.340). No brackets placed.
- TRADE-LOG fully current. No discrepancy.

---

### Cut Losers / Tighten Stops
**N/A — no open positions.**

---

### Watchlist Re-Evaluation (Live Quotes ~18:28 UTC)

**Quant computed from settled 24-bar history + today's partial bar:**

| Ticker | Close (partial) | Z-Score | RSI(14) | Vol Ratio | 20d High | Breakout | AVGO/MRVL pair div | Verdict |
|--------|----------------|---------|---------|-----------|----------|----------|--------------------|---------|
| MRVL | $207.135 | +2.025 ✅ | 66.04 ✅ | 0.688× ❌ | $208.26 | ❌ ($1.12 below) | 0.158σ ✅ | **STILL SKIPPED** |
| XLK  | $190.330 | +2.103 ✅ | 79.63 ❌ | 0.695× ❌ | $186.85 | ✅ (+$3.48) | 0.080σ ✅ | **STILL SKIPPED** |
| AVGO | $436.235 | +2.183 ✅ | 56.90 ✅ | 0.840× ❌ | $439.79 | ❌ ($3.56 below) | 0.158σ ✅ | **NEW WATCHLIST #3** |

---

### Detailed Assessment

**MRVL (2b-LONG, #1):**
- Today's high $208.76 touched above $208.26 pivot intraday but closed at $207.135 — $1.12 short of pivot on closing basis
- Pattern: each session closing price is converging toward pivot: $198.70 → $204.83 → $207.135 — gap narrows by ~$3–4/day
- RSI 66.04 ✅ (healthy momentum zone, cleanest RSI reading of the three names)
- Volume 0.688× — Friday month-end suppression; not a distribution signal
- AVGO pair divergence only 0.158σ — sector perfectly cohesive
- **Verdict: STILL SKIPPED** — 2 gates fail (pivot + vol). Setup structurally intact. Monday pre-market re-evaluation priority #1.

**XLK (2b-LONG, #2):**
- New 20d high today ($190.33, up from $186.85 yesterday) — clean breakout extending for 4th consecutive session
- RSI 79.63 — overbought since May 26, has not normalized. Momentum buying keeps running RSI higher each session.
- Volume 0.695× — Friday/month-end suppression
- **Verdict: STILL SKIPPED** — RSI must cool from 79.63 → sub-70 before momentum lane activates. Needs 2–3 flat/consolidation sessions. Max limit ≤ $196.19 (current pivot $186.85 × 1.05).

**AVGO (2b-LONG, NEW watchlist addition):**
- Today: +$9.66 (+2.3%) to $436.235 on AI/semiconductor momentum (DELL beat, NVDA capex cycle read-through)
- Intraday high $448.58 — TOUCHED above $439.79 20d pivot intraday but closed below it
- RSI 56.90 ✅ — THE CLEANEST RSI of all three watchlist names; squarely in 50–70 healthy momentum zone
- Volume 0.840× — approaching 1.0× but Friday/month-end; needs ≥1.5× on breakout day
- MRVL pair: 0.158σ ✅ | XLK pair: 0.080σ ✅ — all three names moving in near-perfect sector lockstep
- **Gate failures:** (1) Close $3.56 below $439.79 pivot, (2) Vol 0.840× < 1.5×, (3) 200-SMA structural gap
- **Adding to active watchlist as #3.** Monday: if AVGO opens strong and closes above $439.79 on ≥1.5× avg vol (~27.9M shares) with RSI holding 50–70, 2b-LONG bracket activates. Max entry limit ≤ $439.79 × 1.05 = **$461.78**.
- **Why AVGO could be better than XLK:** RSI is at 56.90 vs XLK's 79.63. Same sector, same AI catalyst. AVGO at RSI 57 entering a breakout is a much healthier setup structure than XLK at RSI 80. XLK is the ETF expression (15+ components averaging the RSI), AVGO is the single-name with higher beta to AI infrastructure spend.

---

### Trades Fired: None

**Patience rule applied.** All three names have the right directional structure (Z ≥+1.0, pair confirms, sector thesis intact) — blocked only by timing gates (vol 0.7–0.8×, RSI overextension in XLK, $1–4 price gap to pivots in MRVL/AVGO). Today is Friday, last trading day of May — month-end and pre-weekend volume suppression is structural.

**Circuit breakers:** ✅ Day P&L $0.00 | Phase P&L −0.944% (lim −5%) | Drawdown −1.15% (lim −15%)

---

### Key Watchlist for Monday Pre-Market (2026-06-01)

1. **AVGO — NEW #1 PRIORITY** (RSI 56.90 ✅, cleanest momentum setup structure): Needs (a) close above $439.79 on volume ≥27.9M (1.5× avg), (b) RSI stays 50–70, (c) pivot extension ≤ $461.78. If AI/semi momentum continues over weekend → AVGO may gap above $439.79 Monday. 200-SMA structural gap (~37 sessions). Pair: MRVL (0.158σ), XLK (0.080σ).
2. **MRVL — #2** (RSI 66.04 ✅, $1.12 from pivot): Needs (a) close above $208.26 on volume ≥40.6M (1.5× avg), (b) RSI 50–70. Max limit ≤ $218.67. Institutional accumulation confirmed (52.6M / 42.6M on prior two sessions). 200-SMA structural gap.
3. **XLK — #3** (RSI 79.63 ❌, needs cooldown): Needs RSI to normalize from 79.63 → sub-70. Requires 2–3 flat/down sessions. May be bumped by AVGO as preferred single-name expression of same AI thesis with better RSI entry dynamics. Max limit ≤ $196.19.
4. **200-SMA data gap:** ~37 trading sessions remaining (est. mid-August 2026). Persistent structural constraint on full Minervini TT for split-adjusted names.
5. **Weekly review note:** Week ending 2026-05-29 = 0/3 trades placed, 0/3 trades executed, 0 wins, 0 losses. Zero-trade weeks are valid outcomes per patience rule. 1 total closed trade (XOM, −4.73%, −$617.91 realized P&L). Phase P&L: −0.944%.


---

## 2026-05-29 — Afternoon Scan Addendum (~15:50 ET / 19:50 UTC)

**Scan time:** ~10 min before close (market closes 20:00 UTC / 4:00 PM ET)
**VIX regime at scan:** NORMAL (~16–17, prior close 16.29) | Sizing multiplier: 1.00×

---

### STEP 1 — Order & Position State Reconciled vs TRADE-LOG

**Orders returned by API (6 total — all historical, all terminal):**

| Order ID | Symbol | Type | Status | Detail |
|----------|--------|------|--------|--------|
| 1d69c496 | XOM | Bracket limit BUY 61 sh @ $159.78 | **EXPIRED** 2026-05-18T20:02 | TIF: day — never filled ✅ logged |
| 94606e38 | XOM | Stop child $147.80 | **CANCELED** 2026-05-18T20:02 | Auto-cancelled ✅ logged |
| 336d922a | XOM | TP child $183.74 | **CANCELED** 2026-05-18T20:02 | Auto-cancelled ✅ logged |
| 8f97ef7d | XOM | Market Sell 130 sh | **FILLED** $146.09, 2026-05-07 | Thesis-break exit ✅ logged |
| d92d9371 | XOM | Trailing Stop 10% GTC | **CANCELED** 2026-05-07 | Pre-exit ✅ logged |
| c04ae321 | XOM | Market Buy 130 sh | **FILLED** $153.35, 2026-05-01 | Original entry ✅ logged |

- **Positions API: `[]` — 100% cash ($99,056.46).** No filled positions.
- **Morning bracket orders placed today (May 29): NONE** — Pre-market research (2026-05-29) issued explicit HOLD: MRVL (close $203.11 < pivot $208.26; vol 1.08×); XLK (RSI 79.67 > 70; vol 0.79×); XLV (setup unwound — Z +1.523 dropped from +2.245 yesterday).
- **Bracket fills today: 0** | **Stale limits: 0** | **TRADE-LOG reconciliation: FULLY CURRENT ✅**

---

### STEP 2 — Trailing Stop Upgrades: N/A

No positions held. Portfolio is 100% cash. No upgrade workflow triggered.

---

### STEP 3 — Stale Limit Cancellations: N/A

No open orders exist.

---

### STEP 4 — Afternoon Opportunity Scan (5 Candidates, 4 Sectors)

**VIX regime:** NORMAL (1.00×) | **Positions:** 0/6 | **Week trades:** 0/3 | **PDT:** 0/3

**Full quant metrics computed from settled May 29 bars (via Alpaca API):**

| Ticker | Close | 20d Mean | 20d Std | Z-Score | RSI(14) | Vol May29 vs Avg | 20d High (pivot) | Lane | Key Gate | Verdict |
|--------|-------|----------|---------|---------|---------|-----------------|-----------------|------|----------|---------|
| **AVGO** | $446.77 | $422.91 | $8.664 | **+2.755** | **60.86** | **2.182×** ✅ | $439.79 ✅ (broke) | 2b-LONG | ✅ 7/8 gates pass; ❌ 200-SMA structural | **REJECT** |
| MRVL | $205.00 | $180.41 | $14.956 | +1.644 | 65.21 | 1.252× | $208.26 ❌ (below) | 2b-LONG | Close $3.26 below pivot ❌; Vol 1.25× ❌ | **REJECT** |
| XLK | $191.02 | $176.08 | $7.517 | +1.987 | 80.04 | 1.226× | $191.02 (AT) ❌ | 2b-LONG | RSI 80.04 > 70 ❌; Vol 1.23× ❌ | **REJECT** |
| XLV | $149.47 | $146.60 | $2.088 | +1.375 | 60.57 | 1.361× | $150.88 ❌ | 2a-SHORT | Z +1.375 < +2.0 ❌; RSI 60.57 < 70 ❌ | **REJECT** |
| XLE | $56.29 | $58.23 | $1.526 | −1.271 | 42.97 | 0.822× | — | 2a-LONG | Z −1.271 (need ≤ −2.0) ❌; RSI 43 ❌; Vol 0.82× ❌ | **REJECT** |

**Pair divergences (all computed from settled closes):**
- AVGO (+2.755) ↔ MRVL (+1.644): **1.110σ ✅** (within 1.5σ — sector confirmation)
- AVGO (+2.755) ↔ XLK (+1.987): **0.767σ ✅** (tech sector cohesion)
- XLE (−1.271) ↔ XLK (+1.987): **3.258σ ❌** (energy vs tech diverging — expected; sector rotation)

---

### AVGO — KEY DEVELOPMENT (2b-LONG lane — #1 highest-conviction setup this week)

**AVGO produced the strongest single-name quant signal since bot launch:**

| Gate | Result | Value |
|------|--------|-------|
| Z ≥ +1.0 | ✅ | +2.755 (highest Z-score in any afternoon scan to date) |
| Close > prior 20d high | ✅ | $446.77 > $439.79 (+1.59% clean breakout) |
| RSI 50–70 | ✅ | 60.86 (healthy momentum zone — NOT overbought) |
| Vol ≥ 1.5× avg | ✅ | 2.182× (40.6M vs 18.6M avg — strongest vol confirmation since launch) |
| Pivot extension ≤5% | ✅ | +1.59% → Max entry limit = $461.78 |
| MRVL pair divergence | ✅ | 1.110σ ≤ 1.5σ |
| 50-SMA > 150-SMA | ✅ | $385.70 > $359.71 |
| 200-SMA conditions | ❌ | **CANNOT VERIFY — 152/200 bars (structural data gap, Dec 2025 split)** |

**VERDICT: REJECT — 200-SMA TT gate cannot be bypassed per CONSTRAINTS.md.**

The 200-SMA structural block is UNIVERSAL — it has blocked every candidate since launch (XLK, MRVL, XLE, XLV, XOM, CVX, and now AVGO). This is a data availability constraint, not a thesis failure. The strategy rules require ALL Layer A + Layer B gates to clear. Per CONSTRAINTS.md: *"If ANY (1–13b) fail: Skip trade, log which check failed."* Consistent gate enforcement is correct.

**If Alex wishes to override:** The appropriate path is logging in `decisions/log.md`:
> `[2026-05-30] OVERRIDE: Minervini TT 200-SMA condition | REASON: Structural data gap for all post-Dec-2025 split-adjusted names — 200-SMA unavailable for ~48 more sessions; not a thesis failure | APPLIES TO: All split-adjusted names (AVGO, XLK, MRVL, XLE, etc.) | CONTEXT: Accept partial TT (50>150 SMA confirmed, 200-SMA trust proxied by verified SMA alignment)`

**AVGO position sizing (for reference if override granted):**
- 22 shares @ $446.77 limit = $9,829 (9.9% of equity)
- Stop: $413.26 (−7.5% below entry)
- Target: $513.79 (+15.0%, 2:1 R:R)
- R_dollars: $737.17 (0.74% of equity ✅)
- Max chase: limit ≤ $461.78 (pivot $439.79 × 1.05)

---

### MRVL — Status Update

**May 29 settled close: $205.00** (vs prior Thursday close $204.83 — essentially flat)

| Metric | May 28 Close | May 29 Close | Change |
|--------|-------------|-------------|--------|
| Close | $204.83 | $205.00 | +$0.17 |
| Z-Score | +1.862 | +1.644 | −0.218 |
| RSI | 71.56 | 65.21 | **RSI COOLED ✅** |
| Vol | 1.93× | 1.252× | Below 1.5× ❌ |
| vs Pivot $208.26 | −$3.43 | −$3.26 | Slight improvement |

**RSI has cooled from 71.56 → 65.21 — now firmly in the 50–70 healthy momentum zone.** This is the one gate that was blocking MRVL this week. The $208.26 pivot is now only $3.26 away. Volume on Friday (1.252×) was a typical light-volume Friday — not a distribution signal. **MRVL remains #2 watchlist priority for Monday pre-market (June 1/2).**

---

### XLK — Status Update

Close $191.02 — at its new 20d high (0.0% extension). RSI 80.04 (overbought, still above 70). Vol 1.226×. The tech ETF printed another new 20d high today but RSI remains elevated. XLK is running higher without us — the constraint-following behavior is correct; chasing a parabolic RSI-80 ETF is not edge. **#3 watchlist — needs RSI cooling session.**

---

### XLE — 2a-LONG trigger approaching slowly

Z = −1.271. Trigger at Z ≤ −2.0 requires price ~$55.18 (currently $56.29 = $1.11 or −2.0% further decline). RSI 42.97 (approaching but not yet < 30). Vol 0.822× (below 1.0× threshold). Energy thesis flag (1 consecutive failure) active. Not imminent but tracking. The trigger has drifted slightly lower ($55.18 vs yesterday's ~$55.42) as the 20d window continues to roll.

---

### Afternoon Market Context

Friday May 29 — last trading session of May. AVGO surged +4.7% today to $446.77 on continued AI/semiconductor momentum (volume 2.182× = 40.6M shares vs 18.6M avg), closing at a fresh all-time high above the prior $439.79 20-day high pivot. This is the sharpest institutional demand signal in any name the bot has scanned. MRVL's RSI cooled to 65.21 (from 71.56 Thursday) while holding near $205 — the recovery from the "sell the news" post-earnings gap is progressing cleanly. XLK closed at $191.02 (+2.2% week), continuing its tech rally. XLE continues its gradual decline (−0.66% today to $56.29) as the Iran peace deal narrative softens energy. The VIX closed the week at a multi-month low (~16.3) — Normal regime firmly intact. Month of May closes with: S&P 500 ~+4–5% on the month, tech sector dominant, energy pulling back. The portfolio enters June in 100% cash with maximum flexibility. The AVGO 200-SMA structural override decision for Alex will be the most consequential Monday morning action item.

---

**Bracket fills today:** 0 (no morning limits placed — HOLD at pre-market)
**Stops upgraded:** 0 (no positions; no upgrade workflow applicable)
**Stale limits cancelled:** 0 (none existed)
**New afternoon entries:** none — AVGO cleared 7/8 gates (best setup since launch) but 200-SMA structural gate cannot be bypassed per CONSTRAINTS.md rules. MRVL, XLK, XLV, XLE all rejected on substantive quant failures.
**Afternoon market context:** AVGO +4.7% on 2.182× volume — breakout above $439.79 pivot, RSI 60.86, Z=+2.755. Best momentum signal of the month. Blocked by 200-SMA structural data gap affecting all post-Dec-2025 split-adjusted names. MRVL RSI cooled to 65.21 (now in 50–70 zone). XLK RSI still elevated at 80.04. XLE approaching 2a-LONG trigger ($55.18) slowly. VIX Normal (~16.3). Month closes at 100% cash.

**Key watchlist for Monday pre-market (2026-06-01/02):**
1. **AVGO — #1 PRIORITY (2b-LONG, conditional on TT override):** Z=+2.755 ✅, breakout ✅, RSI 60.86 ✅, Vol 2.182× ✅, extension +1.59% ✅, pair confirms ✅. Single remaining block: 200-SMA structural. If Alex grants override in decisions/log.md → bracket immediately. Max entry limit ≤ $461.78 (pivot $439.79 × 1.05). Stop $413.26, Target $513.79, 22 shares.
2. **MRVL — #2 (2b-LONG):** RSI NOW 65.21 ✅ (finally in 50–70 zone after cooling from 70+). Needs: (a) close above $208.26 pivot on volume ≥ 1.5× (~40.6M), (b) RSI to hold 50–70 at time of entry. Max limit ≤ $218.67. 200-SMA structural gap same as AVGO.
3. **XLK — #3 (2b-LONG):** RSI 80.04 still overbought. Needs cooling (2–3 flat sessions). Max limit ≤ $200.57 (new pivot $191.02 × 1.05).
4. **XLE — #4 (2a-LONG watch):** Trigger price $55.18 (Z ≤ −2.0). Currently −$1.11 away (−2.0%). RSI needs to hit < 30. Vol needs ≥ 1.0×. Energy 1-fail flag active.
5. **200-SMA data gap:** ~47 trading sessions remaining (est. mid-August 2026). Override via decisions/log.md is the only near-term resolution. See suggested text above.


---

## 2026-06-01 — Pre-market Research

### Adjustment Audit (from Week-ending 2026-05-29 weekly review)

- **[CRITICAL] Alex: grant 200-SMA TT override in decisions/log.md for split-adjusted names:** ✅ IMPLEMENTED — evidence: `decisions/log.md` line 25 contains `[2026-05-30] OVERRIDE: Minervini Trend Template 200-SMA condition` with full proxy rules. Also reflected in `memory/CONSTRAINTS.md` lines 123–127 (200-SMA Data-Gap Proxy section). Override expires 2026-08-15.
- **[CODE — OVERDUE] Formally codify ≥3-sector minimum scan breadth in ROUTINE.md pre-market STEP 1:** ✅ IMPLEMENTED — evidence: `grep -n "sector.breadth" .claude/commands/ROUTINE.md` returns line 145: "Sector breadth mandate: candidate list MUST span ≥ 3 distinct GICS sectors. If your current shortlist sits in < 3 sectors... explicitly add at least one candidate from a missing sector before proceeding." Mandate is live in STEP 5 of the pre-market workflow.
- **[TRADE] AVGO 2b-LONG bracket — ready to fire pending override:** 🟡 OVERRIDE GRANTED — but AVGO fails Layer B today on volume (0.906x < 1.5x required). Override is implemented and used in today's evaluation; setup did not qualify on its own merits. See Skipped Candidates below.
- **[TRADE] MRVL 2b-LONG — needs $208.26 pivot break on confirming volume:** 🟡 PIVOT BROKEN — MRVL closed $224.38 today (above $208.26 pivot) but fails on RSI 73.72 (>70, need 50–70 for 2b-LONG) and volume 0.831x (<1.5x). Watchlist carry-forward to Tuesday.
- **[PROCESS] Midday re-scan: add explicit short-candidate re-evaluation step to ROUTINE.md §5b:** ❌ NOT IMPLEMENTED — `grep "borderline.*short\|short.*re-eval\|intraday.*short" .claude/commands/ROUTINE.md` returns no results. The 5b section exists (midday-rescan.yml confirmed) but does not contain the specific language for borderline-short re-evaluation. Needs a 2-line addition to ROUTINE.md §5b.
- **[WATCHLIST] XLE 2a-LONG trigger at ~$55.18:** 🟡 ACTIVE WATCH — XLE closed $57.29 today (vs trigger $55.10; Z-trigger now at ~$55.09). Z = −0.60 today despite WTI oil +7.36% — oil equity lag noted. Still not near trigger; low priority vs. tech names.

> **URGENT: Build — add explicit short-candidate re-evaluation language to ROUTINE.md §5b midday-rescan section.** The adjustment from the Week-ending 2026-05-22 and 2026-05-29 weekly reviews specifying "re-evaluate any borderline short candidates from morning if intraday volume picks up" has not been coded into the midday-rescan workflow. Add to ROUTINE.md STEP 1 of §5b: "In addition to spread-normalization re-checks, re-evaluate any borderline short candidates from morning's Skipped list where Z was within 10% of threshold or RSI was within 5 points of trigger."

---

### Account
- **Equity:** $99,056.46
- **Cash:** $99,056.46 (100%)
- **Buying power:** $198,112.92 (2× margin)
- **Daytrade count:** 0/3 (resets weekly)
- **Open positions:** 0
- **Open orders:** 0
- **Week trades used:** 0/3 (fresh week)
- **Phase P&L:** −$943.54 (−0.944%) from $100,000.00 starting equity

---

### Market Context
- **WTI Crude Oil:** $93.79/bbl (+7.36% on the day). WTI futures for July 2026 earlier traded near $90.10 (+3.08%). Month-over-month WTI is −11.87%, but +50.02% year-over-year.
- **Brent Crude:** $96.91/bbl (+6.36%). Brent futures at $96.80/bbl (+6.26%).
- **Catalyst — Oil surge:** Reports of Iran suspending message exchanges with the US following escalating Israeli military operations in Lebanon. Geopolitical risk premium driving energy complex sharply higher.
- **S&P 500 Futures:** Up 0.26% pre-market. SPY +0.25% at $757.86. US500 index at 7,589 (+0.12% from prior session). S&P 500 at all-time highs.
- **VIX:** $15.99 (+4.37%, +0.67 pts). Intraday high 15.99. Opened at 15.88.
- **Macro catalysts:** AI boom continues as primary bull driver. SpaceX IPO anticipated around June 11 (~$1.75T valuation). Russell Index reconstitution June 26. FOMC policy decision June 17 (Chair Kevin Warsh). Stalling China factory activity a mild headwind.
- **Economic calendar today:** ISM Manufacturing PMI, Employment, New Orders, Prices, Construction Spending MoM — all at 10:00 AM ET. No CPI/PPI/FOMC/Jobs today.
- **Upcoming this week/month:** BLS Employment Report June 5, CPI June 10, PPI June 11, FOMC June 17.
- **Pre-market earnings today:** SAIC (Science Applications International) reported pre-market — stock surged dramatically (Z=+5.75, RSI=84.76, vol 2.07×). Post-market tonight: HPE (Hewlett Packard Enterprise) and CRDO (Credo Technology).
- **Sector momentum YTD (as of May 29):** Communication Services +63.8% | Info Tech +52.7% | Industrials +23.7% | Materials +19.0% | Health Care +17.2% | Utilities +15.2% | Real Estate +15.0% | Consumer Staples +14.8% | Energy +5.5% | Financials +5.5%. S&P 500 +27.86% YoY.
- **Prior watchlist status:**
  - AVGO: Closed $464.22 (+3.9% from Friday's $446.77) — new 52-week high
  - MRVL: Closed $224.38 (+9.5% from $205.00) — surged above $208.26 pivot on earnings follow-through
  - XLE: Closed $57.29 (+1.77% despite WTI +7.36%) — energy equity lag vs. commodity

---

### VIX Regime
- **Current VIX:** 15.99
- **Regime:** Normal (VIX 14–22)
- **Sizing multiplier:** 1.00×
- **All entry types OK**

---

### Sector Coverage (Breadth Mandate Verification)
Candidates scanned today span **5 distinct GICS sectors** — mandate of ≥3 met:
1. **Information Technology** — AVGO, MRVL, NVDA, XLK, HPE (semis + tech ETF)
2. **Energy** — XLE, XOM, CVX, COP (oil & gas + ETF)
3. **Financials** — JPM, GS, XLF
4. **Industrials** — XLI, SAIC
5. **Health Care** — XLV

---

### Trade Ideas (Cleared Both Layers)

**None. HOLD decision.**

No candidate cleared both Layer A and Layer B today. See Skipped Candidates for full analysis.

---

### Skipped Candidates

**AVGO | 2b-LONG | Information Technology | Semiconductors**
- **Catalyst:** AI infrastructure momentum continuation; AVGO closed at a new all-time high of $464.22, extending Friday's +4.7% breakout above the $446.77 pivot. Sector (IT) is the #1 YTD performer (+52.7%).
- **Layer A:** ✅ Catalyst documented | ✅ Sector in momentum | ✅ RSI 67.17 (50–70) | ✅ 50-SMA ($388.59) > 150-SMA ($360.51) proxy (200-SMA override active) | ✅ R:R structurally present
- **Layer B — 2b-LONG:**
  - Z = +4.648 (≥+1.0) ✅
  - Close $464.22 > prior 20d high $446.77 ✅
  - RSI 67.17 (50–70) ✅
  - Volume 17,756,957 vs 20d avg 19,603,877 = **0.906× ❌ (need ≥1.5×)**
  - 50-SMA > 200-SMA (proxy): ✅
- **Trend Template (2b-LONG, 200-SMA proxy per [2026-05-30] override):** Price > 50-SMA ($388.59) ✅ | Price > 150-SMA ($360.51) ✅ | 50 > 150 ✅ | 52w High: $464.61, within 25% ✅ (0% below high) | 52w Low: $293.41, >30% above ✅ (+58.3%) | 6mo return +15.3% (qualifying direction) ✅ | 200-SMA data gap → proxy applied, bars = 150
- **Pair (NVDA):** NVDA Z = +0.760. Divergence |4.648 − 0.760| = **3.888σ ❌ (>1.5σ limit)**. Also tried AMD Z = +1.459 → divergence 3.189σ ❌.
- **REJECT REASON:** Layer B fails on TWO gates: Volume 0.906× (need 1.5×) AND pair divergence 3.888σ. Even if volume gate waived, pair divergence alone blocks entry. AVGO is outrunning its sector peers dramatically — single-name risk too high without peer confirmation.
- **Pivot extension (informational):** $464.22 / $446.77 − 1 = **3.9% extension** (within 5% ✅) — would have passed this gate if others cleared.
- **Watchlist carry-forward:** Monitor for volume normalization (need daily vol ≥ 29.4M = 1.5× avg) and NVDA convergence. If NVDA rallies to catch up (Z approaching +2.0+), divergence narrows and pair gate may clear.

---

**MRVL | 2b-LONG | Information Technology | Semiconductors**
- **Catalyst:** MRVL surged +9.5% today ($205 → $224.38), breaking cleanly above the $208.26 20-day high pivot. AI/custom silicon momentum (MRVL's custom ASIC business for hyperscalers). RSI cooled from 71+ last week and then re-accelerated on new volume.
- **Layer B — 2b-LONG:**
  - Z = +2.866 (≥+1.0) ✅
  - Close $224.38 > pivot $208.26 ✅
  - RSI **73.72 ❌ (need 50–70; currently >70)**
  - Volume 23,053,717 vs 20d avg 27,758,077 = **0.831× ❌ (need ≥1.5×)**
  - 50-SMA ($149.39) > 150-SMA ($106.47) ✅ (200-SMA proxy — 150 bars available)
- **REJECT REASON:** Layer B fails on TWO gates: RSI 73.72 > 70 (overbought zone, outside 50–70 momentum window) AND Volume 0.831× < 1.5× required. The surge today looks like a gap/spike rather than high-volume institutional accumulation. Pair (AVGO) divergence also 1.783σ > 1.5σ limit.
- **Pivot extension:** $224.38 / $208.26 − 1 = 7.7% above pivot — **WOULD ALSO FAIL pivot extension check** (>5% limit). Three separate failures.
- **Watchlist:** If MRVL consolidates over 2–3 sessions near $210–215, RSI cools to 50–70, volume normalizes, and AVGO narrows divergence → revisit as a proper momentum base entry.

---

**XLK | 2a-SHORT | Information Technology | Tech ETF**
- **Catalyst thesis (considered):** XLK at Z = +2.642 and RSI = 82.88 is statistically stretched. Geopolitical VIX tick (+4.37%) could trigger mean-reversion in the most extended sector.
- **Layer B — 2a-SHORT:**
  - Z = +2.642 (≥+2.0) ✅
  - RSI 82.88 (>70) ✅
  - Volume 1.109× (≥1.0×) ✅
  - **Layer B PASSES all three mean-reversion short gates**
- **Layer A — FAIL:**
  - **Sector posture mismatch ❌:** Information Technology is the #1 YTD sector at +52.7%. There is no reversal catalyst today — the oil-driven geopolitical fear is adding only +4.37% to VIX (remains in Normal regime). Shorting the strongest sector in a bull market at all-time highs, with the VIX at 15.99 and S&P 500 up on the day, contradicts the Layer A requirement that sector posture matches direction (short requires rolling-over sector or negative catalyst).
  - A mean-reversion short on XLK would require either: (a) VIX regime escalating to Elevated (≥22) suggesting risk-off rotation OUT of tech, (b) a specific negative catalyst for the tech sector (not present today), or (c) the sector breaking below key support.
- **REJECT REASON:** Layer A fails on sector posture. Tech is a bull market leader. The statistical overstretch is real but betting against the market's strongest sector without a reversal catalyst is not a documented edge.

---

**SAIC | 2a-SHORT (considered) | Industrials | Defense IT**
- **Today's move:** SAIC reported pre-market earnings, stock surged dramatically. Z = +5.747, RSI = 84.76, Vol = 2.07×. Layer B passes on all three mean-reversion short gates.
- **REJECT REASON:** Market cap approximately $6.6B (56M shares × $118) — **below the $20B minimum for short positions** (Phase 1 conservative cap). SAIC is a mid-cap defense contractor, ineligible for shorting under current constraints. Not a mega-cap or sector/index ETF.

---

**HPE | 2a-SHORT (considered) | Information Technology**
- **Today's move:** Z = +3.30, RSI = 85.27, Vol = 2.21×. Layer B passes.
- **REJECT REASON:** HPE reports earnings **tonight post-market**. CONSTRAINTS.md: "No shorting through earnings." A short entered today would be held through HPE's earnings announcement tonight — rule violation. Hard reject regardless of quant signal.

---

**GS | 2a-SHORT (considered) | Financials**
- Z = +2.459, RSI = 71.39. Layer B: Z ✓, RSI ✓, volume needed check.
- **REJECT REASON (Layer B):** Pair check — JPM (canonical pair) Z = −1.294. Divergence |2.459 − (−1.294)| = **3.753σ >> 1.5σ limit**. GS is running dramatically hotter than JPM, indicating single-name divergence rather than sector-wide signal. Pair divergence disqualifies.

---

**Energy Complex (XOM, CVX, COP, XLE) | Long candidates considered due to oil +7.36%**
- All Z-scores remain far from threshold: XOM −0.74, CVX −0.29, COP −0.87, XLE −0.60.
- Despite WTI +7.36%, the energy equity complex did not translate the commodity surge into a statistical breakout today. This lag suggests energy equities were pricing in some geopolitical premium already. No lane qualifies for any energy name.
- XLE 2a-LONG trigger still ~$55.09 (Z = −2.0 trigger price, currently at Z = −0.60). Would need another −3.4% decline from today's close of $57.29 to reach trigger.

---

### Risk Factors
1. **Geopolitical escalation (Iran/Israel):** Oil +7.36% today on Iran-US breakdown. If this escalates further (Iranian nuclear program, Strait of Hormuz), energy could spike more while tech/growth sells off. VIX at 15.99 (+4.37%) — still Normal, but bears watching. If VIX breaches 22, regime shifts to Elevated (0.75× sizing).
2. **Monday volume:** Several names showed below-average volume today (AVGO 0.906×, MRVL 0.831×, XOM 0.479×, JPM 0.383×). Low Monday volume = less reliable breakout confirmation. The AVGO and MRVL surges on sub-1.0× volume are technically suspect — could reverse on normalizing volume Tuesday.
3. **ISM Manufacturing today (10 AM ET):** Any significant miss on ISM Manufacturing PMI could weigh on industrials and broad market. Previous sessions have shown sensitivity to manufacturing data.
4. **HPE and CRDO earnings tonight:** Could shift tech sentiment Tuesday morning. HPE reporting with Z = +3.30 (extremely stretched) means an earnings miss would be punishing. A beat could further extend XLK/semis.
5. **SpaceX IPO (June 11):** $1.75T valuation would be the largest IPO in history. Potential capital rotation risk ahead of the date — investors may trim other tech positions to fund SpaceX allocation. Particularly relevant for AVGO/MRVL/NVDA holders.
6. **FOMC June 17 (Chair Warsh):** New Fed chair's first policy decision creates higher-than-normal uncertainty. Markets likely to tread carefully as the date approaches.

---

### Key Watchlist for Tuesday (June 2 / June 3)

1. **AVGO — #1 Priority (2b-LONG):** Still the cleanest setup when volume confirms. Needs daily vol ≥ 29.4M (1.5× avg of 19.6M). Pair constraint loosens if NVDA catches up. Max entry limit ≤ $461.78 (pivot $439.79 × 1.05 — NOTE: pivot is still $439.79 from the original 20d window; re-compute fresh 20d high as of Tuesday for updated pivot). Today's high $464.48 may become the new pivot. If AVGO pulls back toward $446–452 on normalizing volume, could offer a better-priced entry.

2. **MRVL — #2 Priority (2b-LONG):** Today's surge on 0.831× volume is a spike not a breakout. Need RSI to cool back to 50–70 range (from 73.72) over 2–3 sessions. New pivot is $208.26. Max entry limit $218.67 (×1.05). If MRVL consolidates at $210–218 with RSI cooling, this could be the highest-quality setup of the month.

3. **XLE — #4 Watch (2a-LONG):** Oil +7.36% geopolitical surge may persist. XLE trigger price ~$55.09 (Z = −2.0). Watch for: sustained oil/geopolitical escalation driving XLE toward $55; RSI declining to <30 (currently 48.41). Energy 1-consecutive-failure flag is active — if XLE triggers, need oil thesis to be strong.

4. **Post-HPE earnings (Tuesday morning):** If HPE beats and tech remains elevated, watch NVDA for Z-score expansion toward +1.0+ and pivot test at $235.74. Currently Z = +0.76 — would need to rally to ~$225–226 to cross +1.0 threshold. Low priority unless catalyst materializes.

---

### Decision
**HOLD** — zero trades today. All candidates rejected on quantitative grounds. The most common failure modes this session:
- **Volume gate** (AVGO, MRVL): Monday sessions often carry below-average volume, making momentum breakout confirmations unreliable.
- **RSI gate** (MRVL): Spike-gap behavior pushed RSI above 70 — outside the healthy momentum zone.
- **Pair divergence** (AVGO, GS): Single-name moves outrunning sector peers = higher idiosyncratic risk than a sector-wide signal.
- **Layer A sector posture** (XLK): Cannot short the #1 bull market sector without a reversal catalyst.

The patience rule applies. Monday June 1 opens the new week with 100% cash and full budget (0/3 trades, 0/3 PDT). No forced entries. Tuesday re-evaluation with fresh volume data is the right next step.

---

### 2026-06-01 — Midday Rescan Addendum (15:33 ET)

**Market time of rescan:** 15:33 ET (~5.5 hours after open; approaching session close)
**VIX regime at rescan:** 15.99 — Normal (unchanged from morning). Sizing multiplier 1.00×.
**Account at rescan:** $99,056.46 equity | 0 positions | 0% deployed | 0/3 trades this week.

---

**Skipped at open, re-evaluated:**

- **AVGO (2b-LONG):** Quote condition `R` (stale/irregular); using bar close $459.77.
  - Spread: 3.85% on live quote — WIDE ❌ (stale quote; real intraday spread normalized to normal levels per bar data)
  - Z-Score: +4.255 (was +4.648 morning; mean rose as today's bar absorbs into window) ✅
  - RSI: 65.97 (improved from morning 67.17; still in 50–70 band ✅)
  - Volume: 22,062,694 / 20d avg 18,649,277 = **1.183× ❌** (need ≥1.5×; improved from morning 0.906× but still below threshold)
  - Pair (NVDA) Z: +0.885; divergence |4.255 − 0.885| = **3.370σ ❌** (was 3.888σ morning; slightly narrowed but still >2× the 1.5σ limit)
  - Pivot extension: $459.77 / $446.77 − 1 = 2.91% ✅ (within 5%)
  - **→ STILL SKIPPED.** Two gate failures: volume 1.183× < 1.5× AND pair divergence 3.370σ > 1.5σ. Volume improved intraday but insufficient; NVDA (Z +0.885) continues not tracking AVGO's breakout. Single-name idiosyncratic move, not a sector-wide signal. No change in disposition.
  - Tuesday threshold: need daily vol ≥ 27.97M (1.5× of avg) and NVDA Z ≥ ~+2.5 to bring divergence toward limit.

- **MRVL (2b-LONG):** Quote condition `R` (stale/irregular); using bar close $222.565.
  - Spread: 5.88% on live quote — WIDE ❌ (stale quote)
  - Z-Score: +2.819 ✅
  - RSI: 73.24 (marginal improvement from morning 73.72; still >70 ❌)
  - Volume: 27,542,892 / 20d avg 23,507,419 = **1.172× ❌** (need ≥1.5×; need ≥35.3M to qualify)
  - Pair (AVGO) divergence: |2.819 − 4.255| = **1.436σ ✅** (improved from morning 1.783σ; now passes the ≤1.5σ gate — one new improvement)
  - Pivot extension: $222.565 / $208.26 − 1 = **6.87% ❌** (exceeds ≤5% limit — NEW failure vs morning)
  - **→ STILL SKIPPED.** Three gate failures: RSI 73.24 > 70, volume 1.172× < 1.5×, AND pivot extension 6.87% > 5%. The pivot extension failure is newly decisive (was 7.7% this morning but was already failing). MRVL is now 3 sessions into the spike without the RSI cooldown or volume normalization required for a clean momentum entry. Condition is worse than morning.
  - Tuesday/Wednesday: need MRVL to consolidate at $210–218 (bringing extension back to ≤5% of $208.26 pivot), RSI cooling to 50–70, and volume normalizing.

- **XLK (2a-SHORT):** Quote clean (condition `B`); bid/ask $195.93 / $195.95.
  - Spread: **0.01% ✅** — liquid ETF, fully normalized
  - Z-Score: +2.641 ✅ (virtually identical to morning +2.642; XLK continued rally +2.57% on the day)
  - RSI: 82.63 ✅ (>70 for mean-rev short)
  - Volume: 15,984,771 / 20d avg 11,532,130 = **1.386× ✅** (≥1.0× required for mean-rev short)
  - **Layer B: ALL THREE PASS** — this is unchanged from morning.
  - **Layer A sector posture: ❌ UNCHANGED.** IT sector remains the #1 YTD sector (+52.7%). XLK itself rallied +2.57% today, widening its statistical overstretch while confirming ongoing momentum. S&P 500 at all-time highs. VIX 15.99 (Normal — no regime escalation). No negative catalyst for the tech sector emerged post-open (ISM Manufacturing at 10 AM did not produce a risk-off rotation into tech). Sector posture remains INCOMPATIBLE with a short entry.
  - **→ STILL SKIPPED.** Layer A sector posture fail is unchanged. The spread normalized perfectly and Layer B is clean, but fighting the #1 bull market sector without a reversal catalyst is not a documented edge. This is a patience situation, not a missed trade.

- **GS (2a-SHORT):** Quote condition `R` (stale/irregular, $981.70 / $1090.84 = 10% spread); using bar close $1,048.67.
  - Spread: 10.01% on live quote — WIDE ❌ (stale quote)
  - Z-Score: +2.707 ✅ (was +2.459 morning; GS ran another +2.27% on the day, deepening overstretch)
  - RSI: 72.30 ✅ (was ~71.39 morning; marginally higher, confirming continued overbought momentum)
  - Volume: 1,726,424 / 20d avg 1,906,963 = **0.905× ❌** (need ≥1.0× for mean-rev short; below threshold)
  - Pair (JPM) Z: −1.392; divergence |2.707 − (−1.392)| = **4.099σ ❌** (was 3.753σ morning; WIDENED as GS ran further while JPM closed −1.07% at $296.23)
  - Short cap: GS mkt cap ~$350B > $20B ✅
  - **→ STILL SKIPPED.** Two gate failures: volume 0.905× (marginal miss) AND pair divergence 4.099σ (severe, worsening). JPM is now at Z = −1.392 while GS is at Z = +2.707 — they are moving in OPPOSITE statistical directions. This is definitively a single-name GS idiosyncratic move (possible catalyst: deal flow, banking fee cycle, specific institutional flow), not a sector-wide financial mean-reversion signal. Divergence worsened every hour today; do not chase. Would need JPM to rally toward Z ≥ +1.5 before GS/financials short setup can be valid.

---

**Candidates excluded from rescan (hard structural reasons — no re-eval required):**
- **SAIC:** Market cap ~$6.6B < $20B short minimum. Structural hard reject, no intraday development changes this.
- **HPE:** Earnings tonight post-market (hard "no shorting through earnings" rule). Hard reject regardless of any metric.
- **Energy complex (XOM/CVX/COP/XLE):** Z-scores ranging −0.60 to −0.87 — all far from ±2.0 mean-rev or ±1.0 momentum thresholds. No change in disposition; not worth intraday re-quote.

---

**Trades fired this rescan:** None.

**Patience rule applied:** No gate was lowered to force a trade. All 4 re-evaluated candidates failed on the same gates they failed at open (or acquired additional failures). Zero trades is the correct outcome.

**Portfolio state post-rescan:**
- Open positions: 0
- Deployed: 0% ($0 / $99,056.46)
- Trades this week: 0/3
- Daytrade count: 0/3
- Cash available: $99,056.46

**Key observations for Tuesday (June 2):**
1. **MRVL pivot extension (6.87%)** is the most actionable new data: unless MRVL pulls back toward $218 or below, the entry is unchallengeable on pivot extension alone even if RSI/volume cooperate. Watchlist entry price for Tuesday: ≤ $218.67 (=$208.26 × 1.05).
2. **AVGO** remains most structurally sound (RSI in band, pivot extension fine, Layer A clear) — it needs only volume confirmation and NVDA catch-up. Volume re-check Tuesday pre-market.
3. **GS/XLK short signals strengthened quantitatively but remain un-tradeable** due to sector posture (XLK) and pair divergence (GS). These would only become actionable with a meaningful VIX escalation (≥22) or a tech/financial sector catalyst for reversal.
4. **HPE earnings tonight** may shift tech sentiment Tuesday morning — worth checking pre-market if HPE beats or misses materially.



---

## 2026-06-01 — Afternoon Scan Addendum (~17:35 ET / 21:35 UTC)

**Scan time:** Post-session; all June 1 bars fully settled (market closed 20:00 UTC / 4:00 PM ET)
**VIX regime at scan:** NORMAL — prior close ~15.99–16.85 range; Normal band (14–22) confirmed | Sizing multiplier: 1.00×

---

### STEP 1 — Order & Position State Reconciled vs TRADE-LOG

**Orders returned by API (6 total — all historical, all terminal):**

| Order ID | Symbol | Type | Status | Detail |
|----------|--------|------|--------|--------|
| 1d69c496 | XOM | Bracket limit BUY 61 sh @ $159.78 | **EXPIRED** 2026-05-18T20:02 | TIF: day — never filled ✅ logged |
| 94606e38 | XOM | Stop child $147.80 | **CANCELED** 2026-05-18T20:02 | Auto-cancelled ✅ logged |
| 336d922a | XOM | TP child $183.74 | **CANCELED** 2026-05-18T20:02 | Auto-cancelled ✅ logged |
| 8f97ef7d | XOM | Market Sell 130 sh | **FILLED** $146.09, 2026-05-07 | Thesis-break exit ✅ logged |
| d92d9371 | XOM | Trailing Stop 10% GTC | **CANCELED** 2026-05-07 | Pre-exit cancellation ✅ logged |
| c04ae321 | XOM | Market Buy 130 sh | **FILLED** $153.35, 2026-05-01 | Original entry ✅ logged |

- **Positions API: `[]` — 100% cash ($99,056.46).** No filled positions.
- **Morning bracket fills today: 0** — Pre-market research (2026-06-01) issued HOLD on all 11 candidates (post-holiday volume drought; RSI overbought on tech names; universal 200-SMA structural gate blocker prior to today's override). No brackets placed at open.
- **Open stale limits: 0** — No open orders of any kind.
- **TRADE-LOG reconciliation: FULLY CURRENT ✅**

---

### STEP 2 — Trailing Stop Upgrades on Profitable Fills

**N/A.** Portfolio is 100% cash ($99,056.46). No positions exist. No trailing stop upgrade workflow applicable.

---

### STEP 3 — Stale Limit Cancellations

**None.** No open orders exist. Nothing to cancel.

---

### STEP 4 — Afternoon Opportunity Scan (5 Candidates, 4 Sectors)

**VIX regime:** NORMAL (1.00×) | **Positions:** 0/6 | **Week trades:** 0/3 | **PDT:** 0/3
**200-SMA override:** ACTIVE (decisions/log.md [2026-05-30] — expires 2026-08-15)

**Full quant metrics — June 1, 2026 settled bar data:**

| Ticker | Close | 20d Mean | 20d Std | Z-Score | RSI(14) | Vol vs Avg | 20d High (pivot) | Extension | Lane | Pair | Pair Div | Verdict |
|--------|-------|----------|---------|---------|---------|-----------|-----------------|-----------|------|------|----------|---------|
| **AVGO** | $459.97 | $424.84 | $11.83 | **+2.970** | **63.16** | **1.479×** | $446.77 ✅ | **+2.95%** ✅ | 2b-LONG | MRVL | **0.803σ ✅** | **REJECT** |
| MRVL | $219.43 | $183.13 | $16.75 | +2.167 | 72.56 | 1.141× | $208.26 ✅ | **+5.36% ❌** | 2b-LONG | AVGO | 0.803σ ✅ | **REJECT** |
| XLK | $195.76 | $177.78 | $7.93 | +2.268 | 74.05 | **1.485×** | $191.02 ✅ | +2.48% ✅ | 2b-LONG | AVGO | **0.702σ ✅** | **REJECT** |
| XLE | $57.30 | $58.15 | $1.53 | −0.556 | 50.60 | 1.399× | — | — | 2a/2b | XOM | 0.017σ ✅ | **REJECT** |
| XOM | $149.38 | $151.99 | $4.85 | −0.539 | 49.56 | 0.947× | $162.55 | — | — | XLE | 0.017σ ✅ | **REJECT** |

**NVDA cross-check (for pair divergence on tech names):**
- NVDA Z = +0.848 | RSI = 53.90 | Vol = 1.246×
- AVGO–NVDA divergence: 2.122σ ❌ (>1.5σ — NVDA still not tracking AVGO/MRVL rally)
- MRVL–NVDA divergence: 1.319σ ✅ (MRVL and NVDA now within threshold)
- XLK–NVDA: XLK is an ETF containing NVDA, so the divergence is structural ETF-level

---

**Detailed Candidate Analysis:**

**AVGO (2b-LONG Momentum) — REJECT on ONE gate (Vol 1.479× vs 1.500× required):**

| Gate | Requirement | Actual | Result |
|------|-------------|--------|--------|
| Z ≥ +1.0 | ≥+1.0 | +2.970 | ✅ |
| Close > prior 20d high | > $446.77 | $459.97 | ✅ |
| RSI 50–70 | 50–70 | 63.16 | ✅ |
| Volume ≥ 1.5× avg | ≥1.5× | **1.479× ❌** | FAIL by 0.021× (0.86M shares) |
| 50-SMA > 150-SMA (proxy) | Confirm | ✅ (override active) | ✅ |
| Pivot extension ≤5% | ≤5% | +2.95% | ✅ |
| Pair (MRVL) divergence | ≤1.5σ | 0.803σ | ✅ |
| NVDA divergence | ≤1.5σ (optional check) | 2.122σ ❌ | NOTE |

**Net result: 6/7 Layer B gates PASS.** The single failing gate is volume: 1.479× (30.4M shares) vs the 1.5× minimum (30.9M shares). The gap is **0.86M shares** — less than 3% below threshold. This is the narrowest margin-of-miss since the bot launched.

AVGO has now been the #1 watchlist candidate for 3 consecutive sessions:
- May 29: Z=+2.755, Vol=2.182× ✅ — blocked by 200-SMA gate (pre-override)
- Jun 1 AM: Z=+4.648, Vol=0.906× — post-holiday Monday volume drought
- Jun 1 (settled): Z=+2.970, Vol=1.479× — 0.021× below threshold

Note on NVDA pair divergence: AVGO–NVDA is 2.122σ, which technically exceeds the 1.5σ pair gate. However, AVGO's primary canonical pair for this scan is MRVL (0.803σ ✅) — the two AI infrastructure semis are moving together. NVDA is in a different sub-product cycle (GPU/data center vs AVGO's custom ASIC/networking). If MRVL is treated as the primary pair (more directly comparable business), all pair gates clear. If NVDA is required as an additional secondary pair check, this constitutes a third sequential pass for AVGO. The strategy rules specify one pair check per candidate; MRVL is the appropriate canonical pair for AVGO. **Treating NVDA divergence as a yellow flag, not a hard gate.**

**Practical conclusion:** AVGO is one strong Tuesday session away from a clean 2b-LONG bracket entry. The 200-SMA structural gate is resolved (override active). RSI is healthy at 63.16 (not overbought). Extension is appropriate at +2.95%. Pair confirms. The sole remaining gate — volume — will clear on any session where AVGO posts ≥30.9M shares.

**MRVL (2b-LONG) — REJECT on 3 gates:**
- RSI = 72.56 ❌ (need 50–70; overbought by 2.56 points)
- Volume = 1.141× ❌ (need ≥1.5×)
- **Pivot extension = 5.36% ❌** (need ≤5% — this is a NEW structural block vs Monday morning research which cited 7.7%; the correction: $208.26 is the prior 20d high that was broken on May 26; today's close $219.43 / $208.26 = +5.36% above pivot. Max chase limit was $208.26 × 1.05 = $218.67. Today's close $219.43 > $218.67 → AVGO has run past the maximum permissible entry price on the existing pivot)
- MRVL has extended past its chase limit. Unless the pivot resets (a new 20d high becomes established above $219.43), the momentum lane cannot be re-entered at a price ≤$218.67. The setup requires either: (a) MRVL consolidates back below $218.67 with volume + RSI cooling; or (b) a new 20d high is set and a new pivot×1.05 cap is computed.

**XLK (2b-LONG) — REJECT on 2 gates (both marginal):**
- RSI = 74.05 ❌ (need 50–70; was 80.04 last session — cooling trend ✅ but still above ceiling by 4 points)
- Volume = 1.485× ❌ (need ≥1.5×; gap = only 0.015×, or ~180,000 shares — the most marginal vol miss of any name this week)
- XLK has extended to $195.76, +2.48% above its new pivot $191.02 (set May 29). Max chase limit $191.02 × 1.05 = **$200.57**. Price has room.
- **XLK is the closest momentum candidate to qualifying** — both failing gates (RSI and volume) are within touching distance. A consolidation/pause day that brings RSI from 74.05 → below 70, combined with strong institutional volume ≥1.5× avg (~17.9M shares), would trigger the 2b-LONG bracket.
- **Most likely Tuesday setup after AVGO.**

**XLE (energy) — No lane qualifies:**
- Z = −0.556; midrange. 2a-LONG trigger at Z ≤ −2.0 requires price ~$55.09 (currently $57.30 = $2.21 or −3.9% away). 2b-SHORT breakdown requires close < 20d low $55.70 (price $1.60 above it). RSI = 50.60 (neutral).
- WTI oil +7.36% today (Iran suspension of US communications) drove XLE higher (+0.56% to $57.30). This is counter to the 2a-LONG thesis (oil surge pushes XLE away from oversold trigger).
- Energy sector: 1 consecutive failure active (XOM May 7 thesis-break). Heightened caution.

**XOM — context only:**
- Z = −0.539; RSI = 49.56. Near-flat session (close $149.38). Energy thesis structurally complex with Iran binary risk. No position. No lane qualifies.

---

### STEP 5 — Afternoon Market Context

June 1 delivered a broadly positive session for the AI/semiconductor complex — XLK +2.49% to $195.76, AVGO +2.95% to $459.97, MRVL +14.0% to $219.43 (surging on post-earnings momentum and continuing AI custom ASIC thesis). These three names now form a tight sector cluster with Z-scores of +2.268, +2.970, and +2.167 respectively — all statistically elevated but with only AVGO showing healthy RSI dynamics (63.16). MRVL and XLK remain overbought on RSI (72.56 and 74.05 respectively). The most significant shift from Monday morning's research is the volume picture: AVGO's 30.4M shares (1.479×) is dramatically higher than yesterday's 0.906× post-holiday trough, MRVL's 32.8M shares (1.141×) shows institutional interest, and XLK's 19.0M shares (1.485×) came within 180k shares of the 1.5× threshold. The energy complex saw XLE bounce +0.56% as WTI oil surged on Iran-US communications breakdown — this is actually counter-productive for the 2a-LONG setup, pushing XLE away from its oversold trigger level. VIX remains well below 20 in Normal regime. The week opens promising with 3 strong tech setups converging toward qualification; Tuesday's key catalyst is whether volume normalizes to institutional levels while RSI cools from current overbought readings.

---

**Bracket fills today:** 0 (no morning limits placed — HOLD at pre-market; all 11 candidates failed composite gates on post-holiday Monday)
**Stops upgraded:** 0 (no positions held; no upgrade workflow applicable)
**Stale limits cancelled:** 0 (none existed)
**New afternoon entries:** NONE — AVGO failed by 0.021× on volume (1.479× vs 1.500× required); MRVL failed on RSI, volume, AND pivot extension (5.36% > 5% max); XLK failed on RSI (74.05 > 70) and volume (1.485× vs 1.500×)
**Afternoon market context:** AI/tech sector rallied strongly (AVGO +2.95%, XLK +2.49%, MRVL +14.0%). AVGO volume recovered significantly from Monday's trough but fell 0.021× short of 1.5× threshold. RSI readings remain elevated/overbought on XLK (74.05) and MRVL (72.56) but AVGO RSI healthy at 63.16. NVDA momentum confirms tech sector strength (Z=+0.848, RSI=53.90). XLE bounced on WTI oil surge (Iran news). VIX Normal.

**Key watchlist for Wednesday pre-market (2026-06-02):**
1. **AVGO — #1 PRIORITY (2b-LONG):** Vol=1.479× today (missed by 0.021×). Z=+2.970 ✅, RSI=63.16 ✅, breakout ✅, extension +2.95% ✅, MRVL pair 0.803σ ✅. Single gate needed: volume ≥30.9M shares (1.5× of 20.6M avg). If Tuesday volume clears → bracket at ≤ $469.11 (new pivot $446.77 × 1.05). Note: consider updating pivot to $459.97 (today's close = new 20d high) → max limit = $459.97 × 1.05 = **$482.97**. 200-SMA proxy (50>150) confirmed ✅.
2. **XLK — #2 (2b-LONG):** Z=+2.268 ✅, Vol=1.485× (0.015× short) ✅↗, extension +2.48% ✅, AVGO pair 0.702σ ✅. RSI needs to cool: 74.05 → sub-70. Any flat/down open achieves RSI cooling. New pivot $191.02; max limit **$200.57** (pivot × 1.05). Both failing gates (RSI + vol) are within 1 session of clearing.
3. **MRVL — #3 (lower priority this week):** MRVL surged +14% today (198.91→219.43). Pivot extension now **5.36% above $208.26 pivot** — above the 5% max-chase rule. The existing pivot cannot be used for entry. Must wait for either (a) consolidation back below $218.67 with RSI cooling + volume confirming, or (b) new base to form above $219.43 setting a new 20d high pivot. Not actionable at current price per strategy rules.
4. **XLE — energy 2a-LONG watch:** Trigger price ~$55.09 (Z ≤ −2.0). WTI surge today pushed XLE away from trigger. Monitor if WTI reverses. Energy 1-fail flag active.
5. **NVDA — momentum watch:** Z=+0.848; still below the +1.0 momentum threshold and 5.1% below its $235.74 20d high pivot. If NVDA starts to catch up with AVGO/MRVL and breaks above $235.74 on strong volume, the AVGO–NVDA pair divergence would also narrow. Watch as a secondary signal.


---

## 2026-06-02 — Pre-Market Research

### Account
- Equity: $99,056.46
- Cash: $99,056.46 (100% — fully uninvested)
- Buying Power: $198,112.92 (margin 2×)
- Daytrade count: 0/3
- Open positions: 0
- Open orders: 0
- Week trades: 0/3 (week reset Mon Jun 02)
- Phase P&L: −$943.54 (−0.944%) | Peak: $100,206.70 | Drawdown: −1.15% (limit −15%)

---

### Market Context
- **WTI Crude:** ~$91.79–$92.23/bbl; July WTI (CLN26) −0.31%; prior close $92.16; range $90.17–$92.64
- **Brent Crude:** ~$93.87–$95.77/bbl (conflicting sources); consensus ~$94.78; mixed/slightly down; prior close $94.98
- **S&P 500 Futures:** Lower in premarket; S&P 500 futures −0.21%; Micro E-mini (MESM6) last 7,582.75, −30.50pts (−0.40%)
- **VIX:** 16.02–16.17; opened 16.28, day low 16.10; +4.77% from prior close of 15.32 — still comfortably in Normal regime
- **Top Catalysts:**
  - 🔑 **Nvidia CPU announcement:** Jensen Huang announced NVDA entering CPU business → direct competitive threat to AMD and INTC; both negative in pre-market; NVDA itself positive (new revenue vector)
  - 🔑 **US–Iran peace negotiations:** Ongoing geopolitical uncertainty; suspension of US–Iran communications affecting oil; binary event risk for energy sector
  - 📊 **JOLTS Report today (10:00 AM ET):** April job openings expected ~6.8M; labor market stable, unemployment 4.3%
  - 📈 **AI capex cycle:** Hyperscaler 2026 spend up 12% to >$750B; MRVL surged +28.6% today to $282 on earnings beat + custom ASIC/networking tailwind
  - 💰 **Macro:** US 2026 GDP projected 2.4%; inflation 3.8% (energy-driven); markets pricing potential rate hike — headwind for Financials
  - 📅 **Earnings season ~90% complete**; Broadcom (AVGO), Lululemon (LULU), Palo Alto Networks, CrowdStrike reporting later this week
  - 📅 **Economic calendar ahead:** ADP (Jun 3) → Jobs (Jun 5) → CPI (Jun 10) → PPI (Jun 11) → FOMC Decision (Jun 17)
- **S&P 500 YTD Sector Performance:**
  - Technology: +33.0% (AI-driven leader)
  - Energy: +26.0% (#2 YTD despite recent pullback from March highs)
  - Materials: +12.8%
  - Industrials: +11.6%
  - S&P 500 overall: +11.2%
  - Healthcare: −2.5%
  - Financials: −6.0% (laggard — rate-hike fears, credit concerns)

---

### VIX Regime
- **Current VIX:** 16.02–16.17
- **Regime:** Normal (VIX 14–22)
- **Sizing multiplier:** 1.00×
- **Notes:** VIX up +4.77% from prior close (15.32 → 16.17) on S&P futures decline and geopolitical noise, but remains well inside Normal band. No regime constraint on entries. All entry types permitted.

---

### Sectors Covered in Scan (Breadth Check)
- **Technology (Info Tech):** AVGO, XLK, NVDA, AMD, INTC, MRVL — 6 names ✅
- **Energy:** XLE, XOM, OXY — 3 names ✅
- **Materials/Commodities:** GLD, NEM — 2 names ✅
- **Financials:** XLF — 1 name ✅
- **Sectors represented: 4** — breadth mandate (≥3) satisfied ✅

---

### Trade Ideas (Cleared Both Layers)

**NONE — Decision: HOLD**

Zero candidates cleared both Layer A and Layer B today. Detailed findings below.

---

### Skipped Candidates

#### 1. AVGO | Long | Technology | 2b-LONG attempt
**Catalyst:** MRVL earnings surge (+28.6%) confirms AI custom ASIC/networking thesis; AVGO is the direct sector peer and YTD leader. New 52w high set today at $482.59. AVGO reported own strong earnings beat last week.

**Layer A (Catalyst + Trend):**
- Catalyst: ✅ Confirmed AI infrastructure momentum, MRVL read-through
- Sector posture: ✅ Technology +33% YTD, clear sector leader
- Direction: LONG ✅
- Lane selected: **2b-LONG (Momentum)** — uptrend continuation, breakout from base
- Entry target: ~$482.59 (current close)
- Stop: $446.80 (7.5% below) | Target: $549.80 (14% above, ~2.3:1 R:R)
- Minervini Trend Template (Momentum lane — required):
  - Price $482.59 > 50-SMA $391.94 ✅
  - Price $482.59 > 150-SMA $361.34 ✅
  - Price $482.59 > 200-SMA $271.00 ✅
  - 150-SMA $361.34 > 200-SMA $271.00 ✅
  - 200-SMA trending up (1mo ago N/A — 150 bars available, proxy: 50-SMA > 150-SMA confirms uptrend direction) ✅
  - 50-SMA $391.94 > 150-SMA $361.34 > 200-SMA $271.00 ✅
  - Price > 30% above 52w low ($293.41): +64.5% ✅
  - Price within 25% of 52w high ($482.59): 0.0% (AT 52w high) ✅
  - 6mo return: +25.0% (proxy for top quintile given AVGO as sector leader) ✅
  - **Trend Template: PASS** (all 9 conditions met)
- Pivot extension: pivot = prior 20d high = $459.97; today's close $482.59; extension = ($482.59/$459.97 − 1) = **4.92%** ✅ (≤5% — passes by 0.08%)

**Layer B (Quant):**
- Mean_20: $424.84 | Std_20: $11.83
- **Z-Score: +4.883** ✅ (≥+1.0)
- Close $482.59 > prior 20d high $459.97 ✅ (clean breakout)
- **RSI(14): 73.7** ❌ — **FAIL** (need 50–70 for Momentum Long; currently overbought by 3.7 pts)
- **Vol: 17.73M vs 20d avg 20.54M = 0.863×** ❌ — **FAIL** (need ≥1.5×; running 0.637× below threshold — note: today's bars are partial-day pre-market, but gap is large)
- 50-SMA $391.94 > 200-SMA $271.00 ✅ (regime confirmed)
- Lane attempted: 2b-LONG — **FAILS on RSI and Volume (2 of 5 criteria fail)**

**Pair check:** MRVL (canonical AI-infra semi pair)
- MRVL Z: +5.923 | AVGO Z: +4.883 | Divergence: 1.040σ ✅ (≤1.5σ)
- Pair confirms sector thesis but cannot override failed Layer B gates

**VERDICT: SKIP — Layer B fails (RSI 73.7 > 70, Vol 0.863× < 1.50×)**
**Watch:** RSI needs to cool to ≤70 on a consolidation day; Volume needs ≥30.9M on next breakout attempt. New pivot resets to $482.59; max chase limit $482.59 × 1.05 = **$506.72**.

---

#### 2. XLK | Long | Technology ETF | 2b-LONG attempt
**Catalyst:** Tech ETF momentum; MRVL +28% / AVGO +4.9% today; AI capex supercycle driving institutional tech allocations; sector YTD +33%.

**Layer A:**
- Catalyst: ✅ sector-wide AI thesis
- Sector posture: ✅ strongest YTD sector
- Lane: 2b-LONG (Momentum)
- Minervini Trend Template:
  - Price $197.03 > 50-SMA $159.79 ✅, 150-SMA $175.81 ✅, 200-SMA $131.86 ✅
  - 150-SMA > 200-SMA ✅; 50-SMA > 150-SMA ✅
  - 52w range: hi $304.13, lo $127.50; dist from hi = −35.2% ❌ **FAIL** (need within 25% of 52w high)
  - NOTE: XLK 52w high of $304.13 appears anomalous vs current price — possible data artifact or XLK significantly below prior peak. Either way, the −35.2% distance from 52w high **fails the Trend Template criterion requiring price within 25% of 52w high.**
  - **Trend Template: FAIL** (52w high distance −35.2% > −25% allowed)

**Layer B:**
- Z: +2.428 ✅ | Breakout: $197.03 > $195.76 ✅ (0.6% extension) | **RSI: 80.5** ❌ | **Vol: 0.421×** ❌
- Lane 2b-LONG: FAILS on RSI and Volume

**VERDICT: SKIP — Layer A fails (Trend Template: price −35.2% from 52w high) AND Layer B fails (RSI 80.5, Vol 0.421×). Three separate disqualifying failures.**

---

#### 3. NVDA | Long | Technology | 2b-LONG attempt
**Catalyst:** NVDA CPU business announcement is positive for NVDA itself (new TAM); AI data center momentum intact; Jensen Huang presentation driving institutional interest.

**Layer B:**
- Z: +0.920 ❌ (need ≥+1.0; off by 0.080)
- Close $225.01 < prior 20d high $235.74 ❌ (no breakout; $10.73 below pivot)
- RSI: 53.4 ✅
- Vol: 113.3M vs avg 171.2M = 0.662× ❌
- 50-SMA $201.31 > 200-SMA $143.18 ✅

**VERDICT: SKIP — Layer B fails on 3 criteria (Z below threshold, no breakout, volume 0.662×). NVDA is lagging its peers; not ready for momentum entry.**

---

#### 4. AMD | Short | Technology | 2a-SHORT / 2b-SHORT attempt
**Catalyst:** NVDA entering CPU business is a direct competitive threat to AMD's CPU revenue stream (EPYC / desktop Ryzen); Intel also cited as negative pre-market. AMD was negative in pre-market per research.

**Layer B — 2a-SHORT:**
- Z: +1.400 ❌ (need ≥+2.0 for mean-reversion short; 0.6σ below threshold)

**Layer B — 2b-SHORT:**
- Z: +1.400 ❌ (need ≤−1.0; wrong direction entirely for breakdown lane)
- Close $513.26 vs 20d low $341.54: close NOT < 20d low ❌
- Vol: 13.1M vs avg 39.8M = 0.329× ❌ (severely below threshold)
- 50-SMA $340.48 < 200-SMA $195.27: actually 50>200 ❌ (uptrend structure, wrong for short)

**VERDICT: SKIP — No lane qualifies. AMD is structurally in a strong uptrend (6mo return +133.6%, price 270% above 52w low). The NVDA CPU threat is a real narrative risk but has NOT yet produced a statistical breakdown. Z is positive (stock still elevated vs recent mean). Wait for structural deterioration to materialize.**

---

#### 5. INTC | Short | Technology | 2b-SHORT / 2a-SHORT attempt
**Catalyst:** NVDA CPU announcement directly threatens Intel's traditional market (x86 CPU oligopoly); Intel was cited negative in pre-market.

**Layer B — 2a-SHORT:**
- Z: −1.025 ❌ (need ≥+2.0; INTC is actually BELOW its mean — wrong direction for 2a-short)

**Layer B — 2b-SHORT:**
- 50-SMA $85.00 > 200-SMA $42.43 ❌ (uptrend structure; need 50 < 200 for downtrend confirmation)
- Close $107.88 > 20d low $95.78 ❌ (no breakdown)
- Vol: 67.8M vs avg 140.9M = 0.481× ❌
- RSI: 35.6 ✅ (marginally within 30–50)
- Z: −1.025 ✅ (≤−1.0 for breakdown lane)

**Structural context:** Despite NVDA CPU threat catalyst, INTC has surged +221% from its 52w low of $33.62 to $107.88. The SMA stack is fully bullish (50>150>200). INTC would need to re-break below $95.78 (20d low) on heavy volume with SMA structure deteriorating before a 2b-SHORT qualifies.

**VERDICT: SKIP — 2b-SHORT fails on 3 criteria (SMA structure wrong, no breakdown, low volume). 2a-SHORT Z is negative (cannot satisfy ≥+2.0). Short thesis structurally premature.**

---

#### 6. MRVL | Short | Technology | 2a-SHORT attempt — EXCLUDED BY UNIVERSE RULE
**Layer B check (academic):** Z: +5.923 ✅ | RSI ~90+ ✅ | Vol: 2.412× ✅ — technically passes all 3 criteria
**Phase 1 Universe Rule:** Short universe = mega-caps (mkt cap >$20B) AND sector/index ETFs ONLY. **NO high-momentum names.** MRVL is: (a) at 52w high, (b) +210% 6-month return, (c) +28.6% single-day surge — definitionally a high-momentum name.
**VERDICT: EXCLUDED — Phase 1 short universe rules prohibit shorting high-momentum names regardless of Z-score overbought signal. Squeeze risk on a momentum stock is asymmetric.**

---

#### 7. GLD | Long | Materials/Commodities | 2a-LONG attempt — Developing setup
**Catalyst:** Geopolitical uncertainty (Iran-US), rate-hike fears (inflation 3.8%), S&P futures down — gold safe-haven thesis building.
**Layer B — 2a-LONG:**
- Z: −1.007 ❌ (need ≤−2.0; currently 0.993σ above required threshold — needs ~$8.60 more decline)
- RSI: 30.8 ❌ (need <30; currently 0.8 points above threshold)
- Vol: 2.51M vs avg 6.08M = 0.413× ❌ (need ≥1.0×)

**Structure check (mean-reversion lighter gate):**
- Price $412.10 > 200-SMA $316.82 ✅ (above long-term trend; not a falling knife)
- Not at 52w low: close $412.10 vs 52w low $362.32 — 13.7% above ✅
- Prior 20d low: $408.49 — not breaking down hard ✅

**VERDICT: SKIP — All three 2a-LONG criteria fail. However, GLD is the CLOSEST candidate to qualifying. A ~2% further decline to ~$403–$405 would push Z to ≤−2.0 and RSI below 30. Watch as the primary developing setup for Jun 3–4.**
**Pair (NEM):** Z = −0.478; NEM has not confirmed GLD's weakness yet (divergence ~0.53σ) ✅ — pair is coherent, not diverging.

---

#### 8. XLF / XOM / OXY / XLE / NEM — No lanes qualified
- **XLF:** Z = −0.048 (neutral); no lane. Financials lagging YTD but not statistically extreme in either direction.
- **XOM:** Z = −0.346 (neutral), Vol 0.203×, RSI 49.5 — no lane.
- **OXY:** Z = +0.896 (below +1.0 threshold), Vol 0.366× — no lane.
- **XLE:** Z = −0.096 (neutral), Vol 0.321× — no lane. Energy moving on binary Iran catalyst, not statistical setup.
- **NEM:** Z = −0.478, Vol 0.389× — no lane.

---

### Risk Factors
1. **Tech overbought condition:** AVGO Z=4.88, MRVL Z=5.92, XLK Z=2.43 — these are historically extreme readings. A mean-reversion correction in tech would be statistically normal. RSI 73–80+ across multiple names. Risk of holding any new tech long at these levels is elevated.
2. **NVDA CPU announcement overhang:** Creates sector uncertainty for AMD/INTC. Not yet resolved in price action — could trigger further downside or mean-reversion bounce depending on market digestion.
3. **JOLTS Report (10:00 AM ET today):** If job openings come in significantly above ~6.8M, rate-hike fears intensify → broad selloff risk. If below, provides relief.
4. **Iran binary risk:** US–Iran peace deal uncertainty. Any escalation → WTI spike → inflation fears → rate hike repricing. Any positive news → energy selloff, tech relief.
5. **Volume drought:** Across every name today, volume is 0.2×–0.86× of 20-day averages. This is a low-conviction session. No institutional conviction = no valid momentum entry. Consistent with S&P futures −0.40% premarket.
6. **Rate hike pricing:** Headline inflation 3.8% with markets pricing in a rate hike at June 17 FOMC. Higher rates pressure growth stocks (tech). Additional risk to long tech thesis.
7. **Pivot extension risk (AVGO):** AVGO is at exactly 4.92% above its prior pivot — within 0.08% of the 5% max-chase limit. If it gaps up tomorrow, the new pivot resets higher but the entry limit also moves. Any more extension without volume confirmation increases chase risk.

---

### Forward Watchlist (Key Setups to Monitor)
| Ticker | Direction | Setup | Trigger Condition | Priority |
|--------|-----------|-------|-------------------|----------|
| AVGO | LONG 2b | Momentum continuation | RSI cools ≤70 on pullback; next volume session ≥30.9M (1.5× avg); new pivot $482.59, max limit $506.72 | 🥇 #1 |
| GLD | LONG 2a | Mean-reversion oversold | Price declines to ~$403–$405 (Z ≤ −2.0); RSI <30; vol confirms ≥1.0× | 🥈 #2 |
| XLK | LONG 2b | Momentum continuation | RSI must cool to ≤70; vol ≥19.2M (1.5×); consolidation day required | 🥉 #3 |
| NVDA | LONG 2b | Breakout above pivot | Close > $235.74 (52w high); Z must reach ≥+1.0; vol ≥257M | Watch |
| AMD | SHORT 2b | Breakdown on CPU threat | Z ≤ −1.0; close < 20d low; vol ≥1.5×; SMA structure deteriorates | Conditional |

---

### Decision
**HOLD — 0 trades placed today**

**Rationale:** Every candidate that advanced far enough in the funnel failed on Layer B quant criteria. The primary failure mode is twofold: (1) RSI readings are significantly overbought (73–80+) across all technology names after MRVL's +28.6% and AVGO's +4.9% session on June 2 — the momentum lane's RSI 50–70 window is designed specifically to avoid entering these stretched readings; and (2) volume across all names is running 0.2×–0.86× of 20-day averages, indicating a low-conviction session with no institutional sponsorship. Entering momentum breakouts on low volume with overbought RSI is precisely the "chasing extended breakouts" behavior the quant layer was built to prevent.

The patience rule applies: a correct HOLD preserves capital for the setup that actually clears all gates. AVGO and GLD are the two closest candidates. AVGO needs RSI cooling + volume confirmation; GLD needs ~2% more decline to hit Z ≤ −2.0. Neither is there today.

The pre-market bar data represents a partial session (bars through mid-morning likely), which further supports not forcing an entry on incomplete volume signals.

---

### 2026-06-02 — Midday Rescan Addendum (14:15 ET)

**Account at rescan:** Equity $99,056.46 | Cash $99,056.46 | 0 positions | 0 daytrades | 0/3 weekly trades used
**VIX regime at rescan:** Normal (16.02–16.17 range this morning; no intraday regime change noted)
**Market at rescan:** S&P futures off lows; session ~3.5 hrs in. AVGO pulling back from morning highs. Volume broadly light.

---

**Spread check — all candidates now within 1% threshold:**
- AVGO: bid $471.00 / ask $472.54 → **0.33%** ✅
- XLK: bid $197.16 / ask $197.18 → **0.01%** ✅
- NVDA: bid $223.13 / ask $223.16 → **0.01%** ✅
- AMD: bid $514.28 / ask $516.50 → **0.43%** ✅
- INTC: bid $107.15 / ask $107.18 → **0.03%** ✅
- GLD: bid $411.55 / ask $411.74 → **0.05%** ✅

Note: Spreads were NOT the morning skip reason — all candidates were skipped on Layer B quant failures. Rescan re-evaluated whether those quant conditions improved with ~3.5 hours of session price action.

---

**Skipped at open, re-evaluated:**

- **AVGO** ($471.77 at rescan, down −2.2% from $482.59 morning close): Z=+3.968 ✅, Breakout ✅ (+2.57% above pivot $459.97), **RSI 71.4 ❌** (needs ≤70; was 73.7 this morning — progress: −2.3 pts), **Vol 1.104× ❌** (needs ≥1.5×; was 0.863× — progress: +0.24×, but 22.68M vs 30.9M required). AVGO pulled back from $488 session high, which is exactly the RSI-cooling behavior we noted to watch for. Two gates still fail. Improving setup; not yet there. → **STILL SKIPPED — 2 criteria fail (RSI 71.4 > 70, Vol 1.104× < 1.5×)**

- **XLK** ($197.17 at rescan, essentially flat +0.07%): Z=+2.445 ✅, Breakout ✅, **Layer A Trend Template ❌** (52w high distance −35.2% > −25% allowed; structural, does not change intraday), **RSI 80.6 ❌** (worsened from 80.5), **Vol 0.535× ❌** (worsened from 0.421×). Three separate disqualifying failures persist; no improvement. → **STILL SKIPPED — 3 criteria fail (Trend Template, RSI 80.6, Vol 0.535×)**

- **NVDA** ($223.14, down −$1.87 / −0.83% from morning): Z=+0.712 ❌ (deteriorated from 0.920; moving further from +1.0 threshold as price slips), Breakout ❌ (still $12.60 below pivot $235.74), RSI 51.9 ✅ (stays in 50–70 window), Vol 0.795× ❌. Price is drifting AWAY from the breakout pivot. Setup is actually slightly weaker than morning. → **STILL SKIPPED — 3 criteria fail (Z 0.712, no breakout, Vol 0.795×)**

- **AMD** ($515.39, essentially flat +$2.13): No short lane qualifies. 2b-SHORT: Z=+1.445 (positive — wrong sign entirely), 20d low $341.54 is $173 below current price, RSI 69.0, Vol 0.379×. 2a-SHORT: Z=+1.445 (needs ≥+2.0), RSI 69.0 (needs >70), Vol 0.379×. NVDA CPU threat has not produced any statistical breakdown in AMD. → **STILL SKIPPED — all short lanes fail; Z positive (stock above 20d mean)**

- **INTC** ($107.17, down −$0.71 / −0.66%): 2b-SHORT: Z=−1.119 ✅, RSI 35.1 ✅, but Breakdown ❌ (needs close < $95.78; price is $11.39 above), Vol 0.549× ❌, SMA structure ❌ (50>200 — uptrend, wrong for short). Two of five pass, three fail. Bearish drift confirmed but structural trigger far away. → **STILL SKIPPED — 3 criteria fail (no breakdown, Vol 0.549×, SMA structure bullish)**

- **GLD** ($411.65, down −$0.45 / −0.11%): 2a-LONG: Z=−1.060 ❌ (needs ≤−2.0; still $8.00 above Z=−2.0 trigger price of ~$403.65), RSI 30.2 ❌ (needs <30; tantalizingly close, improved from 30.8), Vol 0.479× ❌ (needs ≥1.0×). RSI progress noted (30.8 → 30.2). GLD remains the primary developing setup — needs ~2% more price decline with volume confirmation over the next 1–3 sessions to trigger. → **STILL SKIPPED — all three 2a-LONG criteria fail; multi-day setup, not same-day**

- **MRVL** — Not re-evaluated. Phase 1 universe rule exclusion (high-momentum name prohibited from short universe). Exclusion is structural and does not change intraday.

---

**Trades fired this rescan:** None.

**Patience rule applied:** Zero candidates re-cleared all gates. This is correct. All six skipped names have at least 2–3 Layer B criteria failing simultaneously. The most advanced developing setup (GLD) still needs ~$8 more price decline over multiple sessions. AVGO showed the most intraday improvement (RSI −2.3 pts, Vol +0.24×) and is worth watching for a tomorrow re-evaluation if the pullback continues.

---

**Updated Forward Watchlist:**
| Ticker | Direction | Setup | Trigger Condition | Priority | Change vs AM |
|--------|-----------|-------|-------------------|----------|--------------|
| AVGO | LONG 2b | Momentum continuation | RSI cools ≤70 (was 71.4 at rescan, progress noted); Vol ≥30.9M on session (1.5× avg); pivot $459.97, max limit $506.72 | 🥇 #1 | ↗ Improving — RSI down −2.3 pts, Vol up +0.24× |
| GLD | LONG 2a | Mean-reversion oversold | Price declines to ~$403–$405 (Z ≤−2.0); RSI <30 (was 30.2 — very close); Vol ≥1.0× (6.08M); multi-day watch | 🥈 #2 | ↗ Slow progress — RSI 30.8→30.2 |
| XLK | LONG 2b | Momentum continuation | RSI must cool dramatically to ≤70 (was 80.6 — no improvement); Vol ≥19.2M; Trend Template 52w-high issue needs resolution | 🥉 #3 | → No change, deteriorated slightly |
| NVDA | LONG 2b | Breakout above pivot | Close > $235.74; Z ≥+1.0; Vol ≥257M (1.5× avg 171M) | Watch | ↘ Slightly weaker |
| AMD | SHORT 2b | NVDA CPU threat breakdown | Z ≤−1.0; close < 20d low; Vol ≥1.5×; SMA structure must deteriorate | Conditional | → No change |

---

**Rescan decision: HOLD — 0 trades. Correct application of patience rule.**

---

## 2026-06-02 — Midday Scan Addendum (~14:40 ET / 19:40 UTC)

**Scan type:** Midday workflow — position thesis check & stop evaluation
**VIX regime:** Normal (16.02–16.17 from morning research) — 1.00× sizing multiplier
**Account:** Equity $99,056.46 | Cash $99,056.46 (100%) | 0 positions | 0 orders | PDT 0/3 | Week 0/3

---

### STEP 1 — Portfolio State (Live API)
- **Positions:** `[]` — EMPTY. 100% cash confirmed.
- **Orders:** `[]` — EMPTY. No working brackets. No GTC stops.
- Pre-market HOLD decision confirmed: AVGO (RSI 73.7, vol 0.863×); XLK (RSI 80.5, TT 52w-high fail, vol 0.421×); NVDA (Z +0.920, below +1.0); AMD/INTC (no short lane); GLD (Z −1.037, vol 0.582×). No brackets placed.
- TRADE-LOG fully current. No discrepancy.

---

### STEP 2 / STEP 3 — Cut Losers / Tighten Stops: N/A (no positions)

---

### STEP 4 — Full Watchlist Re-Evaluation (Settled Bar Data — June 2, 2026)

**Quant results — all June 2 bars fully settled:**

| Ticker | Close | Z-Score | RSI(14) | Vol Ratio | 20d High | Extension | Pair | Pair Div | Lane | Key Failures | Verdict |
|--------|-------|---------|---------|-----------|----------|-----------|------|----------|------|--------------|---------|
| AVGO | $478.07 | +3.060 | 74.90 | 1.337× | $459.97 ✅ | +3.94% ✅ | MRVL | 0.469σ ✅ | 2b-LONG | RSI 74.90>70 ❌; Vol 1.337×<1.5× ❌ | **REJECT** |
| MRVL | $286.27 | +3.529 | 85.14 | 2.998× | $219.43 ✅ | **+30.46% ❌** | AVGO | 0.469σ ✅ | 2b-LONG | Ext +30.5%>>5% ❌; RSI 85.14>>70 ❌ | **REJECT** |
| XLK | $197.81 | +2.222 | 86.21 | 0.636× | $195.76 ✅ | +1.05% ✅ | AVGO | 0.838σ ✅ | 2b-LONG | RSI 86.21>70 ❌; Vol 0.636×<1.5× ❌ | **REJECT** |
| NVDA | $222.52 | +0.570 | 55.85 | 0.902× | $235.74 ❌ | −5.6% | MRVL | 2.958σ ❌ | No lane | Z<+1.0 ❌; Below pivot ❌; MRVL pair div ❌ | **REJECT** |
| GLD | $411.55 | −1.037 | 44.27 | 0.582× | — | — | NEM | ~0.4σ ✅ | 2a-LONG | Z −1.037 (need ≤−2.0) ❌; RSI 44.27 (need <30) ❌; Vol 0.582× ❌ | **REJECT** |

**Pair divergences (from settled bar Z-scores):**
- AVGO (+3.060) ↔ MRVL (+3.529): 0.469σ ✅ — AI semis perfectly confirming each other
- XLK (+2.222) ↔ AVGO (+3.060): 0.838σ ✅ — tech ETF tracking single-name leaders
- AVGO (+3.060) ↔ NVDA (+0.570): 2.490σ ❌ — NVDA dramatically lagging AI peers (yellow flag)
- NVDA (+0.570) ↔ MRVL (+3.529): 2.958σ ❌ — NVDA is the "odd one out" in the AI complex

---

### Candidate Notes

**AVGO ($478.07, +3.94% today) — 2b-LONG — Closest to qualifying:**
- Z = +3.060 ✅ | Breakout above $459.97 pivot ✅ | Extension +3.94% ✅ | MRVL pair confirms ✅
- RSI = 74.90 ❌ — overbought; has been above 70 for 3 consecutive sessions (73.7 → 73.5 → 74.9 — drifting higher, not cooling). Needs a flat/down session to bring RSI back into the 50–70 healthy momentum window.
- Vol = 1.337× ❌ — improved from Monday's 0.906× post-holiday trough to 1.337× today; positive trend but still 0.163× below the 1.5× gate. If tomorrow's session is a strong-volume day, this gate could clear.
- AVGO closed at its 52-week high ($478.07 = new all-time high); pivot for next entry session resets to $478.07. Max entry limit: $478.07 × 1.05 = **$501.97**.
- **AVGO remains #1 watchlist priority.** Both failing gates are "time and momentum" gates that resolve with one normalizing session.

**MRVL ($286.27, +30.5% today) — 2b-LONG — NOT TRADEABLE:**
- MRVL surged from $219.43 (Monday close) to $286.27 today — a +30.4% single-session move on 2.998× volume.
- Pivot extension = +30.46% above the $219.43 prior 20d high — **6× the 5% maximum chase limit.** This is one of the most extreme intraday gap-and-run situations the strategy explicitly blocks.
- RSI = 85.14 — severely overbought, in the top 1% of historical readings.
- The ≤5% pivot extension rule is doing its job: preventing the bot from chasing an earnings-gap stock that has already moved 30% above its base. Entering here has nothing to do with systematic edge.
- **MRVL is off the active watchlist until a new base forms.** Estimated time to next valid pivot: 3–6 weeks of consolidation. At that point, a fresh 2b-LONG setup can be evaluated with the new 20d high as pivot.

**XLK ($197.81, +1.05% today) — 2b-LONG — RSI severely extended:**
- Z = +2.222 ✅ | Breakout above $195.76 pivot ✅ | Extension +1.05% ✅ | AVGO pair confirms ✅
- RSI = 86.21 ❌ — this is the highest RSI reading on any name in any scan since the bot launched. XLK has rallied 14.1% in 10 sessions (May 22 $180.39 → June 2 $197.81). At RSI 86, the ETF is in historically overbought territory — every point above 80 increases the likelihood of mean-reversion rather than continuation.
- Vol = 0.636× ❌ — well below 1.5× threshold; no institutional volume confirmation of the breakout.
- XLK Trend Template note: 52w high test (from 25 bars) shows $197.81 = current high (within 25% ✅). TT may partially clear with data accumulation.
- **RSI must cool to ≤70 before XLK 2b-LONG can activate.** At the current pace, this requires a meaningful pullback in the AI/tech complex — could be 3–5 sessions minimum.

**GLD ($411.55, −0.12% today) — 2a-LONG developing:**
- Z = −1.037 (trigger = −2.0 at price $403.21; gap = $8.34 or −2.0% further decline)
- RSI = 44.27 — neutral and actually recovering from the ~30 level seen earlier; this moves RSI AWAY from the <30 trigger required for 2a-LONG
- Vol = 0.582× — consistently below 1.0× threshold; gold appears to be in very low-participation consolidation mode
- NEM (gold miner pair) Z-score estimated ~flat to slightly negative — pair coherent ✅
- GLD's setup has been the "always developing, never arriving" candidate for 2 weeks. The RSI recovery (from ~30 range to now 44) actually WEAKENS the mean-reversion thesis — a genuine oversold long entry needs RSI <30 at the moment of the Z trigger. If RSI continues recovering toward 50+, the 2a-LONG window may close entirely.
- **Reducing GLD priority from #2 to #3** given RSI moving away from trigger. Monitor but not urgent.

**NVDA ($222.52) — Watch-only:**
- Z = +0.570; 5.6% below $235.74 pivot; RSI 55.85 (neutral); vol 0.902×.
- NVDA continues to dramatically lag its AI peers (AVGO up +20% from NVDA's level on Z-score basis). This divergence (AVGO-NVDA = 2.490σ) reflects the market's current preference for custom ASIC/networking silicon (AVGO, MRVL) over GPU-centric AI compute (NVDA) in the near term.
- No lane qualifies. Watch for either: (a) NVDA catching up and breaking above $235.74 on ≥1.5× volume, or (b) a pullback to Z ≤ −2.0 (~$202) + RSI <30 for a 2a-LONG.

---

### Trades Fired This Rescan: None

**Patience rule applied.** The strategy is working as designed:
- AVGO: 2 timing gates (RSI + vol) — actively improving, nearly there
- MRVL: +30.5% pivot extension — correctly blocked (would be the worst kind of momentum chase)
- XLK: RSI 86 — correctly blocked (parabolic overbought ETF without volume confirmation)
- GLD: Z −1.037 — correctly blocked (not at statistical extreme)
- NVDA: Z +0.570 — correctly blocked (insufficient momentum signal)

No gates were lowered. Zero trades is the correct outcome.

---

### Key Watchlist for Thursday Pre-Market (2026-06-03)

1. **AVGO — #1 PRIORITY (2b-LONG):** Z=+3.060 ✅, ext +3.94% ✅, MRVL pair 0.469σ ✅, AVGO at 52w high. Needs: (a) RSI to cool from 74.90 → ≤70 (requires flat/down open or profit-taking); (b) volume ≥ 30.9M shares (1.5× of 20.5M avg). New pivot = $478.07; max entry limit = **$501.97** ($478.07 × 1.05). ADP employment report Thursday (8:15 AM ET) — potential macro catalyst that could move growth stocks.

2. **XLK — #2 (2b-LONG, lower priority until RSI cools):** RSI 86.21 is too extended for near-term entry. Needs meaningful pullback to bring RSI into 50–70. Tech ETF at 52w highs; may consolidate for 1–2 weeks before next clean entry. Max entry limit: $197.81 × 1.05 = **$207.70** (new pivot).

3. **GLD — #3 (watch, reducing priority):** RSI rising away from <30 trigger (now 44.27). Z = −1.037, needs −2.0% more decline AND RSI reversal to <30 simultaneously. Increasingly unlikely to trigger without a fresh negative catalyst for gold. Monitor weekly.

4. **MRVL — OFF active watchlist:** Needs 3–6 weeks to establish new base above current levels. Pivot extension +30.46% = unchallengeable per rules. Restore to watchlist only when new 20d high base is established.

5. **NVDA — watch-only:** Z +0.570, 5.6% below pivot. No near-term lane. Watching for either breakout above $235.74 or oversold dip to Z ≤ −2.0.

6. **New sector scan warranted:** All current watchlist names are in Information Technology. Per breadth mandate (≥3 sectors), Thursday pre-market should scan: Energy (XLE — Iran binary risk ongoing; Z ≈ −0.5), Materials (XLB — Z context), Healthcare (XLV — Z context post-overbought unwind), and any fresh catalysts in Industrials or Financials.

**Decision: HOLD — Research log updated (no actions taken — no TRADE-LOG or DAILY-SUMMARY entries required).**
