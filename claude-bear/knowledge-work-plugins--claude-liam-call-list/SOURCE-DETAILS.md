# Source Details — knowledge-work-plugins--claude-liam-call-list

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Call List.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-call-list/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/small-business/skills/call-list/SKILL.md
- Name: call-list
- Description: Ranks the top-5 leads most worth calling today, supplies talking points from email history, blocks time on the calendar, and drafts follow-up messages. Accepts optional count and date arguments.

## Capabilities To Name On Screen
- Ranks the top-5 leads most worth calling today
- supplies talking points from email history
- blocks time on the calendar
- and drafts follow-up messages
- Accepts optional count and date arguments.

## Constraints / Failure Modes
- Never send emails automatically. Present drafts for owner approval only
- Never create calendar blocks without owner confirmation — show the proposed list first
- Never update HubSpot deal stages automatically

## Procedure / Sequence
- Pipeline scan: Using the lead-triage skill workflow: 1. Pull open HubSpot deals and contacts with activity in the last 30 days. 2.…
- Rank and select top N: Rank all scored leads and select the top --n. For ties, prefer leads with unanswered inbound signals. For each selected…
- Calendar block: For each lead on the list, offer to block 20 minutes on the owner's calendar for the target date. Show the proposed…
- Draft follow-ups: For any lead that has an unanswered email older than 3 days, draft a brief follow-up

## Supporting Files And Signals
- Referenced: --n
- Referenced: --date
- Referenced: YYYY-MM-DD
- Referenced: lead-triage

## Source Sections
- Step 1 — Pipeline scan
- Step 2 — Rank and select top N
- Step 3 — Calendar block
- Step 4 — Draft follow-ups
- Connector failures
- Approval gates
- Output

## Batch Log Match
- Row: 127
- Canonical path: anthropics/knowledge-work-plugins/small-business/skills/call-list/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-call-list/mp4/claude-liam-call-list.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
