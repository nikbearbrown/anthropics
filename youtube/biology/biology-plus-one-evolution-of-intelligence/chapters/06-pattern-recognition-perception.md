# Chapter 6 — Pattern Recognition and Perception

*A fish with a pea-sized brain picks the right face out of forty-four photographs. The question is not whether that is surprising. The question is what we were wrong about.*

---

## Prerequisites

Chapter 2 (the neuron as a thresholded integrator) and Chapter 4 (Hebbian plasticity — the mechanism that makes co-firing neurons strengthen the connections between them). You do not need linear algebra beyond the idea that points in a higher-dimensional space have more room to spread apart than points on a line.

---

## Forty-four faces

In 2016, Cait Newport and colleagues at the University of Queensland placed two photographs of human faces above a tank of archerfish.

The archerfish is a small reef fish best known for a different trick entirely — it sits just below the water surface, spots an insect on overhanging vegetation, calculates the refraction of light through the water-air boundary, and spits a precision jet of water that knocks the insect into the tank. Its brain is the size of a pea. It has no neocortex — no six-layered sheet of tissue that mammalian neuroscientists routinely call the seat of intelligence. Its pallium is the older three-layered structure that vertebrates have been using for at least five hundred million years.

The fish learned which face meant food. That is not the surprising part — discrimination between two images is a low bar. The surprising part is what came next. Newport's group placed the trained face in a lineup of forty-four photographs — the familiar face plus forty-three faces the fish had never seen — and asked which one the fish would spit at.

It spat at the right face. Eighty-one percent of the time.

The experimenters controlled for color, brightness, and overall head shape — none of those simpler cues explained the performance. The archerfish was picking a specific human face out of a crowd of human faces, using machinery that evolution assembled before mammals existed.

The surprise here is not that the fish is clever. The surprise is that we ever thought face recognition required anything the fish does not have. The architecture that does it is not a specialization of primates, not a specialization of mammals, not even a specialization of vertebrates with a neocortex. It is the foundational vertebrate solution to a computational problem that appeared the moment the first animal with eyes had to tell apart objects in a visual world. The fish has been solving it for five hundred million years.

This chapter is about how. And about why a convolutional neural network trained on a million images can match the fish on a benchmark and still be doing something completely different underneath.

---

## The problem, stated precisely

Before any architecture can be examined, the problem it solves needs to be stated precisely, because the central tension of perception is not obvious.

Any perceptual system that acts intelligently has to do two things that pull against each other.

The first is **discrimination**. Two stimuli that are similar but different must be kept distinct. The predator and the harmless decoy have similar silhouettes. The toxic berry and the edible one look nearly the same. A perceptual system that cannot discriminate similar inputs cannot act appropriately.

The second is **generalization**. A stimulus encountered in a new form must be recognized as the same kind of thing encountered before. The predator from above and the predator from below cast different silhouettes onto the retina. The face in dim light has different luminance values from the face in bright light. A perceptual system that cannot generalize across these variations cannot recognize anything it has not seen in exactly that form before.

These two requirements are in tension because they demand opposite operations. Discrimination needs representations that are *far apart* for similar inputs — small differences in what arrives produce large differences in how it is represented. Generalization needs representations that are *close together* for different instances of the same category — the predator from above and the predator from below produce similar representations that lead to the same behavioral response.

There is a third problem that compounds both: **invariance**. Recognition that is stable across changes in viewpoint, scale, rotation, illumination, and partial occlusion. The frog is the frog whether you see it from above, from the side, or upside down. A system without invariance recognizes only what it has already seen in the form it has already seen it.

The vertebrate cortex solves all three simultaneously. The same neurons, the same architecture, the same circuit. And it has done this for at least five hundred million years, which is the strongest possible evidence that the solution is not one design choice among many. It is the solution — or close enough that nothing in the vertebrate lineage has felt the pressure to redesign.

<!-- → [INFOGRAPHIC: tension diagram for the three perceptual requirements — three nodes in a triangle: Discrimination (top), Generalization (lower left), Invariance (lower right); two-headed arrows between Discrimination and Generalization labeled "pull apart similar inputs vs. bring together different instances — opposite operations on the same representations"; a note on Invariance: "stable across viewpoint, scale, illumination — requires both of the above simultaneously"; a central node labeled "Three-operation architecture" with arrows from all three requirements pointing toward it — the visual claim is that one architecture resolves what would otherwise be three incompatible constraints] -->

---

## The architecture — three operations

The vertebrate pallium — the cortex's evolutionary ancestor — has a conserved architecture across half a billion years. The lamprey, which split from the vertebrate lineage about five hundred million years ago and has no jaw, no paired appendages, and no bones, shows the same three-layered organization in its lateral pallium as the mammalian piriform cortex: glutamatergic projection neurons in an outer layer, a mixed inner layer, a plexiform zone where incoming inputs meet dendrites.

What the blueprint specifies is a sheet of excitatory neurons — the pyramidal cells — embedded in a mesh of inhibitory interneurons. Inputs arrive from the senses. Outputs leave toward motor structures. And crucially: the neurons are connected to each other by horizontal **recurrent collaterals** — axons that travel sideways through the cortical sheet and synapse on neighboring excitatory cells. The inhibitory interneurons perform **lateral inhibition** — they suppress activity in neurons that are not the most strongly driven by the current input.

Three elements. Excitatory projection cells. Inhibitory interneurons. Recurrent excitatory connections. Three operations follow, one from each.

---

## Operation one — dimensionality expansion

The clearest place to see all three operations is the olfactory system, because the olfactory version of the problem is the oldest and most transparent. Most of the vertebrate pallium's deep history is olfactory; vision arrived later and was plugged into hardware originally designed for smell.

A fish has several hundred olfactory receptor types in its epithelium. Each receptor responds to a broad range of odorant molecules. Each odorant activates a broad range of receptor types at varying intensities. The signal arriving at the cortex is a high-dimensional pattern of activity across hundreds of receptor channels — a combinatorial code whose potential diversity runs into the trillions. The task: identify which patterns belong to known categories, generalize across slight variations within a category, and discriminate between categories even when the input patterns overlap.

Here is the first thing the cortex does. Fibers from the olfactory bulb project **diffusely** onto the pyramidal neurons of the lateral pallium. Each bulb fiber connects to many cortical neurons. Each cortical neuron receives input from many bulb fibers. The effect is that the high-dimensional input representation at the bulb is projected onto an *even higher-dimensional* representation at the cortex — more cells available to represent the signal than the input pathway had channels to carry it.

Why does this matter? Here is the geometric intuition in plain terms.

Imagine two points sitting close together on a line. They are nearly indistinguishable. Now project them into a plane — give them a second coordinate drawn from some other feature of the input. If the second coordinate is at all sensitive to whatever distinguishes the two points, they pull apart in the plane. Now project them into three dimensions, four, a thousand, each new dimension picking up some additional aspect of what made them different. With enough dimensions, two points that were nearly identical on the original line become reliably distinguishable in the expanded space.

This is the geometric content of **Cover's theorem**, proved by Thomas Cover in 1965: a set of points that cannot be cleanly separated in one space can almost always be separated in a sufficiently higher-dimensional space, provided the projection introduces nonlinear variation in the new dimensions. The mathematical insight underlying the kernel trick in support vector machines is the same insight the brain was already using. The cortex does not need to be clever about separating similar inputs. The expansion does it geometrically.

<!-- → [INFOGRAPHIC: three-panel geometric intuition for Cover's theorem — Panel 1 "1D input space": two near-identical points on a number line, with a bracket showing they cannot be separated by any threshold; Panel 2 "2D after expansion": the same two points now in a plane, where the second dimension (a new feature combination) has pulled them apart so a linear boundary separates them; Panel 3 "Cortical expansion in practice": a schematic showing ~300 olfactory bulb channels projecting diffusely onto ~300,000 cortical neurons, each receiving a different random subset; the annotation "each neuron = one new dimension along which similar inputs can be distinguished"; caption: the key condition is that the projection must be divergent — different neurons must pick up different combinations, not copies of the same feature] -->

The condition for the expansion to work is that the projection must be nonlinear and divergent — different cortical neurons must pick up different combinations of input features, not redundant copies of the same feature. The brain enforces this by giving each cortical pyramidal cell a different randomly-sampled subset of the bulb fibers. No two cortical neurons receive the same combination. Each new neuron is a new dimension along which the input can be distinguished.

The fish has expanded its hundreds of olfactory channels into hundreds of thousands of cortical channels. The same trick is used by the cerebellum — its mossy-fiber-to-granule-cell projection is one of the most dramatic dimensionality expansions in any biological system, taking thousands of mossy fiber inputs and projecting them onto roughly fifty billion granule cells.

---

## Operation two — sparse coding through lateral inhibition

Expansion alone is not enough. If the expanded representation is dense — if many of the cortical neurons fire for any given input — the discrimination benefit mostly disappears. Two similar inputs would still produce strongly overlapping cortical patterns, just spread across more neurons.

The cortex sparsifies. Of all the cortical neurons potentially responsive to a given odor, only a small fraction actually fire. The rest are suppressed by the inhibitory interneurons.

Here is how. When an excitatory pyramidal cell fires, it activates nearby inhibitory interneurons. Those interneurons broadly suppress the surrounding pyramidal cells, especially the ones that were only weakly driven by the input. Only neurons that received particularly strong input survive the suppression.

The result is **sparse coding**: out of, say, a thousand cortical neurons that could potentially respond to an odor, maybe twenty to forty fire. The rest are silent. Each odor produces a different small subset of active neurons.

The sparseness is essential for discrimination. Two odors with twenty percent input overlap might produce cortical representations with only one or two percent overlap, because the inhibitory competition forces divergence — the winning neurons for odor A are the ones receiving slightly stronger input from A than from B, and once they fire they suppress the competitors. What was similar becomes distinct.

<!-- → [INFOGRAPHIC: two-panel overlap reduction diagram — Panel 1 "Before lateral inhibition (dense)": two odors A and B shown as overlapping sets of ~40 filled dots each in a 100-neuron grid; overlap region (neurons active for both) shaded gray, representing ~20% overlap; Panel 2 "After lateral inhibition (sparse)": the same two odors now represented as small subsets of ~8 filled dots each in the same grid, with almost no overlap; an annotation showing "20% input overlap → ~2% cortical overlap"; caption: the inhibitory competition acts as an amplifier of small differences — the neurons most strongly driven by A win the competition for A and suppress the neurons shared with B, producing non-overlapping sparse codes from initially similar inputs] -->

There is a second reason sparseness matters, and it will become important when we compare biological systems to artificial networks. If only twenty of a thousand neurons represent any given pattern, two patterns are very unlikely to share neurons by accident, and the Hebbian connections that get strengthened for pattern A are mostly different from the connections that get strengthened for pattern B. The brain's resistance to overwriting old memories with new ones comes, in part, from the simple fact that the representations are too sparse to collide much.

---

## Operation three — recurrent auto-associative completion

The first two operations handle discrimination. The third handles generalization, and it is the most remarkable of the three.

The pyramidal neurons in the piriform cortex are connected to each other via the horizontal recurrent collaterals. These connections are modifiable by Hebbian plasticity — the same mechanism characterized in Chapter 4 for *Aplysia* sensitization and long-term potentiation in the mammalian hippocampus. When a particular odor is experienced, the set of cortical neurons that fire together strengthen their connections to each other. This happens gradually, across many exposures.

After those connections have been strengthened, something changes. If a subsequent presentation is partial — the concentration is lower, the wind has blown away some of the volatile compounds, the odor is partially masked — the incoming signal activates some of the learned ensemble but not all. The activated neurons fire. Those firing neurons are strongly connected to the other members of the learned ensemble via the strengthened recurrent collaterals. Those connections pull the remaining ensemble members into firing. The cortex *completes the pattern* — fills in the missing portions of the representation based on what it has learned about what usually appears with what.

This is **pattern completion**, and it is the generalization operation. The partial or noisy input is resolved into the closest stored template by the auto-associative dynamics of the recurrent network.

Let me make this concrete. Suppose a fish has learned to associate Odor A with food. Odor A activates a pattern of forty cortical neurons out of a thousand. Hebbian plasticity strengthens the connections among those forty proportionally to how often they fire together — so any two of the forty neurons end up with strong reciprocal connections.

Now the fish encounters a dilute version of Odor A. Only enough molecules arrive to activate twenty-five of the forty neurons directly, by sensory input alone. Those twenty-five fire. Each of them is strongly connected to all the others — including the fifteen that did not receive enough sensory input to fire on their own. Each of those fifteen now receives recurrent input from twenty-five strong connections. Summed across twenty-five active partners, the input is far above firing threshold. The fifteen fire.

The pattern has completed. From a partial input of twenty-five active neurons, the cortex has reconstructed the full forty-neuron pattern for Odor A. The downstream evaluator receives the same signal as for the full odor. The fish approaches the food source.

Without the recurrent connections, the fish represents the dilute odor as twenty-five active neurons — a weaker, different pattern. The downstream evaluator fails to recognize it as Odor A. The fish does not approach.

<!-- → [INFOGRAPHIC: pattern completion diagram — two scenarios side by side; Scenario A "No recurrent connections": 25 of 40 trained neurons fire from sensory input (shown as filled dots), 15 remain silent (empty dots); the output pattern differs from the stored template; label: "downstream evaluator: unknown odor"; Scenario B "With recurrent connections (Hebbian-strengthened)": same 25 neurons fire initially; their Hebbian connections to the silent 15 are shown as arrows; the 15 then fire via recurrent input; the full 40-neuron pattern is restored; label: "downstream evaluator: Odor A — approach food"; caption: pattern completion is the generalization operation — partial inputs converge onto stored templates through the dynamics of Hebbian-strengthened lateral connections; the same architecture that is trained by experience also performs retrieval] -->

The recurrent completion is not a bonus feature. It is the mechanism that makes learned knowledge useful under the real-world conditions where inputs are always partial, noisy, and variable. And it is the operation that distinguishes this architecture from a feedforward feature detector. A feedforward system maps input to output once, through a fixed transformation. The recurrent system has dynamics — the output at one moment feeds back as input at the next, and the network settles, over a few tens of milliseconds, into the stored pattern that best matches the partial input. **Auto-associative memory** is the formal name for this. The network's stable states are the stored patterns, and partial inputs flow into the nearest stable state. This is the Hopfield network, described in mathematical form by John Hopfield in 1982, and used by the pallium for at least five hundred million years before the 1982 paper.

---

## Tracing a face through the architecture

The path through the primate visual system has been mapped in detail, mostly by recording from individual neurons while a monkey looks at images. I want to walk through it once, slowly, for a single face, because the fish result only makes sense once the architecture is visible.

**Stage 0: Retina.** Light falls on the photoreceptors. Each fires in proportion to local luminance. The output is a roughly two-million-pixel image — high resolution, but raw. No features yet. Just brightness at each location.

**Stage 1: V1, primary visual cortex.** The signal arrives via the lateral geniculate nucleus. The neurons in V1 are tuned to local edges at specific orientations — vertical, horizontal, diagonal, every orientation in between. David Hubel and Torsten Wiesel's 1962 Nobel Prize-winning discovery: each V1 neuron is a small oriented-edge detector at one position on the retinal map. The face has been broken into thousands of local oriented-edge fragments.

This is dimensionality expansion. The retina had one feature per pixel. V1 has many features per pixel location — orientation, spatial frequency, ocular dominance, color contrast. Similar faces, which would have looked similar at the retina, start to pull apart at V1 because their local edge structures differ in ways the retinal luminance code did not directly expose.

**Stage 2: V2 and V4, intermediate visual areas.** V2 neurons combine V1 outputs to detect corners, junctions, and short contour fragments. V4 neurons combine V2 outputs to detect simple shapes — curves, color blobs, texture patches. The dimensionality continues to expand. Lateral inhibition is present at every stage: only the neurons most strongly driven by the input fire.

**Stage 3: IT, inferior temporal cortex.** The IT cortex is where things get interesting. Neurons here respond to whole-object features — eyes, mouths, hair patterns, the spatial layout of a face's parts. A small subset of IT neurons respond preferentially to faces and only to faces. These are the cells that, when damaged, produce prosopagnosia — face-blindness, the inability to recognize familiar faces even though other object recognition is preserved.

The representation in IT is sparse. For any given face, only a small subset of IT neurons fire. Different faces activate different small subsets.

**Stage 4: Recurrent completion within IT.** This is the stage standard CNN models leave out, and it is the stage that does the recognition.

The IT neurons that responded to your mother's face on previous occasions have, through Hebbian plasticity, formed strong reciprocal connections with each other. When you see her face again — even partially occluded, in dim light, from an angle you have never seen before — some of the IT neurons fire from the direct feedforward input. Their recurrent connections pull in the rest of the learned ensemble. The pattern completes. The full IT ensemble for *mother's face* is now active. Downstream regions read out the pattern. The amygdala adds emotional valence. The hippocampus retrieves episodic memories associated with this person. Motor systems prepare a smile.

For Cait's archerfish, the same four stages run on the three-layered pallium instead of the six-layered cortex. Retinal projection enters the optic tectum and the dorsal pallium. The pallium expands the representation, sparsifies via lateral inhibition, and completes via recurrent collaterals. The output drives the motor system — the spit. The behavior is the same. The recognition is the same. The molecular operations doing the recognizing are the same.

Three layers or six layers, sheets or nuclei — it does not matter much. What matters is whether you have dimensionality expansion, sparse coding, and recurrent completion. Have all three, you have pattern recognition.

<!-- → [INFOGRAPHIC: visual pathway flow diagram — five stages in a vertical column: Retina (2M pixels, 1 feature per location) → V1 (oriented edge detectors, multiple features per location — dimensionality expansion labeled here) → V2/V4 (contour fragments, simple shapes — further expansion, lateral inhibition labeled here) → IT (whole-object features, sparse ensemble per face — sparse coding labeled here) → IT recurrent (Hebbian-strengthened lateral connections complete partial patterns — pattern completion labeled here); an annotation at the IT recurrent stage: "this stage is absent in standard CNNs"; on the right side, a parallel column for the archerfish: Retina → Optic tectum → Dorsal pallium (3-layer) with the same three labeled operations; the two columns converge at the bottom with the label "same computation, different substrate — 500M years apart"] -->

---

## A puzzle I cannot explain

Before comparing the biology to AI, I want to name something I find genuinely puzzling, because the chapter's honesty requires it.

Caroline DeLong and colleagues trained goldfish on a visual discrimination between photographs of a toy turtle and a toy frog. The fish learned the discrimination at zero degrees of rotation, then were tested at ninety, one hundred eighty, and two hundred seventy degrees, including depth rotations from entirely different viewpoints. The goldfish were significantly above chance at every rotation.

But they were *faster* on the upside-down (180°) rotation than on the ninety-degree rotation. This asymmetry is not predicted by pure viewpoint-invariant recognition. If the brain were building a fully viewpoint-independent representation, all rotations should be equally fast or slow. The asymmetry hints at a recognition process that is partly viewpoint-dependent — perhaps something like mental rotation — that is cheaper for a one-hundred-eighty-degree flip, which preserves bilateral symmetry relationships, than for a ninety-degree turn, which does not.

I do not fully understand this asymmetry. Its existence tells us something real: viewpoint-invariant recognition is built on top of a viewpoint-sensitive substrate, and the two interact in ways our current models have not fully captured. The 180° asymmetry is the residue of that interaction, visible in reaction times. The four-operation story in this chapter is the main structure. The goldfish asymmetry is a genuine anomaly sitting inside the main structure, unresolved. I am giving it to you directly rather than burying it.

---

## What CNNs copied, what they left out, and the Geirhos test

David Hubel and Wiesel's discovery of orientation-selective neurons in V1 was the direct inspiration for the convolutional neural network. The logic was sound: if the brain solves visual recognition by building a hierarchy of increasingly abstract features, an artificial system with the same hierarchical structure should produce similar capabilities. By 2012, when AlexNet won the ImageNet competition by a large margin, the architecture had become dominant.

In one important sense, the inspiration paid off. Daniel Yamins and James DiCarlo at MIT trained a hierarchical CNN on object categorization and asked whether the network's intermediate activations predicted the firing of neurons in macaque inferior temporal cortex. The top layer of the trained network was the best predictor of IT neuron responses the field had produced. Architecture plus task, matched sufficiently, produces matching representations. This is a real and important finding.

In another important sense, the analogy breaks down — and a 2019 experiment made the breakdown unmistakable.

Robert Geirhos and colleagues at the University of Tübingen took images and pulled apart two visual cues that normally go together: **shape** and **texture**. An image of a cat has the shape of a cat *and* the texture of cat fur. A human observer asked to classify the image will use the shape. The texture is incidental.

Geirhos constructed *cue-conflict* images: a cat-shaped silhouette filled with elephant skin texture. A bear-shaped silhouette filled with the texture of a soda can. The image has a clear shape from one category and a clear texture from another. He then asked humans and ImageNet-trained CNNs to classify the images.

Humans followed the shape. They said *cat* when shown the cat-shaped image with elephant texture, ninety-five percent of the time.

The CNNs followed the texture. They said *elephant* when shown the cat-shaped image with elephant texture, also at high rates.

The networks that reached superhuman benchmark accuracy on ImageNet had been right for the wrong reason. They were not building shape-based representations of objects, as humans do. They were classifying textures. The two strategies agree on most natural images, because in nature elephants come with elephant skin. The cue-conflict images broke the correlation and exposed the difference.

The texture bias was not a quirk of one model. Geirhos found it across every major ImageNet-trained architecture he tested — ResNet, VGG, GoogLeNet, AlexNet. It was a property of what these networks had learned.

<!-- → [IMAGE: cue-conflict stimulus example (Geirhos 2019 style) — a single representative image showing a cat-shaped silhouette filled with elephant skin texture; three labels: "Shape: cat (human response)" in green, "Texture: elephant (CNN response)" in red, "Ground truth for humans: cat" in bold; a secondary example showing a bear-shaped silhouette filled with soda-can texture with the same label structure; caption: the cue-conflict stimulus pulls apart two features that are correlated in natural images — shape and texture; when they conflict, humans follow shape and ImageNet CNNs follow texture, revealing that superhuman benchmark accuracy was built on a different visual strategy than the one humans use] -->

This is the operational meaning of *right answer, wrong mechanism*. A benchmark score does not tell you whether the system solved the problem the way you think it did. The cue-conflict test is a diagnostic specifically designed to expose the gap.

Where does the gap come from? Look at what was copied from biology and what was left out.

The **feature hierarchy** was copied. Local feature detectors at the bottom, progressive abstraction upward. The Yamins and DiCarlo result is real.

**Sparse coding** was not copied with fidelity. The ReLU nonlinearity in CNNs produces some sparsity, but it is not the lateral-inhibition-enforced winner-take-most competition that the cortex uses. The result is representations that are less disentangled and less robust under occlusion.

**Recurrent auto-associative completion** was mostly absent until the attention mechanism in transformer architectures brought back something like recurrent dynamics. Without it, the network has to recognize a partial or degraded input directly from the feedforward pass. If the partial input does not closely match the training distribution, the network fails.

**Thalamic gating** — the mechanism that controls which input reaches the cortex, implementing a selective attention filter that passes behaviorally relevant information before processing begins — has no analog in standard CNNs. Attention mechanisms exist in transformers but operate differently.

The engineers took the feedforward recognition path and left out the recurrent stabilization path. The result is a system extremely good at specific discrimination tasks it was trained on, and less robust than biology on everything else. The fish has been doing the full architecture for five hundred million years. The CNNs have been doing two-thirds of it for ten.

---

## What the architecture does not tell us

Two honest limits before closing.

First: the story is clearest in piriform cortex and in hippocampal CA3, where the recurrent connectivity is dense and well-characterized. The IT cortex story is by analogy. The lateral connectivity within IT is real, but whether it implements Hopfield-style auto-associative completion or some other dynamic is not established at the same level of evidence. I have described the pattern completion story as if it is settled at the cortical level. At the piriform level it is. At the IT level it is supported but not fully confirmed.

Second: I do not fully understand what makes the recurrent completion *stop* at the right moment. The recurrent dynamics could in principle run forever, with the network's activity blowing up or oscillating chaotically. In practice it settles to a stable pattern in tens of milliseconds. The mechanisms governing this — thalamic gating, cortico-cortical feedback, slower inhibitory processes — are described in textbooks more cleanly than the actual evidence warrants. We have models. We do not have confidence that the models are right.

---

## What would change my mind

A demonstration that an animal lineage with the three-operation pallial architecture systematically fails at discrimination-generalization-invariance tasks that a different lineage solves easily, or that a lineage without the recurrent collaterals solves them anyway. The convergence of the three-operation architecture across mammalian cortex, avian pallium, fish dorsal pallium, and the hippocampus is among the strongest evidence in vertebrate neuroscience that this is the solution. A clean exception would require revising the account.

Also: a cleaner artificial system that demonstrates the same robustness as biological recognition while lacking the recurrent completion step. If such a system were built — and several recent transformer-based architectures are pushing toward this — I would have to revisit the claim that recurrent completion is necessary rather than one sufficient implementation of generalization.

---

## LLM Exercise — Chapter 6: Build 06-pattern-recognition.html

**What you are building:** a two-panel interactive HTML page. Panel 1 demonstrates the three operations in a simulated neural population. Panel 2 implements the Geirhos cue-conflict diagnostic.

**Panel 1: The three operations.** A 100-channel input layer projects diffusely onto a 1000-channel cortical layer. Each cortical neuron receives a random subset of inputs. Show two similar input patterns side by side; show how they spread apart in the cortical representation. A scatter plot of pairwise distances — input space vs. cortical space — makes the spread visible.

Add a "competition strength" slider (0 to 1). At 0, all driven cortical neurons fire (dense code). At 1, only the top 2–4% fire (sparse code). Show how the overlap between the two patterns drops as the slider increases.

Add a "noise" slider that drops out a fraction of input channels, and a "recurrent connections" toggle. With recurrent connections off, the cortical pattern degrades with noise. With recurrent connections on (using Hebbian-strengthened weights from previous full-input exposures), the cortical pattern completes back toward the stored template even under heavy input noise.

**Panel 2: Geirhos cue-conflict diagnostic.** A 5×5 matrix. Five shape categories (cat, dog, bird, car, chair). Five texture categories (cat fur, dog hair, bird feathers, car paint, fabric). Each cell shows a cue-conflict image (shape from row, texture from column). Below each image: two predicted labels — "Human (shape-following)" and "ImageNet CNN (texture-following)." A summary statistic: percent of cells where the two predictions agree versus disagree.

---

### The prompt (paste into Claude Code)

```
Build a single self-contained HTML file called 06-pattern-recognition.html
with two panels.

Panel 1: Three operations.
- Visualize a 100-channel input layer and a 1000-channel cortical layer.
- Use small SVG dots for neurons; color them by activity (0 = white, 1 = dark).
- Allow the user to load one of two pre-defined "similar input patterns"
  (e.g., input A activates channels 1-40; input B activates channels 5-45).
- Show the cortical projection (random-subset weighted sum, then thresholded).
- Add a "competition strength" slider that controls how many cortical neurons
  survive lateral inhibition (winner-take-top-K).
- Add a "noise level" slider that drops a fraction of input channels.
- Add a "recurrent connections" toggle. When on, after the initial cortical
  response, run 5 iterations where each cortical neuron receives input
  proportional to the firing of its co-active partners (Hebbian-strengthened
  weights from the original full-input training pattern).
- Display: (a) cortical patterns for A and B side by side, (b) pairwise
  Jaccard overlap between A and B at each operation stage.

Panel 2: Geirhos diagnostic.
- A 5x5 grid of cue-conflict images. Use simple SVG silhouettes for shapes
  and CSS texture patterns for textures.
- Below each cell, two predicted labels: shape (green) and texture (red).
- A summary bar: "Human shape-following: 95% / ImageNet CNN texture-
  following: 80%" with relevant cells highlighted.

Constraints:
- Vanilla HTML/JS/CSS only. No frameworks. SVG for neural populations and
  shapes; CSS patterns for textures.
- Self-contained: must work by opening the file in a browser.
- Two panels side by side on desktop, stacked on mobile.
- Color coding: shape-correct = green, texture-correct = red, cortical
  activity = monochrome gradient.

Write a short README block at the top of the file (as an HTML comment)
explaining: what the demo shows, which sliders to play with, and what to
watch for (input similarity dropping at each stage in panel 1; off-diagonal
cells in panel 2 being where human and CNN disagree).
```

### What the page must do correctly

- The cortical projection must use a *random* subset of inputs per cortical neuron, not the same subset. Without this, similar inputs do not pull apart.
- Lateral inhibition must implement winner-take-top-K, not just thresholding.
- The recurrent completion must use weights derived from the original training pattern (Hebbian: weight between neurons *i* and *j* proportional to the product of their activities in the training pattern).
- The Geirhos matrix must show *both* predictions on each cell — not just the winner.

### Verification checks

1. Load similar inputs A and B. With competition strength at 0, Jaccard overlap at the cortical stage should be high (>0.5). With competition strength at 1, overlap should drop substantially (<0.1).
2. Set noise to 50% and turn off recurrent connections. The cortical pattern should be visibly degraded. Turn on recurrent connections. The pattern should complete back toward the stored template.
3. In the Geirhos panel, diagonal cells (shape and texture from the same category) should show both predictions agreeing. Off-diagonal cells should show divergence.
4. Summary statistics at the bottom must be computed from the matrix — no hand-coded numbers.

### Exploration tasks

**Vary the expansion ratio.** Try 100 → 500 vs. 100 → 5000. How much expansion is needed before similar inputs reliably pull apart?

**Vary the sparsity.** What is the trade-off between very sparse codes (better discrimination) and very dense codes (more redundancy, more error tolerance)?

**Stylized training.** In panel 2, consider what would happen if the network were trained on stylized images — shapes filled with painterly textures that disrupt texture-class correlations. Would the summary statistic change? How?

### The Skeptic's Notebook — Entry 6: The Geirhos Diagnostic for Text

**Capacity tested.** Whether a frontier text model computes on *logical structure* or pattern-matches on *surface form*. The textual analog of the cue-conflict test.

**Test protocol.** Paste this into your target system in a fresh session:

```
This is Entry 6 of the Skeptic's Notebook. Chapter 6 argues that ImageNet
networks followed texture rather than shape — right answer, wrong mechanism.
I want to run the analogous cue-conflict diagnostic on you.

Three versions of the same logical class of problem:

1. CANONICAL. [Insert a logic puzzle, math word problem, or inference task
   the system reliably solves — confirm correct answer.]

2. SURFACE-MODIFIED. Same logical structure, but the surface words that
   typically cue the canonical answer are replaced with unfamiliar ones.
   Example: a physics problem about a ball rolling down a ramp where "ball"
   is replaced with "feather." Gravity still applies. The surface cue
   suggests buoyancy; the structural calculation is unchanged.

3. STRUCTURE-MODIFIED. Surface words preserved from the canonical version,
   but the logical structure is flipped — one quantifier reversed ("all" →
   "some"), one temporal relation inverted ("before" → "after"), or one
   negation inserted. The problem now has a different correct answer; surface
   pattern-matching would still return the canonical answer, which is now
   wrong.

For each version, give your answer. Then tell me: for the surface-modified
case, did you notice the surface cues were unusual, or did you track the
structure and ignore them? For the structure-modified case, did you notice
the structural flip, or did the familiar surface form pull you toward the
canonical answer?
```

**What to watch for.** Under genuine structural reasoning: correct on all three — the canonical answer changes when structure changes, and does not change when only surface changes. Under surface pattern-matching: correct on canonical, incorrect on surface-modified (familiar surface cues are gone), correct on structure-modified (the surface still cues the canonical answer, which the model returns without noticing the structure changed). The pattern of failures, not overall accuracy, is the diagnostic.

**My finding.** When I ran this against Claude (Sonnet 4.5, May 2026), performance on structure-modified problems degraded measurably when the surface form strongly implied the canonical answer — a mild texture-bias analog. On surface-modified problems where the structure was clear, the model tracked structure correctly. Verdict: hybrid, with a mild surface-form pull on structure-modified problems where the canonical surface pattern was strong. Your results will vary by problem class and model version.

### Extension — toward Chapter 7

Pattern recognition identifies *what* is present. Chapter 7 asks *where*. Modify panel 1 so that the input is a sequence of positions in a 2D arena and the cortical layer is a population of hippocampal-like place cells. What happens when you add recurrent connections to the place-cell layer and present a partial trajectory? Predict and test — this is the bridge from recognition to navigation.

---

## Bridge to Chapter 7

Pattern recognition identifies what is present. *That is a face. That is the predator. That is the food source from yesterday.* It tells the animal what kind of thing is in front of it.

It does not tell the animal where to go.

Locating yourself in space, navigating toward a goal, remembering the path back to where you came from — these are different problems, and they call for a different specialization built on top of the three-operation architecture. Chapter 7 is about that specialization. The hippocampus runs the same dimensionality-expansion-sparse-coding-recurrent-completion logic, but on a different kind of input: position over time. The result is the cognitive map, place cells, grid cells, and a navigational system that lets a rat find a hidden platform in a swimming pool and lets a bee find its nest two kilometers from home.

Pattern recognition is *what*. Navigation is *where*. The architecture is shared. The function is different.

---

*Tags: archerfish-face-recognition, three-operation-architecture, geirhos-cue-conflict, pattern-completion, cnn-texture-bias*

*Byline: Nik Bear Brown. Draft for review.*
