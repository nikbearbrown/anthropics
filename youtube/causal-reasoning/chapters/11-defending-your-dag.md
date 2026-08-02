# Defending Your DAG — The Three-Part Argument You Have To Make Out Loud


## TL;DR

- TL;DR: A causal model is not finished when the DAG is drawn — it is finished when you can stand in front of two different audiences and defend every arrow, every missing arrow, and every unmeasured confounder, in two...
- The chapter moves through Opening — Two minutes in a code review, Concept one — The three-part defense structure, Part 1 in detail — what an arrow-as-claim actually looks like, Part 2 in detail — why missing arrows are stronger claims than present ones, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

**Suggested titles:**
1. Defending Your DAG — The Three-Part Argument You Have To Make Out Loud
2. Arrows, Absences, and the Variable You Could Not Measure: A Defense in Two Registers
3. The Document Your VP Will Read, And the Document Your Methodologist Will Read

**TL;DR:** A causal model is not finished when the DAG is drawn — it is finished when you can stand in front of two different audiences and defend every arrow, every missing arrow, and every unmeasured confounder, in two structurally different registers. The defense is the artifact that proves the identification layer was performed; the rest of this book is unusable without it.

**Byline:** Nik Bear Brown

**Prerequisites:**
- The full Act Two toolkit (Chapters 5–10): confounders, mediators, colliders, the backdoor criterion in its two parts, minimal adjustment sets, and non-identifiability as a verdict.
- DAG fluency from Chapter 3 — paths, arrows, what "open" and "blocked" mean.
- The identification layer's framing from Chapter 4 — what the layer is, why nothing downstream can fix what is broken upstream.
- Chapter 2's distinction between causal and associational claims — the basis of the evidence-source discipline you will exercise here.

**Learning objectives:**
- **Evaluate.** State every arrow in a given DAG as a causal claim with an explicit evidence or domain-knowledge source.
- **Evaluate.** Produce a ranked list of missing arrows for a given DAG, ranking by plausibility of the absence and naming the consequence if the absence were wrong.
- **Evaluate.** Name at least two unmeasured confounders for a given problem, with the qualitative bias direction each implies on the estimated effect.
- **Create.** Translate a technical three-part defense into a one-page plain-language register for a decision-maker who will never see the DAG.

---

## 1. Opening — Two minutes in a code review

It is a Thursday in March 2024. You have built a DAG for an internal pricing analysis. The team's senior staff engineer — let me call her Priya — has agreed to give it twenty minutes in code review. You have nine arrows on the graph, three confounders in the adjustment set, two variables explicitly excluded as mediators, and a 280-line analysis notebook that produces the effect estimate. You believe the DAG is right. The estimate is +3.1% on weekly category revenue, plus or minus 0.9.

Priya pulls the diagram up. She reads it for forty seconds. Then she points at one arrow — the one from `competitor_price` to `units_sold` — and says, *why that direction?*

You freeze. You have an answer; you just have not said it out loud before. You start to say *because the competitor sets prices independently before we observe them*, but Priya is already pointing at the next arrow, the one from `inventory_state` to `algorithm_recommendation`, and asking *what study tells you that goes that way and not the other?* You try to recover. She points at a place on the diagram where there is no arrow — between `promotional_intensity` and `units_sold` — and asks, *why isn't there one here?* You begin to answer. She interrupts: *and what's the unmeasured variable that you're worried about most, and which way does its bias go?*

Three minutes have gone by. You have answered none of her questions cleanly. The DAG is *probably* right — you spent two weeks building it, you read the papers, you talked to merchandising — but right does not survive a review by itself. Right has to be defendable, on demand, in the language the reviewer is speaking.

Twenty minutes later, the review ends. Priya is reasonable. She tells you the analysis looks plausible and she's happy to look at it again next week. What she does not say, and what both of you know, is that she has not yet seen anything she can stand behind. She has not seen a defense. She has seen a diagram and a number.

Now let me run the same scene a week later. You have done the same analysis. The DAG is identical. The estimate is identical. The notebook is identical. *One thing* has changed: alongside the diagram you have a three-page document. Page one is a numbered list of every arrow, each with one sentence stating the causal claim and one sentence naming the evidence — sometimes a published study, sometimes a documented mechanism from the business, sometimes the explicit admission *this one is from domain folklore and the team agrees*. Page two is a numbered list of the four most plausible missing arrows, ranked from "I am least confident this absence is right" to "I am most confident," each with one sentence on what would change if I were wrong. Page three names the two unmeasured confounders I am most worried about, with the direction each would bias the estimate.

Priya reads page one for a minute. Then she points at the `competitor_price → units_sold` arrow and says, *why that direction?* You point at line 4 of the document: *Competitor prices are scraped at 06:00; our pricing algorithm runs at 09:00; arrow direction follows the temporal order.* She nods. She points at the absence between `promotional_intensity` and `units_sold`. You point at line 2 of page two: *I'm 70% confident this absence is right because promo intensity is set independently of within-day demand by the marketing calendar — but if I'm wrong, it would only inflate the estimate, not flip its sign.* She nods again. *What unmeasured variable worries you most?* You point at page three. She reads for thirty seconds.

The review ends in seven minutes instead of twenty. Priya says, *ship it; one comment about the promo-intensity absence; let's revisit in three weeks.* The analysis was the same in both scenes. The defense was the difference between *we will need to talk again* and *ship it*.

The chapter you are reading is about that document. It has three parts and two registers. It is the most domain-judgment-intensive artifact in this entire book. And — to telegraph the chapter's thesis bluntly — it is the part of the work that the causal-AI tool downstream cannot do for you, because the defense is *exactly* the thing the tool needs *from* you in order to do anything at all.

---

## 2. Concept one — The three-part defense structure

A causal model is complete when the analyst can produce three things on demand, in front of someone trying to break the model. Not when the DAG is drawn. Not when the adjustment set is chosen. Not when the estimate is computed. When the three things are written down and survive a hostile read.

Let me name the three parts, and then I am going to walk through what each one *actually contains* on the page.

**Part 1 — Arrows-as-claims.** Every directed edge in your DAG is converted from a graphical line into a sentence of the form *X causally affects Y, holding everything else fixed, on the basis of [named evidence].* The defense is not the diagram. The diagram is the index. The defense is the list of sentences the diagram indexes into.

**Part 2 — Missing arrows, ranked by plausibility.** For every pair of variables you considered and chose *not* to connect, you state the absence as a sentence, you assign a rough prior to your confidence in the absence, and you name what would change if you were wrong. This list is ranked — *most confident the absence is right* at one end, *least confident* at the other. The list does not have to be exhaustive. It has to be honest about the ones the reviewer is most likely to push on.

**Part 3 — Unmeasured confounders, with bias direction.** For at least every plausibly-substantial unmeasured variable U that could affect both treatment and outcome, you name (a) U, (b) the qualitative direction of U's effect on the treatment, (c) the qualitative direction on the outcome, (d) the product — which is the qualitative direction of the bias U introduces into your estimate, and (e) any rough magnitude bound you can defend.

Why these three parts and not five, or two? Because these three are the *load-bearing* claims of the entire identification layer. If your arrows are wrong, you have built the wrong DAG. If your missing arrows are wrong, you have built the wrong DAG by omission, which is *exactly the same failure mode* with a different surface. If your unmeasured confounders are wrong, you have not done the trust assessment Chapter 10 ended with — you have produced a point estimate under unstated assumptions, and that is the failure mode this whole book exists to prevent.

Now let me unpack each part in the same way I would in a workshop, slowly, with the discipline made visible.

### Part 1 in detail — what an arrow-as-claim actually looks like

Take an arrow `A → B` on a DAG. In the diagram, it is a line with an arrowhead. In the defense, it is at least two sentences:

1. *A causally affects B, holding the other variables in the model fixed.*
2. *The evidence supporting this claim is [study citation / documented mechanism / expert consensus / tool output, with the source named].*

The two sentences are not optional and not interchangeable. Sentence one is the *structural commitment*: under intervention on A, B would change in expectation. Sentence two is the *epistemic commitment*: this is the basis on which I am willing to make sentence one.

I want to be ruthless about what counts as evidence in sentence two, because the loose version of this discipline produces what looks like a defense but is actually a vibe. Here is the hierarchy of acceptable bases for a causal arrow:

- **Randomized study with the same population and outcome.** Strongest. Rare. Often unavailable.
- **Quasi-experimental study** — instrumental variables, regression discontinuity, difference-in-differences, with the identifying assumption credibly defended in the source paper. Strong.
- **Multiple observational studies with concordant findings and a coherent mechanism story.** Moderate, often the realistic ceiling.
- **A single observational study, well-conducted, with a sensible adjustment.** Weaker, but acceptable for arrows whose direction is mechanistically obvious (age → health outcomes; tenure → salary).
- **Mechanistic argument from physics, biology, business logic, or product instrumentation.** Acceptable when the mechanism is explicit and the alternative directions can be ruled out. *Competitor prices scraped at 06:00 cannot be caused by our 09:00 algorithm* is a mechanistic argument by temporal precedence.
- **Expert consensus, named.** Acceptable when the expert is in fact a domain expert and the consensus is genuinely consensus. *I asked Priya, who runs pricing, and she confirmed* is acceptable in an internal document; it is not acceptable as a citation in a published paper.
- **Candidate from a tool output (DAGitty, causal-discovery algorithm, LLM).** Acceptable as a *starting point*, never as a *defense*. A tool's output is a hypothesis. A defense converts the hypothesis into a stated reason a human is willing to underwrite.

What is *not* acceptable:

- "The correlation is strong." Not evidence for causation. Chapter 2 was about this.
- "The variable seemed relevant." Not a claim; a feeling.
- "The LLM suggested it." See the previous list — candidate, not defense.
- "It was in the data export." Pure availability is not structure.
- "My manager said so." Not a defense unless the manager is the domain expert and you are willing to name them and the basis of their judgment.

Most engineering DAGs have between five and fifteen arrows. A defense produces that many short, evidence-tagged paragraphs. Five to fifteen short paragraphs. That is all Part 1 is.

### Part 2 in detail — why missing arrows are stronger claims than present ones

This is the part of the defense students get wrong most often, and it is the part that distinguishes a defense from a wishlist. Let me state the thing clearly.

A DAG is just as much a claim about what is *not* connected as about what is. When you decline to draw an arrow between `manager_id` and `employee_motivation` in a training-program DAG, you are asserting — *structurally* — that there is no direct causal effect of manager identity on motivation that is unmediated by the other variables in your model. That is a strong claim. It is, in fact, a *stronger* claim than asserting the arrows you did draw, because it excludes an entire class of dependencies rather than asserting one of them.

The procedural move: for the missing arrows your reviewer is most likely to ask about, write a short paragraph each. The paragraph has three components:

1. **The absence stated as a claim.** *There is no direct causal effect of M on Y, holding the rest of the model fixed.*
2. **Your subjective prior on the absence being correct.** This is a calibrated rough probability — 90%, 70%, 50%. The number does not have to be sharp; it has to be honest about your uncertainty.
3. **The consequence if you are wrong.** If the arrow really exists, would it bias your estimate up, down, or in an unclear direction? Would it change the sign, the magnitude, or only the confidence interval? Would it threaten identification entirely, or only nudge the estimate?

Now the harder discipline — the *ranking*. The reviewer does not want to read fifteen missing-arrow paragraphs. They want to read the four or five that you are *least confident* about, because those are the ones a critic would push hardest on. Order the list from "least confident this absence is right" at the top to "most confident" at the bottom. The reviewer reads top-down and stops when they are satisfied.

Why "least confident at the top" and not "most confident at the top"? Because the *point* of the document is to surface the weaknesses, not to celebrate the strengths. The strongest defense — and I want this to sit in your head as a slogan — is the one that surfaces its own limits before the reviewer asks. A document that opens with "here is the absence I am 70% sure about" is doing the work. A document that opens with "here is the absence I am 99% sure about" is performing confidence.

The mathematical intuition for *why missing arrows are stronger claims* is worth a moment. A DAG with every possible arrow drawn has no testable implications — it is consistent with any joint distribution. Adding an arrow only *adds* a degree of freedom to the model. Removing an arrow *constrains* the model. Every absence is a falsifiable structural claim. This is the d-separation insight from [Pearl's *Causality*, second edition (Cambridge, 2009)](https://bayes.cs.ucla.edu/BOOK-2K/) — the *graphical* content of a DAG lives in its absences, because the absences are what license the conditional independencies you can test in the data.

The reviewer who understands d-separation will, sometimes, point to a conditional independence implied by your missing-arrows list and check it in the data. Ankan, Wortel, and Textor's 2021 *Current Protocols* paper ["Testing Graphical Causal Models Using the R Package `dagitty`"](https://doi.org/10.1002/cpz1.45) walks through exactly this procedure. If a missing arrow implies an independence the data rejects, the absence is empirically unsupported — and the defense's prior on that absence has to come down. This is one of the few places where the data can directly *check* a piece of your DAG. The missing-arrows list is what makes the check addressable.

### Part 3 in detail — the humility move, made specific

Part 3 is where you name what you could not measure. Every observational analysis has unmeasured confounders. Every one. The question is not whether they exist; the question is whether you have stated them and stated the direction they push your estimate.

For each unmeasured U you are willing to name, the defense produces:

- **The variable's identity.** Not "unmeasured confounding." *Patient motivation to manage their own disease.* Specific. Named. A reader could imagine an instrument that would measure it.
- **U's direction on T.** Qualitative. *Motivated patients are more likely to enroll in the coaching program.* Positive.
- **U's direction on Y.** Qualitative. *Motivated patients have lower HbA1c six months later through behaviors separate from the program.* Negative (because lower HbA1c is the "better" direction, but watch your signs — what matters is the *direction of the relationship*, not the goodness).
- **The bias direction on your estimate.** The product of the two above. If U is positive on T and U is negative on Y (motivated → enroll, motivated → lower HbA1c), then naive comparison of enrolled vs. unenrolled overestimates how much *the program* reduces HbA1c. The bias is *toward making the program look better than it is*.
- **A rough magnitude bound.** This is the hardest of the five components and the one most often skipped. You do not need a number. You need a *bound* — "at most as large as the effect of baseline HbA1c on six-month HbA1c, because motivation cannot plausibly be a stronger predictor than baseline disease severity" is a defensible magnitude bound. You need *something*, because Chapter 14's E-value calculation will take this bound as input.

The misconception worth naming explicitly: students treat the "I do not have a view on direction" answer as an acceptable default. It is rarely acceptable. There are genuine structural cases where U's direction on the bias is symmetric — perfectly randomized cross-cutting unobservables, certain instrument validity tests — but they are rare. For the routine engineering case, *you have a view on the direction*. You may not have a sharp magnitude. You may have a wide confidence interval on the magnitude. But you have a view on the direction. The defense forces you to write it down.

The Tyler VanderWeele–Peng Ding 2017 *Annals of Internal Medicine* paper introducing the E-value ([VanderWeele and Ding 2017](https://doi.org/10.7326/M16-2607)) is the canonical reference for this discipline; the qualitative version of it lives in Part 3 here, the quantitative version arrives in Chapter 14. The reason Part 3 of the defense matters *now*, even before the quantitative machinery, is that the named unmeasured confounders are the *inputs* to that machinery later. A defense that says "there might be unmeasured confounding" is not yet usable for sensitivity analysis. A defense that names the variable and the direction is.

---

### Mid-chapter checkpoint

Before reading further, can you do the following on a DAG you draw cold, in fifteen minutes?

1. Write one sentence stating the causal claim for each arrow, plus one sentence naming the evidence source.
2. List three missing arrows, with a prior on each absence and what would change if you were wrong.
3. Name two unmeasured confounders, with bias direction on the estimate.

If any of those moves still feels improvisational, the second half of the chapter — where I show how the three-part technical defense gets re-shaped into the plain-language register for a decision-maker — will not land yet. The plain-language register is structural transformation, not vocabulary swap, and it presupposes that the technical register exists.

---

## 3. Concept two — How to state an arrow as a causal claim, concretely

Let me run the discipline on a real-looking DAG so the template is something you have actually used, not just heard.

Suppose you are studying an A/B test of a new recommendation algorithm. Treatment T is the assignment to the new algorithm (binary, randomized at the user level). Outcome Y is seven-day retention (binary: did the user come back at least once between days 1 and 7). The DAG has, in addition to T and Y, three covariates: `prior_engagement` (a user's engagement in the seven days before the experiment started), `cohort_age` (days since signup), and `seasonality` (a derived weekday × time-of-day feature for the user's typical session).

The arrows you drew:

- `prior_engagement → T` — assignment was randomized, but stratified on engagement quintile, so engagement formally appears upstream.
- `prior_engagement → Y` — past behavior predicts future behavior.
- `cohort_age → prior_engagement` — older cohorts have had time to settle into engagement patterns.
- `cohort_age → Y` — older cohorts have different baseline retention.
- `seasonality → Y` — different days have different retention base rates.
- `T → Y` — the effect we want to estimate.

Six arrows. Now I do Part 1 of the defense. One paragraph per arrow.

> **Arrow 1: `prior_engagement → T`.** *Prior engagement causally affects assignment.* Evidence: instrumented at the experiment-design layer. Our randomization was stratified on the engagement quintile to ensure balance. The assignment service code lives in `experiments/assignment_v3.py`, lines 142–168, and the stratification is implemented there. This is mechanism-from-instrumentation evidence, the strongest internal kind.

> **Arrow 2: `prior_engagement → Y`.** *Prior engagement causally affects future retention.* Evidence: well-documented in the recommender-systems and consumer-behavior literatures; the [Kohavi-Tang-Xu 2020 *Trustworthy Online Controlled Experiments*](https://experimentguide.com/) textbook treats this as a standard pre-treatment covariate in retention experiments. Internally, we have three years of A/A tests showing prior engagement is the strongest single predictor of seven-day retention. Mechanism-and-multiple-internal-studies evidence.

> **Arrow 3: `cohort_age → prior_engagement`.** *Cohort age causally affects pre-experiment engagement levels.* Evidence: mechanical — older users have had more time to develop a usage pattern. Internal cohort analyses (referenced in `docs/cohort-analysis-2024-q1.md`) show engagement levels stabilize around day 30 post-signup. This is a documented-mechanism arrow.

> **Arrow 4: `cohort_age → Y`.** *Cohort age causally affects seven-day retention independent of engagement level.* Evidence: weaker than the above. We have an internal claim that newer-cohort users have higher base retention because of the onboarding-promotion effect — a 7-day reactivation push from the lifecycle team. The arrow's direction is set by that promotion mechanism. This evidence is internal-only; I have not found a published study on the exact effect.

> **Arrow 5: `seasonality → Y`.** *Day-of-week and time-of-day patterns causally affect retention.* Evidence: standard in behavioral analytics. Documented in the same Kohavi-Tang-Xu textbook and in our internal weekly retention reports. Mechanism: users with different schedules have different opportunities to return within seven days. Mechanism-plus-internal-data evidence.

> **Arrow 6: `T → Y`.** *Assignment to the new recommendation algorithm causally affects retention.* This is the effect we are trying to estimate. The arrow's existence is a hypothesis, not an evidence-backed claim — the entire purpose of the analysis is to estimate its magnitude. The arrow is in the DAG because that is the structural commitment the analysis tests.

Notice what the Part 1 defense forces you to surface that the DAG alone does not. Arrow 4 — `cohort_age → Y` — has weaker evidence than the others. The reviewer, scanning Part 1, sees this immediately. If they are going to push on any single arrow, this is the one. The defense has done the reviewer's first scan for them, and has done it honestly. That is the move.

Arrow 6 deserves a separate note because students sometimes get confused about it. The treatment-to-outcome arrow is the arrow whose magnitude the analysis is *estimating*. It is in the DAG because you believe a causal effect exists — possibly zero, possibly nonzero. The evidence for the arrow's *existence* is the experimental design itself: we are running this analysis because we have reason to think the new algorithm might affect retention, and the experiment is what produces the evidence. The Part 1 defense of arrow 6 is honest about this — it is not pretending to have evidence for the magnitude. The magnitude is what the analysis produces.

This is the rhythm of Part 1. Short paragraphs. Named evidence. Honest about gradients of strength. The reviewer can scan the list and find the weakest link in thirty seconds, which is precisely what they want to do.

---

## 4. Concept three — Ranking missing arrows, the hardest move

Part 2 is where the defense bends most against the analyst's instinct. The instinct is to *justify what you did*. The discipline is to *surface what you almost did and chose not to*. Most engineers, on the first pass, produce a Part 2 that looks like "I did not add `manager_id` because it is post-treatment" and call it done. That is not a ranked missing-arrows list. That is one bullet from a wishlist.

Let me show you what the move actually looks like, on the same A/B test DAG.

The candidate missing arrows — arrows the reviewer might ask about — are the ones between *plausible* variables that I chose *not* to connect. From the six-arrow DAG above, the candidate missing arrows include:

- `seasonality → prior_engagement` — does seasonality affect pre-experiment engagement?
- `cohort_age → T` — does cohort age affect assignment?
- `seasonality → T` — does seasonality affect assignment?
- `T → prior_engagement` — does the new algorithm affect engagement during the pre-treatment window (a *temporal impossibility*, but the reviewer may still ask)?
- `prior_engagement → seasonality` — does engagement level affect the user's seasonality profile?
- An arrow representing `notification_volume`, a variable I considered but did not include in the DAG at all, to either T, Y, or any other node.

The Part 2 defense, ranked from "least confident the absence is right" to "most confident":

> **Missing arrow 1 (least confident): `notification_volume → Y`.** I am roughly 60% confident this absence is correct. The argument for the absence: notification volume is set by the lifecycle team's separate logic, the cadence has been stable for six months, and to first order it is the same for both treatment and control. The argument against: there is a known interaction between the recommendation algorithm and the notification ranker (described in `docs/recsys-notif-interaction.md`), and if the new algorithm changes which items are surfaced, the notification ranker may surface different items, which would change downstream notification engagement and thus retention. If this arrow exists, my estimate would be biased *upward* (the algorithm is getting credit for some of the notification-system uplift) by an amount bounded by the notification-system's documented effect on retention, which is on the order of 0.4 percentage points. This is the missing arrow I am most worried about.

> **Missing arrow 2: `seasonality → prior_engagement`.** Roughly 70% confident this absence is correct. Seasonality is a feature derived from the user's *typical* session pattern, computed over a 90-day rolling window. Prior engagement is a count over the seven days immediately before treatment. The 90-day feature could in principle reflect seasonal sub-patterns that affect the 7-day count. If the arrow exists, the bias on the estimate is *unclear* in direction because seasonality is balanced by randomization. I am only 70% confident because the rolling window's start can land on different parts of a user's seasonal cycle, which could correlate with engagement.

> **Missing arrow 3: `cohort_age → T`.** Roughly 95% confident this absence is correct. Assignment was randomized; stratification was on engagement quintile, not on cohort age. The assignment service does not read cohort age. If the arrow exists, it would have to enter through some sampling-frame artifact (e.g., the experiment was only available to certain cohorts), and we documented that the experiment ran across all active cohorts. The bias would be in the same direction as cohort age's relationship with Y, which is small.

> **Missing arrow 4 (most confident): `T → prior_engagement`.** 99% confident this absence is correct. The pre-treatment engagement window closes 24 hours before assignment. The new algorithm cannot affect engagement that occurred before it was assigned. The only way this arrow exists is if there is a leakage bug in the data pipeline, which the team has explicitly tested for (test `tests/test_pre_treatment_leakage.py`, last passed yesterday). If the arrow exists, it indicates an instrumentation bug rather than a structural fact, and the analysis would have to halt.

Notice what the ordering produces. The reviewer reads top-down. By the time they have read missing-arrow 1 — the one I am only 60% confident about — they know I have already surfaced the weakest part of my own model. They can either accept the argument I made (and the bound on the bias if I am wrong) or they can push back with new information ("did you know the notification ranker was changed last week?"). Either way, the conversation moves forward. The reviewer is not playing *gotcha* against a defense that pretended to be airtight. They are auditing the prior on the absence I already flagged.

The reverse ordering — *most confident absence first* — produces the opposite dynamic. The reviewer reads "I am 99% sure T does not cause prior engagement," nods, and then has to *discover* on their own where my weakness is. That is the dynamic of the unprepared defense. It wastes their time and makes me look like I have not done the work even when I have.

I want to name a misconception, because it sits exactly here. Ranking by "least confident first" is *not* leading with weakness. It is leading with *visibility*. The strongest defense is the one whose author has audited their own work harder than the reviewer will. A reviewer who looks at Missing arrow 1 and thinks "I would have raised exactly this point" has had their objection answered before it left their mouth. That is not weakness. That is the analyst doing the reviewer's first thirty seconds of work for them.

---

## 5. Concept four — The plain-language register, and why it is structurally different

Now the chapter's second crux move. The defense I just wrote — the six-arrow Part 1, the four-paragraph Part 2 — is the *technical* register. It is written for Priya, the senior staff engineer who runs code review. It is also written for the methodologist who will read the analysis if it gets submitted for a peer or regulatory review. It is the right document for those audiences.

It is the *wrong* document for your VP.

Your VP is going to make a decision based on this analysis. The decision is whether to ship the new recommendation algorithm to all users. The VP does not read DAGs. The VP does not know what a backdoor path is. The VP has fifteen minutes between the analytics meeting and a board call. What the VP needs from you is a document the VP can act on, in the time the VP has, that does not hide the things the analyst is uncertain about.

Most engineers, on the first attempt, produce the plain-language register by *substitution*: take the technical defense, swap technical terms for plain English, send it. This produces what the [Sgaier–Huang–Charles 2020 *NPJ Digital Medicine* paper on translating causal inference into decision-maker action](https://www.nature.com/articles/s41746-020-0301-z) calls "technical text with the vocabulary softened" — and it is the most common failure of stakeholder communication in applied causal work. `[verify-exact-citation]` It fails because the plain-language register is not the technical register with a vocabulary swap. It is a *structurally different document* that foregrounds different things, suppresses different things, and ends with a different shape.

The structural difference, stated carefully:

| Feature | Technical register | Plain-language register |
|---|---|---|
| **Opens with** | The DAG and the arrows-as-claims list | The business question and the headline finding |
| **Confidence framed as** | A bound on bias, a width on a confidence interval, a prior on an absence | A named decision and the evidence weight backing it |
| **Uncertainty appears** | Distributed across Parts 1, 2, 3 — every arrow, every absence, every U | Concentrated in one named sentence: "the strongest thing we do not know" |
| **Number translated to** | A coefficient with units and a standard error | A consequence on the business outcome the decision-maker cares about |
| **Closes with** | The adjustment set, the identification verdict, and any partial-identification bounds | Two sentences: *what decision this supports*, and *what decision this does not support* |
| **Length** | 3–5 pages | 1 page, sometimes a half-page |
| **Audience question answered** | *Is the analysis methodologically sound?* | *Can I make this decision based on this evidence?* |

The plain-language register answers five questions, in this order. The five questions are not vocabulary; they are the document's *structure*:

1. **What was the question, in business terms?**
2. **What did the analysis find?**
3. **What confidence is warranted, and why?**
4. **What would we need to know to be more certain?**
5. **What decision does this support, and what decision does it *not* support?**

Let me run the same A/B test through this structure, side-by-side with the technical register so you see the transformation. The technical register's headline is the adjusted estimate: +1.2 pp ± 0.3 pp on seven-day retention, identifiable given stratified randomization, no unmeasured confounders within the experimental population, with the caveat that the notification-system interaction (Missing arrow 1) bounds the upward bias at ~0.4 pp.

The plain-language register, one page:

> **Subject:** Recommendation algorithm A/B test — readout for the launch decision
>
> **The question.** Should we launch the new recommendation algorithm to all users?
>
> **The finding.** Users in the test group came back during their first week 1.2 percentage points more often than users in the control group — about one additional return visit per 80 users per week. The test ran for two weeks on a randomly selected 5% of new users.
>
> **What we are confident about.** The randomization worked: the test and control groups were balanced on the variables we measured. The size of the effect was measured precisely enough that we are confident it is positive — there is essentially no plausible scenario where the new algorithm hurts retention in this user population.
>
> **What we are not confident about.** There is one substantive uncertainty: the new algorithm interacts with the notification system in a way we have not fully traced. Some of the 1.2 pp lift we measured may actually be coming from notifications surfacing better items, rather than from the algorithm itself. Our best bound says this could account for at most about a third of the measured effect. The other two-thirds is the algorithm.
>
> **What would change the picture.** A direct test of the notification interaction — running the new algorithm with the notification system held constant — would distinguish which share of the lift belongs to which system. This would take three more weeks and require coordination with the lifecycle team. It is the cleanest next step if the decision is high-stakes enough to warrant it.
>
> **What this supports.** This analysis supports launching the new algorithm to all users *in the same user population as the test* (new users in their first 30 days), at the budget allocated for the lifecycle-team's current notification cadence. The two-week effect is the right window for that decision.
>
> **What this does not support.** This analysis does not support claims about long-tenured users (not in the test), about retention beyond seven days (not measured), about behavior under a different notification cadence (held constant during the test), or about content categories that were rare in the test window. If any of those become the load-bearing question for the decision, we need a different analysis.

That is one page. The VP reads it in ninety seconds. The VP knows three things at the end of the page: the algorithm helps in the population we tested, there is one named uncertainty bounded at roughly one-third of the effect, and there is a specific decision the analysis *does not support* (the long-tenured-user question). The VP can now do their job, which is to weigh that against the other inputs they have.

The plain-language register is not dumbed down. Read the technical register again, then read the plain-language one. The plain-language version carries *every substantive piece* of the technical version's uncertainty: the notification interaction is there, the bound is there, the population restriction is there, the time-window restriction is there. What is *not* there are the words *backdoor*, *adjustment set*, *identifiability*, *covariate*, *stratification*, and the DAG itself. The structural commitments are encoded in business terms — *"users in the same population as the test"* is the population-restriction commitment; *"in the test window"* is the temporal-validity commitment; *"under the current notification cadence"* is the held-constant-covariate commitment. The vocabulary changed. The structure of the honest acknowledgment did not.

Let me name where the two-register discipline can over-formalize, because the method applies to itself. Some decision-makers do want the technical version — chief data officers, VPs of analytics, people who came up through ML and read DAGs comfortably. For them, the technical register *is* the decision document. Some decisions do not have a single decision-maker; they have a committee where one member wants the technical version and another wants the plain-language version. The chapter's rigid "two registers, distinct documents" template is the right starting discipline; it is the wrong endpoint for every audience configuration. Read the audience, then choose. The rule is *write the document the reader can act on*; the two-register template is a default that works in the majority of engineering settings, not a law.

The hardest of the five questions, by margin, is question 5 — *what decision does this not support?* Engineers default to "here are the results, you decide," which is an *abdication* of the analyst's responsibility to name the boundary. The "does not support" sentence is the most domain-judgment-intensive sentence in the entire defense. It is also the sentence the LLM cannot produce for you — not yet, possibly not ever — because it depends on the analyst's understanding of which decisions are *adjacent* to the question the analysis answered. That is a piece of domain knowledge no tool currently has.

---

## 6. Concept five — The reproducible defense template

You have seen the three parts and the two registers. Let me consolidate them into a template you can use in next week's review meeting. The template is reproducible — every chapter from here to the end of the book, and the final project, will use it.

### Technical register — 3–5 pages, in this order

```
TREATMENT: [name]
OUTCOME: [name]
ESTIMAND: [total effect / direct effect / controlled direct effect — pick one]
DAG: [figure reference]

PART 1 — ARROWS AS CLAIMS
For every directed edge X → Z in the DAG:
  - Causal claim: X causally affects Z, holding the rest fixed.
  - Evidence source: [study citation / mechanism / consensus / instrumentation /
    tool candidate, named explicitly]
  - Strength tag: [randomized / quasi-experimental / multiple-observational /
    mechanistic / consensus / candidate]

PART 2 — MISSING ARROWS, RANKED LEAST-CONFIDENT FIRST
For the top 3–5 missing arrows the reviewer is most likely to ask about:
  - Absence as a claim
  - Prior on the absence being correct (rough %, calibrated honestly)
  - Consequence if wrong: bias direction, bias magnitude bound, whether
    identification is threatened

PART 3 — UNMEASURED CONFOUNDERS WITH BIAS DIRECTION
For at least 2 unmeasured Us:
  - Variable identity (specific, named)
  - Direction on T
  - Direction on Y
  - Bias direction on the estimate (product)
  - Rough magnitude bound (a defended ceiling, even if loose)

ADJUSTMENT SET: Z = {z_1, z_2, ...} — path-blocking justification per Chapter 9
IDENTIFICATION VERDICT: [identifiable / partially identifiable / not identifiable]
WHAT THIS ANALYSIS CAN CONCLUDE: [bounded statement]
WHAT THIS ANALYSIS CANNOT CONCLUDE: [the non-identifiable parts]
```

### Plain-language register — one page

```
SUBJECT: [the decision being made, in one line]

THE QUESTION: [in business terms, no jargon]

THE FINDING: [one number, translated into business consequence,
  in a sentence the decision-maker can repeat from memory]

WHAT WE ARE CONFIDENT ABOUT: [one paragraph]

WHAT WE ARE NOT CONFIDENT ABOUT: [one paragraph naming the
  single biggest uncertainty, with its bounded consequence]

WHAT WOULD CHANGE THE PICTURE: [the named next-step study or
  data collection, with cost/timeline if you have them]

WHAT THIS SUPPORTS: [the decision this evidence supports,
  with its scope conditions]

WHAT THIS DOES NOT SUPPORT: [the adjacent decisions this
  evidence does NOT support — explicit, with verbs]
```

Print this template. Stick it on your monitor. The first ten times you use it, the structure will feel like compliance overhead. The eleventh time, you will use it because the analyses you ran without it produced documents you could not defend in code review and could not put in front of a VP. The template *is* the defense.

The template's parentage: the technical register is a synthesis of Hernán–Robins's structural-defense tradition (Chapter 7 of [*Causal Inference: What If*](https://miguelhernan.org/whatifbook), 2020), Pearl–Mackenzie's defense-in-prose move (Chapters 9–10 of [*The Book of Why*](https://bayes.cs.ucla.edu/WHY/), 2018), and the model-card discipline from [Mitchell et al. 2019, "Model Cards for Model Reporting," FAccT 2019](https://doi.org/10.1145/3287560.3287596). The plain-language register's structure is informed by [David Spiegelhalter's *The Art of Statistics* (Pelican, 2019)](https://dspiegel.com/the-art-of-statistics) on principled uncertainty communication and by the structural-defense tradition in epidemiology, including Miguel Hernán's 2018 *AJPH* essay "The C-Word: Scientific Euphemisms Do Not Improve Causal Inference From Observational Data" ([Hernán 2018](https://doi.org/10.2105/AJPH.2018.304337)), which argues that hedged language hides causal claims rather than clarifying them — directly applicable to the plain-language register's discipline of stating findings plainly while bounding them honestly.

DAGitty (https://www.dagitty.net/) is the tool that supports the technical register's machinery — the package will compute adjustment sets, list testable implications of missing arrows, and produce the figure. [Textor, van der Zander, Gilthorpe, Liśkiewicz, and Ellison 2016, "Robust causal inference using directed acyclic graphs: the R package 'dagitty,'" *International Journal of Epidemiology* 45(6), 1887–1894](https://doi.org/10.1093/ije/dyw341) is the citation. The tool gets you the *machinery* of the technical register. It does not get you the *defense*. The defense — the evidence source on each arrow, the rank of plausibility on each absence, the bias direction on each unmeasured confounder, the boundary on the decision — is yours.

---

## 7. Integration — The thesis, made literal

Let me close the loop with the book's argument and what this chapter does to it.

The book's thesis is that the identification layer of causal analysis currently requires domain judgment no causal AI tool can supply, and engineers who use causal AI without performing that layer are producing conclusions they cannot defend. Chapter 11 is where *cannot defend* becomes literal rather than rhetorical.

The defense — Parts 1, 2, 3, both registers — is a document with seven kinds of judgment in it. Let me list them, because I want you to see how many places the irreducibly-human work shows up:

1. **Which arrows to draw at all.** Domain.
2. **Which direction each arrow goes.** Mechanism, temporal precedence, biology, business logic.
3. **What counts as evidence for each arrow.** Calibration against published literature and internal data.
4. **Which absences to surface and rank.** Anticipation of the reviewer.
5. **The prior on each absence being correct.** Calibrated subjective probability.
6. **The named unmeasured confounders and their bias directions.** Domain plus structural reasoning.
7. **Which decisions the analysis supports vs. does not support.** Adjacency reasoning about the question space.

For each item in the list, ask: *can the LLM produce this?* The LLM can produce *drafts* of all seven. It can suggest candidate arrows. It can hypothesize directions. It can write evidence-source paragraphs. It can rank absences. It can name unmeasured confounders. It can write the plain-language register. I have tested it. So have you, probably. The drafts look plausible. They use the right words. They have the right structure.

What the LLM cannot do — what every test I have run confirms it cannot yet do — is *stand behind* the drafts. The LLM will produce a defense for an arrow that does not exist in your actual business. It will rank an absence with high confidence based on training data that bears no relationship to your data pipeline. It will name an unmeasured confounder that is, in fact, measured at your company. It will write a plain-language register that says *"this analysis supports launching"* in cases where the analysis does not. The defense is plausible-sounding text; the underlying domain claims are not the analyst's claims, and the analyst has not yet stood behind them.

This is the chapter's hardest move to convey to engineering readers who use LLMs daily for everything else. The LLM is genuinely useful as a *scaffolding tool*. It is plausible-but-not-yet-defensible as a *defense author*. The two roles are different. The LLM can draft Part 1; you defend Part 1. The LLM can suggest Part 2 candidates; you rank Part 2. The LLM can write the plain-language register; you decide what the analysis does and does not support. The signature on the defense is yours. The seven kinds of judgment in the document are yours. The decision the document supports — and the decision it does not support — are yours.

To telegraph Chapter 12: the spec document for the causal AI tool is the formal version of this defense, encoded in a structure the tool can read. Every part of the defense becomes a section of the spec. Part 1 becomes the DAG declaration. Part 2 becomes the "do-not-add" list. Part 3 becomes the unmeasured-confounder inputs to the sensitivity analysis. The plain-language register does not feed the tool — it feeds the decision-maker. Chapter 12 will show how the defense translates into spec, line by line.

Chapter 11 is also the chapter where the "skeptical reviewer" role for the final project's Week 15 presentation gets planted. In the final project, you will present your own domain DAG, defend it in both registers, and answer questions from a reviewer assigned to find the weakest part of your model. The reviewer is not adversarial in the personal sense; they are doing what Priya did in the opening scene. The defense you build for the DAG Draft Checkpoint this week is the document you will refine for that presentation. Treat the checkpoint accordingly.

---

## 8. Worked example — A pricing-effect defense, end to end

To consolidate, let me run a complete three-part defense plus plain-language register on an unnamed pricing scenario. I will keep the domain generic — a mid-sized e-commerce company changing a pricing rule on a subset of categories — so the structure of the defense is what reads, not the specifics.

**Treatment:** Whether a category was placed on the new dynamic-pricing rule (binary, category-level).
**Outcome:** Weekly category revenue, in dollars.
**Estimand:** Total effect of the pricing rule on revenue.
**DAG:** Six nodes — `pricing_rule` (T), `revenue` (Y), `inventory_state`, `competitor_price`, `marketing_spend`, `category_seasonality`.

The arrows: `inventory_state → T`, `inventory_state → Y`, `competitor_price → T`, `competitor_price → Y`, `marketing_spend → Y`, `category_seasonality → T`, `category_seasonality → Y`, `T → Y`.

### Part 1 — Arrows as claims

1. **`inventory_state → T`.** Inventory state causally affects the pricing-rule assignment. Evidence: the assignment was made by the merchandising team and explicitly used inventory state as a selection criterion (categories with sufficient stock were included). Documented in the rollout brief, internal-doc evidence, instrumented.
2. **`inventory_state → Y`.** Inventory state causally affects weekly revenue. Evidence: mechanism — out-of-stock categories cannot sell. Multiple internal weekly retention reports confirm the relationship. Mechanism-plus-internal-data.
3. **`competitor_price → T`.** Competitor prices causally affect the pricing-rule assignment. Evidence: the dynamic-pricing rule reads a third-party competitor-price feed as an input. Instrumented.
4. **`competitor_price → Y`.** Competitor prices causally affect revenue independent of our pricing rule. Evidence: standard demand-curve mechanism plus internal A/B tests of price-comparison features. Mechanism-plus-internal-data.
5. **`marketing_spend → Y`.** Marketing spend causally affects revenue. Evidence: a large internal-marketing-mix-modeling literature; published industry studies (e.g., Nielsen MMM reports — citation `[verify]`). Multiple-observational.
6. **`category_seasonality → T`.** Category-level seasonality causally affects the pricing-rule assignment. Evidence: the merchandising team's selection process explicitly avoided peak-seasonal categories. Internal-documented.
7. **`category_seasonality → Y`.** Category-level seasonality causally affects revenue. Evidence: mechanical — toys sell more in December. Common knowledge plus internal data.
8. **`T → Y`.** The pricing rule causally affects revenue. This is the effect under estimation; the arrow's *existence* is hypothesized, the *magnitude* is what we are computing.

### Part 2 — Missing arrows, ranked least-confident first

1. **`marketing_spend → T`.** I am about 65% confident this absence is right. Argument for the absence: marketing spend is set quarterly by a separate team using a top-down budget, not by the merchandising team that did the pricing-rule rollout. Argument against: there is anecdotal evidence that high-marketing-spend categories were preferentially included in the rollout because the marketing team wanted to "show results." If the arrow exists, my estimate is biased *upward* — the pricing rule is getting credit for spend-driven uplift — by an amount bounded by the marketing team's documented incremental effect on revenue in those categories, roughly 3–5% of weekly revenue. **This is the missing arrow I am most worried about.**
2. **`T → competitor_price`.** About 80% confident this absence is right. Competitor prices are scraped externally and reflect competitor decisions; in principle, if our pricing rule moves enough volume to make competitors react, the arrow could exist. The mechanism would take more than two weeks to operate (competitor-response cycle time in the industry), and the analysis window is two weeks. If the arrow exists, the bias is unclear in direction.
3. **`category_seasonality → competitor_price`.** About 85% confident this absence is right. Competitors face the same seasonality, so their prices may move similarly to ours, but the *direct* effect of seasonality on their pricing decisions is plausibly mediated by their own inventory state, which is not in our DAG. If the arrow exists, it does not affect my adjustment set's path-blocking properties because I am already conditioning on category_seasonality.
4. **`T → marketing_spend`.** About 95% confident this absence is right. Marketing spend was budgeted before the pricing-rule rollout decision; the rollout did not feed back into spend decisions during the analysis window. If the arrow exists, it indicates a budget-process anomaly I would need to investigate separately.

### Part 3 — Unmeasured confounders with bias direction

1. **`category_management_team_attention` (unmeasured).** Some categories receive more attention from their assigned category manager than others. Direction on T: attention-rich categories are more likely to be selected for the rollout (positive). Direction on Y: attention-rich categories have higher revenue independent of the pricing rule (positive). Product: positive × positive = positive bias on the estimate. The naive estimate makes the pricing rule look more positive than it is. Magnitude bound: at most as large as the documented spread in revenue between attention-rich and attention-poor categories in non-rule weeks, roughly 4%.
2. **`upstream_supply_disruption` (unmeasured).** Supply-chain disruptions affecting specific categories during the two-week window. Direction on T: not a factor in selection (rollout was decided pre-window). Direction on Y: disruptions reduce revenue. Direction on T is null, so the bias contribution is zero. *I am including this U not because it biases the estimate but because it inflates the variance of the estimate and the reviewer should know it is an issue. This is a borderline Part 3 case.*

**Adjustment set:** Z = {inventory_state, competitor_price, category_seasonality}. Path-blocking justification: each backdoor path from T to Y through one of these variables is blocked by conditioning on that variable. The two unmeasured Us above are not in any observed backdoor path because they are not measured; their effect on the estimate is what Part 3 quantifies.

**Identification verdict:** Partially identifiable. Conditional on the assumed DAG and the named adjustment set, the effect is identifiable up to the bias contribution from `category_management_team_attention`. The chapter-14 sensitivity analysis will produce the E-value.

**What this analysis can conclude:** The pricing rule's effect on weekly revenue, adjusted for the three observed confounders, with a documented bias bound from the named unmeasured confounder.

**What this analysis cannot conclude:** A clean point estimate independent of the management-attention confounder. A claim about long-run revenue effects (only two weeks observed). A claim about categories outside the rollout selection criteria.

### Plain-language register — one page

> **Subject:** Dynamic-pricing rule rollout — readout for the expansion decision
>
> **The question.** Should we expand the new dynamic-pricing rule from the pilot categories to all eligible categories?
>
> **The finding.** Categories on the new pricing rule produced about 3.4% more weekly revenue than comparable categories not on the rule, after we accounted for inventory, competitor prices, and seasonality — about $X per category per week, depending on category size.
>
> **What we are confident about.** The size of the effect is positive in the categories tested. The three things we accounted for — inventory, competitor prices, and seasonality — are the variables our merchandising and pricing teams use to explain category-level revenue differences.
>
> **What we are not confident about.** The biggest single uncertainty is that the categories selected for the pilot received more attention from their category managers than average, and that attention itself produces revenue lift independent of the pricing rule. Our best estimate is that this could account for up to about 4% of the measured effect — meaning the pricing rule's "real" contribution could be as low as roughly half of what we measured, though we believe it remains positive.
>
> **What would change the picture.** A randomized rollout — randomly assigning the pricing rule to half of eligible categories, holding category-manager attention constant — would resolve the attention question. This would take six to eight weeks. Alternatively, a manager-attention-measurement instrument (the merchandising-engagement score the people-analytics team has piloted) would let us include attention as a measured variable in a follow-up analysis.
>
> **What this supports.** This analysis supports expanding the pricing rule to categories that match the pilot's selection criteria (sufficient inventory, mid-range seasonality), at the budget allocated for the pilot's two-week window. The expansion-decision evidence is strong enough that delaying for the randomized rollout is reasonable only if the cost of being wrong is large.
>
> **What this does not support.** This analysis does not support expansion to categories outside the pilot's selection criteria (peak-seasonal, low-inventory), claims about quarterly or annual revenue impact (we measured two weeks), or pricing-rule changes to the rule itself (only the existing rule was tested). It also does not support a confident attribution of the full 3.4% to the rule itself — the management-attention question reduces the lower-bound estimate to roughly 1.7%.

That is the whole defense. Both registers. Five-and-a-half pages of technical defense; one page of plain-language register. A VP can read the plain-language register in two minutes and act. A methodologist can read the technical register in fifteen minutes and audit. Both audiences get a document calibrated to what they can do.

---

## 9. Chapter summary

A causal model is complete when the analyst can defend it in two registers. The defense has three parts: every arrow stated as a causal claim with named evidence; every plausibly-missing arrow ranked by the analyst's confidence in the absence, least-confident first; every named unmeasured confounder with the direction of the bias it would introduce. Part 1 forces the analyst to convert graphical edges into evidence-tagged sentences; Part 2 surfaces the absences the reviewer is most likely to push on, and ranks them so the visibility is maximal; Part 3 turns vague "unmeasured confounding" into specific named variables with directional bias, ready to feed Chapter 14's sensitivity analysis.

The technical register serves methodologists and code reviewers — three to five pages, organized around the DAG and the identification-layer commitments. The plain-language register serves decision-makers — one page, organized around the business question, the finding, the named uncertainty, the decision the analysis supports, and the decision it does not. The two registers are structurally different documents, not vocabulary swaps. Each one carries the full honest acknowledgment of limits; the structure of *how* the limits are surfaced is what differs.

The defense is the place where the book's thesis — that identification requires domain judgment no AI tool currently supplies — becomes literal. The seven kinds of judgment that go into a defense (which arrows, which directions, what counts as evidence, which absences, what prior on each absence, which unmeasured confounders, which decisions the analysis supports) are each, individually, a place a current LLM can produce plausible drafts but cannot stand behind. The analyst owns the defense. The signature is yours.

The two-register discipline is a default, not a law. Some decision-makers want technical defenses; some committees split between the two. Read the audience, then choose. The reproducible template — Part 1, Part 2, Part 3 in the technical register; the five-question structure in the plain-language register — gives you a starting point you can adapt.

---

## 10. Bridge to Chapter 12

The defended DAG is ready for the causal-AI tool. Chapter 12 begins Act Three with the specification document — the formal translation of the three-part defense into a structure the tool can read. Part 1 becomes the DAG declaration in DAGitty or DoWhy syntax. Part 2 becomes the "do-not-add" list — the variables the tool must not include in the adjustment set even if it sees them in the data. Part 3 becomes the input to the sensitivity-analysis pass in Chapter 14. The plain-language register does not feed the tool; it feeds the decision-maker.

The defense you have just learned to build is the artifact that makes the spec writable. The spec is the artifact that makes the tool runnable. Both are upstream of the estimate, and both are entirely yours.

---

## 11. Exercises

The standard exercise set is replaced this week by the DAG Draft Checkpoint (Section 12 below). The exercises here are for practice; the graded artifact is the Checkpoint.

### Warm-up

**Exercise 11.1 — Arrow as a causal claim.** Take the following DAG: `age → blood_pressure`, `age → cardiovascular_event`, `blood_pressure → cardiovascular_event`. (a) State each arrow as a causal claim with evidence source. (b) For the `age → cardiovascular_event` arrow, list the evidence-strength tag (randomized / quasi-experimental / multiple-observational / mechanistic / consensus / candidate) and defend the tag in one sentence.

**Exercise 11.2 — Three missing arrows, ranked.** For the same DAG, name three plausibly-missing arrows. Rank them from "least confident the absence is right" to "most confident." For each, state your prior, the bias direction if you are wrong, and one sentence on the consequence.

### Application — Part A (instructor's domain)

**Exercise 11.3 — Three-part defense for the standard-domain DAG.** Using the pricing-effect DAG from Section 8 (or whatever standard-domain DAG the instructor has assigned for the course): produce the three-part technical defense. Eight arrows-as-claims with evidence sources; four ranked missing arrows; at least two named unmeasured confounders with bias directions. Length: 3–5 pages.

### Application — Part B (your domain — this is the Checkpoint preparation)

**Exercise 11.4 — Three-part defense for your candidate DAG.** Apply the template to your own domain DAG — the one you have been refining since Chapter 3. This is the preparation for the DAG Draft Checkpoint in Section 12.

### Synthesis

**Exercise 11.5 — Plain-language translation.** Take the technical defense you produced in Exercise 11.3 or 11.4. Translate it into the one-page plain-language register, following the five-question structure. Show the document to someone who does not work in your field — a friend, a partner, a non-technical colleague — and ask them what decision they think the analysis supports. If their answer matches your "what this supports" sentence, the translation is doing its job. If not, revise.

### Challenge

**Exercise 11.6 — The defense the authors did not write.** Find a recent published causal claim — a paper, a model card, a policy brief — that uses observational data and reports a causal effect. Write the three-part defense the authors *did not include*. (a) List the arrows you believe the authors are implicitly assuming, and tag each with the evidence source you can find in the paper. (b) List three missing arrows the authors did not address. (c) Name two unmeasured confounders the authors did not name, with bias directions. (d) Write a one-paragraph methodological note suitable for a referee report. The exercise is graded on the honesty and specificity of the reconstruction, not on whether you ultimately agree or disagree with the published claim.

---

## 12. DAG Draft Checkpoint (100 points — replaces standard graded exercises)

The Checkpoint is a single deliverable: the three-part defense plus the plain-language register for *your own* candidate DAG. The DAG has to be a question you actually care about, in a domain you have working knowledge of. The Checkpoint is graded on the defense, not on whether the DAG is "right." A defensibly-articulated wrong DAG scores higher than an unarticulated right one.

**Rubric:**

- **Part 1 — Arrows as claims (40 points).** Every arrow in your DAG has a stated causal claim *and* a named evidence source. The evidence source is in the acceptable hierarchy (randomized, quasi-experimental, multiple-observational, mechanistic, consensus, candidate). Each arrow has a strength tag. Vague evidence ("the variable seemed relevant"; "the LLM suggested it") loses points; honest weak evidence stated plainly does not. *Partial credit for arrows where the evidence is honestly stated as weak.*
- **Part 2 — Missing arrows ranked (20 points).** At least three missing arrows named. Ranked from least-confident-absence to most-confident-absence. Each has (a) the absence as a claim, (b) a calibrated prior on the absence, (c) the consequence if wrong (bias direction, magnitude bound, identification threat).
- **Part 3 — Unmeasured confounders with bias direction (20 points).** At least two named unmeasured confounders. Each has the variable identity, direction on T, direction on Y, bias direction on the estimate, and a defensible magnitude bound. Bias direction stated as "the naive estimate is biased upward / downward by an amount bounded by ___."
- **Plain-language register (20 points).** One page. Answers the five questions in order. Carries the full uncertainty content from the technical defense. Includes the explicit "what this supports / what this does not support" pair. Readable by someone who does not know what a DAG is.

**Submission:** A single PDF or markdown document with both registers. The technical register first, the plain-language register second. Total length: 4–6 pages.

**Office hours focus this week:** Bring the defense in draft form. The TA team will read Part 2 of your draft and ask "which missing arrow are you least confident about, and what would change if you were wrong?" That conversation is the same conversation Priya had with the analyst in the opening of this chapter. The Checkpoint is preparing you to have that conversation cleanly.

The Part B investment from earlier chapters — the candidate DAG you have been refining — pays out here. There is no Part B bonus this week. The bonus has been paid into the final project, where the defended DAG becomes the spec input for Chapter 12 and the basis of the Week 15 presentation.

---

## 13. LLM exercise

The exercise: have an LLM draft a three-part defense for a small DAG, then critique the draft and find every place the LLM produced plausible-sounding text that does not actually defend the claim.

**Prompt to paste into Claude, ChatGPT, or Gemini:**

> I have a directed acyclic graph for an A/B test of a new email-notification frequency on user retention. The variables are:
> - T: assignment to the new notification frequency (binary, randomized)
> - Y: 14-day retention (binary)
> - prior_engagement: user engagement in the 14 days before the experiment
> - cohort_age: days since signup
> - email_subscription_status: whether the user has subscribed to marketing emails
>
> The arrows in my DAG are:
> - prior_engagement → T
> - prior_engagement → Y
> - cohort_age → prior_engagement
> - cohort_age → Y
> - email_subscription_status → T
> - email_subscription_status → Y
> - T → Y
>
> Produce a three-part defense:
> 1. Every arrow stated as a causal claim with a named evidence source.
> 2. The four most plausible missing arrows, ranked from least-confident-absence to most-confident-absence, each with a prior on the absence and the bias direction if wrong.
> 3. Two unmeasured confounders with bias directions on the estimated effect.
>
> Then translate the defense into a one-page plain-language register for a VP who will decide whether to roll out the new notification frequency to all users.

After the LLM responds:

1. **Read Part 1 critically.** For each arrow, ask: did the LLM cite a specific source you can verify, or did it produce a generic "industry literature supports this" claim? How many arrows have specific citations? How many have vague gestures? Mark each.
2. **Find an evidence-source the LLM invented.** Most LLMs will cite a study or a textbook that does not exist, or attribute a finding to a real author who did not make it. Find at least one such instance. (If you cannot find one, you have either gotten a careful LLM or you have not pushed hard enough — try the same prompt on a different model.)
3. **Read Part 2 critically.** For each missing arrow, ask: is the LLM's prior on the absence calibrated to the *actual mechanism*, or is it pattern-matching to "standard A/B test concerns"? Find one missing arrow where the LLM's reasoning would be wrong for your real-world version of this DAG.
4. **Read Part 3 critically.** For each unmeasured confounder, ask: would this variable actually be unmeasured at a company running this experiment? Sometimes the LLM names a variable that is *standardly measured* in industry practice (like `time_zone`), which means the entry is wrong — the variable is measured and would go in the adjustment set, not in Part 3.
5. **Read the plain-language register critically.** Does it answer the five questions in order? Does the "what this does not support" sentence name something the analysis genuinely cannot support, or is it generic ("this analysis does not support claims about long-term effects")? Generic does-not-support sentences are the most common failure of LLM-drafted plain-language registers.
6. **Write a one-paragraph note** describing where the LLM's draft was useful as a starting point, where it produced plausible-sounding-but-undefendable text, and what an analyst would have to add or replace to make the document a real defense. Submit the note as your exercise deliverable.

**What to expect.** Current models (Claude 3.5 / 4 family, GPT-4 / 5 family, Gemini 1.5 / 2 family) can produce defenses that *look* like a real defense — right structure, right vocabulary, right rhythm. They invent citations roughly 20–40% of the time on specific-source claims. They produce confident priors on absences without the domain knowledge to defend the prior. They name unmeasured confounders that are, in fact, standardly measured in industry. The plain-language register often reads well but defaults to generic "supports / does not support" framings.

The teaching point — the chapter's hard line — is that this is exactly the failure mode the chapter exists to prevent. The LLM can scaffold the defense. The analyst owns the defense. The signature is yours, the citations are yours to verify, the priors are yours to calibrate, the unmeasured confounders are yours to name from your actual data pipeline, and the does-not-support sentence is yours to write from your actual knowledge of which adjacent decisions the analysis cannot underwrite.

---

## 14. AI Use Disclosure

This chapter was drafted with the assistance of Claude (Anthropic), using the Feynman-voice pedagogical scaffold defined in the workshop's CLAUDE.md and the chapter-specific pantry notes prepared for Chapter 11 of *Causal Reasoning: Irreducibly Human*. Every primary source cited was checked against its original venue where verification was possible; citations flagged `[verify]` are pending Nik's review. The Priya code-review scene in Section 1 is a stylized composite of common engineering code-review dynamics, not a transcript of a specific real review. The worked examples — the recommendation A/B test in Sections 3, 4, 5; the pricing-effect rollout in Section 8 — are illustrative scenarios constructed to exercise the three-part-defense discipline. No specific company, team, or individual is identified.

The LLM exercise in Section 13 is designed to be run by the student against current chatbot models. The author has run it against Claude (version family 4) and has confirmed the failure modes described — invented citations, generic does-not-support framings, plausible-but-undefendable confidence on absences. The exercise's teaching point is robust across the models I tested as of the chapter's drafting.

---

## 15. Key terms

- **Three-part defense.** The structural artifact that completes a causal model: arrows-as-claims, missing-arrows-ranked, unmeasured-confounders-with-bias-direction. The defense is the proof that the identification layer was performed. (Section 2.)
- **Arrow as a causal claim.** A directed edge in a DAG, converted into two sentences: the structural commitment (under intervention on the source, the target would change in expectation) and the epistemic commitment (the named evidence source supporting the claim). (Section 3.)
- **Evidence-source hierarchy.** The ranked acceptable bases for an arrow's causal claim: randomized, quasi-experimental, multiple-observational, mechanistic, consensus, tool candidate. Strong-to-weak. (Section 3.)
- **Missing-arrow ranking.** Ordering the absences in your DAG from least-confident to most-confident, so the reviewer sees the weakest claim first. The strongest defense surfaces its own limits before the reviewer asks. (Section 4.)
- **Unmeasured confounder with bias direction.** A named variable that is not in your data but plausibly affects both treatment and outcome, with the qualitative direction (positive, negative) of the bias it introduces into the naive estimate. The input to Chapter 14's sensitivity analysis. (Section 2, Section 8.)
- **Technical register.** The 3–5-page defense document for methodologists and code reviewers, organized around the DAG and the three parts. (Section 5.)
- **Plain-language register.** The one-page defense document for decision-makers, organized around the five questions and ending with the explicit "what this supports / what this does not support" pair. Structurally different from the technical register, not a vocabulary swap. (Section 5.)
- **The five questions.** The plain-language register's structure: (1) the business question, (2) the finding, (3) the warranted confidence, (4) what would change the picture, (5) what the analysis supports and does not support. (Section 5.)
- **Does-not-support sentence.** The plain-language register's hardest sentence — the explicit naming of which adjacent decisions the analysis cannot underwrite. The most domain-judgment-intensive sentence in the entire defense. (Section 5.)

---

## 16. Further reading

- Judea Pearl, *Causality: Models, Reasoning, and Inference*, 2nd edition (Cambridge University Press, 2009), Chapter 3. The graphical content of a DAG, including the d-separation logic that makes missing arrows testable claims.
- Judea Pearl and Dana Mackenzie, *The Book of Why* (Basic Books, 2018), Chapters 9–10. The defense-in-prose tradition; the canonical informal version of the discipline this chapter formalizes.
- Miguel A. Hernán and James M. Robins, *Causal Inference: What If* (Chapman and Hall/CRC, 2020), Chapters 7–8. The structural-defense tradition in epidemiology. Freely available at https://miguelhernan.org/whatifbook.
- Miguel A. Hernán, "The C-Word: Scientific Euphemisms Do Not Improve Causal Inference From Observational Data," *American Journal of Public Health* 108(5) (2018), 616–619. [DOI: 10.2105/AJPH.2018.304337](https://doi.org/10.2105/AJPH.2018.304337). The argument that hedged language hides causal claims; directly applicable to the plain-language register.
- Johannes Textor, Benito van der Zander, Mark K. Gilthorpe, Maciej Liśkiewicz, and George T. H. Ellison, "Robust causal inference using directed acyclic graphs: the R package 'dagitty,'" *International Journal of Epidemiology* 45(6) (2016), 1887–1894. [DOI: 10.1093/ije/dyw341](https://doi.org/10.1093/ije/dyw341). The DAGitty paper.
- Ankur Ankan, Inge M. N. Wortel, and Johannes Textor, "Testing Graphical Causal Models Using the R Package `dagitty`," *Current Protocols* 1(2) (2021), e45. [DOI: 10.1002/cpz1.45](https://doi.org/10.1002/cpz1.45). The procedural treatment of using missing-arrows as testable d-separation claims.
- Margaret Mitchell, Simone Wu, Andrew Zaldivar, Parker Barnes, Lucy Vasserman, Ben Hutchinson, Elena Spitzer, Inioluwa Deborah Raji, and Timnit Gebru, "Model Cards for Model Reporting," FAccT 2019. [DOI: 10.1145/3287560.3287596](https://doi.org/10.1145/3287560.3287596). The model-card discipline; engineering analogue of the structural defense.
- Tyler J. VanderWeele and Peng Ding, "Sensitivity Analysis in Observational Research: Introducing the E-Value," *Annals of Internal Medicine* 167(4) (2017), 268–274. [DOI: 10.7326/M16-2607](https://doi.org/10.7326/M16-2607). The quantitative companion to Part 3 of the defense, arriving in Chapter 14.
- David Spiegelhalter, *The Art of Statistics: How to Learn from Data* (Pelican / Basic Books, 2019). The principled-uncertainty-communication tradition informing the plain-language register.
- Ron Kohavi, Diane Tang, and Ya Xu, *Trustworthy Online Controlled Experiments* (Cambridge University Press, 2020). Engineering-native source on defending experimental analyses to product stakeholders.

---

## 17. Draft flags

The following items in this chapter were flagged for verification during drafting and remain pending Nik's review:

- Sgaier, S. K., Huang, V., & Charles, G. (2020), "Translating Causal Inference into Decision-Maker Action," *NPJ Digital Medicine* — exact volume/issue/article-number `[verify]`. URL inferred but not verified.
- Greenland, S., Mansournia, M. A., & Joffe, M. (2022), on compatibility intervals and uncertainty communication — exact paper `[verify]`. Spiegelhalter 2019 *Pelican* is used as the verifiable plain-language-communication source in its place.
- Frake (2025), *Strategic Management Journal*, on partial identification in strategic management research — referenced in Chapter 10's pantry but not cited in this chapter's body; if the chapter's instructor wants the SMJ tradition cited here for the "stakeholder defense" angle, the exact issue `[verify]`.
- LLM4Causal (arXiv:2312.17122) — referenced in the chapter-11 pantry notes; not cited in the body, since the chapter's "LLM as scaffold, analyst as defender" argument is made on first-principles grounds rather than literature grounds. Could be added to Further Reading if Nik prefers.
- Nielsen marketing-mix-modeling industry reports referenced in Section 8 Worked Example, arrow 5 evidence source — `[verify]` whether a specific cited Nielsen report should replace the generic industry reference.
- The Priya code-review scene in Section 1 is a stylized composite, not a real transcript. Flagged for the author's confirmation that the composite is acceptable.
- The pricing-effect Worked Example in Section 8 uses unnamed mid-sized-e-commerce framing consistent with Chapter 10's "Team Pricing" composite. No specific company is named.

---

## What would change my mind

If the engineering field develops an LLM-driven defense-authoring tool that can *reliably* produce the seven kinds of judgment listed in Section 7 — with verified citations, domain-calibrated priors on absences, correctly-named unmeasured confounders for the specific data pipeline in question, and a does-not-support sentence that correctly identifies the adjacent decisions the analysis cannot underwrite — then the chapter's framing of the defense as irreducibly human would need revision. The current evidence does not support that revision; the LLM produces plausible-sounding scaffolds whose underlying claims do not yet bind to a specific business reality. If that changes, the book's thesis changes with it. I would update.

## Still puzzling

I do not yet have a clean account of when the two-register discipline should collapse into a single document — for audiences that genuinely span both registers (committees with technical and non-technical members), the two-document structure can over-formalize the communication. The hybrid register I have seen work — a one-page plain-language summary on the front, the technical defense as an appendix in the same document — looks right to me in practice, but I have not yet developed a clean rule for when to use it versus the strict two-document version.

---

**Tags:** dag-defense, two-register-communication, missing-arrows, unmeasured-confounders, identification-layer
