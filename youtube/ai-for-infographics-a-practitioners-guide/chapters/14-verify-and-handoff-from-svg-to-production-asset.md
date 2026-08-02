# Chapter 14 — Verify and Handoff: From SVG to Production Asset

## Learning objectives

By the end of this chapter you will be able to:

1. (Apply) Run the Verify phase against the four-category checklist: structure, text, styling, and naming.
2. (Apply) Open a D3-generated SVG in Illustrator (or Inkscape), release all clipping masks, verify group names, correct text alignment, and save as `.ai`.
3. (Apply) Run `node SCRIPTS/svg-to-png.mjs` to produce 300 DPI PNG output.
4. (Evaluate) Produce the complete AI Use Disclosure for the terminal project, naming the design decisions that required human judgment.

---

## Opening: the file that passed every check and still was not done

Your Pipeline Checkpoint SVG from Chapter 13 passed all four `CLAUDE.md` checklist categories. Tokens, not hex. Semantic groups. JetBrains Mono on the ticks. Painter's order correct, band behind line. Metadata block present. The browser renders it perfectly. By every automated measure it is clean.

It is the infrastructure-and-operations figure: a regional grid's load-shed events plotted against time of day, with a callout on the evening peak. You hand it to the editor who will place it in the operations report. Ninety seconds later they send it back with a screenshot from Illustrator, and three things are wrong that the browser never showed you.

First, the evening-peak callout text, which sat perfectly right-aligned in the browser, is now floating fifteen pixels to the left of where it belongs. Second, the whole `ci-band` layer is wrapped in a clipping mask — when the editor tries to nudge the band, the mask fights them, and releasing it is not obvious. Third, opening the Layers panel reveals that your beautiful `estimate-line` and `annotation` groups are *there*, but nested three deep inside an unnamed `<g>` that Illustrator created on import, so the editorial structure you built is buried under a structural artifact you did not author.

None of these are failures of your generation. They are the **gap between a browser-correct SVG and a production-editable asset** — the gap the Verify and Handoff phases exist to close, and the gap most pipelines skip entirely. A pipeline that stops at "it renders" ships the editor a file they cannot edit. This chapter is the two phases that turn the SVG into something a production team can actually work with: human verification against the spec, then the round trip through a vector editor.

![A browser-correct SVG hides drifted text, a fighting clip, and buried groups; the skipped round-trip bridge releases clips, reconciles names, and corrects drift to produce a production-editable file with named layers.](images/14-verify-and-handoff-from-svg-to-production-asset-fig-01.png)

*Figure 14.1 — Browser-correct is not production-editable: the round trip through a vector editor is the step most pipelines skip and the one that produces the editable named-layer asset.*

The research framing for this chapter is blunt about it: *students who skip the Verify phase are not using AI tools; they are being used by them.* The corrections you are about to make are not the tool's failures. They are the human judgment layer in the pipeline — the part no checklist automates.

---

## The Verify phase: a human reads the spec into the output

The Generate-time checklist (Chapter 13) is a *machine-checkable* pass: it catches hardcoded hex, missing tokens, anonymous groups — things you can grep for. The Verify phase is the *human* pass. It asks a question grep cannot: *does this output do what the specification said it should do?* That is a judgment about meaning, not a pattern match.

Verify runs against four categories. The first three overlap the generation checklist deliberately — verification is belt-and-suspenders, because the cost of a missed defect rises sharply after handoff.

- **Structure.** Named groups present and in painter's order; a correct `viewBox`; explicit width and height; the band-behind-line invariant intact; no orphaned or empty groups.
- **Text.** Every label is a real `<text>` element (not outlines, not a raster); the font families are the three-font stack; `text-anchor` is set correctly and — the subtle one — *will survive export* (more below); no `<tspan>` whitespace-collapse damage to multi-word labels.
- **Styling.** Visual properties are presentation attributes, not inline `.style()`; every color is a token; contrast meets WCAG 4.5:1 on all text, measured, not eyeballed; opacity is not silently compounding (`opacity` × `fill-opacity` multiply).
- **Naming.** Semantic IDs throughout; no `g-2` auto-names; no `_x31_` escaping artifacts; `data-name` attributes present on anything that must arrive in Illustrator with a human-readable name.

The Verify phase produces a *correction list* — a written record of what must change before handoff. Crucially, you verify the output against the *specification*, not against your memory of what you intended. Open the CAJAL metadata block and the SCOPE side by side with the rendered figure. The metadata says `AXIS: y begins at 0`. Does it? The SCOPE says `Exclusions: legend`. Is there a legend hiding in a layer? Verification is the disciplined act of holding the artifact accountable to its own stated commitments.

---

## The step most pipelines skip: the Illustrator (or Inkscape) round trip

Here is the claim this chapter is built to defend: **a browser-correct SVG is not a production asset until it has survived a round trip through a vector editor and come out editable.** [High — this is the book's production stance; specific tool behaviors are current-state and version-sensitive]

Most AI-assisted infographic pipelines stop at the browser. The SVG renders, looks great, gets dropped into a slide or a PDF, and ships. This works right up until someone needs to change it — adjust a label, recolor for a different publication, fix a number for a correction — and discovers the file is a thicket of clipping masks and anonymous groups. The editability you assumed was free was never checked. The Handoff phase checks it, by doing the edits a production team will need to do.

### Why the conflict from Chapter 7 surfaces here

This is where the painter's-algorithm-versus-editorial-grouping conflict from Chapter 7 stops being theory and becomes something your hands do.

Recall the conflict. SVG renders by the painter's algorithm: document order *is* z-order, later elements paint over earlier ones. So the *rendering* structure is dictated by visual depth — background first, marks next, annotation last. But the *editorial* structure a designer needs in Illustrator is organized by meaning — "all the annotation in one named layer I can find and recolor." In Chapter 7 you learned the resolution: a multi-layer architecture where the painter's-order layers are *also* the semantically named editorial layers, with `data-name` carrying human-readable names through the export.

The Handoff phase is where you find out whether that resolution held. When Illustrator imports the SVG, it tries to reconcile SVG's grouping with its own layer model — and the reconciliation is imperfect. [Medium — Illustrator import behavior, verify against current version] Your painter's-order semantic layers may import as named layers (the win), or Illustrator may wrap them in an unnamed parent group (the opening-scene defect), or it may convert a `<g>` with a clip into a clipping mask that occludes your intent. The round trip is the test of the Chapter 7 architecture under the one condition that matters: a real editor opening a real file.

### The Illustrator workflow, step by step

1. **Open the SVG in Illustrator.** Use *Open*, not *Place* — *Place* embeds the SVG as a linked or rasterized object you cannot edit; *Open* parses it into editable objects.
2. **Release all clipping masks.** `Object → Clipping Mask → Release`, applied to every clipped group. D3 and the export pipeline frequently wrap layers in clips that constrain rendering to the chart area. In Illustrator those clips fight the editor. Releasing them restores direct manipulation. (Inkscape: `Object → Clip → Release`.)
3. **Verify group names in the Layers panel.** Confirm `ci-band`, `estimate-line`, `annotation` arrived as named layers. If Illustrator wrapped them in an unnamed parent `<g>`, ungroup the parent (preserving the children) or rename it. This is the manual reconciliation of the Chapter 7 conflict — the editorial structure restored by hand because the import flattened it.
4. **Correct text alignment.** This is the opening scene's first defect and it has a specific cause. The `text-anchor` attribute (`start`/`middle`/`end`) tells the renderer where to anchor the text relative to its `x` coordinate. The browser honors it live. But on some export/import paths Illustrator *bakes the rendered position into the coordinates and drops the `text-anchor` attribute* — so a right-anchored label that was positioned by its anchor now sits at its raw `x`, shifted by its own width. [Medium — the `text-anchor` export mismatch; verify against current Illustrator version] The fix is manual: re-align the affected labels. Verify against the spec, not the imported position.
5. **Check `<tspan>` whitespace.** Multi-word labels split across `<tspan>` elements can lose their inter-word spacing to whitespace collapse on import. [Medium — verify against current version] Confirm "Evening Peak" did not become "EveningPeak."
6. **Save as `.ai`.** The native format preserves the editable structure for the production team. The `.ai` is now the editable source of truth for handoff; the original SVG remains the generation artifact.

### The one-way ticket and the exponential nesting bug

There is a reason you do not bounce a file back and forth between Illustrator and SVG repeatedly. Each round trip can re-wrap groups in new parent `<g>` elements and re-introduce clips, and the nesting *compounds* — a file round-tripped several times accumulates layers of anonymous wrapper groups, growing roughly geometrically, until the structure is unnavigable. [Medium — the exponential nesting behavior; verify against current versions] This is why the pipeline treats Illustrator as a **one-way ticket**: SVG is generated once, imported once, corrected once, and saved as `.ai`. If the figure needs a structural change, you fix the *specification* and regenerate the SVG — you do not re-export from Illustrator back to SVG and re-import. Regeneration is cheap (Chapter 13); fighting accumulated nesting is not.

![The disciplined one-way path imports once into a shallow clean .ai; the repeated round-trip path accumulates anonymous wrapper groups whose nesting depth grows 1 to 2 to 4 to 8 until unnavigable, with regenerate-from-spec offered as the cheap alternative.](images/14-verify-and-handoff-from-svg-to-production-asset-fig-02.png)

*Figure 14.2 — The one-way ticket: repeated SVG↔Illustrator round trips compound anonymous nesting geometrically, so structural changes go back to the spec and regenerate.*

### Inkscape as the no-license alternative

Not every student or institution has an Adobe license. Inkscape is a capable, free, open-source vector editor, and the workflow maps almost one-to-one: *Open* the SVG, `Object → Clip → Release`, verify the named groups in the XML editor or Objects panel, correct alignment, and save (Inkscape's native `.svg` with its layer metadata serves the role `.ai` does for Illustrator). [Medium — Inkscape behavior, verify against current version] The conceptual phase is identical; only the menu paths differ. Where this chapter says Illustrator, an Inkscape user reads their own tool.

---

## The conversion: SVG/`.ai` to 300 DPI PNG

The final Handoff artifact is usually a raster at print resolution, because the destination — a report, a slide, a journal figure — needs a fixed-resolution image. The pipeline scripts this so it is reproducible rather than a manual export anybody can get wrong.

```bash
node SCRIPTS/svg-to-png.mjs --in figure.svg --out figure.png --dpi 300
```

The script (built on a headless renderer such as `sharp` or `resvg`) reads the SVG and rasterizes at 300 DPI. [Medium — script/dependency behavior is current-state; `npm install` documented in Chapter 11] Two things to watch, both tying back to earlier chapters:

- **The DPI mismatch (Chapter 4).** SVG's user unit defaults to 96 DPI in CSS contexts but 72 DPI in some print contexts; the conversion must declare the target DPI explicitly so the physical dimensions come out right. A figure that is "the right size" on screen can rasterize at the wrong physical size if the DPI is implicit. The `--dpi 300` flag makes it explicit.
- **Convert from the source of truth, not a derived artifact (Chapter 12).** Rasterize from the verified SVG (or an SVG re-exported deliberately), never from a screenshot. A PNG made from a screenshot inherits the screen's resolution and the browser's anti-aliasing, and it is downstream of nothing you can re-edit.

The PNG is a *derived artifact*. If the figure changes, you regenerate the PNG from the source; you never edit the PNG. This is the Chapter 12 source-versus-derived distinction enforced at the end of the pipeline.

---

## Worked example: verifying and handing off the load-shed figure

**Problem statement.** Take the infrastructure-and-operations load-shed SVG — Generate-checklist-clean — through Verify and Handoff to a production-ready `.ai` and a 300 DPI PNG.

**First attempt (skip Verify, ship the SVG).** The browser renders it perfectly; it is dropped straight into the operations report PDF. Two weeks later a number is corrected and the editor must shift the evening-peak callout. They open the SVG in Illustrator and hit all three opening-scene defects: drifted text, a fighting clip, buried groups. The "finished" figure costs an afternoon of reverse-engineering.

**Design diagnosis (run the Verify phase).** The four-category pass and the round trip surface this:

| Phase | Category | Finding | Correction | Remaining risk |
|---|---|---|---|---|
| Verify | Structure | Painter's order intact; one empty `<g>` | Delete empty group | None |
| Verify | Text | `text-anchor="end"` on callout; spec OK in browser | Flag for export check | Export may drop anchor |
| Verify | Styling | Contrast on grey caption = 4.6:1 | None (passes) | None |
| Verify | Naming | All semantic; no `_x31_` | None | None |
| Handoff | Clip | `ci-band` wrapped in clipping mask | Release clip | None |
| Handoff | Layers | Named groups under unnamed import parent | Ungroup parent, keep names | None |
| Handoff | Text | Callout drifted left on import (anchor dropped) | Re-align to spec position | Re-verify after any edit |
| Handoff | Convert | — | `svg-to-png.mjs --dpi 300` from `.ai`-source SVG | PNG is derived; never edit |

**Corrected version.** A clean `.ai` with named, clip-free, correctly aligned layers, and a 300 DPI PNG generated from the source. The editor opens the `.ai`, finds `annotation`, shifts the callout in five seconds.

**The lesson.** *Verification is reading the specification back out of the artifact; handoff is proving a human can still edit what the machine produced.*

**The limit.** The script rasterizes and the editor releases clips mechanically — but deciding that the drifted callout is *wrong* requires knowing where the spec said it should be, and deciding the grey caption's 4.6:1 is *acceptable* requires knowing the audience and medium. The tools execute the corrections; the human owns the standard of "correct."

---

## The AI Use Disclosure: from two decisions to a habit

Every deliverable in this course carries an AI Use Disclosure naming at least two design decisions that required human judgment the AI could not supply. By Chapter 14 you have produced several. The Verify and Handoff phases are unusually rich sources of such decisions, because verification is *itself* the human-judgment layer made explicit:

- *Deciding that the imported callout position was wrong* — the agent and the importer both produced a position; only a human holding the spec knew it was the wrong one.
- *Deciding the 4.6:1 contrast was acceptable for this medium* — the number is measured automatically; the judgment that it clears the bar for this audience and print context is not.
- *Deciding to release a clip rather than work around it* — a structural-editability judgment about what the production team will need.

For your Pipeline Checkpoint figure, write the Verify/Handoff disclosure now. It is rehearsal: the Chapter 15 final project raises the bar to *three* decisions across the whole pipeline, and the Verify phase is where you learn to see them.

---

## Assessment: Design Critique #5 — Peer Verify (25 points)

**Task.** Run a complete Verify phase on *another student's* Pipeline Checkpoint SVG (Chapter 13), then take it one step into Handoff.

**Deliverables.**

1. **A four-category Verify correction list** — structure, text, styling, naming — with every finding located by file/line or layer, marked PASS / CORRECT / FAIL, exactly as you would hand it to the figure's author. [12 pts]
2. **A handoff finding** — open the SVG in Illustrator or Inkscape, attempt to release clips and confirm named groups, and report at least one editability defect (or confirm, with evidence, that none exists). [8 pts]
3. **A one-paragraph judgment** — would you ship this figure to a production editor as-is? Defend the yes or no against the specification, not against how the figure looks in the browser. [5 pts]

**Constraint.** You may use an agent to extract the SVG structure and measure contrast. You may not use it to write the ship/no-ship judgment; that is the design-intelligence act being assessed. Disclose the split.

---

## Chapter summary

You can now run the Verify phase as a human pass that holds the artifact accountable to its specification across structure, text, styling, and naming — the pass grep cannot do. You can take a browser-correct SVG through the round trip that turns it into a production asset: open (not place) in Illustrator or Inkscape, release clipping masks, reconcile the named groups against Illustrator's import wrapping, correct the `text-anchor` drift, and save as an editable source. You understand why this is a one-way ticket — the exponential nesting bug — and why regeneration beats re-export. You can produce a 300 DPI PNG from the source via `svg-to-png.mjs`, with DPI declared explicitly. And you can write an AI Use Disclosure that names the verification and handoff judgments only a human could make.

## Key terms

- **Verify phase** — the human pass that checks the output against its specification across four categories.
- **Handoff phase** — the round trip through a vector editor that turns a browser-correct SVG into a production-editable asset.
- **Clipping mask** — a group-level clip that constrains rendering; must be released for editing.
- **`text-anchor` export mismatch** — Illustrator baking rendered position into coordinates and dropping the anchor attribute, drifting the label.
- **One-way ticket** — the rule that SVG is imported to Illustrator once; structural changes go back to the spec and regenerate.
- **Exponential nesting bug** — the geometric accumulation of anonymous wrapper groups across repeated round trips.
- **Derived artifact** — the PNG; regenerated from the source, never edited.
- **300 DPI PNG** — the print-resolution raster, produced with DPI declared explicitly via `svg-to-png.mjs`.

## Bridge

You now have every phase: Audit, Generate, Verify, Handoff. Each has been practiced on a fragment. Chapter 15 is the assembly — one brief, every decision, the complete pipeline run end to end into a production package you defend in a design review. It is where the book lands.

---

## AI Wayback Machine: Susan Kare and the editability nobody sees

When Susan Kare designed the original Macintosh icons in the early 1980s, she worked on grid paper, pixel by pixel — the trash can, the watch, the smiling computer. [High — well-documented design history] The icons are remembered as charming. What is less remembered is the production discipline underneath: each icon had to survive at a fixed, tiny resolution, on hardware with brutal constraints, *and remain a clean, editable artifact a team could revise*. Kare was not just making pictures look right on one screen. She was producing assets that had to hand off — to the OS, to other designers, to future revisions — without falling apart.

That is exactly the distinction this chapter draws. A figure that looks right in one viewer is not the same as a figure that survives handoff. Kare's icons endure because they were built as production assets, not screenshots — editable, fixed-resolution, defensible against revision. An AI-generated SVG that renders beautifully in a browser but collapses into clipping masks and anonymous groups when an editor opens it has the opposite property: it looks right and cannot be handed off. The Verify and Handoff phases are how you build the Kare property in on purpose.

Try this prompt with an LLM: *"Susan Kare's Macintosh icons had to be both visually correct at low resolution and editable production assets a team could revise. Explain how that dual requirement parallels the distinction between a browser-correct SVG and a production-editable asset, and name one way the analogy is imperfect."* Read the answer as a draft to verify, not a fact to accept.

---

## Sources

- W3C SVG Working Group. *Scalable Vector Graphics (SVG) 2 Specification.* W3C (current). — Grouping, text, `text-anchor`, presentation attributes.
- Eisenberg, J. D., & Bellamy-Royds, A. (2018). *SVG Essentials* (2nd ed.). O'Reilly.
- Adobe. *Illustrator documentation: SVG import/export, clipping masks, layer behavior.* Adobe Help (current). [verify import, `text-anchor`, and nesting behavior against current version]
- Inkscape Project. *Inkscape documentation: clip release and layers.* inkscape.org (current). [verify against current version]
- W3C WAI. (2023). *Web Content Accessibility Guidelines (WCAG) 2.2.* W3C Recommendation. — 4.5:1 contrast requirement. [access date at final draft]
- Brewer, C. *ColorBrewer 2.0.* Penn State. — Palette reference for handoff recoloring.
- Hertzfeld, A. *Folklore.org: Macintosh stories.* — Wayback figure (Susan Kare's icon work); [verify specific details against a primary source].
