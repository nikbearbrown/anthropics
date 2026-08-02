# Chapter 15: Sensitivity Analysis — How Wrong Could We Be?


## TL;DR

- Companion to the case study by Hrishi Pal.
- The chapter moves through Learning Objectives, Prerequisites, Why This Chapter Exists, Section 1: The Problem That Sensitivity Analysis Solves, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Companion to the case study by Hrishi Pal*

---

## Learning Objectives

By the end of this chapter, you should be able to:

1. **Explain** why every observational causal estimate requires sensitivity analysis — not as a formality, but as the step that determines whether the estimate is actionable.
2. **Compute and interpret** an E-value: what risk ratio an unmeasured confounder would need to achieve in both directions to explain away a finding, and whether that threshold is realistic.
3. **Compute and interpret** a Rosenbaum bound (Γ): how much hidden bias in treatment assignment the study could tolerate before statistical significance is lost.
4. **Benchmark** both measures against real-world confounders from the relevant domain literature — which is what transforms an abstract number into a judgment about whether to act.
5. **Report findings honestly** using calibrated language that conveys the fragility or robustness of a causal estimate — including when the honest report is "we cannot rule out confounding."

---

## Prerequisites

This chapter assumes you know:

- **What a confounder is** and why it creates spurious associations between treatment and outcome. You do not need to know the backdoor criterion cold, but you should understand that unmeasured confounders are the central threat to observational causal inference.
- **What a risk ratio is**: $RR = P(\text{outcome} \mid \text{exposed}) / P(\text{outcome} \mid \text{unexposed})$. We will use risk ratios throughout this chapter.
- **What statistical significance means** — and, more importantly, what it does not mean. A $p$-value below 0.05 tells you the finding is unlikely under the null hypothesis. It tells you nothing about whether an unmeasured variable is driving the association.
- **What propensity score matching or weighting does**: it balances measured covariates between treatment and control groups. If you have read Chapters 5 and 6, you are fully prepared. If not, what you need to know is this: balancing measured variables does not protect you from variables you did not measure.

If you have read Chapters 1–9 of the theory spine, this chapter will fit naturally into the picture. If you are reading this as a standalone, the key concept to keep in your head is: *every method in every earlier chapter assumes you have measured and adjusted for all important confounders. Sensitivity analysis is how you test what happens when that assumption is wrong.*

---

## Why This Chapter Exists

Every method in this book assumes, at some point, that you have controlled for confounding. Matching assumes it. Weighting assumes it. Even instrumental variables, which are designed to avoid it, assume you have found a valid instrument. The assumption goes by different names in different methods — ignorability, no unmeasured confounders, conditional exchangeability — but it is always there, and it is always an assumption, never a fact.

Here is the uncomfortable thing about that assumption: you cannot verify it from your data. You can check that treated and control groups are balanced on the variables you measured. You cannot check balance on variables you did not measure, because you do not have them. The assumption of no unmeasured confounding is, by construction, untestable.

This creates a gap between what causal methods can give you and what you need to responsibly act on a finding. The methods give you an estimate: a best guess at the causal effect, conditional on your measured covariates being sufficient. What you need is a judgment: is this estimate robust enough to act on, or is it fragile — sensitive to hidden variables that your data cannot see?

Sensitivity analysis is how you make that judgment. It does not tell you whether unmeasured confounding exists. It tells you how much unmeasured confounding would be needed to overturn your finding — and then it asks you to evaluate whether that level of confounding is plausible given what you know about your domain.

That last step — the domain evaluation — is where this becomes interesting. The number a sensitivity analysis produces is not its own interpretation. An E-value of 2.17 means nothing until you ask: *are there real-world variables that could achieve a risk ratio of 2.17 in both directions?* Answering that question requires looking at the literature, knowing something about the biology or the economics or the psychology of your domain, and making a judgment call that no formula can make for you.

That is also why this chapter exists. The formula is the easy part. The judgment is where intellectual honesty either happens or does not.

---

## Section 1: The Problem That Sensitivity Analysis Solves

Let me start with the scenario that Hrishi Pal used in his case study, because it is well-chosen. I want to walk through it slowly enough that the problem becomes concrete before we introduce any tools.

A hospital system runs a post-discharge phone call program for patients with heart failure. Nurses call high-risk patients within 72 hours of discharge to check on medications, symptoms, and follow-up appointments. The hypothesis is that early contact reduces 30-day readmissions.

The study uses observational data. Patients were not randomly assigned to receive calls — nurses made judgment calls based on staffing, patient risk scores, and who was reachable. The analysis matches called and uncalled patients on measured covariates: age, primary diagnosis, length of stay, insurance type, prior readmissions. After matching, called patients have a 30-day readmission rate of 18%; uncalled patients have a rate of 31%. The estimated effect is a risk ratio of approximately 0.58 — a 42% relative reduction.

The result is statistically significant. The matched groups are balanced on measured covariates. The paper reports: "Post-discharge phone calls significantly reduced 30-day readmissions (RR = 0.58, 95% CI [0.41, 0.82], p = 0.002)."

Should the hospital scale this program? Should it hire more nurses? Should it present this finding to its board as evidence of an effective intervention?

Here is the thing I want you to sit with before we go further: you do not know yet. You have a number. You do not have a judgment.

The reason you do not have a judgment is that the matching procedure balanced patients on what was measured. It did not — could not — balance them on what was not measured. And there are obvious candidates for unmeasured confounding in this scenario.

Medication adherence is one. Patients who are more diligent about their medications are probably both more likely to answer a post-discharge phone call (they are engaged, they have their phone with them, they are following instructions) and less likely to be readmitted (because they are taking their medications). If medication adherence is driving both treatment receipt and the outcome, the observed risk ratio of 0.58 could be entirely or partially a product of that common cause — not of the calls themselves.

Health literacy is another. Social support is another. All three are well-documented predictors of readmission in the clinical literature, and all three are also plausible predictors of whether a patient picks up the phone. None of them were measured.

The question is not whether these variables exist. They clearly do. The question is: *how big would their effect need to be to explain away the finding?* That is the question sensitivity analysis answers.

![DAG for the hospital readmission scenario. Nodes: PhoneCall (treatment), Readmission (outcome), MeasuredCovariates (age, diagnosis, LOS,...](images/11-chapter-sensitivity-analysis-fig-01.png)
*Figure 11.1 — DAG for the hospital readmission scenario*

---

## Section 2: The E-Value — How Strong Would a Confounder Need to Be?

The E-value was introduced by Tyler VanderWeele and Peng Ding in 2017. It answers a precise question: *what is the minimum strength of association that an unmeasured confounder would need to have — with both the treatment and the outcome — to fully explain away the observed effect?*

I want to build the intuition before I give you the formula, because the formula is easy to memorize and easy to misapply without the intuition.

### The intuition

Imagine you have an unmeasured confounder $U$. For $U$ to explain away the observed association between treatment and outcome, two things need to be true simultaneously:

1. $U$ needs to be associated with treatment receipt — it needs to predict which patients got called.
2. $U$ needs to be associated with the outcome — it needs to predict 30-day readmission.

The E-value asks: given your observed risk ratio, what is the *minimum* value that both of those associations would need to reach? Not one of them — both. A confounder that strongly predicts treatment but weakly predicts the outcome cannot explain away the finding. A confounder that strongly predicts the outcome but weakly predicts treatment cannot explain it away either. Both arms of the confounding path need to be strong enough.

The E-value gives you a single number — a floor — that represents the minimum strength required in both directions simultaneously. If no real-world confounder can plausibly achieve that strength in both directions, the finding is robust. If you can name a confounder that plausibly could, the finding is fragile.

### The formula

For a risk ratio $RR$ (where $RR > 1$; for $RR < 1$, use $1/RR$):

$$E = RR + \sqrt{RR \cdot (RR - 1)}$$

For the lower bound of the confidence interval ($RR_{lower}$), the same formula applies with $RR_{lower}$ substituted in. This gives you the E-value for the confidence interval bound — the minimum confounding needed to shift the confidence interval to include the null.

Let me work through the hospital numbers.

**Observed risk ratio:** $RR = 0.58$. Since this is less than 1, we use $1/RR = 1/0.58 \approx 1.72$.

**E-value for the point estimate:**

$$E = 1.72 + \sqrt{1.72 \cdot (1.72 - 1)} = 1.72 + \sqrt{1.72 \cdot 0.72} = 1.72 + \sqrt{1.238} = 1.72 + 1.113 \approx 2.17$$

Interpretation: to fully explain away an observed risk ratio of 0.58, an unmeasured confounder would need to be associated with *both* treatment receipt and readmission by a risk ratio of at least 2.17 — after adjusting for all measured covariates.

**E-value for the confidence interval lower bound:**

The 95% CI was [0.41, 0.82]. The lower bound of the CI for $RR = 0.58$ is $RR_{lower} = 0.82$ (the bound closer to the null). Using $1/0.82 \approx 1.22$:

$$E_{CI} = 1.22 + \sqrt{1.22 \cdot 0.22} = 1.22 + \sqrt{0.268} = 1.22 + 0.518 \approx 1.56$$

Interpretation: to shift the confidence interval to include the null, a confounder would need risk ratios of at least 1.56 in both directions with treatment and outcome.

**What these numbers mean before we benchmark them:** A confounder with $RR \geq 2.17$ in both directions would be a moderately strong predictor. It is not an impossibly large number — risk ratios of 2–4 are common in clinical confounders. Whether 2.17 is achievable by a real-world variable in this domain is the benchmarking question, and we will get to it.

![E-value visualization. A 2D plot with "Association with treatment (risk ratio)" on the x-axis and "Association with outcome (risk...](images/11-chapter-sensitivity-analysis-fig-02.png)
*Figure 11.2 — E-value visualization*

### Benchmarking the E-value

A raw E-value of 2.17 is neither alarming nor reassuring on its own. What makes it one or the other is whether you can identify a real-world variable that plausibly achieves that strength.

Hrishi's case study draws on the clinical literature to benchmark three confounders. I want to show you how that reasoning works, because the benchmarking is the intellectually honest part — the part where you have to say whether your finding can be trusted, not just compute a number.

**Medication adherence.** In the heart failure literature, medication non-adherence is associated with approximately 2.5-fold increased readmission risk (a risk ratio of roughly 2.5 for the outcome). Adherent patients are also substantially more likely to answer a post-discharge call — estimates in the literature suggest a risk ratio of approximately 2.0–3.0 for treatment receipt among adherent versus non-adherent patients.

If medication adherence achieves $RR \geq 2.17$ in both directions — and the literature suggests it might — then it is a plausible explanation for the observed finding. This does not mean the calls have no effect. It means the data cannot rule out the possibility that the observed association is driven by the shared cause rather than the intervention.

**Health literacy.** High health literacy is associated with lower readmission risk (RR approximately 1.8–2.0) and higher likelihood of engaging with post-discharge care (RR approximately 1.7–1.9 for answering calls). These estimates fall below the E-value of 2.17 in both directions — health literacy alone is probably insufficient to explain away the finding. But it contributes to the overall unmeasured confounding burden.

**Social support.** Strong social support networks are associated with lower readmission risk (RR approximately 2.0–2.5) and higher phone call receipt (RR approximately 1.5–1.8, as patients with support have someone to help them manage follow-up). Social support alone probably cannot achieve 2.17 in both directions — the treatment-receipt arm is likely below the threshold.

**The honest interpretation:** Medication adherence is the benchmark confounder that comes closest to clearing the E-value threshold on its own. The combination of adherence, health literacy, and social support acting together almost certainly could. The finding is not robust. An analyst who reports this as strong causal evidence for the program is making a claim the data cannot support. An analyst who says "the finding is consistent with a program effect but is sensitive to unmeasured confounding by patient engagement characteristics — specifically, medication adherence achieves a risk ratio close to the E-value threshold in both directions" is reporting honestly.

---

## Section 3: The Rosenbaum Bound — How Much Hidden Bias Could Survive?

The E-value asks about confounders that affect both treatment and outcome. Paul Rosenbaum's sensitivity analysis asks a related but distinct question: *how much hidden bias in treatment assignment could this study tolerate before the test of significance is no longer reliable?*

### The intuition

In a perfectly randomized experiment, two patients with identical observed characteristics have exactly the same probability of receiving treatment. The treatment assignment is unconfounded by definition — the randomization guarantee holds.

In an observational study after propensity score matching, two matched patients have approximately equal predicted probabilities of treatment based on their measured covariates. But their *true* probabilities — including the influence of unmeasured variables — may differ. Rosenbaum's sensitivity parameter Γ (gamma) quantifies that potential discrepancy.

Γ = 1 means the study is free of hidden bias: matched patients have exactly equal odds of treatment. Γ = 2 means the true odds of treatment could differ by up to a factor of 2 between matched patients — one patient could be twice as likely to receive treatment as their match, due to unmeasured variables. Γ = 3 means the true odds could differ by a factor of 3. And so on.

The sensitivity analysis asks: *at what value of* Γ *does the study's conclusion — that the treatment effect is statistically significant — become uncertain?* The higher that threshold, the more robust the finding. The lower it is, the more fragile.

### The mechanics

For a matched observational study, the Rosenbaum sensitivity analysis computes, for each value of Γ, the worst-case p-value under the assumption that matched pairs differ in their true treatment probability by up to a factor of Γ. As Γ increases, the worst-case p-value rises. The sensitivity bound is the value of Γ at which the worst-case p-value first exceeds your significance threshold.

Let me be concrete about what "worst case" means. For each matched pair, the unmeasured confounders could be arranged to either maximize or minimize the evidence for a treatment effect. Rosenbaum's bound asks: if unmeasured confounders were arranged as adversarially as possible — to make the evidence for treatment look as weak as possible — at what level of Γ would significance be lost?

For the hospital readmission analysis, Hrishi's case study finds that the Rosenbaum bound is approximately Γ = 1.6. This means:

- If matched pairs differ in their true treatment probability by up to 60% (Γ = 1.6), the study's result could lose statistical significance under worst-case hidden bias.
- If the true treatment assignment probabilities differ by a factor greater than 1.6 between matched patients — which is plausible if medication adherence strongly predicts both — the statistical significance of the result is not reliable.

A Γ of 1.6 is not high. For context: findings in the medical literature that are considered reasonably robust often have Γ in the range of 2–4. A Γ below 2 means the finding is sensitive to relatively modest hidden bias. It is not evidence against the finding — it is evidence that the finding cannot be taken at face value without further investigation.

![Rosenbaum sensitivity curve. X-axis: Γ (hidden bias parameter), from 1.0 to 3.0. Y-axis: worst-case p-value, from 0 to 0.20. A curve...](images/11-chapter-sensitivity-analysis-fig-03.png)
*Figure 11.3 — Rosenbaum sensitivity curve*

### Interpreting Γ = 1.6 against the domain

Like the E-value, the Rosenbaum bound needs to be interpreted against real-world benchmarks to be meaningful.

Is a Γ of 1.6 achievable by medication adherence? The answer requires translating the concept of "association with treatment assignment" into odds ratios. A patient who is highly adherent to their medication regimen has odds of answering a post-discharge call that are, conservatively, 50–80% higher than a non-adherent patient of similar measured characteristics. That is an odds ratio of approximately 1.5–1.8 — straddling the threshold of Γ = 1.6.

This means the study is sensitive to exactly the kind of confounding that is most plausible in this domain. It does not mean the phone call program is ineffective. It means the data cannot establish effectiveness. The distinction matters enormously when the decision is whether to spend $400,000 scaling a program.

---

## Section 4: What Honest Reporting Looks Like

Here is where I want to be direct with you, because this is the part that most methods training skips.

Computing an E-value is technically straightforward. Computing a Rosenbaum bound is technically tractable. What is hard — and what distinguishes a responsible analyst from a technically proficient one — is what you do with those numbers when they are not what you hoped.

Most analysts encounter sensitivity analyses in one of two modes. In the first mode, the finding is robust: the E-value is high, the Γ is large, the benchmark confounders fall well below the threshold, and the honest report is "this finding holds up to plausible unmeasured confounding." That is the good outcome, and it is what we hope for when we design a study.

In the second mode, the finding is fragile: the E-value is modest, the Γ is low, and one or more benchmark confounders plausibly clears the threshold. This is harder to report. The finding may still be real — the sensitivity analysis does not prove confounding exists, only that it *could* explain the result. But the honest report is "this finding is sensitive to unmeasured confounding of a kind that is plausible in this domain, and caution is warranted before acting on it."

I want to give you language for both modes, because language matters here. The difference between "the results are statistically significant" and "the results are statistically significant but sensitive to unmeasured confounding by patient engagement characteristics" is the difference between a finding that will be acted on immediately and a finding that will be investigated further before $400,000 is committed.

### Three tiers of honest reporting

**Tier 1: The finding is robust.**

The E-value exceeds the realistic range of benchmark confounders. The Rosenbaum Γ is large (≥ 2.5 as a rough guide for moderate robustness). No single plausible confounder clears either threshold. Honest report:

> "The estimated effect (RR = X, 95% CI [a, b]) is robust to unmeasured confounding. An unmeasured confounder would need to be associated with both treatment and outcome by a risk ratio of at least [E-value] to explain away the finding. We identified [benchmark confounder] as the strongest candidate from the literature; its estimated associations fall below this threshold. We interpret the finding as providing meaningful evidence for a treatment effect."

**Tier 2: The finding is sensitive but not implausible.**

The E-value is in the range that one or more plausible confounders could approach. The Rosenbaum Γ is modest (1.5–2.5). The finding is real enough to justify further investigation but not strong enough to act on alone. Honest report:

> "The estimated effect (RR = X) is sensitive to unmeasured confounding. An unmeasured confounder with risk ratios of [E-value] in both directions could explain away the finding. [Benchmark confounder] achieves estimated associations of [values] in this domain — close to but not clearly below this threshold. The finding is consistent with a treatment effect but cannot be distinguished from confounding by [benchmark confounder] using observational data alone. Replication with a stronger design — or direct measurement of [confounder] — is warranted before acting on this finding at scale."

**Tier 3: The finding is fragile.**

The E-value is low enough that common, well-documented confounders could clear the threshold. The Rosenbaum Γ is below 1.5. The honest report is the hardest one to write:

> "The estimated effect is sensitive to unmeasured confounding of a magnitude that is plausible for this domain. [Benchmark confounder] could explain the observed association. We cannot conclude that the treatment had a causal effect on the outcome using observational data. A randomized or quasi-experimental design would be required to establish causality. We report the association as descriptive — consistent with but not establishing a causal effect."

Tier 3 is where honest reporting takes courage. An analyst under pressure to justify a program will not want to write those sentences. A journal reviewer may push back. A department head may ask why you ran the analysis if you cannot make a claim. The answer — and it is the right answer — is that the claim would have been wrong, and wrong claims about healthcare interventions cost people their health.

---

## Section 5: A Worked Example End to End

I want to walk a complete sensitivity analysis from a causal estimate to an honest report, showing every step. I will use a hypothetical scenario so the numbers are clean. The procedure is identical to what you would do with real data.

**Scenario:** A study finds that patients enrolled in a hospital's disease management program have significantly lower emergency department utilization over 12 months. The observational analysis matches enrolled and non-enrolled patients on age, diagnosis, insurance, and prior ED visits. The estimated effect is an incidence rate ratio of 0.71 (enrolled patients have 29% fewer ED visits). 95% CI: [0.58, 0.87]. $p = 0.001$.

The study adjusts for prior ED utilization, which is a strong predictor of future utilization. The analysts are confident in their matching procedure.

**Step 1: State the causal estimand.**

What we want to know: $P(\text{ED visits} \mid do(\text{enrollment} = 1)) - P(\text{ED visits} \mid do(\text{enrollment} = 0))$. We want the effect of *being enrolled* — not the effect of self-selecting into enrollment. This is the distinction that makes unmeasured confounding a threat.

**Step 2: Identify the threat.**

Who enrolls in disease management programs? Patients who are more motivated, more health-literate, and more supported. These same characteristics predict lower ED utilization independently of anything the program does. The back-door path is:

$$\text{Enrollment} \leftarrow \text{PatientEngagement} \rightarrow \text{EDUtilization}$$

Patient engagement (an index of motivation, health literacy, and social support) was not measured.

**Step 3: Compute the E-value.**

The incidence rate ratio is 0.71. For $IRR < 1$, use $1/IRR = 1/0.71 \approx 1.41$.

$$E = 1.41 + \sqrt{1.41 \cdot (1.41 - 1)} = 1.41 + \sqrt{1.41 \cdot 0.41} = 1.41 + \sqrt{0.578} = 1.41 + 0.760 \approx 2.17$$

For the CI lower bound ($IRR_{lower} = 0.87$, $1/0.87 \approx 1.15$):

$$E_{CI} = 1.15 + \sqrt{1.15 \cdot 0.15} = 1.15 + \sqrt{0.172} = 1.15 + 0.415 \approx 1.56$$

**Step 4: Benchmark the E-value.**

Is there a real-world measure of patient engagement that could achieve risk ratios of 2.17 with both enrollment and ED utilization? The chronic disease management literature suggests that high-activation patients (using validated patient activation measures) are approximately 2–3 times less likely to have high ED utilization and are 2–4 times more likely to enroll in care management programs. The benchmarks straddle the E-value threshold.

Interpretation: a patient activation variable, had it been measured, could potentially explain the observed association.

**Step 5: Compute the Rosenbaum bound.**

Suppose the matched analysis yields a Rosenbaum Γ = 1.8 (I am using a round number for clarity; in practice this comes from the `rbounds` package in R or equivalent). This means the study's significance is robust to a 1.8-fold difference in treatment odds between matched pairs.

Is a 1.8-fold difference in treatment odds achievable by patient activation? Yes — the literature suggests activation score differences between high- and low-engagement patients predict enrollment with odds ratios in the 2–3 range. The study is sensitive.

**Step 6: Write the honest report.**

> "The estimated effect of disease management program enrollment on 12-month ED utilization (IRR = 0.71, 95% CI [0.58, 0.87]) is sensitive to unmeasured confounding. To fully explain away the point estimate, an unmeasured confounder would need risk ratio associations of at least 2.17 with both enrollment and ED utilization. Patient activation — a validated construct capturing health motivation, literacy, and self-management capacity — achieves estimated associations in this range in the chronic disease literature, and was not measured in this study. The Rosenbaum sensitivity bound of Γ = 1.8 indicates that a 1.8-fold difference in true treatment odds between matched patients would undermine the significance of the finding. Patient activation plausibly produces differences of this magnitude. We interpret the finding as consistent with a program effect but sensitive to unmeasured confounding by patient engagement characteristics. Scaling the program on this evidence alone is premature; a randomized pilot or direct measurement of patient activation in a follow-up study is recommended."

That report takes three minutes longer to write than "the program significantly reduces ED visits." It is also the report that a hospital board deserves before committing resources.

---

## Section 6: What Sensitivity Analysis Cannot Do

I have been making the case for sensitivity analysis, and I believe in it. But I want to be equally clear about its limits, because a tool that is misunderstood as more powerful than it is will be misused.

**Sensitivity analysis does not tell you whether confounding exists.** It tells you how much confounding would be needed to explain your finding. If the required confounding is implausible, the finding is robust. If it is plausible, the finding is fragile. But if the required confounding is plausible and confounding does not in fact exist — if the finding is real — sensitivity analysis will still flag it as fragile. The method is conservative by design. That is a feature, not a bug. The cost of incorrectly dismissing a real finding is lower than the cost of incorrectly acting on a spurious one.

**Sensitivity analysis does not fix confounding.** If you have an unmeasured confounder, computing an E-value does not remove it. The right response to a fragile finding is not to run more sensitivity analyses — it is to get better data. Measure the confounder directly if you can. Find an instrumental variable. Design a randomized experiment. Sensitivity analysis tells you where the vulnerability is; fixing the vulnerability requires design changes.

**Sensitivity analysis does not validate your DAG.** The analysis is only as good as the benchmark confounders you identify. If you have specified the wrong causal structure — if there are confounding paths you have not considered — the E-value and Γ will not tell you. The benchmark step requires genuine domain knowledge and genuine intellectual honesty. An analyst who benchmarks against only weak confounders to make the finding look robust is doing the analysis backwards.

**The E-value and Rosenbaum bound are different tools for different threats.** The E-value addresses magnitude of confounding: how strong would the unmeasured variable need to be? The Rosenbaum bound addresses treatment assignment bias: how different could the true treatment probabilities of matched pairs be? These are related but distinct questions. A finding could be robust on one dimension and fragile on the other.

---

## A note about AI

Sensitivity analysis is the discipline of asking how wrong an assumption would have to be to overturn the conclusion. The model is biased toward not asking.

Where the model genuinely helps: walking through the E-value, the Γ-value, and the standard sensitivity frameworks on a worked example.

Where the model does damage: declaring a study robust to unmeasured confounding. Robustness is a claim about a specific kind of unmeasured threat, and the model cannot evaluate the threats it has not been told about.

The rule: framework from the model; the robustness claim from the analyst who can name the specific threats.

---

## Exercises

### Warm-Up

**Exercise 1 (Computing an E-value)**
A study finds that employees who participate in a workplace wellness program have a 25% lower rate of sick days over 12 months (RR = 0.75, 95% CI [0.62, 0.91]).

a. Compute the E-value for the point estimate. Show your work using the formula $E = RR + \sqrt{RR \cdot (RR - 1)}$, applied to $1/RR$ since $RR < 1$.

b. Compute the E-value for the confidence interval lower bound (the bound closest to the null).

c. State in plain English what each E-value means.

d. The study did not measure general health consciousness — employees who are more health-conscious are both more likely to join the wellness program and less likely to take sick days. If health consciousness is associated with program participation by RR = 1.9 and with sick day rate by RR = 1.7, is this confounder sufficient to explain away the finding? How do you know?

**Exercise 2 (Interpreting a Rosenbaum Bound)**
An observational study of a tutoring program finds that tutored students have significantly higher test scores than matched untutored students. The Rosenbaum sensitivity analysis finds Γ = 2.4.

a. State in plain English what Γ = 2.4 means for this study.

b. Is this finding more or less robust than the hospital readmission finding (Γ = 1.6)? Explain.

c. The tutoring program was offered only to students who applied. Propose one unmeasured confounder that could explain both application to the program and higher test scores. Estimate qualitatively whether this confounder is likely to achieve the level of treatment assignment bias implied by Γ = 2.4.

### Application

**Exercise 3 (Full E-value Analysis)**
A study finds that neighborhoods with community gardens have lower rates of Type 2 diabetes diagnosis (RR = 0.63, 95% CI [0.49, 0.81]) after adjusting for income, age, and population density.

a. Compute the E-value for the point estimate and the CI lower bound.

b. Identify two plausible unmeasured confounders. For each, estimate qualitatively whether it could achieve the E-value threshold in both directions, citing your reasoning.

c. Classify this finding as Tier 1 (robust), Tier 2 (sensitive but not implausible), or Tier 3 (fragile) using the honest reporting framework from Section 4. Write the appropriate honest report in 3–5 sentences.

**Exercise 4 (Benchmarking Practice)**
A social media company publishes a study showing that users who engage with its "digital wellbeing" features (screen time reminders, app limits) report 15% lower anxiety scores after 60 days (standardized difference = −0.28, equivalent to approximately RR = 0.83 for the outcome being "high anxiety").

a. Compute the E-value.

b. Who is most likely to opt into digital wellbeing features? Propose two benchmark confounders from the psychology literature and estimate their plausible strength.

c. The Rosenbaum sensitivity analysis for this study found Γ = 1.3. What does this tell you about the study's robustness to hidden bias? Is a 1.3-fold difference in treatment odds between matched users plausible given your benchmark confounders?

d. Write an honest report for this finding.

**Exercise 5 (Distinguishing E-value from Rosenbaum)**
Explain in your own words why the E-value and the Rosenbaum bound are measuring different things. Give a concrete scenario where a finding could have a high E-value but a low Γ (robust to magnitude of confounding but fragile to treatment assignment bias), and a scenario where it could have a low E-value but a high Γ.

### Synthesis

**Exercise 6 (End-to-End Analysis)**
A city evaluated the effect of a traffic calming intervention (adding speed bumps and pedestrian crossings to residential streets) on pedestrian injury rates. Treated streets were selected by petition from neighborhood associations. The observational analysis matches treated and untreated streets on traffic volume, street width, posted speed limit, and proximity to schools. The result: pedestrian injuries on treated streets fell by 35% (RR = 0.65, 95% CI [0.51, 0.83]) relative to matched controls.

a. Identify at least two plausible unmeasured confounders. For each, draw the confounding path in the DAG and explain why it was likely not measured.

b. Compute the E-value for the point estimate and CI lower bound.

c. Compute a rough qualitative estimate of whether each benchmark confounder could achieve the E-value threshold. (You do not have literature values in front of you — reason qualitatively from first principles.)

d. The city is considering spending $2M to scale the intervention to 50 additional streets. Based on your sensitivity analysis, write a recommendation to the city's transportation department. Your recommendation should use the Tier 1/2/3 framework and include the specific E-value and Γ information that decision-makers need.

### Challenge

**Exercise 7 (Sensitivity Analysis as Design Tool)**
Sensitivity analysis is typically described as a diagnostic — something you do after the study to check robustness. But it can also be used as a design tool: when planning a study, you can ask in advance how large the E-value would need to be for the finding to be actionable given your domain's benchmark confounders.

a. Suppose you are designing an observational study of an occupational health intervention (standing desks and lower back pain). Before collecting data, you identify three benchmark confounders from the ergonomics literature: general physical activity (estimated RR ~2.0 with both treatment and outcome), baseline musculoskeletal health (estimated RR ~1.7/2.2), and job type — sedentary vs. active (estimated RR ~2.5/2.0).

What is the minimum E-value your finding would need to achieve for you to be confident it survives confounding by the strongest benchmark confounder? What does this imply about the minimum detectable risk ratio you should power your study to detect?

b. Is using sensitivity analysis as a design tool — to set a target E-value before data collection — legitimate? What does it require of the analyst? What could go wrong?

c. Propose one study design feature (beyond measuring the benchmark confounders directly) that would improve the robustness of your standing desk study without running a full RCT.

---

## Chapter Summary

Here is what you can do now that you could not before.

**You can state why sensitivity analysis is required, not optional.** Every observational causal estimate rests on the assumption that you have measured and adjusted for all important confounders. That assumption is untestable from your data. Sensitivity analysis is how you assess the vulnerability of your estimate to violations of that assumption. Reporting an observational finding without sensitivity analysis is not just incomplete — it is claiming more than the data supports.

**You can compute and interpret an E-value.** The formula is $E = RR + \sqrt{RR \cdot (RR-1)}$ (applied to $1/RR$ for $RR < 1$). The number it produces is a minimum threshold: an unmeasured confounder needs to exceed it in *both* directions simultaneously to explain away the finding. That threshold is meaningless until you benchmark it — until you find the strongest plausible confounder in your domain and ask whether it can clear the bar.

**You can compute and interpret a Rosenbaum bound.** Γ quantifies how much hidden bias in treatment assignment the study can tolerate before significance is lost. A low Γ means the finding is sensitive to modest imbalances in unmeasured treatment predictors. Interpreting Γ requires the same benchmarking step: is a Γ-fold difference in treatment odds achievable by a real confounder in your domain?

**You can write an honest report.** Tier 1, Tier 2, or Tier 3. The right tier depends on where your benchmark confounders fall relative to your E-value and Γ. The Tier 3 report — "this finding is fragile, we cannot conclude causality, a stronger design is warranted" — is the hardest to write and the most important. It is what intellectual honesty requires when the data cannot support the claim.

**The Feynman test for this chapter:** Can you explain to a colleague who just showed you a statistically significant observational result why that result might not mean what they think it means — and then show them, using two numbers, how to find out? If yes, you have the chapter. If not, the gap is probably in Section 2 (the E-value benchmarking step) or Section 4 (what to do when the benchmarks are close to the threshold). Go back to whichever feels uncertain.

**The one mistake this chapter is designed to prevent:** Reporting a statistically significant observational result in causal language without asking how much unmeasured confounding the finding could survive. That mistake is common. It is consequential. And it is now, for you, inexcusable — because you have the tools to avoid it.

---

## Connections Forward

This chapter ends the standalone companion series. You have now seen both ends of the methodological spectrum: Chapter 11 asked whether the tools you use to analyze data are reasoning correctly. This chapter asked whether the results those tools produce can be trusted. Together, they form a pair — diagnosis of the reasoning process, and diagnosis of the output.

The deeper question this chapter raises is about study design: if sensitivity analysis reveals that an observational finding is fragile, what do you do? The ideal answer is to collect better data — measure the benchmark confounders directly, find a natural experiment, design a randomized trial. Chapters 4 and 7 of the theory spine cover the design strategies that produce findings robust enough that sensitivity analysis becomes a formality rather than a warning. If you have read those chapters, you now see why they matter not just for internal validity, but for the downstream question of whether your finding can survive scrutiny.

The tools introduced here — E-values, Rosenbaum bounds — are the standard sensitivity toolkit for matched and weighted observational studies. There are other approaches: the partial $R^2$ framework of Cinelli and Hazlett (2020) for regression-based analyses, the generalized sensitivity analysis for instrumental variable estimates, and simulation-based approaches that model the full joint distribution of treatment, outcome, and confounder. Each covers a different class of threat. The spirit is the same: ask how much the world would have to differ from your assumptions to overturn your conclusion, then ask whether that world is plausible.

The answer to that question is always a judgment call. The formulas get you to the threshold. The domain knowledge and intellectual honesty get you to the verdict.

---

## References

Cinelli, C., & Hazlett, C. (2020). Making sense of sensitivity: Extending omitted variable bias. *Journal of the Royal Statistical Society: Series B*, 82(1), 39–67.

Hernán, M. A., & Robins, J. M. (2020). *Causal Inference: What If*. Chapman & Hall/CRC.

Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.

Rosenbaum, P. R. (2002). *Observational Studies* (2nd ed.). Springer.

Rosenbaum, P. R. (2010). *Design of Observational Studies*. Springer.

VanderWeele, T. J., & Ding, P. (2017). Sensitivity analysis in observational research: Introducing the E-value. *Annals of Internal Medicine*, 167(4), 268–274.

---

*Chapter 15 is a standalone companion to the case study by Hrishi Pal. It assumes familiarity with basic causal inference concepts (confounding, observational study design, propensity score methods) at approximately the level of Chapters 1–9 of the theory spine. Readers who want implementation details — R code for `rbounds`, Python implementations of E-value calculations, AIPW estimators — should consult Hrishi's case study notebook, which documents the computational workflow in full.*

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Paul Rosenbaum** developed the modern framework for sensitivity analysis in observational studies — quantifying how strong an unobserved confounder would have to be to overturn a study's conclusions. His E-value and Γ-value formalisms let researchers report uncertainty honestly.

**Run this:**

```
Who is Paul Rosenbaum, and how does his sensitivity analysis framework connect to the sensitivity work we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Paul Rosenbaum"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through an E-value calculation on a specific applied result.
- Ask it to compare Rosenbaum's sensitivity analysis with VanderWeele's E-value approach.

What changes? What gets better? What gets worse?

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 11.1 — DAG for the hospital readmission scenario

Create a standalone D3 v7 HTML figure for "DAG for the hospital readmission scenario". Use a horizontal process diagram with 4 to 5 ordered stages with directed connectors. Marks: rectangular stage nodes and arrow connectors. Channels: position for sequence or category, length for quantitative emphasis when bars are used, color for the primary highlighted item only, and direct text labels for accessibility. Use a zero baseline for quantitative bars. Include title, desc, role="img", aria-labelledby, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Deliver as one HTML file with inline CSS and the D3 7.9.0 CDN.

> Reference implementation: `d3/11-chapter-sensitivity-analysis-fig-01.html`

---

### Figure 11.2 — E-value visualization

Create a standalone D3 v7 HTML figure for "E-value visualization". Use a 2x2 matrix with four quadrants plus axis labels. Marks: bars or rectangular panels, direct labels, and concise value labels. Channels: position for sequence or category, length for quantitative emphasis when bars are used, color for the primary highlighted item only, and direct text labels for accessibility. Use a zero baseline for quantitative bars. Include title, desc, role="img", aria-labelledby, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Deliver as one HTML file with inline CSS and the D3 7.9.0 CDN.

> Reference implementation: `d3/11-chapter-sensitivity-analysis-fig-02.html`

---

### Figure 11.3 — Rosenbaum sensitivity curve

Create a standalone D3 v7 HTML figure for "Rosenbaum sensitivity curve". Use a 2x2 matrix with four quadrants plus axis labels. Marks: bars or rectangular panels, direct labels, and concise value labels. Channels: position for sequence or category, length for quantitative emphasis when bars are used, color for the primary highlighted item only, and direct text labels for accessibility. Use a zero baseline for quantitative bars. Include title, desc, role="img", aria-labelledby, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Deliver as one HTML file with inline CSS and the D3 7.9.0 CDN.

> Reference implementation: `d3/11-chapter-sensitivity-analysis-fig-03.html`
