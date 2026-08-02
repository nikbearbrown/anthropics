# Chapter 4 — Learning and Memory

St. Petersburg, sometime in the 1890s. A dog stands in a harness, a small surgical opening in its cheek leading by a fine tube to a graduated glass vessel. Drop by drop, saliva collects. In a room nearby, Ivan Pavlov is studying digestion — the composition of gastric secretions, their volume and acidity and timing, measured to the drop. He has spent years perfecting the surgery that lets him sample the juices of a living, healthy, unanaesthetized animal: the chronic fistula, an implanted opening that turns a dog into what he called, without sentiment, a factory of gastric juice. The work is meticulous. It will win him the Nobel Prize in 1904.

And the data are inconsistent. The dogs are secreting before the food arrives. Not at the smell of it — *before* that. At the sound of footsteps in the corridor. At the sight of the attendant who usually carries the bowl. The animal's body has learned the schedule and is priming its glands for a meal that has not yet appeared.

Pavlov called these intrusions "psychic secretions," and he meant the phrase physiologically, not mystically. Something in the brain was forming a connection — binding a sound to the thing the sound reliably preceded. He had set out to map the stomach. He spent the next three decades instead on the question the leaking saliva had handed him: how does a brain learn to predict?

The building he eventually had constructed for the work was nicknamed the Tower of Silence — chambers within chambers, raised on bedded foundations, sealed against vibration and street noise, the animal reachable only through controlled signals. The isolation was not for the dogs' comfort. It was to protect the measurements. Pavlov wanted to know exactly what a brain did when it learned to expect: how much training it took, what timing was required, what happened when the expectation turned out to be wrong.

Here is the part most retellings leave out, and the part this chapter is built around. When the bell predicts food and the food arrives, the salivation grows trial by trial. But once the prediction is solid — once the bell *reliably* means food — the learning stops. The next pairing changes the dog almost not at all. And if you now introduce a second signal alongside the bell, redundant with it, the dog never learns the second signal. The first one already explained everything there was to explain.

So what updates is not the response to the reward. What updates is the *gap* between what arrived and what was expected. Pavlov's leaking saliva, read carefully, is tracking a quantity that would not have a name until 1972 and a physical address in the brain until 1997: prediction error.

I want to follow that thread all the way down to a single molecule and then back up to an artificial system that fails the test the molecule implies. Three things are going to converge in this chapter — a sea slug, an equation, and a dopamine neuron — and by the end they should look like one object seen from three angles.

There are three kinds of learning, and it helps to take them in order of how much they ask of a nervous system.

The simplest is **habituation** — the fading of a response to something that keeps happening and keeps meaning nothing. Touch the siphon of a sea slug, gently, and it pulls in its gill. Touch it again. And again. The retraction shrinks each time until it nearly vanishes. The animal has not forgotten how to retract — a sharp jab brings the full response back instantly. It has learned, locally and specifically, that *this particular touch predicts nothing worth the trouble*. Habituation appears in animals with no central nervous system at all. It needs only one thing: a way for a repeatedly used connection to become less effective. It is the floor.

**Sensitization** is the mirror image. A slug that takes a shock to its tail afterward withdraws its gill harder and faster at the next gentle touch — even a touch nowhere near where the shock landed. The world has signaled danger; the sensible response is to turn up the gain on everything. No new association has formed. The volume knob has simply been raised.

**Associative learning** is different in kind. Two events that had nothing to do with each other become linked by experience, so that the first now predicts the second. The shape is always the same: *if A, then expect B*. The animal now carries a small model of a relationship in its world that it did not carry before.

For most of the twentieth century the assumption was that this last kind of learning needed a centralized brain. That assumption cracked in 2023, when Gaëlle Botton-Amiot and colleagues trained the starlet sea anemone *Nematostella vectensis* — an animal with no brain and no central anything, just a diffuse net of nerves — by pairing a flash of light with an electric shock. Trained anemones afterward retracted to the light alone, a response the untrained controls did not show. A nerve net with no center had learned the *if-then*.

So the floor of associative learning lies below the brain. What it requires, stripped to the biophysics, is a single capacity: a way for two near-simultaneous signals meeting at the same synapse to leave a longer-lasting mark than either signal leaves alone. What that mark is made of, how it is laid down, and why it is built the way it is — that is what this chapter is after.

## The sea slug

In 1962, Eric Kandel made a bet that looked, at the time, like a step backward. He wanted the molecular basis of memory, and he chose to look for it in *Aplysia californica*, a marine slug the size of a dinner plate.

Everyone serious was working on mammalian cortex — thousands of neurons to a column, intricate circuitry, structural kinship to the human brain. Kandel chose an animal with roughly twenty thousand neurons in its entire nervous system, many of them large enough to see with the naked eye, in the same place from one animal to the next, individually nameable. The wager was explicit: whatever memory turned out to be made of at the molecular level, it would be conserved across the animal kingdom. The way a slug remembered would be recognizably the same chemistry as the way you remember, differing in scale but not in kind.

The bet paid the Nobel Prize in 2000.

The behavior Kandel chose was the gill-withdrawal reflex. *Aplysia* breathes through a delicate gill it extends from a cavity in its mantle. Touch the siphon — a small spout that draws water across the gill — and the gill snaps back. The reflex is simple, measurable to a fraction of a millimeter, and modifiable by experience in all three of the ways just described. It was the perfect place to ask what *modifiable* actually means in molecules.

Take short-term sensitization first, because it is the version that changes nothing physical. A noxious tail shock activates a set of interneurons whose job is to spray serotonin onto the axon terminals of the siphon's sensory neurons — precisely at the synapses where those terminals meet the motor neurons that move the gill. The serotonin sets off a cascade, and the cascade is worth following slowly, one link at a time, because the whole chapter rests on it.

Serotonin lands on the terminal and activates an enzyme called adenylyl cyclase. Adenylyl cyclase builds up a small intracellular messenger, cyclic AMP. Cyclic AMP switches on an enzyme called PKA — a kinase, a protein whose job is to attach phosphate tags to other proteins. PKA tags a potassium channel in the membrane, and the tag slows that channel down. Now, when the next nerve impulse arrives at the terminal, it lasts slightly longer than it would have, because the potassium channel that normally cuts the impulse short is sluggish. A longer impulse holds the terminal's calcium gates open longer. More calcium floods in. More calcium drives more neurotransmitter across the synapse. The motor neuron receives a louder signal. The gill withdraws harder.

Read what just happened. The serotonin did not make the gill retract. It changed how the *next* impulse would behave — and it did so without growing anything, pruning anything, or rewiring anything. It retuned proteins that were already there. That is short-term sensitization, and it lasts exactly as long as those phosphate tags stay attached: minutes to hours, until other enzymes peel them off and the synapse drifts back to baseline.

Long-term sensitization is the same cascade pushed one step further, and the further step is not a matter of degree. It is a change in category.

When the serotonin pulses arrive repeatedly — when training means several shocks spread across hours — enough PKA builds up, and stays active long enough, that some of it migrates out of the cell body's cytoplasm and into the nucleus. There it tags a transcription factor: a protein called CREB-1 that, once tagged, binds specific stretches of DNA and switches on genes. The proteins those genes make go out and grow new synaptic connections — new release sites, new physical contacts between the sensory neuron and the motor neuron. The memory has been moved out of fleeting chemistry and into structure, where it is far harder to erase.

Now the part that is not obvious, and matters most. The bottleneck for committing a long-term memory is not the activator, CREB-1. It is a *repressor* — CREB-2 — that sits on the same DNA sites CREB-1 wants and blocks the way. To lay down a lasting memory you need both things at once: CREB-1 switched on *and* CREB-2 lifted off. Dusan Bartsch and colleagues showed this directly in 1995. Inject antibodies that mop up CREB-2 — release the brake — and a single brief serotonin pulse, normally only enough for a few minutes of short-term change, is suddenly enough to drive lasting, structural growth. Remove the repressor, and one signal does the work of many.

Ask why such a brake would exist, and the answer is a trade-off worth naming plainly. Imagine the alternative: every serotonin pulse commits to permanent structural change. Within hours the machinery saturates. A neuron has only so much membrane for new contacts, only so much capacity to make vesicles, only so much metabolic budget. Without the gate, every trivial experience would overwrite the record of every important one. CREB-2 is the cell's quality control — its rule about what is worth keeping. The cost is that learning becomes slow and grudging; you have to mean it, in repetition or in intensity, before the synapse will commit. The benefit is a memory that does not dissolve the moment something new happens. Donald Hebb had guessed at the principle in 1949 — neurons that fire together wire together — decades before anyone could name the molecules. CREB-1 and CREB-2, working against each other, are part of what that slogan turns out to mean in chemistry.

The mammalian version of all this adds one feature the slug does not need. In 1973, Tim Bliss and Terje Lømo delivered brief, high-frequency bursts to the inputs of a rabbit's hippocampus and found that the synapses there stayed strengthened afterward — long-term potentiation, lasting hours in those first experiments and, in later chronic preparations, far longer. This is the vertebrate cousin of what Kandel found in the slug. But where the slug's circuit gets its timing for free from the serotonin signal, the hippocampus enforces co-activity with a specific protein built into the receiving membrane: the NMDA receptor.

The NMDA receptor is a coincidence detector — a logic gate made of protein. Its channel is plugged, at rest, by a magnesium ion sitting in the pore. The plug pops out only when the receiving membrane is already substantially depolarized. So for the channel to open, two things must be true in the same instant: the sending neuron must be releasing glutamate, which binds the receptor, *and* the receiving membrane must already be active enough to have expelled the magnesium. Glutamate AND depolarization. When both hold, calcium pours through, and calcium is the trigger for the same kind of strengthening cascade Kandel mapped in the slug. Richard Morris showed the behavioral consequence in 1986: rats given a drug that blocks the NMDA receptor could still swim, still see, still use what they already knew — but they could not learn the location of a hidden platform in a pool of cloudy water. Block the coincidence detector and you block new spatial memory, while leaving old memory intact.

More than half a billion years separate the slug's sensory-to-motor synapse from the pyramidal cell in your hippocampus. The molecular elaboration along that distance is real. But the core trick — two signals arriving together at a synapse make that synapse more likely to carry those signals in the future — is one trick, conserved.

## The equation

There is a timing problem hidden inside all of this, and it has to be named before the mechanism makes full sense.

Learning from experience means connecting an outcome to the thing that earned it. But outcomes do not arrive at the instant of the action. The shock comes a beat after the touch. So if the touch is going to get linked to the shock, something has to *tag* the recently active synapse — mark it as "just used" — and hold that tag long enough for the delayed signal to find it and stamp it. This tag is called an eligibility trace. In *Aplysia* it lives in the slow fade of cyclic AMP: when a sensory neuron fires, its cyclic AMP stays elevated for a window afterward, and if serotonin arrives inside that window it finds a primed synapse and the cascade runs harder. The eligibility trace is the molecular memory of *I was just used* — held just long enough to be rewarded if the reward shows up. (This mapping of eligibility trace onto cyclic AMP is an interpretation, a bridge between a learning-theory idea and a piece of slug biochemistry, not a single experimental result — but it is a clean bridge.)

Leon Kamin showed in 1968 that animals learning to associate signals behave as though they track prediction errors rather than correlations. Train a rat that signal A predicts a reward. Then train it on the compound A-plus-B predicting the same reward. The rat learns nothing about B. Why would it? A already predicted everything. The reward held no surprise for B to explain. This is the blocking effect, and it is the diagnostic that separates true prediction-error learning from mere correlation-counting.

Robert Rescorla and Allan Wagner turned that intuition into a single equation in 1972:

$$\Delta V = \alpha \beta (\lambda - V_{\text{total}})$$

It pays to unpack every symbol, because the rest of the chapter pivots on this one line. $V$ is how strongly a cue currently predicts the outcome. $\Delta V$ is how much that strength changes on this trial — how much the animal updates. $\lambda$ is the most the outcome can support — the total there is to be learned. $V_{\text{total}}$ is the sum of $V$ across *all* the cues present on this trial — how much the animal currently expects, all signals added together. $\alpha$ and $\beta$ are how noticeable the cue and the outcome are.

The whole machine lives in one term: $(\lambda - V_{\text{total}})$. That is the prediction error — the gap between what arrived and what was expected. When expectation matches reality, the gap is zero, $\Delta V$ is zero, and nothing updates. Learning has stopped — not from boredom, but because there is nothing left to learn.

Run Kamin's blocking experiment through it. In phase one, cue A is paired with reward until $V_A$ climbs all the way to $\lambda$. Early on the gap is wide and the updates are large; as $V_A$ approaches $\lambda$ the gap shrinks and the updates die away. The animal has learned. In phase two, the compound A-plus-B is paired with the same reward. But now $V_{\text{total}} = V_A + V_B = \lambda + 0 = \lambda$. The gap term is already zero. Both updates are essentially zero. B never gets learned, no matter how many times it is paired with the reward, because A was already explaining all the surprise. That is blocking — not a quirk of the equation but its central prediction, the thing it gets right that correlation-counting gets wrong.

Rescorla–Wagner handles one trial at a time. But real animals, and real learning machines, face rewards that land many steps after the action that earned them. Richard Sutton extended the model in 1988 to update its prediction at every moment, comparing what it expected with the latest evidence about what is coming. He called it temporal-difference learning, and its central quantity is the TD error:

$$\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$$

At each moment, the error is the reward just received, plus the discounted estimate of future reward from the new situation, minus what was expected from the situation just left. Step into something better than expected and the error is positive: the old prediction was too low. Step into something worse and it is negative: too high. Each step nudges the prediction toward the truth. Temporal-difference learning is Rescorla–Wagner read one frame at a time.

And then, in 1997, Wolfram Schultz, Peter Dayan, and Read Montague published in *Science* a result that looked at first like a coincidence and turned out to be the keystone. The dopamine neurons of the midbrain — recorded one at a time in monkeys working for juice — fire in exact correspondence with TD error. Not with reward. With the *gap*.

Three situations, three signatures. When juice arrives with no warning, the dopamine neurons fire a burst at the moment of reward: a positive error, surprise to be learned from. When a light has been paired with juice over many trials, the burst migrates backward in time — it stops firing at the juice and starts firing at the light, the earliest reliable herald of juice, and falls silent at the juice itself, because by then nothing is surprising. And when the light flashes and the juice is withheld, at the exact instant the juice should have come the dopamine neurons dip *below* their baseline: a negative error, a prediction that was too high and must be revised down.

![Three stacked panels of dopamine firing over time, each marking a cue time and a reward time against a baseline. Top: an unpredicted reward produces a burst at reward. Middle: after the cue is learned, the burst moves to the cue and the reward draws no response. Bottom: when the learned reward is omitted, a burst still fires at the cue but the firing dips below baseline at the expected reward moment, with the dip drawn in red.](images/04-learning-and-memory-fig-01.png)

*Figure 4.1 — Dopamine tracks the prediction error: the burst migrates from reward to cue with learning, and dips below baseline (red) when an expected reward fails to arrive — something no pure reward-coder could do.*

The 1972 equation, the 1988 algorithm, and the 1997 recording all land on the same quantity. Learning is gated by surprise, and the gate is a neurotransmitter. It is one of the cleanest cases in all of neuroscience of theory and biology arriving at the same place by separate roads.

## Why the slug still wins

Train a modern neural network on Task A until it does well. Then train it on Task B. Performance on Task A collapses. The connections that encoded A have been quietly written over by the optimization for B. This is catastrophic forgetting, and it has not been solved in any fundamental way in standard architectures.

The reason is in how the learning rule works. Every weight in the network is adjusted on every training step, nudged toward whatever lowers the current error. If the current data is Task B, every weight is nudged toward Task B — regardless of what that weight was contributing to Task A. There is no protection. There is no gate. The system has no way to say: *this connection matters for something I already know; be careful here.*

The slug does not have this problem. Train *Aplysia* to associate one odor with shock, then train it on a second odor, and it keeps the first. Three features of the biology make that possible, and they map exactly onto what the engineers keep having to rebuild:

| Property | The slug (*Aplysia*) | Standard neural net | Engineering fix |
| --- | --- | --- | --- |
| Update scope | Local — each synapse decides for itself | Global — one optimizer sweeps every weight | Selective stiffening (EWC) |
| Protection of old learning | The CREB-2 gate must be cleared | None — every weight is fair game | Penalize change to important weights |
| Forgetting behavior | Sparse and gated | Catastrophic | Partial — re-exposure to old data |
| What does the protecting | Synaptic consolidation | — | Replay of stored examples |

Read down the rightmost column and the point is plain: the fixes are not new discoveries. They are reconstructions of machinery the slug already has. In 2017, James Kirkpatrick and colleagues published Elastic Weight Consolidation, which after training on Task A identifies which weights mattered most and then makes them mathematically stiffer to change while learning Task B — and which cites biological synaptic consolidation as its explicit model. It works, partially. The standard practical approach goes further still: store examples from the old tasks and interleave them with the new, so the network is forever re-exposed to a mixture. This is called experience replay, it is expensive, and it is close to what the mammalian brain appears to do in sleep, when the hippocampus replays the day's experiences to the cortex and consolidates them rather than letting tomorrow overwrite them.

The problem that occupied machine learning for four decades was solved — slowly, imprecisely, but workably — by a sea slug more than half a billion years before the first transistor. That is not a flourish; it is the reading I want you to leave with. Backpropagation already does learning. What it does not do is CREB-2. That is the gap. That is the head start the slug has on the chip.

I want to end with a result I cannot fit cleanly into any of this, precisely because the account above looks more finished than it is.

In 2013, Tal Shomrat and Michael Levin at Tufts trained planarian flatworms to associate a rough-textured floor with food. Then they cut the worms' heads off. Over about two weeks each worm regenerated an entirely new head — including an entirely new brain — from the tail fragment. Returned to the training apparatus and given a single brief refresher session, the regenerated worms reacquired the food association faster than naive worms that had never been trained. Some portion of the memory had survived the complete destruction and replacement of every neuron, every synapse, in the animal's head.

Where it was stored, nobody knows. The candidates include bioelectric gradients held in non-neuronal cells, chemical marks on the DNA of the surviving body tissue, or something not yet identified. The CREB cascade lives at synapses; those synapses were gone. Whatever the planarian kept, it was not in the structure this chapter has spent several thousand words describing. I am not tucking this into a footnote. Either there is a non-synaptic substrate for some kinds of memory that the field has underexplored, or planarians do something genuinely unlike the lineage that produced the slug and the mammal. Both deserve to be taken seriously; neither has been ruled out. The synaptic account is almost certainly right for the animals where it has been studied in detail. It may not be the whole story — and the honest version of the rule I will try to hold throughout this book is to describe the mechanism where it is known, name the edge of the description, and resist the slide from *conserved* to *universal*.

There is one more thing the slug cannot do, and it is the thing you are doing right now. A memory stored in a synapse decays, gets overwritten, dies with the animal. Long before the transistor, humans built a workaround: the written record. A mark on clay, on papyrus, on a page — a memory held outside any nervous system, immune to the CREB-2 gate because it never had to negotiate with it. And once the marks accumulated past the point where any one mind could hold them, we built the second tool, the quiet one: the index, the catalog, the table of contents. A way to find the memory again. The slug's whole problem is consolidation and retrieval inside one fragile head. We solved retrieval by moving the memory out of the head entirely and inventing the address that points back to it. Pavlov's saliva dripped into a graduated glass and was written into a ledger; the ledger outlived the dog, and Pavlov, and the century. The record is the slug's trick run on a different substrate — and it does not forget when you learn something new.

## Sources

- Botton-Amiot, G., Martínez, P., & Sprecher, S. G. (2023). Associative learning in the cnidarian *Nematostella vectensis*. *PNAS*, 120(13), e2220685120.
- Kandel, E. R. — Nobel Prize in Physiology or Medicine, 2000; *Aplysia* gill-withdrawal program.
- Bartsch, D., et al. (1995). *Aplysia* CREB2 represses long-term facilitation. *Cell*, 83, 979–992.
- Hebb, D. O. (1949). *The Organization of Behavior*.
- Bliss, T. V. P., & Lømo, T. (1973). Long-lasting potentiation of synaptic transmission in the dentate area. *Journal of Physiology*, 232, 331–356.
- Morris, R. G. M., Anderson, E., Lynch, G., & Baudry, M. (1986). Selective impairment of learning and blockade of LTP by an NMDA antagonist, AP5. *Nature*, 319, 774–776.
- Kamin, L. J. (1968). Predictability, surprise, attention, and conditioning.
- Rescorla, R. A., & Wagner, A. R. (1972). A theory of Pavlovian conditioning.
- Sutton, R. S. (1988). Learning to predict by the methods of temporal differences. *Machine Learning*, 3, 9–44.
- Schultz, W., Dayan, P., & Montague, P. R. (1997). A neural substrate of prediction and reward. *Science*, 275, 1593–1599.
- Kirkpatrick, J., et al. (2017). Overcoming catastrophic forgetting in neural networks. *PNAS*, 114, 3521–3526.
- Shomrat, T., & Levin, M. (2013). An automated training paradigm reveals long-term memory in planarians and its persistence through head regeneration. *Journal of Experimental Biology*, 216, 3799–3810.
- Pavlov, I. P. — Nobel Prize in Physiology or Medicine, 1904 (physiology of digestion).
