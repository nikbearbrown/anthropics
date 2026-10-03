# Source Details — claude-for-legal--claude-liam-cocounsel-legal:deep-research

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Cocounsel Legal:deep Research.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-cocounsel-legal:deep-research/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/external_plugins/cocounsel-legal/skills/deep-research/SKILL.md
- Name: cocounsel-legal:deep-research
- Description: >

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- The cocounsel-legal MCP server must be connected. Verify it is available before starting research. If the server is not connected, inform the user and stop
- If you suggest an alternative, do not attempt to use the Deep Research skill further for that task
- Never mention tool calls, tool-call budgets, polling, status checks, internal limits, conversation IDs, percent_complete, or any other implementation details to the…
- If you need to pause before the research completes (for any internal reason), do NOT explain why
- query (string, required): The legal research question
- Do not show the conversation_id to the user
- Always run a Bash sleep between polls. Never call check_deep_research_status back-to-back without sleeping
- Only update the user when there is something new to say (a step completed, or a new step started). Do not repeat the same status

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: cocounsel-legal
- Referenced: legal_research_start_deep_research(query, jurisdictions)
- Referenced: conversation_id
- Referenced: legal_research_check_deep_research_status(conversation_id)
- Referenced: is_terminal
- Referenced: next_action_poll_backoff_ms
- Referenced: legal_research_get_deep_research_report(conversation_id)
- Referenced: answer_text

## Source Sections
- Prerequisites
- When to Use
- When Not to Use
- Communication Rules
- Research Workflow
- 1. Frame the query
- 2. Start Research
- 3. Poll for Completion
- 4. Retrieve and Present Report Verbatim
- Helpful information

## Batch Log Match
- Row: 154
- Canonical path: anthropics/claude-for-legal/external_plugins/cocounsel-legal/skills/deep-research/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-cocounsel-legal:deep-research/mp4/claude-liam-cocounsel-legal:deep-research.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
