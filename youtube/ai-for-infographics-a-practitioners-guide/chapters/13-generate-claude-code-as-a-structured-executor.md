# Chapter 13 — Generate: Claude Code as a Structured Executor

**[PIPELINE CHECKPOINT]**

## Learning objectives

By the end of this chapter you will be able to:

1. (Apply) Construct a Claude Code prompt that encodes the complete CAJAL SCOPE specification and the `DESIGN.md` constraints.
2. (Apply) Generate a D3-driven SVG infographic using the clean D3 patterns from `CLAUDE.md` — the semantic layer scaffold, `.join()` lifecycle management, and presentation attributes set via `.attr()`.
3. (Evaluate) Apply the `CLAUDE.md` verification checklist to generated output: correct naming, correct color tokens, correct font stacks, no hardcoded hex, no D3 `.style()` calls for visual properties.
4. (Create) Generate the complete SVG output for the terminal project, with the CAJAL metadata block embedded.

---

## Opening: the same brief, twice

We are going to run an experiment, and the result is the lesson. You will not be told the gap between specification-driven and specification-less generation. You will see it, counted.

The brief is from science communication: *a figure showing how a vaccine's efficacy estimate narrows as a trial enrolls more participants — the point estimate stabilizing while the confidence interval shrinks.* The data are real-shaped: efficacy hovering around 71% with a wide interval at 1,000 enrollees, tightening toward 71% ± 4 points at 30,000. You have, from Chapters 10 through 12, a complete CAJAL SCOPE specification, a finished `DESIGN.md`, a stack-specific `CLAUDE.md`, and an audited project state with the gate open.

### Run one: the specification-less prompt

Open a fresh Claude Code session with no governing files in context. Type what a hurried engineer types:

> *"Make me an SVG infographic showing vaccine efficacy stabilizing as the trial gets bigger. Use D3. Make it look clean and professional."*

Ninety seconds later you have an SVG. It renders. It looks, frankly, good — a confident line with a shaded band, a title, axis labels, a pleasant blue-to-green gradient on the band. If you put it in a slide nobody in the room would object.

Now open it in a text editor and run it against the `CLAUDE.md` checklist. Here is what one such run produced, on eleven counts: [Medium — illustrative; exact violation set varies by model version and run]

1. Band fill is a hardcoded `#4a90d2` — not a design token.
2. A second hardcoded hex, `#2ecc71`, for the line — two hardcoded colors, neither tokenized.
3. The band uses a `linearGradient` — decorative, non-encoding; a Brutalist violation (the gradient encodes nothing; it is ornament).
4. Visual properties set with D3 `.style("fill", …)` rather than `.attr()` — they will not survive the Illustrator export cleanly.
5. Axis font is the browser default sans, not JetBrains Mono.
6. Title font is the same default, not EB Garamond.
7. Groups are anonymous: `<g>`, `<g>`, `<g>` — no semantic layer scaffold.
8. No `data-name` attributes — nothing survives the round trip to Illustrator with a human-readable name.
9. The confidence band sits *on top of* the line in document order — painter's-algorithm error; the band partially occludes the estimate it is supposed to contextualize.
10. No CAJAL metadata block — the figure carries no record of what it claims or what it excludes.
11. The y-axis starts at 50%, not 0 — and there is no annotation saying so, so the stabilization looks more dramatic than it is. A perceptual-accuracy failure that is invisible at the surface.

Count nine and count eleven are the dangerous ones. Eleven is a lie of exactly the kind Chapter 1 opened with: data-accurate, perceptually misleading, dressed in the visual authority of a clean chart. The agent did not lie on purpose. It optimized for "clean and professional" and a truncated axis looks cleaner. Nothing in the prompt told it that the design intelligence — the decision about where the axis starts and whether that decision is disclosed — was not its to make.

### Run two: the specification-driven prompt

Same model, same data, same ninety seconds. But now the session has `CLAUDE.md`, `DESIGN.md`, and the SCOPE specification in context, and the prompt is built to execute against them (we will dissect its structure next). The output requires **zero** corrections on the eleven-count checklist. The axis starts at zero. The band renders behind the line. The colors are tokens. The groups are named. The metadata block is present. The figure is not more beautiful than run one — by Brutalist lights it is plainer. It is *defensible*, which run one was not.

That is the whole chapter. Everything below is how to make run two happen reliably.

![One brief forks into two branches: the specification-less run tallies eleven checklist violations, two of them perceptual lies; the specification-driven run, same model and ninety seconds, requires zero corrections.](images/13-generate-claude-code-as-a-structured-executor-fig-01.png)

*Figure 13.1 — The same brief, twice: governing context is the only variable, and the gap is eleven violations versus zero corrections.*

---

## The reframe: executor, not collaborator

The instinct most engineers bring to a coding agent is *collaboration* — "let's figure this out together." For prose, for exploratory code, that instinct is often right. For infographic generation it is the source of the eleven-count failure.

Claude Code, in this pipeline, is a **structured executor.** [High — this is the book's design stance, not a claim about model capability] It executes a specification you have already authored. The design decisions — what the figure claims, which encoding, which colors, what is excluded, where the axis starts — were made in Chapters 10 through 12 and live in the SCOPE specification and `DESIGN.md`. The agent's job is to render those decisions into correct D3 and correct SVG structure. When you let it make design decisions, it makes them by optimizing surface plausibility, and surface plausibility is orthogonal to communicative accuracy (Chapter 1) and frequently opposed to it.

This is not a limitation you are working around. It is the division of labor the whole book argues for. The agentic-code-generation literature points the same direction: as agents grow more capable, the constraint files and verification checklists that bound them become *more* important, not less, because a more capable agent propagates an unbounded inference further and faster. [Medium — current-state observation about agentic tooling] Capability raises the stakes of specification; it does not retire it.

---

## The prompt structure that makes run two reliable

A specification-driven Claude Code prompt has four parts. The order matters.

**1. The governing context.** The session must have `CLAUDE.md`, `DESIGN.md`, and `PROJECT.md` loaded — the coding constitution, the visual constitution, and the audited project state. In Claude Code this is the working directory plus the files you reference. This is the difference between the two runs above and it is not optional.

**2. The SCOPE specification, restated in the prompt.** Even with `DESIGN.md` in context, restate the figure's SCOPE in the prompt itself — Specification, Content, Organization, Presentation, Exclusions. The Exclusions are the highest-leverage line. *"Exclude: any axis truncation; the y-axis begins at zero. Exclude: gradient fills. Exclude: more than two data-encoding colors."* You are pre-empting the run-one failures by naming them as out of bounds.

**3. The structural directive.** Tell the agent to use the canonical patterns from `CLAUDE.md`: the semantic layer scaffold, `.join()` for the data lifecycle, presentation attributes via `.attr()`, the slug function for stable IDs, and the CAJAL metadata block. Name the patterns; do not assume the agent will infer them.

**4. The generate-one-unit-at-a-time rule.** Do not ask for the whole figure in one shot. Ask for the scaffold first, verify it, then the marks, verify, then the annotation, verify. Each unit is small enough to check against the checklist before the next is issued. This is the single most effective discipline for keeping the eleven-count failure from accumulating silently.

Here is the prompt skeleton:

```text
CONTEXT: Use the loaded CLAUDE.md, DESIGN.md, and PROJECT.md. The phase gate
is open (Audit complete; Schema Layer populated).

SCOPE for this figure:
  S — Specification: line + CI band, efficacy vs. enrollment, 1k–30k.
  C — Content: point estimate (line), 95% CI (band), n on x, efficacy % on y.
  O — Organization: single panel; band behind line; annotation at stabilization.
  P — Presentation: Brutalist; EB Garamond title, JetBrains Mono ticks,
      ink-on-paper, single accent on the stabilization callout only.
  E — Exclusions: NO axis truncation (y starts at 0); NO gradients;
      NO more than two data-encoding colors; NO legend (direct labels).

GENERATE — UNIT 1 ONLY: the semantic layer scaffold per CLAUDE.md.
Use named layers in painter's order. Stop after the scaffold. Do not draw marks yet.
```

You verify Unit 1, then issue Unit 2, and so on. The agent never gets to "make it look clean and professional," because you never delegate the decision that phrase smuggles in.

---

## The D3 patterns, introduced as needed

You do not need to know D3 to read this book; you need the handful of patterns that make generated SVG editable and honest. `CLAUDE.md` canonizes them; here is why each exists.

### The semantic layer scaffold

The single most important pattern. Instead of letting D3 append anonymous `<g>` elements as it draws, you create named layers up front, in painter's order:

```javascript
const layers = {
  background:  svg.append("g").attr("id", "background"),
  gridlines:   svg.append("g").attr("id", "gridlines"),
  ciBand:      svg.append("g").attr("id", "ci-band"),
  estimate:    svg.append("g").attr("id", "estimate-line"),
  annotation:  svg.append("g").attr("id", "annotation"),
};
```

Two things happen here at once. First, **document order is painter's order** (Chapter 7): `ci-band` is appended before `estimate-line`, so the band paints behind the line — fixing run-one's count nine structurally, by construction, not by accident. Second, every layer has a semantic name, so when the file opens in Illustrator the Layers panel reads `ci-band`, `estimate-line`, `annotation` — the editorial structure a designer needs, sitting inside the rendering structure SVG requires. This is the Chapter 7 resolution, executed.

![A painter's-order SVG layer stack on the left mirrors the Illustrator Layers panel on the right; the annotation accent layer paints last, and each layer arrives with a human-readable name.](images/13-generate-claude-code-as-a-structured-executor-fig-02.png)

*Figure 13.2 — The semantic layer scaffold makes painter's order and editorial naming the same act: the band paints behind the line by construction, and named layers survive the round trip.*

### The `.join()` lifecycle

D3 v7's `selection.join()` manages the enter/update/exit lifecycle cleanly: [High — current D3 v7 behavior; verify version pin]

```javascript
layers.estimate.selectAll("path.estimate")
  .data([efficacyData])
  .join("path")
    .attr("class", "estimate")
    .attr("d", lineGenerator)
    .attr("fill", "none")
    .attr("stroke", tokens.ink)        // a token, not a hex literal
    .attr("stroke-width", 2);
```

`.join()` matters because it keeps the data-to-mark binding explicit and avoids the orphaned elements that older enter/exit patterns leave behind — orphans that become anonymous junk groups in Illustrator.

### Presentation attributes via `.attr()`, never `.style()` for visual properties

This is count four from run one, and it is the subtle one. D3 lets you set `.style("fill", …)`, which writes an inline CSS style. It looks identical in the browser. But when Illustrator imports the SVG, inline styles and presentation attributes are handled differently, and `.style()`-set properties are the ones most likely to be flattened, lost, or baked into a form the editor cannot easily change. [Medium — Illustrator import behavior, verify against current version] The rule: **visual properties — fill, stroke, stroke-width, opacity — are set with `.attr()`.** Reserve `.style()` for properties that genuinely belong to CSS layout, which in a static infographic is almost none.

### The slug function for stable IDs

To name layers and elements from data without producing the `_x31_` escaping artifact from Chapter 12, you slug:

```javascript
const slug = s => String(s).toLowerCase()
  .replace(/[^a-z0-9]+/g, "-")
  .replace(/^-+|-+$/g, "")
  .replace(/^(\d)/, "n$1");   // never start an ID with a digit
```

That last replace prepends `n` to a leading digit, so `1st-floor` becomes `n1st-floor` — a name you chose, not `_x31_st-floor`, a name Illustrator chose for you in self-defense.

### The CAJAL metadata block

Every generated figure carries its own record, embedded in the SVG:

```xml
<metadata id="cajal">
  CLAIM: Efficacy estimate stabilizes near 71% as enrollment grows.
  ENCODING: position (y=efficacy, x=enrollment); area (CI band).
  EXCLUSIONS: axis truncation; gradients; >2 data colors; legend.
  AXIS: y begins at 0 (no truncation).
  ACCESSIBILITY: all text ≥ 4.5:1; grayscale-distinguishable.
  GENERATED: Claude Code, spec-driven; verified against CLAUDE.md checklist.
</metadata>
```

The metadata block is what makes the figure a *defensible artifact* rather than a pretty file. It records what the figure claims and — crucially — what it excludes, so a reviewer (or a future you) can check the figure against its own stated commitments.

---

## The verification checklist applied at generation time

You do not wait until the Verify phase (Chapter 14) to start checking. You run the `CLAUDE.md` checklist after each generated unit. The checklist, in four categories:

- **Naming** — semantic group IDs; no auto-generated `g`/`g-2`; no `_x31_` artifacts; `data-name` present where it must survive to Illustrator.
- **Color** — every color is a token; zero hardcoded hex; at most two data-encoding colors; the single accent used once.
- **Type** — EB Garamond for display, Inter for body/labels, JetBrains Mono for ticks; no default sans leaking through.
- **Structure** — painter's-order layers; band-behind-line; `.attr()` not `.style()` for visual props; metadata block present; axis untruncated unless disclosed.

A generated unit that fails any item is regenerated, not patched by hand — patching by hand at the generate stage hides which prompt or pattern produced the failure, and the next figure will reproduce it.

---

## Worked example: generating the efficacy figure, unit by unit

**Problem statement.** Generate the science-communication efficacy figure to pass all four checklist categories with zero hand corrections.

**First attempt (specification-less).** Run one above: eleven violations, two of them perceptual lies.

**Design diagnosis.** The violations cluster: colors (1, 2), ornament (3), export-fragility (4), type (5, 6), naming (7, 8), painter's order (9), provenance (10), and truncation (11). Every cluster maps to a `CLAUDE.md` rule that was absent from the session.

**Corrected version (specification-driven, unit by unit).**

| Unit | Prompt directive | Verification finding | Result |
|---|---|---|---|
| 1. Scaffold | Named layers in painter's order | Five named layers; `ci-band` before `estimate-line` | PASS |
| 2. Scales/axes | y from 0; JetBrains Mono ticks | y domain `[0, 100]`; mono ticks | PASS — kills count 11 |
| 3. CI band | Area mark, token fill, `.attr()` | `fill={tokens.bandTint}`; no gradient | PASS — kills 3, 4 |
| 4. Estimate line | Line mark, ink token, behind annotation | Renders over band; `.attr()` | PASS — kills 9 |
| 5. Annotation | Single accent at stabilization; direct label | Accent used once; no legend | PASS |
| 6. Metadata | CAJAL block w/ claim, exclusions, axis note | Block present, axis-zero noted | PASS — kills 10 |

Six units, six checklist passes, zero hand corrections.

**The lesson.** *A specification turns an agent from a guesser into an executor; the eleven failures were eleven decisions the spec made and the bare prompt left to chance.*

**The limit.** The agent generated a flawless scaffold and an honest axis — but only because a human decided the axis begins at zero, decided two colors was the ceiling, and decided the stabilization callout earned the single accent. Those are the irreducibly human decisions. The agent executed them; it could not have originated them, because each requires knowing the claim the figure must defend, not the file it must render.

---

## Assessment: Pipeline Checkpoint (100 points)

**Task.** Generate the complete SVG output for your terminal-project infographic, using Claude Code as a structured executor against your audited project state (Chapter 12), your `DESIGN.md`, your `CLAUDE.md`, and your CAJAL SCOPE specification.

**Deliverables.**

1. **The generated SVG** with the CAJAL metadata block embedded (claim, encoding, exclusions, axis note, accessibility note, provenance). [40 pts]
2. **The four-part prompt** you used — governing context reference, restated SCOPE, structural directive, and the unit-by-unit generation log. [20 pts]
3. **The completed `CLAUDE.md` verification checklist** for the final output, with every item marked PASS and any item that initially failed shown with the regeneration that fixed it (not a hand patch). [25 pts]
4. **AI Use Disclosure** naming at least two design decisions that required human judgment the agent could not supply — at minimum one perceptual-accuracy decision (e.g., axis-zero, color-count ceiling) and one structural-editorial decision (e.g., painter's-order layer naming). [15 pts]

**Hard requirement.** The Pipeline Checkpoint is returned ungraded if the Chapter 12 Audit deliverable is not attached and the phase gate was not open before generation. You may not generate before you audit; the Checkpoint enforces it.

**Grading note.** A submission whose SVG looks polished but carries hardcoded hex, anonymous groups, or a truncated undisclosed axis is a *run-one* submission and is graded as one regardless of visual quality. Polish is not the rubric. Defensibility is.

---

## Chapter summary

You can now construct a four-part, specification-driven Claude Code prompt that encodes the SCOPE and `DESIGN.md` constraints, and you understand — having seen it counted — why the specification-less prompt fails on perceptual and structural grounds the surface hides. You can deploy the canonical D3 patterns: the semantic layer scaffold (which makes painter's order and editorial naming the same act), `.join()` lifecycle management, presentation attributes via `.attr()`, the slug function, and the embedded CAJAL metadata block. You can run the `CLAUDE.md` verification checklist at generation time and regenerate rather than patch. And you can produce a complete, defensible generated SVG for the terminal project.

## Key terms

- **Structured executor** — the role Claude Code plays in this pipeline: rendering an authored specification, not originating design decisions.
- **Specification-less generation** — generating from a bare prompt with no governing files; the source of the eleven-count failure.
- **Semantic layer scaffold** — named `<g>` layers created up front in painter's order, unifying rendering order and editorial naming.
- **`.join()`** — D3 v7's enter/update/exit lifecycle method; avoids orphaned elements.
- **Presentation attribute** — a visual property set via `.attr()` (not `.style()`) so it survives the Illustrator export.
- **Slug function** — a string normalizer producing stable IDs that never begin with a digit, avoiding the `_x31_` artifact.
- **CAJAL metadata block** — the embedded record of a figure's claim, encoding, and exclusions; what makes it defensible.
- **Generate-one-unit-at-a-time** — the discipline of generating and verifying small units so failures are caught before they accumulate.

## Bridge

The SVG exists and passes the checklist. But "passes the generation checklist" is not "production-ready." In Chapter 14 you run the Verify phase as a human review of every output, and then you do the step most pipelines skip entirely: you open the SVG in Illustrator (or Inkscape), release the clipping masks, confirm the semantic groups survived, fix the text alignment the export mangled, and turn the SVG into a production asset. The painter's-algorithm-versus-editorial-grouping conflict from Chapter 7 becomes, in Chapter 14, a thing your hands do.

---

## AI Wayback Machine: Mike Bostock and the constraint that frees

D3 exists because Mike Bostock, building on the earlier Protovis work with Jeffrey Heer, made a specific and disciplined choice: D3 would not be a charting library that hands you a `barChart()` function. [High — D3 design history] It would bind data to the DOM and let *you* specify the mapping — marks, scales, structure — explicitly. Critics called it low-level. Bostock's wager was that an explicit, specification-driven primitive is more powerful than a convenient black box, because the black box makes the easy chart easy and the honest chart impossible.

That wager is this chapter's thesis in another register. The specification-less prompt is the `barChart()` convenience: fast, plausible, and unable to express the decisions that make a figure defensible. The specification-driven prompt is Bostock's bet — more work up front, total control over the encoding, and the only path to an axis that starts at zero on purpose. D3 was designed so that the human specifies and the library executes. This chapter asks you to treat Claude Code the same way.

Try this prompt with an LLM: *"Mike Bostock designed D3 as a low-level, specification-driven primitive rather than a high-level charting library. Explain how that design choice parallels using a coding agent as a structured executor rather than a creative collaborator — and name one place the analogy breaks."* Interrogate the answer; it is a draft, not a verdict.

---

## Sources

- Anthropic. *Claude Code documentation.* Anthropic Docs (current). [verify before each course offering — high aging risk]
- D3 Team. *D3 selections and `selection.join` documentation.* d3js.org (current). [verify against pinned D3 v7 version]
- Bostock, M., Ogievetsky, V., & Heer, J. (2011). *D³: Data-Driven Documents.* IEEE TVCG. — D3 design rationale behind the Wayback figure.
- Sculley, D., et al. (2015). *Hidden Technical Debt in Machine Learning Systems.* NeurIPS.
- W3C SVG Working Group. *Scalable Vector Graphics (SVG) 2 Specification.* W3C (current).
- Eisenberg, J. D., & Bellamy-Royds, A. (2018). *SVG Essentials* (2nd ed.). O'Reilly. — Reading and authoring SVG structure.
- Adobe. *Illustrator documentation: SVG import and presentation-attribute handling.* Adobe Help (current). [verify `.style()` vs. `.attr()` import behavior against current version]
