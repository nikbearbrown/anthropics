# Chapter 0 — How to Use the Simulations
*Before you read anything else, plot a mouse and an elephant.*

---

Here is a number worth thinking about before you open any other chapter: a 20-gram mouse burns about 185 kilocalories per kilogram of tissue per day just to stay alive. A 5,000-kilogram elephant burns about 8. Every gram of mouse tissue is running at roughly twenty-two times the metabolic rate of every gram of elephant tissue.

The cells are not doing different chemistry. They are doing broadly the same chemistry — the same citric acid cycle, the same oxidative phosphorylation, the same ATP synthase spinning at the inner mitochondrial membrane. What differs is the *rate*. And the rate is not arbitrary. It follows a pattern so regular you can predict it from one number: body mass. That prediction is what this chapter will put on your laptop screen.

The pattern is called Kleiber's law, and it is the deepest quantitative relationship in animal physiology. Before you read anything about circulation, respiration, osmoregulation, or endocrinology, you should understand it — not because it introduces those topics, but because it is the scale on which all comparative claims in this book live or die. Comparing a hummingbird to a whale without correcting for body size is comparing nonsense. Kleiber's law is the correction.

---

## The story behind the line

In 1932, a Swiss-trained animal scientist named Max Kleiber was sitting in his office at the University of California's Davis campus with a stack of metabolism measurements spanning five orders of magnitude in body mass. The smallest animal was a 150-gram rat; the largest was a 600-kilogram steer. Between them, on index cards: ring doves, hens, dogs, sheep, cows, women, and men — every measurement taken at rest, post-absorptive, at a thermoneutral temperature. The calories per day each animal's body burns just to keep itself running.

The textbook said these numbers should scale with surface area. The argument was geometric: an animal of linear size *L* has surface area proportional to *L²* and volume proportional to *L³*, so surface area scales as volume to the two-thirds power, and since heat loss must balance heat production, metabolic rate should scale as *M^(2/3)*. Max Rubner had derived this in 1883 from one species — dogs — and it had sat in physiology textbooks for forty-nine years on the strength of that single species.

Kleiber plotted his measurements on log-log paper. He did it because the equation he suspected — *BMR = a · M^b*, a power law — turns into a straight line if you take logarithms of both sides:

$$\log(BMR) = \log(a) + b \cdot \log(M)$$

On linear axes, a power law sweeps up in a curve. On log-log axes, it is a line whose slope is exactly the exponent *b*. He penciled in the points. He fit a line. The slope came out to 0.74.

Not 0.67. Not the textbook number. A larger value, halfway between 2/3 and 1. In a 1947 follow-up, Kleiber rounded the exponent to 3/4 — partly because 3/4 fit as well, partly because it is easier to compute on a slide rule than 0.74. The number stuck. Modern textbooks still call it Kleiber's 3/4 law, even though it is, at least partly, a slide-rule artifact.

What the line says, in plain English: bigger animals get to burn fewer calories per gram. The exponent being *less than 1* is the entire content of the result. If bigger animals were just little animals scaled up with the same per-cell metabolic rate, the exponent would be exactly 1 and the line on log-log paper would have slope 1. The observed slope of 0.75 means every tenfold increase in body mass produces only a 5.6-fold increase in total metabolic rate — not a tenfold increase. The missing factor goes to lower per-tissue rates in larger animals.

That is the engine of comparative physiology in one number.

---

## The arithmetic, done once

Take *BMR = 70 · M^{0.75}* kcal/day, with *M* in kilograms. These are the numbers for the mammalian/avian Kleiber line. Let us work through the mouse and the elephant.

**Mouse.** *M = 0.020 kg*. The calculation is:

$$BMR = 70 \cdot (0.020)^{0.75}$$

To compute $(0.020)^{0.75}$: take the natural log, multiply by 0.75, exponentiate.

$$0.75 \cdot \ln(0.020) = 0.75 \cdot (-3.912) = -2.934$$
$$e^{-2.934} \approx 0.0532$$

So $BMR_{mouse} \approx 70 \times 0.053 \approx 3.7$ kcal/day.

Mass-specific: $3.7 / 0.020 = 185$ kcal/(kg·day).

**Elephant.** *M = 5{,}000 kg*:

$$0.75 \cdot \ln(5000) = 0.75 \cdot 8.517 = 6.388$$
$$e^{6.388} \approx 594$$

$BMR_{elephant} \approx 70 \times 594 \approx 41{,}600$ kcal/day.

Mass-specific: $41{,}600 / 5{,}000 \approx 8.3$ kcal/(kg·day).

The ratio of mass-specific rates: $185 / 8.3 \approx 22$.

Total BMR rises from 3.7 to 41,600 kcal/day — an 11,000-fold increase across a 250,000-fold difference in body mass. Mass-specific BMR falls 22-fold. If you had expected total BMR to scale proportionally with mass (the naive assumption), you would have predicted a 250,000-fold increase. The actual increase is 11,000-fold. The discrepancy is what the 3/4 exponent encodes.

A shrew sits even further left on this line than the mouse. Its mass-specific metabolic rate is so high that its caloric reserves last fewer than twelve hours, which is why pygmy shrews must hunt and eat almost continuously around the clock — pausing for more than a few hours means starvation. A blue whale sits far to the right of the elephant; its per-gram metabolic rate is even lower. Both extremes obey the same equation.

![Log-log scatter plot of BMR (kcal/day) vs](images/00-how-to-use-the-simulations-fig-01.png)
*Figure 1.1 — Log-log scatter plot of BMR (kcal/day) vs*

---

## Why log-log axes and why it matters

A small digression on the arithmetic, because the visual intuition it creates is worth having permanently.

Any power law *Y = a · M^b* becomes a straight line on log-log axes. That is not a trick; it is a consequence of two logarithm identities:

$$\log(a \cdot b) = \log(a) + \log(b)$$
$$\log(x^n) = n \cdot \log(x)$$

Apply them to *Y = a · M^b*:

$$\log(Y) = \log(a) + b \cdot \log(M)$$

This is $y = c + b \cdot x$ — a straight line in the transformed coordinates $(\log M, \log Y)$, with slope *b* and intercept $\log(a)$.

The slope on a log-log plot *is* the exponent. A slope of 1 means *Y* scales proportionally with *M*. A slope of 0.75 means *Y* grows more slowly than *M*. A slope of 0 means *Y* is constant regardless of *M*. When you look at a log-log chart and eyeball the slope of a line, you are directly reading the allometric exponent. This is the visual skill the first simulation is designed to build.

The ectotherm offset — fish, reptiles, amphibians, and invertebrates sitting roughly an order of magnitude below the mammalian/avian line at any given body mass — appears as a vertical shift of the line, not a change in slope. Both lines have roughly the same slope (the same exponent), but different intercepts (different prefactors *a*). A mammal and a lizard of the same body mass obey the same scaling rule but at different metabolic levels, with the lizard burning roughly 1/17 as many calories per day. That factor is roughly the metabolic price of endothermy — the cost of running your own internal thermostat twenty-four hours a day.

---

## The three governing files

Before you write any code, you write three text files. They go in the same folder as the simulation. The LLM reads them every time you prompt it. This is the entire framework — three plain-text files, nothing installed.

**CLAUDE.md** tells the LLM what kind of code to produce.

```markdown
# CLAUDE.md — Animal Physiology Simulation Coding Constitution

## Stack
- Single .html file per simulation. No external build step.
- D3 v7 loaded from CDN: <script src="https://d3js.org/d3.v7.min.js"></script>
- Plain HTML, CSS, and JavaScript. No frameworks. No npm.

## Visualization
- All drawing happens inside one <svg> element.
- Use D3 selections, scales, and transitions.
- Scaling plots use d3.scaleLog on both axes when the relationship is
  a power law. Ticks at exact powers of 10 via .tickValues().
- Species points are <circle> elements bound to a data array
  of {name, mass, BMR, taxon} objects. Hover reveals species name.
- Regression line drawn as a single <path>; no least-squares fitting —
  sliders set the parameters directly.
- Animated transitions on parameter change: duration 250 ms.

## Layout
- Two panels stacked vertically — a main log-log scatter panel above
  a mass-specific BMR panel below, sharing the x-axis.
- SVG canvas 720 x 480 by default.

## Interaction
- Parameter controls are <input type="range"> sliders.
- A <div id="readout"> displays current values to two significant figures.
- Sliders update in real time via an `input` listener.
- A taxon-toggle row of checkboxes filters which taxa are plotted.

## Biology
- Variables in the code use biology names (M, BMR, a, b, taxon).
- A short comment at the top of every <script> block states the
  biological claim and its limits.

## Verification
- Every simulation includes a console.log block printing the result of
  one biology check the moment the file loads.
- The check is a one-line falsifiable claim.
```

**DESIGN.md** says nothing about biology — it says how things look.

```markdown
# DESIGN.md — Visual Constitution

## Color palette (taxon-coded)
- Mammals:        #c0392b   (warm red)
- Birds:          #e67e22   (orange)
- Fish:           #2980b9   (blue)
- Amphibians:     #27ae60   (green)
- Reptiles:       #7f8c1b   (olive)
- Invertebrates:  #8e44ad   (purple)
- Reference lines: dashed #adb5bd at 1 px

## Chart styling
- Log-log scatter background: white #ffffff.
- Regression line: near-black #1a1714 for all-taxa view.
- Axis labels: 12 px sans-serif. Title: 16 px.
- Grid lines: #e9ecef at 1 px on log scale at powers of 10.
- Point radius: 4 px. Hover state: 6 px with name label.

## Sliders
- 320 px wide. Labels above. Current value to the right.

## Layout
- SVG canvas: 720 px wide x 480 px tall.
- Margins: top 30, right 30, bottom 50, left 60.

## Type
- system-ui, -apple-system, sans-serif.
```

**PROJECT.md** is the only file you edit chapter to chapter.

```markdown
# PROJECT.md — Animal Physiology Simulation Workshop

## Built so far
- (chapter, file, what it models)

## In progress
- 00-allometric-scaling.html — log-log plot of BMR vs body mass,
  20+ species across six taxa, sliders for b and a.

## Next
- 01-body-plans.html

## Conventions
- File naming: NN-slug.html
- Each file is self-contained.
- Every file has a one-line // CLAIM: comment at the top.
```

| Item | Meaning |
| --- | --- |
| File / Controls / Does not control | CLAUDE.md governs code style, DESIGN.md governs appearance, PROJECT.md governs state |

---

## The four-move prompt

Most students paste vague requests into Claude — *"make me a Kleiber plot"* — and spend an hour fighting the output. The four-move structure skips that hour. It is not magic; it is specificity, organized.

**Show.** Point at the governing files. *"Read CLAUDE.md and DESIGN.md. Conform to them."* Attach them in claude.ai, or if you are in Claude Code they are already on disk.

**Say.** One paragraph in biological terms. What the chart shows. What the axes are. What the sliders control.

**Constrain.** The hard numbers beyond what CLAUDE.md already establishes. Slider ranges, color assignments, which species go in the data array, what the readout displays.

**Verify.** One falsifiable biology claim the simulation must satisfy. Not *"make sure it looks right"* — a statement that is either true or false when you read the console.

---

## A worked example

Here is the actual prompt for `00-allometric-scaling.html`:

> **Show:** Read CLAUDE.md and DESIGN.md from this project. Conform to them.
>
> **Say:** Build `00-allometric-scaling.html` — an allometric scaling visualizer. The main panel is a log-log scatter plot of basal metabolic rate (kcal/day, y-axis) against body mass (kg, x-axis) for twenty species across six taxa: mammals (pygmy shrew 0.003 kg, mouse 0.020 kg, rat 0.25 kg, rabbit 2.5 kg, dog 15 kg, human 70 kg, horse 500 kg, cow 600 kg, elephant 5000 kg), birds (hummingbird 0.003 kg, sparrow 0.020 kg, chicken 2.0 kg, eagle 5 kg, ostrich 100 kg), fish (trout 0.5 kg, tuna 200 kg), amphibians (frog 0.05 kg), reptiles (lizard 0.1 kg), invertebrates (honeybee 0.0001 kg, beetle 0.005 kg). Each species's BMR is computed at load time as *BMR = a_taxon · M^b*, with *a_taxon = 70* for endotherms (mammals, birds) and *a_taxon = 4* for ectotherms (fish, amphibians, reptiles, invertebrates). Sliders control *b* (0.5 to 1.0, default 0.75) and *a* (1 to 200, default 70). Two regression lines are drawn: endotherm at *(a, b)* and ectotherm at *(4, b)*. A second panel below plots mass-specific BMR = *a · M^(b−1)* on a shared x-axis.
>
> **Constrain:** Sliders — *b* (0.5 to 1.0, default 0.75), *a* (1 to 200, default 70). Point radius 4 px, colored by taxon per DESIGN.md. Taxon-toggle checkboxes. Use *d3.scaleLog* on all axes. x-axis ticks at exact powers of 10 from 10⁻⁴ to 10⁴ kg; y-axis ticks from 10⁻² to 10⁵ kcal/day. Readout shows current *a*, *b*, predicted BMR for a 20-g mouse, predicted BMR for a 5,000-kg elephant, and their mass-specific BMR ratio. Single self-contained HTML file. Add a comment at the top: `// CLAIM: BMR scales as a power law of body mass with exponent near 0.75 (Kleiber 1932); mass-specific BMR declines with mass at exponent (b−1); ectotherm BMR sits about an order of magnitude below the mammalian line.`
>
> **Verify:** Biology check — print to console on every parameter change: (1) with *a = 70, b = 0.75*, predicted BMR_mouse (M = 0.020 kg) must be within 5% of 3.7 kcal/day; (2) predicted BMR_elephant (M = 5,000 kg) must be within 5% of 41,600 kcal/day; (3) mass-specific ratio (mouse:elephant) must be within 10% of 22:1; (4) when *b = 1.0*, the mass-specific BMR curve in the lower panel must be horizontal.

Paste that. Wait. Save the file. Double-click it.

You should see twenty colored dots arranged in a rising band across the log-log axes. The mammals (warm red) sit along a line climbing at slope 0.75. The birds (orange) overlap them. The ectotherms — fish, amphibians, reptiles, invertebrates — sit on a roughly parallel line about an order of magnitude below.

Now drag *b* from 0.75 to 0.67 (Rubner's surface-law value). The regression line rotates clockwise around the point near 1 kg; the elephant ends up above the line, the shrew below it. The surface law misfits the extremes. That is the empirical content of Kleiber's 1932 paper, replicated in about thirty seconds on your laptop.

Drag *b* to 1.0 — isometric scaling. The line steepens. The lower panel goes flat: mass-specific BMR no longer depends on body size, every gram burning the same regardless of the animal's mass. This is the world the textbook assumed before Kleiber.

Open the developer console (Cmd-Option-J on Mac, Ctrl-Shift-J on Windows). With *b = 0.75* you should see:

```
[Verify] BMR_mouse: 3.7 kcal/day (target 3.7 ±5%) → PASS
[Verify] BMR_elephant: 41,600 kcal/day (target 41,600 ±5%) → PASS
[Verify] Mass-specific ratio (mouse:elephant): 22.4:1 (target 22 ±10%) → PASS
[Verify] b = 1.0 isometric check: lower panel slope = 0.00 → PASS
```

If any line reads FAIL — if the mouse comes back as 8 kcal/day or the elephant as 200,000 — push back at the LLM with the exact numbers: *"With a = 70 and b = 0.75, the simulation reports BMR_mouse = 8.0 kcal/day. Expected 3.7. Check that mass is in kilograms and not grams."* The verification clause turns vague dissatisfaction into a precise bug report.

---

## What this simulation gets wrong, and why that matters

The simulation is wrong about several things, and naming them is part of the method.

*The species BMR values are triangulated, not measured.* Each point's height on the chart comes from plugging that animal's mass into the Kleiber equation. Real measured values for individual species scatter around the line — sometimes by a factor of two in either direction. The shape of the plot will be right. Any individual height should be tagged `[verify]` against a canonical source before being cited. Schmidt-Nielsen's *Scaling: Why Is Animal Size So Important?* (Cambridge, 1984) has the measured data.

*The ectotherm offset is a single number, not a temperature function.* Real ectotherm metabolic rate depends strongly on body temperature — a cold lizard at 10°C burns far less than a warm one at 35°C. The simulation uses *a = 4* as a fixed ectotherm prefactor, which is approximately right at an intermediate temperature but wrong at the extremes. We will revisit this when endothermy is the topic.

*The exponent 0.75 is contested.* Kleiber rounded 0.74 to 0.75 in 1947 for slide-rule convenience. A century of subsequent measurements has produced estimates ranging from roughly 0.67 to over 0.8 depending on the dataset, the taxa included, and how the analysis corrects for phylogenetic relatedness. The West-Brown-Enquist fractal-network derivation (1997) gets to exactly 3/4 in the limit of infinite body size; White and Seymour (2003) argued the empirical data better support 2/3. Glazier (2022) catalogued 358 studies with significant deviations from 3/4. The simulation's slider runs from 0.5 to 1.0 precisely so you can drag the line and see what fits. The textbook value is a useful default, not a law of nature.

Three misconceptions worth naming explicitly.

*"Kleiber's law is a law of nature."* It is a robust empirical regularity. It is not derivable from first principles the way Newton's second law is. The best theoretical derivation (WBE 1997) makes assumptions about fractal vascular networks that hold approximately and in the infinite-size limit. The pattern is real; the explanation is contested; the exact exponent is partly a slide-rule artifact.

*"Big animals just have more cells doing the same thing."* If that were true, BMR would scale as *M^1*. Empirically it scales as roughly *M^{0.75}*, which means per-cell metabolic rate *declines* with body size. An elephant cell runs at roughly 1/22 the metabolic rate of a mouse cell. The same citric acid cycle, running at a lower rate. Why the rate falls with size is one of the genuinely open questions in comparative physiology.

*"Drug dose scales linearly with body weight."* The reason a chemotherapy dose is written as "200 mg per square meter of body surface area" rather than "3 mg per kilogram" is that clearance of many drugs scales with metabolic rate — roughly *M^{0.75}*, not *M^1*. Give a 25-gram mouse the per-kilogram dose that works for a 70-kg human and you overdose the mouse, because the mouse's metabolism processes the drug faster per unit tissue. The FDA's guidance for first-in-human dose extrapolation uses allometric scaling at *M^{0.67}* (the body-surface-area convention). The Kleiber line is the reason BSA-based dosing exists.

![Lower panel of the simulator ](images/00-how-to-use-the-simulations-fig-02.png)
*Figure 1.2 — Lower panel of the simulator *

---

## LLM Exercise — Build your allometric scaling simulator

Create the three governing files using the templates above. Save them in a folder. Then paste this prompt at Claude:

```
Show: Read CLAUDE.md and DESIGN.md from this project. Conform to them.

Say: Build 00-allometric-scaling.html — an allometric scaling
visualizer. The main panel is a log-log scatter plot of basal
metabolic rate (kcal/day, y-axis) against body mass (kg, x-axis)
for twenty species across six taxa:
  mammals: pygmy shrew 0.003 kg, mouse 0.020 kg, rat 0.25 kg,
           rabbit 2.5 kg, dog 15 kg, human 70 kg, horse 500 kg,
           cow 600 kg, elephant 5000 kg
  birds:   hummingbird 0.003 kg, sparrow 0.020 kg, chicken 2.0 kg,
           eagle 5 kg, ostrich 100 kg
  fish:    trout 0.5 kg, tuna 200 kg
  amphibians: frog 0.05 kg
  reptiles:   lizard 0.1 kg
  invertebrates: honeybee 0.0001 kg, beetle 0.005 kg

BMR for each species computed at load time as
  BMR_species = a_taxon * M^b
with a_taxon = 70 for mammals and birds, a_taxon = 4 for all others.
Sliders control b (0.5 to 1.0, default 0.75) and a (1 to 200,
default 70 — applies to the endotherm regression line; ectotherm
line drawn at a = 4 for reference). A second panel below plots
mass-specific BMR = a * M^(b - 1) on a shared x-axis. Readout
shows a, b, predicted BMR for a 20-g mouse, predicted BMR for a
5000-kg elephant, and mass-specific BMR ratio between them.

Constrain: Use d3.scaleLog on all axes. x-axis ticks at exact
powers of 10 from 1e-4 to 1e4 kg. Main y-axis ticks from 1e-2
to 1e5 kcal/day. Point radius 4 px, colored by taxon per
DESIGN.md. Hover shows species name as SVG label. Taxon-toggle
checkboxes. Single self-contained HTML file, no external
dependencies except d3 v7 from CDN. Comment at top:
// CLAIM: BMR scales as a power law of body mass with exponent
// near 0.75 (Kleiber 1932); mass-specific BMR declines at
// exponent (b - 1); ectotherm BMR is ~1 order of magnitude
// below the mammalian line at the same body mass.

Verify: Print to console on every parameter change:
  (1) with a = 70, b = 0.75: BMR_mouse (M = 0.020 kg) within
      5% of 3.7 kcal/day.
  (2) BMR_elephant (M = 5000 kg) within 5% of 41,600 kcal/day.
  (3) mass-specific ratio (mouse:elephant) within 10% of 22:1.
  (4) when b = 1.0: lower-panel curve is horizontal (slope
      within ±0.01 on log axes).
```

Once the file runs, work through these probes:

**The slope-by-eye test.** With *b = 0.75*, look at the mammalian regression line. When *M* increases by one decade (tenfold), the line should climb 0.75 decades on the y-axis. Drag *b* to 1.0 — it should climb one full decade. Drag *b* to 0.5 — half a decade. The slope on log-log axes *is* the exponent. This is the visual fact the chapter most wants you to hold.

**The fit-by-eye test.** Hold *a = 70* and drag *b* from 0.5 to 1.0 in steps of 0.05. At each value, notice how well the mammalian line fits the mammalian points. The fit visibly worsens as you move away from roughly 0.70–0.80, with the elephant ending above or below the line at the extremes. Where, by eye, does the fit look best? Compare your visual estimate to the textbook value of 0.75 and to White and Seymour's empirical claim of 2/3. What does the difference between 0.67 and 0.75 look like across five orders of magnitude?

**The ectotherm split.** Toggle the checkboxes to show only mammals. Then show only ectotherms. The two groups should sit on roughly parallel lines about an order of magnitude apart. That offset is the metabolic price of endothermy — every gram of mammalian tissue burns approximately seventeen times more energy per day than every gram of lizard tissue of the same mass, because the mammal is paying for internal temperature regulation continuously.

**The mass-specific panel.** With *b = 0.75*, the lower panel slopes downward — bigger animals burn less per gram. Drag *b* to 1.0: the panel goes flat. Every gram burns the same regardless of size; the naive "big animals are just lots of small animals" picture. Drag *b* to 2/3: the panel steepens — the surface-law world, where the per-gram difference between small and large animals is even greater. The lower panel is where the slope difference between 2/3 and 3/4 matters for drug dosing: it is the gap that determines how much you should scale a dose between species.

**Extension prompt.** Once the basic simulator works, add a drug-dose calculator:

```
Extension: Modify 00-allometric-scaling.html to add a drug-dose
calculator in the readout. Two input fields: reference body mass
(kg) and reference dose (mg). Two output fields: (1) per-kg
linear dose = reference_dose * target_mass / reference_mass;
(2) allometric dose = reference_dose * (target_mass /
reference_mass)^b, using the current b slider value. A slider
for target body mass (0.001 to 1000 kg, default 15 kg).

Verification: with reference = 70 kg / 100 mg, target = 15 kg,
b = 0.75: linear dose = 21.4 mg, allometric dose = 31.7 mg.
With b = 1.0: both doses equal. With b = 0.67: allometric
dose = 34.0 mg.
```

This extension turns the chart into a clinical-pharmacology object. The same equation that explains why a mouse must eat constantly is why a pediatric drug label uses surface-area dosing rather than per-kilogram dosing.

---

Chapter 1 asks the broader question this chapter deferred: how does body *plan* — radial versus bilateral, segmented versus vertebrate — constrain which physiological solutions are possible? Body size is one constraint. Body plan is the other. Together they determine which point on the Kleiber line a given organism can reach and which physiological strategies it has to evolve to live there. Carry the simulator with you. The first time the next chapter compares a flatworm to a whale, pull up `00-allometric-scaling.html` and see that the comparison is already half-quantified.

---

**What would change my mind.** If a large modern dataset of mammalian BMR — corrected for body temperature, phylogenetic non-independence, and activity state — yielded an exponent varying effectively at random across taxonomic orders rather than clustering near 0.75, the Kleiber line would lose its status as a useful average, and this chapter would have to lead with the heterogeneity rather than the regularity. Glazier 2022 (*Proc R Soc B*) catalogued 358 studies finding significant deviations from 3/4 and only 22 supporting it universally — enough to demote 3/4 from law to useful average. The simulation's pedagogical move (drag the slider, see what fits) would survive that revision. The textbook number would not.

**Still puzzling.** I do not understand why exactly 3/4 rather than 0.7 or 0.8. The West-Brown-Enquist fractal-network derivation produces 3/4 in the limit of infinite body size, but the curvature it predicts for finite organisms has been used both to defend and attack the model. I also do not know whether the right framing for the ectotherm-endotherm offset is "two parallel Kleiber lines" or "one line with a temperature-dependent prefactor *a(T)*" — and that question probably matters for how Chapter 12 will treat endothermy. Both are genuinely open.

---

**Tags:** allometric-scaling, Kleibers-law, mass-specific-BMR, D3-v7-log-log, Brutalist-files
