#!/usr/bin/env bash
# Alpaca API wrapper. All trading API calls go through here.
# Usage: bash scripts/alpaca.sh <subcommand> [args...]
# Env vars: ALPACA_API_KEY, ALPACA_SECRET_KEY (read from .env first, then process env)

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ENV_FILE="$ROOT/.env"

# Load .env if it exists (local testing)
if [[ -f "$ENV_FILE" ]]; then
    set -a
    # shellcheck disable=SC1090
    source "$ENV_FILE"
    set +a
fi

# Check required credentials
: "${ALPACA_API_KEY:?ALPACA_API_KEY not set in environment}"
: "${ALPACA_SECRET_KEY:?ALPACA_SECRET_KEY not set in environment}"

# API endpoints
API="${ALPACA_ENDPOINT:-https://api.alpaca.markets/v2}"
DATA="${ALPACA_DATA_ENDPOINT:-https://data.alpaca.markets/v2}"

# Headers for API calls
H_KEY="APCA-API-KEY-ID: $ALPACA_API_KEY"
H_SEC="APCA-API-SECRET-KEY: $ALPACA_SECRET_KEY"

cmd="${1:-}"
shift || true

case "$cmd" in
    account)
        curl -fsS -H "$H_KEY" -H "$H_SEC" "$API/account"
        ;;
    positions)
        curl -fsS -H "$H_KEY" -H "$H_SEC" "$API/positions"
        ;;
    position)
        sym="${1:?usage: position SYM}"
        curl -fsS -H "$H_KEY" -H "$H_SEC" "$API/positions/$sym"
        ;;
    quote)
        sym="${1:?usage: quote SYM}"
        curl -fsS -H "$H_KEY" -H "$H_SEC" "$DATA/stocks/$sym/quotes/latest"
        ;;
    bars)
        # Return last N daily bars (closes/OHLCV) for a symbol. Used for Z-Score / mean reversion math.
        # Usage: bash scripts/alpaca.sh bars SYM [N=25]
        sym="${1:?usage: bars SYM [N]}"
        n="${2:-25}"
        # Fetch last (N + 5) calendar days to ensure we get N trading bars
        days_back=$((n + 10))
        start=$(python -c "from datetime import datetime, timedelta, timezone; print((datetime.now(timezone.utc) - timedelta(days=$days_back)).strftime('%Y-%m-%d'))" 2>/dev/null || date -d "$days_back days ago" -u +%Y-%m-%d 2>/dev/null || date -v-${days_back}d -u +%Y-%m-%d)
        curl -fsS -H "$H_KEY" -H "$H_SEC" \
            "$DATA/stocks/$sym/bars?timeframe=1Day&start=${start}&limit=$n&adjustment=raw"
        ;;
    orders)
        status="${1:-open}"
        curl -fsS -H "$H_KEY" -H "$H_SEC" "$API/orders?status=$status"
        ;;
    order)
        body="${1:?usage: order '<json>'}"
        curl -fsS -H "$H_KEY" -H "$H_SEC" -H "Content-Type: application/json" \
            -X POST -d "$body" "$API/orders"
        ;;
    cancel)
        oid="${1:?usage: cancel ORDER_ID}"
        curl -fsS -H "$H_KEY" -H "$H_SEC" -X DELETE "$API/orders/$oid"
        ;;
    cancel-all)
        curl -fsS -H "$H_KEY" -H "$H_SEC" -X DELETE "$API/orders"
        ;;
    close)
        sym="${1:?usage: close SYM}"
        curl -fsS -H "$H_KEY" -H "$H_SEC" -X DELETE "$API/positions/$sym"
        ;;
    close-all)
        curl -fsS -H "$H_KEY" -H "$H_SEC" -X DELETE "$API/positions"
        ;;
    *)
        echo "Usage: bash scripts/alpaca.sh <account|positions|position|quote|bars|orders|order|cancel|cancel-all|close|close-all> [args]" >&2
        exit 1
        ;;
esac

echo
