# AI for Infographics: A Practitioner's Guide — CLI Video Ideas ("X with Claude")

## Candidate 01 — "Run a Specification-Driven SVG Infographic: Zero Corrections vs. Eleven Violations"
- Source: ai-for-infographics-a-practitioners-guide/chapters/13-generate-claude-code-as-a-structured-executor.md (Opening experiment)
- Lane: BUILD (Claude Code)
- Hook: A specification-less prompt produces a polished SVG in 90 seconds. The checklist finds eleven violations: hardcoded hex colors, a gradient that encodes nothing, a y-axis starting at 50%, anonymous group names. The specification-driven prompt produces zero corrections. Same model, same 90 seconds, same data. The governing context is the only variable.
- The artifact: Two SVG files — specification-less and specification-driven — for the same vaccine efficacy data. A Python checklist script runs the eleven-item CLAUDE.md audit on both: hardcoded hex, .style() calls, anonymous groups, non-zero axis, gradient fills, missing CAJAL metadata, etc. Output: a side-by-side comparison table of violation counts (11 vs 0), rendered as an animated D3 bar chart.
- Prompt seed: Run 1 (spec-less): `claude "Make me an SVG infographic showing vaccine efficacy stabilizing as the trial gets bigger. Use D3. Make it look clean and professional." > spec-less.svg` then Run 2 (spec-driven, with CLAUDE.md + DESIGN.md in context): `claude "Execute the SCOPE specification for the vaccine efficacy figure. Governing context: CLAUDE.md + DESIGN.md are loaded. SCOPE: S=800x500 SVG, C=efficacy point estimate and 95% CI at enrollment sizes 1k-30k, O=x=enrollment (log scale), y=efficacy (0-100% — zero baseline non-negotiable), CI band behind estimate line, E=no gradient fills, no axis truncation, no hardcoded hex, anonymous groups forbidden. Generate scaffold first, then marks, then annotation layer. Output SVG with CAJAL metadata block." > spec-driven.svg` then `python3 cajal_audit.py spec-less.svg spec-driven.svg`
- Read / check: Verify the audit script fires on hardcoded #4a90d2 in spec-less.svg; verify the y-axis truncation at 50% is flagged; verify spec-driven.svg has zero flags; verify the animated bar chart renders violation counts correctly.
- Human supplies: A synthetic vaccine efficacy dataset (point estimate ~71%, CI narrowing from ±20 at 1k to ±4 at 30k enrollees). The CLAUDE.md + DESIGN.md governing files (writable within the video as minimal versions). Fully synthetic.
- Output medium: d3 (animated) — side-by-side violation-count bars growing, then a sweep revealing the two SVGs in the browser.
- The change: Take one violation from spec-less.svg (the hardcoded gradient) and add a rule to CLAUDE.md; re-run; show the violation disappears from the re-generated spec-less output.
- Teardown angle: Capability raises the stakes of specification — a more capable agent propagates an unbounded inference further and faster. The eleven violations are not a bug. They are what happens when design decisions are left to the executor.
- Exclusions: D3 API internals, Illustrator handoff workflow, WCAG accessibility standards beyond the SVG metadata.
- Score: 10/10

## Candidate 02 — "Write a CAJAL SCOPE Specification and Pass the Exclusion Gate"
- Source: ai-for-infographics-a-practitioners-guide/chapters/11-the-brutalist-system-claude-design-project.md + chapters/10-layout-composition-and-the-cajal-specification-system.md
- Lane: BUILD (Claude Code)
- Hook: Anyone can say what a figure is about. The figures that fail are the ones where no one ever wrote down what the figure is NOT about. The exclusion list is more important than the inclusion list — and a SCOPE prompt without an E block is not finished.
- The artifact: A complete CAJAL SCOPE specification for one infographic brief, plus a Python gate that validates: (a) component count ≤ 8, (b) E block is present with at least 2 specific exclusions, (c) no "and" conjunctions in C block (which signal two figures in disguise), (d) O block names a spatial layout logic (left-to-right process, side-by-side comparison, etc.). Gate output: PASS/FAIL with per-criterion callouts.
- Prompt seed: `claude "Build a CAJAL SCOPE specification for this infographic brief: [3-sentence brief]. Five sections: S=canvas specs and target medium, C=exactly which concepts, entities, relationships are included (no inferring, no 'while we're at it'), O=spatial layout logic (process=left-to-right; comparison=shared axis), P=presentation constraints (flat vector, colorblind-safe palette with hex, uniform strokes, no gradients — do not specify aesthetic), E=exclusion list: at least 2 specific things this figure will NOT show even though they are adjacent to the concept. Apply the 6-to-8 component ceiling." > scope.md` then `python3 cajal_scope_gate.py scope.md`
- Read / check: Verify the gate fires on a C block with 10+ components; verify the "and" conjunction detection catches "A and B are shown"; verify the E block presence check fails on an empty exclusion section; verify the spatial logic detection flags an unspecified O block.
- Human supplies: A real 3-sentence infographic brief from the viewer's domain. Synthetic is acceptable if the concept is specified. The Python gate is writable within the video (~30 lines).
- Output medium: screen-recording mp4 — terminal running the SCOPE prompt, gate script, PASS/FAIL output, then deliberate overcount failure and gate FAIL.
- The change: Remove the E block entirely; re-run the gate (FAIL); run the specification-less prompt and show what the infographic generator adds without it; add the E block back and compare.
- Teardown angle: The exclusion list is not defensive — it is the design judgment. Left without it, every image model defaults to comprehensive. The E block is the difference between a figure that clarifies and a figure you spend an afternoon editing clutter out of.
- Exclusions: Full CAJAL command set, SVG viewBox DPI mismatch details, Illustrator mask-release workflow.
- Score: 9/10

## Candidate 03 — "Build an SVG with Semantic Layer Names That Survive Illustrator"
- Source: ai-for-infographics-a-practitioners-guide/chapters/04-svg-as-a-design-medium.md (Exercises)
- Lane: BUILD (Claude Code)
- Hook: A group named "median-series" in the SVG source becomes a layer named "median-series" in Illustrator. A group named "g" becomes "<Group>". One semantic id is free. The choice between them is the difference between a file you can edit in 2 minutes and one you spend 90 minutes rebuilding.
- The artifact: Two SVG bar charts for the same income-divergence data: (1) generator-default output — anonymous groups, .style() for colors, inline clipping paths, (2) Brutalist-compliant output — semantic ids (median-series, axis-x, callout-2008), presentation attributes via .attr(), no clip paths. A Python audit script checks both: semantic id coverage, .style() call count, clip-path count. Output: a terminal table comparing the two files.
- Prompt seed: Run 1 (default): `claude "Build a D3 v7 bar chart of median vs mean household income divergence over 4 decades. Single HTML, inline SVG." > default.html` then Run 2 (Brutalist): `claude "Build the same chart with Brutalist SVG conventions: (1) every structural group gets a semantic id (e.g., median-series, axis-x, annotation-layer), (2) all visual properties via .attr() not .style() — no .style() calls for fill/stroke, (3) no clipPath elements, (4) add data-name attribute parallel to every id for Illustrator human-readability. Single HTML, dark mode."` then `python3 svg_audit.py default.html brutalist.html`
- Read / check: Verify default.html has at least 3 anonymous <g> elements; verify brutalist.html has 0 anonymous groups; verify .style() call count in default > 0 and brutalist = 0; verify data-name attributes present in brutalist output.
- Human supplies: Synthetic 4-decade income divergence dataset (generate inline: median stagnant, mean rising from 1980 to 2020). Fully synthetic.
- Output medium: screen-recording mp4 — terminal running the audit, comparison table, then opening both files in a browser and simulating the Illustrator inspection (tree view comparison).
- The change: Open the default SVG in a text editor and show what the group tree looks like (<g><g><g>); open the Brutalist SVG and show the named tree. Discuss the one-way ticket principle: once you edit in Illustrator, you don't regenerate over it.
- Teardown angle: "Renders correctly" and "can be edited" are answers to two different questions, asked by two different machines. The reconciliation is irreducibly human — and the cost of getting it wrong is 90 minutes of rebuilding, not 30 seconds of naming groups.
- Exclusions: Full DOM traversal theory, DPI mismatch resolution, Inkscape alternative workflow.
- Score: 9/10

## Candidate 04 — "Run the Blur Test, WCAG Contrast Check, and Grayscale Test on an Infographic"
- Source: ai-for-infographics-a-practitioners-guide/chapters/14-verify-and-handoff-from-svg-to-production-asset.md + chapters/15-the-complete-pipeline-one-brief-every-decision.md
- Lane: BUILD (Claude Code)
- Hook: The blur test is one question: if you blur the infographic to illegibility, can you still see where the reader's eye should go first? A figure that only works at full resolution is relying on detail to carry structure. Structure should be visible without reading.
- The artifact: An infographic through three automated checks: (1) a Python script that applies a PIL Gaussian blur (sigma=5) and checks that the primary visual element is still the darkest/most prominent region, (2) a WCAG AA contrast check (contrast ratio ≥ 4.5:1 for text on background), (3) a grayscale conversion check that the color encoding still conveys information without hue. Output: a PASS/FAIL report per check, with the blurred/grayscale images as visual evidence.
- Prompt seed: `python3 infographic_verify.py infographic.svg` where the script: (a) converts SVG to PNG with cairosvg, (b) applies PIL Gaussian blur sigma=5, (c) checks that the highest-contrast region matches the intended primary element, (d) runs wcag_contrast_checker on all text/background pairs, (e) converts to grayscale and checks that the accent color's grayscale value is distinguishable from body color. Output: JSON report with per-check PASS/FAIL and the processed images saved to verify/.
- Read / check: Verify the blur test fires when the primary element is low-contrast; verify the WCAG check flags text below 4.5:1; verify the grayscale check fails when two encoding colors have identical grayscale values; verify the script accepts SVG input and outputs PNG results.
- Human supplies: An infographic SVG with one planted WCAG failure (text below contrast threshold) and one planted grayscale failure (two encoding colors that converge in grayscale). Synthetic SVG acceptable.
- Output medium: screen-recording mp4 — terminal running the verification script, PASS/FAIL report, the blurred and grayscale images opening in a viewer.
- The change: Fix the WCAG failure (darken the text color), re-run the check, show it passes; then fix the grayscale failure (shift one encoding color to a distinguishably lighter grayscale value).
- Teardown angle: The verification checklist is not optional cleanup. It is the admission price to claiming the figure is publishable. A figure that passes the blur test is structurally sound. One that fails is relying on proximity to be understood.
- Exclusions: Print production color management (CMYK conversion), full SVG accessibility ARIA specification, professional Illustrator export workflow.
- Score: 9/10

## Candidate 05 — "Generate the Complete Infographic Production Package"
- Source: ai-for-infographics-a-practitioners-guide/chapters/15-the-complete-pipeline-one-brief-every-decision.md (Final Project)
- Lane: BUILD (Claude Code)
- Hook: "Done" is not a pretty PNG. It is a package where every artifact traces back to a decision, and every decision traces back to the brief. The DISCLOSURE.md names three things the human decided that no AI tool could decide. That is the proof of ownership.
- The artifact: A complete infographic production package for a real brief: BRIEF.md, PROJECT.md, DESIGN.md, CLAUDE.md, scope.md, generated SVG, DISCLOSURE.md (three human-judgment decisions), DEFENSE.md (one-sentence defense of every encoding decision). The package is built end-to-end in one terminal session.
- Prompt seed: Phase 1 — `claude "Brief: [3-sentence brief]. Build PROJECT.md with two layers: Intent Layer (what does this figure claim, what does it exclude, what is the one thing the reader must understand?) and Schema Layer (data types, attribute names, relationship type, encoding options)."` Phase 2 — `claude "Build DESIGN.md with 7 color tokens, 3-font stack (display/body/data), layout type from {process|comparison|hierarchy|flow}."` Phase 3 — `claude "Build CLAUDE.md coding constitution: D3 v7, semantic groups, .attr() not .style(), zero-baseline rule, CAJAL metadata block required."` Phase 4 — SCOPE + generate SVG. Phase 5 — `claude "Write DISCLOSURE.md: three decisions in this infographic that required human judgment no AI tool could supply — not aesthetic preference, but decisions about what the figure claims and what it excludes."`
- Read / check: Verify the directory has all 9 expected files; verify DISCLOSURE.md names three genuinely human-judgment decisions (not just "I chose the color"); verify DEFENSE.md has at least one sentence per visual choice; verify the SVG passes the CAJAL audit gate.
- Human supplies: A real 3-sentence brief from the viewer's domain (public-health, science communication, journalism). Real brief required — the human-judgment decisions in DISCLOSURE.md only emerge from a real domain problem.
- Output medium: screen-recording mp4 — terminal walking through the five phases, directory tree appearing, DISCLOSURE.md content readable.
- The change: Add DEFENSE.md after generating the SVG by asking Claude to audit every encoding decision and require a one-sentence defense for each; show that two decisions need revision when the defense exposes them as defaults, not choices.
- Teardown angle: The DISCLOSURE.md is not a compliance document. It is the proof that a human owned the judgment. "The y-axis starts at zero because the brief said 'do not be alarmist beyond the data'" is a human decision. "The y-axis starts at zero because that's the default" is not.
- Exclusions: Illustrator-to-PNG export workflow, print production pipeline, full WCAG audit beyond the basic checks.
- Score: 9/10

## Candidate 06 — "Audit an Infographic for Proportional Ink Violations with Claude"
- Source: ai-for-infographics-a-practitioners-guide/chapters/01-the-infographic-that-lied-while-telling-the-truth.md + chapters/06-marks-channels-and-the-grammar-of-infographics.md
- Lane: BUILD (Claude Code)
- Hook: A public-health infographic shows two circles: UNVACCINATED (large, ominous) and VACCINATED (small). The visual reads instantly. It is also wrong — area perception has an exponent of 0.7, so a circle that looks 10x larger represents only 4.7x more in actual area. The circles are lying while telling the truth.
- The artifact: A Python SVG auditor that reads an infographic SVG and flags: (a) area-encoded elements where the radius encodes the value (violates sqrt-scaling), (b) bar charts with non-zero baselines, (c) gradient fills (area-encoding violation), (d) size differences that exceed the Stevens' power law threshold (perceived ratio vs. actual ratio > 1.5). Output: a terminal report with violation type, element id, and the corrected encoding.
- Prompt seed: `python3 proportional_ink_audit.py infographic.svg` then for any flagged area elements: `claude "This SVG has two circles where radius is proportional to the value (not the square root). Fix the encoding: if the values are A and B, the radius should be proportional to sqrt(A) and sqrt(B). Maintain the same center positions. Update the SVG." < infographic.svg > fixed.svg`
- Read / check: Verify the audit fires on a circle where radius=value rather than radius=sqrt(value); verify the gradient fill flag triggers on any linearGradient or radialGradient element; verify the non-zero baseline check fires on rect elements whose y attribute > 0 when the x-scale minimum should be 0.
- Human supplies: A synthetic SVG infographic with at least one planted proportional ink violation (circle with radius=value encoding). Fully synthetic.
- Output medium: screen-recording mp4 — terminal running the audit, violation report, then the Claude fix applied and the corrected SVG opening in the browser.
- The change: Run the correction on the bubble chart radius violation (switch from radius=value to radius=sqrt(value)); show visually how the circles shrink relative to each other; discuss what the before/after comparison means for the public-health story.
- Teardown angle: The infographic can be data-accurate and perceptually misleading. The proportional ink principle is not aesthetic preference — it is the mechanism by which a correct number produces a wrong impression.
- Exclusions: Color perception theory (preattentive attributes lecture), Gestalt principles taxonomy, full SVG DOM tree traversal.
- Score: 8/10

## Candidate 07 — "Build the Color System Audit: Token Coverage and WCAG Check"
- Source: ai-for-infographics-a-practitioners-guide/chapters/08-color-systems-and-typography-for-infographics.md
- Lane: BUILD (Claude Code)
- Hook: A choropleth of county-level vaccination coverage uses a soft gradient from pale yellow to deep green. The WCAG contrast ratio for the lightest county label text is 2.1:1. The data is real. The figure is inaccessible to the 8% of men with red-green color blindness. The fix is specifying the palette once, in DESIGN.md, before any generation happens.
- The artifact: A Python color audit script that reads a DESIGN.md token file and checks: (a) every named token has a WCAG AA contrast ratio ≥ 4.5:1 against its expected background, (b) the palette is color-blind safe (simulates Deuteranopia and Protanopia using daltonize), (c) no hardcoded hex appears in any SVG file that should be using tokens. Output: a per-token PASS/FAIL table plus a grayscale simulation of the palette.
- Prompt seed: `claude "Write a DESIGN.md with 7 color tokens for a public-health infographic series: 1 primary accent, 1 secondary accent, 2 data-encoding colors (must be distinguishable in grayscale and color-blind safe), 1 background, 1 body text, 1 data text. For each token: name, hex, intended use, WCAG ratio against its typical background. The two encoding colors must not be red-green variants (deuteranopia failure)." > DESIGN.md` then `python3 color_audit.py DESIGN.md any_infographic.svg`
- Read / check: Verify the audit fires on a red-green encoding pair when simulated for Deuteranopia; verify WCAG contrast ratio is computed correctly (≥ 4.5:1 = pass, < 4.5:1 = fail); verify the hardcoded-hex scanner fires on any #XXXXXX in the SVG that does not appear in DESIGN.md.
- Human supplies: A DESIGN.md with one planted WCAG failure and one planted red-green color pair. The daltonize library for color-blindness simulation. Synthetic design tokens are fully acceptable.
- Output medium: screen-recording mp4 — terminal running the audit, per-token table, color-blind simulation images opening, then the correction pass.
- The change: Replace the failing red-green pair with an orange-blue pair; re-run the audit; show all tokens passing Deuteranopia simulation.
- Teardown angle: Color that looks fine in the designer's browser is invisible to 8% of the male population. The audit is not a compliance exercise. It is the difference between a figure that communicates to everyone and one that was only ever tested on the designer.
- Exclusions: Print CMYK color management, full CSS custom properties specification, dark-mode implementation details.
- Score: 8/10

## Candidate 08 — "Generate and Verify the Painter's Algorithm Layer Order"
- Source: ai-for-infographics-a-practitioners-guide/chapters/07-visual-hierarchy-and-the-painters-algorithm.md
- Lane: BUILD (Claude Code)
- Hook: A figure opened in Illustrator shows the annotation pointing at "memory B-cell" in the wrong color. The annotation layer is rendering behind the background. The painter's algorithm determines what paints over what — SVG elements later in the document order paint over earlier ones. If the background is last, it covers everything.
- The artifact: A Python SVG layer-order auditor that reads an SVG and checks: (a) background elements (<rect fill=background-color>) are first in document order, (b) data marks are after background, (c) annotation/callout elements are last, (d) no data mark is occluded by a later-painted element. Output: a layer-order diagram as an animated Manim scene showing document order vs. render order.
- Prompt seed: `claude "Build an SVG infographic showing three-layer visual hierarchy: background layer (white rect), data marks (colored bars or circles), annotation layer (callout arrows and labels). Apply the painter's algorithm explicitly: background first in document order, marks second, annotations last. Name every group with a semantic id: background-layer, data-layer, annotation-layer. Include a deliberate violation: one annotation group placed before the data marks — so I can show the occlusion failure." > hierarchy-demo.svg` then `python3 layer_order_audit.py hierarchy-demo.svg`
- Read / check: Verify the planted violation (annotation before data marks) is flagged; verify the audit orders elements correctly against the expected Brutalist layer schema; verify the Manim layer-order animation renders document order as a vertical stack.
- Human supplies: Synthetic SVG with planted painter's-algorithm violation. Manim installed. Fully synthetic.
- Output medium: Manim (animated) — vertical stack showing document order, paint-order arrow sweeping bottom-to-top, occlusion visible as one element covers another.
- The change: Fix the layer order (move the annotation group to last position); re-run the audit; show the occlusion disappear in the corrected render.
- Teardown angle: The painter's algorithm is not a rendering detail — it is the visual hierarchy specification. A designer who does not control document order does not control what the reader sees first.
- Exclusions: Z-index CSS specification, 3D rendering pipelines, full Illustrator layers panel workflow.
- Score: 8/10
