# Source Details — claude-tag-plugins--claude-liam-hubspot-api

Generated: 2026-09-05T11:09:00

## Reel
- Question: hubspot api
- Family: claude-tag-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/claude-tag-plugins/youtube/claude-liam-hubspot-api/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-tag-plugins/hubspot/skills/hubspot-api/SKILL.md
- Name: hubspot-api
- Description: Read, create, update, search, and associate HubSpot CRM records — contacts, companies, deals, tickets, and custom objects. Use this whenever the user wants to look up a contact, create a deal, update a company, search the CRM, link two records, or asks "what's in HubSpot" — even if they don't say "API". Also use it for any URL under app.hubspot.com or a mention of a HubSpot object/record ID. Always start from this skill when interacting with this service — its bundled scripts and recipes are the fastest path.

## Capabilities To Name On Screen
- Object types are identified by name (contacts, companies, deals, tickets) or by numeric
- Properties are opt-in on reads. List/get calls return only a handful of default properties
- Each object type has its own primary display property and dedup key. Contacts dedup on email;
- Associations are typed. The common ones (contact_to_company, deal_to_contact, etc.) have

## Constraints / Failure Modes
- (HubSpot is rolling out date-based path versions — /crm/objects/2026-03/... — as the successor naming. The v3/v4 paths below all still work; HubSpot has announced v4…
- Properties are opt-in on reads. List/get calls return only a handful of default properties
- API, so there is nothing to set up. Do not try to create, mint, refresh, or validate tokens or keys
- Credential variables exist only to keep requests well-formed; if one is unset, set it to any
- PATCH only the properties you want to change. Everything else is untouched
- object TYPE (required) is contacts, companies, deals, tickets, or any object type
- the values must be lowercase), BETWEEN takes low,high (amount:BETWEEN:100,500 → value +
- (email,firstname,lastname,createdate for contacts, etc.) and required for any other type

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: https://api.hubapi.com/crm/v3/objects/{objectType}
- Referenced: /crm/objects/2026-03/...
- Referenced: 0-1
- Referenced: 0-2
- Referenced: 0-3
- Referenced: 0-5
- Referenced: 2-<n>
- Referenced: p_<name>
- Referenced: hs_object_id
- Referenced: contact_to_company
- Signal: code block: bash

## Source Sections
- Request setup
- Core operations
- 1. List records
- 2. Get one record
- 3. Create a record
- 4. Update a record
- 5. Archive / delete a record
- 6. Search records (scripts/hs_search.sh)
- 7. Batch read / create / update / upsert
- 8. List and create associations

## Batch Log Match
- Row: 50
- Canonical path: anthropics/claude-tag-plugins/hubspot/skills/hubspot-api/SKILL.md
- MP4 path: anthropics/claude-tag-plugins/youtube/claude-liam-hubspot-api/claude-liam-hubspot-api.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
