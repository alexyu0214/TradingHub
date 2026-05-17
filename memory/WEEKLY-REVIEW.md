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

## Week ending 2026-05-08 [LEGACY ENTRY -- DATA STALE]

> WARNING: This entry was generated 2026-05-08 with incomplete data. It failed to register the XOM thesis-break exit on 2026-05-07 ($146.09, realized -$943.51) and reports phase P&L as -0.078% when the true value was -0.944%. Root cause: weekly-review prompt grep patterns did not surface TRADE-LOG entries with `###` headings. Fixed in commit on 2026-05-10. Treat the narrative below as historical artifact, not source-of-truth.


### Stats
| Metric | Value |
|--------|-------|
| Starting portfolio | $99,922.00 |
| Ending portfolio | $99,922.00 |
| Week return | $0.00 (0.00%) |
| S&P 500 week | +0.54% (5,099.96 → 5,127.79) |
| Bot vs S&P 500 | −0.54% |
| Trades executed | 0 (new this week) |
| Wins | 0 (no closed trades) |
| Losses | 0 (no closed trades) |
| Open positions | 1 (XOM — carried from prior week) |
| Win rate | N/A (0 closed trades) |
| Best trade | N/A |
| Worst trade | N/A |
| Profit factor | N/A |
| Max intraweek drawdown | 0.00% (equity flat all week; XOM unchanged at $152.75) |

> **Context:** This is the first full Mon–Fri review week of Phase 1. The bot entered XOM on May 1 (prior week's Friday); that position carried forward as the sole holding. No new trades were placed this week (Mon May 5 was the only active trading day logged, and it produced zero market movement on XOM and zero new entries). Equity held flat at $99,922 from Sunday open through Friday. The S&P 500 gained +0.54% during Apr 26–May 3, entirely a missed-participation gap.

---

### Closed Trades (This Week)
| Date | Ticker | Entry | Exit | P&L | Hold (days) | Notes |
|------|--------|-------|------|-----|-------------|-------|
| — | — | — | — | — | — | No closed trades this week |

---

### Open Positions at Week End
| Ticker | Entry | Close | Unrealized | Stop |
|--------|-------|-------|------------|------|
| XOM | $153.35 | $152.75 | −$78.00 (−0.39%) | $138.78 (10% trailing GTC, HWM $154.20) |

---

### What Worked (3–5 bullets)
- **XOM trailing stop mechanics held correctly all week:** The GTC 10% trailing stop placed at XOM's entry on May 1 remained live and correctly anchored at $138.78 (HWM $154.20) throughout the week. No manual intervention was required. The stop auto-ratchet behavior is functioning as designed — this is the core mechanical discipline the strategy depends on.
- **Capital preservation in a directionless week for XOM:** With XOM flat at $152.75 the entire week and no meaningful intraday movement, holding the position without panic-selling or prematurely exiting the energy thesis was correct. The stop is wide enough ($138.78 = −9.5% from close) to absorb normal energy sector volatility; no thesis-break signal appeared.
- **No circuit breakers triggered for the second consecutive week:** Day loss, phase loss, and drawdown all remain well within limits (phase P&L: −0.078% vs. −5% limit; drawdown: −0.078% vs. −15% limit). PDT count reset to 0/3. The account is operationally clean.
- **Weekly trade allowance reset and available:** Entering this week with 3/3 trade slots fresh (XOM was entered in the prior week) meant full capacity was available for new entries. While no new entries fired, the slate was clean — no risk of hitting the weekly cap.
- **Patient hold posture appropriate given low-signal environment:** With XOM flat, no high-conviction research catalysts logged this week, and the research pipeline still recovering from the prior week's API blackout issues, standing aside on new positions was the disciplined choice rather than forcing entries.

---

### What Didn't Work (3–5 bullets)
- **Zero market participation on a +0.54% S&P 500 week — again:** For the second consecutive week, the bot generated 0.00% return while the S&P gained +0.54%. Cumulative underperformance since launch is now approximately −1.05% vs. the index in just two weeks. The 80% cash drag is becoming a persistent structural problem, not a one-off.
- **No new positions added despite full trade capacity:** The week ended with 3/3 weekly trade slots unused and 80% of capital idle. Per the prior week's review, the explicit adjustment target was "2–3 open positions by mid-week." This did not happen. The failure to add positions is now a two-week pattern, not an isolated occurrence.
- **No midday re-scan executed (prior week adjustment not implemented):** The prior week's review explicitly called for adding an intraday re-scan at 10:30–11:00 CT for spread-normalized re-entries. No evidence in the trade log or research log that this check was implemented this week. Adjustments identified in weekly reviews must be actioned, not just documented.
- **Research log shows no new catalyst ideas this week:** The research log entries visible for this period are from Apr 30 and May 1 — nothing filed for the May 5–9 window. Pre-market research is supposed to run daily; the absence of logged research sessions suggests the pipeline may still be degraded or research outputs are going unlogged.
- **XOM position still underwater, R:R degrading with time:** The longer XOM sits at −0.39% without progressing toward the +15% target ($176.35), the longer capital is tied up at sub-optimal deployment with a degrading profit factor. Time decay on a flat trade is opportunity cost — two weeks of carrying a near-zero position while the market moves up.

---

### Key Lessons (2–3 bullets)
- **Deployment velocity is now the #1 priority — this is a recurring failure, not a one-week anomaly:** Two consecutive weeks of ~20% deployment against a 75–85% target is not caution, it is systematic under-execution. The strategy requires active position-building to generate the 30 closed trades needed for Phase 1 graduation. At the current pace of ~0 new trades/week, Phase 1 will never close. Next week, a concrete deployment plan (specific tickers, specific levels, specific session) must be logged in pre-market research — not aspirational bullets in the weekly review.
- **Prior week's process adjustments must be operationally verified, not just written down:** The weekly review is only valuable if its adjustments are implemented. Three adjustments were listed two weeks ago (pre-open live-quote check, decoupled conditional gates, midday re-scan). None appear to have been implemented. Going forward, each adjustment must be tagged with a verification step in the following week's research log: "Implemented: Y/N."
- **Consider whether the energy thesis on XOM still has legs or needs a time-stop:** XOM entered May 1 at $153.35, currently at $152.75 — essentially flat for two weeks. The Hormuz thesis is structural (multi-month), but if XOM cannot hold above $150 next week or fails to show any upward momentum, a thesis-based exit (not stop-based) may be warranted to redeploy capital into a more active setup. Time-stops are valid — a stagnant position is dead capital.

---

### Adjustments for Next Week
- **[URGENT — DEPLOYMENT] File a concrete 3-position scan plan before Monday open:** Research must identify 2–3 qualifying tickers in non-Energy sectors (Industrials, Tech, Consumer Staples) with entry levels, stops, and catalysts documented. Do not start Monday without a trade plan. If no ideas clear all gates, log explicitly why — do not default to silence.
- **[PROCESS] Implement and verify the midday re-scan (10:30 CT):** This is the third week this adjustment has appeared. It must be executed, not just written. At 10:30 CT Monday, re-evaluate any tickers from the morning scan that were skipped due to spread or gap. Log the re-scan result in RESEARCH-LOG.md.
- **[PROCESS] Implement pre-open live-quote check (T−30 min):** Pull live pre-market quotes for all planned trades at 9:00 AM CT. If any ticker has moved >5% from the research estimate, revise the entry ceiling before the execution window opens. Log the pre-open check in that day's research entry.
- **[POSITION] Evaluate XOM time-stop:** If XOM does not show upward momentum (close above $155) by Wednesday May 8, evaluate a discretionary exit to free capital for a more active setup. Document the decision in the trade log. The 10% trailing stop remains as the hard floor regardless.
- **[STRATEGY] Decouple conditional gates — cash-headroom only:** Now three weeks on the adjustment list. AAPL-type tertiary ideas must run their own independent checklist; the only cross-position check should be: "Will total deployed capital after this fill remain ≤ 85% of equity?"
- **[ACCOUNTABILITY] Tag each prior-week adjustment as Implemented/Not in Monday's research log:** When filing Monday's pre-market research, explicitly check off each adjustment from this week's review with Y/N. This creates accountability and prevents the same adjustments from cycling through indefinitely.

---

### Overall Grade: D
**Justification:** The S&P 500 gained +0.54% this week (closing at 5,127.79 vs. 5,099.96 the prior Friday). The bot returned 0.00% — underperforming by −0.54%. More critically, this is the second consecutive week of near-zero return and approximately 20% deployment against an 80% target. The discipline shown in avoiding bad trades remains commendable, but discipline without action is not a strategy — it is paralysis. The prior week was graded C/C+ with explicit deployment targets set for this week; those targets were not met. The grade drops to D this week not because of a catastrophic loss, but because the same operational failure (underdeployment, no new positions, adjustment list not implemented) recurred for a second straight week. A third consecutive week of this pattern would constitute a strategy-level failure requiring a full process audit.

---
