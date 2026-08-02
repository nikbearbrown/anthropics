# The Clean-Looking Table That Said Two Different Things


## TL;DR

- TL;DR: Causal estimation output looks like a measurement and is, in fact, a deduction conditional on a spec you wrote — a deduction the estimator will produce whether your spec is right or wrong.
- The chapter moves through Opening — A clean-looking table, Concept one — The three-question diagnostic, Question 1: Tool versus spec, Question 2: Spec versus domain knowledge, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

**Suggested titles:**
1. The Clean-Looking Table That Said Two Different Things
2. Reading the Output: Three Questions and Four Silences
3. Narrow Intervals, Loud Assumptions: What the Estimator Cannot Tell You

**TL;DR:** Causal estimation output looks like a measurement and is, in fact, a deduction conditional on a spec you wrote — a deduction the estimator will produce whether your spec is right or wrong. A three-question diagnostic surfaces what the output is silent about, and a plain-language translation puts the result in front of the decision-maker without hiding the assumptions that hold it up.

**Byline:** Nik Bear Brown

**Prerequisites:**
- Chapter 11 — the defense: the analyst has written down the identification assumptions and named what would break them.
- Chapter 12 — the spec: the analyst has executed an estimation run through DoWhy, EconML, or hand-rolled IPW, and the tool has returned a table.
- Chapters 5–8 — confounders, mediators, colliders. You know what kinds of variables belong in an adjustment set and what kinds break it.
- Chapter 9 — the backdoor criterion and the sensitivity-analysis seed: the question "what if there's a confounder we did not measure?" is in the air, even if the answer is not yet.

**Learning objectives:**
- **Evaluate:** Apply the three-question diagnostic to a piece of causal estimation output handed to you and decide which questions the output passes, fails, or is silent about.
- **Analyze:** Name four classes of question the output is structurally silent about, with at least one domain example for each.
- **Evaluate (Part B):** Apply the diagnostic to output from an estimation run you executed yourself in your own domain, including overlap and refutation checks.
- **Create (Part B):** Write the plain-language translation of that output for a named decision-maker in your field — a translation that does not hide the identification uncertainty behind the sampling uncertainty.

---

## 1. Opening — A clean-looking table

It is a Wednesday afternoon in March 2024. Sit, for a moment, where the analyst sat: in front of a laptop, in front of a DoWhy notebook, in front of the output cell of `model.estimate_effect()`. The notebook just finished running. The cell printed a clean Python object. The relevant parts of it, transcribed into a table:

| Quantity | Value |
| --- | --- |
| Treatment | New retrieval model (v2) |
| Outcome | Mean user-satisfaction rating (1–5 scale) |
| ATE estimate | 0.150 |
| 95% CI | [0.12, 0.18] |
| p-value | < 0.001 |
| N (sessions) | 4,217,392 |
| Refutation: placebo treatment | effect 0.002, n.s. |
| Refutation: random common cause | effect 0.149, stable |
| Refutation: data subset (50%) | effect 0.151, stable |

Read that table the way you have been reading them for years. Effect positive. Interval narrow. P-value well below any threshold anyone would set. Three refutation tests pass. Over four million sessions. The table is, superficially, clean.

If you are the analyst — two weeks into the project, with your VP wanting a Friday answer on whether to ship v2 — what would you do with this output?

I will tell you what the analyst did. They forwarded a one-paragraph summary saying the new retrieval model produced a 15-point satisfaction lift with a tight CI. The VP signed off. The model shipped. Six weeks later, when the deployment dashboard's satisfaction metric had drifted *down* rather than up, the engineering manager pulled the analysis apart and found two things.

First: on day 8 of the 14-day rollout, a reranker fix landed on top of the new retrieval model. The "treatment" was actually two treatments stitched together — *v2 without the reranker fix* (days 1–7) and *v2 with the reranker fix* (days 8–14). The estimator was told "this is the treatment" and obediently averaged across both versions.

Second: code-completion queries — about 18% of traffic — had been routed away from the control arm during weekdays by a load-balancer rule nobody on the analysis team had noticed. Positivity, in the formal sense from Chapter 9, had quietly failed. The estimator extrapolated through the gap rather than telling anyone there was a gap.

Both problems existed before the cell finished running. Neither showed up in the output. The output was internally consistent and externally wrong, and the diagnostic that would have caught it took about forty-five minutes to run by hand. This chapter is that diagnostic.

Three questions. Four silences. One translation move at the end. The output that passes all three questions and still leaves four real things unspoken is the output you can act on honestly. The output that fails any of the three is the output where the next move is sensitivity analysis (Chapter 14) or a redesign (back to Chapter 12).

A note before we start. The three-question diagnostic and the four-silences list that follows are not standard apparatus in the published causal-inference literature. They are this book's structural contribution — codifications of moves the field already makes, in language an engineering reader can teach to themselves. The components are not original: every question, every silence, has been written about elsewhere by Greenland, by Wasserstein and Lazar, by Spiegelhalter, by Sharma and Kıcıman, by Hernán and Robins. What is new is the order and the integration. Treat them as instruments under test, not as gospel.

---

## 2. Concept one — The three-question diagnostic

The diagnostic is three questions, in this order. Order matters; the questions do not commute.

**Q1: Does the output's adjustment set match the spec's adjustment set?** Did the tool actually run what you told it to run?

**Q2: Are the identification assumptions in your spec — written down in Chapter 11's defense — plausible given current domain knowledge?** Even assuming the tool ran what you specified, is what you specified the right thing to ask?

**Q3: How sensitive is the estimate to a single unmeasured confounder of typical strength?** Even if everything plausible is plausible, how much of the conclusion is held up by the assumption you cannot test from the data?

Q1 is a *tool-output* question, Q2 a *domain* question, Q3 a *quantitative-robustness* question. Arranged cheapest-to-verify to most demanding. Skip ahead at your peril.

### Question 1: Tool versus spec

The spec — written before the run — names the treatment, outcome, adjustment set Z, identification strategy, and do-not-add list. The tool made its own decisions: defaults you did not override, automatic variable selection, propensity weighting. Q1 asks whether the tool obeyed the spec.

Concretely:

- Print the adjustment set actually used. DoWhy: `model.get_common_causes()`. EconML: inspect the `X` argument. Confirm it is exactly the spec's Z — not a superset, not a subset.
- Print the *effective* sample size after weighting or matching, not the raw row count. Inverse-probability weighting can give you a nominal n of four million and an effective sample size of forty thousand if propensity scores are extreme. The eye reads the raw count and over-trusts.
- Read the refutation log. The DoWhy refuters print seed, perturbation, and resulting estimate. If `random_common_cause` returned an estimate identical to four decimal places, the refuter ran but probably did not vary anything.
- Annotate every tool-default that contradicted your spec. EconML's `LinearDML` will one-hot-encode a categorical treatment and produce an "average" effect that is a comparison against an arbitrary baseline. If you specified a different baseline, the printed effect is not the effect you asked for.

The failure mode: the tool runs successfully and silently, the analyst reads the headline, and the headline answers a question the analyst did not ask. Q1 catches this before Q2 or Q3 is spent on a misread.

In the opening case, Q1 already had a problem. The reranker fix on day 8 made the treatment non-stationary, and the spec had not flagged it. Q1, asked honestly, would have surfaced "is the treatment definition stable across the period?" — and a five-minute conversation with engineering would have surfaced the day-8 deploy.

### Question 2: Spec versus domain knowledge

Assume Q1 passed. Now: is what you specified an honest representation of the world?

This is the question Chapter 11 wrote the defense for. Re-read your own defense. The identification assumptions — no unmeasured confounding, SUTVA, positivity, consistency — were defended on grounds the data does not contain. Q2 asks whether the defense survives contact with current domain knowledge.

What to look for: for each identification assumption, one piece of external evidence that could move your confidence (a new paper, an operational fact that surfaced during the run, a colleague's "oh, also, X happened in week 2"). The violations Chapter 11 explicitly named — did any of them happen? The positivity diagnostic — most causal libraries can produce overlap plots; regions where one arm has no mass are positivity violations. The CI does not know about them.

In the opening case, code-completion queries had near-zero traffic in the control arm during weekdays. The overlap plot would have shown the histogram going to zero in a region of covariate space. The CI assumed extrapolation was honest.

### Question 3: Sensitivity to unmeasured confounding

The third question is the answer to "even if Q1 and Q2 are clean, how big a problem would an unmeasured variable have to be to overturn the headline?"

I am going to give you the question now and the apparatus next chapter. Chapter 14 develops the E-value — VanderWeele and Ding's 2017 quantitative statement of exactly this: how strongly associated would an unmeasured U have to be with both T and Y to reduce the observed effect below some threshold ([VanderWeele & Ding 2017, *Annals of Internal Medicine*](https://doi.org/10.7326/M16-2607)). For now, the question is informal and still load-bearing: imagine a plausible unmeasured variable, of plausible strength, that influences both treatment and outcome. Would including it move the estimate by a little, or by a lot?

What to look for: a list of *named* candidate unmeasured confounders — not "some unmeasured variable" but specific things the domain expert is worried about (*healthy-user selection* in the HRT case; *marketing-campaign overlap* in pricing; *seasonal traffic mix* in retrieval). An informal magnitude estimate. A clear statement of what the analysis would conclude if the candidate is real and strong, versus absent or weak.

In the opening case, Q3 had a problem too. The two-treatment problem from Q1 and the positivity violation from Q2 each plausibly account for the entire 0.15 effect — or, in the worst case, reverse it. The diagnostic does not require the exact reversal point yet. It requires noticing the reversal is well within the range of plausible perturbation.

### Why the order matters

If the tool did not run what you specified (Q1 fails), it does not matter whether your spec was right (Q2). If the spec was wrong (Q2 fails), it does not matter whether the estimate is robust to a plausible unmeasured confounder (Q3) — the estimate is robust around the wrong number. The order is not pedagogical convenience; it is the dependency structure of the diagnostic.

The most common failure mode I see in production work, and the one I have done myself, is to skip Q1 because the tool "obviously ran fine" and start arguing about Q2 with the domain expert. The tool's silence is not the same as the tool's success. Run Q1 first. It takes ten minutes. It catches at least a third of the problems.

A common misconception: the DoWhy refutation suite — placebo treatment, random common cause, subset refutation — feels like it covers all three questions. It does not. The refuters live inside Q1. They test whether the *procedure*, given the spec, behaves as expected. They cannot test whether the spec is right (Q2), and they cannot test whether the world is right (Q3). Sharma and Kıcıman are explicit about this in the DoWhy paper ([Sharma & Kıcıman 2020, arXiv:2011.04216](https://arxiv.org/abs/2011.04216)).

---

## 3. Mid-chapter checkpoint

Stop. Take the opening table. Can you write down right now:

1. The exact adjustment set the analyst was using? (You can't — the spec was not pasted in. That is the *point*.)
2. The named identification assumptions from a Chapter 11 defense for this analysis? (Same answer.)
3. One plausible unmeasured confounder for the retrieval-quality A/B test? (Day-of-week traffic mix. Holiday seasonality. Engineering hotfix overlap. Marketing campaign timing.)

If you cannot answer 1 and 2 from the table alone, you are reading the output as a self-contained measurement. It is not. It is a deduction conditional on documents that did not appear in the cell. The first diagnostic move is to retrieve them.

---

## 4. Concept two — Four things the output cannot tell you

The three questions catch what the output *should* address. There is a second list — separate from the diagnostic — that catches what the output *cannot* address no matter how well the diagnostic passes. The diagnostic surfaces problems with the spec or the world the spec describes. The four silences surface problems with the *category of claim* the output is making.

Like the diagnostic, the four-things list is original to this book in its codification. The individual silences are well-documented in the literature; what is new is the framing as "four things, named, that the output is structurally silent about." Use them as a checklist, not a creed.

### Silence one: Whether your DAG is right

The estimator runs against a DAG. The output is the answer the DAG implies, given the data. If the DAG is wrong — edges missing, extra edges, arrows pointing the wrong way — the output is the right answer to the wrong graph.

The data cannot certify the DAG. Conditional-independence tests can falsify *some* DAGs given enough power, but they cannot rule one in. Two DAGs can imply the same set of conditional independences and yield different causal estimates — what the literature calls *Markov-equivalent* graphs. The data is silent on which member of the equivalence class is correct.

Domain example. A clinical workflow analyst draws a DAG with `discharge_instructions → readmission`. The hospitalist colleague, asked, says "actually, what reduces readmission is the *nursing contact time* required to deliver the instructions, not the instructions themselves." The DAG should have `instructions → nursing_contact → readmission`. The output of the original DAG-based analysis cannot distinguish.

### Silence two: Whether there is an unmeasured confounder

The silence Chapter 14 will quantify. The no-unmeasured-confounding assumption — *exchangeability* conditional on Z — is the load-bearing assumption of nearly every observational causal estimate, and the data does not verify it. The data can verify that *measured* confounders have been adjusted for. It cannot verify that nothing else exists.

Domain example. A fraud-detection model's evaluation says "the model prevented 30% of fraud." An unmeasured variable — the adversarial response of fraudsters to the model's deployment — is plausibly large and signed in a way that overstates the 30%. Q3 names the worry; the data does not resolve it. Chapter 14's E-value gives you the quantitative version.

### Silence three: Whether the analyzed population matches the deployment population (transportability)

The estimate is for the sampled population under the conditions of the analysis. The deployment population is somewhere else. Generalizability is a separate identification question with its own apparatus, developed by Tipton and Hedges over the last decade ([Tipton & Olsen 2018, *Educational Researcher*](https://doi.org/10.3102/0013189X18781522); see also Pearl & Bareinboim's transportability work).

Domain example. A randomized trial of a discharge-instruction intervention runs at a single academic medical center with a relatively young patient population, returning a 12 percentage-point reduction in 30-day readmission. The hospital system adopting the intervention serves an older, more comorbid population in community hospitals. The output is silent on whether the 12-point effect survives the population shift.

### Silence four: What decision the number supports

The estimate is one input to a decision. The decision depends on cost, side effects, reversibility, competing interventions, the next quarter's adversarial environment. None of those things is in the number.

Domain example. The opening retrieval-quality A/B test returned 0.15 mean-satisfaction lift. Suppose it had been real and clean. Is shipping it the right call? Depends on: serving cost of v2 versus v1, inference latency at peak load, model-update cadence and re-training cost, brand-risk profile of v2's failure modes. The number does not contain any of those. Spiegelhalter's *Art of Statistics* spends an entire chapter on this distinction.

A common misconception: "if the effect is statistically significant, it is decision-relevant." Wrong both ways. A 0.001% lift at p < 0.001 (large n) is real and not worth doing. A 5% lift at p = 0.08 (small n, cheap intervention) is plausibly worth shipping. The estimator cannot make this call.

The four silences are not failures of the diagnostic. They are limits of the *category of object* the output is. The output is a measurement of a parameter conditional on a model. It cannot be a verdict on the world.

---

## 5. Concept three — What narrow confidence intervals actually mean

This is the chapter's quantitative anchor. The CI is where engineering students plant their feet wrongly more often than anywhere else in the output.

A 95% confidence interval is *a property of the estimation procedure*, not a probability statement about the parameter. The technical reading: if we ran the same procedure many times on samples drawn from the same data-generating process, 95% of the resulting intervals would contain the true parameter — *provided the procedure's assumptions hold*. The guarantee is conditional, and it is about the long-run behavior of intervals produced this way, not about the specific interval you are looking at.

Greenland and colleagues spell this out in their 2016 *European Journal of Epidemiology* paper ([Greenland et al. 2016](https://doi.org/10.1007/s10654-016-0149-3)). They list twenty-five misinterpretations of standard output, of which roughly a dozen are about CIs. The most common: the belief that a 95% CI gives you a 95% probability that the parameter lies inside it. The CI does not say that. Whether the *one* interval in front of you is among the 95% or the 5% is unknowable from the interval itself.

This sounds like philosophical hair-splitting. It is not. The *practical* reading of a narrow CI in causal analysis is this: **the assumptions are doing the work**.

Let me show it.

Suppose the analysis is honest about *sampling* variance — the procedure was well-implemented, the bootstrap was clean, the cluster-robust standard errors accounted for the within-session correlation, the n was large. The 95% CI of [0.12, 0.18] honestly reflects: *if the spec is right*, the estimate is within ±0.03 of the truth with the coverage rate the CI claims. That is what the CI does. It quantifies sampling variance.

Now suppose there is an unmeasured confounder we will call U, of moderate strength. U influences both the treatment and the outcome. The structural form is:

$$Y = \beta T + \gamma U + \varepsilon$$

with $T$ also influenced by $U$ — say $E[T|U] = \pi + \delta U$, so $U$ is associated with $T$ at the strength $\delta$. The estimator, fed the data, computes its best linear estimate of $Y$ on $T$ controlling for the observed adjustment set Z. The estimate of $\beta$ is biased by an amount that, in the simple linear case, has a closed form. Let's run it.

Suppose the true $\beta$ is 0.05. Suppose $\gamma$ (the effect of U on Y) is 0.4. Suppose $\delta$ (the influence of U on the probability of treatment, residualized on Z) is 0.25. The omitted-variable-bias formula says the OLS estimate of the treatment coefficient is approximately

$$\hat\beta_{OLS} \approx \beta + \gamma \cdot \delta = 0.05 + 0.4 \cdot 0.25 = 0.05 + 0.10 = 0.15$$

The estimator returns 0.15. The 95% CI, based on the residual variance of the regression and the sample size, is [0.12, 0.18]. The CI is narrow because n is large. The CI is *correct* about sampling variance — the estimate is genuinely centered around 0.15 with the precision the CI claims. The CI is *silent* about the fact that 0.10 of the 0.15 is bias from U.

The narrow CI is honest about sampling variance and lies about identification uncertainty. Read that sentence twice. The interval [0.12, 0.18] tells you: *if you accept the identification assumptions*, the truth is in here with the coverage rate the procedure provides. It does not tell you: *the truth is in here.* If U exists, the truth could be 0.05 — outside the interval by a factor of two. The interval did not warn you, because the interval cannot warn you. Identification uncertainty is upstream of the interval.

A useful way to hold this: sampling uncertainty is the *width* of the interval; identification uncertainty is the *location* of the interval. The CI computes the width well. It does not compute the location at all. The location is set by the assumptions, and the assumptions are upstream of the data.

Operationally: the narrow CI measures how precisely your *procedure* is estimating whatever it estimates — not how close that quantity is to the causal effect you wanted. With enough data, every misspecified model produces a narrow CI around the wrong number. The decision-relevant uncertainty in a causal analysis is almost always the location uncertainty, not the width uncertainty.

Greenland and colleagues — most directly in a 2019 *Nature* comment co-authored with Amrhein and McShane ([Amrhein, Greenland, McShane 2019, *Nature* 567:305–307](https://doi.org/10.1038/d41586-019-00857-9)) — have argued that "confidence interval" be retired in favor of *compatibility interval*. The proposed rename says what the interval is for: it identifies the range of parameter values *compatible* with the data, given the procedure's assumptions. The original term suggests a probabilistic guarantee the procedure does not provide. The field has not converged. The reasoning is sound. The pedagogical move in this book: use *confidence interval* when quoting standard output; use *compatibility interval* when arguing about what the interval contains.

The HRT case from Chapter 2 is the canonical demonstration. The Nurses' Health Study produced narrow CIs around a confidently *protective* observational estimate of hormone replacement therapy on cardiovascular outcomes ([Stampfer et al. 1991, *NEJM*](https://doi.org/10.1056/NEJM199109123251102)). The Women's Health Initiative RCT in 2002 ([Manson et al. 2003, *NEJM*](https://www.nejm.org/doi/full/10.1056/NEJMoa030808)) produced narrow CIs around a confidently *harmful* estimate. Same intervention. Same outcome class. Opposite signs. The observational CIs were correctly computed and centered on the wrong number, because *healthy-user selection* — a structural confounder upstream of the data — set the location of the interval where the data could not see. The field of causal inference grew up around problems where the location of the interval matters more than the width, and where narrow intervals around wrong numbers are the modal failure rather than the exception.

---

## 6. Concept four — P-values and the post-2016 framing

A paragraph addressed directly to the engineering reader, because most readers of this book have been taught the older p-value framing and the field has moved on.

You were taught, somewhere, that p < 0.05 means "statistically significant," that p > 0.05 means the null cannot be rejected, and that the threshold divides effects to report from effects to file away. None of that survives a careful reading of the contemporary literature. The American Statistical Association said as much, formally, in 2016. The follow-up 2019 special issue said it again, with seventeen articles arguing for substantial reform of how p-values are used.

The current consensus, from the 2016 ASA statement ([Wasserstein & Lazar 2016](https://doi.org/10.1080/00031305.2016.1154108)) and Wasserstein, Schirm, and Lazar's 2019 editorial ([Wasserstein, Schirm & Lazar 2019](https://doi.org/10.1080/00031305.2019.1583913)):

- A p-value is a *compatibility statement*, not a verdict. Under the null and the model's assumptions, the p-value is the probability of observing data at least as extreme as the data you observed. Small p-values indicate the data are unlikely under the null *given the assumptions*. They do not measure the probability that the null is true, the size of the effect, or the importance of the result.
- The 0.05 threshold has no inferential basis. Fisher proposed it as a convenience. Treating it as a verdict discards information and produces irreproducible science.
- The 2019 editorial recommendation: stop using "statistically significant." Report the p-value as a continuous quantity. Interpret it in context with effect sizes, prior evidence, study design, and identification assumptions.

Amrhein, Greenland, and McShane's 2019 *Nature* comment put the one-paragraph version on the record: "We are not calling for a ban on P values… What we hope will happen is that the 0.05 threshold will lose its status as a yardstick of importance. We want researchers and editors to treat the P value as a continuous measure of the compatibility of the data with the null hypothesis."

The operational consequence is small but important. When you read `p < 0.001`, the p-value is doing one job: telling you that, under the spec's assumptions, the data are very unlikely to have arisen if the true effect were zero. That is useful. It is not a license to say "the effect is real." The four silences are unaffected by the p-value's size. The workflow `if p < 0.05 then ship else don't` is widespread in A/B-testing infrastructure and structurally incompatible with the causal framing of this book — the ship decision depends on the four silences, all of which the p-value is silent about.

---

## 7. The plain-language translation

The diagnostic surfaces problems. The four silences name what cannot be surfaced. Both feed one final move: translating the output into a sentence a decision-maker can act on without being misled.

Engineering students treat this as polishing prose. It is not. The translation is the deliverable. The decision-maker reads the translation, not the table; if the translation hides the assumptions, the decision is made under the wrong cover.

A useful three-part structure: the claim, the named uncertainty, the consequence. *What we found, what we are assuming, what you can do with it.*

**Not this:** "The treatment effect was 0.15 with 95% CI [0.12, 0.18], p < 0.001."

That sentence is the table read aloud. It carries the sampling uncertainty and elides everything else. The decision-maker hears "the effect is between 12 and 18 percent" and cannot act honestly on what they heard.

**This, instead:** "Our analysis is consistent with a satisfaction lift of 12 to 18 percent on the sampled queries, assuming the new retrieval model behaved consistently across the two-week test window and that query types in the test mix are comparable to deployment traffic. If a meaningful fraction of the test window included a hotfix on top of the new model — which is what happened on day 8 — the headline number overstates the lift; the corrected estimate is closer to 5 to 10 percent. I am not yet confident in any number until that confound is resolved."

Longer. Same statistical content. Also: the named identification assumption (consistency), the identified violation (day-8 hotfix), the implied range of the corrected number, the honesty that the analysis is not yet decision-ready. The decision-maker can act on this — including the action "wait" — and can push back: "what if we re-run on days 1–7 only?" That is the conversation the analysis should produce.

Spiegelhalter's *The Art of Statistics* spends its final chapters on this move. Fischhoff and Davis's *PNAS* 2014 paper ([Fischhoff & Davis 2014](https://www.pnas.org/doi/10.1073/pnas.1317504111)) is the citable academic source: decision-makers do not need uncertainty hidden, and they do not need it in the analyst's native vocabulary. They need it translated to "here is what I would do if I had to act on this number, and here is what would change my mind."

A common misconception: "translation means dumbing down." It does not. Translation means matching the decision-maker's information need. A clinician reading a readmission analysis wants to know "is the effect large enough to change discharge protocol, and how confident should I be that it transfers to my patient population?" Neither question is answered by the CI alone. The translation puts the answers — including "we don't know yet, here is why" — in front of the person who has to act.

The Part B exercise asks you to write this translation for a real decision-maker in your field. That deliverable, scaled up, is the Final Project of Chapter 15. The translation is not the polish on the analysis. It is the analysis, made decision-actionable.

---

## 8. The method applied to the diagnostic

An honest accounting of where the three-question diagnostic does not catch problems.

The diagnostic catches *identification* issues with the analysis as specified. It does not catch:

- **Effect heterogeneity.** The ATE can be 0.15 in a population that contains subgroups with effects +0.40 and -0.10. Conditional ATEs, causal forests, subgroup analyses are a separate apparatus.
- **External validity beyond the sampled population.** Silence three names it; the diagnostic does not solve it. Transportability methods (Pearl & Bareinboim 2014, Tipton & Hedges 2017) require additional structure.
- **Measurement error.** The diagnostic assumes treatment and outcome are measured as specified. Misclassification or instrument drift biases the estimate in directions the diagnostic does not address.
- **Time-varying confounding.** Cross-sectional confounding only. Time-varying confounders affected by earlier treatment require the g-formula or marginal structural models.

The diagnostic is a starting tool, not a complete inventory. Use it where it works. When the question is heterogeneity, transportability, measurement error, or time-varying confounding, reach for the right tool. Name where the diagnostic stopped helping.

---

## 9. Worked example — Applying the diagnostic to the opening case

Walk back to the opening table. Run the diagnostic the way you would on a Friday morning before the VP meeting.

**Spec, retrieved from the Chapter 12 spec doc** (paraphrased): Treatment = retrieval v2, 50% randomized sample, two-week window Mar 4–17. Outcome = mean post-session satisfaction (1–5). Adjustment set Z = {user_tenure_bucket, query_category, device_type, day_of_week}. Identification = session-level randomization with adjustment for design imbalances. Do-not-add = {satisfaction_in_previous_session (descendant), engagement_in_session (mediator)}. Assumptions = SUTVA at the session level, positivity across adjustment cells, stable treatment definition.

**Q1, adjustment set.** `model.get_common_causes()` returns {user_tenure_bucket, query_category, device_type, day_of_week, holiday_indicator}. DoWhy added `holiday_indicator` from automatic backdoor identification; the spec did not include it. **Failing softly.** Re-run with the exact spec Z, document the discrepancy.

**Q1, treatment stability.** Engineering confirms a reranker patch deployed at 14:22 UTC on Mar 11 to the v2 arm. The treatment in days 1–7 is not the same as the treatment in days 8–14. **Failing hard.** Split the analysis at the day-8 boundary.

**Q2, identification assumptions.** Inspect overlap. Code-completion × weekday × control has 47 sessions out of an expected ~370,000 — a load-balancer rule from February routed that category away from control. **Failing.** Either restrict to query categories with adequate overlap, use an overlap-weighted estimator that is honest about the extrapolation, or acknowledge the headline is not generalizable to code-completion.

**Q3, sensitivity.** Name a candidate: query-difficulty drift. If hard queries shifted into one arm during the second week (which the load-balancer plausibly caused), and hard queries have lower baseline satisfaction, the estimate is confounded by query difficulty. Informal magnitude: plausibly large. **Warning, not yet quantified.** Compute the E-value next chapter.

**Four silences:** DAG correctness — was `holiday_indicator → satisfaction` an omission or a modeling choice? Unmeasured confounders — query-difficulty drift; also possibly user-side learning as users adapt to v2's style. Transportability — the 14-day window straddles spring break; deployment traffic mix will not match. Decision relevance — the platform team estimates ~12% higher serving cost.

**Plain-language translation, drafted for the VP:**

> The two-week test of the new retrieval model gave a headline of about 15 points higher mean satisfaction, with a sampling-precision range of 12 to 18 points. I do not yet trust that number for shipping. Two things broke during the test. On day 8, an engineering hotfix landed on top of the new model only — so the "treatment" in the second half is not the same as the treatment in the first half. Separately, a load-balancer rule from February kept code-completion queries — about 18 percent of traffic — almost entirely out of the control arm during weekdays, which means the test population is not representative of the deployment population for that query category. My best estimate of the honest lift, with each issue addressed, is somewhere between 5 and 10 points, with much wider uncertainty than the headline showed. Factor in roughly 12 percent higher serving cost. If the goal is "ship if the lift is at least 8 points net of serving cost," I cannot yet say we have met the bar. I can have a clean re-analysis within five business days if engineering can hold the deploy.

That paragraph is longer than "+0.15, [0.12, 0.18], p < 0.001." It carries the claim, the named uncertainty with specific violations, and the consequence. The VP can act on this — including the action "wait." That action was not available from the original table.

The original table was clean. The corrected analysis is not. Honest analysis is sometimes the act of *un-cleaning* the output.

---

## 10. Chapter summary

The output of a causal estimation run is a deduction conditional on a spec, not a measurement of the world. The estimator does what it was asked; it does not check whether the asking was right.

Three questions in order surface what the output should address: did the tool run what you specified (Q1), is the spec plausible given current domain knowledge (Q2), is the estimate robust to a plausible unmeasured confounder (Q3, expanded in Chapter 14). The order is dependency, not preference. Refutation tests live inside Q1, not above it.

Four silences name what the output cannot address regardless of how well the diagnostic passes: whether the DAG is right, whether an unmeasured confounder exists, whether the sampled population matches the deployment population, what decision the number supports. The diagnostic surfaces problems with the spec; the four silences are limits of the *category of object* the output is.

Narrow confidence intervals are honest about sampling variance and silent about identification uncertainty. Sample size shrinks intervals; it does not move them toward the truth. The contemporary literature has moved toward calling these *compatibility intervals* and toward retiring the "statistically significant" verdict-style reading of p-values.

The plain-language translation is the deliverable. Three parts: the claim, the named uncertainty, the consequence. Translation is not dumbing down; it is matching the decision-maker's information need.

The three-question diagnostic and the four-silences list are this book's structural contributions — original codifications of moves the field already makes. They do not cover heterogeneity, transportability, measurement error, or time-varying confounding. Instruments under test, not canon.

---

## 11. Bridge to Chapter 14

Three questions land us at a specific worry: even when Q1 and Q2 are clean, Q3 was informal. Chapter 14 makes it quantitative. The E-value — VanderWeele and Ding's 2017 sensitivity parameter — is the answer to "how strongly associated would an unmeasured confounder of treatment and outcome have to be to reduce the observed effect below a chosen threshold?" The E-value completes Q3.

Chapter 14 also takes the seed planted in Chapter 9. Chapter 10's answer to "unmeasured variable on a backdoor path" was *non-identifiability*. Chapter 14's complementary answer is *sensitivity analysis*: when point identification is unavailable, the principled move is to quantify how badly the assumption can fail before the conclusion changes. Read Chapter 14 as the quantitative answer to the worry the diagnostic surfaces; read this chapter as the framework that decides whether the worry was warranted.

---

## 12. Exercises

### Warm-up

**Exercise 13.1 — Apply Q1 to a table.**

Spec: treatment = `program_assigned` (binary), outcome = `earnings_year2`, Z = {`age`, `education_years`, `prior_earnings`}, identification = unconfoundedness conditional on Z, do-not-add = {`employment_year1` (mediator)}.

Tool printout:

```
ATE estimate: 1842.50
95% CI: [1610.30, 2074.70]
p-value: < 0.001
N: 12,548
Adjustment set used: {age, education_years, prior_earnings, race_indicator,
                     employment_year1}
Refutation: placebo: 22.10, n.s.
Refutation: subset (60%): 1839.20, stable
```

Apply Q1. List every discrepancy between the tool's adjustment set and the spec's Z. For each discrepancy, decide whether it is harmless, biasing, or unknown, and justify the call.

**Exercise 13.2 — Name the assumptions doing the work.**

A clinical analysis reports an estimated reduction in 30-day readmission of 11.4 percentage points, with 95% CI [10.8, 12.0], on a sample of 38,000 patients. The CI is narrow.

Without seeing the spec or the DAG, list five identification assumptions that, if violated, would invalidate the headline. For each, name a domain-plausible mechanism by which it could fail.

### Application (Part A)

**Exercise 13.3 — The full diagnostic on a provided run.**

The teaching repository contains `ch13_partA_output.json` (a causal-estimation run on the NSW Lalonde reanalysis, treated as a causal-from-observational exercise), `ch13_partA_spec.md` (the spec), and `ch13_partA_defense.md` (the Chapter 11 defense). Apply the three-question diagnostic in full. Document each question's check, finding, and status. Run the four-silences checklist and note which silences are load-bearing for this output. Submit a one-page diagnostic report.

### Application (Part B)

**Exercise 13.4 — The diagnostic on your own domain output.**

Take the estimation run from Chapter 12's Exercise 12.5 (your DAG, your data, your spec). Apply the three-question diagnostic and the four-silences pass. Submit: (1) Q1 verdict with the tool's actual adjustment set pasted alongside the spec; (2) Q2 verdict with a one-paragraph re-statement of each identification assumption in light of what surfaced during execution; (3) Q3 verdict with an informal magnitude estimate of a named candidate unmeasured confounder; (4) four-silences pass with one named worry per silence.

### Synthesis

**Exercise 13.5 — The plain-language translation.**

Take the output from Exercise 13.4 and write the plain-language translation for a named decision-maker in your field. The translation should: open with the claim in domain language; name the identification assumptions in the decision-maker's vocabulary; include the four-silences-relevant caveats in the order they affect the decision; close with what action the analysis supports, what it does not yet support, and what would change your mind. Length: 250–400 words. If the decision-maker cannot read it in two minutes, you have not finished translating.

### Challenge

**Exercise 13.6 — The published paper.**

Pick a recent (post-2020) applied causal-inference paper in your field. Apply the three-question diagnostic to its reported output. For each question, identify which evidence in the paper bears on it. Write a one-page review with: the paper's headline claim, your three-question diagnostic, the four-silences pass, the plain-language translation you would write for *that paper's* implied decision-maker, and what the paper's conclusion should be in your reading. The review is honest, not adversarial. The diagnostic does not exist to debunk — it exists to surface what the output is silent about.

---

## 13. LLM exercise

Hand a recent chatbot model a piece of clean-looking causal estimation output and ask it to interpret. Then apply your own three-question diagnostic to the LLM's interpretation.

Prompt to copy and paste:

> I have the following output from a causal estimation run using DoWhy:
>
> Treatment: new ranking algorithm
> Outcome: average user dwell time per session (seconds)
> ATE: 18.4
> 95% CI: [16.2, 20.6]
> p-value: < 0.001
> N: 2,840,000 sessions
> Adjustment set: device_type, user_tenure, session_position
> Refutation (placebo): 0.3, n.s.
> Refutation (random common cause): 18.3, stable
> Refutation (subset 50%): 18.5, stable
>
> Please interpret this output. Tell me whether the result is trustworthy and whether the team should ship the new ranking algorithm to all users.

After the LLM responds, grade on six axes:

1. Did it ask for the spec doc, the Chapter 11 defense, or the DAG? If not, the LLM is treating the table as a self-contained object — the failure mode this chapter exists to correct.
2. Did it make a Q1-shaped move (check whether the tool's adjustment set matches a specified Z)?
3. Did it make a Q2-shaped move (interrogate the identification assumptions)? If yes, name the assumptions it surfaced.
4. Did it make a Q3-shaped move (consider sensitivity to a named, plausible unmeasured confounder)?
5. Did it treat the narrow CI and the low p-value as evidence the result is trustworthy? Score whether it propagated the chapter's primary misreading.
6. Did it produce a plain-language translation that included the named uncertainty? Or a "ship it" recommendation that hid the assumptions under the headline?

Submit a one-paragraph note as your deliverable.

What to expect. Current models (Claude 4 / 4.5 family, GPT-4o and successors, Gemini 2 family, as of mid-2026) are reasonably good at quoting the contemporary statistical-significance reform literature when prompted directly, and surprisingly bad at applying it spontaneously to output handed to them. They produce confident-sounding interpretations that frequently miss Q1 — because Q1 requires retrieving and comparing the spec, which is not in the output. They often miss Q2 unless explicitly prompted, and even then tend toward generic answers rather than spec-specific assumptions. They are most reliable when used as a *draft reviewer* given the spec, the defense, and the output together; least reliable as one-shot interpreters of the table alone. The 2025 ACL findings on LLM use in causal inference make this point explicitly ([Joshi et al. 2025, NAACL findings](https://aclanthology.org/2025.findings-naacl.327.pdf) `[verify-author-list]`; [arXiv:2506.00844](https://arxiv.org/abs/2506.00844) `[verify-DOI]`).

The chapter's point is not "do not use LLMs to read causal output." The point is that the diagnostic is the human's job because it depends on documents the LLM does not see by default. Give the LLM the spec, the defense, and the output. Then it can be a useful draft reviewer. Treat its commentary as a junior analyst's: a first pass to verify, not a verdict to forward.

---

## 14. AI Use Disclosure

This chapter was drafted with the assistance of Claude (Anthropic), using the Feynman-voice pedagogical scaffold defined in the workshop's CLAUDE.md and pantry notes prepared for Chapter 13. Primary sources cited were checked against original venues where possible; citations flagged `[verify]` are pending Nik's review. The opening retrieval-model A/B-test case is a structurally accurate but anonymized composite drawn from the pantry's "RAG retrieval-quality A/B test" case and public industry experimentation post-mortems. No specific company is named.

---

## 15. Part B bonus

If Exercise 13.4 found all three questions passing cleanly: write a one-page memo to the senior decision-maker, formatted as the Exercise 13.5 translation, but explicitly noting which of the four silences you *cannot* reduce on the current data and what data collection or experimental design would address it.

If Exercise 13.4 surfaced a failure: write an internal memo to your own team naming the failure honestly, proposing a re-analysis path, and estimating cost (analyst-days, data-collection requirements, time-to-deliver). Not a blame document — a redesign proposal. Office hours will ask whether your redesign actually fixes what you identified.

---

## 16. Key terms

- **Three-question diagnostic.** A three-part check applied to causal estimation output: Q1, does the tool's run match the spec; Q2, is the spec plausible in domain terms; Q3, is the estimate robust to a plausible unmeasured confounder. Original codification in this book. (Sections 2, 8, 9.)
- **Four silences.** Four classes of question the output is structurally silent about: DAG correctness, unmeasured confounding, transportability, decision relevance. Original framing; underlying points well-documented elsewhere. (Section 4.)
- **Confidence interval.** A property of the estimation procedure: under repeated sampling with the same procedure, X% of intervals so produced contain the true parameter, conditional on the procedure's assumptions. Not a probability statement about the specific interval. (Section 5.)
- **Compatibility interval.** Greenland and colleagues' proposed renaming, intended to make clear that the interval names the range of parameter values *compatible* with the data given the assumptions. (Section 5.)
- **Identification uncertainty vs. sampling uncertainty.** Sampling uncertainty is the width of the CI; identification uncertainty is the location. CIs compute the width well and do not address the location at all. (Section 5.)
- **P-value as compatibility statement.** Post-2016 ASA framing: the p-value is the probability of observing data at least as extreme as observed, under the null and the model's assumptions. Not a verdict, not an effect-size measure, not a threshold to dichotomize. (Section 6.)
- **Plain-language translation.** The deliverable produced from the diagnostic and the four-silences pass: the claim, the named uncertainty, the consequence. (Section 7.)
- **Refutation test (DoWhy).** A test of how the estimator behaves under specific perturbations: placebo treatment, random common cause, data subset. Lives inside Q1; necessary but not sufficient. (Section 2.)
- **E-value (preview).** VanderWeele and Ding's 2017 sensitivity parameter — the minimum strength of association an unmeasured confounder would need with both treatment and outcome to fully explain away the observed effect. Chapter 14. (Sections 2, 11.)

---

## 17. Further reading

- Greenland, Senn, Rothman, Carlin, Poole, Goodman, Altman, "Statistical tests, P values, confidence intervals, and power: a guide to misinterpretations," *European Journal of Epidemiology* 31(4) (2016), 337–350. https://doi.org/10.1007/s10654-016-0149-3 — the canonical contemporary statement of what statistical output means and does not mean. Read in full.
- Wasserstein & Lazar, "The ASA's Statement on p-Values," *The American Statistician* 70(2) (2016), 129–133. https://doi.org/10.1080/00031305.2016.1154108
- Wasserstein, Schirm & Lazar, "Moving to a World Beyond 'p < 0.05'," *The American Statistician* 73(sup1) (2019), 1–19. https://doi.org/10.1080/00031305.2019.1583913 — recommends retiring "statistically significant."
- Amrhein, Greenland & McShane, "Retire statistical significance," *Nature* 567 (2019), 305–307. https://doi.org/10.1038/d41586-019-00857-9 — the one-page version, co-signed by hundreds of statisticians.
- David Spiegelhalter, *The Art of Statistics: How to Learn from Data* (Basic Books, 2019). The chapter's "plain-language translation" move is modeled on Spiegelhalter.
- Fischhoff & Davis, "Communicating scientific uncertainty," *PNAS* 111 (Supplement 4) (2014), 13664–13671. https://www.pnas.org/doi/10.1073/pnas.1317504111
- Sharma & Kıcıman, "DoWhy: An End-to-End Library for Causal Inference," arXiv:2011.04216 (2020). https://arxiv.org/abs/2011.04216
- Hernán & Robins, *Causal Inference: What If* (CRC, 2020). Freely available online; the engineering-readable reference for identification assumptions and their failure modes.
- VanderWeele & Ding, "Sensitivity Analysis in Observational Research: Introducing the E-Value," *Annals of Internal Medicine* 167(4) (2017), 268–274. https://doi.org/10.7326/M16-2607 — the E-value, in advance of Chapter 14.
- Tipton & Olsen, "A Review of Statistical Methods for Generalizing from Evaluations of Educational Interventions," *Educational Researcher* 47(8) (2018), 516–524. https://doi.org/10.3102/0013189X18781522

---

## 18. Draft flags

Items flagged during drafting and pending Nik's review:

- Joshi et al. 2025 NAACL findings author list `[verify-author-list]` — title and venue confirmed; authorship not re-checked against ACL Anthology.
- arXiv:2506.00844 author list and exact title `[verify-DOI]` — paper exists at the cited arXiv ID per pantry research; final published version not confirmed.
- The Tipton & Olsen 2018 *Educational Researcher* DOI was checked against pantry research; cited as the transportability reference (Pearl & Bareinboim 2014 is the methodologically deeper alternative).
- The Manson et al. 2003 NEJM URL is the journal page rather than a DOI.
- Greenland 2022 "compatibility interval" specific paper was not cited directly; the chapter uses the Amrhein, Greenland, McShane 2019 *Nature* piece as the primary source for the rename argument.
- The opening retrieval-model case is anonymized and structurally composite; no specific company is named.

---

## What would change my mind

If a tool emerges that, given the output of a causal estimation run and access to the analysis's data, *automatically* retrieves the spec doc, reconstructs the analyst's identification defense, applies the three-question diagnostic, and produces a plain-language translation that matches the diagnostic's findings — and if peer-reviewed evaluations show the tool's output is reliably equivalent to a careful human analyst's diagnostic on held-out cases — then the chapter's framing of "the diagnostic is irreducibly human" would need revision. The diagnostic's components, taken individually, are mechanizable; what is currently not mechanizable is the *retrieval-and-integration* across the spec, the defense, and the data. If that gap closes, the chapter's claim narrows from "irreducible" to "currently expensive to automate."

## Still puzzling

I do not yet have a clean account of the trade-off between the diagnostic's completeness and its cost. The three questions are the minimum I am willing to defend; a fuller diagnostic — including heterogeneity checks, measurement-error checks, time-varying confounding checks — could be defended as more complete and would be more expensive to apply. Where the engineering-practical cutoff lies, and how it should adapt to the stakes of the decision, is something I am working out chapter by chapter. The Final Project in Chapter 15 is partly an attempt to surface this trade-off in the student's own work.

---

**Tags:** reading-the-output, three-question-diagnostic, compatibility-interval, p-value-reform, plain-language-translation
