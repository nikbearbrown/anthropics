# Chapter 3 — Cancer Epidemiology and Risk Factors
*How to read the prior probability that a shadow is malignant — and where in the chain you could have interrupted it.*

The radiologist, the surgeon, and the oncologist all see the same shadow on the chest scan. They read it differently from how they would read the identical shadow in a different patient — not because the image looks different, but because the man attached to it has a 40 pack-year smoking history and spent two decades around asbestos insulation. The prior probability that this shadow is cancer is far higher in this man than in a lifelong non-smoker with no occupational exposure. That prior is what epidemiology gives you. Not the diagnosis — the probability before the biopsy.

Here is the trap the case sets. It is tempting to convert elevated risk into blame: he smoked, he worked in a hazardous industry, he made choices. But those two risk factors behave very differently. Smoking was partly a voluntary exposure, shaped by addiction, advertising, and cultural norm. Asbestos was a structurally imposed hazard — invisible, unchosen, and for decades inadequately regulated. Both act through the same molecular mechanism: carcinogens that damage DNA, mutations that accumulate over decades. Epidemiology's job is not to evaluate what the patient deserves. It is to give the prior probability and to identify where in the chain the damage could have been interrupted.

---

### Why cancer counts lie, and what rates actually tell you

The first tool in cancer epidemiology is the ability to read a statistic without being misled by it. The key distinction is between raw **case counts** and **age-standardized rates**.

**Incidence** is the number of new cases per unit of population per year. **Mortality** is deaths per unit of population per year. **Prevalence** is the number of people living with the disease at a given moment. Each answers a different question. But all three can be reported as raw counts or as rates, and the difference matters enormously.

Cancer is predominantly a disease of age. The probability that any given cell in your body accumulates enough mutations to transform in a single year is very small. Over seventy years of replication, the probability that *some* cell does so becomes substantial. An aging population — one in which a larger fraction of people are over sixty than was true thirty years ago — will produce more cancer cases per year *even if every individual person's age-specific risk is unchanged*. The total count rises because there are simply more old people.

Age-standardized rates correct for this by asking: if both populations had the same age structure, what would the rates be? When you read that cancer cases are rising in a country, the honest question to ask is whether age-standardized incidence rates are rising — or whether an aging population is producing more cases from unchanged per-person risk. Many headlines report the former while meaning the latter.

The global numbers are useful context. The International Agency for Research on Cancer estimated roughly 20 million new diagnoses and 9.7 million cancer deaths worldwide in 2022, drawn from the GLOBOCAN registry data covering over 185 countries. The top cancers by incidence were lung, breast, colorectal, prostate, and stomach. Lung cancer was the leading cause of cancer death — about 1.8 million deaths. In the United States the American Cancer Society estimates approximately 2 million new cases and around 600,000 deaths annually. These numbers are the best available, and imperfect: registry data is comprehensive in high-income countries and estimated in many low- and middle-income ones. The global figures have wide error bars.

---

### Genes and environment are not alternatives

The question "is this cancer genetic or environmental?" is asked constantly and answers nothing. The honest answer is that genetics and environment interact through the same molecular substrate, and treating them as mutually exclusive alternatives is the second major analytical error in cancer epidemiology, after confusing counts with rates.

About 5–10% of cancers are driven primarily by inherited high-penetrance mutations — variants that, if you carry one, raise your lifetime risk substantially. *BRCA1* and *BRCA2* are the canonical examples. A pathogenic *BRCA1* variant carries a lifetime breast cancer risk on the order of 65–80% and a lifetime ovarian cancer risk around 40–60%. *TP53* mutations cause Li-Fraumeni syndrome, with broad cancer susceptibility across multiple organ sites. *APC* mutations cause familial adenomatous polyposis. The mismatch-repair genes — *MLH1*, *MSH2*, *MSH6*, *PMS2* — cause Lynch syndrome, the most common hereditary cancer predisposition, raising risks for colorectal and endometrial cancer and others. *RB1*, *VHL*, *PTEN*, *STK11* each define their own heritable syndromes.

Below the high-penetrance mutations are moderate-penetrance variants (*CHEK2*, *PALB2*, *ATM*) that meaningfully raise risk but less dramatically. And below those are hundreds of common low-penetrance variants identified by genome-wide association studies, each shifting risk by a small amount — but aggregating into a **polygenic risk score** that is beginning to be used clinically to stratify screening decisions.

The remaining 90–95% of cancers are driven by somatic mutations — variants that arise in cells during a person's lifetime, not inherited at birth. These are the mutations that accumulate from environmental exposure.

The interaction between germline and environment is direct and important. Environment causes cancer by damaging DNA or disrupting the control of DNA replication. An inherited variant that impairs DNA repair amplifies the damage from any given environmental exposure. A *BRCA1* carrier exposed to ionizing radiation, or using hormone replacement therapy, or with chronic inflammation from another cause, is under layered risk that neither the genetics nor the exposure alone would predict. This is exactly the structure in the opening case: whatever inherited baseline our patient has, tobacco and asbestos supplied decades of additional DNA-damaging exposure on top of it.

Modern genomics makes the interaction legible. Different carcinogens leave recognizable **mutational signatures** — patterns of base changes stamped into the tumor genome by the specific chemistry of the exposure. The UV signature is C→T transitions at dipyrimidines — the pyrimidine dimers from Chapter 1. The tobacco carcinogen signature is predominantly G→T transversions at specific trinucleotide contexts. Aflatoxin leaves G→T transversions at codon 249 of *TP53* with near-perfect specificity. Mismatch-repair deficiency leaves an extremely high density of mutations across the entire genome — the microsatellite instability signature. Reading the mutational signature in a tumor is, in a real sense, reading its exposure history. The genome records what happened to the cell.

![Four carcinogen mutational signatures: UV, tobacco, aflatoxin, and MMR-deficiency fingerprints](images/03-cancer-epidemiology-and-risk-factors-fig-02.png)
*Figure 3.2 — Mutational signatures as exposure fingerprints*

<!-- → [DIAGRAM: mutational signatures — four panels side by side. Panel 1: UV signature (C→T at CpC contexts, skin cancer); Panel 2: tobacco signature (G→T transversions, lung cancer); Panel 3: aflatoxin signature (G→T at TP53 codon 249, hepatocellular carcinoma); Panel 4: MMR deficiency signature (hypermutation across whole genome, colorectal cancer). Each panel: a simple bar chart of mutation types with the dominant pattern highlighted and the exposure labeled.] -->

---

### Tobacco: the largest preventable cause

Tobacco causes roughly 22% of cancer deaths worldwide and approximately 30% in the United States. That figure — nearly one in three cancer deaths in the U.S. traceable to a single exposure — makes tobacco the largest modifiable cause of cancer death in recorded history.

Cigarette smoke contains over 70 known human carcinogens. Among the most important are polycyclic aromatic hydrocarbons like benzo[a]pyrene, which bind to DNA and form bulky adducts that, when misrepaired or unrepaired, produce G→T transversions. N-nitrosamines are another major class, alkylating DNA at multiple positions. Over decades of inhalation, these carcinogens accumulate mutations in lung epithelial cells — hitting *TP53* first, then *KRAS*, then other drivers — until a cell has the combination to form a tumor. The dose–response is steep: heavy smokers carry roughly a 20-fold relative risk of lung cancer compared to never-smokers. Even secondhand smoke exposure raises lung cancer risk by approximately 25%.

The cessation data is worth knowing precisely because it is more optimistic than most people expect. Quitting before age 40 returns lung-cancer risk to nearly never-smoker levels. The lung can clear the carcinogen burden; the cells that have not yet become malignant remain at risk only if they continue to be exposed. This is what makes tobacco both the clearest cause and the clearest prevention target in cancer epidemiology: the exposure is identifiable, the mechanism is understood, and removing the exposure has a measurable, proportional benefit.

Vaping is the live uncertainty. The carcinogen concentration in vapor is lower than in cigarette smoke, and the long-term cancer risk is probably lower — but 30-year cohort data on vaping does not exist. "Less carcinogenic than smoking" and "safe" are different claims, and only the first is currently defensible.

---

### The major modifiable exposures, briefly

**Alcohol** causes roughly 4% of cancers — mouth, throat, esophagus, liver, colon, and breast. The mechanism is ethanol's conversion to acetaldehyde, a reactive molecule that forms adducts with DNA and interferes with DNA methylation. The dose–response for breast cancer is approximately 7–10% increased risk per drink per day in meta-analysis. The old framing of "one drink per day is protective for cardiovascular disease" badly underweighted this cancer risk; the cardiovascular benefit is smaller and more contested than the cancer signal.

**Obesity** is the second-largest modifiable risk factor in high-income countries, causally linked to at least 13 cancer types. Adipose tissue is not passive storage — it is an endocrine organ. Excess adiposity raises circulating estrogen (driving estrogen-receptor-positive breast and endometrial cancers), elevates insulin and IGF-1 (which signal through the PI3K/AKT proliferation axis), and sustains chronic low-grade inflammation (which you have already seen in Chapter 6 as a pro-carcinogenic environment). Obesity is downstream of food access, food economics, and the design of urban environments — not primarily of individual willpower.

**Infections** cause approximately 13% of cancers globally, and they are among the most tractable prevention targets because the initiating agent is identifiable and often eliminable. High-risk HPV types 16 and 18 cause essentially all cervical cancer and a growing fraction of oropharyngeal, anal, and vulvar cancers — and the HPV vaccine prevents the initiating infection with high efficacy. Australia, with near-universal vaccination coverage, is on track to effectively eliminate cervical cancer as a public health problem within a generation. Hepatitis B is preventable by vaccine; hepatitis C is curable with direct-acting antivirals. Both cause hepatocellular carcinoma through decades of chronic liver inflammation. *H. pylori* is curable with a short antibiotic course and is the primary cause of gastric cancer. In each of these cases, the prevention point is the infection itself — decades before any cancer appears.

**Radiation** damages DNA directly. Ionizing radiation — X-rays, gamma rays, particle radiation — breaks DNA strands, with cancer risk rising roughly linearly with cumulative dose from the evidence of atomic-bomb survivor follow-up studies. Radon, a naturally occurring radioactive gas that accumulates in poorly ventilated basements, is the second leading cause of lung cancer after smoking. UV radiation creates pyrimidine dimers — the signature lesion of skin cancer. Tanning beds are IARC Group 1 carcinogens; they emit UV at intensities comparable to or exceeding the midday sun.

**Occupational and environmental exposures** were largely identified by observational epidemiology — workers in specific industries developing specific cancers at elevated rates, pointing investigators toward specific agents. Asbestos and mesothelioma is the canonical case: asbestos fibers lodged in the pleura persist for decades, producing chronic inflammation and eventually malignancy, with a latency of 30–40 years. Benzene causes acute myeloid leukemia. Fine particulate air pollution (PM2.5) became an IARC Group 1 carcinogen on the basis of consistent evidence across many countries for lung cancer risk in non-smokers living near major pollution sources. Aflatoxins — mycotoxins produced by *Aspergillus* molds contaminating stored grains — are Group 1 carcinogens for hepatocellular carcinoma, compounding HBV risk in parts of sub-Saharan Africa and East Asia.

![Ranked bar chart of cancer deaths attributable to modifiable exposures, tobacco leading at ~22%](images/03-cancer-epidemiology-and-risk-factors-fig-01.png)
*Figure 3.1 — Attributable fraction of cancer by modifiable exposure*

<!-- → [TABLE: major modifiable risk factors — columns: exposure, cancer types caused, approximate fraction of global cancer deaths, mechanism in one line, primary prevention strategy. Rows: tobacco, alcohol, obesity, HPV, HBV/HCV, H. pylori, ionizing radiation, UV, occupational/environmental exposures. Intended as a reference table; student should be able to generate the mechanism and prevention columns from chapter content.] -->

---

### How to decide whether an association is a cause

The opening case involves a man with two risk factors and a mass. Epidemiology can say the mass is more likely cancer than it would be in a low-risk patient — but that prior probability rests on the claim that these associations are causal, not merely correlational. How do we know?

The framework is the **Bradford Hill criteria**, proposed by Austin Bradford Hill in 1965 as a set of considerations for evaluating whether an observed statistical association reflects a genuine causal relationship. They are not an algorithm — Hill himself was explicit that no one criterion is sufficient and none is necessary — but they are a disciplined checklist for thinking about causation when randomized experiments are impossible.

The criteria are: **strength** (a large relative risk is harder to explain away as confounding than a small one); **consistency** (the association replicates across independent studies, populations, and methods); **specificity** (the exposure is associated with a specific outcome, not every disease); **temporality** (exposure precedes disease — this is the one criterion Hill considered non-negotiable); **biological gradient** (a dose–response relationship); **plausibility** (a biologically credible mechanism exists); **coherence** (the association fits with known biology and natural history); **experiment** (when experimental manipulation of the exposure is available, it supports the inference); **analogy** (similar exposures cause similar effects).

Smoking and lung cancer satisfies all of them. Relative risk of roughly 20-fold in heavy smokers. Replicated in dozens of independent cohorts across decades. Correct temporality: the cancer follows years of exposure. A clear dose–response: more pack-years, more risk. A known mechanism: carcinogens forming DNA adducts causing specific mutations. An experimental criterion: smoking cessation reduces risk in proportion to how long ago cessation occurred. This is not a statistical association. It is a cause.

The criteria also diagnose failure. **The beta-carotene story** is one of the most instructive false positives in cancer epidemiology. Observational data in the 1980s consistently showed that people with high dietary beta-carotene had lower lung cancer rates. The association was strong, consistent, and plausible — antioxidants protecting against oxidative DNA damage. Supplements were developed. Then the randomized trials ran: the ATBC trial (Alpha-Tocopherol, Beta-Carotene Cancer Prevention Study) and the CARET trial (Beta-Carotene and Retinol Efficacy Trial) both found that supplemental beta-carotene *increased* lung cancer risk in smokers, by roughly 17–28%. The observational signal had been entirely backwards. What looked like protection was confounding: people who eat foods rich in beta-carotene have many other health-protective behaviors, and it was those behaviors — not the beta-carotene — that explained the lower cancer rates.

The "experiment" criterion exists precisely to catch this. When an epidemiological finding cannot survive randomized intervention, the association was not causal in the way the observational data implied. Bradford Hill's criterion does not require that we randomize people to smoke — it asks that where experimental evidence is available, it should be weighed. Where it is not available (you cannot randomize people to 40-year occupational asbestos exposure), the inference rests on the other criteria, weighted together.

![Bradford Hill criteria side by side: smoking satisfies all nine, beta-carotene fails at experiment](images/03-cancer-epidemiology-and-risk-factors-fig-03.png)
*Figure 3.3 — Bradford Hill: causal inference vs a false positive*

<!-- → [DIAGRAM: Bradford Hill criteria as a diagnostic checklist — nine criteria listed with brief definitions; checkmarks for smoking/lung cancer (all nine satisfied); and a separate column showing the beta-carotene case (most criteria appeared satisfied from observational data, but the experiment criterion reversed the inference). This is a visual summary of how the criteria are applied, not a definitive rubric.] -->

---

### Disparities: unequal burden, structural causes

Cancer outcomes are unequal across populations, and most of the gap is not biological. In the United States, Black Americans have higher cancer mortality than white Americans for most major cancer types. The dominant causes of the gap are structural: less access to preventive care and screening, later-stage diagnosis at presentation, less access to guideline-concordant treatment, and less specialty referral. A tumor caught at stage I is a different clinical problem from the same tumor caught at stage III — not because the biology changed, but because the healthcare system found it later.

Some biological differences are real. Triple-negative breast cancer — which has fewer treatment targets and worse prognosis — is approximately twice as common in women of African ancestry as in women of European ancestry. Aggressive prostate cancer subtypes occur at higher frequency. These biological differences are genuine and worth investigating. They are not, however, the dominant driver of the mortality gap.

Globally the disparity is starker. Low- and middle-income countries account for approximately 70% of cancer deaths but a fraction of cancer research funding and treatment infrastructure. Childhood cancer survival is around 80% in high-income countries and approximately 20% in low-income ones. The biology is identical. The infrastructure is not.

The practical implication for prevention is that targeting the most common modifiable exposures — tobacco, infection, obesity — is particularly high-yield in settings with limited treatment capacity, because prevention prevents the need for expensive curative intervention that the system cannot provide at scale. HPV vaccination, H. pylori eradication, and tobacco control in low-income countries are cost-effective cancer interventions precisely because they act decades before any cancer appears, at a fraction of the cost of treating the cancers they prevent.

---

## Exercises

**Warm-up**

1. *(Recall — difficulty: low)* Define incidence, mortality, prevalence, and age-standardized rate. Then explain in two sentences why a country's cancer case counts can rise over twenty years while its age-standardized incidence rate falls. *What this tests: the counts-versus-rates distinction before applying it to real statistics.*

2. *(Recall — difficulty: low)* What percentage of cancers are driven primarily by inherited high-penetrance mutations, and what does that imply about the fraction driven by somatic mutations from environmental exposure? Name three high-penetrance cancer predisposition genes and the cancers they predispose to. *What this tests: the germline versus somatic framing and baseline quantitative literacy about the genetic fraction.*

3. *(Recall — difficulty: low)* Name the three infection-driven cancers for which a primary prevention intervention (vaccine, antibiotic, or antiviral) exists and state the intervention for each. *What this tests: whether the student can connect specific agents to specific cancers and to specific prevention strategies.*

**Application**

4. *(Apply — difficulty: medium)* A headline reads: "New study links drinking sugary soda to pancreatic cancer." Evaluate this claim against five Bradford Hill criteria. For each criterion, state what evidence you would need and whether the claim is likely to meet it. Conclude with a calibrated verdict — not "proven" or "disproven" but a statement of causal confidence and what evidence would change it. *What this tests: systematic application of the Bradford Hill framework to an unfamiliar association claim.*

5. *(Apply — difficulty: medium)* A *BRCA1* carrier asks her physician whether her risk is "genetic or environmental." Explain in plain terms why this is a false dichotomy, using her specific mutation and two specific environmental exposures to illustrate how the interaction works at the molecular level. *What this tests: the gene-environment interaction framing applied to a clinical scenario.*

6. *(Apply — difficulty: medium)* Draw a mechanism-to-prevention map for one infection-driven cancer of your choice (HPV/cervical, HBV/hepatocellular, or *H. pylori*/gastric). The map should show: initiating exposure → molecular damage or chronic inflammation → cell-level consequence → clinical cancer. Mark on the chain where each available preventive intervention acts, and label what it prevents. *What this tests: causal chain reasoning and the identification of intervention points before clinical disease.*

**Synthesis**

7. *(Synthesize — difficulty: high)* The beta-carotene trials reversed a consistent observational finding. Using Bradford Hill, identify which criteria the original observational data appeared to satisfy, which criterion the trials addressed, and what the reversal implies about the causal status of the original association. Then generalize: what class of bias could produce a strong, consistent, plausible observational association that disappears or reverses in a trial? *What this tests: integration of Bradford Hill with confounding and experimental evidence, and the epistemological lesson of a major false positive.*

8. *(Synthesize — difficulty: high)* Black Americans have higher cancer mortality than white Americans across most cancer types. Separate the plausible biological contributors from the structural contributors, cite the evidence that distinguishes them, and then propose the single intervention — at any level from clinical to policy — you think would close the largest share of the gap. Defend the choice mechanistically and in terms of feasibility. *What this tests: causal attribution between biology and structure, and the application of epidemiological reasoning to health equity.*

**Challenge**

9. *(Challenge — difficulty: high)* The Tomasetti and Vogelstein papers argue that a large fraction of cancer is attributable to random replication errors — "bad luck" — rather than inherited or environmental causes, and that this limits what prevention can achieve. Evaluate this argument: what does it claim, what evidence supports it, what evidence challenges it, and what would it imply for how a public health system should allocate resources between prevention, early detection, and treatment? State clearly where you think the evidence is genuinely unsettled and where it is not. [contested] *What this tests: engagement with a live scientific controversy, evidence evaluation, and the translation of epidemiological findings into resource-allocation reasoning.*

---

## Prompts

### Figure 3.1 — Attributable fraction of cancer by modifiable exposure
Build a ranked horizontal bar chart, bars proportional and starting from a zero baseline. Six categories, sorted descending by value: Tobacco 22 (vermillion, negative, highlighted as the leading bar), Infections 13, Obesity (high-income second-largest) 8, Alcohol 4, Radiation / UV 3, Occupational / environmental 2. X-axis unit: "% of global cancer deaths attributable," zero baseline required. Bars labeled with category on the left and value at the bar end. Keep all non-highlighted bars a single neutral blue; only tobacco takes the vermillion emphasis to mark it as the dominant preventable cause. No reference lines needed beyond the zero axis. Subtitle: "Tobacco is the leading preventable cause." Okabe-Ito semantics: vermillion for the highlighted dominant exposure, blue for the rest. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 3.2 — Mutational signatures as exposure fingerprints
Build a four-panel comparison grid, one row per carcinogen, each row pairing an exposure label (left) with a small mutation-type distribution sketch (right) under a shared axis label "Mutation-type distribution." Rows: (1) UV → "C→T at dipyrimidines (one dominant peak)" (sky-blue anchor); (2) Tobacco → "G→T transversions (peak at a different position)" (sky-blue anchor); (3) Aflatoxin → "G→T at a single TP53 codon (sharp spike)" (vermillion, negative); (4) MMR-deficiency / MSI → "Hypermutation, many bars, no single peak" (neutral secondary). Render each right-side fingerprint as a tiny bar-distribution: rows 1-2 a single tall peak at distinct positions, row 3 one very sharp narrow spike, row 4 many low even bars. Emphasis is on the contrast in shape, not absolute values. Subtitle: "Each carcinogen leaves a distinct mutation pattern." Okabe-Ito semantics: sky-blue anchors for UV/tobacco, vermillion for the aflatoxin spike, neutral for MSI. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 3.3 — Bradford Hill: causal inference vs a false positive
Build a two-column comparison matrix: rows are the Bradford Hill criteria, columns are two cases — "Smoking / lung cancer" (left) and "Beta-carotene / lung cancer" (right), under axis label "Bradford Hill criteria." Eight rows: Strength, Consistency, Specificity, Temporality, Biological gradient, Plausibility / coherence, Experiment, Analogy. In every cell mark satisfied vs reversed: the smoking column is satisfied (green) in all eight rows; the beta-carotene column is satisfied (green) in all rows except Experiment, which is "REVERSED by RCTs" (vermillion, negative). Use a clear checkmark/positive treatment for satisfied cells and a distinct vermillion cross/negative treatment for the single reversed cell so the eye lands on it immediately. Subtitle: "Smoking satisfies all nine; beta-carotene fails experiment." Okabe-Ito semantics: green for satisfied, vermillion for the reversed Experiment cell. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.
