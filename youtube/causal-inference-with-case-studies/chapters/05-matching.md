═══════════════════════════════════════
FORMATTED VERSION (Markdown)
═══════════════════════════════════════

# Chapter 5: Matching


## TL;DR

- ═══════════════════════════════════════ FORMATTED VERSION (Markdown) ═══════════════════════════════════════.
- The chapter moves through A question I can't answer in a laboratory, What you'll be able to do by the end of this chapter, What you should already have, What matching is really doing, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

## A question I can't answer in a laboratory

Here's a question. Does smoking ruin your gums?

Yes, I know. Smoking is bad for you. Everyone knows that. But pretend for a minute you're a dentist, and a patient walks in and asks you specifically: *how bad, exactly, is smoking for my gums? If I quit, will my gums heal? Compared to what?* You need a number. And you need to know if the number is any good.

The standard way to produce a trustworthy number in medicine is to run a randomized controlled trial. Flip a coin, smoker or non-smoker, wait twenty years, measure the gums. Randomization is magic — it forces the smoking group and the non-smoking group to be identical, on average, in every way except the smoking. When you compare their gums, the only thing that could possibly explain the difference is the smoking itself.

You cannot run this trial. No ethics board will approve it. No patient will volunteer. The trial is impossible, full stop. And yet the question is real, and the answer matters.

So I use what I have. A survey — the U.S. National Health and Nutrition Examination Survey, 2011–2012, which sent people to dentists and recorded what those dentists found. Among the adults who got the full periodontal exam, there were 441 daily smokers and 1,506 people who had never smoked. Good sample.

I compute the thing I care about. Smokers have, in this data, roughly *ten times* the median percentage of diseased gum sites as non-smokers. Not twenty percent more. Not double. Ten times.

Now I am tempted to stop right here and print the anti-smoking posters.

Don't stop. Here's the problem.

The smokers in this data are not the same people as the non-smokers in this data. The smokers are more often male, less educated, lower-income, and younger. Each of these things independently affects gum disease. Men tend to have worse gums. People with less access to dental care have worse gums. The ten-times gap is smoking's effect *plus* all these other effects, cooked together into one number I cannot read.

What I want is a fair comparison. Each smoker, paired with a non-smoker who looks — on paper — just like the smoker. Same age. Same sex. Same education. Same income. Then I compare the pair. The two people in the pair differ in whether they smoke; they don't differ much in anything else. So whatever gap remains between their gums must, mostly, come from the smoking.

This is what matching is. That's the whole idea. The rest of the chapter is about how to do it fairly, how to check whether you did it right, and how to recognize when you cannot do it at all.

### What you'll be able to do by the end of this chapter

- **Explain** what matching is trying to do, in terms of what a randomized trial would have given you.
- **Apply** the propensity score — the single most important idea in applied matching — and explain *why* matching on one number can do the work of matching on ten.
- **Execute** a matching analysis: choose a distance, pick an algorithm, match, check balance, and estimate the treatment effect.
- **Diagnose** when matching has worked and when it has quietly failed, using standardized mean differences and overlap checks.
- **Perform** a sensitivity analysis for unmeasured confounding, and interpret what Γ values mean about the robustness of your result.
- **Recognize** the three ways matching can fail — hidden confounders, no overlap, and wrong causal diagram — and know which one you're looking at.

### What you should already have

You should have Chapter 3 (confounding, the back-door criterion, adjustment by stratification) and Chapter 4 (regression adjustment, the overlap problem). Matching is not a new idea — it is the back-door criterion again, with a different computational strategy. If the phrase "back-door path" doesn't instantly mean something to you, review Chapter 3. The rest of this chapter will make much more sense if it does.

---

## 1. What matching is really doing

Let me restate what I just said, but more carefully. Because I think there's a way to hear "matching" and assume it's doing something magical, and it isn't doing anything magical. It's doing one simple thing.

Here's what a randomized trial gives you. You flip a coin. The coin doesn't know anything about the person. It doesn't know their age or their sex or their income. So when the coin lands, the people who get "smoke" and the people who get "don't smoke" are, on average, identical in every way — not because you made them identical, but because the coin wasn't paying attention to anything when it decided. Randomness produced *comparability* as a free side effect.

In observational data, there is no coin. Smokers decided to smoke for reasons. Those reasons correlate with everything else about them. So the smokers and non-smokers aren't comparable — they differ systematically, in ways we can sometimes see and sometimes cannot.

Matching is an attempt to *manufacture* the comparability that randomization would have given you for free. For each smoker, I go find a non-smoker who looks like the smoker. I pair them. I throw away the non-smokers I didn't use. Now I have two groups — 441 smokers and 441 hand-picked non-smokers — that look similar on the variables I matched on. If I matched on everything that matters, the two groups are now, roughly, as comparable as they would have been after randomization.

That's the idea. It's not clever. It's almost embarrassingly simple.

**What makes it hard is the phrase "everything that matters."** Matching only adjusts for the variables you explicitly match on. If you match on age, sex, education, and income, you've handled those four things. If gum disease is also affected by stress, diet, or dental-floss habits — and if any of those things correlate with smoking — matching hasn't handled those, and your estimate is still biased.

This is the same story as Chapter 3. Matching is back-door adjustment with a different haircut. It inherits every limitation of back-door adjustment, including the big one: *you have to have measured the right variables.* Matching does not escape that requirement. It cannot. No observational method can.

I want to say this directly because I think people sometimes see matching, with its fancy-looking pairs and diagnostics, and assume it's a more powerful tool than regression or stratification. It isn't. It's the same tool, performing the same operation, with a different computational strategy. The reason to use matching instead of regression is not that matching is more powerful. It's that matching makes certain assumptions visible — and certain failures visible — that regression can hide.

I'll show you what I mean later. First, the mechanics.

### The wall we hit: why you can't just match on everything

Here's the obvious plan. I have a smoker. I want to find a non-smoker who matches on every variable I measured. Same age, same sex, same education level, same income, same race, same height, same blood pressure, same everything. Perfect twin, except for the smoking.

This is called *exact matching*, and for two or three categorical variables it actually works. Say you have treatment and you have sex (two values) and grade in school (four values) and a GPA category (four values). That's 2 × 4 × 4 = 32 buckets. You look in bucket #1 and find the treated and untreated people there. Then bucket #2. And so on. If every bucket has some of each, you can match everyone.

Now add age, measured in years (say, 0 through 100). That's 101 new values. Your 32 buckets become 3,232 buckets. Now add income, measured to the nearest dollar. Add blood pressure. Add BMI.

You're not going to find a 47-year-old college-educated white non-Hispanic male with BMI 26.1 and blood pressure 132/85 and income $62,400 in your control group. Not now, not ever. He doesn't exist. Your exact-match bucket is empty.

This is the curse of dimensionality, and it shows up everywhere in statistics. When you have lots of variables, the space of possible combinations becomes so big that every individual person is in their own bucket, and there's no one to match them to.

So we give up on exact matching and move to *approximate* matching. Instead of demanding that the match be identical, we demand that the match be *close*. How close? We need a way to measure it. That's the next thing.

---

## 2. The central trick: the propensity score

If I have ten variables, I need to measure whether two people are "close" in ten-dimensional space. That's what a *distance metric* does. The standard choice is called Mahalanobis distance, after Prasanta Chandra Mahalanobis, an Indian statistician who worked it out in the 1930s. You can think of Mahalanobis distance as Euclidean distance — the usual Pythagoras-style measure — with two corrections.

First, it standardizes each variable by its variance. So a one-unit difference in age and a one-unit difference in income don't compete on raw scale; they compete on how *unusual* that difference is. Second, it accounts for correlations between variables. If age and income are correlated — older people earn more on average — then matching closely on age already partially matches on income, and Mahalanobis distance doesn't double-count.

Fine. You compute Mahalanobis distance between each smoker and each non-smoker, and you pair them up. This works. It's been used for decades. But it has a problem, and the problem is still the curse of dimensionality in disguise. With ten variables, you still have a ten-dimensional space, and finding genuinely close neighbors in ten dimensions is hard, even with a clever distance metric.

Now I want to show you the trick that changed everything. This is the 1983 paper by Paul Rosenbaum and Donald Rubin, "The Central Role of the Propensity Score in Observational Studies for Causal Effects." If you read only one paper on matching, read that one.

Here's the idea. Instead of matching on all ten variables at once, fit a model that predicts *treatment* from the variables. For each person, compute a single number — the probability that this person is a smoker, given everything we know about them. Call that number the *propensity score*.

<!-- LATEX: e(x) = P(\text{treatment} = 1 \mid X = x) -->

You can estimate it with any classifier. Logistic regression is the default. Fit a logistic model predicting "smoker or not" from age, sex, education, income, race. Each person gets a predicted probability. That's their propensity score.

Now match on *that one number.*

You might think: but we've thrown away all the information. We had ten variables and now we have one. How can matching on one number possibly do the work of matching on ten?

Here's what Rosenbaum and Rubin proved. **If two people have the same propensity score, they are exchangeable with respect to treatment, in the following sense: within that level of propensity, treatment is as good as random.**

Stop and think about what that means. If I find two people who have the same predicted probability of smoking — say, both had a 40% probability of being smokers given their age, sex, education, income — then the fact that *one of them actually smoked and the other didn't* is, statistically, indistinguishable from having flipped a coin. Their other characteristics must have been distributed similarly, on average, because the model said their smoking probabilities were the same.

This is the *balancing property*. Match on the propensity score alone, and — if the model is right — balance on all the underlying variables comes free. Ten-dimensional matching collapses to one-dimensional matching. The curse of dimensionality is partially broken.

### Why this works, told in a way I wish someone had told me

I remember when I first met this result, I thought: that can't be right. We have ten pieces of information about each person, and we're compressing it all into one number and claiming nothing's lost? Surely some information is lost.

Some information *is* lost. Just not the information we need for this particular job.

Here's the key. For causal inference, I don't need to match people who are identical. I only need to match people whose *treatment assignment process* looks identical. Two people with the same propensity score have the same probability of being assigned to treatment, given their covariates. That's all randomization ever gave us. Randomization didn't make the treated and control groups identical on every dimension — it just made their treatment assignment process identical (a coin flip, for everyone). Matching on the propensity score reproduces exactly that condition: treatment assignment, conditional on the score, is as good as random.

The propensity score is doing exactly what the coin flip does, after the fact. It is literally the observational version of randomization — but only on the variables in the model.

That last clause is important. **The balancing property holds for the *true* propensity score.** We do not observe the true propensity score. We observe an estimated one, from a model that might be wrong. If the model misses a non-linearity, an interaction, a key variable — the estimated score doesn't perfectly balance anymore, and matching on it leaves residual imbalance.

So the propensity score doesn't let you stop thinking. It lets you reduce a ten-dimensional matching problem to a one-dimensional matching problem, *conditional on your having built the right propensity score model.* If the model is wrong, you still have to fix it. You just fix it by looking at the balance it produces — which is what diagnostics are for.

### The design philosophy of the propensity score

Take a step back from the math. Ask: why did the field adopt this approach so universally?

The answer is a kind of pragmatism. Rosenbaum and Rubin didn't invent a new form of adjustment — they invented a computational convenience that made an existing form of adjustment feasible in regimes where it wasn't before. Before 1983, matching meant exact matching, or matching on a couple of variables with crude distance metrics. The curse of dimensionality was a real wall. After 1983, matching scaled to dozens of covariates at once, because you could compress them into a single dimension.

The cost of this convenience is that the single dimension is a model-based construction. Instead of a reviewer being able to inspect "this 52-year-old man was matched to that 52-year-old man," they now see "this person with propensity 0.43 was matched to that person with propensity 0.43," and they have to trust the propensity model that produced the 0.43s. More flexibility, less transparency.

That's the trade-off the field accepted, and it's been productive. But it means matching analyses require more diagnostic discipline than exact matching did. You need to show the reader not just the pairs, but the balance the pairs achieved. We'll get there in a moment.

---

## 3. How you actually do it

We have a distance — the propensity score, or Mahalanobis, or some combination. Now we need an algorithm that takes the distance and produces the matched pairs.

### Greedy matching and optimal matching

There are two main algorithms. Greedy matching, and optimal matching.

Greedy matching is what it sounds like. Start with the first treated person. Find their closest control. Pair them. Remove that control from the pool. Move to the next treated person. Find *their* closest control among whoever's left. Pair them. Continue until you run out of treated people or controls.

This is fast. On ten thousand individuals, it takes seconds. It's easy to implement. It's easy to explain. It's the default in most software.

It is also, strictly speaking, suboptimal. Here's why.

Imagine I have two smokers — smoker A and smoker B — and two non-smokers — control X and control Y. The distances look like this:

- A to X: 0.1 (very close)
- A to Y: 0.2
- B to X: 0.15 (also close)
- B to Y: 10.0 (not close at all)

Greedy matching processes A first. A's closest control is X (distance 0.1). Pair them. Now B has only Y left. B-Y distance is 10.0. Total distance across pairs: 0.1 + 10.0 = 10.1.

But consider the other pairing. Match A with Y (distance 0.2) and B with X (distance 0.15). Total distance: 0.35. Much better.

Greedy matching made the locally best choice for A and paid for it globally with a terrible match for B. Optimal matching looks at all possible pairings simultaneously and picks the one that minimizes total distance. It's a classical problem in operations research, and efficient algorithms exist for it.

Optimal matching gives better matches on average, at the cost of more computation. For data sets up to ten thousand or so, the extra computation is negligible and optimal matching is the better choice. For very large data sets, greedy matching's speed advantage may matter.

In practice, the two methods usually give similar results, because most treated individuals have many plausible controls and the ordering doesn't much matter. When they give different results, it's usually because the data are sparse — not many good matches to go around — and that's exactly when global thinking helps most. Most applied analyses default to greedy; careful ones check with optimal as a robustness check. The R package `MatchIt` does both; so do several Python implementations.

### The knobs you turn: one-to-one, one-to-many, replacement

Beyond the algorithm, there are several structural choices.

**One-to-one matching**: each treated person gets exactly one control. This is the simplest structure and the one most analogous to a paired randomized trial. The analysis is straightforward — paired t-tests, conditional logistic regression, the usual paired-sample tools.

**One-to-many matching**: each treated person gets *k* controls, where *k* might be 2, 5, or more. You use more of the control pool, and the extra matches reduce the statistical noise in the estimate. But the fifth-best match is a worse match than the first-best, so the average match quality drops. You're trading bias (worse matches) for variance (more data). When the control pool is big and good matches are easy to find, one-to-many helps. When good matches are hard, it hurts.

**Matching with replacement**: a single control can be matched to multiple treated individuals. This is useful when the control pool is small or weird — without replacement, you might exhaust your good controls and be forced to use bad ones. With replacement, every treated person gets their personal best control, but the same control now appears in multiple pairs, which creates statistical dependence you have to handle in the analysis.

**Matching without replacement**: each control is used at most once. The pairs are independent. The analysis is cleaner. This is the default.

Each knob trades off bias for variance in slightly different ways. There's no universal right answer. Applied researchers typically try several configurations and report the range of estimates. If the conclusion holds across configurations, that's evidence of robustness. If the conclusion changes depending on which matching scheme you use, that's evidence of fragility, and you should be suspicious of any single estimate.

### The calipers

Sometimes a treated individual has no good match. Their covariate values put them in a region of the space where no control exists nearby. If you force a match, you'll pair them with a control who isn't really similar, and that bad match contaminates the estimate.

A *caliper* is an upper bound on how far a match can be. If the nearest control is farther than the caliper, you don't match that treated person at all. You just drop them.

A standard caliper is 0.2 standard deviations of the logit of the propensity score. The specific number is a convention; the key point is to use *some* caliper and to report how many treated individuals you dropped because of it.

The cost of dropping people is that your analysis no longer applies to the full treated population — only to the subset who had available matches. If 10% of smokers are dropped because they're so unusual no non-smoker resembles them, your estimate is the effect of smoking *among the smokers who look like typical non-smokers.* That may or may not be what you wanted.

This is the overlap problem from Chapter 4, showing up again. Matching makes the overlap problem *visible*: the treated people you can't match are the ones outside the overlap region. Regression doesn't make this visible — it just extrapolates through the gap, quietly, without telling you. A matching analysis that drops 30% of its treated people is being honest about a problem that a regression analysis would have hidden.

That's the kind of thing I meant earlier about matching making assumptions visible that regression can hide.

### Balance diagnostics: the step you cannot skip

After matching, you have a matched sample. You now have to check whether the matching actually *worked*.

This is called balance diagnostics, and it is non-negotiable. A matching analysis without balance diagnostics is not a matching analysis — it's a hope that the matching worked, dressed up in the costume of a matching analysis. Every reviewer should demand these diagnostics. Every paper should report them.

The main diagnostic is the *standardized mean difference*. For each covariate, you compute:

<!-- LATEX: \text{SMD} = \frac{\bar{X}_{\text{treated}} - \bar{X}_{\text{control}}}{\text{pooled SD}} -->

That's the difference in means between the matched treated and matched control groups, divided by the pooled standard deviation. It's expressed in standard-deviation units, so you can compare across variables measured in different units.

The rule of thumb: SMD below 0.1 is good balance. Between 0.1 and 0.25 is marginal. Above 0.25 indicates the matching didn't do its job for that variable.

You compute the SMD for every variable you matched on, and you report both the pre-matching and post-matching values side by side. A successful matching reduces the SMDs across the board. A failed matching leaves some or all of them high. If the matching failed on some variables, you need to respecify the propensity score model — add interactions, add polynomial terms, add missing variables — and rematch, and recheck.

There are also visual diagnostics. Density plots of the propensity score in treated and control groups should overlap substantially after matching. If they don't, you don't have propensity-score balance, which means the matching hasn't reproduced the randomization condition. Q-Q plots can reveal distribution-shape imbalances that means-based diagnostics miss.

**Here is the single most important thing about balance diagnostics. You do them before you look at the outcome.** If you match, peek at the outcome, don't like what you see, and go back to respecify the propensity model, you are doing a form of p-hacking that will produce false-positive findings at much higher rates than nominal. The sequence must be: build the propensity model, match, check balance, refine if needed, freeze the matching — *then* look at the outcome. Once. No going back.

This discipline is the entire reason matching is seen as more credible than ad-hoc regression. If you don't observe the discipline, matching is not more credible.

### The analysis itself

Once you have a matched sample with acceptable balance, the outcome analysis is almost anti-climactic. You treat the matched sample like a randomized trial.

For a continuous outcome, you compute the difference in outcome means between the matched treated and matched control groups. For a binary outcome, the difference in rates, or an odds ratio, or a risk ratio, whichever fits your scientific question. Standard errors come from paired methods (paired t-test, Wilcoxon signed-rank, conditional logistic regression) or from clustered standard errors that respect the matched-set structure.

A common modern practice is to run a regression on the matched sample, including the matched-set identifier as a fixed effect, and read the treatment coefficient. This combines matching with regression adjustment, and the combination is more forgiving of small remaining imbalances than either method alone. It's called a *doubly robust* estimator when both a propensity model and an outcome model are used — the estimate is consistent if either model is correctly specified. This is a property worth buying.

The estimate you get is usually the *average treatment effect on the treated* — the effect of treatment on the specific people who received it. In one-to-one matching without replacement, this is what the matched comparison naturally yields. If you want the effect on the overall population, or the effect on the untreated, you need a different matching structure (or a different method). Be careful to state what effect you're estimating. Different effects answer different questions.

---

## 4. Putting it together, and the limits

Let me go back to smoking and gums and walk the whole pipeline.

I fit a propensity model: logistic regression of smoking status on age, sex, education, income, and race. Each of the 1,947 people gets a score — their estimated probability of being a smoker given their demographics. For each smoker, I find the non-smoker with the closest propensity score and pair them. I use a caliper — say, 0.2 standard deviations on the logit scale — and drop any smoker who has no non-smoker within that distance.

I check balance. Before matching, the standardized mean differences on my five variables range from maybe 0.3 to 0.5 — substantial imbalance. After matching, they're all below 0.1. Good. The matching worked.

Now I compare gum disease in the matched pairs. The ten-to-one raw gap shrinks — but doesn't vanish. The matched estimate says smokers have about three times the periodontal disease of comparable non-smokers. Most of the raw ten-fold gap was demographic noise. But three-fold remains, and that three-fold is the best estimate I have of smoking's causal contribution — *conditional* on having matched on the right variables.

So: is that three-fold estimate right?

This is where I have to be honest about what I don't know. I matched on five things. What about all the things I didn't measure? Stress levels. Diet. Oral hygiene habits. Frequency of dental visits. Genetics. If any of these things independently affects gum disease *and* correlates with smoking, my matching hasn't accounted for them, and my three-fold estimate is biased.

I have no way to measure the bias directly. I never will. The fundamental problem of observational causal inference is that you are adjusting for the variables you have, and hoping the ones you don't have don't matter too much.

### The escape hatch: sensitivity analysis

There is, however, a way to ask a different question. Instead of "is my estimate right?", I can ask: **how wrong would an unmeasured confounder have to be to overturn my result?** If the answer is "catastrophically wrong," the result is robust. If the answer is "a tiny bit wrong," the result is fragile.

This is sensitivity analysis. The most widely used version is Paul Rosenbaum's, which introduces a single parameter called Γ (gamma). Γ measures how much an unmeasured confounder U could distort treatment assignment beyond what the measured covariates explain.

Γ = 1 means no distortion — treatment given the covariates is effectively random. Γ = 2 means an unmeasured confounder could double the odds of treatment for one person over an otherwise-identical person. Γ = 5 means fivefold. And so on.

The sensitivity analysis asks: *at what value of Γ does my significant result become non-significant?*

If the answer is Γ = 1.1, my result is barely standing. Any plausible unmeasured variable could overturn it.

If the answer is Γ = 3, my result holds unless there's an unmeasured confounder with truly implausible strength — a variable that triples treatment odds for identical-looking people and hasn't been measured. That's not impossible but it's hard to make happen.

If the answer is Γ = 9 — which is roughly what Jerome Cornfield computed in his 1959 analysis of smoking and lung cancer — the result is practically bulletproof. An unmeasured confounder that increases smoking probability ninefold for otherwise-identical people is almost inconceivable. Cornfield's argument was a major step in convincing the medical establishment that the smoking-cancer link was causal, because it made the alternative (some mysterious unmeasured variable doing all the work) numerically absurd.

Sensitivity analysis does not prove the causal effect is real. It quantifies the size of the hidden bias you would need to invoke to explain it away. That's a service, and a valuable one. It makes your assumption visible and arguable.

Every matching analysis in a published paper should include a sensitivity analysis. When one is missing, you have a result without a known robustness; treat it provisionally.

### Matching and regression: cousins, not rivals

A common framing says matching is an alternative to regression. This framing is wrong.

Matching and regression are different computational strategies for the same operation — back-door adjustment. Regression fits a model that relates outcome to treatment and confounders, and reads the treatment coefficient. Matching constructs a sample in which the confounders are balanced, and reads the simple difference in outcomes. Both, applied correctly under the same causal diagram, give the same answer.

When they disagree, the disagreement is diagnostic. Regression imposes a functional form — linear, usually — on the relationship between outcome and covariates. If that functional form is wrong, regression is biased. Matching makes no functional-form assumption. When the matching and regression estimates diverge, the regression's functional form is likely misspecified.

Regression will also happily extrapolate into regions where it has no data, using its functional form to fill in. Matching won't. If a treated individual has no nearby control, matching drops them (with a caliper) or gives them a bad match (without one). The bad match shows up in balance diagnostics. The extrapolation in regression is invisible unless you specifically check for it.

These are not arguments for one method over the other. They're arguments for using both, and understanding what each assumes. A modern analysis often matches first to get a balanced sample, then runs a regression on the matched sample to make fine-grained corrections. This combined approach is doubly robust: you get the right answer if *either* the matching or the regression is right. It's a sensible default.

### What matching cannot do

Let me end this section with a hard list of what matching *cannot* do. This is important because matching's outputs look confident — nice clean pairs, clean estimates, clean standard errors — and it is easy to overbelieve them.

**Matching cannot create data that aren't there.** If some of your treated individuals have no comparable controls, you cannot match them. You can drop them (caliper matching) or accept bad matches (no caliper). Neither gives you the effect on the unmatchable individuals. Matching restricts your conclusions to the region of covariate space where overlap exists.

**Matching cannot adjust for unmeasured confounders.** I have said this six times in this chapter. I will say it more. Matching is back-door adjustment, and back-door adjustment requires that you have measured a sufficient set. If you haven't, matching fails, and it fails silently — the output looks identical to a successful analysis. Sensitivity analysis is the only way to quantify your exposure to this failure.

**Matching cannot tell you if your causal diagram is right.** The back-door criterion tells you what variables to match on *given* the diagram. If the diagram is wrong — if you're matching on a collider, or on a mediator, or missing a key confounder — matching will faithfully produce a biased estimate, and no amount of matching diagnostics will detect it. Balance diagnostics only check whether you balanced the variables you matched on. They cannot check whether those were the right variables.

**Matching cannot handle interference between units.** If my treatment affects your outcome — if a vaccinated person reduces the infection risk of their unvaccinated neighbor — the standard matching framework is invalid. It assumes that each person's outcome depends only on their own treatment. That assumption (Rubin's SUTVA, the stable unit treatment value assumption) is required for matching, for regression, for almost every method in this book. Interference is a genuinely hard problem, and it's still an active research area.

**Matching gives you the effect on the treated, not the effect on everyone.** If the treatment works differently on different kinds of people, the effect estimated by one-to-one matching without replacement is the effect on the people who received treatment, not the effect on some hypothetical randomly-chosen person. If you want the latter, you need a different matching structure or a different method.

These limitations are not unique failings of matching. Most of them apply to every back-door method. The virtue of matching is that some of its failures are visible — a matching that fails balance diagnostics or drops most of the treated population is obviously broken. Regression can fail in the same ways silently.

Which is the whole point. Choose matching when you want the failures to be visible.

---

## A note about AI

Matching is the methodology that looks rigorous and can fail invisibly. The model produces propensity-score code on request. The code will run; whether it has produced balance is a separate question.

Where the model genuinely helps: structuring the matching procedure — caliper, ratio, replacement, balance diagnostics — and producing the standard balance tables.

Where the model does damage: certifying that matching has produced balance on unmeasured confounders. By definition the model cannot check the unmeasured.

The rule: matching procedure from the model; the limits of what matching can adjust for from the analyst's substantive knowledge.

---

## Exercises

Solutions are not provided here. I want you to develop the instinct, and the instinct requires doing the work.

### Warm-up

**Exercise 5.1.** *(Objective: restate the matching idea in your own words)*  
Explain in three sentences what matching is trying to do, why it exists as an alternative to a randomized controlled trial, and what condition has to hold for it to work. Do this without using the phrase "propensity score."

**Exercise 5.2.** *(Objective: recognize exact matching's wall)*  
You have five binary covariates and three continuous covariates (age, income, BMI). Describe concretely why exact matching fails in this case, and estimate how many "buckets" you would need if you tried to discretize each continuous variable into ten bins.

**Exercise 5.3.** *(Objective: compute a standardized mean difference)*  
A matched sample has mean age 54.2 (SD 12.1) in the treated group and mean age 52.8 (SD 11.4) in the control group. Compute the standardized mean difference. Interpret: is this acceptable balance?

### Application

**Exercise 5.4.** *(Objective: apply the propensity score balancing property)*  
Explain why, if two individuals have the same *true* propensity score, the treatment assignment between them is as good as random — even if their individual covariates differ. Then explain why this property may fail for the *estimated* propensity score.

**Exercise 5.5.** *(Objective: choose between greedy and optimal matching)*  
Construct a small example (four treated, four controls) in which greedy matching produces a total distance noticeably larger than optimal matching. Identify the pair where greedy makes the "locally good but globally bad" choice.

**Exercise 5.6.** *(Objective: recognize an overlap problem)*  
You are estimating the effect of attending graduate school on lifetime earnings. Your treated group includes people with GRE scores from 320 to 340 (the top of the range). Your control group has GRE scores mostly between 250 and 310. Describe what happens under one-to-one matching without a caliper, and under one-to-one matching with a tight caliper. Which is more honest?

**Exercise 5.7.** *(Objective: diagnose a matching report)*  
A published paper reports a matched observational study of a new cancer drug. The paper reports the matched estimate and p-value but does not include balance diagnostics or a sensitivity analysis. List the specific things a reviewer should demand the authors add before the paper is publishable.

### Synthesis

**Exercise 5.8.** *(Objective: integrate propensity score and balance)*  
A researcher fits a logistic propensity score model using age, sex, and income, then matches and computes standardized mean differences. SMDs on age and sex drop below 0.1, but the SMD on income is still 0.27. What might have gone wrong with the propensity model? Name three specific respecifications to try, in order of what you'd try first.

**Exercise 5.9.** *(Objective: compare matching to regression on the same question)*  
Using any simulated or real dataset of your choice with a known treatment, an outcome, and at least four covariates, compute the treatment effect two ways: by OLS regression with the covariates as controls, and by propensity-score matching. Compare the estimates. Where they differ, propose a specific reason (functional form, overlap, interaction not in the regression) and test it by fitting a regression with the additional flexibility.

**Exercise 5.10.** *(Objective: interpret a sensitivity analysis)*  
A matched study reports a statistically significant effect with Γ sensitivity bound of 1.3 — meaning an unmeasured confounder that distorted treatment odds by 30% would overturn the result. Another study reports the same effect size with Γ = 4. Which result is more robust? Explain what the specific numbers mean about what an unmeasured confounder would look like.

### Challenge

**Exercise 5.11.** *(Objective: reason about a case matching cannot handle)*  
A study tries to estimate the effect of receiving a flu vaccine on infection rates, by matching vaccinated and unvaccinated individuals on demographics. Explain why the SUTVA assumption is violated here, and what that does to the matched estimate. Sketch one research design that could plausibly handle the interference (you may need to look up literature on interference or spillover effects).

**Exercise 5.12.** *(Objective: bring the chapter to a real problem)*  
Pick an observational study from your own field or from a news article making a causal claim. Identify: (a) the treatment, (b) the outcome, (c) the confounders the researchers adjusted for, (d) confounders you suspect they missed, (e) what a sensitivity analysis might show, and (f) whether you believe the reported effect is plausibly causal. Write a one-page critique suitable for submission as a journal referee report.

---

## Chapter summary

You walked in with back-door adjustment and stratification in hand. You walk out with a practical tool — matching — for doing the adjustment in the many-covariates regime where stratification breaks down.

You can now state what matching is trying to do: manufacture, after the fact, the comparability that randomization would have produced for free.

You can use the propensity score to collapse a multi-dimensional matching problem into a one-dimensional one, and you can explain *why* this collapse works — two people with the same propensity score are, within that level, exchangeable with respect to treatment.

You can execute the full pipeline: build a propensity model, match (greedy or optimal, one-to-one or one-to-many, with or without a caliper), check balance with standardized mean differences, and estimate the treatment effect on the matched sample.

You can run a sensitivity analysis and interpret what the Γ value says about how robust your result is to unmeasured confounding.

You can distinguish the three ways a matching analysis can fail: unmeasured confounders (handled by sensitivity analysis, not by matching itself), lack of overlap (handled by calipers, but at the cost of generalizability), and a wrong causal diagram (not handled by anything in matching — the diagram is an input, not an output).

**The one idea from this chapter that matters most.** Matching does not add power to observational causal inference. It exposes, more visibly than regression does, the places where the inference is weak — the treated individuals without comparable controls, the variables that won't balance, the estimates that crumble under mild unmeasured-confounding pressure. Prefer matching when you want to see the weakness. Prefer regression when you want to summarize quickly. Use both when the answer matters.

**The common mistake to watch for.** Using matching without balance diagnostics, without sensitivity analysis, or with a propensity model that was never checked for correct specification. Each of these mistakes turns matching into a dress-up version of the problem it was meant to solve. Matching *only* works when you do the diagnostics, and does less than claimed when you don't.

**The Feynman test.** Can you explain to a curious friend who hasn't read this chapter why matching on one number — the propensity score — does the same work as matching on ten? If yes, you understand the central trick. If not, go back to Section 2 and work through it until you can tell them without using any jargon beyond "probability of getting the treatment."

---

## Connections forward

The next chapter (Chapter 6) extends propensity-score methods in a different direction: *weighting.* Instead of pairing treated to controls, you weight each individual by the inverse of their propensity score, so that the weighted sample looks like a population in which treatment was assigned randomly. Weighting is the same idea as matching, expressed as arithmetic on all the data rather than as pairing. It has some efficiency advantages — it uses all the data, not just the matched subset — and some stability risks — when propensity scores get near 0 or 1, weights explode. You'll see when to reach for which.

Chapter 7 brings in *instrumental variables*, for the cases where the back-door criterion returns no valid adjustment set and no amount of matching or weighting can rescue you. The whole second half of this book is about what to do when the back door is closed — when some critical confounder is unmeasured and you need to find a different way to isolate the causal effect. Those later chapters build on the back-door intuition you now have, but they point to different doors.

One last thing. The methods in the next few chapters will get more abstract and more clever. Remember: the goal is always the same. You are trying to extract the causal effect from data that are contaminated by all the ways the world declines to randomize itself. Matching was the first tool that made this feasible at scale. Every tool after it is a variation on the same project.

---

═══════════════════════════════════════
SUBSTACK HTML (Copy-Paste Ready)
═══════════════════════════════════════

<!-- Manual steps needed:
  1. Insert LaTeX equations (marked <!-- LATEX: ... -->): 2 equations — propensity score definition, standardized mean difference formula
  2. No figures marked in this chapter — it is prose-dense. If you want a figure showing the greedy-vs-optimal matching example from Section 3, or a DAG illustrating the unmeasured-confounder threat, add them manually before publishing.
-->

<h2>Chapter 5: Matching</h2>

<h3>A question I can't answer in a laboratory</h3>

<p>Here's a question. Does smoking ruin your gums?</p>

<p>Yes, I know. Smoking is bad for you. Everyone knows that. But pretend for a minute you're a dentist, and a patient walks in and asks you specifically: <em>how bad, exactly, is smoking for my gums? If I quit, will my gums heal? Compared to what?</em> You need a number. And you need to know if the number is any good.</p>

<p>The standard way to produce a trustworthy number in medicine is to run a randomized controlled trial. Flip a coin, smoker or non-smoker, wait twenty years, measure the gums. Randomization is magic — it forces the smoking group and the non-smoking group to be identical, on average, in every way except the smoking. When you compare their gums, the only thing that could possibly explain the difference is the smoking itself.</p>

<p>You cannot run this trial. No ethics board will approve it. No patient will volunteer. The trial is impossible, full stop. And yet the question is real, and the answer matters.</p>

<p>So I use what I have. A survey — the U.S. National Health and Nutrition Examination Survey, 2011–2012, which sent people to dentists and recorded what those dentists found. Among the adults who got the full periodontal exam, there were 441 daily smokers and 1,506 people who had never smoked. Good sample.</p>

<p>I compute the thing I care about. Smokers have, in this data, roughly <em>ten times</em> the median percentage of diseased gum sites as non-smokers. Not twenty percent more. Not double. Ten times.</p>

<p>Now I am tempted to stop right here and print the anti-smoking posters.</p>

<p>Don't stop. Here's the problem.</p>

<p>The smokers in this data are not the same people as the non-smokers in this data. The smokers are more often male, less educated, lower-income, and younger. Each of these things independently affects gum disease. Men tend to have worse gums. People with less access to dental care have worse gums. The ten-times gap is smoking's effect <em>plus</em> all these other effects, cooked together into one number I cannot read.</p>

<p>What I want is a fair comparison. Each smoker, paired with a non-smoker who looks — on paper — just like the smoker. Same age. Same sex. Same education. Same income. Then I compare the pair. The two people in the pair differ in whether they smoke; they don't differ much in anything else. So whatever gap remains between their gums must, mostly, come from the smoking.</p>

<p>This is what matching is. That's the whole idea. The rest of the chapter is about how to do it fairly, how to check whether you did it right, and how to recognize when you cannot do it at all.</p>

<h4>What you'll be able to do by the end of this chapter</h4>

<ul>
  <li><strong>Explain</strong> what matching is trying to do, in terms of what a randomized trial would have given you.</li>
  <li><strong>Apply</strong> the propensity score — the single most important idea in applied matching — and explain <em>why</em> matching on one number can do the work of matching on ten.</li>
  <li><strong>Execute</strong> a matching analysis: choose a distance, pick an algorithm, match, check balance, and estimate the treatment effect.</li>
  <li><strong>Diagnose</strong> when matching has worked and when it has quietly failed, using standardized mean differences and overlap checks.</li>
  <li><strong>Perform</strong> a sensitivity analysis for unmeasured confounding, and interpret what Γ values mean about the robustness of your result.</li>
  <li><strong>Recognize</strong> the three ways matching can fail — hidden confounders, no overlap, and wrong causal diagram — and know which one you're looking at.</li>
</ul>

<h4>What you should already have</h4>

<p>You should have Chapter 3 (confounding, the back-door criterion, adjustment by stratification) and Chapter 4 (regression adjustment, the overlap problem). Matching is not a new idea — it is the back-door criterion again, with a different computational strategy. If the phrase "back-door path" doesn't instantly mean something to you, review Chapter 3. The rest of this chapter will make much more sense if it does.</p>

<hr>

<h3>1. What matching is really doing</h3>

<p>Let me restate what I just said, but more carefully. Because I think there's a way to hear "matching" and assume it's doing something magical, and it isn't doing anything magical. It's doing one simple thing.</p>

<p>Here's what a randomized trial gives you. You flip a coin. The coin doesn't know anything about the person. It doesn't know their age or their sex or their income. So when the coin lands, the people who get "smoke" and the people who get "don't smoke" are, on average, identical in every way — not because you made them identical, but because the coin wasn't paying attention to anything when it decided. Randomness produced <em>comparability</em> as a free side effect.</p>

<p>In observational data, there is no coin. Smokers decided to smoke for reasons. Those reasons correlate with everything else about them. So the smokers and non-smokers aren't comparable — they differ systematically, in ways we can sometimes see and sometimes cannot.</p>

<p>Matching is an attempt to <em>manufacture</em> the comparability that randomization would have given you for free. For each smoker, I go find a non-smoker who looks like the smoker. I pair them. I throw away the non-smokers I didn't use. Now I have two groups — 441 smokers and 441 hand-picked non-smokers — that look similar on the variables I matched on. If I matched on everything that matters, the two groups are now, roughly, as comparable as they would have been after randomization.</p>

<p>That's the idea. It's not clever. It's almost embarrassingly simple.</p>

<p><strong>What makes it hard is the phrase "everything that matters."</strong> Matching only adjusts for the variables you explicitly match on. If you match on age, sex, education, and income, you've handled those four things. If gum disease is also affected by stress, diet, or dental-floss habits — and if any of those things correlate with smoking — matching hasn't handled those, and your estimate is still biased.</p>

<p>This is the same story as Chapter 3. Matching is back-door adjustment with a different haircut. It inherits every limitation of back-door adjustment, including the big one: <em>you have to have measured the right variables.</em> Matching does not escape that requirement. It cannot. No observational method can.</p>

<p>I want to say this directly because I think people sometimes see matching, with its fancy-looking pairs and diagnostics, and assume it's a more powerful tool than regression or stratification. It isn't. It's the same tool, performing the same operation, with a different computational strategy. The reason to use matching instead of regression is not that matching is more powerful. It's that matching makes certain assumptions visible — and certain failures visible — that regression can hide.</p>

<p>I'll show you what I mean later. First, the mechanics.</p>

<h4>The wall we hit: why you can't just match on everything</h4>

<p>Here's the obvious plan. I have a smoker. I want to find a non-smoker who matches on every variable I measured. Same age, same sex, same education level, same income, same race, same height, same blood pressure, same everything. Perfect twin, except for the smoking.</p>

<p>This is called <em>exact matching</em>, and for two or three categorical variables it actually works. Say you have treatment and you have sex (two values) and grade in school (four values) and a GPA category (four values). That's 2 × 4 × 4 = 32 buckets. You look in bucket #1 and find the treated and untreated people there. Then bucket #2. And so on. If every bucket has some of each, you can match everyone.</p>

<p>Now add age, measured in years (say, 0 through 100). That's 101 new values. Your 32 buckets become 3,232 buckets. Now add income, measured to the nearest dollar. Add blood pressure. Add BMI.</p>

<p>You're not going to find a 47-year-old college-educated white non-Hispanic male with BMI 26.1 and blood pressure 132/85 and income $62,400 in your control group. Not now, not ever. He doesn't exist. Your exact-match bucket is empty.</p>

<p>This is the curse of dimensionality, and it shows up everywhere in statistics. When you have lots of variables, the space of possible combinations becomes so big that every individual person is in their own bucket, and there's no one to match them to.</p>

<p>So we give up on exact matching and move to <em>approximate</em> matching. Instead of demanding that the match be identical, we demand that the match be <em>close</em>. How close? We need a way to measure it. That's the next thing.</p>

<hr>

<h3>2. The central trick: the propensity score</h3>

<p>If I have ten variables, I need to measure whether two people are "close" in ten-dimensional space. That's what a <em>distance metric</em> does. The standard choice is called Mahalanobis distance, after Prasanta Chandra Mahalanobis, an Indian statistician who worked it out in the 1930s. You can think of Mahalanobis distance as Euclidean distance — the usual Pythagoras-style measure — with two corrections.</p>

<p>First, it standardizes each variable by its variance. So a one-unit difference in age and a one-unit difference in income don't compete on raw scale; they compete on how <em>unusual</em> that difference is. Second, it accounts for correlations between variables. If age and income are correlated — older people earn more on average — then matching closely on age already partially matches on income, and Mahalanobis distance doesn't double-count.</p>

<p>Fine. You compute Mahalanobis distance between each smoker and each non-smoker, and you pair them up. This works. It's been used for decades. But it has a problem, and the problem is still the curse of dimensionality in disguise. With ten variables, you still have a ten-dimensional space, and finding genuinely close neighbors in ten dimensions is hard, even with a clever distance metric.</p>

<p>Now I want to show you the trick that changed everything. This is the 1983 paper by Paul Rosenbaum and Donald Rubin, "The Central Role of the Propensity Score in Observational Studies for Causal Effects." If you read only one paper on matching, read that one.</p>

<p>Here's the idea. Instead of matching on all ten variables at once, fit a model that predicts <em>treatment</em> from the variables. For each person, compute a single number — the probability that this person is a smoker, given everything we know about them. Call that number the <em>propensity score</em>.</p>

<!-- LATEX: e(x) = P(\text{treatment} = 1 \mid X = x) -->

<p>You can estimate it with any classifier. Logistic regression is the default. Fit a logistic model predicting "smoker or not" from age, sex, education, income, race. Each person gets a predicted probability. That's their propensity score.</p>

<p>Now match on <em>that one number.</em></p>

<p>You might think: but we've thrown away all the information. We had ten variables and now we have one. How can matching on one number possibly do the work of matching on ten?</p>

<p>Here's what Rosenbaum and Rubin proved. <strong>If two people have the same propensity score, they are exchangeable with respect to treatment, in the following sense: within that level of propensity, treatment is as good as random.</strong></p>

<p>Stop and think about what that means. If I find two people who have the same predicted probability of smoking — say, both had a 40% probability of being smokers given their age, sex, education, income — then the fact that <em>one of them actually smoked and the other didn't</em> is, statistically, indistinguishable from having flipped a coin. Their other characteristics must have been distributed similarly, on average, because the model said their smoking probabilities were the same.</p>

<p>This is the <em>balancing property</em>. Match on the propensity score alone, and — if the model is right — balance on all the underlying variables comes free. Ten-dimensional matching collapses to one-dimensional matching. The curse of dimensionality is partially broken.</p>

<h4>Why this works, told in a way I wish someone had told me</h4>

<p>I remember when I first met this result, I thought: that can't be right. We have ten pieces of information about each person, and we're compressing it all into one number and claiming nothing's lost? Surely some information is lost.</p>

<p>Some information <em>is</em> lost. Just not the information we need for this particular job.</p>

<p>Here's the key. For causal inference, I don't need to match people who are identical. I only need to match people whose <em>treatment assignment process</em> looks identical. Two people with the same propensity score have the same probability of being assigned to treatment, given their covariates. That's all randomization ever gave us. Randomization didn't make the treated and control groups identical on every dimension — it just made their treatment assignment process identical (a coin flip, for everyone). Matching on the propensity score reproduces exactly that condition: treatment assignment, conditional on the score, is as good as random.</p>

<p>The propensity score is doing exactly what the coin flip does, after the fact. It is literally the observational version of randomization — but only on the variables in the model.</p>

<p>That last clause is important. <strong>The balancing property holds for the <em>true</em> propensity score.</strong> We do not observe the true propensity score. We observe an estimated one, from a model that might be wrong. If the model misses a non-linearity, an interaction, a key variable — the estimated score doesn't perfectly balance anymore, and matching on it leaves residual imbalance.</p>

<p>So the propensity score doesn't let you stop thinking. It lets you reduce a ten-dimensional matching problem to a one-dimensional matching problem, <em>conditional on your having built the right propensity score model.</em> If the model is wrong, you still have to fix it. You just fix it by looking at the balance it produces — which is what diagnostics are for.</p>

<h4>The design philosophy of the propensity score</h4>

<p>Take a step back from the math. Ask: why did the field adopt this approach so universally?</p>

<p>The answer is a kind of pragmatism. Rosenbaum and Rubin didn't invent a new form of adjustment — they invented a computational convenience that made an existing form of adjustment feasible in regimes where it wasn't before. Before 1983, matching meant exact matching, or matching on a couple of variables with crude distance metrics. The curse of dimensionality was a real wall. After 1983, matching scaled to dozens of covariates at once, because you could compress them into a single dimension.</p>

<p>The cost of this convenience is that the single dimension is a model-based construction. Instead of a reviewer being able to inspect "this 52-year-old man was matched to that 52-year-old man," they now see "this person with propensity 0.43 was matched to that person with propensity 0.43," and they have to trust the propensity model that produced the 0.43s. More flexibility, less transparency.</p>

<p>That's the trade-off the field accepted, and it's been productive. But it means matching analyses require more diagnostic discipline than exact matching did. You need to show the reader not just the pairs, but the balance the pairs achieved. We'll get there in a moment.</p>

<hr>

<h3>3. How you actually do it</h3>

<p>We have a distance — the propensity score, or Mahalanobis, or some combination. Now we need an algorithm that takes the distance and produces the matched pairs.</p>

<h4>Greedy matching and optimal matching</h4>

<p>There are two main algorithms. Greedy matching, and optimal matching.</p>

<p>Greedy matching is what it sounds like. Start with the first treated person. Find their closest control. Pair them. Remove that control from the pool. Move to the next treated person. Find <em>their</em> closest control among whoever's left. Pair them. Continue until you run out of treated people or controls.</p>

<p>This is fast. On ten thousand individuals, it takes seconds. It's easy to implement. It's easy to explain. It's the default in most software.</p>

<p>It is also, strictly speaking, suboptimal. Here's why.</p>

<p>Imagine I have two smokers — smoker A and smoker B — and two non-smokers — control X and control Y. The distances look like this:</p>

<ul>
  <li>A to X: 0.1 (very close)</li>
  <li>A to Y: 0.2</li>
  <li>B to X: 0.15 (also close)</li>
  <li>B to Y: 10.0 (not close at all)</li>
</ul>

<p>Greedy matching processes A first. A's closest control is X (distance 0.1). Pair them. Now B has only Y left. B-Y distance is 10.0. Total distance across pairs: 0.1 + 10.0 = 10.1.</p>

<p>But consider the other pairing. Match A with Y (distance 0.2) and B with X (distance 0.15). Total distance: 0.35. Much better.</p>

<p>Greedy matching made the locally best choice for A and paid for it globally with a terrible match for B. Optimal matching looks at all possible pairings simultaneously and picks the one that minimizes total distance. It's a classical problem in operations research, and efficient algorithms exist for it.</p>

<p>Optimal matching gives better matches on average, at the cost of more computation. For data sets up to ten thousand or so, the extra computation is negligible and optimal matching is the better choice. For very large data sets, greedy matching's speed advantage may matter.</p>

<p>In practice, the two methods usually give similar results, because most treated individuals have many plausible controls and the ordering doesn't much matter. When they give different results, it's usually because the data are sparse — not many good matches to go around — and that's exactly when global thinking helps most. Most applied analyses default to greedy; careful ones check with optimal as a robustness check. The R package <code>MatchIt</code> does both; so do several Python implementations.</p>

<h4>The knobs you turn: one-to-one, one-to-many, replacement</h4>

<p>Beyond the algorithm, there are several structural choices.</p>

<p><strong>One-to-one matching</strong>: each treated person gets exactly one control. This is the simplest structure and the one most analogous to a paired randomized trial. The analysis is straightforward — paired t-tests, conditional logistic regression, the usual paired-sample tools.</p>

<p><strong>One-to-many matching</strong>: each treated person gets <em>k</em> controls, where <em>k</em> might be 2, 5, or more. You use more of the control pool, and the extra matches reduce the statistical noise in the estimate. But the fifth-best match is a worse match than the first-best, so the average match quality drops. You're trading bias (worse matches) for variance (more data). When the control pool is big and good matches are easy to find, one-to-many helps. When good matches are hard, it hurts.</p>

<p><strong>Matching with replacement</strong>: a single control can be matched to multiple treated individuals. This is useful when the control pool is small or weird — without replacement, you might exhaust your good controls and be forced to use bad ones. With replacement, every treated person gets their personal best control, but the same control now appears in multiple pairs, which creates statistical dependence you have to handle in the analysis.</p>

<p><strong>Matching without replacement</strong>: each control is used at most once. The pairs are independent. The analysis is cleaner. This is the default.</p>

<p>Each knob trades off bias for variance in slightly different ways. There's no universal right answer. Applied researchers typically try several configurations and report the range of estimates. If the conclusion holds across configurations, that's evidence of robustness. If the conclusion changes depending on which matching scheme you use, that's evidence of fragility, and you should be suspicious of any single estimate.</p>

<h4>The calipers</h4>

<p>Sometimes a treated individual has no good match. Their covariate values put them in a region of the space where no control exists nearby. If you force a match, you'll pair them with a control who isn't really similar, and that bad match contaminates the estimate.</p>

<p>A <em>caliper</em> is an upper bound on how far a match can be. If the nearest control is farther than the caliper, you don't match that treated person at all. You just drop them.</p>

<p>A standard caliper is 0.2 standard deviations of the logit of the propensity score. The specific number is a convention; the key point is to use <em>some</em> caliper and to report how many treated individuals you dropped because of it.</p>

<p>The cost of dropping people is that your analysis no longer applies to the full treated population — only to the subset who had available matches. If 10% of smokers are dropped because they're so unusual no non-smoker resembles them, your estimate is the effect of smoking <em>among the smokers who look like typical non-smokers.</em> That may or may not be what you wanted.</p>

<p>This is the overlap problem from Chapter 4, showing up again. Matching makes the overlap problem <em>visible</em>: the treated people you can't match are the ones outside the overlap region. Regression doesn't make this visible — it just extrapolates through the gap, quietly, without telling you. A matching analysis that drops 30% of its treated people is being honest about a problem that a regression analysis would have hidden.</p>

<p>That's the kind of thing I meant earlier about matching making assumptions visible that regression can hide.</p>

<h4>Balance diagnostics: the step you cannot skip</h4>

<p>After matching, you have a matched sample. You now have to check whether the matching actually <em>worked</em>.</p>

<p>This is called balance diagnostics, and it is non-negotiable. A matching analysis without balance diagnostics is not a matching analysis — it's a hope that the matching worked, dressed up in the costume of a matching analysis. Every reviewer should demand these diagnostics. Every paper should report them.</p>

<p>The main diagnostic is the <em>standardized mean difference</em>. For each covariate, you compute:</p>

<!-- LATEX: \text{SMD} = \frac{\bar{X}_{\text{treated}} - \bar{X}_{\text{control}}}{\text{pooled SD}} -->

<p>That's the difference in means between the matched treated and matched control groups, divided by the pooled standard deviation. It's expressed in standard-deviation units, so you can compare across variables measured in different units.</p>

<p>The rule of thumb: SMD below 0.1 is good balance. Between 0.1 and 0.25 is marginal. Above 0.25 indicates the matching didn't do its job for that variable.</p>

<p>You compute the SMD for every variable you matched on, and you report both the pre-matching and post-matching values side by side. A successful matching reduces the SMDs across the board. A failed matching leaves some or all of them high. If the matching failed on some variables, you need to respecify the propensity score model — add interactions, add polynomial terms, add missing variables — and rematch, and recheck.</p>

<p>There are also visual diagnostics. Density plots of the propensity score in treated and control groups should overlap substantially after matching. If they don't, you don't have propensity-score balance, which means the matching hasn't reproduced the randomization condition. Q-Q plots can reveal distribution-shape imbalances that means-based diagnostics miss.</p>

<p><strong>Here is the single most important thing about balance diagnostics. You do them before you look at the outcome.</strong> If you match, peek at the outcome, don't like what you see, and go back to respecify the propensity model, you are doing a form of p-hacking that will produce false-positive findings at much higher rates than nominal. The sequence must be: build the propensity model, match, check balance, refine if needed, freeze the matching — <em>then</em> look at the outcome. Once. No going back.</p>

<p>This discipline is the entire reason matching is seen as more credible than ad-hoc regression. If you don't observe the discipline, matching is not more credible.</p>

<h4>The analysis itself</h4>

<p>Once you have a matched sample with acceptable balance, the outcome analysis is almost anti-climactic. You treat the matched sample like a randomized trial.</p>

<p>For a continuous outcome, you compute the difference in outcome means between the matched treated and matched control groups. For a binary outcome, the difference in rates, or an odds ratio, or a risk ratio, whichever fits your scientific question. Standard errors come from paired methods (paired t-test, Wilcoxon signed-rank, conditional logistic regression) or from clustered standard errors that respect the matched-set structure.</p>

<p>A common modern practice is to run a regression on the matched sample, including the matched-set identifier as a fixed effect, and read the treatment coefficient. This combines matching with regression adjustment, and the combination is more forgiving of small remaining imbalances than either method alone. It's called a <em>doubly robust</em> estimator when both a propensity model and an outcome model are used — the estimate is consistent if either model is correctly specified. This is a property worth buying.</p>

<p>The estimate you get is usually the <em>average treatment effect on the treated</em> — the effect of treatment on the specific people who received it. In one-to-one matching without replacement, this is what the matched comparison naturally yields. If you want the effect on the overall population, or the effect on the untreated, you need a different matching structure (or a different method). Be careful to state what effect you're estimating. Different effects answer different questions.</p>

<hr>

<h3>4. Putting it together, and the limits</h3>

<p>Let me go back to smoking and gums and walk the whole pipeline.</p>

<p>I fit a propensity model: logistic regression of smoking status on age, sex, education, income, and race. Each of the 1,947 people gets a score — their estimated probability of being a smoker given their demographics. For each smoker, I find the non-smoker with the closest propensity score and pair them. I use a caliper — say, 0.2 standard deviations on the logit scale — and drop any smoker who has no non-smoker within that distance.</p>

<p>I check balance. Before matching, the standardized mean differences on my five variables range from maybe 0.3 to 0.5 — substantial imbalance. After matching, they're all below 0.1. Good. The matching worked.</p>

<p>Now I compare gum disease in the matched pairs. The ten-to-one raw gap shrinks — but doesn't vanish. The matched estimate says smokers have about three times the periodontal disease of comparable non-smokers. Most of the raw ten-fold gap was demographic noise. But three-fold remains, and that three-fold is the best estimate I have of smoking's causal contribution — <em>conditional</em> on having matched on the right variables.</p>

<p>So: is that three-fold estimate right?</p>

<p>This is where I have to be honest about what I don't know. I matched on five things. What about all the things I didn't measure? Stress levels. Diet. Oral hygiene habits. Frequency of dental visits. Genetics. If any of these things independently affects gum disease <em>and</em> correlates with smoking, my matching hasn't accounted for them, and my three-fold estimate is biased.</p>

<p>I have no way to measure the bias directly. I never will. The fundamental problem of observational causal inference is that you are adjusting for the variables you have, and hoping the ones you don't have don't matter too much.</p>

<h4>The escape hatch: sensitivity analysis</h4>

<p>There is, however, a way to ask a different question. Instead of "is my estimate right?", I can ask: <strong>how wrong would an unmeasured confounder have to be to overturn my result?</strong> If the answer is "catastrophically wrong," the result is robust. If the answer is "a tiny bit wrong," the result is fragile.</p>

<p>This is sensitivity analysis. The most widely used version is Paul Rosenbaum's, which introduces a single parameter called Γ (gamma). Γ measures how much an unmeasured confounder U could distort treatment assignment beyond what the measured covariates explain.</p>

<p>Γ = 1 means no distortion — treatment given the covariates is effectively random. Γ = 2 means an unmeasured confounder could double the odds of treatment for one person over an otherwise-identical person. Γ = 5 means fivefold. And so on.</p>

<p>The sensitivity analysis asks: <em>at what value of Γ does my significant result become non-significant?</em></p>

<p>If the answer is Γ = 1.1, my result is barely standing. Any plausible unmeasured variable could overturn it.</p>

<p>If the answer is Γ = 3, my result holds unless there's an unmeasured confounder with truly implausible strength — a variable that triples treatment odds for identical-looking people and hasn't been measured. That's not impossible but it's hard to make happen.</p>

<p>If the answer is Γ = 9 — which is roughly what Jerome Cornfield computed in his 1959 analysis of smoking and lung cancer — the result is practically bulletproof. An unmeasured confounder that increases smoking probability ninefold for otherwise-identical people is almost inconceivable. Cornfield's argument was a major step in convincing the medical establishment that the smoking-cancer link was causal, because it made the alternative (some mysterious unmeasured variable doing all the work) numerically absurd.</p>

<p>Sensitivity analysis does not prove the causal effect is real. It quantifies the size of the hidden bias you would need to invoke to explain it away. That's a service, and a valuable one. It makes your assumption visible and arguable.</p>

<p>Every matching analysis in a published paper should include a sensitivity analysis. When one is missing, you have a result without a known robustness; treat it provisionally.</p>

<h4>Matching and regression: cousins, not rivals</h4>

<p>A common framing says matching is an alternative to regression. This framing is wrong.</p>

<p>Matching and regression are different computational strategies for the same operation — back-door adjustment. Regression fits a model that relates outcome to treatment and confounders, and reads the treatment coefficient. Matching constructs a sample in which the confounders are balanced, and reads the simple difference in outcomes. Both, applied correctly under the same causal diagram, give the same answer.</p>

<p>When they disagree, the disagreement is diagnostic. Regression imposes a functional form — linear, usually — on the relationship between outcome and covariates. If that functional form is wrong, regression is biased. Matching makes no functional-form assumption. When the matching and regression estimates diverge, the regression's functional form is likely misspecified.</p>

<p>Regression will also happily extrapolate into regions where it has no data, using its functional form to fill in. Matching won't. If a treated individual has no nearby control, matching drops them (with a caliper) or gives them a bad match (without one). The bad match shows up in balance diagnostics. The extrapolation in regression is invisible unless you specifically check for it.</p>

<p>These are not arguments for one method over the other. They're arguments for using both, and understanding what each assumes. A modern analysis often matches first to get a balanced sample, then runs a regression on the matched sample to make fine-grained corrections. This combined approach is doubly robust: you get the right answer if <em>either</em> the matching or the regression is right. It's a sensible default.</p>

<h4>What matching cannot do</h4>

<p>Let me end this section with a hard list of what matching <em>cannot</em> do. This is important because matching's outputs look confident — nice clean pairs, clean estimates, clean standard errors — and it is easy to overbelieve them.</p>

<p><strong>Matching cannot create data that aren't there.</strong> If some of your treated individuals have no comparable controls, you cannot match them. You can drop them (caliper matching) or accept bad matches (no caliper). Neither gives you the effect on the unmatchable individuals. Matching restricts your conclusions to the region of covariate space where overlap exists.</p>

<p><strong>Matching cannot adjust for unmeasured confounders.</strong> I have said this six times in this chapter. I will say it more. Matching is back-door adjustment, and back-door adjustment requires that you have measured a sufficient set. If you haven't, matching fails, and it fails silently — the output looks identical to a successful analysis. Sensitivity analysis is the only way to quantify your exposure to this failure.</p>

<p><strong>Matching cannot tell you if your causal diagram is right.</strong> The back-door criterion tells you what variables to match on <em>given</em> the diagram. If the diagram is wrong — if you're matching on a collider, or on a mediator, or missing a key confounder — matching will faithfully produce a biased estimate, and no amount of matching diagnostics will detect it. Balance diagnostics only check whether you balanced the variables you matched on. They cannot check whether those were the right variables.</p>

<p><strong>Matching cannot handle interference between units.</strong> If my treatment affects your outcome — if a vaccinated person reduces the infection risk of their unvaccinated neighbor — the standard matching framework is invalid. It assumes that each person's outcome depends only on their own treatment. That assumption (Rubin's SUTVA, the stable unit treatment value assumption) is required for matching, for regression, for almost every method in this book. Interference is a genuinely hard problem, and it's still an active research area.</p>

<p><strong>Matching gives you the effect on the treated, not the effect on everyone.</strong> If the treatment works differently on different kinds of people, the effect estimated by one-to-one matching without replacement is the effect on the people who received treatment, not the effect on some hypothetical randomly-chosen person. If you want the latter, you need a different matching structure or a different method.</p>

<p>These limitations are not unique failings of matching. Most of them apply to every back-door method. The virtue of matching is that some of its failures are visible — a matching that fails balance diagnostics or drops most of the treated population is obviously broken. Regression can fail in the same ways silently.</p>

<p>Which is the whole point. Choose matching when you want the failures to be visible.</p>

<hr>

<h3>Exercises</h3>

<p>Solutions are not provided here. I want you to develop the instinct, and the instinct requires doing the work.</p>

<h4>Warm-up</h4>

<ol>
  <li><strong>Exercise 5.1.</strong> <em>(Objective: restate the matching idea in your own words)</em> Explain in three sentences what matching is trying to do, why it exists as an alternative to a randomized controlled trial, and what condition has to hold for it to work. Do this without using the phrase "propensity score."</li>
  <li><strong>Exercise 5.2.</strong> <em>(Objective: recognize exact matching's wall)</em> You have five binary covariates and three continuous covariates (age, income, BMI). Describe concretely why exact matching fails in this case, and estimate how many "buckets" you would need if you tried to discretize each continuous variable into ten bins.</li>
  <li><strong>Exercise 5.3.</strong> <em>(Objective: compute a standardized mean difference)</em> A matched sample has mean age 54.2 (SD 12.1) in the treated group and mean age 52.8 (SD 11.4) in the control group. Compute the standardized mean difference. Interpret: is this acceptable balance?</li>
</ol>

<h4>Application</h4>

<ol start="4">
  <li><strong>Exercise 5.4.</strong> <em>(Objective: apply the propensity score balancing property)</em> Explain why, if two individuals have the same <em>true</em> propensity score, the treatment assignment between them is as good as random — even if their individual covariates differ. Then explain why this property may fail for the <em>estimated</em> propensity score.</li>
  <li><strong>Exercise 5.5.</strong> <em>(Objective: choose between greedy and optimal matching)</em> Construct a small example (four treated, four controls) in which greedy matching produces a total distance noticeably larger than optimal matching. Identify the pair where greedy makes the "locally good but globally bad" choice.</li>
  <li><strong>Exercise 5.6.</strong> <em>(Objective: recognize an overlap problem)</em> You are estimating the effect of attending graduate school on lifetime earnings. Your treated group includes people with GRE scores from 320 to 340 (the top of the range). Your control group has GRE scores mostly between 250 and 310. Describe what happens under one-to-one matching without a caliper, and under one-to-one matching with a tight caliper. Which is more honest?</li>
  <li><strong>Exercise 5.7.</strong> <em>(Objective: diagnose a matching report)</em> A published paper reports a matched observational study of a new cancer drug. The paper reports the matched estimate and p-value but does not include balance diagnostics or a sensitivity analysis. List the specific things a reviewer should demand the authors add before the paper is publishable.</li>
</ol>

<h4>Synthesis</h4>

<ol start="8">
  <li><strong>Exercise 5.8.</strong> <em>(Objective: integrate propensity score and balance)</em> A researcher fits a logistic propensity score model using age, sex, and income, then matches and computes standardized mean differences. SMDs on age and sex drop below 0.1, but the SMD on income is still 0.27. What might have gone wrong with the propensity model? Name three specific respecifications to try, in order of what you'd try first.</li>
  <li><strong>Exercise 5.9.</strong> <em>(Objective: compare matching to regression on the same question)</em> Using any simulated or real dataset of your choice with a known treatment, an outcome, and at least four covariates, compute the treatment effect two ways: by OLS regression with the covariates as controls, and by propensity-score matching. Compare the estimates. Where they differ, propose a specific reason (functional form, overlap, interaction not in the regression) and test it by fitting a regression with the additional flexibility.</li>
  <li><strong>Exercise 5.10.</strong> <em>(Objective: interpret a sensitivity analysis)</em> A matched study reports a statistically significant effect with Γ sensitivity bound of 1.3 — meaning an unmeasured confounder that distorted treatment odds by 30% would overturn the result. Another study reports the same effect size with Γ = 4. Which result is more robust? Explain what the specific numbers mean about what an unmeasured confounder would look like.</li>
</ol>

<h4>Challenge</h4>

<ol start="11">
  <li><strong>Exercise 5.11.</strong> <em>(Objective: reason about a case matching cannot handle)</em> A study tries to estimate the effect of receiving a flu vaccine on infection rates, by matching vaccinated and unvaccinated individuals on demographics. Explain why the SUTVA assumption is violated here, and what that does to the matched estimate. Sketch one research design that could plausibly handle the interference (you may need to look up literature on interference or spillover effects).</li>
  <li><strong>Exercise 5.12.</strong> <em>(Objective: bring the chapter to a real problem)</em> Pick an observational study from your own field or from a news article making a causal claim. Identify: (a) the treatment, (b) the outcome, (c) the confounders the researchers adjusted for, (d) confounders you suspect they missed, (e) what a sensitivity analysis might show, and (f) whether you believe the reported effect is plausibly causal. Write a one-page critique suitable for submission as a journal referee report.</li>
</ol>

<hr>

<h3>Chapter summary</h3>

<p>You walked in with back-door adjustment and stratification in hand. You walk out with a practical tool — matching — for doing the adjustment in the many-covariates regime where stratification breaks down.</p>

<p>You can now state what matching is trying to do: manufacture, after the fact, the comparability that randomization would have produced for free.</p>

<p>You can use the propensity score to collapse a multi-dimensional matching problem into a one-dimensional one, and you can explain <em>why</em> this collapse works — two people with the same propensity score are, within that level, exchangeable with respect to treatment.</p>

<p>You can execute the full pipeline: build a propensity model, match (greedy or optimal, one-to-one or one-to-many, with or without a caliper), check balance with standardized mean differences, and estimate the treatment effect on the matched sample.</p>

<p>You can run a sensitivity analysis and interpret what the Γ value says about how robust your result is to unmeasured confounding.</p>

<p>You can distinguish the three ways a matching analysis can fail: unmeasured confounders (handled by sensitivity analysis, not by matching itself), lack of overlap (handled by calipers, but at the cost of generalizability), and a wrong causal diagram (not handled by anything in matching — the diagram is an input, not an output).</p>

<p><strong>The one idea from this chapter that matters most.</strong> Matching does not add power to observational causal inference. It exposes, more visibly than regression does, the places where the inference is weak — the treated individuals without comparable controls, the variables that won't balance, the estimates that crumble under mild unmeasured-confounding pressure. Prefer matching when you want to see the weakness. Prefer regression when you want to summarize quickly. Use both when the answer matters.</p>

<p><strong>The common mistake to watch for.</strong> Using matching without balance diagnostics, without sensitivity analysis, or with a propensity model that was never checked for correct specification. Each of these mistakes turns matching into a dress-up version of the problem it was meant to solve. Matching <em>only</em> works when you do the diagnostics, and does less than claimed when you don't.</p>

<p><strong>The Feynman test.</strong> Can you explain to a curious friend who hasn't read this chapter why matching on one number — the propensity score — does the same work as matching on ten? If yes, you understand the central trick. If not, go back to Section 2 and work through it until you can tell them without using any jargon beyond "probability of getting the treatment."</p>

<hr>

<h3>Connections forward</h3>

<p>The next chapter (Chapter 6) extends propensity-score methods in a different direction: <em>weighting.</em> Instead of pairing treated to controls, you weight each individual by the inverse of their propensity score, so that the weighted sample looks like a population in which treatment was assigned randomly. Weighting is the same idea as matching, expressed as arithmetic on all the data rather than as pairing. It has some efficiency advantages — it uses all the data, not just the matched subset — and some stability risks — when propensity scores get near 0 or 1, weights explode. You'll see when to reach for which.</p>

<p>Chapter 7 brings in <em>instrumental variables</em>, for the cases where the back-door criterion returns no valid adjustment set and no amount of matching or weighting can rescue you. The whole second half of this book is about what to do when the back door is closed — when some critical confounder is unmeasured and you need to find a different way to isolate the causal effect. Those later chapters build on the back-door intuition you now have, but they point to different doors.</p>

<p>One last thing. The methods in the next few chapters will get more abstract and more clever. Remember: the goal is always the same. You are trying to extract the causal effect from data that are contaminated by all the ways the world declines to randomize itself. Matching was the first tool that made this feasible at scale. Every tool after it is a variation on the same project.</p>

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Paul Rosenbaum** and Donald Rubin introduced the propensity score in 1983 — a single number summarizing many covariates that, when matched on, balances treated and control groups. The propensity score reshaped how observational studies handle confounding.

**Run this:**

```
Who is Paul Rosenbaum, and how does the propensity score connect to the matching methods we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Paul Rosenbaum"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how propensity-score matching balances two groups on observed confounders — and what it can't fix.
- Ask it about Rosenbaum's later work on sensitivity analysis for hidden bias.

What changes? What gets better? What gets worse?
