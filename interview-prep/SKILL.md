---
name: interview-prep
description: EO Global 인터뷰이 리서치 + 주제 잡기 + 질문지 작성. "인터뷰 준비", "interview prep", "게스트 조사", "질문지" 요청에 사용.
---

# Interview Prep

이 스킬이 호출되면 아래 절차를 따른다.

## 입력

사용자가 게스트 정보를 제공한다. 형태는 자유롭다:
- 이름 + 링크 (LinkedIn, 웹사이트 등)
- 이름만
- 링크만
- "이 사람 조사해줘" + 아는 정보

## 워크플로우

**반드시 `~/.claude/skills/references/eo_interview_research_workflow.md`를 먼저 읽고** 전체 프로세스를 따른다.

### Step 1: 입력 확인

사용자에게 아래 정보를 확인한다 (이미 제공된 것은 스킵):

```
■ 게스트 이름:
■ 링크: (아는 만큼)
■ 시리즈: (Thinking Mode / Before 25 / Intelligence / 기타)
■ 맥락: (왜 이 사람인지, 있으면)
```

시리즈를 모르면 물어본다. 나머지는 없어도 진행 가능.

### Step 2: Phase 1 + 2 실행 (리서치 + 주제 잡기)

워크플로우 파일의 Phase 1, Phase 2를 순서대로 실행한다.

**리서치 시 주의:**
- WebSearch + WebFetch를 병렬로 활용해 속도를 높인다
- LinkedIn은 직접 크롤링이 안 되므로 WebSearch로 우회한다
- 기존 인터뷰/팟캐스트를 최소 3개 이상 분석한다
- 해묵은 얘기 필터(Phase 2.2)를 엄격하게 적용한다

**Phase 2 완료 시 산출물:**
1. 게스트 프로필 요약
2. Hot Take 후보 (평가 점수 포함)
3. Theme + Title/Thumbnail + Lessons 옵션 2-3개

이 결과를 사용자에게 보여주고 **방향을 확정**받는다.

### Step 3: Phase 3 실행 (질문지 작성)

사용자가 방향을 확정하면 질문지를 작성한다.

워크플로우 파일의 Phase 3과 산출물 템플릿을 따른다.

## 출력

1. **파일 저장**: `~/Desktop/Cowork/interview_prep_{guest_name}_{date}.md` 에 저장
2. 저장 경로를 알려준다
3. 다음 단계를 안내한다:
   - "팀 리뷰 후 수정할 부분 있으면 알려주세요"
   - "촬영 후에는 Copy Workflow v5로 제목/썸네일 작업하면 됩니다"

## 규칙

- 인터뷰 언어는 **영어** (EO Global)
- 질문지 본문은 **영어**, 프로덕션 노트는 **한국어 가능**
- 해묵은 얘기 금지 — Phase 2.2 필터를 반드시 적용
- 게스트 고유 질문 우선 — 누구에게나 물을 수 있는 질문은 후순위
- Hot Take 3가지 조건 (Uniqueness × Reactivity × Timeliness) 충족 확인
- 파일 저장 시 전체 경로를 출력
