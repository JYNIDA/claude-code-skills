#!/usr/bin/env bash
# check-auth.sh — Test if YouTube Studio browse session is authenticated.
# Exit 0 = logged in. Exit 1 = login required.
# Fast (~2s). Use before any Studio scraping attempt.

set -euo pipefail
BROWSE="${BROWSE:-$HOME/.claude/skills/gstack/browse/dist/browse}"

if [ ! -x "$BROWSE" ]; then
  echo "ERROR: browse not found at $BROWSE" >&2
  exit 2
fi

# Navigate to Studio home. If authed, URL stays on studio.youtube.com.
# If not, redirects to accounts.google.com.
"$BROWSE" goto "https://studio.youtube.com" >/dev/null 2>&1 || true
sleep 2
url=$("$BROWSE" url 2>/dev/null || echo "")

if echo "$url" | grep -q "accounts.google.com"; then
  echo "AUTH_REQUIRED"
  exit 1
fi

if echo "$url" | grep -q "studio.youtube.com"; then
  echo "AUTHENTICATED"
  exit 0
fi

echo "UNKNOWN_STATE: $url"
exit 1
