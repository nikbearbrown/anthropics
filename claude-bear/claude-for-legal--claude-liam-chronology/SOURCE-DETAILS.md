# Source Details — claude-for-legal--claude-liam-chronology

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Chronology.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-chronology/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/litigation-legal/skills/chronology/SKILL.md
- Name: chronology
- Description: Build or update a chronology from declared document sources and uploads — dated events extracted, de-duped, and tagged by significance per the matter theory. Use when the user asks to build a chronology or timeline from a production or matter file, says "chron from the production" or "what happened when", or needs a working, statement-of-facts, or witness-specific timeline.

## Capabilities To Name On Screen
- Build or update a chronology from declared document sources and uploads — dated events extracted
- and tagged by significance per the matter theory
- Use when the user asks to build a chronology or timeline from a production or matter file
- says "chron from the production" or "what happened when"
- or needs a working

## Constraints / Failure Modes
- England & Wales (CPR 31.22): Documents obtained through disclosure are subject to the implied undertaking — you may only use them for the purpose of the proceedings in…
- Both / varies — ask the user per-chronology which side's framing to apply for significance tags. The underlying timeline is side-neutral; only the significance read…
- Do not proceed on an unintaken matter. Intake is what runs conflicts and writes the _log.yaml row this skill reads from. --documents mode (running against an ad-hoc…
- No silent supplement. If source coverage for an era of the matter is thin — fewer documents than expected for a claimed time window, a custodian whose mailbox isn't…
- Source attribution. Tag every chronology entry with where the event came from: the file path, Bates number, MCP connector, or declared document-storage source for events…
- Tagging reaches every section that states a legal conclusion, deadline, or computed date — not just timeline entries. The timeline is sourced from documents. The Gaps…
- Privilege flag per entry (only when privilege_posture == B-mixed). Three-state rule — never silently decide a subjective privilege test isn't met:
- priv: ok — source is confidently non-privileged (filings, regulatory correspondence, public docs, counterparty communications without our counsel). Used only when…

## Procedure / Sequence
- Privilege gate (runs first, every time): Chronology work pulls from documents. Documents are often privileged (attorney-client, work product, common interest…
- Identify document sources: --matter mode: 1. User-provided paths — anything dropped in this session (file paths, drive links, email exports). 2.…
- Pull + read: For each source with readable files: - PDFs, emails (.eml), .docx, .txt — read directly. - Email archives (Gmail…
- Extract events: For each document, identify dated events: - Email: [date] [sender] told [recipient] [subject/content] - Meeting: [date]…
- De-dupe: The same event surfaces in multiple documents: a meeting is on three calendars and produces a summary email — that's…
- Tag significance — per case theory: Read the pivot fact and key facts from matter.md (--matter mode) or from the configuration's ## Case theory section…
- Write: Default output is the working chronology. Variants on request.

## Supporting Files And Signals
- Referenced: ~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md
- Referenced: --matter
- Referenced: matter.md
- Referenced: history.md
- Referenced: --documents
- Referenced: Significance tags applied from [plaintiff / defense] perspective.
- Referenced: chronology.md
- Referenced: ~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml
- Referenced: _log.yaml
- Referenced: /litigation-legal:matter-intake
- Signal: code block: markdown

## Source Sections
- Disclosed-document use restrictions
- Purpose
- Modes
- Side framing (significance tags)
- Load context
- Workflow
- Step 0: Privilege gate (runs first, every time)
- Step 1: Identify document sources
- Step 2: Pull + read
- Step 3: Extract events

## Batch Log Match
- Row: 139
- Canonical path: anthropics/claude-for-legal/litigation-legal/skills/chronology/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-chronology/mp4/claude-liam-chronology.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
