# Source Details — skills--claude-liam-pdf

Generated: 2026-09-05T11:09:01

## Reel
- Question: PDF
- Family: skills
- Source sheet: /Users/nik/Documents/books/anthropics/skills/youtube/claude-liam-pdf/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/skills/skills/pdf/SKILL.md
- Name: pdf
- Description: Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding watermarks, creating new PDFs, filling PDF forms, encrypting/decrypting PDFs, extracting images, and OCR on scanned PDFs to make them searchable. If the user mentions a .pdf file or asks to produce one, use this skill.

## Capabilities To Name On Screen
- Use this skill whenever the user wants to do anything with PDF files
- This includes reading or extracting text/tables from PDFs
- combining or merging multiple PDFs into one
- splitting PDFs apart
- rotating pages

## Constraints / Failure Modes
- IMPORTANT: Never use Unicode subscript/superscript characters (₀₁₂₃₄₅₆₇₈₉, ⁰¹²³⁴⁵⁶⁷⁸⁹) in ReportLab PDFs. The built-in fonts do not include these glyphs, causing them to…

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: writer.add_page(page)
- Referenced: page.extract_text()
- Referenced: page.extract_tables()
- Referenced: qpdf --empty --pages ...
- Referenced: forms.md
- Referenced: LICENSE.txt
- Referenced: reference.md
- Referenced: scripts/
- Signal: code block: python
- Signal: code block: bash

## Source Sections
- Overview
- Quick Start
- Python Libraries
- pypdf - Basic Operations
- pdfplumber - Text and Table Extraction
- reportlab - Create PDFs
- Command-Line Tools
- pdftotext (poppler-utils)
- qpdf
- pdftk (if available)

## Batch Log Match
- Row: 10
- Canonical path: anthropics/skills/skills/pdf/SKILL.md
- MP4 path: anthropics/skills/youtube/claude-liam-pdf/claude-liam-pdf.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
