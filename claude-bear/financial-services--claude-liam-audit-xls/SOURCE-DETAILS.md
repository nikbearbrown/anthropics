# Source Details — financial-services--claude-liam-audit-xls

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Audit Xls.
- Family: financial-services
- Source sheet: /Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-audit-xls/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/agent-plugins/earnings-reviewer/skills/audit-xls/SKILL.md
- Name: audit-xls
- Description: Audit a spreadsheet for formula accuracy, errors, and common mistakes. Scopes to a selected range, a single sheet, or the entire model (including financial-model integrity checks like BS balance, cash tie-out, and logic sanity). Triggers on "audit this sheet", "check my formulas", "find formula errors", "QA this spreadsheet", "sanity check this", "debug model", "model check", "model won't balance", "something's off in my model", "model review".

## Capabilities To Name On Screen
- Audit a spreadsheet for formula accuracy
- and common mistakes
- Scopes to a selected range
- a single sheet
- or the entire model (including financial-model integrity checks like BS balance

## Constraints / Failure Modes
- > - sheet — the current active sheet only
- ## Step 3: Model-integrity checks (MODEL scope only)

## Procedure / Sequence
- Determine scope: If the user already gave a scope, use it. Otherwise ask them: > What scope do you want me to audit? > - selection…
- Formula-level checks (ALL scopes): Run these regardless of scope: | Check | What to look for | |---|---| | Formula errors | #REF!, #VALUE!, #N/A, #DIV/0!…
- Model-integrity checks (MODEL scope only): If scope is model, identify the model type (DCF / LBO / 3-statement / merger / comps / custom) and run the appropriate…
- Report: Output a findings table: | # | Sheet | Cell/Range | Severity | Category | Issue | Suggested Fix |…

## Supporting Files And Signals
- Referenced: #N/A
- Referenced: #DIV/0!
- Referenced: =A1*1.05
- Referenced: 1.05

## Source Sections
- Step 1: Determine scope
- Step 2: Formula-level checks (ALL scopes)
- Step 3: Model-integrity checks (MODEL scope only)
- 3a. Structural review
- 3b. Balance Sheet
- 3c. Cash Flow Statement
- 3d. Income Statement
- 3e. Circular references
- 3f. Logic & reasonableness
- 3g. Model-type-specific bugs

## Batch Log Match
- Row: 103
- Canonical path: anthropics/financial-services/plugins/agent-plugins/earnings-reviewer/skills/audit-xls/SKILL.md
- MP4 path: anthropics/financial-services/youtube/claude-liam-audit-xls/mp4/claude-liam-audit-xls.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
