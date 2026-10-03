# Source Details — knowledge-work-plugins--claude-liam-crm-cleanup

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Crm Cleanup.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-crm-cleanup/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/small-business/skills/crm-cleanup/SKILL.md
- Name: crm-cleanup
- Description: Scans HubSpot for stale deals, duplicate contacts, and missing fields, then fixes what the owner approves. Accepts optional scope argument for deals, contacts, or all.

## Capabilities To Name On Screen
- Scans HubSpot for stale deals
- duplicate contacts
- and missing fields
- then fixes what the owner approves
- Accepts optional scope argument for deals

## Constraints / Failure Modes
- scope (default: all) — deals for deal audit only, contacts for contact dedup only, all for both
- ## Step 3 — Scan for missing required fields
- Apply only the changes the owner explicitly approves
- Never delete records. Not contacts, not deals, not activities. If the user asks, say the skill cannot and direct them to HubSpot
- Never change deal stage or close a deal without explicit approval. Even if evidence is strong. Flag and defer
- Never auto-merge duplicate contacts. Show side-by-side and wait for approval per pair

## Procedure / Sequence
- Scan for stale deals: If scope includes deals: 1. Pull all open deals from HubSpot. 2. Flag deals with no activity (email, call, meeting…
- Scan for duplicate contacts: If scope includes contacts: 1. Search HubSpot contacts for likely duplicates (same email, similar names, same company +…
- Scan for missing required fields: 1. Check all open deals for missing fields: close date, amount, deal stage, associated contact, next-step/notes. 2.…
- Apply approved fixes: 1. Walk through each finding from Steps 1-3. 2. Apply only the changes the owner explicitly approves. 3. Report each…

## Supporting Files And Signals
- Referenced: crm-maintenance
- Referenced: --scope

## Source Sections
- Step 1 — Scan for stale deals
- Step 2 — Scan for duplicate contacts
- Step 3 — Scan for missing required fields
- Step 4 — Apply approved fixes
- Connector failures
- Approval gates
- Output

## Batch Log Match
- Row: 179
- Canonical path: anthropics/knowledge-work-plugins/small-business/skills/crm-cleanup/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-crm-cleanup/mp4/claude-liam-crm-cleanup.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
