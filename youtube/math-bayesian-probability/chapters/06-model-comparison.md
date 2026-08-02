# Chapter 6 — Model Comparison

---

## Learning Objectives

By the end of this chapter you will be able to:

1. **(Apply)** Compare two statistical models using AIC and the likelihood ratio test, and interpret what the output does and does not say (Bloom: Apply)
2. **(Apply)** Compute a Bayes factor for a two-model comparison and convert it to posterior model probabilities (Bloom: Apply)
3. **(Analyze)** Explain the conceptual difference between what AIC measures — relative predictive accuracy — and what a Bayes factor measures — relative marginal likelihood — and why that distinction matters for communication (Bloom: Analyze)
4. **(Evaluate)** Assess when model comparison produces a clear answer and when it doesn't, and describe what to do in each case, including the role of model averaging and PSIS-LOO cross-validation (Bloom: Evaluate)

---

## Opening Case: The Forecast That Could Go Either Way

It is March 2020. A public health epidemiologist at a state health department is looking at 30 days of confirmed case counts for a rapidly spreading respiratory illness. The data points curve upward. She needs to tell officials which model to trust for the next 30-day forecast.

She has two candidates. Model M1 assumes linear growth: cases increase by a fixed number each day. Model M2 assumes exponential growth: cases increase by a fixed *percentage* each day. Both models fit the early data reasonably well. Both produce defensible-looking curves through the scatter.

The forecast stakes are not symmetric. If she chooses M1 and the truth is M2, she will underestimate peak case counts badly — and health systems will be unprepared. If she chooses M2 and the truth is M1, she will overestimate and cause unnecessary mobilization. Neither mistake is free.

She runs both models. Both produce a good-looking fit. She needs to choose — and she needs to tell the officials *how confident* she is in that choice.

This is a model comparison problem. And the way you answer "which model fits better" turns out to be very different from the way you answer "how confident should I be that the better-fitting model is correct?" The two questions sound similar. They are not the same question at all.

---

## The Frequentist Solution: Ranking Models

### The Likelihood Ratio Test (Nested Models)

Before reaching for AIC, let's establish what likelihood means in this context. For a statistical model, the *likelihood* of the data is the probability of observing those data points given specific parameter values. After fitting the model — choosing the parameter values that best explain the data — we call that the *maximized log-likelihood*, written $\hat{\ell}$.

When two models are *nested* — one is a special case of the other — we can use the **likelihood ratio test (LRT)**. If M1 (linear trend) has 2 parameters and M2 (exponential) has 2 parameters and neither is a restricted version of the other, they are not nested and the LRT does not apply directly. But when they are nested, the test statistic is:

$$\Lambda = -2(\hat{\ell}_{\text{restricted}} - \hat{\ell}_{\text{full}})$$

Under the null hypothesis that the restricted model is correct, $\Lambda$ follows a chi-squared distribution with degrees of freedom equal to the difference in number of parameters.

For our epidemiology case: the models are not nested (linear and exponential growth are fundamentally different functional forms), so the LRT is not appropriate here. We move to AIC.

### AIC: Balancing Fit and Complexity

The **Akaike Information Criterion** asks: which model is likely to make the best predictions on *new* data? Fitting a very complex model to the data you have will always improve in-sample fit, but a model with too many parameters overfits — it learns the noise in your training data rather than the signal.

Akaike (1974) derived a criterion from information theory — specifically from the Kullback-Leibler divergence between the true data-generating process and the fitted model. The result is remarkably simple:

$$\text{AIC} = -2\hat{\ell} + 2k$$

where $\hat{\ell}$ is the maximized log-likelihood and $k$ is the number of parameters. Lower AIC is better. The $2k$ term penalizes model complexity: each additional parameter costs 2 AIC units.

**Applying this to the epidemic data:**

Suppose the epidemiologist fits both models and finds:
- M1 (linear): $\hat{\ell}_1 = -69.15$, $k_1 = 2$, giving AIC(M1) = 142.3
- M2 (exponential): $\hat{\ell}_2 = -67.05$, $k_2 = 2$, giving AIC(M2) = 138.1

The difference is $\Delta\text{AIC} = 142.3 - 138.1 = 4.2$. The exponential model has lower AIC and is preferred.

**What ΔAIC means:** By a widely used rule of thumb (Burnham & Anderson 2002), a ΔAIC between 4 and 7 constitutes "considerably less support" for the higher-AIC model. ΔAIC > 10 is usually treated as decisive.

**What ΔAIC does not mean:** It is a ranking, not a probability. ΔAIC = 4.2 does not mean "there is an 87% probability that M2 is correct." It means "M2 is estimated to have a better balance of fit and parsimony." These are different claims, and the difference matters when you are briefing officials about uncertainty.

### Where the Frequentist Approach Strains

The epidemiologist needs to communicate two things: (1) which model to use, and (2) how confident she is. AIC handles the first question adequately. It fails the second.

"The exponential model fits better by 4.2 AIC units" is not a complete answer to "how confident are you?" The ΔAIC gives a ranking. It does not give a probability. When a health official asks "what's the chance we're wrong about exponential growth?", AIC cannot answer. The frequentist toolkit has no principled way to convert a ΔAIC into a probability that a model is correct.

There is a second limitation: when ΔAIC is small — say 1.8 instead of 4.2 — the guidance is genuinely ambiguous. Rules of thumb say "approximately equivalent." But what should the epidemiologist *do* with models she cannot rank? Frequentist model comparison gives her no principled tool for combining the two models' forecasts.

---

## The Bayesian Solution: Weighing Models

### The Bayes Factor

The Bayesian approach to model comparison asks: given the data we observed, how should we update our beliefs about which model is correct?

Define the **Bayes factor** as:

$$BF_{21} = \frac{P(\mathbf{y} \mid M_2)}{P(\mathbf{y} \mid M_1)}$$

where $P(\mathbf{y} \mid M_j)$ is the *marginal likelihood* of the data under model $j$ — the probability of the data averaged over all parameter values, weighted by the prior on those parameters. This is sometimes called the *evidence* for model $j$.

$$P(\mathbf{y} \mid M_j) = \int P(\mathbf{y} \mid \theta_j, M_j) \, P(\theta_j \mid M_j) \, d\theta_j$$

The Bayes factor is a likelihood ratio with a crucial difference: it integrates over all plausible parameter values according to the prior, rather than comparing only at the maximum-likelihood estimates. This automatic penalty for complexity — more complex models spread their prior over a larger parameter space, reducing the average likelihood — is why Bayesian model comparison does not need a separate complexity penalty like the $2k$ term in AIC.

**Interpreting the Bayes factor:** Jeffreys (1961) proposed an evidence classification that Kass and Raftery (1995) standardized:

| $BF_{21}$ | Evidence for M2 |
|---|---|
| 1–3 | Anecdotal (barely worth mentioning) |
| 3–10 | Moderate |
| 10–30 | Strong |
| 30–100 | Very strong |
| > 100 | Decisive |

For our epidemic example, suppose $BF_{21} = 8.3$. This means the data are 8.3 times more consistent with exponential growth than linear growth — moderate evidence.

**From Bayes factor to model probabilities:** If the epidemiologist assigns equal prior probability to both models ($P(M_1) = P(M_2) = 0.5$), then by Bayes' theorem:

$$P(M_2 \mid \mathbf{y}) = \frac{BF_{21} \cdot P(M_2)}{BF_{21} \cdot P(M_2) + P(M_1)} = \frac{8.3}{8.3 + 1} \approx 0.89$$

The posterior probability of the exponential model, given equal priors, is about 89%. This is a statement the epidemiologist can communicate to officials.

### Model Averaging

What should she do when model uncertainty is non-trivial? The principled Bayesian answer is **model averaging**: rather than picking one model and acting as if it were certainly correct, make predictions using a weighted combination of both models, where the weights are the posterior model probabilities.

Forecast under model averaging = $0.89 \times \hat{y}_{M_2} + 0.11 \times \hat{y}_{M_1}$

This produces a forecast that honestly reflects the remaining uncertainty about which model is true. For the epidemiologist's purposes, it also provides a natural way to construct a prediction interval that includes model uncertainty, not just parameter uncertainty within a single model.

When BF is close to 1 — say $BF_{21} = 1.5$, giving $P(M_2 \mid \mathbf{y}) \approx 0.60$ — model averaging is especially important. Reporting "the exponential model is preferred" when the data only weakly distinguish them would be overconfident.

### A Critical Caution: Prior Sensitivity [contested — see pantry]

Here is where the Bayesian approach has a genuine vulnerability, and intellectual honesty requires stating it clearly.

The Bayes factor depends not just on the observed data but on the priors placed on the *parameters within each model*. A prior that is very spread out (diffuse) penalizes complex models more than a tighter prior does. Two analysts fitting the same data with slightly different priors on model parameters can reach opposite conclusions using Bayes factors — at realistic sample sizes (n = 20–100), this is not a pathological edge case but an expected possibility. This has been formalized as the **Bayes Factor Reversal Paradox** (arXiv:2511.22152, 2025 preprint — not yet peer-reviewed at time of writing).

This prior sensitivity does not afflict AIC in the same way, because AIC uses only the maximized likelihood and does not integrate over a prior. AIC's "prior" is implicit and fixed (the penalty is $2k$ regardless of context); it cannot be made worse by the analyst's choices, but it also cannot be improved by incorporating domain knowledge.

The practical implication: if you use Bayes factors, you should always perform **prior sensitivity analysis** — check whether the conclusion changes if you use different reasonable priors. If the Bayes factor is robust across a range of prior choices, report it with confidence. If it is sensitive to prior choice, report that sensitivity explicitly.

### PSIS-LOO: A More Defensible Practical Tool

For practitioners who want Bayesian model comparison without the prior sensitivity problem, **PSIS-LOO** (Pareto-Smoothed Importance Sampling Leave-One-Out cross-validation) from Vehtari, Gelman, and Gabry (2017) offers a practical alternative.

Instead of computing the marginal likelihood (which requires integrating over the prior), PSIS-LOO estimates how well each model predicts held-out observations — using the fitted posterior, not the prior. It measures *posterior predictive* accuracy, making it less sensitive to prior specification than Bayes factors.

PSIS-LOO produces an *elpd* (expected log predictive density) score for each model. The model with higher elpd is preferred. Unlike AIC, it uses the full posterior rather than just the mode, and unlike Bayes factors, it does not require the prior to be well-specified. The `loo` package in R implements this efficiently.

The current state of the field: the Gelman-Stan community has largely moved toward PSIS-LOO as the default Bayesian model comparison tool for practical work, precisely because of the prior sensitivity issues with Bayes factors. Defenders of Bayes factors (especially in psychology, via the `BayesFactor` R package) argue that the philosophical question of which model is more probable under a prior is sometimes exactly the right question. This debate is not settled.

---

## Side-by-Side Comparison

| | Frequentist (AIC/LRT) | Bayesian (Bayes Factor) |
|---|---|---|
| Core quantity | ΔAIC = 4.2 | BF₂₁ = 8.3 |
| What it says | Exponential fits better by 4.2 units | Data are 8.3× more consistent with exponential |
| Converts to probability? | No | Yes: P(M2 \| data) ≈ 89% with equal priors |
| Model averaging | Not standard; sometimes via AIC weights | Natural: weight by posterior model probability |
| Prior required? | No — implicit flat penalty | Yes — on model parameters within each model |
| Prior sensitivity | None (penalty fixed at $2k$) | High: different priors can reverse conclusions |
| Close-call guidance | "Approximately equivalent" (ΔAIC < 4) | Probability statement; model averaging is appropriate |
| Computation | Fast, closed-form | Requires integration; PSIS-LOO as alternative |
| Field standard | Ecology, econometrics, epidemiology | Clinical trials (Bayesian), psychology (BayesFactor package) |

**Why anyone uses AIC:** It is fast, requires no prior specification, and is understood by every reviewer in ecology, epidemiology, and econometrics. For large samples with well-specified models, AIC and Bayes factors often agree on the winner. AIC is a valid choice when the communicative goal is "which model has better predictive accuracy" rather than "what is the probability that this model is correct." For the epidemiologist briefing non-technical officials, AIC's lack of a probability statement is sometimes a feature — it avoids the misuse of model probabilities that a Bayes factor can invite.

---

## Worked Example: Choosing Between Growth Models

**Situation.** An epidemiologist has 30 days of daily case counts from a novel pathogen. She is comparing M1 (linear daily increase) and M2 (exponential daily growth rate). Both models have two parameters each (intercept + slope for M1; initial level + growth rate for M2). She needs to brief public health officials in 48 hours.

**Process.**

*Step 1: Fit both models and compute AIC.*

After fitting, she finds AIC(M1) = 142.3 and AIC(M2) = 138.1, giving ΔAIC = 4.2. By the standard rule of thumb, this is "considerably less support" for M1 — but not decisive.

*Step 2: Compute the Bayes factor.*

She specifies weakly informative priors on the parameters of each model (consistent with plausible epidemic dynamics for a respiratory illness), computes the marginal likelihoods via numerical integration, and finds BF₂₁ = 8.3. Moderate evidence for M2.

*Step 3: Check prior sensitivity.*

She perturbs the priors modestly — making them slightly wider and slightly tighter. The Bayes factor ranges from 6.1 to 11.4 across these variations. The qualitative conclusion (moderate evidence for M2) is stable, though the strength of evidence varies.

*Step 4: Compute posterior model probabilities and model-averaged forecast.*

With equal prior model probabilities, P(M2 | data) ≈ 89%. She constructs a model-averaged 30-day forecast weighted by these probabilities, which shows a higher peak than M1 alone but lower than M2 alone.

*Step 5: Identify the dead end.*

She initially tried to use the likelihood ratio test. This failed because M1 and M2 are not nested — exponential growth is not a special case of linear growth. The LRT requires nested models. This is a common mistake; the fix is AIC or Bayes factors.

**Resolution and lesson:** Both AIC and the Bayes factor point to M2. For the official briefing, she reports: "The exponential model fits better by a moderate margin. We estimate approximately 89% probability that exponential growth is the correct model, though this figure depends on prior assumptions. Using a model-averaged forecast, the 30-day projection is [X] cases, with uncertainty bounds that account for residual model uncertainty."

**Limit:** Model comparison can only compare the models on the table. If neither M1 nor M2 is the true data-generating process — if, say, the true dynamics are logistic (growth with a ceiling) — both Bayes factors and AIC will select the "least wrong" model from the candidate set, not the correct model. Model comparison does not rescue you from an incomplete model space.

---

## Prompting for Implementation

### A well-formed prompt for model comparison

```
I have daily case count data for 30 days of an epidemic. I want to compare 
two models: M1 assumes a linear daily increase (y = a + b*t) and M2 assumes 
exponential growth (y = a * exp(b*t)).

Please:
1. Fit both models to the data using maximum likelihood estimation.
2. Report AIC for each model and the ΔAIC.
3. Compute the Bayes factor BF_21 using weakly informative priors on the 
   parameters (e.g., half-normal priors consistent with plausible epidemic 
   dynamics). Show the prior specification explicitly.
4. Convert the Bayes factor to posterior model probabilities assuming equal 
   prior model probabilities.
5. Construct a model-averaged 30-day forecast with 90% prediction intervals.
6. Show me what happens to the Bayes factor if you widen the priors by 2× 
   and narrow them by 0.5× (prior sensitivity check).

The data are: [paste data here]

Show the mathematical steps for each calculation, not just the code output.
Interpret each result in one sentence of plain language.
```

### What to verify

The Bayes factor requires numerical integration over the prior. LLMs can produce plausible-looking Bayes factors by using approximations that may not be accurate. Verification checks:

- The marginal likelihood for each model should be a positive number less than 1 (it is a probability density, so it can be less than 1 for continuous data). If the LLM reports values greater than 1, something is wrong.
- The Bayes factor computed via `bridgesampling` or `BayesFactor` R packages should match. Ask the LLM to show the computation method.
- The model-averaged forecast should lie *between* the individual model forecasts, not outside them.

**Aging note:** The specific R packages (`loo`, `bridgesampling`, `BayesFactor`) change their APIs. The principle — compute PSIS-LOO or Bayes factor, verify via prior sensitivity — is stable; the exact package syntax is not.

---

## Common Misconceptions

**Misconception 1: "BIC is a Bayesian model comparison method, so BIC ≈ Bayes factor."**

BIC (Schwarz 1978) is derived from a Bayesian argument and approximates twice the log Bayes factor under a specific prior called the "unit information prior." But this approximation is exact only asymptotically (as $n \to \infty$), and the unit information prior is not necessarily a reasonable prior for the problem at hand. In practice, BIC and Bayes factors can disagree substantially, especially at small samples. BIC is a frequentist-style criterion that borrows Bayesian motivation; it is not a drop-in replacement for a Bayes factor.

**Misconception 2: "A lower AIC means the model is correct."**

AIC estimates relative predictive accuracy. "Correct" is not a category AIC recognizes. If all the models in your candidate set are wrong, AIC will select the least wrong one. ΔAIC = 4.2 means the exponential model is estimated to predict new data better, not that it is the true generating process. This distinction matters especially in model-rich disciplines like ecology and econometrics, where the "true model" is always an idealization.

**Misconception 3: "Bayes factors give a probability that the model is correct, so they're more informative than AIC."**

Bayes factors convert to posterior model *probabilities* — but only conditional on the models in the comparison set and the specified priors. "P(M2 | data) = 89%" means "given that the true model is either M1 or M2 and given these priors, M2 is 89% likely." If neither M1 nor M2 is the true model, this probability is meaningless as a statement about the world. And as the Bayes Factor Reversal Paradox demonstrates, the prior sensitivity problem means two analysts can reach opposite probability conclusions from the same data. The probability output of a Bayes factor is more informative than a ranking only if the priors are well-justified.

---

## AI Wayback Machine: Hirotugu Akaike (1927–2009)

---

*Imagine you could ask a scientist the question their career was built to answer. Here is what Hirotugu Akaike might have said in 1974, just after the AIC paper appeared.*

---

Hirotugu Akaike was a Japanese statistician at the Institute of Statistical Mathematics in Tokyo. In 1974, he published a paper in *IEEE Transactions on Automatic Control* that proposed something deceptively simple: choose models not by asking "which model fits these data?" but by asking "which model would best predict new data drawn from the same process?"

The paper, "A New Look at the Statistical Model Identification" (Akaike 1974), derived the AIC criterion from information-theoretic foundations — specifically from the Kullback-Leibler divergence between the true (unknown) data-generating process and the fitted model. The $2k$ penalty emerged naturally from this derivation, not as an arbitrary regularization but as an estimate of the bias introduced by using the training data to both fit and evaluate the model.

Akaike's insight was that goodness-of-fit tests ask the wrong question. A model with more parameters will always fit better in-sample. The right question is out-of-sample prediction. This shifted model selection from a significance-testing exercise to a decision-theoretic one.

He received the Kyoto Prize in 2006 — one of Japan's highest academic honors. His criterion became foundational in ecology, epidemiology, and econometrics, often without attribution, which is probably the highest form of intellectual honor.

*Anchor for student reflection:* "You are Hirotugu Akaike in 1974, just after submitting the AIC paper. A colleague asks why you used Kullback-Leibler information loss rather than a classical goodness-of-fit test. What do you tell them?"

---

## Exercises

**Exercise 1 (Apply — both frameworks).** An ecologist is comparing two models for species abundance in forest plots: M1 (log-normal distribution) and M2 (negative binomial distribution). Using the following fit statistics from a dataset of 60 plots — M1: log-likelihood = -148.3, k = 2; M2: log-likelihood = -145.1, k = 2 — compute AIC for each model and ΔAIC. Separately, she reports BF₂₁ = 4.1. Do AIC and the Bayes factor agree on the winner? What does each approach tell you that the other doesn't?

**Exercise 2 (Analyze — close call).** In a new dataset, the same ecologist finds ΔAIC = 1.8 in favor of M2 and BF₂₁ = 2.3.

(a) What conclusion does each criterion support?

(b) Using the Jeffreys/Kass-Raftery classification, how would you characterize the strength of evidence from the Bayes factor?

(c) If you had to make a forecast for a conservation policy decision, what would you do, and why? Consider model averaging in your answer.

**Exercise 3 (Evaluate — production).** The epidemiologist from this chapter's opening case needs to brief state health officials in plain language. The analysis found ΔAIC = 4.2 and BF₂₁ = 8.3, both favoring the exponential model. Prior sensitivity analysis showed the Bayes factor ranged from 6 to 11 across reasonable priors.

Write a two-paragraph briefing note for officials who are not statisticians. The first paragraph should state what the analysis found. The second paragraph should explain what "moderate evidence" means for their decision, including what would change the conclusion. Do not use the words "AIC," "Bayes factor," or "marginal likelihood." You may use "probability" and "confidence."

---

## What Would Change My Mind

1. **If prior sensitivity turned out to be severe in practice.** If real applications regularly show Bayes factors reversing conclusions across reasonable prior choices, the claim "Bayes factors give you the probability AIC can't" would need to be qualified much more strongly than this chapter does. The 2025 arXiv preprint on the Bayes Factor Reversal Paradox is not yet peer-reviewed; if its findings hold up to scrutiny, the Bayesian model comparison toolkit needs to be presented with more caution.

2. **If PSIS-LOO became the uncontested standard.** The field is moving in this direction. If PSIS-LOO entirely displaces both AIC and Bayes factors as the practical tool of choice, this chapter's emphasis on Bayes factors as the "Bayesian counterpart to AIC" would need to be rebalanced.

3. **If model averaging became routinely practiced in frequentist workflows.** AIC-based model averaging (AIC weights) is theoretically available and is used in some fields (ecology). If it became as standard as AIC itself, the asymmetry between frequentist (ranking only) and Bayesian (natural model averaging) would be reduced.

---

## Still Puzzling

1. Bayes factors penalize complex models automatically through the prior integration — but this automatic penalty depends on how spread out the prior is. Is there a principled way to specify priors for model comparison that doesn't require domain knowledge about the parameters?

2. PSIS-LOO uses the fitted posterior rather than the prior, which makes it less sensitive to prior specification — but this means it's measuring something different from the Bayes factor. When you want to know "which model's *prior* prediction of the data is better," PSIS-LOO doesn't answer that question. Which question is the right one to ask, and does it depend on whether you're doing science or engineering?

3. AIC is derived for large samples. For very small samples (n < 30), AICc — the corrected version — is recommended. But the correction assumes a linear model. What should you use for small-sample model comparison when the model is not linear? The field does not have a clean answer.

---

## Bridge to Chapter 7

Model comparison assumes the models we are comparing were worth specifying. But where did those models come from? Every model encodes assumptions — about functional form, about error structure, about which predictors matter. In the frequentist framework, these assumptions are mostly implicit. In the Bayesian framework, they show up as priors — and so far we have used priors without asking hard questions about them.

Chapter 7 makes the prior explicit. It asks: where does your assumption come from? And it demonstrates something that should be uncomfortable: the frequentist analyses we have been running all along are not assumption-free. They too have priors. They are just not named.

---

*Sources: Akaike (1974); Schwarz (1978); Kass & Raftery (1995); Jeffreys (1961); Vehtari, Gelman & Gabry (2017); Burnham & Anderson (2002); arXiv:2511.22152 (2025 preprint — not yet peer-reviewed).*
