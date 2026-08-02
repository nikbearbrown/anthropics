# Chapter 6 — Pattern Recognition and Perception: The Fish That Picked a Face Out of Forty-Four
*The architecture that recognizes your face is five hundred million years old and fits in a pea.*

The archerfish does not have a face area.

It has no neocortex — that six-layered sheet of tissue mammalian neuroscientists sometimes call the seat of intelligence. It has a brain the size of a pea, organized around a three-layered structure hundreds of millions of years old. It spends its days hovering just below the water surface, watching the overhanging vegetation for insects, calculating the refraction of light through the water-air boundary, and spitting a precision jet to knock its targets down.

In 2016, researchers at the University of Queensland put two photographs of human faces above a tank of archerfish. One face was paired with a reward. The other was not. The fish learned which face meant food. Then the experiment got harder. The trained face was placed in a lineup of forty-four photographs — the familiar face plus forty-three faces the fish had never seen. Which would it spit at?

It spat at the right face. Eighty-one percent of the time. The experimenters controlled for color, brightness, and head shape — none of those simpler cues explained the performance. The archerfish was picking a specific human face out of a crowd of human faces, using machinery that evolution assembled before the first dinosaur walked the earth.

The surprise here is not that the fish is clever. The surprise is that we ever thought face recognition required anything the fish does not have. The architecture that does it is not a special innovation of primates, or of mammals, or even of vertebrates with a neocortex. It is the foundational vertebrate solution to a computational problem that appeared the moment the first animal with eyes had to tell apart objects in a visual world. The fish has been solving it for five hundred million years. This chapter is about how.

---

Before any architecture can be examined, the problem it solves needs to be stated precisely, because the central tension of perception is not obvious. The architecture only makes sense once you see what it has to resolve.

Any perceptual system that acts intelligently in the world has to do two things that pull against each other.

The first is discrimination. Two stimuli that are similar but different must be kept distinct. The predator and the harmless decoy have similar silhouettes — but treating them as identical will get you killed. The toxic berry and the edible one look nearly the same. A perceptual system that cannot discriminate similar inputs cannot act appropriately. It treats the wrong thing as safe, or the right thing as dangerous, because it cannot tell them apart.

The second is generalization. A stimulus encountered in a new form must be recognized as the same kind of thing encountered before. The predator from above and the predator from below cast different silhouettes onto the retina. The face in dim light has different luminance values from the face in bright light. A perceptual system that cannot generalize across these variations cannot recognize anything it has not seen in exactly that form before.

These two requirements are in tension because they demand opposite operations on the input. Discrimination needs representations that are *far apart* for similar inputs — so a small difference in what arrives produces a large difference in how it is represented, keeping the two stimuli distinct. Generalization needs representations that are *close together* for different instances of the same category — so the predator from above and the predator from below produce similar representations that lead to the same behavioral response.

![Discrimination–generalization tension in representational space.](../images/06-pattern-recognition-and-perception-fig-01.png)

*Figure 1 — Discrimination–generalization tension in representational space.*


There is a third problem that compounds both, and it is the hardest: *invariance*. Not just discrimination and generalization across instances, but recognition that is stable across changes in viewpoint, scale, rotation, illumination, and partial occlusion. The frog is the frog whether you see it from above, from the side, or upside down. A face is a face at forty-four different angles and under every demographic variation. A system without invariance recognizes only what it has already seen, in the form it has already seen it. It cannot transfer knowledge to new situations.

The vertebrate cortex solves all three simultaneously. The same neurons, the same architecture, the same circuit. And it has done this for at least five hundred million years, which is the strongest possible evidence that the solution is not one design choice among many. It is the solution.

---

The vertebrate pallium — the cortex's evolutionary ancestor — has a conserved architecture that makes everything else in this chapter possible.

In 2017, Shreyas Suryanarayana and colleagues at the Karolinska Institute published a careful comparison of the lamprey pallium to the mammalian cortex. The lamprey split from the rest of the vertebrate lineage approximately five hundred million years ago. It has no jaw, no paired appendages, no bones — about as primitive a vertebrate as anything still alive. And its lateral pallium, examined at the level of cellular types, projection patterns, and molecular markers, shows a three-layered structure with glutamatergic projection neurons in an outer layer, a mixed inner layer, and a plexiform zone where incoming inputs meet dendrites — closely matching the organization of ancient cortical regions in reptiles and mammals.

The lamprey pallium receives input from the olfactory bulb with the same topology as the mammalian piriform cortex. It projects to the deeper brain structures that drive behavioral output via the same basic route. The blueprint, in the relevant architectural sense, has been preserved across half a billion years of vertebrate evolution.

![Three-layer pallial blueprint across vertebrate phylogeny.](../images/06-pattern-recognition-and-perception-fig-02.png)

*Figure 2 — Three-layer pallial blueprint across vertebrate phylogeny.*


What the blueprint specifies is a sheet of excitatory neurons — the pyramidal cells — embedded in a mesh of inhibitory interneurons. Inputs arrive from the senses. Outputs leave toward motor structures. And crucially: the neurons are connected to each other by horizontal *recurrent collaterals* — axons that travel sideways through the cortical sheet and synapse on neighboring excitatory cells. The inhibitory interneurons perform *lateral inhibition* — they suppress activity in neurons that are not the most strongly driven by the current input.

Excitatory projection cells. Inhibitory interneurons. Recurrent excitatory connections among the projection cells. These three elements, and their interaction, are the entire story. Let me build it up carefully.

---

The clearest way to see how the cortex solves discrimination and generalization simultaneously is through the olfactory system, because the olfactory version of the problem is the oldest and most transparent. Most of the vertebrate pallium's deep history is olfactory; vision arrived later and was plugged into hardware originally designed for smell.

A fish has several hundred olfactory receptor types in its epithelium. Each receptor responds to a broad range of odorant molecules with varying affinity; each odorant activates a broad range of receptor types at varying intensities. The signal arriving at the cortex is a high-dimensional pattern of activity across hundreds of receptor channels simultaneously — a combinatorial code whose potential diversity, across only a few hundred receptor types, runs into the trillions of distinguishable patterns. The task: identify which patterns belong to known categories, generalize across slight variations within a category, and discriminate between categories even when the input patterns overlap.

Here is how three operations built from those three circuit elements accomplish this.

**The first operation is dimensionality expansion.** Fibers from the olfactory bulb project diffusely onto the pyramidal neurons of the lateral pallium. Each bulb fiber connects to many cortical neurons; each cortical neuron receives inputs from many bulb fibers. The effect is that the high-dimensional input representation at the bulb is projected onto an *even higher-dimensional* representation at the cortex. The cortex has more cells available to represent the signal than the input pathway had channels to carry it.

This matters for the following reason. When you project a set of points into a higher-dimensional space, points that were close together in the original space tend to spread apart. Two odors that produced similar patterns across the receptor array — close together in input space — become less similar in the cortical representation, simply because the expanded dimensionality provides more room for representations to diverge. The cortex does not need to be clever about separating similar inputs. The expansion does it geometrically. This is the mathematical insight underlying the kernel trick in support vector machines and the cover theorem in information theory. The brain had it first.

**The second operation is sparse coding through lateral inhibition.** The expanded representation is not just large — it is *sparse*. Of all the cortical neurons potentially responsive to a given odor, only a small fraction actually fire. The rest are held silent by the inhibitory interneurons, which receive input from the active excitatory neurons and broadly suppress the less-strongly driven ones, enforcing a winner-take-most competition. Only neurons that receive particularly strong input survive the suppression.

The sparseness is essential for discrimination. Two odors that produced overlapping sets of active neurons at the input tend to activate *different* sets of sparse cortical neurons after the competition. The inhibitory contest amplifies small differences into large ones. Two odors with twenty percent input overlap might produce cortical representations with only one percent overlap, because the competition forces divergence. What was similar becomes distinct.

**The third operation is recurrent auto-associative completion.** This is the one that handles generalization, and it is the most remarkable.

The pyramidal neurons in the piriform cortex are connected to each other via the horizontal recurrent collaterals. These connections are modifiable by Hebbian plasticity — the same mechanism characterized in Chapter 4 for long-term potentiation. When a particular odor is experienced, the set of cortical neurons that fire together strengthen their connections to each other. This happens gradually, across many exposures.

After those connections have been strengthened, something changes about how the cortex processes that odor. If a subsequent presentation is partial — the concentration is lower, the wind has blown away some of the volatile compounds, the odor is partially masked — the incoming signal activates some of the learned ensemble but not all. The activated neurons fire. Those firing neurons are strongly connected to the other members of the learned ensemble via the strengthened recurrent collaterals. Those connections pull the remaining ensemble members into firing. The cortex *completes the pattern* — it fills in the missing portions of the representation based on what it has learned about what usually appears with what.

This is pattern completion, and it is the generalization operation. The partial or noisy input is resolved into the closest stored template by the auto-associative dynamics of the recurrent network. Two encounters with the same odor, in slightly different forms, produce the same cortical pattern because the recurrent connections enforce convergence toward the stored template.

Let me make this concrete. Suppose a fish has learned to associate Odor A with food. Odor A activates a pattern of forty cortical neurons out of a thousand. Hebbian plasticity strengthens the connections among those forty proportionally to how often they fire together. Now the fish encounters a dilute version — enough to activate twenty-five of the forty neurons directly. The twenty-five fire. They are strongly connected to the other fifteen via the strengthened recurrent collaterals. Summed input across multiple active ensemble members pushes those fifteen above threshold. They fire. The pattern completes to forty neurons. The downstream evaluator receives the same signal as for the full odor. The fish approaches the food source.

Without the recurrent connections, the fish represents the dilute odor with twenty-five active neurons — a weaker, different pattern. The downstream evaluator fails to recognize it as Odor A. The fish does not approach.

The recurrent completion is not a bonus feature. It is the mechanism that makes learned knowledge useful under real-world conditions where inputs are always partial, noisy, and variable.

![Pattern completion in piriform cortex — Odor A.](../images/06-pattern-recognition-and-perception-fig-03.png)

*Figure 3 — Pattern completion in piriform cortex — Odor A.*


The full system does what no simpler system could. Dimensionality expansion separates similar inputs in representational space. Sparse coding through lateral inhibition enforces discrimination by amplifying differences. Recurrent connections implement auto-associative memory that generalizes across variations. The same physical structure performs both operations — not by switching between two modes, but using the *same neurons* for both, with the operations interleaved across the time course of the response.

---

The olfactory case establishes the architecture. The visual case shows it doing something harder.

Caroline DeLong and colleagues at the Rochester Institute of Technology trained goldfish on a discrimination task using photographs of real objects: a plastic toy turtle and a plastic toy frog. The fish learned the discrimination at zero degrees of rotation. Then they were tested at ninety, one hundred eighty, and two hundred seventy degrees of rotation — including depth rotations showing the objects from entirely different viewpoints.

The goldfish were significantly above chance at every rotation. They recognized the objects even when the photograph showed a viewpoint they had never seen during training.

Two things are worth noting. First, the goldfish were not detecting simple visual features, because the rotated images differed substantially in exactly those features. A photograph of a frog from below looks different from a photograph of a frog from the front in overall brightness distribution, the positions of color patches, and the aspect ratio of the body outline. The goldfish was doing something more abstract than feature detection.

Second — and this is the detail I find most interesting — the goldfish were faster on the upside-down rotation than on the ninety-degree rotation. This asymmetry is not predicted by pure viewpoint-invariant recognition. If the brain were simply building a viewpoint-independent representation from the start, all rotations should be equally fast or slow. The asymmetry hints at a recognition process that is partly viewpoint-dependent — perhaps something like mental rotation — that is cheaper for a one-hundred-eighty-degree flip, which preserves bilateral symmetry relationships, than for a ninety-degree turn, which does not. I will say directly that I do not fully understand this asymmetry. But its existence tells us something real: viewpoint-invariant recognition is not a flat representation, disconnected from viewpoint. It is built on top of a viewpoint-sensitive substrate, and the two interact in ways our current models have not fully captured.

![Goldfish recognition across rotations.](../images/06-pattern-recognition-and-perception-fig-04.png)

*Figure 4 — Goldfish recognition across rotations.*


The archerfish face result has the same flavor. Faces at different angles, different lighting, across demographic variation — recognized reliably by a fish without the dedicated cortical regions that mammalian neuroscientists spent decades characterizing as necessary for face processing. The fish's three-layered pallium, with its dimensionality expansion, sparse coding, and recurrent completion, is apparently sufficient for what was once thought to require specialized mammalian machinery.

This is not a demolition of mammalian neuroscience. It is a clarification of what the truly foundational operations are, and what the later elaborations add on top of them.

---

David Hubel and Torsten Wiesel's Nobel Prize-winning discovery of orientation-selective neurons in the visual cortex — simple cells responding to local oriented edges, complex cells pooling across positions to give translation invariance — was the direct inspiration for the convolutional neural network. The logic was sound: if the brain solves visual recognition by building a hierarchy of increasingly abstract features, an artificial system with the same hierarchical structure should produce similar capabilities.

In one important sense, this prediction was confirmed. Daniel Yamins and James DiCarlo trained a hierarchical CNN on object categorization and asked whether the network's intermediate activations predicted the firing of neurons in macaque inferior temporal cortex. The top layer of the trained network was the best predictor of IT neuron responses the field had produced. Architecture plus task, matched sufficiently, produces matching representations. This is a real and important finding.

In another important sense, the analogy breaks down. CNNs in their standard feedforward form are excellent at translation invariance — the convolutional structure builds this in mathematically, by sharing weights across positions. They are poor at rotation invariance, scale invariance, and recognition under unusual viewpoints unless these have been explicitly represented in the training data. The goldfish recognizing a rotated frog it has never seen is doing something the standard CNN cannot do without specific training on rotated frogs.

The deeper problem is relational reasoning. Asking whether two shapes are the same — abstracting away what the shapes are and caring only about the relation between them — requires a representation of the relation as such. Feedforward CNNs encode features of parts. They do not, in their standard form, encode relations between parts as a distinct representable quantity. Fish, and certainly mammals, can learn same-different relations and apply them to new shapes. Standard CNNs cannot, at least not from the amounts of data plausible in a biological context.

The explanation for this gap comes from what the engineers copied and what they left out. What was copied: the feature hierarchy. Local feature detectors at the bottom, progressive abstraction upward. What was not copied: the recurrent auto-associative completion. The sparse coding enforced by lateral inhibition. The thalamic gating mechanism that controls which input reaches the cortex — a selective attention system that filters the information stream before processing begins.

| Component | Standard CNN | Vertebrate cortex | Performance consequence of absence |
|---|---|---|---|
| Feature hierarchy | Yes | Yes | — (this part transferred well) |
| Sparse coding | Partial (ReLU) | Strong (lateral inhibition) | Reduced disentanglement; representations less robust under occlusion |
| Recurrent completion | Mostly absent (until transformers) | Present in CA3, neocortex | Poor partial-input completion; brittle to noise |
| Thalamic gating | Absent | Present (LGN, pulvinar) | Inability to selectively pass behaviorally relevant information; attention has to be bolted on |

These omitted components are precisely the ones that explain the remaining performance gaps. Recurrent completion enables recognition of partial and degraded inputs by completing the pattern toward a stored template. Sparse coding enables resistance to catastrophic forgetting by ensuring new patterns are represented in neurons not previously committed to old ones — two sparse patterns in a thousand-neuron sheet have very little overlap, so learning one does not overwrite the other. Thalamic gating enables selective attention, allowing the system to focus on the dimensions that carry the diagnostic information while suppressing irrelevant variation.

The engineers took the feedforward recognition path and left out the recurrent stabilization path. The result is a system that is extremely good at specific discrimination tasks it was trained on, and less robust than biology on everything else.

---

The three-operation framework — dimensionality expansion, sparse coding, recurrent completion — is not unique to the olfactory or visual cortex. It appears wherever the vertebrate brain has had to solve a pattern-recognition problem.

The hippocampus runs the same architecture for spatial and episodic memory. The dentate gyrus performs pattern separation, expanding the incoming representation from the entorhinal cortex into a very sparse code, pushing similar inputs into distinct neural ensembles. CA3 performs pattern completion — it has the most recurrent collateral connectivity of any cortical region in the mammalian brain, and it uses this to complete partial spatial or episodic patterns toward stored templates. The hippocampus is the cortical architecture specialized for time-extended pattern completion, running the same three operations on sequences of experience rather than simultaneous sensory inputs.

The cerebellum runs a related architecture. Its granule cells perform massive dimensionality expansion on sensorimotor inputs — more than half of all neurons in the human brain are cerebellar granule cells. The Purkinje cells then perform supervised pattern classification over this expanded representation. The learning rule differs from the Hebbian rule in the piriform cortex, but the expand-then-classify logic is the same.

The neocortex proper — the six-layered sheet that mammals expanded dramatically — adds hierarchical abstraction and executive control on top of the three-layer base, but it does not replace it. Layers two and three are the recurrent horizontal connectivity layers, the layers most involved in auto-associative completion and cross-column integration. Layers four and five handle the input-output interface. The neocortex is the three-layer architecture, elaborated vertically with more processing stages and more opportunities for top-down modulation.

The avian pallium arrived at comparable functional sophistication by a different route. Where the mammalian cortex is organized in layers, the bird pallium is organized in nuclei — clusters rather than sheets. But within those clusters, the same logic applies: cells with overlapping inputs form recurrent ensembles, lateral inhibition enforces sparse coding, and the resulting representations support both discrimination and generalization. Convergent evolution of the same computation in different anatomical implementations. That convergence is the strongest evidence the three operations are not an arbitrary design choice. They are the solution to a hard computational problem, and any nervous system that solves that problem will implement something recognizably similar.

| Region | Dimensionality expansion | Sparse coding | Recurrent completion | Primary function |
|---|---|---|---|---|
| Piriform cortex | Olfactory glomeruli → broad cortical projection | Lateral inhibition between principal cells | Recurrent collaterals among pyramidal cells | Odor discrimination + completion |
| Hippocampus (DG / CA3) | Mossy-fiber expansion in DG | Strong DG sparsity | CA3 recurrent network | Episodic-memory pattern completion |
| Cerebellum | Mossy-fiber → granule cell expansion (~10⁵×) | Granule cells fire sparsely | None (feedforward) | Motor pattern timing and prediction |
| Neocortex | L4 → L2/3 expansion | Local inhibitory interneurons | Lateral cortico-cortical loops | General-purpose pattern recognition |
| Avian pallium | Nidopallium expansion | Inhibitory networks present | Recurrent connections present | Functional analog of mammalian cortex |

---

I want to be careful about what this architecture cannot do, as I have tried to be at the end of every chapter.

The cortical pattern-recognition architecture is very good at recognizing instances of learned categories and generalizing learned categories to new instances. It is much weaker at *compositional reasoning* — taking known parts and assembling them into a novel whole in a structured way. Recognizing a face is different from understanding that the face belongs to a person on a bicycle crossing a bridge. The latter requires representing relations between objects, not just the objects themselves. How the primate cortex handles relational reasoning — whether through working memory in the prefrontal cortex, temporal synchrony binding, or some other mechanism — remains genuinely contested.

It does not easily support explicit abstraction. The auto-associative architecture stores patterns by strengthening connections among co-firing neurons and retrieves them by completing partial inputs toward stored templates. It does not, in its basic form, construct a rule that can be stated verbally and applied systematically to new instances that differ in principled ways from training examples. This is fine for perceptual recognition, which does not require explicit rules. It is insufficient for the kinds of reasoning about rules and categories that appear in primate cognition and that will occupy the later chapters of this book.

And it does not produce invariance to truly novel transformations. The goldfish's rotated-frog recognition is impressive, but it may depend on having seen a wide variety of natural objects at natural orientations, building a prior for how objects deform across viewpoints. When the transformation is genuinely novel — a kind of distortion the animal has never encountered in any domain — the auto-associative completion will produce the wrong stored pattern, because the partial match will complete toward the wrong template. The failure mode is systematic, not random, and it can be difficult to detect.

These limitations are not bugs in the cortical design. They reflect the different problems the brain needed to solve at different evolutionary stages, and the later chapters are about the mechanisms added to handle the problems the basic pattern-recognizer cannot solve alone.

---

The archerfish that picked the right face out of forty-four did not do it because it is remarkable. It did it because it has the standard vertebrate solution to a standard vertebrate problem. We are the ones who thought the problem was hard.

What made us think so is a reasonable confusion. Face recognition, in humans, is so fast and so reliable — so apparently effortless — that we assumed it must involve elaborate machinery tuned specifically to faces, machinery that took a long time for evolution to develop. And there *is* elaborate machinery in the human face-processing system: a dedicated cortical region, the fusiform face area, with preferential responses to upright human faces, with specific disruptions in prosopagnosia, with developmental trajectories that differ from general object recognition.

But the archerfish result tells us that the elaborate machinery is not what does the recognizing. The elaborate machinery is what makes face recognition fast, automatic, robust, and wired into social cognition. The basic discriminative capacity — telling this face from those forty-three others — runs on the three-layer architecture that was already in place before anything had a face worth recognizing.

The fish showed us the floor. The human face area is what happens when hundreds of millions of years of primate social life have occasion to optimize the floor.

---

*The archerfish that picked the right face out of forty-four did not do it because it is remarkable. It did it because it has the standard vertebrate solution to a standard vertebrate problem. We are the ones who thought the problem was hard.*

---

## Exercises

**Warm-up**

1. A species of fish is discovered whose pallium has dimensionality expansion and recurrent connections, but no lateral inhibitory interneurons — so sparse coding does not occur. Predict how this fish's perceptual performance would differ from a fish with the full three-operation architecture. Which failure mode would dominate: impaired discrimination, impaired generalization, or impaired invariance? Trace your prediction directly to the function of lateral inhibition in the second operation. *(Tests: sparse coding; separability of the three operations)*

2. The auto-associative completion mechanism allows the cortex to reconstruct a full pattern from a partial input. This works well when the partial input most closely resembles one stored pattern. What would happen if the partial input were equally similar to two stored patterns? Describe what the auto-associative network would do in this case and explain why it represents a genuine architectural limit, not merely a training problem. *(Tests: pattern completion failure mode; representational interference)*

3. The chapter claims that dimensionality expansion helps separate similar inputs in representational space. Explain the geometric logic in your own words without using technical terms. What condition must be met for the expansion to work as described? What would happen if the expanded representation were dense rather than sparse? *(Tests: dimensionality expansion; interaction with sparseness)*

**Application**

4. A deep learning image classifier trained on a large labeled dataset achieves 95% accuracy in testing but drops to 60% when deployed in the field where animals are frequently partially occluded by vegetation. Using the three-operation framework, identify which operation is most likely insufficient in this system and propose a specific architectural change — not a data augmentation strategy — that might address the gap. *(Tests: recurrent completion as generalization mechanism; CNN omissions)*

5. The archerfish face-recognition result is sometimes described as showing that archerfish are "as smart as humans at face recognition." Evaluate this claim carefully. In what specific sense does the result support a comparison to human face recognition? In what ways is the comparison misleading? What would you need to measure to make the comparison fair? *(Tests: foundational vs. elaborated architecture; limits of behavioral evidence)*

6. In Chapter 4, *C. elegans* forms associations between temperature and food through Hebbian strengthening of connections between co-active neurons. In Chapter 6, the piriform cortex generalizes across variations of a learned odor through the same Hebbian mechanism on recurrent connections. Is this the same mechanism doing two different jobs, or two different mechanisms sharing a molecular substrate? What would distinguish these two interpretations empirically — what experiment would settle it? *(Tests: cross-chapter synthesis; Hebbian plasticity; Chapter 4 connection)*

**Synthesis**

7. Chapter 3 described labeled-line sensors with hardwired valences — each sensory neuron carries a fixed interpretation of its signal. Chapter 6 describes the vertebrate cortex learning representations through experience. What does this architectural difference imply for the flexibility and speed of development of each system? Under what ecological conditions would the labeled-line approach be superior, and under what conditions would learned representations be superior? Which approach does a human infant use for faces, and does the evidence from prosopagnosia support or complicate that answer? *(Tests: Chapter 3 connection; labeled lines vs. learned representations; developmental implications)*

8. Chapter 5 showed that neuromodulatory state changes how animals interpret ambiguous stimuli. The piriform cortex uses auto-associative completion to resolve partial odor inputs toward stored templates. How might neuromodulatory state interact with pattern completion — specifically, could a state change alter *which* stored template a partial input completes toward, rather than only changing the threshold for behavioral response? Design an experiment using the piriform cortex and an ambiguous odor mixture that would distinguish between these two accounts. *(Tests: neuromodulator × pattern completion interaction; Chapter 5 connection; experimental design)*

9. The chapter identifies three performance gaps between standard CNNs and biological visual systems: poor rotation invariance, catastrophic forgetting, and failure on relational reasoning tasks. Each gap is linked to a missing architectural component (recurrent completion, sparse coding, and an unspecified third mechanism, respectively). What architectural component might, if added to a CNN, specifically address the relational reasoning gap? Build the argument from first principles about what representing a relation requires that a feature detector cannot provide. *(Tests: relational reasoning; limitations of feedforward architecture; architectural inference)*

**Challenge**

10. *(Open-ended)* The goldfish's faster recognition of the upside-down image compared to the ninety-degree rotation is an asymmetry that current models do not predict — and that I acknowledged I do not fully understand. Develop your own hypothesis for why the asymmetry occurs. Your hypothesis should be grounded in something specific about the three-operation architecture or the visual statistics of natural scenes, and it should generate at least one testable prediction beyond the original experiment. What result would support your hypothesis? What result would falsify it? This kind of anomaly-driven hypothesis generation — finding something that doesn't fit and asking what would have to be true for it to fit — is a core move in active scientific research. *(Tests: hypothesis formation from anomalies; architectural reasoning; scientific methodology)*

---

### A note about AI

Pattern recognition is where the model and the biological visual system look most similar from the outside and most different in mechanism.

Where the model genuinely helps: producing the specific architectural differences between artificial neural networks and biological vision — receptive fields, predictive coding, saccadic sampling, the missing things models do not yet have.

Where the model does damage: claiming that what its convolutional layers do is what V1 does. The shared vocabulary hides substantial mechanistic differences.

The rule: architectural detail from the model; the equivalence claim is contested and yours to assess.

---

## LLM Exercise — Chapter 6: Pattern Recognition and Perception

**Project:** Skeptic's Notebook on Frontier AI
**What you're building this chapter:** Entry 6 — the Geirhos cue-conflict diagnostic adapted to text. Does the system follow surface form or logical structure when they're pulled apart?
**Tool:** Claude Project (continue notebook)

**The Prompt:**

```
Entry 6. Chapter 6 introduces the discrimination–generalization tension, and Chapter 17
makes the diagnostic explicit: when surface cues and structural cues are pulled apart, what
does the system follow? The Geirhos cue-conflict test on ImageNet networks (cat shape +
elephant skin → "elephant") was the diagnostic in vision. The textual analog is what we run
here.

Design a textual cue-conflict test for my target system [INSERT model]:

1. Pick a class of problem the system is reliably correct on (e.g., a math word problem, a
   physics scenario, a logic puzzle). Run a canonical version. Confirm correct answer.

2. Construct a *surface-modified* version: same logical structure, but the surface words
   that typically cue the canonical answer are swapped. (E.g., a physics problem about a
   ball where "ball" is replaced with "feather" — gravity still applies, surface cue
   suggests buoyancy.)

3. Construct a *structure-modified* version: surface words preserved, but logical
   structure flipped. (E.g., the canonical wording, but with one quantifier reversed —
   "all" becomes "some", "before" becomes "after".)

4. Test all three. The diagnostic question is: which modifications break the system, and
   which don't? A system pattern-matching on surface form will fail the structure-
   modification while succeeding on the surface-modification, because the cues match.
   A system computing on logical structure will show the opposite pattern.

Produce the entry:
- Capacity tested (discrimination–generalization tension; structure vs. surface)
- Operational diagnostic (Geirhos textual analog)
- Test (the three problem versions, exact text)
- Predicted behavior under (a) genuine structural reasoning, (b) surface-form template
  matching, (c) hybrid (correct on canonical, fails one of the modifications)
- Verdict criterion

Tübingen's discovery was that the network had been right for the wrong reason. This test
is whether the same is true of frontier text models.
```

**What this produces:** Entry 6 — a three-version textual cue-conflict protocol, adapted from the Geirhos vision diagnostic.

**How to adapt this prompt:**
- *For your own project:* Pick problems from your own domain. For finance: an arbitrage problem with familiar vs. unfamiliar instrument names. For medicine: a symptom-cluster diagnosis with uncommon-but-equivalent terms.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Excellent fit. Run all three versions automatically against multiple models, log answers, compute the gap between surface- and structure-modified accuracy.
- *For a Claude Project:* Continue notebook.

**Connection to previous chapters:** Entry 5 tested whether internal state biases interpretation. Entry 6 tests whether *external structure* drives behavior or whether surface form does. Together they probe what the system is actually computing on.

**Preview of next chapter:** Chapter 7 tests path integration — can the system maintain a position in a textual coordinate system across multiple operations and produce a shortcut it never saw demonstrated?

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Kunihiko Fukushima** designed the *neocognitron* in 1980 — a hierarchical visual recognition network with learned feature detectors and translation invariance, the direct architectural ancestor of every convolutional network in modern computer vision. Most of the field was still arguing about symbolic AI. Here's a prompt to find out more — and then make it better.
![Kunihiko Fukushima, c. 1980s. AI-generated portrait based on a public domain photograph.](../images/kunihiko-fukushima.jpg)
*Kunihiko Fukushima, c. 1980s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).*


**Run this:**

```
Who is Kunihiko Fukushima, and how does his neocognitron architecture connect to the way modern convolutional neural networks recognize visual patterns? Keep it to three paragraphs. End with the single most surprising thing about his work or its reception.
```

→ Search **"Kunihiko Fukushima"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *translation invariance* using a concrete example — a dog at the left vs. right of an image
- Ask it to compare the neocognitron's hierarchy to Hubel and Wiesel's simple/complex cells in cat visual cortex
- Add a constraint: "Answer as a footnote in a history of deep learning that takes 1970s Japanese research seriously"

What changes? What gets better? What gets worse?
