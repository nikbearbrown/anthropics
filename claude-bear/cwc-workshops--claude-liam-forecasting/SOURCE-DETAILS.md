# Source Details — cwc-workshops--claude-liam-forecasting

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Forecasting.
- Family: cwc-workshops
- Source sheet: /Users/nik/Documents/books/anthropics/cwc-workshops/youtube/claude-liam-forecasting/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/cwc-workshops/agent-decomposition/.claude/skills/forecasting/SKILL.md
- Name: forecasting
- Description: How to produce a demand forecast for a SKU, and when to delegate that to a subagent vs. compute it yourself. Load this for any task involving "forecast", "how much will we sell", "next month", promos, or seasonal SKUs.

## Capabilities To Name On Screen
- How to produce a demand forecast for a SKU
- and when to delegate that to a subagent vs
- compute it yourself
- Load this for any task involving "forecast"
- "how much will we sell"

## Constraints / Failure Modes
- Do not rely on rolling-mean alone — that's pre-promo demand
- Feed {forecast_qty, confidence, flags} into the reorder-policy skill. In particular: if confidence < 0.6, reorder-policy says escalate, don't auto-order. Do not drop the…
- confidence 0.41 < 0.6 → per reorder-policy, do not create a PO. Escalate via notify-templates with the flags, recommend ~2,100 baseline + note that promo uplift could be…

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: is_seasonal
- Referenced: promo_next_month
- Referenced: get_stock_level
- Referenced: get_sales_velocity
- Referenced: /mnt/user/data/
- Referenced: {forecast_qty, confidence, method, flags}
- Referenced: callable_agents
- Referenced: confidence ≤ 0.55
- Referenced: promo_next_month=1
- Referenced: flags: ["promo_uplift_uncertain"]
- Signal: code block: bash

## Source Sections
- Path A — compute it yourself (code execution)
- Path B — spawn a forecaster subagent
- Seasonal calendar (sanity-check your numbers)
- Promotional handling
- What to do with the result
- Worked example (Path B)

## Batch Log Match
- Row: 78
- Canonical path: anthropics/cwc-workshops/agent-decomposition/.claude/skills/forecasting/SKILL.md
- MP4 path: anthropics/cwc-workshops/youtube/claude-liam-forecasting/mp4/claude-liam-forecasting.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
