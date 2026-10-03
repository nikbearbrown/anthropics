# Source Details — cwc-workshops--claude-liam-notify-templates

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Notify Templates.
- Family: cwc-workshops
- Source sheet: /Users/nik/Documents/books/anthropics/cwc-workshops/youtube/claude-liam-notify-templates/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/cwc-workshops/agent-decomposition/.claude/skills/notify-templates/SKILL.md
- Name: notify-templates
- Description: Fixed-format templates for Slack alerts, supplier emails, and escalations. Load this whenever the task is "notify", "alert", "email", or "tell ops".

## Capabilities To Name On Screen
- Fixed-format templates for Slack alerts
- supplier emails
- and escalations
- Load this whenever the task is "notify"
- or "tell ops".

## Constraints / Failure Modes
- Notifications are template fills, not creative writing. Do not spawn a subagent for this. Fill the slots from data you already have, then append the result to the outbox
- | Finance | Only if open-PO balance for one supplier would exceed $100k, or suspected duplicate POs. Nothing routine. | |
- + days-of-cover. Do not echo the full alert text in your reply; it's already

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: action_line
- Referenced: PO {{po_id}} placed for {{qty}} units (ETA {{eta}})
- Referenced: send_slack_alert
- Referenced: /mnt/user/sinks/outbox.jsonl
- Referenced: json.dumps
- Signal: code block: bash

## Source Sections
- Low-stock Slack alert
- Supplier email
- Escalation (human review needed)
- Routing (who gets what)
- Batch, don't spam
- How to send

## Batch Log Match
- Row: 84
- Canonical path: anthropics/cwc-workshops/agent-decomposition/.claude/skills/notify-templates/SKILL.md
- MP4 path: anthropics/cwc-workshops/youtube/claude-liam-notify-templates/mp4/claude-liam-notify-templates.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
