# Chapter 6 — Research Pass: Pantry Population

*The pantry is not a draft and it is not a citation list. It is the only thing standing between Cowork and an authoritative-sounding lie.*

---

Open `pantry/ch-03-domain-research.md`. The file looks substantial — nine sections, three pages, dozens of bullet points. Here is what four of those sections actually contain.

> **1. Primary Sources.**
> - According to a 2024 article, "AI is transforming graphic design" — most designers will need to adopt new tools or face displacement. *(source: a Medium post by an account with 3 followers; no further citation)*
> - "Studies show 78% of design firms are integrating AI." *(no study named; no year; no methodology)*
> - The McKinsey Global Institute has reported significant productivity gains from generative AI. *(no specific McKinsey report; no page; no figure)*

> **3. Application Domain Examples.**
> - Consider a marketing team using AI to write blog posts.
> - A small business owner could use ChatGPT to design a logo.
> - Educators are exploring how AI changes lesson planning.

> **9. Sourcing Notes.**
> Sources include articles from Forbes, Medium, LinkedIn, and a number of industry blogs. Primary sources were prioritized.

Read Section 9 again. *Primary sources were prioritized.* Section 1 has one primary source — a McKinsey reference too vague to find. The percentage in the second bullet has no study behind it. "Studies show" is not a citation; it is the grammatical form of a citation with the substance removed. Section 3 contains zero graphic designers. Section 9 claims to have prioritized primary sources while citing four aggregators.

This is the pantry file the Chapter Research Gatherer produced for a chapter about AI's impact on graphic design. In two days, Cowork will read this file and draft the chapter. It will produce something authoritative-sounding about AI and graphic design that cites no graphic designers, references a percentage no one can verify, and draws examples from marketing, small business, and education — every domain except the one the book is about.

Now read what the same chapter's pantry looks like after a forty-five-minute evaluation pass.

Section 1 names the Adobe Firefly 3 release notes from March 2024 with version-specific features sourced from Adobe's own release page, a peer-reviewed paper from *Journal of Design Research* on AI-augmented studio workflows, and the AIGA 2024 Design Census with methodology and sample size. Section 3 has five examples: a brand identity system for a regional law firm, an editorial layout for a quarterly magazine, a motion design project, a packaging redesign, a product lockup system — all graphic design, all specific. Section 9 names what was filtered out: Medium trend pieces, LinkedIn posts, listicles. The "Studies show" bullet is gone.

Same chapter. Same TIKTOC.md. Same Gatherer run. The difference is what happened after the script finished.

That difference is what this chapter is about.

---

## What the Gatherer does, and what it cannot do

The Chapter Research Gatherer is a Cowork prompt, not a separate piece of software. You give it the TIKTOC.md and a chapter spec file. For every chapter on the list, it does three things in order: reads the capability statement, learning outcomes, bridge question, and application domain; consults any shared library files in `pantry/` (files named with the `_lib_` prefix, covered below); then runs web research and writes a nine-section notes file. One file per chapter, saved as `pantry/research-ch-XX-<chapter-slug>.md`. Both research prompts — the Gatherer and the deeper Research Pass — are reproduced in Appendix D.

The nine sections are: Primary Sources, State of the Field, Application Domain Examples, Book's Thesis Connection, AI Wayback Machine Candidates, Pedagogical Delivery Research, Representation and Display Research, Open Questions and Research Gaps, Sourcing Notes.

This is a research synthesis task in Harris Cooper's sense. Cooper's 1982 framework for integrative research reviews named five stages: problem formulation, data collection, evaluation, analysis, presentation — and argued that compressing any stage was the move that hid the work.[^cooper] The Gatherer compresses Cooper's first three stages into one prompt. The two it cannot compress are evaluation and analysis. Those are yours. The four-questions pass described below is where Cooper's missing stages get re-added by hand.

[^cooper]: Cooper, Harris M. (1982). "Scientific Guidelines for Conducting Integrative Research Reviews." *Review of Educational Research*, 52(2), 291–302.

![A horizontal six-stage process flow along Cooper's review chain: problem formulation, data collection, and presentation grouped inside a machine band on the left, then a vertical dividing seam marking the machine-to-human hand-off, then evaluation and analysis inside a human band, ending in a draft-ready pantry-file terminal; machine stages tinted one color, human stages another.](images/06-research-pass-fig-01.png)
*Figure 6.1 — The Gatherer pipeline and where the human re-enters*

The Gatherer runs on a long-context model with retrieval — what has been called a "Deep Research" agent since the generation of tools Anthropic, OpenAI, and Google shipped between 2024 and 2025. Retrieval-augmented generation has moved citation fabrication down from the staggering rates measured in the first wave of generative models. When Bhattacharyya and colleagues had ChatGPT-3.5 generate thirty short medical papers in 2023, the references were a graveyard: the citation carried an incorrect PMID 93% of the time, a wrong volume or page number nearly two-thirds of the time.[^bhattacharyya] Walters and Wilder, looking across disciplines the same year, found GPT fabricating a substantial share of bibliographic citations outright.[^walters] Retrieval helps; recent benchmarks still report fabricated reference titles for a meaningful fraction of generated citations, and a few percent of cited URLs invented even in retrieval-augmented settings.[^chelli] The improvement is real. The risk is not gone.

There is a structural reason fabrication persists even with retrieval, and it is the same reason Bender and colleagues gave for calling a language model a "stochastic parrot": the model is trained to reproduce the *form* of text, not the act behind it.[^parrots] Extend that argument one step and the failure mode is obvious — a model can learn the surface shape of a citation, the author-year-title silhouette, without ever modeling what it means to open the source and check that it says what you claim. Citation-shaped text is cheap to generate. Verified citation is not. Someone must do the verification. The pantry evaluation pass is where that someone is you.

[^bhattacharyya]: Bhattacharyya, Mehul, et al. (2023). "High Rates of Fabricated and Inaccurate References in ChatGPT-Generated Medical Content." *Cureus*, 15(5), e39238.
[^walters]: Walters, William H., & Wilder, Esther Isabelle (2023). "Fabrication and errors in the bibliographic citations generated by ChatGPT." *Scientific Reports*, 13, 14045.
[^chelli]: Chelli, Mikaël, et al. (2024). "Hallucination Rates and Reference Accuracy of ChatGPT and Bard for Systematic Reviews: Comparative Analysis." *Journal of Medical Internet Research*, 26, e53164.
[^parrots]: Bender, Emily M., Gebru, Timnit, McMillan-Major, Angelina, & Shmitchell, Shmargaret (2021). "On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?" *FAccT '21*.

---

## Four questions before draft-ready

You will read each pantry file once. The goal is not an exhaustive audit — fifteen chapter files in one sitting would make exhaustive impractical. The goal is a sharp triage. Mike Caulfield's SIFT method gave undergraduates four moves: Stop, Investigate the source, Find better coverage, Trace claims.[^sift] The CRAAP test gave five criteria: Currency, Relevance, Authority, Accuracy, Purpose.[^craap] Both are too many to apply habitually across an entire pantry. The four below are adapted from SIFT, sharpened for AI-generated research notes, and designed to fit in five to seven minutes per file.

[^sift]: Caulfield, Mike (2017). *Web Literacy for Student Fact-Checkers*. CC-BY.
[^craap]: Blakeslee, Sarah (2004). CSU Chico Meriam Library. CRAAP Test.

**Question 1 — Is the strongest source primary or secondary?**

Open Section 1. Find the source the Gatherer is leaning on most. Is it a study, a release note, a dataset, a court ruling, an organization's own publication — or is it an article *about* a study, a blog post summarizing a report, a trend piece? If the strongest source in Section 1 is a Medium post or a Forbes article, the chapter is thin even if every other section looks full. A thin Section 1 means Cowork will draft on summaries of summaries. The derivatives compound. The chapter that results sounds authoritative and cites nothing anyone can find.

**Question 2 — Do the domain examples match your reader?**

Open Section 3. Count the examples. Count the ones in your actual domain. If the book is for graphic designers and Section 3 contains marketing, small business, and education examples, the Gatherer found related content but missed the target. This is the most common failure pattern and the easiest to miss, because the examples *sound* relevant — they involve creative work, or visual content, or working with clients. They are not about graphic design. The domain drift operates exactly like the fluency trap: the output has the right shape without the right substance, and the gap only becomes visible when a reader who knows the field opens the page.

**Question 3 — Is anything flagged `[verify]` or `[contested]`?**

Search the file. The Gatherer is instructed to flag any claim it could not source confidently. If the file contains zero flags, that is a yellow flag in itself. Either the chapter covers genuinely well-documented ground or the Gatherer is more confident than the evidence warrants. Sycophancy in long-context models is a measured phenomenon — one of its forms is producing fewer uncertainty markers than the topic deserves.[^sycophancy] A pantry file with no flags is not necessarily a clean pantry file. It may be a pantry file that did not notice what it did not know.

[^sycophancy]: Sharma, Mrinank et al. (2023). "Towards Understanding Sycophancy in Language Models." Anthropic preprint.

**Question 4 — Would a peer in your domain recognize these sources?**

This is the read-aloud test. If you texted Section 1 to your most demanding colleague, would they nod or wince? Practitioners have fast and accurate instincts about what counts as a source in their field. Designers can tell instantly whether a "designer source" was written by a designer. Clinicians can tell instantly whether a "medical source" was written by a clinician. This instinct is the thing the Gatherer does not have. It is the thing you have. Use it.

Four questions. Five to seven minutes per pantry file. Two hours for fifteen chapters, with attention left over.

If all four answers are good: draft-ready. Move on. If any answer fails: thin. The next section gives you the three responses.

| Question | What to open | Pass condition | Fail signal | Common failure pattern |
|---|---|---|---|---|
| 1 — Is the strongest source primary or secondary? | Section 1, Primary Sources | The leading source is a study, dataset, release note, ruling, or an organization's own publication | The strongest source is a Medium post, Forbes article, or trend piece | Section drafts on summaries of summaries; derivatives compound |
| 2 — Do the domain examples match your reader? | Section 3, Application Domain Examples | Most examples sit squarely in the book's actual domain | Examples come from adjacent fields — marketing, small business, education | Domain drift: right-shaped output, wrong substance, only visible to a peer |
| 3 — Is anything flagged `[verify]` or `[contested]`? | Whole file (search) | Uncertainty is marked where confidence wavered | Zero flags across the file | Sycophantic over-confidence: fewer uncertainty markers than the topic deserves |
| 4 — Would a peer in your domain recognize these sources? | Section 1, read aloud | A demanding colleague would nod | A demanding colleague would wince | Sources sound field-adjacent but were not written by practitioners in the field |

---

## What thin means, and the three responses

Thin pantry has three causes. The cause determines the response, and picking the wrong response wastes either an hour of supplementation work on a problem that required a different fix, or weeks of Cowork drift on a problem that required supplementation.

**Cause A: the research was hard.** The topic is recent, niche, or contested. The Gatherer found two reasonable sources and flagged a third. Section 3 has three good domain examples and two stretches. This is a *supplementable* chapter. Open Google Scholar, your professional association's publications, the trade press in your domain. Forty-five minutes. Add two primary sources to Section 1 by hand. Replace the stretched examples in Section 3 with ones you have lived. The pantry becomes draft-ready before the hour is up.

**Cause B: the field evidence is genuinely thin.** This happens. The Gatherer cannot find what does not yet exist. AI's effect on a specific freelance niche may be reported only in trade newsletters. Case law on a contested claim may be too recent. Qualitative effects that practitioners know from experience may not yet be formalized in anything citable. This is an *accept-with-flag* chapter. Add a banner to the pantry file:

```
[contested — see pantry flag]
Field evidence on this topic is thin. The chapter will rely on
the author's domain experience and will be flagged in risks.md
as a contested claim.
```

Cowork will draft carefully. The author will know to be especially careful in the human rewrite. The chapter ships with eyes open rather than eyes closed.

**Cause C: the TIKTOC.md was vague.** The Gatherer could not fix what the spec did not ask for. Section 1 wanders. Section 3 is generic. Section 8 — Open Questions — is short because the Gatherer did not know what was missing. This is a *return-to-Tic-TOC* chapter. Open `/c1` again. Rewrite the capability statement until it names a specific, demonstrable action. Sharpen the application domain. Then rerun the Gatherer for that chapter alone. A hopeless pantry is a downstream signal of a broken spec. The fix is upstream.

The decision is short enough to memorize:

```
Pantry file thin?
   ├── Topic is hard       → Supplement by hand (45 min)
   ├── Field evidence thin → Accept with flag, mark in risks.md
   └── TIKTOC.md vague     → Return to /c1, sharpen spec, rerun Gatherer
```

![A left-to-right decision tree: one root node "pantry thin?" branching into three cause nodes — topic hard, field evidence thin, TIKTOC.md vague — each routing by a single arrow to one paired response on the right: supplement by hand, accept with flag into risks.md, and return to /c1; the return-to-/c1 response carries an upstream back-loop arc.](images/06-research-pass-fig-02.png)
*Figure 6.2 — Thin-pantry triage: three causes, three responses*

Write the choice in `risks.md`. Future-you, four chapters deep in the human rewrite, will need to remember which chapters were accepted with flags and why.

---

## The shared markdown library

Some content recurs across chapters: the glossary, the recurring framework definitions, the book's house position on contested claims. Repeating this content in every pantry file wastes space and — worse — lets the content drift. Two chapters citing the same definition with one-word differences confuse the reader in ways that are hard to trace and hard to fix.

The Pragmatic Programmer's DRY principle applies: every piece of knowledge has a single authoritative home.[^pragprog] In the AI+1 scaffold, that home is any file in `pantry/` whose name starts with `_lib_`. The glossary lives in `_lib_glossary.md`. The AI+1 framework definition lives in `_lib_ai-plus-one-frame.md`. The house position on contested claims lives in `_lib_contested-claims.md`.

[^pragprog]: Hunt, Andrew and David Thomas (2019). *The Pragmatic Programmer*, 20th Anniversary Edition. Addison-Wesley.

The Chapter Research Gatherer reads `_lib_` files before generating chapter-specific notes. Anything in `_lib_` is shared context. The Gatherer does not duplicate it into chapter pantry files; it references the definition and moves on. When the Chapter Writer runs in the next chapter, it consults `_lib_` files the same way. When you update a definition once, every subsequent run sees the update.

What belongs in `_lib_`: terms used across more than two chapters, framework definitions, the book's position on contested claims, style notes that apply everywhere, author bio. What does not belong: chapter-specific examples, citations specific to one chapter's topic, per-chapter image briefs. The line is between what is shared and what is particular.

![A radial hub-and-spoke diagram: a central _lib_ hub node with four to five chapter pantry-file nodes arranged around it, each connected by a reference arrow pointing from the hub into the chapter file — the definition flowing outward from a single authoritative source, so one update at the hub propagates along every arrow.](images/06-research-pass-fig-03.png)
*Figure 6.3 — The `_lib_` shared library: one authoritative home*

| File | Contents | When the Gatherer reads it | Update trigger |
|---|---|---|---|
| `_lib_glossary.md` | Terms used across more than two chapters, with one authoritative definition each | Before generating any chapter's notes | A term's meaning changes or a new cross-chapter term appears |
| `_lib_ai-plus-one-frame.md` | The AI+1 framework definition the whole book leans on | Before every chapter run | The framework's articulation is sharpened or revised |
| `_lib_contested-claims.md` | The book's house position on claims that are disputed in the field | Before every chapter run | New evidence shifts the house position on a contested claim |
| `_lib_style.md` | Style notes and author bio that apply everywhere | Before every chapter run | Voice or house-style guidance changes book-wide |

---

## Pantry is not citation

This is the section the chapter most wants to get right, because the distinction it draws is the one that collapses most easily under time pressure.

The pantry is reference, not citation. The distinction is the same one every designer already knows from moodboard practice. A moodboard is what you consult while working — competitive references, texture samples, typographic directions, visual precedents. You may have looked at two hundred references while developing a brand identity. You cite none of them in the deliverable. The references shaped your judgment; the deliverable carries your judgment, not the references.

The pantry plays the same role for chapter drafting. Cowork consults it while drafting. The chapter draft does not cite the pantry. Chapter drafts cite primary sources. If a chapter draft says "according to a 2024 article" without naming the article, that draft is citing the pantry — which means the claim was sourced from the Gatherer's notes rather than traced back to a primary source. The human rewrite must then trace the claim through the pantry to the original source and either cite it properly or remove it. This is the AI-laundered citation pattern. The pantry structure is the defense against it, but only if the defense is maintained in the rewrite.

Sönke Ahrens's *How to Take Smart Notes* describes the same distinction in a different vocabulary.[^ahrens] Niklas Luhmann's Zettelkasten — the 90,000-card archive that produced 70 books and 400 papers — had three layers: fleeting notes taken in the moment, literature notes recording what a source actually said, and permanent notes carrying the writer's own argued claim. Pantry files are Ahrens's literature notes. Chapter drafts are permanent notes. Treating literature notes as if they were already permanent — cutting from the Gatherer's prose into the chapter without tracing back to the primary source — is what produces academic embarrassment in human writers and hallucinated citations in language models. The fix is structural: keep the layers separate.

![A vertical three-tier stack — fleeting notes at the base, literature notes (the pantry) in the middle, permanent notes (the chapter draft) at the top — with a correct-path arrow routing from the literature layer through a primary-source waypoint up to the permanent layer, and a second arrow attempting to skip the waypoint terminated by a blockage glyph marking the forbidden AI-laundered citation shortcut.](images/06-research-pass-fig-04.png)
*Figure 6.4 — Three note layers: literature notes vs. permanent notes*

It is worth pausing on who Luhmann was, because the lesson is in the dullness of the method. He was a German sociologist who, over roughly thirty years, built a personal archive of about ninety thousand paper slips, indexed by a numeric code he invented and cross-referenced by hand, and out of that wooden cabinet produced seventy books and more than four hundred scholarly papers — an output that has never been credibly explained by anything other than the system itself. His claim was that the thinking happens in the notes, not in the head and not in the draft. The finished books are downstream of the Zettelkasten in exactly the way chapter drafts are downstream of the pantry: a thin slip-box produces thin books, and a thin pantry produces thin chapters no matter how hard the human rewrites later.

The analogy is not perfect, and the place it breaks is instructive. Luhmann wrote every slip himself; the discipline was inseparable from the writing. The pantry outsources the *gathering* to a machine and reserves only the evaluation for the human — which is precisely why the evaluation pass has to be defended so deliberately. Luhmann could not skip the thinking, because there was no one else to do it. You can. That is the disanalogy, and it is the whole reason this chapter exists.

The deeper point is that Luhmann's system was boring. Index cards, a wooden cabinet, a numbering scheme. No magic. The infrastructure was simple and the practice was relentless. The pantry is the same way. The technology is unimpressive. The discipline of evaluating each file before letting Cowork read it is the entire game.

[^ahrens]: Ahrens, Sönke (2017). *How to Take Smart Notes*. North Star Media.

---

## The annotated pantry — Chapter 3 of ai-for-designers

This is the pantry file for Chapter 3 of the running example after the Gatherer ran and after the forty-five-minute supplementation pass. Strong and weak entries are annotated so the evaluation logic is visible in operation.

```
# Research: Chapter 03 — Domain Research
# AI+1: AI Native Personalized Textbooks
Chapter one-line: Students write, run, and synthesize a structured
domain research prompt across three LLMs.
Research date: 2026-05-28

## 1. Primary Sources

[STRONG] Adobe Firefly 3 release notes, March 2024 — Adobe Inc.
Specific features named with version numbers; sourced from Adobe's
own release page. URL preserved.

[STRONG] Hoffmann, M. and Wallace, B. (2023). "Generative AI in
Studio Workflows: An Ethnography of Three Design Practices."
Journal of Design Research, 17(2). Peer-reviewed.

[WEAK — REPLACED] "According to a 2024 trend report, AI adoption
in design is growing." [no source named, percentage unattributed —
removed during supplementation pass]

[STRONG, ADDED MANUALLY] AIGA 2024 Design Census. URL, methodology,
and sample size named. Added by hand after Gatherer missed it.

## 2. State of the Field

[STRONG] What is settled: generative tools are now in every major
design software suite (Adobe, Figma, Canva). What is disputed:
whether AI augments or displaces senior designers. Cite Hoffmann
& Wallace 2023 (augmentation) and Davis 2024 op-ed (displacement).
[verify — Davis op-ed publication venue]

## 3. Application Domain Examples

[STRONG] Five examples, all from graphic design:
(1) Brand identity system for a regional law firm — designer used
Midjourney for moodboarding only, hand-drew the final mark.
(2) Editorial layout for a quarterly magazine — Adobe Firefly used
for stock image generation; layout decisions human.
(3) Motion design for a product launch — AI-assisted storyboarding,
hand-crafted final animation.
(4) Packaging redesign — Figma AI used for variation generation,
typography hand-set.
(5) Product lockup system — generative tools for exploration;
production all manual.

[REMOVED] Marketing teams using AI for blog posts. Small business
owners using ChatGPT for logos. Wrong domain — removed during
evaluation pass.

## 4. Book's Thesis Connection

The fluency trap is most visible in Section 3 examples. AI tools
produce design-shaped output without design judgment. The chapter's
domain research must surface this distinction by example, not claim.

## 5. AI Wayback Machine Candidates

[STRONG] Lead: Paula Scher (1948–). Pentagram partner. Known for
City Opera, MoMA identities. Substantive connection: Scher's career
is the case that design is judgment, not output.

Alternate: Massimo Vignelli (1931–2014). Italian-American designer.
The NYC Subway map. Quote: "If you can design one thing, you can
design everything." Counter-position to AI's generic competence.

## 6. Pedagogical Delivery Research

[STRONG] Three-LLM comparison as cognitive contrasting case
(Schwartz & Bransford 1998). Reading three drafts side by side
makes divergence visible.

## 7. Representation and Display Research

[STRONG] Three-column side-by-side of LLM outputs. Color-coded
agreement/divergence. Designers read color-coded tables natively.

## 8. Open Questions and Research Gaps

- Does Hoffmann & Wallace 2023 have a follow-up study? [verify]
- AIGA 2025 census not yet published; cite 2024 with date stamp.
- Davis op-ed venue uncertain. [verify before draft]

## 9. Sourcing Notes

Primary: Adobe release notes, Hoffmann & Wallace 2023, AIGA 2024.
Avoided: Medium trend pieces, LinkedIn posts, design-tool listicles.
The chapter's source list is the chapter's seriousness.
```

Notice what is missing that the bad version had: unverifiable percentages, the "Studies show" construction, examples from wrong domains. Notice what is present: specific titles, version numbers, peer-reviewed citations, explicit `[verify]` flags where confidence wavered. This is a literature-notes layer in Ahrens's sense. Cowork can draft from this without inventing. That is the only standard the pantry file needs to meet.

---

## What the pantry makes possible downstream

A pantry file is not interesting in itself. Its interest is entirely in what happens two chapters later, when Cowork opens it and drafts.

The Cowork output from the bad pantry produces a chapter that uses the "Studies show 78%" figure as if it were settled. It uses the McKinsey reference in a sentence that sounds specific and cites nothing findable. It includes a worked example about a small business owner using ChatGPT to design a logo — which is not the reader, not the domain, not the book's argument. The human rewrite in Chapter 8 must find these problems, trace each claim back through the pantry to its non-existent source, and either find a real source or remove the claim. This is expensive. It is the upstream defect propagating downstream — the pattern Curtis, Krasner, and Iscoe documented when they watched large software projects fail: a thin spread of application-domain knowledge, requirements that drift, communication that breaks down, and the defect from the design stage surfacing only when someone tries to build on it.[^curtis] Barry Boehm put a number on what that costs. His software-economics work argued that a defect left in the specification can cost on the order of ten to a hundred times more to fix once it has propagated to implementation.[^boehm] The exact multiplier is contested in the software-engineering literature, and you should hold it loosely — but the direction is not in dispute, and it is the direction that matters here: catch it early or pay compounding interest later.

The Cowork output from the good pantry opens with a specific scene drawn from one of the five domain examples in Section 3. It cites the Hoffmann and Wallace 2023 study when it makes a claim about studio workflows. It flags the contested question — augmentation versus displacement — without resolving it falsely. It puts a `[verify]` marker in the draft where the Davis op-ed venue is uncertain, which the human rewrite can resolve in five minutes. The rewrite is tightening and adding voice, not hunting ghosts.

[^curtis]: Curtis, B., Krasner, H., & Iscoe, N. (1988). "A Field Study of the Software Design Process for Large Systems." *Communications of the ACM*, 31(11), 1268–1287.
[^boehm]: Boehm, Barry W. (1981). *Software Engineering Economics*. Prentice-Hall; see also Boehm & Basili (2001), "Software Defect Reduction Top 10 List," *IEEE Computer*, 34(1), 135–137. The relative-cost-of-change curve is widely cited and also widely contested.

The difference is the pantry evaluation pass. Two hours of five-to-seven minutes per file. The cost at specification is a single afternoon. The cost at rewrite, without it, is a week.

Padmakumar and He gave this an empirical underpinning in 2024.[^padmakumar] They had people write with language models and then measured the result, and the finding was directional and clear: writing with a feedback-tuned model produced a statistically significant reduction in content and lexical diversity — the texts grew more alike, the vocabulary narrowed — while a base model did not show the same effect. When a model is given thin research infrastructure and asked to draft authoritatively, it converges on the cheap citation forms that make up most of its training data. A well-constructed pantry file is not a constraint on Cowork's output — it is the input that makes a specific, non-generic output possible. The model will converge on what it is given.

[^padmakumar]: Padmakumar, Vishakh, & He, He (2024). "Does Writing with Language Models Reduce Content Diversity?" *ICLR 2024*. arXiv:2309.05196. The diversity reduction is significant for instruction-tuned models; the magnitude is best read from the paper's results rather than stated as a single headline percentage.

---

## A few open questions

A few things about the pantry are genuinely unsettled, and it is more honest to name them than to paper over them.

Whether there is a recommended maximum pantry size per chapter is open. Liu and colleagues' 2024 "Lost in the Middle" finding — that language models systematically under-attend to content in the middle of long contexts — suggests that very long pantry files may produce partially ignored research.[^lost] In practice, three to five pages per chapter pantry file seems to hit the useful range, and longer files are probably better split into `_lib_` references plus a thinner chapter-specific file. Read that as author experience, not as a measured constant; the exact context-window behavior of the Chapter Writer prompt is an internal-tool detail that should be checked against your own runs rather than trusted from a book.

Whether the Gatherer produces URLs or full bibliographic entries by default is a mix, and which is better depends on where you are publishing. Authors shipping to Substack alongside Kindle tend to benefit from URLs; authors planning print citations benefit from full entries. The Gatherer can be instructed to prefer one, and the cleanest move is to set that preference explicitly rather than rely on whatever the default happens to be in the version you are running.

Whether the Gatherer infers the reader's domain from the TIKTOC.md or needs it stated explicitly is worth testing for niche subfields. Authors in medical illustration, scientific publishing, and motion design sometimes get better Section 3 results by adding an explicit domain hint to the Gatherer prompt. Treat that as a user-discovered workaround, not a documented feature.

[^lost]: Liu, Nelson F., et al. (2024). "Lost in the Middle: How Language Models Use Long Contexts." *Transactions of the Association for Computational Linguistics*, 12, 157–173.

---

## Sources

- Cooper, Harris M. (1982). "Scientific Guidelines for Conducting Integrative Research Reviews." *Review of Educational Research*, 52(2), 291–302. The five stages: problem formulation, data collection, evaluation, analysis, presentation. https://journals.sagepub.com/doi/10.3102/00346543052002291
- Bhattacharyya, Mehul, et al. (2023). "High Rates of Fabricated and Inaccurate References in ChatGPT-Generated Medical Content." *Cureus*, 15(5), e39238. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10277170/
- Walters, William H., & Wilder, Esther Isabelle (2023). "Fabrication and errors in the bibliographic citations generated by ChatGPT." *Scientific Reports*, 13, 14045. A cross-disciplinary measurement of citation fabrication. https://www.nature.com/articles/s41598-023-41032-5
- Chelli, Mikaël, et al. (2024). "Hallucination Rates and Reference Accuracy of ChatGPT and Bard for Systematic Reviews: Comparative Analysis." *Journal of Medical Internet Research*, 26, e53164. https://www.jmir.org/2024/1/e53164
- Bender, Emily M., Gebru, Timnit, McMillan-Major, Angelina, & Shmitchell, Shmargaret (2021). "On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?" *FAccT '21*, 610–623. https://dl.acm.org/doi/10.1145/3442188.3445922
- Sharma, Mrinank, et al. (2023). "Towards Understanding Sycophancy in Language Models." arXiv:2310.13548 (Anthropic). https://arxiv.org/abs/2310.13548
- Liu, Nelson F., et al. (2024). "Lost in the Middle: How Language Models Use Long Contexts." *Transactions of the Association for Computational Linguistics*, 12, 157–173. https://aclanthology.org/2024.tacl-1.9/
- Padmakumar, Vishakh, & He, He (2024). "Does Writing with Language Models Reduce Content Diversity?" *ICLR 2024*. arXiv:2309.05196. https://arxiv.org/abs/2309.05196
- Boehm, Barry W. (1981). *Software Engineering Economics*. Prentice-Hall. The origin of the relative-cost-of-change figure (widely cited and contested).
- Curtis, Bill, Krasner, Herb, & Iscoe, Neil (1988). "A Field Study of the Software Design Process for Large Systems." *Communications of the ACM*, 31(11), 1268–1287.
- Cooper, Harris M. — see above.
- Ahrens, Sönke (2017). *How to Take Smart Notes*. North Star Media.
- Hunt, Andrew, & Thomas, David (2019). *The Pragmatic Programmer*, 20th Anniversary Edition. Addison-Wesley.
- Caulfield, Mike (2017). *Web Literacy for Student Fact-Checkers* (the SIFT method). CC-BY.
- Blakeslee, Sarah (2004). The CRAAP Test. CSU Chico Meriam Library.
- Luhmann, Niklas (1927–1998), and the Zettelkasten — roughly 90,000 slips, 70 books, 400+ papers over some thirty years of academic life. https://en.wikipedia.org/wiki/Niklas_Luhmann
