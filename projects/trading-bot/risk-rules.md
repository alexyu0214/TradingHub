# Risk Rules

**Hard constraints. The bot must not violate these.**

## Position Sizing
- **Max position size:** 5% of account equity per single name
- **Max sector concentration:** 25% of account equity in one sector
- **Max gross exposure:** 150% (longs + |shorts|), max net exposure 100%
- **Per-trade risk:** 0.5%–1% of equity (defined as: position size × stop distance / equity)

## Stops
- Every position has a stop-loss order in the broker before/at entry
- Stops use ATR or technical level — no arbitrary % stops without basis
- No moving stops further from entry. Only trailing toward profit.

## Drawdown Circuit Breakers
- **Daily loss limit:** 2% of equity. Bot stops trading for the day if hit.
- **Weekly loss limit:** 5% of equity. Bot pauses for review.
- **Max drawdown trigger:** 15% from peak. Bot halts entirely. Manual restart only.

## Trade Frequency
- Max 10 open positions at once
- Max 5 new positions opened per day
- No trading in the first 15 minutes of the session (volatility / spread risk)
- No trading in the last 15 minutes unless closing existing positions

## Forbidden Behaviours
- No martingale / averaging down on a losing position
- No "revenge trades" after a stop-out — cooldown 1 hour
- No trading through earnings on positions held over the announcement (unless explicitly part of the strategy)
- No leverage beyond what risk rules permit, even if margin is available

## Live Phase Adjustments ($1k account)
- Per-trade risk drops to 0.5% (smaller account = less margin for error)
- Min position $50 to avoid commission/slippage swamping P&L
- Stricter universe filter: only the most liquid names

## Override
Only the user (Alex) can override a risk rule, and only via an explicit instruction logged in `decisions/log.md`. The bot itself cannot override.
