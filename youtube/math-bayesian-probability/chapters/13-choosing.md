# Chapter 13 — Choosing

---

## Learning Objectives

By the end of this chapter, you should be able to:

1. **(Analyze)** Identify the specific decision factors — sample size, prior availability, output type needed, audience, computational constraints — that favor frequentist methods for a given problem.
2. **(Analyze)** Identify the specific decision factors that favor Bayesian methods for a given problem, and explain why Bayesian methods are not always the principled choice.
3. **(Evaluate)** Apply a structured five-question decision framework to method selection for novel problems you have not seen before.
4. **(Create)** Write a methodological justification for your choice of approach — one that anticipates and responds to the strongest objection from a reviewer who would have chosen differently.

---

## Opening: You Have Both Toolkits

You now have both toolkits. Chapters 1–11 walked you through the same questions solved two ways, in escalating complexity. Chapter 12 asked you to apply both frameworks to a real dataset and write up the comparison. By now you can run a frequentist significance test and a Bayesian posterior analysis for proportions, regressions, model comparisons, sparse counts, grouped data, time series, and classifiers.

The question this chapter addresses is: when do you use which?

The answer is not always Bayesian. This needs saying directly because the structure of this book — frequentist first, then the Bayesian alternative that answers the question the frequentist method could not — naturally makes the Bayesian approach look like the upgrade. It sometimes is. It sometimes is not. The goal of this chapter is to give you a framework for making that judgment deliberately, rather than reflexively.

Bayarri and Berger (2004) concluded, after an extended technical analysis of the two frameworks, that neither approach is entirely self-sufficient — that "each is actually essential for full development of the other." Efron (2005), in his ASA Presidential Address, argued that 21st-century problems require both, and that the statistician's job is to know when to use which. Gelman and Shalizi (2013) went further: they argued that even rigorous Bayesian inference requires frequentist-style model checking to be intellectually honest, because a model that fits the data it was fit on should also be checked against what it predicts. The debate between the paradigms is, at the working methodological level, substantially resolved — not in favor of either side, but in favor of pragmatic competence.

What follows is a framework for exercising that competence.

---

## When Frequentist Methods Are the Right Choice

### Large samples where prior information is genuinely absent

The central limit theorem is one of the most useful results in statistics: for large enough samples, sample means are approximately normally distributed regardless of the underlying population distribution. This means that for large samples, the machinery of frequentist inference — standard errors, t-tests, confidence intervals — is well-grounded without requiring any assumptions about the population distribution.

More importantly: when a sample is large enough that the data dominate any reasonable prior, the Bayesian posterior will be nearly identical to the frequentist confidence interval. The extra work of specifying and defending a prior produces no benefit because the data wash it away. Bayarri and Berger (2004) document this convergence formally. For large samples with flat priors, the two approaches give numerically identical answers. Choosing the simpler approach — frequentist — is not a concession; it is the rational choice.

The key word is "genuinely." Claiming prior ignorance when domain knowledge exists is not intellectual humility; it is a missed opportunity to use real information. The test for genuine prior absence is: would any reasonable expert in this domain put substantial probability on a range of values? If yes, a prior exists. If no — if the problem is truly novel, or if experts genuinely disagree about the plausible range of values — then a frequentist analysis that remains agnostic about the prior is the honest choice.

### Regulated and preregistered environments

The Food and Drug Administration's guidance on adaptive clinical trial designs permits Bayesian methods for interim analyses but requires frequentist operating characteristics — Type I error control — for primary regulatory submissions (FDA 2019) [verify: confirm current FDA guidance document title and URL before publication, as FDA guidance documents are updated periodically]. The European Medicines Agency has similar requirements for most primary endpoints.

The reason is not that frequentist methods are statistically superior for drug trials. It is that frequentist methods provide a reproducibility guarantee that Bayesian analyses with analyst-chosen priors do not. A confidence interval procedure guarantees that, across all trials conducted this way, 95% will contain the true value. This guarantee is auditable, replicable, and adversarially robust — a regulator evaluating a drug company's submission cannot easily argue that the procedure was manipulated, because the procedure does not require any judgment about prior distributions.

In preregistered research — where the analysis plan is locked before data collection — frequentist methods provide the same reproducibility protection. A preregistered analysis is designed to be run mechanically; introducing analyst discretion over prior choice undermines the preregistration's purpose. The frequentist approach is the correct choice here not despite its rigidity but because of it.

### Exploratory research and hypothesis generation

The goal of exploratory research is to generate hypotheses, not confirm them. In genuinely exploratory settings — analyzing a new dataset for patterns, running a first descriptive study in a new domain — the investigator has no strong hypothesis to test and no strong prior to specify. Forcing a prior into this situation risks embedding the analyst's expectation about what the data should show. The frequentist approach, which treats all possible values as equally surprising before data is collected, is appropriate for describing what is actually in the data without prior commitment.

There is an important asymmetry here: the Bayesian approach is powerful when you have a specific hypothesis and relevant prior information. It is not well-suited to the situation where you are trying to find out what questions are worth asking. For exploratory work, frequentist description — means, variances, confidence intervals, correlation matrices — is the right starting point.

### Audiences that require p-values

This is an institutional reality, not a statistical recommendation. Many scientific journals, clinical trial reporting requirements, and professional audiences have been trained to expect p-values and would not know how to act on a posterior probability. In these contexts, choosing Bayesian methods means either translating your results into frequentist language (which loses most of what the Bayesian analysis provides) or educating your audience before presenting your findings (which costs time and risks resistance).

The ASA has moved toward discouraging the mechanical use of p < 0.05 as a decision rule (Wasserstein & Lazar 2016; Wasserstein, Schirm & Lazar 2019), but the adoption of this guidance in applied fields has been uneven. As of 2026, most applied research in psychology, education, medicine, and social science still uses p-values as the primary inferential tool. A student who produces Bayesian analyses in a context where the audience cannot interpret them has not served the decision-maker.

### Computational constraints

This criterion has narrowed substantially since 2015. Stan, PyMC, brms, and LLM-assisted implementation have made Bayesian inference accessible to non-specialists in ways that were not true a decade ago. For simple models — proportions, two-group comparisons, linear regressions — the computational difference is now small.

The criterion still applies in genuine real-time settings: systems that must make decisions in milliseconds, embedded systems without computational resources for MCMC, or analyses that must run as part of automated pipelines without human oversight. In these cases, closed-form frequentist methods remain the practical choice.

---

## When Bayesian Methods Earn Their Complexity Cost

### Decision problems requiring P(outcome > threshold)

Chapter 3 introduced this as the first crack in the frequentist approach: a quality control engineer who needs P(defect rate < 0.20) before accepting a batch cannot get this from a confidence interval. The confidence interval gives her a range and a procedure guarantee; it does not give her the probability that the true rate satisfies the acceptance criterion.

This gap recurs throughout applied decision-making. A pharmaceutical company deciding whether a drug meets efficacy criteria, a loan officer setting a rejection threshold, an inventory manager deciding whether to reorder — all of these decision-makers need probability statements about parameters or outcomes, not significance tests about whether an effect is surprising under the null. Bayesian inference produces these statements directly. Frequentist inference does not, and no amount of careful interpretation can close this gap.

If the decision-maker's actual question is of the form "what is the probability that [quantity] exceeds [threshold]?" — Bayesian methods are the right choice.

### Small samples and rare events

Chapter 8 showed the frequentist approach straining on sparse data: wide confidence intervals, questionable normal approximations, and the "winner's curse" — statistically significant results in underpowered studies that are systematically too large. In these settings, prior information is not just helpful; it is necessary to produce estimates precise enough to act on.

When a hospital sees three complications in 200 procedures, the frequentist confidence interval is [0.003, 0.043] — nearly four-fold range, not informative enough to compare against an accreditation threshold. A Bayesian analysis with a literature-derived prior (reflecting that complication rates for this procedure type are typically around 1.5%) produces a tighter posterior that incorporates the existing evidence base rather than pretending it does not exist. The prior is not a thumb on the scale; it is the accumulated clinical knowledge that every experienced surgeon brings to the question.

The principled use of informative priors in small-sample settings is one of the clearest cases where Bayesian methods provide something the frequentist approach cannot.

### Sequential updating

Sequential updating — using each day's (or week's, or patient's) data to revise your probability distribution and then using that revised distribution as the starting point for the next update — is Bayesian inference in its most natural form. Chapter 10 showed this in the context of inventory forecasting: the posterior from one week becomes the prior for the next, and the forecast narrows as data accumulates.

This structure is directly applicable to adaptive clinical trials, where stopping rules depend on accumulating evidence. Bayesian sequential designs have been shown to reach correct conclusions with substantially fewer patients than fixed-design frequentist trials, because they update enrollment and stopping criteria as data arrives (Berry 2006, *Statistical Science* [verify: full volume and page details]). The I-SPY 2 breast cancer trial used a Bayesian adaptive design with this structure and is now a standard reference for why Bayesian methods are preferred in this sub-domain (Barker et al. 2009, *Clinical Cancer Research*).

In any application where data arrives over time and decisions must be made before all data is collected — clinical trials, A/B testing, quality monitoring, sensor data fusion — the Bayesian sequential framework is the natural fit.

### Hierarchical data and partial pooling

Chapter 9 showed the problem directly: a school district with 30 schools, some with 200 students and some with 8, needs estimates for every school. Complete pooling (treat all students the same) ignores the school structure. No pooling (estimate each school separately) produces wildly unstable estimates for small schools. The mixed-effects model (frequentist) partially pools but does not give you full posterior distributions over the school-level estimates or fully propagate the uncertainty in the shrinkage itself.

The Bayesian hierarchical model does all of this: each school gets a full posterior distribution; small schools shrink more toward the district mean because their data is sparse; the uncertainty in the hyperparameter (the between-school variance) is propagated through all school-level estimates. This is the complexity that, in Chapter 9's language, "buys something real."

Whenever the data has genuine grouping structure — patients nested in hospitals, students nested in schools, users nested in cities — and the group sizes are unequal, the Bayesian hierarchical model provides estimates that are more stable and more honest about their uncertainty than any frequentist alternative.

### Parameter uncertainty affects the decision

In Chapter 11, the loan officer's classification problem showed that the threshold dividing "approve" from "reject" should depend on the asymmetric costs of the two error types. But it should also depend on the uncertainty in the model parameters: if the posterior on the slope coefficient is wide, the optimal threshold under uncertainty is different from the threshold implied by the point estimate alone. Bayesian logistic regression gives you a posterior distribution over the optimal threshold, not just a point estimate.

This generalizes: whenever the decision depends not just on the point estimate but on the uncertainty around it, the full posterior distribution is the right input. Frequentist methods report standard errors and confidence intervals, but propagating those through a decision function is non-standard and often approximate. The Bayesian framework makes this propagation exact.

### Communicating probability to a probability-ready audience

When the audience is comfortable with probability — actuaries, Bayesian economists, clinical pharmacologists, risk managers — a Bayesian posterior is often a more direct communication of what the data established than a p-value. "There is an 87% probability that this treatment reduces hospitalization rates by more than 15%" is a statement the decision-maker can act on directly. "The result is significant at p = 0.03" requires translation.

This criterion interacts with the audience criterion from the frequentist case. The same analysis might be reported as frequentist in a regulatory submission and Bayesian in an internal decision brief — not as inconsistency, but as appropriate communication for different audiences. The FDA is aware that this practice exists; the data is analyzed both ways for different purposes (FDA 2019 [verify]).

---

## The Decision Framework

When you face a new problem and need to choose a statistical approach, work through these five questions in order. The first question is the most important.

| Decision Criterion | Favors Frequentist | Favors Bayesian |
|---|---|---|
| **1. What quantity does the decision-maker actually need?** | A significance threshold; a ranking; a go/no-go decision against a pre-specified rule | A probability statement about a parameter or outcome: P(θ > threshold) |
| **2. Is prior information available and defensible?** | No prior information exists, or it would be contested by an adversarial reviewer | Prior information is documented (published studies, expert consensus, prior data) and appropriate to the question |
| **3. How large is the sample relative to the effect size?** | Large sample; moderate to large effect; central limit theorem applies | Small sample; rare event; sparse data; prior can stabilize the estimate |
| **4. Who will receive the results?** | A regulatory body requiring frequentist operating characteristics; an audience fluent in p-values; a court or audit process | An internal decision-maker; an audience comfortable with probability statements; a sequential decision requiring updating |
| **5. What are the computational and time constraints?** | Real-time decision; embedded system; automated pipeline; rapid turnaround required | Full posterior distribution needed; uncertainty in all parameters affects the decision |

**When the framework gives a split answer.** Many real problems are not cleanly resolved by this table. A problem might have a small sample (favors Bayesian) but an audience that expects p-values (favors frequentist) and a decision that requires P(θ > threshold) (favors Bayesian). In these cases, the right answer is often: run both, report both, and explain the translation. This is not a failure of the framework; it is the honest representation of a problem where the method choice involves real tradeoffs.

**When both approaches converge.** One key finding from the reconciliation literature (Bayarri & Berger 2004): for large samples with flat priors and well-specified models, frequentist and Bayesian results converge numerically. The confidence interval and the credible interval are nearly identical. The significance test and the posterior probability about the null value point in the same direction. In these cases, the choice of framework is largely a communication decision — which output will the audience understand and act on? The statistical question has effectively one answer; the remaining question is presentation.

---

## What This Book Has Not Covered

This section is an honest accounting. Every textbook makes scope choices, and the scope choices here were deliberate. These topics are not here because they were judged too advanced for an on-ramp, not because they are unimportant.

**Full MCMC implementation and probabilistic programming.** This book has used MCMC results and shown how to prompt for them, but it has not taught you to write a Stan or PyMC model from scratch, diagnose convergence, or understand the detailed mechanics of Hamiltonian Monte Carlo. For that, the standard reference is McElreath's *Statistical Rethinking* (2020, 2nd edition, CRC Press) — a graduate-level text that teaches Bayesian inference entirely through model-building and rethinking. If you want to go deeper into the Bayesian side, that is the next book.

**Non-parametric Bayesian methods.** Dirichlet processes, Gaussian process priors on functions, Bayesian nonparametric density estimation — these methods let you learn the structure of a model from the data rather than pre-specifying a parametric form. They are substantially more complex and are not covered in any undergraduate-level textbook accessible to this audience. They are not covered here.

**Frequentist corrections for multiple comparisons.** When you run many hypothesis tests simultaneously — testing 200 gene expressions for associations with disease, comparing 30 schools against each other pairwise — the false positive rate inflates unless you correct for the number of tests. The Bonferroni correction, Benjamini-Hochberg false discovery rate control, and related methods are the frequentist response to this problem. The Bayesian response is hierarchical modeling (Chapter 9), which shrinks estimates toward a common prior and automatically reduces the multiple comparison problem. This book covers the Bayesian solution but not the frequentist correction procedures in detail.

**Robust statistics for non-normal data.** Chapter 12's Dataset C has 8 points where normal approximations are questionable. Many real datasets have heavy tails, outliers, or fundamentally non-normal distributions. Robust regression, M-estimators, and rank-based methods are frequentist tools for these situations; heavy-tailed likelihood models (Student-t likelihoods) are the Bayesian analog. Neither is covered systematically here.

**Causal inference.** Every analysis in this book has been about statistical association — whether one quantity is related to another, how strongly, with what uncertainty. Causal inference asks a different question: does one quantity cause another, and what would happen if you intervened to change it? Answering causal questions requires assumptions — about confounders, about the data-generating mechanism — that go beyond statistical modeling. This is the subject of the companion volume in this series, *Causal Inference with Case Studies*. The methods you have learned here are necessary but not sufficient for causal claims.

**Empirical Bayes as a bridge.** Efron's empirical Bayes framework estimates the prior from the data itself, using the marginal distribution of observations to learn the prior distribution — a procedure that is philosophically frequentist in one reading (it treats the prior as a parameter to be estimated from data) and Bayesian in another (it uses the estimated prior to compute posteriors). In practice it is one of the most widely used "Bayesian" methods in statistics, underlying shrinkage estimators and modern machine learning regularization. It blurs the frequentist/Bayesian boundary in useful ways. A note: the framework this book has used — "choose a prior and defend it" — is not empirical Bayes. Empirical Bayes is a different and powerful approach worth knowing about, even if its epistemological status is contested.

---

## The Decision Table as a Flowchart

For quick reference, the five-question framework can be read as a decision path:

```
Start: What does the decision-maker need?
│
├─ A significance threshold / go-no-go / ranking
│   └─ FREQUENTIST (unless other criteria override)
│
└─ A probability statement: P(θ > threshold)
    └─ BAYESIAN (unless other criteria override)

Then ask:
│
├─ Is defensible prior information available?
│   ├─ No → FREQUENTIST has an advantage (no prior to specify)
│   └─ Yes → BAYESIAN can use it productively
│
├─ Sample size relative to effect?
│   ├─ Large, well-powered → FREQUENTIST works well; both converge
│   └─ Small, sparse, rare → BAYESIAN shrinkage helps
│
├─ Audience?
│   ├─ Regulatory / p-value-fluent → FREQUENTIST output required
│   └─ Decision-maker who can use probabilities → BAYESIAN preferred
│
└─ Computational constraints?
    ├─ Real-time / automated → FREQUENTIST closed-form
    └─ Full uncertainty propagation needed → BAYESIAN
```

**When the arrows point in different directions:** run both. Explain the translation. Deliver the output each audience needs from the same underlying analysis.

---

## The Metacognitive Close

You have built both toolkits. The question is no longer which approach is correct in the abstract — it is which approach is correct for this problem, this data, this decision, and this audience.

That is a judgment, not a formula. The five questions above are a scaffold for making the judgment systematically, but they are not a replacement for it. Two analysts with the same training, the same data, and the same framework can still reach different conclusions about the right approach — because they disagree about whether the prior is defensible, because they assess the audience differently, because they weight the decision-maker's needs differently. These are legitimate differences that no algorithm resolves.

What the framework gives you is the ability to articulate your reasoning. A colleague who disagrees with your method choice should be able to point to a specific criterion — "I think your sample is large enough that the prior doesn't matter" or "I think the audience requires a p-value" — rather than registering a vague preference. And you should be able to respond specifically, not just restating your choice.

Statistics can inform judgments. It cannot replace them.

The "irreducibly human" framing in the title of this series is not a slogan. It is a specific claim: the judgment about which method to use, and why, given this problem and this audience and these constraints, is not automatable. An LLM will implement either framework you specify, and implement it correctly if you prompt carefully (Chapter 2's skill). Only the analyst — you — can identify the decision-maker's actual need, assess whether the prior is defensible, and take responsibility for the choice.

---

## Common Misconceptions

**"I always use Bayesian methods because they're more principled."**

This is the misconception Chapter 13 is designed to correct. The Bayesian approach is not more principled in the abstract; it is more appropriate for specific problems where prior information is available and defensible, where the decision requires a probability statement, or where the data is sparse enough that the prior stabilizes the estimate. For large samples where the prior is uninformative, the two approaches produce numerically identical results. For regulatory submissions where prior-free reproducibility is required, the frequentist approach is the principled choice. "More principled" depends on what the principle is and what problem you are solving.

Gelman and Shalizi (2013) add a deeper point: Bayesian inference is philosophically well-founded only when combined with model checking, which is fundamentally frequentist in character — you check whether the model could have produced data like what you observed. A purely Bayesian practice that updates the posterior without ever checking whether the model fits is not more principled; it is more blind.

**"Frequentist methods are objective because they don't require priors."**

Chapter 7 answered this directly: every frequentist analysis has implicit prior assumptions. The standard t-test treats all possible values of the true mean as equally likely before seeing the data — a flat prior over the real line. In a drug trial where the compound has failed three prior Phase II studies, treating all effect sizes as equally likely is itself a strong and probably wrong assumption. The question is not whether to have prior assumptions; it is whether to name them.

The frequentist approach's objectivity guarantee is a guarantee about the procedure — about repeated behavior across many applications — not about any individual analysis. A 95% confidence interval procedure is "objective" in the sense that, applied across many problems, 95% of the intervals will contain the true value. It is not "objective" in the sense that this particular interval contains the true value with probability 0.95.

**"Bayesian methods are subjective because analysts choose the prior."**

The subjectivity concern is legitimate and should not be dismissed. When analysts choose priors that favor their preferred conclusions, Bayesian analyses can be gamed in ways that frequentist preregistered analyses cannot. This is a real risk, and the requirement that priors be documented and defended is not sufficient to eliminate it.

The honest response is not that Bayesian methods are objective — they are not. It is that the same subjectivity exists in frequentist analyses, but is hidden: in the choice of what test to run, what covariates to include, when to stop data collection, and what significance threshold to apply. The Bayesian approach at least makes the subjective elements explicit, where they can be examined, criticized, and changed. Whether that transparency is a net advantage depends on whether the analyst is honest about their choices.

**"We should always use both methods and report both."**

Appealing, but not always practical. Running two complete analyses doubles the work, and in many applied settings the primary result needs to be one number, not a pair of intervals with different interpretations. The framework this chapter provides is for choosing a primary approach — the one best suited to the decision, sample, audience, and prior information — while acknowledging the alternative. You should understand what the other approach would have found and be able to describe it; you do not always need to run it fully.

---

## Exercises

**Exercise 13.1 — Method Classification**

For each of the five problem descriptions below, recommend a statistical approach (frequentist, Bayesian, or both) and justify your recommendation using the five-question framework. For each recommendation, name the single most important criterion and explain why it dominates the others.

1. A public health department is screening a city population for a rare infectious disease with 0.2% prevalence. The test has 95% sensitivity and 90% specificity. Officials need to decide whether a positive test result is sufficient grounds for mandatory quarantine.

2. A pharmaceutical company is preparing a Phase III trial submission to the FDA for a new cholesterol-lowering drug. The primary endpoint is LDL reduction at 12 weeks. The trial will have 500 patients per arm.

3. A startup is running an A/B test on two versions of their signup page. They have 200 visitors so far and need to decide whether to roll out Version B before the weekend. They have run similar A/B tests on related pages and have prior estimates of typical conversion improvements.

4. An educational researcher wants to explore whether attendance patterns in a dataset of 5,000 students predict graduation outcomes. This is the first analysis of this particular dataset; she has no specific hypothesis going in.

5. A credit union with 800 loan files from the past two years wants to build a model predicting default probability. The base rate of default is 4%. They need to set an approval threshold that minimizes expected losses, where an approved default costs 8 times as much as a declined non-default.

---

**Exercise 13.2 — Methodological Justification**

Take the analysis you completed in Chapter 12. Write a methodological justification (one to two paragraphs) for your choice of primary approach that directly addresses the strongest objection from a reviewer who would have preferred the other approach.

Your justification must:
- State which approach you chose as primary and why (using at least two criteria from the decision framework)
- Name the reviewer's strongest specific objection (not a generic one — what specific criterion would lead a thoughtful reviewer to the other approach?)
- Respond to that objection substantively — not by dismissing it, but by explaining why the criterion it invokes is less important than the criteria you cited, for this specific problem

---

**Exercise 13.3 — Rebuttal**

A colleague says: "I always use Bayesian methods because they're more principled — you have to commit to a prior, which forces you to think carefully about what you know before seeing the data. Frequentist methods let you pretend you don't have assumptions, but you always do."

Write a response that:
- Acknowledges what is correct in this claim
- Names the specific conditions under which the frequentist approach is the right choice, not just a legacy concession
- Cites the reconciliation literature that supports your response (Bayarri & Berger 2004; Efron 2005; Gelman & Shalizi 2013)
- Ends with a statement of where you agree with your colleague and where you do not

Your response should read as a collegial exchange, not a refutation. The goal is calibration — helping a Bayesian enthusiast understand what the other framework legitimately provides — not winning an argument.

---

## What Would Change My Mind

This chapter argues that the decision between statistical approaches is pragmatic — problem-driven, audience-driven, data-driven — rather than philosophical. I am committed to that position, but I should be explicit about what would move it.

**If it turned out that Bayesian methods with well-calibrated priors systematically outperform frequentist methods on prediction accuracy across a wide range of real applied problems**, the case for always preferring Bayesian methods would be stronger. The current evidence is mixed: in some domains (small samples, sequential data, hierarchical structures) Bayesian methods clearly win; in others (large samples, exploratory settings) they are equivalent to or not clearly better than frequentist approaches. A meta-analysis of carefully controlled comparison studies across diverse domains could change this.

**If regulatory agencies substantially expanded their acceptance of Bayesian primary endpoints**, the audience criterion in the decision framework would tilt further toward Bayesian methods. The FDA has been moving in this direction incrementally, but the primary endpoint requirement for frequentist operating characteristics is still the rule for most submissions. If this changed — and the history of the FDA's engagement with adaptive designs suggests it can change — the "audience requires frequentist output" criterion would narrow substantially.

**If the computational cost of MCMC genuinely approached zero** — if LLM-assisted Bayesian inference became as fast and reliable as running a t-test — the computational criterion would effectively disappear from the framework. We are not there yet in 2026, but the trend is in that direction. The framework should be revisited as the tooling continues to evolve.

---

## Still Puzzling

The question this chapter cannot fully resolve is the prior defensibility assessment. The framework asks: "Is prior information available and defensible?" But "defensible" is a judgment about an adversarial process — what a skeptical reviewer or regulator would accept. In practice, the same prior might be defensible to one reviewer and not to another: an informative prior derived from a company's internal historical data might be acceptable to an internal decision committee and entirely unacceptable to an external regulator. The framework gives you the right question; it cannot give you the answer for any specific context.

The deeper puzzle is whether Bayesian and frequentist methods are really two different approaches to the same problem, or two different problems. When Efron (2005) describes 21st-century statistics as needing both, he is describing a world where the two frameworks are genuinely complementary — where Bayesian posterior probabilities and frequentist calibration guarantees are both real things that matter for different purposes, and where a statistician who masters only one has an incomplete toolkit. That is the position this book takes. But the philosophical debate — whether probabilities are properties of procedures or of beliefs about states of the world — has not been settled (Jaynes 2003; Shalizi; Gelman & Shalizi 2013). The pragmatic position that they are both useful is well-established; the deeper question of which is right about the nature of probability remains open.

---

## AI Wayback Machine

**Grace Wahba (born 1934)**

Grace Wahba spent most of her career at the University of Wisconsin–Madison, where she was the I.J. Schoenberg-Hilldale Professor of Statistics. Her most influential contribution is a formal mathematical result that most statistics students never encounter but that underlies an enormous amount of modern applied statistics: she showed that the frequentist solution to a smoothing problem — finding the spline that fits the data subject to a roughness penalty — is identical to the mean of the Bayesian posterior under a specific Gaussian process prior.

The practical implication is significant. Many regularization methods that are described as frequentist — ridge regression, LASSO, spline smoothing, kernel methods — have exact Bayesian interpretations, with the regularization parameter corresponding to a prior on the complexity of the model. Conversely, many Bayesian methods can be computed using fast frequentist numerical techniques once you recognize the equivalence. The divide between the paradigms, at the computational level, is blurrier than the philosophical debate suggests.

Wahba was elected to the National Academy of Sciences in 2000. Her work is a technical embodiment of the thesis this chapter argues for: not that one approach is right and the other wrong, but that the methods developed under each paradigm often turn out to be implementing the same underlying idea — and that understanding both gives you tools to move between them when the problem requires it.

Her 1990 book *Spline Models for Observational Data* (SIAM) remains a standard reference, though its technical level is well above this textbook. For an accessible entry point to the connection she established, search for "Gaussian process regression Bayesian spline smoothing equivalence" — the connection is described in many modern machine learning texts and is accessible to a reader who has completed this book.

---

*This is where the book ends. You began with a patient and a 99%-accurate test result, and the counterintuitive answer that most people give wrong. You are leaving with both toolkits, a framework for choosing between them, and an honest account of what the choice requires. The judgment about which method serves this problem, this audience, and this decision is yours. That was always the point.*
