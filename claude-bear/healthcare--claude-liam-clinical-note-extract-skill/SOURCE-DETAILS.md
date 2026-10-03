# Source Details — healthcare--claude-liam-clinical-note-extract-skill

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Clinical Note Extract Skill.
- Family: healthcare
- Source sheet: /Users/nik/Documents/books/anthropics/healthcare/youtube/claude-liam-clinical-note-extract-skill/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/healthcare/plugins/healthcare/skills/clinical-note-extract/SKILL.md
- Name: clinical-note-extract-skill
- Description: Extract structured data from clinical notes with span-level provenance and null-safety. Use when users say "extract [variables] from this note", "abstract this chart", "pull structured data from these notes", "what does this note say about [field]", or when building a chart-abstraction, registry, or cohort dataset from unstructured clinical text.

## Capabilities To Name On Screen
- Extract structured data from clinical notes with span-level provenance and null-safety
- Use when users say "extract [variables] from this note"
- "abstract this chart"
- "pull structured data from these notes"
- "what does this note say about [field]"

## Constraints / Failure Modes
- However the user supplied notes — pasted text, file paths, a directory, PDFs, a FHIR connector, a database query — resolve each to plain text using whatever tools you…
- Workers have no tools — they return only what they read (value, span, presence/temporality/experiencer, null_reason, unit). All checks happen in step 3. Because note…
- Read references/03-review.md. Produce one row per (note, field): note_id | field | value | presence/temporality/experiencer | span | check. Below it, the completion…
- Offer to write records + report to ~/.claude/data/healthcare/clinical-note-extract/<run-id>/. That directory is local working state, not an archive: do not copy it to…
- Worker emits, per field: {value, span, location, presence?, temporality?, experiencer?, null_reason?, unit?} — only what it read. Step 3 attaches span_verified plus…

## Procedure / Sequence
- Define schema: Read references/01-define-schema.md. Turn the user's request into a schema: each field is {desc, finding?, check?}.…
- Extract: However the user supplied notes — pasted text, file paths, a directory, PDFs, a FHIR connector, a database query…
- Validate: Runs here in the calling session. Deterministic — no model judgment. For every record: 1. Span check. For every…
- Report: Read references/03-review.md. Produce one row per (note, field): note_id | field | value |…

## Supporting Files And Signals
- Referenced: references/01-define-schema.md
- Referenced: {kind: "terminology"|"range"|"date"|"pattern"|"enum"|..., ...params}
- Referenced: note-extract-worker
- Referenced: references/rules.md
- Referenced: null_reason
- Referenced: bun <this skill dir>/scripts/batch.ts <notes-dir> <schema.json> records.jsonl
- Referenced: records.jsonl
- Referenced: span_verified
- Referenced: check.kind
- Referenced: (check.via, value)

## Source Sections
- Steps
- Step 1 — Define schema
- Step 2 — Extract
- Step 3 — Validate
- Step 4 — Report
- Output contract
- Optional — export as FHIR
- Prerequisites

## Batch Log Match
- Row: 149
- Canonical path: anthropics/healthcare/plugins/healthcare/skills/clinical-note-extract/SKILL.md
- MP4 path: anthropics/healthcare/youtube/claude-liam-clinical-note-extract-skill/mp4/claude-liam-clinical-note-extract-skill.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
