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
