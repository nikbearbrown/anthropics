# Chapter 4 — SVG as a Design Medium

## Opening: Three machines look at the same file

A second-year MS student named Priya has an SVG she is happy with. She asked Claude Code to produce a figure for an economics paper — a bar chart showing the divergence between median and mean household income over four decades — and the agent returned something polished. In the browser, it looks publishable: clean bars, a tidy axis, a headline in a serif face. She drops it into her draft and moves on.

Three weeks later her advisor asks her to change one thing: make the median series the visual anchor and push the mean into a supporting role. A two-minute edit, in principle. Priya opens the file in Illustrator to nudge the colors and the label weights.

What she sees is not a figure. It is a flat pile of forty-one anonymous groups named `g`, `g`, `g`, nested six deep, with the headline text broken into individual glyphs because the exporter outlined the font. The bars she wants to recolor are not "the bars" — they are paths scattered across three different clipping masks, and the clipping masks repaint the moment she tries to move anything. She spends ninety minutes and gives up. She rebuilds the chart from scratch.

Here is the thing worth sitting with: **the file was correct.** Every byte rendered exactly as intended in the browser. The data was accurate. The encoding was defensible. And it was still a dead end — because "renders correctly" and "can be edited" are answers to two different questions, asked by two different machines, and the file only satisfied one of them.

This chapter is about holding both questions in view at once. [High]

## SVG means three different things

The acronym is honest: Scalable Vector Graphics. But the *thing* the acronym names looks different depending on who — or what — is reading it.

**To a browser, SVG is a rendering instruction.** The browser parses the document top to bottom, builds a tree, walks that tree, and paints pixels. It does not care what your groups are named. It does not care whether your text is live or outlined, whether your structure is three levels deep or thirty. It cares about one thing: does the final raster match the spec? If the bytes are valid and the geometry resolves, the browser is satisfied. Surface polish is the browser's *entire* job. [High]

**To a code generator, SVG is a serialization target.** When Claude Code or D3 emits SVG, it is translating a data structure — an array bound to DOM nodes, a set of scales, a layout function — into markup. The generator optimizes for what is easy to *produce*, not what is easy to *edit later*. D3's `.join()` pattern, for instance, will happily emit a hundred sibling `<rect>` elements inside one undifferentiated `<g>` because that is the natural shape of a data join. The generator has no concept of "the median series should be its own editable layer." That concept lives in the design intelligence layer — which is to say, in your head. [High]

**To a designer, SVG is a document with structure and intent.** A designer opening a file in Illustrator expects layers that mean something: a layer called `annotations`, a group called `median-series`, text that is still text. The designer's mental model is editorial — organized by what things *are*, not by what order they happen to paint in.

The central problem of this chapter — and, arguably, of the whole production half of this book — is that these three readers want incompatible things, and **only the human can reconcile them.** The browser will accept anything that renders. The code generator will produce anything you can specify. The reconciliation — "render correctly *and* stay editable" — is a judgment call that no current code generator makes on its own. That reconciliation is part of the irreducibly human design layer. [Medium]

![A diagram of one SVG file branching to three readers — browser (cares about a valid raster), code generator (cares about easy serialization), and designer (needs named layers and live text) — all feeding a red-bordered reconciliation band labeled as the irreducibly human judgment.](images/04-svg-as-a-design-medium-fig-01.png)

*Figure 4.1 — One file, three readers: the browser, the generator, and the designer each want incompatible things, and only a human reconciles "renders correctly" with "stays editable."*

## The document object model, briefly and concretely

Strip away the mystique and an SVG is a small set of elements you can learn in an afternoon.

- `<svg>` is the root. Its `viewBox` defines the coordinate system — `viewBox="0 0 800 500"` means "the canvas is 800 units wide and 500 tall, and the origin is top-left." Everything inside is positioned in those units.
- `<g>` is a group. It is the only structural element that matters for editability. A `<g>` can carry an `id`, a transform, and shared presentation attributes that its children inherit. Groups are what become *layers and sub-layers* when the file reaches Illustrator.
- `<rect>`, `<circle>`, `<line>`, `<path>` are the marks. `<path>` is the universal one — it can draw anything via its `d` attribute, which is why generators lean on it heavily, and why a path-heavy file is often a sign that semantic structure was never specified.
- `<text>` holds live, selectable, re-typeable type. `<tspan>` is a span inside it for styling fragments. Live text is fragile across the export boundary — hold that thought; it returns in Chapter 8.
- `<defs>` is the closet: reusable definitions — markers (arrowheads), clip paths, gradients — defined once and referenced by `id`.

That is most of it. The Brutalist system uses a deliberately small vocabulary of these, which is part of why its output survives the round-trip better than a baroque export does.

### The viewBox and the DPI mismatch

One concrete trap belongs here because it bites at generation time. SVG's internal coordinate system is unitless until something maps it to physical space. Illustrator historically treats SVG user units as points at **72 units per inch**; many web and CSS contexts assume **96 units per inch**. The same `width="800"` therefore lands at a different physical size depending on which machine reads it. [Medium — verify exact Illustrator behavior against the current version during drafting; Adobe's import handling is version-sensitive] If your pipeline ends in a 300-DPI PNG for print, the safe move is to define the `viewBox` explicitly and set physical dimensions deliberately at conversion time (the `svg-to-png.mjs` step in Act Three), rather than trusting any default. The mismatch is not a bug to fix; it is a boundary to specify across.

## How the SVG tree maps to Illustrator's layers

Illustrator's Layers panel is a tree. So is an SVG. The correspondence is almost one-to-one, and that is the good news: a `<g id="annotations">` in the source becomes a group named `annotations` in the panel; a `<g>` nested inside it becomes a sub-layer. If you name your groups, Illustrator shows you those names. If you do not, Illustrator shows you `<Group>`, `<Group>`, `<Group>` — and the editor is now navigating a structure that encodes nothing.

This is the single highest-leverage decision available at generation time, and it costs almost nothing: **give every structural group a semantic `id`.** Not `g1`. Not `layer_4`. `median-series`. `axis-x`. `callout-2008`. The browser ignores the names. The designer lives by them. You are writing for the second reader even though only the first one renders. [High]

There is a wrinkle worth naming now and developing in Chapter 7: Illustrator does not import an `id` verbatim. It escapes characters that are illegal in its internal naming, so an `id="2008-spike"` can re-emerge as `_x32_008-spike`, because an XML name token cannot begin with a digit and Illustrator hex-escapes the offender. The fix is to author IDs that are already legal — start with a letter, use hyphens, avoid leading digits and spaces — and, in the Brutalist convention, to carry a parallel human-readable `data-name` attribute that survives untouched. The `id` is for the machine; the `data-name` is for the person. That dual-attribute strategy is the backbone of the editable-handoff design and we return to it in Chapter 7.

## Presentation attributes versus inline CSS

There are two ways to color a bar in SVG, and they are not equal at the export boundary.

```svg
<!-- Presentation attribute -->
<rect x="0" y="0" width="40" height="120" fill="#C8102E"/>

<!-- Inline CSS via style -->
<rect x="0" y="0" width="40" height="120" style="fill:#C8102E"/>
```

In the browser, these render identically. At the handoff, they do not. Illustrator reads the presentation attribute (`fill="..."`) reliably and maps it to the object's appearance. The inline `style` attribute is read less predictably across versions and tools, and CSS that lives in a `<style>` block elsewhere in the document can be flattened, ignored, or partially applied. The Brutalist convention is therefore strict: **write visual properties as presentation attributes, not as styles, and never as separate stylesheets in production SVG.** [Medium — exact Illustrator style-handling is version-sensitive; verify]

This has a direct consequence for how you drive D3 in Act Three. D3 lets you set appearance two ways: `.attr("fill", ...)` writes a presentation attribute; `.style("fill", ...)` writes inline CSS. They look the same in the browser. Only the first survives the trip to Illustrator. The CLAUDE.md constitution in Act Three encodes this as a hard rule — no `.style()` for visual properties — precisely because the failure is invisible until a human opens the file in the editor.

## The clipping-mask problem and the one-way ticket

Generators love clipping. To keep a series of bars from spilling past the plot edge, D3 commonly wraps them in a `clipPath` referenced by the group. In the browser this is invisible and free. In Illustrator it is a wall.

A clip path arrives as a "clipping mask," and a clipping mask locks the geometry it governs: try to move a clipped object and the mask repaints, or the object vanishes below the mask boundary, or the whole group resists selection. The standard Illustrator remedy is to *release* every clipping mask before editing — Object → Clipping Mask → Release — which is exactly the manual correction the Act Three Verify phase budgets for. It is not optional cleanup; it is the price of admission to editing AI-generated SVG. [Medium — verify current Illustrator menu path and behavior]

This is also where the **one-way ticket principle** comes from. Once you have opened an SVG in Illustrator, released its masks, fixed its names, and saved as `.ai`, you should treat that `.ai` as the new source of truth and *not* regenerate the SVG over it. Re-running the generator and re-importing tends to compound nesting — Illustrator wraps the already-wrapped structure, doubling group depth each round-trip until the file becomes unmanageable. Generation is upstream; Illustrator editing is downstream; the river runs one way. Designing for that one-way trip is itself a human decision, because the tool will happily let you run it backward until the file collapses. [Medium]

## Worked example: one figure, three states

The research for this chapter calls for a three-representation display. Here is the same economic figure — median versus mean household income — tracked across the boundary, with the design intent, the generated structure, the verification finding, the correction, and the residual risk for each issue.

| Design intent | Generated structure | Verification finding | Correction | Remaining risk |
|---|---|---|---|---|
| Median series is the editable anchor | All bars in one `<g>` of `<rect>`s; no per-series group | Cannot select "the median bars" as a unit in Illustrator | Author two semantic groups: `median-series`, `mean-series` | None if regenerated under spec |
| Headline stays re-typeable | Headline exported as outlined `<path>` glyphs | Text is no longer text; cannot fix a typo | Re-emit as live `<text>` in EB Garamond stack | Live text may shift on a machine missing the font |
| Bars stay movable | Plot wrapped in `<clipPath>` | Bars locked; move attempts repaint the mask | Release clipping mask before edit (Verify phase) | Manual step; easy to forget — checklist enforced |
| Layers readable by a stranger | Groups named `g`, `g`, `g` | Layers panel encodes nothing | Add `id` + `data-name` to every structural group | Leading-digit IDs hex-escape — author legal IDs |
| Print at 300 DPI | `width="800"` with no explicit physical size | 72-vs-96 unit ambiguity | Set `viewBox` and fix dimensions at PNG conversion | Version-dependent default sizing |

The lesson, in one sentence: **the browser-correct file and the production-ready file are not the same artifact, and the difference is entirely in structure the browser never reads.** [High]

The limit, in one sentence: every one of these corrections is a judgment the code generator could not have made for you, because each depends on what the figure *is for* — which series is the argument, which text is editorial, what the file's downstream life looks like — and none of that is recoverable from the rendered pixels.

## Assessment — Design Critique #2 (25 points)

**Title: "Browser-Correct, Production-Broken."**

Obtain a D3-generated or AI-generated SVG infographic — from the instructor's production repository, from a coding agent you prompt yourself with a deliberately vague brief, or from a public source (redraw if rights require it). Open it in three states: rendered in a browser, raw in a text editor, and imported into Illustrator or Inkscape.

Produce a two-page critique that:

1. States what the figure *claims* and whether the visual structure supports that claim (one paragraph).
2. Lists at least four structural editability failures, each named with the specific mechanism (anonymous groups, outlined text, clipping mask, inline style instead of presentation attribute, leading-digit ID escaping, DPI ambiguity).
3. For each failure, specifies the generation-time decision that would have prevented it.
4. Closes with an **AI Use Disclosure** naming at least two decisions in your critique that required human judgment a code generator could not have supplied — for example, deciding which series *should* have been the anchor, or judging which text was editorial versus decorative.

Deliverable: a two-page critique with the three-state evidence and a completed AI Use Disclosure. (25 points)

## AI Wayback Machine — Tim Berners-Lee

> **Why a web pioneer belongs in a chapter about editable files.** Tim Berners-Lee did not invent SVG, but he established the principle that made SVG possible: that a document on the web should be *structured text a machine can parse and a human can read*, not an opaque binary blob. SVG is a direct descendant of that commitment — a graphic that is also a document, with named parts, an inspectable tree, and meaning that survives outside any single rendering engine.
>
> The connection to this chapter is exact. Priya's failure was a failure of *structure*, not of *rendering* — and structure-as-meaning is the web's founding bet. An infographic that renders but cannot be edited has, in a sense, betrayed that bet: it has become a picture pretending to be a document.
>
> Try this prompt with an AI assistant: *"Explain how Tim Berners-Lee's principle of structured, readable web documents helps an engineer recognize why a browser-correct SVG can still be a production dead end."* Then check the answer against this chapter. The model will likely connect structure to editability; the judgment about *which* structure encodes *your* editorial intent is the part it cannot supply for you. [Verify Berners-Lee's exact Wikipedia page title before the final Wayback pass.]

## Bridge

SVG is the medium. You now know what it is to three different readers and which decisions at generation time keep all three satisfied. But a medium is empty until you fill it with a vocabulary — specific colors, specific type, specific spacing, applied the same way every time so the output is auditable rather than improvised. Chapter 5 supplies that vocabulary: the complete Brutalist design system — seven color tokens, a three-font stack, an 8px spacing grid — as a production-ready specification you can paste straight into DESIGN.md.

## Sources

- W3C SVG Working Group. *Scalable Vector Graphics (SVG) 2 Specification.* W3C. — Authoritative reference for elements, grouping, text, paths, and presentation attributes. [accessed during drafting; verify version]
- Eisenberg, J. D., and Bellamy-Royds, A. *SVG Essentials*, 2nd ed. O'Reilly, 2014/2018. — Practical guide to reading and authoring SVG structure.
- Adobe. *Illustrator documentation: SVG import/export and object/layer behavior.* Adobe Help. — Production reference for the handoff; version-sensitive. [verify import behavior against current version]
- Anthropic. *Claude Code documentation.* Anthropic Docs. — Current workflows and constraints; high aging risk, verify before each offering.
- D3 Team. *D3 selections and `selection.join` documentation.* d3js.org. — Reference for the `.attr()` versus `.style()` distinction central to the editable-handoff rule.
