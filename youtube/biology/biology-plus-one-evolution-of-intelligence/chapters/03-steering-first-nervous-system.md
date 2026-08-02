# Chapter 3 — Steering: The First Nervous System

Here is the experiment. A centimeter of damp agar. A stripe of copper sulfate painted across it — copper is poison, every sensor the worm has that detects it is screaming. And a *C. elegans*, about a millimeter long, pale as glass, approaching the stripe.

The worm hits the copper. It recoils. It tries again. It recoils again. And then — if it has not eaten in several hours — it crosses.

I want to stay with that crossing for a moment, because it is the smallest version of something enormous. You cannot predict what the worm will do by listing what the worm's sensors are detecting. The copper concentration is the same. The sensors are the same. The motor neurons are the same. Two worms at the same stripe do two different things, because one ate recently and one did not. The behavior is not a function of the environment. It is a function of the environment *and a variable the environment cannot see.*

A bacterium cannot do this. You can predict what a bacterium will do at a copper gradient from the gradient alone. A thermostat cannot do this. A Roomba cannot do this. But a worm with 302 neurons — a worm whose every single synapse has been catalogued, named, and mapped — can. And because the entire wiring diagram exists on paper, we can say exactly which wires make it possible.

That is what this chapter is about. Not intelligence in some grand sense. The floor. The minimum architecture for changing your mind.

---

Before the neurons, there is a geometry. And the geometry does most of the cognitive work before a single cell fires.

Think about what it means to be radially symmetric — a hydra, a jellyfish, presenting the same face to the world in all 360 degrees. If such an animal wants to move toward food, the navigation problem it faces is *which direction?* It has to integrate sensory information from everywhere simultaneously and resolve it to a heading. That is a hard problem. You need a lot of machinery to solve it.

Bilateral symmetry solves the problem by anatomy. Once you have a left and a right that mirror each other, you necessarily have a front and a back. Sensors cluster at the front. The animal moves in the direction the sensors point. The navigation problem collapses from *which of 360 degrees?* to *keep going, or turn?* Two options. Forward and not-forward. That is the question the first nervous systems were built to answer. Not vision, not language, not planning — just whether to persist in a direction or change it.

This simplification was apparently so powerful that it happened once. Every bilateral animal on Earth — every worm, insect, fish, frog, bird, and mammal — descends from a single ancestor that made this transition roughly 570 million years ago in the late Ediacaran seafloor. Every brain that has ever existed is an elaboration of a solution to a problem first posed in Cambrian mud: *forward, or not forward?*

*C. elegans* sits about as close to that original solution as any animal we can study. Its nervous system organizes around a nerve ring encircling the throat just behind the head. This is the worm's brain. It is not impressive — 302 neurons, roughly 7,000 chemical synapses, fitting in a structure smaller than the head of a pin. But it does something the bacterium's chemotaxis system from the last chapter cannot do. It integrates multiple, conflicting signals and produces a coherent directional decision that can be tuned by internal state. Each of those words is doing real work. Let me go through them.

---

Smell coffee. Hear a car alarm. Feel heat from a radiator. You do not experience these as one undifferentiated blob of sensation. You know, before you have time to think about it, that one is a smell and one is a sound and one is warmth. That separation is not learned. It is built into the architecture. Separate sensors for separate stimulus categories, each connected to circuits that interpret the signal in light of its source. Neuroscientists call this the labeled-line principle: each sensory neuron is dedicated to one stimulus type, and the *meaning* of its firing is carried by the identity of the wire it travels along, not by some code at the destination.

*C. elegans* has labeled lines in their simplest possible form. The AWC neurons detect volatile attractants — diacetyl, isoamyl alcohol, the smells of the bacteria the worm eats. When AWC fires, its wire terminates at an interneuron called AIY, the most heavily connected cell in the worm's brain, in a way that biases the worm toward longer runs and fewer turns. The interpretation "food: approach" is not computed anywhere. It is built into the connection. The ASH neurons detect nose-touch, high osmolarity, and heavy metals including copper. When ASH fires, its wire terminates at AIY in a way that biases the worm toward reversals and sharp turns. The interpretation "danger: avoid" is, again, in the wire.

This is a tradeoff a 302-neuron animal has to make. You cannot afford a flexible general-purpose cortex when you have fewer neurons than a 1970 chip has transistors. What you can afford is a set of pre-labeled wires that carry their interpretation with them, all terminating at a small integration node — AIY — whose job is not to understand the signals but to tally them into a single binary output: run, or pirouette.

The crucial thing to notice is that labeled lines with hardwired valences are not a limitation of primitive nervous systems. They are a design principle that persists at every scale. Your own brainstem runs the same logic. Certain stimuli mean *bad* through connections established before you were born. Pain feels like pain because of which wires the pain-sensitive neurons connect to, not because of anything intrinsic to the signal. The labeled line is the cognitive atom — the irreducible unit from which every more elaborate judgment is built up.

---

Now here is something worth pausing on. The run-and-pirouette strategy the worm uses to climb a chemical gradient is, at the algorithmic level, identical to what the bacterium from Chapter 2 does. The bacterium alternates between running straight and tumbling to reorient. When concentration is rising — when it is heading toward food — it suppresses tumbles and runs longer. When concentration is falling, it tumbles more, reorienting at random until chance points it uphill. The result is a biased random walk that climbs the gradient without the cell ever computing a direction.

The worm does the same thing with different vocabulary. Instead of runs and tumbles, it has runs and pirouettes — short bursts of tight turning including reversals and omega bends, where the body folds into the shape of the Greek letter Ω. The pirouette is the worm's tumble. The rule governing pirouette initiation is the time-derivative of attractant concentration: heading up the gradient suppresses pirouettes, heading down the gradient triggers them. Each pirouette randomizes heading. Over many pirouettes, the worm drifts uphill. The algorithm is identical.

So far the worm is just a bacterium with 302 neurons. What makes it genuinely different is what happens when the gradient is not the only thing going on.

The worm has multiple attractants and repellents. Their signals arrive simultaneously at AIY. When it smells diacetyl and detects copper at the same time, both labeled lines are firing. AWC says *forward*. ASH says *reverse*. AIY has to produce a single output. The bacterium has no answer to this. It has essentially one sensor channel and one response. The worm has competing sensors, and the competition has to be resolved. And the mechanism that resolves it is not in the labeled lines. It is in something slower.

---

In 2000, Sawin, Ranganathan, and Horvitz published findings that reframed how biologists thought about dopamine — specifically the worm's dopamine. When *C. elegans* encounters a bacterial lawn, it slows down. This slowing is mediated by dopamine released from mechanosensory neurons that physically contact the bacteria. Without dopamine, the worm runs straight through excellent food without pausing. With dopamine, it dwells and eats. Dopamine, half a billion years before any vertebrate brain existed, is already the signal for *food is here — shift from searching to exploiting.*

The same paper showed something easy to miss. When the worm is food-deprived for several hours and then placed on food, the slowing response is dramatically enhanced — but not by more dopamine. By serotonin, released from neurons that signal something close to satiety. A starved worm returned to food gets a larger serotonergic response than a fed worm. The serotonin translates into longer dwelling, slower locomotion, more eating.

What is happening architecturally is this: dopamine and serotonin are not fast neurotransmitters carrying specific messages along specific wires. They are broadcast molecules. They diffuse broadly through the fluid surrounding the worm's neurons, bind to receptors on many cells at once, and change those cells' properties. A neuromodulator does not transmit a message. It changes the *gain* on an entire circuit.

When serotonin is high — the worm has been starving and is finally on food — the gain on the AWC attractive pathway increases. The gain on the ASH repellent pathway decreases. The same copper concentration that turns away a well-fed worm becomes tolerable to a starved one. Nothing in the environment changed. Nothing in the sensors changed. What changed is the weighting function.

Let me make that concrete. The worm's integration node, AIY, is summing competing signals. At a coarse level of abstraction we can write it as:

**Decision = w(food) · S(food) − w(repellent) · S(repellent)**

If the decision is positive, the worm runs forward. If negative, it pirouettes. The signals S are the firing rates of the labeled-line sensors. The weights w are not fixed. They are set by neuromodulator state.

With the same sensor inputs — *S*(food) = 1.0, *S*(repellent) = 1.0 — a well-fed worm runs at baseline weights of approximately 0.4 and 0.8. Decision: 0.4 − 0.8 = −0.4. Pirouette. No crossing.

The same worm after several hours without food. Serotonergic priming has shifted the weights toward approximately 0.9 and 0.4. Decision: 0.9 − 0.4 = +0.5. Forward run. Crossing.

This is not a metaphor. This is, at a coarse level, what the data show happening. A slow-timescale internal variable — the concentration of broadcast neuromodulators — re-weights the integration of fast-timescale sensory signals. That is what the neuromodulatory system does. That is what it is *for.*

And here is the thing I want you to see clearly. The worm at the copper line is not running a more complicated reflex than the bacterium. It is doing something qualitatively different. The bacterium's behavior is determined by its sensory inputs. The worm's behavior is determined by its sensory inputs *and an internal state that has its own history.* The internal state is real, encoded in chemistry, and it is not recoverable from any snapshot of the current environment. You have to know when the worm last ate. That is a new kind of system.

---

In 2002, Ishihara and colleagues published a result I think is one of the most philosophically pointed findings in invertebrate neuroscience. They identified a small secreted protein called HEN-1, released by certain interneurons in the worm, required for it to weigh attractive odors against repellent chemicals correctly. Without HEN-1, the worm can still smell diacetyl. It still approaches food. It can still detect copper. It still recoils. What it cannot do is hold both signals simultaneously and produce a coherent trade-off. HEN-1 mutants wander into copper while chasing food. They retreat from food while fleeing copper. They cannot resolve the conflict.

Think carefully about what this tells us. The machinery for resolving competing signals is *separable from the sensors that generate them.* You can have perfectly functional sensors and still be unable to trade them off against each other. You can disable only the integration machinery and lose the decision without losing the sensation. Sensing and deciding are not the same operation, even in a 302-neuron animal.

The HEN-1 mutant has 302 neurons, all of them working, and cannot make this decision. An animal with no such protein is not less sensitive — it is architecturally incomplete in a specific way. The broken component is not a sensor and not a motor. It is the thing in between that holds two incompatible signals and produces one behavior.

---

There is one more finding worth dwelling on, because it is counterintuitive and it is the bridge to everything that follows.

In 1995, Mori and Ohshima showed that when *C. elegans* is raised at a particular temperature *while eating*, and then placed on a thermal gradient, it migrates toward the temperature it was raised at. The thermosensory neuron AFD acts as if it has stored the cultivation temperature as a set-point.

Here is the strange part. If you deprive the worm of food during cultivation at that temperature, the migration disappears. Raise the worm at 20°C without food, then place it on a gradient — it no longer seeks 20°C. The thermal set-point did not form.

The temperature memory is conditional on the food association. The worm does not learn to want warmth in the abstract. It learns to want the temperature that, in its experience, meant food was available. There is no food signal in the test trial. Nothing in the present moment justifies the migration. The worm seeks the temperature because it remembers that temperature as good.

This is a preference — a behavioral disposition toward a value that depends on prior experience and is not reducible to the current sensory state. Something that was neutral became good, and the goodness endured beyond the circumstances that created it. The molecular machinery underlying it depends on a transcription factor called CREB, which, when activated by sustained signaling at a synapse, enters the cell nucleus and turns on genes that build new synaptic machinery. CREB is roughly the molecular bridge between "this synapse just fired a lot" and "this synapse should now be permanently stronger." The same pathway Eric Kandel characterized in the sea slug *Aplysia* — the work that won him the Nobel Prize in 2000. We will go much deeper into Kandel in Chapter 4. The point for now is that the worm is carrying ancient code. The mechanism that lets it form a conditional temperature preference is the same mechanism that underlies certain forms of long-term memory in vertebrates including you.

---

Let me now say what the worm has assembled, because I want to carry it forward as a checklist.

The architecture has six components. Each is necessary. None is sufficient alone.

A bilateral body plan that collapses the navigation problem from *360 degrees* to *forward or turn* — a cognitive simplification achieved by anatomy, before any neuron fires. Labeled-line sensors that carry their interpretation in the wiring, not in any central code. A temporal comparison — the dC/dt logic that converts the current moment into *am I getting closer or farther?* Mutual-inhibition motor circuits that produce coherent all-or-nothing outputs: run or pirouette, not half of each. A neuromodulatory layer — at minimum dopamine and serotonin — encoding internal state on a timescale slower than neural activity, making the food-copper trade-off possible. And associative plasticity: the CREB-dependent ability to re-weight labeled lines based on outcomes, so that experience can update the valence of a stimulus.

Take any one out and the worm degrades in a specific, predictable way. Disable the labeled lines and the worm cannot interpret its sensors. Eliminate neuromodulation and it becomes a reflex machine — same output regardless of internal state. Block associative plasticity and it cannot learn from experience. Remove the integration machinery — the HEN-1 case — and it cannot resolve conflict. These are not six features of a worm. They are six features of a system capable of changing its mind.

Now compare this to a Roomba.

Brooks's subsumption architecture, which he proposed in 1986 and which eventually became the Roomba's behavioral logic, is genuinely similar to the worm's at the organizational level. Stacked sensory-motor reflexes, higher layers suppressing lower ones when activated, no internal world model required. Brooks was right that most intelligent-seeming behavior does not require a map. His robot descended from that insight has cleaned tens of millions of rooms.

The Roomba has sensors. It has labeled-line equivalents — each sensor has a fixed handler in firmware. It has something like temporal comparison in its dust-sensor history. It has priority rules that arbitrate between competing behaviors. The first four components on the checklist are, at least roughly, present.

The gap is in five and six. The Roomba does not have a neuromodulator equivalent. When its bin is full, it signals for help. It does not change its behavior *across the board* in response to internal depletion the way a hungry worm recalibrates every aspect of its cost-benefit calculus. And the Roomba forms no associative preferences. If it repeatedly fails to clean a particular corner, it does not update the valence of that corner in any enduring way. Most importantly: when genuinely competing signals arise — clean this area versus avoid this obstacle — it falls back on a fixed priority ordering baked into firmware. Obstacle avoidance always trumps cleaning. That ordering never updates. The worm's ordering updates every few hours based on its internal state. That is the difference.

I want to be precise about the claim. The Roomba is not less *sophisticated* in some vague sense. It is architecturally incomplete in two specific ways. It is missing the gain-setting layer that makes behavior state-dependent, and it is missing the plasticity layer that lets experience rewrite the weights. Without five and six, you have a system that responds. With all six, you have a system that decides.

---

I should be careful about what I am not claiming.

*C. elegans* does not build a spatial map. It navigates gradients, not spaces. Remove the gradient and place food at a fixed location and the worm cannot learn to go there from memory. It will find the food each time by running the temporal-comparison algorithm from scratch, as if it had never been there. The worm's memory windows are short. The longest associative learning — the temperature conditioning — operates over hours. There is nothing resembling episodic memory, nothing resembling the capacity to recall a specific past event and use it to plan a specific future action. The worm does not plan. It does not imitate. It cannot learn a behavior by watching another worm perform it.

What I am claiming is that the worm's nervous system, as documented, represents the minimum architecture for state-dependent decision-making. Below this architecture — the bacterium, the slime mold, the Roomba — you have systems that respond. With this architecture you have a system that decides, in the operationally meaningful sense: a behavioral output that cannot be predicted from sensory inputs alone, that requires knowledge of internal state, and that represents a weighting of competing information according to a cost-benefit calculation that is genuinely dynamic.

The floor is real. And it is documented in a specific wiring diagram in a 1986 paper out of the MRC Laboratory in Cambridge, the product of twelve years of slicing worms into thin ribbons with a diamond knife, photographing each ribbon with a transmission electron microscope, and tracing every neuron and every synapse by hand across thousands of overlapping micrographs. John White, Eileen Southgate, Nichol Thomson, and Sydney Brenner. The first complete connectome of any animal nervous system in history. Four decades later it is still one of only two that exist.

The worm in the dish is not a stepping stone to something more important. It is the worked example of the foundation. A decision — a genuine, state-dependent, experience-informed decision — fits in 302 cells.

In a centimeter of soil, a millimeter at a time, half a billion years before anyone was watching.

---

## LLM Exercise — Build and Run *03-celegans-decision.html*

**What you're building:** A single self-contained HTML file that simulates the worm's decision at the copper sulfate line. You will use it to make the chapter's central argument visible and interactive, and you will extend it in Chapter 4 when associative plasticity enters the story.

**Tool:** Claude Code (preferred), or any Claude or ChatGPT session with file output enabled.

---

The build proceeds by the four-move protocol used for every LLM-assisted build in this book: **Show / Say / Constrain / Verify.**

**SHOW** — give the model the chapter so its build is anchored to the actual content, not a generic guess:

```
I'm building an interactive teaching widget for a textbook chapter on
C. elegans decision-making. The chapter is pasted below. The target
file is 03-celegans-decision.html — a single self-contained HTML file
with embedded CSS and JavaScript, no external libraries, no build step.

[PASTE THE CHAPTER, or at minimum the decision-math and HEN-1 sections]

Build the interactive described at the end of the chapter. Constraints follow.
```

**SAY** — give the model the exact behavioral requirements:

```
1. Two sliders (S_food, S_repellent), each 0.0 to 2.0, with 0.05
   increments and a visible numeric readout.
2. Internal-state selector: WELL-FED or STARVED.
3. HEN-1 toggle: PRESENT or ABSENT.
4. Weights:
   - Well-fed:  w_food = 0.4, w_repellent = 0.8
   - Starved:   w_food = 0.9, w_repellent = 0.4
5. Decision = w_food * S_food - w_repellent * S_repellent.
   Render the equation with the current numbers substituted in,
   then the computed value to two decimals.
6. Behavioral output rule:
   - Decision > 0.1:           "FORWARD RUN — worm crosses"
   - Decision < -0.1:          "PIROUETTE — worm retreats"
   - -0.1 <= Decision <= 0.1:  "INDECISION — alternating"
7. Comparison panel: a small table showing the SAME S_food and
   S_repellent evaluated under BOTH internal states side by side.
   This must always be visible — it is the chapter's key teaching move.
8. HEN-1 ABSENT mode: when toggled off, if BOTH sensors are firing
   above 0.3, the behavioral output flickers every ~500ms between
   FORWARD and PIROUETTE. If only one sensor is firing above 0.3,
   respond normally to that one. This represents broken integration.
9. Clean minimal styling. No animations beyond the HEN-1 flicker.
   Readable on a phone.
10. One file. No external scripts or stylesheets.
```

**CONSTRAIN** — name what the model must not do:

```
Do not invent biology I did not give you. Weights, rules, behavioral
outputs — use only what is in the chapter. If you think the chapter
is wrong about something, say so in a comment; do not silently fix it.

Comment the JavaScript so a student can map each block back to the
chapter: // labeled-line section, // neuromodulator section, // HEN-1
section, etc.

Deliver the code as a single ```html block.
```

**VERIFY** — before trusting any output, run all four checks:

```
1. Open the file in a browser. Zero console errors.
2. Reproduce the chapter's worked example exactly:
   S_food = 1.0, S_repellent = 1.0, WELL-FED → Decision must read -0.4,
   behavior must read PIROUETTE.
   Same inputs, STARVED → Decision must read +0.5, behavior must read
   FORWARD RUN. Any other numbers: the build is wrong; return the bug
   with the exact discrepancy.
3. HEN-1 toggle: with both sensors above 0.3 and HEN-1 ABSENT, output
   flickers. With HEN-1 PRESENT, it is steady. Confirm both.
4. Comparison panel: change sensor values. The panel must always show
   the same values evaluated under both internal states. If it doesn't,
   return for revision.
```

---

Once the widget works, use it as a thinking tool:

Find the sensor combination where the fed worm just barely refuses to cross. Switch to starved. How much can you now raise the copper before the worm refuses? That gap is a quick estimate of what "mood" buys in cost-benefit terms.

Toggle HEN-1 off with both sensors near 1.0 and watch the flicker. Now reduce one sensor to zero. The flicker stops. Why? Map this back to the Ishihara experiment.

Find the *S*(food) / *S*(repellent) combination where fed and starved give the same output. What does that combination represent biologically?

---

**Extension to Chapter 4.** The widget treats the weights as fixed by internal state. Chapter 4 asks: what changes those weights themselves? The answer is associative learning — the CREB-dependent re-weighting introduced in this chapter's temperature memory section. Before Chapter 4, ask your LLM:

```
Extend 03-celegans-decision.html with a "training history" panel.
Each time the worm CROSSES into copper, randomly decide (50%
probability) whether the food on the other side was good or bad.
Record the outcomes. After 10 crossings, slowly shift w_food up or
down based on the running average of outcomes — by no more than 0.05
per training event. Add a comment describing what this extension models
that the original widget could not.
```

Save the output. Bring it to Chapter 4. It will be our point of comparison when *Aplysia* enters the story.
