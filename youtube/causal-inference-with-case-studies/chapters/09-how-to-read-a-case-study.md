# Chapter 9: How to Read a Causal Case Study


## TL;DR

- A causal case study is a story about what causes what, backed by data, analysis, and a causal model.
- The chapter moves through What a case study is trying to do, The checklist, The terminology problem, Causal AI: the buzzword problem, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

The theory spine ends here. The rest of the book is case studies — nine pieces of applied causal analysis, written by students in a graduate seminar, each applying the methods of the preceding chapters to a problem the student found worth studying. The cases are why this book exists. Everything before this chapter was preparation for reading them.

A causal case study is a story about what causes what, backed by data, analysis, and a causal model. That framing sounds innocuous. In practice, causal case studies — published ones as well as student ones — vary enormously in quality. Some are meticulous. The assumptions are explicit, the diagrams are drawn, the analysis is appropriate to the question, the sensitivity checks are performed, the limits are acknowledged. Others are sloppy. Causal claims are made in loose language, assumptions go unstated, methods are applied ritualistically without attention to whether they fit the problem, and the limitations sections are either missing or perfunctory.

This chapter is about telling the difference. It is about how to read a causal case study with the structured skepticism that good analysis deserves. The goal is not to reject every case study that falls short of perfection — no real analysis is perfect — but to evaluate fairly. A well-executed case study that admits its limits is more trustworthy than a flashy one that hides them. You will learn to recognize which is which.

The chapter also spends time on a broader problem that every reader of causal inference will encounter: the terminology of the field is a mess. "Control for," "condition on," "adjust for" are used interchangeably but with different technical meanings. "Causal effect" floats around without qualifiers specifying which causal effect. "Confounding" means different things in different disciplines. Most damagingly, a new generation of buzzwords — "Causal AI" is the worst offender — markets machine-learning implementations of old ideas as if they were conceptual breakthroughs, obscuring what the machines actually do and what the human analyst still has to provide. Reading the literature critically requires seeing through these terminological games.

This chapter will not teach you anything new about causal inference itself. It is a synthesis and a practical guide. By the end, you should have a checklist you can apply to any case study you encounter — in this book or elsewhere — and a sharper eye for what causal language can and cannot legitimately claim.

## What a case study is trying to do

Before we get to how to read a case study, we should be clear about what a case study is and isn't.

A causal case study is an application. It takes a specific real-world problem, brings the methods of causal inference to bear on it, and tries to answer a specific causal question about that problem. Unlike a methodological paper, which develops or refines a method, a case study applies existing methods to new data. Unlike a textbook chapter, which explains methods in general, a case study shows methods in action. Unlike a purely descriptive empirical study, which reports patterns in data without trying to explain them causally, a case study commits to a causal interpretation.

The commitment to causal interpretation is what makes a case study hard. A descriptive study can hide behind "we observe a correlation between X and Y" and make no further claims. A case study has to say more. It has to posit a causal structure, argue for the structure's plausibility, apply methods appropriate to that structure, and interpret the results causally. Each step introduces opportunities for error.

A well-constructed case study has a specific shape. It begins with a causal question: *does X cause Y, and by how much, in this particular setting?* It proposes a causal model — often explicitly in a diagram, sometimes implicitly in text — that encodes assumptions about how X, Y, and other relevant variables relate. It discusses identification: given the causal model, what assumptions would allow us to estimate the causal effect from the available data? It applies a method (adjustment, matching, weighting, instrumental variables, or some combination) that is appropriate for those assumptions. It reports the results. It conducts sensitivity analyses. It discusses limitations.

Case studies that skip any of these steps are suspect. The most common shortcuts are skipping the causal model (so the reader has no way to check what the author assumed), skipping the identification argument (so the reader can't tell whether the method is appropriate), and skipping sensitivity analyses (so the reader can't assess robustness). A case study that does all these things well is doing real work. One that skips them is often pretending.

## The checklist

Here is a checklist of questions to ask when reading any causal case study. Apply these questions to every case in this book, and to any causal analysis you encounter in the wider literature.

**1. What is the causal question?**

The first question should be answerable in one sentence. What causal effect is being estimated? What is the treatment? What is the outcome? What is the target population?

A case study that cannot state its causal question in one clear sentence does not know what it is trying to estimate, and the rest of the analysis will be correspondingly confused. Watch for slippery formulations: "we examine the relationship between X and Y" is not a causal question. "We estimate the effect of X on Y in population P" is.

Also pay attention to which specific causal effect is being estimated. The average treatment effect (ATE), the average treatment effect on the treated (ATT), the local average treatment effect (LATE), and various subgroup-specific effects are different quantities. A case study that uses a method appropriate for one effect and then interprets the result as another is making a technical error.

**2. What is the causal model?**

The author should have a causal model in mind, and ideally has drawn it explicitly. The model takes the form of a causal diagram — nodes for the relevant variables, arrows for direct causal effects.

If the diagram is explicit, check it. Are the arrows reasonable given domain knowledge? Are important variables missing? Are there arrows that should not be there? The diagram is an assumption, not a fact, and reviewing it is part of evaluating the analysis.

If the diagram is not explicit, draw one yourself from the paper's description. Does the text imply a specific causal structure? Is that structure consistent with the methods the author uses? Cases where the text's implicit model doesn't match the analysis are a red flag.

**3. What is the identification strategy?**

Given the causal model, how does the author claim to identify the causal effect? This is the link between the model and the methods. Is the claim that a set of measured covariates blocks all back-door paths (back-door adjustment, Chapter 3)? Is the claim that an instrumental variable satisfies relevance, exclusion, and independence (Chapter 7)? Is the claim that a natural experiment provides randomization (Chapter 4)?

The identification strategy is where most case studies live or die. A well-identified analysis has a clear argument for why the method can recover the causal effect. A poorly-identified one hand-waves over this step, applying methods mechanically without justifying them.

Specifically, check whether the assumptions required by the method are stated and defended. For back-door adjustment, the key assumption is that the adjustment set is sufficient to block all back-door paths. For instrumental variables, the key assumptions are relevance, exclusion, and independence. For matching, the assumption is ignorability plus overlap. The author should state the relevant assumptions and provide evidence or argument for each.

**4. Are the data appropriate?**

The data should be appropriate to the question and the method. This involves several considerations.

**Sample.** Does the data come from the target population? If the question is about a general population but the data is from a specific sample (e.g., hospitalized patients, college students, people who volunteered for the study), the results may not generalize. Selection bias can creep in through the sample definition.

**Variables.** Are the key variables measured well? A causal analysis of "smoking" requires a good measure of smoking. A measure based on self-report in a survey where smoking is stigmatized is not as good as a measure based on serum cotinine. The quality of variable measurement affects the quality of the causal estimate.

**Covariates.** For back-door adjustment, matching, or weighting, the analysis requires that important confounders are measured. If plausible confounders are missing from the data, the analysis cannot adjust for them, and the results are vulnerable to unmeasured confounding.

**Sample size.** The analysis requires enough data to support the methods used. Propensity score methods with only a few hundred observations are shaky. Instrumental variables methods are sensitive to sample size through the weak-instruments problem.

Look for explicit discussion of data quality. A serious case study acknowledges the limits of the data, not just the limits of the methods.

**5. Are the methods appropriate?**

Given the question and the data, are the methods suited to the task? Common mismatches include:

- Using matching or weighting when there is reason to believe unmeasured confounders matter. These methods adjust only for measured confounders; they cannot save an analysis where the confounding is fundamentally unobservable.
- Using instrumental variables with a weak first stage. If the F-statistic is below 10, the IV estimates are unreliable.
- Using simple regression when the relationship is non-linear or the treatment interacts with covariates. Regression adjustment is only as good as the specification of the regression.
- Using mediation analysis without defending the no-unmeasured-mediator-outcome-confounding assumption. This assumption is strong and often violated.

A method-question match is a positive sign. A method-question mismatch, or using a fancy method where a simple one would suffice, is a warning.

**6. Are the assumptions stated and defended?**

This is the step where most applied analyses cut corners. Every causal method rests on assumptions. A good case study names the assumptions and argues for their plausibility. A bad one either ignores assumptions or lists them perfunctorily without defending them.

For each major assumption, ask: has the author explained why it's reasonable in this context? Has the author considered how it might fail, and if so, how seriously? Are the assumptions verifiable? Back-door adjustment's core assumption (that the adjustment set blocks all back-door paths) is not verifiable from data; it relies on the causal model. IV's exclusion restriction is not verifiable from data. Mediation's no-unmeasured-mediator-outcome-confounding is not verifiable from data. When assumptions are unverifiable, argumentation carries the weight, and the author's argument should be explicit.

**7. Are the results sensible?**

Do the estimates make sense given domain knowledge? A causal effect that is orders of magnitude larger than any plausible mechanism would produce is a red flag. An effect that goes in the wrong direction (a treatment known to be beneficial showing a harmful effect, say) requires explanation.

This is an informal check, but an important one. Numerical results that disagree with strong prior expectations should be greeted with investigation, not acceptance. Either the prior expectation is wrong, or the analysis is wrong, and both options deserve serious attention before moving on.

**8. Are there sensitivity analyses?**

A good case study reports what would change the conclusion. What if the assumed causal diagram is wrong in specific ways? What if there are unmeasured confounders? What if the functional forms are different?

Sensitivity analyses can take many forms:

- **For back-door adjustment and matching**: Rosenbaum-style bounds on how much unmeasured confounding would be required to overturn the result.
- **For instrumental variables**: sensitivity to exclusion violations, tests for pleiotropy in Mendelian randomization.
- **For mediation**: sensitivity to unmeasured mediator-outcome confounding.
- **In general**: results under different specifications, different subsamples, different methods. If the finding persists across variations, it is more robust. If it flips under minor perturbations, it is fragile.

A case study without sensitivity analyses is asking you to take its assumptions at face value. Sometimes this is reasonable (very strong assumptions well-established in the literature), but more often it is a gap. Look for sensitivity checks; their presence is a marker of careful work.

**9. Are the limitations honestly acknowledged?**

Every case study has limitations. The question is whether the author acknowledges them. A limitations section that says "we used appropriate methods and our results are robust" is doing no work. A limitations section that names specific ways the analysis could fail and discusses their severity is doing real work.

Good limitations sections do at least three things: they name the unmeasured confounders that might matter, they discuss the extent to which the findings generalize beyond the sample, and they acknowledge where the causal model might be wrong. Serious case studies treat this section as a place for intellectual honesty, not ritual disclaimers.

**10. Are the conclusions calibrated to the evidence?**

Finally, do the conclusions match what the analysis can support? The strongest case studies are careful with their conclusions. They distinguish between qualitative claims ("the evidence suggests X causes Y") and quantitative claims ("X causes Y by exactly this much"). They distinguish between population-level effects and individual-level effects. They qualify conclusions with "under the assumptions stated, and if the causal model is correct."

Weaker case studies overstate. A LATE is interpreted as an ATE. A conditional association is described as a causal effect. An observational estimate with strong caveats is reported as if it were an experimental result. Watch for language that claims more than the analysis supports.

## The terminology problem

Causal inference has a terminology problem. Part of the problem is simply that the field developed across multiple disciplines — statistics, epidemiology, economics, computer science, philosophy — each with its own vocabulary. Part is that some terms have technical meanings that drift in common usage. Part is that marketing language has recently invaded the field and produced new terms that obscure rather than clarify.

Reading causal case studies critically requires navigating this terminological landscape. You need to know which words are being used precisely, which are being used loosely, and which are being used as window-dressing.

**"Control for" vs. "condition on" vs. "adjust for."** These are often used interchangeably, but they have slightly different connotations. "Condition on" is the most precise; it refers to the statistical operation of examining a relationship within strata defined by a variable. "Adjust for" refers specifically to including a variable in a back-door adjustment. "Control for" is the loosest; in common usage it can mean any of the above. When reading papers, it helps to translate "control for" into the specific operation being performed: is this a back-door adjustment, a mediator that is being improperly conditioned on, a collider that is being improperly conditioned on? The diagram tells you which.

**"Causal effect" unqualified.** This is a frequent offender. When a paper reports "the causal effect of X on Y," ask: which causal effect? The average treatment effect in the full population? The average treatment effect on the treated? The local average treatment effect? A direct effect? An indirect effect? Different causal effects are different quantities, and they can be quite different numerically. A paper that does not specify which causal effect it is estimating is being imprecise in a way that matters.

**"Randomized."** Used loosely, this can mean anything from a true randomized controlled trial to "haphazardly assigned." A study that describes its treatment as "randomly assigned" should be checked: was there an actual randomization procedure? Were the randomized individuals the same as the analyzed individuals? If the randomization had selection, attrition, or non-compliance, the analysis may not have the properties a pure RCT would.

**"Confounder."** This means different things in different disciplines. In classical epidemiology, a confounder is a variable associated with both the exposure and the outcome. In the graphical framework, a confounder is a common cause of treatment and outcome — specifically, something that opens a back-door path. In econometrics, the term is less used; the corresponding concept is "omitted variable bias" from a specific variable.

These definitions are not equivalent. The classical epidemiological definition can mislabel mediators and colliders as confounders. The graphical definition is more precise. When reading, pay attention to which notion of confounding is being invoked.

**"Natural experiment."** A natural experiment is variation in a treatment that arises from circumstances outside the researcher's control and approximates randomization. Real natural experiments — policy changes with clear exogeneity, geographic discontinuities, genetic variants — can be powerful. But the term has been stretched to cover all sorts of variation that is not actually random. A paper that claims a natural experiment should be scrutinized: is the variation really as-if-random, or is the author hoping you won't notice the selection?

**"Robust to."** When a paper says results are "robust to" various checks, look at which checks were actually performed. Robustness to alternative specifications of the regression is one thing. Robustness to major changes in the causal model is another. The phrase "robust to" is often used to describe narrow robustness checks while implying broad robustness.

**"Causal machine learning."** This is an active area of research that applies machine learning methods to problems in causal inference. Double machine learning, causal forests, and related methods use ML to estimate nuisance parameters (like propensity scores or outcome regressions) in a causal analysis. Under appropriate assumptions, these methods produce valid statistical inference on causal parameters even when the underlying ML models are complex.

Understood properly, "causal machine learning" is a useful family of methods. Understood as marketing, it often suggests more than it delivers.

## Causal AI: the buzzword problem

The most prominent recent example of terminology run amok is "Causal AI." The term sounds like it describes artificial intelligence that reasons about cause and effect — systems that look at data and figure out what causes what. That would be genuinely revolutionary. It would mean AI that had overcome the limitations of purely correlational pattern-recognition.

It is not what "Causal AI" actually does.

Here is what Causal AI products and methods actually do, stated honestly: they use machine learning to estimate the statistical adjustments required by human-specified causal models. The human provides the causal question, the causal diagram, the identification strategy, and every causal claim. The machine learning provides flexible, accurate estimation of the nuisance parameters — typically the propensity score and the outcome regression — that go into the adjustment.

This is a useful capability. It is not a new capability. It is machine-learning-enabled implementation of ideas that causal inference researchers have been developing for decades. The Chernozhukov-Chetverikov-Demirer-Duflo-Hansen-Newey-Robins framework for double machine learning, introduced in 2016, is the main technical backbone. It allows valid statistical inference on a causal parameter of interest even when the nuisance parameters are estimated by complex ML methods. This is real progress in methodology. It is not AI reasoning about causation.

The division of labor in a "Causal AI" analysis is:

**What the human provides:**
- The causal question ("what is the effect of X on Y in population P?")
- The causal diagram (which variables affect which others, through what paths)
- The identification strategy (the argument for why, conditional on the chosen controls, the treatment is effectively random)
- The interpretation of the results (what the estimate means in context)

**What the machine learning provides:**
- Flexible estimation of E[Y|X] and E[T|X] (the nuisance parameters)
- Valid statistical inference on the causal parameter, via techniques like cross-fitting and Neyman orthogonality

Every causal claim in this framework comes from the human. The machine does not detect whether X causes Y. It does not verify the causal diagram. It does not check whether the identification assumptions hold. These tasks remain with the analyst, where they have always been.

Why does this matter? Because calling the framework "Causal AI" invites decision-makers to believe they have bought a system that discovers causation from data. They have not. They have bought a more flexible estimator for the adjustments required by a causal analysis that still depends on human judgment and domain knowledge.

A firm that uses a "Causal AI" system without understanding that the identification assumptions are entirely human-supplied is not doing causal inference. It is doing prediction with extra steps and false confidence.

The more honest name for what these tools do is *ML-assisted causal adjustment*. Machine learning, applied to the statistical adjustment problem defined by a human's causal model. Less exciting. More accurate.

This is not a critique of the underlying methodology. Double machine learning and related techniques are genuine contributions. They handle high-dimensional control variables better than older parametric methods. They provide valid inference under weaker conditions. They are tools worth having.

It is a critique of the marketing. Causal AI is a term that obscures what causal inference requires. Readers should recognize that when a product or paper invokes "Causal AI," the identification strategy is still human work, and the quality of the analysis depends on the quality of that human work.

## Other terminological games

Causal AI is the most prominent recent example, but similar games are played with other terms.

**"Explainable AI."** Often used to describe methods that provide post-hoc explanations of machine learning predictions. These explanations are usually about what features the model attends to, not about causal relationships in the world. A method that explains that "the model's prediction relied heavily on feature X" does not tell you that X causes the outcome; it tells you what the model, which was trained on correlational data, learned to use. Causal explanation and statistical explanation are different things.

**"Evidence-based."** Used widely in policy and medicine to describe practices supported by empirical research. The term is useful when the evidence is well-defined and causal. It becomes slippery when "evidence" includes observational studies with serious limitations, when "evidence-based" is used to claim causal support from correlational findings, or when the evidence base is itself contested.

**"Data-driven."** Similar to "evidence-based" in connotation. "Data-driven" decisions sound objective, but the data cannot tell you what to do without a model of the consequences of different actions. Every data-driven decision includes causal assumptions about how actions produce outcomes, whether or not those assumptions are made explicit.

**"Rigorous."** Often used as a marker of methodological quality, but the term is doing no work — every paper claims rigor. What matters is which specific elements of the analysis are rigorous: the causal model, the identification strategy, the estimation, the sensitivity analyses. "Rigorous" without specifics is usually applause for oneself.

Reading critically means translating terminology into specific operations. When a paper says it "rigorously controls for confounders," ask: what confounders? Identified how? Controlled how? When a paper says it uses "state-of-the-art methods," ask: which methods, and do they match the question? The language of rigor and sophistication often obscures how much is actually being assumed.

## An interdisciplinary Babel

One final source of confusion deserves mention: the same causal concept often has different names in different disciplines.

What an economist calls *endogeneity*, an epidemiologist calls *confounding*, a statistician calls *selection bias* or *omitted variable bias*, and a computer scientist might call *spurious correlation*. These terms are not exactly synonymous — they have different shades of meaning in their native disciplines — but they often point at substantially the same underlying problem: an open back-door path from treatment to outcome that biases the observed association.

What an economist calls *instrumental variables*, a statistician calls *instrumental variable methods*, and an epidemiologist might call *Mendelian randomization* when the instrument is a gene. These are different names for the same core method, adapted to the conventions and applications of different fields.

What Pearl calls the *do-operator*, Rubin calls the *potential outcome under intervention*. What Pearl calls a *causal diagram*, Rubin calls a *potential outcomes model*. The Pearl and Rubin frameworks are mathematically equivalent in many settings but use different notations, and moving between them requires translation.

When you read across disciplines, you need to translate. An epidemiology paper that talks about confounding and adjustment is talking about the same thing as an economics paper that talks about endogeneity and instrumental variables. The causal problems are the same. The methods are often the same under different names. The vocabulary is different because the disciplines developed in different communities with different historical references.

A mature reader of causal inference has learned to see through the vocabulary and recognize the underlying operations. Is this paper using back-door adjustment or instrumental variables? Is this method estimating an average treatment effect or a local average treatment effect? Is this variable functioning as a confounder, a mediator, or a collider in the author's implicit model? These are the questions that matter, and they can usually be answered regardless of which discipline's dialect the paper is written in.

## A template for reading the cases in this book

With all of that in mind, here is a short template for reading each of the case studies that follow. Work through these questions for each case, and you will get substantially more out of them than a passive read.

1. **What is the causal question?** Write it in one sentence. What is the treatment, what is the outcome, what is the target population?

2. **Draw the causal diagram.** If the student provided one, evaluate it. If not, draw one from the description. Identify the front-door and back-door paths between treatment and outcome.

3. **What is the identification strategy?** Which of the methods from earlier chapters is being applied? What assumptions does the method require?

4. **Are the assumptions defended?** Look for explicit discussion of the key assumptions. Plausibility of the causal diagram. Sufficiency of the adjustment set. Validity of the instrument. Ignorability of treatment assignment.

5. **Are the data appropriate?** Sample, variables, covariates, sample size. Would you have made different choices?

6. **Are the methods applied correctly?** Can you spot errors in the application? Common mistakes: conditioning on a collider, missing an important confounder, using a method inappropriate to the question.

7. **Are the results sensible?** Compare to domain knowledge. If the estimate is surprising, what explains the surprise?

8. **Are there sensitivity analyses?** If so, are they meaningful? If not, what's missing?

9. **Are the limitations honestly acknowledged?** Does the author engage with the places the analysis might fail?

10. **Are the conclusions calibrated?** Does the language of the conclusions match the strength of the evidence?

If a case study holds up under this scrutiny, it is a good piece of work. If it doesn't, the specific failures tell you something. Maybe the identification is weak but the substantive problem is interesting. Maybe the methods are rigorous but the question is narrow. Maybe the assumptions are heroic but the sensitivity analyses suggest the conclusions are robust anyway. The template gives you a structured way to assess strengths and weaknesses rather than accepting or rejecting the whole piece.

## The point of this book

Causal inference is not a set of formulas to memorize. It is a way of thinking.

The way of thinking starts with the recognition that correlation is not causation, and that the gap between them is not narrow. Statistical associations in data are the sum of many contributions — causal effects, confounding, selection, coincidence. Disentangling these requires assumptions about how the world works, assumptions that go beyond the data.

The way of thinking continues with the commitment to make those assumptions explicit. A causal claim without explicit assumptions is not a claim at all; it is a plausibility assertion. An explicit causal model — drawn as a diagram, written as equations, or stated in careful text — is the foundation of rigorous causal analysis.

The way of thinking proceeds to the methods that connect assumptions to evidence: back-door adjustment, matching, weighting, instrumental variables, counterfactual analysis. Each method is a formal tool for extracting specific kinds of causal information from data, under specific assumptions. Each has strengths and failure modes that a skilled analyst knows to watch for.

The way of thinking ends with intellectual honesty about what has been achieved. Good causal analysis is careful about what it claims. It acknowledges assumptions. It reports sensitivity analyses. It distinguishes qualitative conclusions ("the evidence suggests X matters") from quantitative precision ("X increases Y by 7.3%"). It resists the temptation to oversell.

The student case studies that follow this chapter are the practical culmination of the book. Each one is an attempt to apply this way of thinking to a specific problem. None of them is perfect. All of them are attempts. The best of them will be rigorous, honest, and illuminating. The weaker ones will reveal, in their weaknesses, the demands of rigorous causal thinking.

Read the cases carefully. Ask the questions from the template. Draw the diagrams. Notice where the authors succeed and where they fall short. In doing so, you will be doing the final, most important kind of learning: the active work of evaluating causal claims in the wild. Causal inference is ultimately a literacy. This book has been an attempt to teach it. The rest is practice.

## A final note

The field of causal inference has come a long way in thirty years. Methods that were fringe research in the 1990s — causal diagrams, propensity score methods, rigorous treatment of counterfactuals — are now standard in epidemiology, policy analysis, and much of applied economics. The methodological foundations are mature. Software implementations are available. Textbooks and courses are plentiful.

What remains underdeveloped is the practice. Too many applied papers still treat causal inference as a set of routines to be executed, rather than a discipline of thought to be applied. Too many still hide their assumptions, skip their sensitivity analyses, and use language that claims more than the evidence supports. The methods are better than the applications.

The response is not more methods. The response is more careful application. This includes case studies like the ones in this book — works of applied causal analysis that try to do it right. It includes readers like you — readers who have been through the theory, who understand the methods and their limitations, and who can evaluate causal claims with the skepticism they deserve.

There is no substitute for thinking carefully. No statistical method, no machine-learning framework, no data set, however large, can replace the work of thinking through what a causal claim means and what evidence would support it. The tools in this book make that thinking easier and more systematic, but they do not replace it. They are aids to a discipline of reasoning that remains fundamentally human.

The case studies are next. Read them with that discipline in mind.

---

## A note about AI

Reading a case study is the meta-skill the chapter teaches. The model can produce a confident summary of any case study on request. The summary is not the reading.

Where the model genuinely helps: producing the structural questions to apply to a case — what is the estimand, what is the identification strategy, what assumptions are required, where is the strongest objection.

Where the model does damage: producing the verdict on whether the case study's claims are credible. Credibility depends on the analyst's interrogation of the assumptions, which is the work the chapter teaches.

The rule: structural questions from the model; the verdict from the working reader.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Miguel Hernán** has spent his career making causal inference accessible to applied researchers — co-authoring (with James Robins) the free textbook *Causal Inference: What If* that has become the standard introduction. His framework for reading observational studies is a checklist against fooling yourself.

**Run this:**

```
Who is Miguel Hernán, and how does his work on causal inference for working researchers connect to the case-study reading skills we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Miguel Hernán"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Hernán's target-trial emulation framework to one specific observational study.
- Ask it to walk through the principal common errors Hernán names in his teaching.

What changes? What gets better? What gets worse?
