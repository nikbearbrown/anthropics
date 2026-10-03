# Source Details — claude-for-legal--claude-liam-client-intake

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Client Intake.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-client-intake/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/legal-clinic/skills/client-intake/SKILL.md
- Name: client-intake
- Description: >

## Capabilities To Name On Screen
- Privilege and confidentiality.: This summary is derived from client communications that may be privileged, confidential, or both. It inherits the…
- Date:: [date] | Intake by: [student] | Practice area: [primary + any cross-area]

## Constraints / Failure Modes
- ### Step 7: Deadline handoff — required deliverable
- If the intake surfaces any timeline deadline (answer due, hearing, statute-of-limitations cutoff, cure period, filing window, notice window, ICE check-in, removal…
- One block per deadline surfaced. Do not combine. Each one will route through the deadlines skill's pre-add duplicate check
- Every statutory, ordinance, regulatory, rule, or case citation in this section carries a provenance tag (see plugin CLAUDE.md ## Shared guardrails for the tag…
- Every statute, ordinance, rule, or case citation in this section carries a provenance tag — same vocabulary as ## Legal issues identified. Default [model knowledge…

## Procedure / Sequence
- Practice area routing: Which practice area does this intake start in? The client may not know — they know their problem, not the legal…
- Practice-area-specific intake: Each practice area asks different questions. Use the template from…
- Cross-practice-area issue spotting: While running the practice-area template, listen for issues outside that area: | Client says | Also flags | |---|---| |…
- Conflict check flags: Per whatever conflict-check process ~/.claude/plugins/config/claude-for-legal/legal-clinic/CLAUDE.md describes. At…
- Triage classification: Not a case-acceptance decision — a triage input: | Classification | Means | |---|---| | Urgent | Deadline in days…
- Supervision flag check: Per ~/.claude/plugins/config/claude-for-legal/legal-clinic/CLAUDE.md supervision style and flag triggers. If formal…
- Deadline handoff — required deliverable: If the intake surfaces any timeline deadline (answer due, hearing, statute-of-limitations cutoff, cure period, filing…

## Supporting Files And Signals
- Referenced: ~/.claude/plugins/config/claude-for-legal/legal-clinic/CLAUDE.md
- Referenced: ~/.claude/plugins/config/claude-for-legal/legal-clinic/guides/<practice-area>.md
- Referenced: /legal-clinic:build-guide
- Referenced: /legal-clinic:deadlines --add ...
- Referenced: [statute / regulator site]
- Referenced: references/intake-templates/[area].md
- Referenced: references/
- Signal: code block: markdown

## Source Sections
- Purpose
- Load context
- Read the supervisor guide
- Workflow
- Step 1: Practice area routing
- Step 2: Practice-area-specific intake
- Step 3: Cross-practice-area issue spotting
- Step 4: Conflict check flags
- Step 5: Triage classification
- Step 6: Supervision flag check

## Batch Log Match
- Row: 145
- Canonical path: anthropics/claude-for-legal/legal-clinic/skills/client-intake/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-client-intake/mp4/claude-liam-client-intake.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
