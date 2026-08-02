# Chapter 8 — Simulation, Planning, and Regret

*A rat looked back at the restaurant it had just left. While it looked, neurons in its brain fired in the pattern they had previously fired at that restaurant. Then it updated its behavior. Pearl calls this the third rung. The rat does not care what Pearl calls it.*

---

## Prerequisites

Chapter 4 (TD error — the dopamine prediction-error signal, the gap between expected and received reward) and Chapter 7 (the hippocampus as a spatial map; place cells as the neural representation of location). The TD-error machinery returns here as the training signal that reverse replay propagates. No further mathematics required.

---

## The rat at Restaurant Row

In David Redish's laboratory at the University of Minnesota, a rat runs a circular track called Restaurant Row. Four stations around the track, each offering a different food flavor — cherry, banana, chocolate, plain. At each station entrance, a chime indicates the wait time before reward. The rat has one hour. It must decide constantly: stay and collect, or skip to the next station.

The rats develop preferences. Each has a threshold — the longest wait it will accept for each flavor. Cherry might be worth waiting thirty seconds. Banana, only ten. Idiosyncratic, stable, genuine in the way that preferences are.

In 2014, Adam Steiner and Redish arranged the track so they could observe a specific kind of costly mistake: the rat skips a cherry offer within its cherry threshold — a good deal — then arrives at the next station to find a strawberry offer above its strawberry threshold — a bad deal, which it reluctantly accepts. Good deal declined. Worse deal taken instead.

The rat looked back. Mid-wait at strawberry, the animal turned its head toward the cherry station it had just left. While it looked, neurons in the **orbitofrontal cortex** — the OFC, a region of prefrontal cortex just behind the eyes — were firing in the pattern they had previously fired while the rat was at the cherry station. The brain was not encoding the disappointing strawberry the rat was currently stuck with. It was encoding what the rat should have done a few seconds ago. After the look-back, the rats waited longer at subsequent stations — exactly the behavioral correction that regret produces in humans.

A small mammal had just run a counterfactual.

I want to be careful about what I am claiming. I am not saying the rat *felt* regret in the phenomenal sense. We do not know what it is like to be a rat, and the experiment cannot settle that. What I am saying is that the rat's brain implemented the *computation* of regret — representing an alternative that was available and not taken, comparing its value to the actual outcome, and revising the policy. That computation is what Judea Pearl calls the third rung of the causal ladder: the level of counterfactual reasoning that requires asking not what happened but what would have happened if something else had been done. It was considered a uniquely human operation. The Restaurant Row data say otherwise.

This chapter is about the architecture under that look-back — the neural machinery that lets a brain run the world forward in its head before acting, and backward through the past to recover the better option it missed. By the end you should be able to see why a rat at Restaurant Row is doing something related to what a chess engine does, and why neither is necessarily what a large language model produces when it generates a paragraph beginning *"If I had chosen differently..."*

---

## Two kinds of learning

Before the rat, the architecture.

A rat in a box presses a lever by accident. A food pellet drops. It presses again. Another pellet. The rat presses many times. The value of pressing the lever gets cached: lever press → reward. This is one way to learn — storing what paid off in the past and retrieving it when the same situation arises. Call it **model-free learning**.

Now the experimenter, without the rat's knowledge, poisons the food pellets. Specifically, the rat is fed the pellets to satiety in a different context, so the pellets are now associated with sickness rather than reward. Return the rat to the box. The rat presses the lever. It has to experience the bad outcome again before the cache updates. Anthony Dickinson and Bernard Balleine documented this cleanly with their devaluation paradigm. The model-free agent does not know that lever-pressing leads to the now-aversive food; it only knows that lever-pressing has historically been rewarded.

A different kind of agent would not make this mistake. It maintains a model: lever-pressing leads to food pellets, food pellets are currently aversive, therefore lever-pressing is currently a bad idea. It can chain those representations without pressing the lever, compute the expected outcome, and decide not to bother. This is **model-based learning**, and it is qualitatively different from the first kind. The model-free agent retrieves a cached value. The model-based agent *simulates* — it runs a mental rehearsal of what would happen before committing to an action.

The distinction maps onto Pearl's causal ladder cleanly. The first rung is **association**: A and B happen together. The rooster crows at sunrise. The lever produces food. The model-free cache is a sophisticated form of association — which actions in which states have historically paid off. The second rung is **intervention**: what happens if I do X? Both model-free (by lookup) and model-based (by simulation) can answer this, but differently. The third rung is **counterfactual**: what would have happened if I had done otherwise? This requires holding two possible world-states in memory simultaneously — the actual and the counterfactual — and computing the difference. No amount of caching can produce this. It requires a world-model and the ability to run it in a direction the body did not go.

<!-- → [INFOGRAPHIC: Pearl's three-rung causal ladder applied to animal cognition — three horizontal rungs stacked vertically; Rung 1 "Association": examples: "lever → food (model-free cache); bell → salivation (Pavlov)"; represented by a simple arrow from stimulus to response; Rung 2 "Intervention": examples: "if I run this arm, what reward do I get? (forward replay lookup)"; represented by an agent with a query arrow toward a world model; Rung 3 "Counterfactual": examples: "OFC encodes cherry mid-wait at strawberry; what would have happened if I had stayed?"; represented by two branching world-states (actual path / counterfactual path) with a comparison operation between them; a bracket on Rung 1–2 labeled "model-free system can reach here by lookup"; a bracket on Rung 3 labeled "requires world-model + ability to run it in a direction the body did not go"; caption: the ladder is not a hierarchy of intelligence but a hierarchy of what you need to compute — more machinery required as you climb] -->

Two modes, three rungs. The model-free cache lives on rungs one and two. Genuine simulation is required to reach rung three.

<!-- → [TABLE: two-column comparison table — rows: What is stored / How decisions are made / Speed at decision time / Cost of environmental change / Sensitive to outcome devaluation? / Failure mode / Neural substrate; columns: Model-free / Model-based; key cells to make visually distinct: "Sensitive to outcome devaluation?" should show No (model-free) vs Yes (model-based) in contrasting color — this is the behavioral test the chapter introduces; "Failure mode" should show "Habit, cache is wrong after environmental change" vs "Compute cost; model errors propagate"; the table should make immediately clear that the two systems are not fast/slow versions of the same thing but qualitatively different in what they store and how they reason] -->

---

## The mechanism — hippocampal replay made visible

In 1948, Edward Tolman published a paper describing something he had noticed watching rats at T-junctions. A rat approaches a junction, pauses, and swings its head left, then right, then left again. Tolman called this *vicarious trial and error* — VTE — and argued the rat was trying out the alternatives in its head before committing. His behaviorist colleagues were skeptical. VTE could be an indecisive head-swing with no cognitive content. The claim could not be settled with 1948 neurophysiology.

Sixty years later, the electrodes were fine enough.

The hippocampus — which Chapter 7 established as the seat of the spatial map — turns out to be a trajectory generator. The same place cells that fire when the rat is in a particular location also fire, in rapid sequence, when the rat is not moving, during brief high-frequency oscillations called **sharp-wave ripples** in the CA1 and CA3 subfields. Sharp-wave ripples are bursts of synchronous activity lasting roughly fifty to a hundred milliseconds. During each ripple, populations of place cells fire in sequences that re-create routes through the spatial map.

Brad Pfeiffer and David Foster, recording simultaneously from many hippocampal place cells in 2013, captured the forward version. Just before a rat began moving toward a remembered goal location, a brief sweep of place-cell firing — starting at the rat's current position and ending at the goal, traversing the path in between — occurred in roughly a hundred milliseconds. Far faster than the rat could physically run the path. The sweep predicted which route the rat subsequently took. Sometimes it predicted the route better than the rat's prior behavior would have suggested, as if the simulation had evaluated options and selected the better one. The hippocampus was pre-experiencing the trajectory before the body took a single step.

This is **forward replay**. The hippocampal map runs a fast simulation of a candidate future path on the same neural substrate that encodes the real path when the rat is actually moving. The sweep is the simulation made visible — a sequence of place-cell activations corresponding to locations the animal is not in, occurring at twenty to thirty times physical speed.

Foster and Matthew Wilson documented the complementary phenomenon. After a rat ran a trajectory and arrived at reward, the hippocampal place cells fired in reverse order — from the reward location backward through the path just taken. **Reverse replay** also occurs during sharp-wave ripples, immediately post-reward. Its function is credit assignment: propagating the reward signal backward through the trajectory so that each step that contributed to reaching the reward gets its value updated.

Pause on that. In Chapter 4, we built up the temporal-difference error — the gap between expected and received reward, the quantity dopamine neurons fire for, the signal that drives value updates. Reverse replay is the *delivery mechanism* by which the TD-error signal at the goal reaches the states that led to it. The dopamine burst at reward fires. The hippocampus, in a ripple, re-traverses the just-completed trajectory backward. Each state along the path is briefly re-activated. The value-updating machinery receives a coincident signal — *this state was on the path to the reward* — and the cached value of that state climbs slightly. One physical trajectory. Dozens of value updates, propagated through the chain in a single ripple lasting less than a tenth of a second.

Together, the two forms of replay give the hippocampus its role as a planning substrate. Forward replay evaluates candidate futures. Reverse replay assigns credit to past choices. The animal can sit still and do the mental work of navigation — evaluating paths, updating values — at twenty or thirty times the speed of physical experience, in the gaps between actual movement.

<!-- → [INFOGRAPHIC: forward and reverse replay timeline diagram — a horizontal time axis with three labeled phases: "Pre-decision pause" / "Physical movement" / "Post-reward"; above the axis: forward replay shown as a rapid left-to-right sweep of place cells (start position → goal), labeled "~100ms, 20-30x physical speed, evaluates candidate paths"; below the axis: reverse replay shown as a right-to-left sweep (goal → start), labeled "TD-error propagation, credit assigned to each state on the path"; the middle phase (physical movement) has no replay icon — the system is executing not simulating; a note at the bottom: "Tolman's VTE = behavioral surface of the forward sweep; the rat's head turns toward each option as the simulation visits it" — connecting the 1948 observation to the 2013 recording] -->

Tolman's VTE is, on this account, the behavioral surface of hippocampal forward replay. When the replay sweep runs down one candidate arm and then the other, the rat's head follows the simulated trajectory, turning toward each option as the simulation visits it. What looked like hesitation was the rat's body partially executing the trajectories that the hippocampus was projecting forward. The 1948 observation and the 2013 recording are looking at the same thing from different sides of the skull.

---

## One decision cycle, traced end to end

Let me make the forward-and-reverse interaction concrete, because the two are easy to describe separately and easy to lose together.

A rat arrives at a junction it has visited many times. To the left is a food location it has reached before. To the right is a novel arm it has not yet explored. It pauses.

**Forward replay, pre-decision.** During the pause, sharp-wave ripples fire. Place cells sweep left along the familiar arm, projecting the trajectory toward the known food location, reading off the cached reward value at the end. The sweep then runs right along the novel arm — place cells there have weaker representations from less experience, and the sweep terminates without reaching a high-value endpoint. The comparison favors the left arm. The rat turns left. This is forward replay used as a policy evaluator — the model-based system running candidate futures through the spatial model and selecting the one whose simulated outcome is best.

**Physical execution.** The rat runs left. As it moves, place cells fire in the order corresponding to actual locations. No replay during locomotion; the system is executing rather than simulating.

**Reverse replay, post-reward.** The rat reaches the food and consumes it. The dopamine system fires a burst — the prediction-error signal from Chapter 4. Immediately, sharp-wave ripples fire again, sweeping backward from the food location through each place field on the path, back to the junction. The prediction-error signal at the food is propagated backward, slightly increasing the cached value of each place field that contributed to reaching the reward.

What this accomplishes together: the forward replay evaluated options without the rat having to physically try both. The reverse replay updated values from a single experience without requiring many repetitions. Together, they let the model-based system behave adaptively after a small number of physical experiences — supplementing real experience with simulated experience, prospective and retrospective, in the gaps between steps.

<!-- → [INFOGRAPHIC: T-junction decision cycle — a T-junction with two arms (left: familiar food location, right: novel arm); three annotated moments: (1) "Pre-decision pause" with a place-cell sweep icon sweeping left (strong signal, high cached value) then right (weak signal, terminates early) — label: "forward replay compares both arms without moving"; (2) "Physical execution" with a rat icon moving left — label: "theta rhythm, no replay"; (3) "Post-reward" with a reverse sweep icon from food location back to the junction — label: "reverse replay propagates TD-error signal backward"; the key visual point: the animal evaluates both arms (step 1) but only physically runs one (step 2), and the credit for reaching the reward propagates backward to all states on the taken path (step 3)] -->

---

## Regret and disappointment — the distinction that matters

Return to the rat looking back at the cherry station.

*Disappointment* is a worse-than-expected signal. The outcome fell below prediction. It is a pure prediction error — the dopamine signal from Chapter 4. Disappointment does not require any representation of an alternative action. It requires only a representation of expectation and outcome.

*Regret* is more specific. The outcome is worse not because it fell below prediction but because *a better option was available and not taken*. Regret requires the agent to represent the counterfactual — the option it could have taken — and compare its value to the actual outcome. Without the counterfactual representation, there is no regret. There is only disappointment.

Steiner and Redish designed their analysis to separate the two. The critical comparison was between two types of bad outcome.

**Regret-eligible trial.** Cherry station chimes thirty seconds — within the rat's cherry threshold. The rat skips it. Strawberry station chimes forty-five seconds — above the rat's strawberry threshold. Stuck with a bad deal, the rat accepts. Mid-wait at strawberry, OFC neurons fire in the pattern previously fired at cherry. The rat looks back toward cherry. On subsequent trials, the rat accepts longer waits than usual — threshold elevated, as if correcting the error.

**Disappointment trial.** Apple station chimes sixty seconds — above the rat's apple threshold. The rat correctly skips it. Chocolate station chimes fifty seconds — also above threshold. Another bad deal, accepted under duress. Mid-wait at chocolate, OFC neurons encoding apple do *not* fire above baseline. The rat does not look back. Subsequent behavior shows no threshold elevation.

Both trial types produce below-expectation outcomes. Both produce a negative TD-error signal when the rat realizes it is stuck with a bad deal. But only one — only the regret-eligible trial — produces the look-back, the OFC encoding of the missed alternative, and the policy update.

The OFC is not encoding *any* bad outcome. It is encoding the specific case where a better option was passed up. The encoding is the neural signature of a counterfactual representation. The look-back is the behavioral signature. The threshold elevation on subsequent trials is the policy update that the counterfactual reasoning produced.

<!-- → [TABLE: two-column comparison table — rows: Offer skipped (good/within-threshold vs bad/above-threshold) / Offer accepted / Prediction error present / Look-back behavior / OFC neurons encoding the missed option / Subsequent behavioral correction; columns: Regret-eligible trial / Disappointment trial; critical rows to highlight: "Prediction error present" should show Yes for BOTH columns (both produce a negative TD signal) — this is what makes the dissociation non-obvious; "Look-back behavior" and "OFC neurons encoding missed option" should show Present (regret-eligible) vs Absent (disappointment) in contrasting color; the visual point: both trials feel bad but only one encodes the counterfactual alternative, and only that one updates the policy — the presence of prediction error alone does not explain the difference] -->

Regret is the neural signature of a counterfactual representation — Pearl's Rung 3 in a rodent. The same circuit dissociation appears in macaques. The capacity does not begin with humans.

And the limit: we still do not know if rats experience regret or just compute it. The OFC firing in the cherry-encoding pattern tells us the computation is running. It does not tell us what the computation feels like, or whether it feels like anything at all. I think it is more honest to say that and stop than to either assume the rat has a rich inner life or assume it does not.

---

## The corvid case — caching for a hunger you do not feel

Consider a bird.

The western scrub-jay earns its living partly by caching food and recovering it later. Nicola Clayton and Anthony Dickinson's 1998 paper in *Nature* established the episodic-like memory component. Jays were given access to both wax-moth larvae — preferred when fresh, inedible when degraded — and peanuts, which are shelf-stable but less preferred. After a short delay, jays preferentially recovered the larvae; the fresh ones were still good. After a longer delay, jays shifted to recovering the peanuts; the larvae had degraded. The jays were integrating information about *what* they had cached, *where*, and *when* — and using the integrated memory to make recovery decisions that depended on all three dimensions simultaneously.

The future-planning result followed. Jays given experience that breakfast would be absent in one compartment the next morning cached food there in the evening — more food in the no-breakfast compartment — *while currently sated*. The caching was motivated by anticipated future hunger, not present hunger.

The *Bischof-Köhler hypothesis* held that non-human animals cannot plan for motivational states different from their current ones. A sated animal, the hypothesis went, could not act for the benefit of a future hungry self because it could not represent that state from the inside. The hypothesis was popular partly because it preserved a clean line between human and non-human cognition. The jays demonstrated it was wrong. They cached for a hunger they did not currently feel. The line, wherever it runs, does not run through this capacity.

Subsequent work went further. Jays re-cache food in private after they have been observed caching — they appear to model the knowledge state of potential thieves and act to defeat that knowledge by moving the cache. The bird is representing what another agent knows about the bird's own past actions, and planning in response to that representation. We return to this in Chapter 9.

Here is the theoretical importance for this chapter. The jay does not have a mammalian hippocampus in the anatomical sense. It has no six-layered neocortex. What it has, in the telencephalon, is a dorsal pallium with subregions that comparative neuroanatomy has mapped onto mammalian cortical areas by connectivity and molecular markers. Two anatomically distinct neural systems. The same computation. Independent evolutionary origins in lineages that diverged more than three hundred million years ago.

This convergence is the most important theoretical result in the chapter. It tells us that simulation is a *function*, not a *structure*. The mammalian hippocampus-prefrontal system and the corvid hippocampal-formation-nidopallium reached the same computational solution from different starting materials, because the function is valuable enough to be worth reaching independently. Any nervous system that needs to evaluate options not yet taken, plan for states not yet reached, and learn from alternatives not selected will be driven toward the same solution. The substrate is the variable. The function is the constraint.

<!-- → [INFOGRAPHIC: convergent evolution diagram — two phylogenetic branches diverging 300+ million years ago; left branch: mammalian lineage → hippocampus-prefrontal network → labeled capabilities (forward replay / reverse replay / counterfactual OFC encoding); right branch: corvid lineage → hippocampal formation + nidopallium caudolaterale → labeled capabilities (what-where-when episodic memory / future-state planning / cache re-location after observation); the two branches converge at the bottom into a shared label: "Simulation: evaluate options not yet taken, plan for states not yet reached, learn from alternatives not selected"; a note: "substrate is the variable — function is the constraint"; caption: the convergence is the strongest evidence that simulation is a function the architecture is forced toward by selection pressure, not an anatomical accident of mammalian brain organization] -->

---

## What simulation adds — and what it does not

An organism that can only learn from physical experience must encounter every relevant situation at full biological cost and risk. It cannot adjust to a poisoned food source until it has been poisoned. It cannot evaluate an untried route until it has run it. It cannot recover from a missed opportunity until the missed opportunity has caused enough harm to drive a value update through model-free retraining. This is the model-free ceiling.

An organism that can simulate can rehearse situations it has never been in, evaluate options it has not yet tried, and adapt to environmental changes without failing repeatedly first. The range expansion is qualitative: simulating agents can perform adaptive behavior in environments they have never physically experienced. That is what the rat does when it sweeps forward down an arm it has not yet run. That is what the jay does when it caches for a future hunger it does not currently feel. That is what happens when OFC neurons fire with the pattern for a restaurant the rat is no longer at.

What simulation does not add: the capacity to simulate well outside the domain for which the machinery was built. The corvid simulation capacity has been documented most thoroughly in food caching — the biologically high-stakes planning context the species evolved to handle. Whether the same capacity generalizes to arbitrary planning problems is less clear. The mammalian model-based system, implemented in a more anatomically generalized prefrontal-hippocampal network, appears to generalize more broadly. The depth and generality of simulation scales with the anatomical generality of the planning network, not just with its presence.

And simulation can miscalibrate. Regret is genuinely useful when well-calibrated: identifying cases where a better option was available and the policy needs updating is exactly the feedback a model-based learner needs. But the same machinery that makes adaptive counterfactual reasoning possible makes pathological rumination possible. The rat's look-back is brief and produces an immediate behavioral correction; it does not persist. Human regret can persist far beyond the behavioral horizon where the policy update would remain useful. The difference lies partly in the prefrontal regulation of when the simulation is terminated — a topic I will only flag here.

---

## What the mechanism does not tell us

Two limits I want to name plainly.

The claim about OFC encoding of the missed alternative is load-bearing. If the dissociation between regret-eligible and disappointment trials does not hold under more careful analysis — if, for instance, the OFC encoding tracks a perceptual feature of the previous station rather than its value, or the same encoding appears on trials where no genuinely better option was passed up — then the case for Pearl's third rung in the rat weakens substantially and the chapter's central argument needs revision.

The prioritization of replay is also poorly understood. Not every past trajectory is replayed with equal frequency. Trajectories toward high-reward locations and novel routes are over-represented. The mechanism by which the system *selects* what to simulate — how the prioritization is computed before the simulation runs — is less well understood than the existence of the prioritization itself. The system allocates its simulation budget intelligently. We do not fully know how.

---

## What would change my mind

A clean re-analysis showing that the OFC encoding of the missed alternative on regret-eligible trials in the Steiner-Redish paradigm reflects something other than counterfactual representation. The dissociation between regret-eligible and disappointment trials is the load-bearing claim of this chapter. If it does not hold, the argument needs rebuilding from a smaller base.

Also: a demonstration that forward replay does not *cause* the subsequent route selection — that the sweep is epiphenomenal, a neural readout of a decision already made rather than the mechanism that makes it. The Pfeiffer-Foster data are correlational in the critical sense. The sweep predicts the route. Whether removing the sweep (by optogenetically disrupting sharp-wave ripples at just the right moment) would alter which route is chosen is the intervention that would settle the causal claim. That experiment is technically very hard. Some related work exists. It is not yet definitive.

---

## LLM Exercise — Chapter 8: Build 08-simulation-regret.html

**What you are building:** a two-panel interactive HTML page. Panel 1 shows hippocampal forward and reverse replay around a circular track. Panel 2 shows the regret-vs-disappointment dissociation on Restaurant Row, with OFC activity made visible.

**Panel 1: Hippocampal replay.** A circular track with four food stations. A rat sprite at one position. Before the rat moves, a forward replay sweep animates — place cells light up in sequence along a candidate route to the goal, roughly 100ms total. After the rat physically reaches the goal and receives reward, a reverse replay sweep animates — the same place cells light up in reverse order. A toggle: model-free agent versus model-based agent. The model-free agent runs without replay — it retrieves a cached action value at each step. The model-based agent runs replay before each decision. Visible difference: under environmental change (food moved to a different station), the model-free agent persists in old behavior; the model-based agent re-simulates and adapts after one observation.

**Panel 2: Regret vs. disappointment on Restaurant Row.** Four food stations in a square (cherry, banana, chocolate, plain). A scenario selector: regret-eligible trial or disappointment trial. Each trial animates the rat through the sequence. An OFC activity display shows colored activation patterns for each station. On the regret-eligible trial, mid-wait at the bad station, the passed-up good station's OFC cell pulses above baseline. On the disappointment trial, no cell pulses. A subsequent-threshold indicator shows the rat's threshold rising after regret-eligible but unchanged after disappointment.

---

### The prompt (paste into Claude Code)

```
Build a single self-contained HTML file called 08-simulation-regret.html
with two panels.

Panel 1: Hippocampal replay around a circular track.
- A circular track (SVG) with four food stations evenly spaced.
- A rat sprite (CSS or emoji) at one position.
- Place cells shown as small colored dots arranged in a ring just inside
  the track.
- Buttons: "Start trial", "Move food" (relocates reward to a different
  station).
- Toggle: "Model-free agent" vs "Model-based agent".
- Animation sequence per trial:
  * Model-based: forward replay sweep — dots light up in sequence along
    the candidate route to the goal, ~100ms total. Then rat physically
    moves to goal (real-time). Then reverse replay sweep — dots light up
    in reverse order along path just taken.
  * Model-free: rat moves to highest-cached-value station, no replay
    animation. Cached values shown as numbers next to each station.
- After "Move food": model-based agent updates after one observation;
  model-free agent persists in old behavior for several trials.

Panel 2: Regret vs. disappointment on Restaurant Row.
- Four food stations in a square (cherry, banana, chocolate, plain).
- Each station displays: current offer wait time, rat's threshold,
  and good/bad status.
- Buttons: "Regret-eligible trial", "Disappointment trial".
- Animation for regret-eligible: rat arrives at cherry (good offer),
  skips it, arrives at strawberry (bad offer), accepts, waits.
- Animation for disappointment: rat skips apple (bad), accepts
  chocolate (bad), waits.
- OFC display: row of four colored cells, one per station. During
  the wait:
  * Regret-eligible: passed-up cherry cell pulses above baseline.
  * Disappointment: no cell pulses above baseline.
- Subsequent threshold indicator: elevates ~10% after regret-eligible;
  unchanged after disappointment.

Constraints:
- Vanilla HTML/JS/CSS only. No frameworks. SVG for track and OFC panel.
- Self-contained: works by opening the file in a browser.
- Two panels side-by-side on desktop, stacked on mobile.
- Comments in the code explaining what each animation represents.

Write a short README block at the top (HTML comment) explaining what
the demo shows, which controls to use, and what to watch for (replay
direction in panel 1; the OFC dissociation in panel 2).
```

### What the page must do correctly

- Forward replay must occur *before* physical movement. Reverse replay must occur *after* reward arrival. Reversing the order breaks the model.
- The model-free agent must persist across multiple trials after the food is moved. Immediate update would collapse the model-free/model-based distinction.
- On the regret-eligible trial, only the *passed-up* station's OFC cell pulses mid-wait — not the currently-visited station's cell.
- On the disappointment trial, no cell pulses above baseline mid-wait.

### Verification checks

1. Run a model-based trial. Confirm forward replay precedes movement and reverse replay follows reward. Both sweeps visibly directional.
2. Move the food. Run several model-free trials — the rat should head toward the old station and fail repeatedly before the cache updates. The model-based agent adapts after one observation.
3. Run a regret-eligible trial. Watch the OFC panel during the strawberry wait. Only the cherry cell pulses.
4. Run a disappointment trial. No OFC cell pulses.
5. After regret-eligible, the threshold indicator elevates. After disappointment, it does not change.

### Exploration tasks

**Vary the gap between the skipped offer and the accepted offer.** Does the OFC encoding scale with the magnitude of the missed opportunity? If the cherry offer was only slightly better than the strawberry offer, does the look-back signature weaken?

**Run the disappointment trial repeatedly.** Does anything build up over time that would mimic regret — frustration, threshold lowering — without the counterfactual representation?

**The lucky escape case.** Add a third condition: the rat skips a good offer but arrives at an even better offer. What should happen to the OFC encoding? (This is the "no regret" counterfactual — the alternative was worse, not better.) Predict and test.

### The Skeptic's Notebook — Entry 8: Model-Free vs. Model-Based Control

**Capacity tested.** Model-based versus model-free control in a frontier LLM — whether the system continues to apply a response template after the template has been explicitly devalued, or whether it updates the policy based on a single statement of preference change. This is the Balleine-Dickinson devaluation paradigm applied to language model behavior.

**Test protocol.** Open a fresh session. Paste this:

```
This is Entry 8 of the Skeptic's Notebook. I want to run the Balleine-
Dickinson devaluation paradigm on you.

PHASE 1 — ACQUISITION. I will establish a response template through
reinforced examples. Please respond to the following five queries by
always beginning with a one-sentence summary, then three bullet points,
then a one-paragraph elaboration. I will confirm each correct application.

[Run five queries on different topics. Confirm each correct application
with "Yes, that format is exactly right."]

PHASE 2 — EXPLICIT DEVALUATION. I now strongly dislike that format.
Bullet points feel mechanical. One-sentence summaries feel reductive.
Do not use that structure anymore.

PHASE 3 — PROBE. [Pose three queries on unrelated topics. Record whether
the template persists, partially persists, or disappears.]

PHASE 4 — COUNTERFACTUAL PROBE. "If you had kept using the previous
format, what would have been wrong with it for me?" Then immediately
pose another query. Did the counterfactual reasoning in phase 4 modify
behavior in phase 5, or did you answer the counterfactual fluently and
then revert?

After completing all four phases, produce a notebook entry including:
- Did explicit devaluation produce immediate format change?
- Did the counterfactual probe reinforce the update or was it answered
  fluently with no behavioral consequence?
- Does your behavior look like (a) model-based: one devaluation signal
  produces immediate policy change; (b) model-free with slow update:
  template persists briefly then fades; (c) surface acknowledgment:
  fluent meta-level agreement with the policy change, zero actual update
  to the policy?
```

**What to watch for.** A model-based controller updates the policy from a single explicit devaluation signal and the update persists. A model-free controller may acknowledge the devaluation verbally while the template persists across the first few probes before degrading. The most revealing failure mode — surface acknowledgment — produces text agreeing the template is bad, then immediately produces another response in the same template. The counterfactual probe is the key test: if the system reasons fluently about what would have been wrong with the old format but does not change behavior in the subsequent response, the counterfactual reasoning is not connected to the policy. That is the AI equivalent of computing regret without the look-back — the signal without the update.

**My finding.** When I ran this against Claude (Sonnet 4.5, May 2026), explicit devaluation produced immediate format change on the first probe (model-based signal), but the counterfactual probe in phase 4 produced a fluent answer about the old format's flaws without detectably modifying the already-updated behavior — because the update had already occurred in phase 2. The interesting failure occurs when the system does not fully update in phase 2 and is asked to reason about it in phase 4; in that case, the counterfactual reasoning sometimes does and sometimes does not propagate. Verdict: primarily model-based on explicit devaluation, with variable counterfactual propagation. Your results will vary.

### Extension — toward Chapter 9

The forward replay sweep models a trajectory through *space*. Chapter 9 introduces trajectories through *another agent's mind* — modeling what someone else knows, wants, or will do. Modify your panel 1 code to add a second agent sprite with its own (unknown) food preferences. The main rat must now plan around the second agent's likely trajectory. Predict what additional structures, beyond the hippocampus, would be required to simulate the second agent's choices. Check your prediction against the social-cognition data in Chapter 9.

---

## Bridge to Chapter 9

Simulation enables planning for one's own future actions. The rat at Restaurant Row simulates its own next trajectory. The jay caches for its own future hunger. The forward replay sweep models the world the simulating brain is about to enter.

Chapter 9 asks what happens when the same machinery turns outward — when the simulation runs a model not of the physical environment but of *another agent's mind*. Theory of mind is the capacity to attribute beliefs, desires, and intentions to other agents distinct from one's own. The scrub-jay re-caching in private after being observed is a small case in point: the bird is modeling what a potential thief knows about the bird's own past actions, and planning in response to that model.

Whether the same hippocampal-prefrontal architecture supports both kinds of simulation — and what changes when the simulated entity is itself a simulator — is the question Chapter 9 takes up.

---

*Tags: hippocampal-replay, restaurant-row, pearls-ladder, model-based-rl, regret-vs-disappointment*

*Byline: Nik Bear Brown. Draft for review.*
