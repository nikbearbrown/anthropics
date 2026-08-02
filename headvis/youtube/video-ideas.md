# headvis Video Ideas

## Candidate 1 — Unpacking attention edges into hidden feature interactions

- Source: `server.py`
- Topic: Feature-pair decomposition of attention edges via sparse dictionaries
- Hook: A single attention weight looks monolithic, but it's secretly the product of interacting sparse features
- Key case: In a gpt2 model, layer 5 head 2: query position 8 attends to key position 5 with weight 0.87. An SAE reveals this is the joint effect of Q-feature 142 ("detects pronouns") and K-feature 89 ("detects verbs"), cooperating.
- The Question: If a head's attention looks unified, why might the underlying feature interactions be sparse and multi-faceted?
- Core idea: Sparse dictionaries decompose dense dot products into discrete feature-pair contributions, making attention geometrically interpretable
- Visual object: An attention edge splitting into multiple colored feature-pair paths (like a circuit diagram)
- Manim move: split
- Example seed: Query learns "is this a noun?", key learns "is this a noun?", their product is one attention edge. SAE reveals: Q-feature 15 ("noun detector") fires, K-feature 15 fires, creating the main edge. But feature 28 on Q ("determiner detector") and feature 44 on K ("determiner detector") also contribute.
- Length band: 3–5 min
- Still lanes: c2v, raster
- Prerequisites: sparse autoencoders, attention heads, dot-product structure
- Exclusions: training procedures for SAEs, full mechanistic interpretation workflows
- Score: 8/10

## Candidate 2 — Layer-wise behavioral specialization revealed by metrics

- Source: `data_pipeline.py`
- Topic: Scatter-plot positioning of heads via induction score, previous-token score, entropy
- Hook: Attention patterns are high-dimensional; how do you summarize what a head does with a single number and spot patterns across 96 heads?
- Key case: Layer 2 heads scatter across (induction=0.05–0.3, entropy=0.8–1.2); layer 6 heads cluster tightly at (induction=0.65–0.85, entropy=0.2–0.4). This reveals specialization by layer.
- The Question: If induction score quantifies "how much does this head copy recent tokens?", why do layer 6-7 heads converge on high scores, while layer 0-2 scatter randomly?
- Core idea: Closed-form metrics project attention onto behavioral axes; scatter plots reveal layer-wise specialization and emergence of function
- Visual object: A 2D scatter plot of heads, with layer color-coding; points cluster by layer
- Manim move: accumulate
- Example seed: 8-layer, 12-head model. For each of 96 heads, compute induction_score and entropy. Plot reveals: layer 0 heads random blob (induction 0.1–0.3), layers 3-4 mixed, layers 6-7 tight cluster (induction 0.6–0.9). This tells a developmental story of head differentiation.
- Length band: 2–3 min
- Still lanes: raster, geo
- Prerequisites: attention, induction behavior, entropy, layer architecture
- Exclusions: how to compute induction score algorithmically, why these specific metrics
- Score: 8/10

## Candidate 3 — Embedding head operations reveals when they generalize

- Source: `data_pipeline.py`, `server.py`
- Topic: PCA/UMAP projection of Q, K, O, V vectors; custom prompts projected into the learned space
- Hook: Individual attention patterns are hard to compare. But if you embed queries and keys into a low-D metric space, similar operations cluster. New data reveals whether a head generalizes.
- Key case: Layer 5, head 2: the dataset's (Q, K) pairs form a tight blob in the bottom-left of the PCA plot. User types "The bird flew away"; these (Q, K) pairs project into the top-right, far from the blob. The head doesn't generalize.
- The Question: If a head has learned a specific input subspace in PCA, what does it tell you when a custom prompt lands in a different region?
- Core idea: PCA/UMAP gives you a visual metric space; out-of-distribution custom prompts reveal overfitting or specialization
- Visual object: The 2D projection cloud, with new custom prompts appearing as distinct clusters or outliers
- Manim move: accumulate, then project
- Example seed: Layer 5, head 2: training data points cluster (color: blue) at (x=−2, y=3). User enters "rare syntactic structure". Server computes Q/K for this prompt, projects via the saved PCA. New point lands at (x=4, y=−1), far from blue cluster. The head is syntactically specialized.
- Length band: 3–5 min
- Still lanes: geo, raster
- Prerequisites: PCA, projection, generalization, UMAP
- Exclusions: how PCA/UMAP algorithms work, training procedure, numerical stability
- Score: 8/10

## Candidate 4 — Stratification reveals activation-strength patterns

- Source: `data_pipeline.py`
- Topic: Decile bucketing of attention weights; per-decile example sequences
- Hook: Across a dataset, a single head generates millions of attention edges. You can't show them all. But the ranking and partition structure itself reveals the head's operating regime.
- Key case: Head 3, layer 4: interval 10 (highest-activation decile) shows queries attending to rare, syntactically coherent tokens; interval 1 (lowest-activation decile) shows near-zero noise patterns on common tokens; interval 5 is transitional.
- The Question: If activations span six orders of magnitude, does bucketing by decile reveal different head behaviors at each activation level, or just signal-to-noise?
- Core idea: Decile bucketing is both compression (show top examples per activation level) and a diagnostic (the distribution shape and per-decile patterns reveal the head's operating regimes)
- Visual object: A histogram showing frequency distribution, with each bucket linked to representative sequences
- Manim move: accumulate
- Example seed: Across 100k tokens, head 2 has 1.2M attention edges. Top 10% (decile 10) mean weight 0.73, minimum weight in decile 0.63. Next 10% (decile 9) mean 0.20. When you flip between deciles, the sequences shift from rare/syntactic (decile 10) to common/noise (decile 1).
- Length band: 2–3 min
- Still lanes: raster, geo
- Prerequisites: attention weights, ranking, bucketing
- Exclusions: implementation details of bucketing algorithm, why deciles vs. percentiles, statistical tests
- Score: 7/10

## Candidate 05 — A single token position hijacks every attention statistic across the whole dataset

- Source: `README.md`
- Topic: BOS token as attention sink; why max-reductions must exclude position 0
- Hook: Including one structural token in an aggregation makes every meaningful pattern invisible
- Key case: Head 3, layer 4: scanning 50k sequences, max_activation selects position 0 with weight > 0.55 in 91% of cases. The underlying syntactic dependency (verb→subject) only surfaces once position 0 is excluded from the max-reduction.
- The Question: If softmax forces attention weights to sum to 1 regardless of content, why should one specific position consistently absorb the plurality of probability mass across thousands of diverse input sequences?
- Core idea: When no key is strongly preferred, softmax must still allocate probability mass. The BOS token, always present and never competing for semantic attention, becomes a consistent low-resistance sink — heads park excess attention there, making it the dominant position in any max-aggregation that includes it.
- Visual object: An attention heatmap where position 0 glows persistently bright across many rows while all other cells stay dim; the same heatmap after masking reveals diverse, meaningful patterns in the remaining columns
- Manim move: collapse (many rows converge on position 0) then spread (masking reveals hidden structure)
- Example seed: 8-token sequence ["<BOS>", "The", "cat", "sat", "on", "the", "mat", "."]. Head 3 attention for "sat": [0.58, 0.04, 0.12, 0.09, 0.06, 0.04, 0.05, 0.02]. Scanning 1000 sequences: position 0 is the max-activation winner 94% of the time. After exclusion: "sat"→"cat" wins 68% of the time, revealing a subject-verb dependency.
- Length band: 2–3 min
- Still lanes: raster
- Prerequisites: softmax, attention weights, max-reduction
- Exclusions: KV-cache eviction and StreamingLLM applications of attention sinks, why BOS specifically accumulates this property during training
- Score: 9/10

## Candidate 06 — Softmax is a one-way gate: sequence length warps every metric computed after it

- Source: `README.md`
- Topic: Pre-softmax vs post-softmax metric hooking; sequence-length distortion in normalized attention
- Hook: A head expressing the same raw preference for one token looks far less "committed" in a long sequence than a short one — but only if you measure after softmax
- Key case: Head 2 attending to "cat" with logit score 5.0 in a 4-token sequence (competitors at 1.0): post-softmax peak = 0.95. Same head, same logit score, 20-token sequence (competitors still at 1.0): post-softmax peak = 0.74. Identical QK geometry; very different apparent confidence. The logit_* metrics hook before softmax and return 5.0 in both cases.
- The Question: If two heads express exactly the same raw dot-product preference for their top key, why does the post-softmax peak differ across sequence lengths — and which number actually describes the head's behavior?
- Core idea: Softmax divides each score by a partition function that grows with sequence length. The same logit gap yields a smaller post-softmax peak when more competitors dilute the probability mass. Pre-softmax logit metrics bypass this distortion and measure the head's preference in the model's own inner-product geometry.
- Visual object: Two side-by-side bar charts with identical raw logit gaps; their softmax transformations show dramatically different peak heights; a third row of "logit_max" labels stays equal
- Manim move: morph (identical logit bars collapse into different-height softmax peaks)
- Example seed: "The cat sat." (4 tokens) vs. a 20-token passage. In both, the query for "sat" has logit 5.0 toward "cat" and 1.0 toward every other token. Softmax peak: exp(5)/(exp(5)+3·exp(1)) ≈ 0.95 vs. exp(5)/(exp(5)+19·exp(1)) ≈ 0.74. logit_max = 5.0 in both. Label both 5.0; watch the softmax bars diverge.
- Length band: 2–3 min
- Still lanes: raster, c2v
- Prerequisites: softmax, dot-product attention, partition function
- Exclusions: implementation details of framework-specific forward hooks, which logit_* metrics headvis computes and why those three specifically
- Score: 7/10
