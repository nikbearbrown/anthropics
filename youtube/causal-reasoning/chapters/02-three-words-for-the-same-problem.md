# Three Words for the Same Problem


## TL;DR

- TL;DR: Conditioning, confounding, and controlling-for produce identical code and identical arithmetic — and three different commitments about the data-generating process the analyst made before the data was touched.
- The chapter moves through What the statistician means by conditioning, What the epidemiologist means by adjusting for a confounder, What the ML engineer means by controlling for, All three are pointing at the same operation. What is it?, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

**Suggested titles:**
1. Three Words for the Same Problem
2. The Same Regression, Wearing Three Hats
3. What Your Vocabulary Already Decided

**TL;DR:** Conditioning, confounding, and controlling-for produce identical code and identical arithmetic — and three different commitments about the data-generating process the analyst made before the data was touched. The vocabulary is the assumption package; the assumption package is the analysis.

**Byline:** Nik Bear Brown

**Prerequisites:**
- Multivariable regression in Python or R, including the experience of adding a covariate and watching a coefficient change.
- Pearl's three rungs (association, intervention, counterfactual) from Chapter 1 — particularly the rung-1-to-rung-2 gap.
- Familiarity with at least one of: the statistics phrase "condition on X," the epidemiology phrase "adjust for the confounder X," the ML phrase "control for X as a covariate."
- One full A/B test cycle, observational or randomized, from design to readout.
- Comfort reading a regression summary table (coefficient, standard error, confidence interval).

**Learning objectives:**
- *Understand:* Translate a single causal claim across the statistician's, epidemiologist's, and ML engineer's registers without losing or smuggling content. (Bloom: Understand → Apply)
- *Analyze:* For a published claim in your own field, name what each of the three framings makes easy to see and what each makes easy to miss. (Bloom: Analyze)
- *Analyze:* Recognize when "controlling for more variables" is harmless, harmful, or required, by working backward from the question being asked to the structural commitment the vocabulary loaded. (Bloom: Analyze)
- *Evaluate:* Diagnose, in a real published controversy (the hormone-replacement-therapy reversal), where the disagreement lived in the data and where it lived in the vocabulary. (Bloom: Evaluate)

---

Three people walk into a room. They are looking at the same table. The table has three columns — *treatment*, *outcome*, and a covariate called *age*. The treatment is binary. The outcome is binary. There are roughly 27,000 rows. They are all trying to answer the same question: *does the treatment reduce the outcome*?

The first person is a statistician. She has the table open in R. She writes: "Let's condition on age in the regression — we want the within-age effect, since the marginal one looks confounded by the cohort imbalance." She fits a logistic regression with treatment and age as predictors. She reads the coefficient on treatment. It is negative. Treatment reduces the outcome.

The second person is an epidemiologist. He has a slightly different worry. He says: "Age is a confounder here. Older women are both more likely to be on the treatment and more likely to have the outcome. We need to adjust for it before we can read the effect as causal." He fits the exact same logistic regression. Same coefficient. Same standard error. He reports it the same way. The effect is protective.

The third person is an ML engineer. She has the table loaded as a pandas DataFrame. She says: "Age is a strong predictor — let me include it as a feature. If I leave it out, the model underperforms, and the treatment coefficient will pick up the variance." She fits the same logistic regression in scikit-learn. Same coefficient. Same standard error. She calls it a control variable. The effect is protective.

The three people are looking at the same coefficient. They reported the same number. They all said the treatment helps.

The treatment, in this case, was estrogen-plus-progestin hormone replacement therapy. The outcome was coronary heart disease. The table is roughly the structure of the Nurses' Health Study analyses that ran from the early 1990s onward.

Three years after the cohort study published the protective effect, the [Women's Health Initiative randomized trial](https://www.nejm.org/doi/full/10.1056/NEJMoa030808) reported the opposite. In the trial, the same treatment *raised* coronary heart disease risk, with a hazard ratio of 1.24 over 5.6 years and a hazard ratio of 1.81 in the first year. Healthy women on the trial arm had more heart attacks, not fewer.

The three analysts in the opening were not wrong about the arithmetic. The arithmetic was the same arithmetic the trial team did. The disagreement was not in the regression. It was in what each person *thought they were doing* when they ran the regression. Each one had committed, before the data was touched, to a different story about why age was in the model. And the three stories — *conditioning*, *confounding*, *controlling for* — looked like translations of each other. They are not translations. They are three different commitments wearing one set of clothes.

This chapter is about how three vocabularies can produce identical code and incompatible analyses. By the end, you should be able to read any one of them and translate it into the other two — and, more importantly, name what each translation forces you to make explicit.

---

## What the statistician means by *conditioning*

Start with conditioning, because it is the cleanest and the most modest of the three. A statistician says "condition on X" and means something specific. It is a statement about probability distributions.

Here is what is actually happening. You have a joint distribution P(T, Y, X) — treatment, outcome, covariate. The marginal effect, the thing you would compute without X in the picture, is the difference E[Y | T=1] − E[Y | T=0]. This is the answer to the question, "if I average over everyone, what's the gap between the treated group's outcome and the untreated group's outcome?" A perfectly well-formed statistical question. It has a sample analog. You can compute it on the back of an envelope.

Conditioning gives you something different. The conditional effect within stratum X=x is E[Y | T=1, X=x] − E[Y | T=0, X=x]. The statistician is asking, "*within* a fixed value of X, what's the gap?" This is also a well-formed statistical question. It also has a sample analog.

The statistician's commitment is small. She is not saying X causes anything. She is not saying X is on a path between T and Y. She is not saying the marginal effect is wrong. She is saying *the within-stratum effect is the quantity I am estimating*. That's it. If you press her — "why this estimand and not the marginal one?" — she will give you a reason that is usually about variance, or interpretability for a particular sub-population, or a structural assumption ("the marginal mixes apples and oranges"). But the word *condition* itself ships only a distributional claim. The distribution of (T, Y) given X = x. Nothing more.

This modesty is the statistician's gift and her trap. The gift: she can talk about conditional effects without committing to a causal model. The trap: a reader who hears "we conditioned on age" may *assume* the conditioning yielded a causal answer, because in a regression report it looks the same as adjustment. The word does not protest. It is not the statistician's job to protest. It is the reader's job to ask what the conditional estimate was supposed to mean.

Cochran's 1968 paper on [adjustment by subclassification](http://users.nber.org/~rdehejia/!@$AEM/Topic%2008%20Matching%20Introduction/readings/Cochran_1968_2528036.pdf) is where this register became technical. Cochran was working in the statistics tradition; he wanted to know how many subclasses you needed to remove bias from a comparison of two groups in an observational study. His famous result: for monotonic relations between the covariate and outcome, two subclasses remove about 64 percent of the bias, three remove about 79 percent, five remove about 90 percent. The paper is a beautiful piece of distributional analysis. It is also fundamentally agnostic about *why* X is in the analysis at all. Cochran assumes you've already decided. He gives you the arithmetic that follows.

That assumption — *you've already decided which X* — is the seam. Conditioning takes the X as given. It then asks: what does the conditional distribution look like, and how do my estimators behave inside it? It does not ask: should X be there? The word *condition* is honest about its own scope. The reader is the one who has to do the rest.

Notice what this register foregrounds. The within-stratum estimator's variance. The behavior of the regression as you add covariates. The trade-off between precision and the size of the effective sample. The mathematics of strata. All of this is real and useful. Now notice what it does not foreground. Whether X is upstream or downstream of T. Whether X is itself caused by T. Whether the conditional comparison answers the question the reader actually wanted answered. The vocabulary doesn't make these things visible because the vocabulary is not in that business.

Here's the trick — and I want you to feel it before we move on. The statistician's register is not wrong. It is *precise about a smaller question*. The "conditioning" word does not lie. It does not even hedge. It restricts itself to the part of the problem where its tools work, and it tells you nothing about the part where its tools don't. When a more ambitious question gets squeezed through this register, the register does not push back. It produces an estimate. The reader then has to know which question the estimate is the answer to.

That is the trap I want you to remember. Not "conditioning is bad." Conditioning is fine. *Conditioning is silent about whether it is the right thing to do.*

---

**Mid-chapter checkpoint** — three ungraded questions before we move on. Don't write them down. Just notice your answers.

1. If you "condition on age" in a logistic regression, are you claiming age causes the outcome? Are you claiming age is *not* caused by the treatment? Which assumptions does the word "condition" actually ship, and which does it leave up to you?
2. If two analysts run the same code and report the same coefficient — one calling X a "control" and one calling X a "confounder" — have they done the same analysis? Where is the difference, if there is one?
3. The WHI trial assigned women to the treatment randomly. The Nurses' Health Study observed who chose to take HRT. Both ran a regression of outcome on treatment with age as a covariate. Which one was *conditioning*, which one was *adjusting for confounding*, and which one was *controlling for*? Could the same regression be all three?

---

## What the epidemiologist means by *adjusting for a confounder*

Now slide the vocabulary one register to the side. The epidemiologist looks at the same regression and says: "We adjusted for age as a confounder." The word *confounder* is the shift.

Specify what it means before disputing it. *Confounder*, in the modern structural register, is not "a variable correlated with both treatment and outcome." That is the old Fisher-era list-based definition, and it is wrong in important cases. The modern definition, the one [VanderWeele and Shpitser](https://doi.org/10.1214/12-AOS1058) made canonical in 2013, is structural. A variable X is a confounder of the effect of T on Y when X is a common cause of T and Y — or, more precisely, when conditioning on X closes a back-door path between T and Y that would otherwise let association leak between them without any causal flow.

That is a mouthful. Translate it. The epidemiologist's word *confounder* makes three commitments at once, and you should see all three.

First commitment: there is a *direction* in the world. Some variables cause others. Age happens before HRT use; HRT use happens before the heart attack. The graph has arrows. The vocabulary refuses to be agnostic about which way they point.

Second commitment: the question being asked is causal. Not "what is the conditional mean of Y given T = 1 and X = x" but "what would the mean of Y be if we *set* T to 1." Pearl's notation for this is E[Y | do(T=1)] — the do is the intervention. The conditional is what you observe; the do is what you would impose. If the question is observational ("among the people who took HRT, who lived longer"), confounding is not a worry. If the question is interventional ("if we put a healthy 60-year-old woman on HRT, will she live longer"), confounding is the central worry.

Third commitment: there exists some adjustment set — some collection of variables you can condition on — that *closes the paths through which spurious association flows*. The epidemiologist's *adjust for X* is shorthand for "X is in the adjustment set that closes the back-door, and conditioning on it removes the bias the back-door was creating." The word presumes both that such a set exists and that you know what's in it.

[Hernán and Robins's *Causal Inference: What If*](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/) — the contemporary epidemiology canon, free online — devotes its first eight chapters to teasing these three commitments apart. The book's central insistence: you cannot tell whether your regression is "adjusting" or merely "conditioning" without specifying the causal structure first. The data does not contain the answer. You bring the answer to the data.

Miguel Hernán made this point sharper in a 2018 paper bluntly titled ["The C-Word"](https://pmc.ncbi.nlm.nih.gov/articles/PMC5888083/) in the *American Journal of Public Health*. The C-word is *causal*. Hernán's argument: epidemiologists routinely refuse to use the word "causal" in published analyses, even when the entire purpose of the analysis is to estimate a causal effect. They use "associated with" instead. The euphemism, he argues, makes the analysis worse — because the analyst can hide from the structural commitments the analysis is implicitly making. If you will not say *causal*, you will not say *confounder*, and if you will not say *confounder*, you will not draw the graph, and if you will not draw the graph, you cannot tell whether your adjustment is valid.

Hernán's piece is not about vocabulary alone. It is about vocabulary as a discipline-wide commitment device. The word forces the work.

That is the trade the epidemiology register makes. The word *confounder* is heavier than the word *condition*. It demands more before you can use it. It demands you know the direction of arrows. It demands you have a causal question. It demands you have a story about which paths exist between T and Y. In return, it gives you a vocabulary that does not let you get away with the analysis the data alone cannot support.

Watch what happens when this register is correctly applied to the HRT case. The epidemiologist asks: was age a confounder of HRT's effect on heart disease? Maybe. Age causes the heart disease (the older you are, the more likely you have one). Does age cause HRT use? Not directly, but it conditions who gets prescribed — younger post-menopausal women got HRT more readily in the era of the Nurses' Health Study, because the prescribers and the patients both thought the benefits were larger near menopause and the risks smaller. So age sits on a path from prescription-decision to outcome that does not run through any biological effect of HRT itself. Adjust for age and you partly close that path. But — and here is where the register gets sharp — adjusting for age alone does *not* close the more important path. The path from "is this patient healthy enough to want HRT and to have a doctor recommend it" to "is this patient healthy enough to survive the next decade." That path is closed only by adjusting for the *healthy-user* selection. And the healthy-user selection was not in the regression. It was not in the cohort study's table. It was a fact about which women chose to go on HRT and which did not, and no covariate available to the analyst captured it cleanly.

The vocabulary names this. *Confounding by indication* is the technical term for the case where the reason a patient was prescribed the treatment is itself a cause of the outcome. The Nurses' Health Study's protective HRT estimate is the textbook case of confounding by indication going un-adjusted. The trial — the WHI — broke the link between "wanting HRT" and "being put on HRT" by randomizing, and the protective effect vanished. (See [Manson et al. 2003](https://www.nejm.org/doi/full/10.1056/NEJMoa030808) for the trial result.)

The epidemiologist's word *confounder* makes this conversation possible. The conversation cannot happen without it. The statistician's *condition* and the ML engineer's *control* do not — by themselves — invite it.

Notice what the epidemiology register foregrounds. Causal direction. The existence of paths. The adjustment-set decision. Confounding by indication. Selection bias. The healthy-user effect. Time-varying treatment-confounder feedback. All of these terms come from a tradition that built its vocabulary around what goes wrong when you treat an observational analysis as if it were a randomized one.

Now notice what it can make easy to miss. The variance of the estimator. The behavior of the regression as the model grows. The interpretability of the conditional estimate for a specific sub-population. The trade-off between adjustment and effective sample size. These are not invisible to the epidemiologist, but they are not the first things her vocabulary names. The register foregrounds bias and structure. It backgrounds precision and computation.

Here's my reading. *Confounding* is the most demanding of the three vocabularies and the one most prone to a particular failure mode: assuming the back-door is closed when it isn't. The word is so committed to the causal story that an analyst who has named her confounders and adjusted for them can come to feel she has done the work. She has done some of the work. She has not done all of it. The vocabulary tells her, every time she uses it, what the work is. It does not check whether she did it.

---

## What the ML engineer means by *controlling for*

Now the third register. The ML engineer says "we controlled for age." The word *control* arrives from a different tradition — regression-as-prediction rather than regression-as-causal-estimation.

Here is what is actually happening when an ML engineer says *control for X*. She is including X in the feature set of a model whose objective is — by default — to minimize some loss on a prediction target. The loss is mean-squared-error or log-loss or AUC. The feature X is in the model because including it improves the loss. Or because she has a strong prior that X carries signal. Or because leaving it out causes the deployed model to fail on a distributional shift. The word *control* is doing feature-engineering work.

This register has its own internal logic, and it is good logic for its question. The question is: *given a new observation with features (T, X, ...), predict Y as accurately as possible*. If X is predictive, X belongs in the model. Whether X is upstream of T, downstream of T, a common cause, or a common effect — the prediction-objective doesn't care. What matters is conditional predictive performance. The information theorist's question: how much of the variance in Y can the features (T, X) account for, jointly, compared to T alone? If X adds information, X stays.

This is a perfectly coherent activity. It is not what the statistician means by conditioning, and it is *not at all* what the epidemiologist means by confounding adjustment. The ML engineer's register imports a feature-engineering claim: *X is a relevant predictor that improves the model*. That claim has nothing to say about causal direction, back-door paths, or adjustment sets. The vocabulary is silent on the structural questions because the vocabulary did not grow up in a tradition where structural questions were the point.

This is also where the trouble enters. Because the regression code is identical. Because the coefficient on T comes out the same number. Because the report sentence is one word away from each of the other two ("controlled for" vs. "adjusted for" vs. "conditioned on") — the ML engineer can hand a stakeholder a result that *sounds like* a causal estimate, and the stakeholder can read it that way, and the analyst may not be wrong by her own register's standards but the reader is being misled by a vocabulary mismatch.

I want to be careful here. The ML engineer is not stupid and is not lying. She is working in a vocabulary whose default objective is prediction. If you ask her, "is this a causal estimate?" — a careful ML engineer will say "no, this is the conditional expectation of Y given T and X, and it should be interpreted as such." A less careful one will say "it's the effect of T controlling for X" and call it a day. The vocabulary does not push her to distinguish. The vocabulary, in fact, makes the distinction quietly disappear.

This is the failure mode I want named. The ML register's most dangerous habit is *the more controls the better*. The intuition is: every variable that adds predictive information reduces bias on the treatment coefficient. The intuition is true if every variable is either a confounder or a noise term. It is *false* if some of those variables are colliders — variables that T and another cause of Y both feed into. Conditioning on a collider opens a path between T and Y that was closed before. It manufactures association where there was none. The collider problem will get a chapter of its own, several chapters from now. For today, register only this: the ML reflex *more controls is safer* is the precise opposite of the epidemiology reflex *only the confounders, please, and never the colliders*. The two reflexes are not synonymous and they do not point in the same direction.

There is a paper by Chernozhukov and co-authors called ["Double/Debiased Machine Learning"](https://doi.org/10.1111/ectj.12097) that has become widely used in industry. It uses ML methods twice — once to predict the treatment from covariates, once to predict the outcome from covariates — and combines the predictions in a way that yields a debiased estimate of the treatment effect when the covariates are a valid adjustment set. The paper is careful. The implementations are careful. The vocabulary in which the paper is summarized in tutorials and blog posts is often not careful: *DML controls for confounders using ML*. The summary suggests DML *solves* the identification problem. It does not. DML *refines the estimation* of the treatment effect given that you have already chosen a valid adjustment set. If you choose the wrong set — if you include a collider, if you omit a confounder, if you adjust for a mediator — DML produces a wrong answer with a beautiful standard error. The vocabulary masks this. The math does not.

Notice what the ML register foregrounds. Prediction. Feature engineering. Out-of-sample loss. Model complexity. Hyperparameter choices. Distributional robustness. The behavior of the estimator under regularization. The kinds of things a careful predictive modeling pipeline pays attention to.

Notice what it can make easy to miss. Whether the treatment coefficient has a causal interpretation. Whether adding a feature has reduced bias or introduced bias. Whether the analysis is answering an interventional question or an observational one. The structural reason X was added to the model in the first place.

Here is what I conclude. The ML register is not worse than the other two. It is *built for a different question*, and when its question is the question, it works beautifully. The harm comes when the question changes and the vocabulary does not. When the engineer who controls for X to predict Y is read as having adjusted for X to estimate the effect of T on Y — and the engineer does not protest the misreading because her vocabulary did not push her to notice the gap — the analysis breaks. The breakage is invisible from inside the register. That is what makes it dangerous, and that is what makes the chapter necessary.

---

## All three are pointing at the same operation. What is it?

So we have three words. They produce identical code. They produce identical coefficients. They commit the analyst to three different stories. What, mechanically, is the underlying operation?

The operation is this: *partition the data on X, compute the within-partition T–Y comparison, and combine the within-partition comparisons in some weighted way to produce a summary*. The weighting can be the proportions of the strata in the sample, in some target population, in some hypothetical intervention, or in the standardizing distribution of the analyst's choice. The arithmetic of the operation is the arithmetic. Whether the summary number you produce is the answer to a useful question depends entirely on what you wanted to know.

The statistician calls this *conditioning* because she is naming the partition-and-summarize step distributionally. The epidemiologist calls it *adjusting for a confounder* because she is naming the *reason* the partition was justified — X was on a back-door path, the partition closes the path, the summary therefore matches the do-question's answer. The ML engineer calls it *controlling for* because she is naming the partition's *effect on her predictive model* — X is a feature, the model improves, the residual variance in T's coefficient is the within-X effect of T on Y.

Three names for the same arithmetic. Three different commitments about why the arithmetic was performed. Three different ways the analysis can fail — and only one of the three vocabularies routinely makes the failure modes visible.

The structural picture, the one Chapter 3 will name properly, is this: variables in a problem have causal relationships among themselves. Some variables cause others. Some are caused by the treatment. Some are caused by the outcome. Some sit between treatment and outcome on the path the treatment uses to affect the outcome. The vocabulary you choose determines which of these structural facts your analysis has to commit to.

Conditioning says: *I am computing a within-X estimate. I am not committing to anything about how X relates structurally to T and Y.* The estimate is what it is. You interpret it.

Confounding adjustment says: *I am closing a back-door path from T to Y by including X in the adjustment. I am committing to a graph where X is on that path. If the graph is wrong, the adjustment is wrong.*

Controlling for says: *I am including X to improve the model's predictive performance. I am committing to a workflow that may not have asked whether X is causally appropriate to include.*

The first vocabulary is silent about structure. The second is loud about structure but can be wrong about structure. The third inherits a workflow that is structure-blind by design.

If you read a paper that says "controlled for X, Y, Z," you have not been told whether the adjustment set was chosen because of structural reasoning, predictive performance, or both. You have to ask. If you read "adjusted for confounders X, Y, Z," you have been told someone made a structural claim — and you can demand they defend it. If you read "conditioned on X, Y, Z," you have been told what was done arithmetically — and you have to do the structural reasoning yourself.

Each vocabulary makes one of these aspects easy. None makes all three easy.

This is the lesson of the chapter, and it is graded. The vocabulary does not matter when X is a clean confounder with no funny business — when X is a common cause of T and Y, when the graph is simple, when the adjustment set is uncontroversial. In that case, all three registers point at the same operation and produce the same correct answer. The vocabulary matters *exactly when X is structurally complicated* — when X is a collider, a mediator, a time-varying covariate, a healthy-user proxy. In those cases, the three vocabularies prescribe three different actions, and the data alone does not say which is correct. The structural commitment does. And the structural commitment lives outside the regression.

---

## The worked example: HRT and WHI

I want to do the hormone-replacement-therapy case end-to-end now, because it is the cleanest cross-vocabulary failure in the literature and because each of the three registers tells a different story about why the trial and the cohort disagreed. The chapter is not going to settle which story is correct. The post-hoc reconciliation is contested in detail and the literature still argues about it. The chapter's job is to show that the *shape* of the argument was determined by the vocabulary each analyst brought.

Set the scene. The [Nurses' Health Study](https://nurseshealthstudy.org/) followed a large cohort of female nurses starting in 1976. By the 1990s it had data on tens of thousands of post-menopausal women, some of whom took hormone replacement therapy, some of whom did not. Stampfer, Manson, and colleagues published a series of papers through the 1990s reporting that women on HRT had roughly 40 to 50 percent lower coronary heart disease incidence than non-users, after adjustment for cardiovascular risk factors. The result was widely cited. By the late 1990s, HRT was being prescribed in part for cardiovascular protection.

In 2002, the [Women's Health Initiative](https://www.nejm.org/doi/full/10.1056/NEJMoa030808) reported the result of a randomized trial of the same regimen — estrogen plus progestin — in roughly 16,000 generally healthy post-menopausal women. The trial was stopped early because the treatment arm had *more* cardiovascular events, not fewer. Manson and colleagues, writing in the *New England Journal of Medicine* in 2003, reported a hazard ratio of 1.24 for coronary heart disease over 5.6 years of follow-up, with the elevation concentrated in the first year (HR 1.81).

The cohort said HRT protected against heart disease. The trial said HRT caused heart disease. Same population (roughly), same treatment, same outcome, opposite answers.

How did each vocabulary tell this story?

**The epidemiologist's account.** The Nurses' Health Study suffered from confounding by indication and the healthy-user effect. Women who took HRT in the 1980s and 1990s were, on average, healthier than non-users at baseline — better educated, more likely to have regular medical care, lower BMI, less likely to smoke, more attentive to their own cardiovascular risk. The decision to take HRT was itself a marker of being the kind of patient whose cardiovascular outcomes would be better regardless of HRT. The regression in the cohort adjusted for *measured* baseline covariates. It could not adjust for *unmeasured* healthy-user status. The back-door path from "healthy person" to "good cardiovascular outcome" was not closed. The protective effect was, in the structural reading, the unblocked back-door leaking from baseline health into the treatment coefficient. Randomization in the WHI severed the back-door because assignment to HRT was unrelated to baseline health. The trial's null-or-harmful effect was the unbiased one.

In this telling, the cohort study was not wrong about its arithmetic. It was wrong about its identifying assumptions. The vocabulary that makes this point sayable is the epidemiology register — *confounding by indication*, *healthy-user effect*, *back-door path*. None of these terms are part of the statistician's vocabulary or the ML engineer's vocabulary in the same way.

**The statistician's account.** The cohort's regression conditioned on age, BMI, smoking status, family history, exercise, and several other covariates. The within-stratum estimator behaved well. The conditional distribution of outcomes given (treatment, covariates) had the protective coefficient as its sample analog. The conditional estimate was *what it was*. The disagreement with the WHI was not about the conditional estimate; it was about whether the conditional estimate answered the question the field thought it answered. The statistician could be asked, "is the conditional estimate causally interpretable here?" and a careful one would say no — the assumptions required for causal interpretation are not vouched for by the conditioning procedure itself. In this telling, the cohort estimate was a *correct conditional estimate of an irrelevant quantity*. The statistician's register did not protest because it does not, on its own, protest. The interpretation gap was on the reader.

**The ML engineer's account.** If we re-imagine the Nurses' Health Study as a 1990s ML pipeline: take the covariates, predict CHD from (treatment, age, BMI, smoking, family history, exercise). Use cross-validated regularization. Report the partial effect of treatment on CHD. Including more features improves predictive performance — which an ML engineer would treat as evidence the model is better. Add as many features as the data supports. The estimate of the treatment coefficient gets more precise as the features pile up. By every standard predictive-modeling metric, the model is good. The treatment coefficient is reproducible across folds. The standard error is small. The result is robust. And the result is wrong, in the WHI's terms, because no amount of conditioning on observed covariates closed the *unobserved* healthy-user path. The ML register did not flag this because the register did not have language for what was missing. The features were not insufficient by any predictive criterion. They were insufficient by a *structural* criterion that the register did not know to apply.

The three accounts are not in conflict about the arithmetic. They are in conflict about which kind of mistake was made. *Confounding by indication* says the mistake was structural. *A correctly computed conditional estimate of an irrelevant quantity* says the mistake was in the question, not the analysis. *Insufficient features for a causal interpretation the ML pipeline did not commit to* says the mistake was a category error — the analysis was solving a prediction problem; the world was asking a causal question.

Three vocabularies. Three diagnoses. Same data. Same arithmetic.

There is a footnote to the WHI story that you should hold lightly. A subsequent literature has argued that the cohort and the trial may not have been answering quite the same question — the women in the cohort were typically younger and started HRT closer to menopause, while WHI enrolled an older average population starting HRT further from menopause. Some authors have argued for a "timing hypothesis": HRT initiated early may genuinely be protective, while HRT initiated late may be harmful, and the two studies were comparing different interventions. This complication is real and I am not equipped to settle it. The point for our chapter is that the *initial* disagreement — protective in cohort, harmful in trial — was structured by the vocabularies each side brought, and the post-hoc reconciliation has continued to be structured by them.

What I conclude from the case is narrow. The same regression, on (close to) the same population, with similar covariates, was correctly described in three vocabularies and produced three different framings of what the field had learned. The vocabulary did not just label the analysis. The vocabulary determined what the analysis was *for*. And when the trial arrived with the answer to the interventional question, the cohort's conditional answer did not gracefully revise — it had to be *re-interpreted* in the vocabulary the cohort had not used, the vocabulary of *confounding by indication*, before the lesson could be absorbed.

That is the chapter's claim, made specific. The vocabulary is not a translation. It is a commitment. The commitment is made before the data is touched. And the regression cannot tell you which commitment you made — only the vocabulary can.

---

## Where this leaves us

Walk back through what you can do now that you could not do at the top of the chapter.

You can read a published analysis that says "we controlled for age, BMI, and exposure" and translate it, in your head, into both the statistician's and the epidemiologist's registers. You can name what the original register left implicit and what each translation forces explicit. You can ask the analyst — or yourself — which question the analysis is supposed to answer, and whether the chosen vocabulary's assumption package matches the question.

You can identify the moments when the choice of vocabulary will matter. They are the moments when the covariate is structurally complicated — when X might be a collider, a mediator, or an effect of the treatment rather than a cause of it. In those moments, the three vocabularies do not produce the same arithmetic and the three vocabularies prescribe different actions. The work of the analyst is to know which structural fact applies; the data alone will not say.

You can spot the failure mode that comes from each register. The statistician's *condition* is silent about structure and can mislead by omission. The epidemiologist's *confounder* commits to a structure that may be wrong and can mislead by mis-specification. The ML engineer's *control for* commits to a predictive workflow that can mislead by category error — answering a prediction question when an intervention question was asked.

You can read the HRT-WHI case as a case study in vocabulary-as-commitment, and you can name where the disagreement lived. It lived in what each side thought their regression was doing.

What you cannot yet do — and this is the bridge to the next chapter — is express any of these commitments in a formal language. The vocabularies are English, and English is not where the commitments need to live. They need to live somewhere precise enough that a fellow analyst, or you in six months, or a colleague who does not share your training, can read the commitment off the page without you in the room to explain it.

What we need is a map. A picture in which every arrow is a claim about causation, every missing arrow is a claim that no direct cause exists, and every variable is a node whose role — confounder, mediator, collider — is determined by where it sits in the picture rather than by which word the analyst chose to use.

If the vocabulary is not neutral, the question is: what formal language is?

That is the next chapter.

---

## Exercises

**Warm-up:**

1. *(Apply)* Take this sentence from a published clinical paper: *"After controlling for age, sex, and baseline glucose, the treatment was associated with a 0.8 percentage-point reduction in HbA1c."* Rewrite the sentence in the statistician's register (one sentence) and in the epidemiologist's register (one sentence). For each rewrite, name one assumption the original sentence left implicit that your rewrite has now made visible.

2. *(Apply)* You are given the abstract of an observational study claiming a treatment effect. The abstract uses the phrase *"controlling for the relevant covariates."* Which of the three vocabularies does this phrase come from? What single question would you ask the authors to determine whether the analysis is causally interpretable?

**Application (Part A — the field's claims):**

3. *(Analyze)* Read the abstract and methods section of [Manson et al. 2003 in *NEJM*](https://www.nejm.org/doi/full/10.1056/NEJMoa030808). Then read the abstract and methods of one of the Nurses' Health Study's HRT papers (Stampfer et al. is a starting point; the Nurses' Health Study publications list is at https://nurseshealthstudy.org/publications). Without resolving which study is "right," name (a) the register each paper writes in, (b) the one structural commitment each register made implicit, and (c) the move each paper *would have had to make* to write the same analysis in the other paper's register.

**Application (Part B — your own field):**

4. *(Analyze)* Pick a causal claim from a paper or product report in your own subfield. Rewrite the claim three times — once in each vocabulary. For each of the three rewrites, name one specific question about the data-generating process that the chosen vocabulary makes you ask, and one question it lets you avoid asking. Submit the three rewrites and the six questions. Be precise about where the questions diverge.

**Synthesis:**

5. *(Analyze)* In Chapter 1, we drew the distinction between a model that predicts a pattern and a model that answers an intervention question. Connect that distinction to the three vocabularies in this chapter. Which vocabulary lives most naturally in rung-1 work? Which presupposes rung-2 work? Which is silent about the rung distinction, and why is the silence itself a problem?

**Challenge:**

6. *(Evaluate)* Pick one of the following: (a) a recent observational study claiming a benefit from a popular nutrition intervention, (b) a recent ML paper claiming a causal interpretation of feature importances, or (c) a recent A/B test writeup that adjusted for covariates. Identify (i) the vocabulary the paper writes in, (ii) the structural commitment the vocabulary loaded silently, and (iii) the specific failure mode the vocabulary makes most likely. Argue, in two paragraphs, whether the paper's conclusion would survive a translation into a different register. Cite a primary source.

---

## LLM exercise

Use this prompt with Claude or ChatGPT. Paste it verbatim, replacing the bracketed claim with one from your own reading.

```
You are helping me check whether a causal claim is being made in a vocabulary
that matches the question it is answering.

Here is a claim from a recent paper or article:

[PASTE THE CLAIM HERE — keep it to 2–4 sentences. Include the regression
covariates if the paper named them.]

Do three things, in order.

1. Identify which of the three vocabularies the claim is written in:
   statistician's "conditioning," epidemiologist's "confounding/adjusting,"
   or ML engineer's "controlling for." Quote the specific words that
   identified the register for you.

2. Rewrite the claim in each of the other two vocabularies. Each rewrite
   should be 1–3 sentences. Do not use the original vocabulary's keywords
   in either rewrite.

3. For each of the three versions (the original and the two rewrites),
   name one assumption about the data-generating process that the vocabulary
   makes implicit. Then name one assumption it forces the analyst to state
   explicitly. Be specific — name a variable, a path, or a structural fact,
   not a category.

End by stating, in one sentence, whether the original vocabulary matched
the question the paper appears to be answering. If it did not match, name
the mismatch.
```

*What good output looks like:* The translations preserve the empirical content. The implicit-assumption naming is specific — not "causal direction" but "the model assumes age is upstream of treatment." The final sentence takes a position and supports it from the translations.

---

## AI Use Disclosure (Part A standard form)

In this exercise I used [tool name and version, e.g., Claude 4.7 Opus, May 2026] to translate a causal claim across three registers. I provided the original claim and verified each translation against the source paper's methods section; I did not accept any rewrite without checking that it preserved the empirical content. The LLM did not have access to the source paper's full text; I supplied the relevant passages.

**Part B bonus criterion:** Name one place where the LLM's translation introduced a structural commitment the original did not make (e.g., a directional claim the original was agnostic about, a variable role the original did not specify). Treat this as evidence of how the model fills in absent structure — useful data about the model, not just about your claim.

---

## Key terms

- *Conditioning on X*: A statistical operation. Restricting attention to the joint distribution of T and Y at a fixed value of X, or equivalently averaging the T–Y comparison over the strata of X. Says nothing about why X is in the analysis or whether the resulting estimate is causally interpretable.
- *Adjusting for a confounder*: An epidemiology phrase. Conditioning on X with the explicit commitment that X is a common cause of T and Y, or otherwise sits on a back-door path that the conditioning closes. Says: I have a causal question, and X is in the adjustment set that makes the estimate identifiable.
- *Controlling for X*: An ML / regression-as-prediction phrase. Including X as a feature in a model whose objective is, by default, predictive. Says: X improves the model. Says nothing structural about why.
- *Confounding by indication*: The structural situation where the reason a unit was assigned to (or selected for) a treatment is itself a cause of the outcome. The canonical example outside this chapter: physicians prescribe a drug to sicker patients, so the treated group has worse outcomes for reasons unrelated to the drug.
- *Healthy-user effect*: A specific kind of confounding by indication in observational pharmacoepidemiology. Patients who take a treatment of unproven benefit (vitamins, HRT in the 1990s, statins for primary prevention in some populations) tend to be healthier than non-users in unmeasured ways.
- *Back-door path*: A path between T and Y in the causal graph that does not flow through any descendant of T (it goes "out the back" of T into the graph and around to Y). Back-door paths transmit non-causal association unless they are blocked.
- *Adjustment set*: A set of variables that, when conditioned on, closes all back-door paths between T and Y. Whether a given set is an adjustment set depends on the causal structure, not on the data.

---

## Further reading

- Pearl, J. (1995). ["Causal Diagrams for Empirical Research."](https://doi.org/10.1093/biomet/82.4.669) *Biometrika* 82(4), 669–688. The paper that made the unifying graph-theoretic treatment available to statisticians. Skim for the do-operator definition and the back-door criterion statement; both will be load-bearing for Chapter 3.
- Greenland, S., Pearl, J., & Robins, J. M. (1999). ["Causal Diagrams for Epidemiologic Research."](https://www.jstor.org/stable/3702180) *Epidemiology* 10(1), 37–48. The translation of Pearl's framework into the epidemiology register. The most useful single paper for seeing how the epidemiology vocabulary maps to the structural definitions.
- VanderWeele, T. J., & Shpitser, I. (2013). ["On the definition of a confounder."](https://doi.org/10.1214/12-AOS1058) *Annals of Statistics* 41(1), 196–220. Resolves competing definitions of "confounder" under a single structural definition. Read for the demonstration that the older associational definition fails in the collider case.
- Hernán, M. A. (2018). ["The C-Word: Scientific Euphemisms Do Not Improve Causal Inference From Observational Data."](https://pmc.ncbi.nlm.nih.gov/articles/PMC5888083/) *AJPH* 108(5). Short and bracing. The argument that refusing to say "causal" makes causal analysis worse, not more cautious.
- Hernán, M. A., & Robins, J. M. (2020). *Causal Inference: What If*. Free PDF at https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/. The contemporary epidemiology canon. Chapters 7 and 8 are the load-bearing chapters for everything we did today on confounding and adjustment.

---

**What would change my mind:** A demonstration that careful practitioners in any one of the three traditions, when given a structurally complicated covariate (a collider or mediator), reliably reach the same analytical decision as careful practitioners in the other two — that the vocabulary is just packaging and the underlying judgment is the same. The evidence I have seen (and my own consulting work) points the other way, but I have not run a controlled study.

**Still puzzling:** Why the ML community has not, by 2026, absorbed the structural-definition shift the epidemiology community absorbed in the early 2000s. The math has been settled for a decade. The vocabulary has not moved. I have hypotheses (different incentive structures, different journal cultures, different training pipelines) but no clean answer.

---

**Tags:** causal-inference, vocabulary, confounding, HRT-WHI, identification-layer

---

**Draft flags:**
- *Voice anchor:* No prior chapter drafts in this book exist beyond placeholders; root `style/` was not located. Drafted to the Feynman voice rules in CLAUDE.md and the pantry notes' voice guidance. Flag `voice-unanchored` per CLAUDE.md §6.
- *Verification status:* All inline citations to peer-reviewed work verified via web search (Manson 2003 *NEJM*, Cochran 1968 *Biometrics*, Hernán 2018 *AJPH*, VanderWeele & Shpitser 2013 *Annals of Statistics*, Pearl 1995 *Biometrika*, Greenland-Pearl-Robins 1999 *Epidemiology*, Chernozhukov 2018 *Econometrics Journal*). Hernán-Robins 2020 textbook free PDF link verified against pantry.
- *Hedged claim:* The Nurses' Health Study HRT effect size ("roughly 40 to 50 percent lower coronary heart disease incidence") is in the right range per Stampfer's NHS papers but not verified against a specific table; the chapter's argument does not depend on the exact number. [verify-against-Stampfer-NHS-table]
- *Hedged claim:* The "timing hypothesis" footnote in the HRT section is treated as a real but unresolved literature; the chapter does not adjudicate.
- *Open question for book.md:* book.md is currently a template (One-Sentence Pitch, Argument, Gap, Reader all empty). The chapter writes to the pantry's working thesis ("domain judgment is irreducible at the identification layer; causal AI tools do not supply it"). Nik should consider filling in book.md before subsequent drafts so cross-chapter consistency tightens.
