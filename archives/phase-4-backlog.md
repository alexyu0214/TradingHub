# Phase 4 Backlog

Items archived from earlier phase planning. Promote to active development when Phase 1 and Phase 2 gate criteria are met.

---

## Conditional Hourly Monitor (Option B)

**Origin:** Considered during Phase 1 setup (2026-05-03) when discussing whether to add hourly intraday scans. Deferred in favor of Option A (single 2 PM afternoon scan + bracket limit orders).

**Concept:**
A lightweight workflow that runs every hour during market hours but does almost nothing on most ticks. It performs a cheap pre-filter check; only if a trigger condition fires does it escalate to the full Claude agent.

**Trigger conditions (cheap to compute):**
1. Any open position within 5% of its stop level
2. VIX intraday spike >20% from morning baseline
3. News/halt headline on any held ticker (via Alpaca news endpoint)
4. Any unfilled bracket limit suddenly within 1% of fill (price moving toward our limit)

**Architecture:**
- New workflow `hourly-monitor.yml` cron `0 14-21 * * 1-5` (every hour 9 AM - 4 PM ET)
- New `hourly-monitor` section in ROUTINE.md — short prompt that runs the trigger checks
- If NO trigger: short Claude call (~1k tokens, ~$0.01), logs "no triggers" and exits
- If trigger fires: escalates to full midday-rescan agent for deep evaluation

**Why deferred to Phase 4:**
- Phase 1 needs to validate the new bracket-limit + quant-layer approach first. Adding hourly monitoring on top of unproven foundation risks masking what's actually working.
- Cost is bounded but real (~$30-80/mo on top of current).
- Most signal value is in the bracket orders themselves — they handle execution without polling.
- Better to see if Option A + brackets give us 80% of the benefit at 0% of the additional cost before adding monitoring complexity.

**Promotion criteria (when to build this):**
- Phase 1 closed (≥30 trades, gate criteria met)
- AND at least 3 documented incidents where intraday catalysts were missed because nothing checked between scheduled scans
- AND Anthropic account at tier 2+ for cost headroom

**Estimated build effort:** 2-3 hours (workflow YAML, ROUTINE.md section, Python helper for trigger checks).

---

## Pairs Trading with Shorts (Phase 3 — already in TRADING-STRATEGY.md backlog)

See `memory/TRADING-STRATEGY.md` "Strategy Backlog" section.
