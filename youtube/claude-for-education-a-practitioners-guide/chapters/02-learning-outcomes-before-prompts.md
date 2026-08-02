# Chapter 2: Learning Outcomes Before Prompts
## Claude for Education: A Practitioner's Guide

---

## Classroom Problem

James teaches tenth-grade chemistry. On a Thursday afternoon, trying to get ahead of the weekend planning, he opens Claude and types:

*Give me a lesson on photosynthesis.*

He's teaching biology next unit. He needs something. Claude gives him something: a warm-up, a reading, a diagram description, some discussion questions, a formative check. It looks like a lesson. He saves it.

On Monday, the lesson happens. Students answer the discussion questions. Some can say that plants use sunlight to make food. Fewer can explain why a plant in a dark room would eventually die. Almost none can connect what they know about photosynthesis to why they need to eat — which is what James was trying to get to, because the next unit is cellular respiration and that connection is load-bearing.

The lesson wasn't wrong. It wasn't the lesson James needed. And he couldn't have known that from the prompt he wrote, because the prompt didn't say what he needed students to be able to do.

---

## Learning-Outcome Anchor

By the end of this chapter, you will be able to write a clear, assessable learning outcome before writing any Claude prompt; explain how backward design changes what Claude produces; and use an outcome-anchored prompt template to generate activities, examples, misconception lists, and formative checks that are aligned to a specific learning target rather than a general topic.

---

## Why Artifact-First Prompting Fails

The natural way to ask Claude for teaching help is to describe what you want the artifact to be: a lesson, a worksheet, a rubric, a set of examples. This is artifact-first prompting, and it has a structural problem.

Claude does not know what you want students to learn. It knows what you asked for. If you ask for a lesson on photosynthesis, Claude generates a lesson that covers photosynthesis. It covers it the way a general explanation would cover it — reasonably, somewhat completely, at a middle level of complexity. It does not know whether you want students to be able to explain the biochemical mechanism, or draw the light and dark reactions, or explain the ecological significance, or connect the concept to the energy cycle you're about to teach next week.

The artifact looks like it addresses the topic. Whether it addresses the learning target is a separate question, and artifact-first prompting never asks it.

This is not a critique of Claude. It is a description of what prompts can and cannot communicate. The gap between "lesson on photosynthesis" and "lesson that helps students explain why plants need sunlight using the concept of energy transformation" is enormous. Claude cannot close that gap without the information. The teacher has to supply it.

Wiggins and McTighe (2005) built the backward design framework around exactly this problem: curriculum planning that begins with activities or content rather than with the end in mind tends to produce coverage without learning. The three questions backward design asks — What should students know and be able to do? What would count as evidence? What learning experiences build toward that evidence? — must be answered in that order, not reversed. Claude is an activity generator. Left to itself, it will give you activities. Getting learning requires you to answer the first two questions before you ask Claude for the third.

---

## What a Learning Outcome Actually Is

A learning outcome is a statement of what students will be able to do, observable and assessable, by the end of a defined period of instruction.

The word "do" is load-bearing. Learning outcomes describe performance, not exposure. "Students will understand photosynthesis" is not a learning outcome — it describes a state, not a performance, and "understand" cannot be directly observed. "Students will explain the role of chlorophyll in capturing light energy using their own words" is a learning outcome — it describes a specific performance that can be observed and assessed.

Bloom's revised taxonomy (Anderson & Krathwohl, 2001) offers a catalog of cognitive performance verbs: remember, understand, apply, analyze, evaluate, create. Used well, these verbs help specify what kind of thinking the student must demonstrate. Used poorly — as a checklist where any Bloom verb counts as an outcome — they produce outcomes that sound specific but remain vague. "Analyze photosynthesis" is better than "understand photosynthesis," but it still doesn't say what students analyze, how, or to what standard.

A usable learning outcome has three components:

1. **A specific performance verb** that describes observable thinking or action
2. **The content or concept** the performance is applied to
3. **The level of specificity** that tells you what successful performance looks like

Example: *Students will explain why a plant in a dark room cannot sustain itself, connecting the role of light to the production of glucose and the plant's energy needs.*

That outcome tells Claude — and you — a great deal: the performance is an explanation, not recall; it involves making a connection, not listing; and it has a specific conceptual anchor (light → glucose → energy) that constrains what activities and examples will actually serve it.

Dee Fink's significant learning taxonomy (Fink, 2003) adds dimensions beyond cognitive performance: foundational knowledge, application, integration with other concepts, the human dimension, caring (why it matters), and how to keep learning. A chemistry teacher who wants students not just to recall the equation but to see why photosynthesis and respiration are mirror processes is reaching for Fink's integration dimension. That intention can be in a prompt, but only if the teacher names it.

---

## The Outcome-to-Prompt Sequence

Here is the method this chapter teaches. Before writing any Claude prompt, answer these five questions:

1. **What should students be able to DO by the end?** (Write an outcome with a performance verb.)
2. **What do students already know that connects to this?** (Prior knowledge anchor.)
3. **What misconception do students typically bring to this topic?** (The thing the lesson must address.)
4. **What would count as evidence that a student has learned this?** (Assessment anchor.)
5. **What constraints apply?** (Time, grade level, prior vocabulary, accessibility needs, materials available.)

Then write the Claude prompt using those answers.

---

## A Worked Teaching Walkthrough

**James's original prompt:**
> Give me a lesson on photosynthesis.

**James's outcome-anchored prompt:**
> I teach 10th-grade biology. My learning outcome is: Students will explain why a plant in a dark room cannot sustain itself, connecting the role of light to glucose production and the plant's energy needs. Students already know that animals need food for energy and that plants are different. A common misconception in this class is that plants get their food from the soil. I have 50 minutes. Evidence of learning: students can answer an explain-in-your-own-words question that makes the light-to-energy connection without being told the answer. Please draft a lesson sequence, including a warm-up that surfaces the soil misconception, two activities that build toward the connection, and a formative check aligned to my outcome.

The second prompt is longer. It is also entirely producible from knowledge James already has. Every piece of information in that prompt — the outcome, the prior knowledge, the misconception, the time, the assessment evidence — James knew before he opened Claude. He just hadn't written it down.

What Claude produces in response to the second prompt is not just better. It is aligned. The warm-up will surface the misconception James named because he named it. The activities will build toward the connection he specified because he specified it. The formative check will match his evidence definition because he included one. And when Claude produces something that doesn't fit, James can see exactly why — because he has a target to compare against.

**What teacher review still requires:** James must verify that (a) the misconception-surfacing activity actually draws out the soil misconception in the way students would voice it, (b) the sequence moves at a pace that works for his class, (c) the formative check question requires explanation, not just recall, and (d) the vocabulary used matches what students have been taught. Claude cannot know any of those things. James can.

---

## From Vague to Assessable: A Rewriting Exercise

Take these common vague instructional intentions and see what happens when they become outcomes:

| Vague Intention | Outcome with Performance Verb |
|---|---|
| "Cover the Civil War" | Students will compare the economic and moral arguments used by leaders on each side of the secession debate using primary source evidence |
| "Do something on fractions" | Students will explain why dividing by a fraction is equivalent to multiplying by its reciprocal using a visual model |
| "Introduce the water cycle" | Students will trace the path of a water molecule through at least three stages of the water cycle, explaining the energy change at each transition |
| "Teach essay structure" | Students will revise a paragraph so that it opens with a claim, supports it with two pieces of evidence, and explains how each piece supports the claim |

Each rewrite does three things: names a performance, specifies the content, and implies what "done" looks like. Each one also gives Claude dramatically more information to work with. And each one can only come from the teacher, because only the teacher knows which step in the sequence this lesson occupies and what students are capable of at this moment.

---

## Misconceptions as Design Input

One of the most powerful uses of the outcome-anchored prompt is naming a specific misconception. The Carnegie Mellon Eberly Center notes that misconceptions are persistent precisely because they are not random errors — they are logically coherent from the student's prior knowledge (CMU Eberly Center, learning objectives guidance). A lesson that covers the correct information without addressing the misconception may leave the misconception intact and add confusion on top of it.

Ambrose et al. (2010) call this the "inert knowledge" problem: students can hold correct information alongside contradicting misconceptions without the contradiction becoming apparent to them, because the new information was never forced into contact with the old.

Naming the misconception in a Claude prompt changes what it generates:

**Without misconception:**
> Draft activities for a lesson on fractions.

**With misconception:**
> Draft activities for a 6th-grade lesson on dividing fractions. Students consistently believe that dividing makes things smaller, so they resist the result when dividing by a fraction produces a larger number. I need one activity that forces this prediction into conflict and one that resolves it with a visual model.

The second prompt will produce activities that do instructional work the first prompt cannot produce, because the first prompt does not contain the problem. The teacher was the only person in the room who knew what the problem was.

---

## Generating Assessment Evidence Before Activities

Backward design asks teachers to design the assessment before the activities — to know what evidence of learning looks like before deciding what experiences will build toward it (Wiggins & McTighe, 2005). This principle transfers directly to Claude prompting.

A teacher who knows what assessment evidence looks like can ask Claude: *Given this learning outcome and this evidence task, what activities would help students develop the capability this evidence requires?*

That is a fundamentally different request from *Give me activities on [topic]*, and it produces fundamentally different output. Claude becomes an activity generator working backward from a specified endpoint, rather than a content generator working forward from a topic.

The Brookhart (2013) guidance on assessment alignment — that assessments should require the same cognitive performance as the learning outcome — maps directly here. If your outcome says "explain," your formative check should require explanation, not recall. If your outcome says "analyze," your exit ticket should not be a multiple-choice item that can be answered by recognition. Naming this in your Claude prompt is the teacher's job.

---

## The Outcome-Anchored Prompt Template

Use this template for any Claude request connected to lesson planning, activity design, or materials creation:

```
Context: [Grade level / subject / course]
Learning outcome: [What students will be able to DO, with performance verb]
Prior knowledge: [What students already know that connects to this]
Misconception: [What students typically believe incorrectly about this topic]
Assessment evidence: [What success looks like — how you'll know they learned it]
Constraints: [Time / reading level / accessibility / vocabulary / materials]
Request: [What you want Claude to produce]
```

This template is not a rigid formula. It is a checklist of information that makes a Claude prompt educationally useful. Not every prompt needs every element. A short brainstorm request might only need outcome and request. A full lesson plan request benefits from all six.

What the template enforces is the sequence: outcome comes before request. The learning target comes before the artifact.

---

## The Human Gate Questions for This Chapter

Before writing a Claude prompt for any lesson-related task:

1. Have I written a specific, assessable learning outcome?
2. Do I know what prior knowledge students bring to this?
3. Have I identified a likely misconception?
4. Do I know what evidence would show a student has learned this?
5. Are those answers in my prompt, or am I still asking for a lesson on a topic?

And after Claude produces output:

6. Does this activity require the performance my outcome names?
7. Does the formative check match my evidence definition?
8. What do I know about my students that Claude doesn't — and does this output account for it?

---

## Common Mistakes

**Writing outcomes that are actually topics.** "Students will learn about the Civil War" is a topic, not an outcome. Ask: what will they be able to do with this knowledge? "Students will compare the military strategies of Grant and Lee at a specific battle and explain which decisions were decisive" is an outcome.

**Using Bloom's verbs without specificity.** "Students will analyze the poem" sounds like an outcome. Analyze how? Looking for what? To what standard? "Students will identify two shifts in the speaker's emotional tone and explain what textual evidence signals each shift" is specific enough to guide both instruction and assessment.

**Writing the prompt before the outcome.** The most common mistake. Open Claude before writing the outcome, and you get an artifact-first prompt almost by reflex. Write the outcome first, even in a notes file or on paper, before you open Claude.

**Treating Claude's first response as final.** When the first response doesn't align with the outcome, iterate. Tell Claude what's missing: "This activity requires recall, but my outcome needs students to explain. Can you revise the activity so it requires explanation, not definition?" Claude can revise toward specificity when given specific feedback.

**Importing the prior lesson's outcome.** Each lesson is its own system. The outcome for Tuesday's lesson is not automatically the right outcome for Thursday's continuation. Check that each Claude prompt carries the outcome for the specific learning moment you are designing.

---

## Student-Learning Risk

The student-learning risk in this chapter is generic instruction: activities that are educationally reasonable in the abstract but do not target the specific gap in front of the class.

Generic instruction produces what Ambrose et al. (2010) describe as knowledge without transfer: students can answer the question on the worksheet but cannot use the concept in a new context. Generic activities do not help students build toward the performance named in the outcome because the activities were never designed around a specific outcome. They were designed around a topic.

The hidden cost is that it feels like teaching happened. Students were busy. The time was structured. Something was covered. The gap between coverage and learning is invisible at the lesson level and visible only when students are asked to perform — which is often too late to repair.

---

## Try This

**Exercise 1 — Outcome Rewrite.** Take three lesson topics from your current planning and rewrite each as an assessable learning outcome. Check each one: Is there a performance verb? Does it name what "done" looks like? Could you write a formative check question from this outcome without returning to the topic?

**Exercise 2 — Side-by-Side Prompt Comparison.** Choose one lesson you need to plan. Write two prompts: the artifact-first version you would have written naturally, and the outcome-anchored version using the template above. Send both to Claude. Compare the outputs: Which activities require the performance the outcome names? Which formative check questions are more aligned? What did the outcome-anchored prompt produce that the artifact-first version missed?

**Exercise 3 — Misconception Inclusion.** Choose a concept your students regularly misunderstand. Write the misconception explicitly. Now write two Claude prompts: one without the misconception, one with it. Compare what Claude generates. Does naming the misconception change what the lesson does?

---

## What Would Change My Mind

If studies of classroom AI use showed that teachers who prompt Claude without explicit outcomes produce lesson sequences that are as well-aligned to their stated learning goals as teachers who prompt with explicit outcomes — controlling for teacher experience and subject expertise — I would revise this chapter's central claim. That evidence does not currently exist. What does exist is a body of instructional design research consistently showing that planning from outcomes rather than from topics improves alignment between instruction and assessment (Wiggins & McTighe, 2005; Brookhart, 2013; Nilson, 2010). Extending that finding to AI-assisted planning is a reasonable inference, not a proven fact, and research in this specific area would sharpen the guidance.

---

## Still Puzzling

**How specific is specific enough?** The chapter argues for specific outcomes, but there is a real tension: outcomes that are too narrow can lead to instruction that is excessively scripted, leaving no room for the unexpected conversation that often produces the deepest learning. The right level of specificity probably depends on the complexity of the concept and the experience of the teacher. More research on how expert teachers calibrate this would be useful.

**Do outcome-anchored prompts work equally well across subjects?** The examples in this chapter draw heavily from science and humanities. Teachers in arts, physical education, and some vocational fields find that their most important learning targets are not easily expressed in performance verbs. Adapting the outcome-before-prompts method for tacit and embodied knowledge is an open problem.

---

## Bridge to Chapter 3

You now have two things: a taxonomy for classifying teaching tasks (Chapter 1) and a method for anchoring Claude requests in learning outcomes before you ask for artifacts (this chapter). The next question is structural: once you know the outcome and you're ready to write the prompt, what makes a Claude prompt work at an instructional level?

Chapter 3 — Prompting Claude Like an Instructional Designer — teaches the full structure of an educational brief: learner profile, prior knowledge, misconception, outcome, constraints, modality, assessment evidence, and tone. It is the craft layer that sits on top of the method layer this chapter built.

---

## Sources Used

- Ambrose, S. A., Bridges, M. W., DiPietro, M., Lovett, M. C., & Norman, M. K. (2010). *How Learning Works: Seven Research-Based Principles for Smart Teaching.* Jossey-Bass.
- Anderson, L. W., & Krathwohl, D. R. (Eds.). (2001). *A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Educational Objectives.* Longman.
- Anthropic. (2024). Introducing Claude for Education. https://www.anthropic.com/news/introducing-claude-for-education [verify — current as of writing]
- Anthropic. (2024). Claude documentation. https://docs.anthropic.com/ [verify — current as of writing]
- Brookhart, S. M. (2013). *How to Create and Use Rubrics for Formative Assessment and Grading.* ASCD.
- Carnegie Mellon University Eberly Center. Learning objectives. https://www.cmu.edu/teaching/designteach/design/learningobjectives.html
- Fink, L. D. (2003). *Creating Significant Learning Experiences: An Integrated Approach to Designing College Courses.* Jossey-Bass.
- Nilson, L. B. (2010). *Teaching at Its Best: A Research-Based Resource for College Instructors* (3rd ed.). Jossey-Bass.
- Wiggins, G., & McTighe, J. (2005). *Understanding by Design* (2nd ed.). ASCD.
