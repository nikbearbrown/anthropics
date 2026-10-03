# Source Details — claude-tag-plugins--claude-liam-asana-api

Generated: 2026-09-05T11:09:00

## Reel
- Question: Asana API
- Family: claude-tag-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/claude-tag-plugins/youtube/claude-liam-asana-api/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-tag-plugins/asana/skills/asana-api/SKILL.md
- Name: asana-api
- Description: Read and manage Asana tasks, projects, sections, comments, and workspaces. Use this whenever the user wants to list or search tasks, create or update a task, complete a task, comment on a task, move tasks between projects or sections, look up a project or workspace, or ask "what's on my Asana list" — even if they don't say "API". Also use it for any app.asana.com URL or an Asana task/project gid. Always start from this skill when interacting with this service — its bundled scripts and recipes are the fastest path.

## Capabilities To Name On Screen
- Read and manage Asana tasks
- and workspaces
- Use this whenever the user wants to list or search tasks
- create or update a task
- complete a task

## Constraints / Failure Modes
- API, so there is nothing to set up. Do not try to create, mint, refresh, or validate tokens or keys
- Credential variables exist only to keep requests well-formed; if one is unset, set it to any
- opt_fields for fields. Compact records carry only gid, name, resource_type. Add a
- Exactly one selector is required: --project GID, --tag GID, --section GID, or
- completed-since WHEN — ISO 8601, or now to show only incomplete tasks (omit to include all)
- assignee, due_on, permalink_url); extra fields appear only in --json output
- With no opt_fields you get only the compact record. Read a task's comments with recipe
- Fields nest under data. One of workspace, projects, or parent is required (a standalone task

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: https://app.asana.com/api/1.0
- Referenced: resource_type
- Referenced: opt_fields
- Referenced: {"data": ...}
- Referenced: {"data": {...}}
- Referenced: .data
- Referenced: .errors
- Referenced: assignee.name
- Referenced: memberships.section.name
- Referenced: scripts/asana_tasks.sh
- Signal: code block: bash

## Source Sections
- Request setup
- Response conventions
- Core operations
- 1. List tasks (scripts/asana_tasks.sh)
- 2. Get one task
- 3. Create a task
- 4. Update or complete a task
- 5. Comment on a task / read its activity (stories)
- 6. Search tasks in a workspace (premium)
- 7. Projects and sections

## Batch Log Match
- Row: 28
- Canonical path: anthropics/claude-tag-plugins/asana/skills/asana-api/SKILL.md
- MP4 path: anthropics/claude-tag-plugins/youtube/claude-liam-asana-api/claude-liam-asana-api.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
