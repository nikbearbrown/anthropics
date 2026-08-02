## C03 — How Neural Networks Store More Concepts Than They Have Neurons

- **slug:** toy-models-superposition-features
- **source:** ../anthropics/toy-models-of-superposition/README.md + paper title
- **bucket:** INTERPRETABILITY / VISUAL-MATH → sim-scout lens → math-explainer (Manim)
- **premise:** A neural network with N neurons can represent far more than N distinct concepts by overlapping them at angles — trading interference for capacity. This is the mechanism behind why larger models "know more" than their parameter count seems to allow.
- **channel:** claude-liam (Kokoro am_onyx, Teardown register)
- **teachable claim:** Neural networks do not use one neuron per concept — they pack many features into the same neurons simultaneously using near-orthogonal directions in high-dimensional space. This is called superposition, and it is why interpretability is hard.

### Ask beat (B00 — cold open, ClaudeComposerAsk)
- command: `How can a neural network know more things than it has neurons?`
- topic: `AI INTERPRETABILITY · Toy Models of Superposition`
- segment: `More Features Than Neurons`
- greeting: `Olá, Liam` (Wagwan check: not 0)

### Spine
B00 ASK → B01 the naive picture: one neuron = one feature (AND WHY THIS IS WRONG) → B02 superposition defined: packing features as nearly-orthogonal vectors → B03 MANIM: 2D toy model — show features crammed into a 2D space as angled arrows, interference shown explicitly → B04 why this makes interpretability hard (you can't just read off one feature per neuron) → HANDOFF → OUTRO

### Sim-scout card fields
- **Lane:** MANIM (directed animation — the geometry is fixed and deterministic)
- **The rule:** Features stored as nearly-orthogonal vectors in a lower-dimensional space; when a feature fires, its vector adds to the representation; other features decode it with small error proportional to the dot product
- **Concrete numbers:** 2D toy model with 5 features; feature importance weights [1, 0.9, 0.8, 0.5, 0.3]; sparsity ~0.01 (each feature fires rarely)
- **The artifact / what moves:** 5 colored arrows emerge from the origin in a 2D plane, each at ~72° intervals (Pentagon arrangement) — text labels appear and the simulation shows one feature "firing" while others show small residual activation (the interference). Arrows rotate and change length to show how the angles change with sparsity.
- **Two testable predictions:**
  - P1: With sparsity 0.01 and 5 features in 2D, the toy model learns the Pentagon arrangement (angles ~72° apart) rather than random placement
  - P2: Decreasing sparsity (features fire more often) forces the model to use fewer features total — it drops the lowest-importance ones first
- **Human supplies:** Nothing — fully synthetic (the toy model matches Anthropic's published notebook)

### Visual beats (4 suggested)
1. **B01 — Manim:** Two boxes side by side. Left: naive picture, 5 neurons, 5 labeled dots (one per concept). Right: reality, 2 neurons (axes), 5 arrows crammed in at angles. Label: "you have 2 dimensions / you want 5 features." Pause for contrast to register.
2. **B02 — Manim:** One arrow in 2D space grows. Its label: "banana" concept. A second arrow appears at a different angle. When "banana" fires, the "apple" direction picks up a small component — animate the projection with a dotted line. Label: "interference = the price."
3. **B03 — Manim (main sim):** Pentagon animation — all 5 arrows growing in from origin, spreading into optimal angles. One feature lights up (color pulse). The other 4 show small error bars. Then slow rotation to show that reducing sparsity (slider at bottom) causes the 2 lowest-importance features to collapse and disappear.
4. **B04 — Remotion concept card:** Why this matters for interpretability: split screen shows "what we hoped neurons mean" (one concept per neuron) vs "what actually happens" (each neuron is a mixture). Text: "You can't interpret a neuron — you have to interpret a direction."

### Teardown angle
The toy model is exactly the right tool here — it proves the mechanism in a case where you can verify it, then the reader extrapolates. The honest caveat: real models are much higher-dimensional (which helps — more near-orthogonal directions available) but the principle scales up.

### Exclusions
No derivation of the loss function. No discussion of phase transitions (interesting but a second video). No comparison to sparse autoencoders (different video). No history of polysemanticity term.

### Sim slug: toy-superposition-pentagon

### Scores
- Teachability: 5/5 — clean geometric mechanism, simulatable in 2D
- Visual potential: 5/5 — Pentagon animation is iconic, immediately graspable
- Audience pull: 4/5 — "how AI stores knowledge" is broadly interesting
- Freshness: 5/5 — most viewers have never seen the geometric story
- **Total: 19/20**
