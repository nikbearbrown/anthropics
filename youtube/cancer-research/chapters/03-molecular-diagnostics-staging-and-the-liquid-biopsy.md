# Chapter 3 — Molecular Diagnostics, Staging, and the Liquid Biopsy
*The difference between a test that measures something and a test that should change what you do.*

The liquid biopsy report lands with the weight of authority. The oncologist ordered a circulating tumor DNA panel on the 67-year-old man with metastatic lung adenocarcinoma — tissue was insufficient for full profiling, and the blood test promised a way around that problem. The report flags two mutations: *DNMT3A* and *TP53*. No targetable lung driver. No EGFR. No ALK. No KRAS G12C.

A trainee reads the report and asks a reasonable question: *DNMT3A* mutations are common in blood cancers, not lung cancer. Should the patient be referred for a hematologic workup?

The oncologist pauses. *DNMT3A* is a cancer gene, but it is also one of the most common mutations found in **clonal hematopoiesis** — the age-related accumulation of mutated blood-cell clones that happens in almost everyone over sixty and has nothing to do with any tumor. The ctDNA assay draws plasma DNA from the blood. The plasma DNA contains fragments from all cellular sources — tumor cells, yes, but also the patient's aging white blood cells. The assay cannot, by itself, tell whether the *DNMT3A* signal came from a lung tumor cell or from a clonal blood-cell population. Acting on it as a tumor finding would send the patient down a pointless and frightening diagnostic path.

The absence of a targetable driver is also ambiguous. If this tumor sheds little DNA into circulation — which some tumors do, particularly smaller or less aggressive ones — the panel might report a clean result not because there is no EGFR mutation but because there was not enough tumor DNA in the tube to find it. The report looks authoritative. Whether anything in it should change a single clinical decision depends on questions the report does not answer.

This chapter is about those questions.

---

### Three kinds of validity — and why the third one is the hard one

A molecular test can be evaluated at three levels, and the failure to distinguish them is responsible for most of the errors in how molecular results get used in oncology.

**Analytic validity** is the first level: does the assay accurately measure what it claims to measure? If the report says EGFR exon 19 deletion present, is that deletion really in the sample, reproducibly, at the claimed sensitivity and specificity? This is a laboratory question about the instrument, the chemistry, and the quality of the specimen. It is answerable by technical validation studies. Most commercially available molecular tests pass this bar for the mutations they are designed to detect — the clinical-grade assay industry is now mature enough that analytic performance is rarely the limiting issue.

**Clinical validity** is the second level: does the measured result correlate with a clinical state or outcome? Does the presence of EGFR exon 19 deletion actually predict that the tumor will respond to an EGFR inhibitor? Does MRD positivity after colon cancer surgery actually predict recurrence? This is a clinical-epidemiological question, answered by observational studies and trials that measure both the molecular result and the clinical outcome in the same patients.

**Clinical utility** is the third level, and it is where most molecular tests fail or have never been tested: does *using* the test to guide decisions improve patient outcomes compared with not using it? Does ordering the test, and acting on the result, lead to longer survival, better quality of life, or fewer harms than not ordering it? This is the hardest bar to clear because it requires a controlled study where patient outcomes are compared between test-guided and non-test-guided decision-making — usually a randomized trial or a very carefully designed observational study.

The three levels are not interchangeable. A test can be analytically perfect and clinically valid but still lack demonstrated utility if the decision it informs does not actually improve outcomes, or if the treatment it prompts is harmful, costly, or not available. The *DNMT3A* mutation in the opening case has analytic validity — the mutation is genuinely present in the plasma DNA — but zero clinical validity as a lung tumor marker, because its most likely source is blood cells, not the tumor. It clears the first bar and fails the second.

This hierarchy is the organizing frame for every molecular test discussion in this chapter, and the reason clinical utility is emphasized throughout oncology regulation. A test that earns approval as a companion diagnostic has cleared all three levels for a specific decision in a specific cancer type. A test that appears on a broad genomic profiling panel has cleared the first two for most of its targets, and the third for some. A novel test with exciting preliminary data may have cleared only the first. Knowing which bar a test has cleared is the skill that converts a molecular report into a treatment decision — or keeps it from becoming one.

![Three sequential gates — analytic validity, clinical validity, clinical utility — narrowing toward the few tests that clear all three](images/03-molecular-diagnostics-staging-and-the-liquid-biopsy-fig-01.png)
*Figure 3.1 — The three-validity hierarchy*

---

### Companion diagnostics: the test is part of the drug

A companion diagnostic is a test whose results are necessary to safely and effectively use a specific therapeutic product. The FDA approves companion diagnostics alongside the drugs they accompany — which means the evidence for the test is the same evidence as the evidence for the drug, not a separate validation exercise.

The structure is important. In a clinical trial for an EGFR inhibitor in lung cancer, the patients enrolled are identified by EGFR mutation testing. The survival benefit is measured in those patients. The companion diagnostic approval says: patients identified by *this test* benefit from *this drug*, based on *these trial results*. Changing the test changes what the trial evidence applies to. This is why test standardization matters — a patient identified as EGFR-positive by a validated companion diagnostic assay is in the population the trial enrolled; a patient identified by a different assay with different performance characteristics may or may not be.

The canonical companion diagnostic pairings are now extensive. HER2 testing — immunohistochemistry or fluorescence in situ hybridization — for HER2-targeted antibodies in breast and gastric cancer. EGFR mutation testing for EGFR inhibitors in non-small-cell lung cancer. BRAF V600E testing for BRAF inhibitors in melanoma. BRCA1/2 testing for PARP inhibitors in ovarian, breast, pancreatic, and prostate cancer. The recent tumor-agnostic approvals are a structural shift: microsatellite instability-high (MSI-H) or mismatch-repair deficiency (dMMR) predicts response to pembrolizumab regardless of tumor type, and NTRK fusion-positive cancer predicts response to TRK inhibitors regardless of histology. The biomarker, not the organ, is the selection criterion.

The technological infrastructure behind comprehensive companion diagnostic testing is next-generation sequencing — high-throughput parallel sequencing that reads millions of short DNA fragments and can characterize hundreds of genes from a single specimen. Comprehensive genomic profiling reports provide a complete catalog of a tumor's mutations, copy-number changes, and structural rearrangements in a single test, enabling identification of both established companion-diagnostic targets and novel findings that might qualify patients for clinical trials.

The companion diagnostic logic has a precise implication for the analytic validity requirement: the assay used to identify patients for treatment must be analytically comparable to the assay used in the trial that established the treatment benefit. If the trial enrolled EGFR-positive patients using a tissue PCR assay with a specific sensitivity, a different assay with a different sensitivity applied to a different sample type may identify a different patient population. The test is embedded in the evidence chain, not separable from it.

---

### Staging: organizing what you know about extent

Once a cancer is confirmed, the next task is describing its extent. Staging is the formal system for doing this — a structured summary of how much disease is present, where it is, and what that implies for prognosis and treatment.

The dominant system is TNM, maintained by the American Joint Committee on Cancer. **T** describes the primary tumor: its size, depth of invasion, and invasion of local structures. **N** describes involvement of regional lymph nodes: whether they are involved and how many. **M** describes distant metastasis: whether the cancer has spread beyond the regional node basin. These three dimensions combine into stage groups — conventionally 0 through IV — that summarize the clinical picture in a single number.

Two versions of TNM staging capture different information at different points in the clinical course. **Clinical staging** uses information available before surgery: physical examination, imaging, any biopsies performed. **Pathological staging** uses the resected specimen — the actual tumor, the actual lymph nodes, examined by the pathologist. Pathological staging is often higher than clinical staging because surgery reveals disease that imaging missed: lymph nodes that appeared normal on CT turn out to contain microscopic tumor deposits; the tumor's true depth of invasion is visible only in the specimen. This upstaging is not a failure of imaging — it reflects the fundamental limitation of seeing inside a body without removing the tissue.

Stage is a prognosis summary, not a treatment prescription. Patients with the same stage can receive different treatments based on fitness, preferences, and biology. Patients with different stages can receive the same treatment if the biology is comparable. What staging provides is a standardized vocabulary for communication and a structure for comparing outcomes across populations and across trials.

The staging system has evolved to incorporate biology alongside anatomy, and the AJCC 8th edition made this explicit. Breast cancer staging now incorporates hormone receptor status, HER2, and the Oncotype DX recurrence score — a genomic test measuring expression of 21 genes — into **prognostic stage groups** that can differ from anatomic stage. A patient with a small, node-negative, hormone-receptor-positive, HER2-negative breast cancer with a low Oncotype DX score may be assigned a lower prognostic stage than her TNM alone would suggest, reflecting the favorable biology overriding the anatomy. Prostate cancer staging now incorporates PSA level and Gleason score — the pathological grade of the tumor's differentiation — for the same reason: anatomy alone understates how much biology determines what happens to the patient.

**Grade** measures something distinct from stage. Grade is a pathologist's assessment of how closely the tumor cells resemble normal tissue — well-differentiated tumors look almost normal under the microscope; poorly differentiated tumors are recognizable as cancer but have lost most of the organizational features of the tissue of origin. The Gleason score for prostate cancer, the Nottingham grade for breast cancer, and the WHO grade for brain tumors are all grading systems. Stage is how much disease is present; grade is how biologically aggressive it looks. Both matter independently for prognosis, and both appear in modern staging systems.

![Hierarchy in which tumor, node, and metastasis dimensions plus molecular modifiers feed into a stage group I-IV](images/03-molecular-diagnostics-staging-and-the-liquid-biopsy-fig-02.png)
*Figure 3.2 — TNM staging with molecular modifiers*

<!-- → [DIAGRAM: TNM staging framework. Three columns: T (primary tumor — rows showing T1-T4 with increasing size/invasion), N (regional lymph nodes — N0/N1/N2/N3 with increasing node involvement), M (distant metastasis — M0/M1). Center: combination rules mapping TNM combinations to Stage I through IV. Right sidebar: molecular factors now incorporated into specific cancers — breast (ER/PR, HER2, Oncotype DX score), prostate (PSA, Gleason). Caption: "stage I through IV = anatomic summary; molecular factors modify the summary where biology overrides anatomy."] -->

---

### The liquid biopsy: what blood can and cannot tell you

Circulating tumor DNA is shed into the bloodstream by tumor cells — released when cells die and fragment, or through active secretion — and can be detected in plasma at concentrations that depend on the tumor's size, shedding rate, vascularity, and location. Detecting and characterizing ctDNA in a blood sample is the liquid biopsy, and it offers properties that tissue biopsy cannot.

The arguments for liquid biopsy are real. A single tissue biopsy samples one location in one lesion at one moment in time. A tumor with spatial heterogeneity — different mutations in different regions — will be incompletely characterized by any single needle. A metastatic cancer with multiple lesions may have genetically diverged sites, and a biopsy of one does not characterize the others. ctDNA, by contrast, aggregates DNA from all shedding tumor cells across all lesions, potentially capturing the heterogeneity that one tissue biopsy misses. This is a genuine advantage for monitoring evolution and detecting resistance mutations — the EGFR T790M resistance mutation that emerges under first-generation EGFR inhibitor therapy in lung cancer was one of the first clinical demonstrations that resistance monitoring via ctDNA was both feasible and clinically useful, prompting a switch to osimertinib.

The liquid biopsy is also repeatable without invasive procedures. Monitoring therapy response, detecting molecular evidence of recurrence after curative-intent treatment, and tracking clonal evolution over months or years are all logistically practical by blood draw in a way that repeat tissue biopsies are not. The DYNAMIC trial tested whether ctDNA-guided decision-making for adjuvant chemotherapy in stage II colon cancer could reduce treatment without sacrificing outcomes — patients with undetectable ctDNA after surgery were spared chemotherapy, and the recurrence-free survival of the guided arm was non-inferior to standard care while reducing chemotherapy use. This is clinical utility evidence, not just analytic or correlative.

The limitations are the ones the opening case displayed, and they matter enough to name precisely.

**Low tumor shedding** is a biological floor on the test's sensitivity that the assay design cannot overcome. Small tumors, early-stage disease, certain histologic types, and anatomic locations with limited vascular access — notably brain tumors, which shed minimal ctDNA across the blood-brain barrier — produce low ctDNA concentrations. A negative liquid biopsy in these settings is not evidence of absent disease; it is evidence of a tumor that is not currently shedding at the assay's detection limit. The distinction matters enormously for how the result is communicated to patients.

**Clonal hematopoiesis** is the specific confounder that the opening case illustrated. Aging blood cell progenitors accumulate somatic mutations, and some of those mutations are in genes associated with hematologic malignancy — *DNMT3A*, *TET2*, *ASXL1*, *TP53*. In a patient over sixty, the prevalence of at least one clonal hematopoiesis mutation detected in plasma DNA is substantial and increases with age. These mutations appear in the plasma because they are present in the white blood cells from which plasma DNA is partly derived. A liquid biopsy panel that detects *DNMT3A* or *TP53* in an elderly patient with a solid tumor may be detecting clonal hematopoiesis rather than tumor — or may be detecting both, with no way to distinguish them without sequencing the white blood cells separately. Most current ctDNA assays are designed to flag this potential confounder, but it remains a source of misinterpretation when reports are read without attention to the patient's age and mutation context.

![Schematic showing tumor and aging white-cell fragments both feeding a plasma cfDNA pool whose flagged mutation has untraceable origin](images/03-molecular-diagnostics-staging-and-the-liquid-biopsy-fig-03.png)
*Figure 3.3 — Two sources of plasma DNA*

**Absence of architectural information** is a categorical limitation, not a technical one. ctDNA can tell you that a mutation is present but cannot tell you where in the tumor it is, what proportion of cells carry it, how deeply the tumor has invaded, or whether the margin of a resection is clear. Tissue pathology provides information about cellular organization, stromal context, grade, and spatial relationships that no molecular test on cell-free DNA can replicate. Liquid biopsy and tissue pathology are complementary, not competitive.

**Unproven utility for emerging applications** is where epistemic honesty requires resisting the momentum of the technology. Multi-cancer early detection — the aspiration that a blood test could screen for many cancers simultaneously in asymptomatic people — is scientifically plausible and commercially active. Several large prospective trials are underway. The analytic validity of current MCED tests is established. Some clinical validity data — correlations between test results and confirmed cancers — is accumulating. Clinical utility evidence that MCED-guided screening reduces cancer mortality in a real population has not yet been established. The same three-validity discipline that justified MRD-guided adjuvant de-escalation in colon cancer has not been satisfied for population screening with MCED. Enthusiasm for the technology is not evidence for the decision.

---

### The colon cancer MRD decision

The DYNAMIC trial result is worth examining as a worked demonstration of how clinical utility is established — not because colon cancer is the main topic, but because the trial's design illustrates exactly what it takes to convert a correlation into a permission to act.

The prior evidence at the start of DYNAMIC was: ctDNA is detectable after colon cancer resection in some patients and predicts recurrence in those patients. That is clinical validity. The question DYNAMIC asked was different: if you use ctDNA status to decide whether to give adjuvant chemotherapy — giving it to MRD-positive patients and withholding it from MRD-negative patients — do patient outcomes differ from the standard approach?

This is a utility question, and it requires a randomized design because the comparison is between decision strategies, not between patients with and without ctDNA. The trial randomized patients to ctDNA-guided management or standard management, then measured recurrence-free survival and chemotherapy usage in both arms. The result — non-inferior recurrence-free survival with fewer patients receiving chemotherapy in the guided arm — established utility for this specific decision in this specific cancer.

The scope of that utility is exactly as wide as the trial: stage II colon cancer, postoperative adjuvant chemotherapy decision. The same MRD assay used in a different cancer, at a different decision point, or for a different purpose — surveillance, screening, intraoperative monitoring — requires its own utility evidence. The trial's result does not generalize to contexts the trial did not measure.

This is not overly restrictive epistemology. It is the structure that prevents a useful test in one context from being deployed harmfully in another. Precision in defining what a test is for is as important as precision in the test itself.

---

### When a molecular result earns the right to change a decision

The chapter's practical question is how to convert a molecular report — authoritative-looking, often lengthy, frequently annotated with "variants of uncertain significance" — into the small set of actionable findings that should change clinical management.

The three-validity framework provides the filter. For each finding in a report: is this analytically valid in this specimen type with this assay? Is it clinically valid as a marker in this cancer type? Is there clinical utility evidence for using it in this specific decision context?

Most findings in a comprehensive genomic profiling report fail the third test in most contexts. A *PIK3CA* mutation is present, real, and associated with potential sensitivity to PI3K inhibitors — but the utility evidence for PI3K inhibitor therapy in a given tumor type at a given line of therapy may be limited or absent. The mutation is a hypothesis for a clinical trial, not a treatment directive. A variant of uncertain significance — a mutation observed in the tumor but with no established clinical consequence — fails the second test. It is real, but it is not known to mean anything.

What earns the right to change a decision: a mutation with a companion diagnostic approval for the specific drug in the specific indication, where the patient's tumor expresses the marker at the level the approval requires. MSI-H status predicts pembrolizumab response across tumor types — that utility is established. EGFR exon 19 deletion predicts osimertinib benefit in first-line lung adenocarcinoma — that utility is established. A BRCA2 mutation in a patient with metastatic pancreatic cancer who might qualify for olaparib — utility is established in that indication.

What does not automatically earn the right to change a decision: a mutation found on a broad panel that has a drug in a different tumor type but not this one. A ctDNA finding in a context where the shedding rate is unknown and the clinical validity for this specific application has not been demonstrated. A finding that matches a phase I trial that may or may not be relevant to this patient's specific biology.

The discipline is not cynicism about molecular testing. The companion diagnostics work. The MRD-guided colon cancer adjuvant approach works. The radioligand theranostics built on molecular imaging work. Each of these succeeded because the three-validity chain was followed, not because the technology was sophisticated. Sophistication of measurement is not a substitute for evidence of benefit.

---

## Exercises

**Warm-up**

1. *(Recall — difficulty: low)* Define analytic validity, clinical validity, and clinical utility in one sentence each. For each level, give one example of a test that has that level established — and, where possible, give one example of the *same* test in a context where a higher level has not yet been established. *What this tests: whether you can hold the three levels as distinct rather than treating validation as a unified category.*

2. *(Recall — difficulty: low)* What is clonal hematopoiesis, and why does it confound liquid biopsy interpretation in older patients? Name two gene mutations commonly associated with it, and explain what additional test would allow a clinician to determine whether a plasma DNA finding came from tumor or blood cells. *What this tests: the specific mechanism of the opening case's confound before applying it to novel scenarios.*

3. *(Recall — difficulty: low)* What did the DYNAMIC trial test, and what did it demonstrate? State the conclusion precisely — not "MRD testing is useful" but what specific decision, in which specific cancer type, at which specific clinical timepoint, was shown to be safely guided by ctDNA status. *What this tests: decision-specific and cancer-specific scoping of utility evidence.*

**Application**

4. *(Apply — difficulty: medium)* A ctDNA panel on a patient with metastatic breast cancer returns an ESR1 mutation. Explain what ESR1 mutations are associated with biologically, then list two reasons — one biological, one technical — why you would want additional evidence before changing the patient's hormone therapy regimen on the basis of this single plasma result. State what that additional evidence would be. *What this tests: the three-validity framework applied to a specific, clinically common ctDNA finding.*

5. *(Apply — difficulty: medium)* A patient has a newly resected stage II colon cancer. Post-surgical ctDNA is negative. A family member who has read about liquid biopsy asks whether this means the cancer is cured and chemotherapy can definitely be skipped. Write a one-paragraph response that accurately represents what the negative result means, what it does not mean, and what the clinical decision-making process looks like. Use the DYNAMIC trial evidence appropriately without overstating it. *What this tests: communication of a probabilistic molecular result, specifically the distinction between "below detection threshold" and "zero residual disease."*

6. *(Apply — difficulty: medium)* A comprehensive genomic profiling report for a patient with metastatic pancreatic cancer includes KRAS G12D mutation, TP53 mutation, CDKN2A deletion, SMAD4 deletion, and — flagged as potentially actionable — a BRCA2 pathogenic variant. Of these five findings, which has the strongest companion-diagnostic utility evidence for a currently available FDA-approved treatment, and what is that treatment? What additional information about the patient would you need before acting on the BRCA2 finding? *What this tests: applying the companion-diagnostic framework to a real multi-alteration genomic report.*

**Synthesis**

7. *(Synthesize — difficulty: high)* A new comprehensive genomic profiling test reports that 45 percent of patients with advanced cancers across all tumor types carry at least one "actionable alteration." A colleague concludes that nearly half of all cancer patients could benefit from targeted therapy. Construct a careful critique of this conclusion by: (a) identifying what "actionable alteration" means at each of the three validity levels, (b) explaining the gap between having an actionable alteration and receiving a beneficial treatment, and (c) specifying what study design would be required to generate utility evidence for the claimed benefit. *What this tests: integration of the three-validity framework with the companion-diagnostic logic to evaluate a specific empirical claim.*

8. *(Synthesize — difficulty: high)* Compare the clinical utility evidence for three uses of ctDNA: (a) resistance monitoring — detecting EGFR T790M emergence to prompt osimertinib switch; (b) MRD-guided adjuvant de-escalation — the DYNAMIC trial approach; (c) multi-cancer early detection in asymptomatic individuals. For each, state what level of clinical validity has been established, what clinical utility evidence exists or is pending, and what the consequences of acting or not acting on the result are for individual patients and populations. Conclude with a ranking of these three uses by current strength of clinical utility evidence and explain the ranking. *What this tests: differentiated evaluation of ctDNA utility across three clinically distinct applications — demonstrating that the same technology requires separate evidence for each use.*

**Challenge**

9. *(Challenge — difficulty: high)* The three-validity framework requires separate utility evidence for each test in each decision context in each cancer type. Critics argue this standard is too demanding for molecular diagnostics in oncology — that it would have delayed companion diagnostics by years, that randomized trials of test-guided versus non-guided decisions are often ethically or logistically impossible, and that when the mechanism is well-understood (EGFR mutation → EGFR inhibitor sensitivity), utility can reasonably be inferred. Defenders of the standard argue that too many molecular tests have been adopted into clinical practice based on analytic and clinical validity alone, generating costs, anxiety, and sometimes harm without demonstrated benefit. Evaluate both positions: what arguments and evidence support each, what the consequences of each standard would be for patients and for the field, and whether there is a middle position that preserves the core of utility-based evaluation while accommodating cases where randomized utility evidence is genuinely impractical. State your own view and identify the single most important unresolved empirical question that would most influence the answer. *What this tests: engagement with a genuine methodological debate in clinical genomics, the relationship between mechanistic reasoning and empirical evidence, and the translation of evaluative standards into policy implications.*

---

## Prompts

### Figure 3.1 — The three-validity hierarchy
Build a left-to-right flow of three sequential gates that visibly narrows at each step: (1) Analytic validity — measures accurately; (2) Clinical validity — correlates with state; (3) Clinical utility — acting improves outcomes. Connect with right-pointing arrows labeled "narrows." Render gates 1 and 2 in green (passable bars) and gate 3 in blue as the dominant, hardest gate. Show the channel literally thinning: make each successive node or the connecting band smaller, with peeled-off "rejected tests" arrows dropping away below each gate in vermillion. Add annotation: "Most tests stall at utility." This is a funnel-style flow; keep one horizontal axis, no data values, structural only. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 3.2 — TNM staging with molecular modifiers
Build a top-down hierarchy (converging tree drawn upward to a single root). Root at top: "Stage group (I-IV)" in blue as the dominant summary node. Four children feeding into it from below: "Tumor (T1-T4)," "Nodes (N0-N3)," "Metastasis (M0/M1)" as sky-blue anchor nodes, plus "Molecular modifiers" rendered in a distinct transitional color (e.g., orange) and connected with a dashed edge to signal it overlays/overrides the anatomic three. Edges converge from the four children up into the root. Add caption: "Anatomy combines into stage; biology can override." Keep the three anatomic nodes visually grouped and the molecular node set slightly apart. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 3.3 — Two sources of plasma DNA
Build a node-edge convergence schematic. Two source nodes on the left: "Tumor (target signal)" in blue as the dominant intended source, and "White cells / clonal hematopoiesis" in a secondary gray. Both send labeled "fragments" arrows into a central node "Plasma cfDNA pool." From the pool, one arrow labeled "origin untraceable" points to a right-hand node "Flagged mutation," rendered in vermillion to signal the interpretive hazard. The visual point: once pooled, the two inputs are indistinguishable — draw the two inbound edges merging into one before the readout. Add annotation: "A plasma mutation may not have come from the tumor." Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.
