# Chapter 6: Weighting Methods


## TL;DR

- Here's a problem you have almost certainly thought about, even if you didn't call it a causal inference problem.
- The chapter moves through What you'll be able to do by the end of this chapter, Concept 1: The pollster's trick, applied to confounding, Polling and the Horvitz–Thompson idea, From sampling to treatment, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*A Feynman-style rewrite*

---

Here's a problem you have almost certainly thought about, even if you didn't call it a causal inference problem.

You want to know what the citizens of a city of one million people think about the mayor. You have money for a survey of a thousand people. The survey comes back: 63% approve.

Now the intern at the newspaper looks at the demographics. Your 1,000 respondents are 80% women and 20% men. The city is 50–50. Do you publish "63% approve"?

Of course you don't. You know this instinctively. If men and women have different opinions on the mayor — and they almost always do — then your sample is skewed, and the 63% figure is pulled toward the opinions of the oversampled group. You need to correct.

The correction is obvious once you say it out loud. Count the men more. Specifically, give each man a weight of about 2.5 and each woman a weight of about 0.625, so that the weighted total puts the sexes back at 50–50. Recompute the approval rate using the weights. That's the number you publish.

Survey statisticians have been doing this since before my grandmother was born. Political polling would be impossible without it. The Horvitz–Thompson estimator — the mathematical formalism for exactly this reweighting trick — was published in 1952, twenty years before anyone in medicine or economics started worrying about confounding in the modern sense.

And here is the thing I want you to carry into this chapter: the math that fixes a survey-sampling problem is the same math that fixes a confounding problem. When we adjust for confounders by weighting, we're doing the pollster's trick. The sample is skewed — not because we oversampled women, but because treated and untreated groups have different covariate distributions. We give some people higher weights so that, after weighting, the two groups look comparable. The rest of this chapter is working out what "some people" means and how much "higher" is the right answer.

If that already sounds obvious to you, good. Most of what's scary in IPTW — inverse probability of treatment weighting, the intimidating name — is actually survey sampling dressed up in health-research vocabulary. I'll show you why.

---

## What you'll be able to do by the end of this chapter

- **Explain**, in plain English, why the *inverse* of the propensity score is the right weight — not by reciting the formula, but by deriving it from the pollster's intuition
- **Compute** IPTW weights and stabilized weights for a small example and explain why stabilization reduces variance
- **Diagnose** extreme-weight problems and choose between truncation, trimming, and overlap weights for a given analysis
- **Identify** when doubly robust estimation is worth the extra modeling burden
- **Decide** whether matching or weighting is the right tool for a given applied problem, and defend the choice

**Prerequisites:** Chapter 3 (confounding, the back-door criterion). Chapter 5 (propensity scores, matching, balance diagnostics). You should know what a logistic regression does. You should be comfortable with the idea that a propensity score is a summary of how likely a person is to be treated given their covariates.

**Why this chapter matters:** Matching and weighting are the two workhorses of observational causal inference from back-door adjustment. Every applied analyst I know uses both, often on the same dataset, and the comparison between them is itself diagnostic. A student who learns only matching will be puzzled by half the applied literature. A student who learns weighting without really understanding why the weights are what they are will pick up the software default, run the analysis, and get the wrong answer without knowing it. I want to prevent both.

---

## Concept 1: The pollster's trick, applied to confounding

Let me make the connection between polling and confounding precise, because the rest of the chapter rides on it.

### Polling and the Horvitz–Thompson idea

Go back to the survey. You have 1,000 respondents; the city has 1,000,000 people. Each respondent is "standing in for" some number of actual citizens. In a simple random sample, each respondent stands in for 1,000 people — the city divided by the sample. They each get weight 1,000, or equivalently weight 1 scaled to a common factor; the scaling doesn't change anything.

But your sample isn't simple random. It's 80% women, 20% men, while the city is 50–50. So among your 800 female respondents, each stands in for 500,000 / 800 = 625 female citizens. Among your 200 male respondents, each stands in for 500,000 / 200 = 2,500 male citizens.

Men are more valuable. Each male respondent represents more people than each female respondent does. Therefore: weight each respondent by how many citizens they represent. Recompute the approval rate using those weights.

Here's the Horvitz–Thompson restatement of that idea. The weight assigned to each person is the inverse of that person's probability of being sampled. A woman has probability 800/500,000 = 0.0016 of being sampled. Her weight is 1/0.0016 = 625. A man has probability 200/500,000 = 0.0004 of being sampled. His weight is 1/0.0004 = 2,500.

Notice what happened. The weights are the inverse of the sampling probabilities, and the people with low sampling probability get high weights — exactly because they are rare in the sample and need to be counted more to represent the underlying population.

**This is the whole idea.** Everything else in this chapter is a variation on it.

### From sampling to treatment

Now the causal inference version. Instead of asking "who got sampled?" we ask "who got treated?"

Suppose we have a population of people, and some of them receive a treatment and others don't. Treatment is not assigned randomly. It's correlated with covariates X — age, sex, income, prior health — that also affect the outcome Y. This is confounding.

For each person, we can compute the probability they received the treatment they actually received, given their covariates. This is the propensity score. Call it e(X) for short, the probability that a person with covariates X was treated.

Now apply the Horvitz–Thompson logic. A treated person with propensity score 0.2 had a 20% chance of being treated. They are rare among the treated — only 20% of people with their X values were treated, and this person is one of those 20%. To make the treated group representative of the full population, this person needs to be counted more. Their weight should be 1/0.2 = 5.

A treated person with propensity score 0.8 is common among the treated — 80% of people with their X values were treated, and this person is one of those 80%. They don't need to be upweighted much. Their weight is 1/0.8 = 1.25.

Symmetrically, for controls: a control with propensity score 0.8 had a 20% chance of being a control (probability not-treated = 1 - 0.8 = 0.2). They are rare among controls. Weight: 1/0.2 = 5. A control with propensity score 0.2 is common among controls. Weight: 1/0.8 = 1.25.

If you apply these weights to every person in the dataset and recompute treated-vs-control averages, you get a weighted estimate that, under the usual assumptions (no unmeasured confounding, correct propensity score model, positivity), is an unbiased estimate of the average causal effect.

**That's IPTW.** Inverse probability of treatment weighting. The weight for each person is the inverse of their probability of receiving the treatment they actually received. Because each person's weight is chosen to make them representative of the full population — not just of their own treatment group — the weighted analysis behaves like an analysis from a randomized trial.

### Where I had to stop and think

When I first learned IPTW, the inverse formula felt arbitrary. Why one over e(X)? Why not some other function?

It felt arbitrary because I hadn't made the Horvitz–Thompson connection. The inverse shows up because we're asking a specific question: "given that this person was treated, how many people with their covariates should they count for?" The answer is one divided by the fraction of such people who were treated. If 20% of people with X were treated, each treated person with X stands in for 5 such people. One over 0.2 is five.

Once I saw the formula as a restatement of "count the rare ones more," it stopped feeling arbitrary and started feeling inevitable. This is a pattern I want you to watch for throughout the rest of this book: techniques that look strange usually look strange because they are being taught as formulas instead of as solutions to specific problems. Find the problem they solve and the formula becomes obvious.

### Worked example 1: computing weights by hand

Let me walk through the arithmetic on a small dataset so you can see the mechanics in full.

Suppose I have ten people. Five are treated, five are not. I've fit a propensity score model and each person has a propensity score: the model's estimate of how likely they were to be treated, given their covariates.

| Person | Treated? | e(X) | Weight |
|--------|---------|------|--------|
| 1 | Yes | 0.80 | 1 / 0.80 = 1.25 |
| 2 | Yes | 0.70 | 1 / 0.70 = 1.43 |
| 3 | Yes | 0.50 | 1 / 0.50 = 2.00 |
| 4 | Yes | 0.30 | 1 / 0.30 = 3.33 |
| 5 | Yes | 0.20 | 1 / 0.20 = 5.00 |
| 6 | No | 0.80 | 1 / 0.20 = 5.00 |
| 7 | No | 0.60 | 1 / 0.40 = 2.50 |
| 8 | No | 0.40 | 1 / 0.60 = 1.67 |
| 9 | No | 0.30 | 1 / 0.70 = 1.43 |
| 10 | No | 0.20 | 1 / 0.80 = 1.25 |

**Step 1: What's going on in the treated group?** Person 5 had a propensity score of 0.20 — meaning only 20% of people with their covariates were treated. Person 5 is a weird person to find in the treated group. They get weight 5, so they count as five people. This upweights them to balance the fact that they represent a covariate region where most people are controls.

**Step 2: What's going on in the control group?** Person 6 had a propensity score of 0.80 — they looked like someone who should have been treated, but wasn't. Rare. Weight 5. Similarly upweighted to balance the fact that their covariate region is mostly treated.

**Step 3: Check the total weights.** Treated total: 1.25 + 1.43 + 2.00 + 3.33 + 5.00 = 13.01. Control total: 5.00 + 2.50 + 1.67 + 1.43 + 1.25 = 11.85. Close to equal, not exactly. In a larger dataset with a correctly specified propensity score model, the weighted totals in the treated and control groups will be approximately equal to the sample size, and the weighted distributions of covariates will match.

**Step 4: Intuition check.** The people with the most extreme weights — persons 5 and 6 — are the ones whose treatment status was most surprising given their covariates. They are the "informative" observations, in a sense: they carry most of the information about what happens when someone of their type is treated vs. not treated. The weighting procedure recognizes this and gives them more influence.

**The general lesson:** IPTW is not equalizing anything. It's redistributing information. People who are well-represented in their treatment group (common propensity scores) get low weights. People who are rare in their treatment group get high weights. The weighted sample, on average, looks like the full covariate distribution — because the rare observations have been promoted to represent the regions of covariate space where their treatment is underrepresented.

### Common mistakes with Concept 1

Two errors I see repeatedly.

The first error is treating the weight as a scaling factor for the outcome rather than a representation factor for the person. Students sometimes think "weight 5 means multiply their outcome by 5." That's not what's happening. It means "this person stands in for five people." The distinction matters because it keeps the interpretation anchored in the counting intuition rather than in dimensionless math.

The second error is forgetting that the propensity score in the denominator is always the probability of the *observed* treatment, not the probability of being treated. For a control, you use 1 − e(X), not e(X). Students who sleepwalk through the formula sometimes divide controls by e(X) and produce nonsense. Always ask yourself: what was the probability of what actually happened? That's what goes in the denominator.

---

## Concept 2: IPTW in practice — stabilization and extreme weights

Concept 1 gave you the weighting idea. Concept 2 is where the idea meets reality, and reality makes trouble.

### Stabilized weights

The basic IPTW formula has a practical problem that shows up as soon as you use it on real data. The weights can get very large, and a small number of people end up dominating the analysis.

The worst cases are when some propensity scores are close to 0 or 1. A person with e(X) = 0.01 who was treated gets a weight of 100. One such person in a sample of a thousand is doing 10% of the work of the analysis. Their outcome, whatever it is, has enormous influence on the estimate. If that outcome is noisy, the estimate is noisy. If they happen to be an unusual person for reasons the covariates don't capture, the estimate is biased toward them.

The variance of an IPTW estimate can blow up even when the propensity score model is correctly specified, simply because a few weights are very large. Stabilization addresses this.

**Stabilized weights** rescale the IPTW weights by multiplying by the marginal treatment probability. For a treated person, the stabilized weight is:

<!-- LATEX: sw_i = P(T=1) / P(T=1 | X_i) -->

```
stabilized weight (treated) = P(T=1) / e(X_i)
```

For a control, it's:

<!-- LATEX: sw_i = P(T=0) / P(T=0 | X_i) -->

```
stabilized weight (control) = P(T=0) / (1 - e(X_i))
```

Where P(T=1) and P(T=0) are the unconditional (marginal) probabilities of treatment and no treatment in the sample — just the simple fraction treated and the fraction not treated.

Here's what stabilization is doing. In the original IPTW, a person with propensity score equal to the sample average gets a weight that's not 1 — it's 1 divided by that average, which could be anything. With stabilized weights, a person with propensity score equal to the sample average gets a weight of exactly 1. They're exactly where they "should" be, and they don't need to be reweighted. Only the people whose propensity scores deviate from the average get weights different from 1.

The practical effect is that stabilized weights center around 1 and have much smaller variance than raw IPTW weights. The estimate is the same in expectation — stabilization doesn't introduce bias when the propensity model is correct — but the standard errors are smaller and the analysis is more stable.

Stabilized weights are the default in modern applied work. If you see a published IPTW analysis, it almost certainly uses stabilized weights, whether or not the paper says so.

### Worked example 2: stabilizing the weights from Example 1

Return to my ten-person example. The marginal treatment probability is 5/10 = 0.50. The marginal probability of no treatment is also 0.50. So:

Stabilized weight for a treated person = 0.50 / e(X).
Stabilized weight for a control = 0.50 / (1 − e(X)).

| Person | Treated? | e(X) | Raw weight | Stabilized weight |
|--------|---------|------|------------|-------------------|
| 1 | Yes | 0.80 | 1.25 | 0.625 |
| 2 | Yes | 0.70 | 1.43 | 0.714 |
| 3 | Yes | 0.50 | 2.00 | 1.000 |
| 4 | Yes | 0.30 | 3.33 | 1.667 |
| 5 | Yes | 0.20 | 5.00 | 2.500 |
| 6 | No | 0.80 | 5.00 | 2.500 |
| 7 | No | 0.60 | 2.50 | 1.250 |
| 8 | No | 0.40 | 1.67 | 0.833 |
| 9 | No | 0.30 | 1.43 | 0.714 |
| 10 | No | 0.20 | 1.25 | 0.625 |

Notice what stabilization did. The raw weights ranged from 1.25 to 5.00, a factor of 4 between the smallest and largest. The stabilized weights range from 0.625 to 2.5, a factor of 4 also — the ratio is the same — but they're centered around 1 instead of around something arbitrary. The sum of stabilized weights is approximately equal to the sample size, which is convenient for standard error calculations.

In a larger dataset with more extreme propensity scores, the benefit of stabilization is more dramatic. Raw weights of 50 or 100 become stabilized weights of 25 or 50 — still large, but less catastrophic for the variance.

### The extreme weights problem

Stabilization helps. It does not solve. When a few propensity scores are genuinely near 0 or 1, even the stabilized weights are large, and those few observations dominate.

This is the single biggest practical problem with weighting methods, and it deserves more attention than the clean textbook account usually gives it.

The issue connects to the **positivity assumption**, one of the three foundational assumptions of observational causal inference (alongside ignorability and consistency). Positivity says that every person in the population has some positive probability of receiving each treatment. Formally: 0 < e(X) < 1 for all X in the population.

Why does positivity matter? Because if there's some combination of covariates for which literally everyone is treated, we have no untreated people with those covariates to compare against. We cannot estimate the causal effect of treatment on people like that — we have no counterfactual. The weighting procedure is trying to do something impossible, and it shows that by blowing up.

When positivity is strictly violated — when e(X) = 0 or e(X) = 1 exactly for some covariate combinations — the weights are infinite or undefined. The software will typically report an error, or quietly produce garbage. When positivity is *nearly* violated — e(X) = 0.02, say — the weights are large but finite, the software runs without complaint, and the analysis produces a confidence interval that looks narrow but is actually driven by a handful of observations.

**The subtle failure mode is the scary one.** A correctly coded IPTW analysis on a dataset with near-positivity-violations will produce an estimate with a plausible-looking standard error and no error messages. Nothing warns you. You have to check.

### Three responses to extreme weights

The field has developed three main responses to extreme weights, each with a different trade-off.

**Truncation** caps the weights at some maximum. A common choice is to cap at the 99th percentile of the weight distribution — anything above that gets replaced with the cap value. Truncation introduces a small amount of bias (the true weighted estimate uses the uncapped weights) in exchange for a large reduction in variance. For most applied purposes, the bias is small and the variance reduction is worth it.

**Trimming** is more aggressive. Observations with propensity scores outside some range — say, below 0.05 or above 0.95 — are dropped from the analysis entirely. This is the weighting analog of caliper matching from Chapter 5. The trade-off is representativeness: you're no longer estimating the effect for the full population but for the subpopulation whose covariates leave them with some meaningful chance of either treatment. Often this subpopulation is the more scientifically interesting one — the people for whom the treatment decision is actually a live question — but you need to report the trimming and say so.

**Overlap weights** are a more recent alternative from Li, Morgan, and Zaslavsky (2018). Instead of weighting by 1/e(X) or its stabilized variant, weight each person by e(X)(1 − e(X)). This weight is maximized at e(X) = 0.5 and approaches zero as e(X) approaches 0 or 1. Extreme observations are smoothly downweighted rather than cut off abruptly. Overlap weights target a subtly different causal estimand — the average treatment effect among the "overlap population," those whose covariates leave them with genuine treatment ambiguity — but they handle extreme propensity scores beautifully without an arbitrary cutoff.

### Design philosophy detour: three tools, three priorities

Truncation, trimming, and overlap weights are three different solutions to the same problem, and the choice between them is a value judgment.

Truncation says: keep the population, accept a little bias for lower variance. It optimizes for generalizability at the cost of introducing a known bias.

Trimming says: redefine the population to the one where the analysis actually works, and be honest about the restriction. It optimizes for valid inference on a subset at the cost of external validity.

Overlap weights say: the population whose covariates make treatment a genuine choice is the scientifically interesting population; target the effect there and use a weight scheme that makes this explicit. It optimizes for a well-defined estimand with good statistical properties, at the cost of answering a slightly different question than you may have started with.

None of these is right for every problem. MKBHD-style, I'd say the field is still working through the trade-off — truncation is the oldest and most common, but overlap weights are clearly in ascent, especially in methodological papers. A mature analyst picks one based on the research question, reports it transparently, and runs sensitivity analyses against the others.

### Balance diagnostics for weighting

Whatever weights you use, you have to check whether they actually produced balance. This is the same discipline as in Chapter 5's matching.

Compute the weighted standardized mean difference (SMD) for every covariate. The weighted treated-group mean minus the weighted control-group mean, divided by the pooled weighted standard deviation. Target: |SMD| < 0.1 on every covariate. If any covariates fail this test, the propensity score model is misspecified with respect to those variables — add them back, add interactions, add polynomial terms. Refit. Check again.

**The order of operations matters.** Iterate on the propensity score model until balance is achieved. Do not look at the outcome during iteration. If you adjust your propensity score model based on what it does to the estimated treatment effect, you are no longer doing causal inference; you are doing specification search, and your p-values are meaningless. Balance is checked first, outcome last, and not the other way around.

---

## Concept 3: Doubly robust estimation — two shots at the target

So far, everything depends on getting one model right: the propensity score model. If the propensity score is wrong, the weights are wrong, and the estimate is biased.

This is uncomfortable. Propensity score models are statistical models fit to data; they're never exactly right. Usually they're approximately right, and approximately right is good enough — but "approximately" is doing a lot of work, and in a problem where the wrong answer confidently reported is the main hazard, we'd like more insurance.

**Doubly robust estimation** is that insurance. The idea is clever enough that I want to motivate it before giving you the machinery.

### The motivating idea

Causal inference from observational data requires a model somewhere. You cannot escape modeling. The question is just which part of the problem you model.

- **Regression adjustment** (Chapter 4) models the outcome: E[Y | T, X]. Given the outcome model, you can predict what each person's outcome would have been under each treatment and average appropriately.

- **Propensity score methods** (Chapter 5 and this chapter) model the treatment: e(X) = P(T=1 | X). Given the propensity score, you can match or weight to remove the confounding effect of X.

Each of these relies on a correctly specified model. Each is biased if its model is wrong.

Now here's the insight: suppose I use *both*. Suppose I fit both an outcome model and a propensity score model, and I combine them in a specific way. Can I arrange things so that, if *either* model is correct, I get the right answer?

The answer is yes. This is the doubly robust property. Design an estimator that gives the right answer whenever at least one of the two models is correctly specified — even if the other is wrong.

Why this is so valuable: you get two independent shots at specifying the problem. If the true outcome relationship is some weird thing I can't quite capture with my outcome model, but my propensity score model is OK, the doubly robust estimate is still unbiased. If instead the propensity score model is wrong but the outcome model is right, still unbiased. Only if both models are wrong does the estimator fail. Two protections instead of one.

### Augmented IPW (AIPW)

The most common doubly robust estimator is **augmented inverse probability weighting**, or AIPW. The intuition: start with the IPTW estimate and add a correction term that uses the outcome model.

<!-- LATEX: 
AIPW estimator: 
τ̂ = (1/n) Σ [ T_i (Y_i - m̂₁(X_i)) / ê(X_i) - (1 - T_i)(Y_i - m̂₀(X_i)) / (1 - ê(X_i)) + m̂₁(X_i) - m̂₀(X_i) ]

where m̂₁(X) is the fitted outcome model for treated, m̂₀(X) is the fitted outcome model for controls, and ê(X) is the fitted propensity score.
-->

I won't put the full formula here, because the mechanics are not what I want you to carry away. The structure is what matters, and I can describe it in English:

- Start with the IPTW estimate, which weights observed outcomes by the inverse propensity score.
- For each person, subtract the outcome model's prediction for their observed treatment. This "residualizes" the IPTW term — if the outcome model is right, the residual is zero in expectation, and the IPTW term contributes nothing.
- Add the direct outcome-model estimate, which plugs in fitted values for both treatments and takes the difference.

If the outcome model is right, the IPTW term vanishes (in expectation) and the estimate reduces to the outcome-model estimate — correct. If the outcome model is wrong but the propensity score is right, the IPTW term handles the confounding and the outcome-model term is just an approximation that doesn't hurt — correct. If both are wrong, nothing saves you.

The practical effect: AIPW estimators have wider applicability than either IPTW or outcome regression alone, at the cost of requiring two models instead of one. In software, this is usually a few extra lines of code.

Doubly robust methods have become the default in modern causal inference research. Most serious applied analyses either use AIPW directly or report AIPW results alongside IPTW and regression as a robustness check. If three different methods give three different answers, you've learned something important about specification sensitivity. If they agree, you've earned some confidence.

### Double machine learning — and what it is not

There's a newer framework that extends the doubly robust idea by allowing flexible machine-learning models for both the outcome and the propensity score. It's called **double machine learning**, or DML, and it was developed by Victor Chernozhukov and colleagues in a sequence of papers starting around 2016.

The problem DML solves: standard causal inference methods have used parametric models (logistic regression for the propensity score, linear regression for the outcome) because those models give you valid standard errors. Modern ML methods (random forests, gradient boosting, neural nets) give you much better predictions in high-dimensional or nonlinear settings — but they don't come with valid inference. Use a random forest for the propensity score, plug the predictions into IPTW, and the resulting confidence interval is unreliable.

DML fixes this through two specific tricks: *Neyman orthogonalization* (a mathematical trick that makes the causal estimate insensitive to small errors in the ML models) and *cross-fitting* (a sample-splitting procedure that avoids overfitting bias). The combination lets you use complex ML models for the nuisance functions while still getting valid confidence intervals for the causal parameter of interest.

**What DML is not:** despite the name and the marketing, DML does not "learn causal structure from data." It does not discover what causes what. It does not reduce the need for a causal diagram or an identification strategy. It is a method for estimating the nuisance parameters in a causal analysis that is still specified entirely by the human analyst. The analyst brings the diagram, the identification argument, the choice of treatment, outcome, and confounders. ML provides flexible estimation of the high-dimensional regression functions, nothing more.

I flag this because DML and related methods are often sold as "Causal AI," which is a poor description and will mislead you about what the methods do. Chapter 9 will return to the terminology problem in more depth. For now: DML is a useful extension of the doubly robust framework for settings with high-dimensional or complex covariates. It is not a shortcut around causal reasoning.

### Common mistakes with Concept 3

Two errors.

First: assuming doubly robust means "robust to any specification problem." It does not. Doubly robust means "robust to misspecification of *one* of the two models, but not both." If your propensity score model misses an important confounder and your outcome model also misses that confounder, double robustness does not save you. No method can — you're missing information that your models need, and no combination of those models can make it up.

Second: using ML methods for the nuisance parameters without cross-fitting or orthogonalization. A random forest propensity score plugged into plain IPTW will give you wildly invalid standard errors. If you want ML flexibility, use the full DML procedure, not just the first piece.

---

## Integration: the Right Heart Catheterization study

Let me show you all three concepts operating together on a real example.

In the 1990s, a team led by Connors studied the Right Heart Catheterization procedure — an invasive diagnostic test in which a thin tube is threaded into a patient's heart to measure pressures directly. RHC was a widely used tool in intensive care units at the time, and the clinical community had substantial faith in its usefulness.

Connors and colleagues studied about 5,700 critically ill patients in five hospitals. About 2,200 received RHC in the first 24 hours of ICU admission; the rest did not. The question: did RHC improve survival?

**The raw comparison is terrible.** Patients who got RHC had 30-day mortality rates *higher* than patients who didn't — by several percentage points. Naively, this suggests the procedure was killing people. But the raw comparison is obviously contaminated: physicians selected sicker patients for RHC. The treatment and control groups were not comparable on baseline health.

**Concept 1 applied.** The dataset contains 50 pre-treatment covariates — demographics, physiological measurements, diagnosis codes, lab values, comorbidities. Fit a logistic regression predicting RHC from these covariates. Compute propensity scores. Compute stabilized IPTW weights. Now the treated and control groups have, approximately, the same covariate distributions. The weighted comparison of mortality rates should reflect the effect of RHC, not the underlying severity difference.

**Concept 2 applied.** Some of the propensity scores are extreme. A handful of patients have e(X) near 0.95 — the model says they were almost certain to receive RHC. Their weights as controls would be 1/(1 - 0.95) = 20, huge. Check the weight distribution. Consider truncation at the 99th percentile, or trimming at e(X) ∈ [0.05, 0.95], or overlap weights. Run the analysis multiple ways. Report what you find.

**Concept 3 applied.** Fit an outcome model for 30-day mortality regressed on treatment and all 50 covariates. Combine with the propensity score through AIPW. Now you have doubly robust protection: if either the propensity score model or the outcome model is approximately correct, the estimate is approximately right.

**Result.** Multiple published analyses of the RHC data, using IPTW, matching, AIPW, and modern ML-based approaches, converge on a similar finding. After adjustment, RHC patients still show somewhat higher mortality than non-RHC patients, though the gap is much smaller than in the raw data. The estimated effect is harmful, but modest.

**Is this causal?** Probably, with caveats. The 50 covariates capture much of the selection on severity but not all of it. Physicians likely have clinical intuitions about patient status that are not captured by any recorded variable. If RHC is selected for patients who are sicker in ways the data miss, the residual difference is still confounded.

Sensitivity analyses — which I'll teach you more formally in a later chapter — suggest that unmeasured confounders of modest strength cannot explain the full result, but very strong unmeasured confounders could. The evidence is that RHC was, on average, harmful rather than helpful in this population. This was a surprise to the clinical community at the time. RHC use has declined substantially in the decades since, partly in response to this analysis.

**The integrated point:** The analysis needed every one of the three concepts from this chapter. Concept 1 gave the basic weighting framework. Concept 2 handled the extreme-weight problem that would otherwise have destabilized the estimate. Concept 3 provided the doubly robust check that made the finding hold up under alternative specifications. Take away any of the three and the analysis is weaker.

### Weighting vs. matching: choosing between siblings

You now know enough to answer a practical question: for a given applied problem, should you use matching (Chapter 5) or weighting (this chapter)?

They are siblings. Both are methods for back-door adjustment using the propensity score. Both rest on the same core assumption: no unmeasured confounding. Both are biased if the propensity score model is wrong. The choice between them is about which trade-offs you prefer.

**Use matching when:** the control pool is much larger than the treated pool; you need a transparent analysis that a skeptic can audit pair-by-pair; the treatment is binary and the covariates have adequate overlap; individual comparisons matter more than efficient aggregate estimation.

**Use weighting when:** data is scarce and you can't afford to discard controls; the treatment is continuous or time-varying; you want to use doubly robust or DML methods (which are formulated in the weighting framework); your propensity score model is trustworthy because the covariate space is well-understood.

**Use both when:** the analysis is important enough to want triangulation, and you have the time to run both and compare. Agreement across methods is evidence of robustness. Disagreement is diagnostic — usually a signal that the propensity score model is fragile or that extreme observations are doing different things under different methods. In either case you've learned something that a single method would have hidden.

The right answer on any given applied problem is often "both, and report both." This is more work, but it's the difference between an analysis that claims robustness and an analysis that demonstrates it.

---

## A note about AI

Weighting methods (IPW, marginal structural models) extend matching to time-varying treatments. They also extend the failure modes — when positivity fails, weights blow up and the analyst's certainty does not.

Where the model genuinely helps: explaining the framework, producing the canonical worked examples, and naming the diagnostic checks (weight distribution, effective sample size, positivity).

Where the model does damage: declaring positivity satisfied in your data. The check is empirical and the data is yours; the model has not seen it.

The rule: framework from the model; positivity check from your data.

---

## Exercises

These are graduated. Start with the warm-ups. The synthesis and challenge exercises assume you've actually worked through the earlier ones — don't skip.

### Warm-up: weight computation

**Exercise 6.1** *(Objective: compute IPTW weights and stabilized weights)* Consider the following five people. Compute the raw IPTW weight and the stabilized IPTW weight for each. The marginal treatment probability is 0.4.

| Person | Treated? | e(X) |
|--------|---------|------|
| A | Yes | 0.6 |
| B | Yes | 0.2 |
| C | No | 0.5 |
| D | No | 0.8 |
| E | No | 0.1 |

For each person, briefly state which direction the stabilization moved the weight relative to the raw version, and why.

**Exercise 6.2** *(Objective: recognize the consequences of extreme propensity scores)* Suppose a dataset of 1,000 people has propensity scores ranging from 0.01 to 0.99. One treated person has e(X) = 0.02; one control has e(X) = 0.98. Compute the raw IPTW weights for these two people. Suppose their outcomes are extreme values — the treated person has an unusually good outcome, the control an unusually bad one. Explain, in one paragraph, how much influence these two people will have on the IPTW estimate relative to a typical person with e(X) near 0.5, and why this is a problem even if the propensity score model is correctly specified.

### Application: reasoning through an analysis

**Exercise 6.3** *(Objective: choose among truncation, trimming, and overlap weights)* You are analyzing the effect of a job training program on earnings using IPTW. After fitting your propensity score model, you discover that about 3% of your sample has extreme propensity scores (below 0.05 or above 0.95). The research question is framed as "what is the effect of the program on the full applicant pool?"

a. Would you choose truncation, trimming, or overlap weights for this analysis? Defend your choice in one paragraph.

b. Suppose instead the research question were "what is the effect of the program on the population for whom the training decision is actually a live question?" How, if at all, does your answer to (a) change? Why?

**Exercise 6.4** *(Objective: identify the failure mode of a weighting analysis)* A colleague runs an IPTW analysis on an observational dataset of hospital patients. They report a large causal effect with a narrow confidence interval. You notice the following in their diagnostics:

1. 2% of their sample has propensity scores below 0.02.
2. The weighted SMD on one important covariate is 0.18.
3. They did not report whether weights are stabilized or truncated.

For each of these three observations, state what it tells you about the analysis and what you would ask them to do before you trust the result.

### Synthesis: reading a real analysis

**Exercise 6.5** *(Objective: integrate all three concepts to evaluate a published weighting analysis)* Find a published paper in your field that uses IPTW or a doubly robust method. (If you don't have a field, try *American Journal of Epidemiology* or *Journal of Causal Inference*.) Answer the following.

a. What is the treatment, outcome, and target population of the analysis?
b. What covariates are in the propensity score model? Do they seem to cover the main confounders you would worry about?
c. What weighting method did the authors use? Stabilized? Truncated? Overlap? Did they report why?
d. What balance diagnostics did they report? Do the results suggest the weighting achieved balance?
e. Did they use a doubly robust method or just IPTW? If just IPTW, does their analysis seem sensitive to propensity score misspecification?
f. On a scale from "confidently causal" to "associational dressed up as causal," where would you place this analysis, and why?

Write this up in 600 words or less.

### Challenge: design against the weakness

**Exercise 6.6** *(Objective: design a sensitivity analysis)* IPTW produces biased estimates when important confounders are missing from the propensity score model. Design a sensitivity analysis that a researcher could use to quantify how strong an unmeasured confounder would need to be to explain away an observed IPTW estimate. Your answer should describe (a) what inputs the researcher would need to provide, (b) what the sensitivity analysis would output, and (c) how the researcher should interpret the output.

You are not required to derive a closed-form formula. A conceptual design, explained in prose, is fine. If you have seen the Rosenbaum bounds, the E-value approach, or similar methods in the literature, you may draw on them — but explain in your own words.

**Exercise 6.7** *(Objective: extend the framework to a setting not covered in the chapter)* I've mostly talked about binary treatments. IPTW generalizes cleanly to continuous treatments using a *generalized propensity score*, which is a conditional density rather than a conditional probability.

a. Write down, in words or math, what the generalized propensity score would be for a continuous treatment.

b. Describe how you would compute weights in the continuous-treatment case.

c. Explain one practical complication that arises with continuous treatments that does not arise with binary treatments, and sketch how you would address it.

*(This exercise has no single right answer. It is testing whether you can extend the framework yourself. If it feels hard, that's the correct feeling — you should be at the edge of what you can do on your own. If it feels impossible, re-read Concept 1 and try again.)*

---

## Chapter summary

You came into this chapter knowing about matching. You're leaving it, I hope, with a sibling technique in hand and a better sense of when to reach for each.

**The one idea from this chapter that matters most.** IPTW is not a new invention of causal inference. It is the survey statistician's trick, applied to confounders instead of sampling probabilities. The inverse probability weight is doing the same job Horvitz and Thompson gave it in 1952: count each observation by how many people with their covariates they are standing in for. If you carry one thing forward, carry this. The formula feels arbitrary until you see it as a solution to the pollster's problem; after that it feels inevitable.

**The common mistake to watch for.** Running an IPTW analysis without checking the weight distribution. The software will happily produce an estimate and a confidence interval even when a handful of observations with enormous weights are driving everything. The estimate will look fine. The confidence interval will look narrow. Nothing will warn you. You have to plot the weights, look at the tails, and decide whether to truncate, trim, or switch to overlap weights. Skipping this step is the single fastest way to get a confident wrong answer out of an IPTW analysis.

**What you should be able to teach someone else.** The Feynman test. Can you explain to a colleague, in a minute, why the inverse of the propensity score is the right weight? If you can — without reciting the formula, starting instead from "imagine you're polling a city" — you have the idea. If you can't, go back to Concept 1 and read it again. The pollster's intuition is the whole chapter in miniature.

**What you can now do that you couldn't before.** You can compute IPTW weights, stabilize them, diagnose extreme-weight problems, and choose among the three standard remedies. You can read a weighting analysis critically — checking the propensity score model, the balance diagnostics, the weight distribution, the specification robustness. You can explain why doubly robust methods provide insurance against model misspecification and when that insurance is worth the extra modeling. You can choose between matching and weighting for a given applied problem, and defend the choice.

Those are real capabilities. You won't run your first weighting analysis without help — there are software details and diagnostic judgments I haven't taught you here — but you now have the framework to supervise someone else's analysis, or to learn the software details quickly.

---

## Connections forward

Every method in this chapter, and every method in Chapter 5, rests on the same assumption: no unmeasured confounding. The back-door criterion says you can estimate a causal effect if you can measure and adjust for every variable that confounds the treatment-outcome relationship. Matching and weighting are both ways of doing the adjustment. Neither can help you if the confounders are unmeasured.

That's a real limitation. In many applied problems, we know there are confounders we can't measure — physicians' clinical judgments, students' motivation, firms' unobserved strategy. The back-door approach is stuck in those settings.

Chapter 7 takes up **instrumental variables**, which solve a subset of the unmeasured-confounding problem through an entirely different mechanism. Instead of adjusting for confounders, IV uses a variable — the instrument — that affects treatment but cannot plausibly affect the outcome except through treatment. A natural experiment. A policy change that happened to some people and not others for reasons unrelated to their outcomes. A genetic variant that affects the treatment but (hopefully) nothing else. These variables, when they exist, give you causal leverage without requiring that you observe all the confounders.

The cost is that IV requires a strong assumption — the *exclusion restriction* — that is usually untestable and frequently debatable. IV is more powerful than matching or weighting, because it handles unmeasured confounding, but it is also more fragile, because its core assumption cannot be verified from the data.

You'll see a pattern by the end of Chapter 7 that's worth noticing now: each method in this book buys one kind of protection at the cost of another kind of vulnerability. No method is free. The craft of causal inference is choosing which vulnerabilities you can live with given the problem in front of you.

Turn the page. We'll work on natural experiments.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **James M. Robins** developed inverse probability weighting and the g-formula in the 1980s — methods that handle time-varying confounders in longitudinal studies, where standard regression breaks down. His work is foundational to modern epidemiology and pharmacoepidemiology.

**Run this:**

```
Who is James M. Robins, and how do his weighting methods connect to the weighting we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"James Robins"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through inverse probability weighting on a specific time-varying treatment example.
- Ask it to compare Robins's structural nested models with marginal structural models — when does each tool apply?

What changes? What gets better? What gets worse?
