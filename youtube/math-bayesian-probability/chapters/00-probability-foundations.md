# Chapter 0 — Probability Foundations

*Everything you need before Chapter 1 — conditional probability, Bayes' theorem as arithmetic, nothing more.*

---

## Learning Objectives

By the end of this chapter you should be able to:

1. **(Remember)** State the definition of conditional probability P(A|B).
2. **(Apply)** Compute P(A|B) from a joint probability table.
3. **(Apply)** Apply Bayes' theorem to a two-hypothesis problem by hand.
4. **(Understand)** Explain why P(A|B) ≠ P(B|A) and where confusing them causes harm.

---

## Opening: The Question Before the Question

Before Chapter 1 can show you what frequentist statistics cannot do, you need one tool it does not provide: a way to update a probability estimate when you learn something new.

Here is the simplest possible version of that problem. An urn holds 3 red balls and 7 blue balls. You draw one ball without looking. Your friend peeks and says: "It's not blue." What is the probability the ball is red?

Your gut says 100%. And your gut is right — but only because the problem is so clean. The moment the problem gets messier — a test that is not perfect, a disease that is not certain — the gut fails. What you need is a formula that works even when the gut doesn't.

That formula is the topic of this chapter.

---

## Joint Probability and the Multiplication Rule

Start with two events, A and B. The **joint probability** P(A∩B) — read "P of A and B" — is the probability that both occur. If you draw a card from a standard deck, P(red ∩ ace) = 2/52, because there are two red aces in 52 cards.

The **multiplication rule** connects joint probability to individual probabilities:

$$P(A \cap B) = P(A) \cdot P(B \mid A)$$

Read this as: the probability that both A and B happen equals the probability that A happens times the probability that B happens *given* A already happened. The term P(B|A) is a **conditional probability** — we have not defined it formally yet, but you already have an intuition for it. If A = "it is raining" and B = "the street is wet," then P(B|A) is close to 1; if A and B are unrelated, P(B|A) = P(B).

---

## Conditional Probability: The Definition

**Conditional probability** answers the question: given that B happened, what is the probability of A?

The formal definition is:

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)} \quad \text{provided } P(B) > 0$$

Why does this make sense? When you learn that B occurred, you restrict your attention to outcomes where B is true. Among those outcomes, you ask what fraction also include A. That is exactly what the formula computes: P(A∩B) is the share of outcomes where both happen; dividing by P(B) rescales to the world where B is certain.

**Example.** In a class of 100 students, 40 passed the exam (P = 0.40), 30 studied all night (P = 0.30), and 25 both studied all night and passed (P = 0.25). What is the probability that a randomly selected student passed, given that they studied all night?

$$P(\text{passed} \mid \text{studied}) = \frac{P(\text{passed} \cap \text{studied})}{P(\text{studied})} = \frac{0.25}{0.30} \approx 0.833$$

Among students who studied all night, about 83% passed. That is a conditional probability.

---

## The Asymmetry: Why P(A|B) ≠ P(B|A)

This is the most important fact in the chapter, and the most reliably ignored.

In the class example above:

$$P(\text{passed} \mid \text{studied}) = \frac{0.25}{0.30} \approx 0.833$$

$$P(\text{studied} \mid \text{passed}) = \frac{0.25}{0.40} = 0.625$$

These are different numbers because they answer different questions. P(passed | studied) asks: among students who studied, how many passed? P(studied | passed) asks: among students who passed, how many studied?

The error of confusing these two is sometimes called the **inverse fallacy** or the **confusion of the inverse**. It is not a beginner's error. In a study of 60 faculty and trainees at Harvard Medical School teaching hospitals, most gave the wrong answer to a medical probability question that required distinguishing these two directions of conditioning (Casscells, Schoenberger & Graboys, 1978). In a separate study, Eddy (1982) found that 95 of 100 physicians estimated a quantity that was ten times larger than the Bayesian answer — because they substituted P(positive test | cancer) for P(cancer | positive test). [UNVERIFIED: exact "95 of 100" figure — Eddy 1982, pp. 249–267, Cambridge UP volume; verify against original.]

Chapter 1 is built on this asymmetry. The test's sensitivity — P(positive | disease) — is not the same as what the clinician needs: P(disease | positive). Keep that distinction in mind. It will matter.

**A useful mnemonic:** read P(A|B) as "A *given* B." The thing after the bar is what you already know. P(positive | disease) means: given the patient has the disease, what is the probability the test is positive? P(disease | positive) means: given the test is positive, what is the probability the patient has the disease? Different questions.

---

## Bayes' Theorem as Arithmetic

Bayes' theorem follows directly from the conditional probability definition in two lines.

From the definition: P(H|D) = P(H∩D) / P(D).

The multiplication rule says P(H∩D) = P(H) · P(D|H).

Substituting:

$$\boxed{P(H \mid D) = \frac{P(H) \cdot P(D \mid H)}{P(D)}}$$

That is Bayes' theorem. It tells you P(H|D) — the probability of hypothesis H given data D — in terms of three quantities you may be able to specify directly:

- **P(H)** — the **prior probability**: how probable is H before seeing D?
- **P(D|H)** — the **likelihood**: if H is true, how probable is this data?
- **P(D)** — the **marginal probability of the data**: over all possibilities, how probable is D?

For a two-hypothesis problem with H and its complement ¬H (read "not H"), P(D) expands as:

$$P(D) = P(H) \cdot P(D \mid H) + P(\neg H) \cdot P(D \mid \neg H)$$

This is the **law of total probability**. It simply says: the probability of seeing D equals the probability of seeing D when H is true (weighted by how likely H is) plus the probability of seeing D when H is false (weighted by how likely H is false).

The full two-hypothesis form of Bayes' theorem is:

$$P(H \mid D) = \frac{P(H) \cdot P(D \mid H)}{P(H) \cdot P(D \mid H) + P(\neg H) \cdot P(D \mid \neg H)}$$

This looks intimidating. It is not. It is fraction arithmetic. Chapter 1 will run this formula on a real problem, step by step.

---

## Worked Example: The Urn

**Setup.** An urn contains 3 red balls and 7 blue balls (10 total). You draw one ball without looking. Your friend, who can see the ball, tells you it is not blue. What is the probability the ball is red?

**Build the table first.** Before using the formula, visualize the joint distribution:

|                    | Red ball | Blue ball | Total |
|--------------------|----------|-----------|-------|
| Friend says "red"  | 3        | 0         | 3     |
| Friend says "blue" | 0        | 7         | 7     |
| **Total**          | 3        | 7         | 10    |

Your friend says "not blue," which means "red" in this problem. Looking at the table: the "friend says red" row has 3 red and 0 blue. So P(red | friend says not blue) = 3/3 = 1. The ball must be red.

Now verify this with Bayes' theorem directly.

Let H = "ball is red" and D = "friend says not blue."

- **P(H) = 3/10** — three of ten balls are red.
- **P(D|H) = 1** — if the ball is red, the friend will certainly say "not blue."
- **P(¬H) = 7/10** — seven of ten balls are blue.
- **P(D|¬H) = 0** — if the ball is blue, the friend cannot say "not blue."

Applying Bayes' theorem:

$$P(H \mid D) = \frac{(3/10) \cdot 1}{(3/10) \cdot 1 + (7/10) \cdot 0} = \frac{3/10}{3/10} = 1$$

The answer is 1.0 — certainty that the ball is red.

This example is deliberately simple so the arithmetic is transparent. In Chapter 1, the probabilities will not be 0 and 1, and the answer will be less obvious. The same formula applies.

**Second worked calculation: a noisy scenario.** Now suppose the friend is not perfectly reliable — they sometimes say "not blue" even when the ball is blue (perhaps they are colorblind and guess). Specifically:

- P(says "not blue" | red) = 0.90 (usually correct when red)
- P(says "not blue" | blue) = 0.15 (sometimes wrong when blue)

With the same prior (3 red, 7 blue):

$$P(\text{red} \mid \text{"not blue"}) = \frac{(0.30)(0.90)}{(0.30)(0.90) + (0.70)(0.15)} = \frac{0.27}{0.27 + 0.105} = \frac{0.27}{0.375} = 0.72$$

Now the probability is 0.72, not 1.0. The friend's imperfect reliability weakened the update. Notice that without the friend's statement (prior alone), P(red) = 0.30. After hearing "not blue" from an imperfect friend, P(red) = 0.72. The data moved the probability in the right direction, just not to certainty.

This is Bayesian updating: you start with a prior, observe data, and end with a posterior. The posterior becomes the prior for the next update.

---

## Common Misconceptions

**Misconception 1: "P(A|B) and P(B|A) are close enough to use interchangeably."**

They are not, and the Sally Clark case shows why. In England in 1999, a mother was convicted of murdering her two infant sons after an expert witness testified the probability of two sudden infant death syndrome (SIDS) deaths in the same family was about 1 in 73 million. The Royal Statistical Society issued a formal public statement in 2001 criticizing the statistical reasoning; the conviction was quashed in 2003. One central error: the expert computed P(two SIDS deaths), but the court needed P(murder | two infant deaths). These are different quantities. The second requires the prior probability of murder in such cases — which was not supplied. [Sally Clark case documented by the Royal Statistical Society statement (2001) and reviewed in forensic statistics literature.]

**Misconception 2: "The formula only works when you know all the exact numbers."**

Bayes' theorem requires P(H), P(D|H), and P(D|¬H). In practice these are often estimated, not known. That is acceptable. An approximate prior produces an approximate posterior — but an approximate posterior is usually better than no posterior at all. The decision about how much to trust the prior is a judgment, not a formula. Chapters 7 and 8 examine this question in depth.

**Misconception 3: "Bayesian reasoning is a different kind of mathematics from regular probability."**

It is not. Bayes' theorem is a consequence of the conditional probability definition, which is itself a consequence of Kolmogorov's (1933) axioms of probability that all mathematicians and statisticians accept. There is no special mathematics required. The disputes about Bayesian statistics — and there are real ones — are about how to assign priors in practice, not about whether the theorem is valid. The theorem is valid. It is arithmetic.

---

## AI Wayback Machine: Hilda Geiringer

**Hilda Geiringer** (1893–1973) was an Austrian-American mathematician who worked on probability theory, statistics, and mechanics in the early twentieth century. Born in Vienna, she studied under Richard von Mises — one of the founders of the frequentist interpretation of probability — and made contributions to the study of frequency distributions and plastic deformation. When the Nazi regime came to power, she lost her university position in Berlin; she ultimately fled to Turkey, then immigrated to the United States, where she worked at Bryn Mawr College and later Wheaton College.

Geiringer's work sits at a foundational moment in probability theory — the early twentieth century when Kolmogorov's axiomatic framework was consolidating probability as a branch of measure theory, and when the frequentist versus subjectivist debate was live. She worked within the frequentist tradition, which treated probability as the long-run frequency of events rather than a degree of belief. Chapter 0's formal definition of conditional probability rests on Kolmogorov's (1933) axioms, the same foundation Geiringer's work assumed. Her career is a reminder that the mathematics Chapter 0 teaches was not always obvious or settled — and that establishing it required real work by people in difficult circumstances.

---

## Exercises

**Exercise 1.** A 2×2 table describes the joint distribution of "passed the driving test" and "took a preparation course." Of 200 students, 80 took the course and 120 did not. Of those who took the course, 70 passed. Of those who did not take the course, 60 passed.

(a) Build the joint frequency table.  
(b) Compute P(passed | took course).  
(c) Compute P(took course | passed).  
(d) Are these equal? Explain in one sentence why or why not.

**Exercise 2.** A factory produces widgets. Machine A produces 60% of widgets and has a 2% defect rate. Machine B produces 40% of widgets and has a 5% defect rate. A widget is selected at random and found defective.

(a) Write down P(defective | Machine A), P(defective | Machine B), P(Machine A), and P(Machine B).  
(b) Use Bayes' theorem to compute P(Machine A | defective).  
(c) Interpret the result in plain language: what does this number tell a quality control manager?

**Exercise 3.** The Sally Clark case (England, 1999–2003) involved an expert witness who testified that the probability of two SIDS deaths in a single family was approximately 1 in 73 million. The Royal Statistical Society stated that this reasoning was flawed.

(a) Identify the conditional probability the expert computed.  
(b) Identify the conditional probability the jury needed.  
(c) Explain in two sentences what additional information is required to compute the quantity the jury needed, and why the expert's figure cannot serve as a substitute.

---

## Still Puzzling

1. The urn problem in this chapter has a perfectly known prior (3 red, 7 blue). In real problems the prior is estimated. When the prior is uncertain, should you use Bayes' theorem on the point estimate, or is there a principled way to account for uncertainty in the prior itself? (Chapter 7 addresses this.)

2. Bayes' theorem in this chapter involves two hypotheses (H and ¬H). Real problems often involve many competing hypotheses — multiple diseases, multiple machines. How does the sum in the denominator extend, and what computational challenges arise? (Chapter 6 touches on this via model comparison.)

3. The worked example in this chapter uses exact numbers. In practice, the prior P(H) and the likelihoods P(D|H) and P(D|¬H) are measured with uncertainty. Does propagating that uncertainty require a different framework entirely?

---

## Bridge to Chapter 1

You can now compute a posterior probability from a prior and a likelihood. Chapter 1 will show you a problem where a 99%-accurate medical test produces a posterior of only 9% — and where the standard frequentist analysis cannot produce a posterior at all. The asymmetry P(A|B) ≠ P(B|A) that this chapter introduced is the key to understanding why.
