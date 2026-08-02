# Chapter 5 — Regression, Both Ways

---

## A Note on Asymmetry

Starting with this chapter, you will notice something: the Bayesian solution gets more space than the frequentist one. This is deliberate, and it is the lesson.

The frequentist regression analysis in this chapter is simpler. It has a closed-form solution, minimal assumptions to specify, and produces a result in seconds. You likely encountered it in a previous statistics course. There is nothing wrong with it.

The Bayesian analysis requires more: a prior on each parameter, a posterior computation, and a different framework for prediction. It takes more work to specify and more computation to run. But it returns something the frequentist analysis structurally cannot: a full probability distribution over outcomes — including $P(\text{sales increase} > \text{threshold} | \text{budget increase})$.

That extra output is why the extra space. The asymmetry in the chapter is not an apology for Bayesian complexity. It is evidence that the complexity buys something real.

---

## Learning Objectives

By the end of this chapter you should be able to:

1. **(Apply)** Fit and interpret a frequentist linear regression (OLS) model, including coefficient estimates, standard errors, and 95% confidence intervals.
2. **(Apply)** Specify and fit a Bayesian linear regression with weakly informative priors on slope and intercept, and summarize the posterior distributions.
3. **(Analyze)** Explain what a posterior predictive distribution is, how it differs from a frequentist prediction interval, and why it is more useful for decisions involving a probability threshold.
4. **(Evaluate)** Assess the practical implications of both approaches for a budget recommendation, and state when the Bayesian approach earns its additional complexity cost.

---

## The Problem

*Note: the following scenario is illustrative — the specific numbers are constructed for pedagogy, not drawn from a documented company.*

A retail analyst has weekly sales figures and advertising spend for a chain of stores over 60 weeks. She wants to answer two questions:

1. Does advertising spend drive sales? If so, by how much per dollar?
2. Should the company increase its advertising budget next quarter?

These questions look similar but are actually different. The first is a question about the relationship in the data. The second is a decision under uncertainty about a future outcome.

The analyst runs a regression. She gets a slope estimate and a significance test. She sends the result to the marketing director with a recommendation. The marketing director asks: "What is the probability that a 10% increase in advertising budget will increase sales by at least 5%?"

The analyst stares at her output. The p-value does not answer this. Neither does the coefficient.

This chapter is about that gap — and the tool that closes it.

---

## The Frequentist Solution

### Ordinary Least Squares

Let $Y_t$ = weekly sales (in thousands of dollars) and $X_t$ = weekly advertising spend (in thousands of dollars) for weeks $t = 1, \ldots, 60$.

The OLS regression model is:

$$Y_t = \alpha + \beta X_t + \epsilon_t, \quad \epsilon_t \sim N(0, \sigma^2)$$

OLS finds the $\hat{\alpha}$ and $\hat{\beta}$ that minimize the sum of squared residuals:

$$\hat{\alpha}, \hat{\beta} = \arg\min \sum_{t=1}^{60} (Y_t - \alpha - \beta X_t)^2$$

This is the *Best Linear Unbiased Estimator* (BLUE) under the Gauss-Markov conditions: homoscedastic errors, no autocorrelation, no perfect multicollinearity. These assumptions are worth checking in practice — but for a 60-week series with one predictor, OLS is a defensible starting point.

### Results

From the illustrative dataset:

$$\hat{\beta} = 2.3, \quad SE(\hat{\beta}) = 0.4$$

$$\hat{\alpha} = 124.7, \quad SE(\hat{\alpha}) = 8.2$$

The 95% confidence interval for the slope:

$$\hat{\beta} \pm 1.96 \times SE(\hat{\beta}) = 2.3 \pm 1.96 \times 0.4 = [1.52, \ 3.08]$$

The t-statistic:

$$t = \hat{\beta} / SE(\hat{\beta}) = 2.3 / 0.4 = 5.75, \quad p < 0.001$$

Goodness of fit: $R^2 = 0.36$ — advertising spend explains about 36% of the variance in weekly sales.

### Interpreting the OLS Result

"On average, each additional thousand dollars of weekly advertising spend is associated with a 2,300-dollar increase in weekly sales. This relationship is highly statistically significant ($p < 0.001$). The 95% confidence interval for the slope is $[1.52, 3.08]$."

This is a description. It is an association, not necessarily a causal claim. Both advertising spend and sales could be driven by a third variable — seasonal demand, for instance. The regression tells us the data are consistent with a positive relationship; it does not tell us that *increasing* advertising spend will *cause* sales to increase. This distinction (association vs. causal effect) is outside the scope of this chapter, but it is worth naming: regression is a descriptive and predictive tool; causal inference requires additional structure (McElreath, 2020).

### Prediction

For a given advertising spend $X_\text{new}$, OLS produces:
- **A fitted value:** $\hat{Y} = \hat{\alpha} + \hat{\beta} X_\text{new}$
- **A 95% confidence interval for the conditional mean** $E[Y | X_\text{new}]$: narrow, captures uncertainty in the estimated regression line.
- **A 95% prediction interval for a new observation** $Y_\text{new}$: wider, also includes the residual variance $\sigma^2$.

For the prediction of next quarter's average weekly sales at current advertising spend, the OLS prediction interval might be something like $[810, 1140]$ (thousands of dollars per week). This is a *range* — an interval. Not a probability distribution.

### Where Frequentist Strains

The analyst's question is: *What is the probability that a 10% increase in advertising budget will produce a sales increase of at least 5%?*

The OLS output cannot answer this directly. Why?

1. The slope estimate $\hat{\beta} = 2.3$ is a *point estimate*. It is the best single guess, but it is not a probability distribution. OLS uncertainty is quantified via the standard error and confidence intervals — these describe the sampling variability of $\hat{\beta}$ across hypothetical repeated samples, not a probability distribution over what $\beta$ might actually be.

2. The prediction interval for next quarter is a range, not a distribution. It tells her where a new observation might fall; it does not directly give $P(Y_\text{new} > \text{threshold})$.

Technically, you can extract such a probability from the prediction interval by using the normality of the predictive distribution. But this is the analyst doing Bayesian reasoning while pretending not to — she is using the interval's implicit distribution to compute a probability. The frequentist prediction interval does not officially support this interpretation, for the same reason the confidence interval does not.

The gap is structural: OLS produces point estimates and intervals. Decisions about future outcomes require probability distributions over future values. The Bayesian framework is built exactly for this.

---

## The Bayesian Solution

### Specifying Priors

The Bayesian regression model has the same structural form:

$$Y_t = \alpha + \beta X_t + \epsilon_t, \quad \epsilon_t \sim N(0, \sigma^2)$$

The difference is that $\alpha$, $\beta$, and $\sigma$ are now treated as random variables with prior distributions, updated to posterior distributions by the data.

**What should the priors encode?**

Before seeing the data, the analyst knows a few things:
- Advertising spend should have a non-negative effect on sales (or at least, it is implausible that advertising lowers sales).
- The effect per dollar is unlikely to be enormous — a dollar of advertising doesn't generate a thousand dollars of sales.
- The intercept (baseline sales with zero advertising) is somewhere in the positive range.

**Weakly informative priors** for this problem:

- **Intercept** $\alpha$: Normal(100, 50) — baseline weekly sales are somewhere around 100K, with substantial uncertainty.
- **Slope** $\beta$: Normal(0, 5) — centered at zero (no assumed direction), but most plausible values are in $[-10, 10]$. This is weakly informative relative to the data.
- **Residual standard deviation** $\sigma$: Half-Normal(30) — standard deviation of the unexplained variation is plausibly under 60K, but we have no strong view.

**Prior predictive check:** Before fitting the model, simulate data from these priors. Do the simulated sales figures look plausible? If the prior on $\beta = 5$ with Normal(0, 5) occasionally generates sales effects of 30K per dollar of advertising, the prior may be too diffuse. Checking this before seeing the data is the *prior predictive check* (McElreath, 2020) — a discipline that makes prior specification concrete and testable rather than arbitrary.

For this illustration, Normal(0, 5) on the slope produces plausible simulated sales series. We proceed.

### The Posterior

With $n = 60$ weekly observations, the data are fairly informative relative to these priors. In large samples, the posterior concentrates near the OLS estimate regardless of the prior — this is the Bayesian-frequentist convergence result (Gelman et al., 2013). For this dataset:

**Posterior on slope** $\beta$: approximately Normal(2.3, 0.4).
- Posterior mean: 2.3 (same as OLS)
- 95% credible interval: $[1.5, 3.1]$

**Posterior on intercept** $\alpha$: approximately Normal(124.7, 8.2).

**Posterior on** $\sigma$: posterior mean around 125K (the residual standard deviation).

These are nearly identical to the OLS results. This is expected and important. The OLS estimates equal the *maximum a posteriori* (MAP) Bayesian estimates under a flat (uniform) prior on the coefficients (Gelman & Hill, 2007). When the prior is weakly informative and the dataset is moderate (n = 60), the posterior is dominated by the data.

**This is the key result:** With 60 observations, the Bayesian and frequentist analyses produce the same coefficient estimates. The difference is not in the numbers. The difference is in what those numbers can do.

### The OLS = MAP Equivalence

It is worth making this precise. Under a flat (improper uniform) prior on $\alpha$, $\beta$, and $\sigma$:

$$P(\alpha, \beta, \sigma) \propto 1 \quad \text{(flat prior)}$$

The posterior is proportional to the likelihood alone:

$$P(\alpha, \beta, \sigma | \text{data}) \propto P(\text{data} | \alpha, \beta, \sigma) \times 1$$

The mode of this posterior (the MAP estimate) is exactly the OLS solution. This is not a coincidence — it is a theorem (Gelman & Hill, 2007; Gelman et al., 2013).

A note of precision: a flat (improper) prior on regression coefficients is not a valid probability distribution — it integrates to infinity. This creates no problem for point estimation (the MAP is still well-defined), but it creates problems for model comparison using Bayes factors. Do not use a flat prior when comparing models; use weakly informative priors instead.

### The Posterior Predictive Distribution

Here is where the Bayesian analysis diverges from OLS in a decision-relevant way.

The **posterior predictive distribution** for a new observation $Y_\text{new}$ at advertising spend $X_\text{new}$ integrates over the uncertainty in all parameters:

$$P(Y_\text{new} | X_\text{new}, \text{data}) = \int P(Y_\text{new} | X_\text{new}, \alpha, \beta, \sigma) \cdot P(\alpha, \beta, \sigma | \text{data}) \, d\alpha \, d\beta \, d\sigma$$

This is not just a point estimate plus a standard error. It is a full probability distribution over possible future sales values, incorporating:
1. Uncertainty in the regression coefficients ($\alpha$, $\beta$)
2. Irreducible residual variability ($\sigma$)

The frequentist prediction interval also accounts for both, but as a scalar interval — not a full distribution. The posterior predictive distribution is a distribution: you can compute any quantile, any probability above a threshold, any tail probability you need.

### Answering the Marketing Director's Question

The marketing director asked: "What is the probability that a 10% increase in advertising budget will increase sales by at least 5%?"

Let current average advertising spend be $X_0 = 50$ (thousands/week). A 10% increase gives $X_1 = 55$. The expected sales increase is:

$$E[\Delta Y | X_1 - X_0, \text{data}] = \hat{\beta} \times (X_1 - X_0) = 2.3 \times 5 = 11.5 \text{ thousand/week}$$

Current average sales are around 240 thousand/week (from the regression line). A 5% increase requires $\Delta Y \geq 12$ thousand/week.

From the posterior predictive distribution of $\Delta Y$ (which is approximately Normal with mean 11.5 and SD driven by parameter uncertainty and residual variance), we can compute:

$$P(\Delta Y \geq 12 | X_1 = 55, \text{data}) \approx 0.46$$

The marketing director now has the probability she needed: there is roughly a 46% chance the budget increase achieves the 5% sales target. That is not enough to say "increase the budget" confidently — the answer is actually "it's nearly a coin flip."

Contrast this with the OLS result: "The slope is 2.3, which is highly significant ($p < 0.001$)." This is technically true but does not directly answer the question. The slope is positive, advertising is associated with sales — but the specific probability of achieving the threshold cannot be extracted from OLS output without doing the posterior computation implicitly anyway.

---

## Side-by-Side Comparison

| | **Frequentist (OLS)** | **Bayesian** |
|---|---|---|
| Slope estimate | $\hat{\beta} = 2.3$, $SE = 0.4$ | Posterior mean 2.3, SD ≈ 0.4 |
| 95% slope interval | CI: $[1.52, 3.08]$ (procedure guarantee) | CrI: $[1.5, 3.1]$ (probability statement) |
| Residual variance | Point estimate ($s^2$) | Posterior distribution over $\sigma$ |
| Prediction | Prediction interval (a scalar range) | Posterior predictive distribution (full) |
| $P(\text{ROI} > 0)$? | Not directly available | Computable from the posterior |
| $P(\Delta Y > \text{threshold})$? | Not directly available | Directly computable |
| Prior required? | No (implicit flat) | Yes — weakly informative here |
| Computation | Closed form (OLS formula) | MCMC or approximation |

### Why Anyone Uses OLS Regression

OLS is fast, produces identical point estimates to MAP Bayesian regression with flat priors, and its output ($\hat{\beta}$, $SE$, $p$-value, $R^2$) is understood by every statistician, economist, and data analyst on the planet. For *description* — characterizing the historical relationship between advertising and sales — OLS is excellent and efficient. For *explanation* in stable settings — "how much is each variable associated with the outcome, on average?" — OLS is entirely adequate.

The Bayesian approach earns its additional complexity cost specifically when:

1. **The decision requires a probability statement about a future outcome.** "$P(\Delta Y > \text{threshold})$" or "$P(\text{ROI} > 0)$" cannot be produced by OLS without converting it to a quasi-Bayesian calculation anyway. Better to do it explicitly.

2. **The prior contains real information.** If the analyst has historical advertising data from prior quarters, a prior that encodes "slopes of 2–3 are typical for this chain" would modestly shrink an outlier slope estimate toward what is historically plausible. OLS ignores this.

3. **The sample is small.** With $n = 10$ weeks, OLS estimates are imprecise and the choice of prior matters substantially. With $n = 60$, as here, the prior is almost irrelevant — both methods converge on similar answers.

The honest case for OLS: it is not wrong. For most descriptive and explanatory regression tasks in business analytics, it is entirely sufficient. The argument for switching to Bayesian regression is a decision-theoretic argument: the analyst needs a probability, not just an estimate.

---

## Worked Example

### Situation

The economist wants to estimate the return to education: how much does an additional year of schooling increase weekly earnings? This question uses publicly available wage data (Mincer, 1974 — the foundational economics earnings equation). *The specific scenario below is illustrative.*

She has a dataset of 200 workers with weekly earnings ($Y$, in dollars) and years of schooling ($X$, in years). She fits a simple regression:

$$\ln(Y_t) = \alpha + \beta X_t + \epsilon_t$$

(Using log-earnings is standard in labor economics because the relationship between schooling and earnings is approximately log-linear.)

### OLS First

$$\hat{\beta} = 0.09, \quad SE = 0.015$$

95% CI for $\beta$: $[0.06, 0.12]$.

Interpretation: "Each additional year of schooling is associated with approximately a 9% increase in weekly earnings. This relationship is highly statistically significant."

$R^2 = 0.28$. About 28% of the variance in log-earnings is explained by years of schooling.

### A Dead End

The economist's policy client asks: "If we fund a community college program that gives 200 workers two additional years of schooling, what is the probability that the average wage increase for participants exceeds 15%?"

Two years of additional schooling: $\hat{\beta} \times 2 = 0.18$ in log-earnings, which corresponds to approximately $e^{0.18} - 1 \approx 20\%$ in wages.

The OLS estimate suggests the average increase will exceed 15%. But *with what probability?* There is uncertainty in the coefficient; there is individual variation in returns to education; there are unobserved confounders. The OLS output cannot translate all of this into a direct probability for the policy client.

### Bayesian Regression

Priors:
- Intercept $\alpha$: Normal(6, 1) (log-weekly-earnings of ~$400 with uncertainty)
- Slope $\beta$: Normal(0.10, 0.05) (prior belief that returns to schooling are around 10%, based on labor economics literature [verify])
- $\sigma$: Half-Normal(0.5)

Posterior on slope (after seeing data): approximately Normal(0.09, 0.015) — the data dominate the prior.

For a 2-year schooling increase, the posterior on $\Delta \ln Y = \beta \times 2$ is approximately Normal(0.18, 0.03). Translating to wage percentage increase:

$$P(\text{wage increase} > 15\% | \text{data}) = P(\Delta \ln Y > 0.139 | \text{data}) \approx P(Z > (0.139 - 0.18)/0.03) \approx P(Z > -1.37) \approx 0.91$$

There is approximately a 91% probability that a 2-year schooling increase produces a wage gain exceeding 15%.

**Resolution:** The Bayesian posterior predictive distribution gives the policy client the probability she needed. The OLS analysis established that the relationship is real and positive; the Bayesian analysis answered the decision-relevant probability question.

**The lesson:** OLS and Bayesian regression agree on the size of the effect. They diverge on what questions they can answer downstream. The posterior predictive distribution is the tool for probability-valued decision support.

**The limit:** This example assumes the regression relationship is causal — that schooling *causes* earnings to increase, rather than both being caused by a third factor (ability, family background). Regression establishes association; causal claims require stronger design assumptions. The posterior on $\beta$ is a posterior on the association parameter, not on the causal effect. McElreath (2020) develops causal regression explicitly; the companion volume on causal inference goes further.

---

## Prompting for Implementation

### A Good Prompt

> "I have a linear regression problem with 60 weekly observations. Y = weekly sales (thousands). X = weekly advertising spend (thousands). OLS gives slope ≈ 2.3, SE ≈ 0.4, intercept ≈ 124.7.
>
> Please:
> 1. Confirm the OLS result (slope, SE, 95% CI, R²).
> 2. Fit a Bayesian linear regression with these weakly informative priors: Normal(100, 50) on intercept, Normal(0, 5) on slope, HalfNormal(30) on sigma. Use Python (PyMC) or R (brms) — your choice.
> 3. Report the posterior means and 95% credible intervals for slope, intercept, and sigma.
> 4. Compute the posterior predictive distribution for next quarter's sales if advertising spend increases by 10% from current levels (say from 50K to 55K per week).
> 5. From the posterior predictive distribution, compute P(sales increase > 5%) if we implement the 10% budget increase.
> 6. Show the mathematical steps for both approaches and interpret in plain language."

### What to Verify

1. **OLS = MAP convergence:** The posterior mean on the slope should be approximately equal to the OLS estimate (2.3). If they differ substantially with a weakly informative prior and $n = 60$, something is wrong.

2. **Prior influence check:** Ask the LLM to rerun with a tighter prior (Normal(1, 1) on slope). The posterior should shift slightly toward 1. This confirms the model is actually using the prior. If the posterior doesn't change at all, the LLM may have specified a flat prior regardless.

3. **Posterior predictive reasonableness:** For $X = 55$, the expected sales are around $124.7 + 2.3 \times 55 = 251.2$K. The posterior predictive distribution should be centered near this value with substantial spread ($\pm 2\sigma$).

### Aging Note

The specific syntax for PyMC, brms, or Stan changes with each major release. Do not memorize it. The mathematical structure — prior $\times$ likelihood $\propto$ posterior, posterior predictive by integrating over parameter uncertainty — does not change. Prompt for the structure; verify the output against the math.

### A Specific Trap

LLMs sometimes return a **confidence interval for the conditional mean** when you ask for a **prediction interval for a new observation**. These are different widths. A CI for $E[Y|X]$ does not include residual variance; a prediction interval for $Y_\text{new}$ does. The Bayesian posterior predictive distribution correctly includes both. If the LLM's prediction interval looks implausibly narrow (say, $\pm 5$ when you expect $\pm 50$), it may have given you the CI for the mean rather than the full posterior predictive.

---

## Common Misconceptions

### Misconception 1: "OLS and Bayesian regression are just two ways to get the same answer"

**The plausible claim:** With $n = 60$ and weakly informative priors, both methods give slope = 2.3 and nearly identical intervals. They must be equivalent.

**Why it fails:** The coefficient estimates converge — this is the MAP = OLS theorem. The *downstream capabilities* do not. OLS cannot directly produce $P(\Delta Y > \text{threshold})$ without implicitly assuming a Bayesian posterior structure. The posterior predictive distribution is genuinely different from the prediction interval in what it licenses: one is a probability statement about a future value; the other is a frequentist coverage guarantee. Morey et al. (2016) showed the same distinction for intervals that Chapter 3 established: similar numbers, different meanings, different capabilities.

**Tie to the opening case:** The analyst got the same slope from both methods. But only the Bayesian analysis could answer the marketing director's question.

### Misconception 2: "A statistically significant slope means advertising works — increase the budget"

**The plausible claim:** $p < 0.001$ for the advertising coefficient. This is overwhelming evidence. Advertise more.

**Why it fails:** Statistical significance is about whether the slope is reliably different from zero — not about whether the expected return exceeds the cost of the investment. A slope of 2.3 means each additional dollar of advertising is associated with $2.30 of additional sales *on average*. If the gross margin is 40%, that is $0.92 of profit per dollar of advertising — a loss. Without knowing the decision threshold (ROI requirement), statistical significance is a necessary but not sufficient condition for "increase the budget." Greenland et al. (2016) document this confusion: a significant result establishes association; the decision to act requires a loss function.

**Tie to the opening case:** The manager who concludes "advertising works, spend more" from $p < 0.001$ has not asked whether the expected return exceeds the cost. That is a threshold question, and it requires the posterior predictive distribution to answer.

### Misconception 3: "The 95% prediction interval tells me the probability of achieving the threshold"

**The plausible claim:** The OLS 95% prediction interval for next quarter's sales is $[810, 1140]$ thousand per week. The threshold is 850. Since 850 is inside the interval, we're probably fine.

**Why it fails:** A prediction interval is a frequentist coverage guarantee — not a probability statement about this particular next-quarter outcome. Whether 850 is "inside" or "outside" the interval tells you something about the width of plausible outcomes, but not about $P(Y > 850 | \text{data})$ directly. The posterior predictive distribution is the tool for that calculation, and it requires the Bayesian framework. This is the exact same philosophical issue from Chapter 3, now applied to regression prediction.

---

## AI Wayback Machine

**Helen M. Walker (1891–1983)** wrote the history of statistics while also practicing it. Her 1929 book *Studies in the History of Statistical Method* traced the development of regression and correlation from Galton's inheritance studies through the work of Karl Pearson and beyond (Walker, 1929). She was President of the American Statistical Association in 1944 and co-authored a major statistics textbook in 1953. What makes her worth pausing on here: Walker understood that statistical methods carry their origins with them. The word "regression" comes from Galton's observation that the children of tall parents "regress toward mediocrity" — they tend to be closer to the average than their parents. Every time an analyst fits a regression line to sales data, they are using a tool invented to study heredity. Walker would have asked: what gets lost when we forget that? The answer: the assumptions built into the method — linearity, normality of residuals, independent observations — are legible only if you understand where the method came from and what it was designed for. Using regression to predict sales without checking its assumptions is using a heredity tool without reading the instructions.

---

## Exercises

**1. (Apply)** Using the advertising-sales setup from this chapter:

*(a)* Verify the OLS calculation by hand: given slope = 2.3, intercept = 124.7, and current advertising spend $X = 50$, what is the fitted weekly sales value?

*(b)* Interpret the 95% CI for the slope, $[1.52, 3.08]$, in frequentist terms. What does it claim?

*(c)* Interpret the 95% credible interval for the slope, $[1.5, 3.1]$, in Bayesian terms. What does it claim that the CI does not?

*(d)* Use the posterior on the slope (Normal(2.3, 0.4)) to compute $P(\beta > 2.0 | \text{data})$. Show the calculation.

**2. (Analyze — Production)** The manager looks at the regression output and says: "The p-value is 0.0003. Advertising clearly works. Let's increase the budget by 20%."

Write a two-paragraph response (aimed at the manager) that:
- Correctly interprets what $p < 0.001$ establishes
- Explains what additional information is needed to justify the budget increase
- Describes the question the posterior predictive distribution can answer

**3. (Evaluate)** The company uses a decision threshold of $P(\text{ROI} > 0) > 0.85$ before approving budget increases. Current advertising spend is $X_0 = 50$K/week; proposed increase is to $X_1 = 60$K/week. Gross margin on sales is 40%.

*(a)* From the OLS output alone, can you determine whether $P(\text{ROI} > 0) > 0.85$? Explain why or why not.

*(b)* Using the posterior on the slope (Normal(2.3, 0.4)), compute $P(\Delta \text{profit} > 0 | X_1 = 60)$, where $\Delta \text{profit} = 0.40 \times 2.3 \times 10 - 10$ (in thousands). Does the Bayesian analysis support the budget increase at this threshold?

*(c)* Which approach can directly evaluate the company's decision criterion? State one scenario where you would still prefer the OLS approach despite its limitation here.

---

## What Would Change My Mind

The argument that Bayesian regression earns its complexity specifically when decisions require probability thresholds would weaken if a frequentist alternative — say, conformal prediction intervals (which provide distribution-free finite-sample coverage guarantees) — could provide calibrated probability statements about future outcomes without requiring a prior. As of this writing, conformal methods provide coverage guarantees but not direct $P(Y > \text{threshold})$ statements in the way a posterior predictive distribution does. If this gap closes — and it is an active research area — the decision-theoretic advantage of Bayesian regression for threshold-based decisions would diminish. Additionally, if the analyst's prior is poorly specified (e.g., based on an outdated or irrelevant historical dataset), the Bayesian posterior predictive distribution could be *worse* calibrated than the OLS prediction interval. Prior misspecification is a real failure mode, not a theoretical one.

---

## Still Puzzling

1. **What counts as "weakly informative" for a regression prior?** Normal(0, 5) on the slope was used here, but whether this is weakly informative depends on the units of $X$ and $Y$. If advertising is measured in millions rather than thousands, the same prior becomes extremely tight. Gelman recommends standardizing predictors before specifying priors — but how to communicate standardized coefficients to a non-statistical audience remains an open pedagogical question.

2. **The causal question.** The regression gives an association; the decision to increase the budget requires a causal claim. What additional assumptions would make the regression coefficient interpretable as a causal effect? Does the Bayesian posterior distribution over a causal effect look different from the posterior over an associational coefficient?

3. **Does the posterior predictive distribution handle model misspecification?** The posterior predictive distribution accounts for parameter uncertainty but still conditions on the model being correct (linear relationship, normal errors). If the true relationship is saturating — advertising has diminishing returns — both OLS and Bayesian regression will overestimate the effect of large budget increases. Neither framework protects against model misspecification automatically.

4. **When do OLS and MAP actually differ?** With $n = 60$ and weakly informative priors, they agree. At what sample size or prior strength does the difference become practically significant? Is there a rule of thumb?

---

## Bridge to Chapter 6

Regression assumes you know which model to fit. Here, you fit a line: $Y = \alpha + \beta X + \epsilon$. But what if you didn't know whether a linear model or an exponential growth model better describes the data? Chapter 6 is about comparing models — choosing between them, or averaging over them. The frequentist approach produces rankings (which model fits better by AIC or likelihood ratio); the Bayesian approach produces probabilities (how much more likely is one model given the data?). The difference matters most when the models are close in fit, and when the downstream decision depends on which model you trust.

---

## References

Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A., & Rubin, D. B. (2013). *Bayesian Data Analysis* (3rd ed.). Chapman and Hall/CRC.

Gelman, A., & Hill, J. (2007). *Data Analysis Using Regression and Multilevel/Hierarchical Models*. Cambridge University Press.

Gelman, A., Hill, J., & Vehtari, A. (2020). *Regression and Other Stories*. Cambridge University Press. [verify publication details]

Greenland, S., Senn, S. J., Rothman, K. J., Carlin, J. B., Poole, C., Goodman, S. N., & Altman, D. G. (2016). Statistical tests, P values, confidence intervals, and power: A guide to misinterpretations. *European Journal of Epidemiology*, 31, 337–350. https://doi.org/10.1007/s10654-016-0149-3

McElreath, R. (2020). *Statistical Rethinking: A Bayesian Course with Examples in R and Stan* (2nd ed.). Chapman and Hall/CRC.

Mincer, J. (1974). *Schooling, Experience, and Earnings*. National Bureau of Economic Research.

Morey, R. D., Hoekstra, R., Rouder, J. N., Lee, M. D., & Wagenmakers, E.-J. (2016). The fallacy of placing confidence in confidence intervals. *Psychonomic Bulletin & Review*, 23(1), 103–123. https://doi.org/10.3758/s13423-015-0947-8

Walker, H. M. (1929). *Studies in the History of Statistical Method*. Williams & Wilkins.
