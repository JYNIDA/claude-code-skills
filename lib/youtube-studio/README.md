# lib/youtube-studio

Shared YouTube Studio scraper used by `weekly-meeting`, `media-impact-lab`, `media-weekly`.

Scrapes Impressions / CTR / traffic sources / retention that the YouTube Data API can't provide — via gstack browse with imported Google cookies.

## Scripts

| Script | Purpose | Input | Output |
|--------|---------|-------|--------|
| `check-auth.sh` | Test if Studio session is authenticated | — | exit 0 (authed) / exit 1 (need login) |
| `import-cookies.sh` | Launch cookie picker to import Google cookies | — | verifies auth on exit |
| `fetch-reach.sh` | Scrape Reach tab (Impressions, CTR, traffic) | `VIDEO_ID [OUTDIR]` | `{VIDEO_ID}_reach.png` + `{VIDEO_ID}_reach.json` |

## How calling skills should integrate

```bash
LIB=~/.claude/skills/lib/youtube-studio

# 1. Auth gate — always check first (fast, ~2s)
if ! "$LIB/check-auth.sh" >/dev/null 2>&1; then
  echo "Studio session expired — run: $LIB/import-cookies.sh"
  # Graceful degradation: continue without Studio data, flag in report
  STUDIO_AVAILABLE=false
else
  STUDIO_AVAILABLE=true
fi

# 2. Fetch per video
if [ "$STUDIO_AVAILABLE" = true ]; then
  "$LIB/fetch-reach.sh" "yPux3-jDW9g" /tmp/studio
  # Returns JSON + PNG. Parse JSON with jq.
fi
```

## Cookie lifecycle

- Cookies persist in gstack browse session (`~/.gstack/...`)
- Long-term Google cookies (`__Secure-3PSID`) last 6–12 months if "stay signed in" is enabled
- Re-import needed when: Google forces logout, password change, gstack browser profile reset
- Calling skills should call `check-auth.sh` first, never blindly assume auth

## DOM selector fragility

Studio's DOM changes periodically. `fetch-reach.sh` uses two extraction strategies:
1. **Primary** — JS query on `ytcp-metric-card` / class substring matches
2. **Fallback** — regex over page innerText for labeled values
3. **Always saves a screenshot** as the reliable capture

If both extractions return empty, the screenshot is still actionable. Update selectors by inspecting the Reach tab in devtools and patching the JS block in `fetch-reach.sh`.

## Multi-channel (EO Global + EO Korea)

Studio scopes by logged-in channel. The cookie picker captures whichever channel was active in the source browser. To switch channels:
1. In the source browser, use the Studio channel switcher (top-right)
2. Re-run `import-cookies.sh`

For scripted channel-switching inside a single session (EO Global + EO Korea in one run), we'd need to programmatically click the channel switcher — not implemented yet. Current workflow: run twice, once per channel.

---

## Known issues (as of 2026-04-13 first-run attempt)

1. **User-Agent must be set to modern Chrome** before navigation. `fetch-reach.sh` should call `browse useragent "..."` first. Default gstack UA gets flagged as "unsupported browser" by Studio.

2. **Channel context not handled**. Cookie import captures whichever channel was active in the source browser. Accessing a video that belongs to a different channel returns "Oops, something went wrong" error page. Need to either:
   - Programmatically click the channel switcher UI (top-right avatar)
   - Or use URL param `?c=<channelId>` if Studio supports it
   - Or split into two separate `fetch-reach-gl.sh` / `fetch-reach-kr.sh` with pre-navigation channel switch

3. **Screenshot path restricted to `/tmp` and skill dirs**. gstack browse sandboxes `screenshot <path>` — can't save to `~/Desktop/...`. Update callers to use `/tmp/youtube-studio/` and copy results to final location separately.

4. **DOM selectors need real-world tuning**. Current `ytcp-metric-card` + class-substring fallback returns empty. Must manually inspect a successful Reach tab render and capture actual selectors (likely involves shadow DOM piercing on `ytcp-*` custom elements).

Next debug session:
- Start from a known-good video ID on the default-logged-in channel
- Use `browse html` + `browse js "document.querySelectorAll('*[class*=metric]').length"` to explore live DOM
- Consider switching to Analytics API v2 (`yt-analytics.readonly` OAuth scope) for Impressions/CTR instead of scraping — might be possible now even though YouTube historically blocked it
