# Source Details — claude-for-legal--claude-liam-matter-briefing

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Matter Briefing.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-matter-briefing/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/litigation-legal/skills/matter-briefing/SKILL.md
- Name: matter-briefing
- Description: Deep briefing on one matter — current posture, what's changed, next deadline, open questions, and a risk re-assessment check, ready before a GC update or outside counsel call. Use when the user says "brief me on [matter]", "where are we on [matter]", or needs a read on a specific matter.

## Capabilities To Name On Screen
- Deep briefing on one matter — current posture
- what's changed
- next deadline
- open questions
- and a risk re-assessment check

## Constraints / Failure Modes
- Slug (required). If ambiguous or missing, ask the user to pick from a list of active matters

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: ~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md
- Referenced: last_updated
- Referenced: ~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml
- Referenced: _log.yaml
- Referenced: /litigation-legal:matter-intake
- Referenced: not-run
- Referenced: last_updated > 30 days ago
- Referenced: /litigation-legal:matter-update [slug]
- Referenced: /matter-update
- Signal: code block: markdown

## Source Sections
- Purpose
- Load context
- Input
- The briefing
- One-paragraph summary
- What's changed recently
- What's next
- Exposure
- Internal owners
- Risk re-assessment check

## Batch Log Match
- Row: 301
- Canonical path: anthropics/claude-for-legal/litigation-legal/skills/matter-briefing/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-matter-briefing/mp4/claude-liam-matter-briefing.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
