# Chapter 12 — Building Your AI Workflow: Monday Morning to End of Year


## TL;DR

- Two teachers, same building, same tool, ten hours apart.
- The chapter moves through The selection problem, named honestly, What the library actually is, The schedule: the other half, Why most teachers plateau, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Two teachers, same building, same tool, ten hours apart. The gap is not skill. It is what was captured and what was scheduled.*

---

There is a concept in knowledge management that Thomas Davenport and Laurence Prusak named in 1998: the difference between *tacit* knowledge and *explicit* knowledge.[^davenport] Tacit knowledge is what you know how to do — it lives in your hands, your habits, your accumulated professional judgment. Explicit knowledge is the same thing written down in a form someone else can pick up and use. The conversion from tacit to explicit — from knowing to having documented — is where organizations stop reinventing the wheel.

Most teachers using AI are stuck at the tacit end. They have learned, through trial and error, which kind of prompt gets a useful lesson skeleton and which gets a generic one. They know that telling the model the class has three ELL students at WIDA Level 2 gets better differentiation scaffolds than asking generically. They know which tasks to trust the output of and which to review carefully. This knowledge is real, hard-won, and professionally valuable.

And then they close the tab, and the next Tuesday they write the lesson-planning prompt from scratch.

This is not a character flaw. It is the natural state of a tool you were never trained to use systematically, operating in a job that never gave you time to think about your tools. The Gallup-Walton survey of 2,232 U.S. public school teachers found that roughly 52 percent of those who use AI taught themselves, and only 31 percent received any district-provided training.[^gallup] RAND's 2024–25 survey of the American School District Panel put it more starkly: about 68 percent of U.S. teachers had received no formal AI training at all.[^rand]

The workflow this chapter describes is what you build when the training was not offered. It is not complicated. It is a document, a schedule, and a maintenance habit. The document captures the prompts that worked. The schedule creates the recurring context in which they get used. The maintenance habit keeps both from rotting. Put the three together and you have converted your accumulated tacit AI knowledge into something explicit — something that works on a hard Wednesday as well as it works on a motivated Sunday.

![Three-box flow diagram. First box "Tacit knowledge" lists prompt patterns, trust judgments, phase-gate habits living in the teacher's head. An arrow labeled "Capture event — the prompt worked, you save it to workflow.md" leads to a second box "Explicit knowledge" listing parameterized, labeled, maintained, reusable entries. A dashed red decay arrow loops back from the first box to a third box "Closed tab — reinvented next Tuesday," showing what happens when the capture step is skipped.](../images/12-building-your-ai-workflow-fig-01.png)
![Tacit-to-explicit conversion, and the decay path that runs if the capture event never fires. The workflow](images/12-building-your-ai-workflow-fig-01.png)
*Figure 12.1 — Tacit-to-explicit conversion, and the decay path that runs if the capture event never fires. The workflow document is the structural insistence that the capture happens.*

---

## The selection problem, named honestly

Before building anything, name the limit of the evidence behind this chapter.

The Gallup-Walton survey shows that teachers who use AI weekly save an average of 5.9 hours per week — six weeks across the school year.[^gallup] It also shows that systematic users report higher savings than ad hoc users. The temptation is to read this as: *build the system and get the higher savings.*

Two readings live side by side in that data and the survey cannot distinguish them.

The first reading: systematic users save more time because the system — the captured prompts, the recurring schedule — produces efficiencies that ad hoc use does not. Install the system and get the efficiency.

The second reading: systematic users save more time because the kind of teacher who builds a system is also the kind of teacher who was already organized, motivated, and strategic about her time. The AI is correlated with the savings, not causing them. Drop a less-organized teacher into the same tool and you do not get the same result.

The Gallup-Walton design is observational. It cannot separate these. No randomized trial has assigned teachers to systematic-workflow training versus tool-access-only and measured the difference. The Center on Reinventing Public Education has raised this concern most directly, noting that the headline savings figure conflates the tool's effect with the selection effect of the teachers most inclined to use it carefully.

The honest framing is: the workflow I am about to describe is a credible hypothesis you test in your own week. Track your hours before and after installation. If after six weeks your saved time has moved, you have your own data point. If it has not, the system did not work for you and you should reorganize or stop. The only data that finally answers the question for your week is the data from your week.

---

## What the library actually is

The prompt library is the heart of the system, and it is worth being precise about what it is and what it is not.

It is not a collection of screenshots. It is not a folder of chat exports. It is a structured document, maintained deliberately, in which each entry has four properties.

**It is organized.** Entries are grouped by recurring task — lesson planning, feedback, differentiation, communication, slides, charts. Future-you should be able to find the relevant entry in under fifteen seconds.

**It is named.** Each entry has a one-line task label. *Lesson skeleton. Rubric-aligned feedback. Lexile pass. Parent note from bullets.* The label is the index.

**It is parameterized.** The variables that change with each use — the standard, the class profile, the specific student population detail — are explicit slots in `[ALL CAPS]`, not buried in prose. A prompt that bakes "7th-grade life science" into the body is single-use. A prompt with `[GRADE LEVEL]`, `[STANDARD]`, and `[CLASS PROFILE]` slots is reusable. The difference is whether you are copying and editing or copying and filling.

**It is maintained.** Entries that stop working get revised or retired. I will return to the maintenance cadence, because it is the part most people skip and it is the part that eventually determines whether the library is an asset or a junk drawer.

The Template Pattern from Chapter 3 — role, context, task, format, constraints — is the skeleton for every entry. The library is what happens when you stop letting good prompts disappear.

| Property | What it looks like | What it prevents |
|---|---|---|
| Organized | Entries grouped by task type — lesson planning, feedback, differentiation, communication, slides, charts. Future-you finds the right one in under fifteen seconds. | Scattered entries you cannot locate under pressure; the library that exists but you stop opening. |
| Named | One-line task label at the top of each entry: *Lesson skeleton. Rubric-aligned feedback. Lexile pass. Parent note from bullets.* | Label-less entries you skip because you are not sure which one is the right one for this task. |
| Parameterized | Variables that change per use sit in `[ALL CAPS]` slots — `[GRADE LEVEL]`, `[STANDARD]`, `[CLASS PROFILE]`. Reusable: copy-and-fill, not copy-and-rewrite. | Baked-in specifics ("7th-grade life science") that make the prompt single-use; rewriting from scratch every Tuesday. |
| Maintained | A "last verified" date on each entry plus a *renewed / revised / retired* status, refreshed twice a year. | The junk drawer: a library that quietly stops working as models drift, and that you cannot tell apart from one that still does. |

*Table 12.1 — The four properties of a prompt library entry. Drop any one and the library degrades into a folder of chat exports that future-you stops opening.*

---

## The schedule: the other half

A library without a schedule sits unused. The library is the what; the schedule is the when. Both are required.

The relevant psychology here is Wendy Wood and David Neal's program of work on habit formation.[^wood] Their central finding is that habits are not primarily goal-driven — they are context-cued. Once a behavior has been performed often enough in the same context, the context itself triggers the behavior, with limited conscious involvement by current motivation. The teacher who relies on *"I should use AI more this week"* is using the goal system. The goal system is effortful, depletable, and loses to a hard Wednesday. The teacher who installs the workflow as a recurring context — Sunday at 4 p.m., kitchen table, laptop, Claude in the browser, lesson-planning template loaded — is using the habit system. The work happens whether motivation is high or low.

The practical instruction is simple: fixed commitments first (classes, duty, meetings), then named AI-assisted blocks with a specific task, specific tool, specific library entry, and the correct phase gate from Chapter 2. Not *"open Claude and see what needs doing,"* but *"Sunday 4–6 p.m., lesson planning, library entry #01, phase gate: I verify every objective is achievable by this class before accepting the plan."* The pairing is what turns a vague block of "AI work" into a recoverable hour.

Build 30 percent slack into each block. A block that hits 100 percent utilization on the first attempt is miscalibrated and will be skipped under pressure.

An honest caveat: the habit literature is well-validated for individual behaviors — exercise, snacking, commuting routes. Its application to professional-workflow installation is plausible by extension, not specifically validated for teacher AI workflows. Use it as an operational scaffold, not a guaranteed mechanism.

![Two parallel horizontal tracks merging at a single endpoint. Upper track labeled "Goal system: effortful, depletable, loses to a hard Wednesday" runs through five stations: motivation high, open tool, write prompt from scratch, use output, close tab — and a loop back to motivation. Lower track labeled "Habit system: context-cued, low activation cost, works whether motivation is high or low" runs through Sunday 4pm at the kitchen table, context triggers behavior, open workflow.md, run library entry 01, phase gate, done. Both tracks merge at a single labeled endpoint "Output reaches students."](../images/12-building-your-ai-workflow-fig-02.png)
![Goal system versus habit system, after Wood and Neal. Both routes can deliver an output. Only one of them](images/12-building-your-ai-workflow-fig-02.png)
*Figure 12.2 — Goal system versus habit system, after Wood and Neal. Both routes can deliver an output. Only one of them is robust to a hard Wednesday.*

---

## Why most teachers plateau

Two adoption frameworks name the structural pattern most teachers fall into and how to get out.

Everett Rogers's *Diffusion of Innovations* describes five sequential stages: knowledge, persuasion, decision, implementation, confirmation.[^rogers] Rogers's empirical observation is that most adopters reach *implementation* — the tool is being used — and stop short of *confirmation*, the stage where the innovation has been integrated into ongoing practice and the user has evidence it is working. The plateau at implementation looks exactly like ad hoc adoption. The tool is used. Each use is a fresh decision.

Gene Hall and Shirley Hord's Concerns-Based Adoption Model describes a more granular arc of concerns that teachers move through when adopting any innovation.[^cbam] The stages run from awareness through personal management concerns, consequence concerns, collaboration, and refocusing. The systematic-AI plateau is consistent with teachers stuck at the *management* stage — do I have time and materials to make this work? — and not yet moved into the *consequence* stage — how is this affecting students? — because the logistics of using the tool are still the primary cognitive load.

Both frameworks say the same thing in different vocabularies: the plateau is structural, not personal. The fix is structural support. A peer who has already built the workflow and can share it. A scheduled block that removes the management question from every individual use. A captured library that removes the prompt-writing question. These structures are what move teachers from management concerns to consequence concerns — from *can I make this work?* to *is this working for students?*

The workflow document is the structural support.

![Two-row plateau map. Top row shows Rogers's five sequential stages — Knowledge, Persuasion, Decision, Implementation, Confirmation — with a red plateau flag wedged between Implementation and Confirmation labeled "ad hoc adoption: tool is used but each use is a fresh decision." Bottom row shows the CBAM stages of concern condensed — Awareness, Personal, Management, Consequence, Collaboration, Refocusing — with a red plateau flag between Management and Consequence labeled "stuck on logistics: do I have time and materials?" An ochre arrow beneath both rows labeled "workflow.md moves you past both plateaus" sweeps from Implementation to Confirmation on top and from Management to Consequence below.](../images/12-building-your-ai-workflow-fig-03.png)
![Rogers and Hall-Hord, side by side. Two different vocabularies, the same plateau, the same structural fix](images/12-building-your-ai-workflow-fig-03.png)
*Figure 12.3 — Rogers and Hall-Hord, side by side. Two different vocabularies, the same plateau, the same structural fix.*

---

## The 68 percent problem

If you are reading this chapter without having received formal AI training from your district, you are not the exception.

RAND's 2024–25 American School District Panel survey found that roughly 68 percent of U.S. teachers received no formal AI training during the 2024–25 school year.[^rand] Only 48 percent of districts had provided any teacher AI training by fall 2024 — and that number was skewed heavily toward well-resourced districts. By fall 2024, 67 percent of low-poverty districts had provided AI training versus 39 percent of high-poverty districts. The training gap is also a poverty gap.

A common misreading: the teachers who haven't been trained are resistant. The data shows the opposite. The primary barrier is that training was not offered, not that teachers refused it. If your district has not yet trained you, this workflow is what you build while you wait.

---

## What platform to use for what

The tool landscape shifts on a quarterly cadence. Model rankings change. New entrants appear. Established tools add features that duplicate each other. Chasing the leaderboard is a losing strategy — every migration costs library rewrites, habit re-installation, and the inevitable "where did I save that prompt?" loss.

The stable answer is task-fit, not platform fashion. Assign tools to task categories, and stay with those assignments until the tool stops working for that category — not until something newer benchmarks higher.

The category map at time of writing: open-ended writing, reasoning, structured outputs, and lesson design are well-served by a general reasoning model with strong instruction-following. Document-grounded summaries and study guides benefit from a tool that cites back to user-supplied sources, reducing hallucination risk on content the teacher must trust. Search-augmented quick lookups and spreadsheet-integrated tasks benefit from a model with native search and office-suite integration. Bulk rubric scoring benefits from an LMS-integrated grader with FERPA-compatible logging, verified against your district's data-handling rules. Slides and charts are covered in Chapters 8 and 9 respectively, and the same five-question diagnostics from those chapters apply regardless of which tool produced the output.

The product names matter less than the principle. Review the platform-assignment section of your workflow document at every six-month maintenance check. Products change faster than principles.

---

## The six-month shelf life

A captured prompt is not a permanent artifact. The major commercial models ship significant updates on roughly a two-to-four-month cadence. A prompt that produced clean rubric-aligned feedback in August may produce something subtly different by March — the model's alignment behavior has shifted, its output structure has changed, its default verbosity has moved. The teacher who runs an unmaintained prompt against a changed model may not notice the regression until a grading dispute surfaces it.

The six-month maintenance cycle is a working heuristic, not a measured shelf life. Controlled studies of prompt-output stability across model versions have not been published at the granularity teachers need. Treat the six-month interval as an operating guess calibrated to roughly two model generations; if you observe drift sooner, shorten the cycle.

The maintenance move is a calendar entry — twice a year, January and July, 30 minutes each. Pull the top 8–10 library entries by use frequency. Rerun each on a current real task. Mark each entry as renewed (works as is, update the verification date), revised (works after edits, update both), or retired (no longer useful, archive it). Identify any prompt patterns you have been writing repeatedly from scratch in the past six months and promote at least one into the library. Update the platform-assignment section if the tool landscape has shifted.

This is not maintenance for its own sake. It is the difference between a library that degrades and a library that improves. The work takes 30 minutes twice a year. Skipping it costs you the asset you built.

![Line chart with months 0 to 24 on the x-axis and prompt output quality, relative to an initial baseline of 1.0, on the y-axis from 0 to 1. A solid red "no maintenance" line starts at 1.0 and decays smoothly to roughly 0.60 by month 12 and 0.30 by month 24. A dark "six-month maintenance" line starts at 1.0, decays slightly, snaps back to 1.0 at month 6, decays again, snaps back at months 12 and 18, holding near 1.0 across the full 24 months. Two ochre tick marks at months 6 and 12 mark the 30-minute maintenance calendar events.](../images/12-building-your-ai-workflow-fig-04.png)
![Prompt output quality with and without a six-month maintenance cycle. The maintenance events are 30 minut](images/12-building-your-ai-workflow-fig-04.png)
*Figure 12.4 — Prompt output quality with and without a six-month maintenance cycle. The maintenance events are 30 minutes apiece, twice a year. The thing they prevent is the slow degradation that nobody notices until a grading dispute surfaces it.*

---

## What the document looks like

Here is the shape of *workflow.md* — the four-section document that is the system. What follows is a template. Adapt every line to your actual week, your actual grade level, your actual tools.

**Section 1** is the prompt library. Ten entries minimum, one or two from each task category covered in Chapters 4 through 9. Each entry follows the role-context-task-format-constraints skeleton from Chapter 3. Each entry has variable slots in `[ALL CAPS]` and a one-line phase gate naming what you verify before the output reaches a student or parent. Each entry has a "last verified" date.

A representative entry:

```
### 03 · Rubric-aligned feedback (Ch 5)
ROLE: You are a [SUBJECT] teacher writing first-pass feedback
against a rubric.
CONTEXT: Rubric: [PASTE RUBRIC]. Assignment: [BRIEF DESCRIPTION].
Student work: [PASTE]. No student identifying information.
TASK: Score each rubric dimension; draft one comment per dimension;
do not assign a letter grade.
FORMAT: Table — dimension, score, comment.
CONSTRAINTS: Comments must be actionable; no praise without
specificity.
Phase gate: I calibrate on five samples before a bulk run;
I review every comment before release; I make the final grade
decision.
Last verified: 2026-01-14
```

**Section 2** is the weekly schedule. Fixed commitments first. Then four to six named AI-assisted blocks, each with task, tool, library entry number, and phase gate. A 30 percent slack budget on each block. The schedule is a default, not a contract — when the week breaks, the captured library still works in whatever 25-minute slot you can find.

**Section 3** is the platform-assignment note. Which tool for which task category. Why. When to revisit.

**Section 4** is the phase-gate map — one line per gate, printed and posted above the desk. Rubric calibration gate. Discrepancy resolution gate. Content accuracy gate. Anonymization gate. PCK gate. Sensitive communication gate. Document grounding gate.

The document is twelve pages when built out. The first pass takes about 90 minutes. It improves across the following two weeks in 15-minute touch-ups as you test what works against your actual tasks.

---

## The lesson and the limit

Build the document in August. Watch it survive November.

The schedule fails when your week fails. A parent meeting eats the Wednesday feedback block. A snow day moves Monday to Tuesday. The IEP that runs long takes Thursday's communication window. The system cannot prevent any of that. What it does is make the recovery cheap. When the week breaks, you have a captured library that still works in whatever fragment of time remains. The ad hoc user in the same broken week has neither the schedule nor the prompts. She writes from scratch or she does not write at all.

The system is not a guarantee of Teacher B's twelve hours. It is a hypothesis you test in your own week, with your own data. Track your hours honestly. The gap between two hours saved and twelve is real in the population. Whether that gap is causal — whether the system produces the savings or the savings attract the teachers who build systems — is a question the current evidence cannot settle. Your week is the experiment.

---

## Exercises: using AI to build the workflow document

These exercises are done with an AI tool, and they are the chapter's deliverables.

**Exercise 1: Build the starter library.**

Open your AI tool of choice. Describe your recurring task load in about 200 words — grade level, subject, the five or six tasks that repeat every week or unit. Ask the tool to generate a starter ten-entry prompt library in the role-context-task-format-constraints structure, with variable slots in `[ALL CAPS]` and a one-line phase-gate note for each entry. Then edit every entry against your actual class, your actual standards, and your actual phase-gate knowledge from Chapters 2 through 9. The AI provides the skeleton; you provide the professional judgment. Save the result as Section 1 of *workflow.md*. Write one sentence at the end of each entry noting what you changed from the AI's draft and why.

**Exercise 2: Generate and audit the weekly schedule.**

Describe your typical weekly schedule to the AI tool — fixed commitments, available time windows, task categories from the library. Ask it to propose a weekly AI workflow: four to six blocks, each with task, tool, library entry number, phase gate, and a 30 percent slack note. Review the proposed schedule against your actual week. Where does the AI's proposal assume resources or flexibility you do not have? Revise until the schedule is something you would actually keep. Save it as Section 2. Write one sentence about the revision that most surprised you.

**Exercise 3: Design the six-month maintenance check.**

Describe the structure of your prompt library to the AI tool. Ask it to generate a maintenance protocol: a step-by-step procedure for a 30-minute twice-yearly review, with criteria for renewed, revised, and retired entries, and a checklist for identifying new patterns to promote from scratch into the library. Review and revise the protocol until it is specific enough to run without re-reading the chapter. Put it in Section 5 of *workflow.md*. Then set two recurring calendar entries — January and July — with the 30-minute block and a link to the document. The protocol exists when the calendar entries exist. Write one sentence about the entry you are most likely to need to retire at the first maintenance check and why.

---

The workflow document is not the thing. The teaching is the thing. The document is what frees enough of your attention from logistics so that the teaching can be the bottleneck again — the place where your professional judgment, your knowledge of these students, your PCK, your relationships actually operate without competing with prompt-writing and schedule-improvising for the same cognitive bandwidth.

Chapter 13 turns the workflow around: the same *workflow.md* that saves you time is a documented record of what AI did and what you did. When a student, a parent, or an administrator asks what role AI played in something you produced, the workflow document is the answer. The library is the substrate of honest practice, not just efficient practice.

---

##  AI Wayback Machine
The argument that a teaching week can be made tractable by writing it down belongs to a longer engineering tradition than it sounds. **Henry Laurence Gantt** (1861–1919) was an American mechanical engineer who, working with Frederick Winslow Taylor at Midvale Steel and then on his own, invented the production planning chart that still carries his name. The Gantt chart — horizontal bars on a time axis showing scheduled tasks, their durations, their dependencies, and their actual progress against plan — turned a foreman's tacit week into a wall-sized explicit document anyone on the shop floor could read in five seconds. The United States Army built warships against Gantt's charts in the First World War; the Hoover Dam was built against them; every project-management tool you have ever used is downstream of them. The deep idea is not the bars. The deep idea is that the schedule has to live outside the planner's head, in a form a second person can read, or it does not really exist. *Workflow.md* is the same move at the scale of a single teacher's week: a captured library and a recurring schedule, written down so that future-you can read them on a hard Wednesday without rebuilding them from scratch.

![Henry Gantt, American mechanical engineer (1861–1919). AI-generated portrait based on public-domain reference photographs.](../images/henry-gantt.jpg)
*Henry Gantt, circa 1910. AI-generated portrait based on public-domain reference photographs.*

**Run this:**

```
Who was Henry Gantt, and how does his invention of the Gantt chart and his work on scientific scheduling connect to the prompt library plus weekly schedule plus maintenance cycle in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or method.
```

→ Search **"Henry Gantt"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask the model to translate Gantt's original 1910s production-planning chart into a one-week teacher schedule template — what survives the translation, and what gets lost?
- Ask whether Gantt's break from Taylor on the question of worker bonuses changes how you should think about teacher AI adoption as a system-design problem.

What changes? What gets better? What gets worse?

---

[^davenport]: Davenport, T. H., & Prusak, L. (1998). *Working Knowledge: How Organizations Manage What They Know.* Harvard Business School Press. <https://store.hbr.org/product/working-knowledge-how-organizations-manage-what-they-know/3014>.

[^gallup]: Gallup & Walton Family Foundation (2025). *Teaching for Tomorrow: Unlocking Six Weeks a Year With AI.* Survey fielded March 18 – April 11, 2025, n = 2,232 U.S. public K–12 teachers via RAND American Teacher Panel. <https://news.gallup.com/poll/691967/three-teachers-weekly-saving-six-weeks-year.aspx>. Full PDF: <https://static.waltonfamilyfoundation.org/df/fb/eba12807470a9402d7433cc47dba/teaching-for-tomorrow-unlocking-six-weeks-a-year-with-ai-report.pdf>.

[^rand]: Diliberti, M. K., Lake, R. J., & Weiner, S. R. (2025). *More Districts Are Training Teachers on Artificial Intelligence: Findings from the American School District Panel* (RR-A956-31). RAND Corporation. <https://www.rand.org/pubs/research_reports/RRA956-31.html>. The 68% figure refers to teachers reporting no formal AI training during 2024–25; verify exact wording against the primary report before publication.

[^wood]: Wood, W., & Neal, D. T. (2007). A new look at habits and the habit-goal interface. *Psychological Review*, 114(4), 843–863. <https://dornsife.usc.edu/wendy-wood/wp-content/uploads/sites/183/2023/10/wood.neal_.2007psychrev_a_new_look_at_habits_and_the_interface_between_habits_and_goals.pdf>. Wood, W., & Rünger, D. (2016). Psychology of habit. *Annual Review of Psychology*, 67, 289–314.

[^rogers]: Rogers, E. M. (2003). *Diffusion of Innovations* (5th ed.). Free Press.

[^cbam]: Hall, G. E., & Hord, S. M. (2020). *Implementing Change: Patterns, Principles, and Potholes* (5th ed.). Pearson Education. SEDL CBAM resources: <https://sedl.org/cbam/>.

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 12.1 — Tacit-to-explicit conversion, and the decay path that runs if the capture event never fires. The workflow

Create a standalone D3 v7 HTML file for a phase-gate workflow diagram titled "Tacit-to-explicit conversion, and the decay path that runs if the capture event never fires. The workflow". Use teacher AI-workflow states: learning goal, AI draft, teacher review gate, classroom use, equity check, and student evidence. Encode the AI-assisted step with one red mark and all teacher-controlled checks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/12-building-your-ai-workflow-fig-01.html`

---

### Figure 12.2 — Goal system versus habit system, after Wood and Neal. Both routes can deliver an output. Only one of them

Create a standalone D3 v7 HTML file for a side-by-side comparison diagram titled "Goal system versus habit system, after Wood and Neal. Both routes can deliver an output. Only one of them". Use teacher AI-workflow states: learning goal, AI draft, teacher review gate, classroom use, equity check, and student evidence. Encode the AI-assisted step with one red mark and all teacher-controlled checks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/12-building-your-ai-workflow-fig-02.html`

---

### Figure 12.3 — Rogers and Hall-Hord, side by side. Two different vocabularies, the same plateau, the same structural fix

Create a standalone D3 v7 HTML file for a side-by-side comparison diagram titled "Rogers and Hall-Hord, side by side. Two different vocabularies, the same plateau, the same structural fix". Use teacher AI-workflow states: learning goal, AI draft, teacher review gate, classroom use, equity check, and student evidence. Encode the AI-assisted step with one red mark and all teacher-controlled checks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/12-building-your-ai-workflow-fig-03.html`

---

### Figure 12.4 — Prompt output quality with and without a six-month maintenance cycle. The maintenance events are 30 minut

Create a standalone D3 v7 HTML file for a bar or comparison chart titled "Prompt output quality with and without a six-month maintenance cycle. The maintenance events are 30 minut". Use teacher AI-workflow states: learning goal, AI draft, teacher review gate, classroom use, equity check, and student evidence. Encode the AI-assisted step with one red mark and all teacher-controlled checks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/12-building-your-ai-workflow-fig-04.html`
