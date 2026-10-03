# Source Details — knowledge-work-plugins--claude-liam-account-research

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Account Research.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-account-research/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/partner-built/common-room/skills/account-research/SKILL.md
- Name: account-research
- Description: Research a company using Common Room data. Triggers on 'research [company]', 'tell me about [domain]', 'pull up signals for [account]', 'what's going on with [company]', or any account-level question.

## Capabilities To Name On Screen
- Research a company using Common Room data
- Triggers on 'research [company]'
- 'tell me about [domain]'
- 'pull up signals for [account]'
- 'what's going on with [company]'

## Constraints / Failure Modes
- → Fetch only the relevant field(s). Return a direct, concise answer — do not produce a full brief for a simple question
- → If Common Room has limited data for an account, say so honestly: "There is limited information available for this account." Never speculate or fill gaps with generic…
- Use the Common Room object catalog to see available field groups and their contents. For full overviews, request all field groups. For targeted questions, request only…
- Scores — always return as raw values or percentiles, never labels
- ## Step 4: Web Search (Sparse Data Only)
- Common Room is the primary data source. Do not run web search when CR returns rich data
- Only include sections where Common Room returned actual data. Omit sections entirely rather than filling them with guesses
- [Present only the returned fields]

## Procedure / Sequence
- Load User Context (Me): Before researching any account, fetch the Me object from Common Room. This provides: - The user's profile, title, role…
- Identify the Interaction Pattern: Determine what the user actually needs before deciding how much data to fetch: Pattern 1 — Full Overview: "Tell me…
- Look Up the Account: Search Common Room for the account by domain or company name. Exact match first; if no result, try partial match and…
- Fetch the Right Fields: Use the Common Room object catalog to see available field groups and their contents. For full overviews, request all…
- Web Search (Sparse Data Only): Common Room is the primary data source. Do not run web search when CR returns rich data. When CR data is sparse…
- Apply Reasoning (Pattern 4): When the user's question invites synthesis — not just data retrieval — layer in analysis: - Compare account data to…
- Produce Output: Only include sections where Common Room returned actual data. Omit sections entirely rather than filling them with…

## Supporting Files And Signals
- Referenced: references/my-company-context.md
- Referenced: references/signals-guide.md
- Referenced: references/

## Source Sections
- Step 0: Load User Context (Me)
- Step 1: Identify the Interaction Pattern
- Step 2: Look Up the Account
- Step 3: Fetch the Right Fields
- Step 4: Web Search (Sparse Data Only)
- Step 5: Apply Reasoning (Pattern 4)
- Step 6: Produce Output
- [Company Name] — Account Overview
- [Company Name] — Account Overview (Limited Data)
- Quality Standards

## Batch Log Match
- Row: 93
- Canonical path: anthropics/knowledge-work-plugins/partner-built/common-room/skills/account-research/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-account-research/mp4/claude-liam-account-research.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
