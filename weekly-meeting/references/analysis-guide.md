# Analysis Guide — Weekly Meeting Prep

이 문서는 YouTube 데이터 분석 시 사용하는 규칙과 패턴을 정의한다.

---

## 1. 성과 등급 (Video Grade)

영상별 조회수(views)를 기준으로 등급을 매긴다.

| Grade | Criteria | Emoji |
|-------|----------|-------|
| MEGA-HIT | views >= `mega_hit_threshold` (default: 500K) | * |
| HIT | views >= `hit_threshold` (default: 200K) and < mega_hit_threshold | ! |
| BASELINE | views between 0.5x ~ 2x of baseline_avg | |
| UNDERPERFORMER | views < 0.5x of baseline_avg | ? |

### Baseline 계산
- 최근 30일 영상 중 조회수 상위 N개(`top_n_exclude_for_baseline`, default: 3) 제외
- 나머지 영상의 평균 조회수 = baseline_avg
- 이유: 바이럴 영상이 평균을 왜곡하는 것을 방지

---

## 2. 이상치 탐지 (Anomaly Detection)

### 2-A. vs Baseline 이상치

| Flag | Condition | 의미 |
|------|-----------|------|
| `POTENTIAL HIT` | views >= baseline_avg * `potential_hit_multiplier` (2.0x) | 평균 대비 크게 상회 → 히트 가능성 |
| `UNDERPERFORMING` | views <= baseline_avg * `underperformer_multiplier` (0.5x) | 평균 대비 크게 하회 → 원인 분석 필요 |

### 2-B. vs Last Week 이상치

| Flag | Condition | 의미 |
|------|-----------|------|
| `SIGNIFICANT CHANGE` | 주간 변화율 >= `significant_change_threshold` (30%) | 지표에 유의미한 변화 발생 |

적용 대상: Monthly Views, Subscribers, Baseline avg

---

## 3. 인사이트 생성 패턴

### 3-A. 주간 요약 (1줄 자동 생성)

조건별 템플릿:

- **Monthly Views가 목표 초과**: "Strong week — Monthly Views {X}% above target, driven by {top_video_title}"
- **Mega-hit 발생**: "Breakout week — {count} mega-hit(s) led by \"{title}\" ({views} views)"
- **목표 미달이지만 개선**: "Recovering — Monthly Views still {X}% below target but up {Y}% from last week"
- **하락세**: "Challenging week — Monthly Views down {X}% from last week, {count} underperformers flagged"
- **안정적**: "Steady week — metrics in line with targets, no significant outliers"

### 3-B. Top Performer 분석

조회수 1위 영상에 대해 가능한 성공 요인 가설을 제시:

1. **제목/썸네일**: 클릭 유도 요소 분석
2. **주제**: 시의성, 트렌드 부합도
3. **게스트**: 인지도, 팔로워 수
4. **게시 타이밍**: 요일, 시간대
5. **시리즈 효과**: 기존 히트 영상과의 연관성

### 3-C. Underperformer 분석

부진 영상에 대해 가능한 원인 가설:

1. **주제 관심도**: 니치한 주제 vs 대중적 관심
2. **경쟁 콘텐츠**: 같은 주제의 경쟁 영상 존재 여부
3. **제목/썸네일**: 클릭 유도력 부족
4. **게시 타이밍**: 비최적 시간대
5. **채널 피로도**: 유사 주제 연속 게시

---

## 4. Trend 판단 기준

최근 4주 데이터를 기반으로 추세를 판단:

| Trend | Condition |
|-------|-----------|
| ↑ (improving) | 최근 2주 연속 상승 OR 4주 중 3주 상승 |
| → (stable) | 변동 폭이 ±10% 이내 |
| ↓ (declining) | 최근 2주 연속 하락 OR 4주 중 3주 하락 |

Trend가 표시되려면 최소 2주치 이전 데이터가 필요. 없으면 "—" 표시.

---

## 5. Slack 데이터 처리 규칙

### 5-A. 프로덕션 단계 식별

메시지에서 다음 키워드로 단계를 판단:

| Stage | 한국어 키워드 | 영어 키워드 |
|-------|-------------|-------------|
| Outreach | 섭외, 컨택, 이메일 | outreach, contact, email |
| Confirmed | 확정, 컨펌 | confirmed, locked in |
| Pre-production | 사전 준비, 질문지, 브리핑 | pre-production, questions, briefing |
| Filming | 촬영, 녹화 | filming, recording, shoot |
| Editing | 편집, 자막, 후반 | editing, subtitles, post |
| Review | 검수, 리뷰, 확인 | review, check |
| Upload | 업로드, 예약 | upload, schedule |
| Published | 게시, 공개 | published, live |

### 5-B. 프로젝트 식별

메시지에서 인물명, 회사명, 에피소드 번호 등을 추출하여 프로젝트 단위로 그룹핑.

---

## 6. Graceful Degradation 규칙

| 상황 | 대응 |
|------|------|
| YouTube API 실패 | "[API ERROR] Unable to fetch — please enter manually" 표시. Phase 3에서 수동 입력 |
| API quota 초과 | "[QUOTA EXCEEDED] Daily limit reached" 표시. 다음 날 재시도 안내 |
| Slack 미연결 | Section 3 "From Slack" → "(Slack not connected — enter manually below)" |
| 이전 주 데이터 없음 | "vs Last Week" = "N/A (first run)" / Trend = "—" |
| 영상 0개 (30일) | "No videos published in last 30 days" 경고 |
