#!/usr/bin/env python3
"""Generate a PDF from the latest daily/weekly report and send it via Telegram.

Usage: python scripts/send_report.py <daily|weekly>

Reads from memory/DAILY-SUMMARY.md or memory/WEEKLY-REVIEW.md, extracts the
most recent entry, renders to PDF, and sends as a document via the Telegram
Bot API.

Required env vars: TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
"""

import os
import sys
from datetime import datetime
from pathlib import Path


REPORT_TYPES = {
    "daily": {
        "source": "memory/DAILY-SUMMARY.md",
        "subject": "TradingHub Daily Summary — {date}",
        "filename": "tradinghub-daily-{date}.pdf",
    },
    "weekly": {
        "source": "memory/WEEKLY-REVIEW.md",
        "subject": "TradingHub Weekly Review — {date}",
        "filename": "tradinghub-weekly-{date}.pdf",
    },
}


def extract_last_entry(content: str) -> str:
    """Return everything from the last top-level (## …) entry to the end of file.
    Falls back to the full content if no ## heading exists."""
    parts = content.rsplit("\n## ", 1)
    if len(parts) == 2:
        return "## " + parts[1]
    return content


def md_to_pdf(md_content: str, output_path: str, title: str) -> None:
    """Render markdown content to a styled PDF file."""
    import markdown
    from weasyprint import HTML

    html_body = markdown.markdown(
        md_content, extensions=["tables", "fenced_code", "nl2br"]
    )

    styled = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{title}</title>
  <style>
    @page {{ size: A4; margin: 1.5cm 2cm; }}
    body {{
      font-family: -apple-system, "Segoe UI", "Helvetica Neue", Arial, sans-serif;
      font-size: 10.5pt;
      line-height: 1.45;
      color: #1a1a1a;
    }}
    h1, h2, h3, h4 {{ color: #0d47a1; margin-top: 1.2em; margin-bottom: 0.4em; }}
    h1 {{ font-size: 18pt; border-bottom: 2px solid #0d47a1; padding-bottom: 4px; }}
    h2 {{ font-size: 14pt; }}
    h3 {{ font-size: 12pt; }}
    table {{ border-collapse: collapse; width: 100%; margin: 0.8em 0; font-size: 9.5pt; }}
    th, td {{ border: 1px solid #cfd8dc; padding: 5px 8px; text-align: left; }}
    th {{ background: #eceff1; font-weight: 600; }}
    code {{
      background: #f5f5f5; padding: 1px 5px; border-radius: 3px;
      font-family: "SF Mono", Consolas, monospace; font-size: 9.5pt;
    }}
    pre {{
      background: #f5f5f5; padding: 10px; border-radius: 5px;
      overflow-x: auto; font-size: 9.5pt;
    }}
    blockquote {{
      border-left: 3px solid #90a4ae; padding-left: 12px;
      color: #455a64; margin: 0.8em 0;
    }}
    hr {{ border: 0; border-top: 1px solid #cfd8dc; margin: 1.5em 0; }}
    .header {{ color: #607d8b; font-size: 9pt; margin-bottom: 1em; }}
  </style>
</head>
<body>
  <div class="header">Generated {datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")} · TradingHub Bot</div>
  {html_body}
</body>
</html>
"""
    HTML(string=styled).write_pdf(output_path)
    print(f"PDF written: {output_path}")


def send_telegram(pdf_path: str, caption: str) -> None:
    """Send the PDF as a Telegram document via Bot API."""
    import httpx  # already a transitive dep of the anthropic SDK

    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    url = f"https://api.telegram.org/bot{token}/sendDocument"

    print(f"Sending PDF to Telegram chat {chat_id}")
    with open(pdf_path, "rb") as f:
        files = {"document": (Path(pdf_path).name, f, "application/pdf")}
        data = {
            "chat_id": chat_id,
            "caption": caption,
            "parse_mode": "Markdown",
        }
        r = httpx.post(url, files=files, data=data, timeout=30.0)
        r.raise_for_status()
    print(f"Telegram delivery OK: {r.json().get('result', {}).get('message_id')}")


def main(report_type: str) -> None:
    cfg = REPORT_TYPES[report_type]
    src = Path(cfg["source"])
    if not src.exists():
        print(f"Source file missing: {src}. Nothing to send.")
        sys.exit(0)

    full = src.read_text(encoding="utf-8")
    body_md = extract_last_entry(full).strip()
    if not body_md:
        print(f"No content in {src}. Nothing to send.")
        sys.exit(0)

    today = datetime.utcnow().strftime("%Y-%m-%d")
    pdf_path = cfg["filename"].format(date=today)
    subject = cfg["subject"].format(date=today)
    md_to_pdf(body_md, pdf_path, title=subject)

    caption = (
        f"*{subject}*\n"
        f"Generated {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}"
    )
    send_telegram(pdf_path, caption)


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in REPORT_TYPES:
        print(f"Usage: {sys.argv[0]} <{'|'.join(REPORT_TYPES)}>")
        sys.exit(1)
    main(sys.argv[1])
