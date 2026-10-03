# Source Details — knowledge-work-plugins--claude-liam-invoice-chase

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Invoice Chase.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-invoice-chase/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/small-business/skills/invoice-chase/SKILL.md
- Name: invoice-chase
- Description: >

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- ## Setup (first run only)
- Do not ask again on subsequent runs
- transaction_status: S (settled only — filters out pending and denied transactions that inflate result size and increase rate-limit risk)
- If the retry also returns 429, skip the PayPal cross-reference entirely for this run. Flag all customers in the batch as "PayPal unavailable — verify manually" in the…
- Send or queue — only after approval
- Never send without explicit approval
- Never send or queue a draft without explicit owner approval. Present all drafts first; wait for the go-ahead
- Never include a customer who paid in the last 14 days. Flag as "possibly paid — verify" instead

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: transaction_status: S
- Referenced: good-payer
- Referenced: occasionally-late
- Referenced: repeat-late
- Referenced: reference/

## Source Sections
- Quick start
- Setup (first run only)
- Workflow
- Approval gates
- Reference

## Batch Log Match
- Row: 277
- Canonical path: anthropics/knowledge-work-plugins/small-business/skills/invoice-chase/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-invoice-chase/mp4/claude-liam-invoice-chase.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
