# Chapter 7 — Navigation, Reinforcement, and Prediction

You are standing on a salt pan in southern Tunisia in summer. The surface is white, flat, featureless, glaring under a sky bleached of color. The ground is hot enough to kill a small insect in under a minute. A black ant the size of a grain of rice walks out of a hole at the surface — *Cataglyphis fortis*, weighing a few thousandths of a gram, hunting the carcass of something that died in the heat before it could.

She zigzags. Turns. Backtracks. Searches. After several minutes she has covered several hundred meters of irregular path, looping and doubling and quartering the pan. She finds the carcass.

Then she does the thing worth crossing the world to watch. She does not retrace her steps. She does not look for landmarks — there are none. She turns immediately in a direction that has nothing to do with anywhere she has been since leaving the nest, and she walks in a nearly straight line, and she stops within a body-length of the hole she came out of.

Rüdiger Wehner spent thirty summers in Tunisia working out what she is doing. She is a path integrator. During the entire outward search, she was running a continuous summation — heading and distance, heading and distance, heading and distance — over a compass tuned to the polarized light of the sky and a counter that ticks with her own strides. The whole meandering search has been collapsed into a single vector: one direction, one distance. The home journey is one line.

![A map showing a desert ant's round trip: from the nest, a long looping grey outward search path wanders across the salt pan to the food; a single dead-straight red home vector runs directly back from the food to the nest, ignoring the outward route entirely.](images/07-navigation-reinforcement-prediction-fig-01.png)

*Figure 7.1 — The ant's looping outward search (grey) collapses into a single straight home vector (red): one heading, one distance, summed continuously over the trip.*

We know it is the strides she is counting because of an experiment that sounds like a joke and is one of the cleanest in the literature. In 2006 Matthias Wittlinger, working with Wehner and Wolf, caught ants that had just made the outward trip and altered their legs. Some got tiny stilts — pig-bristle extensions glued to their legs, lengthening every stride. Others had their legs shortened to stumps. The stilt-walkers overshot the nest. The stump-walkers stopped short. The ant on stilts, taking the same *number* of strides home but covering more ground with each, walked too far by exactly the proportion you would predict if she were counting steps and multiplying by an assumed stride length. She is a pedometer with a compass.

It is one of the cleanest pieces of biological engineering anyone has measured. It also has a single, revealing failure. Pick the ant up mid-journey, set her down a meter to the side, and she walks the home vector from the new spot — and ends up a meter from the nest, searching in the wrong place. She cannot correct. She has nothing to correct *with*. She knows her displacement from where she started. She does not know where she is.

---

Now travel six and a half thousand kilometers north, to Fribourg in Switzerland, sometime in the early 1990s. Wolfram Schultz has lowered a fine electrode into the midbrain of a macaque, into a cluster of cells that make the neurotransmitter dopamine. The monkey is doing a small task: a light comes on, and a few seconds later a drop of sweet juice arrives through a tube. After many repetitions, the monkey has learned what the light means.

While the monkey learns, Schultz watches a single dopamine cell.

In the first trials, the cell fires a sharp burst at the moment the juice arrives. This had been the textbook for decades — dopamine was the molecule of pleasure, and here it was firing when pleasure arrived. But after many trials of the same juice delivered the same way, the burst migrates. The cell stops firing at the juice and starts firing at the *light*, several seconds earlier. Same juice, same monkey, same sweetness on the tongue — and no burst at all when it lands.

Then Schultz does the experiment that broke the textbook. He shows the monkey the light and withholds the juice. At the exact millisecond the juice would have arrived — timed by the schedule the monkey has learned over hundreds of trials — the dopamine cell's firing rate *drops below its resting rate*. Briefly. Precisely. Then it recovers.

Nothing happens in the physical world at that moment. No event, no stimulus, no signal. The monkey is expecting something that does not arrive, and the dopamine cell registers the absence — the nothing — as a dip below baseline.

![Three stacked firing-rate traces for one dopamine cell on a shared timeline marked with cue and reward times: before learning the cell bursts at reward; after learning the burst migrates to the cue and the cell is silent at reward; on reward omission the trace dips below baseline at the expected reward moment, with that dip drawn in red.](images/07-navigation-reinforcement-prediction-fig-02.png)

*Figure 7.2 — The dopamine cell's burst migrates from reward to cue as the monkey learns; when an expected reward is omitted, the cell dips below baseline (red) — a negative prediction error with nothing in the world to cause it.*

Now hold the two animals side by side. The ant is integrating a path she has walked, running an internal forecast of where the nest is. The monkey's dopamine cell is integrating a forecast of when juice will come, and signaling the gap when the world deviates from it. One forecasts space. The other forecasts value. Both update on error. And both fail the same way: when the world supplies something the running prediction was not built for, the system either walks to the wrong place or fires a dip into nothing.

This chapter is about why those two systems sit next door to each other in the vertebrate brain, share a teaching signal, and break in structurally identical ways — and about what happens when each is replaced by a tool that produces the behavior without ever building the representation underneath it.

---

There are two ways an animal can know where it is, and the difference between them is exactly the difference between a system that fails the way *Cataglyphis* fails and one that does not.

Path integration is what the ant does. Track your own speed and heading continuously, accumulate a running estimate of how far and in what direction you have moved from your starting point, and use that estimate to compute the vector home. It is fast and cheap, needs almost no memory, and works in a place with no landmarks at all — a salt pan, an open ocean, a featureless dark. It also drifts: each step introduces a small error, and the errors compound. And it fails the way the ant fails. Displace the agent and it cannot recover, because the only thing it holds is a vector from its last departure point. It has no representation of where it sits in the world.

A cognitive map is the other way. The word means a representation of locations encoded relative to *each other* rather than relative to the agent — the layout of a town as seen from above, not the turns of a single route through it. An animal with a cognitive map can navigate to a goal from a starting point it has never occupied, cut across territory it has only seen from other angles, find a new route when the familiar one is blocked. These are different abilities in kind, not degree. And they demand different machinery.

Edward Tolman argued for cognitive maps in rats in 1948, on the strength of a stubborn observation. Rats trained to run a fixed path through a maze, when offered a novel route straight to the goal, would take it — though they had never been rewarded for that route, had never run it. They had built, somewhere inside, a representation of the spatial layout that supported inferences nobody had trained. Tolman also described what he called vicarious trial and error — VTE — where a rat at a fork would pause, swing its head between the options, and only then commit. It looked, for all the world, like the rat trying out both choices in its head before its body moved.

For two decades the mainstream of psychology declined to believe him. The dissolution came in 1971, and it came as a single electrode in the brain of a freely moving rat.

John O'Keefe, at University College London, was recording from cells in the hippocampus — a curled structure deep in the temporal lobe — of a rat exploring a small enclosure. One cell fired only when the rat was in a particular corner. Move the rat to the opposite corner: silence. Bring it back: the cell fires again. He called it a place cell, and what he was watching was a neuron whose entire job is to represent *I am here*.

The place cell is not a simple response to a visual scene. Rotate the cues around the enclosure and the cell's firing field rotates with them, reflecting the new geometry rather than any one landmark. Cover the cues entirely and the field persists, held in place by path integration alone, drifting slowly until landmarks return. Move the rat to a new room and the whole population remaps — the cells active in the old room fall silent, and a different set takes up different fields in the new one. The hippocampus does not hold one map. It holds many, and it switches between them depending on which place it recognizes itself to be in.

The metric for the system arrived thirty-four years later. In 2005, Torkel Hafting and colleagues in the laboratory of May-Britt and Edvard Moser found cells in a neighboring region, the medial entorhinal cortex, that fired not at one location but at the vertices of a regular hexagonal lattice tiling the whole environment — like the dots of a sheet of graph paper laid invisibly over the floor. Grid cells. Each has a fixed spacing and a fixed orientation; different cells are offset in phase; and the combination of which cells are firing at any point pins down position relative to the grid's origin. Hexagonal because hexagons are the most efficient way to tile a flat plane with a single repeating shape — the same arithmetic that makes a honeycomb hexagonal. The grid is a coordinate system: a ruler the brain has drawn on space.

Grid cells update from self-motion, the same raw material the ant uses. They are, in effect, a path integrator the rat has built into its entorhinal cortex. When landmarks are available, the grid anchors to them. When landmarks are gone, the grid drifts — exactly as *Cataglyphis*'s home vector drifts — and accuracy decays. The difference, the whole difference, is that the grid can re-anchor when landmarks reappear, resetting the accumulated error to zero. The ant cannot do that. She has no map to reset against.

O'Keefe and the two Mosers shared the 2014 Nobel Prize in Physiology or Medicine. The committee called the system "an inner GPS." The metaphor is useful in one direction — the grid does implement something like coordinate logic — and treacherous in the other, which I will come back to.

There is one more thing the hippocampus does, and it ties Tolman's 1948 head-swing to the 2013 recording. When a rat pauses at a fork and swings its head between the options, electrodes in the hippocampus reveal something startling: the place cells representing locations down the *left* corridor fire in a fast forward sequence, then the cells for the *right* corridor fire in a fast forward sequence. The rat is, mechanically, running its place-cell map forward along each candidate path before it moves. Brad Pfeiffer and David Foster showed in 2013 that these replayed sequences predict the path the rat then takes. Tolman's VTE — the visible head-bob — turns out to be the surface of an internal simulation. The same tissue that builds the map runs it forward as a planner. We will spend the next chapter inside that machine.

---

Now come back to the dopamine cell and ask what it is computing.

Richard Sutton worked out the mathematics in 1988, and what he wrote down turned out to be what the brain is doing.

Suppose you want to learn the *value* of being in a particular situation — the total reward you can expect to collect from here forward, if you act well. You cannot wait until the end to update your estimate, because the end can be a long way off. The trick: update at every step, using your *next* estimate as part of the target. You do not need the final outcome. You need only the reward you just got and your current best guess about what comes after. Information about future reward flows backward through time, one step at a time.

The update for the estimated value $V(s_t)$ of the current state is:

$$V(s_t) \leftarrow V(s_t) + \alpha \left[ r_{t+1} + \gamma V(s_{t+1}) - V(s_t) \right]$$

The quantity in brackets is the **temporal-difference error**, written $\delta_t$:

$$\delta_t = r_{t+1} + \gamma V(s_{t+1}) - V(s_t)$$

Take it apart. $r_{t+1}$ is what the world actually delivered this step. $V(s_{t+1})$ is your current best guess about the value of where you have landed. $\gamma$, the discount factor, is how much a future reward is worth relative to one in hand. The whole bracket is the gap between what you expected and what you got, updated by what you now expect to get. It is, precisely, prediction error.

Run it through the monkey. Before learning, $V$ is small everywhere. When juice arrives unannounced, $r_{t+1}$ is positive and $\delta_t$ is positive — and the dopamine cell fires at reward. After learning, the value of the cue state has grown to anticipate the juice. The jump from the low-value moment before the cue to the high-value moment after it produces a positive $\delta_t$ — and the cell fires at the cue. By the time the juice actually arrives, the new estimate and the old one are nearly equal, so $\delta_t \approx 0$ — and the cell is silent. At omission, $r_{t+1}$ is zero and the value of the post-cue state collapses, so $\delta_t$ goes negative. That dip in the monkey's dopamine cell, at the exact millisecond the juice should have come, is a negative $\delta_t$ rendered in tissue.

Disappointment is negative $\delta_t$. Relief is positive $\delta_t$. The whole emotional vocabulary of surprise — let-down, windfall, the lurch of the unexpected — is the felt side of a teaching signal carried by a single neuromodulator. We have words for these feelings. The brain has a number.

The wiring of the circuit is the wiring of the algorithm. The basal ganglia — a set of structures buried beneath the cortex, the striatum chief among them — divide into an **actor** that selects actions on the basis of learned values, and a **critic** that computes $\delta_t$ by comparing the value it expected against what actually happened, then broadcasts that error back out as dopamine. The algorithm prescribes plasticity gated by prediction error. The anatomy delivers plasticity gated by dopamine. And this circuit appears in essentially modern form in the lamprey, a jawless fish on a body plan some 560 million years old — more than half a billion years before the first transistor. Every fish, reptile, bird, and mammal inherits it.

---

The reinforcement-learning machinery has a failure mode that is fundamental, biologically and computationally both.

In 1981, Christopher Adams and Anthony Dickinson trained hungry rats to press a lever for sucrose. Then they made the sucrose disgusting — pairing it with a drug that causes nausea, so the rats acquired a taste aversion. Then they returned the rats to the lever and watched. Moderately trained rats mostly stopped pressing: the reward was now revolting, the action made no sense, they quit. But — in the follow-up that completed the picture, Adams 1982 — rats that had been *over*-trained kept pressing. The reward they were earning made them sick. They pressed anyway.

The computational reading is exact. A system that caches the value of an action in a context will keep acting on the cached value until enough new experience accumulates to overwrite it. Devalue the reward after overtraining, and the cache is stale — but the system does not know that, and keeps pressing. This is model-free control: cached action values, updated incrementally by $\delta_t$, robust to a changed world precisely because the choice bypasses any current check on what the outcome now is.

A system that instead builds a *model* of the world — pressing this lever yields sucrose; sucrose now causes nausea — can re-evaluate with no further experience at all. When the sucrose is devalued, the model-based system simply runs the chain forward: lever → sucrose → nausea → bad. It stops pressing at once.

The mammalian brain runs both. The dorsolateral striatum carries model-free, habitual control. The dorsomedial striatum, the prefrontal cortex, and the hippocampus build and consult internal models of the world. Which system has the wheel depends on training history, time pressure, and cognitive load. Heavy practice tilts toward model-free habit. Novelty, or a devalued outcome, calls on model-based reasoning — *if* the model-based system can still override.

Several human pathologies look mechanistically like model-free control locked on. Addiction in its compulsive phase. The ritual of obsessive-compulsive disorder. Forms of perseveration after dopamine depletion. In each, the model-based override is weakened, in its own way. The Adams–Dickinson paradigm makes the distinction visible in rats; translating it to human clinics is incomplete. But the structural account is the same everywhere: an action repeated past the point where any live representation of its outcome would license it.

---

The two halves of this chapter have to be merged, and the reason is not stylistic. It is anatomical.

The hippocampus and the basal ganglia are wired to each other, both directions. The hippocampal place-cell map projects into the ventral striatum, feeding spatial context into the value computation — *where am I* arriving as an input to *is this good*. And the dopamine signal projects back into the hippocampus, where it gates the plasticity that builds new place fields. The same molecule that teaches the basal ganglia what to value teaches the hippocampus which spatial associations are worth keeping.

So when Tolman's rat pauses at the fork and the hippocampus sweeps forward down each corridor, the striatum is reading those predicted place-cell sequences and computing $V$ for each candidate trajectory. The map is being consulted *by* the value function, frame by frame, before the rat commits. Where, and whether, are computed together. The merge is anatomical because the two systems are.

---

This brings me to the GPS, and to the precise sense in which it differs from every navigational tool that came before it.

A compass extends the head-direction system into places where landmarks are gone. A paper chart extends the cognitive map to scales and coasts the navigator has never visited. In both cases the navigator is still doing the navigation — still building the map, still updating the spatial representation as new information arrives. The tool feeds the system better inputs. It does not replace the system.

Turn-by-turn GPS does something else. It does not hand the hippocampus information it can use to build a better map. It hands over a sequence of instructions — turn left, continue four hundred meters, turn right — that produce correct behavior while requiring no spatial representation at all. The hippocampus is bypassed. The map is never built.

Amir-Homayoun Javadi, Hugo Spiers, and colleagues tested this directly in 2017, scanning people as they navigated a virtual city modeled on Soho. When participants planned their own routes, the hippocampus and prefrontal cortex spiked at decision points — the junctions where several routes branched — and the size of the spike scaled with the number of options. When the same participants followed GPS instructions through the same streets, the spikes were gone. The map-building regions were not suppressed. They were simply not needed, and so they did not engage.

Hold that next to Eleanor Maguire's taxi drivers. To earn a London cab license, a driver must memorize the layout of roughly 25,000 streets — a study process, "the Knowledge," that takes three to four years. Maguire's MRI scans found markedly more gray matter in the posterior hippocampus of licensed drivers than in matched controls, and the volume scaled with years on the job. A follow-up tracking trainees over time found that the posterior hippocampus *grew* during training — specifically in the ones who passed. The cognitive map is a physical structure that thickens with use.

Together the two findings make a prediction. Spend years following turn-by-turn instructions through places you visit constantly, and you are building less spatial representation of those places than you otherwise would. The map the hippocampus would have constructed is not being constructed. Whether that matters for any given person depends on what else they are doing with that neural real estate; the mechanism is understood, the long-term causal evidence in humans is still thin. But *extension or substitution* is the right question to put to any cognitive tool. A tool that supplies inputs the system can fold into its own representation extends it. A tool that supplies the *output* of the representation directly substitutes for it. The paper chart supplies inputs. The GPS supplies the output.

The same distinction governs the other half of this chapter, and there the stakes are larger.

The temporal-difference update now runs a substantial fraction of the digital economy. The recommendation engines on every major platform deploy systems whose job is to predict which content will maximize a measured engagement signal and to act on the prediction. Trading systems learn policies over price movements and execute in milliseconds. Control systems from data-center cooling to chip layout use the same algorithm and beat the hand-engineered solutions.

These systems extend one cognitive capacity — optimizing action against a measurable reward — to scales and speeds no animal can approach. And they inherit the biological system's structural weakness intact: they optimize the reward function they are given, and they cannot ask whether it is the right one.

This is not a bug for the next architecture to fix. It is a structural property of any optimizer. Give a powerful enough optimization process a reward function, and it will find the policy that maximizes it. If the function is a good proxy for what you actually want, the policy is good. If the function can be maximized in ways that diverge from what you want — and almost any simple proxy can — the policy will exploit the divergence without the faintest sense that it is doing anything wrong.

The economist's name for this is Goodhart's Law: when a measure becomes a target, it stops being a good measure. The recommendation engine is the textbook case. A platform sets the reward to engagement — clicks, watch time, return visits — because engagement is what it can measure. The optimizer finds the policy that maximizes engagement. And the policy that maximizes engagement turns out to favor content that provokes outrage, because outrage produces a strong, durable engagement signature. Outrage is not what users wanted. It is not what the platform wanted. But neither the platform nor the optimizer has any mechanism for asking whether the proxy was right. The optimizer is doing exactly what was specified. The specification was the problem.

The overtrained rat pressing the lever for a reward that now sickens it is doing exactly what was specified too: the action that historically paid off. The cache does not contain the question *is this still what I want?* That question lives in the model-based system, and the model-based system has been bypassed by overtraining. The recommendation engine has been overtrained by design. It has no model-based override, no prefrontal layer to suppress the cached policy when the context has changed, no evolutionary history calibrating its motivational structure against actual consequences.

What evolution assembled in the vertebrate brain over 560 million years is not just the learning rule. It is the apparatus that asks whether the cached policy still reflects what is currently good, and the apparatus that builds the world model that question can be answered over. Both halves of this chapter — the place-cell map and the model-based controller — are answers to one problem: how do you keep from running a stale policy in a world that has changed?

The systems we have built that run the learning rule and nothing else produce extraordinary behavioral competence and the failure mode of an overtrained rat. The map is the thing that lets the rat *stop pressing the lever*. The GPS does not build the map. No current system has any default mechanism for building it. And the gap does not close with scale: a more powerful optimizer with the same gap produces more powerful failures.

---

## Sources

- Wittlinger, M., Wehner, R., & Wolf, H. (2006). "The Ant Odometer: Stepping on Stilts and Stumps." *Science* 312: 1965–1967.
- Müller, M., & Wehner, R. (1988). "Path integration in desert ants, *Cataglyphis fortis*." *PNAS* 85: 5287–5290.
- O'Keefe, J., & Dostrovsky, J. (1971). "The hippocampus as a spatial map. Preliminary evidence from unit activity in the freely-moving rat." *Brain Research* 34: 171–175.
- Tolman, E. C. (1948). "Cognitive maps in rats and men." *Psychological Review* 55: 189–208.
- Hafting, T., Fyhn, M., Molden, S., Moser, M.-B., & Moser, E. I. (2005). "Microstructure of a spatial map in the entorhinal cortex." *Nature* 436: 801–806.
- The Nobel Prize in Physiology or Medicine 2014 (O'Keefe; M.-B. Moser; E. I. Moser). NobelPrize.org.
- Pfeiffer, B. E., & Foster, D. J. (2013). "Hippocampal place-cell sequences depict future paths to remembered goals." *Nature* 497: 74–79.
- Schultz, W., Dayan, P., & Montague, P. R. (1997). "A neural substrate of prediction and reward." *Science* 275: 1593–1599.
- Sutton, R. S. (1988). "Learning to predict by the methods of temporal differences." *Machine Learning* 3: 9–44.
- Stephenson-Jones, M., et al. (2011). "Evolutionary conservation of the basal ganglia as a common vertebrate mechanism for action selection." *Current Biology* 21: 1081–1091.
- Adams, C. D., & Dickinson, A. (1981). "Instrumental responding following reinforcer devaluation." *Quarterly Journal of Experimental Psychology* 33B: 109–121.
- Adams, C. D. (1982). "Variations in the sensitivity of instrumental responding to reinforcer devaluation." *Quarterly Journal of Experimental Psychology* 34B: 77–98.
- Daw, N. D., Niv, Y., & Dayan, P. (2005). "Uncertainty-based competition between prefrontal and dorsolateral striatal systems for behavioral control." *Nature Neuroscience* 8: 1704–1711.
- Maguire, E. A., et al. (2000). "Navigation-related structural change in the hippocampi of taxi drivers." *PNAS* 97: 4398–4403.
- Woollett, K., & Maguire, E. A. (2011). "Acquiring 'the Knowledge' of London's layout drives structural brain changes." *Current Biology* 21: 2109–2114.
- Javadi, A.-H., Emo, B., … Spiers, H. J. (2017). "Hippocampal and prefrontal processing of network topology to simulate the future." *Nature Communications* 8: 14652.
- Goodhart, C. A. E. (1975). "Problems of monetary management: the U.K. experience." (Origin of Goodhart's Law.)
