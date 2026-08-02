# Chapter 15: LLMs for Causal Variable Identification

## TL;DR

- This chapter gives a working overview of LLMs for Causal Variable Identification, focusing on the ideas a reader needs before moving to the next chapter.
- The chapter moves through From Data Dictionaries to Draft DAGs, Learning Objectives, Opening: Dr. Osei's Spreadsheet, Concept 1: What an LLM Actually Does When It Reads a Data Dictionary, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

### From Data Dictionaries to Draft DAGs

*By Trimbkeshwar*

---

## Learning Objectives

By the end of this chapter, you should be able to:

1. **Distinguish** distributional plausibility from causal validity, and explain why an LLM that sounds causally correct is not the same as one that *is* causally correct
2. **Classify** LLM capabilities on Pearl's three-rung causal hierarchy — and identify precisely which rung the LLM is operating on when it proposes a variable or an edge
3. **Apply** a five-stage pipeline to extract candidate causal variables from a data dictionary, propose draft DAG edges, and produce a validated causal graph
4. **Diagnose** the four structural failure modes in LLM-proposed DAGs — hallucinated edges, reversed directions, missing confounders, and collider conditioning — using the three-question Human Decision Node protocol
5. **Redesign** a broken DAG by detecting which failure mode occurred and correcting the causal structure before estimation

**Prerequisites:** Chapters 2–5 (causal diagrams, confounding, the backdoor criterion, matching). You need to know what a DAG is, what a confounder is, and what it means to condition on a collider. This chapter takes those tools and shows you what happens when a language model tries to do your job for you.

**Where this fits:** The theory spine taught you the formal machinery of causal graphs. This chapter teaches you the workflow of *building* one from messy real-world inputs — and where that workflow breaks down if you trust the wrong tool at the wrong step.

---

## Opening: Dr. Osei's Spreadsheet

Here is the actual problem that makes causal inference hard in practice.

Dr. Amara Osei is staring at a spreadsheet. Two hundred and fourteen columns. Each one a variable in the CMS Hospital Readmissions Reduction Program dataset — patient age, primary diagnosis code, length of stay, discharge disposition, payer type, attending physician specialty, number of prior admissions, lab values at discharge, medication counts, zip code, and on and on, deep into the weeds of American hospital bureaucracy.

Her task is straightforward to state and brutal to execute: build a causal model that estimates the effect of a post-discharge nursing intervention on thirty-day readmission rates. To do that, she needs a DAG. To build the DAG, she needs to decide which of those 214 variables are confounders, which are mediators, which are colliders, and which are irrelevant. She needs to draw the arrows. She needs to get the arrows right.

If you have never sat with a data dictionary and tried to do this by hand, the difficulty is hard to appreciate. A data dictionary is typically a document — sometimes a spreadsheet, sometimes a PDF maintained by someone who left the organization three years ago — that lists each variable along with a short description, its data type, and perhaps a note about collection. In principle, this contains enough information to begin reasoning about causal structure. In practice, the descriptions are inconsistent. Some variables get a sentence; others get a single word. Relationships between variables are implied, never stated. The analyst must read between the lines, summon domain knowledge, make judgment calls, and keep a mental map of a graph that quickly grows too complex to hold in working memory.

Dr. Osei estimates it will take her three weeks of full-time effort to review the dictionary, consult the clinical literature, interview the physicians, and produce a defensible DAG. Her grant timeline gives her four days.

![A representative data dictionary showing inconsistent variable descriptions. Patientage gets a full sentence. LOS gets "Stay length....](images/13-llm-causal-variable-identification-fig-01.png)
*Figure 13.1 — representative data dictionary showing inconsistent variable descriptions*

This is the pain point. Not an abstract one — a real, recurring bottleneck in applied causal inference. The conceptual machinery of causal modeling has matured dramatically over the past two decades. The statistical estimators are well-developed and computationally tractable. What remains stubbornly manual, stubbornly slow, and stubbornly error-prone is the step that precedes all of it: identifying and enumerating the causal variables, deciding what goes in the graph, and drawing the first draft of the arrows.

Large Language Models offer a seductive promise here. An LLM can read a data dictionary. It can parse variable names and descriptions. It can draw on vast pre-trained knowledge to propose which variables are likely causes, effects, confounders, or colliders. It can, in minutes, produce a draft DAG that would take a human analyst days or weeks.

The promise is real. The danger is equally real. This chapter teaches you how to use LLMs to accelerate the first step of causal modeling — and, more importantly, teaches you exactly where you must stop trusting them and start thinking for yourself.

---

## Concept 1: What an LLM Actually Does When It Reads a Data Dictionary

### Strip Away the Mysticism

Before you can use LLMs responsibly in a causal pipeline, you need a clear picture of what actually happens when you feed one a data dictionary and ask it to propose causal relationships. The mechanism is specific. It is worth understanding precisely.

When an LLM reads a variable entry — say, `LOS: Length of stay in days, integer, range 0–365` — it converts each word into a high-dimensional numerical vector called an **embedding**. These vectors are not random. They are learned from billions of words of training text. Words that appear in similar contexts during training end up as vectors that are close together in this high-dimensional space.

"Length of stay" and "readmission" end up near each other in this space because they co-occur frequently in clinical research papers. "Discharge protocol" and "thirty-day outcome" end up near each other for the same reason. When you ask the model to propose causal relationships among the variables, it is doing something specific: it is finding pairs of variable descriptions whose embeddings are close to each other *and* that appeared near causal language in the training data — words like "causes," "leads to," "increases risk of." The model retrieves these associations and generates text that arranges them into causal-sounding sentences.

Here is the critical distinction you must hold in your mind for the rest of this chapter:

> The LLM proposes edges based on **distributional plausibility**. Causal inference requires **causal validity**. These are not the same thing.

**Distributional plausibility** means the proposed relationship frequently appears in the kind of text the model was trained on — it *sounds* like the sort of thing a clinical researcher would write. **Causal validity** means the relationship correctly represents the data-generating process in the real world — it is actually true. These two properties overlap frequently, which is what makes LLMs useful. But they diverge in ways that are silent, systematic, and devastating to downstream estimation.

![Two overlapping circles. Left circle: distributional plausibility. Right circle: causal validity. Overlap region (useful): age →...](images/13-llm-causal-variable-identification-fig-02.png)
*Figure 13.2 — Two overlapping circles*

### Where LLMs Sit on Pearl's Causal Hierarchy

You know Pearl's three rungs from Chapter 1. They are worth revisiting now, because placing LLMs precisely on this ladder tells you exactly what they can and cannot do for causal modeling.

**Rung 1 — Association:** "What variables co-occur?" An LLM can answer this reliably. Co-occurrence is exactly what its training data encodes. If two variables frequently appear together in clinical literature, the LLM will report that they are related. This is pattern retrieval, and LLMs are extraordinarily good at it.

**Rung 2 — Intervention:** "What happens if we intervene on $X$?" An LLM can *attempt* this, but its answers are extrapolations from Rung 1 patterns, not genuine interventional reasoning. When the LLM proposes `intervention_received → readmitted_30d`, it is not reasoning about what would happen if you forced every patient to receive the intervention. It is reporting that, in its training data, descriptions of discharge interventions frequently co-occur with descriptions of reduced readmission. These are associational echoes dressed in causal language.

**Rung 3 — Counterfactual:** "What would have happened if this specific patient had *not* received the intervention?" An LLM cannot answer this at all. Counterfactual reasoning requires a complete structural causal model and the ability to replay a specific observation under different conditions. No amount of distributional pattern-matching can produce this.

The pipeline in this chapter asks the LLM to do Rung 2 work — proposing causal directions between variables — using Rung 1 capabilities. The LLM can tell you which variables travel together in text. It cannot tell you which variables actually cause which. The Human Decision Node exists to bridge that gap.

### A Common Misconception

Before moving on: some analysts trust HIGH-confidence LLM proposals and scrutinize only MEDIUM and LOW ones. This is backwards. Confidence in an LLM's output is a function of *distributional frequency* — how often the proposed relationship appeared in training text — not epistemic certainty about the causal structure. An LLM will propose `age → readmission` with HIGH confidence because that relationship appears in thousands of clinical papers. It will also propose `zip_code → infection_rate` with HIGH confidence for the same reason, even though zip code is a proxy, not a cause.

Validate HIGH-confidence edges first, not last. They are the ones most likely to create the false impression that scrutiny is unnecessary.

---

## Concept 2: The Four Failure Modes

The divergence between distributional plausibility and causal validity manifests in four characteristic failure modes. You need to know all four before you write a single line of pipeline code, because recognizing them is the core skill this chapter develops.

The history of applied statistics shows what is at stake. In 1973, UC Berkeley was accused of gender discrimination in graduate admissions based on aggregate data showing women were admitted at lower rates than men. When statisticians examined the data department by department, the pattern reversed — women were admitted at slightly *higher* rates within most departments, but they had applied disproportionately to more competitive ones. The aggregate data told a causal story (gender causes rejection) that was not just wrong but directionally opposite to the truth. The confounding variable — department choice — was hiding in plain sight.

In the 1990s, the Nurses' Health Study reported that hormone replacement therapy reduced cardiovascular risk in postmenopausal women. Millions of prescriptions followed. Then the Women's Health Initiative randomized controlled trial revealed the opposite: HRT *increased* cardiovascular risk. The observational estimate had been biased by an unmeasured confounder — healthy user bias. Women who chose to take HRT were systematically healthier than those who did not, and that health difference, not the hormone therapy, explained the apparent protective effect.

These are not ancient history. They are the kind of errors an LLM-assisted pipeline can reproduce at scale if the human analyst does not intervene. Here are the four specific mechanisms.

![Three-panel diagram showing structural failure modes. Panel 1 — hallucinated edge: zip code → infection rate, with annotation "proxy,...](images/13-llm-causal-variable-identification-fig-03.png)
*Figure 13.3 — Three-panel diagram showing structural failure modes*

### Failure Mode 1: Hallucinated Edges

The LLM proposes a causal link between two variables that does not exist in reality.

Given a data dictionary with `patient_zip_code` and `infection_rate`, the model may propose that zip code causes infection rate. In the training data, research papers frequently discuss geographic variation in infection rates, so the co-occurrence is strong. But zip code does not cause infection — it is a proxy for a cluster of socioeconomic and environmental factors (housing density, air quality, access to healthcare) that are the actual causes.

To see why this matters for identification: socioeconomic status causes both zip code (people sort into neighborhoods by income) and infection rate (through healthcare access and housing quality). The correct DAG routes the causal pathway through SES: `SES → zip_code` and `SES → healthcare_access → infection_rate`. If you instead include a direct `zip_code → infection_rate` edge, you have introduced a shortcut that collapses the mediated pathway. Conditioning on zip code now partially blocks the causal pathway through SES without fully adjusting for the confounding — leaving you with an estimate that is neither cleanly causal nor cleanly confounded.

### Failure Mode 2: Reversed Causal Direction

The LLM proposes that $A$ causes $B$ when, in reality, $B$ causes $A$.

Consider `patient_satisfaction_score` and `LOS`. An LLM may propose that satisfaction causes length of stay (happy patients leave sooner). Domain knowledge tells a different story: length of stay *influences* satisfaction (patients stuck in the hospital for extended periods report lower satisfaction). If you accept the LLM's reversal and condition on satisfaction as a confounder, you have conditioned on a *mediator* — a textbook form of overcontrol bias that will attenuate your effect estimate toward zero.

This failure is particularly insidious because both directions are distributionally plausible. The LLM cannot tell them apart. The Berkeley admissions case is a vivid real-world instance: an LLM reading a data dictionary with variables `gender`, `department`, and `admission_decision` could easily propose `gender → admission_decision` as a direct edge. The subtlety — that the causal effect is mediated and confounded by departmental choice — requires structural reasoning that distributional pattern-matching cannot provide.

### Failure Mode 3: Missing Confounders

The LLM fails to propose a variable that is a common cause of both the treatment and the outcome. This happens most often when the confounding variable is simply not in the data dictionary.

Suppose your dictionary includes `intervention_received` and `readmitted_30d`, but no variable for illness severity. The LLM cannot propose what it cannot see. But severity is a classic confounder: sicker patients are both more likely to be flagged for the intervention *and* more likely to be readmitted. Omitting it leaves a back-door path open.

The HRT reversal is the canonical demonstration at population scale. The Nurses' Health Study's DAG was missing a node — healthy user bias — and that missing node rendered the causal estimate not just imprecise but directionally wrong. When the Women's Health Initiative RCT randomized treatment assignment, the effect reversed. An LLM parsing the observational study's data dictionary would have had no way to propose "healthy user bias" as a variable. It was never collected, never named, never appeared in the dictionary.

### Failure Mode 4: Collider Bias

The LLM proposes conditioning on a variable that is a common *effect* of both the treatment and the outcome — a collider.

Consider `patient_satisfaction` that is caused by both `intervention_received` (patients who receive a follow-up call report higher satisfaction) and `readmitted_30d` (patients who are readmitted report lower satisfaction). Satisfaction has two causes: treatment and outcome. It is a collider. If the LLM proposes it as a confounder and you condition on it, you have opened a non-causal path between treatment and outcome, introducing a spurious association that did not exist in the unconditional data.

LLMs are particularly prone to proposing collider conditioning because satisfaction scores are frequently described as "control variables" in the training data. The label "control variable" is a distributional echo from papers that conditioned on them without checking whether they were confounders or colliders.

**The underlying asymmetry you must remember:** Conditioning on a confounder *closes* a spurious back-door path — it removes confounding. Conditioning on a collider *opens* a spurious path — it *introduces* confounding that did not previously exist. Both operations look identical in code. They have opposite causal consequences.

None of these failures announce themselves. A DAG with a hallucinated edge looks exactly like a DAG with a valid edge. A reversed arrow is graphically identical to a correct one. A missing confounder is, by definition, absent from the graph. The LLM will present its proposed DAG with the same confident, fluent prose regardless of whether the DAG is valid or catastrophically wrong. This is not a bug in LLMs. It is a fundamental property of how they generate text.

The burden of validation falls entirely on you.

---

## Concept 3: The Five-Stage Pipeline

### Before You Build Anything: Stage 0

Before you feed anything to an LLM, answer a prior question: should you use this pipeline at all?

The pipeline is designed for a specific class of problems: large variable sets (50+ variables), domains well-represented in published literature, and analysts who have enough domain knowledge to validate proposals but not enough time to enumerate variables from scratch.

Three conditions where you should skip the pipeline and draw the DAG by hand:

First, when the variable count is small — fewer than about 20 variables. The overhead of running the pipeline is not worth the gain. Second, when the domain is novel or poorly studied. LLM proposals are only as good as the literature they were trained on; a domain with no published causal literature will produce proposals that are essentially random. Third, when you are the deep domain expert who can draw a better first-draft DAG in an hour than the LLM can produce in a minute. The pipeline accelerates variable enumeration for generalists. Specialists do not need it.

### The Pipeline Architecture

![Five-stage pipeline with automation boundary clearly marked. Stages 1–3 (Ingestion, Extraction, Edge Proposal) are LLM-automated. Stage...](images/13-llm-causal-variable-identification-fig-04.png)
*Figure 13.4 — Five-stage pipeline with automation boundary clearly marked*

The pipeline is sequential in backbone but iterative in practice. When Stage 4 reveals errors in Stage 2 or 3, you loop back. The stages are non-negotiable in the sense that you must not skip any of them — not in the sense that you traverse them exactly once.

Two warnings before you run anything.

**Non-determinism.** LLMs are stochastic — the same prompt may produce different outputs across runs. Run the extraction and edge proposal stages at least three times. Edges that appear in all runs are stable proposals. Edges that appear in only one run deserve extra scrutiny at the Human Decision Node. The consensus set is more reliable than any single run's output.

**Anchoring bias.** When you evaluate LLM-proposed edges, you are psychologically anchored to the proposals in front of you. Edges the LLM did not propose are harder to think of — not because they are less important, but because they were not presented. Perform an independent brainstorming session *before* looking at the LLM's edge proposals. Write down the confounders you expect to see. Then check which ones the LLM missed.

### Stage 1: Ingestion

The ingestion prompt is the most important single piece of text in the entire pipeline. Three design choices matter:

```
SYSTEM PROMPT:
You are a causal inference research assistant. Your task is to:
1. List every variable in the dictionary.
2. For each variable, propose a causal role from:
   [treatment, outcome, confounder, mediator, collider, instrument, irrelevant]
3. Provide a one-sentence justification per variable.
4. Return as a JSON array.

CONSTRAINTS:
- Only list variables in the dictionary. Do NOT invent variables.
- If uncertain, assign "uncertain" and explain why.
- Do not propose causal directions at this stage.
```

**The anti-hallucination constraint** is not optional. Without it, LLMs propose phantom variables — composite constructs like `frailty_index` that sound clinically reasonable but correspond to no column in the data. In testing across GPT-4, Claude, and Gemini Pro using five real clinical data dictionaries, hallucinated variables appeared in approximately 30–50% of runs without the constraint, dropping to 8–15% with it. You still need to check programmatically (Stage 2 shows how), but the constraint reduces the false-positive rate dramatically.

**Role separation before edge proposal** produces cleaner output. Asking the LLM to classify roles and propose edges simultaneously encourages shortcuts — it starts proposing edges while still deciding roles, and the two tasks contaminate each other.

**The "uncertain" category** is the most important output in the extraction stage. It flags exactly the cases where human expertise is most needed. Pay attention to uncertain entries — they are the LLM telling you it doesn't know.

### Stage 2: Variable Extraction

The extraction stage produces a structured table of candidate variables with proposed roles and justifications. Here is what that looks like for the readmissions dataset:

| Variable Name | Proposed Role | Justification |
|---|---|---|
| `intervention_received` | treatment | The intervention whose causal effect is being estimated |
| `readmitted_30d` | outcome | The primary outcome of interest |
| `patient_age` | confounder | Age affects both intervention targeting and readmission risk |
| `LOS` | mediator | The intervention may affect readmission partly through length of stay |
| `num_prior_admissions` | confounder | Prior admission history predicts both intervention targeting and readmission |
| `primary_dx_code` | confounder | Diagnosis determines both treatment protocols and readmission risk |
| `payer_type` | confounder | Payer type correlates with access to post-discharge resources |
| `patient_zip_code` | uncertain | May proxy for socioeconomic factors, but direct causal role is unclear |

Before proceeding to Stage 3, run the hallucination check programmatically:

```python
llm_variables = {v["variable_name"] for v in llm_output}
actual_columns = set(dataframe.columns)
hallucinated = llm_variables - actual_columns
if hallucinated:
    print(f"HALLUCINATED VARIABLES DETECTED: {hallucinated}")
```

Any variable in `hallucinated` cannot be in your DAG. Remove it now, before it contaminates the edge proposals.

### Stage 3: Edge Proposal

The edge proposal stage asks the LLM to propose directed edges between the variables it classified in Stage 2. The output is a table of source → target pairs with justifications and confidence levels:

| Source | Target | Justification | Confidence |
|---|---|---|---|
| `patient_age` | `readmitted_30d` | Older patients have higher vulnerability to readmission | HIGH |
| `patient_age` | `intervention_received` | Older patients may be preferentially targeted | MEDIUM |
| `intervention_received` | `readmitted_30d` | The causal effect of interest | HIGH |
| `LOS` | `readmitted_30d` | Longer stays may indicate sicker patients | MEDIUM |
| `primary_dx_code` | `LOS` | Diagnosis determines expected length of stay | HIGH |
| `primary_dx_code` | `readmitted_30d` | Certain diagnoses have higher readmission rates | HIGH |
| `payer_type` | `intervention_received` | Insurance may determine eligibility | MEDIUM |
| `num_prior_admissions` | `readmitted_30d` | Prior admissions are a strong predictor | HIGH |

Do not act on this table yet. Stage 4 is where science begins.

### Stage 4: The Human Decision Node

This is where the pipeline stops being automated and starts being science. For each proposed edge, answer three questions in order.

![Three-question validation flowchart. Input: proposed edge A → B. Q1: Is there a plausible causal mechanism? If No → REJECT. If Yes → Q2....](images/13-llm-causal-variable-identification-fig-05.png)
*Figure 13.5 — Three-question validation flowchart*

**Question 1: Is there a plausible causal mechanism?** Not a correlation. A mechanism — a physical, biological, institutional, or behavioral pathway by which changing the source variable would change the target variable, holding all else fixed. "These variables are correlated in the literature" is not a mechanism. "Discharge follow-up calls allow nurses to identify early warning signs and redirect patients to outpatient care, reducing the probability of a return admission" is a mechanism.

**Question 2: Is the direction correct?** For every edge, ask: could the arrow run the other way? If yes, which direction does domain knowledge support? This question catches Failure Mode 2. It requires you to actively consider the reverse direction, not just accept the one the LLM proposed.

**Question 3: What is missing?** For every pair of variables connected by an edge, ask: is there a third variable that causes both? If yes, is that variable in the graph? This question catches Failure Mode 3. It is the hardest question to answer well, because missing confounders are by definition absent from the proposals you are looking at.

Here is what the validation walkthrough looks like for three edges from the readmissions dataset:

**Edge: `patient_age → intervention_received` (MEDIUM confidence)**
Mechanism: risk-scoring protocols weight age heavily when targeting patients for follow-up calls. Direction: correct — the intervention cannot change the patient's age. Missing: possibly unmeasured comorbidity burden, which increases with age and also affects readmission. Decision: ACCEPT, flag potential residual confounding from comorbidity.

**Edge: `LOS → readmitted_30d` (MEDIUM confidence)**
Mechanism: ambiguous. Longer stays could reflect sicker patients who are also more likely to be readmitted — but in that case, both LOS and readmission are likely downstream consequences of underlying severity, not causes of each other. The proposed edge collapses a mediated pathway. Decision: REVISE. Remove the direct edge. Add `severity → LOS` and `severity → readmitted_30d`. Route through the actual mechanism.

**Edge: `payer_type → intervention_received` (MEDIUM confidence)**
Mechanism: some discharge programs are funded by specific payers and are only available to patients with that insurance. Direction: correct — the intervention doesn't change the payer type. Missing: payer type is also associated with socioeconomic status, which likely has its own path to readmission. Decision: ACCEPT. Add edge `payer_type → readmitted_30d` that the LLM did not propose.

Notice what happened in the `payer_type` evaluation: the LLM proposed one edge and the human added another. This is the pipeline working correctly. The LLM found the edge that is well-documented in the literature. The human found the edge that required reasoning about the mechanism.

### Stage 5: DAG Finalization

After the Human Decision Node, encode the validated DAG in code and verify acyclicity:

```python
import networkx as nx

dag = nx.DiGraph()
dag.add_edge("patient_age", "intervention_received")
dag.add_edge("patient_age", "readmitted_30d")
dag.add_edge("severity", "intervention_received")      # added by human
dag.add_edge("severity", "readmitted_30d")             # added by human
dag.add_edge("intervention_received", "readmitted_30d")
dag.add_edge("primary_dx_code", "LOS")
dag.add_edge("primary_dx_code", "readmitted_30d")
dag.add_edge("primary_dx_code", "intervention_received")
dag.add_edge("num_prior_admissions", "readmitted_30d")
dag.add_edge("num_prior_admissions", "intervention_received")
dag.add_edge("payer_type", "intervention_received")
dag.add_edge("payer_type", "readmitted_30d")           # added by human
dag.add_edge("discharge_disposition", "readmitted_30d")
dag.add_edge("intervention_received", "discharge_disposition")

# Verify acyclicity — a cycle means you have a logical contradiction in the DAG
assert nx.is_directed_acyclic_graph(dag), "Cycle detected — check for feedback loops"
```

![Before/after comparison. LLM Draft DAG: includes LOS → readmitted30d (removed), satisfaction → readmitted30d (removed), missing severity...](images/13-llm-causal-variable-identification-fig-06.png)
*Figure 13.6 — Before/after comparison*

The validated DAG is not the LLM's DAG. It is your DAG — one that you can defend edge by edge, name the mechanism for, and explain to a reviewer. The LLM produced the raw material. You produced the causal model.

---

## Integration: What Breaks When You Skip Stage 4

Understanding that the Human Decision Node matters is different from *feeling* how much it matters. This section makes the consequences of skipping it visceral. You will produce bias, measure it, and see exactly how a plausible-looking DAG can destroy a causal estimate.

The simulation uses a known true causal effect of $-0.3$ log-odds — the intervention reduces readmission probability, and you know the exact magnitude. Everything that follows is about how far from $-0.3$ you land when the DAG is wrong.

```python
import numpy as np, pandas as pd
np.random.seed(42); n = 5000

severity = np.random.normal(0, 1, n)
patient_age = np.random.normal(65, 10, n)
age_std = (patient_age - 65) / 10

p_treat = 1 / (1 + np.exp(-(0.5 * severity + 0.3 * age_std)))
intervention = np.random.binomial(1, p_treat)

p_readmit = 1 / (1 + np.exp(-(
    0.5 * severity + 0.2 * age_std - 0.3 * intervention)))
readmitted = np.random.binomial(1, p_readmit)

satisfaction = (0.4 * intervention - 0.5 * readmitted
                + np.random.normal(0, 0.5, n))

df = pd.DataFrame({
    "severity": severity, "patient_age": patient_age,
    "intervention_received": intervention,
    "readmitted_30d": readmitted, "satisfaction": satisfaction
})
```

Notice what the data-generating process encodes. Severity causes both treatment assignment and readmission — it is the confounder. The intervention has a true effect of $-0.3$. Satisfaction is caused by both treatment and readmission — it is the collider. These facts are known to you because you wrote the simulation. In real data, you never know them. That asymmetry is the point.

### Part A: The Correct DAG

```python
import statsmodels.api as sm

X_correct = df[["intervention_received", "severity", "patient_age"]].astype(float)
X_correct = sm.add_constant(X_correct)
model_correct = sm.Logit(df["readmitted_30d"].astype(float), X_correct).fit()
print(model_correct.summary())
```

The estimated coefficient on `intervention_received` should be close to $-0.3$. This is your baseline — the answer you get when the DAG is right.

### Part B: The Broken DAG (Missing Confounder)

```python
X_broken = df[["intervention_received", "patient_age"]].astype(float)
X_broken = sm.add_constant(X_broken)
model_broken = sm.Logit(df["readmitted_30d"].astype(float), X_broken).fit()
print(model_broken.summary())
```

Severity is gone. You omitted it because the LLM couldn't propose it — it wasn't in the data dictionary. The estimated coefficient on `intervention_received` will be attenuated toward zero, typically landing around $-0.18$ to $-0.22$. You have the right sign. But the magnitude is wrong by 25–50%.

For a policymaker, this is the difference between "the program works, fund it" and "the program barely works, cut it." The LLM gave you a confident-sounding DAG. The DAG gave you the wrong answer.

### Part C: The Reversal Stress Test

Now suppose the LLM reversed the severity arrow. Instead of `severity → intervention_received` (severity causes targeting), the LLM proposed `intervention_received → severity` (the intervention affects severity). Under this incorrect DAG, severity looks like a mediator — something downstream of treatment. You follow the rule: don't condition on mediators. You drop severity.

Run the same model as Part B. The result is identical.

**This is the pedagogical punchline.** Two different LLM failure modes — missing confounder and reversed arrow — produce exactly the same statistical consequence. The pipeline does not care *why* the confounder was excluded. It only cares that it was. Missing it through ignorance and excluding it through a reasoning error are indistinguishable in the output.

### Part D: The Collider Stress Test

```python
X_collider = df[["intervention_received", "severity", "patient_age",
                  "satisfaction"]].astype(float)
X_collider = sm.add_constant(X_collider)
model_collider = sm.Logit(df["readmitted_30d"].astype(float), X_collider).fit()
print(model_collider.summary())
```

You added satisfaction because the LLM proposed it as a control variable and it sounded reasonable. Satisfaction correlates with readmission. It looks like a confounder. It is a collider.

Conditioning on satisfaction biases the estimate in a *different direction* from the omitted-confounder case — the effect estimate is now too large, typically around $-0.35$. You overcorrected past the truth. The direction of bias from collider conditioning depends on the structure of the graph; what matters is that it is nonzero and not predictable without the DAG.

![Bias comparison bar chart. True effect: −0.30. Correct DAG: −0.29. Broken DAG (severity omitted): −0.18. Collider DAG (+ satisfaction):...](images/13-llm-causal-variable-identification-fig-07.png)
*Figure 13.7 — Bias comparison bar chart*

### The E-Value: Quantifying What You Can't See

For the omitted-confounder case, you can quantify how strong an unmeasured confounder would have to be to explain away the observed effect — even when you cannot measure it directly. The E-value (VanderWeele & Ding, 2017) gives you this bound.

For an observed risk ratio of $RR_{obs}$, the E-value is:

$$E = RR_{obs} + \sqrt{RR_{obs}(RR_{obs} - 1)}$$

An unmeasured confounder would have to have an association with both treatment and outcome of at least $E$ on the risk ratio scale to fully explain away the observed effect. Large E-values indicate robust findings. Small E-values indicate findings that could be explained by modest unmeasured confounding.

For the omitted-severity case: the observed effect in the broken model corresponds to a risk ratio of approximately 0.84. The E-value is approximately 1.47. This means an unmeasured confounder would need associations of 1.47 or higher on both the treatment and outcome sides to fully explain away the estimate — a modest threshold. The finding is not robust to unmeasured confounding of that magnitude.

---

## Exercises

### Warm-Up

These exercises check mechanical understanding. Each should take 5–10 minutes.

**W1.** *Tests Objective: Classify LLM capabilities on Pearl's hierarchy*

For each of the following questions, state which rung of Pearl's causal hierarchy it belongs to and whether an LLM can answer it reliably. Justify each answer in one sentence.

(a) "Which variables in this dataset co-occur with hospital readmission in the published literature?"
(b) "If we force all patients to receive the discharge intervention, what will happen to thirty-day readmission rates?"
(c) "Would this specific patient have been readmitted if she had not received the intervention?"

**W2.** *Tests Objective: Distinguish distributional plausibility from causal validity*

An LLM proposes the edge `hospital_bed_count → patient_mortality` with HIGH confidence. Write a three-sentence evaluation using the three-question Human Decision Node protocol: (1) Is there a plausible mechanism? (2) Is the direction correct? (3) What common causes might be missing?

**W3.** *Tests Objective: Diagnose failure modes*

Classify each of the following as Failure Mode 1 (hallucinated edge), 2 (reversed direction), 3 (missing confounder), or 4 (collider conditioning). Explain your classification in one sentence each.

(a) The LLM proposes `patient_satisfaction → LOS` as a confounder.
(b) The LLM proposes `frailty_index → readmission`, but `frailty_index` is not in the dataset.
(c) The LLM's DAG includes `intervention_received` and `readmitted_30d` but omits illness severity entirely.
(d) The LLM proposes conditioning on `discharge_disposition`, which is caused by both the intervention and the outcome.

---

### Application

These exercises require applying the concepts to problems that differ from the worked examples. Each should take 15–25 minutes.

**A1.** *Tests Objective: Apply the five-stage pipeline*

You are building an LLM-assisted causal inference pipeline to estimate the causal effect of urban green space on childhood asthma rates. You have a dataset with 80 variables and a data dictionary.

(a) Perform the Stage 0 feasibility assessment. Should you use the pipeline? Justify your answer against the three criteria.
(b) Write the Stage 1 ingestion prompt. Include the anti-hallucination constraint and the role taxonomy.
(c) Name at least three variables the LLM would likely propose with HIGH confidence, and three variables it would likely miss entirely. For each missed variable, explain why the LLM cannot propose it.
(d) For each of your three proposed variables, apply the three-question Human Decision Node protocol. Accept, revise, or reject each.

**A2.** *Tests Objective: Redesign a broken DAG*

A data dictionary contains 150 variables. You run the LLM extraction pipeline and receive 158 proposed variables.

(a) Describe the diagnostic steps you would take to identify and handle the discrepancy.
(b) What are the two most likely causes of the extra variables?
(c) Write the Python code to programmatically identify hallucinated variables given `llm_output` (a list of dicts with key `"variable_name"`) and `dataframe` (a pandas DataFrame). What should you do with each detected hallucination?

**A3.** *Tests Objective: Diagnose failure modes from simulation output*

Run Parts A–D of the simulation in the Integration section. Record the coefficient estimates for `intervention_received` in each model.

(a) How large was the bias from omitting the confounder? Express it as both an absolute difference in log-odds and as a percentage of the true effect.
(b) How did the collider bias differ in direction and magnitude from the omitted-confounder bias?
(c) Would either level of bias change a policy decision about whether to fund the discharge intervention program? Under what assumptions?

---

### Synthesis

These exercises require combining multiple concepts from the chapter.

**S1.** *Tests Objectives: Apply pipeline; diagnose failure modes; redesign broken DAG*

You have a validated DAG with 12 variables and 28 edges. You discover that removing a single edge changes your treatment effect estimate by 40%.

(a) What does this sensitivity tell you about the robustness of your causal model?
(b) Which of the four failure modes is most likely responsible for this sensitivity? How would you determine which one?
(c) Design a sensitivity analysis plan: which edges would you test first, what range of estimates would you report, and under what conditions would you decline to report a point estimate at all?
(d) What additional analysis would you perform before reporting the estimate to a policymaker?

**S2.** *Tests Objectives: Distinguish distributional plausibility from causal validity; redesign broken DAG*

You are reviewing an LLM-proposed DAG for a study of a workplace wellness intervention on employee productivity. The proposed DAG includes `manager_rating → productivity` as a direct edge.

(a) Identify at least two causal mechanisms that could support this edge. Identify at least one that would reverse it.
(b) Identify at least two variables that could be confounders of this relationship and that an LLM might miss.
(c) Identify one variable that the LLM might propose as a confounder but is actually a collider. Draw the relevant portion of the DAG.
(d) After applying the Human Decision Node protocol, write a one-paragraph justification for your final decision on this edge — accept, revise, or reject — that you could present to a domain expert reviewer.

---

### Challenge

These exercises go beyond the chapter's boundary. They are open-ended; there is no single correct answer.

**C1.** *Open Design: Non-determinism and the Consensus DAG*

Run the LLM extraction and edge proposal pipeline three times on the same data dictionary with temperature > 0.

(a) How many edges appear in all three runs? How many appear in only one?
(b) Design a consensus protocol: which edges should automatically advance to the Human Decision Node, which should be flagged for extra scrutiny, and which (if any) should be automatically rejected?
(c) What does the instability of single-run edges tell you about the reliability of LLM-proposed causal structure? Frame your answer in terms of distributional plausibility versus causal validity.
(d) Propose a formal measure of edge instability across runs. How would you incorporate this measure into the Stage 4 validation workflow?

**C2.** *Computational Extension: Compounding Collider Bias*

Using the simulated dataset, add a second collider: `composite_quality_score` caused by both `intervention_received` and `LOS`.

(a) Condition on both colliders simultaneously (`satisfaction` and `composite_quality_score`) and report the bias.
(b) Compare to the single-collider case. Does conditioning on two colliders compound the bias additively, multiplicatively, or in some other way?
(c) Explain structurally why conditioning on multiple colliders compounds the problem. Draw the relevant portion of the DAG for each case.
(d) Propose a general rule for identifying collider variables in a proposed adjustment set *before* running the model. What graph-theoretic property distinguishes a collider from a confounder, and how would you check it programmatically using `networkx`?

---

## Chapter Summary

**What you can now do that you couldn't before this chapter:**

You can sit down with a data dictionary — 80 variables, 200 variables, however many — and run a structured pipeline that transforms that raw input into a defensible causal graph. You know the mechanism by which the LLM contributes: pattern retrieval from training text, operating at Rung 1 of Pearl's hierarchy while the causal questions you are asking live at Rung 2. You know the four ways that contribution can go wrong: hallucinated edges, reversed directions, missing confounders, collider conditioning. And you have a three-question protocol that catches all four at Stage 4.

You also know something more important than the pipeline itself: you know that the LLM's confidence is a function of distributional frequency, not epistemic certainty. Validate the high-confidence proposals first. The low-confidence flags are the ones the LLM already told you to worry about.

**The one idea from this chapter that matters most:**

The Human Decision Node is not a bureaucratic checkpoint. It is the only mechanism in the pipeline that bridges the gap between distributional plausibility and causal validity. Every failure mode documented in this chapter — Berkeley admissions, the HRT reversal, the collider trap in the triage system from Chapter 14 — represents a case where someone built a model on a DAG they did not sufficiently interrogate. The pipeline makes interrogation tractable. It does not make it optional.

**The mistake to watch for:**

Trusting HIGH-confidence proposals more than MEDIUM ones. The simulation showed you directly: an LLM can propose a collider as a confounder with HIGH confidence, and conditioning on it will bias your estimate in a direction the LLM will never warn you about. Confidence in an LLM output is information about distributional frequency. It is not information about causal truth.

**The Feynman test:** Can you explain to a first-year graduate student why the Nurses' Health Study got the HRT estimate backwards, what structural feature of the data-generating process caused the error, and what the LLM-assisted pipeline in this chapter would and would not have done to prevent it? If you can, you understand this chapter.

---

## Connections Forward

This chapter treated the DAG as something you build from external inputs — a data dictionary, domain knowledge, an LLM proposal. The Human Decision Node validates that structure edge by edge. But the pipeline assumes you can, in principle, enumerate the relevant variables and propose the relevant edges, even if imperfectly. That assumption breaks down in a specific class of problems: settings with many potential confounders, poorly understood causal mechanisms, and large observational datasets where the graph structure itself is unknown.

Chapter 16 takes on a harder version of the same problem. Instead of asking "how do I validate a proposed DAG?", it asks "how do I learn a DAG from data when I don't have a proposed one?" The tools — constraint-based algorithms like PC and FCI, score-based methods like GES — can recover causal structure from observational data under specific assumptions. Those assumptions are strong, and understanding exactly where they fail is the direct continuation of what this chapter taught you: the line between what the data can tell you and what requires a human judgment that no algorithm can substitute.

The connection is direct. The missing-confounder problem from Failure Mode 3 — the variable that isn't in the dictionary, the healthy user bias that was never collected — is the same problem that makes causal discovery from observational data fundamentally limited in the presence of unmeasured variables. The pipeline you built here handles measured variables. Chapter 16 handles the ones you couldn't measure, and the assumptions you have to make about them before any estimate is defensible.

---

## References

Bickel, P. J., Hammel, E. A., & O'Connell, J. W. (1975). Sex bias in graduate admissions: Data from Berkeley. *Science*, 187(4175), 398–404.

Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.

VanderWeele, T. J., & Ding, P. (2017). Sensitivity analysis in observational research: Introducing the E-value. *Annals of Internal Medicine*, 167(4), 268–274.

Writing Group for the Women's Health Initiative. (2002). Risks and benefits of estrogen plus progestin in healthy postmenopausal women: Principal results from the Women's Health Initiative randomized controlled trial. *JAMA*, 288(3), 321–333.

---

*Chapter 15 · Causal Inference with LLMs*  
*© 2026 Trimbkeshwar — INFO 7390 Advanced Data Science and Architecture*

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Yoshua Bengio** has argued that the next generation of AI must learn causal structure — not just statistical regularities — to achieve robust, generalizable reasoning. His "consciousness prior" research program proposes mechanisms by which causal variables might emerge in neural networks.

![Yoshua Bengio](../images/yoshua-bengio-1zo.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who is Yoshua Bengio, and how does his work on causal representation learning connect to LLM causal variable identification we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Yoshua Bengio"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through the "consciousness prior" hypothesis — what specifically is the bottleneck Bengio proposes?
- Ask it about Bengio's recent advocacy for AI safety and the constraints on advanced AI development.

What changes? What gets better? What gets worse?

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 13.1 — representative data dictionary showing inconsistent variable descriptions

Create a standalone D3 v7 HTML figure for "representative data dictionary showing inconsistent variable descriptions". Use a horizontal bar chart with 5 labeled categories with approximate values from 0 to 100. Marks: bars or rectangular panels, direct labels, and concise value labels. Channels: position for sequence or category, length for quantitative emphasis when bars are used, color for the primary highlighted item only, and direct text labels for accessibility. Use a zero baseline for quantitative bars. Include title, desc, role="img", aria-labelledby, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Deliver as one HTML file with inline CSS and the D3 7.9.0 CDN.

> Reference implementation: `d3/13-llm-causal-variable-identification-fig-01.html`

---

### Figure 13.2 — Two overlapping circles

Create a standalone D3 v7 HTML figure for "Two overlapping circles". Use a horizontal bar chart with 5 labeled categories with approximate values from 0 to 100. Marks: bars or rectangular panels, direct labels, and concise value labels. Channels: position for sequence or category, length for quantitative emphasis when bars are used, color for the primary highlighted item only, and direct text labels for accessibility. Use a zero baseline for quantitative bars. Include title, desc, role="img", aria-labelledby, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Deliver as one HTML file with inline CSS and the D3 7.9.0 CDN.

> Reference implementation: `d3/13-llm-causal-variable-identification-fig-02.html`

---

### Figure 13.3 — Three-panel diagram showing structural failure modes

Create a standalone D3 v7 HTML figure for "Three-panel diagram showing structural failure modes". Use a horizontal process diagram with 4 to 5 ordered stages with directed connectors. Marks: rectangular stage nodes and arrow connectors. Channels: position for sequence or category, length for quantitative emphasis when bars are used, color for the primary highlighted item only, and direct text labels for accessibility. Use a zero baseline for quantitative bars. Include title, desc, role="img", aria-labelledby, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Deliver as one HTML file with inline CSS and the D3 7.9.0 CDN.

> Reference implementation: `d3/13-llm-causal-variable-identification-fig-03.html`

---

### Figure 13.4 — Five-stage pipeline with automation boundary clearly marked

Create a standalone D3 v7 HTML figure for "Five-stage pipeline with automation boundary clearly marked". Use a horizontal bar chart with 5 labeled categories with approximate values from 0 to 100. Marks: bars or rectangular panels, direct labels, and concise value labels. Channels: position for sequence or category, length for quantitative emphasis when bars are used, color for the primary highlighted item only, and direct text labels for accessibility. Use a zero baseline for quantitative bars. Include title, desc, role="img", aria-labelledby, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Deliver as one HTML file with inline CSS and the D3 7.9.0 CDN.

> Reference implementation: `d3/13-llm-causal-variable-identification-fig-04.html`

---

### Figure 13.5 — Three-question validation flowchart

Create a standalone D3 v7 HTML figure for "Three-question validation flowchart". Use a horizontal process diagram with 4 to 5 ordered stages with directed connectors. Marks: rectangular stage nodes and arrow connectors. Channels: position for sequence or category, length for quantitative emphasis when bars are used, color for the primary highlighted item only, and direct text labels for accessibility. Use a zero baseline for quantitative bars. Include title, desc, role="img", aria-labelledby, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Deliver as one HTML file with inline CSS and the D3 7.9.0 CDN.

> Reference implementation: `d3/13-llm-causal-variable-identification-fig-05.html`

---

### Figure 13.6 — Before/after comparison

Create a standalone D3 v7 HTML figure for "Before/after comparison". Use a horizontal process diagram with 4 to 5 ordered stages with directed connectors. Marks: rectangular stage nodes and arrow connectors. Channels: position for sequence or category, length for quantitative emphasis when bars are used, color for the primary highlighted item only, and direct text labels for accessibility. Use a zero baseline for quantitative bars. Include title, desc, role="img", aria-labelledby, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Deliver as one HTML file with inline CSS and the D3 7.9.0 CDN.

> Reference implementation: `d3/13-llm-causal-variable-identification-fig-06.html`

---

### Figure 13.7 — Bias comparison bar chart

Create a standalone D3 v7 HTML figure for "Bias comparison bar chart". Use a horizontal bar chart with 5 labeled categories with approximate values from 0 to 100. Marks: bars or rectangular panels, direct labels, and concise value labels. Channels: position for sequence or category, length for quantitative emphasis when bars are used, color for the primary highlighted item only, and direct text labels for accessibility. Use a zero baseline for quantitative bars. Include title, desc, role="img", aria-labelledby, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Deliver as one HTML file with inline CSS and the D3 7.9.0 CDN.

> Reference implementation: `d3/13-llm-causal-variable-identification-fig-07.html`
