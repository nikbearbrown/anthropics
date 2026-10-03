# Source Details — claude-tag-plugins--claude-liam-graphing

Generated: 2026-09-05T11:09:00

## Reel
- Question: graphing
- Family: claude-tag-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/claude-tag-plugins/youtube/claude-liam-graphing/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-tag-plugins/claude-tag-data-viz/skills/graphing/SKILL.md
- Name: graphing
- Description: Compose polished charts (timeseries, bar, line, area, pie, scatter, or anything else the data calls for) from tabular data using the chartkit primitives, producing PNG, SVG, or self-contained interactive HTML. Use when the user asks to chart, graph, plot, or visualize data and wants something better than raw matplotlib defaults.

## Capabilities To Name On Screen
- Compose polished charts (timeseries
- or anything else the data calls for) from tabular data using the chartkit primitives
- producing PNG
- or self-contained interactive HTML
- Use when the user asks to chart

## Constraints / Failure Modes
- zero_fill_days(pairs) rolling_mean(values, w) log_floor(values): Small data helpers for the gotchas listed below. Use them only when they fit
- Infer colors from context. Check your conversation and memory for design indicators: a tailwind config, CSS variables, or brand guidelines, and consider the semantic…
- Rotate x labels only when they would otherwise collide. Short labels stay horizontal
- A title states what the chart shows. A subtitle carries the time range or scope. The source caption says where the data came from and when. Skip any of them only…
- Legends only when there is more than one series. A single series is named by the title
- Rolling averages: rolling_mean is trailing, early points average what exists so far. Do not center it on data that ends today

## Procedure / Sequence
- Look at the data and decide what it deserves.: Shape, count, and meaning drive the choice: trends over time want lines or day bars, ranked categories want horizontal…
- Infer colors from context.: Check your conversation and memory for design indicators: a tailwind config, CSS variables, or brand guidelines, and…
- Write a short script: in your scratchpad that imports chartkit, builds the figure with plain matplotlib (or a Recharts component for…
- Render and look at the result.: Read the PNG back and check it with your own eyes before handing it over: labels legible, nothing overlapping, colors…

## Supporting Files And Signals
- Referenced: scripts/
- Referenced: sys.path
- Referenced: /path/to/graphing/scripts
- Referenced: font_css
- Referenced: stem.png
- Referenced: stem.svg
- Referenced: write_html(out, data, component_js, title, bg, font)
- Referenced: third_party/
- Referenced: window.__CHART_DATA__
- Referenced: zero_fill_days(pairs)
- Signal: code block: python
- Signal: code block: bash

## Source Sections
- The primitives
- Steps
- The shape of a chart script
- Judgement, not flags
- Gotchas the helpers exist for
- Verification

## Batch Log Match
- Row: 48
- Canonical path: anthropics/claude-tag-plugins/claude-tag-data-viz/skills/graphing/SKILL.md
- MP4 path: anthropics/claude-tag-plugins/youtube/claude-liam-graphing/claude-liam-graphing.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
