# Source Details — knowledge-work-plugins--claude-liam-cash-flow-snapshot

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Cash Flow Snapshot.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-cash-flow-snapshot/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/small-business/skills/cash-flow-snapshot/SKILL.md
- Name: cash-flow-snapshot
- Description: >

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- Required columns (flexible naming): date, amount, type (income or expense), description
- from the actual payment variance — do not assume ±30%
- Thin data warning: "Only 2 payments on record for Customer Y — confidence
- No-connector warning: "Running on CSV data only — no real-time AP or
- No destructive actions — this skill is read-only. No approval gate required

## Procedure / Sequence
- Identify available data sources: Check which connectors are live. Try in this order: 1. QuickBooks — primary source for AR aging, AP, and fixed costs 2.…
- Pull the data: From QuickBooks: - AR aging report: customer name, invoice amount, invoice date, due date, days outstanding - AP…
- Compute historical payment timing: For each AR customer (or income source from CSV), calculate: - Mean payment lag — average days from invoice/transaction…
- Build the 30/60/90-day forecast: Produce three time windows: 0–30 days, 31–60 days, 61–90 days. For each window, compute: | Line | Method | |---|---| |…
- Flag named risks: Scan for conditions that push the low-band estimate negative or create a liquidity crunch. For each risk found, produce…
- Deliver outputs: Chat summary (always): XLSX workbook (always): Read xlsx/SKILL.md before generating. Produce a workbook with three…

## Supporting Files And Signals
- Referenced: xlsx/SKILL.md
- Referenced: cash-flow-snapshot-[YYYY-MM-DD].xlsx
- Referenced: reference/gotchas.md
- Referenced: reference/examples/worked-example.md
- Referenced: reference/

## Source Sections
- Workflow
- Step 1 — Identify available data sources
- Step 2 — Pull the data
- Step 3 — Compute historical payment timing
- Step 4 — Build the 30/60/90-day forecast
- Step 5 — Flag named risks
- Step 6 — Deliver outputs
- Approval gates
- Reference files

## Batch Log Match
- Row: 134
- Canonical path: anthropics/knowledge-work-plugins/small-business/skills/cash-flow-snapshot/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-cash-flow-snapshot/mp4/claude-liam-cash-flow-snapshot.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
