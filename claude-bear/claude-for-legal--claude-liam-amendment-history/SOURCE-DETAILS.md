# Source Details — claude-for-legal--claude-liam-amendment-history

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Amendment History.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-amendment-history/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/commercial-legal/skills/amendment-history/SKILL.md
- Name: amendment-history
- Description: >

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- to Mode 2. If no provision is mentioned, run Mode 1. Ask only if
- Matter context. Check ## Matter workspaces in the practice-level CLAUDE.md. If Enabled is ✗ (the default for in-house users), skip the rest of this paragraph — skills…
- Parse the user's request to determine which mode to run. Do not ask
- Only ask the user to confirm ordering if:
- top of the output only where uncertain:
- This skill reads the base agreement and amendments — often privileged or confidential in their own right, and typically used for privileged analysis. The output inherits…
- drive the output — do not show it to the user
- Every finding must include an inline section reference so the reader

## Procedure / Sequence
- Load and order the documents: Accept documents from any of these sources: [CLM integration coming soon] (if connected): Search by counterparty name…
- Read and index: Read each document in chronological order. For each, extract: - Document type (base agreement, amendment number…

## Supporting Files And Signals
- Referenced: /commercial-legal:matter-workspace switch <slug>
- Referenced: practice-level
- Referenced: matter.md
- Referenced: . Never read another matter's files unless
- Referenced: ~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md
- Signal: code block: markdown

## Source Sections
- Instructions
- Examples
- Matter context
- Purpose
- Mode detection
- Step 1: Load and order the documents
- Privilege inheritance
- Step 2: Read and index
- Mode 1: Summary of all changes
- Section reference rule

## Batch Log Match
- Row: 99
- Canonical path: anthropics/claude-for-legal/commercial-legal/skills/amendment-history/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-amendment-history/mp4/claude-liam-amendment-history.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
