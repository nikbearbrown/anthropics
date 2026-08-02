# Chapter 12 — Audit: What Exists Before You Touch Anything

## Learning objectives

By the end of this chapter you will be able to:

1. (Apply) Run a complete Audit phase: inventory all existing assets, name every convention already in use, and map every gap between the current project state and `DESIGN.md`.
2. (Analyze) Identify naming-convention violations in an existing codebase using the `CLAUDE.md` rules.
3. (Apply) Populate the Schema Layer of `PROJECT.md` from the Audit output.
4. (Evaluate) Determine whether the phase-gate condition is met — both the Intent Layer and the Schema Layer populated — before any generation begins.

---

## Opening: the directory you inherited

It is the second week of the term and you have been handed a folder. It belongs to a team that produced a quarterly economic briefing for a regional development authority — a set of infographics about lending volume, default rates, and regional capital flows. The lead designer left. Their last commit message reads `wip — fix later`. You have been asked to refresh three figures for the new quarter.

You open the directory. There are eleven SVG files. Two are named `final_v2_REAL.svg` and `final_v2_REAL_fixed.svg`. There is a `DESIGN.md`, but it stops mid-sentence in the typography section. There is no `CLAUDE.md` at all. One SVG opens in the browser and looks immaculate — a clean diverging bar chart of regional lending, EB Garamond headline, the ochre accent sitting exactly where the eye should land. You open the same file in a text editor. The bars are `<rect>` elements with hardcoded `fill="#c08a2d"` repeated forty times. The groups are named `g`, `g-2`, `g-3`, and one called `Layer_1 copy`. The axis labels are in Arial.

Here is the temptation, and it is a strong one: open Claude Code, point it at the cleanest-looking file, and say *"refresh this for Q3 with the new numbers."* You will get something back in ninety seconds. It will look plausible. And you will have just built the new quarter on top of a foundation you never inspected — inheriting the Arial labels, the hardcoded ochre, the anonymous groups, and whatever the previous designer meant by `final_v2_REAL_fixed`.

This chapter is about the discipline that the temptation skips. Before you generate anything, you audit what exists. Not because it is tidy. Because **the cost of generating against an unaudited state is paid later, in a currency — production time, editorial trust, accessibility failures — that is far more expensive than the audit would have been.** [High]

---

## The Audit phase is a gate, not a courtesy

In Chapter 11 you met the Brutalist system's five phases — **Audit → Schema → Generate → Verify → Handoff** — and the three governing files that hold them: `CLAUDE.md` (the coding constitution), `DESIGN.md` (the visual constitution), and `PROJECT.md` (the project state). You also met the phase gate: no generation begins until both the Intent Layer and the Schema Layer of `PROJECT.md` are populated.

The Audit phase is what populates the Schema Layer. That is its entire job. It is not a warm-up, not a code review, not a "let me get oriented" stroll through the files. It is the phase that produces the factual record of *what is actually here* — so that when Claude Code generates, it generates against a known state rather than a guessed one.

Treat the Audit as a gate. A gate has a binary condition: open or closed. The condition here is simple to state and unforgiving to fake:

> **The gate is closed until the Audit has produced (a) a complete inventory of existing assets, (b) a list of every naming and structural convention currently in use, and (c) a gap map between the current state and `DESIGN.md`. When all three exist and the Intent Layer is already populated, the gate opens.**

![Four audit conditions feeding a single barrier; one unmet condition holds the gate closed and walls off the Generate phase.](images/12-audit-what-exists-before-you-touch-anything-fig-01.png)

*Figure 12.1 — The Audit phase is a binary gate: all four conditions must hold, and one incomplete DESIGN.md keeps it CLOSED.*

Why a gate and not a guideline? Because repository-aware coding agents have changed the failure economics. [Medium — tool behavior, current-state] An agent like Claude Code can read your whole directory, infer patterns, and edit many files in one pass. That is enormously useful and exactly why the audit matters more, not less. An agent that infers the wrong pattern — that the ochre `#c08a2d` is the *intended* data color, say, because it appears forty times — will propagate that inference confidently across every new file. The polish of the output will hide the propagated error. The audit is the human act of establishing ground truth before the agent's inferences get a vote.

This echoes a lesson the machine-learning systems literature learned the hard way. Sculley and colleagues, writing about hidden technical debt in ML systems, observed that the most expensive failures are not the visible bugs but the *unmanaged dependencies and silent assumptions* that accumulate when artifacts are generated faster than they are understood. [High] An unaudited SVG directory is exactly that: a pile of generated artifacts carrying silent assumptions. The audit is debt service paid before the debt compounds.

---

## What the Audit produces: three artifacts

The Audit phase is not abstract reflection. It produces three concrete things, in order.

### 1. The asset inventory

You list every file that bears on the figure you will produce: SVGs, data files, the `DESIGN.md`, any `CLAUDE.md`, fonts, conversion scripts, and the PNG outputs if any exist. For each, you record what it is, when it was last touched, and whether it is a source of truth or a derived artifact. The distinction matters: a PNG is derived from an SVG; if you "fix" the PNG you have fixed nothing. Derived artifacts are downstream of decisions, not records of them.

You are not reading the files closely yet. You are taking attendance. The point is to know the full set before you privilege any one member of it — which is precisely the discipline the opening scene violated when it reached for "the cleanest-looking file."

![A source SVG produces a derived PNG; a futile edit to the PNG fixes nothing, while an unknown-provenance file is quarantined and not built upon.](images/12-audit-what-exists-before-you-touch-anything-fig-02.png)

*Figure 12.2 — Source of truth versus derived artifact: editing the PNG fixes nothing, and the unknown-provenance file is quarantined, not reused.*

### 2. The convention inventory

Now you read for patterns. What naming conventions are actually in use — not what the `DESIGN.md` says should be in use, but what is *there*? What color values appear, and are they tokens or hardcoded hex? What fonts are referenced? How are groups structured and named? Is there a semantic layer scaffold, or is everything flat?

You write these down as observed facts, value-neutral. `Groups named g, g-2, g-3 (auto-generated, non-semantic).` `Forty instances of fill="#c08a2d" (hardcoded; not tokenized).` `Axis labels: font-family="Arial" (not in the three-font stack).` You are building a description of reality, and reality includes the violations. You do not fix anything during the audit. Fixing during auditing is how you lose the record of what was wrong.

### 3. The gap map

This is where the convention inventory meets `DESIGN.md`. The gap map is a two-column reckoning: *what the specification requires* on one side, *what currently exists* on the other, and the delta named explicitly.

The gap map is the most valuable artifact the Audit produces, because it converts a vague unease ("this file is kind of a mess") into a finite, addressable list. A finite list can be checked off. A vague unease cannot. And — critically for the thesis of this book — the gap map is a human judgment product. An agent can list the hardcoded hex values. Whether a given hex value *is a gap* depends on whether `DESIGN.md` intended that color to be a token, and whether the previous designer's choice was a deviation or a documented exception. That determination is the design-intelligence layer. The agent supplies the inventory; you supply the standard against which it counts as a gap.

---

## Auditing naming against `CLAUDE.md`

The naming audit deserves its own treatment because it is where the SVG-to-Illustrator handoff lives or dies, and because it ties directly back to Chapter 7.

Recall the conflict from Chapter 7: SVG's rendering model (the painter's algorithm — later elements paint over earlier ones, so z-order *is* document order) is structurally in tension with the editorial grouping a designer needs when the file is opened in Illustrator. The resolution was a multi-layer architecture with semantic names: primary layers ordered by visual depth, semantic sub-layers within, and a `data-name` dual-attribute strategy so that human-readable names survive the round trip.

The naming audit checks whether the existing files honor that architecture. The `CLAUDE.md` for this stack specifies the rules; the audit finds the violations:

- **Auto-generated group names.** `g`, `g-2`, `Layer_1 copy` — these tell you the file was exported without semantic grouping, or that an agent generated it without a layer scaffold. In Illustrator's Layers panel they become an undifferentiated pile, and the editor cannot find "the annotation layer" because nothing is named the annotation layer.
- **ID character-escaping artifacts.** If you find an ID like `_x31_st-floor`, you are looking at the ghost of `1st-floor`. Illustrator (and the SVG spec's ID rules) cannot begin an ID with a digit, so the leading `1` gets escaped to `_x31_`. [High — documented SVG/Illustrator behavior, verify exact escaping against current Illustrator version] This is a naming-convention failure with a specific fingerprint, and the audit should flag every instance, because every one is a name a human will fail to recognize later.
- **Inconsistent casing or separators.** A mix of `dataLayer`, `data-layer`, and `data_layer` across files means there is no convention, only accidents. The audit names this so the Schema Layer can fix it.

The discipline: **name the violation, locate it, do not fix it during the audit.** The fix belongs to the Generate and Verify phases, against a populated Schema Layer. The audit's job is to make sure nothing is fixed in ignorance of the whole.

---

## Populating the Schema Layer of `PROJECT.md`

The Audit's three artifacts flow directly into the Schema Layer of `PROJECT.md`. Where the Intent Layer answers *what is this figure claiming and for whom* (and is human-authored, never overwritten by the agent), the Schema Layer answers *what is the current structural state of the project* — and it is the layer the agent may maintain, because it is a factual record, not a judgment.

The Schema Layer, populated from the audit of the economic-briefing directory, looks like this:

```markdown
## SCHEMA LAYER  (maintained from Audit phase; AI may update)

### Asset inventory
- regional-lending.svg        — SOURCE OF TRUTH (last edit: prev quarter)
- regional-lending.png        — DERIVED (regenerate; do not edit)
- default-rates.svg           — SOURCE; 3 hardcoded-hex violations
- final_v2_REAL_fixed.svg     — UNKNOWN PROVENANCE; quarantine, do not build on
- DESIGN.md                   — INCOMPLETE (typography section truncated)
- CLAUDE.md                   — ABSENT (must be authored before Generate)
- data/q3-lending.csv         — NEW; matches expected schema

### Conventions in use (observed)
- Color: hardcoded hex (#c08a2d ×40); NOT tokenized
- Fonts: EB Garamond (headline OK); Arial (axis — VIOLATION)
- Groups: g, g-2, g-3 (auto-generated; NON-SEMANTIC)
- IDs: one instance of _x31_st-floor escaping artifact

### Gap map (DESIGN.md required  →  current state)
- Seven-token palette          → hardcoded hex            [GAP]
- JetBrains Mono on axis ticks → Arial                    [GAP]
- Semantic layer names         → auto-generated groups    [GAP]
- WCAG 4.5:1 on all labels     → UNVERIFIED               [GAP]
- DESIGN.md complete           → typography truncated     [GAP — fix Intent]

### Phase-gate status
- Intent Layer:  POPULATED (Q3 brief approved)
- Schema Layer:  POPULATED (this section)
- DESIGN.md gap (typography) must be closed before gate opens.
- GATE: CLOSED — one blocking gap remains.
```

Notice what the gate status does. It does not say "looks good, proceed." It says the gate is *closed* because `DESIGN.md` itself is incomplete — the typography section was truncated, so there is no specified rule for the axis font to audit against. You cannot map a gap to a specification that does not exist. The audit surfaced a blocking condition that no amount of generation polish would have revealed, and it surfaced it *before* a single new bar was drawn.

This is the audit earning its keep. The most costly production failure is the one you discover after handoff, when the figure is in the briefing and an axis label fails contrast and the development authority's accessibility reviewer rejects the document. The audit moves that discovery to the cheapest possible moment.

---

## Worked example: auditing `default-rates.svg`

Let us run the worked example in the book's standard form, on the second file in the directory.

**Problem statement.** `default-rates.svg` renders a small-multiples grid of regional default rates. It looks correct in the browser. You must determine whether it can be the basis for the Q3 refresh, or whether it must be quarantined and regenerated.

**First attempt (what an unaudited reach produces).** A practitioner under deadline opens the file in the browser, sees the clean grid, and tells Claude Code: *"Update default-rates.svg with q3 numbers."* The agent reads the file, infers the structure, and updates the numbers. Output in two minutes. It looks right. It ships.

**Design diagnosis (what the audit finds).** Run against `CLAUDE.md` and `DESIGN.md`, the file shows five facts:

| Audit dimension | Specification (`DESIGN.md` / `CLAUDE.md`) | Current state | Finding |
|---|---|---|---|
| Color | Seven-token palette; no hardcoded hex | `fill="#c08a2d"` ×3 on emphasis cells | GAP |
| Encoding color count | ≤ 2 data-encoding colors | 3 hues across the grid | GAP — perceptual |
| Axis type | JetBrains Mono ticks | Arial | GAP |
| Group naming | Semantic, painter's-order layers | `g`, `g-4`, `g-7` | GAP |
| Contrast | WCAG 4.5:1 on all text | Light-grey caption: 3.1:1 measured | FAIL |

The "update the numbers" path inherits every one of these. The third hue is the worst, because it is not a code-cleanliness issue — it is a perceptual-accuracy issue. The grid uses three data-encoding colors where the design system permits two; a reader cannot reliably distinguish three categorical hues at small-multiple size, so the figure encodes a distinction the eye cannot recover. Data-accurate, perceptually false. The agent's "update" preserves the lie because the lie is invisible at the SVG surface.

**Corrected version (what auditing first produces).** The Schema Layer records `default-rates.svg` as: source structure unusable; three blocking gaps and one contrast failure; rebuild rather than patch. The figure is quarantined. The Q3 figure will be generated fresh against a completed `DESIGN.md`, with the third hue collapsed into a luminance or direct-label distinction. The audit cost twenty minutes. The unaudited path would have cost a rejected briefing.

**The lesson.** *Auditing is the act of refusing to inherit decisions you have not inspected.*

**The limit.** The audit can list the three hues. It cannot decide that three hues is one too many for *this* audience at *this* size — that judgment requires knowing the comparison the figure must support and the perceptual ceiling of categorical color. The tool inventories; you adjudicate.

---

## Why audit before generate, stated plainly

Three reasons, in descending order of how often they bite.

1. **Inheritance.** Generation against an unaudited state silently inherits the state's defects — its hardcoded colors, its non-semantic groups, its contrast failures. The polish of the new output hides the inherited rot.
2. **Overwrite.** A repository-aware agent can edit or overwrite files you did not intend it to touch. The inventory tells you which files are sources of truth and which are quarantined, so the agent's reach is bounded by a record rather than a guess. [Medium — current tool behavior]
3. **The phantom specification.** You cannot generate against a `DESIGN.md` you have not confirmed is complete. The audit's gap map catches the truncated typography section before generation builds on a rule that was never written.

The through-line: every one of these failures is *cheaper to catch in the audit than anywhere downstream.* That is the whole argument for the gate.

---

## Assessment: Audit Deliverable for the Terminal Project

**Type:** Required deliverable, ungraded on its own, but a prerequisite for the Pipeline Checkpoint in Chapter 13. A Pipeline Checkpoint submitted without a completed Audit deliverable is incomplete and is returned without a grade.

**Task.** For the directory that will become your terminal-project infographic, run a complete Audit phase and produce a populated Schema Layer in `PROJECT.md` containing all three audit artifacts:

1. **Asset inventory** — every relevant file, each marked SOURCE / DERIVED / UNKNOWN, with the last-edit signal and a one-line role.
2. **Convention inventory** — every naming, color, font, and grouping convention *observed* in the files (not prescribed), recorded value-neutrally, with violations located by file and line where possible.
3. **Gap map** — a two-column reckoning of `DESIGN.md` requirements against current state, each delta tagged `[GAP]`, `[FAIL]`, or `[OK]`.
4. **Phase-gate status** — an explicit OPEN / CLOSED determination, with any blocking gap named.

**Constraint.** You may use Claude Code to *generate the inventory* (list files, extract hex values, find non-semantic group names). You may not use it to decide whether a given observation counts as a gap. Your AI Use Disclosure for this deliverable must name at least two judgments you supplied that the agent could not: for example, *deciding that the third encoding hue is a perceptual gap rather than a stylistic choice*, and *deciding that an unknown-provenance file must be quarantined rather than reused.*

**Deliverable.** The `PROJECT.md` Schema Layer section, plus a one-paragraph gate determination. (Ungraded; gates the 100-point Pipeline Checkpoint.)

---

## Chapter summary

You can now run the Audit phase as a phase gate rather than a courtesy. You can produce the three audit artifacts — asset inventory, convention inventory, gap map — and you understand why each precedes generation. You can locate naming-convention violations against `CLAUDE.md`, including the auto-generated-group and `_x31_`-escaping fingerprints that tie back to Chapter 7's painter's-algorithm conflict. You can populate the Schema Layer of `PROJECT.md` from the audit, and you can make the binary gate determination — open or closed — that protects every downstream phase from inheriting an unaudited state.

## Key terms

- **Audit phase** — the first phase of the Brutalist pipeline; produces the factual record of the current project state.
- **Phase gate** — the binary condition (both Intent and Schema Layers populated) that must be met before generation begins.
- **Asset inventory** — the complete list of relevant files, each marked as a source of truth or a derived artifact.
- **Gap map** — the two-column reckoning of `DESIGN.md` requirements against observed current state.
- **Schema Layer** — the section of `PROJECT.md` recording structural state; agent-maintainable because it is factual, not judgmental.
- **Derived artifact** — a file (e.g., a PNG) produced downstream of a source; editing it fixes nothing upstream.
- **Quarantine** — marking an unknown-provenance or defect-laden file as not-to-be-built-upon.

## Bridge

The Audit is complete and the gate is open: Intent Layer populated, Schema Layer populated, `DESIGN.md` confirmed complete, gaps mapped. Now comes the hardest demonstration in the book. In Chapter 13 you give the specification to Claude Code and watch what happens when the agent generates *with* it versus *without* it. The gap between specification-driven and specification-less output is not something you will be told. It is something you will see, on eleven counts, in a single before-and-after.

---

## AI Wayback Machine: Ida B. Wells and the audit before the argument

Before she published *The Red Record* in 1895, Ida B. Wells did something that looks, in retrospect, exactly like an audit phase. [High — historical record; verify specific figures against a primary biography] She did not begin with the visual or rhetorical artifact. She began by inventorying what existed: she compiled lynching statistics from the records of white-owned newspapers — sources hostile to her conclusion — precisely because their provenance made the count unassailable. She named her conventions (what counted, what was excluded, where each figure came from) before she made her claim.

The parallel to this chapter is not decorative. Wells understood that the *authority of a visual or statistical artifact rests on the integrity of the state it was built from* — and that the most persuasive move is to audit the existing record, hostile sources included, before generating the argument. An engineer who reaches for "the cleanest-looking file" and refreshes it is doing the opposite: generating before auditing, inheriting a provenance they never inspected.

Try this prompt with an LLM: *"Explain how Ida B. Wells's practice of compiling lynching statistics from hostile white-owned newspapers parallels the discipline of auditing an existing SVG project state before generating against it. Where does the parallel hold, and where does it break down?"* Read the answer as a draft to interrogate, not a fact to trust — exactly the posture this chapter teaches toward a plausible SVG.

---

## Sources

- Anthropic. *Claude Code documentation.* Anthropic Docs (current). [verify before each course offering — high aging risk]
- D3 Team. *D3 selections and `selection.join` documentation.* d3js.org (current).
- Sculley, D., et al. (2015). *Hidden Technical Debt in Machine Learning Systems.* NeurIPS. — Source for the production-debt analogy.
- Gebru, T., et al. (2021). *Datasheets for Datasets.* Communications of the ACM. — Provenance-documentation model adapted to the asset inventory.
- W3C SVG Working Group. *Scalable Vector Graphics (SVG) 2 Specification.* W3C (current). — ID and naming rules behind the `_x31_` escaping fingerprint.
- Wells, I. B. (1895). *The Red Record.* — Wayback figure; [verify specific statistics against a primary biography].
- Adobe. *Illustrator documentation: SVG import and layer behavior.* Adobe Help (current). [verify escaping behavior against current Illustrator version]
