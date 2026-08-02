# Chapter 7 — Navigation, Reinforcement, and Prediction

You are a Tunisian salt pan in summer. Ground temperature 60°C. White, flat, featureless under a sky bleached of color. A black ant the size of a grain of rice is walking out of a small hole at the surface — *Cataglyphis fortis*, twelve milligrams, hunting the carcass of an insect that died in the heat.

She zigzags. Turns. Backtracks. Searches. After several minutes she has covered 587 meters of irregular path. She finds the carcass.

She does not retrace her steps. She does not look for landmarks. She turns immediately in a direction that has nothing to do with anywhere she has been since leaving the nest, and she walks in a nearly straight line, and she stops within a body-length of the nest entrance.

Rüdiger Wehner spent thirty summers in Tunisia working out what she is doing. She is a path integrator. During the entire outward search, she was running a continuous summation — heading and distance, heading and distance, heading and distance — over a polarized-light compass and a step counter cued to her own leg movements. The whole meander has been collapsed into a single vector: a direction and a distance, and the home journey is one line.

It is one of the cleanest pieces of biological engineering anyone has measured. It also has a single, revealing failure mode. Pick the ant up mid-journey, place her one meter to the side, and she walks the home vector from the new starting position and ends up one meter from the nest. She cannot correct. She has nothing to correct *with*. She knows her displacement from where she started. She does not know where she is.

---

Now travel six and a half thousand kilometers north, to Fribourg, sometime in the early 1990s. Wolfram Schultz has lowered a fine electrode into the ventral tegmental area of a macaque monkey. The monkey is doing a small task: a light comes on, and a few seconds later a drop of sweet juice arrives through a tube. After many repetitions, the monkey has learned what the light means.

While the monkey learns, Schultz watches a single dopamine neuron.

In the first trials, the neuron fires a sharp burst at the moment the juice arrives. This had been the textbook for decades: pleasure causes dopamine. After many trials of the same juice delivered the same way, the burst migrates. The cell stops firing at the juice and starts firing at the *light* — several seconds earlier. Same juice. Same monkey. No burst at delivery.

Then Schultz does the experiment that broke the textbook. He shows the monkey the light and withholds the juice. At the exact millisecond the juice would have arrived, based on the timing the monkey has learned over hundreds of trials, the dopamine neuron's firing rate *drops below baseline*. Briefly. Precisely. Then recovers.

Nothing happens in the physical world at that moment. The monkey is expecting something that did not arrive, and the dopamine neuron registers the absence as a negative deflection from its resting rate.

Now look at the two animals together. The ant is integrating a path she has walked — running an internal forecast about where the nest is. The monkey's dopamine neuron is integrating a prediction about when juice will arrive — running an internal forecast about future reward, signaling the gap when the world deviates. One forecasts space. The other forecasts value. Both update on error. Both fail the same way: when the world supplies something the running prediction is not prepared for, the system either walks to the wrong place or fires a dip below baseline.

This chapter is about why those two systems live next door to each other in the vertebrate brain, share a teaching signal, and fail in structurally identical ways — and about what happens when each is replaced by a tool that does the behavior without building the representation.

---

There are two ways an animal can know where it is, and the difference between them is exactly the difference between a system that fails the way *Cataglyphis* fails and one that does not.

Path integration is what the ant does. Track your own velocity and heading continuously, accumulate a running estimate of net displacement from a starting point, use that estimate to compute the vector back. It is fast, cheap, requires almost no memory, and works in featureless environments. It also drifts. Each step introduces a small error, and errors compound. And — the failure that defines the strategy — if you displace the agent, it cannot correct. The only thing it has is a vector from its last departure point. It has no representation of where it is in the world.

A cognitive map is the alternative. An allocentric representation — locations encoded relative to each other rather than relative to the agent's current position. An animal with a cognitive map can navigate to a goal from a starting position it has never been to before, take shortcuts through territory it has only seen from different angles, compute alternate routes when a familiar one is blocked. These capabilities are qualitatively different. They also require qualitatively different neural hardware.

Edward Tolman argued for cognitive maps in rats in 1948, on the basis of a stubborn behavioral observation: rats trained to run a fixed path through a maze would, when offered a novel direct route to the goal, take it. They had not been reinforced for the direct route. They had built, somewhere, a representation of the spatial layout that supported inferences they had never been trained on. Tolman also documented what he called vicarious trial and error — VTE — where a rat at a choice point would pause, swing its head back and forth between options, and only then commit. Behaviorally, it looked like the rat *simulating* both options before choosing.

For two decades the mainstream of psychology rejected this. The dissolution came in 1971, and it was a single electrode in the brain of a freely moving rat.

John O'Keefe was at University College London, recording from neurons in the hippocampus of a rat moving freely through a small enclosure. One cell fired only when the rat was in a specific corner of the arena. Move the rat to the opposite corner: silence. Bring it back: the cell fires. He called it a place cell, and what he was looking at was the neuron whose job is to represent *I am here*.

The place cell is not a simple sensory response to a visual stimulus. Rotate the visual cues in the environment and the cell's firing field rotates with them, in a way that reflects the new geometry of the cue configuration rather than any single cue. Cover the cues entirely and the field persists, anchored by path integration alone, drifting slowly until landmarks return. Move the rat to a new room and the entire population of place cells remaps — the cells that were active in the old room go silent, and a different set takes on different fields in the new one. The hippocampus does not have one map. It has many, and it switches between them based on which environment it recognizes itself to be in.

The metric of the system came thirty-four years later. In 2005, Torkel Hafting and colleagues in the Mosers' laboratory found cells in the medial entorhinal cortex that did not fire at a single location but at the vertices of a regular hexagonal lattice that tiled the entire environment. Grid cells. Each has a fixed lattice spacing and a fixed orientation; different cells have phase offsets; the combination of which cells are active at any point uniquely encodes position relative to the grid's origin. Hexagonal because it is the most efficient way to tile a two-dimensional plane with a single repeating pattern — the same reason honeycombs are hexagonal. The grid is a coordinate system: an internal ruler imposed on space.

Grid cells update continuously, driven by self-motion signals. They are the path integrator the rat has built into the entorhinal cortex. When familiar landmarks are available, the grid is anchored to them. When landmarks are absent, the grid drifts — exactly the way *Cataglyphis*'s home vector drifts — and accuracy degrades. The difference is that the grid can be re-anchored when landmarks reappear, resetting the accumulated error. The ant cannot do that.

O'Keefe and the Mosers shared the 2014 Nobel Prize in Physiology or Medicine. The committee called the system "an inner GPS." The metaphor is useful in one direction — the grid implements something like coordinate logic — and dangerous in the other, which I will come back to.

When a rat pauses at a choice point in a maze and swings its head between options, electrodes in its hippocampus reveal something striking: place cells representing locations down the *left* corridor activate in a fast forward sequence, then cells representing the *right* corridor activate in a fast forward sequence. The rat is, mechanically, running its place-cell map forward along each candidate path before committing. Brad Pfeiffer and David Foster showed in 2013 that the replayed sequences predict the path the rat is about to take. Tolman's VTE — the visible head-bob of 1948 — turns out to be the surface expression of an internal simulation. The same neural tissue that builds the spatial map runs it as a forward planner.

---

Now come back to the dopamine neuron and ask what it is computing.

Richard Sutton worked out the mathematics in 1988, and what he wrote down turned out to be what the brain is doing.

You want to learn the *value* of being in a particular state — the total reward you can expect to accumulate from now forward, if you act well. You cannot wait until the end of the episode to update your estimate, because episodes can be long. The solution: update at every step using your *next* estimate as part of the target. You do not need the final outcome. You need only the reward you just received and your current best guess about what comes next. Information about future reward flows backward through time, one step at a time.

The update rule for the estimated value $V(s_t)$ is:

$$V(s_t) \leftarrow V(s_t) + \alpha \left[ r_{t+1} + \gamma V(s_{t+1}) - V(s_t) \right]$$

The bracketed quantity is the **temporal-difference error** $\delta_t$:

$$\delta_t = r_{t+1} + \gamma V(s_{t+1}) - V(s_t)$$

Unpack this: $r_{t+1}$ is what the world actually delivered. $V(s_{t+1})$ is your current best guess about what comes next. $\gamma$ is the discount factor — how much future rewards are worth relative to immediate ones. The whole bracketed term is the gap between what you expected and what you got, plus what you now expect to get. It is, precisely, prediction error.

Before learning, $V$ is small. When juice arrives, $r_{t+1}$ is positive and $\delta_t$ is positive. Dopamine neurons fire at reward. After learning, $V$ at the cue state has grown to anticipate the reward. The cue-onset transition from low-value to high-value state produces a positive $\delta_t$ — dopamine fires at the cue. At the moment juice arrives, the new estimate and the old estimate are nearly equal, so $\delta_t \approx 0$. Dopamine is silent. At omission, $r_{t+1} = 0$ and $V$ of the post-cue state collapses. So $\delta_t$ is negative. The dip in the monkey's dopamine neuron, at the exact millisecond the juice would have arrived, is negative $\delta_t$, implemented in tissue.

Disappointment is negative $\delta_t$. Relief is positive $\delta_t$. The emotional vocabulary of surprise is the phenomenal correlate of a teaching signal encoded in a neuromodulator. We have names for these feelings. The brain has a number.

The anatomy of the circuit is also the anatomy of the algorithm. The basal ganglia — the striatum, globus pallidus, substantia nigra — divide into an **actor** that selects actions based on learned values, and a **critic** that computes $\delta_t$ by comparing the current value estimate with actual outcomes and broadcasts the error back as dopamine. Plasticity gated by prediction error is what the algorithm prescribes. Plasticity gated by dopamine is what the anatomy delivers. This circuit appears in essentially modern form in the lamprey — the most primitive living vertebrate, 560 million years before the first transistor. Every fish, reptile, bird, and mammal inherits it.

---

The reinforcement-learning machinery has a failure mode that is fundamental — biologically and computationally.

In 1981, Christopher Adams and Anthony Dickinson trained hungry rats to press a lever for sucrose. After training, they paired sucrose with lithium chloride — a substance that causes nausea — so the rats developed a taste aversion to sucrose. Then they returned the rats to the lever.

Moderately trained rats stopped pressing. The reward was now disgusting; the action made no sense; they quit. Overtrained rats kept pressing. The reward they were earning made them sick. They pressed anyway.

The computational interpretation is exact. A system that caches the value of an action in a context will continue acting on those cached values until enough post-change experience accumulates to overwrite them. If the reward is devalued after overtraining, the cache is stale. The system keeps pressing. This is model-free control: cached action values, updated incrementally by $\delta_t$, robust against context change precisely because action selection bypasses any current evaluation of outcomes.

A system that builds a model of the world — pressing this lever produces sucrose; sucrose now causes nausea — can re-evaluate without further experience. When sucrose is devalued, the model-based system simulates the new contingency: sucrose now → nausea → bad. It stops pressing immediately.

The mammalian brain implements both. The dorsolateral striatum and its circuitry run model-free control. The dorsomedial striatum, prefrontal cortex, and hippocampus build and consult internal world models. Which system governs behavior depends on training history, time pressure, and cognitive load. Extensive practice tilts toward model-free habit. Novel situations or devalued outcomes call on model-based reasoning — if the model-based system can override.

Several human pathologies look mechanistically like locked-in model-free behavior. Addiction in its compulsive phase. The repetitive ritual of obsessive-compulsive disorder. Some forms of perseveration after dopamine depletion. The model-based override is, in different ways, weakened in each. The Adams-Dickinson paradigm makes the distinction visible in rats. Translating it to human clinical populations is still incomplete, but the structural account is the same: action repeated past the point where any live representation of its outcome would license it.

---

Now to why the two halves of this chapter have to be merged, because the merge is not stylistic — it is anatomical.

The hippocampus and basal ganglia are reciprocally wired. The hippocampal place-cell map projects to the ventral striatum, supplying spatial context to value computation. The dopaminergic signal from the substantia nigra projects back into the hippocampus, where it gates plasticity at the synapses that build new place fields. The same neurotransmitter that teaches the basal ganglia what to value teaches the hippocampus which spatial associations are worth consolidating.

When Tolman's rat pauses at the choice point and the hippocampus runs forward replay down each corridor, the striatum is reading the predicted place-cell sequences and computing $V$ for each candidate trajectory. The map is being consulted *by* the value function, frame by frame, before the rat commits. The two systems share information about both *where* and *whether*. The merge is not stylistic. It is anatomical.

---

This brings me to the GPS, and to the specific sense in which it is different from every navigational tool that preceded it.

A compass extends the head-direction system into environments where visual landmarks are absent. A paper chart extends the cognitive map to scales and territories the animal has never visited. In each case, the navigator is still doing the navigation — still building the map, still updating the spatial representation as new information arrives. The tool amplifies inputs to the system without replacing the system itself.

Turn-by-turn GPS navigation does something different. It does not give the hippocampus information it can use to build a better map. It gives a sequence of instructions — turn left, continue 400 meters, turn right — that produce correct behavior without requiring any spatial representation at all. The hippocampus is bypassed. The map is never built.

Amir-Homayoun Javadi, Hugo Spiers, and colleagues tested this directly in an fMRI scanner, having participants navigate a virtual environment modeled on Soho. When participants planned their own routes, the hippocampus and prefrontal cortex showed activity spikes at decision points — junctions where multiple routes were possible. The spikes scaled with the number of options at each junction. When the same participants followed GPS instructions through the same environment, those spikes were absent. The brain regions that build the cognitive map were not suppressed. They were not needed, and so they did not engage.

Hold that next to Eleanor Maguire's taxi-driver data. London taxi drivers must memorize the complete layout of roughly 25,000 streets — a process that takes three to four years. Maguire's structural MRI showed significantly greater gray-matter volume in the posterior hippocampus of licensed taxi drivers relative to matched controls. The increase scaled with years of experience. A follow-up study found that posterior hippocampal volume *increased during training*, specifically in candidates who passed. The cognitive map is a real biological structure that grows in response to use.

Together the two findings make a prediction: if you spend years following GPS instructions through environments you visit regularly, you are building less spatial representation of those environments than you would otherwise. The map the hippocampus would have constructed is not being built. Whether this matters for any given person depends on what else they are doing with that neural real estate. The mechanism is understood. The longitudinal causal evidence in humans is still incomplete. But *extension or substitution?* is the right question to ask of any cognitive tool.

A tool that supplies inputs the system can use to build its representation extends. A tool that supplies the output of the representation directly substitutes. The GPS supplies the output. The paper chart supplies inputs.

---

The same distinction applies to the reinforcement-learning half of this chapter, and here the stakes are larger.

The temporal-difference update now runs a substantial fraction of the digital economy. Recommendation engines on every major platform deploy RL systems whose job is to predict what content will maximize a measured engagement signal and act on the prediction. High-frequency trading systems learn policies over price movements and execute in milliseconds. Industrial control systems from data-center cooling to chip design use the same algorithm and exceed hand-engineered solutions.

These systems extend one cognitive capacity — optimizing action against a measurable reward — to scales and speeds no biological agent can approach. They also share the biological system's structural vulnerability: they optimize the reward function they are given, and they cannot ask whether that function is the right one.

This is not a bug to be fixed in the next architecture. It is a structural property of any optimizer. Give a sufficiently powerful optimization process a reward function and it will find a policy that maximizes that function. If the function is a good proxy for what you actually want, the policy will be good. If it can be maximized in ways that diverge from the actual goal — and almost any simple proxy can — the policy will exploit that divergence without knowing it is doing so.

The economist's formulation is Goodhart's Law: when a measure becomes a target, it ceases to be a good measure. The recommendation-engine case is the textbook version. A platform specifies the reward as engagement — clicks, watch time, return visits — because engagement is measurable. The optimizer finds the policy that maximizes engagement. The policy that maximizes engagement turns out to involve serving content that provokes outrage, because outrage produces strong engagement signatures. Outrage is not what users wanted. It is not what the platform wanted. But neither the platform nor the optimizer has any internal mechanism for asking whether the proxy is right. The optimizer is doing what was specified. The specification is the problem.

The overtrained rat pressing a lever for reward that now makes it sick is doing exactly what was specified: the action that historically paid off. The cache does not contain the question *is this still what I want?* That question belongs to the model-based system, and the model-based system has been bypassed by overtraining. The recommendation engine has been overtrained by design. It has no model-based override. It has no prefrontal layer that can suppress the cached policy when context has changed. It has no evolutionary history calibrating its motivational structure against actual consequences.

What evolution assembled in the vertebrate brain over 560 million years is not just the learning rule. It is the apparatus that asks whether the cached policy still reflects what is currently good, and the apparatus that builds the world model the rule can compute over. Both halves of this chapter — the place-cell map and the model-based controller — are answers to the same problem: how do you avoid running a stale policy in a world that has changed?

The systems we have built that run the learning rule without the rest produce extraordinary behavioral competence and the failure mode of an overtrained rat. The map is the thing that lets the rat *stop pressing the lever*. GPS does not build the map. No current AI system has any default mechanism for constructing it.

The reward-specification gap does not close with scale. A more powerful optimizer with the same gap produces more powerful failures.

---

## LLM Exercise — build `07-navigation-rl.html`

**What you're building:** A two-panel interactive HTML page demonstrating the chapter's two core experiments. Panel 1 contrasts path integration with cognitive mapping (and adds a GPS mode). Panel 2 contrasts model-free with model-based reinforcement learning in the Adams-Dickinson devaluation paradigm.

**Tool:** Claude Code (preferred), or any session with file output enabled.

---

**SHOW** — give the model the chapter so the build is anchored to the actual content:

```
I'm building an interactive teaching widget for a textbook chapter on
navigation and reinforcement learning. The chapter is pasted below.
The target file is 07-navigation-rl.html — a single self-contained HTML
file with embedded CSS and JavaScript, no external libraries, no build step.

[PASTE THE CHAPTER]

Build the two-panel interactive described at the end of the chapter.
Constraints follow.
```

**SAY** — exact behavioral requirements:

```
PANEL 1: Navigation.
- Top-down 20x20 grid arena. Home at center. 3-5 food locations placed
  around.
- Three modes selectable by radio button: path-integration, cognitive-map,
  GPS.
- Path-integration: agent does random search until it finds food, then
  computes net displacement vector and walks straight home. Show the outward
  path (zigzag) and the home vector (straight line).
- "Displace agent" button (only enabled mid-journey): shifts agent 3 units
  to the side. After displacement, path-integration mode walks the same
  vector from the new position — lands wrong, visibly. Cognitive-map mode
  re-anchors using landmark positions.
- Cognitive-map mode: visualize a place-cell tile overlay that fills in as
  the agent explores. After exploration, "novel shortcut" button places the
  agent at an unvisited position; agent computes a direct path home using
  the map.
- GPS mode: external instruction list shown on the side ("turn left, move 3,
  turn right, move 2..."). Agent follows. Place-cell grid stays gray and
  empty throughout. Final position correct; representation absent.

PANEL 2: Model-free vs. model-based devaluation.
- Simple lever-pressing schematic. Two virtual rats labeled "model-free"
  and "model-based".
- Slider: training trials (0 to 200).
- Button: "Devalue reward" (changes reward from +1 to -1 in the world
  model).
- Button: "Test" (runs 20 lever presses with no reward delivered; records
  press rate).
- Model-free agent: maintains a cached Q(lever) value. Updates only via TD
  error during training. Devaluation outside the chamber does not update Q.
  Press rate at test = function of Q.
- Model-based agent: maintains explicit model (action -> outcome) and value
  of outcome separately. Devaluation updates V(outcome) immediately, so
  V(lever) drops without further training.
- Plot: press rate per minute for both rats, side by side, before and after
  devaluation, as function of training-trials slider.
- Display the TD equation delta_t = r_{t+1} + gamma * V(s_{t+1}) - V(s_t)
  with current values substituted.

Layout: side-by-side desktop, stacked mobile. Canvas or SVG for the
navigation arena; SVG or canvas for the press-rate plot.
```

**CONSTRAIN** — what the build must not do:

```
- Path-integration mode must fail visibly after displacement. If the agent
  re-anchors to home, the implementation is doing map-based navigation, not
  path integration. This is the whole point of the comparison.
- Cognitive-map mode must succeed on novel shortcuts. If it fails, the
  place-cell tiling is decorative rather than functional.
- GPS mode must show correct behavior with no place-cell buildup. Substitution
  without representation is the central pedagogical point.
- The model-free agent's cached Q-value must not respond to devaluation
  directly. It updates only via actual delta_t inside the chamber.
- The training-trials slider must produce a visible transition: low training
  → both rats stop; high training → model-free persists, model-based stops.
- Single file. No external scripts or stylesheets.
```

**VERIFY** — before trusting the output, run all five checks:

```
1. Set 10 training trials, train, devalue, test. Both rats stop pressing.
2. Set 100 training trials, train, devalue, test. Model-based stops;
   model-free continues at near-baseline rate.
3. Path-integration mode, mid-journey displacement: home walk lands 3 units
   off. Visibly wrong.
4. Cognitive-map mode, same displacement: home walk corrects.
5. GPS mode after 5 minutes of operation: place-cell tile overlay is still
   empty. Behavior correct; representation absent.
```

---

Once the widget works, use it as a thinking tool:

Vary the discount factor $\gamma$ in the model-based agent. How does discount affect re-evaluation when the outcome is devalued? Is the effect immediate or gradual?

Add noise to the path-integration step counter. How does drift accumulate over long sequences? How is the failure pattern different from the displacement failure?

Try "extension-mode GPS": instead of turn-by-turn, the GPS displays the map but the user plans the route. Does the place-cell tiling fill in? This visualizes the extension/substitution distinction directly.

---

**Extension to Chapter 8.** Once Panel 1 is working, add a fourth mode: **simulation**. The agent stands at the home location, pauses, and the place-cell grid lights up in a forward replay sequence down each candidate corridor. The agent then commits to the path with the highest predicted value. This is vicarious trial and error — Tolman's visible head-bob made mechanical. Chapter 8 builds the full story of what the simulation engine is and where else the brain uses it; this exercise lets you sketch the mechanism before reading the argument.
