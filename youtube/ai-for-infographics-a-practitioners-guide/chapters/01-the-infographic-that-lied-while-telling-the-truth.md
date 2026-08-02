# Chapter 1 — The Infographic That Lied While Telling the Truth

## A figure that passed every check and failed the only one that mattered

A public-health agency publishes an infographic during an outbreak. The headline reads: *"Vaccination cuts severe outcomes."* Beneath it sit two circles. The left circle, labeled UNVACCINATED, is large and ominous. The right circle, labeled VACCINATED, is small. The visual reads, instantly and unmistakably, as *huge versus tiny* — a near-total collapse in risk. A reader glances, absorbs the relief, and moves on.

Now read the numbers printed inside the circles. The left circle says 8 severe cases per 1,000. The right circle says 2 per 1,000. That is a real and important reduction — a factor of four. But the circles do not encode 8 and 2. Look closely and you find the designer set the *diameter* of each circle proportional to the value. The unvaccinated circle is four times the diameter of the vaccinated one. Because area scales with the square of diameter, the big circle covers *sixteen* times the area of the small one [High]. The reader's visual system does not read the printed labels first; it reads the blobs, and the blobs say sixteen-to-one. The figure has taken a true 4× and shown it as a perceptual 16×.

Every number on this figure is correct. You could fact-check it against the agency's own dataset and find nothing wrong. And yet the figure lies. It tells the truth in its data and a falsehood in its form. This is not a hypothetical edge case [verify — replace with a cleared, real published example or an instructor-created equivalent before course use; the area-encoding failure itself is well documented]. It is the most common kind of infographic failure, and it is the one this entire book exists to make you incapable of shipping by accident.

You have probably made this exact error. If you have ever asked an AI tool for "a figure comparing two quantities" and accepted a result with proportional circles, bubbles, or pictograms scaled by height, you produced a version of it. The tool did exactly what you asked. The judgment it could not supply was the one that decides *which visual channel carries the comparison* — and that judgment is yours.

## Every infographic makes a claim

Start with the idea that does the most work in this chapter: **an infographic is an argument, not an illustration.** It asserts something about the world. Sometimes the claim is explicit, printed in the headline — *vaccination cuts severe outcomes.* But there is always a second claim, a *structural* claim, made silently by the encoding itself. The structural claim of our circles is: *the difference is enormous.* That structural claim is carried not by any sentence but by the relationship between two areas.

This is why a figure can be factually correct and still mislead. The explicit claim ("8 versus 2") and the structural claim ("sixteen-to-one") can disagree, and when they do, the reader believes the structure. The eye is faster than the caption [High]. The structural claim is read pre-attentively, before conscious reading begins; the labels are read second, if at all. A designer who controls only the numbers and leaves the encoding to chance — or to a code generator — has surrendered control of the actual message.

So the first diagnostic question you will ever ask of an infographic, yours or anyone else's, is not *is the data right?* It is: **what is this figure's structural claim, and does it match the explicit one?**

## Data accuracy versus perceptual accuracy

We now have the book's central distinction, and it is worth stating with care.

**Data accuracy** is the property that the numbers, sources, and stated relationships are correct. It is necessary. It is also, by itself, almost worthless as a guarantee of honesty.

**Perceptual accuracy** is the property that the impression a reader forms from the figure's *form* matches the impression the data warrant. It is the question of whether the visual structure delivers the true magnitude, direction, and proportion to a human visual system — not to a parser.

Our circles are data-accurate and perceptually inaccurate. The two are orthogonal: you can have either without the other. A figure with perfect data and a square-of-the-diameter area scale is perceptually inaccurate. A figure with a clear bar chart but a fabricated dataset is perceptually accurate and data-false. The whole craft lives in getting both right, and the failure mode this book targets is the seductive one — the figure that gets the data right and *therefore feels trustworthy* while the form does the lying.

![Side-by-side panels of the same 8-versus-2 data: honest bars on a common baseline read as a 4× difference, while diameter-scaled circles read as a 16× difference because area grows with the square of diameter.](images/01-the-infographic-that-lied-while-telling-the-truth-fig-01.png)

*Figure 1.1 — Same data, two structural claims: length on a common baseline delivers the true 4×, while diameter-scaled circles inflate it to a perceptual 16×.*

Why does form win? Because visual authority amplifies. A figure carries an implicit promise of objectivity: it looks measured, mechanical, neutral. That authority is borrowed from the data's correctness and spent on the form's distortion. The reader extends trust earned by the numbers to a claim made by the geometry. This is the mechanism by which "pretty but wrong" becomes "trusted but wrong," and it is exactly why AI-generated polish is dangerous: polish *increases* the authority while doing nothing for the perceptual accuracy.

Consider the asymmetry of effort. A misleading sentence in a paper can be challenged with another sentence; the reader holds both in working memory and weighs them. A misleading figure resists challenge in the same way, because the rebuttal — "actually the areas exaggerate the ratio four-fold" — is a slow verbal correction fighting a fast pre-attentive impression that has already landed. The figure got there first, and first impressions in perception are sticky. This is not a reason to distrust figures; it is a reason to hold the people who make them, including you, to a higher standard of perceptual honesty than we hold a paragraph. The authority that makes infographics worth producing is the same authority that makes a dishonest one worse than a dishonest sentence. With the power comes the obligation.

There is also a production-pipeline reason this matters now, specifically. The cost of generating a polished figure has collapsed to near zero. A decade ago, the labor of building a clean chart imposed a small tax that, as a side effect, made the designer *look at* the encoding — you could not place every bar by hand without noticing what the bars were doing. Generation removes the tax and removes the side effect with it. The polished figure now arrives before any human has examined its structural claim. That is why this book inserts a deliberate examination step — the human design layer — back into a process from which automation quietly deleted it.

> **AI Wayback Machine — William Playfair (1759–1823)**
>
> The Scottish engineer and political economist William Playfair invented or popularized the line graph, the bar chart, and the pie chart, publishing them in his *Commercial and Political Atlas* (1786) and *Statistical Breviary* (1801) [High]. He did this a full century before perceptual science existed to explain why his choices worked. Playfair's bars encoded magnitude as *length on a common baseline* — the most accurately read channel humans have [High] — and his time series put quantity on position along an axis. He was not theorizing about cognitive architecture; he was an engineer reaching, by trained intuition, for forms that delivered true magnitudes to the eye.
>
> The instructive part is where he reached *wrong*. Playfair's pie charts and his occasional area-based comparisons introduced exactly the channel — area — that humans estimate least reliably. Two centuries later your AI tool will happily generate a Playfair pie or a proportional bubble because it pattern-matches "comparison" to "circles." Playfair's legacy is the lesson of this chapter in miniature: the same designer, the same dataset, can encode a relationship honestly or misleadingly, and *only the encoding choice* — not the data — decides which. *Prompt to try: "Explain how William Playfair's choice of bars over areas helps an engineer avoid a polished but indefensible infographic."*

## Memorability is not comprehension

Here is where the naïve fix goes wrong. A reader who absorbs the data-vs-perception distinction often jumps to a conclusion: *strip everything decorative; the plainest chart is the truest.* That is half right, and the half that is wrong matters.

Borkin and colleagues, in *What Makes a Visualization Memorable?* (2013), found that visualizations with distinctive features — pictograms, unusual forms, human-recognizable imagery, color — were *more memorable* than plain statistical charts [High]. People remembered them. This is sometimes cited as license to decorate. But memorability and comprehension are different outcomes measured by different tests [High]. A figure you can recall the *gist* of a day later is memorable. A figure from which you can extract the *correct quantitative relationship* in ten seconds is comprehensible. They are not the same axis, and a figure can score high on one and low on the other.

The related and frequently mangled result is Bateman et al., *Useful Junk?* (2010). The careful finding: embellishment that was *semantically meaningful* — imagery related to the chart's actual subject — improved long-term recall without reliably degrading comprehension accuracy in their study [Contested]. This is not "decoration is good." It is "*meaningful* decoration may aid memory; *arbitrary* decoration carries risk and earns nothing." The study has been challenged on generalizability — small sample, specific tasks, particular charts — so we tag it Contested and refuse to build doctrine on it [Contested]. What survives is a discipline, not a slogan: a mark earns its place by doing a job. Memorability is a job. Restating the axis label is not.

You will meet this distinction again in Chapter 3, where Brutalism's "functional marks" commitment turns it into a checklist. For now, hold the line: do not confuse *they remembered it* with *they understood it*. Our circles are highly memorable. That is part of the problem.

## Classifying a claim: accurate, misleading, or indeterminate

The practical skill of this chapter is triage. Given a figure, you sort its central claim into one of three bins.

- **Accurate** — the structural claim and the explicit claim agree, and the encoding delivers the true relationship to the eye. A bar chart of 8 versus 2 on a common baseline, with a zero origin: accurate.
- **Misleading** — the data are correct but the form distorts the relationship. Our diameter-scaled circles: misleading. A truncated y-axis that turns a 2% change into a visual cliff: misleading. A dual-axis chart engineered so two unrelated series appear to "cross": misleading.
- **Indeterminate** — you cannot tell, because the figure withholds what you need. A bubble chart with no scale legend and no stated encoding rule: you genuinely cannot say whether area or diameter carries the value, so you cannot certify it. Indeterminate is a real verdict, and an important one: *I cannot defend this* is different from *this is wrong*, and both are different from *this is fine.*

The reason indeterminate matters for your own work: an AI-generated SVG is *indeterminate by default*. You did not specify the encoding rule, so you cannot certify the result. The remedy is not to squint harder at the output. It is to populate the design specification *before* generation so the verdict is decidable. This is the thesis in operational form — the human design layer makes the figure's claim defensible; the AI execution layer cannot.

It is worth being concrete about what "indeterminate by default" buys an adversary, including the careless version of yourself. When a figure is indeterminate, its maker can claim whichever verdict is convenient after the fact. Challenged, the maker of the proportional circles can say "but the real numbers are right there in the labels" — retreating to data accuracy — while the figure goes on delivering its 16:1 impression to every reader who does not stop to do arithmetic. Indeterminacy is not neutral; it is a hiding place. A defensible figure forecloses the hiding place by stating its encoding rule so plainly that the verdict can only be *accurate* or *misleading*, never *who can say*. Specification is, among other things, the refusal to hide.

## Worked example: the specification-less generation

Let us run the failure end to end, because seeing the SVG is the point.

**Problem statement.** You need a figure comparing severe-outcome rates: 8 per 1,000 unvaccinated, 2 per 1,000 vaccinated.

**First attempt (what an AI tool produces without specification).** You prompt: *"Make an SVG infographic comparing 8 and 2 severe cases per thousand for unvaccinated vs vaccinated."* You get, plausibly, something like:

```svg
<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <circle cx="110" cy="120" r="80" fill="#c0392b"/>
  <circle cx="300" cy="120" r="20" fill="#27ae60"/>
  <text x="110" y="125" text-anchor="middle" fill="#fff">8</text>
  <text x="300" y="125" text-anchor="middle" fill="#fff">2</text>
</svg>
```

The radii are 80 and 20 — a 4:1 ratio, matching the data. But area goes as r², so the red circle has 6,400π and the green 400π: a **16:1** area ratio. The figure is data-accurate and perceptually inaccurate.

**Design diagnosis.** The violated principle is channel selection. The comparison task is *magnitude judgment between two values*, and the chosen channel is *area*, which humans read with high error [High]. Worse, the designer (or the tool) scaled the channel inconsistently — diameter proportional to value, so the *read* channel (area) is the square of the *intended* one. There is also a color problem we will return to in Chapter 8 (red/green fails for color-blind readers), but the load-bearing failure is the channel.

**Corrected version (specification-driven).** The specification says: comparison task → magnitude → use position/length on a common baseline. Bars, zero origin, shared scale:

```svg
<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg">
  <!-- baseline -->
  <line x1="60" y1="200" x2="360" y2="200" stroke="#1a1a1a" stroke-width="2"/>
  <!-- unvaccinated: 8 -> 160px -->
  <rect x="100" y="40" width="60" height="160" fill="#1a1a1a"/>
  <!-- vaccinated: 2 -> 40px -->
  <rect x="240" y="160" width="60" height="40" fill="#1a1a1a"/>
  <text x="130" y="220" text-anchor="middle" font-family="Inter">Unvaccinated · 8</text>
  <text x="270" y="220" text-anchor="middle" font-family="Inter">Vaccinated · 2</text>
</svg>
```

Heights of 160 and 40 px give a 4:1 length ratio read on a common baseline — the relationship the data warrant, delivered to the eye without distortion. The structural claim now equals the explicit claim.

**The lesson.** *The data did not change; the channel did, and the channel is the message.*

**The limit.** Choosing "bars on a common baseline" required a human to classify the task as a magnitude comparison and to know that length beats area for that task. The tool generated valid SVG both times. It had no basis for preferring the second. That preference — the channel decision — is one of the at-least-two human judgments you would name in this figure's AI Use Disclosure. The second: the decision to drop the red/green encoding in favor of a single dark mark, because the comparison is fully carried by length and a second color would add visual weight without adding information.

## Reading Response #1 (30 pts)

**Deliverable.** Find one published infographic (news outlet, agency, journal, or company report) whose *data appears correct* but whose *form you suspect distorts the relationship*. In 600–900 words:

1. **State the explicit claim** (the headline or stated message) and the **structural claim** (what the encoding asserts pre-attentively). Name where they agree and where they diverge. *(10 pts)*
2. **Identify the encoding decision** responsible for the divergence — channel choice, axis truncation, scale, dual-axis, area-vs-length — by name, and explain the perceptual mechanism that makes it mislead, citing the relevant principle from this chapter. *(10 pts)*
3. **Render a verdict**: accurate, misleading, or indeterminate, with justification. If indeterminate, state exactly what information the figure withholds that prevents certification. *(5 pts)*
4. **AI Use Disclosure** *(5 pts).* If you used an AI tool to help locate, transcribe, or analyze the figure, name **at least two** judgments in your analysis that you made and the tool could not — e.g., deciding which claim was the *structural* one, or deciding that the verdict was "indeterminate" rather than "misleading." *Submissions without a completed disclosure lose 15 points per course policy.*

## Bridge

You can now name the disease, but not yet its cause. *Why* do these encoding errors mislead so reliably? Why is area read worse than length? Why does the eye believe the blob over the label? The answers are not matters of taste; they are facts about the cognitive architecture you and your readers are running on. Chapter 2 opens that architecture — dual coding, cognitive load, the channel hierarchy, Gestalt grouping — and turns "this feels off" into "this violates a measured perceptual constraint."

## Sources

- Cleveland, W. S., & McGill, R. (1984). *Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods.* Journal of the American Statistical Association. — Experimental ranking of visual channels; the basis for "length beats area." [High]
- Mackinlay, J. (1986). *Automating the Design of Graphical Presentations of Relational Information.* ACM Transactions on Graphics. — Matching data type and task to encoding; why a plausible chart can choose the wrong channel. [High]
- Borkin, M., et al. (2013). *What Makes a Visualization Memorable?* IEEE TVCG. — Memorability is distinct from comprehension. [High]
- Bateman, S., et al. (2010). *Useful Junk? The Effects of Visual Embellishment on Comprehension and Memorability of Charts.* CHI. — Meaningful vs. arbitrary embellishment; finding is genuine but contested on generalizability. [Contested]
- Tufte, E. (1983/2001). *The Visual Display of Quantitative Information.* Graphics Press. — The minimalist pole; useful as a foil for the Brutalist position developed in Chapter 3. [High]
