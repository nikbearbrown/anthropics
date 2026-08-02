# Chapter 9 — Hierarchical Problems

> **Asymmetry notice.** This chapter spends more space on the Bayesian
> solution than any chapter before it. That asymmetry is the lesson.
> Hierarchical Bayesian models are substantially more complex than their
> frequentist analogs — and the extra complexity buys something real:
> a principled way to share information across groups that frequentist
> mixed models approximate but do not fully characterize. By the end of
> this chapter you will understand what the complexity buys, and when it
> is worth the price.

---

## Learning Objectives

By the end of this chapter you will be able to:

1. **(Understand)** Explain the partial-pooling problem and why it requires a hierarchical model — not just separate analyses of each group.
2. **(Apply)** Fit and interpret a frequentist linear mixed-effects model for grouped data using REML estimation.
3. **(Apply)** Specify and interpret a Bayesian hierarchical model with hyperpriors on group-level means and between-group variance.
4. **(Analyze)** Compare complete pooling, no pooling, and partial pooling — what each assumes, what each gets wrong, and when each fails.
5. **(Evaluate)** Assess when the added complexity of a full Bayesian hierarchical model is worth its computational cost compared to a mixed-effects model.

---

## The Problem

A school district wants to evaluate math performance across its 30 schools before deciding which ones receive additional instructional resources. The district testing office sends you a dataset. You open it and see the immediate problem: some schools have 200 students in the tested cohort, but four schools have fewer than 10 students each, and one has only 6.

You need to report a performance estimate for each school. The board meeting is in two weeks. School C scored 92% average on the standardized exam — but that average is based on 8 students. School A scored 74% — based on 200 students. Is School C actually performing better than School A, or is its high average a small-sample artifact?

This is not a new problem. Every time analysts rank schools, hospitals, police precincts, or baseball players on measurements taken from unequal-sized groups, they face the same structure: some groups have enough data to speak for themselves; others do not. The question is how to handle the ones that do not — and how to do it without letting the method quietly decide the answer.

The failure modes are visible before you run any analysis:

- **Complete pooling** — treat all 2,400 students as a single group, ignore school membership. Clean. Wrong. If schools differ at all, this erases the differences you were asked to measure.
- **No pooling** — analyze each school independently. School C's estimate is 92%, full stop. Unbiased? Yes. Useful? No: with 8 students, the standard error on that estimate is enormous, and the estimate will swing wildly with one student's score.
- **Partial pooling** — let small schools borrow information from the district-wide distribution, while allowing large schools to speak for themselves. Intuitively right. The question is how to do it rigorously.

This chapter builds both approaches to partial pooling — the frequentist mixed-effects model and the Bayesian hierarchical model — and shows exactly where they diverge.

---

## Frequentist Solution: The Mixed-Effects Model

### The Setup

The frequentist approach to partial pooling is the **linear mixed-effects model** (also called a multilevel model or random-effects model). The standard implementation in R is the `lme4` package (Bates, Mächler, Bolker, & Walker 2015).

The model assumes two levels:

- **Level 1 (students):** Each student's score $y_{ij}$ is drawn from a normal distribution with mean $\mu_j$ (the true performance level of school $j$) and residual variance $\sigma^2$.
- **Level 2 (schools):** Each school's true performance level $\mu_j$ is drawn from a normal distribution with mean $\mu_{\text{district}}$ (the district-wide grand mean) and variance $\tau^2$ (between-school variance).

Written out:

$$y_{ij} \sim \text{Normal}(\mu_j, \sigma^2)$$

$$\mu_j \sim \text{Normal}(\mu_{\text{district}}, \tau^2)$$

The model has three parameters to estimate from data: $\mu_{\text{district}}$, $\sigma^2$, and $\tau^2$. School-level values $\mu_j$ are not parameters in the frequentist sense — they are **random effects**, predicted from the estimated variance components using Best Linear Unbiased Predictions (BLUPs).

### Estimation: REML

The mixed-effects model is typically fit by **Restricted Maximum Likelihood (REML)**. The details of REML are beyond our scope here, but the key outputs are:

1. Fixed-effect estimate of $\mu_{\text{district}}$ (the grand mean).
2. Variance component estimates $\hat{\sigma}^2$ and $\hat{\tau}^2$.
3. For each school $j$: a BLUP estimate of $\mu_j$ and an associated standard error.

The critical feature of REML estimation is that the BLUPs for schools automatically shrink toward the grand mean — small schools shrink more, large schools less. This is partial pooling.

### Results for Our 30 Schools

With the district data (grand mean ≈ 72%, between-school SD $\hat{\tau}$ ≈ 6.5 points, within-school residual SD $\hat{\sigma}$ ≈ 8.2 points), the REML estimates for four representative schools look like this:

| School | n   | Raw mean | REML estimate | SE (REML) |
|--------|-----|----------|---------------|-----------|
| A      | 200 | 74.2%    | 74.0%         | 1.4%      |
| B      | 12  | 81.5%    | 79.2%         | 3.1%      |
| C      | 8   | 92.0%    | 83.1%         | 4.8%      |
| D      | 6   | 61.0%    | 67.4%         | 5.9%      |

*(Illustrative example based on the hierarchical structure in Rubin 1981 and Gelman et al. 2013.)*

School C's estimate (83.1%) is pulled substantially toward the district mean (72%), reflecting that 8 students cannot anchor a 92% estimate. School A's estimate barely moves (74.0% vs. 74.2% raw) because 200 students carry real weight. This is partial pooling in action.

### Where the Frequentist Model Strains

The mixed-effects model handles partial pooling correctly *in point-estimate terms*. But there is a specific gap in what it reports.

**The standard error reported for each school does not account for uncertainty in $\tau$.** The REML procedure first estimates $\hat{\tau}$, then uses that estimate as a fixed value when computing school-level standard errors. If $\hat{\tau}$ is itself uncertain — and with 30 schools it carries substantial uncertainty — that uncertainty is not propagated into the reported SEs.

For School C, the reported SE of 4.8% says: *given our estimate of the between-school variance, this is how uncertain we are about School C's performance.* What it does not say: *and our estimate of the between-school variance is itself uncertain, which would make School C's interval wider still.*

For large schools like School A, this gap is small: there is enough data that the school-level estimate is driven by its own 200 observations, not by the prior distribution. For School C with 8 observations, the school-level estimate is dominated by the prior — and the uncertainty in that prior matters a lot.

Bates et al. (2015) document this limitation directly: the profile likelihood intervals for variance components can be skewed, and the standard errors reported by `lme4` use approximations that understate uncertainty for small samples. This is not a bug in `lme4`; it is a consequence of what REML estimation can and cannot propagate.

---

## Bayesian Solution: Full Hierarchical Model

The Bayesian hierarchical model starts from the same structural specification as the mixed-effects model, but treats all parameters — including $\tau$ — as unknown quantities with posterior distributions, not as fixed estimates.

### Model Specification

$$y_{ij} \sim \text{Normal}(\mu_j, \sigma^2) \qquad \text{[likelihood]}$$

$$\mu_j \sim \text{Normal}(\mu_{\text{district}}, \tau^2) \qquad \text{[group-level prior = hyperprior]}$$

$$\mu_{\text{district}} \sim \text{Normal}(70, 15^2) \qquad \text{[district-level prior]}$$

$$\tau \sim \text{Half-Normal}(0, 10^2) \qquad \text{[prior on between-school SD]}$$

$$\sigma \sim \text{Half-Normal}(0, 15^2) \qquad \text{[prior on within-school SD]}$$

**Term by term:**

- $\mu_j$ is the true performance level of school $j$. It is not estimated from school $j$'s data alone — it is drawn from a district-wide distribution with mean $\mu_{\text{district}}$ and SD $\tau$. This is the formal statement of partial pooling.
- $\mu_{\text{district}}$ is the district-wide mean. We use a weakly informative prior centered at 70 (plausible for standardized exam scores) with SD 15 (wide enough to let the data move it substantially).
- $\tau$ is the between-school standard deviation — how much schools genuinely differ from each other. We use a half-normal prior on $\tau$ rather than a flat or uniform prior; Gelman (2006) showed that flat priors on variance components produce poorly behaved posteriors in sparse-group settings. A half-normal with scale 10 says: "between-school variation is probably less than 20 points, but I could be wrong."
- $\sigma$ is the within-school residual SD. Same logic: half-normal, informative enough to avoid degeneracy, loose enough to learn from data.

### What the Priors Buy

The priors on $\tau$ and $\sigma$ are not neutral defaults — they encode genuine prior knowledge. For a standardized exam in a typical school district:
- Within-school variation across students ($\sigma$) is almost always between 5 and 20 points.
- Between-school variation ($\tau$) in a moderately mixed district is typically 3–12 points.

A half-normal with scale 10 concentrates prior mass in this range while remaining diffuse enough to be updated by data. This is the principle from Chapter 7: when prior knowledge exists and is defensible, using it improves inference. A uniform prior on $\tau$ from 0 to ∞ would let the data pull $\tau$ to implausibly large values, producing poorly calibrated posteriors.

### Fitting the Model

In practice, this model is fit with Markov Chain Monte Carlo (MCMC) — a computational method that draws samples from the joint posterior distribution of all parameters. Modern software (`brms` in R, `PyMC` in Python, or Stan directly) handles the mechanics; Chapter 2's prompting skill applies directly here.

The output is not a single estimate per school — it is a posterior distribution for each $\mu_j$, which in turn reflects both the school's own data and the district-wide distribution, with the uncertainty in $\tau$ propagated through.

### Results

With the same district data:

| School | n   | Raw mean | Posterior mean | 95% CrI         | Interval width |
|--------|-----|----------|----------------|-----------------|----------------|
| A      | 200 | 74.2%    | 74.1%          | [71.3%, 76.9%]  | 5.6%           |
| B      | 12  | 81.5%    | 79.4%          | [73.1%, 85.7%]  | 12.6%          |
| C      | 8   | 92.0%    | 83.4%          | [74.2%, 92.8%]  | 18.6%          |
| D      | 6   | 61.0%    | 67.6%          | [56.9%, 78.3%]  | 21.4%          |

*(Illustrative example; structure derived from Rubin 1981 and Gelman et al. 2013, BDA3 Ch. 5.)*

Compare School C's interval: the REML SE was 4.8%, implying a 95% interval of roughly 83.1 ± 9.4, or [73.7%, 92.5%]. The Bayesian CrI is [74.2%, 92.8%] — slightly wider and more asymmetric. The difference reflects the propagated uncertainty in $\tau$: the Bayesian model says "we are also uncertain about how much schools vary, and that uncertainty widens School C's interval."

**The interval widths are the lesson.** School A's interval is 5.6 points wide — tight, because 200 observations anchor it. School D's interval is 21.4 points wide — genuinely uncertain, because 6 students cannot determine a school's true performance level. A model that reported School D's estimate as confidently as School A's would be misleading.

### The Partial Pooling Mechanism: How Much Does Each School Shrink?

The degree of shrinkage toward the grand mean is governed by a ratio called the **shrinkage factor**:

$$\lambda_j = \frac{\tau^2}{\tau^2 + \sigma^2 / n_j}$$

When $n_j$ is large, $\sigma^2/n_j$ is small, $\lambda_j \approx 1$, and the school's posterior mean is close to its raw mean. When $n_j$ is small, $\sigma^2/n_j$ dominates, $\lambda_j$ drops toward 0, and the posterior mean is pulled toward $\mu_{\text{district}}$.

School A (n=200): $\lambda_A \approx 0.95$ — near-no-pooling; 95% of the estimate comes from its own data.
School D (n=6): $\lambda_D \approx 0.37$ — strong pooling; more than half the estimate comes from the district-level prior.

This is not a bug. This is correct inference. With 6 students, School D's raw mean of 61% is a noisy measurement of something that may be quite different from 61%. The district average of 72% is a strong signal that should pull the estimate.

### Complete vs. No vs. Partial Pooling: A Summary

| Strategy          | What it assumes                             | What it gets wrong                                         |
|-------------------|---------------------------------------------|------------------------------------------------------------|
| Complete pooling  | All schools are the same                    | Ignores real between-school differences                    |
| No pooling        | Schools are completely independent          | Wildly unstable estimates for small schools                |
| Partial pooling   | Schools differ, drawn from a common distribution | Nothing structural — the question is how much to pool |

The no-pooling estimator (treat each school independently, take the raw mean) is **inadmissible** in the formal statistical sense: there is always a shrinkage estimator with lower mean squared error, for every possible true value of the school means. This is Stein's paradox (Stein 1956), made accessible in Efron & Morris (1977): simultaneous estimation of three or more normal means is always improved by shrinking toward a common value. The James-Stein estimator demonstrated this concretely with 18 baseball players' batting averages — pooling estimates across players produced smaller total prediction error than treating each player independently, even though batting averages are completely unrelated across players.

---

## Side-by-Side Comparison

| | Frequentist mixed model (lme4) | Bayesian hierarchical model |
|---|---|---|
| Small-school point estimates | Shrunk toward grand mean — correct in direction | Same shrinkage, correctly calibrated |
| Small-school uncertainty | SE understates due to fixed $\hat{\tau}$ | CrI wider — uncertainty in $\tau$ propagated |
| District-level inference | Fixed effect for $\mu_{\text{district}}$ with SE | Full posterior on $\mu_{\text{district}}$ and $\tau$ |
| Uncertainty in between-group variance | Not propagated to group estimates | Fully propagated |
| Computation | Fast — REML is closed-form | Slow — requires MCMC |
| Software | `lme4` — widely available, well-tested | `brms`, `PyMC`, `Stan` — accessible but steeper learning curve |
| Output interpretability | Familiar to social science audiences | Requires explanation of posteriors |
| Scales to 30+ groups | Yes | Yes, with patience |

### Why Anyone Uses Frequentist Mixed Models

Bluntly: because they work well most of the time. `lme4` is fast, its outputs are understood by every education researcher and public health analyst who has encountered mixed models, and for large balanced datasets where the variance components are well-identified, REML and full Bayesian models produce nearly identical answers.

The difference matters when three conditions hold simultaneously:

1. Group sizes are very unequal (as here — 8 vs. 200 students).
2. Some groups are small enough that their estimates are dominated by the prior (as here — Schools C, D).
3. The decision downstream cares about the *uncertainty* in those small-group estimates, not just the point estimates (as here — ranking schools for resource allocation).

If all three conditions hold, the Bayesian model's full propagation of $\tau$-uncertainty into each school's CrI earns its computational cost. If only large, balanced groups are involved, the two approaches are functionally equivalent. Choose accordingly.

---

## Worked Example: Eight Schools

The Eight Schools study (Rubin 1981) is the field's canonical case for hierarchical models. In 1976–1977, eight New York area high schools ran special SAT-preparation coaching programs. Each school had an estimated effect size (improvement in SAT scores attributable to the coaching) and a standard error, based on the number of students who took both the coaching and the exam. Three schools had very small enrolled samples.

The raw effect estimates ranged from −2 to +28 points. The question: what is each school's *true* coaching effect?

**Setup:** The analyst runs three analyses:

**(1) Complete pooling** — fit a single mean coaching effect across all eight schools. Result: 7.7 points. This is a defensible district-wide estimate but erases all information about which schools' programs actually work.

**(2) No pooling** — treat each school's estimate independently. Schools with small samples show huge uncertainty: School A's estimate is 28 points (SE 15), School C's is −3 points (SE 16). At the noisy end, these estimates overlap almost completely. No pooling forces the analyst to pretend the −3 and +28 estimates are both equally reliable.

**(3) Partial pooling (hierarchical Bayesian)** — specify a normal distribution over true school effects with unknown mean and variance. Fit via MCMC.

**Process and dead ends:** The first attempt at partial pooling uses a flat (uniform) prior on the between-school SD $\tau$. The posterior for $\tau$ has a long right tail — there are only 8 schools, so the data can barely identify $\tau$. With a flat prior, some MCMC chains estimate $\tau$ near zero (almost complete pooling) and others estimate $\tau$ large (near no-pooling). This does not produce a usable result.

**Resolution:** Switch to a half-normal prior on $\tau$ with scale 10 (Gelman 2006). The posterior for $\tau$ now concentrates around 6–10 points, consistent with the data and prior knowledge that coaching effects in similar programs vary modestly. School-level posteriors become well-behaved.

The posterior means for the eight schools range from 5 to 11 points — substantially compressed compared to the raw estimates of −2 to +28. The large compression reflects that the raw estimates are noisy, and the hierarchical model borrows information across schools to stabilize all estimates. School A's posterior mean is around 11 points (down from raw 28), with a credible interval of [1, 21] — meaningful improvement but with genuine uncertainty. The school that scored −2 raw has a posterior mean around 5 points with a wide interval — the data barely distinguish it from the others.

**Lesson:** Partial pooling doesn't mean "assume all schools are the same." It means "use the distribution of effects across schools to inform each school's estimate, with weight proportional to what that school's data can actually support." The school with 28 raw points gets pulled toward the mean because 28 is implausibly large given what we know about coaching effects in general. The school with −2 gets pulled toward the mean because −2 is implausibly small.

**Limit:** The Eight Schools example has only eight schools — too few to identify $\tau$ precisely. The posterior on $\tau$ is wide, which means the degree of shrinkage is uncertain, which makes all eight school estimates genuinely uncertain. With 30 schools (as in our main example), $\tau$ is better identified and the shrinkage is more reliable.

---

## Prompting for Implementation

This chapter's prompting section is longer than previous chapters. Specifying a hierarchical model requires more precision; misspecified hyperpriors produce wrong answers that pass syntactic checks.

### Step 1: Describe the data structure before the model

Bad prompt: *"Fit a hierarchical model to my school data."*

Better prompt:

> I have data from 30 schools. Each row is a student test score (continuous, 0–100). Students are nested within schools, and school sizes range from 6 to 200 students. I want to estimate each school's true mean performance, accounting for the fact that small schools have less reliable estimates. Please fit a Bayesian hierarchical model (also called a multilevel model) with:
> - A normal likelihood for student scores within each school
> - School-level means drawn from a district-wide normal distribution
> - Weakly informative priors: Normal(70, 15) on the district mean, Half-Normal(0, 10) on the between-school SD, Half-Normal(0, 15) on the within-school residual SD
> - Fit using `brms` in R (or `PyMC` in Python) and return the posterior mean and 95% credible interval for each school

### Step 2: Verify the output against first principles

After the model runs, check:

1. **Large schools:** their posterior means should be close to their raw means. If not, the prior is too strong or the between-school variance is being estimated incorrectly.
2. **Small schools:** their posteriors should be pulled toward the district mean. The smaller the school, the more pull. If a 6-student school's posterior mean equals its raw mean exactly, the model is not pooling — something is wrong.
3. **Interval widths:** small schools should have wider CrIs than large schools. If all schools have similar interval widths, the uncertainty propagation is broken.
4. **$\tau$ posterior:** with 30 schools, the posterior for $\tau$ should be identifiable — not flat. Ask the LLM to report the posterior mean and 95% CrI for $\tau$.

### Step 3: Common LLM failure modes for hierarchical models

- **Wrong likelihood:** LLMs sometimes use a Poisson likelihood by default for count-like outcomes, even when scores are continuous. Specify "normal likelihood" explicitly.
- **Misspecified hyperprior scale:** LLMs may default to `Half-Normal(0, 1)` which places nearly all prior mass below 2 points of between-school variation — implausibly tight. Always specify the scale explicitly.
- **Treating random effects as fixed:** Some LLM-generated code fits fixed effects for each school (a no-pooling model) while labeling it a "hierarchical model." Verify that the school-level means are modeled as drawn from a distribution, not estimated independently.

**Aging note (2026):** LLM-generated `brms` and `PyMC` code for hierarchical models is improving but remains more error-prone than ARIMA or logistic regression code. Always verify the model specification against the description you provided. The statistical core of this section will remain stable; the specific tools and prompting style may evolve.

---

## Common Misconceptions

### 1. "No pooling is unbiased, therefore it is best."

Unbiasedness is one property of an estimator — not the only one. The no-pooling estimator is unbiased for each school's true mean: its expected value equals the truth. But its variance is enormous for small schools. Mean squared error (MSE) = variance + bias². No pooling has low bias and high variance. Partial pooling introduces a small bias in exchange for substantially lower variance. For prediction and ranking purposes, partial pooling has lower MSE — which is what matters for the district's resource-allocation decision.

Stein's paradox (Stein 1956; Efron & Morris 1977) established this formally: for estimating three or more normal means simultaneously, the sample means are inadmissible — there always exists an estimator with lower total MSE. Shrinkage is not an approximation; it is provably better.

### 2. "Mixed-effects models and Bayesian hierarchical models give the same answer."

For large, balanced groups, yes — nearly identical point estimates. The difference is in what is reported about uncertainty. The mixed model reports standard errors that condition on fixed $\hat{\tau}$; the Bayesian model reports credible intervals that average over the posterior distribution of $\tau$. For School C (n=8), this difference is substantial: the Bayesian CrI is wider, more honest about what 8 students can tell you. The two models agree about *where* the estimate is; they disagree about *how confident* you should be.

### 3. "The hyperprior choice is arbitrary — the result depends on whatever prior I pick."

This conflates sensitivity with arbitrariness. The prior on $\tau$ does influence the result — Gelman (2006) documents this — but within a reasonable range of defensible choices (half-normal scale between 5 and 20, for exam scores), the posterior point estimates are robust. What does change with the prior is the uncertainty in the posterior: tighter priors on $\tau$ produce tighter school-level CrIs, which may be overconfident. The right response is to run a prior sensitivity analysis (Chapter 7), not to despair at having to choose. The choice of prior is an argument to make, not a problem to hide.

---

## AI Wayback Machine

**Donald B. Rubin (born 1943)**

In 1981, Donald Rubin published a paper in the *Journal of Educational Statistics* that seemed narrow in scope: eight New York high schools, a coaching program for the SAT, the question of how to combine noisy estimates across sites (Rubin 1981). The paper introduced the dataset that has appeared in nearly every serious Bayesian statistics textbook written since — including as the central example of Chapter 5 in Gelman et al.'s *Bayesian Data Analysis* (BDA3, 2013).

Rubin's contribution was to ask the right question. Not: *what is the true effect of coaching?* (complete pooling) or *what is this particular school's effect?* (no pooling) but: *how should we combine evidence from related but not identical experiments?* The answer — a hierarchical Bayesian model in which each school's effect is drawn from a common distribution — made the problem tractable and the uncertainty honest.

Rubin is also the originator of the Rubin Causal Model (potential outcomes framework, foundational to causal inference), which means the Eight Schools paper is something of an underknown contribution next to his causal-inference work. But for this chapter, it is the cornerstone.

Anchor prompt: *"What does Donald Rubin's 1981 Eight Schools study show about the limits of analyzing schools completely independently, and how does his hierarchical model improve on no-pooling estimates?"*

---

## Exercises

**1. (Apply)** Using the school district dataset on the companion website (or a similar NCES public dataset), fit both a frequentist mixed-effects model (`lme4` in R or `statsmodels` MixedLM in Python) and a Bayesian hierarchical model (`brms` or `PyMC`). Compare the posterior means and interval widths for the five smallest schools. What changes, and why?

**2. (Analyze)** A school with 6 students scores 95% average on the district exam. The district average is 72%. Under complete pooling, no pooling, and partial pooling, what is your estimate of this school's true performance? Compute the shrinkage factor $\lambda = \tau^2 / (\tau^2 + \sigma^2/n)$ using $\tau = 6.5$, $\sigma = 8.2$, $n = 6$. Which estimate do you trust most, and why? What would change your answer?

**3. (Evaluate)** A district official wants to rank all 30 schools and publish the rankings publicly. Using what you know from this chapter, write a one-page memo to the official that:
   - Explains which estimates are reliable and which are not
   - Specifies what sample size a school would need before its ranking should be taken at face value
   - Recommends one actionable step the district should take before publishing any ranking

**4. (Production)** Prompt an LLM to fit a Bayesian hierarchical model to the school data. Verify that: (a) small schools shrink more than large schools; (b) the posterior for $\tau$ is identifiable (not flat); (c) interval widths are wider for smaller schools. Report what verification steps you ran and what you had to correct.

---

## What Would Change My Mind

**The mixed-effects model is good enough when:**
- Group sizes are large and roughly equal (all schools have 50+ students).
- The downstream decision uses only point estimates, not probability statements about individual schools.
- Computational constraints make MCMC infeasible.

In those cases, I would use `lme4` without apology.

**The Bayesian hierarchical model earns its cost when:**
- Some groups are very small (fewer than 20 observations).
- The decision requires probability statements about individual groups (ranking confidence, outlier detection).
- The uncertainty in the between-group variance $\tau$ is large enough to matter.

If evidence emerged that REML-based standard errors were as accurate as posterior CrIs for small-group settings, I would update toward simpler tools. The gap I am defending here is empirical, not doctrinal.

---

## Still Puzzling

1. **How many groups are enough to identify $\tau$?** With 8 schools, the posterior on $\tau$ is wide and prior-sensitive. With 30, it is better. With 100+, it is well-identified. There is no sharp threshold, and the chapter cannot give one — it is a function of between-group effect size, within-group sample sizes, and how much $\tau$ matters for the decision.

2. **Empirical Bayes vs. full Bayes:** Empirical Bayes (Efron & Morris 1977) estimates $\tau$ from the data and then uses it as if it were known — a two-stage procedure that is simpler than full MCMC. For large numbers of groups, it performs nearly as well. For small numbers of groups, it underestimates the uncertainty in $\tau$. How to help a reader choose between them remains an open pedagogical question.

3. **What to do when groups have different predictors:** The model here uses only group membership as a predictor. Real school-performance analyses often include school-level predictors (size, demographics, funding). Adding covariates to the hierarchical model is straightforward in principle but increases the specification burden considerably.

4. **Value-added models for teacher effectiveness:** Hierarchical Bayesian models applied to teacher performance data produce estimates with wide credible intervals — so wide that teacher rankings shift by up to 8 deciles depending on context and year (IES research, ongoing). The model is correctly specified; the signal is genuinely weak. This suggests that some policy uses of hierarchical models are answering the right methodological question but the wrong substantive one.

---

## Bridge to Chapter 10

Chapter 9 handled grouped structure in cross-sectional data — students nested within schools, observed at one time. Chapter 10 introduces structure in time. Sequential updating is Bayesian inference in its most natural form: the posterior from today is the prior for tomorrow. If grouped structure is the clearest case for Bayesian hierarchical models, sequential updating is the clearest case for why Bayesian inference makes sense at all.

---

*Sources: Stein (1956); Efron & Morris (1977); Rubin (1981); Gelman et al. (2013, BDA3); Bates, Mächler, Bolker, & Walker (2015); Gelman (2006). Eight Schools numerical structure is illustrative based on BDA3 Ch. 5; labeled as such.*
