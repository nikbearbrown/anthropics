# Source Details — knowledge-work-plugins--claude-liam-contact-research

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Contact Research.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-contact-research/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/partner-built/common-room/skills/contact-research/SKILL.md
- Name: contact-research
- Description: Research a specific person using Common Room data. Triggers on 'who is [name]', 'look up [email]', 'research [contact]', 'is [name] a warm lead', or any contact-level question.

## Capabilities To Name On Screen
- Research a specific person using Common Room data
- Triggers on 'who is [name]'
- 'look up [email]'
- 'research [contact]'
- 'is [name] a warm lead'

## Constraints / Failure Modes
- | Name only | Search by name; if multiple matches, show a brief list and ask the user to confirm |
- If no match is found, respond: "Common Room doesn't have a record for this person." Do not speculate or fabricate profile data
- Use the Common Room object catalog to see available field groups and their contents. For full profiles, request all groups. For targeted questions, request only what's…
- Scores — always return as raw values or percentiles, never labels
- If Spark is unavailable but real activity data exists (recent actions, website visits, community engagement), infer a persona from those signals. If neither Spark nor…
- Only include sections where data was actually returned. Omit sections with no data rather than filling them with guesses
- When data is sparse (e.g., only name, title, email, tags returned; sparkSummary is null):
- [Present only the returned fields]

## Procedure / Sequence
- Locate the Contact: Common Room supports multiple lookup methods — use whichever the user has provided: | What the user gives | Lookup…
- Fetch Contact Fields: Use the Common Room object catalog to see available field groups and their contents. For full profiles, request all…
- Run Spark Enrichment (If Available): If Spark is available, use it. Spark provides: - Professional background and job history - Social presence and…
- Assess Account Context: Pull an abbreviated account snapshot for this contact's parent company. Note: - Open opportunities, expansion signals…
- Identify Conversation Angles: Based on activity and signals, surface the strongest 2–3 hooks: - A recent Contact Initiated activity (community post…

## Supporting Files And Signals
- Referenced: references/contact-signals-guide.md
- Referenced: references/

## Source Sections
- Step 1: Locate the Contact
- Step 2: Fetch Contact Fields
- Step 3: Run Spark Enrichment (If Available)
- Step 4: Assess Account Context
- Step 5: Identify Conversation Angles
- Output Format
- [Contact Name] — Profile
- [Contact Name] — Profile (Limited Data)
- Quality Standards
- Reference Files

## Batch Log Match
- Row: 170
- Canonical path: anthropics/knowledge-work-plugins/partner-built/common-room/skills/contact-research/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-contact-research/mp4/claude-liam-contact-research.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
