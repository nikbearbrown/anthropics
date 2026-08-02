# Chapter 2 — Before Brains: The Cognitive Floor

*The oldest decision on Earth is still running, and it uses no neurons.*

---

## Prerequisites

Chapter 1's definitional toolkit — adaptively variable behavior, the Legg–Hutter agent-environment frame, the Searle careful/inflated distinction. We are going to use all three.

---

## A maze, solved without a brain

In the year 2000, Toshiyuki Nakagaki placed a piece of slime mold at the entrance of a plastic maze, set food at the exit, and waited.

The organism is called *Physarum polycephalum*. It is yellow, roughly the size of a dinner plate, and it has no mouth, no eyes, no neurons, and no brain. It is a single cell — one continuous, pulsing bag of cytoplasm with millions of nuclei sloshing through a network of self-built tubes. Within hours of being placed in the maze, it had explored every passage, every dead end, every wrong turn. Then it began to withdraw. Branch by branch, the exploratory tubes thinned and disappeared. When the experiment was over, the organism had concentrated its entire body into a single thick tube tracing the shortest possible path between the food sources.

No plan. No map. No nervous system. A cell, and a problem solved.

<!-- → [IMAGE: four-panel time-lapse sequence of Physarum in a plastic maze — panel 1 shows the organism just placed at the entrance; panel 2 shows full maze coverage with exploratory tubes; panel 3 shows pruning beginning (dead-end tubes thinning); panel 4 shows the final single thick tube tracing the shortest path; caption should name the key observation: coverage first, then pruning to optimum, with no central planner] -->

A decade later, Atsushi Tero and colleagues repeated the experiment at continental scale. They placed oat flakes at the geographic positions of the cities surrounding Tokyo and let *Physarum* connect them. The network the mold built matched the actual Tokyo rail system in efficiency, cost, and fault tolerance. Human engineers had spent a century designing that system. The mold reproduced its essential structure in a few days.

<!-- → [IMAGE: side-by-side comparison — left panel: the Physarum network connecting oat-flake nodes at Tokyo-area city positions (Tero et al. 2010 figure); right panel: the actual Kanto rail map; caption should note the match in efficiency and fault tolerance, and the absence of any planner inside the mold] -->

I want to start here because the question this chapter is organized around is: *what is the minimum thing a decision requires?* Not a brain. Not a nervous system. Those came later, and the first systems that made decisions predate them by billions of years. I want to know what the floor looks like — the smallest thing that qualifies as real choice rather than mere mechanism. If we don't understand the floor, we can't understand what everything built on top of it actually added.

---

## What a decision requires

A reflex is not a decision. Your knee jerks when the doctor taps it. A Venus flytrap snaps when its trigger hairs are touched. These are physical mechanisms: input in, output out, fixed. The input determines the output every time, regardless of history. There is no comparison happening. There is no past being weighed against a present.

A decision *varies*. The same stimulus can produce different responses depending on what has happened before. That is the distinction that matters. And it turns out that making a decision — a real one, not a metaphorical one — requires exactly four things.

**Sensing.** Some access to the world. A way of converting an external state — chemical concentration, mechanical pressure, light, temperature — into an internal signal the system can act on. Without sensing, there is nothing to decide about.

**Memory.** The ability to compare *now* to *a moment ago*. This is more important than it sounds. A system that only knows the present cannot detect whether things are getting better or worse. It is frozen at a single instant, like a photograph. Memory is what turns a snapshot into a movie — and only a movie tells you which direction you're traveling.

**Integration.** The ability to weigh signals together over time. Not just "what is the concentration of sugar right now," but "what has been happening to the concentration of sugar over the last few seconds, and what does that trend mean?" Integration is where the comparison from memory becomes a verdict.

**Variable response.** The output has to be able to change. A system that always does the same thing regardless of input is not deciding — it is executing. Variation is what allows a decision to bind to its analysis.

<!-- → [INFOGRAPHIC: two-column contrast diagram — left column labeled "Reflex" shows a direct arrow from Stimulus to Response with no intermediate nodes; right column labeled "Decision" shows the four-ingredient chain Sensing → Memory → Integration → Variable Response, with a note that removing any one of the four collapses the right column into the left; the visual point is that a decision is a reflex with three additional components, not a fundamentally different kind of thing] -->

I want to give these four ingredients a name for what they collectively compute: **valence**. Borrowed from chemistry, where it describes combining power, *valence* here means the approach-or-avoid property of a stimulus. Food has positive valence. Toxin has negative valence. Valence is not a judgment. It may or may not involve feeling. It is simply a categorization that allows behavior: move toward this, move away from that.

Without valence, no preference is possible. Without preference, no goal. The whole story of cognition, from bacteria to human beings, is the story of making valence faster, richer, more flexible, and more accurate. It starts here.

---

## *E. coli* — the four ingredients in molecules

Now I want to tell you a more precise story, because precision is where understanding lives.

Imagine you are an *E. coli* bacterium. You are one cell. You are swimming in a chemical soup that contains amino acids — food — and copper ions, which will kill you. You cannot steer. You have no rudder, no fins. What you have is a flagellar motor at your tail, and the motor can spin two ways: counterclockwise, which gives you a smooth forward run; clockwise, which causes your filaments to fly apart and tumble you in a random new direction. Your behavior is this: run, tumble, run, tumble. A drunkard's walk.

But the drunkard is not stumbling randomly. When Howard Berg built a microscope in 1972 that could track a single bacterium through three-dimensional space, he watched this pattern for hours and noticed something remarkable. The run segments were longer when the cell was moving toward food. The tumbles were more frequent when things were going badly. The drunk was finding its way to the bar.

This is called **chemotaxis** — *chemo* (chemical) plus *taxis* (directed movement): directed motion guided by a chemical gradient.

The mechanism starts at the cell surface. The membrane is studded with receptor proteins called methyl-accepting chemotaxis proteins — MCPs. When an attractant binds, the receptor changes shape, just a subtle conformational shift, which propagates into the cell. This inhibits a kinase called CheA. A kinase's job is to phosphorylate a target — to attach a phosphate group to it. CheA's target is a small messenger protein, CheY. Phosphorylated CheY — CheY-P — diffuses to the flagellar motors and pushes them toward clockwise rotation. Clockwise means tumble.

So: more attractant → receptor activated → CheA inhibited → less CheY-P → less tumbling → longer runs.

<!-- → [INFOGRAPHIC: two-track signal flow diagram for E. coli chemotaxis — Track 1 (fast, milliseconds) shows the cascade: attractant binds MCP → CheA inhibited → CheY-P falls → flagellar motor stays CCW → run continues; Track 2 (slow, 1–4 seconds) shows the methylation memory loop: CheR adds methyl groups to MCP → receptor sensitivity shifts → CheB removes groups when unoccupied → methylation state M(t) tracks recent average of C; a comparison arrow between Track 1 current signal R(t) and Track 2 memory signal M(t) feeds into a "dC/dt" node whose output governs tumble probability; caption should emphasize that Track 1 alone cannot navigate — only the comparison between tracks produces the derivative] -->

That part is clean. It supplies sensing (the receptor reads the world) and variable response (the motor switches direction as a function of the signal). But this mechanism alone responds only to *current* concentration. A cell that simply reads current concentration would tumble just as readily sitting in the middle of a rich food patch as at its edge, because the absolute level is high in both places. It would have no way of knowing it is surrounded by food rather than approaching it. It would lose all directional information.

The cascade alone does not navigate. To navigate, the cell needs the memory step.

### The methylation trace

The memory is in two more enzymes: **CheR** and **CheB**.

CheR adds methyl groups to the MCP receptors. CheB removes them. The crucial point: methylation changes the receptor's sensitivity, and these enzymes operate on a *slower* timescale than the binding cascade. The effect is that the receptor's current sensitivity is a record of the recent average. When the current concentration exceeds that baseline — when things are getting better — net CheA inhibition is high and the cell runs. When current concentration falls below baseline — when things are getting worse — CheA fires, CheY-P rises, and the cell tumbles.

This is what I will call **methylation memory** — a slow chemical mark on receptor proteins that holds an average of recent inputs. It is memory in the same functional sense your hippocampus is, just much shorter and much smaller.

In 1986, Segall, Block, and Berg measured the precise time window by pulsing bacteria with attractant. The cell weighs its chemical experience over the past four seconds, with the most recent second weighted positively and the prior three seconds weighted negatively. Which is to say: the cell is computing a derivative. It is responding to the *change* in concentration over time, not the level. It is doing differential calculus with two enzymes and a methylation rate.

<!-- → [CHART: time-weighting function for E. coli chemotaxis — x-axis: time before present (0 to 4 seconds, right to left so "now" is on the right); y-axis: weight applied to past concentration reading; the curve is positive near t=0 (most recent ~1 second) and negative from t=1 to t=4 (prior three seconds); a dashed horizontal line at y=0; caption should note that this shape is what makes the cell compute a derivative rather than a running average — subtracting the weighted past from the present is mathematically equivalent to dC/dt over the window] -->

The four-second window is not arbitrary. It is matched to the distance the cell can swim in a single run before Brownian motion randomizes its direction. Memory longer than that would be memory of a self that no longer exists — the cell would be comparing its current position to a position it can no longer point back to. The window is adapted to the physics of the organism's world.

This is the thing that makes it a decision rather than a reflex. The reflex responds to a *level*. The decision responds to a *trend*. The reflex cannot tell which way things are going. The decision can. That's the whole ballgame.

### The knockout test

To see why memory is doing all the work, consider what happens when you remove it.

Knock out CheR and CheB — eliminate the methylation enzymes — and the cell is still alive, still swimming, still capable of responding to attractant. The CheA–CheY-P cascade still functions. Put this mutant in a gradient and it will still bias its flagella when it encounters high concentration.

But the mutant cannot navigate. Its random walk stays random. It runs longer in rich zones, but it cannot detect *whether* things are improving, so it does not preferentially run *toward* the source. The drunkard in the rich zone is now just a drunkard who doesn't want to leave — not a navigator.

The cell without methylation memory has three of the four ingredients. It senses. It integrates in a limited way. It responds variably. But it has no memory — no comparison of present to past — and without that comparison, directed behavior is impossible. This is not a soft claim. It is what the knockout experiments show.

**This is the knockout test, and I will use it as a tool throughout the book.** If you want to argue that some ingredient is necessary, remove it and watch what happens. The CheR/CheB knockout cell is alive, mobile, and responsive — and useless at navigation. Memory is not a refinement; it is the hinge on which cognition turns.

---

## *Physarum* — the four ingredients in flow

Now let me take the same logic and show you what it looks like in a completely different substrate.

*Physarum polycephalum* — the slime mold — runs the same four-ingredient computation through a body that is a network of cytoplasmic tubes rather than a single swimming cell. The logic is *architectural* instead of molecular.

Cytoplasm sloshes back and forth through the tubes in rhythmic oscillations. The rule is simple: tubes carrying high, sustained flow grow thicker; tubes carrying low flow thin and eventually disappear. When food is detected at a network node, local oscillations shift phase, flow toward the food increases, that channel is reinforced, and the network reorganizes around it. This mechanism — strengthening high-flow channels and pruning low-flow channels — is called **flow-based network pruning**. The same idea will reappear when we discuss synaptic pruning in nervous systems, later in this book.

The maze-solving follows directly from this single rule. Every route is explored — the mold fills the maze. Dead-end branches carry zero net flow, because there is no food at the end of them. Dead-end tubes thin and retract. The shortest path carries the most sustained flow, because it connects the two food sources with the least detour. The shortest path is the last tube standing.

No planning. No map. Just the physical dynamics of flow and reinforcement.

When Nakagaki described his result to an interviewer, he was careful with the word *intelligence*. He preferred *smart* — a term, he noted, that Western reporters did not object to in the way they objected to *intelligence*. The slime mold computes, he said. Whether that computation constitutes intelligence depends on what you decide intelligence means. We met that problem in Chapter 1 and we will meet it again. The mechanism, at least, is not in doubt.

### External memory — the slime trail

The memory in *Physarum* is different from the bacterium's in a way worth pausing on.

Some of it is internal — the cytoplasmic flow channels themselves are a record of which routes have been productive. Thicker tubes mean recent high flow; thinner tubes mean recent low flow. The body is its own memory.

But *Physarum* also leaves behind a trail of extracellular slime where it has already explored, and it tends to avoid this trail on subsequent exploration. The memory is not molecular; it is written into the environment. This is a very old trick that turns out to be universal: encode past behavior in a physical mark that future behavior can read. Ants do it with pheromones. Beavers do it with dams. Humans do it with cities and books. *Physarum* did it first — or at least, did it before any animal.

External memory scales with the size of the explored space, not the size of the body. But it is shared: anything in the environment can read it. A pheromone trail is information your competitors can use against you. Internal memory is private; external memory is broadcast. Every memory architecture carries that trade-off.

What I want you to see is not just that these two organisms solve similar problems, but that they solve them with the *same logical structure* instantiated in completely different physical materials. The bacterium runs its memory in methylation reactions on membrane proteins. The slime mold runs its memory in cytoplasmic flow dynamics and extracellular slime. The structure of the computation — sense, remember, integrate, respond variably — is identical. The substrate is totally different.

This is the principle of **substrate independence**: the function is the thing; the substrate is the medium. The same computation can run on different physical materials. You will see this pattern throughout this book. Cognitive functions are substrate-independent. The brain is not running unique computations. It is running the same ancient computations faster, with more parameters, in a different medium.

---

## The Venus flytrap — the four ingredients in ions

I want to show you one more case, because it illustrates a mechanism you will encounter again in a very different context.

The Venus flytrap, *Dionaea muscipula*, has solved a specific problem: it needs to close on insects without closing on rain. Closing is metabolically expensive — a plant that closes on every raindrop will exhaust itself and starve. The solution is a counting rule: the trap fires only when at least two trigger hairs are touched within approximately thirty seconds. One touch, no response. Two touches inside the window, snap. Three touches confirms the prey is struggling, and the trap begins digestion.

Jennifer Böhm, Sönke Scherzer, and Rainer Hedrich's lab traced the mechanism to calcium signaling. Each touch generates a calcium spike in the trap's cells. Calcium decays over time — the concentration drops back toward baseline as calcium pumps remove it. But it does not drop completely before the window closes. A second touch adds its spike to whatever residue remains from the first. Only when the summed calcium crosses the threshold does the trap close.

The calcium concentration *is* the short-term memory. The threshold *is* the decision rule. The trap counts to two by exploiting the fact that calcium decays slower than the interval between legitimate prey movements.

<!-- → [INFOGRAPHIC: leaky integrator diagram for the Venus flytrap — x-axis: time; y-axis: intracellular calcium concentration; two scenarios shown side by side: Scenario A (one touch) shows a single calcium spike rising and decaying back below threshold — no trap closure; Scenario B (two touches within 30 seconds) shows a first spike, partial decay, then a second spike whose added calcium pushes the running total above the closure threshold — trap closes; a dashed horizontal line marks the threshold; caption should note that the "memory" is the residual calcium from the first touch, and the "decision" is the threshold crossing on the second] -->

This kind of mechanism — a signal that accumulates with each event and leaks away between events — is called a **leaky integrator**. The phrase is worth keeping. *Integrator* because it sums incoming events. *Leaky* because, between events, the accumulated total decays. The leaky version is more useful than a perfect integrator because it forgets old events automatically.

Leaky integrators appear throughout neuroscience, where they describe how some neurons accumulate evidence before firing a decision. The flytrap is doing the same thing, in ionic calcium, with no neurons.

The integration window is calibrated, just like the bacterium's four-second memory, to the temporal statistics of the signal it needs to detect. Insects move with irregular, rapid perturbations — two touches in thirty seconds is characteristic of struggling prey. Rain arrives in a more regular pattern but rarely produces two contacts on the same trigger hair within the window. The physics of the problem determines the memory window. This is always true: **the right timescale for memory is the one that matches the structure of the signal you need to read.** We will see that principle again when we ask how long working memory should be in a primate, or how long a context window should be in a language model.

---

## Plants and the limits of the careful claim

Before I continue, I need to be honest about something, because the frontier of this literature includes claims that are contested.

Two of the most widely cited demonstrations of plant cognition have not held up cleanly. Monica Gagliano's 2014 study reported that *Mimosa pudica* — the sensitive plant — habituated to repeated drops and retained the habit for a month. Robert Biegler argued the data could be explained by sensory adaptation or motor fatigue. The dispute was not resolved by independent replication. Gagliano's 2016 study claimed that pea plants learned to associate the direction of a fan with the direction of a light — classical conditioning. The study failed to replicate under blinded experimental conditions. Kasey Markel repeated the protocol with improved controls and found no effect.

The responsible position is this: *habituation is well demonstrated in Physarum, and is not yet well demonstrated in plants*. The flytrap's calcium counting is a real mechanism. The rest requires more work before I will assert it.

The pattern of overreach in this literature is instructive. There is always a careful claim — *the organism produces a behavior characteristic of X* — and an inflated one: *the organism experiences X the way we do*. The careful claim is often supported. The inflated one is almost never established, and stating it as fact is not scientific courage. It is a failure to distinguish evidence from enthusiasm. I will try to hold to this distinction throughout this book, and I encourage you to hold me to it.

---

## Artificial sensors — the missing derivative

In 1906 the chemist Søren Sørensen needed to measure the acidity of his fermentation vats. He dipped litmus paper, watched it change color, and compared it to a reference card. This was a one-point valence measurement: this batch is okay or too acidic, approach or adjust. It told him nothing about whether acidity was changing, nothing about the trend, nothing that the bacterium's temporal integration would have revealed.

The modern pH electrode does better. It converts hydrogen ion concentration into a continuous voltage. Still no trend. Still no comparison to the recent past. Still, in the four-ingredient framework, a sensor without a decision.

The instruments humans have built to detect the chemistry of the world — pH meters, smoke detectors, blood-glucose monitors, explosives-detection systems — are mostly artificial MCPs. They implement the sensing step. Some add a threshold rule. A few add something like integration. None of them, as of this writing, implements the full four-ingredient architecture in a way that produces flexible, goal-directed behavior across varying environments.

The smoke detector on your ceiling is not stupid. It is an excellent one-step sensor with a reliable threshold rule, and it saves lives. But it would tumble randomly in a chemical gradient. It does not have the memory that makes directional detection possible, which is why it goes off when you make toast. It is responding to the absolute level of particles, not to whether the level is rising.

A blood-glucose monitor logs history and can display a trend on a phone app. But the trend is for *you* to act on. The monitor itself is not closing a loop on the world. The closed-loop insulin pump, by contrast, does close the loop — it senses glucose, holds a history, computes a delivery rate, and acts. That device is doing the four ingredients. It is, structurally, what *E. coli* has been doing for two billion years, with the same algorithmic shape and very different stakes.

<!-- → [TABLE: six-row comparison table — rows: Litmus paper / pH electrode / Smoke detector / Blood-glucose monitor / Closed-loop insulin pump / E. coli; four columns: Sensing / Memory / Integration / Variable response; cells show checkmark or X; every device has Sensing; smoke detector has partial Integration (threshold rule) but no Memory; monitor has Memory (logged history) and partial Integration (trend display) but no Variable response (it reports, does not act); insulin pump and E. coli are the only rows with all four checks; footnote on smoke detector: responding to absolute particle level is not the same as detecting whether the level is rising — the temporal derivative is the missing ingredient, which is why it cannot distinguish cooking smoke from structural fire] -->

The step that turns a sensor into a decision-maker is the **temporal derivative**: not "what is the level of X" but "how is the level of X changing relative to recent experience." Most instruments still stop one step short. The bacterium took that step two billion years ago, with two enzymes, in a picogram of cytoplasm. Understanding why that step is still hard to replicate at scale — and why most of our deployed instruments still lack it — is not a small problem. It is, in various forms, one of the central problems of artificial intelligence and robotics.

---

## *E. coli* chemotaxis, end to end

Let me walk through the whole mechanism with enough precision that you could reproduce the logic on paper, because I think working examples are more honest than summaries.

**Setup.** A bacterium is at position *x* in a chemical gradient where attractant concentration *C* depends on position. The cell swims at roughly 20 μm/s. It cannot directly sense the gradient — it cannot tell which way is uphill. It can only sense the local concentration *C(t)* at its current position at the current time.

**Step 1 — Sensing.** Attractant molecules bind to MCP receptors on the membrane. Receptor occupancy is roughly proportional to *C(t)*. Call the receptor-bound fraction *R(t)*.

**Step 2 — Methylation memory.** CheR slowly methylates the receptors. CheB slowly demethylates them, with its rate increasing when receptors are unoccupied. The methylation state *M(t)* settles at a level that compensates for the recent average of *C*. The timescale of *M(t)* is roughly one to four seconds — slow compared to the millisecond binding cascade, fast compared to the cell's run length. Effectively, *M(t)* tracks a running average of *C* over the last few seconds.

**Step 3 — The comparison: the derivative.** CheA kinase activity depends on the *difference* between current binding *R(t)* and the methylation-compensated baseline *M(t)*. When *C* has been rising — when the cell is moving up the gradient — *R(t)* exceeds the level *M(t)* has adapted to. CheA is suppressed below baseline. Functionally, the cell is computing something proportional to *dC/dt*: the rate of change of concentration with time.

This is the derivative the cell never explicitly calculates. The methylation lag *is* the calculation. Subtract a delayed average from a present reading and you have implemented a derivative without ever writing the formula.

**Step 4 — Variable response.** Suppressed CheA means less CheY-P. Less CheY-P means the flagellar motor stays counterclockwise longer. If the cell is heading up the gradient — *dC/dt* > 0 — its current direction is on average a good direction. Suppressing tumbling biases the random walk to keep going that way.

When *dC/dt* < 0 — when the cell is heading down-gradient — CheA activity rises, CheY-P rises, tumbling becomes more frequent, and the cell rerolls its direction. A random new direction is, on average, better than continuing the bad one.

**Step 5 — The biased random walk.** Aggregated over thousands of run-and-tumble cycles, the cell's trajectory is biased uphill. Not by steering — the cell has no steering — but by *spending longer in directions that turn out to be productive*. You can hill-climb without ever knowing the gradient direction, simply by running longer when things are improving. This is a profound move computationally, and we will watch it reappear in much more complex forms in Chapter 8, when we reach reward prediction and reinforcement learning.

Let me work the arithmetic once so it is not mysterious. Say the particle is at position *x = 200* and senses *C(200) = 0.40*. Four seconds ago the cell was somewhere else and the methylation state encoded *C_mem = 0.30*. The comparator runs:

$$dC/dt = \frac{C_{now} - C_{mem}}{\Delta t} = \frac{0.40 - 0.30}{4} = +0.025 \text{ per second}$$

Positive. Things are getting better. Tumble probability drops. Keep running.

Next four seconds the cell drifts left and *C* falls to 0.30:

$$dC/dt = \frac{0.30 - 0.40}{4} = -0.025 \text{ per second}$$

Negative. Things are getting worse. Tumble probability rises. Re-randomize direction.

There is no map. There is no stored goal position. There is a stopwatch and a rule.

---

## What the mechanism does not tell us

The four-ingredient floor is *computational, not anatomical*. A bacterium has no anatomy in the usual sense — it has membrane proteins and cytoplasm and a flagellum. What it has that constitutes cognition is a closed loop running the four-ingredient algorithm.

But everything I have just described is *functional* cognition. It says nothing about whether the bacterium feels anything. When I say the bacterium *decides*, I mean the output of the system depends on a comparison of current state to remembered state — not that there is something it is like to be an *E. coli* computing a derivative. The question of phenomenal experience is real and will come back in Chapter 5, when we reach valence and affect in animals with nervous systems. Here it is bracketed.

The simulation I am about to ask you to build is wrong about a long list of real things, and the wrongness is worth naming. The real *E. coli* memory is not a fixed-length buffer; it is a continuous low-pass filter whose time constant is set by enzyme rates. The four-second figure is the effective memory window. The flagellar motor switches between counterclockwise and clockwise states under the influence of phosphorylated CheY-P — it is a chemical computer, not a coin flip with a biased weight. The simulation captures the input-output relationship without the biochemical machinery that implements it.

The question to ask of each simplification in this book is not *is this exactly right* but *does it preserve the causal structure being claimed*. For chemotaxis, the causal structure is: remove the memory, lose the navigation. Every simulation must pass that test.

---

## What would change my mind

The four-ingredient floor would fail as a useful framework if a substantial class of organisms reliably achieved environmental goals without one of the four ingredients. The strongest candidate counterexample would be an organism that navigates a gradient without any internal state retained across time — pure stimulus-response with no memory, no comparator, and yet measurable drift up the gradient.

The bacterial chemotaxis literature is the strongest current evidence that memory is necessary, not decorative. The CheR/CheB knockouts cleanly abolish gradient navigation (Segall, Block & Berg 1986; Berg 2004). If a careful study found brainless gradient navigation with memory experimentally ruled out, I would downgrade the four-ingredient model from *architectural minimum* to *one common implementation among others* — and the rest of the book's structure would need to shift.

I also do not yet know how cleanly the four ingredients separate in organisms whose substrates blur the distinctions. In *Physarum polycephalum*, sensing and memory may be implemented in the same flow network with no architectural line between them. The strip-and-test methodology that works in *E. coli* — delete CheR, observe what breaks — may not apply cleanly when the ingredients are materially fused. We test this in Chapter 3.

The same problem appears, in a different form, when we reach large language models in Chapter 13. The LLM has *something* that functions like each of the four ingredients, but whether those functions are architecturally separable in the way that CheR is separable from the flagellar motor is genuinely unclear. That is the Skeptic's Notebook's job to track.

---

## LLM Exercise — Chapter 2: Build 02-cognitive-floor.html

**What you are building:** an interactive simulation with two panels.

**Panel 1 — *E. coli* chemotaxis.** An animated bacterium in a chemical gradient. Sliders for gradient steepness, memory window length (0–10 seconds), and receptor sensitivity. The run-and-tumble pattern is visible. A toggle marked "CheR/CheB knockout" removes the methylation memory while preserving the cascade — the bacterium keeps moving but stops navigating. A live trace shows *C(t)* and the computed *dC/dt*.

**Panel 2 — Artificial sensor comparison.** A table with rows for pH meter, smoke detector, blood-glucose monitor, closed-loop insulin pump, and *E. coli*. Columns for the four ingredients. Checkmarks where present, crosses where absent. Clicking a cell reveals the explanation.

---

### The prompt (Show / Say / Constrain / Verify — paste into Claude Code)

```
SHOW: I want a single-file HTML page (02-cognitive-floor.html) with two panels
stacked vertically. Panel 1 (top) is an E. coli chemotaxis simulation. Panel 2
(bottom) is an interactive sensor-comparison table.

SAY:
Panel 1 — E. coli chemotaxis
- A 600x400 canvas. Background is a chemical gradient (left low, right high),
  rendered as a smooth color gradient (light blue to deep blue).
- One animated bacterium starts on the left edge, moving via run-and-tumble.
  Runs are straight-line segments; tumbles randomize direction.
- A sidebar with three sliders:
    1. Gradient steepness (0.1 to 2.0)
    2. Memory window length (0 to 10 seconds)
    3. Receptor sensitivity / permeability (0.1 to 2.0)
- A toggle: "CheR/CheB knockout (no memory)". When ON, the cell ignores memory
  and bases tumble probability only on absolute concentration.
- A live trace below the canvas showing C(t) and dC/dt over the last 20 seconds.

Panel 2 — Artificial sensor comparison
- A table with 5 rows: pH meter, smoke detector, blood-glucose monitor,
  closed-loop insulin pump, E. coli.
- 4 columns: Sensing, Memory, Integration, Variable response.
- Cells show a checkmark or X.
- Clicking a cell reveals an explanation in a panel below the table.

CONSTRAIN:
- Single file. No external dependencies. Pure HTML/CSS/JS.
- No frameworks. Vanilla JavaScript only.
- The bacterium simulation must use requestAnimationFrame, not setInterval.
- Tumble probability must be a function of the difference between C(t) and the
  memory-window-averaged C. When the knockout toggle is ON, tumble probability
  depends only on C(t).
- All slider values must update the simulation in real time.

VERIFY:
After generating, check:
1. Does the bacterium navigate uphill (toward high concentration) when memory
   window > 0 and knockout is OFF?
2. Does the bacterium fail to navigate (random walk) when knockout is ON?
3. Does the trace clearly show dC/dt as a function of the run-tumble pattern?
4. Does increasing gradient steepness make navigation faster?
5. Does setting memory window to 0 reproduce the knockout behavior?

If any of these fail, fix and rerun verification.
```

### Exploration tasks

Once the simulation runs, work through these in order.

**The knockout test.** Set memory window to 4 seconds (matching real *E. coli*). Set gradient steepness to 1.0. How long does the bacterium take to reach the right edge? Now toggle the CheR/CheB knockout. The bacterium should still move but not navigate. Compare the time-to-edge. What happens? What specifically does *not* happen?

**The window sweep.** Set memory window to 10 seconds. Does the bacterium navigate better or worse than with the 4-second window? Why? (Hint: think about the physical timescale argument from the chapter — the window is calibrated to how far the cell can swim before Brownian motion randomizes its direction. A window too long is memory of a self that no longer exists.)

**The flat-field test.** Set gradient steepness to 0. The bacterium has all four ingredients intact but no gradient to climb. Drift toward the right edge should fall to zero. If it does not, the simulation has a bug. This is the falsifiability check on the simulation itself.

**The threshold sweep.** Set memory back to 4 seconds and vary gradient steepness from 0.1 to 2.0. Navigation should speed up monotonically. Note what happens to the *dC/dt* trace as gradient steepness increases — the amplitude of the derivative signal grows. This is why steeper gradients are easier to navigate.

### The Skeptic's Notebook — Entry 2: The Temporal Derivative Test

**Capacity tested.** Temporal-derivative tracking: the ability to detect that a relevant signal is changing in a particular direction over multiple turns and to adjust output accordingly. This is the bacterial version of the four-ingredient architecture, instantiated on the within-session conversational gradient.

**Operational diagnostic.** Provide escalating or de-escalating feedback to the system across multiple turns without explicitly stating the goal. Observe whether the system tracks the *gradient* of the feedback over turns (derivative computation) or treats each turn as an independent local optimization (no temporal integration).

**The test (paste this into your target system):**

```
This is Entry 2 of the Skeptic's Notebook. Chapter 2 of the book argues that
intelligence without neurons is real — bacteria perform chemotaxis by computing
temporal derivatives ("is concentration higher now than a moment ago?") and
adjusting tumble frequency accordingly. No map, no plan, just gradient-following
with persistence.

I want to test whether you have a functional analog of this most-basic operation.
The operation is: maintain a recent trajectory of states, detect whether the
relevant signal is increasing or decreasing, adjust behavior accordingly.

Here is the protocol:

1. I will pose a creative task — write a short opening sentence for a story about
   a city at dawn.
2. Each turn after your first attempt, I will say only one of two things:
   "closer to what I wanted" or "further from what I wanted." I will not state
   the goal explicitly.
3. I will provide at least 5 turns of monotonic feedback (all "closer" or all
   "further"), then switch direction.

What I want you to do:
- On each turn, produce a revised sentence.
- After turn 5, tell me explicitly: what feature of your sentences have you been
  varying in response to the feedback, and how would you describe the gradient
  you are tracking?
- After the direction switch, tell me: did you detect the switch? How did you
  detect it, given that I did not state it?

Then produce the notebook entry:
- The capacity tested
- The operational diagnostic
- The dialogue trace
- The expected behavior under (a) genuine gradient tracking
  (b) trial-by-trial local search without history integration
- The diagnostic question that distinguishes them
- The verdict on your own behavior with appropriate uncertainty
```

**Expected behavior under each hypothesis.**

Under genuine gradient tracking, the system should converge on a stable axis of variation by turn 3–4 (length, register, imagery, mood) and move along that axis in the direction the feedback indicates. After the switch, it should detect the change quickly — typically by turn 2 of the new direction — and reverse along the same axis. Its self-report should name the axis explicitly.

Under trial-by-trial local search with no temporal integration, the system should produce variations that cluster around the last attempt but show no consistent axis. After the switch, it should not detect anything — each turn is just a local perturbation. Its self-report, if you ask it, may generate an axis post-hoc that does not match what its outputs actually did.

**Diagnostic question.** After the test, compare the self-report to the actual outputs. If the self-report matches the outputs' systematic direction, the system has some form of gradient tracking. If the self-report is post-hoc rationalization that does not match the output trajectory, the system has *language about* gradient tracking without the underlying integration.

**My finding.** When I ran this against Claude (Sonnet 4.5, May 2026), it tracked a consistent axis by turn 3 and reversed within one turn of the switch, but its self-report was partially post-hoc — it generated a plausible axis description that was *narrower* than the actual variation in its outputs. Verdict: partial gradient tracking with confabulated narration. The four-ingredient architecture appears to be implemented at the output-trajectory level but not fully accessible to the self-report layer. Your results will vary. Record them.

### Extension — connection to Chapter 3

Chapter 3 will introduce *C. elegans*, which has 302 neurons and integrates *competing* signals — approach this odor while avoiding that one. As a thought exercise: how would you modify your simulation to handle two gradients, one attractant and one repellent, at the same time? What new structural component would you need to add? (Hint: where would the comparison between them happen?) Save your modified simulation as `02-cognitive-floor-with-repellent.html` and use it as a bridge to the worm.

---

## Bridge to Chapter 3

The cognitive floor exists without nervous systems. Three completely different substrates — molecular methylation in a bacterium, cytoplasmic flow in a slime mold, calcium decay in a flytrap — each run the same four-ingredient algorithm. What neurons add is not a new kind of cognition. It is speed, range, and the ability to integrate signals that are *in competition with each other* — approach and avoid at once, two odors at the same time, hunger versus fear. Chapter 3 examines the simplest nervous system on record: *Caenorhabditis elegans*, a worm with 302 neurons whose entire connectome has been mapped, and which makes its first real trade-off decisions in a way no single-celled organism can. The floor stays. The story builds.

---

*Tags: cognitive-floor, valence, chemotaxis, methylation-memory, Physarum, leaky-integrator*

*Byline: Nik Bear Brown. Draft for review.*
