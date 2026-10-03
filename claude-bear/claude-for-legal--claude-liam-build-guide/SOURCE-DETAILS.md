# Source Details — claude-for-legal--claude-liam-build-guide

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Build Guide.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-build-guide/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/legal-clinic/skills/build-guide/SKILL.md
- Name: build-guide
- Description: >

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- Load ~/.claude/plugins/config/claude-for-legal/legal-clinic/CLAUDE.md → role (must be Supervising attorney), practice areas, jurisdiction
- Every output from this skill is a supervisor-facing configuration artifact, not student work product. Do NOT prepend [AI-ASSISTED DRAFT — requires student analysis and…
- When must the student stop and get your sign-off? (Filing, sending to a client, making a representation, advising on strategy)
- > - Teach: The skill doesn't produce work product — students draft, the skill gives Socratic feedback and only shows models after two attempts. Slowest, most…
- | Client letter (substantive advice / bad news) | [always supervisor — cannot override] |
- | Draft filing (court / agency) | [always supervisor — cannot override] |
- | Status update to court | [always supervisor — cannot override] |
- If the supervisor names a cross-plugin skill they want, record: skill name, when students should use it, what supervision wrapper applies (always reviewer, only when…

## Procedure / Sequence
- Check role: This is a supervisor skill. Read ~/.claude/plugins/config/claude-for-legal/legal-clinic/CLAUDE.md → ## Who's using this…
- Which practice area?: > What clinic is this guide for? (Immigration / Housing / Family / Transactional / Criminal defense / Consumer / Other)…
- Intake questions: > What should students ask a new client for this clinic type? I'll start with a generic intake for [practice area]…
- Pedagogy posture: > How much should the skills do vs. how much should the student do? > > - Guide (default): The skill produces…
- Review gates: > Which work product needs your review before it goes to a client? Which can students send directly? Default…
- Cross-plugin checks: > Do you want students to use skills from other plugins (defined-terms checks, doc consistency, section references…
- Local rules and jurisdiction: > What court(s) does your clinic practice in? Any local rules or forms students need to use? Check CLAUDE.md → ##…
- Write the guide: Write to ~/.claude/plugins/config/claude-for-legal/legal-clinic/guides/<practice-area>.md. Create the guides/ directory…

## Supporting Files And Signals
- Referenced: ~/.claude/plugins/config/claude-for-legal/legal-clinic/CLAUDE.md
- Referenced: /legal-clinic:ramp
- Referenced: ~/.claude/plugins/config/claude-for-legal/legal-clinic/guides/<practice-area>.md
- Referenced: guides/
- Referenced: /legal-clinic:draft
- Referenced: [AI-ASSISTED DRAFT — requires student analysis and attorney review]
- Referenced: /legal-clinic:cold-start-interview
- Referenced: immigration-removal-defense.md
- Referenced: transactional-nonprofit.md
- Referenced: CLAUDE.md
- Signal: code block: markdown

## Source Sections
- Purpose
- Work-product header
- Key things your guide should address
- Workflow
- Step 1: Check role
- Step 2: Which practice area?
- Step 3: Intake questions
- Step 4: Pedagogy posture
- Step 5: Review gates
- Step 6: Cross-plugin checks

## Batch Log Match
- Row: 115
- Canonical path: anthropics/claude-for-legal/legal-clinic/skills/build-guide/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-build-guide/mp4/claude-liam-build-guide.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
