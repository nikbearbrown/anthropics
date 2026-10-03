# Source Details — claude-quickstarts--claude-liam-first-run

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, First Run.
- Family: claude-quickstarts
- Source sheet: /Users/nik/Documents/books/anthropics/claude-quickstarts/youtube/claude-liam-first-run/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-quickstarts/computer-use-best-practices/.claude/skills/first-run/SKILL.md
- Name: first-run
- Description: Guide a new user through their first computer-use agent run (env check, safe browser-only task, then open the trajectory viewer).

## Capabilities To Name On Screen
- Guide a new user through their first computer-use agent run (env check
- safe browser-only task
- then open the trajectory viewer).

## Constraints / Failure Modes
- description: Guide a new user through their first computer-use agent run (env check, safe browser-only task, then open the trajectory viewer)
- browser-only task that does not touch their mouse or keyboard, and then
- > Never read the contents of .env. Do not cat, grep (without -q),
- > Read, or otherwise display it — the user's API key must never appear in
- > this conversation or in your context. Only check for its presence
- the key into chat, and do not edit .env for them). Wait until they confirm
- and explain any warnings. These permissions are only needed for the desktop
- ## 2. Run a safe browser-only task

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: .env
- Referenced: -q
- Referenced: python -c "import computer_use, playwright; print('ok')"
- Referenced: README.md
- Referenced: .env.example
- Referenced: trajectory: runs/...
- Referenced: python -m computer_use "open TextEdit and type hello world"
- Referenced: python -m uvicorn dev_ui.tool_panel.server:app --reload
- Signal: code block: bash

## Source Sections
- 0. Orient
- 1. Environment check
- 2. Run a safe browser-only task
- 3. Open the trajectory viewer
- 4. Next steps

## Batch Log Match
- Row: 77
- Canonical path: anthropics/claude-quickstarts/computer-use-best-practices/.claude/skills/first-run/SKILL.md
- MP4 path: anthropics/claude-quickstarts/youtube/claude-liam-first-run/mp4/claude-liam-first-run.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
