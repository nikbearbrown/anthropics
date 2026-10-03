# Source Details — claude-for-legal--claude-liam-dsar-response

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Dsar Response.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-dsar-response/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/privacy-legal/skills/dsar-response/SKILL.md
- Name: dsar-response
- Description: >

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- Output response draft. Do NOT send — human reviews and sends
- Before pasting the request: the request will contain the data subject's PII. Confirm your session and output storage meet your data-handling requirements. Redact…
- Matter context. Check ## Matter workspaces in the practice-level CLAUDE.md. If Enabled is ✗ (the default for in-house users), skip the rest of this paragraph — skills…
- > No silent supplement. If a research query to the configured legal research tool returns few or no results for the jurisdiction's rights, exemptions, or deadlines…
- > Tool-retrieved citations keep their source tag ([Westlaw], [issuing authority site], or the MCP tool name); web-search citations remain [web search — verify]…
- is at issue. To proceed, please [verification step]. We cannot provide personal
- data in response to a request we cannot verify
- > Research-connector pre-flight. Before emitting either letter or the internal exemption analysis, check whether a legal research connector is reachable for this session…

## Procedure / Sequence
- Classify the request: Identify which right the data subject is invoking. Common categories: - Access — copy of their data + information about…
- Verify identity: Per the method in ~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md. Common approaches: - Logged-in…
- Locate the data: Walk the systems list from ~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md. For each system: | System…
- Exemption analysis: Not everything gets produced or deleted. Research the applicable rule before proceeding. For each item, identify every…
- Draft the response — TWO LETTERS: > Research-connector pre-flight. Before emitting either letter or the internal exemption analysis, check whether a…
- Log it: DSARs get audited. Record: - Date received - Date identity verified - Date responded - What was produced/deleted…

## Supporting Files And Signals
- Referenced: ~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md
- Referenced: /privacy-legal:matter-workspace switch <slug>
- Referenced: practice-level
- Referenced: matter.md
- Referenced: ~/.claude/plugins/config/claude-for-legal/privacy-legal/matters/<matter-slug>/
- Referenced: Cross-matter context
- Referenced: [verify-pinpoint]
- Referenced: . Per-citation
- Signal: code block: markdown

## Source Sections
- Matter context
- Purpose
- Jurisdiction assumption
- Load the process
- Workflow
- Step 1: Classify the request
- Step 2: Verify identity
- Step 3: Locate the data
- Step 4: Exemption analysis
- Step 5: Draft the response — TWO LETTERS

## Batch Log Match
- Row: 223
- Canonical path: anthropics/claude-for-legal/privacy-legal/skills/dsar-response/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-dsar-response/mp4/claude-liam-dsar-response.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
