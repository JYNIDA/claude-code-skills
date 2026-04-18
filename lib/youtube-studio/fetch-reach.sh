#!/usr/bin/env bash
# fetch-reach.sh <VIDEO_ID> [OUTPUT_DIR]
# Scrape YouTube Studio Reach tab for a video.
# Captures: Impressions, CTR, Views, Unique viewers, Traffic sources.
#
# Always saves a screenshot (reliable).
# Attempts JSON metric extraction via JS (best-effort — DOM selectors may drift).
# Exit 0 on success. Exit 1 on auth failure. Exit 2 on other errors.

set -euo pipefail
BROWSE="${BROWSE:-$HOME/.claude/skills/gstack/browse/dist/browse}"

VIDEO_ID="${1:-}"
OUTDIR="${2:-/tmp/youtube-studio}"

if [ -z "$VIDEO_ID" ]; then
  echo "Usage: $0 <VIDEO_ID> [OUTPUT_DIR]" >&2
  exit 2
fi

mkdir -p "$OUTDIR"
URL="https://studio.youtube.com/video/${VIDEO_ID}/analytics/tab-reach_viewers/period-default"

# Auth gate
if ! "$(dirname "$0")/check-auth.sh" >/dev/null 2>&1; then
  echo "AUTH_REQUIRED" >&2
  exit 1
fi

# Navigate + wait for metrics to render
"$BROWSE" goto "$URL" >/dev/null 2>&1
sleep 4
"$BROWSE" wait --networkidle >/dev/null 2>&1 || true
sleep 2

# Screenshot (reliable primary capture)
SCREENSHOT="${OUTDIR}/${VIDEO_ID}_reach.png"
"$BROWSE" screenshot "$SCREENSHOT" >/dev/null 2>&1 || true

# JS-based extraction — looks for metric cards by their common Studio labels.
# These selectors are best-effort; Studio DOM changes periodically.
# If extraction fails, the screenshot is still usable.
JS_EXTRACT=$(cat <<'EOF'
(() => {
  const out = { video_id: '__VID__', url: location.href, metrics: {}, traffic: {}, error: null };
  try {
    // Metric cards — each has a label + value. Studio uses ytcp-metric-card or similar.
    const cards = document.querySelectorAll('ytcp-metric-card, [class*="metric-card"]');
    cards.forEach(c => {
      const label = (c.querySelector('[class*="label"], [class*="title"]')?.textContent || '').trim();
      const value = (c.querySelector('[class*="value"], [class*="primary"]')?.textContent || '').trim();
      if (label && value) out.metrics[label] = value;
    });
    // Fallback: scan all text nodes for "Impressions", "CTR", etc.
    const body = document.body.innerText;
    const pat = (re) => { const m = body.match(re); return m ? m[1].trim() : null; };
    out.fallback = {
      impressions: pat(/Impressions[^\n]*\n([\d,\.KM]+)/i),
      ctr:         pat(/Impressions click-through rate[^\n]*\n([\d\.]+%)/i),
      views:       pat(/Views\n([\d,\.KM]+)/i),
      unique:      pat(/Unique viewers\n([\d,\.KM]+)/i),
      avg_duration: pat(/Average view duration\n([\d:]+)/i),
    };
    // Traffic sources (best-effort)
    const trafficRows = document.querySelectorAll('[class*="traffic-source"] tr, [class*="traffic"] [class*="row"]');
    trafficRows.forEach(r => {
      const cells = r.querySelectorAll('td, [class*="cell"]');
      if (cells.length >= 2) {
        out.traffic[cells[0].textContent.trim()] = cells[1].textContent.trim();
      }
    });
  } catch (e) { out.error = String(e); }
  return JSON.stringify(out);
})()
EOF
)
JS_EXTRACT="${JS_EXTRACT//__VID__/$VIDEO_ID}"

JSON_FILE="${OUTDIR}/${VIDEO_ID}_reach.json"
"$BROWSE" js "$JS_EXTRACT" > "$JSON_FILE" 2>/dev/null || echo '{"error":"extraction_failed"}' > "$JSON_FILE"

echo "screenshot: $SCREENSHOT"
echo "json: $JSON_FILE"
cat "$JSON_FILE"
