# Source Details — k12-teacher-skills--claude-liam-k12-lesson-differentiation

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, K12 Lesson Differentiation.
- Family: k12-teacher-skills
- Source sheet: /Users/nik/Documents/books/anthropics/k12-teacher-skills/youtube/claude-liam-k12-lesson-differentiation/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/k12-teacher-skills/plugin/skills/k12-lesson-differentiation/SKILL.md
- Name: k12-lesson-differentiation
- Description: Adapts an existing K-12 lesson (math, ELA, science, or social studies) for students at different proficiency levels (below / at / above grade level). Load this skill BEFORE asking the teacher any clarifying question about the lesson, tiers, or student levels. Triggers on explicit asks to differentiate, tier, or scaffold a lesson, and on implicit signals like "my students are at different levels". Produces 1 teacher-facing differentiation plan + 3 student-ready tier documents as editable Word documents in a single output turn, rendered from one material-source JSON via bundled scripts (shared content is written once so tiers cannot drift). Uses the Learning Commons Knowledge Graph when connected; works without it. This skill adapts a lesson the teacher brings or names. Not for creating a new lesson from scratch — a new-lesson request that asks for differentiated or leveled materials is k12-lesson-planning's job, one package. Not for grading, rubrics, assessment feedback, or quizzes.

## Capabilities To Name On Screen
- Adapts an existing K-12 lesson (math
- or social studies) for students at different proficiency levels (below / at / above grade level)
- Load this skill BEFORE asking the teacher any clarifying question about the lesson
- or student levels
- Triggers on explicit asks to differentiate

## Constraints / Failure Modes
- description: Adapts an existing K-12 lesson (math, ELA, science, or social studies) for students at different proficiency levels (below / at / above grade level). Load…
- "The teacher" throughout this skill is the user you are talking with — the same person, never
- teacher can watch them check off; the only reason to skip this is that no such tool exists
- Teacher language only — name what the teacher is getting, never tool names, file names,
- never name a specific module, unit number, lesson number, or proprietary routine name anywhere
- conversation — use it directly, do not re-ask), Scenario B (teacher uploads a lesson — read it
- first; if unreadable, say so and ask to re-share, never silently fabricate), Scenario B
- ask them to paste or upload; fetching completes Step 1 only — the KG calls in Step 2 are still

## Procedure / Sequence
- Route (silent, before anything else): 1. Subject. Detect math / ELA / science / social studies from the source lesson or the request, then read the matching…
- Identify the source lesson: Follow the subject file's source-lesson section: Scenario A (lesson exists earlier in this conversation — use it…
- Ground in standards: If the LC Knowledge Graph is connected: follow the subject's section in references/learning-commons-kg.md — call BEFORE…
- The differentiation rules: Apply all eight rules (R1–R8) from the subject file to every differentiated lesson. The rules are subject-specific…
- The draft offer: The teacher gets the choice of a fast draft before the build. The offer is asked the same way as the clarify questions…
- Output (one turn): Runs immediately when the teacher chose the full set, or in the turn the draft is approved. Four artifacts — 1…
- Complete: The skill is complete when the teacher has confirmed they are satisfied with all four Word documents (5c). The closing…

## Supporting Files And Signals
- Referenced: references/math.md
- Referenced: references/ela.md
- Referenced: references/science.md
- Referenced: references/social_studies.md
- Referenced: find_standard_statement
- Referenced: find_curriculum_lessons
- Referenced: references/learning-commons-kg.md
- Referenced: differentiation.json
- Referenced: {"type": "from_shared", "key": …}
- Referenced: .html
- Signal: code block: bash

## Source Sections
- Keeping the teacher posted
- Step 0 — Route (silent, before anything else)
- Step 1 — Identify the source lesson
- Step 2 — Ground in standards
- Step 3 — The differentiation rules
- Copyright guardrail
- Step 4 — The draft offer
- Step 5 — Output (one turn)
- 5a. Write the complete differentiation.json (same turn)
- 5b. Render all four Word documents — one command, same turn

## Batch Log Match
- Row: 79
- Canonical path: anthropics/k12-teacher-skills/plugin/skills/k12-lesson-differentiation/SKILL.md
- MP4 path: anthropics/k12-teacher-skills/youtube/claude-liam-k12-lesson-differentiation/mp4/claude-liam-k12-lesson-differentiation.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
