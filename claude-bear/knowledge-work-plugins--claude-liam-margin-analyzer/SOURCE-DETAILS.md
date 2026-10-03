# Source Details — knowledge-work-plugins--claude-liam-margin-analyzer

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Margin Analyzer.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-margin-analyzer/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/small-business/skills/margin-analyzer/SKILL.md
- Name: margin-analyzer
- Description: >

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- correlates with ~3% volume drop"). Surfaces analysis only — does not
- If QuickBooks is connected but COGS = $0 across all periods, do not use $0 as the cost input. Surface this to the owner:
- If only one data source is available, note the limitation in the output
- Keep it factual. Do not say "you should raise prices" or "consider lowering your price." The owner is looking at data to make their own call
- This is intentional. Pricing decisions have real business consequences and depend on context only the owner knows (competitive positioning, customer relationships, cash…

## Procedure / Sequence
- Pre-flight check: QuickBooks: Call company-info to verify the industry field is populated. If it's missing or "Unknown", ask: "I need…
- Clarify scope: Ask the owner two questions: 1. "Which products or services do you want to analyze?" - All of them, or a specific…
- Pull cost data (QuickBooks): Fetch from QuickBooks using profit-loss-quickbooks-account: - Date range: Last 12 months (or full history if less is…
- Pull revenue data (PayPal / Square): Fetch from list_transactions (PayPal) or make_api_request (Square): - Date range: Match the cost data window (last 12…
- Compute unit economics: For each product/service in scope, calculate: | Metric | Formula | |---|---| | Revenue | Sum of transaction amounts for…
- Benchmark: Layer in context to make the numbers meaningful: - Inflation: Note relevant cost trends if discussing input cost…
- Pricing scenarios: Build a table for each product/service showing three price-change scenarios: | Scenario | New Price | Projected…
- Present the analysis: Structure the output as: Structure the output with an H2 header showing the business name and date range, followed by…

## Supporting Files And Signals
- Referenced: company-info
- Referenced: quickbooks-profile-info-update
- Referenced: reference/gotchas.md
- Referenced: reference/csv-schema.md
- Referenced: profit-loss-quickbooks-account
- Referenced: list_transactions
- Referenced: make_api_request
- Referenced: reference/industry-benchmarks.md
- Referenced: reference/examples/
- Referenced: reference/

## Source Sections
- Quick start
- Workflow
- Step 1: Pre-flight check
- Step 2: Clarify scope
- Step 3: Pull cost data (QuickBooks)
- Step 4: Pull revenue data (PayPal / Square)
- Step 5: Compute unit economics
- Step 6: Benchmark
- Step 7: Pricing scenarios
- Step 8: Present the analysis

## Batch Log Match
- Row: 298
- Canonical path: anthropics/knowledge-work-plugins/small-business/skills/margin-analyzer/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-margin-analyzer/mp4/claude-liam-margin-analyzer.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
