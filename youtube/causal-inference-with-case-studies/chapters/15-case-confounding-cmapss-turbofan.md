# Chapter 15 — Case: Don't Trust the Sensors


## TL;DR

- Regime-aware causal anomaly triage on NASA CMAPSS turbofan data — when "normal" depends on what the engine is doing.
- The chapter moves through Question, Causal diagram, Identification strategy, Results, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Regime-aware causal anomaly triage on NASA CMAPSS turbofan data — when "normal" depends on what the engine is doing.*

**Author:** Jahnavi Patel
**Editor:** Nik Bear Brown

---

## 1. Question

Industrial monitoring systems generate too many alarms because they compare each sensor reading to a single global threshold. A turbofan engine climbing at 35,000 feet runs hotter and at higher pressure than the same engine at sea level — but a detector that only knows the global mean cannot tell that "hot for cruise" is healthy. It fires anyway. Operators, drowning in the noise, learn to ignore alerts. The 1994 Texaco Milford Haven explosion ran at 275 alarms in eleven minutes before the incident, and the UK Health and Safety Executive concluded the alarm load was a contributing factor [UK HSE, 1997].

The causal question this case asks: *does an alert from sensor S indicate that engine E is degrading, or only that E is operating in a regime its training set under-represented?* The data is NASA's Commercial Modular Aero-Propulsion System Simulation (CMAPSS) benchmark [Saxena & Goebel, 2008], available from the [NASA Prognostics CoE](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/). Of its four sub-datasets, FD001 and FD003 run at one operating condition and FD002 and FD004 cycle through six. The identification strategy — back-door adjustment via stratification on operating regime — is attempted because the operating settings (altitude, Mach, throttle) drive both the regime classifier the system uses and the raw sensor values themselves. They are the textbook back-door confounder of any "is this reading anomalous" claim.

## 2. Causal diagram

The DAG Patel specifies has three layers. The root nodes are the three operating settings the flight crew sets: `op_setting_1` (Altitude), `op_setting_2` (Mach number), `op_setting_3` (Throttle Resolver Angle). A second layer holds latent physical variables — air density, tip speed, fuel flow, combustor temperature, HPC loading — that the operating settings determine through the engine's thermodynamics. The leaves are five observed sensor channels selected as the system's causal-branch sensors: sensor_3, sensor_4, sensor_9, sensor_11, sensor_15. Engine health (the unobserved degradation state, indexed by RUL) is a separate parent that also affects the observed sensors.

In arrow form, the structure is:

`Settings → LatentPhysics → Sensor_observed`
`EngineHealth → Sensor_observed`
`Settings → RegimeClassifier`

The two parents of any observed sensor are `Settings` (through latent physics) and `EngineHealth`. A scoring rule that asks "is this reading far from the global mean?" cannot tell which parent moved the sensor. The reading might be high because the engine is at altitude, or because the compressor is wearing out. Without conditioning on `Settings`, the back-door path *Sensor ← Settings → (other readings drawn from training data)* contaminates the estimate of the causal effect *EngineHealth → Sensor*. Settings sit at exactly the position Chapter 3 calls a confounder.

## 3. Identification strategy

Patel's identification claim is back-door adjustment by stratification on operating regime. The argument runs: the three operating settings determine the conditional expectation of every observed sensor through known thermodynamic relationships. If we partition readings by regime and judge each reading against the within-regime expected value, the back-door path through `Settings` is blocked. What remains in the residual is the contribution of `EngineHealth` plus measurement noise — the causal signal we wanted.

The mechanics. A KMeans classifier with k = 6, trained on the three op-setting columns, assigns each incoming reading to a cluster. The choice of k is not free: the CMAPSS specification defines six discrete operating points, and a silhouette analysis on FD002 confirms k = 6 (silhouette = 0.9971, with within-cluster inertia collapsing from 1133.9 at k = 5 to 0.2 at k = 6). Inside each cluster, a separate LinearRegression predicts each sensor from the op-settings. The anomaly score is `causal_z = |observed − predicted| / residual_std`, aggregated as the mean of the top three of five causal sensor z-scores and capped at a five-sigma ceiling. The vague word "anomaly" means, specifically, *the residual z-score from the regime-conditional expected value*.

The identifying assumption is that regime cluster membership captures all relevant settings-driven confounding of the sensor signal. This is a strong assumption and the chapter should name it. It will fail when the same nominal cluster contains genuinely different regimes — when, for example, an engine on a hot day at altitude differs systematically from the same engine on a cold day, and ambient temperature is not part of the cluster definition.

A second device, presented as a sensitivity check rather than primary identification, applies a structural veto. The isentropic compression relation requires HPC outlet temperature (sensor_11) and pressure (sensor_15) to move together. A G-test for independence on a 5×5 contingency table built from the last 100 readings detects when the coupling breaks; the critical value is χ²(df = 16, *p* = 0.05) = 26.30, not the 9.49 of a 3×3 table. When the test rejects, the system applies a graduated veto factor `1.0 − 0.5 × min(G/26.30, 1.0)` and labels the reading as more consistent with sensor fault than with engine degradation. The veto does not identify the same effect; it constrains the alert by a physical relationship the regression does not encode.

## 4. Results

Two patterns matter, and the chapter will report both honestly.

On the single-condition data, regime conditioning is largely redundant — there is only one regime — and the win is coverage. On FD001, the full pipeline (causal blend at α = 0.60) alerts on 69% of the 100 test engines against Isolation Forest's 17%, with mean lead time 164.9 cycles versus 107.4 (Fisher *p* < 0.001 on coverage; Wilcoxon *p* = 0.031 on lead time, which does not survive Bonferroni correction across the ablation). On FD003 (single condition, dual fault mode), coverage rises to 89% versus 19%.

On the multi-condition data, the picture is sharper and uglier. Both the global z-score baseline (means from FD001) and the retrained z-score baseline (means recomputed from FD002) alert on 100% of the 259 FD002 test engines. Every alert is premature; F1 = 0.000 on both. Retraining is statistically indistinguishable from not retraining (Wilcoxon *p* = 0.548, Fisher *p* = 1.000). Regime-aware causal scoring drops coverage to 66% on FD002 with F1 = 0.279, and to 57% on FD004 with F1 = 0.352, both Fisher *p* < 0.001 against the global baseline. The F1 numbers are below 0.50. They are not impressive as classifiers. What the regime-aware approach does is move the system off a 100% false-positive rate — a useless detector — onto something that suppresses the false alarms while alerting on engines whose median RUL is 54 cycles versus 103 in the non-alerted group (Wilcoxon *p* < 0.001, *r* = 0.484 on FD002). The gain is the false-positive collapse that did not happen, not classifier excellence.

## 5. Sensitivity and limitations

Patel names several limits, and the most consequential is a miscluster cascade. The regime classifier is unsupervised KMeans, and per-regime regression coefficients are conditioned on its assignments. A misclassified reading is scored against the wrong regime's expected values and the wrong residual standard deviation. There is no ground truth for cluster membership at inference time, so the system cannot detect this failure on its own — the error propagates silently into the residual. This is the named failure mode for the chapter: **the entire identification rests on cluster membership being correct, and the system has no inside-the-loop check that it is.**

Three further limits compound that one. The isentropic veto encodes one physical coupling out of many — fan-bypass, combustor, turbine — so it catches one class of sensor fault and is silent on the rest. CMAPSS is simulated; the noise structure is what NASA's solver produces, not what real-fleet sensors do, and field deployment would require revalidation. The blend weight α = 0.60 was selected on the test set the paper also reports performance on, which is data leakage — the F1 numbers are an optimistic upper bound and Patel says so. Finally, the structural-veto evaluation in §5.2 of the manuscript cannot distinguish the veto correctly catching sensor faults from the veto over-firing on real degradation that genuinely breaks the coupling; the labelled set is too small.

## 6. Theory connection

This case pairs directly with Chapter 3 on confounding and adjustment. The operating settings are the textbook back-door confounder: parents of the cause-of-interest signal (engine health → sensor) and of the candidate predictor (sensor reading itself). Conditioning on regime — by stratification through the KMeans classifier, not by regression-style coefficient adjustment — is the back-door operation Chapter 3 develops, applied to a streaming engineering problem rather than a clinical contingency table.

## 7. Transfer prompt

Three questions for your own work. What variables in the system you monitor play the role of operating regime — observable settings that determine what "normal" looks like and that you can condition on? What would have to be true for stratification on those variables to recover a clean residual signal, and how would you check it? What structural relationship in your domain could play the role the isentropic coupling plays here — a physical or mechanical constraint a healthy reading must satisfy regardless of regime?

---

**Tags:** causal-inference, back-door-adjustment, anomaly-detection, industrial-iot, NASA-CMAPSS, turbofan, regime-conditioning, confounding, stratification, sensor-fusion

---

## A note about AI

The CMAPSS turbofan case is an engineering causal-inference problem — sensor data, degradation, remaining useful life. The model handles engineering causal language fluently and confidently.

Where the model genuinely helps: structuring the candidate confounders in a multi-component engineered system, and surfacing where sensor measurements collide with the physical causal structure.

Where the model does damage: producing engineering causal claims (this sensor failure caused this degradation) from associational sensor data. The model has not seen the turbofan; the physics is in the data and in the engineer.

The rule: structure from the model; the engineering causal call from someone who has worked on turbofans.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Susan Athey** has built much of the modern field of machine-learning-augmented causal inference — including causal forests for estimating heterogeneous treatment effects. Her work crosses the boundary between traditional econometrics and modern ML in cases like equipment failure prediction.

**Run this:**

```
Who is Susan Athey, and how does her work on ML for causal inference connect to the confounding case-study we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.
```

→ Search **"Susan Athey"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through causal forests on a specific applied problem (treatment effects of an industrial sensor calibration).
- Ask it about Athey's parallel role as a tech industry consultant and an academic economist.

What changes? What gets better? What gets worse?
