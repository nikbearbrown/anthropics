# Chapter 5 — Color Is Doing Nothing (or Harm)


## TL;DR

- Every color on the slide is either encoding something or competing with what is.
- The chapter moves through What color can and cannot do, The contrast problem, What the failure looks like, What the repair looks like, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Every color on the slide is either encoding something or competing with what is. Find out which. Cut the rest.*

---

Let me tell you about a puzzle I find genuinely interesting.

Take a slide with six colors on it. A gradient background, a navy headline, four bullets in red, green, orange, and blue, a colored chart, a yellow badge in the corner. The slide looks polished — it came out of some AI tool's "professional" preset. It looks, in the ordinary sense of the word, designed.

Now ask: what does red mean? What does green mean? Are they paired? Is the red bullet the one that is bad news and the green the one that is good news, or are they just different colors for different bullets? Sit with the question. If you were a student in the third row, which element is calling for your attention?

The slide does not have an answer. There is no code. The colors were chosen to look interesting, not to mean anything. And "looking interesting" while meaning nothing is not a neutral outcome. It is a specific kind of damage.

Here is why. The moment a color appears on a visual display, your brain's pattern-recognition system begins searching for the rule. Red appears on bullet A. Green on bullet B. A rule must exist. The brain is looking for it — *is red the warning? is green the progress? are they paired by category?* — and the search fails, and the brain has spent cognitive resources on a failure. Resources that were supposed to go to the content. This is friction without yield: the cognitive struggle that produces learning is struggle over the content, not struggle over a chart that promised a code and never delivered one.

The colors that are doing real work — if any are — are now drowned out by the colors that are not. The signal is lost in noise. This chapter is about the rules that determine which colors are signal and which are noise.

---

## What color can and cannot do

Start with what the research says about color as an information channel.

William Cleveland and Robert McGill published a paper in 1984 that ranked visual encoding channels by how accurately people could read quantitative information from them. Position along a common scale came first — you can read a bar chart accurately because you are judging where the bar's end lands on a shared axis. Then length, then angle, then area. Near the bottom: color saturation.

![Color saturation ranks near the bottom. Most slide designers use it as their primary encoding channel.](images/05-color-is-doing-nothing-or-harm-fig-01.png)
*Figure 5.1 — Horizontal ranked bar chart of Cleveland-McGill perceptual accuracy*

Sit with that. Color is one of the *weakest* channels for conveying quantitative information accurately. When a chart uses color as its primary encoding — four bars, four different saturated colors, no other distinguishing feature — it is asking the weakest available channel to do the heaviest work. The same information encoded in position (bars sorted by value on a labeled axis) would be read more accurately by more readers with less effort.

This does not mean color is useless. It means color has a specific job it is good at and a specific job it is bad at. Color is excellent for categorical distinction when the categories are few — two or three — when the color is paired with a second encoding such as a label, a shape, or a position in a sort, and when the color choice is consistent across the deck. Color is bad at encoding quantity, bad at working alone without a backup, and catastrophically bad when used inconsistently.

| Color works when |
| --- |
| 1) categories are 2–3 |
| 2) paired with label, shape, or position |
| 3) same color means same thing throughout |
| 4) encoding is categorical |

Richard Mayer's Signaling Principle makes the consistency requirement precise. The principle's force is not "use color cues." It is "the cue must mean the same thing every time it appears." A color that means one thing on slide three and something else on slide seven — or means nothing — is not a weak signal. It is anti-signal. The reader's brain searches for the rule, finds no rule, and has paid a cost for nothing.

There is also a fact about human vision that is non-negotiable and widely ignored. Approximately eight percent of men of Northern European ancestry have some form of red-green color vision deficiency. In a lecture hall of one hundred men from that population, about eight of them cannot reliably distinguish red from green. A chart encoded in red and green alone is, for those eight students, an unencoded chart. They are not paying less attention. The information is simply invisible to them. This is not a rare edge case. It is a routine fact about a significant fraction of every audience, and most slide authors ignore it every time they make a chart.

---

## The contrast problem

Separate from encoding is legibility — whether the text on the slide can be read at all.

The W3C Web Content Accessibility Guidelines specify a contrast ratio of at least 4.5:1 for normal text against its background, and 3:1 for large text, at Level AA. The ratio measures relative luminance: 1:1 is the same color on the same color; 21:1 is black on white. AA represents approximately the minimum readable contrast for someone with moderately reduced vision.

But a classroom is harder than a laptop screen. Ambient light from windows and overhead fluorescents washes out perceived contrast. Projector bulbs vary in quality and age. The student in the back row is farther away, at an angle, in a room the slide designer has never visited. Practitioner consensus targets 7:1 or higher for projected slides as a margin against environmental degradation. WCAG's own AAA level is 7:1 for normal text. That is the practical floor for any slide that will be projected.

Gradient backgrounds fail this test structurally. A gradient is a continuous range of luminance values across the slide. The headline that achieves 6:1 contrast at the light end achieves 2:1 at the dark end. The same headline, on the same slide, is legible in one region and invisible in another. Whether a given student can read it depends on which part of the gradient happens to sit behind the specific letters they are parsing. There is no gradient configuration that keeps every text element above a stable contrast ratio. The only fix is a solid background, which has one luminance value, and every contrast relationship can be checked against it precisely.

This is worth stating plainly: a gradient background is an architectural choice that makes contrast compliance impossible to verify or guarantee. It is not a style preference. It is a structural obstacle to legibility.

![A gradient is not one contrast ratio. It is hundreds. You cannot pass them all.](images/05-color-is-doing-nothing-or-harm-fig-02.png)
*Figure 5.2 — Showing same headline text ("Q3 Results") rendered at*

---

## What the failure looks like

The slide has a title: "Q3 Results: Three Initiatives." The content is a status report on four projects. An AI tool produced it from a brief.

The background is a teal-to-purple gradient. The headline is navy. Four bullets list the four initiatives, each in a different color: red, green, orange, blue. Below the bullets, a bar chart shows percent complete for each initiative, each bar in a saturated color matching its bullet. A yellow badge in the upper right reads "NEW" in white text.

![Mockup of the failing slide ](images/05-color-is-doing-nothing-or-harm-fig-03.png)
*Figure 5.3 — Mockup of the failing slide *

Let me count the problems.

The yellow badge: white text on yellow. The contrast ratio is approximately 1.07:1. That is functionally indistinguishable from white on white. The badge is invisible. The constraint it was supposed to satisfy — calling attention to what is new — is not met.

The headline: navy text on a teal-to-purple gradient. The contrast ratio varies from approximately 6:1 at the lightest part of the gradient to 2.1:1 at the darkest. The headline is readable in one region and invisible in another.

The bullet colors: four distinct saturated colors, one per bullet. What does red mean? Nothing. What does green mean? Nothing. They are decorative differentiation. But here is where decorative becomes actively misleading: red is on bullet A, labeled "on track." Green is on bullet B, labeled "ahead of plan." Red for "on track" and green for "ahead of plan" accidentally inverts a deeply learned color convention. In most contexts, red signals a problem and green signals success. The slide has assigned them backwards relative to their actual content. The decorative choice has become a misleading signal — which is worse than no signal at all.

The chart: four bars in saturated colors, rendered in 3D perspective. The 3D perspective means bars closer to the viewer appear larger than bars farther away, regardless of their actual values. Cleveland and McGill named this in 1984: volume is near the bottom of the accuracy ranking. The 3D chart makes the data harder to read while appearing more sophisticated.

And the underlying failure: Initiative C is delayed. That is the piece of information the slide should be organized around — the one claim the slide should make. But Initiative C's bullet is in orange, which has no more salience than the red, green, and blue of the other three. The signal — "this one is the problem" — is invisible under three other colors of equal visual weight.

The slide has six colors doing decorative work and zero colors doing the one job that matters.

---

## What the repair looks like

Same content. Different decisions.

![Mockup of the repaired slide ](images/05-color-is-doing-nothing-or-harm-fig-04.png)
*Figure 5.4 — Mockup of the repaired slide *

The background is a solid near-white. Every contrast relationship on the slide is now stable and checkable.

The color budget is two: a dark neutral for everything that is body content, and one accent for the one thing the slide is saying. What is the slide saying? Initiative C is delayed. That is where the accent goes.

The four bullets are in dark gray — body text, no color differentiation. Next to Initiative C's entry, the word "DELAYED" appears in the accent color. The chart is four horizontal bars sorted by percent complete: three in dark gray, one — Initiative C — in accent. The chart is two-dimensional, axis-labeled, sorted so the reader can compare bars by position along a common scale.

Red appears exactly twice on this slide: once in the text and once in the chart. Both instances mean the same thing. A reader scanning for half a second knows where to look.

The encoding survives colorblindness because red is paired with the text label and bar position. A reader who cannot see the red still reads "DELAYED" in the text and still sees the bar sitting last in the sort. The encoding survives projection because dark gray on near-white passes contrast requirements by a wide margin.

Total colors on the live slide: two. Color attention spent: one place. The eye has nowhere to go but where the slide is pointing it.

The word count on the bad slide and the good slide is identical. The content is identical. The only thing that changed is the decision about what each color is *for*.

---

## The asymmetry of detection

The bad slide looks more designed than the good slide. That is not an accident, and it is not a trivial observation.

AI tools that generate slides are optimizing for a signal they can measure from training data: visual interest. Visual interest, measured at the level of pixel patterns, correlates with color variety, gradient sophistication, and decorative density. The tool produces the gradient, the four saturated bullet colors, the 3D chart, and the yellow badge because those features appear in slides that human raters have called polished or professional.

But the tool has no access to the cognitive experience of the student in the third row, trying to process a gradient-background slide while a speaker is talking. The tool cannot measure working memory load, cannot simulate colorblindness, cannot check a contrast ratio, cannot ask "what does red mean on this slide?" The tool has learned the surface of professionalism, not its function.

The fix, when working with AI tools, is to give the tool an explicit color policy before it generates. Not "use professional colors" — specific rules:

```
Restrict this slide to a two-color palette: one neutral for backgrounds,
body text, and chart marks, and one accent for the elements that carry
the slide's claim.

Reserve the accent for exactly the parts of the slide the audience
should look at first. Every other element uses the neutral.

If color encodes categories in a chart, pair it with at least one other
channel: shape, position in a sort, or a text label. The encoding must
survive loss of color discrimination.

Ensure every text-against-background pairing meets WCAG contrast of
4.5:1 minimum. For projection, target 7:1.

Use a solid background. No gradients.

If a colorblind-safe pair is needed for two categorical colors, use
blue-orange rather than red-green.
```

Two things to notice. First, the prompt specifies the *role* of each color before naming the color. "One neutral, one accent" is a structural rule. "The accent goes where the claim is" is a semantic rule. Together they give the tool a decision procedure rather than an aesthetic preference to approximate. Second, the colorblind-safe pair is named explicitly because the tool will otherwise default to red-green — the most intuitive pair and the most common colorblindness failure mode. You have to name the exception.

---

## The design principle underneath

Cleveland and McGill, Mayer's Signaling Principle, WCAG contrast ratios, and the colorblindness statistics are four different research traditions pointing at the same conclusion: color is a finite, fragile resource that only works when used sparingly, consistently, and with backup.

Finite: working memory cannot attend to more signals than it has capacity for. Color that does not encode is spending capacity the reader cannot recoup.

Fragile: color depends on ambient light, projector quality, display calibration, and individual color vision — all of which vary. A chart readable only under ideal conditions is not a chart a designer can rely on.

With backup: any encoding that uses color as its only channel fails for some fraction of readers. Pairing color with a label, a position, or a shape makes the encoding redundant in the engineering sense — if one channel fails, another carries the information through. That is what accessibility means in practice: not a special accommodation for a minority, but an architectural property that makes the signal robust to the conditions of the real world.

![These three properties are independent failure modes. A good color decision addresses all three.](images/05-color-is-doing-nothing-or-harm-fig-05.png)
*Figure 5.5 — Strip titled "Why color fails when over-relied on"*

![Paired encoding (color + label + position) survives colorblindness. Color alone does not.](images/05-color-is-doing-nothing-or-harm-fig-06.png)
*Figure 5.6 — Colorblind simulation *

Tufte's phrase for this in *Envisioning Information* is "small effective differences" — the discipline of using the minimum visual variation needed to make a distinction, so that variation is available for the moments that matter. Six saturated category colors usually mean the categories are not being separated by position, label, or hierarchy, and color is compensating for structural failures it cannot fix.

The elegant version of the principle is this: if you cannot say what a color means in one word, it should not be on the slide.

---

## Two honest disagreements

Two reasonable designers can read this chapter and disagree.

One position: color is one of the most powerful affective channels available. A deck using only dark gray and one accent is clinical, maybe joyless. A faculty member teaching first-year students at eight in the morning cannot afford to look austere. A richer palette, used with deliberate restraint, signals energy, credibility, and care — things that matter for an audience's willingness to engage.

The other position: every color beyond the two doing semantic work competes with the two doing semantic work. Austere is not the cost of precision — it is the form precision takes. The student confused about what red means has paid a cognitive cost that warmth and energy cannot reimburse.

The vocabulary for the disagreement is the question: *what does this color encode?* If the answer is a specific job — *this category*, *this method*, *this concept* — the color earns its place. If the answer is "it adds warmth" or "it matches the brand," the color is decoration. On that point the two positions converge: decoration on instructional slides is the failure mode both camps are trying to avoid. They disagree about whether some decorative color, deployed carefully, costs less than it buys. That is a defensible disagreement that will not be resolved by a single study.

One thing that is not a disagreement: the contrast standard. WCAG 2.2 was finalized in October 2023 and is the current normative version. APCA, an experimental successor algorithm under consideration for a future version of the standard, aims to better model how humans perceive contrast at different text sizes and weights. As of this writing, APCA is not normative — using it now is a forward bet, not a current best practice. The reader designing for the future should know it exists. The reader preparing this week's lecture should use WCAG 2.1/2.2 ratios and check them with a contrast tool before projecting.

---

Once you know what each color is for, the next question is how many words each slide needs. Some slides have too many colors; almost all slides have too many words. Chapter 6 is about that pressure — where the words come from, why cutting them feels like information loss, and why it usually isn't.

---

**What would change my mind:** A controlled study showing that affectively rich color — four or five palette colors, even when not all semantically loaded — produces meaningfully higher engagement and equivalent or better comprehension compared to a two-color deck in actual classroom conditions. The case for affective color is intuitive and I take it seriously. The evidence for its cost in working memory load is stronger than the evidence for its benefit in engagement. If that balance shifts, the austerity recommendation in this chapter should soften.

**Still puzzling:** I do not have a clean rule for institutional brand color. Every university has a palette and a brand standard, and most of them have four or five colors in it. The honest answer is that brand colors are almost always more numerous than semantic clarity requires, and the designer's job is to pick one from the palette as the accent and treat the others as neutrals. But the politics of that choice — a department insisting its green be used as much as its blue — are real, and I have not found a satisfying way to resolve them through design principles alone.

---

## Exercises

**Warm-up**

1. A slide has five elements: a dark gray headline on white, a red callout box, a blue hyperlink in the body text, a green checkmark icon, and an orange footer. For each element, answer in one word: what does this color encode? If you cannot answer, classify it as decorative. Which elements fail the one-word test, and what does that tell you about the slide? *Tests: applying the one-word encoding diagnostic.*

2. A bar chart shows sales figures for four regions. The designer has used four distinct saturated colors — red, blue, green, orange — one per bar, with no axis labels and no text labels on the bars. According to the Cleveland-McGill hierarchy, what is the problem with using color as the primary encoding here, and what encoding channel should replace it as primary? *Tests: understanding of Cleveland-McGill and color's ranking.*

3. A faculty member projects a slide with medium gray body text (#888888) on a white background (#FFFFFF). Using a contrast checker tool, calculate the approximate contrast ratio and determine whether it meets WCAG AA for normal text (4.5:1), large text (3:1), and the 7:1 projection target. *Tests: ability to apply WCAG contrast standards to a specific pair.*

**Application**

4. A line chart in a climate science lecture shows two trajectories: "Pre-industrial baseline" in green and "Current trend" in red. The lines diverge sharply in the final third. Redesign the encoding so that (a) it communicates correctly to a red-green colorblind reader and (b) it uses a backup channel beyond color. Name the specific changes and why each one addresses a different failure mode from this chapter. *Tests: paired-encoding principle and colorblind-safe palette choice.*

5. An AI-generated slide uses a teal-to-purple gradient background. The headline achieves 5.5:1 contrast at the lightest region of the gradient. Explain why this slide cannot pass a WCAG contrast audit regardless of the headline color chosen, and what architectural change is required to make verification possible. *Tests: understanding gradient backgrounds as structurally incompatible with stable contrast.*

6. You inherit a six-color slide deck from a colleague. Before the next lecture, you have fifteen minutes to apply the two-color discipline to one slide. Walk through the steps: what is the slide's claim, which color becomes the accent, which elements revert to neutral, and what do you check before projecting? *Tests: executing the two-color repair under time constraints.*

**Synthesis**

7. The chapter argues that "loud color is usually a confession that the structure beneath it is failing." Take a slide from a deck you have built that uses four or more colors. Audit it: is the color density compensating for missing labels, missing sort order, or missing categorical hierarchy? Fix the structure first, then reapply the color rule. Describe what changed and why fixing the structure made the color question easier. *Tests: ability to see color as a symptom of structural failure, not the failure itself.*

8. A colleague pushes back: "My students need visual engagement — two colors looks like a government memo." Using the vocabulary from the "Two honest disagreements" section, construct the strongest version of the colleague's argument, then construct the strongest rebuttal. Where do the two positions converge, and where do they genuinely diverge? *Tests: ability to use the chapter's disagreement vocabulary precisely and distinguish the genuine dispute from the apparent one.*

**Challenge**

9. WCAG 2.2 (current) and APCA (proposed for a future version) give different contrast recommendations for the same text-background pair at small sizes. Research the specific difference in how the two algorithms handle light text on dark backgrounds at 14pt. Which algorithm would you use for a slide deck today, and what would change about your recommendation if APCA becomes normative? *Tests: ability to reason about forward-looking standards decisions under current uncertainty; requires research beyond the chapter.*

---

## Tier Connection

Decorative color is friction without yield — every unrooted hue triggers the brain's pattern-recognition search for a rule that does not exist, and the search consumes working-memory budget the slide was supposed to be supporting. The struggle is real; the learning it produces is zero. That is the textbook profile of extraneous cognitive load, and it is the precise opposite of the productive struggle that earns its cognitive cost.

The **phase gate** in this chapter is the `DESIGN.md` file. Color rules belong there — once, with explicit reasons — not in per-slide judgment calls that drift. Six color variables, documented intentions, and the AI applies them consistently across every slide generated. The model does the consistency work (Tier 1). You make the encoding decisions (Tier 4). The file holds the boundary between them. See *Appendix A — The Fundamental Themes*.

**Tags:** color-encoding, Cleveland-McGill, Mayer-signaling, WCAG-contrast, colorblindness, cognitive-load, gradient-backgrounds, two-color-discipline

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 5.1 — Horizontal ranked bar chart of Cleveland-McGill perceptual accuracy

Create a standalone D3 v7 HTML file for a ranked or grouped bar chart titled "Horizontal ranked bar chart of Cleveland-McGill perceptual accuracy". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/05-color-is-doing-nothing-or-harm-fig-01.html`

---

### Figure 5.2 — Showing same headline text ("Q3 Results") rendered at

Create a standalone D3 v7 HTML file for a ranked or grouped bar chart titled "Showing same headline text ("Q3 Results") rendered at". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/05-color-is-doing-nothing-or-harm-fig-02.html`

---

### Figure 5.3 — Mockup of the failing slide

Create a standalone D3 v7 HTML file for a side-by-side comparison diagram titled "Mockup of the failing slide". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/05-color-is-doing-nothing-or-harm-fig-03.html`

---

### Figure 5.4 — Mockup of the repaired slide

Create a standalone D3 v7 HTML file for a side-by-side comparison diagram titled "Mockup of the repaired slide". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/05-color-is-doing-nothing-or-harm-fig-04.html`

---

### Figure 5.5 — Strip titled "Why color fails when over-relied on"

Create a standalone D3 v7 HTML file for a left-to-right flow diagram titled "Strip titled "Why color fails when over-relied on"". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/05-color-is-doing-nothing-or-harm-fig-05.html`

---

### Figure 5.6 — Colorblind simulation

Create a standalone D3 v7 HTML file for a concept map titled "Colorblind simulation". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/05-color-is-doing-nothing-or-harm-fig-06.html`
