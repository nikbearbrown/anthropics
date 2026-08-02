# Chapter 2 — Cancer Diagnosis: Imaging and the Tissue Sample
*The Scan Was Never the Diagnosis.*

A 64-year-old woman has a 2-centimeter mass in the tail of her pancreas, found incidentally on a CT scan ordered for back pain. The radiologist's report reads "mass suspicious for adenocarcinoma." Her family hears the word *adenocarcinoma* and assumes the diagnosis is made.

It is not.

An endoscopic ultrasound-guided fine-needle aspiration returns "atypical cells, cannot exclude malignancy — nondiagnostic." A second aspiration returns "benign pancreatic acinar tissue." Now there are three pieces of evidence pointing in different directions: an image that looks like cancer, a first sample that is ambiguous, and a second sample that is reassuring. The oncologist has to decide whether the reassuring biopsy means there is no cancer — or whether the needle simply missed it.

Pancreatic tumors grow inside dense reactive tissue. A needle can pass directly through the mass and pull back stroma rather than tumor. A negative result here is genuinely ambiguous: it could mean no cancer, or it could mean the cancer was there and the needle didn't reach it.

The image was never the diagnosis. The image was a probability. The tissue is supposed to be the ground truth — but only if the tissue is the right tissue. Understanding that chain — how imaging assigns a probability, why tissue is privileged, and how tissue can mislead when the sample is wrong — is what this chapter is about.

---

Every imaging modality reports a signal: tissue density, water content, sound reflection, metabolic activity. Each of these signals correlates with malignancy imperfectly. The radiologist converts the signal into a probability, usually expressed in calibrated language. "Suspicious for" is not "diagnosed as." "Cannot exclude" is not "consistent with." These words encode genuine uncertainty about whether a specific set of cells, in a specific patient, are malignant.

**Computed tomography** reconstructs cross-sectional anatomy from X-rays rotated around the patient. It is the workhorse for detecting masses, evaluating metastatic spread, and guiding needles to lesions. Its soft-tissue contrast is limited — adjacent structures with similar densities can be hard to distinguish — and it exposes patients to ionizing radiation, roughly 8–15 millisieverts for a body CT versus about 0.1 for a chest X-ray (NCI, *CT Scans and Cancer Fact Sheet*). CT is also the substrate for RECIST — the Response Evaluation Criteria in Solid Tumors — the standardized measurement rules that allow tumor size to be compared reliably across serial scans and between institutions (Eisenhauer et al., 2009).

**Magnetic resonance imaging** uses magnetic fields and radiofrequency pulses; different pulse sequences emphasize different tissue water environments, giving it superior soft-tissue contrast for the brain, spinal cord, pelvic structures, and breast. Breast MRI is the most sensitive imaging modality for breast cancer detection, at the cost of lower specificity — more false positives. No ionizing radiation. Longer acquisition time, contraindicated with certain metallic implants.

**Ultrasound** uses high-frequency sound waves and is real-time, portable, and radiation-free. It excels at guiding needles to superficial lesions in real time and at characterizing solid versus cystic masses. Its quality is substantially operator-dependent — the same lesion can look different in different hands. Gas and bone block sound transmission, limiting its use in the lung and for structures deep to the ribs.

**Positron emission tomography** with fluorodeoxyglucose — PET-FDG — images metabolic function rather than anatomy. FDG is a glucose analog labeled with fluorine-18; cells with high glucose uptake trap it, and the positron emission is detected. Cancer cells, with their high metabolic rates, accumulate FDG. But so does inflammation, active infection, healing surgical sites, and brown adipose tissue. And some tumors — mucinous cancers, some indolent lymphomas, some brain metastases from certain primaries — take up FDG poorly. PET-FDG raises probability at a hot spot and lowers it at a cold one. It does not establish diagnosis at either.

The unifying point: each modality has a characteristic false-positive and false-negative profile that is determined by the biology of what it measures. CT misses lesions below its resolution threshold and conflates similar-density structures. MRI misses fast-moving processes and certain calcified lesions. Ultrasound depends on who is holding the probe. PET lights up inflammation and misses low-metabolism tumors. No combination of imaging eliminates the false-positive rate. None eliminates the false-negative rate. The image raises or lowers the probability of malignancy; it does not determine it.

![Five-link diagnostic chain from clinical suspicion through molecular workup, with each link's failure mode annotated](images/02-cancer-diagnosis-imaging-and-the-tissue-sample-fig-01.png)
*Figure 2.1 — The diagnostic chain and its failure modes*

<!-- → [DIAGRAM: diagnostic workup flow — clinical suspicion → imaging (probability raised or lowered) → biopsy (sampling) → pathology (ground truth, conditional on representative sampling) → molecular workup; failure modes annotated at each arrow: imaging: false positive/false negative by modality; biopsy: needle miss, sampling bias, insufficient tissue; pathology: sampling error propagated forward] -->

---

A radiographic abnormality, however compelling, is not a cancer diagnosis. Cancer diagnosis requires cells or tissue examined by a pathologist — this is not convention or caution, it is a reflection of what malignancy is. Malignancy is defined by what cells look like, how they are organized, whether they have invaded through basement membranes, and whether they display features of de-differentiation that predict behavior. These features are visible only under a microscope. An image shows a mass. It does not show the cells inside it.

The standard tissue preparation for solid tumors is **FFPE** — formalin-fixed, paraffin-embedded. The tissue is fixed to stop autolysis and preserve morphology, then infiltrated with paraffin to allow thin sectioning. Sections are cut at a few micrometers and mounted on glass slides. The routine stain is **hematoxylin and eosin**: hematoxylin binds nucleic acids and stains nuclei blue; eosin binds proteins and stains cytoplasm and extracellular matrix pink. The contrast between the two reveals cell shape, nuclear size and regularity, the ratio of nucleus to cytoplasm, mitotic figures, glandular or squamous architecture, necrosis, and invasion into vessels or nerves. A trained pathologist reads this landscape and makes the diagnosis: what cell type, what grade, what is the margin status, what has the tumor invaded.

The pathology report is the foundation document for treatment — not the imaging report, not the laboratory values, not the clinical impression. The report establishes what the cancer is. Everything else establishes what to do about it.

**Immunohistochemistry** extends the morphological reading. Antibodies against specific proteins are applied to the tissue section; secondary antibodies carry a chromogen that stains where the protein is present. This lets the pathologist identify a tumor's lineage and its therapeutic targets. Cytokeratins identify carcinomas and distinguish them from sarcomas and lymphomas. TTF-1 identifies lung and thyroid origin among adenocarcinomas. CD20 marks B-cell lymphomas. Estrogen receptor and progesterone receptor status in breast cancer directly determines whether hormonal therapy applies. HER2 overexpression or amplification determines trastuzumab eligibility. PD-L1 expression informs checkpoint inhibitor selection. Mismatch-repair deficiency, detectable by IHC loss of MLH1, MSH2, MSH6, or PMS2, identifies tumors likely to respond to pembrolizumab regardless of histological type.

IHC is what converts "adenocarcinoma" into "lung adenocarcinoma, TTF-1 positive, PD-L1 TPS 80%" — a diagnosis with enough specificity that treatment can be assigned. The morphology tells you what kind of thing it is. The IHC tells you which one.

---

Tissue is ground truth only if the tissue is representative of the lesion. This is the hardest idea in this chapter, and it is the one that the opening case turns on.

A biopsy samples a tiny fraction of a heterogeneous mass through a needle a millimeter or two in diameter. Three distinct failures are possible.

**The needle misses the tumor.** It passes through the mass and samples adjacent normal or reactive tissue instead. In pancreatic adenocarcinoma, the tumor often constitutes a minority of the mass volume; the bulk is dense desmoplastic stroma — activated fibroblasts, collagen, and inflammatory cells — that surrounds and compresses the malignant glands. A needle aimed at the radiographic center of the mass can aspirate stroma and return benign acinar cells or inflammatory tissue while the tumor sits millimeters away.

**The needle samples an unrepresentative region.** It hits the mass but catches a necrotic core, a low-grade area, or a region of reactive change rather than the viable, diagnostically informative tumor. In a large, heterogeneous tumor, the region biopsied may not carry the mutations or the grade that drive the lethal behavior. This is a version of the spatial heterogeneity problem: the sample is genuine tumor tissue, just not the tissue that matters most.

**The needle obtains too little tissue.** It enters the right region and retrieves tumor cells, but the material is insufficient for the full molecular profiling that modern treatment requires. A diagnosis can be made from a small sample. A complete molecular workup — next-generation sequencing of a gene panel, PD-L1 quantification, HER2 amplification by FISH — may require substantially more tissue than a fine-needle aspiration provides.

The asymmetry of these failures is critical: **a positive biopsy is highly reliable; a negative biopsy does not exclude cancer.** A positive result means malignant cells were identified — they were present in the sample. A negative result means this sample showed no malignancy, which is consistent with no cancer in the lesion, or with a cancer that the needle did not reach. The reliability of a negative result is bounded by how confident you are that the needle sampled the right place.

![Three needle endpoints that each yield a false negative: stroma beside tumor, necrotic zone, and too-small core](images/02-cancer-diagnosis-imaging-and-the-tissue-sample-fig-02.png)
*Figure 2.2 — Three ways a needle returns a false negative*

---

The two main needle approaches trade off invasiveness against how much the sample can establish.

**Fine-needle aspiration** uses a thin needle — typically 22–25 gauge — to aspirate loose cells, which are smeared on a slide and read as cytology. The procedure is fast, well-tolerated, and usable for superficial lesions and for endoscopic guidance. FNA yields cells but not architecture — the pathologist can identify malignant cells but cannot determine whether they have invaded beyond a basement membrane, cannot always distinguish well-differentiated cancer from reactive atypia, and usually cannot obtain enough material for molecular profiling. FNA is appropriate when cytological confirmation is all that is needed — confirming lymph node metastasis in a patient with a known primary, for instance — and when the architecture and molecular material the next treatment decision requires are not necessary.

**Core needle biopsy** uses a larger needle — typically 14–18 gauge — with a spring-loaded mechanism that cuts a cylinder of tissue a millimeter or two in diameter and a centimeter or more long. The cylinder preserves architecture: the pathologist can see how cells are arranged relative to each other and to surrounding tissue, can assess invasion, and has enough material for IHC and molecular testing. Core biopsy is the preferred approach when the diagnosis requires architectural assessment or when treatment planning requires a molecular profile. Its complication rate is low but not zero — bleeding, infection, pneumothorax for lung lesions, pancreatitis for pancreatic sampling.

For any given lesion, the choice between FNA and core is a question of what the diagnosis needs to establish and what the downstream treatment decision will require. A thyroid nodule can often be diagnosed by FNA cytology; the diagnosis of follicular carcinoma, which requires the identification of capsular or vascular invasion, cannot be made on FNA at all and requires surgical excision of the whole nodule. A retroperitoneal soft-tissue mass requires core biopsy both to establish histological subtype — which determines whether surgery, radiation, or chemotherapy comes first — and to provide tissue for molecular profiling that identifies targetable alterations.

---

Return to the woman with the pancreatic mass. Image is highly suspicious. First FNA: nondiagnostic. Second FNA: benign acinar tissue. The team must decide whether to accept the benign result or proceed.

The tempting reasoning: tissue beats imaging; the most recent tissue shows no cancer; call it benign and reassure her. This correctly ranks tissue above imaging but makes a specific error — it treats "benign tissue obtained" as equivalent to "the lesion is benign." For a pancreatic mass, those are not the same statement.

Work through the numbers. From the imaging features and clinical context, the pretest probability of malignancy is high — say 80%. EUS-guided FNA of solid pancreatic masses has a sensitivity in the 80–90% range, meaning 10–20% of true cancers yield a non-malignant aspirate (NCI, *Tests and Procedures*). Apply this informally. The pretest odds are 80:20 = 4:1 in favor of cancer. A negative result is roughly 15% likely if cancer is present (a missed sampling) and 95% likely if cancer is absent — a likelihood ratio of about 0.16. Posterior odds of cancer are approximately 4 × 0.16 = 0.64, corresponding to a post-biopsy probability of malignancy around 39%.

Thirty-nine percent is not a benign result. It is a result that leaves more than one-in-three chance that the patient has cancer and the needle missed it. The benign tissue is consistent with two explanations — no cancer, or the cancer was present and the dense stroma deflected or filled the needle. The image set the probability; the negative biopsy could not overturn it, because when sensitivity is imperfect and pretest probability is high, even a reassuring result leaves substantial residual probability.

![Bar pair showing probability of malignancy falling only from 80% pretest to 39% after a negative biopsy](images/02-cancer-diagnosis-imaging-and-the-tissue-sample-fig-03.png)
*Figure 2.3 — A negative biopsy cannot overturn high pretest odds*

The correct course is not reassurance. It is repeat sampling with a core technique to obtain architecture and more material, presentation at a multidisciplinary conference, and consideration of surgical resection for definitive pathology if repeat sampling remains nondiagnostic against a high pretest probability.

The principle works in both directions and has a real cost. Refusing to accept negative biopsies drives repeat procedures, each carrying its own complication risk. The skill is not "never trust a negative" but calibrated interpretation: how much does this specific negative result, from this specific technique, against this specific pretest probability, move the posterior? That requires knowing the test's sensitivity and the pretest probability — neither of which is printed on the pathology report.

---

The diagnostic chain in oncology is: clinical suspicion, then imaging to assign a probability, then biopsy to sample the tissue, then pathology to examine it, then molecular workup to characterize it for treatment. Each link can break in its characteristic way.

Imaging breaks by producing false positives that lead to unnecessary biopsies or false negatives that miss cancers. The false-positive and false-negative profiles differ by modality: CT for anatomy with limited soft-tissue contrast, MRI for soft-tissue detail with lower specificity in some settings, PET for metabolic function that lights up inflammation as readily as cancer.

Biopsy breaks by sampling the wrong tissue — missing the lesion, hitting a non-representative region, or obtaining too little for the downstream workup. The failure is silent: the report comes back and says what was in the sample, not whether the sample was the right tissue.

Pathology breaks when the tissue is genuinely ambiguous — atypical but not diagnostic, like the first FNA in the opening case. IHC extends the resolution, but it cannot compensate for a sample that contained no tumor cells.

The whole chain is only as strong as its weakest link, and the weakest link is almost always the biopsy — not the imaging, not the pathology reading, but the question of whether the needle was in the right place.

---

## Exercises

**Warm-up**

1. *[Recall — moderate]* Explain in three sentences why a pathologist's reading of tissue is treated as the diagnostic ground truth while a radiologist's reading of an image is not, even when both experts are equally skilled. Your answer should name what the pathologist sees that the radiologist cannot, and why that difference defines malignancy.
*What this tests: whether you understand the epistemological basis for tissue diagnosis — it is not just hierarchy, it is that malignancy is defined by cellular features visible only under the microscope.*

2. *[Recall — moderate]* Name three benign processes that can produce an FDG-avid focus on PET and two tumor types that can be FDG-negative despite being malignant. For each false positive, name the biological mechanism that elevates glucose uptake; for each false negative, name the mechanism that reduces it.
*What this tests: understanding PET as a functional rather than anatomical modality — the false-positive and false-negative profiles follow from the biology of glucose uptake, not from imaging artifact.*

3. *[Recall — moderate]* State the asymmetry of biopsy results — why a positive biopsy is reliable in a way a negative biopsy is not — and name the three specific mechanisms by which a needle can return a negative result from a lesion that contains cancer.
*What this tests: the central conceptual claim of the biopsy section — the positive-negative asymmetry and the physical mechanisms that produce false negatives.*

**Application**

4. *[Apply — moderate-hard]* A breast core biopsy has sensitivity of 95% for a sampled lesion. A radiologist estimates the pretest probability of malignancy for a particular mass at 60% (BI-RADS 4C). The biopsy returns benign. Using a likelihood-ratio or 2×2 approach, calculate the post-biopsy probability of malignancy. Then state whether you would accept the benign result or recommend re-biopsy, justify the threshold you used, and explain how your answer would change if the pretest probability were 30% instead of 60%.
*What this tests: applying Bayesian reasoning to a biopsy result; understanding that the same test result carries different clinical implications at different pretest probabilities.*

5. *[Apply — moderate-hard]* Compare FNA and core needle biopsy for a 2-cm thyroid nodule versus a 4-cm retroperitoneal soft-tissue mass. Which would you choose for each? Your answer should specify what diagnosis each case requires, whether architectural assessment is necessary, and whether molecular profiling for downstream treatment planning changes the choice.
*What this tests: matching biopsy technique to diagnostic requirement — FNA when cytology is sufficient, core when architecture and molecular material are required.*

6. *[Apply — hard]* A lung nodule is 8 mm, FDG-avid on PET with an SUV of 6.4, and has spiculated margins on CT. A bronchoscopic biopsy returns normal bronchial mucosa. The pulmonologist considers the case closed. Using the positive-negative asymmetry of biopsy results and the pretest probability logic from the pancreatic-mass example, explain why the pulmonologist's reasoning is potentially wrong, what specific sampling failure could explain the result, and what the appropriate next step is.
*What this tests: applying the negative-biopsy reasoning to a new clinical scenario; connecting imaging probability to the interpretation of a negative result.*

**Synthesis**

7. *[Synthesis — hard]* Draw the diagnostic chain for a suspected liver lesion in a 55-year-old with known hepatitis B cirrhosis: clinical suspicion → imaging choice → biopsy choice → pathology → IHC. At each arrow, write the dominant failure mode and one mitigation. Then explain how the pretest probability for hepatocellular carcinoma changes the biopsy decision — specifically, at what level of pretest probability established by imaging criteria (LI-RADS) would current guidelines allow treatment without biopsy, and what is the reasoning that justifies that exception to the tissue-is-ground-truth principle.
*What this tests: integrating the full diagnostic chain; applying the pretest-probability logic to a real clinical scenario where the "tissue is required" rule has a justified exception.*

8. *[Synthesis — hard]* An oncologist receives a pathology report on a lung mass: "poorly differentiated carcinoma, TTF-1 negative, p40 negative, synaptophysin weakly positive." The oncologist needs to determine the primary site and whether the patient is eligible for a KRAS G12C inhibitor. Explain what the IHC pattern establishes and does not establish about cell lineage, what additional IHC markers you would request to narrow the differential, and what the molecular testing requirement means for the biopsy — specifically whether the current sample is likely sufficient and what you would do if it is not.
*What this tests: reading an IHC panel as a logical problem; connecting lineage determination to treatment eligibility; applying the "insufficient material" failure mode to a real diagnostic scenario.*

**Challenge**

9. *[Challenge — very hard]* The "Still Puzzling" section asks how heterogeneous a tumor can be before a single core biopsy is fundamentally inadequate for treatment decisions. Design a prospective clinical study that would quantify the rate at which a single core biopsy from the most accessible region of a solid tumor fails to identify the dominant driver mutation — defined as the mutation present in more than 50% of tumor cells — compared to multiregion sampling or surgical resection. Specify the tumor type, the number and locations of biopsy cores, the molecular testing approach, the reference standard, and the statistical threshold for "inadequacy." Then explain what the result would mean for clinical practice if the inadequacy rate turned out to be above 20% in the tumor type you studied — specifically, what changes in the diagnostic protocol would be justified and what changes would require additional evidence before implementation.
*What this tests: translating the spatial heterogeneity problem into a study design; reasoning about what level of diagnostic inadequacy would justify changing standard practice.*

---

## What Would Change My Mind

The central claim is that imaging is probabilistic and tissue, when correctly sampled, is the arbiter — so a negative biopsy must be weighed against pretest probability rather than accepted at face value. What would revise this: rigorous prospective evidence that a non-invasive modality — advanced quantitative MRI, molecular-imaging tracers, or AI-enhanced imaging — could distinguish malignant from benign tissue with positive and negative predictive values high enough to replace biopsy for a defined lesion type, validated against pathology as the reference standard. If imaging could deliver tissue-equivalent certainty for some cancers, the privileged status of the needle would erode for those cancers. So far, imaging informs the probability and tissue settles it — but this is an empirical claim about current technology, not a law of nature.

## Still Puzzling

- How heterogeneous is a tumor allowed to be before a single core biopsy is fundamentally inadequate? For some cancers, the region a needle hits may not carry the mutations that drive lethality. Where is the line, and how would we know we had crossed it? `[contested]`
- AI tools now read mammograms, lung CTs, and digital pathology slides. When an algorithm and a human radiologist disagree, whose probability should drive the biopsy decision — and how do we validate the algorithm against a ground truth that is itself a sampled, imperfect biopsy?
- For lesions that cannot be safely biopsied — some brain, some pancreatic, some lung — we are forced to treat on imaging probability alone. How should the threshold for treating-without-tissue be set, and who decides?

## References

- National Cancer Institute. *Cancer Imaging Basics.* https://dctd.cancer.gov/research/research-areas/imaging/basics
- National Cancer Institute. *Tests and Procedures Used to Diagnose Cancer.* https://www.cancer.gov/about-cancer/diagnosis-staging/diagnosis
- National Cancer Institute. *CT Scans and Cancer Fact Sheet.* https://www.cancer.gov/about-cancer/diagnosis-staging/ct-scans-fact-sheet
- Advances in Diffusion and Perfusion MRI for Quantitative Cancer Imaging. 2020. https://pmc.ncbi.nlm.nih.gov/articles/PMC7747414/
- Eisenhauer, E. A., et al. (2009). New response evaluation criteria in solid tumours: Revised RECIST guideline (version 1.1). *European Journal of Cancer*, 45(2), 228–247.
- National Cancer Institute. *Research Areas: Cancer Diagnosis.* https://www.cancer.gov/research/areas/diagnosis

---

## Prompts

### Figure 2.1 — The diagnostic chain and its failure modes
Build a left-to-right flowchart of five sequential stages: (1) Clinical suspicion, (2) Imaging, (3) Biopsy, (4) Pathology (ground truth), (5) Molecular workup. Connect them with right-pointing arrows in order. Render the middle anchor stages (1, 2, 3, 5) in sky-blue as process boxes and highlight stage 4, Pathology, in blue as the dominant ground-truth node so it reads as the privileged link. Below each fallible link, attach a small annotation of its failure mode in vermillion text: imaging — false positive/false negative; biopsy — sampling miss; pathology — ambiguous tissue. Add a caption strip: "Pathology is ground truth, conditional on sampling." Uniform box sizes, numbered, single horizontal track. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 2.2 — Three ways a needle returns a false negative
Build a three-panel annotated comparison (two columns, three rows). Left column header "Needle endpoint," right column header "Why it fails." Row 1: "Tip lands in stroma beside tumor" vs "Miss: tumor never sampled." Row 2: "Tip in necrotic / low-grade zone" vs "Unrepresentative: not viable tumor." Row 3: "Reaches tumor but tiny core" vs "Insufficient tissue for workup." Render every "why it fails" cell in vermillion to signal the failure; left cells neutral. Optionally add a small schematic icon per row (needle relative to a tumor blob) as an annotated callout. Add a bottom banner: "A negative biopsy is not a negative lesion." Equal row heights, clear column divider. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 2.3 — A negative biopsy cannot overturn high pretest odds
Build a two-bar vertical bar chart (before-after pair). X-axis: "Pretest" and "After negative biopsy," in that order. Y-axis: probability of malignancy in percent, zero baseline, 0–100. Bars: 80 and 39. Render both bars in vermillion to signal that malignancy probability remains clinically worrying in both states; highlight the "After negative biopsy" bar with a heavier outline as the key result. Direct-label each bar with its value. Add a horizontal reference line at a plausible "rule-out" threshold (e.g., 10%) annotated "below this you might stop looking," making visually clear that 39% sits far above it. Annotation: "imperfect sensitivity + high pretest = residual risk." Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.
