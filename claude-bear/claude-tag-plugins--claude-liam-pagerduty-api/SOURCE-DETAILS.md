# Source Details — claude-tag-plugins--claude-liam-pagerduty-api

Generated: 2026-09-05T11:09:00

## Reel
- Question: pagerduty-api
- Family: claude-tag-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/claude-tag-plugins/youtube/claude-liam-pagerduty-api/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-tag-plugins/pagerduty/skills/pagerduty-api/SKILL.md
- Name: pagerduty-api
- Description: Query and manage PagerDuty — find out who's on call, list and manage incidents, read escalation policies and schedules, trace who got paged and why, acknowledge/resolve/snooze/escalate incidents, and create or update services. Use this whenever the user mentions PagerDuty, on-call, paging, escalation, an incident ID like `PXXXXXX` or `Q...`, asks "who's on call", "page the on-call", "ack this incident", "why wasn't I paged", or pastes a pagerduty.com URL — even if they don't say "API". Always start from this skill when interacting with this service — its bundled scripts and recipes are the fastest path.

## Capabilities To Name On Screen
- Query and manage PagerDuty — find out who's on call
- list and manage incidents
- read escalation policies and schedules
- trace who got paged and why
- acknowledge/resolve/snooze/escalate incidents

## Constraints / Failure Modes
- API, so there is nothing to set up. Do not try to create, mint, refresh, or validate tokens or keys
- Credential variables exist only to keep requests well-formed; if one is unset, set it to any
- only on user tokens; account-level tokens can verify with /abilities
- email via /users?query= to user_ids[] (repeatable). Name lookups (here and --service) must
- earliest returns only the next-up entry per policy
- — Credential rejected. Body is empty — print the status. Header must be Authorization: Token token=.... If it persists, the credential isn't configured — report it
- — Forbidden. Read-only credential mutating, or scoped to a team that doesn't own the resource

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: Q...
- Referenced: https://api.pagerduty.com
- Referenced: https://events.pagerduty.com
- Referenced: api.pagerduty.com
- Referenced: events.pagerduty.com
- Referenced: jq '.user | {id, name, email}'
- Referenced: /users/me
- Referenced: /abilities
- Referenced: -g
- Referenced: -w '%{http_code}'
- Signal: code block: bash

## Source Sections
- Request setup
- Core operations
- 1. Who's on call (scripts/pd_oncall.sh)
- 2. List open incidents
- 3. Get one incident
- 4. Who actually got paged? (log entries)
- 5. Acknowledge / resolve / escalate / snooze / note
- 6. Trace routing: service → escalation policy → schedule
- 7. Create an incident
- 8. Trigger an alert via Events API v2

## Batch Log Match
- Row: 57
- Canonical path: anthropics/claude-tag-plugins/pagerduty/skills/pagerduty-api/SKILL.md
- MP4 path: anthropics/claude-tag-plugins/youtube/claude-liam-pagerduty-api/claude-liam-pagerduty-api.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
