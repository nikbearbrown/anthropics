# Source Details — healthcare--claude-liam-doc-extract

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Doc Extract.
- Family: healthcare
- Source sheet: /Users/nik/Documents/books/anthropics/healthcare/youtube/claude-liam-doc-extract/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/healthcare/plugins/healthcare/skills/doc-extract/SKILL.md
- Name: doc-extract
- Description: Extract plain text from a document file - PDF, DOCX, XLSX, PPTX, RTF, or plain text/markdown/HTML. Use when a binary document needs to be turned into text, for example a contract PDF or an EHR DocumentReference attachment. Other skills (fhir) invoke scripts/extract.ts directly; the contracts MCP server bundles its own copy (servers/documents/src/extract.mjs) so its bundle stays self-contained — port fixes to both.

## Capabilities To Name On Screen
- Extract plain text from a document file - PDF
- or plain text/markdown/HTML
- Use when a binary document needs to be turned into text
- for example a contract PDF or an EHR DocumentReference attachment
- Other skills (fhir) invoke scripts/extract.ts directly

## Constraints / Failure Modes
- No explicit constraints extracted.

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: pdftotext -layout
- Referenced: --content-type
- Referenced: application/pdf
- Referenced: {"error": "..."}
- Referenced: package.json
- Referenced: scripts/
- Referenced: tsconfig.json
- Signal: code block: bash
- Signal: code block: json
- Signal: code block: ts

## Source Sections
- Setup (once)
- Use
- Table caveat
- For other skills

## Batch Log Match
- Row: 215
- Canonical path: anthropics/healthcare/plugins/healthcare/skills/doc-extract/SKILL.md
- MP4 path: anthropics/healthcare/youtube/claude-liam-doc-extract/mp4/claude-liam-doc-extract.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
