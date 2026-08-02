# Chapter-by-Chapter Scope: 9-Chapter Theory Spine


## TL;DR

- Target length per chapter: ~5,000-7,000 words.
- The chapter moves through Chapter 1: Why Causal Inference?, Chapter 2: The Language of Causal Diagrams, Chapter 3: Confounding and Adjustment, Chapter 4: Randomization and Its Limits, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

Target length per chapter: ~5,000-7,000 words. Total spine: ~50,000 words, plus student cases. Kindle-handbook format.

---

## Chapter 1: Why Causal Inference?

**Capability build:** After this chapter the reader can distinguish causal questions from predictive questions, recognize which rung of the causation ladder a given question sits on, and articulate why statistics alone has historically failed at causal questions.

**Opening:** The bleeding-George-Washington story, compressed. Doctors for 2,000 years believed disease was caused by humor imbalances, bled patients, killed many of them, and had no way to see they were wrong. The question "does bleeding cause death or cure disease?" is a causal question. It cannot be answered by correlation. This is why causal inference exists.

**Core content:**

- The three levels of causation. Observation ("what is?") — Intervention ("what if I do?") — Counterfactual ("what if I had done differently?"). Each level answers questions the levels below it cannot. Examples at each level: what's the probability someone with a headache took aspirin (rung 1), what happens if we give everyone aspirin (rung 2), would Joe's headache have gone away without aspirin (rung 3).

- Why correlation is not causation, with real examples: ice cream sales and crime rates, divorces in Maine and margarine consumption, chocolate consumption and Nobel prizes. Spurious correlation is the default; genuine causation is the exception.

- The 80-year prohibition. Galton and Pearson discovered correlation in the 1890s and then, failing to solve causation, declared it outside the scope of science. Generations of statisticians internalized "correlation is not causation" as a prohibition on ever asking causal questions. The field eventually recovered but the damage shaped modern statistics.

- What causal inference actually does. Given a causal question and observational or experimental data, causal inference tells you (a) whether the question can be answered with the data you have, (b) under what assumptions, and (c) how. It does not invent causal knowledge; it connects causal knowledge to data.

- The role of a causal model. You cannot answer a causal question from data alone. You need a model — a structured statement of assumptions about how the variables in your problem relate. Data plus model gives you causal answers. Data alone gives you correlations.

**Closing:** A preview of the book's structure. Chapter 2 gives you the language for writing down causal models. Chapters 3-8 teach you how to use those models to answer causal questions under different conditions. Chapter 9 teaches you how to read the student cases that follow, and how to read causal claims in the wild.

**Tone notes:** This is the chapter that hooks readers who aren't yet sure why they should care. Pearl's historical storytelling works well here — Fisher, Snow, Washington. Keep the math minimal; this chapter is about motivation and framing.

---

## Chapter 2: The Language of Causal Diagrams

**Capability build:** After this chapter the reader can read a causal diagram, draw one from a verbal story, identify chains, forks, and colliders, and trace paths through a diagram to find whether two variables are statistically associated.

**Opening:** Soul Wright's 1920 paper on guinea pig coat colors. The first causal diagram ever published, drawn before anyone knew what to call it. The statistics community mocked it; it took 60 years to catch on. But the picture Wright drew is essentially the same picture used today to reason about causation across every applied field. Causal diagrams are that fundamental.

**Core content:**

- What a causal diagram is. Nodes for variables, arrows for direct causal effects. An arrow from A to B means "A has some causal effect on B." Absence of an arrow means "no direct effect, given the other variables in the diagram." The absence is as important as the presence.

- Drawing a diagram from a story. Work through a real example — maybe the smoking / tar / cancer causal chain, or the Berkeley admissions example. Show how each claim in the story translates to an arrow, and how the arrows together produce a diagram.

- Three building blocks. Chains (A → B → C): information flows from A to C through B. Forks (A ← B → C): A and C are correlated because B causes both. Colliders (A → B ← C): A and C are independent, but conditioning on B creates a spurious association between them.

- Paths and path-tracing. What a path is. Directed paths vs paths with reversed arrows. Back-door paths. Front-door paths. How two nodes can be connected through many paths simultaneously.

- The collider is the weird one. Every student gets chains and forks quickly. Colliders violate intuition and are the source of most advanced-level confusion in causal inference. Work a concrete example: two independent traits both causing hospital admission; conditioning on admission status induces a spurious correlation between the traits (Berkson's paradox). The selection effect in dating: you'll date either attractive people or nice people, so in your dating pool attractiveness and niceness look negatively correlated even though they're independent in the general population.

- d-separation conceptually. Without going into the full formal rules, explain the idea: a path is "blocked" if conditioning on any non-collider variable on the path, or if the path contains a collider that you haven't conditioned on. Two variables are d-separated by a set Z if every path between them is blocked by Z. When two variables are d-separated, they are statistically independent given Z.

- Mediators. A mediator is a variable on a directed path from cause to effect. Smoking → tar → cancer makes tar a mediator. Mediators are not confounders. Controlling for a mediator is often a mistake — it blocks the causal effect you're trying to measure. This is important enough that it gets its own warning in this chapter and is reinforced in Chapter 3.

**Closing:** The diagram is not just a picture. It is a compact statement of all the causal assumptions you're making, and every downstream conclusion will inherit those assumptions. Draw the diagram honestly. The rest of the book assumes you can.

**Tone notes:** This is the most technically demanding chapter and the most load-bearing. Every subsequent chapter uses this vocabulary. Be patient. Use lots of diagrams. Walk through at least three extended examples in full.

---

## Chapter 3: Confounding and Adjustment

**Capability build:** After this chapter the reader can identify confounders in a causal diagram, apply the back-door criterion to find a valid adjustment set, recognize the most common mistakes (mediator fallacy, collider conditioning, M-bias), and compute an adjustment from data when given a sufficient set of deconfounders.

**Opening:** The Simpson's paradox example, worked in full. A drug appears bad for men, bad for women, but good for people. What does it actually do? The answer depends entirely on the causal diagram. Show the two diagrams that produce the same data but opposite conclusions (gender as confounder vs blood pressure as mediator). The data cannot tell you which diagram is right. You need the causal model.

**Core content:**

- What confounding actually is. A confounder is a variable that affects both the treatment and the outcome, creating a non-causal association between them. Equivalently, a confounder opens a back-door path from treatment to outcome. Confounding is why observing a correlation is not enough to conclude causation.

- The back-door criterion. Pearl's formulation: to estimate the causal effect of X on Y, find a set Z of variables such that (a) Z blocks every back-door path from X to Y, and (b) Z contains no descendants of X. When you can find such a Z, you can estimate the causal effect by adjusting for Z. Walk through this with increasingly complex diagrams.

- Adjustment as a computation. Once you have a valid Z, you stratify the data by levels of Z, compute the treatment-outcome association within each stratum, and take a weighted average. This is adjustment in its rawest form. Regression adjustment is the parametric version of the same idea. Propensity score methods (Chapter 5) are the same idea again with a different computational shortcut.

- The mediator fallacy. Conditioning on a mediator is one of the two most common causal inference mistakes. Walk through a concrete example where a researcher controls for a variable that lies on the causal pathway, finds the treatment effect vanishes, and wrongly concludes the treatment doesn't work. The effect was real; the adjustment destroyed it.

- The collider fallacy. The other most common mistake. Controlling for a collider creates a spurious association where none existed. The Berkeley admissions reversal example works well here. So does Berkson's bias — hospital-based studies routinely get this wrong.

- M-bias. A subtle case where a pre-treatment variable looks like a confounder but is actually a collider in disguise. This is the example that generations of statisticians got wrong because they couldn't see the diagram. Work it through carefully.

- What if you can't find a valid adjustment set? Sometimes no combination of observed variables blocks all the back-door paths. This doesn't mean causal inference is impossible — it means you need different tools (Chapters 6, 7, 8). But it does mean you should stop trying to force an adjustment that won't work.

**Closing:** Adjustment is the first and most fundamental tool of causal inference. When it works, it gives you the causal effect directly. When it doesn't, the diagram tells you that too — and points you toward the methods in the following chapters.

**Tone notes:** This is the conceptual workhorse. Spend time on examples. Every reader needs to leave this chapter understanding the difference between a confounder, a mediator, and a collider, and knowing which ones to adjust for.

---

## Chapter 4: Randomization and Its Limits

**Capability build:** After this chapter the reader can explain why a randomized controlled trial produces valid causal estimates, recognize when randomization is infeasible or unethical, and articulate the bridge from experimental to observational methods that the rest of the book builds.

**Opening:** The book of Daniel, with reading it seriously as a controlled experiment. Daniel proposed to feed himself and his companions vegetables for ten days while other young men ate the king's meat. "As thou seest, deal with thy servants." This is a prospective controlled trial with a treatment group, a control group, and a clear decision rule. Ancient. The principle is not modern.

**Core content:**

- What randomization does. Randomization breaks all back-door paths between treatment and outcome because it severs the treatment's dependence on every other variable, measured or unmeasured. That's the whole trick. Randomization is a way of guaranteeing that no confounding exists, without having to know what the confounders would have been.

- The skillful interrogation of nature. Fisher's insight: nature answers the question we actually ask, not the question we meant to ask. If we ask about the yield on these plots given whatever determined which fertilizer they got, she answers that question — including all the confounding effects. Randomization changes the question we're asking into the question we want answered.

- RCTs in practice. Treatment groups, control groups, blinding, placebo effects. Why these protocols exist. The palm trial (Ebola treatments) as a contemporary example of what a well-run RCT looks like. The smoking-and-cancer studies of the 1950s as an example of what happens when you can't run an RCT.

- Why we can't always randomize. Ethics (you can't assign people to smoke). Practicality (you can't assign people to live in certain cities). Cost (some RCTs cost millions of dollars). Feasibility (you can't randomize history). In economics, medicine, epidemiology, and public policy, most interesting questions can't be answered by an RCT.

- Non-compliance and the intent-to-treat problem. Even when you run an RCT, people don't always do what you assigned them to do. This complicates the analysis and sets up the instrumental variables chapter (Chapter 7).

- The bridge to observational methods. If randomization is the gold standard because it breaks all back-door paths, then observational methods work by doing the same thing through different means — by identifying and adjusting for the back-door paths directly (matching, weighting, regression), or by finding natural experiments that approximate randomization (IVs), or by modeling the causal structure densely enough to extract causal estimates (counterfactual methods).

**Closing:** Randomization is the cleanest way to answer a causal question. It's not always available. The rest of this book is about what to do when it isn't.

**Tone notes:** Medium-length chapter. Sets up the structural transition from "ideal world (RCT)" to "real world (everything else)." Keep RCT methodology coverage light — readers who need full RCT methodology should go to a dedicated trials textbook.

---

## Chapter 5: Matching

**Capability build:** After this chapter the reader can describe how matching methods work, explain the role of the propensity score, assess covariate balance, recognize the limitations of matching (especially hidden bias), and interpret a matched-study result from the causal inference literature.

**Opening:** The smoking / periodontal disease study. Smokers have much more periodontal disease than non-smokers, but they also differ in age, sex, income, education, and race. Is the observed difference due to smoking, or to the other factors? Matching is the method that tries to answer this question by constructing a comparison group of non-smokers who look like the smokers in every measurable way.

**Core content:**

- The matching idea. Pair each treated individual with a control individual who has similar values of the measured covariates. Analyze the matched pairs instead of the raw data. When the matching is good, the analysis approximates what a randomized trial would have shown.

- Exact matching and its limits. With a few binary covariates you can match exactly — treated male aged 45 with control male aged 45. With many covariates, especially continuous ones, exact matches become impossible. You need a notion of similarity.

- Distance metrics. Mahalanobis distance and its robust variants. How to measure how close two individuals are across many covariates. This is where the machinery starts.

- The propensity score. Rosenbaum and Rubin's 1983 insight: you can collapse all the covariates into a single number — the probability of receiving treatment given the covariates — and match on that number. Under certain assumptions, propensity score matching gives you the same balance that matching on all the covariates would. This is a huge computational simplification.

- Greedy matching vs optimal matching. Algorithms for actually finding the matches. Greedy is fast and usually good enough. Optimal minimizes total distance across all pairs and matters when matches are hard to find.

- Balance assessment. After matching, you have to check that the treated and control groups actually look similar. Standardized mean differences across covariates. Visual checks. If balance fails, matching failed, and your causal estimate is contaminated.

- Sensitivity to hidden bias. The fundamental limit of matching: you can only match on covariates you measured. If there's a confounder you didn't measure, matching doesn't help. Rosenbaum's sensitivity analysis framework — how much unmeasured confounding would it take to overturn the observed result? If a little, your result is fragile. If a lot, your result is robust.

- Adjustment as matching's cousin. Regression adjustment, stratification, and matching are three computational approaches to the same conceptual operation: estimating the causal effect within strata of the confounders and averaging. Matching is the most transparent; regression is the most common; stratification is the oldest. Pick the one that fits your data.

**Closing:** Matching is the most intuitive method of observational causal inference. When your confounders are all measured, matching works. When they aren't, you need something more.

**Tone notes:** This is the first heavily-methodological chapter. Expect it to run long — matching has a lot of machinery. Use a single extended example throughout (the smoking / periodontal study is good) rather than jumping between examples for each technique.

---

## Chapter 6: Weighting Methods

**Capability build:** After this chapter the reader can explain inverse probability of treatment weighting, understand what a pseudo-population is, recognize when weighting is preferable to matching, and interpret a weighted analysis from the literature.

**Opening:** A matching problem where matching fails. Suppose you have a treatment that's assigned unevenly across subgroups — most treated subjects are young, most controls are old. Matching will discard huge portions of the data because there aren't enough old treated subjects to match against the young ones. You lose statistical power. Weighting offers a different approach: keep every subject, but reweight them so the treatment and control groups collectively look balanced.

**Core content:**

- The weighting idea. Give each subject a weight equal to 1 / probability of receiving their actual treatment. Treated subjects get weighted by 1 / P(treatment). Control subjects get weighted by 1 / (1 - P(treatment)). The reweighted population is called a pseudo-population, and in it, treatment is effectively randomized.

- Why this works. Conceptually: if treated subjects were three times as rare as controls among young people, you count each young treated subject three times when computing the treatment effect. This compensates for their under-representation and restores balance.

- The propensity score returns. The weight depends on the probability of receiving treatment given the covariates — the same propensity score used in matching. Weighting and matching are two ways of using the same quantity. Weighting uses everyone; matching uses a subset.

- Marginal structural models. IPTW is often implemented inside a marginal structural model — a regression fit to the weighted population. Introduce this briefly without going deep into the technical machinery. The reader should know the name and what it's for.

- Balance diagnostics for weighting. Just as matching requires balance checks, weighting requires checking that the weighted population is actually balanced. Standardized mean differences, weighted. If balance fails, the weights aren't doing their job.

- The weight problem. If some subjects have very extreme propensity scores — close to 0 or close to 1 — their weights become enormous, and a few subjects dominate the analysis. This produces unstable estimates. Weight truncation and stabilized weights are the standard responses.

- Doubly robust estimation. A methodological idea worth introducing: combine a model for the outcome and a model for the treatment, and the resulting estimator is consistent if either model is correct. This is the motivation for methods like Double ML, which the Chapter 9 terminology discussion will pick up.

- When to use weighting vs matching. Weighting is more statistically efficient (uses all the data). Matching is more transparent (you can see exactly who was compared to whom). Weighting handles continuous treatments more naturally. Matching handles situations where a few exact matches are more informative than many rough ones. Neither is universally better.

**Closing:** Weighting and matching are cousins. They solve the same problem — adjusting for measured confounders — with different computational trade-offs. A reader who understands both can read most observational causal inference literature.

**Tone notes:** Shorter than Chapter 5, since it's building on the same conceptual foundation. Focus on the weighting-specific ideas — the pseudo-population, the weight instability problem, doubly robust estimation — and cross-reference back to Chapter 5 for balance diagnostics.

---

## Chapter 7: Instrumental Variables

**Capability build:** After this chapter the reader can explain what an instrumental variable is, recognize the three core assumptions (relevance, exclusion, monotonicity), interpret 2SLS output, and critically evaluate a paper that claims an instrumental variables identification strategy.

**Opening:** John Snow and the Broad Street pump. The water companies in 1850s London drew water from different parts of the Thames — one upstream of the sewers, one downstream. Snow realized that which company served your house was essentially random with respect to every other thing about you, but it dramatically affected your exposure to cholera. Water company was an instrumental variable for cholera exposure. This was instrumental variables analysis a century before the method had a name.

**Core content:**

- The basic idea. An instrumental variable Z affects the treatment X, but has no direct effect on the outcome Y — its only path to Y runs through X. When you find such a Z, you can use variation in Z to estimate the causal effect of X on Y, even when X and Y are confounded. The confounding doesn't touch Z.

- The three assumptions. Relevance (Z really does affect X). Exclusion (Z affects Y only through X). Monotonicity (Z doesn't flip people — no one takes the treatment when Z says no while also refusing it when Z says yes). These assumptions are not verifiable from data. They're scientific claims you have to defend.

- The encouragement design. Randomized trials with non-compliance are a canonical IV setting. The randomization affects who's encouraged to take treatment, but doesn't force anyone. The treatment group has higher uptake than the control group, and we use the gap to estimate the treatment effect among compliers — people who take treatment if encouraged and refuse if not.

- Compliance classes. Compliers, always-takers, never-takers, defiers. What IV estimates is the local average treatment effect — the effect on compliers, not on everyone. This is a real limitation. If compliers are different from the general population, the IV estimate doesn't generalize.

- Two-stage least squares. The standard computational approach. First stage: regress treatment on the instrument and controls. Second stage: regress outcome on the predicted treatment and controls. The coefficient on predicted treatment is the IV estimate. Walk through this mechanically.

- Mendelian randomization. Genetic variants as natural instruments. They're randomly assigned at conception, they often affect specific traits, and they usually have no direct effect on outcomes of interest. This has become a major approach in medical research.

- Weak instruments. If the instrument's effect on treatment is small, the IV estimator becomes unstable and badly biased. Diagnostics and the "F > 10" rule of thumb. When your instrument is weak, your result is not trustworthy no matter how clever the identification strategy sounds.

- The critical reading question. When someone claims an IV design, the first question is always: is the exclusion restriction defensible? Can you tell a plausible story for why Z affects Y only through X? Most bad IV papers fail this test — the instrument has other paths to the outcome that the authors didn't consider.

**Closing:** Instrumental variables is the most powerful tool for causal inference under unmeasured confounding. It's also the most fragile. When the assumptions hold, IV works. When they don't, IV produces confident-sounding wrong answers.

**Tone notes:** Conceptually demanding. The compliance classes and LATE discussion are the hardest part for most readers. Use the Snow example and at least one contemporary example (like Mendelian randomization for cholesterol) to keep the abstract machinery grounded.

---

## Chapter 8: Counterfactuals and Mediation

**Capability build:** After this chapter the reader can explain what a counterfactual is, work through the three-step computation (abduction, action, prediction), distinguish direct from indirect effects, recognize the mediation formula, and interpret a mediation analysis from the literature.

**Opening:** "Had Cleopatra's nose been shorter, the whole face of the world would have changed." Pascal was asking a counterfactual. Counterfactuals are how humans reason about individual cases, responsibility, blame, regret, and policy. Legal but-for causation is a counterfactual. Medical decisions are counterfactuals. Most interesting causal questions in everyday life are counterfactuals. This chapter is about how to compute them.

**Core content:**

- What a counterfactual is. A statement of the form "if X had been different, Y would have been different." Counterfactuals live on the third rung of the causation ladder — above association, above intervention. They describe outcomes in worlds that didn't happen.

- The fundamental problem. For any individual, you observe one outcome. You never observe both the factual outcome and the counterfactual outcome for the same person. This is what makes counterfactuals hard and why they can't be answered from data alone.

- The structural approach. Counterfactuals can be computed from a causal model. Pearl's three-step procedure: abduction (use the data to infer the individual's idiosyncratic factors), action (change the model to reflect the counterfactual intervention), prediction (compute the outcome in the altered model with the inferred factors).

- A worked example. Use a simple structural causal model — maybe the education / experience / salary example from Pearl, or the firing squad example — to walk through the three steps concretely. Show how the computation proceeds.

- Individual vs population counterfactuals. At the population level, counterfactual questions sometimes reduce to interventional questions we can answer. At the individual level, they depend on structural assumptions. Both kinds of counterfactuals are legitimate and useful.

- Direct and indirect effects. When a treatment affects an outcome through a mediator, we can ask: how much of the effect goes through the mediator, and how much goes directly? These are counterfactual questions, not interventional ones. The natural direct effect is what you'd see if you fixed the mediator at the value it would have had under control while changing the treatment. The natural indirect effect is the residual.

- The mediation formula. Under a suitable causal diagram, natural direct and indirect effects can be computed from the observed data. The formula is not the point; the conceptual distinction is. Direct effect means "the effect when the mediator is held at its baseline." Indirect effect means "the effect produced by letting the mediator respond to treatment."

- Why linear regression mediation analysis is usually wrong. The Baron-Kenny approach — regress Y on X, then on X and M, and attribute the coefficient change to mediation — gives the wrong answer whenever there are interactions between X and M, or whenever the mediator-outcome relationship is confounded. Most published mediation analyses suffer from at least one of these problems.

- Probability of necessity and sufficiency. Refined causal questions: how likely is it that the cause was necessary for the outcome? How likely is it that the cause was sufficient? These matter in law (but-for causation), in epidemiology (attribution of disease to exposure), in climate science (attribution of extreme events to climate change).

**Closing:** Counterfactuals are where causal inference meets human reasoning. Every student case that asks "what if" is making a counterfactual claim, whether it uses the vocabulary or not.

**Tone notes:** The most conceptually abstract chapter. Ground it aggressively in examples. The three-step procedure worked example is the most important single piece of the chapter.

---

## Chapter 9: How to Read a Causal Case Study

**Capability build:** After this chapter the reader can approach any student case in the book (or any causal inference paper in the literature) with a structured set of questions, distinguish rigorous causal claims from loose ones, recognize terminological games, and assess what kind of causal claim is actually being made.

**Opening:** A causal case study is a story about what causes what, backed by data, analysis, and a causal model. Some case studies are rigorous: they name their assumptions, show their diagrams, discuss what would overturn their conclusions. Others dress up correlational claims in causal language and hope the reader doesn't notice. This chapter teaches you to tell the difference.

**Core content:**

- What to look for first. The causal question. What exactly is being claimed to cause what? Is the question about a population or an individual? Interventional or counterfactual? A well-written case study answers these questions in the first paragraph.

- The causal diagram. Every causal claim has an implicit diagram. If the authors drew one, check it. If they didn't, draw it yourself from their description. Is it plausible? Does it include the obvious confounders? Are the arrows oriented correctly?

- The identification strategy. How are the authors claiming to estimate the causal effect? Randomization? Matching? IV? Regression adjustment? Mediation analysis? Whatever they claim, check that their diagram supports it. A matching case with unmeasured confounders is fragile. An IV case with a weak instrument is fragile. A mediation analysis with a confounded mediator is wrong.

- The assumptions. Every causal method has assumptions. Back-door adjustment assumes a sufficient adjustment set. IV assumes exclusion and monotonicity. Mediation assumes no unmeasured mediator-outcome confounding. When the authors don't state their assumptions explicitly, they have them anyway — they're just hoping you won't notice.

- What would change the conclusion. A good case study discusses this. Sensitivity to hidden bias. Alternative models. Robustness checks. When this discussion is absent, the authors are either being careless or hiding something.

- The terminology problem. Causal inference vocabulary is a mess across disciplines. "Control for" vs "condition on" vs "adjust for" — often used interchangeably but with different technical meanings. "Causal effect" with no qualifier — is this the average treatment effect, the effect on the treated, the local effect? They're different and they answer different questions. "Confounder" — means different things in econometrics, epidemiology, statistics, and machine learning. Know the vocabulary of the field the case is written in.

- "Causal AI" and its cousins. Extended example: the buzzword "causal AI" sounds like AI that reasons about causation. It is not. It is ML-assisted estimation of the statistical adjustments required by human-specified causal models. The machine learning provides flexible estimation of nuisance parameters. The human provides the causal model, the identification strategy, and every causal claim. If a case study invokes "causal AI" or similar buzzwords, check what the human actually supplied and what the machine actually did. The marketing almost always exaggerates.

- The interdisciplinary Babel. Economists call it endogeneity. Epidemiologists call it confounding. Statisticians call it bias from omitted variables. Computer scientists call it spurious correlation. Philosophers call it the problem of common causes. These are all names for substantially the same phenomenon — an open back-door path — but the vocabularies don't always translate cleanly. When you read a case across disciplines, check that you're tracking the underlying concept, not just the surface words.

- A structured checklist. By the end of the chapter, the reader should have a short, memorable list of questions to ask of any causal case study: What's the question? What's the diagram? What's the strategy? What are the assumptions? What would overturn it? What's the terminology actually claiming?

**Closing:** The student cases that follow this chapter are the real book. The theory spine exists to equip you to read them. Read actively. Draw the diagrams. Check the assumptions. Be skeptical of the vocabulary. This is what reading causal inference means.

**Tone notes:** Shorter chapter — maybe 4,000-5,000 words. Serves as the bridge between the theory spine and the student cases. The terminology critique (including Causal AI as the extended example) lives here, in service of teaching the reader to read critically, rather than as a standalone polemic.

---

## Chapter sequencing rationale

- **1 → 2**: motivation before machinery. Reader needs to want to learn this before learning the hard part.
- **2 → 3**: diagrams before confounding. You can't understand confounding without the diagram language.
- **3 → 4**: confounding before randomization. The reader needs to understand the problem before understanding why randomization solves it.
- **4 → 5 → 6 → 7**: RCTs, then observational methods in order of increasing sophistication. Matching is the most intuitive. Weighting shares the propensity score machinery. IV is the most conceptually demanding because it handles unmeasured confounding.
- **7 → 8**: IV uses counterfactual concepts (LATE, compliance classes) that set up the counterfactual chapter.
- **8 → 9**: mediation and counterfactuals are the last technical content; Chapter 9 is the exit ramp to the cases.

## Length estimates

| Chapter | Target words | Complexity |
|---|---|---|
| 1. Why Causal Inference? | 5,000 | Low — motivation chapter |
| 2. Language of Causal Diagrams | 6,500 | High — load-bearing vocabulary |
| 3. Confounding and Adjustment | 7,000 | High — conceptual workhorse |
| 4. Randomization and Its Limits | 5,000 | Medium — bridge chapter |
| 5. Matching | 7,000 | High — first methods chapter |
| 6. Weighting Methods | 5,500 | Medium — builds on Chapter 5 |
| 7. Instrumental Variables | 6,500 | High — most demanding method |
| 8. Counterfactuals and Mediation | 6,000 | High — most abstract |
| 9. How to Read a Causal Case Study | 4,500 | Low — synthesis chapter |
| **Total spine** | **~53,000 words** | |

Add 9 student cases at ~1,500-2,500 words each = ~13,500-22,500 more words. Total book: 65,000-75,000 words. This is comfortably within Kindle-handbook range.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Donald Rubin** developed the potential outcomes framework — the Rubin Causal Model — starting in the 1970s. The notation Y(0), Y(1) and the missing-data view of causal inference let researchers reason about counterfactuals when only one outcome is observed per unit.

**Run this:**

```
Who is Donald Rubin, and how does the Rubin Causal Model connect to the chapter scope we covered? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Donald Rubin"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one specific RCM analysis using potential outcomes notation.
- Ask it to compare the Rubin (potential outcomes) and Pearl (graphical) traditions in causal inference — what each emphasizes.

What changes? What gets better? What gets worse?
