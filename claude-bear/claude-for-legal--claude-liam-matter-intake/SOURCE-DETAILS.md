# Source Details — claude-for-legal--claude-liam-matter-intake

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Matter Intake.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-matter-intake/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/litigation-legal/skills/matter-intake/SKILL.md
- Name: matter-intake
- Description: Intake a new matter — uniform questions covering identification, conflicts, source, risk triage, materiality, outside counsel, owners, legal hold, and key dates; writes matter.md and history.md and appends a structured row to _log.yaml. Use when the user says "new matter", "intake this matter", or wants to bring a new matter into the portfolio.

## Capabilities To Name On Screen
- Intake a new matter — uniform questions covering identification
- outside counsel
- and key dates
- writes matter.md and history.md and appends a structured row to _log.yaml
- Use when the user says "new matter"

## Constraints / Failure Modes
- If the practice profile's ## Side is plaintiff, defense, or a "both — default X" variant, pre-fill the role from that default and confirm. If ## Side is varies by…
- Path 2 — Mark pending with owner + due date. Allowed only when ~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md Conflicts clearance declares…
- Path 3 — Bypass with documented rationale. Only if the user explicitly acknowledges the bypass. Record in conflicts.override:
- This field is visible in every /portfolio-status, every /matter briefing, and every /matter-update until removed. It is never removed by the skill — only by explicit…
- Do not proceed silently. "I'll do it later" is not an acceptable response. One of Path 1/2/3 must be chosen, and the choice is captured in the record
- Append-only event log. Most recent at top
- override: # populated only on Path 3 bypass

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: ~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md
- Referenced: ~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml
- Referenced: _log.yaml
- Referenced: matter.md
- Referenced: cleared | pending | not-run | waived
- Referenced: corporate-legal | outside-counsel | system-check | informal | other
- Referenced: /matter-update
- Referenced: /portfolio-status
- Referenced: not-run
- Referenced: history.md
- Signal: code block: yaml
- Signal: code block: markdown

## Source Sections
- Purpose
- Load context
- The intake
- 1. Identification
- 2. Conflicts check
- 3. Source
- 4. Risk triage — against house calibration
- 5. Materiality
- 6. Outside counsel
- 7. Internal owners

## Batch Log Match
- Row: 303
- Canonical path: anthropics/claude-for-legal/litigation-legal/skills/matter-intake/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-matter-intake/mp4/claude-liam-matter-intake.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
