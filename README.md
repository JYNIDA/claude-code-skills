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
| **broll-finder** | Paste a script → find B-roll sources → download → generate source doc | `/broll-finder` |

## Highlight: broll-finder

The fastest way to go from script to downloaded B-roll with source credits:

```
/broll-finder     → Paste your script, skill extracts scenes automatically
```

**How it works (5 phases):**
1. **Script Analysis** — AI extracts scenes and search keywords per shot
2. **Source Search** — Searches YouTube, news outlets (Reuters, AP, BBC), and image libraries in parallel
3. **Interactive Loop** — Add keywords, change source type, or paste URLs directly; repeat until satisfied
4. **Auto Download** — Downloads selected YouTube videos in 4K MP4 via yt-dlp
5. **Source Doc** — Generates `sources.md` with titles, links, channel credits, and ready-to-use credit lines

**Requirements:**
- Claude Code installed
- `yt-dlp` installed (`brew install yt-dlp`)
- Notion MCP (optional, for Notion upload)

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
