# Source Details — claude-tag-plugins--claude-liam-salesforce-api

Generated: 2026-09-05T11:09:00

## Reel
- Question: salesforce-api
- Family: claude-tag-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/claude-tag-plugins/youtube/claude-liam-salesforce-api/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-tag-plugins/salesforce/skills/salesforce-api/SKILL.md
- Name: salesforce-api
- Description: Query, read, create, update, and describe Salesforce records — Accounts, Contacts, Opportunities, Leads, Cases, and custom objects. Use this whenever the user wants to look up a Salesforce record, run a SOQL query, update an Opportunity, check an object's fields, or asks "what's in Salesforce" — even if they don't say "API". Also use it for any URL under *.salesforce.com / *.lightning.force.com or a mention of a Salesforce record ID or SOQL. Always start from this skill when interacting with this service — its bundled scripts and recipes are the fastest path.

## Capabilities To Name On Screen
- and describe Salesforce records — Accounts
- Opportunities
- and custom objects
- Use this whenever the user wants to look up a Salesforce record
- run a SOQL query

## Constraints / Failure Modes
- never see errorCode
- API, so there is nothing to set up. Do not try to create, mint, refresh, or validate tokens or keys
- Credential variables exist only to keep requests well-formed; if one is unset, set it to any
- The instance URL must be real — every org has its own and it's part of every request path:
- subrequest url is an absolute path that must repeat the same API version as the outer request** —
- finish — back off and retry. Be frugal: batch with Composite, select only the fields you need,
- REQUIRED_FIELD_MISSING, FIELD_CUSTOM_VALIDATION_EXCEPTION — Missing required field or a validation rule fired

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: if type == "array" then . else <projection> end
- Referenced: __c
- Referenced: __r
- Referenced: -H
- Referenced: scripts/sf_query.sh
- Referenced: Account.Name
- Referenced: SALESFORCE_INSTANCE_URL
- Referenced: SALESFORCE_ACCESS_TOKEN
- Referenced: --instance-url
- Referenced: --api-version
- Signal: code block: bash

## Source Sections
- Request setup
- Core operations
- 1. Run a SOQL query (scripts/sf_query.sh)
- 2. Full-text search (SOSL)
- 3. Read / create / update / delete one record
- 4. Upsert by external ID
- 5. Describe an sObject (schema)
- 6. Composite: several operations in one request
- 7. Check limits
- Pagination

## Batch Log Match
- Row: 63
- Canonical path: anthropics/claude-tag-plugins/salesforce/skills/salesforce-api/SKILL.md
- MP4 path: anthropics/claude-tag-plugins/youtube/claude-liam-salesforce-api/claude-liam-salesforce-api.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
