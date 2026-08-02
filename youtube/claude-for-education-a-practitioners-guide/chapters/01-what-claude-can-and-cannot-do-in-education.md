# Chapter 1: What Claude Can and Cannot Do in Education
## Claude for Education: A Practitioner's Guide

---

## Classroom Problem

It is 9:30 on a Sunday evening. Dana teaches eighth-grade English in a large suburban middle school. She has a stack of thirty-one argumentative essays due back Tuesday, a lesson plan for a new unit she hasn't started, and three students on IEPs whose materials she needs to differentiate by Friday. She opens Claude.

She types: *Help me grade these essays.*

This is the moment the book is designed for. Not the moment of first contact with an AI tool — Dana already uses Claude. The moment of not quite knowing where the line is. Which tasks can Claude actually help with? Which ones need her judgment even if Claude can produce an output? And which ones should she keep entirely to herself, not because the technology fails but because delegating them would compromise the teaching?

This chapter gives her the map.

---

## Learning-Outcome Anchor

By the end of this chapter you will be able to classify any teaching task into one of four categories: tasks Claude can assist directly, tasks Claude can draft but the teacher must review, tasks that should remain human judgment, and tasks governed by local policy. You will be able to explain the reasoning behind each classification, and you will recognize the student-learning risks that arise when the wrong category is applied.

---

## The Four-Task Taxonomy

The easiest mistake in using any AI tool is treating it as uniformly capable. Claude is genuinely strong in some teaching-adjacent tasks and genuinely weak in others. The weakness is not always obvious, because Claude produces fluent, confident-sounding output across the board.

The taxonomy below is not a judgment about Claude's intelligence. It is a map of where teacher judgment is necessary — and where the cost of skipping it is real.

### Category 1: Assist Directly

These are tasks where Claude can produce a usable output with light human review, because the stakes of a minor error are low and the teacher retains full editorial authority.

**Examples:**
- Generating five alternative practice problems for a concept already planned
- Drafting a list of common student misconceptions about a topic for the teacher to review
- Producing three different analogies for an abstract concept so the teacher can pick the one that fits the class
- Rewriting a passage at a lower reading level for a student who needs it
- Brainstorming discussion questions the teacher will curate
- Producing a first draft of a lesson warm-up activity
- Creating vocabulary definitions for the teacher to check

The key feature of this category: the teacher sees everything before students do, the stakes of an error in any single item are low, and the teacher's professional knowledge is the quality-control filter.

### Category 2: Draft With Review

These tasks benefit from Claude's drafting capability, but the output goes nowhere without teacher review that is substantive, not just glancing.

**Examples:**
- Rubrics — Claude can draft criteria and descriptors, but the teacher must check that the criteria actually reflect the learning outcome, that the descriptors distinguish levels meaningfully, and that the language matches what was taught
- Feedback on student work — Claude can draft formative feedback, but the teacher must verify it is calibrated to the specific student's history, does not overstep into doing the thinking for the student, and uses language that will land with this particular learner
- Lesson plans — Claude can generate a sequence, but the teacher must verify it aligns with standards, that the timing is realistic for this class, that prior knowledge assumptions are correct, and that the formative checks are actually going to show what students understand
- Unit pacing guides — useful as a first draft; the teacher knows what disruptions are coming and how this group actually moves through material
- Sample student responses or exemplars — Claude can produce them, but the teacher must judge whether they represent the actual range of student work in the course

The critical distinction for this category: "draft with review" is not "skim and approve." It means reading the output against specific professional knowledge — what do I know about my students, my standards, and my context that Claude did not have? Where does this draft assume something that isn't true?

### Category 3: Protect — Keep Human

These tasks produce outputs Claude can generate, but using those outputs in place of human judgment carries a serious risk to student learning, to the teacher-student relationship, or to assessment integrity.

**Final grading.** Claude can comment on work. Commenting and grading are not the same action. Grading is a judgment about the degree to which a student has met a defined standard, made by someone who knows the standard, knows the student, knows the context of the assignment, and takes responsibility for the decision. Lee Shulman's concept of pedagogical content knowledge — the integration of content expertise, knowledge of learners, and instructional reasoning (Shulman, 1987) — applies here. Grading requires all three. Claude has access to none of them.

**Care and advising decisions.** When a student discloses stress, a mental health concern, a family crisis, or academic difficulty with underlying causes, the teacher's response must be human. Claude can help a teacher think through how to have a difficult conversation, but it cannot make the relational judgment, and the student's disclosure should not be pasted into a third-party AI tool [see Chapter 9 on privacy].

**High-stakes accommodation decisions.** Claude is not a qualified professional for determining what accommodations a student needs. That is a legal and ethical determination made by specialists, documented in institutional records, and implemented by educators with training.

**Curriculum and standards alignment.** Claude does not reliably know your district's current adopted standards, your department's scope and sequence, or your school's approach to controversial topics. Treating Claude output as standards-aligned without checking is a professional risk.

**The meaning of assessments.** Grant Wiggins spent his career arguing that assessment only has meaning if it reflects genuine evidence of understanding (Wiggins, 1998). What counts as evidence of learning in your course, for your learning goals, is a judgment you must make. Claude can generate questions. Claude cannot decide whether those questions actually reveal understanding versus pattern-matching.

### Category 4: Policy-Dependent

Some tasks are not inherently off-limits but depend on your institution's policies, your students' ages, your jurisdiction, and the agreements your school has with software providers.

**Examples:**
- Putting student work into Claude — depends on FERPA-adjacent privacy policy, age of students, and your institution's data agreements [verify — current as of writing]
- Using Claude for student-facing tutoring — depends on your school's permitted AI tools, parent/guardian consent frameworks, and your district's digital equity commitments
- Using Claude-generated materials in student-facing settings — depends on your institution's disclosure expectations and copyright guidance
- Recording or summarizing student conversations in Claude — almost certainly off-limits; see Chapter 9

The FERPA guidance from the U.S. Department of Education establishes that student education records are protected and that sharing them with third parties without consent carries legal risk. What counts as an "education record" and what sharing threshold requires consent are institutional questions you must resolve with your administration before putting student-identifiable information into any AI system (U.S. Department of Education, FERPA guidance).

---

## A Worked Teaching Walkthrough: Sorting Dana's Tasks

Return to Dana on Sunday evening. Here is how the taxonomy applies to her three problems.

**Grading thirty-one essays.** This is Category 3, with a Category 2 option. Dana should not have Claude grade the essays — the final judgment is hers. She can, however, use Claude to help her draft feedback prompts for common patterns she notices, or to generate sentence-level examples of a particular criterion so she can compare student work against a concrete model. The cognitive labor of reading each essay and deciding what it shows belongs to her.

**Lesson plan for the new unit.** This is Category 2. Claude can draft a sequence. Dana should review it against her actual standards, her knowledge of where this class is coming from, the time she actually has, and what she knows about misconceptions this group tends to carry. A thirty-second draft is worth exactly as much work as she puts into the review.

**Differentiated materials for three IEP students.** This starts as Category 2 and shades toward Category 4. Claude can adapt a reading passage to a different level or generate scaffolded versions of a task. But Dana must know the specific goals of each student's IEP — Claude doesn't — and she should not paste identifying information about named students into Claude without knowing her institution's data policy.

---

## What Claude Gets Wrong in Education — Specifically

General AI cautions (hallucination, overconfidence) are real, but educators need to know the specific failure modes most likely to appear in teaching tasks.

**Overhelping students.** Claude's default is to be helpful — to answer the question asked. In tutoring or student-facing use, "answering the question" is often the wrong response pedagogically. The student needs to do the thinking. A tool calibrated for helpfulness will often short-circuit the productive struggle that learning requires. Anthropic has introduced Learning Mode as one mitigation [verify — current as of writing], but the design of student-facing Claude use still requires explicit attention from the teacher (Anthropic, 2024).

**Generic feedback.** Claude does not know the student. Feedback it drafts will tend toward the general: "strengthen your argument," "add more evidence," "clarify your thesis." These comments are often accurate and rarely useful. Useful feedback is specific, tied to the learning goal, calibrated to what this student needs to work on next, and delivered in a register the student can hear. Claude can draft feedback options — and an experienced teacher can revise them toward that specificity — but off-the-shelf Claude feedback is rarely ready to hand to a student.

**Hallucinated facts.** Claude can produce confident-sounding factual errors, especially in specialized domains, rapidly changing fields, and areas where its training data is sparse or contested. In a history class, this might mean an incorrect date or a misattributed quote. In a science class, it might mean an outdated fact presented as current. In a law or medicine course, it might mean a legal standard or clinical guideline that has changed. The NIST AI Risk Management Framework names this class of failure — AI systems producing plausible but incorrect outputs — as a primary risk requiring human oversight (NIST, 2023).

**Standards confusion.** Claude knows about educational standards in general terms. It does not reliably know your state's current adopted standards, your district's local modifications, or your school's interpretation. Asking Claude to "align to the Common Core" [verify — current as of writing] or "align to [state standard code]" will produce output that looks standards-aligned but may not be.

**Confidently wrong rubrics.** Rubric descriptors generated by Claude often sound precise but conflate levels or use criteria that are not actually distinguishable in student work. The descriptor "demonstrates basic understanding" and "demonstrates developing understanding" may be genuinely unmeasurable in a specific assignment. Teacher review of rubric language against actual student work is essential.

---

## The Human Gate Questions for This Chapter

Before using any Claude output in your teaching:

1. Which category does this task belong to — assist, draft-with-review, protect, or policy-dependent?
2. If draft-with-review: what specific professional knowledge must I apply to the review?
3. If protect: am I substituting Claude output for my judgment, or am I using Claude to support my thinking before I make the judgment?
4. If policy-dependent: have I confirmed my institution's current position on this task?
5. What is the student-learning risk if this output is wrong or generic?

---

## Common Mistakes

**Treating "draft-with-review" as "done."** The most frequent error: Claude produces a lesson plan or rubric, the teacher glances at it, it looks fine, and it goes into the course unchanged. Draft-with-review means the draft is the starting point, not the product.

**Using Category 1 framing to justify Category 2 tasks.** "I'll just check it quickly" is not a review of a rubric. A rubric requires checking each criterion against the learning outcome, each descriptor against the range of student work you have seen, and the overall structure against how you will actually use it in scoring.

**Putting student-identifiable information into Claude as a matter of routine.** Even with good intentions, this is a policy and legal question that varies by institution. Default to anonymizing or describing students in general terms unless you have confirmed your institution permits the use.

**Assuming Claude knows your context.** Claude knows a great deal about education in general. It knows nothing about your school, your class, this semester's dynamics, what happened in Tuesday's lesson, or which three students will struggle with the transition from concrete to abstract. Context is your expertise.

**Accepting confident output as accurate output.** Claude's fluency is not a signal of accuracy. Verify factual content in any domain where accuracy matters. Check citations — Claude can generate plausible-sounding fake citations. Do not cite a source Claude named without finding the source independently.

---

## Student-Learning Risk

The highest student-learning risk in this chapter is not using Claude badly. It is using it in ways that reduce what students have to do for themselves.

If Claude drafts feedback and the teacher sends it without adaptation, students receive generic comments that do not tell them what to do differently. If Claude generates examples and they go into the lesson without connecting to the specific misconception the class has, the examples don't actually address the confusion. If Claude writes the rubric and the teacher doesn't check whether it measures what was taught, students receive grades on criteria they were never actually taught to meet.

The student-learning risk is usually invisible at the surface. The artifact still looks like teaching.

---

## Try This

**Exercise 1 — Task Classification Practice.** Take the following ten teaching tasks and classify each as assist, draft-with-review, protect, or policy-dependent. Then compare your classifications with a colleague.

1. Generating five multiple-choice questions on the water cycle
2. Drafting final comments on senior capstone projects
3. Adapting a reading passage to a 6th-grade reading level
4. Writing individualized feedback on a student's draft essay
5. Determining whether a student qualifies for extended time
6. Building a first-draft lesson sequence for a two-week unit
7. Pasting three student essays (names included) for Claude to analyze themes
8. Generating discussion questions for a Socratic seminar
9. Deciding whether a student has met the standard for promotion
10. Drafting an email to a parent about a student's progress

**Exercise 2 — The Specific Review.** Take a rubric Claude generates for an assignment in your course. Before accepting it: (a) check each criterion against the learning outcome it is supposed to measure; (b) check each descriptor against student work you have seen — are the levels actually distinguishable? (c) note any criterion Claude included that was not in your original learning design. What did the review reveal?

---

## What Would Change My Mind

If Anthropic or a rigorous third party published peer-reviewed evidence that Claude-generated feedback, when used without teacher review, produced learning gains equivalent to teacher-authored feedback — and if that finding replicated across subject areas and student populations — I would revise the category placement of feedback drafting upward, toward a stronger assist role. The current evidence base for AI-generated feedback quality in real classrooms is thin, and the burden of proof should fall on the tool, not on skepticism of it.

Similarly, if institutions developed robust, tested technical controls that reliably enforced privacy protections for student data in AI systems, some policy-dependent tasks could move to assist or draft-with-review. The technical barriers and legal ambiguities make this a future possibility, not a current reality.

---

## Still Puzzling

Two questions this chapter cannot resolve:

**Where exactly is the line between "draft-with-review" and "protect" for formative feedback?** The taxonomy above places feedback in draft-with-review, but a strong case exists that feedback — particularly for struggling students, or feedback at high-stakes moments in a student's trajectory — should be protected. The answer probably depends on how substantive the teacher's review is and how well the teacher knows the student. This deserves more empirical research.

**How will the policy-dependent category evolve as institutions develop formal AI use policies?** Many schools are in the process of writing these policies now. Some will land in places that are more permissive than the conservative stance this book takes; others will be more restrictive. The framework here is designed to hold across that variation, but the specific guidance in Chapter 9 should be checked against your institution's current position.

---

## Bridge to Chapter 2

The taxonomy this chapter gives you tells you which tasks Claude can help with and where your judgment must stay. But it doesn't yet answer the deeper question: once you know Claude can help with a task, what does good Claude use for that task actually look like?

The answer begins with outcomes. Before you write any prompt, you need to know what students should be able to do by the end of whatever this lesson, unit, or activity is for. Chapter 2 teaches the practice of writing outcomes-first — starting from what students should learn before asking Claude for anything. That sequence turns the taxonomy from a classification system into an actual workflow.

---

## Sources Used

- Anthropic. (2024). Introducing Claude for Education. https://www.anthropic.com/news/introducing-claude-for-education [verify — current as of writing]
- Anthropic. (2024). Claude documentation. https://docs.anthropic.com/ [verify — current as of writing]
- NIST. (2023). *Artificial Intelligence Risk Management Framework (AI RMF 1.0).* National Institute of Standards and Technology.
- Shulman, L. S. (1987). Knowledge and teaching: Foundations of the new reform. *Harvard Educational Review, 57*(1), 1–22.
- U.S. Department of Education. (2023). *Artificial Intelligence and the Future of Teaching and Learning.*
- U.S. Department of Education. FERPA guidance. https://studentprivacy.ed.gov/
- UNESCO. (2023). *Guidance for Generative AI in Education and Research.*
- Wiggins, G. (1998). *Educative Assessment: Designing Assessments to Inform and Improve Student Performance.* Jossey-Bass.
