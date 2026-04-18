#!/usr/bin/env python3
"""Re-authorize a single YouTube channel and update only that channel's refresh_token.

Preserves multi-channel structure in config.json.

Usage:
    python3 reauth-channel.py eo_global
    python3 reauth-channel.py eo_korea
"""

import http.server
import json
import sys
import urllib.parse
import urllib.request
import webbrowser
from datetime import datetime
from pathlib import Path

CONFIG_PATH = Path.home() / ".claude/skills/weekly-meeting/config/config.json"
AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"
SCOPES = " ".join([
    "https://www.googleapis.com/auth/yt-analytics.readonly",
    "https://www.googleapis.com/auth/yt-analytics-monetary.readonly",
    "https://www.googleapis.com/auth/youtube.readonly",
])


class Callback(http.server.BaseHTTPRequestHandler):
    code = None

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        if "code" in params:
            Callback.code = params["code"][0]
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"<h2>Authorized. Return to your terminal.</h2>")
        else:
            self.send_response(400)
            self.end_headers()

    def log_message(self, *a, **kw):
        pass


def post(url, data):
    req = urllib.request.Request(url, data=urllib.parse.urlencode(data).encode())
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 reauth-channel.py <channel_key>", file=sys.stderr)
        print("  channel_key: one of the keys under youtube_oauth.channels", file=sys.stderr)
        sys.exit(1)

    channel_key = sys.argv[1]
    cfg = json.loads(CONFIG_PATH.read_text())
    yo = cfg.get("youtube_oauth", {})
    channels = yo.get("channels", {})
    if channel_key not in channels:
        print(f"Unknown channel '{channel_key}'. Available: {list(channels.keys())}", file=sys.stderr)
        sys.exit(1)

    client_id = yo["client_id"]
    client_secret = yo["client_secret"]
    channel_name = channels[channel_key].get("name", channel_key)

    print(f"Re-authorizing channel: {channel_name} ({channel_key})")
    print(f"Make sure to sign in with the Google account that owns/manages this channel.")
    print()

    server = http.server.HTTPServer(("localhost", 0), Callback)
    port = server.server_address[1]
    redirect = f"http://localhost:{port}"

    auth_url = f"{AUTH_URL}?" + urllib.parse.urlencode({
        "client_id": client_id,
        "redirect_uri": redirect,
        "response_type": "code",
        "scope": SCOPES,
        "access_type": "offline",
        "prompt": "consent",
    })

    print("Opening browser. If it doesn't open, visit:")
    print(f"  {auth_url}")
    print()
    webbrowser.open(auth_url)

    server.timeout = 180
    while Callback.code is None:
        server.handle_request()
        if Callback.code is None:
            print("Timeout. Try again.", file=sys.stderr)
            sys.exit(1)

    server.server_close()

    tokens = post(TOKEN_URL, {
        "code": Callback.code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect,
        "grant_type": "authorization_code",
    })

    refresh_token = tokens.get("refresh_token")
    if not refresh_token:
        print(f"No refresh_token returned. Response: {tokens}", file=sys.stderr)
        sys.exit(1)

    channels[channel_key]["refresh_token"] = refresh_token
    yo["channels"] = channels
    yo["setup_date"] = datetime.now().strftime("%Y-%m-%d")
    cfg["youtube_oauth"] = yo
    CONFIG_PATH.write_text(json.dumps(cfg, indent=2, ensure_ascii=False))

    print()
    print(f"Refresh token saved for channel '{channel_key}'.")
    print("Verifying with a quick Analytics API call...")

    access = post(TOKEN_URL, {
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token",
    })["access_token"]

    cid = channels[channel_key]["channel_id"]
    url = "https://youtubeanalytics.googleapis.com/v2/reports?" + urllib.parse.urlencode({
        "ids": f"channel=={cid}",
        "startDate": "2026-04-01",
        "endDate": "2026-04-16",
        "metrics": "views",
    })
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {access}"})
    try:
        resp = json.load(urllib.request.urlopen(req))
        print(f"Analytics API OK. Views Apr 1-16: {resp.get('rows', [[0]])[0][0]}")
    except Exception as e:
        print(f"Verification call failed: {e}")


if __name__ == "__main__":
    main()
