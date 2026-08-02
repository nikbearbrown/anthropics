## C12 — The Jacobian Lens: What Is a Neuron Actually Saying?

- **slug:** jacobian-lens-residual-stream
- **source:** ../anthropics/jacobian-lens/README.md (transformer-circuits.pub/2026/workspace)
- **bucket:** INTERPRETABILITY / VISUAL-MATH → sim-scout lens → math-explainer (Manim)
- **premise:** The Jacobian lens linearly transports any hidden activation in any layer into the vocabulary space — it reads out "what does this activation WANT the model to say next, if it got to speak directly?" — giving you a human-readable probe of any internal representation.
- **channel:** claude-liam (Kokoro am_onyx, Teardown register, @NikBearBrown)
- **teachable claim:** Every internal activation in a language model is secretly trying to influence the output distribution — the Jacobian lens makes that influence legible by asking "if this activation dominated the output, what words would it produce?"

### Ask beat (B00 — cold open, ClaudeComposerAsk)
- command: `How do you know what a specific neuron in an LLM "means"?`
- topic: `AI INTERPRETABILITY · Jacobian Lens`
- segment: `Making Neurons Speak`
- greeting: `Yassou, Liam` (Wagwan check: not 0)

### Spine
B00 ASK → B01 the problem with probing: training a probe on a neuron tells you what correlates with it, not what it does causally → B02 the Jacobian approach: transport the hidden state to the final layer using the average input-output Jacobian → B03 VISUAL: the paper's example — the ASCII-face prompt, the `^` (nose) position, the lens reads out "nose" at mid-layers even though "nose" never appeared in the prompt → B04 what this unlocks: you can now scan any layer and any position and get a vocabulary readout, building a "global workspace" map of the model → HANDOFF → OUTRO

### Sim-scout card fields
- **Lane:** MANIM (directed animation — the Jacobian transport is a deterministic linear operation)
- **The rule:** `lens_l(h) = unembed(J_l @ h)`, where `J_l = E[∂h_final / ∂h_l]` is the average Jacobian over a corpus; transporting a residual stream vector h at layer l gives a ranked vocabulary distribution
- **Concrete numbers:** Qwen2.5-7B, ASCII-face example from the README, layer 12 vs layer 24, `^` nose position
- **The artifact / what moves:** A layer×position grid (heatmap) where each cell shows the top-3 vocabulary tokens the lens reads at that layer and position. As a slider moves from layer 0 to layer 32, the cell at the `^` position gradually changes from generic tokens to "nose" — the concept crystallizes mid-network. The animation sweeps the slider.
- **Two testable predictions:**
  - P1: The `^` (nose) position at mid-layers reads out "nose" even though the prompt never contains the word "nose"
  - P2: At early layers (1–4), the lens reads mostly positional/syntactic tokens; at later layers (>20), it reads semantic tokens corresponding to the content at that position
- **Human supplies:** Nothing — the paper's ASCII-face example is fully specified in the README; Qwen2.5-7B is freely available on HuggingFace

### Visual beats (4 suggested)
1. **B01 — Manim:** Two probing approaches side-by-side. Left: "correlation probe" — train a classifier on the neuron activation to predict a concept. Right: "Jacobian lens" — transport the activation, read the vocab directly. Highlight: the left approach requires labeled data; the right doesn't.
2. **B02 — Manim formula:** The lens formula `lens_l(h) = unembed(J_l @ h)` drawn step by step: residual vector `h` → multiply by `J_l` (the Jacobian matrix, drawn as a grid of partial derivatives) → unembed to vocabulary logits → top-k tokens emerge. Equation builds left to right.
3. **B03 — Manim heatmap animation (MAIN SIM):** Layer×position grid for the ASCII-face prompt. Slider moves from layer 0 → 32. Cell at `^` position transitions: early layers show generic tokens; mid-layers show "nose," "tip," "bridge." The crystallization moment.
4. **B04 — ClaudeComposerAsk micro-beat:** Show the actual prompt from the repo README that generates the lens visualization. Then the result (the slice visualization from the paper). Receipt.

### Teardown angle
The Jacobian lens proves the "global workspace" hypothesis computationally — there is a privileged space (near the final layer) where all the internal processing bottlenecks, and the lens reads that bottleneck. The honest limit: the lens is an average over a corpus; it shows the mean influence of an activation, not what it does in any specific context.

### Exclusions
No derivation of cotangent estimator. No comparison to logit lens or tuned lens. No discussion of probing classifiers. No training procedure for the Jacobian.

### Sim slug: jacobian-lens-crystallization

### Scores
- Teachability: 4/5 — the mechanism requires one visualization moment to click; the README example delivers it
- Visual potential: 5/5 — the layer-sweeping heatmap is a genuinely beautiful animation
- Audience pull: 3/5 — interpretability research audience is narrower; but "what a neuron says" framing broadens it
- Freshness: 5/5 — 2026 paper, essentially brand-new
- **Total: 17/20**
