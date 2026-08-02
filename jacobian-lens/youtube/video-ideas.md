# jlens — Jacobian lens Video Ideas

## Candidate 1 — Concept identity flips sharply during embedding interpolation

- Source: `data/experiments/ignition.json`
- Topic: Layer-wise concept identity resolution
- Hook: Smoothly blend two country embeddings 50/50; the model's internal readout doesn't blend smoothly—instead it sharply favors one country, then flips to the other at a threshold.
- Key case: Set the `{W}` token embedding to 0.5·emb(France) + 0.5·emb(Germany); at layer 8 the lens reads France (rank 1), at layer 20 it reads Germany (rank 1), with the flip concentrated in layers 12–16.
- The Question: Embedding space interpolation should smoothly blend concept identity at each layer; why does the model's latent state show a sharp layer-dependent transition instead?
- Core idea: Concept identity is encoded as direction in residual space; when inputs are ambiguous, each layer independently resolves the ambiguity at different blend ratios, creating a cascading flip that propagates deeper.
- Visual object: Heatmap of (concept-A reciprocal-rank share) over [layer × (α − threshold)], showing sharp transition bands per country-pair.
- Manim move: accumulate|scan|split
- Example seed: Interpolate 0.3·Paris + 0.7·London embedding; model reads France at layer 6, UK at layer 18, threshold shifts predictably across country pairs.
- Length band: 3–5 min
- Still lanes: geo (embedding→latent), c2v (identity preservation), raster (layer × blend-factor)
- Prerequisites: embedding interpolation, lens readout, layer stacking
- Exclusions: multihead attention allocation; why threshold magnitude depends on country pair; exact residual-stream geometry
- Score: 10/10

## Candidate 2 — Reading what the model hasn't said yet

- Source: `README.md`
- Topic: Linear activation projection through layers
- Hook: Multiply a layer-8 activation by an average Jacobian and unembed to predict vocabulary—predicting what the model will eventually say, three layers before it computes it.
- Key case: Prompt "The ASCII-faced character has a ^, which is its"; lens at layer 12 reads "nose" (rank 1), though the prompt never says "nose" and the actual output is "feature".
- The Question: An internal activation should only predict final output after processing all remaining layers; why does linearly transporting it to vocabulary space already predict the latent goal?
- Core idea: The average Jacobian captures how each position's activation traces through downstream layers and emerges at the unembedding; multiplying and decoding reads out the implicit target of current-layer computation.
- Visual object: 2D grid [layer × token-position], each cell shows top-1 lens token; one cell highlighted and tracked across layers to show how predicted token changes with depth.
- Manim move: scan|trace
- Example seed: "Napoleon invaded [Italy]"; highlight Italy position; lens shows {Italy, Rome, invasion, campaign} cluster at rank 1 by layer 10, before model outputs "Italy".
- Length band: 2–3 min
- Still lanes: c2v (activation→vocabulary), raster (layer × position grid), trace (token rank over depth)
- Prerequisites: Transformer residual stream, token embeddings and unembedding, Jacobian matrices
- Exclusions: numerical Jacobian estimation; fitting procedure and convergence; corpus selection for expectation
- Score: 9/10

## Candidate 3 — Causality via surgical swapping

- Source: `data/experiments/probe-swap.json`
- Topic: Layer-dependent information bottlenecks
- Hook: Replace the model's internal representation of one concept with another's, and the final answer flips—but only at certain layers; swap at other layers has no effect.
- Key case: "Marie Curie won the [Prize]"; swap the lens direction of Prize↔Medal at layer 12; model generates "…Medal"; same swap at layer 4 doesn't change output.
- The Question: If swapping deletes information, why does the layer matter? Both removals lose the same signal.
- Core idea: Information refines and commits through layers; early layers can route around a swap, but mid-layers form a bottleneck where the information is necessary and irreplaceable.
- Visual object: Heatmap of [answer-flip rate] over [layer × concept-pair], showing critical-layer band where swaps succeed.
- Manim move: split|morph|collapse
- Example seed: "Abraham Lincoln signed the [Emancipation]"; swap to Constitution at layers 4, 12, 20; effect emerges at 10–16, disappears below and above.
- Length band: 2–3 min
- Still lanes: c2v (latent concept→output), raster (layer × concept-pair), comparison (before/after text)
- Prerequisites: lens readout, linear-probe directions, swap intervention
- Exclusions: gradient-based attribution; mechanistic analysis of which sublayers commit information; multi-token answers
- Score: 8/10

## Candidate 4 — Task interference in latent space

- Source: `data/experiments/dual-task.json`
- Topic: Representational capacity competition
- Hook: Single task: model tracks a concept perfectly mid-generation; same model with same concept but one arithmetic task running simultaneously: concept disappears from lens readout.
- Key case: Task 1: "Focus on animals, complete: The dog barked at the…"; concept-word rank ≤ 5 throughout generation. Task 2: "Focus on animals and remember 15÷3, complete: The dog barked at the…"; concept-word rank > 10 during response.
- The Question: The concept hasn't changed, the generation task is unchanged; why does adding one unrelated task erase the concept from latent readout?
- Core idea: Residual-stream capacity is finite; both tasks encode their target direction; whichever task has higher priority monopolizes the shared bottleneck.
- Visual object: Grouped bar chart [condition: concept alone | math alone | both-in-order-1 | both-in-order-2], axes [reachability rate = % positions where concept-word rank ≤ 5].
- Manim move: duplicate|split|collapse
- Example seed: "Focus on metals. Remember 24÷6, describe: The object was shiny"; metal-word reachability drops from 85% (single) to 40% (dual).
- Length band: 2–3 min
- Still lanes: raster (condition × task), c2v (latent bottleneck)
- Prerequisites: lens readout, concept tracking, covert-task setup
- Exclusions: attention-head competition; memory overhead of task representation; layer-wise capacity bounds
- Score: 8/10

## Candidate 5 — Linear steering with nonlinear saturation

- Source: `data/experiments/verbal-introspection.json`
- Topic: Dose-response of injected concept directions
- Hook: Inject a concept's lens direction at increasing strength; rank drops smoothly at first, then falls off a cliff at a threshold, flattening near-zero after.
- Key case: Inject "Einstein" steering at α ∈ {0, 0.1, 0.2, …, 1.0}; at α = 0.2 Einstein rank is ~400; at α = 0.3 it jumps to rank 5; at α ≥ 0.5 it's always rank 1.
- The Question: Lens directions are linear; output should respond linearly; why does the response show a sharp threshold and saturation plateau?
- Core idea: Lens directions are a linear mode, but output logits are a nonlinear function of the residual stream; once the injected direction dominates, further increases hit diminishing returns.
- Visual object: Line chart of [concept reciprocal-rank share] vs [strength α], showing linear decline, threshold knee, and plateau.
- Manim move: accumulate|trace
- Example seed: Inject "color-word" direction to "The car was…"; α = 0 gives "red" or "fast" randomly; α = 0.4 mostly colors; α ≥ 0.7 always colors (red, blue, silver).
- Length band: 2–3 min
- Still lanes: c2v (injected direction→output), raster (strength vs rank), curve (dose-response)
- Prerequisites: lens direction extraction, residual-stream steering, logit softmax
- Exclusions: layer-wise saturation at specific layers; MLP nonlinearity contribution; why threshold occurs at specific strength value
- Score: 7/10

Scanning the corpus for uncovered concepts before writing candidates.

The sources not yet used as primary cards: `lens-eval-typo.json`, `top-down-summoning.json`, `capacity.json`, `directed-modulation.json`, `flexible-generalization.json`, `lens-eval-multihop.json`. I'll evaluate each for motion, then write only those that pass the bar.

- **typo** — lens reads the *correct* spelling at the misspelled token, layer by layer. Strong accumulate/trace motion; 3-point surprise. Passes.
- **top-down-summoning** — the question preceding the passage primes which directions get amplified as passage tokens process; same stimulus, different question → different workspace content over the stimulus. Strong split/scan motion. Passes.
- **capacity** — counts how many list items are simultaneously in lens top-k; interesting accumulation, but the README gives no shape to the result curve, so the tension is underspecified. Borderline — skip.
- **directed-modulation** — focus vs suppress vs control hit-rate contrast; overlaps substantially with dual-task (Candidate 4). Skip.
- **flexible-generalization** — arg-swap generalizes across templates; interesting, but the mechanism is essentially the swap story in Candidate 3 applied to a different axis. Skip.
- **lens-eval-multihop** — intermediate reasoning steps surface in lens; the mechanism is identical to Candidate 2, just in a multi-hop setting. Skip.

Two new candidates pass.

---

# jlens — Jacobian lens Video Ideas

## Candidate 06 — The model spells it right inside even when the input is wrong

- Source: `data/evaluations/lens-eval-typo.json`
- Topic: Latent error correction before output
- Hook: Feed the model a sentence ending in a common misspelling; the lens at that exact misspelled token position already reads the correctly-spelled word, layer by layer, before any output is produced.
- Key case: Prompt ends with "…to recieve"; the last tokenizer fragment of "recieve" is the readout position; at layer 6 the lens ranks "receive" at ~150; at layer 14 rank 8; at layer 20 rank 1—while the surface token never changes.
- The Question: The residual stream at the misspelled token starts with that token's own embedding; if the model simply uses that embedding, the lens should read the misspelling, not the correction; why does the correct spelling rise to rank 1 mid-network?
- Core idea: Context before the typo (e.g., "make sure to") makes the intended word unambiguous; later layers integrate this context into the misspelled token's residual vector, pushing it toward the correct token's direction; the Jacobian lens traces that direction shift layer by layer.
- Visual object: Rank-vs-layer descent curve for the correctly-spelled word at the misspelled token position—starts high, drops sharply through mid-layers to rank 1.
- Manim move: trace|decay
- Example seed: "Please make sure to recieve the package"; lens at "ive" (final fragment of "recieve"): layer 4 rank 200, layer 10 rank 35, layer 18 rank 1 ("receive"). Labeled illustrative at build time.
- Length band: 2–3 min
- Still lanes: c2v (misspelled token → corrected direction), raster (layer × rank), trace (rank descent)
- Prerequisites: lens readout, tokenization basics, residual stream
- Exclusions: subword tokenization mechanics for multi-fragment misspellings; why the model may still *output* the misspelling in some contexts despite internal correction; attention-head attribution for which heads perform the correction
- Score: 9/10

## Candidate 07 — The question you ask changes what the same passage encodes

- Source: `data/experiments/top-down-summoning.json`
- Topic: Task-context priming of workspace content
- Hook: Present the same passage under two questions; under "predict the next word" the concept barely surfaces in the lens over the passage; under "what is the latent property?" the same passage positions suddenly show the concept at rank 1 across most of the band.
- Key case: Passage implies grief without naming it; Q1 ("predict next word") — grief appears in lens at <10 % of passage positions; Q2 ("what does the character feel?") — grief hits rank 1 at ~70 % of passage positions, same residual-stream tokens, same model.
- The Question: The passage tokens are identical under both conditions; their residual streams should encode the same surface content; why does placing a different question before the passage change what the lens reads over it?
- Core idea: The question precedes the passage in the prompt; as each passage token processes, it attends back to the question tokens and selectively amplifies directions that are relevant to answering the question; the lens reads these primed directions—demonstrating that task context acts as a top-down filter on what information a passage activates.
- Visual object: Side-by-side lens heatmaps [band-layer × stimulus position] under Q1 vs Q2, with a Q2 − Q1 difference strip below showing where the property label emerges.
- Manim move: split|scan
- Example seed: Passage: "He sat alone, holding her photograph"; Q1 before passage: grief at rank 180 over stimulus; Q2 before passage: grief at rank 1 over 6 of 8 stimulus positions. Labeled illustrative at build time.
- Length band: 2–3 min
- Still lanes: raster (Q1 vs Q2 heatmaps, difference strip), c2v (question priming → workspace), comparison (Q1 / Q2 side-by-side)
- Prerequisites: lens readout, workspace band, hit rate metric, causal attention
- Exclusions: which attention heads carry the backward priming signal; why some stimulus positions respond more than others; causal swap results across all token pairs
- Score: 8/10
