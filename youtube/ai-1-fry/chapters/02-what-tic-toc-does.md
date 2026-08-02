# Chapter 2 — What Tic TOC Does and Why You Spend Two Hours Here First

*The architecture comes before the writing — and the architecture is the harder work.*

---

Here is something that surprises most authors when they first encounter it: the most expensive mistake you can make in this pipeline happens before a single chapter is drafted. It happens when you decide what the book is about, who it is for, and what a reader should be able to do after finishing it — and you get those things subtly wrong. The mistake is invisible at the time. It becomes visible fifty thousand words later, when a chapter refuses to connect to the one before it, when the exercises feel decorative, when a colleague reads the manuscript and says, "I'm not sure what I'm supposed to do with this."

The purpose of Tic TOC is to make that mistake expensive to commit, and cheap to catch.

I want to show you what I mean before I explain why. The next several pages contain an excerpt from the actual `TIKTOC.md` produced for *AI for Designers: A Practitioner's Guide* — the running example of this book. Read it as a finished object. Notice what is in it. Notice, more importantly, what a typical author's outline would have left out.

---

> **AI for Designers: A Practitioner's Guide**
> Full TOC Draft — compiled from all phase outputs
> Author: [redacted] · Series: AI+1 · Status: Pre-draft
>
> ---
>
> **PART 1 — BOOK CONCEPT AND THESIS**
>
> *Book concept summary:* This book teaches the **one-client freelance designer to operate as an AI+1 practitioner** — keeping the design identity, adding fluent and risk-aware AI use, and protecting the decisions that carry client trust, brand meaning, and creative accountability — by **walking them through the specific moves of an AI-enabled design practice: the delegation map, the contractual rider, the disclosure conversation, the brand stewardship discipline, and the portfolio defense.** It fills the gap left by tool tutorials (which teach Firefly but not the client conversation) and traditional design education (which teaches taste but not how to deploy AI without destroying it).
>
> *One-sentence logline:*
> The fluency trap costs you the account; the AI+1 designer keeps it.
>
> *Central thesis:*
> "This book argues that the working freelance designer's most valuable professional asset is the layer of tacit client knowledge that no AI tool can reach — and that AI fluency is most valuable when it accelerates production without ever being allowed to make decisions from that layer."
>
> ---
>
> **PART 2 — LEARNER PROFILE**
>
> *Primary reader:* A freelance graphic or brand designer with five to fifteen years of practice, one primary anchor client, and a ChatGPT-or-Claude tab open while reading this paragraph.
>
> *Prior knowledge assumed:* Working knowledge of Adobe Creative Cloud or Figma; basic familiarity with at least one generative AI tool; client-facing experience; comfort defending design decisions in a presentation.
>
> *Prior knowledge NOT assumed:* Legal training; copyright law; AI/ML literacy beyond consumer-grade tool use; experience writing for publication.
>
> *Prior misconceptions:*
> 1. "If the client likes it, it worked."
> 2. "The fluency trap means bad AI output."
> 3. "AI fluency means better prompting."
> 4. "If I reject AI, my role is safe."
>
> ---
>
> **PART 7 — LEARNING OUTCOMES BY CHAPTER (excerpt)**
>
> | Ch | Title | Bloom's Ceiling | Create-level outcome |
> |----|-------|----------------|----------------------|
> | 1 | The AI+1 Designer | Evaluate | — |
> | 2 | Production Tasks | Apply | — |
> | 3 | The Fluency Trap | Evaluate | — |
> | 4 | IP and Copyright | Apply | — |
> | 5 | Client Disclosure | Create | Disclosure framework |
> | 6 | The One-Client Relationship | Evaluate | — |
> | 7 | Taste and Accountability | Create | Defense rubric |
>
> ---
>
> **PART 8 — CHAPTER 1 ENTRY (excerpt — capability statement and bridge)**
>
> **Chapter 1 one-line:** *Readers learn to distinguish the AI+1 designer from the designer who has been replaced — and to identify the specific decisions their own practice depends on protecting.*
>
> **Opening:** A freelance brand designer delivers an AI-generated identity system to a long-term client. The presentation looks clean. Six months later, the client asks: "Why did we choose this typeface?" The designer does not have an answer.
>
> **Bridge to Chapter 2:** The AI+1 designer is not the designer with the most tools. It is the designer with the clearest boundary between assistance and abdication. Chapter 2 turns the frame into a work tool: the delegation map.

![Vertical document map of the TIKTOC.md: eight uniform boxes stacked top to bottom in reading order, threaded by a thin spine line. Parts 1 (Book Concept and Thesis), 2 (Learner Profile), 7 (Learning Outcomes by Chapter), and 8 (Chapter Entries) are rendered as solid filled boxes because the chapter excerpts them; Parts 3 through 6 are hollow outlines to signal that the structure exists but is not shown.](images/02-what-tic-toc-does-fig-01.png)
*Figure 2.1 — The TIKTOC.md document map*

---

Three things are doing work in those 1,200 words that a standard author's outline does not do.

The capability statements use verbs that name what the reader can *do* — *distinguish*, *identify* — not what they will be *aware of*. The Bloom's ceiling table assigns every chapter a maximum cognitive level it is required to reach, which means the book has a cognitive arc, not just a topical progression. And the bridge question at the end of the Chapter 1 entry makes a structural commitment: Chapter 2 *must* deliver on the question that Chapter 1 raises. Once that bridge is written, the two chapters are in a logical contract with each other.

These three features — capability verbs, Bloom's ceilings, bridge questions — are what separate a TIKTOC.md from an outline. An outline tells you what topics the author intends to cover. A TIKTOC.md tells Cowork what the reader must be able to do, at what cognitive level, and in what sequence. The downstream system can execute against a TIKTOC.md without asking for clarification. It cannot execute against an outline in the same way, because an outline does not resolve those questions. It simply defers them.

![A two-column feature matrix comparing an author's outline against a TIKTOC.md across six rows. The left (outline) column shows hollow, partial cells to mark each feature as deferred; the right (TIKTOC.md) column shows solid filled cells to mark each feature as resolved, with a clear divider between the columns. The fill-versus-hollow contrast carries the message that the outline defers what the specification resolves.](images/02-what-tic-toc-does-fig-02.png)
*Figure 2.2 — Author's outline vs. TIKTOC.md specification*

| Feature | Author's outline | TIKTOC.md |
|---|---|---|
| What it specifies | Topics the author intends to cover | What the reader must be able to do, in what order |
| Who the audience is | A category ("freelance designers") | A specific named person with a job, a tool, and a current problem |
| What the reader can do | Left implicit — "be aware of," "understand" | Stated as demonstrable capability verbs — distinguish, identify, defend |
| Cognitive level required | Unspecified | A Bloom's ceiling assigned per chapter, giving the book a cognitive arc |
| Chapter-to-chapter logic | Topical adjacency only | Bridge questions that put each chapter in a logical contract with the next |
| Whether Cowork can execute without clarification | No — defers the load-bearing questions | Yes — resolves audience, outcome, level, and sequence at runtime |

---

## What makes a specification different from a plan

The software engineering field has a precise vocabulary for the distinction I am drawing. A specification is a document that a downstream system — whether that system is a compiler, a manufacturing process, or a language model running a Cowork pipeline — can execute against without additional input from the author. A plan is a document that orients the author. Plans are useful for getting started. Specifications are required for handing off.

In 1988, Bill Curtis, Herb Krasner, and Neil Iscoe published a study of seventeen large software projects in *Communications of the ACM*.[^curtis] They were trying to understand where defects came from. The finding that stayed with the field was this: defects introduced during requirements analysis — the specification stage — cost roughly ten to a hundred times more to fix than defects introduced during implementation. The further upstream the defect, the more catastrophic the downstream rework, because every subsequent decision is built on top of the mistaken one.

The number has been replicated in various forms across software engineering literature, with the exact ratio varying by domain. What has not been formally replicated is the direct analog for textbook authorship — there is no peer-reviewed study confirming that a vague TIKTOC.md costs ten times as much to repair as vague prose in a chapter draft. I am inferring from the analogy, and the inference is honest rather than certain. What I can say is that the practitioner experience matches the prediction: authors who begin Cowork runs with underspecified capability statements spend more time rewriting chapters than they would have spent fixing the statements. The arithmetic of the two-hour session is straightforward even if the ratio is approximate.

[^curtis]: Curtis, B., Krasner, H., & Iscoe, N. (1988). "A Field Study of the Software Design Process for Large Systems." *Communications of the ACM*, 31(11), 1268–1287.

The deeper point is structural. Cowork is a downstream execution system. It reads the TIKTOC.md at runtime and drafts against it. When the TIKTOC.md says "by the end of Chapter 5, the reader will have produced a disclosure framework for their primary client," Cowork knows what the chapter must accomplish, what register the exercises must work in, and what a finished chapter looks like. When the TIKTOC.md says "Chapter 5 covers client disclosure," Cowork has none of that. It will write something. The something will look like a chapter. But it will not be the chapter, because the chapter requires knowing who the reader is, what they are afraid of, what they are capable of doing, and what they will hand a client at the end.

The TIKTOC.md is the specification. The Cowork run is the implementation. Tic TOC is the tool that builds the specification by forcing you to answer the questions you would otherwise defer.

---

## The three disciplines inside the prompt

Tic TOC behaves as if three different professionals are present throughout the session. The prompt does not literally simulate three roles, but the questions it asks come from three distinct intellectual traditions, and naming them helps you understand why the prompt pushes back where it does.

The first discipline is that of the **curriculum theorist**. The canonical contemporary framework here is Wiggins and McTighe's *Understanding by Design*, first published in 1998.[^wiggins] Their argument, called Backward Design, is that the sequence most instructors follow — choose topics, write content, add assessment at the end — is backwards. The right sequence is: start with the outcomes you want, design the assessments that would demonstrate those outcomes, then design the instruction that prepares students to perform them. They call the first stage *Identify Desired Results*, and they argue it is the most commonly skipped stage in curriculum design.

Tic TOC enforces it as a software constraint. You cannot advance from the audience intake phases to the learning outcomes phases without a confirmed Book Concept Summary. The gate is not a suggestion. The prompt will not advance until you explicitly confirm that the summary reflects your book, not a plausible-sounding approximation of it.

An older voice here is Hilda Taba, the Estonian-American curriculum theorist whose 1962 *Curriculum Development: Theory and Practice* argued for an inductive approach: begin with the specific needs of actual students, and build the curriculum upward from there.[^taba] The first intake question Tic TOC asks — not "what is your book about," but "who is the specific person you are writing for?" — is Taba's move at the conversational level.

[^wiggins]: Wiggins, G., & McTighe, J. (2005). *Understanding by Design* (Expanded 2nd ed.). ASCD.
[^taba]: Taba, H. (1962). *Curriculum Development: Theory and Practice*. Harcourt, Brace & World.

The second discipline is that of the **acquisitions pragmatist**. This is the publishing-industry voice. It asks whether your reader actually exists, whether they have a reason to read this book rather than some adjacent one, whether the timeline is realistic given your other obligations, and whether there is a defensible position for this book on the shelf. Publishing acquisitions is a craft tradition more than a research field — no single canonical text governs it — but the vocabulary it uses (comparable texts, positioning, reader profile) is well-established in trade publishing, and Tic TOC imports it directly into the specification session.[^publishing-note]

[^publishing-note]: The chapter's references here are to general trade publishing practice. No single text is load-bearing; the vocabulary is standard in imprint editorial culture.

The third discipline is that of the **instructional designer**. Robert Gagné's *Conditions of Learning*, first published in 1965, argued that different types of learning require different instructional conditions and sequences — that you cannot teach a student to solve a novel problem without first teaching the component skills, and that the sequence matters as much as the content. The Anderson-Krathwohl 2001 revision of Bloom's taxonomy provides the verb vocabulary: Remember, Understand, Apply, Analyze, Evaluate, Create.[^bloom] Robert Mager's shorter work, *Preparing Instructional Objectives*, argued that a real objective specifies three things — the *performance* the learner will demonstrate, the *condition* under which they demonstrate it, and the *criterion* for success — and that the verb is load-bearing in ways most authors do not appreciate until they try to write an exercise against a poorly formed objective.[^mager]

The instructional designer in Tic TOC is what refuses to let a capability statement pass if the verb is *understand* or *appreciate* or *be familiar with*. Those verbs name states of mind that cannot be observed or tested. *Apply*, *analyze*, *construct*, *defend* — those name actions a reader can actually perform, and a chapter can actually aim at.

[^bloom]: Anderson, L. W., & Krathwohl, D. R. (Eds.). (2001). *A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy of Educational Objectives*. Longman.
[^mager]: Mager, R. F. (1962, revised 1997). *Preparing Instructional Objectives*. Center for Effective Performance.

The three disciplines are not crisp categories. They overlap, and a working professional in any one of them borrows from the others. The point of naming them is not academic taxonomy. It is to give you a vocabulary for noticing which discipline is speaking when Tic TOC pushes back. When the prompt says your audience profile is too vague and asks you to name a specific person — that is the curriculum theorist applying Taba. When it asks what comparable book sits on the shelf next to this one — that is the acquisitions pragmatist. When it says your capability statement has no demonstrable verb — that is the instructional designer applying Mager.

![An equilateral triangle with the three disciplines at its vertices — curriculum theorist, acquisitions pragmatist, and instructional designer — each in a distinct color. From each vertex a single directional arrow points to a small target node naming the phase of Tic TOC that discipline governs: the curriculum theorist points to the intake/audience phase, the instructional designer to capability-verb enforcement, and the acquisitions pragmatist to the positioning and comparable-text check. The triangle edges are thin and neutral to show the disciplines overlap yet stay distinct.](images/02-what-tic-toc-does-fig-03.png)
*Figure 2.3 — The three disciplines triangle*

---

## The phase gates, and what each one catches

Tic TOC is phase-gated. The session moves through three phases — Intake, Learning Architecture, Chapter Architecture — and you cannot advance past a gate until the prompt explicitly confirms it has been passed. This is not novel software design. Robert Cooper formalized the logic in a 1990 paper in *Business Horizons*, calling it Stage-Gate: work flows through bounded phases with explicit decision points between them, and compressing or skipping a gate produces compounding downstream cost.[^cooper]

[^cooper]: Cooper, R. G. (1990). "Stage-Gate Systems: A New Tool for Managing New Products." *Business Horizons*, 33(3), 44–54.

Cooper's original model had five gates. Tic TOC has fewer. The architecture is the same.

![A left-to-right process flowchart of three phase blocks — Intake, Learning Architecture, Chapter Architecture — each in a distinct color, separated by diamond checkpoint gates. A final /g2 diagnostic diamond feeds a Cowork-handoff terminal node. A blockage symbol sits on a "skip the gate" branch to convey that compressing a gate produces compounding downstream cost. The thirteen individual gate commands are grouped into the three phase-boundary checkpoints rather than drawn separately.](images/02-what-tic-toc-does-fig-04.png)
*Figure 2.4 — Phase gates and what each catches*

| Gate | Question the gate asks | What breaks if skipped |
|---|---|---|
| /i3 → /i4 (audience confirmed) | Who is the specific person you are writing for? | Audience drift — chapters address a category, not a reader, and exercises feel decorative |
| /i4 → /l1 (thesis confirmed) | What is the one argument this book makes, in a sentence? | The book sprawls; chapters cover topics with no load-bearing claim to serve |
| /l1 → /l4 (learning architecture) | What must the reader be able to do, at what Bloom's ceiling? | Outcomes stated as "understand" rather than demonstrable verbs; over-claimed outcomes slip through |
| /l4 → /c1 (architecture confirmed) | Does the cognitive arc sequence prerequisites correctly? | Missing prerequisites; a chapter assumes a skill the book never taught |
| /c1 → /g1 (chapter entries) | Does each chapter's bridge question commit the next chapter? | Chapter-to-chapter logic collapses; chapters stop connecting |
| /g1 → /g2 (pre-diagnostic) | Are contested claims flagged and sources attributed? | Contested claims pass as settled; the brief over-promises |
| /g2 → Cowork handoff | Does the completed TOC pass the seven-failure-mode diagnostic? | A defect ships into 50,000 words of drafting, where it costs 10–100× more to repair |

What "confirmed" means at each gate is concrete. Tic TOC will ask explicitly: *I am proposing to mark this gate as confirmed. Do you confirm, or do you want to revise?* You can revise. You can ask for elaboration. The gate does not advance on inertia. It advances on your explicit agreement, which means you have a record of every architectural decision you made and the moment you made it.

The final gate — the /g2 diagnostic — runs the completed TOC against seven recurring failure modes for instructional texts: audience drift, missing prerequisites, over-claimed outcomes, contested claims left unflagged, and others. When /g2 returns clean, the TIKTOC.md is ready for Cowork. When it flags items, those items are blockers: you resolve them, or you log them as open questions and proceed knowing where the risk is.

---

## What the session actually feels like

The most common reason an author abandons Tic TOC in the first twenty minutes is that they expect it to behave like a form. It does not.

Tic TOC asks one question at a time. It waits for an answer that has *content*. When you give a vague answer, it does not log the vagueness and move on. It pushes back. The pushback is direct: *"That answer would produce a chapter Cowork could write about any field. Can you make it specific to your reader's actual practice?"*

The session's value is in the friction. Most of what a Tic TOC session produces could, in principle, be produced by a sufficiently self-critical author working alone. The problem is that self-criticism of this kind is nearly impossible to sustain across an entire specification session. We accept our first approximations. We paper over the vague spots with fluent sentences. We defer the difficult questions because they are difficult and the easy ones are ready. Tic TOC enforces a standard you cannot maintain against yourself, because the standard is applied question by question, and the prompt does not get tired.

The cognitive load is real. John Sweller's work on cognitive load theory — first set out in 1988 and consolidated by Sweller, van Merriënboer, and Paas in 2019 — argues that sustained working memory engagement, the kind required when you are simultaneously holding audience profile, learning outcomes, chapter sequencing, and prerequisite structure, is finite and fatiguing under high element-interactivity load.[^sweller] A two-hour Tic TOC session is more cognitively demanding than two hours of drafting, because drafting draws on what you already know, while the specification session requires you to construct what you do not yet know you need. Take a break between phases. The session is dialogue, not deliverable.

[^sweller]: Sweller, J. (1988). "Cognitive Load During Problem Solving: Effects on Learning." *Cognitive Science*, 12(2), 257–285. Consolidated in Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). "Cognitive Architecture and Instructional Design: 20 Years Later." *Educational Psychology Review*, 31, 261–292.

The two-hour timebox is a heuristic, not a law. Ericsson's deliberate-practice research supports focused sessions of sixty to ninety minutes, though later meta-analysis by Macnamara and colleagues found deliberate practice explains less performance variance than the original work claimed — so lean on the figure lightly.[^ericsson] Two hours is long enough for sustained specification judgment and short enough that a working author will commit to it. Treat it as an estimate.

[^ericsson]: Ericsson, K. A., Krampe, R. T., & Tesch-Römer, C. (1993). "The Role of Deliberate Practice in the Acquisition of Expert Performance." *Psychological Review*, 100(3), 363–406. The major meta-analytic qualifier is Macnamara, B. N., Hambrick, D. Z., & Oswald, F. L. (2014), *Psychological Science*, 25(8), 1608–1618.

You will sometimes disagree with the prompt. You should. When Tic TOC pushes back on a domain-specific claim where your expertise exceeds the prompt's knowledge, override it. The phrase to use is: *"I am keeping this — here is why, in one sentence."* The prompt will accept the override, log the rationale, and continue. But notice the asymmetry: most of the time, when Tic TOC pushes back, it has caught something you did not see. The author who finishes in thirty minutes by accepting every first answer has not had a productive session. They have produced the appearance of a specification without the substance of one.

---

## One gate, in transcript

The most useful texture I can give you before your own session is a moment from the /i3 audience intake gate of the ai-for-designers session. This is what one phase-gate conversation actually looks like.

> **Tic TOC (/i3):** Who is the specific person you are writing for? Not the type of reader. A specific person you know — with a face, a job, and a current problem.
>
> **Author:** Freelance graphic designers who want to use AI without losing their professional identity.

That is a category. Watch what happens next.

> **Tic TOC:** That is a category. Can you name one designer in that category that you actually know — first name only is fine — and describe what they were working on this week?

The author paused for thirty seconds.

> **Author:** Okay. Maya. She has been freelance for nine years, mostly brand identity work. Her main client is a healthcare consultancy. She uses Photoshop and Figma daily, has a paid ChatGPT account, and used Midjourney once last month for a moodboard. She has been quietly worried for six months that her contracts are getting smaller. She has not raised her rates in two years because she does not know if AI is making her work easier or making her replaceable.
>
> **Tic TOC:** Good. One more probe. Maya has a paid ChatGPT account but only used Midjourney once. Why? Is this a learning curve problem, a confidence problem, a billing problem, or a "she hasn't needed it yet" problem? The answer matters because it tells me whether your book's Chapter 1 needs to be a tool tutorial, a permission conversation, a business case, or a defense against the fluency trap.

This is the curriculum theorist at work. The pushback is not about Maya's psychology. It is about what the chapter structure must address depending on which answer is true.

> **Author:** Confidence. She knows how to prompt. She does not know how to disclose AI use to her client without looking like she's cheating. So she uses it secretly for moodboards and refuses to use it for deliverables.
>
> **Tic TOC:** Confirmed. /i3 gate ready to mark passed. Your reader is Maya — nine-year freelance brand designer, one anchor healthcare client, paid ChatGPT, hesitant about disclosure. Do you confirm this as your primary learner profile, or do you want to revise?
>
> **Author:** Confirm.
>
> **Tic TOC:** Gate /i3 passed. Advancing to /i4 (thesis).

That exchange took roughly twenty minutes. It produced the learner profile that appears in Part 2 of the TIKTOC.md you read at the opening of this chapter. It established that Chapter 1 is a permission conversation, not a tool tutorial. It explains why Chapter 5 has a Create-level ceiling and a disclosure framework as its deliverable. One gate. Twenty minutes. The whole book's emotional center clarified.

The session has thirteen gates total. They do not all run this deep. Some confirm cleanly in two exchanges. But the ones that push back — the ones that return "that is a category, not a person" or "that verb is not demonstrable" — are the ones that are doing the work that the author cannot do alone.

---

## The five-minute setup

The deployment is mechanical. The session is not.

**Step 1.** Get the Tic TOC prompt. It is reproduced in full in Appendix A of this book — copy the entire contents from there. The latest maintained version lives at Bear Brown & Company's prompt library online; if it differs from the appendix, the online copy is newer.

**Step 2.** Create a Claude Project. In claude.ai, click *Projects* in the left sidebar, then *Create Project*. Name it specifically — *Tic TOC — [your working title]*. You will keep this project open across multiple sessions.

**Step 3.** Paste the prompt into the project's Instructions field. (Interface labels shift; these are current as of this writing.) Save.

**Step 4.** Upload or paste your domain research brief from Chapter 3 into Project Knowledge. Tic TOC references it during the domain-specific intake phases. On first read of this book, use `pantry/ai-for-designers-final-brief.md` as the running example.

**Step 5.** Start a new conversation in the project. Type `/help`. If the prompt is loaded correctly, a menu of commands appears. The first entries should include `/i1`, `/i2`, `/i3`, `/i4`, then `/l1` through `/l4`, then `/c1` through `/c4`, then `/g1`, `/g2`, `/p2`. If you do not see this menu, the prompt is not loaded. Re-paste into Instructions and start a fresh conversation.

**Step 6.** Type `/i1`. The session has begun.

Total setup time: five minutes. Total session time: roughly two hours, spread across one or two sittings depending on your domain and your tolerance for sustained specification work.

---

## What you are not doing yet

The session in this chapter — the five-minute setup, the one gate transcript, the list of what the gates catch — is preparation, not execution. The full session is Chapter 4.

What the session requires, and what you do not yet have, is the input: a synthesized domain research brief that gives Tic TOC something to push back against. If your first answer to `/i1` is "I'm not sure who my reader is," the pushback has nothing to grip. The session will stall not because the prompt failed but because the specification session requires raw material the same way a Cowork run requires a TIKTOC.md.

That raw material — the domain research brief — is what Chapter 3 walks you through producing. Chapter 3 is short, mechanical, and indispensable. It is the chapter that makes this one usable.

---

That raw material — the domain research brief — is what the next chapter walks you through producing. It is short, mechanical, and indispensable: the chapter that makes this one usable.

---

## Sources

1. Curtis, B., Krasner, H., & Iscoe, N. (1988). "A Field Study of the Software Design Process for Large Systems." *Communications of the ACM*, 31(11), 1268–1287. https://dl.acm.org/doi/10.1145/50087.50089
2. Wiggins, G., & McTighe, J. (1998; 2nd ed. 2005). *Understanding by Design.* ASCD. https://www.ascd.org/books/understanding-by-design-expanded-2nd-edition
3. Taba, H. (1962). *Curriculum Development: Theory and Practice.* Harcourt, Brace & World.
4. Gagné, R. M. (1965). *The Conditions of Learning.* Holt, Rinehart and Winston.
5. Anderson, L. W., & Krathwohl, D. R. (Eds.). (2001). *A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy of Educational Objectives.* Longman.
6. Mager, R. F. (1962; rev. 1997). *Preparing Instructional Objectives.* Center for Effective Performance.
7. Cooper, R. G. (1990). "Stage-Gate Systems: A New Tool for Managing New Products." *Business Horizons*, 33(3), 44–54. https://ideas.repec.org/a/eee/bushor/v33y1990i3p44-54.html
8. Sweller, J. (1988). "Cognitive Load During Problem Solving: Effects on Learning." *Cognitive Science*, 12(2), 257–285. https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1202_4
9. Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). "Cognitive Architecture and Instructional Design: 20 Years Later." *Educational Psychology Review*, 31, 261–292. https://link.springer.com/article/10.1007/s10648-019-09465-5
10. Ericsson, K. A., Krampe, R. T., & Tesch-Römer, C. (1993). "The Role of Deliberate Practice in the Acquisition of Expert Performance." *Psychological Review*, 100(3), 363–406. https://psycnet.apa.org/record/1993-40718-001
11. Macnamara, B. N., Hambrick, D. Z., & Oswald, F. L. (2014). "Deliberate Practice and Performance in Music, Games, Sports, Education, and Professions: A Meta-Analysis." *Psychological Science*, 25(8), 1608–1618. https://journals.sagepub.com/doi/10.1177/0956797614535810
