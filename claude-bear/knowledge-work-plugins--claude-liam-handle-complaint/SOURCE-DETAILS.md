# Source Details — knowledge-work-plugins--claude-liam-handle-complaint

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Handle Complaint.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-handle-complaint/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/small-business/skills/handle-complaint/SKILL.md
- Name: handle-complaint
- Description: Handles an incoming customer complaint end-to-end — pulls context, drafts a response, and suggests an operational fix. Accepts optional email or ticket ID argument.

## Capabilities To Name On Screen
- Handles an incoming customer complaint end-to-end — pulls context
- drafts a response
- and suggests an operational fix
- Accepts optional email or ticket ID argument.

## Constraints / Failure Modes
- Present the draft to the owner. Do NOT send
- If Gmail and HubSpot are both unreachable, ask the owner to paste the complaint text — the skill works with manual input. If PayPal is missing, skip transaction lookup…
- Never send a response without explicit owner approval. Drafts only
- Never issue refunds or credits automatically. Present the option; the owner decides
- Never close tickets or resolve disputes without owner confirmation

## Procedure / Sequence
- Load the complaint (ticket-deflector): Using the ticket-deflector skill workflow: 1. If an ID was given: pull the full thread from Gmail or HubSpot. 2. If…
- Pull context: 1. Search HubSpot for the customer's history: past purchases, prior complaints, deal stage, lifetime value. 2. Search…
- Draft response (ticket-deflector): Using the ticket-deflector skill workflow for tone-matched response: 1. Draft a reply matched to the severity and the…
- Suggest operational fix (customer-pulse): 1. Check if this complaint matches a known theme (from prior /customer-pulse-check runs or similar complaints in…

## Supporting Files And Signals
- Referenced: EMAIL_OR_TICKET_ID
- Referenced: ticket-deflector
- Referenced: /customer-pulse-check

## Source Sections
- Step 1 — Load the complaint (ticket-deflector)
- Step 2 — Pull context
- Step 3 — Draft response (ticket-deflector)
- Step 4 — Suggest operational fix (customer-pulse)
- Connector failures
- Approval gates
- Output

## Batch Log Match
- Row: 256
- Canonical path: anthropics/knowledge-work-plugins/small-business/skills/handle-complaint/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-handle-complaint/mp4/claude-liam-handle-complaint.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
