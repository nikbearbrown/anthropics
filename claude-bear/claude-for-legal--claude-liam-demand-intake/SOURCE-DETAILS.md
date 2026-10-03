# Source Details — claude-for-legal--claude-liam-demand-intake

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Demand Intake.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-demand-intake/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/litigation-legal/skills/demand-intake/SKILL.md
- Name: demand-intake
- Description: Pre-drafting context gathering for a demand letter — parties, facts, basis, leverage, BATNA, and privilege filters — written to a structured intake.md the demand-draft skill reads. Use when the user wants to prep a demand letter, run intake before drafting, or capture context for a payment demand, breach/cure notice, cease-and-desist, employment separation, or preservation demand.

## Capabilities To Name On Screen
- Pre-drafting context gathering for a demand letter — parties
- and privilege filters — written to a structured intake.md the demand-draft skill reads
- Use when the user wants to prep a demand letter
- run intake before drafting
- or capture context for a payment demand

## Constraints / Failure Modes
- Record the answers in the intake under a ## Posture section before ## Parties. These answers govern the rest of the intake and the downstream draft — do not fall back to…
- Demand compliance deadline — how long we give the recipient. Use the response window captured in ## Posture for this matter above; do not fall back to a practice-level…
- > - Skip — proceed to draft with only the core block; I'll flag strategic_block: skipped in the intake
- What's in our internal analysis that must NOT appear in the letter? (Facts we haven't verified, our doubts about our case, strategic reasoning, prior settlement…
- [What CANNOT appear in the draft]

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: ~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md
- Referenced: --full
- Referenced: /litigation-legal:demand-draft [slug]
- Referenced: customer | vendor | ex-employee | competitor | third-party | other
- Referenced: [CITE:___]
- Referenced: cease-desist
- Referenced: breach-cure
- Referenced: employment-separation
- Referenced: strategic_block: skipped
- Referenced: [SME VERIFY: leverage/tone/privilege not captured in intake]
- Signal: code block: yaml
- Signal: code block: markdown

## Source Sections
- Purpose
- Load context
- Flags
- The intake
- Posture for this matter (ask FIRST, before the core)
- Core — always asked (8 questions)
- Strategic — asked if material, or if --full
- Writing the intake
- Slug
- ~/.claude/plugins/config/claude-for-legal/litigation-legal/demand-letters/[slug]/intake.md

## Batch Log Match
- Row: 203
- Canonical path: anthropics/claude-for-legal/litigation-legal/skills/demand-intake/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-demand-intake/mp4/claude-liam-demand-intake.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
