# Source Details — skills--claude-liam-skill-creator

Generated: 2026-09-05T11:09:01

## Reel
- Question: Skill Creator
- Family: skills
- Source sheet: /Users/nik/Documents/books/anthropics/skills/youtube/claude-liam-skill-creator/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/skills/skills/skill-creator/SKILL.md
- Name: skill-creator
- Description: Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.

## Capabilities To Name On Screen
- Create new skills
- modify and improve existing skills
- and measure skill performance
- Use when users want to create a skill from scratch
- or optimize an existing skill

## Constraints / Failure Modes
- The skill creator is liable to be used by people across a wide range of familiarity with coding jargon. If you haven't heard (and how could you, it's only very recently…
- compatibility: Required tools, dependencies (optional, rarely needed)
- ├── SKILL.md (required)
- │ ├── YAML frontmatter (name, description required)
- Claude reads only the relevant reference file
- This goes without saying, but skills must not contain malware, exploit code, or any content that could compromise system security. A skill's contents should not surprise…
- This section is one continuous sequence — don't stop partway through. Do NOT use /skill-test or any other testing skill
- This is the only opportunity to capture this data — it comes through the task notification and isn't persisted elsewhere. Process each notification as it arrives rather…

## Procedure / Sequence
- Spawn all runs (with-skill AND baseline) in the same turn: For each test case, spawn two subagents in the same turn — one with the skill, one without. This is important: don't…
- While runs are in progress, draft assertions: Don't just wait for the runs to finish — you can use this time productively. Draft quantitative assertions for each…
- As runs complete, capture timing data: When each subagent task completes, you receive a notification containing total_tokens and duration_ms. Save this data…
- Grade, aggregate, and launch the viewer: Once all runs are done: 1. Grade each run — spawn a grader subagent (or grade inline) that reads agents/grader.md and…
- Read the feedback: When the user tells you they're done, read feedback.json: Empty feedback means the user thought it was fine. Focus your…
- Generate trigger eval queries: Create 20 eval queries — a mix of should-trigger and should-not-trigger. Save as JSON: The queries must be realistic…
- Review with user: Present the eval set to the user for review using the HTML template: 1. Read the template from assets/eval_review.html…
- Run the optimization loop: Tell the user: "This will take some time — I'll run the optimization loop in the background and check on it…

## Supporting Files And Signals
- Referenced: eval-viewer/generate_review.py
- Referenced: evals/evals.json
- Referenced: references/schemas.md
- Referenced: /skill-test
- Referenced: <skill-name>-workspace/
- Referenced: iteration-1/
- Referenced: iteration-2/
- Referenced: eval-0/
- Referenced: eval-1/
- Referenced: without_skill/outputs/
- Signal: code block: markdown
- Signal: code block: json
- Signal: code block: bash

## Source Sections
- Communicating with the user
- Creating a skill
- Capture Intent
- Interview and Research
- Write the SKILL.md
- Skill Writing Guide
- Report structure
- Executive summary
- Key findings
- Recommendations

## Batch Log Match
- Row: 12
- Canonical path: anthropics/skills/skills/skill-creator/SKILL.md
- MP4 path: anthropics/skills/youtube/claude-liam-skill-creator/claude-liam-skill-creator.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
