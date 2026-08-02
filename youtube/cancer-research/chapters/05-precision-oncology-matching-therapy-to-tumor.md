# Chapter 5 — Precision Oncology: Matching Therapy to Tumor
*A Match Is a Hypothesis. The Response Is the Test.*

A 58-year-old never-smoker is diagnosed with metastatic lung adenocarcinoma. Comprehensive genomic profiling returns a *KRAS G12C* mutation. KRAS G12C is, on paper, an actionable alteration — sotorasib and adagrasib, approved in 2021 and 2022, target precisely this mutation. The molecular tumor board calls it a match. She starts sotorasib.

Her tumor shrinks for four months. Then it grows again. Repeat biopsy shows the KRAS G12C mutation is still present — but the tumor now carries new alterations in the downstream signaling pathway, and a subpopulation of cells has switched to a different growth driver entirely. The drug still binds its target. The target still drives part of the cancer. The cancer is winning.

Down the hall, a different patient with the same KRAS G12C mutation never responded at all. Same biomarker, same drug, zero shrinkage from day one.

Two patients, one alteration, two different failures. The match was real in both cases. The response was not durable in one and absent in the other. This is the gap between "matched" and "responded" — and understanding that gap is the whole subject of this chapter.

---

For most of oncology's history, drugs were assigned by tissue type. This chemotherapy regimen for everyone with this cancer, regardless of molecular features. Some patients responded. Others didn't. The difference was attributed to "biological variability" — which is a way of saying the field didn't know why.

**Precision oncology** is the reframing of that variability as molecular. The insight: the cancer's genetic and protein features, more than its tissue of origin, predict which drugs will work. The practice: sequence the tumor, identify a molecular feature shown in trials to predict response, and prescribe the matched drug.

A clarification before going further. *Precision* does not mean the treatment is unique to one patient. Two patients with the same alteration receive the same drug. The precision is in the molecular targeting, not in individual customization. **Personalized medicine** — which accounts for the whole patient, including comorbidities, preferences, and germline genetic background — is a related but stronger claim that remains largely aspirational in routine practice (NCI, *Targeted Therapy*).

An **actionable alteration** is the unit of precision oncology: a molecular feature for which a matched therapy exists and has demonstrated benefit. Actionable features include point mutations (*EGFR* exon-19 deletion, *BRAF* V600E, *KRAS* G12C), gene fusions (*ALK*, *ROS1*, *RET*, *NTRK*), copy-number changes (*HER2* amplification), expression patterns (estrogen receptor, PD-L1), and functional signatures (microsatellite instability, tumor mutational burden). The word *actionable* is load-bearing. It does not mean present. It means present and linked, by clinical evidence, to a drug that helps. A mutation you can detect but cannot exploit is interesting biology, not an actionable alteration.

---

The single most important distinction in this chapter — the one students most consistently collapse, and the one every clinical precision-oncology failure traces back to — is the difference between a **predictive biomarker** and a **prognostic biomarker**.

A **prognostic biomarker** tells you how the patient will fare, regardless of treatment. It forecasts the natural history of the disease. A patient with a high-grade tumor and lymphovascular invasion has a worse prognosis than one without — that is prognostic information. It does not tell you which therapy to use.

A **predictive biomarker** tells you whether a specific therapy will work in this patient. *EGFR* exon-19 deletion predicts response to osimertinib; it does not predict a better outcome across all treatments. *BRCA1/2* germline mutation predicts response to PARP inhibitors through synthetic lethality — the drug is lethal only in cells that have already lost one DNA repair pathway, so the homologous recombination deficiency that the mutation creates is the target (NCI, *Targeted Therapy*). The same *BRCA1/2* mutation is also prognostic for worse outcome in some settings. That is a different fact.

Precision oncology runs on predictive biomarkers. A feature can be both prognostic and predictive — *KRAS* mutation is a negative prognostic factor in colorectal cancer and, until recently, was considered non-actionable because no drug could block it. Conflating the two biomarker types produces a specific clinical error: treating a marker of *aggressive biology* as if it were a *drug target*. The feature predicts bad outcomes not because it drives a pathway you can block, but because it marks a tumor type that is inherently aggressive. Treating it does nothing. This is not a theoretical mistake; it drove years of failed KRAS clinical programs before G12C-specific covalent inhibitors showed that one specific KRAS variant was indeed actionable.

![Two-panel comparison of survival-curve pairs: a prognostic marker forecasts outcome regardless of treatment, a predictive marker shows benefit only in marker-positive patients](images/05-precision-oncology-matching-therapy-to-tumor-fig-01.png)
*Figure 5.1 — Predictive versus prognostic biomarker*

<!-- → [DIAGRAM: predictive versus prognostic biomarker — four-panel grid with biomarker-positive and biomarker-negative patients on the x-axis, treated and untreated on the y-axis; prognostic marker shows both treated groups worse than untreated, with parallel survival curves regardless of treatment; predictive marker shows treatment benefit diverging only in the biomarker-positive group; the divergence between the two graphs is labeled "the distinction that drives everything"] -->

---

The most evolved expression of predictive-biomarker logic is **tumor-agnostic therapy**: a drug approved to treat any cancer that carries a specific molecular feature, regardless of where in the body the cancer originated.

The first tumor-agnostic approval was pembrolizumab for **microsatellite-instability-high (MSI-H)** tumors in 2017 — approved based on response rates of roughly 30–50% in MSI-H cancers spanning colorectal, endometrial, gastric, biliary, and other sites (NCI, *Immunotherapy*). The claim: a tumor's mismatch-repair deficiency, not its tissue origin, predicts response to PD-1 blockade. Then larotrectinib and entrectinib for *NTRK* fusion-positive tumors (2018–2019); pembrolizumab for tumor-mutational-burden-high tumors at ≥10 mutations per megabase (2020); dabrafenib plus trametinib for *BRAF* V600E solid tumors (2022).

Each approval embeds the same claim: the biology is what matters; the tissue is incidental.

That claim is powerful and not without limits. The denominator behind a tumor-agnostic approval is typically a patchwork of small cohorts across many cancer types, assembled from basket trials and analyzed together. The pooled response rate looks like one number, but it may hide tissue-specific variation — responses that are strong in some histologies and weak in others, aggregated into an average `[verify — per-tissue response rates in NTRK and MSI-H approvals]`. "Agnostic" in the regulatory label does not mean uniform in the biology.

The *BRAF* V600E case is the clearest illustration of why tissue matters even within a tumor-agnostic framework. In melanoma, BRAF V600E predicts a strong, durable response to BRAF plus MEK inhibition — response rates above 60%. In colorectal cancer, the same mutation responds poorly to single-agent BRAF inhibition because feedback reactivation of EGFR restores the signaling the BRAF inhibitor blocked, requiring the addition of an anti-EGFR antibody to achieve even modest benefit. Same mutation, same approved drug class, profoundly different biology — because colorectal cancers have abundant EGFR signaling that melanomas do not, and that signaling provides a bypass route around BRAF blockade. The tissue that was supposed to be incidental turns out to matter after all, even for a mutation the label calls agnostic.

---

Precision oncology needed new trial designs because the molecular subgroups it works with are small and scattered across many cancer types. Conventional trials enroll patients by cancer type and compare one regimen to another. Molecular subgroups — patients with a specific fusion, a specific mutation — may be 1–5% of any given cancer type. Enrolling enough of them in a single-tumor trial would take decades.

**Basket trials** enroll patients by molecular alteration across many tumor types. A basket trial for *NTRK* fusions might enroll lung adenocarcinoma, thyroid cancer, sarcoma, and colon cancer — any tumor with the fusion, from any origin. The design that produces tumor-agnostic claims; larotrectinib and entrectinib reached approval through basket programs that enrolled patients regardless of histology.

**Umbrella trials** work in the opposite direction: they enroll one cancer type and subdivide patients into arms by molecular feature. Lung-MAP is the classic example — a non-small-cell lung cancer trial with multiple sub-studies, each testing a different drug in a different molecular subgroup. The umbrella design answers: does this matching work *within this cancer type*? It cannot make cross-tissue claims the way a basket can.

**Platform trials** maintain permanent infrastructure and add or drop treatment arms over time as evidence accumulates. I-SPY 2 in breast cancer tests experimental agents in molecularly defined subgroups, graduating agents showing promise to confirmatory trials and dropping those that do not. The platform design generates evidence efficiently across time.

Reading a precision-oncology result requires knowing which design produced it. A basket result is evidence for a biomarker across tissues — it supports a tumor-agnostic claim. An umbrella result is evidence for matching within a defined cancer type. Citing a basket result to justify treatment in a tumor type not represented in the basket is an extrapolation, not an evidence application.

![Three-panel comparison of basket, umbrella, and platform trial structures, each labeled with the evidence claim it supports](images/05-precision-oncology-matching-therapy-to-tumor-fig-02.png)
*Figure 5.2 — Basket vs umbrella vs platform trial designs*

<!-- → [DIAGRAM: basket versus umbrella versus platform trial designs — basket: three different tumor types enrolling to a single biomarker-defined arm, arrow pointing to tumor-agnostic approval; umbrella: one tumor type branching into three biomarker-defined arms, arrow pointing to tissue-specific matching; platform: a timeline showing arms added and dropped over time with a continuous infrastructure spine; each design labeled with its evidence claim] -->

---

Return to the first opening patient — KRAS G12C, sotorasib, four months of response, then progression. The first instinct when a matched treatment fails is to question the assay: perhaps the sequencing called a mutation that wasn't really there. This is always worth checking. Analytic validity — whether the test is reliably calling what it claims to call — is the foundation every precision decision rests on. But the repeat biopsy confirmed KRAS G12C was present at baseline and at progression. The test was right. The match was real. So the assay-error explanation fails here.

The productive reframing separates the *target* from the *tumor's dependence on that target over time*. At baseline the cancer was driven by KRAS G12C signaling, sotorasib blocked it, and the tumor shrank — the hypothesis "this tumor depends on KRAS G12C" was, for four months, confirmed by the response itself. Resistance emerged not because the drug stopped binding, but because the tumor evolved. Treatment is selection pressure. It does not act on a static tumor; it acts on a population under selection, and it selects for the cells capable of routing around the blockade. New downstream mutations restored the MAPK signal; a subclone adopted an entirely different driver. The drug still engaged its target. The cancer found another way to grow.

The second patient — same mutation, never responded — is a different story. The most likely explanation is a **co-occurring alteration** that made the cancer independent of KRAS G12C signaling from the start. If a tumor also carries a loss-of-function mutation in a tumor-suppressor pathway, or has activated a parallel oncogenic pathway, blocking KRAS G12C changes nothing — the proliferative signal arrives through a channel the drug doesn't touch. The biomarker was present; the dependency was not. Target presence and target dependence are different properties of the tumor.

KRAS G12C inhibitors are, by the field's own assessment, meaningful but not transformative — response rates in the 35–40% range for lung adenocarcinoma, well below the 60–80% response rates of EGFR or ALK inhibitors in their respective populations, and with resistance that develops reliably within months rather than years (NCI, *Targeted Therapy*). The contrast with those other targets is informative: EGFR-mutant and ALK-rearranged lung cancers are highly dependent on a single oncogenic driver, with few escape routes available. KRAS-mutant cancers are biologically more heterogeneous — co-occurring alterations are common, the downstream signaling more plastic, the escape options more numerous.

---

The pattern of success and failure across precision oncology is not random. It follows from the biology.

**Single-driver, oncogene-addicted cancers** have responded most dramatically. Chronic myeloid leukemia with BCR-ABL: imatinib produced response rates above 90% and changed a disease with median survival measured in years to one managed as a chronic condition. EGFR-mutant lung cancer: response rates above 60%, progression-free survivals of one to two years, with sequential generations of inhibitors extending benefit further. HER2-positive breast cancer: trastuzumab transformed a subtype with among the worst prognosis to one of the most treatable. *NTRK* fusion-positive tumors: larotrectinib response rates above 75% across all histologies, with responses so durable that some are described as potentially curative. In these settings, the cancer has concentrated its survival dependency on one molecular driver, the drug blocks that driver, and the cancer has limited escape options.

**Multi-driver, microenvironment-dominated cancers** have resisted. Pancreatic adenocarcinoma has been comprehensively sequenced; the dominant drivers are KRAS, TP53, SMAD4, and CDKN2A — none of them cleanly druggable with current small molecules, and the desmoplastic microenvironment blocks delivery of what drugs do reach the tumor. Glioblastoma has many alterations and few that drive a single dominant dependency. Triple-negative breast cancer has high mutation burden but heterogeneous drivers and limited targeted options. These cancers resist not because precision oncology doesn't apply, but because they lack the concentrated, druggable single dependency that makes the approach work.

The failure pattern is as informative as the success pattern. Precision oncology does not work by measuring more molecular features; it works when the features measured correspond to a genuine, durable dependency that the matched drug reliably disrupts.

---

Two patients with the same alteration. Three possible outcomes across the whole population of KRAS G12C patients: durable benefit, transient benefit followed by resistance, and no benefit at all from day one. The match identified a candidate dependency. Whether each patient's tumor actually depended on it — and kept depending on it — was an empirical question that the drug answered.

![Three diverging tumor-burden trajectories from one matched alteration: durable benefit, transient response then resistance, and primary non-response](images/05-precision-oncology-matching-therapy-to-tumor-fig-03.png)
*Figure 5.3 — Matched is not responded: three fates of one alteration*

This is why "matched" and "responded" are different measurements. The report says what alteration is present. It does not say whether the tumor depends on it. It does not say whether that dependency will persist under selective pressure. The match is a prediction, scored by the response, not a property readable off the sequencing panel.

The field is working toward pre-treatment tools that would close this gap: patient-derived organoid testing, AI-integrated multi-omic models that account for co-occurring alterations and expression context, functional assays of pathway dependence. None has yet reached the positive predictive value that would make the prediction reliable rather than probabilistic (NCI, *Research Areas*). Until they do, the match remains the hypothesis, and the response remains the test.

---

## Exercises

**Warm-up**

1. *[Recall — moderate]* Define predictive biomarker, prognostic biomarker, and actionable alteration in one sentence each. Then explain why conflating the first two produces a specific clinical error — give a concrete example of a feature that is prognostic but not (or not yet) predictive for a specific drug, and state what happens if you treat it as predictive.
*What this tests: whether you can distinguish the concepts mechanistically, not just definitionally — the example forces you to apply the distinction to a real case.*

2. *[Recall — moderate]* Name four tumor-agnostic approvals with their molecular feature, approximate pooled response rate, and the year of approval. Then explain in two sentences why a pooled response rate across many cancer types is a necessary but not sufficient description of what the drug actually does.
*What this tests: knowing the landmark approvals and understanding the epidemiological limitation of pooled rates — what the single number hides.*

3. *[Recall — moderate]* Distinguish basket, umbrella, and platform trial designs by what each enrolls and what evidence claim each can and cannot support. Your answer should make clear why a basket result cannot substitute for an umbrella result when a clinician wants to know whether a matching strategy works specifically in one cancer type.
*What this tests: trial-design literacy — matching the design to the evidence claim rather than treating all precision-oncology results as equivalent.*

**Application**

4. *[Apply — moderate-hard]* A patient with metastatic colorectal cancer has a BRAF V600E mutation. Their oncologist read that BRAF V600E responds to BRAF plus MEK inhibition in melanoma and proposes the same regimen. Explain, using the concept of bypass signaling and tissue-specific co-occurring features, why the melanoma response rate does not predict the colorectal cancer response rate — and what the correct treatment approach for BRAF V600E colorectal cancer is and why it differs.
*What this tests: applying the tissue-specificity problem within a tumor-agnostic framework — why "same mutation" does not mean "same response" across tissues.*

5. *[Apply — moderate-hard]* A patient with *NTRK* fusion-positive salivary gland cancer — a rare histology not represented in the larotrectinib basket trial — is offered larotrectinib based on the tumor-agnostic approval. Evaluate the strength of the evidence supporting that treatment decision: what does the basket trial establish, what is the extrapolation involved, and what information about *NTRK* biology would support or undermine the extrapolation?
*What this tests: applying basket-trial evidence to a histology not in the trial — understanding the difference between evidence application and evidence extrapolation.*

6. *[Apply — hard]* Design a molecular-profiling-to-treatment reasoning chain for a hypothetical never-smoker with metastatic lung adenocarcinoma. Name (a) the sequencing test you would order; (b) three alterations you would hope to find and the matched drug for each; (c) the expected response rate and durability where known; (d) one specific point in the chain where a "matched but didn't respond" outcome could arise and which mechanism you would suspect first. Mark anything you are uncertain about with `[verify]`.
*What this tests: end-to-end application of the precision-oncology framework to a specific clinical scenario; the [verify] requirement enforces intellectual honesty about the limits of your knowledge.*

**Synthesis**

7. *[Synthesis — hard]* The KRAS G12C case and the EGFR exon-19 deletion case both represent "matched therapies." Compare them across four dimensions: (1) the response rate in the indicated population; (2) the typical durability of response; (3) the most common resistance mechanisms; (4) what these differences reveal about the relative degree of oncogene addiction in each cancer. Your comparison should end with a one-sentence claim about what distinguishes a "good" actionable alteration from a merely "present" one.
*What this tests: comparative analysis of two actionable alterations using the oncogene-addiction concept; moving from empirical observations to a mechanistic generalization.*

8. *[Synthesis — hard]* Pembrolizumab was first approved for MSI-H tumors in 2017 and later for TMB-high tumors in 2020. Both are immunotherapy biomarkers, but the evidence base and the per-tissue response rates are different. Compare these two tumor-agnostic approvals across three dimensions: (1) the biological mechanism by which each biomarker predicts immunotherapy response; (2) the strength of the evidence supporting each approval (trial design, pooled response rate, per-tissue variation); (3) what the per-tissue variation tells you about whether "agnostic" is a biologically accurate description for each. Conclude with a recommendation about which approval you would rely on more confidently in a histology not represented in the pivotal trials, and why.
*What this tests: mechanistic comparison of two immunotherapy biomarkers; applying the evidence-quality argument to a clinical decision under uncertainty.*

**Challenge**

9. *[Challenge — very hard]* The "Still Puzzling" section asks why some patients with a textbook actionable alteration never respond at all — when the target is present and the drug demonstrably binds it — and why pre-treatment prediction of durability remains unsolved. Design a translational research program that would, for one specific alteration-drug pair of your choice, attempt to identify the molecular features in pre-treatment tumor biopsies that predict: (a) primary resistance (no response); (b) secondary resistance (initial response then progression); (c) durable benefit. Specify the cohort you would enroll, the multi-omic data types you would collect (genomic, transcriptomic, proteomic, spatial), the computational approach to identifying predictive features, and the validation strategy. Then explain what the program would need to demonstrate to justify using the resulting classifier to withhold the matched drug from a patient whose tumor carries the actionable alteration.
*What this tests: translating a fundamental precision-oncology problem into a research design; reasoning about the ethical and evidentiary threshold for using a predictive classifier to override a molecular match.*

---

## What Would Change My Mind

The central claim of this chapter is that a molecular match is a hypothesis about response, validated only by the response itself — that "matched" and "responded" are distinct measurements separated by an irreducible gap. What would revise this: a pre-treatment assay — likely multi-omic, integrating the alteration with co-occurring mutations, expression state, and microenvironment — that predicts response and durability for a targeted drug with accuracy high enough to act on (a positive predictive value above 80% for durable response, prospectively validated). If such an assay existed and held up across cancer types, the gap between "matched" and "responded" would largely close, and the match would become close to a guarantee rather than a hypothesis. Patient-derived organoid testing and AI-integrated multi-omic models are the current candidates; none has yet met that bar (NCI, *Research Areas*).

## Still Puzzling

- Why do some patients with a textbook actionable alteration never respond at all, when the target is present and the drug demonstrably binds it? Co-occurring alterations explain some cases, but not all `[contested — see pantry flag]`.
- What is the right denominator for a tumor-agnostic approval? Pooling across tissues maximizes statistical power but assumes a uniformity the biology may not honor. How small can a per-tissue cohort be before "agnostic" becomes a statistical artifact?
- Can resistance be predicted and pre-empted — combinations chosen at baseline to block the escape routes — or is treatment-driven evolution fast enough that we will always be one step behind?
- Why have cancers like pancreatic adenocarcinoma resisted precision approaches despite exhaustive molecular characterization? Is the limit the absence of druggable drivers, or our inability to drug the drivers that are present?

## References

- National Cancer Institute. *Targeted Therapy to Treat Cancer.* https://www.cancer.gov/about-cancer/treatment/types/targeted-therapies
- National Cancer Institute. *Immunotherapy to Treat Cancer.* https://www.cancer.gov/about-cancer/treatment/types/immunotherapy
- National Cancer Institute. *Tests and Procedures Used to Diagnose Cancer.* https://www.cancer.gov/about-cancer/diagnosis-staging/diagnosis
- National Cancer Institute. *Research Areas: Cancer Diagnosis.* https://www.cancer.gov/research/areas/diagnosis
- Eisenhauer, E. A., et al. (2009). New response evaluation criteria in solid tumours: Revised RECIST guideline (version 1.1). *European Journal of Cancer*, 45(2), 228–247.

---

## Prompts

### Figure 5.1 — Predictive versus prognostic biomarker
Build a two-panel comparison, left panel "Prognostic marker," right panel "Predictive marker." Each panel holds a pair of small survival curves (treated vs untreated) for marker-positive and marker-negative subgroups. Prognostic panel: treated and untreated curves stay close (treatment makes no difference); marker-positive curves sit lower (worse outcome) than marker-negative — the marker forecasts outcome regardless of therapy. Predictive panel: marker-positive shows the treated curve riding clearly above untreated (benefit), rendered in green; marker-negative shows treated and untreated curves overlapping (no benefit), in neutral gray. Use green for the place benefit appears and neutral for no-benefit; keep both panels on identical axes (survival vs time). Add a connecting caption between panels: "Treatment benefit only where the marker predicts it." Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 5.2 — Basket vs umbrella vs platform trial designs
Build a three-panel structural comparison. Panel 1 "Basket": several distinct tumor-type icons converging (arrows inward) into one biomarker-defined arm, then an arrow out to "Tumor-agnostic benefit" in green. Panel 2 "Umbrella": one tumor type diverging (arrows outward) into three biomarker-defined arms, arrow out to "Tissue-specific matching" in sky-blue. Panel 3 "Platform": a horizontal time spine with arms appearing and dropping off above it at different times, arrow out to "Continuous evolving evidence" in a secondary color. Each panel titled with structure on top and evidence claim on the bottom. The three panels should visually contrast convergent, divergent, and temporal architectures. Equal panel widths, shared visual vocabulary. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 5.3 — Matched is not responded: three fates of one alteration
Build a single line chart with three trajectories of tumor burden over time on treatment (x-axis: time on treatment; y-axis: tumor burden, with the treatment start at the left). All three start at the same point. Trajectory 1 descends and stays low — "Durable benefit," green. Trajectory 2 descends to a trough then climbs back up — "Transient response then resistance," a secondary color (e.g., orange). Trajectory 3 stays flat or rises from the start — "Primary non-response," vermillion. Direct-label each line at its right end. Add a horizontal reference line at baseline burden to make rising-above-baseline (progression) legible. Annotation: "Same alteration, same drug, three trajectories — the match is a hypothesis the response tests." Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.
