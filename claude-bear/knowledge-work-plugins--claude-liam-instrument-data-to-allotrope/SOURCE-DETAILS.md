# Source Details — knowledge-work-plugins--claude-liam-instrument-data-to-allotrope

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Instrument Data To Allotrope.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-instrument-data-to-allotrope/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/bio-research/skills/instrument-data-to-allotrope/SKILL.md
- Name: instrument-data-to-allotrope
- Description: Convert laboratory instrument output files (PDF, CSV, Excel, TXT) to Allotrope Simple Model (ASM) JSON format or flattened 2D CSV. Use this skill when scientists need to standardize instrument data for LIMS systems, data lakes, or downstream analysis. Supports auto-detection of instrument types. Outputs include full ASM JSON, flattened CSV for easy import, and exportable Python code for data engineers. Common triggers include converting instrument files, standardizing lab data, preparing data for upload to LIMS/ELN systems, or generating parser code for production pipelines.

## Capabilities To Name On Screen
- Convert laboratory instrument output files (PDF
- TXT) to Allotrope Simple Model (ASM) JSON format or flattened 2D CSV
- Use this skill when scientists need to standardize instrument data for LIMS systems
- or downstream analysis
- Supports auto-detection of instrument types

## Constraints / Failure Modes
- Calculated values MUST include traceability via data-source-aggregate-document:
- Required metadata present
- When the user provides a file, check if allotropy supports it before falling back to manual parsing. The scripts/convert_to_asm.py auto-detection only covers a subset of…
- Only use if allotropy doesn't support the instrument. This fallback:
- For PDF-only files, extract tables using pdfplumber, then apply Tier 2 parsing

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: references/
- Referenced: scripts/
- Referenced: references/field_classification_guide.md
- Referenced: measurement-document
- Referenced: calculated-data-aggregate-document
- Referenced: data-source-aggregate-document
- Referenced: --strict
- Referenced: references/supported_instruments.md
- Referenced: scripts/convert_to_asm.py
- Referenced: references/examples/
- Signal: code block: python
- Signal: code block: json
- Signal: code block: bash

## Source Sections
- Workflow Overview
- Quick Start
- Output Format Selection
- Calculated Data Handling
- Validation
- Supported Instruments
- Detection & Parsing Strategy
- Tier 1: Native allotropy parsing (PREFERRED)
- Tier 2: Flexible fallback parsing
- Tier 3: PDF extraction

## Batch Log Match
- Row: 265
- Canonical path: anthropics/knowledge-work-plugins/bio-research/skills/instrument-data-to-allotrope/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-instrument-data-to-allotrope/mp4/claude-liam-instrument-data-to-allotrope.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
