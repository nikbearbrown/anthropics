# Source Details — knowledge-work-plugins--claude-liam-call-prep

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Call Prep.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-call-prep/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/partner-built/common-room/skills/call-prep/SKILL.md
- Name: call-prep
- Description: Prepare for a customer or prospect call using Common Room signals. Triggers on 'prep me for my call with [company]', 'prepare for a meeting with [company]', 'what should I know before talking to [company]', or any call preparation request.

## Capabilities To Name On Screen
- Prepare for a customer or prospect call using Common Room signals
- Triggers on 'prep me for my call with [company]'
- 'prepare for a meeting with [company]'
- 'what should I know before talking to [company]'
- or any call preparation request.

## Constraints / Failure Modes
- Company name — required; look up the account in Common Room
- When reviewing activity history, prioritize Gong and call recording activities — these provide direct context about previous conversations. Do not filter out call…
- After gathering all Common Room data, run a quick recency check to catch anything that happened since the last CR data sync. This is supplementary — CR data drives the…
- The output adapts to how much data Common Room returned. Only include sections where you have real data. Never fill a section with invented details
- [Only the fields actually returned, presented as-is]
- Do not generate a full call prep brief from sparse data. A short honest output is always better than a long fabricated one
- Never invent deal context — no fabricated proposals, competitor comparisons, pricing, trial terms, or objections not returned by a tool call

## Procedure / Sequence
- Identify the Account and Attendees: Parse what the user has provided: - Company name — required; look up the account in Common Room - Attendee names…
- Run Account Research: Use the account-research skill process to build a full account snapshot. For call prep, prioritize: - Recent product…
- Run Contact Research for Each Attendee: For each external attendee, use the contact-research skill process. For call prep, focus on: - Role and influence in…
- Synthesize Talking Points and Objectives: Based on the combined account and contact research: - Identify the call objective (e.g., discovery, demo, expansion…
- Recency Check (Web Search): After gathering all Common Room data, run a quick recency check to catch anything that happened since the last CR data…

## Supporting Files And Signals
- Referenced: references/my-company-context.md
- Referenced: references/call-types-guide.md
- Referenced: references/

## Source Sections
- Prep Process
- Step 1: Identify the Account and Attendees
- Step 2: Run Account Research
- Step 3: Run Contact Research for Each Attendee
- Step 4: Synthesize Talking Points and Objectives
- Step 5: Recency Check (Web Search)
- Output Format
- When data is rich (multiple field groups returned, activity history, scores, signals):
- Call Prep: [Company] — [Date/Time if known]
- Company Snapshot

## Batch Log Match
- Row: 128
- Canonical path: anthropics/knowledge-work-plugins/partner-built/common-room/skills/call-prep/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-call-prep/mp4/claude-liam-call-prep.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
