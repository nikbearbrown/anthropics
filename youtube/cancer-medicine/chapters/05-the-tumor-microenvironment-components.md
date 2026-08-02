# Chapter 5 — The Tumor Microenvironment: Components
*The Cancer Cell Was Never Alone.*

Here is a number that should stop you. In some pancreatic tumors, cancer cells make up less than fifteen percent of the tissue. Cut out the tumor, section it, stain it, look through the microscope — and the malignant cells are a small minority in their own house. The rest is collagen, fibroblasts, immune cells clustered at the edges and absent from the center, adipocytes, nerve fibers, vessels, and bacteria. The drug the oncologist prescribed kills pancreatic cancer cells efficiently in a dish. In the patient, it barely touches them — because it cannot get through the wall the tumor built around itself before the drug arrived.

This is the opening puzzle of the tumor microenvironment, and it forces a fundamental reorientation. The field spent decades treating cancer as a problem of cancer cells. A tumor is a population of malignant cells that needs to be killed. The drugs need to kill them. When the drugs fail, the cancer cells must have mutated resistance. That framework is not wrong, but it is incomplete in a way that kills people. The cancer cells live in a community they help construct and that actively defends them. Understanding that community — who lives in it, what each member does, and how the whole structure shapes what any therapy can achieve — is what this chapter is about.

---

The formal term is **tumor microenvironment** — the TME. It names the complete local ecosystem in which cancer cells live: the non-malignant cellular residents (fibroblasts, immune cells of many types, endothelial cells, pericytes, adipocytes, nerve fibers), the **extracellular matrix** that fills the spaces between all of them, the soluble signals (cytokines, growth factors, metabolites) moving through that space, and, in many tumors, resident microorganisms. The relationship between cancer cells and their environment is **bidirectional**: cancer cells secrete factors that reshape the habitat, and the habitat sends back signals that reshape the cancer cells — altering their gene expression, metabolism, invasiveness, and response to drugs. Mina Bissell demonstrated this experimentally in three-dimensional culture systems: malignant cells returned to near-normal behavior when placed in the right matrix context (Bissell & Radisky, 2001). The habitat shapes the cancer. That principle runs through everything that follows.

The first task is a census.

![Spatial map of the tumor microenvironment showing cancer cells as a minority among CAFs, T cells, myeloid cells, abnormal vessels, and dense ECM in bidirectional signaling contact](images/05-the-tumor-microenvironment-components-fig-01.png)
*Figure 5.1 — TME cell-component census map*

<!-- → [DIAGRAM: TME cell-component map — central nest of tumor cells surrounded by labeled populations: CAFs (with distance gradient, myCAFs close, iCAFs farther), CD8+ T cells, Tregs, TAMs, MDSCs, dendritic cells, endothelial cells with pericyte coverage shown as partial wrapping, adipocytes, nerve fibers, and ECM collagen fibers filling interstitial space; small inset showing cytokine arrows flowing bidirectionally between populations] -->

---

The most abundant non-malignant cell type in many solid tumors — more numerous than the cancer cells themselves in some regions — is the **cancer-associated fibroblast**. In healthy tissue, fibroblasts are quiet maintenance workers: they synthesize ECM, balance its production and degradation, and activate transiently during wound repair before returning to quiescence. CAFs are the activated, permanently altered version. They do not return to quiescence. They are recruited from resident tissue fibroblasts, from bone-marrow-derived mesenchymal precursors, and from trans-differentiated pericytes and adipocytes — multiple origins feeding the same activated pool (Sahai et al., 2020).

Single-cell sequencing since roughly 2010 has resolved at least three functionally distinct subtypes. **Myofibroblastic CAFs** — myCAFs — express α-smooth muscle actin, sit close to tumor cell borders, and are the primary manufacturers of dense collagen. They build the wall. **Inflammatory CAFs** — iCAFs — sit farther from tumor cells and are the primary secretors of pro-inflammatory, immunosuppressive cytokines: IL-6, CXCL12, LIF. They run the chemical defense. **Antigen-presenting CAFs** — apCAFs — express MHC class II and can interact directly with T cells, though whether they activate or suppress them depends on context (Sahai et al., 2020).

![Radial-zone gradient of CAF subtypes by distance from the tumor — myCAFs hugging the border building the collagen wall, iCAFs farther out secreting immunosuppressive cytokines, apCAFs presenting antigen](images/05-the-tumor-microenvironment-components-fig-02.png)
*Figure 5.2 — CAF subtypes and their spatial gradient*

What CAFs *do* in combination explains why the pancreatic cancer patient's gemcitabine failed at multiple levels simultaneously. The myCAFs laid down the collagen that physically stopped the drug from diffusing into the tumor interior. The iCAFs secreted TGF-β and CXCL12, which repelled cytotoxic T cells from the tumor core and recruited immunosuppressive myeloid cells instead. Other CAF-derived signals — HGF, IGF — fed pro-survival pathways directly into the cancer cells. And some CAF populations appear able to supply metabolites directly to cancer cells when nutrients are scarce. High CAF density correlates with worse prognosis and reduced therapy response across multiple cancer types `[verify]`. Targeting them has proven difficult: partly because the subtypes have different and sometimes opposing functions, and partly because some CAF activity appears genuinely tumor-restraining, so blunt depletion can worsen the disease `[contested — blunt CAF depletion accelerating progression in some pancreatic models; see pantry flag]`.

---

The immune compartment of a tumor is the section most likely to mislead you if you treat cell identity as equivalent to cell function. The same cell type, in different activation states, can either kill cancer cells or protect them. The mix — and more importantly the *state* and *location* of each component — determines whether the immune system is the tumor's enemy or its ally.

**Cytotoxic CD8+ T cells** are what you want: they recognize tumor-specific antigens presented on MHC class I, form immunological synapses with cancer cells, and kill them. High CD8+ infiltration throughout the tumor is the single best cellular predictor of response to checkpoint immunotherapy and, in many cancers, of better outcomes generally. **Regulatory T cells (Tregs)** are the direct antagonists: they suppress cytotoxic T-cell activity through IL-10, TGF-β, and CTLA-4-mediated mechanisms, and tumors actively recruit them. High Treg infiltration predicts worse outcomes and reduced immunotherapy response. **Natural killer cells** patrol for MHC class I loss — the trick many tumors use to hide from CD8+ T cells — and kill without requiring antigen recognition, making them important in tumors that have downregulated their MHC.

**Tumor-associated macrophages** are the clearest illustration of the identity-versus-function problem. They exist on a spectrum — "M1" at one end (pro-inflammatory, tumoricidal) and "M2" at the other (tissue-remodeling, pro-tumor) — though the M1/M2 binary is a simplification of a biological continuum (Mantovani et al., 2017). In most established tumors, the macrophages that have been recruited and shaped by tumor-secreted signals (IL-4, IL-13, M-CSF, CSF1) are skewed toward the M2-like end: they promote angiogenesis through VEGF secretion, suppress T-cell function, remodel matrix through MMP secretion, and provide metabolic support to cancer cells. They are not defending the host. They have been converted into construction workers and guards for the tumor.

**Myeloid-derived suppressor cells** are immature myeloid cells that never fully differentiated into macrophages, dendritic cells, or neutrophils because the tumor arrested their development. Their primary function, in the context of a tumor, is immune suppression: they deplete arginine (required for T-cell proliferation), produce reactive oxygen species that damage T cells, and express PD-L1. They are one of the main reasons that checkpoint inhibitors — which release T cells from PD-1-mediated suppression — sometimes fail even when T cells are present: the T cells are being suppressed through other channels.

**Dendritic cells** should be the initiators of anti-tumor immune responses — they capture tumor antigens, migrate to lymph nodes, and activate naïve T cells. In most tumors, tumor-secreted VEGF, IL-10, and TGF-β keep dendritic cells immature and functionally paralyzed. A tumor that prevents dendritic-cell maturation has, in effect, cut the wire between the tumor and the lymph node — the immune response never gets started.

<!-- → [TABLE: immune cell populations in the TME — columns: cell type, identifying marker(s), pro- or anti-tumor function in established tumors, mechanism, consequence for therapy] -->

The spatial distribution of these populations defines what is now called the tumor's **immune phenotype**. An **inflamed (hot) tumor** has CD8+ T cells distributed throughout, in direct contact with cancer cells. A **cold (desert) tumor** has almost no lymphocytes. An **excluded tumor** — the clinically crucial middle category — has abundant CD8+ T cells, but they are arrested at the tumor margin, unable to penetrate the interior. The difference between hot and excluded matters enormously for checkpoint inhibitors: in a hot tumor, releasing the PD-1 brake lets T cells that are already touching cancer cells kill them. In an excluded tumor, the T cells are not touching anything — removing the brake disinhibits a stalled army and accomplishes nothing.

---

The blood supply of a tumor is not normal vasculature. Tumor endothelial cells grow rapidly under VEGF pressure, and the vessels they form are structurally abnormal: tortuous, irregularly branching, focally dilated or constricted, with poor pericyte coverage and walls that leak macromolecules and cells. These structural defects have direct consequences at every level.

Leaky vessels elevate **interstitial fluid pressure** — fluid pushed out of the vasculature raises the hydraulic pressure in the tumor stroma, which then *opposes* the pressure gradient that drives drug delivery. Drugs carried by the blood cannot diffuse into a compartment at higher pressure than the vessel. Chemotherapy arrives at the tumor periphery and cannot penetrate. This is the same physical principle that explains why lymphedema prevents normal tissue from receiving adequate circulation — but here the tumor has engineered the condition to protect itself.

Endothelial cells in tumors also regulate immune trafficking. Abnormal adhesion molecule expression changes which immune cells can roll, adhere, and transmigrate. In some highly immunogenic tumors, specialized **high endothelial venules** form — structures that actively recruit lymphocytes into the tissue — and their presence correlates with T-cell infiltration and better immunotherapy response `[verify]`. In most tumors, the reverse is true: the vascular architecture discourages cytotoxic immune-cell entry while permitting passage of immunosuppressive myeloid populations.

**Pericytes** are the contractile cells that wrap capillaries and stabilize them. Sparse pericyte coverage is part of why tumor vessels leak. It is also therapeutically relevant: vessels with heavy pericyte investment are mature and VEGF-independent — they survive anti-VEGF therapy because they no longer require VEGF signaling to maintain themselves. Vessels with sparse pericyte coverage remain VEGF-dependent and drug-responsive. The pericyte status of tumor vasculature is one of the determinants of which tumors respond to anti-angiogenic agents `[verify]`.

---

Between all of these cells sits the **extracellular matrix** — and it is not passive scaffolding. In healthy tissue, the ECM is a precisely maintained structure of collagen I and III, fibronectin, laminin, hyaluronic acid, and proteoglycans, continuously synthesized and degraded by a balanced set of enzymes. In tumors, particularly pancreatic and breast tumors, the matrix is heavily remodeled toward elevated collagen I, fibronectin, tenascin-C, and hyaluronic acid. The overall structure is *stiffer* than normal tissue — measurably so, which is part of why some tumors can be palpated.

Stiffness is not just a mechanical property. Cancer cells sense matrix rigidity through **integrins** — surface receptors that span the membrane and connect to the cytoskeleton — and transduce it into intracellular signals through the YAP/TAZ transcription factor pathway and Rho GTPase activation. A stiffer matrix drives proliferation and survival signaling. The tumor has, in effect, built a scaffold that tells cancer cells to keep growing. The matrix is also a reservoir: growth factors including TGF-β and VEGF are bound to matrix components and released when proteases cleave them. And the cleavage products themselves — **matrikines** like endostatin, tumstatin, and arresten — have their own bioactivities, some anti-angiogenic, some mitogenic.

For therapy, the dense ECM is a double barrier. It physically impedes drug diffusion. It also blocks immune-cell migration — cytotoxic T cells and NK cells move through tissue by extending protrusions and exerting force against matrix fibers; in a highly crosslinked collagen network, that movement is mechanically blocked. The "excluded" immune phenotype described above is often a matrix exclusion: the T cells are stopped at the collagen capsule the CAFs have built. This is why PEGPH20, a hyaluronidase that degrades hyaluronic acid in the matrix, was tested in pancreatic cancer — the logic was sound. The results were mixed, which is a warning that the barrier model, while correct in outline, is not the complete story `[contested — see What Would Change My Mind]`.

![Feedback cycle of ECM remodeling: CAFs deposit and stiffen matrix, integrins sense stiffness via YAP/TAZ to drive proliferation, proteases release matrix-bound growth factors and bioactive matrikines](images/05-the-tumor-microenvironment-components-fig-03.png)
*Figure 5.3 — ECM remodeling cycle*

<!-- → [INFOGRAPHIC: ECM remodeling cycle — matrix deposition by CAFs, stiffness sensing via integrins/YAP-TAZ, growth factor storage and protease-mediated release, matrikine generation; arrows showing bidirectional feedback between ECM state and cancer cell behavior] -->

---

Three more TME inhabitants deserve mention because they complicate treatment in ways that are not widely appreciated.

**Adipocytes** adjacent to tumors are not passive fat depots. Breast and ovarian cancers recruit nearby adipocytes to become **cancer-associated adipocytes**, which transfer fatty acids and adipokines to cancer cells — supplying energy substrate and mitogenic signals. This is part of why obesity elevates risk and worsens prognosis in several cancers: the adipose tissue itself becomes a resource the tumor can mine.

**Nerve fibers** grow into many tumors — a process called **cancer neoneurogenesis** — and neural signaling, particularly through sympathetic β-adrenergic pathways, can promote tumor progression, metastasis, and suppression of anti-tumor immunity. Retrospective studies have associated β-blocker use with improved outcomes in some cancers, but prospective evidence is sparse and the mechanism in human tumors remains incompletely established `[contested — see pantry flag]`.

**Microorganisms** inhabit many tumors. In colorectal cancer, *Fusobacterium nucleatum* is enriched relative to adjacent normal tissue and correlates with worse prognosis — it may promote tumor growth through FadA adhesin binding to E-cadherin on cancer cells and activating Wnt signaling. In pancreatic tumors, bacterial communities including Gammaproteobacteria express long-form isoforms of the enzyme cytidine deaminase, which metabolizes gemcitabine into an inactive form before the drug reaches tumor cells (Riquelme et al., 2019). The opening patient's chemotherapy may have been degraded by bacteria before it reached the cells it was designed to kill. That is not a resistance mutation in a cancer cell. It is a bacterial enzyme in the tumor's ecosystem doing the cancer's work for it.

<!-- → [TABLE: non-fibroblast, non-immune TME residents — columns: cell/organism type, representative example, mechanism of tumor support, therapeutic relevance or vulnerability] -->

---

Two patients have melanoma. Patient A's tumor, on staining, shows CD8+ T cells distributed throughout the tumor nests. Patient B's tumor shows CD8+ T cells dense at the outer rim but absent from the interior, with a thick collagen capsule on trichrome stain. Both are offered anti-PD-1 therapy.

The naive prediction is that both patients have anti-tumor T cells and both should respond. But this conflates identity with location — CD8+ cells anywhere on the slide — with the functional question: are those T cells in contact with cancer cells, or not? Patient A is an inflamed tumor: T cells are already touching their targets, held in check by PD-1/PD-L1 signaling. Remove that checkpoint and they kill. Patient B is an excluded tumor: the T cells are arrested at the collagen wall the CAFs built. Releasing the PD-1 brake on T cells that are not engaging their target changes nothing. Patient A responds. Patient B likely does not — not because the immune cells are absent, but because the structural TME has made them irrelevant.

This is the identity-versus-function principle at full resolution: what a cell is called is not what it is doing. A tumor packed with immune cells can be more immune-*suppressed* than a tumor with few, if the cells present are Tregs and M2 macrophages rather than CD8+ killers. The therapeutic implication is not to ask "is the immune system present?" but to ask "which immune cells, in what state, in what location, with what structural barriers between them and the cancer cells?"

![Three tumor cross-sections contrasting hot/inflamed (CD8+ T cells throughout), excluded (T cells trapped at a collagen margin), and cold/desert (sparse lymphocytes) immune phenotypes with their checkpoint-blockade responses](images/05-the-tumor-microenvironment-components-fig-04.png)
*Figure 5.4 — Hot vs excluded vs cold immune phenotypes*

<!-- → [DIAGRAM: hot vs. excluded vs. cold immune phenotype — three tumor cross-sections side by side; hot: CD8+ cells distributed throughout tumor nests; excluded: CD8+ cells dense at margin, absent in core, collagen band visible at border; cold: sparse immune cells throughout; each labeled with predicted checkpoint inhibitor response] -->

---

The cancer cell is the protagonist of most oncology narratives. It is the cell that mutated, that proliferated, that metastasized. It gets the gene sequencing and the targeted therapy. But in many solid tumors, the cancer cell is a minority resident in a community it has co-opted, living behind walls it hired others to build, supplied by vessels it corrupted, and defended by immune cells it converted. Treating only the cancer cell — designing drugs in monolayer culture, testing them in cancer-cell xenografts without stroma, measuring response by the fraction of cancer cells killed in vitro — is treating a fraction of the problem.

The still-open questions in this field are genuinely hard: we cannot yet distinguish tumor-promoting from tumor-restraining CAF subtypes in a living patient. We do not know whether the tumor microbiome is a driver or a passenger in most cancers. We cannot reliably convert a cold tumor to a hot one. The β-adrenergic question is decades old and still unresolved in humans. Some hot tumors, full of CD8+ T cells in apparent contact with cancer cells, still resist checkpoint blockade — and we do not fully understand why.

What this chapter provides is the framework the field is working inside: cancer as an ecosystem, where the habitat shapes the malignancy, where therapy must reach through structural and cellular barriers to get to its target, and where the question "will this treatment work?" requires an answer about the whole community, not just the cancer cell.

---

## Exercises

**Warm-up**

1. *[Recall — moderate]* Name the three major CAF subtypes identified by single-cell sequencing. For each, give its location relative to tumor cells, one defining marker or secreted factor, and one mechanism by which it worsens therapy response.
*What this tests: whether you can distinguish CAF subtypes by location and function, not just as a single undifferentiated population.*

2. *[Recall — moderate]* Explain in three sentences why a tumor packed with immune cells is not necessarily an immunologically active tumor. Name two specific cell types whose high abundance would indicate immune suppression rather than immune attack.
*What this tests: the identity-versus-function principle — cell presence versus cell state and function.*

3. *[Recall — moderate]* Describe two ways in which tumor ECM stiffness promotes cancer-cell survival, naming the mechanosensing pathway involved and the downstream transcriptional consequence.
*What this tests: understanding the ECM as an active signaling environment, not passive scaffolding.*

**Application**

4. *[Apply — moderate-hard]* A colorectal tumor biopsy shows a desert immune phenotype and high *Fusobacterium nucleatum* burden. The patient is offered anti-PD-1 therapy. Predict the likely response and justify your prediction using at least two distinct TME components. Then propose one rational combination strategy that might convert this tumor toward responsiveness and state the specific mechanism your strategy engages.
*What this tests: applying immune phenotype classification and microbiome biology to a treatment decision.*

5. *[Apply — moderate-hard]* A new drug degrades hyaluronic acid in the tumor matrix. A trial in pancreatic cancer shows improved drug penetration in early biopsies but no overall survival benefit. Using the TME framework, generate two hypotheses that could explain the disconnect between improved drug delivery and unchanged survival. For each hypothesis, name the TME component that would need to be characterized to test it.
*What this tests: ability to move from a single-component model to a multi-component explanation of treatment failure.*

6. *[Apply — hard]* Build a two-column identity-versus-function table for six TME immune populations: CD8+ T cell, Treg, M1 macrophage, M2 macrophage, MDSC, and dendritic cell. Column one: the marker or feature used to identify it. Column two: its function in an established tumor and one consequence for therapy. Then write a two-sentence caption explaining why a therapy that depletes all macrophages by identity (targeting a pan-macrophage marker) could harm as much as help.
*What this tests: systematic application of the identity/function distinction across the immune compartment.*

**Synthesis**

7. *[Synthesis — hard]* The opening case describes gemcitabine failure in pancreatic cancer. Trace the failure through at least four distinct TME mechanisms — physical, cellular, signaling, and microbial — naming the specific component responsible for each and what a combination strategy targeting all four would require. Then identify which of the four components is hardest to target and explain why.
*What this tests: integration of multiple TME components into a mechanistic account of therapy failure; ability to identify the limiting step.*

8. *[Synthesis — hard]* Patient A has an inflamed melanoma (CD8+ T cells throughout the tumor nests). Patient B has an excluded melanoma (CD8+ T cells at the margin only, dense collagen capsule). Both progress after anti-PD-1 monotherapy. For each patient, propose a different mechanism of resistance, a different rational next therapy, and the TME feature that would need to change for that therapy to work. Your answers for A and B should be mechanistically distinct.
*What this tests: applying the immune phenotype framework to resistance scenarios; generating mechanistically grounded next-line strategies.*

**Challenge**

9. *[Challenge — very hard]* The chapter notes that some CAF subtypes appear tumor-restraining, and that blunt CAF depletion can worsen outcomes in some preclinical models. Design a translational study — using paired biopsies, single-cell sequencing, and a functional readout — that could determine whether the dominant CAF population in a given patient's pancreatic tumor is net tumor-promoting or net tumor-restraining before initiating any CAF-targeting therapy. What markers, timepoints, functional assays, and control conditions would the study require? What is the minimum data package that would justify a CAF-targeting trial arm in that patient?
*What this tests: ability to translate the heterogeneity problem into a clinical study design; reasoning about biomarker strategy and therapeutic gatekeeping.*

---

## What Would Change My Mind

The chapter's central claim is that the non-malignant TME is a causal driver of tumor behavior and therapy failure — not a passive bystander. The cleanest finding that would force revision: a well-powered set of clinical trials showing that drugs that successfully remove or normalize a defined TME component — enzymatic degradation of hyaluronic acid, genetic ablation of the dominant CAF subtype, normalization of tumor vasculature — produce no improvement in drug delivery, immune infiltration, or survival across multiple desmoplastic cancers. If dismantling the stroma reliably failed to change outcomes, the "habitat shapes the cancer" thesis would be downgraded from causal driver to correlated epiphenomenon. The early PEGPH20 results in pancreatic cancer — which showed improved drug penetration but equivocal survival benefit — are already a partial warning: the relationship between ECM barrier removal and clinical outcome is more complex than the simple physical barrier model predicts.

## Still Puzzling

- CAFs are heterogeneous and some appear protective — but reliable markers to distinguish tumor-promoting from tumor-restraining CAFs in a living patient do not yet exist. Until they do, "target the CAFs" is dangerously underspecified.
- The tumor microbiome is real, but causation is largely unproven. Are these bacteria drivers of cancer biology, passengers selected by the tumor's conditions, or both — and does it differ by organ?
- Nerve infiltration and β-adrenergic signaling clearly affect tumor biology in models, yet we do not know how much of the "stress and cancer outcomes" literature reflects this mechanism versus confounders. The β-blocker question is genuinely open.
- Why do some hot tumors — full of CD8+ T cells in apparent contact with cancer cells — still resist checkpoint blockade? The immune phenotype framework predicts they should respond, and the exceptions are not fully explained.

## References

- Bissell, M. J., & Radisky, D. (2001). Putting tumours in context. *Nature Reviews Cancer*, 1(1), 46–54.
- Hanahan, D., & Weinberg, R. A. (2011). Hallmarks of cancer: The next generation. *Cell*, 144(5), 646–674.
- Mantovani, A., Marchesi, F., Malesci, A., Laghi, L., & Allavena, P. (2017). Tumour-associated macrophages as treatment targets in oncology. *Nature Reviews Clinical Oncology*, 14(7), 399–416.
- Riquelme, E., et al. (2019). Tumor microbiome diversity and composition influence pancreatic cancer outcomes. *Cell*, 178(4), 795–806.
- Sahai, E., et al. (2020). A framework for advancing our understanding of cancer-associated fibroblasts. *Nature Reviews Cancer*, 20(3), 174–186.

---

## Prompts

### Figure 5.1 — TME cell-component census map
Build a single-panel annotated spatial ecosystem map. Place a central anchor node "Tumor-cell nest" (sky-blue anchor) and surround it with labeled callout populations connected by short leader lines: cancer-associated fibroblasts (abundant, adjacent); T-cell compartment (CD8+ and Tregs); myeloid compartment (TAMs, MDSCs); abnormal vessels with partial pericytes; ECM collagen filling the interstitium; and a bidirectional cytokine-signaling annotation with double-headed arrows between populations. Convey that cancer cells are a minority within a crowded habitat. Use muted secondary fills for stromal/immune/vascular components and the anchor color for the tumor nest. No axes. Subtitle "Cancer cells as a minority in their habitat." Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 5.2 — CAF subtypes and their spatial gradient
Build a radial-zone / spatial-gradient schematic where function tracks distance from the tumor. Innermost reference: tumor-cell border (sky-blue anchor). Moving outward in concentric zones: myCAFs (α-SMA+) closest, building the dense collagen wall (blue = dominant); iCAFs farther out secreting IL-6, CXCL12, LIF (transitional); apCAFs (MHC II+) presenting antigen to T cells (secondary). Annotate each zone with its marker and function via callouts. Encode the proximity ordering explicitly (label radial distance increasing outward). Color encodes subtype role: wall-builder (dominant), immunosuppressive (transitional), antigen-presenting (secondary). Subtitle "Function tracks distance from the tumor." Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 5.3 — ECM remodeling cycle
Build a closed-loop cycle diagram of four stages connected by directional arrows around a ring. Stages: CAFs deposit collagen, fibronectin, hyaluronic acid (sky-blue anchor); stiffness sensed by integrins → YAP/TAZ → proliferation (blue = dominant); proteases release matrix-bound TGF-β, VEGF (green = positive); bioactive matrikines — endostatin, tumstatin, arresten (transitional). Show the loop as a feedback cycle between matrix state and cancer-cell behavior. Color encodes deposition (anchor), mechanosensing (dominant), growth-factor release (positive), matrikine generation (transitional). Subtitle "Matrix as an active signaling reservoir." Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 5.4 — Hot vs excluded vs cold immune phenotypes
Build a three-panel cross-section comparison of tumor immune phenotypes, each panel paired with its checkpoint-inhibitor response. Panel 1 — Hot/inflamed: CD8+ T cells distributed throughout the tumor nests, contacting cancer cells (green = positive) | "Responds." Panel 2 — Excluded: CD8+ T cells dense at a thick collagen margin, absent from the core, collagen band drawn at the border (vermillion = negative) | "Does not respond." Panel 3 — Cold/desert: sparse scattered lymphocytes (vermillion = negative) | "Does not respond." Render T cells as dots and the collagen barrier as a distinct band in the excluded panel. Axis label "T-cell distribution." Color encodes responder (positive) vs non-responder (negative). Subtitle "Phenotype predicts checkpoint-blockade response." Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.
