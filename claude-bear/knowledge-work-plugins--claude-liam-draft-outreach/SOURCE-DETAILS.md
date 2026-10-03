# Source Details — knowledge-work-plugins--claude-liam-draft-outreach

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Draft Outreach.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-draft-outreach/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/sales/skills/draft-outreach/SKILL.md
- Name: draft-outreach
- Description: Research a prospect then draft personalized outreach. Uses web research by default, supercharged with enrichment and CRM. Trigger with "draft outreach to [person/company]", "write cold email to [prospect]", "reach out to [name]".

## Capabilities To Name On Screen
- Research a prospect then draft personalized outreach
- Uses web research by default
- supercharged with enrichment and CRM
- Trigger with "draft outreach to [person/company]"
- "write cold email to [prospect]"

## Constraints / Failure Modes
- Research first, then draft. This skill never sends generic outreach - it always researches the prospect first to personalize the message. Works standalone with web…
- Must find before drafting:
- | Capability | Web Only | + Enrichment | + CRM | + Email |
- | Background details | Public only | Full | Full | Full |
- No markdown formatting — Never use asterisks, bold (text), or other markdown. Write plain text that looks natural in any email client
- Plain text formatting only

## Procedure / Sequence
- Parse Request
- Research First (Always): Use research-prospect skill internally: Must find before drafting: - Who they are (title, background) - What the…
- Identify Hook
- Draft Message: Email Structure (AIDA): LinkedIn Connection Request (<300 chars): LinkedIn Follow-up Message
- Create Email Draft: ---

## Supporting Files And Signals
- No referenced files extracted.
- Signal: code block: markdown

## Source Sections
- Connectors (Optional)
- How It Works
- Output Format
- Research Summary
- Email Draft
- LinkedIn Message (if no email)
- Why This Approach
- Email Draft Status
- Follow-up Sequence (Optional)
- Execution Flow

## Batch Log Match
- Row: 221
- Canonical path: anthropics/knowledge-work-plugins/sales/skills/draft-outreach/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-draft-outreach/mp4/claude-liam-draft-outreach.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
