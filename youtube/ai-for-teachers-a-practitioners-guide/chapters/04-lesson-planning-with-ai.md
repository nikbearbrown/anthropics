# Chapter 4 — Lesson Planning and Curriculum Design with AI


## TL;DR

- The plan that looks right and the plan that lands are not the same document.
- The chapter moves through What the evidence actually shows, Why a lesson plan is not one task, Backward design and why most AI prompts get it wrong, The prompt is the primary lever, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The plan that looks right and the plan that lands are not the same document.*

---

Here is a thing that happened to a researcher named Lee Shulman in the 1980s. He was trying to figure out what teachers actually know — not what they know about their subjects, and not what they know about general pedagogy, but the specific thing that distinguishes an expert teacher from someone who merely knows the content. He called it pedagogical content knowledge, or PCK, and his 1986 paper in *Educational Researcher* is the closest thing educational research has to a founding document on the question.[^shulman86]

The concept is easier to see than to define. A chemistry teacher who has taught the weight-versus-mass unit for ten years knows that students will say, confidently, that a brick has more mass on Earth than on the Moon. She knows they will say it in week two and again in week four and get it wrong on the unit test even after three weeks of correction. She knows this because she has watched it happen. She has tried the textbook definition. She has tried the diagram. She has tried the analogy. What finally worked, for this class in this school, was a bathroom scale in an elevator accelerating downward — the weight drops, the mass is obviously unchanged because the student has not gotten smaller. A different teacher with a different class might need a different move. That knowledge — which move works on which students for which misconception — is PCK. It is not in the textbook. The textbook has the correct definition of mass. PCK is the knowledge of why the correct definition is not enough.

I am starting the chapter on AI and lesson planning here because the distinction Shulman named is the entire chapter. AI can produce a structurally correct lesson plan in seconds. It cannot supply PCK. Understanding what that means, precisely, is the difference between a lesson-planning workflow that earns the time savings the evidence says are available, and one that produces a document that looks right and then fails in the room.

---

## What the evidence actually shows

The best evidence we have on AI in lesson planning is the NFER / Education Endowment Foundation randomized controlled trial, published in 2024.[^nfer] Sixty-eight secondary schools in England. Two hundred and fifty-nine Key Stage 3 science teachers. Ten weeks. Treatment teachers were given access to ChatGPT plus a structured usage guide. Control teachers planned normally. At the end, both groups kept time logs. A panel of five expert science teachers evaluated thirty lesson resources — fifteen from each group — without knowing which was which, scoring on clarity, engagement, age-appropriateness, and scientific accuracy.

The results: treatment teachers spent 56.2 minutes per week on lesson and resource preparation; control teachers spent 81.5 minutes. The difference is about 25 minutes per week — roughly 31 percent of the baseline. The blind panel found no statistically significant difference in resource quality on any of the four dimensions.

That is the finding. Time went down. Blind-rated quality held. This is a real randomized trial with a real control group, and I want to be honest about what it is and is not. It measured teacher time and expert-rated resource quality. It did not measure student learning. Whether students taught from AI-assisted lesson plans learn more, less, or the same as students taught from teacher-prepared plans is a question the trial was not designed to answer. That distinction — between a lesson plan looking good to expert reviewers and a lesson plan producing learning in actual students — is not a minor caveat. It is where the whole question of PCK lives.

The 31 percent time saving is real. What the saved time actually buys students is not yet established at the level of evidence the trial provides. Keep that in tension as you read the rest of this chapter.

| Metric | Treatment (ChatGPT + guide) | Control | Difference |
|---|---|---|---|
| Weekly lesson prep time | 56.2 min | 81.5 min | −25.3 min (−31%) |
| Resource quality (clarity) | rated by blind panel | rated by blind panel | no statistically significant difference |
| Resource quality (engagement) | rated by blind panel | rated by blind panel | no statistically significant difference |
| Resource quality (age-appropriateness) | rated by blind panel | rated by blind panel | no statistically significant difference |
| Resource quality (scientific accuracy) | rated by blind panel | rated by blind panel | no statistically significant difference |
| Student learning outcomes | not measured | not measured | open question |

*Table 4.1 — NFER/EEF Teacher Choices trial (2024). The time finding is real; the quality finding is held; the learning question is unanswered. The gap between expert-rated quality and student-rated learning is where PCK lives.*

---

## Why a lesson plan is not one task

Here is what I mean when I say AI does lesson planning well. It can produce, in seconds, a structurally correct plan: learning objectives in standard verb-list form, a timed activity sequence, a formative check, differentiation frameworks in template form, a homework prompt. It does this reliably. The NFER blind reviewers looked at the output and could not distinguish it from teacher-produced work on the dimensions they measured.

Here is what I mean when I say AI cannot do lesson planning. It has never taught your class. It does not know which students confuse photosynthesis and respiration in a particular persistent way that requires a particular move to dislodge. It does not know which analogy will backfire because of something that happened in a prior unit. It does not know that the sequence you are about to use caused two days of confusion last year, and that swapping days two and three would have prevented it. It cannot tell you which exit ticket question will surface the exact misconception the unit needs to address, as opposed to the misconception that looks similar but is actually downstream of the real problem.

These are not minor gaps. They are the gaps where teaching lives.

A lesson plan is a bundle of tasks that the profession has chosen to represent as a single document. Some of those tasks are structural: write objectives, sequence activities, align to a standard, produce a worksheet. Those are the tasks AI does well. Some of those tasks are PCK: anticipate the misconception this class will carry, choose the analogy that lands for these students, sequence the content in the order that does not collapse on itself for this population. Those are the tasks AI cannot do because they require knowledge of a particular room acquired over time.

The plan that the AI produces in fifteen minutes is complete at the structural layer. It is a draft at the PCK layer. These are different claims, and treating the structural completeness as overall completeness is the trap.

![Two-column infographic. Left column, headed "Structural layer — AI does well," lists six items: objectives in verb-list form, timed activity sequence, differentiation templates, exit ticket prompts, standards citations, worksheet first drafts. Right column, headed "PCK layer — teacher supplies," lists four items: which misconception this class will carry, which analogy backfires here, correct sub-topic sequence for this population, the exit ticket question that surfaces the right confusion.](../images/04-lesson-planning-with-ai-fig-01.png)
![Two layers of a lesson plan. The structural layer is delegable; the PCK layer is not. Treating the first ](images/04-lesson-planning-with-ai-fig-01.png)
*Figure 4.1 — Two layers of a lesson plan. The structural layer is delegable; the PCK layer is not. Treating the first as the whole is the trap.*

---

## Backward design and why most AI prompts get it wrong

Grant Wiggins and Jay McTighe's *Understanding by Design* makes a discipline of where to start.[^ubd] Their sequence: first identify what students should understand; then determine what evidence would demonstrate that understanding; then, and only then, choose the activities and resources that produce the evidence. They call these Stage 1, Stage 2, and Stage 3.

A default AI prompt — "Write a 50-minute lesson on cellular respiration for tenth-grade biology" — collapses Stages 1 and 2 into an implicit guess and runs immediately to Stage 3. The model produces activities and resources. It has no idea what the teacher's specific learning target is, what assessment will follow the lesson, or what understanding the activities are supposed to produce. The output looks complete. It is Stage 3 work done before Stages 1 and 2 were set.

This matters in practice because a Stage 3 lesson plan is a plan for a class that is not yours. It is a plan for a generic tenth-grade biology student, aimed at an implicit target the model chose on your behalf, with activities designed to produce evidence for a standard the model cited but did not verify.

The fix is mechanical. Before opening the AI, write two things down. One sentence for Stage 1: what should students understand by the end of this lesson or unit? One sentence for Stage 2: what evidence would show me they understand it? These two sentences are the brief. The AI prompt becomes a Stage 3 request: *given these targets and this evidence, propose activities, resources, and a formative check*.

This switch changes the nature of the output entirely. The model is no longer guessing at your purpose. It is proposing structure for a purpose you have already specified. And the revision pass you run on the output has a clear test: does each element of this plan serve the Stage 1 target and produce the Stage 2 evidence? Yes — keep. No — revise.

The ninety seconds you spend writing the two sentences before opening the prompt is the most important ninety seconds in the workflow. It is also the step that most teachers skip for the first six months of AI lesson planning, then discover, and never skip again.

![Backward-design flow diagram. Three boxes left to right labeled Stage 1, Stage 2, Stage 3, with arrows between them. Captions beneath each: "What should students understand?" "What evidence shows they understand it?" "What activities produce that evidence?" A skip arrow from a default AI prompt jumps straight to Stage 3, marked with a red X. A second path shows a two-sentence sticky note feeding Stage 1, then Stage 2, then the AI prompt at Stage 3, marked with a green check.](../images/04-lesson-planning-with-ai-fig-02.png)
![Backward design and where AI prompts collapse it. A default prompt skips Stages 1 and 2 and runs straight](images/04-lesson-planning-with-ai-fig-02.png)
*Figure 4.2 — Backward design and where AI prompts collapse it. A default prompt skips Stages 1 and 2 and runs straight to Stage 3; the two-sentence sticky note is the ninety-second fix.*

---

## The prompt is the primary lever

The NFER trial treated all treatment teachers as receiving essentially the same intervention — ChatGPT plus a structured guide. A 2025 preprint by Xincheng Liu evaluated AI-generated physics lesson plans across multiple models and prompt frameworks and found that prompt framework dominated curricular alignment accuracy — not the model being used.[^liu25] That is consistent with my experience and with the argument of the prior chapter: the quality of the AI output is, more than anything else, a function of the specificity and completeness of the prompt you send it.

A vague prompt produces a generic plan that requires heavy revision. A specified prompt — with grade level, subject, standards target, prior-knowledge context, student population detail, differentiation needs, and explicit constraints on framing to avoid — produces a draft that is much closer to usable, at the structural layer, before revision.

The practical implication is uncomfortable because it means the dividend requires work upfront. The fifteen-minute generation time in the NFER trial is preceded by however long it takes to write a prompt that includes all of that context. A teacher who sends a one-sentence prompt and gets back a generic plan and then spends forty minutes revising it has not captured the dividend. A teacher who spends ten minutes writing a rich prompt, gets back a contextually appropriate draft, and spends twenty minutes on PCK revision has. The time savings live in the second workflow, not the first.

Here is what a rich single-lesson prompt includes: class profile (grade, subject, number of students, period length), the prior unit and what students can now do, the specific prior-knowledge gaps that this lesson needs to build on, the student population in enough detail to make differentiation plausible (ELL count and proficiency level, IEP and 504 specifics, reading-level range), the targeted standard, what this lesson must set up for the next unit, explicit constraints on framing to avoid, and a format specification for the output. That is roughly four hundred words of prompt. That is the difference between a draft you argue with productively for twenty minutes and a draft you argue with unproductively for an hour.

---

## The phase gate, stated

Here is the gate that sits between the AI's draft and a plan that touches students:

> AI generates the structure. You confirm — for this class, this week — that every learning objective is achievable, every activity is contextually appropriate, every misconception is anticipated, and every standard alignment is real.

Two sentences. The gate is not a procedure; it is a question you ask about each element of the draft. *What does this plan assume about the room, and is that assumption true?* When the assumption is true, accept. When the assumption is false — when the analogy will backfire, when the exit ticket misses the actual misconception, when the sequence is wrong for this class — revise. The model cannot ask itself this question because it does not know the room. You ask it on every section of every draft, every time.

The standards verification is a specific case of this. A current large language model can cite a standard with the confidence of a correct citation. Whether the assessment in your Stage 2 actually produces the evidence the standard requires is a separate question, and the model has no reliable way to verify it. The rule is: treat every AI standards citation as a cross-reference to verify, not an authority to accept. Open the actual standard. Read the actual language. Confirm that the assessment produces work that demonstrates the standard rather than merely mentions the topic. This check takes ninety seconds. The lesson that skips it has an alignment claim on its cover sheet and may have no alignment in its bones.

---

## A worked example: cellular respiration, prompt to plan to revision

Take a tenth-grade biology teacher planning a five-day unit on cellular respiration. Twenty-eight students. Three newcomer ELLs at intermediate Spanish-L1 proficiency. Two IEPs. The class has just finished thermodynamics and can balance equations, but most cannot label the organelles of a cell. Photosynthesis follows in three weeks; the ATP foundation has to be clean or photosynthesis collapses.

Before the prompt, on a sticky note, she writes the two sentences.

Stage 1: Students will explain how cellular respiration converts the chemical energy in glucose into the chemical energy in ATP, including where in the cell each major stage occurs and what each stage produces.

Stage 2: A short written response in which a student traces one glucose molecule from cytoplasm through the mitochondrion, naming inputs and outputs at each stage, plus a labeled diagram. The day-five exit ticket asks the same thing in miniature.

The prompt runs to about four hundred words — class profile, prior unit, knowledge gaps, student population, standard, next unit, constraints on framing, format specification. She hits send. Fifteen minutes later, she has a five-day unit skeleton and a detailed Day 1 lesson plan. Reasonable structure. Three activity options per day. A first-pass exit ticket. An NGSS HS-LS1-7 citation flagged as draft pending verification, because the prompt asked for that flag.

Then she works for thirty minutes.

She crosses out the opening video on glucose oxidation chemistry and replaces it with a five-minute opening in which students try to explain, using the thermodynamics vocabulary they just learned, what the word "energy" means in the equation `glucose + O2 → CO2 + H2O + energy`. She knows from last year that this class will arrive with "ATP is energy" as an undisturbed prior belief, and she wants that belief surfaced on day one before the rest of the unit calcifies on top of it. The AI did not know this. The AI could not have known this. This is a PCK move.

She swaps the order of days two and three. The AI had the cellular respiration overview before the photosynthesis-versus-respiration contrast. Last year this order produced two days of confusion at the glycolysis-versus-Krebs-cycle boundary. Putting the contrast first gives students a framework — the two processes as inverse reactions — into which glycolysis and Krebs then slot. This decision is two years of teaching this unit in this school. The AI had no access to it.

She replaces the AI's exit ticket with last year's version, which asked students to draw the path of one glucose molecule from cytoplasm to mitochondrion and label every input and output. That version surfaced the specific misconception the unit is trying to dislodge — that students think glucose enters the mitochondrion whole, rather than as pyruvate after glycolysis. The AI's version was structurally correct and missed the target.

She opens NGSS HS-LS1-7 in another tab, reads the actual standard language, and confirms that the Stage 2 assessment produces the evidence the standard asks for. It does.

Fifteen minutes of generation. Thirty minutes of PCK revision. Forty-five minutes total. The revision is not waste — the revision is the work. What AI replaced was the blank-page production time. What AI preserved was the judgment time. The dividend lives in that substitution.

| Element revised | What AI produced | What the teacher changed it to | Why (PCK basis) |
|---|---|---|---|
| Day 1 hook | Glucose oxidation chemistry video | Five-minute opening using thermodynamics vocabulary on `glucose + O₂ → CO₂ + H₂O + energy` | Surfaces the "ATP is energy" prior belief on day one, before the rest of the unit calcifies on top of it |
| Day sequence | Cellular respiration overview before photosynthesis/respiration contrast | Contrast first, then overview | Last year, the AI's order produced two days of confusion at the glycolysis/Krebs boundary; the contrast gives a framework into which the stages slot |
| Exit ticket | Label diagram plus two sentences on stages | Trace one glucose molecule from cytoplasm through the mitochondrion, naming inputs and outputs at each stage | Surfaces the specific misconception that students think glucose enters the mitochondrion whole rather than as pyruvate after glycolysis |

*Table 4.2 — Three PCK revision moves on a single Day 1 plan. Fifteen minutes of generation, thirty minutes of revision. The revision is the work; the AI's job was to clear the blank page.*

---

## The unit-versus-lesson asymmetry

Counter-intuitively, AI is more useful for unit-scale planning than for next-day lesson planning. Unit-scale planning is largely structural: sequencing, cognitive-load staging, mid-unit formative checkpoints, identification of the sub-topics that must come before others can land. The model is reasonable at this, and the context it lacks — specific knowledge of the room — is less critical at this scale.

Next-day lesson planning is heavily context-bound. What students did yesterday. What confused them on Thursday's exit ticket. Who is absent on Friday. What energy the room had at the end of last period. The model knows none of this.

This means the dividend is largest when you give AI the work where it has the most context and smallest when you give it the work where context is everything. Most teachers do the opposite: they reach for AI on Monday night for Tuesday's lesson because Tuesday's lesson is what is burning. That is exactly the scope where the AI knows the least about the room and where the PCK revision pass will be heaviest.

The practical rule: use AI at the unit level, planned a week or two ahead, with class-specific context that has accumulated over the prior weeks. Reserve Monday night for the context-dependent revisions to whatever draft you generated on Sunday afternoon.

And do not generate a year of plans at once. A year of plans generated in August cannot reflect what you will learn about your class in September. The Tuesday-of-week-eight lesson depends on what surfaced in Tuesday-of-week-seven's exit ticket. PCK accumulates through the year. Locking in annual plans in advance discards that accumulation.

![Line chart with planning horizon on the x-axis (tomorrow's lesson, next week's lesson, unit at two to three weeks, semester, full year) and AI dividend on the y-axis (time saved minus revision cost). The curve rises steeply from tomorrow to unit level, peaks at the unit, then flattens and dips toward the full-year mark.](../images/04-lesson-planning-with-ai-fig-03.png)
![AI dividend by planning horizon. Unit-level is the sweet spot; Monday-night single-lesson generation and ](images/04-lesson-planning-with-ai-fig-03.png)
*Figure 4.3 — AI dividend by planning horizon. Unit-level is the sweet spot; Monday-night single-lesson generation and August year-ahead generation both capture less of the dividend.*

---

## What the dividend actually costs

The NFER trial's 31 percent time saving is real and I believe it is reproducible for teachers who write rich prompts and run proper PCK revision passes. But it is a population average over ten weeks of a specific trial condition. It is not a guarantee for week one.

The learning curve exists. Teachers new to AI lesson planning typically spend more time in the first weeks, not less — they are learning what a rich prompt requires, what the model can and cannot produce, where the PCK gaps predictably live. The dividend accrues after that learning, not before. A teacher who tries AI on a Monday, finds it slower than her normal workflow, and concludes the dividend is fictional is reading week one as if it were steady state.

There is also the equity question, which I want to name even though I cannot resolve it. RAND's 2025 survey of U.S. teachers found that higher-poverty schools use AI less than lower-poverty schools, and that principals in those schools provide AI guidance less often.[^rand] The schools whose teachers stand to gain the most from a competent structural-draft tool are the schools where the tool is least available and least supported. If the PCK revision step is the part that turns a structural draft into a usable plan, and front-end access to the draft is uneven, the technology could quietly widen the gaps it might have closed. I do not yet know what this produces at the student-outcome level. It is the question I would most want answered by a researcher with access to the data.

---

## Three things that would make me revise this chapter

The argument rests on three claims: AI saves time at the structural layer; PCK revision is necessary and non-delegable; and the combination produces better outcomes than either AI or the teacher working alone. The first claim has RCT support. The second has decades of educational research behind it. The third is, at the level of student learning outcomes, an open empirical question.

A rigorous randomized trial with student learning as the primary endpoint — showing that students taught from AI-generated plans without substantive PCK revision learn at least as much as students taught from teacher-revised plans, across diverse populations and subjects — would require a significant revision to the chapter's central argument about the necessity of the revision step. That trial does not yet exist.

A long-running observational study showing that teachers using AI lesson planning at steady state across a full academic year produce student outcomes statistically indistinguishable from a matched non-AI cohort would partially close the gap between the resource-quality finding and the student-learning question. Also does not yet exist.

The NFER follow-up Aila trial, measuring lesson quality and exploring student outcomes for AI-assisted lesson planning with roughly 450 Key Stage 2 teachers, is expected to report in 2026.[^aila] That result will be the most important piece of new evidence on this question in the near term.

---

## Exercises: using AI to understand AI lesson planning

These exercises are done with an AI tool. That is the point — using the thing you are learning about to understand it more precisely.

**Exercise 1: The vague-versus-specified prompt comparison.**

Take one upcoming lesson. Generate it twice. Prompt A is one sentence: "Write a [N]-minute [grade] [subject] lesson on [concept]." Prompt B uses the full template structure described in this chapter, filled in for your actual class. Compare the outputs side by side. Document which required less revision to make usable, what the class-specific context in Prompt B got you that Prompt A could not, and which plan you would actually teach from. The exercise is not to prove that specified prompts work — they do — but to feel, in your own room, how much of the dividend is a function of what you put in rather than what the model knows.

**Exercise 2: The PCK revision audit.**

Use AI to generate a unit skeleton for an upcoming unit you have to plan anyway. Then read the draft against the four PCK questions: what will students predictably get wrong? Which analogy will backfire? What sub-topic order does this class need? What is the smallest example that exposes the deepest confusion? List every revision you make and categorize each as: PCK (knowledge of this class), standards verification, structural correction, or stylistic preference. Calculate the ratio of PCK revisions to total revisions. That ratio is the share of the work the AI cannot do for you. The higher the ratio, the more the AI is buying you time on the work that matters.

**Exercise 3: The phase gate interview.**

Pick the hybrid lesson planning task you are most nervous about delegating — the one where an AI mistake would have real classroom consequences. Describe the task to an AI assistant. Ask it: *What information would you need from me to produce a first draft that I would need to substantially revise?* Then ask: *What would be the most likely ways this draft would be wrong?* Its answer to the second question is your phase gate for this task — the checklist you run before any draft from this task moves toward students. Write the gate down before you use the tool for the task the first time.

---

The lesson plan that looks right to a blind expert panel and the lesson plan that anticipates the misconception this class will carry into Tuesday are not the same document. AI produces the first reliably. You produce the second, and only you can. The dividend is what you get when you let AI handle the first so you have bandwidth left for the second.

Chapter 5 takes the same framework into assessment and feedback — where the time savings are larger, the failure modes are louder, and the question of who is doing the cognitive work cuts at both the teacher's grading desk and the student's writing desk.

---

##  AI Wayback Machine
The two-sentence sticky note in this chapter — *what should students understand, and what evidence shows they understand it* — did not begin with Grant Wiggins and Jay McTighe in 1998. It began with **Ralph W. Tyler** (1902–1994), the American educator whose 1949 *Basic Principles of Curriculum and Instruction* set out four questions that every curriculum must answer: what educational purposes should the school seek to attain; what educational experiences can be provided that are likely to attain these purposes; how can these educational experiences be effectively organized; and how can we determine whether these purposes are being attained. The *Tyler rationale* — objectives, experiences, organization, evaluation — is the structural skeleton beneath backward design, beneath outcomes-based education, and beneath the lesson-planning workflow in this chapter. When you write Stage 1 and Stage 2 before opening the AI, you are doing Tyler's first and fourth steps; when the AI proposes activities and you sequence them, you are doing his second and third. The chapter's prompt-then-revise workflow is Tyler's rationale with a new tool inserted at the activity-design step.

![Ralph W. Tyler, American educator (1902–1994). AI-generated portrait based on public-domain reference photographs.](../images/ralph-tyler.jpg)
*Ralph W. Tyler, circa 1950. AI-generated portrait based on public-domain reference photographs.*

**Run this:**

```
Who was Ralph Tyler, and how does his 1949 Tyler rationale (objectives, experiences, organization, evaluation) connect to the backward-design and prompt-then-revise workflow in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or method.
```

→ Search **"Ralph W. Tyler"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask the model to translate Tyler's four questions into a one-page lesson-planning intake form a teacher could fill out before opening an AI tool — what survives the translation, and what gets lost?
- Ask whether Tyler's rationale is fundamentally compatible with backward design, or whether Wiggins and McTighe quietly reversed one of his steps.

What changes? What gets better? What gets worse?

---

[^shulman86]: Shulman, L. S. (1986). Those Who Understand: Knowledge Growth in Teaching. *Educational Researcher*, 15(2), 4–14. <https://journals.sagepub.com/doi/10.3102/0013189X015002004>. The 1987 companion piece: Shulman, L. S. (1987). Knowledge and Teaching: Foundations of the New Reform. *Harvard Educational Review*, 57(1), 1–22.

[^nfer]: NFER & Education Endowment Foundation (2024). *ChatGPT in Lesson Preparation: A Teacher Choices Trial — Evaluation Report.* Cluster-randomised trial, 68 secondary schools, 259 KS3 science teachers, ten weeks. <https://d2tic4wvo1iusb.cloudfront.net/production/documents/projects/chatgpt_in_lesson_planning_-_evaluation_report.pdf?v=1736353004>. EEF news summary: <https://educationendowmentfoundation.org.uk/news/teachers-using-chatgpt-alongside-a-guide-to-support-them-to-use-it-effectively-can-cut-lesson-planning-time-by-over-30-per-cent>.

[^ubd]: Wiggins, G., & McTighe, J. (2005). *Understanding by Design* (2nd ed.). Alexandria, VA: ASCD. <https://www.ascd.org/books/understanding-by-design-expanded-2nd-edition?variant=103055>.

[^liu25]: Liu, X. (2025). *An Evaluation of the Pedagogical Soundness and Usability of AI-Generated Lesson Plans Across Different Models and Prompt Frameworks in High-School Physics.* arXiv:2510.19866. <https://arxiv.org/abs/2510.19866>. Preprint, not yet peer-reviewed.

[^rand]: RAND Corporation (2025). *Uneven Adoption of Artificial Intelligence Tools Among U.S. Teachers and Principals in the 2023–2024 School Year* (RR-A134-25). <https://www.rand.org/pubs/research_reports/RRA134-25.html>.

[^aila]: Education Endowment Foundation (2025). *Lesson planning using AI lesson assistant, Aila — Teacher Choices Trial.* ~450 Key Stage 2 teachers, 86 English primary schools; results expected 2026. <https://educationendowmentfoundation.org.uk/projects-and-evaluation/projects/aila-teacher-choices-trial>.

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 4.1 — Two layers of a lesson plan. The structural layer is delegable; the PCK layer is not. Treating the first 

Create a standalone D3 v7 HTML file for a side-by-side comparison diagram titled "Two layers of a lesson plan. The structural layer is delegable; the PCK layer is not. Treating the first ". Use teacher AI-workflow states: learning goal, AI draft, teacher review gate, classroom use, equity check, and student evidence. Encode the AI-assisted step with one red mark and all teacher-controlled checks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/04-lesson-planning-with-ai-fig-01.html`

---

### Figure 4.2 — Backward design and where AI prompts collapse it. A default prompt skips Stages 1 and 2 and runs straight

Create a standalone D3 v7 HTML file for a concept map titled "Backward design and where AI prompts collapse it. A default prompt skips Stages 1 and 2 and runs straight". Use teacher AI-workflow states: learning goal, AI draft, teacher review gate, classroom use, equity check, and student evidence. Encode the AI-assisted step with one red mark and all teacher-controlled checks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/04-lesson-planning-with-ai-fig-02.html`

---

### Figure 4.3 — AI dividend by planning horizon. Unit-level is the sweet spot; Monday-night single-lesson generation and 

Create a standalone D3 v7 HTML file for a bar or comparison chart titled "AI dividend by planning horizon. Unit-level is the sweet spot; Monday-night single-lesson generation and ". Use teacher AI-workflow states: learning goal, AI draft, teacher review gate, classroom use, equity check, and student evidence. Encode the AI-assisted step with one red mark and all teacher-controlled checks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/04-lesson-planning-with-ai-fig-03.html`
