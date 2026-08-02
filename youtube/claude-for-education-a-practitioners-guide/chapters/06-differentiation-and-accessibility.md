# Chapter 6 — Differentiation and Accessibility

---

## The Problem in the Room

A ninth-grade history teacher assigns a primary source document — a Civil War-era letter — to a class that includes four English-language learners at different proficiency stages, two students with individualized accommodation plans requiring simplified reading materials, a handful of students reading well below grade level, and three students who will finish the annotated reading exercise in ten minutes and spend the rest of the period staring at the ceiling.

One document. Seven different access problems. A planning period of forty minutes.

This is not an unusual classroom. It is the ordinary one. Differentiation — the practice of adapting content, process, products, or the learning environment to reach varied learners — has been a professional obligation since at least Carol Ann Tomlinson's foundational work on the subject. Universal Design for Learning, developed by CAST and expanded by Meyer, Rose, and Gordon, added the insight that barriers to learning are often embedded in the learning environment itself, not in the learner. The W3C's Web Content Accessibility Guidelines codified accessibility as a design standard, not an afterthought.

The theory is sound. The gap has always been execution at scale.

Claude does not solve the underlying complexity of differentiated learning. What it does is reduce the production labor — drafting alternate explanations, generating glossaries, writing extension prompts — so the teacher can spend time on the judgment that actually requires a human: deciding whether a given support serves a given student, whether the intellectual target has been preserved, and whether the student is being helped or condescended to.

---

## What This Chapter Lets You Do

By the end of this chapter, you will be able to:

- Use Claude to generate reading-level adaptations that preserve the conceptual target
- Draft multilingual scaffolds and glossaries with appropriate verification steps
- Build UDL-aligned choice boards and alternative format options
- Create extension tasks for advanced learners without separating them from the shared learning goal
- Apply a five-question audit to any Claude-generated adaptation before using it

---

## Core Concepts

**Differentiation** changes how students access content, how they engage with it, and how they demonstrate learning — without changing what the learning is for. Tomlinson's framework distinguishes differentiation by readiness, interest, and learning profile. The key constraint is that scaffolding should reduce barriers to the goal, not replace the goal.

**Accessibility** has both a legal dimension — formal accommodations under disability law — and an instructional dimension. This chapter works in the instructional dimension: practical steps to reduce unnecessary barriers in materials. Formal accommodations are set by institutional processes, not by Claude. If a student has a documented accommodation plan, that plan governs. Claude-generated adaptations are instructional supports, not legal substitutes for accommodation.

**Universal Design for Learning** proposes designing materials that can work for varied learners from the start: multiple means of representation, multiple means of action and expression, and multiple means of engagement (CAST). The practical effect for this chapter is that a well-designed adaptation is not charity for struggling students — it is better design for everyone.

**The intellectual target** is the thing you are not negotiating away. A reading-level adaptation changes vocabulary and sentence structure. It does not change the conceptual demand, the historical argument, or the analytic work the student must do. When Claude collapses the thinking into the scaffolding — when the annotation exercise becomes so guided that the student only needs to copy — the adaptation has failed, even if the student completes it.

---

## Worked Walkthrough: Three Adaptations from One Prompt

### The starting material

A history teacher has this document-analysis assignment for a grade 9 class:

> Read the attached excerpt from a letter written by a Confederate soldier in 1862. Identify the author's reasons for fighting. What does the language he uses reveal about his values and assumptions? Write three annotated claims supported by direct evidence from the text.

The teacher wants three versions: one for students reading 2–3 grade levels below, one for English-language learners at an intermediate proficiency stage, and one extension version for students ready for a more complex challenge.

### Step 1: Give Claude the target outcome first

Before asking for adaptations, the teacher writes the learning outcome explicitly:

> Students will analyze a primary source document by identifying an author's claims, values, and assumptions, and by supporting their analysis with textual evidence.

This outcome anchors the request. The difficulty of the task is in the analysis, not in the length of the sentences.

### Step 2: Request the plain-language version

**Prompt:**

> I am adapting this assignment for students reading at a 6th-grade level. I want to preserve the full analytic task: identify reasons, analyze language, support claims with evidence. Please rewrite the instructions in simpler language without reducing the intellectual demand. Do not do the analysis for the student. Flag any place where you think the simplification might be losing something important.

**Claude's response (abridged):**

> Here is a plain-language version of the instructions:
>
> Read the letter from a Confederate soldier written during the Civil War in 1862.
>
> As you read, look for three things:
> - Why does the soldier say he is fighting?
> - What words does he use? What do those words tell you about what he believes?
> - What does he seem to take for granted — things he thinks are obviously true?
>
> After reading, write three paragraphs. In each one: make a claim, quote the exact words from the letter that support it, and explain what those words show about the soldier's thinking.
>
> Flag: The phrase "assumptions" may still need defining for some students. Consider adding a sentence like: "An assumption is something a person believes without saying it directly."

Notice what happened. Claude simplified the vocabulary, restructured the instructions into steps, and flagged a residual term. It did not do the annotation for the student. The teacher now decides whether the flagged suggestion is correct.

### Step 3: Request the multilingual scaffold

**Prompt:**

> Now create a version for English-language learners at an intermediate proficiency level. Include a short glossary of key academic vocabulary terms (5–7 terms). Use sentence stems to support annotation without giving the answer. Keep the analytical task intact.

**Claude's response (abridged):**

> Key vocabulary:
> - **primary source**: a document written by someone who was actually there, at the time it happened
> - **claim**: a statement that something is true, supported by evidence
> - **evidence**: specific words or details from the text that back up your claim
> - **assumption**: something a person believes is true without explaining why
> - **values**: the beliefs and principles that matter most to a person
>
> Sentence stems for annotation:
> - "The soldier says ___ because ___."
> - "The words '___ ' show that the soldier believes ___."
> - "I think the soldier assumes ___, because he writes ___."
>
> [Instructions continue in simplified form with glossary embedded.]

**Teacher's verification step:** The teacher checks whether the glossary definitions are accurate (they are), whether the sentence stems foreclose the analysis (they do not — they cue structure, not content), and whether any translation is needed for specific student language backgrounds. For that last step, Claude can assist, but the teacher who knows the student verifies. [verify — current as of writing: Claude's translation quality varies by language; always have a bilingual colleague or community member check high-stakes translations]

### Step 4: Request the extension version

**Prompt:**

> Create an extension version for students who are ready for additional challenge. Maintain the same learning outcome but add a layer of historical contextualization. The student should move from analyzing one letter to analyzing what a letter like this suggests about how ordinary soldiers understood the war's meaning. Do not add busywork — add depth.

**Claude's response (abridged):**

> Extension task:
>
> Complete the standard annotation exercise. Then write a fourth paragraph that addresses this question: If many Confederate soldiers held views similar to this author's, what does that suggest about how ordinary soldiers understood what they were fighting for? How does this complicate or confirm what your textbook says about the causes of the Civil War?
>
> You may use the letter and your class notes. You should also identify one assumption the soldier seems unaware he is making.

The teacher reviews this for historical accuracy — does it ask something fair to answer with available materials? Is "complicate or confirm" too vague? She tightens the question. Claude drafted it; she finished it.

---

## The Human Gate

Every Claude-generated adaptation requires a review before use. The five-question audit:

1. **Is the learning target preserved?** The intellectual demand may be accessed differently, but it should not be removed.

2. **Is the support matched to an actual barrier?** A simplified vocabulary list for a student who reads fluently but needs content extension is mismatched support. Ambrose et al. note that motivation, prior knowledge, and practice structure are all part of what determines whether a student can succeed (Ambrose et al., *How Learning Works*).

3. **Does any part of the adaptation do the student's thinking for them?** Sentence stems that point to the answer, glossary entries that contain the analysis, or scaffolds so tight that completion requires no student judgment — these undermine the learning.

4. **Is the student's dignity protected?** A student with a reading accommodation does not need a version that looks different from the class's materials in a way that marks them. Consider whether adaptations can be offered as choices available to all students.

5. **Does this accommodation touch anything that requires institutional process?** If a student has a formal accommodation plan, that plan governs. Check with your institution's disability services office before substituting Claude-generated supports for documented accommodations. [verify — current as of writing: policies vary by institution and jurisdiction]

---

## Common Mistakes

**Lowering the floor instead of reducing barriers.** The assignment becomes simpler, not more accessible. The student with the adapted version does less intellectual work and leaves the class having learned less. This is the most consequential mistake and the hardest to detect because the student appears to have completed the task.

**Treating differentiation as deficit labeling.** Adaptations should support learners, not announce their limitations. Framing a plain-language version as "the easy version" is not neutral. Consider how materials are distributed and named.

**Accepting Claude's multilingual output without verification.** Claude can generate text in many languages. That does not mean the text is accurate, idiomatic, or appropriately pitched. The U.S. government's Plain Language guidance emphasizes that clarity must be verified by the intended reader, not just by the writer. For multilingual supports, always verify with a speaker of the target language who understands the educational context.

**Using extension tasks as busy work.** More questions, longer responses, and additional readings are not automatically deeper. Depth comes from the kind of thinking required, not the quantity of output.

**Skipping the audit.** The five-question review takes four minutes. Skipping it means distributing materials you have not actually examined.

---

## Try This

**Exercise 1 (Immediate — single assignment):** Take one assignment you use regularly that has a reading-heavy component. Write the learning outcome in one sentence. Give Claude the assignment text and the outcome, then request a plain-language adaptation with this instruction: "Preserve the intellectual task. Flag anywhere the simplification may reduce rigor." Run the result through the five-question audit before deciding whether to use it.

**Exercise 2 (Classroom-applicable — UDL choice board):** Choose one unit topic you teach. Ask Claude to draft a UDL choice board: three ways students could represent their understanding of the core concept. Include at least one option that does not require extended writing. Review the options: do all three paths lead to evidence of the same learning outcome? Revise any that drift. Use the board with students and note which options they choose and what that tells you about their access needs.

**Exercise 3 (Multilingual scaffold):** If you have English-language learners in your class, take one set of academic vocabulary terms from your current unit. Ask Claude to write plain-English definitions and example sentences. Have a bilingual colleague or community member review the definitions before distributing them. Compare what Claude produced with what the reviewer changed — that gap is your verification lesson.

---

## What Would Change My Mind

This chapter argues that Claude is a useful production tool for differentiated materials as long as teacher review guards the intellectual target. That view would be weakened by evidence that:

- AI-generated adaptations systematically lower rigor in ways teachers do not catch in review — that is, that the human gate reliably fails
- Students given AI-generated scaffolds show worse retention than students given no scaffold, suggesting that the supports substitute for productive struggle rather than removing access barriers
- Teachers systematically use Claude-generated materials for formal accommodations without institutional process, creating compliance and equity risk

If that evidence emerged, the chapter's advice would shift toward more restricted use and more explicit warnings. The current argument is not that Claude's output is reliable — it requires review — but that the production assistance is worth the review effort. That trade-off is the thing to watch.

---

## Still Puzzling

**The accuracy problem in multilingual support.** Claude can produce text in dozens of languages, but the variation in quality across languages is large and not easy for a monolingual teacher to assess. The guidance here — verify with a speaker — is correct but sometimes unavailable. What institutional infrastructure would make this verification routine rather than exceptional?

**The distinction between scaffolding and accommodation at scale.** This chapter treats Claude-generated supports as instructional scaffolds, not formal accommodations. But in classrooms where formal processes are slow or inaccessible, teachers may use informal scaffolds to fill a gap. That practice has equity implications that are not fully resolved here.

**Whether UDL choice boards increase equity or complexity.** Offering multiple paths sounds like good design, but if the paths are not genuinely equivalent in rigor, or if some students consistently gravitate toward lower-demand options, the design may reproduce the inequity it means to address.

---

## Bridge

Differentiation changes how students access learning. Chapter 7 turns to a related question: how do students know what quality looks like? Rubrics, exemplars, and clear criteria help every student — not just those with access barriers — understand what they are being asked to produce and how their work will be judged. Claude can help draft those criteria, but the same principle applies: the teacher owns what quality means.

---

## Sources Used

- CAST, Universal Design for Learning guidelines
- W3C, Web Content Accessibility Guidelines
- Tomlinson, Carol Ann. Differentiated instruction
- Meyer, Anne, David H. Rose, and David Gordon. UDL foundations
- Ambrose, Susan A., et al. *How Learning Works*
- Anthropic Claude documentation. https://docs.anthropic.com/
- U.S. Department of Education, accessibility guidance
- UNESCO, inclusive education resources
- U.S. government Plain Language guidance
- NIST AI Risk Management Framework
