# Source Details — financial-services--claude-liam-earnings-preview-single

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Earnings Preview Single.
- Family: financial-services
- Source sheet: /Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-earnings-preview-single/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/partner-built/spglobal/skills/earnings-preview-beta/SKILL.md
- Name: earnings-preview-single
- Description: Generate a concise 4-5 page equity research earnings preview for a single company. Analyzes the most recent earnings transcript, competitor landscape, valuation, and recent news to produce a professional HTML report.

## Capabilities To Name On Screen
- Generate a concise 4-5 page equity research earnings preview for a single company
- Analyzes the most recent earnings transcript
- competitor landscape
- and recent news to produce a professional HTML report.

## Constraints / Failure Modes
- Data Sources (ZERO EXCEPTIONS): The ONLY permitted data sources are Kensho Grounding MCP (search) and S&P Global MCP (kfinance). Absolutely NO other tools, data sources…
- Do NOT use WebSearch, WebFetch, web_search, brave_search, google_search, or ANY generic web/internet search tool — even if Kensho is slow, returns no results, or is…
- Do NOT use any browser, URL fetch, or web scraping tool
- If Kensho Grounding returns no results for a query, try rephrasing the query or note "data not available" in the report. NEVER fall back to web search as an alternative
- Every piece of information in the report must be traceable to either a kfinance MCP function call or a Kensho search call. If it cannot be sourced to one of these two…
- Critical Rule: You MUST complete ALL research and data collection (Phases 1-5) BEFORE writing any part of the report
- Intermediate File Rule: All raw data from MCP tool calls MUST be written to files in /tmp/earnings-preview/ immediately after each tool call returns — before moving to…
- Fiscal Quarter Rule: NEVER infer the fiscal quarter from the calendar report date. Many companies have non-standard fiscal years (e.g., Walmart's FY ends Jan 31, so a…

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: web_search
- Referenced: brave_search
- Referenced: google_search
- Referenced: /tmp/earnings-preview/
- Referenced: mkdir -p /tmp/earnings-preview
- Referenced: get_next_earnings_from_identifiers
- Referenced: get_earnings_from_identifiers
- Referenced: get_financial_line_item_from_identifiers
- Referenced: get_consensus_estimates_from_identifiers
- Referenced: <a href="#ref-N" class="data-ref">
- Signal: code block: html

## Source Sections
- Phase 1: Company Profile & Setup
- Phase 2: Earnings Transcript Analysis (MANDATORY — COMPLETE BEFORE WRITING)
- Phase 3: Competitor Analysis
- Phase 4: News, Estimates & Sector Intelligence (via Kensho Grounding)
- Phase 5: Financial Data Collection
- Phase 6: Verification & Calculations (MANDATORY — DO NOT SKIP)
- Phase 7: Generate the HTML Report
- Report Structure (4-5 pages total)
- Phase 8: Output
- Writing Guidelines

## Batch Log Match
- Row: 226
- Canonical path: anthropics/financial-services/plugins/partner-built/spglobal/skills/earnings-preview-beta/SKILL.md
- MP4 path: anthropics/financial-services/youtube/claude-liam-earnings-preview-single/mp4/claude-liam-earnings-preview-single.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
