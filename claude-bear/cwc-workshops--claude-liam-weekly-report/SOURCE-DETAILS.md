# Source Details — cwc-workshops--claude-liam-weekly-report

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Weekly Report.
- Family: cwc-workshops
- Source sheet: /Users/nik/Documents/books/anthropics/cwc-workshops/youtube/claude-liam-weekly-report/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/cwc-workshops/agent-decomposition/.claude/skills/weekly-report/SKILL.md
- Name: weekly-report
- Description: Structure and data sources for the weekly inventory report. Load this when the task is "weekly report", "Monday report", or "summarize inventory status".

## Capabilities To Name On Screen
- Structure and data sources for the weekly inventory report
- Load this when the task is "weekly report"
- "Monday report"
- or "summarize inventory status".

## Constraints / Failure Modes
- Generate the report by writing one Python script via code execution that reads the CSVs and emits markdown. Do not make per-SKU tool calls
- ## Aging-PO check (weekly only)

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: lead_time_days
- Referenced: /mnt/user/data/stock_levels.csv
- Referenced: /mnt/user/data/products.csv
- Referenced: on_hand / avg_daily_sales
- Referenced: /mnt/user/data/sales_history.csv
- Referenced: /mnt/user/sinks/purchase_orders.jsonl
- Signal: code block: markdown

## Source Sections
- Structure
- Stockouts (on_hand = 0)
- Low Stock (below reorder point)
- Open POs
- Forecast Risk
- Operating cadence (which report is being asked for)
- Aging-PO check (weekly only)
- Data sources
- Do this in code

## Batch Log Match
- Row: 88
- Canonical path: anthropics/cwc-workshops/agent-decomposition/.claude/skills/weekly-report/SKILL.md
- MP4 path: anthropics/cwc-workshops/youtube/claude-liam-weekly-report/mp4/claude-liam-weekly-report.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
