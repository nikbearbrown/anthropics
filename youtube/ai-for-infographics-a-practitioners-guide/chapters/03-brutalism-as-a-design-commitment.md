# Chapter 3 — Brutalism as a Design Commitment

## A building and a chart, side by side

Look at a photograph of a Brutalist building — say, a poured-concrete university library from the 1960s. The first reaction is often discomfort. There is no cladding. The concrete is bare, board-marks from the formwork still visible. You can see where the floor slabs meet the columns, where the stairwell rises, where the structure carries its load. Nothing is hidden behind a polite skin. The building shows you how it stands up.

Now put beside it an AI/ML performance chart built the same way. A small-multiples grid of model benchmarks: no gradient fills, no drop shadows, no rounded glossy bars, no decorative background. Bars on a common baseline in a single ink. Direct labels on the marks. A visible structure — you can see the axis, the baseline, the grid of comparisons — and nothing on the canvas that is not encoding a number or guiding the eye to one. It too can read as severe at first. And it too is showing you exactly how it stands up: which model beats which, by how much, with no surface ornament borrowing authority it did not earn.

The parallel is not a metaphor reached for after the fact. It is structural, and it names the three commitments this chapter is about. *Exposed concrete* is *exposed data structure* — the figure shows its construction rather than concealing it. *No ornament* is *no non-encoding marks* — nothing on the canvas that does not carry information or direct attention. *Honest material* is *honest channel selection* — the figure uses each channel for what it actually communicates accurately, the way concrete is used in compression where concrete is strong.

Here is the claim this chapter defends, and it is the one most readers will resist: **Brutalism in infographic design is not a style. It is a set of commitments that fall out, almost deductively, from the perceptual science of Chapter 2.** Every Brutalist rule traces back to a measured constraint. When you remove a drop shadow, you are not expressing a taste; you are deleting extraneous cognitive load. When you put bars on a common baseline, you are not being austere; you are climbing the Cleveland–McGill hierarchy. The aesthetic is a *consequence*. Confuse it for a cause and you will imitate the surface while violating the substance — which, as we will see, is exactly the failure mode generative tools make easy.

## Three commitments, and the science under each

**Exposed structure.** A Brutalist figure makes its organizing structure visible rather than smoothing it into a seamless picture. The axis is present. The baseline is present. The grouping that the data actually has is the grouping the reader sees. This is Gestalt honesty: because the visual system groups pre-attentively (Chapter 2), the perceived structure *will* be read as the claimed structure whether you intend it or not. Exposing the true structure means the automatic grouping the reader performs lands on the real organization of the data instead of on an artifact of layout. A figure that hides its structure does not become neutral; it becomes a figure whose structural claim you no longer control.

**Functional marks.** Every mark on the canvas must do a job: encode a value, label an encoding, or direct attention to one. A mark that does none of these is, by definition, extraneous cognitive load (Sweller) — it consumes the reader's scarce working-memory capacity and returns nothing [High]. This is the commitment most often mistaken for "minimalism," and the difference is the whole subject of the next section. The Brutalist does not remove marks because fewer is prettier. The Brutalist removes a mark when it cannot state the mark's job. The test is functional, not quantitative: a dense figure full of working marks is more Brutalist than a sparse one carrying a single decorative flourish.

**Honest hierarchy.** The visual prominence of an element must match its informational importance. The headline claim should be the most prominent thing; the primary encoding next; supporting annotation below that; the source line quiet at the bottom. When prominence and importance diverge — when a gridline shouts as loud as the data, or the decorative element outweighs the claim — the figure's hierarchy lies. This is dual coding and load theory together: the reader's attention is allocated by visual weight, pre-attentively, so misallocated weight wastes the reader's first and most valuable glance on the wrong thing.

State all three as one sentence and you have the Brutalist commitment: *show the real structure, let every mark do a job, and make weight track importance.* Each clause is a perceptual constraint wearing work clothes.

This is precisely where generative tools create a new hazard, and it is worth naming sharply because it is the failure this chapter is built to prevent. A code generator can imitate a *surface* with ease — ask for "a Brutalist infographic" and it will give you bare type, heavy rules, a monospace font, a stark palette. It has seen the look. What it cannot do is preserve the *commitments under* the look, because the commitments are not visual features — they are relationships between the figure's marks and the figure's meaning, and meaning is the thing the generator does not have. A figure can wear every surface signature of Brutalism — the bare concrete aesthetic — while violating all three commitments: hiding its true structure behind a stylish but arbitrary grid, carrying decorative monospace labels that encode nothing, and allocating heavy visual weight to an unimportant element because heaviness "looks Brutalist." That figure is Brutalist cosplay. It has the costume and none of the discipline. The whole point of treating Brutalism as commitment rather than style is that commitment survives the translation into a specification a generator can execute against; style does not. When you write `DESIGN.md` in Act Two, you are encoding the commitments, not the costume — which is exactly why the generator can then execute them faithfully.

## The hard part: meaningful embellishment versus arbitrary decoration

The commitment to functional marks runs straight into the most contested result in the field, and a careless reading of it can wreck a designer. So we handle it carefully.

The naïve Brutalist says: all embellishment is load, therefore strip everything to the data. That is overcorrection, and it collides with Bateman et al.'s *Useful Junk?* (2010). Their finding, stated precisely: chart embellishment that was *semantically meaningful* — imagery genuinely related to the chart's subject — improved long-term recall of the chart's content, without reliably degrading comprehension accuracy in their experiment [Contested]. Plainly: a chart about shrinking forests, decorated with imagery of trees, was remembered better than the plain bars, and readers still answered questions about it correctly.

This is real, and it is widely *mis*used as "decoration is fine, even good." It is not that. Three disciplines keep it honest:

1. **Meaningful, not arbitrary.** The embellishment in the study *referred to the subject*. Trees on a forest chart carry semantic content; a random gradient or a glossy 3-D bevel carries none. The finding licenses *semantically meaningful* imagery, never arbitrary visual noise. Arbitrary decoration remains pure extraneous load with no recall payoff [Medium].
2. **Memorability is not comprehension.** The benefit measured was *recall* (Chapter 1's distinction returns). If your figure's job is precise quantitative comparison in the moment, a recall benefit a week later is irrelevant and the comprehension cost — if any — is what matters [High].
3. **The result is contested.** Small sample, particular charts, specific tasks; replications and critiques question how far it generalizes [Contested]. You do not build a practice on a contested result. You build a practice on the robust core — functional marks — and treat meaningful embellishment as a *narrow, justified exception* that must earn its place by naming the recall job it does.

So the Brutalist position is not anti-ornament by reflex. It is: *a mark earns its place by doing a job; "be memorable to a relevant audience" can be a job; "fill space" and "look serious" cannot.* This is a sharper, more defensible line than minimalism's "less ink is more," and it is the line that separates this book from both poles of the old debate.

## Why Brutalism is neither Tufte nor Holmes

Two figures anchor the historical poles, and naming the difference clarifies the Brutalist position.

**Edward Tufte** is the minimalist pole. His "data-ink ratio" prescribes maximizing the proportion of ink that encodes data and erasing the rest [High]. Tufte and Brutalism agree enormously — both despise non-functional marks — and a Tufte sparkline is nearly a Brutalist object. But Tufte's principle is *quantitative* (minimize non-data ink), while Brutalism's is *functional* (every mark does a job). The gap matters at the edges: a label that directs attention, a region that encloses a meaningful group, or a semantically meaningful image carries no *data* yet does a real *job*. Tufte's reflex deletes it; Brutalism keeps it if it can name the job. Brutalism is not minimalism; it is functionalism, which sometimes keeps what minimalism throws away.

**Nigel Holmes** is the explanatory-illustration pole — the *Time* magazine tradition of charts wrapped in vivid, often figurative imagery designed to engage and to stick [High]. Holmes is frequently cast as Tufte's opposite. The Brutalist reading is more generous and more precise: Holmes's *best* work is exactly Bateman's "meaningful embellishment" — imagery that refers to the subject and aids recall. His *worst* imitators produce arbitrary decoration that borrows his energy without his discipline. Brutalism does not reject Holmes; it extracts the rule Holmes followed intuitively (embellishment must be *about* the subject) and discards the part that does not survive the functional test.

> **AI Wayback Machine — Alison Smithson (1928–1993)**
>
> The British architect Alison Smithson, with her partner Peter Smithson, is widely credited with giving Brutalism its name — the term "the New Brutalism" appears in their orbit in the early 1950s — and, in buildings like the Hunstanton School (1954), they insisted that a building should display its materials and structure honestly rather than disguise them [High]. (The critic Reyner Banham became the movement's principal *theorist*, and his account and the Smithsons' own did not always agree — a wrinkle worth knowing but not load-bearing here.) Their principle, often quoted as the demand that a building's structure and services be *legible* — that you can read how it works from how it looks — is the architectural ancestor of this chapter's "exposed structure" commitment.
>
> The transfer to infographics is exact. Hunstanton ran its steel and its ductwork in the open; a Brutalist infographic runs its axis, baseline, and grouping in the open. The Smithsons were reacting against decorative facades that concealed how a building stood — the same reaction a Brutalist figure makes against gradients and shadows that conceal how a claim is constructed. *Prompt to try: "Explain how Alison Smithson's principle of legible structure helps an engineer avoid a polished but indefensible infographic."*
>
> A note on lineage: Reyner Banham's *The New Brutalism* (1966) is the standard secondary source for these claims; verify the Hunstanton date and the exact wording of the Smithsons' coinage against it before final publication [verify].

## The blur test: a practical instrument

Theory has to become a check you can run in ten seconds, and the Brutalist instrument is the **blur test**. Take the figure, blur it heavily — squint, defocus, or apply a strong Gaussian blur in software — until fine detail vanishes and only large shapes and weights remain. Then ask: *what survives?*

In an honest hierarchy, three things should survive the blur, in order of prominence: the **headline claim**, the **main visual** (the primary encoding), and the **primary annotation** (the one note that carries the interpretation). If those three emerge as a clear visual hierarchy when everything else has dissolved, the figure allocates the reader's first pre-attentive glance correctly. If a gridline, a legend, or a decorative element survives the blur as loudly as the data, the hierarchy is dishonest — weight is not tracking importance.

The blur test works because it simulates exactly what the visual system does in its first fraction of a second: it strips detail and reads gross structure and weight (Chapter 2's pre-attentive processing). Passing the blur test is operational proof of honest hierarchy. You will use it in Chapter 9 to verify annotation and in Chapter 15 as part of the final review. Run it now, on the corrected bar chart from Chapter 1: blurred, the tall bar, the short bar, and the headline survive; nothing else competes. It passes.

![Two panels of the same chart: a sharp version with headline, bars, annotation, faint gridlines and a decorative star, and a heavily blurred version in which only the headline, the dominant bar, and the one annotation survive while the gridlines and star dissolve.](images/03-brutalism-as-a-design-commitment-fig-01.png)

*Figure 3.1 — The blur test: in an honest hierarchy only the headline, main visual, and primary annotation survive a heavy blur; gridlines and decoration vanish, so the figure passes.*

## Worked example: an ML-benchmark figure made Brutalist-consistent

**Problem statement.** You need a figure showing four language models' accuracy on a benchmark: 71%, 74%, 88%, 91% [verify — illustrative; substitute real cited benchmark numbers].

**First attempt (AI, unspecified).** A bar chart with a vertical gradient fill, soft drop shadows under each bar, rounded bar tops, a textured background, a y-axis that starts at 70. It looks like a product slide.

**Design diagnosis — by commitment.**
- *Honest hierarchy violated:* the y-axis starting at 70 turns a 20-point spread into a visual chasm; weight (apparent bar-height ratio) does not track the true importance (the real differences). The structural claim exaggerates.
- *Functional marks violated:* gradient, shadow, rounding, and texture are four mark-classes doing no encoding job — pure extraneous load [High]. None refers to the subject, so even the Bateman exception does not apply.
- *Exposed structure obscured:* the textured background and shadows blur the baseline, so the structure the reader needs to see is muddied.

**Corrected version.** Single dark ink, flat fill, square corners, no shadow, no texture. Baseline at zero (the honest origin for accuracy bars). Direct value labels on each bar. The result, in SVG skeleton:

```svg
<svg viewBox="0 0 480 300" xmlns="http://www.w3.org/2000/svg">
  <line x1="60" y1="260" x2="460" y2="260" stroke="#1a1a1a" stroke-width="2"/>
  <!-- zero-origin scale: 0–100% over 220px -->
  <rect x="80"  y="103" width="60" height="157" fill="#1a1a1a"/> <!-- 71% -->
  <rect x="180" y="97"  width="60" height="163" fill="#1a1a1a"/> <!-- 74% -->
  <rect x="280" y="66"  width="60" height="194" fill="#1a1a1a"/> <!-- 88% -->
  <rect x="380" y="60"  width="60" height="200" fill="#1a1a1a"/> <!-- 91% -->
  <text x="110" y="95"  text-anchor="middle" font-family="JetBrains Mono">71</text>
  <text x="210" y="89"  text-anchor="middle" font-family="JetBrains Mono">74</text>
  <text x="310" y="58"  text-anchor="middle" font-family="JetBrains Mono">88</text>
  <text x="410" y="52"  text-anchor="middle" font-family="JetBrains Mono">91</text>
</svg>
```

Blur it: four bars of honestly proportioned height and a clear tallest survive. It passes.

**The lesson.** *Strip every mark that cannot state its job, set the honest origin, and the figure's hierarchy stops lying.*

**The limit.** Two judgments here no tool supplies. First, the decision that accuracy bars take a *zero origin* — a human call about what baseline makes the comparison honest for this metric (a different metric, like a change-from-baseline, might warrant a different origin). Second, the decision that *no embellishment is warranted* because this audience needs in-the-moment comparison, not week-later recall — a Bateman judgment the tool cannot make because it cannot read the audience or the use. Those two are this figure's AI Use Disclosure.

## Reading Response #2 (30 pts)

**Deliverable.** In 600–900 words, take one infographic and argue whether it is **Brutalist-consistent or Brutalist-violating**, using the commitments as a rubric — not as a vibe.

1. **Test each commitment** *(12 pts).* For *exposed structure*, *functional marks*, and *honest hierarchy* in turn, state whether the figure honors or violates it, with the specific mark or decision as evidence. For at least one mark, state its *job* — or state that it has none.
2. **Run the blur test** *(8 pts).* Describe (or show) what survives a heavy blur. Name whether the surviving elements form an honest hierarchy (headline → main visual → primary annotation) and what, if anything, survives that should not.
3. **Adjudicate one embellishment** *(5 pts).* Identify one embellished or decorative element and classify it as *semantically meaningful* (Bateman-defensible, with the recall job named) or *arbitrary* (extraneous load). Cite the relevant principle and tag your confidence.
4. **AI Use Disclosure** *(5 pts).* Name **at least two** judgments in your analysis that required human reasoning a tool could not supply — e.g., deciding whether an embellishment *refers to the subject*, or deciding what the figure's honest *origin* should be. *Missing disclosure: −15 per policy.*

## Bridge

You now hold a design philosophy that is really a science in work clothes: three commitments, each traceable to a measured constraint, plus an instrument — the blur test — to check them. But a philosophy needs a *medium*. These commitments have to be expressed in a real file that a browser renders, a code generator writes, and a designer edits. And it turns out SVG means three different things to those three audiences. Chapter 4 introduces SVG as a design medium, with all three in view — because the gap between "looks right in the browser" and "editable in production" is where the next set of failures lives.

## Sources

- Bateman, S., et al. (2010). *Useful Junk? The Effects of Visual Embellishment on Comprehension and Memorability of Charts.* CHI. — The meaningful-embellishment finding; genuine but contested on generalizability. [Contested]
- Tufte, E. (1983/2001). *The Visual Display of Quantitative Information.* Graphics Press. — The data-ink ratio and the minimalist pole; the foil against which Brutalism defines its functionalism. [High]
- Holmes, N. (1984). *Designer's Guide to Creating Charts and Diagrams.* Watson-Guptill. — The explanatory-illustration tradition; source of the "embellishment about the subject" intuition. [High]
- Ware, C. (2020). *Information Visualization: Perception for Design* (4th ed.). Morgan Kaufmann. — Bridges perceptual science to applied design; supports the attention-and-hierarchy claims. [High]
- Banham, R. (1966). *The New Brutalism: Ethic or Aesthetic?* — Standard secondary source for the Smithsons and the architectural commitments; verify dates and quotations before final publication. [verify]
