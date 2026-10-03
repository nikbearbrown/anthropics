# Source Details — k12-teacher-skills--claude-liam-k12-lesson-planning

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, K12 Lesson Planning.
- Family: k12-teacher-skills
- Source sheet: /Users/nik/Documents/books/anthropics/k12-teacher-skills/youtube/claude-liam-k12-lesson-planning/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/k12-teacher-skills/plugin/skills/k12-lesson-planning/SKILL.md
- Name: k12-lesson-planning
- Description: >

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- Creates a lesson plan, student-facing materials, and observation template. Load this skill BEFORE asking the teacher any clarifying question about grade, subject, topic…
- "The teacher" throughout this skill is the user you are talking with — the same person, never
- teacher can watch them check off; the only reason to skip this is that no such tool exists
- Teacher language only — name what the teacher is getting, never tool names, file names,
- file doesn't cover, follow its "no curriculum named" path and do not fake
- critical failure. Extract only what each call specifies, then proceed directly to Step 3 — do
- general best practice."* Do not invent KG citations or attribute content to curriculum
- structure, and non-negotiables. Respect the Copyright guardrail below — never reproduce

## Procedure / Sequence
- Route (silent, before anything else): 1. Subject. Determine the subject of the requested lesson from the prompt and any prior conversation: - math…
- Clarify: Read the subject file first — its clarify section defines the priorities and defaults. We usually ask 0–2 clarifying…
- Ground in standards: If the LC Knowledge Graph is connected: follow the subject's section in references/learning-commons-kg.md — call BEFORE…
- Build the lesson: Follow the subject file's build section: curriculum branching, grade-band structure, section structure, and…
- The draft offer: The teacher gets the choice of a fast draft before the build. The offer is asked the same way as the clarify questions…
- Output (one turn): Runs immediately when the teacher chose the full packet, or in the turn the draft is approved. The artifacts are…

## Supporting Files And Signals
- Referenced: references/math.md
- Referenced: references/ela.md
- Referenced: references/science.md
- Referenced: references/social_studies.md
- Referenced: find_standard_statement
- Referenced: references/learning-commons-kg.md
- Referenced: lesson.json
- Referenced: {"type": "from_shared", "key": …}
- Referenced: references/example_lesson.json
- Referenced: .html
- Signal: code block: bash

## Source Sections
- Keeping the teacher posted
- Step 0 — Route (silent, before anything else)
- Step 1 — Clarify
- Step 2 — Ground in standards
- Step 3 — Build the lesson
- Copyright guardrail
- Step 4 — The draft offer
- Step 5 — Output (one turn)
- 5a. Write the complete lesson.json (same turn)
- 5b. Render every Word document — one command, same turn

## Batch Log Match
- Row: 80
- Canonical path: anthropics/k12-teacher-skills/plugin/skills/k12-lesson-planning/SKILL.md
- MP4 path: anthropics/k12-teacher-skills/youtube/claude-liam-k12-lesson-planning/mp4/claude-liam-k12-lesson-planning.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
