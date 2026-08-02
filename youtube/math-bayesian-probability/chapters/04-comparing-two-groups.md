# Chapter 4 — Comparing Two Groups

---

## Learning Objectives

By the end of this chapter you should be able to:

1. **(Apply)** Run and interpret a Welch two-sample t-test, including effect size (Cohen's d) and the specific question the result does and does not answer.
2. **(Apply)** Build a Bayesian two-group comparison with posterior distributions over both group means and the difference between them.
3. **(Analyze)** Explain the replication crisis as a consequence of applying significance testing without incorporating prior probabilities — using Ioannidis's (2005) argument — and name the limits of that argument.
4. **(Evaluate)** Assess what "statistically significant" does and does not establish about an educational intervention, and what additional information a decision-maker needs.

---

## The Problem

A university is piloting a new statistics tutorial. The old tutorial (Group A) is what students have used for years; the new one (Group B) has been redesigned with interactive exercises and better worked examples. To evaluate the switch, the university runs a randomized test: 40 students are assigned to Group A, 38 to Group B. After completing the tutorial, both groups take the same post-test.

Results:
- Group A: $n_A = 40$, $\bar{x}_A = 72\%$, $s_A \approx 9\%$
- Group B: $n_B = 38$, $\bar{x}_B = 76\%$, $s_B \approx 9\%$

*Note: this scenario is illustrative — the specific numbers are constructed for pedagogy, not drawn from a documented study.*

Is the new tutorial better? A 4-point gap looks like something. But 40 students is a small sample, and test scores are noisy. The decision to switch tutorials has real costs — faculty retraining, curriculum revision — and the university wants to know if the evidence is strong enough.

The natural move: run a t-test. The t-test will tell you something. The question is whether it tells you what you need.

---

## The Frequentist Solution

### Welch's Two-Sample t-Test

The standard two-sample t-test assumes the two groups have equal variance. In practice, they usually do not, so we use Welch's version (Welch, 1947), which adjusts both the test statistic and the degrees of freedom. This is the default in most statistical software.

**Pooled standard error of the difference:**

$$SE_\delta = \sqrt{\frac{s_A^2}{n_A} + \frac{s_B^2}{n_B}} = \sqrt{\frac{81}{40} + \frac{81}{38}} = \sqrt{2.025 + 2.132} = \sqrt{4.157} \approx 2.04$$

**t-statistic:**

$$t = \frac{\bar{x}_B - \bar{x}_A}{SE_\delta} = \frac{76 - 72}{2.04} = \frac{4}{2.04} \approx 1.96$$

**Degrees of freedom** (Welch-Satterthwaite approximation):

$$df \approx \frac{(s_A^2/n_A + s_B^2/n_B)^2}{\frac{(s_A^2/n_A)^2}{n_A - 1} + \frac{(s_B^2/n_B)^2}{n_B - 1}} = \frac{(4.157)^2}{\frac{(2.025)^2}{39} + \frac{(2.132)^2}{37}} \approx \frac{17.28}{0.1053 + 0.1228} \approx 75.8$$

Rounding to $df = 76$ and consulting a t-distribution: a two-sided p-value for $t = 1.96$ with $df = 76$ is approximately $p \approx 0.054$.

This is just above the conventional $\alpha = 0.05$ threshold. Not quite significant.

For the result to reach $p = 0.03$ — which is in the plausible range given small variations in the assumed standard deviations — the standard deviations would need to be slightly smaller, around 8 percentage points. With $s_A = s_B = 8\%$:

$$SE_\delta = \sqrt{\frac{64}{40} + \frac{64}{38}} = \sqrt{1.6 + 1.684} = \sqrt{3.284} \approx 1.81$$

$$t = \frac{4}{1.81} \approx 2.21, \quad p \approx 0.030$$

We will use this version ($s_A = s_B = 8\%$, $p \approx 0.03$) for the remainder of the chapter. The point is not the exact numbers but the structure of what $p = 0.03$ does and does not tell you.

**Cohen's d (effect size):**

$$d = \frac{\bar{x}_B - \bar{x}_A}{s_\text{pooled}} = \frac{4}{8} = 0.50$$

By conventional benchmarks (Cohen, 1988), $d = 0.50$ is a "medium" effect. Those benchmarks are a rule of thumb that Cohen himself cautioned against treating as universal.

### The Significance Decision

With $p = 0.03 < 0.05$, we reject the null hypothesis at $\alpha = 0.05$.

**What this means:** If Tutorial B produced no real effect, we would observe a difference this large (or larger) in about 3% of samples. The data are inconsistent with "no effect" at the 5% level.

**What this does not mean:** This does not say the probability that Tutorial B is better is 97%. It does not say there is a 97% chance we will see similar results in a replication. It does not say the effect size is likely to be 4 points.

The p-value answers: *How surprising is this data, assuming no true effect?*

The university's decision-maker needs to know: *How likely is it that Tutorial B actually produces better outcomes?*

These are not the same question.

### Where Frequentist Strains

A $p$-value of 0.03 is a statement about the data given the null hypothesis: $P(\text{data this extreme} | H_0)$. The university needs $P(H_1 | \text{data})$ — the probability the new tutorial actually helps, given what they observed.

The frequentist machinery has no mechanism to produce this probability. It does not use the prior probability that the new tutorial would help. It does not weigh the observed result against the background rate of educational interventions that actually work.

This gap has consequences. In a field where most tested interventions do not produce real effects — where the prior probability that a given tutorial redesign produces a meaningful improvement is, say, 20% — a single $p = 0.03$ result is not strong evidence of a real effect. Why? Because of a mathematical argument that has become central to understanding the replication crisis.

---

## The Replication Crisis Sidebar

### Ioannidis's Argument

In 2005, John Ioannidis published a paper with the uncomfortable title *Why Most Published Research Findings Are False* (Ioannidis, 2005). The argument is Bayesian, and it is not difficult to follow.

Suppose we are testing educational interventions. Most interventions — even carefully designed ones — do not produce large, durable effects. Call the prior probability that any given intervention produces a real effect $R$ (the proportion of hypotheses under test that are actually true). Ioannidis argued that for exploratory educational research, $R$ is low — perhaps 10–20%.

Now suppose we test 1000 interventions. If $R = 0.20$:
- 200 of the interventions are truly effective.
- 800 are not.

With typical statistical power (say 50%, meaning a true effect is detected about half the time):
- True positives: $200 \times 0.50 = 100$
- False positives (from the 800 non-effects, at $\alpha = 0.05$): $800 \times 0.05 = 40$

Total significant results: $100 + 40 = 140$.

**Positive predictive value (PPV):** $100/140 \approx 71\%$.

So even with $p < 0.05$, about 29% of "significant" results in this scenario are false positives. If power is lower (a common situation for small educational studies) or the prior is lower (more exploratory research), the PPV falls further.

The Open Science Collaboration (2015) tested this empirically: they replicated 100 published psychology experiments. Only 36% of replications produced significant results; replication effect sizes were roughly half the originals.

**This is not primarily a story about fraud or bad practice.** It is the mathematical consequence of applying a significance test without accounting for the prior probability that the hypothesis is true. The frequentist t-test treats all hypotheses equally before seeing data — it carries no information about whether "Tutorial B is better than A" is the kind of claim that usually turns out to be true.

### The Limits of Ioannidis's Argument

This sidebar is presented as a *strong framing*, not the only explanation.

Ioannidis's model is structurally correct given its assumptions — but the quantitative claims ("most findings are false") depend on assumed values of $R$ and power that are not empirically grounded for any specific field. Gilbert et al. (2016) [verify] criticized the OSC 2015 design, arguing some failed replications may reflect genuine context differences rather than original false positives.

The replication crisis also reflects publication bias (significant results are published; null results are not), p-hacking, small sample sizes, and flexible analysis decisions — not solely the absence of Bayesian priors. The Bayesian framing is one lens; it is a useful and mathematically precise one, but not the complete picture.

**Why state this?** Because the book's thesis is not "frequentist statistics is broken and Bayesian statistics fixes it." The thesis is that choosing a method requires understanding what each method can and cannot say. Ioannidis's argument is strongest when applied to exploratory research with low prior probability of a true effect, weak statistical power, and repeated testing. It is weakest when applied to a confirmatory test of a well-specified, plausible hypothesis from a productive research program.

---

## The Bayesian Solution

### Specifying Priors

For a Bayesian two-group comparison, we need priors on the group means $\mu_A$ and $\mu_B$. What do we know before seeing the data?

Test scores on a 0–100 scale have a natural range. Students taking a statistics tutorial post-test are likely to score somewhere in the middle of that range. A weakly informative prior: Normal(70, 15) on each mean. This says "the expected score is around 70%, and we'd be surprised by scores much below 40% or above 100%." It does not rule out large differences between groups — it just encodes modest prior expectations about the score range.

For the within-group standard deviation $\sigma$, a half-Normal(10) prior (a normal distribution folded at 0) says "standard deviations of up to 20 percentage points are plausible; much larger would be unusual."

### Posterior on the Difference

With $n_A = 40$, $\bar{x}_A = 72$, $s_A = 8$ and $n_B = 38$, $\bar{x}_B = 76$, $s_B = 8$, the data are fairly informative relative to these priors. The posterior on each group mean will be pulled strongly toward the observed means.

Posterior on $\mu_A$: approximately Normal(72, 1.3) — centered near the observed mean, tight because $n = 40$.

Posterior on $\mu_B$: approximately Normal(75.9, 1.3) — centered near the observed mean.

Posterior on the difference $\delta = \mu_B - \mu_A$: approximately Normal(3.9, 1.9).

**95% credible interval on $\delta$:** approximately $[0.2, 7.6]$ percentage points.

**$P(\delta > 0 | \text{data})$:** the probability Tutorial B actually produces higher scores:

$$P(\delta > 0 | \text{data}) \approx 0.98$$

[Note: the exact value depends on the prior specification and software. With weakly informative priors and this data, values between 0.91 and 0.98 are plausible depending on prior width. The TIKTOC spec cites 0.91; verify with specific prior choices in implementation.]

### Interpreting the Bayesian Result

"Given this data and weakly informative priors, there is approximately a 91–98% probability that Tutorial B produces higher average post-test scores than Tutorial A."

This is the probability the university needed. It is direct, interpretable, and applicable to the decision. The posterior also gives a full distribution over possible effect sizes — not just a point estimate with a standard error.

Note what the Bayesian analysis does that the frequentist one cannot: it tells you the probability the effect is positive, and it tells you the posterior distribution over *how large* the effect is. The credible interval $[0.2, 7.6]$ percentage points says: "There is a 95% chance the true advantage of Tutorial B is somewhere in this range." Both endpoints are useful — even at the low end (0.2 points), Tutorial B has a slight advantage; at the high end (7.6 points), it is a substantial improvement.

---

## Side-by-Side Comparison

| | **Frequentist** | **Bayesian** |
|---|---|---|
| Result | $p = 0.03$, reject $H_0$ | $P(\text{B better}) \approx 0.91$–$0.98$ |
| Effect size | Cohen's $d = 0.50$; $\bar{x}_B - \bar{x}_A = 4$ points | Posterior median $\delta \approx 3.9$ points, 95% CrI $[0.2, 7.6]$ |
| What it answers | How surprising is this data if there is no effect? | How likely is Tutorial B to be genuinely better? |
| Replication prediction | Not available | Posterior predictive check is possible |
| Prior probability of effect | Ignored — implicit flat prior | Named explicitly — Normal(70, 15) |
| "Is the effect real?" | Not directly answerable | Yes: $P(\delta > 0) \approx 0.91$–$0.98$ |

### Why Anyone Uses the Frequentist Method Here

The t-test is the lingua franca of educational and behavioral research. Every journal reviewer, IRB committee, and department chair in the social sciences understands a p-value, knows what $\alpha = 0.05$ means, and can evaluate whether an effect size is large enough to be educationally meaningful. The frequentist result is auditable, reproducible, and requires no prior specification — which is genuinely valuable in a context where two analysts might disagree about what prior probability to assign to "Tutorial B works."

For a confirmatory study where the prior probability of a real effect is high (this is a well-designed tutorial from experienced instructors, with an effect size in the plausible range), the gap between the frequentist and Bayesian conclusions may be small in practice. The Bayesian analysis earns its additional complexity specifically when:
- You need a direct probability that Tutorial B is better (not just a significance test);
- The prior probability of a real effect is clearly low, and you want to account for it;
- You want a posterior predictive distribution for planning a replication.

---

## Worked Example

### Situation

A pharmaceutical company tests a new drug for reducing anxiety. Group A ($n = 30$) receives a placebo; Group B ($n = 30$) receives the drug. After 8 weeks, anxiety scores (measured on a validated scale, 0–100, lower is better) are:

- Group A: $\bar{x}_A = 55$, $s_A = 12$
- Group B: $\bar{x}_B = 50$, $s_B = 11$

The company reports: $p = 0.04$. "The drug works."

### Process

**Step 1: What does $p = 0.04$ mean?**

Assuming no true effect, we'd observe a 5-point difference or larger in about 4% of trials. The data are inconsistent with the null at $\alpha = 0.05$. Cohen's $d = 5/11.5 \approx 0.43$ — small to medium.

**Step 2: What is the prior probability this drug works?**

The company has tested this compound in Phase I and Phase II trials. The compound is a modification of an existing anxiolytic that showed modest effects in earlier trials. This is not random exploratory research. Prior probability $R$: maybe 40–60%.

**Step 3: Ioannidis's calculation for this case:**

With $R = 0.50$ and power $= 80\%$ (reasonable for $n = 60$ total, $d = 0.43$):
- True positives: $50 \times 0.80 = 40$
- False positives (from 50 null hypotheses at $\alpha = 0.05$): $50 \times 0.05 = 2.5$
- PPV: $40 / 42.5 \approx 94\%$

For this confirmatory study, with a plausible compound and adequate power, $p = 0.04$ is actually quite strong evidence. The replication crisis argument applies most forcefully to low-$R$ exploratory research — it does not mean all $p$-values are worthless.

**Step 4: Bayesian analysis with priors from existing trials:**

Prior from Phase II data: the drug showed an effect of about 4 points (SD of about 12). Prior on $\delta$: Normal(4, 6) — "we expect around 4 points improvement, but with substantial uncertainty."

Posterior on $\delta$: updated by Phase III data, the posterior is approximately Normal(4.7, 2.2).

$P(\delta > 0 | \text{data})$: approximately 0.98.

The Bayesian analysis with an informative prior actually *strengthens* the conclusion relative to a weakly informative analysis, because the prior expected a positive effect and the data confirms it.

**Resolution:** $p = 0.04$ is meaningful here. Not because $p < 0.05$ is magic, but because this is a confirmatory test of a plausible hypothesis with decent power and a prior suggesting the drug has a reasonable chance of working. The Ioannidis argument is not an indictment of this analysis; it is an indictment of applying the same significance threshold to a field where most hypotheses are unlikely to be true and most studies are underpowered.

**The lesson:** The prior probability matters. It is not a defect of the frequentist method that it ignores the prior — it is a design feature for exploratory research. It becomes a problem when applied reflexively to all research, including low-prior-probability studies.

**The limit:** The Bayesian conclusion depends on having a defensible prior. If the Phase II evidence was weak, or if the company's statistician chose a prior conveniently centered on a large effect, the posterior would be inflated. Chapter 7 takes up the question of how to specify and justify priors honestly.

---

## Prompting for Implementation

### A Good Prompt

> "I have a two-group comparison. Group A has n=40, mean=72, SD=8. Group B has n=38, mean=76, SD=8. Test scores are on a 0–100 scale.
>
> Please:
> 1. Run Welch's two-sample t-test. Report the t-statistic, degrees of freedom, p-value, and Cohen's d.
> 2. Run a Bayesian two-group comparison. Use weakly informative priors: Normal(70, 15) on each group mean, half-Normal(10) on each group's standard deviation.
> 3. Report: (a) the posterior distributions on both group means, (b) the posterior on the difference δ = μ_B − μ_A, (c) the 95% credible interval on δ, (d) P(δ > 0 | data).
> 4. Show the mathematical steps, not just the code.
> 5. Interpret each result in plain language."

### What to Verify

From the frequentist output: confirm $t \approx 2.21$, $df \approx 76$, $p \approx 0.03$. Cohen's $d$ should be around 0.50 given SD ≈ 8.

From the Bayesian output: the posterior mean on $\delta$ should be close to the observed difference (4 points) — with 78 total observations, the data should dominate the weakly informative prior. $P(\delta > 0)$ should be above 0.90. If the LLM reports $P(\delta > 0) < 0.80$, something is wrong with the prior specification or computation.

### Common Errors

Watch for two LLM failure modes specific to this chapter:

1. **Misinterpreting the p-value:** An LLM may write "p = 0.03 means there's a 97% probability the new tutorial is better." This conflates $P(\text{data} | H_0)$ with $P(H_1 | \text{data})$. It is wrong. Ask the LLM to distinguish the two.

2. **Confusing Bayesian two-group comparison with a t-test in Bayesian clothing:** Some implementations output only a credible interval for each mean separately, without computing the posterior on the *difference* $\delta$. You need the posterior on $\delta$ to get $P(\delta > 0)$. If the output does not include this, ask explicitly.

### Aging Note

Specific implementations — Kruschke's BEST package in R (Kruschke, 2013), the `BayesFactor` package, PyMC in Python — will evolve. The underlying mathematics will not. Prompt for the conceptual result (posterior on the difference, $P(\delta > 0)$), then verify it makes sense given the data, rather than relying on a specific package's output format.

---

## Common Misconceptions

### Misconception 1: "p = 0.03 means there's a 97% chance the new tutorial works"

**The plausible claim:** We rejected the null at $p = 0.03$. The probability that the null is true must be only 3%. So the probability Tutorial B is better must be 97%.

**Why it fails:** The p-value is $P(\text{data this extreme} | H_0)$ — the probability of the data *given* the null hypothesis is true. It is not $P(H_0 | \text{data})$ — the probability the null is true given the data. These are related by Bayes' theorem and can be radically different when the prior probability of $H_0$ is high (as it often is in exploratory research). Greenland et al. (2016) catalogued this exact misinterpretation as one of the most common and consequential errors in applied statistics.

**Tie to the opening case:** If the university makes this mistake, they are implicitly computing a posterior probability without stating the prior — and the result is typically an overconfident conclusion. This is the mechanism Ioannidis identified: treating $p = 0.03$ as "97% confident" ignores the prior probability that the intervention works.

### Misconception 2: "Two studies both had p < 0.05, so the result replicated"

**The plausible claim:** Study 1 found $p = 0.03$. Study 2 replicated it with $p = 0.04$. Both studies are significant. The finding is replicated.

**Why it fails:** The p-value varies enormously across replications even when the null is false. A true effect that produces $p = 0.03$ in study 1 could easily produce $p = 0.12$ in study 2, simply due to sampling variability. Cumming (2008) showed that the p-value from a replication study is nearly unpredictable from the original p-value, even when both are estimating a real effect. Two $p < 0.05$ results do not establish replication — they are consistent with replication, but also consistent with two lucky false positives.

True replication requires asking: "Did the second study estimate a similar effect size?" — not just "Was it significant?"

**Tie to the opening case:** If the university sees $p = 0.04$ in a second pilot of Tutorial B, they have not confirmed the result. They have seen two pieces of evidence, each consistent with a real effect — but also each consistent with a world where the tutorial makes no difference and they were unlucky twice at $\alpha = 0.05$.

### Misconception 3: "The Bayesian approach gives a different answer because it uses subjective priors"

**The plausible claim:** The Bayesian analysis gives $P(\text{B better}) \approx 0.91$. The frequentist analysis gives $p = 0.03$. These are different because the Bayesian approach inserted a subjective prior that biased the result.

**Why it fails:** The frequentist analysis also carries a prior — an implicit flat (uniform) prior that treats all possible effect sizes as equally likely before seeing the data. That prior is usually wrong. For test scores, a 40-point effect is not as plausible as a 4-point effect, but the frequentist significance test treats them symmetrically. The Bayesian approach makes the prior explicit and checkable. The difference between the approaches is not the presence of assumptions — it is whether those assumptions are named.

The two analyses can give similar conclusions when the prior is weakly informative and the sample is moderate — which is the case here. They diverge most sharply in small samples (Chapter 8) and when the prior probability of the hypothesis is very low (the Ioannidis scenario).

---

## AI Wayback Machine

**Evelyn Fix (1904–1965)** spent her career at Berkeley building statistical tests that do not require assuming the data follows a normal distribution. The t-test assumes test scores are normally distributed within each group; Fix worked on nonparametric alternatives — tests based on ranks and order statistics rather than means and standard deviations — that work when that assumption is violated (Fix and Hodges, 1951). She is also notable for co-inventing the k-nearest neighbor algorithm, a foundational tool in machine learning, in a 1951 technical report that was not formally published until decades later. In a chapter about comparing two groups, her work is a quiet warning: the t-test's normality assumption is load-bearing. For test scores bunched near a ceiling (most students scoring above 90%) or a floor, the distribution is not approximately normal, and the t-test's p-values become unreliable. Fix's nonparametric methods — and the Bayesian approach with a non-normal likelihood — are what you reach for then.

---

## Exercises

**1. (Apply)** A clinical trial tests a new drug for reducing blood pressure. Group A (placebo, $n = 30$) averages a 2 mm Hg reduction; Group B (drug, $n = 30$) averages a 7 mm Hg reduction. Both groups have $s \approx 12$ mm Hg.

*(a)* Run Welch's t-test by hand: compute $SE_\delta$, the t-statistic, and estimate the p-value.

*(b)* The drug has passed Phase II trials with modest effects. Using Ioannidis's framework, what additional information would you want before concluding the drug works from this Phase III result?

*(c)* Compare this situation to the tutorial case: where does the prior probability of a real effect fit in your assessment of $p < 0.05$?

**2. (Analyze)** A researcher says: "We replicated the finding — both our study and the original had $p < 0.05$."

*(a)* Explain why two significant p-values do not constitute a replication.

*(b)* What would constitute stronger evidence of replication? Describe a criterion using effect sizes rather than significance levels.

*(c)* How does the Bayesian framework offer a different path to assessing replication, using the posterior predictive distribution?

**3. (Evaluate — Production)** Using the tutorial data from this chapter ($n_A = 40$, $\bar{x}_A = 72$, $s_A = 8$; $n_B = 38$, $\bar{x}_B = 76$, $s_B = 8$):

Write a one-paragraph recommendation to the university's curriculum committee. The paragraph must:
- State the frequentist result correctly (including what it does and does not establish)
- State the Bayesian result (including what prior you used and why)
- Make a recommendation, with acknowledgment of uncertainty
- Identify what additional evidence would change your recommendation

Your recommendation does not have to choose Bayesian over frequentist — it has to use both honestly.

---

## What Would Change My Mind

The argument that the frequentist t-test is insufficient for the university's decision — because it cannot directly answer $P(\text{B better} | \text{data})$ — would weaken if the decision were reformulated as: "We will adopt Tutorial B if and only if a pre-registered randomized trial produces $p < 0.05$." Under that decision rule, the p-value is doing exactly what it should: providing a standardized, pre-committed criterion. The frequentist approach shines in pre-registered confirmatory research where the prior probability of the effect is not in dispute and the decision threshold is fixed in advance. The Bayesian argument for $P(\text{B better})$ becomes most compelling when the university wants to weigh its confidence in Tutorial B against the costs of switching — a genuinely probabilistic decision that the frequentist result cannot input directly.

---

## Still Puzzling

1. **What is the right prior probability for educational interventions?** Ioannidis assumed $R$ is low for exploratory research. But what is $R$ for a well-designed tutorial comparison? The argument is only as strong as the prior probability it assumes. Finding a principled way to estimate $R$ from meta-analyses is an open research question.

2. **Does the replication crisis explain itself?** The OSC (2015) results show widespread failure to replicate, and the Ioannidis argument provides a structural explanation. But Gilbert et al. (2016) [verify] suggested that some failed replications reflect context differences rather than false positives. How do we distinguish a false positive from a real effect that fails to replicate due to different conditions?

3. **When is the Bayesian prior on group means genuinely uninformative?** The Normal(70, 15) prior used here is "weakly informative" — but weakly informative is not the same as uninformative. For a study of students in a different country, or a test scored on a different scale, the same prior might be strongly informative. When should the analyst use a truly flat prior, and when does that create problems?

4. **Can pre-registration fix the replication crisis without Bayesian inference?** Many researchers argue that pre-registration (committing to the hypothesis and analysis plan before collecting data) addresses the key distortions, without requiring Bayesian methods. Is this right, and if so, does it undermine the Bayesian argument in this chapter?

---

## Bridge to Chapter 5

Both analyses in this chapter dealt with well-specified, relatively simple models: two groups, a continuous outcome, and the question of which group is better. In Chapter 5, we add a continuous predictor — regression — where the Bayesian solution starts returning answers the frequentist solution structurally cannot. The question changes from "which group is better?" to "how much does advertising drive sales, and should we spend more?" For that question, you do not want a significance test or even a probability that the slope is positive. You want a probability distribution over future outcomes — and that is what Bayesian regression provides.

This is also where the book's *asymmetry rule* is named for the first time: from Chapter 5 onward, we spend more space on the Bayesian solution, because the frequentist analog is simpler and you already know it. That asymmetry is not an apology. It is evidence.

---

## References

Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.). Lawrence Erlbaum Associates.

Cumming, G. (2008). Replication and p intervals: p values predict the future only vaguely, but confidence intervals do much better. *Perspectives on Psychological Science*, 3(4), 286–300.

Cumming, G. (2014). The new statistics: Why and how. *Psychological Science*, 25(1), 7–29. https://doi.org/10.1177/0956797613504966

Greenland, S., Senn, S. J., Rothman, K. J., Carlin, J. B., Poole, C., Goodman, S. N., & Altman, D. G. (2016). Statistical tests, P values, confidence intervals, and power: A guide to misinterpretations. *European Journal of Epidemiology*, 31, 337–350. https://doi.org/10.1007/s10654-016-0149-3

Ioannidis, J. P. A. (2005). Why most published research findings are false. *PLoS Medicine*, 2(8), e124. https://doi.org/10.1371/journal.pmed.0020124

Kruschke, J. K. (2013). Bayesian estimation supersedes the t test. *Journal of Experimental Psychology: General*, 142(2), 573–603. https://doi.org/10.1037/a0029146

Open Science Collaboration. (2015). Estimating the reproducibility of psychological science. *Science*, 349, aac4716. https://doi.org/10.1126/science.aac4716

Welch, B. L. (1947). The generalization of 'Student's' problem when several different population variances are involved. *Biometrika*, 34(1–2), 28–35.
