# AI for Graphs: A Practitioner's Guide — CLI Video Ideas ("X with Claude")

## Candidate 01 — "Build a D3 Bar Chart in 12 Seconds with the Four-Move Prompt"
- Source: ai-for-graphs-a-practitioners-guide/chapters/06-working-with-claude-code.md (Exercise 5.4 — LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: A 9-word prompt produces a bar chart with a non-zero baseline, unsorted categories, and rotated labels. A 200-word four-move prompt produces a publishable chart on the first attempt. The difference is discipline, not intelligence.
- The artifact: Two HTML files — vague-prompt output and four-move-prompt output — for the same humanitarian funding dataset. A Python comparison script counts: axis-start violations, sort-order failures, missing value labels, missing ARIA. Output: a D3-animated side-by-side comparison with the violation counts animating in.
- Prompt seed: First: `claude "Make a bar chart of humanitarian funding by sector." > vague.html` then: `claude "Show what I have: 5 rows, sector (string), funding_usd_millions (number). Sample: Food Security 380.2 / Shelter 142.7 / Water 98.4 / Health 87.3 / Protection 64.1. Say what I want: horizontal bar chart, single HTML, D3 v7 CDN. Constrain it: marks=rectangles, y=sector sorted descending, x from zero baseline (non-negotiable), luminance encoding funding, value labels at bar end, margins top60 right80 bottom40 left160, dark mode. Verify: restate channel decomposition, then code with per-line channel comments, list unspecified decisions." > four-move.html`
- Read / check: Verify vague.html has a non-zero x-axis; verify four-move.html has zero baseline and sort-by-value; verify value labels are present in the four-move output; verify both files open in a browser.
- Human supplies: The 5-row humanitarian funding dataset (fully synthetic — values provided in the prompt). Nothing requiring external data. Fully self-contained.
- Output medium: screen-recording mp4 — terminal running both prompts, browser side-by-side, violation counter animating.
- The change: Add a CLAUDE.md file with the zero-baseline and accessibility rules; shorten the "Constrain it" block for a sixth chart; verify the output quality holds without re-specifying the constants.
- Teardown angle: The four-move structure encodes the upstream analysis (channel decomposition, chart selection, data audit) into the prompt. Without the upstream work, the prompt is just longer — not better.
- Exclusions: D3 v7 API internals, full Evergreen/Emery 22-point checklist, scales and projections outside bar charts.
- Score: 10/10

## Candidate 02 — "Fix the Five Most Common Claude Code Chart Failures"
- Source: ai-for-graphs-a-practitioners-guide/chapters/06-working-with-claude-code.md (Common Failures table)
- Lane: BUILD (Claude Code)
- Hook: Five failures account for most first-output problems: auto-fit axis, wrong channel for data type, wrong sort order, unnecessary label rotation, no ARIA. Each has a one-sentence targeted follow-up that fixes it. The pattern is always the same: name the failure, name the rule it violates, tell Claude what to do differently.
- The artifact: A "failure demo" HTML gallery — five charts, each showing one of the five failures — plus a repair script that runs targeted follow-up prompts and produces five corrected charts. The gallery animates the before/after with a sweep transition.
- Prompt seed: Run each failure case with a vague prompt, then each repair: e.g., `claude "The y-axis starts at 40M instead of 0. Reset to a zero baseline. The proportional ink principle: bar length is the magnitude channel. A non-zero baseline makes a 90k month look 10x larger than an 85k month. Regenerate the scale and gridlines." < failure-01.html > fixed-01.html`
- Read / check: Verify failure-01.html has a non-zero baseline; verify fixed-01.html has baseline at 0; verify the hue-vs-luminance fix replaces the hue ramp with a sequential luminance scale; verify ARIA labels appear on the fixed accessibility chart.
- Human supplies: Five synthetic datasets (one per failure type) — fully fabricable from the book's examples. No external data required.
- Output medium: d3 (animated) — gallery with before/after sweep animation per failure, violation label animating out on repair.
- The change: Chain all five repairs into one CLAUDE.md rule set and run a sixth chart — show that the CLAUDE.md eliminates all five failures on first output.
- Teardown angle: Targeted follow-ups are surgical. Re-specifying the full prompt from scratch introduces new failures while fixing the original. One concern per iteration is the discipline.
- Exclusions: Full Evergreen/Emery checklist (22 points), D3 layout algorithms for advanced charts, performance optimization for large datasets.
- Score: 9/10

## Candidate 03 — "Plot Distribution Shape with Claude: Histogram Bin Width vs Violin"
- Source: ai-for-graphs-a-practitioners-guide/chapters/09-distribution-charts.md (Exercise 8.4-8.5)
- Lane: BUILD (Claude Code)
- Hook: Two distributions with identical five-number summaries look completely different as violin plots. The box plot cannot distinguish a normal distribution from a bimodal one. The bin-width problem hides both peaks at wide bins and drowns them in noise at narrow bins. Freedman-Diaconis is the rule, and you can watch it work.
- The artifact: Three panels for the same bimodal income dataset: (1) histogram at wide bins ($50K intervals) — peaks merged, (2) histogram at Freedman-Diaconis binning — bimodality visible, (3) violin plot — shape confirmed. All three rendered as a D3 animated reveal, one panel at a time.
- Prompt seed: `claude "I have a bimodal income dataset with peaks around 40k and 120k. Build three D3 v7 HTML panels: (1) histogram with 50k-wide bins (peaks should disappear), (2) histogram with Freedman-Diaconis binning (bin_width = 2*IQR/n^(1/3)), (3) violin plot using KDE with bandwidth chosen by Silverman's rule. Single HTML file with three labeled panels side by side. Zero baseline on histograms. Value labels on violin IQR. Dark mode."` then verify each panel tells a different story.
- Read / check: Verify panel 1 does not show bimodality (peaks merged); verify panel 2 shows two distinct peaks; verify panel 3 shows the two bulges; verify Freedman-Diaconis formula is implemented, not just labeled.
- Human supplies: A synthetic bimodal income dataset (generate with numpy: two Gaussian peaks at 40k and 120k). Fully synthetic — the lesson is the bin-width comparison, not real income data.
- Output medium: d3 (animated) — three-panel reveal, one panel animating in per beat, with annotation "what the mean hides" appearing on panel 1.
- The change: Replace the KDE bandwidth with a fixed wide bandwidth on the violin plot; show the bimodality disappearing from the violin; discuss the kernel-choice trade-off.
- Teardown angle: The distribution chart is not a decoration on top of the summary statistic. It is the correction to the summary statistic. Every bin-width choice is a claim about the data's structure.
- Exclusions: Statistical inference from distributions, formal KDE theory, box-plot whisker mathematics beyond the 1.5*IQR rule.
- Score: 9/10

## Candidate 04 — "Build a Time-Series Chart and Enforce the Zero-Baseline Rule"
- Source: ai-for-graphs-a-practitioners-guide/chapters/08-time-series-and-temporal-charts.md (Exercise 8.4)
- Lane: BUILD (Claude Code)
- Hook: A bar chart and a line chart can both start their y-axis at $80K. In the bar chart, this is a proportional ink violation — bar length is the magnitude channel and the truncated baseline lies. In the line chart, this is fine — the channel is point position, and a tight y-range is a design choice. Same visual trick. Different verdict.
- The artifact: Three panels for the same monthly revenue data: (1) area chart with y starting at $80K — a proportional ink lie, (2) area chart with zero baseline — corrected, (3) line chart with tight y-range — legitimate. D3 animated, with the "what this visual area actually encodes" annotation appearing on panel 1.
- Prompt seed: `claude "I have 12 months of revenue data, values ranging 85k-95k. Build three D3 v7 HTML panels: (1) area chart, y-axis from 80k (proportional ink violation — the fill encodes revenue-minus-80k, not revenue), (2) area chart, y-axis from 0 (correct — area encodes actual revenue), (3) line chart, y-axis from 80k (legitimate — channel is point position). Add annotation on panel 1: 'Visual area encodes (value - 80k), not value. The ratio is distorted.' Single HTML file, dark mode, direct value labels."` then verify all three panels match their descriptions.
- Read / check: Verify panel 1 y-axis starts at 80k; verify panel 2 y-axis starts at 0; verify panel 3 y-axis starts at 80k; verify the annotation appears on panel 1; verify all three use the same data.
- Human supplies: Synthetic 12-month revenue dataset (generate inline: `[85, 88, 87, 91, 93, 90, 89, 92, 95, 91, 88, 87]`). Fully synthetic.
- Output medium: d3 (animated) — three panels revealing sequentially, with the annotation flying in on panel 1 as a highlighted callout.
- The change: Ask Claude to build a panel 4: a stacked area chart with the same data — show that the zero-baseline rule applies absolutely to area encoding regardless of chart subtype.
- Teardown angle: The channel determines the verdict. Area-as-channel requires zero baseline; position-as-channel does not. This one distinction separates honest from misleading across the entire temporal chart family.
- Exclusions: Gestalt continuity theory lecture, spiral plot construction, stream graph aesthetics, full temporal family taxonomy.
- Score: 9/10

## Candidate 05 — "Build a Scatterplot with the Causation Caveat and Annotate the Cloud"
- Source: ai-for-graphs-a-practitioners-guide/chapters/10-relationship-and-correlation-charts.md (Exercise 10.1)
- Lane: BUILD (Claude Code)
- Hook: A scatterplot of education index vs. life expectancy across 170 countries, r = 0.79, OLS trend line — the reader forms the causal inference before the chart title finishes. Alberto Cairo calls this a moral failure. The fix is 12 words. Building it takes 30.
- The artifact: Two D3 scatterplots of the same 170-country dataset: (1) without causation caveat — the reader is invited to infer causation, (2) with causation caveat block: "Correlation does not imply causation. These variables are associated; the causal mechanism is not established by this chart." Both panels side by side, with a third panel showing a heteroscedastic cloud (same r = 0.7) to demonstrate that the number does not capture cloud shape.
- Prompt seed: `claude "I have 170-country education-vs-life-expectancy data. Build three D3 v7 panels: (1) scatterplot, OLS line, r annotated, no caveat, (2) same but with text block: 'Correlation ≠ causation. These variables are associated; causal mechanism not established.' positioned near the trend line, (3) scatterplot of a heteroscedastic cloud (same r≈0.7 but fan-shaped) with annotation 'Same r = 0.7, different cloud shape.' Single HTML, zero baseline on axes, dark mode, ARIA."` then verify the caveat appears in panel 2 only.
- Read / check: Verify panel 1 has no caveat text; verify panel 2 caveat is visible and correctly worded; verify panel 3 cloud is visually fan-shaped (heteroscedastic); verify all three annotate r value.
- Human supplies: A synthetic 170-row education-life-expectancy dataset (generate with numpy: two correlated Gaussian series, r ≈ 0.79). Fully synthetic.
- Output medium: d3 (animated) — three panels revealing sequentially, caveat text in panel 2 animated in with a highlight flash.
- The change: Add a fourth panel where the causal direction is reversed (life expectancy on x, education on y) — show how the axis convention changes the reader's causal inference even with identical data.
- Teardown angle: The visual authority of a chart exceeds its empirical claim. The designer's professional responsibility includes preventing the over-reading that the chart's visual authority would otherwise produce. The caveat does not weaken the chart. It completes it.
- Exclusions: Regression diagnostics, instrumental variable methods, Anscombe's quartet full derivation, Pearson vs. Spearman comparison.
- Score: 9/10

## Candidate 06 — "Build a Complete Visualization Project: Five Phases, Three Charts"
- Source: ai-for-graphs-a-practitioners-guide/chapters/17-building-a-complete-project.md (LLM Exercise — full pipeline)
- Lane: BUILD (Claude Code)
- Hook: A project is not three independent charts. It is three questions, a shared visual language, a paper trail of decisions. The MBTA lesson still applies: nothing beats iterating on working code — and when it takes 12 seconds to produce a chart, the right move is to get the artifact in front of you as fast as possible.
- The artifact: A complete three-chart visualization package for UNHCR forced displacement data: CLAUDE.md (coding constitution), DESIGN.md (visual constitution), PROJECT.md (decision log), three publishable D3 HTML charts answering the three reader questions. The package is structured as a directory with all six files.
- Prompt seed: Phase A: `claude "Three reader questions for UNHCR forced displacement 2020-2024 data: (1) which countries produce the most refugees and how has this changed? (2) which countries receive the most? (3) what proportion is internal vs international? Data audit: ~5000 rows, categorical country + temporal year + quantitative count. What relationship type does each question require and what chart family?"` then Phase B: `claude "Build CLAUDE.md for a D3 project: zero baseline for bars, d3.scaleSqrt for bubbles, equal-area projection for choropleths, accessibility on every chart, naming convention, no .style() for visual properties."` then Phase C: generate each chart.
- Read / check: Verify CLAUDE.md contains at least the zero-baseline rule, the scale-type rules, and the accessibility requirement; verify each chart answers one of the three questions; verify all three charts use the same color tokens from DESIGN.md.
- Human supplies: The UNHCR displaced-persons dataset (publicly available) or a synthetic approximation (~50 rows covering 10 countries × 5 years). Real data preferred; synthetic acceptable if labeled as illustrative.
- Output medium: screen-recording mp4 — terminal walking through the five phases, three charts opening in browser, directory structure visible.
- The change: Load both CLAUDE.md and DESIGN.md at the start of a fourth chart session; verify the "Constrain it" block shrinks compared to the first three charts.
- Teardown angle: The project infrastructure is not bureaucracy — it is the elimination of repeated decisions. CLAUDE.md is every constraint you would otherwise re-specify in every prompt.
- Exclusions: D3 geographic projections deep dive, Sankey layout internals, multi-chart responsive frameworks.
- Score: 8/10

## Candidate 07 — "Chart Selection as Design Decision: Cairo's Four Steps with Claude"
- Source: ai-for-graphs-a-practitioners-guide/chapters/04-chart-selection-as-design-decision.md (Exercise 4.x)
- Lane: BUILD (Claude Code)
- Hook: "The wrong chart feels familiar; the right one takes work." A pie chart for five categories with one dominant category feels natural. A bar chart sorted by value answers the reader's question. Cairo's four steps take the same 30 seconds either way.
- The artifact: A D3 decision-tree animation of Cairo's four-step chart selection framework: (1) one-sentence key message, (2) functional category (comparison/distribution/relationship/part-to-whole/etc.), (3) specific chart form, (4) channel decomposition. The tree animates with a real dataset as input, showing which branch each decision takes.
- Prompt seed: `claude "I want to build a D3 chart-selection decision tree using Cairo's four-step framework. Data: the 8 chart categories (comparison, distribution, relationship, part-to-whole, flow, spatial, temporal, specialized) as branches. Animate: a user inputs a dataset description and one-sentence key message; the tree highlights the path to the recommended chart form. D3 v7, single HTML, dark mode, tree layout with animated path highlighting."` then test with the humanitarian funding example: key message = "Food security received 56% of total funding, more than the next four combined."
- Read / check: Verify the tree renders 8 functional categories as branches; verify the animation highlights the path from message → category → form; verify the humanitarian example navigates to "horizontal bar chart sorted descending."
- Human supplies: The chart-category taxonomy from the book (FT Visual Vocabulary / Cairo framework — publishable reference). Synthetic dataset for the demo (5-sector funding data from chapter 6). Fully synthetic.
- Output medium: d3 (animated) — tree with path highlighting animation, input prompt animating at top, branch labels growing.
- The change: Input a temporal dataset (monthly series, single variable) — show the tree navigating to line chart, and a temporal+cyclic dataset navigating to spiral plot as a contrast.
- Teardown angle: Chart selection is a channel choice, and the channel choice has perceptual consequences. The familiar chart is often wrong not because it is ugly but because it encodes the wrong channel for the reader's question.
- Exclusions: Full FT Visual Vocabulary taxonomy, Gestalt theory lecture, perceptual ranking tables beyond what the decision drives.
- Score: 8/10

## Candidate 08 — "Build a Stacked Area Chart with Correct Layer Ordering"
- Source: ai-for-graphs-a-practitioners-guide/chapters/08-time-series-and-temporal-charts.md (Exercise 8.5)
- Lane: BUILD (Claude Code)
- Hook: In a stacked area chart, the bottom layer has a fixed zero baseline and the reader can compare it accurately. The top layer has a highly variable baseline and the reader is working hardest. The design rule is simple: put the most stable series at the bottom. Claude defaults to alphabetical. The fix is one sentence.
- The artifact: A five-layer stacked area chart of humanitarian funding over 12 months, with two versions: (1) alphabetical ordering (Claude's default) — the most volatile series at the bottom, (2) stability-ordered — most stable series (Food Security) at the bottom. An accuracy-gradient annotation shows the decreasing accuracy as layers move up.
- Prompt seed: `claude "I have 5-sector humanitarian funding data over 12 months. Build a D3 v7 stacked area chart with: zero baseline, alphabetical layer ordering for version 1. Then build version 2 with layer ordering by stability (lowest variance across months first). Add annotations on the right edge showing: bottom layer = fixed baseline (high accuracy), middle layers = variable baseline (lower accuracy), top layer = noisiest baseline (lowest accuracy). Single HTML, both versions side by side, dark mode."` then verify layer ordering.
- Read / check: Verify version 1 ordering is alphabetical; verify version 2 ordering is by variance (lowest variance at bottom); verify accuracy-gradient annotations appear on both versions; verify both have zero baseline.
- Human supplies: Synthetic 5-sector, 12-month funding dataset (generate with numpy: Food Security high/stable, Protection low/volatile). Fully synthetic.
- Output medium: d3 (animated) — two stacked area charts revealing sequentially, accuracy-gradient annotations growing in on the right edge.
- The change: Ask Claude to add a "small multiples" version — one panel per sector, shared y-axis — and show when this serves the reader better than the stacked form.
- Teardown angle: Layer ordering is not aesthetic. It is an accuracy decision. The bottom layer is the most accurate comparison surface; every designer has a responsibility to put the most important series there.
- Exclusions: Stream graph aesthetics, spiral plot construction, D3 Sankey layout.
- Score: 8/10

## Candidate 09 — "Build the D3 MBTA Marey Diagram: Two Position Channels"
- Source: ai-for-graphs-a-practitioners-guide/chapters/08-time-series-and-temporal-charts.md (Exercise 8.9)
- Lane: BUILD (Claude Code)
- Hook: Barry and Card's 2014 MBTA Marey diagram uses two position channels — time on x, station distance on y — and both are the highest-accuracy channel in the Cleveland-McGill ranking. The result shows train-delay cascades that are invisible in a bar chart of average delays. Nothing beat iterating on working code. That was 2014. Now the first working chart takes 12 seconds.
- The artifact: A D3 Marey diagram (space-time chart) for a transit dataset: time on x, station sequence on y, each train as a line. The chart reveals delay cascades, train bunching, and service gaps — patterns invisible in the aggregated bar chart that the same data would normally produce. Both versions shown side by side.
- Prompt seed: `claude "Build a D3 v7 Marey diagram (space-time chart) for a transit system. Data: 20 trains, each with arrival times at 10 stations over a 4-hour window. X-axis: time (minutes). Y-axis: station sequence (0 to 9). Each train is a line. Color-encode on-time vs. delayed trains. Add a bar chart of average delay per train as a second panel. Show what the Marey diagram reveals that the bar chart hides: delay cascades where a slow train causes the next train to bunch behind it. Single HTML, dark mode, zero baseline on bar chart."` then verify the cascade is visible.
- Read / check: Verify the Marey diagram shows train lines converging (bunching) in at least one section; verify the bar chart shows the same delay data but the cascade pattern is not visible; verify both x and y axes are quantitative position channels.
- Human supplies: Synthetic transit dataset (generate with Python: simulate a delay cascade where one train at minute 30 slows, and subsequent trains bunch behind it). Fully synthetic.
- Output medium: d3 (animated) — Marey diagram drawing train lines one by one, then the bar chart rendering for comparison, annotation "cascade visible here" pointing to the bunching region.
- The change: Collapse the space-time diagram to a single aggregated bar per train; show that the cascade completely disappears in the aggregated view.
- Teardown angle: Two quantitative position channels is the highest-accuracy combination in the Cleveland-McGill ranking. The Marey diagram earns its complexity because both channels matter — and the interaction between them is the data.
- Exclusions: Graph theory for transit networks, GTFS data format, full Cleveland-McGill ranking lecture.
- Score: 8/10
