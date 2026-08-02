# Chapter 3 — Steering: The First Nervous System

Here is the experiment. A centimeter of damp agar. A stripe of copper sulfate painted across it — copper is poison, and every sensor the worm has for detecting it is screaming. And a *C. elegans*, about a millimeter long, pale as glass, approaching the stripe.

The worm hits the copper. It recoils. It tries again. It recoils again. And then — if it has been starved of food for a few hours first — it crosses. This is a real assay: lay a copper-sulfate barrier on agar, deprive some worms of food and feed others, and the hungry ones cross the poison at a far higher rate than the fed ones, and not because they happen to be moving more.

Stay with that crossing for a moment, because it is the smallest version of something enormous. You cannot predict what the worm will do from a list of what its sensors are detecting. The copper concentration is the same for both worms. The sensors are the same. The motor neurons are the same. Two worms at the same stripe do two different things, because one ate recently and one did not. The behavior is not a function of the environment. It is a function of the environment *and a variable the environment cannot see.*

A bacterium cannot do this. You can predict what a bacterium will do at a copper gradient from the gradient alone. A thermostat cannot do this. A robot vacuum cannot do this. But a worm with 302 neurons — a worm whose every synapse has been catalogued, named, and mapped — can. And because the entire wiring diagram exists on paper, we can say exactly which wires make it possible.

That is what this chapter is about. Not intelligence in some grand sense. The floor. The minimum architecture for changing your mind.

---

Before the neurons, there is a geometry, and the geometry does most of the cognitive work before a single cell fires.

Think about what it means to be radially symmetric — a hydra, a jellyfish, presenting the same face to the world in all 360 degrees. If such an animal wants to move toward food, its navigation problem is *which direction?* It has to gather sensory information from everywhere at once and resolve it into a heading. That is hard, and it takes a lot of machinery.

Bilateral symmetry solves the problem by anatomy. Once you have a left and a right that mirror each other, you necessarily have a front and a back. Sensors cluster at the front. The animal moves where the sensors point. The navigation problem collapses from *which of 360 degrees?* to *keep going, or turn?* Two options. Forward and not-forward. That is the question the first nervous systems were built to answer — not vision, not language, not planning, just whether to persist in a direction or change it.

The simplification was apparently so powerful that it happened once. Every bilateral animal on Earth — every worm, insect, fish, frog, bird, and mammal — descends from a single ancestor that made this transition roughly 570 million years ago, in the late Ediacaran, the dim shallow seafloor that came just before the Cambrian. Every brain that has ever existed is an elaboration of a solution to a problem first posed in that late-Ediacaran mud: *forward, or not forward?*

*C. elegans* sits about as close to that original solution as any animal we can study. Its nervous system organizes around a nerve ring encircling the throat just behind the head. This is the worm's brain. It is not impressive — 302 neurons, roughly 5,000 chemical synapses (plus some 2,000 neuromuscular junctions and 600 gap junctions), fitting in a structure smaller than the head of a pin. But it does something the bacterium's chemotaxis system of the last chapter cannot. It integrates multiple, conflicting signals and produces a coherent directional decision that can be tuned by internal state. Each of those words is doing real work. Let me go through them.

---

Smell coffee. Hear a car alarm. Feel heat from a radiator. You do not experience these as one undifferentiated blob of sensation. You know, before you have time to think, that one is a smell and one is a sound and one is warmth. That separation is not learned; it is built into the architecture — separate sensors for separate stimulus categories, each wired to circuits that interpret the signal in light of its source. Neuroscientists call this the labeled-line principle: each sensory neuron is dedicated to one stimulus type, and the *meaning* of its firing is carried by the identity of the wire it travels along, not by some code at the destination.

*C. elegans* has labeled lines in their simplest possible form. The AWA neurons detect volatile attractants such as diacetyl — the buttery-smelling compound given off by the bacteria the worm eats — and a related pair, AWC, picks up other food odors like isoamyl alcohol and benzaldehyde. When these fire, their wires run to an interneuron called AIY, a major integration hub, in a way that biases the worm toward longer runs and fewer turns. The interpretation "food: approach" is not computed anywhere. It is built into the connection. The ASH neurons, by contrast, detect nose-touch, high salt, and heavy metals including copper. When ASH fires, its wire reaches the circuit in a way that biases the worm toward reversals and sharp turns. The interpretation "danger: avoid" is, again, in the wiring.

This is a trade-off a 302-neuron animal is forced to make. You cannot afford a flexible, general-purpose cortex when you have fewer neurons than the 2,300 transistors on Intel's first microprocessor, the 4004 of 1971. What you *can* afford is a set of pre-labeled wires that carry their interpretation with them, converging on a small set of integration cells whose job is not to understand the signals but to tally them into a single output: run, or pirouette. Labeled lines with hardwired valences are not a limitation of primitive nervous systems. They are a design principle that persists at every scale. Your own brainstem runs the same logic. Pain feels like pain because of which wires the pain-sensitive neurons connect to, not because of anything intrinsic to the signal. The labeled line is the cognitive atom — the irreducible unit from which every more elaborate judgment is built.

---

Now something worth pausing on. The way the worm climbs a chemical gradient is, at the algorithmic level, identical to what the bacterium of Chapter 2 does. The bacterium alternates running straight with tumbling to reorient; when concentration is rising it suppresses tumbles and runs longer, and when concentration falls it tumbles more, reorienting at random until chance points it uphill. The result is a biased random walk that climbs the gradient without the cell ever computing a direction.

The worm does the same thing with different vocabulary. Instead of runs and tumbles it has runs and pirouettes — bursts of tight turning that include reversals and omega bends, where the body curls into the shape of the Greek letter Ω. The pirouette is the worm's tumble. What governs it is the time-derivative of attractant concentration: heading up the gradient suppresses pirouettes, heading down triggers them, and over many pirouettes the worm drifts uphill. The algorithm is the bacterium's.

So far the worm is just a bacterium with 302 neurons. What makes it genuinely different is what happens when the gradient is not the only thing going on. The worm has multiple attractants and repellents, and their signals arrive at the integrating circuit at the same time. When it smells diacetyl and detects copper at once, both labeled lines fire. One says *forward*. The other says *reverse*. The circuit has to produce a single output. The bacterium has no answer to this — it has essentially one sensor channel and one response. The worm has competing sensors, and the competition has to be resolved. And the mechanism that resolves it is not in the labeled lines. It is in something slower.

---

In 2000, James Sawin, Rajesh Ranganathan, and Robert Horvitz published findings that reframed how biologists thought about the worm's dopamine. When *C. elegans* meets a bacterial lawn, it slows down. The slowing is driven by dopamine released from mechanosensory neurons that physically touch the bacteria. Without dopamine the worm runs straight through excellent food without pausing; with it, the worm dwells and eats. Dopamine, half a billion years before any vertebrate brain existed, is already the signal for *food is here — shift from searching to exploiting.*

The same paper showed something easy to miss. When the worm has been food-deprived for hours and is then placed on food, the slowing is dramatically enhanced — but not by more dopamine. By serotonin, released from neurons that signal something close to satiety. A starved worm returned to food gets a larger serotonergic response than a fed one, and the serotonin translates into longer dwelling, slower movement, more eating.

What is happening architecturally is this. Dopamine and serotonin are not fast transmitters carrying specific messages along specific wires. They are broadcast molecules. They diffuse through the fluid around the worm's neurons, bind receptors on many cells at once, and change those cells' properties. A neuromodulator does not transmit a message; it changes the *gain* on an entire circuit. When serotonin is high — the worm has been starving and is finally on food — the gain on the attractive pathway rises and the gain on the copper-avoidance pathway falls. The same copper concentration that turns away a well-fed worm becomes tolerable to a starved one. Nothing in the environment changed. Nothing in the sensors changed. What changed is the weighting.

Let me make that concrete, with a warning attached. We can write the integration, at a coarse level of abstraction, as a competition between a weighted attractive signal and a weighted repellent one:

**Decision = w(food) · S(food) − w(repellent) · S(repellent)**

If the result is positive, the worm runs forward; if negative, it pirouettes. The signals *S* are the firing rates of the labeled-line sensors. The weights *w* are not fixed — they are set by the neuromodulatory state. Suppose both sensors fire equally, S(food) = 1.0 and S(repellent) = 1.0. A well-fed worm might carry weights around 0.4 and 0.8: the decision comes out to 0.4 − 0.8 = −0.4. Pirouette. No crossing. The same worm after several hours without food, its weights shifted by serotonergic priming to roughly 0.9 and 0.4: the decision is 0.9 − 0.4 = +0.5. Forward run. Crossing.

![Two decision bars on either side of a horizontal zero threshold, both driven by identical sensory inputs. The fed worm's bar drops below the line to minus 0.4 and is labeled "pirouette"; the starved worm's bar rises above the line to plus 0.5, drawn in red and labeled "crosses the poison," with only the neuromodulatory weights differing between them.](images/03-steering-first-nervous-system-fig-01.png)

*Figure 3.1 — Identical copper and food signals yield opposite verdicts; serotonergic priming in the starved worm tips the weighted sum positive (red), and it crosses the poison.*

Those specific numbers are illustrative, not measured — I am inventing the weights to show the *shape* of the computation, not reporting values from an electrode. What the data do show is the structure: a slow internal variable, the concentration of broadcast neuromodulators, re-weighting the integration of fast sensory signals. That is what the neuromodulatory system does. That is what it is for.

And here is the thing to hold onto. The worm at the copper line is not running a more complicated reflex than the bacterium. It is doing something different in kind. The bacterium's behavior is fixed by its sensory inputs. The worm's behavior is fixed by its sensory inputs *and an internal state with its own history* — a state that is real, encoded in chemistry, and not recoverable from any snapshot of the present environment. You have to know when the worm last ate. That is a new kind of system.

---

In 2002, Kunihiro Ishihara and colleagues published a result that is one of the most philosophically pointed in invertebrate neuroscience. They identified a small secreted protein, HEN-1, required for the worm to weigh attractive odors against repellent chemicals correctly. Without HEN-1 the worm can still smell diacetyl, still approach food, still detect copper, still recoil. What it cannot do is hold both signals at once and produce a coherent trade-off. HEN-1 mutants wander into copper while chasing food; they retreat from food while fleeing copper. They cannot resolve the conflict.

Think about what that tells us. The machinery for resolving competing signals is *separable from the sensors that generate them.* You can have perfectly functional sensors and still be unable to trade them off. You can disable only the integration machinery and lose the decision without losing the sensation. Sensing and deciding are not the same operation, even in a 302-neuron animal. The HEN-1 mutant has 302 neurons, all working, and cannot make this decision. The broken component is not a sensor and not a motor. It is the thing in between that holds two incompatible signals and produces one behavior. This is the knockout test from the last chapter, run on a worm: remove the part you think is doing the integrating, and watch the integration fail while everything else keeps working.

---

There is one more finding worth dwelling on, because it is counterintuitive and it is the bridge to everything that follows.

In 1995, Ikue Mori and Yasumi Oshima showed that when *C. elegans* is raised at a particular temperature *while it is eating*, and then placed on a thermal gradient with no food present, it migrates back toward the temperature it was raised at. The thermosensory neuron AFD acts as if it has stored the cultivation temperature as a set-point.

Here is the strange part. The preference is tied to the food. A worm raised at a given temperature while well-fed seeks that temperature later; disrupt the pairing of warmth with food during cultivation and the preference does not form the same way. The worm does not learn to want warmth in the abstract. It learns to want the temperature that, in its experience, meant food. There is no food in the test trial. Nothing in the present moment justifies the migration. The worm seeks the temperature because it remembers that temperature as good.

This is a preference — a behavioral disposition toward a value that depends on prior experience and is not reducible to the current sensory state. Something that was neutral became good, and the goodness outlasted the circumstances that created it. The molecular machinery behind such durable changes runs through a transcription factor called CREB, which, when a synapse fires hard and long enough, enters the cell nucleus and switches on genes that build new synaptic hardware. CREB is roughly the bridge between "this synapse just fired a lot" and "this synapse should now be permanently stronger" — the same pathway Eric Kandel characterized in the sea slug *Aplysia*, the work that won him a Nobel Prize in 2000. We will go deeper into Kandel in the next chapter. The point for now is that the worm carries ancient code. The mechanism that lets it form a conditional temperature preference is, in its essentials, the mechanism behind certain forms of long-term memory in vertebrates, including you.

---

Let me say what the worm has assembled, because I want to carry it forward as a checklist. The architecture has six components. Each is necessary; none is sufficient alone.

A bilateral body plan that collapses navigation from *360 degrees* to *forward or turn* — a cognitive simplification achieved by anatomy, before any neuron fires. Labeled-line sensors that carry their interpretation in the wiring, not in any central code. A temporal comparison — the same rate-of-change logic the bacterium uses, converting the present moment into *am I getting closer or farther?* Mutual-inhibition motor circuits that produce coherent all-or-nothing outputs: run or pirouette, not half of each. A neuromodulatory layer — dopamine and serotonin at minimum — encoding internal state on a timescale slower than neural firing, making the food-against-copper trade-off possible. And associative plasticity: the CREB-dependent ability to re-weight the labeled lines based on outcomes, so experience can update the valence of a stimulus.

Take any one out and the worm degrades in a specific, predictable way. Disable the labeled lines and it cannot interpret its sensors. Eliminate neuromodulation and it becomes a reflex machine, the same output regardless of internal state. Block associative plasticity and it cannot learn from experience. Remove the integration machinery — the HEN-1 case — and it cannot resolve conflict. These are not six features of a worm. They are six features of a system capable of changing its mind.

---

I should be careful about what I am not claiming.

*C. elegans* does not build a spatial map. It navigates gradients, not spaces. Remove the gradient and put food at a fixed location and the worm cannot learn to go there from memory; it will find the food each time by running the temporal-comparison algorithm from scratch, as if it had never been there. Its memory windows are short; the longest associative learning, the temperature conditioning, runs over hours. There is nothing resembling episodic memory, nothing resembling the recall of a specific past event used to plan a specific future. The worm does not plan. It does not imitate. It cannot learn a behavior by watching another worm.

What I am claiming is that the worm's nervous system, as documented, is the minimum architecture for state-dependent decision-making. Below it — the bacterium, the slime mold, the robot vacuum — you have systems that respond. With it you have a system that decides, in the operationally meaningful sense: an output that cannot be predicted from sensory inputs alone, that requires knowledge of internal state, and that represents a weighting of competing information by a cost-benefit calculation that is genuinely dynamic.

The floor is real. And it is documented in a specific wiring diagram, in a 1986 paper out of the MRC Laboratory of Molecular Biology in Cambridge — the product of more than a decade of slicing worms into thin ribbons with a diamond knife, photographing each ribbon under a transmission electron microscope, and tracing every neuron and every synapse by hand across thousands of overlapping micrographs. John White, Eileen Southgate, Nichol Thomson, and Sydney Brenner. The first complete connectome of any animal nervous system ever assembled.

The worm in the dish is not a stepping-stone to something more important. It is the worked example of the foundation. A decision — a genuine, state-dependent, experience-informed decision — fits in 302 cells. In a centimeter of soil, a millimeter at a time, half a billion years before anyone was watching.

---

There is a machine that runs the worm's first four components and stops there, and tens of millions of them are bumping around living rooms right now.

The roboticist Rodney Brooks proposed, in 1986 — the same year the worm's connectome went to press — an architecture he called subsumption: stacked sensory-motor reflexes, higher layers suppressing lower ones when they activate, no internal model of the world required. Brooks's bet was that most intelligent-seeming behavior does not need a map, and the robot vacuum descended from that bet, the Roomba, has cleaned a staggering number of rooms on the strength of it. The Roomba has sensors. It has labeled-line equivalents — each sensor has a fixed handler in firmware. It has something like temporal comparison in the history of its dust sensor. It has priority rules that arbitrate between competing behaviors. The first four items on the worm's checklist are, roughly, present.

The gap is in items five and six. The Roomba has no neuromodulator. When its bin fills, it signals for help; it does not recalibrate its entire cost-benefit calculus the way a hungry worm does, shifting every weight at once in response to internal depletion. And it forms no associative preferences. If it fails again and again at one particular corner, it does not update the valence of that corner in any enduring way. Most tellingly, when genuinely competing signals arise — clean this patch versus avoid this obstacle — it falls back on a fixed priority order baked into firmware. Obstacle avoidance always trumps cleaning. That ordering never updates. The worm's ordering updates every few hours, set by its internal state.

So the Roomba is not less *sophisticated* in some vague sense. It is architecturally incomplete in two specific ways: it is missing the gain-setting layer that makes behavior state-dependent, and it is missing the plasticity layer that lets experience rewrite the weights. Without them you have a system that responds. With all six you have a system that decides. The robot steering across your floor steers like the worm — and knows nothing the worm does not know, and rather less.

---

## Sources

- White, J. G., Southgate, E., Thomson, J. N. & Brenner, S. (1986). "The structure of the nervous system of the nematode *Caenorhabditis elegans*." *Phil. Trans. R. Soc. Lond. B* 314:1–340. (302 neurons; first complete connectome; ~5,000 chemical synapses.)
- Food-deprivation copper-avoidance assay: "A *C. elegans* Nutritional-status Based Copper Aversion Assay" and related work, *JoVE* (2017); see also PMC9070953 (intestine-to-neuron signaling alters risk-taking in food-deprived worms).
- Sawin, E. R., Ranganathan, R. & Horvitz, H. R. (2000). "*C. elegans* locomotory rate is modulated by the environment through a dopaminergic pathway and by experience through a serotonergic pathway." *Neuron* 26:619–631.
- Ishihara, T. et al. (2002). "HEN-1, a Secretory Protein with an LDL Receptor Motif, Regulates Sensory Integration and Learning in *C. elegans*." *Cell* 109:639–649.
- Mori, I. & Oshima, Y. (1995). "Neural regulation of thermotaxis in *Caenorhabditis elegans*." *Nature* 376:344–348.
- Pierce-Shimomura, J. T., Morse, T. M. & Lockery, S. R. (1999). "The fundamental role of pirouettes in *Caenorhabditis elegans* chemotaxis." *J. Neurosci.* 19:9557–9569.
- Bargmann lab / *WormBook*, "Chemosensation in *C. elegans*" (AWA/AWC/ASH labeled lines; diacetyl is an AWA attractant).
- Kandel, E. R. — CREB-dependent synaptic plasticity in *Aplysia*; Nobel Prize in Physiology or Medicine, 2000.
- Brooks, R. A. (1986). "A Robust Layered Control System for a Mobile Robot." *IEEE Journal of Robotics and Automation* 2(1):14–23. (Subsumption architecture; later the basis of the Roomba.)
- Bilaterian ancestor timing: late Ediacaran (~570 Mya); trace fossils and *Kimberella*/*Ikaria wariootia* (~555 Mya).
