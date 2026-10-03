# Source Details — financial-services--claude-liam-comps-analysis

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Comps Analysis.
- Family: financial-services
- Source sheet: /Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-comps-analysis/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/agent-plugins/market-researcher/skills/comps-analysis/SKILL.md
- Name: comps-analysis
- Description: |

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- DO NOT use web search if the above MCP data sources are available
- ONLY if MCPs are unavailable: Then use Bloomberg Terminal, SEC EDGAR filings, or other institutional sources
- NEVER use web search as a primary data source - it lacks the accuracy, audit trails, and reliability required for institutional-grade analysis
- DO NOT use examples for:
- Office JS merged cell pitfall: Do NOT call .merge() then set .values on the merged range (throws InvalidArgument — range still reports its pre-merge dimensions). Instead…
- Every derived value (margin, multiple, statistic) MUST be an Excel formula referencing input cells — never a pre-computed number pasted in
- The only hardcoded values should be raw input data (revenue, EBITDA, share price, etc.) — and every one of those gets a cell comment with its source
- Why: the model must update automatically when an input changes. A hardcoded margin is a silent bug waiting to happen

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: examples/comps_example.xlsx
- Referenced: Excel.run(async (context) => {...})
- Referenced: range.formulas = [["=E7/C7"]]
- Referenced: range.values
- Referenced: range.format.*
- Referenced: cell.value = "=E7/C7"
- Referenced: .merge()
- Referenced: .values
- Referenced: cell.value = 0.687
- Signal: code block: js
- Signal: code block: excel

## Source Sections
- ⚠️ CRITICAL: Data Source Priority (READ FIRST)
- Overview
- Core Philosophy
- ⚠️ CRITICAL: Formulas Over Hardcodes + Step-by-Step Verification
- Section 1: Document Structure & Setup
- Header Block (Rows 1-3)
- Visual Convention Standards (OPTIONAL - User preferences and uploaded templates always override)
- Section 2: Operating Statistics & Financial Metrics
- Core Columns (Start with these)
- Optional Additions (Choose based on industry/purpose)

## Batch Log Match
- Row: 166
- Canonical path: anthropics/financial-services/plugins/agent-plugins/market-researcher/skills/comps-analysis/SKILL.md
- MP4 path: anthropics/financial-services/youtube/claude-liam-comps-analysis/mp4/claude-liam-comps-analysis.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
