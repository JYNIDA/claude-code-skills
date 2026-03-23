---
name: ttm-research
description: >
  Produces a 9-section research brief for The Thinking Mode (TTM) guests.
  Use when Jiyoon asks to "research [guest]", "조사해줘", "브리프 만들어줘",
  "TTM 게스트 리서치", or needs background research + series fit analysis.
  Does NOT generate interview questions — use thinking-mode-pipeline Stage 6.
---

# The Thinking Mode — Guest Research Brief

Produce a **9-section bilingual research brief** (English + Korean) for any TTM guest.
English first, Korean below each section. Cite sources inline as [source-name]. Flag unverified claims.

---

## Series Context (internalize, do not print)

**Read before starting:** `~/.claude/skills/references/ttm_series_context.md`
This file contains the full series mission, 6-theme structure, Beyond Question framework, confirmed episodes, and pipeline. Do not reconstruct this from memory.

**The Thinking Mode** — EO Global (@eoglobal, 650K+ subs, entrepreneur/builder audience).
Stance: **Practical Optimism**. Every episode answers: *given what's happening, what do you do?*

**6 Themes** (theme determines the Beyond Question, not the guest's field):
1. **After Coding** — If AI writes the code, why are we still teaching it?
2. **Redesigning Learning** — If AI democratizes knowledge, what should we still learn — and how?
3. **When AI Dreams** — If AI can imagine, create, and socialize — what's left that's uniquely human?
4. **The Future of Work** — How is AI transforming the way we work?
5. **A New Map of Power** — How is AI redrawing the map of power?
6. **The Architects** — Who designs AI's character and rules?

**Episode Arc:** ① HOOK → ② WHO → ③ THE CHANGE → ④ HUMAN EDGE → ⑤ HOW TO → ⑥ HORIZON

---

## 9 Sections

### 1 — Disambiguation
If multiple people share this name, identify the subject. State criteria. Include links.

---

### 2 — Person Deep Dive

**2a. Current Role** — Title, org, location. How long in role.

**2b. Career Timeline** — Table: Period | Role | Organization.

**2c. Research/Work Footprint** — Key papers (citation counts), products, talks, patents.
- Academics: h-index, total citations, landmark papers
- Practitioners: products shipped, measurable impact

**2d. Public Stance & Themes** — 2–3 central intellectual commitments. What do they argue that others resist?

**2e. Network** — Key collaborators, mentors, funders, critics.

---

### 3 — Company / Project Deep Dive
If company/startup: what it does, founding story, business model, funding, traction.
If academic: describe lab and research agenda.

---

### 4 — What's New (Last 90 Days)
Papers, talks, interviews, podcasts, major press, launches, controversy. Use specific dates.

---

### 5 — Open Questions & Diligence Flags
Numbered list. Flag: unverified funding, unknown team size, unresolved controversy, uncorroborated claims.

---

### 6 — TTM Fit Analysis ⭐ (most important)

**6a. Theme** — Which of the 6 TTM themes? (After Coding / Redesigning Learning / When AI Dreams / The Future of Work / A New Map of Power / The Architects) Cite 2–3 specific works. If multi-theme, pick primary. Check confirmed guests in `ttm_series_context.md` to ensure this guest's angle is distinct.

**6b. Core Question** — *"What does it mean for an entrepreneur/builder/thinker that [THIS GUEST'S WORK] is true?"*

**6c. Arc Weight** — Which 2–3 arc sections should carry most weight for this guest? Why?

**6d. Series Angle** — Unlearning / Access & Equity / Frontier Builder / Human Resistance / Governance Gap?
Name the angle and explain the connection.

---

### 7 — Framing + Yama
2–3 sentences for the producer: who this person is, why now, what the episode is really about.

**Yama:**
> **"[A tension or paradox specific to this guest's work]?"**

---

### 8 — YouTube Titles & Thumbnail Phrases

**8 title options.** TTM voice: no sensationalism, no doom, Practical Optimism.
Must make a builder or entrepreneur want to clear an hour.

**5 Korean thumbnail phrases** (2–8 characters, punchy, works as overlay text on face shot).

---

### 9 — Universal Questions Mapping

For each of the 6 TTM universal questions, write:
- **(a)** Stock question
- **(b)** Guest-specific adaptation that makes the question land harder

| # | Question | Guest-Specific Adaptation |
|---|----------|--------------------------|
| Q1 | Blind Spot — "What's hiding in plain sight about AI that the smartest people in your field keep getting wrong?" | [adapted] |
| Q2 | Hot Take — "What do you believe about AI that almost nobody agrees with you on?" | [adapted] |
| Q3 | Human Edge — "What skill do *you personally* have that you're most convinced AI can never replace?" | [adapted] |
| Q4 | How To — "If a 25-year-old asked: what's the *one* thing I should do differently this year because of AI?" | [adapted] |
| Q5 | The Bet — "Write a letter to your 2030 self about AI. What's the first line?" | [adapted] |
| Q6 | Horizon *(always last)* — "Ten years from now — what does the world look like if we get this right? And if we get it wrong?" | [adapted] |

---

## Invocation

```
Research [GUEST NAME].
[Optional: "They are a [role description]."]
[Optional: "TTM vertical: [THINK/WORK/POWER/HUMAN]"]
[Optional: "Preliminary angle: [one sentence]"]
```

If vertical/angle not specified, determine from research and state reasoning in Section 6.

---

## Output

After completing the brief:
1. **Notion:** Append to TTM Research Brief page (ID: `32574768-ec37-80f3-b782-f49ff8c989bd`) using `notion-update-page` → `update_content` append at the bottom. Add a `---` divider before each new brief.
2. **Local file:** Save to `~/Desktop/Cowork/Research workflow/validation_[GuestName]_[date].md`

## Quality Rules

- No preamble. Start directly with Section 1.
- Bilingual throughout (English → Korean every section).
- Section 6 is analytical, not descriptive — make a recommendation.
- Practical Optimism tone. Audience is builders, not bystanders.
- Flag uncertainty: "Unverified as of [date]" beats false confidence.
- Include numbers in all data points (citations, followers, view counts, dates).
