# Source Details — knowledge-work-plugins--claude-liam-business-pulse

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Business Pulse.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-business-pulse/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/small-business/skills/business-pulse/SKILL.md
- Name: business-pulse
- Description: >

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- Dispatch all connector calls in a single parallel batch — see reference/data_sources.md for the exact tool-to-metric mapping. Do not pull serially; latency turns a…
- If a connector errors or returns no data, record it internally and move on. Never block the pulse on a single bad integration
- QuickBooks fallback: if QBO returns an unexpected state (account not connected, sync pending, empty response), mark the Cash section "n/a — QuickBooks unavailable" and…
- Gmail fallback: Gmail auth is intermittently flaky. If the call errors, skip the Watch List section silently and note "Gmail unavailable" in the appendix — do not…
- Scan for actionable items. Every risk entry must name a specific record and a next step — "some overdue invoices" is useless; "$3,400 from Acme Corp, 47 days overdue, no…
- Use the exact template in reference/output_template.md. Include only sections where real data exists — omit headers for connectors that weren't available. Adapt depth to…
- Numbers lead, words follow. Never write "revenue is healthy" — write "$43k this month, ▲ 8% MoM" and let the owner judge
- "Should I post this to your Slack?" (only if Slack is connected and the user confirms — Slack write requires explicit approval)

## Procedure / Sequence
- Pull data in parallel: Dispatch all connector calls in a single parallel batch — see reference/data_sources.md for the exact tool-to-metric…
- Compute metrics: Read reference/thresholds.md for red/yellow/green cutoffs. Compute: - AR aging — open QuickBooks invoices grouped by…
- Flag risks proactively: Scan for actionable items. Every risk entry must name a specific record and a next step — "some overdue invoices" is…
- Compose the output: Use the exact template in reference/output_template.md. Include only sections where real data exists — omit headers for…
- Export and share (once): After presenting the pulse, offer once: - "Want me to save this as a file?" (use Files connector if available)…

## Supporting Files And Signals
- Referenced: reference/data_sources.md
- Referenced: reference/thresholds.md
- Referenced: reference/output_template.md
- Referenced: reference/gotchas.md
- Referenced: reference/

## Source Sections
- Step 1 — Pull data in parallel
- Step 2 — Compute metrics
- Step 3 — Flag risks proactively
- Step 4 — Compose the output
- Step 5 — Export and share (once)
- Scope variants
- What not to do
- Reference files

## Batch Log Match
- Row: 125
- Canonical path: anthropics/knowledge-work-plugins/small-business/skills/business-pulse/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-business-pulse/mp4/claude-liam-business-pulse.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
