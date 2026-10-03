# Source Details — claude-for-legal--claude-liam-diligence-issue-extraction

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Diligence Issue Extraction.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-diligence-issue-extraction/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/corporate-legal/skills/diligence-issue-extraction/SKILL.md
- Name: diligence-issue-extraction
- Description: >

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- Matter context. Check ## Matter workspaces in the practice-level CLAUDE.md. If Enabled is ✗ (the default for in-house users), skip the rest of this paragraph — skills…
- Change of control provision (triggered by this deal? consent required?)
- > Source attribution. Where a finding references a statute, regulation, case, or regulator action — e.g., a change-of-control provision analyzed under an applicable law…
- > When disagreeing with a user's cited statute, quote the text or decline to characterize it. If the user (or a deal-team note, or a sell-side disclosure) cites a…
- > No silent supplement. If a research query to the configured legal research tool returns few or no results for a legal basis the finding needs (e.g., the rule governing…
- Recommendation: [price adjustment / indemnity / consent required / rep & warranty / walk]
- 🟡 Yellow: Needs attention, solvable. Consent required but likely obtainable. Open source requiring remediation. Employment classification risk
- Shareholder vote / other closing action — §280G cleansing votes, required stockholder consents, required board resolutions, appraisal-rights notice periods, conversion…

## Procedure / Sequence
- Inventory the VDR: If VDR MCP (Box/Intralinks/Datasite) is connected, pull the index. Map VDR folders to diligence request list…
- Apply materiality filter: Per ~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md / deal-context thresholds. Don't review…
- Extract issues: For each document read, check against the standard diligence concerns for its category: Material contracts — standard…
- State each finding: > Source attribution. Where a finding references a statute, regulation, case, or regulator action — e.g., a…
- Assemble per category: Group findings by request list category. Within category, sort by severity. `markdown [WORK-PRODUCT HEADER — per plugin…

## Supporting Files And Signals
- Referenced: ~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md
- Referenced: ai-tool-handoff
- Referenced: /corporate-legal:matter-workspace switch <slug>
- Referenced: practice-level
- Referenced: matter.md
- Referenced: ~/.claude/plugins/config/claude-for-legal/corporate-legal/matters/<matter-slug>/
- Referenced: Cross-matter context
- Referenced: ## Outputs → Dashboard offer for data-heavy outputs
- Signal: code block: markdown

## Source Sections
- Matter context
- Purpose
- Load context
- Workflow
- Step 1: Inventory the VDR
- VDR Inventory: [Deal code]
- Step 2: Apply materiality filter
- Step 3: Extract issues
- Step 4: State each finding
- Step 5: Assemble per category

## Batch Log Match
- Row: 212
- Canonical path: anthropics/claude-for-legal/corporate-legal/skills/diligence-issue-extraction/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-diligence-issue-extraction/mp4/claude-liam-diligence-issue-extraction.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
