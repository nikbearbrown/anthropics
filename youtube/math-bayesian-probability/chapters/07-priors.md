# Chapter 7 — Priors: Where Does Your Assumption Come From?

---

## Learning Objectives

By the end of this chapter you will be able to:

1. **(Analyze)** Identify the implicit prior assumptions in a standard frequentist t-test, and explain why calling the method "prior-free" is an oversimplification (Bloom: Analyze)
2. **(Apply)** Run the same Bayesian analysis under three different priors — uniform, weakly informative, and informative — and document what changes in the posterior (Bloom: Apply)
3. **(Evaluate)** Defend a prior choice using domain knowledge, pilot data, or principled ignorance, and explain when each justification is appropriate (Bloom: Evaluate)
4. **(Evaluate)** Assess when prior sensitivity matters for a conclusion and when it does not — and explain what to do in each case (Bloom: Evaluate)

---

## Opening Case: Same Data, Two Analysts, Two Conclusions

A biostatistician at a pharmaceutical company analyzes the results of a Phase III clinical trial. The treatment is a new antihypertensive drug. Forty patients were randomized to treatment or control; the primary outcome is the reduction in systolic blood pressure. The data show a mean reduction of 5.2 mmHg in the treatment group and 0.3 mmHg in the control group, a difference of 4.9 mmHg. The standard error of that difference is 2.3 mmHg.

She runs a two-sample t-test. The result is t = 2.13, p = 0.038. Significant at α = 0.05.

An independent statistician at the FDA reviews the same dataset. He is aware that this compound is structurally related to two other drugs in the same class that failed Phase III trials with null effects. He runs a Bayesian analysis incorporating that prior information. His conclusion: the posterior probability that the drug produces a clinically meaningful effect (defined as a reduction > 3 mmHg) is 0.41 — not compelling.

Both used valid statistical methods. Both looked at the same 40 patients. One concludes the trial succeeded; one concludes it didn't.

How is this possible?

The answer is priors — and what makes this chapter difficult is that *both analysts had priors*. One's was hidden. One's was explicit. Understanding that difference, and taking it seriously rather than dismissing it, is the work of this chapter.

---

## The Fairness Test: Why Frequentist Methods Have Real Advantages Here

Before we do anything else, let us state the frequentist position honestly.

Frequentist methods do not require prior specification. In the clinical trial example above, the t-test treats all possible true effect sizes as equally likely before seeing the data. This is itself a prior — but it is a *prespecified, non-negotiable, non-manipulable* prior. The analyst cannot choose it to favor their drug. The method is the same regardless of whether the researcher wants the trial to succeed or fail.

This is not a trivial advantage. Consider the alternative: a pharmaceutical company's statistician specifies an informative prior for their own drug, centered on a large positive effect, citing internal pilot data that has not been publicly reviewed. The Bayesian machinery then combines this convenient prior with the data and produces a posterior that looks convincing. The analyst has essentially weighted the scales. The prior has done work that the evidence should have done.

Regulators — including the FDA [verify: the 2026 FDA draft guidance on Bayesian clinical trials addresses prior construction, but its requirements and final status should be confirmed from fda.gov/media/190505/download before treating this as binding guidance] and the EMA [verify: the EMA's 2020 public consultation on Bayesian methods and its current regulatory language should be verified directly from ema.europa.eu before citing specific requirements] — have historically required frequentist analyses in confirmatory trials precisely because they are harder to game with convenient priors. The prespecification requirement in a registered clinical trial is the regulatory community's answer to the question "how do we prevent the analyst's choice of prior from determining the result?"

This is a *real* advantage of frequentist methods, not a strawman. In genuinely novel situations — a drug with no prior trials, a phenomenon observed for the first time — specifying a prior is genuinely difficult, because there is no evidence to draw on. In that setting, the implicit flat prior of the t-test is not dishonest: it is an admission that we don't know. Demanding an explicit prior when none can be reasonably justified imposes epistemic precision that the situation does not support.

The demand for explicit priors is a feature when knowledge exists. It is a burden when it doesn't.

---

## The Hidden Prior

With that fairness test established, let us look carefully at what "prior-free" actually means.

A two-sample t-test compares two group means under the model:

$$y_{ij} = \mu_j + \epsilon_{ij}, \quad \epsilon_{ij} \sim \text{Normal}(0, \sigma^2)$$

The t-test estimates $\mu_A$ and $\mu_B$ by their sample means and computes a test statistic for the null hypothesis $\delta = \mu_B - \mu_A = 0$. This is equivalent — in the mathematical sense — to fitting a Bayesian model with *flat (uniform) priors* on $\mu_A$, $\mu_B$, and $\sigma$.

What does a flat prior on $\delta$ actually say? It says: before seeing the data, all values of $\delta$ — a 1-mmHg reduction, a 100-mmHg reduction, a 50-mmHg increase — are equally plausible. For a drug that has failed two prior Phase II trials, this is a strong assumption. The drug might work. But the prior probability that it produces a 100-mmHg reduction is the same as the prior probability that it produces a 4.9-mmHg reduction. For a blood pressure drug, that is not neutrality — it is an implicit claim that enormous effects are just as likely as small ones.

Gelman (2006) and Gelman et al. (2008) formalized this argument: a prior that looks flat on the parameter scale is often not flat on the observable scale. A flat prior on a regression coefficient implies a prior that assigns substantial probability to implausibly large predictions. The issue is not whether you have a prior. The issue is whether you have *named* it.

The implication: "prior-free" does not mean "no prior." It means "implicit flat prior." Whether an implicit flat prior is an honest choice depends on the domain. For a genuinely novel situation, it may be the right choice. For a drug with a documented history of small or null effects, it is a choice that happens to favor the analyst who wants a significant result — it just doesn't look like one.

---

## The Bayesian Solution: Three Priors, Same Data

Let us run the clinical trial analysis three times, using three different priors on the true treatment effect $\delta$.

**The data (hypothetical worked example, illustrative numbers):** 40 patients, mean difference $\bar{d} = 4.9$ mmHg, standard error $\text{SE} = 2.3$ mmHg, degrees of freedom $= 38$. The sampling distribution of $\bar{d}$ is approximately Normal$(\delta, 2.3^2)$.

For each prior, we compute the posterior distribution of $\delta$ using Bayes' theorem:

$$P(\delta \mid \mathbf{y}) \propto P(\mathbf{y} \mid \delta) \cdot P(\delta)$$

where the likelihood $P(\mathbf{y} \mid \delta) \propto \text{Normal}(4.9, 2.3^2)$.

---

### Prior 1: Uniform (Flat) — "I Know Nothing"

$$P(\delta) \propto 1 \quad \text{(flat over all values)}$$

A flat prior places equal probability on every value of $\delta$ from $-\infty$ to $+\infty$. This is what the t-test implicitly uses.

**Posterior:** When the prior is flat, the posterior is proportional to the likelihood:
$$\delta \mid \mathbf{y} \sim \text{Normal}(4.9, 2.3^2)$$

**Posterior mean:** 4.9 mmHg. **95% credible interval:** [0.4, 9.4] mmHg.

**P(δ > 3 | data, Prior 1) ≈ 0.79.** About 79% probability of a clinically meaningful effect.

---

### Prior 2: Weakly Informative — "Large Effects Are Unlikely, But I'm Not Sure"

$$P(\delta) = \text{Normal}(0, 10^2)$$

This prior says: before seeing the data, I expect the effect is probably somewhere between −20 and +20 mmHg (within two standard deviations). Effects of ±30 mmHg or more are unlikely. This reflects general knowledge about the scale of blood pressure effects — not knowledge about this drug specifically.

**Posterior (conjugate Normal update):**
$$\delta \mid \mathbf{y} \sim \text{Normal}\left(\frac{4.9/2.3^2}{1/10^2 + 1/2.3^2}, \frac{1}{1/10^2 + 1/2.3^2}\right)$$

Working this through: precision from data = $1/2.3^2 \approx 0.189$; precision from prior = $1/100 = 0.01$; total precision $\approx 0.199$.

**Posterior mean:** $\approx 4.75$ mmHg. **95% CrI:** approximately [0.4, 9.1] mmHg.

**P(δ > 3 | data, Prior 2) ≈ 0.76.** Nearly identical to Prior 1 here, because the data are informative relative to the wide prior.

---

### Prior 3: Informative — "Previous Trials Showed Small or Null Effects"

$$P(\delta) = \text{Normal}(0, 2^2)$$

This prior encodes specific domain knowledge: the compound is structurally related to two drugs that showed null effects in Phase III. Before seeing this trial, we believe the effect is probably small — perhaps zero, perhaps 1–2 mmHg — and effects above 6–7 mmHg are quite unlikely.

**Posterior (conjugate update):**
Precision from data = 0.189; precision from prior = $1/4 = 0.25$; total precision $= 0.439$.

**Posterior mean:** $\frac{4.9 \times 0.189 + 0 \times 0.25}{0.439} \approx \frac{0.926}{0.439} \approx 2.11$ mmHg.

**95% CrI:** approximately [−0.8, 5.0] mmHg.

**P(δ > 3 | data, Prior 3) ≈ 0.27.** Only about 27% probability of a clinically meaningful effect under this prior — a sharply different conclusion.

---

### What Changed?

| | Prior 1 (Flat) | Prior 2 (Weakly informative) | Prior 3 (Informative) |
|---|---|---|---|
| Prior specification | Uniform (implicit) | Normal(0, 10²) | Normal(0, 2²) |
| Posterior mean | 4.9 mmHg | 4.75 mmHg | 2.11 mmHg |
| 95% CrI | [0.4, 9.4] | [0.4, 9.1] | [−0.8, 5.0] |
| P(δ > 3) | 0.79 | 0.76 | 0.27 |
| Interpretation | Treatment probably works | Treatment probably works | Treatment probably doesn't clear clinical threshold |

The point estimates barely move between Prior 1 and Prior 2. They move substantially with Prior 3. The tails move in all cases — the probability of large effects changes across priors — but the mode of the posterior is mainly data-driven when the prior is weak relative to the data.

**This is the key lesson:** with n = 40 and a plausibly informative prior, the *point estimate* is fairly robust. The *tail probabilities* — including P(δ > 3), the clinically relevant question — are sensitive to prior choice. Sensitivity analysis is not a weakness of the Bayesian approach; it is the analysis telling you honestly where the prior is doing work.

---

## Prior Sensitivity Analysis

When do priors matter and when do they not?

**Rule of thumb:** as the sample size grows, the likelihood dominates and the prior shrinks toward irrelevance. The posterior converges on the data — all three priors would give nearly the same answer if n = 400 instead of 40.

**Rule of thumb 2:** when the prior and likelihood are well-separated — when the data says "large effect" but your prior says "small effect" — the prior matters. When they agree, it doesn't.

**What to do:** run the analysis under at least two priors — one more diffuse, one more concentrated — and report whether the conclusion changes. If it doesn't change, you can report with confidence. If it does change, you have found the region where more data or better prior justification is needed.

This is not optional. A systematic survey found that among 64 published Bayesian clinical trials using non-informative priors, only 17.2% performed sensitivity analyses (BMC Medical Research Methodology 2026, DOI: 10.1186/s12874-026-02803-6). That is a field-wide failure to use the epistemic honesty that Bayesian methods make available.

Sensitivity analysis is not a concession to the frequentist critic who says "priors are arbitrary." It is the practice of showing your prior's work, which is exactly what scientific transparency requires.

---

## Side-by-Side Comparison

| | Frequentist (t-test) | Bayesian (three priors) |
|---|---|---|
| Prior | Implicit flat on δ | Explicit: named and auditable |
| Result | t = 2.13, p = 0.038; significant | P(δ > 3 | data) = 0.79 / 0.76 / 0.27 depending on prior |
| Point estimate of δ | 4.9 mmHg | 4.9 / 4.75 / 2.11 mmHg |
| 95% interval | CI: [0.4, 9.4] (approximate) | CrI: [0.4, 9.4] / [0.4, 9.1] / [−0.8, 5.0] |
| Probability of clinically meaningful effect? | Not available | Directly computable |
| Prior gameable? | No — flat prior is fixed | Yes — informative prior can be constructed to favor a hypothesis |
| Sensitivity to prior | Not applicable | High in tails, low near mode (for n = 40) |

**Why anyone uses frequentist methods:** In regulated, preregistered, or novel settings, the implicit flat prior is a guarantee of reproducibility and resistance to gaming. Every analyst who runs a t-test on this dataset gets the same p-value; no analyst can adjust the prior to produce a desired outcome. For regulatory approval in a first-in-class drug, this is a feature. For the clinician deciding whether to prescribe, who has domain knowledge about prior trials, the informative Bayesian analysis uses that knowledge correctly — but only if the analyst is honest.

---

## Worked Example: Three Priors in Practice

**Situation.** A clinical research organization is evaluating a pain medication for use in post-operative recovery. The trial randomizes 52 patients. The primary outcome is a 10-point visual analog scale for pain at 24 hours. The treatment group scores 4.1 (lower is better); the control group scores 5.3. Mean difference: −1.2 points. SE = 0.6 points.

The analyst knows that similar drugs in this class show typical effects of −1 to −2 points, with large effects (> 3 points) being very rare.

**Process.**

*Step 1: Frequentist baseline.* t = −2.0, p = 0.051. Not quite significant at α = 0.05. Under the frequentist framework, this is a borderline result. Under strict significance testing, the drug is "not proven effective."

*Step 2: Prior 1 (Flat).* Posterior mean = −1.2 points, 95% CrI = [−2.4, 0.0]. P(δ < −1) ≈ 0.57. Marginal.

*Step 3: Prior 2 (Weakly informative: Normal(0, 5²)).* Very similar to Prior 1 — the prior is wide relative to the data. Posterior mean ≈ −1.19, 95% CrI nearly identical.

*Step 4: Prior 3 (Informative: Normal(−1.5, 1²) — "typical effect around −1.5 points").* Posterior mean ≈ −1.32 points, 95% CrI = [−2.2, −0.4]. P(δ < −1) ≈ 0.76. Considerably more compelling.

**Resolution and lesson:** The borderline frequentist result (p = 0.051) becomes meaningful under an informative prior that encodes actual domain knowledge. The analysis honestly shows that if you believe the drug works like others in its class, the data are consistent with a useful effect. If you believe the drug is unproven (flat prior), the evidence is marginal.

This is not the Bayesian analysis "fixing" the frequentist result. It is making explicit what the analyst already knew — and showing what the data add to that knowledge.

**Dead end:** The analyst initially tried to specify a prior centered on −3 points, reasoning that "that's the effect the company is hoping for." This is the gaming case the regulatory framework guards against. The prior was revised to −1.5 points based on published literature on similar compounds — not on the company's aspirations.

**Limit:** The informative prior's advantage disappears if the prior is wrong. If this drug works differently from its predecessors — perhaps it has a novel mechanism — the informative prior pulls the posterior in the wrong direction. Prior knowledge is never free.

---

## Prompting for Implementation

### A well-formed prompt for prior sensitivity analysis

```
I have clinical trial data comparing a treatment to control. The outcome 
is mean difference in pain score, with observed mean difference = -1.2 
points and standard error = 0.6 points (n = 52 patients, 26 per group).

Please run a Bayesian analysis of this data under three priors for the 
true treatment effect delta:

Prior 1: Flat/uniform (improper prior -- equivalent to MLE/frequentist baseline)
Prior 2: Normal(0, 5^2) -- weakly informative, no strong knowledge about effect size
Prior 3: Normal(-1.5, 1^2) -- informative, based on published literature showing 
         similar drugs have effects around -1.5 points

For each prior:
1. Show the posterior distribution (give mean, SD, and 95% credible interval).
2. Compute P(delta < -1 | data) -- the probability the effect exceeds the 
   clinical minimum of 1 point.
3. Plot or describe the three posterior distributions on the same scale.

Also run the standard frequentist two-sample t-test equivalent and report 
the t-statistic, p-value, and 95% confidence interval.

Show all mathematical steps. Explain in one sentence what changes across 
the three posteriors and what stays the same.
```

### What to verify

- The flat-prior Bayesian result should match the frequentist confidence interval closely (they are equivalent when the prior is flat and the likelihood is normal). If they differ, something is wrong with the implementation.
- The posterior mean under Prior 3 should be pulled toward −1.5 relative to the data mean of −1.2. If the Prior 3 posterior mean is *farther* from −1.5 than −1.2 is, the prior and likelihood are being combined incorrectly.
- P(δ < −1) should be higher under Prior 3 than under Prior 1, not lower.

---

## Common Misconceptions

**Misconception 1: "Bayesian methods are subjective because they use priors; frequentist methods are objective because they don't."**

Frequentist methods use priors — specifically, flat priors on all parameters. The t-test does not avoid a prior; it uses one that is implicit and fixed. The Bayesian approach makes the prior explicit, which makes it auditable. A named prior is more transparent than a hidden one. Whether a named prior is "more subjective" than a hidden flat one depends on whether the knowledge it encodes is defensible — and that judgment requires domain expertise, not statistical theory.

**Misconception 2: "If the posterior changes across priors, the Bayesian analysis is unreliable."**

Prior sensitivity is information, not failure. If the conclusion changes dramatically with different priors, the data are not strong enough to overwhelm prior assumptions — and that is a fact worth knowing. The correct response is not to abandon Bayesian analysis; it is to report the sensitivity, seek more data if possible, or justify the prior more carefully. A frequentist analysis that reaches a definitive conclusion from data too sparse to warrant one is not more reliable; it is less honest.

**Misconception 3: "A flat prior means I'm not assuming anything."**

A flat prior on $\delta$ assigns equal probability to a treatment effect of 0.001 mmHg and a treatment effect of 10,000 mmHg. For a drug trial, this is not neutrality — it is an assumption that effects of any size are equally plausible. Gelman (2006) showed that flat priors on variance parameters in hierarchical models can produce prior predictive distributions that strongly favor implausible predictions. "No assumption" is not a state you can achieve; you can only choose between named and unnamed assumptions.

---

## AI Wayback Machine: Bertha Swirles Jeffreys (1903–1999)

---

*This chapter's central figure — Harold Jeffreys — built the philosophical foundations for Bayesian inference. But the intellectual context in which he worked included a remarkable collaborator: Bertha Swirles, who married Jeffreys in 1940.*

---

Bertha Swirles earned first-class honours in mathematics at Girton College, Cambridge, and went on to work in quantum mechanics alongside Paul Dirac and Subrahmanyan Chandrasekhar as a research student of Ralph Fowler. She later worked with Max Born and Werner Heisenberg on relativistic quantum theory. In 1940, she and Harold Jeffreys published *Methods of Mathematical Physics* — a textbook that remained a standard reference for decades.

Harold Jeffreys's *Theory of Probability* (1939, revised 1961) laid out the systematic Bayesian approach to scientific inference, including the "noninformative" Jeffreys prior — a prior invariant under reparameterization, designed to represent genuine prior ignorance in a mathematically principled way. The project was not philosophical abstraction: it emerged from his work in geophysics and seismology, where the question of how to update beliefs about earth structure from seismic data required exactly the machinery he built.

Bertha Swirles became President of the Mathematical Association in 1969–1970. She outlived Harold Jeffreys by more than a decade, dying in 1999 at age 95.

The Jeffreys prior — the prior named after Harold — is still used today, particularly in objective Bayesian analysis where the analyst genuinely has no domain knowledge to encode. It is a precise mathematical answer to the question this chapter began with: what should a prior look like when the honest answer is "I don't know"?

*Anchor for student reflection:* "You are Bertha Swirles in 1940. Harold believes that scientific inference requires prior probabilities; most statisticians around you resist this. What is the strongest argument for his position, and what is the strongest objection you can imagine from his critics?"

---

## Exercises

**Exercise 1 (Apply).** Using the clinical trial data from this chapter's worked example (mean difference = −1.2 points, SE = 0.6 points, n = 52), run the analysis under all three priors. Compute and report: (a) the posterior mean and 95% credible interval for each prior; (b) P(δ < −1 | data) for each prior; (c) a one-sentence description of where the posteriors agree and where they diverge.

**Exercise 2 (Analyze).** A pharmaceutical company's statistician specifies a prior for their Phase III trial centered at δ = +8 mmHg — a large positive effect — citing unpublished internal pilot data. The trial shows a mean difference of 4.2 mmHg (SE = 2.8, n = 30).

(a) What concern does this prior specification raise?

(b) How would the FDA's preregistration requirement address this concern?

(c) Run the analysis under the company's prior and under a weakly informative prior of Normal(0, 5²). How different are the posteriors? What does this difference tell you about the prior's influence on the conclusion?

**Exercise 3 (Evaluate).** A colleague says: "Bayesian methods are subjective because they require you to choose a prior. Frequentist methods are objective because you don't have to choose anything." 

Write a response of three to five paragraphs that is genuinely fair to *both* the concern and the Bayesian counterargument. Your response should: (a) acknowledge the legitimate grain of truth in the colleague's concern; (b) explain the hidden-prior argument without presenting it as a "gotcha"; and (c) identify at least one setting where you would choose the frequentist approach for principled reasons.

---

## What Would Change My Mind

1. **If the "hidden prior" argument turned out to be unfair.** The claim that t-tests implicitly use flat priors is made by Bayesian statisticians (Gelman and others) and is mathematically defensible. But frequentist statisticians dispute that calling this a "prior" is a fair characterization of what the method assumes. If the frequentist counterargument — that flat priors are a convention, not a belief — were more compelling, the chapter's framing of "both have priors, one is hidden" would need revision.

2. **If the regulatory landscape solidified around Bayesian methods.** The FDA's 2026 draft guidance [verify] moves toward endorsing Bayesian methods with conditions, rather than defaulting to frequentist requirements. If this became settled regulatory practice and the gaming concern were adequately handled by preregistration requirements, the "regulatory preference for frequentist" advantage would diminish substantially.

3. **If a principled solution to the "what is a weakly informative prior?" problem emerged.** Currently, "weakly informative" is more of a practice norm than a formal definition. If a rigorous criterion for weak informativeness were established — analogous to the Jeffreys prior for objective Bayesian analysis — the prior specification problem would become more tractable.

---

## Still Puzzling

1. The Jeffreys prior is designed to be invariant under reparameterization — if you change the parameter scale, the prior changes accordingly. Does this solve the "flat prior is not neutral" problem? Or does it just move the arbitrariness to a different level?

2. Empirical Bayes — estimating the prior from the data and then using it in the posterior — is widely used in practice (e.g., in genomics). This violates the principle that the prior should be specified before seeing the data. Is this a pragmatic compromise or a logical error? The field disagrees.

3. If two analysts use the same data but different priors and reach different conclusions, which conclusion should a policymaker act on? Is there a rational rule for aggregating Bayesian posteriors across analysts with different priors?

4. The chapter shows that point estimates are relatively robust to prior choice but tail probabilities are not. Does this mean that frequentist point estimates (which correspond to the flat-prior posterior mode) are more reliable than they appear? Or does it mean that tail probabilities — which are what decisions often hinge on — are exactly where the prior does its most consequential work?

---

## Bridge to Chapter 8

Priors do their most visible work when data is sparse. When n = 40, the prior on $\delta$ still moves tail probabilities substantially. When n = 400, it barely matters. Chapter 8 takes you to the hardest inferential conditions: small samples, rare events, and underpowered studies — exactly where the prior does the most work, and where the choice between "import prior knowledge" and "report honest ignorance" has the highest stakes.

Chapter 8 also introduces the winner's curse: a systematic bias that afflicts frequentist analysis of underpowered studies — not because of any mistake by the analyst, but as a mathematical consequence of using a significance threshold as a publication filter. Understanding the winner's curse requires understanding what sparse data does to inference, which is why it belongs immediately after this chapter.

---

*Sources: Jeffreys (1961); Gelman (2006); Gelman, Jakulin, Pittau & Su (2008); Gelman, Simpson & Betancourt (2017) [verify volume/page]; BMC Medical Research Methodology (2026); FDA 2026 draft guidance [verify final status at fda.gov/media/190505/download]; EMA ICH E9(R1) addendum (2019) [verify EMA position on Bayesian methods from ema.europa.eu].*
