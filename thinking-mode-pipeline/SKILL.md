---
name: thinking-mode-pipeline
description: The Thinking Mode 시리즈 콘텐츠 파이프라인. 트렌드 스캔 → 게스트 검증 → 의사결정 → 아웃리치 → 심층 리서치 → 질문지. "thinking mode pipeline", "게스트 발굴", "파이프라인", "guest validation", "게스트 검증", "섭외 파이프라인" 요청에 사용.
user_invocable: true
---

# The Thinking Mode — Content Pipeline

EP1 (Po-Shen Loh) 1M views가 기준. 이 파이프라인은 1M-view 에피소드를 체계적으로 재현하기 위한 6단계 프로세스다.

**핵심 원칙: 인물 발굴이 핵심** — 누구를 인터뷰하느냐가 조회수의 80%를 결정한다.

---

## 호출 방법

```
/thinking-mode-pipeline              → 6단계 안내 + 어디서 시작할지 질문
/thinking-mode-pipeline trend        → Stage 1: Trend Radar
/thinking-mode-pipeline validate <name>  → Stage 2: Guest Validation
/thinking-mode-pipeline validate-batch   → Stage 2-Batch: 여러 게스트 동시 검증
/thinking-mode-pipeline decide       → Stage 3: Decision Gate
/thinking-mode-pipeline outreach <name>  → Stage 4: Outreach Email
/thinking-mode-pipeline research <name>  → Stage 5: Deep Research
/thinking-mode-pipeline questions <name> → Stage 6: Interview Questions
```

인자 없이 호출 시, AskUserQuestion으로 어떤 단계를 실행할지 묻는다.

---

## 시리즈 컨텍스트

| Item | Detail |
|------|--------|
| **시리즈** | The Thinking Mode: A guide for thinking human |
| **미션** | AI 시대, 미래를 어떻게 대비하고, 새로운 생각을 하며 인간의 Edge를 유지할 것인가 |
| **톤** | Practical Optimism — FOMO가 아닌 성장 동기 |
| **채널** | EO Global (@eoglobal), 650K+ subscribers |
| **벤치마크** | EP1 Po-Shen Loh: 1M views |
| **타겟** | AI 시대에 대체 불가능한 해법을 찾는 고지능 실용주의 성취자 |
| **듀얼 레이어** | 표면=실용적 AI 리터러시 / 깊은 층=정체성·사고방식 전환 |

### 4 Core Audience Personas

1. **실전 지향형 창업가/실무자** — 당장 쓸 수 있는 프레임워크 요구
2. **AI 공생 희망자** — AI와 협업하는 미래 설계
3. **회의적 지식 검증가** — 근거 있는 주장만 수용, 해묵은 얘기 거부
4. **교육 혁신 갈망자** — 학습/교육 시스템의 근본적 변화 추구

---

## Stage 1: Trend Radar (`trend`)

**목적:** 시리즈 미션에 맞는 현재 핫이슈를 스캔한다.

### 프로세스

1. **WebSearch** — AI × Education × Career × Ethics 최근 2주 트렌드
2. **소셜 버즈** — X/Twitter, LinkedIn, Reddit, Hacker News 키워드 스캔
3. **경쟁 채널 갭 분석** — DOAC, Lex Fridman, Impact Theory, Veritasium가 안 다룬 주제
4. **미션 매핑** — 트렌드를 시리즈 미션(인간의 Edge 유지)에 연결
5. **트렌드 스코어링**

### 스코어링

각 트렌드에 3개 차원 평가:

| Dimension | Question | Score |
|-----------|----------|:-----:|
| **Media Impact** | 유튜브에서 얼마나 임팩트를 만들 수 있나? (조회수, 댓글, 공유) | ★1-5 |
| **Series Fit** | 시리즈 미션(AI 시대 인간의 Edge)에 맞나? | ★1-5 |
| **Timeliness** | 지금이 아니면 늦는 주제인가? | ★1-5 |

### 출력

트렌드 보고서:
- 상위 5-10개 핫이슈 (스코어 순 정렬)
- 각 이슈: 지지 기사/포스트 링크 + 수치
- 각 이슈: 잠재 게스트 앵글 1-2개
- 경쟁 채널 갭 표

---

## Stage 2: Guest Validation (`validate <name>`)

**이 단계가 가장 중요하다** — 이 게스트가 다음 1M-view 에피소드가 될 수 있는지 결정한다.

### 2-Document 구조

Stage 2는 **두 개의 문서**를 동시에 생성한다:

1. **리서치 문서** (Research Brief) — 딥 리서치 에이전트가 작성
   - 인물 배경, 경력, 핵심 주장/프레임워크 (실제 저서·논문·강연 기반)
   - 최근 활동 (최근 몇 주~몇 개월 이내 기사, 인터뷰, 출판)
   - 기존 미디어 출연, SNS 팔로워, 논쟁 이력
   - 이 문서가 검증의 근거 자료

2. **검증 문서** (Validation Report) — 검증 에이전트가 리서치 문서를 읽고 작성
   - 정보 브리프 (처음 보는 사람도 즉시 파악 가능한 1-2줄 소개)
   - 5-Dimension 점수 + 근거
   - 야마 (리서치에서 나온 실제 주장 기반)
   - Framing Test + Verdict

**에이전트 구조 (validate-batch 시):**
```
리서치 에이전트 (정보 수집) → 리서치 문서 작성
       ↓
검증 에이전트 (리서치 문서를 읽고 판단) → 검증 문서 작성
```

### 프로세스

**Step 1: 프로필 리서치** (WebSearch + WebFetch 병렬) → 리서치 문서로 정리
- 배경, 현재 역할, 핵심 성과 (수치 포함)
- SNS 팔로워 수, 뉴스레터 구독자 수
- 기존 미디어 출연 (팟캐스트, YouTube, TED, 기사)
- 최근 출판/프로젝트

**Step 2: 5-Dimension Scoring**

확정 게스트 패턴 기반 (Po-Shen Loh, Mihail Eric, Rem Koning, Drew Bent, Kartik Hosanagar 등):
- 공통점: 톱 대학/기관 소속 + AI×Education 교차점 + 명확한 앵글

| # | Dimension | Question | 체크 포인트 | Score |
|:-:|-----------|----------|------------|:-----:|
| 1 | **Authority (권위)** | 이 사람의 말에 무게를 실어줄 근거가 있나? | 대학 소속(어디?), 저서/논문, 직함, 수상/인정 | ★1-5 |
| 2 | **Media Charisma (미디어 매력도)** | 영상에서 매력적인가? | 젊은가, 말 잘하나, 본인 채널/콘텐츠 운영 여부, 기존 영상 매력도 | ★1-5 |
| 3 | **Hot Take** | 이 사람만의 뾰족한 관점이 있나? | 논쟁 가능한 주장, 프레임워크, 남들과 다른 포지션, **새로운 시각/본인만의 미션** (새로운 시각을 제시하는 게스트 = 채널 반응 좋음) | ★1-5 |
| 4 | **Timeliness (시의성)** | 왜 지금? | 신작/프로젝트, 뉴스 사이클, 최근 6개월 이내 활동 | ★1-5 |
| 5 | **EO Fit (시리즈 적합성)** | The Thinking Mode에 맞나? | 미션(인간의 Edge) 부합, 기존 에피소드와 차별화, 오디언스 매칭 | ★1-5 |

**Authority 기준 (확정 게스트 패턴):**
- ★5: 세계적 대학 교수 + 베스트셀러 저자 (예: Wharton, Stanford, MIT)
- ★4: 톱 대학 소속 + 전문 분야 인정 (예: HBS 교수, Anthropic 연구원)
- ★3: 유명 기관 소속 또는 저서 1-2권 (예: 테크 기업 리더 + 책)
- ★2: 업계 전문가이지만 학술적/저서 권위 약함
- ★1: 권위 근거 불충분

**Media Charisma 기준:**
- ★5: 본인 채널(YouTube/팟캐스트) 운영 + 기존 영상에서 탁월한 전달력 + 에너지
- ★4: 미디어 출연 다수 + 말 잘함 + 시각적 매력
- ★3: TED/팟캐스트 경험 있음, 무난한 전달력
- ★2: 미디어 경험 적음, 학술적 톤 위주
- ★1: 영상 매력도 증거 없음

**EO 채널 적합성 판단 시 핵심 고려사항:**
- EO Global은 Po-Shen Loh, Jeremy Utley 같은 **교수형 thought leader**가 폭발적 반응을 얻은 채널
- 다른 미디어에서 조회수가 낮더라도 EO 오디언스에게 매력적이면 터질 수 있음
- 반대로 빅네임이라도 EO 시청자 취향과 맞지 않으면 성과가 낮을 수 있음
- **빅네임(섭외 난이도 ★★★★★)은 장기 타겟으로 분류** — 즉시 아웃리치보다 관계 구축 우선
- 판단 기준: "이 사람의 강의/인터뷰를 EO 시청자가 끝까지 볼 것인가?"

**Threshold:**
- **≥ 20/25 → Go** — 즉시 아웃리치
- **15-19 → Maybe** — 추가 조사 또는 앵글 개발 필요
- **≤ 14 → Pass** — 사유와 함께 아카이브

**Step 3: Framing Test** (Copy Workflow v6 패턴)

`~/.claude/skills/copy-thinking-mode/SKILL.md`의 CTR Scoring Model v6을 참조하여:
- 제목/썸네일 콘셉트 카드 3개 생성
- CTR 스코어링 적용 (Base 3.11% + 가산/감산)
- 검증된 패턴 활용: 정체성 제안 + 버전넘버링 + 변환

**Framing Test Pass: 최소 1개 콘셉트 predicted CTR ≥ 6.0%**

**Step 4: 레퍼런스 미디어**
- 베스트 기존 인터뷰/강연 3개 (링크 + 조회수)
- 핵심 인용구 (훅 후보)
- 논쟁/토론 앵글

**Step 5: 오디언스 페르소나 매칭**
- 4 Core Personas 중 해당하는 것
- 듀얼 레이어 체크: 표면적 실용 가치 + 깊은 정체성 전환

**Step 6: 야마 (One-Line Angle)**

영상의 핵심 앵글을 영어 한 줄로 정의한다. 이것이 곧 이 에피소드의 주제(야마)가 된다.

**야마 작성 공식 (EP1/EP2 패턴 기반):**
- EP1: "The One Human Edge That Only Grows Sharper After AI | **Carnegie Mellon University**, Po-Shen Loh" → 렌즈: 수학적 사고/공감 능력
- EP2: "How to Manage Multiple Agents Like a Top 1% Engineer | **Stanford University**, Mihail Eric" → 렌즈: 소프트웨어 엔지니어링

**야마 필수 요소:**
1. **실제 리서치 기반** — 야마는 반드시 게스트가 **실제로 주장/연구/출판한 내용**에 근거해야 함. 바이럴을 위해 지어내는 것 절대 금지. 게스트의 책, 논문, 인터뷰, 강연에서 나온 실제 테제를 야마의 뼈대로 삼는다.
2. **구체적 토픽 렌즈** — "AI" 일반론 금지. 반드시 specific domain을 명시 (예: neuroscience, game theory, labor economics, governance, learning science, antifragility)
3. **대학 이름** — 명문대 소속이면 반드시 야마/제목에 포함 (Harvard, Stanford, MIT, Wharton, CMU 등)
4. **행동 가능한 주장** — "How to..." / "Why..." / "The Only..." 형태의 provocative claim
5. **정체성 제안** — 시청자가 되고 싶은 모습을 암시 ("Top 1% Engineer", "Thinking Human")

**야마 시간축 분류 (반드시 태깅):**
- 🔴 **TIMELY** — 최근 몇 주 이내 이슈와 직결되는 앵글. "몇 개월 전"은 TIMELY가 아님.
- 🟢 **EVERGREEN** — 12개월 후에도 유효한 보편적 인사이트 (프레임워크, 인간 본성)
- 🟡 **BOTH** — 에버그린 인사이트 + 타임리 훅이 동시에 있는 최적 조합

**정보 브리프 필수:** 야마와 함께 반드시 게스트 정보 브리프를 포함한다. 처음 보는 사람도 "어디 소속이고, 어떤 일을 하고, 어떤 주장을 하는 사람"인지 즉시 파악할 수 있어야 함.

**야마 출력 형식:**
```
[이름] ([대학]) — [🔴/🟢/🟡]
> "[구체적 도메인] + [대담한 주장] | [대학], [이름]"
> **Topic Lens:** [구체적 분야 키워드]
> **Why Now:** [2-3문장]
```

**야마는 검증 보고서의 가장 중요한 항목 중 하나 — 이것이 없으면 보고서가 불완전하다.**

**Step 7: 팩트체크 (Fact-Check)**

리서치 결과의 정확성을 검증한다. 틀린 내용이 팀에 공유되면 안 된다.

**검증 항목:**
1. **인물 정보** — 소속 대학/기관, 직함이 현재 기준으로 맞는가?
2. **저서/논문** — 제목, 출판연도, 출판사가 정확한가?
3. **수치** — 팔로워 수, 조회수, 수강자 수 등이 출처가 있는가?
4. **최근 활동** — 날짜, 매체, 발언 내용이 실제 기사/영상에서 확인되는가?
5. **핵심 주장** — 게스트가 실제로 그 주장을 했는가? 맥락에서 벗어나 과장/왜곡하지 않았는가?

**검증 방법:**
- WebSearch로 각 주요 사실(이름+직함, 책 제목+연도, 발언+매체)을 개별 교차 확인
- 확인된 사항은 ✅, 미확인은 ⚠️ 태깅
- ⚠️가 2개 이상이면 해당 게스트의 리서치를 재검색

**팩트체크 출력 형식:**
```
[게스트 이름] 팩트체크:
✅ 소속: [확인된 정보] (출처)
✅ 저서: [확인된 정보] (출처)
⚠️ 수치: [미확인 항목] — 재확인 필요
✅ 최근 발언: [확인된 정보] (출처 링크)
```

### 출력

**2개 문서 동시 생성:**

1. **검증 문서** (Validation Master) — `references/guest-validation-template.md` 형식
   - 정보 브리프 + 5-Dimension 점수 + 야마 + Verdict
   - 팀 공유용: 핵심만 빠르게 파악 가능

2. **리서치 문서** (Research Compilation) — 우선순위 순으로 정렬
   - 최우선 게스트가 맨 위, 낮은 순서대로 아래로
   - 상세 리서치: 경력, 핵심 주장/프레임워크, 최근 활동, 기존 인터뷰, 출처 링크
   - 시리즈 연결이 약한 게스트는 리서치를 더 상세히 (앵글 탐색용)
   - 팩트체크 결과 포함

---

## Stage 2-Batch: Batch Validation (`validate-batch`)

**목적:** 여러 게스트를 병렬로 검증한다.

### 프로세스

1. 사용자에게 게스트 리스트 확인 (AskUserQuestion)
2. **에이전트 팀 생성** (TeamCreate)
   ```
   Team Lead (main)
   ├── validator-1 (general-purpose agent, guest A)
   ├── validator-2 (general-purpose agent, guest B)
   ├── validator-3 (general-purpose agent, guest C)
   └── ... (max 5 concurrent)
   ```
3. 각 validator에게 전달:
   - 게스트 이름/정보
   - Stage 2 전체 방법론 (이 SKILL.md의 Stage 2 섹션)
   - Copy Workflow v6 패턴 (framing test용)
   - 시리즈 미션 + 오디언스 컨텍스트
4. 결과 수집 → 총점 기준 정렬
5. 비교 테이블 + 개별 보고서 제시

### 비교 테이블 출력 형식

```
━━━ Batch Validation Results ━━━━━━━━━━━━━━━━━━━━━━━
| Rank | Guest | Total | Auth | Charm | HotTk | Time | Fit | CTR Best | Verdict |
|:----:|-------|:-----:|:----:|:-----:|:-----:|:----:|:---:|:--------:|:-------:|
| 1 | ... | /25 | /5 | /5 | /5 | /5 | /5 | X.XX% | GO |

야마 (One-Line Angle):
- Guest A: "..."
  → Why Now: ...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 게스트 수가 5명 초과 시

5명씩 배치(batch)로 나눠 순차 실행. 각 배치 완료 후 중간 결과 보고.

---

## Stage 3: Decision Gate (`decide`)

**목적:** 검증 결과를 보고 Jiyoon이 Go/Maybe/Pass 결정.

### 프로세스

1. Stage 2(또는 2-Batch) 결과 요약 테이블 표시
2. 각 게스트별:
   - 5-dimension 점수
   - 베스트 framing 콘셉트
   - 핵심 리스크
3. **AskUserQuestion** — 게스트별 Go / Maybe / Pass 선택
4. Go → Stage 4로 진행
5. Maybe → 추가 조사 필요 항목 기록
6. Pass → 사유와 함께 아카이브

### 출력

결정 기록:
```
━━━ Decision Gate Results ━━━━━━━━━━━━━━━━━━━━━━━━━
| Guest | Score | Decision | Next Step |
|-------|:-----:|:--------:|-----------|
| ... | /25 | GO | → Stage 4 Outreach |
| ... | /25 | MAYBE | Need: [추가 정보] |
| ... | /25 | PASS | Reason: [사유] |
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Stage 4: Outreach Email (`outreach <name>`)

**목적:** 승인된 게스트에게 보낼 섭외 이메일 초안.

### 프로세스

1. `references/outreach-email-template.md` 읽기
2. Stage 2 검증 데이터로 P2(개인화 단락) 작성:
   - 게스트의 최근 작업/프로젝트에 대한 구체적 언급
   - 시리즈와의 연결점
   - 유니크 앵글
3. 채널 신뢰도 포인트 포함:
   - EP1 Po-Shen Loh 1M views
   - 650K+ subscribers
   - Past guests: Stanford, HBS, Wharton, Anthropic, Roblox
4. 영어로 작성
5. 사용자에게 보여주고 승인받기

### 출력

- 이메일 초안 (바로 보낼 수 있는 형태)
- 제목 라인 3개 옵션
- 7일 후 팔로업 이메일 초안

---

## Stage 5: Deep Research & Briefing (`research <name>`)

**목적:** 확정 게스트에 대한 포괄적 리서치. 인터뷰 준비의 핵심.

### 프로세스

**반드시 `~/Desktop/Cowork/Research workflow/eo_interview_research_workflow_v1.md`를 먼저 읽고** Phase 1 + Phase 2를 실행한다.

**Step 1: Deep Background**
- 전체 경력 타임라인 (수치 포함)
- 모든 출판물 (책, 논문, 기사, 뉴스레터)
- 핵심 주장/테제
- 최근 공개 발언 및 포지션

**Step 2: Content Audit**
- 기존 인터뷰/팟캐스트 상위 5개+ 분석 (WebFetch 활용)
- **해묵은 얘기 필터**: 3회 이상 반복한 스토리 → "Already Exhausted" 태그
- **아직 안 물어본 것**: 모든 인터뷰어가 빠뜨린 질문 = EO의 기회

**Step 3: Issue Mapping**
- 현재 핫토픽과 연결 (Stage 1 결과 참조)
- 논쟁/토론 앵글
- 4 Core Personas 매핑

**Step 4: Hot Take Extraction**

Hot Take = 3가지 동시 충족:
1. **Uniqueness** — 이 사람만 할 수 있는 이야기
2. **Reactivity** — 자기진단/논쟁/놀라움/자격도전 유발
3. **Timeliness** — 6개월 전에도 할 수 있었으면 탈락

각 Hot Take에 3조건 점수 부여 (총 /15). 12 이상 → Lesson 핵심 소재.
**Staleness filter**: 5회 이상 반복 → 자동 하위 배치.

### 출력

리서치 브리핑 (`research-briefing-2026-03-01.md` 형식 참조):
1. 상황 컨텍스트 (지금 무슨 일이 벌어지고 있나)
2. 게스트 프로필 + 경력 타임라인
3. Hot Take 후보 (평가 점수 포함)
4. Theme + Title/Thumbnail + Lessons 옵션 2-3개
5. 앵글 브레인스토밍
6. 추천 우선순위

Phase 2 완료 시 사용자에게 결과를 보여주고 **방향 확정**받는다.

---

## Stage 6: Interview Questions (`questions <name>`)

**목적:** 인터뷰 질문지 초안 작성 (영어).

### 프로세스

1. Stage 5 리서치 브리핑 읽기 (없으면 Stage 5 먼저 실행 안내)
2. `references/question-list-template.md` 형식 따르기
3. `~/Desktop/Cowork/Research workflow/eo_interview_research_workflow_v1.md` Phase 3 절차 따르기

**질문지 구조:**

| Section | Duration | Content |
|---------|:--------:|---------|
| Introduction | ~8 min | Who is this person + why now |
| Lesson 1 | ~10-15 min | {게스트별 고유 주제} |
| Lesson 2 | ~10-15 min | {게스트별 고유 주제} |
| Lesson 3 | ~10-15 min | {게스트별 고유 주제} |
| Additional/Closing | ~8 min | 추가 질문 + 마무리 |

**Lesson 설계 원칙:**
- 각 Lesson은 독립된 주제와 명확한 Goal을 가져야 함
- 3개 Lesson 전체에 걸쳐 아래 3가지가 반드시 포함되어야 함:
  - **왜 들어야 하는가** (hook/context)
  - **핵심 인사이트** (core insight)
  - **그래서 뭘 해야 하는가** (actionable takeaway)
- 단, 순서와 배분은 게스트와 주제에 따라 자유롭게 설계

**질문 작성 규칙:**
- 영어 본문 + 한국어 번역 병기
- 🔴 Must-ask (Lesson당 최소 2개)
- → Follow-up (모든 🔴에 최소 1개)
- 🖥️ Screen share 포인트 표시
- 구체적 질문만 (일반론 금지)
- 게스트 고유 질문 우선
- 해묵은 얘기 필터 적용 (Stage 5 결과 활용)

### 출력

파일 저장: `~/Desktop/Cowork/interview_prep_{guest_name}_{date}.md`

---

## 규칙

- **야마** = 영상의 핵심 앵글, 한 줄 주제. 게스트 검증 시 반드시 영어 한 줄 + Why Now 브리프 포함
- 출력 언어: 제목/썸네일/질문은 **영어**. 분석/노트는 **한국어 가능**
- 리서치 결과에는 반드시 수치 포함 (조회수, 구독자, 날짜 등)
- 모호하면 추측하지 말고 AskUserQuestion으로 질문
- Stage 간 이동 시 이전 단계 결과를 참조 (데이터 연결)
- 파일 저장 시 전체 경로 출력
- EP1 벤치마크(1M views, Po-Shen Loh)를 검증 기준으로 활용
- 각 단계에 독립적으로 진입 가능 — 이전 단계 결과 없이도 실행 가능하지만, 있으면 활용

## 참고 파일

| File | Purpose |
|------|---------|
| `references/guest-validation-template.md` | Stage 2 출력 템플릿 |
| `references/outreach-email-template.md` | Stage 4 이메일 템플릿 |
| `references/question-list-template.md` | Stage 6 질문지 템플릿 |
| `~/.claude/skills/copy-thinking-mode/SKILL.md` | CTR Scoring Model v6, framing 패턴 |
| `~/Desktop/Cowork/Research workflow/eo_interview_research_workflow_v1.md` | 심층 리서치 방법론 |
