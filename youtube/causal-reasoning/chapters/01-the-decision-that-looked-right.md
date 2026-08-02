# The Decision That Looked Right


## TL;DR

- TL;DR: A prediction model can be right about a pattern in the world and wrong about a decision in the world, and the difference is not engineering polish — it is a mathematical fact about which question the data was actually asked.
- The chapter moves through The question switches under your feet, Checkpoint — three questions, no grade, The ladder — three kinds of question, not three grades of answer, Why prediction tools fail at strategy, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

**Suggested titles:**
1. The Decision That Looked Right
2. Accurate, And Wrong: What Pneumonia Teaches About Prediction
3. Why Your 94% Model Will Get Someone Hurt

**TL;DR:** A prediction model can be right about a pattern in the world and wrong about a decision in the world, and the difference is not engineering polish — it is a mathematical fact about which question the data was actually asked. This chapter shows you the fact through one real case, then hands you Pearl's Ladder as the tool you will use for the rest of the book to tell which question you are answering before you answer it.

**Byline:** Nik Bear Brown

**Prerequisites:**
- Comfort with conditional probability — you can read `P(Y | X)` and say in plain English what it asks the data for.
- Regression intuition — you can interpret a coefficient as "the effect of X on Y holding other things fixed," and you have at least once felt suspicious about what "holding fixed" actually means.
- Familiarity with the slogan "correlation is not causation." Not as a slogan — as something you have already seen go wrong in code.
- Used at least one causal inference library (DoWhy, EconML, CausalImpact, a propensity-score package) on a project, even briefly.
- Heard of Pearl's *Book of Why*, even if you have not finished it.

**Learning objectives:**
- **(Understand)** Describe the difference between a statistical association and a causal claim using a domain example you can name, draw, and defend.
- **(Apply / Part B)** Classify a claim from your own field as causal or correlational and write the one-sentence justification you would put in a code review.

---

In the mid-2010s, a group at Microsoft Research, Carnegie Mellon, and Columbia trained a model on hospital records to predict which pneumonia patients were at high risk of dying. The model worked. By the standard scoreboard — area under the ROC curve, held-out validation, the whole apparatus — it was state of the art for the task. The team that built it was not careless. The data was real. The labels were real. The math was correct.

The model learned, among other things, that pneumonia patients with a history of **asthma had lower mortality risk** than pneumonia patients without asthma. It learned this confidently and consistently across model classes — neural nets, rule learners, generalized additive models. The pattern was in the data. It was real. And if anyone had deployed the model to triage admissions — to decide which pneumonia patients to send home and which to keep — the asthmatic patients would have been ranked low-risk. Some of them would have been sent home. Some of them would have died.

I want you to sit with that for a second. The model was not buggy. The data was not poisoned. The training set was a faithful record of what happened in the hospital. The model fit the data correctly and produced a number that, on the test set, tracked the truth. And it would have killed people.

The team caught it because they were using an *intelligible* model — a generalized additive model whose terms a clinician could look at directly — and the clinicians, looking at the asthma term, said: *that cannot possibly be right.* Asthma is a known risk factor for severe pneumonia. The team [traced it back](https://www.microsoft.com/en-us/research/publication/intelligible-models-healthcare-predicting-pneumonia-risk-hospital-30-day-readmission/) and found the answer. Hospitals admitting a pneumonia patient with a documented asthma history sent that patient straight to the intensive care unit. The aggressive treatment lowered their mortality below the baseline. The data recorded the outcome — lower mortality — and labeled it with the input — asthma. The model learned: *asthma reduces pneumonia mortality.* What the data was actually telling it was: *we treat asthmatic pneumonia patients very aggressively, and the treatment works.* The pattern was real. The decision the pattern implied was inverted. ([Caruana et al., 2015](https://dl.acm.org/doi/10.1145/2783258.2788613))

That is the case I want you to carry through this chapter — and through the rest of the book.

Now, the part most engineering write-ups stop at is: "this is why interpretability matters." That is true, and it is not the lesson I am after. The deeper lesson is that the model and the decision were asking *different mathematical questions*, and no amount of additional data of the same kind would have made the model right for the second question. More patient records would have sharpened the estimate of a quantity the deployment did not actually need. The team did not have a data problem. They had a question problem. And the question problem was invisible until someone looked.

This book is about seeing the question problem before it ships.

## The question switches under your feet

Let me show you why the question changed.

The model estimated something. What did it estimate? In the language of probability — and this is one of those moments where the notation is doing real work, so let me write it out — the model estimated `P(mortality | asthma, other features)`. *Probability of mortality, given that I observed asthma in this patient's record, given the other features.* The vertical bar is the load-bearing piece. It says: *condition on what you saw.* The model is a calculator for the question "among patients who looked like this in the records, what fraction died?"

That is a perfectly well-defined question. The model answered it well. The data could settle it.

Now the deployment. The hospital wants to use the score to make a decision: which patients to admit, which to send home. The score is high — keep. The score is low — discharge to outpatient care. The question the hospital is asking is *not* "among patients who looked like this in the past, what fraction died?" The question the hospital is asking is "if I send this patient home, what is the probability they die?"

Watch what happens when you write that out: `P(mortality | send home, asthma, other features)`. That looks like the same thing — another bar, another conditioning. It is not the same thing. The first expression is conditioned on a *thing the analyst observed*. The second is conditioned on a *thing the analyst is about to do*. In the training data, no one was sent home with an asthmatic pneumonia presentation, because the policy was: aggressive admission. The data does not contain the rows where the new policy is in effect. The model never saw them. The model cannot produce them.

We need a piece of notation for this — one piece, and you have probably already met it. Pearl writes the *intervention* version with a `do` operator. `P(Y | do(X = x))` means: *probability of Y in a world where I intervened and set X to the value x*. It is not a Python function. It is not a SQL operator. It is a label the analyst attaches to a question to mark *which kind of question it is*. The training data — any training data, however large — is conditioned on whatever policy generated it. The do-question asks about a policy that may not be in the data at all. ([Pearl, 1995, *Biometrika*](https://doi.org/10.1093/biomet/82.4.669))

Here is the cleanest way I have found to feel the difference. Picture two SQL queries side by side. The first is `SELECT mortality FROM patients WHERE asthma = 1`. That is `P(mortality | asthma)`. It says: *show me the rows where asthma happened to be present, and tell me the mortality rate among them.* The second query is the one that does not compile. It would have to read something like: *go back in time, find the patients who had asthma, force the hospital to send them home instead of to the ICU, run the world forward, come back, and tell me the mortality rate.* No `WHERE` clause does that. No `JOIN` does that. The data, by construction, cannot contain the answer to the second query. You can only get it from a different operation: an intervention, in the world or in a model that justifies the leap from one to the other.

When the Caruana team's data said `asthma → lower mortality`, the data was answering the first query honestly. The deployment would have read the answer as if it were answering the second query. *That* is the failure. Not bad data. Not bad math. A silent change of question.

Two more things to mark before we move on. First, this is not an artifact of small samples. More records of the same kind — collected under the same hospital policy — produce a sharper, more confident estimate of *the same wrong thing for the new question*. The asthma-lowers-mortality coefficient gets a tighter confidence interval. The decision the coefficient implies gets no less wrong. This is one of the genuinely hard intuitions to install, because most of what your statistics training taught you about sample size assumed you were answering the right question and just needed a better estimate of it.

Second, this is not a "biased data" story in the [Obermeyer 2019](https://www.science.org/doi/10.1126/science.aax2342) sense — where the *labels* were proxies that encoded inequality, and the model faithfully reproduced the encoding. The Caruana data was not biased. The hospital's prior policy was *good policy*. Aggressive ICU admission for asthmatic pneumonia patients saved lives. The data correctly recorded that. The story is not that the records lied. It is that the records correctly answered one question and the deployment was asking another. Worth distinguishing because the two failure modes — biased labels and shifted question — have different fixes, and you will see both in your career.

## Checkpoint — three questions, no grade

Before we name the formal tool, pause. Try these out loud — to a colleague, to yourself, to the air. The point is to surface what is still fuzzy.

1. The Caruana team's model had high test-set accuracy. Why did that not protect the deployment?
2. Suppose the hospital had ten million pneumonia records instead of a hundred thousand, all collected under the same triage policy. Would the deployment have been safe? If your gut says yes, say why. If your gut says no, say why in one sentence.
3. Imagine I write `P(churn | sent_promotion = 1)` in a notebook. A teammate writes `P(churn | do(sent_promotion = 1))`. Are they computing the same thing? If not — in plain English — what is each one asking?

If the third question feels slippery, you are paying attention. That slipperiness is what the rest of the chapter (and arguably the rest of the book) is built to dissolve.

## The ladder — three kinds of question, not three grades of answer

Judea Pearl, in [*The Book of Why*](https://www.basicbooks.com/titles/judea-pearl/the-book-of-why/9780465097609/) and earlier in his technical work, draws a picture of a three-rung ladder. I want to teach it the way it does work, not the way it is sometimes recited.

**Rung 1 — Association.** *What does seeing X tell me about Y?* The mathematical object is `P(Y | X)`. The data settles it directly. Weather forecasts live here. Pneumonia mortality predictions live here. Most of what gets called "machine learning" in practice lives here. A correct Rung 1 model is a correct answer to a Rung 1 question. Nothing about Rung 1 is shameful.

**Rung 2 — Intervention.** *What happens to Y if I do X?* The mathematical object is `P(Y | do(X))`. Randomized controlled trials are the canonical instrument. A/B tests in a product context are Rung 2 for the specific intervention, population, and time window of the test. To get a Rung 2 answer from Rung 1 data, you need additional structure — a model of *what causes what* — that the data alone cannot provide. The structure is what you supply, as the human in the loop, and what the rest of this book teaches you to supply defensibly.

**Rung 3 — Counterfactual.** *Given that X and Y both happened, what would Y have been if X had been different?* The mathematical object is `P(Y_{X = x'} | X = x, Y = y)` — read as "the value Y would have taken in a world where X had been x', given that in this world X was x and Y was y." Legal questions live here. Medical-decision second-guessing lives here. Counterfactuals require still more structure than interventions — they ask about a specific individual in a specific alternate world, not a population average under a new policy.

I will keep coming back to the ladder, so let me name three things that go wrong when people first meet it.

The first thing that goes wrong is reading the rungs as a *quality hierarchy*. People hear "Rung 3 is the top rung" and think Rung 3 is the best kind of answer and Rung 1 is the worst kind of answer. That is wrong. The rungs are *kinds of question*. The weather forecaster who gives you `P(rain tomorrow | today's pressure, today's wind)` and is well-calibrated is doing Rung 1 at a high level. Asking the forecaster `P(rain | do(more umbrellas))` is not a harder version of the same question — it is a malformed question, because in the causal structure of the world there is no edge from umbrellas to rain. The forecaster's job is not to climb to Rung 2. The forecaster's job is to answer Rung 1 well.

The second thing that goes wrong is treating `do(X)` as an operator the software performs. It is not. `do(X)` is a discipline the analyst performs *before* the software runs. You decide, looking at your problem, which question you are asking. You label it. Then you check whether the data — and the assumptions you are willing to defend — can settle it. The do-notation is a sticker you put on a question to make it harder to lie to yourself about what you are computing.

The third thing that goes wrong is the assumption that "we A/B tested it" closes the Rung 2 question for all time. A specific A/B test settles the do-question for the population sampled, the magnitude of the treatment delivered, and the time horizon of the test. Generalizing to a different population, a different magnitude, or a different season requires identification assumptions the test alone does not supply. (Bottou and colleagues at Facebook have a careful paper on this — [counterfactual reasoning for ad placement](https://www.jmlr.org/papers/v14/bottou13a.html) — where the training data is generated by the *old* policy and the question is what happens under a *new* policy, and the importance-weighting needed to bridge them depends on a causal model you have to commit to in writing.)

The ladder is not the answer. It is a navigation tool. It tells you what question your calculation is settling so you can notice when the calculation is settling the wrong one. The first move in every causal analysis is to ask: *which rung is my question on, and which rung does my data, by itself, reach?* If the answer is "different rungs," the rest of the chapters in this book are the bridge.

## Why prediction tools fail at strategy

There is a common shape to ML deployment failures that the ladder makes visible. I am going to call it the Rung 1 / Rung 2 silent swap, and once you see it you will see it in three or four projects you have already shipped.

You build a model to predict an outcome. The outcome is something you eventually want to *change* — churn you want to reduce, fraud you want to catch, readmissions you want to avoid, click-through you want to increase. The model is accurate. The team plans an *intervention* based on the prediction: call the high-churn users, route the high-fraud transactions to review, follow up on the high-readmission patients. The intervention rolls out. The metric does not move in the direction the team expected. Sometimes it moves the other way.

The mechanism is the same every time. The model estimates `P(outcome | features)` on data generated by the *old policy* — the policy in place when the data was collected. The intervention is a *new policy*, by definition, because the team is doing something different than the data records. The question the intervention is asking — `P(outcome | do(new policy), features)` — is not a question the training data can settle. The data does not contain rows from the new policy. The data does not even contain rows that the old policy could not produce. The model is computing a sharp estimate of an irrelevant quantity, and the deployment is reading the estimate as if it answered the policy question, and the policy question is on a rung the data cannot reach.

I have watched this kill projects across very different domains. Consider three.

A fraud-detection team trains on labeled historical transactions and ships a 99% accuracy model. The model blocks the transactions it predicts are fraud. The blocked transactions never produce a labeled outcome — they are blocked, so there is no "actually fraud / actually not" ground truth on them. The next training cycle pulls a fresh dataset that is missing exactly the kinds of transactions the previous model blocked. The model degrades. The team retrains. The new model is sharper on the data it sees and blinder to the data it does not. The do-operator — block or do not block — modifies the data-generating process. ([Lakkaraju et al., 2017, on the "selective labels" problem](https://dl.acm.org/doi/10.1145/3097983.3098066), which is the same shape.)

A recommender team trains on logged user-item engagement under the current recommendation policy and ships a new ranking model that lifts predicted engagement. They A/B test. Predicted engagement and observed engagement diverge. The training distribution was conditioned on what the *old* recommender chose to show. The new model is being asked `P(engagement | do(show item to user))` and was trained on `P(engagement | observed-shown(item, user))`. They are the same expression only when the old recommender showed items in a way uncorrelated with the engagement signal — which it never does, because that would defeat the purpose of having a recommender. Bottou et al. work through the math for this exact case.

A healthcare-AI vendor ships a readmission predictor with 94% accuracy on historical data. The hospital uses the scores to prioritize follow-up calls. Readmission rates go up, not down. The model was right about *who* would readmit under the no-call policy. The intervention — calls plus protocol changes — is a new policy the model has no information about. The team thinks they have a model accuracy problem. They have a question problem. (The pattern is documented across several deployment-failure write-ups; the canonical Caruana paper is the load-bearing one. The contemporary echoes are everywhere, but vendor blogs are not load-bearing primary sources, so I am naming the structure, not picking a specific 2024 incident as canon. [verify: a peer-reviewed 2024–2026 readmission deployment post-mortem with this structure])

There is a sentence that floats around the ML-pedagogy world and I think it is exactly right: *using a prediction model to set policy is like using a thermometer to set the thermostat*. The thermometer reads temperature. The thermostat changes temperature. The temperature reading does not tell you what action will change the temperature, even if the temperature reading is perfectly accurate. The analogy has limits — a real thermostat is a one-knob system and real policies touch many variables — but it does its job: a measurement of the world and a lever on the world are different objects. ([The framing is folkloric in causal-ML pedagogy; I do not have a single load-bearing source for it and I would not lean on it harder than this paragraph does.])

I should pause to name one place this framework itself is contested, because the method applies to the method. There is a long-running argument over whether reinforcement-learning agents — which act on the world and observe consequences — should be described as "operating on Rung 2" or "still doing Rung 1, but on action-conditioned data." Pearl and Mackenzie put modern deep learning on Rung 1; Bareinboim and others argue this misreads what RL agents are doing structurally. I do not need to adjudicate the dispute here, and I will not try. What I will commit to is that the dispute does not affect the chapter's claim — that prediction models trained on observational data, used to set policy, are doing the Rung 1 / Rung 2 swap whether or not RL agents are. Hold the dispute lightly. The book returns to it in Act Two when it is load-bearing. ([Pearl & Mackenzie, 2018](https://www.basicbooks.com/titles/judea-pearl/the-book-of-why/9780465097609/); [Bareinboim et al., 2022](https://ftp.cs.ucla.edu/pub/stat_ser/r60.pdf).)

## Bringing it back — what the Caruana team actually did

Now reread the pneumonia story with the ladder in your hand.

The model estimated `P(mortality | asthma, other features)` on data collected under the policy *"asthmatic pneumonia patients get aggressive ICU admission."* That is a Rung 1 calculation. The data could settle it. The model settled it correctly. The number — asthma reduces mortality — is the right answer to the Rung 1 question. The number is wrong as an answer to any Rung 1 question if you remove the policy context, but inside the policy context the data was collected under, it is right.

The deployment would have asked `P(mortality | do(triage to outpatient), asthma, other features)`. That is a Rung 2 calculation. It is asking about a world in which the triage policy changes. The data — *any* data collected under the old policy — does not contain that world. The training set could be the size of every hospital record in North America and the answer would not be in it.

Here is the move the Caruana team made, and it is the move I want you to internalize. They did not throw the model away. They did not declare the data corrupt. They named the gap. They said: *this number is a faithful Rung 1 estimate; the deployment requires a Rung 2 answer; therefore this model, as it stands, cannot be deployed for triage without additional structure we are not yet willing to commit to.* In the paper, they speak of "patterns ... that previously had prevented complex learned models from being fielded in this domain." That is not a polite way of saying the model was bad. That is an honest way of saying the question was bigger than the model.

The mechanism of the rescue is what I want you to carry. Once the team saw that the asthma term encoded a *policy*, they could ask: what would it take to estimate the Rung 2 quantity? It would take either a randomized trial of triage strategies (ethically not on the table), or an observational study with an explicit causal model — *asthma causes ICU admission, ICU admission causes lower mortality, asthma itself causes higher pneumonia severity* — and an analysis that adjusts for the right variables and avoids the wrong ones. The chapters from here to Week 11 of this course are about which variables are the right ones, which are the wrong ones, and why "control for everything" — which is what a careless ML reflex would do — gets parts of the answer exactly backwards. The Caruana case is the first case in a fifteen-week arc that ends with you able to do this yourself, on your own data, with your own defensible model of the causal structure.

For now, the capability I want you to leave the chapter with is the diagnosis. Given a deployment and its data, can you state which rung the data reaches, which rung the decision requires, and whether the gap is bridged? If yes, defend the bridge. If no, name the missing structure. That is the move.

## Worked example — a churn model in a code review

Let me walk you through a smaller version of the same diagnosis, on a setup you have probably already encountered.

You are in a code review. A teammate has built a churn model. The model takes a user's recent activity, plan tier, support-ticket history, and a few engagement signals, and outputs a probability that the user churns next quarter. The model is good. On a held-out cohort it discriminates churners from non-churners with an AUC of 0.81. The team plans to deploy it as a *retention* model: the customer-success team will reach out to the top 5% predicted churners with a discount offer.

The PR description says, in part: *"This will reduce churn in the high-risk segment."*

Stop the review. Ask the question. *Which rung is that claim on?*

The claim "this will reduce churn in the high-risk segment" is a Rung 2 claim. It is a claim about what happens to churn *under the intervention* of reaching out with a discount. Write it: `P(churn | do(outreach), high_risk)` and compare it to `P(churn | high_risk)`. The model estimates the second. The deployment requires the first.

Now ask the diagnostic question: *can the data, as collected, settle the first?* The training data was generated under the previous policy — which is some mix of "no outreach, organic churn" and whatever ad-hoc retention the team was already doing. None of the rows are labeled with "outreach happened." Some users may have received outreach for unrelated reasons, but the policy was not randomized, and whatever drove the existing outreach is correlated with whatever drove churn. The data alone — no matter how much of it there is — does not produce `P(churn | do(outreach), high_risk)`.

What would? Either an A/B test where outreach is randomly assigned within the high-risk segment — which would directly estimate the do-quantity for that segment, that magnitude of offer, that time horizon — or an observational analysis with an explicit causal model that justifies adjusting for the variables that confound outreach and churn. The first is cleaner. The second is what you will spend the rest of this course learning to do when the first is not available.

Here is what you put in the code review:

> *The model is a well-calibrated Rung 1 predictor — it answers "who will churn next quarter under the current policy" with AUC 0.81 on held-out data. The PR description claims the deployment will reduce churn in the high-risk segment. That is a Rung 2 claim about `P(churn | do(outreach))`, which the training data cannot settle by itself. Two options: (1) phase the rollout as a randomized A/B within the high-risk segment, so we directly estimate the intervention effect on this population, magnitude of offer, and quarter; (2) commit to an explicit causal model of outreach, churn, and their common causes, and use it to derive an adjustment set we can defend. I would block on (1) for the initial rollout and revisit (2) for later generalization.*

That is a Rung 1 / Rung 2 diagnosis in five sentences. Notice what is and is not in it. It does not say the model is bad. It does not say the engineer is wrong. It does not appeal to authority or to the slogan "correlation is not causation." It states which mathematical object the model is computing, which mathematical object the deployment needs, and what would bridge the gap. That is the defense you want to be able to write by the end of this chapter. The rest of the course makes the defenses progressively heavier — DAGs, adjustment sets, sensitivity analyses, two-register conclusions. The shape of the move is the same as the one you just made.

## What you can do now

A short list, capabilities not topics.

You can read a model description and a deployment description and identify which rung each lives on. You can write `P(Y | X)` and `P(Y | do(X))` in a way that distinguishes them and explains the distinction to someone who has not yet seen it. You can recognize the Rung 1 / Rung 2 silent swap as a class of failure independent of model quality, data quality, or sample size. You can name the Caruana case — pneumonia, asthma, ICU triage policy — as the canonical instance and use it as a touchstone when a teammate confuses prediction accuracy with decision correctness. You can write a five-sentence code-review block that diagnoses a rung mismatch without sliding into "correlation is not causation" sloganeering. You cannot yet *fix* the mismatch in the general case — that is the rest of the book. But you can see it. Seeing it is most of the work.

## Bridge to next week

Three different fields have three different words for the operation you just performed when you mentally adjusted for the hospital's admission policy. Statisticians call it conditioning. Epidemiologists call it confounding. ML engineers call it controlling-for. The words are not synonyms. Each one carries a commitment about what the analyst knows. Which commitments? And which one is each of these words quietly making for you when you write it?

---

## Exercises

**Warm-up:**

1. **Two queries.** Write out, in plain English, the difference between `P(promotion_response | recent_purchases)` and `P(promotion_response | do(send_promotion), recent_purchases)`. One paragraph. Then say which one a SQL `WHERE` clause can compute on historical data.

2. **Classify the claim.** For each of the following claims, label it Rung 1 / Rung 2 / Rung 3 and give one sentence of justification.

   a. "Users who clicked the upgrade banner have 3.2× higher conversion."
   b. "Showing the upgrade banner increases conversion by 12%."
   c. "If we had shown the banner to user 8472 last week, they would have converted."
   d. "The model predicts a 0.7 probability of churn for this user."
   e. "Calling churn-risk users reduces 90-day churn by 18%."
   f. "Patients with elevated CRP have higher mortality."

**Application (Part A — instructor's standard domain):**

3. **Recommender deployment.** A team has a recommender that, on historical engagement data, predicts click-through rate (CTR) per (user, item) pair. They want to ship a new ranking model and claim it will lift CTR by 4%. Write the do-question their deployment is actually asking. State whether the training data can answer it. Propose one experimental design and one observational design that would let the team defend the claim, and name one identification commitment each design requires the team to make.

**Application (Part B — your own domain):**

4. **Your code review.** Pick a real claim from your current or most recent work — a paper, a project, a slide, a Jira ticket, anything you have written or read in the last six months that uses a model output to make a decision. Write:
   - The claim, verbatim.
   - The rung the claim sits on (Rung 1 / Rung 2 / Rung 3).
   - The rung the data behind the claim reaches.
   - One sentence on what would close the gap.

   The point is not to find a "wrong" claim. It is to practice the diagnosis on a claim that is yours, in vocabulary that is yours.

**Synthesis:**

5. **The book's thesis, in advance.** This book argues that the identification layer of causal analysis — variable selection, edge orientation, conditioning decisions — requires domain judgment no causal AI tool can supply. Using the Caruana case as a single example, write one paragraph (≤150 words) defending or pushing back on that thesis. The Caruana team caught the asthma problem because a clinician recognized the term. Could a sufficiently capable tool have caught it instead? Use evidence from this chapter — not "I think" — to support your answer.

**Challenge:**

6. **Find your own case.** Find a public, named, dated ML deployment failure with substantial post-mortem documentation (peer-reviewed paper preferred, but a serious public write-up — Anthropic safety case, a transparency report, an audit — is acceptable). Trace the failure to a specific rung mismatch. Cite your source. Word count is whatever it takes. The hard part is finding a case with enough provenance to defend; that is the exercise.

---

## LLM exercise

You will use a frontier LLM (Claude, ChatGPT, or Gemini) to test whether the tool can perform the diagnosis you just learned to perform. Paste the following prompt verbatim. Do not paraphrase. Do not warm up the model first. Read the output critically.

```
I am studying causal inference. I want you to play the role of a careful code reviewer.

A teammate has built a churn-prediction model. Trained on logged customer 
data from the last 18 months, AUC 0.81 on a held-out cohort. The model uses 
plan tier, login frequency, support tickets, and feature usage. The team's 
PR description says: "We will deploy this to identify high-risk users and 
reach out to them with a discount, reducing churn in the high-risk segment 
by an estimated 15%."

Please do four things, in order, with no preamble:

(1) Identify the mathematical object the model estimates. Write it in 
P(Y | X) notation.

(2) Identify the mathematical object the deployment claim assumes. Write 
it in P(Y | do(X), ...) notation if applicable.

(3) State whether the training data, as described, can settle the 
deployment claim. Justify in two sentences.

(4) Propose one experimental design and one observational design that 
would let the team defend the deployment claim, and name one identification 
commitment each design requires.

Use Pearl's ladder of causation explicitly. Do not hedge. If the answer is 
"the data cannot settle this," say so and explain why.
```

**What the artifact should look like:** Four numbered responses. The first two should be probability expressions. The third should commit to "yes the data settles it" or "no the data does not settle it," with the no answer named explicitly when the rung-1 / rung-2 swap is in play. The fourth should propose a randomized design (likely an A/B test or RCT) and an observational design (likely a regression / matching / propensity-score / DoWhy-style adjustment).

**How to assess it:** Compare the LLM's response to the diagnosis in the worked-example section of this chapter. Where did the LLM match the book's framing? Where did it omit something a careful reviewer would catch? Where did it add a hedge or boilerplate that the book's framing would cut? Where did it cite something — and is the citation real, or hallucinated? (Check.) Three to five sentences in your write-up.

---

## AI Use Disclosure (Part A standard form)

For any assignment in this course where you used an LLM or other AI tool, submit the standard Part A disclosure form: (1) which tool, (2) for which task in the assignment, (3) what you verified yourself before submitting, and (4) one specific thing the tool got wrong or omitted that you had to fix.

**Part B bonus criterion:** Submissions using your own domain earn 5 bonus points if your AI Use Disclosure names *one specific identification decision in your domain problem that required expertise no LLM or causal AI tool supplied* — and you can defend why. "I'm a domain expert and I just know" does not earn the bonus; "the tool proposed the edge X → Y, but in this domain Y temporally precedes X, which the tool's training data did not contain" does.

---

## Key terms

- **Association** — the Rung 1 question. "Among rows where X is what I observed, what does Y look like?" Computable directly from data. The mathematical object is `P(Y | X)`.
- **Intervention** — the Rung 2 question. "If I act on the world by setting X, what happens to Y?" Not directly computable from observational data alone; requires either an experiment or a causal model that justifies the bridge. Written `P(Y | do(X))`.
- **Counterfactual** — the Rung 3 question. "Given that X and Y actually happened, what would Y have been if X had been different?" Requires more structure than Rung 2 — a specific alternate world for a specific individual.
- **The do-operator** — Pearl's notational sticker that marks a question as an intervention question. Not a Python function. A discipline the analyst applies *before* computing.
- **Identification** — the act of deciding whether (and how) a causal question can be answered from the available data and assumptions. The thing this book is about. The thing tools cannot do for you.
- **Pearl's Ladder of Causation** — three kinds of causal question (association, intervention, counterfactual), introduced as navigation tool. Not a hierarchy of quality; a taxonomy of question.
- **Rung mismatch (informal)** — the failure mode where the data reaches one rung and the decision requires another, and no one notices until the deployment moves a metric the wrong way.
- **Selective labels (related, will return in Week 8)** — the situation where the decision to act on a prediction truncates the future labels you get back. A class of Rung 1 / Rung 2 swap that creates a feedback loop in production ML.

---

## Further reading

- [Caruana, R., Lou, Y., Gehrke, J., Koch, P., Sturm, M., & Elhadad, N. (2015). *Intelligible Models for HealthCare: Predicting Pneumonia Risk and Hospital 30-day Readmission.* KDD '15.](https://dl.acm.org/doi/10.1145/2783258.2788613) — The chapter's load-bearing case. Read for the asthma example and for the GA2M architecture that made the term visible to a clinician.
- [Pearl, J., & Mackenzie, D. (2018). *The Book of Why.* Basic Books.](https://www.basicbooks.com/titles/judea-pearl/the-book-of-why/9780465097609/) — The trade-book introduction to the ladder. Chapters 1–3 are the touchstone. Read for framing; come to Pearl (2009) for the math.
- [Hernán, M. A. (2018). The C-Word: Scientific Euphemisms Do Not Improve Causal Inference From Observational Data. *AJPH* 108(5).](https://doi.org/10.2105/AJPH.2018.304337) — Five-page commentary that does for the word "causal" what this chapter does for the word "prediction." Pair with the Caruana case for a sharper sense of how language hides which rung you are on.
- [Bottou, L. et al. (2013). Counterfactual Reasoning and Learning Systems. *JMLR* 14.](https://www.jmlr.org/papers/v14/bottou13a.html) — The closest thing the ML literature has to a "how Rung 2 actually works in production" reference. Long. Worth working through if recommenders or ad placement is your day job.
- [Bareinboim, E., Correa, J. D., Ibeling, D., & Icard, T. (2022). *On Pearl's Hierarchy and the Foundations of Causal Inference.*](https://ftp.cs.ucla.edu/pub/stat_ser/r60.pdf) — The technical paper behind the ladder. Read for the formal version of the rungs and for the precise sense in which Rung 2 is not reducible to Rung 1.

---

**What would change my mind:** If a peer-reviewed result demonstrated that a current-generation causal AI tool, given only the Caruana training data and no clinical hand-holding, flagged the asthma term as policy-confounded before deployment — for the same structural reason a human clinician did — I would weaken the chapter's claim that catching the failure required domain expertise the tool cannot supply.

**Still puzzling:** I do not have a clean, satisfying account of *why* the Rung 1 / Rung 2 swap is so persistent in production ML even among teams that know the ladder exists. The math is not the hard part. The vigilance is.

---

**Tags:** causal-inference, pearl-ladder, prediction-vs-decision, caruana-2015, ML-deployment-failure, do-operator, identification-layer, intervention, observational-data, code-review

---

## Draft flags

- `[verify]` 2024–2026 readmission deployment post-mortem with full provenance. The chapter does not lean on a specific recent incident as canon; it uses the Caruana case as the load-bearing primary source and describes the contemporary echo at the structural level. If a peer-reviewed 2024–2026 case with the same shape exists, it would strengthen the "this is still happening" claim in the prediction-tools-fail-at-strategy section.
- The "thermometer-thermostat" framing is folkloric in causal-ML pedagogy and I could not run it to a single load-bearing primary source. The paragraph names that fact and treats the analogy as a memory hook, not as evidence.
- Pearl's Rung 1 / RL dispute is named without adjudication, by design. Confirm Bareinboim et al. (2022) is the right citation for "RL agents operate on Rung 2 by construction" — the citation supports the formal hierarchy but the practical dispute is scattered across multiple papers and conference talks, which would be hard to anchor without padding the chapter.
