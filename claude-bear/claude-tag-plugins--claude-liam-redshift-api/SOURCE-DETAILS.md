# Source Details — claude-tag-plugins--claude-liam-redshift-api

Generated: 2026-09-05T11:09:00

## Reel
- Question: redshift-api
- Family: claude-tag-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/claude-tag-plugins/youtube/claude-liam-redshift-api/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-tag-plugins/redshift/skills/redshift-api/SKILL.md
- Name: redshift-api
- Description: Run SQL against Amazon Redshift — submit statements, poll status, page through results, and browse databases/schemas/tables. Use this whenever the user wants to query Redshift (provisioned cluster or Serverless), ask "what tables are in this schema", check a query's status, or mentions `redshift-data`, a Redshift cluster identifier / workgroup name, or a `redshift-data.{region}.amazonaws.com` endpoint. Always start from this skill when interacting with this service — its bundled scripts and recipes are the fastest path.

## Capabilities To Name On Screen
- Run SQL against Amazon Redshift — submit statements
- page through results
- and browse databases/schemas/tables
- Use this whenever the user wants to query Redshift (provisioned cluster or Serverless)
- ask "what tables are in this schema"

## Constraints / Failure Modes
- provisioned clusters and Serverless; only the connection-target field differs
- configured for the workspace, so there is nothing to set up. Do not try to obtain AWS keys or sign
- Two pieces of configuration are real and required:
- Status ∈ SUBMITTED, PICKED, STARTED, FINISHED, FAILED, ABORTED. Only FINISHED
- Status filter: SUBMITTED, PICKED, STARTED, FINISHED, FAILED, ABORTED, ALL — **only
- (includes statements from anyone assuming the same IAM role); set false to see only this session's
- ExecuteStatement 30, GetStatementResult 20, BatchExecuteStatement 20, and only 3 TPS for
- ExecuteStatement returning 200 ≠ the query succeeded. SQL errors only surface later as

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: redshift-data
- Referenced: redshift-data.{region}.amazonaws.com
- Referenced: https://redshift-data.<region>.amazonaws.com/
- Referenced: Content-Type: application/x-amz-json-1.1
- Referenced: X-Amz-Target: RedshiftData.<Action>
- Referenced: scripts/rs_query.sh
- Referenced: RS_TARGET
- Referenced: $t + {Database: $db, ...}
- Referenced: {"__type": "<Exception>", "message": "..."}
- Referenced: AWS_DEFAULT_REGION
- Signal: code block: bash

## Source Sections
- Request setup
- Core operations
- 1. Run a query (scripts/rs_query.sh)
- 2. Resume a statement by id (DescribeStatement → GetStatementResult)
- 3. Cancel a running statement (CancelStatement)
- 4. Run multiple statements in one call (BatchExecuteStatement)
- 5. List recent statements (ListStatements)
- 6. Browse the catalog (ListDatabases / ListSchemas / ListTables / DescribeTable)
- Pagination
- Rate limits

## Batch Log Match
- Row: 62
- Canonical path: anthropics/claude-tag-plugins/redshift/skills/redshift-api/SKILL.md
- MP4 path: anthropics/claude-tag-plugins/youtube/claude-liam-redshift-api/claude-liam-redshift-api.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
