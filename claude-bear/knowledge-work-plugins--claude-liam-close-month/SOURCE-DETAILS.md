# Source Details — knowledge-work-plugins--claude-liam-close-month

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Close Month.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-close-month/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/small-business/skills/close-month/SKILL.md
- Name: close-month
- Description: Closes the month — reconciles QB vs payment processors, flags gaps, writes P&L narrative, exports close packet. Accepts optional month and save-to arguments.

## Capabilities To Name On Screen
- Closes the month — reconciles QB vs payment processors
- writes P&L narrative
- exports close packet
- Accepts optional month and save-to arguments.

## Constraints / Failure Modes
- Unmatched processor settlements — money came in via PayPal/Stripe/Square but never landed in QB
- Wait for owner to triage flagged items before generating the narrative. Do not auto-categorize or auto-delete
- If QuickBooks is unreachable, stop — reconciliation requires QB as the source of truth. If a payment processor (PayPal, Stripe, Square) is unreachable, run…
- Never auto-fix flagged items. Always show the gap, recommend an action, wait for the owner
- Never delete duplicates without explicit confirmation. Show both records side-by-side

## Procedure / Sequence
- Reconcile: Trigger the month-end-prep skill workflow: 1. Pull all QuickBooks transactions for the target month. 2. Pull…
- Flag suspicious entries: Surface in the same report: - Uncategorized transactions — QB entries with no category - Suspicious duplicates — same…
- P&L narrative: After triage, generate a plain-English P&L narrative: Numbers come from QB; the why comes from cross-referencing top…
- Export the close packet: Generate two files: 1. close-packet-{YYYY-MM}.xlsx — multi-tab workbook: - Reconciliation — QB ↔ processor match table…

## Supporting Files And Signals
- Referenced: --month
- Referenced: YYYY-MM
- Referenced: --save-to
- Referenced: month-end-prep
- Referenced: close-packet-{YYYY-MM}.xlsx
- Referenced: close-packet-{YYYY-MM}.pdf
- Referenced: close-packet-2026-04.xlsx

## Source Sections
- Step 1 — Reconcile
- Step 2 — Flag suspicious entries
- Step 3 — P&L narrative
- Step 4 — Export the close packet
- Connector failures
- Approval gates
- Output

## Batch Log Match
- Row: 152
- Canonical path: anthropics/knowledge-work-plugins/small-business/skills/close-month/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-close-month/mp4/claude-liam-close-month.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
