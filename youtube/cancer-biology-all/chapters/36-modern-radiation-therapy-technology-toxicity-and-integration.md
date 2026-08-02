# Chapter 36 — Modern Radiation Therapy: Technology, Toxicity, and Integration


## TL;DR

- A photon doesn't know what it's supposed to hit.
- The chapter moves through Intensity-modulated radiation therapy, Image-guided radiation therapy, Stereotactic body radiation therapy, Proton therapy, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

A photon doesn't know what it's supposed to hit. Modern radiation oncology has figured out how to point it.

Hold the framing. Radiation therapy works because it kills cancer cells. The challenge has always been that radiation also kills normal cells. The history of radiation oncology is the history of progressively better technology for delivering radiation to tumors while sparing the surrounding tissue. In 1950, the technology was crude — radiation delivered through simple rectangular fields with minimal sparing of normal organs. The cancers that could be treated were limited; the toxicities were substantial.

Modern radiation oncology in 2026 looks dramatically different. Intensity-modulated radiation therapy (IMRT) sculpts dose distributions to follow tumor shape while avoiding adjacent organs. Image-guided radiation therapy (IGRT) verifies tumor position before each fraction. Stereotactic body radiotherapy (SBRT) delivers very high doses with sub-millimeter accuracy. Proton therapy uses charged particles with characteristic dose deposition properties that reduce integral dose to normal tissue. Adaptive radiotherapy adjusts the plan during the treatment course as anatomy changes. The result is that cancers in difficult locations (close to spinal cord, near the optic nerves, deep in the pelvis) can now be treated with curative doses while keeping normal tissue toxicities manageable.

The technological progress has paralleled biological progress. We understand much better which tumors are radiosensitive, which patients benefit most, and how to combine radiation with chemotherapy, targeted therapy, and immunotherapy. The clinical applications continue to expand — radiation has roles in essentially every cancer at some point in management.

This chapter — the second on radiation oncology — covers the modern technologies (IMRT, IGRT, SBRT, proton therapy, brachytherapy techniques, adaptive radiotherapy), the management of radiation toxicities, and the integration of radiation with other treatment modalities. The chapter builds on the principles covered in 21A.

Hold the question: *how have technological advances allowed radiation to treat cancers that were once untreatable and to do so with fewer side effects?*

---

## Intensity-modulated radiation therapy

Intensity-modulated radiation therapy (IMRT) is the dominant modern external beam technique. The technology delivers radiation through multiple beams whose intensity varies across the beam profile, producing complex dose distributions that conform tightly to the target shape.

The physics: a multi-leaf collimator (MLC) — an array of metal leaves that can move independently to shape the radiation beam — modulates the beam intensity. By combining multiple beam directions, each with varying intensity profiles, IMRT achieves dose distributions that are much more conformal than older techniques.

The advantages of IMRT:
- *Conformality*. The dose distribution closely matches the target volume shape, sparing adjacent organs.
- *Dose escalation*. Higher tumor doses can be delivered while keeping organ doses within tolerance.
- *Concave dose distributions*. IMRT can produce dose distributions with concavities (e.g., around the spinal cord), impossible with older techniques.

Applications across cancer types:

*Head and neck cancer*. IMRT has been particularly transformative for head and neck cancer. The parotid glands (which produce most of the saliva) can be largely spared, dramatically reducing xerostomia (dry mouth) compared to older techniques. Hearing apparatus, swallowing structures, and skin can also be better preserved.

*Prostate cancer*. IMRT allows higher doses (78-80 Gy) than older techniques while maintaining low rectal and bladder doses. Dose escalation has improved oncologic outcomes.

*Lung cancer*. IMRT for locally advanced lung cancer (treated with concurrent chemoradiation) reduces dose to esophagus, heart, and lung tissue, improving tolerability.

*Brain tumors*. IMRT for primary brain tumors and brain metastases spares normal brain tissue, reducing neurocognitive toxicity.

*Gynecologic cancers*. IMRT for cervical, endometrial, and vulvar cancers reduces small bowel and bladder dose.

*Pediatric cancers*. IMRT in children reduces dose to normal tissues, which is particularly important given the long expected survival and the risks of secondary cancers and long-term effects.

IMRT planning is more complex than older techniques. The inverse planning process — specifying the desired dose distribution and using software optimization to generate the beam configuration — produces plans that are not intuitive geometrically. Quality assurance for IMRT requires careful verification.

*Volumetric modulated arc therapy (VMAT)* is a refinement of IMRT in which the beam continuously varies as the gantry rotates around the patient. The treatment is delivered more quickly than static IMRT (typically 2-3 minutes versus 5-15 minutes), with similar or slightly improved dose distributions. VMAT has largely replaced static IMRT in many practices.

---

## Image-guided radiation therapy

Image-guided radiation therapy (IGRT) verifies tumor position before each treatment fraction. The technique addresses two sources of geometric uncertainty:

*Interfraction motion*. Tumor position differs from day to day. Bowel filling, bladder filling, weight changes, and patient positioning produce variability.

*Intrafraction motion*. Tumor position changes during a single treatment fraction. Breathing motion is the major source for thoracic and upper abdominal tumors. Bladder filling affects pelvic tumors.

IGRT techniques:

*Cone-beam CT (CBCT)*. A CT scan acquired in treatment position immediately before treatment delivery. Provides three-dimensional verification of tumor position. The most common IGRT modality.

*Orthogonal kV images*. Two perpendicular X-ray images of bony anatomy. Faster than CBCT but provides only bony anatomy reference, not soft tissue.

*Fiducial markers*. Implanted radiopaque markers (typically gold) provide reference points for daily setup. Used commonly for prostate cancer and emerging for other sites.

*MR-guided radiation therapy (MRgRT)*. Real-time MR imaging during radiation delivery. The MR-Linac systems (ViewRay MRIdian, Elekta Unity) combine an MR scanner with a linear accelerator. The technology provides excellent soft tissue visualization without ionizing imaging dose. The treatment can be gated to anatomy (delivering radiation only when the tumor is in position) or adapted to daily anatomy.

*Respiratory motion management*. For tumors that move with breathing (lung, liver, pancreas), techniques include:
- *Breath-hold techniques*. The patient holds breath during treatment delivery, reducing motion.
- *Gating*. Treatment is delivered only during specific phases of the respiratory cycle.
- *Tracking*. The radiation beam follows the tumor as it moves.
- *4D CT planning*. Four-dimensional CT acquired during a respiratory cycle, used for planning the dose distribution accounting for motion.

IGRT has reduced the margin required around target volumes for setup uncertainty, allowing more conformal treatment and reduced normal tissue dose.

---

## Stereotactic body radiation therapy

Stereotactic body radiation therapy (SBRT, also called stereotactic ablative radiotherapy or SABR) delivers very high doses in few fractions to small targets with extreme precision. The approach extends the principles of stereotactic radiosurgery (SRS) for brain tumors to extracranial sites.

The defining features:
- *High biological dose*. Total doses delivered in 1-5 fractions, with each fraction typically 7-25 Gy. The biological dose substantially exceeds conventional fractionation.
- *Sub-millimeter accuracy*. Image guidance and immobilization ensure precise targeting.
- *Steep dose gradients*. Dose falls off rapidly outside the target, sparing surrounding tissues.
- *Multiple beam angles*. Often using arc-based delivery (VMAT-SBRT) for optimal conformality.

Clinical applications:

*Early-stage non-small-cell lung cancer*. SBRT for medically inoperable patients (and increasingly for operable patients in some studies) with stage I lung cancer. Doses of 50-60 Gy in 3-5 fractions. Local control rates around 90 percent at 3 years. Comparable outcomes to surgery in some studies (though direct comparison remains active research). Has transformed the management of inoperable early-stage lung cancer.

*Liver metastases and hepatocellular carcinoma*. SBRT for selected patients not suitable for resection or ablation. Doses depending on liver function and size.

*Prostate cancer*. Hypofractionated SBRT (typically 5 fractions of 7.25 Gy) as an alternative to conventional fractionation. Equivalent or improved outcomes in trials. Substantial convenience advantage (5 visits versus 30-40 visits).

*Spinal metastases*. SBRT delivers high doses to vertebral metastases for pain relief and local control while sparing the spinal cord. Particularly valuable for radioresistant tumors (renal cell carcinoma metastases).

*Oligometastatic disease*. SBRT to limited metastatic deposits across various cancers. The SABR-COMET trial showed survival benefit from SBRT to 1-5 metastatic lesions in selected patients. The concept of "ablative therapy for oligometastatic disease" continues to expand.

*Reirradiation*. SBRT can deliver curative-intent treatment to areas previously irradiated, leveraging the rapid dose falloff to spare normal tissues that have already received radiation.

*Brain metastases*. Stereotactic radiosurgery (SRS) for limited brain metastases is well-established and increasingly preferred over whole-brain radiation (which has greater neurocognitive toxicity) for selected patients.

SBRT requires substantial infrastructure: precise immobilization, image guidance, motion management for moving targets, sophisticated planning software, and rigorous quality assurance. The technique has rapidly become standard at major centers and is expanding to community practices.

---

## Proton therapy

Proton therapy uses charged particles (protons) instead of photons. The physics is different in ways that have therapeutic implications.

The key property is the *Bragg peak*. Protons deposit energy gradually as they pass through tissue, then deposit a sharp peak of dose at the end of their range, then deposit essentially zero dose beyond. This contrasts with photons, which deposit dose maximally near the entry point and gradually decrease through tissue and beyond.

The clinical implication: proton therapy can deliver high doses to tumors at depth without depositing exit dose distal to the target. The integral dose to non-tumor tissue is reduced compared to photon therapy.

Applications where proton therapy provides advantages:

*Pediatric cancers*. The reduced integral dose to normal tissues is particularly valuable for children, who have decades of life ahead during which radiation-induced secondary cancers could develop. Brain tumors, sarcomas, and other pediatric cancers are increasingly treated with protons.

*Skull base and head and neck cancers* in difficult locations. Tumors adjacent to optic nerves, brainstem, and other critical structures benefit from the steep dose falloff.

*Chordomas and chondrosarcomas*. These radioresistant tumors near the spine and skull base benefit from the high doses possible with protons.

*Some prostate cancers*. The dose reduction to rectum and bladder may reduce late toxicities, though randomized trial evidence has been mixed.

*Reirradiation cases* where the integral dose reduction is valuable.

The limitations of proton therapy:
- *Cost*. Proton centers cost hundreds of millions of dollars to build. The treatments are 2-3 times more expensive than photon therapy.
- *Range uncertainty*. The exact stopping point of protons is somewhat uncertain due to tissue heterogeneity, motion, and other factors. This requires careful planning margins.
- *Less clinical data*. Proton therapy has been used for fewer cancers and shorter durations than photon therapy, so the comparative effectiveness data are more limited.

The growth of proton therapy has been substantial, with dozens of centers in operation worldwide. The cost-effectiveness debate continues; for clearly advantageous applications (pediatric cancer, specific anatomic locations), the cost is justified. For others (most prostate cancer, most lung cancer), photon therapy with IMRT/SBRT may achieve similar outcomes at lower cost.

*Carbon ion therapy* (heavy ion therapy) is an even more advanced approach using carbon ions with both Bragg peak properties and higher relative biological effectiveness. Available at limited centers (mostly in Japan and Europe), it is reserved for selected radioresistant tumors.

---

## Brachytherapy

Brachytherapy places radioactive sources directly in or adjacent to a tumor. The approach delivers very high doses to the tumor with rapid dose falloff to surrounding tissues — the inverse square law produces dramatic dose reduction with distance.

Types of brachytherapy:

*Interstitial brachytherapy*. Sources placed within the tumor tissue. Common for prostate cancer (transperineal placement of iodine-125 or palladium-103 seeds for low-dose-rate; iridium-192 catheters for high-dose-rate). Also used for breast cancer (accelerated partial breast irradiation), head and neck cancers, and others.

*Intracavitary brachytherapy*. Sources placed within natural body cavities. Standard for cervical cancer (intrauterine and vaginal applicators with iridium-192 sources). Also used for endometrial cancer, bronchial cancer (endobronchial brachytherapy), and others.

*Surface brachytherapy*. Sources placed on the skin surface. For skin cancers.

*Permanent versus temporary*. Permanent implants (prostate seeds) deliver dose over the half-life of the isotope and stay in place. Temporary implants (HDR brachytherapy) deliver dose during the procedure and are then removed.

*Low-dose-rate versus high-dose-rate*. LDR delivers dose continuously at slow rates over hours to days. HDR delivers dose in brief fractions over minutes per session, with multiple sessions over days to weeks.

Brachytherapy advantages:
- *Very conformal dose*. The dose falls off rapidly with distance from the source.
- *Higher biological dose*. The continuous dose delivery in LDR or large doses per fraction in HDR provide significant biological dose.
- *Less geometric uncertainty*. The source is placed directly at the target, eliminating much setup uncertainty.

Brachytherapy challenges:
- *Procedural complexity*. Placing sources requires specialized expertise and equipment.
- *Anesthesia requirements*. Most brachytherapy requires sedation or general anesthesia.
- *Workforce limitations*. The procedural skills are decreasing as fewer trainees learn brachytherapy.

Brachytherapy has been progressively replaced by external beam techniques (SBRT, IMRT) in many indications, but remains standard for cervical cancer and is valuable in selected other settings.

---

## Adaptive radiotherapy

Tumor anatomy and patient anatomy change during a treatment course. *Adaptive radiotherapy* adjusts the treatment plan to account for these changes.

Reasons for replanning:
- *Tumor response*. Tumors may shrink during treatment. The original plan, designed for the initial tumor size, may now deliver excessive dose to surrounding normal tissue.
- *Weight loss*. Patients with head and neck cancer or other treatment areas may lose weight, changing external anatomy.
- *Bladder/bowel filling changes*. For pelvic radiation, daily filling variability affects target and organ positions.
- *Tumor growth or progression* (rare but possible during treatment).

Adaptive approaches:
- *Offline adaptation*. Periodic plan revisions based on imaging during treatment. A new CT is acquired, the plan is regenerated, and subsequent fractions use the updated plan.
- *Online adaptation*. Plan adjustments based on imaging immediately before each fraction. The MR-Linac systems enable this by combining MR imaging with linac delivery, allowing the plan to be optimized to the day's anatomy before treatment.
- *Real-time adaptation*. Adjustments during the fraction based on imaging during treatment. Emerging with MR-Linac systems and tracking technology.

Adaptive radiotherapy improves dose distribution accuracy throughout the treatment course, allowing more aggressive treatment of moving or changing targets with reduced toxicity. The technology is rapidly developing and expanding.

---

## Radiation toxicity management

All radiation has side effects. The toxicities depend on the dose, fractionation, volume, anatomic site, patient factors, and concurrent therapies.

*Acute toxicities* occur during or shortly after radiation. Examples:
- *Skin*. Erythema, desquamation, ulceration in the radiation field.
- *Mucosal*. Mucositis in head and neck radiation, esophagitis in chest radiation, proctitis in pelvic radiation.
- *Hematologic*. Cytopenias if substantial bone marrow is in the field.
- *Fatigue*. Common across all radiation treatments.
- *Site-specific*. Pneumonitis (lung radiation), nausea (abdominal radiation), neurologic symptoms (brain radiation).

Management of acute toxicities:
- *Skin care*. Moisturizers, gentle cleansing, avoidance of irritants.
- *Mucositis*. Oral hygiene, pain control, nutritional support, sometimes feeding tube placement.
- *Antiemetics* for nausea.
- *Hydration and electrolyte management*.
- *Treatment breaks* for severe toxicity (with awareness that breaks may compromise oncologic outcome).

*Late toxicities* occur months to years after radiation. The biology of late effects is different from acute effects — different cell populations affected, different repair mechanisms involved. Late toxicities are often more disabling than acute ones.

Examples:
- *Fibrosis*. Lung fibrosis after thoracic radiation, soft tissue fibrosis after radiation to extremities, breast fibrosis after breast radiation.
- *Xerostomia*. Dry mouth after head and neck radiation.
- *Hypothyroidism*. After neck or upper chest radiation.
- *Secondary malignancies*. Most concerning in young patients. Risk is small but real (1-5% absolute risk over decades, depending on radiation dose, age, and other factors).
- *Cardiovascular effects*. Coronary artery disease after thoracic/mediastinal radiation.
- *Neurologic*. Cognitive decline after brain radiation, especially whole-brain radiation. Lhermitte's sign (cervical spinal cord symptom) is generally self-limited.
- *Erectile dysfunction and incontinence*. After prostate radiation.

Prevention of late toxicities is the main strategy. Modern conformal techniques (IMRT, IGRT, SBRT, proton therapy) reduce the dose to normal tissues and the risk of late effects. Specific organ-sparing techniques (parotid sparing in head and neck cancer, cardiac sparing in left breast irradiation, hippocampal sparing in whole-brain radiation) reduce specific late effects.

Treatment of established late effects is often supportive. Hyperbaric oxygen for tissue necrosis. Pentoxifylline and tocopherol for fibrosis. Saliva substitutes for xerostomia. Hormone replacement for hypothyroidism. Aggressive cardiovascular risk management after thoracic radiation. Cognitive rehabilitation after brain radiation.

---

## Combining radiation with systemic therapy

Modern oncology often combines radiation with systemic therapy. The combinations can be synergistic, additive, or competing depending on the agents and the cancer.

*Concurrent chemoradiation*. Chemotherapy given simultaneously with radiation. Standard for many cancers:
- *Head and neck cancer*. Concurrent platinum-based chemotherapy with radiation.
- *Locally advanced lung cancer*. Concurrent platinum-based chemotherapy with radiation.
- *Cervical cancer*. Concurrent cisplatin with radiation.
- *Rectal cancer*. Concurrent fluoropyrimidine with radiation.
- *Glioblastoma*. Concurrent temozolomide with radiation.
- *Anal cancer*. Mitomycin and 5-FU with radiation (curative without surgery for most cases).

The chemotherapy serves as a radiosensitizer and addresses microscopic systemic disease. The toxicity is increased compared to either modality alone.

*Sequential chemotherapy and radiation*. Chemotherapy followed by radiation, or vice versa. Used when concurrent approach is too toxic or when sequencing is otherwise optimal.

*Radiation combined with targeted therapy*. Specific examples:
- *Cetuximab + radiation* in head and neck cancer (alternative to chemoradiation in some patients).
- *Bevacizumab + radiation* (concerns about increased toxicity have limited use).
- *BRAF inhibitors + radiation* for melanoma (timing requires careful consideration due to skin toxicity).

*Radiation combined with immunotherapy*. A rapidly expanding area:
- *Concurrent or sequential immune checkpoint inhibitor + radiation*. Multiple trials in lung cancer, melanoma, head and neck cancer. The PACIFIC trial established consolidation durvalumab after concurrent chemoradiation for locally advanced lung cancer, with substantial survival benefit.
- *Abscopal effect*. Radiation to one lesion sometimes produces immune responses that cause regression of distant lesions. The phenomenon has been hard to harness reliably but is being studied as a way to integrate radiation with immunotherapy.
- *Combinations being explored*. SBRT + checkpoint inhibitors for oligometastatic disease. Localized radiation + immunotherapy as primary treatment for some cancers.

The biology of radiation-immune interactions is complex. Radiation can:
- Release tumor antigens through cell death, potentially priming immune responses.
- Cause immunogenic cell death with specific molecular features.
- Modulate the tumor microenvironment (vasculature, immune infiltration).
- Activate innate immunity through DNA damage signaling.
- Also have immunosuppressive effects (lymphocyte depletion if lymphoid tissue in field).

The combinations are an active area of clinical trial development. The optimal sequencing, dose, fractionation, and target volumes for radiation-immunotherapy combinations are being defined.

---

## Specific clinical contexts

A few specific applications of radiation oncology deserve mention:

*Whole-brain radiation versus stereotactic radiosurgery for brain metastases*. The choice depends on number and location of metastases, primary disease control, patient prognosis. SRS is increasingly preferred for limited metastases (≤5 lesions in many guidelines, ≤10-15 in some recent studies) to avoid neurocognitive effects of WBRT.

*Hippocampal-sparing whole-brain radiation*. When WBRT is needed (extensive brain metastases, leptomeningeal disease), sparing the hippocampi reduces memory and cognitive effects.

*Radiation for spine metastases*. Conventional fractionation versus SBRT depends on indication. SBRT preferred for limited metastases with histology that suggests radioresistance, or in salvage settings.

*Total body irradiation*. For hematopoietic stem cell transplant conditioning. Different doses for different conditioning regimens.

*Radium-223 for prostate cancer bone metastases*. An alpha-emitting radiopharmaceutical that accumulates in bone, providing palliation and some survival benefit.

*Lutetium-177-PSMA for prostate cancer*. Theranostic approach combining PSMA imaging with PSMA-targeted radiation delivery. Approved 2022.

*Lutetium-177-DOTATATE for neuroendocrine tumors*. Somatostatin receptor-targeted radiation.

These examples illustrate the breadth of modern radiation oncology applications and the integration of radiation with molecular targeting.

---

## What this chapter gives you

Modern radiation therapy uses sophisticated technologies (IMRT, IGRT, SBRT, proton therapy, brachytherapy, adaptive radiotherapy) to deliver radiation with sub-millimeter precision and steep dose gradients. The technologies have transformed the safety and effectiveness of radiation therapy across cancer types.

Intensity-modulated radiation therapy (IMRT) shapes dose distributions to conform to tumor shape while sparing organs at risk. Image-guided radiation therapy (IGRT) verifies tumor position before each fraction. Stereotactic body radiation therapy (SBRT) delivers very high doses in few fractions to small targets with extreme precision, transforming the management of early-stage cancers, oligometastatic disease, and reirradiation.

Proton therapy uses charged particles with characteristic Bragg peak dose deposition, reducing integral dose to normal tissues. The technology is particularly valuable for pediatric cancers and tumors in challenging anatomic locations. Cost is a major consideration.

Brachytherapy places radioactive sources directly in or adjacent to tumors, providing very conformal dose with rapid falloff. Standard for cervical cancer and selected other applications.

Adaptive radiotherapy adjusts treatment plans during the course as tumor and patient anatomy change. Online adaptation using MR-Linac systems enables daily plan optimization.

Radiation toxicities include acute effects (skin, mucosal, hematologic, fatigue, site-specific) and late effects (fibrosis, xerostomia, hypothyroidism, secondary malignancies, cardiovascular effects, neurologic effects). Prevention through conformal techniques is the main strategy; treatment is largely supportive.

Combinations of radiation with chemotherapy (concurrent chemoradiation for many cancers), targeted therapy, and immunotherapy are central to modern cancer treatment. Radiation-immunotherapy combinations are a particularly active area, with concepts like the abscopal effect and emerging data from trials like PACIFIC informing practice.

This concludes Chapter 21 and the cancer therapy modalities. Chapter 22 turns to specific cancer types and their management, applying the principles covered in chapters 17-21 to specific clinical contexts.

---

## LLM exercises

1. Ask your LLM to compare intensity-modulated radiation therapy (IMRT) with three-dimensional conformal radiation therapy (3D-CRT). What does each technique allow, what is the technological complexity, and what is the clinical evidence for IMRT improving outcomes? Identify the cancers where IMRT provides the most meaningful clinical benefit.

2. Have your LLM walk through the SABR-COMET trial of stereotactic body radiotherapy for oligometastatic disease. What was the trial design, what were the results, and what does it suggest about the role of radiation in metastatic disease? Identify the patient selection factors that determine response to SBRT for oligometastatic disease.

3. Use your LLM to assess the comparative effectiveness of proton therapy versus IMRT photon therapy for prostate cancer. What is the physics rationale for protons, what does the clinical evidence show, and how does cost-effectiveness compare? Identify which patients are most likely to benefit from proton over photon therapy.

4. Ask your LLM to walk through the PACIFIC trial of consolidation durvalumab after concurrent chemoradiation for locally advanced non-small-cell lung cancer. What was the trial design, what were the survival outcomes, and how has it changed practice? Identify the biological rationale for combining immunotherapy with radiation.

5. Have your LLM explain the abscopal effect in radiation oncology. What is the underlying biology, what are the historical and modern reports, and what current approaches are being studied to harness this phenomenon for clinical benefit? Identify the most promising trial design to demonstrate consistent abscopal effect.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Cornelius Tobias** at the Lawrence Berkeley National Lab pioneered heavy-ion radiotherapy in the 1950s — using particle accelerators to deliver radiation with sharper depth control than X-rays. His work is the ancestor of modern proton and carbon-ion therapy.

**Run this:**

```
Who was Cornelius Tobias, and how does his work on heavy-ion radiotherapy connect to the modern radiation therapy technologies we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Cornelius A. Tobias"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to explain why proton beams deposit most of their energy at a sharp depth (the Bragg peak) — and how that helps spare healthy tissue.
- Ask it to compare the clinical evidence for proton therapy with conventional photon therapy — when is each justified?

What changes? What gets better? What gets worse?
