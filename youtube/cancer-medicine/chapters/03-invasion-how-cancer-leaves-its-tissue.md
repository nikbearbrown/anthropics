# Chapter 3 — Invasion: How Cancer Leaves Its Tissue
*The single cellular crossing that turns a curable lesion into a lethal one.*

Two women are diagnosed with the same cell type in the same organ on the same day. The cells are malignant in both cases. The genetics are nearly identical. Under the microscope you could mix up the slides. One woman will almost certainly be alive in five years. The other may not be.

The difference is not which genes are mutated. It is whether a small number of cells have crossed a membrane.

That is the central fact of invasion biology, and it is worth sitting with before we discuss any molecules: the event that changes a survivable disease into a potentially fatal one is not the accumulation of more mutations, not the growth of a bigger mass, not the recruitment of more blood vessels — it is a single discrete capacity, the capacity to *leave*. Most cancer cells cannot do this. They proliferate, pile on top of each other, fill a duct or a gland, and stay put. A small minority — sometimes a handful in a tumor of millions — acquire the machinery to detach, chew through the barrier in front of them, and crawl into the surrounding tissue. Those cells are what kills patients. Every other cellular event in cancer — the uncontrolled division, the metabolic reprogramming, the immune evasion — matters primarily because it eventually produces, or enables, or is accompanied by, invasion. Understanding what makes a cell mobile is understanding what makes a cancer lethal.

---

### The barrier and what it means to cross it

Most solid cancers arise in **epithelial** tissue — the cells that line surfaces (skin, gut, lung, bladder) and form glands (breast, prostate, pancreas). Epithelial cells are organized, polarized, and stationary. They have a defined apical surface facing the lumen and a basolateral surface anchored to the **basement membrane** — a thin but specialized sheet of type IV collagen, laminin, and nidogen that underlies every epithelium in the body. Epithelial cells are glued to each other by tight junctions and adherens junctions and locked to the basement membrane through integrins. They form sheets. They maintain architecture. Individually motile behavior is not part of their job description.

The basement membrane is not just a structural mat. It is a **signaling boundary** — one side sends one set of messages, the other side sends different ones. Epithelial cells are tuned to the signals from below the basement membrane, not the signals from above it. Cross the membrane, and you are in a different chemical environment. Cross the membrane, and you have *invaded*.

Carcinoma *in situ* — the breast lesion called DCIS, the cervical lesion called CIN, the colonic lesion before it breaks through the muscularis mucosae — means malignant cells filling a compartment but held behind an intact basement membrane. Five-year survival for DCIS approaches 100%. The cells are genetically malignant. They are not clinically lethal. The instant some cells breach that membrane and enter the surrounding stroma, the diagnosis changes, the staging changes, and the survival statistics change.

The job of this chapter is to explain, mechanistically, how a cell acquires the ability to make that crossing — and why it is so hard to stop.

![Breast duct cross-section comparing DCIS with an intact basement membrane against invasive carcinoma where cells breach the membrane and stream into the stroma](images/03-invasion-how-cancer-leaves-its-tissue-fig-01.png)
*Figure 3.1 — Basement-membrane crossing: DCIS vs invasive carcinoma*

<!-- → [DIAGRAM: cross-section of a breast duct — left side showing DCIS (malignant cells filling duct, basement membrane intact), right side showing invasive carcinoma (cells breaching membrane, entering stroma). Label the basement membrane (type IV collagen layer), the in situ cells, the invasive front, and the stromal fibroblasts on the invasive side.] -->

---

### What it takes to invade: three problems to solve

A cancer cell sitting in a mass wants to cross into surrounding tissue. It faces three distinct problems, and it needs solutions to all three at once.

**First: it has to let go.** Epithelial cells are aggressively attached to each other and to the matrix. The molecular glue is **E-cadherin** — a transmembrane protein whose extracellular domain hooks to the E-cadherin on the adjacent cell and whose cytoplasmic tail anchors to the actin cytoskeleton through β-catenin. A cell that has full E-cadherin function cannot meaningfully detach. It is, quite literally, stuck. So before anything else, the cell has to weaken those bonds.

**Second: it has to cut through.** Even after letting go of neighbors, the cell faces the basement membrane and then the dense extracellular matrix of the stroma — a cross-linked web of collagen, laminin, fibronectin, and proteoglycans that is not permeable to a cell-sized object. The cell needs enzymes that degrade this web fast enough to make a path, targeted enough to open a channel rather than just dissolve everything uniformly.

**Third: it has to move.** Crawling through tissue is not passive. It requires a coordinated machinery: protrude the front, grip the new surface, pull the body forward, release the rear. Cells that have never done this before have to reorganize their internal cytoskeleton into something resembling a motility engine.

These three requirements are fulfilled, in many invasive cancers, by a single developmental program that solves all three problems simultaneously. That program is the epithelial-mesenchymal transition.

---

### Epithelial-mesenchymal transition: the cell becomes something else

**Mesenchymal cells** are the antipodes of epithelial cells. A fibroblast, the canonical mesenchymal cell, has no fixed apical-basal polarity, no tight junctions, no sheet organization, and no stable anchorage to a membrane. It migrates. It remodels matrix. It is, constitutively, what an epithelial cell needs to transiently become in order to invade.

The **epithelial-mesenchymal transition (EMT)** is a program in which an epithelial cell sheds its epithelial character and acquires mesenchymal character. This is not a cancer invention. In embryogenesis, EMT is essential and precisely controlled: neural crest cells that will form cranial bone and peripheral neurons migrate from the dorsal neural tube via EMT; the mesoderm of the early embryo is laid down via gastrulation, which requires EMT; heart valves form from endocardial cells that undergo EMT. These are some of the most important cell movements in development. Cancers do not invent EMT — they steal it, reactivating a developmental program that was supposed to be shut down in adult tissue.

The molecular hallmarks track a predictable switch:

| Lost in EMT | Gained in EMT |
|---|---|
| E-cadherin (adherens junction) | N-cadherin (weaker, dynamic) |
| Cytokeratins (epithelial cytoskeleton) | Vimentin (mesenchymal cytoskeleton) |
| Claudins, occludins (tight junctions) | Fibronectin |
| EpCAM | Smooth-muscle actin (context-dependent) |

The loss of E-cadherin is the most consequential single event in this table, and not only because it removes the glue. The cytoplasmic tail of E-cadherin sequesters **β-catenin**. When E-cadherin is lost, β-catenin is released into the cytoplasm and can translocate to the nucleus, where it drives Wnt-pathway transcription of genes that are pro-proliferative and pro-invasive. E-cadherin loss does not just unstick cells from each other — it simultaneously activates a signaling cascade that tells the cell to proliferate and invade. One molecular event, two consequences.

In a minority of cancers, E-cadherin is silenced by direct mutation of the gene *CDH1*: roughly half of lobular breast carcinomas have biallelic *CDH1* inactivation, and germline *CDH1* mutation causes hereditary diffuse gastric cancer. But in the majority of EMT-driven invasion, E-cadherin is not mutated — it is *transcriptionally repressed*. The gene is intact; it is simply not being read. That repression is the work of a small family of transcription factors that function as EMT switches.

![Before/after schematic of the epithelial-mesenchymal transition: a junction-locked epithelial cell loses E-cadherin and becomes a motile mesenchymal cell with vimentin, N-cadherin, and front-back polarity](images/03-invasion-how-cancer-leaves-its-tissue-fig-02.png)
*Figure 3.2 — The epithelial-mesenchymal transition*

<!-- → [DIAGRAM: epithelial cell undergoing EMT — show junction disassembly, E-cadherin loss, β-catenin release and nuclear translocation, acquisition of vimentin and front-back polarization, N-cadherin appearing at the new leading edge. This is a before/after schematic, not a pathway diagram.] -->

---

### The transcription factors that throw the switch

A small number of transcription factors repress E-cadherin and activate mesenchymal gene expression. They are collectively called the EMT transcription factors, and they represent the immediate answer to the question "what turns EMT on in cancer."

**SNAI1 (Snail)** and **SNAI2 (Slug)** are zinc-finger proteins that bind E-box sequences in the *CDH1* promoter and recruit chromatin-modifying complexes — histone deacetylases, the PRC2 complex — to silence the gene. They are among the fastest responders: TGF-β can induce Snail expression within hours, and Snail-mediated E-cadherin repression follows shortly after.

**ZEB1** and **ZEB2** are also zinc-finger E-box-binding factors, and they are the central players in the regulatory architecture that controls the *stability* of the EMT state — which matters enormously, as I will explain in a moment.

**TWIST1** and **TWIST2** are basic helix-loop-helix factors that drive E-cadherin repression in many carcinomas, particularly in aggressive triple-negative breast cancer and in head-and-neck cancers.

These factors are induced by a convergence of signals from the tumor environment: **TGF-β** is the dominant inducer in most contexts, acting through SMAD transcription factors. **Wnt** signaling, through β-catenin, induces EMT transcription factors and is itself potentiated by E-cadherin loss — a positive feedback. **Notch** signaling drives EMT in pancreatic and other carcinomas. Receptor tyrosine kinases — EGFR, MET (the HGF receptor), FGFR, PDGFR — activate EMT through Ras-MAPK and PI3K-AKT signaling. And **hypoxia**, through HIF-1α, induces Twist and other EMT factors — connecting the angiogenesis chapter to this one: the same oxygen deprivation that drives VEGF production also drives invasion.

The word "convergence" here is deliberate. No single pathway drives EMT in cancer; many pathways feed the same downstream factors. This is why EMT is so difficult to block with a single drug — there are too many entry points into the program. And because these signals arrive at different intensities in different cells within the same tumor, different cells transition at different times and to different extents. The result is a heterogeneous population, some cells fully epithelial, some partially transitioned, some more completely mesenchymal. And — here is the counterintuitive finding — the most metastatic cells are *not* the fully mesenchymal ones.

---

### Partial EMT: the spectrum that matters most

The textbook picture of EMT as a binary switch — fully epithelial flips to fully mesenchymal — has been substantially revised. Most cells undergoing EMT in actual tumors achieve only **partial EMT**: they retain some epithelial features (residual E-cadherin, cytokeratin expression) while gaining mesenchymal ones (vimentin, migratory capacity, invasiveness). And the partial-EMT state appears to be the most metastatic.

Why would a *partial* transition be more metastatic than a complete one? Because metastasis is not just invasion — it requires the cell to survive in the bloodstream, arrest in a capillary bed, extravasate, and *re-establish epithelial character* in the new organ to grow a secondary tumor. A cell that is fully locked in the mesenchymal state cannot do that last step. It needs the **plasticity to reverse** — to undergo **mesenchymal-epithelial transition (MET)** and re-epithelialize at the metastatic site. Partial-EMT cells, sitting in an intermediate state, retain that plasticity. They are the ones that successfully complete the full metastatic journey.

The mechanism that enforces these intermediate states and creates the spectrum is an elegantly simple regulatory circuit: the **miR-200/ZEB double-negative feedback loop**.

The microRNA family **miR-200** represses the translation of **ZEB1** and **ZEB2** — it binds their 3' UTRs and prevents their protein from accumulating. ZEB1 and ZEB2, in turn, repress the *transcription* of miR-200. Two mutual repressors. Think about what that topology produces.

A double-negative feedback loop is a **bistable switch**: because each repressor suppresses the other, the system has two stable equilibria — one where miR-200 is high and ZEB is low (the epithelial state, because miR-200 is relieving ZEB's repression of E-cadherin and other epithelial genes), and one where ZEB is high and miR-200 is low (the mesenchymal state, because ZEB is actively repressing E-cadherin and miR-200). Intermediate states are inherently unstable in a pure bistable switch — small perturbations push the system toward one pole or the other.

But this loop is not operating in isolation. It is tuned by the strength of incoming EMT signals. A strong, sustained TGF-β signal keeps the system pushed toward the mesenchymal pole. A weaker or transient signal leaves it in an intermediate zone. Single-cell RNA sequencing of actual tumors reveals many coexisting EMT states — not two, not three, but a continuous distribution across the epithelial-mesenchymal spectrum. The bistable topology explains why cells *tend toward* one state or the other; the varying signal strengths explain why many cells sit in the middle.

![Mutual-repression circuit between miR-200 and ZEB creating epithelial and mesenchymal attractors, with TGF-β pushing toward the mesenchymal pole and the unstable partial-EMT middle marked most metastatic](images/03-invasion-how-cancer-leaves-its-tissue-fig-03.png)
*Figure 3.3 — The miR-200 / ZEB bistable switch*

<!-- → [DIAGRAM: miR-200/ZEB double-negative feedback loop — two nodes (miR-200 and ZEB1/2) with mutual repression arrows. Label the epithelial attractor (high miR-200 / low ZEB) and mesenchymal attractor (low miR-200 / high ZEB). Show a TGF-β arrow pushing the system toward the mesenchymal state. Annotate the partial-EMT zone in the middle as the most metastatic region.] -->

---

### Cutting through: MMP enzymes and why they failed as drug targets

A cell that has undergone EMT and detached from its neighbors still faces the basement membrane. To cross, it needs to degrade type IV collagen — the structural backbone of the membrane. The enzymes that do this are the **matrix metalloproteinases (MMPs)**, a family of 23 zinc-dependent proteases that together can degrade essentially every component of the extracellular matrix.

The key players in basement-membrane breach are the **gelatinases**: **MMP-2** and **MMP-9**, both of which cleave type IV collagen. And **MT1-MMP (MMP-14)**, a membrane-anchored protease that is uniquely important because it is displayed on the cell surface — it degrades matrix *right where the cell is touching it*, and it activates MMP-2 by cleaving its zymogen form.

All MMPs are secreted as inactive zymogens — the active site is blocked by a propeptide domain until a cleavage event removes it. MT1-MMP activates MMP-2 at the cell surface; plasmin and other proteases activate others. Their activity is opposed by **tissue inhibitors of metalloproteinases (TIMPs)** — four of them, each with different affinities for different MMPs. The net matrix degradation at any location in tissue is determined by the **MMP-to-TIMP ratio** at that site.

In tumors, this balance is shifted aggressively toward proteolysis. Cancer cells overexpress MMP-2, MMP-9, and MT1-MMP. Tumor-associated fibroblasts and macrophages — recruited by signals from the cancer cells — also express MMPs, so the protease contribution is not just from the tumor cells themselves but from the entire cellular neighborhood they have restructured. MMP-9 is upregulated in essentially every invasive carcinoma. And MMP-9 does more than cut collagen: it releases growth factors that are stored in latent, matrix-bound form — TGF-β, VEGF, FGF-2 — which then drive further EMT, angiogenesis, and immunosuppression. The protease that opens the path amplifies the signals that produce more invasion. A positive feedback loop written in enzyme activity.

![An invadopodium concentrating MT1-MMP and MMP-2/9 to cleave type IV collagen, opposed by TIMPs with the balance tipped toward proteolysis, releasing matrix-bound TGF-β, VEGF, and FGF-2](images/03-invasion-how-cancer-leaves-its-tissue-fig-04.png)
*Figure 3.4 — Basement-membrane proteolysis at the invadopodium*

<!-- → [FIGURE: invasion through the basement membrane — an invadopodium concentrating MT1-MMP and MMP-2/9 at the cell surface, cleaving type IV collagen, with TIMPs shown opposing and the MMP–TIMP balance tipped toward proteolysis. Include the ECM-bound growth factor release arrow (MMP-9 releasing TGF-β and VEGF).] -->

Given all of this, the pharmaceutical reasoning in the 1990s seemed airtight: MMPs are required for basement-membrane breach; MMP-9 is in every invasive tumor; therefore, inhibit MMPs and stop invasion. Broad-spectrum MMP inhibitors — marimastat, batimastat, prinomastat, others — were developed and taken to phase 3 clinical trials in lung, breast, colorectal, ovarian, and other cancers. *All failed.* No survival benefit. The class was largely abandoned.

What went wrong? Three things, each illuminating a general principle.

First, MMPs are not tumor-specific. They are required for normal tissue homeostasis — wound healing, bone remodeling, immune cell migration, reproductive cycling. Systemic inhibition produces musculoskeletal toxicity: joint pain and stiffness severe enough to limit dosing long before therapeutic concentrations are reached in the tumor.

Second, timing. By the time a patient has clinically detectable cancer — the stage at which these trials enrolled patients — invasion through the basement membrane has already happened. In many cases it happened years before diagnosis. Blocking MMP activity at that point is closing the barn door after every horse has left.

Third, and most instructively for what follows: even in the right patient at the right time, a cancer cell that cannot use MMPs can simply *switch to a different mode of migration*. The cell has options.

---

### Moving: three modes, each a different problem

A cell that has lost epithelial adhesion and opened a path through the matrix still has to physically move. Migration is a coordinated mechanical cycle: the leading edge extends a protrusion driven by actin polymerization, new adhesions form between the protrusion and the matrix, the cell body contracts and pulls forward, the rear detaches and retracts. The **Rho-family GTPases** coordinate it: Cdc42 drives filopodia formation at the leading edge, Rac1 drives the broad flat lamellipodia, RhoA drives actomyosin contraction at the rear. In invasive cancer cells this machinery is hyperactivated, and cells form specialized **invadopodia** — actin-rich protrusions that concentrate MT1-MMP and physically drill through the matrix. Invadopodia are regulated by Src kinase and the Tks5 scaffold, and they are the cellular apparatus that makes invasion possible at the boundary between a cell and the matrix it needs to cross.

But here is the complication for therapy: cancer cells do not use just one mode of migration. Three distinct modes have been documented, each with different dependencies.

**Single-cell mesenchymal invasion** is the classical EMT-driven mode. Lone cells use integrin traction, invadopodia, and secreted MMPs to carve individual paths through the matrix. This mode requires matrix proteolysis and integrin-matrix adhesion. It is the mode most disrupted by MMP inhibitors and integrin-blocking antibodies.

**Amoeboid invasion** requires neither. Cells squeeze through pre-existing gaps and pores in the matrix using high actomyosin contractility — they change shape instead of cutting through barriers. Like an amoeba. This mode is faster than mesenchymal migration, does not depend on MMP activity, and is not disrupted by MMP inhibitors or integrin blockade. A cancer cell blocked from mesenchymal invasion by an MMP inhibitor can, in many cases, shift to amoeboid invasion and keep moving. This is one of the mechanistic explanations for why the broad-spectrum MMP trials failed even if the timing and toxicity problems were set aside.

**Collective invasion** is what actually dominates many of the most common solid tumors. Cohorts of cells move together, maintaining cell-cell contacts. Leader cells at the front acquire partial-EMT features and drive the group forward; follower cells maintain epithelial characteristics. This mode is prominent in breast cancer, colorectal cancer, and head-and-neck cancer. Importantly, circulating clusters of cells — shed from collectively invading groups — are far more efficient at seeding metastases than single cells. A cluster of fifty cells arriving in a capillary bed has a much higher probability of establishing a colony than a single cell does.

These three modes are not fixed properties of a cell. A single tumor can simultaneously employ all three, and individual cells can switch between modes in response to mechanical cues, growth factor gradients, and drug pressure. A therapy that blocks one mode may simply select for cells using another. This is not a deficiency in our understanding — it is a fundamental property of a system that has redundancy built into it by evolution. Neural crest cells, which use EMT and active migration in development, need to be robust to perturbations. The cancer cell is exploiting the robustness of a developmental program.

![Three side-by-side cancer-cell migration modes — single-cell mesenchymal (MMP/integrin-dependent), amoeboid (proteolysis-independent squeezing), and collective leader/follower clusters — each paired with its drug vulnerability](images/03-invasion-how-cancer-leaves-its-tissue-fig-05.png)
*Figure 3.5 — Three modes of cancer-cell migration*

<!-- → [DIAGRAM: three migration modes side-by-side — (1) single-cell mesenchymal: lone cell with invadopodia and MMP activity; (2) amoeboid: cell squeezing through gap without proteolysis; (3) collective: cluster with leader/follower cells, leader showing partial EMT markers. Label the drug-vulnerability of each mode: MMPs/integrins vulnerable in mode 1, neither required in mode 2, complex in mode 3.] -->

---

### What the cell has done, and what it still has to do

By the end of invasion, a cancer cell has accomplished something developmentally extraordinary. It has activated a program — EMT — that was last used in embryogenesis. It has reorganized its cytoskeleton, shed its epithelial identity, weakened its junctions, and acquired polarity suited for movement rather than for sheet integrity. It has recruited or stimulated a local proteolytic environment that cleared a path through the matrix. And it has physically crawled out of the primary mass and into the surrounding stroma.

That is invasion. It is not yet metastasis.

The cell is now in the stroma — but it needs to reach a blood or lymphatic vessel, survive the transit, extravasate at a distant site, and re-establish a colony. Each of those steps has its own molecular logic and its own failure modes. Most cells that successfully invade never become metastases. The process is enormously inefficient — a large primary tumor sheds millions of cells into the circulation daily, and most of them die before doing anything.

The reason to understand invasion with this precision is not only that it is scientifically elegant — which it is — but that every failure in the anti-invasion therapeutic program has been a failure of incomplete mechanistic understanding. MMP inhibitors failed because their developers did not adequately account for where else the enzymes were needed, when in the disease their action would matter, and what the cell would do when one route was blocked. A therapy that accounts for all three of those considerations does not yet exist. Building it requires understanding what this chapter has tried to lay out: the three problems the cell must solve, the multiple programs it can use to solve each one, and the redundancy baked into every step.

---

## Exercises

**Warm-up**

1. *(Recall — difficulty: low)* State in one sentence the single molecular event that distinguishes invasive carcinoma from carcinoma *in situ*, and name the specific structural barrier involved. *What this tests: whether you can distinguish bulk from barrier-crossing as the defining event.*

2. *(Recall — difficulty: low)* Name two molecular markers lost during EMT and two gained, and identify which single lost marker has a secondary signaling consequence beyond loss of cell-cell adhesion. *What this tests: familiarity with the EMT marker table and E-cadherin's dual role.*

3. *(Recall — difficulty: low)* What is the MMP–TIMP balance, and in which direction is it shifted in an invasive tumor? *What this tests: the basic proteolytic framework before the drug-target reasoning is applied.*

**Application**

4. *(Apply — difficulty: medium)* A breast tumor biopsy shows loss of E-cadherin protein with no mutation in the *CDH1* gene sequence. Propose the most likely mechanism of E-cadherin silencing, name two transcription factors capable of mediating it, and explain what happens to the β-catenin that is released from the disassembled junctions. *What this tests: transcriptional versus mutational silencing, EMT factor identity, and the dual role of E-cadherin.*

5. *(Apply — difficulty: medium)* A patient's tumor is treated with a potent, selective MT1-MMP inhibitor, yet invasion continues in 3D culture assays. Propose a specific migration mode that would explain continued invasion without MMP activity, and describe the cytoskeletal mechanism it uses instead. *What this tests: migration-mode diversity and the limits of protease-targeted therapy.*

6. *(Apply — difficulty: medium)* A drug company proposes treating early-stage DCIS patients with a broad-spectrum MMP inhibitor to prevent progression to invasive carcinoma. Assess whether the two most-cited problems with MMP inhibition in previous trials (toxicity and timing) would still apply in this population, and state whether the rationale is improved relative to the advanced-disease trials. *What this tests: application of the failure-mode analysis to a different disease setting.*

**Synthesis**

7. *(Synthesize — difficulty: high)* Draw or describe the miR-200/ZEB double-negative feedback loop. Label the two stable attractors. Then: (a) explain what "bistability" means in this context and why the loop topology produces it, and (b) explain why partial-EMT cells — sitting between the two attractors — are more metastatic than fully mesenchymal cells, invoking the MET step required at the distant site. *What this tests: regulatory circuit logic, bistability, and the connection between invasion plasticity and metastatic efficiency.*

8. *(Synthesize — difficulty: high)* A cancer cell in a hypoxic, TGF-β-rich microenvironment activates HIF-1α. Trace the molecular chain from HIF-1α activation to (a) E-cadherin repression via an EMT transcription factor, and (b) matrix degradation via MMP-9. At each step, name the intermediate factor. Then explain what positive feedback loop connects MMP-9 activity back to further EMT signaling. *What this tests: integration of hypoxia, EMT, and proteolysis as a convergent system.*

**Challenge**

9. *(Challenge — difficulty: high)* Design a hypothetical combination therapy targeting invasion that addresses the three failure modes of the historical MMP inhibitor trials: normal-tissue toxicity, timing, and migration-mode switching. For each failure mode, specify a mechanistic approach that addresses it, name a molecular target, and identify one predicted resistance mechanism the combination might still face. There is no single correct answer; the goal is mechanistically coherent reasoning. *What this tests: integrative thinking about target selection, therapeutic windows, and resistance anticipating the next chapter on metastasis.*

---

## Prompts

### Figure 3.1 — Basement-membrane crossing: DCIS vs invasive carcinoma
Build a two-panel cross-section comparison of a breast duct: left "Carcinoma in situ (DCIS)," right "Invasive carcinoma," aligned as matched rows. Row pairs: intact continuous basement membrane (sky-blue anchor) vs membrane breached at one point; malignant cells confined to duct lumen vs cells streaming through the gap (vermillion = negative); clean stroma vs cells entering surrounding stroma (negative); no invasive front vs stromal fibroblasts at the invasive front (secondary). Draw the basement membrane as a distinct continuous line on the left and a broken line on the right, with cells crossing. Color encodes intact (anchor) vs breached/invading (negative). Axis label "Breast duct cross-section." Subtitle "The breach that turns curable into lethal." Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 3.2 — The epithelial-mesenchymal transition
Build a left-to-right three-stage process flow with arrows between stages. Stage 1: epithelial cell with junctions + E-cadherin and apical-basal polarity (sky-blue anchor). Stage 2: junctions disassemble, E-cadherin lost, β-catenin translocates to nucleus (secondary), with the arrow into it labeled "EMT." Stage 3: mesenchymal cell with leading edge, vimentin, N-cadherin (vermillion = negative, the motile invasive end). Render each stage as a labeled cell glyph showing the marker change. Add an annotation note: "E-cadherin loss frees β-catenin → nucleus → Wnt transcription." Color encodes epithelial (anchor) → transitional → mesenchymal (negative). Subtitle "From junction-locked epithelial to motile mesenchymal." Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 3.3 — The miR-200 / ZEB bistable switch
Build a node-edge systems diagram of a double-negative mutual-repression loop. Two primary nodes facing each other: "miR-200 (epithelial attractor)" (sky-blue anchor) and "ZEB1/2 (mesenchymal attractor)" (vermillion = negative), connected by two opposing block-tipped (flat-bar) edges labeled "miR-200 inhibits ZEB" and "ZEB inhibits miR-200." Add an input node "TGF-β input" (secondary) with an arrow to a central transitional ridge node "Partial-EMT ridge (most metastatic)," labeled "pushes toward mesenchymal pole." Optionally underlay a shallow double-well attractor landscape behind the two poles with the unstable middle highlighted. Color encodes epithelial pole (anchor), mesenchymal pole (negative), metastatic middle (transitional). Subtitle "A double-negative loop with a metastatic middle." Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 3.4 — Basement-membrane proteolysis at the invadopodium
Build a left-to-right localized-mechanism flow with a balance element. Stage 1: type IV collagen basement membrane as the barrier (sky-blue anchor). Stage 2: invadopodium concentrating MT1-MMP + MMP-2/9 (vermillion = negative, the proteolytic apparatus). Stage 3: TIMPs oppose via a block-tipped edge labeled "TIMP restraint," with the MMP–TIMP balance tipped toward proteolysis (secondary). Stage 4: matrix cleaved, releasing TGF-β, VEGF, FGF-2 (secondary), edge labeled "release." Render the invadopodium drilling through the collagen line. Add a note: "Released growth factors feed back to drive further EMT and invasion (positive feedback)." Color encodes barrier (anchor) vs protease (negative) vs balance/release (secondary). Subtitle "Proteases drill the barrier and release growth factors." Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 3.5 — Three modes of cancer-cell migration
Build a three-panel side-by-side comparison pairing each migration mode with its drug vulnerability. Panel rows: single-cell mesenchymal — invadopodia cut a channel via MMP/integrin (vermillion = negative) | "Vulnerable to MMP inhibitors / integrin blockers"; amoeboid — rounded cell squeezes through gaps, no MMP use (transitional) | "Not blocked by MMP/integrin agents"; collective — leader (partial-EMT) + follower cohort (sky-blue anchor) | "Complex/mixed; seeds metastases efficiently." Render a distinct cell glyph per mode (lone cell with protrusions; rounded cell in a pore; leader-follower cluster). Color encodes mode behavior; left column = mode, right column = vulnerability. Axis label "Mode vs vulnerability." Subtitle "Switching modes defeats single-mode therapy." Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.
