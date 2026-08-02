# Chapter 8: Counterfactuals and Mediation


## TL;DR

- "Had Cleopatra's nose been shorter, the whole face of the world would have changed.
- The chapter moves through What a counterfactual is, Potential outcomes, Computing counterfactuals from a causal model, A worked example, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

"Had Cleopatra's nose been shorter, the whole face of the world would have changed."

So wrote Blaise Pascal in 1669, in the *Pensées*. The claim is a counterfactual — a statement about what would have happened in a world that did not happen. Pascal is asserting that Cleopatra's appearance causally affected the course of history, by way of the judgments of Julius Caesar and Mark Antony, and that a slightly different nose would have produced a substantially different world.

The claim is un-testable, of course. We have only one Cleopatra and one historical record. We cannot re-run the first century BCE with a different-nosed queen of Egypt to see what happens. The counterfactual world Pascal is invoking is, by definition, not available for inspection.

And yet we reason about counterfactuals constantly. Legal systems ask whether a defendant's action was a but-for cause of an injury — whether the injury would have occurred but for the defendant's negligence. Medical decisions for individual patients ask what would happen under different treatment choices. Policy analysis asks whether an outcome would have been different under a different policy. Historians ask what would have happened if a battle had gone differently. Parents ask whether they should have said something different to their teenagers. Counterfactual reasoning is as natural as breathing, and it is also the hardest kind of causal reasoning to do rigorously.

This chapter is about how to do it. We will move up the ladder of causation to the third rung — the rung of counterfactuals — and introduce the tools that make counterfactual reasoning possible. We will see how counterfactuals are defined, how they can be computed from a causal model, and how the specific case of *mediation analysis* — the decomposition of a causal effect into direct and indirect pathways — is really a counterfactual question in disguise.

This is the most abstract chapter in the book. The material is genuinely hard. But the rewards are substantial: counterfactual methods let us ask questions that no other causal framework can answer.

## What a counterfactual is

A counterfactual is a statement of the form "if X had been different, Y would have been different." The "if" specifies a hypothetical alteration to the factual world. The "would" asserts a consequence under that alteration.

Formally, we can write a counterfactual as Y_x, pronounced "Y under x." This denotes the value of Y that would have been observed if X had been set to x. The subscript indicates the counterfactual intervention; the capital letter remains the random variable.

To give a concrete example. Suppose we are studying a patient, Joe, who took aspirin and whose headache went away. The factual observation is (X = aspirin, Y = no headache). The counterfactual Y_{no aspirin} is the value Y would have taken if Joe had not taken aspirin. This value is unobserved — we cannot see Joe's headache in a world where he did not take the drug. But it is, nonetheless, a well-defined quantity. If Joe's headache would have gone away anyway, then Y_{no aspirin} = "no headache." If it would have persisted, then Y_{no aspirin} = "headache."

The counterfactual effect of aspirin on Joe is the contrast Y_{aspirin} - Y_{no aspirin}. If this contrast is non-zero, aspirin had a causal effect on Joe. This is different from the average causal effect in a population — it is the effect in Joe, in this specific instance.

Counterfactuals live on the third rung of the ladder of causation. They are about what would have happened, not just what does happen or what happens if we intervene. The distinction matters because intervention questions (rung two) can, in principle, be answered by running an experiment — give some people the drug, give others placebo, measure the difference. Counterfactual questions (rung three) cannot be answered by experiment even in principle, because they are about the outcome in a particular individual under a hypothetical alternative, and we cannot run both the factual and counterfactual experiments on the same individual.

This is what Judea Pearl calls the *fundamental problem of causal inference*: for any individual, we observe either the factual outcome or one of the counterfactual outcomes, never both. The factual outcome is what happened; the counterfactual outcome is what would have happened. They are different slices of reality, and we see only one at a time.

Counterfactuals are nevertheless tractable. Given a causal model, we can compute them. Given observed data and a model, we can estimate them. The key is that while we cannot observe both factual and counterfactual outcomes in the same individual, we can, under appropriate assumptions, use the factual outcomes of many individuals to learn something about the counterfactual outcomes of specific individuals. The rest of this chapter is about how.

## Potential outcomes

The standard framework for reasoning about counterfactuals in modern statistics is called *potential outcomes*. It was introduced by Jerzy Neyman in 1923 for analyzing agricultural experiments, and extended and popularized by Donald Rubin beginning in the 1970s. The framework is sometimes called the *Neyman-Rubin causal model*, or the *Rubin causal model*.

The core idea is to associate each individual with a vector of potential outcomes, one for each possible treatment. If there are two treatments (treated and control), each individual has two potential outcomes: Y(1) and Y(0). If Joe is treated, we observe Y(1) for Joe; we do not observe Y(0). If Jane is not treated, we observe Y(0) for Jane; we do not observe Y(1).

The causal effect of treatment on individual i is Y_i(1) - Y_i(0). This is the individual-level causal effect. It is almost never observable, because we only see one of the two potential outcomes for any individual.

But we can estimate averages of these individual-level effects under various conditions. The *average treatment effect* (ATE) is E[Y(1) - Y(0)], averaged over the full population. The *average treatment effect on the treated* (ATT) is E[Y(1) - Y(0) | T = 1], averaged over the subpopulation that actually received treatment. These are population-level quantities defined in terms of counterfactuals, and under the assumptions of the various methods we've seen in previous chapters, they can be estimated from data.

The potential outcomes framework gives a language for stating causal assumptions precisely. The *ignorability assumption*, for instance, says that Y(1) and Y(0) are independent of T conditional on the measured covariates X. In plain English: once we condition on the right covariates, treatment assignment is as-good-as-random with respect to potential outcomes. This is the formal statement of the back-door criterion from Chapter 3, expressed in potential-outcomes notation.

The framework also gives a clean way to define different types of causal effects. Direct effects, indirect effects, effects on specific subpopulations, effects under specific conditions — all can be expressed as functions of potential outcomes. This flexibility is one reason potential outcomes has become the dominant framework in statistics and much of social science.

The framework has limitations. It is awkward for reasoning about *mechanisms* — how the treatment produces its effect — because potential outcomes focuses on outcomes under different treatments, not on the pathways through which treatments work. For mechanism questions, structural causal models and causal diagrams are often more natural. But as a foundation for counterfactual reasoning in general, potential outcomes is a powerful and widely used tool.

## Computing counterfactuals from a causal model

How do we actually compute counterfactuals? The answer, in general, is: with a structural causal model.

A *structural causal model* (SCM) specifies, for each variable in the system, a function that determines its value from the values of other variables. If A causes B, the SCM contains a function B = f(A, U), where U represents everything else that affects B (unobserved noise, in effect).

The functions in an SCM encode the mechanisms by which variables affect each other. If we want to know what B would have been under a counterfactual value of A, we can plug that value into the function.

This is not trivial in the general case, because other variables besides A may also affect B. To compute a counterfactual, we need to know or model the other factors too. The procedure for computing counterfactuals from an SCM has three steps:

**Step 1: Abduction.** Use the observed data to infer the values of the unobserved factors (U) for the individual or population of interest. This is where the factual observations enter the computation — we use what we know about the individual to pin down the values of the noise variables that, combined with the factual treatments, produced the observed outcomes.

**Step 2: Action.** Modify the SCM to reflect the counterfactual intervention. If we are asking what would have happened under a different value of A, we replace the equation that determines A with an assignment to the counterfactual value.

**Step 3: Prediction.** Using the modified SCM and the inferred values of U from step 1, compute the counterfactual outcome.

This three-step procedure — abduction, action, prediction — is the general method for computing counterfactuals from a causal model. It applies to individual-level counterfactuals ("what would Joe's outcome have been?") and to population-level counterfactuals ("what would the average outcome have been if everyone had been treated?"). The computational details vary, but the conceptual structure is the same.

Let's make this concrete with a simple example.

## A worked example

Suppose we have a simple causal model with three variables: a treatment T (binary), a mediator M (continuous), and an outcome Y (continuous). The structural equations are:

M = α·T + U_M  
Y = β·M + γ·T + U_Y

The first equation says that M is determined by T plus a noise term U_M. The second says Y is determined by M and T plus a noise term U_Y. The coefficients α, β, γ represent the causal relationships: α is the effect of T on M, β is the effect of M on Y (holding T fixed), γ is the direct effect of T on Y (not through M).

For concreteness, suppose α = 2, β = 3, γ = 1. These are the true parameters of the model.

Now consider a specific individual, i, for whom we observe T_i = 1, M_i = 5, Y_i = 17. The individual took the treatment, has a mediator value of 5, and has an outcome of 17.

**Abduction.** We use the observed data to compute the individual's noise terms. From the first equation: M_i = 2·T_i + U_{M,i}, so 5 = 2·1 + U_{M,i}, so U_{M,i} = 3. From the second equation: Y_i = 3·M_i + 1·T_i + U_{Y,i}, so 17 = 3·5 + 1·1 + U_{Y,i}, so U_{Y,i} = 1. These are the individual-specific noise values that, combined with T_i = 1 and the true parameters, produced the observed M_i and Y_i.

**Action.** Now consider the counterfactual: what would Y have been if T had been 0 instead of 1? We modify the SCM by setting T = 0.

**Prediction.** Using the modified SCM with T = 0 and the inferred noise values (U_{M,i} = 3, U_{Y,i} = 1), compute the counterfactual values:

M_i(T=0) = 2·0 + 3 = 3  
Y_i(T=0) = 3·3 + 1·0 + 1 = 10

So the counterfactual outcome for individual i under T = 0 is Y_i(T=0) = 10. The individual would have had outcome 10 instead of 17 if they had not been treated. The individual-level causal effect of treatment for individual i is Y_i(1) - Y_i(0) = 17 - 10 = 7.

This computation works because we had a fully specified causal model and complete observation of the individual. In real applications, we typically have to estimate the parameters from data, and we often cannot pin down the individual-specific noise values exactly. But the logic of the computation is the same: infer what we can about the individual, modify the model for the counterfactual, compute the result.

## Individual vs. population counterfactuals

A population-level counterfactual is an average of many individual-level counterfactuals. If we want to know the average outcome in the population under a counterfactual treatment, we can think of it as the average of the individual outcomes that would have obtained if each individual had been given that treatment.

Under the ignorability assumption — that treatment is as-good-as-random given covariates — population-level counterfactuals reduce to observable quantities. The average counterfactual outcome E[Y(1)] equals the average outcome among the treated (adjusted for any imbalances in covariates). This is why matching, weighting, and other back-door adjustment methods can estimate causal effects. They estimate population-level counterfactuals by exploiting ignorability.

Individual-level counterfactuals are harder. They require more assumptions and more model structure. You can compute them given a fully specified causal model, but the answer depends on the assumptions built into the model, and different models can produce different counterfactual answers from the same data.

This is why individual-level counterfactual questions — "would Joe's headache have gone away without aspirin?" — are not usually the focus of applied causal inference. They are scientifically meaningful but methodologically fragile. Most of the methods in this book focus on population-level quantities.

Some important applications do require individual counterfactuals: legal responsibility ("was the defendant's action a but-for cause of this specific injury?"), medical decision-making for individual patients ("will this treatment help this patient?"), and increasingly, algorithmic fairness ("would this individual have received a different decision from the algorithm if their race had been different?"). In these applications, the methods of structural causal modeling become essential. The analyst cannot fall back on the simpler tools of matching or weighting — those estimate averages, not individual effects.

## Mediation: the search for mechanisms

Having introduced counterfactuals, we can now turn to the specific and important case of *mediation analysis*.

Mediation is the study of mechanisms. When we know that X causes Y, we often want to know *how* X causes Y. Does it work through one particular intermediate variable? Through several? Through none that we can identify?

Mediation questions are ubiquitous in science. Smoking causes lung cancer — but how? Through the tar? Through nicotine's effects on the immune system? Through some other mechanism? Exercise reduces heart disease — but is it because exercise lowers blood pressure, because it reduces cholesterol, because it changes body composition, or because of direct cardiovascular training effects? An educational intervention improves student outcomes — but is it because it increases attendance, because it improves teacher quality, or because it boosts student confidence?

Answering these questions matters practically. If smoking causes cancer only through tar, then tar-reduction measures (filters, lower-tar cigarettes) should be effective preventive strategies. If smoking causes cancer through multiple mechanisms, filters may not help. If exercise prevents heart disease mainly through blood pressure, then medications that lower blood pressure should be comparably effective to exercise. If exercise works through many mechanisms, pharmaceutical substitution is less likely to fully replicate its benefits.

Mediation analysis is the formal study of how a treatment's effect decomposes into components flowing through different pathways.

## The naive approach and why it fails

For decades, applied researchers used a simple approach to mediation analysis, attributed to Baron and Kenny in a 1986 paper. The approach:

1. Regress the outcome Y on the treatment T. The coefficient on T estimates the *total effect* of T on Y.
2. Regress the mediator M on the treatment T. If T predicts M, then T affects M.
3. Regress Y on both T and M. The coefficient on T in this regression estimates the *direct effect* of T on Y, controlling for M. The coefficient on M estimates the effect of M on Y, controlling for T.
4. The *indirect effect* of T on Y (through M) is the total effect minus the direct effect, or equivalently, the product of the T→M coefficient (from step 2) and the M→Y coefficient (from step 3).

This approach is intuitive and mechanical. It was used in tens of thousands of published papers in psychology, sociology, education, public health, and management.

It is also wrong, in important situations.

The Baron-Kenny approach assumes a specific simple structure: a linear causal relationship from T to Y, with M as a single mediator, no interaction between T and M, and no confounding of the M-Y relationship (other than T itself). When all these conditions hold, the approach gives the right answer. When any of them fails — interactions between T and M, non-linear relationships, confounding of M-Y by other variables — the approach gives wrong answers that can be substantially biased.

The most insidious problem is confounding of the mediator-outcome relationship. Even if the treatment T is randomized, the mediator M is typically not randomized. The relationship between M and Y can be confounded by other variables that affect both M and Y. In a Baron-Kenny analysis, this confounding contaminates the estimate of the direct effect, leading to biased decomposition of the total effect.

The problem was recognized gradually through the 1990s and 2000s. A better framework emerged, rooted in counterfactual reasoning. This framework, developed largely by Robins, Greenland, VanderWeele, and Pearl, recasts mediation as a counterfactual question and provides conditions under which the components can be rigorously identified.

## The counterfactual formulation of mediation

The counterfactual formulation starts by defining what we actually mean by direct and indirect effects.

Consider a treatment T, a mediator M, and an outcome Y. We want to decompose the total effect of T on Y into direct and indirect components.

The *natural direct effect* (NDE) is defined as: the change in Y we would observe if we changed T from control to treated, while holding M fixed at the value it would have taken under the control condition. Symbolically: NDE = E[Y(T=1, M=M(0))] - E[Y(T=0, M=M(0))], where M(0) is the counterfactual value of M under T=0.

In plain English: the NDE is the effect of T on Y that doesn't go through M. We counterfactually freeze M at its "without treatment" value and ask what the effect of T is.

The *natural indirect effect* (NIE) is: the change in Y we would observe if we held T fixed at the treated value, while changing M from the value it would have taken under control to the value it would have taken under treatment. Symbolically: NIE = E[Y(T=1, M=M(1))] - E[Y(T=1, M=M(0))].

In plain English: the NIE is the effect of T on Y that goes through M. We fix T at treated and change M from its "without treatment" value to its "with treatment" value, asking what the effect on Y is.

These definitions involve nested counterfactuals — quantities like Y(T=1, M=M(0)) refer to outcomes under multiple counterfactual interventions. The quantity Y(T=1, M=M(0)) is: what would Y be if T were set to 1 and M were set to the value M would have taken under T=0? This is a deeply counterfactual construct. It involves imagining a world where the treatment is given but the mediator is not affected by it.

The total effect decomposes as: Total Effect = NDE + NIE. The total effect of T on Y is the sum of the direct effect (not through M) and the indirect effect (through M). This decomposition holds in general, for any causal structure, under appropriate assumptions.

## The mediation formula

Pearl showed that the natural direct and indirect effects can be identified from observable data under specific assumptions. The resulting formulas are called the *mediation formulas*.

For the NDE:

NDE = ∑_m [E(Y | T=1, M=m) - E(Y | T=0, M=m)] · P(M=m | T=0)

For the NIE:

NIE = ∑_m E(Y | T=0, M=m) · [P(M=m | T=1) - P(M=m | T=0)]

These are summations over the possible values of M, weighted in specific ways. They look daunting, but they have clear interpretations. The NDE averages the direct effect of T on Y (computed at each value of M) over the distribution of M that would obtain under T=0. The NIE averages the "what if the mediator distribution were shifted?" effect over the distribution of Y given M and control treatment.

The mediation formulas can be computed from observational data under four assumptions:

1. **No unmeasured T-Y confounding.** The effect of T on Y is not confounded by unmeasured variables (conditional on observed covariates).
2. **No unmeasured M-Y confounding.** The effect of M on Y is not confounded by unmeasured variables (conditional on observed covariates including T).
3. **No unmeasured T-M confounding.** The effect of T on M is not confounded by unmeasured variables (conditional on observed covariates).
4. **No effects of T on M-Y confounders.** The treatment does not affect variables that confound the M-Y relationship.

The fourth assumption is the subtle one. It rules out a specific structure: T affects some variable W, and W confounds the M-Y relationship. If this structure exists, the mediation formulas don't identify the natural effects.

These assumptions are strong. They require no unmeasured confounding at multiple places in the causal diagram, which is a lot to ask. The assumptions are also often violated in practice, especially in observational studies.

The upshot: mediation analysis is harder than Baron-Kenny suggested. The Baron-Kenny approach hides this difficulty by making implicit assumptions. The counterfactual framework makes the assumptions explicit, which is honest but also uncomfortable — applied researchers often find that their mediation questions cannot be answered under the available assumptions.

## When mediation analysis works

Mediation analysis can produce valid results when several conditions are met:

**The treatment is randomized.** This handles the first assumption automatically. In an RCT, treatment is not confounded with anything, so T-Y and T-M confounding are eliminated. The remaining concerns are M-Y confounding and the "no T-effects on confounders" condition.

**The mediator-outcome relationship is well-understood.** If we have strong reasons to believe that M-Y confounders are limited and measurable, we can adjust for them and estimate mediation reliably. This is more plausible in laboratory sciences with clear mechanisms than in behavioral or social research with many unmeasured influences.

**Sensitivity analyses are conducted.** Even under strong assumptions, the estimates can be probed for robustness. Analyses that explicitly model the potential bias from unmeasured confounders give readers a sense of how trustworthy the decomposition is.

**The scientific question is modest.** Decomposing an effect into "some through M" vs. "some not through M" is easier than pinpointing exact fractions. Qualitative conclusions ("most of the effect is mediated by M") are often defensible when precise quantitative decompositions are not.

A well-designed mediation analysis in a randomized trial, with careful adjustment for observed M-Y confounders and sensitivity analyses for unmeasured ones, can produce credible estimates of direct and indirect effects. Most published mediation analyses do not meet this standard. Most rely on observational data, Baron-Kenny-style methods, and no sensitivity analysis. Results from such studies should be treated skeptically.

## Mediation in the smoking-cancer case

Let's bring this back to a classic example. Smoking causes lung cancer. Does it cause cancer through tar accumulation, through nicotine-related effects on the immune system, through chronic inflammation, through direct DNA damage from smoke particles, or through some combination?

A mediation analysis of smoking-cancer would define the treatment (smoking), the candidate mediator (say, tar accumulation), and the outcome (lung cancer). It would try to decompose the total effect of smoking on cancer into the part that goes through tar and the part that doesn't.

The challenges are severe. We cannot randomize smoking. Tar is not directly measured in most studies; we infer it indirectly. The confounders of the tar-cancer relationship are themselves numerous and hard to measure. The assumption that smoking doesn't affect the confounders of tar-cancer is strong and probably false.

A rigorous mediation analysis of smoking-cancer would likely conclude: "Tar appears to mediate a substantial portion of smoking's effect on cancer, under assumptions about confounders that are consistent with current knowledge but cannot be directly verified. Sensitivity analyses suggest that the qualitative conclusion — that tar is an important mediator — is robust to plausible violations of the assumptions."

This is a much more tentative conclusion than the "X% of smoking's effect on cancer is through tar" that a Baron-Kenny analysis might produce. But it is the honest conclusion. The data and assumptions support a qualitative claim about mediation; they do not support a precise quantitative decomposition.

Most real mediation questions are like this. The qualitative conclusions are often defensible and useful. The quantitative precision that Baron-Kenny papers offer is often illusory.

## Probability of necessity and sufficiency

One specific application of counterfactual reasoning deserves separate mention: probabilities of necessity and sufficiency.

The *probability of necessity* (PN) is: given that X occurred and Y occurred, what is the probability that Y would not have occurred if X had not occurred? In legal terms, this is the "but for" probability — the probability that X was necessary for Y. If the defendant's negligence occurred and the injury occurred, PN is the probability that the injury would not have occurred absent the negligence.

The *probability of sufficiency* (PS) is: given that X did not occur and Y did not occur, what is the probability that Y would have occurred if X had occurred? This is the probability that X would have been sufficient to cause Y.

These quantities are fundamentally counterfactual. They ask about what would have happened in counterfactual scenarios. They can be bounded or estimated from observational data under appropriate causal models, and they have become increasingly important in epidemiology, law, and policy analysis.

A compelling recent application is climate attribution. When an unusual heat wave or storm occurs, scientists ask: would this event have happened without anthropogenic climate change? This is a PN question. Estimates based on climate models and observational data can bound the probability that a specific event was necessary-dependent on climate change — that is, the probability that the event would not have occurred without human influence on climate.

These attribution analyses use counterfactual methods extensively. They compute what the probability of the event would have been under a counterfactual climate (pre-industrial greenhouse gas levels) and compare it to the probability under the actual climate. The ratio gives a measure of how much climate change contributed to the event.

The methodology is at the frontier of applied counterfactual analysis. The conclusions are sometimes dramatic: some recent heat waves have been estimated to be essentially impossible without climate change, meaning PN ≈ 1. Other events have PN estimates around 0.5, suggesting climate change roughly doubled their probability.

Probability of necessity and sufficiency have a long history in philosophical analysis of causation but have become practically important only with the development of computational methods for counterfactual inference. They represent some of the most refined causal questions that modern methods can address.

## When counterfactuals matter most

The counterfactual framework comes into its own in three broad categories of application:

**Individual-level questions.** When you need to know the effect of a treatment on a specific individual — not on average, but for this particular person — counterfactuals are essential. Personalized medicine, individualized legal judgments, and algorithmic fairness assessments all require individual-level counterfactual reasoning.

**Mechanism questions.** When you need to understand how a cause produces its effects, mediation analysis provides the formal tools. The counterfactual definition of direct and indirect effects, though more demanding than simpler approaches, is the only framework that handles complex causal structures correctly.

**Attribution questions.** When you need to assign responsibility or credit for a specific outcome, counterfactual methods are the formal foundation. Legal liability, scientific attribution (as in climate science), and many policy evaluations all turn on counterfactual questions.

Outside these categories, population-level causal inference using the methods of Chapters 3-7 is often sufficient. You don't need counterfactuals to answer "does smoking cause cancer on average?" — you need them to answer "did smoking cause this person's cancer?"

## What counterfactual analysis cannot do

**It cannot escape the fundamental problem.** We observe one outcome per individual. Inferring the other outcome requires model assumptions. The assumptions may be reasonable or implausible, well-supported or speculative, but they are always assumptions. Counterfactual analysis does not prove the counterfactual; it computes it under a model.

**It cannot verify its own assumptions.** The causal model that underlies a counterfactual analysis contains assumptions about structure and functional forms. These are not generally testable from the data. Different models can give different counterfactual answers from the same observations. The analyst's commitment to a specific model is where the answer comes from.

**It cannot handle arbitrary nested counterfactuals without data.** Some counterfactual questions involve nested manipulations that the data cannot support. "What would have happened if X had been different, and Y had responded to that change, and Z had responded to both?" is the kind of question that requires strong model assumptions or experimental evidence.

**It is often more fragile than it looks.** The elegance of the formulas can mask the strength of the assumptions. A reader who sees a published mediation analysis with precise decompositions might not realize how many things had to go right for those numbers to be valid. Sensitivity analysis is essential, and when it is absent, skepticism is warranted.

## Summary

Counterfactuals are statements about what would have happened under alternative conditions. They occupy the third rung of the ladder of causation and enable the most refined causal questions — about individuals, mechanisms, and attribution.

The potential outcomes framework provides a formal language for counterfactual reasoning, associating each individual with a vector of outcomes under different possible treatments. Under appropriate assumptions, average counterfactuals at the population level can be estimated from data using the methods of earlier chapters. Individual-level counterfactuals require structural causal models and more demanding assumptions.

The three-step procedure for computing counterfactuals from a structural causal model — abduction, action, prediction — is the general mechanical framework. It applies to both individual and population counterfactuals.

Mediation analysis is a particularly important counterfactual application. The Baron-Kenny approach to mediation, while widely used, makes implicit assumptions that often fail in practice. The counterfactual formulation, based on natural direct and indirect effects, is more demanding but more correct. Under appropriate assumptions, the mediation formulas identify direct and indirect effects from observable data. The assumptions are strong and often not fully satisfied.

Probability of necessity and sufficiency are counterfactual quantities that answer questions about attribution and responsibility. They are increasingly important in epidemiology, law, and climate science.

Counterfactual analysis is the deepest and most ambitious layer of causal inference. Its tools enable questions that no other framework can ask. Its fragility is that the answers depend on model assumptions that the data cannot verify. When the assumptions are defensible, counterfactual analysis gives answers of unique value. When they are not, it produces elegant fictions.

The next and final chapter of the theory spine takes a step back from technique to teach you how to read causal case studies — the ones in this book, and the ones you will encounter in the wider literature. We will pull together the lessons of the preceding chapters and develop a structured approach to evaluating causal claims, including an extended discussion of how contemporary buzzwords like "Causal AI" confuse what causal inference actually does.

---

## A note about AI

Counterfactual reasoning is the rung where the data alone cannot answer the question. The model produces counterfactual claims fluently because language permits them — but the claims rest on assumptions the data cannot verify.

Where the model genuinely helps: walking through the distinction between controlled direct effects, natural direct effects, and natural indirect effects on a specific applied example.

Where the model does damage: producing the counterfactual claim itself without naming the cross-world assumption it rests on. Every counterfactual depends on an assumption that cannot be empirically checked.

The rule: framework from the model; the assumption set is a commitment the analyst must name and defend.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Tyler VanderWeele** built the modern theory of mediation analysis in the 2010s — extending classical Baron-Kenny mediation to handle interactions, time-varying mediators, and exposure-mediator confounding. His textbook is the standard reference for causal mediation.

**Run this:**

```
Who is Tyler VanderWeele, and how does his mediation work connect to counterfactuals and mediation we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Tyler VanderWeele"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through controlled vs. natural direct/indirect effects on a specific applied example.
- Ask it about VanderWeele's controversial advocacy for incorporating measures of human flourishing in public health.

What changes? What gets better? What gets worse?
