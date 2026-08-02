# Claude for Education: A Practitioner's Guide — CLI Video Ideas ("X with Claude")

## Candidate 01 — Build a Rubric Adjective Detector with Claude
- Source: claude-for-education-a-practitioners-guide/chapters/08-rubrics-and-assessment-design.md
- Lane: BUILD (Claude Code)
- Hook: The rubrics most teachers use are written in a language Claude can game perfectly, because the criteria are aesthetic adjectives, not observable behaviors.
- The artifact: A Python CLI that reads a rubric (markdown or plain text) and classifies each criterion as either "observable" (can be verified without judgment) or "vague" (requires evaluator taste), then generates a rewritten version of each vague criterion as an observable behavioral description. The output is an animated diff showing the before/after criterion pairs.
- Prompt seed: `claude "Read this rubric and classify each criterion: observable (can be verified without evaluator judgment) or vague (requires taste/interpretation). For each vague criterion, rewrite it as a specific, observable behavior a student can demonstrate and an evaluator can check. Format: ORIGINAL | TYPE | REWRITTEN." < rubric.md`
- Read / check: Verify the rewritten criteria are genuinely observable — they should specify a count, a structure, a format, or a concrete action, not a quality level. Check that "clear argument" becomes something like "contains a claim statement in the first paragraph and at least two supporting examples with citations" — not "makes a clear and well-supported argument."
- Human supplies (Claude can't): A real rubric from their course or institution. The book's example rubric (with deliberately vague criteria) is acceptable as a synthetic stand-in.
- Output medium: d3 (animated) — a two-column comparison where vague criteria appear on the left, then the observable rewrites appear on the right cell by cell, with vague ones marked in amber.
- The change: Run the rewritten rubric back through Claude and ask it to produce a student submission that would score at the top level — then show which version (vague vs. observable) produces more meaningful differentiation in the AI-generated submission.
- Teardown angle: Vague rubric criteria don't fail because they're unclear to humans — they fail because they're too clear to AI: a model knows exactly how to produce output that sounds "insightful" without being insightful.
- Exclusions: Full rubric management system, auto-grading integration, student-facing rubric display.
- Score: 9/10

## Candidate 02 — Audit a Prompt for Cognitive Labor Transfer
- Source: claude-for-education-a-practitioners-guide/chapters/04-the-cognitive-labor-question.md
- Lane: BUILD (Claude Code)
- Hook: Most instructional prompts don't ask students to think — they ask Claude to think and students to observe. The difference is invisible in the output.
- The artifact: A Python script that takes an instructional prompt (as text) and produces a cognitive labor audit: which cognitive operations are required from the student vs. which are being delegated to the AI. The output includes a "cognitive labor ratio" score (0–100% human labor) and an animated breakdown showing each learning objective and who is doing the thinking for it.
- Prompt seed: `claude "Audit this instructional prompt for cognitive labor distribution. For each learning objective implied by the prompt, classify the cognitive operation as: (a) student-performed — student must do the thinking, (b) AI-performed — AI does the thinking and student observes, or (c) shared — both contribute. Return a labor ratio: % of cognitive operations that are student-performed." < prompt.txt`
- Read / check: Verify the audit correctly identifies "Ask Claude to explain X and summarize" as AI-performed (not student-performed, even though summarizing is involved); check that the ratio is calculated only on substantive cognitive operations, not on mechanical steps like "copy the output."
- Human supplies (Claude can't): One or more instructional prompts from their actual course materials. The book's example prompts (including the deliberately AI-heavy ones) are acceptable and work well for the video.
- Output medium: Manim — a horizontal bar chart where each learning objective is a row; bars animate to show the student/AI/shared split for each, then a summary ratio bar appears at the bottom.
- The change: Rewrite the same instructional prompt to shift cognitive labor back to the student (e.g., "predict the answer before asking Claude, then compare"), re-run the audit, and show the ratio change.
- Teardown angle: Cognitive labor is zero-sum in the moment: every operation the AI performs is one the student doesn't. The ratio isn't a judgment about AI use — it's a diagnostic for whether the assignment is still doing what it was designed to do.
- Exclusions: Full LMS integration, automated assignment redesign, student-facing cognitive tracking.
- Score: 9/10

## Candidate 03 — Build an Assessment Vulnerability Map with Claude
- Source: claude-for-education-a-practitioners-guide/chapters/07-assessment-in-the-ai-era.md
- Lane: BUILD (Claude Code)
- Hook: Every assessment has an AI vulnerability level — and most educators don't know what theirs is until a student submits something that passes but wasn't written by them.
- The artifact: A Python CLI that takes a list of assessments (description + format for each) and scores each on three dimensions: AI-completability without domain knowledge (0–10), AI-detectability of use (0–10), and learning-validity-at-risk (0–10). The output is an animated vulnerability matrix with each assessment plotted by completability vs. detectability, colored by learning risk.
- Prompt seed: `claude "Score each assessment on three dimensions from 0–10: (1) AI-completability without domain knowledge — how easily can a frontier AI complete this without any real understanding? (2) AI-detectability — how easy is it to detect AI use in the output? (3) Learning-validity-at-risk — if AI completes this, how much of the intended learning is lost? For each, state the key reason for your score." < assessments.txt`
- Read / check: Verify the scores are internally consistent (a take-home essay should score higher on completability than an in-class oral defense); check that the "learning-validity-at-risk" scores align with the assignment's stated learning objectives rather than just the format.
- Human supplies (Claude can't): A list of 8–12 assessments from their course or institution. The book's example assessment list (covering the full spectrum from high-risk to low-risk) is acceptable.
- Output medium: d3 (animated) — a scatter plot where each assessment appears as a dot at its (completability, detectability) coordinates, colored by learning risk; dots animate in one by one with labels.
- The change: Take the two highest-vulnerability assessments and apply the book's redesign patterns (add oral component, convert to process portfolio, add AI-use reflection requirement), re-score, and show the dots moving to lower-risk positions.
- Teardown angle: Vulnerability isn't a binary — it's a spectrum. The matrix doesn't tell you to ban AI; it tells you which assessments need redesign first and what kind.
- Exclusions: Student-facing vulnerability disclosure, automated assessment redesign, integration with gradebook systems.
- Score: 9/10

## Candidate 04 — Backward-Design a Lesson Outcome with Claude
- Source: claude-for-education-a-practitioners-guide/chapters/02-learning-outcomes-before-prompts.md + chapters/03-the-instructional-brief.md
- Lane: BUILD (Claude Code)
- Hook: Most AI-assisted lesson design starts with the prompt and then figures out what students were supposed to learn — which is exactly backward from how learning design works.
- The artifact: A Python CLI that takes a topic + grade level + available AI tools and produces a backward-designed lesson plan: desired outcome first, then assessment evidence, then the AI-integrated activity that produces the evidence. The output shows the three layers building in sequence, making the design logic explicit.
- Prompt seed: `claude "Design a backward-designed lesson on [topic] for [grade level] that integrates [AI tool]. Start with: (1) the desired learning outcome in Bloom's taxonomy terms (specify the cognitive level), (2) the assessment evidence that would demonstrate the outcome, (3) the AI-integrated activity that produces that evidence. Make the design logic explicit at each step." < lesson_params.txt`
- Read / check: Verify the Bloom's level is genuinely reflected in the activity (if the outcome is "evaluate," the activity should require evaluation, not just recall or comprehension); check that the assessment evidence is specific enough to distinguish students who achieved the outcome from those who didn't.
- Human supplies (Claude can't): A topic, grade level, and available AI tool(s). Fully synthetic — no human-supplied materials required.
- Output medium: Remotion — three stacked cards animating in sequence: Outcome card, then Assessment Evidence card, then Activity card, each with arrows showing how the lower card serves the one above it.
- The change: Run the same topic through two Bloom's levels (e.g., "remember" vs. "evaluate") and show how the entire lesson design changes downstream — different assessment, different activity, different AI role.
- Teardown angle: Backward design forces you to commit to what learning looks like before you commit to how the AI will help — which is the only order that keeps the AI in service of the learning rather than in place of it.
- Exclusions: Full curriculum mapping, LMS integration, cross-unit alignment checks.
- Score: 8/10

## Candidate 05 — Build a Feedback Type Classifier with Claude
- Source: claude-for-education-a-practitioners-guide/chapters/05-feedback-that-produces-learning.md
- Lane: BUILD (Claude Code)
- Hook: Feedback from AI is abundant and fast — but most of it is the wrong type for learning, and educators can't easily tell the difference without a framework.
- The artifact: A Python script that reads a set of AI-generated feedback samples and classifies each along three dimensions from the Hattie-Timperley model: feed-up (where are we going?), feed-back (how are we going?), and feed-forward (where to next?). Each sample gets a type classification, a component score, and a rewrite showing what the missing component would say. The output is an animated table showing the classification and rewrite for each sample.
- Prompt seed: `claude "Classify this feedback along three Hattie-Timperley dimensions: (1) feed-up — does it clarify the goal? (2) feed-back — does it assess progress toward the goal? (3) feed-forward — does it specify next actions? Score each dimension 0-3. Then rewrite the feedback to include any missing component." < feedback_samples.md`
- Read / check: Verify the feed-forward component is genuinely actionable (not "try harder" or "revise for clarity" but "add a topic sentence to paragraph 3 that states your claim explicitly"); check that the rewrite doesn't just add a generic next step but ties it to the specific student work described.
- Human supplies (Claude can't): 5–8 feedback samples (AI-generated, teacher-written, or both). The book's example feedback samples (including the deliberately feed-forward-missing ones) work as a stand-in.
- Output medium: d3 (animated) — a table where each feedback sample appears, then the three dimension scores fill in as colored cells, then the rewrite appears beneath the row.
- The change: Generate the same feedback in three modes — "diagnose only," "diagnose + coach question," "diagnose + directive correction" — and show which students would benefit most from each based on the proficiency context.
- Teardown angle: Feedback type mismatch is the most common reason AI feedback doesn't improve learning — not because it's wrong, but because it's answering the wrong question for where the student is.
- Exclusions: Integration with student submission systems, automated feedback generation at scale, student-facing feedback dashboards.
- Score: 8/10

## Candidate 06 — Build a Student AI Policy Classifier with Claude
- Source: claude-for-education-a-practitioners-guide/chapters/10-policy-and-student-ai-use.md
- Lane: BUILD (Claude Code)
- Hook: Most AI use policies are written at the institution level but enforced at the assignment level — and the mismatch between them is where unintended violations happen.
- The artifact: A Python CLI that takes a set of assignment descriptions and maps each to one of four policy modes (Prohibited, Permitted with Disclosure, Required for Process, Reflective Use), then generates a per-assignment guidance statement that could go directly into the syllabus. The output is an animated policy matrix with each assignment's classification appearing alongside its rationale and syllabus language.
- Prompt seed: `claude "For each assignment, classify the appropriate AI use policy mode: (1) Prohibited — AI use undermines the assignment's purpose, (2) Permitted with Disclosure — AI use is allowed if students document it, (3) Required for Process — students must use AI as part of the learning task, (4) Reflective Use — students use AI and then reflect on what it did and didn't do well. For each, provide a one-paragraph syllabus-ready policy statement." < assignments.txt`
- Read / check: Verify the classifications align with the assignment's stated purpose (a coding exercise designed to build debugging skill should be Prohibited or Required-with-handgrip, not Permitted-with-Disclosure); check that the syllabus language is specific enough to answer the most common student edge-case question ("can I use it to check my grammar?").
- Human supplies (Claude can't): A list of 8–12 assignments from their course. The book's example assignments (spanning all four policy modes) are acceptable.
- Output medium: Remotion — a 4-quadrant policy matrix where each assignment animates into its quadrant with a short rationale; then a "syllabus export" animates the policy statements appearing in a formatted document.
- The change: Take one assignment from "Prohibited" and show what it would look like redesigned as "Required for Process" — what changes in the assignment design, what changes in the policy statement, and what the student does differently.
- Teardown angle: Policy mode is a design choice, not just a rule — the same topic can legitimately sit in any of the four quadrants depending on what the learning objective is and how the AI use is structured.
- Exclusions: Institution-wide policy implementation, automated policy enforcement in LMS, student-facing AI declaration forms.
- Score: 8/10

## Candidate 07 — Research What Makes AI Feedback Effective: Evidence Review
- Source: claude-for-education-a-practitioners-guide/chapters/05-feedback-that-produces-learning.md
- Lane: RESEARCH (Claude assistant)
- Hook: Educators are being told AI feedback is as good as human feedback — but the evidence is mixed, domain-dependent, and rarely presented in a form teachers can act on.
- The artifact: A sourced 6-study evidence summary comparing AI-generated feedback effectiveness vs. human feedback across three domains (writing, mathematics, programming), with a structured table showing study design, sample size, key finding, and applicability rating for each. The research terminal shows the prompts used to gather, cross-check, and synthesize the evidence.
- Prompt seed: `claude "Find and summarize the best available evidence on AI-generated feedback effectiveness vs. human feedback in K-12 and higher education. For each study you cite: state the domain, sample size, key finding, and one limitation. Cross-check any study that appears to have corporate sponsorship." `
- Read / check: Verify all cited studies are real (check titles and authors against Google Scholar); confirm the "limitation" field is genuinely stated, not invented; check that corporate-sponsored studies are flagged in the output.
- Human supplies (Claude can't): Access to a research database or Google Scholar to verify citations. Claude can draft the synthesis; the human must verify the studies cited are real and the findings are accurately represented.
- Output medium: screen-recording mp4 — the research terminal shows the multi-turn prompting sequence (gather, cross-check, synthesize, format), then the final comparison table appears as a screen-captured artifact.
- The change: Ask Claude to identify what the evidence would need to show to change the conclusion — what kind of study would move "AI feedback is adequate in narrow contexts" to "AI feedback is robustly equivalent to human feedback across domains"?
- Teardown angle: "Studies show AI feedback works" and "studies show AI feedback works for short-answer math at the 5th grade level" are the same sentence at different zoom levels — and the zoom level is everything for instructional decisions.
- Exclusions: Meta-analysis of all AI feedback research, study replication, primary research design.
- Score: 7/10

## Candidate 08 — Build a Lesson AI-Integration Audit with Claude
- Source: claude-for-education-a-practitioners-guide/chapters/01-the-practitioner-frame.md + chapters/02-learning-outcomes-before-prompts.md
- Lane: BUILD (Claude Code)
- Hook: Most "AI-integrated" lessons are really "AI-adjacent" — the AI is doing something, but not the thing that would actually change what students learn.
- The artifact: A Python CLI that reads a lesson plan (with explicit learning objectives) and classifies the AI's role in each activity as: central (AI is doing the cognitive work the objective targets), peripheral (AI is supporting but the student does the objective-relevant thinking), or decorative (AI is present but not meaningfully affecting the learning). The output is an animated lesson map showing each activity and its AI role classification.
- Prompt seed: `claude "Read this lesson plan and its learning objectives. For each activity, classify the AI's role as: central (AI performs the cognitive work the objective targets), peripheral (AI supports but student does the key thinking), or decorative (AI present but not affecting learning toward the objective). Provide one-sentence reasoning for each classification." < lesson_plan.md`
- Read / check: Verify the "decorative" classification is genuinely distinct from "peripheral" — decorative means the lesson outcome would be identical if the AI were removed; check that the reasoning cites the specific learning objective each activity is supposed to serve.
- Human supplies (Claude can't): A lesson plan with explicit learning objectives. The book's example lesson plans (including the deliberately AI-heavy ones) work as a stand-in.
- Output medium: d3 (animated) — a horizontal timeline of the lesson where each activity block appears and then gets color-coded (blue = central, green = peripheral, gray = decorative), with the learning objective alignment appearing as a note below each block.
- The change: Redesign the activity with the worst AI-role classification (most "central" when it shouldn't be) to shift the cognitive work back to the student — show the classification change after redesign.
- Teardown angle: "AI-integrated" is not a quality metric — a lesson where AI is central to everything is just a lesson where students watch an AI work. The audit reveals whether integration is purposeful or cosmetic.
- Exclusions: Full curriculum integration audit, LMS-based lesson tracking, student-facing activity classification.
- Score: 7/10

## Candidate 09 — Build an Instructional Brief Generator with Claude
- Source: claude-for-education-a-practitioners-guide/chapters/03-the-instructional-brief.md
- Lane: BUILD (Claude Code)
- Hook: The quality gap between instructors who get useful AI outputs and those who don't is almost entirely explained by whether they specified what students know, what they don't know, and what "done" looks like before they started.
- The artifact: A Python CLI that guides an instructor through filling an 8-field instructional brief (Learner Profile, Prior Knowledge, Misconception, Outcome, Constraints, Modality, Assessment Evidence, Review Criteria) via interactive prompts, then uses Claude to generate the instructional prompt that matches the brief. The comparison shows how the generated prompt changes between a minimal brief (only 3 fields filled) and a complete brief (all 8 fields).
- Prompt seed: `claude "Generate an instructional prompt for Claude to tutor a student, based on this 8-field brief. The prompt must address the stated misconception explicitly, stay within the constraints, and produce an output that could serve as the stated assessment evidence. Do not generate a generic tutoring prompt — every element of the brief must appear in the generated prompt." < brief.md`
- Read / check: Verify the generated prompt explicitly references the misconception (not just the topic); check that a prompt generated from a 3-field brief is noticeably less targeted than one from an 8-field brief — this is the video's key demonstration.
- Human supplies (Claude can't): A real teaching scenario (topic + grade level + one common student misconception). Fully synthetic examples from the book work well.
- Output medium: screen-recording mp4 — the terminal shows the 8-field form filling in interactively, then the generated prompt appearing, then a diff showing what changes between the 3-field and 8-field versions.
- The change: Generate the same prompt twice, once treating the misconception field as optional (leaving it blank) and once filling it in, and show exactly which lines of the generated instructional prompt change.
- Teardown angle: The instructional brief forces specificity upstream — instead of discovering the AI doesn't know your students' prior knowledge at the end of a lesson, you state it at the beginning and get a tutoring prompt that actually addresses where they are.
- Exclusions: Full LMS integration, student-specific brief customization, automated lesson sequencing.
- Score: 7/10
