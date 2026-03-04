#!/usr/bin/env python3
"""
YouTube Analytics API — OAuth setup + data fetcher.
No pip install needed. Uses only Python standard library.

Usage:
  python3 youtube-analytics.py setup              # One-time OAuth setup (opens browser)
  python3 youtube-analytics.py fetch [days]        # Fetch analytics data (default: 30 days)
  python3 youtube-analytics.py fetch_channel [days] # Fetch channel-level analytics

Config: reads/writes ../config/config.json (relative to this script)
"""

import http.server
import json
import os
import sys
import threading
import time
import urllib.parse
import urllib.request
import webbrowser
from datetime import datetime, timedelta

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(SCRIPT_DIR, "..", "config", "config.json")

SCOPES = "https://www.googleapis.com/auth/yt-analytics.readonly"
TOKEN_URL = "https://oauth2.googleapis.com/token"
AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
ANALYTICS_URL = "https://youtubeanalytics.googleapis.com/v2/reports"


def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)


def save_config(config):
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
        f.write("\n")


def http_post(url, data):
    """POST request using urllib (no pip install needed)."""
    encoded = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(url, data=encoded)
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"Error: HTTP {e.code}", file=sys.stderr)
        print(f"Detail: {error_body}", file=sys.stderr)
        sys.exit(1)


def http_get(url, access_token):
    """GET request with Bearer token."""
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"Bearer {access_token}")
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"Error: HTTP {e.code}", file=sys.stderr)
        print(f"Detail: {error_body}", file=sys.stderr)
        sys.exit(1)


def refresh_access_token(config):
    """Use stored refresh_token to get a new access_token."""
    oauth = config.get("youtube_oauth", {})
    if not oauth.get("refresh_token"):
        print("Error: No refresh token found. Run 'setup' first.", file=sys.stderr)
        sys.exit(1)

    result = http_post(TOKEN_URL, {
        "client_id": oauth["client_id"],
        "client_secret": oauth["client_secret"],
        "refresh_token": oauth["refresh_token"],
        "grant_type": "refresh_token",
    })

    return result["access_token"]


# ── Setup: OAuth flow ───────────────────────────

class OAuthCallbackHandler(http.server.BaseHTTPRequestHandler):
    """Handles the OAuth redirect callback."""
    auth_code = None

    def do_GET(self):
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)

        if "code" in params:
            OAuthCallbackHandler.auth_code = params["code"][0]
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(
                b"<html><body style='font-family:system-ui;text-align:center;padding:60px'>"
                b"<h1>Authorization successful!</h1>"
                b"<p>You can close this tab and go back to the terminal.</p>"
                b"<p style='color:green;font-size:48px'>&#10003;</p>"
                b"</body></html>"
            )
        elif "error" in params:
            error = params.get("error", ["unknown"])[0]
            self.send_response(400)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(
                f"<html><body><h1>Error: {error}</h1></body></html>".encode()
            )
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass  # Suppress server logs


def cmd_setup():
    """Interactive OAuth setup flow."""
    config = load_config()

    print("=" * 50)
    print(" YouTube Analytics API — OAuth Setup")
    print("=" * 50)
    print()

    # Check if already set up
    if config.get("youtube_oauth", {}).get("refresh_token"):
        print("OAuth is already configured.")
        answer = input("Re-authorize? (y/N): ").strip().lower()
        if answer != "y":
            print("Setup cancelled.")
            return

    print("Before starting, make sure you have:")
    print("  1. YouTube Analytics API enabled in Google Cloud Console")
    print("  2. OAuth 2.0 Client ID created (type: Desktop app)")
    print()
    print("If not, follow these steps:")
    print("  1. Go to https://console.cloud.google.com/apis/library")
    print("  2. Search 'YouTube Analytics API' → Enable")
    print("  3. Go to Credentials → Create Credentials → OAuth client ID")
    print("  4. Application type: Desktop app")
    print("  5. Copy the Client ID and Client Secret")
    print()

    # Get client credentials
    existing_id = config.get("youtube_oauth", {}).get("client_id", "")
    if existing_id:
        print(f"Current Client ID: {existing_id[:20]}...")
        use_existing = input("Use existing credentials? (Y/n): ").strip().lower()
        if use_existing != "n":
            client_id = config["youtube_oauth"]["client_id"]
            client_secret = config["youtube_oauth"]["client_secret"]
        else:
            client_id = input("Client ID: ").strip()
            client_secret = input("Client Secret: ").strip()
    else:
        client_id = input("Client ID: ").strip()
        client_secret = input("Client Secret: ").strip()

    if not client_id or not client_secret:
        print("Error: Client ID and Secret are required.", file=sys.stderr)
        sys.exit(1)

    # Start local server for OAuth callback
    server = http.server.HTTPServer(("localhost", 0), OAuthCallbackHandler)
    port = server.server_address[1]
    redirect_uri = f"http://localhost:{port}"

    # Build authorization URL
    auth_params = urllib.parse.urlencode({
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "scope": SCOPES,
        "access_type": "offline",
        "prompt": "consent",
    })
    auth_url = f"{AUTH_URL}?{auth_params}"

    print()
    print("Opening browser for authorization...")
    print(f"(If browser doesn't open, visit this URL manually:)")
    print(f"  {auth_url}")
    print()
    print("Waiting for authorization...")

    webbrowser.open(auth_url)

    # Wait for callback (timeout 120 seconds)
    server.timeout = 120
    while OAuthCallbackHandler.auth_code is None:
        server.handle_request()
        if OAuthCallbackHandler.auth_code is None:
            print("Timeout: No authorization received.", file=sys.stderr)
            sys.exit(1)

    server.server_close()
    auth_code = OAuthCallbackHandler.auth_code

    print("Authorization code received. Exchanging for tokens...")

    # Exchange auth code for tokens
    token_data = http_post(TOKEN_URL, {
        "code": auth_code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code",
    })

    refresh_token = token_data.get("refresh_token")
    if not refresh_token:
        print("Error: No refresh token received. Try again with prompt=consent.", file=sys.stderr)
        sys.exit(1)

    # Save to config
    config["youtube_oauth"] = {
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
        "setup_date": datetime.now().strftime("%Y-%m-%d"),
    }
    save_config(config)

    print()
    print("Setup complete! OAuth credentials saved to config.json")
    print("You can now use 'fetch' to get analytics data.")


# ── Fetch: Analytics data ───────────────────────

def cmd_fetch(days=30):
    """Fetch per-video analytics data."""
    config = load_config()
    access_token = refresh_access_token(config)

    end_date = datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")

    params = urllib.parse.urlencode({
        "ids": "channel==MINE",
        "startDate": start_date,
        "endDate": end_date,
        "metrics": "views,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,likes,comments,subscribersGained",
        "dimensions": "video",
        "sort": "-views",
        "maxResults": 50,
    })

    url = f"{ANALYTICS_URL}?{params}"
    data = http_get(url, access_token)

    # Parse the response into a cleaner format
    columns = [col["name"] for col in data.get("columnHeaders", [])]
    rows = data.get("rows", [])

    videos = []
    for row in rows:
        video = dict(zip(columns, row))
        videos.append({
            "video_id": video.get("video", ""),
            "views": video.get("views", 0),
            "watch_time_minutes": round(video.get("estimatedMinutesWatched", 0), 1),
            "avg_view_duration_seconds": round(video.get("averageViewDuration", 0), 1),
            "avg_view_percentage": round(video.get("averageViewPercentage", 0), 1),
            "likes": video.get("likes", 0),
            "comments": video.get("comments", 0),
            "subscribers_gained": video.get("subscribersGained", 0),
        })

    result = {
        "period": f"{start_date} to {end_date}",
        "days": days,
        "video_count": len(videos),
        "videos": videos,
    }

    print(json.dumps(result, indent=2, ensure_ascii=False))


def cmd_fetch_channel(days=30):
    """Fetch channel-level daily analytics."""
    config = load_config()
    access_token = refresh_access_token(config)

    end_date = datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")

    params = urllib.parse.urlencode({
        "ids": "channel==MINE",
        "startDate": start_date,
        "endDate": end_date,
        "metrics": "views,estimatedMinutesWatched,subscribersGained,subscribersLost",
        "dimensions": "day",
        "sort": "day",
    })

    url = f"{ANALYTICS_URL}?{params}"
    data = http_get(url, access_token)

    columns = [col["name"] for col in data.get("columnHeaders", [])]
    rows = data.get("rows", [])

    days_data = []
    total_views = 0
    total_impressions = 0
    total_watch_minutes = 0

    for row in rows:
        day = dict(zip(columns, row))
        views = day.get("views", 0)
        total_views += views
        total_watch_minutes += day.get("estimatedMinutesWatched", 0)
        days_data.append({
            "date": day.get("day", ""),
            "views": views,
            "watch_time_minutes": round(day.get("estimatedMinutesWatched", 0), 1),
            "subscribers_gained": day.get("subscribersGained", 0),
            "subscribers_lost": day.get("subscribersLost", 0),
        })

    result = {
        "period": f"{start_date} to {end_date}",
        "summary": {
            "total_views": total_views,
            "total_watch_time_hours": round(total_watch_minutes / 60, 1),
        },
        "daily": days_data,
    }

    print(json.dumps(result, indent=2, ensure_ascii=False))


# ── Main ────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 youtube-analytics.py <command> [args]")
        print("Commands: setup, fetch [days], fetch_channel [days]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "setup":
        cmd_setup()
    elif command == "fetch":
        days = int(sys.argv[2]) if len(sys.argv) > 2 else 30
        cmd_fetch(days)
    elif command == "fetch_channel":
        days = int(sys.argv[2]) if len(sys.argv) > 2 else 30
        cmd_fetch_channel(days)
    else:
        print(f"Unknown command: {command}", file=sys.stderr)
        sys.exit(1)
