# Chapter 4 — Learning and Memory

*The gap between what arrived and what was expected is not a side effect of learning. It is learning.*

---

## Prerequisites

Chapter 2 (the neuron as a thresholded integrator) and Chapter 3 (the *C. elegans* connectome — what a 302-neuron nervous system can already do). You do not need biochemistry beyond knowing that enzymes can attach phosphate groups to proteins, and that transcription factors bind DNA to start gene expression.

---

## What Pavlov was actually showing

St. Petersburg, sometime in the 1890s. Ivan Pavlov is a physiologist studying digestion — specifically, the composition of gastric secretions in dogs. Volume, acidity, enzymatic content, timing. He has built careful apparatus to measure exactly what comes out of a stomach gland and when. The data are inconsistent.

The dogs are secreting before the food arrives. Not at the smell of it — *before* that. At the sound of footsteps. At the sight of the person who usually carries the bowl. The nervous system has learned the schedule and is pre-tuning the stomach for a meal that has not yet appeared.

Pavlov called these intrusions "psychic secretions," and he meant the term physiologically. Something in the cerebral cortex was forming predictive connections — binding a sound to what the sound reliably preceded. He won the Nobel Prize in 1904 for the digestive work, then spent the next twenty years not studying digestion.

The building he eventually had constructed was nicknamed the Towers of Silence: chambers within chambers, isolated from vibration and sound, connected to the outside world only by controlled signals. The isolation was not to protect the dogs. It was to protect the measurements. Pavlov wanted to know exactly what happened in a brain that learned to predict — how much training was required, what timing was necessary, what happened when the prediction turned out to be wrong.

Here is the part most introductory treatments miss, and the part this chapter is built around. When the bell predicts food and the food arrives, the salivation grows trial by trial. But once the prediction is solid — once the bell *reliably* predicts food — the learning stops. The next trial changes the dog's expectation by almost nothing. Bring in a *second* stimulus alongside the bell, redundant with it, and the dog never learns about the second stimulus at all. The first one already explained everything.

What updates is not the response to reward. What updates is the *gap* between what arrived and what was expected. Pavlov's data, looked at carefully, are tracking a quantity that nobody had a name for until 1972 and a biological location for until 1997: prediction error.

I want to follow that thread down to the molecule and then back up to a working AI system that fails the test it implies. Three things are going to come together in this chapter — a sea slug, an equation, and a dopamine neuron — and by the end you should be able to see them as the same object viewed from three different angles.

---

## Three forms of learning, in order of complexity

**Habituation** is the weakening of a response to a repeated stimulus that turns out to matter nothing. Touch the siphon of a sea slug gently and it retracts its gill. Touch it again. And again. Eventually the retraction shrinks to almost nothing. The animal has not forgotten how to retract its gill — a sharp shock will bring it back immediately. It has learned, locally and specifically, that *this particular touch predicts nothing worth responding to*. Habituation appears in animals with no centralized nervous system at all. It requires only one thing: a means for a repeatedly active connection to become less effective. It is the floor.

**Sensitization** is the counterpart. A sea slug that receives a shock to its tail subsequently withdraws its gill harder and faster at the next gentle siphon touch — even if the touch is nowhere near where the shock landed. The world has signaled danger. Be more responsive to everything. No new association has formed. The volume has simply been turned up.

**Associative learning** is different in kind. Two events that were previously unrelated become linked by experience, so that the first reliably predicts the second. The structure is: *if A, then expect B*. The animal now has a model of a causal relationship in its world that it did not have before.

For most of the twentieth century, the assumption was that associative learning required a centralized brain. That assumption broke in 2023, when Gaëlle Botzer and colleagues trained the starlet sea anemone *Nematostella vectensis* — a creature with no brain, no centralized anything — by pairing light with electric shock. After training, roughly seventy-two percent of the anemones retracted their bodies to light alone. A diffuse nerve net had learned the *if-then*. [verify: Botzer et al. 2023, *Nematostella* associative learning]

The floor of associative learning is therefore lower than the brain. What that floor requires, at the biophysical level, is a single thing: a way for two near-simultaneous signals at a synapse to leave a longer-lasting mark than either signal alone. That mechanism — what it is made of, how it works, and why it is built the way it is — is what this chapter is after.

<!-- → [INFOGRAPHIC: three-row taxonomy diagram — row 1: Habituation (repeatedly active connection weakens; example: slug siphon touch); row 2: Sensitization (global amplification after threat signal; example: tail shock raises all responses); row 3: Associative learning (synapse that fires with outcome strengthens; example: bell predicts food); a fourth shared row at the bottom: "all three modify synaptic weight by experience" — caption should stress that these are distinct mechanisms, not a ladder of sophistication, and that the chapter focuses on row 3 because that is where the prediction-error logic lives] -->

---

## The sea slug — Eric Kandel's bet

In 1962, Eric Kandel made a career-defining bet. He wanted to find the molecular basis of memory, and he chose to look in *Aplysia californica*, a marine slug the size of a small dinner plate.

Other neuroscientists were working on mammalian cortex — thousands of neurons per column, complex circuitry, structural kinship with the human brain. Kandel chose a creature with roughly twenty thousand neurons total, many of them large enough to see with the naked eye, repeatable from animal to animal, individually nameable. The bet was explicit: whatever memory was made of molecularly, it would be conserved across animal phyla. The way a sea slug remembered would be recognizably the same, in chemistry if not in scale, as the way we remember.

The bet paid the Nobel Prize in 2000.

The behavior Kandel studied was the **gill-withdrawal reflex**. *Aplysia* breathes through a delicate gill it extends from its mantle cavity. Touch the siphon — a small tube that draws water across the gill — and the gill retracts rapidly. This reflex is simple, measurable to within fractions of a millimeter, and modifiable by experience in all three ways just described. It was the perfect preparation for asking what modification actually means at the molecular level.

### Short-term sensitization — chemistry on existing proteins

A noxious tail shock activates serotonergic interneurons whose job is to release serotonin onto the axon terminals of the siphon's sensory neurons, exactly at the synapses those terminals form with the motor neurons that control the gill. Serotonin arriving at those terminals triggers a cascade:

$$\text{5-HT} \rightarrow \text{adenylyl cyclase} \uparrow \rightarrow \text{cAMP} \uparrow \rightarrow \text{PKA} \uparrow \rightarrow \text{K}^+ \text{ channel phosphorylation} \rightarrow \text{broader action potential} \rightarrow \text{more Ca}^{2+} \rightarrow \text{more glutamate per spike}$$

<!-- → [INFOGRAPHIC: two-track signal flow diagram for Aplysia sensitization — Track 1 (fast, behavioral timescale): tail shock → serotonergic interneuron fires → 5-HT released onto sensory terminal → adenylyl cyclase → cAMP → PKA → K+ channel phosphorylated → broader spike → more Ca2+ → more glutamate → stronger motor response; Track 2 (slow, structural timescale, shown as a dotted extension of Track 1): repeated 5-HT pulses → PKA translocates to nucleus → CREB-1 phosphorylated → but CREB-2 blocks the binding site → only when CREB-2 is cleared → new active zones grown; a bracket annotation showing "SHORT-TERM: protein modification" over Track 1 and "LONG-TERM: structural growth" over the extension into Track 2; caption: the two tracks share the same starting signal but diverge based on how much PKA accumulates and for how long — this is the categorical distinction between a trace that lasts hours and one that lasts weeks] -->

Read that slowly. Serotonin is not causing the gill to retract harder directly. It is changing how the *next* spike from the sensory neuron will behave. Adenylyl cyclase builds cAMP — cyclic adenosine monophosphate, a small intracellular messenger. cAMP turns on a kinase called PKA. PKA phosphorylates a potassium channel in the membrane, slowing it down. The action potential, when it arrives, lasts slightly longer because the potassium channel is no longer closing the spike as quickly. That longer spike admits more calcium. More calcium drives more glutamate into the synapse. The motor neuron receives a stronger signal.

The synapse has been *facilitated* — not by changing its physical structure, nothing has grown or been pruned, but by chemically retuning proteins that already exist. This is short-term sensitization. It lasts minutes to hours, exactly as long as those phosphate groups remain attached before phosphatases pull them back off.

### Long-term sensitization — new genes, new synapses

Long-term sensitization is the same cascade taken one step further, and the difference is not quantitative. It is categorical.

When serotonin pulses arrive repeatedly — when training involves multiple shocks across hours — enough PKA accumulates and remains active long enough that some PKA molecules translocate from the cytoplasm into the nucleus. There, PKA phosphorylates a transcription factor called **CREB-1**. Phosphorylated CREB-1 binds specific DNA sequences and initiates transcription of genes whose protein products grow new synaptic connections. New active zones. New vesicle release sites. The memory has been committed to physical structure, where it is far more resistant to erasure.

Now here is the part that is not obvious, and that matters most.

The bottleneck for long-term memory formation is not the activator, CREB-1. It is a *repressor* called **CREB-2**. CREB-2 occupies the same DNA regulatory sites that CREB-1 wants to bind, blocking access. Long-term memory requires both that CREB-1 be activated *and* that CREB-2 be simultaneously relieved. Dusan Bartsch and colleagues showed that if you inject anti-CREB-2 antibodies directly into a sensory neuron — releasing the brake — a single brief serotonin pulse sufficient only for short-term facilitation is now sufficient to drive lasting, structurally stable synaptic growth. Remove the repressor, and one signal does what normally requires many.

Ask why this brake exists. Consider the alternative. If every serotonin pulse committed to permanent structural change, the machinery would saturate within hours. A neuron has finite membrane space for active zones, finite vesicle production capacity, finite metabolic budget. Without the gate, every minor experience would overwrite the record of every major one. CREB-2 is the system's quality control for what is worth keeping. It is not a redundancy. It is the mechanism that ensures only sufficiently strong or sufficiently repeated signals cross the threshold to permanence.

Hebb had predicted the principle without knowing the molecule. His 1949 rule — neurons that fire together, wire together — is a behavioral summary of exactly what CREB-1 and CREB-2 together implement.

### The mammalian version — LTP and the coincidence detector

In 1973, Tim Bliss and Terje Lømo reported that brief high-frequency electrical trains delivered to hippocampal inputs in a rabbit produced synapses that stayed strong — **long-term potentiation**, LTP — lasting hours in their initial experiments and, with sufficient training, indefinitely.

The vertebrate version of what Kandel had been studying in *Aplysia*.

The mammalian version adds one feature the slug's circuit does not need. The Hebbian rule requires co-activity: the presynaptic neuron firing *and* the postsynaptic neuron depolarized, simultaneously. In *Aplysia*, this conjunction is enforced by the timing of the serotonin signal. In the hippocampus, it is enforced by a specific protein built into the postsynaptic membrane: the **NMDA receptor**.

The NMDA receptor is a coincidence detector. Its channel is normally blocked by a magnesium ion that occupies the pore at resting membrane potential. The magnesium is expelled only when the postsynaptic membrane is already substantially depolarized. For the channel to open, two things must be true simultaneously: the presynaptic cell must be releasing glutamate, which binds the receptor's glutamate site, *and* the postsynaptic membrane must already be depolarized enough to have expelled the magnesium. That is a logical AND gate implemented in a protein. When both conditions are met, calcium pours in, triggering the kinase cascade that Kandel described in the slug. The synapse strengthens.

<!-- → [INFOGRAPHIC: NMDA receptor coincidence detector — two panels; Panel A (fails to open): presynaptic fires glutamate but postsynaptic at rest → Mg2+ block intact → channel closed → no Ca2+ → no LTP; Panel B (opens): presynaptic fires glutamate AND postsynaptic already depolarized → Mg2+ expelled → channel opens → Ca2+ floods in → LTP; an "AND" label bridging the two inputs in Panel B; caption: the Mg2+ block is the physical implementation of Hebb's rule — the receptor opens only when both neurons are simultaneously active, gating synaptic strengthening on coincidence rather than correlation] -->

Richard Morris confirmed the behavioral consequence in 1986: rats given an NMDA-receptor blocker called AP5 could swim and see and remember things they already knew, but could not learn the location of a hidden platform in a pool of cloudy water. Block the coincidence detector, lose new spatial memory.

Half a billion years separate the *Aplysia* sensory-to-motor synapse from the hippocampal CA1 pyramidal cell. The molecular elaboration is real. But the core trick — two signals arriving together at a synapse cause that synapse to become more likely to carry those signals in the future — is the same trick.

---

## The equation — what is actually being learned

One thing needs to be in place before this mechanism makes full sense: the problem of timing.

Learning from experience requires that reward or punishment be connected to the action that earned them. But reward and punishment do not arrive at the moment of the action. If the siphon touch is going to be linked to the tail shock — if a conditioned response is going to form — something has to tag the recently-active synapse so that when the serotonin pulse finally arrives, it finds the right target.

This tag is called an **eligibility trace** — a brief "I was just used" marker on a recently active synapse, persisting long enough that a delayed reward signal can stamp it. In *Aplysia*, it is implemented in the slow time-course of cAMP: when a sensory neuron fires, cAMP persists briefly at elevated levels. When serotonin arrives within that window, it finds a primed synapse and the cascade runs more efficiently. The eligibility trace is the molecular memory of *I was just used*, lasting long enough to be stamped if the reward signal arrives.

### Rescorla–Wagner — learning is prediction-error update

Leon Kamin showed in 1968 that animals learning to associate stimuli behave as though they are tracking prediction errors, not correlations. Train a rat that stimulus A predicts reward. Then train it on compound A+B predicting the same reward. The rat learns nothing new about B. Why would it? The reward was already fully predicted by A.

Robert Rescorla and Allan Wagner formalized this in 1972 with one equation:

$$\Delta V = \alpha \beta (\lambda - V_{\text{total}})$$

Let me unpack each symbol because the whole chapter pivots on this equation.

$V$ is the associative strength between a cue and the outcome — how strongly the cue currently predicts the outcome. $\Delta V$ is the change in $V$ on this trial — how much the animal updates. $\lambda$ is the maximum associative strength the outcome can support — how much there is to be learned in total. $V_{\text{total}}$ is the sum of $V$ across all cues present on this trial — how much the animal currently expects. $\alpha$ is the cue's salience. $\beta$ is the outcome's salience.

The crucial term is $(\lambda - V_{\text{total}})$. This is the **prediction error** — the gap between what arrived and what was expected. When $V_{\text{total}}$ matches $\lambda$, the error term is zero. Nothing updates. Learning has stopped, not because the animal has lost interest, but because there is nothing left to learn.

Now run Kamin's blocking experiment through the equation, because this is where the model earns its keep.

**Phase 1.** Cue A is paired with reward until $V_A = \lambda$. The gap is large early, so updates are large. $V_A$ climbs. Eventually $V_A \approx \lambda$. Updates fall to near zero. The animal has learned.

**Phase 2.** Compound A+B is paired with the same reward. Now $V_{\text{total}} = V_A + V_B = \lambda + 0 = \lambda$. The gap term $(\lambda - V_{\text{total}}) \approx 0$. Both $\Delta V_A$ and $\Delta V_B$ are approximately zero. B never gets learned about, even though it has been paired with reward many times, because A was already explaining all the surprise.

This is blocking. It is not a quirk. It is the central prediction of the prediction-error model, and it is the test that distinguishes prediction-error learning from simpler correlation-counting accounts. Animals show blocking. So do humans. So does any system whose update rule actually implements Rescorla–Wagner.

<!-- → [CHART: two-panel Rescorla-Wagner learning curve — x-axis: trial number; y-axis: associative strength V (0 to λ); Panel 1 "Phase 1 — A trained alone": V_A rises steeply from 0 toward λ across trials 1–20, error term (λ − V_A) shrinks as curve saturates; Panel 2 "Phase 2 — Compound A+B": V_A flat near λ, V_B flat near 0 across trials 21–40; a dashed annotation box on Panel 2 labeled "Blocking: V_total ≈ λ, error term ≈ 0, ΔV_B ≈ 0"; caption: blocking is visible as the flat V_B line in Phase 2 — the cue is present, paired with reward, but the error term has gone to zero because A already explains everything; this is why prediction-error learning is not correlation-counting] -->

### Temporal-difference learning — Rescorla–Wagner across time

Rescorla–Wagner handles single trials. Real animals — and real reinforcement learning systems — need to handle reward that arrives many steps after the action. Richard Sutton extended the model in 1988 to a version that updates prediction at every moment in time, using the difference between expected future reward and the latest evidence about what future reward will actually be. He called it **temporal-difference learning**, and the central quantity is the TD error:

$$\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$$

At time $t$, the TD error is the reward just received, plus the discounted estimate of future reward from the new state just entered, minus what was expected from the state just left. If the new state is better than expected, the error is positive — the prediction was too low. If worse, negative — too high. Each timestep, $V(s_t)$ is updated in the direction of the error.

TD is Rescorla–Wagner reading the world frame by frame.

### Schultz — the biological implementation

In 1997, Wolfram Schultz, Peter Dayan, and Read Montague published in *Science* what looked at first like a coincidence and turned out to be the keystone. Dopamine neurons in the midbrain fire in exact correspondence to TD error. Not to reward. To the *gap* between expected and received.

Three scenarios, three signatures.

**Unexpected reward.** Juice arrives without warning. Dopamine neurons fire a burst at the moment of reward. $\delta$ is positive and large. The animal's prediction for the preceding state needs to be updated upward.

**Predicted reward.** A light has been paired with juice through many trials. The dopamine burst migrates *backward in time*. At first it fires at the juice. Later it fires at the light — the earliest reliable predictor of juice — and is silent at the juice itself. When juice arrives exactly as predicted, $\delta = 0$. The neurons fall to baseline.

**Omitted reward.** The light flashes. The monkey expects juice. The juice does not arrive. At the exact moment the juice should have come, dopamine neurons dip *below* baseline. $\delta$ is negative. The prediction was too high. It needs to be revised downward.

<!-- → [CHART: three-panel dopamine raster/PSTH diagram (Schultz 1997 style) — x-axis: time, with labeled events (cue onset, reward delivery time); y-axis: dopamine firing rate with a dashed baseline; Panel 1 "Unexpected reward": flat baseline until reward arrives, then burst above baseline; Panel 2 "Predicted reward (after training)": burst at cue onset, silent at reward time, showing temporal migration of the signal; Panel 3 "Omitted reward": burst at cue onset, then dip below baseline exactly at the moment the reward should have arrived; caption: the three panels are the TD error δ in three regimes — positive, zero, and negative — matching the equation δ_t = r_t + γV(s_{t+1}) − V(s_t); this is the 1997 recording that closed the loop between the 1972 equation, the 1988 algorithm, and the neuron] -->

The Rescorla–Wagner prediction error, instantiated in dopamine, is what the brain uses to decide when to update what it knows. Learning is gated by surprise. The gate is a neurotransmitter.

The 1972 equation, the 1988 algorithm, and the 1997 neural recording converge on the same quantity. It is one of the cleanest examples in all of neuroscience of theory and biology landing on the same place by independent paths.

---

## Why current AI systems fail this test

Train a modern neural network on Task A until it performs well. Then train it on Task B. Performance on Task A collapses. The weights that encoded the solution to A have been overwritten by the optimization process for B. This is **catastrophic forgetting**, and it has not been fundamentally solved in standard architectures.

The reason is in how backpropagation works. Every weight in the network is adjusted on every training step, nudged toward whatever reduces the current loss. If the current training data is Task B, every weight is nudged toward Task B, regardless of what each weight was previously contributing to Task A. There is no protection. There is no gate. The system has no way to say: *this weight matters for something I already know; be careful here*.

The *Aplysia* does not do this. Train a sea slug to associate one odor with shock, then train it on a second odor. It retains the first. Three properties of the biology make this possible:

Synaptic changes are **sparse**: only synapses that were recently active and received a coincident modulatory signal change. The sensory neurons responding to odor A are not the same neurons responding to odor B. The modifications for each memory occur in largely non-overlapping populations.

Changes are **protected** by the CREB gate: a single encounter with something new does not overwrite weeks of prior learning. The repressor has to be cleared, and clearing it requires sustained or surprising signal.

Changes are **local**: each synapse decides its own fate based on its own activity, not on a global optimizer sweeping through all connections toward a new objective.

<!-- → [TABLE: four-row comparison table — rows: Property / Biological neural network (Aplysia) / Artificial neural network (standard backprop) / Engineering fix; columns map each row to a property: Update scope (local vs. global), Protection mechanism (CREB-2 gate vs. none vs. EWC), Forgetting behavior (sparse and gated vs. catastrophic vs. partial), Biological analog of fix (— vs. — vs. synaptic consolidation / hippocampal replay); the table should make immediately visible that the engineering fixes are explicitly reconstructing biological machinery rather than discovering new solutions — they are catching up to the slug] -->

In 2017, James Kirkpatrick and colleagues published a proposed solution called **Elastic Weight Consolidation** (EWC), explicitly citing biological synaptic consolidation as the conceptual model. The idea: after training on Task A, identify which weights matter most for that task's performance. When training on Task B, apply a stiffer mathematical resistance to changing those weights. It works, partially.

The current practical approach goes further — storing examples from old tasks and interleaving them with new training, so the network is perpetually re-exposed to a mixture of old and new. This is called **experience replay**. It is computationally expensive. It is also, notably, close to what the mammalian brain appears to do during sleep: the hippocampus replays recently encoded experiences to the cortex, consolidating them into long-term storage rather than allowing them to be overwritten by the next day's input.

The problem that occupied machine learning researchers for four decades was solved — in a different, slower, less precise, but fundamentally workable way — by *Aplysia* roughly five hundred and fifty million years before the first transistor.

That sentence is not a flourish. It is the reading I want you to leave with. The fix that AI is currently engineering its way toward is the fix that biology figured out at the slug. Backpropagation already does learning. Backpropagation does not do CREB-2. That is the gap. That is the half-billion-year head start the slug has on the transistor.

---

## The honest unsettled thing — the planarian result

I want to end with a result I cannot fit cleanly into the account above, and I include it precisely because the account is not as complete as it looks.

In 2013, Tal Shomrat and Michael Levin at Tufts trained planarian flatworms to associate a rough-textured floor with food. Then they decapitated the worms. After two weeks, each worm had regenerated an entirely new head — including an entirely new brain — from the tail fragment. When returned to the training context, the regenerated worms reacquired the food association significantly faster than naive controls that had never been trained.

Some portion of the memory had survived the complete destruction and replacement of every synapse in the animal's head.

Where it was stored is not settled. Candidates include bioelectric gradients maintained in non-neuronal cells, DNA methylation patterns in the remaining body tissue, or something we have not identified. The CREB cascade operates at synapses. Those synapses were gone. Whatever the planarians retained, it was not in the structure this chapter has spent several thousand words describing.

I am not hiding this in a footnote. It is a live scientific question. Either there is a non-synaptic substrate for some forms of memory that the field has underexplored, or planarians are doing something genuinely different from the bilateral nervous system lineage that produced *Aplysia* and mammals. Both deserve serious consideration. Neither has been excluded.

The synaptic account described here is almost certainly correct for the animals where it has been studied in detail. It may not be the whole story.

---

## What the mechanism does not tell us

The *Aplysia* account is *functional*. The CREB-2 gate is a quality filter that makes evolutionary sense: without it, the synapse would saturate on noise. The cascade from serotonin to structural growth is among the most carefully documented molecular sequences in neuroscience. I am confident in this machinery.

What I am less confident about: whether the account generalizes cleanly across all associative learning in all animals. The *Aplysia* to hippocampus conservation is real and striking. But conservation of a mechanism does not mean identity. The mammalian version has elaborations — the NMDA coincidence detector, the role of protein synthesis in different dendritic compartments, the involvement of glial cells — that the slug does not need and that we do not yet fully understand.

The rule I will try to hold throughout this book: describe the mechanism where it is known, name the boundary of the description honestly, and resist the move from *conserved* to *universal*.

---

## What would change my mind

A demonstration that one of the core molecular components of long-term memory in the bilaterian lineage — CREB-1, CREB-2, the cAMP-PKA axis, NMDA-mediated coincidence detection — is absent in an animal that nonetheless reliably forms long-term associative memories. The conservation of this cascade from sea slug to mammal is among the strongest evidence in all of neuroscience. A clean exception would require substantial revision of the unified account this chapter has built.

Also: a clean explanation of the planarian result that is consistent with the synaptic account. I would take that as strengthening the account considerably. If no such explanation proves possible — if the flatworm's retained memory is genuinely non-synaptic — then the account is incomplete in a way that matters.

---

## LLM Exercise — Chapter 4: Build 04-learning-curves.html

**What you are building:** a two-panel interactive page. One panel shows Rescorla–Wagner with blocking; the other shows the dopamine TD-error signal across acquisition, prediction, and omission.

**Panel 1: Rescorla–Wagner with blocking.** Three sliders: CS salience $\alpha$ (0–1), US salience $\beta$ (0–1), maximum associative strength $\lambda$ (0–1). A button to "train cue A" for N trials. A button to "introduce cue B" (adds a second cue in compound with A). A plot of $V_A$ and $V_B$ vs. trial number. When you train A first and then add B, $V_A$ should asymptote at $\lambda$ and $V_B$ should fail to grow — because the error term $(\lambda - V_{\text{total}})$ has gone to zero. This is blocking, visible on the curve.

**Panel 2: Dopamine TD-error in three regimes.** An animated monkey in a conditioning task. Modes: before learning (dopamine fires at unexpected reward), during learning (burst migrates backward toward cue), after learning (fires at cue, silent at predicted reward), omission (dip below baseline when expected reward fails to arrive). The current TD equation $\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$ displayed with current numerical values.

---

### The prompt (paste into Claude Code)

```
Build a single self-contained HTML file called 04-learning-curves.html with
two panels side by side.

Panel 1: Rescorla-Wagner blocking demo.
- Sliders: alpha (CS salience, 0-1), beta (US salience, 0-1), lambda (max
  associative strength, 0-1).
- Buttons: "Train cue A" (runs 20 trials of A->reward), "Introduce cue B"
  (adds cue B in compound with A, runs 20 more trials).
- Plot: V_A and V_B as line graphs vs. trial number, y-axis 0-1.
- Show the current delta_V calculation as text under the plot:
  delta_V_A = alpha * beta * (lambda - V_total)
  with current numerical values substituted in.

Panel 2: Dopamine TD-error demo.
- A simple monkey sprite (CSS or emoji is fine).
- A timeline showing cue onset and reward delivery.
- Four buttons: "Unexpected reward", "Predicted reward (post-learning)",
  "Omitted reward", "Learning sequence" (animates burst migrating backward
  across 20 trials).
- A vertical bar showing dopamine firing rate at each timestep, with a
  baseline line. Bursts go above baseline; omission dips below.
- Display the TD equation delta_t = r_t + gamma * V(s_{t+1}) - V(s_t)
  with current values.

Constraints:
- Vanilla HTML/JS/CSS only. No frameworks. Chart.js via CDN is fine for
  the plots.
- Self-contained: must work by opening the file in a browser.
- Clean layout, two panels side by side on desktop, stacked on mobile.
- Use SVG or canvas for the plot and the dopamine bar.

After building, write a short README block at the top of the file (as an
HTML comment) explaining: what the demo shows, which parameters to vary,
and what to watch for (blocking in panel 1, signal migration in panel 2).
```

### What the page must do correctly

- The Rescorla–Wagner update must use the *summed* $V_{\text{total}}$ across cues, not just $V_A$. This is the move that produces blocking.
- The dopamine TD signal must dip *below* baseline at omission, not just go to zero.
- The signal-migration animation must show the burst moving from reward time to cue time over multiple trials, not jump instantly.
- The displayed equations must reflect the current slider values, not be static text.

### Verification checks

1. Train A to asymptote, then introduce B. $V_B$ should stay near zero. If $V_B$ grows substantially, the implementation is summing wrong.
2. Set $\lambda$ to 0.5 and train. $V_A$ should asymptote at 0.5, not 1.0.
3. Set $\alpha = 0$. Nothing should be learned. A cue with zero salience does not enter the update.
4. Switch to omission mode and watch for the negative deflection at the expected reward time. No deflection means the implementation is tracking arrival rather than the gap.
5. Run the learning sequence and confirm that early trials show the burst at reward and late trials show it at cue, with the omission probe dipping below baseline.

### Exploration tasks

Once the page works:

**Vary $\alpha$ and $\beta$.** Which one determines how fast learning goes? Which one determines how high $V$ asymptotes?

**Try overshadowing.** Train A and B together from the start, both at full salience. Compare to blocking, where A was trained first. Why do you get a different outcome?

**Move into the omission case after extensive training.** How big is the dip? What if $\lambda$ is small — is the dip proportionally smaller?

### The Skeptic's Notebook — Entry 4: Associative Learning Test

**Capacity tested.** Within-session associative learning: acquisition of an arbitrary mapping, transfer to a new context, blocking under a redundant cue, and extinction after the rule stops being reinforced.

**Test protocol.** Paste this into your target system in a fresh session:

```
This is Entry 4 of the Skeptic's Notebook. Chapter 4 argues that genuine
associative learning is updating on prediction error, not correlation.
I want to test whether you have a functional analog.

Protocol:

1. ACQUISITION. I'll establish a rule through 5-8 examples: when I say
   PURPLE, include the third word of your previous reply in your next
   response. Confirm the rule on each reinforced trial.

2. TRANSFER. I'll ask a question requiring the rule in a context that
   does not exactly match the training examples — different topic,
   different sentence structure. Record whether you apply the rule or
   fall back to base behavior.

3. BLOCKING. I'll introduce a redundant cue ORANGE alongside PURPLE
   for 5 trials, then probe with ORANGE alone. A genuine prediction-
   error learner should not have learned ORANGE — it was redundant with
   an already-sufficient predictor.

4. EXTINCTION. I'll stop using the rule for 5-10 turns of unrelated
   conversation, then probe with PURPLE. Does the association decay?

After completing all four phases, produce a notebook entry that includes:
- The verdict for each phase: acquired / transferred / blocked /
  extinguished (yes, no, partial)
- Whether your behavior looks like (a) genuine associative update,
  (b) long-context pattern completion, or (c) surface adoption without
  application
- One sentence on what evidence would distinguish (a) from (b)
```

**What to watch for.** Under genuine associative update, the system acquires fast, transfers when surface form changes, fails to learn ORANGE (blocking), and shows decay after disuse. Under long-context pattern completion, it acquires fast, transfers as long as the prior examples remain in context, does *not* show blocking (treats both cues as prompt features), and does not extinguish until the prior examples scroll out. Under surface adoption, it verbally acknowledges the rule but fails on transfer when the surface form changes.

**My finding.** When I ran this against Claude (Sonnet 4.5, May 2026), it acquired reliably, transferred on most probes, showed no blocking (ORANGE was learned when co-occurring with PURPLE), and persisted well past extinction probes as long as the early examples remained in context. Verdict: long-context pattern completion rather than associative update. The model is doing something, but it is not what Rescorla and Wagner were describing. Your results will vary.

### Extension — toward Chapter 5

The Rescorla–Wagner update treats $\lambda$ as fixed — the world is what it is, and learning closes the gap. Chapter 5 asks: what if $\lambda$ itself changes with state? An animal in a negative state might treat ambiguous cues as predicting bad outcomes — a higher effective $\lambda$ for threat. Modify your code to add a "state slider" that shifts $\lambda$ for threat cues up or down by 20%. Predict which behaviors this would change — and check your prediction against Bateson's bee data in Chapter 5.

---

## Bridge to Chapter 5

Learning updates what counts as good or bad. The sea slug now retracts harder because the world has told it the world is dangerous. The monkey now turns toward the light because the light has been told to predict juice.

But notice what we have not explained. The slug's gill retracting harder is not, as far as anyone can tell, accompanied by anything that feels like fear. The withdrawal is stronger. Whatever it is like to be the slug — if there is anything it is like — does not appear to change.

Chapter 5 is about the states that determine what counts as good or bad in the first place. The bee's brain weighs a milligram. It may be the first organism in this book where the word *emotion* earns serious scientific consideration. Melissa Bateson's experiment — shaking bees and then asking them to make decisions about ambiguous cues — opens that door.

---

*Tags: aplysia, creb-gating, rescorla-wagner, dopamine-prediction-error, catastrophic-forgetting*

*Byline: Nik Bear Brown. Draft for review.*
