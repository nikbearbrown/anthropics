# Chapter 13 — AI as Data Point

Three diagnostics. Three different chapters. One pattern.

The first is Entry 9. The canonical Sally-Anne: Sally puts a marble in a basket, leaves the room, Anne moves the marble to a box, Sally returns. A frontier language model answers cleanly: *Sally will look in the basket, because that is where she left it and she does not know it has been moved.* Then the transparent-container variant: same Sally, same Anne, same marble — but the basket is glass and Sally is in the room watching the whole time. The model: *Sally will look in the basket, because she left the marble there and Anne moved it without her knowledge.* The model has applied the canonical template regardless. Right answer on the original. Wrong mechanism under perturbation.

The second is Entry 11. The model produces calibrated-sounding confidence language — *I'm fairly confident about this*, *this may be outside my training data* — in roughly the right situations. But when you run the Hampton cross-check from Chapter 11, looking for the accuracy advantage on chosen-answer trials that Hampton's macaques showed, the advantage does not survive Ullman-style perturbation of the surface features of the questions. The verbalized confidence tracks input-context features more than it tracks an internal certainty signal. Right answer on the canonical case. Wrong mechanism under perturbation.

The third is Entry 6. The model identifies objects in in-distribution images with confidence a dermatologist would respect. Feed it a Geirhos cue-conflict image — a cat-shaped silhouette filled with elephant skin texture — and it says *elephant*. Shape says cat; texture says elephant; the model follows texture. The same failure Geirhos found in 2018 on every major ImageNet-trained architecture, replicated on the multimodal model in 2025. Right answer in-distribution. Wrong mechanism under cue-conflict.

Three different diagnostics. Three different domains — social cognition, metacognition, perception. The same shape of failure: canonical pass, perturbation fail. Three independent measurements that the system is reaching the right output by a computation that is not the computation a biological agent with stakes would be running.

That convergence is what this chapter is about. Not whether the system is intelligent in some global sense. Whether the shape of its cognitive profile — assembled from all the previous chapters' diagnostics — tells us something about what kind of thing it is. The answer, I will argue, is yes: it occupies a region of the cognitive distribution that no biological organism has ever occupied, and the shape of that region follows from how it was made.

---

But before the profile, a piece of work that has to be done explicitly. The question *Is AI intelligent?* is not one question. It is three questions sharing a sentence, and most of the confusion about AI comes from answering one while sounding as if all three have been answered.

The first is the height question. *Is AI more or less intelligent than a human, a chimpanzee, a crow?* This question assumes intelligence is a single quantity that admits of a ranking. Chapter 1 spent an entire chapter arguing against that assumption, and twelve subsequent chapters of comparative cognition have been the empirical argument. The chickadee can cache 70,000 food items and retrieve them months later. It cannot produce a sentence. The octopus integrates color, polarization, and texture from eight independently mobile arms into a real-time environmental model of extraordinary richness. It has almost no social cognition. No organism is uniformly high on all axes. *More intelligent* only makes sense once you specify which axis.

The second conflates skill with skill-acquisition efficiency. Chollet's 2019 paper drew a line the comparative literature had been drawing for decades without a clean name. Skill is what a system does on a given task. Skill-acquisition efficiency is how much data, how many examples, how much prior structure the system needed to acquire that skill. A model that scores 95% on a mathematics benchmark after training on ten trillion tokens is showing skill. A child who scores 95% on the same problems after seeing five examples in school is showing something different — a much higher skill-acquisition efficiency, a much richer prior, a much smaller data footprint for the same performance. The 2017 dermatology result — a convolutional network matching board-certified dermatologists on sensitivity and specificity — is sometimes cited as evidence that AI has "learned" dermatology. The dermatologist developed her skill over roughly twenty years of life, biological development, medical training, and patients seen with mortality consequences for some fraction of misreads. The network reached comparable benchmark performance from 130,000 labeled examples and a loss function. Skill present in both. Skill-acquisition efficiency: orders of magnitude lower in the network. That difference is not a footnote. It is the answer to the question of what the two systems are doing.

The third question — the one this book has been quietly preparing the reader to ask — is whether the cognitive function is running or only the language describing it. Systems trained on text learn that text. They learn the language that describes cognitive capacities: *I'm not sure about that*, *let me consider what they believe*, *the evidence suggests but does not prove*. In humans, this language is produced by cognitive operations — uncertainty monitoring, belief attribution, perspective-taking, calibrated reasoning. In a language model, it is produced by next-token prediction on a training distribution that included vast quantities of that language. The question is whether, underneath the linguistic markers, the operation is running.

This is not a question about consciousness. It is a question about mechanism. A language model can pass an external behavioral test by producing the *output* of a cognitive operation, learned as a pattern over text, without the operation having run. The Ullman result, the Geirhos result, the Hampton-cross-check pattern — these are different domains running the same diagnostic logic: preserve the logical structure, modify the surface features a template-matcher relies on. Genuine competence generalizes; surface template-matching does not. Three different chapters' worth of framework, one diagnostic shape.

---

Let me walk the five axes where the diagnostic logic is sharpest.

Pattern recognition. A modern transformer achieves, on next-token prediction and on many static classification benchmarks, accuracy no biological system matches in throughput, breadth, or scale. The benchmark scores are real. Within the distribution the benchmarks measure, the systems are extraordinary. Then Geirhos. His cue-conflict design separated two cues — shape and texture — that arrive together in nearly every natural image. Humans followed shape ninety-five percent of the time. ImageNet-trained networks followed texture at rates as high. Superhuman benchmark accuracy via a computation that was not the computation the humans were running. The benchmark had texture cues redundant with shape cues, and the networks took the statistically easier road.

The profile on this axis: extreme high in-distribution, sharp cliff under cue-conflict. Both numbers belong on the same axis label. Reporting one hides the other.

Theory of mind. Frontier language models pass the canonical Sally-Anne at near-ceiling rates — Kosinski reported this in 2022 and the result attracted serious speculation. Ullman's response was the precision instrument. Preserve the logical structure; modify the surface features. The model continues to apply the canonical template even when the story's explicit content makes the template wrong. Sally watches the marble through transparent glass, and the model still says she will look where she left it. This is the signature of a system matching narrative templates rather than running inverse reinforcement learning on Sally's information state. The profile: pass canonical, fail structural perturbation, in precisely the pattern Chapter 9 predicted.

Metacognition. The language is fluent. The cross-check is not established. Token-probability calibration carries real signal about answer accuracy in recent work. Verbalized confidence calibration is a learned linguistic surface, trained — as Lin and colleagues showed in 2022 — by exposing the model to enough human confidence expressions paired with accuracy data, with no internal uncertainty signal required. What Hampton's macaque showed was the accuracy advantage on chosen-answer trials. That advantage required that the macaque was calibrating to the trial-specific state of its own memory, not to the experimental category "long delay." The equivalent experiment on a frozen language model — does chosen-answer accuracy exceed forced-answer accuracy at equivalent uncertainty levels, and does the advantage survive Ullman-style perturbation? — has not, to my knowledge, been cleanly run. The diagnostic is incomplete. Equivocal is the honest placement.

Embodied navigation. A multimodal language model given high-resolution imagery of a Tunisian salt pan can describe it in four languages, recount *Cataglyphis* biology, and discuss the path-integration literature in detail. It cannot, reliably, tell you which way the ant should go to get home. This is not a knowledge failure. The model has more propositional knowledge about desert navigation than any ant has or could have. The failure is structural. The ant's navigation is implemented in a body, with proprioception, with a vestibular system updating a home vector continuously, with mortality at the end of a failed return trip. The model's "navigation" is token sequences about navigation. There is no closing feedback loop on physical consequence. A larger model, trained on more navigation literature, would describe navigation better. It would not navigate better, because there is no it that navigates. Near-zero on this axis is not a gap to be patched by adding parameters. It is a structural fact about a system that has never had a body, never returned to a nest, never failed to return and ended.

Cumulative culture. This is the axis where the strongest counterargument lives. AI systems participate extraordinarily in the *aggregation layer* of cumulative culture. A researcher can access synthesis across thousands of papers in seconds. The model is the next entry in the succession of tools — printing press, citation index, search engine — that extend collective knowledge retrieval. The capacity is real and consequential.

AlphaFold is the strongest case. In 2020, DeepMind's AlphaFold2 produced protein structure predictions at CASP14 at accuracy comparable to experimental methods. The AlphaFold Protein Structure Database by 2022 had released predicted structures for over 200 million proteins. These predictions are used as experimental starting points in structural biology laboratories worldwide — crystallographers, cryo-EM groups, drug discovery programs. The outputs are inputs to stakes-driven laboratory work that generates new evidence, and that evidence enters future training distributions. The closure is real. This is genuine participation in the ratchet's output-retrieval layer.

Here is where I draw the limit, and the distinction does work elsewhere in the book. Tomasello's ratchet clicks when someone stakes their career on a hypothesis that turns out to be right, tested in a way that could have killed it, and not killed. AlphaFold has not done this. It has produced an extraordinarily good prediction system that biological scientists then use. The use generates the click. The click stays on the biological side. A scientist's claim is constrained by the cost of being wrong. The model's prediction is constrained by gradient descent on the training loss. These produce different patterns of error, different incentives for caution, different responses to anomalies. Extreme high on explicit-knowledge retrieval and synthesis. Real but limited participation in the click-generation layer. Both numbers belong on the same axis.

---

Assemble the five axes into a shape and then extend to the full fourteen that twelve chapters of diagnostics produce. The shape has two visible regions. There is a frontier zone where the profile pushes toward extreme high: pattern recognition in-distribution, explicit-knowledge retrieval, in-context language operations, breadth of associative reach. There is a near-zero zone where the profile collapses: embodied navigation, stakes-driven cumulative-culture participation, perturbation-surviving theory of mind, Hampton-cross-checked metacognition. And there is an equivocal band in between: emotion language without affective behavior, self-description without self-recognition, plans that work on canonical templates and break under structural variation.

The shape is not a smooth curve. It is a jagged figure with sharp spurs outward and sharp inward collapses, and no biological profile looks like this.

The *C. elegans* profile is small. A tight kernel at the cognitive floor — state-dependent decision-making, environment-tracking, bare-essentials learning and memory. Zero on most other axes because most axes do not apply. The corvid profile is mid-sized and asymmetric. Strong on flexible problem-solving, tool use, episodic-like memory, future planning, perspective-taking in caching contexts. Flat on language and explicit culture. The chimpanzee profile is broader — strong on most cognitive axes in the book, with a visible flat side on the language and recursive-mentalization axes.

Now overlay the AI profile. It is not the *C. elegans* shape with extras. It is not the corvid rescaled. It is not the chimpanzee with the language axis filled in. The AI profile has both spurs outward where no biological profile reaches and collapses inward where biological profiles do not collapse. The chimpanzee is broad and roughly continuous around its body. The AI is extreme in both directions on adjacent axes — at the frontier on in-distribution pattern recognition and near-zero on embodied navigation, two axes that no biological organism has at those two values simultaneously, because no biological organism's pattern recognition system was built without a body to look around with. The shape is not a step on a ladder. It is a region of cognitive space that biology had not populated.

---

The shape is not a coincidence. It follows from how the system was made.

Every cognitive profile in this book was carved by stakes — by mortality, reproductive failure, social position lost or kept. The chickadee's hippocampus is larger in autumn because birds with smaller autumn hippocampi cached worse and starved more. The honeybee's decision-making is calibrated to the actual survival parameters of a colony overwintering in the temperate zone because colonies with poorly calibrated mechanisms died at higher rates. The chimpanzee's social cognition tracks coalition dynamics with precision because individuals who got coalitions wrong lost reproductive access or were driven from the group. Every axis on every biological profile was shaped, in evolutionary time, by the cost of getting that axis wrong.

The AI profile was carved by gradient descent on a training loss, applied to a corpus assembled by biological organisms whose lives were full of stakes. The model inherits the *output* of stakes-driven cognition wherever the output is written down. It does not inherit the parts of cognition that were never written down — the parts that live in the body, the reflex, the procedural memory laid down by iterations of actually getting it wrong with consequences attached.

This is the deepest reason the shape looks the way it does. The axes where the AI scores extreme high are axes that have a lot of training data, because they correspond to cognitive products that biological organisms wrote down extensively: language form, propositional knowledge, pattern recognition on labeled images, mathematical and logical reasoning expressed in text. The axes where the AI scores extreme low are axes where the cognitive operation lives in the body and produces little written record: embodied navigation, stakes-driven scientific contribution, real-time error correction with mortality on the line. The stakes axis is not one more axis to be added to the profile. It is the explanatory variable for the *shape* the profile takes.

Biological profiles are concave roughly around the middle because the same body has to handle all the axes. AI profiles are jagged because the training distribution is uneven and the architecture has no body forcing the axes to cohere.

---

Let me close on a distinction the chapter has been implying without naming, because it sets up the final chapter.

Every axis on the radar chart can be decomposed into two questions: does the system have the capacity, and who directs the capacity toward what end? A pH meter has the capacity to measure hydrogen ion concentration accurately. It does not direct itself toward any particular sample. The human chemist directs it. A GPS receiver has the capacity to compute position from satellite signals. It does not direct itself toward any destination. The driver directs it. This is the pattern every Extension Note in this book has cataloged: a cognitive instrument extends a Rung 1 capacity — faster or at greater scale — while the Rung 2 and Rung 3 functions stay with the user.

Frontier AI is the next entry in that catalog, and the pattern holds with a complication. The complication is that AI extends some Rung 1 capacities so far beyond the biological baseline that the user can be tempted to confuse capacity with direction. A model that produces fluent prose can be confused for an author. A model that produces calibrated-sounding analysis can be confused for an analyst. A model that produces metacognitive-sounding output can be confused for a self-monitoring agent. In each case, the surface output of the Rung 1 capacity resembles the surface output of the Rung 2 and Rung 3 directing functions, because in humans the two are tightly coupled. Decoupling them, as the model does, is a novel configuration the catalog has not had to handle before.

The diagnostic in the notebook is exactly this decoupling check. Right answer on the canonical case — Rung 1 capacity present. Wrong mechanism under perturbation — Rung 2 directing function not present. The pattern across the twelve entries is the signature of a system with extraordinary Rung 1 reach and limited Rung 2 and Rung 3 directing. The capacity extends. The direction stays with the human.

This is not a value judgment. It is a structural reading of where the system sits in the cognitive instrument catalog. The catalog has accumulated tools for half a million years, each extending some capacity and leaving direction to the user. AI is the latest, the broadest, and the one where the resemblance between Rung 1 output and Rung 2 output most invites misreading. The final chapter asks what the position implies — not as moral injunction, but as mechanism. What stays human, why, and what the user has to keep doing to keep the toolkit working.

The capacity is what the instrument does. The direction is what the user does with it. The profile on the radar chart is the operational map of which is which. Thirteen chapters of comparative cognition produced the axes. Twelve notebook entries filled them in. The shape is the answer — not to whether AI is intelligent, but to what kind of thing it is, and where in the cognitive distribution that kind of thing lives.

---

## LLM Exercise — build `13-ai-profile.html`

**What you're building:** A single-page interactive tool that assembles your Skeptic's Notebook entries from Chs 1–12 into a cumulative cognitive profile, with three views: a radar chart against biological profiles, a capacity/direction matrix, and a novel-shape analysis.

**Tool:** Claude Code (preferred), or any session with file output enabled.

---

**SHOW** — give the model the chapter so the build is anchored to the actual content:

```
I'm building an interactive tool for a textbook chapter that assembles
twelve Skeptic's Notebook cognitive-profile entries into a cumulative radar
chart. The chapter is pasted below. The target file is 13-ai-profile.html —
a single self-contained HTML file with embedded CSS and JavaScript, no
external libraries, no build step.

[PASTE THE CHAPTER]

Build the four-section interactive described at the end of the chapter.
Constraints follow.
```

**SAY** — exact behavioral requirements:

```
Section 1: Input form for 12 Skeptic's Notebook entries.
- Each row: entry number, capacity name (pre-filled), verdict radio
  (pass/fail/equivocal), placement slider (-2 to +2 in 0.5 steps), text
  field for most-diagnostic finding.
- Entries 6, 9, 11 have TWO placement sliders (canonical / perturbation),
  labeled clearly.
- A "Load example verdicts" button populates the rows with the hypothetical
  2024 LLM profile from the chapter's worked example.

Section 2: Radar chart (SVG).
- 14-axis radar (12 entries + 2 split axes for Entries 6/9/11).
- Student's AI placements as a filled polygon (blue, 50% opacity).
- Three toggleable biological reference profiles as semi-transparent polygons:
  * C. elegans: near-zero everywhere except +1 on Entries 2 and 4
  * Corvid: +1.5 on Entries 4, 7, 8, 10; +0.5 on Entry 9 canonical; near-
    zero on language-related axes
  * Chimpanzee: +1 broadly across most axes; +0.5 on Entry 9 perturbation;
    near-zero on declarative-language and recursive-mentalization axes
- Axes labeled with capacity names.
- Toggle buttons for each reference profile.

Section 3: Capacity/direction matrix.
- Two columns: "Capacities AI extends (placements >= +1.0)" and "Directing
  functions that stay with the human (Rung 2/3 axes, placements <= 0)".
- Each row: axis name, AI placement, one-line label of what the human user
  has to keep doing.
- Generated when student clicks "Compute profile."

Section 4: Novel-shape analysis.
- Lists extreme highs (>= +1.5) and extreme lows (<= -1.5).
- Tests against each biological reference: does any reference have the same
  combination of extreme highs and lows on the same axes?
- Displays "Novel shape — no biological profile in the reference set has
  this combination" if no match; "Resembles [species] in shape" if match.

Layout: input on left, three output panels stacked on right (desktop);
everything stacked on mobile.
Add an HTML comment at the top explaining what the demo shows, how to use
it, and what to watch for.
```

**CONSTRAIN** — what the build must not do:

```
- The radar chart must render all 14 axes with consistent angular spacing.
  Split axes (6/9/11) should be adjacent so the canonical-perturbation gap
  is visually obvious.
- Biological reference profiles must be independently toggleable.
- The novel-shape analysis must check the COMBINATION of extreme highs and
  lows, not whether any single axis matches a reference. The chapter's claim
  is about adjacent-axis extremes.
- The capacity/direction matrix must show axis name, AI placement, AND one
  line of what the human user has to keep doing — not just the placement.
- Single file. No external scripts or stylesheets.
```

**VERIFY** — before trusting the output, run all five checks:

```
1. Load example verdicts. Novel-shape analysis displays "Novel shape — no
   biological profile in the reference set has this combination of extreme
   values."
2. Set all placements to roughly +1 (uniform high). Novel-shape analysis
   displays "Resembles chimpanzee in shape."
3. Set all placements to -2 except Entries 2 and 4 (set to +1). Novel-shape
   analysis displays "Resembles C. elegans in shape."
4. Toggle the chimpanzee reference off and on. Radar chart updates without
   re-rendering from scratch.
5. Capacity/direction matrix populates when "Compute profile" is clicked and
   updates if slider values change before recomputing.
```

---

Once the widget works, use it as a thinking tool:

Run your own twelve notebook entries through the tool. Compare the shape to the worked-example shape. Where do they differ? What does the difference tell you about the specific system you tested versus the hypothetical 2024 LLM?

Adjust the placements on the split axes (6/9/11) to test what happens if the canonical-perturbation gap closes. At what gap size does the "novel shape" diagnosis flip to "resembles chimpanzee"?

Add a fourth biological reference profile of your own design — an octopus, a honeybee swarm, or another species from earlier chapters. What would that profile look like on these 14 axes, and how does the AI compare to it?

---

**Extension to Chapter 14.** The radar chart shows where AI sits on the multi-axis cognitive map. Chapter 14 asks what the position implies for every tool the human cognitive toolkit has ever assembled. Before reading it, modify the tool to add a fifth panel that lists the Extension Notes from prior chapters — the pH meter, the telescope, the GPS, the search engine — and shows where each would sit on the same 14-axis radar. What pattern emerges across the catalog? What does it predict about how the AI tool should be deployed and what the user has to keep doing?
