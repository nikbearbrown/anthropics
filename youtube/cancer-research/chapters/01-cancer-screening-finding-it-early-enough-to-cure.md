# Chapter 1 — Cancer Screening: Finding It Early Enough to Cure

A 58-year-old man with no symptoms reads that a new blood test can detect 50 cancers from a single tube of blood. He pays out of pocket and the test comes back positive, with a predicted tissue of origin of pancreas or biliary system. He is terrified. Over the next six weeks he undergoes a contrast CT, an MRI, an endoscopic ultrasound with fine-needle aspiration, and a PET scan. The pancreas is normal. The aspiration nicks a small vessel and he is admitted overnight for observation. Three months and several thousand dollars later, the working conclusion is that the test was a false positive — or possibly that something is there that nobody can find.

His physician is now in an uncomfortable position. The test reported a cancer signal, but every test that can actually see tissue says otherwise. Was the blood test wrong? Is there a tumor too small to image? Should they keep looking, or stop?

The trouble is that the man was never told the number that mattered. The test's specificity sounds excellent. But a positive result in a healthy, low-risk person carries far less weight than the marketing implied — and nobody computed how much less before he was sent down a cascade of invasive follow-up. This chapter is about that number, and about the several ways early detection can fool us into thinking we are saving lives when we are mostly producing alarm.

---

## Screening is a population test, not a diagnosis

A **screening test** is applied to people without symptoms, drawn from a defined risk group, to find disease earlier than it would otherwise appear. This is categorically different from a **diagnostic test**, which is applied to someone in whom disease is already suspected. The distinction is not pedantic. Because most screened people do not have the disease, the test must be judged by what happens across the whole population — deaths prevented, false alarms generated, healthy people harmed by follow-up — not by whether it found a cancer in one person.

When a test meets a person, four outcomes are possible. The person has the disease and the test flags it (**true positive**), or has it and the test misses it (**false negative**), or lacks it and the test correctly clears them (**true negative**), or lacks it and the test incorrectly flags them (**false positive**). The false positive is the person sent for six weeks of invasive workup who had nothing wrong.

Two properties describe the test itself. **Sensitivity** is the fraction of people with the disease who are correctly flagged — a sensitive test misses few cancers. **Specificity** is the fraction of people without the disease who are correctly cleared — a specific test generates few false alarms. These are properties of the test, measured once and applied everywhere.

The number a worried patient actually wants is the **positive predictive value (PPV)**: given a positive result, the probability that disease is truly present. PPV is not a property of the test. It depends on **prevalence** — the fraction of the screened population that actually has the disease. This is the fact that makes screening mathematics unintuitive and the fact that the opening-case patient was never given.

![2x2 grid of test outcome by true disease status, with sensitivity, specificity, and PPV read off the margins](images/01-cancer-screening-finding-it-early-enough-to-cure-fig-01.png)
*Figure 1.1 — The 2x2 confusion matrix of a screening test*

<!-- → [CHART: 2x2 confusion matrix — TP/FP/FN/TN cells with sensitivity, specificity, and PPV labeled on the margins] -->

---

## Why prevalence governs PPV

Compute it explicitly to see why prevalence dominates.

A blood screen has sensitivity 90% and specificity 99% — numbers that sound superb. Apply it first to an asymptomatic general-population cohort where prevalence is 0.5%, then to a high-risk cohort where prevalence is 10%.

**Low-prevalence population — 100,000 people, 0.5% with disease.**

Diseased: 500 people. The test correctly flags 90% of them: 450 true positives, 50 false negatives.

Disease-free: 99,500 people. The test incorrectly flags 1% of them: 995 false positives, 98,505 true negatives.

PPV = true positives / (true positives + false positives) = 450 / (450 + 995) = **31%**.

A positive result is real only about one time in three. Nearly two-thirds of positives are false — 995 healthy people sent for follow-up to find 450 true cancers. The "99% specific" test produces a PPV of 31% because the 1% of false positives is drawn from a pool of 99,500 healthy people, far outnumbering the 500 who are sick.

**High-prevalence population — same test, 10% with disease.**

Diseased: 10,000. True positives: 9,000. False negatives: 1,000.

Disease-free: 90,000. False positives: 900. True negatives: 89,100.

PPV = 9,000 / (9,000 + 900) = **91%**.

The identical test — same sensitivity, same specificity — yields PPV 31% in the low-prevalence population and 91% in the high-prevalence one. Nothing about the test changed. Only who was tested changed.

![Bar chart of positive predictive value rising from 31% to 91% as prevalence climbs at fixed test performance](images/01-cancer-screening-finding-it-early-enough-to-cure-fig-02.png)
*Figure 1.2 — PPV climbs with prevalence at fixed test performance*

<!-- → [CHART: PPV as a function of prevalence at fixed sensitivity 90% / specificity 99% — curve climbing steeply from low prevalence] -->

This is why screening guidelines specify populations so narrowly — age bands, smoking pack-years, risk syndromes. Targeting raises the prevalence in the screened group, which raises PPV, which reduces the ratio of harm to benefit. The opening-case patient was a low-risk person tested with a test designed for an elevated-risk population. No one applied the arithmetic that would have revealed how likely his positive result was to be false before he underwent invasive workup.

---

## The biases that flatter screening

Three artifacts can make a screening program look effective even when it changes nothing about when people die.

**Lead-time bias.** Screening moves the diagnosis date earlier. If cancer is found at age 50 by screening but the patient still dies at 60, survival from diagnosis is ten years. If the same cancer surfaces as symptoms at 55 with death at 60, survival is five years. The screened patient appears to survive twice as long, but died at the identical age. Earlier diagnosis inflates measured survival even when treatment changes nothing. A program can show a dramatic improvement in five-year survival statistics while leaving age at death completely unchanged.

**Length-time bias.** Screening catches cancers during their detectable preclinical phase. Slow-growing tumors spend a long time in that phase and are therefore over-represented among screen-detected cancers. Fast, lethal tumors tend to produce symptoms between screening rounds and are therefore under-represented. Screen-detected cancers are on average more indolent than symptom-detected cancers — not because screening found them early enough to change their biology, but because the fast-moving ones were never there to be found. A screened population's tumors would have done better on average even without treatment.

**Overdiagnosis.** The most consequential bias, and the hardest to see. Screening can detect cancers that would never have caused symptoms in the person's lifetime — slow tumors in older patients, indolent histologies, in-situ lesions. The patient is diagnosed, treated, and potentially harmed by treatment, but would have lived just as long without any of it. Overdiagnosis is especially severe in PSA-detected prostate cancer, thyroid cancer identified incidentally, and some screen-detected breast ductal carcinoma in situ. At the individual level, overdiagnosis is invisible: you cannot tell whether a particular patient was overdiagnosed. Only population-level studies reveal it as excess diagnoses over expected incidence.

The corrective for all three is to evaluate screening by **disease-specific mortality** in randomized trials with long follow-up: does the screened group die of this cancer less often than the unscreened group? Not survival time from diagnosis, not how many cancers were found — how many people died of the disease. This is the only endpoint that is immune to all three biases simultaneously.

![Comparison of what screening statistics show versus the reality for lead-time, length-time, and overdiagnosis biases](images/01-cancer-screening-finding-it-early-enough-to-cure-fig-03.png)
*Figure 1.3 — Three biases that flatter screening*

---

## When screening is justified

In 1968, a WHO report by Wilson and Jungner laid out criteria still in use today. The disease must be important and have a significant burden. It must have a detectable preclinical phase — a window during which the disease is present but asymptomatic and catchable. Effective treatment must exist for early disease; finding something earlier only matters if earlier treatment works better. The test must be acceptable to the population in terms of cost, access, and tolerability. The test must perform well enough that benefits outweigh harms. And critically: **the benefits must outweigh the harms** — harm including false positives, unnecessary procedures, overdiagnosis, and anxiety.

Most proposed screening programs strain at least one criterion. The accepted ones are those where randomized trial evidence shows that benefit clearly dominates harm in a defined population: low-dose CT for lung cancer in current and former heavy smokers, cervical cytology and HPV testing, mammography with appropriate age and interval qualification, colonoscopy and stool-based tests for colorectal cancer. In each case the evidence is specific to the defined population — apply the program to a lower-risk group and the PPV falls and the harm-to-benefit ratio shifts.

Prostate-specific antigen screening for prostate cancer is the sharpest example of a program that satisfies some criteria and strains others. PSA finds cancers that would not otherwise have been found. But PSA-detected prostate cancer includes a substantial fraction of tumors that would never have caused symptoms in the patient's lifetime. Major trials — the ERSPC and PLCO — produced conflicting results on mortality benefit, and clinical guidelines now emphasize shared decision-making between patient and physician rather than universal recommendation. Reasonable experts disagree, and the disagreement tracks directly to differing estimates of overdiagnosis.

---

## Survival statistics and when to trust them

A pervasive error in the public understanding of screening is treating improved survival statistics as proof of benefit. They are not. The opening paragraph of every news story about a screening test announces improved five-year or ten-year survival among people whose cancers were found early. Lead-time bias guarantees this result even with zero therapeutic benefit. Length-time bias adds to it. Overdiagnosis inflates the denominator with patients who were never going to die of the disease.

The correct question is: did the screened group die of this cancer less often than the unscreened group? Five-year survival among screen-detected cases versus symptom-detected cases is the wrong comparison. It is a population-level version of the dead-end in the worked example — confusing a metric that is guaranteed to look better with a metric that would actually show benefit.

This does not mean survival statistics are useless. For comparing treatments in patients who are already diagnosed — where lead-time is identical across arms — survival statistics are appropriate. For evaluating screening programs, they are not. The NLST — the National Lung Screening Trial — showed that low-dose CT screening in heavy smokers reduced lung cancer mortality by approximately 20%. That is the kind of endpoint that licenses a recommendation.

---

## What would change this picture

The chapter's central claim is that screening must be judged by population-level mortality reduction, because survival statistics, detection counts, and even PPV can each mislead. The finding that would revise this: a large, well-conducted randomized trial of a multi-cancer early detection blood test that demonstrated a clear reduction in cancer-specific mortality — not just more cancers found, not just longer survival from diagnosis, but fewer deaths — with an acceptable false-positive and overdiagnosis burden. The NHS-Galleri trial and NCI prospective MCED studies are designed to answer exactly this question. If they show mortality benefit, the framework extends to blood-based multi-cancer screening. If they show improved survival statistics with unchanged mortality, the biases described here remain the binding constraint on every new screening technology.

---

## Still open

For multi-cancer detection tests, the curable early-stage cancers shed the least circulating tumor DNA — precisely the cancers screening most needs to find. Whether sensitivity at stage I can ever be high enough to matter for the cancers that would most benefit is a question set partly by tumor biology, not only by assay technology.

Overdiagnosis is invisible at the individual level by construction. We can estimate population-level overdiagnosis rates from excess diagnoses above expected incidence, but we cannot know which particular patient was overdiagnosed. What informed consent means under that uncertainty — how to counsel a patient whose screen-detected tumor might be a threat or might be nothing — is unresolved.

Risk-stratified screening promises to raise prevalence in the screened group and thus PPV, by targeting people with elevated genetic risk, family history, or prior biomarker exposure. But concentrating screening on the highest-risk group may leave too many cancers in the larger, lower-risk majority, where most absolute cases arise. The right trade-off between depth of coverage and population breadth is not established.

---

## LLM Exercises

1. **(Definitions)** Define sensitivity, specificity, and positive predictive value in one sentence each. State which of the three depends on disease prevalence and construct a one-sentence explanation of why.

2. **(2×2 calculation)** A mammography program has sensitivity 85% and specificity 90%. In women aged 40 to 49, breast cancer prevalence at screening is approximately 0.4%. Build the full 2×2 table on 100,000 women, compute PPV, and interpret the result in plain language. Repeat for a 70-year-old cohort with prevalence 1.2%, and explain in one sentence why the PPV differs in terms of who is being tested. State what additional evidence — beyond PPV — you would need before concluding the program saves lives in either group.

3. **(Bias identification)** A new screening test reports that screen-detected patients have five-year survival of 80% versus 45% for symptom-detected patients. A colleague concludes the test nearly doubles survival. Identify each of the three biases — lead-time, length-time, overdiagnosis — that could each, individually, produce this gap with zero true benefit. For each bias, describe one feature of a study design that would let you rule it out.

4. **(Wilson and Jungner applied)** Apply the Wilson and Jungner criteria to PSA screening for prostate cancer. Identify which criteria it satisfies and which it strains, explain why major randomized trials produced conflicting results on mortality benefit, and state the specific feature of prostate cancer natural history that makes overdiagnosis an irreducible concern.

5. **(Multi-cancer test evaluation)** A company marketing a multi-cancer early detection blood test claims it has 90% sensitivity and 99% specificity across 50 cancer types. A journalist writes that the test "could save hundreds of thousands of lives." Using the PPV framework, the three biases, and the Wilson and Jungner criteria, construct a methodical evaluation of whether the claim is warranted. Identify the single most important piece of evidence — not yet available — that would settle whether the test saves lives.

---

## References

- National Cancer Institute. *Cancer Screening Tests.* https://www.cancer.gov/about-cancer/screening/screening-tests
- National Cancer Institute. *Cancer Screening Overview.* https://www.cancer.gov/about-cancer/screening
- Wilson JMG, Jungner G. *Principles and Practice of Screening for Disease.* WHO, 1968.
- US Preventive Services Task Force. Screening recommendations (breast, cervical, colorectal, lung, prostate). https://www.uspreventiveservicestaskforce.org
- National Lung Screening Trial (NLST) Research Team. (2011). Reduced lung-cancer mortality with low-dose computed tomographic screening. *New England Journal of Medicine*, 365(5), 395–409.
- Schröder, F. H., et al. (2009). Screening and prostate-cancer mortality in a randomized European study. *New England Journal of Medicine*, 360(13), 1320–1328. [ERSPC]
- Andriole, G. L., et al. (2009). Mortality results from a randomized prostate-cancer screening trial. *New England Journal of Medicine*, 360(13), 1310–1319. [PLCO]
- National Cancer Institute. *Tests and Procedures Used to Diagnose Cancer.* https://www.cancer.gov/about-cancer/diagnosis-staging/diagnosis

---

## Prompts

### Figure 1.1 — The 2x2 confusion matrix of a screening test
Build a 2x2 annotated grid (confusion matrix). Two columns are true disease status (disease present, disease absent); two rows are test result (test positive, test negative). The four cells hold true positive (top-left), false negative (top-right), false positive (bottom-left), true negative (bottom-right). Mark the positive-outcome row/diagonal cells (TP, TN) in blue as the anchor cells and the error cells (FP, FN) in vermillion to signal harm. Add marginal annotations: sensitivity read down the disease-present column, specificity down the disease-absent column, PPV across the test-positive row — each with a small ratio formula and a leader line to the relevant cells. Equal-sized cells, clean gridlines, label every cell with its name. No data magnitudes; this is a schematic of definitions. Use a callout box restating each margin ratio in words. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 1.2 — PPV climbs with prevalence at fixed test performance
Build a vertical bar chart. X-axis: three prevalence scenarios in ascending order (low 0.5%, medium 2%, high 10%), kept in that sorted order, not re-sorted by value. Y-axis: positive predictive value in percent, zero baseline, 0–100 scale. Bars: 31, 65, 91. Color the low-prevalence bar (31%) in vermillion to flag the misleadingly low PPV, the high-prevalence bar (91%) in green as the favorable case, the middle bar neutral blue. Add a subtitle noting sensitivity 90% and specificity 99% held fixed. Direct-label each bar with its value. Add a light annotation: "same test, different population." No legend needed if bars are labeled. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 1.3 — Three biases that flatter screening
Build a two-panel comparison table with three rows. Left column header "What screening shows," right column header "The reality." Row 1: "Earlier diagnosis, longer measured survival" vs "Same death date (lead-time bias)." Row 2: "Detects mostly slow indolent tumors" vs "Fast lethal ones slip between rounds (length-time bias)." Row 3: "Flags a screen-detected lesion" vs "Patient outlives it, dies of something else (overdiagnosis)." Render each left cell in neutral/blue and each right cell in vermillion to signal the artifact undercutting the apparent benefit. Connect each pair with a horizontal arrow from left to right. Add a bottom annotation: "Survival looks longer; age at death unchanged." Equal row heights, clear divider between columns. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.
