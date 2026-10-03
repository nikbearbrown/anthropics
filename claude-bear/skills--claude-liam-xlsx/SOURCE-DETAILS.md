# Source Details — skills--claude-liam-xlsx

Generated: 2026-09-05T11:09:01

## Reel
- Question: XLSX
- Family: skills
- Source sheet: /Users/nik/Documents/books/anthropics/skills/youtube/claude-liam-xlsx/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/skills/skills/xlsx/SKILL.md
- Name: xlsx
- Description: Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like \"the xlsx in my downloads\") — and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliverable must be a spreadsheet file. Do NOT trigger when the primary deliverable is a Word document, HTML report, standalone Python script, database pipeline, or Google Sheets API integration, even if tabular data is involved.

## Capabilities To Name On Screen
- Use this skill any time a spreadsheet file is the primary input or output
- This means any task where the user wants to: open
- or fix an existing .xlsx
- or .tsv file (e.g.
- adding columns

## Constraints / Failure Modes
- description: "Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an…
- Every Excel model MUST be delivered with ZERO formula errors (#REF!, #DIV/0!, #VALUE!, #N/A, #NAME?)
- Never impose standardized formatting on files with established patterns
- #### Required Format Rules
- LibreOffice Required for Formula Recalculation: You can assume LibreOffice is installed for recalculating formula values using the scripts/recalc.py script. The script…
- "error_summary": { // Only present if errors found

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: scripts/recalc.py
- Referenced: scripts/office/soffice.py
- Referenced: errors_found
- Referenced: error_summary
- Referenced: #DIV/0!
- Referenced: pd.notna()
- Referenced: data_only=True
- Referenced: load_workbook('file.xlsx', data_only=True)
- Referenced: read_only=True
- Referenced: write_only=True
- Signal: code block: python
- Signal: code block: bash
- Signal: code block: json

## Source Sections
- All Excel files
- Professional Font
- Zero Formula Errors
- Preserve Existing Templates (when updating templates)
- Financial models
- Color Coding Standards
- Number Formatting Standards
- Formula Construction Rules
- Overview
- Important Requirements

## Batch Log Match
- Row: 17
- Canonical path: anthropics/skills/skills/xlsx/SKILL.md
- MP4 path: anthropics/skills/youtube/claude-liam-xlsx/claude-liam-xlsx.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
