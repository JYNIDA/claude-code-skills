# Claude Code Skills

Custom Claude Code skills for YouTube content production workflow.

Built for a global business & tech interview channel exploring how thinkers and builders navigate the AI era.

## Skills

| Skill | Purpose | Trigger |
|-------|---------|---------|
| **thinking-mode-pipeline** | 6-stage content pipeline: Trend → Validation → Decision → Outreach → Research → Questions | `/thinking-mode-pipeline` |
| **copy-thinking-mode** | YouTube title/thumbnail/intro optimization with CTR scoring model | `/copy-thinking-mode` |
| **copy-founder-focused** | Title/thumbnail optimization for founder interview series | `/copy-founder-focused` |
| **interview-prep** | Guest research + topic development + question list | `/interview-prep` |
| **weekly-meeting** | Weekly meeting prep: YouTube analytics + Slack status + meeting notes | `/weekly-meeting` |
| **my-clarify** | Turn vague content planning into actionable specs | `/my-clarify` |

## Highlight: thinking-mode-pipeline

The most comprehensive skill — a full content production pipeline:

```
/thinking-mode-pipeline              → Overview + stage selection
/thinking-mode-pipeline trend        → Stage 1: Trend Radar
/thinking-mode-pipeline validate <name>  → Stage 2: Guest Validation
/thinking-mode-pipeline validate-batch   → Stage 2: Batch Validation
/thinking-mode-pipeline decide       → Stage 3: Decision Gate
/thinking-mode-pipeline outreach <name>  → Stage 4: Outreach Email
/thinking-mode-pipeline research <name>  → Stage 5: Deep Research
/thinking-mode-pipeline questions <name> → Stage 6: Interview Questions
```

**Key concepts:**
- **5-Dimension Guest Scoring** — Authority, Media Charisma, Hot Take, Timeliness, Series Fit (each /5)
- **Yama** — One-line angle defining the episode's core thesis
- **CTR Scoring Model v6** — Predictive click-through rate based on title/thumbnail patterns
- **Timely vs Evergreen** — Prioritize outreach by news cycle windows

## Setup

1. Clone into `~/.claude/skills/`
2. For `weekly-meeting`: copy `config/config.example.json` → `config/config.json` and add your API keys

## How Skills Work

Each skill = a folder with `SKILL.md` that tells Claude Code what to do, step by step. Type a trigger and it runs autonomously.

## License

MIT
