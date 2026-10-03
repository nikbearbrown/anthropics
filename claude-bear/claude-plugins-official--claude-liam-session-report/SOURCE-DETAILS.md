# Source Details — claude-plugins-official--claude-liam-session-report

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Session Report.
- Family: claude-plugins-official
- Source sheet: /Users/nik/Documents/books/anthropics/claude-plugins-official/youtube/claude-liam-session-report/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-plugins-official/plugins/session-report/skills/session-report/SKILL.md
- Name: session-report
- Description: Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive prompts) from ~/.claude/projects transcripts.

## Capabilities To Name On Screen
- Generate an explorable HTML report of Claude Code session usage (tokens
- expensive prompts) from ~/.claude/projects transcripts.

## Constraints / Failure Modes
- Do not restructure existing sections
- Report the saved file path to the user. Do not open it or render it

## Procedure / Sequence
- Get data.: Run the bundled analyzer (default window: last 7 days; honor a different range if the user passed one, e.g. 24h, 30d…
- Read: /tmp/session-report.json. Skim overall, by_project, by_subagent_type, by_skill, cache_breaks, top_prompts.
- Copy the template: (also bundled alongside this SKILL.md) to the output path in the current working directory
- Edit the output file: (use Edit, not Write — preserve the template's JS/CSS): - Replace the contents of <script id="report-data"…
- Report: the saved file path to the user. Do not open it or render it.

## Supporting Files And Signals
- Referenced: analyze-sessions.mjs
- Referenced: --since
- Referenced: /tmp/session-report.json
- Referenced: by_project
- Referenced: by_subagent_type
- Referenced: by_skill
- Referenced: cache_breaks
- Referenced: top_prompts
- Referenced: <script id="report-data" type="application/json">
- Referenced: <!-- AGENT: anomalies -->
- Signal: code block: sh
- Signal: code block: html

## Source Sections
- Steps
- Notes

## Batch Log Match
- Row: 65
- Canonical path: anthropics/claude-plugins-official/plugins/session-report/skills/session-report/SKILL.md
- MP4 path: anthropics/claude-plugins-official/youtube/claude-liam-session-report/mp4/claude-liam-session-report.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
