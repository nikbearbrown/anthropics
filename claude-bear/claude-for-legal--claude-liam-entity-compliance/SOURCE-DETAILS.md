# Source Details — claude-for-legal--claude-liam-entity-compliance

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Entity Compliance.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-entity-compliance/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/corporate-legal/skills/entity-compliance/SKILL.md
- Name: entity-compliance
- Description: >

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- > The filing calendar depends on entity type, not just jurisdiction. Treating a "Delaware entity" as a single bucket is a common and consequential error — DE…
- > - DE LLC: No annual report required. Annual tax is a flat $300, due June 1. Statutory basis: 6 Del. C. § 18-1107(d) [verify current fee and date]
- > - DE LP: No annual report required. Annual tax is a flat $300, due June 1 (parallel to the LLC rule). Statutory basis: 6 Del. C. § 17-1109 [verify current]
- > A DE LLC is NOT required to file a March 1 annual report — writing that deadline for an LLC carries real risk (spurious "overdue" flags that mask actual June 1…
- # Disclaimer: deadlines are reference only — confirm with registered agent or Secretary of State
- For each entity, confirm the current filing schedule with the registered agent or the relevant Secretary of State. State filing schedules change (some states move from…
- For anything the user does not know, flag the entity × jurisdiction entry as unknown — do not populate dates from a cached reference. The user's next step is to confirm…
- > 1. What type of filing is required? (Annual report, franchise tax, confirmation

## Procedure / Sequence
- Load entity table: Read ~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md → ## Entity Management → Entity table. If the…
- For each entity × jurisdiction, confirm the filing requirements: For each entity, confirm the current filing schedule with the registered agent or the relevant Secretary of State.…
- Write the tracker: Generate ~/.claude/plugins/config/claude-for-legal/corporate-legal/entities/compliance-tracker.yaml with all entities…

## Supporting Files And Signals
- Referenced: ~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md
- Referenced: --init
- Referenced: --report
- Referenced: --update
- Referenced: --sweep
- Referenced: --audit
- Referenced: --export
- Referenced: type_unknown
- Referenced: due_soon
- Referenced: --rebuild
- Signal: code block: yaml

## Source Sections
- Purpose
- Important: deadline reference caveat
- Jurisdiction assumption
- Entity-type disambiguation (especially Delaware)
- Tracker file
- Mode 1: Initialise
- Step 1: Load entity table
- Step 2: For each entity × jurisdiction, confirm the filing requirements
- Step 3: Write the tracker
- Mode 2: Report

## Batch Log Match
- Row: 229
- Canonical path: anthropics/claude-for-legal/corporate-legal/skills/entity-compliance/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-entity-compliance/mp4/claude-liam-entity-compliance.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
