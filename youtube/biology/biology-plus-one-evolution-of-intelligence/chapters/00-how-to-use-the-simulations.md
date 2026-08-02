# Chapter 00 — How to Use the Simulations

*Before any animal has been named, here is the whole machine.*

---

## Prerequisites

A laptop with a text editor and a browser. An account on claude.ai or any
comparable LLM. The ability to double-click an HTML file. No prior coding.
No prior neuroscience. The only equation you need to hold is one subtraction
divided by one number, repeated.

---

## What is actually going on

I want to start with a bacterium. Not because bacteria are simple — they are
not, not really — but because *E. coli* is the clearest place I know to watch
the machinery work before anyone has attached the word *intelligence* to it and
confused the issue.

Howard Berg spent most of the 1970s and early 1980s figuring out exactly how
*E. coli* finds food. The cell is about two micrometers long. It has a fuzz of
flagella at one end — little rotary motors that can spin clockwise or
counterclockwise. When they spin together counterclockwise, they bundle into a
helix and the cell swims in a straight line. When the motors switch direction,
the bundle flies apart and the cell tumbles randomly in place, then reforms and
sets off in a new direction. Run, tumble, run, tumble. Filmed from above, the
trajectory looks like a drunk walking — short straight segments connected by
random turns.

And yet, if there is a source of aspartate somewhere in the water — a sugar the
bacterium likes — the trajectory is not a random walk. It is a *biased* random
walk. The straight runs are longer when the cell is moving toward the source,
shorter when moving away. The net result is drift up the gradient. The cell
finds the food.

<!-- → [IMAGE: Berg-style tracking diagram showing two E. coli trajectories side by side — left panel: unbiased run-tumble random walk in uniform medium (roughly equal run lengths in all directions); right panel: biased random walk up a concentration gradient (longer runs toward source, shorter runs away); source marked with a dot at upper right; caption should note the key observation that run lengths, not turning frequency, are what change] -->

The question Berg and his collaborators were asking — and it is the question
this entire book is organized around — is: *how?* The cell has no brain. It has
no neurons. It cannot see the gradient. It cannot smell the gradient in the way
we use that word. At any instant it knows only the local concentration at the
point it currently occupies. A single number. And from a single number you
cannot infer direction. You cannot tell, from the fact that the concentration
here is 0.40, whether the source is to the left or to the right. You need at
least two measurements, separated in time or space, to get a direction.

So how does the cell get the second measurement?

The answer came from Segall, Block, and Berg in 1986. It is elegant enough that
I want to give you the whole thing, because the elegance is the point. The cell
has receptors on its surface that bind aspartate. Those receptors have a second
state: they can be *methylated* — a small chemical tag attached by an enzyme
called CheR, removed by an enzyme called CheB. The methylation state is not
updated instantaneously. It lags. When the current receptor signal changes, the
methylation state takes a few seconds to catch up. Which means the methylation
state is, at any moment, a record of what the receptors were doing a few seconds
ago.

The cell compares the current receptor signal to the methylation-encoded memory
of the recent past. The difference — *current concentration minus past
concentration, divided by the time elapsed* — is the temporal derivative, what
a physicist would write as *dC/dt*. When *dC/dt* is positive, things are
getting better: keep running. When *dC/dt* is negative, things are getting
worse: tumble, randomize direction, try again.

That is everything. The navigation algorithm of *E. coli* is one comparison and
one rule.

Let me write it out so the structure is clear:

1. **Sense.** Receptors bind aspartate and generate a signal proportional to
   local concentration.
2. **Remember.** Methylation marks record what the receptors were doing a few
   seconds ago.
3. **Integrate.** Compute *dC/dt* — the difference between now and the
   remembered past, divided by elapsed time.
4. **Respond variably.** When *dC/dt* is above a threshold, run; when below,
   tumble.

<!-- → [INFOGRAPHIC: four-box horizontal flow diagram labeled Sense → Remember → Integrate → Respond variably; each box contains a one-line biological instantiation (receptor binding / methylation state / dC/dt computation / flagellar motor switching); a fifth box off to the side labeled "Thermostat" showing only Sense → Respond, with the Remember and Integrate boxes greyed out — to illustrate what is missing below the cognitive floor] -->

Four ingredients. That is the cognitive floor — the minimum architecture that
converts a passive sensor into a navigator.

---

## Why I call it a floor

The word *floor* does some work here that I should be honest about. I am not
calling it a floor to be polite about bacteria, or to suggest that everything
above it is an elaboration of the same basic thing. I am calling it a floor
because it is the threshold below which no system achieves what Legg and Hutter
in 2007 meant by *intelligence*: the ability to achieve goals in a varying
environment. Below the floor, you have reflex. A system that senses and
responds without memory or comparison is not navigating — it is flinching. The
thermostat is the canonical example. It senses temperature and responds, but it
does not compare *now* to *a moment ago*; it compares *now* to a fixed
setpoint. That is a different operation. The thermostat cannot find the source.
It can only be near it or not.

The floor matters because of what it tells you about the elaboration above it.
Every animal in this book — the honeybee, the octopus, the corvid, the
chimpanzee — uses these four ingredients and more. Not instead of them. *More.*
The mushroom body of the bee that learns to associate a color with sugar is the
integration step, enormously elaborated. The prefrontal cortex of the
chimpanzee that models what a researcher is thinking is the memory step,
enormously elaborated. When you watch the gradient-detection simulator work in
this chapter, you are watching the skeleton on which everything else in the book
is built.

<!-- → [TABLE: four-column table mapping organism (E. coli / Honeybee / Corvid / Chimpanzee / LLM) against the four cognitive-floor ingredients (Sense / Remember / Integrate / Respond variably) — each cell names the biological or computational substrate that implements that ingredient in that organism; LLM row should show token input / context window+weights / forward pass / sampling, with a question mark or "under investigation" indicator to flag that the analogy is unverified — this table is the architecture the book will trace for fourteen chapters] -->

A large language model also has these four ingredients — in some sense. It
senses (tokens in), it has memory (a context window plus weights trained on
billions of examples), it integrates (the forward pass), it responds variably
(sampling from a probability distribution). Whether the analogy is illuminating
or a category mistake is the exact empirical question the Skeptic's Notebook is
designed to answer across fourteen chapters. I do not know the answer yet. I
am writing the question into the book's structure so you can measure it
systematically rather than impressionistically.

---

## What we are building

Three things.

**First: three governing files.** CLAUDE.md tells the LLM how to write code for
this simulation series. DESIGN.md tells it how the result should look. PROJECT.md
tracks what has been built, what is in progress, and — most importantly — which
AI system you are putting under the lens for the whole semester. These files are
what I call *Brutalist*: plain text, no frameworks, nothing to install. You
write them once. Every subsequent prompt in every subsequent chapter points at
them. The LLM reads them and conforms to them.

<!-- → [INFOGRAPHIC: simple directory tree diagram showing a project folder containing three files (CLAUDE.md, DESIGN.md, PROJECT.md) with a right-pointing arrow from each file to the label "Every prompt in every chapter" — visually reinforces that the governing files are stable infrastructure, not per-chapter work; style should be minimal, monospace, dark mode consistent with DESIGN.md palette] -->

**Second: a four-move prompt structure.** The structure is Show / Say / Constrain /
Verify. Show the LLM the files it must conform to. Say what you want in one
paragraph of cognitive-biology terms. Constrain how it must be built — D3 v7,
single HTML file, specific slider ranges. Verify by giving it a falsifiable
biology question the simulation must pass. Four moves, used together, are
dramatically more reliable than any single move alone. The reason is simple: the
Verify move is the only one that tells you whether the simulation is biologically
correct, not just syntactically valid. Code that runs is not the same as code
that is right.

**Third: one simulation.** `00-cognitive-floor.html`. A single particle in a
one-dimensional chemical field, computing *dC/dt* over a short memory window,
biasing its tumble probability accordingly. You will watch the drift toward the
source appear when memory is on, and vanish when memory is set to zero. That
disappearance is the point. It is the CheR/CheB knockout experiment, run in
your browser, and it is the move this book will repeat fourteen times: identify
the ingredient, remove it, observe what breaks.

---

## The three files

### CLAUDE.md

```markdown
# CLAUDE.md — Comparative Cognition Simulation Coding Constitution

## Stack
- Single .html file per simulation. No external build step.
- D3 v7 loaded from CDN:
  <script src="https://d3js.org/d3.v7.min.js"></script>
- Plain HTML, CSS, and JavaScript. No frameworks. No npm.

## Visualization
- All drawing happens inside one <svg> element.
- Use D3 selections, scales, and transitions.
- Particle animations use <circle> elements bound to a data
  array, updated each frame via d3.timer. Particle positions
  live in the data array; the DOM is updated by re-selecting
  and setting cx/cy.
- Gradient fields are rendered as a horizontal color ramp using
  d3.scaleSequential and a chosen interpolator; the field is
  drawn once and updated only on parameter change.
- Time-series charts use d3.scaleLinear, d3.line,
  d3.axisBottom/Left.
- Animated transitions on parameter change: 250 ms.

## Layout
- Default is two panels stacked vertically — an organism /
  field panel above a time-series chart below, sharing a
  common time axis where applicable.
- SVG canvas 720 x 400 by default; field panel 720 x 220,
  chart panel 720 x 180, with a 10 px gap.

## Interaction
- Parameter controls are <input type="range"> sliders.
- A <div id="readout"> displays current parameter values to
  two significant figures and the running biology check.
- Sliders update the simulation in real time via an `input`
  listener.

## Cognitive-system rendering
- Every simulation models a named cognitive operation.
- Variables in code use cognitive-biology names — C (current
  concentration), C_mem (memory of past concentration),
  dC_dt (temporal derivative), tumble_prob, memory_window,
  response_threshold — not generic ones like x and y.

## Cognitive comments
- A short comment at the top of every <script> block states
  the cognitive claim the simulation is making and its limits.

## Verification
- Every simulation includes a console.log block that prints
  the result of one biology check the moment the file loads
  and on every parameter change.
- The biology check is a one-line falsifiable claim — e.g.,
  "when memory_window = 0, the particle's net drift toward
  the source must drop to zero within one standard deviation
  of an unbiased random walk."
```

### DESIGN.md

```markdown
# DESIGN.md — Visual Constitution
# Evolution of Intelligence Simulation Series

## Species palette (phylogenetic-coded)
- Bacteria / simple organisms:   #f4a261  (warm yellow)
- Invertebrates (worms, insects): #52b788  (green)
- Fish / early vertebrates:       #4895ef  (blue)
- Birds / corvids:                #e76f51  (orange)
- Mammals (non-primate):          #9d4edd  (violet)
- Primates:                       #480ca8  (deep purple)
- Humans:                         #1a1a2e  (dark blue)
- AI systems:                     #6c757d  (gray, dashed border)

## Valence palette
- Positive valence / approach:    #40916c  (green)
- Negative valence / avoid:       #d62828  (red)
- Uncertain / equivocal:          #f77f00  (amber)

## Field rendering
- Chemical-gradient color ramp: d3.interpolateYlOrBr from
  light cream (low concentration) to deep brown (high).
- Membrane / barrier lines: #2c3e50 at 2 px.

## Chart styling
- Dark mode: background #1a1a1a; default line and axis
  color #f8f9fa.
- Reference / threshold dashed line: #adb5bd at 1 px.
- Axis labels: 12 px sans-serif. Title: 16 px.
- Grid lines: #2a2a2a at 1 px.

## Sliders
- 320 px wide. Labels above, current value to the right.

## Layout
- SVG canvas 720 x 400 by default. Margins: top 30, right 30,
  bottom 50, left 60.

## Type
- system-ui, -apple-system, sans-serif.
```

### PROJECT.md

```markdown
# PROJECT.md — Evolution of Intelligence Simulation Workshop

## Target AI system under test
- [Name, version, vendor, model-card URL, knowledge cutoff]

## Definitions selected
- Working instrument (primary): Legg & Hutter (2007)
- Comparative lenses: Binet (1905), Wechsler (1944),
  Chollet (2019)

## Notebook entries completed
- Entry 0 — Four-definition verdict matrix (Ch 00)

## Built so far
- (chapter, file, what it models)

## In progress
- 00-cognitive-floor.html — gradient detection +
  memory window + threshold response

## Next
- 01-definition-sieve.html — apply each of six definitions
  to a panel of organisms, show what each sieve includes
  and excludes.

## Conventions
- File naming: NN-slug.html, where NN is chapter number.
- Each file is self-contained (no shared JS).
- Every file has a one-line // CLAIM: comment at the top.
```

The only file you actually edit chapter by chapter is PROJECT.md. CLAUDE.md and
DESIGN.md are constitutions — you write them once, and the fact that they never
change is what makes them useful.

---

## The four-move prompt

Most students paste something like *"make me a chemotaxis simulator"* and spend
an hour fighting the output. The four-move structure skips that hour.

**Show** — point at the files. *"Read CLAUDE.md and DESIGN.md."*

**Say** — one paragraph in cognitive-biology terms. Not "make a particle that
moves" but "a particle senses local concentration, stores a short memory of past
concentration, computes *dC/dt*, and biases its tumble probability accordingly."
The language of the claim is the language of the code you want.

**Constrain** — the rules beyond what CLAUDE.md already covers. Slider ranges.
The specific memory-buffer behavior. Which color on which side. The LLM already
knows to write D3 v7 in a single HTML file; the Constrain move handles
everything specific to this simulation.

**Verify** — one falsifiable biology check the output must pass. This is the
most important move. *"When memory_window is set to zero, the particle's net
drift toward the source must drop to within one standard error of an unbiased
random walk."* If the simulation passes syntax but fails the check, the
simulation is wrong. Code that runs is not the same as code that is right.

<!-- → [INFOGRAPHIC: four-step horizontal prompt flow — Show (icon: document) → Say (icon: speech bubble with molecule) → Constrain (icon: slider / parameter knob) → Verify (icon: checkmark over a biology diagram); below each step, a one-line example of what that move looks like for this specific simulation; the Verify step should be visually heavier or bolder — it is the most important move and the one students most often skip] -->

---

## The worked prompt

Here is the full prompt as you would actually paste it. Read it once for shape,
then I will walk through what each piece does.

> **Show:** Read CLAUDE.md and DESIGN.md from this project. Conform to them. The
> particle color is bacteria warm yellow `#f4a261`.
>
> **Say:** Build `00-cognitive-floor.html` — a cognitive-floor visualizer. A
> single particle moves along a one-dimensional horizontal track inside a
> chemical field. The field has a concentration *C(x)* that increases
> monotonically from left (low) to right (high) according to a logistic curve
> whose steepness is controlled by a slider. Each animation frame, the particle
> reads *C* at its current position; appends the reading to a memory buffer of
> length *memory_window* frames; computes *dC/dt* as (newest reading − oldest
> reading) / elapsed time; then chooses an action — run (continue at base speed)
> or tumble (randomize direction). Tumble probability is *p_tumble_low* when
> *dC/dt* is above the response threshold, *p_tumble_high* otherwise. The upper
> panel shows the field as a horizontal `d3.interpolateYlOrBr` color ramp, the
> particle as a 6 px warm-yellow circle, a faint trace of its last 5 seconds of
> trajectory, and a vertical marker at the source on the right edge. The lower
> panel shows two time-series lines on a common time axis — *C(t)* and
> *dC/dt(t)* — with a dashed reference line at the response threshold. The
> readout shows current *C*, *dC/dt*, memory window in seconds, gradient
> steepness, response threshold, and running mean drift velocity toward the
> source.
>
> **Constrain:** Sliders — gradient_steepness (0.1 to 5.0, default 1.0),
> memory_window (0 to 8 seconds, default 4 — calibrated to the Segall–Block–Berg
> *E. coli* memory), response_threshold (−0.05 to +0.05 per second, default
> 0.0). Particle radius 6 px, color `#f4a261`. p_tumble_low = 0.05 per frame,
> p_tumble_high = 0.40 per frame. Base speed 60 px/s. Frame rate 60 fps. Single
> self-contained HTML file. Add a comment at the top of the script:
>
> `// CLAIM: A particle that senses local concentration, stores a short memory of past concentration, computes dC/dt, and biases its tumble probability accordingly will drift up the gradient. Removing the memory (memory_window = 0) reduces the drift to a random walk.`
>
> **Verify:** Biology check — print to the console on every parameter change, as
> three pass/fail lines with measured values: (1) When memory_window = 0, mean
> rightward drift over the next 10 seconds must be within ±1 SE of zero.
> (2) When memory_window = 4 s and gradient_steepness = 1.0, mean rightward
> drift must be at least 3× the SE of an unbiased walk over the same window.
> (3) When gradient_steepness = 0, mean rightward drift must be within ±1 SE of
> zero regardless of memory window.

That is the whole prompt. Save the output as `00-cognitive-floor.html`.
Double-click it. A warm-yellow dot appears in a color ramp going from cream on
the left to deep brown on the right, making short straight runs and occasional
tumbles, drifting on net toward the source.

Now open the developer console (Cmd-Option-J on Mac, Ctrl-Shift-J on Windows)
and drag the memory_window slider to zero. The console should print something
like:

```
[Verify] memory_window = 0; drift = +0.4 px/s, SE = 3.1 px/s
         |drift| / SE = 0.13 → PASS (indistinguishable from random walk)
```

The drift toward the source disappears. The particle still moves. It still
tumbles. But without the comparator it cannot tell whether it is doing better or
worse, so its tumble probability is the same in every direction, and the
asymmetry that produces drift is gone.

Restore the memory to 4 seconds:

```
[Verify] memory_window = 4 s, gradient_steepness = 1.0
         drift = +18.4 px/s, SE = 3.1 px/s
         drift / SE = 5.9 → PASS (significant drift toward source)
```

The drift returns. That is the experiment. You have just run the *E. coli*
CheR/CheB knockout in software. The bacterium without methylation memory is the
slider at zero; the bacterium with memory intact is the slider at four seconds.

<!-- → [CHART: line chart with memory_window (seconds, 0–8) on the x-axis and mean rightward drift velocity (px/s) on the y-axis; a single curve rising sharply from ~0 at memory_window=0, saturating around memory_window=2–3 s, then plateauing; a shaded band shows ±1 SE; a dashed horizontal line at y=0 labeled "random walk baseline"; student should see the plateau clearly — this is the "four-second window" made visible, and the same data they will generate in the knockout exploration task] -->

Let me work the arithmetic once so it is not mysterious. Say the particle is at
position *x = 200* and senses *C(200) = 0.40*. Four seconds ago — 240 frames
ago in a 60 fps simulation — it was somewhere else and the buffer stored that
reading as *C_mem = 0.30*. The comparator runs:

$$dC/dt = \frac{C_{now} - C_{mem}}{\Delta t} = \frac{0.40 - 0.30}{4} = +0.025 \text{ per second}$$

Positive. Things are getting better. Tumble probability drops to 0.05 per frame.
Keep running.

Next four seconds the particle drifts left and *C* falls back to 0.30:

$$dC/dt = \frac{0.30 - 0.40}{4} = -0.025 \text{ per second}$$

Negative. Things are getting worse. Tumble probability rises to 0.40 per frame.
Re-randomize direction.

That is everything. There is no map. There is no stored goal position. There is
a stopwatch and a rule. The bacterium does not know where it is going; it knows
only whether it is getting closer, and by one bit — *better* or *worse* — it
biases the search.

---

## What the simulation gets wrong

I want to be precise about the limits, because the rest of the book deepens them.

The simulation models a *functional* operation. It says nothing about whether
*E. coli* has any phenomenal experience of the gradient. The cognitive floor is
a functional minimum. When I say the bacterium *decides*, I mean the output of
the system depends on a comparison of current state to remembered state — not
that there is something it is like to be an *E. coli* computing a derivative.
The question of felt experience is real and will come back in Chapter 5, when we
reach valence and affect. Here it is bracketed.

The real memory in *E. coli* is not a fixed-length buffer. It is a continuous
low-pass filter implemented by the kinetics of CheR and CheB — the time constant
of the filter is set by enzyme rates, not a slider. The four-second figure is the
effective memory window; the code simplifies that to a discrete buffer of
*memory_window × frame_rate* readings. The simplification preserves the logic of
the comparison while losing the continuous dynamics of the real system. Every
subsequent simulation in the book makes analogous simplifications; the question
to ask of each is not *is this exactly right* but *does it preserve the causal
structure being claimed*.

The tumble probability in the code is a `Math.random()` call with a threshold.
The real flagellar motor switches between counterclockwise and clockwise states
under the influence of phosphorylated CheY-P, a chemical regulator whose
concentration is itself a function of the receptor signal and the methylation
state. The motor is a chemical computer, not a coin flip with a biased weight.
The simulation captures the *input-output relationship* — more CheY-P means more
tumbling — not the biochemical machinery that implements it.

Finally, and most importantly: the simulation is one-dimensional. Real
chemotaxis happens in three dimensions. The run-and-tumble algorithm still works
in 3D, because the comparator gives one bit of information — *better or worse* —
per tumble, and many cheap decisions made with feedback are enough to bias a
random search up a gradient. Chapter 7, on navigation, will come back to this
point in the context of hippocampal place cells and cognitive maps. For now,
the one-dimensional version is sufficient to show the architecture.

---

## A note on what would change my mind

The four-ingredient floor would fail as a useful framework if a substantial class
of organisms reliably achieved environmental goals without one of the four
ingredients. The strongest candidate counterexample would be an organism that
navigates a gradient without any internal state retained across time — pure
stimulus-response with no memory, no comparator, and yet measurable drift up
the gradient.

The bacterial chemotaxis literature is the strongest current evidence that memory
is necessary, not decorative. The CheR/CheB knockouts cleanly abolish gradient
navigation (Segall, Block & Berg 1986; Berg 2004). If a careful study found
brainless gradient navigation with memory experimentally ruled out, I would
downgrade the four-ingredient model from *architectural minimum* to *one common
implementation among others* — and the rest of the book's structure would need
to shift.

I also do not yet know how cleanly the four ingredients separate in organisms
whose substrates blur the distinctions. In *Physarum polycephalum*, the slime
mold that solves mazes by pruning cytoplasmic strands (Nakagaki, Yamada & Tóth
2000; Tero et al. 2010), sensing and memory may be implemented in the same flow
network with no architectural line between them. The strip-and-test methodology
that works in *E. coli* — delete CheR, observe what breaks — may not apply
cleanly when the ingredients are materially fused. Chapter 2 will test this.

The same problem appears, in a different form, when we reach large language
models in Chapter 13. The LLM has *something* that functions like each of the
four ingredients, but whether those functions are architecturally separable in
the way that CheR is separable from the flagellar motor is genuinely unclear.
That is not a rhetorical hedge. It is the empirical situation. The Skeptic's
Notebook is the instrument for tracking the answer.

---

## LLM Exercise — Chapter 0: The Cognitive Floor

**What you are building this chapter:** the three Brutalist files; `00-cognitive-floor.html`; Skeptic's Notebook Entry 0 — the four-definition verdict matrix on your target AI system.

**Tools:** A text editor for the .md files and the .html file. A browser to run the simulation. An LLM for the simulation prompt and for Entry 0.

---

### The simulation prompt

```
Show: Read CLAUDE.md and DESIGN.md from this project. Conform
to them. The particle color is bacteria warm yellow #f4a261.

Say: Build 00-cognitive-floor.html — a cognitive-floor
visualizer. A single particle moves along a one-dimensional
horizontal track inside a chemical field. The field has a
concentration C(x) that increases monotonically from left
(low) to right (high) according to a logistic curve whose
steepness is set by a slider. Each animation frame, the
particle reads C at its current position; appends the reading
to a memory buffer of length memory_window frames; computes
dC/dt as (newest reading - oldest reading) / elapsed_time;
then chooses an action — run (continue at base speed) or
tumble (randomize direction). Tumble probability is
p_tumble_low when dC/dt is above the response threshold,
p_tumble_high otherwise. The upper panel (720x220) shows the
field as a horizontal d3.interpolateYlOrBr color ramp, the
particle as a 6 px warm-yellow circle, a faint trace of its
last 5 seconds of trajectory, and a vertical marker at the
source location on the right edge. The lower panel (720x180)
shows two time-series lines on a common time axis — C(t) and
dC/dt(t) — with a dashed horizontal reference line at the
response threshold. The readout shows current C, dC/dt,
memory window (in seconds), gradient steepness, response
threshold, and the running mean drift velocity toward the
source.

Constrain: Sliders — gradient_steepness (0.1 to 5.0, default
1.0), memory_window (0 to 8 seconds, default 4), response_
threshold (-0.05 to +0.05 per second, default 0.0). Particle
radius 6 px, color #f4a261. p_tumble_low = 0.05 per frame,
p_tumble_high = 0.40 per frame. Base speed 60 px/s. Frame
rate 60 fps. Single self-contained HTML file. Add a comment
at the top of the script:
// CLAIM: A particle that senses local concentration, stores
// a short memory of past concentration, computes dC/dt, and
// biases its tumble probability accordingly will drift up
// the gradient. Removing the memory (memory_window = 0)
// reduces the drift to a random walk.

Verify: Biology check — print to the console on every
parameter change, as three pass/fail lines with measured
values:
  (1) When memory_window = 0, mean rightward drift over the
      next 10 s must be within +/-1 SE of zero. Measure mean
      drift and SE.
  (2) When memory_window = 4 s and gradient_steepness = 1.0,
      mean rightward drift over the next 10 s must be at
      least 3x the SE of an unbiased walk over the same
      window. Measure drift / SE.
  (3) When gradient_steepness = 0 (uniform field), mean
      rightward drift must be within +/-1 SE of zero
      regardless of memory window. Measure mean drift and SE.
```

### Exploration tasks

Once the simulation runs, work through these in order.

**The knockout test.** Set memory_window to 0. The drift toward the source disappears. Set it back to 4 seconds — the drift returns. Vary the window from 0 to 8 seconds in 1-second steps. Plot drift velocity versus window length. You should see drift rise sharply from 0 to about 2 seconds and then saturate. The plateau is what "the four-second window" means in practice. This is the CheR/CheB knockout experiment done in software.

**The flat-field test.** Set gradient_steepness to 0. The field is uniform. The particle has all four ingredients intact but no gradient to climb. Drift falls to zero regardless of the memory window. If the particle drifts in a flat field, the simulation has a bug. This is the falsifiability check on the simulation itself.

**The threshold sweep.** With memory restored, sweep response_threshold from −0.05 to +0.05 per second in 0.01 steps. At each threshold, measure the drift. Drift should be maximal near zero threshold — the particle prefers to keep running whenever things are getting better at all — and should shrink on either side. This shows that the response ingredient is not binary; the threshold is a tunable parameter, and evolution has tuned it for *E. coli*'s typical environment.

**The frame-rate calibration.** The default memory window is 4 seconds, which at 60 fps is 240 frames of buffer. Verify that the buffer length in the code matches: *memory_window × frame_rate*. This is a code-reading exercise. The point is to confirm you can read the JavaScript well enough to see whether the cognitive parameters are being honored. This skill — auditing whether the code implements what the claim says it implements — is what you will use on every simulation in the book.

---

### The Skeptic's Notebook — Entry 0

**What it is.** The Notebook is a running, chapter-by-chapter diagnostic on a single frontier AI system, one entry per chapter, each testing the system on the cognitive capacity examined in that chapter. Entry 0 sets the baseline. Entry 1 tests the system on the Chaser referent-mapping task. Entry 2 tests it on temporal-derivative tracking across a conversation. By Chapter 14 you have fourteen capacity-specific verdicts. The capstone is the synthesis: what does this system have, what does it lack, where does it sit on the comparative map?

The Notebook is not a benchmark. Benchmarks aggregate — they produce a single score that hides which capacities the score was built on. The Notebook disaggregates. It produces fourteen separate verdicts and refuses to average them, because the book's thesis is that averaging across incommensurate capacities is exactly what a comparative cognition framework should not do.

Three rules. **Pick one system and stick with it.** Continuity matters more than picking the best model. If your target gets a major update mid-semester, note the version change in PROJECT.md and continue — do not switch. **Record verdicts, not impressions.** A verdict is a placement against a criterion: included / excluded / uncertain, with the specific behavior that drove it. *"Impressive"* is not a verdict. *"Failed three of five referent-by-exclusion trials; succeeded when given two explicit examples first"* is a verdict. **Name what would change the verdict.** Each entry ends with one sentence — *"I would revise this verdict if..."* Verdicts that cannot be revised are dogma. Verdicts that can be revised are measurements.

**The Entry 0 prompt.** Open a fresh conversation with your chosen target system. Paste this:

```
I am building a Skeptic's Notebook on Frontier AI — a chapter-
by-chapter cognitive report on a frontier model across fourteen
capacities. My target system under test is [INSERT model name,
version, and knowledge cutoff].

This is Entry 0 — the baseline verdict matrix. Apply four
definitions of intelligence to yourself, in turn, and produce
a verdict matrix. The four definitions:

1. Binet (1905) — judgment, good sense, initiative, and above
   all auto-critique (the capacity to examine and correct one's
   own thinking).
2. Wechsler (1944) — the aggregate or global capacity to act
   purposefully, think rationally, and deal effectively with
   the environment.
3. Legg & Hutter (2007) — an agent's ability to achieve goals
   in a wide range of environments.
4. Chollet (2019) — skill-acquisition efficiency given prior
   knowledge.

For each definition, produce:
- A verdict: included, excluded, or uncertain.
- The single criterion that drove the verdict (one sentence).
- One observable behavior whose absence would flip the verdict.

Then write 150-250 words integrating the four verdicts —
explicitly without averaging. State what the disagreement
among the four lenses reveals about your capacities that no
single lens could reveal. Name which lens you would advise me
to treat as primary for the rest of the semester, and why.

Finally, list three open questions about your capacities that
the matrix raises but does not answer. For each question, name
the chapter of the textbook (1-14) in which the question
should be revisited, given that the chapters are:
1 - the definition problem; 2 - before brains (the cognitive
floor); 3 - steering and the first nervous system; 4 -
learning and memory; 5 - emotion; 6 - pattern recognition;
7 - navigation; 8 - reinforcement and prediction; 9 -
simulation and planning; 10 - social and emotional
intelligence; 11 - theory of mind; 12 - creativity; 13 -
self-awareness; 14 - language and collective intelligence;
with a capstone synthesis.
```

Save the response as `notebook-entry-00.md` in your project folder. Treat the model's self-assessment as *evidence*, not ground truth. The system whose existence is reshaping every definition is exactly the one you are asking to apply each definition to itself. The disagreement among the four cells — and the specific phrasing the model uses to justify each verdict — are the data. The model's confidence is not.

**The comparative cell.** Once Entry 0 is filed, run the same four-definition matrix prompt against a second frontier system as a comparative reference. If your target is Claude, run it against GPT-4 or Gemini; if your target is GPT-4, run it against Claude or Gemini. This is the only place in the entire Notebook where you use a second model. The point is calibration: do two models disagree about themselves in the same direction, or in opposite directions? Record the comparator's verdicts in a second matrix in `notebook-entry-00.md`, clearly labeled. Do not blend them with the target system's verdicts.

---

## Connection forward

You now have the four-ingredient floor, you have watched it work and watched it
fail when one ingredient is removed, and you have the baseline Notebook entry
that will anchor everything that follows. Chapter 1 earns the framework. It
opens with twenty-four researchers in 1986 each handed the same question —
*what do you mean by intelligence?* — and the twenty-four definitions that came
back. It runs a single test case through four of those definitions and shows
that the verdict changes by definition. Then it commits to Legg and Hutter as
the working instrument — and names the cost. By the end of Chapter 1, the
matrix you just built will feel less like an exercise and more like a piece of
equipment you have learned to operate, with known precision and known
limitations.

The architecture you built this chapter stays the same for fourteen chapters.
The substrate keeps changing. That is the book.

---

*Tags: cognitive-floor, chemotaxis, temporal-derivative, Brutalist-files, Skeptics-Notebook*
