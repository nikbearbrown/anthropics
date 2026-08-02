# The Smallest Set That Closes the Door — And the Door That Will Not Close


## TL;DR

- TL;DR: A valid adjustment set is rarely unique — and among the valid ones, smaller is usually better, for reasons that are statistical, structural, and operational.
- The chapter moves through Opening — The extra control that made everything worse, Concept one — Minimal valid adjustment, defined carefully, Concept two — Why less is sometimes more, Mid-chapter checkpoint, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

**Suggested titles:**
1. The Smallest Set That Closes the Door — And the Door That Will Not Close
2. Minimal Adjustment, Honest Failure: When the Backdoor Will Not Close
3. The Variable You Did Not Add, And the One You Cannot Find

**TL;DR:** A valid adjustment set is rarely unique — and among the valid ones, smaller is usually better, for reasons that are statistical, structural, and operational. Sometimes no valid adjustment set exists, and that verdict — *not identifiable from observational data* — is a real scientific result rather than a course you failed.

**Byline:** Nik Bear Brown

**Prerequisites:**
- The backdoor criterion as stated in Chapter 9: condition (i) no descendants of treatment, condition (ii) block every backdoor path.
- Confounders (Ch. 5), mediators (Ch. 6), and colliders (Ch. 7–8) — what each does on the graph and what conditioning on each does to a path.
- Reading a DAG fluently: paths, arrows, the meaning of "open" and "blocked." (Ch. 3.)
- The identification layer as the layer that lives upstream of estimation (Ch. 4).

**Learning objectives:**
- **Analyze (Part A):** Derive the minimal valid adjustment set for a six-to-eight-node DAG and defend why removing any variable from your set breaks validity.
- **Evaluate (Part A):** Given a DAG with an unmeasured variable on an open backdoor path, state whether the causal effect of T on Y is identifiable from observational data alone, and explain why the answer does not depend on sample size.
- **Evaluate (Part B):** Assess whether the causal effect you care about in your own domain is identifiable from the data your field currently collects.
- **Create (Part B):** Specify what data collection — interventional, instrumental, or measurement — would unlock identification when current data does not.

---

## 1. Opening — The extra control that made everything worse

In April 2023, the team I will call Team Pricing at a mid-sized e-commerce company shipped what they thought was a careful causal analysis. The treatment was a new dynamic-pricing algorithm rolled out to a subset of product categories. The outcome was weekly category revenue. The team had been schooled, properly, on confounders. They knew seasonality mattered, inventory state mattered, upstream marketing spend mattered, and the competitor's pricing — observable through a third-party scraping service — mattered.

So they did the careful thing. They built a DAG. They identified four observable variables that sat on backdoor paths. To be safe — *to be safe* — they also added two more variables that were available and seemed like they might matter: a "promotional intensity score" the marketing team published, and a "category lifecycle indicator" the merchandising team maintained. Six controls. More is more. Right?

The effect estimate flipped sign. Under four controls, the new pricing algorithm looked mildly positive — about a 2.3% lift in weekly revenue. Under six, it looked mildly *negative* — about a 1.8% drag. Same treatment. Same outcome. Same data. Two variables added "for safety," and the conclusion the team would walk into their VP's office to defend had reversed.

The pricing algorithm's effect on revenue did not change. The team's *estimate* of it changed because they had inadvertently conditioned on variables that — in the actual structure of the business — were not backdoor blockers. The promotional-intensity score was a downstream consequence of the pricing algorithm itself; the marketing team adjusted intensity in response to algorithmic price changes within the week. The category-lifecycle indicator was set, in part, by the merchandising team's observation of recent revenue — which is to say, by the outcome. One of those new "controls" was a mediator. The other was a descendant of the outcome. Both were *correlated* with treatment and outcome. By the broken-but-widespread "throw them all in" rule, they belonged in the regression. By the structural criterion from Chapter 9, they did not. Adding them did not improve identification. It destroyed it.

The team was not careless. They had read Pearl. They had drawn a DAG. They had even, in their write-up, *named the backdoor paths*. What they had not yet internalized is the move this chapter is about: among the variables a careful analyst could add, there is a smallest set that does the job — and adding anything beyond that set is not free.

The previous five weeks collapse into a single sentence. Mediators? Don't add them. Colliders? Don't add them. Descendants of the outcome? Don't add them. Variables already on a closed path? Don't bother. Of what remains — the variables that *do* block open backdoor paths — pick the smallest set that gets the job done. Then we look at the case where no such set exists at all. Which, it turns out, is not a failure. It is a finding.

---

## 2. Concept one — Minimal valid adjustment, defined carefully

Let me name the term before I argue about it. A *valid* adjustment set is a set of observed variables that, when you condition on them, satisfies the backdoor criterion from Chapter 9: no member of the set is a descendant of the treatment, and every backdoor path from treatment to outcome is blocked by the set. A *minimal* valid adjustment set is a valid adjustment set such that no proper subset of it is also valid. Read that twice. "Minimal" does *not* mean "smallest cardinality among all valid sets." It means: if you remove any single variable from this set, the set stops being valid. Minimality is a *lattice* property — a local property of the set you are holding — not a global property comparing all sets in the universe.

The distinction matters because DAGs frequently admit several minimal sets of different sizes. A DAG can have one minimal set of size two and another of size three; both are minimal in the lattice sense, neither contains the other, and the question of which to *use* is a different question from the question of which sets *qualify*. The procedural answer — enumerate all minimal sets — comes from Benito van der Zander, Maciej Liśkiewicz, and Johannes Textor, who published a polynomial-time algorithm at UAI 2014 ([van der Zander, Liśkiewicz, and Textor, "Constructing Separators and Adjustment Sets in Ancestral Graphs," UAI 2014](https://auai.org/uai2014/proceedings/individuals/325.pdf) `[verify-URL]`; subsequent journal version "Separators and adjustment sets in causal graphs: Complete criteria and an algorithmic framework," *Artificial Intelligence*, vol. 270 — `[verify-pagination]`). DAGitty implements this as `adjustmentSets()`. So does the `dagitty` R package. The student does not have to *invent* the procedure. The student has to understand what it returns and what to do with the return value.

Let me make all of this concrete.

Consider a DAG with seven nodes: T (treatment), Y (outcome), and five candidate adjustment variables Z₁, Z₂, Z₃, Z₄, M. The edges are:

```
        Z₁
       /  \
      ↓    ↓
      T    Y
       \  /
        Z₂
       /  \
      ↓    ↓
      Z₃   T
            ↓
            M
            ↓
            Y
```

Let me list that more cleanly. The arrows are: Z₁ → T, Z₁ → Y, Z₂ → T, Z₂ → Z₃, Z₃ → Y, T → M, M → Y, and Z₄ — a fully isolated noise variable — has no arrows to or from anything in the diagram. (Z₄ is in the data the analyst pulled because someone left it in the export script.)

What are the backdoor paths from T to Y? Two of them. The first: T ← Z₁ → Y. The second: T ← Z₂ → Z₃ → Y. Both start with an arrow *into* T (the backdoor signature) and end at Y.

What blocks each path? The first path is blocked by Z₁, and only by Z₁ — there is no other observed node on it. The second path is blocked either by conditioning on Z₂ *or* by conditioning on Z₃. Either node sits on a chain in the path, and conditioning on any node in a chain blocks the chain.

So the candidate adjustment sets that block both backdoor paths are:

- {Z₁, Z₂}
- {Z₁, Z₃}
- {Z₁, Z₂, Z₃}

The first two are minimal — remove any single variable from either, and an open backdoor path reopens. The third is *sufficient* but not minimal: removing Z₂ leaves {Z₁, Z₃}, which is still valid. Both {Z₁, Z₂} and {Z₁, Z₃} are valid choices in the lattice sense, and neither contains the other.

What about M, the mediator on T → M → Y? It is *not* on a backdoor path. (Its path from T does not start with an arrow into T; the arrow goes the other way.) Conditioning on M does not close a backdoor. What conditioning on M *does* is intercept the very causal effect we are trying to estimate. If we adjust for M, we are no longer estimating the total effect of T on Y — we are estimating something like the *direct* effect, holding M fixed. Different question. Different number. Almost certainly not the one the analyst was asked.

What about Z₄, the noise variable? It is on no path between T and Y. Adjusting for it does not change which paths are open or closed. It does not bias the estimate. But — and this matters more than the textbook treatments usually acknowledge — it does inflate the variance of the estimate by adding an irrelevant parameter to the model. Z₄ is harmless in expectation and costly in finite samples.

The minimal-set principle does not say "always use the smallest minimal set." It says: of the sets you might use, prefer one that does the job and no more. The "no more" is what we are about to take apart.

A common misconception lives here. Students arriving from the regression-with-many-controls tradition — which is most of applied ML — have absorbed the heuristic "bigger is safer." Chapters 6 and 7 already showed why that heuristic is wrong on the bias side. Mediators and colliders, added "for safety," do not just fail to help; they actively destroy what the analysis was trying to do. Chapter 10 names the principle: bigger is not safer. *Exactly enough* is safer than either *not enough* or *more than enough*.

---

## 3. Concept two — Why less is sometimes more

There are three reasons, at three different levels of the analysis. Keep them apart.

The first reason is **statistical**. Every variable in your adjustment set is a parameter your estimator has to estimate from finite data. The variance of an estimator under standard methods — OLS, propensity-score weighting, doubly-robust estimation — depends on how much information in the data is left after the conditioning has been done. Variables that block real backdoor paths *earn* their inclusion: bias removed is worth the variance cost. Variables that do not block anything take variance and give nothing back. Let me show it.

Take a stripped-down linear case. The treatment T is binary. The outcome Y is continuous. The structural equation is

$$Y = \beta T + \gamma_1 Z_1 + \gamma_2 Z_2 + \gamma_3 Z_3 + \varepsilon$$

with $\varepsilon$ a mean-zero noise term independent of everything else, variance $\sigma^2$. The candidate adjustment sets are $A = \{Z_1, Z_2\}$ (size 2, minimal) and $B = \{Z_1, Z_2, Z_3, Z_4, Z_5\}$ (size 5, valid but not minimal, with $Z_4$ and $Z_5$ being adjustment-irrelevant — they block nothing, but they are correlated with $T$ at $r_4$ and $r_5$).

Under OLS, the variance of the estimated $\hat\beta$ in a sample of size $n$ is approximately

$$\text{Var}(\hat\beta) \approx \frac{\sigma^2}{n \cdot \text{Var}(T \mid Z) \cdot (1 - R^2_{T \sim Z})}$$

where $R^2_{T \sim Z}$ is the share of variance in T explained by the adjustment set. When we adjust for variables that are correlated with T but do not sit on backdoor paths, $R^2_{T \sim Z}$ goes up, $1 - R^2_{T \sim Z}$ goes down, and $\text{Var}(\hat\beta)$ goes *up*. Bias did not improve. Variance got worse.

Plug in numbers. Suppose $\sigma^2 = 1$, $n = 1000$, and under set $A$ the residual treatment variance is $\text{Var}(T \mid Z_1, Z_2) = 0.20$ with $R^2_{T \sim A} = 0.20$. Then

$$\text{Var}(\hat\beta_A) \approx \frac{1}{1000 \cdot 0.20 \cdot 0.80} = \frac{1}{160} \approx 0.00625$$

so the standard error is roughly $\sqrt{0.00625} \approx 0.079$.

Now add $Z_4$ and $Z_5$, which together raise $R^2_{T \sim Z}$ from 0.20 to 0.50 — the new variables are correlated with T but contribute nothing to closing a backdoor. Residual variance of T drops to roughly 0.125. Then

$$\text{Var}(\hat\beta_B) \approx \frac{1}{1000 \cdot 0.125 \cdot 0.50} = \frac{1}{62.5} \approx 0.016$$

and the standard error is roughly $\sqrt{0.016} \approx 0.126$.

Standard error went from 0.079 to 0.126. A 60% inflation. With the same bias profile. For two variables that did no path-blocking work. The team that adds variables "to be safe" is paying for that safety in confidence-interval width, and the interval is the place the decision-maker actually reads the result.

Lars Henckel, Emilija Perković, Andrea Rotnitzky, and James Robins formalized the full version of this argument in 2022 in the *Journal of the Royal Statistical Society B* ([Henckel et al. 2022](https://doi.org/10.1093/jrsssb/qkac001)). Their result is more nuanced than "smaller is better": the *variance-optimal* adjustment set is a particular graphical construction that is not always the smallest, and not always equal to any minimal set — sometimes adding a pre-treatment variable downstream of the confounders can *reduce* variance because it carries information about the noise in Y. The take-away for the engineering reader: minimality is a strong default; the efficient-adjustment-set literature complicates it in ways worth knowing about but not worth teaching in week 10. Use minimal sets unless you have a specific reason to deviate.

The second reason is **structural**. Every variable in your adjustment set is a chance for a collider you did not notice. The Chapter 7 lesson: conditioning on a collider opens a path that was closed. Real DAGs frequently contain subtle colliders. A variable that looks like a benign control may, on inspection, turn out to be a common consequence of two of your covariates. The bias from accidentally conditioning on a collider can be larger than the bias the adjustment was meant to fix. The Team Pricing example sits in this category — the promotional-intensity score was a descendant of the treatment, and conditioning on it broke the causal path.

The third reason is **operational**. Every variable in your adjustment set is a measurement requirement on your data pipeline. The "promotional intensity score" in the Team Pricing example was a number that came from a different team's spreadsheet, updated weekly. A year after the analysis shipped, the team that maintained the score reorganized; the format changed; the pricing team's regression broke; their nightly causal-effect monitor stopped running. The lesson is dull and important: every variable in your model is a dependency, and dependencies break. The minimal-set principle, viewed operationally, is an argument for not letting your causal analysis depend on more parts than the question requires.

The three reasons usually point the same way. When they do not — when a careful variance analysis says a slightly larger set is preferable, or a structural pattern says a strictly larger set is the only valid one — go with the analysis, not the heuristic. The heuristic is a default. The DAG is the law.

---

### Mid-chapter checkpoint

Stop. Before you read further, can you do the following on a DAG given to you cold?

1. Find every backdoor path between T and Y.
2. Enumerate the minimal valid adjustment sets — every set where removing any variable breaks validity.
3. Identify every variable that is *not* in any minimal set, and say what it is: a mediator, a collider, a descendant of T, a descendant of Y, an isolated noise variable, or something else.
4. Pick a minimal set and write one sentence justifying the choice on grounds of variance, structure, or operational simplicity.

If any of those moves still feels uncertain, the second half of the chapter is going to feel harder than it has to. The second half is about the case where the first three steps return *the empty answer*: no valid adjustment set exists at all. The reasoning we are about to do depends on the reasoning we just did.

---

## 4. Concept three — Non-identifiability, what it actually means

Here is the situation we are about to handle. You have built your DAG. You believe it is approximately right. You run the backdoor criterion on it. You enumerate the candidate adjustment sets. The enumeration returns nothing. There is no observed set of variables that blocks every backdoor path. The reason, every time you trace it, is the same: somewhere on the graph there is an unmeasured variable U that creates a backdoor path between T and Y, and no observed variable sits on that path.

This is the situation we call *non-identifiability from observational data*. Let me define it carefully, because the term is doing real work and the misreading of it is the load-bearing pedagogical mistake in this corner of causal inference.

**A causal effect of T on Y is non-identifiable from observational data, given a DAG, if no procedure exists that can estimate that effect from observations of T, Y, and the observed variables alone — regardless of sample size, model class, or computational budget.**

Read that twice. The verdict is *not* "we have not yet figured out how to estimate it." The verdict is "no procedure can estimate it, given this graph and this data, full stop." The verdict is *not* about your skill, your sample size, your model, or your patience. It is a statement about what the joint distribution of the observed variables determines, and what it does not determine, given the structural constraints the graph encodes.

The formal version of this statement is Ilya Shpitser and Judea Pearl's ID algorithm, published in 2008 in the *Journal of Machine Learning Research* ([Shpitser and Pearl, "Complete Identification Methods for the Causal Hierarchy," *JMLR* vol. 9, 2008](https://www.jmlr.org/papers/volume9/shpitser08a/shpitser08a.pdf)). The algorithm takes a DAG and a causal query — for instance, "what is $P(Y \mid do(T = 1))$?" — and returns, in finite time, either an explicit expression for the query in terms of observational probabilities (identifiable) or the verdict "not identifiable." The algorithm is *complete*: if a causal query is identifiable from observational data given the DAG, the algorithm produces the formula; if it returns "not identifiable," no such formula exists. The verdict is sharp.

Let me walk through the canonical case so the word "non-identifiable" is something you have actually touched. The DAG is four nodes: T (treatment), Y (outcome), U (unmeasured), Z (observed).

The edges are: U → T, U → Y, Z → T, Z → Y, and T → Y.

```
       Z ─────→ T ─────→ Y
        \              ↗
         \            /
          \   U ─────/
           \ /
            T  (from U)
```

(Cleanly: Z has arrows to T and Y; U has arrows to T and Y; T has an arrow to Y; U is unmeasured.)

The backdoor paths from T to Y:

1. T ← Z → Y. Z is observed. Conditioning on Z blocks this path.
2. T ← U → Y. U is unmeasured. *Nothing observed* sits on this path. We cannot condition on what we cannot measure.

No matter what we do with the observed variables, path 2 stays open. The Shpitser-Pearl algorithm reads the graph, finds the open path through U, and returns: not identifiable. No collection of conditioning operations on Z (or anything else observed) reproduces $P(Y \mid do(T))$.

To see *why* the answer cannot be coaxed out of more data, let me write down what the data actually tells us. From samples we can estimate

$$P(Y \mid T = t, Z = z)$$

— that is, the conditional probability of Y given that we observe T = t and Z = z. From this and $P(Z = z)$ we can estimate

$$\sum_z P(Y \mid T = t, Z = z) P(Z = z)$$

which is the so-called *adjustment formula* applied to Z. If U did not exist, this would equal $P(Y \mid do(T = t))$ — that is the entire content of the backdoor criterion. But U does exist. Specifically, U influences both T and Y. The distribution we just wrote down still carries information about Y that flowed through the U-path — the path we did not close. The adjustment formula no longer equals the interventional distribution. The gap is what statisticians call *unmeasured-confounding bias*, and the size of the gap depends on the strength of U's effect on T and on Y. We cannot estimate the gap from observational data, because every observational quantity is contaminated by it.

Note what does *not* dissolve the problem. Collecting more rows: $P(Y \mid T, Z)$ converges to its true value, but the true value is still wrong. Switching to a more flexible model: the model fits a more accurate version of the wrong thing. Adding a more sophisticated estimator (DML, IPW, BART): the estimator targets the same observational quantity, which is the same biased one. None of the machinery applied below the identification layer can change the verdict. The verdict was determined at the structural level.

I want to spend one paragraph on the contrast with sample-size problems, because the conflation is where most of the engineering reader's confusion lives. A *statistical* problem is one where, with more data, the answer gets more precise — the confidence interval narrows, the estimate stabilizes, the standard error shrinks. A *structural* problem is one where, with more data, the answer gets more precise *around the wrong number*. Non-identifiability is the second kind. The data has answered a question — just not the question you asked. It has answered "what is $P(Y \mid T)$ in this observational distribution?" with arbitrary precision. What it has not answered, and what it cannot answer, is "what is $P(Y \mid do(T))$?" — because that quantity is not a function of the observational distribution alone.

This is the place where you have to slow down and let the framing change. In supervised learning, "more data" is the universal therapy. In identification, it is not. Some problems do not respond to that medicine, and the diagnosis is structural rather than statistical.

---

## 5. Concept four — Non-identifiability is a finding, not a failure

The phrase that has to settle in the engineering reader's head — and the phrase the textbook tradition has so often mishandled that TIKTOC explicitly flags it — is this one. *Non-identifiability is an honest result, not a failure.* Read it slowly. *Honest result. Not failure.* Let me argue for it from three directions, because the misreading is so common that one argument is not enough.

The first direction is **what the analysis is for**. An identification analysis is a trust assessment. You are asking: can the data I have, under the structure I believe holds, support the causal claim I want to make? When the analysis returns "yes, conditioning on this set," the trust assessment has produced a positive result. When it returns "no, the question cannot be answered from this data," the trust assessment has produced a different kind of positive result — it has correctly diagnosed the situation. The analyst who reports "not identifiable, given this DAG and this data" has done their job. The analyst who quietly forces an estimate by adjusting for what happens to be available has not done their job; they have produced a number that does not bear the weight the decision will place on it.

The second direction is **what a decision-maker actually needs**. A VP looking at a regression output is going to make a decision. They are going to decide whether to keep the new pricing algorithm, whether to expand the clinical referral program, whether to escalate the fraud-detection model. The decision is downstream of the number. If the number was produced by a procedure that quietly absorbed unmeasured confounding into the point estimate, the decision rides on a wrong premise. If the number was accompanied by "this is the estimate under the assumption that no unmeasured confounding exists, and we have reason to think there is a substantial unmeasured confounder," the decision-maker can — *and a good one will* — ask the follow-up question. Bounds. Sensitivity analysis. Additional data. The honest report does not eliminate the decision; it preserves the decision-maker's ability to make it for the right reasons. A point estimate with hidden assumptions does the opposite.

The third direction is **what the field considers good work**. Charles Manski has been making this argument for thirty-five years. His 1990 *American Economic Review* paper — "Nonparametric Bounds on Treatment Effects" — laid out the case that, when point identification is unavailable, reporting an informative *range* under stated assumptions is a more honest analytical output than a point estimate under unstated ones ([Manski 1990](https://www.jstor.org/stable/2006592)). The argument has aged well. The Strategic Management literature has begun, in the last five years, to recommend partial-identification framings as the methodological default for many corporate-data questions where randomization is unavailable. Will Frake's 2025 piece in *Strategic Management Journal* argues for moving "the conversation from whether a result is 'identified' to a discussion that allows the reader to judge what may be learned given their priors" `[verify-exact-citation]`. Tan et al. published "Consistency of Neural Causal Partial Identification" at NeurIPS 2024, showing that the technical machinery for bounds analysis has matured to where the engineering reader can run it computationally ([Tan et al. 2024](https://arxiv.org/abs/2405.15673) `[verify-exact-citation]`). The "non-identifiability is a failure" reading is not just out of step with current methodology — it is out of step with where the field has been moving for a generation.

A diagnostic analogy may help here, and like every analogy in this book it has to earn its keep. Picture a physician ordering a blood test. The test comes back *inconclusive* — not "negative" and not "positive," but "this test, with this patient, with this prior, cannot distinguish the conditions we were trying to distinguish." A good physician does not blame the test for being inconclusive. They order a different test, or they collect a different kind of evidence (history, imaging, biopsy), or — if the consequences of being wrong are small — they decide they have enough to act. The test did its job. The inconclusive verdict is the test reporting honestly on what it can and cannot say. The identification analysis is the analytical version of that test, and "not identifiable" is the analytical version of "inconclusive." The analogy breaks down at the edges — a blood test is run on a single patient, an identification analysis is a property of a question and a distribution — but the core posture is right. Inconclusive is a verdict. Verdicts are results.

What does this look like in practice? Concretely, in the deliverable the student produces in Chapter 11 and again in Chapter 14:

1. The DAG is presented with the unmeasured variable named explicitly. Not glossed over. *Named.*
2. The verdict — "this effect is not identifiable from currently-available observational data, given the assumed DAG" — is the headline finding.
3. The sources of non-identifiability are listed individually: which backdoor path is open, which variable would close it.
4. The *escape routes* are listed individually: which intervention would help, which proxy might help, which assumption would suffice if defensible, what bounds can be computed under what assumptions.
5. The recommendation is for the next analytical step — *not* a point estimate. The point estimate is what the analysis explicitly declines to produce.

This is not a defeat. It is a different kind of output. It is the output of an analyst who knows the difference between a question their data can answer and a question their data cannot, and who declines to manufacture an answer where none is warranted. The engineering field rewards the second behavior over the first because the cost of an unjustified point estimate, multiplied by the size of the decision it informs, dwarfs the cost of a slower analysis with bounds.

I will name where this framing has limits. The framing assumes the analyst has organizational room to deliver "not identifiable" as a deliverable. In some settings — particularly settings under deadline pressure or with executives who believe analysis equals number — that room does not exist. The chapter cannot solve that problem for you. What the chapter can do is equip you to know which conversation you are having, so that when you are pushed to produce a number, you know what the number is worth and you can tell the person asking. That conversation is the subject of Chapter 11.

---

## 6. Concept five — Partial identification, what you can do anyway

If non-identifiability is the wall, partial identification is the door cut into the wall. The idea, in one sentence: even when you cannot estimate the causal effect as a single number, you can sometimes estimate a *range* into which the causal effect must fall under a stated set of assumptions. The range is the analytical output. It is honest. It is decision-relevant whenever the range is narrow enough to distinguish the policy alternatives — and when it is not, the width itself is a useful piece of information, because it tells you that the data plus the assumptions you are willing to make do not distinguish the alternatives.

Manski's 1990 paper introduces the simplest version, often called the *no-assumptions bounds* or the *worst-case bounds*. Let me run it on a stylized example, because the arithmetic is the whole point.

Consider a binary treatment T (assigned somehow, possibly with confounding) and a binary outcome Y. We want the average treatment effect (ATE) — the difference between the population's outcome under universal treatment and its outcome under universal non-treatment. Formally,

$$\text{ATE} = E[Y \mid do(T = 1)] - E[Y \mid do(T = 0)]$$

In the observed data, suppose the marginal probability of being treated is $P(T = 1) = 0.6$ and that $P(T = 0) = 0.4$. Suppose the observed outcome rates are $P(Y = 1 \mid T = 1) = 0.7$ and $P(Y = 1 \mid T = 0) = 0.3$.

A naive analyst would report the difference, 0.7 − 0.3 = 0.4, and call it the ATE. The naive analyst is treating $P(Y \mid T)$ as if it were $P(Y \mid do(T))$. If there is unmeasured confounding, those quantities differ — that is the whole content of the chapter so far. So we cannot report 0.4 as the ATE. The naive analyst is doing the failure mode.

The Manski approach instead asks: under *no assumptions about the unmeasured confounding*, what is the largest and smallest the ATE could possibly be, given the marginal and conditional probabilities we observe?

Decompose $E[Y \mid do(T = 1)]$:

$$E[Y \mid do(T = 1)] = P(T = 1) \cdot P(Y = 1 \mid T = 1, \text{counterfactual}) + P(T = 0) \cdot P(Y = 1 \mid T = 0, \text{counterfactual under do(T=1)})$$

The first piece, we know: for units that were observed under T = 1, the observed outcome is the *do(T=1)* outcome (since for those units, treatment did equal 1). So $P(Y = 1 \mid T = 1, \text{counterfactual T=1}) = P(Y = 1 \mid T = 1) = 0.7$.

The second piece, we do not know: what would Y have been for the units that were observed under T = 0 if instead they had been treated? With no assumptions, this is somewhere between 0 and 1.

So the bounds on $E[Y \mid do(T = 1)]$ are:

- Lower bound: $0.6 \cdot 0.7 + 0.4 \cdot 0 = 0.42$
- Upper bound: $0.6 \cdot 0.7 + 0.4 \cdot 1 = 0.82$

By symmetric reasoning,

- Lower bound on $E[Y \mid do(T = 0)]$: $0.4 \cdot 0.3 + 0.6 \cdot 0 = 0.12$
- Upper bound on $E[Y \mid do(T = 0)]$: $0.4 \cdot 0.3 + 0.6 \cdot 1 = 0.72$

The bounds on the ATE are the bounds on the difference. The lower bound on the difference is (lower on do(1)) − (upper on do(0)) = 0.42 − 0.72 = −0.30. The upper bound is (upper on do(1)) − (lower on do(0)) = 0.82 − 0.12 = 0.70.

So under no assumptions about the confounding, the ATE lies somewhere in the interval [−0.30, +0.70]. That interval is one unit wide. It contains zero. It does not distinguish "the treatment helps a lot" from "the treatment hurts." The naive point estimate of +0.40 sits inside this interval, but so does almost everything else. The data, under no assumptions, has not answered the question.

This is the bare-no-assumptions bound. Watch what happens when you add an assumption. Suppose you are willing to assume *monotone treatment response* — that for every unit, being treated weakly improves the outcome (Y under T=1 is at least as large as Y under T=0). That is a substantive domain assumption — it has to be defended, not just declared — but if you can defend it, the bound on the counterfactual outcome under T = 0 (for treated units) is no longer [0, 1]; it is [0, 0.7], because Y under T = 0 cannot exceed Y under T = 1 for any unit. Each substantive assumption tightens the bounds. Each tightening is purchased with a defensible premise. The output of the analysis is now: under monotone treatment response, the ATE lies in [some narrower interval] — and the engineering reader can see exactly which assumption is bearing the weight.

The general principle: partial identification is a ladder. The bottom rung is *no assumptions*, and the bounds are typically wide. Each rung up is *one additional assumption*, and the bounds typically narrow. The analyst chooses how far up the ladder to climb based on what they can defend. At every rung, the output is honest: the bounds reflect what the data plus the named assumptions say. The point estimate at the top of the ladder — equivalent to point identification — corresponds to a particular set of strong assumptions, which the partial-identification framing has now made *visible* rather than hidden.

This is the move the engineering reader did not have before this chapter. When point identification fails, the analyst is not out of analytical tools. They are inside a different toolset, where the deliverable is a bound and a list of assumptions, and the decision-maker gets to see both. The chapter does not teach the algorithms for partial identification in any depth — Tan et al. (2024) on neural causal models for continuous variables, Duarte et al. (2024) for discrete settings `[verify-exact-citations]`, and the long Manski tradition for the foundations. What it teaches is the *framing*: bounds are output. Width is information. Honesty is the deliverable.

The implementation: when point identification fails, climb the partial-identification ladder. Start with the no-assumptions bounds. If they are useful, stop. If they are not, add the weakest defensible assumption and recompute. Continue. The number you eventually report is the bounds you can defend, not the bounds you wish you had.

---

## 7. Concept six — The other ways out, briefly and honestly

Partial identification is one escape route from non-identifiability. There are others. I name them here, briefly, because the engineering reader needs to know they exist; this book does not teach them all, and the ones it does not teach are pointed toward the textbooks where you can learn them properly.

**Interventional data.** The cleanest escape. Run a randomized experiment that breaks U's influence on T. The randomization breaks the U → T arrow at the design level: the treatment assignment is now a function of a random number, not of U. The backdoor path T ← U → Y closes structurally. Identification, post-randomization, is trivial. The cost: experimentation may be expensive, slow, ethically constrained, or infeasible. When randomization is available, it is the right answer.

**Front-door adjustment.** Pearl introduced this in 1995 in *Biometrika* ([Pearl 1995](https://www.biostat.jhsph.edu/~cfrangak/biostat_causal/pearl_1995_causaldiagrams.pdf) `[verify-URL]`). If there is an observed variable M sitting *on the causal pathway* between T and Y, and M is itself unconfounded with Y given T, then the causal effect of T on Y can be recovered from data on T, M, and Y — even with an unmeasured U confounding T and Y. The structural conditions are restrictive; in real DAGs the front-door criterion is satisfied less often than one might hope. When it applies, it is exact.

**Instrumental variables.** A variable Z that affects T but does not affect Y except through T (and is not confounded with Y) can be used to estimate the causal effect even under unmeasured U. The mechanism is different from backdoor adjustment — instruments do not block paths, they isolate a portion of the variation in T that is *exogenous*. This book does not teach instrumental variables in depth — TIKTOC Part 14 places them outside scope. Read Scott Cunningham's *Causal Inference: The Mixtape* Chapter 7 ([Cunningham 2021](https://mixtape.scunning.com/)), or Hernán and Robins *Causal Inference: What If* Chapters 16–17 ([Hernán and Robins 2020](https://miguelhernan.org/whatifbook)).

**Negative controls.** Variables that, under the assumed DAG, should be unaffected by treatment or should not affect outcome. Detecting non-null effects on negative controls reveals unmeasured confounding. Diagnostic, not identifying. Lipsitch, Tchetgen Tchetgen, and Cohen 2010 *Epidemiology* ([Lipsitch et al. 2010](https://doi.org/10.1097/EDE.0b013e3181d61eeb) `[verify-DOI]`).

**Sensitivity analysis.** Rather than asking "is the effect identifiable?" ask "how strong would the unmeasured confounding have to be to change the conclusion?" The E-value, from Tyler VanderWeele and Peng Ding in *Annals of Internal Medicine* 2017 ([VanderWeele and Ding 2017](https://doi.org/10.7326/M16-2607)), operationalizes this. Chapter 14 teaches it properly.

Each is a different route. None universal. Each with its own assumptions.

One note on the **Generalized Adjustment Criterion**: Shpitser, VanderWeele, and Robins's 2010 UAI paper ([Shpitser, VanderWeele, Robins 2010](https://event.cwi.nl/uai2010/papers/UAI2010_0162.pdf) `[verify-URL]`) defines a more general adjustment criterion handling cases the backdoor criterion does not — including situations where conditioning on certain descendants of treatment can yield valid adjustment. DAGitty's `adjustmentSets()` uses it by default. When a tool suggests a non-obvious adjustment set, the Generalized Adjustment Criterion is likely what the tool is using.

---

## 8. Integration — The identification toolkit, complete

You have, by the end of this chapter, the conceptual machinery of the identification layer. To consolidate:

You can read a DAG, trace a path, name what an arrow means. You know the three failure modes from Chapter 4 — wrong variables, wrong functional form, wrong conditioning. You know what a confounder is *structurally* (Chapter 5), what a mediator is and why not to adjust for one (Chapter 6), what a collider is and what conditioning on one opens up (Chapters 7–8), and the backdoor criterion as both conditions complete (Chapter 9). You know that among valid adjustment sets smaller is usually better — variance, structural risk, operational fragility — and you computed the variance comparison concretely. You know that some causal effects cannot be identified from observational data, that the verdict is structural rather than statistical, that more data does not dissolve the problem, and that the verdict is the output of the Shpitser-Pearl ID algorithm. You know the verdict is a result, not a failure. You know partial identification produces bounds, you computed one with no assumptions, and you saw what tightening with assumptions looks like. You know the other escapes — interventional data, front-door, instruments, negative controls, sensitivity analysis — exist, and where to read them properly.

What is left? Two things.

**Defense.** The DAG you draw, the adjustment set you pick, the variables you exclude, the non-identifiability you name — all of these are domain claims. They are not algorithmic outputs. Chapter 11 is on defending them to a hostile audience, in both registers: a methodologist will read your DAG and try to break it; a VP will read your conclusions and ask "can I make this decision based on this?" Both audiences need their answer.

**Specification.** The DAG, the adjustment set, the assumptions, and the named non-identifiabilities have to be communicated, formally, to the causal-AI tool that will run the estimation downstream — and the tool takes specification *literally*. Chapter 12 is the specification document, with the "do-not-add" list as the formal artifact built from Chapters 6, 7, and 10. Chapter 13 is reading the tool's output critically. Chapter 14 is qualifying the conclusion under sensitivity analysis. The terminal deliverable in Chapter 15 ties them together.

You have the toolkit. You have the honest move. Act Two closes here.

---

## 9. Worked example — A non-identifiability report

Let me show you what an honest non-identifiability finding looks like as a deliverable. Imagine you are a senior data scientist at a healthcare platform. The question your VP wants answered: does enrolling diabetic patients in our new app-based coaching program reduce their HbA1c six months later? You have a year of observational data: enrollment status, baseline HbA1c, age, sex, insurance type, primary-care provider ID, and six-month HbA1c.

You build a DAG. You think it through with the clinical lead. The candidate confounders you identified: baseline disease severity (proxied imperfectly by baseline HbA1c), age, comorbidity burden (partially captured by insurance type as a crude proxy), and *motivation to manage one's disease*. The last variable is the one the clinical lead names but the data does not capture. Motivation affects both whether a patient enrolls in the coaching program (motivated patients self-select in) *and* whether their HbA1c improves (motivated patients are doing other things, separately from the program, that improve their numbers).

You run the analysis. The minimal valid adjustment set on observed variables is {baseline HbA1c, age, insurance type}. After conditioning, the residual backdoor path T ← motivation → Y is open. The Shpitser-Pearl algorithm returns: not identifiable.

The naive analysis — adjusting only for observed variables and reporting a point estimate — would produce a number. The number would attribute to the coaching program a portion of the improvement that actually came from motivation, which the program neither created nor controlled. The VP, reading the point estimate, would over-estimate the program's value. The decision to expand the program would be based on a wrong premise. Six months later, when the expanded program produced smaller effects in the broader population — because the expansion drew in less-motivated patients — the team would scramble for an explanation. The explanation was on the DAG the whole time.

The honest report looks like this:

> **Causal Effect Estimate of App-Based Coaching Program on Six-Month HbA1c**
>
> **Finding: Effect is not identifiable from currently available observational data.**
>
> The treatment-outcome relationship is confounded by patient motivation — a variable that influences both program enrollment (motivated patients self-select in) and outcome (motivated patients independently improve their HbA1c through other means). Motivation is not captured in our data pipeline.
>
> Under the no-assumptions bounds (Manski 1990), the ATE on HbA1c lies in [−1.8, +1.1] percentage points. Under the additional assumption that the program does not harm patients (monotone treatment response), the bounds tighten to [−0.4, +1.1]. The bounds contain zero. The data, even under the monotone-response assumption, does not distinguish "the program meaningfully reduces HbA1c" from "the program has no effect."
>
> **Routes to identification:**
> - A randomized pilot (50% of new diabetic patients randomly offered enrollment) would break the motivation confound at the design level and produce a point estimate. Estimated cost: $X over six months. Estimated sample size for adequate power: N.
> - A validated motivation instrument administered at intake (PAM-13 or similar) would convert motivation from an unmeasured to a measured variable, and allow inclusion in the adjustment set. Estimated implementation cost: $Y. Requires intake-flow change.
> - A sensitivity analysis (Chapter 14) can characterize how strong the unmeasured-motivation confounding would have to be to overturn any apparent program effect. We recommend this as the immediate next step.
>
> **Recommendation:** Defer the decision to expand the coaching program until one of the three routes has been pursued. The honest answer to the question as posed is that current data does not support either the "expand" or "do not expand" decision. We can produce decision-relevant evidence within six months under any of the three routes.

That is the deliverable. It is not a number. It is a structured set of statements about what the data can and cannot say, what the alternative routes are, and what cost each route carries. The VP, reading this, has been given the materials to make a real decision — including the decision *not* to commit to a program based on inadequate evidence. The analyst has done the analysis honestly. Nobody has been told the program works when the data does not support that claim. Nobody has been told it does not work when the data does not support that claim either. The deliverable is calibrated to what is known.

Chapter 11 is going to teach you how to defend a deliverable like this against the inevitable pushback ("can't you just give us a point estimate?"). For now, hold onto the shape of the document. This is what a non-identifiability finding looks like when the analyst takes it seriously.

---

## 10. Chapter summary

A minimal valid adjustment set is the smallest set that blocks every backdoor path between treatment and outcome — "smallest" in the lattice sense, meaning no variable can be removed without losing validity. DAGs frequently admit several minimal sets; the procedural answer comes from the van der Zander, Liśkiewicz, and Textor algorithm and is implemented in standard tooling. Among valid sets, smaller is usually preferable for three reasons that operate at three different levels: statistical (variance), structural (collider risk), and operational (pipeline fragility). The Henckel–Perković–Rotnitzky–Robins efficient-adjustment-set theory complicates "smaller is better" with a more refined variance argument, which the engineering reader should know exists.

Some causal effects are not identifiable from observational data, given the DAG. The Shpitser-Pearl ID algorithm makes this a sharp, finite-time verdict. Non-identifiability is a structural property of the question and the graph; it does not respond to sample size, model class, or analytical effort. It is also not a failure mode of the analysis — it is the analysis succeeding at the task of trust assessment, returning the verdict the structure requires. The honest analytical output is the verdict plus the routes out: interventional data, partial identification, front-door adjustment (when applicable), instruments (when defensible), negative controls (as diagnostic), and sensitivity analysis (as quantitative companion).

Partial identification, in the Manski tradition, replaces a point estimate with a range of values consistent with the data and the assumptions. The bounds widen or narrow as assumptions are added or relaxed. The output is decision-relevant when narrow and informative when wide. Either way, the output is honest about what the analysis can support.

The student arriving at "this effect is not identifiable from my data" has produced a result. They have not failed to produce one.

---

## 11. Bridge to Chapter 11

Everything you have built so far — the DAG, the adjustment set, the named confounders, the named non-identifiabilities — is a set of claims. Each claim has to be defended. The DAG has to be defended to a methodologist who will look at every arrow and ask "why that direction?" The adjustment set has to be defended to a peer who will ask "why these and not others?" The non-identifiability has to be defended to a VP who will ask "but can't you just give me a number?" Chapter 11 is the chapter on defending what you built — in two registers, to two audiences, with two different shapes of pushback. The toolkit is built. Now you learn to argue for it.

---

## 12. Exercises

### Warm-up

**Exercise 10.1 — Find the minimal set.** Consider the DAG with nodes T, Y, A, B, C, D, E and arrows: A → T, A → Y, B → T, B → C, C → Y, D → A, D → Y, E → Y (E is not connected to T except through any path you can find — check carefully). Treatment is T, outcome is Y. (a) List every backdoor path from T to Y. (b) List every minimal valid adjustment set. (c) Identify any variables that are *not* in any minimal set, and classify each as a non-confounder, an irrelevant noise variable, or a member of a non-minimal valid superset.

**Exercise 10.2 — Identifiability verdict.** Consider the DAG with nodes T, Y, Z, U, where U is unmeasured. The arrows are U → T, U → Y, Z → T, Z → Y, and T → Y. (a) State whether the causal effect of T on Y is identifiable from observational data on T, Y, and Z. (b) Justify your answer in two sentences. (c) State the verdict if U *were* measured. What changes?

### Application — Part A (any domain)

**Exercise 10.3 — Domain scenario, with and without data.** You are evaluating a new employee training program at a mid-sized company. Treatment: enrollment in the program. Outcome: performance review score six months later. The HR team can give you: pre-training performance review, department, tenure, manager ID, and a "manager-rated motivation" score that the manager assigned at the same time as the enrollment decision. (a) Draw a candidate DAG. Name at least one plausible unmeasured confounder. (b) Identify the minimal valid adjustment set on observed variables. (c) State whether the effect is identifiable. If not, specify (i) what data collection would close the open backdoor path and (ii) what randomized design would also work, and compare the two options on cost and timeline.

### Application — Part B (your own field)

**Exercise 10.4 — Identifiability in your own domain.** Pick a causal question you actually face in your work, your research, or your studies. (a) State the treatment, the outcome, and the population. (b) Draw the DAG to the best of your domain knowledge. (c) List the variables your field actually collects. (d) Determine whether the effect is identifiable from the data your field collects. (e) If not, name the specific unmeasured variable that is the source of non-identifiability. Be specific. "Unmeasured confounding" is not an answer; "patient adherence behavior, which is not captured in our clinical-decision-support pipeline" is an answer.

### Synthesis

**Exercise 10.5 — Unlock identification by design.** Pick a non-identifiable scenario (from Exercise 10.3, 10.4, or one of the chapter's worked examples). Specify, in writing: (a) what data collection — interventional, instrumental, or measurement — would unlock identification; (b) what the cost and timeline of that data collection would be in your setting; (c) what the deliverable would look like under each route. Present the result as a two-paragraph memo to a non-technical decision-maker.

### Challenge

**Exercise 10.6 — Read a published claim.** Pick a recent observational-data paper in your field that reports a causal estimate. (a) Reconstruct the DAG you believe the authors are implicitly assuming. (b) Identify their adjustment set, as reported in the methods section. (c) Determine whether their adjustment set is minimal, larger-than-minimal-but-valid, or *invalid* (contains a mediator, collider, or descendant). (d) Determine whether their effect is identifiable from observational data under the DAG you reconstructed. (e) Write a one-paragraph methodological note suitable for a referee report, naming any concerns with calibrated language. (f) If you found their analysis defensible, say so plainly. The exercise is graded on the honesty of the assessment, not on the verdict.

---

## 13. LLM exercise

The exercise: get an LLM to compute the minimal adjustment set for a specific DAG, then verify the answer and identify any place the LLM is wrong.

**Prompt to paste into Claude, ChatGPT, or Gemini:**

> I have a directed acyclic graph with the following edges:
> A → T
> A → Y
> B → T
> B → Y
> T → M
> M → Y
> C → A
> C → Y
> D → C
>
> The treatment is T. The outcome is Y. I want to estimate the total causal effect of T on Y.
>
> (1) List every backdoor path from T to Y.
> (2) List every minimal valid adjustment set.
> (3) Identify any variable that should never appear in the adjustment set, and explain why for each.
> (4) Determine whether the total causal effect of T on Y is identifiable from observational data on the variables A, B, C, D, M, T, and Y. Justify your answer.
>
> Show your reasoning step by step. Do not skip steps.

After the LLM responds:

1. Verify each backdoor path it listed. Did it miss any? Did it list any that are not actually backdoor paths (for instance, paths that start with T → rather than T ←)?
2. Verify each minimal set. For each set the LLM offered, can you remove a variable and still block every backdoor path? If yes, the set was not minimal — the LLM gave you a *valid* set but mislabeled it as minimal.
3. Check whether the LLM correctly excluded M (mediator on T → M → Y).
4. Check the identifiability verdict. If the LLM said "identifiable" or "not identifiable," is its reasoning structural or statistical? Sometimes LLMs slide into "with enough data we can estimate it" — which is the failure mode this chapter exists to refute.
5. Write a one-paragraph note on where the LLM was correct, where it was wrong, and where it gave a confident-sounding answer that did not match the structural definition of identifiability. Submit the note as your exercise deliverable.

A note on what to expect: current models (Claude 3.5 / 4 family, GPT-4o and successors, Gemini 1.5 / 2 family) are generally reliable on the backdoor-path enumeration for small DAGs and somewhat less reliable on minimality (they often produce valid sets and call them minimal without checking the lattice property). They are inconsistent on identifiability verdicts when an unmeasured variable is in the graph, because the structural-versus-statistical distinction is one of the places their training data is genuinely ambiguous. The LLM is fast and useful for the procedural parts of this work. It is not yet a substitute for the structural judgment the chapter has been building.

---

## 14. AI Use Disclosure

This chapter was drafted with the assistance of Claude (Anthropic), using the Feynman-voice pedagogical scaffold defined in the workshop's CLAUDE.md and the chapter-specific pantry notes prepared for Chapter 10 of *Causal Reasoning: Irreducibly Human*. Every primary source cited was checked against its original venue; citations flagged `[verify]` are pending Nik's review. The LLM exercise in section 13 was designed to be run by the student against current chatbot models; the chapter's author has run it against Claude (version family 4) and the qualitative description of where current models succeed and fail reflects that testing.

---

## 15. Part B bonus

If you completed Exercise 10.4 (identifiability in your own domain) and arrived at "not identifiable," do this: write a one-page memo to the most senior person in your organization who is making a decision based on the answer to your causal question. The memo should follow the structure of the worked example in Section 9. State the finding. Name the source of non-identifiability. List the routes to identification with cost estimates. Make a recommendation. Bring the memo to office hours.

If you completed Exercise 10.4 and arrived at "identifiable" — congratulations, and submit the DAG with annotations on every backdoor-blocking variable. Office hours will ask whether the DAG is *actually* identifiable or whether it merely looks identifiable because you have not yet named all the unmeasured confounders.

---

## 16. Key terms

- **Minimal valid adjustment set.** A set of observed variables satisfying the backdoor criterion, such that no proper subset is also valid. Minimality is a lattice property, not a cardinality property. (Sections 2, 8.)
- **Non-identifiability from observational data.** The property of a DAG and a causal query such that no procedure can estimate the query from observations of the available variables alone, regardless of sample size. A structural property, not a statistical one. (Sections 4, 5.)
- **Shpitser-Pearl ID algorithm.** A complete, finite-time algorithm that returns either an explicit formula for the causal query in terms of observational probabilities (identifiable) or the verdict "not identifiable" (Shpitser and Pearl 2008). (Section 4.)
- **Partial identification.** An analytical framework — Manski 1990 onward — that produces a range of values consistent with the data and the maintained assumptions, used when point identification fails. (Section 6.)
- **No-assumptions bounds.** The widest possible bounds on a causal effect, given only the observed marginal and conditional distributions, with no substantive assumptions about the confounding structure. (Section 6.)
- **Generalized Adjustment Criterion.** Shpitser, VanderWeele, and Robins's 2010 extension of the backdoor criterion to a broader class of adjustment sets, including some sets containing descendants of treatment. (Section 7.)
- **Efficient adjustment set.** The graphical construction (Henckel et al. 2022) that minimizes estimator variance among valid adjustment sets in linear causal models. Not always equal to a minimal adjustment set. (Section 3.)
- **Front-door adjustment.** Pearl's 1995 alternative identification strategy that recovers a causal effect through a fully mediating observed variable, even when the direct backdoor path through an unmeasured U cannot be closed. (Section 7.)
- **Sensitivity analysis (preview).** A quantitative companion to non-identifiability findings: how strong would the unmeasured confounding have to be to overturn the conclusion? Chapter 14. (Section 7.)

---

## 17. Further reading

- Judea Pearl, *Causality: Models, Reasoning, and Inference*, 2nd edition (Cambridge University Press, 2009), Chapter 3. The canonical statement of the backdoor and front-door criteria, with worked examples.
- Ilya Shpitser and Judea Pearl, "Complete Identification Methods for the Causal Hierarchy," *Journal of Machine Learning Research* 9 (2008), 1941–1979. The ID algorithm.
- Benito van der Zander, Maciej Liśkiewicz, and Johannes Textor, "Constructing Separators and Adjustment Sets in Ancestral Graphs," *UAI* 2014. The polynomial-time algorithm for enumerating minimal adjustment sets.
- Lars Henckel, Emilija Perković, Andrea Rotnitzky, and James M. Robins, "Graphical criteria for efficient total effect estimation via adjustment in causal linear models," *Journal of the Royal Statistical Society B* (2022). The efficient-adjustment-set theory. Read after the chapter, not before.
- Charles F. Manski, "Nonparametric Bounds on Treatment Effects," *American Economic Review* 80(2) (1990), 319–323. The foundation of partial identification. Short and worth reading in full.
- Miguel A. Hernán and James M. Robins, *Causal Inference: What If* (Chapman and Hall/CRC, 2020). Chapters on bounds (3), instruments (16), and unmeasured confounding throughout. Freely available online.
- Scott Cunningham, *Causal Inference: The Mixtape* (Yale University Press, 2021), Chapter 7. Instrumental variables for the engineering reader.
- Ilya Shpitser, Tyler J. VanderWeele, and James M. Robins, "On the Validity of Covariate Adjustment for Estimating Causal Effects," *UAI* 2010. The Generalized Adjustment Criterion.
- Tyler J. VanderWeele and Peng Ding, "Sensitivity Analysis in Observational Research: Introducing the E-Value," *Annals of Internal Medicine* 167(4) (2017), 268–274. The E-value, in advance of Chapter 14.
- Johannes Textor, *Drawing and Analyzing Causal DAGs with DAGitty*, manual v3.x (2023). The practical tool.

---

## 18. Draft flags

The following items in this chapter were flagged for verification during drafting and remain pending Nik's review:

- The van der Zander–Liśkiewicz–Textor 2014 UAI paper has an extended journal version in *Artificial Intelligence* (vol. 270, 2019). The exact pagination is `[verify]`.
- Frake (2025), *Strategic Management Journal*, on partial identification in strategic management research — exact issue and DOI `[verify]`.
- Tan et al. (2024), "Consistency of Neural Causal Partial Identification," NeurIPS 2024 — arXiv link is provided; final proceedings citation `[verify]`.
- Duarte et al. (2024) on automated causal inference in discrete settings — exact journal and date `[verify]`.
- Pearl 1995 *Biometrika* URL — the URL provided is a hosted PDF; canonical journal access is at the *Biometrika* page `[verify-URL]`.
- Lipsitch et al. 2010 *Epidemiology* DOI `[verify]`.
- Shpitser, VanderWeele, Robins 2010 UAI URL `[verify]`.
- The Team Pricing opening case is a structurally accurate but anonymized composite drawn from the pantry's "supply-chain process change with capacity confounding" and "pricing analysis with limited control set" cases. No specific company is named. Public-facing post-mortems of similar events exist but are typically anonymized; the chapter uses the structurally accurate illustrative form rather than name a specific firm.

---

## What would change my mind

If the engineering field develops a tool that reliably identifies, for an arbitrary DAG, *both* the minimal valid adjustment set *and* a defensible domain-aware judgment about whether the unmeasured-confounder assumptions hold — that is, if domain judgment about the realism of the DAG itself becomes algorithmically replaceable — then the chapter's framing of identification as the layer requiring human judgment would need revision.

## Still puzzling

I do not yet have a clean account of when the efficient adjustment set (Henckel et al. 2022) is large enough to overturn the minimal-set default in practice for engineering applications. The theory is precise; the engineering rule of thumb for *when to deviate* is still something I am working out chapter by chapter.

---

**Tags:** minimal-adjustment-set, non-identifiability, partial-identification, Manski-bounds, identification-layer
