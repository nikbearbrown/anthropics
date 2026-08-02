# Chapter 2 — Prompting for Statistics

*Learn to use an LLM as a statistical implementation partner — describing problems precisely, verifying outputs critically, and iterating toward solutions that match what the math actually requires.*

---

## ⚠️ Aging Notice

This chapter is the highest aging-risk chapter in the book. The durable skill it teaches — how to specify a statistical problem precisely and verify the output against the problem's structure — will not change. The specific models named, and the exact quirks of any particular interface, will age within months. Read accordingly: the principles are stable; the footnotes on current tools are snapshots, not specifications.

---

## Learning Objectives

By the end of this chapter you should be able to:

1. **(Apply)** Prompt an LLM to implement a two-hypothesis Bayesian inference problem and verify the result against your hand calculation.
2. **(Analyze)** Identify when an LLM's statistical output is wrong by checking it against the problem's structure.
3. **(Apply)** Prompt for both frequentist and Bayesian solutions to the same problem and compare the outputs.
4. **(Create)** Write a statistical problem description precise enough that an LLM produces correct, verifiable code on the first attempt.

---

## Opening: The Unfinished Calculation

In Chapter 1 you left the medical testing problem with three open computations:

> *Recompute the posterior for disease prevalence = 0.001, 0.01, and 0.1.*

You can do each one by hand in about two minutes using the formula from Chapter 0. But what happens when the problem has five prevalence values instead of three? Or ten thousand, because you want to plot the relationship? Or a continuous predictor, a hierarchical grouping structure, or a time series of 52 weeks?

At that point, implementation by hand is not a practical option. You need code.

The question this chapter answers is: how do you get correct code — and equally important, correct *interpretation* — from an LLM that can produce plausible-looking wrong answers?

That question has two parts. First: code that runs without errors can still compute the wrong thing. Second: code that computes the right thing can still be accompanied by an interpretation that describes a different result than the one that was computed. Both errors occur, and the second is harder to catch than the first.

A peer-reviewed study published in *Frontiers in Artificial Intelligence* (2025) evaluated four prompting strategies for statistical reasoning tasks using current LLMs. Zero-shot prompting — asking "run a t-test on this data" without further specification — failed consistently on inferential tasks because the LLM did not check assumptions or correctly identify the target quantity. [CURRENT — flag for revision; see DOI: 10.3389/frai.2025.1658316; full authorship unverified — verify before final citation.] The pattern is documented elsewhere too: research on LLM code generation identifies a class of "semantic errors" where the model produces syntactically correct code that implements a different problem than the one specified (cf. CodeHalu, arXiv:2405.00253 — verify journal status before final citation).

This chapter is about preventing and catching those errors.

---

## Block 1: Why Prompting for Statistics Is Different

Prompting an LLM for a poem or a cover letter has a natural verification step: you read it and decide whether you like it. Prompting for statistical analysis is different because:

1. **Statistical code that runs without errors can compute the wrong thing.** A Python script that fits a one-sample t-test when you needed a two-sample t-test will run cleanly and produce a p-value. The p-value will be wrong. The error is invisible unless you know what a two-sample t-test looks like.

2. **Statistical interpretation can be wrong even when the numbers are correct.** An LLM that correctly computes P(positive | no disease) = 0.01 and then writes "this means the patient has a 99% chance of being disease-free" has computed the right number and drawn the wrong conclusion. You will not catch this error by checking the arithmetic.

3. **LLMs default to frequentist methods in most contexts.** The training data distribution of statistical text skews heavily toward frequentist methods (p-values, confidence intervals, t-tests), because that is what most published statistics papers use. If you ask an LLM for "a statistical analysis" without specifying the framework, you will almost certainly get a frequentist one — and a description that may use Bayesian-sounding language to describe it. You must specify "Bayesian posterior probability" explicitly.

4. **Verification requires knowing what the correct output should look like.** This is the load-bearing skill this chapter teaches: before you can catch an error, you have to know what correct looks like. That requires the statistical understanding you are building in this book. The LLM will not tell you its output is wrong.

Mathematical computation by current LLMs is generally reliable for the level of arithmetic in this book. The verification burden has shifted from "did the model get the arithmetic right?" to "did the model answer the question I actually asked?" The former is usually fine; the latter requires your attention.

---

## Block 2: The Anatomy of a Good Statistical Prompt

A statistical prompt has five components. Leaving any of them out increases the probability of an error.

**1. State the data generating process, not just the data.**

Weak: "Here is a dataset with test results. Analyze it."  
Better: "A patient tested positive on a binary diagnostic test. The data generating process is: each person either has the disease (probability = prevalence) or does not. If they have the disease, the test is positive with probability 0.99. If they do not, the test is positive with probability 0.01."

The data generating process tells the LLM which probability model to fit. Without it, the LLM infers a model from context — and may infer the wrong one.

**2. Name the quantity you want, not just the analysis.**

Weak: "What does the positive test tell us?"  
Better: "Compute P(disease | positive test) — the posterior probability that this patient has the disease given that the test was positive."

"What does this tell us?" invites the LLM to answer a question of its choosing. Naming the quantity directs it to the quantity you need.

**3. Specify both frameworks explicitly when you want a comparison.**

The standard comparative prompt for this book is:

> *Solve [PROBLEM] using both a frequentist hypothesis test and a Bayesian posterior calculation. Show the mathematical steps for each, implement both in [language], and explain in plain language what each result means and what each approach cannot tell us.*

This template appears in every chapter's prompting section from Chapter 3 onward. Introducing it here makes it reusable.

**4. Ask for the mathematical steps, not just the code.**

Weak: "Write Python code to compute the posterior probability."  
Better: "Show the mathematical steps for Bayes' theorem first, then implement those steps in Python."

When an LLM explains its reasoning before coding, errors in the reasoning become visible. Research on "chain-of-thought prompting" confirms that models perform better on inferential tasks when they reason through the steps explicitly (*Frontiers in AI*, 2025). The durable principle is: ask for the reasoning, not just the result.

**5. Request a plain-language interpretation alongside the output.**

Weak: "Compute the posterior and show the result."  
Better: "Compute the posterior and explain what it means for a clinician deciding whether to pursue further testing. Specifically: is the posterior the probability of disease given a positive test, or the probability of a positive test given disease? State which quantity is which."

This last instruction directly guards against the most common LLM interpretation error in statistical contexts: reporting sensitivity as positive predictive value, or reporting a p-value as a posterior probability.

---

## Block 3: Finishing Chapter 1's Open Problem

Here is what a well-specified prompt for Chapter 1's computation looks like. Read it in full before examining the output.

---

**PROMPT:**

> A patient has tested positive for a rare disease. Use Bayes' theorem to compute the posterior probability that the patient actually has the disease.
>
> Parameters:
> - Disease prevalence: P(disease) = 0.001 (1 in 1,000 people have this disease)
> - Test sensitivity: P(positive test | disease) = 0.99
> - False positive rate: P(positive test | no disease) = 0.01
>
> Steps required:
> 1. Write out Bayes' theorem in symbolic form for this problem.
> 2. Substitute the numerical values.
> 3. Compute the denominator using the law of total probability.
> 4. Compute the posterior P(disease | positive test).
> 5. Interpret the result: explain what this number means for the clinician, and state explicitly whether it is P(disease | positive test) or P(positive test | disease).
>
> Implement this in Python and verify by also expressing the solution using natural frequencies (a population of 10,000 people).

---

A well-functioning LLM should return something close to this:

---

**LLM OUTPUT (representative):**

> **Bayes' theorem:**
> P(disease | positive) = P(disease) × P(positive | disease) / P(positive)
>
> **Denominator via law of total probability:**
> P(positive) = P(disease) × P(positive | disease) + P(no disease) × P(positive | no disease)
> P(positive) = (0.001)(0.99) + (0.999)(0.01) = 0.00099 + 0.00999 = 0.01098
>
> **Posterior:**
> P(disease | positive) = 0.00099 / 0.01098 ≈ 0.0902
>
> **Natural frequency check:**
> In 10,000 people: 10 have disease, 9,990 do not.
> True positives: 10 × 0.99 ≈ 10
> False positives: 9,990 × 0.01 ≈ 100
> P(disease | positive) = 10 / 110 ≈ 0.091 ✓
>
> **Interpretation:** This result — approximately 9% — is P(disease | positive test), the probability the patient actually has the disease given that the test was positive. This is *not* the test's sensitivity of 99%, which is P(positive test | disease). Even though the test is 99% sensitive, a positive result means there is roughly a 1-in-11 chance of disease, because the disease is rare: false positives from healthy people outnumber true positives from sick people.

---

This output is correct. But notice what we asked for that produced the correctness: we named the quantity (P(disease | positive)), we asked for the interpretation to explicitly distinguish it from sensitivity, and we requested a natural frequency cross-check. Without those instructions, the LLM might have produced the correct computation but concluded with something like: "The test is 99% accurate, so the patient has a 99% probability of having the disease."

**Verification against hand calculation:** The output of 0.0902 matches the hand calculation from Chapter 1 (0.090). The natural frequency version (10/110 ≈ 0.091) matches within rounding. Verification is satisfied.

---

## Block 4: When to Iterate

Even with a well-specified prompt, the first output will sometimes be wrong. Here is a documented failure mode and the iteration that fixed it.

---

**PROBLEM IDENTIFIED: Correct computation, wrong interpretation.**

Suppose the LLM's output ended with this paragraph instead of the one above:

> *"The posterior probability of 9% is low, which means the test is not very useful. The sensitivity is only 9%, which is below acceptable clinical thresholds."*

This sentence is wrong in a specific way: it describes the posterior as the test's sensitivity. Sensitivity is P(positive | disease) = 0.99; the posterior is P(disease | positive) = 0.09. The LLM has confused two conditional probabilities — the exact confusion that Chapter 0 and Chapter 1 were designed to prevent.

**REVISED PROMPT:**

> Your computation is correct but the interpretation contains an error. Sensitivity is P(positive | disease), which is 0.99 in this problem. Positive predictive value (PPV) is P(disease | positive), which you correctly computed as ~0.09. Please rewrite the interpretation paragraph, correctly using these two quantities and making clear which one is 9% and which one is 99%.

**REVISED OUTPUT (representative):**

> *The positive predictive value (PPV) — P(disease | positive test) — is approximately 9%. This means that of all patients who test positive, about 9% actually have the disease. The test's sensitivity — P(positive test | disease) — is 99%, meaning the test almost never misses a case. The low PPV despite high sensitivity occurs because the disease is rare: most positive tests come from the large pool of healthy people, even though each healthy person has only a 1% chance of a false positive.*

---

This is the correctly interpreted result. The iteration required knowing what the error was — which required knowing the distinction between sensitivity and positive predictive value from Chapter 1.

**The lesson from this iteration:** The LLM did not know its first interpretation was wrong. It produced a fluent, confident-sounding paragraph with a factual error. You found the error because you knew the correct answer from Chapter 1. The verification skill and the statistical knowledge are inseparable.

---

## Block 5: Failure Mode Taxonomy

These are the four most common ways LLM statistical output goes wrong. Name them so you can look for them.

**Failure Mode 1: Correct code, wrong model.**  
The LLM implements a statistical test that runs without error and produces output — but for a different problem. Examples: running a one-sample t-test when you need a two-sample test; fitting a linear model to binary data; computing a confidence interval on the mean when you asked for a proportion. Diagnosis: check that the degrees of freedom, the test structure, and the output quantity match what the problem calls for.

**Failure Mode 2: Correct model, wrong interpretation.**  
The mathematics is correct but the plain-language explanation describes a different quantity. The most common version in this book: describing a p-value as a posterior probability ("there is a 1% chance the null is true") or describing sensitivity as positive predictive value. Diagnosis: identify the specific numerical quantity, verify its definition, and check whether the interpretation uses the correct definition.

**Failure Mode 3: Frequentist answer in Bayesian language.**  
The LLM produces a frequentist analysis but uses language suggesting it answered a Bayesian question. Example: reporting "the probability that the effect is real is 0.97" based on a p-value of 0.03. This is wrong. The p-value does not give the probability that the null hypothesis is false; that requires a prior and Bayes' theorem (Wasserstein & Lazar, 2016). Diagnosis: ask explicitly "what framework is this analysis using — frequentist or Bayesian?" and verify that the output matches.

**Failure Mode 4: Missing the prior entirely.**  
The LLM produces a Bayesian-sounding analysis but omits the prior, or implicitly uses a flat (uniform) prior without saying so. A uniform prior is a prior; it just treats all values as equally likely before seeing any data. If the problem has relevant prior information (disease prevalence, historical defect rate, previous studies), the uniform prior may be a poor choice. Diagnosis: ask the LLM to state what prior it used and justify it.

---

## Common Misconceptions

**Misconception 1: "If the code runs without errors, the analysis is correct."**

Code execution and correctness are independent. A correctly running Python script can compute the wrong test statistic, condition on the wrong event, or report a sensitivity when you asked for a positive predictive value. The only check for statistical correctness is knowing what the correct answer should look like. For the problems in this book, that means verifying the Bayesian calculation against your hand computation from Chapter 1 (or from subsequent chapters), and checking that the interpretation correctly names the quantity computed.

**Misconception 2: "More detailed output means more reliable output."**

LLMs produce verbose, confident-sounding text. Length is not a proxy for accuracy. A four-paragraph interpretation can be wrong in its second sentence while being perfectly correct about everything else. The check is targeted: identify the specific claim that matters (is this P(disease | positive) or P(positive | disease)?) and verify that claim specifically. Ignore length; evaluate precision.

**Misconception 3: "I can prompt my way around needing to understand the statistics."**

You cannot — and this is a feature of the book's design, not a limitation to work around. The LLM will implement whatever framework you specify, but it cannot tell you which framework is appropriate for your problem. An LLM asked to "run a statistical test" will produce a frequentist test by default, because that is what the training data mostly contains. An LLM asked to "run a Bayesian analysis" will attempt one, but whether a Bayesian analysis is appropriate, what prior is defensible, and whether the output answers the decision-maker's actual question — these require the statistical understanding this book is building. The prompting skill amplifies statistical knowledge; it does not substitute for it.

---

## AI Wayback Machine: Grace Murray Hopper

**Grace Murray Hopper** (1906–1992) was an American mathematician, computer scientist, and United States Navy Admiral who is credited, among many other contributions, with developing the first compiler for a programming language and with insisting that computers should speak human-readable languages rather than binary machine code. She is also associated with the origin of the term "debugging" — her team in 1947 found a literal moth inside a relay of the Harvard Mark II, and she taped it into the logbook with the note "First actual case of bug being found."

The debugging story is a useful one for this chapter. Hopper's principle was that code must be understandable by humans and verifiable against human expectations, not simply executable by machines. The fact that a program runs does not establish that it does what you intended. Finding the discrepancy — debugging — requires a human who can read both the specification and the output.

Chapter 2's verification principle is Hopper's principle applied to statistical code: a prompt that runs and produces output has not necessarily produced the output you needed. Finding the discrepancy requires you to know what correct output looks like. Hopper insisted on human-readable code so that debugging was possible; this chapter insists on human-verifiable statistical reasoning so that statistical errors are catchable. The tools are different. The epistemic principle is the same.

---

## Exercises

**Exercise 1 (Apply).** Prompt an LLM to compute P(disease | positive test) for the following five prevalence values: 0.001, 0.01, 0.05, 0.1, and 0.3. Use the same test parameters from Chapter 1: sensitivity = 0.99, false positive rate = 0.01.

(a) Write out the full prompt you will use, following the anatomy from Block 2.  
(b) Record the LLM's outputs for all five values.  
(c) Verify two of the five values by hand calculation. Choose the two values that would best reveal an error if one were present — explain why you chose those two.  
(d) Does the LLM's interpretation of the results correctly explain how the posterior changes as prevalence increases? If not, write the corrected prompt.

**Exercise 2 (Analyze).** Below is a (constructed, representative) LLM output for the following prompt: "A researcher tests whether a new drug reduces blood pressure. The two-group data are provided. Run a statistical analysis and tell me whether the drug works."

> *LLM OUTPUT: I ran a t-test comparing the two groups. The p-value is 0.023. This means there is a 97.7% probability that the drug is effective. The result is statistically significant at α = 0.05, confirming that the new drug reduces blood pressure.*

(a) Identify the failure mode from the taxonomy in Block 5. Name it.  
(b) Identify the specific sentence where the error occurs.  
(c) Write a corrected interpretation paragraph.  
(d) Write a revised prompt that would have prevented this error.

**Exercise 3 (Create).** A diagnostics manufacturer has a new test for a viral infection. The infection affects 3% of the population during flu season. The test has 97% sensitivity and a 4% false positive rate.

Write a prompt that asks an LLM to:
- Compute P(infection | positive test) using Bayes' theorem
- Compute the frequentist p-value for a positive result
- Show the mathematical steps for both
- Provide a plain-language interpretation that correctly distinguishes what each result means
- Flag which quantity each result corresponds to (prior, likelihood, posterior, p-value)

Your prompt should be precise enough that an LLM produces correct, verifiable output on the first attempt. After writing the prompt, run it (or predict what a correct output would contain) and identify which two values you would verify by hand.

---

## What Would Change My Mind

This chapter teaches prompting as a durable skill grounded in statistical verification. The implicit claim is that even as LLM capabilities improve, the human verification step remains essential — because the student must still identify which framework is appropriate and verify that the LLM implemented it. I would revise this claim if future LLMs reliably and transparently audited their own statistical reasoning — explicitly stating the framework used, the prior assumed, the quantity computed, and the degree of confidence in the interpretation, in a form the student could check without statistical background. That capability does not exist in current systems; the research on LLM statistical output (arXiv:2511.04213, arXiv:2511.07628 — verify publication status) documents ongoing errors in interpretation even when computation is correct. If that capability develops, the chapter would shift from "verify everything" to "verify the judgment calls," but the underlying principle — that statistical reasoning requires understanding what the correct answer looks like — would survive.

---

## Still Puzzling

1. This chapter treated prompting as a skill to be learned once and applied uniformly. But different statistical tasks may require very different prompts — asking for a posterior is structurally different from asking for a model comparison or a hierarchical posterior. Is there a general framework for statistical prompt anatomy, or must it be learned separately for each class of problem?

2. The failure modes in Block 5 were identified by reasoning from how LLMs work and what statistical errors are common. They have not been validated as a complete or definitive taxonomy by systematic research. What would a rigorous taxonomy of LLM statistical errors look like, and how would it be constructed?

3. This chapter assumed that the verification step (checking two values by hand) is always feasible. For Chapter 9's hierarchical models or Chapter 10's time series models, hand verification of the full posterior is not possible. What does verification look like when the model is too complex to compute by hand?

---

## Bridge to Chapter 3

From here forward, every chapter includes a prompting section that applies this skill to that chapter's problems. You will not need to implement everything from scratch — but you will need to know enough to tell when the implementation is wrong. In Chapter 3, the problem is estimating a proportion: a quality control engineer tests 50 circuit boards and finds 8 defective. You will see for the first time the difference between a confidence interval and a credible interval — two intervals that look similar on the page but answer different questions. The prompting section in Chapter 3 will apply the template from Block 4 to both.
