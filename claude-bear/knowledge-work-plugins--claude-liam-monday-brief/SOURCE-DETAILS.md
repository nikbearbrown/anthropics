# Source Details — knowledge-work-plugins--claude-liam-monday-brief

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Monday Brief.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-monday-brief/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/small-business/skills/monday-brief/SKILL.md
- Name: monday-brief
- Description: Generates a one-page Monday morning briefing — cash, sales, pipeline, week ahead, top three to-dos. Accepts optional post destination and save-to arguments.

## Capabilities To Name On Screen
- Generates a one-page Monday morning briefing — cash
- top three to-dos
- Accepts optional post destination and save-to arguments.

## Constraints / Failure Modes
- If --post slack or --post teams, post the Three things section only (not the full brief — keep the channel post short) and link to the saved file
- Never post if the brief surfaces unflattering numbers (significant cash drop, deal slipping) without explicitly asking the owner — the channel may have non-leadership…

## Procedure / Sequence
- Run business-pulse: Trigger the business-pulse skill workflow. It pulls in this order, scoping to whatever is connected: 1. Cash…
- Format the one-page brief: Layout (markdown, fits on one screen): ` # Monday Brief — {Mon DD, YYYY}
- Save and (optionally) post: 1. Save the brief to the chosen --save-to location: - files — Google Drive or OneDrive root, filename…

## Supporting Files And Signals
- Referenced: --post
- Referenced: --save-to
- Referenced: business-pulse
- Referenced: monday-brief-YYYY-MM-DD.md
- Referenced: ~/Desktop/monday-brief-YYYY-MM-DD.md
- Referenced: --post slack
- Referenced: --post teams

## Source Sections
- Step 1 — Run business-pulse
- Step 2 — Format the one-page brief
- Cash
- Sales (last 7d vs prior 7d)
- Pipeline
- Week ahead
- Three things that need you today
- Step 3 — Save and (optionally) post
- Approval gates
- Cadence note

## Batch Log Match
- Row: 313
- Canonical path: anthropics/knowledge-work-plugins/small-business/skills/monday-brief/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-monday-brief/mp4/claude-liam-monday-brief.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
