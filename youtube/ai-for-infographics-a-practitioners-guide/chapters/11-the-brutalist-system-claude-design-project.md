# Chapter 11 — The Brutalist System: The Claude Design Project

## Opening: The plausible figure that cost a week

An ML team needed one figure for a model-card appendix: inference latency across three serving configurations, with the p50 and p99 percentiles for each. An engineer who could already drive Claude Code opened a session, pasted "make an SVG bar chart comparing latency for our three configs, p50 and p99, brutalist style," and got an answer in under a minute. The chart rendered. It had bars, axes, a title, a legend, the word "brutalist" honored as a flat gray palette. It looked done.

It was not done, and the ways it was not done were invisible on screen. The bars encoded p50 and p99 as two adjacent reds — two data-encoding reds, violating the single-accent rule, so neither percentile was emphasized. The y-axis did not start at zero, exaggerating the spread between configs. The group structure, opened later in Illustrator, was a nest of anonymous `<g>` elements named `g`, `g_1`, `g_2` — uneditable. Hex values were hardcoded throughout rather than drawn from tokens. There was no metadata, no source line, no caveat that p99 was computed over a single day's traffic.

The engineer shipped it. A reviewer caught the zero-baseline problem. The figure went back. The second generation fixed the baseline but reintroduced the double-red. The third fixed the color but the Illustrator handoff failed on the clipping masks. By the time the figure was correct and editable, the engineer had spent the better part of a week in a loop of generate-inspect-regenerate — longer than specifying it correctly once would have taken.

The failure was not the tool. The tool did exactly what it was asked. The failure was that **generation began before the design intelligence layer existed.** There was no claim, no encoding plan, no exclusion list, no constitution telling the tool what "brutalist" actually constrains. This chapter is about the governing files and the phase gate that make that failure structurally impossible — and about the labor separation that defines the rest of the book: **the tool builds the implementation; the human owns the design intelligence.**

## Core content

### Three governing files, three jobs

The Brutalist System organizes AI-assisted production around three files. Each answers a different question, each changes on a different schedule, and each has a different owner [High — this is the book's designed system; *verify — system specifics* against the live project files].

| File | Question it answers | Scope | Changes when | Owned/maintained by |
|---|---|---|---|---|
| **CLAUDE.md** | *How is code written here?* | The coding constitution: stack, naming conventions, canonical patterns, prohibited actions | The renderer changes (e.g., a D3 major version) | Human; stable across projects on the same stack |
| **DESIGN.md** | *What does this figure look like and claim?* | The visual constitution: seven color tokens with roles, typography stack, layout type, annotation plan, exclusion list | Per project; comes from the Chapter 10 SCOPE specification | Human; the design intelligence layer |
| **PROJECT.md** | *What is the current state?* | Project state in two layers: an Intent Layer and a Schema Layer | Continuously, as work proceeds | Intent Layer: human only. Schema Layer: maintained by AI |

The separation is the point. **CLAUDE.md** is stack-specific and stable — for this book's pipeline it pins the D3 v7 stack, the semantic-layer scaffold, the `.join()` lifecycle pattern, the rule that presentation goes through `.attr()` not `.style()`, the slug function for stable IDs, and the prohibited actions (no hardcoded hex, no rainbow palettes, no opacity-for-encoding). It changes only when the renderer changes. **DESIGN.md** is project-specific and *is* your Chapter 10 output operationalized — it carries the seven tokens, the typography roles, the layout type, the annotation plan, and the exclusion list as explicit prohibitions. **PROJECT.md** holds the live state.

### The two layers of PROJECT.md, and who may touch them

PROJECT.md is split deliberately:

- The **Intent Layer** records *what the human decided and why* — the claim, the audience, the chosen layout type, the rationale for key exclusions. **The Intent Layer is never overwritten by the AI.** It is the human's record of design intelligence, and a tool that edited it would be editing the judgment it exists to serve. This is an enforced boundary, not a courtesy.
- The **Schema Layer** records *the current technical state* — assets that exist, naming conventions in use, the gap between current state and DESIGN.md. **The Schema Layer is maintained by the AI** as it audits and generates. It is the working memory of the pipeline.

A tool reading PROJECT.md reads the Intent Layer as fixed law and writes only to the Schema Layer. The reader who understands this distinction understands the whole labor separation in miniature: intent is human and immutable to the tool; state is shared and maintained by the tool under human supervision.

### The phase gate: no generation before both layers are populated

The single most important rule in the system is a gate, not a guideline. **Generation may not begin until both the Intent Layer and the Schema Layer of PROJECT.md are fully populated** [High — designed enforcement mechanism]. In the book's five-phase pipeline —

**Audit → Schema → Generate → Verify → Handoff**

— the gate sits between *Schema* and *Generate.* Audit (Chapter 12) inventories what exists. Schema populates the Schema Layer from that audit. Only when the Intent Layer (the human's design intelligence, from DESIGN.md and the SCOPE work) and the Schema Layer (the audited technical state) are both complete does the gate open and Generate (Chapter 13) begin. Verify (Chapter 14) reviews every output before the next is issued; Handoff (Chapter 14) carries the SVG to Illustrator-editable `.ai` and 300 DPI PNG.

The opening story is a textbook gate violation: the engineer ran Generate with an empty Intent Layer and an unaudited Schema Layer. The gate would have stopped it. The phase gate is an *enforcement mechanism* precisely because the failure mode it prevents — plausible, polished, wrong output produced from an empty specification — is invisible at generation time and expensive at review time. A guideline you can ignore under deadline; a gate you cannot.

![The five-phase pipeline Audit, Schema, Generate, Verify, Handoff with a red locked gate before Generate, above a human design-intelligence band and a tool implementation band](images/11-the-brutalist-system-claude-design-project-fig-01.png)

*Figure 11.1 — The five-phase pipeline with the human-judgment gate (red) locked between Schema and Generate until both PROJECT.md layers are populated; the human owns the design intelligence, the tool owns the implementation.*

### Labor separation and refusal behavior

The governing files encode a labor separation that is the operational form of the book's thesis: **the tool builds the implementation; the human owns the design intelligence.** Concretely, the tool's jobs are to audit existing assets, populate the Schema Layer, generate SVG that conforms to CLAUDE.md and DESIGN.md, and run verification checks. The human's jobs are to write the claim, choose the encoding, set the exclusion list, populate and protect the Intent Layer, and make the final accept/reject decision in Verify.

A well-configured system also exhibits **refusal behavior**: instructed to generate before the gate is open, a correctly governed tool should decline and report which layer is unpopulated, rather than produce a plausible figure from nothing. Refusal is a feature. A tool that always says yes is a tool that will happily reproduce the week-long loop. The refusal is the system enforcing the gate on the human's behalf — a small, useful friction at exactly the moment the human is tempted to skip the design layer. In practice the refusal should be informative, not merely a "no": it should name *which* layer is unpopulated and *what* the human must supply — "Intent Layer is empty: no claim, no exclusion list. Populate DESIGN.md before generation." A refusal that diagnoses the gap turns the friction into a checklist, and converts the tool from an order-taker into a collaborator that protects the design intelligence layer it depends on.

### What CLAUDE.md actually pins: canonical patterns and prohibited actions

It is worth seeing why CLAUDE.md must be specific rather than aspirational, because "write clean D3" is not a constraint a tool can obey — it is a wish. CLAUDE.md pins *named, checkable* patterns [High — these are the book's canonical D3 v7 conventions; *verify* against the live file and current D3].

- **The semantic-layer scaffold.** Every figure opens by creating named layer groups in render order, so the SVG's structure is editorially meaningful from the first line rather than an emergent tangle: `const layers = { background: svg.append("g").attr("id","background"), grid: svg.append("g").attr("id","grid"), data: svg.append("g").attr("id","data"), annotation: svg.append("g").attr("id","annotation") }`. This is the Painter's-Algorithm-meets-editability resolution from Chapter 7, written as a rule the generator cannot skip.
- **`.join()` for lifecycle, not enter/update/exit by hand.** Pinning the modern `.join()` pattern keeps data binding clean and predictable, which matters because hand-rolled enter/exit code is where generated SVG accumulates the orphaned, un-named nodes that wreck the Illustrator handoff.
- **Presentation via `.attr()`, never `.style()`.** Visual properties set with `.attr()` become *presentation attributes* on the element — which survive the SVG-to-Illustrator round trip — whereas `.style()` writes inline CSS that Illustrator may flatten or drop. This single rule prevents a whole class of handoff failures.
- **Stable IDs via `slug()`.** A pinned slug function turns `"1st Floor"` into a stable, escape-safe id rather than letting the renderer emit something like `_x31_st-floor` (the ID-escaping failure from Chapter 7). Stable IDs are what make the Illustrator layers panel navigable.
- **Prohibited actions, enumerated.** No hardcoded hex (tokens only); no rainbow palettes; no opacity-for-encoding (Chapter 8); no auto-named groups; no non-zero baseline on magnitude bars. A prohibition the tool can check is worth more than a principle it can rationalize around.

The pattern across all five: CLAUDE.md encodes the *coding* decisions that are stable across projects, leaving the *visual* decisions to DESIGN.md and the *intent* to PROJECT.md. A reader who tries to put a color token in CLAUDE.md or a `.join()` pattern in DESIGN.md has misunderstood the separation — and the misplacement will surface as a figure that is either off-stack or off-brand.

### Why this is debt management, not bureaucracy

It is fair to ask whether three files and a gate are overhead. Borrow the framing from Sculley and colleagues' work on hidden technical debt in machine-learning systems: unmanaged generated artifacts accumulate maintenance debt that comes due later, with interest [High — Sculley et al., 2015, on ML technical debt; applied here by analogy]. An ungoverned SVG that "looks right" is exactly such an artifact — a glue-coded, un-named, hardcoded figure that the next person (often you, a month later) cannot edit, audit, or trust. The governing files are the debt-prevention discipline: they make the figure's provenance, intent, and constraints explicit at creation time, when it is cheap, rather than reconstructing them at edit time, when it is not. The Datasheets-for-Datasets and Model-Cards lineages make the same move for data and models; the Brutalist System makes it for figures.

## Worked example: governing the latency figure

**Problem statement.** The opening figure — inference latency across three serving configs, p50 and p99 — done correctly under the governing files.

**First attempt (specification-less, from the opening).** Eleven-ish defects across color, baseline, structure, tokens, metadata, and caveat. Three regeneration loops. A week.

**The governed setup (the corrected design intelligence):**

```
CLAUDE.md (stack constitution, stable):
  - Stack: D3 v7. Semantic-layer scaffold:
      const layers = { background: svg.append("g").attr("id","background"), ... }
  - Presentation via .attr(), never .style(). Stable IDs via slug().
  - Prohibited: hardcoded hex; rainbow palettes; opacity-for-encoding;
    auto-named groups; non-zero baseline on magnitude bars.

DESIGN.md (visual constitution, from Ch.10 SCOPE):
  - Claim: "p99 latency, not p50, separates the three configs."
  - Mark/channel: grouped bars, position on a common zero-based scale.
  - Color: p50 in --color-ink; p99 in --color-red (the SINGLE accent —
    p99 is the story). Two categories, two channels (ink vs. red): legal.
  - Type: title EB Garamond; ticks JetBrains Mono; labels Inter.
  - Annotation: INTERPRETATION beside the widest p99 gap; direct labels,
    no legend; CAVEAT "p99 over one day of traffic" in secondary gray.
  - Exclusions: no dual axis; zero-based y; no gradient; no ochre on data;
    do not imply causation between config and latency.

PROJECT.md:
  Intent Layer (HUMAN, never overwritten):
    - The figure's job is to show p99 separation; p50 is context.
    - p99-over-one-day caveat is required for honesty.
  Schema Layer (AI-maintained, from Audit):
    - existing assets: none. Conventions: n/a. Gap: full build needed.
```

**Phase-gate check.** Intent Layer populated? Yes. Schema Layer populated (post-Audit)? Yes. **Gate opens.** Generate may proceed — and now produces a near-correct figure on the first pass, because every defect from the opening was pre-empted by a token role, a prohibition, or an exclusion.

**The lesson.** The week-long loop was not a tooling problem; it was a missing-constitution problem. Three files and a gate convert generation from trial-and-error into execution of a decided design.

**The limit.** The tool can write CLAUDE.md's patterns and maintain the Schema Layer. It cannot decide that *p99 is the story and p50 is context*, that *causation must not be implied*, or that *the one-day caveat is required.* Those live in DESIGN.md and the Intent Layer — written by the human, protected from the tool, and named in the disclosure.

## AI Wayback Machine: Grace Hopper and the discipline of the machine you can read

**Grace Hopper** — naval officer, computer scientist, and a principal force behind machine-independent programming languages — spent her career on a conviction that maps directly onto this chapter: that instructions to a machine should be *human-readable and human-governable*, not opaque [High]. (Wayback target: Wikipedia "Grace Hopper.") She is also, famously, associated with the most literal "bug" in computing history — in 1947 her team at Harvard found a moth jammed in a relay of the Mark II and taped it into the logbook — which is to say, with the discipline of *recording the state of the system in a form a human can later audit.*

That is PROJECT.md. Hopper's instinct that a machine's behavior must be expressible in language a person can read, govern, and hold accountable is the instinct behind the three governing files: CLAUDE.md and DESIGN.md as human-readable constitutions, PROJECT.md as the human-auditable log of intent and state. The phase gate is the modern descendant of her insistence that you do not let the machine run until the instructions are right.

> **Prompt to try:** "Explain how Grace Hopper's insistence on human-readable, machine-independent instructions anticipates the role of CLAUDE.md, DESIGN.md, and PROJECT.md in governing an AI code generator — and why a phase gate is a form of the accountability she demanded."

The throughline: from the moth in the logbook to the Schema Layer, the discipline is the same — keep the machine's state in a form a human can read, govern, and answer for.

## Assessment — Reading Response (Act Three framing) (30 pts)

In 600–800 words, using a real or AI-generated specification-less figure from the AI/ML-system-performance domain (keep the prompt and the output):

1. **Diagnose the gate violation.** Identify what was missing from the Intent Layer and the Schema Layer when generation began, and list at least four defects in the output that a populated DESIGN.md would have prevented (12 pts).
2. **Assign each defect to a file.** For each defect, state whether the fix belongs in CLAUDE.md (a stack/coding rule), DESIGN.md (a visual/claim decision), or PROJECT.md (a state/intent record), and justify the assignment (10 pts).
3. **Write the refusal.** Draft the message a correctly governed tool *should* have returned when asked to generate from the empty specification — naming which layer was unpopulated and what the human must supply first (8 pts).

Attach an **AI Use Disclosure** naming at least two decisions in the corrected setup that required your judgment and that no AI tool could supply — for example, *what the figure claims* and *which exclusion protects its honesty*.

## Bridge

The governing files are written and the phase gate is in place, but the gate cannot open until you know what already exists in the project. You cannot populate the Schema Layer from nothing. Chapter 12 runs the **Audit** phase: a complete inventory of existing assets, the naming conventions actually in use, and the gap between the current state and what DESIGN.md specifies — the work that fills the Schema Layer and earns the right to begin generating.

## Sources

- Anthropic. *Claude Code documentation.* Anthropic Docs (current). Source for Claude Code workflows, project files, and constraints. [High aging risk; verify access date before each course offering.]
- D3 Team. *D3 selections and `selection.join` documentation.* d3js.org (current). Reference for the lifecycle patterns CLAUDE.md pins for the D3 v7 stack.
- Sculley, D., et al. "Hidden Technical Debt in Machine Learning Systems." *NeurIPS*, 2015. Source for the debt-management framing of governing files.
- Gebru, Timnit, et al. "Datasheets for Datasets." *Communications of the ACM*, 2021. Documentation-as-provenance model adapted to figures.
- Mitchell, Margaret, et al. "Model Cards for Model Reporting." *FAccT*, 2019. Structured-disclosure model behind the AI Use Disclosure.
- Hopper, Grace. Work on compilers and machine-independent programming languages. [Verify exact page title and dates before Wayback citation.]
- Brutalist System governing files — CLAUDE.md, DESIGN.md, PROJECT.md (this book; `pantry/cajal-svg-generator.md` for tokens and style). [*Verify — system specifics* against the live project files.]
