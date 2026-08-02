# Chapter 9 — Annotation: When It Earns Its Place

## Opening: Ten seconds, two versions

Here is an experiment you can run in a classroom or on yourself. Take an infographic — say, a chart of median household income by race and ethnicity across four decades, a social-demographic figure most readers half-recognize — and prepare two versions. The data are identical. The marks are identical. The colors and the axes are identical. The *only* difference is the annotation.

Version A carries annotation at the defaults a tool leaves behind: a legend in the top-right corner, a label on every one of the forty data points, a title that restates the axis ("Median Household Income by Year"), and a stray text box that says "income tends to rise over time." Version B carries four sentences. One sits directly beside the line that diverges most sharply and reads "The gap widens fastest after 2008." One labels the two endpoint lines directly, killing the legend. One sits under the title and states the figure's actual claim. One small-print caveat names what the dollars are *not* adjusted for.

Show each version to a different group for exactly ten seconds, then take the figure away and ask: *what was the main point?* Group B will tell you about the post-2008 divergence. Group A will tell you the chart was "about income" and that there were "a lot of lines." [Medium — this is the standard signaling/spatial-contiguity result from Mayer's multimedia learning work, restaged as a classroom demonstration; the specific dataset is illustrative.]

The lesson lands before any theory: annotation is not the layer you add at the end to be helpful. It is, in most infographics, **the highest-leverage design decision you will make** — the single change that most moves comprehension up or down. Version A had *more* annotation than Version B and communicated less. That inversion is the whole chapter. More text is not more help. The right four sentences, placed correctly, beat forty labels every time.

And it is irreducibly human. A tool can generate captions all day — it is, if anything, far too eager to. What it cannot do is decide *which* sentence is the one worth placing beside the line, and which thirty-nine labels are clutter wearing the costume of thoroughness. That decision requires knowing what the figure is *for*.

## Core content

### The four-job test

Annotation earns its place when it does one of exactly four jobs. If a piece of text on your figure is not doing one of these, it is not annotation — it is noise, and it should be cut [High — synthesizes the settled position across Mayer, Schwabish, and Cairo].

1. **Interpretation.** It tells the reader what a feature of the data *means*. "The gap widens fastest after 2008" interprets a slope the reader can see but might not weigh correctly. Interpretation is the highest-value annotation because it does the work the marks cannot: it states the claim.
2. **Orientation.** It tells the reader how to *read* the figure — what the axes are, which direction is "more," where to start. A direct label on a line ("Group A") orients without forcing a trip to a legend.
3. **Context.** It supplies information *not in the data* that the reader needs to judge it. "U.S. dollars, not inflation-adjusted" or "recession shaded" is context. So is a reference line marking a meaningful threshold.
4. **Caveat.** It names a limitation, exclusion, or source of doubt. "Excludes households with zero reported income" is a caveat. Caveats are where editorial honesty lives; they are also where AI-drafted annotation is weakest, because a model does not know what *your* data quietly leaves out.

![Candidate annotations passing through four gates — interpretation in red, then orientation, context, caveat — with a cut bin for text that does no needed job](images/09-annotation-when-it-earns-its-place-fig-01.png)

*Figure 9.1 — The four-job test: candidate text either does one of four jobs — interpretation (red, the highest value), orientation, context, or caveat — or it falls to the cut bin as clutter.*

The test is easy to state and brutally hard to apply — which is why this chapter uses a domain you recognize. The difficulty is that almost any label *can* be rationalized as doing one of the four jobs if you squint. "Income tends to rise over time" sounds like interpretation. It is not: it interprets nothing specific about *this* figure, it restates a generality the reader already holds, and it competes for attention with the one sentence that does carry the claim. The four-job test is not "could this text plausibly do a job?" It is "**does this text do a job that the figure needs done and that no other element is already doing?**" Run it ruthlessly. Most candidate annotation fails.

### The spatial proximity rule

Where annotation sits is nearly as important as whether it exists. Mayer's spatial-contiguity principle states that people learn better when words and the corresponding graphics are placed *near each other* rather than far apart, because separation forces the reader to hold one in working memory while searching for the other [High — Mayer, *Multimedia Learning*]. A legend in the corner is a spatial-contiguity violation by design: it puts the key as far as possible from the thing it keys.

The operational rule: **place the annotation as close as possible to the mark it explains, and prefer the order adjacent → leader line → legend.**

- **Adjacent** is best. Label the line at its endpoint. Put the interpretation sentence in the white space *beside* the feature it interprets. No leader line needed because none is needed.
- **Leader line** is the fallback when adjacency would cause overlap. A thin leader (ink, `stroke-width` 1) connects the label to its mark. The leader is itself apparatus — keep it hairline and unobtrusive.
- **Legend is the last resort.** A legend is an admission that you could not place the labels near their marks. Sometimes — a dense scatter with twelve categories — it is unavoidable. But in a Brutalist editorial figure, reaching for a legend should feel like a small defeat, and you should first ask whether the figure has too many categories to begin with.

Direct labels beat legends not because legends are ugly but because legends cost working memory the reader needs for the actual comparison.

### The blur test for annotation hierarchy

You met the blur test in Chapter 3 as a check on overall figure structure. Applied to annotation, it answers a specific question: *do my headline, my main visual, and my primary annotation form a visible hierarchy at low resolution?*

Blur the figure — squint, defocus, or apply a Gaussian blur in any image tool — until you can no longer read the words. Three things should still be distinguishable by size, weight, and position: the headline (largest, EB Garamond display), the main visual (the marks), and the *one* primary annotation (the interpretation sentence). If all your annotation blurs into one undifferentiated gray texture, you have no annotation hierarchy — every label is shouting at the same volume, which means none is heard [High — consistent with pre-attentive size/weight processing from Chapter 2]. The fix is not to delete everything; it is to make the one sentence that carries the claim larger and darker (ink, not secondary gray) and demote the rest.

### Annotation that clutters

It helps to name the recurring offenders so you can spot them by reflex:

- **The axis restater.** A label that repeats what the axis already says. If the y-axis is "%" and you label a bar "37%", fine — that is a direct value, useful. If you label it "this bar shows 37 percent," you have spent a sentence on what the axis already communicates.
- **The title that names the variables instead of the claim.** "Median Income by Year and Group" is a description; "The income gap widens fastest after 2008" is a claim. An editorial infographic should make a claim in its title. (A purely analytical chart in a methods appendix may legitimately use a descriptive title — know which you are making.)
- **The over-labeled series.** Forty points, forty labels. The reader cannot attend to forty things; you have hidden the signal in the labeling. Label endpoints, extrema, and the points your claim depends on. Nothing else.
- **Decorative text.** A pull-quote, a motivational tag, a redundant caption. If it does none of the four jobs, it is decoration, and Brutalism does not permit decoration that fails to encode.

### Density is editorial judgment, not a rule you can hardcode

It would be convenient if annotation reduced to a count — "no more than five labels," "always a caveat." It does not, and the place where the four-job test stops being mechanical is exactly here. **Annotation density is an editorial judgment that depends on audience, medium, and the figure's job** [Contested as a fixed rule; settled as a principle]. A figure for a peer-reviewed methods appendix can carry dense, technical annotation because its readers will sit with it; the same figure projected at an all-hands for ten seconds must shed nearly all of it or fail. Sparse labeling can *under-explain* — a single unlabeled inflection leaves the reader guessing — while dense labeling can *overwhelm*. There is no count that is right across contexts.

What is *not* a matter of judgment is the four-job test and the placement hierarchy; those hold everywhere. The judgment is calibration: *given this audience and this medium, how much interpretation does the reader need supplied versus how much can they be trusted to infer?* This is precisely the kind of decision an AI tool cannot make, because it does not know who is reading or under what time budget — and it is precisely the decision a model will get wrong by defaulting to "more," since adding a label always *looks* like adding help. The density call is yours, and it is one of the human-judgment decisions worth naming in a disclosure.

A useful discipline: state the comprehension budget *before* you annotate. "Ten seconds, projected, mixed audience" forces sparse, claim-first annotation. "A reader with two minutes and domain expertise" permits density. Decide the budget first; let it govern the density; never let the tool's default decide for you.

### Annotation at decision points

The positive principle that organizes all of the above: **annotate at the points where the reader makes a decision.** The reader's eye arrives somewhere, asks a question, and either gets an answer or gets lost. Annotation belongs exactly at those junctions — the inflection in the line, the outlier, the crossover where two series swap order, the threshold that changes the interpretation. Annotation spent anywhere else is annotation spent where the reader was not asking. This is the discipline that turns the four-job test from a filter into a placement strategy: find the decision points, then ask what job each one needs done.

## Worked example: the wage-gap figure

**Problem statement.** A line chart of median household income for two groups, 1980–2020, for a policy brief. The brief's claim: the gap is not static — it widens after the 2008 recession. Show that.

**First attempt (specification-less AI output).** Prompted "add helpful annotations to this income chart," a coding agent produced: a title reading "Median Household Income Over Time"; a top-right legend mapping color to group; a numeric label on every data point (82 labels); a text box reading "Income generally increases over the period"; and a footnote in 8px gray: "Source: data." Every element is *plausibly* annotation. The figure is unreadable in ten seconds.

**Design diagnosis (four-job test, run ruthlessly).**
- Title: descriptive, not the claim. Fails — does no job the figure needs; the *claim* is undone.
- Legend: orientation, but via the worst placement. Replaceable by direct labels (better job, better place).
- 82 point labels: none individually interprets, orients, or caveats; collectively they bury the signal. Fail.
- "Income generally increases": pseudo-interpretation of a generality. Fails the strict four-job test.
- "Source: data": gestures at context but supplies none. Fails as written.

**Corrected version (annotation that earns its place).**
- **Title (interpretation):** "The income gap widens fastest after 2008." The claim, stated. EB Garamond display.
- **Direct labels (orientation):** each line labeled at its 2020 endpoint, adjacent, no legend. Legend deleted.
- **One interpretation sentence (interpretation), placed adjacent** to the post-2008 divergence in the chart's white space: "After 2008, the upper line recovers; the lower line does not." No leader line — it sits in the gap it describes.
- **Reference shading (context):** the 2008–2009 recession lightly shaded with `--color-border`, labeled once.
- **One caveat (caveat), small print, `--color-secondary`:** "U.S. dollars, not inflation-adjusted; excludes households reporting zero income." A real limitation, named.
- Point labels reduced to the two endpoints and the 2008 inflection — the three points the claim depends on.

**Blur test.** Defocus: title (large, dark) > the diverging lines (the marks) > the one interpretation sentence (ink, mid-size) > everything else (smaller, gray). A visible hierarchy. Pass.

**The lesson.** Annotation is subtraction before it is addition: the four sentences that earn their place are visible only once the forty that do not have been cut.

**The limit.** The agent can draft fifty candidate sentences in a second. It cannot know that *post-2008 divergence* is the claim this brief exists to make, or that *not inflation-adjusted* is the caveat that keeps the figure honest for this audience. Choosing the one interpretation and the one caveat is the human-judgment work — and it is what your disclosure names.

## AI Wayback Machine: Richard Saul Wurman and the cost of unorganized information

The architect **Richard Saul Wurman** coined the term "information architecture" and spent a career arguing that information has no value until it is *organized for understanding* — that the job of the designer is not to present data but to make it answer a person's question [High]. (He coined the phrase in a talk at the 1976 AIA national convention; Wayback target: Wikipedia "Richard Saul Wurman.") He liked to say that he was interested only in the gap between what he understood and what he didn't, and that the entire purpose of a graphic was to close it.

That is the four-job test before it had a name. Wurman's instinct — that most of what gets added to a figure is added for the *maker's* comfort, not the *reader's* comprehension, and should be cut — is exactly the discipline this chapter asks you to internalize against a tool that will happily generate annotation forever.

> **Prompt to try:** "Explain how Richard Saul Wurman's idea of information architecture helps an engineer decide which annotations to cut from an AI-over-annotated infographic — and connect it to the four-job test of interpretation, orientation, context, and caveat."

The throughline: Wurman's career is a forty-year argument that the highest-value design act is often deletion. An AI annotation generator is a deletion-resistance machine. You are the deletion.

## Assessment — Design Critique #4 (25 pts)

Take a published, over-annotated infographic in the social/demographic domain (or one an AI tool generates for you from a vague prompt — keep the prompt). In 500–700 words plus a marked-up image:

1. **Apply the four-job test** to every annotation in the figure. Tabulate each one as interpretation, orientation, context, caveat, or *cut*, with a one-line justification for each verdict (10 pts).
2. **Re-place** the surviving annotations using the adjacent → leader line → legend hierarchy. State at least one legend you eliminated and what you replaced it with (7 pts).
3. **Run the blur test** on your revised version and report whether headline, main visual, and primary annotation form a visible three-level hierarchy. Attach the blurred image (5 pts).

Include an **AI Use Disclosure** naming at least two judgment decisions an AI tool could not have supplied — for example, *which* single sentence carries the figure's claim, and *which* caveat the data require that no model could infer from the data alone (3 pts).

## Bridge

You can now decide what each element of a figure encodes, how it is colored and set, and which words earn their place beside it. What you cannot yet do is decide how the whole thing is *arranged* — whether it is one panel or six, what gets the top-left where the eye lands first, and, most importantly, what gets *left out*. Chapter 10 is the capstone of Act Two: it covers layout and the CAJAL specification system, the process that turns a vague brief into a complete, defensible design specification document — the artifact you will hand to Claude Code in Act Three.

## Sources

- Mayer, Richard E. *Multimedia Learning.* 2nd ed. Cambridge University Press, 2009. Source for the spatial-contiguity and signaling principles underlying the proximity rule and the blur-test hierarchy.
- Schwabish, Jonathan. *Better Data Visualizations.* Columbia University Press, 2021. Practitioner reference for direct labeling, annotation discipline, and clutter reduction.
- Cairo, Alberto. *The Functional Art.* New Riders, 2012. Communication-first basis for reader-centered, claim-making annotation.
- Paivio, Allan. *Mental Representations: A Dual Coding Approach.* Oxford University Press, 1986. Foundation for verbal-visual integration (why adjacent text and graphic reinforce one another).
- Sweller, John. "Cognitive Load During Problem Solving: Effects on Learning." *Cognitive Science*, 1988. Working-memory basis for the cost of legends and over-labeling.
- Wurman, Richard Saul. Originator of the term "information architecture" (coined at the 1976 AIA national convention); *Information Architects*, Graphis, 1996.
