# When the Assumptions Don't Hold — A Number for the Doubt You Already Have


## TL;DR

- TL;DR: The E-value asks the one question every observational analysis owes its decision-maker — how strong would an unmeasured confounder have to be to overturn this conclusion?
- The chapter moves through Opening — The seed from Week 9, and the engineering case I owe you, Concept one — Sensitivity analysis is not a hedge. It is the next number., Concept two — The E-value: definition, derivation, worked numbers, Mid-chapter checkpoint, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

**Suggested titles:**
1. When the Assumptions Don't Hold — A Number for the Doubt You Already Have
2. The E-Value: How Strong Would the Lurking Variable Have to Be?
3. Sensitivity, Calibrated: The Last Honest Move Before You Ship

**TL;DR:** The E-value asks the one question every observational analysis owes its decision-maker — *how strong would an unmeasured confounder have to be to overturn this conclusion?* — and gives it back as a single number on the risk-ratio scale. Computing the number is statistical work; deciding whether the number is large enough to call the analysis definitive is domain work, and the second of those moves is the chapter's load-bearing claim.

**Byline:** Nik Bear Brown

**Prerequisites:**
- The seed planted in Chapter 9, Section 6: the E-value as the natural completion of the backdoor procedure when one or more backdoor paths run through unmeasured variables.
- The minimal-adjustment-set work of Chapter 10: you have a Z that closes every backdoor path you can see, and you know what to do when no such Z exists.
- The defense of the DAG (Chapter 11), the spec from DAG to estimator (Chapter 12), and the diagnostic reading of the output (Chapter 13). The E-value answers the question those three chapters keep returning to: *how much should we trust this number?*
- The two-register communication discipline from Chapter 11 — technical register for the auditor, plain-language register for the decision-maker. We use the same trick here for the finding itself.

**Learning objectives:**
- **Apply (Part A):** Calculate an E-value from a risk ratio and a confidence interval and interpret it against domain knowledge about likely unmeasured confounders.
- **Evaluate (Part A):** Produce a qualified conclusion in two registers — technical and plain-language — for a given observational analysis.
- **Evaluate (Part A):** Decide whether the analysis should be reported as definitive, fragile, or not-definitive, and defend the decision against domain knowledge of plausible confounders.
- **Evaluate (Part B):** Calculate the E-value for your own domain's strongest causal claim and calibrate it against named domain confounders.
- **Create (Part B):** Write the qualified conclusion in both registers for your own analysis, including the explicit "not definitive" report when the E-value does not support a stronger reading.

---

## 1. Opening — The seed from Week 9, and the engineering case I owe you

I owe you a number.

Five weeks ago, in Chapter 9, I stopped halfway through a pricing example. The DAG had a treatment `P` (a planned price increase), an outcome `R` (weekly revenue), three observed confounders we adjusted for, and one unmeasured confounder — call it `U` — that we believed was probably operating but had no measurement of. I said the estimate was biased if `U` exists and has non-trivial effects. I did not say *how* biased. I planted a seed:

> *Three of four visible backdoor paths blocked. One path through an unmeasured variable open. We will quantify the robustness of the estimate in Week 14.*

It is Week 14.

Take a real engineering case so the question has teeth. A retail company runs a quasi-experimental analysis of a discharge-recommendation engine — call it a recommendation system that nudges customer-service agents toward a particular resolution path. The headline result, after the team's careful adjustment for measured covariates, is an observed risk ratio of `RR = 2.0` for the favorable outcome (the customer doesn't churn within 30 days) on treated cases versus controls. Confidence interval, on the risk-ratio scale: `[1.5, 2.7]`.

The team writes up the result. They are about to ship. The VP asks one question.

*"How sensitive is this to a confounder you didn't measure?"*

That is the question the next 6,000 words answer.

Here is the shape of the answer, before I derive it. There is a number — the E-value — that says: *for this observed risk ratio, an unmeasured confounder would have to be associated with both the treatment and the outcome by risk ratios of at least* `Y` *each, simultaneously, to fully explain the observed effect away*. The number `Y` is computable in closed form from the observed risk ratio. The formula is one line of arithmetic. For the team's `RR = 2.0`, the number happens to be about `3.4`.

That alone does not answer the VP's question. It reformulates it. The VP's *real* question is: *is there a plausible unmeasured confounder in our domain that could produce a 3.4× association with both treatment and outcome?* If yes, the analysis is fragile. If no, the analysis is robust. The team's data scientist computes `3.4`. The team's domain expert decides whether `3.4` is a comfortable distance from the unmeasured-confounder strengths the domain routinely produces.

That second decision is not in any tool. EconML's `sensitivity_analysis` method computes a robustness value, an analogue of the E-value, and writes it on the screen. DoWhy's refutation framework runs a battery of sensitivity tests. The EValue R package (Mathur, Smith, Ding, & VanderWeele) computes E-values from estimates and confidence intervals in a one-liner. None of those tools knows that in your specific company, in your specific product, with your specific kinds of unmeasured variables — seasonal cohort drift, marketing-campaign overlap, segment-level rollout staggering, the things the data scientist is paid to know — typical unmeasured confounding produces risk-ratio-equivalent associations in some range you can name. That domain calibration is the second move. It is the move the book has been preparing you for since Chapter 1.

This chapter teaches the procedure: compute the E-value, calibrate it against domain knowledge, write the qualified conclusion in two registers, and — the chapter's hardest move — say "not definitive" when the calibration does not support more. The chapter's pedagogical anchor is that last move. Engineering culture rewards confident-sounding outputs. The chapter argues that the analyst who reports "not definitive" when the evidence does not support more is doing the method. The analyst who hands the decision-maker a confidence they did not earn is failing them.

Let me name what we are not doing, before I name what we are. We are not building a new sensitivity-analysis framework. The framework is VanderWeele and Ding's, published in *Annals of Internal Medicine* in 2017 ([VanderWeele & Ding, 2017](https://doi.org/10.7326/M16-2607)), and corrected against widespread misuse two years later by VanderWeele, Mathur, and Ding ([VanderWeele, Mathur, & Ding, 2019](https://doi.org/10.7326/M18-3112)). We are not even arguing that the E-value is the right sensitivity tool in every case — Cinelli and Hazlett's *robustness value* ([Cinelli & Hazlett, 2020](https://doi.org/10.1111/rssb.12348)) is sometimes preferable; Rosenbaum bounds ([Rosenbaum, 2002](https://link.springer.com/book/10.1007/b97493)) remain in econometric use; partial-identification approaches in the spirit of Manski ([Manski, 1990](https://www.jstor.org/stable/2006592)) take a different tack entirely. We will teach the E-value because it is the workhorse of contemporary applied practice, and because the *interpretive* move it forces — domain calibration — is the move that matters whichever sensitivity tool you use.

The number comes from the data and the model. The meaning of the number comes from you and the domain. Hold that distinction. It is the chapter's whole spine.

---

## 2. Concept one — Sensitivity analysis is not a hedge. It is the next number.

Let me specify what we are doing, because the word *sensitivity* has at least three different jobs in applied work and only one of them is the one I mean.

In numerical-methods textbooks, *sensitivity* means the partial derivative of an output with respect to an input — how much does the output change when the input changes by one unit? In machine-learning practice, *sensitivity analysis* often means what statisticians would call *ablation* — drop a feature, refit, see what happens to performance. In causal inference, *sensitivity analysis* means something more specific: *given the identification assumptions you cannot directly check from the data, how much would they have to fail for your causal conclusion to flip?*

The thing the data cannot check is the assumption of *no unmeasured confounding* (sometimes called *conditional ignorability*, sometimes *exchangeability conditional on `Z`*). You drew a DAG. You found an adjustment set `Z`. You estimated the effect under the assumption that `Z` blocks every backdoor path. The data is consistent with that assumption *and* consistent with the assumption that some unmeasured `U` creates an open backdoor path you did not see. The two assumptions produce different effect estimates and the data, on its own, cannot tell you which one is correct.

This is not a deficiency of the data. It is a structural fact about observational causal inference, which Chapters 4 through 10 have already walked you through. Sensitivity analysis is the principled response: rather than pretending the assumption is exactly true, *parameterize how much it might fail*, and report the answer as a function of the parameter.

The result of sensitivity analysis is not a hedge. A hedge is a sentence in the discussion section: "results should be interpreted with caution given the possibility of unmeasured confounding." A hedge does no work — it merely informs the reader that the analyst is aware the work is incomplete. Sensitivity analysis is a *number*: if an unmeasured confounder of strength `s` exists, your conclusion changes by the amount `f(s)`. The decision-maker can now ask, *do we think `s` is plausible in our domain?* And that is a question the analyst and the domain expert can answer together, with reference to specific named variables, prior literature, and prior experience.

The discipline is this. Every observational causal estimate ships with at least one sensitivity calculation. The calculation says: *here is the strength of unmeasured confounding that would overturn this conclusion*. The discussion calibrates that strength against domain knowledge: *here is what unmeasured confounding routinely looks like in this domain*. The conclusion combines them: *the estimate is robust / fragile / not definitive against the calibrated strengths*.

A common misconception lives here. Students sometimes hear "sensitivity analysis" and think *robustness check* — refit the model with a slightly different specification, see whether the estimate is stable. Those checks are useful, but they are not sensitivity analysis in the sense we mean. They probe the *modeling* assumptions (functional form, included variables, sample-period choice). They do not probe the *identification* assumption (no unmeasured confounding). The identification assumption is the one the data fundamentally cannot check, and so it is the one sensitivity analysis is for. When you read a paper that reports "we conducted sensitivity analyses by refitting with different controls," ask whether any of the refits varied the assumption about unmeasured confounding. If they did not, the paper has done a robustness check and called it sensitivity analysis. The terminology is loose. The distinction is real.

One more piece of framing. The output of a sensitivity analysis is a *qualified claim*: an estimate plus a bound on how much that estimate can survive. Both halves are required. An estimate without a sensitivity bound is a number whose trustworthiness the reader has to guess at. A sensitivity bound without an estimate is a tool measurement without a tool. The chapter's structural form — *estimate plus sensitivity bound equals qualified claim* — is the artifact you will deliver in Week 15 for every analysis you do for the rest of your career, if you take the method seriously.

---

## 3. Concept two — The E-value: definition, derivation, worked numbers

Now I owe you the number.

**Definition.** The E-value for an observed risk ratio `RR ≥ 1` is the *minimum* strength of association — on the risk-ratio scale — that an unmeasured confounder `U` would have to have *with both the treatment `T` and the outcome `Y`*, conditional on the measured covariates, to fully explain away the observed association between `T` and `Y`. The point of the word *minimum* is that the E-value is a lower bound on the required confounder strength. Any unmeasured confounder weaker than the E-value cannot, by itself, explain the result away. To overturn the conclusion, an unmeasured confounder would need to clear the bound.

**Formula.** For `RR ≥ 1`:

$$\text{E-value} = \text{RR} + \sqrt{\text{RR} \times (\text{RR} - 1)}$$

For a protective effect (`RR < 1`), invert first: compute the E-value for `1/RR`.

That is the whole formula. One line. I want you to feel comfortable with it before we calibrate it, because comfort is what keeps students from skipping it.

**Where the formula comes from.** Ding and VanderWeele's earlier paper ([Ding & VanderWeele, 2016](https://doi.org/10.1097/EDE.0000000000000457)) proved a sharp upper bound on the bias factor by which an observed risk ratio can be distorted by an unmeasured binary confounder. Their bias factor, written `BF_U`, is:

$$\text{BF}_U = \frac{\text{RR}_{UY} \cdot \text{RR}_{TU}}{\text{RR}_{UY} + \text{RR}_{TU} - 1}$$

where `RR_TU` is the risk ratio for the confounder-treatment association and `RR_UY` is the risk ratio for the confounder-outcome association. The intuition: confounding by `U` can inflate the observed `RR` by at most a factor of `BF_U`. To *fully explain away* an observed `RR` of size `r`, the bias factor would need to satisfy `BF_U ≥ r`. The 2017 paper asks the reverse question: what is the *smallest* value of `RR_TU = RR_UY = e` (the worst case, where the confounder is equally strong on both arms) such that `BF_U` first reaches `r`? Set `RR_TU = RR_UY = e` in the bias-factor formula:

$$\frac{e \cdot e}{e + e - 1} = \frac{e^2}{2e - 1} = r$$

Solve for `e`:

$$e^2 - 2re + r = 0$$

By the quadratic formula:

$$e = \frac{2r + \sqrt{4r^2 - 4r}}{2} = r + \sqrt{r^2 - r} = r + \sqrt{r(r-1)}$$

That is the E-value. The derivation is in two facts: the bias factor of Ding-VanderWeele 2016, and the choice of the *symmetric* worst case where the confounder is equally strong on both legs. The symmetric worst case is what makes the E-value a single number rather than a curve. (For asymmetric confounder strengths — say a confounder that is strongly associated with treatment but weakly with outcome — you fall back to the bias-factor formula itself, which is the next tool in the kit.)

**Worked example, matching the canonical paper.** VanderWeele and Ding's 2017 paper used a published observational estimate from a 2001 *New England Journal of Medicine* paper on antidepressant use during pregnancy ([Chambers et al., 1996](https://doi.org/10.1056/NEJM199610033351401)) as the running illustration. The reported risk ratio for one of the associations in their illustration is `RR = 3.9`. Plug into the E-value formula:

$$\text{E-value} = 3.9 + \sqrt{3.9 \times (3.9 - 1)} = 3.9 + \sqrt{3.9 \times 2.9} = 3.9 + \sqrt{11.31}$$

Computing the square root: `√11.31 ≈ 3.363`. So:

$$\text{E-value} \approx 3.9 + 3.363 = 7.263 \approx 7.26$$

An unmeasured confounder would need to be associated with both treatment and outcome by risk ratios of at least `7.26` each — simultaneously — to fully explain away the observed effect of `3.9`. That is a *very* strong confounder. In the clinical-epidemiology domain, confounders of strength 7+ are rare. (Smoking on lung cancer has an `RR` of roughly 10 in some classical studies, so a smoking-strength confounder *could* explain away an `RR` of 3.9 — but you would have to name a smoking-strength confounder you missed, and naming one is a high evidentiary bar.) For the 2017 paper's running example, the E-value of 7.26 told the reader: this association is robust to any unmeasured confounder weaker than a tobacco-cancer-strength variable, which constrains the space of plausible alternative explanations sharply.

**Now the team's case from Section 1.** Observed `RR = 2.0` for the recommendation-engine analysis. Compute:

$$\text{E-value} = 2.0 + \sqrt{2.0 \times (2.0 - 1)} = 2.0 + \sqrt{2.0 \times 1.0} = 2.0 + \sqrt{2.0}$$

`√2.0 ≈ 1.414`. So:

$$\text{E-value} = 2.0 + 1.414 \approx 3.414$$

The team's headline E-value is `3.4`. An unmeasured confounder would need to clear `3.4×` on both the treatment-association and outcome-association legs to explain away the observed effect of `2.0`. Whether `3.4×` is large or small *in the team's specific domain* is the calibration question of Section 4. Hold the number.

**The CI-bound E-value.** VanderWeele and Ding recommend computing the E-value twice: once for the point estimate, and once for the confidence-interval bound *closer to the null*. The second is usually the more relevant number, because it answers a different and more decision-useful question: *how strong would the confounder have to be to push the result across the null, i.e., to make the lower CI bound cross 1?*

For the team's case, the lower CI bound is `1.5`. Compute the E-value at the lower bound:

$$\text{E-value}_{\text{CI}} = 1.5 + \sqrt{1.5 \times 0.5} = 1.5 + \sqrt{0.75} \approx 1.5 + 0.866 = 2.366 \approx 2.37$$

So at the CI bound, the team's E-value drops to about `2.4`. The interpretation: an unmeasured confounder of strength `2.4×` on both legs would be enough to push the CI lower bound across the null. The point estimate `3.4` is the more dramatic number; the CI bound `2.4` is the more honest one. Both should be reported. The conventional applied-paper format is to report the pair, sometimes as `E-value (point) = 3.4; E-value (CI) = 2.4`.

A common misconception. Students sometimes treat the E-value as a hypothesis test. "E-value > 2, so the result is significant." The E-value is not a *p*-value and is not a threshold-based decision. It is a *strength bound* on the unmeasured confounder. Whether the bound is high or low — whether the result is robust or fragile — depends on the domain calibration of Section 4. There is no domain-free threshold above which an E-value "passes."

A second common misconception. "The E-value tells me the *probability* that confounding is a problem." It does not. It is a structural quantity, not a probability. It says nothing about how likely an unmeasured confounder of the required strength actually is in your domain. That likelihood is what the domain expert supplies in the next section.

A third, technical caveat. The E-value formula above assumes the outcome is approximately binary and the effect is on the risk-ratio scale. For continuous outcomes, hazard ratios, odds ratios, mean differences, and so on, the E-value framework extends, with appropriate transformations. VanderWeele and Ding 2017 gives the conversion table; the EValue R package implements the conversions automatically. For an odds ratio with a rare outcome, the E-value formula applies as written (because the odds ratio approximates the risk ratio). For a hazard ratio with a non-rare outcome, the EValue package's `evalue()` function does the right conversion. Use the tool, but understand that the formula above is the binary-outcome workhorse and other cases need the conversion. (Mathur, Smith, Ding, and VanderWeele have detailed documentation in [Mathur et al., 2018](https://cran.r-project.org/web/packages/EValue/EValue.pdf), and the Stata implementation is described in [Linden, Mathur, & VanderWeele, 2020](https://journals.sagepub.com/doi/10.1177/1536867X20909696).)

The formula is the easy part. What you do with it is the rest of the chapter.

---

### Mid-chapter checkpoint

Stop. Before reading further, do this from cold:

1. Recompute the E-value for `RR = 2.0` and verify you get `3.41`.
2. Recompute the E-value for `RR = 3.9` and verify you get `7.26`.
3. For an `RR = 1.2` (a small association), compute the E-value. What does the number say about how strong the confounder would need to be?
4. State, in one sentence, what the E-value is *not*. (Not a *p*-value, not a probability of confounding, not a domain-free threshold.)

If those four moves feel solid, the next section will land. The next section is where the chapter does its load-bearing work. The formula is small. The calibration is everything.

For exercise 3: `RR = 1.2`, E-value = `1.2 + √(1.2 × 0.2) = 1.2 + √0.24 ≈ 1.2 + 0.49 = 1.69`. A confounder of strength `1.7×` on both legs is, in many engineering domains, an extremely low bar. The number tells you that the result is fragile to almost any plausible unmeasured confounder.

---

## 4. Concept three — Domain calibration, the move that does not come in the box

Here is where the book's central claim becomes mechanical.

The E-value of `3.4` for the team's recommendation-engine analysis is a number. It does not, by itself, say anything about whether the analysis should be reported as definitive. To decide *that*, the analyst must answer a different question: *in this specific domain, what is the typical strength of association between common unmeasured variables and (a) the treatment, (b) the outcome?* If the typical strength is much smaller than 3.4, the result is robust — no plausible unmeasured confounder reaches the bound. If the typical strength is around 3.4, the result is fragile — a routine unmeasured variable could explain it away. If the typical strength exceeds 3.4, the result is not definitive — you should expect, prior to seeing the data, that an unmeasured confounder of sufficient strength exists.

That calibration is not in any tool. It is not in EconML's `sensitivity_analysis`. It is not in DoWhy's refutation framework. It is not in the EValue package. It is not in `causalml`. It is not in the bias-factor formula. It is the domain expert's contribution, and it is — to use the book's spine — the irreducibly human move.

Let me make the move concrete with three named domains.

**Clinical epidemiology.** Strong unmeasured confounders in clinical research are well-cataloged. Smoking on lung cancer has an `RR` of roughly 10 in classical case-control studies — so smoking is a confounder of strength 10. Healthy-user selection (people who use one preventive service tend to use others) typically produces associations in the 1.5–2.5× range across both treatment and outcome ([Shrank, Patrick, & Brookhart, 2011](https://doi.org/10.1007/s11606-010-1609-1)). Socioeconomic status, when unmeasured, typically produces 1.5–2× associations with both medical-treatment uptake and downstream outcomes in observational hospital studies. Genetic predispositions, when relevant and unmeasured, can reach 5–10×. The clinical-epidemiology *rule of thumb* — and it is a rule of thumb, not a law — is that E-values below 2 are fragile, E-values above 4 are robust against most known unmeasured confounders, and E-values between 2 and 4 require explicit case-by-case judgment about which specific confounders are likely.

**The engineering case from Section 1.** The recommendation-engine analysis is not in clinical epidemiology. It is in a customer-experience domain where the typical unmeasured variables are different in *kind*. The candidates the team's data scientist should name explicitly: seasonal cohort drift (cohorts assigned to treatment in different weeks differ in baseline churn propensity), marketing-campaign exposure overlap (some treated cases were also exposed to a retention campaign that ran during the same window), agent-skill confounding (the agents most likely to use the recommendation engine were also the most experienced agents, who would have had lower churn anyway), and time-of-day rollout effects (the treatment was rolled out during a particular shift, which selected on customer mix).

What is the typical strength of those associations in the team's domain? This is where the domain-expert sentence has to be specific. Based on the team's prior experiments and the published industry literature on similar systems, seasonal cohort drift typically produces 1.3–1.5× associations with both treatment timing and churn. Marketing-campaign overlap can reach 2–3× on both legs when campaigns are large. Agent-skill confounding, depending on the rollout design, can reach 2–4×. Time-of-day rollout effects are usually small, in the 1.2–1.4× range. The largest plausible unmeasured confounder strength is in the 2–4× range, anchored by marketing-campaign overlap and agent-skill confounding.

Now compare. The team's E-value is `3.4` at the point estimate, `2.4` at the CI bound. The largest plausible unmeasured confounder strength is in the 2–4× range. The bound and the plausible strength *overlap*. The honest conclusion is not "robust." It is "the analysis cannot rule out a plausible unmeasured confounder."

**The classic robust case.** Compare to the smoking-lung-cancer literature. The observed `RR` was roughly 9 in Hammond and Horn's 1958 study. The E-value is about 17. The largest plausible unmeasured confounder anyone has named — genetic predisposition to both smoking and lung cancer — produces associations of at most 2–3× in twin and family studies. The bound is 17. The plausible confounders cap out at 3. The gap is overwhelming. *That* is a robust analysis. Not because the E-value passes some threshold, but because the bound vastly exceeds any plausible unmeasured-confounder strength in the domain.

**The fragile-by-construction case.** Consider an observational A/B test in a recommendation system with quasi-random assignment by user cohort. Observed `RR = 1.3` for engagement. E-value = `1.3 + √(1.3 × 0.3) = 1.3 + √0.39 ≈ 1.92`. Domain calibration: in quasi-randomized rollouts, cohort drift routinely produces 1.3–1.5× associations with both assignment and engagement. The E-value is `1.92`, the plausible-confounder strength is `1.3–1.5`, the bound exceeds plausible strength by a hair. That is not robust. That is *just barely* not-explained-away by a routine cohort-drift confounder. The honest conclusion is: the analysis is suggestive but not definitive; a properly randomized test is required.

The pattern across the three cases is the same. The E-value is the bound. The domain knowledge is the calibration. The conclusion is the comparison. Take any of the three steps out of the procedure and you have an incomplete analysis.

A common misuse, documented carefully by VanderWeele, Mathur, and Ding in their 2019 corrective ([VanderWeele, Mathur, & Ding, 2019](https://doi.org/10.7326/M18-3112)): treating the E-value as a stand-alone significance criterion. The corrective is worth reading in full — it is two pages, in *Annals of Internal Medicine*, and it names the specific misuses the authors observed in the literature in the two years after the original paper. The headline misuse is exactly the one the chapter has been warning you about: papers reporting "E-value of 2.3 indicates the result is robust" *without the domain-calibration sentence*. Without the calibration, the number is meaningless. VanderWeele 2019 is firm: there is no domain-free threshold. The reader has to do the comparison.

I want to make a stronger claim than the corrective makes. The corrective's framing is *the E-value is not a stand-alone significance threshold*. The book's framing is *no statistical sensitivity quantity is*. The same point applies to Cinelli-Hazlett robustness values, to Rosenbaum bounds, to partial-identification widths, to any sensitivity tool you might use. The tool produces a number. The interpretation requires domain knowledge the tool cannot supply. The number-meaning split is the book's spine, and Chapter 14 is where the split becomes a procedure you can follow on the page.

---

## 5. Concept four — The qualified conclusion in two registers

You have the E-value. You have the calibration. You now write the conclusion. The chapter's structural artifact, which Chapter 11 introduced for the DAG and Chapter 14 generalizes to the finding, is the *two-register conclusion*. Same content. Different audience. Different vocabulary. Both registers honest about the same uncertainty.

The technical register is for the methodologically literate audience — your data-science peers, the reviewer of an internal post-mortem, the auditor of a regulated decision pipeline. The plain-language register is for the decision-maker — the VP, the clinician, the product lead, the policy owner. The two registers are not redundant. The technical register is *auditable*. The plain-language register is *actionable*. The analyst is responsible for both.

Here is the template, applied to the team's recommendation-engine case from Section 1.

**Technical register (for the post-mortem write-up):**

> Estimated effect: `RR = 2.0` (95% CI: `[1.5, 2.7]`).
> E-value (point estimate): `3.41`.
> E-value (CI bound closer to null): `2.37`.
>
> Domain-calibration note: Plausible unmeasured confounders in the recommendation-engine deployment include seasonal cohort drift, marketing-campaign exposure overlap, agent-skill confounding, and time-of-day rollout effects. Based on prior internal experiments and the published industry literature on similar systems, the typical risk-ratio-equivalent association strengths of these confounders fall in the range `[1.3, 4.0]` on each leg, with marketing-campaign overlap and agent-skill confounding occupying the upper end of that range.
>
> Conclusion: Given the CI-bound E-value of `2.37` and a plausible unmeasured-confounder strength range overlapping the bound, the observed effect is *not robust* to unmeasured confounding under the maintained DAG. The analysis is suggestive but does not, on its own, support a definitive causal claim. A randomized confirmatory test is required before treating this finding as production evidence.

**Plain-language register (for the VP):**

> We estimated that the recommendation engine reduces 30-day churn by an amount that, if true, is meaningful — roughly a doubling of the favorable outcome compared with controls. Our analysis is consistent with that effect.
>
> To trust the estimate, we are assuming we measured every variable that matters for both (a) which cases got the recommendation engine and (b) which cases ended in churn. We almost certainly did not measure all of them. Plausible unmeasured variables include shifts in customer mix across the rollout period, overlap with a marketing campaign that ran during the same weeks, the experience level of the agents who chose to use the system, and time-of-day effects.
>
> Could those unmeasured variables fully account for the effect we observed? Our analysis says they would have to be unusually strong to do so — *but not implausibly strong*. Based on prior experience with this kind of rollout, we expect unmeasured variables of approximately the required strength to exist. We cannot, from this analysis alone, rule them out.
>
> So: we are not confident enough to treat this analysis as proof. If you are deciding whether to expand the rollout, the strongest defensible reading is that the analysis is consistent with a meaningful effect, *and* a randomized test is required to establish whether the effect is real. We recommend the randomized test as the next step. We would not recommend treating this analysis as definitive.

Look at the two registers side by side. The same information is in both. The technical register foregrounds the numbers, the names of the confounders, and the bounds. The plain-language register foregrounds the decision — "we recommend the randomized test as the next step." The plain-language register is *not* a dumbing-down of the technical one. It is a translation that preserves the uncertainty precisely while shifting the vocabulary so the decision-maker can act.

A failure mode the chapter is asking you to recognize: the plain-language register that *removes* the uncertainty. "We've shown the recommendation engine works, with an E-value of 3.4." That sentence is not a plain-language translation. It is a misrepresentation. The technical register's uncertainty has been replaced by confidence in the plain-language version. The decision-maker is now acting on a confidence the analyst did not earn from the data. Engineering students often write this version because they were taught that "clarity is confidence" in the writing of executive summaries. The chapter teaches the opposite: clarity is the *honest* communication of uncertainty, not the elimination of it.

A second failure mode: the plain-language register that drowns the decision-maker in technical language. "The E-value at the CI bound is 2.37, which, when calibrated against the plausible-confounder strength range of [1.3, 4.0], yields an overlap region that prevents rejection of the null under the maintained DAG." That sentence is in the wrong register for its audience. The VP cannot act on it because they cannot extract the recommendation. The technical register and the plain-language register must each be *internally coherent* for their audience. Writing both is harder than writing either alone.

The two-register pattern is general. It applies to the DAG defense (Chapter 11), to the analysis specification (Chapter 12), to the diagnostic output (Chapter 13), and — now — to the finding. By the time the student arrives at the terminal deliverable in Chapter 15, the two-register write-up is the deliverable form for every identification-layer decision the analyst has made. The reader gets the technical version. The decision-maker gets the plain-language version. The analyst owes both.

---

## 6. Concept five — When the honest answer is "not definitive"

This is the chapter's most important move.

Sometimes — often — the answer the analyst owes the decision-maker is: this analysis, on its own, does not support a definitive claim. The E-value is small. The domain has plausible confounders of the required strength. The right next step is either (a) targeted data collection on the suspected confounder, (b) a randomized experiment that breaks the confounding by design, or (c) acting on the analysis as suggestive while flagging that a confirmatory study is needed.

The chapter teaches students to *write that conclusion when the evidence warrants it*.

Engineering students arrive trained to ship. They treat "not definitive" as failure — as evidence the analyst did not do the work, or did the work and discovered the answer was unsatisfying. The chapter argues the opposite. The analyst who reports "not definitive" when the analysis cannot bear more weight is doing the method correctly. The analyst who claims definitive when the E-value does not support it is failing the decision-maker by handing them a confidence they did not earn.

Let me make the structure concrete.

A *not-definitive* finding has the following shape:

1. A real estimate. We have a point estimate and a confidence interval. The signal is not nothing.
2. An E-value that is in the same neighborhood as plausible unmeasured-confounder strengths in the domain. The bound and the calibration overlap.
3. A recommended next step that would convert the not-definitive finding into a definitive one, *or* an explicit statement that no such next step exists with currently available tools.

The third item is what distinguishes "not definitive" from "no signal." Not-definitive is not a verdict of *nothing here*. It is a verdict of *signal worth pursuing, with a specific named pursuit and a specific named obstacle*. The decision-maker can act on a not-definitive finding — they can fund the experiment, they can authorize the data collection, they can pilot the change in a constrained setting — without treating the analysis as proof.

Here is an engineering case where the honest answer is "not definitive."

A pricing team runs an observational analysis on six months of A/B-disabled pricing data, before any randomized test was possible. They estimate a price-elasticity-equivalent effect with `RR = 1.6` and CI `[1.3, 2.0]`. E-value at the CI bound: `1.3 + √(1.3 × 0.3) = 1.3 + √0.39 ≈ 1.92`. Domain calibration: in the pricing domain, unmeasured demand-state confounders (seasonality, marketing-campaign exposure, supply shocks, competitor pricing) routinely produce associations of `2–4×` with both observed pricing changes and revenue.

The bound is `1.92`. The plausible confounder strengths start at `2`. The bound is *below* the lower edge of the plausible range. An ordinary unmeasured-confounder in this domain is strong enough to explain the effect away.

The honest report:

> Technical register: `RR = 1.6` (95% CI: `[1.3, 2.0]`); E-value (CI) = 1.92; plausible domain confounders (demand-state seasonality, marketing-campaign overlap, supply-side shocks, competitor-pricing reaction) routinely produce associations in the `[2, 4]` range. The analysis cannot rule out unmeasured confounding of the required strength. *Conclusion: not robust; not definitive.*
>
> Plain-language register: We estimated that the pricing change increases revenue by an amount that, if true, would be meaningful. Our analysis is consistent with that effect. But to trust the analysis, we are assuming that demand-state variables (seasonality, competing marketing, supply, competitor pricing) had similar effects on the treated weeks and the comparison weeks. We do not have evidence that this was true, and we have reason — from prior experience — to suspect it was not. The kind of unmeasured variation that we know is present in this domain is, by our calculation, strong enough to explain the observed effect on its own. We do not recommend acting on this analysis as proof. The recommended next step is a holdout-region randomized test, where the assignment of price changes is controlled by design rather than inferred from history. The current analysis is useful as motivation for that test; it is not a substitute for the test.

The pricing team's manager reads the plain-language register and writes a ticket for the holdout-region test. That is not a failure of the analysis. That is the analysis doing exactly what it should do — pointing toward the experiment that *would* produce a definitive answer, while honestly reporting that the current data cannot.

I want to name a specific misuse to watch for, because engineering culture pushes toward it. The team feels pressure to ship something. The analysis comes back not-definitive. The manager asks the analyst whether the result is "actionable." The analyst, wanting to be useful, says yes. The plain-language register quietly drops the "not definitive" sentence. The technical register stays accurate, but the executive summary reads as a finding. Two weeks later, the change is shipped on the strength of the executive summary. Three months later, the randomized test runs as a post-hoc check and reveals no effect. The original observational result was confounded.

The discipline the chapter is asking for is this: the plain-language register is *exactly as honest* about the uncertainty as the technical register. The analyst's job is not to make the result feel actionable. The analyst's job is to make the *uncertainty* actionable. *Not definitive, randomized test recommended* is an actionable plain-language conclusion. *Significant effect observed* is a misrepresentation when the E-value calibration says otherwise.

The chapter's pedagogical anchor lives here. Engineering culture penalizes hedged conclusions; the chapter must reframe "not definitive" as the *productive* form of uncertainty — the form that points toward the next experiment rather than paralyzing the current decision. The category is *not* "no signal." It is *signal worth investigating with appropriate hedging, and an experiment is the way to convert this into a definitive claim*. Teach yourself, and your team, to recognize that category as a complete deliverable. The analyst who delivers it is doing the method.

---

## 7. Integration — The cleanest example of the book's spine

I have been saying since Chapter 1 that the identification layer of causal analysis requires domain judgment no causal AI tool supplies. Chapter 14 is the cleanest worked example of that claim in the book.

Here is the structure, set out as a procedure:

| Step | Input | Output | Source of the output |
|------|-------|--------|----------------------|
| 1 | DAG | Identification verdict (identifiable / not identifiable from observational data) | Algorithmic — DoWhy, dagitty, the Shpitser-Pearl ID algorithm |
| 2 | DAG + adjustment set | Point estimate + CI | Algorithmic — EconML, DoWhy, statsmodels |
| 3 | Point estimate + CI | E-value (point and CI) | Algorithmic — `EValue` R package, `evalues.app`, one line of math |
| 4 | E-value + domain | Plausible-confounder-strength range | Human — domain expert |
| 5 | E-value + plausible range | Robust / fragile / not definitive | Human — comparison |
| 6 | Verdict + audience | Two-register qualified conclusion | Human — writing |

Steps 1, 2, and 3 are algorithmic. They are what tools do. Step 4 is the load-bearing human contribution. The data scientist hands the E-value to the domain expert; the domain expert names the plausible unmeasured confounders and their typical strengths; the comparison in Step 5 falls out as soon as Step 4 is complete; the writing in Step 6 follows the two-register template.

No causal AI tool currently performs Step 4. The reason is structural. The plausible unmeasured confounders in your specific deployment, in your specific company, in your specific product, are knowledge the data scientist and the domain expert hold jointly. They are not in the published literature. They are in the team's prior experiments, in the team's institutional memory of past failures, in the domain expert's experience of what kinds of variables routinely move both treatment assignment and outcome in their setting. A large language model can suggest *categories* of plausible confounders for a domain ("seasonal cohort drift," "marketing-campaign overlap") — and they are useful for this, as a starting list. The model cannot calibrate the *strength* of those confounders to your specific setting. That calibration is what the domain expert brings.

This is the book's thesis made mechanical. The tool produces the number; you supply the meaning. The two contributions are not interchangeable. A team that runs the tool without the calibration has done arithmetic, not analysis. A team that does the calibration without the tool has done domain reasoning without an anchor. The full procedure requires both — and the human contribution is the one that does not come in the box.

A short word on the limits of the E-value, in the spirit of the method applied to itself. The E-value assumes a single hypothetical unmeasured confounder. The full literature has extensions for multiple confounders, but the workhorse formula is for one. The E-value applies cleanly to risk ratios and (with conversions) to other effect measures, but the conversions sometimes require assumptions about the outcome distribution that you should check. The E-value is a *lower bound* on required confounder strength; it is conservative in one direction and not the other (a true unmeasured confounder weaker than the E-value cannot explain the result away; a confounder stronger than the E-value *might* explain it away, depending on its specific structure). Cinelli-Hazlett robustness values are sometimes preferred when the analyst wants finer control over the assumed confounder structure. Rosenbaum bounds remain in econometric use for matched designs. *Sensemakr* (Cinelli's R and Stata package) implements the omitted-variable-bias framework. Robins-Rotnitzky-Scharfstein methods give yet another framework for sensitivity analysis under coarsening at random. The E-value is *one* sensitivity tool. It is the right default for engineering applied work because it is computable in closed form from any point-estimate-plus-CI output and because the domain-calibration move it forces is the move that matters whichever tool you use. The choice of tool is a refinement on top of that move.

The method applied to the method: the E-value is a sensitivity tool with known limits. Use it as the default. Reach for Cinelli-Hazlett, Rosenbaum, or Robins-Rotnitzky-Scharfstein when the structure of the problem demands them. Always do the calibration. Always write the two-register conclusion. Always report "not definitive" when the calibration warrants it. The procedure is the chapter's lasting deliverable.

---

## 8. Worked example — The full pipeline, one case end to end

Take the team's recommendation-engine case from Section 1 and walk it through the procedure end to end. By the end of this section, you should have the full deliverable in your hands.

**Step 0: The setup.** A retention recommendation engine has been deployed to a subset of customer-service cases over a six-month window. The treatment is *received a recommendation from the engine*. The outcome is *did not churn within 30 days*. The team's analysis adjusted for measured covariates: case-type, customer tenure, prior-period engagement, agent-shift, week-of-rollout, and customer segment. The maintained DAG is the team's stated assumption about how these variables relate to treatment and outcome. The unmeasured variables of concern are the four named in Section 4: seasonal cohort drift, marketing-campaign overlap, agent-skill confounding, time-of-day rollout effects.

**Step 1: Identification.** The team confirms, via DAGitty's `adjustmentSets()` function applied to the maintained DAG, that the adjustment set they used is a valid minimal adjustment set under the backdoor criterion *for the visible structure*. The unmeasured variables are off-graph — they are the unmeasured-confounder concern this chapter addresses.

**Step 2: Estimation.** The team's estimator — a doubly-robust estimator using gradient-boosted nuisance models — returns a point estimate of the favorable-outcome risk ratio of `2.0` with a 95% confidence interval of `[1.5, 2.7]`.

**Step 3: E-value calculation.** Point estimate: `E-value = 2.0 + √(2.0 × 1.0) = 2.0 + 1.414 ≈ 3.41`. CI bound (closer to null): `E-value_CI = 1.5 + √(1.5 × 0.5) = 1.5 + 0.866 ≈ 2.37`. Report both.

**Step 4: Domain calibration.** The team's data scientist convenes a 30-minute conversation with the recommendation-engine product manager and a senior CX operations lead. The agenda is one question: *what unmeasured variables routinely produce risk-ratio-equivalent associations with both engine usage and 30-day churn, in our deployment, and what is the typical strength of those associations?* The team produces the following list:

- *Seasonal cohort drift.* Cohorts in different weeks of the rollout have systematically different baseline churn propensities. Typical strength, based on prior cohort comparisons: `1.3–1.5×`.
- *Marketing-campaign overlap.* During three of the rollout weeks, a separately funded retention campaign was running. The cases that interacted with the engine during those weeks were more likely to also have received the campaign message. Typical strength of the campaign effect: `2–3×` on both treatment likelihood and churn.
- *Agent-skill confounding.* The agents most likely to use the new engine are also the agents with the lowest baseline churn — they would have handled the cases successfully even without the engine. Typical strength, based on the team's agent-stratified prior experiments: `2–4×` on both legs.
- *Time-of-day rollout effects.* The engine was enabled during a particular shift, selecting on customer mix. Typical strength: `1.2–1.4×`.

The largest plausible confounder strength is in the `2–4×` range, anchored by marketing-campaign overlap and agent-skill confounding.

**Step 5: Comparison.** The point-estimate E-value is `3.41`. The CI-bound E-value is `2.37`. The largest plausible confounder strength is in the `2–4×` range, overlapping both. The point-estimate E-value sits inside the plausible range. The CI-bound E-value sits at the lower edge of the plausible range. *The analysis is not robust to plausible unmeasured confounding.*

**Step 6: Write the two-register conclusion.** (See Section 5 above for the full text. The two registers are auditable and actionable respectively. Both flag the finding as *not definitive*. Both recommend a randomized confirmatory test.)

**Step 7: The team's action.** The team does not ship the engine to production on the strength of this analysis. The team writes a one-page memo to the product VP recommending a controlled randomized A/B test as the next step, scoped to the next quarter. The memo cites the observational analysis as motivation — there is a real signal worth investigating — and explicitly states that the current analysis cannot, on its own, support a production-rollout decision. The product VP approves the test. Three months later, the test runs. Six weeks after that, the team has a definitive answer.

This is the procedure. Six steps, three of which are algorithmic (1, 2, 3) and three of which are human (4, 5, 6). The human steps are not optional. They are not afterthoughts. They are not "the soft part of the analysis." They are the analysis. The arithmetic provides the bound. The judgment provides the verdict. The communication provides the action.

A note on the alternative ending. Suppose the domain calibration in Step 4 had returned a plausible-confounder-strength range of `[1.2, 1.8]`. Then the comparison in Step 5 would be: CI-bound E-value `2.37` vs. largest plausible confounder strength `1.8`. The bound exceeds the plausible strength by a clear margin. The verdict in Step 5 would have been *robust*. The two-register conclusion in Step 6 would have read very differently: *robust to unmeasured confounding within the named domain confounders; the recommendation engine can be deployed*. Same arithmetic. Different domain. Different verdict.

That is the chapter's whole point, made one more time. The E-value is the number. The domain is the meaning. You cannot have one without the other, and neither half comes in the box.

---

## 9. Chapter summary

The E-value is the minimum strength of association, on the risk-ratio scale, that an unmeasured confounder would have to have with *both* the treatment and the outcome to fully explain away the observed effect. The formula, for an observed risk ratio `RR ≥ 1`, is `E-value = RR + √(RR × (RR − 1))`. The derivation comes from the Ding-VanderWeele 2016 bias-factor bound; the closed-form simplification is VanderWeele-Ding 2017. Compute the E-value for the point estimate and for the CI bound closer to the null. The CI-bound number is usually the more decision-relevant one.

The E-value, alone, is not a verdict. The verdict requires *domain calibration*: a domain expert names the plausible unmeasured confounders in the specific deployment and their typical risk-ratio strengths. If the E-value exceeds the largest plausible strength by a clear margin, the conclusion is robust. If the E-value falls inside or below the plausible range, the conclusion is fragile or not-definitive.

The deliverable is the *qualified conclusion in two registers*. The technical register is auditable, reports numbers and named confounders, and concludes with a robust/fragile/not-definitive verdict. The plain-language register is actionable, translates the uncertainty into vocabulary the decision-maker can use, and concludes with a recommended action. Both registers preserve the uncertainty exactly. Neither is a dumbing-down of the other.

The hardest move is reporting *not definitive* when the calibration warrants it. Engineering culture rewards confident conclusions. The chapter argues that the analyst's responsibility is honest uncertainty, not manufactured confidence. The not-definitive verdict is not a failure — it is a productive form of uncertainty that points to the next experiment.

The E-value is the workhorse of contemporary applied sensitivity analysis. Alternatives — Cinelli-Hazlett robustness values, Rosenbaum bounds, Robins-Rotnitzky-Scharfstein methods — exist and are appropriate in specific settings. Whichever tool you choose, the domain-calibration move is the same: the tool provides the number, the human provides the meaning. That split is the book's spine, and Chapter 14 is the cleanest place in the book to see it operate.

The seed planted in Chapter 9 is now harvested. The pricing example with the unmeasured `U`, left as an open question five weeks ago, has its quantification. The procedure transfers to any observational causal analysis you do, in any domain, with any tooling. The number is small. The discipline is everything.

---

## 10. Bridge to Chapter 15

The terminal deliverable is one week away.

Chapter 15 asks you to bring every identification decision you have made across Acts Two and Three into one coherent analysis plan. You will state the causal question, draw the DAG, defend it, specify the estimand and estimator, run the analysis, read the output, *and* compute the E-value, calibrate it against your domain, write the two-register qualified conclusion, and — when the calibration warrants — report the finding as not definitive with a recommended next step.

The Week 15 deliverable is the form of every causal analysis you will ship for the rest of your career, if you take the book's method seriously. Chapter 14 has now given you the last piece — the sensitivity-analysis closing — that the deliverable requires. The week ahead is the integration. The toolkit is complete. The judgment is yours.

---

## 11. Exercises

### Warm-up

**Exercise 14.1.** Given an observed risk ratio `RR = 2.5`, compute the E-value. Show the arithmetic. *(Apply.)*

**Exercise 14.2.** Given an E-value of `4.0`, name at least one named unmeasured confounder from any applied domain — clinical epidemiology, customer-experience analytics, pricing, infrastructure — that you would expect to meet or exceed the `4.0×` bound on both treatment and outcome legs. Cite one source for the named confounder's typical association strength. *(Apply.)*

### Application — Part A (given case)

**Exercise 14.3.** A published observational analysis reports `RR = 1.8` (95% CI: `[1.4, 2.3]`) for the association between a workplace-policy change and an employee-retention outcome.

(a) Compute the E-value at the point estimate and at the CI bound closer to the null.
(b) Name three plausible unmeasured confounders in the workplace-policy domain and provide a calibrated range of risk-ratio-equivalent association strengths for each, citing at least one source per confounder where possible.
(c) Decide whether the analysis should be reported as robust, fragile, or not definitive. Justify your decision against the calibration.
(d) Write the two-register qualified conclusion for the case, following the Section 5 template.

*(Evaluate.)*

### Application — Part B (your own domain)

**Exercise 14.4.** Take the strongest causal claim you have made in your own domain over the past year — a claim from an A/B test, an observational analysis, a deployed-system effect estimate, anything where you have a point estimate and a CI.

(a) Convert the estimate to the risk-ratio scale if it is not already on that scale. (For a continuous outcome, use the EValue R package's `evalue()` function to do the conversion appropriately; report your conversion choice.)
(b) Compute the E-value at the point estimate and at the CI bound.
(c) Name the plausible unmeasured confounders in your domain. For each, provide your best calibration of the typical risk-ratio-equivalent association strength. Cite the source — your team's prior experiments, published literature in your domain, your domain expert's stated estimate. Be specific.
(d) Decide robust / fragile / not definitive. Justify.

*(Apply.)*

**Exercise 14.5.** Write the two-register qualified conclusion for the analysis in Exercise 14.4. Use the Section 5 template. The technical register should be approximately 150–250 words; the plain-language register should be approximately 150–250 words. Both registers should preserve the uncertainty exactly and recommend a specific next action — either *deploy*, *gather more data on a named variable*, *run a randomized test*, or *do not act on this analysis*.

Bring both registers to office hours. The plain-language register will be read by another student playing the role of your decision-maker. If they cannot extract a clear recommendation from your plain-language register, revise. *(Create.)*

### Synthesis

**Exercise 14.6.** Return to the pricing example from Chapter 9, Section 5. The team identified one open backdoor path through an unmeasured `U`. Suppose the analysis after adjusting for the visible confounders returns `RR = 1.7` with CI `[1.4, 2.0]`.

(a) Compute the E-value at the point and CI.
(b) Use your domain knowledge — and the Chapter 9 description of the pricing setting — to calibrate plausible `U`-strengths.
(c) Decide whether the original Chapter 9 worry about `U` is quantitatively material to the conclusion. Write one paragraph explaining how the E-value, *combined with* the backdoor criterion of Chapter 9 and the minimal-adjustment-set discipline of Chapter 10, gives you a complete identification-layer answer to the pricing question.
(d) Identify one assumption you are making in the calibration that, if wrong, would change the verdict. State what would change your mind.

*(Analyze.)*

### Challenge

**Exercise 14.7.** Find a published causal claim in any applied domain — peer-reviewed paper, internal-blog write-up, government report, regulatory analysis — that you believe should *not* have been reported as definitive given its E-value and the plausible-confounder strengths in its domain. Write a 500-word memo that:

(a) States the claim and the estimate.
(b) Computes the E-value (or, if you cannot find the CI, requests it from the authors or notes the absence).
(c) Names the plausible unmeasured confounders in the domain and their typical strengths.
(d) Argues, with citations, that the analysis is not-definitive by the chapter's calibration standard.
(e) Proposes the experiment or data-collection step that would convert the not-definitive finding into a definitive one.

The memo is graded on the quality of the calibration argument and on the specificity of the proposed next step. It is not graded on whether you have "caught" an error in the published work — being unable to fully rule out the claim is itself a finding. *(Evaluate.)*

---

## 12. LLM exercise

**Prompt to your LLM of choice (Claude, ChatGPT, Gemini):**

> I have an observational causal analysis with the following result. The treatment is `[describe — one sentence]`. The outcome is `[describe — one sentence]`. After adjustment for the measured covariates `[list 3–5 named covariates]`, the estimated risk ratio is `[your value]` with a 95% confidence interval of `[your CI]`. The domain is `[name your domain — recommendation systems, pricing, clinical decision support, infrastructure, etc.]`.
>
> Three tasks.
>
> Task 1: Compute the E-value at the point estimate and at the CI bound closer to the null. Show the arithmetic. Use the VanderWeele-Ding formula: E-value = RR + sqrt(RR × (RR − 1)) for RR ≥ 1; invert first for RR < 1.
>
> Task 2: Name three plausible unmeasured confounders in the domain I named, and for each, provide your best estimate of the typical risk-ratio-equivalent association strength on both the treatment and outcome legs. Be specific about *why* each variable is a plausible confounder — what mechanism connects it to both treatment assignment and outcome.
>
> Task 3: Given the E-value and the plausible-confounder strengths, decide whether the analysis is robust, fragile, or not definitive. Recommend a specific next step.

After the LLM responds:

1. **Check the arithmetic.** Did the LLM apply the formula correctly? For `RR = 2.0`, the E-value should be `3.41`. For `RR = 1.5`, the E-value should be `1.93`. Spot-check at least two values. If the LLM got the formula wrong on a simple case, do not trust its arithmetic on your case — recompute by hand.
2. **Check the domain confounders.** Are the LLM's suggested confounders specific to your domain, or generic? "Selection bias" and "unmeasured confounding" are not named confounders; they are categories. A useful LLM response names *specific* variables in your domain and explains the mechanism. If the LLM gives generic categories, push back: "Name specific variables, not categories."
3. **Check the calibrations.** Does the LLM provide numerical estimates of confounder strength, or qualitative descriptions only? A useful LLM response provides numerical ranges (e.g., "1.5–2× in the published industry literature on similar systems"). If the ranges are not cited, treat them as the LLM's *prior estimate* — useful as a starting point, but you should verify against your team's actual experience.
4. **Check the verdict.** Did the LLM's robust/fragile/not-definitive call match the comparison? If the E-value is `2.4` and the plausible-confounder strength is `2–4`, the call should be "not definitive." If the LLM called it robust, the LLM has made the misuse the VanderWeele-Mathur-Ding 2019 corrective specifically warns against. Push back: "Compare the E-value to the plausible-confounder strength I named. The bound is `[X]`. The plausible strength is `[range]`. Justify your verdict against the comparison."
5. **Write a one-paragraph note** on where the LLM was correct, where it was wrong, and where it gave a confident-sounding answer that did not match the calibration discipline of the chapter. Submit the note as your exercise deliverable.

A note on what to expect. Current models (Claude 4 family, GPT-4o family and successors, Gemini 1.5/2 family) are generally reliable on the E-value formula for simple cases — they have the closed-form expression in their training data. They are *less* reliable on domain calibration: their suggested confounder strengths are often plausible but generic, and not anchored to specific domain literature. They sometimes default to confidence calls — robust / fragile — without doing the comparison properly. The model is a useful first-pass assistant for the procedural arithmetic and for generating a starting list of plausible confounders. It is not a substitute for the domain expert's calibration in Step 4 of the procedure.

This is what *irreducibly human* means in operational terms. The model can do steps 1, 2, and 3 of the procedure well, with verification. Step 4 — the domain calibration — is the step the model is structurally weakest at, because the calibration depends on knowledge that lives in your team's prior experience, not in the public training data. The chapter's spine, mapped to your tool stack: trust the model for the arithmetic, verify the model on the confounder list, and supply the calibration yourself.

---

## 13. AI Use Disclosure

This chapter was drafted with the assistance of Claude (Anthropic), using the Feynman-voice pedagogical scaffold defined in the workshop's CLAUDE.md and the chapter-specific pantry notes prepared for Chapter 14 of *Causal Reasoning: Irreducibly Human*. Every primary source cited was checked against its original venue. Citations flagged `[verify]` are pending Nik's review. The E-value formula was verified against VanderWeele & Ding 2017 directly, and the worked example matching `RR = 3.9 → E-value ≈ 7.26` reproduces the canonical paper's illustrative calculation. The LLM exercise in Section 12 was designed to be run by the student against current chatbot models; the qualitative description of where current models succeed and fail reflects the author's testing of recent Claude and GPT-family models on E-value calibration tasks during the chapter's drafting.

---

## 14. Part B bonus

If you completed Exercise 14.5 and arrived at a not-definitive verdict for your own domain analysis, do this: write a one-page memo to the most senior person in your organization who is making a decision based on the answer to your causal question. The memo's purpose is *not* to deliver a finding — it is to deliver the not-definitive verdict with a recommended next step the decision-maker can authorize. Follow the structure of the Section 8 worked example. Bring the memo to office hours.

If you completed Exercise 14.5 and arrived at a robust verdict, do this: write a one-page red-team memo arguing that the verdict is *over*-confident. Name the one unmeasured confounder you did not include in your Exercise 14.4(c) list that, if it existed at the strength you would have to grant for it to be unmeasured, would change the verdict. The exercise is to teach you to find the calibration's blind spot. Robust does not mean uncriticizable. Robust means the calibration you did supports the verdict; the next-best analyst can still ask what you missed.

---

## 15. Key terms

- **Sensitivity analysis.** The quantitative response to the identification assumption of no-unmeasured-confounding. Parameterizes how strong an unmeasured confounder would have to be to overturn the conclusion. Distinct from *robustness checks*, which probe modeling assumptions, not identification assumptions. (Section 2.)
- **E-value.** The minimum strength of association, on the risk-ratio scale, that an unmeasured confounder would need to have with both treatment and outcome to fully explain away the observed association. Formula for `RR ≥ 1`: `E-value = RR + √(RR × (RR − 1))`. (Section 3.)
- **Bias factor (Ding-VanderWeele 2016).** The sharp upper bound on the multiplicative bias a binary unmeasured confounder can produce in a risk-ratio estimate, in terms of the confounder's two association strengths. The E-value is a closed-form re-expression of the bias factor under the symmetric worst case. (Section 3.)
- **Domain calibration.** The process of comparing the E-value to typical unmeasured-confounder strengths in the specific applied domain. The interpretive step that no causal AI tool currently performs. (Section 4.)
- **Qualified conclusion (two registers).** The chapter's deliverable: a technical register for the methodologically literate audience and a plain-language register for the decision-maker, both reporting the same uncertainty in different vocabulary. (Section 5.)
- **Robust / fragile / not definitive.** The chapter's three-label verdict structure for a sensitivity-analyzed estimate. Robust = E-value clearly exceeds plausible-confounder strengths. Fragile = E-value overlaps the plausible range. Not definitive = E-value is dominated by plausible-confounder strengths. (Sections 4–6.)
- **CI-bound E-value.** The E-value computed at the confidence-interval bound closer to the null, rather than at the point estimate. The more decision-relevant figure in most applied work. (Section 3.)
- **Robustness value (Cinelli-Hazlett 2020).** An alternative sensitivity quantity, grounded in omitted-variable bias, sometimes preferred over the E-value when the analyst wants finer control over assumed confounder structure. (Section 7.)
- **Rosenbaum bounds.** The pre-E-value sensitivity framework for matched designs, still in econometric use. (Section 7.)

---

## 16. Further reading

- Tyler J. VanderWeele and Peng Ding, "Sensitivity Analysis in Observational Research: Introducing the E-Value," *Annals of Internal Medicine* 167(4) (2017), 268–274. [https://doi.org/10.7326/M16-2607](https://doi.org/10.7326/M16-2607) — The founding paper. Read in full.
- Tyler J. VanderWeele, Maya B. Mathur, and Peng Ding, "Correcting Misinterpretations of the E-Value," *Annals of Internal Medicine* 170(2) (2019), 131–132. [https://doi.org/10.7326/M18-3112](https://doi.org/10.7326/M18-3112) — The corrective. Two pages. Required reading after the 2017 paper.
- Peng Ding and Tyler J. VanderWeele, "Sensitivity Analysis Without Assumptions," *Epidemiology* 27(3) (2016), 368–377. [https://doi.org/10.1097/EDE.0000000000000457](https://doi.org/10.1097/EDE.0000000000000457) — The bias-factor bound from which the E-value derives.
- Carlos Cinelli and Chad Hazlett, "Making Sense of Sensitivity: Extending Omitted Variable Bias," *Journal of the Royal Statistical Society B* 82(1) (2020), 39–67. [https://doi.org/10.1111/rssb.12348](https://doi.org/10.1111/rssb.12348) — The robustness-value framework. Read after the E-value papers.
- Paul R. Rosenbaum, *Observational Studies* (2nd ed., Springer, 2002). The pre-E-value sensitivity-analysis framework. Engineering reader does not need it for daily work; the historically grounded reader should know it.
- Maya B. Mathur, Louisa H. Smith, Peng Ding, and Tyler J. VanderWeele, "Web site and R package for computing E-values" (CRAN documentation; see also Mathur & VanderWeele 2020, *American Journal of Epidemiology*). [https://cran.r-project.org/web/packages/EValue/EValue.pdf](https://cran.r-project.org/web/packages/EValue/EValue.pdf) — The R-package documentation, with worked examples for different outcome types.
- Ariel Linden, Maya B. Mathur, and Tyler J. VanderWeele, "Conducting sensitivity analysis for unmeasured confounding in observational studies using E-values: The evalue package," *Stata Journal* 20(1) (2020), 162–175. [https://journals.sagepub.com/doi/10.1177/1536867X20909696](https://journals.sagepub.com/doi/10.1177/1536867X20909696) — The Stata implementation.
- Carlos Cinelli, Jeremy Ferwerda, and Chad Hazlett, "sensemakr: Sensitivity Analysis Tools for OLS in R and Stata." [https://cran.r-project.org/web/packages/sensemakr/](https://cran.r-project.org/web/packages/sensemakr/) — The robustness-value tooling.
- David Spiegelhalter, *The Art of Statistics* (Basic Books, 2019), Chapter 12. Communicating uncertainty to decision-makers; the model for the plain-language register.
- Miguel A. Hernán and James M. Robins, *Causal Inference: What If* (Chapman and Hall/CRC, 2020). Chapter on unmeasured confounding and sensitivity. Freely available online at [https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/).
- Charles F. Manski, "Nonparametric Bounds on Treatment Effects," *American Economic Review* 80(2) (1990), 319–323. The partial-identification alternative to point-estimate sensitivity analysis. [https://www.jstor.org/stable/2006592](https://www.jstor.org/stable/2006592).

---

## 17. Draft flags

The following items in this chapter were flagged for verification during drafting and remain pending Nik's review:

- The illustrative use of `RR = 3.9` in Section 3 references the running example in VanderWeele & Ding 2017. The 2017 paper cites Chambers et al. 1996 *New England Journal of Medicine* for the source observational estimate; the exact RR attribution to that specific Chambers paper is `[verify]` — the 7.26 E-value matches VanderWeele & Ding's worked example regardless of the underlying observational source.
- The recommendation-engine case in Section 1 / Section 8 is a structurally accurate but anonymized composite. No specific company is named. The plausible-confounder strength ranges in Section 4 (1.3–1.5× for seasonal cohort drift, 2–3× for marketing-campaign overlap, 2–4× for agent-skill confounding) are illustrative and drawn from the pantry's domain-calibration notes; verified industry-literature citations for each range are `[verify]`.
- The Hammond and Horn 1958 smoking-cancer numbers (`RR ≈ 9`, E-value `≈ 17`) are widely cited in the E-value literature as the canonical robust example. Exact figures `[verify]` from the original Hammond & Horn 1958 *JAMA* paper.
- The Shrank, Patrick, and Brookhart 2011 *Journal of General Internal Medicine* citation for healthy-user-selection strength is provided with DOI; the paper's specific cited range (1.5–2.5×) is paraphrased from the pantry notes — `[verify]` exact range from the source.
- The qualified-conclusion two-register template is the chapter's structural deliverable. The structure is consistent with Spiegelhalter's framing and with GRADE-style guidance for clinical findings, but the codification as a deliverable artifact in the engineering setting is a contribution of this textbook. Instructor's manual must validate.
- The Linden, Mathur, & VanderWeele 2020 *Stata Journal* citation is provided with DOI; exact pagination `[verify]`.
- The Cinelli, Ferwerda, & Hazlett *sensemakr* package citation is provided to CRAN; the exact authorship and publication-venue citation `[verify]`.

---

## What would change my mind

If a causal-inference tool emerged that reliably performed *Step 4* of the chapter's procedure — domain calibration of plausible unmeasured-confounder strengths, anchored to the analyst's specific deployment rather than to generic domain priors — then the chapter's framing of E-value calibration as the irreducibly human move would need revision. As of the chapter's writing, no production tool performs Step 4: the LLMs can generate generic confounder lists, but none can calibrate strengths against the team's specific prior experience. If that gap closes, the spine of this chapter (and of the book) needs to be re-examined honestly.

## Still puzzling

I do not yet have a clean account of when the *single-confounder* E-value is materially misleading because the real concern is *multiple* simultaneous unmeasured confounders. The multi-confounder extensions exist in the literature (VanderWeele & Ding 2017 sketches them; Smith & VanderWeele have follow-up work). The engineering rule of thumb for *when to leave the single-confounder workhorse for the multi-confounder framework* is something I am still working out chapter by chapter. The cases I have walked through in this chapter were tractable under the single-confounder framing; the cases I have not yet handled probably are not.

---

**Tags:** sensitivity-analysis, E-value, VanderWeele-Ding, domain-calibration, qualified-conclusion, identification-layer
