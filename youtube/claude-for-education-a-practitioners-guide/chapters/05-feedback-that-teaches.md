# Chapter 5 — Feedback That Teaches

---

## 1. Classroom Problem

It is 10 p.m. on a Tuesday. Priya has thirty-two student essays due tomorrow and an hour left before she needs to stop. She opens the first paper. The thesis is muddy. The evidence is present but not connected to the claim. The conclusion restates the introduction. She has seen this paper, or a close cousin of it, many times. She types a comment about the thesis, then a comment about evidence, then a comment about the conclusion. She copies a phrase she has written before — "work on connecting your evidence to your claim more explicitly" — and pastes it in. Twenty minutes and three papers later, she is not sure she is still reading.

Priya is not a bad teacher. She is trying to give feedback under conditions that make good feedback nearly impossible: volume, time, fatigue, and repetition. What she is actually producing is efficient notation. Notes that tell students something is wrong without giving them enough to try something different.

This is where Claude can help. And this is where Claude can harm.

Feedback is the teaching moment closest to the student's actual thinking. It is also the teaching moment where AI assistance is most likely to slip from drafting support into ghostwriting, from coaching into answer-giving, from preserving student agency into removing it. This chapter teaches you to use Claude to draft better feedback while keeping every substantive judgment — about this student's thinking, on this draft, in this context — with you.

---

## 2. What This Chapter Lets You Do

By the end of this chapter, you will be able to:

- Use Claude to draft feedback options while preserving your judgment about which option fits this student.
- Distinguish three types of feedback response and identify which Claude can draft and which it cannot produce.
- Write a feedback brief that prevents Claude from overhelping.
- Apply a six-question quality check to any AI-drafted feedback before delivering it to a student.
- Recognize the boundary between feedback and grading, and protect it.

---

## 3. Core Concept — What Makes Feedback Work

The most useful description of feedback's function comes from Hattie and Timperley's 2007 review: effective feedback answers three questions — Where am I going? How am I going? Where to next? (Hattie and Timperley, "The Power of Feedback"). Feed-up (the goal), feed-back (current status), and feed-forward (what to try) are the three functions. Most teacher feedback concentrates on the second function and neglects the third. Students often receive accurate descriptions of what is wrong without receiving usable guidance about how to revise.

Susan Brookhart's work on classroom feedback adds precision to what "usable" means: feedback should be timed appropriately (close to the work), referenced to criteria (not impressions), specific enough to guide revision, and pitched at a level of challenge the student can actually meet (Brookhart, *How to Give Effective Feedback to Your Students*). Praise without criteria and criticism without direction both fail this test.

Nicol and Macfarlane-Dick's model of formative assessment and self-regulated learning argues that the deepest goal of feedback is to build the student's capacity to judge their own work — to internalize the criteria so thoroughly that external feedback becomes less necessary over time (Nicol and Macfarlane-Dick, formative assessment and self-regulated learning). This means feedback that does the judgment for the student — that rewrites the thesis, supplies the missing argument, or corrects every surface error — may produce a better-looking draft while leaving the student no better at drafting.

Royce Sadler's foundational work on formative assessment makes the same point structurally: students cannot use feedback to improve unless they understand the standard, can compare their work to it, and know how to close the gap (Sadler, formative assessment and standards). Feedback that tells a student "your thesis is weak" without explaining what a strong thesis would look like for this assignment tells them where they are but not where they are going or how to get there.

These four bodies of research converge on a practical principle: feedback teaches when it supports the student's revision thinking, not when it replaces it.

Claude can produce language that sounds like feedback. The question you must answer is whether that language supports revision thinking or replaces it.

---

## 4. Three Types of Feedback Response

Before using Claude for feedback, it helps to distinguish three types of feedback response. They differ in what they require of the student and in what Claude can and cannot contribute to each.

**Type 1 — Diagnostic description:** Describes what the student has done, accurately referenced to criteria. Example: "Your thesis states a topic but does not yet make a claim that could be contested." Claude can draft this type accurately if given the student's text, the relevant criteria, and a constraint against rewriting.

**Type 2 — Coaching question:** Asks the student to think rather than telling them what to think. Example: "If someone read this thesis and asked 'so what?' — what would you want them to understand?" Claude can generate coaching questions from criteria, but the right question for this student at this moment requires your knowledge of the student. Use Claude to generate three to five options; you select the one that fits.

**Type 3 — Directive correction:** Tells the student explicitly what to change or how to revise, sometimes rewriting the problematic passage. Example: "Change your thesis to: [rewritten sentence]." Claude should not write this type for you. Directive correction at the sentence level removes the student's revision work from the student. If the teacher rewrites the thesis, the student submits a thesis the teacher wrote. This is the clearest way AI assistance becomes overhelping.

The boundary is not always sharp. A question that implies its own answer ("Wouldn't it be stronger to lead with your main claim?") functions more like a directive correction than a coaching question. Your review must catch these.

---

## 5. A Worked Teaching Walkthrough

### The Situation

A student has submitted a history essay. The prompt asked for an argument about the causes of World War I. The student's thesis reads: "World War I was caused by many complex factors including nationalism, militarism, and the alliance system." The body paragraphs describe each factor in sequence. No paragraph argues for a relationship between factors or for the relative weight of any one.

Your outcome for this assignment: students will construct an original argument that claims a relationship between causes, not merely lists them.

The student needs feedback. You have twenty minutes before your next class.

### Step 1: Write the Feedback Brief

```
STUDENT WORK: [paste the student's thesis and first body paragraph, or
summarize them accurately]

ASSIGNMENT CRITERIA: The essay should construct an argument about
cause-and-effect relationships, not list factors. The thesis should
make a claim that could be contested. Evidence should be used to
support the relationship being argued, not just to describe the factor.

STUDENT SITUATION: This is a first essay in the course. The student
demonstrates solid factual knowledge. This is a common first-draft
failure — listing rather than arguing.

FEEDBACK STANCE: I want coaching questions that prompt revision thinking,
not corrections. Do not rewrite any of the student's sentences. Do not
state what the thesis should say.

REVIEW CRITERIA — Claude must not: Rewrite the student's thesis.
Provide a model argument the student could paste in. Use praise that
is not tied to specific criteria. Invent details about the student's
reasoning beyond what is shown in the text.

REQUEST: Draft three coaching questions I could ask this student about
their thesis. Each question should prompt the student to think about
the relationship between causes rather than telling them to list less.
Then draft one sentence of diagnostic description tied to the assignment
criteria.
```

### Step 2: Read the Output for Overhelping

Claude will return coaching questions and a diagnostic sentence. Before selecting, check for:

- Questions that answer themselves ("Have you considered that the assassination of Franz Ferdinand was really the trigger rather than the cause?")
- Questions that imply a specific revision the student should make
- Diagnostic language that is vague praise ("This shows good historical thinking")
- Any rewriting of the student's text

Discard any response that answers rather than asks. Select the coaching question that opens thinking rather than closes it.

### Step 3: Add Your Knowledge of the Student

Claude's coaching question is a starting draft. Before delivering it, add what you know:

- Is this student anxious about getting things wrong? A question that implies failure will land differently than one that opens possibility.
- Has this student already revised once and been told the same thing? If so, a coaching question may not be enough — a different kind of support is needed.
- Does this student understand what "an argument" means in historical writing? If not, the coaching question assumes prior knowledge they do not have.

These are things Claude cannot know. They are the reason feedback is a human act even when the drafting is assisted.

### Step 4: Run the Six-Question Quality Check

Before delivering any AI-drafted feedback to a student:

1. **Is it tied to criteria?** Does the feedback reference the assignment's criteria rather than impressions?
2. **Is the next action specific?** Does the student have something to try, or only a description of the problem?
3. **Is the tone respectful and appropriately encouraging for this student?** You know this student; adjust the tone accordingly.
4. **Is student agency preserved?** Has Claude avoided rewriting, implying the answer, or reducing the student's revision work?
5. **Is there no invented evidence?** Has Claude avoided inventing claims about the student's intentions or reasoning not visible in the submitted text?
6. **Have you approved the final judgment?** Is your professional knowledge of this student, this assignment, and this moment reflected in the final feedback?

If any answer is no, revise before sending.

---

## 6. The Feedback–Grading Boundary

Feedback and grading are not the same task, and the confusion between them is one of the clearest failure modes of AI-assisted response.

**Feedback** is information that supports learning. It is directed at the student's revision thinking. It does not produce a score.

**Grading** is evaluation that produces a judgment about the quality of work relative to criteria, usually resulting in a mark or grade. It requires the teacher to make a summative decision about what the student demonstrated.

Claude can draft feedback language. It cannot grade. This is not a capability limitation; it is an authority and context limitation. Grading requires knowledge of what this student was trying to do, what constraints they were working under, how their work compares to the range of work in the class, and what the grade means institutionally for this student's trajectory. Claude does not have this knowledge.

The risk of using Claude to draft "feedback" is that teachers sometimes accept outputs that contain implicit grades — statements like "this essay reaches a B-level of argumentation" or "this draft is not yet passing." If you paste such language into your comments without review, you have delegated a grading judgment to a system without the context to make it.

Remove any evaluative judgment from Claude's feedback drafts unless you are explicitly using Claude to help you articulate a grade you have already determined. Even then, the final language and the grade itself are yours.

---

## 7. Comment Banks — A Useful Pattern That Requires Care

One productive application of Claude in feedback work is generating a comment bank: a set of reusable feedback phrases you can adapt and deploy rather than rewriting from scratch for each paper.

A comment bank generated by Claude is useful when:
- You anchor it to specific assignment criteria
- The comments are written as coaching language (What to try) rather than diagnostic only (What went wrong)
- You treat the bank as a starting vocabulary, not a script
- You edit comments before inserting them to reflect the specific student

A comment bank generated by Claude becomes harmful when:
- Comments are copied verbatim without adjustment to the specific student
- The same comment appears on ten papers with no variation
- The bank substitutes for reading the student's work

The failure mode of comment banks is not AI overreach; it is teacher underreading. If you use a comment bank to avoid engaging with a specific student's thinking, you have produced notation, not feedback.

---

## 8. Student Self-Assessment as a Feedback Amplifier

One of the most useful ways to use Claude in the feedback cycle is to draft student self-assessment prompts — questions you ask students to answer before you read their work or before you return it.

This is a high-leverage application because:
- It keeps the cognitive labor with the student (Nicol and Macfarlane-Dick, formative assessment and self-regulated learning)
- It gives you information about what the student thinks they did before you read what they actually did
- It reduces the amount of feedback you need to write, because students who can accurately self-assess need less external corrective feedback

Example Claude request:

```
ASSIGNMENT: Argumentative essay on WWI causes.
OUTCOME: Students construct an argument about causal relationships,
not a list of factors.
COMMON STUDENT MISCONCEPTION: Students believe listing factors is
equivalent to arguing about their relationships.

Draft three self-assessment questions students answer before
submitting their draft. Questions should help them notice whether
they are listing or arguing, without telling them which they are doing.
```

The resulting questions give you a diagnostic window into each student's metacognition. Combined with the draft, they make your feedback more targeted and more efficient.

---

## 9. The Human Gate — What Stays With You

Every piece of feedback that leaves your hands carries your professional authority. Students read feedback from their teacher, not from Claude. The following remain entirely yours:

**The judgment about this student.** Claude reads text. You know the student. Feedback decisions — how direct to be, how much encouragement is warranted, whether this student needs challenge or reassurance — require knowledge you hold.

**The decision to give directive correction.** There are moments when a student needs you to show them rather than ask them — when coaching questions will be understood as evasion, or when a student is so far from the standard that questions are not an efficient path. That decision is yours. Claude should not make it for you by defaulting to directives.

**The final language.** Even when Claude drafts the feedback, you are responsible for the words a student reads. Read every comment aloud before sending. Would you say this to the student? Does it sound like you?

**The grade.** As stated: grading is yours. Claude can help you articulate your reasoning; it cannot make the judgment.

**The relationship.** Feedback lands in a relationship. A comment that is technically accurate can damage trust if the relationship is fragile, if the timing is wrong, or if the tone misreads the student's state. You know this. Claude does not.

---

## 10. Common Mistakes

**Mistake 1: Pasting Claude's feedback directly into a grade book or learning management system.**
Always read and revise. The act of reading forces you to evaluate whether the language fits the student.

**Mistake 2: Asking Claude to "write feedback" rather than "draft feedback options."**
When you ask for a single feedback comment, you tend to accept it. When you ask for three options, you evaluate them. The evaluation keeps the judgment with you.

**Mistake 3: Generating feedback without providing the student's actual text.**
Claude cannot give specific feedback on work it has not seen. Feedback based on your description of the work will be generic. Paste in the relevant passage (see privacy guidance, Chapter 9, before doing so) or describe it with sufficient specificity.

**Mistake 4: Letting Claude rewrite the student's text.**
This is the clearest form of overhelping. If the feedback comment contains a revised version of the student's sentence, the student's revision work is done. Remove it.

**Mistake 5: Using the same AI-generated comment bank for every student.**
Students notice when comments do not fit their specific work. Generic feedback communicates that the teacher did not read carefully. Edit every comment for the specific student.

**Mistake 6: Using AI-drafted feedback to avoid reading student work entirely.**
Feedback assistance is for situations where you have read the work and need language help, or where you need a coaching question and want options to choose from. If you are using Claude to avoid engaging with student thinking, you have removed the learning relationship from the process.

---

## 11. Try This

**Exercise 1 — Three-type audit.**
Take five feedback comments you have written recently (your own, unassisted). Classify each as Type 1 (diagnostic description), Type 2 (coaching question), or Type 3 (directive correction). What is your ratio? Would any Type 3 comments be more effective as Type 2?

**Exercise 2 — Coaching question generation.**
Choose a common error your students make. Write a feedback brief (Section 5, Step 1) specifying the error, the assignment criteria, and the constraint "do not rewrite student text." Ask Claude to generate five coaching questions. Evaluate each against the question: "Does this ask the student to think, or does it imply the answer?" Select one. Use it next time a student makes that error.

**Exercise 3 — Self-assessment prompt design (classroom-applicable).**
For your next major assignment, draft a student self-assessment sequence using Claude. Use the pattern in Section 8. Deploy the self-assessment before students submit. After reading drafts, note whether students who completed the self-assessment submitted work that required different (more targeted, less basic) feedback. Adjust the self-assessment for the next cycle.

---

## 12. What Would Change My Mind

This chapter argues that Claude should draft feedback options — not final feedback — and that grading judgment belongs to the teacher entirely. That argument would weaken if:

- Research demonstrated that AI-generated feedback produced better student revision and learning outcomes than teacher-generated feedback, across a range of students and contexts. Some studies suggest AI feedback can support specific kinds of writing revision, but general superiority over teacher judgment has not been established [verify — current as of writing].
- Models became capable of accurately inferring student emotional state, relationship context, and learning trajectory from submitted work alone. That would require access to longitudinal student data that current AI systems do not have in the typical classroom deployment [verify — current as of writing].
- The volume and complexity of grading loads became so extreme that teacher-read feedback became statistically rare compared to AI-generated feedback. In that scenario the ethical question shifts: the harm is in the system, not the tool.

---

## 13. Still Puzzling

- At what point does a coaching question become directive? The line between "What would you want a reader who disagreed to understand?" and "Have you considered that your claim is too broad?" is a matter of degree, not kind. What is the right test?
- How should feedback briefs handle situations where a student's first language is not the language of instruction? The advice "match the tone to the student" becomes more complex when tone reads differently across linguistic and cultural contexts.
- Should students know when their teacher used AI to help draft feedback comments? This is an emerging transparency question that institutions have not yet resolved. The argument for disclosure — that students deserve to know — is not trivially weaker than the argument against.

---

## 14. Bridge to Chapter 6

Feedback designed for the average student misses the students who need it most. Chapter 6 addresses differentiation and accessibility: how to use Claude to adapt materials, adjust reading levels, and provide varied entry points without lowering the intellectual target. The principle is the same as in feedback — Claude can generate options; the teacher decides which option fits which learner.

---

## Sources Used

- Ambrose, S. A., Bridges, M. W., DiPietro, M., Lovett, M. C., and Norman, M. K. *How Learning Works: Seven Research-Based Principles for Smart Teaching.* Jossey-Bass, 2010.
- Anthropic. Claude documentation. https://docs.anthropic.com/ [verify — current as of writing]
- Brookhart, S. M. *How to Give Effective Feedback to Your Students.* ASCD, 2008.
- CAST. Universal Design for Learning Guidelines. https://udlguidelines.cast.org/ [verify — current as of writing]
- Hattie, J., and Timperley, H. "The Power of Feedback." *Review of Educational Research* 77, no. 1 (2007): 81–112.
- NIST. AI Risk Management Framework. National Institute of Standards and Technology, 2023.
- Nicol, D. J., and Macfarlane-Dick, D. "Formative Assessment and Self-Regulated Learning: A Model and Seven Principles of Good Feedback Practice." *Studies in Higher Education* 31, no. 2 (2006): 199–218.
- Sadler, D. R. "Formative Assessment and the Design of Instructional Systems." *Instructional Science* 18, no. 2 (1989): 119–144.
- UNESCO. Guidance for Generative AI in Education and Research. UNESCO, 2023.
- U.S. Department of Education. Artificial Intelligence and the Future of Teaching and Learning. Office of Educational Technology, 2023.
