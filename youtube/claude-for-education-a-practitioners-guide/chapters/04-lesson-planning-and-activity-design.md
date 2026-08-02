# Chapter 4 — Lesson Planning and Activity Design

---

## 1. Classroom Problem

Deshawn teaches high school chemistry. He asks Claude for a lesson plan on chemical reactions and gets back three paragraphs introducing the topic, a teacher-led demonstration, a worksheet with ten definitional questions, and a homework problem set. The plan is complete. It has a learning objective, materials list, timing, and closure. It looks like every other lesson plan he has seen.

He posts it to his shared drive and starts printing the worksheet.

What Deshawn has is a lesson-shaped object, not a lesson. The demonstration keeps the chemical thinking with him, not with students. The worksheet questions can be answered by looking up definitions — they do not require students to apply chemical reasoning. The timing assumes everyone finishes step two before step three begins. Nothing in the plan reveals whether students learned anything until the unit test three weeks later.

Claude produced a plausible lesson. Deshawn accepted it because it looked right. That is the central risk of AI-assisted lesson planning: plausibility masquerading as alignment.

This chapter teaches you to use Claude as a planning partner without letting it decide what counts as learning.

---

## 2. What This Chapter Lets You Do

By the end of this chapter, you will be able to:

- Use Claude to generate lesson-plan drafts anchored in clear learning outcomes.
- Audit a Claude-generated plan for cognitive labor — whether students are doing the thinking.
- Redesign teacher-centered sequences into active learning alternatives.
- Use Claude to produce targeted lesson components rather than complete plans.
- Apply a five-question review gate before using any Claude-generated plan.

---

## 3. Core Concept — Backward Design and Cognitive Labor

Two principles govern good lesson planning. The first is backward design. The second is cognitive labor.

**Backward design**, developed by Wiggins and McTighe in *Understanding by Design*, holds that planning should begin with the evidence of learning — what would count as acceptable proof that students achieved the outcome — and work backward to instruction. Most lesson plans work forward: topic, activities, then assessment. Backward design reverses this. It asks: what will students produce or demonstrate? Then: what practice prepares them for that? Then: what instruction and materials enable the practice?

Claude, left to itself, plans forward. It begins with the topic, adds activities, and appends an assessment. The output feels complete because it mirrors the structure of lesson plans teachers have seen. But completeness is not alignment. A complete forward-planned lesson can have no logical connection between its activities and its assessment.

When you prompt Claude using the brief format from Chapter 3, starting with outcome and assessment evidence, you push Claude toward backward logic. This is not the tool's default mode; it is your instructional decision imposed on the tool.

**Cognitive labor** is the principle that students learn by thinking, not by being told. Freeman et al.'s 2014 meta-analysis of active learning in STEM courses across more than 225 studies found that active learning conditions reduced failure rates by 1.5 times and increased exam performance compared to traditional lecture (Freeman et al., active learning meta-analysis). Prince's review of active learning research found consistent positive effects on student engagement, retention, and transfer across disciplines (Prince, active learning review).

Ambrose et al. summarize the mechanism: learning requires students to engage in effortful processing — retrieving, connecting, applying, explaining, predicting (Ambrose et al., *How Learning Works*). Activities that allow students to be passive observers, definition-copiers, or answer-locators do not produce this processing. They produce compliance.

Claude is excellent at generating lesson plans where the teacher is active and the student is passive. It models the lesson-plan genre, and that genre often centers the teacher. Your audit task is to check, for every major activity in a Claude-generated plan, who is doing the thinking.

Merrill's first principles of instruction add precision: effective instruction is problem-centered and involves activation of prior knowledge, demonstration of the new skill or concept, application with feedback, and integration into real-world contexts (Merrill, first principles of instruction). These principles give you an audit vocabulary. When you look at a Claude-generated activity, you can ask: Is there a problem students are working on, or are they absorbing presented information? Is there a feedback mechanism in the activity, or is feedback deferred to grading?

---

## 4. A Worked Teaching Walkthrough

### The Situation

You teach a college writing course. Your next class session is ninety minutes. Students have submitted a first draft of an argumentative essay. Your learning outcome: students will revise a weak thesis statement using specific evidence from their own drafts, not general writing advice.

Most students believe their theses are already specific. Your experience tells you they confuse specificity with confidence of tone — a thesis can sound certain while saying very little.

You want Claude to help you design the class session.

### Step 1: Write the Backward-Design Brief

Using the eight-field template from Chapter 3:

```
LEARNER PROFILE: College students in first-year writing. Mixed academic
backgrounds. Have submitted first-draft argumentative essays.

PRIOR KNOWLEDGE: Can identify a thesis statement. Understand that a thesis
makes a claim. Have not revised a thesis based on evidence from their
own drafts.

MISCONCEPTION: Students believe their theses are already specific. They
confuse confident tone with precise claim. "Technology is changing society"
sounds certain; they do not see that it says nothing arguable.

TARGET OUTCOME: Students revise their own thesis statement to make one
specific, arguable claim tied to at least one piece of evidence they have
already written in their draft.

CONSTRAINTS: 90 minutes. Students bring printed drafts. No new writing
outside revision. Room allows small groups.

MODALITY: Active learning sequence — not a lecture. Students should be
doing the thinking for most of the 90 minutes. I want a draft sequence
with timing estimates.

ASSESSMENT EVIDENCE: At end of session, each student writes a revised thesis
on a half-sheet and staples it to their original draft. I review before
returning feedback.

REVIEW CRITERIA — Claude must not: Include a lecture segment longer than
10 minutes. Create activities where the teacher generates the examples.
Include generic writing advice not connected to the students' own drafts.
Give the criteria for a good thesis as a definition to copy.

REQUEST: Generate an activity sequence for this 90-minute session using
backward design. Students' drafts are the primary material.
```

### Step 2: Receive and Audit the Draft

Claude will likely return a sequence. Before accepting it, run the five-question audit:

**Audit Question 1 — Who is thinking?**
In each major activity, are students retrieving, applying, or producing? Or are they receiving?

**Audit Question 2 — Does the activity lead toward the outcome?**
If the outcome is "revise a thesis using evidence from their own draft," is every activity connected to that? Remove anything that is interesting but not load-bearing.

**Audit Question 3 — Is timing plausible?**
Claude's timing estimates are generic. Adjust for your students. If you know your class takes longer to get into small-group work, add time.

**Audit Question 4 — Where are the misconceptions surfaced?**
Does the sequence create a moment where students confront the difference between confident tone and specific claim? If not, the misconception survives the lesson.

**Audit Question 5 — Is there a feedback loop inside the class period?**
Students need to know whether their revision is working before they leave. Is peer feedback, teacher check-in, or self-assessment built into the sequence?

### Step 3: A Sample Activity Claude Might Generate — and How to Audit It

Suppose Claude generates this activity:

*"Show students two example thesis statements — one weak, one strong — and discuss what makes the strong one better. (15 minutes)"*

Audit: The teacher is generating the examples. Students are receiving. This activity does not require students to engage with their own drafts. It does not surface the misconception that students' own theses are already specific. It fails Questions 1, 2, and 4.

Revision: Replace with this:

*Students find their own thesis statement and underline it. Working in pairs, each student asks: "What is the one specific thing I am claiming? What would someone who disagreed say?" Pairs share one thesis sentence with the class; teacher asks the class whether the claim is arguable or general. (20 minutes)*

Now students are working on their own material. The misconception (my thesis sounds confident, therefore it is specific) has a chance to surface when peers ask "what would someone who disagrees say?"

### Step 4: Use Claude for Components, Not Only Complete Plans

One of the most productive ways to use Claude in lesson planning is to ask for specific components rather than full plans. Complete plans invite wholesale acceptance. Component requests stay focused.

Useful component requests:
- "Draft three discussion questions for this activity. Each question should be unanswerable by recalling a definition."
- "Generate four plausible student thesis statements ranging from vague to specific, using this topic. I will use these as examples."
- "Draft an exit ticket with two questions: one that assesses whether students achieved the outcome, and one that asks them to name one thing they are still unsure about."
- "Suggest two formative-check moments I can embed in this sequence without adding more than five minutes total."

Component requests are easier to evaluate than complete plans. They are also faster to revise. If one component misses, you discard it; you do not lose the whole sequence.

### Step 5: Use Claude to Critique Before Generating

A technique that experienced teachers find valuable: write your own rough lesson plan first, then ask Claude to critique it before asking it to generate alternatives.

Example prompt:

```
Here is my rough plan for a 90-minute writing class:
[paste your plan]

My outcome is: [outcome]
My students' misconception is: [misconception]

Critique this plan. Identify where students might be passive rather
than active. Identify where the activity does not lead toward the outcome.
Do not generate a replacement plan yet — just identify the gaps.
```

Claude's critique is often more useful than its original generation because you are asking it to evaluate against explicit criteria. After the critique, you can decide which gaps to address yourself and which to ask Claude to help redesign.

---

## 5. The Human Gate — What Stays With You

Lesson planning with Claude is a design iteration process, not a production process. The following decisions belong to you:

**Pacing and classroom reality.** Claude does not know that your Tuesday section always arrives ten minutes distracted after gym class, that your building runs fire drills in November without notice, or that three students in your third period have modified schedules. Timing adjustments are yours.

**Content accuracy.** Claude can introduce disciplinary errors, oversimplifications, or outdated content, particularly in rapidly changing fields. Verify any factual claims in generated examples before using them with students.

**Sequence logic for your specific unit.** A lesson that works for a class that has completed Unit 2 may not work for a class still in Unit 1. Claude does not track your unit sequence unless you tell it explicitly. You are responsible for coherence across the unit.

**Who needs what.** Claude does not know which students need more scaffolding, which can handle extension, or which are disengaged because they already know the material. Differentiation within a lesson plan is your instructional judgment, not a Claude output (see Chapter 6).

**The relationship dimension.** Activities that look equivalent on paper may land differently depending on the trust in your classroom, the social dynamics of particular groups, and what students experienced the period before they arrived at yours. These are things you know. Claude does not.

---

## 6. Common Mistakes

**Mistake 1: Accepting the complete plan.**
Complete plans are complete. That is their surface quality. Completeness is not alignment. Audit the plan; do not accept its completeness as evidence of quality.

**Mistake 2: Requesting a lesson plan without stating the outcome first.**
If you do not anchor the prompt in a specific outcome, Claude will generate content-coverage activities. Always start with what students should be able to do.

**Mistake 3: Keeping the teacher at the center of every activity.**
Claude models lesson-plan genre, and that genre often places the teacher as explainer and demonstrator. Explicitly instruct Claude: "Students should be doing the intellectual work in every activity." Then check whether the output honors that.

**Mistake 4: Using Claude's examples without checking them.**
Claude generates examples that are often slightly wrong, slightly dated, or slightly mismatched to your disciplinary standards. Check every example against your own knowledge of the field.

**Mistake 5: Ignoring the formative feedback loop.**
Lessons that have no feedback mechanism inside them — no moment where students learn whether they are right — leave students to discover errors at the graded assessment. Ask Claude explicitly to include a formative check; then verify it is there.

---

## 7. Try This

**Exercise 1 — The cognitive labor audit.**
Take a lesson plan you have used before — your own, a colleague's, or one from a shared resource library. For each activity, write one word next to it: "receiving" (students are watching or listening) or "producing" (students are thinking, writing, discussing, solving, or making). Count the ratio. Then identify one "receiving" moment you could redesign into a "producing" moment.

**Exercise 2 — Component request practice.**
For your next lesson, do not ask Claude for a complete plan. Instead, ask for three specific components: one discussion question that cannot be answered by reciting a definition, one exit ticket aligned to your specific outcome, and one formative check that takes fewer than five minutes. Evaluate each component separately. Notice which components required more revision.

**Exercise 3 — Critique before generate (classroom-applicable).**
Write your own rough lesson plan for an upcoming class. Submit it to Claude with explicit audit criteria (see Step 5 above). Read the critique. Address at least one gap yourself before asking Claude to draft any replacement activities. This sequence keeps the pedagogical reasoning with you.

---

## 8. What Would Change My Mind

This chapter argues that Claude-generated lesson plans require systematic audit and that teachers should drive the backward-design logic. That argument would weaken if:

- AI models became consistently good at inferring student misconceptions and pacing realities from minimal context. That would require models to access classroom-specific data they do not currently have [verify — current as of writing].
- Research showed that teachers using AI-generated lesson plans without audit produced better student outcomes than teachers who audited and revised. The existing literature on instructional alignment suggests the opposite: alignment between outcomes, activities, and assessments is positively associated with student learning (Wiggins and McTighe, *Understanding by Design*).
- The administrative load on teachers became so heavy that any planning assistance — even unaudited — improved outcomes by freeing time for human-centered work. This is a real concern worth watching; the answer depends on whether freed time is reinvested in student relationships and feedback rather than more content production.

---

## 9. Still Puzzling

- What is the minimum viable audit for a lesson plan when a teacher is under severe time pressure? A five-question audit may still be too long for teachers preparing six lessons a day.
- How should audit criteria differ across disciplines? The "who is thinking" question may have different answers in a studio art class, a mathematics lecture hall, and a lab-based science course.
- Does Claude improve lesson-plan quality when used iteratively — multiple rounds of critique and revision — compared to a single-generation-and-audit approach? That comparison has not been systematically studied.

---

## 10. Bridge to Chapter 5

A well-designed lesson generates student work. That work requires feedback. Chapter 5 addresses the moment where AI assistance is most ethically loaded: when Claude is helping you respond to what a specific student has actually done. Feedback is not lesson planning. It is judgment about a person's learning. The human gate there is sharper, and the risks of overhelping are more direct.

---

## Sources Used

- Ambrose, S. A., Bridges, M. W., DiPietro, M., Lovett, M. C., and Norman, M. K. *How Learning Works: Seven Research-Based Principles for Smart Teaching.* Jossey-Bass, 2010.
- Anthropic. Claude documentation. https://docs.anthropic.com/ [verify — current as of writing]
- Freeman, S., Eddy, S. L., McDonough, M., Smith, M. K., Okoroafor, N., Jordt, H., and Wenderoth, M. P. "Active Learning Increases Student Performance in Science, Engineering, and Mathematics." *Proceedings of the National Academy of Sciences* 111, no. 23 (2014): 8410–8415.
- Merrill, M. D. "First Principles of Instruction." *Educational Technology Research and Development* 50, no. 3 (2002): 43–59.
- Nilson, L. B. *Teaching at Its Best: A Research-Based Resource for College Instructors.* Jossey-Bass, 2016.
- Prince, M. "Does Active Learning Work? A Review of the Research." *Journal of Engineering Education* 93, no. 3 (2004): 223–231.
- UNESCO. Guidance for Generative AI in Education and Research. UNESCO, 2023.
- Wiggins, G., and McTighe, J. *Understanding by Design.* ASCD, 2005.
