# Source Details — claude-plugins-official--claude-liam-playground

Generated: 2026-09-05T11:09:00

## Reel
- Question: playground
- Family: claude-plugins-official
- Source sheet: /Users/nik/Documents/books/anthropics/claude-plugins-official/youtube/claude-liam-playground/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-plugins-official/plugins/playground/skills/playground/SKILL.md
- Name: playground
- Description: Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through controls, see a live preview, and copy out a prompt. Use when the user asks to make a playground, explorer, or interactive tool for a topic.

## Capabilities To Name On Screen
- Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through controls
- see a live preview
- and copy out a prompt
- Use when the user asks to make a playground
- or interactive tool for a topic.

## Constraints / Failure Modes
- Prompt output. Natural language, not a value dump. Only mentions non-default choices. Includes enough context to act on without seeing the playground. Updates live
- // Only mention non-default values
- Preview doesn't update instantly → every control change must trigger immediate re-render

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: templates/
- Referenced: templates/design-playground.md
- Referenced: templates/data-explorer.md
- Referenced: templates/concept-map.md
- Referenced: templates/document-critique.md
- Referenced: templates/diff-review.md
- Referenced: templates/code-map.md
- Referenced: open <filename>.html
- Referenced: border-radius of ${state.borderRadius}px
- Referenced: Update the card to use ${parts.join(', ')}.
- Signal: code block: javascript

## Source Sections
- When to use this skill
- How to use this skill
- Core requirements (every playground)
- State management pattern
- Prompt output pattern
- Common mistakes to avoid

## Batch Log Match
- Row: 58
- Canonical path: anthropics/claude-plugins-official/plugins/playground/skills/playground/SKILL.md
- MP4 path: anthropics/claude-plugins-official/youtube/claude-liam-playground/claude-liam-playground.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
