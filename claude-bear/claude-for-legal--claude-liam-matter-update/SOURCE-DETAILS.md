# Source Details — claude-for-legal--claude-liam-matter-update

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Matter Update.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-matter-update/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/litigation-legal/skills/matter-update/SKILL.md
- Name: matter-update
- Description: Append a dated event to a matter's history file and refresh the log row — captures new developments, status changes, risk re-assessments, deadline shifts, and settlement authority changes. Use when the user wants to log an update on a matter, note a development, or record a status change against the portfolio.

## Capabilities To Name On Screen
- Append a dated event to a matter's history file and refresh the log row — captures new developments
- status changes
- risk re-assessments
- deadline shifts
- and settlement authority changes

## Constraints / Failure Modes
- The portfolio only stays useful if it stays current. This skill makes logging an update cheap — two minutes of structured capture, no freeform drift
- Slug (required). If not provided, ask — with a short list of recently updated matters to pick from
- risk: — reassessment required?
- Only prompt for fields likely affected by the event type. Procedural updates usually touch stage and next_deadline only; a settlement offer might touch materiality…
- Do not log the acceptance or flip materiality on acceptance basis without an explicit yes. Logging offers or counters does not require the gate — acceptance does
- Acceptable answers include no change — but no change must be explicit, not implied by silence. Capture in the history entry:

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: ~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/
- Referenced: _log.yaml
- Referenced: last_updated
- Referenced: ~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml
- Referenced: ~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md
- Referenced: /litigation-legal:matter-intake
- Referenced: history.md
- Referenced: exposure_range:
- Referenced: next_deadline:
- Referenced: outside_counsel:
- Signal: code block: markdown

## Source Sections
- Purpose
- Load context
- Input
- The update
- 1. Event type
- 2. Date
- 3. Summary
- 4. Log field changes
- 4pre. Settlement-acceptance gate
- 4a. Materiality trigger — explicit prompt

## Batch Log Match
- Row: 304
- Canonical path: anthropics/claude-for-legal/litigation-legal/skills/matter-update/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-matter-update/mp4/claude-liam-matter-update.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
