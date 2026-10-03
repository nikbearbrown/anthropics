# Source Details — claude-for-legal--claude-liam-exam-forecast

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Exam Forecast.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-exam-forecast/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/law-student/skills/exam-forecast/SKILL.md
- Name: exam-forecast
- Description: >

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- Not magic. A forecast, not a prediction. The skill cannot tell you what's on the exam — it can tell you what's been on past exams and what's likely to recur based on…
- If only 1-2 past exams are available, say so explicitly — any pattern inferred from 1 exam is noise
- If the professor is new (no past exams available), skill can't forecast. Say so; fall back to syllabus-based "these are the subjects covered" only
- Topics covered in class that have NEVER been tested in past exams — don't skip these, but don't weight them heavily either
- Header — required, first line of the forecast, both in-chat and in the saved file. Per plugin config ## Outputs, every study output carries the verbatim study-notes…

## Procedure / Sequence
- Intake: - Which class are we forecasting for? - How many past exams from this professor are available? - Are they from the same…
- Read each past exam: For each past exam: - Format (number of questions, length, time limit, open/closed book) - Subject coverage (which…
- Cross-exam pattern analysis: Roll up what's consistent across exams: Stable patterns (appeared in most/all past exams): - Subject weights (e.g.…
- Forecast for the upcoming exam: Header — required, first line of the forecast, both in-chat and in the saved file. Per plugin config ## Outputs, every…
- Output location: Write to ~/.claude/plugins/config/claude-for-legal/law-student/exam-forecasts/[class]/forecast-[YYYY-MM-DD].md.…

## Supporting Files And Signals
- Referenced: ~/.claude/plugins/config/claude-for-legal/law-student/CLAUDE.md
- Signal: code block: markdown

## Source Sections
- Purpose
- Confidence discipline
- Load context
- Workflow
- Step 1: Intake
- Step 2: Read each past exam
- Step 3: Cross-exam pattern analysis
- Step 4: Forecast for the upcoming exam
- Subject weighting (historical)
- Question-style forecast

## Batch Log Match
- Row: 232
- Canonical path: anthropics/claude-for-legal/law-student/skills/exam-forecast/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-exam-forecast/mp4/claude-liam-exam-forecast.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
