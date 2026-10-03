# Source Details — claude-for-legal--claude-liam-matter-close

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Matter Close.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-matter-close/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/litigation-legal/skills/matter-close/SKILL.md
- Name: matter-close
- Description: Close a matter — capture outcome, final exposure, and lessons, then archive it out of the active portfolio without deleting the record. Use when the user wants to close a matter, says "[matter] is done", or needs to record a settlement, dismissal, judgment, withdrawal, or consolidation outcome.

## Capabilities To Name On Screen
- Close a matter — capture outcome
- final exposure
- then archive it out of the active portfolio without deleting the record
- Use when the user wants to close a matter
- says "[matter] is done"

## Constraints / Failure Modes
- > "I don't see [matter slug] in the matter log. Nothing to close — either the slug is wrong or the matter was never intaken through /litigation-legal:matter-intake.…
- Slug (required)
- Settlement agreement, final order, dismissal — path if available. Not required
- Do not write the close fields or append the close entry without an explicit yes
- Retain all existing fields. Do not delete the row

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: _log.yaml
- Referenced: closed: YYYY-MM-DD
- Referenced: ~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/[slug]/
- Referenced: /portfolio-status
- Referenced: ~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml
- Referenced: /litigation-legal:matter-intake
- Referenced: judgment-for-us
- Referenced: judgment-against-us
- Referenced: ~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md
- Referenced: /legal-hold --release
- Signal: code block: yaml
- Signal: code block: markdown

## Source Sections
- Purpose
- Load context
- Input
- The close
- 1. Resolution type
- 2. Resolution date
- 3. Final exposure
- 4. Lessons
- 5. Seed doc prompt
- Writing

## Batch Log Match
- Row: 302
- Canonical path: anthropics/claude-for-legal/litigation-legal/skills/matter-close/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-matter-close/mp4/claude-liam-matter-close.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
