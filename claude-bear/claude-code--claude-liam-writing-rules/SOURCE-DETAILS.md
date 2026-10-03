# Source Details — claude-code--claude-liam-writing-rules

Generated: 2026-09-05T11:09:00

## Reel
- Question: Writing Hookify Rules
- Family: claude-code
- Source sheet: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-code/youtube/claude-liam-writing-rules/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-code/plugins/hookify/skills/writing-rules/SKILL.md
- Name: Writing Hookify Rules
- Description: This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify rule", or needs guidance on hookify rule syntax and patterns.

## Capabilities To Name On Screen
- This skill should be used when the user asks to "create a hookify rule"
- "write a hook rule"
- "configure hookify"
- "add a hookify rule"
- or needs guidance on hookify rule syntax and patterns.

## Constraints / Failure Modes
- name (required): Unique identifier for the rule
- enabled (required): Boolean to activate/deactivate
- event (required): Which hook event to trigger on
- not_contains: Substring must NOT be present
- All conditions must match for rule to trigger
- Reminders about required steps
- pattern: rm -rf /tmp # Only matches exact path

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: .claude/hookify.{rule-name}.local.md
- Referenced: warn-dangerous-rm
- Referenced: block-console-log
- Referenced: file_path
- Referenced: new_text
- Referenced: old_text
- Referenced: regex_match
- Referenced: not_contains
- Referenced: starts_with
- Referenced: ends_with
- Signal: code block: markdown
- Signal: code block: yaml
- Signal: code block: bash

## Source Sections
- Overview
- Rule File Format
- Basic Structure
- Frontmatter Fields
- Advanced Format (Multiple Conditions)
- Message Body
- Event Type Guide
- bash Events
- file Events
- stop Events

## Batch Log Match
- Row: 25
- Canonical path: anthropics/claude-code/plugins/hookify/skills/writing-rules/SKILL.md
- MP4 path: anthropics/claude-code/youtube/claude-liam-writing-rules/claude-liam-writing-rules.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
