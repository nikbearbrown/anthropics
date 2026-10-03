# Source Details — knowledge-work-plugins--claude-liam-customer-pulse

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Customer Pulse.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-customer-pulse/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/small-business/skills/customer-pulse/SKILL.md
- Name: customer-pulse
- Description: >

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- Pull PayPal disputes. Fetch disputes opened in the window. If the PayPal API returns a rate-limit error, skip and add PayPal: rate-limited — not included to the Sources…
- Pull HubSpot tickets and feedback. Fetch open and recently closed tickets. If 0 tickets exist, record HubSpot tickets: 0 and continue — do not surface a warning
- Accept pasted reviews (optional). If the user pastes Google or Yelp review text, include it in the source pool tagged as [Review]. No connector required
- Extract themes. Group all evidence into 3–5 recurring themes. Each theme must include:
- Verbatim quotes are non-negotiable — never paraphrase. See reference/gotchas.md for the verbatim anti-pattern
- This skill is read-only — it does not post, send, reply, or modify any records. No approval gate is required

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: PayPal: rate-limited — not included
- Referenced: search_conversations
- Referenced: get_conversation
- Referenced: conversation_parts
- Referenced: author.type === 'user'
- Referenced: author.type
- Referenced: reference/

## Source Sections
- Quick start
- Workflow
- Approval gates
- Reference

## Batch Log Match
- Row: 182
- Canonical path: anthropics/knowledge-work-plugins/small-business/skills/customer-pulse/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-customer-pulse/mp4/claude-liam-customer-pulse.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
