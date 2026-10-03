# Source Details — claude-tag-plugins--claude-liam-grafana-api

Generated: 2026-09-05T11:09:00

## Reel
- Question: grafana-api
- Family: claude-tag-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/claude-tag-plugins/youtube/claude-liam-grafana-api/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-tag-plugins/grafana/skills/grafana-api/SKILL.md
- Name: grafana-api
- Description: Work with a Grafana instance — search and read dashboards, run datasource queries (Prometheus, Loki, PostgreSQL, etc.), inspect alert rules and silences, post annotations, and manage folders. Use this whenever the user mentions a Grafana dashboard, panel, or alert; pastes a Grafana URL; asks "what does this dashboard show", "query this metric in Grafana", "is this alert firing", "silence this alert", or wants to create/export a dashboard — even if they don't say "API". Always start from this skill when interacting with this service — its bundled scripts and recipes are the fastest path.

## Capabilities To Name On Screen
- Work with a Grafana instance — search and read dashboards
- run datasource queries (Prometheus
- inspect alert rules and silences
- post annotations
- and manage folders

## Constraints / Failure Modes
- wherever the org runs it (e.g. https://grafana.example.com). The API surface is the same; only the
- API, so there is nothing to set up. Do not try to create, mint, refresh, or validate tokens or keys
- Credential variables exist only to keep requests well-formed; if one is unset, set it to any
- The instance URL must be real — it's part of every request path:
- Datasource queries and dashboard reads only need Viewer
- # live STATE (firing/pending/inactive) — read-only

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: https://<your-org>.grafana.net
- Referenced: https://grafana.example.com
- Referenced: /api/ds/query
- Referenced: /api/annotations
- Referenced: dash-db
- Referenced: dash-folder
- Referenced: .../d/<uid>/<slug>
- Referenced: .dashboard.panels[].targets
- Referenced: "rawSql": "SELECT ..."
- Referenced: results.<refId>.frames[]
- Signal: code block: bash

## Source Sections
- Request setup
- Core operations
- 1. Search dashboards and folders
- 2. Get a dashboard by UID
- 3. Run a datasource query
- 4. List alert rules
- 5. Silences
- 6. Annotations
- 7. Folders
- 8. Create or update a dashboard

## Batch Log Match
- Row: 47
- Canonical path: anthropics/claude-tag-plugins/grafana/skills/grafana-api/SKILL.md
- MP4 path: anthropics/claude-tag-plugins/youtube/claude-liam-grafana-api/claude-liam-grafana-api.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
