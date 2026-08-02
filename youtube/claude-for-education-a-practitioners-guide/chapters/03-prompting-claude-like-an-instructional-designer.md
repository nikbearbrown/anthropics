# Chapter 3 — Prompting Claude Like an Instructional Designer

---

## 1. Classroom Problem

Marta teaches ninth-grade biology in a mid-sized public school. She has tried Claude a handful of times, mostly by typing something like: "Give me a lesson on cells." The results were fine — clean paragraphs, reasonable vocabulary — but they fit no one in particular. They didn't match her unit sequence, didn't address the misconception she knew her students carried (that cells are static containers rather than dynamic systems), and didn't line up with what she actually needed students to be able to do on Friday's lab assessment.

Marta's problem is not that Claude is bad. Her problem is that her prompts describe a topic rather than a teaching situation. She is asking Claude to be a search engine when she needs it to be a design partner.

This chapter shows you how to write prompts the way an instructional designer would write a project brief: specific enough to be actionable, bounded enough to be reviewable, and anchored in what students actually need to learn.

---

## 2. What This Chapter Lets You Do

By the end of this chapter, you will be able to:

- Translate a teaching goal into a structured Claude brief.
- Identify the eight fields that separate a useful educational prompt from a generic one.
- Recognize common prompt failures and their instructional consequences.
- Use reusable prompt patterns for lessons, feedback, adaptations, tutoring sessions, and rubric audits.

---

## 3. Core Concept — Prompting as Instructional Specification

A prompt is not a magic phrase. It is a specification. When a software engineer writes a specification, she describes the user, the inputs, the expected behavior, the constraints, and the acceptance criteria. When an instructional designer writes a design brief, she describes the learner, the prior knowledge, the misconception, the target outcome, the activity constraints, the evidence of learning, and the review criteria.

Good prompting for education is instructional specification made explicit (Anthropic prompt engineering documentation [verify — current as of writing]).

The reason this matters is that Claude generates plausible language — language that sounds like what a lesson, rubric, or feedback comment looks like. Plausibility is not alignment. A plausible lesson may have nothing to do with your students, your unit, or your learning objectives. Instructional specification transforms a plausible output into a useful candidate that you can evaluate against real criteria.

Three educational theorists anchor this idea:

**Robert Gagne** argued that effective instruction requires nine distinct conditions, including gaining attention, activating prior knowledge, providing the stimulus, guiding learning, and enabling transfer (Gagne, *Conditions of Learning*). A prompt that specifies these conditions will produce materials designed to meet them. A prompt that skips them will produce materials that assume they are not needed.

**M. David Merrill** proposed that learning is facilitated when instruction is problem-centered and moves through activation, demonstration, application, and integration (Merrill, first principles of instruction). This maps directly onto the kind of brief you will write: name the problem the student needs to solve, describe what demonstration looks like, specify how practice is structured, and state how the student will integrate the new knowledge.

**Grant Wiggins and Jay McTighe** made the case that design should begin with evidence — what you would accept as proof that the student has learned — and work backwards to instruction (Wiggins and McTighe, *Understanding by Design*). This "backward design" principle reframes prompting: you specify the assessment evidence first, then ask Claude for activities that lead there.

---

## 4. The Eight-Field Instructional Brief

The following eight fields make up a reusable instructional brief. Each field prevents a specific failure.

### Field 1: Learner Profile

Who are these students? Grade level, course, rough context, language situation, any relevant access needs.

*Failure it prevents:* Claude defaulting to a generic college-educated adult reader when you teach seventh graders whose home language is not English.

### Field 2: Prior Knowledge

What do these students already know that is relevant? What gaps are you working across?

*Failure it prevents:* Material pitched at the wrong level, assuming concepts students have not yet encountered — or assuming they lack knowledge they already hold.

### Field 3: Misconception

What does your experience tell you students believe that is wrong or incomplete?

*Failure it prevents:* Lessons that never confront the error students are actually making, leaving misconceptions intact even after instruction (Ambrose et al., *How Learning Works*).

### Field 4: Outcome

What should the student be able to do, make, argue, or demonstrate after instruction? This is the measurable terminal behavior — not a topic.

*Failure it prevents:* Claude producing content-coverage prose rather than outcome-aligned activity. "Students will understand photosynthesis" is not an outcome. "Students will explain why a plant placed in the dark for two weeks loses mass" is an outcome.

### Field 5: Constraints

Time, format, tools available, word count, age-appropriateness, reading level, no-go zones.

*Failure it prevents:* Receiving a three-day unit when you have forty-five minutes, or a technology-heavy plan for a classroom with one shared device.

### Field 6: Modality

What form should the output take? Lesson plan, worksheet, discussion prompt, exit ticket, rubric draft, comment bank, reading adaptation, tutoring script.

*Failure it prevents:* Getting prose explanation when you need a structured document your students can interact with.

### Field 7: Assessment Evidence

What would count as acceptable evidence that the student has achieved the outcome? This can be informal (exit ticket, class discussion), or formal (rubric-scored essay, lab report).

*Failure it prevents:* Activities that are engaging but do not connect to how you will actually know whether students learned anything.

### Field 8: Teacher Review Criteria

State explicitly what Claude must not do, and what you will check before using the output. Common not-do's: do not invent student data; do not lower rigor without disclosure; do not provide final answers when drafting a tutoring script; do not generate questions that could be answered by looking up a definition.

*Failure it prevents:* Outputs that look polished but contain invented examples, reduced challenge, or answers embedded in what should be student-facing practice.

---

## 5. A Worked Teaching Walkthrough

### The Situation

You teach a college introductory economics course. You want to build a thirty-minute discussion activity on opportunity cost. Students have read a textbook chapter. Your experience tells you that most of them understand opportunity cost as "what you give up" but apply it only to money — not to time, attention, or non-market goods. The unit assessment asks students to analyze a real decision using opportunity cost reasoning, including identification of the next-best alternative.

### Step 1: Write the Brief

Copy the template below and fill in each field before submitting to Claude.

---

**Prompt template — instructional brief**

```
LEARNER PROFILE: [Who are your students?]

PRIOR KNOWLEDGE: [What do they already know? What gaps exist?]

MISCONCEPTION TO ADDRESS: [What do they believe that is incomplete or wrong?]

TARGET OUTCOME: [What should they be able to DO after this activity?]

CONSTRAINTS: [Time, format, tools, reading level, access needs]

MODALITY: [What form should the output take?]

ASSESSMENT EVIDENCE: [What would count as evidence of learning?]

REVIEW CRITERIA — Claude must not: [List what Claude should avoid]

REQUEST: [Your actual ask, in one or two sentences]
```

---

**Filled example — opportunity cost discussion activity**

```
LEARNER PROFILE: First-year college students in introductory economics.
Average age 18–19. Varied mathematical backgrounds. No economics
prerequisites assumed.

PRIOR KNOWLEDGE: Have read a textbook chapter on opportunity cost.
Understand the definition "value of the next-best alternative." Have not
applied the concept in any practice task yet.

MISCONCEPTION TO ADDRESS: Students apply opportunity cost only to money.
They do not spontaneously include time, attention, or forgone experiences
as opportunity costs. They also tend to list multiple alternatives rather
than identifying the single next-best one.

TARGET OUTCOME: Students will identify the correct opportunity cost
(the value of the single next-best alternative, not a list of possibilities)
for at least two non-market decisions — one involving time and one involving
attention or social good.

CONSTRAINTS: 30-minute class period. Discussion format — no writing required
during activity. No technology in room. Students are seated in rows, not
small groups.

MODALITY: A discussion sequence with 3–4 teacher-led questions and brief
facilitator notes for each question. Include one check question that reveals
whether students have applied the misconception.

ASSESSMENT EVIDENCE: A one-sentence exit ticket: "State the opportunity cost
of studying for this exam instead of sleeping an extra hour." A correct
response names one thing (sleep's benefits), not a list.

REVIEW CRITERIA — Claude must not: Invent statistics. Use examples requiring
prior knowledge of specific industries. Include questions answerable by
reciting the definition alone.

REQUEST: Draft the discussion sequence with facilitator notes.
```

### Step 2: Review the Output

Before using any Claude output, run it through the checklist from the research:

- Is the learner accurately described in the output?
- Is the prior knowledge assumption correct?
- Does the activity actually surface and address the misconception?
- Does the activity lead toward the stated outcome?
- Are the constraints respected?
- Is there assessment evidence built in?
- Has Claude avoided the no-go behaviors?

Claude will sometimes produce outputs that pass visual inspection but fail instructional review. A question can look like a good discussion prompt and still be answerable by reciting the definition. Your review is the quality gate.

### Step 3: Revise and Annotate

Do not use Claude's output as-is. Annotate, adjust, and cut. Add the specific example your class discussed last week. Remove the question that is too abstract for your context. Change the vocabulary to match your students' register. The brief makes the output useful; your review makes it yours.

---

## 6. Five Reusable Brief Patterns

The following patterns adapt the eight-field brief for specific educational tasks. Fill in the brackets for each.

**Pattern A — Lesson brief:** For planning a class session or module segment.

**Pattern B — Feedback brief:** For drafting feedback comments on student work. Include field for "feedback stance" (coaching questions, directive comments, or rubric-aligned language) and "what Claude must not do" that explicitly prohibits rewriting the student's text.

**Pattern C — Accessibility adaptation brief:** Include current reading level, target reading level, concepts that must not be simplified, and whether vocabulary glosses should be embedded or marginal.

**Pattern D — Tutoring script brief:** Include "Claude must not give final answers" and specify whether the script should ask questions, offer hints, or both.

**Pattern E — Rubric audit brief:** Describe the assignment, the current rubric, and ask Claude to identify criteria that are ambiguous, grade-compressed (all descriptors sound similar), or unverifiable from student work.

All five patterns appear in reusable form in the workshop card at the end of this chapter.

---

## 7. The Human Gate — What Stays With You

Instructional specification is not a hand-off. You are creating conditions for a useful draft, not delegating instructional decisions.

The following judgments are yours, not Claude's:

- **Outcome validity.** You decide what learning matters for your students in your course context. Claude can suggest; it cannot decide.
- **Misconception accuracy.** You know what your students actually believe. The misconception field is only as good as your pedagogical content knowledge.
- **Classroom fit.** Claude does not know that your third-period class moves faster than your first, that one student has a 504 plan requiring extended time, or that the room has no projector.
- **Example authenticity.** Claude generates plausible examples. Plausible is not the same as true, representative, or appropriate for your community.
- **Tone and relationship.** Claude does not know your students. Feedback that is technically accurate can still be damaging if the tone is wrong for a specific student at a specific moment.

This is why the brief includes a review-criteria field. "Claude must not" is not distrust of the tool; it is clarity about where human judgment remains essential. The act of writing the constraint makes your own professional knowledge visible to you.

---

## 8. Common Mistakes

**Mistake 1: Describing a topic instead of a situation.**
"Give me a lesson on the American Revolution" describes content. "Give me a discussion activity for tenth graders who understand the political causes but cannot yet explain why the revolution succeeded in America but not in France" describes a teaching situation.

**Mistake 2: Omitting the misconception.**
Lessons that do not address what students actually believe leave the misconception intact. Instruction that feels complete produces learning that doesn't transfer (Ambrose et al., *How Learning Works*).

**Mistake 3: Accepting the first output.**
Claude's first output is a draft. Treat it like a first draft from a capable but uninformed colleague: useful, in need of revision, not ready to use.

**Mistake 4: Forgetting to state what Claude must not do.**
If you do not specify "do not reduce the reading level without disclosure," Claude may simplify text to improve clarity and produce material below grade-level expectation.

**Mistake 5: Writing the brief once and reusing it unchanged.**
A brief is a situated document. Your learner profile shifts between sections. Your constraints change when you lose a day to a school event. Revision of the brief is revision of the instructional design.

---

## 9. Try This

**Exercise 1 — Brief autopsy.**
Take a prompt you have used before with Claude, or write one you would naturally use (the kind you used before reading this chapter). Map it against the eight fields. Which fields are missing? Draft the missing fields and resubmit. Compare the outputs.

**Exercise 2 — Brief for tomorrow.**
Choose one class session you are planning this week. Write a full eight-field brief before prompting Claude. Use the lesson-brief pattern (Pattern A above). After Claude responds, run the checklist from Section 5. What did Claude get right? What required revision? Keep a one-paragraph note on what the brief changed.

**Exercise 3 — Misconception excavation (classroom-applicable).**
Before writing your next brief, ask three students (informally, after class or in office hours) what they currently believe about the concept you are planning to teach. Write their actual language into the misconception field of your brief. Notice whether Claude's output now engages more directly with what you know your students think.

---

## 10. What Would Change My Mind

This chapter argues that instructional specification improves Claude outputs. That argument would weaken if:

- AI models became reliably good at inferring learner context from minimal description, making specification overhead unnecessary. That capability does not yet exist at the specificity teaching requires [verify — current as of writing].
- Research showed that teachers using structured briefs produced worse learning outcomes than teachers using open prompts. No such finding exists; the opposite is suggested by the literature on instructional design alignment (Wiggins and McTighe, *Understanding by Design*).
- Specification time costs exceeded the benefit for experienced teachers with deep pedagogical content knowledge who could verify outputs quickly. This is a real trade-off worth tracking; the answer probably depends on how novel the content or format is.

---

## 11. Still Puzzling

- How much brief detail is too much? There is probably a point at which specification becomes so long that it introduces its own errors and makes revision harder. That threshold has not been established for educational prompting.
- Should the misconception field be a standard element of AI-assisted lesson planning tools, or does it require teacher knowledge that cannot be systematized?
- How do briefs change for multilingual classrooms where the gap between a student's content knowledge and English-language expression creates a confounding variable in the learner profile?

---

## 12. Bridge to Chapter 4

A well-written brief produces a useful draft. Chapter 4 takes that draft and asks the harder question: does the lesson plan actually protect student thinking? Activity design is where briefs meet the classroom, and where the temptation to accept a polished plan — rather than audit it against student cognitive labor — is strongest.

---

## Sources Used

- Ambrose, S. A., Bridges, M. W., DiPietro, M., Lovett, M. C., and Norman, M. K. *How Learning Works: Seven Research-Based Principles for Smart Teaching.* Jossey-Bass, 2010.
- Anthropic. Claude prompt engineering documentation. https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview [verify — current as of writing]
- Gagne, R. M. *The Conditions of Learning and Theory of Instruction.* Holt, Rinehart and Winston, 1985.
- Merrill, M. D. "First Principles of Instruction." *Educational Technology Research and Development* 50, no. 3 (2002): 43–59.
- Wiggins, G., and McTighe, J. *Understanding by Design.* ASCD, 2005.
