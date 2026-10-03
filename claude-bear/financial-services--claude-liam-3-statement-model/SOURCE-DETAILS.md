# Source Details — financial-services--claude-liam-3-statement-model

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, 3 Statement Model.
- Family: financial-services
- Source sheet: /Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-3-statement-model/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/agent-plugins/model-builder/skills/3-statement-model/SKILL.md
- Name: 3-statement-model
- Description: Complete, populate and fill out 3-statement financial model templates (Income Statement, Balance Sheet, Cash Flow Statement) . Use when asked to fill out model templates, complete existing model frameworks, populate financial models with data, complete a partially filled IS/BS/CF framework, or link integrated financial statements within an existing template structure. Triggers include requests to fill in, complete, or populate a 3-statement model template

## Capabilities To Name On Screen
- populate and fill out 3-statement financial model templates (Income Statement
- Balance Sheet
- Cash Flow Statement)
- Use when asked to fill out model templates
- complete existing model frameworks

## Constraints / Failure Modes
- If running inside Excel (Office Add-in / Office JS): Use Office JS directly. Write formulas via range.formulas = [["=D14*(1+Assumptions!$B$5)"]] — never range.values for…
- Office JS merged cell pitfall: Do NOT call .merge() then set .values on the merged range — throws InvalidArgument because the range still reports its pre-merge…
- Every projection cell, roll-forward, linkage, and subtotal MUST be an Excel formula — never a pre-computed value
- The ONLY cells that should contain hardcoded numbers are: (1) historical actuals, (2) assumption drivers in the Assumptions tab
- Why: the model must flex when scenarios toggle or assumptions change. Hardcodes break every downstream integrity check silently
- Do NOT populate the entire model end-to-end and present it complete — break at each statement, show the work, catch errors early
- Keep colors minimal. Use only blues and greys for cell fills. Do NOT introduce greens, yellows, oranges, or multiple accent colors — a clean model uses restraint
- Note: The following margin analysis should only be performed if prompted by the user or if the template explicitly requires it. If no prompt is given, skip this section

## Procedure / Sequence
- Analyze the Template Structure: Before entering any data, thoroughly review the template to understand its architecture: Identify Input vs. Formula…
- Filling in Data Without Breaking Formulas: Golden Rules for Data Entry | Rule | Description | |------|-------------| | Only edit input cells | Never overwrite…
- Validating Formulas: Formula Integrity Checks Before relying on template outputs, validate that formulas are functioning correctly: | Check…
- Quality Checks by Sheet: Perform these validation checks on each sheet after populating the template: Income Statement (IS) Quality Checks…
- Cross-Statement Integrity Checks: After validating individual sheets, confirm the three statements are properly integrated: | Check | Formula | Expected…
- Final Review: Before considering the model complete: - Toggle through all scenarios (if applicable) to verify checks pass in each…

## Supporting Files And Signals
- Referenced: range.formulas = [["=D14*(1+Assumptions!$B$5)"]]
- Referenced: range.values
- Referenced: context.workbook.worksheets.getItem(...)
- Referenced: ws["D15"] = "=D14*(1+Assumptions!$B$5)"
- Referenced: recalc.py
- Referenced: .merge()
- Referenced: .values
- Referenced: references/

## Source Sections
- ⚠️ CRITICAL PRINCIPLES — Read Before Populating Any Template
- Formatting — Professional Blue/Grey Palette (Default unless template/user specifies otherwise)
- Model Structure
- Identifying Template Tab Organization
- Understanding Template Structure
- Projection Period
- Margin Analysis
- Core Margins to Include
- Income Statement Layout with Margins
- Credit Metrics

## Batch Log Match
- Row: 91
- Canonical path: anthropics/financial-services/plugins/agent-plugins/model-builder/skills/3-statement-model/SKILL.md
- MP4 path: anthropics/financial-services/youtube/claude-liam-3-statement-model/mp4/claude-liam-3-statement-model.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
