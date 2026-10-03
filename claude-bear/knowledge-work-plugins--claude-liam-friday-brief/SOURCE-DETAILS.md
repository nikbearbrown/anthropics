# Source Details — knowledge-work-plugins--claude-liam-friday-brief

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Friday Brief.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-friday-brief/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/small-business/skills/friday-brief/SKILL.md
- Name: friday-brief
- Description: Delivers the Friday end-of-week pulse — revenue vs prior week, top sellers, wins and watches. Accepts optional lookback window of 7 or 14 days.

## Capabilities To Name On Screen
- Delivers the Friday end-of-week pulse — revenue vs prior week
- wins and watches
- Accepts optional lookback window of 7 or 14 days.

## Constraints / Failure Modes
- Run with whatever is connected — this command degrades gracefully. If PayPal is missing, skip transaction data and note "PayPal not connected — revenue data from HubSpot…
- Never send or post this brief automatically. Always display it for the owner to review first
- Never auto-cancel or modify anything. Surface the data and recommendations only

## Procedure / Sequence
- Revenue pulse: Using the business-pulse skill workflow: 1. Pull PayPal transactions for the lookback period. 2. Pull any HubSpot deal…
- Sales breakdown: 1. List the top 5 selling products/services by volume and revenue. 2. List the bottom 3 (anything that moved less than…
- Wins and watches summary: Format the output as

## Supporting Files And Signals
- Referenced: --lookback
- Referenced: business-pulse

## Source Sections
- Step 1 — Revenue pulse
- Step 2 — Sales breakdown
- Step 3 — Wins and watches summary
- Connector failures
- Approval gates
- Output

## Batch Log Match
- Row: 246
- Canonical path: anthropics/knowledge-work-plugins/small-business/skills/friday-brief/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-friday-brief/mp4/claude-liam-friday-brief.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
