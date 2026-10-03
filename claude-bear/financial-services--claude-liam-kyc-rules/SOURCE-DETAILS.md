# Source Details — financial-services--claude-liam-kyc-rules

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Kyc Rules.
- Family: financial-services
- Source sheet: /Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-kyc-rules/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/agent-plugins/kyc-screener/skills/kyc-rules/SKILL.md
- Name: kyc-rules
- Description: Apply the firm's KYC/AML rules grid to a parsed onboarding record — assign a risk rating, list every rule outcome with the rule cited, and flag what's missing or escalation-worthy. Use after kyc-doc-parse; this skill decides nothing, it scores and routes.

## Capabilities To Name On Screen
- Apply the firm's KYC/AML rules grid to a parsed onboarding record — assign a risk rating
- list every rule outcome with the rule cited
- and flag what's missing or escalation-worthy
- Use after kyc-doc-parse
- this skill decides nothing

## Constraints / Failure Modes
- ## Step 2: Required-document check
- From the grid, list the documents required for this applicant_type at this risk rating, and mark each received / missing / expired against documents_received
- clear only if rating is low/medium, all required docs received, and no escalation rule fired. Otherwise route — this skill never approves; the escalator and a human…

## Procedure / Sequence
- Risk-rate: Compute a risk rating from the grid's factors. Typical factors and how to read them from the record: | Factor | Source…
- Required-document check: From the grid, list the documents required for this applicant_type at this risk rating, and mark each received /…
- Rule outcomes: For every rule in the grid that applies, output one row: rule id, rule text, outcome (pass | fail | n/a), and the…
- Disposition: clear only if rating is low/medium, all required docs received, and no escalation rule fired. Otherwise route — this…

## Supporting Files And Signals
- Referenced: kyc-doc-parse
- Referenced: nationality_or_jurisdiction
- Referenced: applicant_type
- Referenced: beneficial_owners
- Referenced: pep_declared
- Referenced: source_of_funds
- Referenced: documents_received
- Referenced: pass | fail | n/a
- Signal: code block: json

## Source Sections
- Step 1: Risk-rate
- Step 2: Required-document check
- Step 3: Rule outcomes
- Step 4: Disposition

## Batch Log Match
- Row: 287
- Canonical path: anthropics/financial-services/plugins/agent-plugins/kyc-screener/skills/kyc-rules/SKILL.md
- MP4 path: anthropics/financial-services/youtube/claude-liam-kyc-rules/mp4/claude-liam-kyc-rules.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
