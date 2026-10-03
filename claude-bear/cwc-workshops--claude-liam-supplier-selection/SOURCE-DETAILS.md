# Source Details — cwc-workshops--claude-liam-supplier-selection

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Supplier Selection.
- Family: cwc-workshops
- Source sheet: /Users/nik/Documents/books/anthropics/cwc-workshops/youtube/claude-liam-supplier-selection/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/cwc-workshops/agent-decomposition/.claude/skills/supplier-selection/SKILL.md
- Name: supplier-selection
- Description: How to rank and pick a supplier for a SKU. Load this whenever a task involves choosing a supplier, comparing quotes, or creating a purchase order.

## Capabilities To Name On Screen
- How to rank and pick a supplier for a SKU
- Load this whenever a task involves choosing a supplier
- comparing quotes
- or creating a purchase order.

## Constraints / Failure Modes
- Ranking suppliers is arithmetic, not judgment. Compute it in Python via code execution — do not reason about it in prose
- | SUP-05 Granite Gear Partners | West-coast DC only. Add 2–3 days to catalog lead time for WH-EAST deliveries. |
- | SUP-07 Ridgecrest Imports | Import-only; lead times are port-congestion sensitive. Don't rely on stated lead for an urgent order. |

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: /mnt/user/data/supplier_catalog.csv
- Referenced: (supplier_id, unit_price, min_order_qty)
- Referenced: /mnt/user/data/suppliers.csv
- Referenced: supplier_id
- Referenced: lead_time_days
- Referenced: unit_price
- Referenced: min_order_qty
- Signal: code block: python

## Source Sections
- Method
- Do this in code
- Supplier-specific overrides
- Warehouse lead-time adjustments
- Expedite override
- Output

## Batch Log Match
- Row: 87
- Canonical path: anthropics/cwc-workshops/agent-decomposition/.claude/skills/supplier-selection/SKILL.md
- MP4 path: anthropics/cwc-workshops/youtube/claude-liam-supplier-selection/mp4/claude-liam-supplier-selection.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
