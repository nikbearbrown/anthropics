# Chapter 32 — Precision Oncology: Matching Therapy to Tumor


## TL;DR

- The right drug for the wrong cancer is the wrong drug.
- The chapter moves through What precision oncology means, Tumor-agnostic therapy, Biomarker-defined patient populations, Clinical trial frameworks for precision oncology, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

The right drug for the wrong cancer is the wrong drug.

Hold the inversion. For most of cancer therapy's history, drugs were assigned by tumor type — chemotherapy for everyone with this cancer, regardless of how their particular cancer might respond. The approach worked imperfectly. Some patients responded; others didn't, with similar tumors but different underlying biology. The variability was attributed to "biological variability" — a placeholder for ignorance about what actually distinguished responders from non-responders.

The reframing of the past two decades is that the variability is not random. It is *molecular*. Specific genetic alterations, specific protein expression patterns, specific biomarker statuses determine whether a given drug will work in a given patient. Two patients with histologically identical lung adenocarcinoma may have very different responses to standard chemotherapy or to targeted therapy based on whether they carry an EGFR mutation, an ALK rearrangement, a KRAS G12C mutation, or no targetable alteration. The cancer's molecular profile, more than its histological diagnosis alone, determines the appropriate treatment.

This is the foundation of *precision oncology* — sometimes called *personalized medicine* or *precision medicine*. The framework matches specific therapies to specific tumor features. It is informed by the molecular diagnostics covered in Chapter 18B and operationalized through the multidisciplinary infrastructure covered in 19A. The result is improved outcomes for patients who carry actionable alterations and a more efficient use of expensive therapies (since the drugs are given to patients most likely to benefit).

This chapter — the second on principles of cancer therapy — covers precision oncology in detail. The biomarker-driven treatment paradigms that have emerged across cancer types. The implementation infrastructure required to make precision oncology accessible. The clinical trials framework that has evolved to test biomarker-defined therapies. The integration with immunotherapy. The challenges remaining, including resistance, access disparities, and the cancers that haven't yet benefited from precision approaches.

Hold the question: *if the optimal treatment for every cancer is determined by its molecular features, what infrastructure and decisions translate this idea into care for every patient?*

---

## What precision oncology means

The terms "precision medicine" and "personalized medicine" are sometimes used interchangeably. They mean similar but slightly different things.

*Precision medicine* refers to using precise molecular information to make treatment decisions. The treatment may not be unique to the individual; multiple patients with the same molecular feature may receive the same treatment. The "precision" refers to the molecular targeting, not to individual customization.

*Personalized medicine* implies treatment tailored to the individual, accounting for that person's specific tumor profile, genetic background, comorbidities, and preferences. The treatment for two patients with similar molecular features might still differ based on these other factors.

The current oncology landscape is mostly precision medicine — defined molecular biomarkers identify subgroups for specific therapies. True personalization, customizing treatment to individual factors beyond the obvious biomarkers, is emerging but limited.

Beyond the terminology, the framework involves several elements:

*Identification of actionable alterations*. Specific molecular features in cancers that correlate with response to specific therapies. These include genetic mutations (EGFR, BRAF, KRAS, BRCA1/2, others), gene fusions (ALK, ROS1, RET, NTRK), copy number alterations (HER2 amplification, MET amplification), expression patterns (ER, PR, HER2, PD-L1), and functional features (microsatellite instability, tumor mutational burden, homologous recombination deficiency).

*Diagnostic infrastructure*. Tests to detect these alterations reliably, comprehensively, and quickly. NGS-based comprehensive genomic profiling, multiplex IHC, liquid biopsy, methylation profiling, expression profiling.

*Therapeutic options*. Drugs that target each actionable alteration. Many FDA-approved drugs exist; many more are in clinical trials.

*Treatment decision-making*. Frameworks for matching patients to therapies based on their molecular profile. This involves clinical guidelines, molecular tumor boards, clinical trial access, and decision support tools.

*Outcomes measurement*. Tracking the outcomes of patients treated with biomarker-driven approaches to refine the framework over time.

---

## Tumor-agnostic therapy

A particularly elegant manifestation of precision oncology is *tumor-agnostic therapy* — drugs approved for use across cancer types based on a molecular feature, regardless of the tissue of origin.

The first tumor-agnostic approval was *pembrolizumab for microsatellite-instability-high (MSI-H) tumors* in 2017. The approval was based on response rates around 30-50 percent in MSI-H tumors across many different cancer types — colorectal, endometrial, gastric, biliary tract, others. The defining feature was the molecular biomarker, not the tissue.

Subsequent tumor-agnostic approvals:
- *Larotrectinib* (2018) and *entrectinib* (2019) for NTRK fusion-positive tumors. NTRK fusions are rare but, when present, predict dramatic response to TRK inhibitors regardless of cancer type.
- *Pembrolizumab for tumor mutational burden-high* (TMB-H, ≥10 mutations/megabase) tumors (2020). The decision was based on response rates exceeding the typical TMB-defined cutoff across multiple cancer types.
- *Dabrafenib + trametinib* for BRAF V600E-positive solid tumors (2022). Originally approved for melanoma, then for thyroid cancer, lung cancer, and others, finally for any solid tumor with BRAF V600E.
- *Selpercatinib* for RET-altered cancers across tumor types (2022).
- *Entrectinib* for ROS1-positive cancers including non-NSCLC.
- *Repotrectinib* for ROS1-positive lung cancer and NTRK-positive solid tumors.

The tumor-agnostic concept extends precision medicine beyond its tissue-based history. The biology is what matters; the tissue location is incidental. This reframing has been one of the conceptually significant developments of the past decade.

The clinical implementation requires molecular profiling of cancers regardless of cancer type. The detection of NTRK fusions, for instance, requires either NGS profiling or specific IHC/FISH testing. The accessibility of such testing across cancer types is variable; broadening access is a major equity issue.

---

## Biomarker-defined patient populations

The major biomarker-defined populations in current oncology practice:

*HER2-positive cancers*. Breast cancer (15-20% are HER2-positive), gastric/gastroesophageal junction cancer (~20%), colorectal cancer (~3%), endometrial cancer (~10% in some subgroups), and others. HER2-targeted therapies include trastuzumab, pertuzumab, T-DM1, T-DXd, lapatinib, neratinib, tucatinib, margetuximab. The development of these drugs (especially T-DXd, an antibody-drug conjugate) has dramatically extended survival in HER2-positive cancers.

*Hormone receptor-positive cancers*. Estrogen receptor (ER) and progesterone receptor (PR) status in breast cancer determines hormone therapy use. Standard agents include tamoxifen (for premenopausal), aromatase inhibitors (for postmenopausal), fulvestrant. Combined with CDK4/6 inhibitors, hormone therapy has substantially improved outcomes in HR-positive metastatic breast cancer.

*BRCA-mutant cancers*. Germline or somatic BRCA1/2 mutations in breast, ovarian, pancreatic, and prostate cancer predict response to PARP inhibitors (olaparib, talazoparib, niraparib, rucaparib). The synthetic lethal mechanism (Chapter 6) underlies the response. PARP inhibitors have become standards of care in BRCA-mutant cancers and are being extended to other homologous recombination-deficient tumors.

*EGFR-mutant non-small-cell lung cancer*. Specific EGFR mutations (exon 19 deletions, L858R, T790M, exon 20 insertions, C797S) determine sensitivity to different EGFR inhibitors. Osimertinib has become standard first-line therapy for sensitizing EGFR mutations. Mobocertinib for exon 20 insertions. The treatment landscape is sophisticated, with sequential use of different generations of EGFR inhibitors as resistance develops.

*ALK-rearranged lung cancer*. ALK fusions in lung adenocarcinoma. ALK inhibitors (crizotinib, alectinib, brigatinib, ceritinib, lorlatinib) have transformed outcomes for this molecular subtype.

*ROS1-rearranged lung cancer*. ROS1 fusions. Crizotinib, entrectinib, repotrectinib provide effective therapy.

*BRAF V600E-mutant cancers*. Melanoma (most common), thyroid cancer, hairy cell leukemia, colorectal cancer (with cetuximab combination), some others. BRAF + MEK inhibitor combinations (dabrafenib + trametinib, encorafenib + binimetinib, vemurafenib + cobimetinib) provide substantial benefit.

*KRAS G12C-mutant cancers*. Approximately 13% of lung adenocarcinomas. Sotorasib and adagrasib were approved in 2021 and 2022 respectively. The activity is meaningful but not dramatic; resistance develops.

*FGFR-altered cancers*. FGFR2 or FGFR3 alterations in cholangiocarcinoma, urothelial cancer, others. Pemigatinib, infigratinib, futibatinib for cholangiocarcinoma; erdafitinib for urothelial cancer.

*RET-altered cancers*. RET fusions or RET point mutations. Selpercatinib, pralsetinib are approved for RET-mutant thyroid cancer and RET fusion-positive lung cancer.

*NTRK fusion-positive cancers* (tumor-agnostic). Larotrectinib, entrectinib.

*MET-altered cancers*. MET exon 14 skipping mutations, MET amplification. Capmatinib, tepotinib for MET exon 14-mutant lung cancer.

*PI3K-altered breast cancer*. PIK3CA mutations. Alpelisib for hormone receptor-positive breast cancer.

*IDH-mutant cancers*. IDH1 and IDH2 mutations. Ivosidenib and enasidenib for AML; ivosidenib for cholangiocarcinoma.

*MSI-H/dMMR cancers* (tumor-agnostic). Pembrolizumab, dostarlimab, and other immune checkpoint inhibitors.

*TMB-H cancers* (tumor-agnostic). Pembrolizumab for tumor mutational burden ≥10 mut/Mb.

*PD-L1 high cancers*. Various PD-1 and PD-L1 inhibitors for cancers with high PD-L1 expression.

The list is partial and growing. Each year brings new biomarker-defined approvals. The cumulative effect is that for most metastatic cancers, the optimal treatment increasingly depends on molecular profiling rather than tumor type alone.

---

## Clinical trial frameworks for precision oncology

Traditional clinical trials enrolled patients by tumor type. Precision oncology has driven new trial frameworks that focus on molecular features.

*Basket trials* enroll patients with a specific molecular alteration regardless of cancer type. The same trial might include patients with NTRK fusions in many different tumor types. If the drug works across the molecular biomarker, the trial can produce a tumor-agnostic approval. Larotrectinib and entrectinib were approved through basket trial designs.

*Umbrella trials* enroll patients with a specific cancer type and assign them to different treatment arms based on their molecular features. The Lung-MAP trial in non-small-cell lung cancer is the classical example. Patients with the same cancer type are matched to different targeted therapies based on their genomic profile.

*Master protocols* combine basket and umbrella elements, sometimes with adaptive features that allow the trial design to change based on accumulating data.

*Adaptive trial designs* allow modification of the trial based on early results. The dose may be adjusted, arms may be added or dropped, randomization ratios may change. Adaptive designs are useful when the optimal dose or schedule is uncertain at trial initiation.

*Platform trials* maintain a permanent infrastructure (eligible patients, standardized assessments, central data management) and allow new treatment arms to be added over time. The I-SPY 2 trial in breast cancer is an example.

The trial frameworks have evolved because precision oncology requires identifying small molecular subgroups across many cancer types. Traditional single-arm, single-tumor-type trials cannot efficiently identify and validate biomarker-defined therapies.

The infrastructure to support these trial frameworks — central molecular profiling, real-time data sharing, multi-institutional collaboration, adaptive analytics — is being built but is uneven across institutions and geographic regions.

---

## Implementation infrastructure

The translation of precision oncology from concept to practice requires substantial infrastructure.

*Molecular profiling at scale*. Comprehensive genomic profiling for every newly diagnosed metastatic cancer. The diagnostic capacity exists in major academic centers; smaller centers and many community practices have variable access. Reimbursement for testing is increasing (Medicare and most commercial insurers cover NGS-based profiling for many cancers) but remains inconsistent.

*Bioinformatics and interpretation*. Translating raw sequencing data into clinically actionable reports. The variant interpretation requires evolving knowledge bases (OncoKB, CIViC, COSMIC) that link genetic alterations to clinical implications. Many institutions use commercial profiling companies that provide both the testing and the interpretation.

*Molecular tumor boards*. As described in 18B, multidisciplinary review of molecular profiling results. The expertise required is real and not universally available.

*Decision support tools*. Software that integrates patient clinical data, molecular profile, and current therapeutic landscape to suggest treatment options. Several commercial and academic tools exist (PharmGKB, MyCancerGenome, Watson for Oncology). The quality and integration varies.

*Clinical trial matching*. Linking patients to appropriate clinical trials based on their molecular profile. Matching tools exist but the implementation is uneven. Many patients with actionable alterations are not enrolled in trials they would qualify for.

*Patient navigation*. Patients with cancer often face complex care pathways. Navigators help coordinate appointments, explain options, manage logistics. The role is particularly important for precision oncology with its multiple specialty involvements.

*Reimbursement and access*. The cost of molecular profiling and the cost of targeted therapies create access challenges. Some targeted drugs cost over $10,000 per month. Patient assistance programs, insurance navigation, and clinical trial enrollment are essential for access.

The infrastructure varies enormously by setting. Major US cancer centers have most of this infrastructure in place. Community oncology practices in the US have variable access. Public hospitals in many countries lack much of this infrastructure. Low- and middle-income countries face particularly large gaps.

---

## Where precision oncology has succeeded and failed

A balanced assessment of the current state:

*Areas of success*. Several cancer types have been transformed by precision oncology:
- *Chronic myeloid leukemia*. BCR-ABL targeting with imatinib and successors. Treatment outcomes are now better than would have been imaginable in 1990.
- *EGFR-mutant lung adenocarcinoma*. Multiple generations of EGFR inhibitors. Median survival approaching three years from a disease that was once measured in months.
- *HER2-positive breast cancer*. Multiple HER2-targeted agents. Outcomes have moved from worst breast cancer prognosis to among the best.
- *Melanoma*. BRAF/MEK inhibitors and immunotherapy have transformed outcomes.
- *ALK-rearranged lung cancer*. Sequential ALK inhibitors. Substantial extension of life.

*Areas of partial success*. Many cancers have some patients benefiting from precision approaches:
- *Colorectal cancer*. BRAF V600E, MSI-H, HER2-amplified subgroups benefit from specific therapies. Most patients (without these biomarkers) still receive standard chemotherapy.
- *Bladder cancer*. FGFR alterations and PD-L1 status guide some decisions; most patients on more conventional approaches.
- *Cholangiocarcinoma*. IDH, FGFR, BRAF alterations identify subgroups for targeted therapy.

*Areas of limited success*. Some cancers have benefited little from precision oncology:
- *Pancreatic cancer*. Despite extensive characterization, most patients have no actionable alterations. KRAS G12C inhibitors help a small subset. The vast majority continue to receive chemotherapy with modest outcomes.
- *Glioblastoma*. Multiple targeted therapy approaches have failed. The cancer's biology continues to defeat precision approaches.
- *Many sarcomas*. Specific subtypes have benefited (gastrointestinal stromal tumors with imatinib; dermatofibrosarcoma protuberans with imatinib), but most sarcomas have no good targeted options.

The pattern is informative. Cancers driven by single dominant oncogenes (CML by BCR-ABL, melanoma by BRAF V600E, GIST by KIT mutations) have responded dramatically to targeted therapies. Cancers with many cooperating alterations, complex genetic landscapes, or fundamental microenvironmental drivers (pancreatic cancer, glioblastoma) have been more resistant.

The next frontier is extending precision approaches to the harder cancers. This may require:
- *Drug combinations* that hit multiple targets simultaneously.
- *Microenvironmental targeting* in addition to cancer cell targeting.
- *Immunotherapy integration* to address cancers with poor neoantigen profiles.
- *Resistance prediction and management* to extend response durations.
- *Better drug development* for "undruggable" targets (KRAS, MYC, p53).

---

## The future of precision oncology

Several trends are shaping the future:

*Expanding biomarker space*. Beyond classical mutations, biomarkers increasingly include gene expression patterns, epigenetic features, immune phenotypes, microenvironmental characteristics, and integrated multi-omic profiles. AI-based integration of these complex datasets is improving prediction.

*Liquid biopsy at scale*. As ctDNA technology improves, real-time monitoring becomes feasible. Treatment decisions could be made based on weekly ctDNA changes rather than every-3-month imaging.

*Multi-omic profiling*. Combining genomics, transcriptomics, proteomics, epigenomics, and metabolomics for deeper tumor characterization. The integration is improving but most clinical practice still uses primarily genomics.

*Tumor microenvironment profiling*. Beyond cancer cells, characterizing the immune infiltrate, stromal composition, and metabolic environment. Spatial transcriptomics and multiplex immunofluorescence are increasingly used.

*Patient-derived organoids and xenografts*. Functional testing of drugs on patient-specific tumor models. The technology is improving and may eventually inform treatment decisions in real time.

*AI in treatment recommendation*. Machine learning systems trained on outcomes data to suggest treatment plans. The technology is emerging; clinical validation is still developing.

*Theranostics*. Combining molecular imaging with targeted radioligand therapy. PSMA-targeted approaches for prostate cancer leading the way.

*Cancer interception*. Detecting and intervening in the very earliest stages of cancer development, perhaps even before clinical disease. The pre-cancer concept is being extended through liquid biopsy and other approaches.

*Equity and access*. The infrastructure to support precision oncology is unevenly distributed. Expanding access to molecular profiling and targeted therapies — particularly in low- and middle-income countries — is one of the major challenges of the next decade.

---

## What this chapter gives you

Precision oncology matches specific therapies to specific molecular features of tumors. The framework has transformed many cancer types and continues to expand. The biomarker-defined treatments span genetic mutations (EGFR, BRAF, KRAS G12C, BRCA1/2, others), gene fusions (ALK, ROS1, RET, NTRK, others), copy number alterations (HER2 amplification, MET amplification), expression patterns (ER, PR, HER2, PD-L1), and functional features (MSI-H, TMB-H, HRD).

Tumor-agnostic approvals — drugs approved across cancer types based on molecular features — represent the most evolved form of precision oncology. Larotrectinib, pembrolizumab for MSI-H, BRAF + MEK for BRAF V600E across cancers, and others demonstrate that the biology can matter more than the tissue.

Clinical trial frameworks have evolved to support precision oncology — basket trials, umbrella trials, master protocols, adaptive designs, platform trials. These designs efficiently identify and validate biomarker-defined therapies.

Implementation requires substantial infrastructure: molecular profiling capacity, bioinformatic interpretation, molecular tumor boards, decision support tools, clinical trial matching, patient navigation, and access mechanisms. The infrastructure is uneven across institutions and geographies, creating equity challenges.

Precision oncology has succeeded dramatically in cancers driven by dominant oncogenes (CML, EGFR-mutant lung cancer, HER2-positive breast cancer, melanoma) and has had more limited impact in cancers with complex multi-factorial driving biology (pancreatic cancer, glioblastoma).

Future directions include expanding biomarker space, liquid biopsy at scale, multi-omic profiling, microenvironmental characterization, patient-derived models, AI-based decision support, theranostics, cancer interception, and addressing global access inequities.

The integration of precision oncology with the rest of cancer biology covered in this book — genetics (4-6), epigenetics (7), immunology (16), microenvironment (14) — is increasingly the framework for treating individual patients. Chapter 20 turns to surgical oncology, the first and still essential modality of cancer treatment.

---

## LLM exercises

1. Ask your LLM to construct the precision oncology workup and treatment recommendation for a hypothetical patient with metastatic non-small-cell lung adenocarcinoma. Cover the testing required, the major targetable alterations, the expected response rates, and the sequential treatment options as resistance develops.

2. Have your LLM compare basket trials, umbrella trials, and platform trials. For each: the trial design, the conceptual rationale, an example trial in oncology, and the limitations. Identify which trial framework is most appropriate for testing a new drug targeting a rare molecular alteration (less than 1% prevalence across all cancers).

3. Use your LLM to walk through the development of imatinib for chronic myeloid leukemia from BCR-ABL identification (1960 Philadelphia chromosome) through to current standard of care. What was the timeline, what were the key milestones, and what does this story illustrate about how precision oncology develops?

4. Ask your LLM to explain why precision oncology has had limited success in pancreatic cancer despite extensive molecular profiling. What is the underlying biology that has resisted targeted approaches, what are the current and emerging strategies, and what would a breakthrough in pancreatic cancer look like?

5. Have your LLM survey the major access disparities in precision oncology globally. Where are molecular profiling and targeted therapies most accessible, and where are they least? What are the cost barriers, policy levers, and institutional approaches that could improve global access? Identify the highest-impact interventions.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Brian Druker** developed imatinib (Gleevec) — the first targeted cancer therapy — by inhibiting the BCR-ABL kinase that drives chronic myeloid leukemia. The drug turned a fatal disease into a chronic, manageable condition and launched the era of precision oncology.

**Run this:**

```
Who is Brian Druker, and how does his work on imatinib connect to the precision oncology principles we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Brian J. Druker"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how imatinib was designed against the structure of BCR-ABL — and why it's so specific.
- Ask it about Druker's role in the patient-driven movement to get pharmaceutical companies to keep imatinib affordable.

What changes? What gets better? What gets worse?
