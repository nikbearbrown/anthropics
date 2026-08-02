# Chapter 00 — How to Use the Simulations

**Suggested titles:**
- *Before You Read Anything Else, Build a Growth Curve*
- *Four Files, One Curve, and the Habit That Holds the Book Together*
- *How to Make a Microbe Grow on Your Laptop*

---

**TL;DR.** Before you read any biology in this book, you will build a working bacterial growth-curve simulator on your laptop — three governing files (CLAUDE.md, DESIGN.md, PROJECT.md), one HTML file, four lines of math. The point is not the simulation; the point is the habit of prompting an LLM precisely enough that the simulation runs the first time and you can tell from looking at it whether the biology is right.

---

## Learning objectives

By the end of this chapter, you will be able to:

1. **Construct** the three Brutalist governing files — CLAUDE.md, DESIGN.md, PROJECT.md — for a microbiology simulation project, and **explain** what each one constrains.
2. **Compose** a four-move prompt (Show / Say / Constrain / Verify) that produces a runnable D3 v7 simulation in a single pass.
3. **Implement** the logistic growth equation *dN/dt = rN(1 − N/K)* using Euler-method numerical integration, and **identify** the four phases (lag, log, stationary, death) on the resulting curve.
4. **Verify** a simulation against biology by asking *one* falsifiable question — "does halving the doubling time double the slope of the log phase?" — and reading the answer off the chart.
5. **Critique** three failure modes ("the simulation IS the biology," "more parameters = more realistic," "if it runs, it's correct") and **apply** the critique to your own build.

**Prerequisites.** A laptop with a text editor and a browser. An account on claude.ai (or any LLM — the prompts work with minor edits in ChatGPT and Gemini). The ability to double-click an HTML file. No coding background assumed.

---

## A scene from the lab

It is 11:47 p.m. on a Tuesday in the second week of microbiology lab. Maria has spent the last six hours pipetting *E. coli* from a starter flask into eight tubes, each with a different concentration of glucose, and she has been reading the optical density on a benchtop spectrophotometer every fifteen minutes. Her notebook has 32 rows of numbers. The TA wants a growth curve for each tube by 8 a.m. — and Maria does not actually know what a growth curve is supposed to look like. She knows the shape of an exponential. She knows the shape of a plateau. She does not know what they look like glued together, and she does not know whether the wobble at minute 90 in tube 3 is a real lag or a pipetting error.

She has a choice. She can plot the data in Excel and hope for the best. Or she can spend ten minutes building a simulator that draws the *idealized* growth curve, slide the parameters around until the simulated curve matches the shape of her data, and *then* plot her measurements on top.

This chapter is for the second choice.

The reason is simple. A growth curve is a hypothesis about how a population of cells changes through time. Maria's 32 rows of numbers are evidence. Without a hypothesis to compare them to, the evidence is just numbers. With a hypothesis — a simulated curve she can see, modify, and probe — the evidence becomes a test. The wobble at minute 90 is either consistent with the lag phase the model predicts, or it isn't. She does not need a textbook to tell her. She needs a model on her screen that responds when she changes the inputs.

That is the entire purpose of the +1 simulations in this book. They are not illustrations. They are not pretty pictures generated to decorate a paragraph. They are *runnable hypotheses*. You build one, you change a parameter, the curve changes, and you learn something about the biology by watching what the curve does — or refuses to do.

By the end of this chapter, you will have built Maria's tool.

---

## What we are actually doing

Three things, in order.

**One.** We are setting up a project structure that will outlast this chapter. The structure is called Brutalist because there is nothing decorative in it — three plain-text files governing the entire workshop, no frameworks, no build tools, no `npm install`. The files are CLAUDE.md, DESIGN.md, and PROJECT.md. CLAUDE.md tells the LLM how to write code for this book. DESIGN.md tells it how the result should look. PROJECT.md tells it what already exists and what comes next. Every simulation in every chapter will refer back to these three files. Get them right once and you will not write them again.

**Two.** We are learning a four-move prompt structure. Most students paste vague requests into Claude — *"make me a growth curve simulation"* — and then spend an hour fighting the output. We are going to skip that hour. The structure is **Show / Say / Constrain / Verify**. Show the LLM the files it should follow. Say what you want in one paragraph. Constrain how it has to be built (D3 v7, single HTML file, no external dependencies). Verify by giving it a falsifiable biology question it must satisfy. Four moves. Used together they are absurdly more reliable than any single move alone.

**Three.** We are building one specific simulation — a bacterial growth curve — and we are building it because every student who takes a microbiology lab will need to understand it. The growth curve is the most common quantitative tool in the field. If you can read one, you can read antibiotic-susceptibility curves, biofilm-formation kinetics, viral-replication curves, immune-response curves. The math underneath is identical. Different *r*, different *K*, same equation.

Let me unpack the math now, because it is the only formal piece in the chapter and the rest depends on it.

### The logistic growth equation, plainly

A bacterium in a flask of fresh broth at 37 °C does the simplest possible thing: it eats, it grows, it splits in two. Each daughter cell does the same. If nothing stopped this process, the population would double on a fixed schedule — every 20 minutes for healthy *E. coli*, every 30 minutes for most clinically relevant bacteria, every 24 hours for *Mycobacterium tuberculosis*. The schedule is called the **doubling time**, written *t_d*. Fancy word, plain meaning: how long it takes the population to become twice itself.

If doubling were the whole story, the math would be:

> *N(t) = N₀ · 2^(t/t_d)*

— starting population *N₀*, time *t*, doubling time *t_d*. Pure exponential. Plot this on a log y-axis and you get a straight line, forever.

The problem: nothing grows forever. The flask is finite. The glucose runs out. The waste products accumulate. The cells crowd each other. At some point the population stops growing not because the cells got tired but because there is no more room in the meaning that matters — no more food, no more space, too much acid, too much something.

Pierre Verhulst, a Belgian mathematician, wrote down the simplest correction in 1838. He said: the rate at which the population grows is proportional to how many cells you already have, *minus* a term that gets bigger as the population approaches some ceiling. Call the ceiling *K* — the **carrying capacity**, the largest population the flask can support. Then:

> *dN/dt = r · N · (1 − N/K)*

Read it left to right. *dN/dt* is the rate of change of the population — how fast the number of cells is going up per unit time. *r* is the intrinsic growth rate — for *E. coli*, roughly 2 per hour, which means the population would multiply by *e²* ≈ 7.4 every hour if nothing slowed it. *N* is the current population. The term *(1 − N/K)* is the brake: when *N* is small relative to *K*, the brake is near 1 and the equation behaves like pure exponential growth. When *N* approaches *K*, the brake approaches zero and the population stops growing. When *N* somehow exceeds *K*, the brake goes negative and the population shrinks back.

This is the **logistic growth equation**. *Logistic* here is a historical name from Verhulst that has nothing to do with logistics in the modern sense — it comes from a now-archaic mathematical term and you can safely forget the etymology. What matters is the shape it produces: an S-curve. Slow start, fast middle, slow finish.

We have to solve the equation to plot it, and the easy way to solve a differential equation on a computer is called the **Euler method** — named after the eighteenth-century Swiss mathematician Leonhard Euler and pronounced *oiler*. The trick is humble. If you know how fast something is changing right now, you can estimate where it will be a tiny moment later by assuming the rate stays the same for that moment. Mathematically:

> *N(t + Δt) ≈ N(t) + (dN/dt) · Δt*

Pick a small *Δt* — say, one minute. Compute *dN/dt* from the current *N*. Add the result, times *Δt*, to *N*. That is your new *N*. Repeat. The smaller *Δt* is, the more accurate the result. For a growth curve running over eight hours, *Δt* of 0.1 to 1 minute is plenty.

Euler's method is the worst numerical integrator that still works. For genuine accuracy you would use Runge-Kutta or an adaptive solver. We are going to use Euler anyway, because it is twelve lines of code, students can read it, and the error is far smaller than the error in any biological parameter you are putting into the model. *r* is uncertain. *K* is uncertain. The integration scheme is the least uncertain thing in the simulation.

To get the lag phase — the early stretch where the cells are alive but not yet dividing because they are adjusting to the new medium — we just set *dN/dt = 0* for the lag duration *L*. To get the death phase — the late stretch where waste products kill cells faster than survivors can replace them — we add a death-rate term once the carrying capacity has been held for a while. Both are crude. Both produce a curve that looks like every textbook figure you will ever see of a bacterial growth curve. That is the point.

Now we are ready to build it.

---

## The three governing files

Before you write any HTML, you write three text files. They go in the same folder as the simulation. The LLM reads them every time you ask for new code. This is the cheap, durable substitute for everything that more elaborate development environments do — there is no `package.json`, no `vite.config.js`, no framework. Three text files.

### CLAUDE.md — the coding constitution

This file tells the LLM what kind of code to produce. It is short. It does not change between chapters.

```markdown
# CLAUDE.md — Microbiology Simulation Coding Constitution

## Stack
- Single .html file per simulation. No external build step.
- D3 v7 loaded from CDN: <script src="https://d3js.org/d3.v7.min.js"></script>
- Plain HTML, CSS, and JavaScript. No frameworks. No npm.

## Visualization
- All drawing happens inside one <svg> element.
- Use D3 selections, scales, and transitions.
- Charts use d3.scaleLinear or d3.scaleTime, d3.line, d3.axisBottom/Left.
- Animated transitions on parameter change: duration 250 ms.

## Interaction
- Parameter controls are <input type="range"> sliders.
- A <div id="readout"> displays current parameter values to two significant figures.
- Sliders update the chart in real time via an `input` event listener.

## Biology
- Every simulation models a named biological process.
- Variables in the code use biology names (N, K, r, t_d) — not generic
  ones like x and y.
- A short comment at the top of every <script> block states the
  biological claim the simulation is making and its limits.

## Verification
- Every simulation includes a hidden console.log block that prints
  the result of one biology check the moment the file loads.
- The biology check is a one-line falsifiable claim: e.g., "doubling t_d
  halves the slope of the log phase on a log y-axis."
```

That is it. Forty lines, give or take. The LLM follows it because you point at it in every prompt: *"Conform to CLAUDE.md."*

### DESIGN.md — the visual constitution

```markdown
# DESIGN.md — Visual Constitution

## Color palette (biology-coded)
- Bacteria:        #2d6a4f   (dark green)
- Viruses:         #e63946   (red)
- Host cells:      #457b9d   (blue)
- Dead cells:      #adb5bd   (gray)
- Immune cells:    #e76f51   (orange)
- Drug / antibiotic: #7b2d8b (purple)

## Chart styling
- Growth curves and time series: line color #1a1714 (near-black) on
  white background #ffffff.
- Dark-mode background: #1a1a1a. Line color in dark mode: #f8f9fa.
- Axis labels: 12 px sans-serif. Title: 16 px.
- Grid lines: #e9ecef at 1 px.

## Sliders
- 320 px wide. Labels above. Current value to the right.

## Layout
- SVG canvas: 720 px wide × 400 px tall by default.
- Margins: top 30, right 30, bottom 50, left 60.

## Type
- system-ui, -apple-system, sans-serif.
```

DESIGN.md says nothing about biology. It says how things look. Keeping the two files separate matters: when you change a color scheme, you do not touch the biology. When you fix a biology bug, you do not touch the colors.

### PROJECT.md — the state file

```markdown
# PROJECT.md — Microbiology Simulation Workshop

## Built so far
- (chapter, file, what it models)

## In progress
- 00-growth-curve.html — bacterial growth curve, logistic model
  with lag and death phases. Sliders for r, K, t_lag.

## Next
- 01-microscope-resolution.html — diffraction-limit calculator.

## Conventions
- File naming: NN-slug.html, where NN is chapter number.
- Each file is self-contained (no shared JS).
- Every file has a one-line `// CLAIM:` comment at the top.
```

PROJECT.md is the only file you actually edit chapter to chapter. The other two stay fixed.

---

## The four-move prompt

Now you have three governing files. To get a working simulation, you paste one prompt at Claude. The structure is **Show / Say / Constrain / Verify**.

**Show** — point at the files Claude must conform to. *"Read CLAUDE.md and DESIGN.md."* If you are working in Claude.ai, you attach the files. If you are working in Claude Code or Cowork, the files are already on disk and the LLM reads them automatically.

**Say** — one paragraph describing the artifact in biological terms. *"Build a bacterial growth-curve simulator. The model is logistic growth with an explicit lag phase and a death phase. Sliders control growth rate r, carrying capacity K, and lag duration t_lag. The chart shows population N versus time on a log y-axis from t = 0 to t = 8 hours."*

**Constrain** — the rules the file has to obey, beyond what CLAUDE.md already says. *"Use Euler integration with dt = 0.1 min. Label each of the four phases (lag, log, stationary, death) directly on the chart. Display doubling time t_d = ln(2)/r in the readout, in minutes."*

**Verify** — one falsifiable biology check the simulation must pass. *"Verification: when I halve r, the slope of the log phase on the log y-axis must halve. Print the measured slope of the log phase to the console on every parameter change."*

That is the entire prompt. Four moves. Three short paragraphs. The LLM writes one HTML file. You double-click it. It runs.

Let me show you what that looks like in practice.

---

## A worked example — building 00-growth-curve.html

Here is the actual prompt I would paste at Claude:

> **Show:** Read CLAUDE.md and DESIGN.md from this project. Conform to them.
>
> **Say:** Build `00-growth-curve.html` — a bacterial growth curve simulator. The model is logistic growth *dN/dt = r · N · (1 − N/K)* with an explicit lag phase (during which *dN/dt = 0*) and a death phase (where, after the population sits within 5% of *K* for one hour, a death rate of *0.3 r* kicks in). Sliders control *r* (range 0.5 to 4 per hour, default 2.0), *K* (range 10⁷ to 10¹⁰ cells/mL, log scale, default 10⁹), and *t_lag* (range 0 to 120 min, default 30). Y-axis is log scale, *N* in cells/mL. X-axis is time in hours, 0 to 8.
>
> **Constrain:** Use Euler integration with *dt = 0.1 min*. The chart labels each of the four phases — lag, log, stationary, death — directly on the curve at the phase midpoint. The readout shows current *r*, *K*, *t_lag*, and the computed doubling time *t_d = ln(2)/r* in minutes. Sliders update the chart with a 250 ms transition. Bacteria color (#2d6a4f) for the curve.
>
> **Verify:** Biology check — when I halve *r*, the slope of the log phase on the log y-axis must halve, and *t_d* must double. Print the measured log-phase slope and *t_d* to the console after every parameter change. Add a comment at the top: `// CLAIM: Logistic growth with explicit lag and death predicts a four-phase curve; doubling t_d halves the log-phase slope.`

Paste that into Claude. Wait twenty seconds. Save the file. Double-click it in your browser. You should see a green S-curve climbing from 10⁶ cells/mL at *t = 0* to roughly 10⁹ at *t = 4 hours*, leveling off, and beginning to drift downward around *t = 6 hours*. The four phases are labeled on the curve.

Now do the verification yourself. Move the *r* slider from 2.0 to 1.0. The doubling time should jump from about 21 minutes to about 42 minutes. The log phase should look noticeably gentler. Open the browser's developer console (Cmd-Option-J on Mac, Ctrl-Shift-J on Windows). The console should print two numbers: the measured log-phase slope and *t_d*. Halving *r* should halve the slope. If it doesn't, the simulation is wrong, and you push back at the LLM with the exact failure: *"Halving r changed the slope from 0.046 to 0.041, not 0.023. Fix it."*

Let me work the math once on the page so you can see what the numbers should be.

For *r = 2.0* per hour:

> *t_d = ln(2) / r = 0.693 / 2.0 = 0.347 hours ≈ 20.8 minutes*

The log-phase slope on a log₁₀ y-axis is:

> *slope = r / ln(10) = 2.0 / 2.303 ≈ 0.868 per hour*

— which means the population multiplies by 10 every *1 / 0.868 ≈ 1.15* hours. Halve *r* to 1.0:

> *t_d = 0.693 / 1.0 ≈ 41.6 minutes*
>
> *slope = 1.0 / 2.303 ≈ 0.434 per hour*

The doubling time doubled. The slope halved. That is the verification.

**The lesson.** When the verification passes — and it usually does on the first try, because the prompt was specific enough — you have a working tool you can probe for the rest of the semester. You can simulate any culture by adjusting two numbers. You can answer "what does a 30-minute change in doubling time do to an 8-hour outgrowth?" in five seconds.

**The limit.** The simulation is wrong about death. Real bacterial death is not a constant rate; it depends on pH, accumulated waste, oxygen depletion, and quorum-sensing signals. Real lag is not a flat zero; cells are upregulating genes the whole time. The model is a useful caricature, not a microbiologically faithful account. You should always be able to state which simplifications a simulation makes — and our simulation makes three: instantaneous lag-to-log transition, constant death rate, no nutrient depletion model. We will come back to each of these in Chapter 9.

---

## Common misconceptions

**"The simulation IS the biology."** No. The simulation is a hypothesis about the biology, encoded in a few lines of math. Every parameter is something a real bacterium does not actually know about itself. *K* is not stamped on the cell wall. *r* changes with temperature, oxygen, and substrate. The simulation tells you *what would happen if the world worked the way the equation says it works*. Real bacteria do not consult the equation. They consult their surroundings.

**"More parameters = more realistic."** No. More parameters means more places to be wrong. Every parameter you add is a thing you have to justify, measure, and defend. The simplest model that captures the four phases is the best teaching tool, because it lets you see what each parameter does. A model with twelve parameters and one knob hidden inside `oxygenAffinityCoefficient` is not more realistic; it is more obscure. Aim for the smallest model that captures the behavior you care about, and add complexity only when you can articulate what new question the new parameter answers.

**"If it runs, it's correct."** No — and this is the most expensive mistake students make. Code that runs has passed a *syntax* check, not a *biology* check. A simulation that produces a smooth curve from random noise is still running. The verification step in the four-move prompt is the firewall: a falsifiable biology claim that the simulation must satisfy. *"Halving r halves the log-phase slope."* If that statement fails — even though the page renders — the simulation is wrong. The simulation runs in JavaScript. Biology lives in the verification.

A subtler misconception, which I'll add because students hit it often: *"The LLM understands the biology."* The LLM understands *patterns in text* about biology. Sometimes those patterns line up with the underlying mechanism; sometimes they look right but encode a subtle error. When you ask the LLM to write a simulation, you are not delegating biological judgment. You are delegating typing. The biological judgment is yours, expressed in the verification clause.

---

## Exercises

**Exercise 1 — Build (warm-up).** Create the three governing files (CLAUDE.md, DESIGN.md, PROJECT.md) using the templates above. Use the four-move prompt to build `00-growth-curve.html`. Open it in your browser and confirm: (a) the curve shows four labeled phases, (b) sliders change the curve in real time, (c) the console prints *t_d* and log-phase slope. *Deliverable:* a working HTML file plus a one-sentence description of what changed when you moved the *r* slider.

**Exercise 2 — Apply.** A patient is on a 24-hour intravenous antibiotic that, you are told, doubles bacterial doubling time from 30 minutes to 60 minutes for the bloodstream pathogen *Staphylococcus aureus*. The blood culture is drawn 8 hours after dosing started. Using your simulator, set *r* such that *t_d ≈ 30 min* and read off *N* at *t = 8 hours*. Then set *r* such that *t_d ≈ 60 min* and read off *N* at *t = 8 hours*. Report both numbers and the ratio. Is the ratio what you would predict from doubling-time math alone? *(Hint: 8 hours is 16 doublings versus 8 doublings. Predict the ratio first, then check.)*

**Exercise 3 — Verify the biology check empirically.** With the simulator open and the console visible, sweep *r* from 0.5 to 4.0 per hour in steps of 0.5. At each value, record *r*, the console-printed *t_d*, and the console-printed log-phase slope. Plot *t_d* vs. *1/r* and slope vs. *r*. Both plots should be straight lines through the origin. If either is not, the simulation has a bug and you should push the LLM to fix it. *Deliverable:* a table of values plus a one-sentence verdict on whether the biology check passed.

**Exercise 4 — Stretch (challenge).** Modify the simulation so the death phase begins when the cumulative metabolic waste — modeled as the time-integral of *N* — crosses a threshold *W_max*. This is a more biological mechanism than the "5% of *K* for one hour" rule. *(a)* Write a four-move prompt asking the LLM for this modification, with a verification clause: *"doubling K must roughly halve the time-to-death-phase onset, because waste accumulates proportional to the standing population."* *(b)* Run the modified simulation. *(c)* Decide whether the new model behaves more or less like real bacterial death than the original. Justify your answer in three sentences.

---

## What would change my mind

The logistic model would fail as a first approximation if, across a substantial set of bacterial species grown in well-mixed liquid culture under standard laboratory conditions, the observed population trajectories systematically failed to be S-shaped — for example, if oscillating populations, multi-modal plateaus, or geometric collapse without a stationary phase were the rule rather than the exception. The evidence to date (most introductory microbiology lab manuals; the canonical Monod 1949 paper on bacterial growth kinetics [verify]) is that S-shapes are the typical observation in well-mixed batch culture, with deviations explained by specific mechanisms (diauxic shifts, biofilm formation, lytic phage) rather than by failure of the underlying logistic intuition. If a large empirical review found logistic to be a poor description in the majority of cases, I would downgrade the model from "useful first approximation" to "historical convention" and the worked example would need to lead with a different equation.

## Still puzzling

I do not fully understand how much of the apparent agreement between logistic curves and real bacterial growth data is genuine mechanism versus a measurement artifact — most growth measurements use optical density, which saturates at high cell densities, which may flatten real curves into apparent stationary phases even when underlying cell division has not stopped. I also do not know how much the lag phase in any given experiment reflects metabolic adjustment versus damage repair versus residual stationary-phase physiology carried over from the inoculum. Each of those is its own paper. And I am not yet sure whether the "best simplest model" stance I took above — Euler integration, three parameters — actually scales to the more complex simulations later in the book, or whether by Chapter 9 we will need an adaptive solver and I will eat my words.

---

## LLM Exercise — Build your growth-curve simulator

This block is the one you actually do. The prompt below is ready to paste at Claude (or ChatGPT, or Gemini) once you have CLAUDE.md and DESIGN.md saved in the same folder.

### The simulation prompt

```
Show: Read CLAUDE.md and DESIGN.md from this project. Conform to them.

Say: Build 00-growth-curve.html — a bacterial growth-curve simulator.
The model is logistic growth dN/dt = r * N * (1 - N/K) with an explicit
lag phase (dN/dt = 0 for the first t_lag minutes) and a death phase
(after the population sits within 5% of K for one hour, a death rate
of 0.3 * r kicks in). Sliders control r (range 0.5 to 4.0 per hour,
default 2.0), K (range 1e7 to 1e10 cells/mL, log scale, default 1e9),
and t_lag (range 0 to 120 minutes, default 30). Initial population
N0 = 1e6 cells/mL. Y-axis is log scale from 1e5 to 1e11. X-axis is
time in hours from 0 to 8.

Constrain: Use Euler integration with dt = 0.1 min. The chart labels
each of the four phases (lag, log, stationary, death) directly on the
curve at the phase midpoint. The readout shows current r, K, t_lag,
and the computed doubling time t_d = ln(2) / r in minutes, all to two
significant figures. Sliders update the chart with a 250 ms transition.
Use bacteria color #2d6a4f for the curve. Single self-contained HTML
file, no external dependencies except d3 v7 from CDN.

Verify: Biology check — when r is halved, the slope of the log phase
on the log y-axis must halve, and t_d must double. After every
parameter change, print to the console: r, K, t_lag, computed t_d,
and the measured log-phase slope. Add a comment at the top of the
script:
// CLAIM: Logistic growth with explicit lag and death predicts a
// four-phase curve; halving r doubles t_d and halves the log-phase
// slope.
```

### Exploration tasks

Once the file runs, work through these. Each one is a small experiment.

1. **The doubling-time test.** Set *r = 2.0*. Note *t_d* and *N(8 h)*. Set *r = 1.0*. Note both again. Then set *r = 4.0*. The relationship between *r*, *t_d*, and *N(8 h)* should be predictable from the math. Is it?

2. **The carrying-capacity test.** Set *r = 2.0*, *t_lag = 0*. Sweep *K* from 10⁷ to 10¹⁰. At which *K* does the population reach stationary before *t = 4 hours*? At which *K* does it not reach stationary by *t = 8 hours*? What does this tell you about why fast-growing organisms in nutrient-rich media plateau early?

3. **The lag-phase test.** Set *r = 2.0*, *K = 10⁹*. Sweep *t_lag* from 0 to 120 minutes. How much does a 60-minute lag shift the *t = 4 hour* population versus the *t = 8 hour* population? Why does the *t = 4 hour* shift matter more than the *t = 8 hour* shift in a clinical setting?

4. **The death-phase test.** Run the simulation with default parameters out to *t = 8 hours*. When does death begin? What is *N* at death-onset? Now ask: in a real flask, would death really begin at exactly the population the simulation predicts? Why not? *(Hint: think about what "5% of K for one hour" actually models — and what it does not.)*

### Extension prompt

Once the basic simulator works, the obvious extension is to add a second curve so you can compare two cultures side by side. Paste this:

```
Extension: Modify 00-growth-curve.html so the chart shows two curves
simultaneously — one for a "control" culture (bacteria color #2d6a4f)
and one for a "test" culture (drug color #7b2d8b). Each culture has
its own set of three sliders (r, K, t_lag). The readout shows t_d for
both cultures and the population ratio N_control(t) / N_test(t) at
t = 4 h and t = 8 h. Verification: when both cultures have identical
parameters, the ratio at every time point must equal 1.0 to within
0.1%. When the test culture's r is half the control's r, the ratio at
t = 8 h must equal approximately 2^(4 h / t_d_test - 4 h / t_d_control),
provided neither culture has hit stationary.
```

This is the simulation you will reach for when Chapter 14 introduces antibiotics. The "test" culture becomes the drug-exposed culture. The ratio becomes the kill curve. The math is the same.

A connection forward, then. The growth curve you just built tells you *what microbes do* under idealized conditions. Chapter 1 asks the much older question: how did anyone figure out microbes existed in the first place, and what tools made the invisible visible? You will carry this simulator with you. The first time the chapter mentions doubling time, you will be able to pull up a curve and see it.

---

**What would change my mind:** If the same prompt structure, applied to a non-D3 stack or a different domain, produced reliable runnable simulations in a single pass without any of Show / Say / Constrain / Verify, then the four-move discipline would not be a real teaching object — it would just be ceremonial scaffolding around a process that works anyway.

**Still puzzling:** I do not yet know whether students with no prior coding background can read the JavaScript an LLM produces well enough to spot a biology-coded variable being used wrong, and that gap — between running the file and reading the file — is the real test of whether this method teaches.

---

**Tags:** logistic-growth, bacterial-doubling-time, D3-v7, Brutalist-files, four-move-prompt
