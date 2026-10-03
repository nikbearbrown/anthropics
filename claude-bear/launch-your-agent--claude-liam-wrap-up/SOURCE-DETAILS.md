# Source Details — launch-your-agent--claude-liam-wrap-up

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Wrap Up.
- Family: launch-your-agent
- Source sheet: /Users/nik/Documents/books/anthropics/launch-your-agent/youtube/claude-liam-wrap-up/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/launch-your-agent/.claude/skills/wrap-up/SKILL.md
- Name: wrap-up
- Description: Close out (or revisit) a Claude Managed Agent build — refresh the overview page, recap every primitive the founder now owns, show the run log and live status, suggest 1–2 tailored next upgrades, and sweep hygiene (sessions archived, key only in .env, no literal dates in deployment kickoffs). Use when the founder says "/wrap-up", "wrap up", "close it out", "where do things stand with my agent", or at the end of a /launch-your-agent build.

## Capabilities To Name On Screen
- Close out (or revisit) a Claude Managed Agent build — refresh the overview page
- recap every primitive the founder now owns
- show the run log and live status
- suggest 1–2 tailored next upgrades
- and sweep hygiene (sessions archived

## Constraints / Failure Modes
- description: Close out (or revisit) a Claude Managed Agent build — refresh the overview page, recap every primitive the founder now owns, show the run log and live…
- dependencies: A ./my-agent/ folder from /launch-your-agent. ANTHROPIC_API_KEY in my-agent/.env optional — without it the wrap-up is describe-only
- Follow the same voice rules as /launch-your-agent: warm, compact, tables for anything enumerable, primitives called by their real names (Outcome, Session, Deployment…
- If my-agent/.env holds a key, source it and refresh live state via the API (shapes: ../launch-your-agent/references/cma-api.md): each session's status +…
- No key → continue describe-only and say in one sentence that live status needs the key in .env
- Nothing launched yet → wrap the plan only; everything below still applies but the status is "○ Planned"
- Overview page. Refresh agent-overview.html (template: ../launch-your-agent/references/overview-template.html; styling in the sibling overview.css, linked, never…
- Hygiene sweep — quiet by default. Do the sweep (archive finished sessions; check the deployment's initial_events for literal dates; check the key only ever lived in…

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: ./my-agent/
- Referenced: my-agent/.env
- Referenced: /launch-your-agent
- Referenced: build-sheet.json
- Referenced: IDS.env
- Referenced: NEXT-DIRECTIONS.md
- Referenced: outcome.md
- Referenced: evals/
- Referenced: agent-overview.html
- Referenced: my-agent/

## Source Sections
- 1. Read the state
- 2. Produce the wrap-up (in this order)
- Notes

## Batch Log Match
- Row: 90
- Canonical path: anthropics/launch-your-agent/.claude/skills/wrap-up/SKILL.md
- MP4 path: anthropics/launch-your-agent/youtube/claude-liam-wrap-up/mp4/claude-liam-wrap-up.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
