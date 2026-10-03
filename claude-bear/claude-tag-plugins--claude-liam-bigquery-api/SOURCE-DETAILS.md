# Source Details — claude-tag-plugins--claude-liam-bigquery-api

Generated: 2026-09-05T11:09:00

## Reel
- Question: BigQuery API
- Family: claude-tag-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/claude-tag-plugins/youtube/claude-liam-bigquery-api/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-tag-plugins/bigquery/skills/bigquery-api/SKILL.md
- Name: bigquery-api
- Description: Run SQL against Google BigQuery and browse its catalog — submit queries (sync or async), poll job status, page through results, list datasets/tables, and read table schemas. Use this whenever the user wants to query a BigQuery table, ask "what's in this dataset", check a BigQuery job's status, or mentions bigquery.googleapis.com or a `project.dataset.table` path. Always start from this skill when interacting with this service — its bundled scripts and recipes are the fastest path.

## Capabilities To Name On Screen
- Run SQL against Google BigQuery and browse its catalog — submit queries (sync or async)
- poll job status
- page through results
- list datasets/tables
- and read table schemas

## Constraints / Failure Modes
- BigQuery's REST API (bigquery.googleapis.com/bigquery/v2) lets you run SQL, inspect jobs, and browse datasets and table schemas with plain curl — no SDK required
- Authentication is handled by the runtime — credentials are injected into outbound requests to this API, so there is nothing to set up. Do not try to create, mint…
- export GCP_PROJECT="my-project" # the project that pays for queries — must be real

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: project.dataset.table
- Referenced: bigquery.googleapis.com/bigquery/v2
- Referenced: scripts/bq_query.sh
- Referenced: jobs.query
- Referenced: jobs.insert
- Referenced: jobs.get
- Referenced: jobs.getQueryResults
- Referenced: Authorization: Bearer ...
- Referenced: JSON — post-process with
- Referenced: bigquery-public-data.usa_names.usa_1910_current
- Signal: code block: bash

## Source Sections
- Request setup
- Core operations
- 1. Run a query (scripts/bq_query.sh)
- 2. Submit a job directly (jobs.insert → jobs.get)
- 3. Cancel a running job
- 4. List recent jobs
- 5. List datasets
- 6. List tables in a dataset
- 7. Get a table's schema and size
- 8. Preview table rows without a query (tabledata.list)

## Batch Log Match
- Row: 29
- Canonical path: anthropics/claude-tag-plugins/bigquery/skills/bigquery-api/SKILL.md
- MP4 path: anthropics/claude-tag-plugins/youtube/claude-liam-bigquery-api/claude-liam-bigquery-api.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
