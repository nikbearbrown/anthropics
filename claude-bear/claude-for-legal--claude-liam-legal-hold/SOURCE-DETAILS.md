# Source Details — claude-for-legal--claude-liam-legal-hold

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Legal Hold.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-legal-hold/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/litigation-legal/skills/legal-hold/SKILL.md
- Name: legal-hold
- Description: Issue, refresh, release, or report on legal holds — drafts the hold notice as .docx, updates legal_hold fields in _log.yaml, and calendars the next refresh. Use when the user says "issue a hold", "refresh hold", "release hold", or asks for a portfolio-wide hold status report.

## Capabilities To Name On Screen
- or report on legal holds — drafts the hold notice as .docx
- updates legal_hold fields in _log.yaml
- and calendars the next refresh
- Use when the user says "issue a hold"
- "refresh hold"

## Constraints / Failure Modes
- A legal hold is the most mechanical high-stakes document in-house counsel writes. The notice itself is templated. The failure modes are operational: issued too late…
- Do not proceed on an unintaken matter. Intake is what runs conflicts and writes the _log.yaml row the --refresh / --release / --status flags operate against
- Required when legal_hold.issued == false and the matter is active or reasonably anticipated
- Do not send the notice without an explicit yes. Drafting and scoping do not require the gate — issuance does
- Research the applicable preservation rule before issuing. Identify the jurisdiction and the source of the preservation duty (common law, rule of civil procedure…
- > External deliverable: the notice below is sent to custodians. Do NOT include a PRIVILEGED & CONFIDENTIAL — ATTORNEY WORK PRODUCT — PREPARED AT THE DIRECTION OF COUNSEL…
- EFFECTIVE IMMEDIATELY, you must preserve:
- DO NOT:

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: --status
- Referenced: _log.yaml
- Referenced: ~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md
- Referenced: --issue
- Referenced: legal-hold-v1.docx
- Referenced: legal_hold
- Referenced: next_refresh
- Referenced: --refresh
- Referenced: last_refresh
- Referenced: --release
- Signal: code block: yaml
- Signal: code block: markdown

## Source Sections
- Purpose
- Jurisdiction assumption
- Load context
- Modes
- --issue — first issuance
- --refresh — periodic reaffirmation
- --release — close the hold
- --status — report across the portfolio
- Active holds
- ⚠️ Attention

## Batch Log Match
- Row: 292
- Canonical path: anthropics/claude-for-legal/litigation-legal/skills/legal-hold/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-legal-hold/mp4/claude-liam-legal-hold.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
