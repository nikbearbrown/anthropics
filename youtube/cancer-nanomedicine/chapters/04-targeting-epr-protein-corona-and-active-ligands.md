# Chapter 4 — Targeting: EPR, Protein Corona, and Active Ligands

A biotech company designs a nanoparticle decorated with antibodies against HER2, a receptor overexpressed on some breast cancers. In the lab, the targeted particle binds HER2-positive cells beautifully and is taken up at many times the rate of an untargeted control. The story writes itself: the antibody steers the particle to the tumor. The company raises money on the strength of "active tumor targeting."

In the animal study, the targeted and untargeted particles accumulate in the tumor at nearly the same total amount. The targeting antibody, so decisive in a dish, made almost no difference to how much drug reached the tumor. Two things had gone wrong with the company's mental model. First, the antibody acts only at the final step — cellular uptake — and only *after* the particle has already arrived; it does nothing to get the particle to the tumor in the first place. Second, the moment the particle entered blood, plasma proteins swarmed its surface and formed a coating — a **protein corona** — that buried many of the antibodies, blunting the targeting they had engineered so carefully.

The company had confused *binding cells in a dish* with *reaching a tumor in a body*. This chapter is about that gap — about what targeting can and cannot do, and about the honest, unsettled state of the central idea the whole field was built on.

---

## Passive targeting and the EPR effect

**Passive targeting** means accumulation without a targeting ligand — getting particles to the tumor through the physical properties of the particle and the physical properties of the tumor, nothing more. The mechanism that makes this possible is the **enhanced permeability and retention** (EPR) effect, first characterized by Matsumura and Maeda in 1986 and still the conceptual foundation of every approved nanoparticle cancer therapy.

The EPR effect rests on two features of tumor vasculature. Tumor blood vessels are structurally abnormal — leaky, with gaps between endothelial cells that normal capillaries do not have. Nanoparticles in the right size range can escape through these gaps into the tumor tissue. Once there, the second feature holds them: tumors have impaired lymphatic drainage, so macromolecules and particles that enter do not clear efficiently. They accumulate. This is retention — not because the particle is sticky, but because the exit is broken.

For passive targeting to work, a particle needs to be in the size range that fits through the vessel gaps (roughly 10 to 200 nm), and it needs to survive circulation long enough to reach the tumor multiple times before being cleared. PEGylation — coating with polyethylene glycol — extends circulation by shielding the particle from the opsonin proteins that would flag it for liver and spleen removal. This is the logic behind Doxil, the PEGylated liposomal doxorubicin approved in 1995: extend circulation, let the particle drift out of leaky tumor vessels, retain it there because the lymphatics are bad.

EPR is the field's founding mechanism. It is also genuinely contested, and treating it as settled dogma rather than a hypothesis to be measured in each patient is one of the field's recurring mistakes.

---

## The honest problem with EPR

The EPR effect was characterized primarily in rodent tumor models — fast-growing, relatively uniform, highly vascular, and highly permeable. Human tumors are slower-growing, more heterogeneous, and far more variable in their vascular permeability. Some human tumors are permeable enough for meaningful EPR-driven accumulation; many are not; and there is currently no reliable way to know before treatment which category a given patient's tumor falls into.

The sharpest quantification of the gap came from a 2016 meta-analysis by Wilhelm and colleagues, who compiled published nanoparticle delivery data across studies and found a median of roughly **0.7% of the injected dose reaching the tumor**. This number is widely cited and widely contested — it conflates particles of different sizes, surface chemistries, and tumor types; it is drawn largely from mouse studies; and the fraction of dose needed for clinical benefit is separately uncertain. But the underlying message is not seriously disputed: EPR is variable and frequently weak in human tumors, and the high accumulation fractions observed in many mouse experiments do not reproduce reliably in patients.

The honest position is neither "EPR is fake" nor "EPR reliably delivers drugs." It is something more uncomfortable: EPR is real but heterogeneous, it is the mechanism behind every approved passive-targeting nanomedicine, and its magnitude in any given patient's tumor cannot currently be predicted from outside the patient. The tumor permeability that enables accumulation in one patient may be absent in another with an apparently identical diagnosis.

This matters practically. A particle designed entirely around EPR-based delivery is betting on a mechanism that may simply not operate in a substantial fraction of patients. Recognizing this is not a reason to abandon nanomedicine; it is a reason to measure delivery rather than assume it, and to develop imaging tools that identify which patients have permeable enough tumors before committing to a therapy designed around that permeability.

<!-- → [DIAGRAM: EPR reliability spectrum — a horizontal bar from "mouse models (high, uniform permeability)" on the left to "human tumors (variable, often weak)" on the right; a marker at ~0.7% median injected dose to tumor (Wilhelm 2016); two annotation labels "hype: reliable targeting" and "cynicism: nanomedicine fails" struck through, with a centered "calibrated: real but variable" label] -->

---

## Active targeting and what it actually changes

**Active targeting** adds surface ligands — antibodies, peptide fragments, aptamers, small molecules like folic acid — to the particle's surface so that it binds a specific marker on cancer cells. The targets are typically receptors overexpressed on tumor cells: HER2, EGFR, transferrin receptor, folate receptor, CD44.

The crucial and widely misunderstood point is that active targeting changes **cellular uptake**, not necessarily **tumor accumulation**. A ligand operates at the final step of the delivery chain — binding and internalization into a cell. It acts only after the particle has already survived circulation, extravasated through the vessel wall, and penetrated the tumor interstitium. It cannot improve those earlier steps. The fraction of dose that reaches the tumor is determined by circulation half-life, vessel permeability, and tissue penetration — all of which precede the ligand's moment of action.

This is why the opening-case company saw equal total accumulation between targeted and untargeted particles: the antibody affected what happened to particles that were already in the tumor, not how many got there. Their total amount at the tumor site — governed by EPR and clearance — was the same. The targeted particles entered cells more efficiently once present; the untargeted particles sat in the interstitium longer. From the perspective of delivered drug to tumor tissue, the difference was small.

This is not a universal finding — there are experimental systems where active targeting has improved tumor accumulation, often by altering how particles interact with the tumor endothelium rather than with tumor cells directly. But it is the dominant pattern, and assuming that a ligand which works in a dish will increase tumor delivery in an animal is the mistake the field has made repeatedly.

Active targeting can still be valuable. Better cellular uptake means more drug inside tumor cells rather than stranded in the interstitium. Receptor-mediated endocytosis can deliver particles to specific intracellular compartments and improve payload release. And when the target is truly tumor-specific and dense, the ligand can improve the ratio of tumor-cell uptake to non-specific stromal uptake. These are real benefits. They are just not the benefit most often claimed — tumor accumulation.

![Three-panel sequence: a bare particle extravasating by EPR, ligands docking a cell-surface receptor, and the protein corona burying ligands in blood and diverting the particle to clearance](images/04-targeting-epr-protein-corona-and-active-ligands-fig-01.png)
*Figure 4.1 — Passive vs active targeting and the protein corona*

<!-- → [DIAGRAM: passive vs active targeting + protein corona schematic. Left panel: passive — bare PEGylated particle drifting out of a leaky tumor vessel (EPR), no ligand. Middle panel: active — particle with surface antibodies binding a receptor on a tumor cell, AFTER extravasation. Right panel (corona): a particle entering blood, plasma proteins (opsonins) adsorbing onto its surface and burying the targeting ligands; arrow to liver/spleen uptake.] -->

---

## The protein corona

The moment a nanoparticle enters blood, plasma proteins begin adsorbing onto its surface. Within seconds, the particle acquires a dense coating of biomolecules — albumin, immunoglobulins, fibrinogen, apolipoproteins, complement proteins, and many others — that forms what is called the **protein corona**. The engineered surface you designed is no longer what the body sees; the corona is.

Two consequences matter for targeting.

The corona can **mask targeting ligands**. Proteins adsorbing onto the particle surface can physically cover antibodies, peptides, or aptamers that were engineered to bind tumor receptors. The ligand is still covalently attached to the particle, but it cannot reach its receptor because a layer of plasma protein is in the way. This is precisely what happened in the opening case: the HER2 antibodies were buried by the corona before the particles ever encountered a tumor cell. The targeting that worked perfectly in protein-free culture medium failed in blood.

The corona can **redirect particle fate**. Certain proteins in the corona — complement fragments and opsonins — are recognition signals for macrophages in the liver and spleen. A particle whose engineered surface evades clearance may, once coated with the wrong proteins, be flagged for rapid removal. The PEG coating that was supposed to prevent this may be partially effective, but PEG does not prevent all corona formation, and the specific protein composition of the corona varies with particle surface chemistry, particle size, and patient plasma composition. The corona the particle acquires in one patient may differ from the corona it acquires in another.

The protein corona is why validating a targeting strategy in clean cell-culture medium is insufficient. The bare ligand works in medium because there is no corona. In blood, the corona forms and the ligand may fail. Any targeting strategy must be tested in conditions that allow corona formation — at minimum, in full plasma — before conclusions about in vivo function are warranted.

There is an emerging view that the corona could be engineered as a feature rather than fought as a bug. Designing surfaces that deliberately recruit beneficial corona proteins — ones that prolong circulation or aid uptake by specific cell types — is conceptually appealing. This is an active research area, not an established strategy, but it represents a more honest engagement with the corona than pretending it can be eliminated.

---

## What targeting can and cannot do

A particle travels through a sequence of environments — blood, tumor vessel wall, tumor interstitium, tumor cell surface, intracellular space — and targeting strategies act at specific points in that sequence, not uniformly across all of them.

**Passive targeting (EPR)** operates at the vessel-wall step: it gets particles from the blood into the tumor tissue, when tumor vessels are permeable enough. It is real but variable and often weak in human patients.

**Active targeting (ligands)** operates at the cell-surface step: it improves uptake into cells, after the particle has arrived. It does not improve accumulation at the tumor, and it can be sabotaged by the corona before it ever operates.

**Neither strategy overrides the dose-loss chain.** The fraction of injected dose that reaches the tumor is still determined primarily by clearance organs, vessel permeability, and interstitial penetration. Targeting is an intervention at a specific step, not a global multiplier on delivery. Claiming it is anything more requires data from the steps it is supposed to affect — not inference from the step it actually affects.

---

## The folate receptor: a case study in inference gone wrong

Consider a concrete example. A team reports that their folate-targeted nanoparticle is taken up by folate-receptor-positive tumor cells at eight times the rate of an untargeted control in cell culture. They conclude the targeting will substantially increase tumor drug delivery in patients.

The 8× figure is real. The inference is wrong. Cell-culture uptake measures only the final step — binding and entry — in conditions with no circulation, no clearance, and no protein corona. It cannot predict total tumor accumulation, which is set by the earlier steps the ligand does not affect. In blood, the corona may mask the folate ligand. In the tumor, folate-receptor expression is heterogeneous — many cells may not express the target. Total accumulation will be governed by EPR, not by the folate ligand.

The history confirms this. The folate-camptothecin conjugate EC145 — tested specifically in folate-receptor-positive cancers — did not achieve regulatory approval. Meanwhile, folate-receptor targeting succeeded in a completely different format: the antibody-drug conjugate mirvetuximab soravtansine, approved for ovarian cancer. The same target, different carrier format, opposite outcome. What this suggests is that the format and the delivery chain, not the targeting concept in isolation, decide the result. An antibody-drug conjugate is not a nanoparticle — its delivery mechanism, circulation, and tumor penetration are different — and those differences, not the shared target, explain why one worked and the other did not.

![Two-track comparison of the same folate-receptor target: a bulky nanoparticle conjugate (EC145) that failed approval versus a compact antibody-drug conjugate (mirvetuximab) that succeeded](images/04-targeting-epr-protein-corona-and-active-ligands-fig-02.png)
*Figure 4.2 — Same target, two formats: nanoparticle vs ADC*

Before a trial based on folate targeting, the right measurements are: total tumor accumulation *in vivo* with a labeled particle, ligand function in the presence of plasma, and receptor expression in the specific patient population.

---

## What would change this picture

The chapter's central claim is twofold: EPR-based passive targeting is real but variable and often weak in human tumors, and active targeting improves cellular uptake rather than tumor accumulation. Two findings would force revision in opposite directions.

If a large, rigorously controlled human study showed that a targeting ligand *increases total tumor accumulation* — not just intracellular uptake — by a clinically meaningful margin across patients, the claim that ligands cannot overcome the circulation-and-clearance bottleneck would need revising. And if robust noninvasive imaging across many patients showed that EPR delivers a consistent, substantial fraction of injected dose to most human solid tumors, the "variable and often weak" characterization would be wrong.

The current evidence — the ~0.7% median, the variability across tumor types, the corona-masking mechanism, and the repeated failure of active targeting to improve accumulation over passive — points toward the claims as stated. But these are active experimental questions, not closed ones.

---

## Still open

Whether the ~0.7% median delivery figure is the right metric at all is genuinely debated. It conflates very different particles and tumors, and the fraction of dose needed for clinical benefit — which depends on drug potency, tumor volume, and receptor density — is separately uncertain. Local concentration at the tumor may matter more than whole-body percentage, and very potent payloads may produce clinical benefit from fractional delivery that would look inadequate by a percent-of-dose metric.

Whether patients can be stratified before treatment by tumor permeability — a companion imaging test that identifies who has EPR-accessible tumors — remains a major open question. Such a test would transform the clinical use of passive-targeting nanomedicines from population-average strategies to truly individualized therapy selection.

Whether the protein corona can be deliberately engineered to improve targeting rather than blocked as interference is an active area of inquiry that has not yet produced a clinical-stage strategy. Recruiting specific corona proteins that promote uptake by tumor endothelium or that extend circulation half-life is conceptually achievable but practically undemonstrated at scale.

And the folate-receptor comparison — the same target failing in a nanoparticle format and succeeding in an antibody-drug conjugate format — is a natural experiment that the field has not fully analyzed. Understanding precisely which aspects of the delivery chain differed between EC145 and mirvetuximab soravtansine would clarify when targeting the same receptor in different formats changes the outcome.

---

## LLM Exercises

1. **(EPR mechanics)** Define the EPR effect, name its two underlying vascular features, and explain in one sentence each why it works more reliably in mouse tumor models than in human tumors. Then identify the single measurement that would tell you whether EPR is operating in a specific patient's tumor before treatment.

2. **(Active targeting chain analysis)** A targeted nanoparticle shows 10× higher cellular uptake than an untargeted control in cell culture, but identical total tumor accumulation in mice. Explain this result by mapping each finding to the specific step of the delivery chain it reflects. Identify the one in-blood experiment that would test whether the protein corona is masking the targeting ligand, and describe the result that would confirm corona-mediated masking.

3. **(0.7% calibration)** Interpret the ~0.7% median tumor-delivery figure for two audiences: an investor who concludes "nanomedicine has failed," and an enthusiast who insists EPR reliably targets tumors. Write a two- to three-sentence calibrated response to each that neither dismisses nor overstates the evidence. Reference at least one approved nanomedicine and the contested nature of the statistic in your response.

4. **(Folate-receptor case)** The folate-receptor-targeted nanoparticle conjugate EC145 failed in clinical trials; the folate-receptor-targeted antibody-drug conjugate mirvetuximab soravtansine succeeded. Both targeted the same receptor on the same cancer type. Identify at least three mechanistic differences between a nanoparticle and an antibody-drug conjugate at each step of the delivery chain that could explain the different outcomes. State which difference you consider most likely to be decisive and why.

5. **(Targeting evaluation plan)** Design an evaluation plan for a new HER2-targeted liposomal nanoparticle before committing to a clinical trial. Specify: one experiment to measure total tumor accumulation independent of cellular uptake; one experiment to test whether the protein corona masks the HER2 ligand; one pre-specified criterion that would tell you the active-targeting ligand adds enough value over a simpler passive (PEGylated) design to justify the added complexity. State, in advance, the result that would lead you to drop active targeting.

---

## References

- Matsumura, Y., & Maeda, H. (1986). A new concept for macromolecular therapeutics in cancer chemotherapy: mechanism of tumoritropic accumulation of proteins and the antitumor agent SMANCS. *Cancer Research*, 46(12 Pt 1), 6387–6392.
- Maeda, H. (2001). The enhanced permeability and retention (EPR) effect in tumor vasculature: the key role of tumor-selective macromolecular drug targeting. *Advances in Enzyme Regulation*, 41, 189–207.
- Nichols, J. W., & Bae, Y. H. (2014). EPR: evidence and fallacy. *Journal of Controlled Release*, 190, 451–464.
- Wilhelm, S., Tavares, A. J., Dai, Q., Ohta, S., Audet, J., Dvorak, H. F., & Chan, W. C. W. (2016). Analysis of nanoparticle delivery to tumours. *Nature Reviews Materials*, 1, 16014.

---

## Prompts

### Figure 4.1 — Passive vs active targeting and the protein corona
Build a left-to-right three-stage sequential flow / schematic showing where each targeting mechanism acts and how the corona sabotages it. Stage 1 "Passive (EPR)": a bare particle extravasating from a leaky tumor vessel into tissue. Stage 2 "Active": surface ligands docking a cell-surface receptor, occurring AFTER arrival — connect from Stage 1 with an arrow labeled "then". Stage 3 "Corona": in blood, plasma proteins (albumin, immunoglobulins, fibrinogen, opsonins) swarm the particle and bury the ligands → diverted to clearance — connect with an arrow labeled "but in blood". Encode Stage 1 (passive extravasation) in dominant blue; Stage 2 (successful ligand docking) in green (positive); Stage 3 (corona masking → clearance) in vermillion (blocking/negative). Make explicit that active binding happens downstream of arrival and the corona acts before the ligand can. Direct-label each stage. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned via CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 4.2 — Same target, two formats: nanoparticle vs ADC
Build a two-track parallel comparison schematic contrasting two delivery formats aimed at the same folate-receptor target, with opposite outcomes. Left track "Nanoparticle conjugate (EC145)": a bulky particle bearing surface ligands; its delivery path is blocked before meaningful delivery; result: failed approval. Right track "Antibody-drug conjugate (mirvetuximab soravtansine)": a compact Y-shaped antibody conjugate whose path completes and reaches the target; result: approved. Lay the two tracks in parallel along a shared axis labeled "Same folate-receptor target, opposite outcome". Encode the failing nanoparticle track (blocked path, failed approval) in vermillion (blocking/negative); encode the succeeding ADC track in green (positive). Use the antibody/particle shapes as the sky-blue anchor distinguishing the two formats. Direct-label each track's path-completion and approval outcome. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned via CDN, Okabe-Ito colorblind-safe palette via CSS variables.
