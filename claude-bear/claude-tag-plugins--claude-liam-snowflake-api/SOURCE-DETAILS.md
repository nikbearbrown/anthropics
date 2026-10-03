# Source Details — claude-tag-plugins--claude-liam-snowflake-api

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Snowflake Api.
- Family: claude-tag-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/claude-tag-plugins/youtube/claude-liam-snowflake-api/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-tag-plugins/snowflake/skills/snowflake-api/SKILL.md
- Name: snowflake-api
- Description: Run SQL against Snowflake — submit statements, poll async handles, fetch result partitions, cancel, and browse warehouses/databases/schemas/tables. Use this whenever the user wants to query Snowflake, ask "what tables are in this schema", check a warehouse's status, or mentions `snowflakecomputing.com`, `/api/v2/statements`, or a Snowflake account identifier (like `xy12345.us-east-1`). Always start from this skill when interacting with this service — its bundled scripts and recipes are the fastest path.

## Capabilities To Name On Screen
- Run SQL against Snowflake — submit statements
- poll async handles
- fetch result partitions
- and browse warehouses/databases/schemas/tables
- Use this whenever the user wants to query Snowflake

## Constraints / Failure Modes
- API, so there is nothing to set up. Do not try to create, mint, refresh, or validate tokens or keys
- Credential variables exist only to keep requests well-formed; if one is unset, set it to any
- The account identifier must be real — it's the hostname. It's the part of the Snowflake URL
- export SNOWFLAKE_ACCOUNT="xy12345.us-east-1" # your account identifier — must be real
- (User-Agent is required — Snowflake rejects requests without one. --compressed matters for
- it), and carry only data — no metadata
- and temporary table/stage creation are only supported inside a multi-statement request — as a
- Warehouse is required for anything that scans data. Metadata-only statements (most SHOW

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: snowflakecomputing.com
- Referenced: /api/v2/statements
- Referenced: xy12345.us-east-1
- Referenced: INFORMATION_SCHEMA
- Referenced: .snowflakecomputing.com
- Referenced: myorg-myaccount
- Referenced: User-Agent
- Referenced: --compressed
- Referenced: Content-Encoding: gzip
- Referenced: scripts/snow_query.sh
- Signal: code block: bash

## Source Sections
- Request setup
- Helper and sanity check
- Core operations
- 1. Run a statement (scripts/snow_query.sh)
- 2. Fetch results from an existing handle
- 3. Cancel a running statement
- 4. Idempotent submits with requestId
- 5. Run multiple statements in one request
- 6. Browse the catalog (databases, schemas, tables, columns)
- Pagination

## Batch Log Match
- Row: 67
- Canonical path: anthropics/claude-tag-plugins/snowflake/skills/snowflake-api/SKILL.md
- MP4 path: anthropics/claude-tag-plugins/youtube/claude-liam-snowflake-api/mp4/claude-liam-snowflake-api.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
