# The Thinking Mode — Claude Code Skills

Custom Claude Code skills for YouTube interview series content production.

Built for a global business & tech interview channel that explores how thinkers and builders navigate the AI era.

## Skills

### 1. thinking-mode-pipeline

6-stage content pipeline: Trend Scan → Guest Validation → Decision Gate → Outreach → Deep Research → Interview Questions

```
/thinking-mode-pipeline              → Full pipeline overview
/thinking-mode-pipeline validate <name>  → Validate a single guest
/thinking-mode-pipeline validate-batch   → Batch validate multiple guests
/thinking-mode-pipeline outreach <name>  → Draft outreach email
/thinking-mode-pipeline research <name>  → Deep research briefing
/thinking-mode-pipeline questions <name> → Interview question list
```

**Key features:**
- 5-Dimension Guest Scoring (Authority, Media Charisma, Hot Take, Timeliness, Series Fit — each /5)
- Yama: one-line angle that defines the episode's core thesis
- Timely vs Evergreen tagging for outreach prioritization
- Parallel batch validation with agent teams
- Fact-checking step built into the process

### 2. copy-thinking-mode

YouTube title, thumbnail text, and intro hook optimization with a predictive CTR scoring model.

```
/copy-thinking-mode
```

**Key features:**
- CTR Scoring Model v6 (base rate + pattern bonuses)
- Title/thumbnail concept cards with predicted CTR
- Hook line brainstorming

## How Claude Code Skills Work

Each skill is a folder with a `SKILL.md` that tells Claude Code:
- When to activate (trigger keywords)
- What to do step-by-step
- What format to output
- What reference files to use (templates, scoring models)

Type a trigger like `/thinking-mode-pipeline validate Sam Altman` and Claude Code follows the instructions autonomously.

## License

MIT
