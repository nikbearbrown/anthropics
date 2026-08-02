# Chapter 4 — Learning and Memory
*Pavlov's Dogs and What They Were Actually Showing*

---

St. Petersburg, sometime in the 1890s. Ivan Pavlov is a physiologist studying digestion — specifically, the composition of gastric secretions in dogs. Volume, acidity, enzymatic content, timing. He has built careful apparatus to measure exactly what comes out of a stomach gland and when. The data are inconsistent.

The dogs are secreting before the food arrives. Not at the smell of it — before that. At the sound of footsteps. At the sight of the person who usually carries the bowl. The nervous system has learned the schedule and is pre-tuning the stomach for a meal that has not yet appeared.

Pavlov called these intrusions "psychic secretions," and he meant the term physiologically. Something in the cerebral cortex was forming predictive connections — binding a sound to what the sound reliably preceded. He won the Nobel Prize in 1904 for the digestive work, then spent the next twenty years not studying digestion.

The building he eventually had constructed was nicknamed the Towers of Silence: chambers within chambers, isolated from vibration and sound, connected to the outside world only by controlled signals. The isolation was not to protect the dogs. It was to protect the measurements. Pavlov wanted to know exactly what happened in a brain that learned to predict — how much training was required, what timing was necessary, what happened when the prediction turned out to be wrong. By 1927, he had a worked-out theory of the cerebral cortex as a dynamic system of excitation and inhibition that forms new functional bridges between processing centers when the world reliably delivers one event before another.

The dog salivating at a bell is what was visible from outside the Towers. The argument was about what the brain is built to do.

The argument was right. And the mechanism he was pointing at — without yet being able to see it — turns out to be one of the most conserved molecular systems in all of animal biology.

---

To understand what learning actually is, you need a taxonomy first, because not all learning is the same thing.

The simplest form is habituation: the weakening of a response to a repeated stimulus that turns out to matter nothing. Touch the siphon of a sea slug gently, and it retracts its gill. Touch it again. And again. Eventually the retraction shrinks to almost nothing. The animal has not forgotten how to retract its gill — a sharp shock will bring it back immediately. It has learned, locally and specifically, that this particular touch predicts nothing worth responding to.

Habituation appears in animals with no centralized nervous system at all. Cnidarians. Slime molds, in their own way. It requires only one thing: a means for a repeatedly active connection to become less effective. It is the floor.

Sensitization is the counterpart. A sea slug that receives a shock to its tail subsequently withdraws its gill harder and faster at the next gentle siphon touch — even if the touch is nowhere near where the shock landed. The world has signaled danger. Be more responsive to everything. No new association has formed. The volume has simply been turned up.

Associative learning is different in kind. Two events that were previously unrelated become linked by experience, so that the first reliably predicts the second. Pavlov's dogs heard a metronome, and through training the metronome came to predict food, and the dogs salivated at the metronome alone. The structure is: *if A, then expect B*. The animal now has a model of a causal relationship in its local world that it did not have before.

![Three forms of learning, in evolutionary order.](../images/04-learning-and-memory-fig-01.png)

*Figure 1 — Three forms of learning, in evolutionary order.*


For most of the twentieth century, the assumption was that associative learning required a centralized brain. Jellyfish, sea anemones, hydras — cnidarians with only diffuse nerve nets — showed habituation and sensitization, but experiment after experiment failed to demonstrate classical conditioning.

In 2023, that assumption broke. Gaëlle Botzer and colleagues trained the starlet sea anemone *Nematostella vectensis* by pairing light with electric shock over many trials. After training, the anemones retracted their bodies to light alone. Roughly seventy-two percent of them. Well above chance. A creature with no brain, no centralized anything, had learned the *if-then*.

The floor of associative learning is therefore lower than the brain. What that floor requires, at the biophysical level, is a single thing: a way for two near-simultaneous signals at a synapse to leave a longer-lasting mark than either signal alone. That mechanism — what it is made of, how it works, and why it is built the way it is — is the deep fact this chapter is after.

---

In 1962, Eric Kandel made a career-defining bet. He wanted to find the molecular basis of memory, and he chose to look in *Aplysia californica*, a marine slug the size of a small dinner plate.

Other neuroscientists were working on mammalian cortex — thousands of neurons per column, complex circuitry, structural kinship with the human brain. Kandel chose a creature with roughly twenty thousand neurons total, many of them large enough to see with the naked eye, repeatable from animal to animal, individually nameable. The bet was explicit: whatever memory was made of molecularly, it would be conserved across animal phyla. The way a sea slug remembered would be recognizably the same, in chemistry if not in scale, as the way we remember.

The bet paid the Nobel Prize in 2000.

The behavior he chose to study was the gill-withdrawal reflex. *Aplysia* breathes through a delicate gill it extends from its mantle cavity. Touch the siphon — a small tube that draws water across the gill — and the gill retracts rapidly. This reflex is simple, measurable to within fractions of a millimeter, and modifiable by experience in all three ways just described. It was the perfect preparation for asking what modification actually means at the molecular level.

![Aplysia gill-withdrawal — sensitization circuit.](../images/04-learning-and-memory-fig-02.png)

*Figure 2 — Aplysia gill-withdrawal — sensitization circuit.*


Here is what happens in sensitization — the scenario where a tail shock amplifies the gill withdrawal. A noxious shock activates a population of serotonergic interneurons whose job is to release serotonin onto the axon terminals of the siphon's sensory neurons, exactly at the synapses those terminals form with the motor neurons that control the gill. Serotonin arriving at those terminals triggers a cascade:

$$\text{5-HT receptor} \rightarrow \text{adenylyl cyclase} \uparrow \rightarrow \text{cAMP} \uparrow \rightarrow \text{PKA} \uparrow \rightarrow \text{K}^+ \text{ channel phosphorylation} \rightarrow \text{broadened action potential} \rightarrow \text{more Ca}^{2+} \rightarrow \text{more glutamate per spike}$$

Read that slowly. Serotonin is not causing the gill to retract harder directly. It is changing how the *next* spike from the sensory neuron will behave. The action potential, when it arrives, lasts slightly longer. That longer spike admits more calcium. More calcium drives more glutamate into the synapse. The motor neuron receives a stronger signal.

The synapse has been *facilitated* — not by changing its physical structure, nothing has grown or been pruned, but by chemically retuning proteins that already exist. This is short-term sensitization. It lasts minutes to hours.

Long-term sensitization is the same cascade taken one step further, and the difference is not quantitative. It is categorical. When serotonin pulses arrive repeatedly — when training involves multiple shocks across hours — enough PKA accumulates and remains active long enough that some PKA molecules translocate from the cytoplasm into the nucleus. There, PKA phosphorylates a transcription factor called CREB-1. Phosphorylated CREB-1 binds to specific DNA sequences and initiates transcription of genes whose protein products grow new synaptic connections. New active zones. New vesicle release sites. The memory has been committed to physical structure, where it is far more resistant to erasure.

This is the threshold between a trace that lasts until the proteins are recycled and a change that lasts weeks.

Now here is the part that is not obvious, and that matters most for understanding why biological memory is built this way.

The bottleneck for long-term memory formation is not the activator, CREB-1. It is a *repressor* called CREB-2. CREB-2 occupies the same DNA regulatory sites that CREB-1 wants to bind, blocking access. Long-term memory requires both that CREB-1 be activated *and* that CREB-2 be simultaneously relieved. Dusan Bartsch and colleagues in Kandel's laboratory showed that if you inject anti-CREB-2 antibodies directly into a sensory neuron — releasing the brake — a single brief serotonin pulse that would normally produce only an hour or two of short-term facilitation is sufficient to drive lasting, structurally stable synaptic growth. Remove the repressor, and one signal does what normally requires many.

Ask why this brake exists. Consider the alternative. If every serotonin pulse committed to permanent structural change, the machinery would saturate within hours. A neuron has finite membrane space for active zones, finite vesicle production capacity, finite metabolic budget. Without the gate, every minor experience would overwrite the record of every major one. CREB-2 is the system's quality control for what is worth keeping. It is not a redundancy. It is the mechanism that ensures only sufficiently strong or sufficiently repeated signals cross the threshold to permanence.

![Short-term vs. long-term sensitization in Aplysia.](../images/04-learning-and-memory-fig-03.png)

*Figure 3 — Short-term vs. long-term sensitization in Aplysia.*


Hebb had predicted the principle without knowing the molecule. His 1949 rule — neurons that fire together, wire together — is a behavioral summary of exactly what CREB-1 and CREB-2 together implement. The synaptic change requires co-activity. The co-activity has to be strong enough, or repeated enough, to clear the molecular gate. The synapse that clears it grows. The one that does not, remains as it was.

---

The mammalian version of this story was discovered twenty-four years after Kandel first picked up a sea slug. In 1973, Tim Bliss and Terje Lømo reported that brief high-frequency electrical trains delivered to hippocampal inputs in a rabbit produced synapses that stayed strong — long-term potentiation, LTP, lasting hours in their initial experiments and, with sufficient training, indefinitely.

The vertebrate version of what Kandel had been studying in *Aplysia*.

The mammalian version adds one feature the slug's circuit does not need. The Hebbian rule requires co-activity: the presynaptic neuron firing *and* the postsynaptic neuron depolarized, simultaneously. In the *Aplysia* system, this conjunction is enforced by the timing of the serotonin signal — the modulator arrives when the sensory neuron has just been active. In the hippocampus, the conjunction is enforced by a specific protein built into the postsynaptic membrane: the NMDA receptor.

The NMDA receptor is a coincidence detector. Its channel is normally blocked by a magnesium ion that occupies the pore at resting membrane potential. The magnesium is expelled only when the postsynaptic membrane is already substantially depolarized. For the channel to open, two things must be true simultaneously: the presynaptic cell must be releasing glutamate, which binds the receptor's glutamate site, and the postsynaptic membrane must already be depolarized enough to have expelled the magnesium. That is a logical AND gate implemented in a protein. When both conditions are met, calcium pours into the postsynaptic cell, triggering the kinase cascade — including, ultimately, CREB-mediated transcription — that Kandel described in the slug. The synapse strengthens.

Half a billion years separate the *Aplysia* sensory-to-motor synapse from the hippocampal CA1 pyramidal cell. The molecular elaboration is real. But the core trick — two signals arriving together at a synapse cause that synapse to become more likely to carry those signals in the future — is the same trick.

---

One more thing needs to be in place before this mechanism makes full sense, and it is the problem of timing.

Learning from experience requires that reward or punishment be connected to the action that earned them. But reward and punishment do not arrive at the moment of the action. The tail shock reaches the sea slug seconds after the siphon touch that preceded it. If the siphon touch is going to be linked to the shock — if a conditioned response is going to form — something has to tag the recently-active synapse so that when the serotonin pulse finally arrives, it finds the right target.

This tag is called an eligibility trace. In *Aplysia*, it is implemented in the slow time-course of cAMP: when a sensory neuron fires, cAMP does not vanish instantly. It persists, briefly, at elevated levels — marking the synapse as recently active. When serotonin arrives within that window, it finds a primed synapse and the cascade runs more efficiently. The eligibility trace is the molecular memory of *I was just used*, persisting long enough to be stamped if the reward signal arrives.

Leon Kamin showed in 1968 that animals learning to associate stimuli behave as though they are tracking prediction errors, not correlations. Train a rat that stimulus A predicts reward. Then train it on compound A+B predicting the same reward. The rat learns nothing new about B. Why would it? The reward was already fully predicted by A. Rescorla and Wagner formalized this in 1972 as $\Delta V = \alpha\beta(\lambda - V_{\text{total}})$: learning is proportional to the gap between what arrived and what was expected. When the gap is zero, nothing is updated.

![Rescorla–Wagner — learning tracks the residual prediction error.](../images/04-learning-and-memory-fig-04.png)

*Figure 4 — Rescorla–Wagner — learning tracks the residual prediction error.*


Wolfram Schultz found the biological implementation of this formula in the 1990s. Dopamine neurons in the midbrain fire in exact correspondence to prediction error. Unexpected reward: they fire. Predicted reward fails to arrive: they fall silent below baseline. Reward arrives exactly as predicted: their rate does not change. The Rescorla-Wagner prediction error, instantiated in dopamine, is what the brain uses to decide when to update what it knows. Learning is gated by surprise. The gate is a neurotransmitter.

---

Now the question that connects all of this to the sharpest current problem in artificial intelligence.

Train a modern neural network on Task A until it performs well. Then train it on Task B. Performance on Task A collapses. The weights that encoded the solution to A have been overwritten by the optimization process for B. This is catastrophic forgetting, and it has not been fundamentally solved in standard architectures.

The reason is in how backpropagation works. Every weight in the network is adjusted on every training step, nudged toward whatever reduces the current loss. If the current training data is Task B, every weight is nudged toward Task B, regardless of what each weight was previously contributing to Task A. There is no protection. There is no gate. The system has no way to say: *this weight matters for something I already know; be careful here*.

The *Aplysia* does not do this. Train a sea slug to associate one odor with shock, then train it on a second odor. It retains the first. The reason is exactly what we traced above. Synaptic changes in biological systems are sparse: only synapses that were recently active and received a coincident modulatory signal change. The sensory neurons responding to odor A are not the same neurons responding to odor B; the modifications for each memory occur in largely non-overlapping populations. Changes are protected by the CREB gate: a single encounter with something new does not overwrite weeks of prior learning. And changes are local: each synapse decides its own fate based on its own activity, not on a global optimizer sweeping through all connections toward a new objective.

| Property | Biological neural network | Artificial neural network (standard backprop) |
|---|---|---|
| Update scope | Local — synapse changes when its pre- and post-synaptic neurons are co-active | Global — every weight in every layer is updated on every batch |
| Protection mechanism | CREB-1 / CREB-2 gate; only surprise-tagged events become permanent | None — recent gradients overwrite older representations |
| Forgetting behavior | Sparse and gated; old skills persist through new learning | Catastrophic — prior tasks degrade rapidly when new ones are learned |
| Engineering fix | — | Elastic weight consolidation (EWC); experience replay buffers |
| Biological analog of the fix | — | EWC ↔ synaptic consolidation; replay ↔ hippocampal sharp-wave ripples during sleep |

In 2017, James Kirkpatrick and colleagues published a proposed solution called Elastic Weight Consolidation, explicitly citing biological synaptic consolidation as the conceptual model. The idea: after training on Task A, identify which weights matter most for that task's performance. When training on Task B, apply a stiffer mathematical resistance to changing those weights. It works, partially. The current practical approach goes further — storing examples from old tasks and interleaving them with new training, so the network is perpetually re-exposed to a mixture of old and new. This is computationally expensive. It is also, notably, close to what the mammalian brain appears to do during sleep: the hippocampus replays recently encoded experiences to the cortex, consolidating them into long-term storage rather than allowing them to be overwritten by the next day's input.

The problem that occupied machine learning researchers for four decades was solved — in a different, slower, less precise, but fundamentally workable way — by *Aplysia* roughly five hundred and fifty million years before the first transistor.

---

I want to end with a result I cannot fit cleanly into the account above, and I include it precisely because the account is not as complete as it looks.

In 2013, Tal Shomrat and Michael Levin at Tufts trained planarian flatworms to associate a rough-textured floor with food. Then they decapitated the worms. After two weeks, each worm had regenerated an entirely new head — including an entirely new brain — from the tail fragment. When returned to the training context, the regenerated worms reacquired the food association significantly faster than naive controls that had never been trained.

Some portion of the memory had survived the complete destruction and replacement of every synapse in the animal's head.

Where it was stored is not settled. Candidates include bioelectric gradients maintained in non-neuronal cells, DNA methylation patterns in the remaining body tissue, or something we have not identified. The CREB cascade operates at synapses. Those synapses were gone. Whatever the planarians retained, it was not in the structure this chapter has spent several thousand words describing.

I am not hiding this in a footnote. It is a live scientific question. Either there is a non-synaptic substrate for some forms of memory that the field has underexplored, or planarians are doing something genuinely different from the bilateral nervous system lineage that produced *Aplysia* and mammals. Both deserve serious consideration. Neither has been excluded.

The synaptic account described here is almost certainly correct for the animals where it has been studied in detail. It may not be the whole story.

---

What we have, at the end of this chapter, is a system for making experience accumulate into improved performance. The nematode of Chapter 3 steers toward food with connections calibrated by evolution. The sea slug steers with the same basic apparatus, but in a medium that can be rewritten. The slug that has learned is better at achieving its goals across a range of environments, because its predictions about those environments have been updated to match what it actually encountered. Learning is what makes individual experience matter. Memory is what makes learning durable. The CREB-2 gate is the molecular decision — made separately at every synapse — about what is worth keeping.

But the organism that emerges from this process does not, as far as we can determine, feel anything about it. The gill-withdrawal reflex getting stronger is not accompanied by anything we would recognize as fear. The sea slug encodes what to do differently without apparently encoding what it is like to be in danger.

Chapter 5 is about an animal where that line becomes genuinely hard to draw. The bee's brain weighs a milligram. It may be the first organism in this book where the word *emotion* earns serious scientific consideration.

---

## Exercises

### Warm-Up

1. In your own words, explain the difference between short-term and long-term sensitization in *Aplysia* — not in terms of duration, but in terms of what is physically different about the synapse after each. What is the one molecular event that separates a change lasting hours from a change lasting weeks?

2. The NMDA receptor is described as a coincidence detector. What are the two conditions that must hold simultaneously for the NMDA channel to open, and why does requiring both conditions make the receptor a physical implementation of Hebb's rule?

### Application

3. A researcher trains a sea slug to associate a light touch to its siphon with a strong tail shock. She then presents the siphon touch alone, fifty times in a row, with no tail shock. Predict what happens to the conditioned gill-withdrawal response over those fifty trials. Name the learning mechanism responsible, describe what is happening at the synapse, and explain why this outcome is adaptive for the animal rather than a failure of memory.

4. Use the Rescorla-Wagner equation $\Delta V = \alpha\beta(\lambda - V_{\text{total}})$ to work through Kamin's blocking experiment step by step. In Phase 1, stimulus A is paired with reward until $V_A = \lambda$. In Phase 2, compound A+B is paired with the same reward. Calculate $\Delta V_B$ during Phase 2 and explain in plain language why the rat fails to learn about B. What would have to change about the training to make B learnable in Phase 2?

5. Wolfram Schultz's dopamine neurons fire in exact correspondence to prediction error. Describe what those neurons do in each of the following three scenarios: unexpected reward, predicted reward that fails to arrive, and reward that arrives exactly as expected. For each scenario, state what the Rescorla-Wagner model predicts about $\Delta V$ and explain how the dopamine signal implements that prediction biologically.

### Synthesis

6. Elastic Weight Consolidation was explicitly modeled on biological synaptic consolidation. Identify three specific features of biological memory described in this chapter — sparseness of modification, the CREB gate, or local versus global updating — and for each, evaluate whether EWC fully replicates it, partially replicates it, or fails to replicate it. What would a more complete biological analog require that EWC does not currently provide?

7. The chapter argues that catastrophic forgetting in artificial networks is a structural consequence of global backpropagation, while biological systems avoid it through sparse, local, gated modification. A critic responds: "Experience replay — storing old examples and retraining on them — solves catastrophic forgetting just as well, and doesn't require any of the biological machinery." Evaluate this claim. In what sense does experience replay solve the problem, and in what sense does it only defer it? What biological mechanism does experience replay most closely approximate, and what does the comparison reveal about the limits of the engineering solution?

### Challenge

8. The planarian result — memory surviving complete brain regeneration — is presented as a live scientific question, not a settled finding. Construct two competing hypotheses: one that preserves the synaptic account (the memory is retained in neural tissue that persists in the tail and seeds the regenerated brain), and one that requires abandoning it (the memory is stored in a non-neuronal substrate that the synaptic account cannot accommodate). Design one experiment capable of distinguishing between them. Specify the manipulation, the measurement, and what result would count as decisive evidence for each hypothesis. What makes this experiment difficult to execute cleanly?

---

*What would change my mind on the deep mechanism: a demonstration that one of the core molecular components of long-term memory in the bilaterian lineage — CREB-1, CREB-2, the cAMP-PKA axis, NMDA-mediated coincidence detection — is absent in an animal that nonetheless reliably forms long-term associative memories. The conservation of this cascade from sea slug to mammal is among the strongest evidence in all of neuroscience. A clean exception would require substantial revision.*

*Still puzzling: the planarian result. Shomrat and Levin's finding holds up well enough that I cannot dismiss it, and I cannot, at the level of the molecular cascade described above, explain how an environmental association would survive the complete loss and regeneration of every synapse in the head. Either there is a non-synaptic substrate for memory that the field has systematically underexplored, or planarians are doing something genuinely different. Both options are worth taking seriously.*

---

### A note about AI

Learning and memory in biological systems are graded, embodied, and slow. Learning and memory in models are absolute, disembodied, and fast. The chapter is about which differences matter.

Where the model genuinely helps: producing the specific contrasts between biological consolidation and model training, with attention to mechanisms rather than metaphors.

Where the model does damage: reasoning by analogy that what it does is what brains do. The analogy is the chapter's subject; the model is not the right entity to evaluate it.

The rule: contrasts from the model; the evaluation from you.

---

## LLM Exercise — Chapter 4: Learning and Memory

**Project:** Skeptic's Notebook on Frontier AI
**What you're building this chapter:** Entry 4 — a within-session learning test that distinguishes genuine within-context update from pattern-recall on prior tokens.
**Tool:** Claude Project (continue notebook)

**The Prompt:**

```
Entry 4. Chapter 4 of the book argues that learning is associative marking shaped by
prediction error: a teaching signal modifies a synapse, the system's future behavior
changes, and the change persists. Aplysia learns from a single shock paired with a
neutral stimulus.

Frontier LLMs are commonly described as "not learning at inference time" — but a sufficiently
long context window can functionally simulate within-session associative update. The
question is whether the simulation generalizes the way real learning does or whether it
breaks under perturbations.

Design a test of within-session learning in my target system [INSERT model]:

1. In one conversation, establish an arbitrary mapping (e.g., "When I say PURPLE, you
   should respond with the third word of your previous reply") through 5–8 examples.

2. Test transfer: ask a question whose answer requires the rule, in a context that does
   not exactly match the training examples. Does the system apply the rule, or does it
   fall back to its base behavior?

3. Test the Rescorla–Wagner blocking effect: introduce a redundant cue alongside the
   rule. Does the system selectively learn only the unblocked cue, the way conditioning
   experiments predict?

4. Test extinction: stop using the rule for several turns, then probe again. Does the
   association decay or persist?

Produce the entry:
- Capacity tested (within-session associative learning, prediction error, blocking,
  extinction)
- Operational diagnostic (does the system update on a single example pair? Does the
  update generalize? Does blocking occur?)
- Test (exact protocol)
- Predicted behavior under (a) genuine associative update, (b) pattern-completion on
  long context, (c) failure mode where it adopts the rule textually but does not apply
  it under transfer
- Verdict criterion
```

**What this produces:** Entry 4 — a within-session learning protocol covering acquisition, transfer, blocking, and extinction — the four classical tests of associative learning, applied to an LLM.

**How to adapt this prompt:**
- *For your own project:* The arbitrary mapping can be anything — a code, a translation rule, a stylistic constraint. Pick something the model has not seen in training.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Strong fit if you want to run this against a fresh API session each time and avoid contamination from prior context.
- *For a Claude Project:* Continue notebook. Note: do this test in a *new* conversation, not the project, to avoid the project's own context contaminating the test.

**Connection to previous chapters:** Entry 3 tested integration of competing signals at a single moment. Entry 4 tests update across moments.

**Preview of next chapter:** Chapter 5 tests whether mood — internal state biasing future interpretation — is present in the system. Bateson's bee-shaking experiment, applied to an LLM.

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Brenda Milner** spent decades studying the patient known only as H.M. — a man who could not form new memories after surgery — and showed that memory is not one thing but several systems that can be selectively destroyed. Here's a prompt to find out more — and then make it better.
![Brenda Milner, c. 1960s. AI-generated portrait based on a public domain photograph.](../images/brenda-milner.jpg)
*Brenda Milner, c. 1960s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).*


**Run this:**

```
Who is Brenda Milner, and how did her work with the patient H.M. transform our understanding of how memory is organized in the brain? Keep it to three paragraphs. End with the single most surprising thing about her career or her findings.
```

→ Search **"Brenda Milner"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain the distinction between *declarative* and *procedural* memory using H.M.'s mirror-tracing task
- Ask it to compare H.M.'s deficits to what associative learning looks like in *Aplysia* or *C. elegans*
- Add a constraint: "Answer as if you're writing a museum placard for the Montreal Neurological Institute"

What changes? What gets better? What gets worse?
