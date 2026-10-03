# Source Details — knowledge-work-plugins--claude-liam-build-zoom-rest-api-app

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Build Zoom Rest Api App.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-rest-api-app/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/partner-built/zoom-plugin/skills/rest-api/SKILL.md
- Name: build-zoom-rest-api-app
- Description: Reference skill for Zoom REST API. Use after choosing an API-based workflow when you need endpoint selection, resource-management patterns, OAuth requirements, rate-limit awareness, or API error debugging.

## Capabilities To Name On Screen
- Reference skill for Zoom REST API
- Use after choosing an API-based workflow when you need endpoint selection
- resource-management patterns
- OAuth requirements
- rate-limit awareness

## Constraints / Failure Modes
- For S2S OAuth, use an explicit host user ID or email in the path. Do not use me
- The JWT app type is deprecated. Migrate to Server-to-Server OAuth. This does NOT affect JWT token signatures used in Video SDK — only the Marketplace "JWT" app type for…
- User-level OAuth apps: MUST use me instead of userId (otherwise: invalid token error)
- Server-to-Server OAuth apps: MUST NOT use me — provide the actual userId or email
- UUIDs that begin with / or contain // must be double URL-encoded:
- Some report APIs only accept UTC. Check the API reference for each endpoint
- User OAuth: MUST use me
- S2S OAuth: MUST NOT use me

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: plan-zoom-product
- Referenced: plan-zoom-integration
- Referenced: debug-zoom
- Referenced: https://developers.zoom.us/api-hub/<domain>/methods/endpoints.json
- Referenced: join_url
- Referenced: references/
- Referenced: endpoints.json
- Referenced: api_url
- Referenced: https://api.zoom.us/v2
- Referenced: https://api-au.zoom.us/v2
- Signal: code block: bash
- Signal: code block: json
- Signal: code block: javascript

## Source Sections
- Quick Links
- Quick Start
- Get an Access Token (Server-to-Server OAuth)
- Create a Meeting
- List Users with Pagination
- Base URL
- Regional Base URLs
- Key Features
- Prerequisites
- Critical Gotchas and Best Practices

## Batch Log Match
- Row: 121
- Canonical path: anthropics/knowledge-work-plugins/partner-built/zoom-plugin/skills/rest-api/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-rest-api-app/mp4/claude-liam-build-zoom-rest-api-app.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
