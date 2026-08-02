# Claude Code for Teachers — CLI Video Ideas ("X with Claude")

---

## Candidate 01 — Write a CLAUDE.md Constitution for a Classroom Project with Claude Code
- Source: claude-code-for-teachers/chapters/03-claude-md.md
- Lane: BUILD (Claude Code)
- Hook: One line in CLAUDE.md — "no backend, mailto: links only" — and the next session never proposes a form-processing endpoint you can't deploy.
- The artifact: a Claude-assisted CLAUDE.md generator that takes five inputs (deployment environment, code style deviations, test/verification commands, architectural decisions, environment quirks) and writes a project-appropriate CLAUDE.md in the five-element format — animated as each section building in dependency order.
- Prompt seed: `claude "Generate a CLAUDE.md for a class-website project with these constraints: (1) Bash: deployment=rsync, no npm build step; (2) Style: semantic HTML5 only, vanilla CSS, no Tailwind; (3) Verification: after any HTML change run npm run lint-html; (4) Architecture: static-HTML only, no backend, no api/* endpoints, contact forms are mailto: links; (5) Environment: school server uses old mod_rewrite, all paths end in .html, no trailing slash. Format with the five-element headings from the CLAUDE.md spec."`
- Read / check: verify the output has all five sections (Bash commands, style deviations, test runners, architectural decisions, environment quirks); verify the architectural section explicitly states "no backend" and "no /api/* endpoints"; verify the environment section names the mod_rewrite constraint; test by opening a new session with this CLAUDE.md and asking for a Contact page — Claude should propose a mailto: link, not a form endpoint.
- Human supplies: nothing — the ch.3 class-website example is fully synthetic.
- Output medium: screen-recording mp4 (terminal: five-input generation, CLAUDE.md output, validation session showing correct Contact page proposal)
- The change: remove the "no backend" line from the generated CLAUDE.md and re-run the Contact page request — verify Claude now proposes a form endpoint, demonstrating what the omission costs.
- Teardown angle: CLAUDE.md is not documentation — it is active context Claude reads at every session start; the cost of maintaining it is one line per constraint; the cost of not maintaining it is a session that re-derives all your decisions wrong.
- Exclusions: user-level CLAUDE.md hierarchy, managed policy locations, district-level enforcement.
- Score: 9/10

---

## Candidate 02 — Build a PreToolUse Hook That Blocks Grade Generation with Claude Code
- Source: claude-code-for-teachers/chapters/08-hooks.md
- Lane: BUILD (Claude Code)
- Hook: "NEVER generate a final grade" in CLAUDE.md lasts two sessions — a PreToolUse hook lasts forever; here's the twenty-line script that makes "do not" into "cannot."
- The artifact: a bash hook script (block-grades.sh) that reads proposed Write tool input from stdin, detects numeric grade patterns (85%, A-, B+, 5/5, 3 out of 5), and returns exit code 1 with a blocking message — plus a settings.json configuration wiring it to the PreToolUse event — animated as Claude proposing grade content and the hook intercepting it.
- Prompt seed: `claude "Write a PreToolUse hook script block-grades.sh that: reads proposed Write tool input from stdin as JSON, extracts the content field, uses grep -qE to detect grade patterns like [0-9]{1,3}%, [A-F][+-]?, [0-9]+/[0-9]+, [0-9]+ out of [0-9]+, and exits 1 with 'BLOCKED: content contains a final grade' if detected, exits 0 otherwise. Also write the settings.json PreToolUse configuration."`
- Read / check: verify the hook correctly blocks "Overall performance: B+" (contains B+); verify it correctly allows "The student showed strong analytical reasoning" (no grade pattern); verify the settings.json points to the correct hook path; test the hook by asking Claude to "summarize student performance" in a hooked session and verify the grade is blocked.
- Human supplies: nothing — the ch.7 grading tool context is the test environment — synthetic.
- Output medium: screen-recording mp4 (terminal: hook script written, settings.json configured, Claude blocked mid-generation, error message printed)
- The change: extend the hook to also detect letter grades in percentile ranges ("in the top 15%") and verify the pattern correctly distinguishes percentage quantities from grade patterns.
- Teardown angle: a CLAUDE.md instruction is probabilistic — Claude weights it and sometimes overrides it; a hook is deterministic — it executes mechanically regardless of prompt phrasing; the teacher gets reliability, not compliance.
- Exclusions: PostToolUse hooks, SessionStart hooks, HTTP endpoint hooks, full hook event lifecycle.
- Score: 9/10

---

## Candidate 03 — Deploy a Pattern-Analysis Subagent for a Grading Tool with Claude Code
- Source: claude-code-for-teachers/chapters/10-subagents.md
- Lane: BUILD (Claude Code)
- Hook: Policy research fills 48% of the session window — a subagent does the same research and returns three sentences, leaving the main build clean.
- The artifact: a custom subagent definition file (pattern-analyzer.md in .claude/agents/) that reads a student submissions directory, extracts common misconception patterns, and returns a structured three-section report (patterns found / severity / recommended feedback focus) — animated as the subagent running in isolation, main session context meter staying flat.
- Prompt seed: `claude "Write a pattern-analyzer subagent definition for .claude/agents/pattern-analyzer.md. It should: (1) accept a submissions directory and rubric file as inputs, (2) use only Read, Grep, Glob tools (no Write or Edit), (3) output a structured report: common_misconceptions (list), severity_by_section (dict), recommended_feedback_focus (3-sentence max). Include the YAML frontmatter with name, description, and tools."`
- Read / check: verify the subagent definition has correct YAML frontmatter (name, description, tools: Read/Grep/Glob only); verify it explicitly excludes Write and Edit tools; verify the output format is structured and under three sentences for feedback_focus; test by invoking the subagent on three synthetic submissions and verify main session context did not grow during the subagent run.
- Human supplies: three short synthetic student submissions (any topic — the book's CS assignment example works — synthetic).
- Output medium: screen-recording mp4 (terminal: subagent defined, invoked, structured report returned, /context showing flat main session usage)
- The change: add a WriterReviewer pattern — a second subagent that reviews the pattern-analyzer's output from a different context window — and verify this catches one additional error the first subagent missed.
- Teardown angle: a subagent is the discipline of keeping the main build clean by delegating context-heavy work; the summary that comes back is all the main session needs — the policy doc, meeting notes, and LMS export stay isolated.
- Exclusions: multi-agent orchestration architecture, Claude API parallel calls, autonomous agent systems.
- Score: 9/10

---

## Candidate 04 — Build a Simulation with the Three-File System with Claude Code
- Source: claude-code-for-teachers/chapters/12-three-file-system.md
- Lane: BUILD (Claude Code)
- Hook: "Build me a sorting simulator" produces Material Design blue and drag-and-drop — three files written first produce your class colors and single-click stepping.
- The artifact: a working single-file HTML/CSS/JS sorting algorithm simulator generated from three input files (CLAUDE.md technical constitution, DESIGN.md visual constitution with color palette and interaction model, PROJECT.md pedagogical intent) — animated as the three files being written, then Claude generating the simulator that matches all three specifications.
- Prompt seed: `claude "Using the three files in context — CLAUDE.md (vanilla JS, no framework, single-file), DESIGN.md (earth-tone palette: #8B7355 #6B8E6B #8B6B45 #9B8B7B, single-click stepping not drag-drop, 44px minimum touch targets), PROJECT.md (sorting algorithms: bubble/merge/quick, pedagogical annotations showing comparison count and swap count, designed for ninth-grade students) — generate index.html as a single deployable file. Do not use any color not in DESIGN.md. Do not use drag-and-drop interaction."`
- Read / check: verify the output HTML contains no framework imports (no React, Vue, Bootstrap); verify the color values in the CSS match DESIGN.md exactly; verify interaction is click-based (no mousedown drag handlers); verify comparison_count and swap_count are displayed; verify it runs locally by opening in browser.
- Human supplies: nothing — the three files are written by the teacher in the video — synthetic; the book's sorting simulator is the worked example.
- Output medium: screen-recording mp4 (three files written in terminal, then simulator generated, then browser opened showing the class-colored result)
- The change: modify DESIGN.md to add a contrast requirement (all text must have 4.5:1 contrast ratio) and re-run — verify Claude updates the color choices in the output without being told which specific colors to change.
- Teardown angle: the simulation that emerges is yours — the colors are yours, the interaction model is yours, the pedagogy is yours — because you decided each before Claude saw the project; the three-file system is what prevents "build me a simulator" from producing a generic demo.
- Exclusions: Brutalist Design System full framework, designmd.app catalog, full accessibility audit tooling.
- Score: 9/10

---

## Candidate 05 — Run the Three-Check Deployment Verification Protocol with Claude Code
- Source: claude-code-for-teachers/chapters/14-deploying-in-class.md
- Lane: BUILD (Claude Code)
- Hook: The simulator works on your laptop — the three-check protocol finds the font that won't load on the school network before thirty students hit a blank screen.
- The artifact: a deployment verification checklist runner that executes three checks (functional: does it run end-to-end on a clean browser profile; environment: does it work on the school's network restrictions; pedagogical: does it deliver the intended learning experience when used by a student who hasn't read the documentation) — animated as three checkboxes filling in sequentially.
- Prompt seed: `claude "Generate a deployment verification protocol for this classroom simulation: (1) Functional check — list five browser-console tests that confirm no errors, correct rendering at 375px and 1024px, and all three algorithms run to completion; (2) Environment check — list three network-sensitive elements to verify (CDN fonts, external APIs, CORS requests); (3) Pedagogical check — write a five-question teacher walkthrough that a ninth-grader should be able to answer after using the simulator for ten minutes without instruction."`
- Read / check: verify the functional check includes a mobile breakpoint test (375px); verify the environment check lists all external resource dependencies; verify the pedagogical check's questions are answerable from the simulator's on-screen annotations (not from reading the source code); test the environment check against the school's known network restrictions from CLAUDE.md.
- Human supplies: a running sorting simulator (from Candidate 04 or any synthetic equivalent); the school's network restrictions (real or synthetic — the book's cloudfront.net blocking example is the test case).
- Output medium: screen-recording mp4 (terminal: three checks run sequentially, one environmental failure caught and fixed before classroom deployment)
- The change: add a fourth check (accessibility: run axe-core in browser devtools) and verify it catches at least one contrast or keyboard-navigation issue.
- Teardown angle: the three-check protocol is not QA overhead — it is the fifteen minutes that prevents the forty-minute class where the demo doesn't work; each check catches failures that the other two are blind to.
- Exclusions: full WCAG 2.2 accessibility audit, LMS integration testing, screen-reader compatibility.
- Score: 9/10

---

## Candidate 06 — Write the Post-Build Document for a Classroom Tool with Claude Code
- Source: claude-code-for-teachers/chapters/16-post-build-document.md
- Lane: BUILD (Claude Code)
- Hook: What you built, what you delegated, what you kept, what you'd do differently — the five-section post-build document is the evidence your workflow is trustworthy.
- The artifact: a Claude-assisted post-build document generator that takes build session logs and SDD artifacts, then structures a five-section document (what was built, surface-routing decisions, delegation log with gate checks, verification evidence, reflection for next build) — animated as the five sections filling in from build artifacts.
- Prompt seed: `claude "Generate a post-build document for the sorting simulator project. Use this session log [paste simplified log]. Five sections required: (1) What was built (artifact description, deployed URL or path), (2) Surface-routing decisions (which tasks went to Claude Code, which stayed human-only and why), (3) Delegation log (what Claude did, what gate checks were run, what errors were caught), (4) Verification evidence (which checks passed, what was corrected before deployment), (5) Reflection (one thing that went wrong that the three-file system would have caught earlier; one thing to change next build)."`
- Read / check: verify the surface-routing section names at least one human-only task and the reason it stayed human; verify the delegation log names specific gate checks (not "reviewed output"); verify the reflection section names a concrete change (not "be more careful"); verify the document could serve as an AI-use disclosure to a supervisor.
- Human supplies: a simplified build session log (ten lines of key decisions and outputs — synthetic from the sorting simulator build).
- Output medium: screen-recording mp4 (terminal: log input, five-section document generated, disclosure-ready format highlighted)
- The change: ask Claude to score the delegation log on the four process dimensions from the claude book's AI-use log (task routed, gate check, error corrected, verification evidence) — verify the scoring matches what the document records.
- Teardown angle: the post-build document is not about proving AI use — it is about proving that the teacher's supervisory judgment was the deliverable; the sections record where the line was drawn, not just what was generated.
- Exclusions: institutional AI disclosure policy compliance, formal audit trail systems.
- Score: 8/10

---

## Candidate 07 — Design a Classroom Activity Around the Dangerous Middle with Claude Code
- Source: claude-code-for-teachers/chapters/09-dangerous-middle.md
- Lane: BUILD (Claude Code)
- Hook: You generate three classroom tasks where Claude is "clearly" right — then the students run the plausibility probe and find the bug in all three.
- The artifact: a classroom activity generator that produces three dangerous-middle task scenarios (tasks that look like pattern work but require one specific supervisory capacity), each with a teacher note naming which capacity is required and what the student probe should be — rendered as a three-card activity deck animated one card at a time.
- Prompt seed: `claude "Generate three dangerous-middle task scenarios for a high-school CS class using Claude Code. Each scenario: (1) a task description that reads as pure pattern work, (2) the actual bug Claude's output will contain, (3) the supervisory capacity required (PA/PF/TO/IJ/EI from the five-capacity taxonomy), (4) the specific probe the student should run to expose the bug. The three scenarios should each require a different capacity."`
- Read / check: verify each scenario names a different supervisory capacity; verify the stated bug is one that Claude's self-audit would miss; verify the probe is specific (a concrete input or question, not "check the output"); test at least one scenario by running it through Claude and confirming the bug appears.
- Human supplies: nothing — the GPA sort, SQL injection, and graph algorithm examples from ch.9 are the reference cases — synthetic.
- Output medium: screen-recording mp4 (terminal: three scenario cards generated, one scenario live-tested showing bug appears and probe catches it)
- The change: ask Claude to design a fourth scenario for a non-coding task (e.g., research synthesis or spreadsheet formula) and verify the dangerous-middle structure still applies outside code.
- Teardown angle: teaching the dangerous middle is teaching students to categorize their work before they delegate it — the three scenarios are the cases that build that categorization muscle, one probe at a time.
- Exclusions: full Bondi-Kelly 2025 automation-trust study pedagogy, formal CS education research.
- Score: 8/10

---

## Candidate 08 — Build a Specification Prompt Template for Student Assignments with Claude Code
- Source: claude-code-for-teachers/chapters/04-prompts-to-specifications.md
- Lane: BUILD (Claude Code)
- Hook: The student's weak prompt produces three different wrong functions — the specification template produces one correct function every time, because there's nothing left for Claude to guess.
- The artifact: a Python CLI that takes an assignment description and generates a five-element specification template (specific task with function signature, invariants, context pointers, output format, negative constraints) students can fill in before each Claude Code session — animated as the template populating from the assignment description.
- Prompt seed: `claude "Write spec_template.py: takes an assignment description as stdin, generates a five-element specification template: (1) specific_task (fill in: function signature with types), (2) invariants (fill in: constraints that must not change), (3) context (fill in: file paths / SDD sections / sample data), (4) output_format (fill in: what Claude should produce and then run), (5) negative_constraints (fill in: what Claude must NOT do or touch). Output as a markdown template with fill-in placeholders."`
- Read / check: verify the template includes a function signature slot (not just "task description"); verify negative_constraints is a separate section (not merged with invariants); verify the output_format includes a "then run" slot for the oracle command; test on the GPA sort assignment — the template should reject "help me sort students" as too vague for the specific_task field.
- Human supplies: nothing — the ch.8 grade-parsing assignment is the test case — synthetic.
- Output medium: screen-recording mp4 (terminal: weak assignment description in, five-element template out, student filling in each slot)
- The change: add a validation step that refuses to generate the template if the assignment description doesn't name a specific function or artifact — verify it catches "help me with the CSV stuff."
- Teardown angle: the specification template is the bridge between the assignment rubric and the Claude prompt — students who fill in all five slots are doing the planning work that prevents the three-wrong-draft loop.
- Exclusions: DSPy prompt optimization, full IEEE 830 standard, system prompt engineering for grading tools.
- Score: 8/10

---

## Candidate 09 — Define a Reusable Skill for Common Teacher Workflows with Claude Code
- Source: claude-code-for-teachers/chapters/07-skills.md
- Lane: BUILD (Claude Code)
- Hook: A grading skill you write once this semester runs every submission cycle forever — including for the teacher down the hall who has never written a prompt.
- The artifact: a Claude Code Skill definition file (.claude/skills/grade-pattern-analyzer.md) that encodes a grading workflow (read submissions → extract pattern flags → format per-student report without final grade) — plus a demo showing the skill invoked by name on a new submission set without re-specifying the workflow.
- Prompt seed: `claude "Write a Claude Code Skill definition for .claude/skills/grade-pattern-analyzer.md. The skill should: (1) accept a submissions directory and rubric.md as inputs, (2) scan each submission for rubric criteria, (3) output a per-student markdown report with: strength flags, gap flags, and a 'recommended focus' sentence — but NO numeric or letter grade, (4) include YAML frontmatter with name, description, and input parameters. Demonstrate the skill being invoked with /grade-pattern-analyzer submissions/ rubric.md."`
- Read / check: verify the YAML frontmatter includes name, description, and parameter definitions; verify the output format explicitly excludes numeric and letter grades; verify the skill is invocable by name (not by re-pasting instructions); test on three synthetic submissions — each should produce a flag report without a grade.
- Human supplies: rubric.md for any assignment (synthetic — a simple 3-criteria rubric works); three short submissions (synthetic text matching or missing the criteria).
- Output medium: screen-recording mp4 (terminal: skill defined, saved, invoked on new submissions, three pattern reports printed without grades)
- The change: add a second skill (feedback-drafter) that takes the pattern-analyzer output and drafts per-student feedback sentences, then chain the two skills — verify the chain runs without re-specifying the workflow.
- Teardown angle: a skill is the difference between a workflow you run once and a workflow you run every semester — the definition is written once by the teacher, invoked by name by anyone, and constrained the same way every time.
- Exclusions: Skill publication and sharing across districts, Claude API batch processing, LMS integration.
- Score: 8/10

---

## Candidate 10 — Map Your Build to What Students Are Reading with Claude Code
- Source: claude-code-for-teachers/chapters/15-teaching-the-discipline.md
- Lane: BUILD (Claude Code)
- Hook: You just built a grading tool with hooks and subagents — here's the exact chapter in the students book that corresponds to every decision you made.
- The artifact: a Python mapping tool that takes a list of build decisions (e.g., "added PreToolUse hook to block grade output," "used subagent for policy research," "wrote SDD before first prompt") and outputs a cross-reference table showing the matching chapter in Claude Code for Students and a one-sentence classroom activity for each — animated as the mapping table populating row by row.
- Prompt seed: `claude "Map these build decisions from a teacher's grading-tool build to the Claude Code for Students chapter that covers the same concept: (1) wrote CLAUDE.md before first session, (2) used a specification prompt with five elements, (3) ran a plausibility probe on sorting function, (4) added PreToolUse hook to block grade output, (5) deployed a pattern-analyzer subagent. For each: name the students book chapter, state the key concept, and suggest a 10-minute classroom activity using this mapping."`
- Read / check: verify the hook decision maps to ch.8/ch.9 (hooks / dangerous middle) in the students book; verify the specification prompt maps to ch.8 (prompts as specifications); verify each classroom activity is completable in ten minutes and uses the same concept the teacher implemented; verify there are no "read the book" activities — all must be active.
- Human supplies: a list of five build decisions from the teacher's recent grading tool build (the book's Act Two summary is the source — synthetic).
- Output medium: screen-recording mp4 (terminal: five decisions in, cross-reference table with chapter and activity out)
- The change: run the mapping on the Act Three (simulation) build decisions and verify the cross-reference correctly maps the three-file system to ch.7 (SDD) and the deployment verification to ch.13 (verification).
- Teardown angle: the teacher who has lived through the build knows something that makes the students book chapter real — the mapping tool turns that experience into pedagogical content the teacher can share on Monday.
- Exclusions: curriculum alignment to CS education standards (CSTA, AP CS), LMS integration of the activity design.
- Score: 7/10

