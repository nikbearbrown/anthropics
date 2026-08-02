# Chapter 1 — The Same Question, Two Answers

*The medical testing problem reveals what frequentist statistics can and cannot say — and introduces the Bayesian alternative that answers the question the test actually asks.*

---

## Learning Objectives

By the end of this chapter you should be able to:

1. **(Understand)** Explain what a p-value does and does not say about a single patient's diagnosis.
2. **(Analyze)** Identify the specific question frequentist hypothesis testing cannot answer about a positive test result.
3. **(Apply)** Compute a posterior probability using Bayes' theorem for a two-hypothesis diagnostic problem.
4. **(Evaluate)** Compare what each approach tells the clinician and what each leaves unanswered.

---

## Opening: The Test That Is 99% Accurate

A patient walks into a clinic and is screened for a rare disease. The test comes back positive. The physician explains that the test is 99% accurate.

What is the probability the patient actually has the disease?

Most people say: 99%. The actual answer — if the disease affects about 1 in 1,000 people in this population — is approximately **9%**.

That gap is not a rounding error. It is a structural consequence of asking two different questions and mistaking them for one.

This chapter shows you both questions, both answers, and exactly why the two approaches differ. It will not resolve the question of which approach is "correct" — that depends on what you need to know and why. What it will do is make sure you never again mistake the frequentist answer for the Bayesian one, or the Bayesian one for the frequentist one.

Before any definitions, try to name the gap. Why might the correct answer be 9% rather than 99%? What information is the "99% accurate" figure not telling you?

---

## The Frequentist Solution

**Null hypothesis testing** (also called NHST — null hypothesis significance testing) asks: *how surprising is this data, assuming the null hypothesis is true?*

For the medical test, set it up as follows.

- **Null hypothesis H₀:** The patient does not have the disease.
- **Alternative hypothesis H₁:** The patient does have the disease.
- **Test result (our data):** Positive test.

The test is 99% accurate. In statistical language:

- **Sensitivity:** P(positive test | disease) = 0.99 — if the patient has the disease, the test flags it 99% of the time.
- **False positive rate:** P(positive test | no disease) = 0.01 — if the patient is healthy, the test incorrectly flags it 1% of the time.

Under the null hypothesis (patient is healthy), the probability of seeing a positive test is:

$$p\text{-value} = P(\text{positive test} \mid H_0) = P(\text{positive test} \mid \text{no disease}) = 0.01$$

The decision rule: reject H₀ at significance level α = 0.01. Since the p-value equals α, we are right at the standard threshold for rejection. In clinical practice, a p-value this small is typically reported as: "reject the null hypothesis; the positive test is statistically significant."

This is the frequentist answer. It is technically correct. A positive result from a test with a 1% false positive rate would be surprising if the patient were healthy.

### Where the Frequentist Answer Strains

Here is what the frequentist analysis does not say and cannot say:

*How likely is it that this patient actually has the disease?*

The p-value is P(data | H₀). The clinician needs P(H₁ | data) — the probability the hypothesis is true given the data. These are not the same quantity. They are not even close to the same quantity in this problem, as the Bayesian calculation will show.

The American Statistical Association's formal statement on p-values makes this explicit: "A p-value does not measure the probability that the studied hypothesis is true" (Wasserstein & Lazar, 2016). This is not a minority position or a Bayesian critique — it is the official statement of the leading professional statistics organization.

What the frequentist test provides is a decision rule with known long-run properties: if we set α = 0.01 and the null is true, we will falsely reject it 1% of the time across many experiments. That is a useful guarantee for a research program. For a single patient sitting in a clinic waiting for news, it does not answer the question.

The clinician cannot act on "the result would be surprising if the patient were healthy." The clinician needs an actionable probability of disease — one that incorporates everything known before the test was run.

---

## The Bayesian Solution

Bayesian inference starts from Bayes' theorem (derived in Chapter 0):

$$P(H \mid D) = \frac{P(H) \cdot P(D \mid H)}{P(D)}$$

For this problem, H = "patient has the disease" and D = "positive test result."

**Step 1: Specify the prior.**

The disease affects 1 in 1,000 people in this population — the prevalence, also called the base rate.

$$P(\text{disease}) = 0.001 \qquad P(\text{no disease}) = 0.999$$

**Step 2: Specify the likelihoods.**

From the test's known performance:

$$P(\text{positive} \mid \text{disease}) = 0.99$$
$$P(\text{positive} \mid \text{no disease}) = 0.01$$

**Step 3: Compute the denominator.**

Using the law of total probability:

$$P(\text{positive}) = P(\text{disease}) \cdot P(\text{positive} \mid \text{disease}) + P(\text{no disease}) \cdot P(\text{positive} \mid \text{no disease})$$

$$P(\text{positive}) = (0.001)(0.99) + (0.999)(0.01) = 0.00099 + 0.00999 = 0.01098$$

**Step 4: Apply Bayes' theorem.**

$$P(\text{disease} \mid \text{positive}) = \frac{(0.001)(0.99)}{0.01098} = \frac{0.00099}{0.01098} \approx 0.0902$$

The posterior probability that the patient has the disease, given a positive test, is approximately **9%**.

### Why Is the Answer 9% and Not 99%?

Look at the denominator: 0.01098. This is the total probability of testing positive. It has two contributions:

- **From people with the disease:** (0.001)(0.99) = 0.00099
- **From healthy people who test falsely positive:** (0.999)(0.01) = 0.00999

About 10 times as many healthy people produce a positive test as do sick people — because there are roughly 1,000 times as many healthy people, even though each healthy person has only a 1/100 chance of a false positive while each sick person has a 99/100 chance of a true positive. The false positives swamp the true positives.

The 9% result is counterintuitive until you see it in natural frequencies (Gigerenzer & Hoffrage, 1995). Imagine 10,000 people screened:

- **10 have the disease.** Of those, 9.9 ≈ **10 test positive** (true positives).
- **9,990 do not have the disease.** Of those, 99.9 ≈ **100 test positive** (false positives).
- Total positive tests: approximately 110.
- Of those 110, 10 have the disease: **10/110 ≈ 9%.**

The test is genuinely useful — it shifted the probability from 0.1% (prior) to 9% (posterior), a 90-fold increase. But a positive test still means the patient probably does not have the disease, because the disease is rare enough that false positives outnumber true positives.

This is not a flaw in the test. It is a consequence of rarity. A confirmatory test, or a test in a higher-prevalence population (a patient with symptoms), changes the posterior substantially. That is the point: the posterior is not a property of the test alone. It depends on who gets tested.

---

## Side-by-Side Comparison

| | Frequentist (NHST) | Bayesian |
|---|---|---|
| **Question answered** | How surprising is a positive test if the patient is healthy? | Given a positive test, how likely is disease? |
| **Uses prevalence (prior)?** | No | Yes — required |
| **Output** | p = 0.01; reject null | P(disease \| positive) ≈ 9% |
| **Clinician's decision** | "Significant" — but ambiguous about what to do | Grounded in 9% probability; suggests confirmatory testing |
| **Long-run property** | Controls false positive rate across experiments | Gives probability for this specific patient |

**Why anyone uses the frequentist approach here.** The frequentist hypothesis test was not designed to answer the diagnostic question. It was designed for a different task: deciding whether experimental data is consistent with a null hypothesis, in a setting where you will run many experiments and want to control your long-run error rate. For that task — the controlled experiment, the clinical trial, the research program — the frequentist framework is well-suited. The problem in this chapter arises when a tool designed for research decisions is repurposed for individual diagnostic decisions. That repurposing is common, and it is the source of the gap.

---

## Worked Example: The Prior Drives the Posterior

**Situation.** A public health official proposes mass screening for Disease X. The test has 99% sensitivity and a 1% false positive rate — the same numbers as before. The official's proposal is to screen all 500,000 residents of a mid-sized city. The disease prevalence in the general population is 1 in 1,000.

**Analytical process.**

The official's intuition: "Our test is 99% accurate — positive results are almost certainly real cases." This is the error the Harvard physicians made (Casscells, Schoenberger & Graboys, 1978). Let us work through why it is wrong.

*Step 1: How many true cases are in the screened population?*

500,000 × 0.001 = 500 people with the disease.

*Step 2: How many false positives?*

499,500 healthy people × 0.01 false positive rate = 4,995 false positives.

*Step 3: Of all positive tests, what fraction are true cases?*

500 true positives / (500 + 4,995) = 500 / 5,495 ≈ **9.1%**

The official will report approximately 5,495 positives to the city's health system. Of those, about 500 are genuinely sick and about 4,995 are not.

*Where a dead end appears:* The official might argue "we should use a more accurate test." Suppose the false positive rate drops from 1% to 0.1%:

499,500 × 0.001 = 499.5 false positives
500 / (500 + 499.5) ≈ **50%**

Better — but still, half of positive results are false positives in a low-prevalence population. The only complete solution is to target screening at higher-prevalence groups (symptomatic patients, high-risk demographics) where the prior shifts the posterior substantially. The Bayesian framework makes this visible; the frequentist framework does not.

*Resolution.* The official's screening program would generate roughly ten times as many false positives as true cases. Each false positive is a person who receives anxiety, follow-up testing, possibly unnecessary treatment. The Bayesian calculation is the tool that reveals this — not as a theoretical concern, but as a concrete operational forecast.

**The lesson:** The posterior is not a property of the test in isolation. It depends on who gets tested and what the disease prevalence is in that population.

**The limit:** This analysis assumed the prevalence estimate is accurate. In practice, disease prevalence estimates carry their own uncertainty. A Bayesian analyst who wanted to propagate that uncertainty would need a prior distribution over prevalence — the topic of Chapters 7 and 8.

---

## Prompting for Implementation (Preview)

You have now done this calculation by hand for one set of numbers. Chapter 2 will teach you how to prompt an LLM to do it for any combination of prevalence, sensitivity, and false positive rate. For now, a bridge exercise:

By hand, recompute the posterior for the following three prevalence values. Keep the test parameters fixed: P(positive | disease) = 0.99, P(positive | no disease) = 0.01.

- Prevalence = 0.001 (1 in 1,000) — the case in this chapter.
- Prevalence = 0.01 (1 in 100).
- Prevalence = 0.1 (1 in 10).

What happens to the posterior as prevalence increases? What does this tell you about when a positive test is strong evidence?

In Chapter 2, you will prompt an LLM to generate this calculation for any prevalence you name — and learn to verify that the LLM's interpretation (not just its arithmetic) is correct.

---

## Common Misconceptions

**Misconception 1: "The 9% answer means the test is useless."**

The test moved the probability from 0.1% to 9% — a 90-fold increase. That is a meaningful update. The right response to a 9% posterior is not "ignore the result" but "get a confirmatory test" or "reassess the prior" (Is this patient symptomatic? Are they in a high-risk group?). The test is informative; it just does not, by itself, establish disease. A tool that moves a probability from 0.1% to 9% is not useless — it is doing exactly what a test should do. The error is treating a 9% posterior as if it were a 99% posterior.

**Misconception 2: "The p-value of 0.01 means there is a 1% chance the patient is healthy."**

This is the most common misreading of the p-value in clinical settings. The p-value is P(positive test | patient is healthy) = 0.01. It is not P(patient is healthy | positive test). The first is about the test's behavior when applied to healthy people; the second is what the clinician needs. The American Statistical Association's statement is unambiguous: the p-value does not measure the probability that the null hypothesis is true (Wasserstein & Lazar, 2016). Surveys of academic researchers consistently find that most misread p-values in exactly this way; one study found the misinterpretation prevalent across fields, not only among non-statisticians (Lyu et al., 2020).

**Misconception 3: "The Bayesian approach requires subjective judgment that taints the analysis."**

The prior — prevalence 0.001 — was not guessed. It came from epidemiological data about the disease in this population. Using it is not an act of subjectivity; it is using available information rather than ignoring it. Ignoring the prior (the frequentist approach) is also a choice — it is choosing to treat the question as if the prior does not exist. That choice has consequences, as the 9% vs. 99% gap demonstrates. The question is not whether to have a prior but whether to name it.

---

## AI Wayback Machine: Florence Nightingale

**Florence Nightingale** (1820–1910) is remembered as the founder of modern nursing. She should also be remembered as a statistician. During the Crimean War, Nightingale collected systematic mortality data from British military hospitals and used it to show that soldiers were dying primarily from preventable infectious disease — not from battle wounds — at rates far above what anyone in the War Office had acknowledged.

Her contribution was not just the data collection but the presentation. She developed the polar-area diagram (sometimes called the "coxcomb" chart) to display seasonal mortality causes in a form that was compelling to non-statisticians — specifically, to the government officials who needed to act on it. Her goal was to answer the decision-maker's actual question: "Is this dying preventable, and if so, how?" — the same structure as Chapter 1's question: "What does this positive test mean, and what should the clinician do about it?"

Nightingale understood that statistical reasoning in service of a decision requires more than a correct calculation. It requires communicating the result to someone with the authority and motivation to change behavior. The Bayesian posterior in this chapter — 9%, not 99% — is not just a number. It is the input to a decision. Nightingale's work is an early example of statistics as decision support, not just description.

---

## Exercises

**Exercise 1 (Apply).** Recompute the posterior probability P(disease | positive test) for the following prevalence values, keeping sensitivity = 0.99 and false positive rate = 0.01 throughout:

(a) Prevalence = 0.01 (1 in 100).  
(b) Prevalence = 0.1 (1 in 10).  

Show the full Bayes' theorem calculation for each. What does the pattern tell you about how the positive predictive value of a test depends on prevalence?

**Exercise 2 (Analyze).** A forensic expert testifies at trial: "The defendant's DNA matches the crime scene sample. The probability of this match occurring by chance in an unrelated person is 1 in 1,000,000. Therefore, the defendant is almost certainly guilty."

(a) Identify the conditional probability the expert calculated.  
(b) Identify the conditional probability the jury needs.  
(c) What additional information is required to compute the quantity the jury needs?  
(d) Using the logic from this chapter, explain in two sentences what is wrong with the expert's argument. (Note: this type of reasoning error has been documented in legal proceedings and analyzed in National Research Council, 2009.)

**Exercise 3 (Evaluate).** A public health official wants to screen all 200,000 residents of a county for a condition that affects 0.5% of the general population. The available test has 95% sensitivity and a 2% false positive rate.

(a) Compute the expected number of true positives, false positives, and false negatives.  
(b) Compute the posterior probability P(condition | positive test).  
(c) Write a two-sentence briefing for the official explaining what the screening program will find — and what the most important operational implication is.

---

## What Would Change My Mind

This chapter claims that the frequentist p-value and the Bayesian posterior are answering different questions, and that for the individual diagnostic decision the clinician needs the posterior, not the p-value. I would revise this claim if I encountered a principled argument that the long-run error-rate guarantee of the frequentist test is the correct criterion for individual diagnostic decisions — not just for research programs — and that probability statements about individual cases are not meaningful. Some frequentist statisticians hold a view close to this (frequentist probability is only defined for repeatable experiments; individual cases are not the domain of probability), and if that view is defensible for clinical decisions, the chapter's framing needs revision. The version of this argument I find most credible is in Senn (2011), who argues that much Bayesian practice is less principled than its advocates claim. I do not find it ultimately convincing for the diagnostic case, but it is the strongest objection.

---

## Still Puzzling

1. This chapter used a point estimate for prevalence (0.001 exactly). In reality, disease prevalence is measured with uncertainty. How would you incorporate uncertainty in the prior itself — a distribution over possible prevalence values rather than a single number? (Addressed in Chapter 7.)

2. The worked example suggested that a high-risk patient's higher prevalence would shift the posterior. How much higher does prevalence need to be before a single positive test is strong evidence? Is there a threshold?

3. The chapter showed that two sequential tests (first an imperfect screening test, then a confirmatory test) effectively perform two Bayesian updates. Is this equivalent to designing a single, better test from the start, or does sequencing add something the arithmetic of a single test cannot capture?

4. The frequentist test in this chapter used a p-value of 0.01. But α = 0.05 is the more common threshold in research. Does the choice of α affect the analysis — and what does the choice of α correspond to in Bayesian terms?

---

## Bridge to Chapter 2

You have seen that the Bayesian calculation requires one thing the frequentist test ignores: the prior probability. For this chapter's numbers, you computed the posterior by hand. In Chapter 2, you will learn to prompt an LLM to run this calculation for any disease prevalence and test accuracy — and, more importantly, to verify that the LLM's interpretation is correct, not just its arithmetic. The verification skill matters because an LLM, like the Harvard physicians, can produce a plausible-sounding answer to the wrong question.
