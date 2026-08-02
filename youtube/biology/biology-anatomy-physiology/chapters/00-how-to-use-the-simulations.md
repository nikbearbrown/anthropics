# Chapter 0 — How to Use the Simulations
*Before you read anything else, build a thermostat.*

---

Here is the simplest question I can ask about a living body: how does it stay the same?

Not the same forever — everything wears out, everything changes. But same enough. Same within a band. The core temperature of a healthy adult right now is somewhere near 37 °C. It was near 37 °C an hour ago. It will be near 37 °C an hour from now, whether you are sitting in a warm room or stepping into February. The cells in your liver are metabolizing. Your muscles, if you are doing anything at all, are generating heat as a byproduct. The air around you is either warmer or cooler than your skin. All of these things are pushing on the number. And the number stays put.

That stability is not an accident. It is not even particularly surprising, once you know what is doing the work. The body is running a control loop, and that control loop is the first thing this book is going to teach you — not because temperature regulation is the most important piece of physiology you will encounter, but because the loop that keeps you at 37 °C is the *same loop* that keeps your blood pressure near 90 mmHg, your blood glucose near 90 mg/dL, and your blood pH between 7.35 and 7.45. Different names on the nodes, same mathematics. Learn the loop once and you have learned the architecture of an enormous fraction of what the body does.

The question is how to learn it. You could read the description. Most textbooks have one — a cartoon with boxes and arrows, labels like *sensor*, *control center*, *effector*, and a looping arrow that says *negative feedback*. It is accurate. It is also the equivalent of reading the word *bicycle* and believing you understand how to ride one. The diagram does not move. The body moves.

So instead of a diagram, I want you to build one.

![Comparison of the static textbook feedback loop diagram](../images/00-how-to-use-the-simulations-fig-01.png)
*Figure 1.1 — Comparison of the static textbook feedback loop diagram*

---

## What the loop actually does

The regulated variable we are going to track is core body temperature, *T*, in degrees Celsius. Forget, for the moment, everything about hypothalamuses and sweat glands. Start with just the mathematics, because the mathematics is actually simple.

There are two forces acting on *T* at any given moment.

The first is whatever is pushing the temperature away from where the body wants it. Call this the *disturbance*. On a hot run in August, the disturbance is the heat your muscles generate plus the heat pouring in from the environment. On a cold morning, the disturbance is the heat you are losing to cold air. The disturbance is a rate — degrees per minute — and it can be positive (heating) or negative (cooling).

The second force is the body's corrective response. When the temperature drifts above the set point, the hypothalamus triggers things that cool the body — vasodilation, sweating. When it drifts below, it triggers things that warm the body — vasoconstriction, shivering. The corrective response is *proportional to how far the temperature has drifted*. A small drift gets a gentle push back. A large drift gets a hard one. The number that describes how aggressively the body responds to a given drift is called the *gain* of the loop, and we will call it *k*.

Put those two forces together and you have a rate equation:

$$\frac{dT}{dt} = \text{disturbance} - k \cdot (T - T_{\text{set}})$$

Read it out loud. *The rate of change of temperature equals the disturbance minus the gain times the deviation from set point.* The second term is the corrective response: it is negative when the temperature is above the set point (pushing back down) and positive when the temperature is below (pushing back up). As long as *k* is positive, the corrective response always opposes the disturbance. That is what *negative feedback* means, in plain terms. The response sign is opposite to the deviation sign.

Now here is the interesting question. What happens to *T* in the long run, under a steady disturbance?

At some point the system reaches a state where *T* stops changing — *dT/dt = 0*. Set the right side of the equation to zero and solve:

$$0 = \text{disturbance} - k \cdot (T_{\text{ss}} - T_{\text{set}})$$

$$T_{\text{ss}} = T_{\text{set}} + \frac{\text{disturbance}}{k}$$

This is the steady-state temperature. With a set point of 37.0 °C, a disturbance of +0.2 °C/min (mild heating), and a gain of +0.5 per minute, the system settles at 37.4 °C — four-tenths of a degree above the set point. The loop does not return the temperature all the way to target. It *can't*, with a proportional response of finite gain. To get exact tracking you would need infinite gain, or a different kind of controller. Real physiology gets around this with tricks we will encounter later. For now, notice what the formula tells you: the steady-state offset is *disturbance / k*. Double the gain and the offset halves. Halve the gain and the offset doubles.

![Line chart of T vs](../images/00-how-to-use-the-simulations-fig-02.png)
*Figure 1.2 — Line chart of T vs*

Now ask what happens when *k* is negative. The corrective response then *amplifies* the disturbance instead of opposing it — the temperature runs away from the set point and does not stop. That is positive feedback. Positive feedback is not an error in the equation; it is a real thing that physiology uses deliberately in a few specific situations: blood clotting, the action potential, the oxytocin surge during labor. All of them share the same signature — a process that *needs* to run to completion fast, where amplification rather than stability is the point. Every other homeostatic system uses negative feedback, because the alternative is runaway.

You should find all of this plausible, sitting here reading it. The next step is to *watch it happen*.

---

## The Euler method, and why it is enough

The rate equation above is a differential equation. It tells you how fast *T* is changing at any instant, as a function of the current *T*. To find *T* as a function of time — the curve you will eventually see on a chart — you have to integrate: add up all those instantaneous rates over every moment from the start.

Doing that analytically is possible for this particular equation, because it is linear. Doing it for the more complicated equations we will encounter later is often not possible, or not convenient. Computers solve this problem the same way a sensible person would: take a small step in time, assume the rate stays roughly constant for that step, compute the new value, repeat.

This is the Euler method, named for Leonhard Euler — the eighteenth-century Swiss mathematician pronounced *oiler*, not *yooler*. The idea is:

$$T(t + \Delta t) \approx T(t) + \frac{dT}{dt} \cdot \Delta t$$

Choose *Δt* small enough that the approximation is good — one second works fine for a process unfolding over tens of minutes — and you can integrate any rate equation a computer can evaluate. The accuracy of the Euler method is the worst of any standard numerical integrator. It is also wildly more accurate than any physiological parameter you will feed into it. The uncertainty in the real gain *k* — which depends on hydration, skin blood flow, ambient humidity, the patient's medication list, and about twelve other things — swamps the numerical error by several orders of magnitude. Euler is enough.

One more ingredient: real systems have *lag*. The sensor takes time to register a change. The hypothalamus takes time to compute the error. The sweat glands take time to ramp up. We can approximate this crudely by saying the effector responds not to the current deviation but to the deviation it saw *τ* seconds ago, where *τ* (the Greek letter tau, pronounced like *tow* as in towrope) is the delay. A loop with high gain and a long delay will overshoot the set point on the way back and ring for a few cycles before settling. You have probably seen this in a poorly-tuned home thermostat — the system overshoots, the furnace cuts off, the temperature drops back past the target, the furnace fires again. Same mathematics.

![Temperature vs](../images/00-how-to-use-the-simulations-fig-03.png)
*Figure 1.3 — Temperature vs*

---

## The governing files

Before you write any code, you write three text files. They go in the same folder as the simulation. The LLM reads them every time you prompt it. This is the entire "framework" — three plain-text files, nothing installed.

**CLAUDE.md** is the coding constitution. It tells the LLM what kind of code to produce.

```markdown
# CLAUDE.md — A&P Simulation Coding Constitution

## Stack
- Single .html file per simulation. No external build step.
- D3 v7 loaded from CDN: <script src="https://d3js.org/d3.v7.min.js"></script>
- Plain HTML, CSS, and JavaScript. No frameworks. No npm.

## Visualization
- All drawing happens inside one <svg> element.
- Use D3 selections, scales, and transitions.
- Time-series charts use d3.scaleLinear, d3.line, d3.axisBottom/Left.
- Feedback-loop diagrams use d3.linkHorizontal or simple SVG paths for
  arrows between labeled nodes (sensor, control center, effector).
- Animated transitions on parameter change: duration 250 ms.
- Real-time simulations advance using d3.timer.

## Interaction
- Parameter controls are <input type="range"> sliders.
- A <div id="readout"> displays current parameter values to two
  significant figures.
- Sliders update the simulation in real time via an `input` listener.

## Physiology
- Every simulation models a named physiological process.
- Variables in the code use physiology names (T, T_set, k, tau).
- A short comment at the top of every <script> block states the
  physiological claim the simulation is making and its limits.

## Verification
- Every simulation includes a console.log block printing the result of
  one physiology check the moment the file loads.
- The physiology check is a one-line falsifiable claim.
```

**DESIGN.md** is the visual constitution. It says nothing about physiology — it says how things look. The separation matters: you change a color scheme without touching the physiology. You fix a physiology bug without touching the colors.

```markdown
# DESIGN.md — Visual Constitution

## Color palette (physiology-coded)
- Arterial blood:   #c1121f
- Venous blood:     #023e8a
- Nerve signals:    #ffd60a
- Hormones:         #7b2d8b
- Muscle:           #e76f51
- Bone:             #f5f2ee (gray outline #adb5bd)
- Lymph:            #2d6a4f
- Epithelial:       #e9c46a
- Connective:       #90e0ef

## Chart styling
- Time series: line color #1a1714 on white #ffffff.
- Set-point reference line: dashed, #adb5bd at 1 px.
- Axis labels: 12 px sans-serif. Title: 16 px.
- Grid lines: #e9ecef at 1 px.

## Sliders
- 320 px wide. Labels above. Current value to the right.

## Layout
- SVG canvas: 720 px wide x 400 px tall.
- Margins: top 30, right 30, bottom 50, left 60.

## Type
- system-ui, -apple-system, sans-serif.
```

**PROJECT.md** is the state file — the only one you edit chapter to chapter.

```markdown
# PROJECT.md — A&P Simulation Workshop

## Built so far
- (chapter, file, what it models)

## In progress
- 00-homeostasis-loop.html — body temperature regulation

## Next
- 01-cell-membrane-transport.html

## Conventions
- File naming: NN-slug.html
- Each file is self-contained.
- Every file has a one-line // CLAIM: comment at the top.
```

| Item | Meaning |
| --- | --- |
| File / Controls / Does not control | showing CLAUDE.md governs code generation, DESIGN.md governs appearance, PROJECT.md governs state, with zero overlap between columns |

---

## The four-move prompt

Most students paste vague requests into Claude — *"make me a homeostasis simulation"* — and then spend an hour fighting the output. The four-move structure skips that hour. It is not magic; it is just specificity, organized.

**Show.** Point at the governing files. *"Read CLAUDE.md and DESIGN.md. Conform to them."* Attach them if you are working in claude.ai. If you are working in Claude Code or Cowork, they are already on disk.

**Say.** One paragraph in physiological terms. What variable. What equation. What sliders. What the chart shows.

**Constrain.** The rules beyond what CLAUDE.md already establishes. Integration step size. Playback speed. What each element's color should encode.

**Verify.** One falsifiable physiology claim the simulation must satisfy. Not *"make sure it looks right"* — a statement that is either true or false when you read the chart and the console.

Used together, these four moves are reliably more effective than any one of them alone. The LLM is very good at following specific instructions. It is unreliable when the instructions are absent.

---

## A worked example

Here is the actual prompt for `00-homeostasis-loop.html`:

> **Show:** Read CLAUDE.md and DESIGN.md from this project. Conform to them.
>
> **Say:** Build `00-homeostasis-loop.html` — a body-temperature regulation simulator. The model is a single-variable negative feedback loop *dT/dt = disturbance − k · (T − T_set)*, where *T* is core temperature in °C, *T_set* is the set point, *disturbance* is an external heating or cooling rate in °C/min, and *k* is the loop gain in 1/min. The effector responds to the deviation as it was *τ* seconds ago (a simple delay). Sliders control *T_set* (35.0 to 39.0, default 37.0), disturbance (−0.5 to +0.5 °C/min, default +0.2), *k* (−0.5 to +1.0 per min, default +0.5), and *τ* (0 to 60 s, default 10). The chart plots *T* versus time over 30 simulated minutes, with *T_set* drawn as a dashed reference line. Above the chart, draw a loop diagram with three nodes — *Thermoreceptors* (sensor), *Hypothalamus* (control center), *Sweat glands / vessels* (effector) — connected by arrows.
>
> **Constrain:** Use Euler integration with *dt = 1 s*. Run in real time at 60× speed, advancing via `d3.timer`. Color the temperature line arterial blood #c1121f. Color the set-point dashed line gray #adb5bd. Color the effector node muscle #e76f51 when warming, venous blood #023e8a when cooling, and pulse its radius in proportion to current response magnitude. Use nerve-signal yellow #ffd60a for the arrows between nodes. The readout shows *T_set*, current *T*, disturbance, *k*, and *τ* to two significant figures. Single self-contained HTML file, no external dependencies except D3 v7 from CDN.
>
> **Verify:** Physiology check — (1) when *k > 0* and disturbance is held nonzero, *T* must reach a steady-state offset of approximately *disturbance / k* above the set point; (2) when *k > 0* and the disturbance is removed, *T* must return to within 0.1 °C of *T_set* within 10 simulated minutes; (3) when *k < 0*, *T* must diverge monotonically from *T_set*. Print all three outcomes to the console after every parameter change. Add a comment at the top: `// CLAIM: A single-variable negative feedback loop with delay predicts a damped return to set point; positive gain stabilizes, negative gain destabilizes.`

Paste that. Wait. Save the file. Double-click it.

You should see a red temperature line wobbling in a narrow band around 37.0 °C. Push the disturbance slider to +0.4 °C/min. The line climbs, the effector node pulses harder, and the line settles a fraction above 37.0 °C rather than running away. Push the disturbance back to zero. The line glides back down.

Now drag *k* into negative territory — say, −0.2. The line runs away from the set point in whichever direction the disturbance points. It does not stop. Push *k* back to +0.5. The line damps back down.

Open the browser's developer console (Cmd-Option-J on Mac, Ctrl-Shift-J on Windows). The console should print the three verification outcomes after each run. If the steady-state offset under *disturbance = 0.2* and *k = 0.5* is not near 0.4 °C, the simulation is wrong. Tell the LLM exactly what failed: *"With disturbance 0.2 and k 0.5, the steady-state offset should be 0.4 °C but I'm seeing 0.6 °C. Fix it."* The Verify clause turns vague complaints into precise bug reports.

Check the math once. At steady state, *dT/dt = 0*:

$$0 = \text{disturbance} - k \cdot (T_{\text{ss}} - T_{\text{set}})$$
$$T_{\text{ss}} = T_{\text{set}} + \frac{\text{disturbance}}{k} = 37.0 + \frac{0.2}{0.5} = 37.4 \text{ °C}$$

The body settles four-tenths of a degree above target. That is the price of proportional control under a persistent disturbance — exact tracking requires either infinite gain or a more sophisticated controller that integrates the error over time.

Now sweep *τ* from 0 to 60 s with *k = 1.0*. At low *τ* the line damps cleanly to the set point. As *τ* grows, the line starts to overshoot and ring. You have just observed why a fast reflex with a long conduction delay is dangerous: the system corrects past its target, then has to correct back, and every cycle of overshoot is a period during which the regulated variable is outside its intended range.

![Single run with k = 1](../images/00-how-to-use-the-simulations-fig-04.png)
*Figure 1.4 — Single run with k = 1*

---

## What this model gets wrong, and why that matters

The simulation is wrong about a lot of real physiology. This is not a bug — it is the point.

Real body temperature regulation has multiple effectors: sweating, vasodilation, behavioral thermoregulation, shivering, brown-fat thermogenesis. Each has a different threshold, a different gain, and a different time constant. The model collapses all of these into a single proportional response with a single *k*. Real thermoreceptors are not a single sensor measuring a single *T*; peripheral receptors in the skin and central receptors in the hypothalamus are weighted differently and respond to rate-of-change as well as absolute temperature. Real effectors saturate — you can only sweat so fast. The model's effector has no ceiling.

Naming these simplifications is not modesty; it is honesty about what the model is for. The model captures *the signature behavior of negative feedback*: damped return to set point, steady-state offset proportional to disturbance divided by gain, ringing when lag is large. Those signatures appear in blood pressure regulation, glucose regulation, respiratory rate regulation. The model is not faithful to the details of any one of those systems. It is faithful to the *architecture* that all of them share.

Three failure modes to watch for as you use simulations throughout this book.

*"The simulation IS the physiology."* No. The simulation is a hypothesis about the physiology, encoded in a few lines of math. Every parameter is a stand-in for something a real body does not actually know about itself. *T_set* does not exist as a number stamped on any structure in the hypothalamus; it emerges from the collective activity of many neurons and shifts with circadian phase, fever, sleep, and the menstrual cycle. *k* is shorthand for the combined gain of half a dozen effector systems. The simulation tells you what would happen if the body worked the way the equation says it works. Real bodies do not consult the equation.

*"More parameters = more realistic."* No. More parameters means more places to be wrong. A model with twelve parameters and one buried `circadianPhaseShift` constant is not more realistic; it is more obscure. The smallest model that captures the behavior you care about is the best teaching tool, because you can see exactly what each part is doing. Add complexity only when you can articulate what new question the new parameter answers.

*"If it runs, it's correct."* Code that runs has passed a syntax check, not a physiology check. A simulation that produces a smooth curve from arbitrary parameter choices is still running. The Verify clause is the firewall. A falsifiable claim — *"when k > 0 the temperature returns to set point"* — is either satisfied by the chart or it is not. The chart does not care whether the JavaScript compiled cleanly.

One more, subtler: *"The LLM understands the physiology."* The LLM understands patterns in text about physiology. Sometimes those patterns align with the underlying mechanism. Sometimes they produce output that looks right but encodes a sign flip, a unit confusion, or a steady-state condition imposed where the system should be transient. When you ask the LLM to write a simulation, you are delegating the typing, not the physiological judgment. The physiological judgment lives in the Verify clause. You write that clause. Not the LLM.

---

## LLM Exercise — Build your homeostasis simulator

Create the three governing files using the templates above. Save them in a folder. Then paste this prompt at Claude:

```
Show: Read CLAUDE.md and DESIGN.md from this project. Conform to them.

Say: Build 00-homeostasis-loop.html — a body-temperature regulation
simulator. The model is a single-variable negative feedback loop
dT/dt = disturbance - k * (T - T_set), where T is core temperature
in degrees Celsius, T_set is the set point, disturbance is an external
heating or cooling rate in C/min, and k is the loop gain in 1/min.
The effector responds to the deviation as it was tau seconds ago
(a simple delay). Sliders control T_set (35.0 to 39.0, default 37.0),
disturbance (-0.5 to +0.5 C/min, default +0.2), k (-0.5 to +1.0 per
min, default +0.5), and tau (0 to 60 s, default 10). The chart plots
T versus time over 30 simulated minutes, with T_set drawn as a dashed
reference line. Initial T = 37.0 C. Above the chart, draw a loop
diagram with three nodes — Thermoreceptors (sensor), Hypothalamus
(control center), Sweat glands / vessels (effector) — connected by
arrows.

Constrain: Use Euler integration with dt = 1 s. Run in real time at
60x speed (30 simulated minutes plays in 30 wall-clock seconds),
advancing via d3.timer. Color the temperature line arterial blood
#c1121f. Color the set-point dashed line gray #adb5bd. Color the
effector node muscle #e76f51 when warming, venous blood #023e8a when
cooling, and pulse its radius in proportion to the current response
magnitude. Use nerve-signal yellow #ffd60a for arrows between nodes.
The readout shows T_set, current T, disturbance, k, and tau to two
significant figures. Single self-contained HTML file, no external
dependencies except D3 v7 from CDN.

Verify: Physiology check — (1) when k > 0 and the disturbance is held
nonzero, T must reach a steady-state offset of approximately
disturbance / k above the set point and stay there; (2) when k > 0
and the disturbance is then removed, T must return to within 0.1 C of
T_set within 10 simulated minutes; (3) when k < 0, T must diverge
monotonically from T_set. Print all three outcomes to the console
after every parameter change. Add a comment at the top:
// CLAIM: A single-variable negative feedback loop with delay predicts
// a damped return to set point; positive gain stabilizes, negative
// gain destabilizes.
```

Once the file runs, work through these probes:

**The steady-state test.** Set *T_set = 37.0*, disturbance = +0.2, *k = +0.5*, *τ = 10*. Read the steady-state temperature off the chart. Then set *k = +1.0*. The offset should halve. Set *k = +0.25*. It should double. Does the chart match *T_ss = T_set + disturbance / k*?

**The negative-gain test.** Set *k = −0.2* with any nonzero disturbance. The temperature should diverge. Does it diverge faster when the disturbance is larger? Flip the sign of the disturbance — does the divergence flip direction? What does this tell you about why positive feedback in physiology is reserved for events that complete fast?

**The lag test.** Hold *k = +1.0* (high gain). Sweep *τ* from 0 s to 60 s. At what value does the temperature start to overshoot on the return? What happens as *τ* grows further? Why might a fast reflex with a long conduction delay be dangerous?

**Extension prompt.** Once the basic simulator works, add a second regulated variable — blood glucose — side by side with temperature:

```
Extension: Modify 00-homeostasis-loop.html so the chart shows two
regulated variables simultaneously — body temperature (arterial blood
#c1121f) and blood glucose (hormones #7b2d8b). Each variable has its
own set of four sliders (set point, disturbance, k, tau). Default
glucose set point is 90 mg/dL with disturbance of +1.0 mg/dL/min,
k = +0.05 per min, tau = 30 s. Both variables share the same time
axis but use separate y-axes (temperature on the left in C, glucose
on the right in mg/dL). Verification: with both loops at positive
gain and steady disturbances, each variable independently reaches
T_ss = T_set + disturbance/k. When either k is set to zero, that
variable drifts linearly with its disturbance. When either k goes
negative, that variable diverges.
```

This is the simulation you will reach for when the endocrine chapters arrive. The glucose loop becomes the insulin-glucagon axis. The math is unchanged. Only the names of the sensor, control center, and effector change.

---

## Exercises

| Item | Meaning |
| --- | --- |
| of the four failure modes | Name / What it assumes / Why it fails |

**Warm-up 1.** The steady-state formula says *T_ss = T_set + disturbance / k*. Without running the simulator, calculate the expected steady-state temperature for each of the following parameter sets. Then run the simulator and check your answers against the chart. *(a)* T_set = 37.0, disturbance = +0.3 °C/min, k = +0.6 per min. *(b)* T_set = 36.5, disturbance = −0.2 °C/min, k = +0.4 per min. *(c)* T_set = 37.0, disturbance = +0.1 °C/min, k = +1.0 per min. For each case, state whether the regulated temperature is above or below the set point, and explain in one sentence why proportional control cannot achieve exact tracking under a persistent disturbance. *Tests: deriving steady-state offset from the feedback equation.*

**Warm-up 2.** With k = +0.5 per min and τ = 0 s, apply a step disturbance of +0.4 °C/min at t = 0 and hold it constant. Predict (on paper) the approximate time constant for the return toward steady state. The time constant for this system is 1/k — the time after which the gap between the current temperature and the steady-state temperature has closed to about 37% of its initial value. Check your prediction against the simulator by reading the temperature at t = 2 min after the step. *Tests: connecting the gain parameter to loop dynamics.*

**Application 1.** A patient has an infection that raises the hypothalamic set point from 37.0 °C to 38.5 °C — this is how fever works: the set point shifts, the loop is still functioning, the body is now regulating to a higher target. In the simulator, implement this by changing T_set from 37.0 to 38.5 while keeping all other parameters constant (disturbance = 0, k = +0.5, τ = 10 s). Describe what the temperature curve does. Does it look like a system that is malfunctioning, or a system that is working correctly toward a new target? What does this tell you about the difference between fever and hyperthermia? *Tests: distinguishing a set-point shift from a control-loop failure.*

**Application 2.** In exertional heat illness, the effector response saturates — the sweat glands cannot cool fast enough to offset the heat load from strenuous exercise in a hot environment. Model this as a case where the effective gain k drops from +0.5 to near zero because the effectors are maxed out. Set disturbance = +0.5 °C/min and sweep k from +0.5 down to +0.05. Observe and record the steady-state temperature at each k value. At what k does the steady-state temperature exceed 40 °C (clinically dangerous hyperthermia)? What does this tell you about why heat illness can escalate rapidly once the effector capacity is overwhelmed? *Tests: applying the steady-state formula to a physiological failure mode.*

**Application 3.** Explore the interaction between gain and delay. Hold disturbance = +0.2 °C/min and run three separate trials: *(a)* k = +0.3, τ = 30 s; *(b)* k = +0.7, τ = 30 s; *(c)* k = +0.7, τ = 60 s. For each trial, describe whether the temperature overshoots, rings, or damps cleanly to steady state. From your observations, complete this sentence in your own words: "A feedback loop becomes oscillatory when \_\_\_\_ is large relative to \_\_\_\_." *Tests: identifying the conditions that produce ringing and relating them to the gain-delay interaction.*

**Synthesis 1.** The chapter introduces four failure modes for simulation-based reasoning: the simulation IS the physiology, more parameters = more realistic, if it runs it's correct, and the LLM understands the physiology. Choose any two of these and write a concrete example of each one, set in the context of the temperature simulator you built. The example should describe a specific wrong conclusion a student could reach, explain what physiological reality the simulation does not capture, and state what additional evidence or reasoning would correct the error. *Tests: applying critical analysis of model limitations to a concrete simulation.*

**Synthesis 2.** The same feedback equation governs blood glucose regulation, with the insulin-glucagon axis playing the roles of sensor, control center, and effector. A fasting healthy adult has a glucose set point near 90 mg/dL; a typical post-meal disturbance might push glucose toward +1.5 mg/dL per minute for roughly 20 minutes before being absorbed. Using the steady-state formula, estimate what gain k (in units of per minute) would be needed to hold the peak steady-state glucose below 120 mg/dL under a persistent disturbance of +1.0 mg/dL per minute. State clearly what biological structure or process corresponds to each parameter in the equation. *Tests: transferring the feedback framework from temperature to a second physiological system.*

**Challenge.** The chapter's model uses a single effector with a single gain k. Real temperature regulation uses multiple effectors in sequence: cutaneous vasodilation activates first (threshold ~37.0 °C), then sweating (~37.2 °C), then behavioral responses (~37.5 °C), each with a different gain. Write a four-move prompt that would ask an LLM to modify the simulator to implement two sequential effectors — vasodilation alone active below a threshold T1, both vasodilation and sweating active above T1 — each with its own gain parameter. Include a Verify clause with a specific falsifiable claim about how the combined system should behave differently from the single-effector model when the disturbance is large enough to exceed the first effector's capacity but not the second's. You do not need to run the simulation — the prompt itself is the deliverable. *Tests: composing a specification-level description of a more realistic physiological model and embedding a falsifiable verification clause.*

---

Chapter 1 asks the anatomical question this chapter deferred: what structures play sensor, what play control center, what play effector, and how are they organized — at the levels of cells, tissues, organs, and systems — to produce the stability we just modeled? Carry the simulator with you. The first time the chapter mentions the hypothalamus, you will already know its job in the loop.

---

**What would change my mind.** The four-move prompt structure would lose its claim to being a genuine teaching object — rather than ceremonial scaffolding — if the same prompt, in any order or none at all, reliably produced runnable simulations. My claim is that the Show / Say / Constrain / Verify sequence does meaningful work: Constrain prevents the LLM from making architectural choices you did not intend; Verify converts vague correctness into a falsifiable test. If a controlled comparison showed equivalent first-pass success rates with and without the structure, on simulations of comparable complexity, I would revise the method or drop it.

**Still puzzling.** I do not know whether students with no prior coding background can read the JavaScript an LLM produces well enough to spot a physiology-coded variable being used incorrectly — and that gap, between *running the file* and *reading the file*, is the real test of whether this method teaches or just produces outputs. I also do not know how much of the apparent agreement between simple proportional-feedback models and real physiological regulation reflects genuinely linear control versus a feature of how variables are measured at time scales that average over faster nonlinear dynamics. Both of those are open questions for later chapters.

---

**Tags:** negative-feedback, homeostasis-set-point, D3-v7, Brutalist-files, four-move-prompt
