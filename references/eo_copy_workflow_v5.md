# EO Global Copy Workflow v5.1
## 데이터 기반 제목·썸네일 최적화 프로세스

> v5 → v5.1 업데이트: 4개 영상 댓글 분석(397개) 결과 반영. Comment Intelligence 프레임워크 실전 데이터로 강화
> v4 → v5 업데이트: Thinking Mode EP1 (Mihail Eric) A/B 테스트 2회 결과 반영 + Intelligence EP1 (Po-Shen Loh) 실제 우승 세트 보정
> Thinking Mode EP1 결과: CTR 6.0%, 노출 91.3K, 조회수 8.3K (+3.4K vs 평소)
> A/B 1차: 3세트 중 "Software Engineer 3.0" + "From X to Y" 조합 WTS 38% 우승
> A/B 2차: 우승 세트 vs 챌린저 → 62.7% vs 37.3%로 우승 세트 압도적 재확인
> Intelligence EP1 보정: 실제 우승 세트는 "RURAL / URBAN" + "AI Will Create New Wealth, But Not Where You Think" (Watch Time Share 35.4%)
> v5.1 핵심 추가: 댓글 논쟁 패턴 = CTR 예측의 후행 지표. 논쟁 유발하는 제목이 알고리즘도 밀어줌

---

## 워크플로우 8단계

```
촬영 전 ─── Step 0: 콘셉트 사전검증
              │
촬영 후 ─── Step 1: 스크립트 분석 (Hook Inventory)
              │
              Step 1.5: 이전 영상 댓글 분석
              │
              Step 2: 트렌드 인텔리전스 (3-Layer Scan) + 경쟁 채널 카피 분석
              │
              Step 3: 콘셉트 개발 (Title + Thumbnail = 1 Unit)
              │
              Step 4: CTR 예측 + 근거 매칭
              │
게시 ──── Step 5: A/B 테스트 세팅 (3세트) + 게시
              │
0~24h ──── Step 6: 실시간 모니터링 + 적극 교체
              │
7~30일 ─── Step 7: 피드백 루프 (패턴 풀 업데이트)
```

---

### Step 0: 콘셉트 사전검증 (촬영 전 — 선택)

**DOAC 방식:** 촬영 전에 썸네일 100개 → Facebook 광고 CTR 테스트. 안 먹히면 촬영 안 함.

**EO 적용:**
- 촬영 전 게스트 정보만으로 제목-썸네일 콘셉트 3-5개 스케치
- 팀 내부 투표 또는 커뮤니티 스토리로 반응 확인
- 안 되면 인터뷰 질문 조정 (훅이 될 답변을 끌어낼 질문 추가)

**언제 필수:** 게스트가 무명이거나 주제가 니치할 때

---

### Step 1: 스크립트 분석 (Hook Inventory)

**입력:** 편집 완료된 스크립트 or 촬영 내용 요약

**뽑아야 하는 것:**

| Hook 유형 | 설명 | 예시 |
|-----------|------|------|
| **신뢰 Hook** | 검증 가능한 성과, 투자, 수치 | a16z+Sequoia 공동투자, Stanford's first AI class |
| **드라마 Hook** | 희생, 갈등, 반전, 언더독 | 1000 applications, 2 callbacks |
| **숫자 Hook** | 달러, 유저수, 나이, 퍼센트 | Top 1%, 0.1%, 3 Forces |
| **반직관 Hook** | 통념을 뒤집는 사실 | More agents = worse code |
| **최상급 Hook** | 최초, 최대, 유일, 가장 | Stanford's first AI-native software dev class |
| **변환 Hook (v5 신규)** | 역할/정체성의 변화 | From writing code to managing agents |

**게스트 유명도 판단:**

| 유명도 | 제목 전략 | 파이프(\|) 뒤 |
|:---:|-----------|-----------|
| 대중적 유명 (일론 머스크급) | 이름이 곧 훅. 이름 먼저 | 이름만 |
| 업계 유명 (Sam Altman급) | 이름 + 직함/회사 | 이름, 회사 |
| 니치/무명 | 이름 쓰지 않음. 스토리/숫자로 훅 | 이름, 회사 (태그만) |

> 무명 기업/게스트 이름은 제목 메인에 넣지 않는다. 파이프 뒤에만.

**게스트 직함 주의사항 (v4~):**
- 게스트의 **현재 직함**만 사용. 과거 직함 쓰지 않기
- 약어 금지: "CMU" ✗ → "Carnegie Mellon" ✓
- 대중이 모르는 기관/직함은 더 보편적인 표현으로 대체
- 파이프 뒤 기관명은 줄일 수 있음: 썸네일에 이미 있으면 제목에서 생략 가능 (v5 추가)

---

### Step 1.5: Comment Intelligence (댓글 분석)

**같은 게스트의 이전 영상, 비슷한 주제 영상, 또는 최근 잘 나간 EO 영상 3-5개에서 실행.**

> **핵심 원칙: 늘 긍정적인 댓글만 달리는 영상은 오히려 별로다. 논쟁을 유발하는 제목/썸네일이 더 좋은 카피.** 댓글에서 찬반이 갈리고 답글이 폭발하면, 그 제목이 강한 감정을 건드렸다는 증거이자 알고리즘이 밀어줄 engagement 신호다.

#### 1.5-A: 댓글 수집 방법

| 방법 | 설명 | 권장 |
|------|------|------|
| **브라우저 자동 추출** | YouTube 영상 페이지에서 JS로 상위 댓글 30-50개 자동 수집 | 가장 빠름. 인기순(Top) 정렬로 |
| **수동 텍스트 입력** | PD가 댓글을 복사해서 텍스트로 전달 | 영상 3-5개 × 20-30개씩, 좋아요순 |

> 이상적인 입력 포맷: `[영상 제목] | CTR X% | 조회수 XX만` 아래에 `- 댓글 (좋아요 수)` 형태

#### 1.5-B: 댓글 유형 분류 (5 Types)

| 유형 | 아이콘 | 설명 | Copy 활용도 |
|------|--------|------|:-----------:|
| **💎 Quote Extraction** | 영상 속 명언을 뽑아서 공유 | ★★★ — 해당 문구가 강력한 훅. 썸네일 카피 후보 |
| **🔥 Challenge / Skeptic** | 게스트 자격 의심, 내용 반박, 회의론 | ★★★★★ — **논쟁 유발 = CTR 최강 신호** |
| **🪞 Self-Projection** | "나도 ~", "나는 ~인데 공감" | ★★★★ — 타겟 범위와 자기투영 강도 확인 |
| **✨ Discovery Joy** | "알고리즘 감사", "드디어 찾았다" | ★★★ — 추천 피드 클릭 증거 |
| **⚔️ Debate Trigger** | 찬반 양쪽이 격렬하게 싸움 | ★★★★★ — **답글 수 최다 = 알고리즘 연료** |

#### 1.5-C: 논쟁 축(Debate Axis) 도출

**답글 수 기준** 상위 5개 댓글을 분석해서, 그 영상이 유발하는 논쟁의 축을 추출.

**실전 예시 (4개 영상 분석 결과):**

| 영상 | 최다 답글 댓글 | 답글 수 | 논쟁 축 |
|------|--------------|:-------:|---------|
| Po-Shen Loh (447K views) | "We could unplug AI... but our desire to crush each other is greater" | 17 | 인간 본성 비관론 vs 낙관론 |
| Mihail Eric (12K/15h) | "Since when do journalists train engineers?" | — (15h) | 자격 도전: 누가 가르칠 자격이 있나 |
| Carina Hong / Axiom | "Silicon Valley = biggest ponzi scheme" | 14 | VC 거품론: 투자 정당성 |
| Lucy Guo | "She didn't MAKE a billion" | 3+ | 사실 검증: 성과 과장 여부 |

**논쟁 축 유형 5가지:**

| 논쟁 축 | 트리거 | 제목에서의 활용 |
|---------|--------|--------------|
| **자격 도전 (Credential Threat)** | 제목이 특정 집단의 정체성을 건드림 | "Most Engineers Aren't Ready" → 엔지니어들이 "누가 감히?" 하면서 클릭 |
| **시스템 비판 (System Critique)** | 숫자의 불균형이 불공정 감각 유발 | "24-Year-Old + $64M" → "이건 말이 안 돼" 반응 폭발 |
| **인간 본성 논쟁 (Human Nature)** | AI의 미래에 대한 철학적 질문 | "work together to survive" → 낙관 vs 비관 |
| **과대평가 회의 (Hype Skepticism)** | 과장된 것 같은 제목이 오히려 클릭 유발 | "Software Engineer 3.0" → "hype인 줄 알았는데 진짜였다" |
| **사실 검증 (Fact Check)** | 극단적 수치/주장이 검증 욕구 유발 | "Billionaire by 30" → "진짜? 확인해봐야지" |

#### 1.5-D: 시청자 생성 표현(Viewer-Generated Language) 추출

시청자가 댓글에서 직접 만든 표현은 다음 에피소드 카피에 활용하면 자연스럽게 resonance가 높음.

**실전 추출 예시:**

| 시청자 표현 | 출처 | Copy 활용 방향 |
|------------|------|--------------|
| "my mind is firing for once" | Po-Shen Loh 댓글 (412 likes) | 지적 자극 프레임 — "이 영상은 뇌가 다시 돌아가는 느낌" |
| "speaking my language" | Mihail Eric 댓글 | 전문가 공감 — "진짜 하는 사람만 알아듣는" |
| "I still don't understand how" | Carina Hong 댓글 (123 likes) | 인지 부조화 제목 — "이해가 안 되는 이유" |
| "the system is rigged" | Carina Hong 댓글 | 시스템 비판 프레임 |
| "hype clickbait... but actually legit" | Mihail Eric 댓글 | "hype 같지만 진짜" 포지셔닝 |
| "no performative drama" | Po-Shen Loh 댓글 (28 likes) | EO 브랜드 차별화 |

#### 1.5-E: 논쟁도 점수 산출 (v5.1 신규)

| 점수 | 기준 | 의미 |
|:----:|------|------|
| ★★★★★ | 상위 댓글 50%+ 가 Challenge/Debate 유형 | **카피가 강한 감정을 건드림. CTR + engagement 모두 높을 가능성** |
| ★★★★☆ | 상위 댓글에 3개 이상 논쟁 댓글 (답글 3+) | 좋은 카피. 논쟁이 살아있음 |
| ★★★☆☆ | 논쟁 댓글 1-2개 있으나 대부분 긍정 | 보통. 카피가 안전한 편 |
| ★★☆☆☆ | 거의 모든 댓글이 긍정/감사 | **카피가 너무 안전함. 더 도발적 방향 필요** |
| ★☆☆☆☆ | 댓글 자체가 적음 | 카피가 감정을 못 건드림 |

> **역설적 원칙**: 논쟁도 ★★☆ 이하인 영상의 카피 패턴은 다음 에피소드에서 **회피**하는 것이 좋다. 모두가 동의하는 제목은 클릭 유도력이 약하다는 증거.

**뽑아야 하는 기존 시그널 (유지):**

| 시그널 | 설명 | 활용 |
|--------|------|------|
| **감정 반응** | "scary", "amazing" 등 강한 감정 댓글 | 어떤 앵글이 감정을 건드리는지 확인 |
| **요약 시도** | 시청자가 직접 takeaway를 정리한 댓글 | actionable takeaway 갈증 = 썸네일에서 "답이 있다"는 약속 필요 |
| **논쟁/반박** | 찬반이 갈리는 댓글 | 해당 키워드를 제목에 넣으면 댓글 활성화 → 알고리즘 부스트 |
| **반복 피로** | "같은 얘기 반복" 류의 댓글 | 이전 영상과 다른 프레임/앵글 필수 |
| **클릭베이트 비난** | "clickbait" 댓글 | 구체적 사실 기반 카피로 방어 |
| **시스템 비판 공감** | 교육/사회 비판에 동의하는 댓글 | 해당 앵글 강화 |
| **계층/권력 반응** | 억만장자/빅테크 비판 에너지 | 대비 구조 활용 |

---

### Step 2: 트렌드 인텔리전스 (3-Layer Scan) + 경쟁 채널 카피 분석

**Layer 1 — 업계 버즈:** 게스트 산업의 최근 1-2주 뉴스, 관련 검색량 추이
**Layer 2 — YouTube 검색 수요:** 실제 사람들이 검색하는 키워드 (vidIQ/TubeBuddy)
**Layer 3 — 경쟁 채널 갭:** YC/DOAC/Lenny's가 안 다루는 주제 = 기회

**Layer 4 — 경쟁 채널 카피 패턴 분석:**

| 채널 | 참고 포인트 |
|------|----------|
| **DOAC** | 감정 트리거 단어 ("EMERGENCY"). 단, 1,400만 구독자 신뢰 기반 — EO에 그대로 적용 불가 |
| **Lex Fridman** | 주제 키워드 명확 표기 ("AGI", "SCALING LAWS"). 정보 밀도 높음 |
| **Impact Theory** | 구체적 숫자 + 경고 ("PHASE 5 OF COLLAPSE", "26 WAYS"). 가짜 정밀도 = 권위감 |
| **Ali Abdaal** | 숫자 + 변환 약속 ("4 BOOKS", "FINANCIALLY FREE"). 짧고 실용적 |
| **Colin & Samir** | 게스트 중심. 인지도 높은 이름이 훅 |

**EO 적용 원칙:**
- Impact Theory/Lex 스타일의 **구체적 사실/숫자 + 키워드** 조합이 EO에 가장 적합
- DOAC 스타일의 **모호한 감정 트리거**는 EO 규모에서는 효과 약함
- 썸네일 카피에 **영상 주제 키워드** 반드시 포함

**Layer 5 — 실시간 트렌드 매칭 (v5 신규):**

> 게시 직전 1-3일 이내의 업계 빅뉴스가 영상 주제와 겹치면, 제목에서 시의성을 직접 활용.

**적용 예시 (Thinking Mode EP1):**
- Cursor Cloud Agents 발표 (게시 2일 전) → "20 AI Agents" 키워드를 제목 후보에 활용
- "multi-agent", "vibe coding" 등 트렌딩 키워드를 썸네일/제목에 자연스럽게 삽입
- 단, 트렌드 키워드는 영상 내용과 실제로 연결될 때만 사용 (억지 삽입 금지)

**트렌딩 키워드 레퍼런스 (2026년 2월 기준, 주기적 업데이트 필요):**

| 키워드 | 바이럴 강도 | 맥락 |
|--------|:---:|------|
| **vibe coding** | ★★★★★ | Collins 올해의 단어 2025. Pichai vs Vembu 논쟁 폭발. "vibe coding kills open source" 해커뉴스. 가장 대중적 |
| **AI agents / coding agents** | ★★★★★ | Cursor Cloud Agents, GitHub Agent HQ, Claude Code Swarms. 개발자 사이 가장 핫한 주제 |
| **multi-agent / swarm** | ★★★★☆ | Gartner 문의 1,445% 급증. Claude Code Swarms HN 281pt. Cursor 20 에이전트 병렬 |
| **Software Engineer 3.0** | ★★★★☆ | EO가 만든 프레이밍. A/B WTS 38%. 자기투영 최강 |
| **agentic coding / engineering** | ★★★☆☆ | Anthropic 리포트 제목. 업계/기업 레벨에서 많이 쓰임. 대중 인지도는 아직 낮음 |
| **MCP (Model Context Protocol)** | ★★★☆☆ | 1,000+ 커뮤니티 서버. 개발자 사이에서 급성장. 비개발자에겐 생소 |
| **AI writes 30% of code** | ★★★☆☆ | Microsoft/Google CEO 발언. 충격적 수치로 대중 기사에 자주 인용 |
| **AI-native** | ★★☆☆☆ | Xebia "2026 = AI Native Year". 범용적이지만 그 자체로 바이럴은 아님 |

> **활용 원칙:** 바이럴 강도 ★★★★ 이상인 키워드가 영상 내용과 겹치면 적극 사용. ★★★ 이하는 맥락이 정확히 맞을 때만.

---

### Step 3: 콘셉트 개발 (Title + Thumbnail = 1 Unit)

제목과 썸네일을 **동시에** 하나의 콘셉트 카드로 설계.

| 카테고리 | 개수 | 설명 |
|---------|:---:|------|
| 검증 콘셉트 | 3-4개 | EO에서 성과 검증된 패턴 |
| 최적화 콘셉트 | 3-4개 | 데이터상 최고 조합, 아직 안 써본 것 |
| 실험 콘셉트 | 2-3개 | 새 앵글, 실패 가능하지만 성공 시 새 패턴 |

#### 썸네일 카피 9원칙 (v5 업데이트)

**기본 3원칙 (v3):**
1. 제목과 **다른 레이어** (요약 금지)
2. **통념 뒤집기** or **인사이트 암시**
3. **시청자 참여** (질문, 도발, 자기 투영)

**v4 추가 원칙:**
4. **구체성 필수** — 모호한 감정 태그 절대 금지
5. **영상 주제 키워드 포함** — 영상의 핵심 주제어가 반드시 들어가야 함
6. **영상 전체 내용과 일치** — 30초짜리 소재를 전체 콘셉트로 확대 금지
7. **자기투영 가능해야 함** — 시청자가 "나한테 해당되나?"로 연결될 수 있는 카피

**v5 추가 원칙 (Thinking Mode EP1 A/B 2회에서 학습):**
8. **정보 밀도 높을수록 좋다** — 썸네일 안에 여러 시각 요소(텍스트 + 그래프 + 태그 + 부제)가 서로 보강하면 시선 체류시간이 늘어남. "Software Engineer 3.0" + Top 1% 그래프 + CS146S 태그가 동시에 작동한 사례 (WTS 38% → 2차 62.7%)
9. **타겟 범위를 넓히는 단어 선택** — 특정 레벨/직급을 한정하는 단어("Junior Dev")보다 전체 직군을 포괄하는 단어("Software Engineer")가 더 넓은 오디언스를 잡음
10. **새로운 정체성/프레임워크 제안 > 실수 지적 (v5 2차 테스트)** — "Software Engineer 3.0"(정체성 제안, 62.7%)이 "More Agents ≠ Better Code" + "The Mistake 90% Make"(실수 지적, 37.3%)를 압도. 시청자는 **뭐가 될 수 있는지**(aspirational)를 보려고 클릭하지, **뭘 잘못하고 있는지**(guilt)를 보려고 클릭하지 않음

#### 썸네일 카피 금지사항

| 금지 유형 | 예시 | 왜 안 되나 |
|----------|------|----------|
| **모호한 감정 태그** | "YOUR JOB IS NEXT", "GOOD LUCK" | 어떤 AI 영상에나 붙일 수 있음. 이 영상만의 고유한 약속이 없음 |
| **스테레오타입** | "PHONES MAKE KIDS DUMBER" | 진부하고 예상 가능. 호기심 유발 실패 |
| **맥락 없는 짧은 문구** | "NOT FOR DANCING", "ROBOTS HAVE NO EYES" | 무슨 말인지 바로 이해 안 됨. 모바일에서 1초 안에 읽혀야 함 |
| **영상 주제와 무관** | 30초 분량 소재를 메인 카피로 | 기대 불일치 → 시청 이탈 → 알고리즘 페널티 |
| **HR/업계 전문 톤** | "HOW TO FIND THE BEST TALENT" | 대중 시청자가 자기 문제로 못 느낌 |
| **타겟 한정 라벨 (v5 추가)** | "Junior Dev:", "For Beginners" | 해당 안 되는 시청자가 이탈. A/B 테스트에서 "Junior Dev: Are We Cooked?"(32.1%) < "Software Engineer 3.0"(38%) |
| **업계 전문 용어 썸네일 (v5 추가)** | "Agentic Engineering 101" | 아직 대중적이지 않은 용어는 이해 장벽. A/B 테스트에서 29.9%로 최하위 |
| **소모된 YouTube 공식 (v5 2차)** | "The Mistake X% Make With Y" | 너무 많이 쓰인 템플릿. 신선함 없음. 2차 A/B에서 37.3%로 패배 |
| **실수 지적형 썸네일 (v5 2차)** | "More Agents ≠ Better Code" | 주장/사실은 "아 그렇구나"로 끝남. 새로운 정체성 제안("3.0")이 62.7%로 압도 |

#### 좋은 썸네일 카피의 조건 (v5 업데이트)

| 조건 | 설명 | 좋은 예시 |
|------|------|----------|
| **자기투영** | 시청자가 "나한테 해당되나?" | "Software Engineer 3.0" ("나는 몇 점대지?") |
| **구체적 답 약속** | 단수형("one thing", "trait")으로 답이 있다는 시그널 | "The One Human Edge That Only Grows Sharper After AI" |
| **영상 키워드** | AI/AGI/engineering/future 등 | "Software Engineer 3.0" |
| **적절한 길이** | 5-12단어. 너무 짧으면 맥락 부족, 너무 길면 안 읽힘 | 2-3단어 ✗ / 5-10단어 ✓ / 15단어+ ✗ |
| **제목과 다른 스케일** | 썸네일 = WHAT/WHERE, 제목 = WHY/HOW | 썸네일: 3.0이라는 목적지. 제목: 왜 지금 변해야 하는지 |
| **버전 넘버링 (v5 추가)** | X.0 형식이 자기투영 + 진화 프레임을 동시에 작동시킴 | "Software Engineer 3.0" (WTS 38% → 2차 62.7%) |
| **구체적 콘셉트 + 부분 공개 (v5 추가)** | 영상 본문의 핵심 개념을 구체적으로 제시하되 다 설명하지 않음 | "RURAL / URBAN" (Po-Shen Loh 우승, 35.4%) |
| **새로운 정체성 제안 (v5 2차)** | 이 영상 전에 존재하지 않던 프레임워크/라벨을 만들어 제안. "뭐가 될 수 있는지" aspirational pull | "Software Engineer 3.0" (62.7% vs "Mistake" 37.3%) |

#### 제목 작성 원칙 (v5 업데이트)

| 원칙 | 설명 |
|------|------|
| **썸네일과 같은 영상처럼 읽혀야 함** | 썸네일이 "3.0"인데 제목이 완전 다른 주제면 불일치 |
| **em dash(—) 사용 금지** | 콤마 또는 마침표로 대체 |
| **약어 금지** | CMU ✗ → Carnegie Mellon 또는 풀어쓰기 |
| **현재 직함만** | 과거 직함 쓰지 않기 |
| **인트로와 연결** | 인트로 내러티브와 제목의 방향이 일치해야 시청 지속시간 유지 |
| **한 문장 원칙** | 제목은 가급적 한 문장으로. 문장이 두 개면 짧은 문장끼리 조합 |
| **100자 제한 (v5 추가)** | YouTube 제목은 **최대 100자**. 파이프(\|) + 게스트명/소속 포함해서 100자 이내. 80자 이내가 이상적 — 모바일에서 잘리지 않음 |
| **"From X to Y" 변환형 우선 (v5 추가)** | "How to" 튜토리얼보다 변환 내러티브가 클릭률이 높음. "From Writing Code to Managing Agents" > "How to Manage AI Agents" (38% vs 29.9%) |
| **직접 도발 > 중립 관찰 (v5 추가)** | "Most Engineers Aren't Ready"(도발) > "What the Top 1% Do Differently"(관찰). 시청자를 직접 겨냥하는 톤이 더 강한 클릭 유발 |
| **파이프 뒤 기관명 중복 방지 (v5 추가)** | 썸네일에 "Stanford" 이미 있으면 제목 파이프 뒤에서 "Stanford University" 생략 가능. 글자수 절약 |

#### 제목-썸네일 세트 호환성 체크 (v5 업데이트)

콘셉트 카드 완성 후 아래 체크리스트로 검증:

```
□ 썸네일과 제목이 같은 영상의 이야기처럼 읽히는가?
□ 썸네일과 제목이 서로 다른 레이어를 담당하는가? (같은 말 반복 ✗)
□ 썸네일만 보고도 클릭 이유가 있는가? (모바일 = 썸네일 먼저 보임)
□ 제목만 읽어도 영상 방향이 잡히는가?
□ 영상 전체 내용의 핵심 주제와 일치하는가? (일부 소재 확대 ✗)
□ 인트로 내러티브와 방향이 맞는가?
□ 시청자가 자기 문제로 느낄 수 있는가?
□ 이전 영상과 차별화되는가? (같은 게스트 재출연 시)
□ 타겟이 특정 레벨/직급으로 한정되지 않는가? (v5 추가)
□ 썸네일 정보 밀도가 충분한가? (텍스트 + 시각 요소 보강) (v5 추가)
```

#### 검증된 패턴 (v5 업데이트 — 2개 영상, A/B 3회 결과)

| 패턴 | 예시 | 성과 | 등급 |
|------|------|:---:|:---:|
| **새로운 정체성 + 버전 넘버링 + 변환 내러티브 + 직접 도발** | 썸네일 "Software Engineer 3.0" + 제목 "From Writing Code to Managing Agents. Most Engineers Aren't Ready" | CTR 6.0%, 1차 WTS 38%, 2차 WTS 62.7% | **최고신뢰 ★★★★★+** |
| **구체적 콘셉트 + 부분 공개 (대비형)** | 썸네일 "RURAL / URBAN" + 제목 "AI Will Create New Wealth, But Not Where You Think" | WTS 35.4% | **고신뢰 ★★★★★** |
| **자기투영 + AI 키워드 + trait/edge 단수형** | 썸네일 "The Rarest Human Trait After AI" + 제목 "The One Human Edge That Only Grows Sharper After AI" | CTR 6.0~7.3% | **고신뢰 ★★★★☆** |
| **역설 구조 (AI↑ = Human Edge↑)** | "The One Human Edge That Only Grows Sharper After AI" | CTR 6.0~7.3% | **고신뢰 ★★★★☆** |
| **숫자 + 위기 + Top X% 반전** | 썸네일 "Junior Dev: Are We Cooked?" + 제목 "3 Forces Killing Software Careers. What the Top 1% Do Differently" | CTR 6.0%, WTS 32.1% | **보통 ★★★☆☆** |

**v5 핵심 발견: Aspirational Identity > Guilt Callout**

> "Software Engineer 3.0"(새로운 정체성 제안)이 "More Agents ≠ Better Code" + "The Mistake 90% Make"(실수 지적)를 62.7% vs 37.3%으로 압도.
> 시청자는 **뭐가 될 수 있는지**(pull)를 보려고 클릭하지, **뭘 잘못하고 있는지**(push)를 보려고 클릭하지 않는다.
> 새로운 프레임워크/라벨 창조가 기존 YouTube 공식("The Mistake X% Make")보다 강력하다.

#### 회피 패턴 (v5 업데이트)

| 패턴 | 예시 | 성과/문제 |
|------|------|------|
| **업계 전문 용어 + 101/가이드 톤** | "Agentic Engineering 101" + "How to Manage Multiple AI Agents Like a Top 1% Engineer" | WTS 29.9% — 3세트 중 최하위. 전문 용어 + 튜토리얼 톤 = 범용성 부족 |
| **타겟 한정 라벨** | "Junior Dev: Are We Cooked?" | WTS 32.1% — "Junior"가 시니어/리드를 이탈시킴 |
| **"How to" 튜토리얼 프레임** | "How to Manage Multiple AI Agents Like a Top 1% Engineer" | 같은 콘셉트에서 "From X to Y" 변환형(38%)에 완패(29.9%) |
| **중립 관찰 톤** | "What the Top 1% Do Differently" | 같은 콘셉트에서 "Most Engineers Aren't Ready" 도발형(38%)에 밀림(32.1%) |
| **소모된 YouTube 공식 (v5 2차)** | "The Mistake 90% of Engineers Make With~" | 2차 A/B WTS 37.3%. 너무 많이 쓰인 템플릿 = 신선함 없음. 새로운 개념 창조("3.0")에 압도당함 |
| **실수 지적(Guilt) 프레임 (v5 2차)** | 썸네일 "More Agents ≠ Better Code" + 제목 "The Mistake 90%~" | 주장/사실 전달은 "아 그렇구나"로 끝남. 정체성 제안(aspirational)이 62.7%로 압도 |
| 모호한 2-3단어 감정 태그 | "YOUR JOB IS NEXT" | 구체성 없음, 어떤 AI 영상에나 붙일 수 있음 |
| 맥락 없는 짧은 문구 | "NOT FOR DANCING" | 무슨 말인지 모름 |
| 영상 일부 소재로 전체 콘셉트 | 30초 분량 소재 → 메인 카피 | 기대 불일치 |
| HR/전문가 톤 | "How to Find the Best Talent" | 시청자 자기투영 불가 |
| 썸네일-제목 주제 불일치 | 썸네일: Talent / 제목: Future | 두 개의 다른 영상처럼 보임 |

---

### Step 4: CTR 예측 + 근거 매칭

점수 + **유사 EO 영상 성과** + **신뢰도 등급**:

```
콘셉트 A: "3.0 변환형" — 예측 CTR 6.26%

  Base:                    3.11%
  + Contrarian:           +1.17%  ← "코드를 쓰는 게 아니라 관리한다"
  + Transformation:       +0.50%  ← "From X to Y" 구조 (v5 신규)
  + Direct challenge:     +0.30%  ← "Aren't Ready" 도발 (v5 신규)
  + Self-projection:      +0.30%  ← 버전 넘버링 자기투영
  + Version numbering:    +0.30%  ← "3.0" (v5 신규)
  + Person pipe:          +0.57%
  ──────────────────────────────
  TOTAL:                   6.26%

  근거: Thinking Mode EP1 실제 CTR 6.0% → 모델 정확도 높음
  신뢰도: ★★★★★
```

**v5 추가 스코어링 보너스:**
```
+ Transformation:        +0.50%  ← "From X to Y" 변환 내러티브
                                   근거: Thinking Mode EP1 WTS 38% (vs "How to" 29.9%)

+ Direct challenge:      +0.30%  ← "Aren't Ready", "No One Taught You This" 등 직접 도발
                                   근거: Thinking Mode EP1 "Aren't Ready"(38%) > "Do Differently"(32.1%)

+ Version numbering:     +0.30%  ← "3.0", "2.0" 등 버전 넘버링
                                   근거: Thinking Mode EP1 "Software Engineer 3.0" WTS 38%

+ Concept partial reveal: +0.30% ← 구체적 콘셉트를 보여주되 다 설명하지 않는 구조
                                   근거: Intelligence EP1 "RURAL / URBAN" WTS 35.4%

+ Novel identity:        +0.50%  ← 이 영상 전에 존재하지 않던 새로운 정체성/프레임워크 제안
                                   근거: Thinking Mode EP1 2차 A/B "Software Engineer 3.0" 62.7%
                                   (vs "The Mistake 90% Make" 37.3%)
```

**v5.1 댓글 기반 보너스 (Comment Intelligence에서 도출):**
```
+ Identity threat:       +0.30%  ← 특정 집단의 자격/정체성을 직접 건드리는 제목
                                   근거: Mihail "Most Engineers Aren't Ready" → "Since when do
                                   journalists train engineers?" (자격 도전 댓글 = 클릭한 증거)
                                   Carina "24-Year-Old + $64M" → "ponzi scheme" 304 likes, 14 replies

+ Cognitive dissonance:  +0.25%  ← 이해가 안 되는 숫자 조합 또는 상식 파괴 주장
                                   근거: Carina "I still don't understand how they got $64M" 123 likes
                                   시청자가 "이해하려고" 클릭하는 패턴

+ Debate axis present:   +0.20%  ← 제목이 명확한 찬반 논쟁 축을 형성할 수 있는 구조
                                   근거: 논쟁도 ★★★★★ 영상이 engagement 최상위
                                   Po-Shen "unplug AI" 17 replies, Carina "ponzi" 14 replies
```

**v5 감점 요소:**
```
- Jargon penalty:        -0.30%  ← 대중적이지 않은 전문 용어 ("Agentic Engineering" 등)
                                   근거: Thinking Mode EP1 "Agentic Engineering 101" WTS 29.9% (최하위)

- Target limiter:        -0.20%  ← 특정 직급/레벨로 타겟 한정 ("Junior Dev", "For Beginners")
                                   근거: "Junior Dev"(32.1%) < "Software Engineer"(38%)

- Tutorial framing:      -0.15%  ← "How to" / "101" / "Guide" 튜토리얼 톤
                                   근거: "How to Manage"(29.9%) < "From X to Y"(38%)

- Overused formula:      -0.30%  ← "The Mistake X% Make", "X Things You're Doing Wrong" 등
                                   소모된 YouTube 공식
                                   근거: 2차 A/B "The Mistake 90%"(37.3%) 완패

- Guilt framing:         -0.20%  ← "You're doing it wrong" 실수 지적 프레임
                                   근거: 2차 A/B 실수 지적(37.3%) < 정체성 제안(62.7%)
```

**전체 스코어링 모델 (v5):**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CTR Scoring Model v5
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Base:                      3.11%

가산 요소:
+ Contrarian:             +1.17%   (통념 뒤집기)
+ X in Y time:            +1.17%   (기간 내 성과)
+ User count:             +1.05%   (유저/지원자 수)
+ Superlative:            +0.81%   (최초/유일/가장)
+ Dollar:                 +0.65%   (달러 수치)
+ Age:                    +0.58%   (나이)
+ Person+Company pipe:    +0.57%   (게스트 | 소속)
+ 15-18 words:            +0.50%   (제목 길이)
+ Transformation:         +0.50%   (From X to Y 변환)     ← v5 신규
+ How I:                  +0.45%   (How I~)
+ Percentage:             +0.35%   (퍼센트)
+ Self-projection:        +0.30%   (자기투영 트리거)
+ Direct challenge:       +0.30%   (직접 도발)            ← v5 신규
+ Version numbering:      +0.30%   (X.0 버전 넘버링)      ← v5 신규
+ Concept partial reveal: +0.30%   (구체적 콘셉트 부분 공개) ← v5 신규
+ + Novel identity:         +0.50%   (새로운 정체성/프레임워크 제안)  ← v5 2차
+ Identity threat:        +0.30%   (타겟 집단 자격/정체성 건드림)  ← v5.1 댓글 기반
+ Cognitive dissonance:   +0.25%   (이해 불가 숫자/상식 파괴)     ← v5.1 댓글 기반
+ Debate axis present:    +0.20%   (명확한 찬반 논쟁 축 형성)     ← v5.1 댓글 기반
+ Trigger USE:            +0.15%   (how, built, raised, startup, founder)

감산 요소:
- Jargon penalty:         -0.30%   (대중 미인지 전문 용어)  ← v5 신규
- Overused formula:       -0.30%   (소모된 YouTube 공식)   ← v5 2차
- Target limiter:         -0.20%   (타겟 한정 라벨)        ← v5 신규
- Guilt framing:          -0.20%   (실수 지적 프레임)      ← v5 2차
- Tutorial framing:       -0.15%   (How to / 101 / Guide)  ← v5 신규
- Spam-attracting generic:-0.15%   (너무 범용적인 성공/부자 키워드 → 봇 유입)  ← v5.1
- Trigger AVOID:          -0.15%   (entrepreneur, lessons, ceo, advice)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### Step 5: A/B 테스트 세팅 (3세트) + 게시 (v5 업데이트)

**v5 핵심 변경: YouTube A/B 테스트를 3세트로 운영**

> Thinking Mode EP1에서 YouTube 내장 A/B 테스트를 3세트로 돌려 직접 Watch Time Share 데이터를 확보. 이 방식이 감으로 1순위를 고르는 것보다 압도적으로 효과적.

**게시 체크리스트:**
- [ ] **3개 콘셉트 세트** 각각 썸네일 + 제목 완성
- [ ] YouTube Studio A/B 테스트 세팅 (Title and Thumbnail 모드)
- [ ] 3세트의 앵글을 충분히 다르게 (같은 콘셉트 미세 변형 ✗ → 아예 다른 프레임 ✓)
- [ ] 게시 시간: EO 채널 최적 시간대

**3세트 구성 전략 (v5 신규):**

| 세트 | 역할 | 예시 (Thinking Mode EP1) |
|------|------|----------|
| **세트 A** | 검증 패턴 적용 | "Software Engineer 3.0" + "From X to Y" (변환 + 도발) |
| **세트 B** | 감정/밈 앵글 | "Junior Dev: Are We Cooked?" (위기감 + 공감) |
| **세트 C** | 정보/가이드 앵글 | "Agentic Engineering 101" + "How to" (튜토리얼) |

> **3세트는 반드시 서로 다른 프레임**이어야 함. 미세 변형(같은 제목, 다른 썸네일)은 인사이트가 약함. 프레임 자체를 바꿔야 어떤 앵글이 먹히는지 배움.

---

### Step 6: 실시간 모니터링 + 적극 교체

> **EO 운영 원칙:** A/B 테스트가 자동으로 우승 세트를 선택. CTR 5% 이하면 수동 교체.

#### 모니터링 타임라인

```
H+0  게시 + A/B 테스트 시작
│
H+2  ── 1차 체크: A/B 테스트 중간 수치 확인
│        └─ 아직 데이터 부족. 관찰만
│
H+4  ── 2차 체크
│        └─ Watch Time Share 트렌드 확인
│        └─ 전체 CTR < 3% → A/B 테스트 외 4순위 세트로 수동 교체
│
H+8  ── 3차 체크
│        └─ A/B 테스트 우승 세트 윤곽이 보이기 시작
│        └─ 전체 CTR < 5% → 수동 교체 고려
│
H+12 ── 4차 체크
│        └─ A/B 테스트 결과 거의 확정
│        └─ 우승 세트 "Set this option" 적용
│
H+24 ── 24시간 판단
│        └─ CTR < 5% → 마지막 교체 시도
│        └─ CTR ≥ 5% → 확정
│
H+48 ── 48시간 확정
         └─ 최종 CTR 기록. 이후 교체 안 함
```

#### 교체 판단 매트릭스

| 시점 | CTR < 3% | CTR 3~5% | CTR ≥ 5% |
|:---:|:---:|:---:|:---:|
| **H+2** | 관찰 (A/B 진행 중) | 관찰 | 유지 |
| **H+4** | 수동 교체 고려 | A/B 결과 대기 | 유지 |
| **H+8** | 수동 교체 | A/B 우승 세트 적용 | 유지 |
| **H+12** | 교체 | A/B 우승 세트 적용 | 유지 |
| **H+24** | 마지막 교체 | 마지막 교체 | 확정 |
| **H+48** | 기록. 원인 분석 | 기록 | 기록. 패턴 등록 |

---

### Step 7: 피드백 루프 (패턴 풀 업데이트)

#### 영상별 최종 기록 (v5 업데이트)

| 필드 | 설명 |
|------|------|
| 게시일 | yyyy-mm-dd |
| 최종 제목 | (A/B 우승 또는 교체 후 확정 제목) |
| A/B 테스트 세트 | 세트 A/B/C 각각의 제목 + 썸네일 + WTS |
| 최종 패턴 | (예: Transformation + Direct challenge + Version numbering) |
| 썸네일 카피 | (최종 썸네일 카피) |
| 썸네일 앵글 | (자기투영형 / 도발형 / 변환형 / 대비형 / 질문형) |
| 예측 CTR | ?% |
| H+2 CTR | ?% |
| H+8 CTR | ?% |
| H+24 CTR | ?% |
| H+48 CTR | ?% |
| 7일 CTR | ? |
| 30일 CTR | ? |
| 30일 노출 | ? |
| 30일 조회수 | ? |
| 평균 시청 지속시간 | ? |
| Browse features % | ? (v5 추가) |
| Suggested videos % | ? (v5 추가) |
| Content suggesting this video | 상위 5개 (v5 추가) |
| A/B 학습 메모 | (어떤 프레임이 이겼고, 왜) |

#### 패턴 풀 업데이트 기준

| 조건 | 액션 |
|------|------|
| A/B WTS ≥ 35% + CTR ≥ 5% | **고신뢰 패턴** 등록 |
| A/B WTS 30-35% | 보통 패턴. 추가 데이터 필요 |
| A/B WTS < 30% | **회피 패턴** 등록 |
| H+24 CTR ≥ 5% (교체 없이) | **고신뢰 패턴** 등록 |
| H+24 CTR < 3% (교체 다 해도) | **회피 패턴** 등록 |

---

## 검증 사례

### Case 1: Intelligence EP1 (Po-Shen Loh)

**A/B 우승 세트 (v5 보정):**
- 썸네일: "RURAL / URBAN"
- 제목: "AI Will Create New Wealth, But Not Where You Think | Carnegie Mellon University, Po-Shen Loh"
- Watch Time Share: **35.4%**

**게시 세트 (A/B 후 교체 없음):**
- 썸네일: "The Rarest Human Trait After AI"
- 제목: "The One Human Edge That Only Grows Sharper After AI | Carnegie Mellon University, Po-Shen Loh"
- CTR: 6.0% (H+9: 7.3%), 노출 88.6K, 조회수 7.7K

**핵심 학습:**
1. "RURAL / URBAN" — 구체적 콘셉트 + 부분 공개. 영상 본문의 핵심 대비를 2단어로 압축
2. "But Not Where You Think" — 통념 뒤집기 + 궁금증 유발
3. **구체적일수록, 다 알려주지 않을수록 클릭률이 높다** — 이 원칙이 v5의 핵심

---

### Case 2: Thinking Mode EP1 (Mihail Eric)

**A/B 테스트 결과:**

| 세트 | 썸네일 | 제목 | WTS |
|------|--------|------|:---:|
| A | Agentic Engineering 101 | How to Manage Multiple AI Agents Like a Top 1% Engineer | 29.9% |
| B | Junior Dev: Are We Cooked? | 3 Forces Killing Software Careers. What the Top 1% Do Differently | 32.1% |
| **C** | **Software Engineer 3.0** | **From Writing Code to Managing Agents. Most Engineers Aren't Ready** | **38.0%** |

**최종 성과 (Set C):**
- CTR: 6.0%, 노출 91.3K, 조회수 8.3K (+3.4K), 시청시간 568.7h (+338.7)
- Browse features: 70.7%, Suggested: 14.0%
- 구독자: +58

**A/B 2차 테스트 (우승 확인전):**

| 세트 | 썸네일 | 제목 | WTS |
|------|--------|------|:---:|
| **A (우승)** | **Software Engineer 3.0** | **From Writing Code to Managing Agents. Most Engineers Aren't Ready** | **62.7%** |
| B | More Agents ≠ Better Code | The Mistake 90% of Engineers Make With AI Coding Agents | 37.3% |

**핵심 학습 (1차 + 2차 종합):**
1. **"From X to Y" 변환형 > "How to" 튜토리얼형** — 38% vs 29.9%. 방향을 보여주되 방법은 영상에서
2. **직접 도발("Aren't Ready") > 중립 관찰("Do Differently")** — 시청자를 겨냥해야 클릭
3. **버전 넘버링("3.0")이 최강 자기투영 트리거** — 모든 레벨의 엔지니어가 "나는 몇 점대?" 자문
4. **넓은 타겟("Software Engineer") > 좁은 타겟("Junior Dev")** — Browse 70.7%의 원동력
5. **썸네일 정보 밀도가 높을수록 좋다** — 3.0 + Top 1% + CS146S + Stanford = 시선 체류시간↑
6. **전문 용어 썸네일은 안 먹힌다** — "Agentic Engineering" 최하위. 대중이 모르면 스킵
7. **새로운 정체성 제안(aspirational) >> 실수 지적(guilt)** — 62.7% vs 37.3%. 시청자는 "뭐가 될 수 있는지"를 보려고 클릭하지, "뭘 잘못하는지" 보려고 클릭하지 않음 (2차 테스트)
8. **새로운 개념 창조 >> 소모된 YouTube 공식** — "Software Engineer 3.0"(이 영상 전에 없던 개념)이 "The Mistake X% Make"(흔한 공식)를 압도 (2차 테스트)

---

## 실행 타임라인 (v5)

```
D-14 ── [PD/에디터] Step 0: 게스트 정보로 콘셉트 스케치
D-7  ── [에디터] 인터뷰 질문에 훅 끌어낼 질문 추가
D-Day── [호스트] 훅 답변 나오면 깊이 파기
D+3~5── [PD] Step 1 + 1.5 + 2: 스크립트 + 이전 댓글 + 트렌드 + 경쟁채널 카피
D+5~6── [PD] Step 3+4: 콘셉트 10개 생성 + 스코어링 + 호환성 체크
D+6~7── [PD] Top 3 선택 → [디자이너] 썸네일 3개 제작 (A/B용)
D+7  ── [PD] Step 5: A/B 테스트 3세트 세팅 + 게시

         ┌─ H+2: A/B 중간 확인 (관찰만)
D+7~8 ──│─ H+4: 전체 CTR 확인. <3% → 수동 교체
  (24h)  │─ H+8: A/B 우승 윤곽. <5% → 교체 고려
         │─ H+12: A/B 확정. 우승 세트 적용
         └─ H+24: <5% → 마지막 교체. ≥5% → 확정

D+9  ── H+48: 최종 기록
D+14 ── 7일 CTR 기록
D+37 ── 30일 CTR + Step 7: 패턴 풀 업데이트 + A/B 학습 기록
```

---

## Claude 입력 포맷

### Step 1 + 1.5 + 2 (훅 추출 + 댓글 + 트렌드):
```
"이 스크립트로 EO 카피 워크플로우 돌려줘"
+ 스크립트 전문
+ 게스트: [이름], [회사], 유명도: [대중적/업계/무명]
+ 이전 영상 댓글: [붙여넣기]
```

### Step 3+4 (콘셉트 + 스코어링):
```
"콘셉트 10개 + CTR 스코어링해줘"
(Step 1-2에 이어서 자동)
+ 추가 요청: "감정형 위주" / "VC 타겟" / "일반 대중 타겟" 등
+ 반드시 호환성 체크 포함
+ A/B 테스트용 3세트 추천 포함 (v5)
```

### Step 6 A/B 결과 분석:
```
"A/B 테스트 결과야. 분석해줘"
+ 세트별 Watch Time Share
+ 현재 CTR, 노출, 조회수
+ Content suggesting this video 리스트
```

### Step 7 분기 업데이트:
```
"지난 3개월 데이터로 모델 업데이트해줘"
+ YouTube Studio CSV (3개월)
+ A/B 테스트 결과 모음
+ 교체 로그
```

---

## 프롬프트 템플릿 (v5)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EO 카피 생성 요청 템플릿 (v5)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

■ 게스트 정보
이름:
회사:
현재 직함:
유명도: [대중적 유명 / 업계 유명 / 무명]

■ 핵심 훅 (아는 만큼)
가장 큰 성과:
반직관적 사실:
감정적 스토리:
핵심 숫자:

■ 스크립트
(여기에 전문 또는 요약 붙여넣기)

■ 이전 영상 댓글 (있으면)
(같은 게스트 이전 영상 또는 비슷한 주제 영상의 댓글 붙여넣기)

■ 요청
위 정보로 EO Global 유튜브 제목+썸네일 콘셉트 10개 만들어줘.
그중 A/B 테스트용 3세트도 추천해줘.

규칙:
- 무명 기업/게스트 이름은 제목 메인에 넣지 마. 파이프(|) 뒤에만
- 전문용어/업계 용어/약어 제목에 넣지 마
- 썸네일은 제목을 요약하지 말고, 다른 레이어로
- 썸네일 카피는 5-12단어, 구체적 주장/사실 + 영상 주제 키워드 필수
- 모호한 감정 태그 금지 ("YOUR JOB IS NEXT" 류)
- 제목에 em dash(—) 쓰지 마
- 제목은 파이프+게스트명 포함 100자 이내 (80자 이내 이상적)
- "How to" 튜토리얼보다 "From X to Y" 변환형 우선
- 제목에 직접 도발 톤 포함 ("Aren't Ready", "No One Taught You This" 등)
- 새로운 정체성/프레임워크 제안 > 실수 지적 ("Software Engineer 3.0" >> "The Mistake X% Make")
- "The Mistake X% Make" 같은 소모된 YouTube 공식 쓰지 마
- 썸네일에 전문 용어 쓰지 마 (대중이 모르면 스킵됨)
- 타겟을 특정 직급으로 한정하지 마 ("Junior Dev" 같은 라벨 금지)
- 댓글 데이터가 있으면 논쟁 축 도출 + 시청자 생성 표현 활용
- 논쟁을 유발하는 카피 방향 최소 2개 포함 (모두가 좋아하는 안전한 카피 지양)
- 각 콘셉트에 CTR 예측 점수 매겨줘
- 세트별 호환성 체크
- A/B 3세트는 각각 다른 프레임으로

CTR 스코어링 모델 v5:
Base: 3.11%
Contrarian: +1.17% | X in Y time: +1.17%
User count: +1.05% | Superlative: +0.81%
Dollar: +0.65% | Age: +0.58%
Person+Company pipe: +0.57%
15-18 words: +0.50% | Transformation: +0.50%
How I: +0.45% | Percentage: +0.35%
Self-projection: +0.30% | Direct challenge: +0.30%
Version numbering: +0.30% | Concept partial reveal: +0.30%
Novel identity: +0.50%
Identity threat: +0.30% | Cognitive dissonance: +0.25%
Debate axis: +0.20%
Trigger USE: +0.15% (how, built, raised, startup, founder)
Jargon penalty: -0.30% | Overused formula: -0.30%
Target limiter: -0.20% | Guilt framing: -0.20%
Tutorial framing: -0.15% | Spam-attracting generic: -0.15%
Trigger AVOID: -0.15% (entrepreneur, lessons, ceo, advice)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## v5 → v5.1 변경 요약

| 항목 | v5 | v5.1 (댓글 분석 397개 반영) |
|------|------|------|
| **Step 1.5** | 시그널 7종 (이론적) | **Comment Intelligence 프레임워크로 확장**: 댓글 유형 5종 분류, 논쟁 축 도출법, Viewer-Generated Language 추출법, 논쟁도 점수(★) 시스템 — 4개 영상 실전 데이터로 검증 |
| **스코어링 가산** | 14개 요소 | **17개 요소** (+Identity threat +0.30%, +Cognitive dissonance +0.25%, +Debate axis +0.20%) |
| **스코어링 감산** | 6개 요소 | **7개 요소** (+Spam-attracting generic -0.15%) |
| **핵심 원칙 추가** | — | **"논쟁 유발하는 카피 > 모두가 좋아하는 카피"** — 긍정 댓글만 달리는 영상의 카피 패턴은 회피 대상 |
| **댓글 수집 방법** | "붙여넣기" 안내만 | **브라우저 자동 추출 + 수동 입력 2가지 방법 문서화** |
| **논쟁 축 분류** | 없음 | **5가지 논쟁 축 유형 + 제목 활용법** (자격 도전, 시스템 비판, 인간 본성, 과대평가 회의, 사실 검증) |
| **시청자 표현 추출** | 없음 | **Viewer-Generated Language 테이블 + Copy 활용 방향** 6개 예시 |
| **댓글 ↔ CTR 연결** | 없음 | **댓글에서 추출한 감정 패턴이 CTR 스코어링에 직접 반영** |

---

## v4 → v5 변경 요약

| 항목 | v4 | v5 (Thinking Mode EP1 A/B 결과 반영) |
|------|------|------|
| **Po-Shen Loh 우승 세트** | "Rarest Human Trait" (오기록) | **"RURAL / URBAN" + "AI Will Create New Wealth, But Not Where You Think" (WTS 35.4%)로 보정** |
| **A/B 테스트** | 1순위 게시 + 백업 교체 | **YouTube 내장 A/B 3세트 동시 테스트. 다른 프레임으로 구성** |
| **썸네일 원칙** | 7원칙 | **9원칙** (정보 밀도, 타겟 범위 추가) |
| **제목 원칙** | 7원칙 | **10원칙** ("From X to Y" 변환형 우선, 직접 도발 > 중립 관찰, 파이프 중복 방지 추가) |
| **검증 패턴** | 자기투영 + AI 키워드 위주 | **새로운 정체성 제안 + 버전 넘버링 + 변환 내러티브 + 직접 도발 (1차 WTS 38%, 2차 WTS 62.7%) 최고신뢰 등록** |
| **회피 패턴** | 모호한 태그 위주 | **전문 용어, 타겟 한정, "How to" 튜토리얼, 중립 관찰, 소모된 YouTube 공식, 실수 지적(Guilt) 프레임 추가** |
| **스코어링 모델** | 가산만 | **감산 요소 5개 추가** (Jargon -0.30%, Overused formula -0.30%, Target limiter -0.20%, Guilt framing -0.20%, Tutorial framing -0.15%) |
| **스코어링 가산** | Self-projection +0.30% | **Novel identity +0.50%, Transformation +0.50%, Direct challenge +0.30%, Version numbering +0.30%, Concept partial reveal +0.30% 추가** |
| **호환성 체크** | 8항목 | **10항목** (타겟 한정 여부, 정보 밀도 추가) |
| **모니터링 기록** | CTR + 교체 로그 | **Browse features %, Suggested %, Content suggesting 상위 5개, A/B WTS 기록 추가** |
| **패턴 판정 기준** | CTR 기준만 | **A/B WTS ≥ 35% + CTR ≥ 5% = 고신뢰** |
| **제목 글자수** | 규칙 없음 | **100자 제한 명시 (YouTube 제한). 80자 이내 이상적** |
| **트렌딩 키워드** | 없음 | **Layer 5에 트렌딩 키워드 레퍼런스 테이블 추가 (바이럴 강도 ★ 평가)** |
| **핵심 원칙 (2차 A/B)** | 없음 | **"새로운 정체성 제안 > 실수 지적" 원칙 확립. Aspirational pull > Guilt push** |
| **썸네일 원칙** | 9원칙 | **10원칙** (새로운 정체성/프레임워크 > 실수 지적 추가) |

---

*EO Global Copy Workflow v5.1 — February 27, 2026*
*Based on: 355-video dataset + Intelligence EP1 (Po-Shen Loh, CTR 6.0~7.3%) + Thinking Mode EP1 (Mihail Eric, CTR 6.0%, A/B 1차 WTS 38%, 2차 WTS 62.7%) + 3회 실전 A/B 테스트 학습 + 4개 영상 397개 댓글 분석 (Po-Shen Loh 447K, Mihail Eric 12K, Carina Hong/Axiom, Lucy Guo/Passes)*
