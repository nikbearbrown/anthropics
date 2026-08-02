# Chapter 7 — Radioligand Theranostics

A man with metastatic, castration-resistant prostate cancer has exhausted standard options. His oncologist knows that lutetium-177-PSMA-617 extends survival in this setting and wants to give it. The temptation is to treat on the basis of the diagnosis alone — it is prostate cancer, the drug is for prostate cancer, give it.

But the team first performs a PSMA PET scan, imaging the same target the therapy will exploit. On most patients this lights up bright: the metastases express prostate-specific membrane antigen abundantly, and those patients are good candidates. On this patient, several large, symptomatic lesions show almost no PSMA signal. They have dedifferentiated and lost the target. Had the team treated on diagnosis alone, they would have irradiated his salivary glands and kidneys — which do express PSMA — while the lesions causing his symptoms received little therapeutic radiation. The drug would have delivered toxicity without benefit to exactly the tumors that mattered.

The PSMA scan is not a formality before treatment; it is the patient-selection step. And it works because the imaging agent and the therapeutic agent target the same molecule. This chapter is about that design — the cleanest, most clinically successful idea in the field — and about why "the target is on the image" is necessary but not the whole story.

---

## What theranostics means

**Theranostics** combines therapy and diagnostics in a single molecular framework. The molecule used for imaging is the same molecule — or a matched sister molecule — used for therapy. The same molecular event, target binding, drives both diagnosis and treatment. You image to confirm the target is present; you treat by delivering a therapeutic payload through that same target; you image again after treatment to confirm delivery and predict response.

Conventional oncology separates imaging and therapy. A patient is staged with one agent and treated with an unrelated drug, and information flows one direction: the image informs the treatment decision, but the treatment is not mechanistically connected to the imaging target. In theranostics the loop closes. The imaging step becomes a genuine companion diagnostic for that specific therapy, not a generic staging procedure.

The cleanest realization is **radioligand therapy**: a small targeting molecule — the ligand — carries a radioisotope. Swap the imaging isotope for a therapeutic isotope on the same ligand and you have a matched diagnostic/therapeutic pair. The patient selection step (imaging) and the treatment step (therapy) are built from the same molecular event.

![Closed five-step image-then-treat cycle in which one molecular target carries two isotopes](images/07-radioligand-theranostics-fig-01.png)
*Figure 7.1 — Image-then-treat theranostic loop*

<!-- → [DIAGRAM: radioligand theranostic image-then-treat loop. A circular flow: (1) inject diagnostic radioligand (e.g., Ga-68-PSMA-11) → (2) PET scan confirms target expression → (3) if positive, inject therapeutic radioligand (same ligand, e.g., Lu-177-PSMA-617) → (4) the emitted radiation kills bound cells + crossfire → (5) post-therapy imaging confirms delivery → loop back to assess response. Center label: SAME TARGET, two isotopes.] -->

---

## The PSMA pair

Prostate-specific membrane antigen is a transmembrane protein expressed at high levels on prostate cancer cells. Expression correlates with disease aggressiveness and is detectable on nearly all metastatic prostate cancer. The protein also happens to be expressed on salivary glands and renal tubules — normal tissues that will become the dose-limiting organs.

The imaging side of the pair uses small molecules that bind PSMA's active site, labeled with PET isotopes. **Gallium-68-PSMA-11** and **fluorine-18-DCFPyL (piflufolastat)** are both FDA-approved for prostate cancer staging and restaging. PSMA PET is dramatically more sensitive than conventional imaging — CT and bone scan — for recurrence and metastasis, particularly at low PSA values where conventional imaging shows nothing. This sensitivity matters not just for staging but for patient selection: a clear signal is what licenses proceeding to therapy.

The therapy side uses the same targeting molecule loaded with **lutetium-177**, a beta-emitting radioisotope. **Lutetium-177-PSMA-617 (Pluvicto)** was approved by the FDA in 2022 for PSMA-positive metastatic castration-resistant prostate cancer that has progressed on a taxane and an androgen receptor pathway inhibitor. The pivotal VISION trial showed improved overall survival when the drug was added to best supportive care in this heavily pretreated population.

Because imaging and therapy share the targeting molecule, the PSMA PET scan is integrated into the therapy as a mandatory companion diagnostic. This is not regulatory caution or institutional process — it is mechanistic. The scan asks the question the therapy requires an answer to: does this patient's tumor express the target? If the answer is no, the therapy will not work on the tumor. If the answer is yes, the therapy can be delivered through the same molecular handle that just produced the image.

The second established pair follows the same logic in a different cancer. **Lutetium-177-DOTATATE (Lutathera)** targets somatostatin receptor type 2, which is overexpressed on gastroenteropancreatic neuroendocrine tumors. The imaging companion, **gallium-68-DOTATATE PET**, images the same receptor. DOTATATE was the first FDA-approved radioligand theranostic in the modern era, approved in 2018, and established the regulatory pathway that PSMA-617 followed. The shared structure — same target, two isotopes, imaging before therapy — is identical.

---

## Beta emitters and alpha emitters

The therapeutic isotope is not a fixed choice. Two classes of emitting particles are in clinical use or advanced development, and they differ in ways that determine which tumor geometry each serves.

**Beta emitters** release electrons. Lutetium-177 is the most clinically used; yttrium-90 has higher energy and longer range; iodine-131 is the classic thyroid isotope. The key physical property is range: beta particles travel **several millimeters** through tissue before depositing their energy. This long range produces **crossfire** — a cell that does not express the target can still be killed by radiation originating from a neighboring cell that has bound the radioligand. Crossfire is directly useful in tumors with heterogeneous target expression: even if the ligand does not bind every cell, the radiation from cells it does bind can reach the ones it does not. The cost of the long range is lower **linear energy transfer** — beta particles deposit their energy sparsely along their path, producing radiation damage that cells can sometimes repair, and the longer range also irradiates adjacent normal tissue.

**Alpha emitters** release helium nuclei — two protons and two neutrons. Actinium-225 is the leading clinical candidate; radium-223 is already approved for prostate cancer bone metastases. The key physical property is again range: alpha particles travel only **50 to 100 micrometers** — a few cell diameters. But in that short distance they deposit enormously more energy per unit length than a beta particle. This very high linear energy transfer produces dense, clustered DNA double-strand breaks that are far harder for the cell to repair. High-LET radiation can kill cells that have developed resistance to the sparser damage of low-LET beta radiation. The cost is the same property that gives it precision: the 50 to 100 micrometer range means an alpha particle bound to one cell cannot reach cells more than a few widths away. There is very little crossfire. For heterogeneous tumors with PSMA-negative cores, an alpha emitter would sterilize the PSMA-positive rim and leave the negative interior untouched.

![Side-by-side comparison of long sparse beta crossfire versus short dense alpha kill](images/07-radioligand-theranostics-fig-02.png)
*Figure 7.2 — β vs α emitter range and LET*

<!-- → [DIAGRAM: beta vs alpha emitter comparison. Left: a beta-emitter (Lu-177) on a tumor cell, electron track ~mm crossing several cells including a target-negative one (crossfire kills it); label "low LET, long range, crossfire helps heterogeneity." Right: an alpha-emitter (Ac-225) on a tumor cell, dense short track ~50-100 µm causing clustered double-strand breaks in 1-2 cells; label "high LET, short range, more lethal, less crossfire." Scale bar in micrometers.] -->

The practical consequence is that emitter choice should be matched to tumor geometry. Micrometastatic disease or uniformly target-positive tumors favor alpha emitters: every tumor cell is a few widths from a bound radioligand, the high LET maximizes killing, and the short range minimizes off-target damage. Bulky, heterogeneous tumors with target-negative regions favor beta emitters: the millimeter crossfire reaches cells the ligand does not bind. The question is never "which isotope is stronger" — it is "which range matches the spatial distribution of the target in this patient's tumor."

---

## Off-target uptake sets the dose limit

PSMA is expressed not only on prostate cancer cells but on salivary glands and renal tubules. The radioligand binds wherever the target is present. This means that regardless of how clearly the tumor lights up on PET, the delivered dose is shared between tumor and normal organs, and the tolerances of the normal organs cap how much isotope can be given.

The predictable toxicities of lutetium-177-PSMA-617 follow directly from this anatomy: **xerostomia** (dry mouth) from salivary gland uptake, **kidney toxicity** from renal tubule uptake, and bone marrow suppression. You cannot simply give more isotope to deliver a higher tumor dose; more isotope also increases the salivary and renal dose, and those organs have tolerance limits that are crossed before the tumor dose reaches what might be needed to overcome resistance.

This is the absorbed-dose logic in practice. **Absorbed dose** — energy deposited per unit mass of tissue, measured in gray — is the quantity that connects radioactivity to biological effect. The therapeutic goal is to deliver a lethal absorbed dose to target-expressing cells. The constraint is keeping the absorbed dose to salivary glands, kidneys, and bone marrow below their tolerances. The gap between the two — how much dose can reach the tumor before normal-organ toxicity limits further dosing — is the therapeutic window, and it is narrower than the simplest version of the theranostic story suggests.

This is also exactly why the opening-case patient with PSMA-negative metastases would have been harmed rather than helped. His symptomatic lesions would have received little radioligand, because the ligand has nothing to bind there. His salivary glands and kidneys would have received their full dose, because PSMA is expressed there regardless of what has happened to his tumor. The dose-limiting organs would have been irradiated; the target-negative tumors would have been largely spared. The imaging step that identified PSMA-negative lesions was not a preliminary — it was the step that prevented a harmful treatment.

---

## Why this works when multifunctional nanoparticles mostly do not

Throughout the previous chapters, engineered nanoparticles with multiple functions — targeting ligands, drug payloads, imaging labels, release triggers — have appeared promising in cell culture and animal models but have largely failed to translate to clinical benefit. Radioligand theranostics is different. Several approved therapies, clinical benefit demonstrated in randomized trials, a clear mechanism linking imaging to therapy. Why?

The answer is in the simplicity of the design, not its sophistication. A radioligand is a small molecule — typically a few hundred to a few thousand daltons — carrying an isotope. It has no nanoparticle-scale architecture to characterize, no protein corona to worry about, and no dose-loss chain of the kind described in Chapter 1. It circulates, binds its target wherever the target is expressed, and emits. The targeting is chemical and direct. The imaging uses the same chemistry to confirm the target is present before delivering the therapy.

The design succeeds because it is mechanistically parsimonious: one target, one binding event, two isotopes. Every multifunctional nanoparticle that has failed has failed somewhere in the chain between injection and intracellular payload release. Radioligands skip most of that chain. They are not an alternative to nanoparticles for delivery of complex payloads — they cannot carry a chemotherapy in the way a liposome can — but for targets that are accessible to a small molecule and that can be imaged with a PET tracer, the simpler design translates where the more sophisticated one has not.

---

## What would change this picture

The chapter's central claim is that radioligand theranostics succeeds because its companion-diagnostic loop is built from a shared targeting molecule — making patient selection mechanistic rather than statistical — and that emitter choice must be matched to tumor geometry. Two findings would force revision.

If rigorous data showed that treating PSMA-PET-negative or low-expressing patients with lutetium-177-PSMA-617 produced survival benefit comparable to PSMA-positive patients, the claim that the shared-target selection step is the engine of success would be weakened. The imaging would be confirmed as a staging step rather than a companion diagnostic.

If controlled comparisons showed alpha emitters outperforming beta emitters even in demonstrably heterogeneous bulky tumors — where crossfire physics should favor beta — the geometry-matching argument would need revision. Perhaps high-LET killing advantage overrides range limitation in ways the current model does not capture.

Both questions are under active investigation, and the current evidence supports the claims as stated.

---

## Still open

How precisely absorbed dose can be measured per lesion, in real time, in a patient — rather than estimated from post-therapy scintigraphy — is an open technical problem. Per-lesion dosimetry that could individualize the number of treatment cycles and the activity per cycle would improve both efficacy and toxicity management, but it is not yet routine.

The actinium-225 supply chain is a genuine constraint on alpha-emitter development. The isotope is produced in limited quantities and its availability may not scale to meet demand as alpha-emitter therapies multiply through clinical trials. Whether this is solved by new production methods or whether it limits the field is unresolved.

How low PSMA expression can fall and still predict therapeutic benefit is not crisply defined. The PSMA PET scan gives an image, but the minimum uptake that licenses treatment — the analog of HER2-low thresholds in antibody-drug conjugate therapy — is not established. Patients who are faintly positive and treated at the margin of eligibility may have different outcomes than those who are strongly positive, and the current approval criteria may not capture this gradient.

---

## LLM Exercises

1. **(Image-then-treat loop)** Draw the theranostic loop for the PSMA pair as a labeled sequence of steps, naming the specific imaging agents, the therapeutic agent, and the shared target. At each step, state the decision the step informs and what a negative result at that step implies for proceeding.

2. **(DOTATATE analog)** A patient with a gastroenteropancreatic neuroendocrine tumor is being considered for lutetium-177-DOTATATE. Name the companion imaging agent, the receptor targeted, and what a negative scan implies about treating on diagnosis alone. Explain how this case maps onto the PSMA logic and where it differs.

3. **(Emitter geometry)** Two patients with metastatic castration-resistant prostate cancer are PSMA-positive on imaging. Patient A has widespread micrometastatic disease with uniformly bright PSMA signal. Patient B has a few bulky lesions with bright rims and cold centers on PET. For each patient, recommend beta or alpha emitter therapy, justify the recommendation in terms of range, LET, and crossfire, and explain why the intuition "alpha is stronger, use alpha" gives the wrong answer for one of them.

4. **(Absorbed dose budget)** Construct an absorbed-dose budget for lutetium-177-PSMA-617 listing at least four tissues that take up the radioligand — tumor and three normal organs. For each, state whether the absorbed dose is the therapeutic goal or a dose-limiting constraint. Write one sentence describing how the salivary and renal tolerance caps the deliverable tumor dose, and predict how the budget would change if an alpha emitter with 50-micrometer range replaced the beta emitter.

5. **(Claims evaluation)** A company claims its new radioligand "guarantees tumor-selective killing because the PET scan proves the target is there." Identify three specific ways this claim overstates what the imaging result demonstrates, drawing on off-target uptake, absorbed dose limits, and the relationship between LET and resistance. For each, state the additional measurement or criterion that would be needed to support the claim.

---

## Prompts

### Figure 7.1 — Image-then-treat theranostic loop
Build a closed-loop cycle diagram showing five ordered stages connected by arrows returning to the start: (1) inject diagnostic radioligand Ga-68-PSMA-11, (2) PET scan shows bright tumor foci, (3) target-positive decision branch, (4) inject therapeutic radioligand Lu-177-PSMA-617, (5) post-therapy image confirms delivery, looping back. Arrange the five nodes evenly around a circle, arrows running clockwise, with a central label "ONE TARGET — TWO ISOTOPES." Use Okabe-Ito semantics: anchor stages (diagnostic inject, PET scan) in sky-blue, the decision branch in a neutral/transitional gray, the two therapeutic stages in green (active/positive). Each node a rounded rectangle with concise wrapped text; arrowheads clearly directional. No data scale or axes. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 7.2 — β vs α emitter range and LET
Build a two-panel comparison: left panel "β (Lu-177)," right panel "α (Ac-225)," sharing a common axis label "Track range and energy density." Lay out four aligned rows comparing the two emitters: (1) range several millimeters vs 50-100 micrometers, (2) low vs high linear energy transfer, (3) sparse track crosses many cells vs dense track confined to 1-2 cells, (4) crossfire kills target-negative cells vs minimal crossfire. Render each side as a labeled cell or bar; align rows horizontally so the contrast reads left-to-right per attribute. Use Okabe-Ito: emphasize the dominant LET row (blue), mark the beta-crossfire benefit in green (positive). Include a small micrometer/millimeter scale cue distinguishing track lengths. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

---

## References

- NCI. *CT Scans and Cancer Fact Sheet.* https://www.cancer.gov/about-cancer/diagnosis-staging/ct-scans-fact-sheet
- NCI. *Theranostics and AI in Cancer Precision Medicine.* https://www.cancer.gov/about-nci/organization/cbiit/news-events/blog/2023/theranostics-and-ai-next-advance-cancer-precision-medicine
- Sartor, O., et al. (2021). Lutetium-177–PSMA-617 for Metastatic Castration-Resistant Prostate Cancer. *New England Journal of Medicine*, 385(12), 1091–1103. [VISION trial]
- Strosberg, J., et al. (2017). Phase 3 Trial of 177Lu-Dotatate for Midgut Neuroendocrine Tumors. *New England Journal of Medicine*, 376(2), 125–135. [NETTER-1 trial]
- Baum, R. P., & Kulkarni, H. R. (2012). THERANOSTICS: From Molecular Imaging Using Ga-68 Labeled Tracers and PET/CT to Personalized Radionuclide Therapy. *Theranostics*, 2(5), 437–447.
- Sgouros, G., Bodei, L., McDevitt, M. R., & Nedrow, J. R. (2020). Radiopharmaceutical therapy in cancer: clinical advances and challenges. *Nature Reviews Drug Discovery*, 19(9), 589–608.
