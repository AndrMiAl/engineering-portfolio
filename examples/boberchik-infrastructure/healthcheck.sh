#!/usr/bin/env bash
set -euo pipefail

URL="${HEALTH_URL:-http://127.0.0.1:8080/health}"

status="$(curl --silent --show-error --output /dev/null --write-out '%{http_code}' "$URL")"

if [[ "$status" != "200" ]]; then
  echo "healthcheck failed: HTTP $status" >&2
  exit 1
fi

echo "healthcheck passed"
