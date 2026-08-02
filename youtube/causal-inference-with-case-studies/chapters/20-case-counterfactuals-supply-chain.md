# Chapter 20 — Case: Supply Chain Collapse Predictor


## TL;DR

- Using counterfactual feature ablation to ask whether a disruption model is tracking seasonality or stress.
- The chapter moves through Question, Causal diagram, Identification strategy, Results, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Using counterfactual feature ablation to ask whether a disruption model is tracking seasonality or stress.*

**Author:** Reva Pethe
**Editor:** Nik Bear Brown

## 1. Question

A model trained on logistics data learns quickly that October is risky. October is also a high-demand month, so the correlation is real. The danger is what comes next. When the model raises a disruption flag in October, is it responding to something genuinely happening in the network — delays piling up, inventory thinning, suppliers wobbling — or to the calendar?

The Supply Chain Collapse Predictor is built around that question. It ingests 730 days of synthetic supply-chain records and trains an isotonic-calibrated probability model for daily disruption risk. The causal claim under investigation is *negative*: the model's high-confidence predictions are NOT caused by genuine operational stress; they are caused by seasonal patterns the features encode. The system is designed to test that claim by intervention rather than by inspection.

Counterfactual reasoning is the right tool because the question is not "what is the average effect of seasonality on predictions" but "what would the model predict in a world where time-of-year information were not available, all else held equal." That is a do-statement on the model's input, not an estimate of an effect in the field.

## 2. Causal diagram

The relevant nodes are: time-of-year (T), unobserved operational stress (O), the observable inventory and delay signals the model uses as features (S), the realized disruption outcome (Y), and the model's predicted probability (P̂).

The edges are these. T → S because seasonality drives feature levels: October ships more, inventory thins, lead times stretch. O → S because real operational stress also drives those same feature levels: a struck port pushes delays up regardless of the month. S → P̂ because the model maps features to a probability. O → Y because real stress causes real disruptions. T → Y because seasonal demand can directly produce disruptions even without underlying operational fragility.

```
        T ──────► S ──────► P̂
        │         ▲
        │         │
        ▼         │
        Y ◄────── O
```

The confound sits at S. Two distinct upstream causes — T and O — both push S in the same direction, and the model only sees S. From the model's vantage point, a high-stress July and a calm-but-busy October can look the same. The counterfactual question is what P̂ becomes under do(T = removed): intervene to strip time-of-year information from the input, hold everything else fixed, and read out what remains.

## 3. Identification strategy

The intervention is feature ablation. Pearl's do-operator, applied here, means refitting and scoring the model on a feature set with month, quarter, and any explicit time-of-year encodings dropped. Every other input — the seven-day rolling averages of delay, inventory, lead time, demand index, transport stress, weather risk, supplier reliability, plus the three-day velocity measures — is held fixed. The model is re-scored on the same days. The readout is the change in the high-confidence predictions: how many survive, how far they shift, whether the calibration holds.

If the high-confidence predictions persist with similar magnitude, the model was using S in a way that did not depend on T being explicit. If the high-confidence predictions collapse — if days the original model flagged at 80% drop to 30% under ablation — the original predictions were carried by T, not by O working through S.

This is a counterfactual question rather than a confounding-adjustment question. We are not estimating the effect of treatment on outcome and trying to remove a back-door path. We are asking what the model would do under intervention on its inputs. The estimand is a property of the function P̂ = f(S), not a property of the world.

The limit of this strategy must be named. Removing T at the input level does not remove T's information from the model entirely. The seven-day rolling average of demand index is itself partly a function of T. If the model can re-learn seasonality from features that survive ablation, the test understates the dependence. The counterfactual confound test is a feature-level diagnostic, not a representational one. It bounds the problem from one side.

## 4. Results

The README reports what the system measures. Disruption events are injected on roughly 4% of days by amplifying risk features: shipment delays multiply 2.5 to 5 times, inventory drops to 10 to 40% of normal, supplier reliability falls to 30 to 60% of baseline. Adversarial validation reports drift via AUC: near 0.5 means the training and current distributions are indistinguishable; above 0.75 indicates significant drift. Population Stability Index is reported per feature: below 0.1 is stable, above 0.25 is a significant shift between the reference window and current data.

The counterfactual confound test is described as a capability of the system rather than a measured outcome. The README states that the test exists, that its purpose is to surface seasonal-confound predictions, and that a prediction which dissolves under removal of month and quarter was never real evidence. The README does not (visibly) report a single headline number for what the test finds on this dataset. The framework is in place. The load-bearing measurement — the actual delta between with-T and without-T predictions on the 730-day record — is the place where a published case would need to add a measured result.

## 5. Sensitivity and limitations

The dataset is synthetic. Disruption events are injected by amplification rather than observed in field data, which means the test conditions are constructed to be detectable by the kind of features the model uses. A real logistics record would not be guaranteed to produce the same feature signatures under stress.

The drift detector says that a distribution has shifted; it does not say what is causing the shift. A PSI value above 0.25 on the inventory feature could reflect a genuine operational change, a measurement-pipeline change, or a seasonal pattern the reference window happened to miss. The signal is a flag for investigation, not a diagnosis.

The counterfactual test operates at the input-feature level. It cannot rule out that the model has internalized seasonality through correlated features that survive ablation — rolling averages of demand, weather risk, transport stress all carry seasonal structure that month and quarter do not exhaust.

The named failure mode the system is built to catch is **confidently-wrong seasonal alarms**: high-probability disruption flags raised in calendrically risky periods that would not survive removal of time-of-year features. The drift detector and the counterfactual test are diagnostics, not predictions. Neither is appropriate to deploy as the primary classifier. The probability model has to be correct first; these are checks on whether to trust it.

## 6. Theory connection

This case pairs with Chapter 8, *Counterfactuals and Mediation*. The counterfactual confound test is a direct application of Pearl's Rung 2 reasoning — intervention rather than observation — to a model's inputs rather than to a real-world treatment.

## 7. Transfer prompt

Take a model you have built or rely on. What feature do you suspect might be carrying false signal — a calendar effect, a geography effect, an instrument effect? What intervention on that feature could your system actually perform: drop it, randomize it, hold it constant? What would it look like if the result of that intervention was: prediction unchanged?

---

**Source.** Pethe, R. (2026). *Supply Chain Collapse Predictor.* Application: https://adsfinalproject.streamlit.app/. Code: https://github.com/revapethe/ads_final_project. README and supplementary materials.

---

## A note about AI

Supply-chain counterfactuals ask what would have happened under different sourcing, routing, or inventory decisions. The model can construct any counterfactual narrative on request.

Where the model genuinely helps: laying out the canonical supply-chain counterfactual estimands and their identification challenges (spillovers, network effects, time-varying confounders).

Where the model does damage: producing the counterfactual estimate itself. The estimate depends on assumptions about supplier behavior the model is willing to make and the operator should not be.

The rule: framework from the model; the counterfactual claim from the operator who has to defend it.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Guido Imbens** shared the 2021 Nobel Prize in Economics for advancing causal inference in observational data — including the local average treatment effect (LATE) framework. His work made instrumental-variable analysis a rigorous tool for counterfactual estimation.

**Run this:**

```
Who is Guido Imbens, and how does his work on LATE and instrumental variables connect to the counterfactual case-study we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Guido Imbens"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Imbens's classic LATE examples — what's the "complier" subpopulation, and why does estimation target only them?
- Ask it about Imbens's collaboration with Joshua Angrist on the "credibility revolution" in empirical economics.

What changes? What gets better? What gets worse?
