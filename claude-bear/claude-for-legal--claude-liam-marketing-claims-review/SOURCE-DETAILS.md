# Source Details — claude-for-legal--claude-liam-marketing-claims-review

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Marketing Claims Review.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-marketing-claims-review/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/product-legal/skills/marketing-claims-review/SKILL.md
- Name: marketing-claims-review
- Description: >

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- Matter context. Check ## Matter workspaces in the practice-level CLAUDE.md. If Enabled is ✗ (the default for in-house users), skip the rest of this paragraph — skills…
- Comparative claims policy (allowed with substantiation / discouraged / never)
- Substantiation standard (what's required before a claim ships)
- Research the currently operative advertising and substantiation standards for the applicable jurisdictions and media (for example, FTC, NAD, state UDAP regimes, sector…
- > Only cite the standards that apply to the specific claims under review. A blanket list of every FTC guideline, NAD practice note, or sector rule makes the load-bearing…
- > No silent supplement. If a research query to the configured legal research tool returns few or no results for the applicable standard (FTC rule, NAD decision, state…
- > Tool-retrieved citations keep their source tag ([Westlaw], [CourtListener], [FTC site], [NAD], [platform policy], or the MCP tool name); web-search citations remain…
- | "The only platform that does X" | False if anyone else does X — "The first platform to..." (if true) or drop "only" |

## Procedure / Sequence
- Extract every claim: Read the copy. List every sentence or phrase that asserts a fact, makes a comparison, or promises something. Ignore…
- Classify and check: For each claim
- Check against the product: Does the product actually do what the copy says? Not a philosophical question — check the PRD or ask the PM. Common…
- Output: Prepend the work-product header from ~/.claude/plugins/config/claude-for-legal/product-legal/CLAUDE.md ## Outputs (it…

## Supporting Files And Signals
- Referenced: ~/.claude/plugins/config/claude-for-legal/product-legal/CLAUDE.md
- Referenced: /product-legal:matter-workspace switch <slug>
- Referenced: practice-level
- Referenced: matter.md
- Referenced: ~/.claude/plugins/config/claude-for-legal/product-legal/matters/<matter-slug>/
- Referenced: Cross-matter context
- Referenced: [verify-pinpoint]
- Signal: code block: markdown

## Source Sections
- Matter context
- Purpose
- Load standards
- Research the applicable standards before clearing copy
- Claim taxonomy
- Vague / subjective claims
- Specific factual claims
- Comparative claims (heightened scrutiny)
- Implied claims
- Absolute claims

## Batch Log Match
- Row: 299
- Canonical path: anthropics/claude-for-legal/product-legal/skills/marketing-claims-review/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-marketing-claims-review/mp4/claude-liam-marketing-claims-review.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
