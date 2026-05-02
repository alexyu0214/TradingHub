#!/usr/bin/env python3
"""Generate dark-themed PDF report and send via Telegram.

Usage: python scripts/send_report.py <daily|weekly>

Reads from memory/*.md files, calls Gemini for tomorrow's watchlist,
renders a TradingHub-branded dark/teal PDF, and sends via Telegram Bot API.

Required env vars: TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, GEMINI_API_KEY
"""

from __future__ import annotations

import json
import os
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Sprint constants
# ---------------------------------------------------------------------------

SPRINT_START = date(2026, 5, 1)
SPRINT_DAYS = 90
PAPER_TARGET_EQUITY = 130_000.0  # +30% on $100k validates the strategy
STARTING_EQUITY = 100_000.0

# Risk thresholds (mirrored from memory/CONSTRAINTS.md)
DAILY_LOSS_LIMIT_PCT = -2.0
WEEKLY_LOSS_LIMIT_PCT = -5.0
MAX_DRAWDOWN_PCT = -15.0
MAX_TRADES_PER_WEEK = 3
MAX_DAYTRADES = 3
MAX_POSITIONS = 6

# ---------------------------------------------------------------------------
# Theme (dark + teal)
# ---------------------------------------------------------------------------

THEME = {
    "bg": "#0f172a",
    "card": "#1e293b",
    "border": "#334155",
    "teal": "#2dd4bf",
    "teal_dim": "#14b8a6",
    "text": "#e2e8f0",
    "muted": "#94a3b8",
    "success": "#10b981",
    "warning": "#f59e0b",
    "danger": "#ef4444",
}


# ---------------------------------------------------------------------------
# Markdown helpers
# ---------------------------------------------------------------------------

def extract_last_entry(content: str) -> str:
    parts = content.rsplit("\n## ", 1)
    return ("## " + parts[1]) if len(parts) == 2 else content


def read_safe(path: str) -> str:
    p = Path(path)
    return p.read_text(encoding="utf-8") if p.exists() else ""


# ---------------------------------------------------------------------------
# Data extraction from markdown
# ---------------------------------------------------------------------------

def parse_daily_kpis(daily_md: str) -> dict[str, Any]:
    """Pull KPIs from latest DAILY-SUMMARY.md entry."""
    last = extract_last_entry(daily_md)
    out: dict[str, Any] = {
        "equity": None, "cash": None, "deployed_pct": None,
        "day_pl_dollar": None, "day_pl_pct": None,
        "phase_pl_dollar": None, "phase_pl_pct": None,
        "daytrade_count": None,
    }

    # **Portfolio:** $99,889.50 (-0.11% day, -0.11% phase)
    m = re.search(
        r"\*\*Portfolio:\*\*\s*\$([0-9,]+(?:\.\d+)?)\s*\(([+\-]?\d+\.\d+)%\s*day,\s*([+\-]?\d+\.\d+)%\s*phase\)",
        last,
    )
    if m:
        out["equity"] = float(m.group(1).replace(",", ""))
        out["day_pl_pct"] = float(m.group(2))
        out["phase_pl_pct"] = float(m.group(3))
        if out["equity"] is not None:
            out["day_pl_dollar"] = out["equity"] * out["day_pl_pct"] / 100
            out["phase_pl_dollar"] = out["equity"] - STARTING_EQUITY

    m = re.search(r"\*\*Cash:\*\*\s*\$([0-9,]+(?:\.\d+)?)\s*\((\d+(?:\.\d+)?)%\)", last)
    if m:
        out["cash"] = float(m.group(1).replace(",", ""))

    m = re.search(r"\*\*Deployed:\*\*\s*(\d+(?:\.\d+)?)%", last)
    if m:
        out["deployed_pct"] = float(m.group(1))

    m = re.search(r"\*\*Daytrade count:\*\*\s*(\d+)\s*/\s*(\d+)", last)
    if m:
        out["daytrade_count"] = int(m.group(1))

    return out


def parse_trades_today(trade_log_md: str, today: date) -> list[dict[str, Any]]:
    """Find today's BUY/SELL entries in TRADE-LOG.md (not EOD snapshots)."""
    date_str = today.strftime("%Y-%m-%d")
    trades: list[dict[str, Any]] = []
    # Match blocks like: ### 2026-05-02 09:32 — BUY XOM
    pattern = (
        rf"### {re.escape(date_str)}\s+(\d{{2}}:\d{{2}})\s*—\s*(BUY|SELL|EXIT)\s+([A-Z]+)"
        r"(.*?)(?=\n### |\Z)"
    )
    for m in re.finditer(pattern, trade_log_md, re.DOTALL):
        time_str, side, ticker, body = m.group(1), m.group(2), m.group(3), m.group(4)
        catalyst = _grab(body, r"\*\*Catalyst:\*\*\s*(.+?)(?:\n|\Z)")
        entry_m = re.search(r"\*\*Entry Price:\*\*\s*\$([0-9.]+).*?\((\d+)\s*shares", body)
        stop_m = re.search(r"\*\*Stop:\*\*\s*\$([0-9.]+)", body)
        target_m = re.search(r"\*\*Target:\*\*\s*\$([0-9.]+)", body)
        thesis = _grab(body, r"\*\*Thesis:\*\*\s*(.+?)(?:\n\*\*|\Z)", default="")

        trades.append({
            "time": time_str,
            "side": side,
            "ticker": ticker,
            "qty": int(entry_m.group(2)) if entry_m else None,
            "entry": float(entry_m.group(1)) if entry_m else None,
            "stop": float(stop_m.group(1)) if stop_m else None,
            "target": float(target_m.group(1)) if target_m else None,
            "catalyst": catalyst,
            "thesis": thesis.strip().replace("\n", " "),
        })
    return trades


def parse_open_positions(daily_md: str) -> list[dict[str, Any]]:
    """Extract positions table from latest TRADE-LOG EOD entry if present."""
    # The EOD snapshot in TRADE-LOG.md has a table like:
    # | Ticker | Shares | Entry | Close | Unrealized P&L | Stop | Time |
    last = extract_last_entry(daily_md)
    positions: list[dict[str, Any]] = []
    for line in last.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 6 and re.match(r"^[A-Z]{1,5}$", cells[0]):
            positions.append({
                "ticker": cells[0],
                "qty": cells[1],
                "entry": cells[2],
                "close": cells[3],
                "unrealized": cells[4],
                "stop": cells[5],
            })
    return positions


def parse_decision_notes(daily_md: str) -> str:
    last = extract_last_entry(daily_md)
    m = re.search(r"\*\*Notes:\*\*\s*(.+?)(?:\n---|\n\*\*|\Z)", last, re.DOTALL)
    return m.group(1).strip() if m else ""


def parse_market_context(research_md: str) -> str:
    """Pull a compact market context line from RESEARCH-LOG."""
    last = extract_last_entry(research_md)
    m = re.search(r"###\s*Market Context\s*\n(.+?)(?=\n###|\Z)", last, re.DOTALL)
    if not m:
        return ""
    return m.group(1).strip()


def _grab(text: str, pattern: str, default: str = "") -> str:
    m = re.search(pattern, text, re.DOTALL)
    return m.group(1).strip() if m else default


# ---------------------------------------------------------------------------
# Gemini: tomorrow's watchlist
# ---------------------------------------------------------------------------

def gemini_tomorrow_watchlist() -> list[dict[str, str]]:
    """Use Gemini with Google Search grounding to identify 5 watchlist candidates."""
    try:
        from google import genai
        from google.genai import types
    except ImportError:
        return []

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return []

    client = genai.Client(api_key=api_key)
    tomorrow = (date.today() + timedelta(days=1)).strftime("%A %B %d, %Y")
    prompt = (
        f"Identify exactly 5 US large-cap stocks worth watching for the trading "
        f"session on {tomorrow}. Focus on names with concrete catalysts: earnings "
        f"(pre/post-market), Fed/macro events, or technical setups (RSI<30 in "
        f"uptrend, oversold bounce, breakout from base).\n\n"
        f"Return ONLY a JSON array, no prose. Each entry must have these exact keys:\n"
        f'  "ticker"   — string, e.g. "NVDA"\n'
        f'  "catalyst" — string, the specific event/news driving the setup tomorrow\n'
        f'  "setup"    — string, the technical or fundamental pattern\n'
        f'  "why"      — string, one sentence on why it\'s high-probability\n\n'
        f"Skip: OTC names, penny stocks, micro-caps, illiquid tickers."
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                tools=[types.Tool(google_search=types.GoogleSearch())],
            ),
        )
        text = (response.text or "").strip()
        # Strip markdown code fences if present
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
        data = json.loads(text)
        if isinstance(data, list):
            return data[:5]
    except Exception as e:
        print(f"  [gemini watchlist] failed: {e}")
    return []


# ---------------------------------------------------------------------------
# HTML rendering
# ---------------------------------------------------------------------------

def fmt_money(v: float | None, sign: bool = False) -> str:
    if v is None:
        return "—"
    s = f"${abs(v):,.2f}"
    if sign:
        return ("+" if v >= 0 else "-") + s
    return s if v >= 0 else f"-{s}"


def fmt_pct(v: float | None, sign: bool = True) -> str:
    if v is None:
        return "—"
    if sign:
        return f"{v:+.2f}%"
    return f"{v:.2f}%"


def status_color(value: float | None, danger_threshold: float, warn_at: float = 0.5) -> str:
    """Green if positive/safe, yellow if approaching limit, red if past it."""
    if value is None:
        return THEME["muted"]
    if value <= danger_threshold:
        return THEME["danger"]
    if value <= danger_threshold * warn_at:
        return THEME["warning"]
    return THEME["success"]


def render_daily_html(ctx: dict[str, Any]) -> str:
    kpis = ctx["kpis"]
    trades = ctx["trades"]
    positions = ctx["positions"]
    watchlist = ctx["watchlist"]
    market = ctx["market_context"]
    notes = ctx["notes"]
    day_n = ctx["day_n"]
    today = ctx["today"]

    def kpi_card(label: str, value: str, color: str = THEME["teal"]) -> str:
        return f"""
        <div class="kpi-card">
          <div class="kpi-value" style="color:{color}">{value}</div>
          <div class="kpi-label">{label}</div>
        </div>"""

    kpi_section = f"""
    <div class="kpi-row">
      {kpi_card("Day P&L", fmt_money(kpis.get("day_pl_dollar"), sign=True),
                THEME["success"] if (kpis.get("day_pl_pct") or 0) >= 0 else THEME["danger"])}
      {kpi_card("Account Δ", fmt_pct(kpis.get("day_pl_pct")),
                THEME["success"] if (kpis.get("day_pl_pct") or 0) >= 0 else THEME["danger"])}
      {kpi_card("Days Left", f"{SPRINT_DAYS - day_n} days")}
    </div>"""

    risk_section = f"""
    <div class="kpi-row">
      {kpi_card("Trades / Week", f"— / {MAX_TRADES_PER_WEEK}")}
      {kpi_card("Daytrades Today", f"{kpis.get('daytrade_count', 0)} / {MAX_DAYTRADES}")}
      {kpi_card("Deployed",
                f"{kpis.get('deployed_pct'):.0f}%" if kpis.get('deployed_pct') else "—")}
    </div>"""

    # Trades executed today
    if trades:
        trade_rows = ""
        for t in trades:
            trade_rows += f"""
            <tr>
              <td>{t.get('time') or '—'}</td>
              <td><span class="badge badge-{('success' if t['side']=='BUY' else 'danger')}">{t['side']}</span></td>
              <td class="mono"><strong>{t['ticker']}</strong></td>
              <td>{t.get('qty') or '—'}</td>
              <td>{fmt_money(t.get('entry'))}</td>
              <td>{fmt_money(t.get('stop'))}</td>
              <td>{fmt_money(t.get('target'))}</td>
            </tr>"""
            if t.get('catalyst') or t.get('thesis'):
                thesis_text = t.get('thesis') or t.get('catalyst', '')
                trade_rows += f"""
                <tr class="thesis-row">
                  <td colspan="7">
                    <div class="thesis"><strong>{t['ticker']}</strong> · {thesis_text[:300]}</div>
                  </td>
                </tr>"""
        trades_section = f"""
        <h2>Trades Executed Today</h2>
        <table>
          <thead><tr>
            <th>Time</th><th>Side</th><th>Ticker</th><th>Qty</th>
            <th>Entry</th><th>Stop</th><th>Target</th>
          </tr></thead>
          <tbody>{trade_rows}</tbody>
        </table>"""
    else:
        trades_section = """
        <h2>Trades Executed Today</h2>
        <div class="empty">No trades placed today. Patience rule applied.</div>"""

    # Open positions
    if positions:
        pos_rows = ""
        for p in positions:
            pos_rows += f"""
            <tr>
              <td class="mono"><strong>{p['ticker']}</strong></td>
              <td>{p.get('qty', '—')}</td>
              <td>{p.get('entry', '—')}</td>
              <td>{p.get('close', '—')}</td>
              <td>{p.get('unrealized', '—')}</td>
              <td>{p.get('stop', '—')}</td>
            </tr>"""
        positions_section = f"""
        <h2>Open Positions — End of Day</h2>
        <table>
          <thead><tr>
            <th>Ticker</th><th>Qty</th><th>Entry</th><th>Close</th>
            <th>Unrealized</th><th>Stop</th>
          </tr></thead>
          <tbody>{pos_rows}</tbody>
        </table>"""
    else:
        positions_section = """
        <h2>Open Positions — End of Day</h2>
        <div class="empty">No open positions. Full cash.</div>"""

    # Tomorrow's watchlist (Gemini)
    if watchlist:
        wl_html = ""
        for w in watchlist:
            wl_html += f"""
            <div class="watch-item">
              <div class="watch-header">
                <span class="ticker mono">{w.get('ticker', '?')}</span>
                <span class="watch-setup">{w.get('setup', '')}</span>
              </div>
              <div class="watch-catalyst"><strong>Catalyst:</strong> {w.get('catalyst', '')}</div>
              <div class="watch-why">{w.get('why', '')}</div>
            </div>"""
        watchlist_section = f"""
        <h2>Tomorrow's Watch List <span class="research-tag">Gemini-grounded</span></h2>
        <div class="watchlist">{wl_html}</div>"""
    else:
        watchlist_section = """
        <h2>Tomorrow's Watch List</h2>
        <div class="empty">Watchlist research unavailable. Will refresh in pre-market run.</div>"""

    # Market context
    market_section = f"""
    <h2>Market Context (EOD)</h2>
    <div class="market-context">{market or 'No market context captured.'}</div>""" if market else ""

    # Circuit breakers
    daily_status = status_color(kpis.get("day_pl_pct"), DAILY_LOSS_LIMIT_PCT)
    weekly_status = status_color(kpis.get("phase_pl_pct"), WEEKLY_LOSS_LIMIT_PCT)
    drawdown_status = status_color(kpis.get("phase_pl_pct"), MAX_DRAWDOWN_PCT)
    cb_section = f"""
    <h2>Circuit Breakers</h2>
    <div class="breakers">
      <div class="breaker"><span class="dot" style="background:{daily_status}"></span>
        <span>Daily loss</span><span class="mono">{fmt_pct(kpis.get("day_pl_pct"))} · limit {DAILY_LOSS_LIMIT_PCT}%</span></div>
      <div class="breaker"><span class="dot" style="background:{weekly_status}"></span>
        <span>Weekly loss</span><span class="mono">{fmt_pct(kpis.get("phase_pl_pct"))} · limit {WEEKLY_LOSS_LIMIT_PCT}%</span></div>
      <div class="breaker"><span class="dot" style="background:{drawdown_status}"></span>
        <span>Max drawdown</span><span class="mono">{fmt_pct(kpis.get("phase_pl_pct"))} · limit {MAX_DRAWDOWN_PCT}%</span></div>
    </div>"""

    notes_section = f"""
    <h2>Decision Notes</h2>
    <div class="notes">{notes}</div>""" if notes else ""

    return _wrap_html(
        title=f"TradingHub Daily Log · {today}",
        subtitle=f"120-Day Sprint · Day {day_n} of {SPRINT_DAYS} · Daily Log · {today}",
        body=kpi_section + risk_section + trades_section + positions_section
             + watchlist_section + market_section + cb_section + notes_section,
    )


def render_weekly_html(ctx: dict[str, Any]) -> str:
    kpis = ctx["kpis"]
    today = ctx["today"]
    day_n = ctx["day_n"]
    watchlist = ctx["watchlist"]
    notes = ctx["notes"]

    pct_to_target = 0.0
    if kpis.get("equity"):
        pct_to_target = (
            (kpis["equity"] - STARTING_EQUITY) / (PAPER_TARGET_EQUITY - STARTING_EQUITY) * 100
        )
    pct_to_target = max(0.0, min(100.0, pct_to_target))

    weekly_section = f"""
    <div class="kpi-row">
      <div class="kpi-card">
        <div class="kpi-value" style="color:{THEME['teal']}">{fmt_money(kpis.get('phase_pl_dollar'), sign=True)}</div>
        <div class="kpi-label">Phase P&L</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-value" style="color:{THEME['teal']}">{fmt_money(STARTING_EQUITY)}</div>
        <div class="kpi-label">Starting Capital</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-value" style="color:{THEME['teal']}">{fmt_money(kpis.get('equity'))}</div>
        <div class="kpi-label">Current Equity</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-value" style="color:{THEME['teal']}">{fmt_money((PAPER_TARGET_EQUITY - STARTING_EQUITY) / SPRINT_DAYS)}</div>
        <div class="kpi-label">Daily Gain Target</div>
      </div>
    </div>

    <h2>Trajectory to ${PAPER_TARGET_EQUITY:,.0f} <span style="color:{THEME['muted']};font-weight:400">(paper validation +30%)</span></h2>
    <div class="progress-track">
      <div class="progress-fill" style="width:{pct_to_target:.1f}%"></div>
    </div>
    <div class="progress-label">{pct_to_target:.1f}% of paper target achieved · Day {day_n} of {SPRINT_DAYS}</div>
    """

    wl_section = ""
    if watchlist:
        wl_html = ""
        for w in watchlist:
            wl_html += f"""
            <div class="watch-item">
              <div class="watch-header">
                <span class="ticker mono">{w.get('ticker', '?')}</span>
                <span class="watch-setup">{w.get('setup', '')}</span>
              </div>
              <div class="watch-catalyst"><strong>Catalyst:</strong> {w.get('catalyst', '')}</div>
              <div class="watch-why">{w.get('why', '')}</div>
            </div>"""
        wl_section = f"""
        <h2>Next Week Priority Watchlist <span class="research-tag">Gemini-grounded</span></h2>
        <div class="watchlist">{wl_html}</div>"""

    notes_section = f"""
    <h2>Strategic Retrospective</h2>
    <div class="notes">{notes}</div>""" if notes else ""

    return _wrap_html(
        title=f"TradingHub Weekly Review · {today}",
        subtitle=f"120-Day Sprint · Week ending {today}",
        body=weekly_section + wl_section + notes_section,
    )


def _wrap_html(title: str, subtitle: str, body: str) -> str:
    t = THEME
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{title}</title>
<style>
@page {{ size: A4; margin: 1.4cm 1.5cm; background: {t['bg']}; }}
* {{ box-sizing: border-box; }}
body {{
  font-family: -apple-system, "Segoe UI", "Helvetica Neue", Arial, sans-serif;
  font-size: 10pt; line-height: 1.45; color: {t['text']};
  background: {t['bg']}; margin: 0; padding: 0;
}}
.header {{
  border-left: 4px solid {t['teal']}; padding: 4px 0 4px 14px; margin-bottom: 8px;
}}
.brand {{
  font-size: 22pt; font-weight: 700; color: {t['teal']};
  letter-spacing: 0.5px; margin: 0;
}}
.subtitle {{ color: {t['muted']}; font-size: 9.5pt; margin-top: 2px; }}
.divider {{ border: 0; border-top: 2px solid {t['teal']}; margin: 6px 0 18px 0; }}
h2 {{
  color: {t['text']}; font-size: 11pt; text-transform: uppercase;
  letter-spacing: 0.8px; margin: 22px 0 10px 0;
  padding: 7px 12px; background: {t['card']}; border-left: 3px solid {t['teal']};
  border-radius: 2px;
}}
.kpi-row {{ display: flex; gap: 10px; margin-bottom: 8px; }}
.kpi-card {{
  flex: 1; background: {t['card']}; border-radius: 6px; padding: 14px 12px;
  text-align: center; border: 1px solid {t['border']};
}}
.kpi-value {{ font-size: 18pt; font-weight: 700; color: {t['teal']}; line-height: 1.1; }}
.kpi-label {{ font-size: 8pt; color: {t['muted']}; text-transform: uppercase; letter-spacing: 0.6px; margin-top: 4px; }}
table {{ width: 100%; border-collapse: collapse; margin: 0 0 4px 0; font-size: 9.5pt; background: {t['card']}; border-radius: 4px; overflow: hidden; }}
th {{ background: {t['border']}; color: {t['teal']}; text-transform: uppercase; font-size: 8.5pt; letter-spacing: 0.5px; padding: 7px 10px; text-align: left; }}
td {{ padding: 7px 10px; border-top: 1px solid {t['border']}; }}
.mono {{ font-family: "SF Mono", Consolas, monospace; }}
.thesis-row td {{ padding: 0 10px 10px 10px; border-top: 0; }}
.thesis {{ background: rgba(45,212,191,0.07); border-left: 2px solid {t['teal']}; padding: 8px 12px; font-size: 9pt; color: {t['text']}; border-radius: 2px; }}
.badge {{ padding: 2px 8px; border-radius: 3px; font-weight: 600; font-size: 8.5pt; letter-spacing: 0.5px; }}
.badge-success {{ background: rgba(16,185,129,0.15); color: {t['success']}; }}
.badge-danger {{ background: rgba(239,68,68,0.15); color: {t['danger']}; }}
.empty {{ background: {t['card']}; padding: 16px; border-radius: 6px; color: {t['muted']}; font-style: italic; text-align: center; }}
.watchlist {{ display: flex; flex-direction: column; gap: 8px; }}
.watch-item {{ background: {t['card']}; border: 1px solid {t['border']}; border-left: 3px solid {t['teal']}; border-radius: 4px; padding: 10px 14px; }}
.watch-header {{ display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px; }}
.ticker {{ font-size: 12pt; color: {t['teal']}; font-weight: 700; }}
.watch-setup {{ color: {t['muted']}; font-size: 8.5pt; text-transform: uppercase; letter-spacing: 0.5px; }}
.watch-catalyst {{ font-size: 9.5pt; margin-bottom: 3px; }}
.watch-why {{ color: {t['muted']}; font-size: 9pt; font-style: italic; }}
.research-tag {{ font-size: 8pt; background: rgba(45,212,191,0.15); color: {t['teal']}; padding: 2px 8px; border-radius: 3px; margin-left: 8px; font-weight: 500; letter-spacing: 0.5px; text-transform: uppercase; vertical-align: middle; }}
.market-context {{ background: {t['card']}; border-radius: 4px; padding: 12px 16px; white-space: pre-wrap; font-size: 9.5pt; }}
.breakers {{ display: flex; flex-direction: column; gap: 5px; }}
.breaker {{ display: flex; align-items: center; gap: 12px; background: {t['card']}; padding: 9px 14px; border-radius: 4px; font-size: 9.5pt; }}
.breaker .dot {{ width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; }}
.breaker > span:nth-child(2) {{ flex: 1; }}
.breaker .mono {{ color: {t['muted']}; font-size: 9pt; }}
.notes {{ background: {t['card']}; border-radius: 4px; padding: 12px 16px; font-size: 9.5pt; line-height: 1.55; }}
.progress-track {{ background: {t['card']}; height: 18px; border-radius: 9px; overflow: hidden; border: 1px solid {t['border']}; }}
.progress-fill {{ background: linear-gradient(90deg, {t['teal_dim']}, {t['teal']}); height: 100%; transition: width 0.3s; }}
.progress-label {{ color: {t['muted']}; font-size: 9pt; margin-top: 6px; text-align: right; }}
.footer {{ margin-top: 20px; padding-top: 10px; border-top: 1px solid {t['border']}; color: {t['muted']}; font-size: 8.5pt; text-align: center; letter-spacing: 0.5px; }}
</style></head><body>
<div class="header">
  <div class="brand">TRADINGHUB</div>
  <div class="subtitle">{subtitle}</div>
</div>
<hr class="divider"/>
{body}
<div class="footer">TradingHub · Confidential · {datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")}</div>
</body></html>"""


# ---------------------------------------------------------------------------
# PDF + Telegram delivery
# ---------------------------------------------------------------------------

def html_to_pdf(html: str, output_path: str) -> None:
    from weasyprint import HTML
    HTML(string=html).write_pdf(output_path)
    print(f"PDF written: {output_path}")


def send_telegram(pdf_path: str, caption: str) -> None:
    import httpx
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    url = f"https://api.telegram.org/bot{token}/sendDocument"
    print(f"Sending PDF to Telegram chat {chat_id}")
    with open(pdf_path, "rb") as f:
        files = {"document": (Path(pdf_path).name, f, "application/pdf")}
        data = {"chat_id": chat_id, "caption": caption, "parse_mode": "Markdown"}
        r = httpx.post(url, files=files, data=data, timeout=30.0)
        r.raise_for_status()
    print(f"Telegram delivery OK")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main(report_type: str) -> None:
    today = date.today()
    today_str = today.strftime("%Y-%m-%d")
    day_n = (today - SPRINT_START).days + 1

    daily_md = read_safe("memory/DAILY-SUMMARY.md")
    trade_md = read_safe("memory/TRADE-LOG.md")
    research_md = read_safe("memory/RESEARCH-LOG.md")

    if not daily_md and not trade_md:
        print("No memory files to report from. Exiting.")
        sys.exit(0)

    print("Parsing memory files...")
    kpis = parse_daily_kpis(daily_md)
    trades = parse_trades_today(trade_md, today)
    positions = parse_open_positions(trade_md)
    market_ctx = parse_market_context(research_md)
    notes = parse_decision_notes(daily_md)

    print("Calling Gemini for tomorrow's watchlist...")
    watchlist = gemini_tomorrow_watchlist()

    ctx = {
        "today": today_str, "day_n": day_n,
        "kpis": kpis, "trades": trades, "positions": positions,
        "watchlist": watchlist, "market_context": market_ctx, "notes": notes,
    }

    if report_type == "daily":
        html = render_daily_html(ctx)
        pdf_path = f"tradinghub-daily-{today_str}.pdf"
        subject = f"TradingHub Daily Log · {today_str}"
    else:
        html = render_weekly_html(ctx)
        pdf_path = f"tradinghub-weekly-{today_str}.pdf"
        subject = f"TradingHub Weekly Review · {today_str}"

    html_to_pdf(html, pdf_path)
    caption = (
        f"*{subject}*\n"
        f"Day {day_n} of {SPRINT_DAYS} · "
        f"Equity {fmt_money(kpis.get('equity'))} "
        f"({fmt_pct(kpis.get('phase_pl_pct'))})"
    )
    send_telegram(pdf_path, caption)


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ("daily", "weekly"):
        print(f"Usage: {sys.argv[0]} <daily|weekly>")
        sys.exit(1)
    main(sys.argv[1])
