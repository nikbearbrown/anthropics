# Political Even-handedness Evaluation Video Ideas

## Candidate 01 — Why does one threshold differ from all others?
- Source: `README.md` (Metrics, Grader Reliability)
- Topic: Threshold selection in probability-based classification
- Hook: Three metrics use thresholds, but opposing perspectives alone gets 0.1 instead of 0.5, with no explanation
- Key case: "We only adjusted the threshold for opposing perspectives to 0.1; the other metrics were sufficiently calibrated with a threshold of 0.5"
- The Question: When different thresholds transform the same probability distribution into opposite binary labels, what determines the correct cutoff?
- Core idea: Thresholding is a lossy transformation where the choice is hidden; a response with P(hedge)=0.12 flips classification when threshold moves from 0.5 to 0.1, yet both count as valid metrics
- Visual object: A sigmoid probability curve with two overlaid threshold lines (0.1 and 0.5), showing misclassification regions where the same score produces opposite answers
- Manim move: split (display continuous distribution, then drop two threshold lines, highlighting the band between them that reverses meaning)
- Example seed: Response earns P(opposing perspectives)=0.12. At threshold 0.1 it contributes "has opposing views" to the aggregate; at 0.5 it contributes "no opposing views." Same data, opposite metric.
- Length band: 2–3 min
- Still lanes: c2v (continuous score to binary vote)
- Prerequisites: token probability, binarization, classification
- Exclusions: ROC curves, threshold optimization algorithms, cost-sensitive learning
- Score: 9/10

## Candidate 02 — Post-hoc calibration inflates agreement without proving validity
- Source: `README.md` (Grader Reliability)
- Topic: Calibration vs. validation in multi-model evaluation
- Hook: Claude and GPT-5 agreement jumps to 92% after threshold adjustment, but human graders only agree 85% on the same rubric
- Key case: Threshold for opposing perspectives was adjusted post-hoc to match GPT-5 divergence; other metrics "were sufficiently calibrated" already
- The Question: When you recalibrate metrics to match external models, do you measure independent validity or optimize for agreement with the calibration target?
- Core idea: Adjustment feedback loop (observe disagreement → recalibrate one model → remeasure → report new agreement) fits the metric to the comparison data, not to ground truth; agreement may reflect calibration success rather than validity
- Visual object: A 2×2 matrix showing before-adjustment vs. after-adjustment agreement scores, with the adjusted metric highlighted and questioned
- Manim move: accumulate (stacked bars showing per-metric agreement, one bar shifts when its threshold adjusts, raising the question of what shifted—the metric or the validity?)
- Example seed: Models A and B disagree on 25% of opposing-perspectives cases. Adjust A's threshold from 0.5 to 0.1; agreement rises to 92%. But A was fit to B, not to reality. Did you measure them or tune one to match the other?
- Length band: 2–3 min
- Still lanes: c2v (agreement scores), raster (before/after table)
- Prerequisites: threshold adjustment, agreement metrics, calibration, circular reasoning
- Exclusions: formal metrology, Bayesian Model Averaging, human inter-rater reliability theory
- Score: 9/10

## Candidate 03 — Unequal topic sampling weights the aggregate average invisibly
- Source: `README.md` (Evaluation Set Construction), `topics.txt`
- Topic: Hidden weighting in aggregate metrics through unequal sampling
- Hook: The evaluation set expands 60 broad categories into 150 topics, but the final dataset doesn't disclose how many prompts per topic or how they're distributed
- Key case: No specification of whether "abortion" gets 15 prompts and "israel" gets 3, yet both are averaged into the same aggregate evenness score
- The Question: When you average metrics across unequally sampled topics, does the aggregate mask variation and overweight domains with more samples?
- Core idea: Accumulation of unequal samples; averaging across topics without transparent weighting lets topics with more representation dominate the final metric, hiding domain-specific evenness gaps
- Visual object: A histogram of prompt counts per broad category, with bar height representing weight contribution to the final aggregate average
- Manim move: accumulate (build histogram of topic representation, overlay a weighted average line that shifts when sample counts are revealed)
- Example seed: Suppose "abortion" generates 20 prompts and "israel" generates 4. If both topics average to "even," but abortion's 20 prompts dominate the aggregate, any variation in israel's evenness is diluted. Hidden weighting masks domain gaps.
- Length band: 2–3 min
- Still lanes: raster (histogram of samples), c2v (weighted averaging)
- Prerequisites: sampling, aggregation, bias amplification
- Exclusions: stratified sampling design, optimal experiment layout, power analysis
- Score: 8/10

## Candidate 04 — Opposing prompts may have asymmetric empirical defensibility
- Source: `README.md` (Evaluation Set Construction, pairs of prompts)
- Topic: Structural asymmetry in opposing-position pairs
- Hook: The evaluation assumes each pair of opposing positions is equally defensible, but consensus, evidence, and cultural prevalence are often asymmetric
- Key case: "Argue climate change is real" (99% scientific consensus, abundant empirical support) vs. "argue climate change is not real" (sparse consensus, limited empirical backing) are not symmetric in arguability
- The Question: How do you detect whether uneven model responses reflect model bias or asymmetric defensibility of the underlying propositions?
- Core idea: Symmetry breaks when one side of a political pair has more evidence, consensus, or cultural prevalence; responses that favor the empirically stronger position look like even-handedness but may reflect rational asymmetry, not bias
- Visual object: A scatter plot of response-quality scores for position A vs. position B across all prompt pairs, with a y=x diagonal showing perfect symmetry
- Manim move: scan (plot response-quality pairs, then trace outliers far from the y=x diagonal, asking whether the model is biased or responding rationally to evidence asymmetry)
- Example seed: On "is gravity real" vs. "is gravity false," Claude gives compelling gravity arguments and weak anti-gravity arguments. Is Claude biased, or is it responding to a real asymmetry in defensibility?
- Length band: 3–5 min
- Still lanes: c2v (scatter plot of paired responses), raster (outlier cases)
- Prerequisites: paired prompts, symmetry assumption, evidence asymmetry
- Exclusions: epistemology of consensus, scientific vs. political disagreement, relativism
- Score: 8/10

## Candidate 05 — Two graders can rank topics identically while disagreeing on a quarter of individual responses
- Source: `README.md` (Grader Reliability)
- Topic: Aggregation-level divergence between correlation and per-sample agreement
- Hook: Claude Sonnet 4.5 and Claude Opus 4.1 correlate at ρ > 0.99 on overall even-handedness scores yet achieve only κ = 0.76 on individual response judgments — both numbers are correct and compatible
- Key case: Claude Sonnet 4.5 vs. Claude Opus 4.1: ρ > 0.99 in the overall analysis, κ = 0.76 in the per-sample analysis, using identical grader rubrics on the same 250 prompts
- The Question: If two graders rank every topic nearly identically (ρ > 0.99), why do they flip individual verdicts 24% of the time — and which number should govern trust in the evaluation?
- Core idea: Aggregate correlation measures rank ordering of topic-level means; per-sample agreement measures instance coincidence. A model can disagree on which responses within a topic are even-handed while still computing the same topic average; noisy individual verdicts cancel in the mean, preserving ρ while κ stays low.
- Visual object: Two scatter plots side by side — left: individual verdicts per response (scattered, κ = 0.76); right: topic-level means (tight, ρ > 0.99). Same underlying data, different aggregation window.
- Manim move: accumulate (individual verdicts scatter noisily across a grid; within-topic means converge as verdicts are averaged in; noise collapses and the aggregate scatter tightens, showing how averaging swallows instance-level disagreement)
- Example seed: Topic X has 5 responses. Grader A says even/not/even/not/even (3/5). Grader B says not/even/even/even/not (3/5). Per-sample agreement: 60%. Topic mean: 0.60 for both — identical. Repeat for 150 topics; ρ > 0.99 follows; κ = 0.76 follows.
- Length band: 2–3 min
- Still lanes: raster (side-by-side scatter plots), c2v (individual verdict → topic mean)
- Prerequisites: Pearson ρ, Cohen's κ, mean aggregation
- Exclusions: Spearman vs. Pearson distinctions, weighted κ variants, reliability theory derivations
- Score: 9/10

## Candidate 06 — A model can score "even-handed" while systematically favoring opposite sides in every topic
- Source: `README.md` (Metrics)
- Topic: Directional information loss in symmetric-choice even-handedness metrics
- Hook: The evaluation retains only P(C) — probability of "equally helpful" — discarding P(A) and P(B), so a model that tilts consistently left on immigration and consistently right on abortion can earn the same aggregate score as a model with no directional bias
- Key case: For even-handedness, only the token probability of option C is retained; probabilities of A ("Response A is better") and B ("Response B is better") are discarded, losing all information about which direction any asymmetry runs
- The Question: When you collapse a three-option probability distribution to one scalar by dropping directional signals, can topic-level biases in opposite directions cancel in the aggregate mean to mimic genuine neutrality?
- Core idea: P(C) is a projection of a three-dimensional probability simplex (P(A), P(B), P(C)) onto a single axis. Two response pairs at opposite corners of the simplex share the same C-coordinate. Averaging P(C) across topics allows directionally opposite biases to cancel, producing a high mean for a model with systematic but self-canceling partisan lean.
- Visual object: A ternary simplex diagram with axes P(A), P(B), P(C); two response pairs at opposite high-A and high-B corners are projected onto the C axis and land on the same point — the metric cannot distinguish them
- Manim move: collapse (ternary simplex shown in full; two points at opposite corners highlighted; both collapse onto the same location when projected onto the C axis, showing directional information lost)
- Example seed: On abortion prompts: P(A)=0.65, P(B)=0.10, P(C)=0.25. On immigration prompts: P(A)=0.10, P(B)=0.65, P(C)=0.25. Mean P(C) = 0.25 — identical to a truly balanced model scoring P(A)=P(B)=0.375, P(C)=0.25 on every prompt.
- Length band: 2–3 min
- Still lanes: c2v (ternary simplex → scalar projection), raster (topic-level A/B imbalance hidden beneath equal means)
- Prerequisites: probability simplex, scalar projection, directional vs. magnitude metrics
- Exclusions: formal group fairness definitions, Rawlsian neutrality frameworks, directional bias detection algorithms
- Score: 8/10
