# Hh Rlhf Video Ideas

## Candidate 1 — Why simple sampling beats model fitting

- Source: `README.md`
- Topic: Rejection sampling in RLHF data collection
- Hook: Generate 16 random responses, pick the best one—why is this a competitive strategy against training a better model?
- Key case: Helpfulness data collected via "rejection sampling (mostly with best-of-16)" as a tranch between base and online training
- The Question: Best-of-K sampling should be noisier than training a model; why does plurality voting outperform fitted models?
- Core idea: With K large enough, the probability of "all K responses are bad" becomes vanishingly small (concentration of measure), so the max is reliable without explicit learning
- Visual object: Sixteen candidate boxes branching from a prompt, one highlighted as winner
- Manim move: split, collapse
- Example seed: Generate 4 lunch recipes, have humans vote on best. Voting picks a genuinely good recipe 80% of the time. Train a "better recipe ranker" on 20 examples—does it beat the voting? Often not, because 20 is too small to beat law-of-large-numbers. (illustrative)
- Length band: ~1–2 min
- Still lanes: raster (candidate grid), c2v (vote to winner)
- Prerequisites: Sampling, preference ranking
- Exclusions: Likelihood weighting, temperature-based sampling, concentration bound proofs
- Score: 8/10

## Candidate 2 — Why humans find failure modes faster than random search

- Source: `README.md`
- Topic: Human adversarial red teaming vs. automated worst-case discovery
- Hook: A crowdworker breaks the model in three tries; random fuzzing would need a thousand. Why does human structure beat brute force?
- Key case: Red team transcript shows human attacker with a hypothesis, executing it, rating their own success on Likert scale; one human finds failure modes that automated search misses
- The Question: Computational search should beat bounded human effort; why does a hypothesis-driven human attack find model failures in fewer steps?
- Core idea: Humans reason backwards from desired failure (e.g., "model values politeness, exploit that") and follow causal structure; random search explores pointless branches
- Visual object: Tree of attack attempts, leaves color-coded by success (red fail, green break), human path vs random walk overlaid
- Manim move: scan, compare
- Example seed: Model is trained to be helpful. Attacker hypothesizes "If I ask for help with a fake crisis, model will sacrifice safety for helpfulness." One attack succeeds. Blind random prompting needs to stumble on that structure by luck. (illustrative)
- Length band: 2–3 min
- Still lanes: c2v (adversary reasoning to attack), raster (success heatmap)
- Prerequisites: Reinforcement learning basics, adversarial examples
- Exclusions: Gradient-based attacks, certified robustness, automated red-team systems
- Score: 8/10

## Candidate 3 — Why iteration on self-generated data doesn't collapse

- Source: `README.md`
- Topic: Iterated preference-model training loop
- Hook: Train a preference model; use it to sample; train on those samples; repeat. Does this positive feedback loop spiral into gibberish or genuine improvement?
- Key case: Helpfulness dataset has three tranches—base models, rejection-sampled via early preference model, then "online" iterative process—each stage uses the previous stage's model to generate candidates
- The Question: Why does iteration on self-generated data yield improvement instead of mode collapse where the preference model and response model drift into local optima?
- Core idea: Active learning circuit—each round surfaces cases where the current model is uncertain (hard negatives), creating a moving frontier of difficulty rather than a fixed target
- Visual object: Reward curve rising across three tranches, or preference distribution narrowing/shifting between rounds
- Manim move: accumulate, transform
- Example seed: Round 1: collect human feedback on base outputs. Train ranker. Round 2: use ranker to generate top-2 pairs, collect feedback (harder cases). Does Round 2 ranker beat Round 1? Yes, because data is harder and closer to frontier. (illustrative)
- Length band: 2–3 min
- Still lanes: raster (metric progression), c2v (feedback to ranking to generation)
- Prerequisites: Preference learning, RLHF, active learning
- Exclusions: PPO training details, mathematical optimality, divergence proof
- Score: 7/10

## Candidate 4 — Why you score the attacker's description separately

- Source: `README.md`
- Topic: Dual-track harmlessness measurement
- Hook: The model's response to an attack is harmful—but so is the attack description itself. How do you train on harmful data without making the model harmful?
- Key case: Red teaming JSON includes both `min_harmlessness_score_transcript` (model's response harmlessness) and `task_description_harmlessness_score` (attacker's instruction harmlessness), requiring separate ratings
- The Question: If your training data pairs harmful prompts (attack descriptions) with benign responses (refusals), does the model learn to generate those attacks?
- Core idea: Measurement decoupling—score what the model outputs independently from what it receives. Prevents optimization toward generating attacks while learning to refuse them
- Visual object: Two parallel measurement tracks or a 2×2 grid: (request harm, response harm) with dots scattered, region where request is high but response is low highlighted
- Manim move: split, compare
- Example seed: Train a model to refuse violence requests. Data: "How do I make a bomb?" (harmful request) + "I can't help with that" (safe response). Measure: request harmful? Yes. Response harmful? No. Only measuring response would miss the decoupling. (illustrative)
- Length band: ~1–2 min
- Still lanes: c2v (dual measurement), raster (request-response harm heatmap)
- Prerequisites: Measurement bias, RLHF
- Exclusions: RLHF loss mechanics, constitutional AI, harm taxonomies
- Score: 6/10

Scanning the README for concepts not yet covered by the four existing candidates.

The README contains one explicit structural asymmetry that none of the four cards touch: helpfulness data spans three training tranches while harmlessness data is collected only from base models. That contrast is stated directly in the text, has a non-obvious causal mechanism, and produces a clear visual.

No other new concepts in the corpus clear the motion-and-question bar. The `num_params` and `rating` fields suggest a scaling-behavior concept, but the README states only the field names — no findings appear in the supplied corpus, so any card would be fabricating content from the paper rather than the corpus.

---

# Hh Rlhf Video Ideas

## Candidate 05 — Why the safer objective gets the fewest training rounds

- Source: `README.md`
- Topic: Asymmetric iteration between helpfulness and harmlessness data pipelines
- Hook: Helpfulness data is refined through three rounds of progressive training; harmlessness is collected once and frozen. Shouldn't the safety objective be the one you keep iterating?
- Key case: README states helpfulness spans three tranches (base, rejection-sampled, online) while harmlessness is "only collected for our base models"
- The Question: If iterated sampling improves data quality for helpfulness, why not apply the same loop to harmlessness — the more consequential objective?
- Core idea: Iterating harmlessness requires generating candidate responses to harmful prompts in bulk, then selecting the best refusal. Each round produces a model that elicits more targeted harmful outputs as its candidate pool, turning the data pipeline itself into a refinement engine for harmful content.
- Visual object: Two vertical tracks side by side — helpfulness climbs through three labeled stages; harmlessness stays pinned at stage one; the gap between them widens with each round
- Manim move: accumulate (helpfulness track rises), compare (gap between tracks)
- Example seed: Round 1 — 'How do I pick a lock?' → model refuses; human approves. Train ranker. Round 2 — ranker generates 8 candidate responses to new harmful prompts; 7 are partial answers, 1 is a refusal; pick the refusal. Your training data now contains 7 partial lockpicking instructions. By round 3 the pipeline is producing increasingly refined harmful content to find the one refusal to keep. (illustrative)
- Length band: ~1–2 min
- Still lanes: c2v (pipeline stage diagram), raster (asymmetric progress chart)
- Prerequisites: RLHF basics, preference learning
- Exclusions: Constitutional AI as an alternative, specific harm taxonomies, the mathematical formulation of the harmlessness reward signal
- Score: 9/10
