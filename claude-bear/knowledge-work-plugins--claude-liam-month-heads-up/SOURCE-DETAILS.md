# Source Details — knowledge-work-plugins--claude-liam-month-heads-up

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Month Heads Up.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-month-heads-up/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/small-business/skills/month-heads-up/SKILL.md
- Name: month-heads-up
- Description: Runs on the 25th — shows the next 30-day cash-flow outlook and flags anything that needs attention before month-end. Accepts optional 30 or 60 day horizon.

## Capabilities To Name On Screen
- Runs on the 25th — shows the next 30-day cash-flow outlook and flags anything that needs attention before month-end
- Accepts optional 30 or 60 day horizon.

## Constraints / Failure Modes
- If QuickBooks is unreachable, stop — the cash forecast requires QB as the source of truth. If PayPal is missing, run the forecast from QB-only data and note "PayPal not…
- Never initiate payments or send emails automatically. Surface the data and actions for the owner to take
- Never project revenue that hasn't been confirmed in QB or PayPal. Use conservative estimates only

## Procedure / Sequence
- Current cash position: Using the cash-flow-snapshot skill workflow: 1. Pull QuickBooks current cash and receivables balance. 2. Pull PayPal…
- Upcoming obligations: 1. Pull recurring expenses from QuickBooks (payroll, subscriptions, rent/lease) due in the next 30 days. 2. Pull any…
- Cash-flow forecast: 1. Project 30-day net cash: current balance + expected inflows − known obligations. 2. Identify the single tightest…
- Two things to watch: Surface no more than two specific, actionable watches: - Which invoice(s) to chase now - Which expense(s) to defer or…

## Supporting Files And Signals
- Referenced: --horizon
- Referenced: cash-flow-snapshot

## Source Sections
- Step 1 — Current cash position
- Step 2 — Upcoming obligations
- Step 3 — Cash-flow forecast
- Step 4 — Two things to watch
- Connector failures
- Approval gates
- Output

## Batch Log Match
- Row: 315
- Canonical path: anthropics/knowledge-work-plugins/small-business/skills/month-heads-up/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-month-heads-up/mp4/claude-liam-month-heads-up.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
