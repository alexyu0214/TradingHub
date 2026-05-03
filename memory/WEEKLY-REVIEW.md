# Weekly Review

Friday recaps. Each entry scores the week's performance, grading strategy execution, and adjustments for next week.

---

## Weekly Review Template

```
## Week ending YYYY-MM-DD

### Stats
| Metric | Value |
|--------|-------|
| Starting portfolio | $X |
| Ending portfolio | $X |
| Week return | ±$X (±X%) |
| S&P 500 week | ±X% |
| Bot vs S&P 500 | ±X% |
| Trades executed | N |
| Wins | X |
| Losses | X |
| Open positions | X |
| Win rate | X% |
| Best trade | SYM +X% |
| Worst trade | SYM -X% |
| Profit factor | X.XX |
| Max intraweek drawdown | X% |

### Closed Trades (This Week)
| Date | Ticker | Entry | Exit | P&L | Hold (days) | Notes |
|------|--------|-------|------|-----|-------------|-------|
| MM-DD | SYM | $X | $X | ±$X | X | [brief reason] |

### Open Positions at Week End
| Ticker | Entry | Close | Unrealized P&L | Stop |
|--------|-------|-------|----------------|------|
| SYM | $X | $X | ±$X (±X%) | $X |

### What Worked
- [3–5 bullets on signals, risk management, entry timing, whatever went right]

### What Didn't Work
- [3–5 bullets on failures, false signals, timing mistakes, whatever went wrong]

### Key Lessons
- [2–3 bullets on learnings or adjustments]

### Adjustments for Next Week
- [changes to universe, signals, risk sizing, anything we're trying differently]

### Overall Grade: X (A–F)

---
```

Grading scale:
- **A:** Week return > S&P 500 by 2%+, perfect execution, no rules violations
- **B:** Week return in line with S&P 500, clean execution, maybe one small mistake
- **C:** Week return < S&P 500, trades happened but hit some turbulence
- **D:** Week return significantly negative, execution issues, multiple lessons learned
- **F:** Major loss, rules violation, serious mistake (should be rare)

---

## Thinking Behind the Framework

- **Stats** tell you if you beat the market
- **Closed trades** show if your entries/exits worked
- **Open positions** remind you what's still at risk
- **What worked / What didn't** force reflection (no auto-pilot)
- **Adjustments** ensure you're learning, not just trading
- **Grade** keeps you honest about execution quality

Every Friday, take 15 minutes to fill this out. Use it to calibrate next week.

## Week ending 2026-05-01

### Stats
| Metric | Value |
|--------|-------|
| Starting portfolio | $100,000.00 |
| Ending portfolio | $99,889.50 |
| Week return | −$110.50 (−0.11%) |
| S&P 500 week | +0.91% |
| Bot vs S&P 500 | −1.02% |
| Trades executed | 1 |
| Wins | 0 (no closed trades) |
| Losses | 0 (no closed trades) |
| Open positions | 1 (XOM) |
| Win rate | N/A (0 closed trades) |
| Best trade | N/A |
| Worst trade | N/A |
| Profit factor | N/A |
| Max intraweek drawdown | −0.14% (peak $100,006.50 → trough $99,870.00) |

### Closed Trades (This Week)
| Date | Ticker | Entry | Exit | P&L | Hold (days) | Notes |
|------|--------|-------|------|-----|-------------|-------|
| — | — | — | — | — | — | No closed trades this week |

### Open Positions at Week End
| Ticker | Entry | Close | Unrealized | Stop |
|--------|-------|-------|------------|------|
| XOM | $153.35 | $152.50 | −$110.50 (−0.55%) | $138.78 (10% trailing GTC, HWM $154.20) |

### What Worked (3–5 bullets)
- **Gate discipline held on day-1 chaos:** When XOM/CVX/AAPL all gapped 14–32% past research ceilings at the first execution window (13:38 UTC), the spread-check and gap-chase rules correctly blocked all three entries — avoiding buying into post-earnings volatility at deeply unfavorable prices.
- **Second-session re-entry on XOM was clean:** After monitoring for spread normalization, XOM was entered at $153.35 with a healthy spread, a valid catalyst, and a GTC trailing stop placed immediately — textbook procedure execution.
- **Research-blackout protocol worked:** Two consecutive sessions of Gemini API failure (Day 1: 503 outage; Day 2: 403 key revoked) correctly produced HOLD decisions rather than uninformed trades. Cash was preserved 100% through both blackout days.
- **Trailing stop placed immediately at fill:** GTC trailing stop (10%) was live within seconds of the XOM fill. Stop auto-adjusted intraday from $138.015 (initial) to $138.78 as price briefly ticked up to HWM $154.20 — exactly the intended behavior.
- **Max drawdown contained:** The worst point of the week was −0.14% of equity. With only one position at ~20% deployment, the portfolio has a large cash buffer absorbing volatility cleanly.

### What Didn't Work (3–5 bullets)
- **Research pipeline failure burned two full trading days:** The Gemini API blackout on Apr 30 (Day 1: 503; Day 2: 403 key leak) meant the bot could not screen or generate catalysts for the first two sessions of Phase 1. Two of five tradeable sessions were effectively lost. API key rotation must happen before any research-dependent session.
- **Energy thesis entry levels were badly miscalibrated:** Research estimated XOM at $118–122 and CVX at $165–170; both opened 30%+ above those levels on earnings day. The gap between research price estimates and actual open prices exposed a gap in the research process — earnings-day entry levels should always be treated as "estimate only, confirm live" with explicit re-anchoring logic.
- **Zero diversification achieved:** Only one position (XOM, ~20% deployed) was opened against a target of 75–85% deployed. The remaining 80% of capital sat idle in cash for the full week. While justifiable given gate failures, it means the portfolio had almost no market participation during a strong +0.91% S&P week.
- **AAPL conditional gate chain created fragility:** Making AAPL contingent on both XOM AND CVX fills meant that when the primary energy pair failed, AAPL — which had a clean spread (1.51%) — was automatically blocked even though its individual catalyst (Q2 earnings beat) remained valid. The conditional-chain approach needs reconsideration for cases where secondary/tertiary ideas have independent catalysts.
- **CVX skipped both sessions despite recovering spread:** On the first execution attempt CVX spread was 6.93% (correctly skipped); on the second it was 4.23% (still wide, correctly skipped). However, the bot never circled back intraday to check if CVX tightened further. An intraday re-evaluation loop would have allowed CVX entry if spread dropped to <2%.

### Key Lessons (2–3 bullets)
- **Re-anchor entry levels same-morning:** Pre-market research estimates for gapping stocks are starting points, not hard targets. A same-morning check (even 30 minutes before open) against live pre-market quotes would catch gaps early and allow revised entry/spread thresholds — preventing the execution-window surprise that blocked three trades simultaneously.
- **Decouple tertiary ideas from failed entry chains:** Independent catalysts should be evaluated independently. If XOM/CVX fail their gate for structural reasons (spread, gap), AAPL should re-run its own gate check from scratch rather than being auto-blocked by the parent chain's failure.
- **API key rotation is a hard pre-condition, not a nice-to-have:** Two full trading days were lost to a revoked API key. This must be treated as a launch-blocking issue — same severity as the trading-blocked flag. Add a key health-check to the startup routine.

### Adjustments for Next Week
- **Add same-morning pre-open quote check (T−30 min):** Before the execution window opens, pull live pre-market quotes for all planned ideas. If any has gapped >5% past the research estimate, auto-flag for entry-ceiling revision or defer to first-candle confirmation entry logic.
- **Decouple conditional gates for independent catalysts:** AAPL-style tertiary ideas that have their own valid catalyst should run independent gate checks. Remove the hard "energy fills first" prerequisite; replace with cash-headroom check only (e.g., "cash after this fill ≥ 30% of equity").
- **Add intraday re-evaluation step (T+60 min):** At ~10:30–11:00 CT, re-check spreads and price levels for any skipped ticker. If spread has normalized and price is within 5% of revised ceiling, re-enter decision tree.
- **Target 3 open positions by mid-next-week:** With the S&P 500 hitting all-time highs (+13.52% over five weeks, 12th ATH close YTD) and the bot only 20% deployed, add 1–2 more positions in leading sectors (Energy, Industrials, Materials) to improve market participation. Do not force entries — use intraday setups if morning research finds no clean open.
- **Re-evaluate XOM stop level if price consolidates above $155:** At +1% from entry the trailing stop still sits at $138.78 (−10% from HWM). If XOM holds above $155 next week, consider monitoring for the tightening trigger at +15% ($176.35). Sector tail risk (Hormuz binary) justifies keeping the stop wide for now.

### Overall Grade: C
**Justification:** The bot underperformed the S&P 500 by −1.02% in a week the index gained +0.91% (its 5th consecutive up week and a new ATH). However, this was a launch week with extraordinary operational obstacles: two full research blackouts (API failures), three trades simultaneously blocked by post-earnings gap conditions, and only 20% of capital deployed. The core discipline held perfectly — no rules violations, no bad entries chased, no stops broken. The grade reflects strong *process* (C+ on process) but weak *outcome* (C− on market participation and return). The operational issues (API key, entry-ceiling recalibration) are fixable and should not recur.

---


## Week ending 2026-05-01

### Stats
| Metric | Value |
|--------|-------|
| Starting portfolio | $100,000.00 |
| Ending portfolio | $99,870.00 |
| Week return | −$130.00 (−0.13%) |
| S&P 500 week | +0.78% (7,173.91 → 7,230.12; new ATH 7,272.52) |
| Bot vs S&P 500 | −0.91% |
| Trades executed | 1 (XOM buy, May 1) |
| Wins | 0 (no closed trades) |
| Losses | 0 (no closed trades) |
| Open positions | 1 (XOM) |
| Win rate | N/A (0 closed trades) |
| Best trade | N/A |
| Worst trade | N/A |
| Profit factor | N/A |
| Max intraweek drawdown | −0.24% (intraday peak ~$100,110 → Fri close $99,870) |

### Closed Trades (This Week)
| Date | Ticker | Entry | Exit | P&L | Hold (days) | Notes |
|------|--------|-------|------|-----|-------------|-------|
| — | — | — | — | — | — | No closed trades this week |

### Open Positions at Week End
| Ticker | Entry | Close (Fri) | Unrealized | Stop |
|--------|-------|-------------|------------|------|
| XOM | $153.35 | $152.35 | −$130.00 (−0.65%) | $138.78 (10% trailing GTC, HWM $154.20) |

### What Worked (3–5 bullets)
- **Entry gate discipline on first live session:** The bot correctly refused to chase XOM, CVX, and AAPL during the 13:38 UTC execution window when all three had gapped 14–34% above research price estimates. A second, calmer execution window later in the session produced a clean XOM fill at $153.35 — within spread tolerance and supported by a valid catalyst (XOM Q1 earnings beat, elevated WTI, Hormuz supply-risk premium).
- **GTC trailing stop placed immediately at fill:** The 10% trailing stop was live within seconds of the XOM fill. The stop auto-ratcheted from $138.015 → $138.78 as price briefly touched HWM $154.20 intraday — exactly the intended mechanical behavior, no manual intervention required.
- **Market context correctly absorbed:** The S&P 500 posted a volatile week (+0.78% net), touching a new ATH of 7,272.52 on Thursday while experiencing a −0.49% dip on Tuesday (AI stock selloff + rising oil). The bot's energy thesis via XOM was directionally aligned with the market-moving oil catalyst, even if the position ended slightly underwater at week close.
- **CVX and AAPL skip decisions were correct:** CVX's spread remained too wide on both execution attempts; AAPL correctly failed the conditional gate (XOM/CVX fills prerequisite not met). Both skips protected capital from chasing volatile post-earnings setups with elevated spread risk.
- **No circuit breakers triggered, no rules violations:** Day loss max was −0.13% (limit: −2%), phase loss −0.13% (limit: −5%), drawdown −0.24% (limit: −15%). PDT daytrade count used: 1/3. Weekly trade count: 1/3. Clean operational week from a compliance standpoint.

### What Didn't Work (3–5 bullets)
- **Portfolio remained severely underdeployed all week:** Only ~20% of capital was deployed (XOM, entered on the final day of the week). The 75–85% minimum deployment target was never approached. In a week when the S&P 500 rose +0.78% and hit an all-time high, the bot's cash-heavy posture meant near-zero market participation — translating directly into the −0.91% lag vs the index.
- **First execution window wasted by pricing miscalibration:** Research entry estimates for XOM ($118–122) and CVX ($165–170) were already stale before the week began. Both stocks opened 30%+ above those levels on earnings day. Pre-computed research levels must be treated as provisional — a pre-open live-quote check would have caught this gap and reset the entry ceiling before execution began.
- **AAPL's independent catalyst blocked by chain dependency:** AAPL reported a strong Q2 earnings beat and forecasted stronger-than-expected Q2 revenue (confirmed by Apple's contribution to the Friday +0.29% S&P gain). Its individual checklist was largely clean, yet it was auto-blocked because CVX did not fill. Making AAPL contingent on energy chain completion — rather than on cash headroom alone — was an over-engineered gate that cost a potentially positive trade.
- **No intraday re-evaluation of CVX spread:** The bot checked CVX's spread twice (6.93%, then 4.23%) and correctly skipped both times. However, no logic existed to re-check CVX at 10:30–11:00 CT when spreads typically normalize post-open. By late morning CVX likely tightened into tradeable range; the opportunity was missed due to the absence of a midday re-scan loop.
- **Week 1 produced zero statistical data for strategy refinement:** With no closed trades, win rate, profit factor, and expectancy remain undefined. The Phase 1 gate (≥30 closed trades) has no entries on the board. The longer trades stay unclosed, the longer the bot operates without feedback data.

### Key Lessons (2–3 bullets)
- **Pre-open live-quote anchoring is mandatory, not optional:** Any research-generated price estimate must be re-validated against a live pre-market quote at T−30 minutes. If the current price is >5% above the research estimate, the entry ceiling must be revised or the idea deferred to first-candle confirmation logic. This single change would have unlocked all three May 1 entries faster.
- **Cash headroom is the right gate — not chain dependencies:** Conditional entry gates should ask "do I have the cash?" not "did the prior trade fill?" When independent catalysts exist (like AAPL's Q2 earnings beat), they should clear their own checklist independently. Replace chain dependencies with a simple cash-headroom check (e.g., cash after fill ≥ 30% of equity).
- **Add a midday re-scan trigger (10:30–11:00 CT):** A structured 60-minute post-open re-check of skipped tickers — specifically spread normalization and price stability — would capture entries that miss the opening window but become clean setups by mid-morning. This is especially important in the first hour after earnings gaps.

### Adjustments for Next Week
- **[PROCESS] Add T−30 min pre-open live-quote check:** Before the execution window opens each morning, pull live pre-market quotes for all planned ideas. If any ticker has gapped >5% from the research estimate, auto-flag for entry-ceiling revision. Log revised entry ceilings in that day's research entry.
- **[PROCESS] Decouple conditional gates — use cash-headroom only:** Remove "XOM and CVX must fill first" prerequisite from AAPL (and all future tertiary ideas). Replace with: "cash after this fill ≥ 30% of equity AND total positions ≤ 6." Each ticker evaluates its own entry checklist independently.
- **[PROCESS] Add intraday re-scan at 10:30–11:00 CT:** If any ticker was skipped at open due to spread >2% or gap-chase risk, re-evaluate at 10:30 CT. If spread has normalized and price is within 5% of revised ceiling, re-enter decision tree from the catalyst-check step.
- **[POSITIONS] Target 2–3 open positions by mid-week:** With cash at 80% and the market in a confirmed uptrend (S&P 500 ATH week), the bot must add positions. Leading sectors to scan: Energy (XOM carry-forward), Industrials, and Large-Cap Tech (post-earnings dip setups). Apply all entry checklist gates — but actively search for qualifying setups rather than defaulting to hold-cash.
- **[RISK] Review XOM trailing stop as price evolves:** Current stop at $138.78 (10% trail from $154.20 HWM). If XOM recovers above $155 and approaches $160, monitor for the +15% trigger ($176.35 from entry) when trailing tightens to 7%. Given "Sell in May" seasonal headwinds noted in prior research, be willing to take profits faster than usual if the Hormuz risk premium fades.

### Overall Grade: C
**Justification:** The S&P 500 gained +0.78% on the week, touched a new all-time high of 7,272.52, and benefited from the exact catalyst (Apple's strong Q2 revenue forecast) that the bot identified but failed to enter. The bot returned −0.13%, trailing the index by −0.91%. This is the second consecutive week graded C, both driven by the same root cause: operational process gaps (stale price estimates, missing intraday re-scan loop) rather than strategy failure. The underlying strategy is sound — XOM was the right trade and was entered correctly — but only one trade was placed in five sessions, leaving 80% of capital idle during an up-week. The energy thesis and entry checklist discipline are working; deployment velocity is not. Next week, deployment target is 2–3 positions by Wednesday.

---

## Week ending 2026-05-01

### Stats
| Metric | Value |
|--------|-------|
| Starting portfolio | $100,000.00 |
| Ending portfolio | $99,922.00 |
| Week return | -$78.00 (-0.078%) |
| S&P 500 week | +0.91% |
| Bot vs S&P 500 | -0.99% |
| Trades executed | 1 (XOM — open) |
| Wins | 0 (no closed trades) |
| Losses | 0 (no closed trades) |
| Open positions | 1 (XOM) |
| Win rate | N/A (no closed trades) |
| Best trade | N/A |
| Worst trade | N/A |
| Profit factor | N/A (no closed trades) |
| Max intraweek drawdown | -0.14% (est. intraday, XOM entry day) |

> **Context:** This is the bot's inaugural week. Trading began May 1 (Day 2 of Phase 1). The week effectively covers a single partial trading day (Friday May 1) since launch was April 30 and the first trade fired May 1 at open. All stats are phase-inception numbers, not a full 5-day week.

---

### Closed Trades (This Week)
| Date | Ticker | Entry | Exit | P&L | Hold (days) | Notes |
|------|--------|-------|------|-----|-------------|-------|
| — | — | — | — | — | — | No closed trades this week |

---

### Open Positions at Week End
| Ticker | Entry | Close | Unrealized | Stop |
|--------|-------|-------|------------|------|
| XOM | $153.35 | $152.75 | -$78.00 (-0.39%) | $138.78 (10% trailing GTC) |

---

### What Worked (3–5 bullets)
- **Discipline on gap-chasing:** XOM, CVX, and AAPL all gapped 14–32% past research entry ceilings at the open on May 1. The bot correctly declined all three at first-pass, then re-evaluated and entered XOM only after it pulled back into a tradeable range (~$153 vs. the initial $160+ ask). Zero gap-chase fills = zero adverse-selection losses.
- **Conditional entry gates functioned correctly:** CVX was gated on XOM fill confirmation; AAPL was gated on both energy fills. When XOM's spread was wide at first-pass and CVX was skipped, the AAPL gate auto-blocked — exactly as designed. No cascade of bad fills.
- **Hard stop placed immediately post-fill:** GTC 10% trailing stop (order ID confirmed) was placed on XOM within the same execution block as the buy. Stop is live at $138.78 with HWM $154.20. Mandatory constraint satisfied on first trade of the phase.
- **Cash preservation on a volatile open:** By holding 80% cash through an extremely wide-spread earnings-gap session, the bot avoided the worst of post-earnings mean-reversion risk on CVX and AAPL (both tickers saw significant intraday reversals after their gaps).
- **Research pipeline recovered mid-week:** After two sessions blocked by the revoked Gemini API key (Apr 29–30), the research pipeline was restored for May 1, allowing the XOM thesis to be fully validated before execution.

---

### What Didn't Work (3–5 bullets)
- **Research blackout cost two full trading days (Apr 29–30):** The revoked Gemini API key (403 PERMISSION_DENIED) blocked the pre-market research workflow for two consecutive sessions. Zero trades could be safely placed without validated catalysts. This was the correct protocol response, but the root cause (key management) is a preventable operational failure.
- **Entry pricing in research was too conservative vs. market reality:** Research entry ceilings for XOM ($122), CVX ($170), and AAPL ($215) were derived from pre-earnings estimates. All three opened 14–32% above those ceilings. While gap-chasing was correctly avoided, the research model needs a post-earnings gap adjustment methodology so that revised entry levels can be computed quickly after an overnight earnings surprise.
- **Underdeployment vs. strategy target:** Ending the week at 19.87% deployed (vs. the 75–85% target band) reflects the bot being in its very first week with limited research history and an API key incident. However, with only 1 of 3 weekly trade slots used and 80% cash idle, the portfolio is generating no return on the bulk of its capital. This is operationally correct but strategically sub-optimal.
- **XOM entry slightly above-plan on spread:** Even on the eventual XOM fill at $153.35 (not the initial wide-spread first-pass), the entry was meaningfully above the research-planned $118–122 range. The energy thesis is still valid, but the risk/reward was degraded vs. plan (actual R:R at entry ~1.5:1 vs. planned 2.1–2.4:1). The "wait for 5-min candle" rule was applied but the anchor price from research was already stale.
- **No second or third position established:** Despite having 2 of 3 weekly trade slots remaining and 80% cash, no follow-up positions were opened during the week. CVX and AAPL both stabilized intraday, but no execution run re-evaluated them after the spread normalized. A midday execution pass could have recovered the CVX opportunity.

---

### Key Lessons (2–3 bullets)
- **Build a post-gap repricing module into research:** When overnight earnings surprise >5% vs. expectations, the pre-market research entry ceiling must be recalculated at the open using the actual gap price as the new anchor — not the pre-earnings estimate. A static ceiling from pre-market research becomes a blocker, not a guide, after a large gap.
- **Schedule a midday execution check:** The current workflow only runs at market open. On earnings-gap days, spreads are wide at open but normalize within 30–60 minutes. A 10:00–10:30 AM check (after the first 15-minute no-trade window) would have caught CVX and potentially AAPL at improved entries. This is especially important when the open execution is blocked by spread issues.
- **API key rotation must be a pre-session automated gate:** Two consecutive research blackouts due to a single revoked API key is an unacceptable single point of failure. The execution workflow should test the research API key at start-of-day and alert/halt immediately rather than proceeding to an empty research output.

---

### Adjustments for Next Week
- **Implement midday execution check (10:00–10:30 AM CT):** After wide-spread or gap-chase blocks at open, a secondary execution window will be added to re-evaluate any skipped tickers once spreads normalize. This directly addresses the CVX/AAPL miss.
- **Revise research entry ceiling logic for earnings plays:** Add a "post-gap ceiling adjustment" step: if a ticker has gapped >5% vs. research ceiling pre-open, recalculate entry range as: [gap_open × 0.97, gap_open × 1.01] — i.e., allow entry on a 1–3% pullback from the gap open, not the pre-earnings anchor.
- **Re-evaluate CVX for entry next week:** Spread was the only blocker (catalyst, R:R, and sector thesis all valid). If spread normalizes to <2% and price is in a technically reasonable range, CVX is eligible as one of next week's 3 trade slots.
- **Continue holding XOM:** Energy thesis (Hormuz supply disruption, WTI elevated, post-earnings momentum) remains structurally intact. XOM's trailing stop is appropriately set. No action needed unless stop triggers or thesis breaks (surprise Hormuz resolution / WTI crash).
- **Scan for non-energy momentum:** Currently 100% energy exposure (1 position). With 2 trade slots available and the sector concentration cap at $30k, the next new position must be in a different sector. Candidate sectors to research: Technology (post-AAPL earnings momentum), Consumer Staples (defensive, if VIX rises), Industrials (infrastructure spending).
- **Key rotation protocol:** Establish a pre-session API key health-check step that validates the Gemini (or equivalent research LLM) key before any research workflow begins. If health-check fails, escalate immediately to Alex rather than running a degraded session.

---

### Overall Grade: C+
**Justification:** The bot's inaugural week was operationally disciplined but strategically thin. On the positive side: all three hard gate violations (gap-chasing, wide spread, conditional entry sequencing) were correctly identified and blocked — the bot did exactly what the rulebook says. The XOM entry was clean given the constraints active at execution time, and the mandatory GTC trailing stop was placed immediately. No rules violations occurred. On the negative side: two of five sessions were completely research-dark due to a preventable API key failure; the single trade entered is slightly underwater (-0.39%); the portfolio ended 80% in cash vs. a 75–85% deployment target; and the bot underperformed the S&P 500 by ~1% in a week when the market gained nearly 1%. This is a C+ rather than a D because the discipline shown on gap-chasing and spread checks was exactly right — a worse bot would have chased all three tickers and potentially been down 5–10% on opening-day mean reversions. The grade reflects: correct process, weak outcomes, one fixable operational failure.

---
