# Current Priorities

As of Q2 2026.

## Priority 1 — Paper Trading Validation
Run the bot on the $100k Alpaca paper account. Goal: prove the strategy has real edge before any live money goes in.

Tracked in `projects/trading-bot/`.

## Priority 2 — Strategy Research & Documentation
Research and document trading strategies (long/short equities, swing horizon). Capture rules, entries, exits, and risk. Stored in `references/sops/` and `projects/trading-bot/strategy.md`.

## Priority 3 — Risk Framework
Lock down risk rules: max position size, max drawdown, stop-loss methodology, exposure limits. Bot does not trade until these are set.

## Priority 4 — Live Cutover (after paper proves out)
Move to the live $1k account. Begin the 90-day sprint toward $30k under realistic sub-targets.
