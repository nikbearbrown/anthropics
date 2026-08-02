# Chapter 2 — How the Visual System Processes Information

## Two figures, one dataset, and a measurable error

Put two figures in front of yourself. Both encode the same eight numbers: annual electricity generation by source for some country, in terawatt-hours — coal 142, gas 118, nuclear 96, hydro 71, wind 54, solar 38, biomass 19, oil 11 [verify — illustrative figures; replace with a real, cited national energy dataset before course use].

The first figure is a bar chart. Eight bars on a common baseline, sorted descending, generation on the vertical axis. The second is a treemap: eight rectangles whose *areas* are proportional to the same values, packed into a square, in different hues.

Now do the experiment the chapter is built on. Cover the labels. From the **bar chart**, estimate: how much bigger is coal than wind? You will say "about two and a half times," and you will be close — 142 versus 54 is 2.6×. From the **treemap**, estimate the same ratio by eye. Most people land somewhere between "twice" and "four times," with errors two to three times larger than on the bars [High]. Same data. Same reader. The only thing that changed is the *channel* carrying the magnitude — length on a common scale versus area — and your measurement error changed with it.

That error is the entire lesson, and it is not about taste. You did not prefer the bars; you *read them more accurately*. The difference is a property of the visual system you were issued at birth, and it is stable enough across people that we can rank channels by it and predict failures before they happen. This chapter gives you the cognitive architecture that makes those predictions — so that the diagnoses you learned to *name* in Chapter 1 you can now *derive*.

## The channel hierarchy: why length beats area

In 1984, Cleveland and McGill ran controlled experiments asking people to judge quantities encoded in different ways, then measured how far off the judgments were [High]. They produced a ranking of *elementary perceptual tasks* by accuracy. From most to least accurate, roughly:

1. **Position along a common scale** (points or bar tops on a shared axis)
2. **Position along non-aligned scales** (separate panels)
3. **Length** (bar height, with no shared baseline)
4. **Angle / slope** (pie slices, line steepness)
5. **Area** (bubble size, treemap rectangles)
6. **Volume / curvature**
7. **Color hue / saturation** (heatmap shading)

This ranking is the most operationally useful result in the book. Read it as a rule: **match the channel to the precision the task demands.** If the reader must compare quantities precisely, push the encoding *up* the list — position or length. If the reader needs only a rough category or a "more/less" gist, a lower channel may be acceptable, and may buy you something else (a treemap shows part-to-whole packing that bars do not). The treemap is not *wrong* in some absolute sense; it is wrong *for a precise magnitude comparison*, and right for showing nested composition. The failure is always a mismatch between channel and task, never the channel alone.

![A vertical ladder ranking seven perceptual channels from position on a common scale at the top to color hue at the bottom, with a reading-error band that widens as the channel becomes less accurate; the area rung is flagged as where the Chapter 1 circles sit.](images/02-how-the-visual-system-processes-information-fig-01.png)

*Figure 2.1 — The Cleveland–McGill channel-accuracy ladder: position on a common scale is read most accurately, and reading error grows steadily as you descend toward area and hue.*

Notice what this does to the circles from Chapter 1. Diameter-scaled circles put the comparison on channel 5 (area) while squaring the intended ratio. The bar-chart correction moved it to channel 1 (position on a common scale). The cognitive science did not just explain the fix after the fact — it *predicted* it. That predictive power is why we say the theory is an instrument, not decoration.

A second, subtler use: the hierarchy tells you which AI-generated outputs to distrust on sight. A code generator pattern-matches "comparison" to forms it has seen, and it has seen a great many pies, bubbles, and treemaps. When you ask for "a comparison" and receive area, the hierarchy tells you to demand a reason or change the channel.

> **AI Wayback Machine — Jacques Bertin (1918–2010)**
>
> The French cartographer Jacques Bertin, in *Sémiologie graphique* (1967), did something no one had done systematically: he decomposed every graphic into *marks* and the *visual variables* that modulate them — position, size, shape, value (lightness), color (hue), orientation, texture [High]. Crucially, he argued that these variables are not interchangeable. Position is *associative and quantitative*; it preserves order and ratio. Hue is *selective* — good for separating categories — but *not quantitative*: you cannot reliably read "twice as much" from "twice as red," because hue has no natural order [High].
>
> Bertin reached this by analysis, before the experimental confirmation Cleveland and McGill would supply seventeen years later. He is the reason we can say "this attribute is categorical, so encode it with hue, not length" and "this attribute is quantitative, so encode it with position, not hue" as *rules* rather than preferences. When you build the seven-token color system in Chapter 8 and forbid hue from carrying quantity, you are operationalizing Bertin. *Prompt to try: "Show how Jacques Bertin's separation of marks and visual variables anticipates the design-intelligence layer this book teaches."*

## Cognitive load: why the seventh component breaks the figure

Channels govern how accurately a *single* encoding is read. Cognitive load governs how many encodings a reader can hold *at once* before comprehension collapses.

Sweller's cognitive load theory (1988) starts from a hard constraint: working memory is small and easily overrun [High]. When a figure presents more distinct elements than working memory can juggle, the reader does not process them more slowly — they fail to integrate them at all. The figure becomes a wall. Sweller distinguishes *intrinsic* load (the irreducible complexity of the material), *extraneous* load (complexity the presentation adds without need), and *germane* load (effort that actually builds understanding). The design goal is to crush extraneous load to near zero so the reader's scarce capacity goes to the material, not to decoding your layout.

The often-quoted "7 ± 2" figure descends from Miller's 1956 work on memory span, and the precise number is contested — later estimates put the usable chunk count lower, around four [Contested]. The book does not stake anything on the exact integer. What it stakes is the *direction*: above roughly **4–7 simultaneous components**, comprehension degrades, and the degradation is steep, not gradual [Medium]. This is why the design system in Act Two enforces a component limit and a *split decision* — when a figure exceeds the budget, you do not shrink the type; you split the figure. "More information per figure equals more value" is one of the misconceptions this book is built to break, and cognitive load theory is why it is exactly backwards above the threshold.

For the practitioner, load theory yields a discipline: count the components a reader must hold to extract the claim. Every gridline, legend entry, annotation, and color is a component competing for the same scarce buffer. The Brutalist instinct — remove every mark that does not encode — is load theory applied: each removed non-encoding mark returns capacity to the material.

The legend deserves a moment, because it is the load failure engineers commit most. A legend is a *lookup table the reader must hold in working memory*: to read a six-color stacked chart, the reader encodes six color-to-category bindings, then re-fetches each binding every time their eye moves to a new band. That re-fetch is extraneous load, manufactured entirely by the decision to separate the label from the thing labeled. Direct labeling — putting "Coal" on the coal band — deletes the lookup table, returning the six slots of capacity to the actual comparison. This is why "use a legend" is, for many figures, a small design failure that compounds: it is not merely inelegant, it is measurably costlier to read, and the cost scales with the number of categories. When you see an AI tool default to a legend (it almost always will, because legends are the dominant pattern in its training data), read it as a load liability to be removed, not a convention to be honored.

![Two panels comparing a chart with a separated color legend, where dashed shuttle arrows show the eye re-fetching each color-to-category binding, against the same chart with labels placed directly on the bands and no lookups required.](images/02-how-the-visual-system-processes-information-fig-02.png)

*Figure 2.2 — The legend tax: a separated legend forces a working-memory re-fetch on every glance, while direct labeling deletes the lookup table and satisfies spatial contiguity.*

A related discipline is the *split decision*, which Act Two formalizes. When a figure's component count exceeds the budget, the engineer's instinct is to compress — smaller type, tighter spacing, a denser legend. Load theory says this is exactly wrong: compression preserves the component count while degrading legibility, doubling the penalty. The correct move is to *split* — two figures, each under budget, each making one claim cleanly. A figure that needs ten components is not a hard figure to design; it is two figures wearing one frame.

## Dual coding: text and image as two channels into one mind

Paivio's dual coding theory (1986) proposes that the mind has two partly independent systems for representing information — a *verbal* system for language and a *nonverbal/imagery* system for pictures and spatial structure — and that information encoded in both is remembered and understood better than information in either alone [High]. The two systems can reinforce each other.

For infographic design this is the theoretical license for the genre itself: a well-built infographic is not a chart with text bolted on, nor prose with a decorative picture. It is a *deliberate integration* of a verbal channel and a visual channel that say the same thing two ways. The headline states the claim; the encoding shows it. When they agree — as in the corrected bar chart of Chapter 1 — the two coding systems converge and comprehension is fast and durable. When they disagree — as in the misleading circles — the systems conflict, and the reader is left with a memorable image and a contradicted caption. Dual coding explains both the power and the danger.

But integration is not the same as duplication. A label that merely restates the axis adds verbal load without adding a second representation — it is redundant, not reinforcing. The craft, which Chapter 9 makes precise, is putting verbal and visual content in *spatial and semantic register* so each does work the other cannot. Mayer's multimedia research (2009) sharpens this into placement rules — the *spatial contiguity* principle: words belong next to the graphic element they describe, not in a distant legend, because the reader otherwise spends working memory shuttling between them [High]. That principle is why direct labels beat legends, and we will cash it out in Chapter 9. For now: text and image are two doors into one mind; align them or you build a contradiction.

## Gestalt: the grouping the reader sees before they decide to look

Before any conscious reading happens, the visual system organizes the field into groups. The Gestalt principles — proximity, similarity, enclosure, connection, common region, continuity — describe these automatic groupings [High]. They are *pre-attentive*: they happen in the first fraction of a second, without effort or choice, and they are extraordinarily powerful. Things close together are read as belonging together. Things sharing a color are read as a class. A line connecting two marks asserts a relationship whether or not one exists.

This is leverage and hazard in one. Leverage, because you can group related content by simply placing it near, enclosing it, or coloring it alike — no label required. Hazard, because accidental proximity asserts a relationship you did not intend, and an AI tool laying out elements by coordinate has no idea which adjacencies are meaningful. A legend floating near an unrelated cluster will be read as labeling that cluster. Two series sharing an accent color will be read as the same category. Gestalt is always on; the only question is whether it is working for your claim or against it.

The practical move: *spend* Gestalt deliberately. Encode "these belong together" with proximity and common region before you reach for a label, because the pre-attentive grouping arrives before the label is read. This is also where Brutalism's "honest hierarchy" lives — the visual grouping the reader perceives must match the logical structure of the content, or the figure groups a lie.

## Memorability is a different axis than comprehension

One more distinction belongs in the architecture, because it cuts against a natural inference from everything above. Having learned that the visual system reads channels with measurable accuracy and groups pre-attentively, a careful reader concludes that the *most accurate, lowest-load* figure is always the best one. That is right for comprehension and silent about memory — and the two are separate outcomes on separate axes [High].

Borkin et al. (2013) measured *memorability* — whether people, shown a visualization briefly, later recognized it — and found that visualizations with distinctive, recognizable features were remembered better than spare statistical charts [High]. This is not a refutation of the channel hierarchy; the two findings answer different questions. The hierarchy predicts how *accurately* a reader extracts a quantity *in the moment*. Memorability predicts whether the figure *survives in the reader's memory* afterward. A figure can be high-comprehension and low-memorability (a clean bar chart you forget by lunch) or low-comprehension and high-memorability (a vivid infographic you recall the gist of but could not reconstruct the numbers from).

The design consequence is to *ask which outcome the figure's job requires* before optimizing. A figure whose job is a precise, one-time comparison in a paper should be optimized for comprehension; memorability is irrelevant. A figure whose job is to lodge a single idea in a lay audience's memory for a campaign may legitimately trade some comprehension precision for memorability. Confusing the two — optimizing a precise-comparison figure for memorability, or a memory-campaign figure for analytic precision — is a category error, and it is the error that the embellishment debate (Chapter 3) keeps re-staging. Hold the axes apart: the architecture in this chapter governs comprehension; memorability is a second, sometimes competing, design objective.

## Worked example: diagnosing a climate figure by mechanism

**Problem statement.** An AI tool produced a figure for a climate brief: a stacked area chart of CO₂ emissions by sector over thirty years, six sectors, six hues, a legend in the top-right, the goal being to let readers compare each sector's *trajectory*.

**First attempt.** Stacked areas in six hues; legend off to the side. It looks rich and serious.

**Design diagnosis — three mechanisms, named.**
1. *Channel mismatch.* Reading an individual sector's change over time from a *stacked* area requires judging the thickness of a band whose baseline wobbles — a length-without-common-baseline task (channel 3, degraded further by the moving baseline). Only the bottom band sits on a common scale. The comparison the figure promises is on a poor channel for five of six series [High].
2. *Cognitive load.* Six categories, six hues, plus a legend the reader must cross-reference: components exceed the comfortable budget, and the legend forces a working-memory shuttle between color swatch and band [Medium].
3. *Gestalt / contiguity failure.* The legend's separation from the bands violates spatial contiguity (Mayer); proximity is doing no useful grouping work because the labels are nowhere near the things they label [High].

**Corrected version.** Split into a small-multiples grid: six tiny line charts, one per sector, each on its *own common baseline*, each *directly labeled* in place, sorted by total emissions. Trajectory now reads on position-over-time (channel 1); each panel holds well under the load budget; labels sit on the lines (contiguity satisfied); hue is freed from carrying category and can be dropped to a single ink. The claim — "which sectors are rising, which falling" — now reads in seconds.

**The lesson.** *A single figure that overruns the channel and the load budget is two or three figures pretending to be one.*

**The limit.** Deciding that the reader's task was *per-sector trajectory* (not total emissions, not part-to-whole share) is an editorial judgment about communicative intent. Change that intent and the stacked area might be right after all. The tool cannot read the brief's purpose; you can. That intent decision, plus the decision to spend the freed hue channel on nothing rather than re-introducing it, are the two human judgments this figure's disclosure would name.

## Design Critique #1 (25 pts)

**Deliverable.** Select one infographic — yours, an AI-generated one, or a published example — and write a 500–800 word critique organized strictly by mechanism, not by impression.

1. **Channel audit** *(8 pts).* For the figure's primary comparison, name the channel in use, place it on the Cleveland–McGill hierarchy, state the reader's task, and judge whether channel and task match. If they mismatch, name the channel you would substitute and why.
2. **Load audit** *(6 pts).* Count the components a reader must hold to extract the central claim. State whether the figure is over or under the 4–7 budget, and identify the single highest-value component to remove. Distinguish at least one *extraneous*-load element from the *intrinsic*-load core.
3. **Gestalt / contiguity audit** *(6 pts).* Identify one place where automatic grouping (proximity, similarity, enclosure, connection) is doing work — for the claim or against it — and one place where text and the element it describes are *not* in spatial register, with the fix.
4. **AI Use Disclosure** *(5 pts).* Name **at least two** judgments in your critique that required your reasoning and that an AI tool could not have supplied — e.g., deciding what the reader's *task* actually is, or deciding which of two competing groupings the figure *should* assert. *Missing disclosure: −15 per policy.*

## Bridge

You now have the architecture: a channel hierarchy that ranks accuracy, a load budget that caps complexity, dual coding that licenses text-plus-image, and Gestalt that groups before the reader chooses to look. These are constraints, not preferences. The natural next question is whether there is a *design philosophy* that takes these constraints as its starting axioms rather than treating them as afterthoughts. There is. Chapter 3 argues that Brutalism — exposed structure, functional marks, honest hierarchy — is not an aesthetic at all but precisely the operationalization of the perceptual science you just learned.

## Sources

- Cleveland, W. S., & McGill, R. (1984). *Graphical Perception.* Journal of the American Statistical Association. — The experimental channel-accuracy ranking. [High]
- Bertin, J. (1967/1983). *Sémiologie graphique / Semiology of Graphics.* — Marks and visual variables; which variables are quantitative vs. selective. [High]
- Paivio, A. (1986). *Mental Representations: A Dual Coding Approach.* Oxford University Press. — Verbal and imagery systems; reinforcement through integration. [High]
- Sweller, J. (1988). *Cognitive Load During Problem Solving: Effects on Learning.* Cognitive Science. — Intrinsic/extraneous/germane load; the component budget. [High]
- Mayer, R. E. (2009). *Multimedia Learning.* Cambridge University Press. — Spatial contiguity, coherence, signaling; placement of words near graphics. [High]
- Miller, G. A. (1956). *The Magical Number Seven, Plus or Minus Two.* Psychological Review. — Origin of "7±2"; the precise capacity figure is contested by later work. [Contested]
