# Source Details — skills--claude-liam-docx

Generated: 2026-09-05T11:09:01

## Reel
- Question: DOCX
- Family: skills
- Source sheet: /Users/nik/Documents/books/anthropics/skills/youtube/claude-liam-docx/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/skills/skills/docx/SKILL.md
- Name: docx
- Description: Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation.

## Capabilities To Name On Screen
- Use this skill whenever the user wants to create
- or manipulate Word documents (.docx files)
- Triggers include: any mention of 'Word doc'
- 'word document'
- or requests to produce professional documents with formatting like tables of contents

## Constraints / Failure Modes
- description: "Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc'…
- Legacy .doc files must be converted before editing:
- paragraph: { spacing: { before: 240, after: 240 }, outlineLevel: 0 } }, // outlineLevel required for TOC
- ### Lists (NEVER use unicode bullets)
- // ❌ WRONG - never manually insert bullet characters
- columnWidths: [4680, 4680], // Must sum to table width (DXA: 1440 = 1 inch)
- columnWidths: [7000, 2360] // Must sum to table width
- Always use WidthType.DXA — never WidthType.PERCENTAGE (incompatible with Google Docs)

## Procedure / Sequence
- Unpack: Extracts XML, pretty-prints, merges adjacent runs, and converts smart quotes to XML entities (&#x201C; etc.) so they…
- Edit XML: Edit files in unpacked/word/. See XML Reference below for patterns. Use "Claude" as the author for tracked changes and…
- Pack: Validates with auto-repair, condenses XML, and creates DOCX. Use --validate false to skip. Auto-repair will fix…

## Supporting Files And Signals
- Referenced: docx-js
- Referenced: .doc
- Referenced: npm install -g docx
- Referenced: WidthType.DXA
- Referenced: WidthType.PERCENTAGE
- Referenced: type: SectionType.NEXT_COLUMN
- Referenced: orientation: PageOrientation.LANDSCAPE
- Referenced: LevelFormat.BULLET
- Referenced: ShadingType.CLEAR
- Referenced: --merge-runs false
- Signal: code block: bash
- Signal: code block: javascript
- Signal: code block: xml

## Source Sections
- Overview
- Quick Reference
- Converting .doc to .docx
- Reading Content
- Converting to Images
- Accepting Tracked Changes
- Creating New Documents
- Setup
- Validation
- Page Size

## Batch Log Match
- Row: 6
- Canonical path: anthropics/skills/skills/docx/SKILL.md
- MP4 path: anthropics/skills/youtube/claude-liam-docx/claude-liam-docx.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
