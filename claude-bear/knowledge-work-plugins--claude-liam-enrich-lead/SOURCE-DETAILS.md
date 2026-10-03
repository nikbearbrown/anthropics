# Source Details — knowledge-work-plugins--claude-liam-enrich-lead

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Enrich Lead.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-enrich-lead/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/partner-built/apollo/skills/enrich-lead/SKILL.md
- Name: enrich-lead
- Description: Instant lead enrichment. Drop a name, company, LinkedIn URL, or email and get the full contact card with email, phone, title, company intel, and next actions.

## Capabilities To Name On Screen
- Instant lead enrichment
- LinkedIn URL
- or email and get the full contact card with email
- company intel
- and next actions.

## Constraints / Failure Modes
- No explicit constraints extracted.

## Procedure / Sequence
- Parse Input: From "$ARGUMENTS", extract every identifier available: - First name, last name - Company name or domain - LinkedIn URL…
- Enrich the Person: > Credit warning: Tell the user enrichment consumes 1 Apollo credit before calling. Use…
- Enrich Their Company: Use mcp__claude_ai_Apollo_MCP__apollo_organizations_enrich with the person's company domain to pull firmographic…
- Present the Contact Card: Format the output exactly like this: --- [Full Name] | [Title] [Company Name] · [Industry] · [Employee Count] employees…
- Offer Next Actions: Ask the user which action to take: 1. Save to Apollo — Create this person as a contact via…

## Supporting Files And Signals
- Referenced: /apollo:enrich-lead Tim Zheng at Apollo
- Referenced: /apollo:enrich-lead https://www.linkedin.com/in/timzheng
- Referenced: /apollo:enrich-lead sarah@stripe.com
- Referenced: /apollo:enrich-lead Jane Smith, VP Engineering, Notion
- Referenced: /apollo:enrich-lead CEO of Figma
- Referenced: mcp__claude_ai_Apollo_MCP__apollo_mixed_people_api_search
- Referenced: mcp__claude_ai_Apollo_MCP__apollo_people_match
- Referenced: first_name
- Referenced: last_name
- Referenced: organization_name

## Source Sections
- Examples
- Step 1 — Parse Input
- Step 2 — Enrich the Person
- Step 3 — Enrich Their Company
- Step 4 — Present the Contact Card
- Step 5 — Offer Next Actions

## Batch Log Match
- Row: 228
- Canonical path: anthropics/knowledge-work-plugins/partner-built/apollo/skills/enrich-lead/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-enrich-lead/mp4/claude-liam-enrich-lead.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
