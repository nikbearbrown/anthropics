# Mediators: The Variable You Shouldn't Touch


## TL;DR

- TL;DR: A mediator is a variable that sits on the causal path from treatment to outcome, and conditioning on it removes from your estimate the part of the effect that flows through it.
- The chapter moves through Opening — A model that "didn't work" because the team measured the wrong question, Concept one — A mediator is a structural position, not a name, Mid-chapter checkpoint, Concept two — Total effect, direct effect, indirect effect, and the policy question as the prior, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

> **Draft status:** `voice-anchored: partial` — no per-book `style/` examples exist for `causal-reasoning` as of 2026-05-13; voice calibrated from CLAUDE.md §6 and from the in-book precedents set by Chapters 4 and 5.

**Suggested titles:**
1. Mediators: The Variable You Shouldn't Touch
2. The Pipe You Didn't Mean to Clamp
3. Two Correct Analyses of the Same Data

**TL;DR:** A mediator is a variable that sits *on the causal path* from treatment to outcome, and conditioning on it removes from your estimate the part of the effect that flows through it. Whether that removal is what you want depends on which question your team is asking — a policy decision the data does not contain and the algorithm cannot make.

**Byline:** Nik Bear Brown

**Prerequisites:**
- Read a directed acyclic graph and tell whether a path is open or blocked given a set of conditioning variables (Chapter 3).
- State the three identification-failure types from Chapter 4 (wrong variables, wrong functional form, wrong conditioning) and recognize that this chapter sits inside *wrong conditioning*.
- Apply the three diagnostic questions for backdoor paths from Chapter 5 and find a valid adjustment set when one exists.
- Stipulate that an arrow `A → B` on a DAG means "A is part of what produces B," not "A and B are correlated." Same stipulation as Chapter 5; we use it harder here.
- Know what a regression coefficient does *not* tell you about a causal effect — that the same coefficient can answer at least two different questions depending on what you condition on.

**Learning objectives:**
- **(Analyze, Part A)** Given a DAG, identify mediators by structural position and predict the consequence of conditioning on each.
- **(Evaluate, Part A)** Make an explicit choice between estimating the total effect and the direct effect for a stated decision, with justification.
- **(Evaluate, Part B)** Make the total-vs-direct effect choice for a treatment–outcome problem in your own domain, naming the policy question that drives the choice.
- **(Create, Part B)** Begin specifying the estimation approach for that own-domain analysis — which variables enter the adjustment set, which do not, and why.

---

## 1. Opening — A model that "didn't work" because the team measured the wrong question

A recommendation team at a streaming platform — pick whichever one you like; the structure repeats across the industry — runs an A/B test on a new ranking policy. The product question is unambiguous. *Does this new ranker keep users around longer over the next ninety days?* Treatment: ranker version. Outcome: retention at day ninety.

The team designs the experiment well. They randomize at the user level. They run for long enough to clear the typical novelty bump and the typical reversion bump. They have a primary metric (day-90 retention) and a secondary metric (content diversity of the user's feed, defined as the entropy of category visits across the test window). The secondary metric is there because the team has, very reasonably, hypothesized that the new ranker increases diversity, and diversity is — the team believes from prior work — part of why users stick around.

Two analyses come back.

Analysis A is the naive one. Compare day-90 retention in treatment versus control. The treatment group retains a little better. The effect is small but consistent — the kind of number you ship with a green light if it survives a few sensitivity checks.

Analysis B is the "rigorous" one. The lead data scientist, trained to control for known confounders, adds content diversity to the regression. The team has been told for years that controlling for stable user-level features makes estimates more precise. Diversity feels like such a feature. The lead also notes — correctly, as far as it goes — that diversity explains a lot of the variance in retention. Adding it to the model should make the retention estimate sharper.

The estimate gets sharper. It also gets smaller. After conditioning on diversity, the policy effect on retention shrinks to something indistinguishable from zero. Analysis B's confidence interval barely crosses the null. The lead writes the memo. "After controlling for content-diversity differences, the new ranker has no detectable impact on retention. Recommend shelving."

The team shelves it.

Now sit with what happened. The new ranker, in this case, *worked primarily by changing what users saw*. Its effect on retention was almost entirely routed *through* diversity — different distribution of categories → different feed feel → users who stuck around. The thing the lead controlled for was the very channel through which the policy worked. By holding diversity fixed, the analysis removed almost all of the policy's effect from the estimate. What remained was the residual — whatever the new ranker did to retention *not* by changing what users saw. That residual was, plausibly, near zero. The total effect was not.

I want to be careful about claims, so let me flag what is verifiable and what is illustrative. The structural failure mode — *conditioning on a post-treatment mediator destroys the indirect effect from the total-effect estimate* — is canonical, taught in [VanderWeele's *Explanation in Causal Inference* (Oxford, 2015)](https://global.oup.com/academic/product/explanation-in-causal-inference-9780199325870), and documented as a recurring practical hazard in the Microsoft-Bing-LinkedIn experimentation literature [(Deng, Xu, Kohavi & Walker, 2013, WSDM)](https://dl.acm.org/doi/10.1145/2433396.2433413). The KDD 2019 paper that formalizes direct/indirect-effect decomposition for online A/B tests with click-stream mediators is the closest published case to the cold open I just walked. `[verify-KDD-2019-full-citation — pantry notes flag the venue and author list; I have not yet pulled a stable PDF.]` The vignette above is composite: the structure is real and named in the literature; the specific platform, the specific numbers, and the specific shelving memo are stylized.

Stylized or not, the move has happened at large platforms repeatedly enough to be a known hazard. The team that shipped Analysis B was not careless. They were applying the regression-class rule — *if it correlates with the outcome and is easy to measure, control for it* — that has worked for them in dozens of prior analyses. The rule fails here for a structural reason. Diversity is not a confounder of policy and retention. Diversity is the *pipe* the policy is flowing through. Conditioning on a pipe is plugging it. You stop the water, then ask why the basin is not filling.

The fix is not technical. The fix is that someone in the room — analyst, product manager, anyone — asks, before any conditioning happens, *which question is this analysis trying to answer?* If the question is "should we ship the policy?", do not touch diversity. If the question is "given the diversity each user already gets, what residual effect does the ranker have on retention?", touch it deliberately and report that you are answering a narrower question. Two questions. Same data. Same DAG. Different effects. Different conditioning decisions. The data does not contain the question; the team does.

That is the chapter. We are going to learn the variable you should not touch — and how to know it from the variable you should.

---

## 2. Concept one — A mediator is a structural position, not a name

Pull the diversity case to the whiteboard. Three nodes is enough.

```
        P (new ranker policy)
       / \
      ↓   ↓
      D   R (day-90 retention)
       \ ↗
        ↘
```

Let me write that more cleanly as a list of edges so the picture is unambiguous.

1. `P → D` (the new policy shifts content diversity in user feeds)
2. `D → R` (diversity affects retention through user experience)
3. `P → R` (the policy has some additional effect on retention that does not flow through diversity — UI changes, latency changes, novelty-without-diversity, anything else the policy bundle changes at once)

The total effect of `P` on `R` decomposes into two parts: the part that flows along `P → D → R` (call it the *indirect effect*, the effect through the mediator) and the part that flows along `P → R` (call it the *direct effect*, the effect not through this mediator). Total effect equals direct effect plus indirect effect. This decomposition is the central object of mediation analysis, formalized in counterfactual language by [Robins and Greenland in *Epidemiology* in 1992](https://journals.lww.com/epidem/abstract/1992/03000/identifiability_and_exchangeability_for_direct_and.13.aspx) and translated into the DAG/`do`-operator framework by [Pearl in his 2001 UAI paper](https://ftp.cs.ucla.edu/pub/stat_ser/r273-u.pdf).

Here is the definition the rest of the chapter rests on.

> A *mediator* of the effect of `X` on `Y` is a variable `M` that occupies a position on a directed (causal) path from `X` to `Y` — that is, there exist arrows `X → M` and `M → Y`, possibly with other variables in between.

Two things in that definition are doing all the work, and you should feel both before you read on.

First, the mediator is *downstream of treatment*. There is an arrow *from* `X` *into* `M`. That fact, by itself, distinguishes a mediator from a confounder. A confounder has arrows going *out* to both treatment and outcome (it is upstream of both). A mediator has an arrow coming *in* from treatment and an arrow going *out* to outcome (it is downstream of treatment and upstream of outcome). Same picture of "a third variable connected to X and Y." Different arrow geometry. Different time-ordering. Different conditioning logic.

Second, the mediator is on a *forward* path — a path traveling in the direction of the arrows from `X` to `Y`. Recall Chapter 5: backdoor paths begin with an arrow *into* `X`. The path `X → M → Y` does not begin with an arrow into `X`; it begins with an arrow out of `X`. So `X → M → Y` is *not* a backdoor path. It is the part of the causal effect of `X` on `Y` that the analysis is supposed to *include*, not the part the analysis is supposed to *block*.

This is the punchline most students need to hear twice.

Conditioning on a non-collider on a backdoor path *closes a path that should be closed*. That is what Chapter 5 taught. Conditioning on a non-collider on a *forward* path *closes a path that should be open*. That is what this chapter teaches. The same operation — *condition on this variable* — has opposite effects depending on the structural role of the variable. Same operation. Opposite consequences. The thing that tells you which case you are in is the DAG.

I want to make the mechanism specific because the word "blocks" is doing a lot of work in causal-inference textbooks and the student should see what it actually means.

Here is what is actually happening when you condition on `D` (content diversity) in the diversity case.

The total effect we want is the answer to *what is the probability of `R` if we set `P` to `P=1` versus `P=0`?* In Pearl's notation, that is `P(R | do(P=1)) − P(R | do(P=0))`. The `do` says: *intervene to set `P`, then let the rest of the DAG run.* Crucially, when you set `P`, the value of `D` is allowed to respond — because `P → D` is in the DAG. The downstream cascade includes the change in `D` that the policy produces, and then the change in `R` that the new `D` produces. The total effect includes the indirect effect *because we let `D` move*.

Now condition on `D = d`. In notation, you are estimating `P(R | do(P), D=d)`. The `D=d` *fixes* `D` at the value `d`. Whatever variation `P` would have produced in `D` is no longer allowed to flow downstream — because `D` is pinned. The only variation in `R` left to attribute to `P` is the variation that does not pass through `D` — the direct effect along `P → R`. Whatever the indirect path `P → D → R` would have contributed has been clamped off. Not because the path went away; because you clamped one of the nodes along it.

If the policy's effect on retention is *purely* mediated by diversity — no direct effect at all — then conditioning on `D` removes the *entire* effect of `P` on `R` from the estimate. The coefficient on `P` in the conditional regression goes to zero. Not because the policy does not work. Because the policy works only through `D`, and you stopped `D` from doing its job in the analysis. The estimand has changed. *What you are estimating* is now a different quantity than *what you wanted to estimate*. The estimator is unbiased for the wrong thing.

A useful slogan, since the student will need one: *conditioning on a confounder removes bias. Conditioning on a mediator removes effect.* The two operations look identical in code — both are an entry in your adjustment set. The DAG tells you whether the entry helps or hurts.

There is one common misconception I want to head off before it lodges. Engineering readers from a regression tradition sometimes argue: *conditioning on `D` just makes my standard errors smaller, because `D` explains variance in `R`*. That is true — it does reduce residual variance — and that is precisely why the move feels productive. But reducing residual variance is *how precisely you estimate a quantity*. Changing the estimand is *what quantity you estimate*. You are entitled to a sharper estimate of the direct effect if you understand that you are estimating the direct effect. You are not entitled to a sharper estimate of the total effect by conditioning your way out of part of it. Variance reduction and estimand change are different operations wearing the same syntax. The DAG is where the difference is visible.

---

## Mid-chapter checkpoint

Pause. Make sure something has landed before the next move.

A mediator `M` is structurally defined: it has an arrow from treatment `X` coming in, and an arrow to outcome `Y` going out. Conditioning on a mediator clamps it; the part of the effect of `X` on `Y` that flows through `M` no longer appears in the estimate. What remains is the *direct effect* — the part of `X`'s influence on `Y` that travels by some other route.

Whether that is what you want is not a statistical question. It is a question about what decision the analysis is feeding.

You should now be able to say in your own words: *the streaming-platform case in Section 1 estimated the direct effect by accident, because the team conditioned on content diversity without naming the question they were answering.* If that sentence makes sense, the structural framing is doing its work. If it does not yet, reread Section 2 before going further. The rest of the chapter builds on this distinction.

---

## 3. Concept two — Total effect, direct effect, indirect effect, and the policy question as the prior

I want to give the three effects names that stick, because the literature uses the terms inconsistently and I do not want you to lose the structure in the vocabulary.

**Total effect** of `X` on `Y`. *If we change `X`, what happens to `Y`, end to end, regardless of pathway?* In `do`-notation, `P(Y | do(X=1)) − P(Y | do(X=0))`. This is the deploy-or-don't decision. It is the question every product manager asks when they want to know whether to ship.

**Direct effect** of `X` on `Y`. *If we change `X` while holding the mediator `M` at some specified value, what happens to `Y`?* In `do`-notation, `P(Y | do(X=1, M=m)) − P(Y | do(X=0, M=m))`. This is the mechanism-attribution question — *of the effect we measured, how much is operating through some other channel than `M`?* If `M` is the only mediator on the path, this is the channel the analyst did not name.

**Indirect effect** of `X` on `Y` through `M`. *How much of the effect of `X` on `Y` is routed through `M`?* It is the difference between the total effect and the direct effect (in the simplest decomposition). Useful when the next intervention is going to target the mediator and the team wants to know how big the prize is.

Now the key claim of this chapter, restated as a verdict rather than as machinery:

> The choice between estimating the total effect and the direct effect is a *substantive policy question*, not a methodological default. The data does not contain the question. The student does.

Pearl is explicit about this in the 2001 UAI paper. Robins and Greenland were explicit about it nine years earlier. VanderWeele's 2015 textbook is a sustained sermon on this point. Three correct analyses of the same data with the same DAG can produce three different effect estimates — total, direct, indirect — and *each is correct for the question it answers*. None is the "real" effect. The "real" effect is not a single number waiting to be discovered. The "real" effect is whichever number answers the decision the analysis is in service of.

This is the chapter the book is named after. *Causal Reasoning: Irreducibly Human* is not a slogan; it names which step in the analysis lives outside the algorithm. The total-vs-direct choice is that step. Every causal-inference tool I know — DoubleML, EconML, `dowhy`, `mediation`, the entire `gComp`-style g-method family — can estimate either effect given the question. None of them can pick the question. The pick is yours.

Let me walk three policy questions through three correct analyses, all on the diversity case, so the distinction lands.

**Question 1. "Should we ship the new ranker?"**
The decision is binary: deploy yes/no. The relevant number is *what happens to retention if we change the ranker?* — total effect. Conditioning on diversity is wrong. Estimate `P(R | do(P=1)) − P(R | do(P=0))` without conditioning on `D`. Report the number to the product manager. They decide.

**Question 2. "If we shipped the new ranker, what fraction of the retention lift came from changing the feed, and what fraction came from the policy's other changes (UI, latency, etc.)?"**
The decision is allocation of next-quarter engineering effort. The relevant numbers are the indirect effect (the diversity channel) and the direct effect (everything else). Estimate both. The indirect effect is total minus direct. Report both. The team decides whether to invest in further diversity-mechanism work or in the residual channel.

**Question 3. "Given users who would naturally see the same level of diversity under either policy, does the new ranker help?"**
The decision is more subtle — possibly *should the ranker be applied only to users for whom diversity is not the binding constraint?* The relevant number is the direct effect: `P(R | do(P), D=d)` for some chosen `d`. Conditioning on diversity is appropriate, and the report makes clear that the estimate is conditional on a fixed level of diversity.

Same DAG. Same data. Three questions. Three correct estimands. *None* of the three is "more rigorous" than the others. None is "the answer." Each is the answer to its own question. The pretense that there is a single right effect to estimate — and that "controlling for known confounders" gets you to it — is the failure mode that shelved the new ranker in Section 1.

I want to give you a heuristic for this in your own work. Before you write any conditioning set, write the *decision* the analysis is serving. Two sentences, no jargon. *"We are going to use this number to decide whether to ship the new ranker"* implies total effect, no mediator conditioning. *"We are going to use this number to decide which mechanism to invest in next"* implies direct/indirect decomposition. *"We are going to use this number to model what would happen for users at a given diversity level"* implies direct effect. Write the sentence. Then design the conditioning. The order matters. The estimand precedes the estimator.

The Baron-Kenny ghost. I should address the procedure some students will have encountered. [Baron and Kenny published a four-step mediation procedure in the *Journal of Personality and Social Psychology* in 1986](https://psycnet.apa.org/doi/10.1037/0022-3514.51.6.1173) that was the social-science default for two decades and is still in undergraduate stats curricula. It is worth knowing two things about it. The procedure correctly distinguished mediator from moderator, and its staged logic of "show treatment moves mediator, show mediator moves outcome, attribute" survives in modern frameworks. *And* the modern framework has retired its first step — the requirement that you find a statistically significant total effect before testing for mediation. Mediation can exist with no significant total effect when direct and indirect effects offset each other. [Zhao, Lynch, and Chen made this argument carefully in the *Journal of Consumer Research* in 2010](https://doi.org/10.1086/651257). [Hayes laid out the modern statistical treatment in *Communication Monographs* in 2009](https://doi.org/10.1080/03637750903310360) and David Kenny himself acknowledges the retirement of step 1 on his [current mediation page](https://davidakenny.net/cm/mediate.htm). Baron-Kenny also did not name confounding explicitly; the modern framework requires you to. If you were trained on Baron-Kenny, the upgrade you are being asked to make is: state the DAG, state the question, derive the conditioning. The procedure stops being a checklist and becomes a structural argument.

---

## 4. Concept three — Natural and controlled direct effects (a brief, signposted look)

There is a distinction the careful student should at least see, even though we are not going to wrestle it to the ground in Week 6. Pearl 2001 and VanderWeele 2015 split the direct effect into two kinds, and they answer different questions.

**Controlled direct effect (CDE).** The effect of `X` on `Y` when `M` is held fixed at some specified value `m`. *If we changed the policy and pinned diversity to its mean baseline level, what would retention do?* This is the effect you get by conditioning on `M=m` and reading off the `X` coefficient. It requires assumptions about confounding of `X→Y` (the usual Chapter 5 work) and confounding of `M→Y` (a new requirement — there must be no unmeasured common cause of `M` and `Y` beyond the ones in the adjustment set).

**Natural direct effect (NDE).** The effect of `X` on `Y` if we changed `X` but `M` behaved as it *would have behaved* under the reference value of `X`. *If we shipped the new ranker but somehow forced each user's diversity to be what it would have been under the old ranker, what would retention do?* This is conceptually elegant — it isolates the part of the effect that does not run through `M` while letting `M` take a realistic value rather than an analyst-chosen one. It is also much harder to identify. It requires what the literature calls "sequential ignorability" or "cross-world independence" — assumptions about the joint distribution of counterfactual values of `M` that cannot be tested from observational data alone.

Pearl's *mediation formula* expresses the natural indirect effect in terms of observable quantities under those assumptions. The formula is mechanically simple — you can write it on one line — but the assumptions behind it are not. [Imai, Keele, and Tingley reviewed the identification conditions carefully in *Psychological Methods* in 2010](https://doi.org/10.1037/a0020761), and the practical implication for our reader is this: *natural effects are real, formally elegant, and often estimable in practice — but the estimates rest on assumptions you cannot check from data*. Treat them the way you treat any structural assumption: state it, signpost it, and run a sensitivity analysis later in the project if the decision is high-stakes. Chapter 14 picks up the sensitivity story.

For this chapter, the default is *controlled* direct effects. The reason is practical. Controlled effects require weaker assumptions, answer a narrower question, and are what the engineering tools you will use — DoubleML's mediation routines, the `mediation` R package in its standard mode, EconML's mediation extensions — actually estimate when you ask for "the direct effect." If you have specified a `m` to condition on, you are estimating a CDE. If you have not specified `m` and the tool returned a number, find out which assumption it just made.

I want to name what we are doing here pedagogically because the chapter is treading carefully on purpose. The natural-vs-controlled distinction is real, the literature is unambiguous about it, and any honest mediation chapter has to flag it. Treating it fully takes more apparatus than Week 6 can carry. So we plant it, name the sources, and move on. If your downstream project requires natural effects, you will need to come back to VanderWeele 2015 Chapter 2 and to Imai et al. 2010, and to read sensitivity analyses for sequential ignorability. The chapter has done its job if you know the distinction exists, know which one your tool returned, and know where to find the rest.

---

## 5. Concept four — Mediator versus moderator (the confusion the engineering reader inherits)

The single most common mistake I see in engineering A/B test analyses is conflating mediators with moderators. The two words sound similar. The two operations are different. The literature uses both, sometimes loosely. Here is what each is, structurally, on a DAG.

A **mediator** `M` sits *on the causal path* from `X` to `Y`. Arrow in from `X`. Arrow out to `Y`. Conditioning on `M` blocks the indirect effect.

A **moderator** `W` does not sit on the `X → Y` path at all. It sits *to the side*. What `W` does is *change the strength or direction of the `X → Y` effect at different levels of `W`*. The effect of `X` on `Y` is one thing at `W=0` and a different thing at `W=1`. Statistically, this is an *interaction term*. Structurally, `W` is not on the causal path; it is a moderator of the effect along the path. Conditioning on `W` does not block anything. Conditioning on `W` *estimates the effect of `X` on `Y` at each level of `W` separately* — heterogeneous effects, conditional average treatment effects, the whole stratified-effect family from Chapter 11.

The Baron and Kenny 1986 paper made this distinction crisply and the field has kept their framing on this specific point. (Their paper has held up better on the mediator-vs-moderator question than on the four-step procedure. The good parts persist.)

The diagnostic is one question. *Does `W` respond to the treatment?* If yes, `W` is downstream of treatment, and `W` is at least partly a mediator. If no, `W` is plausibly a moderator. The diagnostic is asymmetric and the asymmetry is structural: a true moderator's value does not move when you flip the treatment; a true mediator's value does.

A worked case the engineering reader will recognize. Treatment: new pricing policy. Candidate "covariate to stratify on" in the A/B analysis: customer tenure (months since signup at experiment start). Is tenure a mediator or a moderator? Tenure was determined *before* the experiment started. The treatment did not change anyone's tenure. So tenure is a moderator. Stratifying on tenure to estimate heterogeneous price effects is fine. Now contrast: candidate "covariate to stratify on": engagement-rate-during-the-experiment-window. Did the treatment change engagement rate? Almost certainly yes — the pricing policy changed behavior during the window. So engagement rate is a mediator. Stratifying on it conditions on a post-treatment variable; you are now estimating direct effects, not heterogeneous total effects. Same syntax. Same `stratify_by=` argument in your analysis pipeline. Different structural object. Different effect.

I am dwelling on this because it is the place engineering teams make the silent mistake the most often. "We stratified on engagement-rate-during-experiment to reduce variance" is a sentence I have read in internal experiment write-ups and not seen flagged. It is mediator conditioning by another name. The variance reduction is real. The estimand has changed without anyone noticing. The DAG is the only check.

---

## 6. Integration — Same DAG move, opposite consequence

I want to gather Chapter 5 and Chapter 6 together because the contrast is the lesson.

In Chapter 5 you learned that conditioning on a confounder *closes a backdoor path that should be closed*. The variable was upstream of treatment. The path it sat on was a backdoor (arrows from `U` into both `X` and `Y`). Conditioning on `U` blocked the backdoor and removed bias from the estimate. Good move. You did it deliberately and the estimate got better.

In Chapter 6 you have learned that conditioning on a mediator *closes a forward path that should be open*. The variable was downstream of treatment. The path it sat on was a forward (causal) path (`X → M → Y`). Conditioning on `M` blocked the forward path and removed *effect* from the estimate. Bad move (if your question was total effect). You did it deliberately or by accident and the estimate got smaller.

Same operation in your code: `adjustment_set = [confounder] + [mediator]` looks like one list of variables to your modeling library. The library does not know which is which. It does not ask. It conditions on what you hand it.

Same operation on the DAG: "place a conditioning bar through this node." The notation does not change between the two cases. The graphical move is identical.

Opposite consequence: bias removed versus effect removed. *Only the DAG tells you which case you are in*. And the DAG is a domain-knowledge artifact — written by someone who knows whether the variable is upstream or downstream of treatment, whether the arrow goes in or out, whether the path is backdoor or forward. The data does not know. The model does not know. The DAG is where the knowing lives.

This is the pedagogical reason these two chapters travel together and live next to each other in the curriculum. Chapter 5 taught the move. Chapter 6 taught the *limit* of the move. If you stopped at Chapter 5, you would walk away with the "control for everything you can measure" reflex, applied with new structural language. Chapter 6 is the chapter where that reflex has to be unlearned for a specific class of variable.

I want to name one further thing, because it primes Chapter 7. A variable's *structural role* is defined relative to the query. Diversity is a mediator when the query is *the effect of ranker policy on retention*. Diversity might be a confounder for some other treatment–outcome pair on the same data — say, *the effect of category preference on retention* — depending on how the arrows are drawn. The same variable plays different roles in different queries. The label "mediator" is not a property of the variable in the abstract. It is a property of the variable's position on the path for a particular `X` and `Y`.

That observation — *roles are query-dependent* — is the door into Chapter 7. There is a third structural role we have not named yet. Neither confounder nor mediator. For that role, conditioning produces a third kind of consequence, and the rule is different from both of the ones you have learned so far. Definition next chapter.

---

## 7. Worked example — Pricing → conversion → revenue, end to end with numbers

I am going to walk one case with hypothetical numbers, because the abstract claim *"conditioning on a mediator destroys the total effect"* lands harder when you watch a number actually shrink.

**Setup.** A subscription pricing experiment. Treatment `T`: a price reduction from $20/month to $15/month for new signups. `T = 1` means reduced price; `T = 0` means baseline price. Mediator `C`: conversion rate, the probability that a visitor who lands on the pricing page subscribes. Outcome `R`: revenue per visitor over the first 30 days.

The DAG is three nodes.

```
   T ──→ C
   │     │
   │     ↓
   └───→ R
```

Edges:
1. `T → C` — lower price increases conversion rate.
2. `C → R` — higher conversion means more paying subscribers, which (price held constant) means more revenue per visitor.
3. `T → R` — there is a direct edge too, capturing the fact that *for visitors who do convert*, lower price means lower revenue per converter.

Note something deliberate about the structure. The direct effect (`T → R`) is *negative* (lower price, lower revenue per converter), and the indirect effect (`T → C → R`) is *positive* (lower price → more converters → more revenue per visitor through volume). The total effect is the sum. Whether the total is positive or negative is an empirical question about elasticity. The decomposition is structural.

**Edge strengths (hypothetical, for the worked example).**

I am picking numbers that make the arithmetic clean and the structural lesson clear. They are stylized; in your own analysis you would estimate them from the experiment.

- Baseline conversion rate at `T=0`: 4%.
- Conversion rate at `T=1`: 6%. So the effect of `T` on `C` is `+0.02` (a 2-percentage-point lift).
- Revenue per converter at `T=0`: $20 (one month at $20, simplified).
- Revenue per converter at `T=1`: $15 (one month at $15).
- For now ignore second-month renewals; this is a one-period model.

Compute revenue per visitor under each treatment.

`R | T=0` = conversion rate × revenue per converter = `0.04 × $20` = `$0.80` per visitor.
`R | T=1` = `0.06 × $15` = `$0.90` per visitor.

**Total effect of `T` on `R`:** `$0.90 − $0.80` = `+$0.10` per visitor. Lower price is total-effect positive — the volume gain more than offsets the per-converter loss. This is the number a product manager needs to decide whether to ship the price cut.

Now run the analysis the team will run if they "control for conversion rate." Condition on `C=c` for some fixed conversion level. Within a stratum of `C`, what is the effect of `T` on `R`?

Inside the stratum, conversion is held fixed by stipulation. So the only way `T` can affect `R` is through the direct edge `T → R` — the price-per-converter effect. Within a stratum:

Effect of `T` on `R` | `C = c` = `($15 − $20) × c` = `−$5 × c`.

At `c = 0.04`: `−$5 × 0.04` = `−$0.20` per visitor (within the stratum).
At `c = 0.06`: `−$5 × 0.06` = `−$0.30` per visitor (within the stratum).

Take a weighted average across strata (any sensible weight; the qualitative direction does not depend on it). The conditional-on-`C` effect is *negative*. The unconditional (total) effect was *positive*. The conditioning flipped the sign.

I want to make sure the student sees what just happened. The team that conditions on conversion rate to "be rigorous" gets back a number that says the price cut *reduces* revenue per visitor. They write the memo. *Recommend not shipping the price cut.* The total-effect answer was that the price cut *raises* revenue per visitor. Two correct analyses of the same data. Opposite recommendations. The conditioning decision flipped the policy.

**The estimand decomposition.**

Let me write it out symbolically to anchor what we just computed.

Direct effect (controlled, at `C=c`): `E[R | do(T=1), C=c] − E[R | do(T=0), C=c]` = `($15 − $20) × c` = `−$5c`.

Indirect effect (along `T → C → R`, at baseline price): the change in `C` caused by `T` times the change in `R` caused by `C`, all at the reference revenue-per-converter. Change in `C`: `+0.02`. Change in `R` per unit change in `C`, at `T=0`: `$20`. Indirect contribution: `+0.02 × $20` = `+$0.40` per visitor.

(Aside on what I just did, because the careful reader will catch the subtle move. I computed the indirect effect using the reference revenue-per-converter — the `T=0` per-converter price — rather than the treated price. That is one of two ways to do it; the other is to use the treated price `$15`, which would give `+0.02 × $15` = `+$0.30`. The two are different decompositions; in the natural-effects framework they are the "pure" and "total" indirect effects. The total effect of `$0.10` ends up the same either way, but it splits differently between direct and indirect. This is exactly the natural-effects subtlety I signposted in Section 4 — the decomposition is not unique when there is interaction between `T` and `C` on `R`. The fact that lower `T` also reduces the per-converter contribution to `R` is precisely such an interaction. Honest answer: a clean decomposition requires either no `T`-by-`C` interaction or an explicit choice of which reference to fix. For this worked example I have chosen the `T=0` reference; document the choice in your own writeups.)

Total effect: direct plus indirect (with the convention noted above) ≈ `−$0.30 + $0.40` = `+$0.10`. The arithmetic closes within rounding for the reference convention I used. The reader who runs the numbers with the treated-price reference will get a different split but the same total.

**The policy question, applied.**

The product manager wants to know: *should we run the price cut?* Question is *total effect*. Right number: `+$0.10` per visitor. Ship.

The growth-team strategist wants to know: *of the $0.10 lift, how much is volume and how much is per-converter retention?* Question is *direct vs. indirect decomposition*. Right numbers: roughly `−$0.30` direct (per-converter), roughly `+$0.40` indirect (volume), `+$0.10` total. Most of the win is volume.

The finance team wants to know: *if conversion happened to stay at the old rate — say a competitor matches our cut — what does the price reduction do to revenue per visitor?* Question is *controlled direct effect at `c = 0.04`*. Right number: `−$0.20` per visitor. Under that scenario, do not cut.

Three correct analyses. Same DAG. Same data. Three numbers. Each is the right number for the question it answers. None is the answer.

**An honest limit.**

The worked example assumed no unmeasured confounder of `C` and `R`. That is the strong assumption I flagged in Section 4 for direct-effect identification. In a real pricing experiment, things like *visitor-source channel* or *device type* might affect both conversion and revenue per converter, and if those are unobserved or unbalanced, the conditional-on-`C` analysis carries `M→Y` confounding bias on top of the structural effect we computed. The total-effect analysis (no conditioning on `C`) does not have this problem — randomization of `T` handles the `T→R` identification. Mediation analysis is harder than confounder analysis because you need *two* identification arguments: one for `T→Y` and one for `M→Y`. VanderWeele 2015 is the careful treatment. The chapter has done its job if you carry forward the awareness that direct-effect estimates require more assumptions than total-effect estimates do.

---

## 8. Chapter summary

What you can do at the end of this chapter that you could not do at the start:

- **Identify a mediator by structural position.** A variable downstream of treatment, on a forward path to outcome. Arrow from `X` in, arrow to `Y` out.
- **Predict the consequence of conditioning on a mediator.** The indirect effect along the forward path through the mediator is removed from the estimate. What remains is the direct effect for the stratum at which `M` is fixed.
- **Distinguish total effect, direct effect, and indirect effect.** Three different estimands. Each answers a different policy question. None is universally "the right one."
- **Choose between total and direct effect explicitly.** Write down the decision the analysis is feeding, in plain English. Derive the conditioning from the decision, not the other way around.
- **Distinguish controlled from natural direct effects.** Controlled requires weaker assumptions, answers a narrower question, is what your tools return by default. Natural requires stronger assumptions (sequential ignorability), answers a more elegant question, requires sensitivity analysis to defend.
- **Distinguish mediator from moderator.** Mediator is on the path; moderator is to the side. Diagnostic: *does the variable respond to treatment?*
- **See the symmetry with Chapter 5.** Same conditioning operation in code. Opposite consequence on the DAG. Only the structural knowledge tells you which case you are in.

This chapter is the second toolkit-building chapter of Act Two, and it is the first chapter that gives you something to *not* do on Monday. Find a model you already work with. Find the variables in your adjustment set. Check each one. Was that variable measured *after* treatment was assigned? If yes, the variable is at least possibly a mediator, and conditioning on it is at least possibly changing your estimand. The audit is mechanical. The conversation it provokes with your team about what question the analysis is *for* is the actual artifact.

---

## 9. Bridge to Chapter 7

A reader who has paid close attention has a question.

In Section 6 I said the same variable can play different roles depending on the query. A confounder for one analysis, a mediator for another, depending on which `X` and `Y` you have in mind.

That is true so far as it goes. But there is a third role, one I have been carefully not naming, that does not fit either Chapter 5 or Chapter 6's logic. The variable is downstream of *both* treatment and outcome — it has arrows coming *in* from both sides. It is not a confounder (not upstream of treatment). It is not a mediator (not on the forward path *from* treatment to outcome). It is a different structural position. The conditioning rule that applies to it is different from the rule that applies to either of the variables you have learned so far.

In fact — and this is the part that should bother you in the right way — for this third role, the rule reverses again. For a confounder: condition on it to close a backdoor. For a mediator: do not condition on it, or you close a forward path you wanted open. For the third role: *not* conditioning leaves the path closed, and conditioning *opens* it. Same DAG move. Third consequence. The structural rule is a third one.

I am going to make you wait a chapter for the name. The reason is pedagogical: I want you to come at the third case fresh, without the label doing the thinking for you. Next chapter is when the rule shows up. You are going to recognize the structural shape before you learn what it is called.

The short preview: conditioning on a confounder removes bias. Conditioning on a mediator removes effect. Conditioning on the third thing — *creates* bias that was not there before. Same syntax. A third opposite consequence. The DAG is still the only thing telling you which case you are in.

---

## Exercises

**Warm-up.**

1. **(Analyze)** Given the DAG with edges `X → M`, `M → Y`, `X → Y`, list every path from `X` to `Y`. For each path, state whether conditioning on `M` would close it. State the consequence for the estimate of the total effect of `X` on `Y` of including `M` in the adjustment set.

2. **(Apply)** Given the DAG with edges `U → X`, `U → Y`, `X → M`, `M → Y`, write a minimal adjustment set for the *total* effect of `X` on `Y`. Write a minimal adjustment set for the *direct* effect of `X` on `Y` controlling at `M=m`. Verify that the two sets are different, and state in one sentence why.

**Application (Part A).**

3. **(Evaluate)** A team running an A/B test on a new search-ranking algorithm reports the following analysis: *we regressed 30-day retention on the treatment indicator, controlling for click-through rate during the experiment, session length during the experiment, and number of searches per session during the experiment.* The estimated effect is small and not statistically significant. Read this analysis. Identify each variable in the control set as a likely mediator, likely moderator, or likely confounder. State explicitly which estimand the analysis is now estimating. Write the one-paragraph note you would send the team. (You may invoke `[verify]` for any structural claim that depends on platform-specific details you cannot confirm — the goal is the structural read, not the empirical one.)

**Application (Part B — own domain).**

4. **(Evaluate, Create)** Pick a treatment–outcome pair from a model or experiment you have worked on. Draw the DAG. Identify at least one mediator on the forward path from treatment to outcome. State the *policy question* the analysis is feeding, in two plain-English sentences. From the policy question, derive whether you want the total effect or the direct effect. From that derivation, write the conditioning decision: which variables enter the adjustment set, which do not. Defend each decision in one sentence. This becomes the second artifact in your Defend-Your-DAG portfolio (the first was Chapter 5's unmeasured confounder).

**Synthesis.**

5. **(Analyze)** Chapter 5 taught that conditioning on a confounder is good (closes a backdoor) and that "control for everything you can measure" is wrong because it can also condition on non-confounders. Use Chapter 6's machinery to give a concrete worked counter-example: a DAG where conditioning on the "obviously correlated" variable does the wrong thing, and explain in one paragraph what structural role the variable plays and why the conditioning fails. You may use a stylized example or one from your domain. Cite the structural claim you are using.

**Challenge.**

6. **(Evaluate)** Find a published paper (or industry blog post) that performs a mediation analysis using the [Baron and Kenny (1986)](https://psycnet.apa.org/doi/10.1037/0022-3514.51.6.1173) four-step procedure. Re-read its Step 1 — the requirement that a significant total effect must exist before mediation can be tested. Using either [Zhao, Lynch, and Chen (2010)](https://doi.org/10.1086/651257) or [Hayes (2009)](https://doi.org/10.1080/03637750903310360), write a one-paragraph audit: which of the paper's Baron-Kenny steps survive in the modern structural framework, which have been retired, and what conclusion the paper drew that the modern framework would either upgrade, downgrade, or leave alone. If you find a paper whose conclusion the modern framework reverses, that is the best kind of find — bring it to office hours.

---

## LLM exercise

Open Claude, ChatGPT, or Gemini. Paste this prompt exactly.

```
I am designing a causal analysis. The treatment variable is [PICK ONE: a new
recommendation-ranking policy / a price reduction on a subscription plan /
a new onboarding flow for first-time users / a search-relevance model
upgrade]. The outcome variable is [PICK CORRESPONDING: 90-day user
retention / monthly revenue per visitor / 30-day feature adoption /
satisfaction at session end].

Please give me:
(1) A list of at least four candidate mediators between the treatment and
the outcome — variables that are plausibly downstream of treatment and
upstream of outcome, on the causal path.
(2) For each mediator, state in plain English what mechanism the mediator
represents.
(3) For each mediator, state whether conditioning on it would estimate the
total effect, the direct effect (at fixed mediator level), or destroy a
meaningful indirect effect that the analysis wanted to include.
(4) For a final question — "should we ship this treatment?" — recommend
total or direct effect estimation, with one-sentence justification.

Be explicit about what would make your mediator-vs-moderator classification
wrong.
```

Now critique what you get back. For each candidate mediator:

- *Is the variable structurally downstream of treatment?* Apply the diagnostic from Section 5: *does the variable respond to the treatment?* If yes, treat as a candidate mediator. If no, the LLM has given you a moderator under the wrong label.
- *Is the LLM's effect-type classification correct?* The LLM should say *conditioning on a mediator estimates the direct effect (or controlled direct effect, depending on framing), and removes the indirect effect from the total*. If it confuses these, the LLM is reasoning from generic statistical priors rather than from the structural framework. Flag it.
- *Does the LLM correctly identify the right effect for the policy question?* For "should we ship this?", the right answer is total effect, no conditioning on the mediator. If the LLM recommends conditioning, it is making the diversity-case error from Section 1. Flag it.

Write a one-paragraph note on where the LLM was useful (probably: enumerating candidate mediators broadly) and where it was not (probably: the policy question → estimand mapping, which is the irreducibly human move this chapter is about). Save the note for your portfolio.

---

## AI Use Disclosure (Part A standard form)

Per the course's AI Use Disclosure standard:

1. Name the LLM(s) used and the date of each session.
2. State which exercises you used an LLM for and what you used it for in each.
3. For each LLM-generated claim that survived into your final submission, state the source you used to verify it.
4. For each LLM-generated claim that did not survive, state briefly why you removed it.

**Part B bonus criterion:** Submissions naming the total-vs-direct effect choice *with the explicit policy question that drives it* in their own domain receive Part B credit. The named question must (a) be plausibly real in the domain, (b) imply unambiguously which estimand the analysis serves, and (c) drive a specific conditioning decision that follows from the choice.

---

## Key terms

- **Mediator** — a variable occupying a position on a directed (causal) path from treatment to outcome. Arrow in from `X`, arrow out to `Y`. Conditioning on a mediator blocks the part of the effect that flows through it.
- **Total effect** — the effect of treatment on outcome along *every* pathway, including all mediated pathways. The deploy-or-don't number. Notation: `P(Y | do(X)) − P(Y | do(X'))`.
- **Direct effect** — the effect of treatment on outcome *not* through a specified mediator. Estimated by conditioning on the mediator (controlled direct effect) or by isolating the non-mediated counterfactual (natural direct effect).
- **Indirect effect** — the effect of treatment on outcome *through* the mediator. Total effect minus direct effect in the simplest decomposition; more carefully, the change in `Y` produced when `T` changes the mediator and the mediator changes `Y`.
- **Controlled direct effect (CDE)** — the direct effect when the mediator is held fixed at a specified value `m`. Requires `X→Y` and `M→Y` identification assumptions.
- **Natural direct effect (NDE)** — the direct effect when the mediator behaves as it would have under the reference value of treatment. Requires sequential-ignorability assumptions that are not testable from observational data alone.
- **Indirect path** — a directed path from `X` to `Y` that passes through a mediator. Distinguishes from the *direct path* `X → Y` and from any backdoor path beginning with an arrow into `X`.
- **Moderator** — a variable whose level changes the strength or direction of the `X → Y` effect, but which does not sit on the causal path. Modeled as an interaction term. Conditioning on a moderator estimates heterogeneous effects, not direct effects.
- **Mediation formula** — Pearl's expression of the natural indirect effect in terms of observable conditional distributions, under sequential-ignorability assumptions. Pearl (2001).
- **Overadjustment (mediator variant)** — conditioning on a post-treatment variable on the forward path, thereby removing part of the total effect from the estimate. The mediator-side counterpart of the Chapter 5 overadjustment story.

---

## Further reading

1. **Pearl, J. (2001).** "Direct and Indirect Effects." *Proceedings of UAI '01*. [PDF](https://ftp.cs.ucla.edu/pub/stat_ser/r273-u.pdf). The DAG-side foundation for the modern mediation framework. The *mediation formula* introduced here is the source of every natural-effects estimator we have today. Read after Sections 2–3 of this chapter for the formal version.

2. **VanderWeele, T. J. (2015).** *Explanation in Causal Inference: Methods for Mediation and Interaction*. Oxford University Press, Chapter 2. The contemporary textbook treatment of mediation, careful and complete. The book is paywalled and excellent. Read Chapter 2 for natural-vs-controlled direct effects in formal language and for the identification conditions sequential-ignorability requires.

3. **Robins, J. M., & Greenland, S. (1992).** "Identifiability and Exchangeability for Direct and Indirect Effects." *Epidemiology* 3(2), 143–155. [JSTOR](https://www.jstor.org/stable/3702894). The founding paper for the counterfactual definition of direct and indirect effects. Pearl 2001 is the DAG translation; this is the potential-outcomes original.

4. **Zhao, X., Lynch, J. G., & Chen, Q. (2010).** "Reconsidering Baron and Kenny: Myths and Truths about Mediation Analysis." *Journal of Consumer Research* 37(2), 197–206. [DOI](https://doi.org/10.1086/651257). The clean modern critique of the Baron-Kenny procedure; written for an applied audience and a useful bridge for engineering readers who have encountered the older framework.

5. **Imai, K., Keele, L., & Tingley, D. (2010).** "A General Approach to Causal Mediation Analysis." *Psychological Methods* 15(4), 309–334. [DOI](https://doi.org/10.1037/a0020761). The statistics-register treatment, widely cited and tooling-aligned with the `mediation` R package. Read for the identification conditions and for examples that match the engineering reader's likely workflow.

6. **Hayes, A. F. (2009).** "Beyond Baron and Kenny: Statistical Mediation Analysis in the New Millennium." *Communication Monographs* 76(4), 408–420. [DOI](https://doi.org/10.1080/03637750903310360). The methodological transition document that retired Baron-Kenny's first step in the social-science literature.

7. **Hernán, M. A., & Robins, J. M. (2020).** *Causal Inference: What If*, Chapter 21 ("Causal Mediation Analysis"). [Free PDF](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/). The epidemiology contemporary reference. Pairs well with VanderWeele for the formal apparatus.

8. **Schisterman, E. F., Cole, S. R., & Platt, R. W. (2009).** "Overadjustment Bias and Unnecessary Adjustment in Epidemiologic Studies." *Epidemiology* 20(4), 488–495. [DOI](https://doi.org/10.1097/EDE.0b013e3181a819a1). The mediator-conditioning failure mode written for applied readers. Re-read alongside the corresponding Chapter 5 entry.

---

## Draft flags

- `[verify-KDD-2019-full-citation]` — Pantry notes flag a KDD 2019 paper, *"Direct and Indirect Effects in A/B Tests through Causal Mediation Analysis,"* with a Hongliang Jie PDF URL ([source](https://www.hongliangjie.com/publications/kdd2019_2.pdf)). I did not perform a live web verification in this draft; the cold open in Section 1 is therefore deliberately written as a structural composite rather than as a hard cite of that paper. If the KDD 2019 citation verifies (full author list, exact title, page numbers), Section 1 can be rewritten to anchor the cold open in the documented case.
- `[verify-Microsoft-LinkedIn-Netflix-named-case]` — The cold open invokes a recommendation-platform mediator-conditioning failure mode. Deng, Xu, Kohavi & Walker (2013, WSDM) on variance-reduction-via-pre-experiment-data is the closest published reference for the *general practice*; I have not found a single named, post-mortemed A/B test in the public Microsoft Experimentation Platform, Netflix Tech Blog, or LinkedIn Engineering blog that I can cite as the specific case. Section 1's "pick whichever platform you like" framing is deliberate. If a stable named case turns up (the documented Bing 1% A/B test from the 2013 Deng et al. lineage is the most likely candidate), the cold open can become a named instance.
- `voice-anchored: partial` — Root `style/` is the fry-voice spec; no per-book `style/` exists for `causal-reasoning`. The chapter is written in the feynman default voice per CLAUDE.md §6 and chapter-brief directive, and calibrated against Chapter 5's in-book precedent.
- `[verify-natural-effects-decomposition-reference-convention]` — In Section 7's worked example, the indirect-effect computation uses the `T=0` per-converter revenue as the reference. The natural-effects literature distinguishes "pure" and "total" indirect effects depending on this choice, and the textbook treatment in VanderWeele 2015 Ch. 2 names the conventions formally. The chapter signposts the issue but does not litigate it. If a careful reader of VanderWeele points out the chapter's convention is non-canonical, the worked example should be re-derived with the canonical convention.

---

**What would change my mind:** If a careful review of recent industry A/B testing literature (Microsoft, LinkedIn, Netflix, Meta) showed that engineering teams reliably distinguish post-treatment from pre-treatment covariates in their default tooling — that is, if "mediator conditioning by another name" is no longer a documented failure mode in practice — I would soften the chapter's diagnostic emphasis and lean harder on the natural-vs-controlled-effects distinction, which is more pedagogically scarce.

**Still puzzling:** I do not yet fully understand how to teach the natural-effects identification assumptions (sequential ignorability, cross-world independence) without either oversimplifying — to the point where the student leaves thinking natural effects are estimable like any other effect — or burying the student in formalism that Week 6 cannot carry. The chapter's signposting move is a compromise, and I am not satisfied with it.

---

**Tags:** mediator, total-vs-direct-effect, Pearl-2001, VanderWeele-2015, Baron-Kenny-critique
