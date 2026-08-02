## C05 — Attribution Graphs: Reading the Wiring Diagram Inside a Language Model

- **slug:** attribution-graphs-circuit-tracing
- **source:** ../anthropics/attribution-graphs-frontend/README.md (transformer-circuits.pub/2025)
- **bucket:** INTERPRETABILITY / VISUAL-MATH → sim-scout lens → math-explainer (Manim) + claude-explainer
- **premise:** Anthropic built a tool that traces which neurons activated which other neurons to produce a specific word in a specific sentence — giving you an actual computational graph you can inspect, not just aggregate statistics.
- **channel:** claude-liam (Kokoro am_onyx, Teardown register)
- **teachable claim:** For the first time you can look at a specific LLM output and trace the actual sequence of internal computation that produced it — not which inputs correlate with which outputs, but which circuits fired, in what order, with what weights.

### Ask beat (B00 — cold open, ClaudeComposerAsk)
- command: `Can you actually see inside an AI when it thinks?`
- topic: `AI INTERPRETABILITY · Attribution Graphs`
- segment: `The Wiring Diagram`
- greeting: `Ciao, Liam` (Wagwan check: not 0)

### Spine
B00 ASK → B01 why this is hard (billions of parameters, distributed representations) → B02 what attribution graphs are: directed graph from input token → intermediate features → output token → B03 DEMO VISUAL: the actual frontend from the paper — a specific sentence with nodes and edges → B04 what this enables: finding "grammar circuits," "indirect object identification," fact recall circuits → HANDOFF → OUTRO

### Sim-scout card fields
- **Lane:** D3/DATAVIZ (the frontend IS the artifact; a simplified interactive version is the sim)
- **The rule:** Each edge in the attribution graph has a signed weight — how much did feature A's activation causally increase feature B's activation in the residual stream? Computed via activation patching: patch one node's value, measure downstream change.
- **The artifact / what moves:** A force-directed graph where nodes are model features and edges are attribution weights. Click a node to highlight its upstream/downstream neighborhood. Drag to rearrange. Edge thickness = attribution weight; color = sign (positive/negative influence).
- **Two testable predictions:**
  - P1: The "Indirect Object Identification" circuit (the paper's canonical example: "John and Mary went to the store; Mary gave a drink to ___") shows a small, identifiable subgraph that consistently activates for the correct pronoun
  - P2: Ablating (zeroing out) the identified circuit nodes degrades performance specifically on IOI sentences while leaving unrelated tasks intact
- **Human supplies:** Nothing — the frontend repo runs with `npx hot-server` locally; the paper's examples are in the repo

### Visual beats (4 suggested)
1. **B01 — Manim:** A transformer block as a black box. Input tokens enter. Output tokens exit. Interior: a tangle of unlabeled lines. Label: "We knew the input and output. Not the path."
2. **B02 — Manim graph emerging:** The black box's tangle resolves into a cleaner directed graph as attribution is applied. Nodes light up in sequence. Edge weights appear as thickness. The resolution metaphor: from fog to wiring diagram.
3. **B03 — Human screen recording or screenshot of the actual attribution-graphs-frontend:** The interactive layer×position view from the paper, zoomed in on the IOI example. Show clicking a node and watching the neighborhood highlight. This IS the product being taught.
4. **B04 — Remotion concept card:** Three circuits found via this method: IOI circuit, factual recall, syntax agreement. Each shown as a tiny labeled graph. Point: the tool is now general — you can find circuits for other behaviors.

### Register notes
Teardown: this work is a step change — moving from "which heads are important on average" to "here is the exact computational path for this prediction." The honest limit: the graphs are still complex and hard to read for non-experts. This is interpretability research, not interpretability solved.

### Est length
~140 s (mechanism + interactive demo)

### Scores
- Teachability: 4/5 — the concept is clear; the graphs are complex but the point lands
- Visual potential: 5/5 — the actual interactive frontend is a showpiece visual
- Audience pull: 4/5 — "see inside a working AI" is broadly compelling
- Freshness: 5/5 — circuit tracing at this scale is brand new (2025)
- **Total: 18/20**
