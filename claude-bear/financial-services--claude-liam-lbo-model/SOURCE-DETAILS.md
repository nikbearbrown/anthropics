# Source Details — financial-services--claude-liam-lbo-model

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Lbo Model.
- Family: financial-services
- Source sheet: /Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-lbo-model/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/agent-plugins/model-builder/skills/lbo-model/SKILL.md
- Name: lbo-model
- Description: This skill should be used when completing LBO (Leveraged Buyout) model templates in Excel for private equity transactions, deal materials, or investment committee presentations. The skill fills in formulas, validates calculations, and ensures professional formatting standards that adapt to any template structure.

## Capabilities To Name On Screen
- This skill should be used when completing LBO (Leveraged Buyout) model templates in Excel for private equity transactions
- deal materials
- or investment committee presentations
- The skill fills in formulas
- validates calculations

## Constraints / Failure Modes
- IMPORTANT: When a file like LBO_Model.xlsx is attached, you MUST use it as your template - do not build from scratch. Even if the template seems complex or has more…
- Use Office JS (Excel.run(async (context) => {...})) directly — do NOT use Python/openpyxl
- The same formulas-over-hardcodes rule applies: set range.formulas, never range.values for anything that should be a calculation
- Merged cell pitfall: Do NOT call .merge() then set .values on the merged range (throws InvalidArgument — range still reports original dimensions). Instead: write value…
- Every calculation must be an Excel formula - NEVER compute values in Python and hardcode results into cells. When using openpyxl, write cell.value = "=B5B6" (formula…
- Use the template structure - Follow the organization in examples/LBO_Model.xlsx or the user's provided template. Do not invent your own layout
- Use proper cell references - All formulas should reference the appropriate cells. Never type numbers that should come from other cells
- Work section by section, verify with user at each step - Complete one section fully, show the user what was built, run the section's verification checks, and get…

## Procedure / Sequence
- Check the Template: * Does the cell already have a formula? If yes, verify it's correct and move on. * Is there a comment or note…
- Check the User's Instructions: * Did the user specify a particular calculation method? * Are there stated assumptions that affect this formula? * Any…
- Apply Standard Practice: * If neither template nor user specifies, use standard LBO modeling conventions * Document any assumptions you make *…

## Supporting Files And Signals
- Referenced: examples/LBO_Model.xlsx
- Referenced: LBO_Model.xlsx
- Referenced: Excel.run(async (context) => {...})
- Referenced: range.formulas = [["=B5*B6"]]
- Referenced: range.formulas
- Referenced: range.values
- Referenced: range.format.font.color
- Referenced: range.format.fill.color
- Referenced: .merge()
- Referenced: .values
- Signal: code block: bash

## Source Sections
- TEMPLATE REQUIREMENT
- CRITICAL INSTRUCTIONS FOR CLAUDE - READ FIRST
- Environment: Office JS vs Python
- Core Principles
- Formula Color Conventions
- Fill Color Palette — Professional Blues & Greys (Default unless user/template specifies otherwise)
- Number Formatting Standards
- Clarify Requirements First
- TEMPLATE ANALYSIS PHASE - DO THIS FIRST
- FILLING FORMULAS - GENERAL APPROACH

## Batch Log Match
- Row: 289
- Canonical path: anthropics/financial-services/plugins/agent-plugins/model-builder/skills/lbo-model/SKILL.md
- MP4 path: anthropics/financial-services/youtube/claude-liam-lbo-model/mp4/claude-liam-lbo-model.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
