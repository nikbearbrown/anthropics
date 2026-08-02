# Claude Code for Teachers Video Ideas

## Candidate 01 — Why "Never Generate a Grade" Fails Until You Write a Hook
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-code-for-teachers/youtube/vox-hook-enforcement/vox-hook-enforcement-review.mp4`
- Source: `claude-code-for-teachers/chapters/08-hooks.md`
- Topic: CLAUDE CODE FOR TEACHERS
- Hook: A rule written in plain English to an AI system is a request, not a constraint — the AI weighs it probabilistically and can lose the vote.
- Key case: A teacher types "NEVER generate a final grade" in all-caps into CLAUDE.md. Two sessions later, asked to "summarize this student's performance," Claude returns: "Overall performance: B+."
- The Question: A CLAUDE.md instruction should prevent grade generation. Here is the session where it did not. Why?
- Core idea: CLAUDE.md is advisory — Claude probabilistically follows it; a Hook is a script that intercepts the tool call before it executes, making the rule mechanically enforced regardless of what Claude decides.
- Visual object: A two-lane diagram — left lane labeled "CLAUDE.md advisory path" with a probability dial; right lane labeled "Hook enforcement path" with a gate/switch that physically blocks the Write call.
- Manim move: compare
- Example seed: Maria builds a grading tool for 28 students. She adds one CLAUDE.md rule: "Never write a letter grade." On session 3, she asks Claude to draft a summary report. Claude writes "Grade: A-" in file student-07.md. She runs her PreToolUse hook on a fresh project; sends the same prompt; the hook intercepts, exits non-zero with "BLOCKED: grade pattern detected," and the file is never written.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: Basic understanding that CLAUDE.md is a file Claude reads at session start
- Exclusions: No shell scripting tutorial, no regex deep-dive, no full settings.json walkthrough, no history of enforcement systems
- Score: 9/10

---

## Candidate 02 — Why the Agentic Loop Can Delete Your Files Before You Finish Reading the Plan
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-code-for-teachers/youtube/vox-agentic-loop/vox-agentic-loop-review.mp4`
- Source: `claude-code-for-teachers/chapters/02-first-terminal-session.md`
- Topic: CLAUDE CODE FOR TEACHERS
- Hook: Claude.ai produces text you can ignore; Claude Code executes actions that change your file system before you have a chance to read the explanation.
- Key case: A teacher opens Claude Code for the first time on a class-website project, types a request, and watches Claude begin editing files — modifying styles.css, adding a dependency, changing a path — while the explanation is still scrolling.
- The Question: A chatbot should produce text the user reviews before anything changes. Here is the system where file changes happen inside the same loop as the explanation. Why?
- Core idea: Claude Code runs an agentic loop — gather context, take action, verify result, loop — that can execute multiple file changes before returning control; plan mode is the interruption point that makes the plan visible before execution begins.
- Visual object: A looping cycle diagram with three nodes (Gather / Act / Verify) and a blinking cursor at "Act" showing a file being modified in real time.
- Manim move: trace
- Example seed: Teacher opens terminal in ~/class-website. Types: "Add a contact page." Claude reads index.html, proposes a plan, then immediately begins writing contact.html, modifying nav in index.html, and installing a form library — all before the teacher can read the output. In plan mode (Shift+Tab twice), the same request produces a proposal only; nothing executes until the teacher edits and approves.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: Knows what a terminal is; has used Claude.ai or ChatGPT
- Exclusions: No npm install walkthrough, no full Claude Code installation tutorial, no comparison with GitHub Copilot or other tools, no discussion of API keys
- Score: 9/10

---

## Candidate 03 — Why AI Feedback That Passes Every Check Can Still Harm Your Students
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-code-for-teachers/youtube/vox-ai-feedback-bias/vox-ai-feedback-bias-review.mp4`
- Source: `claude-code-for-teachers/chapters/09-dangerous-middle.md`
- Topic: CLAUDE CODE FOR TEACHERS
- Hook: The most dangerous AI output isn't the one that's obviously wrong — it's the one that passes every test you thought to write and is systematically biased against a specific group of students.
- Key case: Seth opens three per-student flag reports from his grading tool. Marcus's report is accurate. Sara's report (ESL student, strong arguments, non-standard prepositions) recommends "grammar review before content review" — deprioritizing her strongest work. Jaden's report flags AAVE grammatical features as "errors." Both reports passed every automated handoff condition in the system.
- The Question: High rubric-grading accuracy (0.86–0.93 correlation with human raters) should predict safe AI feedback generation. Here is documented underperformance of up to 25% on AAVE-using students on the same systems. Why?
- Core idea: LLM rubric assessment bias is concentrated precisely in the 7–14% disagreement zone — the ESL and AAVE cases where teacher judgment matters most — so high overall accuracy masks systematic disadvantage for specific student populations; the structural fix is the narrowing principle: Claude detects patterns, the teacher writes per-student feedback.
- Visual object: A distribution curve showing 0.86–0.93 agreement in the middle, with the disagreement zone highlighted at the tails — and student names (Sara, Jaden) placed in the tail.
- Manim move: split
- Example seed: A teacher runs the grading tool on 25 submissions for a persuasive essay assignment. The cohort-pattern report correctly identifies "thesis present but unfocused" as the most common issue (18/25 submissions). For student Keisha, who writes in AAVE, the tool flags "non-standard grammar throughout; thesis acceptable" — correct grammar by rubric standards, wrong interpretation of what those grammatical choices mean. Teacher reads the flag, knows Keisha, writes feedback that engages with the argument rather than the surface.
- Length band: 3–5 min
- Still lanes: geo
- Prerequisites: Basic understanding of AI-generated feedback; no statistics required
- Exclusions: No Bayesian probability formalism, no NLP model architecture explanation, no second bias case (only ESL/AAVE), no history of standardized-testing bias literature
- Score: 9/10

---

## Candidate 04 — Why "Add a Page to My Website" Takes 45 Minutes When the 90-Second Version Takes 12
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-code-for-teachers/youtube/vox-spec-saves-time/vox-spec-saves-time-review.mp4`
- Source: `claude-code-for-teachers/chapters/04-prompts-to-specifications.md`
- Topic: CLAUDE CODE FOR TEACHERS
- Hook: A vague request to an AI agent doesn't save time — it delegates four decisions to the agent's defaults, and the defaults are wrong for your specific project.
- Key case: Two teachers ask for the same thing: a syllabus page on a class website. Teacher A says "Add a syllabus page." Teacher B spends 90 seconds writing which file to create, what must not change, which CLAUDE.md rules apply, what done looks like, and what Claude must not do. Teacher A spends 45 minutes correcting a JavaScript-rendered table with a CDN-loaded font that their school server can't serve. Teacher B's page is done in 12 minutes.
- The Question: A detailed request should take longer and produce comparable results to a short request. Here is the case where the 90-second request took 12 minutes total and the 8-second request took 45 minutes. Why?
- Core idea: The five-element specification (operation, invariants, context, output format, negative constraint) moves four scope decisions — file path, CSS approach, JavaScript inclusion, external dependencies — from Claude's defaults to explicit human choices; the 90 seconds is the cost of making those decisions; the 45 minutes is the cost of not making them.
- Visual object: A five-cell table with "Request" column (blank or generic entries) versus "Specification" column (concrete specific entries for each element), side by side.
- Manim move: compare
- Example seed: Teacher wants to add a Resources page to ~/class-website. Request prompt: "Add a resources page." Result: Claude creates resources.html with a JavaScript accordion component, loads Google Fonts, adds inline styles. School server blocks googleapis.com. Teacher spends 38 minutes removing JS and fonts. Specification: "Create src/resources.html. Do not modify any other files. Per CLAUDE.md: vanilla HTML, no JS, no CDN fonts. Output: semantic list of links matching the existing page structure. Negative constraint: no JavaScript, no new dependencies." Result: clean page in 11 minutes.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: Has used Claude Code or any AI coding assistant at least once
- Exclusions: No Bloom's taxonomy, no formal prompt engineering theory, no comparison of different specification formats, no discussion of other tools
- Score: 9/10

---

## Candidate 05 — Why "Looks Good" Fails as a Gate and What to Write Instead
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-code-for-teachers/youtube/vox-handoff-conditions/vox-handoff-conditions-review.mp4`
- Source: `claude-code-for-teachers/chapters/05-handoff-conditions.md`
- Topic: CLAUDE CODE FOR TEACHERS
- Hook: "Looks good" is a feeling, not a condition — and a feeling can approve a build that silently fails three days later in front of a student.
- Key case: A teacher reviews Claude's output. The new About page renders. The nav link is there. CSS looks right. They approve and push. Three days later a student emails: the link from About to Syllabus doesn't work. The link used a page-relative path that worked on local dev and failed on the school server's outdated mod_rewrite. The condition that would have caught it — "every link on the new page resolves on the actual deployment, not just on local dev" — was never written.
- The Question: Reviewing output visually and verifying exit-0 should be sufficient to catch link failures before deployment. Here is the case where a link passed both checks and failed in production. Why?
- Core idea: A handoff condition must be specific (names the artifact and property), testable (verifiable by a command or explicit visual criteria), and binary (pass or fail) — "looks good" fails all three, and the conditions that catch deployment failures require checking against the actual deployment environment, not the local one.
- Visual object: A gate/threshold diagram with "weak condition" (fuzzy, has a question mark) on the left and "strong condition" (sharp, binary, has a checkmark or X) on the right; a bug icon slipping through the left but blocked by the right.
- Manim move: transform
- Example seed: Teacher builds a contact page. Weak condition: "page renders." Build passes, deployed. A student on a mobile device finds the mailto link fires but the page's CSS drops off at 375px width. Strong condition: "page renders at 375px mobile width with no horizontal scroll; every link on the page resolves to a real file at the expected path (run npm run lint-html); the change appears only in the new file and index.html nav." Both failures caught before deployment.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: Knows what a deployment is; has done at least one Claude Code build step
- Exclusions: No git diff walkthrough, no full deployment pipeline explanation, no discussion of CI/CD, no formal specification of the five handoff-condition questions in full
- Score: 8/10

---

## Candidate 06 — Why CLAUDE.md Breaks When It Gets Too Long
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-code-for-teachers/youtube/vox-claudemd-length/vox-claudemd-length-review.mp4`
- Source: `claude-code-for-teachers/chapters/03-claude-md.md`
- Topic: CLAUDE CODE FOR TEACHERS
- Hook: The file you write to control Claude's behavior works against you once it gets long enough — and most teachers make it too long within three builds.
- Key case: A teacher's CLAUDE.md grows to 340 lines across a semester: style rules, lessons learned, architecture notes, volatile sprint goals, some personal reminders. Claude starts violating the Tailwind prohibition from line 12. The rule hasn't changed. The file is just too noisy for Claude to give it full weight.
- The Question: Adding more rules to CLAUDE.md should make Claude more reliable. Here is the project where Claude began ignoring key rules as CLAUDE.md grew past 200 lines. Why?
- Core idea: CLAUDE.md competes with other context for attention; a 340-line file causes rule-following to degrade because Claude's instruction-following is probabilistic and higher-priority immediate-prompt content outweighs standing rules buried in long context — the fix is to keep CLAUDE.md under 200 lines by moving workflow-specific content to Skills and inviolable rules to Hooks.
- Visual object: A single scrolling document that grows longer and longer; a "rule compliance" meter visible alongside it that starts high and dips as the document hits 200, 300, 400 lines.
- Manim move: accumulate
- Example seed: Teacher starts with a 47-line CLAUDE.md after the class website build. After the grading tool (80 lines), it covers stack, code style, environment quirks, never-rules. After the simulation (220 lines), it includes sprint goals, a note about a colleague's phone number, and four near-duplicate CSS rules. Claude generates Tailwind classes on a new component despite "Vanilla CSS only" being in the file. Teacher trims to 95 lines, moves grading workflow to a Skill, converts the grade-generation rule to a Hook. Claude respects the CSS rule again.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: Has read or written a CLAUDE.md file at least once
- Exclusions: No context-window math or token-count discussion, no comparison of CLAUDE.md with other tools' context files, no full Skills/Hooks explanation (they're referenced only as the fix)
- Score: 8/10

---

## Candidate 07 — Why One Subagent Query Saved 48% of the Context Window
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-code-for-teachers/youtube/vox-subagent-context/vox-subagent-context-review.mp4`
- Source: `claude-code-for-teachers/chapters/10-subagents.md`
- Topic: CLAUDE CODE FOR TEACHERS
- Hook: When you ask Claude to research something in the same session where you're building something, the research doesn't just take time — it evicts your build from memory.
- Key case: A teacher's grading-tool session is at 30% context usage after an hour of focused build work. They ask Claude to investigate late-submission policy across three docs and a meeting-notes file. Claude reads everything inline. The session hits 78% context. Only 22% remains — barely enough for one feedback draft. The session quality starts degrading before the work is done.
- The Question: Adding a research task to a productive session should extend the session's usefulness. Here is the session where a 10-minute research task left only 22% of the context window for the remaining build work. Why?
- Core idea: A subagent is a Claude session spawned in its own isolated context window — it reads the 30 policy files, returns a three-paragraph summary, and the main session only sees the summary; the main session's build context is untouched.
- Visual object: Two context bars side by side — "without subagent" bar fills to 78% after research; "with subagent" bar stays at 30% and receives only a summary-sized addition.
- Manim move: compare
- Example seed: Teacher builds a grade-flagging tool for 25 student submissions. At 35% context, she needs to understand how the LMS handles late-submission penalties. Without subagent: reads policy doc, three emails, LMS export — context jumps to 79%, session degrades, last five students get shallower analysis. With subagent: pattern-analyzer reads all 25 submissions in its own window, returns "top 5 misconceptions, outlier list, coverage table" (300 words). Main session receives 300 words. Context stays at 37%.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: Knows what a context window is; has experienced a Claude session getting slower over time
- Exclusions: No subagent configuration YAML walkthrough, no multi-agent orchestration patterns, no Writer/Reviewer pattern, no discussion of auto memory
- Score: 8/10

---

## Candidate 08 — Why the Simulation That Took 8 Minutes to Generate Wasn't Theirs
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-code-for-teachers/youtube/vox-simulation-ownership/vox-simulation-ownership-review.mp4`
- Source: `claude-code-for-teachers/chapters/12-three-file-system.md`
- Topic: CLAUDE CODE FOR TEACHERS
- Hook: Claude can build a working interactive simulation in 8 minutes — and the result will look professional, function correctly, and belong to nobody.
- Key case: A teacher types "build me an interactive sorting algorithm simulator." Claude builds it in 8 minutes — index.html, style.css, simulation.js. It works. It uses Material Design's default blue-white-gray palette, drag-and-drop interaction, and no pedagogical scaffolding. The teacher's class website uses four earth tones. The interaction model was supposed to be single-click stepping. The simulation works as code and does not work as the lesson.
- The Question: A specific natural-language request should produce output matching the requester's intent. Here is the simulation where a clear-sounding request produced a technically correct result that was pedagogically wrong for this classroom. Why?
- Core idea: One line of intent gives Claude the goal and nothing else — it fills every aesthetic, interaction, and pedagogical decision with defaults; the three-file system (CLAUDE.md for technical constraints, DESIGN.md for the complete visual vocabulary, PROJECT.md Intent Layer for what students should understand) makes the human's decisions visible to Claude before any code is generated.
- Visual object: A blank project folder with three files appearing one at a time — CLAUDE.md, DESIGN.md, PROJECT.md — each labeled with what it constrains (technical / visual / pedagogical); then a simulation emerging that matches the files rather than the defaults.
- Manim move: accumulate
- Example seed: Teacher wants a bubble-sort visualizer in earth tones, single-click stepping, showing O(n²) intuitively. One-line prompt: generates blue Material Design with drag-and-drop. Three files first: DESIGN.md specifies six colors (terracotta, near-black, warm white, blue, gray, amber), interaction vocabulary (single-click forward, long-click backward, spacebar play/pause, no drag-and-drop), PROJECT.md Layer 1 says "student should understand why bubble sort scales as O(n²)." Resulting simulation: earth tones, click to step, comparison counter visible. Teacher recognizes it as hers.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: Has used any AI coding tool; basic familiarity with HTML
- Exclusions: No Brutalist design system history, no CSS custom properties tutorial, no comparison with other design systems (designmd.app, getdesign.md), no full six-principle framework
- Score: 8/10

---

## Candidate 09 — Why Rewriting the Wrong Fix Makes the Build Worse, Not Better
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-code-for-teachers/youtube/vox-rewind-respec/vox-rewind-respec-review.mp4`
- Source: `claude-code-for-teachers/chapters/05-handoff-conditions.md`
- Topic: CLAUDE CODE FOR TEACHERS
- Hook: When Claude produces wrong output, the instinct is to ask Claude to fix it — but that fix-on-top-of-failure pattern accumulates context pollution that makes the next prompt worse than if you had started over.
- Key case: A teacher's About page has a broken link (page-relative path, fails on the school server). They ask Claude to fix it. Claude patches the link. The patch introduces a second issue — a trailing slash the school's mod_rewrite doesn't handle. They ask for another fix. Now the session's context contains the original failure, the first failed fix, the second failure, and Claude is reasoning against all of it as if it's part of the desired result.
- The Question: Iteratively asking Claude to fix its own mistakes should converge on a correct solution. Here is the session where two forward-correction attempts compounded into a worse state than the original failure. Why?
- Core idea: Forward correction after a failed step pollutes the session context — Claude reasons against the failure history as if it's constraint; /rewind restores both the conversation and the file system to the checkpoint before the failure, and a respecified prompt with the failure mode as an explicit negative constraint executes cleanly.
- Visual object: Two paths from a failure point — "forward correction" path shows a growing tangle of patches stacked on the original error; "/rewind" path shows a clean restart with one revised specification that produces the correct result.
- Manim move: split
- Example seed: Teacher builds a contact page. Link to syllabus.html uses a page-relative path. Handoff condition catches it: "link 404s on school server." Teacher asks: "fix the broken link." Claude changes it to `./syllabus.html` — still relative, still wrong. Session context is now 60% failure history. Teacher runs /rewind to before the contact-page step. Rewrites specification: "All link paths must use absolute server-relative paths with leading /; never use page-relative paths." New execution produces `/syllabus.html`. Handoff condition passes.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: Has encountered a Claude Code build failure; knows what a prompt is
- Exclusions: No git revert comparison, no /clear versus /rewind distinction in depth, no context-window token math, no formal discussion of context pollution beyond the intuition
- Score: 8/10

---

## Candidate 10 — Why Your Students' CLAUDE.md Is the Best Evidence They Conducted the Build
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-code-for-teachers/youtube/vox-buildlog-assessment/vox-buildlog-assessment-review.mp4`
- Source: `claude-code-for-teachers/chapters/15-teaching-the-discipline.md`
- Topic: CLAUDE CODE FOR TEACHERS
- Hook: AI can generate the code but it cannot generate the record of the human decisions that governed the code — which makes the build log the assessment you can't fake.
- Key case: A CS teacher grades two student submissions for a class website build. Both look identical. Student A's build log shows five-element specifications, plan-mode edits, three handoff conditions, two /rewind moments, and a Lessons Learned entry in CLAUDE.md. Student B's build log is a list of one-line prompts with no gates. The code is the same. The discipline is not.
- The Question: If AI can generate working code, assessing the code output should measure AI capability rather than student capability. Here is the assessment artifact that measures what AI cannot produce for the student. Why?
- Core idea: A build log that captures specifications, plan-mode edits, handoff conditions, supervisory capacity labels, and /rewind moments cannot be cleanly generated by AI from the code alone because it records the human decisions made before and during execution — grading the build log measures the conducting discipline, not the output.
- Visual object: Two side-by-side build transcripts — one with labeled gates, capacity labels, /rewind entries; one with bare prompts; both producing the same code output but clearly different in what they show about the builder.
- Manim move: compare
- Example seed: Teacher assigns: build a three-page class website using Claude Code. Assessment rubric has five dimensions (specification quality, gate execution, handoff conditions, capacity labeling, lessons learned), each 0–4, for 20 points. Student Maya's build log: five-element spec for each page, Ctrl+G plan edit documented, handoff condition "npm run lint-html exits 0 and mobile renders at 375px" documented, [PA] label when she caught a CDN font Claude tried to import, one /rewind documented with the respecification. Score: 17/20. Student output: identical to a peer who scored 7/20.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: Teaches a class that uses AI tools; familiar with rubric-based assessment
- Exclusions: No academic integrity policy discussion, no plagiarism detection comparison, no build-log rubric scoring in full, no peer-review methodology
- Score: 8/10
