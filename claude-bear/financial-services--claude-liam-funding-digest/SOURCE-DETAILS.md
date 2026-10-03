# Source Details — financial-services--claude-liam-funding-digest

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Funding Digest.
- Family: financial-services
- Source sheet: /Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-funding-digest/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/partner-built/spglobal/skills/funding-digest/SKILL.md
- Name: funding-digest
- Description: Generate a polished one-page PowerPoint slide summarizing key takeaways from recent funding rounds and notable capital markets activity across a user's watched sectors or companies. Use this skill when the user asks for a deal flow summary, weekly recap, funding digest, transaction roundup, or capital markets briefing. Triggers on: 'deal flow digest', 'weekly funding recap', 'deal roundup', 'transaction summary this week', 'what happened in [sector] this week', 'capital markets update', or any request to compile recent funding activity into a briefing slide. Produces a professional single-slide PPTX with key takeaways, valuation data, and Capital IQ deal links.

## Capabilities To Name On Screen
- Use this skill when the user asks for a deal flow summary
- weekly recap
- funding digest
- transaction roundup
- or capital markets briefing

## Constraints / Failure Modes
- You MUST include the following disclaimer text in the powerpoint footer. This is not optional — the report is incomplete without it:
- "Operating Subsidiary" → The company exists but is owned by a parent. It will return zero funding rounds. Note this in the digest as context (e.g., "acquired by…
- ### Rule 1: Never trust empty results without a fallback
- The summary tool is faster but less reliable — it can return errors or incomplete data even when detailed rounds exist. Always use the detailed rounds tool as the…
- Using the wrong role returns empty results silently. For deal flow digests, you almost always want company_raising_funds. Only use the investor role when specifically…
- Expand via competitors (using only the ✅ resolved seeds):
- If the user provides specific companies, add those directly but still run them through the pre-validation triage. Never skip validation — even well-known brand names can…
- Log the company as "no data" only after exhausting fallbacks

## Procedure / Sequence
- Establish Coverage & Period: Determine what the digest should cover. There are two setups: Returning user (has a watchlist): If the user has…
- Build the Company Universe: For each sector specified, build a company universe using a validated bootstrapping approach: 1. Seed companies from…
- Pull Funding Rounds: For all companies in the universe: Process in batches of 15–20 if the universe is large. After each batch, identify…
- Pull Company Context for Notable Deals: For any company involved in a significant deal (large round, notable valuation shift), get a brief description: This…
- Identify Highlights & Trends: Before designing the slide, analyze the data to surface the story: Flag as "Notable": - Rounds ≥ $100M - Down rounds…
- Generate Company Logos: For each company featured in the key takeaways or notable deals, generate a logo using a two-tier local pipeline. Do…
- Generate the One-Page PPTX: Read /mnt/skills/public/pptx/SKILL.md and /mnt/skills/public/pptx/pptxgenjs.md before creating the slide. Create a…
- QA the Slide: Follow the QA process from the PPTX skill: 1. Content QA: python -m markitdown deal-flow-digest.pptx — verify all text…

## Supporting Files And Signals
- Referenced: /mnt/skills/public/pptx/SKILL.md
- Referenced: pptxgenjs.md
- Referenced: get_info_from_identifiers
- Referenced: references/sector-seeds.md
- Referenced: company_id
- Referenced: get_rounds_of_funding_from_identifiers
- Referenced: get_info_from_identifiers(identifiers=["Company"])
- Referenced: get_funding_summary_from_identifiers
- Referenced: company_raising_funds
- Referenced: company_investing_in_round_of_funding
- Signal: code block: bash
- Signal: code block: javascript

## Source Sections
- When to Use
- Nested Skills
- Entity Resolution & Tool Robustness
- Rule 0: Pre-validate ALL identifiers before querying funding
- Rule 1: Never trust empty results without a fallback
- Rule 2: Subsidiaries have no funding rounds
- Rule 3: Use get_rounds_of_funding_from_identifiers as the primary tool, not get_funding_summary_from_identifiers
- Rule 4: Batch carefully and validate
- Rule 5: The role parameter is critical
- Rule 6: Identifier resolution is case-insensitive but spelling-sensitive

## Batch Log Match
- Row: 249
- Canonical path: anthropics/financial-services/plugins/partner-built/spglobal/skills/funding-digest/SKILL.md
- MP4 path: anthropics/financial-services/youtube/claude-liam-funding-digest/mp4/claude-liam-funding-digest.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
