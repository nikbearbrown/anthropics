# Chapter 7 — Rubrics, Exemplars, and Criteria

---

## The Problem in the Rubric

A student submits an essay and receives a grade of B+ with the rubric notation: "Analysis: Good. Demonstrates strong analytical thinking with minor areas for development."

The student reads this and learns nothing specific. "Strong analytical thinking" is not observable. "Minor areas for development" names a gap without locating it. The rubric has done what Susan Brookhart describes as one of the most common rubric failures: it describes performance levels in terms of quality words — good, excellent, adequate — rather than in terms of what is observable in the work (Brookhart, rubric design and formative assessment).

Now the student is writing the next essay with no clearer sense of what analysis means in this course than they had before.

Rubrics are supposed to solve a transparency problem: students should know in advance what they are being asked to produce and how their work will be judged. But a rubric written in vague language does not create transparency — it just moves the opacity earlier in the process. Students encounter the same fog when they try to read the rubric that they encounter when they try to interpret a grade.

Claude is good at several rubric-adjacent tasks: converting vague quality words into observable criteria, generating common-failure examples that show students what "adequate" actually looks like in a piece of work, drafting student-facing checklists from complex analytic rubrics, and proposing performance level descriptions that distinguish between levels without rewarding the wrong things. What Claude cannot do is decide what quality means in this course, for these students, on this assignment. That judgment belongs to the teacher.

---

## What This Chapter Lets You Do

By the end of this chapter, you will be able to:

- Identify vague language in rubrics and convert it into observable criteria with Claude's help
- Draft analytic and single-point rubrics with Claude, then audit them before use
- Generate common-failure exemplars that show students what to avoid
- Create student-facing checklists from complex rubrics
- Apply a six-question rubric audit before distributing any Claude-drafted assessment tool

---

## Core Concepts

**A rubric** is a scoring guide that lists criteria and describes performance levels. The two most common forms are analytic rubrics (separate criteria scored independently, then summed) and single-point rubrics (one column describes the target quality; the teacher notes what is missing or exceeds it). Heidi Andrade's research on rubric use shows that rubrics improve student performance when students use them before and during work, not only after it (Andrade, rubric research).

**Criteria** are the dimensions of quality you are actually judging: what counts as evidence, how claims are structured, how evidence is used, what form the product takes. Criteria that are worth having are observable — a reader of the student work and a reader of the rubric can agree on whether the criterion is met.

**Performance levels** describe how well the criterion is met across a range: exemplary, proficient, developing, not yet. The failure mode Brookhart identifies is describing levels with adjectives that assume the judgment rather than enabling it. "Excellent analysis" does not describe; it endorses. "The essay identifies three or more specific textual examples and connects each to a stated claim about the author's purpose" describes.

**Exemplars** are samples of work that illustrate a performance level. Royce Sadler's work on standards and formative assessment emphasizes that students learn to recognize quality partly through exposure to examples, not only through rubric text (Sadler, standards and formative assessment). A well-chosen exemplar makes the abstract criterion concrete. Claude can generate artificial exemplars — examples it constructs to illustrate a level — but these require teacher review and should be labeled as constructed, not passed off as authentic student work.

**Assessment transparency** — what Grant Wiggins called making the criteria visible and the game worth playing — is the pedagogical purpose behind rubrics and exemplars (Wiggins and McTighe, assessment evidence). When students know what quality looks like before they start working, they can use that knowledge to guide their own practice. When criteria are opaque or withheld until after the submission, assessment becomes a guessing game about what the teacher values.

---

## Worked Walkthrough: From Vague Rubric to Observable Criteria

### The starting rubric

A university writing instructor uses this rubric for argumentative essays:

| Criterion | Excellent | Good | Adequate | Unsatisfactory |
|---|---|---|---|---|
| Argument | Strong, clear argument | Good argument with some issues | Argument present but unclear | No clear argument |
| Evidence | Excellent use of evidence | Good evidence | Some evidence used | Little or no evidence |
| Analysis | Demonstrates sophisticated analysis | Good analysis | Basic analysis | No analysis evident |

This rubric has four criteria. All four use quality words to describe quality. A student who receives "Good" in Analysis knows they are not in the top band and not in the bottom band. They do not know what they need to do differently.

### Step 1: Audit the rubric for vague language

**Prompt:**

> Here is a rubric for argumentative essays. Identify the vague language — places where the description assumes the judgment rather than enabling it. List what is observable versus what is just a quality word. Do not revise yet.

**Claude's response (abridged):**

> Vague language in the rubric:
> - "Strong," "good," "basic," "sophisticated," "clear" — all quality words; none describes what you would observe in the work
> - "Good argument with some issues" — which issues? What distinguishes this from "Excellent"?
> - "Demonstrates sophisticated analysis" — what does sophisticated analysis look like in an essay? What is the observable behavior?
>
> What would be observable:
> - Whether the thesis is stated explicitly and its position identifiable
> - Whether evidence is quoted or paraphrased with attribution
> - Whether each paragraph connects evidence to the central claim
> - Whether the essay addresses a counterargument
> - Whether the analysis explains rather than restates the evidence

This output is a working tool, not a finished rubric. The teacher looks at the list and makes decisions: does this course require explicit counterargument? Is paraphrase-with-attribution what the assignment asks for, or does it require primary sources?

### Step 2: Request observable performance level descriptions

**Prompt:**

> Using the "Analysis" criterion as the test case, write four performance level descriptions that describe observable qualities in the work rather than quality words. The assignment is a 5-paragraph argumentative essay for a first-year writing course. Criterion: the student explains how the evidence supports the claim.

**Claude's response:**

> **Analysis — Observable performance level descriptions:**
>
> **Exemplary:** Each body paragraph connects at least one piece of evidence directly to the paragraph's claim and to the essay's central argument. The explanation does more than restate the quotation — it interprets the evidence and identifies what it shows about the issue.
>
> **Proficient:** Most body paragraphs connect evidence to the paragraph's claim. Some interpretation is present, though a few passages restate the evidence without extending it.
>
> **Developing:** Evidence is present in most paragraphs but is not consistently connected to a claim. The analysis tends to summarize or paraphrase the source rather than interpret it.
>
> **Not yet:** Paragraphs include quotations or summaries without connecting them to an argument. The reader cannot tell why the evidence was included.

The teacher reviews this. The description of "Exemplary" assumes students know what "interprets" means — that may need a glossary or in-class example. The "Developing" level correctly distinguishes summary from analysis. She adjusts the "Not yet" description to be less punitive in tone. Claude drafted; she finished.

### Step 3: Generate a common-failure exemplar

**Prompt:**

> Write a short paragraph (3–5 sentences) that would score at the "Developing" level on the Analysis criterion. The topic is the essay's argument about social media and adolescent mental health. The paragraph should include evidence but fail to interpret it — it should summarize rather than analyze. Label it clearly as a constructed example for instructional use.

**Claude's response:**

> **Constructed example — Developing level (instructional use only, not authentic student work):**
>
> Studies show that adolescent social media use is linked to higher rates of anxiety and depression. A 2023 survey found that teenagers who spent more than three hours per day on social media were significantly more likely to report feeling anxious. Social media is therefore bad for adolescent mental health. This suggests that platforms should be more regulated.
>
> Note: This paragraph includes evidence but does not explain how the survey finding supports the specific argument being made. It moves from data to conclusion without interpreting what the data shows about the mechanism. That is the "Developing" pattern this example is meant to illustrate.

The teacher verifies that the example correctly illustrates the target failure. She also checks whether the claim in the exemplar is reasonable (not offensive, not misleading), and whether the source reference, though constructed, resembles what students actually cite in this class. She labels it clearly in the materials she distributes.

---

## The Human Gate

The six-question rubric audit, applied before distributing any Claude-drafted rubric or exemplar:

1. **Are criteria observable?** A reviewer of the student work and a reader of the rubric should be able to agree on whether the criterion is met — without additional interpretation from the teacher.

2. **Are performance levels distinct?** Could a student's work sit plausibly in two adjacent levels? If yes, the level descriptions overlap. Tighten them.

3. **Is the rubric aligned to the outcome?** Does each criterion measure something you said students would learn? A rubric can grow criteria that were never part of the learning goal.

4. **Are exemplars labeled and reviewed?** AI-generated exemplars must be identified as constructed. Students should know the example is illustrative, not authentic. If you use authentic student exemplars, you need student permission.

5. **Is student language clear?** A rubric written for your own grading logic may not work as a student-facing tool. Test it: give it to a student (or a colleague unfamiliar with the assignment) and ask whether they could use it to self-assess before submission.

6. **Does grading judgment remain human?** The rubric is a tool for making your judgment legible, not a replacement for judgment. Nilson's work on teaching and assessment emphasizes that rubrics support the teacher's evaluative thinking — they do not substitute for it (Nilson, teaching and assessment).

---

## Common Mistakes

**Accepting Claude's quality words.** If you ask Claude to write performance level descriptions and do not specify that they must be observable, Claude will often produce the same adjective-chain problem the original rubric had. The prompt must specify: no quality words, observable behaviors only.

**Using AI-generated exemplars without review.** Claude's constructed examples may contain factual errors, misrepresent the assignment, or model a failure in a way that is unclear. Review every exemplar before distributing it. The research on exemplar-based learning is clear that a poorly chosen exemplar can encode the wrong target in the student's mind (Sadler, standards and formative assessment).

**Building rubrics before defining the outcome.** Rubrics should follow from what you decided students should learn, not precede it. If you ask Claude to generate a rubric before you have a clear learning outcome, you will get a rubric that fits a generic version of the assignment type rather than your specific course.

**Letting the rubric expand beyond what you actually grade.** Claude may generate five or six criteria for an assignment that really only requires three. More criteria is not more transparency — it is more noise. Trim.

**Failing to share the rubric before the assignment.** A rubric that students see only after submission is a grading key, not a learning tool. Andrade's research consistently shows the learning benefit comes from students using rubrics before and during work (Andrade, rubric research).

---

## Try This

**Exercise 1 (Immediate — rubric audit):** Take a rubric you currently use. Run it through the six-question audit above. Identify the two most vague performance level descriptions. Write a prompt asking Claude to convert those descriptions into observable terms for your assignment type. Review Claude's output and make the final edit yourself.

**Exercise 2 (Classroom-applicable — single-point rubric):** Choose one assignment. Ask Claude to draft a single-point rubric: one column describing the target quality, with space for the teacher to note what is missing or exceeds it. Ask Claude to write the target description using only observable behaviors. Test the rubric by trying to apply it to one sample of student work you already have. Does it work? What needs adjustment?

**Exercise 3 (Exemplar generation):** Take one criterion from a rubric you use. Ask Claude to write two exemplar paragraphs: one at the target level, one at the "developing" level. Label both as constructed examples. Use them as an in-class exercise: give students both paragraphs and ask them to identify which one meets the criterion and explain why. What their explanation reveals about their understanding of the criterion is data you cannot get from a rubric alone.

---

## What Would Change My Mind

This chapter argues that Claude is useful for rubric drafting and exemplar generation, provided the teacher applies the six-question audit and makes all final editorial decisions. That argument would be weakened by evidence that:

- Teachers who use Claude-drafted rubrics are less likely to revise them than teachers who draft rubrics themselves — that the production ease reduces critical examination
- Claude-generated exemplars introduce systematic errors or biases that are difficult to detect without domain expertise
- Students who receive Claude-drafted rubrics show no improvement in self-regulation or performance compared to students who receive vague criteria, suggesting the precision is cosmetic rather than functional

The chapter's claim is practical: Claude can save rubric-drafting time and improve criterion clarity, with teacher review. If the review reliably fails to catch problems, the calculation changes.

---

## Still Puzzling

**Rubric bias.** Rubrics make criteria visible, but they do not make the choice of criteria neutral. A rubric that values thesis-driven argument over exploratory or dialogic writing encodes a particular discourse norm. Claude will reflect whatever criteria the teacher supplies. This chapter does not address rubric bias systematically — that would require a chapter of its own. The audit question "aligned to outcome?" is a start, but it does not ask whether the outcome reflects whose ways of knowing.

**AI-generated exemplar disclosure.** If a teacher uses a Claude-drafted exemplar in class without disclosing that it is AI-generated, what does that model for students about attribution and authorship? The chapter says: label it. But the field does not yet have a standard for what disclosure looks like in instructional exemplars.

**Whether rubrics help all students equally.** The research on rubric benefit (Andrade) is robust, but it is not uniformly distributed across student populations. Students who already operate fluently in the expected discourse benefit more readily from criteria stated in that discourse. Students who are learning academic register may find even well-written rubrics opaque without additional exemplar work.

---

## Bridge

Rubrics clarify what quality looks like when students are working. Chapter 8 takes up the harder question that AI forces on every teacher: when a student can use Claude to produce the artifact the rubric describes, does the rubric still measure learning? Assessment in the age of Claude requires looking beyond the artifact to the thinking that should have produced it.

---

## Sources Used

- Brookhart, Susan M. Rubric design and formative assessment
- Andrade, Heidi. Rubric research and student self-assessment
- Sadler, D. Royce. Standards and formative assessment
- Wiggins, Grant, and Jay McTighe. Assessment evidence (*Understanding by Design*)
- Ambrose, Susan A., et al. *How Learning Works*
- Anthropic Claude documentation. https://docs.anthropic.com/
- UNESCO, generative AI guidance
- U.S. Department of Education, AI report
- Nilson, Linda B. Teaching and assessment
- NIST AI Risk Management Framework
