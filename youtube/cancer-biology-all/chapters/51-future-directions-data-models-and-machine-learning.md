# Chapter 51 — Future Directions: Data, Models, and Machine Learning


## TL;DR

- The next decade of oncology will be defined by what we can measure and what we can compute.
- The chapter moves through Liquid biopsy: cancer monitoring through blood, Artificial intelligence in oncology, Foundation models and large language models in oncology, Patient-derived models for functional drug testing, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

The next decade of oncology will be defined by what we can measure and what we can compute.

Hold the framing. Cancer biology has produced enormous data over recent decades — sequencing data from millions of tumors, imaging data from billions of clinical encounters, treatment outcome data across millions of patient-years, real-world data from electronic health records. The data exist. The challenge has been turning data into decisions — extracting clinical value from the accumulated information.

Three technological currents are reshaping how oncology uses data. *Liquid biopsy* allows real-time molecular monitoring of cancer through blood-based assays, providing data streams that previously required tissue biopsy. *Artificial intelligence and machine learning* can extract patterns from large datasets, identifying signals invisible to manual analysis. *Patient-derived models (organoids, xenografts)* allow functional testing of individual patient cancers, providing data about specific tumor responses to specific drugs.

Together, these technologies enable a more personalized, more dynamic, more predictive cancer care than was possible even a decade ago. Cancer monitoring through serial liquid biopsies. Treatment selection informed by AI analysis of multi-omic data. Drug testing on patient-derived organoids before treatment selection. The infrastructure for these approaches is being built at scale.

This chapter — the first of two on future directions in cancer research — covers the data, modeling, and computational technologies that are reshaping oncology. The next — 29B — covers the biological frontiers including microbiome, metabolism beyond Warburg, novel combinatorial approaches, and resistance/relapse strategies.

Hold the question: *given that we can now generate vast amounts of cancer-related data, how do we extract clinical value from it?*

---

## Liquid biopsy: cancer monitoring through blood

Liquid biopsy was introduced in earlier chapters (especially 18B). The future of liquid biopsy in oncology involves expansion of applications and improvement of sensitivity.

Current major applications:

*Genomic profiling*. ctDNA-based identification of targetable mutations. FDA-approved liquid biopsy CDx tests (Guardant360 CDx, FoundationOne Liquid CDx, and others) cover many cancer types.

*Resistance monitoring*. Detection of resistance mutations during targeted therapy. T790M emergence in EGFR-mutant lung cancer triggers switch to osimertinib. ESR1 mutations indicate aromatase inhibitor resistance in breast cancer.

*MRD detection*. Minimal residual disease detection after curative-intent treatment. The DYNAMIC trial in colorectal cancer (2022) showed that MRD-guided adjuvant chemotherapy decisions can reduce overtreatment without compromising outcomes. Similar approaches are being validated in other cancers.

*Treatment response monitoring*. ctDNA dynamics during treatment can detect response or resistance earlier than imaging.

*Multi-cancer early detection (MCED)*. Detecting cancer in asymptomatic individuals from blood. Galleri (GRAIL), DELFI, and other approaches are being clinically validated.

The future directions:

*Ultra-sensitive detection*. Improvements in sequencing technology and computational analysis allow detection of cancer signals at ever-lower allele frequencies. Some platforms now detect mutations at 0.01% variant allele frequency or lower, enabling MRD detection in early-stage disease and detection of very small tumors.

*Personalized assays*. Patient-specific assays designed against the mutations found in the original tumor can be more sensitive for detection of that patient's specific cancer than general assays. Signatera (Natera), RaDaR (NeoGenomics), and similar approaches use this strategy.

*Methylation-based detection*. DNA methylation patterns are characteristic of tissue of origin and of cancer. Methylation signatures may detect cancers that shed minimal mutated DNA, particularly early-stage disease.

*Fragmentation analysis*. Cell-free DNA fragments from cancer cells have different size distributions than fragments from normal cells. Analysis of fragmentation patterns may improve cancer detection. DELFI is the leading approach using this principle.

*Tumor-derived extracellular vesicles*. Exosomes carry proteins, RNAs, lipids, DNA from cancer cells. Exosome-based diagnostics provide complementary information to free ctDNA.

*Multi-analyte approaches*. Combining ctDNA, methylation, fragmentation, protein biomarkers, and other signals into integrated detection algorithms.

*Real-time monitoring*. Frequent liquid biopsies during treatment to detect response dynamics. Eventually, possibly continuous monitoring through implantable or wearable devices.

*Cancer interception*. Detecting cancer in its very earliest stages, perhaps before clinical disease, allowing intervention before progression. The concept depends on detection sensitivity exceeding what current technology achieves, but the trajectory is favorable.

The integration of liquid biopsy into standard care continues to expand. The infrastructure (laboratory capacity, ordering systems, result interpretation, treatment decision support) is being built. The clinical evidence for specific applications is accumulating.

---

## Artificial intelligence in oncology

Machine learning approaches are being applied across cancer care:

*Radiology AI*. Automated detection and characterization of cancer on imaging. Multiple FDA-approved tools assist radiologists in:
- Mammography interpretation (multiple FDA-cleared products).
- Lung nodule detection on CT.
- Prostate MRI interpretation.
- Brain tumor segmentation.
- Bone fracture detection in elderly patients with cancer.

The technology can augment radiologist interpretation, reduce variability, and improve detection rates. Implementation has been variable across institutions.

*Pathology AI*. Automated analysis of digital pathology images:
- Prostate biopsy interpretation. Paige Prostate has FDA clearance for assisting in prostate cancer detection.
- Breast cancer Ki-67 quantification.
- Tumor grading assistance.
- Immunohistochemistry quantification.
- Spatial analysis of immune cell infiltration.

The technology is moving from research to clinical practice but adoption is uneven.

*Clinical decision support*. AI tools that synthesize patient data and suggest treatment plans. IBM Watson for Oncology was an early ambitious attempt that didn't achieve broad adoption. Newer tools (often more focused) are being developed. The challenge is integrating diverse data sources, handling uncertainty, and gaining clinician trust.

*Drug discovery*. AI applications throughout drug development:
- Target identification from multi-omic data.
- Molecule design and optimization.
- Predicting drug properties (absorption, distribution, metabolism, toxicity).
- Generating candidate molecules with desired properties.
- AlphaFold-based protein structure prediction enabling structure-based drug design for previously undruggable targets.

The drug discovery applications are reshaping the early stages of drug development.

*Clinical trial design and recruitment*. AI tools for:
- Identifying candidate trials for individual patients.
- Predicting trial enrollment rates.
- Optimizing trial design.
- Synthetic control arms using historical or real-world data.

*Precision oncology decision-making*. Tools to interpret molecular profiling results and suggest treatment options:
- OncoKB, CIViC, ClinGen, and other knowledge bases.
- Commercial tools (Tempus, Foundation, etc.) that integrate molecular and clinical data.
- AI-based ranking of treatment options.

*Real-world evidence generation*. ML approaches to extract clinically meaningful information from electronic health records and other real-world data sources. Helps with comparative effectiveness, safety surveillance, and post-marketing evaluation.

*Risk prediction models*. ML-based prediction of:
- Cancer recurrence risk.
- Treatment response.
- Toxicity risk.
- Survival prognosis.

The model performance for these applications varies. Some models achieve clinical utility; others remain research tools. The translation from model development to clinical impact requires validation, regulatory clearance, integration into workflows, and clinician adoption.

The major challenges of AI in oncology:

*Training data quality*. ML models reflect their training data. Biased or incomplete training data produces biased models.

*Generalization*. Models trained on one population may not perform as well on others (demographic, geographic, institutional differences).

*Interpretability*. Many AI models produce predictions without clear explanation of why. Clinical use requires interpretability that supports clinician decision-making.

*Regulatory clearance*. The FDA framework for AI tools (Software as a Medical Device, SaMD) is evolving. Adaptive ML systems that change over time challenge traditional regulatory approaches.

*Privacy and data sharing*. AI development requires large datasets; privacy regulations and data ownership issues complicate data sharing.

*Integration with workflows*. AI tools must fit into existing clinical practice without adding friction. Poorly integrated tools fail regardless of model performance.

*Trust and adoption*. Clinicians must trust AI recommendations to use them. Building appropriate trust (neither over-trust nor under-trust) is an ongoing challenge.

Despite these challenges, AI in oncology is advancing rapidly. The next decade will likely bring substantial expansion of clinical AI applications across imaging, pathology, decision support, and drug development.

---

## Foundation models and large language models in oncology

A particular development is the application of *foundation models* — large neural networks trained on vast datasets that can be adapted to specific tasks — to oncology.

*Medical large language models*. Models trained on clinical text (research articles, clinical notes, guidelines) that can:
- Summarize patient histories.
- Identify relevant clinical information from notes.
- Answer clinical questions.
- Support clinical reasoning.
- Generate documentation.

The capabilities have advanced rapidly with general LLM development. Specific medical/oncology adaptations (Med-PaLM, GPT-4 with medical specialization, specialty-specific models) demonstrate substantial capabilities. The clinical use is emerging.

*Imaging foundation models*. Self-supervised learning approaches that learn general representations of medical images, then fine-tune for specific tasks. May reduce the data requirements for specific applications.

*Multi-modal foundation models*. Models that integrate text, images, structured clinical data, and other modalities. The integration may enable more sophisticated clinical reasoning.

*Genomics foundation models*. Models trained on large genomic datasets that can predict gene function, variant effects, and other features.

The foundation model development is moving very fast. The clinical applications are emerging but the trajectory suggests substantial impact over the next 5-10 years. The regulatory framework for these systems is still being established.

---

## Patient-derived models for functional drug testing

Beyond data and computation, *patient-derived models* allow functional testing of how individual patient cancers respond to drugs.

*Organoids*. Three-dimensional cellular structures grown from patient tumor samples that recapitulate aspects of the original tumor's biology. Developed in the 2010s and now widely used in research.

The process:
1. Tumor tissue is obtained from biopsy or surgical resection.
2. Tissue is enzymatically disaggregated.
3. Cells are cultured in three-dimensional matrices with specific growth factors and inhibitors.
4. Organoids form within days to weeks.
5. Organoids can be expanded, biobanked, and used for various assays.

Organoid characteristics:
- Maintain genetic and phenotypic features of the parent tumor.
- Can be expanded over months or years.
- Allow high-throughput drug testing.
- Provide individual patient models for treatment selection.

Cancer organoid applications:
- *Drug sensitivity testing*. Test multiple drugs against the patient's organoid to identify which drugs are most active. The information can guide treatment selection.
- *Mechanism of resistance*. Compare drug-sensitive and -resistant organoids to identify resistance mechanisms.
- *Combination screening*. Identify drug combinations with synergistic activity.
- *Personalized medicine*. Match treatments to individual tumors based on organoid response.

Multiple companies and academic groups offer organoid-based testing services. Clinical utility has been demonstrated in case series and small trials but not yet established through large prospective studies as a routine treatment selection tool.

*Patient-derived xenografts (PDXs)*. Tumor tissue implanted in immunodeficient mice. The tumor grows as a more in-vivo-like model, including some interaction with mouse stroma and vasculature.

PDX characteristics:
- Better preserve some aspects of tumor biology (3D architecture, stromal interactions) than organoids.
- Time-consuming to establish (months from implantation to drug testing).
- Resource-intensive (animal facilities, expertise).
- Useful for drug testing and biology research.

Clinical PDX use:
- Drug testing in PDX models that can guide treatment selection. Often not fast enough for individual patient decisions but useful for cancer research.
- Late-line patient guidance when standard options are exhausted.

*Co-culture models*. Organoids or other cellular models grown with immune cells, fibroblasts, or other stromal components. Better recapitulate the tumor microenvironment.

*Tumor-on-a-chip technologies*. Microfluidic devices that recreate aspects of tumor and stromal architecture. Allow more controlled study of cell interactions.

*Single-cell patient-derived models*. Models established from single cells, capturing tumor heterogeneity.

The patient-derived model field is rapidly developing. Clinical translation as a routine treatment decision tool is emerging but not yet established as standard care. The expectation is that integration of patient-derived model testing with conventional molecular profiling will provide more comprehensive treatment guidance over time.

---

## Spatial biology and single-cell technologies

Two related technologies are providing new views of cancer biology:

*Single-cell sequencing*. Sequencing individual cells rather than bulk tissue. Reveals:
- Cellular heterogeneity within tumors.
- Rare cell populations that may drive resistance or metastasis.
- Cancer stem cell biology.
- Tumor evolutionary dynamics.
- Immune cell diversity.

Major single-cell approaches:
- *Single-cell RNA-seq*. Transcriptional profiling of individual cells. Most widely used.
- *Single-cell DNA-seq*. Genomic profiling of individual cells.
- *Single-cell ATAC-seq*. Chromatin accessibility in individual cells.
- *Single-cell proteomics*. Protein expression in individual cells.
- *Multi-omic single-cell*. Combined analysis of multiple data types per cell.

The technology has been research-focused but is moving toward clinical applications. Some specific clinical uses are emerging (single-cell analysis of leukemias for minimal residual disease, characterization of T cells in immunotherapy patients).

*Spatial transcriptomics and proteomics*. Mapping gene expression or protein abundance with spatial resolution in tissue sections. Reveals:
- Tumor architecture in detail.
- Microenvironmental zones with different cell composition.
- Spatial heterogeneity within tumors.
- Cell-cell interactions inferred from neighboring cell types.

Major spatial technologies:
- *Visium* (10X Genomics). Spatial gene expression with 55-micrometer resolution.
- *MERFISH*. High-resolution mapping of hundreds to thousands of genes.
- *CODEX, IBEX, IMC*. Multiplexed protein imaging in tissue.
- *GeoMx (NanoString)*. Region-of-interest profiling.
- *Xenium*. Higher-resolution gene expression mapping.

These technologies are increasing in resolution, multiplexing capability, and accessibility. Clinical applications include better characterization of tumor immune microenvironment, identifying spatial patterns associated with response to immunotherapy, and understanding tumor heterogeneity.

The combination of single-cell and spatial technologies provides multi-dimensional views of cancer that previous approaches could not achieve. The translation to routine clinical care is emerging but not yet standard.

---

## Comprehensive multi-omic profiling

The data dimensions for characterizing cancer continue to expand:

*Genomics*. DNA-level variants, copy number, structural rearrangements. Foundation of current molecular profiling.

*Transcriptomics*. RNA expression patterns. Increasingly part of comprehensive profiling. Bulk and single-cell approaches.

*Proteomics*. Protein expression and modifications. Mass spectrometry-based approaches and antibody-based approaches.

*Phosphoproteomics*. Post-translational modifications relevant to signaling. Can reveal kinase activation patterns.

*Metabolomics*. Small molecule metabolites. Provides functional information about metabolic state.

*Lipidomics*. Lipid composition and metabolism.

*Epigenomics*. DNA methylation, histone modifications, chromatin accessibility.

*Glycomics*. Glycan structures on proteins and lipids. Often abnormal in cancer.

*Microbiomics*. Tumor and gut microbiome composition.

*Immunomics*. Immune cell repertoires (TCR-seq, BCR-seq) and functional states.

Comprehensive multi-omic profiling combines multiple data types for richer characterization. The integration is computationally demanding but provides better understanding of cancer biology than single-data-type approaches.

Clinical translation of multi-omic profiling is emerging:
- *Comprehensive Genomic Profiling (CGP)* tests now often include RNA sequencing.
- *Proteomics-based companion diagnostics* are emerging (mass spectrometry-based assays).
- *Methylation profiling* is increasingly part of brain tumor and other cancer diagnostics.
- *Multi-omic decision support tools* are being developed.

The vision is that future cancer diagnosis and treatment selection will integrate genomic, transcriptomic, proteomic, metabolomic, microbiome, and immune profiling data — informed by AI/ML analysis — to provide truly personalized care. The infrastructure is being built; the clinical implementation is years away from comprehensive use.

---

## Real-world evidence and learning health systems

Beyond research and clinical trials, *real-world evidence* (data from routine clinical practice) is increasingly important:

*Electronic health record data*. Routine clinical data on millions of patients. Provides information on treatment outcomes in practice, comparative effectiveness, and patterns of care.

*Claims data*. Insurance claims data on healthcare utilization. Provides population-scale views of cancer care.

*Registries*. Disease-specific or treatment-specific registries that collect detailed information on cancer patients. SEER, NCDB, AACR Project GENIE, and many others.

*Patient-reported outcomes*. Symptoms, function, quality of life reported by patients. Increasingly collected systematically.

*Wearables and digital health data*. Activity, sleep, vital signs from wearable devices. Emerging applications in oncology.

The use of real-world evidence:
- *FDA acceptance*. Increasing FDA acceptance of real-world data for regulatory decisions, label expansions, and safety surveillance.
- *Comparative effectiveness*. Comparing treatments in real-world practice beyond clinical trials.
- *Synthetic control arms*. Using real-world data as controls for clinical trials, particularly in rare diseases.
- *Post-marketing safety*. Detecting safety signals more rapidly than spontaneous reporting.

*Learning health systems*. Healthcare systems that continuously generate evidence from clinical care, feeding back into improved care. Cancer is one of the disease areas where learning health system concepts are being developed.

The integration of clinical care and research through real-world evidence is one of the major directions in oncology. The infrastructure (data standardization, privacy management, integration with research) is being built.

---

## What this chapter gives you

The data and computational frontiers of oncology are rapidly developing. *Liquid biopsy* enables real-time molecular monitoring through blood-based assays, with applications spanning genomic profiling, resistance monitoring, MRD detection, treatment response monitoring, and multi-cancer early detection. Future directions include ultra-sensitive detection, personalized assays, methylation-based detection, fragmentation analysis, exosome-based diagnostics, multi-analyte approaches, and eventually cancer interception.

*Artificial intelligence* is being applied across oncology — radiology AI for image interpretation, pathology AI for digital pathology, clinical decision support, drug discovery, clinical trial design, precision oncology decision-making, real-world evidence generation, and risk prediction. The technology is advancing rapidly but faces challenges in training data quality, generalization, interpretability, regulatory clearance, privacy, workflow integration, and clinical adoption.

Foundation models and large language models are being adapted for medical applications, with substantial capabilities emerging in clinical text analysis, imaging, multi-modal integration, and genomics.

*Patient-derived models* (organoids, PDXs, co-culture systems, tumor-on-a-chip) allow functional drug testing on individual patient cancers. Clinical translation as treatment selection tools is emerging but not yet established as routine care.

Single-cell sequencing and spatial transcriptomics provide multi-dimensional views of cancer heterogeneity and microenvironment that previous approaches could not achieve. Translation to routine clinical care is emerging.

Comprehensive multi-omic profiling (genomics, transcriptomics, proteomics, metabolomics, epigenomics, microbiome, immune profiling) is being integrated to provide richer cancer characterization than single-data-type approaches.

Real-world evidence from electronic health records, claims data, registries, patient-reported outcomes, and wearables is increasingly used to complement clinical trial evidence. The integration through learning health systems is one of the major directions in oncology.

Chapter 29B continues with biological frontiers — microbiome, metabolism beyond Warburg, novel combinatorial approaches, and resistance/relapse strategies that complement the data and computational approaches covered here.

---

## LLM exercises

1. Ask your LLM to walk through the DYNAMIC trial in colorectal cancer that demonstrated ctDNA-guided adjuvant therapy. What was the trial design, what were the outcomes for ctDNA-positive vs. ctDNA-negative patients, and how does this trial define the future role of MRD detection in oncology? Identify other cancers where similar approaches are being tested.

2. Have your LLM compare three approaches to multi-cancer early detection — Galleri (methylation-based), DELFI (fragmentation-based), and DELFI plus protein biomarkers. For each: the underlying biology, the sensitivity and specificity profile, the strengths and limitations, and the clinical validation status.

3. Use your LLM to explain how patient-derived organoids could be used for treatment selection. What is the process from tumor biopsy to organoid drug testing, what is the typical timeline, and what does the existing clinical evidence suggest about the value-added over conventional molecular profiling? Identify the cancers where organoid-based decision-making is most promising.

4. Ask your LLM to survey FDA-approved AI tools in radiology and pathology. What types of tools have been approved (mammography, lung nodule detection, pathology assistance, others), what is the clinical evidence supporting them, and what is the level of clinical adoption? Identify the major barriers to wider adoption.

5. Have your LLM analyze how foundation models and large language models are being applied to medical decision-making in oncology. What are the demonstrated capabilities, what are the major limitations, and what are the regulatory and ethical considerations? Identify the most promising applications over the next 5 years.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Regina Barzilay** has applied machine learning to cancer risk prediction at MIT — including the Mirai model that predicts breast cancer risk from screening mammograms five years ahead. Her interest in the field began after her own breast cancer diagnosis.

**Run this:**

```
Who is Regina Barzilay, and how does her work on machine learning for cancer connect to the data-driven future directions we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.
```

→ Search **"Regina Barzilay"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through what the Mirai breast-cancer risk model actually predicts and how it's been validated.
- Ask it about the privacy and bias concerns specific to deploying ML models trained on medical imaging data.

What changes? What gets better? What gets worse?
