# Source Details — claude-for-legal--claude-liam-deadlines

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Deadlines.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-deadlines/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/legal-clinic/skills/deadlines/SKILL.md
- Name: deadlines
- Description: >

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- A clinic's biggest operational risk is a missed deadline. Students carry multiple cases, work part-time, turn over every semester. Deadlines that live only in individual…
- Plausibility sanity band. After the student enters a due date, do NOT compute or verify — but apply a rough plausibility check against typical ranges for the filing…
- Hard stop at cold-start if the band file is missing. If references/plausibility-bands/{state}.md does not exist for the clinic's jurisdiction, do NOT silently run…
- > "I don't have deadline plausibility checks for [state] — the sanity band for this clinic's jurisdiction isn't in the shipped reference files. I can still track…
- Do not fall back to the CA table for a non-CA clinic. The silent-degradation case — shipping a California sanity check to an Illinois clinic — is the failure this fix…
- If no band is known for this type: (unusual filing, non-standard deadline), do not sanity-check — write the entry and note in the warnings: field that no plausibility…
- The skill does not compute. If the student enters [VERIFY] in the due: field because they haven't done the math yet, write the entry with due: [VERIFY] — the sanity band…
- [count only — expand with /deadlines --report --horizon=30 for details]

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: ~/.claude/plugins/config/claude-for-legal/legal-clinic/CLAUDE.md
- Referenced: --add
- Referenced: ~/.claude/plugins/config/claude-for-legal/legal-clinic/deadlines.yaml
- Referenced: --report
- Referenced: --update [id]
- Referenced: --complete [id]
- Referenced: --close [id]
- Referenced: /semester-handoff
- Referenced: --add | --report | --update | --complete | --close
- Referenced: [case]-[short-desc]-[YYYY-MM]
- Signal: code block: markdown

## Source Sections
- Purpose
- Load context
- Modes
- --add — log a new deadline
- --report (default) — cross-case rollup
- ⚠️ Overdue (flagged for immediate attention)
- 🔴 Due today / next 3 days
- 🟡 Due in 4-7 days
- 🟢 Due in 8-14 days
- Beyond 14 days

## Batch Log Match
- Row: 193
- Canonical path: anthropics/claude-for-legal/legal-clinic/skills/deadlines/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-deadlines/mp4/claude-liam-deadlines.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
