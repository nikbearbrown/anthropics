# Chapter 3 — Counting and Estimating

---

## Learning Objectives

By the end of this chapter you should be able to:

1. **(Apply)** Construct a frequentist confidence interval for a proportion using both the Wald and Wilson methods, and state what the interval does and does not claim.
2. **(Apply)** Build a Beta-Binomial Bayesian model, perform a conjugate posterior update, and compute a credible interval.
3. **(Analyze)** Explain the difference between what a confidence interval and a credible interval actually say about the true parameter — and why the distinction matters for real decisions.
4. **(Evaluate)** Assess when each approach is more useful for a quality-control decision, and articulate a fair case for using either.

---

## The Problem

A quality-control engineer at a circuit-board manufacturer tests 50 boards pulled at random from a production batch. Eight of the 50 are defective.

Her question is simple: *What is the true defect rate for this batch, and how confident should I be in my estimate?*

More precisely, she has a purchasing threshold: the contract with her client specifies that she will reject any batch where the underlying defect rate exceeds 20%. She needs to decide, based on 50 boards, whether this batch is acceptable.

She reaches for what she knows — a confidence interval — and gets an interval. Then she asks the question the interval cannot answer. This chapter is about that gap, and about the tool that closes it.

---

## The Frequentist Solution

### Point Estimate

With 8 defective boards out of 50, the natural estimate of the true defect rate is:

$$\hat{p} = \frac{8}{50} = 0.16$$

That is the maximum likelihood estimate (MLE). It is the value of $p$ most consistent with the data.

### Standard Error and the Wald Interval

The standard error of a sample proportion is:

$$SE = \sqrt{\frac{\hat{p}(1 - \hat{p})}{n}} = \sqrt{\frac{0.16 \times 0.84}{50}} = \sqrt{\frac{0.1344}{50}} = \sqrt{0.002688} \approx 0.0519$$

The Wald 95% confidence interval (the one most textbooks teach by default) is:

$$\hat{p} \pm 1.96 \times SE = 0.16 \pm 1.96 \times 0.0519 = 0.16 \pm 0.102$$

$$\text{Wald 95% CI: } [0.058, \ 0.262]$$

### The Wilson Interval (Preferred)

The Wald interval has a known problem: for proportions near 0 or 1, or for small samples, its actual coverage falls below the nominal 95% — sometimes badly. Brown, Cai, and DasGupta (2001) showed this definitively and recommended the Wilson interval as the default for proportions. The Wilson interval adjusts the center of the interval and is asymmetric:

$$\frac{\hat{p} + \frac{z^2}{2n}}{1 + \frac{z^2}{n}} \pm \frac{z}{1 + \frac{z^2}{n}} \sqrt{\frac{\hat{p}(1-\hat{p})}{n} + \frac{z^2}{4n^2}}$$

For our data ($\hat{p} = 0.16$, $n = 50$, $z = 1.96$):

$$\text{Wilson 95% CI: } [0.074, \ 0.284]$$

The Wilson interval is slightly wider and shifted. We will use it as the frequentist answer because it is the more defensible choice. Note that neither interval touches 0 or 1, which is reassuring here — the Wald interval can produce nonsensical bounds like $[-0.02, 0.34]$ at more extreme proportions or smaller samples.

### The Correct Interpretation

Here is where the frequentist framework requires care. A 95% confidence interval does *not* mean:

> "There is a 95% probability that the true defect rate is between 0.074 and 0.284."

That is the interpretation almost everyone wants — and it is wrong, in the frequentist framework.

What a 95% CI actually means is this: if you were to repeat this procedure — sample 50 boards, compute the interval — many times, then 95% of the intervals you construct would contain the true defect rate. This particular interval either contains the true rate or it does not. No probability attaches to *this* interval.

This is not a technicality. It is the foundational philosophical position that Jerzy Neyman built confidence intervals on when he introduced them in 1937 (Neyman, 1937). He was explicit: the guarantee is on the *procedure*, not on any particular outcome. Hoekstra et al. (2014) documented that this misinterpretation is not limited to students — 120 researchers in psychology endorsed, on average, more than three out of six false statements about confidence intervals.

### Where Frequentist Strains

The engineer's actual question is not "does this interval contain the true rate?" It is:

> **What is the probability that the true defect rate is below 20%?**

The confidence interval cannot answer this. It gives her a range. It gives her a frequentist guarantee about the procedure that produced the range. It does not give her a probability statement about this particular batch.

To put it plainly: the engineer needs $P(\text{defect rate} < 0.20)$. The frequentist machinery produces an interval — and staring at $[0.074, 0.284]$, she can see that 0.20 falls inside the interval, but she cannot say *how far* it falls inside, or what probability she should assign to the rate being on either side of 0.20. That question is structurally outside what a confidence interval can answer. It requires a probability distribution over possible parameter values — which is exactly what Bayesian inference provides.

---

## The Bayesian Solution

### Ingredients: Prior, Likelihood, Posterior

Bayesian inference requires three things:

1. A **prior** on the parameter $p$ — our belief about the defect rate before seeing the data.
2. A **likelihood** — the probability of the data given each possible value of $p$.
3. A **posterior** — the updated belief about $p$ after seeing the data.

The relationship is Bayes' theorem:

$$\text{posterior} \propto \text{likelihood} \times \text{prior}$$

### The Beta Distribution as a Prior

The defect rate $p$ is a probability — it must lie between 0 and 1. The Beta distribution is the natural prior for proportions. A Beta($\alpha$, $\beta$) distribution has:

- **Mean:** $\frac{\alpha}{\alpha + \beta}$
- **Shape:** controlled by $\alpha$ (pseudocounts of "successes") and $\beta$ (pseudocounts of "failures")

For this problem, the engineer knows nothing specific about this supplier's defect rate. The **uniform prior** Beta(1, 1) assigns equal probability to every possible defect rate between 0 and 1. It encodes: "I have no prior knowledge — all values are equally plausible." This is the most conservative choice in the absence of historical data. (A note for precision: the Jeffreys prior for a proportion is Beta(0.5, 0.5), which has better theoretical properties near the boundaries. For $n = 50$, the choice between them makes little practical difference. We use Beta(1, 1) here for simplicity.)

### The Likelihood

With $k = 8$ defective boards out of $n = 50$, the likelihood of the data under any particular defect rate $p$ is the Binomial probability:

$$P(\text{data} | p) = \binom{50}{8} p^8 (1-p)^{42}$$

This function is maximized at $p = 0.16$ — which is why the MLE and the sample proportion agree.

### The Conjugate Update

The Beta distribution is the **conjugate prior** for the Binomial likelihood. This means the posterior is also a Beta distribution, and the update is a simple closed-form calculation (Gelman et al., 2013):

$$\text{Beta}(\alpha, \beta) + \text{Binomial}(n, k) \rightarrow \text{Beta}(\alpha + k, \ \beta + n - k)$$

Starting with Beta(1, 1) and observing $k = 8$ successes in $n = 50$ trials:

$$\text{Posterior: } \text{Beta}(1 + 8, \ 1 + 42) = \text{Beta}(9, 43)$$

That is the entire update. Add the number of defectives to $\alpha$; add the number of working boards to $\beta$.

### Posterior Summary

**Posterior mean:**

$$E[p | \text{data}] = \frac{\alpha}{\alpha + \beta} = \frac{9}{9 + 43} = \frac{9}{52} \approx 0.173$$

This is slightly higher than the frequentist estimate of 0.16. Why? The uniform prior Beta(1,1) contributes two "pseudocount" observations (one defective, one working), pulling the posterior mean slightly toward 0.5 relative to the raw proportion.

**95% credible interval:** The equal-tailed 95% credible interval is the range containing the middle 95% of the posterior distribution. For Beta(9, 43), this is approximately:

$$\text{95\% CrI: } [0.082, \ 0.295]$$

**The correct interpretation:** Given these data and a uniform prior, there is a 95% probability that the true defect rate is between 0.082 and 0.295.

This is the statement the engineer wanted. It is a direct probability claim about the parameter — not a claim about the procedure that produced the interval.

### Answering the Engineer's Actual Question

The engineer needs $P(\text{defect rate} < 0.20 | \text{data})$. This is the cumulative distribution function (CDF) of the Beta(9, 43) posterior evaluated at 0.20:

$$P(p < 0.20 | \text{data}) = \int_0^{0.20} \text{Beta}(p; 9, 43) \, dp \approx 0.76$$

In plain language: given 8 defectives in 50 boards and no prior information about this supplier, there is approximately a **76% probability** that the true defect rate is below the 20% threshold.

Is that enough to accept the batch? That depends on the engineer's decision standard — and that is a judgment that lives outside the statistics. But notice what has changed: she now has the probability she needed to make a principled decision. The frequentist CI gave her a range; the Bayesian posterior gave her the probability.

---

## Side-by-Side Comparison

| | **Frequentist** | **Bayesian** |
|---|---|---|
| Point estimate | $\hat{p} = 0.16$ (MLE) | Posterior mean = 0.173 |
| 95% interval | Wilson CI: $[0.074, 0.284]$ | Credible interval: $[0.082, 0.295]$ |
| What the interval means | 95% of such intervals (over repeated sampling) contain the true rate | 95% probability the true rate is in this range |
| $P(\text{rate} < 0.20)$ available? | No | Yes: $\approx 0.76$ |
| Prior required? | No | Yes — uniform (Beta(1,1)) here |
| Assumption about the world | The true $p$ is fixed; data are random | Both $p$ and data are uncertain; $p$ has a distribution |

The intervals are similar in width. This is expected: with $n = 50$, both methods have reasonable amounts of data to work with. The convergence on similar *numbers* is not the point. The point is that the same numbers mean different things — and only one of them can answer the engineer's question.

### Why Anyone Uses the Frequentist Method Here

The frequentist approach is fast, requires no prior specification, and is the accepted standard in manufacturing quality frameworks (ISO 2859 attribute sampling plans, for instance). For large samples where the decision only requires the interval itself — "is the interval far from the threshold?" — the frequentist approach is entirely adequate, and the philosophical objection to it is largely academic.

Moreover, the Wilson CI has good frequentist properties: Brown et al. (2001) showed it has near-nominal coverage across the range of $p$. For a manufacturer who needs to produce consistent, auditable accept/reject decisions, a frequentist procedure with documented coverage properties is a defensible choice that does not require justifying a prior to a quality auditor.

The Bayesian approach earns its additional complexity specifically when:
- The decision requires $P(\text{rate} < \text{threshold})$ directly, or
- Prior information about the supplier's historical performance genuinely exists and should be incorporated, or
- The sample size is small enough that the choice of prior has material effect on the posterior.

Neither approach is wrong. They answer different questions.

---

## Worked Example

### Situation

A new supplier sends a trial batch of 30 circuit boards. The engineer tests all 30. Three are defective. Her acceptance standard requires $P(\text{defect rate} < 0.15) > 0.80$ before she approves the batch for regular orders.

### Process

**Frequentist first:**

Point estimate: $\hat{p} = 3/30 = 0.10$.

Standard error: $SE = \sqrt{0.10 \times 0.90 / 30} = \sqrt{0.003} \approx 0.0548$.

Wilson 95% CI for $p = 0.10$, $n = 30$: approximately $[0.034, 0.258]$.

The interval comfortably spans both sides of 0.15. The engineer cannot rule out rates from 3% to 26%. Can she accept the batch?

The frequentist framework does not give her a probability answer. Looking at the interval, 0.15 is toward the higher end, but there is no mechanism to say "the probability it's below 0.15 is X%."

She could do a one-sided hypothesis test: $H_0: p \geq 0.15$ vs. $H_1: p < 0.15$. The test statistic is $z = (0.10 - 0.15)/0.0548 \approx -0.91$, giving $p$-value $\approx 0.18$. She fails to reject $H_0$ — but "failing to reject" is not the same as "the rate is probably below 0.15." The frequentist machinery is not built to answer her question directly.

**Dead end noted:** The hypothesis test approach looks like it might work, but it produces a p-value for the data given the null, not a probability that the null is false. She is at the same wall she hit before.

**Bayesian:**

Again using a uniform prior Beta(1, 1):

$$\text{Posterior: } \text{Beta}(1 + 3, \ 1 + 27) = \text{Beta}(4, 28)$$

Posterior mean: $4/32 = 0.125$.

95% credible interval: approximately $[0.038, 0.287]$.

Now compute $P(p < 0.15 | \text{data})$ from the Beta(4, 28) CDF:

$$P(p < 0.15 | \text{data}) \approx 0.72$$

The engineer's standard requires $P < 0.15 > 0.80$. The posterior gives 0.72 — she falls short of her threshold.

**Resolution:** Based on 3 defectives in 30 boards, the evidence is not strong enough to meet the acceptance criterion. The sample is too small to establish with 80% confidence that the defect rate is below 15%. She has two defensible options: (a) reject the trial batch and ask for a larger sample, or (b) use prior knowledge about the supplier if it exists (e.g., if they have a documented history of 5–8% defect rates, an informative prior would shift the posterior).

**The lesson:** The Bayesian framework makes the engineer's decision explicit and calculable. The limit: the answer depends on what prior she uses. A non-uniform prior — justified by supplier history — would give a different $P(p < 0.15)$. That dependence on the prior is not a bug; it is the framework forcing her to confront what she actually knows.

---

## Prompting for Implementation

The conjugate Beta-Binomial update is simple enough to do by hand, but for computing posterior probabilities and credible intervals, an LLM with code execution can verify and extend your calculations.

### A Good Prompt

> "I have a Beta-Binomial inference problem. I started with a uniform prior Beta(1, 1) on a proportion. I observed 8 successes in 50 trials. Please:
> 1. Compute the posterior distribution.
> 2. Compute the posterior mean and 95% equal-tailed credible interval.
> 3. Compute P(p < 0.20) from this posterior.
> 4. Also compute the frequentist Wilson 95% confidence interval for comparison.
> 5. Show the mathematical steps for each, not just the code."

### Verification

You should be able to verify by hand:
- The posterior parameters: Beta(9, 43). Check: $\alpha + \beta = 52$, posterior mean $= 9/52 \approx 0.173$. ✓
- The credible interval bounds should bracket approximately 95% of the Beta(9, 43) distribution.
- The frequentist CI from the LLM should match the Wilson formula calculation.

### Aging Caveat

The specific Python or R syntax for `scipy.stats.beta.cdf()` or `qbeta()` may change. What does not change is the mathematical structure: posterior $=$ Beta($\alpha + k$, $\beta + n - k$), CDF evaluated at the threshold. Verify the LLM's output against this formula, not against prior familiarity with the code.

### Common LLM Error to Watch For

LLMs occasionally produce a "probability statement" interpretation of a confidence interval — e.g., "the 95% CI means there is a 95% probability the true rate is in [0.074, 0.284]." This is the fundamental confidence fallacy (Morey et al., 2016). If you see this in an LLM's output, the interpretation is wrong even if the numbers are correct. Check any plain-language explanation the LLM produces against the strict frequentist definition: a coverage guarantee on the procedure, not a probability statement about this particular interval.

---

## Common Misconceptions

### Misconception 1: "The 95% CI means there's a 95% chance the true rate is in the interval"

**The plausible claim:** You computed a 95% confidence interval of $[0.074, 0.284]$. It is natural to read this as: "I'm 95% confident the true rate is somewhere in here."

**Why it fails:** In the frequentist framework, the parameter $p$ is a fixed (unknown) constant, not a random variable. Before you compute the interval, there is a 95% probability the interval you compute will capture $p$. After you compute it, the interval either contains $p$ or it doesn't — there is no probability left to assign. The 95% applies to the *procedure*, not to this particular interval.

Morey et al. (2016) showed this formally: a specific confidence interval does not provide a 95% probability in the Bayesian sense, and can in fact provide strong evidence that the true value is *outside* the interval even when the value appears inside it. This is counterintuitive but mathematically correct.

**Tie to the opening case:** If the engineer says "I'm 95% confident the true rate is below 0.284," she is making a probability statement a confidence interval cannot support. She is accidentally doing Bayesian reasoning without the prior. The credible interval is the honest way to make that statement.

### Misconception 2: "Bayesian credible intervals require strong assumptions; confidence intervals don't"

**The plausible claim:** A CI requires no prior. A credible interval requires a prior. Priors are subjective. Therefore confidence intervals are more objective.

**Why it fails:** Both approaches assume something. The frequentist CI assumes a specific data-generating procedure (repeated sampling from the same population) that usually does not literally hold. In practice, you test one batch once. The Bayesian analysis with a uniform prior, Beta(1, 1), assumes nothing about the true rate except that it's between 0 and 1 — which is implied by the problem. That is not a strong assumption. The "objectivity" of a CI comes from avoiding the prior, but it buys that objectivity by declining to answer the probability question the engineer needs.

**Tie to the opening case:** The engineer cannot use the CI to answer $P(p < 0.20)$. This is not because she made a bad choice; it is because the CI does not carry a probability distribution over parameter values. The Bayesian model does, and the uniform prior is the most conservative way to get it.

### Misconception 3: "Because the numbers are similar, the two approaches say the same thing"

**The plausible claim:** The Wilson CI is $[0.074, 0.284]$ and the credible interval is $[0.082, 0.295]$. These are close. Aren't the two approaches really equivalent?

**Why it fails:** The numerical similarity is real and expected for moderate sample sizes. But the *content* of the statements is different. The CI says: a procedure guarantee. The credible interval says: a probability. One can be used to compute $P(p < 0.20)$; the other cannot. The numbers converging does not mean the questions converge.

This similarity also foreshadows something important: in Chapters 8 and 9, when data is sparse or grouped, the two approaches can produce substantially different intervals, not just differently interpreted ones. The convergence here is a special case, not a general rule.

---

## AI Wayback Machine

**Prasanta Chandra Mahalanobis (1893–1972)** founded the Indian Statistical Institute in 1931 and built the National Sample Survey of India — the infrastructure that estimated agricultural output, food deficits, and economic conditions across a subcontinent of hundreds of millions of people, from carefully designed samples. Harold Hotelling described his sampling methods as the most accurate developed anywhere (Mahalanobis, biography, ISI archives). He was wrestling with the same question the circuit-board engineer faces: how confident can you be in an estimate based on a fraction of the whole? His answer — grounded in study design, sample size, and probability — was that you could be quite confident, if you designed the sampling procedure carefully. The engineer's 50-board test, the statistician's 95% CI, and Mahalanobis's national survey all rest on the same mathematical foundation: the central limit theorem and the law of large numbers, applied to samples taken from populations too large to enumerate entirely.

---

![Prasanta Chandra Mahalanobis (1893–1972)](../images/prasanta-chandra-mahalanobis-i48.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

## Exercises

**1. (Apply)** A new supplier sends a batch of 30 circuit boards. You test all 30 and find 3 defective.

*(a)* Compute the Wald 95% CI and the Wilson 95% CI for the defect rate. Report both intervals and explain why they differ.

*(b)* Using a uniform prior Beta(1, 1), compute the posterior distribution, its mean, and the 95% credible interval.

*(c)* Does your conclusion about whether to accept the batch change between the frequentist and Bayesian approaches? What question can the Bayesian approach answer that the frequentist approach cannot?

**2. (Analyze)** A colleague says: "The 95% confidence interval for the defect rate is $[0.074, 0.284]$. That means there's a 95% chance the true defect rate is somewhere in that range."

Write a two-paragraph response explaining (a) what the colleague got wrong, and (b) what interpretation would be correct. Use Neyman's (1937) original framework — the guarantee is on the *procedure*, not on this particular interval.

**3. (Evaluate — Production)** The acceptance standard requires $P(\text{defect rate} < 0.15) > 0.80$ before approving a batch.

*(a)* Using the original data (8 defective in 50), compute $P(p < 0.15 | \text{data})$ from the Beta(9, 43) posterior. Does this batch meet the standard?

*(b)* Suppose you tested 100 boards instead of 50, and found 16 defective (the same proportion). Recompute the posterior and $P(p < 0.15 | \text{data})$. Did the additional data change the decision?

*(c)* Which approach — frequentist or Bayesian — can directly evaluate the acceptance criterion? Explain why, and state what you would need to add to the frequentist approach to match the Bayesian answer.

---

## What Would Change My Mind

The main argument in this chapter — that the Bayesian credible interval is more useful for the engineer's decision because it directly provides $P(\text{parameter} < \text{threshold})$ — would weaken substantially if the acceptance decision could be reformulated as a pure pass/fail test with a fixed $\alpha$ level, auditable and legally defensible. ISO 2859 sampling plans are designed precisely for that context: the frequentist procedure provides a documented, standardized accept/reject rule that is harder to game than a Bayesian analysis where the prior is chosen by the analyst. In regulated industries where the procedure must be auditable regardless of any individual's prior beliefs, the frequentist method is not just adequate — it may be required. The argument for Bayesian methods here is strongest when the decision is probabilistic and the decision-maker can act on a posterior probability; it is weakest when the decision requires a fixed, prior-independent rule.

---

## Still Puzzling

1. **The prior sensitivity question.** The uniform prior Beta(1, 1) was a conservative choice, but it was still a choice. If the engineer had historical data suggesting this supplier typically produces 5% defect rates, a prior like Beta(3, 57) (encoding "roughly 5% with some uncertainty") would shift the posterior toward lower values and might produce $P(p < 0.20) > 0.90$. How should analysts justify their prior choice to someone who disputes it? This question deepens in Chapter 7.

2. **Small samples and the Wald interval's failure.** Brown et al. (2001) showed erratic coverage for $n < 30$ and extreme proportions. But exactly how small does the sample need to be before the Wilson interval also becomes unreliable? This gets serious in Chapter 8.

3. **The Jeffreys prior question.** The Jeffreys prior Beta(0.5, 0.5) has better theoretical properties than the uniform Beta(1, 1), particularly near the boundaries. For a defect rate close to 0%, this choice could matter. Should the textbook-standard "no prior information" prior be Beta(0.5, 0.5) rather than Beta(1, 1)?

4. **When do the intervals really diverge?** At $n = 50$, the Wilson CI and Beta(1, 1) credible interval are nearly identical in width. Is there a closed-form relationship between sample size and the expected width difference? At what $n$ do they become practically indistinguishable?

---

## Bridge to Chapter 4

The Beta-Binomial model works cleanly because the prior and likelihood are *conjugate* — the math closes to a simple formula. You add the data to the prior parameters and you are done. In Chapter 4, you will compare two groups — tutorial A versus tutorial B — where the clean closure starts to break down. Each group has its own mean, and you need a distribution over the *difference* between means. That requires more specification, more computation, and forces the question: what is the prior probability that an educational intervention of this kind actually produces a meaningful effect? The answer to that question will introduce the book's first encounter with the replication crisis.

---

## References

Brown, L. D., Cai, T. T., & DasGupta, A. (2001). Interval estimation for a binomial proportion. *Statistical Science*, 16(2), 101–133. https://doi.org/10.1214/ss/1009213286

Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A., & Rubin, D. B. (2013). *Bayesian Data Analysis* (3rd ed.). Chapman and Hall/CRC.

Hoekstra, R., Morey, R. D., Rouder, J. N., & Wagenmakers, E.-J. (2014). Robust misinterpretation of confidence intervals. *Psychonomic Bulletin & Review*, 21(5), 1157–1164.

Morey, R. D., Hoekstra, R., Rouder, J. N., Lee, M. D., & Wagenmakers, E.-J. (2016). The fallacy of placing confidence in confidence intervals. *Psychonomic Bulletin & Review*, 23(1), 103–123. https://doi.org/10.3758/s13423-015-0947-8

Neyman, J. (1937). Outline of a theory of statistical estimation based on the classical theory of probability. *Philosophical Transactions of the Royal Society of London, Series A*, 236, 333–380.
