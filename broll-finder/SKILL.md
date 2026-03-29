---
name: broll-finder
description: 스크립트를 붙여넣으면 B-roll 영상/기사/사진 소스를 찾아주고, 선택한 영상을 로컬에 다운로드하고, 출처 문서를 Notion 또는 텍스트 파일로 생성. "b-roll 찾아줘", "영상 소스", "broll", "footage 찾아줘" 요청에 사용.
---

# B-Roll Finder

스크립트를 분석해 필요한 B-roll 소스를 찾고, 다운로드하고, 출처 문서를 만든다.

---

## 입력

사용자가 스크립트(또는 에피소드 개요)를 붙여넣는다. 형태는 자유롭다:
- 전체 스크립트 텍스트
- 장면 목록
- "Dan Wang 에피소드, 베이징/상하이/소수민족" 같은 키워드 요약

추가로 확인할 것:
- 에피소드 제목/게스트 (있으면): 파일명에 사용
- 저장 위치: 기본값 `~/Desktop/Cowork/B-Roll/[에피소드명]/`
- 출처 문서 형식: Notion (기본) 또는 텍스트 파일

---

## Phase 1: 스크립트 분석 → 장면/키워드 추출

스크립트를 읽고 다음을 추출한다:

1. **장면 목록**: 영상이 필요한 구체적 장면 (예: "베이징 스모그", "천안문 광장", "묘족 축제")
2. **검색 키워드**: 각 장면별 YouTube/웹 검색에 쓸 영어 키워드 (3-5개)
3. **소스 타입 분류**: 각 장면이 어떤 소스가 필요한지
   - `youtube`: B-roll 영상 (다운로드 가능)
   - `news`: 뉴스 기사/영상 (Reuters, AP, BBC 등)
   - `stock`: 스톡 이미지/영상 (Getty, Shutterstock)
   - `social`: SNS 영상 (Instagram Reel 등)

추출 결과를 다음 형식으로 사용자에게 보여준다:

```
📋 장면 분석 결과
━━━━━━━━━━━━━━━━━━━━━━━━━
[장면 번호] 장면 설명
→ 검색 키워드: "키워드1", "키워드2", "키워드3"
→ 소스 타입: youtube / news / stock
━━━━━━━━━━━━━━━━━━━━━━━━━
총 N개 장면 | 검색 시작할까요? (또는 추가/수정사항 있으면 말씀해주세요)
```

사용자 확인 후 Phase 2로 진행.

---

## Phase 2: 소스 검색

각 장면의 검색 키워드로 소스를 찾는다. **병렬로 실행**한다.

### 2-A. YouTube 검색 (yt-dlp)

소스 타입이 `youtube`인 장면마다:

```bash
yt-dlp "ytsearch5:[검색 키워드]" \
  --print "%(title)s | %(webpage_url)s | %(duration_string)s | %(uploader)s" \
  --no-playlist 2>/dev/null
```

장면당 최대 5개 후보를 수집한다.

### 2-B. 뉴스/이미지 검색 (WebSearch)

소스 타입이 `news` 또는 `stock`인 장면마다 WebSearch를 실행한다:
- 검색어: `[키워드] site:reuters.com OR site:apnews.com OR site:bbc.com video footage`
- 결과에서 직접 URL이 있는 것만 추출

### 2-C. 결과 정리 및 제시

장면별로 검색 결과를 정리해 보여준다:

```
🔍 검색 결과
━━━━━━━━━━━━━━━━━━━━━━━━━

[장면 1] 베이징 스모그
  ① Beijing Smog in 4K - 24h Time Lapse | 0:37 | tvdillen
     https://youtube.com/watch?v=rWOn7op0dew
  ② Time-Lapse Video Shows Smog Enveloping Beijing | 1:26 | TIME
     https://youtube.com/watch?v=BPzzlBVtXH0
  ...

[장면 2] 천안문 광장
  ① 4K | Tiananmen Square in Beijing | 1:04 | Soltau Cruiser
     https://youtube.com/watch?v=IIwbf9LU3Nw
  ...

━━━━━━━━━━━━━━━━━━━━━━━━━
다운로드할 영상 번호를 알려주세요. (예: 1-①, 2-①, 3-②)
추가 검색이 필요하면 요청해주세요.
```

---

## Phase 3: 추가 요청 루프 (인터랙티브)

사용자가 다운로드할 영상을 선택하기 전, 또는 선택 후에도 추가 요청을 받는다.

### 3-A. 키워드 입력 → 소스 타입 선택

사용자가 키워드를 직접 입력하면 먼저 어떤 타입의 소스가 필요한지 물어본다:

```
"[키워드]"로 어떤 소스를 찾을까요?
  1. 🎬 YouTube 영상 (다운로드 가능)
  2. 📰 뉴스 기사/영상 (Reuters, AP, BBC 등)
  3. 🖼️ 사진/이미지 (Getty, AP Photo)
  4. 전체 다 찾아줘
```

선택에 따라:
- YouTube → yt-dlp `ytsearch5:` 실행
- 뉴스 → WebSearch `site:reuters.com OR site:apnews.com OR site:bbc.com`
- 사진 → WebSearch `site:gettyimages.com OR site:apimages.com`
- 전체 → 세 가지 병렬 실행

### 3-B. 직접 URL 제공

사용자가 URL을 직접 주면 소스 타입을 자동 판별하고:
- YouTube URL → yt-dlp로 메타데이터 추출 후 다운로드 목록에 추가
- Reuters/AP/기타 뉴스 URL → yt-dlp 다운로드 시도. 실패 시 링크만 출처 목록에 기록
- Instagram URL → yt-dlp 시도 (로그인 필요할 수 있음, 실패 시 알림)

```bash
# 다운로드 가능 여부 먼저 확인
yt-dlp --simulate "[URL]" 2>&1 | head -5
```

### 3-C. 루프 종료 조건

사용자가 "다운로드 시작", "이걸로 할게", "완료" 등을 말하면 Phase 4로 진행.

추가 요청이 없으면 Phase 4로 진행.

---

## Phase 4: 다운로드

사용자가 선택한 영상을 다운로드한다.

### 저장 위치 확인

```
저장 위치: ~/Desktop/Cowork/B-Roll/[에피소드명]/
```

디렉토리가 없으면 자동 생성:

```bash
mkdir -p "~/Desktop/Cowork/B-Roll/[에피소드명]"
```

### YouTube 영상 다운로드

선택된 YouTube URL들을 yt-dlp로 일괄 다운로드:

```bash
cd "~/Desktop/Cowork/B-Roll/[에피소드명]" && yt-dlp \
  [URL1] [URL2] [URL3] ... \
  -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" \
  --merge-output-format mp4 \
  --output "%(uploader)s — %(title)s.%(ext)s" \
  --write-info-json
```

### 다운로드 후 메타데이터 추출

`*.info.json` 파일에서 채널명, URL, 업로드일을 추출하고 JSON 파일은 삭제:

```bash
python3 -c "
import json, glob, os
files = glob.glob('*.info.json')
results = []
for f in sorted(files):
    with open(f) as fp:
        d = json.load(fp)
    results.append({
        'title': d.get('title'),
        'url': d.get('webpage_url'),
        'channel': d.get('uploader'),
        'channel_url': d.get('channel_url') or d.get('uploader_url'),
        'duration': d.get('duration_string'),
        'upload_date': d.get('upload_date'),
    })
    os.remove(f)
print(results)
"
```

### 뉴스/기타 소스

YouTube가 아닌 소스(Reuters, AP 등)는 다운로드 대신 링크만 출처 문서에 기록한다.

---

## Phase 5: 출처 문서 생성

### Notion 업로드 (기본)

`mcp__notion__notion-create-pages`로 Notion 페이지 생성 (parent 없이 workspace-level):

페이지 제목: `[에피소드명] B-Roll 출처 목록`
아이콘: 🎬

콘텐츠 구조:
- 총 N개 영상 / 총 용량 / 저장 위치
- 각 영상별 섹션 (표 대신 섹션 형식 사용 — `|` 문자가 표를 깨뜨림):
  ```
  ## 🏙️ [카테고리명]
  **제목**: ...
  **길이**: ...
  **채널**: ...
  **YouTube**: [URL]
  **채널 링크**: [채널 URL]
  **업로드**: YYYY-MM-DD
  **출처 표기**: `[영상 제목] — YouTube @[채널명]`
  ```
- 편집 시 출처 표기 방법 섹션
- 편집 흐름 메모 (있으면)

### 텍스트 파일 (조건부 필수)

다운로드 또는 링크 수집이 1개 이상인 경우 `~/Desktop/Cowork/B-Roll/[에피소드명]/sources.md`에 저장한다.

**수집된 소스가 0개이면 파일을 생성하지 않는다.**

Notion 업로드는 선택이지만, sources.md는 소스가 있으면 항상 생성한다.

---

## 완료 보고

```
✅ B-Roll 수집 완료
━━━━━━━━━━━━━━━━━━━━━━━━━
📁 저장 위치: ~/Desktop/Cowork/B-Roll/[에피소드명]/
🎬 영상 N개 다운로드 완료 (총 XGB)
📋 출처 문서: [Notion URL]
━━━━━━━━━━━━━━━━━━━━━━━━━
추가 영상이 필요하면 언제든 요청해주세요.
```

---

## 주의사항

- **표(table) 사용 금지**: Notion에서 `|` 문자가 표 셀을 깨뜨림. 항상 섹션 형식 사용.
- **yt-dlp 검색 키워드**: 반드시 영어로. 한국어 키워드는 검색 품질이 낮음.
- **Reuters/AP**: 직접 URL이 없으면 다운로드 불가. 링크만 문서에 기록.
- **저작권**: 다운로드 영상은 편집 레퍼런스/B-roll 용도로만 사용. 실제 방송 사용 시 라이선스 확인 필요.
- **파일명**: `%(uploader)s — %(title)s.%(ext)s` 형식으로 저장해 출처가 파일명에 포함되도록.
