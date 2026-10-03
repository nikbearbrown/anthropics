# Source Details — cwc-workshops--claude-liam-reorder-policy

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Reorder Policy.
- Family: cwc-workshops
- Source sheet: /Users/nik/Documents/books/anthropics/cwc-workshops/youtube/claude-liam-reorder-policy/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/cwc-workshops/agent-decomposition/.claude/skills/reorder-policy/SKILL.md
- Name: reorder-policy
- Description: How to decide whether and how much to reorder a SKU. Load this whenever a task involves reorder recommendations, purchase orders, or "should we restock" questions.

## Capabilities To Name On Screen
- How to decide whether and how much to reorder a SKU
- Load this whenever a task involves reorder recommendations
- purchase orders
- or "should we restock" questions.

## Constraints / Failure Modes
- | forecast_qty, confidence, flags | From the forecasting skill, only if the task looks forward more than 14 days or mentions a promo/season |
- Confidence guard. If you obtained a forecast and confidence < 0.6, do not place a PO automatically. Instead:
- Trending toward reorder — note only, no action
- Do not place a second PO for a SKU that already has an open PO covering the
- When you only recommend (no side-effect requested), return a structured ReorderDecision:

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: on_hand
- Referenced: /mnt/user/data/stock_levels.csv
- Referenced: reorder_point
- Referenced: /mnt/user/data/products.csv
- Referenced: avg_daily_sales
- Referenced: units_sold
- Referenced: /mnt/user/data/sales_history.csv
- Referenced: lead_time_days
- Referenced: forecast_qty
- Referenced: on_hand < reorder_point
- Signal: code block: json

## Source Sections
- Inputs you need
- Decision rules
- Worked example
- Prioritization (when many SKUs are at risk)
- Transfer vs reorder
- Compliance
- Output

## Batch Log Match
- Row: 85
- Canonical path: anthropics/cwc-workshops/agent-decomposition/.claude/skills/reorder-policy/SKILL.md
- MP4 path: anthropics/cwc-workshops/youtube/claude-liam-reorder-policy/mp4/claude-liam-reorder-policy.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
