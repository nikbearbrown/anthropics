# Chapter 44 — Cellular Therapies Vaccines and Cytokines


## TL;DR

- Engineering immunity is harder than releasing it, but the engineered version has reached cancers that releasing alone cannot.
- The chapter moves through CAR-T cell therapy in clinical practice, CAR-T toxicities and their management, CAR-T for solid tumors, Tumor-infiltrating lymphocyte therapy, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

Engineering immunity is harder than releasing it, but the engineered version has reached cancers that releasing alone cannot.

Hold the framing. Checkpoint inhibitors work by releasing the brakes on existing immune responses. The patient must have anti-tumor T cells with some recognition of the cancer; the drug just removes the suppression. For cancers where no significant anti-tumor immune response exists naturally — many "cold" tumors, some advanced disease, hematologic malignancies with specific surface markers — checkpoint inhibitors alone don't work.

The alternative is to *engineer* an immune response. Take T cells out of the patient, give them artificial recognition for a specific tumor antigen, expand them in vitro, and infuse them back. The engineered T cells provide a tumor-specific killing force that the patient's natural immune system couldn't produce. This is *adoptive cellular therapy*, and it has produced some of the most dramatic responses in cancer treatment for B-cell malignancies and multiple myeloma.

Beyond cellular therapy, *cancer vaccines* aim to prime new immune responses against tumor antigens. *Cytokine therapy* provides direct immune-stimulating signals. *Oncolytic viruses* engage immunity through cancer cell lysis. Each approach has its own clinical applications and limitations.

This chapter — the second of two on cancer immunotherapy in practice — covers these complementary approaches: CAR-T cells, TIL therapy, TCR-T cells, cancer vaccines (including personalized neoantigen vaccines), cytokines, and other immune-based therapies. The chapter builds on the biology covered in Chapter 16 and complements the checkpoint inhibitor focus of 25A.

Hold the question: *what kinds of cancer require engineered rather than released immunity, and what are we doing to deliver the engineering?*

---

## CAR-T cell therapy in clinical practice

CAR-T cell therapy was introduced in Chapter 16B. The clinical implementation deserves additional detail because the practical aspects are substantial.

The basic process:
1. *Apheresis*. The patient's blood is collected and T cells are isolated through apheresis (typically over several hours).
2. *Genetic engineering*. The T cells are transduced with a viral vector (lentivirus or retrovirus) encoding the chimeric antigen receptor.
3. *Expansion*. The engineered T cells are expanded in vitro over 1-2 weeks to generate sufficient cells for treatment.
4. *Lymphodepletion*. The patient receives lymphodepleting chemotherapy (typically fludarabine + cyclophosphamide) for several days before CAR-T infusion. This depletes the patient's existing lymphocytes, creating "space" for the infused CAR-T cells and removing immunosuppressive regulatory T cells.
5. *CAR-T infusion*. The engineered T cells are infused back into the patient.
6. *Expansion in vivo*. The infused CAR-T cells proliferate in response to encountering their target antigen and recruit additional immune effects.
7. *Monitoring*. Close observation, typically in the hospital, for the first 1-2 weeks for cytokine release syndrome and neurotoxicity.

The total process from apheresis to infusion takes 2-4 weeks. During this time, the patient may receive *bridging therapy* (chemotherapy, radiation, or other treatment) to keep the disease controlled.

The FDA-approved CAR-T products as of 2026:

*Tisagenlecleucel* (Kymriah). Anti-CD19 CAR-T. Approved 2017 for B-cell ALL in pediatric and young adult patients, and for relapsed/refractory diffuse large B-cell lymphoma. The first CAR-T approval.

*Axicabtagene ciloleucel* (Yescarta). Anti-CD19. Approved for DLBCL, primary mediastinal B-cell lymphoma, and follicular lymphoma.

*Brexucabtagene autoleucel* (Tecartus). Anti-CD19. Approved for mantle cell lymphoma and adult B-cell ALL.

*Lisocabtagene maraleucel* (Breyanzi). Anti-CD19. Approved for DLBCL and other B-cell lymphomas.

*Idecabtagene vicleucel* (Abecma). Anti-BCMA. Approved for multiple myeloma after multiple prior therapies.

*Ciltacabtagene autoleucel* (Carvykti). Anti-BCMA. Approved for multiple myeloma. Higher response rates than ide-cel in pivotal trials.

The clinical results have been remarkable in approved indications:
- *Pediatric/young adult B-ALL*. Complete response rates of 70-90% in heavily pretreated patients with relapsed/refractory disease.
- *DLBCL*. Complete response rates of 40-60% in patients who have failed multiple prior therapies.
- *Multiple myeloma*. Response rates of 60-80% in patients with multiple prior lines of therapy.

The responses are often durable, with substantial percentages of patients in remission years after CAR-T treatment. Some patients appear to be effectively cured.

---

## CAR-T toxicities and their management

The toxicities of CAR-T therapy are distinctive and require specialized expertise.

*Cytokine release syndrome (CRS)*. Massive cytokine production from activated CAR-T cells produces systemic inflammatory response. Fever is typically the first sign. Severity ranges from mild (fever, mild hypotension responsive to fluids) to life-threatening (vasopressor-requiring shock, respiratory failure, organ dysfunction).

The grading system (ASTCT criteria):
- *Grade 1*: Fever ≥38°C.
- *Grade 2*: Fever + hypotension responsive to fluids OR hypoxia requiring low-flow oxygen.
- *Grade 3*: Fever + hypotension requiring vasopressors OR hypoxia requiring high-flow oxygen.
- *Grade 4*: Fever + multiple vasopressors OR severe hypoxia requiring ventilation.

Management:
- *Supportive care*. Fluids, oxygen, vasopressors as needed.
- *Tocilizumab* (anti-IL-6 receptor). The mainstay of CRS treatment. Targets the cytokine signaling that drives CRS without affecting CAR-T anti-tumor activity.
- *Corticosteroids*. For severe or tocilizumab-refractory CRS. Used cautiously because high-dose steroids could potentially suppress CAR-T efficacy.
- *Anakinra* (IL-1 receptor antagonist). Increasingly used for severe CRS, particularly with neurotoxicity.
- *ICU care* for severe cases.

CRS typically occurs 1-10 days after CAR-T infusion. About 80% of patients have some CRS; about 20% have severe (grade 3-4) CRS.

*Immune effector cell-associated neurotoxicity syndrome (ICANS)*. Neurologic toxicity from CAR-T treatment, mechanistically related to but distinct from CRS. Manifestations include confusion, aphasia, tremor, seizures, decreased consciousness, and rarely cerebral edema (which can be fatal).

The grading system (ICE score):
- Tests immune effector cell encephalopathy through cognitive assessment, language, attention, motor function, and consciousness level.
- Grade 1: mild changes.
- Grade 4: severe (coma, seizures, cerebral edema).

Management:
- *Supportive care*. Avoid medications that worsen mental status; airway protection if needed.
- *Corticosteroids*. The mainstay of ICANS treatment. Often used at higher doses than for CRS.
- *Tocilizumab* is not particularly effective for ICANS alone (in contrast to CRS).
- *Anakinra* and other agents for refractory cases.

ICANS typically occurs 3-14 days after CAR-T infusion, often after CRS has begun.

*Cytopenias*. Prolonged cytopenias after lymphodepletion + CAR-T are common. Some patients have persistent neutropenia, thrombocytopenia, or anemia requiring transfusion and growth factor support for weeks to months.

*B-cell aplasia and hypogammaglobulinemia*. Anti-CD19 CAR-T eliminates not just CD19+ leukemia/lymphoma cells but also normal B cells. The resulting hypogammaglobulinemia increases infection risk. Many patients require IVIG replacement.

*Infections*. Increased infection risk during cytopenias and from immunosuppression. Antimicrobial prophylaxis is standard.

*Late toxicities*. Long-term consequences of CAR-T are still being characterized. Concerns include persistent cytopenias, secondary malignancies (recent reports of T-cell lymphomas in some CAR-T recipients), and long-term immune dysfunction.

The toxicities require specialized centers with experience. CAR-T treatment is concentrated at high-volume centers, with patient referral required. The infrastructure includes ICU support, specialized nursing, neurology consultation, and 24/7 access to tocilizumab and other treatments.

---

## CAR-T for solid tumors

CAR-T has been transformative for B-cell malignancies and multiple myeloma. Solid tumor applications have been more challenging, and as of 2026 no CAR-T product is FDA-approved for solid tumors.

The challenges:

*Tumor antigen heterogeneity*. Solid tumors have more heterogeneous expression of any single antigen. CAR-T targeting a single antigen may produce response in some cells while missing antigen-negative subclones.

*Tumor antigen and normal tissue overlap*. Most candidate antigens are also expressed on critical normal tissues. On-target/off-tumor toxicity has been severe in some trials (fatal cardiopulmonary toxicity in early HER2-CAR-T trials, for instance).

*Solid tumor microenvironment*. Dense matrix impedes CAR-T infiltration. Immunosuppressive factors in the TME impair CAR-T function. Hypoxia and nutrient depletion reduce CAR-T persistence.

*T cell exhaustion*. CAR-T cells in solid tumors often become exhausted (reduced effector function) more quickly than in hematological cancers, where they engage their target rapidly and clear most of the disease.

Approaches being explored:

*Local delivery*. Intratumoral or regional delivery (intraperitoneal for ovarian; intrathecal for CNS disease) to concentrate CAR-T at the tumor site.

*Multi-antigen CAR-T*. CARs targeting multiple antigens simultaneously to address heterogeneity.

*Logic-gated CARs*. Engineered to recognize tumor cells through combinations of markers (requiring presence of two antigens to activate), improving selectivity.

*TRUCKs (T cells redirected for universal cytokine killing)*. CAR-T cells engineered to release immunostimulatory factors (IL-12, IL-15) at the tumor site, recruiting additional immune effects.

*Armored CARs*. Engineered to resist immunosuppression (e.g., expressing dominant-negative TGF-β receptors).

*Specific targets in development*. GD2 (neuroblastoma, melanoma, sarcoma), claudin 18.2 (gastric and pancreatic cancer), mesothelin (mesothelioma, lung, ovarian, pancreatic), CD70 (renal cell carcinoma), GPC3 (hepatocellular carcinoma), EGFRvIII (glioblastoma), B7-H3, and others.

*Allogeneic CAR-T*. Using cells from healthy donors rather than the patient. Avoids the manufacturing time and individual variability of autologous CAR-T. Several allogeneic products in clinical trials. Challenges include graft-versus-host disease, host rejection of the allogeneic cells, and persistence.

Early clinical data for solid tumor CAR-T have shown some signals of activity in specific cancers (claudin 18.2 CAR-T in gastric/pancreatic cancer; GD2 CAR-T in neuroblastoma and DIPG; others), but consistent responses have been elusive.

---

## Tumor-infiltrating lymphocyte therapy

TIL therapy involves a different cellular approach. T cells are isolated directly from the patient's tumor, expanded in vitro, and reinfused. The cells include T cells that have already recognized tumor antigens (since they migrated to the tumor for that reason). The expansion process amplifies these tumor-specific cells.

The process:
1. *Surgical tumor harvest*. Surgical removal of a tumor (or portion of tumor) for cell isolation.
2. *T cell isolation and expansion*. Tumor is digested; T cells are isolated and expanded using IL-2 and other factors over weeks.
3. *Lymphodepletion*. Similar to CAR-T preparation.
4. *TIL infusion*. The expanded T cells are infused back.
5. *High-dose IL-2*. Standard post-infusion IL-2 supports TIL persistence and function. Causes significant toxicity (capillary leak syndrome, multi-organ effects).

*Lifileucel* (Amtagvi) was the first FDA-approved TIL therapy, approved in February 2024 for unresectable or metastatic melanoma after progression on immune checkpoint inhibitor and BRAF/MEK inhibitor (if BRAF-mutated). Response rates in registration trials were about 30% in heavily pretreated metastatic melanoma patients, with some durable responses.

The technical and logistical complexity of TIL is substantial. Surgery, weeks of cell expansion in specialized facilities, intensive inpatient management with high-dose IL-2 — the process is more elaborate than CAR-T. Few centers have the capability.

TIL is being tested in many other cancers — cervical cancer (some early data), head and neck cancer, lung cancer, others. The activity varies. The selection of patients (which tumors yield expansible, functional T cells; which patients can tolerate the process) is critical.

---

## TCR-T cell therapy

TCR-T therapy uses T cells engineered to express a specific T cell receptor that recognizes a defined tumor antigen presented on MHC. Unlike CARs (which use antibody-derived recognition independent of MHC), TCRs use the normal MHC-restricted recognition system.

The advantages over CAR-T:
- Can target intracellular antigens (which can be processed and presented on MHC).
- May better recognize tumor cells in their normal cellular context.

The disadvantages:
- HLA restriction. Each TCR-T product is specific to a particular HLA allele, limiting patient eligibility.
- Can be evaded by MHC downregulation (which cancer cells do as immune escape).

*Tebentafusp* (Kimmtrak) was approved in 2022 for HLA-A*02:01-positive metastatic uveal melanoma. It's technically a soluble bispecific TCR-fusion protein rather than cellular therapy, but uses the TCR-recognition concept. Activity in uveal melanoma is meaningful and the drug provides one of few effective options for this rare cancer.

Cellular TCR-T products are in development for various cancers:
- NY-ESO-1-targeted TCR-T for sarcomas (synovial sarcoma) and other NY-ESO-1-expressing cancers.
- MAGE family-targeted TCR-T.
- HPV-targeted TCR-T for HPV-driven cancers.

The technology is more complex than CAR-T because TCR-T requires both the TCR engineering and HLA-matching. Implementation is more limited.

---

## Cancer vaccines

Cancer vaccines aim to prime or boost adaptive immune responses against tumor antigens. The history has been frustrating; many vaccines produced immune responses without clinical responses. Recent progress has focused on personalized neoantigen vaccines.

*Preventive vaccines* against oncogenic viruses remain the great success — HPV vaccines preventing HPV infection and HPV-driven cancers; hepatitis B vaccines preventing HBV-driven liver cancer. These vaccines work by preventing the initial infection, not by treating established cancer.

*Therapeutic cancer vaccines* aim to treat existing cancer:

*Sipuleucel-T* (Provenge). The first approved therapeutic cancer vaccine (2010). Autologous dendritic cells activated against PAP-GM-CSF fusion protein. Approved for asymptomatic metastatic castration-resistant prostate cancer. Modest survival benefit. Use has been limited by cost and complexity.

*BCG* (Bacillus Calmette-Guérin). Used intravesically for non-muscle-invasive bladder cancer for decades. Activates innate and adaptive immunity locally. The original "immunotherapy" in some sense.

*Talimogene laherparepvec (T-VEC)*. An oncolytic herpes simplex virus engineered to lyse cancer cells and stimulate immunity. Approved 2015 for advanced melanoma. Local injection produces local lesion regression and some systemic responses.

The newer wave is *personalized neoantigen vaccines*. The patient's tumor is sequenced, neoantigens are predicted computationally, and a personalized vaccine is manufactured and administered. The vaccine primes T cell responses against the patient's tumor neoantigens.

Early clinical data:
- *mRNA-based personalized vaccines* (BioNTech BNT122 and similar). Phase 1-2 trials in melanoma, pancreatic cancer, glioblastoma, and others.
- *Peptide-based vaccines*. Various formulations.
- *DNA-based vaccines*.

The mRNA-4157 melanoma trial (Moderna/Merck, mRNA-4157 + pembrolizumab vs pembrolizumab in adjuvant melanoma) showed improved recurrence-free survival. Phase 3 trials are underway.

The combination of personalized neoantigen vaccines with checkpoint inhibitors is particularly appealing — the vaccine primes new T cell responses; the checkpoint inhibitor prevents shutdown of those responses. Several phase 3 trials are testing this combination across cancer types.

The technical pipeline (sequencing, neoantigen prediction, manufacturing) has become faster (currently weeks rather than months) and cheaper. The infrastructure to support personalized vaccines at scale is being built.

---

## Cytokine therapy

Cytokines are signaling molecules that immune cells use to communicate. As cancer therapy, cytokines provide direct immune-stimulating signals.

*Interleukin-2 (IL-2, aldesleukin)*. High-dose IL-2 produces durable responses in approximately 10-15% of patients with metastatic renal cell carcinoma and metastatic melanoma. The toxicity is severe (capillary leak syndrome, multi-organ effects, ICU-level care required) and limited use to specialized centers. Despite the toxicity, IL-2 was for years the only therapy producing potential cures in these cancers — the first immune-based therapy with that distinction. With newer agents (TKIs for RCC, checkpoint inhibitors for both), IL-2 use has decreased dramatically.

*Interferon-α*. Various indications historically — chronic myelogenous leukemia (replaced by imatinib), hairy cell leukemia, melanoma (adjuvant, with modest benefit), some carcinoid tumors. Use has substantially decreased in oncology.

*Interleukin-12* and other cytokines have been tested but limited by toxicity.

*Engineered cytokines*. Modified cytokines with improved therapeutic ratios are in development. Examples include pegylated IL-2 variants, IL-15 superagonists, IL-12-based products. The technology aims to retain immune activation while reducing systemic toxicity.

*Cytokine fusion proteins*. Antibody-cytokine conjugates that deliver cytokines selectively to tumor sites. Several in clinical trials.

Cytokine therapy is one of the oldest immunotherapy approaches and is being reinvented through engineering. The hope is to maintain the immune-activating benefits while addressing the toxicities that limited the original drugs.

---

## Other emerging immunotherapy approaches

The immunotherapy field continues to expand:

*Bispecific T-cell engagers* (BiTEs). Already covered in 24A. Blinatumomab, teclistamab, talquetamab, mosunetuzumab, epcoritamab, and others. The class is expanding rapidly.

*Allogeneic CAR-T and "off-the-shelf" cellular products*. Cells from healthy donors that can be administered without patient-specific manufacturing. Multiple products in clinical trials.

*Macrophage-based therapies*. CAR-macrophages and engineered macrophages. In early clinical development.

*Engineered NK cells*. CAR-NK cells, expanded NK cells, NK cell engagers (BiKEs, TriKEs). Various clinical trials.

*Innate immune system targeting*. TLR agonists, STING agonists, MDA5 agonists. Multiple agents in clinical trials.

*Microbiome modulation*. Fecal microbiome transplant, defined microbiome compositions, microbiome-derived metabolites. The gut microbiome influences immunotherapy response, and modulation strategies are being tested.

*Photodynamic therapy with immune adjuvants*. Combined approaches.

*Personalized peptide vaccines beyond neoantigens*. Targeting shared tumor antigens with patient-specific HLA matching.

*Tumor microenvironment-modifying agents*. Drugs targeting CAFs, immunosuppressive cells, matrix components, and metabolic factors that suppress anti-tumor immunity.

*Multispecific antibodies* engaging multiple targets simultaneously.

The breadth of approaches in development reflects the recognition that immunity can be engaged through many mechanisms. The integration of these approaches with checkpoint inhibitors and other modalities is one of the major directions in cancer therapy development.

---

## What this chapter gives you

Cancer immunotherapy includes multiple modalities beyond checkpoint inhibitors. CAR-T cells have transformed treatment of B-cell malignancies and multiple myeloma — Tisagenlecleucel, axicabtagene ciloleucel, brexucabtagene autoleucel, lisocabtagene maraleucel for B-cell lymphomas and leukemias; idecabtagene vicleucel and ciltacabtagene autoleucel for multiple myeloma. Response rates in heavily pretreated disease are remarkable, with substantial durable responses.

CAR-T toxicities — cytokine release syndrome and neurotoxicity (ICANS) — require specialized management with tocilizumab, corticosteroids, anakinra, and supportive care. CAR-T treatment is concentrated at high-volume centers.

Solid tumor CAR-T has been more challenging due to antigen heterogeneity, on-target/off-tumor toxicity, immunosuppressive microenvironment, and T cell exhaustion. Multiple approaches (local delivery, multi-antigen targeting, logic-gated CARs, TRUCKs, armored CARs, allogeneic products) are being explored. Early signals exist for specific solid tumor indications.

TIL therapy (lifileucel approved 2024 for melanoma) uses T cells expanded from the patient's tumor. The process is technically complex but provides effective treatment for some patients with limited other options.

TCR-T cell therapy uses T cells engineered with specific T cell receptors. Tebentafusp (technically a soluble bispecific) is approved for HLA-A*02:01-positive uveal melanoma. Cellular TCR-T products are in development for various cancers.

Cancer vaccines have had limited historical success beyond sipuleucel-T, BCG, and T-VEC. Personalized neoantigen vaccines (using mRNA, peptides, or DNA platforms) are showing renewed promise, particularly in combination with checkpoint inhibitors. The mRNA-4157 melanoma trial provides encouraging early data.

Cytokine therapy (IL-2, interferons) is an older immunotherapy approach being reinvented through engineering (modified cytokines, fusion proteins, antibody-cytokine conjugates).

Emerging approaches include allogeneic CAR-T, CAR-macrophages, engineered NK cells, innate immune system targeting (TLR, STING agonists), microbiome modulation, and multispecific antibodies.

The integration of these various immunotherapy approaches with checkpoint inhibitors and other modalities will likely define cancer therapy development over the next decade.

Chapter 26 turns to gene therapy and oncolytic virotherapy — two related approaches that engineer either the patient's cells or attacking viruses to combat cancer.

---

## LLM exercises

1. Ask your LLM to walk through the manufacturing process for autologous CAR-T cell therapy from apheresis through infusion. What are the major technical challenges, what is the typical timeline, and what alternatives (allogeneic CAR-T) are being developed? Identify the major manufacturing innovations that have improved the process.

2. Have your LLM compare the management of grade 3 cytokine release syndrome and grade 3 ICANS after CAR-T therapy. What are the typical presentations, the workup, the role of tocilizumab versus corticosteroids, and the expected outcomes? Construct a clinical algorithm.

3. Use your LLM to explain why CAR-T has worked so well in B-cell ALL but has been more challenging in solid tumors. What specific features of B-cell ALL biology favor CAR-T (CD19 as a clean target, replaceable normal B cells, accessibility of cancer cells), and what specific challenges does solid tumor biology pose?

4. Ask your LLM to walk through the personalized neoantigen vaccine development pipeline. What are the technical steps (sequencing, neoantigen prediction, validation, manufacturing), what are the current performance characteristics, and what is the role in combination with checkpoint inhibitors? Identify the specific cancer types where personalized vaccines are most likely to add benefit.

5. Have your LLM survey the engineered cytokine field. What are the major approaches (pegylated IL-2 variants like NKTR-214/bempegaldesleukin, IL-15 superagonists, IL-12-based products), what is the clinical evidence, and which are most promising? Compare with the historical experience of high-dose IL-2 in renal cell carcinoma and melanoma.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Carl June** developed CAR-T cell therapy for leukemia — engineering a patient's own T cells to recognize and kill cancer. The first clinical successes in 2011 turned terminal pediatric leukemia into a curable disease in some patients.

**Run this:**

```
Who is Carl June, and how does his work on CAR-T cell therapy connect to the cellular therapies we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Carl H. June"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how a CAR-T cell is engineered, expanded, and reinfused.
- Ask it about the cytokine release syndrome that nearly killed early CAR-T patients — and how it was eventually managed.

What changes? What gets better? What gets worse?
