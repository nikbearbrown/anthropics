# Source Details — knowledge-work-plugins--claude-liam-build-dashboard

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Build Dashboard.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-build-dashboard/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/data/skills/build-dashboard/SKILL.md
- Name: build-dashboard
- Description: Build an interactive HTML dashboard with charts, filters, and tables. Use when creating an executive overview with KPI cards, turning query results into a shareable self-contained report, building a team monitoring snapshot, or needing multiple charts with filters in one browser-openable file.

## Capabilities To Name On Screen
- Build an interactive HTML dashboard with charts
- Use when creating an executive overview with KPI cards
- turning query results into a shareable self-contained report
- building a team monitoring snapshot
- or needing multiple charts with filters in one browser-openable file.

## Constraints / Failure Modes
- Build a self-contained interactive HTML dashboard with charts, filters, tables, and professional styling. Opens directly in a browser -- no server or dependencies…
- No external data fetches required
- | 10,000 - 100,000 rows | Pre-aggregate server-side. Embed only aggregated data. |
- Avoid rebuilding the entire DOM on filter change -- update only changed elements
- // Render only pageData

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: sales_dashboard.html
- Referenced: ${sign}${pctChange.toFixed(1)}% vs prior period
- Referenced: kpi-change ${pctChange >= 0 ? 'positive' : 'negative'}
- Referenced: $${(value / 1e6).toFixed(1)}M
- Referenced: $${(value / 1e3).toFixed(1)}K
- Referenced: $${value.toFixed(0)}
- Referenced: ${value.toFixed(1)}%
- Referenced: ${(value / 1e6).toFixed(1)}M
- Referenced: ${(value / 1e3).toFixed(1)}K
- Referenced: ${context.dataset.label}: ${formatValue(context.parsed.y, 'currency')}
- Signal: code block: html
- Signal: code block: javascript
- Signal: code block: css

## Source Sections
- Usage
- Workflow
- 1. Understand the Dashboard Requirements
- 2. Gather the Data
- 3. Design the Dashboard Layout
- 4. Build the HTML Dashboard
- 5. Implement Chart Types
- 6. Add Interactivity
- 7. Save and Open
- Base Template

## Batch Log Match
- Row: 114
- Canonical path: anthropics/knowledge-work-plugins/data/skills/build-dashboard/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-build-dashboard/mp4/claude-liam-build-dashboard.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
