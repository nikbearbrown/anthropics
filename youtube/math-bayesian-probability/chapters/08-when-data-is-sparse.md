# Chapter 8 — When Data Is Sparse

---

## Learning Objectives

By the end of this chapter you will be able to:

1. **(Apply)** Identify when standard frequentist methods are unreliable for sparse data and explain the specific failure modes (Bloom: Apply)
2. **(Apply)** Build a Bayesian Beta-Binomial model with an informative prior derived from published literature and interpret the resulting posterior (Bloom: Apply)
3. **(Analyze)** Explain why statistically significant effects in underpowered studies are systematically too large — the winner's curse — using the Type M (magnitude) and Type S (sign) error framework from Gelman and Carlin (2014) (Bloom: Analyze)
4. **(Evaluate)** Assess the tradeoff between waiting for more data and acting on sparse evidence — and identify when Bayesian shrinkage helps and when it could lead you astray (Bloom: Evaluate)

---

## Opening Case: Three Complications in Two Years

A quality improvement committee at a regional hospital is reviewing surgical outcomes. Over the past two years, the hospital performed 200 laparoscopic appendectomies. Three patients developed a post-operative complication requiring a second intervention — a rate of 3/200 = 1.5%.

The committee needs to answer several questions. Is 1.5% an acceptable complication rate, given that the accreditation benchmark is below 2.5%? Is the rate getting better or worse compared to last year, when there were 2 complications in 150 procedures (1.33%)? And what should they tell the hospital board — which wants numbers, not hedges?

A biostatistician runs the standard frequentist analysis. The 95% confidence interval for the true complication rate is [0.31%, 4.35%]. The comparison to last year: p = 0.71, not significant. The statistical summary: no evidence of a change, but we cannot say much with confidence.

The committee chair, a former medical school professor, looks at this output and says exactly what every committee chair says in this situation: "So the statistics are useless. What do we actually do?"

She is wrong that the statistics are useless. But she is right that the output — a very wide interval, a non-significant p-value — is not what the committee needs. The problem is not a failure of statistical analysis. It is a structural feature of sparse data: with counts this small, the data simply do not speak loudly. The question is what to do about it.

---

## The Frequentist Solution: Technically Correct, Practically Incomplete

### Exact Binomial Analysis

When counts are small (as a rule of thumb, when n·p < 5 or n·(1−p) < 5), the normal approximation underlying the standard proportion test breaks down. For 3/200, we have n·p = 3 — well below the threshold. The appropriate frequentist method is the **exact binomial test**.

The maximum likelihood estimate of the complication rate is $\hat{p} = 3/200 = 0.015$. The exact binomial 95% confidence interval is computed by finding the values of $p$ for which the observed count (or more extreme) has at least 2.5% probability under each tail. This gives:

$$\text{95\% CI} = [0.0031, 0.0435]$$

In percentage terms: [0.31%, 4.35%]. The interval spans from nearly zero to nearly the accreditation threshold. This is not a computational error — it is the honest answer from 3 events. The data support almost any conclusion between "the rate is excellent" and "the rate is borderline acceptable."

**Year-over-year comparison:** Comparing 3/200 (current year) to 2/150 (last year) using a two-proportion exact test: p = 0.71. With counts this small, the test has almost no statistical power. Even if the true rate had doubled, there is only a 10–15% chance the test would detect it. The non-significant result is not reassuring evidence that the rate is stable; it is evidence that we cannot detect change at this sample size.

### Where the Frequentist Approach Strains: The Winner's Curse

Before introducing the Bayesian solution, let us address a deeper problem that sparse data creates for frequentist inference — one that the hospital example does not fully illustrate but that appears consistently in published research.

When studies are underpowered — when sample size is small relative to the true effect size — a specific statistical bias emerges at publication. Gelman and Carlin (2014) named its components:

- **Type S error (sign error):** the significant result points in the wrong direction. The true effect is positive, but you conclude negative, or vice versa.
- **Type M error (magnitude error):** the significant result is correct in direction but exaggerated in size. The true effect is 0.2, but you observe and report 0.8.

Why does this happen? When power is low, the only way a study clears the significance threshold ($p < 0.05$) by chance is with an unusually large observed effect. The significance threshold acts as a filter: studies that happen to draw an observation in the tail — one that overestimates the effect — are the ones that get published. Studies that draw a more typical observation — one that accurately reflects the small true effect — fail to reach significance and get filed away.

**A concrete illustration.** Suppose the true effect of an intervention is δ = 0.2 standard deviations (a small effect). A study with n = 20 per group has about 12% power to detect this effect at α = 0.05. Now suppose 1,000 researchers independently run this study. About 120 will get p < 0.05. What do those 120 studies find? Not δ = 0.2. They find effects around δ = 0.8 — four times the true size — because that is the threshold effect size needed to cross the significance bar at n = 20. The 880 studies that accurately estimated the small effect are never published.

The consequence: a reader who sees only the published literature finds a false consensus. The intervention "works" at δ = 0.8. When a larger, well-powered replication is run, it finds δ = 0.2 — and is dismissed as a "failure to replicate" even though it found the truth.

This is not research misconduct. It is the mathematical consequence of applying a significance threshold when power is low. The Bayesian framing is clarifying: Ioannidis (2005) showed using precisely this logic that when the prior probability of a true effect is low and power is also low, the majority of significant findings in a literature are false positives. The winner's curse is the magnitude analog: even among the real effects, their published magnitudes are systematically inflated.

The Open Science Collaboration (2015, *Science*, 349: aac4716 [verify citation details before citing]) provided empirical confirmation: 61 of 100 published psychology findings failed to replicate under well-powered conditions. Gelman and Carlin's framework provides the statistical mechanism for why this was the expected outcome, not a scandal. [verify citation]

**What this means for the hospital case:** the year-over-year comparison is low-powered. A non-significant result from a low-powered test is nearly uninformative. Reporting "no significant change" as reassurance to the hospital board misuses the test's output.

---

## The Bayesian Solution: Importing Prior Knowledge

### Setting Up the Beta-Binomial Model

The complication rate $p$ is a probability: it lives between 0 and 1. The natural prior for a probability is a **Beta distribution**, written Beta$(α, β)$. Its parameters encode prior knowledge in a directly interpretable way: $α$ represents "prior successes" (complications) and $β$ represents "prior failures" (no complication). The prior mean is $α/(α + β)$.

The data follow a **Binomial distribution**: 3 complications in 200 procedures. The Beta distribution is conjugate to the Binomial, meaning the posterior is also a Beta distribution — the update is closed-form arithmetic.

**The update rule:**
$$\text{Prior: Beta}(\alpha_0, \beta_0) \quad + \quad \text{Data: } k \text{ successes in } n \text{ trials}$$
$$\text{Posterior: Beta}(\alpha_0 + k, \, \beta_0 + n - k)$$

The posterior is just the prior with the observed data added in.

### Constructing the Prior from Published Literature

Published literature on laparoscopic appendectomy complication rates suggests that well-resourced regional hospitals typically see rates between 1% and 2.5%, with a central tendency around 1.5%. To encode a prior centered on 1.5% with moderate confidence, we specify:

$$\text{Prior: Beta}(3, 200)$$

This prior encodes: "Before seeing this hospital's data, I believe the complication rate is distributed around 3/(3+200) = 1.47%, with uncertainty roughly consistent with having seen ~3 complications in ~200 procedures of prior experience."

Is this prior too tight? Too loose? Prior sensitivity analysis — which we will run — addresses this.

### Computing the Posterior

With k = 3 complications in n = 200 procedures:

$$\text{Posterior} = \text{Beta}(3 + 3, \, 200 + 200 - 3) = \text{Beta}(6, 397)$$

**Posterior mean:** $6/(6 + 397) = 6/403 \approx 0.0149 = 1.49\%$

**Posterior mode:** $(6-1)/(403-2) = 5/401 \approx 1.25\%$

**95% Credible Interval:** [0.55%, 3.18%] — computed from the Beta(6, 397) distribution

**P(p < 2.5% | data):** The posterior probability that the true complication rate is below the accreditation threshold. This is directly computable from the Beta(6, 397) CDF. The answer is approximately 0.92 — about 92% probability the hospital is within acceptable limits.

Compare to the frequentist output:

| | Frequentist (exact binomial) | Bayesian (Beta-Binomial) |
|---|---|---|
| Estimate | 3/200 = 1.50% | Posterior mean = 1.49% |
| 95% interval | [0.31%, 4.35%] | [0.55%, 3.18%] |
| Interval width | 4.04 percentage points | 2.63 percentage points |
| P(rate < 2.5%)? | Not directly available | 0.92 |
| Prior used | Implicit flat | Beta(3, 200) from published literature |

The Bayesian interval is meaningfully tighter. The point estimates are nearly identical. The probability statement — 92% confidence the rate is below threshold — is directly usable by the committee.

### Bayesian Shrinkage: What It Is and What It Costs

The key mechanism is **shrinkage**: the Bayesian posterior pulls the estimate toward the prior mean. With only 3 events, the observed rate (1.5%) and the prior mean (1.47%) happen to be very close here, so the shrinkage is minimal. If the hospital had observed 8 complications in 200 procedures (4%), the posterior under the same prior would shrink that estimate toward 1.5% — producing a posterior mean around 2.2%, not 4%.

Is this appropriate? It is appropriate when the prior reflects genuine knowledge about the distribution of complication rates across similar hospitals. The published literature supports the prior: most comparable hospitals see rates in the 1–2.5% range, not 4%. Shrinking toward that distribution is the correct inference when you believe this hospital is typical.

It is *not* appropriate when:
- The prior is mis-specified — if this hospital has substantially different patient risk profiles than the hospitals used to construct the prior, shrinking toward the published mean imports bias.
- The true rate is genuinely an outlier — if this hospital is genuinely worse (or better) than the typical hospital, Bayesian shrinkage will be slower to detect that.

This is the honest cost. Bayesian shrinkage helps when the prior is well-matched. It hurts when it isn't. There is no free lunch.

### Prior Sensitivity Check

What if the prior is wrong? Run the analysis under alternatives:

- **Beta(1, 100):** Prior centered at ~1.0%, weaker prior confidence. Posterior: Beta(4, 297), mean ≈ 1.33%, 95% CrI ≈ [0.36%, 3.39%].
- **Beta(5, 300):** Prior centered at ~1.64%, stronger prior confidence. Posterior: Beta(8, 497), mean ≈ 1.58%, 95% CrI ≈ [0.68%, 3.08%].
- **Beta(1, 1):** Flat prior (effectively non-informative). Posterior: Beta(4, 198), mean ≈ 1.98%, 95% CrI ≈ [0.54%, 4.99%] — nearly the same as the frequentist CI.

The posterior mean across priors ranges from ~1.3% to ~2.0%. The 95% CrI ranges from fairly wide (with the flat prior) to reasonably tight (with the informative prior). The qualitative conclusion — the rate is probably within acceptable limits — is robust across all three informative priors. The flat-prior posterior is wider and matches the frequentist CI.

---

## Side-by-Side Comparison

| | Frequentist (exact binomial) | Bayesian (Beta-Binomial, informative prior) |
|---|---|---|
| Estimate | 1.50% (MLE) | 1.49% (posterior mean) |
| 95% interval | [0.31%, 4.35%] | [0.55%, 3.18%] |
| P(rate < threshold)? | Not available | Directly computable |
| Year-over-year change | p = 0.71 (insufficient power) | Posterior on change, P(improved) = direct |
| Winner's curse risk | High in underpowered comparisons | Shrinkage reduces magnitude inflation |
| Prior required? | No (implicit flat) | Yes — from published literature |
| Cost of prior | None declared | Risk of bias if prior is mis-specified |

**Why anyone uses frequentist methods for sparse data:** In a genuinely novel procedure — no published complication rate benchmarks, no prior experience with this technique — the frequentist analysis does the right thing: it reports a wide interval and a non-significant trend. "The data are too sparse to conclude anything" is sometimes the honest scientific answer, and the frequentist machinery makes that sparsity visible rather than smoothing it with an unsupported prior. A hospital using a Bayesian prior derived from the wrong comparison population could get a misleadingly tight posterior — false precision rather than honest uncertainty.

---

## Worked Example: Small Study, Large Reported Effect

**Situation.** A sports medicine researcher publishes a study with n = 18 athletes (9 per group). The intervention is a new warm-up protocol. The outcome is knee injury rate over a season. The treatment group has 0 injuries; the control group has 3. The researcher reports a risk reduction of 100% (3/9 vs. 0/9), p = 0.07 under Fisher's exact test (not significant). A colleague runs a Bayesian analysis and finds this compelling.

Should the sports medicine community adopt the new protocol?

**Process.**

*Step 1: Frequentist assessment.* p = 0.07 — not significant. With 9 athletes per group and only 3 events total, the study has approximately 15% power to detect a true 50% risk reduction. Under these conditions, most significant results would reflect the winner's curse.

*Step 2: Type M and Type S error analysis (Gelman & Carlin 2014).* Using the retrodesign framework: if the true risk reduction is 30% (a plausible prior assumption for a warm-up change), and power is 15%, the expected Type M exaggeration ratio is approximately 3.5×. Published "significant" results from this study design would, on average, overstate the true effect by 3.5 times. The 100% risk reduction is likely a substantial overestimate even if the direction is correct.

*Step 3: Bayesian analysis with an informative prior.* Prior knowledge suggests that warm-up interventions for injury prevention typically reduce injury rates by 20–40%. Encoding this as a Beta prior centered on a 30% reduction, the Bayesian posterior given 0/9 vs. 3/9 gives a credible interval spanning [3%, 75%] for the true risk reduction — wide, reflecting the sparse data. The posterior probability of a "clinically meaningful" reduction (> 25%) is about 0.58. Interesting, but not compelling.

*Step 4: Identify the dead end.* The researcher initially interpreted the Bayesian result as endorsing the protocol (P > 50% that it works!). This was an overreading: 58% posterior probability is barely above chance, and the prior did substantial work in generating that 58%. Under a flat prior, P(reduction > 25%) ≈ 0.42.

**Resolution and lesson:** Both approaches correctly indicate that the evidence is insufficient to adopt a policy change. The frequentist result (p = 0.07) says this directly. The Bayesian result, when read honestly, says the same thing: prior knowledge of warm-up effects combined with these sparse data yields weak evidence. The winner's curse analysis explains why the reported 100% reduction is almost certainly inflated.

**Limit:** Neither approach tells the researcher whether to run a larger study. That is a decision under resource constraints, which requires information about costs, the plausibility of the effect, and the cost of injury — not statistical analysis alone.

---

## Prompting for Implementation

### A well-formed prompt for sparse count data

```
I have sparse count data from a hospital quality improvement project:
- Current year: 3 complications in 200 procedures
- Last year: 2 complications in 150 procedures
- Accreditation threshold: complication rate < 2.5%

Please:
1. Run a frequentist exact binomial analysis of the current year's data.
   Report the MLE point estimate and exact 95% confidence interval.
2. Run a frequentist two-proportion exact test comparing this year to last year.
   Report p-value and note the statistical power for this test.
3. Build a Bayesian Beta-Binomial model with an informative prior Beta(3, 200) 
   based on published complication rates for this procedure type.
   Report the posterior: mean, 95% credible interval, and P(rate < 0.025 | data).
4. Run a prior sensitivity analysis: repeat step 3 with Beta(1,1) (flat), 
   Beta(1,100) (weaker informative), and Beta(5,300) (stronger informative).
   Show how the posterior mean and interval change.
5. Explain in plain language: what does the Bayesian analysis tell the hospital 
   committee that the frequentist analysis cannot? What assumption is it making?

Show all mathematical steps. Do not just report code output — show the 
posterior parameters explicitly (e.g., "Posterior is Beta(6, 397)").
```

### What to verify

- The posterior parameters should satisfy the conjugate update rule: Beta(α₀ + k, β₀ + n − k). Check this arithmetic directly.
- The posterior mean should be a weighted average between the prior mean and the sample proportion. With an informative prior, it should be pulled toward the prior. If it's farther from the prior mean than the sample proportion is, the model is wrong.
- P(p < 0.025 | data) should be computable from the Beta CDF. Ask the LLM to show the computation, not just the result.
- The flat-prior Bayesian result should closely match the frequentist exact CI. If it doesn't, ask why.

---

## Common Misconceptions

**Misconception 1: "Bayesian methods always give better estimates than frequentist methods for small samples."**

Bayesian shrinkage improves estimates when the prior captures real prior knowledge. When the prior is wrong — centered on the wrong value, or too tight — shrinkage pulls the estimate in the wrong direction and can be worse than the honest-but-noisy frequentist estimate. A hospital with an unusual patient population that uses a prior derived from general hospitals may get a misleadingly precise posterior. There is no free improvement.

**Misconception 2: "A non-significant result from a small study means the effect is probably small."**

A non-significant result from a low-powered study means almost nothing. When power is 15%, a non-significant result occurs 85% of the time regardless of whether the true effect is zero or large. The information content of p = 0.7 from a study with 15% power is very low — it is consistent with no effect and consistent with a moderate effect. The correct interpretation is not "the effect is probably small" but "the study cannot distinguish between no effect and a moderate effect." These are very different statements.

**Misconception 3: "The winner's curse is a problem with publication bias, not with statistics."**

Publication bias — the tendency to publish significant results and file non-significant ones — amplifies the winner's curse. But Gelman and Carlin (2014) demonstrated that even without selective publication, the statistical mechanism of a significance threshold combined with low power produces inflated effect size estimates among the significant results. The winner's curse exists in single studies (where the observed effect overstates the true effect when that study happened to be lucky), not just across literatures. Publication bias makes it worse; low power makes it exist.

---

## AI Wayback Machine: Persi Diaconis (born 1945)

---

*Intuitions about small numbers are reliably wrong. Few people have thought harder about why — or how to correct them.*

---

Persi Diaconis left home at 14 to apprentice with the sleight-of-hand magician Dai Vernon, traveling across America for nearly a decade performing card magic. He returned to formal education at 24, earned a PhD in mathematical statistics from Harvard, became a MacArthur Fellow in 1982, and is now the Mary V. Sunseri Professor of Statistics and Mathematics at Stanford.

The connection between magic and statistics is not accidental. A magician's livelihood depends on exploiting the audience's faulty intuitions about randomness. Diaconis's mathematical career has been substantially organized around formalizing those failures: how many times must you shuffle a deck of cards before it is random (seven riffle shuffles, he proved with Dave Bayer)? Why do people see patterns in noise — runs, streaks, clustering — and infer structure where none exists?

Small samples amplify this problem. Three complications in 200 procedures looks like a pattern. Two complications last year, three this year — looks like a trend. Both judgments outrun what the data can support. Diaconis's contributions to the mathematics of randomness provide the rigorous foundation for why: the human visual system and intuitive probability sense were shaped by evolutionary pressures, not by statistical training. We see signal in noise because false positives were rarely fatal; false negatives (failing to see the tiger) sometimes were.

Bayesian shrinkage is, in part, a formal mechanism for correcting exactly this overfit to noise: by pulling estimates toward a prior mean derived from broader experience, the analysis resists the local fluctuations that our pattern-detection machinery will otherwise over-interpret.

*Anchor for student reflection:* "You are Persi Diaconis, teaching a student who has just learned that winner's curse means significant findings in small studies are probably inflated. The student says: 'How do we develop good intuitions about rare events when our brains are wired to see patterns everywhere?' What do you tell them?"

---

## Exercises

**Exercise 1 (Apply — both frameworks).** A rare disease affects 0.1% of a regional population. A hospital's oncology unit sees 500 patients over two years and records 1 new case.

(a) Compute the frequentist MLE estimate and exact 95% confidence interval for the disease rate in this patient population.

(b) Specify a Beta prior based on the known population rate of 0.1% (encode this as Beta(1, 999) as a starting point). Compute the posterior and report the mean and 95% credible interval.

(c) Compare the two intervals. What does the Bayesian analysis gain, and at what cost?

(d) The hospital administrator wants to know: "Is our rate consistent with the regional background rate?" Which approach can answer this directly? Compute the answer.

**Exercise 2 (Analyze — winner's curse).** A nutrition researcher publishes a study with n = 20 participants per group. The intervention is a dietary supplement. The study reports a statistically significant effect on a blood biomarker: p = 0.04, Cohen's d = 0.82 (a "large" effect by convention). A pre-registered replication with n = 200 per group finds p = 0.06, d = 0.21.

(a) Using the winner's curse framework (Gelman & Carlin 2014), explain what likely happened between the original study and the replication. Identify the roles of sample size and significance filtering.

(b) Which estimate of the effect size — 0.82 or 0.21 — is more likely to be close to the truth? Justify your answer.

(c) A meta-analyst wants to combine both studies. What consideration about effect size inflation should they apply to the original study's estimate?

**Exercise 3 (Evaluate — when does Bayesian shrinkage help and when could it mislead?).** Consider two hospitals using Bayesian Beta-Binomial analysis to monitor a surgical complication, both using the same prior Beta(3, 200) based on published rates.

Hospital A performs 1,500 procedures per year and observes 18 complications (1.2%).

Hospital B performs 80 procedures per year and observes 6 complications (7.5%) — a small, specialized unit performing high-risk cases.

(a) Compute the posterior mean and 95% CrI for each hospital under the shared prior.

(b) For Hospital A, is Bayesian shrinkage toward the prior mean appropriate? Why?

(c) For Hospital B, is Bayesian shrinkage toward the same prior mean appropriate? What additional information would you need to evaluate this?

(d) Write a one-paragraph policy recommendation for Hospital B's committee that accurately represents what the data and analysis can and cannot tell them.

---

## What Would Change My Mind

1. **If the prior construction problem turned out to be tractable.** The hardest part of the Bayesian sparse-data analysis is identifying a defensible prior. If systematic tools for extracting priors from published literature — meta-analysis, expert elicitation, prior predictive checking — became standard workflow, the "prior is hard to specify" objection would weaken. Current practice is inconsistent.

2. **If replication rates in psychology and medicine improved substantially.** The winner's curse argument draws much of its force from the documented replication failures of the 2010s. If pre-registration, power analysis, and replication norms substantially reduced these failures, the case that underpowered studies produce systematically inflated estimates would need to be qualified temporally: "this was a problem through the mid-2020s; the field has since corrected it."

3. **If Bayesian adaptive trial designs produced worse outcomes than frequentist trials.** Rare disease trials using Bayesian priors from adult data to inform pediatric trials (e.g., FDA-approved adaptive designs) represent a growing empirical record. If this record showed that imported priors regularly produce worse regulatory decisions than frequentist analysis with honest uncertainty, the case for Bayesian shrinkage in small samples would be substantially weakened.

---

## Still Puzzling

1. The winner's curse shows that published significant effects from underpowered studies are inflated. The correct response is to run larger studies. But resource constraints are real, and for rare diseases or rare events, large studies may be infeasible. Is there a principled way to decide when Bayesian shrinkage is "good enough" to act on sparse evidence without waiting for a well-powered study?

2. Bayesian shrinkage is equivalent to regularization (L2 penalty / ridge regression) in the non-hierarchical case. This connection is mathematically clean. But the interpretation differs: regularization is a computational trick to prevent overfitting; Bayesian shrinkage is a claim about prior probabilities. Are these actually the same thing, or does the interpretation matter for how we should evaluate the approach?

3. The hospital example uses a prior from published complication rates. But published rates are themselves estimates from previous studies — which also have uncertainty and their own potential for winner's curse inflation. At what point does using prior literature stop being "importing knowledge" and start being "inheriting someone else's inflated estimates"?

---

## Bridge to Chapter 9

Sparse data at the observation level is one challenge. Chapter 9 introduces a different kind of sparsity: data with natural grouping structure, where some groups have many observations and some have very few. A school district with 30 schools, some with 200 students tested and some with only 8, faces exactly this problem.

The solution — borrowing strength across groups — is Bayesian shrinkage applied hierarchically. Each group's estimate is pulled toward the group-level mean, with the amount of pulling calibrated automatically by how sparse the group's data are. Small groups shrink more; large groups retain their own data.

Chapter 9 is the hardest chapter in the book. It is also where the Bayesian approach earns its complexity cost most directly — and where the frequentist alternative, the mixed-effects model, partially replicates the shrinkage but cannot fully propagate the uncertainty about how much to shrink.

---

*Sources: Gelman & Carlin (2014); Ioannidis (2005); Clayton (2021) [framing only; not a primary research source]; Gelman, Carlin, Stern, Dunson, Vehtari & Rubin (2013); Open Science Collaboration (2015) [verify citation: Science, 349:aac4716]; James & Stein (1961) [verify proceedings details: "Estimation with Quadratic Loss," Proceedings of the Fourth Berkeley Symposium on Mathematical Statistics and Probability]; PMC5391146 (surgical site infection monitoring, Bayesian network); PMC9713380 (GWAS winner's curse); Osthus et al. (2021).*
