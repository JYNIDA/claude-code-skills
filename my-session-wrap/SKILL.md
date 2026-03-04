---
name: my-session-wrap
description: 세션 종료 시 작업 정리, 문서 업데이트, 학습 기록을 하는 스킬. "/wrap", "세션 정리", "마무리" 요청에 사용.
---

# My Session Wrap

Comprehensive session wrap-up workflow with multi-agent analysis.

## Execution Flow

```
┌─────────────────────────────────────────────────────┐
│  1. Check Git Status                                │
│     (What changed in this session?)                 │
├─────────────────────────────────────────────────────┤
│  2. Phase 1: 4 Analysis Agents (Parallel)           │
│     ┌─────────────────┬─────────────────┐           │
│     │  doc-updater    │  automation-    │           │
│     │                 │  scout          │           │
│     ├─────────────────┼─────────────────┤           │
│     │  learning-      │  followup-      │           │
│     │  extractor      │  suggester      │           │
│     └─────────────────┴─────────────────┘           │
├─────────────────────────────────────────────────────┤
│  3. Phase 2: Validation Agent (Sequential)          │
│     ┌───────────────────────────────────┐           │
│     │       duplicate-checker           │           │
│     │  (Remove duplicates from Phase 1) │           │
│     └───────────────────────────────────┘           │
├─────────────────────────────────────────────────────┤
│  4. Integrate Results                               │
│     (Combine all findings into summary)             │
├─────────────────────────────────────────────────────┤
│  5. User Selection + Execute                        │
│     (Choose which actions to perform)               │
└─────────────────────────────────────────────────────┘
```

## Step 1: Check Git Status

Run the following commands to understand what changed in this session:

```bash
git status --short
git diff --stat HEAD~3 2>/dev/null || git diff --stat
```

Then create a session summary:

```
Session Summary:
- Work: [Main tasks performed in this session]
- Files: [Created/modified files]
- Decisions: [Key decisions made]
```

This summary will be provided to all Phase 1 agents as context.

## Step 2: Phase 1 - Analysis Agents (Parallel)

Execute 4 agents in parallel (single message with 4 Agent tool calls).

### Agent Roles

| Agent | Role | Output |
|-------|------|--------|
| **doc-updater** | Analyze if CLAUDE.md or context.md need updates | Specific content to add/change |
| **automation-scout** | Detect repetitive patterns, suggest automation | Skill/command/agent suggestions |
| **learning-extractor** | Extract learnings, mistakes, new discoveries | TIL format summary |
| **followup-suggester** | Suggest incomplete tasks and next priorities | Prioritized task list |

### Parallel Execution

All 4 agents receive the Session Summary from Step 1 and run simultaneously:

```
Agent(
    subagent_type="session-wrap:doc-updater",
    description="Document update analysis",
    prompt="[Session Summary]\n\nAnalyze if CLAUDE.md, context.md need updates."
)

Agent(
    subagent_type="session-wrap:automation-scout",
    description="Automation pattern analysis",
    prompt="[Session Summary]\n\nAnalyze repetitive patterns or automation opportunities."
)

Agent(
    subagent_type="session-wrap:learning-extractor",
    description="Learning points extraction",
    prompt="[Session Summary]\n\nExtract learnings, mistakes, and new discoveries."
)

Agent(
    subagent_type="session-wrap:followup-suggester",
    description="Follow-up task suggestions",
    prompt="[Session Summary]\n\nSuggest incomplete tasks and next session priorities."
)
```

IMPORTANT: All 4 agents must be called in a single message to ensure parallel execution.

## Step 3: Phase 2 - Validation Agent (Sequential)

Run AFTER Phase 1 completes. This agent receives all Phase 1 results and checks for duplicates.

```
Agent(
    subagent_type="session-wrap:duplicate-checker",
    description="Phase 1 proposal validation",
    prompt="""
Validate Phase 1 analysis results for duplicates.

## doc-updater proposals:
[doc-updater results]

## automation-scout proposals:
[automation-scout results]

## learning-extractor proposals:
[learning-extractor results]

## followup-suggester proposals:
[followup-suggester results]

For each proposal, classify as:
1. Complete duplicate → Recommend SKIP
2. Partial duplicate → Suggest MERGE approach
3. No duplicate → APPROVE for addition
"""
)
```

### Validation Rules

| Classification | Action | Example |
|---------------|--------|---------|
| **Complete duplicate** | Skip one | doc-updater and followup-suggester both say "update README" |
| **Partial duplicate** | Merge into one | Similar suggestions with different details |
| **No duplicate** | Approve as-is | Unique insight from each agent |

## Step 4: Integrate Results

Combine all findings into a single summary for the user:

```markdown
## Session Wrap Analysis

### Documentation Updates
[doc-updater findings, filtered by duplicate-checker]

### Automation Opportunities
[automation-scout findings, filtered by duplicate-checker]

### Today I Learned
[learning-extractor findings]

### Follow-up Tasks
[followup-suggester findings, filtered by duplicate-checker]
```

## Step 5: User Selection + Execute

Ask the user which actions to perform:

```
AskUserQuestion(
    questions=[{
        "question": "Which actions would you like to perform?",
        "header": "Wrap Actions",
        "multiSelect": true,
        "options": [
            {"label": "Create commit (Recommended)", "description": "Commit current changes with a descriptive message"},
            {"label": "Update CLAUDE.md", "description": "Apply documentation updates from analysis"},
            {"label": "Create automation", "description": "Generate new skill/command from detected patterns"},
            {"label": "Skip all", "description": "End session without any action"}
        ]
    }]
)
```

## Step 6: Execute Selected Actions

Execute ONLY the actions the user selected:

- **Create commit**: Stage changes and commit with a summary message
- **Update CLAUDE.md**: Apply the specific updates identified by doc-updater
- **Create automation**: Generate the skill/command file suggested by automation-scout
- **Skip all**: End gracefully with no changes

## Quick Reference

### When to Use
- End of a significant work session
- Before switching to a different project
- After completing a feature or fixing a bug

### When to Skip
- Very short session with trivial changes
- Only reading/exploring code
- Quick one-off question answered
