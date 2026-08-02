# Chapter 48 — Theranostics and Emerging Cancer Nanotechnology


## TL;DR

- A theranostic agent doesn't just treat or diagnose.
- The chapter moves through Radioligand theranostics: the prostate cancer story, Other radioligand theranostics, Beta vs. alpha emitter radioisotopes, Multifunctional theranostic nanoparticles, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

A theranostic agent doesn't just treat or diagnose. It does both, and uses the diagnosis to guide the treatment.

Hold the framing. Conventional cancer care separates diagnostics from therapeutics. A patient gets imaging to identify and characterize cancer, then receives separate therapy aimed at that cancer. The diagnostic and the therapeutic are different molecules, different infrastructures, often different doctors and clinics. The information flow goes one way — diagnostics inform treatment decisions, but the therapy doesn't update the diagnostic in real time.

*Theranostics* combines therapy and diagnostics in a single agent. The molecule used for imaging is the same molecule (or a sister molecule) used for therapy. The imaging confirms which patients have the target. The therapy delivers payload through the same targeting mechanism. The post-therapy imaging confirms delivery and predicts response. The same molecular event — target binding — drives both diagnosis and treatment.

The cleanest examples are *radioligand theranostics*. Lutetium-177-PSMA-617 for prostate cancer combines PSMA imaging (using gallium-68-PSMA-11 or fluorine-18-DCFPyL for PET imaging) with PSMA-targeted radioligand therapy (using lutetium-177-PSMA-617 for treatment). The patient is imaged to confirm PSMA expression; the same targeting principle then delivers therapeutic radiation. The FDA approval of lutetium-177-PSMA-617 in 2022 was a landmark moment for theranostics in oncology.

This chapter — the second of two on cancer nanotechnology — covers theranostic platforms, multifunctional nanoparticles, and emerging technologies including DNA nanotechnology, exosome-based therapies, and the integration of nanotechnology with other modalities.

Hold the question: *what becomes possible when a single agent can both find a tumor and treat it?*

---

## Radioligand theranostics: the prostate cancer story

The theranostic approach has been most successful with radioligand therapy. The story of PSMA-targeted theranostics for prostate cancer illustrates the principles.

*Prostate-specific membrane antigen (PSMA)*. A transmembrane protein expressed at high levels on prostate cancer cells (and on neovasculature of some other cancers). PSMA expression correlates with disease aggressiveness and is detectable on nearly all metastatic prostate cancer.

*PSMA-targeted imaging*. Small molecules that bind PSMA's active site can be radiolabeled for imaging. The leading agents:
- *Gallium-68-PSMA-11* (Locametz, Illuccix). FDA-approved 2020-2021 for prostate cancer staging and restaging.
- *Fluorine-18-DCFPyL (piflufolastat F-18)* (Pylarify). Similar applications.

PSMA PET imaging is dramatically more sensitive than conventional imaging (CT, bone scan) for detecting prostate cancer recurrence and metastases. The detection of disease at lower PSA levels and at smaller sites has transformed prostate cancer staging.

*PSMA-targeted therapy*. The same targeting molecule can be loaded with a therapeutic radioisotope:
- *Lutetium-177-PSMA-617* (Pluvicto). Approved by FDA in 2022 for PSMA-positive metastatic castration-resistant prostate cancer that has progressed on prior taxane chemotherapy and androgen receptor pathway inhibitor.
- *Actinium-225-PSMA*. An alpha-emitter version in clinical trials. Alpha particles have higher linear energy transfer and may overcome resistance to beta-emitter therapy.

The clinical use:
1. *Staging with PSMA PET*. Identifies patients with PSMA-expressing disease.
2. *Treatment with Lu-177-PSMA-617*. Patients with sufficient PSMA expression receive radioligand therapy.
3. *Follow-up imaging*. Assesses response and remaining disease.

The pivotal VISION trial showed improved overall survival with Lu-177-PSMA-617 plus best supportive care versus best supportive care alone in heavily pretreated mCRPC. The approval has changed the prostate cancer treatment landscape.

The theranostic approach works because:
- The same molecule (PSMA ligand) provides imaging and therapy.
- Patients can be screened for the target before treatment.
- Imaging confirms delivery and predicts response.
- The companion diagnostic is integrated into the therapy.

Toxicities of Lu-177-PSMA-617 include xerostomia (dry mouth from salivary gland uptake — PSMA is expressed on salivary glands), kidney toxicity (PSMA on kidney tubules), bone marrow suppression, and fatigue. The toxicities are generally manageable but can be substantial.

The success of PSMA theranostics has driven development of similar approaches for other cancers.

---

## Other radioligand theranostics

The success of PSMA theranostics has accelerated development of similar approaches.

*Lutetium-177-DOTATATE (Lutathera)*. Approved by FDA in 2018 for gastroenteropancreatic neuroendocrine tumors (GEP-NETs). The targeting moiety is octreotate (a somatostatin analog) that binds somatostatin receptor type 2 (SSTR2), which is overexpressed on most well-differentiated neuroendocrine tumors. Companion diagnostic uses Ga-68-DOTATATE PET imaging.

DOTATATE was the first FDA-approved radioligand theranostic in modern era and established the regulatory pathway. The clinical use has been transformative for neuroendocrine tumor management.

*FAPI (fibroblast activation protein inhibitor) theranostics*. Fibroblast activation protein (FAP) is expressed on cancer-associated fibroblasts in many tumor types. FAPI-based agents target the tumor stroma rather than cancer cells directly. FAPI imaging (Ga-68-FAPI PET) is being explored for many cancer types. FAPI therapy with various radioisotopes is in clinical trials.

*GPR101, GRPR (gastrin-releasing peptide receptor) targets*. Bombesin analogs targeting GRPR for prostate cancer and other cancers expressing the receptor.

*CXCR4 targets*. Pentixafor (chemokine receptor 4 ligand) for imaging various cancers and hematological malignancies. Therapeutic versions in development.

*Glypican-3 targets*. For hepatocellular carcinoma.

*Mesothelin targets*. For mesothelioma, ovarian, and pancreatic cancers.

*HER2 targets* (radiolabeled antibodies). For HER2-positive cancers.

*L1CAM, CEACAM5, others*. Multiple emerging targets.

The radioligand theranostic pipeline is one of the most active areas in cancer drug development. The combination of molecular imaging confirmation + targeted therapy has demonstrated the value of integrating diagnostics with treatment.

---

## Beta vs. alpha emitter radioisotopes

The choice of radioisotope affects the therapeutic profile of radioligand therapy.

*Beta-emitters*. Electrons with intermediate energy and range (millimeters). Lutetium-177 is the most clinically used beta-emitter. Yttrium-90 has higher energy and longer range. Iodine-131 is the classical beta-emitter for thyroid cancer. Copper-67, samarium-153, others.

Advantages of beta-emitters:
- Longer range allows treatment of larger tumors and heterogeneous expression (cells without the target can be killed by crossfire from neighboring cells).
- Well-established clinical experience.
- Lower cost than alpha-emitters.

Disadvantages:
- Lower linear energy transfer means more potential resistance.
- Longer range can damage adjacent normal tissue.

*Alpha-emitters*. Helium nuclei (4 protons + 4 neutrons) with very high energy and short range (50-100 micrometers, about the size of a few cells). Actinium-225 is the leading clinical candidate. Radium-223 is approved for prostate cancer bone metastases (Xofigo, approved 2013). Thorium-227, astatine-211, bismuth-213, others.

Advantages of alpha-emitters:
- Very high linear energy transfer means more lethal DNA damage per particle.
- Short range minimizes off-target effects.
- May overcome resistance to beta-emitter therapy.

Disadvantages:
- More technically challenging to produce (especially Ac-225).
- Higher cost.
- Limited clinical experience.

The development of alpha-emitter theranostics is one of the more exciting current areas. Multiple alpha-emitter products are in clinical trials for various cancer types.

*Auger emitters*. Electrons with very short range (nanometer to micrometer). Indium-111 in some applications. Generally less developed than beta- or alpha-emitter approaches.

---

## Multifunctional theranostic nanoparticles

Beyond radioligand approaches, multifunctional nanoparticles can combine multiple functions in a single platform:

*Drug + imaging agent*. Nanoparticles carrying both a therapeutic drug and an imaging agent (fluorophore, MRI contrast, PET tracer). The imaging tracks the nanoparticle distribution and tumor accumulation; the drug provides therapy.

*Drug + photothermal agent*. Nanoparticles with photothermal properties (gold, certain metals) plus drug payload. Triggered release of drug combined with photothermal cell killing.

*Drug + targeting + responsive release*. Active targeting + drug payload + stimulus-responsive linker for triggered release at the tumor.

*Hybrid platforms*. Multiple imaging modalities (MRI + fluorescence; PET + MRI) plus therapeutic payloads.

The multifunctional approach is conceptually appealing but adds substantial complexity. Each function must work; the integration must be reproducible; the regulatory pathway becomes more complex. Most multifunctional nanoparticles remain in research or early clinical development.

The trade-off is between elegance of design and practical translation. Simpler nanoparticles (single function, well-characterized) have achieved more clinical success than complex multifunctional platforms.

---

## DNA nanotechnology

A more speculative area is *DNA nanotechnology* — using DNA itself as a structural and functional material at the nanoscale.

The principle: DNA is a programmable molecule. Specific base sequences hybridize with complementary sequences in predictable ways. By designing sequences carefully, complex three-dimensional structures can be assembled from DNA strands. These structures can carry drugs, recognize targets, and release payload in response to specific molecular triggers.

*DNA origami*. Folding long DNA strands into specific shapes using shorter "staple" strands. Can create complex three-dimensional shapes (cubes, tubes, complex geometries) at nanoscale.

*DNA aptamers*. Short DNA sequences selected for binding to specific targets. Can serve as targeting ligands.

*DNA nanocarriers*. DNA structures designed to encapsulate drugs and release them upon target recognition.

The clinical translation of DNA nanotechnology has been slow. DNA is rapidly degraded in vivo by nucleases. Manufacturing complex DNA structures at scale is challenging. The regulatory pathway is largely undefined.

Despite these challenges, DNA nanotechnology continues to develop in research. Specific applications (DNA aptamers for targeted delivery; DNA nanostructures for vaccine adjuvants) may emerge in clinical use.

---

## Exosomes and extracellular vesicle-based therapy

Exosomes — small membrane vesicles (30-150 nm) secreted by cells — are increasingly being explored as therapeutic platforms.

*Natural roles*. As discussed in Chapter 13B, exosomes are involved in cell-cell communication, contributing to pre-metastatic niche formation and other cancer behaviors. Their natural roles include carrying proteins, nucleic acids, lipids to recipient cells.

*Therapeutic applications*:

*Exosomes as drug carriers*. Loading exosomes (from various source cells) with drug payloads. Advantages over synthetic nanoparticles include natural membrane composition, ability to cross biological barriers (including the blood-brain barrier), and potentially lower immunogenicity.

*Engineered exosomes*. Source cells genetically modified to express specific surface molecules (targeting ligands) and to load specific cargo (siRNA, mRNA, proteins). The resulting exosomes have engineered properties.

*Tumor-derived exosomes for vaccines*. Tumor exosomes carry tumor antigens. Engineered tumor exosomes have been explored as vaccine platforms.

*Mesenchymal stem cell-derived exosomes*. MSC-derived exosomes have natural immunomodulatory and regenerative properties. Various therapeutic applications being explored.

Clinical translation:
- *Codiak BioSciences* (now Lonza Pharma & Biotech) developed engineered exosomes for clinical applications.
- *exoIL-12* loaded with IL-12 for intratumoral injection. Phase 1 trials in melanoma.
- *Other engineered exosome products* in early development.

The field is young. Manufacturing, characterization, regulatory pathways, and clinical validation are all still being established. The potential is substantial but unproven.

---

## Photodynamic and photothermal therapy

Nanoparticles can mediate light-based therapy approaches:

*Photodynamic therapy (PDT)*. Photosensitizer molecules accumulate in tumors, then are activated by light to produce reactive oxygen species that kill cells. Approved PDT agents include photofrin (porfimer sodium), 5-aminolevulinic acid, temoporfin, and others. Used for skin cancers, esophageal cancer, lung cancer (with bronchoscopic delivery), and bladder cancer (intravesical).

Nanoparticle-based PDT uses nanoscale photosensitizer carriers for improved tumor accumulation and reduced systemic toxicity.

*Photothermal therapy (PTT)*. Nanoparticles that absorb specific wavelengths of light (typically near-infrared) and convert it to heat, ablating tumors. Gold nanoparticles, gold nanorods, gold nanoshells, carbon-based nanomaterials all have photothermal properties.

The approach: nanoparticles accumulate in tumors; near-infrared laser is applied; the heat selectively kills tumor cells. The NIR wavelengths penetrate tissue better than visible light, allowing treatment of deeper lesions.

Nanospectra Biosciences AuroLase (gold nanoshells) reached clinical trials for prostate cancer but did not achieve broad approval.

The PDT and PTT fields have produced clinical applications but limited compared to research activity.

---

## Cancer nanotheranostics for specific cancer types

Different cancer types have different nanotheranostic opportunities:

*Glioblastoma*. The blood-brain barrier limits drug delivery. Nanoparticles designed to cross the BBB (transferrin-receptor targeting, focused ultrasound-enhanced delivery, others) are being developed. Convection-enhanced delivery (direct catheter-based intratumoral delivery) combined with nanoparticle drugs is being explored.

*Pancreatic cancer*. Desmoplastic stroma limits drug penetration. Nanoparticles designed to penetrate stromal barriers (hyaluronidase-co-delivery, matrix-modulating approaches) are being explored.

*Ovarian cancer*. Intraperitoneal delivery of nanoparticle drugs takes advantage of the cavity for prolonged exposure. Nab-paclitaxel and other formulations are being tested.

*Hepatocellular carcinoma*. Liver-targeted nanoparticles (AAV, lipid nanoparticles with liver tropism, specific targeting ligands) provide local delivery. Transarterial chemoembolization combines local delivery with embolization.

*Melanoma*. Accessible to local injection. Various nanoparticle approaches being tested.

*Hematological malignancies*. Less reliant on EPR-based delivery (cancer cells circulate). Targeted delivery through cell-surface receptors (CD20, CD22, CD30, BCMA, CD33, others) is the main approach.

The application varies by cancer biology and accessibility. Solid tumors with limited drug penetration have particularly large opportunities for nanotechnology approaches but also particularly challenging delivery.

---

## Challenges and limitations in cancer nanotechnology

The field has produced extensive research but more modest clinical impact. The major challenges:

*Heterogeneity of tumors and patients*. The EPR effect varies dramatically. Tumor microenvironment varies. Targeting marker expression varies. The "average" nanoparticle behavior across patients may obscure substantial individual variability.

*Manufacturing complexity and cost*. Nanoparticles are more complex to manufacture, characterize, and scale than small molecules. The cost reflects this complexity.

*Regulatory considerations*. Nanoparticle drugs are evaluated as complex products requiring extensive characterization. Bioequivalence between nanoparticle batches is harder to demonstrate than for small molecules.

*Reproducibility*. Some nanoparticle approaches that worked in preclinical models have failed to translate to clinical benefit. The disconnect reflects differences between mouse and human biology, between preclinical and clinical disease, and between optimal model conditions and clinical reality.

*Long-term safety*. Some nanoparticles accumulate in organs (liver, spleen) for extended periods. Long-term consequences of this accumulation are not always well-characterized.

*Competition from non-nanotechnology approaches*. Some applications that nanotechnology was developed for have been displaced by other approaches (e.g., targeted therapy, ADCs).

*Clinical trial challenges*. Demonstrating the value-added of nanoparticle approaches over conventional formulations requires substantial trials.

These challenges have contributed to a slower trajectory than initial enthusiasm predicted. The successful nanomedicines (Doxil, Abraxane, T-DM1, T-DXd, Lu-177-PSMA-617) have demonstrated that the challenges can be addressed, but the bar is substantial.

---

## Future directions

Several trends are reshaping cancer nanotechnology:

*Better tumor accumulation strategies*. Beyond EPR, approaches to enhance tumor delivery include:
- *Tumor-penetrating peptides*. Peptides (iRGD and others) that increase nanoparticle penetration into solid tumors.
- *Microenvironment modulation*. Disrupting the dense matrix (hyaluronidase) or vasculature (anti-VEGF) before nanoparticle delivery to improve penetration.
- *Cell-based delivery*. Using cells (macrophages, T cells, MSCs) as carriers that home to tumors.

*Personalized theranostics*. The PSMA story will be extended to other cancers. Personalized selection of patients based on target expression imaging followed by targeted radioligand therapy. The approach may expand to many tumor types.

*Alpha-emitter therapies*. The actinium-225 and other alpha-emitter approaches are expanding. The supply chain for these isotopes is being scaled.

*Cell-derived nanoparticles*. Exosomes, cell membrane-coated nanoparticles (using natural cell membranes from blood cells or cancer cells), and biomimetic approaches.

*mRNA-based therapeutics beyond vaccines*. mRNA-encoded proteins delivered by LNPs as therapy. Cancer applications emerging.

*siRNA and antisense therapy*. LNP-delivered siRNA and antisense oligonucleotides. Cancer applications increasing.

*Combination platforms*. Single nanoparticles delivering multiple drugs or modalities (chemotherapy + immunotherapy; drug + radiation sensitizer; combination immunotherapy).

*AI-designed nanoparticles*. Computational approaches to designing nanoparticle structures and predicting in vivo behavior. May accelerate discovery and optimization.

*Microbiome-modulating nanoparticles*. Delivering compounds that modulate the gut microbiome to enhance immunotherapy response.

*Self-assembling nanoparticles*. Forming nanostructures in situ rather than as pre-formed particles.

The pipeline is broad and active. The next decade will likely bring more approved cancer nanomedicines, particularly in radioligand theranostics and engineered cellular/exosome therapies.

---

## What this chapter gives you

Theranostics combines therapy with diagnostics in a single molecular framework. The cleanest examples are radioligand theranostics — Lu-177-PSMA-617 for prostate cancer (approved 2022), Lu-177-DOTATATE for neuroendocrine tumors (approved 2018), and many others in development. The approach allows patient selection based on target expression imaging followed by targeted therapy through the same molecular mechanism.

Beta-emitters (Lu-177, Y-90, I-131) provide longer-range cell killing useful for heterogeneous tumors. Alpha-emitters (Ac-225, Ra-223) provide more potent cell killing through very high linear energy transfer in short range, with potential to overcome resistance. The radioisotope choice significantly affects therapeutic profile.

Multifunctional theranostic nanoparticles combine multiple functions (drug, imaging, targeting, responsive release) in single platforms. Conceptually elegant but complex to translate; simpler nanoparticles with well-characterized single functions have achieved more clinical success.

DNA nanotechnology, exosome-based therapies, photodynamic and photothermal therapy, and other emerging approaches expand the toolkit. Most remain in research or early clinical development.

Cancer-specific applications vary by tumor biology and accessibility. Glioblastoma benefits from BBB-crossing strategies; pancreatic cancer needs stroma penetration; ovarian cancer benefits from intraperitoneal delivery; hepatocellular carcinoma from local approaches. Hematological malignancies use surface receptor targeting more than EPR-based delivery.

Challenges include tumor and patient heterogeneity, manufacturing complexity, regulatory considerations, reproducibility issues, long-term safety questions, competition from non-nanotechnology approaches, and clinical trial challenges. These have contributed to slower-than-expected clinical translation but successful nanomedicines demonstrate that the challenges can be addressed.

Future directions include better tumor accumulation (penetrating peptides, microenvironment modulation, cell-based delivery), expanded personalized theranostics, alpha-emitter therapies, cell-derived nanoparticles, mRNA and siRNA therapeutics, combination platforms, AI-designed nanoparticles, and microbiome-modulating approaches.

Chapter 28 turns to clinical trials and regulatory pathways — the infrastructure that translates novel therapies (including nanomedicines) from research to clinical use.

---

## LLM exercises

1. Ask your LLM to walk through the VISION trial of Lu-177-PSMA-617 in metastatic castration-resistant prostate cancer. What was the trial design, what were the outcomes, and how did this trial establish the theranostic paradigm for prostate cancer? Identify the patient selection process and what role PSMA PET imaging plays.

2. Have your LLM compare beta-emitter and alpha-emitter radioisotopes for cancer therapy. For each: the typical energy, range, mechanism of cell killing, manufacturing considerations, and clinical applications. Identify the cancers where alpha-emitter therapy is likely to provide most advantage.

3. Use your LLM to explain how PSMA-targeted theranostics works mechanistically. What is PSMA, why is it a good target for prostate cancer, how do PET imaging and radioligand therapy use the same targeting principle, and what limits the approach (off-target uptake in salivary glands and kidneys)?

4. Ask your LLM to survey the radioligand theranostics in development beyond PSMA and DOTATATE. What targets (FAPI, CXCR4, GRPR, glypican-3, others) are being explored, what is the level of clinical development, and which next theranostic FDA approval is most likely?

5. Have your LLM analyze the gap between cancer nanotechnology research output and clinical translation. What are the major reasons that many promising preclinical nanotechnology approaches fail in clinical trials? Identify specific examples of nanomedicines that succeeded (Doxil, Abraxane, T-DXd) versus those that failed (BIND-014, others), and what distinguished the successes from the failures.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Sanjiv Sam Gambhir** built much of the modern field of molecular imaging at Stanford — including techniques that image specific molecular signatures in vivo for both diagnosis and therapy monitoring. He died of cancer himself in 2020.

**Run this:**

```
Who was Sam Gambhir, and how does his work on molecular imaging connect to the theranostics we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Sanjiv Sam Gambhir"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how a theranostic agent works — image with one isotope, treat with the same molecule labeled differently.
- Ask it about Gambhir's son Milan, whose death from glioblastoma at 16 reshaped his research priorities.

What changes? What gets better? What gets worse?
