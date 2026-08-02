# Chapter 10 — Enrichment for AI

*The fluency trap, one more time — this time inside the textbook that warned you about it.*

---

Open the *ai-for-designers* draft. Chapter 7 — *The Cowork Draft Run*. Two LLM Exercises were proposed for the end of this chapter on different runs. Read both.

> **Exercise A.** *Ask Claude to explain the eight-section structure of a textbook chapter. Then ask Claude to draft a chapter using that structure for a topic of your choice. Read the output and identify three improvements you would make.*

> **Exercise B.** *Open your most recent client brief — the one with the most contested feedback. Paste it into Claude with this prompt: "Read this brief as a senior creative director would. Where is the client telling me what they want, and where are they telling me what they don't want? Quote the lines and explain." Then read Claude's answer next to your own read. List three places where Claude saw something you missed, three places where Claude misread the client's voice because the model has not worked with this client before, and one decision you will make differently on the next round of revisions.*

Exercise A is generic. It would work — unchanged — in a textbook on cooking, accounting, screenwriting, or veterinary medicine. The prompt is about how Claude responds to structure, not about how a freelance designer uses Claude inside a real client relationship.

Exercise B cannot transplant. It is built around a real brief the designer has, a real client whose voice the designer has calibrated, a real friction point in a real project. It assumes the *irreducibly human* layer — the designer's history with this client, the accumulated reads of past feedback, the sense of what the brief is not saying. Claude is used as a second reader whose *disagreements* with the designer are the data. An accountant has no client brief in this sense. An educator has no brief at all. The exercise is only useful for this domain, this reader, this career stage.

This is the fluency trap at the pedagogy scale. A textbook can be written entirely in Exercise A form. The exercises will look correct and read pedagogical. They will teach nothing the reader could not get from the Claude documentation, and they will hand the reader the habit of using LLMs the way a tourist uses a phrasebook — correctly, generically, without understanding what the words mean in context. The same shape that made a brand identity feel designed without being designed, and made a chapter feel authored without being authored, now makes an exercise feel domain-specific without being domain-specific.

You caught the verbal fluency trap in Chapter 1. The visual fluency trap arrived in Chapter 9. The pedagogical fluency trap arrives here. Same shape, different layer.

---

## The AI+1 standard — one test, stated precisely

The test is a single question:

> *Could this exercise appear in a different field's textbook unchanged? If yes, it fails.*

The "different field" is at the field level, not the sub-specialty level. A graphic-design exercise that transplants to product design might still pass — adjacent sub-specialties within design share enough workflow structure. A graphic-design exercise that transplants to accounting fails. The standard is set at the field boundary because that is where the *irreducibly human* layer lives: in the domain expertise the model cannot infer from training data because the data is private, embodied, relational, or local.

The deep-source argument is Paulo Freire's, from *Pedagogy of the Oppressed*.[^freire] Freire's critique of what he called the "banking model" — the teacher deposits content, the student stores and withdraws — is that it treats the learner as a container for transferable knowledge rather than as a domain-situated practitioner. A generic LLM exercise *is* a banking-model exercise.

bell hooks extended Freire in *Teaching to Transgress*, arguing that pedagogy must be *engaged* — must take the learner's specific context seriously as the precondition for competence, not as decoration around it.[^hooks] She made the commitment operational, not abstract: she chose the lowercase pen name to pull attention away from the author and toward the work, taking it from her maternal great-grandmother Bell Blair Hooks, and she taught at Yale, Oberlin, and the City College of New York before settling at Berea College in Kentucky — the last chosen precisely because Berea served Appalachian students who would not otherwise reach an elite education. Her line cuts directly at the difference between Exercise A and Exercise B above: pedagogy that does not take the learner's specific context seriously cannot produce competent practitioners. It produces *credentialed* ones. The AI+1 standard is engaged pedagogy translated into an exercise-design rule.

[^freire]: Freire, Paulo (1968; English trans. 1970). *Pedagogy of the Oppressed*. Continuum.
[^hooks]: hooks, bell (1994). *Teaching to Transgress*. Routledge.

There is empirical backing in the concept-inventory tradition. Eric Mazur's *Peer Instruction* research at Harvard demonstrated that students who pass traditional exams routinely fail at the application layer when the application is novel.[^mazur] A 2014 meta-analysis by Scott Freeman and colleagues pooled 225 studies and found the same gap at scale: passive instruction underperforms active, application-focused instruction across every science and engineering field measured.[^freeman] Generic LLM exercises produce the same failure pattern: students who complete them retain generic prompting habits and fail to apply LLMs to their own domain. The exercise has to test domain integration, not prompt syntax.

[^mazur]: Mazur, Eric (1997). *Peer Instruction: A User's Manual*. Prentice Hall.
[^freeman]: Freeman, S., et al. (2014). "Active learning increases student performance in science, engineering, and mathematics." *PNAS*, 111(23), 8410–8415.

There is also a bound on the standard. Apply it too aggressively and you produce hyper-specific exercises that no individual reader matches — designed for a branding designer who works with D2C fashion startups in Brooklyn during economic downturns. The standard is *field-distinguishing*, not *individual-distinguishing*. Graphic design as a whole. When the enrichment generator drifts toward hyper-specificity, edit back.

For any LLM Exercise in the book, three questions determine whether it passes.

First: could this appear in a different field's textbook unchanged? If yes — fails. Second: does it require the reader to bring something only they have — a real brief, portfolio, client, or remembered failure? If no — fails. Third: is the deliverable a judgment the reader produces, not just LLM output? If the deliverable is just "read Claude's answer" — fails.

An exercise that passes all three is doing AI+1 work. An exercise that fails any one is, on at least one axis, generic.

| Question | Pass condition | Fail signal | Common failure pattern |
|---|---|---|---|
| Could this appear in a different field's textbook unchanged? | The exercise breaks if you swap "graphic design" for "accounting" — it names a client brief, a portfolio, a Figma file. | The prompt reads cleanly in any field; "Ask Claude to explain the eight-section chapter structure" works for cooking or veterinary medicine alike. | Generic prompt-craft dressed as domain work — teaching how Claude responds to structure, not how a designer uses Claude. |
| Does it require the reader to bring something only they have? | The reader must supply a real brief, a real portfolio, a real client whose voice they have calibrated, or a remembered failure. | "Pick a topic of your choice" — nothing the reader owns is required; any input would do. | The exercise runs fine on invented or hypothetical material, so no irreducibly human layer is exercised. |
| Is the deliverable a judgment the reader produces, not just LLM output? | The reader writes the verdict — three places Claude missed, three it misread, one decision they will change. | The deliverable is "read Claude's answer" with nothing the reader is asked to author. | The artifact is the model's text, not the reader's analysis of it — consumption mistaken for assessment. |

![A horizontal chain of three decision gates with a passing arrow continuing rightward to a PASS terminal node, and each gate also draining downward to a single shared FAIL sink below.](images/10-enrichment-for-ai-fig-01.png)
*Figure 10.1 — The three-question audit scorecard*

---

## Two kinds of LLM-integrated content — and why mixing them breaks the chapter

The enrichment pipeline adds two kinds of material, and they are different in placement, purpose, and what they require of the reader. Mixing them is the most common failure the enrichment pass produces.

A **Dig Deeper** prompt is a short, copy-paste-ready prompt embedded in the chapter prose, at the moment it would be useful. It is offered as an optional rabbit hole — the reader can take it or skip it without losing the thread of the chapter. Two to four per chapter is typical. It has no enforced deliverable. The reader gets value from running the prompt; the textbook does not require an artifact. Example, mid-chapter in *ai-for-designers* Chapter 7:

> *Take one of your last three project briefs. Paste it into Claude with: "What is this client asking for in a way that does not name what they actually want?" Read the answer. You do not have to do anything with it. Notice whether Claude saw something you missed.*

An **LLM Exercise** sits at the end of the chapter, inside the assessable-exercises block, with the same Apply/Analyze/Evaluate Bloom's label as the other exercises. It is not optional. It produces a deliverable the reader will reference in a later chapter. One per chapter. Example, end of *ai-for-designers* Chapter 7:

> **(Apply.)** Take the brief you used in the Dig Deeper above. Paste it into Claude with the prompt: "Read this brief as a senior creative director would. Where is the client telling me what they want, and where are they telling me what they don't want? Quote the lines and explain." Save Claude's response. Write 250 words naming three places Claude saw something you missed, three places Claude misread the client because the model has no relationship history, and one revision decision you will make differently on the next round.

Same chapter. Same client brief. Different scaffolding. The Dig Deeper is permission-to-explore. The LLM Exercise is the assignment. The 250-word comparison from the Exercise becomes part of the *running project* — the cumulative artifact the reader builds across chapters — that the next chapter will reference.

![Two side-by-side panels against a shared horizontal attribute axis — left panel Dig Deeper, right panel LLM Exercise — with three aligned rows comparing placement, obligation, and output.](images/10-enrichment-for-ai-fig-02.png)
*Figure 10.2 — Dig Deeper vs LLM Exercise*

The failure mode: putting what should be an LLM Exercise inline as a Dig Deeper, or giving a Dig Deeper the formal structure of an Exercise. An LLM Exercise without an explicit "Save this. You will use it in Chapter X" belongs as a Dig Deeper. A Dig Deeper that says "write 250 words and submit them in your portfolio" belongs as an LLM Exercise. The distinction is structural, not just cosmetic — the scaffolding tells the reader what to keep and what to let go.

---

## Enrichment is a category — the LLM layer is one band

Everything so far has been about one form of enrichment: the LLM layer — the Dig Deeper prompts and the LLM Exercises that turn a textbook into an *AI+1* textbook. It is the most important form, and the rest of this chapter builds it in full. But it is not the only one, and treating it as the whole of enrichment is its own quiet version of the fluency trap — mistaking the part you can generate for the part that matters. Two other forms earn their place, and both are prompts in Appendix H.

The first is **deep-research enrichment**. A chapter drafted in May reads as current in May and stale by the following spring — a tool gets renamed, a ruling lands, a number moves. A deep-research prompt, run in Gemini's or ChatGPT's research mode (or Claude), takes a chapter and a field and comes back with what has changed, what new sources exist, and the specific places the chapter could be made more relevant to *this* topic and *this* reader. It is the standing answer to the aging-risk register: not the one-time fact-check of Chapter 12, but a recurring pass that keeps a living book alive.

The second is the **when-to-use / when-not-to-use-AI map**, and this one is the book's whole thesis turned into a deliverable. For a given field, where should a practitioner reach for AI, and where is reaching for it malpractice? The answer is not universal — it moves by subject. A radiologist and a family-court mediator draw the line in different places, for good reasons. The map names both sides for *your* field, with the reasoning attached, so the reader inherits a position rather than a vibe. It is the irreducibly-human taxonomy from Chapter 3, sharpened to the point of use.

The rest of this chapter builds the LLM-exercise layer in depth. The other two forms are prompts you run when the book needs them.

---

## The enrichment generator — three phases

The pipeline has a name: *"With LLMs" Series — Curriculum Enrichment Generator*. It runs in three phases and pauses for judgment between them. The generator prompts are reproduced in Appendix H.

**Phase one** detects the book's state. Three possibilities: flat chapters in `chapters/` (most readers of this book, by Chapter 10); source subfolders with multi-file chapter directories (the OpenStax-import pattern); or chapters that live elsewhere and need to be brought in. If you are in Phase one after completing Chapter 8, you are in the flat-chapters state. The generator proceeds.

**Phase two** generates Chapter 00: *Claude Basics for [your field]*. This is an onboarding chapter, customized to the book's domain, that introduces the reader to the LLM layer before the first domain chapter begins. It explains what Claude can and cannot do for this craft, when to use Claude versus a Claude Project versus Claude Code versus Cowork, and what Claude's field-specific failure modes look like. Without Chapter 00, the LLM Exercises read as a series of disconnected prompts. With it, they read as a curriculum that the reader enters understanding the vocabulary.

**Phase three** proposes three to five candidate *running projects* — the cumulative artifact the reader builds across chapters via LLM Exercises — and asks the author to pick one. Once the project is chosen, the generator runs across every chapter and inserts two to four Dig Deeper prompts inline and one LLM Exercise at chapter end. It updates the TOC and logs every insertion. The book becomes an AI+1 textbook at the pedagogy layer.

Two failure modes appear regularly in phase three. First: the generator produces a Dig Deeper that is too generic because the chapter prose did not give it enough domain hooks. If the chapter prose does not name specific tools, specific deliverables, or specific moments in the reader's workflow, the generator has nothing to attach to. The fix is to enrich the chapter prose before re-running the generator on that chapter. Second: the LLM Exercise does not advance the running project because the chapter covers a topic that does not cleanly connect. Either the running project was poorly chosen — pick a different one and regenerate — or the chapter needs a different end-of-chapter exercise that does not advance the project. A book does not need every chapter to feed the running project. Three-quarters is fine.

![A horizontal flow of three phase nodes connected by arrows, with small interrupt glyphs sitting on the arrows between phases to mark author-judgment pauses, ending in a terminal node.](images/10-enrichment-for-ai-fig-03.png)
*Figure 10.3 — The enrichment generator, three phases*

---

## Chapter 00 — what makes it AI+1

The generator produced a Chapter 00 for *ai-for-designers* that runs about 4,800 words. Four sections, each carrying the line between generic and domain-specific in a different register.

**What Claude can and cannot do for a freelance graphic designer.** The generic version: *"Claude is a large language model that can answer questions, generate text, and assist with creative tasks."* True. Useless. The AI+1 version: *"Claude can read a client brief and tell you what the brief is not saying. Claude can produce a logo concept brief that reads professional and is content-empty. Claude cannot tell you whether this particular client tends to backslide on color choices three weeks into a project. Claude can audit your portfolio site as an outside reader and surface positioning gaps. Claude cannot replace the taste-calibration conversation you had with your senior designer in your first year."* Every capability paired with a designer-specific workflow; every limitation named at the workflow-integration level, not the model level.

**When to use Claude vs. Claude Project vs. Claude Code vs. Cowork.** Four tools, each paired with a part of the freelance workflow: Claude in chat for brief reading and portfolio audits (roughly 80% of LLM use for this reader), Claude Project for ongoing client work where the conversation needs to remember the brand guide and past decisions (roughly 15%), Claude Code for asset-batching and design-system token reports (roughly 5%, high-leverage), Cowork for the book-building activity the reader is doing right now. A generic Chapter 00 would list capabilities. The AI+1 Chapter 00 names the workflows and estimates the distribution, because the reader needs a decision rule, not a feature list.

**Worked example: brief intake on a real client brief.** An anonymized real brief, pasted into Claude with the brief-intake prompt, annotated in three registers: three places Claude saw something the designer would have seen, three places Claude missed something the designer would have caught, and one place Claude *introduced* a constraint the brief did not state — which the designer caught and rejected. The last category is the one the generic version never shows. The model invents constraints. The designer must catch them. Showing this at production speed — not tutorial speed, not hypothetical-client speed — is the work Chapter 00 is doing.

**Claude's field-specific failure modes.** Five named failure modes, each paired with a specific tool and a specific workflow moment: the brief-summary trap (Claude summarizes and the summary obscures the contested terms — fix: ask Claude to *quote* the disputed lines), generative-fill overreach (Adobe Firefly is excellent at production, not at concepts), brand-system drift (Figma AI Make produces type weights and grid units that compound across the system), taste-calibration replacement (Midjourney variants surface only good variants, not the bad ones the designer needs to see), portfolio-positioning blindspot (Claude reads the portfolio but misses the meta-claim about the designer's positioning). Every failure mode names a specific tool, a specific workflow, a specific failure texture. The generic version would say "Claude can hallucinate." The AI+1 version says where, how, and what the designer does about it.

The line that divides AI+1 from generic at the Chapter 00 scale is the binding of the LLM behavior to the domain workflow. When that binding is tight, the chapter passes. When the binding is loose — when the chapter could be retitled "Claude Basics for Accountants" with a search-and-replace on field names — it fails.

---

## The AI Wayback Machine

The enrichment pipeline adds a fourth artifact after the LLM Exercises are in place: a short section in each chapter connecting its argument to a lesser-known historical figure whose work substantively bears on the chapter's claim. Three operating principles.

**Substantive connection only.** A figure included for representation but whose work does not connect to the chapter's argument fails the AI+1 standard at the figure-selection layer. A token figure is a tokenized chapter. If the connection from figure to argument is forced, drop the figure and find one whose work genuinely bears on the chapter.

**Diverse on multiple axes.** Gender, geography, era, discipline. The generator maintains a diversity tracker and reports at the end. Across a typical AI+1 book, the targets are at least one woman, at least one non-Western figure, no era or discipline in more than half the chapters. Sara Ahmed's framing in *Living a Feminist Life* is the operative one: representation done well is labor, not gesture.[^ahmed] The Wayback Machine is not a diversity-performance mechanism. It is a genuine intellectual labor that requires finding figures whose work actually connects, and that is harder and more valuable when the search is not restricted to the usual suspects.

[^ahmed]: Ahmed, Sara (2017). *Living a Feminist Life*. Duke University Press.

**Wikipedia instruction, not Wikipedia summary.** Every prompt directs the reader to a substantial Wikipedia entry. The Wiki Education program (wikiedu.org) uses the phrase: students read Wikipedia critically and produce something. The textbook is not summarizing Wikipedia. It is teaching the reader to use it. Every Wayback prompt should end with a follow-up move — verify a claim against a second source. Wikipedia is an excellent starting point and an inadequate ending point.

---

## The audit — catching the fluency trap after the fact

Once the enrichment pipeline has run, the AI+1 standard becomes an audit problem. The book now contains somewhere between twenty and sixty new LLM-integrated artifacts. Some of them passed the standard. Some did not. They will not be caught by reading them in order — they read fluently and pedagogically because they were generated by a fluent model. This is the same mechanism that made the pantry files look thorough and the Cowork drafts look authored. The audit that catches them is the same kind of move every previous chapter's evaluation pass was: pull the artifacts out of their context and read them against the standard.

The pattern: copy every LLM Exercise from every chapter into a single document, strip the chapter context, and read them in sequence as if you had never seen the book. Three failure patterns become visible that are invisible chapter by chapter.

The **interchangeable pattern**: two exercises that could swap chapter positions without losing anything. Diagnosis: at least one is generic. The **Claude-documentation pattern**: an exercise that teaches Claude itself — "try this prompt format and observe how Claude responds." Diagnosis: this is documentation, not pedagogy; it belongs in Chapter 00 if anywhere. The **no-deliverable pattern**: an exercise without a saved artifact. Diagnosis: this is a Dig Deeper in Exercise clothing; demote it.

When an exercise fails the audit, rewrite it by hand, not by re-running the enrichment generator. The generator produced the failure once; it is more likely than not to produce a similar failure on the second run. The rewrite is where you name the specific domain knowledge the exercise now requires the reader to bring. The acid test for a rewrite: can you state, in one sentence, why no generic prompt could have supplied the same outcome? If the answer is "the reader has to bring [the specific thing only they have]," the rewrite passes. If the answer is "the reader has to bring expertise" — that is not specific enough. Every exercise in every textbook requires expertise. The standard demands the specific thing.

| Pattern name | Diagnostic symptom | Diagnosis | Fix |
|---|---|---|---|
| Interchangeable | Two exercises could swap chapter positions without losing anything. | At least one is generic — neither is bound to the chapter's specific domain moment. | Rewrite by hand so each names the chapter-specific artifact only that chapter's reader would have. |
| Claude-documentation | The exercise teaches Claude itself — "try this prompt format and observe how Claude responds." | This is documentation, not pedagogy; it tests prompt syntax, not domain integration. | Move it to Chapter 00 if it belongs anywhere; replace the chapter-end slot with a domain-integration exercise. |
| No-deliverable | The exercise ends without a saved artifact the reader will reference later. | This is a Dig Deeper wearing Exercise clothing — permission-to-explore, not an assignment. | Demote it to an inline Dig Deeper, or add an explicit "Save this; you will use it in Chapter X" deliverable. |

![A blank ruled grid with one header band over three labeled pattern rows, each row marked by a distinct left-edge color swatch, and four empty columns reading left to right as a diagnostic-to-fix progression.](images/10-enrichment-for-ai-fig-04.png)
*Figure 10.4 — Audit pattern table*

---

The line that the standard tests against is not perfectly sharp, and it helps to admit that. "Field" here means what a working practitioner would name their profession to a stranger at a dinner party — graphic design versus accounting, not graphic design versus product design. That is a working definition, not a taxonomy; a more rigorous version might lean on occupation codes. And the whole framing rests on a moving target: when a future model can read a client relationship's history, calibrate taste, and surface unstated constraints — all the things this chapter names as irreducibly human in 2026 — the standard does not collapse, it relocates. There is always a current irreducibly human layer. Good pedagogy works at whatever that layer happens to be.

The enrichment layer is in: the exercises treat the reader as a domain expert rather than a generic AI user, useful in this field and no other. One craft remains before the book ships. The figure pipeline from Chapter 9 produced figures — but whether those figures *teach* is a separate question, and it is the one the next chapter answers.

---

## Sources

1. Freire, Paulo. (1968; English trans. 1970). *Pedagogy of the Oppressed*. Continuum.
2. hooks, bell. (1994). *Teaching to Transgress: Education as the Practice of Freedom*. Routledge.
3. Mazur, Eric. (1997). *Peer Instruction: A User's Manual*. Prentice Hall. https://mazur.harvard.edu/publications/peer-instruction-users-manual
4. Freeman, S., et al. (2014). "Active learning increases student performance in science, engineering, and mathematics." *PNAS*, 111(23), 8410–8415. https://www.pnas.org/doi/10.1073/pnas.1319030111
5. Ahmed, Sara. (2017). *Living a Feminist Life*. Duke University Press.
