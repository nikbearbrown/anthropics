# Source Details — claude-for-legal--claude-liam-board-minutes

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Board Minutes.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-board-minutes/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/corporate-legal/skills/board-minutes/SKILL.md
- Name: board-minutes
- Description: >

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- Matter context. Check ## Matter workspaces in the practice-level CLAUDE.md. If Enabled is ✗ (the default for in-house users), skip the rest of this paragraph — skills…
- If ~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md has no minutes format: run cold-start first. Do not proceed with a generic format
- Any guests who attended for specific agenda items only (note their attendance as limited to that item)
- Confirm quorum was present. If not: stop and flag before drafting. Do not produce minutes that imply a valid meeting occurred. Surface the question to outside counsel…
- Use the house format from ~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md. Do not default to a generic format. The seed minutes are the template…
- Long-form narrative: Summarise the substance of the discussion — what questions were raised, what information was presented, what factors the board considered. Do not…
- Action minutes: Note only what was presented and what action was taken. No discussion content beyond "the board discussed the matter."
- Hybrid: Full narrative for major items (acquisitions, financials, significant approvals), action-only for routine items

## Procedure / Sequence
- Identify the meeting
- Attendance: Ask for the attendee list, or offer to pull from the calendar invite if the connector is authorized. Directors present…
- Materials: Ask for the meeting materials. These are the source for the agenda items and any resolutions. > Can you share the…
- Draft the minutes: Use the house format from ~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md. Do not default to a…
- 5: Consequential-action gate (adopt minutes): Before adopting minutes as final: Read ## Who's using this in…
- Output and review prompts: Produce the full draft. The minutes themselves are a corporate record, not privileged; do not apply the work-product…

## Supporting Files And Signals
- Referenced: /corporate-legal:matter-workspace switch <slug>
- Referenced: practice-level
- Referenced: matter.md
- Referenced: ~/.claude/plugins/config/claude-for-legal/corporate-legal/matters/<matter-slug>/
- Referenced: Cross-matter context
- Referenced: ~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md
- Referenced: /corporate-legal:written-consent

## Source Sections
- Matter context
- Purpose
- Load context
- Step 1: Identify the meeting
- Calendar detection
- Meeting metadata to confirm
- Step 2: Attendance
- Step 3: Materials
- Step 4: Draft the minutes
- Standard structure (adapt to house format)

## Batch Log Match
- Row: 106
- Canonical path: anthropics/claude-for-legal/corporate-legal/skills/board-minutes/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-board-minutes/mp4/claude-liam-board-minutes.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
