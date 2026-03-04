#!/bin/bash
# fetch-youtube-data.sh — YouTube Data API v3 호출 스크립트
# Usage:
#   bash fetch-youtube-data.sh <command> <api_key> <param1> [param2]
#
# Commands:
#   channel_id    <api_key> <handle>        → 채널 핸들(@name)로 채널 ID 조회
#   channel_stats <api_key> <channel_id>    → 채널 통계 (구독자, 총 조회수)
#   recent_videos <api_key> <channel_id> [days]  → 최근 N일 영상 목록 (기본: 30일)
#   video_details <api_key> <video_ids>     → 영상별 상세 통계 (콤마로 구분된 ID)
#
# Output: JSON (YouTube API 원본 응답)
# Error: stderr로 에러 메시지 출력, exit code 1

set -euo pipefail

BASE_URL="https://www.googleapis.com/youtube/v3"

command="${1:-}"
api_key="${2:-}"
param1="${3:-}"
param2="${4:-}"

# ── Validation ──────────────────────────────────

if [[ -z "$command" ]]; then
  echo "Error: No command specified" >&2
  echo "Usage: bash fetch-youtube-data.sh <command> <api_key> <param>" >&2
  exit 1
fi

if [[ -z "$api_key" ]]; then
  echo "Error: API key is required" >&2
  exit 1
fi

# ── Helper: curl with error handling ────────────

api_call() {
  local url="$1"
  local response
  local http_code

  # Use temp file to capture both body and http code
  local tmpfile
  tmpfile=$(mktemp)

  http_code=$(curl -s -w "%{http_code}" -o "$tmpfile" "$url" 2>/dev/null) || {
    rm -f "$tmpfile"
    echo "Error: Network request failed" >&2
    exit 1
  }

  response=$(cat "$tmpfile")
  rm -f "$tmpfile"

  if [[ "$http_code" -ne 200 ]]; then
    echo "Error: API returned HTTP $http_code" >&2
    # Try to extract error message from response
    local error_msg
    error_msg=$(echo "$response" | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    print(data.get('error', {}).get('message', 'Unknown error'))
except:
    print('Unknown error')
" 2>/dev/null || echo "Unknown error")
    echo "Detail: $error_msg" >&2
    exit 1
  fi

  echo "$response"
}

# ── Commands ────────────────────────────────────

case "$command" in

  channel_id)
    # 채널 핸들(@name)로 채널 ID 조회
    handle="${param1}"
    if [[ -z "$handle" ]]; then
      echo "Error: Channel handle is required (e.g., @eoglobal)" >&2
      exit 1
    fi

    # Remove @ prefix if present for the forHandle parameter
    handle_clean="${handle#@}"

    url="${BASE_URL}/channels?part=id,snippet&forHandle=${handle_clean}&key=${api_key}"
    response=$(api_call "$url")

    # Extract channel ID
    echo "$response" | python3 -c "
import sys, json
data = json.load(sys.stdin)
items = data.get('items', [])
if items:
    ch = items[0]
    result = {
        'channel_id': ch['id'],
        'title': ch['snippet']['title']
    }
    print(json.dumps(result, indent=2))
else:
    print(json.dumps({'error': 'Channel not found'}))
    sys.exit(1)
"
    ;;

  channel_stats)
    # 채널 통계 (구독자, 총 조회수, 영상 수)
    channel_id="${param1}"
    if [[ -z "$channel_id" ]]; then
      echo "Error: Channel ID is required" >&2
      exit 1
    fi

    url="${BASE_URL}/channels?part=statistics,snippet&id=${channel_id}&key=${api_key}"
    response=$(api_call "$url")

    echo "$response" | python3 -c "
import sys, json
data = json.load(sys.stdin)
items = data.get('items', [])
if items:
    stats = items[0]['statistics']
    snippet = items[0]['snippet']
    result = {
        'title': snippet['title'],
        'subscribers': int(stats.get('subscriberCount', 0)),
        'total_views': int(stats.get('viewCount', 0)),
        'video_count': int(stats.get('videoCount', 0))
    }
    print(json.dumps(result, indent=2))
else:
    print(json.dumps({'error': 'Channel not found'}))
    sys.exit(1)
"
    ;;

  recent_videos)
    # 최근 N일 영상 목록
    channel_id="${param1}"
    days="${param2:-30}"

    if [[ -z "$channel_id" ]]; then
      echo "Error: Channel ID is required" >&2
      exit 1
    fi

    # Calculate date N days ago in RFC 3339 format
    if [[ "$(uname)" == "Darwin" ]]; then
      after_date=$(date -v-"${days}"d -u +"%Y-%m-%dT%H:%M:%SZ")
    else
      after_date=$(date -u -d "${days} days ago" +"%Y-%m-%dT%H:%M:%SZ")
    fi

    url="${BASE_URL}/search?part=id,snippet&channelId=${channel_id}&type=video&order=date&publishedAfter=${after_date}&maxResults=50&key=${api_key}"
    response=$(api_call "$url")

    echo "$response" | python3 -c "
import sys, json
data = json.load(sys.stdin)
items = data.get('items', [])
videos = []
for item in items:
    videos.append({
        'video_id': item['id'].get('videoId', ''),
        'title': item['snippet']['title'],
        'published_at': item['snippet']['publishedAt']
    })
result = {
    'total_results': data.get('pageInfo', {}).get('totalResults', 0),
    'returned': len(videos),
    'videos': videos,
    'video_ids': ','.join(v['video_id'] for v in videos if v['video_id'])
}
print(json.dumps(result, indent=2, ensure_ascii=False))
"
    ;;

  video_details)
    # 영상별 상세 통계 (콤마로 구분된 ID, 최대 50개)
    video_ids="${param1}"
    if [[ -z "$video_ids" ]]; then
      echo "Error: Video IDs are required (comma-separated)" >&2
      exit 1
    fi

    url="${BASE_URL}/videos?part=statistics,snippet,contentDetails&id=${video_ids}&key=${api_key}"
    response=$(api_call "$url")

    echo "$response" | python3 -c "
import sys, json
data = json.load(sys.stdin)
items = data.get('items', [])
videos = []
for item in items:
    stats = item.get('statistics', {})
    snippet = item.get('snippet', {})
    content = item.get('contentDetails', {})
    videos.append({
        'video_id': item['id'],
        'title': snippet.get('title', ''),
        'published_at': snippet.get('publishedAt', ''),
        'duration': content.get('duration', ''),
        'views': int(stats.get('viewCount', 0)),
        'likes': int(stats.get('likeCount', 0)),
        'comments': int(stats.get('commentCount', 0))
    })
# Sort by views descending
videos.sort(key=lambda v: v['views'], reverse=True)
result = {
    'count': len(videos),
    'videos': videos
}
print(json.dumps(result, indent=2, ensure_ascii=False))
"
    ;;

  *)
    echo "Error: Unknown command '$command'" >&2
    echo "Available commands: channel_id, channel_stats, recent_videos, video_details" >&2
    exit 1
    ;;
esac
