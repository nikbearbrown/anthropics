# Chapter 15 — The Complete Pipeline: One Brief, Every Decision

**[FINAL PROJECT]**

## Learning objectives

By the end of this chapter you will be able to:

1. (Create) Produce a complete infographic production package: brief, SCOPE specification, `DESIGN.md`, `CLAUDE.md`, `PROJECT.md`, generated SVG, Illustrator-corrected `.ai`, and 300 DPI PNG.
2. (Evaluate) Apply the CAJAL blur test, the WCAG contrast check, and the grayscale test to the final output.
3. (Evaluate) Defend every encoding decision — mark, channel, color token, font role, annotation placement, layout type — in a 10-minute design review.
4. (Create) Produce the final AI Use Disclosure: three design decisions across the complete pipeline that required human judgment no AI tool could supply.

---

## Opening: what does "done" look like?

Before you start the final project, you should see a finished one. Not a description of one — a finished package, opened folder by folder, so the target is concrete before you aim at it.

Here is a complete production package for a public-health figure produced by a previous cohort. The brief was three sentences from a city health department: *show how the gap between two neighborhoods' asthma-ER-visit rates widened over a decade, for a council briefing. The data are real and the disparity is the story. Do not let the figure be alarmist beyond what the data support.* The folder looks like this:

```
asthma-disparity/
├── BRIEF.md              ← the 3-sentence ask, plus the audience and medium
├── PROJECT.md            ← Intent Layer + Schema Layer (audit output)
├── DESIGN.md             ← seven tokens, three-font stack, layout type
├── CLAUDE.md             ← D3 v7 coding constitution
├── scope.md              ← CAJAL SCOPE: S/C/O/P/E for this figure
├── data/asthma-er.csv    ← source data
├── asthma-disparity.svg  ← generated, spec-driven, metadata embedded
├── asthma-disparity.ai   ← Illustrator-corrected; clips released; named layers
├── asthma-disparity.png  ← 300 DPI, derived from source
├── DISCLOSURE.md         ← three human-judgment decisions named
└── DEFENSE.md            ← one-page defense of every encoding decision
```

Open `DEFENSE.md` and you find a sentence for every visual choice: *the two neighborhoods are encoded as position on a common scale (Cleveland–McGill's most accurate channel), not as area, because the council must compare magnitudes precisely; the widening gap is the single emphasis, so the accent token appears exactly once, on the gap itself; the y-axis begins at zero because a truncated axis would make the disparity look larger than it is, and "do not be alarmist beyond the data" is in the brief.* Every line is a decision the student can defend against a skeptic.

That is "done." Not a pretty PNG. A package where every artifact traces back to a decision, and every decision traces back to the brief. Your final project is to produce one of these, for a domain problem you choose. This chapter is the assembly instructions — and the assembly is nothing more than running the four phases you already know, end to end, without skipping.

![A traceability tree rooted at BRIEF.md branching to the package files (scope, governing files, the source SVG with its derived .ai and .png) and an evidence column where DISCLOSURE.md names the three human-judgment decisions.](images/15-the-complete-pipeline-one-brief-every-decision-fig-02.png)

*Figure 15.2 — The production package as the infographic's datasheet: every artifact traces to a decision, and DISCLOSURE.md is the proof the human owned the judgment.*

---

## The whole pipeline, in one view

You have built each phase in isolation. Here it is as one process, with the human-judgment act named at every step. This is the spine of the book made operational.

| Phase | Chapter | What the agent does | What only you can do |
|---|---|---|---|
| **(Design)** | 1–10 | — | Author the SCOPE: claim, encoding, exclusions, layout |
| **Audit** | 12 | Inventory files, extract hex, find anonymous groups | Decide what counts as a *gap*; quarantine unknown files |
| **Generate** | 13 | Render the spec into D3/SVG, unit by unit | Decide axis-zero, color ceiling, what earns the accent |
| **Verify** | 14 | Extract structure; measure contrast | Decide ship / no-ship against the spec |
| **Handoff** | 14 | Rasterize at 300 DPI; release clips mechanically | Decide the imported position is *wrong*; own "correct" |

Read the right-hand column top to bottom. That column is the design-intelligence layer — the part this book insists is irreducibly human. [High — book's thesis] The agent's column is execution: real, valuable, fast, and incapable of supplying a single entry on the right. The final project is the proof that you can run the left column with an agent while owning the right column yourself.

![Five pipeline phases shown as a top lane of neutral agent-execution tasks above a connected red human-judgment spine, with three judgment points marked: what counts as a gap, axis-zero and color ceiling, and the imported position is wrong.](images/15-the-complete-pipeline-one-brief-every-decision-fig-01.png)

*Figure 15.1 — The complete pipeline in one view: the agent runs the execution lane, while the irreducibly-human-judgment spine runs beneath, with three decision points marked.*

A note the field has learned recently, and that the package format answers: *the artifact alone no longer proves the human made the decisions.* [Medium — current-state observation] A clean SVG could have come from a careful designer or from a lucky bare prompt. This is why the package includes `DISCLOSURE.md` and `DEFENSE.md`. They are the evidence that the right-hand column was you. The documentation models the field built for AI systems — datasheets, model cards, data statements — exist for exactly this reason: to make provenance, intended use, and limitations explicit when the artifact cannot speak for itself. [High] Your production package is an infographic's datasheet.

---

## Running the pipeline: one brief, every decision

Let us walk the asthma-disparity package through the phases, so the assembly is concrete.

### Design (the SCOPE)

Three brief sentences become a SCOPE specification. **Specification:** a two-line slope/gap chart, ER visit rate per 10,000 by neighborhood, 2014–2024. **Content:** two neighborhoods (lines), the gap (the emphasis), years on x, rate on y. **Organization:** single panel, long-form caption; gap callout at the most recent year. **Presentation:** Brutalist — EB Garamond headline, Inter caption, JetBrains Mono ticks, ink on paper, accent once on the gap. **Exclusions** — the highest-leverage line: *no axis truncation; no third color; no area fill (which would imply a volume the data do not measure); no projection beyond 2024.*

The Exclusions are where the brief's "do not be alarmist" lives. "No axis truncation" and "no projection" are how that human instruction becomes a machine-checkable constraint. This is the design-intelligence layer doing its irreducible work: translating an editorial value into a specification an agent can execute against.

### Audit

The project directory has last term's template SVG and a partial `DESIGN.md`. The audit inventories them, finds the template uses a truncated axis (a gap against this figure's exclusions), and quarantines it — you will not inherit the truncation. Gate: Intent populated (brief approved), Schema populated (audit done), `DESIGN.md` complete. Open.

### Generate

Unit by unit, against `CLAUDE.md`: named layer scaffold (painter's order); scales with y from zero; two lines as token-colored paths via `.attr()`; the gap as the single accent; direct labels, no legend; CAJAL metadata block recording the claim and the exclusions. Each unit verified before the next. Zero hand corrections.

### Verify

The four-category human pass. Structure: painter's order intact. Text: real `<text>`, three-font stack, anchors set. Styling: tokens only, contrast measured at 5.1:1 on the caption, no opacity compounding. Naming: semantic, no `_x31_`. The metadata says `AXIS: y=0`; the figure confirms it. Ship — but first, handoff.

### Handoff

Open in Illustrator. Release the one clip on the plot area. The named layers imported under an unnamed wrapper; ungroup it, keep the names. The gap callout drifted on import (the `text-anchor` mismatch); re-align to the spec. Save `.ai`. Run `node SCRIPTS/svg-to-png.mjs --in asthma-disparity.svg --out asthma-disparity.png --dpi 300` from the source. Done.

Every decision in that walk-through has an owner. The agent owns the rendering. You own the axis, the color count, the exclusions, the ship call, and the correction of the drift. The package records both columns.

---

## The three final checks

Before the package is done, it passes three tests you have used throughout the book, now applied to the finished figure.

- **The blur test (Chapter 9).** Squint at the figure, or view it at low resolution. The headline, the two lines, and the gap callout should remain a visible three-level hierarchy when the detail blurs out. If everything blurs to one gray mass, the hierarchy is decorative, not structural. The asthma figure passes: the gap callout's single accent survives the blur because it is the only chromatic element.
- **The grayscale test (Chapter 5).** Convert to grayscale. The two lines must remain distinguishable by luminance, not only by hue — because color-blind readers and grayscale printers exist, and because a distinction that survives grayscale is a distinction the perceptual system can recover reliably. The figure passes: the two neighborhoods differ in luminance, not just hue, and the accent is a luminance step as well as a color.
- **The WCAG contrast check (Chapter 8).** Measure every text element against its background; all must clear 4.5:1. Measured, not eyeballed. The caption at 5.1:1 passes; had it failed, the fix would be a token swap, not a redesign — because the design system was built to pass.

A figure that fails any of these goes back a phase. It does not ship with a known failure and a promise to fix it later. "Later" is the failure mode this entire book is written against.

---

## The design review: defending every decision

The final project includes a 10-minute design review, because a figure you cannot defend is a figure you do not understand. The protocol:

1. **Brief (1 min).** State the ask, the audience, the medium.
2. **Specification (2 min).** Walk the SCOPE, ending on the Exclusions — *especially* the exclusions, because what you left out is the highest-leverage decision and the one a skeptic will probe.
3. **Output (2 min).** Show the figure and the package.
4. **Three encoding decisions defended (5 min).** The reviewer picks three — mark, channel, color token, font role, annotation placement, layout type — and you defend each against an alternative. Not "it looked better." A defense in the language of the book: *position on a common scale because the task is precise magnitude comparison and it is Cleveland–McGill's most accurate channel; the alternative — area — would degrade comparison accuracy and imply a volume the data do not measure.*

A defense that reduces to taste fails the review. A defense grounded in perceptual accuracy, cognitive load, the design system, or the brief passes. The review is the empirical test of the book's thesis: if the design-intelligence layer were not irreducibly human, you would not need to defend it, because the agent could.

---

## The AI Use Disclosure: three decisions, the highest bar

Every deliverable in this course required a disclosure naming at least two human-judgment decisions. The final project raises the bar to **three, across the full production process** — and they must be genuinely distinct, spanning the pipeline, not three flavors of the same call.

A strong final disclosure for the asthma package names one decision from different phases:

1. **A design decision (SCOPE phase).** *I excluded axis truncation and forward projection, translating the brief's "do not be alarmist beyond the data" into specification constraints. The agent had no access to the editorial value behind that instruction; it would have produced a truncated axis if asked for "impact," because impact and truncation correlate in surface plausibility.*
2. **An encoding decision (Generate phase).** *I capped the figure at two data colors and assigned position-on-common-scale rather than area. This is a perceptual-accuracy judgment from Cleveland–McGill that the agent could execute but not originate, because originating it requires knowing the comparison task the council must perform.*
3. **A verification/handoff decision (Verify/Handoff phase).** *I judged the imported gap-callout position wrong and re-aligned it to the spec, and I decided the 5.1:1 caption contrast was acceptable for a printed council briefing. Both required holding the artifact to a standard the tools measure but cannot set.*

Three decisions, three phases, three distinct kinds of judgment. That is the disclosure the final project requires. It is also, not incidentally, the clearest possible articulation of what you have learned: the precise locations in an AI-assisted pipeline where the human is irreducible. A student who can name those three locations has internalized the book's argument more thoroughly than any exam could test.

---

## Assessment: Final Project (250 points)

**Task.** Produce a complete infographic production package for a real domain problem of your choosing — your own research, work, or a public-interest dataset — and defend it in a 10-minute design review.

**Deliverables (the package).**

1. **`BRIEF.md`** — the ask, audience, and medium, in the spirit of a real client brief. [15 pts]
2. **`scope.md`** — the complete CAJAL SCOPE (S/C/O/P/E), with the Exclusions list explicitly justified. [30 pts]
3. **`DESIGN.md`, `CLAUDE.md`, `PROJECT.md`** — the three governing files, `PROJECT.md` showing both a populated Intent Layer and a Schema Layer from a real Audit. [30 pts]
4. **`asthma-style` generated SVG** — spec-driven, with the CAJAL metadata block embedded; passes the four-category `CLAUDE.md` checklist. [40 pts]
5. **Corrected `.ai` (or Inkscape source)** — clips released, named layers reconciled, text alignment corrected; demonstrably editable by a production team. [30 pts]
6. **300 DPI PNG** — derived from the source via `svg-to-png.mjs`, DPI declared. [15 pts]
7. **Three final checks** — documented results of the blur test, grayscale test, and WCAG contrast check, with measured values. [20 pts]
8. **`DEFENSE.md`** — one page; a defensible sentence for every encoding decision. [25 pts]
9. **`DISCLOSURE.md`** — three distinct human-judgment decisions across three phases. [25 pts — a disclosure naming fewer than three distinct decisions, or three of the same kind, loses this component and incurs the standard 15-point disclosure deduction.]
10. **The 10-minute design review** — brief, specification, output, three decisions defended on demand. [40 pts]

**The bar.** A package whose figure is beautiful but whose `DEFENSE.md` reduces to taste, or whose `DISCLOSURE.md` cannot locate the human in the pipeline, has produced a *run-one* artifact (Chapter 13) and is graded as one. The rubric is defensibility, traceability, and editability — not polish. Polish that cannot be defended is the precise failure this book was written to prevent.

---

## Chapter summary — and the book's landing

You can now run the complete pipeline end to end: a brief becomes a SCOPE, a SCOPE survives an audit, an audited state is generated against unit by unit, the output is verified by a human and handed off through a vector editor into an editable production asset and a 300 DPI raster. You can subject the result to the blur, grayscale, and contrast tests; defend every encoding decision in the language of perceptual science and the design system rather than taste; and write the three-decision disclosure that locates the human in an AI-assisted process.

That last skill is the book. You began as someone who could prompt an AI tool into a polished SVG and could not tell whether it was trustworthy. You end as someone who can run an agent as a structured executor across a disciplined pipeline *and name, precisely, the decisions the agent could not make.* The infographic is a claim about the world dressed in visual authority. The pipeline produces the claim; the design-intelligence layer makes it true; and that layer — variable selection, encoding, exclusion, hierarchy, the ship call — is, for now and demonstrably, yours.

The companion volume, *Brutalist D3 × Claude*, picks up where this one's pantry stops: the full chart-type grammar, sixty-one forms, the marks-and-channels vocabulary at depth. Together they are the curriculum. But the thesis is the same in both, and you can now state it from the inside: AI handles the code; the judgment is irreducibly human; and the disclosure is the empirical test that you knew the difference.

## Key terms

- **Production package** — the complete folder (brief, spec, governing files, SVG, `.ai`, PNG, defense, disclosure) that makes a figure defensible.
- **Design review** — the 10-minute defense of every encoding decision against an alternative.
- **`DEFENSE.md`** — one page; a defensible sentence per encoding decision.
- **`DISCLOSURE.md`** — the final, three-decision-across-three-phases AI Use Disclosure.
- **Three final checks** — blur test, grayscale test, WCAG contrast check, applied to the finished figure.
- **Traceability** — the property that every artifact traces to a decision and every decision to the brief.

## Bridge — to your own work

There is no next chapter. The bridge now runs out of the book and into the next figure you are asked to produce — for a paper, a briefing, a product, a court. When that figure arrives, you have a method: audit before you touch, generate against a specification, verify against the spec, hand off into an editable asset, and disclose where you were irreducible. Begin there.

---

## AI Wayback Machine: Otto Neurath and the system behind the picture

Between the world wars in Vienna, Otto Neurath built the Isotype system — the International System of Typographic Picture Education — with the artist Gerd Arntz and the curator Marie Reidemeister (later Marie Neurath). [High — well-documented history] Isotype is remembered for the pictograms: rows of little figures standing for thousands of people, a visual language that crossed literacy barriers. But the pictograms were the surface. Underneath was a *production system* — a controlled vocabulary of symbols, strict rules for how quantity was encoded (more figures, never bigger figures, so area never lied about magnitude), and a division of labor in which Marie Neurath's role, which she called the "transformer," was to turn raw data and the client's intent into a defensible specification *before* the artist drew anything.

That transformer role is this entire book. Marie Neurath sat exactly where the design-intelligence layer sits: between the brief and the execution, deciding what the figure would claim, what it would exclude, and how quantity would be honestly encoded — and only then handing a specification to the person (or, now, the agent) who renders it. Neurath's rule that quantity is shown by *repetition, never by scaling area* is Cleveland–McGill avant la lettre: a perceptual-accuracy commitment baked into the system so the execution layer could not violate it. The Isotype pipeline and the Brutalist pipeline are the same shape across a century: a human transforms intent into specification; the specification governs execution; and the system's integrity lives in the transform, not the picture.

Try this prompt with an LLM: *"Marie Neurath called her role in the Isotype system the 'transformer' — turning data and client intent into a specification before any image was drawn. Map that role onto the design-intelligence layer in an AI-assisted SVG pipeline, and onto the production package's `scope.md` and `DISCLOSURE.md`. Where is the parallel exact, and where does a coding agent change it?"* Treat the answer as a draft to interrogate — which is the posture this whole book has taught.

---

## Sources

- Gebru, T., et al. (2021). *Datasheets for Datasets.* Communications of the ACM. — Production-package-as-datasheet model.
- Mitchell, M., et al. (2019). *Model Cards for Model Reporting.* FAT*/FAccT. — Structured-disclosure model behind the AI Use Disclosure.
- Bender, E. M., & Friedman, B. (2018). *Data Statements for Natural Language Processing.* TACL. — Documenting assumptions in the production package.
- Cleveland, W. S., & McGill, R. (1984). *Graphical Perception.* JASA. — The channel-accuracy basis for the encoding defenses.
- Anthropic. *Claude Code documentation.* Anthropic Docs (current). [verify before each course offering — high aging risk]
- D3 Team. *D3 selections and `selection.join` documentation.* d3js.org (current). [verify against pinned D3 v7]
- W3C WAI. (2023). *Web Content Accessibility Guidelines (WCAG) 2.2.* W3C Recommendation. [access date at final draft]
- Neurath, O., with Arntz, G., & Neurath, M. *Isotype: International System of Typographic Picture Education.* — Wayback figure; [verify specific attributions, esp. Marie Neurath's "transformer" role, against a primary history].
- *Brutalist D3 × Claude* (companion volume). — Chart-type grammar and the 61-form pantry.
