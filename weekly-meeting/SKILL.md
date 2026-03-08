---
name: weekly-meeting
description: 위클리 회의 준비 및 회의록 정리. YouTube 지표 자동 수집 + Slack 프로덕션 현황 + 한국어 메모를 영어 회의록으로 변환. "위클리", "weekly meeting", "회의록" 요청에 사용.
---

# Weekly Meeting Prep — Automated Workflow

이 스킬이 호출되면 아래 4단계(Phase 0~4)를 순서대로 실행한다.

---

## Phase 0: First-Time Setup (최초 1회)

`config/config.json` 존재 여부를 확인한다.

### config.json이 없으면 → 셋업 위자드 실행

1. **YouTube API 키 입력**
   - AskUserQuestion으로 YouTube Data API v3 키 입력 요청
   - 키가 없으면 발급 방법 안내:
     > 1. [Google Cloud Console](https://console.cloud.google.com/) 접속
     > 2. 프로젝트 생성 → "YouTube Data API v3" 활성화
     > 3. 사용자 인증 정보 → API 키 생성
     > 4. (선택) API 키 제한: YouTube Data API v3만 허용

2. **채널 ID 자동 조회**
   - `scripts/fetch-youtube-data.sh channel_id` 호출로 `@eoglobal` 채널 ID 확인
   - 실패 시 수동 입력 안내

3. **2026 목표치 확인**
   - CLAUDE.md에서 가져온 기본값 제시 (구독자 100만)
   - AskUserQuestion으로 추가 목표치 확인:
     - Monthly Views 목표
     - Mega-hit 기준 (기본: 500K+)
     - Hit 기준 (기본: 200K-500K)

4. **Slack 채널 설정**
   - Slack MCP 연결 확인 (ToolSearch로 `slack` 도구 검색)
   - 연결되어 있으면:
     - `slack_search_channels`로 채널 목록 조회
     - 기본 모니터링 채널: `#team-gl-media`, `#gl-youtube-operation`
     - AskUserQuestion으로 추가 채널 확인
   - 연결 안 되어 있으면: Slack 섹션 스킵 설정

5. **config/config.json 저장**
   - `config/config.example.json` 구조를 기반으로 실제 값 채워서 저장

### config.json이 있으면 → Phase 1로 건너뛰기
- 설정 변경 필요 시 사용자가 명시적으로 "설정 변경" 요청

---

## Phase 1: 데이터 자동 수집 (~15초)

### 1-A. YouTube Data API v3

`scripts/fetch-youtube-data.sh` 스크립트를 사용하여 데이터를 수집한다.

**수집 항목:**

| API 호출 | Quota | 수집 데이터 |
|----------|-------|-------------|
| `channels.list` (statistics) | 1 | 구독자 수, 총 조회수 |
| `search.list` (최근 30일 영상) | 100 | 영상 ID 목록 (max 50개) |
| `videos.list` (batch, 50개 단위) | 1 | 영상별 views, likes, comments, publishedAt |
| **총 예상 quota** | **~102** | (일일 한도 10,000 중 ~1%) |

**스크립트 호출 순서:**
```bash
# 1. 채널 통계
bash scripts/fetch-youtube-data.sh channel_stats "$API_KEY" "$CHANNEL_ID"

# 2. 최근 30일 영상 목록
bash scripts/fetch-youtube-data.sh recent_videos "$API_KEY" "$CHANNEL_ID" 30

# 3. 영상별 상세 통계 (ID를 콤마로 연결)
bash scripts/fetch-youtube-data.sh video_details "$API_KEY" "$VIDEO_IDS"
```

### 1-B. 메트릭 자동 계산

수집된 데이터로 다음을 계산:

- **Monthly Views**: 최근 30일 영상 조회수 합산
- **Mega-hits**: 500K+ 조회수 영상 수 (기준은 config에서 변경 가능)
- **Hits**: 200K-500K 조회수 영상 수
- **Baseline avg**: 상위 3개 제외한 나머지 영상의 평균 조회수
- **영상별 성과 등급**:
  - `MEGA-HIT`: 500K+ views
  - `HIT`: 200K-500K views
  - `BASELINE`: baseline avg의 0.5x ~ 2x 범위
  - `UNDERPERFORMER`: baseline avg의 0.5x 미만

### 1-C. Slack 프로덕션 현황 (Slack 연결 시)

Slack MCP 도구를 사용하여 프로덕션 진행상황 수집:

1. **채널 메시지 읽기**: 설정된 각 채널에서 최근 7일 메시지 확인
   - ToolSearch로 `slack_read_channel` 로드
   - 각 모니터링 채널에서 메시지 읽기
2. **키워드 검색**: 프로덕션 관련 키워드 검색
   - ToolSearch로 `slack_search_public_and_private` 로드
   - 검색 키워드: "촬영", "편집", "업로드", "섭외", "인터뷰", "filming", "editing", "upload", "outreach"
3. **파이프라인 상태표 구성**: 메시지에서 프로젝트별 진행 단계 추출

**Slack 미연결 시**: Slack 섹션 전체 스킵, Phase 3에서 수동 입력 안내

### 1-D. 주간 비교

- `~/Desktop/Cowork/meeting-notes/` 에서 가장 최근 `weekly-*.md` 파일 찾기
- 파일이 있으면: 이전 주 지표 파싱 → 변화량(delta) 계산
- 파일이 없으면: "vs Last Week" 컬럼 = "N/A (first run)"

### Graceful Degradation

- **YouTube API 실패** → 에러 메시지 표시 + Phase 3에서 수동 입력으로 폴백
- **Slack 미연결** → Slack 섹션 스킵, 수동 입력 안내
- **이전 주 노트 없음** → "vs Last Week" = "N/A (first run)"

---

## Phase 2: 자동 분석 + 인사이트 생성

`references/analysis-guide.md`의 규칙을 참고하여 분석한다.

### 2-A. 퍼포먼스 테이블 자동 채우기

- **vs Target**: config의 목표치 대비 현재치 (%, ↑↓)
- **vs Last Week**: 이전 주 대비 변화 (delta, %)
- **Trend**: 최근 4주 추세 (↑ improving / → stable / ↓ declining)

### 2-B. 이상치 탐지 & 플래그

- baseline avg 대비 **2x 이상** → `POTENTIAL HIT` 플래그
- baseline avg 대비 **0.5x 이하** → `UNDERPERFORMING` 플래그
- 이전 주 대비 **±30% 이상** 변동 → `SIGNIFICANT CHANGE` 플래그

### 2-C. 자동 인사이트

- 주간 요약 1줄 자동 생성 (예: "Strong week — 2 mega-hits pushed Monthly Views 15% above target")
- Top performer 분석 (왜 잘 됐는지 가설)
- Underperformer 분석 (가능한 원인 가설)

### 2-D. Slack 파이프라인 상태표

Slack 데이터가 있으면:

| Project | Stage | Owner | ETA | Notes |
|---------|-------|-------|-----|-------|
| (자동 채움) | | | | |

---

## Phase 3: 수동 입력 (AskUserQuestion)

**자동 수집 결과를 먼저 표시**한 후, 빈 칸만 질문한다.

### 표시할 자동 결과

Phase 1-2의 결과를 요약 표시:
- 채널 통계 (구독자, 조회수)
- 퍼포먼스 테이블 (자동 채운 부분)
- 영상별 성과 등급
- Slack 파이프라인 상태 (있는 경우)

### 질문할 항목 (Analytics API 필요 → 수동)

AskUserQuestion을 사용하여 질문:

1. **YouTube Studio 데이터** (자동 수집 불가):
   - Direct Traffic %
   - CTR (Click-Through Rate)
   - 기타 Analytics 지표 (선택)

2. **정성적 판단**:
   - What we tested this week
   - What we learned
   - What we will change

3. **파이프라인 업데이트** (Slack 데이터 보충):
   - 추가/변경된 프로젝트
   - 이번 주 결정이 필요한 사항

4. **추가 메모** (선택):
   - 회의에서 공유할 추가 사항

---

## Phase 4: 최종 문서 생성

### 4-A. 데이터 합치기
- Phase 1-2 자동 데이터 + Phase 3 수동 입력을 `references/template.md` 형식으로 결합

### 4-B. 한국어 → 영어 변환
- 모든 한국어 텍스트를 영어로 번역
- 번역 규칙:
  - 고유명사(인물명, 회사명, 프로젝트명): 원문 그대로 유지
  - 메트릭/숫자: 정확하게 보존
  - 비즈니스 톤: 간결하고 전문적인 영어 (bullet point 위주)
  - 한국어 맥락이 필요한 경우 괄호 안에 원문 병기

### 4-C. 파일 저장
1. 디렉토리 확인/생성: `~/Desktop/Cowork/meeting-notes/`
2. 마크다운 저장: `~/Desktop/Cowork/meeting-notes/weekly-YYYY-MM-DD.md`
3. 클립보드 복사: `pbcopy`

### 4-D. 차트 HTML 생성
1. `~/Desktop/Cowork/meeting-notes/weekly-YYYY-MM-DD-chart.html` 저장
2. 다크 테마 standalone HTML (Chart.js CDN 사용, 서버 불필요)
3. 포함 차트:
   - **KPI Cards**: 구독자, 월간 조회수, 메가히트/히트 수, 베이스라인 평균
   - **Views by Video**: 가로 막대 차트 (등급별 색상 — 녹색=HIT, 노란색=Potential, 파란색=Baseline, 빨간색=Under)
   - **포맷별 도넛 차트**: 교수/학자 인터뷰 vs Shorts vs Founder Stories 조회수 비중
   - **Engagement 차트**: 좋아요/댓글 (Top 6 영상)
   - **Key Insight 박스**: 핵심 분석 1-2줄
4. `open` 명령으로 브라우저에서 자동 열기
5. 용도: 노션에 캡처해서 붙여넣기, 회의 화면 공유

### 4-E. 핵심 지표 요약 출력

최종적으로 사용자에게 한눈에 보이는 요약을 출력:

```
── Weekly Summary ──────────────────────
Subscribers: XXX,XXX (target: 1M → XX%)
Monthly Views: X.XM (vs target: +XX%)
Mega-hits: X | Hits: X | Underperformers: X
Top: "Video Title" (XXX,XXX views)
────────────────────────────────────────
Saved: ~/Desktop/Cowork/meeting-notes/weekly-YYYY-MM-DD.md
Chart: ~/Desktop/Cowork/meeting-notes/weekly-YYYY-MM-DD-chart.html
Copied to clipboard.
```

---

## 참고 파일

| 파일 | 용도 |
|------|------|
| `config/config.json` | API 키, 채널 ID, 목표치, Slack 채널 (gitignore 대상) |
| `config/config.example.json` | 설정 파일 템플릿 (구조 참고용) |
| `references/template.md` | 최종 출력 마크다운 템플릿 |
| `references/analysis-guide.md` | 이상치 감지 규칙, 인사이트 생성 패턴 |
| `scripts/fetch-youtube-data.sh` | YouTube API 호출 스크립트 |
