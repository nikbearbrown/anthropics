# The Identification Layer: What Only You Can Do


## TL;DR

- TL;DR: Three failures show up before the taxonomy that names them — a hospital model that learned the wrong rule, a pricing model that estimated its own beliefs back to itself, a retrieval system that mistook easy...
- The chapter moves through Three things that went wrong before we had names for them, The first failure — wrong variables, Checkpoint — what we have so far, The second failure — wrong arrows, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

> **Draft status:** `voice-unanchored` — no per-book or root `style/` examples exist as of 2026-05-13. Voice calibrated from CLAUDE.md Section 6 and pantry notes; review with voice in mind. This is the MIDTERM chapter; the assessment at the end is the heart of the chapter.

**Suggested titles:**
1. The Identification Layer: What Only You Can Do
2. Three Ways the Data Cannot Save You
3. The Question the Tool Did Not Ask

**TL;DR:** Three failures show up before the taxonomy that names them — a hospital model that learned the wrong rule, a pricing model that estimated its own beliefs back to itself, a retrieval system that mistook easy queries for good retrieval. The identification layer is the set of decisions — which variables, which arrows, which conditioning — that the data alone cannot make for you, and the AI Use Disclosure is how you prove you made them.

**Byline:** Nik Bear Brown

**Prerequisites:**
- Read a directed acyclic graph and tell whether a path is open or blocked given a set of conditioning variables (Chapter 3).
- Distinguish association, intervention, and counterfactual queries — Pearl's three rungs — in plain words (Chapter 2).
- Tell the difference between *what the model predicts* and *what would happen if you acted on the prediction* (Chapter 1, the pneumonia case).
- Write down a candidate DAG for a problem you have actually worked on (homework from Week 3).
- Run a regression or a `DoWhy` / `EconML` estimation and read its output. You do not need to know the internals; you need to know the function signature.

**Learning objectives:**
- **(Apply, Bloom 3)** Given an unseen scenario, draw a candidate DAG and identify which of three identification failures it contains.
- **(Apply, Bloom 3)** Name, specifically, the domain knowledge a dataset cannot supply for that failure.
- **(Analyze, Bloom 4)** Cross-reference your candidate DAG against a competing DAG for the same scenario and decide which one the data does or does not distinguish.
- **(Evaluate, Bloom 5)** Write the AI Use Disclosure for an analysis — track which decisions were yours, which the literature's, which the LLM's, and defend the boundary.

---

## Three things that went wrong before we had names for them

**Case one. Beth Israel Deaconess, around 2012.** A team led by Rich Caruana at Microsoft Research was building a pneumonia-mortality model on data from several hospitals, and one of the rules the model learned was that *patients with asthma had lower mortality from pneumonia*. The model was not buggy. On the data, the rule was correct. Asthma patients in this cohort really did die less often. If you had deployed the model as a triage tool — send the high-risk people to the ICU, send the low-risk people home — you would have sent the asthma patients home. The doctors looked at the rule and said, immediately, *no, this kills people*. The reason it killed people sat outside the model in a way no amount of regularization, more data, or better architecture would fix. ([Caruana et al., KDD 2015](https://dl.acm.org/doi/10.1145/2783258.2788613))

**Case two. A subscription company estimating price elasticity.** The analytics team has five years of monthly transactions. They run a regression of quantity-purchased on price, with controls for season, customer tenure, plan tier. They get an elasticity of −0.4. They report it. A small price experiment three months later returns an elasticity closer to −0.9. The team blames noise. They are wrong. The −0.4 was the answer to a question they did not realize they were asking — *given the prices the firm chose for the reasons the firm chose them, how do purchases vary?* — and the −0.9 was the answer to the question they thought they were asking. The two questions were never the same question. ([Athey & Imbens, *JEP* 2017](https://doi.org/10.1257/jep.31.2.3))

**Case three. A retrieval-augmented chatbot.** Each session logs query, retrieved documents, response, thumbs-up or thumbs-down. The team estimates retrieval quality by regressing thumbs-up on a feature called "retrieval-score." Higher retrieval-score correlates with happier users. The team ships a new retriever that scores higher on the same metric. Satisfaction goes down. Nobody can explain it for a week. Then someone notices that easy queries — short, common, well-served by the index — both produce high retrieval-scores *and* produce satisfied users. The retrieval-score was a proxy for *the query was easy*. The new retriever, optimized to maximize the proxy, found ways to score high on hard queries that did not actually help users. The team had estimated the effect of retrieval quality on satisfaction by conditioning on something the new retriever could game.

Three failures. Three different mechanisms. One thing in common, which we will get to.

If you tell me your first instinct on case one is "they didn't have enough data," I will tell you the data was enormous. Several hospitals. Tens of thousands of admissions. More features than the team could fit in a regression. If you tell me your instinct on case two is "they should have used a better model," I will tell you the team had tried `XGBoost`, a neural network, and a Bayesian hierarchical model. They all gave answers in the same neighborhood. If you tell me case three is a metric design problem, you are closer, but you are still pointing at the wrong layer. The metric design problem *was* the identification problem, and the team did not yet have language to name it.

That language is what this chapter is for. We are going to walk into each failure, take it apart, and at the end name what they share. By the end of the chapter you should be able to look at a fourth case — one we have never discussed — and say which of these three things is happening to it.

---

## The first failure — wrong variables

Let me draw the asthma case on a DAG. Stay with me; the picture is going to be small but important.

There is a thing called *severity*. It is the actual clinical state of the patient at admission — how sick they are, how close to physiological collapse, how reactive their immune system is, how much oxygen they cannot move. Severity does not appear in the dataset as a column. Hospitals do not record "severity = 7.4 on the Bear scale." They record proxies: vitals, labs, comorbidities, treatments started.

Severity drives two things. It drives how the patient is treated — sicker patients get sent to the ICU faster, get antibiotics sooner, get watched more carefully. And it drives the patient's outcome.

Now consider an asthmatic patient with pneumonia. The treating physician sees "asthma" and, knowing asthma puts the patient at risk of respiratory failure, escalates immediately. ICU. Aggressive oxygenation. Faster antibiotics. The asthma flag, in the doctor's hands, is a signal to *treat more*. So an asthmatic pneumonia patient in this cohort gets, on average, the most aggressive care the hospital has.

The treatment, of course, works. That is its job.

So on the data, asthmatic pneumonia patients die less often. The DAG looks like this:

```
   SEVERITY (unmeasured)
     ↙          ↘
ASTHMA-FLAG      OUTCOME
     ↘          ↙
    AGGRESSIVE-CARE
```

The arrow from asthma-flag to aggressive-care exists because doctors react to the flag. The arrow from severity to outcome exists because biology does what biology does. The unmeasured node — severity — is upstream of everything that matters. Strip severity out of the picture, regress outcome on asthma, and you get *asthma protects you*. Put severity back in and you get *asthma is correlated with aggressive care, which protects you*. The first answer is the model's. The second answer is the truth.

Here is the part the engineer needs to feel. You can run the analysis with every feature the hospital records. You can `OneHotEncoder` the labs, embed the medication list, attention-pool the nursing notes. None of it brings severity into your dataset, because severity is not a column. Severity is a *construct* — a thing physicians believe in for reasons that come from biology, not from the rows of the table. The dataset does not contain severity, and no amount of clever feature engineering can recover it from the proxies, because the proxies are downstream of severity rather than equivalent to it.

This is *wrong variables* in its sharpest form. The DAG is missing a node. The node that is missing is one a domain expert can name and a dataset cannot.

Let me name the move. Cinelli, Forney, and Pearl call the analyst's problem here a *bad control* by omission — the analyst failed to adjust for the thing they needed to, because the thing was not in the data. ([Cinelli, Forney & Pearl, "A Crash Course in Good and Bad Controls"](https://ftp.cs.ucla.edu/pub/stat_ser/r493.pdf)) [verify-final-publication-venue-and-year — the working paper is widely circulated; the published version in *Sociological Methods & Research* is reported but I have not confirmed the final volume/issue].

The fix is not algorithmic. The fix is that a clinician walks in, looks at the DAG, points at the empty space upstream of asthma and outcome, and says *severity goes there*. From that moment, the analysis changes shape. Maybe the team builds a severity score from the available proxies and treats it as an instrument; maybe they collect a new variable; maybe they conclude the question is not identified and propose an experiment. None of those moves come from the data. All of them come from a person who knows what severity is.

A small bit of math to make this concrete. Say you have only two variables in your dataset, asthma `A` and outcome `Y`. Severity `S` is unmeasured. The data lets you compute the conditional probability `P(Y | A)`. What you actually want, for any decision, is `P(Y | do(A))` — the probability of the outcome if you intervened to change asthma status, the rung-two query from Chapter 2.

Pearl's backdoor formula tells you that if you could adjust for `S`, you would write:

```
P(Y | do(A)) = Σ_s P(Y | A, S=s) · P(S=s)
```

That sum requires the joint distribution over `S`. You do not have it. You have `P(Y | A)`, which equals:

```
P(Y | A) = Σ_s P(Y | A, S=s) · P(S=s | A)
```

Compare the two lines. The first weights each severity stratum by `P(S=s)` — how common that severity is in the population you would intervene on. The second weights by `P(S=s | A)` — how common that severity is *among the patients who happened to have asthma*. Different weights. Different answers. The asthma cohort is enriched for the kind of patient who gets aggressive care, so `P(S=s | A)` puts mass on severities where outcomes are well-managed. The marginal `P(S=s)` does not.

The fix requires `S`. The dataset does not contain `S`. No statistical procedure invents `S`.

That is the mechanism. Wrong variables means the DAG is missing a node, and the missing node was knowable from outside the data and not from inside it.

---

## Checkpoint — what we have so far

Before we move on, let me pin down what just happened, because the next two failures are going to want to confuse you with it.

The first failure was about *which variables exist*. The analyst's DAG had asthma and outcome and not severity. The data could not tell the analyst that severity belonged on the DAG. Only someone who knew pneumonia could.

If you stopped reading here and never met the other two failures, you would still have a story. "Make sure you have all the variables." It is a useful sentence as far as it goes. It is also, by itself, a trap, because the next two failures happen when you have the right variables and still get it wrong.

---

## The second failure — wrong arrows

Back to the price-elasticity case.

The analyst's DAG, drawn explicitly, looks like this:

```
PRICE → QUANTITY
```

The estimated elasticity is the coefficient on `PRICE` in a regression of `QUANTITY` on `PRICE`. The team gets −0.4.

The DAG that actually generated the data looks like this:

```
DEMAND-EXPECTATION → PRICE
DEMAND-EXPECTATION → QUANTITY
PRICE → QUANTITY
```

Demand-expectation is what the firm's pricing team thought demand would be when they set the price. When they expected weak demand, they cut prices. When they expected strong demand, they held prices firm or raised them. So prices and quantities both move with the firm's beliefs. The regression sees high-quantity months at moderate prices (strong-demand months where prices were held firm and people bought anyway) and low-quantity months at low prices (weak-demand months where prices were cut and people bought a bit less than usual). It draws a line through that pattern and reports the slope. The slope is not the elasticity. It is a contaminated mixture of the firm's beliefs and the consumer's responsiveness.

Now here is the part that matters for our taxonomy. Suppose I tell you the firm has a column in its database called `EXPECTED-DEMAND-SCORE`, populated by the pricing team each month. The analyst now has all three variables. Have we solved the problem?

Not yet. Because the *arrows* are still up for grabs.

Watch this. The observational distribution `P(price, quantity, expected-demand)` is consistent with at least two DAGs:

```
DAG A:   EXPECTED-DEMAND → PRICE,  EXPECTED-DEMAND → QUANTITY,  PRICE → QUANTITY
DAG B:   PRICE → EXPECTED-DEMAND,  PRICE → QUANTITY,  EXPECTED-DEMAND → QUANTITY
```

These two DAGs encode the same conditional independencies. The data — *just the joint distribution of the three variables* — cannot tell them apart. Statisticians call this *Markov equivalence*; two DAGs are Markov-equivalent when they imply the same set of conditional-independence relations, which is the same set of statistical tests, which is the same set of fitted models. ([Verma & Pearl, UAI 1990](https://arxiv.org/abs/1304.1108); [Spirtes, Glymour & Scheines, *Causation, Prediction, and Search*, 2nd ed., MIT 2000](https://philpapers.org/rec/SPICPS).)

DAG A says the firm's expectations drive both price and quantity. DAG B says prices, set first, drive the firm's later expectations and the quantity simultaneously. Both stories are coherent. Both fit the data equally well. They give different answers to the elasticity question.

The arrow from `EXPECTED-DEMAND` to `PRICE` rather than the other way around is a *temporal-and-mechanism* claim: the pricing team forms an expectation, then sets the price, and the expectation is not caused by the price. That claim is true in this firm because that is how the pricing process works — someone at a desk looks at next month's signals and types in a number, and there are minutes and human cognition between expectation and price. The dataset does not record that minute. The dataset does not record the human cognition. The dataset records the value of `PRICE` and the value of `EXPECTED-DEMAND` in the same monthly row.

A causal-discovery algorithm can recover the *Markov equivalence class* — the set of DAGs consistent with the data — but it cannot orient the edges within the class without information from outside the data. The PC algorithm, the FCI algorithm, NOTEARS — all of them stop where Markov equivalence stops. ([Spirtes, Glymour, Scheines 2000](https://mitpress.mit.edu/9780262194402/causation-prediction-and-search/); [Zheng et al., NeurIPS 2018, "DAGs with NO TEARS"](https://proceedings.neurips.cc/paper/2018/hash/e347c51419ffb23ca3fd5050202f9c3d-Abstract.html).) This is a theorem, not an engineering limitation. The data does not contain the information needed to orient certain edges. You can wait for a better algorithm forever and the theorem will still hold.

This is where the temptation to call an LLM is strong. *"Hey Claude, look at this DAG with three unoriented edges and tell me which way the arrows go."* Does it work?

The honest answer, as of 2026, is: it works *unevenly*. Kıcıman, Ness, Sharma, and Tan reported in 2023 that GPT-4 reaches high accuracy on certain pairwise causal-direction benchmarks — smoking and cancer, exercise and mortality, the classics of the literature — by recalling consensus DAGs that are in fact in its training data. ([Kıcıman et al., 2023, arXiv:2305.00050](https://arxiv.org/abs/2305.00050)) Then Jin and colleagues built *Corr2Cause*, a benchmark deliberately constructed to require pure causal inference from correlational statements rather than recall, and found that the same class of models performed near chance. ([Jin et al., 2024, *Corr2Cause*, arXiv:2306.05836](https://arxiv.org/abs/2306.05836)) Long and colleagues evaluated LLM-assisted DAG elicitation on an ASCVD (cardiovascular risk) case study and found the model helpful for surfacing consensus knowledge from the literature and unreliable when the question stepped outside the consensus. ([Long et al., 2024, PMC12581789](https://pmc.ncbi.nlm.nih.gov/articles/PMC12581789/))

The honest reading: LLMs are *librarians for consensus DAGs* in well-studied domains, and unreliable for the novel-domain edges that are exactly the engineering reader's daily problem. The pricing case is not a textbook DAG. It is your firm's pricing process, and an LLM that has not been inside your firm has no privileged knowledge of it. (Recent foundation-model work — FairPFN at ICML 2025, and the broader causal-PFN literature — explicitly notes that when the causal quantity is not identified, the model "learns a posterior that may never concentrate around the true causal quantity." [verify-FairPFN-icml-2025-full-citation — referenced in pantry notes from arXiv:2506.10914, 2025; I have the family of papers but have not personally verified the ICML 2025 proceedings listing.])

The fix for wrong arrows is not an algorithm. The fix is a person who knows the data-generating process — in this case, *someone at the firm who knows what happens between the pricing team's morning meeting and the database write*. The arrow orientation comes from process knowledge. The dataset does not contain process knowledge. The dataset contains only the joint distribution of the variables.

I want to name the move precisely. *Wrong arrows* means the analyst's DAG is in the same Markov equivalence class as the true DAG but pointed differently, and the only way to choose within the class is information that the data does not contain — domain knowledge about mechanism, or an actual intervention.

---

## The third failure — wrong conditioning

Now the retrieval-augmented chatbot.

We have the right variables. Imagine the team has, finally, recorded *query-difficulty* — maybe a calibrated score from a small offline benchmark. And they have arrows that look about right:

```
QUERY-DIFFICULTY → RETRIEVAL-SCORE
QUERY-DIFFICULTY → USER-SATISFACTION
RETRIEVAL-SCORE → USER-SATISFACTION
```

The team wants to estimate the effect of `RETRIEVAL-SCORE` on `USER-SATISFACTION`. They know that difficulty confounds the relationship — easy queries inflate both. So they condition on `QUERY-DIFFICULTY`. Then they regress satisfaction on retrieval-score, holding difficulty fixed. Better, right?

Yes, *if difficulty is the only confounder*. But suppose there is one more variable, *response-length*, that the system also logs. The team thinks: "more variables, more controls, safer." They add `RESPONSE-LENGTH` to the conditioning set.

Here is what the DAG looks like with response-length added:

```
QUERY-DIFFICULTY → RETRIEVAL-SCORE → RESPONSE-LENGTH ← USER-SATISFACTION
                ↘                                  ↗
                  USER-SATISFACTION ←
```

Read the arrows. Retrieval-score affects response-length because a retriever that found relevant docs leads the LLM to write more (or less, depending on system). User-satisfaction also affects response-length, because satisfied users sometimes interact longer, asking follow-ups that the system logs. Response-length is a *collider* — two arrows point into it from different ancestors.

Conditioning on a collider opens a path that was closed. This is the structural fact that breaks the *more-variables-is-safer* intuition. By including `RESPONSE-LENGTH` in the regression, the team opens an artificial association between retrieval-score and satisfaction that was not in the underlying DAG. The estimate gets worse. The team thought they were being careful. Structurally, they were creating bias.

There is a sister failure. Suppose instead the team conditions on something on the *causal path* from retrieval-score to satisfaction — say, a "perceived-relevance" score the system also logs. Perceived-relevance is a *mediator*: retrieval-score → perceived-relevance → satisfaction. If you condition on the mediator, you block part of the effect you wanted to estimate. The total effect of retrieval-score on satisfaction *is* its effect through perceived-relevance. Subtract that out, and you have the *direct* effect, which is a different quantity. The team's reported number is now the answer to a different question than the one they thought they asked.

So *wrong conditioning* is two siblings under one roof. Conditioning on a collider opens a spurious path. Conditioning on a mediator blocks a real one. Both look like "controlling for variables" in regression notation. Neither is structurally what the analyst wanted.

Cinelli, Forney, and Pearl walked through these structurally distinct cases in their "Good and Bad Controls" piece and showed that the sign of your estimated effect can *flip* depending on whether you condition on a confounder, a collider, or a mediator. ([Cinelli, Forney & Pearl, working paper, R-493](https://ftp.cs.ucla.edu/pub/stat_ser/r493.pdf)) [verify final venue]. The intuition "control for everything you can measure" is not just suboptimal in their analysis. In the wrong structural setting, it is exactly backwards.

Watch what happens when an engineer reaches for a tool to fix this. `DoWhy.estimate_effect(treatment="retrieval_score", outcome="satisfaction", common_causes=["query_difficulty", "response_length"])`. The tool runs. It returns a number. The number is wrong for a reason the tool will never tell you: `response_length` is not a common cause. It is a collider. The tool trusted you. You told it `common_causes`. It estimated, given that DAG. The estimation step worked. The identification step — *is `response_length` really a common cause?* — happened before you called the function, and the function did not check.

This is the chapter's quietest important sentence: **the tool estimated `P(Y | do(X))` under the DAG you gave it. If the DAG was wrong, the tool returned the answer to a question that does not exist in the world.**

The fix is to know, on the DAG, what role each variable plays — confounder, collider, mediator — before adjusting. That knowledge requires understanding the data-generating process. The data-generating process is not in the dataset. It is in the heads of the people who built the system.

Chapters 5 through 8 are going to make confounders and mediators and colliders specific. We are not doing that yet. For this chapter, what you need is the recognition that *wrong conditioning* is a third, distinct way the data alone does not save you, and that recognizing it requires looking at the DAG with a particular question in mind: *for this query, what role does each conditioning variable play?*

---

## What the three failures share

Three failures. Hospital pneumonia. Pricing. Retrieval evaluation. Three different fields. Three different DAGs. Three different specific mistakes — a missing node, a misoriented edge, a misjudged conditioning role.

What they share is this: the data, all of it, every row, every column, every interaction, does not contain the information needed to fix the failure.

In the pneumonia case, the data does not contain severity. To know severity belongs on the DAG, a clinician has to say so. To know what severity does on the DAG, someone has to know pneumonia.

In the pricing case, the data does not contain the temporal-and-mechanism fact that the pricing team's expectation precedes their price. The arrow orientation comes from process knowledge. The data is consistent with both orientations.

In the retrieval case, the data does not contain the structural role of response-length. The classification of response-length as collider rather than confounder requires knowing how user-satisfaction and retrieval-score each cause response-length, separately. That is a system-architecture claim. The data is silent.

This is what I mean by **the identification layer**. It is the set of decisions a causal analysis requires before estimation can begin: *which variables exist on the DAG, which direction the edges point, and which variables to condition on for which query*. Pearl's framework names these three decisions; the Shpitser-Pearl ID algorithm (2008) makes the dependence of identification on the DAG explicit by returning identifiable-or-not for any DAG-and-query pair in finite time. ([Shpitser & Pearl, JMLR 2008](https://www.jmlr.org/papers/v9/shpitser08a.html)) The algorithm is *complete*. It will tell you, with mathematical certainty, when the DAG-plus-data combination cannot answer your causal question. What it requires from you is the DAG.

The DAG is the question. The data is the answer to *some* question. Identification is the check that the DAG and the data match.

I want to make the thesis explicit, because this chapter is where the book first allows itself to state it cleanly: **the identification layer of causal analysis — variable selection, edge orientation, conditioning decisions — currently requires domain judgment that no causal AI tool reliably supplies.** Tools can estimate, given a DAG. Tools can search the Markov equivalence class. Tools can recall consensus DAGs from the literature when the question has been well-studied. None of this replaces the act of supplying the DAG for *your* problem, in *your* domain, under *your* constraints.

Two pieces of methodological honesty before we move on.

First, the *three-failures taxonomy* is a heuristic. It is the smallest set of failure types I have found that distinguishes the cases an engineering reader actually meets. Real DAGs sometimes have several of these going on at once — the pneumonia case is technically a wrong-variables failure (severity is missing) and a wrong-conditioning failure (asthma sits downstream of severity, and conditioning on it stratifies the wrong way). When the failures co-occur, the cleanest move is to name each and treat them sequentially. The taxonomy is a tool for diagnosis; do not treat it as a partition.

Second, the taxonomy under-specifies a fourth class of failure that lives just outside this chapter's scope: *selection failures*, where the sample itself is generated by a process that conditions on variables not in your DAG. Estimating fraud-model accuracy on transactions the model approved is the canonical case — the labels exist only because the model approved the transaction, so the entire training set conditions on a downstream variable. ([Lakkaraju et al., 2017](https://dl.acm.org/doi/10.1145/3097983.3098066)) I am calling this a separate class because the structural fix is different — you cannot generally repair selection by adjusting on the DAG; you need either an experiment, an instrument, or a partial-identification bound. Chapter 8 takes this seriously. For this chapter, when in doubt, flag the failure as "wrong-conditioning, possibly selection," and let the next chapter sort it out.

---

## A worked walk-through — the pneumonia case, three failures at once

Let me show you what a clean reading of the pneumonia case looks like, using all three failure types as diagnostic tools. The team's reported finding: *asthma is protective in pneumonia patients*.

**Step 1. Draw the team's DAG.** As reported, the model is `mortality ~ f(asthma, age, vitals, labs, comorbidities)`. The implicit DAG has asthma as one parent of mortality, alongside other measured features. There is no severity node.

**Step 2. Apply Failure Type 1 — wrong variables.** Is there a variable the data does not contain that affects both the treatment-like variable (asthma flag) and the outcome (mortality)? Yes — severity. A clinician supplies this. The DAG is missing the node `SEVERITY`, which causes both *who-gets-aggressive-care* and *outcome*. The data does not contain severity, only proxies.

Domain knowledge required: *what severity is, that it exists, that it drives both treatment escalation and outcome*. Provided by: a pulmonologist or hospitalist, not by any statistic.

**Step 3. Apply Failure Type 2 — wrong arrows.** With severity now on the DAG, ask whether the edges as drawn are oriented correctly. Does asthma cause severity, or is asthma a side-condition that interacts with severity to determine treatment? Domain answer: asthma is a pre-existing condition, severity is determined by the current pneumonia plus the patient's baseline — they are roughly independent of each other at admission. The arrow from severity to treatment-aggressiveness is right; the arrow from asthma to treatment-aggressiveness is right (because the doctor reacts to the flag); the absence of an arrow between asthma and severity is, in this DAG, a substantive claim.

Domain knowledge required: *temporal ordering of patient conditions and medical decisions*. Provided by: clinical workflow knowledge, again the doctor, not the data.

**Step 4. Apply Failure Type 3 — wrong conditioning.** Even with severity and asthma both on the DAG, what should we condition on to estimate the effect of `asthma` on `mortality`?

```
   SEVERITY
   ↙      ↘
ASTHMA → AGGRESSIVE-CARE → MORTALITY
                            ↑
                         SEVERITY
```

The model in the original analysis conditioned on aggressive-care indirectly (by including ICU admission, intubation status, antibiotic timing). Aggressive-care is *on the causal path* from asthma to mortality — it is a mediator. Conditioning on it blocks the protective effect of asthma-triggers-escalation. The model's reported effect is the direct effect of asthma on mortality holding aggressive-care fixed, which, biologically, is *the harmful effect of asthma when you do not treat it more aggressively*. That number is correctly small (asthma alone, without escalation, is bad), but the model's downstream behavior interprets it as "asthma is protective," which is a misreading of which question the number answers.

Domain knowledge required: *which variables sit on the causal path from asthma to mortality and which sit off it*. Provided by: clinical-workflow knowledge plus DAG literacy. The doctor knows the path. The DAG-literate analyst knows what conditioning on the path does.

**Step 5. Synthesize.** The original analysis suffered from Failure Type 1 (severity unmeasured), and the consequence rendered the model's predictions backwards under intervention. Fixing Failure Type 1 alone would not be enough — the analysis would also need to attend to Failure Type 3 (the mediator role of aggressive-care). Failure Type 2 is, in this case, mostly clean; the arrows the domain experts would draw match the arrows the original analysis implicitly assumed, except for the missing severity node.

None of these fixes are in the dataset. All of them require a person.

That is what the identification layer feels like in one full case. The data did not lie. The data answered correctly. It just answered a different question than the one the model's deployment behavior would have implied.

---

## Chapter summary — what you can now do

You can look at a problem with a candidate DAG and ask three diagnostic questions:
1. *Is the DAG missing a node?* If a domain expert would say "but X drives both of these," that is Failure Type 1. The data cannot supply X; only the expert can.
2. *Are the edges pointed correctly?* If two DAGs in the same Markov equivalence class are both consistent with the data, that is Failure Type 2. The data cannot orient; only mechanism or intervention can.
3. *Is the conditioning set doing what you think?* If you are conditioning on a collider or a mediator under the belief you are conditioning on a confounder, that is Failure Type 3. The data cannot tell you which role a variable plays in the DAG; only the structural reading can.

And you can write down, for any analysis, a one-page AI Use Disclosure that lists every identification-layer decision and names its source. That artifact — *which decisions were yours, which were the LLM's, which were the literature's* — is the chapter's proof-of-work.

Act One closes here. We have now experienced the identification layer (Chapter 3), and named it explicitly (Chapter 4). The book has been telling you, since Chapter 1, that there is a layer of causal analysis the tools do not supply. You have the name for it now.

The data does not contain the question.

---

## Bridge to Chapter 5

Act Two begins next week. The three failure types are heuristics — useful for diagnosis, not yet operational. Each of them gets sharper teeth in the chapters that follow. We start with the structural role that the pneumonia case quietly relied on, the one that lurked behind both the missing-variable and the wrong-conditioning readings. The first tool gets a name.

---

## Midterm — Identification-Layer Diagnostics

*This midterm replaces the standard exercise set for Chapter 4. Three scenarios, four parts each, ~25 minutes per scenario, 100 points total. Closed book except for one page of handwritten notes. The AI Use Disclosure (Section A.4 of each problem) is mandatory and graded for honesty as well as content. You may use Claude or ChatGPT for Part A.1; you must disclose if you do.*

---

### Scenario M1 — A production recommendation system (production ML domain)

A streaming service trained a recommendation model on six months of logged data: `(user_id, recommended_item, was_clicked, was_completed, watch_time)`. The model maximizes predicted click-through. The team deploys the new model and finds that watch-time has *decreased* by 4.2 percent week-over-week, even though predicted click-through went up. Internal review notes that the previous model had been live for two years and that its recommendations had been the source of all the training data. The team is now debating whether the new model is "worse" or whether the change is a measurement artifact.

**Parts:**
**(a)** Draw a candidate DAG for the data-generating process. Include at minimum: the previous policy's recommendations, the items shown to each user, the user's click decision, completion decision, watch-time, and any latent variables you believe necessary. (15 pts)
**(b)** Identify the dominant identification failure type the team is at risk of. Use the taxonomy: wrong variables, wrong arrows, wrong conditioning. (5 pts)
**(c)** Name, in one sentence each, two pieces of domain knowledge no dataset alone could supply that would help resolve the failure. (10 pts)
**(d)** Write the AI Use Disclosure for the analysis you performed on this problem. Use the template at the end of this chapter. The named irreducibly-human contribution must be specific to recommendation systems. (5 pts)

**Subtotal: 35 pts**

---

### Scenario M2 — A sepsis-prediction model at a regional hospital network (healthcare AI domain)

A hospital network deploys a model that predicts sepsis onset four hours before clinical diagnosis, using continuously logged EHR data (vitals, labs, medications, nursing notes). External validation reports AUC of 0.84. After eighteen months of deployment, an audit finds that the model triggered alerts mostly on patients who were *already receiving antibiotics* — and a retrospective analysis shows the model's predictive power dropped sharply (AUC 0.61) when restricted to patients who had not yet received antibiotics at the time of prediction. The model vendor argues this is expected. The clinical lead argues the model is "predicting its own footprint." A reporter is asking questions.

**Parts:**
**(a)** Draw a candidate DAG including: clinical state of the patient, attending clinician's judgment, antibiotic-administration decision, the model's prediction, and any latent variables you find necessary. (15 pts)
**(b)** Identify the dominant identification failure type. The taxonomy applies; you may also flag if you suspect selection (Chapter 8 territory) and justify briefly. (5 pts)
**(c)** Name, in one sentence each, two pieces of domain knowledge no dataset alone could supply that would help resolve the failure — at least one must come from clinical practice, not from statistics. (10 pts)
**(d)** Write the AI Use Disclosure for your analysis. The named irreducibly-human contribution must reference a specific clinical variable, edge, or conditioning choice. (5 pts)

**Subtotal: 35 pts**

---

### Scenario M3 — Capacity planning for an inference cluster (infrastructure domain)

An ML infrastructure team runs a fleet of inference servers. They want to predict the effect of doubling GPU memory per node on p99 latency. They have a year of telemetry: per-node memory utilization, request volume, model size deployed, p50/p95/p99 latency, autoscaler decisions, evictions. They estimate a regression of p99 latency on GPU memory across nodes, controlling for request volume and model size. The reported effect is small. A capacity-planning proposal cites this number to argue against the upgrade. A senior engineer pushes back, saying the analysis "is asking the data to do something it cannot do." She does not yet explain why.

**Parts:**
**(a)** Draw a candidate DAG including: workload mix (which models get scheduled where), autoscaler decisions, per-node memory and GPU configuration, request routing, observed latency, and any latent variables you find necessary. (15 pts)
**(b)** Identify the dominant identification failure type. (5 pts)
**(c)** Name, in one sentence each, two pieces of domain knowledge no dataset alone could supply — at least one must concern the autoscaler or the request-routing process. (10 pts)
**(d)** Write the AI Use Disclosure for your analysis. The named irreducibly-human contribution must reference a specific infrastructure variable, edge, or conditioning choice. (5 pts)

**Subtotal: 30 pts**

---

**Grading rubric, briefly:**
- A correctly oriented DAG with all necessary latent nodes named — full marks on (a).
- A correctly identified failure type *with reasoning* — full marks on (b). A wrong type with sound reasoning earns partial credit; a right type with no reasoning does not.
- Domain-knowledge items that are *specific* (named clinical concept, named infrastructure mechanism) get full marks. Items at the level of "more domain expertise" do not.
- Disclosure items that show genuine boundary-drawing — "the LLM offered this DAG and I rejected this edge for this reason" — get full marks. Items that read as compliance paperwork ("I used Claude for help") do not.

---

## LLM exercise (in addition to the midterm)

Open Claude (or ChatGPT, or Gemini — the exercise specifies the comparison below). Paste the following prompt exactly. Save the full response.

```
You are helping me draft a causal DAG for a problem I am working on.

The problem: A B2B SaaS company sends marketing emails to leads. Each lead is
either "engaged" (opens >2 emails in the first 30 days) or not. The company
wants to estimate the causal effect of "engaged" on "converted-to-paid".

The data the company has:
- email opens (counts and timestamps)
- email click-throughs
- whether the lead came from organic search vs. paid ads
- company size of the lead's employer
- industry of the lead's employer
- whether a sales rep followed up by phone after the third email
- whether the lead converted to paid within 90 days

Please propose a DAG for this problem. List the nodes, list the edges with
directions, and indicate any unmeasured variables you believe should be on
the DAG. For each edge, give a one-sentence justification.
```

**Your assignment:**
1. Run the prompt on at least two different LLMs.
2. Apply the three-failure taxonomy to each LLM's DAG. Where are the unmeasured variables? Where are the arrows that could be reversed under Markov equivalence? Where are the variables the LLM proposed as confounders that you suspect are colliders or mediators?
3. Write a one-page critique. The critique must name at least one identification failure in each LLM's output. If an LLM produced a DAG you genuinely find correct, defend it against the taxonomy: explain why each failure type does not apply.
4. Write the AI Use Disclosure for the exercise. The "irreducibly-human contribution" cell must name the specific edge or variable judgment you made that no LLM in this exercise made for you.

Submit: the two raw LLM outputs (copy-pasted), your DAG critique, your Disclosure. Due with the midterm.

---

## AI Use Disclosure — full format introduced here

The AI Use Disclosure is an artifact of this course. It is not, as of 2026, a published standard. It is the operational test of the thesis: *every analysis where the identification layer matters should be able to name, decision by decision, which decisions a human made and which a tool made*. If every cell in the disclosure points to the tool, the thesis is wrong and we should know that. If at least one cell in every Disclosure points to a person making a judgment no tool supplied, the thesis is doing work.

Treat the format as a working specification. We may revise it after seeing how Spring 2026's submissions read.

```
AI Use Disclosure
─────────────────
Tool(s) used:           [name and version, e.g., Claude 4.x Opus, ChatGPT-4o, Gemini 2.5 Pro]
Prompts pasted:         [the exact prompts, or paraphrased + transcript link]
LLM output used:        [what you kept from the LLM output and used in your analysis]
LLM output revised:     [what you changed in the LLM output and why]
LLM output rejected:    [what you discarded from the LLM output and why]
Identification decision YOU made that no LLM could:
                        [the irreducibly-human contribution — name a specific
                         variable, edge, or conditioning choice; cite the domain
                         fact that grounded the decision]
```

**Note for the Part B bonus:** the named identification decision must reference a *specific* domain variable, edge, or conditioning choice from your own field — not "I used domain expertise." The point is that "domain expertise" generic-ed-out becomes its own jargon. Name the variable. Name the edge. Name the choice.

---

## Key terms

- **Identification layer.** The set of decisions a causal analysis requires *before* estimation: which variables exist on the DAG (variable selection), which direction the edges point (edge orientation), and which variables to condition on for which query (conditioning decision). These decisions cannot be made from data alone in the general case (Pearl 2009, Ch. 3; Shpitser-Pearl 2008).
- **Identification vs. estimation.** Identification asks "given a DAG and a causal query, can the query be written as a function of the observable joint distribution?" Estimation asks "given an identified expression, what does the data say?" Identification is logically prior; an estimator running on a wrong DAG produces a number that does not correspond to any quantity in the world.
- **Markov equivalence class.** The set of DAGs that imply the same conditional-independence relations on a given set of variables. DAGs within the same class fit the same observational data equally well; the data cannot distinguish among them. Distinguishing requires information external to the data — domain knowledge or intervention (Verma & Pearl 1990; Spirtes-Glymour-Scheines 2000).
- **Edge orientation.** The directional claim made by an arrow in a DAG: that the variable at the tail causes the variable at the head, in the sense that intervening on the tail propagates to the head and not the reverse. Within a Markov equivalence class, the data does not determine all orientations.
- **Variable selection (for identification).** The decision of which variables to include on the DAG — including unmeasured ones that nonetheless belong because they affect both treatment and outcome. Not the same as feature selection in a predictive model; this selection determines whether the causal query is even identified.
- **Conditioning decision.** The choice of which variables to adjust for in the estimation step. The structurally correct conditioning set depends on the DAG and the query — adjusting for confounders, not adjusting for mediators or descendants of colliders. The data does not tell you which role a variable plays.
- **AI Use Disclosure.** Course artifact introduced in this chapter. A short structured document accompanying any analysis, naming which identification-layer decisions came from a tool, which from a literature, which from a domain expert, and which from the analyst's own judgment. Adjacent precedents: model cards ([Mitchell et al. 2019](https://dl.acm.org/doi/10.1145/3287560.3287596)), datasheets for datasets ([Gebru et al. 2018, updated 2021](https://arxiv.org/abs/1803.09010)), Hernán's "C-Word" ([Hernán 2018, *AJPH*](https://ajph.aphapublications.org/doi/10.2105/AJPH.2018.304337)).

---

## Further reading

1. Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge. Chapter 3 — the technical reference for identification.
2. Shpitser, I., & Pearl, J. (2008). "Complete Identification Methods for the Causal Hierarchy." *Journal of Machine Learning Research* 9, 1941–1979. [JMLR](https://www.jmlr.org/papers/v9/shpitser08a.html). The completeness theorem for identification.
3. Cinelli, C., Forney, A., & Pearl, J. "A Crash Course in Good and Bad Controls." Working paper R-493, UCLA Cognitive Systems Laboratory. [PDF](https://ftp.cs.ucla.edu/pub/stat_ser/r493.pdf). The classification of structural roles for conditioning variables. *[Verify final publication venue and year; widely cited as forthcoming or as *Sociological Methods & Research*; I have not personally confirmed the published version.]*
4. Kıcıman, E., Ness, R., Sharma, A., & Tan, C. (2023). "Causal Reasoning and Large Language Models: Opening a New Frontier for Causality." [arXiv:2305.00050](https://arxiv.org/abs/2305.00050). On LLM strengths and weaknesses in causal DAG elicitation.
5. Jin, Z., Liu, J., Lyu, Z., et al. (2024). "Can Large Language Models Infer Causation from Correlation?" *Corr2Cause* benchmark. [arXiv:2306.05836](https://arxiv.org/abs/2306.05836). The benchmark that separates recall from inference.
6. Long, S., et al. (2024). "Can Contemporary LLMs Provide the Domain Knowledge Needed for Causal Inference?" ASCVD case study. [PMC12581789](https://pmc.ncbi.nlm.nih.gov/articles/PMC12581789/).
7. Caruana, R., Lou, Y., Gehrke, J., Koch, P., Sturm, M., & Elhadad, N. (2015). "Intelligible Models for Healthcare." *KDD 2015*. [ACM DL](https://dl.acm.org/doi/10.1145/2783258.2788613).

---

**What would change my mind:** A demonstration that an automated tool — causal-discovery algorithm, LLM, foundation model, anything — can reliably propose the missing-variable, the correct edge orientation, *and* the correct conditioning set on a novel domain problem (one outside its training data) without a domain expert in the loop. The Corr2Cause benchmark numbers and the ASCVD case study say this is not currently the case; a stronger result on a comparable benchmark would force me to revise the thesis.

**Still puzzling:** I do not yet have a clean way to teach the boundary between *wrong-conditioning* (Type 3 here) and *selection-on-outcome* (Chapter 8) without spoiling the later chapter. The two failures co-occur often in production ML cases — fraud-model evaluation, survivor-bias in churn, the dataset-construction step in active learning — and the structural fix is genuinely different for each. The chapter currently flags this once; I am not sure that is enough.

---

**Tags:** identification-layer, Pearl-causality, DAG-elicitation, LLM-limitations, midterm

---

## Draft flags

- Cinelli, Forney & Pearl, "A Crash Course in Good and Bad Controls" — I cite the UCLA working paper PDF (R-493). The piece is widely circulated as forthcoming / published in *Sociological Methods & Research*; the pantry notes flag the same uncertainty. **Action:** confirm final venue and year before publication.
- FairPFN ICML 2025 referenced in pantry research notes (via arXiv:2506.10914, 2025). I have not personally verified the ICML 2025 proceedings listing. The chapter mentions FairPFN briefly and parenthetically. **Action:** verify the ICML 2025 acceptance and citation form before publication; if unverifiable, replace with the arXiv preprint citation only.
- Verma & Pearl 1990 — cited as the original Markov-equivalence result. The reference often appears as a UAI 1990 paper; an arXiv-mirrored later version exists (arXiv:1304.1108) and I link to it. **Action:** confirm preferred primary citation (UAI 1990 conference paper vs. the arXiv-archived version) per course style.
- The retrieval-augmented chatbot opening case is composed from the pantry's "Case 4: RAG quality evaluation under user feedback" (`research-ch-04-the-identification-layer.md`, Section 3) plus the chapter notes' Case 4 in pantry/04-the-identification-layer_notes.md. The case is engineering-realistic but has no canonical primary citation. The chapter does not cite it as a published case. **Action:** if a published RAG-evaluation post-mortem becomes available (Microsoft, LinkedIn, Netflix engineering blogs), substitute the cite.
- Voice-unanchored flag — no `style/` examples exist for this book. Voice was calibrated from CLAUDE.md §6 and from the pantry notes' "smartest friend at coffee" target.
- Open question for `book.md`: The current `book.md` is largely a template — One-Sentence Pitch, Argument, Gap, Reader, Outline are all placeholder. The chapter assumes the audience and thesis from the prompt and from TIKTOC. Filling in `book.md` would let later chapters anchor more tightly. Not blocking for this draft; flagging for Nik.
