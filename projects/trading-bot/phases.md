# Bot Phases

## Phase 1 — Paper Validation
**Account:** Alpaca paper, $100k
**Duration:** Until gate criteria are met (minimum 30 days, 30 trades)
**Purpose:** Prove edge before risking real money

**Gate to advance:**
- Sharpe ≥ 1.5
- Max drawdown ≤ 15%
- Positive expectancy (not just win rate)
- 30+ trading days, 30+ trades

If gates aren't met, iterate strategy. Don't advance to live just because the calendar says so.

## Phase 2 — Live Sprint
**Account:** Alpaca live, $1k
**Duration:** 90 days
**Target:** Reach $30k (stretch). Realistic checkpoints in `context/goals.md`.
**Purpose:** Execute proven strategy with real money

Same strategy as Phase 1. Same risk rules. Smaller capital.

**Watch-out:** $1k live ≠ $100k paper in execution. Slippage hurts more, position sizing changes the strategy mix (some setups that work on $100k won't fit a $1k account). Phase 2 design must account for this.

## Phase 3 — Compounding (post-sprint)
After Day 90, reassess. Don't blow up the account chasing the next moonshot.
