# Bayesian Probability: with LLMs — CLI Video Ideas ("X with Claude")

---

> **Note:** This book currently contains only placeholder frontmatter and back-matter chapters (00-frontmatter.md, 99-back-matter.md). No substantive chapter content is present. Cards below are drafted from the book's stated scope — Bayesian probability and LLM exercises — based on the author's other titles in this series (which follow a consistent BUILD + LLM-exercise pattern). When chapter content is added, these cards should be revised and scored against actual exercises.

---

## Candidate 01 — "Build a Bayesian Coin-Flip Updater with Claude Code"
- Source: bayesian-probability-with-llms/chapters/00-frontmatter.md (scope; no chapter content yet)
- Lane: BUILD (Claude Code)
- Hook: Bayesian inference is a machine for changing your mind proportional to evidence — not to being wrong. A coin-flip updater shows the entire update cycle in 10 lines and makes the prior-to-posterior shift visible.
- The artifact: A Manim animation of Bayesian updating for coin-flip inference: a beta distribution prior (uniform) that updates after each observed flip, the posterior narrowing as evidence accumulates. The script accepts N flips and k heads, computes the beta posterior analytically, and animates the distribution tightening over 20 sequential observations.
- Prompt seed: `claude "Write a Python script that performs Bayesian updating for a biased coin. Start with a Beta(1,1) uniform prior on p_heads. After each of 20 flips (10 heads, 10 tails), compute the Beta posterior analytically: Beta(alpha + k_heads, beta + k_tails). Plot the evolving distribution. Animate in Manim: show the prior, then each posterior update as a curve that shifts and narrows, with the true probability marked."`
- Read / check: Verify that Beta(1+k, 1+(n-k)) is the correct conjugate posterior for a Binomial likelihood with Beta prior. Verify the posterior mean converges to the true p as n increases. Verify the animation shows the distribution narrowing (not just shifting) with more data.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated beta distribution updating after each flip, posterior tightening)
- The change: Add two competing priors: a strong prior for p=0.7 (Beta(7,3)) vs. the uniform — show that with enough data both converge to the true p, but the biased prior takes longer.
- Teardown angle: The update is mechanical — Bayes' theorem doesn't care what you believe, only by how much the evidence shifts it. The prior is not stubbornness; it's information about base rates.
- Exclusions: Cut Markov Chain Monte Carlo; cut hierarchical Bayes; cut full frequentist comparison.
- Score: 9/10

---

## Candidate 02 — "Simulate Medical Test False Positives with Claude Code"
- Source: bayesian-probability-with-llms/chapters/00-frontmatter.md (scope; no chapter content yet)
- Lane: BUILD (Claude Code)
- Hook: A test with 99% accuracy on a disease affecting 1% of the population is wrong 50% of the time when it says positive. This is the base-rate neglect fallacy — and it kills people who misread medical tests. Claude can compute it and animate the confusion matrix.
- The artifact: A Python script that computes the full Bayesian analysis for a medical test: given prevalence, sensitivity, and specificity, computes posterior P(disease | positive test) via Bayes' theorem. Manim animates a population of 10,000 people split into 4 groups (true positive, false positive, true negative, false negative), then shows the PPV calculation as counts flowing into buckets.
- Prompt seed: `claude "Write a Python script computing the positive predictive value of a medical test using Bayes' theorem. Parameters: disease prevalence 1%, test sensitivity 99%, specificity 99%. Compute: P(disease | positive), P(disease | negative), plot the 2x2 confusion matrix. Then animate in Manim: start with 10000 people, split by disease status (100 sick, 9900 healthy), then split each group by test result, show the 4 buckets, and highlight that of 198 positive tests, only 99 are true positives."`
- Read / check: Verify calculation: 100 sick × 0.99 = 99 TP; 9900 healthy × 0.01 = 99 FP; PPV = 99/(99+99) = 50%. Verify the confusion matrix shows correct counts. Verify the animation correctly routes people through disease status → test result → bucket.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated population splitting into 4 buckets with PPV revealed)
- The change: Show how PPV changes with prevalence: plot PPV vs prevalence for fixed sensitivity/specificity — demonstrate that screening low-prevalence populations produces mostly false positives even with accurate tests.
- Teardown angle: The test accuracy is not the probability the result is correct. Prevalence is prior information that must be included. This is why mass screening programs for rare diseases require careful threshold-setting.
- Exclusions: Cut ROC curves; cut multi-test sequential updates; cut Bayesian network notation.
- Score: 9/10

---

## Candidate 03 — "Build a Naive Bayes Text Classifier with Claude Code"
- Source: bayesian-probability-with-llms/chapters/00-frontmatter.md (scope; no chapter content yet)
- Lane: BUILD (Claude Code)
- Hook: Naive Bayes spam filtering is Bayes' theorem applied word by word — and the "naive" part (treating words as independent) is wrong but works remarkably well. Claude can build a working classifier in under 50 lines.
- The artifact: A Python script that implements a Naive Bayes classifier from scratch (no scikit-learn): tokenizes training emails, computes word log-likelihoods per class, classifies test emails using the log-sum-of-log-likelihoods approach. Manim animates the classification of a single test email word by word, showing each word's contribution to the log-posterior as a growing bar chart.
- Prompt seed: `claude "Build a Naive Bayes email spam classifier from scratch in Python (no ML libraries except numpy). Train on 50 example emails (25 spam, 25 ham — generate realistic examples). Implement Laplace smoothing. Classify 5 test emails. For each classification, print the log-posterior per word. Then build a Manim animation showing a single email being classified word by word, each word adding to a running log-posterior bar chart for spam vs. ham."`
- Read / check: Verify Laplace smoothing is implemented (add-1 to all word counts before normalizing). Verify the log-sum approach avoids underflow (log P(spam|words) = log P(spam) + sum of log P(word|spam)). Verify the bar chart animation grows the correct bar (spam or ham) for each word.
- Human supplies: Nothing — fully synthetic (Claude generates training examples).
- Output medium: Manim (word-by-word log-posterior update bar chart)
- The change: Remove the "naive" assumption by adding bigram features — show how accuracy changes when word pairs are considered (some improve, some don't).
- Teardown angle: The naive independence assumption is mathematically wrong but computationally efficient and surprisingly effective. Understanding why it works — even when wrong — is a lesson about when approximate Bayesian inference outperforms exact methods.
- Exclusions: Cut EM algorithm for Gaussian mixture models; cut variational inference; cut full probabilistic graphical models.
- Score: 8/10

---

## Candidate 04 — "Simulate Bayesian A/B Testing with Claude Code"
- Source: bayesian-probability-with-llms/chapters/00-frontmatter.md (scope; no chapter content yet)
- Lane: BUILD (Claude Code)
- Hook: Frequentist A/B testing gives you a p-value — which is not the probability that B is better than A. Bayesian A/B testing gives you exactly that, and Claude can compute it with a Monte Carlo simulation you can watch update in real time.
- The artifact: A Python script that runs a Bayesian A/B test: two variants with unknown conversion rates, Beta priors, observed clicks/conversions. Computes P(B > A) via Monte Carlo sampling from both posteriors. Manim animates both posterior distributions updating as observations accumulate, with P(B>A) displayed as a live number and a third panel showing the Monte Carlo samples.
- Prompt seed: `claude "Build a Bayesian A/B testing simulator in Python. Variant A has 1000 visitors, 100 conversions. Variant B has 1000 visitors, 120 conversions. Use Beta priors (Beta(1,1) for both). Compute P(B > A) by sampling 100000 times from each posterior and computing the fraction where B_sample > A_sample. Animate in Manim: two Beta distributions updating with data, P(B>A) as a live number, and a scatter plot of sampled pairs with the B>A region highlighted."`
- Read / check: Verify P(B>A) calculation: sample from Beta(1+120, 1+880) and Beta(1+100, 1+900), compute fraction where B>A. Verify the result is ~75-80% (roughly consistent with the observed difference). Verify the animation shows both distributions updating simultaneously.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (two posterior distributions + P(B>A) live counter + Monte Carlo scatter)
- The change: Add sample size sensitivity — what is P(B>A) after 100 observations, 1000, and 10000? Show that the probability converges to near 100% or falls back to 50% depending on the true difference.
- Teardown angle: The Bayesian result is a probability over outcomes, not over hypotheses. "P(B>A) = 78%" is a directly actionable number. A frequentist p-value is neither.
- Exclusions: Cut multi-armed bandit formulation; cut Thompson sampling; cut Bayesian optimization.
- Score: 8/10

---

## Candidate 05 — "Research the Base Rate Fallacy in Medical and Legal Contexts with Claude"
- Source: bayesian-probability-with-llms/chapters/00-frontmatter.md (scope; no chapter content yet)
- Lane: RESEARCH (Claude assistant)
- Hook: The prosecutor's fallacy and the base rate neglect fallacy both come from the same Bayesian error. Claude can find documented cases where the error affected legal verdicts and medical decisions, and explain the correction.
- The artifact: A sourced 3-section research brief: (1) the Sally Clark case (UK, 2003) — how base rates were ignored in the SIDS/murder prosecution, (2) HIV testing and population-level false positive rates, (3) a documented case where Bayesian correction was formally applied in a legal or medical setting. Includes 4+ verifiable citations and a one-sentence Bayesian correction for each case.
- Prompt seed: `claude "Research documented cases of the base rate fallacy in legal and medical contexts. Provide: (1) the Sally Clark conviction (UK, 2003) — what probability error was made, what the correct Bayesian analysis shows, and what the outcome was; (2) HIV testing base rate neglect — why even a 99.9% accurate test produces many false positives in low-prevalence populations; (3) a documented case where Bayesian reasoning was formally applied in court (e.g., R v T in the UK, or DNA evidence standards). Include at least 4 verifiable citations."`
- Read / check: Verify Sally Clark was convicted in 1999 (not 2003 — verify dates), released 2003. Verify the probability error involved multiplying SIDS risks without accounting for family correlation. Verify that Roy Meadow's testimony was criticized by the Royal Statistical Society. Check that all citations are verifiable.
- Human supplies: Nothing — fully researchable.
- Output medium: slate (3-case brief with citations, human fills with publicly available court document images or probability diagrams)
- The change: Add the "prosecutor's fallacy" formally — show that P(evidence | innocent) ≠ P(innocent | evidence), and demonstrate the correct Bayesian calculation that should be applied to DNA match probabilities.
- Teardown angle: The Bayesian correction is not pedantic — it has put people in prison and killed patients. The failure is systematic and predictable: experts ignore the prior.
- Exclusions: Cut full decision theory; cut utility functions; cut comparative legal system analysis.
- Score: 8/10

---

## Candidate 06 — "Build a Bayesian Network for Disease Diagnosis with Claude Code"
- Source: bayesian-probability-with-llms/chapters/00-frontmatter.md (scope; no chapter content yet)
- Lane: BUILD (Claude Code)
- Hook: A Bayesian network is a directed acyclic graph where each node is a probability conditioned on its parents — and even a 3-node network (disease → symptom1, symptom2) can demonstrate how adding symptoms updates diagnosis. Claude can build and visualize one.
- The artifact: A Python script using pgmpy (or manual conditional probability tables) that builds a 4-node Bayesian network: {flu} → {fever, cough} ← {cold} → {runny_nose}. Computes the posterior P(flu | fever=True, cough=True) and P(cold | runny_nose=True, fever=False). Manim animates belief propagation through the network as evidence is added node by node.
- Prompt seed: `claude "Build a Bayesian network in Python using pgmpy for a simple diagnostic model: nodes = {Flu (prior 0.05), Cold (prior 0.15), Fever (P=0.9 if flu, 0.1 if cold, 0.01 baseline), Cough (P=0.8 if flu, 0.6 if cold, 0.05 baseline), RunnyNose (P=0.3 if flu, 0.85 if cold, 0.05 baseline)}. Compute P(Flu | Fever=True, Cough=True) and P(Cold | RunnyNose=True). Animate belief propagation in Manim as each symptom is added."`
- Read / check: Verify pgmpy (or manual CPT) computation is setting up the tables correctly. Verify that P(Flu | Fever, Cough) is substantially higher than the prior (0.05 → should reach ~0.6+ with both symptoms). Verify Manim shows evidence flowing inward to disease nodes.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated Bayesian network belief propagation)
- The change: Add "explaining away" — show that if flu is confirmed, the probability of cold drops even if cough is present (because flu explains the cough away). This is the hallmark behavior of Bayesian networks.
- Teardown angle: The network encodes causal structure, not just correlation. Belief propagation doesn't just update — it correctly handles the explaining-away phenomenon that frequentist statistics can't express.
- Exclusions: Cut exact inference algorithms (variable elimination derivation); cut learning CPTs from data; cut dynamic Bayesian networks.
- Score: 8/10

---

## Candidate 07 — "Simulate Monte Carlo Estimation of Pi and Bayesian Parameter Recovery with Claude Code"
- Source: bayesian-probability-with-llms/chapters/00-frontmatter.md (scope; no chapter content yet)
- Lane: BUILD (Claude Code)
- Hook: Monte Carlo methods sample from distributions to compute integrals — including the integral of the posterior. Claude can demonstrate both the classic pi estimation and the connection to Bayesian posterior sampling in one script.
- The artifact: A Python script that: (1) estimates pi via Monte Carlo (dots in square vs. circle), (2) uses MCMC (Metropolis-Hastings, implemented from scratch) to sample from a posterior for a Gaussian mean given observed data. Manim animates both: dots accumulating and the pi estimate converging in one panel, MCMC chains exploring the posterior in the other.
- Prompt seed: `claude "Write two Monte Carlo demonstrations in Python: (1) Estimate pi by sampling 10000 points uniformly in a unit square and computing fraction inside the unit circle; (2) Implement Metropolis-Hastings MCMC from scratch (no pymc) to sample from the posterior P(mu | data) for a Gaussian with known sigma=1, given 20 observed data points. Animate both in Manim: pi estimation dots accumulating; MCMC chain tracing through the posterior with the true mu marked."`
- Read / check: Verify MH implementation: proposal distribution, acceptance ratio, burn-in handling. Verify the MCMC chain converges to the true posterior mean within ~1000 steps. Verify pi estimate converges toward 3.14159 with visible noise at low N and convergence at high N.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (two-panel: pi estimation + MCMC chain exploring posterior)
- The change: Add a comparison between the MCMC samples and the analytical Beta posterior from Candidate 01 — show that sampling and analytic solutions converge to the same distribution.
- Teardown angle: MCMC is how we do Bayesian inference when the posterior has no closed form — which is most of the time. The random walk isn't magic; it's a guaranteed-converging exploration algorithm.
- Exclusions: Cut Gibbs sampling; cut Hamiltonian Monte Carlo; cut variational inference comparison.
- Score: 8/10

---

## Candidate 08 — "Research the History of Bayes' Theorem and Its Delayed Acceptance with Claude"
- Source: bayesian-probability-with-llms/chapters/00-frontmatter.md (scope; no chapter content yet)
- Lane: RESEARCH (Claude assistant)
- Hook: Bayes wrote his theorem in 1763 — and it spent 200 years being dismissed as "not really probability." Claude can reconstruct the frequentist-Bayesian controversy and show why the debate was philosophical, not mathematical.
- The artifact: A sourced 4-event timeline: (1) Bayes' original 1763 paper and Price's posthumous publication, (2) Laplace's independent derivation and broader use, (3) the Fisher-vs-Jeffreys controversy (1920s-1940s), (4) the Bayesian revival (de Finetti, Savage, Cox) and modern computational Bayesian statistics. Includes 4+ verifiable citations.
- Prompt seed: `claude "Research the history of Bayes' theorem and the Bayesian-frequentist debate. Construct a sourced 4-event timeline: (1) Thomas Bayes' 1763 posthumous paper and Richard Price's role; (2) Laplace's independent derivation and use in astronomy; (3) Fisher's opposition to Bayesian priors in the 1920s-1940s, Jeffreys' defense; (4) the modern Bayesian revival — de Finetti, Savage, Cox's theorem, MCMC enabling computational Bayes. Include at least 4 verifiable citations."`
- Read / check: Verify Bayes' paper publication year (1763, read posthumously by Richard Price). Verify Laplace's independent derivation in 1774. Verify Fisher's specific objection (subjective priors are not scientific). Verify Cox's theorem year (1946). Check de Finetti's coherence argument for subjective probability.
- Human supplies: Nothing — fully researchable.
- Output medium: slate (4-event timeline, human fills with public-domain portrait images of Bayes, Laplace, Fisher)
- The change: Ask Claude to evaluate the modern consensus — is the debate settled, and if so, which "side" won? (Answer: pragmatically Bayesian, philosophically unresolved.)
- Teardown angle: The controversy was not about the math — Bayes' theorem is mathematically true. It was about whether probability can represent subjective belief. That debate shaped 200 years of statistics and still affects how science is taught.
- Exclusions: Cut full decision theory derivation; cut economic utility theory; cut all of information theory.
- Score: 7/10
