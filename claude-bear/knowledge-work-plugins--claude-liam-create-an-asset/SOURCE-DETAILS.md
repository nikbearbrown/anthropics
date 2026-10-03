# Source Details — knowledge-work-plugins--claude-liam-create-an-asset

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Create An Asset.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-create-an-asset/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/sales/skills/create-an-asset/SKILL.md
- Name: create-an-asset
- Description: Generate tailored sales assets (landing pages, decks, one-pagers, workflow demos) from your deal context. Describe your prospect, audience, and goal — get a polished, branded asset ready to share with customers.

## Capabilities To Name On Screen
- Generate tailored sales assets (landing pages
- workflow demos) from your deal context
- Describe your prospect
- and goal — get a polished
- branded asset ready to share with customers.

## Constraints / Failure Modes
- | Field | Prompt | Required |
- | Rich | Transcripts uploaded, detailed pain points, clear requirements | Light — fill gaps only |
- value_note: "No manual data gathering required"
- ## Phase 5: Clarifying Questions (REQUIRED)
- | "What's the ONE thing this must nail to succeed?" | Focus on priority |
- If brand colors cannot be extracted:

## Procedure / Sequence
- 1: Detect Seller Context: From the user's email domain, identify what company they work for. Actions: 1. Extract domain from user's email 2.…
- 2: Collect Prospect Context (a): Ask the user: | Field | Prompt | Required | |-------|--------|----------| | Company | "Which company is this asset…
- 3: Collect Audience Context (b): Ask the user: | Field | Prompt | Required | |-------|--------|----------| | Audience type | "Who's viewing this?" | ✓…
- 4: Collect Purpose Context (c): Ask the user: | Field | Prompt | Required | |-------|--------|----------| | Goal | "What's the goal of this asset?" | ✓…
- 5: Select Format (d): Ask the user: "What format works best for this?" | Format | Description | Best For |…
- 6: Format-Specific Inputs: #### If "Workflow / Architecture demo" selected: First, parse from user's description. Look for: - Systems and…
- 1: Summarize Understanding: First, show the user what you understood
- 2: Ask Standard Questions (ALL formats): | Question | Why | |----------|-----| | "Does this match your vision?" | Confirm understanding | | "What's the ONE…

## Supporting Files And Signals
- Referenced: /create-an-asset
- Referenced: /create-an-asset [CompanyName]
- Referenced: "[domain]" company products services site:linkedin.com OR site:crunchbase.com
- Referenced: var(--bg-surface)
- Referenced: var(--accent)
- Referenced: [ProspectName]-[format]-[date].html
- Referenced: CentricBrands-workflow-demo-2026-01-28.html
- Referenced: QUICKREF.md
- Referenced: README.md
- Signal: code block: yaml
- Signal: code block: css
- Signal: code block: markdown

## Source Sections
- Triggers
- Overview
- Phase 0: Context Detection & Input Collection
- Step 0.1: Detect Seller Context
- Step 0.2: Collect Prospect Context (a)
- Step 0.3: Collect Audience Context (b)
- Step 0.4: Collect Purpose Context (c)
- Step 0.5: Select Format (d)
- Step 0.6: Format-Specific Inputs
- Phase 1: Research (Adaptive)

## Batch Log Match
- Row: 176
- Canonical path: anthropics/knowledge-work-plugins/sales/skills/create-an-asset/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-create-an-asset/mp4/claude-liam-create-an-asset.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
