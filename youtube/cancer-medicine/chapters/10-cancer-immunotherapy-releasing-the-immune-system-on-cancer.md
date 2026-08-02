# Chapter 10 — Cancer Immunotherapy: Releasing the Immune System on Cancer

The drugs that saved the man in the opening case never touched his cancer cells. They touched his T cells — specifically, they removed a molecular brake that his tumor had been pressing to keep his T cells from killing it. The tumor shrank because his own immune system, finally released, attacked it. He developed colitis, thyroiditis, and hepatitis along the way, because releasing a brake on T cells does not produce selective tolerance of cancer cells and nothing else; it produces a broader reactivation of immune activity that happens to include normal tissues. The inflammation and the tumor response were not unrelated events. They were the same mechanism operating in different places at the same time.

This is the strange logic of cancer immunotherapy: treat the immune system, not the cancer, and pay for efficacy in autoimmunity. Understanding why this works — and why it works for some patients and not others — requires starting with how T cells are normally controlled.

---

## The brake, and why it exists

A T cell needs two signals to activate. The first is antigen: a peptide fragment from a foreign protein, presented in an MHC complex on an antigen-presenting cell, binding the T-cell receptor. This provides specificity — it tells the T cell what to recognize. The second is co-stimulation: the receptor CD28 on the T cell binding CD80 or CD86 on the antigen-presenting cell. This provides authorization — it tells the T cell the context is right to proceed. A T cell that receives signal one without signal two does not activate; it goes anergic, effectively silenced. The requirement for two simultaneous confirmations is a safeguard against autoimmunity.

**Immune checkpoints** are inhibitory receptors that, when engaged, dampen or terminate T-cell activation. They are brakes, and they serve an essential purpose: preventing activated T cells, once they leave the lymph node and enter peripheral tissue, from attacking healthy tissue indiscriminately. Remove the brakes entirely and the result is autoimmune disease. The brakes are not a design flaw. They are necessary.

The therapeutic insight, which won James Allison and Tasuku Honjo the 2018 Nobel Prize, is that tumors have learned to press these same brakes. The immune system is not blind to cancer — it generates T cells that recognize tumor antigens and are capable of killing tumor cells. What the tumor does is engage the checkpoints to shut those T cells down before they can do their work. Block the checkpoint, and the T cells can kill again. You are not giving the immune system new capabilities; you are removing an obstacle the tumor installed.

---

## Two checkpoints, two points in the cycle

The two checkpoints at the center of current therapy are not redundant. They operate at different steps.

**CTLA-4** — cytotoxic T-lymphocyte-associated protein 4 — appears on activated T cells and on regulatory T cells. It competes with CD28 for the same binding sites on CD80 and CD86, and it binds with higher affinity, effectively stealing signal two. Its dominant effect is at *priming* — in the lymph node, before any T cell has left for the tumor. CTLA-4 sets the threshold for which T cells get activated in the first place. James Allison's group showed in 1996 that blocking CTLA-4 with an antibody caused established tumors to regress in mice — the founding experiment of the field. The logic is simple: lower the activation threshold, and more anti-tumor T cells get licensed to act.

**PD-1** — programmed death-1 — appears on activated and *exhausted* T cells. Its ligand, **PD-L1**, is expressed broadly: on tumor cells, on tumor-associated macrophages, and notably on cells in response to the very interferon-gamma that infiltrating T cells produce. The tumor's T cells announce their presence through interferon, and the tumor responds by upregulating the molecule that shuts them off. PD-1 engagement inhibits T-cell effector function in *peripheral tissue* — inside the tumor, late in the process, at the killing step rather than the priming step. Tasuku Honjo identified PD-1 in 1992; the receptor-ligand axis was later shown to be a dominant tumor escape mechanism across many cancer types.

The practical consequence of this distinction: blocking CTLA-4 widens the pool of T cells that get activated. Blocking PD-1 or PD-L1 lets T cells that are already primed, already infiltrating the tumor, keep killing once they get there. Block both, and you attack the cycle at two separate points — which is why the combination is more potent and, inevitably, more toxic than either alone.

![CTLA-4 brakes priming in the lymph node; PD-1 brakes killing in the tumor](images/10-cancer-immunotherapy-releasing-the-immune-system-on-cancer-fig-01.png)
*Figure 10.1 — CTLA-4 vs. PD-1: two checkpoints, two sites*

<!-- → [DIAGRAM: checkpoint blockade mechanism — CTLA-4 stealing CD80/86 from CD28 during priming in the lymph node, versus PD-1 engaging PD-L1 to shut down killing in the tumor; antibodies blocking each] -->

---

## What happened in the clinic

Ipilimumab, the anti-CTLA-4 antibody, was approved in 2011 for metastatic melanoma — the first checkpoint inhibitor and the first drug ever to extend overall survival in that disease. Response rates were modest, roughly 15 to 20 percent. But the patients who responded often stayed in response. The survival curve developed a "tail" — a flat portion indicating that some fraction of patients were alive years later with no further therapy, in durable remission that looked, for practical purposes, like cure. This was new. Prior melanoma drugs had occasionally shrunk tumors; none had produced durable remissions at meaningful rates.

Anti-PD-1 antibodies — nivolumab and pembrolizumab — followed in 2014 with higher response rates and a somewhat more manageable toxicity profile. The combination of ipilimumab and nivolumab in melanoma raised response rates to around 60 percent and five-year survival above 50 percent, at the cost of grade 3–4 immune-related toxicity in roughly half of patients. Checkpoint blockade now has FDA approvals across more than twenty cancer types, including a tumor-agnostic approval — the first in oncology — for any solid tumor with high microsatellite instability, regardless of where it started.

But response is deeply uneven. Hodgkin lymphoma responds in 65 to 75 percent of patients. Melanoma responds in 30 to 45 percent with single-agent anti-PD-1. Pancreatic cancer and microsatellite-stable colorectal cancer respond in under 5 percent. The pattern is not random.

![Checkpoint-blockade response rates by tumor type, from ~70% in Hodgkin lymphoma to under 5% in pancreatic and MSS colorectal cancer](images/10-cancer-immunotherapy-releasing-the-immune-system-on-cancer-fig-04.png)
*Figure 10.4 — Checkpoint-blockade response rates by tumor type*

---

## Hot and cold, and why the distinction determines everything

Checkpoint blockade releases brakes on T cells that are already present and primed. If those T cells were never there, releasing the brake does nothing. This is the central constraint of the approach, and it maps onto a framework that turns out to predict response better than tumor type alone.

A **hot tumor** has three features: high mutational burden (meaning many neoantigen peptides for T cells to recognize), high PD-L1 expression (meaning the tumor is actively pressing the PD-1 brake — so there is a brake to release), and dense CD8+ T-cell infiltration (meaning the T cells are already in the tumor). Microsatellite-instability-high tumors are hot because defective mismatch repair produces thousands of mutations, each a potential neoantigen. Hodgkin lymphoma is hot for reasons specific to its biology. These are the cancers checkpoint blockade helps most.

A **cold tumor** has few mutations, no PD-L1, and almost no T cells inside. Pancreatic ductal adenocarcinoma is cold partly because it has a dense desmoplastic stroma that physically excludes T cells, partly because its mutational burden is low, and partly because it has active immunosuppressive mechanisms beyond PD-L1. Releasing a PD-1 brake in a tumor that has no T cells and no PD-L1 is pressing a release on a brake that was not engaged, in a car that has no engine running.

![Hot tumor with dense T-cell infiltration and PD-L1 versus cold tumor with no infiltrate and a stromal wall](images/10-cancer-immunotherapy-releasing-the-immune-system-on-cancer-fig-02.png)
*Figure 10.2 — Hot vs. cold tumors*

The hot/cold framework is not binary — tumors fall on a spectrum — and the framework predicts populations better than individuals. Some PD-L1-negative tumors respond; some PD-L1-positive tumors do not. The biomarkers are imperfect proxies for a complex immune state. But the framework is mechanistically grounded and clinically useful: it identifies the right question, which is not "how dangerous is this tumor?" but "are primed, tumor-reactive T cells present and being suppressed?"

Combination strategies for cold tumors follow from the same logic. Chemotherapy can kill cancer cells immunogenically, releasing antigen and potentially recruiting T cells. Radiation can do the same. Anti-angiogenic agents normalize tumor vasculature and relieve the VEGF-driven immunosuppression that contributes to T-cell exclusion. Each combination strategy is chosen by mechanism: what the first agent leaves open, the second closes.

---

## CAR-T: a different approach to the same problem

Checkpoint blockade requires pre-existing anti-tumor T cells. When they do not exist or cannot be generated, a different approach becomes relevant: remove a patient's T cells, rebuild them with new targeting capability, and return them.

The dominant form is **CAR-T** — chimeric antigen receptor T cells. A patient's T cells are collected by apheresis, engineered with a gene encoding an artificial receptor, expanded in culture, and reinfused. The chimeric antigen receptor combines an antibody-derived binding domain — which recognizes a surface protein on cancer cells — fused to intracellular T-cell signaling domains that trigger killing when the receptor engages its target. The recognition is direct, without MHC presentation.

That last point is more than a technical detail. It means CAR-T bypasses several evasion mechanisms: it does not require MHC class I on the cancer cell (so tumors that have downregulated MHC to hide from normal T cells are still vulnerable), it does not require professional antigen presentation, and it does not require the normal priming machinery. The T cell's new receptor is the equivalent of a new sensory organ, purpose-built to find one specific target.

![CAR-T pipeline: collect, engineer, expand, reinfuse, and kill the CD19+ target](images/10-cancer-immunotherapy-releasing-the-immune-system-on-cancer-fig-03.png)
*Figure 10.3 — CAR-T workflow*

<!-- → [DIAGRAM: CAR-T workflow — leukapheresis, genetic engineering of the chimeric receptor, ex vivo expansion, reinfusion, and direct MHC-independent killing of a CD19+ cell] -->

In CD19-positive B-cell acute lymphoblastic leukemia, tisagenlecleucel produced complete-response rates around 80 percent in heavily pretreated children who had no remaining options. Anti-CD19 and anti-CD22 products for lymphoma, and anti-BCMA products for multiple myeloma, followed. These are among the most dramatic responses in oncology.

---

## Why CAR-T stalls at solid tumors

The success in B-cell malignancies reflects a confluence of favorable conditions that solid tumors do not share.

CD19 is expressed on essentially all malignant B cells, so there is no antigen-negative escape subclone. It is also on normal B cells — but losing your normal B cells is survivable; immunoglobulins can be replaced, and the on-target/off-tumor toxicity is acceptable. And B-cell cancers are in the blood and lymphoid organs, physically accessible to the infused T cells.

Solid tumors violate each of these conditions. Antigen expression is heterogeneous — one region of the tumor may express the target at high levels, another barely at all, and a CAR directed at one target will simply miss the negative cells. Few solid-tumor antigens are truly cancer-specific rather than cancer-associated; candidate targets are typically also expressed on critical normal tissue, making on-target/off-tumor toxicity severe or fatal. And the solid-tumor microenvironment — dense extracellular matrix, hypoxia, nutrient depletion, and a complex network of immunosuppressive cells and signals — physically impedes infiltration and exhausts the T cells that manage to get in.

No CAR-T product for a solid tumor is yet approved, and this is not for lack of effort. The three obstacles are real and, at present, unsolved. Dual-target CARs address heterogeneity partially; armored CARs that secrete their own cytokines attempt to survive the microenvironment; synthetic biology approaches try to make T cells that degrade the matrix. Each strategy addresses one of the three obstacles and leaves the others standing.

CAR-T carries its own distinctive toxicities. Cytokine release syndrome — a flood of cytokines from massively activated cells — causes fever, hypotension, and hypoxia, treated with the anti-IL-6-receptor antibody tocilizumab. Immune effector cell-associated neurotoxicity syndrome causes confusion, aphasia, and in severe cases seizures. Both are predictable, manageable in specialized centers, and acceptable given the benefit in approved indications.

---

## Other cellular strategies, and what they share

TIL therapy — expanding a patient's own tumor-infiltrating lymphocytes and reinfusing them — was approved in 2024 for melanoma. The cells are already tumor-reactive; the therapy provides numbers and reactivation. TCR-T engineering inserts a T-cell receptor with MHC-restricted recognition of a specific peptide, allowing targeting of intracellular antigens that surface-targeting CARs cannot reach.

Personalized neoantigen vaccines sequence a patient's tumor, identify its unique mutant peptides, manufacture a vaccine — peptide or mRNA — and administer it to prime T cells against those specific targets. A randomized trial of an mRNA neoantigen vaccine combined with pembrolizumab improved recurrence-free survival over pembrolizumab alone in melanoma. The pairing is mechanistically natural: the vaccine generates new anti-tumor T-cell responses, and the checkpoint inhibitor prevents the tumor from shutting those responses down once they arrive. One component addresses the cold-tumor problem — insufficient T cells — and the other addresses the suppression problem. Together they cover both steps.

---

## What the toxicity tells you about the mechanism

The immune-related adverse events of checkpoint blockade — colitis, hepatitis, pneumonitis, thyroiditis, hypophysitis — are not collateral damage from a drug that also happens to be useful. They are the mechanism operating in normal tissue.

Blocking CTLA-4 or PD-1 does not produce selective tolerance of cancer cells. It produces a broader reactivation of T-cell surveillance that eliminates the brake everywhere it was engaged — in the tumor and in normal tissues that the same T cells would otherwise have left alone. The patient in the opening case whose gut inflamed and whose thyroid shut down was experiencing the same drug action as the patient whose liver metastases shrank. The anti-tumor T cells and the self-reactive T cells were both released.

This has a corollary worth stating explicitly: patients who develop immune-related adverse events tend, on balance, to have better tumor responses. The correlation is imperfect and the relationship is not one you would deliberately aim for clinically — severe colitis is managed aggressively with corticosteroids, and treatment is paused or stopped. But mechanistically, the association makes sense. A patient whose immune system responds to the released brake in the gut and thyroid is a patient whose immune system is responding to the released brake. The two events are not unrelated. They are the same event in different tissues.

---

## What would change this picture

The chapter's central claim is that checkpoint blockade works by releasing brakes on pre-existing, primed anti-tumor T cells — which is why infiltrated, high-mutation tumors respond and T-cell-poor, low-mutation tumors do not. The finding that would force revision: durable checkpoint-blockade responses at meaningful rates in tumors verified before treatment to have no neoantigen-specific T cells anywhere in the patient, no tumor infiltrate, and no PD-L1 — indistinguishable response rates from hot tumors. If responses did not require a pre-existing T-cell response, the "release the brake on T cells already there" model would need a different mechanism: the antibodies would have to generate anti-tumor immunity de novo. The correlational evidence makes this unlikely, but a clean contradicting result would break the framework.

---

## Still open

Why do some patients sustain remission for a decade after stopping therapy while others with apparently identical tumors and immune phenotypes relapse? The determinants of the durable flat tail on the survival curve are not understood, and understanding them would change how long treatment continues and who gets combination versus single-agent therapy.

Can a cold tumor be reliably converted to hot? Radiation, chemotherapy, oncolytic viruses, intratumoral injections, and microbiome manipulation have all been proposed and tested. No generally applicable, predictable method exists. This is not for lack of effort.

Whether immune-related adverse events and anti-tumor response are mechanistically separable — whether a drug or schedule exists that produces one without the other — is genuinely unresolved. The correlation argues they share a mechanism; the imperfection of the correlation leaves open the possibility that they can be uncoupled.

And why CAR-T's apparent advantage of MHC-independent killing has not translated to solid tumors remains partly unclear. Is the microenvironment the dominant barrier, or is antigen heterogeneity the deeper problem? Answering that question would tell you whether engineering better T cells is the right investment, or whether the tumor environment needs to be changed first.

---

## LLM Exercises

1. **(Two checkpoints)** Explain why blocking CTLA-4 and blocking PD-1 are not redundant. Locate each checkpoint's dominant effect in the cancer-immunity cycle — priming versus killing — and predict, from mechanism, why the combination is both more effective and more toxic than either alone.

2. **(Hot and cold)** Patient 1's tumor has high mutational burden, strong PD-L1 staining, and dense CD8+ T-cell infiltration. Patient 2's tumor has low mutational burden, no PD-L1, and almost no T cells inside. Both are offered single-agent anti-PD-1. For each patient, predict the likelihood of response and explain the mechanism behind your prediction. For the patient unlikely to respond, propose a rationally designed combination strategy and name the specific problem each component addresses.

3. **(CAR-T design)** A solid tumor expresses a candidate antigen at high levels on average but with significant cell-to-cell variability. Before designing a CAR-T against it, identify the three major obstacles this tumor type presents, and for each, describe one specific piece of evidence you would gather about this antigen and this tumor to estimate whether the obstacle is surmountable.

4. **(Toxicity and mechanism)** A patient starting ipilimumab plus nivolumab develops grade 2 colitis at week six. Their oncologist is considering stopping both drugs. Write the argument for continuing treatment with corticosteroid management rather than stopping, grounding it in what the colitis reveals about the mechanism of action. Then write the argument for stopping. State which decision you would make and what additional information would change it.

5. **(Vaccine combination)** Personalized neoantigen vaccines are tested in combination with checkpoint inhibitors rather than alone. Using the cancer-immunity cycle, construct the mechanistic argument for the combination: name the step each component addresses, explain why each component is insufficient alone, and predict what feature of a patient's tumor would most increase the benefit of adding the vaccine to pembrolizumab.

---

## References

- Hodi, F. S., O'Day, S. J., McDermott, D. F., et al. (2010). Improved survival with ipilimumab in patients with metastatic melanoma. *New England Journal of Medicine*, 363(8), 711–723.
- Ishida, Y., Agata, Y., Shibahara, K., & Honjo, T. (1992). Induced expression of PD-1, a novel member of the immunoglobulin gene superfamily, upon programmed cell death. *EMBO Journal*, 11(11), 3887–3895.
- Leach, D. R., Krummel, M. F., & Allison, J. P. (1996). Enhancement of antitumor immunity by CTLA-4 blockade. *Science*, 271(5256), 1734–1736.
- Maude, S. L., Frey, N., Shaw, P. A., et al. (2014). Chimeric antigen receptor T cells for sustained remissions in leukemia. *New England Journal of Medicine*, 371(16), 1507–1517.
- Weber, J. S., Carlino, M. S., Khattak, A., et al. (2024). Individualised neoantigen therapy mRNA-4157 (V940) plus pembrolizumab versus pembrolizumab monotherapy in resected melanoma (KEYNOTE-942). *The Lancet*, 403(10427), 632–644.

---

## Prompts

### Figure 10.1 — CTLA-4 vs. PD-1: two checkpoints, two sites
Build a two-panel comparative mechanistic schematic placing each checkpoint at its site of action. Left panel "CTLA-4 (priming, lymph node)": an APC–T cell interface where CTLA-4 outcompetes CD28 for CD80/86 (vermillion, blocking), so signal 2 is blocked and priming fails; an anti-CTLA-4 antibody restores priming (green, positive). Right panel "PD-1 (killing, tumor)": a tumor cell–T cell interface where PD-1 engages PD-L1 (vermillion, blocking), shutting down the effector T cell; an anti-PD-1/PD-L1 antibody restores killing (green, positive). Use four aligned rows: interface, blocking interaction, consequence, antibody rescue. Marks: receptor–ligand contact glyphs, blocking and restoring annotations, antibody symbols. Color semantics (Okabe-Ito): vermillion = the inhibitory brake, green = antibody-restored function, sky-blue = the T cell as anchor. Structural, no axis. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 10.2 — Hot vs. cold tumors
Build a two-panel contrasting tumor cross-section schematic. Left panel "Hot tumor": dense interior CD8+ T-cell infiltration (green, positive), high mutational burden, high surface PD-L1 density (sky-blue, anchor), no stromal wall. Right panel "Cold tumor": near-zero interior T cells, few mutation markers, little/no PD-L1, and a desmoplastic stroma wall excluding T cells (vermillion, negative). Draw each tumor as a rounded cross-section with scatter glyphs for T cells (dense left, absent right), surface PD-L1 ticks, and a stromal border ring on the right only. Use four aligned comparison rows: T-cell density, mutational burden, PD-L1, stromal wall. Marks: cross-section regions, T-cell dots, surface PD-L1 marks, stromal ring. Color semantics (Okabe-Ito): green = T-cell infiltration, sky-blue = PD-L1 anchor, vermillion = excluding stroma. No axis. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 10.3 — CAR-T workflow
Build a horizontal five-step flowchart of the CAR-T pipeline. Steps left to right: (1) "Leukapheresis: collect patient T cells" (secondary); (2) "Engineer with chimeric antigen receptor" (sky-blue, anchor); (3) "Ex vivo expansion: one → many" (green, positive) — show a single cell multiplying; (4) "Reinfusion into patient"; (5) "MHC-independent killing of CD19+ target" (vermillion). Connect steps with four rightward arrows. Add a note: "The chimeric receptor binds the target directly, bypassing MHC presentation." Marks: labeled step nodes, a multiplication motif at step 3, a receptor-on-T-cell glyph at steps 2 and 5, four flow arrows. Color semantics (Okabe-Ito): sky-blue = the engineering anchor step, green = expansion/positive, vermillion = the killing step. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 10.4 — Checkpoint-blockade response rates by tumor type
Build a vertical bar chart of single-agent checkpoint-blockade objective response rates across four tumor types. Bars: Hodgkin lymphoma 70% (blue, dominant, highlighted), Melanoma (single-agent anti-PD-1) 38% (secondary), Pancreatic cancer 4%, MSS colorectal cancer 4%. Y-axis "objective response rate (%)" starting at zero (zero baseline required), 0–80 range. Sort bars descending by value. Label each bar with its value. Optionally add a faint reference annotation noting these track the hot/cold spectrum (Hodgkin/melanoma hot, pancreatic/MSS-CRC cold). Marks: rectangular bars, value labels, category axis. Color semantics (Okabe-Ito): blue = the dominant highest responder, secondary hue = melanoma, neutral gray = the low-responding cold tumors. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.
