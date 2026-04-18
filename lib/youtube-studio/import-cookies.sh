#!/usr/bin/env bash
# import-cookies.sh — Launch cookie picker to import Google/YouTube cookies.
# Opens browser UI at 127.0.0.1. User selects domains + imports. Returns when done.

set -euo pipefail
BROWSE="${BROWSE:-$HOME/.claude/skills/gstack/browse/dist/browse}"

echo "Opening cookie picker..."
echo "Required domains: google.com, youtube.com, studio.youtube.com"
echo ""
echo "Steps:"
echo "  1. Select your logged-in browser (Chrome/Comet)"
echo "  2. Check: google.com + youtube.com"
echo "  3. Click Import, close the picker"
echo ""

# Launch picker — blocks until user closes picker window
"$BROWSE" cookie-import-browser 2>&1

# Verify after import
echo ""
echo "Verifying auth..."
if "$(dirname "$0")/check-auth.sh" >/dev/null 2>&1; then
  echo "✓ Studio auth confirmed"
  exit 0
else
  echo "✗ Auth still failing — make sure you're logged into YouTube Studio in the source browser"
  exit 1
fi
