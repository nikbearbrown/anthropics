# Chapter 11 — Classification and Decision

---

## Learning Objectives

By the end of this chapter you will be able to:

1. **(Apply)** Fit a frequentist logistic regression model and interpret its output as a probability model that requires a threshold to produce a classification.
2. **(Apply)** Build a Bayesian logistic regression with posterior distributions over coefficients and a posterior predictive probability for each case.
3. **(Analyze)** Explain what loss function any given classification threshold implicitly assumes — and derive the optimal threshold from an explicit cost ratio.
4. **(Evaluate)** Assess the decision-theoretic implications of threshold choices under asymmetric costs, including the equity consequences when error costs differ across groups.

---

## The Problem

A consumer bank has built a logistic regression model to predict loan default. The model takes ten features — credit history, debt-to-income ratio, employment status, loan amount, and others — and outputs a number between 0 and 1: the estimated probability that this applicant will default.

A loan officer must now make a decision: above what probability does she decline the loan?

The model does not answer this question. The model outputs a probability. The decision — approve or decline — requires a threshold. And the threshold is not a statistical question. It is a question about costs.

If the bank approves a loan that defaults (false negative), it loses the outstanding balance. If the bank declines a good borrower (false positive), it loses the interest revenue and may face fair-lending scrutiny. These costs are not equal. In retail lending, the cost of approving a bad loan is typically several times the cost of declining a good one — a common rule of thumb in the industry is roughly 5:1, though the actual ratio depends on loan size, recovery expectations, and regulatory context. The specific ratio in this chapter's worked example (5:1) is illustrative.

Almost every classification model in practice sets the threshold at 0.5 by default. This threshold implies the costs are equal. They rarely are. The gap between the threshold the model is given and the threshold the decision requires is where most of the practical failures in applied classification originate.

This chapter makes the threshold choice explicit, derives the optimal threshold from the cost structure, and shows how the Bayesian logistic regression model propagates uncertainty in coefficients through to uncertainty in the optimal threshold itself.

---

## Frequentist Solution: Logistic Regression

### The Setup

**Logistic regression** models the probability that a binary outcome $Y = 1$ (default) occurs, given features $\mathbf{x}$:

$$P(Y = 1 | \mathbf{x}) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x_1 + \ldots + \beta_p x_p)}} = \text{logit}^{-1}(\mathbf{x}^T \boldsymbol{\beta})$$

The logit link function — coined by Berkson (1944) in the context of bioassay dose-response modeling — maps the linear predictor (which ranges from $-\infty$ to $+\infty$) to a probability (which must lie in [0, 1]).

Coefficients $\boldsymbol{\beta}$ are estimated by maximum likelihood: find the $\boldsymbol{\beta}$ that maximizes the probability of observing the training data. For a large, well-balanced dataset, this produces stable, interpretable estimates with asymptotically normal standard errors.

### Fitting the Model

With a training dataset of 5,000 loan applications (15% default rate), the logistic regression produces estimated coefficients, standard errors, and z-statistics. The key outputs:

```
Logistic regression results (5,000 observations, 750 defaults):
  Intercept:           −2.84  (SE 0.14)
  Debt-to-income:       1.73  (SE 0.21)   *** 
  Credit score:        −0.89  (SE 0.12)   ***
  Employment (binary):  0.43  (SE 0.18)   **
  Loan amount:          0.31  (SE 0.09)   ***
  [remaining 6 features ...]

AUC: 0.76
Log-likelihood: −1,842
```

*(Illustrative example using the structure in Berger 1985 and Wald 1950.)*

Each coefficient is a log-odds ratio. The debt-to-income coefficient of 1.73 means that a one-unit increase in debt-to-income multiplies the odds of default by $e^{1.73} \approx 5.6$. For a specific applicant, plugging in their feature values produces a probability of default.

### The ROC Curve and AUC

The **ROC curve** (Receiver Operating Characteristic, adapted from radar signal detection by Swets 1988) plots the true positive rate (sensitivity) against the false positive rate (1 − specificity) as the threshold varies continuously from 0 to 1. Walking along the curve from left to right corresponds to lowering the threshold: more applicants are flagged as potential defaulters (higher sensitivity), but more good borrowers are also incorrectly flagged (higher false positive rate).

The **AUC** (Area Under the Curve) is a threshold-independent measure of model discrimination: AUC = 0.76 means the model ranks a randomly chosen defaulter above a randomly chosen non-defaulter 76% of the time. AUC measures the model; it does not determine the threshold.

Swets (1988) established this separation explicitly: diagnostic accuracy (AUC) and decision bias (where the threshold is set) are distinct quantities. A high-AUC model with a badly chosen threshold can produce worse decisions than a lower-AUC model with a well-chosen threshold. Making threshold choice separate from model quality is not a weakness; it is a feature.

### The Default Threshold and What It Assumes

At threshold = 0.5:

```
Performance at threshold = 0.5:
  Sensitivity (true positive rate):   0.71   [71% of defaulters correctly flagged]
  Specificity (true negative rate):   0.85   [85% of good borrowers correctly approved]
  False positive rate:                0.15   [15% of good borrowers declined]
  False negative rate:                0.29   [29% of defaulters approved]
```

The threshold 0.5 minimizes total misclassifications when false positives and false negatives are equally costly. This is almost never true. In lending: a false negative (bad loan approved) costs the bank the outstanding balance. A false positive (good borrower declined) costs the bank the expected interest. If bad loans average $20,000 in losses and declined good loans average $4,000 in foregone revenue, the cost ratio is 5:1.

### Where the Frequentist Model Strains

The frequentist logistic regression does exactly what it is designed to do: estimate the probability of default for each applicant. It does this well. The gap is not in the model — it is in what happens next.

The model does not produce a decision. The threshold that converts probability to decision is imported from outside, usually as 0.5 by convention. This convention is rarely examined and almost never justified. A loan officer who sets threshold = 0.5 has implicitly decided that approving a bad loan and declining a good loan are equally costly. She has made a decision-theoretic choice without knowing she made one.

The second gap: the coefficient estimates are point estimates with standard errors, not distributions. For each applicant, the predicted probability is a point estimate — not a posterior distribution. If the model's parameters are estimated imprecisely (small dataset, rare default class, high collinearity), the prediction uncertainty is not propagated to the decision.

---

## Bayesian Solution: Logistic Regression with a Loss Function

### Bayesian Logistic Regression

The Bayesian logistic regression uses the same likelihood as the frequentist model but adds priors on the coefficients:

$$Y_i \sim \text{Bernoulli}(p_i) \qquad \text{[likelihood]}$$

$$\text{logit}(p_i) = \beta_0 + \beta_1 x_{i1} + \ldots + \beta_p x_{ip}$$

$$\beta_k \sim \text{Normal}(0, 2.5^2) \qquad \text{[weakly informative prior on each coefficient]}$$

The prior Normal(0, 2.5) on log-odds coefficients is a standard weakly informative choice (the default weakly informative prior in **rstanarm**'s `stan_glm`, with predictor autoscaling). It says: "Coefficients larger than ±5 in log-odds are implausible but possible." For the debt-to-income coefficient, this means a one-unit increase producing an odds ratio above $e^5 \approx 148$ is implausible a priori — which is reasonable.

With 5,000 observations, the posterior concentrates tightly around the likelihood maximum, and posterior means will be close to the MLE estimates. The Bayesian advantage is not in the point estimates — it is in two things:

1. **Posterior predictive probabilities:** For each applicant, the model produces a full posterior predictive distribution on their default probability, not a single number. Integrating over parameter uncertainty: $P(Y=1 | \mathbf{x}, \text{data}) = \int P(Y=1 | \mathbf{x}, \boldsymbol{\beta}) \cdot p(\boldsymbol{\beta} | \text{data}) \, d\boldsymbol{\beta}$.

2. **Propagation to the threshold:** If the optimal threshold is derived from the posterior, the uncertainty in the posterior propagates to uncertainty in the threshold itself.

### The Optimal Threshold from a Loss Function

This derivation is straightforward and worth doing from scratch.

Define:
- $c_{\text{FP}}$: cost of a false positive (declining a good borrower). Set to 1 unit.
- $c_{\text{FN}}$: cost of a false negative (approving a bad borrower). Set to 5 units (the 5:1 ratio).
- $p$: model's predicted probability of default for a given applicant.

For a new applicant, the expected cost of **approving** the loan is:

$$E[\text{cost of approve}] = p \cdot c_{\text{FN}} + (1-p) \cdot 0 = 5p$$

The expected cost of **declining** the loan is:

$$E[\text{cost of decline}] = p \cdot 0 + (1-p) \cdot c_{\text{FP}} = (1-p)$$

Decline when the expected cost of approving exceeds the expected cost of declining:

$$5p > (1-p) \implies 5p > 1 - p \implies 6p > 1 \implies p > \frac{1}{6} \approx 0.167$$

The optimal threshold is $p^* = c_{\text{FP}} / (c_{\text{FP}} + c_{\text{FN}}) = 1/(1+5) = 0.167$.

This is a two-line derivation from Wald (1950) and Berger (1985). The key insight: the optimal threshold is entirely determined by the cost ratio. Equal costs → threshold 0.5. Asymmetric costs → the threshold shifts toward the more expensive error.

At threshold = 0.167 versus 0.5:

```
Performance comparison:

                    Threshold = 0.5    Threshold = 0.167
Sensitivity:             0.71                0.91
Specificity:             0.85                0.64
False positive rate:     0.15                0.36
False negative rate:     0.29                0.09
Expected cost/100 apps:  189 units           142 units
```

*(Illustrative; derived from the logistic regression model above using the cost structure from the loan default problem.)*

The cost-optimized threshold approves fewer good borrowers (higher false positive rate) but catches more defaulters. The total expected cost is 25% lower. Whether this cost reduction justifies the reduced approval rate is a business and ethical question — not a statistical one. But the Bayesian framework makes the choice visible, auditable, and derivable from stated values rather than invisible convention.

### Posterior Uncertainty on the Threshold

Because the Bayesian model produces a posterior distribution over coefficients, and the threshold is derived from the model's predicted probabilities, the optimal threshold is itself uncertain. 

For a specific borderline applicant ($p \approx 0.2$), the posterior predictive probability has a 95% CrI of, say, [0.14, 0.28]. This means the decision for this applicant is genuinely uncertain: under some plausible parameter values she would be declined; under others she would be approved. The Bayesian model makes this ambiguity explicit rather than hiding it behind a single point estimate.

The posterior uncertainty on the threshold itself (integrating over the parameter posterior) produces something like a 95% CrI of [0.12, 0.22] for the optimal threshold — reflecting that we are not certain enough about the model's predictions to treat the threshold as a fixed rule. This uncertainty should inform how the bank audits borderline cases.

---

## Side-by-Side Comparison

| | Frequentist logistic regression | Bayesian logistic regression + loss function |
|---|---|---|
| Coefficient estimates | Point estimates (MLE) with SEs | Full posterior distributions |
| Predicted probability for applicant | Single value | Posterior predictive distribution |
| Default threshold | 0.5 by convention | Derived from explicit cost ratio: $c_{\text{FP}}/(c_{\text{FP}} + c_{\text{FN}})$ |
| What threshold 0.5 implies | Equal costs (rarely true) | Stated explicitly |
| Threshold uncertainty | Not reported | CrI from parameter posterior |
| Expected cost | Cannot be directly optimized without additional step | Minimized by construction |
| Computation | Fast (MLE) | MCMC required |
| Regulatory acceptance | Industry standard | Requires documentation of priors and loss function |

### Why Anyone Uses Frequentist Logistic Regression

Logistic regression is the industry standard for credit scoring, fraud detection, medical diagnosis, and most high-stakes binary classification. Regulators — banking regulators (FDIC, OCC, Fed), clinical trial agencies (FDA), insurers — understand its outputs. The log-odds coefficients are interpretable, auditable, and documentable in model risk management frameworks.

For large, balanced datasets where parameter uncertainty is small, Bayesian and frequentist logistic regression produce nearly identical predicted probabilities. The Bayesian approach earns its complexity cost specifically when: sample sizes are small or the default class is rare (common in fraud and rare event detection); when parameter uncertainty is large enough to affect the decision for borderline cases; or when the decision requires a full posterior predictive distribution for formal decision analysis.

The threshold-from-loss-function argument in this chapter does not require Bayesian logistic regression. A frequentist analyst can derive the same threshold (0.167) from the same 5:1 cost ratio and apply it to the MLE-estimated probability. The Bayesian model adds uncertainty quantification on top. The decision-theoretic framework — make the loss function explicit — is the core lesson, and it applies regardless of which model generates the probability.

---

## Worked Example: The 0.5 Default and What It Costs

**Situation:** A fintech startup builds its first loan-approval model. The data scientist fits a logistic regression and reports it to the product team. The product team sets the threshold at 0.5 "because that's the standard." The model goes live.

Six months later, the finance team reports unexpectedly high default rates. The data scientist is asked to investigate.

**Process:**

Step 1: Pull the prediction distribution. Of 10,000 approved loans, 1,400 have predicted default probabilities between 0.35 and 0.50 — in the range that would be declined at a threshold of 0.35, but approved at 0.5. These are the borderline approvals.

Step 2: Check default rates in this band. Of the 1,400 loans with predicted probabilities in [0.35, 0.50], 580 (41%) have defaulted in the six-month window — significantly above the 15% overall rate. The high-risk applicants in this band were being approved at 0.5.

Step 3: What threshold would the 5:1 cost ratio imply? Threshold = $1/(1+5) = 0.167$. But the finance team estimates the actual cost ratio closer to 8:1 for this loan product (higher-risk borrowers, lower recovery). Threshold = $1/(1+8) = 0.111$.

Step 4: Rerun the model with threshold = 0.111 on the training data. Sensitivity rises to 0.95; false positive rate rises to 0.49 — nearly half of good borrowers would be declined. The product team balks: too conservative.

**Dead end:** The model with the correct cost-derived threshold is too strict for the business. The investigation reveals the problem: the training data included high-risk applicants the company no longer wants to serve, which inflated the estimated default probability for borderline cases.

**Resolution:** Retrain the model on the target applicant population. The data shift reduces the predicted probability for borderline cases, and the optimal threshold produces a more balanced outcome. The lesson: threshold optimization and model training are coupled. Changing the threshold without reexamining the training distribution can produce unexpected behavior.

**Lesson:** The default threshold of 0.5 is not neutral. It is a decision with consequences. Making the cost structure explicit forces the question: are the assumed costs actually the right costs? In this case, they were not — and finding that out earlier would have prevented the defaults.

**Limit:** Deriving the optimal threshold from expected cost minimization assumes the predicted probabilities are well-calibrated (that a predicted probability of 0.3 corresponds to a 30% actual default rate). Logistic regression is generally well-calibrated with large, balanced datasets; it can be poorly calibrated for rare events or imbalanced classes. Calibration should be checked before applying decision-theoretic threshold optimization.

---

## Prompting for Implementation

### Step 1: Fit the logistic regression, both ways

Frequentist prompt:

> I have a dataset of 5,000 loan applications stored as `loans` with a binary outcome `default` (0/1) and 10 feature columns. Please fit a logistic regression using glm() in R (or sklearn LogisticRegression in Python). Report: the coefficient estimates and 95% confidence intervals, the AUC on a held-out 20% test set, and the confusion matrix at threshold 0.5. Compute the confusion matrix again at threshold 0.167.

Bayesian prompt:

> Using the same loan dataset, fit a Bayesian logistic regression using `brms` in R (or PyMC in Python). Use Normal(0, 2.5) priors on all coefficients. Run 2,000 warmup + 2,000 sampling iterations. Report: the posterior mean and 95% CrI for each coefficient, the posterior predictive default probability with 95% CrI for three representative applicants (low risk, medium risk, high risk), and the confusion matrix at threshold 0.167 using the posterior predictive probability.

### Step 2: Derive the optimal threshold

> Given: the cost of approving a defaulting loan is 5× the cost of declining a good borrower. Show the derivation of the optimal threshold from expected cost minimization. Then compute the confusion matrix and expected cost per 100 applications at threshold 0.5 and at the cost-optimal threshold. Compare.

### Step 3: Verify the result

Check:
1. The cost-optimal threshold should equal $c_{\text{FP}} / (c_{\text{FP}} + c_{\text{FN}}) = 1/(1+5) = 0.167$. If the LLM produces a different value, check its derivation.
2. At threshold 0.167, sensitivity should be higher than at 0.5 (more defaulters caught). False positive rate should also be higher (more good borrowers declined). If sensitivity drops at the lower threshold, the model has computed something incorrectly.
3. Expected cost at threshold 0.167 should be lower than at 0.5 when costs are 5:1. If not, recheck the cost calculation.

**Common LLM failure modes:**
- Computing AUC-optimal threshold rather than cost-optimal threshold. Ask explicitly for the expected-cost minimization approach.
- Applying the threshold to the training set rather than a held-out test set. Specify test set evaluation.
- Reporting accuracy (fraction correct) rather than expected cost. Accuracy is the right metric when costs are equal; expected cost is right when they are not.

**Aging note (2026):** EU AI Act provisions for high-risk AI systems (credit scoring, employment screening) took effect in 2026 and require documented threshold rationale for automated decisions. The decision-theoretic framework in this chapter provides exactly this documentation. The regulatory requirement is current as of this writing; verify implementation status before print. [AGING — verify EU AI Act enforcement timeline.]

---

## Common Misconceptions

### 1. "A more accurate model always leads to better decisions."

Not if the threshold is wrong. A model with AUC = 0.85 and threshold 0.5 can produce worse expected cost outcomes than a model with AUC = 0.76 and threshold 0.167, when the true cost ratio is 5:1. Model accuracy (AUC) and decision quality (expected cost at the right threshold) are separate quantities. Swets (1988) formalized this separation: AUC measures discrimination; the threshold determines decision bias. Both matter; they are independent.

The COMPAS recidivism algorithm provides a stark case. The algorithm has reasonable discrimination (AUC around 0.70). But its threshold choices produced false positive rates for Black defendants (40%) that were significantly higher than for white defendants (26%), documented by Angwin et al. (ProPublica 2016). The accuracy of the model and the equity of the threshold are separate problems. Chouldechova (2017) proved that when base rates differ across groups, it is mathematically impossible to simultaneously equalize false positive rates, false negative rates, and calibration — so any threshold choice implicitly trades off these criteria. Making the loss function explicit surfaces which trade-off is being made. [AGING — COMPAS facts are verified; the broader fairness literature referenced by Chouldechova 2017 is well-established but the policy recommendations are contested and evolving.]

### 2. "The threshold 0.5 is neutral or objective."

Threshold 0.5 is a decision. It minimizes total misclassifications when false positives and false negatives cost the same. For loan default: this would mean the bank considers approving a $20,000 bad loan and declining a good loan as equally bad outcomes. This is not a defensible cost structure in retail lending. There is no neutral threshold; there are only stated and unstated cost assumptions.

### 3. "Bayesian logistic regression is necessary to derive the optimal threshold."

It is not. The optimal threshold derivation — $p^* = c_{\text{FP}} / (c_{\text{FP}} + c_{\text{FN}})$ — is a decision-theoretic result that can be applied to any probability estimate, frequentist or Bayesian. The Bayesian approach adds: (a) posterior uncertainty on predicted probabilities for borderline cases, and (b) uncertainty on the threshold itself. These are valuable for borderline decisions. For clear-cut high- and low-probability cases, they matter less. The decision-theoretic framework is the core contribution; the Bayesian model is the fuller implementation.

---

## AI Wayback Machine

**Abraham Wald (1902–1950)**

In 1950, Abraham Wald published *Statistical Decision Functions*, the monograph that formalized what this chapter has been doing informally: making decisions under uncertain knowledge, given a stated loss for each type of error (Wald 1950). Wald defined loss functions, risk functions, admissible rules, and the Bayes decision rule — which minimizes expected posterior loss. The classification threshold derived earlier in this chapter is a direct application of Wald's framework.

Wald's path to this work was remarkable. Born in Cluj, Romania (then Austria-Hungary), he was one of the most mathematically talented students in Vienna in the 1930s. Jewish, he was barred from academic positions after the Nazi annexation of Austria. He emigrated to the US in 1938 and was hired by the Statistical Research Group at Columbia University, where he worked on sequential analysis and decision theory under wartime contract. His contributions to survivorship bias analysis — advising the US military to armor the parts of returning aircraft that showed no damage, because those were the parts whose damage caused planes not to return — is one of the canonical cases of Bayesian-style reasoning in applied statistics.

He died in a plane crash in India in 1950 at age 47, weeks after completing the monograph.

The loss-function framework that underlies every cost-optimal threshold in this chapter is Wald's. His work connects directly: whenever you ask "what threshold minimizes expected cost?" you are applying his 1950 framework, whether you know it or not.

Anchor prompt: *"What did Abraham Wald's 1950 statistical decision theory contribute to the question of how to set a classification threshold — and how does his concept of a loss function formalize the choice that practitioners usually leave implicit?"*

---

## Exercises

**1. (Apply)** Using the provided loan dataset (or a public credit dataset), fit both a frequentist logistic regression and a Bayesian logistic regression. At threshold 0.5: report the false positive rate, false negative rate, sensitivity, and specificity. Repeat at threshold 0.3 and 0.7. What pattern do you observe? How do the interval estimates differ between the Bayesian and frequentist models for a borderline applicant with predicted probability ≈ 0.35?

**2. (Analyze)** The bank estimates that approving a bad loan costs $20,000 in expected losses, and declining a good loan costs $4,000 in foregone interest revenue. Derive the optimal threshold from the cost ratio. Run the logistic regression model at this threshold and compute the expected cost per 100 applications. Compare to the expected cost at threshold 0.5. Write a one-paragraph memo to the loan committee explaining the difference and recommending a threshold.

**3. (Evaluate — O*NET connection)** Using the O*NET occupation dataset available at the companion website, build a classifier that predicts whether an occupation has above-median automation exposure (using the Frey & Osborne 2017 susceptibility scores as the label). Fit a logistic regression with occupation-level task and skill features as predictors.

   (a) What false positive and false negative rates result from threshold 0.5?
   (b) Frey & Osborne (2017) used threshold 0.70 to define "high-risk" occupations, finding ~47% of US employment at risk. Arntz, Gregory, & Zierahn (OECD, 2016) used a task-level analysis and found only ~9% at high risk. Apply your model at thresholds 0.50, 0.60, 0.70, and 0.80. How does the fraction of "at-risk" occupations change? What loss function does each threshold imply — what relative costs of false positive and false negative does each encode?
   (c) Write two sentences stating which threshold you would recommend and why, acknowledging the contested nature of the estimates.

**4. (Production)** Prompt an LLM to: (a) fit a Bayesian logistic regression on the loan dataset; (b) derive the optimal threshold from a 5:1 cost ratio; (c) compute the confusion matrix and expected cost at threshold 0.5 and 0.167; (d) report the posterior predictive probability with 95% CrI for three representative applicants. Verify steps (b) and (c) by hand. Report what you had to correct.

---

## What Would Change My Mind

**Frequentist logistic regression is the right tool when:**
- The dataset is large and the classes are balanced — posterior and MLE estimates are nearly identical, so the Bayesian model adds little.
- The regulatory or auditing environment requires standard logistic regression output (log-odds, coefficients), and explaining posterior distributions is not feasible.
- The threshold decision can be made adequately from the point-estimate probability, without needing to propagate parameter uncertainty.

In those cases, apply the decision-theoretic threshold derivation to the MLE probabilities, and the core lesson of this chapter is still fully implemented.

**Bayesian logistic regression earns its cost when:**
- Classes are severely imbalanced (fraud, rare disease, rare events) and the prior regularizes coefficient estimates more effectively than MLE.
- Parameter uncertainty is large enough to affect decisions for borderline cases — the posterior CrI on predicted probability for a borderline applicant would change whether you approve or decline.
- The decision requires explicit uncertainty quantification on the threshold itself (for model governance, regulatory documentation, or fairness auditing).

If evidence emerged that the calibration of Bayesian logistic regression was systematically worse than frequentist logistic regression for a given class of problems, I would update toward simpler tools for those problems.

---

## Still Puzzling

1. **Fairness and incompatible criteria.** Chouldechova (2017) proved that when base rates differ across groups, you cannot simultaneously equalize false positive rates, false negative rates, and calibration. Every threshold choice implicitly selects one fairness criterion over others. How to communicate this trade-off to decision-makers who want "the fair threshold" is an unsolved problem. The mathematics is settled; the ethics are not.

2. **Calibration as a prerequisite.** The threshold derivation assumes predicted probabilities are well-calibrated. Logistic regression is generally well-calibrated for large balanced datasets; it can be poorly calibrated for rare events, high-dimensional feature spaces, or models fit on misrepresentative training data. How to check calibration quickly and what to do when calibration is poor are open pedagogical problems at this level.

3. **The Frey-Osborne 47% vs. Arntz-Gregory-Zierahn 9% disagreement.** The two estimates disagree by a factor of 5. The difference is primarily methodological: occupation-level classification (Frey & Osborne) versus task-level analysis (Arntz et al.). The disagreement is a direct application of this chapter's threshold-sensitivity lesson — where you draw the line determines everything. Which estimate is "right" remains contested, and the chapter should not pretend otherwise.

4. **Temporal stability of classification models.** A model trained on 2023 loan data may not be well-calibrated on 2026 applicants if the population has shifted. Sequential updating (Chapter 10) applies here: as new loan outcomes arrive, the model should be retrained or updated. How frequently to update, and how to detect when calibration has drifted, are production questions this chapter does not fully address.

---

## Bridge to Chapter 12

Chapters 1 through 11 have given you both toolkits: frequentist and Bayesian, for proportions, group comparisons, regression, model selection, priors, sparse data, hierarchical structures, time series, and classification. Chapter 12 turns you loose on a real dataset of your choice. The deliverable is not a worked example — it is a comparative analysis you write, using the full toolkit, making a defensible method choice, and documenting what each approach found and where they agree or diverge.

The six questions every comparative analysis must answer are waiting. You have what you need to answer all of them.

---

*Sources: Wald (1950); Berger (1985); Berkson (1944); Swets (1988); Frey & Osborne (2017); Chouldechova (2017); Angwin et al. / ProPublica (2016); Buolamwini & Gebru (2018). Numerical examples are illustrative — labeled as such. COMPAS false positive rates are from ProPublica's published methodology; Chouldechova's mathematical incompatibility result is verified at doi:10.1089/big.2016.0047. Frey & Osborne threshold and job-at-risk estimates are documented; the 47% figure is contested — see Arntz, Gregory, & Zierahn (OECD 2016) for the task-level reanalysis [verify full OECD citation before print]. EU AI Act enforcement status: [AGING — verify before print].]*
