# The Full Analysis: One Problem, Every Decision


## TL;DR

- TL;DR: A complete causal analysis is eleven components, every one defended, every limit named, the conclusion labeled in one of three honest registers — definitive, suggestive, or inconclusive.
- The chapter moves through Opening — What "done" looks like, Concept one — The eleven-component analysis plan, Mid-chapter checkpoint, Concept two — The peer-review protocol, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

**Suggested titles:**
1. The Full Analysis: One Problem, Every Decision
2. The Eleven-Component Deliverable: A Causal Analysis You Can Defend
3. What "Done" Looks Like: The Final Project as the Whole Course Compressed

**TL;DR:** A complete causal analysis is eleven components, every one defended, every limit named, the conclusion labeled in one of three honest registers — *definitive*, *suggestive*, or *inconclusive*. This chapter shows the target, hands you the rubric, and hands you the course back at the end.

**Byline:** Nik Bear Brown

**Prerequisites:**
- The full course (Chapters 1–14). The chapter integrates rather than introduces.
- A working draft of your own-domain analysis from Chapters 12–14 — specification (Ch. 12), output and diagnostic (Ch. 13), sensitivity and qualified conclusion (Ch. 14).
- Familiarity with the three-question diagnostic from Chapter 13 and the E-value from Chapter 14.

**Learning objectives:**
- **Create:** Produce a complete causal-analysis plan in eleven components, integrated end-to-end, defensible against a skeptical reader.
- **Evaluate:** Apply the three-question diagnostic to a peer's analysis plan and write a one-page review that names the specific revision each failed check requires.
- **Create:** Defend the analysis, in writing and in presentation, against the question *why this label and not the next one*.

---

## 1. Opening — What "done" looks like

Before any student in this course writes a single component of their final project, I am going to show them what the finished thing looks like. The pedagogical reason is the apprenticeship literature: students who cannot envision the deliverable cannot produce it. The deeper reason is that this chapter is the test of whether the previous fourteen weeks taught what they claimed to teach, and the only way to administer the test fairly is to show the target before scoring against it.

Here, then, is the target. Five pages, plus appendices. The format is fixed; the substance is yours. I will use a composite case for the example — the pricing-A/B-testing case that has run through Act Three since Chapter 12 — and I will flag where the substance is illustrative versus prescriptive. The eleven components are prescriptive. The values inside them are illustrative.

> **TITLE.** Causal Effect of Dynamic-Pricing Algorithm v2 on Weekly Category Revenue, Pricing-Experiment Cohort, Q3 2025.
>
> **EXECUTIVE SUMMARY (150 words).** We estimated the average treatment effect of deploying Dynamic-Pricing Algorithm v2 on weekly category revenue, using a four-month observational comparison between treated categories (n = 47) and matched control categories (n = 51). The point estimate is +2.1% with a 95% confidence interval of [+0.3%, +3.9%]. The three-question diagnostic passes Q1 (spec correct) and Q3 (refutation tests stable); Q2 (data supports spec) passes with a noted overlap concern at the high-margin tail. The E-value at the lower CI bound is 1.21. Plausible unmeasured confounding from concurrent merchandising changes is calibrated at 1.15–1.30 in this domain. **Label: suggestive but not definitive.** Recommended next step: a category-level randomized rollout on a fresh cohort to convert this to a definitive estimate. Confidence to expand the program absent that experiment: low.
>
> **§1 The question.** *Estimand.* The average treatment effect, in weekly revenue percentage points, of deploying DPA v2 instead of DPA v1 on a category, averaged over the population of categories carrying ≥$50K weekly revenue at baseline. *Not* "is there a relationship between algorithm version and revenue." A specific number, attached to a specific intervention, on a specific population.
>
> **§2 The setting and the data.** Q3 2025 observational data from the Pricing Decision Platform. 98 categories total; 47 treated, 51 control. Sixteen weeks. Weekly aggregates of revenue, units, price points, promotional intensity, competitor scrape, and inventory state. *Not measured:* merchandising team's category-by-category attention allocation; cross-category cannibalization at the SKU level.
>
> **§3 The DAG.** *(Figure: 11 nodes, defended in §4.)*
>
> **§4 The DAG defense.** Each of seventeen arrows annotated with the literature or domain reasoning that supports it. Three assumed-absent arrows justified explicitly. The defense survives the methodological-reviewer pass.
>
> **§5 The identification argument.** Backdoor criterion satisfied by adjustment set {baseline revenue, competitor price index, season-week, inventory state}. No mediators or colliders included. The do-not-add list is appendix B.
>
> **§6 The estimation specification.** Doubly robust ATE estimator (DoWhy `causal_estimator="backdoor.linear_regression"` with `causal_estimator="backdoor.propensity_score_weighting"` as the cross-check). Sample inclusion: category-weeks with ≥1,000 sessions. Outcome: log-revenue. Treatment: binary deployment indicator.
>
> **§7 The estimation output with diagnostic.** Point estimate +2.1%; 95% CI [+0.3%, +3.9%]; refutation tests (random common cause, placebo treatment, subset robustness) stable within ±0.4%; overlap diagnostic shows a thin region at the high-margin tail (handled by trimming, with sensitivity reported).
>
> **§8 The sensitivity analysis.** E-value at point estimate 1.36; E-value at lower CI bound 1.21. Domain calibration: plausible concurrent merchandising attention shifts produce effects of magnitude 1.15–1.30 in similar past analyses (citing two internal post-hoc reviews).
>
> **§9 The qualified conclusion in two registers.**
> *Technical:* Under the assumed DAG and the stated adjustment set, the ATE of DPA v2 on weekly category revenue is +2.1% [95% CI +0.3%, +3.9%]; the lower-bound E-value of 1.21 is comparable to plausible unmeasured confounding from concurrent merchandising shifts, so the identification assumptions are non-trivially uncertain.
> *Plain-language:* The data is consistent with a small positive revenue effect, but we cannot rule out that the effect we are seeing is partly the merchandising team paying more attention to the new-algorithm categories. Treat this as motivation to run a clean randomized rollout, not as evidence to expand the program firm-wide.
>
> **§10 The limits and what would relax them.** Category-level randomization on a fresh cohort (estimated cost: $X; timeline: 8 weeks) would convert "suggestive" to "definitive" by breaking the merchandising-attention confound at the design level. A merchandising-attention log, if instituted, would convert the confound from unmeasured to measured.
>
> **§11 The AI Use Disclosure (final-project version).** Three identification decisions across the full 15-week analysis that required domain expertise no AI tool could supply: (1) the choice to include the merchandising-attention arrow in the DAG despite its being unmeasured; (2) the calibration of plausible confounder strength at 1.15–1.30 against internal post-hoc reviews; (3) the decision to label the result "suggestive" rather than "definitive" given a small but non-zero CI that includes effects of decision-relevant magnitude. Each is specified in detail in appendix D.
>
> **APPENDICES.** A: DAG figure with full arrow annotations. B: Do-not-add list. C: Refutation-test outputs. D: AI Use Disclosure long form. E: Reproducible code (notebook).

That is the deliverable. Five pages of content, no padding, no boilerplate. Read it twice. The shape matters more than any single value inside it.

The student who can produce that document, defend it for thirty minutes against a skeptical reviewer, and assign the label honestly — that student has demonstrated, in one artifact, what the previous fourteen weeks were for. Everything else in this chapter is the rubric, the protocol, and the meta-move. The artifact is the proof.

---

## 2. Concept one — The eleven-component analysis plan

Let me walk through each component, because the integration is the work and the document is the proof of the work. I will say what each section is, where it inherits from in the course, and what students get wrong about it.

**§1 The question.** Stated as a causal estimand. The discipline here is the one Miguel Hernán has been arguing for since the 2018 *AJPH* editorial ["The C-Word: Scientific Euphemisms Do Not Improve Causal Inference From Observational Data"](https://ajph.aphapublications.org/doi/full/10.2105/AJPH.2018.304337) (DOI: 10.2105/AJPH.2018.304337). The student names the target — *what specific causal quantity, on what population, under what intervention* — before any analysis touches it. The estimand could be ATE (average over the whole population), ATT (average among the treated), or CATE (a conditional version on a sub-population). The choice is a domain choice and gets defended here. The failure mode: vague targets like "the impact of the program," which permit the analysis to drift toward whatever number comes out cleanest. The discipline: a specific number, on a specific population, under a specific intervention, named *first*. This is Chapters 1–3 made operational.

**§2 The setting and the data.** What population. What time period. What unit of observation. What data sources. *What was measured and what was not.* The "what was not" is the honest core of this section. The DAG in §3 will contain unmeasured variables; this section is where the analyst commits, on paper, to *which* variables those are. The failure mode: leaving "what was not measured" as a gesture rather than an enumeration. The discipline: a list. This is Chapter 2 made operational.

**§3 The DAG.** A figure. Every relevant variable as a node, every defended arrow drawn, every assumed-absent arrow either drawn-and-justified or named in §4 and explained. This is the artifact that makes the identification argument auditable, and it is the artifact that the methodological reviewer will read first. The failure mode: a sparse, presentable DAG that omits the variables the analyst could not measure. The discipline: include the unmeasured variables on the graph. They are the variables a skeptical reader will ask about; better to show them now than to be ambushed later. This is Chapter 4 made operational.

**§4 The DAG defense.** Each arrow named, the evidence for it cited, the assumed-absent arrows justified. Domain literature, prior internal analyses, mechanistic reasoning — whatever the basis is, the basis is on the page. The failure mode: "this DAG is based on domain knowledge" as the entire defense. The discipline: one paragraph per non-obvious arrow; one paragraph per non-obvious assumed-absent arrow. This is Chapter 11's artifact, integrated.

**§5 The identification argument.** Which backdoor paths exist. Which adjustment set blocks them. *Why this set and not another* — minimal adjustment, efficient adjustment, or domain-preferred. The named identification assumptions: no unmeasured confounding given the adjustment set; positivity; consistency; SUTVA. This is Chapters 5–10 made operational — the toolkit that took six weeks to build, now compressed into one section.

**§6 The estimation specification.** The spec doc from Chapter 12. Estimator named. Software named with version. Parameters listed. Adjustment-set membership matched to §5. Functional form chosen. Treatment-effect definition (ATE / ATT / CATE) chosen and matched to §1. The do-not-add list as an artifact, separately. The failure mode: producing a spec that does not match §5 in adjustment-set membership, because the analyst added a few "useful-looking" controls during estimation. The discipline: the spec is a contract with the version of the analysis the student committed to in §1–§5. This is Chapter 12 made operational.

**§7 The estimation result with diagnostic.** Point estimate. Confidence interval. Refutation-test outputs from the DoWhy- or EconML-style robustness suite. Overlap diagnostic. The three-question diagnostic from Chapter 13 applied — Q1 (is the spec correct), Q2 (does the data support the spec), Q3 (do the refutation checks pass). Pass or fail for each, with reasoning. The failure mode: reporting the point estimate cleanly and burying the diagnostic in an appendix. The discipline: the diagnostic is on the main page, next to the estimate. This is Chapter 13 made operational.

**§8 The sensitivity analysis.** E-value at the point estimate. E-value at the relevant CI bound. *Domain calibration:* a defended statement about how strong plausible unmeasured confounders are in this domain. The calibration is the irreducibly-human part. The E-value is a number; the question whether 1.21 is large or small in this setting is a domain judgment. This is Chapter 14 made operational.

**§9 The qualified conclusion in two registers.** Technical and plain-language, both. Technical: a sentence the methodological reviewer can audit. Plain-language: a sentence the decision-maker can act on, with the limits embedded in the sentence itself rather than buried in a footnote. The two registers point at the same conclusion; they speak to two readers. This is Chapter 14 made operational.

**§10 The limits and what would relax them.** What the analysis cannot say. What data collection or experimental design would convert "not definitive" into "definitive." This section is what makes the analysis useful as a *next step*, not just as a report. The failure mode: listing limits without naming the work that would address them. The discipline: every limit paired with the specific intervention that would remove it.

**§11 The AI Use Disclosure (final-project version).** Three identification decisions across the full 15-week analysis where domain expertise was required that no AI tool could supply. This is the higher-bar form. Concrete to your domain. Specific to your analysis. I will say more about this in Concept five.

The integration is the work. Each section cites the section above it. §5 cites §4. §7 cites §6. §8 cites §5. §9 cites everything. A student who writes eleven self-contained documents and staples them together has produced eleven self-contained documents and stapled them together. A student who writes one document with eleven sections has produced an analysis.

I should flag something before moving on. The eleven-component structure as a graded artifact is original to this book — the components individually trace to Hernán 2019 ([*A Second Chance to Get Causal Inference Right*](https://doi.org/10.1080/09332480.2019.1579578)), Pearl 2018 ([*Theoretical Impediments to Machine Learning*](https://arxiv.org/abs/1801.04016)), [Hernán & Robins 2020](https://miguelhernan.org/whatifbook), and prior chapters of this book. The integration as a unit, and the requirement that the eleven sections cite each other, is the contribution this book makes. Other instructors may use eight, or thirteen, or some other count. The number is not sacred. The integration is.

---

## 3. Mid-chapter checkpoint

Stop. Before reading further, look at the deliverable in §1 and the eleven components in §2. Can you say, for your own domain analysis, which of the eleven sections you have a draft of and which you do not? If the answer is "I have drafts of one to four sections," you are roughly where most students are at this point in the course. If the answer is "I have drafts of seven to ten sections," you are ahead. If the answer is "I do not yet know what my §1 estimand is," go back to Chapter 12 and write it before you read on. The chapter from here forward assumes you have at least a working estimand. The rest of the components have a place to land only if §1 is in place.

---

## 4. Concept two — The peer-review protocol

Before the final presentation, you will review one peer's analysis plan, and one peer will review yours. The review is not opinion. It is the three-question diagnostic from Chapter 13, applied to your peer's deliverable, written as structured feedback.

I want to walk through the protocol concretely, because students who treat peer review as a courtesy produce courtesy-quality reviews, and courtesy-quality reviews are useless.

**The structure** adapts Emily Wray's [RISE feedback model](https://www.risemodel.com/) — Reflect, Inquire, Suggest, Elevate — which was developed for educational peer feedback and has been adopted across writing-instruction, design-critique, and engineering-review settings. The RISE model's logic is: feedback that starts with reflection (what did you understand the work to be?) is harder to dismiss than feedback that starts with critique; feedback that ends with elevation (what is this work doing well?) is more likely to be acted on than feedback that ends with criticism. The book's adaptation substitutes the three-question diagnostic for RISE's general inquiry move, because the three-question diagnostic is what the chapter has been teaching as the analytical-review instrument.

The adapted protocol has six moves. The peer carries out each in order.

**Reflect.** State, in your own words, the peer's causal question and identification strategy. Two paragraphs maximum. If you cannot — if reading the analysis plan does not leave you able to summarize the estimand and the adjustment strategy — the writeup needs revision before review can proceed. This is the diagnostic's precondition: clarity of communication is identification work. An analysis that cannot be summarized has not yet been written.

**Inquire — Question 1 (Is the specification correct?).** Where is the treatment definition? Is it stable across the analysis window? Where is the outcome definition? Is the adjustment set in §6 the same as the one claimed in §5? Is the do-not-add list respected by the estimator (no mediators or colliders sneaking back in)? Are the named identification assumptions consistent with the DAG? Pass / fail with one-sentence reasoning for each.

**Inquire — Question 2 (Does the data support the specification?).** Overlap diagnostic present? Sample-selection criteria compatible with the §1 estimand? Missing-data assumptions stated? If there are weights, are they stable? Pass / fail with reasoning.

**Inquire — Question 3 (Do the refutation checks pass?).** Refutation tests reported? Sensitivity analysis present? E-value reported with domain calibration? Pass / fail with reasoning.

**Suggest.** For each failed check, name the specific revision that would address it. Not "redo the analysis." Specific. "The overlap diagnostic in §7 shows a thin region at the high-margin tail; either trim and report the trimming, or restrict the §1 estimand to exclude high-margin categories and note the restriction in §10."

**Elevate.** Name what the analysis does well. Specifically, where the analyst's domain knowledge is doing identification work that no tool could supply. Concrete examples from the peer's draft. This is not flattery. It is the peer learning to recognize good identification work when they see it — which is itself a course objective.

**Timing.** The protocol runs one week before final presentations. Drafts circulate Monday; peer reviews due Thursday; author responses due Saturday; presentations on Monday. The author's response is written, addresses each diagnostic verdict, and is submitted with the final deliverable. The peer reviewer asks the first question after the presentation. (Ten minutes presentation; ten minutes Q&A; the peer reviewer's first question is the question that came out of their review.)

**Grading.** The peer review is itself a graded artifact, worth 40 points within the final-project allocation. The student is responsible for the quality of their critique as much as for the quality of their own analysis. This serves the book's thesis: identification skill is exercised both in producing analyses and in critically reading them. A perfunctory review costs the reviewer real points. A careful review, even one that finds nothing major to revise, earns full credit if its diagnostic application is rigorous and its elevation is concrete.

A common misconception lives here. Students arriving from coursework where peer review means "find typos and say something nice" will treat this protocol the same way. The protocol resists that treatment by making each Inquire step a specific question with a pass/fail verdict. There is no place to deposit politeness; there are places to deposit observations and conclusions. If the conclusion is "passes all three questions," that is itself a real conclusion that the author can use.

---

## 5. Concept three — The definitive / suggestive / inconclusive register

Here is the chapter's hardest conceptual move, and one I want to flag honestly: the three-label register I am about to teach is original to this book. The standard causal-inference literature does not formalize "definitive / suggestive / inconclusive" as a labeling discipline. Hernán's 2018 *AJPH* editorial argues for explicitly calling causal questions causal, but does not provide a tiered labeling vocabulary for the strength of the resulting claim. Tyler VanderWeele and Maya Mathur have argued, in the [2019 *American Journal of Epidemiology* paper on Bonferroni correction](https://academic.oup.com/aje/article/188/3/617/5193218), that the strength of the conclusion language should be calibrated to the strength of the underlying evidence — but again, no tiered vocabulary. The three-label register is my proposal. It is grounded in the existing practice, but it is original here.

I propose it anyway, because the alternative is what students currently do — which is hedge ambiguously and let the reader guess how much weight to put on the result. The three labels force a commitment. The commitment can be challenged in the presentation. The challenge is the point.

The criteria. An analysis is **definitive within scope** when *all three* of the following hold:

1. The estimand is well-specified and the identification assumptions are defended.
2. The three-question diagnostic passes all three questions.
3. The E-value at the relevant CI bound substantially exceeds plausible domain confounding (rule of thumb: by a factor of 2 or more, with the domain calibration defended).

"Within scope" matters. A definitive estimate on the population of categories carrying ≥$50K in weekly revenue is not a definitive estimate on the population of all categories. Generalization beyond the analyzed population is its own claim, requiring its own argument. (Beth Tipton's work on generalizability — see [Tipton & Olsen 2018](https://doi.org/10.3102/0162373717748966) `[verify]` and the broader literature on external validity — makes the case for treating the population specification as a first-class object of the analysis. I name this here without going deeper; the engineering reader should be aware that "for whom is this effect estimated" is a question separate from "is this effect identified.")

An analysis is **suggestive but not definitive** when the estimand is well-specified *and* the identification assumptions are defended, but one or more of the following holds:

1. The three-question diagnostic passes Q1 and Q3 but Q2 shows a non-trivial concern (overlap thin in a region, missingness non-ignorable in a sub-population).
2. The E-value at the CI bound is comparable to — within a factor of 2 of — plausible domain confounding.
3. The point estimate's sign is stable across refutation tests but the magnitude moves enough that the decision-relevant comparison (e.g., "effect larger than X is needed to justify expansion") sits on the boundary.

The decision-maker reading a suggestive label should treat the estimate as motivation for action under monitoring, with a confirmatory study planned. *Suggestive* does not mean "don't believe it." It means "act on it, but treat the action as also being the next experiment." This is the register most engineering analyses live in. Most observational analyses, honestly, should be labeled suggestive. The student who learns to write suggestive without flinching has learned something the field is still learning.

An analysis is **inconclusive** when at least one of the following holds:

1. Identification cannot be defended without assumptions the analyst does not believe (i.e., a backdoor path remains open under the maintained DAG, and the variable that would close it is unmeasured).
2. The three-question diagnostic fails Q1 (the spec is wrong) or Q2 (the data does not support the spec).
3. The E-value at the CI bound is small relative to plausible domain confounding (within 20% of plausible confounder strength).

The honest report on an inconclusive analysis is that the analysis is *not* the evidence the decision-maker needs. A different design is required. The student who reports "inconclusive" with the specific next-step proposal in §10 has done the job; the student who reports "inconclusive" as a way to avoid committing has not.

The three labels are not standard. The book is proposing them. I want students to use them as a *discipline for honest commitment*, not as a slot-filling exercise. The presentation is where the discipline is tested: the instructor presses the assigned label ("why suggestive and not definitive? what would convert it?"), and the student either defends the label with the criteria, or the label revises. That conversation is the pedagogical payoff of the chapter.

A common misconception, again. "If I report inconclusive or suggestive, I failed the project." The opposite. The student who reports honestly is doing the method. The student who claims definitive without earning it is failing the decision-maker and failing the chapter. I will repeat this once more in Concept four because it is the single most counter-cultural move the chapter asks for.

---

## 6. Concept four — What "definitive" means and when to claim it

Engineering culture rewards confident outputs. The pipeline that ships a number is the pipeline that gets resources. The analyst who reports "the new model improves CTR by 2.1%" gets a different reception than the analyst who reports "the new model is suggestively associated with a 2.1% CTR lift, with E-value 1.2 at the lower CI bound against plausible cohort-drift confounding of 1.3, label: suggestive but not definitive." The first analyst gets faster meetings. The second analyst occasionally annoys people.

The second analyst is doing the work the field needs done.

Here is the rubric, plainly stated. *Definitive* is a label you defend; it is not a property the data hands you. The three layers — identification, sensitivity, domain — must align before you claim it. When they align, claim it. The decision-maker, reading a definitive analysis, can act on the estimate as evidence within the scope of the analyzed population and conditions. They will act. The analyst has handed them something they can act on, and the analyst's name is on it.

This is heavier than it sounds. A definitive label is an underwriting move. You are signing your name to the claim that, given everything you know about the domain and given the analytical work that backs the claim, the decision-maker can use this number to decide. If you cannot live with that signature, the label is wrong. *Suggestive* is the right label when you can live with "the decision-maker should plan a confirmation experiment based on this" but not with "the decision-maker should commit firm-wide based on this."

Most analyses are suggestive. I will say it once more for the engineering reader who finds this counter-intuitive: most observational analyses, honestly assessed, should be labeled suggestive. The world is full of unmeasured confounders. The DAG you can defend is usually narrower than the DAG that would be needed to claim definitive identification. The E-value is usually smaller than plausible confounding by a factor that lands in the "comparable to" range. *Suggestive* is the modal honest answer. The student who can write *suggestive* without apology has internalized something the field is still teaching itself.

When can you claim definitive? Concretely, in engineering practice: when you ran a randomized experiment with full compliance and the question is the average effect on the experimental cohort. When you have an instrumental variable that the field accepts and the LATE is the quantity you wanted to estimate. When you have a regression-discontinuity design with a strong first stage and the question is the local average treatment effect at the cutoff. When you have a controlled-A/B-test setup with the treatment-control assignment uncorrupted by interference. In each of these, the identification machinery does the heavy lifting that the observational analysis cannot do, and the E-value calculation reflects a sensitivity question that has been pre-empted by the design. Definitive, then. Sign the name.

When can you almost-claim definitive on observational data? When the unmeasured confounders are all small, well-characterized, and dominated by the measured ones; when the E-value at the CI bound is several times plausible confounder strength; when refutation tests are stable across all reasonable specifications; and when the decision-maker can write down a smaller next-step than a full randomization. This is rare. When it happens, claim it. Most of the time, write *suggestive* and propose the next experiment.

I want to acknowledge where the three-label register may over-formalize. The labels are discrete. Real evidence is continuous. An E-value of 1.99 next to plausible confounding of 1.00 is "definitive" under the rule of thumb; an E-value of 1.95 next to plausible confounding of 1.00 is not. The boundary is artificial. The defense, however, is not artificial — the student is required to argue why their case is on one side of the boundary or the other, and the argument is what the chapter is grading. If two students disagree about whether the same case is definitive or suggestive, and both produce coherent arguments for their assignment, both have done the chapter. The label is the discipline. The argument is the work.

---

## 7. Concept five — The higher-bar final-project AI Use Disclosure

The standard AI Use Disclosure, introduced in Chapter 4 and used throughout the course, requires naming *one* identification decision that no AI tool could make. The final-project version requires naming *three* across the full 15-week analysis. This is the book's thesis operationalized as a course artifact. I do not think of it as a footnote. I think of it as the chapter's deliverable that is most likely to outlive the course.

Here is why. The course's claim is that identification decisions require domain judgment no causal AI tool currently supplies. That claim is testable. The test is: across a full causal analysis, can the analyst name three specific decisions where their domain expertise was load-bearing, in a way that an LLM-orchestrated workflow could not have supplied? If yes, the claim is supported in the analyst's case. If no — if the analyst cannot name three — either (a) the claim is wrong for this domain, or (b) the analyst has not yet learned to see their own contribution. Either finding is useful.

Candidates for what the three decisions might be, drawn from prior chapters' framing:

- **Selection of which variables enter the DAG (Chapters 4 / 11).** What counts as a relevant confounder is a domain question. An LLM can suggest standard confounder lists; it cannot know which variable in your data pipeline is *secretly* a downstream consequence of an upstream decision your team made last quarter. That kind of fact lives in the analyst's head and the team's institutional memory.
- **Defense of the no-unmeasured-confounding assumption (Chapters 5 / 11).** The analyst names the candidate unmeasured confounders and argues why they are not present, blocked, or substantially correlated with measured variables. The candidates come from domain knowledge. An LLM can prompt you to consider unmeasured confounders; it cannot tell you which specific unmeasured confounder, in your domain, is most likely to be load-bearing.
- **Calibration of the E-value against typical confounder strengths (Chapter 14).** "In this domain, plausible unmeasured confounders produce risk-ratio-equivalents of 1.15 to 1.30" is a domain claim. The 1.15-to-1.30 is not a fact the LLM has. It is a fact the analyst has, drawn from prior internal analyses or domain literature, and it is the fact that converts an E-value of 1.21 from "looks small" to "small relative to plausible confounding here."
- **Specification of what counts as "definitive" for the decision at stake (Chapter 15).** The threshold for action is a decision-maker's question, not a statistician's. If a 1% revenue lift justifies expansion in this business and a 5% lift would be required to justify staffing a permanent team, the boundary between "definitive enough" and "not definitive enough" sits at 1%, not at 5%, and not at whatever default a tool uses. That boundary is a decision-maker's, articulated to the analyst, and the analyst's role is to defend the label against it.

Your three are yours. They must be specific to your domain. The disclosure is graded on whether the three are *concrete*, not on whether they match a canonical list. A disclosure that says "I selected variables for the DAG, I defended the no-unmeasured-confounding assumption, and I calibrated the E-value" is generic and earns a low score. A disclosure that says "I included the merchandising-attention arrow because I know from 2024 Q2 post-hoc analysis that the merchandising team responded to algorithmic-pricing-category prioritization in week 3, even though that response is not logged anywhere; I excluded the 'high-value-customer' indicator from the adjustment set because I traced it to a downstream eligibility calculation; I calibrated plausible confounding at 1.20 because internal post-hoc reviews of two prior pricing-experiment retrospectives produced confounder strengths between 1.15 and 1.25" — that is the disclosure. Specific. Domain-anchored. Reproducible-in-spirit. The thesis the book has been advancing for 14 chapters, now exhibited as evidence in your own analysis.

The grading is harsh on generic disclosures, because the generic disclosure is the failure mode the chapter is trying to prevent. A student who treats the AI Use Disclosure as a checkbox has not internalized the book; a student who treats it as a learning artifact has.

---

## 8. Integration — The whole course in one chapter

You arrived in Week 1 not knowing the difference between a pattern and a causal claim. The argument is in front of you now.

Across **Act One (Weeks 1–4)**, you learned the language. The decision that looked right and was not (Chapter 1) — the question Pearl's three-rung ladder addresses (Chapter 2). The three representations of a causal claim — verbal, graphical, structural — and how to translate between them (Chapter 3). The identification layer as a layer of judgment that lives upstream of estimation (Chapter 4). You arrived without vocabulary for these distinctions. You leave able to name them.

Across **Act Two (Weeks 5–11)**, you built the toolkit. Confounders (Chapter 5). Mediators and why not to adjust for them (Chapter 6). Colliders, and the two consecutive weeks they cost (Chapters 7–8). The backdoor criterion in both directions — sufficiency and minimality (Chapters 9–10). The defense of a DAG to two audiences in two registers (Chapter 11). You arrived not having the toolkit. You leave with it.

Across **Act Three (Weeks 12–14)**, you learned the handoff. The specification document that tells a causal-AI tool what to do, literally (Chapter 12). The three-question diagnostic for reading the tool's output critically (Chapter 13). The sensitivity analysis and the qualified conclusion in two registers, for the cases where the assumptions do not hold (Chapter 14). You arrived not knowing how to hand off to a tool. You leave with the spec, the diagnostic, and the qualifier.

**Week 15 is the integration.** Not a fifteenth skill. The eleven-component deliverable is the previous fourteen weeks in one document. Producing it is the demonstration that you can use the toolkit; defending it is the demonstration that you can argue for the use; reviewing a peer's is the demonstration that you can read the use critically; labeling honestly is the demonstration that you can stop where the evidence stops; disclosing three identification decisions is the demonstration that you know what you, specifically, contributed.

If I were teaching a different course — one that ended at Chapter 11 — the closing chapter would be different. But the course is fifteen weeks and the closing is this: you have come a long way. The artifact that proves it is the one you submit on the last Monday of the term.

---

## 9. Worked example — The instructor's complete analysis, end to end

I will run the pricing-A/B-testing case through the eleven components in full, because the integration is what the chapter is teaching and an example is the only way to teach it.

The domain is the running case from Chapter 12 forward — a mid-sized e-commerce company evaluating Dynamic-Pricing Algorithm v2 (DPA v2) against v1, observational data on Q3 2025. (I am flagging here: the specific engineering domain for the running case across Weeks 12–15 is the instructor's choice. I am using pricing-A/B as the placeholder; an instructor running this course in a healthcare-deployment context, or a recommendation-system context, would substitute accordingly. The eleven-component structure does not change. The substance does. `[verify-domain-selection]`.)

**§1 The question.** Estimand: ATE of DPA v2 deployment versus continued DPA v1 operation on log(weekly category revenue), averaged over the population of product categories carrying ≥$50K in weekly revenue at baseline. *Not* the ATT (which would average only among treated categories) and *not* a CATE on a sub-population. The choice of ATE reflects the business question: should we expand DPA v2 to all qualifying categories, on average? The 1% threshold for expansion comes from a stakeholder conversation (Concept five candidate).

**§2 The setting and the data.** Q3 2025, 16 weeks. 98 categories (47 treated, 51 control) meeting the ≥$50K threshold. Data sources: Pricing Decision Platform (revenue, units, price points, deployment indicator), Marketing Data Mart (promotional intensity), External Scraper Service (competitor price index), Inventory System (state). Measured weekly. *Not measured:* merchandising team's category-by-category attention allocation; cross-category cannibalization at the SKU level; new-launch versus mature-category status when not encoded in the inventory state.

**§3 The DAG.** Eleven nodes. Treatment (T) = DPA v2 deployment indicator. Outcome (Y) = log(weekly category revenue). Measured: baseline revenue (Z1), competitor price index (Z2), season-week (Z3), inventory state (Z4), promotional intensity (M, mediator on T → M → Y). Unmeasured: merchandising attention (U1), cross-category cannibalization (U2), new-launch status (U3). Arrows defended in §4. *(Figure not rendered here; in the actual deliverable it is appendix A.)*

**§4 The DAG defense.** Selected highlights. The arrow Z1 → T (baseline revenue affects deployment) comes from the platform's deployment-prioritization logic, which selects higher-baseline-revenue categories first. The arrow U1 → T (merchandising attention affects deployment) is the load-bearing unmeasured-confounder claim: the merchandising team learns about which categories the pricing platform is prioritizing for DPA v2 and shifts merchandising-meeting attention accordingly within 1–2 weeks of deployment. This is not documented anywhere in the system; it is the analyst's domain knowledge from the 2024 Q2 post-hoc analysis of a prior pricing-experiment retrospective. The arrow U1 → Y (merchandising attention affects revenue) is plausible on its face. The assumed-absent arrow from T to U1 (DPA v2 deployment does not influence merchandising attention in week zero) is the structural justification for treating U1 as a confounder rather than a mediator. Each is defended in one paragraph in the full document.

**§5 The identification argument.** Backdoor paths: T ← Z1 → Y; T ← Z2 → Y; T ← Z3 → Y; T ← Z4 → Y; T ← U1 → Y; T ← U2 → Y; T ← U3 → Y. The first four are blockable by conditioning on {Z1, Z2, Z3, Z4}. The last three are not blockable on observed variables. *Strictly speaking, the effect is not identifiable.* What the analysis is doing — and what §8 and §9 will qualify — is reporting a point estimate under the assumption that U1, U2, U3 are small relative to the measured confounders. The named identification assumptions: positivity (every category had positive probability of treatment given the adjustment set; checked in §7), consistency (DPA v2 is well-defined across deployments; checked against engineering changelog), SUTVA (no interference between treated and control categories; defended via the SKU-level cannibalization concern, which is U2).

**§6 The estimation specification.** DoWhy. Estimator: `backdoor.linear_regression` with `backdoor.propensity_score_weighting` as cross-check. Sample inclusion: category-weeks with ≥1,000 sessions (to handle the §2 ≥$50K threshold at the unit-of-observation level). Outcome: log-revenue. Treatment: binary deployment indicator. Adjustment set: {Z1, Z2, Z3, Z4}. Do-not-add list: {M (promotional intensity; mediator), customer-cohort-id (downstream of T through algorithmic personalization), and any field with "intensity" in its name unless verified as not a mediator}. The do-not-add list is the chapter-6/7 artifact, written down so the pipeline cannot accidentally adjust for it.

**§7 The estimation output with diagnostic.** Point estimate: ATE on log-revenue = 0.0208 (translates to +2.1% on revenue at the means). 95% CI: [0.003, 0.039], i.e., [+0.3%, +3.9%]. Refutation: random common cause stable (point shifts by 0.4% within 1,000-sim envelope); placebo treatment estimates a non-significant 0.1% effect; subset robustness (50% random hold-out, repeated 100 times) stable within the CI. Overlap diagnostic: propensity scores between 0.05 and 0.95 for 92% of units; the remaining 8% sit in a high-margin tail that gets trimmed, with the trimmed estimate reported alongside. Three-question diagnostic: Q1 (spec correct) — passes; Q2 (data supports spec) — passes with overlap noted; Q3 (refutation passes) — passes.

**§8 The sensitivity analysis.** E-value at point estimate: 1.36. E-value at lower CI bound: 1.21. Domain calibration: in two prior pricing-experiment retrospectives (2024 Q2, 2024 Q4 — internal post-hoc reviews), the implied confounder strength from merchandising-attention shifts was between 1.15 and 1.30. The E-value of 1.21 is *comparable to* plausible domain confounding, not several times larger. This is the load-bearing observation.

**§9 The qualified conclusion in two registers.**
*Technical:* Under the assumed DAG and the adjustment set {Z1, Z2, Z3, Z4}, the ATE of DPA v2 deployment on log(weekly category revenue) is 0.0208 (95% CI [0.003, 0.039]), corresponding to +2.1% on revenue [+0.3%, +3.9%]. The lower-bound E-value of 1.21 is comparable to plausible unmeasured confounding from concurrent merchandising-attention shifts (calibrated at 1.15–1.30 in similar past analyses), so the no-unmeasured-confounding assumption is non-trivially uncertain. **Label: suggestive but not definitive.**
*Plain-language:* DPA v2 is associated with a small revenue lift over DPA v1 — somewhere between zero and four percent, with most of the evidence pointing at around two percent. But we cannot rule out that part of what we are seeing is the merchandising team paying more attention to the new-algorithm categories during the experiment. The honest call is to treat this as motivation to run a clean randomized rollout, not as evidence to expand the program firm-wide.

**§10 The limits and what would relax them.** Category-level randomization on a fresh cohort (estimated cost: $40K analyst-time + $20K platform-engineering-time + opportunity cost of 8 weeks delay; estimated power for a 1% effect at 80% power: N = 110 categories, achievable in the current platform): converts "suggestive" to "definitive" by breaking the merchandising-attention confound at the design level. Alternatively, a merchandising-attention log (estimated cost: $15K analyst-time + 4 weeks platform-engineering, plus a process change with the merchandising team): converts U1 from unmeasured to measured and allows inclusion in the adjustment set.

**§11 The AI Use Disclosure.** Three identification decisions across the full 15-week analysis where domain expertise was required that no AI tool could supply:

1. *The choice to include the merchandising-attention arrow (U1 → T, U1 → Y) in the DAG even though merchandising attention is unmeasured.* An LLM-orchestrated DAG-construction workflow would not have included this arrow, because no data field corresponds to it. The choice came from my reading of the 2024 Q2 retrospective, which documented (in a Slack channel, not the platform) that merchandising-meeting agendas in week 3 of the prior pricing experiment shifted toward the categories the pricing team had publicly named as DPA-v2-prioritized. Including the arrow is the load-bearing identification move; without it, the analysis would have reported a clean point estimate without the merchandising-attention caveat, and the §9 plain-language conclusion would have been wrong.

2. *The calibration of plausible confounder strength at 1.15–1.30 against internal post-hoc reviews.* The E-value of 1.21 is a number; the question whether 1.21 is large or small in this domain required reading the 2024 Q2 and Q4 retrospectives and comparing the magnitudes implied by the post-hoc reasoning. No general-purpose tool has access to those retrospectives, and even if it did, the inference from "the merchandising team shifted attention to the prioritized categories" to "this implies a confounder strength of approximately 1.15–1.30" requires domain familiarity with how merchandising attention translates into revenue effects in this business.

3. *The decision to label the result "suggestive" rather than "definitive" given the small but non-zero CI that includes effects of decision-relevant magnitude.* The 1% threshold for expansion is the stakeholder's, not the statistician's. The fact that the lower CI bound (0.3%) falls below the threshold while the point estimate (2.1%) sits above it means a substantial share of the posterior on the effect lives in the "should not expand" region. An AI tool would have reported the CI and the E-value as numbers; the decision to attach the *suggestive* label, rather than the *definitive* label, came from the stakeholder conversation about the 1% threshold and from my own judgment that handing the decision-maker an estimate whose lower bound sits below the threshold would be irresponsible without the experimental confirmation.

The disclosure ends here. Three decisions, each one specific to the domain, each one a place where a person's familiarity with the system did identification work the tools did not.

That is the worked example. Eleven sections. Five pages in the actual document. The label is *suggestive*. The recommended next step is a randomized rollout. The decision-maker can use the analysis to ask the right next question. The analyst has done the work.

The student's job in Part B of the final project is to produce the analogous document for their own domain. Same structure. Different substance. Same discipline.

---

## 10. Chapter summary — capabilities gained across the entire course

A complete causal analysis is eleven components, each one a section of a deliverable, each one citing the section above it. The analysis is integrated, not stapled together. The integration is the work; the deliverable is the proof.

The peer-review protocol applies the three-question diagnostic to a peer's analysis. The student is responsible for the quality of the critique as much as for the quality of their own analysis. The protocol adapts the RISE feedback model: Reflect, Inquire (in three diagnostic moves), Suggest, Elevate. Each move has a verdict; the verdicts feed a one-page review.

The qualified conclusion is labeled in one of three registers. *Definitive within scope* requires identification, sensitivity, and domain alignment. *Suggestive but not definitive* is the modal honest answer for observational analyses. *Inconclusive* is the honest answer when a different design is required. The three-label register is original to this book; the discipline of forcing a commitment to one label, and defending it under questioning, is the chapter's pedagogical move.

The AI Use Disclosure for the final project names three identification decisions across the full 15-week analysis where domain expertise was required that no AI tool could supply. The disclosure is graded on concreteness. A generic disclosure earns a low score; a domain-specific disclosure with three concrete examples earns full credit and demonstrates the book's thesis as an exhibit in the student's own work.

Across all fifteen weeks: the student arrived without language for causal claims, without the toolkit to identify them, and without the discipline to qualify them. They leave with all three. The artifact that proves it is the eleven-component analysis plan they submit on the last Monday of the term.

---

## 11. Closing reflection — handing the course to the reader

This is where I stop teaching. You have read fifteen weeks of material. You have built one analysis, end to end. You have a label on it that you can defend. You have named three places where your own judgment was the load-bearing element. You have, on the desk in front of you, a document that did not exist before this course.

On Monday morning you go back to work. The work has not changed. What you can do with it has.

The next time someone hands you an observational dataset and asks for "the causal effect," you will reach for the eleven-component structure before you reach for the estimator. You will draw the DAG before you write the regression. You will name the unmeasured confounders before someone asks. You will report the qualified conclusion in two registers because the decision-maker reads one register and the methodologist reads the other and you owe both of them an honest answer. You will sign your name to *definitive* only when the three layers align, and you will write *suggestive* without apology when they do not. You will know which identification decisions in your analysis your tools could have made, and which ones you, specifically, made.

That is not a small change. That is the change the book was trying to produce.

I have not solved the problem the book opens with — that identification decisions currently require domain judgment no causal AI tool supplies. The state of the field as of May 2026 still has tools that orchestrate the pipeline and analysts who supply the judgment. Whether that will hold in 2028, or 2030, I genuinely do not know. Some of the candidates for AI-assisted DAG construction are getting better. Some of the candidates for AI-assisted sensitivity analysis are getting better. The structural-judgment piece — the read of the domain — is the slowest to move, and I suspect it will be the last to move, but I do not believe in being certain about this. What I believe is that *for now*, the work is yours. You are equipped to do it.

The book ends here. The work does not.

---

## 12. Final Project — 250 points

This chapter's terminal assessment replaces the standard exercise structure. The final project has two parts; both apply the eleven-component analysis plan to a domain problem.

### Part A — The instructor's domain plus required own-field section (250 pts)

**A.1 Complete analysis plan for the instructor's standard domain (180 pts).** Produce the eleven-component analysis plan, end to end, for the running case from Chapters 12–14. The case substance is provided in the course materials; the structural work is yours. Each of the eleven components is graded against the rubric below. The integration — whether the sections cite each other in the way the chapter requires — is graded separately as part of "Output diagnostic application."

**A.2 Required own-field section (40 pts).** Apply one identification skill from the course (your choice: a DAG defense, a backdoor-criterion derivation, a sensitivity-analysis calculation, a non-identifiability finding with the routes-out memo from Chapter 10) to a question from your own field, separately from the instructor's case. Two pages. The point of the own-field section is to demonstrate that the skill transfers; the instructor's case demonstrates that you can run the full pipeline.

**A.3 AI Use Disclosure, three identification decisions, full long form (30 pts).** Higher bar. See Concept five.

### Part B — Complete analysis of your own domain (250 pts, alternate path)

**B.1 Complete analysis plan for your own domain (210 pts).** Eleven components, end to end, on a question you face in your work, your research, or your studies. The own-domain analysis is harder than the instructor's case in one respect (you supply the domain knowledge) and easier in another (you have the domain knowledge to supply). Students may select Part B in place of Part A by week 12; both paths total 250 points.

**B.2 AI Use Disclosure, three identification decisions, full long form (40 pts).**

### Rubric (per component, applied to whichever path the student selected)

| Component | Points (A) | Points (B) | Criterion |
| --- | --- | --- | --- |
| §1 The question | 15 | 18 | Estimand named specifically. Population specified. Intervention specified. Choice of ATE / ATT / CATE defended against alternatives. |
| §2 The setting and data | 15 | 18 | Time, unit, sources, measured variables, unmeasured variables enumerated. "What was not measured" is an enumeration, not a gesture. |
| §3 The DAG | 18 | 21 | Figure complete. Unmeasured variables present on the graph. No mediators or colliders inadvertently drawn as confounders. |
| §4 DAG defense | 22 | 26 | One paragraph per non-obvious arrow. Assumed-absent arrows justified. The defense survives a methodologist's reading. |
| §5 Identification argument | 22 | 26 | Backdoor paths enumerated. Adjustment set chosen and defended. Identification assumptions named (positivity, consistency, SUTVA). |
| §6 Estimation specification | 15 | 18 | Spec doc complete (estimator, software, parameters, adjustment-set membership, functional form, estimand-type). Do-not-add list as artifact. |
| §7 Estimation output + diagnostic | 18 | 21 | Point estimate, CI, refutation tests, overlap diagnostic. Three-question diagnostic applied with explicit verdicts. |
| §8 Sensitivity analysis | 15 | 18 | E-value at point estimate and CI bound. Domain calibration against plausible confounders (the load-bearing item). |
| §9 Two-register conclusion | 15 | 18 | Technical and plain-language registers, both present. Same conclusion, different audiences. |
| §10 Limits + what would relax them | 10 | 13 | Specific limits paired with specific interventions. Estimated costs / timelines where applicable. |
| §11 AI Use Disclosure | 30 | 40 | Three identification decisions. Domain-specific. Concrete. Generic disclosures earn ≤10. |
| Integration (across all components) | 15 | 15 | Sections cite each other. The document reads as one analysis, not eleven. |
| **Total** | **210** | **252** | (Part A totals 210 + 40 own-field = 250; Part B totals 252 ≈ 250 with rounding.) |

The peer-review artifact is graded separately, on the same 40-point scale, against the peer-review protocol described in Concept two.

---

## 13. Peer Review Protocol — Operational Details

Pairing: randomly assigned within course on week 14, with substitution allowed for declared conflicts of interest (former colleague, current collaborator, supervisor-supervisee relationship). Students who selected Part B may opt into peer-reviewing another Part B student to facilitate domain-specific feedback, at the instructor's discretion.

Timing: complete analyses circulated Monday of week 15. Peer reviews due Thursday of week 15 by 11:59 PM. Author responses to peer reviews due Saturday of week 15 by 11:59 PM. Final presentations Monday of week 16.

Format: peer applies the three-question diagnostic via the Reflect / Inquire / Suggest / Elevate protocol described in Concept two. Output is one page of structured feedback, plus a verdict on each of the three diagnostic questions (pass / pass-with-note / fail) and an Elevate paragraph identifying the analyst's irreducibly-human contribution.

Author response: written, before presentation. Addresses each diagnostic verdict in turn. Does not have to *accept* the verdict (a verdict can be challenged) but must engage it. A response that says "the peer flagged Q2 overlap concern; I disagree because of X" is acceptable. A response that ignores a flagged concern is not.

Final presentation: 15 minutes per student plus 10 minutes of Q&A. The peer reviewer asks the first question after the presentation — typically the question that came out of their review. The instructor (or invited skeptical reviewer) asks the second question. The presentation is the moment the analysis is defended against challenge; the chapter's grade rests substantially on whether the defense holds.

---

## 14. LLM exercise — Closing the course on the AI Use Disclosure thesis

The exercise: ask an LLM to grade your draft analysis using the three-question diagnostic, then identify where the LLM missed the irreducibly-human contribution.

**Prompt to paste into Claude, ChatGPT, or Gemini (or whichever current model is available):**

> I have produced a draft causal analysis plan in eleven sections. I am pasting it below. Please apply the three-question diagnostic to it:
>
> Q1: Is the specification correct? Treatment defined, outcome defined, adjustment set matched between identification argument and estimation spec, do-not-add list respected?
>
> Q2: Does the data support the specification? Overlap acceptable, sample-selection compatible with the estimand, missingness assumptions stated?
>
> Q3: Do the refutation checks pass? Refutation tests stable, sensitivity analysis present, E-value reported with domain calibration?
>
> For each question, return a verdict (pass / pass-with-note / fail) and reasoning. Then assign one of three labels: definitive within scope / suggestive but not definitive / inconclusive. Show your reasoning for the label.
>
> Here is the analysis: [paste your §§1–11 here]

After the LLM responds:

1. Compare its verdicts to your own. Where do you agree? Where do you disagree?
2. Look at the LLM's *reasoning* for each verdict. Specifically: does its reasoning engage the §11 AI Use Disclosure decisions (the three identification decisions you named as load-bearing)? Or does its reasoning operate at the structural level (counting backdoor paths, checking arithmetic on the E-value) without engaging the domain-specific judgments that the disclosure named?
3. Most current models (the Claude 4.x family, GPT-4o and successors, Gemini 2.x) will produce competent verdicts on the procedural questions — Q1's spec consistency, the arithmetic on the E-value, the formal structure of the adjustment set. They will be inconsistent on the domain-judgment questions — whether your domain calibration of plausible confounding is reasonable, whether your three identification decisions in the disclosure are concrete or generic, whether your *suggestive* label is defensible given the stakeholder context. The procedural part is the part the tool can do. The judgment part is the part you, specifically, contributed.
4. Write a one-paragraph note on where the LLM was correct, where it was wrong, and where it gave a confident-sounding answer that did not engage the irreducibly-human content of your analysis. Submit the note with your final deliverable.

This exercise closes the course. The book's thesis was: identification decisions require domain judgment no causal AI tool currently supplies. The exercise tests the thesis on your own analysis. If the LLM caught everything — if it engaged every one of your three identification decisions with the same domain depth you brought — the thesis is wrong in your case, and you should write that, honestly, as your note. If the LLM missed the irreducibly-human part — if its verdicts were competent on the procedural questions and shallow on the judgment ones — the thesis is supported in your case, and you should write that, honestly, with the specific places it missed.

Either finding is the right finding. The exercise is about the honesty of the test, not about the verdict.

---

## 15. AI Use Disclosure — chapter level (higher-bar form)

This chapter was drafted with the assistance of Claude (Anthropic), using the Feynman-voice pedagogical scaffold defined in the workshop's CLAUDE.md and the chapter-specific pantry notes prepared for Chapter 15 of *Causal Reasoning: Irreducibly Human*. The eleven-component structure, the definitive / suggestive / inconclusive register, and the higher-bar AI Use Disclosure are originals proposed in this book; the components individually trace to Hernán 2018, Hernán 2019, Pearl 2018, Hernán & Robins 2020, and prior chapters. The RISE feedback model adaptation cites Emily Wray's original work directly.

Three identification decisions across the full 15-week development of this textbook that required domain expertise no AI tool could supply:

1. *The choice to treat identification as a single pedagogical layer separable from estimation.* Many causal-inference textbooks present identification as a sequence of techniques (matching, propensity-score weighting, instruments) rather than as a single layer of judgment. The book's decision to organize the entire 15-week arc around the identification layer, and to relegate estimation tools to Act Three, came from observing — across several years of teaching ML engineers — that the failure mode in practice is upstream of estimator choice. An LLM-assisted curriculum-design workflow would not have prioritized this organization without that field observation.

2. *The decision to propose the three-label register (definitive / suggestive / inconclusive) even though the standard literature does not formalize it.* The literature has the components (Hernán's *causal* discipline, VanderWeele's calibration-of-conclusion-language argument) but does not assemble them into a tiered labeling vocabulary. The decision to assemble them — and to require students to commit to one label and defend it — is a pedagogical bet that the discipline of forced commitment is worth the cost of over-formalizing. A tool would have summarized the existing literature; the decision to *go beyond* it for pedagogical reasons is mine.

3. *The decision to make the higher-bar AI Use Disclosure the chapter's central deliverable rather than its footnote.* The standard treatment of "AI in causal inference" textbooks is to add a chapter or appendix on LLM-assisted workflows. The decision to make the AI Use Disclosure structurally central, and to require *three* concrete decisions for the final project, came from the book's thesis — and the thesis came from looking at where causal-AI tools currently break down in practice. The placement of the disclosure as the chapter's most consequential pedagogical artifact, rather than as a checkbox, is my decision, and it is the decision the book most lives or dies on.

---

## 16. Part B bonus

If you have completed your final project in Part B (your own domain) and arrived at the *suggestive* label: write a one-page memo to the senior person in your organization who is making a decision based on your analysis. The memo follows the structure of §9–§10 of the worked example. State the finding. Name the source of suggestive-versus-definitive. List the route to definitive with cost estimate. Make the recommendation. Bring the memo to the final presentation; the instructor will use it as the basis for the first Q&A question.

If you have arrived at *inconclusive*: write the same memo, with the recommendation being the design that would convert inconclusive into at least suggestive. The recommendation is the value of the work.

If you have arrived at *definitive within scope*: congratulations, and be ready in the Q&A to defend why your case meets all three layers (identification, sensitivity, domain) at the rule-of-thumb threshold. The instructor will ask. Have the answer ready.

---

## 17. Key terms

- **Eleven-component analysis plan.** The book's terminal deliverable structure: question, setting-and-data, DAG, DAG defense, identification argument, estimation specification, estimation output with diagnostic, sensitivity analysis, qualified two-register conclusion, limits and what would relax them, AI Use Disclosure. Originals to this textbook (Brown 2026); each component traces to prior literature.
- **Peer-review protocol (RISE-adapted, three-question-diagnostic-anchored).** Reflect, Inquire (Q1/Q2/Q3), Suggest, Elevate. One page of structured feedback per peer, written one week before final presentation.
- **Definitive within scope.** Label assigned when identification, sensitivity, and domain layers align. Decision-maker can act on the estimate as evidence within the analyzed population's bounds.
- **Suggestive but not definitive.** Label assigned when one layer is weak — typically the E-value is comparable to plausible confounder strength, or Q2 of the diagnostic shows a non-trivial concern. Treat as motivation to act under monitoring, with a confirmatory study planned.
- **Inconclusive.** Label assigned when a layer fails — identification gap, diagnostic failure on Q1 or Q2, or E-value small relative to plausible confounding. Different design required.
- **Higher-bar AI Use Disclosure.** Final-project form of the disclosure used throughout the book. Names *three* identification decisions across the full 15-week analysis where domain expertise was required that no AI tool could supply. Concrete, domain-specific.
- **Integration (as a graded property of the deliverable).** The property that the eleven components cite each other rather than read as eleven self-contained documents. Section 6 cites Section 5; Section 8 cites Section 5; Section 9 cites everything.

---

## 18. Further reading

- Miguel A. Hernán, "The C-Word: Scientific Euphemisms Do Not Improve Causal Inference From Observational Data," *American Journal of Public Health* 108(5) (2018), 616–619. DOI: [10.2105/AJPH.2018.304337](https://ajph.aphapublications.org/doi/full/10.2105/AJPH.2018.304337). The case for naming causal questions causal. Read once, then once more.
- Miguel A. Hernán, John Hsu, and Brian Healy, "A Second Chance to Get Causal Inference Right: A Classification of Data Science Tasks," *Chance* 32(1) (2019), 42–49. [DOI: 10.1080/09332480.2019.1579578](https://doi.org/10.1080/09332480.2019.1579578). The analytical-task classification that frames the deliverable's shape.
- Miguel A. Hernán and James M. Robins, *Causal Inference: What If* (Chapman & Hall/CRC, 2020). The reference textbook. [Free PDF.](https://miguelhernan.org/whatifbook)
- Judea Pearl, "Theoretical Impediments to Machine Learning With Seven Sparks from the Causal Revolution," *Proceedings of WSDM '18*. [arXiv:1801.04016](https://arxiv.org/abs/1801.04016). Pearl's seven challenges; the book's overall framing builds on this.
- Tyler J. VanderWeele and Maya B. Mathur, "Some Desirable Properties of the Bonferroni Correction: Is the Bonferroni Correction Really So Bad?," *American Journal of Epidemiology* 188(3) (2019), 617–618. [DOI link](https://academic.oup.com/aje/article/188/3/617/5193218). On calibrating conclusion-language strength to evidence strength.
- Sander Greenland, "For and against methodologies: some perspectives on recent causal and statistical inference debates," *European Journal of Epidemiology* 32(1) (2017), 3–20. [DOI: 10.1007/s10654-017-0230-6](https://doi.org/10.1007/s10654-017-0230-6). On methodological responsibility — the methodology is a tool, the analyst is accountable for the analysis.
- Emily Wray, "RISE Model for Meaningful Feedback," 2014-present. [risemodel.com](https://www.risemodel.com/). The original feedback model the peer-review protocol adapts.
- Beth Tipton and Robert Olsen, "A Review of Statistical Methods for Generalizing From Evaluations of Educational Interventions," *Educational Researcher* 47(8) (2018), 516–524. `[verify-DOI]` On generalizability and population specification.
- Allan Collins, John Seely Brown, and Susan E. Newman, "Cognitive Apprenticeship: Teaching the Crafts of Reading, Writing, and Mathematics," in *Knowing, Learning, and Instruction: Essays in Honor of Robert Glaser* (Lawrence Erlbaum, 1989). `[verify-pagination]` The pedagogical evidence for "show 'done' before students begin." The chapter's opening pedagogical move comes from this tradition.
- Stefan Wager, *Causal Inference: A Statistical Learning Approach* (Stanford, manuscript, 2024). [Free PDF.](https://web.stanford.edu/~swager/causal_inf_book.pdf) Engineering-reader reference for the integrated-deliverable workflow.

---

## 19. Draft flags

The following items in this chapter were flagged during drafting and remain pending Nik's review:

- The eleven-component analysis plan as a graded artifact is the book's contribution. The components individually trace to Hernán 2019, Pearl 2018, VanderWeele 2017, and prior chapters; the integration as a unit, and the requirement that the sections cite each other, is original (Brown 2026). The instructor's manual must validate.
- The definitive / suggestive / inconclusive three-label register is original to this textbook. The literature does not standardize this vocabulary. The chapter explicitly flags this when introducing it.
- The higher-bar final-project AI Use Disclosure ("three identification decisions across the full 15-week analysis") is the book's terminal thesis test. The grading rubric for this section is calibrated to reward concreteness over polish; the instructor's manual must guard against the failure mode where students produce generic disclosures and against the inverse failure mode where rubric strictness penalizes a student whose three decisions are concrete-but-shorter than the example in §9.
- The specific engineering domain for the running case across Weeks 12–15 is the instructor's choice (TIKTOC Open Question 2). The worked example in §9 uses pricing-A/B-testing as a placeholder. The eleven-component structure does not depend on the domain; the example's substance does. `[verify-domain-selection]`
- The Tipton & Olsen 2018 *Educational Researcher* DOI for "A Review of Statistical Methods for Generalizing" is `[verify]` — title and venue confirmed in this round; DOI not yet pulled.
- Collins, Brown, & Newman 1989 cognitive-apprenticeship — the pagination in the cited essay volume is `[verify]`.
- VanderWeele & Mathur 2019 was identified by year correction (the original spec called it 2020; the actual *AJE* paper is 2019, vol. 188 iss. 3). Verified in this round.
- The Part B grading-fairness question across diverse student-chosen domains (TIKTOC Open Question 6) is acknowledged in the rubric design; the rubric assigns points to *structural* properties (eleven components, integration, AI Use Disclosure) rather than to domain-specific content, to preserve fairness across domains. The chapter notes the question without claiming to have solved it. `[verify-Part-B-rubric-fairness]`
- The "skeptical reviewer" role for the final presentation — proposed structures: rotating peer, instructor, or invited industry expert. The chapter proposes a default of *peer reviewer asks first, instructor (or invited reviewer) asks second* without claiming this is the only acceptable structure.

---

## What would change my mind

If a causal-AI tool, in 2027 or 2028 or 2029, can independently produce a defensible DAG for a non-trivial engineering domain — including the unmeasured-confounder arrows that come from organizational tacit knowledge rather than from data — and can calibrate plausible confounder strength against domain-specific past analyses rather than against a generic prior, then the book's framing of identification as the irreducibly-human layer would need substantial revision. The book's thesis is not that LLMs cannot help with causal analysis; they manifestly can. The thesis is that the three layers — DAG-arrow selection from tacit organizational knowledge, calibration of plausible confounder strength from domain-specific past analyses, and labeling honest enough to commit *suggestive* against career incentives toward *definitive* — currently require human judgment. If those three layers move into the tool, the chapter changes.

## Still puzzling

I am not yet satisfied with the boundary between *suggestive* and *definitive* under the rule-of-thumb threshold (E-value 2× plausible confounding). The boundary is artificial; real evidence is continuous; two well-trained analysts will sometimes disagree on the same case. I have hand-waved this in the chapter by saying "the argument is what is graded, not the label." That is true and it is also a hedge. A cleaner statement of when the threshold should be 2× versus 3× versus context-dependent is something I am still working out, and I do not yet have a defensible domain-by-domain rule.

---

**Tags:** final-project, eleven-component-analysis-plan, peer-review-protocol, definitive-suggestive-inconclusive, AI-use-disclosure, identification-layer, course-integration
