# Source Details — claude-for-legal--claude-liam-demand-draft

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Demand Draft.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-demand-draft/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/litigation-legal/skills/demand-draft/SKILL.md
- Name: demand-draft
- Description: Draft a demand letter from a completed intake, gated on a privilege / FRE 408 / waiver / admission checklist, with a .docx output, post-send checklist, and an offer to create a matter. Use when the user says "draft the demand", "write the [type] letter", or has a finished demand intake ready to turn into a sendable draft.

## Capabilities To Name On Screen
- Draft a demand letter from a completed intake
- gated on a privilege / FRE 408 / waiver / admission checklist
- with a .docx output
- post-send checklist
- and an offer to create a matter

## Constraints / Failure Modes
- Run the pre-draft gate: privilege filter, admission risk, accord-and-satisfaction, FRE 408 posture, waiver scan, tone, factual accuracy. Do not proceed until each is…
- Verbatim quotes must be verbatim. Never put quotation marks around words attributed to the counterparty, their counsel, a witness, or any document unless you have the…
- Never fill the gap. A misquoted contract provision in a demand letter is the fastest way to lose credibility with opposing counsel on the first round
- Every [verify exact quote] must be flagged in the reviewer note before the letter leaves
- Pinpoint cites must support the whole proposition. If the demand asserts "Section 4.2 requires payment within 30 days upon invoice receipt," the cited section must cover…
- > External deliverable: the drafted demand letter is sent to counterparty. Do NOT include a PRIVILEGED & CONFIDENTIAL — ATTORNEY WORK PRODUCT — PREPARED AT THE DIRECTION…
- The answers drive tone verb choice, the consequence language, the Without prejudice header (or its absence), the signature block, and the compliance deadline. A posture…
- ~/.claude/plugins/config/claude-for-legal/litigation-legal/demand-letters/[slug]/intake.md — required; refuse to proceed if missing

## Procedure / Sequence
- Seed doc: Check ~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md → Demand-letter practice → seed-doc table…
- Soft templates (used only when no seed doc): Each is a skeleton — headings and expected content. Deviate when the facts require. Payment demand skeleton: 1. Parties…

## Supporting Files And Signals
- Referenced: ~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md
- Referenced: matter-intake
- Referenced: CLAUDE.md
- Referenced: demand-received
- Referenced: ~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml
- Referenced: strategic_block: skipped
- Referenced: /demand-intake [slug] --resume-strategic
- Referenced: --skip-gate
- Referenced: --version=N
- Referenced: draft-vN.docx
- Signal: code block: markdown

## Source Sections
- Purpose
- Record fidelity — quotes and pinpoints
- Candor about weak arguments
- Echo vs repeat
- Side context
- Posture for this matter
- Jurisdiction assumption
- Load context
- Strategic-block skipped handling
- Flags

## Batch Log Match
- Row: 202
- Canonical path: anthropics/claude-for-legal/litigation-legal/skills/demand-draft/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-demand-draft/mp4/claude-liam-demand-draft.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
