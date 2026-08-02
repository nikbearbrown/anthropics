# Video Ideas — math-bayesian-probability

Scouted: 2026-07-09
Source book: Bayesian Probability — AI+1, Hands on. Domain specific. No generic prompts.
Chapters read: 00-probability-foundations through 13-choosing (14 narrative chapters)

---

## Candidate 01 — The Test That Is 99% Accurate (And Why the Answer Is 9%)

- Source: `math-bayesian-probability/chapters/01-the-same-question-two-answers.md`
- Topic: BAYESIAN THINKING
- Hook: A test is 99% accurate. A patient tests positive. Most people say there is a 99% chance they have the disease. The real answer is 9%. The test is not broken — the math is.
- Key case: Disease prevalence 1 in 1,000; sensitivity 99%; false positive rate 1%. Of 10,000 screened: 10 true positives, 100 false positives. Only 10 of 110 positives have the disease.
- The Question: If a 99%-accurate test comes back positive, what is the actual probability the patient is sick — and why is it so far from 99%?
- Core idea: When a disease is rare, healthy people vastly outnumber sick people, so even a small false-positive rate creates a flood of false alarms that drowns the true cases. The posterior probability depends on who gets tested, not just how good the test is.
- Visual object: A population of 10,000 dots that splits into disease/healthy, then into positive/negative test columns — true positives teal, false positives crimson — so the viewer sees 10 teal dots next to 100 crimson dots.
- Manim move: split (population → disease status) then split again (test result), then collapse both positive columns into a single bar so the 10:100 ratio is unavoidable
- Example seed: A city screens 10,000 people for a rare condition. Ten have it; all ten test positive (teal). One hundred healthy people also test positive (crimson). The doctor holds 110 positive results. Nine of ten are false alarms.
- Length band: 3–5 min
- Still lanes: geo (hospital screening queue), c2v (Bayes theorem derivation panel)
- Prerequisites: Viewer understands that tests can make errors; no probability notation needed
- Exclusions: No Bayes formula on screen; no p-values; no frequentist framing; no discussion of sensitivity vs. specificity by name — carry the concept visually only
- Score: 10/10

---

## Candidate 02 — Why Small Schools Look Like Geniuses (The Partial-Pooling Problem)

- Source: `math-bayesian-probability/chapters/09-hierarchical-problems.md`
- Topic: BAYESIAN THINKING
- Hook: The highest-scoring school in the district has 8 students. The worst-scoring school has 6. Both rankings are almost certainly wrong — and the statistics can prove it.
- Key case: 30-school district; School C (n=8) raw mean 92%; School A (n=200) raw mean 74%. After partial pooling, School C's estimate drops to 83% and School A barely moves. The ranking was noise.
- The Question: When a small school outperforms every other school in the district, should you believe the result — and how much should you trust a ranking built on tiny samples?
- Core idea: The no-pooling estimator is mathematically inadmissible: there always exists a shrinkage estimator with lower total error (Stein's paradox). The trick is to let each school borrow information from the district average — small schools borrow heavily, large schools barely at all.
- Visual object: A dot-and-rope diagram: each school is a dot, pulled by a rope toward the district mean; the rope's tension scales with 1/n so small schools snap toward center and large schools barely move.
- Manim move: accumulate (dots appear per school proportional to n) then trace (ropes materialize and pull small-n dots toward center, leaving large-n dots nearly fixed)
- Example seed: School C scores 92% on 8 students. School A scores 74% on 200 students. After borrowing from the district mean of 72%, School C's estimate drops to 83%. It is still above average — but the 18-point lead was mostly noise. School A barely moves. Two hundred data points speak for themselves.
- Length band: 3–5 min
- Still lanes: geo (school building exterior), c2v (shrinkage factor equation panel)
- Prerequisites: Viewer understands the idea of an average; no prior probability knowledge required
- Exclusions: No MCMC mechanics; no REML estimation details; no discussion of hyperpriors or variance components by name; no comparison to mixed-effects models
- Score: 9/10

---

## Candidate 03 — The Interval That Cannot Answer the Question

- Source: `math-bayesian-probability/chapters/03-counting-and-estimating.md`
- Topic: BAYESIAN THINKING
- Hook: A quality engineer computes a confidence interval for the defect rate. The interval says [7%, 28%]. She asks: what is the probability the rate is below 20%? The confidence interval has no answer — not because the data is bad, but because it is the wrong kind of interval.
- Key case: 8 defective boards in 50; Wilson 95% CI [7.4%, 28.4%]; Bayesian 95% credible interval [8.2%, 29.5%] — nearly identical numbers, but only one can answer P(rate < 20%) = 76%.
- The Question: A confidence interval and a credible interval look almost identical on a chart — so why can one answer the engineer's decision question and the other cannot?
- Core idea: A confidence interval is a statement about the procedure — 95% of such intervals contain the true rate — not about this particular interval. A credible interval is a direct probability statement about the parameter. Same numbers, different philosophical content, different decision power.
- Visual object: Two intervals drawn side by side on the same number line, numerically near-identical, but with their interpretive labels animating differently — one "procedure guarantee" vs. one "probability statement" — then a threshold line at 20% and only the credible interval shading the region below it.
- Manim move: morph (single interval duplicates into two identical-looking intervals; labels differentiate them; threshold line appears; one interval fills with probability mass, the other does not)
- Example seed: Eight defective boards in fifty. Both intervals sit from roughly 8% to 29%. The threshold is 20%. The engineer asks: what is the chance the real rate is below 20%? The Bayesian posterior says 76%. The confidence interval stares back silently.
- Length band: 2–3 min
- Still lanes: c2v (Beta distribution posterior shape panel)
- Prerequisites: Basic idea of a margin of error; no prior probability knowledge needed
- Exclusions: No Beta distribution parameterization; no conjugacy mechanics; no Jeffreys prior discussion; no Wilson formula derivation
- Score: 9/10

---

## Candidate 04 — Same Data, Two Conclusions: The Hidden Prior

- Source: `math-bayesian-probability/chapters/07-priors.md`
- Topic: BAYESIAN THINKING
- Hook: Two statisticians look at the same clinical trial and reach opposite conclusions. One says the drug works. One says it probably does not. Both analyses are valid. The difference is a prior one chose to name.
- Key case: Mean blood pressure reduction 4.9 mmHg, SE 2.3, n=40; p=0.038 (significant). Flat-prior Bayesian: P(effect > 3 mmHg) = 79%. Informative prior (two prior failed trials): P(effect > 3 mmHg) = 27%.
- The Question: If both statisticians see the same 40 patients, run valid analyses, and reach opposite conclusions — whose answer do you trust, and where did the difference come from?
- Core idea: Every analysis carries a prior. The frequentist t-test uses a flat prior: it treats a 100-mmHg drug effect as equally plausible as a 4.9-mmHg one. An informative Bayesian prior reflects accumulated evidence from related trials. Neither analyst is cheating — they are answering different questions about what the data adds to different bodies of prior knowledge.
- Visual object: A single posterior distribution that morphs as the prior changes — wide and tall (flat prior), then squeezed leftward (informative prior) — while the likelihood stays fixed and visible as a separate curve. The intersection of prior and likelihood traces the posterior.
- Manim move: transform (likelihood curve is fixed; prior slides from flat to peaked; posterior morphs in real time showing how prior shape drives the tail probability past the 3 mmHg threshold line)
- Example seed: The drug's compound failed two prior Phase III trials. Before this new trial, an FDA reviewer encodes that history: the prior says small effects are likely, large ones are not. The new trial's 4.9 mmHg result shifts the posterior — but not nearly as much as the company's flat-prior analysis suggests. Seventy-nine percent vs. twenty-seven percent, same forty patients.
- Length band: 3–5 min
- Still lanes: geo (pharmaceutical lab or clinical chart), c2v (three-panel prior comparison table)
- Prerequisites: Basic understanding that averages have uncertainty; no probability notation required
- Exclusions: No Jeffreys prior; no improper priors; no empirical Bayes; no regulatory guidance specifics; no discussion of FDA submission procedures
- Score: 9/10

---

## Candidate 05 — Why Significant Results in Small Studies Are Wrong Twice

- Source: `math-bayesian-probability/chapters/08-when-data-is-sparse.md`
- Topic: BAYESIAN THINKING
- Hook: A sports medicine study finds a 100% risk reduction for knee injuries. The study has 18 athletes. Published, peer-reviewed, cited. Almost certainly wrong — and the statistics can tell you exactly how wrong, and in which direction.
- Key case: True effect = 30% risk reduction. Study power = 15%. Published significant results from this design overstate the true effect by 3.5x on average (Type M error). The "100% reduction" is probably closer to 30% — but only the studies that shouted "100%" got published.
- The Question: When a study reports a dramatic result from a tiny sample, is the effect real — and if it is real, why is the published number almost certainly too large?
- Core idea: When statistical power is low, the only way a study clears the significance threshold is by accidentally drawing an extreme sample. The significance bar acts as a filter: inflated results get published, accurate ones get filed away. This is not fraud — it is the mathematical consequence of a threshold applied to an underpowered test.
- Visual object: A distribution of effect sizes that 1,000 imaginary replications would observe, with a vertical significance bar at the threshold. Studies to the right of the bar are published (crimson); studies to the left are not (slate). The published distribution's center is far right of the true effect (teal line).
- Manim move: spread (1,000 study dots accumulate under the distribution curve); decay (dots left of the threshold fade to slate/invisible); collapse (surviving dots form a new distribution whose center the viewer can compare to the true-effect line)
- Example seed: Imagine 1,000 researchers each run the 18-athlete warm-up study. About 150 get p < 0.05. What do those 150 find? Not 30% reduction — around 100%, because that is the magnitude needed to clear the significance bar at n=18. The 850 accurate studies are never seen.
- Length band: 3–5 min
- Still lanes: geo (sports medicine or lab setting), c2v (Type M / Type S error table panel)
- Prerequisites: Basic understanding of "statistically significant"; no formula knowledge needed
- Exclusions: No Bayesian shrinkage mechanics (focus on the frequentist failure mode); no Beta-Binomial derivation; no MCMC; no hospital complication rate example
- Score: 9/10

---

## Candidate 06 — The Threshold No One Chose (But Everyone Lives With)

- Source: `math-bayesian-probability/chapters/11-classification-and-decision.md`
- Topic: BAYESIAN THINKING
- Hook: Every loan-approval model in existence quietly assumes that approving a bad loan and rejecting a good one are equally bad mistakes. They are not. And no one decided this — it was the default.
- Key case: Bad loan costs $20,000; rejected good loan costs $4,000 (5:1 ratio). Optimal threshold from expected-cost minimization: 1/(1+5) = 16.7%, not 50%. At the correct threshold, expected cost per 100 applications drops 25%.
- The Question: When a machine learning model outputs a probability and you set the threshold at 0.5, what decision are you secretly making — and is it the right one?
- Core idea: The decision threshold is not a statistical output — it is a statement about relative costs. Threshold 0.5 minimizes total misclassifications when both errors cost the same. Threshold = c_FP/(c_FP + c_FN) minimizes expected cost for any asymmetric cost structure. The formula is two lines of algebra from Abraham Wald (1950).
- Visual object: A single ROC curve with a movable threshold point; as the threshold slides from 0.5 down to 0.167, the sensitivity/specificity tradeoff traces along the curve, and a running cost meter (expected cost per 100 applications) ticks down until it hits a minimum.
- Manim move: trace (threshold point slides along ROC curve from 0.5 toward cost-optimal point); accumulate (cost meter fills and then empties as threshold passes the minimum)
- Example seed: A fintech sets its threshold at 0.5. Six months later: high default rates. Investigation finds 1,400 loans approved with predicted default probabilities between 35% and 50%. At a 5:1 cost ratio, the optimal threshold is 16.7%. Every loan above 16.7% should have been reviewed. The 0.5 default silently approved the riskiest quartile.
- Length band: 2–3 min
- Still lanes: c2v (cost derivation panel: two-line algebra), geo (loan application desk)
- Prerequisites: Basic understanding of machine learning outputs as probabilities; no statistics background required
- Exclusions: No Bayesian logistic regression mechanics; no MCMC; no posterior distributions; no fairness/equity analysis (COMPAS); no discussion of model calibration
- Score: 8/10

---

## Candidate 07 — Most Published Research Findings Are False (The Math Behind the Claim)

- Source: `math-bayesian-probability/chapters/04-comparing-two-groups.md`
- Topic: BAYESIAN THINKING
- Hook: In 2005, a paper with the title "Why Most Published Research Findings Are False" appeared in one of medicine's top journals. The argument was not about fraud or bad science. It was a two-line probability calculation that most researchers had never seen.
- Key case: R = 20% prior probability that any given hypothesis is true; power = 50%; alpha = 0.05. Of 1,000 hypotheses tested: 100 true positives, 40 false positives. Positive predictive value = 100/140 = 71%. More than 1 in 4 "significant" results is wrong.
- The Question: If a study reaches p < 0.05, what is the actual probability that the finding is real — and why does the answer depend on something the study never measured?
- Core idea: The significance test asks "how surprising is this data if the null is true?" — but the researcher needs to know "how likely is the hypothesis given this data?" Those require Bayes' theorem, a prior on how often hypotheses in this field are correct, and the test's power. Ignore any of those three ingredients and the calculation is incomplete.
- Visual object: A 2x2 contingency table of all hypotheses tested (true/false) vs. results (significant/not) — built cell by cell so the viewer sees each count appear, culminating in the PPV = 100/140 fraction highlighted in teal.
- Manim move: accumulate (dots fill each cell of the 2x2 table as narration names each count); split (the significant column separates and the PPV fraction labels itself)
- Example seed: 1,000 studies. 200 test real effects; 800 test null effects. With 50% power, 100 real effects are detected. With 5% false-positive rate, 40 null results look significant anyway. The journal's "significant" pile: 140 papers. 40 are wrong. The statistician did nothing wrong. The field's prior probability of a true effect is the invisible variable.
- Length band: 2–3 min
- Still lanes: c2v (Ioannidis table panel), geo (journal stack or research lab)
- Prerequisites: Basic understanding of what "statistically significant" means; no formula knowledge required
- Exclusions: No Bayesian two-group analysis; no posterior distributions; no credible intervals; no educational tutorial scenario; no replication crisis historical examples beyond the Ioannidis argument structure
- Score: 8/10

---

## Candidate 08 — Which Model Is More Likely to Be True? (Why Rankings and Probabilities Are Not the Same)

- Source: `math-bayesian-probability/chapters/06-model-comparison.md`
- Topic: BAYESIAN THINKING
- Hook: Two epidemic models both fit the first 30 days of data. One predicts a manageable outbreak; the other predicts a catastrophe. The health official asks: "Which model is more likely to be correct?" AIC can tell her which fits better. It cannot answer the question she actually asked.
- Key case: Linear growth vs. exponential growth for epidemic data; AIC difference = 4.2 (favors exponential); Bayes factor = 8.3; P(exponential model | data) = 89% with equal priors. Same data, two different outputs.
- The Question: When two models both fit the data, how do you find out which one is probably right — not just which one fits better?
- Core idea: AIC measures predictive accuracy — which model would make better predictions on new data from the same process. The Bayes factor measures something different: how much more likely is the data under one model than the other, averaged over all plausible parameter values. AIC produces a ranking. The Bayes factor produces a probability. For communicating to officials who need to decide, only one of those is actionable.
- Visual object: Two fitted curves (linear teal, exponential crimson) through the same scatter of data points, both plausible-looking; then a confidence/probability meter for each model that AIC fills partially (ranking bar) and the Bayes factor fills with a probability (89% arc) — making visible what each criterion returns.
- Manim move: compare (two curves materialize simultaneously against the data), then split (AIC ranking fills a bar chart; Bayes factor fills a probability arc — different visual grammar for different outputs)
- Example seed: March 2020. Thirty days of case counts curve upward. Linear model: 4,000 cases by day 60. Exponential model: 40,000 cases. Both fit the first 30 days almost equally well. AIC says exponential is better by 4.2 units. The Bayes factor says the data are 8.3 times more consistent with exponential growth. P(exponential | data) = 89%. The health official can brief her board with a number.
- Length band: 2–3 min
- Still lanes: geo (public health briefing room or epidemic data dashboard), c2v (Jeffreys evidence scale panel)
- Prerequisites: Basic understanding that models make predictions; no statistics background required
- Exclusions: No PSIS-LOO cross-validation; no marginal likelihood integration details; no prior sensitivity analysis mechanics; no BIC discussion; no MCMC
- Score: 8/10

---

*Scouted by Claude — 2026-07-09. All scores based on: Surprise/aha (0–3) + Visual obviousness (0–3) + Self-containment (0–2) + Pedagogical payoff (0–2). Cards written only for scores ≥ 8.*
