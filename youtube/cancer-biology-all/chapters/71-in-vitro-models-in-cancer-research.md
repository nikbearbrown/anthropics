# Chapter 71 — In Vitro Models in Cancer Research


## TL;DR

- The cancer cell in a dish is not a cancer cell in a patient.
- The chapter moves through Two-dimensional cell culture: the workhorse, Established cancer cell lines, Primary cancer cell culture, Three-dimensional cell culture, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

The cancer cell in a dish is not a cancer cell in a patient. But it's how we figure out what cancer cells do.

Hold the framing. Cancer biology is built on experimental models — systems that approximate aspects of human cancer well enough to be informative. Each model has limitations. Cells in culture are not in a body. Mice with cancers are not humans with cancers. Organoids preserve some features but lose others. The art of cancer research is choosing the right model for the question being asked and interpreting results with awareness of what the model captures and what it misses.

The model hierarchy goes from simple (cell lines in 2D culture) to increasingly complex (3D culture systems, co-cultures, organoids, mouse xenografts, genetically engineered mice, patient-derived models). More complex models capture more of the biology but are more expensive and slower. Most cancer research uses combinations — simpler models for screening and mechanism studies, more complex models for validation, ultimately human studies for clinical translation.

This appendix — the first of two on experimental models — covers in vitro cell culture models: established cell lines, primary cultures, 3D systems, co-culture approaches, and organoids. The next — A-B — covers in vivo mouse models, model selection, and practical considerations.

Hold the question: *what aspects of cancer biology can a cell in a dish actually teach us, and how do we set up experiments to extract that information reliably?*

---

## Two-dimensional cell culture: the workhorse

Standard 2D cell culture is the most widely used cancer research model. Cells grown as monolayers on plastic or glass surfaces in defined media. The system has substantial advantages for high-throughput experimentation but profound limitations.

*Advantages*:
- Inexpensive and accessible.
- Easy to manipulate (drug treatments, genetic modifications).
- High-throughput capable.
- Reproducible across labs (in principle).
- Suitable for many biochemical assays.
- Live-cell imaging possible.
- Large quantities of cells can be generated.

*Limitations*:
- Lack of 3D tissue architecture.
- Absence of stromal cells (fibroblasts, immune cells, endothelial cells).
- No vascular system.
- Different mechanical environment than in vivo.
- Selection pressure during establishment of cell lines.
- Genetic drift during long-term culture.
- Often poor predictor of in vivo behavior for many phenotypes.

The limitations have led to recognition that 2D cell culture results require validation in more complex systems before clinical translation. Many drugs that work in 2D culture fail in animal models or clinical trials. The screening function of 2D culture is valuable but the predictive power for clinical efficacy is limited.

---

## Established cancer cell lines

Cancer cell lines are immortalized cancer cells that can be propagated indefinitely in culture. They are the dominant cell-based research tool.

*Major cell line collections*:

*American Type Culture Collection (ATCC)*. The primary US repository. Hundreds of cancer cell lines characterized and distributed.

*European Collection of Authenticated Cell Cultures (ECACC)*. European equivalent.

*Japanese Collection of Research Bioresources (JCRB)*. Japanese repository.

*Cancer Cell Line Encyclopedia (CCLE)*. Database from Broad Institute and Novartis with comprehensive molecular characterization of cancer cell lines. Genomic, transcriptomic, and proteomic data on ~1,000+ cell lines. Available publicly.

*Genomics of Drug Sensitivity in Cancer (GDSC)*. Drug sensitivity data integrated with molecular characterization of cancer cell lines.

*NCI-60*. Panel of 60 cancer cell lines that NCI uses for systematic drug screening since the 1990s. Substantial historical data.

*DepMap (Cancer Dependency Map)*. Systematic CRISPR and RNAi screens across cancer cell lines to identify essential genes. Substantial resource for target identification.

*Selection considerations*:
- *Tissue of origin*. Cell lines derived from specific cancer types.
- *Molecular features*. Specific mutations, gene fusions, expression patterns.
- *Authentication*. Cell lines should be authenticated (STR profiling) to ensure they are what they're claimed to be — cell line cross-contamination is a major historical problem in cancer research.
- *Mycoplasma testing*. Routine testing for mycoplasma contamination.

*Common limitations*:
- Cell lines accumulate genetic and phenotypic changes during long-term culture (genetic drift).
- May not reflect current patient tumor biology.
- Often represent more aggressive/proliferative variants of original tumors.
- Lab-to-lab variation in culture conditions affects behavior.

*Specific cell lines often used*:
- *Breast cancer*. MCF-7 (ER+/PR+), T47D (ER+/PR+), MDA-MB-231 (triple-negative), MDA-MB-468 (TNBC), SK-BR-3 (HER2+), BT-474 (HER2+), HCC1937 (BRCA1-mutant), and many others.
- *Lung cancer*. A549 (NSCLC, KRAS-mutant), H1299 (NSCLC, p53-null), H460 (large cell), H1975 (EGFR L858R/T790M), PC-9 (EGFR exon 19 del), and others.
- *Colorectal cancer*. HCT-116 (MSI), HT-29, SW480, SW620, DLD-1, RKO, and others.
- *Prostate cancer*. LNCaP (AR+), VCaP, PC-3 (AR-negative), DU145 (AR-negative).
- *Leukemia/lymphoma*. K-562 (CML), HL-60 (AML), Jurkat (T-ALL), Ramos and Raji (Burkitt), various.
- *Many other cell lines* for various cancers.

The cell line system provides extensive standardized resources but with the limitations noted.

---

## Primary cancer cell culture

Primary cultures are cells freshly isolated from patient tumors. They have advantages and disadvantages compared to established cell lines.

*Advantages*:
- Closer to original tumor biology.
- Less time for genetic drift.
- Captures patient-specific features.
- Useful for studying tumor heterogeneity.

*Disadvantages*:
- Difficult to establish and maintain.
- Limited propagation (most don't immortalize).
- High variability between samples.
- Stromal cell contamination.
- Limited cell numbers.
- Difficult standardization.

*Sources of primary cells*:
- Surgical specimens (with patient consent and IRB approval).
- Biopsies.
- Fluid samples (ascites, pleural effusions, CSF).
- Blood (for circulating tumor cells and hematologic malignancies).

*Establishment techniques*:
- Tissue dissociation (mechanical and enzymatic).
- Selection methods (FACS, magnetic bead separation, density gradients).
- Specific media optimized for the cancer type.

Primary cultures are particularly useful when established cell lines don't adequately represent the patient population or when studying patient-specific features is important.

---

## Three-dimensional cell culture

3D culture systems address some limitations of 2D culture by recreating aspects of tissue architecture.

*Spheroid culture*. Cells form spherical aggregates in non-adherent conditions or with specific matrices. Multicellular tumor spheroids (MCTS) recreate features like nutrient and oxygen gradients (necrotic core in larger spheroids), cell-cell contacts, and certain signaling environments not present in 2D.

Methods for spheroid formation:
- *Hanging drop method*. Drops of cell suspension on inverted plate lids.
- *Non-adherent culture surfaces*. Cells aggregate spontaneously.
- *Spinner flask*. Continuous agitation.
- *Microwell plates*. Specifically designed for spheroid formation.

*3D matrix-based culture*. Cells grown within or on extracellular matrix preparations:
- *Matrigel*. The dominant matrix. Derived from EHS mouse sarcoma. Contains laminin, collagen IV, heparan sulfate proteoglycans, growth factors. Forms gel at body temperature. Used for organoid culture and many other applications.
- *Collagen gels*. Type I collagen primarily. Used to study fibrillar matrix effects.
- *Synthetic matrices*. Defined hydrogels (PEG-based, others) that allow control of mechanical properties.

*Microfluidic devices and organ-on-chip*. More sophisticated 3D culture systems with controlled flow, multiple cell types, and tissue-like architecture. Increasingly used for cancer research and drug testing.

The 3D culture systems capture some features missed by 2D culture but vary in their fidelity to in vivo tissue.

---

## Organoid culture

Organoids are 3D cellular structures grown from patient tumor samples or pluripotent stem cells that recapitulate aspects of the original tissue or tumor. Developed in the 2010s by Hans Clevers, Toshiro Sato, and others. Now a major research tool.

*Patient-derived tumor organoids*:
- Established from tumor tissue (biopsy or surgical resection).
- Grown in specific 3D matrix (typically Matrigel) with defined growth factors.
- Maintain genetic and phenotypic features of original tumor.
- Can be expanded over months to years.
- Bankable for long-term studies.

*Applications*:
- Drug sensitivity testing for individual patients (personalized medicine applications).
- Mechanism of resistance studies.
- High-throughput drug screening.
- Combination drug screening.
- Genetic perturbation studies (CRISPR, RNAi).
- Biomarker discovery.

*Cancer types where organoid culture has been developed*:
- Colorectal cancer (well-established).
- Pancreatic cancer.
- Breast cancer.
- Prostate cancer.
- Gastric cancer.
- Hepatocellular carcinoma.
- Endometrial cancer.
- Lung cancer.
- Many other cancers (efficiency varies).

*Advantages*:
- Maintain patient-specific tumor biology.
- 3D architecture preserved.
- Multiple cell types possible (though typically tumor cells dominant).
- Suitable for many assays.
- Can be cryopreserved and biobanked.

*Limitations*:
- No vasculature.
- Limited immune cells (without co-culture).
- Matrigel batch variability.
- Establishment efficiency varies (some cancers difficult to grow as organoids).
- Time and cost.
- Standardization challenges across labs.

*Patient-derived organoid biobanks*. Multiple institutions have established organoid biobanks for various cancer types. The Human Cancer Models Initiative (HCMI) is one major effort.

*Clinical applications*. Several studies have correlated organoid drug responses with patient clinical outcomes. The technology is emerging as a potential treatment selection tool but not yet established as standard care.

The organoid field has grown rapidly and is one of the most important recent developments in cancer modeling.

---

## Co-culture systems

Co-culture systems combine cancer cells with other cell types to study interactions.

*Cancer cell-fibroblast co-culture*. Studies cancer-stroma interactions. Various configurations:
- Direct co-culture in same well.
- Trans-well systems separating cell types.
- Conditioned media transfer.
- 3D co-culture in matrix.

*Cancer cell-immune cell co-culture*. Studies cancer-immune interactions:
- T cells with cancer cells to assess cytotoxicity or T cell exhaustion.
- NK cells with cancer cells.
- Macrophages with cancer cells.
- Particularly relevant for immunotherapy research.

*Cancer cell-endothelial cell co-culture*. Studies vascular interactions, including invasion and intravasation.

*Multi-cell type co-culture*. Increasingly complex systems including three or more cell types.

*Organoid co-culture*. Tumor organoids combined with immune cells, fibroblasts, or other components.

*Air-liquid interface culture*. For epithelial cells, growth at air-liquid interface produces more differentiated phenotype.

Co-culture systems are important for studying cancer-microenvironment interactions but add complexity and variability to experiments.

---

## Specialized in vitro systems

Several specialized systems address specific research questions:

*Tumor-on-a-chip*. Microfluidic devices recreating aspects of tumor architecture and microenvironment. Various designs including vascularized tumor models, tumor-immune interaction chips, and others. Used for drug testing and mechanism studies.

*Patient-derived explants*. Fresh tumor tissue maintained ex vivo for short periods. Preserves architecture and cell populations briefly. Used for some drug sensitivity testing.

*Ex vivo tissue slice cultures*. Tumor tissue slices maintained in culture for days. Preserves cellular complexity of original tumor.

*Bioprinted tumor models*. 3D-printed tissue constructs with defined geometries and cell compositions. Emerging technology.

*Microphysiological systems*. Complex multi-organ chip systems modeling tumor and metastatic sites.

*Cancer stem cell assays*. Specific culture conditions to select for or assay cancer stem cell populations (sphere formation, side population, etc.).

Each specialized system addresses particular research questions. The choice depends on the experimental question and the resources available.

---

## What this appendix gives you

In vitro cancer models range from simple 2D cell culture to sophisticated 3D systems, with each level providing different capabilities and limitations.

Two-dimensional cell culture is the workhorse of cancer research — inexpensive, high-throughput, manipulable. Major limitations include lack of 3D architecture, absence of stromal cells, no vascular system, different mechanical environment, and selection pressures during establishment. Results require validation in more complex systems for clinical translation.

Established cancer cell lines provide standardized resources for cancer research. Major collections include ATCC, ECACC, JCRB, CCLE, GDSC, NCI-60, DepMap. Cell line authentication and mycoplasma testing are essential quality control measures. Major cancers each have multiple commonly used cell lines with different molecular features. Limitations include genetic drift, selection bias, and variable lab-to-lab behavior.

Primary cancer cell culture provides closer relationship to patient tumor biology but is difficult to establish and maintain. Useful for patient-specific studies but with high variability.

Three-dimensional cell culture systems address some 2D limitations through spheroid culture (multicellular tumor spheroids), 3D matrix-based culture (Matrigel, collagen gels, synthetic matrices), and microfluidic devices/organ-on-chip systems.

Organoid culture has emerged as a major recent advance. Patient-derived tumor organoids maintain genetic and phenotypic features of original tumors and have applications in drug sensitivity testing, mechanism studies, high-throughput screening, and personalized medicine. Multiple cancer types have established organoid systems. Limitations include no vasculature, limited immune cells, matrix variability, and standardization challenges. Patient-derived organoid biobanks (like HCMI) provide substantial research resources.

Co-culture systems combine cancer cells with fibroblasts, immune cells, endothelial cells, or multiple cell types to study microenvironment interactions. Various configurations from direct co-culture to trans-well systems to 3D matrix-based systems.

Specialized in vitro systems include tumor-on-a-chip microfluidic devices, patient-derived explants, ex vivo tissue slice cultures, bioprinted tumor models, microphysiological systems, and cancer stem cell-specific assays. Each addresses particular research questions.

Appendix A-B continues with in vivo mouse models, model selection, and practical considerations for cancer research.

---

## LLM exercises

1. Ask your LLM to compare the major cancer cell line databases (CCLE, GDSC, DepMap, NCI-60). For each: the scope of data, the major use cases, the access requirements, and an example research question addressable through that resource.

2. Have your LLM explain how patient-derived tumor organoids are established. Walk through the steps from tumor sample to expandable organoid culture: tissue dissociation, embedding in Matrigel, growth factor cocktail, expansion, characterization. Identify the major technical challenges and how they're addressed.

3. Use your LLM to compare 2D cell culture with 3D organoid culture for cancer drug screening. What are the advantages of each, what types of drugs might show different responses between systems, and how should the choice be made for a particular screening application?

4. Ask your LLM to construct a co-culture experiment to study cancer cell-T cell interactions in the context of immune checkpoint inhibitor research. What cells would be co-cultured, what assays would be used, what controls would be needed, and what conclusions could be drawn versus the limitations of in vitro systems for studying immunotherapy?

5. Have your LLM analyze how tumor-on-a-chip technologies might address specific limitations of conventional cancer models. For three example applications (vascularized tumor, tumor-immune interaction, multi-organ metastasis modeling): what unique capabilities does the chip technology provide, and what would the experimental questions be?

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **John Minna** established the NCI lung cancer cell line panel in the 1970s — a systematic collection of patient-derived lines that became the in vitro substrate for nearly all lung cancer drug discovery in the following decades.

**Run this:**

```
Who is John Minna, and how does his lung cancer cell line panel connect to the in vitro models we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"John Minna"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how cell line panels are profiled (gene expression, mutation, drug sensitivity) to guide hypothesis-testing.
- Ask it about the major criticisms of cell line research — and where modern organoid and PDX models address them.

What changes? What gets better? What gets worse?
