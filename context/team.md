# Team

**Solo operator.** I run the account, set risk limits, and make the final call.

## AI Roles
| Agent | Role |
|---|---|
| Claude (this assistant) | Bot architect, strategy designer, code author, trade analyst |
| Gemini | Secondary research / sanity checks when needed |

## Decision Protocol
1. **Instructions first.** When deciding any trade, Claude must check user-provided instructions/playbook before anything else.
2. **Technical analysis second.** After instructions, apply the most appropriate TA for the setup.
3. **Risk rules always.** No trade goes through that violates `projects/trading-bot/risk-rules.md`.
