# Chapter 35 — Radiation Oncology: Principles and Biology


## TL;DR

- Radiation kills cancer cells the same way it killed the first cell that ever lived.
- The chapter moves through How radiation damages cells, Cellular response to radiation, The dose-response curve and the linear-quadratic model, The five Rs of radiobiology, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

Radiation kills cancer cells the same way it killed the first cell that ever lived.

Hold the framing. Ionizing radiation has been part of cancer therapy since 1896, when Wilhelm Roentgen's discovery of X-rays was applied to treating skin cancers within months. The mechanism — DNA damage and cellular death — has been understood at progressively deeper molecular levels for over a century. Modern radiation oncology uses sophisticated technology to deliver radiation precisely to tumors while sparing normal tissue, but the underlying biology is the same: photons or particles deposit energy in tissue, ionize atoms, damage DNA, and trigger cellular consequences including apoptosis and reproductive death.

What has changed is the precision. Radiation therapy in 1950 used cobalt-60 sources or kilovoltage X-rays delivered through simple geometric fields, with little ability to spare adjacent normal tissue. The treatment worked for some cancers but at substantial morbidity. Modern radiation therapy uses intensity-modulated radiation therapy (IMRT), image-guided radiation therapy (IGRT), stereotactic body radiation therapy (SBRT), and proton therapy to deliver radiation doses with sub-millimeter accuracy, sparing organs at risk and enabling cancers that were previously untreatable.

This chapter — the first of two on radiation oncology — covers the principles and biology of radiation therapy: how radiation kills cancer cells, the dose-response relationships, the fractionation schemes, the planning process, and the basic categories of radiation therapy. The next — 21B — covers the modern technologies and clinical applications: IMRT, SBRT, proton therapy, adaptive radiotherapy, radiation toxicities and their management.

Hold the question: *if radiation damages DNA indiscriminately, how do we use it to kill cancer cells preferentially?*

---

## How radiation damages cells

Ionizing radiation transfers energy to tissue through several physical processes. The primary effect is *ionization* — displacing electrons from atoms, breaking chemical bonds, and producing reactive species that damage cellular molecules.

The major targets of radiation damage:

*DNA*. The most consequential target. Radiation can damage DNA in two ways:
- *Direct effect*. Radiation energy directly breaks DNA bonds. This is most important for high-LET (linear energy transfer) radiation like alpha particles and protons at end of range.
- *Indirect effect*. Radiation ionizes water molecules surrounding DNA, producing reactive species (hydroxyl radicals, hydrogen peroxide, superoxide) that diffuse short distances and damage DNA. This is the dominant mechanism for low-LET radiation like X-rays and gamma rays.

The DNA damage includes single-strand breaks, double-strand breaks, base modifications, and crosslinks. Double-strand breaks are the most lethal lesion — they are difficult to repair accurately and can produce chromosomal rearrangements or cell death if mismanaged.

*Other targets*. Beyond DNA, radiation damages cellular membranes (lipid peroxidation), proteins, and other macromolecules. The contributions to cell death vary by cell type and radiation conditions.

The amount of DNA damage scales with radiation dose. A typical fraction of clinical radiation therapy (2 Gray, the standard unit of absorbed dose) produces approximately 40 double-strand breaks per cell. Across a typical treatment course (60-80 Gy total), the cumulative damage is substantial.

---

## Cellular response to radiation

How cells respond to radiation damage determines whether they die or survive. The responses include:

*DNA damage detection*. Sensor proteins (ATM, ATR, DNA-PK, others) detect double-strand breaks and other DNA damage and activate signaling cascades.

*Cell cycle arrest*. The damage response activates p53, p21, and other regulators that halt the cell cycle at the G1/S or G2/M checkpoints, allowing time for repair.

*DNA repair*. Multiple pathways repair the damage:
- *Homologous recombination (HR)*. Accurate repair using the sister chromatid as template. Active primarily in S and G2 phases. BRCA1/2-mediated.
- *Non-homologous end joining (NHEJ)*. Faster but error-prone repair that ligates broken ends. Active throughout cell cycle.
- *Base excision repair (BER)*. For base modifications and single-strand breaks.
- *Nucleotide excision repair (NER)*. For bulky lesions including some radiation-induced damage.

*Apoptosis*. If damage exceeds repair capacity, the cell triggers programmed death through p53-mediated intrinsic apoptosis. Some cell types (lymphocytes, intestinal stem cells, hematopoietic precursors) are particularly susceptible to radiation-induced apoptosis.

*Mitotic catastrophe*. Cells that proceed through mitosis with unrepaired damage may die during or after division. This is the major mechanism of cell death for many slowly proliferating tumor cells.

*Senescence*. Some cells enter permanent cell cycle arrest without dying. They are functionally removed from the proliferative pool but persist in tissue.

*Survival with mutations*. Cells with imperfectly repaired damage may survive but carry mutations. These are the cells that could become secondary cancers years or decades later.

The balance between these responses determines tumor response and normal tissue toxicity. Cancer cells often have altered damage responses (lost p53, defective repair pathways) that affect their radiation sensitivity.

---

## The dose-response curve and the linear-quadratic model

The relationship between radiation dose and cell killing is described mathematically. The standard model is the *linear-quadratic (LQ) model*, which describes the surviving fraction (SF) of cells after radiation dose D:

SF = exp(-αD - βD²)

The α coefficient represents linear cell killing (single-track damage causing lethal lesions). The β coefficient represents quadratic cell killing (two-track damage combining to produce lethal lesions). The ratio α/β characterizes the cellular response and varies by tissue type.

*High α/β tissues* (10 Gy or higher). These tissues respond similarly to high or low fraction sizes. Most cancers (especially rapidly proliferating) have high α/β ratios. Acute-responding normal tissues (skin, mucous membranes, hematopoietic system) also have high α/β.

*Low α/β tissues* (3 Gy or lower). These tissues are more sensitive to fraction size, with high fraction sizes producing more damage than equivalent total doses delivered in many small fractions. Late-responding normal tissues (lung, brain, spinal cord, kidney) generally have low α/β. Some cancers (prostate cancer, melanoma) also have low α/β.

The LQ model has clinical implications:

*Fractionation*. Dividing a total dose into multiple fractions exploits the difference between high α/β tumors and low α/β normal tissues. Each small fraction kills cancer cells (high α/β response) while allowing repair of sublethal damage in normal tissue (low α/β response). The result is a *therapeutic ratio* favoring tumor kill over normal tissue toxicity.

*Hypofractionation*. Delivering radiation in fewer, larger fractions exploits the low α/β of some cancers. For prostate cancer (α/β around 1.5), hypofractionated regimens (e.g., 5 fractions of 7.25 Gy in SBRT) deliver equivalent biological dose with shorter treatment courses. For breast cancer, the START trials and others have shown that moderate hypofractionation (15-16 fractions instead of 25-30) produces equivalent oncologic outcomes.

*Stereotactic body radiotherapy (SBRT)*. Extreme hypofractionation delivering very high doses per fraction (10-25 Gy) in 1-5 fractions. The approach exploits the physics of conformal dose delivery and the biology of cells exposed to very high single-fraction doses (which may include vascular and immunological effects beyond direct cell killing).

*Brachytherapy*. Placing radioactive sources directly in or adjacent to a tumor delivers high doses to the tumor with rapid dose falloff to surrounding tissues. The fractionation can be continuous (low-dose-rate, LDR) or pulsed (high-dose-rate, HDR).

The mathematics of dose, fractionation, and biology underlies modern radiation therapy planning.

---

## The five Rs of radiobiology

A classical framework for understanding tissue responses to fractionated radiation is the *five Rs*:

*Repair*. Normal tissues repair sublethal damage between fractions. The repair process favors normal tissue over tumor tissue (which often has impaired DNA damage response). Fractionation enables this repair-based therapeutic ratio.

*Repopulation*. Cells (both normal and tumor) divide during a treatment course. Acutely responding normal tissues need to repopulate to maintain function. Rapidly proliferating tumors can also repopulate, which is one reason prolonged treatment courses may be less effective. For some tumors (head and neck cancer), accelerated fractionation (delivering treatment faster) overcomes tumor repopulation.

*Redistribution*. Cells in different cell cycle phases have different radiation sensitivities (G2/M most sensitive, S phase most resistant). Fractionation allows cells initially in resistant phases to redistribute through the cycle and become sensitive during subsequent fractions.

*Reoxygenation*. Hypoxic tumor cells are 2-3 times more radioresistant than well-oxygenated cells (because oxygen is required for the chemical reactions that fix radiation damage). After a fraction kills well-oxygenated cells, the remaining hypoxic cells become better oxygenated as the tumor blood supply reaches more cells. This reoxygenation enables subsequent fractions to kill the previously hypoxic cells.

*Radiosensitivity*. The intrinsic sensitivity of cells to radiation varies. Cell type, biological context, and molecular features all affect radiosensitivity.

The five Rs explain why fractionated radiation works better than equivalent total doses in single fractions for many cancers. They also inform why specific fractionation schemes have been developed for specific cancers.

A sixth R sometimes added is *Reactivation* — the recognition that radiation can stimulate immune responses, potentially producing immune-mediated effects beyond direct radiation damage. This is one of the emerging concepts in combining radiation with immunotherapy.

---

## Cancer cell radiation response

Beyond the general cellular response, cancer cells often have specific features that affect radiation sensitivity:

*Cell cycle*. Rapidly dividing cancer cells are typically more sensitive than slowly dividing cells because more cells are in radiosensitive phases of the cycle.

*DNA repair status*. Cancer cells with intact homologous recombination repair are more resistant. BRCA-mutant cells, with HR defects, are more sensitive. Cells with defective NHEJ may be unable to repair double-strand breaks and are very sensitive.

*p53 status*. Cells with intact p53 trigger apoptosis after extensive damage. Cells with mutated p53 may survive damage that would have killed wild-type cells. This is one reason p53-mutant cancers may be relatively radioresistant.

*Hypoxia*. Hypoxic regions of tumors (Chapter 12A) are radioresistant because the indirect mechanism of DNA damage requires oxygen. Drugs that sensitize hypoxic cells (nimorazole, hypoxia-activated prodrugs) are being explored.

*Stem cells*. Cancer stem cells (Chapter 15A) often have enhanced DNA repair and are more radioresistant than bulk tumor cells. Their survival can drive recurrence after radiation.

*Glycolysis and metabolism*. Cancer cell metabolic state affects radiation response. High glycolysis correlates with various radiation responses.

*Specific molecular features*. EGFR amplification is associated with increased radiation resistance. HER2 amplification correlates with radiation response in some contexts. Multiple molecular biomarkers may predict radiation response.

*Tumor microenvironment*. Stromal cells, immune cells, vasculature all affect radiation response. The microenvironment can be a therapeutic target (anti-angiogenic agents combined with radiation; immunotherapy combinations).

The radiobiological understanding of cancer cell response has informed both fractionation choices and combination strategies. Radiation combined with chemotherapy, targeted therapy, or immunotherapy can produce synergistic effects.

---

## Categories of radiation therapy

Radiation therapy is categorized in several ways.

*By treatment intent*:
- *Curative (definitive)*. Cure as the goal. Often combined with other modalities. Examples: head and neck cancer (concurrent chemoradiation), localized prostate cancer (EBRT, brachytherapy, or both), early-stage lung cancer (SBRT).
- *Adjuvant (postoperative)*. After surgical resection to reduce local recurrence. Examples: breast cancer (whole-breast irradiation), rectal cancer (postoperative chemoradiation in some cases), sarcoma.
- *Neoadjuvant (preoperative)*. Before surgery to facilitate resection. Examples: rectal cancer, esophageal cancer.
- *Palliative*. Symptom relief. Examples: bone metastases (single fraction 8 Gy or 5 fractions of 4 Gy), brain metastases (whole brain or SBRT), bleeding tumors.

*By delivery method*:
- *External beam radiation therapy (EBRT)*. Radiation delivered from outside the body. The most common form. Includes IMRT, IGRT, SBRT, proton therapy.
- *Brachytherapy*. Radioactive sources placed directly in or adjacent to the tumor. Includes interstitial brachytherapy (sources placed within the tissue), intracavitary brachytherapy (sources placed within body cavities), surface brachytherapy.
- *Systemic radiotherapy*. Radiopharmaceuticals administered systemically. Iodine-131 for thyroid cancer. Lutetium-177-PSMA for prostate cancer. Lutetium-177-DOTATATE for neuroendocrine tumors. Radium-223 for bone metastases from prostate cancer.

*By radiation type*:
- *Photons*. The most common. X-rays from linear accelerators in EBRT. Gamma rays from radioactive sources in older systems (cobalt-60) or in brachytherapy.
- *Electrons*. Used for superficial tumors. Deposit dose superficially with rapid falloff.
- *Protons*. Charged particles with characteristic Bragg peak (dose deposition increases at end of range, then drops to zero). Allow conformal dose delivery with less integral dose than photons.
- *Heavy ions*. Carbon ions and others. Even more conformal than protons; higher relative biological effectiveness. Available at limited centers worldwide.

---

## The treatment planning process

Modern radiation therapy involves a sophisticated planning process before any treatment is delivered.

*Simulation*. The patient is positioned for treatment in the same position as will be used for therapy. Immobilization devices (custom-molded thermoplastic masks for head and neck cancer, body molds for thoracic cancers, indexing systems for prostate cancer) ensure reproducible positioning across treatment fractions. Imaging — typically a CT scan in treatment position — is acquired for planning.

*Contouring*. The radiation oncologist defines the target volumes and organs at risk on the planning CT. Multiple target volumes are used:
- *Gross tumor volume (GTV)*. The visible tumor.
- *Clinical target volume (CTV)*. The GTV plus regions of suspected microscopic disease.
- *Planning target volume (PTV)*. The CTV plus a margin for setup uncertainty and physiological motion.
- *Internal target volume (ITV)*. The CTV plus margin for internal motion (especially for thoracic and abdominal tumors that move with breathing).

Organs at risk (OARs) are also contoured — heart, lung, spinal cord, brain, kidneys, liver, bowel, salivary glands, others, depending on the treatment site.

*Plan generation*. Using treatment planning software, the medical physicist or dosimetrist generates a plan that delivers the prescribed dose to the target volumes while keeping doses to OARs within acceptable limits. Modern plans use inverse planning — the desired dose distribution is specified, and the software calculates the beam configurations that achieve it.

*Plan evaluation*. The radiation oncologist reviews the plan. Dose-volume histograms (DVHs) summarize the dose received by each target and OAR. Specific dose constraints (typically based on tolerance doses for late effects) guide the evaluation. The plan is approved or revised iteratively.

*Quality assurance*. The plan is independently verified by physics QA before treatment begins. The verification includes both calculation checks and physical measurement on phantom systems.

*Treatment delivery*. The patient is set up daily in treatment position. Image-guided systems verify positioning before each fraction. The treatment is delivered, typically over 5-40 fractions depending on the regimen.

*Quality control during treatment*. Daily imaging confirms positioning. Periodic plan reviews assess whether replanning is needed (for tumor response or anatomic changes during treatment).

The planning process is technologically intensive and requires close collaboration among radiation oncologists, medical physicists, dosimetrists, and therapists. The infrastructure is one of the major investments cancer centers make.

---

## Specific tissue tolerances

Different tissues have different tolerances for radiation. The tolerance is generally expressed as TD5/5 (tolerance dose with 5 percent probability of severe late complications at 5 years) for various organs. Approximate values for standard fractionation:

- *Bone marrow*. 2.5-3 Gy (whole body), much higher for limited volumes.
- *Lens of eye*. 5 Gy.
- *Whole kidney*. 23 Gy.
- *Whole liver*. 30 Gy.
- *Whole lung*. 17.5 Gy.
- *Spinal cord*. 50 Gy.
- *Brain*. 50-72 Gy (depending on volume).
- *Heart*. 40 Gy (whole organ).
- *Esophagus*. 60 Gy.
- *Stomach*. 50 Gy.
- *Small bowel*. 50 Gy.
- *Rectum*. 60 Gy.
- *Bladder*. 65 Gy.

These are approximate values; modern dose constraints use volumetric measures (V20 for lung, V30 for liver) that capture the partial-organ tolerance more accurately than maximum dose alone.

Tumor cure doses vary by cancer type. Approximate doses for definitive radiation:
- *Hodgkin lymphoma*. 20-30 Gy.
- *Some seminomas*. 25 Gy.
- *Cutaneous lymphoma*. 30-36 Gy.
- *Breast cancer (postlumpectomy)*. 45-50 Gy + boost.
- *Prostate cancer*. 70-80 Gy (conventional) or 36-40 Gy in 5 fractions (SBRT).
- *Head and neck cancer*. 70 Gy with concurrent chemotherapy.
- *Lung cancer*. 60-66 Gy conventional or 45-60 Gy in 3-5 fractions for SBRT.
- *Glioblastoma*. 60 Gy.

The therapeutic ratio is the gap between tumor cure dose and normal tissue tolerance dose. For some tumors, this gap is comfortable (lymphomas cure at low doses, well below tissue tolerance). For others, it is narrow (head and neck cancers require doses close to several organ tolerances).

---

## What this chapter gives you

Ionizing radiation kills cancer cells primarily by damaging DNA — either directly through ionization of DNA molecules or indirectly through reactive oxygen species generated from water. Double-strand breaks are the most lethal lesions.

Cellular response to radiation includes DNA damage detection, cell cycle arrest, DNA repair, apoptosis, mitotic catastrophe, and senescence. The balance among these determines cell fate. Cancer cells often have altered responses (p53 loss, repair defects) that affect their radiosensitivity.

The linear-quadratic model describes radiation cell killing mathematically. Different tissues have different α/β ratios — high for most cancers (and acutely responding normal tissues), low for late-responding normal tissues. Fractionation exploits this difference to achieve a therapeutic ratio favoring tumor kill over normal tissue toxicity.

The five Rs of radiobiology — repair, repopulation, redistribution, reoxygenation, radiosensitivity — explain how fractionated radiation works and inform clinical fractionation choices.

Categories of radiation therapy include external beam radiation therapy (the dominant form), brachytherapy (sources placed in or near the tumor), and systemic radiotherapy (radiopharmaceuticals). Modern EBRT uses photons (most common), electrons (for superficial tumors), protons (with conformal Bragg peak dose deposition), or heavy ions.

The treatment planning process — simulation, contouring (GTV, CTV, PTV), inverse plan generation, plan evaluation, quality assurance, and treatment delivery with image guidance — is technologically intensive and requires multidisciplinary expertise.

Tissue tolerance doses and tumor cure doses define the therapeutic window for radiation. The window varies by cancer type and is one of the key considerations in treatment planning.

Chapter 21B turns to the modern technologies that have transformed radiation oncology — IMRT, IGRT, SBRT, proton therapy, adaptive radiotherapy — and the management of radiation toxicities. The integration of these technologies with the biology covered here produces the modern practice of radiation oncology.

---

## LLM exercises

1. Ask your LLM to walk through the linear-quadratic model of radiation cell killing. What do α and β represent biologically, why does the α/β ratio differ between tissues, and how does the model inform fractionation choices? Construct a numerical example comparing 60 Gy in 30 fractions versus 36 Gy in 5 fractions for prostate cancer (α/β=1.5).

2. Have your LLM explain how oxygen affects radiation cell killing. What is the oxygen enhancement ratio (OER), why are hypoxic cells radioresistant, and how does reoxygenation during fractionated radiation affect tumor response? Identify the therapeutic strategies being developed to overcome hypoxic radioresistance.

3. Use your LLM to construct a typical treatment planning scenario for early-stage breast cancer. Walk through the simulation, target volumes (GTV, CTV, PTV), organs at risk (heart, lung, contralateral breast), dose prescription, and key plan evaluation criteria. Identify the major late effects of radiation and how to minimize them.

4. Ask your LLM to compare proton therapy with photon therapy from a physics perspective. What is the Bragg peak, how does it affect dose distribution, and in what specific cancers does proton therapy offer meaningful advantage? Probe: which patients should be referred for proton therapy versus standard photon therapy?

5. Have your LLM explain the rationale for stereotactic body radiation therapy (SBRT). What biological principles does SBRT exploit, what tumors are particularly suited for SBRT, and how do oncologic outcomes compare with conventional fractionation? Identify the key technological prerequisites for SBRT delivery.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Henri Coutard** developed fractionated radiotherapy in the 1920s at Paris's Curie Foundation — discovering that dividing radiation into many small doses dramatically reduces normal-tissue damage while maintaining tumor kill. Every modern radiotherapy regimen builds on his protocols.

**Run this:**

```
Who was Henri Coutard, and how does his work on fractionated radiotherapy connect to the radiation oncology principles we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Henri Coutard"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to explain the four R's of radiobiology — repair, repopulation, reoxygenation, redistribution — that justify fractionation.
- Ask it about how early radiation oncologists figured out tumor sensitivities by trial-and-error.

What changes? What gets better? What gets worse?
