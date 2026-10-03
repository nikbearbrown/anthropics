# Source Details — claude-tag-plugins--claude-liam-linear-api

Generated: 2026-09-05T11:09:00

## Reel
- Question: linear api
- Family: claude-tag-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/claude-tag-plugins/youtube/claude-liam-linear-api/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-tag-plugins/linear/skills/linear-api/SKILL.md
- Name: linear-api
- Description: Read and manage Linear issues, projects, cycles, teams, comments, and labels. Use this whenever the user wants to list their issues, search issues, create or update an issue, move an issue between states, add a comment, check a project or cycle, look up a team, or ask "what's on my plate in Linear" — even if they don't say "API" or "GraphQL". Also use it for any linear.app URL or an issue identifier like "ENG-123". Always start from this skill when interacting with this service — its bundled scripts and recipes are the fastest path.

## Capabilities To Name On Screen
- Read and manage Linear issues
- Use this whenever the user wants to list their issues
- search issues
- create or update an issue
- move an issue between states

## Constraints / Failure Modes
- API, so there is nothing to set up. Do not try to create, mint, refresh, or validate tokens or keys
- Credential variables exist only to keep requests well-formed; if one is unset, set it to any
- body is Markdown. issueId must be the UUID, not the identifier — fetch it with recipe 3 first
- errors[].extensions.code: "INVALID_INPUT" / "INPUT_ERROR" — Validation failed. message names the bad field. Common: passing a key (ENG) where a UUID is required, or a…
- errors[].message: "Cannot query field …" — Typo or schema mismatch. Field doesn't exist. Check spelling; use introspection (references/api.md)

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: /api/v1/issues
- Referenced: ENG-123
- Referenced: issue(id: "ENG-123")
- Referenced: .errors
- Referenced: .data
- Referenced: scripts/linear_issues.sh
- Referenced: pageInfo.endCursor
- Referenced: --team KEY
- Referenced: --state NAME
- Referenced: --assignee EMAIL
- Signal: code block: bash

## Source Sections
- Request setup
- Core operations
- 1. Who am I / what's assigned to me
- 2. Search issues
- 3. Get one issue (by identifier or UUID)
- 4. List and filter issues (scripts/linear_issues.sh)
- 5. Create an issue
- 6. Update an issue (change state, assignee, priority, …)
- 7. Comment on an issue
- 8. Discover teams, workflow states, labels, members

## Batch Log Match
- Row: 52
- Canonical path: anthropics/claude-tag-plugins/linear/skills/linear-api/SKILL.md
- MP4 path: anthropics/claude-tag-plugins/youtube/claude-liam-linear-api/claude-liam-linear-api.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
