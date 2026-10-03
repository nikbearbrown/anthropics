# Source Details — claude-for-legal--claude-liam-draft

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Draft.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-draft/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/legal-clinic/skills/draft/SKILL.md
- Name: draft
- Description: >

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- Match doc type to template. Gather facts from case notes — flag missing, never guess
- guide (default): Produce the structure and the checklist. Ask the student to draft each section. Give feedback on their draft (register, reading level, required…
- teach: Don't produce the work product. Ask the student to draft it. Give feedback. Ask leading questions when they're stuck. Only show a model paragraph after two…
- Missing required facts → don't guess. Mark them: [FACT NEEDED: client's entry date — get from I-94 or ask client]
- Use the practice-area template. Fill what can be filled from facts. Leave placeholders explicit — never fill with plausible-sounding invention
- Every [VERIFY] and [FACT NEEDED] flag must be resolved before filing
- Before this leaves the clinic. This is a student draft for supervising-attorney review, not a final letter, filing, or form. Filing it with a court or agency, or sending…
- Produce final work product. First draft only. Student revises, professor reviews

## Procedure / Sequence
- Which document?: Match the request to the clinic's template set (from ~/.claude/plugins/config/claude-for-legal/legal-clinic/CLAUDE.md).…
- Gather the facts: Read the intake summary or case notes. For each fact the document needs: do we have it? | Document needs | Have? |…
- Apply jurisdiction: Per ~/.claude/plugins/config/claude-for-legal/legal-clinic/CLAUDE.md jurisdiction: - Caption format: state and local…
- Draft: Use the practice-area template. Fill what can be filled from facts. Leave placeholders explicit — never fill with…
- Flag uncertainty: Three kinds of flags, in-line: - [FACT NEEDED: ...] — the document needs a fact the case notes don't have - [VERIFY…
- Supervision routing: Filing a document with a court or agency is a consequential action. The gate is the supervision workflow in ##…

## Supporting Files And Signals
- Referenced: ~/.claude/plugins/config/claude-for-legal/legal-clinic/CLAUDE.md
- Referenced: ~/.claude/plugins/config/claude-for-legal/legal-clinic/guides/<practice-area>.md
- Referenced: pedagogy_posture
- Referenced: [FACT NEEDED: client's entry date — get from I-94 or ask client]
- Referenced: [FACT NEEDED: ...]
- Referenced: [VERIFY: ...]
- Referenced: [UNCERTAIN: ...]
- Signal: code block: markdown

## Source Sections
- Purpose
- Load context
- Pedagogy check
- Workflow
- Step 1: Which document?
- Step 2: Gather the facts
- Step 3: Apply jurisdiction
- Step 4: Draft
- Step 5: Flag uncertainty
- Step 6: Supervision routing

## Batch Log Match
- Row: 218
- Canonical path: anthropics/claude-for-legal/legal-clinic/skills/draft/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-draft/mp4/claude-liam-draft.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
