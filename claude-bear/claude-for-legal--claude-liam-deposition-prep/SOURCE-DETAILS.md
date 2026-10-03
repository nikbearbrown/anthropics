# Source Details — claude-for-legal--claude-liam-deposition-prep

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Deposition Prep.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-deposition-prep/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/litigation-legal/skills/deposition-prep/SKILL.md
- Name: deposition-prep
- Description: Build a deposition outline for a witness — pull their documents from the eDiscovery platform, organize topics around the case theory, and surface impeachment material. Use when the user says "depo prep for [witness]", "build a depo outline", or "prepare for [name]'s deposition".

## Capabilities To Name On Screen
- Build a deposition outline for a witness — pull their documents from the eDiscovery platform
- organize topics around the case theory
- and surface impeachment material
- Use when the user says "depo prep for [witness]"
- "build a depo outline"

## Constraints / Failure Modes
- If the user's jurisdiction includes England & Wales and they're asking for a trial witness statement for the Business & Property Courts (or any CPR-governed proceeding)…
- Before producing output, check where it's going. If the user has named a destination (a channel, a distribution list, a counterparty, "everyone"), ask whether it's…
- Verbatim quotes from the record must be verbatim. Never put quotation marks around words attributed to opposing counsel, the witness, another deponent, the court, or any…
- Never fill the gap. An invented prior statement destroys the impeachment the moment the witness disavows it and the transcript doesn't back you up. Every [verify exact…
- Pinpoint cites must support the whole proposition. If an impeachment point is "the witness said X, Y, and Z on [date]," verify the pinpoint cite supports X AND Y AND Z.…
- Do not proceed on an unintaken matter. Intake is what runs conflicts and writes the _log.yaml row this skill reads from
- No silent supplement. If a research query to the configured legal research tool (Westlaw, CourtListener, Trellis, Descrybe, or firm platform) returns few or no results…
- Source attribution. Tag every rule reference, case cite, and authority in the outline with where it came from: [Westlaw], [CourtListener], [Trellis], [Descrybe], or the…

## Procedure / Sequence
- Who is this witness?: - Name, role, relationship to the case - Why are we deposing them — what do we need from this witness? The "why"…
- a: Witness posture — branch before drafting questions: Prep structure differs by posture. Identify the witness posture before writing a single question: - Adverse / hostile…
- Pull their documents: From the eDiscovery platform (Everlaw/Relativity/DISCO if connected): - Documents authored by witness - Documents sent…
- Build topics: Each topic is a thing you want to establish or explore. Organize around the theory: Background (always first — lock in…
- Write the outline: `markdown [WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see ## Who's using this] # Deposition…

## Supporting Files And Signals
- Referenced: ~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md
- Referenced: CLAUDE.md
- Referenced: [verify against record — Tr. p. __]
- Referenced: ~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml
- Referenced: _log.yaml
- Referenced: /litigation-legal:matter-intake
- Signal: code block: markdown

## Source Sections
- Witness statements for England & Wales — PD 57AC
- Destination check
- Purpose
- Record fidelity — quotes and pinpoints
- Oral calibration
- Load context
- Workflow
- Step 1: Who is this witness?
- Step 1a: Witness posture — branch before drafting questions
- Step 2: Pull their documents

## Batch Log Match
- Row: 206
- Canonical path: anthropics/claude-for-legal/litigation-legal/skills/deposition-prep/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-deposition-prep/mp4/claude-liam-deposition-prep.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
