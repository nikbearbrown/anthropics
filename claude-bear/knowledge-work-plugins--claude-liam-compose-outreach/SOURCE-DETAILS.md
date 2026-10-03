# Source Details — knowledge-work-plugins--claude-liam-compose-outreach

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Compose Outreach.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-compose-outreach/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/partner-built/common-room/skills/compose-outreach/SKILL.md
- Name: compose-outreach
- Description: Generate personalized outreach messages using Common Room signals. Triggers on 'draft outreach to [person]', 'write an email to [name]', 'compose a message for [contact]', or any outreach drafting request.

## Capabilities To Name On Screen
- Generate personalized outreach messages using Common Room signals
- Triggers on 'draft outreach to [person]'
- 'write an email to [name]'
- 'compose a message for [contact]'
- or any outreach drafting request.

## Constraints / Failure Modes
- If the user specified a person, run contact-level research. If only a company was given, identify the best contact to target based on title, engagement, and role
- Do not draft outreach from thin air. Outreach grounded in fabricated signals is worse than no outreach
- [Only the real data from CR and web search]
- Every message must reference something specific — generic outreach is not acceptable output
- The LinkedIn message must be under 300 characters — no exceptions
- The call script must be speakable naturally — read it aloud mentally to check rhythm
- Never fabricate signals — only reference data retrieved from Common Room or web search

## Procedure / Sequence
- Look Up the Target: Use Common Room MCP tools to find and retrieve data for the target (company and/or specific contact). Pull: - Recent…
- Web Search for External Hooks (If CR Signals Are Thin): If CR returned strong signals (recent activity, engagement, product usage), those should drive personalization — skip…
- Spark Enrichment (If Available): If Spark is available, run enrichment on the target contact to get persona classification, background, and influence…
- Identify the Best Hooks: From the signal data, identify the 1–3 strongest personalization hooks. Rank by: 1. Recency — happened in the last 7–14…
- Generate All Three Formats: Use the strongest hooks to write all three formats. Each format has different constraints and conventions — follow the…
- Annotate Your Choices: After the three drafts, include a brief note (2–4 sentences) explaining: - Which signals were used and why they were…

## Supporting Files And Signals
- Referenced: references/outreach-formats-guide.md
- Referenced: references/my-company-context.md
- Referenced: references/

## Source Sections
- Outreach Process
- Step 1: Look Up the Target
- Step 2: Web Search for External Hooks (If CR Signals Are Thin)
- Step 3: Spark Enrichment (If Available)
- Step 4: Identify the Best Hooks
- Step 5: Generate All Three Formats
- Step 6: Annotate Your Choices
- Output Format
- Outreach for [Name / Company]
- 📧 Email

## Batch Log Match
- Row: 165
- Canonical path: anthropics/knowledge-work-plugins/partner-built/common-room/skills/compose-outreach/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-compose-outreach/mp4/claude-liam-compose-outreach.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
