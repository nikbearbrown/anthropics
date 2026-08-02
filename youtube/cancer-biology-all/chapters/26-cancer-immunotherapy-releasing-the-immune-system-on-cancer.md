# Chapter 26 — Cancer Immunotherapy: Releasing the Immune System on Cancer


## TL;DR

- The drug that doesn't kill the cancer cell directly is the drug that has changed cancer therapy most in this century.
- The chapter moves through Immune checkpoint inhibitors, Combination immunotherapy, CAR-T cell therapy, Other cellular therapies, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

The drug that doesn't kill the cancer cell directly is the drug that has changed cancer therapy most in this century.

Hold the framing. Most cancer drugs do something to the cancer cell — chemotherapy damages its DNA, targeted therapy blocks its signaling, BH3 mimetics trigger its apoptosis, anti-angiogenic agents starve its vasculature. *Immune checkpoint inhibitors* do something else. They don't kill cancer cells. They release the brakes on T cells, which then kill cancer cells. The drug acts on the immune system; the immune system acts on the cancer. A whole different therapeutic logic.

The clinical results, when this logic works, are unlike anything else in cancer medicine. Some patients with metastatic melanoma, which 15 years ago was uniformly fatal within months, are now disease-free more than a decade after a course of ipilimumab and nivolumab. Some patients with non-small-cell lung cancer, previously incurable, achieve durable remissions on pembrolizumab. CAR-T cells produce complete responses in heavily pretreated leukemias and lymphomas where every other therapy has failed. These are not the slow attritional gains of chemotherapy. They are dramatic, durable responses that look like cures.

The therapies also fail in plenty of patients. Most cancers do not respond. Some tumors are inherently "cold" and never engage the immune system. Some that respond initially progress later. The toxicities — autoimmune-like reactions from over-activated immune cells — are real and sometimes life-threatening. Immunotherapy is not a universal solution. But its successes have established a new modality and reshaped the field.

This is the second chapter on tumor immunology. The first — 16A — covered the immune biology: surveillance, antigens, the immune response, evasion mechanisms. This one covers the therapeutic translation: checkpoint inhibitors (ipilimumab, nivolumab, pembrolizumab, others), cellular therapies (CAR-T, TIL therapy, TCR-T), cancer vaccines, oncolytic viruses, and the combinations that have become standard in many cancers.

Hold the question: *if cancers evade the immune system, can we engineer the immune system to win the rematch?*

---

## Immune checkpoint inhibitors

The clinical breakthrough that launched the immunotherapy era was the discovery that blocking *immune checkpoints* — the negative regulatory receptors on T cells — could unleash anti-tumor immunity.

The biology: T cell activation requires two signals. *Signal 1* is the antigen-MHC complex binding to the T cell receptor. *Signal 2* is co-stimulation, primarily through CD28 on the T cell binding CD80/CD86 on antigen-presenting cells. Without both signals, T cells either fail to activate or enter an anergic state.

*Inhibitory checkpoints* are receptors on T cells that, when engaged, reduce or terminate T cell activation. Their normal function is to prevent autoimmune attack on healthy tissues. They are essential to peripheral tolerance. But in cancer, tumors exploit these same checkpoints to suppress anti-tumor T cell responses.

*CTLA-4* (cytotoxic T-lymphocyte-associated protein 4) is expressed on activated T cells and on regulatory T cells. It competes with CD28 for binding to CD80/CD86 (with higher affinity than CD28), reducing the co-stimulation that T cells receive. The dominant effect is to limit T cell priming in lymph nodes.

*PD-1* (programmed death-1) is expressed on activated and exhausted T cells. Its ligands are *PD-L1* (expressed broadly, including on tumor cells and tumor-associated macrophages) and *PD-L2* (more restricted expression). PD-1 binding inhibits T cell effector function in peripheral tissues — including in tumors. The dominant effect of PD-1/PD-L1 signaling is to suppress T cell killing of cancer cells.

Other inhibitory checkpoints include *LAG-3*, *TIM-3*, *TIGIT*, *BTLA*, *VISTA*, and others. Each has its own ligands and contexts. The system has many layers of negative regulation, and tumors often engage multiple checkpoints simultaneously.

The therapeutic strategy is *checkpoint blockade* — monoclonal antibodies that bind these inhibitory receptors or their ligands, preventing the inhibitory signal and allowing T cells to remain activated and to kill cancer cells.

*Ipilimumab* (Yervoy, anti-CTLA-4) was approved by the FDA in 2011 for metastatic melanoma. It was the first checkpoint inhibitor and the first drug to extend overall survival in metastatic melanoma. Response rates were modest (about 15-20 percent), but a substantial subset of responders achieved durable remissions — the "tail" of the survival curve that suggested some patients were being cured.

*Nivolumab* (Opdivo, anti-PD-1) was approved in 2014 for melanoma and has been progressively expanded. *Pembrolizumab* (Keytruda, anti-PD-1) was approved the same year. Both have similar mechanisms and overlapping but somewhat different indications.

*Atezolizumab* (Tecentriq, anti-PD-L1), *durvalumab* (Imfinzi, anti-PD-L1), *avelumab* (Bavencio, anti-PD-L1), *cemiplimab* (Libtayo, anti-PD-1), *dostarlimab* (Jemperli, anti-PD-1), and others have followed.

*Relatlimab* (anti-LAG-3) was approved in 2022 in combination with nivolumab for melanoma. Other LAG-3 inhibitors, TIM-3 inhibitors, and TIGIT inhibitors are in clinical development.

The FDA-approved indications across these drugs span more than 20 cancer types: melanoma, non-small-cell lung cancer, small-cell lung cancer, renal cell carcinoma, head and neck squamous cell carcinoma, urothelial carcinoma, hepatocellular carcinoma, classical Hodgkin lymphoma, primary mediastinal B-cell lymphoma, Merkel cell carcinoma, cutaneous squamous cell carcinoma, microsatellite instability-high tumors regardless of tissue type (tumor-agnostic approval), gastric/gastroesophageal junction adenocarcinoma, triple-negative breast cancer, esophageal cancer, cervical cancer, endometrial carcinoma, biliary tract cancer, mesothelioma, and others. The expansion has been rapid.

Response rates vary by cancer type and biomarker status:
- Melanoma: 30-45 percent with anti-PD-1 monotherapy, higher with combinations.
- Non-small-cell lung cancer (PD-L1 high): 40-45 percent with pembrolizumab.
- Microsatellite-instability-high tumors: 30-50 percent with anti-PD-1.
- Triple-negative breast cancer: 10-20 percent with anti-PD-L1 alone, higher with chemotherapy combinations.
- Renal cell carcinoma: 25-30 percent with monotherapy, higher with combinations.
- Hodgkin lymphoma: 65-75 percent with anti-PD-1 — one of the most responsive cancers.
- Some "cold" tumors (pancreatic, prostate, microsatellite-stable colorectal): <5 percent.

The pattern of response is informative. Tumors with high mutation burden, high PD-L1 expression, and pre-existing T cell infiltration ("hot" tumors) tend to respond. Tumors with low mutation burden, low PD-L1, and minimal T cell infiltration ("cold" tumors) tend not to respond.

---

## Combination immunotherapy

Single-agent checkpoint inhibitors are effective in some cancers but limited in others. Combinations have been pursued aggressively.

*Anti-CTLA-4 + anti-PD-1*. The first major combination. Ipilimumab + nivolumab in metastatic melanoma produces response rates around 60 percent — substantially higher than either drug alone. Five-year overall survival exceeds 50 percent, dramatically better than historical norms. The combination has been approved for several other cancers: renal cell carcinoma, microsatellite-instability-high colorectal cancer, hepatocellular carcinoma, malignant pleural mesothelioma, esophageal squamous cell carcinoma, others. The toxicity is higher than either drug alone — about 55 percent of patients experience grade 3-4 immune-related adverse events, compared to about 20 percent with nivolumab monotherapy.

*Anti-PD-1 + chemotherapy*. Chemotherapy can release tumor antigens through cancer cell death and modulate the immune microenvironment. Pembrolizumab + chemotherapy combinations are standard first-line therapy for non-small-cell lung cancer, triple-negative breast cancer, head and neck cancer, and other diseases.

*Anti-PD-1/L1 + anti-angiogenic agents*. As discussed in Chapter 12B, anti-angiogenic therapy normalizes tumor vasculature, reduces hypoxia, and reduces VEGF-mediated immunosuppression. Atezolizumab + bevacizumab in hepatocellular carcinoma. Pembrolizumab + axitinib in renal cell carcinoma. Lenvatinib + pembrolizumab in endometrial cancer. Multiple approvals.

*Anti-PD-1 + targeted therapy*. Combinations with BRAF inhibitors in melanoma, with EGFR inhibitors in lung cancer, with PARP inhibitors in BRCA-mutant cancers. Mixed results — some combinations enhance activity, others increase toxicity without benefit.

*Anti-PD-1 + LAG-3 inhibitor*. Nivolumab + relatlimab in melanoma improved progression-free survival over nivolumab alone (RELATIVITY-047). The first non-CTLA-4 checkpoint combination to gain approval.

*Anti-PD-1 + radiation*. Radiation can release tumor antigens (the abscopal effect — radiation to one lesion sometimes causes regression of distant lesions, presumably through immune mechanisms). Combinations of immunotherapy with stereotactic radiation are being tested.

The space of possible combinations is huge. Selection of which combinations to advance is informed by biology — what compensatory mechanisms might emerge from single-agent therapy, what synergies are mechanistically plausible. The clinical trial pipeline is extensive.

---

## CAR-T cell therapy

Beyond checkpoint inhibitors, the other transformative immunotherapy approach is *adoptive cellular therapy* — taking immune cells out of the patient (or a donor), modifying them, expanding them, and infusing them back.

The most established form is *chimeric antigen receptor T cell (CAR-T) therapy*. CAR-T cells are autologous T cells (taken from the patient) genetically engineered to express an artificial receptor — the *chimeric antigen receptor* — that recognizes a specific tumor antigen. The CAR consists of an extracellular antibody-derived antigen-binding domain, a transmembrane region, and intracellular T cell signaling domains. When the CAR binds its target antigen on a cancer cell, it activates the T cell's killing machinery — directly, without needing MHC presentation.

CAR-T cells therefore bypass several immune evasion mechanisms. They don't require MHC class I (so MHC-downregulated tumors are still vulnerable). They don't need professional antigen presentation. They don't need normal T cell priming.

The first FDA-approved CAR-T was *tisagenlecleucel* (Kymriah, anti-CD19) in 2017 for B-cell acute lymphoblastic leukemia (ALL). CD19 is expressed on essentially all B cells, including the leukemia cells. Tisagenlecleucel CAR-T produced complete response rates around 80 percent in heavily pretreated pediatric ALL — patients who had failed multiple prior therapies. Several long-term remissions have been reported.

Subsequent approvals:
- *Axicabtagene ciloleucel* (Yescarta, anti-CD19) for diffuse large B-cell lymphoma.
- *Brexucabtagene autoleucel* (Tecartus, anti-CD19) for mantle cell lymphoma.
- *Lisocabtagene maraleucel* (Breyanzi, anti-CD19) for diffuse large B-cell lymphoma.
- *Idecabtagene vicleucel* (Abecma, anti-BCMA) for multiple myeloma.
- *Ciltacabtagene autoleucel* (Carvykti, anti-BCMA) for multiple myeloma.

The technology has been most successful in B-cell malignancies (using CD19 as a target) and multiple myeloma (using BCMA as a target). The success in these hematological cancers reflects features that are favorable for CAR-T: the target antigens are expressed on all or nearly all malignant cells; the target antigens are also expressed on normal cells of the same lineage, but those normal cells (B cells, plasma cells) can be lost without immediate fatal consequences; the cells are accessible in blood and lymphoid organs.

CAR-T in solid tumors has been more challenging. The reasons include:
- *Tumor antigen heterogeneity*. Solid tumors have more heterogeneous antigen expression than hematological cancers. CAR-T targeting one antigen may miss antigen-negative subclones.
- *Tumor antigen targeting normal tissues*. Many candidate antigens are also expressed on critical normal tissues, and on-target/off-tumor toxicity is severe.
- *Solid tumor microenvironment*. Dense matrix impedes CAR-T infiltration. Immunosuppressive factors in the TME impair CAR-T function. Hypoxia and nutrient depletion reduce CAR-T persistence.
- *Lack of cancer-specific surface antigens*. Most solid tumor antigens are also expressed on some normal cells.

CAR-T research for solid tumors is active but has not yet produced approved products. Approaches include local delivery (intratumoral injection), CAR engineering for the TME (CARs designed to survive the suppressive environment), bispecific CARs targeting multiple antigens, and TRUCKs (CAR-T cells engineered to release immunostimulatory factors).

CAR-T toxicities are distinctive. *Cytokine release syndrome (CRS)* — massive cytokine production from activated CAR-T cells — produces fever, hypotension, hypoxia, and in severe cases multi-organ dysfunction. Most patients experience some degree of CRS. Tocilizumab (anti-IL-6 receptor) is the standard treatment. *Immune effector cell-associated neurotoxicity syndrome (ICANS)* — neurological toxicity ranging from confusion to seizures to cerebral edema — occurs in a substantial fraction of patients and is the more difficult-to-treat toxicity. These toxicities are predictable, manageable in specialized centers, and acceptable given the clinical benefits in approved indications.

---

## Other cellular therapies

Beyond CAR-T, several other forms of adoptive cellular therapy are in clinical use or development.

*Tumor-infiltrating lymphocyte (TIL) therapy*. T cells are isolated from a patient's tumor, expanded in vitro, and reinfused. The cells include T cells that have already recognized tumor antigens. Lifileucel was the first FDA-approved TIL therapy, approved in 2024 for melanoma. The technology is technically complex (requires surgical tumor harvest, prolonged ex vivo expansion) but has shown durable responses in melanoma and other cancers.

*T cell receptor (TCR) therapy*. T cells are engineered to express a specific T cell receptor that recognizes a known tumor antigen presented on MHC. Unlike CARs, TCRs use the normal MHC-restricted recognition. TCR-T can target intracellular antigens (which can be processed and presented on MHC). Tebentafusp, a bispecific TCR-fusion protein, was approved in 2022 for uveal melanoma. Other TCR-T candidates targeting NY-ESO-1, MAGE family antigens, and others are in development.

*Engineered NK cells*. NK cells modified with CARs (CAR-NK) or expanded with cytokines and infused. Potentially advantages over CAR-T include reduced CRS risk and the possibility of "off-the-shelf" allogeneic products that don't require patient-specific manufacturing.

*Macrophage-based therapies*. CAR-macrophages, where macrophages are engineered to phagocytose specific cancer cells. In early development.

*Dendritic cell vaccines*. DCs loaded with tumor antigens and infused. Sipuleucel-T (Provenge) for prostate cancer was the first approved cancer vaccine (2010); it works through this mechanism.

The cellular therapy space is rapidly evolving. The combination of genetic engineering, in vitro expansion, and in vivo immune effector function is producing therapies that can be highly targeted and highly effective. Manufacturing complexity and cost are major practical challenges.

---

## Cancer vaccines

Cancer vaccines aim to prime or boost an adaptive immune response against tumor antigens. The history has been frustrating — many candidates produced immune responses without clinical responses — but more recent neoantigen-targeted approaches are showing promise.

*Preventive vaccines* against cancer-causing viruses are the great success stories. HPV vaccines (Gardasil 9) prevent HPV infection and the cancers it causes (cervical, anal, oropharyngeal). Hepatitis B vaccines prevent HBV infection and hepatocellular carcinoma. These are well-established and highly effective.

*Therapeutic cancer vaccines* — designed to treat established cancer — have been harder. The few approved therapies:
- *Sipuleucel-T* (Provenge) for prostate cancer (2010). Autologous DCs activated against PAP (prostatic acid phosphatase). Modest overall survival benefit.
- *BCG* for non-muscle-invasive bladder cancer. Bacillus Calmette-Guérin instilled into the bladder; activates innate and adaptive immunity. Long-established standard.
- *Talimogene laherparepvec* (T-VEC) for advanced melanoma. An engineered oncolytic herpes simplex virus that lyses cancer cells and stimulates immunity. Modest activity as monotherapy.

The newer wave of cancer vaccines focuses on *personalized neoantigen vaccines*. The patient's tumor is sequenced, neoantigens are predicted computationally, and a personalized vaccine (peptides, RNA, or DNA encoding the neoantigens) is manufactured and administered. The vaccine primes T cell responses specifically against the patient's tumor neoantigens.

Early clinical data from BioNTech, Moderna, and academic groups show that personalized neoantigen vaccines can produce neoantigen-specific T cell responses in cancer patients. A randomized phase 2 trial of mRNA-based neoantigen vaccine (mRNA-4157) plus pembrolizumab in melanoma showed improved recurrence-free survival compared to pembrolizumab alone. The technology is maturing.

The combination of neoantigen vaccines with checkpoint inhibitors is particularly appealing — the vaccine primes new T cell responses, and the checkpoint inhibitor prevents those responses from being shut down by the tumor. Several phase 3 trials are testing such combinations.

---

## Oncolytic viruses

A different immunotherapy approach uses viruses that selectively replicate in and kill cancer cells, releasing tumor antigens and stimulating immune responses in the process.

*T-VEC* (talimogene laherparepvec, 2015) is an attenuated herpes simplex virus engineered to lack a viral gene required for replication in normal cells (the virus needs cellular factors that are abundant in cancer cells) and to express GM-CSF (a cytokine that recruits and matures dendritic cells). Injected intratumorally in metastatic melanoma, T-VEC produces local lesion regression and some systemic responses. The drug is FDA-approved for melanoma.

Other oncolytic viruses are in development: oncolytic adenoviruses, vaccinia viruses, vesicular stomatitis virus, reovirus, others. The technology has been most successful in accessible tumors (skin metastases, peritoneal disease) where direct injection is feasible. Systemic delivery is harder because the virus is neutralized by pre-existing antibodies or cleared by the liver.

Oncolytic viruses are increasingly being combined with checkpoint inhibitors. The virus kills cancer cells immunogenically; the released antigens prime T cell responses; the checkpoint inhibitor sustains those responses. Several combinations are in clinical trials.

---

## Immune-related adverse events

The flip side of immunotherapy is *immune-related adverse events* — autoimmune-like reactions caused by the activated immune system attacking normal tissues.

The toxicities can affect essentially any organ system. Skin (rash, vitiligo). GI (colitis). Liver (hepatitis). Lung (pneumonitis). Endocrine (thyroiditis, hypophysitis, adrenal insufficiency, type 1 diabetes). Musculoskeletal (arthralgia, myositis). Cardiac (myocarditis — rare but often fatal). Renal (nephritis). Neurological (neuropathy, encephalitis, myasthenia-like syndromes). Hematological (cytopenias).

Most events are mild and managed with corticosteroids. Severe events require holding immunotherapy, high-dose corticosteroids, and sometimes additional immunosuppression. Some events (endocrine deficiencies in particular) may persist after immunotherapy is stopped and require lifelong hormone replacement.

Management of immune-related adverse events is now a substantial part of oncology practice. Specialized clinics have emerged. The expertise required is real — distinguishing immunotherapy toxicity from disease progression or unrelated medical conditions takes experience.

The toxicities also reveal something important about the immunotherapies' mechanism. They work by overriding peripheral tolerance — the same mechanism that normally prevents autoimmune disease. The autoimmune-like toxicities are the price of overriding tolerance. Patients who develop some immune-related adverse events tend, on balance, to have better tumor responses — the autoimmunity is mechanistically linked to anti-tumor activity, though the correlation is not perfect.

---

## Where immunotherapy stands

A reasonable summary of the field as of 2026:

*Checkpoint inhibitors* are standard of care for many cancers. They produce dramatic durable responses in a subset of patients across many cancer types. They are limited by inherent resistance in many tumors (cold tumors), acquired resistance after initial response, and immune-related toxicities. Combinations with chemotherapy, anti-angiogenic agents, targeted therapies, and other immunotherapies are increasingly the standard approach.

*CAR-T cells* have transformed treatment of B-cell malignancies and multiple myeloma. They are being extended to solid tumors with limited success so far. Manufacturing complexity, cost, and CRS/ICANS toxicities are real limitations. Allogeneic CAR-T products that can be manufactured at scale are in development.

*Other cellular therapies* (TIL, TCR-T, CAR-NK) are showing activity in specific contexts. Manufacturing and personalization remain limitations.

*Personalized neoantigen vaccines* are showing promise, particularly in combination with checkpoint inhibitors. The technology is becoming faster and cheaper. Phase 3 trials will determine clinical utility.

*Oncolytic viruses* have one FDA-approved product (T-VEC) and are most useful when delivered locally to accessible tumors. Combinations with checkpoint inhibitors are extending applications.

*Future directions* include: better biomarkers for patient selection; conversion of cold tumors to hot tumors; combinations targeting multiple checkpoints and resistance mechanisms; reduced toxicity through tumor-selective immunotherapy; off-the-shelf cellular products; and integration with other modalities.

The field has transformed cancer therapy. It has not solved cancer. The progress has been substantial and continuing, with new mechanisms, new combinations, and new manufacturing approaches entering the clinic each year.

---

## What this chapter gives you

Cancer immunotherapy has reshaped oncology through several mechanisms. *Checkpoint inhibitors* — antibodies targeting CTLA-4, PD-1, PD-L1, LAG-3, and other inhibitory receptors on T cells — release the brakes on anti-tumor immunity. They have FDA approvals across more than 20 cancer types and produce durable responses in subsets of patients, though most cancers remain refractory.

*CAR-T cells* are autologous T cells engineered to recognize specific tumor antigens through a chimeric receptor. They have transformed treatment of B-cell malignancies and multiple myeloma. Solid tumors remain a challenge.

*Other cellular therapies* — TIL, TCR-T, CAR-NK, dendritic cell vaccines — extend the cellular therapy paradigm to additional contexts.

*Cancer vaccines*, especially personalized neoantigen vaccines, are showing renewed promise particularly in combination with checkpoint inhibitors. Phase 3 trials are underway.

*Oncolytic viruses* (T-VEC and others in development) selectively replicate in cancer cells, killing them and stimulating immune responses.

The therapeutic landscape is increasingly dominated by combinations — checkpoint inhibitors plus chemotherapy, plus anti-angiogenic agents, plus radiation, plus targeted therapies, plus other immunotherapies. The biology of why these combinations work or fail connects to the immune evasion mechanisms covered in 16A and to the cancer biology covered throughout this book.

*Immune-related adverse events* are the inherent cost of overriding peripheral tolerance. Management of these toxicities is now a substantial part of oncology practice and requires specialized expertise.

The integration of immunotherapy with everything else covered in this book — genetics, metabolism, angiogenesis, metastasis, microenvironment, heterogeneity — is increasingly the framework for treating cancer. Treatment selection for an individual patient is now informed by genetic profile, immune phenotype, mutational burden, microenvironmental characteristics, and disease state. Precision oncology has become precision immuno-oncology in many contexts.

Chapter 17 turns to diagnosis and staging — the workup of cancer, the imaging and laboratory tests, the biopsy and histology, the molecular profiling that now informs treatment selection. The biology of cancer covered through Chapter 16 is the foundation; the diagnostic infrastructure of Chapter 17 is how we apply it to individual patients.

---

## LLM exercises

1. Ask your LLM to walk through the discovery and translation of CTLA-4 by James Allison and PD-1 by Tasuku Honjo. What were the key experiments, how did the field move from basic discovery to clinical drug, and what was the predicted versus actual benefit? Identify what the trajectory tells us about basic-to-clinical translation in oncology.

2. Have your LLM construct a table comparing the major FDA-approved checkpoint inhibitors — ipilimumab, nivolumab, pembrolizumab, atezolizumab, durvalumab, relatlimab. For each: target, approved indications, response rates in major indications, common toxicities, and combination strategies.

3. Use your LLM to explain why CAR-T cells have been more successful in hematological cancers than solid tumors. What specific features of B-cell malignancies make CD19 a good CAR target, and what specific challenges does solid tumor biology pose for CAR-T? Identify the most promising solid tumor CAR-T candidates and their target antigens.

4. Ask your LLM to walk through the major immune-related adverse events of checkpoint inhibitor therapy. For each major organ system, identify the typical clinical presentation, the management approach, and the relationship to tumor response. Construct a clinical decision framework for managing a patient with new-onset diarrhea on checkpoint inhibitor therapy.

5. Have your LLM survey the current state of personalized neoantigen cancer vaccines. What is the technical pipeline (sequencing, prediction, manufacturing), what are the recent clinical data (including the mRNA-4157 melanoma trial), and what are the major challenges remaining? Identify the cancer types where personalized neoantigen vaccines are most likely to produce clinical benefit in the next 5 years.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **James P. Allison** showed in 1996 that blocking CTLA-4 unleashes T cells against tumors — the founding result of checkpoint immunotherapy. He won the 2018 Nobel Prize with Tasuku Honjo for the discovery.

**Run this:**

```
Who is James P. Allison, and how does his CTLA-4 work connect to releasing the immune system against cancer, as we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"James P. Allison"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through Allison's original 1996 mouse experiment with the anti-CTLA-4 antibody.
- Ask it about the long path from Allison's mouse data to ipilimumab approval — and the institutional skepticism along the way.

What changes? What gets better? What gets worse?
