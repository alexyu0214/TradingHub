# Remote Bot Setup — GitHub Actions Deployment

This guide walks you through setting up the TradingHub bot to run 24/7 on GitHub Actions.

## Prerequisites

- GitHub repo for TradingHub (already set up)
- Alpaca API credentials (API key + secret key)
- Gemini API key (for secondary research)
- Claude API key (for automated workflow execution)

## Step 1: Add GitHub Secrets

Secrets are encrypted environment variables that Actions can access without exposing them in logs.

### How to Add Secrets

1. Go to your TradingHub repo on GitHub
2. Navigate to **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret** for each of these:

| Secret Name | Value | Source |
|---|---|---|
| `ALPACA_API_KEY` | Your Alpaca API key | Alpaca dashboard |
| `ALPACA_SECRET_KEY` | Your Alpaca secret key | Alpaca dashboard |
| `GEMINI_API_KEY` | Your Gemini API key | Google Cloud Console |
| `CLAUDE_API_KEY` | Your Claude API key | Anthropic Console |

**Important:** Never paste secrets into code or commit them. GitHub Secrets keeps them encrypted.

## Step 2: Enable GitHub Actions

1. Go to your TradingHub repo
2. Click **Actions** (top menu)
3. You should see the 5 workflows listed:
   - Pre-Market Research
   - Market-Open Execution
   - Midday Scan
   - Daily Summary
   - Weekly Review

If you don't see them, the workflows may be disabled. Click "Enable" if prompted.

## Step 3: Workflow Schedule

The workflows are set to run on this schedule (all times UTC):

| Workflow | Schedule | Day(s) | Cron Expression |
|---|---|---|---|
| Pre-Market Research | 1:00 PM UTC | Mon–Fri | `0 13 * * 1-5` |
| Market-Open Execution | 2:30 PM UTC | Mon–Fri | `30 14 * * 1-5` |
| Midday Scan | 5:00 PM UTC | Mon–Fri | `0 17 * * 1-5` |
| Daily Summary | 9:15 PM UTC | Mon–Fri | `15 21 * * 1-5` |
| Weekly Review | 9:15 PM UTC | Friday | `15 21 * * 5` |

**Note:** UTC times vary by season (EST/EDT). Adjust the cron expressions in `.github/workflows/*.yml` if needed.

### UTC to ET Conversion
- 1:00 PM UTC = 8:00 AM EST / 9:00 AM EDT
- 2:30 PM UTC = 9:30 AM EST / 10:30 AM EDT
- 5:00 PM UTC = 12:00 PM EST / 1:00 PM EDT
- 9:15 PM UTC = 4:15 PM EST / 5:15 PM EDT

## Step 4: Test a Workflow Manually

Before letting it run automatically, test one workflow to verify it works.

1. Go to **Actions** tab
2. Click on one of the workflows (e.g., "Pre-Market Research")
3. Click **Run workflow** → **Run workflow**
4. GitHub will execute it immediately

**What to check:**
- The workflow completes (green checkmark)
- Check the logs: click the workflow run → scroll through steps
- Verify no API keys leaked in logs (GitHub masks secrets)
- If the workflow wrote files, check that memory files were updated in the repo

## Step 5: Verify Memory Files Are Updated

After a test run, check that the memory files were committed to GitHub.

1. Go to the repo main page
2. Click **commits** or navigate to `.github/commits`
3. Look for recent commits from "TradingHub Bot" (e.g., `chore: pre-market research YYYY-MM-DD HH:MM:SS UTC`)
4. Click the commit to see which files changed
5. Verify memory files (e.g., `memory/RESEARCH-LOG.md`) were updated

## Step 6: Monitor Workflows

Once workflows are running automatically, monitor them to catch failures.

### Check Status
- **Actions tab** → View all recent workflow runs
- **GitHub status page** — Shows if Actions is experiencing downtime
- **Email notifications** — GitHub sends emails on workflow failure

### If a Workflow Fails
1. Click the failed workflow run
2. Expand the failed step to see error details
3. Common issues:
   - **API credentials missing or wrong** — Check GitHub Secrets
   - **Git auth failed** — GitHub token should be automatic; check logs
   - **API rate limit** — Wait and retry; consider adding delays
   - **Memory file conflict** — Manual edit conflicts with automated commit

## Step 7: Adjust Timings (Optional)

If the default UTC times don't work for your timezone, adjust the cron expressions.

**Cron format:** `minute hour day-of-month month day-of-week`

Examples:
- `0 13 * * 1-5` = 1:00 PM UTC, Mon–Fri
- `30 14 * * 1-5` = 2:30 PM UTC, Mon–Fri
- `15 21 * * 5` = 9:15 PM UTC, Friday

**To change a workflow's timing:**
1. Edit `.github/workflows/WORKFLOW_NAME.yml` in GitHub or locally
2. Update the `cron` line under `schedule:`
3. Commit and push (changes take effect immediately)

**Cron reference:** [crontab.guru](https://crontab.guru) — paste your expression to see when it runs.

## Step 8: Understanding Memory Files in GitHub

Memory files are stored in `memory/` and are the bot's persistent state across runs.

| File | Purpose | Written By |
|---|---|---|
| `memory/TRADING-STRATEGY.md` | Strategy library (living document) | Manual + weekly-review |
| `memory/TRADE-LOG.md` | Trade-by-trade log | market-open, midday, daily-summary |
| `memory/RESEARCH-LOG.md` | Daily research notes | pre-market, midday |
| `memory/DAILY-SUMMARY.md` | End-of-day summaries | daily-summary, market-open, midday |
| `memory/WEEKLY-REVIEW.md` | Weekly stats + grading | weekly-review |
| `memory/CONSTRAINTS.md` | Risk rules + limits | Manual (reference) |

**Note:** GitHub preserves full git history. You can revert changes or view past versions of any file.

## Step 9: Manual Fallback Procedures

If GitHub Actions is down or a workflow fails:

1. **Clone the repo locally**
   ```bash
   git clone <repo-url>
   cd TradingHub
   ```

2. **Create a local .env file with your secrets**
   ```bash
   cp .env.template .env
   # Edit .env and fill in your API keys
   ```

3. **Copy the appropriate prompt from `.claude/commands/ROUTINE.md`**

4. **Paste into Claude Code and run manually**

5. **Push changes back to GitHub**
   ```bash
   git add memory/
   git commit -m "manual execution: workflow-name"
   git push
   ```

## Step 10: Troubleshooting

### Workflow Never Runs
- **Check:** GitHub Actions is enabled (Settings → Actions)
- **Check:** Cron schedule is correct (use [crontab.guru](https://crontab.guru))
- **Note:** GitHub may have up to 10-minute delay; not guaranteed to run at exact time

### API Key Errors
- **Check:** All 4 secrets added to GitHub Settings
- **Check:** Secret names match exactly (case-sensitive)
- **Check:** Keys are current (not revoked/expired)

### Memory Files Not Updating
- **Check:** Workflow logs show no errors
- **Check:** Git credentials configured in workflow (already done in YAML)
- **Check:** No file conflicts (multiple workflows writing simultaneously)

### Git Push Fails
- **Cause:** Usually token issues (shouldn't happen; GitHub provides automatically)
- **Fix:** Try re-running the workflow; log a GitHub issue if it persists

## Step 11: Monitoring & Maintenance

### Weekly Checks
- Review memory files for accuracy (main page of repo)
- Check workflow run history (Actions tab)
- Note any anomalies or failures

### Monthly Tasks
- Verify memory files are growing (logs accumulating)
- Check GitHub storage usage (Settings → Usage)
- Review P&L and trading stats

### API Key Rotation
- Rotate Alpaca keys annually (or per their policy)
- Rotate Claude and Gemini keys as recommended
- Update GitHub Secrets immediately after rotation

## Example: Full Week of Automated Runs

```
Monday 1:00 PM UTC (8 AM ET):  Pre-market research
Monday 2:30 PM UTC (9:30 AM ET): Market-open execution
Monday 5:00 PM UTC (12 PM ET):   Midday scan
Monday 9:15 PM UTC (4:15 PM ET): Daily summary

Tuesday 1:00 PM UTC: Pre-market research
... (repeat) ...

Friday 1:00 PM UTC:   Pre-market research
Friday 2:30 PM UTC:   Market-open execution
Friday 5:00 PM UTC:   Midday scan
Friday 9:15 PM UTC:   Daily summary + weekly review

Saturday–Sunday: No scheduled runs (market closed)
```

## Next Steps

1. Add all 4 secrets to GitHub
2. Test one workflow manually
3. Verify memory files updated
4. Enable remaining workflows
5. Monitor for 24 hours to confirm all run on schedule
6. Adjust timings if needed
7. Set up email notifications for failures

---

**Need help?** Check GitHub Actions documentation: https://docs.github.com/en/actions
