# Chapter 12 — A Real Problem, Both Ways

---

## Learning Objectives

By the end of this chapter, you should be able to:

1. **(Apply)** Conduct a complete frequentist analysis — selecting the appropriate test, interpreting the output, and stating what the method cannot tell you — for a self-selected real dataset.
2. **(Apply)** Conduct a complete Bayesian analysis of the same dataset, specifying and defending a prior, computing and interpreting the posterior, and reporting a credible interval.
3. **(Evaluate)** Compare the outputs of both analyses: where they agree numerically, where they diverge in the quantities they return, and why those divergences matter for the specific analysis goal.
4. **(Create)** Produce a written methodological justification — not a lab report, an argument — for a preferred approach given the analysis goals.

---

## What This Chapter Asks of You

The previous eleven chapters gave you tools. Each tool was demonstrated on a constructed problem designed to isolate one concept at a time. The data was tidy, the sample sizes were cooperative, and the analysis goal was pre-specified. Real analysis does not work that way.

This chapter is different. There is no standard lecture anatomy here. You choose a dataset from the vetted library below. You apply both frameworks — completely, not partially. And you write a comparative analysis that answers six specific questions. The deliverable is a 4–6 page written comparison that demonstrates statistical judgment: not just which numbers came out, but what those numbers mean, where each framework reached its limit, and which approach better served the analysis goal and why.

The chapter IS the exercise. There are no additional problems at the end.

What makes this hard is not the computation. An LLM can implement both frameworks for any of these datasets in under an hour. What makes it hard is questions 5 and 6 of the analysis scaffold: *which approach better serves the goal, and why?* and *what would change your conclusion?* These require you to know what the decision-maker actually needs, whether a probability statement or a significance threshold or a point estimate, and to be honest about the assumptions you made and what happens if they are wrong. That judgment is not in the output. It comes from working through Chapters 1–11 and knowing what the machinery is actually doing.

---

## Dataset Selection Guide

All five datasets are verified as publicly accessible. Each comes with 2–3 pre-specified analysis questions. You choose the dataset; the questions are provided. Choose based on the domain that interests you, not on which you think is easiest — the difficulty is roughly equal across A through D.

---

**Dataset A: OEWS May 2024 National Occupational Employment and Wage Estimates**

- **Source:** U.S. Bureau of Labor Statistics, Occupational Employment and Wage Statistics program
- **URL:** Overview at https://www.bls.gov/oes/2024/may/featured_data.htm; flat file downloads at https://www.bls.gov/oes/tables.htm
- **Format:** Excel or CSV, approximately 830 occupational rows; columns include employment estimates, mean wage, median wage, percentile wages (10th, 25th, 75th, 90th), SOC code, and occupation title
- **Access:** Freely public; no registration required

**Pre-specified questions:**

1. *Distribution question.* Within Healthcare Support occupations (SOC major group 31-0000), is the median hourly wage distribution consistent with a log-normal model? **Frequentist approach:** Kolmogorov-Smirnov or Shapiro-Wilk test on log(wages). **Bayesian approach:** Posterior on log-normal parameters (μ, σ); posterior predictive check against the observed distribution.

2. *Comparison question.* Is the mean wage for Computer and Mathematical occupations (SOC 15-0000) different from the national cross-occupation median? **Frequentist:** One-sample t-test on the difference. **Bayesian:** Posterior on the difference between the group mean and the population median, with a weakly informative normal prior on the mean.

**Why it works both ways:** The frequentist test answers "is this result surprising if the null is true?" The Bayesian approach answers "what is the probability the true mean is above or below a threshold?" — exactly the contrast the book has built toward. Data is pre-aggregated, clean, and domain-agnostic. One work session handles both questions.

---

**Dataset B: O*NET 30.3 Work Context — Degree of Automation**

- **Source:** O*NET Resource Center, U.S. Department of Labor
- **URL:** Database download at https://www.onetcenter.org/database.html; individual descriptor at https://www.onetonline.org/find/descriptor/result/4.C.3.b.2
- **Format:** CSV flat file; columns include O*NET-SOC code, occupation title, element ID (4.C.3.b.2 for "Degree of Automation"), scale ID, data value (1–5 scale), standard error, sample size
- **Access:** Freely public; database ZIP download; no registration required

This dataset is used in combination with the Frey-Osborne automation probability scores (Frey & Osborne 2017), which are reported for 702 occupations in the appendix of their paper, available at https://oxfordmartin.ox.ac.uk/downloads/academic/The_Future_of_Employment.pdf. A crosswalk between O*NET-SOC codes (8-digit) and 2010 SOC codes (6-digit) is available at https://www.onetcenter.org/crosswalks.html. [verify: the exact CSV hosting of the Frey-Osborne appendix table; several GitHub repositories have reformatted it but none has been confirmed as the authoritative release — check the companion website for the pinned version before downloading from a third-party source.]

**Pre-specified questions:**

1. *Correlation question.* Does the O*NET "Degree of Automation" score correlate with the Frey-Osborne automation probability score across matched occupations? **Frequentist:** Pearson *r* or Spearman rank correlation with significance test. **Bayesian:** Posterior on the correlation coefficient ρ using a weakly informative prior.

2. *Classification question.* Does a high "Degree of Automation" score (above the scale midpoint of 3) predict high Frey-Osborne risk (probability > 0.5)? **Frequentist:** Logistic regression, coefficient significance test, ROC/AUC. **Bayesian:** Logistic regression with a weakly informative normal prior on the slope; posterior on P(high-risk | automation score).

**Why it works both ways:** The logistic regression comparison is the cleanest application of the Chapter 11 machinery to real data. The frequentist model gives significance and odds ratios; the Bayesian model gives the posterior probability that automation score is a meaningful predictor. Two different questions, same data.

**Aging caveat:** The Frey-Osborne automation probability scores are widely disputed. Arntz, Gregory, and Zierahn (2016, OECD) found substantially lower automation risk when analyzing task heterogeneity *within* occupations rather than treating occupations as homogeneous. Use this dataset as a methodological exercise, not as a claim about actual automation risk. The statistical structure is what matters here.

---

**Dataset C: BLS Education Pays 2024 — Earnings and Unemployment by Educational Attainment**

- **Source:** U.S. Bureau of Labor Statistics, derived from the Current Population Survey
- **URL:** https://www.bls.gov/careeroutlook/2025/data-on-display/education-pays.htm (2024 data); underlying CPS table at https://www.bls.gov/emp/chart-unemployment-earnings-education.htm
- **Format:** Small table — 8 rows by education level; columns include median weekly earnings and unemployment rate. Directly readable from the BLS site.
- **Access:** Freely public

**Pre-specified questions:**

1. *Regression question.* Is there a linear relationship between education level (mapped to approximate years: less than high school ≈ 10, high school diploma ≈ 12, associate's ≈ 14, bachelor's ≈ 16, master's ≈ 18, professional degree ≈ 20, doctoral ≈ 22) and median weekly earnings? **Frequentist:** OLS regression with significance test on the slope; R². **Bayesian:** Bayesian linear regression with a weakly informative prior on the slope and intercept; posterior predictive interval for a given education level.

2. *Threshold question.* What is the probability that a worker with a bachelor's degree earns more than $1,500/week? **Frequentist:** Cannot directly compute this probability; can construct a prediction interval and note the limitation explicitly. **Bayesian:** Compute P(earnings > $1,500 | bachelor's degree) directly from the posterior predictive distribution.

**Why it works both ways:** The threshold question is the sharpest single demonstration of the frequentist/Bayesian contrast in the dataset library. The frequentist approach structurally cannot answer the question the student wants answered — not because of a limitation in this particular test, but because significance tests and confidence intervals are not designed to return posterior probabilities about parameter values. The student must name this gap explicitly.

**Small-N note:** This dataset has only 8 data points. That is not a limitation to work around; it is the pedagogical point. With 8 observations, confidence intervals are wide, the normal approximation is questionable, and the prior matters. A student who uses a weakly informative prior derived from previous years' BLS data (also on the BLS site) will see Bayesian shrinkage in action. A student who uses a flat prior will see why small-sample frequentist intervals are honest about their uncertainty.

---

**Dataset D: BLS Employment Projections 2024–2034 — Occupational Growth Rates**

- **Source:** U.S. Bureau of Labor Statistics, Employment Projections program
- **URL:** https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm; interactive at https://data.bls.gov/projections/occupationProj; CSV downloads at https://www.bls.gov/emp/data/occupational-data.htm
- **Format:** CSV or Excel, approximately 830 occupations; columns include base employment (2024), projected employment (2034), change in employment (thousands and percent), median annual wage, typical entry-level education requirement
- **Access:** Freely public; released August 2024; no registration required

**Pre-specified questions:**

1. *Comparison question.* Do occupations requiring a bachelor's degree or higher show significantly different projected growth rates than those requiring less than a bachelor's? **Frequentist:** Two-sample t-test on percent change. **Bayesian:** Bayesian two-group comparison; posterior on the difference in mean growth rates; posterior P(bachelor's-required group grows faster).

2. *Regression question.* Does current median wage predict projected growth rate? **Frequentist:** OLS regression with significance test on slope. **Bayesian:** Bayesian linear regression with a weakly informative prior; posterior predictive interval for a high-wage occupation.

**Why it works both ways:** The two-group comparison is the direct Chapter 4 structure applied to real data. Students who have seen the tutorial score example before can now work through the same machinery with actual BLS projections — and the prior-choice discussion becomes concrete: if you believe healthcare occupations will grow because of demographic trends, what prior does that imply on growth rates for that group?

---

**Dataset E (Advanced Option): BLS OEWS Metropolitan Area Wage Estimates**

- **Source:** U.S. Bureau of Labor Statistics, OEWS program
- **URL:** https://www.bls.gov/oes/current/oessrcma.htm
- **Format:** One file per metropolitan statistical area, or a combined cross-MSA file; columns as in Dataset A
- **Access:** Freely public

**Pre-specified questions:** Do software developer wages vary significantly across metropolitan areas? Does the Chapter 9 partial-pooling framework change what you conclude about any individual metro area?

**Recommended for:** Students who engaged strongly with Chapter 9 and want to revisit the hierarchical thread in capstone form. Not recommended as a first choice. The data wrangling is non-trivial and may consume more time than the analysis itself.

---

### Quick Selection Table

| Dataset | Domain | Analysis Type | Recommended If You... |
|---|---|---|---|
| A — OEWS Wages | Labor economics | Distribution check + group comparison | Want clean data; no merge required |
| B — O*NET + Frey-Osborne | Automation & labor | Correlation + logistic regression | Engaged with Ch 11; comfortable with a data merge |
| C — Education Pays | Education & earnings | Regression + threshold probability | Want the sharpest frequentist/Bayesian contrast; 8-row dataset |
| D — Employment Projections | Labor economics | Two-group comparison + regression | Used Ch 4 machinery; want to revisit it with real data |
| E — Metro Wages (advanced) | Regional labor markets | Hierarchical structure | Completed Ch 9 and want the full partial-pooling challenge |

---

## The Analysis Scaffold: Six Questions Every Comparative Analysis Must Answer

A comparative statistical analysis is not a list of outputs. It is an argument about method grounded in results. The six questions below are the minimum structure that argument requires. Questions 1–4 can be answered by examining your outputs carefully. Questions 5 and 6 require judgment — they cannot be read off any model output.

Every question has a "what your answer must include" specification. Answers that address the question generically without applying it to your specific dataset will not satisfy the deliverable.

| # | Question | What Your Answer Must Include |
|---|---|---|
| 1 | What is the data generating process? What does each framework assume about it? | Name the assumed distribution (e.g., normal, log-normal, binomial); name the assumed sampling procedure; say explicitly whether those assumptions are met for your dataset |
| 2 | What did the frequentist analysis find? What can it not tell you? | State the test statistic, p-value or CI, and — critically — the specific question the frequentist method cannot answer for this analysis goal |
| 3 | What did the Bayesian analysis find? What prior did you use and why? | State the posterior mean or median and the 95% credible interval; name the prior distribution and defend its parameters with at least one sentence of justification |
| 4 | Where do the analyses agree? Where do they diverge? | Compare point estimates and intervals numerically; identify at least one case, if one exists, where the two approaches would recommend different actions |
| 5 | Which approach better serves the analysis goal, and why? | State what the decision-maker in your framing actually needs — a probability statement, a significance threshold, a point estimate, a ranking — and map that need to a framework; acknowledge what the other framework adds |
| 6 | What would change your conclusion? | Name at least one: more data, a different prior, a different model specification, a different analysis goal |

Questions 5 and 6 are the ones that differentiate a strong analysis from a narration of outputs. An LLM given your dataset and outputs will produce a generic answer to both. The student who has worked through Chapters 1–11 can produce a specific one.

---

## Worked Partial Example: Dataset C (Education Pays 2024)

The following example takes Dataset C through the analysis about halfway — far enough to show what the scaffold produces when applied seriously, not far enough to do the work for you.

**The dataset.** Eight rows: less than high school diploma through doctoral degree. Median weekly earnings (2024 USD): approximately $682, $900, $1,054, $1,165, $1,603, $2,031, $2,109 (in ascending order of education level, mapped to approximate years 10, 12, 13, 14, 16, 18, 20, 22). Source: BLS Current Population Survey, reported at bls.gov/careeroutlook/2025/data-on-display/education-pays.htm.

Note: these values are illustrative of the structure; confirm against the actual BLS table before analysis, as values are updated annually. The data is real; the specific figures are presented here as a worked scaffold, not a definitive citation.

**Question 1: Data generating process and framework assumptions.**

The data is derived from the Current Population Survey (CPS), a monthly household survey. The observations are *aggregated medians across educational attainment groups*, not individual observations. This matters: we do not have 8 independent draws from an underlying distribution; we have 8 summary statistics. The assumed relationship is linear — more education produces higher earnings at a roughly constant marginal rate — which is a simplification. Log-linear would be more defensible on economic grounds (returns to education are often modeled multiplicatively), but linear is adequate for a pedagogical exercise with 8 points.

Frequentist assumption: the OLS estimator assumes the residuals are approximately normal, which is nearly untestable with 8 points. The t-test on the slope coefficient assumes normal error distribution.

Bayesian assumption: we will use a weakly informative normal prior on the slope — say, Normal(0, 500), meaning we expect the slope to be near zero but allow large values. On the intercept, Normal(1000, 500) — reflecting that someone with minimal education still earns something.

**Question 2: Frequentist analysis.**

OLS regression with earnings as the outcome and education years as the predictor. On a dataset this small, the output will show a positive, statistically significant slope coefficient (expected around $80–100 per additional year of education), with an R² likely above 0.95. The 95% confidence interval on the slope reflects substantial uncertainty — with 8 points, the standard error is large.

What the frequentist model cannot tell you: it cannot directly compute P(earnings > $1,500 | bachelor's degree) — the question of whether a specific educational credential is likely to produce an earnings level above a threshold. The prediction interval will tell you where a new observation might fall, but not the probability that the true mean earnings for bachelor's degree holders exceeds $1,500/week. This is the wall from Chapter 3 in regression form.

**Question 3: Bayesian analysis.**

Bayesian linear regression with the priors described above. The posterior on the slope will be similar to the OLS estimate if the prior is sufficiently flat relative to the likelihood — with 8 data points and a strong linear pattern, the data dominate even a moderately informative prior. The posterior predictive distribution for "bachelor's degree" (16 years) gives a full distribution over predicted earnings, not just a point and interval.

From the posterior predictive distribution, computing P(earnings > $1,500 | 16 years) is direct: it is the proportion of posterior predictive draws that exceed $1,500. This is the quantity the frequentist analysis could not produce.

**Prior defense:** The slope prior Normal(0, 500) is weakly informative in the sense that it places very little probability on implausible slopes (negative returns to education, or implausibly large returns like $1,000 per year), while remaining wide enough not to substantially constrain the posterior with only 8 data points. A student with stronger domain knowledge could tighten this prior using estimates from published labor economics literature (Card 1999, in *Handbook of Labor Economics*, reports returns to education of roughly 8–13% per year of schooling) — using that as prior information is exactly what Chapter 7 described.

**Questions 4–6: Left for the student.**

The remaining three questions — where the analyses agree and diverge, which better serves the goal, and what would change the conclusion — are your work. The answer to question 5 depends on what you decide the analysis goal actually is: description (the frequentist OLS table is excellent for this), or decision under uncertainty about a specific threshold (the Bayesian posterior predictive does this work, the frequentist approach cannot).

---

## Prompting Section

### Dataset Selection Prompt Template

Use this prompt to get help choosing a dataset and confirming that the analysis questions suit your background:

```
I am selecting a dataset for a comparative frequentist and Bayesian analysis.
My background: [describe relevant coursework or domain knowledge].
My interest area: [labor economics / education / automation / regional variation — or other].

From the following options, which dataset would best support a complete
frequentist AND Bayesian analysis in a single work session, given my background?
Please describe the specific frequentist test and Bayesian model I would use for
each pre-specified question, and flag any data preparation steps I should expect.

Datasets:
[Paste the Dataset A–E descriptions from the chapter.]
```

### Analysis Scaffold Prompts

**For the frequentist half:**

```
I am analyzing [DATASET NAME] to answer the following question: [QUESTION].
The dataset has [N rows / columns / key variables].

Please implement a complete frequentist analysis using [t-test / OLS regression /
logistic regression / other]. Show:
1. The mathematical form of the test statistic
2. The code to compute it in Python or R
3. The numeric output (test statistic, p-value, confidence interval)
4. A plain-language interpretation of what the result means
5. The specific question this method CANNOT answer for this analysis goal
```

**For the Bayesian half:**

```
I am running a Bayesian analysis of the same question using this prior:
[PRIOR DISTRIBUTION AND PARAMETERS — be specific].

My prior justification: [one or two sentences explaining why these parameters
are appropriate for this domain and dataset].

Please implement the Bayesian model in Python (PyMC or similar) or R (brms or similar).
Show:
1. The model specification, including the full prior and likelihood
2. The posterior mean/median and 95% credible interval
3. How to compute P([quantity] > [threshold]) directly from the posterior
4. A verification check: does the posterior mean agree approximately with the
   frequentist point estimate? If not, why not?
```

**For the comparative summary:**

```
I have completed both analyses. Here are the results:
[Paste frequentist output]
[Paste Bayesian output]

Please help me write a comparative summary that answers the following six questions:
[Paste the six-question scaffold]

Important: for question 5 (which approach better serves the analysis goal),
do NOT give a generic answer. The decision-maker in this analysis needs
[specify what the decision-maker needs]. Map that specific need to a framework.
```

**Verification note:** Any LLM output from the analysis prompts should be checked against the structure of the analysis before you accept it. The most common errors are: (1) a Bayesian model that silently uses a flat prior without telling you; (2) a posterior interpreted as if it were a p-value; (3) a credible interval stated as if it were a confidence interval. Chapter 2 gave you the diagnostics for each of these. Use them.

---

## The Writing Guide

### What the 4–6 Page Deliverable Is

A written comparative statistical analysis is an argument about method. It is not a lab report listing outputs, and it is not a journal article. The audience is a reader who has completed the same course — someone who can follow the statistical reasoning and will push back if the argument is unclear.

The deliverable answers all six scaffold questions, in order, with the following structure:

**Section 1: Setup (approximately 0.5 pages)**
Dataset description (name, source, URL, variables used). Analysis goal (what question are you answering, and for what implicit decision-maker?). Why the dataset supports both approaches.

**Section 2: Frequentist Analysis (approximately 1 page)**
What you ran, what it returned, and — explicitly — what it cannot tell you. Include the test statistic, p-value or confidence interval, and a plain-language interpretation. The statement of what the method cannot tell you is the most important sentence in this section.

**Section 3: Bayesian Analysis (approximately 1 page)**
Model specification: likelihood, prior (named, with parameters), posterior. Prior justification: why these parameters and not others. Results: posterior mean/median, 95% credible interval, and any posterior probability computations that answered questions the frequentist analysis could not. The prior justification paragraph is what separates a Bayesian analysis from a frequentist analysis with different output labels.

**Section 4: Comparison (approximately 1 page)**
Where do the analyses agree numerically? Where do they diverge? Be specific — compare point estimates, interval widths, and (if applicable) the existence of a probability statement only one framework could produce. If the two approaches would lead to the same action, say so. If they would lead to different actions, say that too.

**Section 5: Methodological Judgment (approximately 1 page)**
Which approach better serves the analysis goal you stated in Section 1, and why? This requires naming what the decision-maker actually needed — a significance threshold, a probability about a parameter, a point estimate — and matching that need to a framework. Acknowledge what the other framework adds even if it is not the primary choice.

**Section 6: Epistemic Honesty (approximately 0.5 pages)**
What would change your conclusion? At minimum: what sample size or data quality would shift your confidence? What prior assumption, if wrong, would change your Bayesian result most? What model specification choice did you make that someone with different domain knowledge might make differently?

### Common Failure Modes to Avoid

**The false symmetry error.** "Both approaches have merits and each is useful in different contexts." This is true but useless. The scaffold requires you to state a preference in question 5 — forced prioritization is the point.

**The prior cop-out.** "I used a flat prior because I had no prior information." Before claiming you have no prior information, search for at least one published study or BLS prior-year data. Prior information is almost always available in labor market analysis. Choosing a flat prior is a defensible choice when justified; it is not a default that requires no defense.

**The p-value restatement.** "The Bayesian credible interval means there is a 95% chance the true value is in this range." This is actually correct for a credible interval — it is the misstatement you should apply to a confidence interval. Make sure you are applying each interpretation to the right interval.

**The implementation pass-through.** Accepting LLM output without checking it against the structure of the analysis. If the LLM reports a posterior that is identical to the frequentist point estimate with no visible effect of the prior, ask why. With 8 data points (Dataset C), the prior should move the posterior.

---

## What Would Change My Mind

This section is honest about the limits of the chapter design itself.

**On the dataset library.** The five datasets are real and verified. But they are all U.S. labor market data, which means the domain is narrow. A student whose research question lives in medicine, ecology, or finance might find the domain mismatch distracting. If your institution has a different dataset that is real, publicly available, and supports both frameworks — use it. The six-question scaffold applies to any dataset.

**On the worked partial example.** I chose Dataset C (Education Pays) because the 8-row structure fits on a page and the threshold question is the sharpest demonstration of the frequentist/Bayesian contrast. But the small N makes normal-theory frequentist tests questionable. A case could be made that Dataset D (Employment Projections) is more pedagogically honest because the sample is large enough that the frequentist tests are well-grounded. I stayed with Dataset C because the small-N limitation is itself instructive, not despite it.

**On whether the deliverable should be a report or a presentation.** The 4–6 page written format is chosen because writing forces precision in a way that presentation slides do not. A student who cannot write the prior justification paragraph probably cannot defend it in conversation either. If your course format requires a presentation, the six-question scaffold translates directly to six slides — but do not let the slides abbreviate the argument.

---

## Still Puzzling

The question that Chapter 12 leaves genuinely open is what it means to "choose" a framework when the two analyses return compatible conclusions. If your frequentist test is significant at the conventional level and your Bayesian posterior places most probability on a positive effect, and both favor the same action — did it matter which framework you used? The answer is yes, for at least one reason: the Bayesian analysis returned a quantity (a probability about a parameter) that the frequentist analysis could not, and if the decision-maker ever needs that quantity, you needed the Bayesian analysis. But if the decision-maker only ever needed the significance threshold, and the analyses agree on the threshold decision, the additional complexity of the Bayesian analysis was a cost with no benefit for this specific decision. Chapter 13 develops this into a framework. For now: the puzzle is real, not rhetorical.

---

## AI Wayback Machine

**W.E.B. Du Bois (1868–1963)**

W.E.B. Du Bois and his students at Atlanta University produced a series of statistical infographics for the 1900 Paris Exposition, displaying data on Black American social and economic conditions: employment, wages, education, property ownership. The datasets he used — Census records, labor surveys, state-level employment data — are the direct predecessors of the BLS and O*NET datasets this chapter uses. His infographics are comparative analyses of real labor market data, translated into visualizations designed to make the comparison legible to a non-technical audience (Du Bois 1900, *The Georgia Negro: A Social Study*, Paris Exposition).

Du Bois exemplifies both halves of the capstone. The analysis required statistical judgment: choosing what to measure, how to aggregate, what comparison to draw. The communication required something else: translating that comparison into a form that a general audience at a world exposition could grasp and act on. His work demonstrates that the deliverable is not finished when the analysis is finished. It is finished when the argument is made.

If you want to explore what Du Bois actually built, the Library of Congress holds the original visualizations and they are widely reproduced. Searching "Du Bois data portraits" will find high-resolution scans. The data structures — comparative tables across groups, longitudinal employment trends — map directly onto the analysis questions in this chapter's dataset library.

---

*Chapter 12 is the exercise. Chapter 13 gives you a framework for making the choice you just made in that exercise — systematically, across any problem you will face after this course.*
![W.E.B. Du Bois (1868–1963)](../images/w-e-b-du-bois-9ef.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

