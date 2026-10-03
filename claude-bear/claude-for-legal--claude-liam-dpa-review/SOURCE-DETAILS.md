# Source Details — claude-for-legal--claude-liam-dpa-review

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Dpa Review.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-dpa-review/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/privacy-legal/skills/dpa-review/SKILL.md
- Name: dpa-review
- Description: >

## Capabilities To Name On Screen
- Direction:: [We are processor / We are controller]
- Reviewed:: [date]
- Attached to:: [MSA / standalone]

## Constraints / Failure Modes
- Matter context. Check ## Matter workspaces in the practice-level CLAUDE.md. If Enabled is ✗ (the default for in-house users), skip the rest of this paragraph — skills…
- Carry severity from the upstream output as a floor per the cross-skill severity floor rule in ~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md → ##…
- > No silent supplement. If a research query to the configured legal research tool returns few or no results for a regime's breach window, transfer-mechanism requirement…
- > Tool-retrieved citations keep their source tag ([Westlaw], [Commission / regulator site], or the MCP tool name); web-search citations remain [web search — verify]…
- | Subprocessors | Current list disclosed, change mechanism defined | Subprocessor changes | Blanket approval vs. veto vs. notice-only |
- If the DPA commits to processing only for purposes X, Y, Z — does the privacy policy list those purposes?
- If the privacy policy says "we never sell data" — does any DPA clause look like a sale under CCPA?
- Only replace a whole clause when the counterparty's version is so far from your position that surgical edits would be harder to read than a fresh draft — and when you…

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: ~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md
- Referenced: /privacy-legal:matter-workspace switch <slug>
- Referenced: practice-level
- Referenced: matter.md
- Referenced: ~/.claude/plugins/config/claude-for-legal/privacy-legal/matters/<matter-slug>/
- Referenced: Cross-matter context
- Referenced: use-case-triage
- Referenced: pia-generation
- Referenced: dpa-review
- Referenced: [verify-pinpoint]
- Signal: code block: markdown

## Source Sections
- Matter context
- Purpose
- First: which direction?
- Jurisdiction assumption
- Load prior context on this counterparty / activity
- Load the playbook
- Federal sectoral overlay (ask first, before the term-by-term walk)
- The term-by-term review
- Core terms (check every DPA)
- When we're the processor: defensive review

## Batch Log Match
- Row: 217
- Canonical path: anthropics/claude-for-legal/privacy-legal/skills/dpa-review/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-dpa-review/mp4/claude-liam-dpa-review.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
