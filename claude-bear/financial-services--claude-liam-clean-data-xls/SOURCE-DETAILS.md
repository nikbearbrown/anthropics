# Source Details — financial-services--claude-liam-clean-data-xls

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Clean Data Xls.
- Family: financial-services
- Source sheet: /Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-clean-data-xls/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/vertical-plugins/financial-analysis/skills/clean-data-xls/SKILL.md
- Name: clean-data-xls
- Description: Clean up messy spreadsheet data — trim whitespace, fix inconsistent casing, convert numbers-stored-as-text, standardize dates, remove duplicates, and flag mixed-type columns. Use when data is messy, inconsistent, or needs prep before analysis. Triggers on "clean this data", "clean up this sheet", "normalize this data", "fix formatting", "dedupe", "standardize this column", "this data is messy".

## Capabilities To Name On Screen
- Clean up messy spreadsheet data — trim whitespace
- fix inconsistent casing
- convert numbers-stored-as-text
- standardize dates
- remove duplicates

## Constraints / Failure Modes
- Only overwrite in place with computed values when the user explicitly asks for it, or when no sensible formula equivalent exists (e.g. encoding/mojibake repair)

## Procedure / Sequence
- Scope: - If a range is given (e.g. A1:F200), use it - Otherwise use the full used range of the active sheet - Profile each…
- Detect issues: | Issue | What to look for | |---|---| | Whitespace | leading/trailing spaces, double spaces | | Casing | inconsistent…
- Propose fixes: Show a summary table before changing anything: | Column | Issue | Count | Proposed Fix | |---|---|---|---|
- Apply: - Prefer formulas over hardcoded cleaned values — where the cleaned output can be expressed as a formula (e.g.…

## Supporting Files And Signals
- Referenced: Excel.run(async (context) => {...})
- Referenced: range.values
- Referenced: range.formulas = [["=TRIM(A2)"]]
- Referenced: 3/8/26
- Referenced: 2026-03-08
- Referenced: #N/A
- Referenced: #DIV/0!
- Referenced: =VALUE(SUBSTITUTE(B2,"$",""))

## Source Sections
- Environment
- Workflow
- Step 1: Scope
- Step 2: Detect issues
- Step 3: Propose fixes
- Step 4: Apply

## Batch Log Match
- Row: 142
- Canonical path: anthropics/financial-services/plugins/vertical-plugins/financial-analysis/skills/clean-data-xls/SKILL.md
- MP4 path: anthropics/financial-services/youtube/claude-liam-clean-data-xls/mp4/claude-liam-clean-data-xls.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
