# Chapter 76 — In Vivo Imaging, Photodynamic Therapy, and Specialized Techniques


## TL;DR

- A tumor that you can see growing in a mouse in real time is more useful than one you have to euthanize the mouse to measure.
- The chapter moves through In vivo optical imaging, Other in vivo imaging modalities, Orthotopic tumor models for imaging, Photodynamic therapy, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

A tumor that you can see growing in a mouse in real time is more useful than one you have to euthanize the mouse to measure.

Hold the framing. Cancer research benefits enormously from imaging that allows non-invasive measurement of disease in living organisms. Static measurements at the end of experiments tell you the final result. Dynamic measurements throughout an experiment tell you the trajectory — how quickly the tumor grew, when treatment started working, when resistance emerged. Live animal imaging has become central to modern cancer research.

Beyond imaging, the same fluorescence-based principles enable specific therapeutic applications. Photodynamic therapy uses light-activated drugs to kill cancer cells. Fluorescence-guided surgery improves tumor margin identification during cancer operations. The technologies blur the line between imaging and treatment — diagnostic and therapeutic applications increasingly converge.

This appendix — the second of two on advanced imaging — covers in vivo optical imaging, photodynamic therapy, orthotopic tumor models for imaging applications, specialized applications, and emerging technologies. The chapter complements C-A, which covered flow cytometry and fluorescence microscopy.

Hold the question: *given that we can image cancer in living animals and use light for therapy, what are the specific technologies and applications?*

---

## In vivo optical imaging

In vivo imaging visualizes cancer in living animals (typically mice) over time:

*Bioluminescence imaging (BLI)*. The dominant in vivo optical imaging modality:

*Principle*. Cancer cells engineered to express luciferase (typically firefly luciferase from *Photinus pyralis*). Inject luciferin substrate. Luciferase catalyzes oxidation of luciferin in presence of ATP and oxygen, producing light. Sensitive cameras detect light through tissue.

*Workflow*:
1. Engineer cancer cells with luciferase (stable transfection or transduction).
2. Implant cells in mice.
3. Inject luciferin substrate (typically IP injection).
4. Wait 10-15 minutes for substrate distribution.
5. Image in BLI chamber.
6. Quantify total light emission as surrogate for tumor burden.

*Advantages*:
- Non-invasive (no anesthesia required for imaging itself, though usually used).
- Sensitive (detects as few as ~1000 cells in some applications).
- Reasonably specific (luciferase + substrate = signal only from engineered cells).
- Multiple time points possible (longitudinal studies).
- Whole-body imaging possible.
- Quantitative.

*Limitations*:
- Light absorption by tissues (deeper tumors give less signal).
- Substrate distribution issues (variability over time after injection).
- Requires cancer cells engineered with luciferase.
- 2D imaging primarily (3D possible with multiple views).
- Background autoluminescence in some cases.

*Applications*:
- Monitoring tumor growth and treatment response.
- Detecting metastases.
- Following cancer cell trafficking.
- Comparing treatment efficacy.
- Studying tumor dormancy.

Multiple luciferase variants (firefly, click-beetle red/green, *Renilla*, others) enable multi-color BLI for tracking multiple populations.

*Fluorescence imaging in vivo*. Less common than BLI for tumor monitoring but useful in specific applications:

*Principle*. Cancer cells or animals express fluorescent proteins (GFP, mCherry, etc.). Excite with appropriate wavelength; detect emission.

*Limitations*:
- Tissue autofluorescence creates background.
- Limited tissue penetration (especially with visible-light fluorophores).
- Lower sensitivity than BLI for many applications.

Near-infrared fluorophores (NIR) penetrate tissue better:
- ICG (indocyanine green) — clinically used for various applications.
- Genetically encoded NIR proteins (iRFP variants).
- NIR small molecule probes.

NIR fluorescence imaging is increasingly used for clinical applications, including fluorescence-guided surgery (covered below).

*Specific fluorescent probes for cancer imaging*:
- Cancer-targeted probes (peptides, antibodies labeled with fluorophores).
- Activatable probes (fluorescent only when cleaved by tumor-associated enzymes).
- Reactive oxygen species probes.
- Hypoxia probes.

*In vivo confocal/multiphoton microscopy (intravital imaging)*. Imaging individual cells in living tissues:

*Principle*. Microscope with two-photon laser. Imaging window or exposed tissue. Image individual cancer cells, immune cells, vasculature at cellular resolution.

*Applications*:
- Tumor cell behavior in vivo.
- Tumor-immune cell interactions.
- Drug penetration into tumors.
- Metastasis dynamics.
- Vascular function.

*Limitations*:
- Highly specialized technique.
- Limited depth (still <1 mm typically).
- Specific imaging windows needed.
- Time-intensive.

Intravital imaging has produced important insights about cancer cell behavior that other techniques can't reach. The technique is used in a relatively small number of specialized labs.

---

## Other in vivo imaging modalities

Beyond optical imaging, cancer research uses other modalities:

*Small animal CT*. Computed tomography for animal imaging:
- Anatomic imaging.
- Useful for tumor size and location.
- Higher radiation than diagnostic human CT.
- Functional imaging with contrast agents.

*Small animal MRI*. Magnetic resonance imaging:
- Soft tissue contrast.
- Various sequences for different information.
- Functional imaging possible (DWI, perfusion).
- More expensive and slower than CT.

*Small animal PET*. Positron emission tomography:
- Metabolic and molecular imaging.
- Various tracers (FDG, others).
- Combined with CT (PET-CT).

*Small animal ultrasound*. Ultrasound imaging:
- Real-time imaging.
- Functional and Doppler imaging.
- Tumor blood flow and vascular function.
- Increasingly available with high-frequency systems.

*Hybrid modalities*:
- PET-CT, PET-MRI.
- Optical-CT.
- Multimodal imaging platforms.

The choice depends on the specific information needed. Many studies combine multiple imaging modalities for comprehensive characterization.

---

## Orthotopic tumor models for imaging

The combination of orthotopic implantation and imaging enables sophisticated cancer studies:

*Orthotopic mammary fat pad models for breast cancer*. Cancer cells implanted in mammary fat pad. BLI for tumor monitoring. Metastasis tracking through serial imaging.

*Orthotopic pancreatic cancer models*. Pancreatic cancer cells injected into pancreas. Surgical procedure but produces models more faithful to human pancreatic cancer than subcutaneous implants.

*Orthotopic brain tumor models*. Cancer cells injected intracranially. BLI monitors tumor growth despite blood-brain barrier limitations for substrate.

*Orthotopic lung cancer models*. Intratracheal instillation or other techniques. Lung tumors imaged by BLI or CT.

*Orthotopic colorectal cancer models*. Cecal wall injection. Tumor and metastasis (especially liver) tracking.

*Orthotopic prostate cancer models*. Surgical implantation in prostate. Combined imaging with CT/MRI for prostate visualization.

*Various other tissue-specific models*.

The orthotopic + imaging combination provides better recapitulation of tumor biology than ectopic models while still enabling non-invasive monitoring.

---

## Photodynamic therapy

Photodynamic therapy (PDT) uses light-activated photosensitizing drugs to kill cancer cells.

*Principle*:
1. Patient receives photosensitizer drug.
2. Drug accumulates preferentially in cancer cells (tissue selectivity through tumor microenvironment effects).
3. Light of specific wavelength applied to tumor.
4. Photosensitizer absorbs light energy.
5. Energy transferred to molecular oxygen, generating singlet oxygen and other reactive oxygen species.
6. ROS kill cancer cells.

*Approved photosensitizers and applications*:

*Porfimer sodium (Photofrin)*. The original FDA-approved photosensitizer (1995). Used for:
- Esophageal cancer.
- Lung cancer (endobronchial).
- Early gastric cancer.
- Various other cancers.

Activated by 630 nm red light. Long half-life and prolonged skin photosensitivity.

*5-aminolevulinic acid (5-ALA) and methyl-ALA (MAL)*. Precursors to protoporphyrin IX. Topical or oral administration:
- Actinic keratosis treatment.
- Basal cell carcinoma.
- Bladder cancer (intravesical).
- Brain tumor (5-ALA for surgical guidance).

5-ALA fluorescence-guided surgery is particularly important for glioblastoma — patients drink 5-ALA preoperatively; tumor tissue fluoresces during surgery, helping the surgeon achieve maximal resection.

*Temoporfin (Foscan)*. Used for head and neck cancers. Activated by 652 nm laser.

*Verteporfin*. Used for age-related macular degeneration (vascular targeting). Some cancer applications.

*Newer photosensitizers*. Various in clinical development.

*PDT advantages*:
- Selective (combination of drug accumulation and light targeting).
- Minimal invasive (uses light delivery).
- Repeat treatments possible.
- No cumulative toxicity in conventional sense.
- Surface/cavity application straightforward.

*PDT limitations*:
- Depth of treatment limited by light penetration.
- Photosensitizer pharmacokinetics affect timing.
- Skin photosensitivity (avoid sunlight after some PDT).
- Limited to accessible tumors.
- Resistance can develop.
- Not curative for deep or disseminated disease.

*Light sources*:
- Lasers (various wavelengths).
- LED arrays.
- Fiber optic delivery for internal applications (endoscopic, intraoperative).

PDT has specific clinical applications but has not become a major cancer treatment modality. Specific cancers and contexts (specific skin cancers, early lung cancer, brain tumor surgical guidance with 5-ALA) have established roles.

---

## Photothermal therapy and related approaches

Beyond PDT, related approaches use light-induced heat:

*Photothermal therapy (PTT)*. Light-activated nanoparticles (typically gold) convert light to heat, ablating tumors. As discussed in Appendix C of the original text, has had limited clinical success despite preclinical promise.

*Photoimmunotherapy*. Antibody-photosensitizer conjugates that selectively target cancer cells. The IR700 dye conjugated to antibodies (e.g., cetuximab-IR700, RM-1929/ASP-1929) is activated by near-infrared light, causing membrane damage and antitumor immune responses. Approved in Japan; trials globally.

*Combined imaging and therapy (theranostics)*. The same molecule provides both imaging and therapy. Lutetium-177-PSMA-617 (covered in Chapter 27B) is the major clinical example.

---

## Fluorescence-guided surgery

Cancer surgery increasingly uses fluorescence for tumor margin identification:

*Principle*. Patient receives fluorescent agent that accumulates in cancer cells. During surgery, fluorescence imaging system reveals tumor distribution.

*5-ALA in glioblastoma surgery*. Established clinical application. Patient drinks 5-ALA preoperatively. Tumor cells convert 5-ALA to protoporphyrin IX, which fluoresces under blue light. Surgeon can see tumor extent during surgery, achieving greater extent of resection.

*Indocyanine green (ICG)*. Approved by FDA for many uses. Various oncologic applications:
- Sentinel lymph node mapping.
- Tumor visualization in liver, breast, and other cancers.
- Bowel perfusion assessment.

*Tumor-targeted fluorescent probes*. In clinical development:
- Antibody-fluorophore conjugates (panitumumab-IRDye800, others).
- Activatable probes (cleaved by tumor enzymes).
- Specific cancer cell-targeting probes.

The field aims to provide surgeons with real-time visualization of tumor extent for improved oncologic outcomes. Several products in clinical development; some approved for specific indications.

---

## Cancer imaging in clinical translation

The cancer imaging tools developed in research increasingly translate to clinical applications:

*Clinical imaging modalities* (covered in Chapter 18A):
- CT, MRI, PET, ultrasound — standard cancer imaging.
- PSMA PET for prostate cancer.
- DOTATATE PET for neuroendocrine tumors.
- Other specialized tracers.

*Emerging clinical imaging*:
- Multi-modal imaging combining functional and anatomic information.
- AI-augmented image interpretation.
- Quantitative imaging biomarkers.
- Real-time intraoperative imaging.

*Liquid biopsy as imaging adjunct*. Combining imaging with ctDNA analysis for comprehensive disease assessment.

The translation pipeline from preclinical imaging research to clinical applications is active. Many preclinical imaging tools eventually inform clinical practice.

---

## Practical considerations for cancer imaging research

Several practical issues affect cancer imaging studies:

*Quantitative analysis*. Imaging produces large datasets requiring systematic analysis:
- Volume of interest definition.
- Signal quantification.
- Background subtraction.
- Normalization.
- Time-course analysis.

*Anesthesia for animal imaging*. Most in vivo imaging requires anesthesia:
- Isoflurane is the standard.
- Specific concerns about depth, temperature, recovery.
- Affects physiology (temperature drops, breathing changes).

*Standardization*. Reproducible imaging requires:
- Consistent equipment.
- Standardized protocols.
- Quality controls.
- Calibration standards.

*Data analysis software*. Specialized tools:
- Living Image (PerkinElmer/Revvity) for BLI.
- ImageJ/Fiji for general image analysis.
- Specialized software for specific modalities.
- Machine learning increasingly integrated.

*Statistical considerations for imaging studies*:
- Longitudinal data analysis (repeated measures).
- Mixed-effects models.
- Handling missing data.
- Multiple comparison corrections.

*Ethical considerations*:
- Animal welfare during imaging studies.
- Humane endpoints based on imaging findings.

The imaging field requires substantial expertise across biology, physics, computer science, and engineering. Multidisciplinary teams are typical.

---

## Emerging technologies in cancer imaging

Several emerging technologies are reshaping cancer imaging research:

*Single-cell imaging in vivo*. Combining intravital microscopy with sophisticated reporters to track individual cells over time. Particularly important for metastasis biology.

*Optogenetics in cancer*. Light-activated proteins to control cellular signaling. Various applications in cancer biology research.

*CRISPR-based imaging*. Imaging specific genomic loci using CRISPR-Cas9 systems with fluorescent labels.

*Lattice light sheet microscopy*. High-speed, low-phototoxicity 3D imaging. Cancer applications emerging.

*Tissue clearing methods (CLARITY, iDISCO, others)*. Make tissues optically transparent for whole-organ 3D imaging. Cancer applications include tumor characterization in whole organs.

*Light-sheet fluorescence microscopy for cleared tissues*. Combination with tissue clearing.

*Smart imaging probes*. Activatable, ratiometric, and other sophisticated probe designs.

*AI for image analysis*. Deep learning for image segmentation, classification, and quantitative analysis.

*Multimodal in vivo imaging*. Combining BLI, MRI, PET, etc. in same animal.

*Photoacoustic imaging*. Light-induced ultrasound. Provides both optical contrast and ultrasound spatial resolution.

The cancer imaging field continues to develop rapidly, with new technologies emerging regularly.

---

## What this appendix gives you

In vivo optical imaging uses bioluminescence imaging (BLI) as the dominant modality. Luciferase-expressing cancer cells produce light when luciferin substrate is provided. BLI is sensitive, quantitative, and enables longitudinal studies. Limitations include tissue light absorption, substrate variability, and 2D imaging primarily. Fluorescence imaging in vivo is less common but useful in specific applications, with near-infrared fluorophores providing better tissue penetration.

Intravital microscopy provides single-cell resolution imaging in living tissues. Two-photon microscopy enables deeper imaging with less phototoxicity. Applications include tumor cell behavior, tumor-immune interactions, and metastasis dynamics.

Other in vivo imaging modalities include small animal CT (anatomic, fast), MRI (soft tissue contrast, functional capabilities), PET (metabolic and molecular), ultrasound (real-time, vascular function). Hybrid modalities combine multiple approaches.

Orthotopic tumor models combined with imaging enable studies in physiologically appropriate locations. Various tissue-specific models (mammary, pancreatic, brain, lung, colorectal, prostate) provide better recapitulation than ectopic models.

Photodynamic therapy (PDT) uses light-activated drugs to kill cancer cells through reactive oxygen species generation. FDA-approved photosensitizers include porfimer sodium (Photofrin), 5-aminolevulinic acid (5-ALA) and methyl-ALA, temoporfin, and others. PDT has specific clinical applications (cutaneous cancers, esophageal cancer, bladder cancer, early lung cancer) but has not become a major cancer therapy. 5-ALA fluorescence-guided surgery is established for glioblastoma resection.

Photothermal therapy and photoimmunotherapy (antibody-photosensitizer conjugates) represent related approaches with various development status. The IR700-cetuximab conjugate for head and neck cancer is approved in Japan.

Fluorescence-guided surgery uses fluorescent agents to identify tumor margins during cancer operations. 5-ALA for glioblastoma is established. ICG has multiple applications. Tumor-targeted fluorescent probes in clinical development.

Clinical translation of cancer imaging includes standard modalities (covered in Chapter 18A), emerging tracers (PSMA PET, DOTATATE PET), AI-augmented interpretation, quantitative imaging biomarkers, and real-time intraoperative imaging.

Practical considerations include quantitative analysis approaches, anesthesia for animal imaging, standardization, data analysis software, statistical considerations for longitudinal studies, and ethical considerations.

Emerging technologies include single-cell imaging in vivo, optogenetics in cancer, CRISPR-based imaging, lattice light sheet microscopy, tissue clearing methods, smart imaging probes, AI for image analysis, multimodal in vivo imaging, and photoacoustic imaging.

The cancer imaging field provides essential research tools and increasingly translates to clinical applications. The combination of imaging with treatment (theranostics, fluorescence-guided surgery, PDT, photoimmunotherapy) represents one of the most exciting current directions.

Appendix D covers the molecular biology techniques (Western blot, ELISA, IHC, PCR) that complete the cancer research toolkit.

---

## LLM exercises

1. Ask your LLM to walk through bioluminescence imaging (BLI) for cancer research. What are the components (luciferase-expressing cells, luciferin substrate, imaging system), what is the workflow, and what cancer research questions can BLI address? Identify the major sources of variability in BLI measurements and how to minimize them.

2. Have your LLM compare intravital microscopy with conventional ex vivo histology for studying tumor cell behavior. What unique insights has intravital imaging provided about cancer biology that other techniques couldn't reach? Identify specific examples of cancer biology phenomena discovered or characterized through intravital imaging.

3. Use your LLM to explain 5-ALA fluorescence-guided surgery for glioblastoma. What is the biological basis (heme biosynthesis), how does the surgery proceed, what is the clinical evidence for improved outcomes, and what are the limitations? Identify other fluorescence-guided surgery applications in cancer.

4. Ask your LLM to compare photodynamic therapy with conventional cancer treatments. For three FDA-approved photosensitizers (Photofrin, 5-ALA/MAL, temoporfin): the mechanism, the approved indications, the typical patient experience, and the limitations. Identify why PDT has remained relatively niche despite promising biology.

5. Have your LLM survey emerging technologies in cancer imaging — tissue clearing combined with light sheet microscopy, single-cell in vivo imaging, AI-augmented image analysis, CRISPR-based genomic imaging. For each: the underlying principle, the current state of development, and the cancer research questions these technologies might address.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Ralph Weissleder** founded the Center for Molecular Imaging Research at MGH — developing optical and PET imaging probes that visualize specific molecular signatures in living animals and patients. His work bridges the lab bench and the clinic.

**Run this:**

```
Who is Ralph Weissleder, and how does his molecular imaging work connect to the in vivo imaging techniques we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Ralph Weissleder"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how a near-infrared fluorescent probe is designed for tumor imaging — target choice, optical window, clearance.
- Ask it about Weissleder's miniature MRI for point-of-care cancer diagnostics — the bioengineered scanner that became a startup.

What changes? What gets better? What gets worse?
