# Chapter 4 — Tic TOC: Generating Your TIKTOC.md

*What you produce in two hours determines what two months of drafting produces.*

---

There is one question inside the Tic TOC intake phase that stops most authors cold. It appears somewhere in the first fifteen minutes, and it is not complicated. It is this:

> *In one sentence — not a paragraph — what does the reader LEARN?*

Try to answer it. Right now, for your own book, before reading further.

If you answered in under thirty seconds with a sentence that names something a reader can *do* — a specific capability they do not have before the book and have after — you are in a small minority. Most authors discover, at this question, that they do not yet know what their book is. They have a topic. They have an outline. They have a strong conviction that they have something to say. They have not compressed it into one demonstrable outcome, and the act of compression turns out to be the hardest cognitive work in the entire pipeline.

Here is what the discovery looks like in practice. The author types a draft: *"The reader learns how to use AI in their design practice."* Reads it back. Deletes it. Tries again. After five attempts, the draft still reads like a topic restated as a sentence, because that is exactly what it is.

Tic TOC will not let it stand. The response will come back as something like: *"That is a topic. A learning outcome names what the reader can do after the book that they cannot do before. 'Use AI' is a category. What specific capability? 'Defend an AI-assisted brand identity to a skeptical client without losing the account'? 'Triage AI-generated moodboards into a workable presentation in ninety minutes'? Pick the one that, if your reader masters it, justifies the book."*

Now it is harder. Now the author has to *choose* — to commit to one capability and let the others go. The book they were going to write was about everything AI-related in their field. The book Tic TOC is about to help them build is about one specific thing the reader cannot do today and can do at the end.

That commitment is not a constraint on the book. It is the book.

You will spend roughly two hours in Tic TOC. Most of that time will be spent discovering what you did not yet know. This is the most cognitively expensive chapter in the pipeline and the one with the highest return on investment. The Curtis, Krasner, and Iscoe 1988 study of large software projects found that defects introduced at the specification stage cost roughly ten to a hundred times more to fix downstream than defects introduced during implementation.[^curtis] You are at specification. The arithmetic of these two hours is straightforward even if the exact ratio is approximate.

[^curtis]: Curtis, B., Krasner, H., & Iscoe, N. (1988). "A Field Study of the Software Design Process for Large Systems." *Communications of the ACM*, 31(11), 1268–1287.

![Horizontal process flowchart of the three-phase Tic TOC pipeline: a Phase One block, a Phase Two block, and a Phase Three block in sequence — each carrying four small command sub-ticks — feeding a /g2 diagnostic decision diamond that loops back to the relevant phase on a re-run and arrows forward to the Cowork handoff terminal.](images/04-generating-your-tiktoc-fig-01.png)
*Figure 4.1 — The three-phase Tic TOC pipeline*

---

## Phase One: what you actually know about your book

The intake phase is four commands — `/i1` through `/i4` — and roughly forty-five minutes of session time when done well. The output is a confirmed Book Concept Summary: working title, one-sentence capability statement, one-sentence thesis, reader profile, deployment context, positioning against comparable texts. Each element looks simple. None of them are.

`/i1` asks the foundation questions. What is the working title? What does the reader learn — in one sentence? What is the central thesis — in one sentence? The pushback pattern across these questions is predictable and worth knowing before you encounter it. Vague topic answers get pushed toward specific capabilities. Lists of topics get pushed toward which one is load-bearing. Capability statements without measurable outcomes get pushed toward how you would know the reader could demonstrate them. Theses that anyone in the field would agree with get pushed toward what the book argues that competing books do not.

That last one is the hardest. A thesis that no one disagrees with is not a thesis — it is a topic restated as a claim. The acquisitions pragmatist discipline (introduced in Chapter 2) is asking what argument the book is making, and the question is sharper than most authors have been asked before.

Here is the `/i1` exchange that produced the ai-for-designers capability statement:

> **Tic TOC:** What does the reader learn — in one sentence?
>
> **Author:** The reader learns to use AI in their freelance design practice.
>
> **Tic TOC:** That is a topic. Not a learning outcome. Try: "The reader learns to [verb] [specific object] under [specific condition]." What is the one capability that, if mastered, justifies the book?
>
> **Author:** The reader learns to deploy AI in their design practice without losing the decisions their clients pay them to make.
>
> **Tic TOC:** Closer. "Deploy" is still vague. What does "deploy" look like as an action a reader could demonstrate?
>
> **Author:** The reader learns to identify which design decisions must stay human and which can be delegated to AI — and to defend that delegation map to a client.
>
> **Tic TOC:** Confirmed. That is a capability statement. Note: this statement now constrains every downstream chapter. Every chapter must contribute to either identification (which decisions stay human) or defense (how to articulate the delegation). Chapters that do neither are out of scope.

![Ascending staircase of four refinement rungs left to right — a vague topic rung, a rung that adds a constraint, a rung that adds an action, and a confirmed-capability rung at the top — connected by arrows, with three short Mager-criterion stubs (performance, condition, criterion) branching off the final rung.](images/04-generating-your-tiktoc-fig-02.png)
*Figure 4.2 — Capability statement: topic vs. demonstrable outcome*

Read the last note again. The moment the capability statement is committed, the chapter list narrows. Topics that seemed essential — an introduction to Midjourney, say — may no longer fit. Topics that seemed peripheral — the disclosure conversation — may now be load-bearing. The commitment does not just define the book. It defines what is not the book.

`/i2` asks what kind of book this is and where the reader will use it: practitioner handbook versus course textbook versus trade book versus field-defining monograph, and self-directed read versus workshop companion versus course adoption. Tic TOC will push back on misclassification. If the answer is "trade book" but the chapters end with assessable exercises, the answer is wrong. If the answer is "course textbook" but the reader is a self-directed solo practitioner, it is also wrong. The book type shapes downstream sequencing decisions in ways that propagate forward, and a misclassified book type at `/i2` produces misaligned sequence logic at `/l2`.

`/i3` is the gate where the most time gets spent. Chapter 2 showed the full Maya exchange — the thirty-second pause before the author moved from category to person. The pattern is the same in every session. "Designers" becomes "who, specifically?" becomes "what tenure, what client situation, what specific worry they have not yet acted on?" When the answer reaches a *person* — name, tenure, current client, current toolset, current fear — `/i3` is ready to mark passed.

`/i4` is where the thesis gets sharp. The thesis sentence stated in `/i1` returns now with harder questions: what does the book argue that competing books do not? Where does it sit on a shelf between which existing titles? The positioning move is borrowed from publishing acquisitions — the *vs.* statement: *unlike X, which does Y, this book does Z.* If the blanks cannot be filled, the book does not have positioning yet, and `/i4` will not pass.

Phase One ends when Tic TOC states: *"Phase One complete. Book Concept Summary ready for confirmation. Confirm, or revise?"* You confirm. The spec has a foundation.

| Command | Central question asked | Common pushback pattern | What confirmation produces downstream |
|---|---|---|---|
| `/i1` | Working title, one-sentence learning outcome, one-sentence thesis — what does the reader learn? | Vague topics pushed toward specific capabilities; lists pushed toward the one load-bearing item; theses everyone agrees with pushed toward what the book argues that competitors do not | A confirmed capability statement that constrains every later chapter — any chapter contributing to neither identification nor defense is out of scope |
| `/i2` | What kind of book (handbook / textbook / trade / monograph) and where the reader uses it (self-directed / workshop / course) | Misclassification: "trade book" with assessable exercises, or "course textbook" for a solo practitioner | A locked book type that governs sequencing at `/l2`; a misclassified type here produces misaligned sequence logic later |
| `/i3` | Who, specifically, is the reader — tenure, current client, current toolset, current fear? | "Designers" pushed to "who, specifically?"; category pushed to a named person with a concrete unacted-on worry | A reader profile sharp enough to test every example and exercise against a real person |
| `/i4` | What does the book argue that competing books do not? Where does it sit between which titles? | The positioning *vs.* move: *unlike X, which does Y, this book does Z* — if the blanks cannot be filled, positioning does not exist yet | A defensible shelf position and a thesis sharp enough to survive acquisitions scrutiny |

---

## Phase Two: the pedagogical spine

Phase Two is the learning architecture — four commands, roughly thirty to forty-five minutes when Phase One is solid. The output is the pedagogical spine of the book: outcomes, sequence, arc, prerequisites.

`/l1` is where the curriculum theorist takes over. Tic TOC asks for three to five learning outcomes per chapter, each tagged with a Bloom's level. The Anderson-Krathwohl 2001 revision of Bloom's taxonomy supplies the vocabulary: Remember, Understand, Apply, Analyze, Evaluate, Create.[^anderson] The verbs matter in a way that catches most authors unprepared. *Understand* is a low-ceiling verb — the reader can explain. *Apply* is the working floor of a useful practitioner handbook — the reader can do it once, in a constrained context. *Evaluate* and *Create* are the high-judgment ceilings.

A practitioner handbook should have no chapter with an outcome below Apply as its ceiling. The reader has not committed time to reading a book in order to *understand* something — they read it to *do* something. If an outcome is written at Understand level, Tic TOC will push upward: what can the reader *do* with the understanding?

Robert Mager's 1962 criterion gives the analytical foundation.[^mager] A real learning outcome names three things: the *performance* (what the reader does), the *condition* (under what circumstances), and the *criterion* (what counts as success). "The reader will understand the fluency trap" fails all three. "The reader will identify three fluency trap patterns in their own AI-assisted work from the last six months, distinguishing patterns that collapse under client questioning from patterns that do not" satisfies them. The difference is not pedantry. It is the difference between a chapter Cowork can draft against and a chapter Cowork will pad.

![Bar chart of the six Bloom's taxonomy levels in order — Remember, Understand, Apply, Analyze, Evaluate, Create — with bars rising from a zero baseline to encode increasing cognitive ceiling, and a single horizontal threshold line drawn at the Apply level marking the practitioner-handbook working floor; bars below the floor (Remember, Understand) shown in lower saturation than bars at or above it.](images/04-generating-your-tiktoc-fig-03.png)
*Figure 4.3 — Bloom's verb ceiling for a practitioner handbook*

[^anderson]: Anderson, L. W., & Krathwohl, D. R. (Eds.). (2001). *A Taxonomy for Learning, Teaching, and Assessing*. Longman.
[^mager]: Mager, R. F. (1962, revised 1997). *Preparing Instructional Objectives*. Center for Effective Performance.

`/l2` asks in what order the chapters appear and why — chronological, conceptual, build-sequence, or by complexity — and what dependencies exist between chapters. For a practitioner handbook organized around a production pipeline, the answer is build-sequence: each chapter produces an artifact that the next chapter consumes. This is what makes the bridge questions structurally load-bearing rather than ornamental.

`/l3` applies three-act structure pedagogically. Act One establishes; Act Two builds; Act Three applies. What matters is not the act labels but the *transition conditions* — the explicit statements of what the reader must be able to do before the next act can begin. Without transition conditions, the acts blur, the reader cannot tell when they are ready to move forward, and Cowork cannot tell either. For the ai-for-designers running example, the transition into Act Two is: *"The reader can articulate the delegation principle"* — not "the reader has read chapters 1 and 2," but a capability the reader either has or does not have.

`/l4` maps prerequisites. What must the reader already know to start the book? What is addressed at first use via sidebar? What is explicitly out of scope? The forcing function: anything listed as a prerequisite must actually exist in the reader. Anything listed as "addressed at first use" requires a sidebar to be written somewhere. Anything listed as "explicitly out of scope" must be defended — the *power of No*, in publishing acquisitions vocabulary.

Phase Two passes when outcomes are mapped to Bloom's levels with a defensible distribution and every chapter has at least one outcome at Apply or above.

| Chapter | Title | Bloom's ceiling | Create-level deliverable (if any) |
|---|---|---|---|
| Ch 1 | The fluency trap | Analyze | — |
| Ch 2 | The AI+1 designer | Apply | — |
| Ch 3 | Diagnosing the fluency trap in your own work | Create | A 200-word defense-or-acknowledgment statement for one piece of AI-assisted work |
| Ch 4 | What you can actually assign | Evaluate | — |
| Ch 5 | The delegation map | Create | A documented delegation map separating human-only from AI-eligible decisions |
| Ch 6 | Presenting AI-assisted work | Apply | — |
| Ch 7 | Defending the account | Create | A rehearsed client-defense script for a skeptical revision review |

---

## Phase Three: the chapter that Cowork will actually draft

Phase Three is the chapter architecture — four commands, roughly forty-five minutes to an hour. This is where the specification becomes executable.

The engine of Phase Three is `/c1`, which produces a structured entry for every chapter in the book. Each entry must contain: a one-line capability statement, an opening strategy, four to five core content blocks in sequence, a worked example, assessable exercises with Bloom's tags, and a bridge question that commits to what the next chapter will deliver.

The capability statement is where most chapters fail. Topic headings produce Cowork drift. Capability statements give Cowork a target. The difference between the two is the most important thing this chapter can demonstrate, so here it is demonstrated directly.

Both entries below are real — from the same chapter of the ai-for-designers TIKTOC.md, one from the first-pass session before `/g2` was run, one from the revised version after pushback was honored.

**First-pass entry — Chapter 3 (pre-/g2):**

> **One-line:** Students learn about the fluency trap in graphic design.
>
> **Opening:** Discussion of how AI tools produce output that looks professional.
>
> **Core content blocks:** Examples of fluency trap; common patterns; how to recognize fluency trap; what to do about it.
>
> **Worked example:** AI-generated logo case study.
>
> **Exercises:** Identify a fluency trap example; reflect on implications; discuss with peer.
>
> **Bridge:** Now that you understand the fluency trap, we move on to copyright issues.

**Revised entry — Chapter 3 (post-/g2, pushback honored):**

> **One-line:** Readers learn to identify the seven fluency trap patterns in their own AI-assisted design work and to predict which patterns will collapse under specific kinds of client questioning.
>
> **Opening:** A senior designer's portfolio review — five pieces presented, four AI-assisted, the reviewer's pen pauses at the third. The reader reads the same five pieces and tries to predict which one the pen will land on.
>
> **Core content blocks:**
> 1. The fluency trap defined — Oppenheimer's processing fluency framing, applied to design specifically
> 2. The seven patterns (typographic, brand-like-not-brand, additive overload, polished-empty, variation overload, portfolio misrepresentation, presentation collapse)
> 3. The three client-questioning failure modes (why-this-typeface, revision-of-one-element, defend-the-rationale)
> 4. The pattern × question matrix — which patterns collapse under which questions
> 5. The five-minute self-audit — running the patterns against your own recent work
>
> **Worked example:** Three AI-assisted brand identities, all presented as finished, each demonstrating one or more fluency trap patterns. Side-by-side critique against the seven-pattern taxonomy.
>
> **Assessable exercises:**
> 1. (Analyze) Identify three fluency trap patterns in a piece of your own AI-assisted work from the last six months.
> 2. (Evaluate) For each pattern, predict the client question that would expose it.
> 3. (Create) Draft a 200-word defense-or-acknowledgment statement for one piece of AI-assisted work you might present this week.
>
> **Bridge:** The fluency trap is now diagnosable in your own work. Identifying the trap is not enough — at some point the work must be presented and assigned to a client, and the legal question arrives. Chapter 4 addresses what you can actually assign.

Now read the Cowork output each entry produced.

**From the first-pass entry:**

> In this chapter we will discuss the fluency trap in graphic design. AI tools have become widely used in design workflows, and one of the challenges designers face is that AI output often looks professional and finished, even when it lacks the strategic depth or craft judgment that defines high-quality design work. This chapter explores what the fluency trap is, why it matters, and what designers can do about it...
>
> [continues for roughly 2,800 more words in similar register]

Generic. "In this chapter we will discuss" is exactly the phrase a practitioner handbook must not begin with. No scene. No specific reader. No specific designer in a specific moment. The chapter is *about* the fluency trap without ever *demonstrating* it.

**From the revised entry:**

> *The dangerous AI output is not ugly. It is attractive enough to stop your judgment too early.*
>
> A senior brand director leans over a portfolio review at a London agency, 2026. Five pieces on the table. Four were assisted by AI in some part of the workflow; the reviewer does not know which. Her pen pauses at the third piece — a healthcare consulting identity. She points to a single decision in the wordmark and asks: "Why did you choose this terminal stroke weight?"
>
> The designer hesitates.
>
> The reader reads the same five pieces, on the following pages, and tries to predict before turning each page which one the pen will land on. The exercise is at the chapter's spine because the diagnostic skill it builds is the spine: you will learn to see the fluency trap before your reviewer does...
>
> [continues into the seven-pattern taxonomy]

This is the chapter's central argument made operational. The difference between those two openings is one round of `/g2` pushback and one hour of honored revision. Propagated across eleven chapters, that difference is the difference between a book worth rewriting and a Cowork dump.

The other three `/c` commands — `/c2` through `/c4` — are supporting passes. `/c2` formalizes the chapter anatomy template: what every chapter must contain as a structural minimum. `/c3` decides the running-example strategy — one domain consistently across all chapters, or rotating examples. For practitioner handbooks, consistency compounds; rotating examples lose the narrative scaffolding that builds from chapter to chapter. `/c4` is the honesty pass: what does the book claim that is contested in the field? What does it skip? What is the aging risk — content that will be wrong in two years? Everything flagged here goes into the open questions log.

---

## The /g2 diagnostic

`/g2` runs the 7 Adoption Failure Mode diagnostic against the completed TIKTOC.md. It is the gate to Cowork handoff.

The seven failure modes are roughly: audience drift, missing prerequisites, over-claimed outcomes, under-specified deliverables, contested claims left unflagged, bridge questions that do not actually bridge, and capability statements that are topics in disguise. (The exact list shifts across prompt versions; the current set is the one reproduced in Appendix A.) Each chapter entry is read against each failure mode. The output is a structured table — failure mode × chapter — with a status flag and a one-line diagnostic per cell.

Here is the `/g2` table from the ai-for-designers running example, lightly trimmed:

> | Failure Mode | Ch 1 | Ch 2 | Ch 3 | Ch 4 | Ch 5 | Ch 6 | Ch 7 |
> |---|---|---|---|---|---|---|---|
> | Audience drift | PASS | PASS | PASS | PASS | WARN | PASS | PASS |
> | Missing prerequisites | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
> | Over-claimed outcomes | PASS | PASS | WARN | PASS | PASS | PASS | PASS |
> | Under-specified deliverables | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
> | Contested claims unflagged | WARN | PASS | PASS | PASS | PASS | PASS | PASS |
> | Bridge fails to bridge | PASS | PASS | PASS | PASS | PASS | WARN | PASS |
> | Capability statement is topic | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
>
> *Five WARNINGS. Zero FAILs. Recommend resolving the Ch 3 over-claim, the Ch 1 contested-claims flag, the Ch 6 bridge, and the Ch 5 audience-drift before Cowork handoff. Ch 1's contested claim is high-priority: the WEF "fastest-declining job" framing is genuinely contested in the literature and the chapter should flag it explicitly.*

Five warnings, each addressable in ten to twenty minutes. The intellectual operation the `/g2` diagnostic performs — structured comparison, each chapter entry read against each failure mode, every discrepancy surfaced before it reaches a Cowork run — is one the instructional research treats as high-yield. Marzano, Pickering, and Pollock's 2001 meta-analysis reported an average effect size of 1.61 for "identifying similarities and differences," among the highest in the study; later re-analysis, including a 2010 McREL report by Beesley and Apthorp, could not reproduce that figure and treats it as an implausibly high upper bound.[^marzano] Lean on the direction, not the number: structured comparison is a strong move, and the exact magnitude is contested. Either way, surfacing every discrepancy before it reaches drafting is cheaper than fixing it after.

[^marzano]: Marzano, R. J., Pickering, D. J., & Pollock, J. E. (2001). *Classroom Instruction That Works*. ASCD. The 1.61 figure has not been reproduced; see Beesley, A. D., & Apthorp, H. S. (Eds.) (2010), *Classroom Instruction That Works* (2nd ed. research report), McREL, which recalibrates the strategy effects downward.

After resolving the warnings, re-run `/g2`. If the second pass returns clean, the TIKTOC.md is ready for Cowork. If warnings persist, the choice is binary: resolve them, or log them to `/p2` as BLOCKED with explicit rationale. Logged and acknowledged is acceptable. Unaddressed is not.

![A seven-row by seven-column status grid — seven failure modes read against seven chapters — with five cells filled solid to mark WARN and the remaining forty-four shown as outline-only PASS cells, and zero FAIL; thin grid rules throughout.](images/04-generating-your-tiktoc-fig-04.png)
*Figure 4.4 — The /g2 failure-mode × chapter diagnostic grid*

| Failure mode | Ch 1 | Ch 2 | Ch 3 | Ch 4 | Ch 5 | Ch 6 | Ch 7 | Diagnostic for the warning |
|---|---|---|---|---|---|---|---|---|
| Audience drift | PASS | PASS | PASS | PASS | **WARN** | PASS | PASS | Ch 5 examples drift toward agency teams; reader is a solo practitioner |
| Missing prerequisites | PASS | PASS | PASS | PASS | PASS | PASS | PASS | — |
| Over-claimed outcomes | PASS | PASS | **WARN** | PASS | PASS | PASS | PASS | Ch 3 promises seven-pattern mastery but exercises test only three |
| Under-specified deliverables | PASS | PASS | PASS | PASS | PASS | PASS | PASS | — |
| Contested claims unflagged | **WARN** | PASS | PASS | PASS | PASS | PASS | PASS | Ch 1 uses the WEF "fastest-declining job" framing without flagging it as contested |
| Bridge fails to bridge | PASS | PASS | PASS | PASS | PASS | **WARN** | PASS | Ch 6 bridge restates the topic rather than committing to Ch 7's deliverable |
| Capability statement is topic | PASS | PASS | PASS | PASS | PASS | PASS | PASS | — |

*Five WARNINGS. Zero FAILs. Each warning is addressable in ten to twenty minutes; the Ch 1 contested-claim flag is highest-priority.*

---

## What "ready for Cowork" means

Cowork is a downstream execution system. It reads the TIKTOC.md at runtime and drafts against it. It cannot ask you to clarify what you meant.

This practical constraint defines what the specification must be. Every section of the TIKTOC.md must be specific enough that a model reading it can produce a chapter without needing your judgment for any structural decision. Voice can drift in ways the human rewrite corrects. But the *structure* — the capability statement, the opening strategy, the worked example specification, the exercise verbs, the bridge commitment — must be unambiguous, because Cowork will execute against whatever it finds, and a vague specification produces a vague chapter at the same speed as a precise specification produces a precise one.

The checklist for ready-for-Cowork is eight items. Every chapter must have a capability statement at Apply level or above. Every chapter must have a Bloom's ceiling explicit in the outcome map. Every chapter must have at least one Apply-or-above exercise. Every chapter must have a bridge question that commits to the next chapter's content. Every chapter must have either a worked example specified or a `[verify]` placeholder that flags the gap. Every contested claim must be labeled. The `/g2` diagnostic must return clean, or every warning must be logged as BLOCKED in `/p2` with rationale. And `/p2` itself must be current — no open questions forgotten, every risk acknowledged and assigned.

When all eight conditions are met, the TIKTOC.md is ready. The 10–100x cost ratio applies here with the same force it applied in Chapter 2. Every BLOCKED item that propagates to the Cowork draft costs roughly an hour of rewriting. Every BLOCKED item that propagates to the final check costs roughly a day. The arithmetic of the checklist is the same arithmetic as the session itself: do it now, cheaply, or pay for it later.

---

## What the session leaves you with

Two hours. The output is a markdown file — the TIKTOC.md — that specifies every chapter of the book in enough detail that Cowork can draft without clarification.

That is a strange thing to hold at the end of two hours that felt like cognitive work and produced no prose. The TIKTOC.md is not the book. It looks nothing like the book. It is a specification document full of structured tables, capability statements, Bloom's-tagged exercises, and bridge questions. Nothing in it resembles the chapter you will eventually write or revise.

But the specification is the part that determines what the rest of the pipeline produces. Wiggins and McTighe's Backward Design argument is that the most-skipped stage in curriculum design — *Identify Desired Results* — is also the highest-leverage one.[^wiggins] The spec defines what counts as a successful chapter. Without it, you cannot evaluate a draft; you can only react to one. With it, the evaluation is structural: does this chapter have what the TIKTOC.md said it would have? Does it deliver on the bridge question? Does the worked example match the specification?

There is a name for what we are doing here. The systems thinker Donella Meadows — who, with three co-authors, wrote the 1972 *Limits to Growth* and, alone, the posthumous *Thinking in Systems* — spent her career mapping leverage points, the places in a system where a small change moves everything else. She ranked them from weak to strong: tweak a parameter and little shifts; change the system's structure and its whole behavior changes; reach the level that determines structure and you have moved the most. *The structure of a system determines its behavior*, she wrote. The TIKTOC.md is that structural level for the book. Two hours spent here move more than two months spent anywhere downstream — not because the work is larger, but because it sits higher in the system.[^meadows]

[^wiggins]: Wiggins, G., & McTighe, J. (2005). *Understanding by Design* (Expanded 2nd ed.). ASCD.
[^meadows]: Meadows, D. H. (2008). *Thinking in Systems: A Primer*. Chelsea Green. The 1972 *Limits to Growth* was co-authored with Dennis Meadows, Jørgen Randers, and William Behrens; the "Leverage Points" essay (1999) is widely available online.

The sessions in which authors resist the pushback — accept every first answer, advance quickly through the gates — produce TIKTOC.md files that look complete. The Cowork runs they produce look like textbook chapters. They read generically. The exercises ask the reader to "reflect" and "consider." The bridge questions say "now that you understand X, we move on to Y." The opened paragraphs say "in this chapter we will discuss." The author spends the human rewrite phase rebuilding the structure that the specification session was supposed to produce.

The sessions in which authors honor the pushback — pause at the hard question, rewrite the capability statement until it names a demonstrable action, sit with the commitment until the chapter list actually narrows — produce the other kind. The kind where the Cowork output opens with a scene, runs a specific taxonomy, ends with an exercise the reader actually completes.

The difference is made in two hours, early, when it is cheap to make it.

Tic TOC is not the only way to do this work. A practicing acquisitions editor or instructional designer reading your TIKTOC.md will catch things the prompt misses; both is better, one is workable, zero is the path that ends in a Cowork dump and a rewrite that costs more than the session would have. With the spec in hand, the next move is the scaffold — one command that turns the specification into a directory of files and quietly tests how much of the spec was real.

---

## Sources

1. Curtis, B., Krasner, H., & Iscoe, N. (1988). "A Field Study of the Software Design Process for Large Systems." *Communications of the ACM*, 31(11), 1268–1287. https://dl.acm.org/doi/10.1145/50087.50089
2. Anderson, L. W., & Krathwohl, D. R. (Eds.). (2001). *A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy of Educational Objectives.* Longman.
3. Mager, R. F. (1962; rev. 1997). *Preparing Instructional Objectives.* Center for Effective Performance.
4. Wiggins, G., & McTighe, J. (2005). *Understanding by Design* (Expanded 2nd ed.). ASCD. https://www.ascd.org/books/understanding-by-design-expanded-2nd-edition
5. Marzano, R. J., Pickering, D. J., & Pollock, J. E. (2001). *Classroom Instruction That Works.* ASCD. https://files.eric.ed.gov/fulltext/ED543521.pdf
6. Beesley, A. D., & Apthorp, H. S. (Eds.). (2010). *Classroom Instruction That Works* (2nd ed. research report). McREL. The re-analysis that did not reproduce Marzano's 1.61 effect size. https://files.eric.ed.gov/fulltext/ED543521.pdf
7. Meadows, D. H. (2008). *Thinking in Systems: A Primer.* Chelsea Green. https://www.chelseagreen.com/product/thinking-in-systems/
