# AI for Teachers: A Practitioner's Guide — CLI Video Ideas ("X with Claude")

## Candidate 01 — Build the Bastani Experiment: Simulate AI's Hidden Learning Loss with Claude

- Source: ai-for-teachers-a-practitioners-guide/chapters/02-the-phase-gate.md
- Lane: BUILD (Claude Code)
- Hook: An AI study tool boosted practice scores by 48% — then tank exam scores by 17% below the control group. The same data appears to show both success and failure simultaneously. How?
- The artifact: An animated bar chart (Manim) showing three conditions — GPT Base, GPT Tutor, Control — across two time points (assisted practice, unassisted exam). The bars grow during practice showing all three rising, then the GPT Base bar reverses sharply below control on the exam. The "learning loss" gap animates with a red band. Numbers sourced from the Bastani et al. 2025 PNAS study.
- Prompt seed: `claude "Using the Bastani et al. 2025 PNAS data (GPT Base: +48% practice, -17% exam vs. control; GPT Tutor: +127% practice, no deficit), write a Python/Manim script that animates a grouped bar chart showing practice vs. exam performance for all three conditions. Animate the bars growing in the practice phase, then transition to exam phase — GPT Base drops below zero. Mark the gap with a red annotation band labeled 'learning loss'. Include a title card: The same tool, two different outcomes."`
- Read / check: Verify the bar heights match the published PNAS figures. Check that the y-axis zero baseline is clear. Confirm the "learning loss" annotation text is legible at video resolution.
- Human supplies: Nothing — the Bastani numbers are published. Data is fully synthetic/replication of a published result. Real-data upgrade: run a small classroom pilot with and without scaffolded AI and substitute actual scores (only if authentic data is available and IRB-cleared).
- Output medium: Manim (animated bar chart with transition between practice and exam phases)
- The change: Add a second revision showing what happens if only the GPT Tutor design is used — the deficit disappears. Run the animation again with just two conditions. Label why: "system prompt + teacher-authored content = the real variable."
- Teardown angle: The tool didn't change. The interaction design did. This is what "human in the loop" actually means vs. what dashboard approval rates measure.
- Exclusions: Do not derive new statistical claims, do not discuss the PNAS correction (minor affiliation error), do not digress into general AI ethics.
- Score: 9/10

---

## Candidate 02 — Build the Twelve Gates: Map Every AI Task Against the Phase-Gate Framework with Claude

- Source: ai-for-teachers-a-practitioners-guide/chapters/02-the-phase-gate.md
- Lane: BUILD (Claude Code)
- Hook: Teachers report saving 4–7 hours a week with AI grading tools — yet a 99.4% approval rate still produces wrong feedback for every third student who complains. The click is not the operation.
- The artifact: An interactive D3 v7 HTML file rendering the twelve-gate cluster map as a sortable table — gate number, name, cognitive operation, downstream action, and risk tier (green/yellow/red). Each row expandable to show the cost of skipping. Color-coded by risk tier. Exported as a screen recording for the video.
- Prompt seed: `claude "Build a self-contained D3 v7 HTML file that renders the twelve teacher AI phase gates as an interactive sortable table. Columns: Gate #, Gate Name, Cognitive Operation (what must happen), Downstream Action (what is blocked until it does), Risk Tier (green/yellow/red). Color-code rows by tier. On row click, expand a panel showing 'Cost of skipping this gate.' Use inline CSS and D3 7.9.0 from cdnjs. Data: [paste the 12-gate table from the chapter]."`
- Read / check: Verify all 12 gates are present. Confirm color coding matches green/yellow/red tier definitions. Check that expandable panels show accurate cost descriptions. Ensure the sort function works in a browser before recording.
- Human supplies: Nothing — the twelve-gate data is in the chapter. Synthetic only. Real-data upgrade: a teacher supplies their own workflow mapped against the gates, with actual approval-rate logs.
- Output medium: screen-recording mp4 (browser interaction of the D3 table with hover/expand)
- The change: Add a 13th "custom gate" row that prompts the viewer to name their own workflow task, its cognitive operation, and its risk tier. Show the empty row in the final frame.
- Teardown angle: The gap between "human in the loop" and "the operation actually happened" is not a technology problem — it is a workflow design problem. The gate is the answer.
- Exclusions: Cut the surgical-timeout metaphor extended discussion; cut FERPA legal detail; cut the Chapter 9 professional-development thread.
- Score: 9/10

---

## Candidate 03 — Build the Jagged Frontier: Plot Where AI Helps vs. Hurts on Teaching Tasks with Claude

- Source: ai-for-teachers-a-practitioners-guide/chapters/02-the-phase-gate.md
- Lane: BUILD (Claude Code)
- Hook: BCG consultants with AI were 40% better on tasks AI handles well — and 19 points more likely to fail on tasks AI handles poorly. Both happened in the same experiment with the same tool. How do you know which side you're on?
- The artifact: A Manim scatter plot of 12–15 teaching tasks (quiz generation, live instruction, parent emails, IEP accommodations, etc.) plotted on axes "Task definition clarity" (x) vs. "AI reliability" (y). A jagged frontier line separates the high-reliability zone from the low-reliability zone. Tasks in the danger zone are highlighted red. The frontier animates — tasks snap into position as labeled dots.
- Prompt seed: `claude "Write a Manim Python scene that plots teaching tasks on a 2D grid: x-axis 'Task Definition Clarity' (low to high), y-axis 'AI Reliability' (low to high). Plot these tasks as labeled dots: [quiz generation, rubric scoring, parent email draft, live instruction, IEP compliance, behavioral crisis, content accuracy check, Socratic scaffolding, anonymization]. Draw a jagged frontier line separating high-reliability from low. Color tasks above the frontier green, below red. Animate each dot appearing with its label, then draw the frontier."`
- Read / check: Verify the task placements match the chapter's frontier logic (e.g., IEP compliance = red/below frontier; quiz generation = green/above). Check that the animation sequence is legible — not too fast.
- Human supplies: Nothing — fully synthetic task classification. Real-data upgrade: a teacher or department maps their own actual tasks against the grid using their district's AI platform.
- Output medium: Manim (animated scatter plot with frontier line)
- The change: Reveal a second layer: "Add one task you use AI for today" — show an empty labeled slot appear, then ask the viewer to mentally place it. End with a voiceover question: "Is it above or below the line?"
- Teardown angle: The frontier is jagged, not a straight line. The same AI tool can be safe for some tasks and dangerous for adjacent ones. Uniform policy ("review all AI output") can't replace task-specific gates.
- Exclusions: Cut the Dell'Acqua BCG study detail beyond the headline numbers; cut discussion of vendor market dynamics.
- Score: 8/10

---

## Candidate 04 — Build the Prompt Specification Gap: Watch AI Output Change as Prompts Get Specific with Claude

- Source: ai-for-teachers-a-practitioners-guide/chapters/03-prompting-that-works.md
- Lane: BUILD (Claude Code)
- Hook: Two teachers, same tool, same minute. One got reusable quiz items. One got generic trivia. The only difference was the prompt. The model didn't change — the specification did.
- The artifact: A side-by-side screen recording showing two actual Claude API calls running in sequence — the one-sentence Teacher A prompt vs. the four-component Teacher B prompt (role, context, task, constraints). Both outputs appear in terminal panes. A D3-rendered comparison table animates below: row by row, criteria vs. output quality. The contrast is visible.
- Prompt seed: `claude "Call the Claude API twice for the same task — generating a formative quiz on the American Revolution for 8th grade. First call: prompt = 'Generate quiz questions about the American Revolution.' Second call: use the four-component prompt template (role: veteran 8th-grade history teacher; context: 8th grade, students carry the taxation misconception; task: 8 multiple-choice items, one per cause, four choices, ban date-recall, 6th-grade reading level; constraints: target documented misconceptions as distractors). Print both outputs side by side. Then generate a comparison table showing: misconception targeted, reading level, item count, usability."`
- Read / check: Verify both API calls actually run. Confirm the four-component output targets the taxation misconception specifically. Check the reading level of both outputs (rough heuristic: sentence length). Confirm the comparison table renders correctly.
- Human supplies: Claude API key (or Claude.ai session). Nothing else synthetic needed.
- Output medium: screen-recording mp4 (terminal + browser table side by side)
- The change: A third prompt iteration — add a "close one gap" follow-up that addresses one visible weakness in the four-component output (e.g., the lab requires a week but the class meets tomorrow). Show how the output improves in a single additional round.
- Teardown angle: The model is a probability distribution conditioned on the prompt. A vague prompt requests the average. The average is never useful for a specific class. Specification is how you close the gap between what you typed and what you meant.
- Exclusions: Cut tool-comparison table (Claude vs. ChatGPT vs. Gemini); cut role-prompting research uncertainty; cut prompt library advice.
- Score: 9/10

---

## Candidate 05 — Build the Lesson Plan Backward: Automate Stages 1–2 Before Stage 3 with Claude

- Source: ai-for-teachers-a-practitioners-guide/chapters/04-lesson-planning-with-ai.md
- Lane: BUILD (Claude Code)
- Hook: Every AI lesson plan starts at Stage 3 — activities — and skips Stages 1 and 2. That is the flaw. 90 seconds of setup changes the output from generic to usable.
- The artifact: A screen recording of a terminal session: (1) the teacher types a two-sentence sticky note (Stage 1 target + Stage 2 evidence); (2) Claude generates a rich four-component prompt from those two sentences; (3) Claude generates the lesson plan from that prompt. Three rounds, annotated with voice. A final Manim slide shows the backward design flow with the "skip arrow" struck through in red.
- Prompt seed: `claude "I'm planning a 10th-grade biology lesson on cellular respiration. Stage 1 target: students explain how cellular respiration converts glucose energy to ATP, naming where each major stage occurs. Stage 2 evidence: a written trace of one glucose molecule from cytoplasm through mitochondrion, naming inputs and outputs. Now generate a rich four-component prompt (role, context, task, constraints) I can use to get a usable lesson plan draft from Claude. Include grade level, class profile (28 students, 3 newcomer ELLs, 2 IEPs), prior unit, standards target (NGSS HS-LS1-7), and specific constraints."`
- Read / check: Verify the generated prompt includes all four components. Check that the output lesson plan references the Stage 1 target explicitly. Confirm the NGSS standard is cited correctly (HS-LS1-7). Check that ELL differentiation appears.
- Human supplies: A real teacher's Stage 1 and Stage 2 sentences for their own unit (the 90-second sticky note). Optionally, a real class profile. Synthetic otherwise — the cellular respiration case is fully illustrative.
- Output medium: screen-recording mp4 (terminal session) + Manim closing slide (backward design diagram)
- The change: Show the PCK revision pass — the teacher changes the hook, swaps day 2/3 order, and replaces the exit ticket. Three moves, each annotated with the PCK reason the AI couldn't supply.
- Teardown angle: AI replaces the blank-page production time. The 30-minute PCK revision is not waste — it is the actual teaching work. The dividend lives in the substitution.
- Exclusions: Cut unit vs. lesson asymmetry detail; cut RAND equity data; cut platform tool comparison.
- Score: 8/10

---

## Candidate 06 — Build the Rubric Calibration Gate: Catch AI Grading Bias Before It Reaches Students with Claude

- Source: ai-for-teachers-a-practitioners-guide/chapters/02-the-phase-gate.md + chapters/05-assessment-grading-and-feedback-with-ai.md
- Lane: BUILD (Claude Code)
- Hook: Gate 1 costs 25 minutes. Skipping it costs 3–5 hours later. The math is obvious — so why do teachers skip it?
- The artifact: A screen recording of Claude scoring 5 sample essays against a rubric, followed by the teacher scoring the same 5 essays, followed by Claude generating a criterion-by-criterion comparison table showing where the two diverge. The divergence table animates (Manim or D3) with a traffic-light overlay — green match, yellow drift, red conflict.
- Prompt seed: `claude "I'm piloting an AI grading assistant for 8th-grade argument essays. Score these 5 essays [paste anonymized essays] against this rubric [paste rubric]. For each criterion, give a score and a one-sentence rationale. Output as a markdown table: Essay ID, Criterion, AI Score, AI Rationale."`  Then: `claude "I scored the same 5 essays as follows: [paste teacher scores]. Compare my scores to yours criterion by criterion. Where do we diverge? Generate a calibration report: which criteria are aligned (within 0.5 pts), which need discussion, and which should trigger rubric revision."`
- Read / check: Verify the AI scores are within a plausible range for the rubric. Check that the comparison table identifies actual divergences, not just noise. Confirm the calibration report gives actionable revision guidance, not vague language.
- Human supplies: 5 real or realistic anonymized student essays (or teacher-generated synthetic essays at varying quality levels). The rubric. Teacher's own scores. Synthetic stand-ins acceptable for the video; real data preferred for authenticity.
- Output medium: screen-recording mp4 (terminal session) + Manim/D3 calibration table with traffic-light overlay
- The change: Run the full bulk pass after calibration. Show how the rubric adjustment in the gate changes 8 of 120 scores that would have been biased — display those 8 as highlighted rows in the bulk output.
- Teardown angle: The gate is not about distrust. It is about the specific cognitive operation — "does this fit this student?" — that 3 seconds per approval cannot contain.
- Exclusions: Cut FERPA detail; cut parent-call narrative; cut IEP compliance gate.
- Score: 8/10

---

## Candidate 07 — Build the AI Workflow Decision Tree: Which Tasks to Delegate, Which to Keep with Claude

- Source: ai-for-teachers-a-practitioners-guide/chapters/12-building-your-ai-workflow.md
- Lane: BUILD (Claude Code)
- Hook: Every teacher's AI workflow is different — but the decision logic behind which tasks to delegate is the same. Build the tree once, use it every time.
- The artifact: A D3 v7 interactive decision tree rendered as a standalone HTML file. The root node: "Is this task bounded?" Two branches: yes → "Is failure quickly inspectable?" → delegate or explore-then-decide. No → protect. 8–10 teaching-specific task labels snap into their nodes as examples. Screen-recorded with the viewer following the logic for one real task.
- Prompt seed: `claude "Build a self-contained D3 v7 HTML file rendering an interactive decision tree for teacher AI task delegation. Root: 'Is this task bounded?' Branches: Yes → 'Is failure quickly inspectable?' → Yes: Delegate (green node); No: Explore-then-decide (yellow). No → Protect (red). Add 8 labeled example tasks as leaf annotations: quiz drafting (green), parent email draft (yellow), IEP accommodation decision (red), standards citation (yellow), live instruction (red), rubric scoring (yellow), FERPA anonymization (red), lesson plan structure (yellow). Clicking a leaf shows a one-sentence rationale. Inline CSS, D3 7.9.0 from cdnjs."`
- Read / check: Verify all 8 tasks route to the correct node per the chapter's framework. Check that the rationale tooltips are accurate. Confirm the tree renders legibly without overlap.
- Human supplies: Nothing — fully synthetic. Real-data upgrade: a teacher inputs their own task list and the tree re-routes based on their answers.
- Output medium: screen-recording mp4 (browser interaction of D3 decision tree)
- The change: Add a "log your own task" input at the root — teacher types a task name, answers the two questions, and the tree places it. Show one user entering a task and following the logic live.
- Teardown angle: The workflow decision is not made task by task under pressure. It is made once, written down, and consulted. The decision tree is the "build once, reuse" artifact.
- Exclusions: Cut prompt library and template detail; cut multi-tool platform comparison.
- Score: 7/10

---

## Candidate 08 — Research the Academic Integrity Line: Where Does AI Use Become Dishonesty with Claude

- Source: ai-for-teachers-a-practitioners-guide/chapters/13-academic-integrity-privacy-and-honest-use.md
- Lane: RESEARCH (Claude assistant)
- Hook: Every school has an AI policy. Almost none of them define where the line actually is. The line matters — and it is not where most people think.
- The artifact: A sourced 4-section research brief synthesized by Claude: (1) what existing academic integrity frameworks say about AI assistance vs. AI substitution; (2) the three tested detection methods and their error rates; (3) three worked examples showing how the same student behavior falls on different sides of the line under different definitions; (4) a one-page draft policy language section a teacher or department chair could adapt. Rendered as a formatted markdown document, screen-recorded as the synthesis builds.
- Prompt seed: `claude "Research the current state of AI academic integrity frameworks in K–12 and higher education. I need a sourced brief covering: (1) how existing honor codes define AI use vs. AI substitution — cite at least two institutional policies; (2) what peer-reviewed research says about AI detection tools (error rates, false positives on ELL students); (3) three worked examples showing identical student behavior classified differently under different definitions; (4) draft policy language distinguishing 'AI as tool' from 'AI as author.' Cite sources. Flag any claim you cannot verify."`
- Read / check: Verify the institutional policy citations are real and current. Check that detection error-rate claims match published research. Confirm the three worked examples are genuinely distinct, not variations on the same scenario. Flag any unverified claims for human follow-up.
- Human supplies: Nothing — Claude researches and synthesizes from public sources. Human must verify flagged claims against actual sources before using in a real policy. Synthetic/illustrative stand-in acceptable for the video; real policy verification is the NEXT STEP.
- Output medium: screen-recording mp4 (Claude chat session building the brief) + slate (the final formatted brief as a document image)
- The change: Ask Claude to stress-test its own draft: "What is the strongest argument that this policy language would harm ELL students or students with learning disabilities? Revise accordingly."
- Teardown angle: Policy language that says "do not use AI" without defining what "use" means is not a policy. It is a liability. The line must be drawn at the cognitive operation — did the student do the thinking?
- Exclusions: Cut FERPA/COPPA detail; cut detection-tool vendor comparisons; cut district-level compliance process.
- Score: 7/10
