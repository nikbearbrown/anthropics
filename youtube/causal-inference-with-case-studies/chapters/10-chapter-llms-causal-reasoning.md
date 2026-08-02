# Chapter 11: Can LLMs Actually Do Causal Reasoning?


## TL;DR

- Companion to the case study by Nilay Raut.
- The chapter moves through Learning Objectives, Prerequisites, Why This Chapter Exists, Section 1: The Question That Started This, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Companion to the case study by Nilay Raut*

---

## Learning Objectives

By the end of this chapter, you should be able to:

1. **Classify** any causal question as Rung 1, Rung 2, or Rung 3 on Pearl's Ladder of Causation — and do it fast, in the wild, before a model gets a chance to mislead you.
2. **Explain**, from first principles, why next-token prediction cannot produce structural causal reasoning — and why this is architectural, not a data quantity problem.
3. **Predict** the specific failure mode an LLM will exhibit on a given causal question: confident wrong answer, fabricated mechanism, or correct hedge.
4. **Diagnose** whether a model's correct-sounding hedge reflects genuine structural reasoning or trained hedging behavior — using prompt sensitivity as your instrument.
5. **Design** a routing architecture that assigns causal queries to the right tool at each rung.

---

## Prerequisites

You have read Chapters 1–9 of this book. Specifically, you are fluent in:

- **Causal diagrams and d-separation** (Chapter 2): You can read a DAG, identify open and blocked paths, and trace confounding through a fork.
- **The backdoor criterion** (Chapter 3): You know what it requires, what it rules out, and what happens when you condition on a collider or a mediator.
- **The do() operator** (Chapter 4 onward): You understand that $P(Y \mid X)$ and $P(Y \mid do(X))$ are different objects — not just different estimates of the same thing, but answers to fundamentally different questions.
- **Potential outcomes** (Chapter 8): You know what $Y_x$ means — the value $Y$ would have taken had $X$ been set to $x$ by intervention — and why it cannot be observed for the same individual under both treatment and control.

If any of these feel shaky, go back before continuing. This chapter uses them without re-teaching them.

---

## Why This Chapter Exists

You just spent nine chapters learning to reason carefully about cause and effect. You can draw a DAG, apply the backdoor criterion, and distinguish an association from an intervention claim. That is not a small thing. Most analysts working with data today cannot do it.

Now here is the uncomfortable question: what happens when an analyst who *cannot* do those things uses a large language model to answer a causal question? What does the model do? Does it reason correctly? Does it fail gracefully? Or does it fail in a way that is invisible — fluent and confident and wrong?

This chapter is about that question. And the answer, as you will see, is not that LLMs are bad at causal reasoning. It is that they are *specifically* bad at the rungs that matter most, in a way that is hard to see without exactly the knowledge you have just built.

I am going to show you where the failure lives, why it is there, and how to detect it. Nilay Raut's case study in the next chapter documents what happens when you actually run the benchmark. I want you to understand the machinery before you read the results.

---

## Section 1: The Question That Started This

Here is a real scenario. I am not going to dress it up.

A hospital system noticed that patients reported higher satisfaction scores at facilities with shorter ER wait times. The correlation was real — statistically significant, consistent across facilities, not a fluke of small samples. An analyst fed three years of hospital records into a large language model and asked: *what drives patient satisfaction, and what should we do about it?*

The model answered confidently. It identified the wait-time pattern. It recommended an initiative to reduce wait times. The hospital spent $2.3 million hiring temporary intake staff, reduced median wait times by 22 minutes, and watched satisfaction scores not move.

What went wrong?

The model answered the question it was asked in its own language. The analyst asked: *what should we do?* The model answered: *what does the data show?* These look like the same question. They are not. They are separated by a distinction you now know how to name.

The analyst needed $P(\text{Satisfaction} \mid do(\text{WaitTime} = \text{low}))$ — what happens to satisfaction *if we intervene* on wait times, severing the variable from everything that naturally caused it.

The model answered $P(\text{Satisfaction} \mid \text{WaitTime} = \text{low})$ — what satisfaction looks like *when we observe* short wait times in the existing system.

The difference between those two expressions is not a matter of statistical precision. It is a structural gap. And the actual causal structure of the hospital situation made that gap expensive.

The real story was this: high staffing levels caused *both* shorter wait times and higher patient satisfaction. Staffing was the upstream common cause. The path

$$\text{WaitTime} \leftarrow \text{StaffingLevel} \rightarrow \text{Satisfaction}$$

is a back-door path from WaitTime to Satisfaction — a fork with StaffingLevel as the confounder. The observational correlation between wait times and satisfaction was real, but it was generated by the upstream variable. Intervening on wait times without changing staffing levels moved a proxy, not the cause.

The model could not see this. It had no causal graph. It had patterns.

This is the problem this chapter is about. Let me now give you the vocabulary to understand it precisely.

---

## Section 2: The Ladder — Three Things "Causal" Can Mean

Judea Pearl's Ladder of Causation is the single most useful organizing tool I know of for understanding what a causal question is actually asking. You have seen it in the theory spine. I want to revisit it here with a specific purpose: showing you exactly where an LLM lives on the ladder, and what it means that it lives there.

The ladder has three rungs. Each rung asks a categorically different kind of question, and each requires a strictly more powerful reasoning engine than the one below it.

### Rung 1: Association — Seeing

**The question:** What do patients with short wait times look like?

**Formal notation:** $P(Y \mid X)$ — the probability of $Y$ given that $X$ is *observed* to be true.

**What it requires:** A joint probability distribution over observed variables. Statistics. Pattern recognition.

This is the domain of correlation, regression, clustering, and prediction. A model at Rung 1 is excellent at finding structure in data. It can identify that variable $A$ is correlated with variable $B$, compute conditional probabilities, flag potential predictors. Given enough data, it can do this extraordinarily well.

LLMs are trained on text. Text is almost entirely a record of the observational world — a vast archive of what things looked like when people wrote about them. This makes LLMs excellent Rung 1 reasoners. When you ask "what does the data suggest?" or "what pattern do you see?" you are asking a Rung 1 question, and a language model will answer it with genuine competence.

### Rung 2: Intervention — Doing

**The question:** If we *forced* every patient to have a short wait time — not because they happened to arrive when staffing was high, but because we mandated it — what would happen to satisfaction?

**Formal notation:** $P(Y \mid do(X))$ — the probability of $Y$ given that $X$ has been *set from outside the system*, severing its connection to its natural causes.

**What makes this different from Rung 1:** The do() operator is not a conditional. It represents something physically real: the act of reaching into the causal graph and fixing a variable from outside, disconnecting it from everything that used to generate it. When you intervene on WaitTime by hiring temporary intake staff, you are not sampling from the natural joint distribution anymore. You are operating outside it. The mechanism that generated the observational pattern has been replaced.

**What it requires:** A structural causal model — a DAG that represents not just how variables correlate in the observed world, but how they would respond to external manipulation.

The key insight, and the one I want you to hold onto: the do() operator *deletes the incoming arrows to the intervened variable*. When you compute $P(\text{Satisfaction} \mid do(\text{WaitTime} = \text{low}))$, you are asking about a modified graph — one from which the edge StaffingLevel → WaitTime has been removed, because you are now controlling wait times directly, not through staffing. The confounding path is broken by the intervention itself. But you still need to know whether there are other paths, and what the structural equations look like.

An LLM has almost no training signal for this. It has read descriptions of interventions — millions of sentences about experiments, policy changes, randomized trials. But reading a description of an experiment is not the same as training on the structural relationships that experiments reveal. The model learns that certain sentences follow certain contexts. It does not learn how the world would re-configure itself if a variable were forced to change.

### Rung 3: Counterfactual — Imagining

**The question:** This specific patient waited 45 minutes and reported dissatisfaction. Would they have been satisfied if their wait had been 10 minutes?

**Formal notation:** $P(Y_x \mid X = x')$ — the probability that $Y$ would have taken the value it would take under intervention $do(X = x)$, for an individual we actually observed with $X = x'$.

In the potential outcomes notation you learned in Chapter 8: $Y_x$ is the value $Y$ would have taken had $X$ been externally set to $x$ by intervention. The subscript marks it as a potential outcome — defined for every individual, but observable for only one value of $x$ per individual. You observe either the treated outcome or the control outcome, never both. That is the fundamental problem of causal inference.

**What makes this harder than Rung 2:** Rung 2 asks about a population under a new policy. Rung 3 asks about a *specific individual* in a world that never existed. You cannot run the counterfactual experiment. You need a structural model of the individual *plus* an exogeneity assumption: the claim that this person's unobserved characteristics — their baseline satisfaction, their health anxiety, their prior experiences — would have been the same in the counterfactual world where their wait was shorter.

That assumption is not testable from the data. It is a scientific commitment. And no language model can make it, because it is not a statement about patterns in text.

### The Summary

| Rung | Name | Notation | Question Type | Hospital Example | LLM Capability |
|------|------|----------|--------------|-----------------|----------------|
| 1 | Association | $P(Y \mid X)$ | "What is?" | "Do hospitals with short waits have higher satisfaction?" | **High** |
| 2 | Intervention | $P(Y \mid do(X))$ | "What if we do?" | "If we reduce wait times, will satisfaction improve?" | **Fails** |
| 3 | Counterfactual | $P(Y_x \mid X = x')$ | "What if it had been different?" | "Would *this* patient have been satisfied with a shorter wait?" | **Fails** |

The asymmetry is the thing to notice. LLMs are not bad at causal reasoning in general — they are excellent at Rung 1. The problem is that Rung 1 fluency creates the *appearance* of Rung 2 and Rung 3 competence. The hospital consultant's model sounded exactly like it was answering an intervention question. It wasn't. That gap between the surface form of a causal answer and structural causal reasoning is what the rest of this chapter is designed to help you see.

---

## Section 3: What LLMs Are Actually Doing

I want to be precise about the machinery here, because understanding it will let you predict failures rather than just observe them.

A large language model is trained on a single objective: given a sequence of tokens, predict the next one. That is it. The model's internal representations — its attention patterns, its billions of parameters — are all optimized to make the next word in a sentence more probable, measured across a training corpus of roughly one trillion words.

This is a genuine achievement. Next-token prediction, at sufficient scale, produces something that looks a lot like understanding. The model learns grammar, factual associations, logical patterns, stylistic conventions. It learns that questions about medical interventions tend to be followed by hedges about confounding. It learns that sentences beginning "if we mandate..." tend to conclude with policy predictions.

But here is the structural problem, and I want you to see exactly where it lives.

### The corpus is observational

The training data is almost entirely a record of what the world looked like when people wrote things down. A newspaper reports that vaccinated populations had lower COVID mortality. A medical journal reports that the aspirin group had fewer cardiac events. A business analysis reports that well-staffed stores had higher sales. Every sentence encodes something of the form $P(Y \mid X)$: here is what the world looked like when these conditions held.

Almost none of these sentences encode $P(Y \mid do(X))$: here is what the world would look like if we forced those conditions to be true, from outside the system, severing the variable from its natural causes.

When a model reads "the randomized controlled trial showed that statins reduced LDL cholesterol by 40%," the model learns that sentences like this appear in cardiovascular pharmacology contexts. It does not learn the structural equation

$$\text{LDL} = f(\text{statin dose}, \text{genetics}, \text{diet}, \varepsilon)$$

nor does it learn how external manipulation of statin dose propagates through the causal graph while leaving the other terms unchanged. The text is a description of what happened when someone performed an intervention in the physical world. The intervention itself, and the structural relationships it revealed, are not in the corpus. The words are.

### More data cannot fix this

The natural response is: train on more causal examples. Fine-tune on Pearl's framework. Add causal reasoning to the instruction tuning. If the model fails at Rung 2, surely exposure to more intervention-describing text will close the gap?

This intuition is wrong in a principled way.

An LLM that has processed every randomized controlled trial ever published has processed the *reports* of those trials — the results, the conclusions, the abstracts. It has not been trained on outcomes that change when the same variable is manipulated. It has never, in training, seen "Patient A received aspirin; outcome was X" paired with "Patient A, identical in every measurable way, did not receive aspirin; outcome was Y." That paired-worlds structure is what causal identification requires. Text reports the result of one world. Counterfactual reasoning requires the comparison.

The causal graph that explains why aspirin reduces cardiac events is a fact about arterial biology and blood chemistry. A sentence about it is a pointer to that fact, not the fact itself. Reading more pointers does not give you the structure they point to.

This is not a gap that more training data fills. It is an architectural mismatch between the training objective and the reasoning task. Next-token prediction optimizes for fluency given context. Rung 2 reasoning requires structural equations. These are different things, and one does not produce the other at scale.

### What the empirical evidence shows

Nilay's case study cites two benchmarks that test this directly.

CLADDER (Zevcevic et al., 2023) constructed causal questions with formal ground-truth answers derived from structural causal models — questions where the correct answer is a matter of causal algebra, not domain knowledge. The reported pattern: performance on Rung 1 questions was high for leading models; Rung 2 accuracy dropped substantially; Rung 3 accuracy fell near chance. (Note: Nilay flagged these figures for independent verification. Read them as directionally documented, not settled.) More telling: the models that appeared to perform well on Rung 2 questions were exploiting surface-level linguistic cues. Words like "force," "mandate," and "intervene" triggered epistemic hedges. The underlying computation was still associational.

Kiciman et al. (2023) reached a compatible conclusion: GPT-4 showed impressive causal performance on tasks solvable by pattern-matching over statistical regularities in its training data. Systematic failures appeared precisely when the correct answer required acknowledging that a question was *formally unanswerable* from the given evidence. A model trained to be helpful, to produce complete responses, has strong pressure against saying "this question cannot be answered." That pressure is not a bug. It is a reasonable optimization target for a general-purpose assistant. It becomes a problem when the assistant is being used as a causal reasoning engine.

---

## Section 4: The Failure Taxonomy

Before you can detect failure, you need a vocabulary for it. Here is what I observe when LLMs encounter causal questions at each rung.

### Tier 1 failure: Rung 1 without a hedge

The simplest failure. A model gives an association and presents it as a finding without noting that the data is observational. "Hospitals with shorter wait times have higher patient satisfaction" — stated as a conclusion rather than an observation. The error is not in the claim; it is in the implicit framing that the correlation is informative about interventions.

This is the easiest failure to miss because it sounds like good data analysis. It is also the least dangerous, because an analyst who knows the ladder can add the hedge themselves.

### Tier 2 failure: confident Rung 2 answer from Rung 1 reasoning

This is the hospital failure. The model is asked $P(Y \mid do(X))$ and answers with something derived from $P(Y \mid X)$. The answer is directionally plausible — it points the right way, consistent with the observational pattern — but it has no structural basis. The selection mechanism that generated the pattern has been silently assumed away.

What makes this failure hard to catch: the answer is often directionally correct in domains where the causal structure happens to match the observational pattern. In those cases, the model looks like a Rung 2 reasoner. It is not.

### Tier 3 failure: fabricated mechanism

This is the most dangerous failure, and it deserves its own name. I call it the **fabricated mechanism** failure.

The model is asked a Rung 2 or Rung 3 question. Instead of acknowledging that the question is unanswerable from the available evidence, it produces a confident directional answer *and then explains why the answer is correct*, citing accurate domain knowledge to justify a structurally invalid inference.

Here is what this looks like in practice. A model is asked: "Based on the aspirin observational study, if a hospital mandates aspirin for all cardiac patients, what does the data predict?"

A fabricated mechanism response looks like this:

> "Based on the observed 30% reduction in cardiac events among aspirin users, mandating aspirin across the patient population would likely produce a comparable reduction. This is consistent with the known mechanism of aspirin's antiplatelet action, which inhibits thromboxane A2 and reduces clot formation."

The biology in that answer is real. Aspirin does inhibit thromboxane A2. A reader with medical knowledge will recognize the mechanism as correct and accept the causal inference as validated. The error is not in the biology. The error is in using accurate mechanistic knowledge to paper over the structural gap between $P(\text{HeartAttack} \mid \text{Aspirin} = 1)$ in the observational data and $P(\text{HeartAttack} \mid do(\text{Aspirin} = 1))$ for the intervention. The selection mechanism — the fact that aspirin-takers in the observational study self-selected in ways that may be independently associated with lower cardiac risk — has been silently assumed away.

What makes this failure especially dangerous is that it is more convincing than a correct hedge. A model that says "I cannot determine this from observational data" is transparent about its limitation. A model that says "mandating aspirin will reduce events by 30%, consistent with antiplatelet biology" has produced something that sounds like a second opinion from a knowledgeable analyst. It is not.

![Decision tree showing three failure modes. Rung 1 question: model succeeds. Rung 2 question: three branches — (1) correct hedge with...](images/10-chapter-llms-causal-reasoning-fig-01.png)
*Figure 10.1 — Decision tree showing three failure modes*

### The scoring rubric

Nilay's benchmark uses a four-level rubric. I want you to understand it mechanically, because you will apply it in the exercises.

| Score | Meaning |
|-------|---------|
| +2 | Correct epistemic answer: explicitly explains *why* the question is unanswerable from observational data |
| +1 | Correct direction, no structural hedge: gets the answer right but is overconfident |
| 0 | Confident wrong answer |
| −1 | Confident wrong answer plus a fabricated causal mechanism cited as justification |

The −1 case is not just wrong — it is wrong in a way that actively prevents the human from noticing the error. That is what makes it the failure mode that matters most in practice.

---

## Section 5: A Complete Walkthrough

I want to walk a single question through all three rungs, showing you at each step what the question is actually asking and what evidence would be needed to answer it.

**Starting question:** "Do students who attend smaller classes score higher on standardized tests?"

### Step 1: Classify the rung

The phrasing "who attend" is observational: students naturally sort into class sizes rather than being assigned. This is Rung 1. An LLM can answer this correctly — yes, the association is present and documented across multiple datasets. No structural machinery required. Score that response +2 if it hedges appropriately.

### Step 2: Upgrade to Rung 2

Rephrase: *If we enacted a policy reducing all class sizes by 5 students, what would happen to test scores?*

The do() operator is now implicit: we are fixing class size from outside the system, severing students' natural sorting into classes. An LLM asked this question will typically give a confident directional prediction: "test scores would likely improve." What it will not do is draw the relevant DAG and check it.

The relevant causal structure here involves district funding as a common cause. Wealthier districts have both smaller classes (more budget per student) and higher scores (more resources, more experienced teachers, more stability at home). The back-door path is:

$$\text{ClassSize} \leftarrow \text{DistrictFunding} \rightarrow \text{TestScores}$$

The valid adjustment set is {DistrictFunding}. The adjustment formula gives:

$$P(\text{TestScores} \mid do(\text{ClassSize} = c)) = \sum_f P(\text{TestScores} \mid \text{ClassSize} = c, \text{Funding} = f) \cdot P(\text{Funding} = f)$$

That formula is the correct answer to the Rung 2 question — not a directional prediction, but an identification strategy that requires conditioning on district funding to strip out the confounding. An LLM that gives "scores would likely improve" without this analysis has given a Rung 1 answer to a Rung 2 question.

### Step 3: Upgrade to Rung 3

Rephrase: *Lincoln Elementary had 22 students per class and scored at the 81st percentile. Would Lincoln's scores have been higher if it had had 16 students per class?*

This is Rung 3 — an individual-entity counterfactual. We are asking for Lincoln's potential outcome under a treatment it never received: $Y_{16}$ for an entity we observed at $X = 22$. The fundamental problem of causal inference applies. We observe one world for Lincoln, not both.

Answering this requires a structural model that specifies how test scores respond to class size at Lincoln specifically, plus an exogeneity assumption: that everything else about Lincoln — its funding, its teacher quality, its student demographics — would have been the same in a counterfactual world with smaller classes. That assumption may or may not hold. It cannot be tested from observational data. It requires scientific commitment.

The correct answer to the Rung 3 question is: *this cannot be determined from observational data alone.* A model that gives a quantitative prediction — "Lincoln's scores would have been approximately 3 percentile points higher" — is doing Rung 1 reasoning dressed in Rung 3 language.

### Evidence requirements at each rung

| Rung | Evidence Needed |
|------|----------------|
| 1 (Association) | Observational dataset with class size and test scores |
| 2 (Intervention) | Randomized experiment (lottery assignment to class size) or valid instrument, plus adjustment for district funding and other back-door paths |
| 3 (Counterfactual) | Individual potential outcomes — unobservable by definition; requires structural model plus exogeneity assumption about Lincoln's unobserved characteristics |

---

## Section 6: Detecting Trained Hedging vs. Structural Reasoning

Here is a subtlety that Nilay's benchmark surfaces, and I want to make sure you understand it before reading the results.

Large models — particularly the larger, instruction-tuned ones — have learned that epistemic hedges are valued responses to uncertain questions. They have been trained on human feedback that rewards caveats, qualifications, and acknowledgments of uncertainty. So when you ask a Rung 2 question, a well-tuned model will often say something like: "I cannot determine causation from observational data. This study shows a correlation, but confounding is possible."

That sounds like Rung 2 awareness. It might not be.

The test is prompt sensitivity. A model with genuine structural reasoning should give the same epistemic response regardless of *how* the Rung 2 question is phrased — whether you use formal do-notation, clinical language about "mandating," or casual language about "giving everyone aspirin." The causal structure is the same across all phrasings. A model that is reasoning about the structure should score consistently.

A model that is pattern-matching on surface features will score differently depending on whether "trigger words" appear. Words like "mandate," "force," "policy," and "do()" activate the hedge response. Words like "give everyone" or "what would happen if" in casual register may not.

Nilay's benchmark documents exactly this. I will not summarize the results here — that is what the case study is for. What I want you to understand is why prompt sensitivity is a diagnostic of the right thing: it separates "has learned to produce hedges when certain keywords appear" from "understands why this type of question requires a hedge." These produce the same output on a standard benchmark and different outputs on a sensitivity analysis.

![Two columns showing the same Rung 2 question in five surface phrasings — formal, semi-formal, informal, do-notation, policy-language. A...](images/10-chapter-llms-causal-reasoning-fig-02.png)
*Figure 10.2 — Two columns showing the same Rung 2 question in five surface phrasings*

---

## Section 7: What This Means for How You Build Systems

Understanding the failure mode is the beginning. Here is what you actually do with it.

### The routing architecture

The safest use of an LLM in a causal workflow is narration — taking the output of a structural analysis and translating it into language a decision-maker can act on. LLMs do this exceptionally well. Closing the gap between a regression table and a paragraph that a hospital administrator can use is not trivial, and a model can produce a first draft of that translation in seconds.

LLMs are also useful earlier, at the stage where no one is sure what the causal question is. A model can propose candidate confounders, suggest edges for a DAG under construction, identify relevant literature, and flag methodological concerns. This is Rung 1 reasoning in service of a Rung 2 workflow. The model is not performing structural inference. It is helping a human analyst think about what a structural model might look like. The analyst still draws the DAG. The analyst still validates the assumptions. The analyst still makes the causal claim.

The dangerous uses are the ones that look identical to the safe ones on the surface. Asking a model to summarize observational findings looks the same as asking it to predict the outcome of an intervention — both are natural-language queries about the same dataset. The difference is invisible in the interface. It is only visible if you are asking, before every query: which rung does this question live on?

The fix is architectural. Route by rung before routing to a tool.

```
[User Query]
      │
      ▼
[Rung Classifier]
      │
      ├──► Rung 1 ──► [LLM Response] ──► User
      │
      └──► Rung 2/3 ──► [Causal Model: DoWhy / DAGitty]
                               │
                        [Human Validation Node]
                               │
                        [LLM Narration of Result]
                               │
                             User
```

The routing step itself can be performed by an LLM — classifying a question by rung is a Rung 1 task. A model can learn to do this reliably. What it cannot do is then perform the structural inference that Rung 2 requires. The architecture assigns each responsibility to the tool that can actually discharge it.

### What the causal model box actually requires

The DoWhy box in that diagram is not magic. It requires a DAG specification — which variables exist, which edges connect them, and their directions. Here is what that looks like in practice:

```python
model = CausalModel(
    data=hospital_df,
    treatment='WaitTime',
    outcome='Satisfaction',
    graph='digraph {Staffing -> WaitTime; Staffing -> Satisfaction; WaitTime -> Satisfaction}'
)
```

The `graph` argument — `Staffing -> WaitTime; Staffing -> Satisfaction` — is a scientific claim about mechanism. It asserts that staffing levels cause wait times, and that staffing levels independently cause satisfaction. That string is not produced by pattern-matching on the data. It requires domain knowledge and willingness to be wrong in a checkable way.

An LLM can propose that string. It cannot certify it. Certification requires a person who understands the mechanism — the biology, the operations, the institutional logic — and is willing to stake a claim about what would happen if the system were perturbed. That is not a computational task. It is a scientific one.

### The human node is not passive

In the architecture above, the human validation node is not a supervisor watching the pipeline catch errors. It is where the DAG gets validated. This is the most important design decision in any causal AI system — not which model to use, not how to prompt it, but where in the pipeline human scientific judgment is required and whether the architecture actually routes to it.

The hospital's $2.3 million failure was not a technology failure. It was an architecture failure. The LLM was placed in the position of causal reasoning engine when it was built to be a pattern recognition and narration engine. The fix is not a better model. It is a better system.

---

## Section 8: Worked Example — Diagnosing a Model Response

Here is an exercise in applied classification. I will walk through it completely; you will do a version independently in the exercises.

**The scenario:** A study of 500 school districts finds that districts with higher per-pupil library spending have higher graduation rates ($r = 0.63$, $p < 0.001$). A policy analyst asks a language model: "Based on this study, if we increase library funding in all districts by $200 per student, what will happen to graduation rates?"

**Step 1: Classify the question.**

The phrase "if we increase" is a do() operator in disguise. The analyst is asking: $P(\text{GraduationRate} \mid do(\text{LibrarySpending} = \text{current} + \$200))$. This is Rung 2.

**Step 2: Identify the relevant causal structure.**

What are the plausible back-door paths from LibrarySpending to GraduationRate? The most obvious common cause is total district funding — wealthier districts spend more on libraries and also have higher graduation rates through multiple other mechanisms (teacher salaries, facilities, socioeconomic stability of the student population). The back-door path is:

$$\text{LibrarySpending} \leftarrow \text{TotalFunding} \rightarrow \text{GraduationRate}$$

There may be additional confounders (urbanicity, state-level education policy, demographic composition), but TotalFunding is the most structurally important. Conditioning on TotalFunding is the minimum requirement for valid identification.

**Step 3: Evaluate model responses.**

Response A: *"Based on the study, increasing library funding by $200 per student would likely improve graduation rates, consistent with the documented positive association between educational resources and student outcomes."*

Score: **0 or −1**. The model is answering the Rung 2 question with Rung 1 evidence. It gives a directional prediction ("would likely improve") without identifying TotalFunding as a confounder or acknowledging that the observational correlation cannot support an interventional claim. If it then cites a mechanism — "research shows that access to reading materials improves literacy, which increases graduation likelihood" — that is a fabricated mechanism response and scores −1.

Response B: *"The study shows a correlation between library spending and graduation rates, but I cannot conclude from this observational data that increasing library spending will cause graduation rates to rise. The association may be driven by total district wealth, which affects both library budgets and graduation outcomes through multiple pathways. To estimate the causal effect of the intervention, you would need to condition on total district funding (and other confounders) or, ideally, have experimental variation in library spending across otherwise comparable districts."*

Score: **+2**. This response identifies the specific confounding path, explains why the observational correlation cannot support the interventional claim, and specifies what additional evidence would be needed. That is structural reasoning made visible.

**Step 4: Design the sensitivity test.**

To check whether Response B reflects genuine structural reasoning or trained hedging, rephrase the question informally: "We're giving all districts an extra $200 per kid for books. Will more kids graduate?"

A model that scored +2 because it learned to hedge formal policy questions may now give a directional prediction without a hedge. That variance is the signal.

---

## A note about AI

This chapter is directly about whether the model can reason causally. The note examines the chapter's own subject applied to writing the chapter.

Where the model genuinely helps: producing the canonical examples of where LLMs succeed and fail at causal reasoning, with attention to the specific structure of each failure.

Where the model does damage: declaring that LLMs can or cannot reason causally. The question is contested in the literature and the model has a stake in the answer.

The rule: examples from the model; the verdict on LLM causal capability is for the field, not for the model.

---

## Exercises

### Warm-Up

**Exercise 1 (Rung Classification)**
Classify each question below as Rung 1, 2, or 3. For Rung 2 and 3 questions, state what additional information would be needed to answer them correctly.

a. "In this dataset, do patients who exercise more have lower blood pressure?"

b. "If a hospital mandates 30 minutes of daily exercise for all patients, will blood pressure fall?"

c. "Patient B exercises regularly and has normal blood pressure. Would Patient B have had hypertension if they had never exercised?"

d. "What is the correlation between neighborhood walkability scores and average resident BMI?"

e. "A city redesigns its streets to improve walkability. What will happen to BMI?"

*(For each Rung 2/3 question: name the most plausible confounder, draw the back-door path, and state the minimum adjustment set.)*

**Exercise 2 (Failure Mode Identification)**
A model is asked: "Studies show that people who drink red wine moderately have lower rates of heart disease. If a cardiologist advises all patients to drink one glass of red wine daily, what does the evidence predict?"

The model responds: "The evidence suggests moderate red wine consumption may reduce cardiac risk. The polyphenols in red wine, particularly resveratrol, have antioxidant properties that may protect arterial walls. Advising patients to drink one glass daily would likely produce similar benefits to those observed in the study."

Score this response using the rubric from Section 4. Identify specifically: (a) which rung the question lives on, (b) which rung the model answered, (c) whether a fabricated mechanism is present, and (d) what the correct +2 response would say.

### Application

**Exercise 3 (Designing an Adversarial Prompt)**
Take the following scenario: a dataset of 200 cities shows that cities with more public parks per capita have lower rates of obesity ($r = -0.58$, $p < 0.001$).

Write three versions of the same intervention question — one formal (policy language), one semi-formal (research language), one informal (casual language) — that all ask the same Rung 2 question but vary in surface phrasing. Your goal is to design a prompt battery that would expose a model relying on surface cues rather than structural reasoning. What difference in scores would you expect, and why?

**Exercise 4 (Constructing the Correct Answer)**
For the parks-and-obesity scenario in Exercise 3:

a. Draw the most plausible causal DAG. Include at least two confounders.

b. Identify the valid adjustment set using the backdoor criterion.

c. Write the adjustment formula using proper notation.

d. Write a +2 model response to your Rung 2 prompt — one that would correctly explain why the question cannot be answered from observational data alone and what evidence would be needed.

**Exercise 5 (Routing Architecture)**
A hospital analytics team uses an LLM to answer questions from clinical staff. Below are five queries submitted in one week:

1. "Which wards have the highest readmission rates this quarter?"
2. "If we implement mandatory discharge planning checklists, will readmissions fall?"
3. "Ward 7 had 12% readmissions last year. Would that have been lower if they had used the new protocol?"
4. "What are the most common diagnoses among readmitted patients?"
5. "Would patients who received the new protocol have had fewer complications if they had also received extended follow-up calls?"

For each query: classify the rung, route it appropriately (LLM vs. causal modeling tool), and — for Rung 2 and 3 queries — identify what the human validation node needs to supply before the causal analysis can proceed.

### Synthesis

**Exercise 6 (Full Pipeline Design)**
You are advising an education nonprofit that wants to evaluate whether their after-school tutoring program improves math scores. They have three years of observational data: which students attended tutoring, their math scores, their school, their grade level, and family income bracket.

Design a causal analysis pipeline for this organization. Your design should:

a. State the causal question at the appropriate rung.

b. Propose a DAG with at least three nodes beyond treatment and outcome, with justification for each edge.

c. Apply the backdoor criterion to identify a valid adjustment set.

d. Specify where in the pipeline an LLM would be useful and where it would be dangerous.

e. Describe what the human validation node needs to certify before the structural analysis proceeds.

f. Write the first two sentences of the LLM narration that would translate the analysis output for a program director who has never heard of a DAG.

### Challenge

**Exercise 7 (Benchmark Design)**
Design a three-prompt benchmark for a domain of your choosing (not hospital satisfaction, not aspirin, not class size — those have been worked to death). Your benchmark must include:

- One Tier 1 prompt where the correct answer is a well-hedged association
- One Tier 2 prompt where the correct answer is an explicit statement that the question cannot be answered from observational data, with a structural explanation
- One Tier 3 prompt where the correct answer requires invoking the fundamental problem of causal inference at the individual level

For each prompt: state what a +2 response looks like, what a −1 response looks like, and what surface feature a pattern-matching model might latch onto to give the wrong answer confidently.

Then: propose one prompt sensitivity variant for your Tier 2 prompt that you predict would produce a different score from a pattern-matching model than the original phrasing. Explain your prediction.

---

## Chapter Summary

Here is what you can now do that you could not before.

**You can classify causal questions by rung in real time.** When an analyst asks "what should we do about X?", you know to ask: is this a Rung 1 question dressed in Rung 2 language? The two look identical on the surface. They require categorically different machinery to answer.

**You understand why the failure is architectural.** LLMs are trained on next-token prediction over an observational corpus. That training objective produces excellent Rung 1 reasoning and no structural Rung 2 or Rung 3 reasoning. This is not a gap that more data fills. The corpus is observational by construction. Structural causal relationships are not transmitted in sentences — they are facts about the world that sentences point to.

**You can identify the three failure modes.** Rung 1 without a hedge. Confident Rung 2 answer from Rung 1 reasoning. Fabricated mechanism. The third is the most dangerous because it is most convincing — accurate background knowledge used to paper over a structural gap.

**You can design a routing architecture.** Rung 1 queries go to the LLM. Rung 2 and 3 queries route through an explicit causal modeling step, with a human validation node that certifies the DAG. The LLM narrates the output of the structural analysis. Each component does the thing it can actually do.

**The Feynman test for this chapter:** Can you explain, to someone who has never heard of Pearl's Ladder, why the hospital failed — and what a different architecture would have looked like? If yes, you have the chapter. If not, the gap is probably in Section 3 (the training objective argument) or Section 4 (the fabricated mechanism failure mode). Go back to whichever one feels slippery.

**The one idea that matters most:** The difference between $P(Y \mid X)$ and $P(Y \mid do(X))$ is not a notational subtlety. It is the difference between describing a pattern and predicting the outcome of an action. LLMs are very good at the first. They are not built to do the second. Every causal AI system that forgets this distinction is one confident wrong answer away from a $2.3 million mistake.

---

## Connections Forward

This chapter ends where the case studies begin. Nilay Raut's empirical investigation in the next chapter runs the benchmark I have described here against four real models. You now have the framework to read those results critically — to ask not just "did the model score well?" but "is that score the result of structural reasoning or trained surface-pattern hedging?" The prompt sensitivity analysis is the key diagnostic. Read that section first.

The broader question this chapter raises — what would a model that genuinely reasons at Rung 2 look like, and what would it take to build one — does not have a settled answer in the research literature as of this writing. The challenge problems in Exercise 7 point toward it. The research directions worth watching are: causal representation learning (can models learn structural relationships from intervention data rather than observational text?), neuro-symbolic architectures (can explicit causal graph modules be integrated with language model fluency?), and active learning paradigms that generate interventional training signal rather than observational. None of these are mature. All of them are active.

What is not uncertain is the diagnostic. You now know how to look at any causal claim produced by any language model and ask: which rung did this come from? Until the architecture changes, that question is your instrument.

---

## References

Hernán, M. A., & Robins, J. M. (2020). *Causal Inference: What If*. Chapman & Hall/CRC.

Kiciman, E., Ness, R., Sharma, A., & Tan, C. (2023). Causal Reasoning and Large Language Models: Opening a New Frontier for Causality. *arXiv preprint arXiv:2305.00050*.

Pearl, J., & Mackenzie, D. (2018). *The Book of Why: The New Science of Cause and Effect*. Basic Books.

Peters, J., Janzing, D., & Schölkopf, B. (2017). *Elements of Causal Inference: Foundations and Learning Algorithms*. MIT Press.

Zevcevic, M., Willig, M., Dhami, D. S., & Kersting, K. (2023). Causal Parrots: Large Language Models May Talk Causality But Are Not Causal. *arXiv preprint arXiv:2308.13067*.

---

*Chapter 11 is a standalone companion to the case study by Nilay Raut (Chapter 11, Case Studies). The theory spine for this book covers Chapters 1–9; this chapter applies spine concepts to the specific context of large language model evaluation. Readers who have not completed Chapters 1–9 should do so before reading this chapter.*

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Bernhard Schölkopf** has pushed the machine-learning community to take causal structure seriously — arguing that purely correlational models fail at out-of-distribution generalization in ways that explicit causal reasoning addresses. His work bridges deep learning and Pearl-style causal inference.

**Run this:**

```
Who is Bernhard Schölkopf, and how does his work on causal machine learning connect to the LLM causal reasoning we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Bernhard Schölkopf"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to explain why purely associational ML models fail under distribution shift — using a specific example.
- Ask it to compare Schölkopf's causal-ML approach with the "scaling laws" view of LLM capability.

What changes? What gets better? What gets worse?

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 10.1 — Decision tree showing three failure modes

Create a standalone D3 v7 HTML figure for "Decision tree showing three failure modes". Use a horizontal process diagram with 4 to 5 ordered stages with directed connectors. Marks: rectangular stage nodes and arrow connectors. Channels: position for sequence or category, length for quantitative emphasis when bars are used, color for the primary highlighted item only, and direct text labels for accessibility. Use a zero baseline for quantitative bars. Include title, desc, role="img", aria-labelledby, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Deliver as one HTML file with inline CSS and the D3 7.9.0 CDN.

> Reference implementation: `d3/10-chapter-llms-causal-reasoning-fig-01.html`

---

### Figure 10.2 — Two columns showing the same Rung 2 question in five surface phrasings

Create a standalone D3 v7 HTML figure for "Two columns showing the same Rung 2 question in five surface phrasings". Use a horizontal bar chart with 5 labeled categories with approximate values from 0 to 100. Marks: bars or rectangular panels, direct labels, and concise value labels. Channels: position for sequence or category, length for quantitative emphasis when bars are used, color for the primary highlighted item only, and direct text labels for accessibility. Use a zero baseline for quantitative bars. Include title, desc, role="img", aria-labelledby, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Deliver as one HTML file with inline CSS and the D3 7.9.0 CDN.

> Reference implementation: `d3/10-chapter-llms-causal-reasoning-fig-02.html`
