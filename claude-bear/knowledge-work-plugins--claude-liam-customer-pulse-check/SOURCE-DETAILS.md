# Source Details — knowledge-work-plugins--claude-liam-customer-pulse-check

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Customer Pulse Check.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-customer-pulse-check/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/small-business/skills/customer-pulse-check/SKILL.md
- Name: customer-pulse-check
- Description: Synthesizes themes from PayPal disputes, HubSpot tickets, and review exports into a top-3 fixable issues list with drafted response templates. Accepts optional since-date argument.

## Capabilities To Name On Screen
- Synthesizes themes from PayPal disputes
- HubSpot tickets
- and review exports into a top-3 fixable issues list with drafted response templates
- Accepts optional since-date argument.

## Constraints / Failure Modes
- Never send response emails automatically. Present drafts for owner review only
- Never close HubSpot tickets or resolve PayPal disputes without explicit owner confirmation
- Never include customer PII in the summary — use first name + last initial only

## Procedure / Sequence
- Gather feedback signals: Using the customer-pulse skill workflow: 1. Pull PayPal disputes and chargebacks for the period: reason codes, amounts…
- Theme extraction: Cluster all signals into recurring themes. For each theme: - Count how many signals mention it - Classify: Product…
- Top-3 fixable issues: Using the ticket-deflector skill workflow: Select the top 3 themes by: frequency × impact rating. For each: 1. State…
- Summary table: Format the output as

## Supporting Files And Signals
- Referenced: --since
- Referenced: YYYY-MM-DD
- Referenced: customer-pulse
- Referenced: ticket-deflector

## Source Sections
- Step 1 — Gather feedback signals
- Step 2 — Theme extraction
- Step 3 — Top-3 fixable issues
- Step 4 — Summary table
- Connector failures
- Approval gates
- Output

## Batch Log Match
- Row: 183
- Canonical path: anthropics/knowledge-work-plugins/small-business/skills/customer-pulse-check/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-customer-pulse-check/mp4/claude-liam-customer-pulse-check.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
