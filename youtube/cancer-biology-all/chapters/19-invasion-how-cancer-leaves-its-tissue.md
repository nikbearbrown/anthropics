# Chapter 19 — Invasion: How Cancer Leaves Its Tissue


## TL;DR

- This chapter gives a working overview of Invasion: How Cancer Leaves Its Tissue, focusing on the ideas a reader needs before moving to the next chapter.
- The chapter moves through Epithelial-mesenchymal transition, The EMT transcription factors, Partial EMT and the EMT spectrum, Matrix metalloproteinases and ECM degradation, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

A localized cancer is curable. Almost any localized cancer.

Hold that observation. A breast tumor in the breast can be cut out. A lung tumor in the lung can be resected. A prostate tumor in the prostate can be removed or radiated. The five-year survival rates for stage I cancers across most cancer types are 80 to 95 percent. The same cancers, once they have spread to distant organs, are usually incurable. Stage IV breast cancer: about 30 percent five-year survival. Stage IV colorectal cancer: about 14 percent. Stage IV pancreatic cancer: under 3 percent.

What separates stage I from stage IV is not just biological progression. It is a discrete cellular capacity — the ability to *invade* through tissue barriers and ultimately *metastasize* to distant sites. Most cancer cells, in any tumor, cannot do this. They proliferate, they pile up, they form a mass, but they stay where they are. A small minority — sometimes a handful of cells in a tumor of ten million — acquire the capacity to detach, to migrate through surrounding tissue, to enter the bloodstream, to survive in circulation, to exit into a distant tissue, and to grow there. That small minority is what kills patients.

This is the first of two chapters on invasion and metastasis. This one — 13A — covers invasion: how a cancer cell escapes its tissue of origin. The epithelial-mesenchymal transition (EMT) that gives cells migratory capacity. The matrix metalloproteinases that chew through extracellular matrix. The cytoskeletal reorganization that lets cells crawl through tissue. The molecular signaling that drives the whole transformation. The next chapter — 13B — covers the metastatic cascade beyond local invasion: circulating tumor cells, organ-specific seeding patterns, the "seed and soil" hypothesis, and the molecular basis of organotropism.

Hold the question that organizes the chapter: *what makes a cancer cell mobile?*

---

## Epithelial-mesenchymal transition

Most solid cancers arise from *epithelial* tissue — the cells that line surfaces (skin, gut, lung) and form glandular organs (breast, prostate, pancreas). Epithelial cells are organized, polarized, and stationary. They have a defined *apical* surface (facing the lumen or outside) and a defined *basolateral* surface (facing other cells and the basement membrane). They are tightly attached to each other through *tight junctions*, *adherens junctions*, and *desmosomes*. They are attached to the basement membrane through *integrins* and *hemidesmosomes*. They form sheets that maintain organ architecture.

Mesenchymal cells are different. They are loose, motile, and individually mobile. They lack the strict apical-basal polarity of epithelial cells. They make extracellular matrix rather than attaching to organized basement membranes. Fibroblasts, the canonical mesenchymal cell type, can migrate through tissue, deposit collagen, and reorganize the matrix around them.

The *epithelial-mesenchymal transition (EMT)* is a developmental program by which an epithelial cell loses its epithelial characteristics and acquires mesenchymal ones. EMT is essential in normal development — gastrulation during embryogenesis, neural crest cell migration, heart valve formation, secondary palate development, all involve EMT. The cells that will become mesenchymal-derived tissues (much of the connective tissue, skeletal system, smooth muscle) start as epithelial cells in the early embryo and undergo EMT to become migratory.

Cancers reactivate EMT inappropriately. A cancer cell that has acquired the molecular changes of EMT loses its epithelial characteristics — its cell-cell junctions weaken or disassemble, its polarity is lost, its cytoskeleton reorganizes — and gains mesenchymal characteristics including migratory capacity. The cell can then detach from the tumor mass and invade.

The classical molecular markers of EMT:

*Epithelial markers (lost in EMT)*:
- E-cadherin (the dominant adhesion protein of epithelial adherens junctions)
- Cytokeratins (intermediate filament proteins of epithelial cytoskeleton)
- Claudins and occludins (tight junction proteins)
- ZO-1 (zonula occludens, tight junction scaffold)
- EpCAM (epithelial cell adhesion molecule)

*Mesenchymal markers (gained in EMT)*:
- N-cadherin (replaces E-cadherin; mediates weaker, more dynamic adhesion)
- Vimentin (mesenchymal intermediate filament)
- Fibronectin (extracellular matrix protein)
- Smooth muscle actin (in some EMT contexts)

The most consequential single change is *loss of E-cadherin*. E-cadherin is the molecular glue that holds epithelial cells in their organized sheets. Its cytoplasmic domain binds β-catenin, which links to the actin cytoskeleton through α-catenin. When E-cadherin is lost — through gene mutation, promoter methylation, transcriptional repression, or post-translational degradation — the cells lose their tight cell-cell adhesion and the β-catenin that was tethered at junctions becomes available for nuclear translocation and Wnt signaling (Chapter 1). The cells also lose their epithelial morphology and acquire migratory capability.

In some cancers, *E-cadherin (CDH1)* is mutated directly — about 50 percent of lobular breast carcinomas carry biallelic *CDH1* inactivation. Hereditary diffuse gastric cancer is caused by germline *CDH1* mutations. In most cancers that undergo EMT, however, E-cadherin loss is by transcriptional repression rather than mutation, mediated by the EMT-inducing transcription factors.

---

## The EMT transcription factors

The molecular switches that drive EMT are a small family of transcription factors that repress E-cadherin and other epithelial genes while activating mesenchymal genes.

*SNAI1 (Snail) and SNAI2 (Slug)*. Zinc finger transcription factors that bind E-boxes in the *CDH1* promoter and recruit chromatin-modifying complexes to repress E-cadherin expression. Snail and Slug also activate mesenchymal gene expression directly.

*ZEB1 and ZEB2*. Zinc finger E-box binding factors. They repress E-cadherin, claudins, and other epithelial genes, and activate vimentin and other mesenchymal genes. ZEB1/2 are particularly important in cancer EMT and form a feedback loop with the microRNA miR-200 family — miR-200 represses ZEB1/2, ZEB1/2 represses miR-200 expression. The double-negative feedback creates a bistable switch: cells are either in the high-miR-200/low-ZEB epithelial state or the low-miR-200/high-ZEB mesenchymal state.

*TWIST1 and TWIST2*. Basic helix-loop-helix transcription factors. Activated in many cancers; drive E-cadherin repression and mesenchymal gene expression.

*FOXC2, GSC, E47, others*. Additional EMT transcription factors with more specific contexts.

The EMT transcription factors are induced by several upstream signals. *TGF-β* is the dominant inducer in many contexts — TGF-β binds TGFR-I/II, activates SMAD-mediated transcription, and the SMADs drive expression of Snail, Slug, and others. *Wnt signaling* activates Snail through β-catenin-mediated transcription. *Notch signaling* activates Snail and Slug. *Receptor tyrosine kinase signaling* (EGFR, HGF/MET, FGF, PDGF) activates multiple EMT transcription factors through Ras-MAPK and PI3K-AKT downstream pathways. *Hypoxia* activates Snail through HIF-1α.

The pattern is that EMT is not a single signal but a convergence of many. In a tumor microenvironment with active TGF-β signaling from stromal cells, hypoxia from outpacing the blood supply, and oncogenic kinase signaling within the cancer cells, EMT is multiply driven. Individual cancer cells transition into the mesenchymal state asynchronously, producing tumor heterogeneity (Chapter 15) and providing a pool of cells with metastatic capacity.

---

## Partial EMT and the EMT spectrum

The textbook picture — cells switching from a fully epithelial state to a fully mesenchymal state — has been refined by recent research. Most cancer cells undergoing EMT in vivo achieve only *partial* EMT, where they retain some epithelial features (some E-cadherin expression, some cytokeratin) while gaining mesenchymal features (vimentin, migratory capacity, invasive behavior).

The partial-EMT cells appear to be the most metastatic. They retain enough cell-cell adhesion to migrate as small clusters rather than individually (which improves survival in circulation), and they retain the *epithelial plasticity* needed to convert back to a more epithelial state at the metastatic site (the *mesenchymal-epithelial transition*, MET, that allows seeding and growth at a distant organ).

This *EMT spectrum* model — cells exist along a continuum between fully epithelial and fully mesenchymal, with partial-EMT cells being most metastatically capable — has been supported by single-cell RNA sequencing of tumor cells, which reveals heterogeneous EMT states within the same tumor.

The implication for cancer biology is that EMT is not a binary switch but a continuum, and the cancer cells that successfully metastasize have access to multiple states along the spectrum. Drugs that lock cells into either pure epithelial or pure mesenchymal states might both be effective against metastasis, depending on the cellular context.

---

## Matrix metalloproteinases and ECM degradation

To invade through tissue, a cell needs to chew through the extracellular matrix in its way. The *extracellular matrix (ECM)* is the dense network of proteins and polysaccharides that fills the spaces between cells in tissue. Collagen (especially types I, III, IV) is the dominant fibrous component. Laminin and fibronectin are major basement membrane components. Hyaluronic acid, proteoglycans, and various other components fill out the matrix.

The basement membrane is a specialized ECM layer that separates epithelial sheets from underlying stroma. It is composed primarily of type IV collagen, laminin, and nidogen, with embedded proteoglycans. The basement membrane is a barrier that epithelial cells normally do not cross. Crossing it — *invasion through the basement membrane* — is the molecular event that defines the transition from in situ carcinoma to invasive carcinoma.

The enzymes that degrade ECM are the *matrix metalloproteinases (MMPs)* — a family of zinc-dependent endopeptidases. There are 23 human MMPs, categorized by substrate preference:

*Collagenases* (MMP-1, MMP-8, MMP-13) cleave native fibrillar collagens (types I, II, III).
*Gelatinases* (MMP-2, MMP-9) degrade type IV collagen of the basement membrane and denatured collagen (gelatin).
*Stromelysins* (MMP-3, MMP-10, MMP-11) have broad substrate specificity for ECM proteins.
*Matrilysins* (MMP-7, MMP-26) are smaller MMPs without a hemopexin domain.
*Membrane-type MMPs* (MT1-MMP/MMP-14, MT2-MMP, others) are anchored in the cell membrane and degrade ECM at the cell surface.

The MMPs are secreted (or membrane-anchored) as inactive zymogens. They are activated by proteolytic cleavage of an inhibitory prodomain. The most important activators are other MMPs (MT1-MMP activates MMP-2 in particular) and plasmin (which converts plasminogen-bound surfaces into a powerful proteolytic system).

MMP activity is opposed by *tissue inhibitors of metalloproteinases (TIMPs)*. There are four TIMPs (TIMP-1 through TIMP-4). The TIMPs bind MMPs and inhibit their proteolytic activity. The MMP-TIMP balance determines net ECM proteolysis in a given location.

In tumors, the MMP-TIMP balance is heavily shifted toward proteolysis. Cancer cells overexpress MMPs, especially MMP-2, MMP-9, and MT1-MMP. Tumor-associated fibroblasts and macrophages also produce MMPs. The result is local degradation of basement membrane and stromal ECM, opening paths for cancer cell migration.

MMP-9 in particular has been heavily studied in cancer biology. It is upregulated in essentially every invasive cancer. It cleaves type IV collagen of the basement membrane, allowing breakthrough invasion. It also releases ECM-bound growth factors (TGF-β, VEGF, FGF) into the local microenvironment, where they can drive further angiogenesis, EMT, and immunosuppression. MMP-9 cleavage of various substrates generates bioactive peptides that affect immune cell function.

Therapeutic targeting of MMPs was heavily pursued in the 1990s and 2000s. Several broad-spectrum MMP inhibitors (marimastat, batimastat, prinomastat) were taken to phase 3 trials. All failed. The reasons appear to include musculoskeletal toxicity (probably from inhibition of MMPs needed for normal tissue homeostasis), poor pharmacokinetics, and timing — by the time cancer is clinically detected, MMP-driven invasion has often already occurred. The field has largely moved on from broad-spectrum MMP inhibitors, though selective inhibitors of specific MMPs are still in development.

---

## Cytoskeletal reorganization for migration

A cell that has lost its junctions and acquired migratory potential still needs to actually move. Cell migration is a coordinated cellular behavior involving the actin cytoskeleton, focal adhesions to the extracellular matrix, and signaling cascades that coordinate the whole process.

The classical migration cycle:

1. *Polarization*. The cell establishes front-back asymmetry. The leading edge accumulates pro-protrusive signaling components.

2. *Protrusion*. Actin polymerization at the leading edge pushes the cell membrane forward. *Lamellipodia* are broad, sheet-like protrusions driven by branched actin networks (regulated by the Arp2/3 complex and WAVE/WASP family proteins). *Filopodia* are thin, finger-like protrusions driven by parallel actin bundles (regulated by formins and fascin).

3. *Adhesion*. The protruded leading edge forms new contacts with the substrate (the ECM) through integrin-mediated focal adhesions. The focal adhesions are anchored to the actin cytoskeleton through a complex of proteins (talin, vinculin, paxillin, kindlin, and others).

4. *Contraction*. Myosin II generates contractile force across the cell, pulling the cell body forward over the established adhesions.

5. *Rear retraction*. The trailing edge releases its old adhesions and the cell moves forward by one cycle.

The Rho family GTPases (RhoA, Rac1, Cdc42) coordinate this process. Cdc42 drives filopodial formation at the leading edge. Rac1 drives lamellipodial protrusion. RhoA drives myosin-mediated contraction at the rear. The spatial and temporal balance of these three GTPases determines migration speed, direction, and persistence.

In cancer cells, the migration machinery is hyperactivated. Rho GTPases are often elevated. Actin-modulating proteins (cortactin, fascin, formins) are overexpressed in invasive cancers. The cells acquire amoeboid migration mode (squeezing through tissue through actomyosin contractility) or mesenchymal migration mode (using integrin-mediated traction).

Some cancer cells form specialized invasive structures called *invadopodia*. These are dynamic, actin-rich membrane protrusions that concentrate proteases (MMPs, particularly MT1-MMP) and degrade local ECM. Invadopodia are the cancer-specific equivalent of *podosomes* that occur in normal cells (macrophages, osteoclasts, endothelial cells in tip-cell mode). Invadopodia formation is regulated by Src kinase, the Tks5 scaffold protein, and various actin-regulatory proteins. They are essentially the cellular drilling apparatus for invasion through ECM barriers.

---

## Collective versus individual invasion

Cancer cells can invade in two main modes.

*Single-cell invasion*. Individual cells detach from the tumor mass and migrate through tissue independently. This is the classical EMT-driven invasion. The cells acquire mesenchymal migration mode, use invadopodia and matrix proteases, and travel through stroma either to enter blood vessels or to reach distant sites by direct extension.

*Collective invasion*. Groups of cancer cells migrate together as cohorts, maintaining cell-cell contacts. The leader cells at the front of the cohort acquire some EMT features and drive invasion, while the follower cells retain more epithelial characteristics. Collective invasion is common in many epithelial cancers (breast, colon, head and neck, lung). The cohorts can be small (a few cells) or large (extensive strands or sheets).

The two modes are not mutually exclusive. A single tumor can have both, in different regions or at different times. Collective invasion may be more common in early invasion, with single-cell invasion taking over for entry into circulation. Single-cell migration may be more relevant for distant metastasis because individual cells more readily enter and survive in the bloodstream.

A particularly cancer-specific mode is *amoeboid migration* — cells move by squeezing through tissue using actomyosin contractility, without requiring matrix proteases. Amoeboid migration is faster than mesenchymal migration and is the mode of immune cell migration through tissue. Cancer cells that can switch to amoeboid migration may evade MMP inhibitor therapies and find tissue compartments that mesenchymal migrators cannot reach.

---

## What this chapter gives you

Invasion is the first step in metastasis — cancer cells leaving their tissue of origin. The process requires several cellular capabilities: loss of cell-cell adhesion (through EMT or related transitions), degradation of the extracellular matrix (through matrix metalloproteinases and other proteases), and migratory motility (through cytoskeletal reorganization).

EMT is the developmental program that gives epithelial cells mesenchymal characteristics. The molecular hallmark is loss of E-cadherin — usually through transcriptional repression by Snail, Slug, ZEB1/2, or Twist — accompanied by gain of N-cadherin, vimentin, and migratory capacity. Partial EMT, in which cells retain some epithelial features while acquiring mesenchymal ones, appears to be most relevant for metastasis because partial-EMT cells can both invade tissue and re-epithelialize at metastatic sites.

Matrix metalloproteinases (MMPs) degrade extracellular matrix and basement membrane, allowing cancer cells to pass through tissue barriers. The MMP-TIMP balance determines local proteolysis. MMP-9, MT1-MMP, and others are heavily upregulated in invasive cancers. Therapeutic targeting of MMPs has failed in multiple phase 3 trials, partly due to musculoskeletal toxicity and partly due to inadequate timing relative to natural disease progression.

The cytoskeletal machinery — actin, myosin, Rho GTPases, formins, Arp2/3 — is hyperactivated in invasive cancer cells. Specialized invasive structures called invadopodia concentrate proteases and drill through ECM. Cancer cells can invade as individuals (mesenchymal or amoeboid migration) or as collective groups, depending on the cellular and microenvironmental context.

Chapter 13B continues the metastatic story beyond local invasion — circulating tumor cells, the survival of cells in the bloodstream, the organ-specific patterns of metastatic seeding, and the molecular basis of organotropism. The biology connects to the angiogenesis topics of Chapter 12 (metastatic colonies need their own vasculature) and to the tumor microenvironment topics of Chapter 14 (the metastatic site has its own ecosystem that supports or rejects incoming cancer cells).

---

## LLM exercises

1. Ask your LLM to walk through the molecular events of EMT in detail — what initiates it, which transcription factors are activated, which genes are repressed, and what cellular consequences follow. Then probe: is EMT truly necessary for metastasis, or are there metastatic cancers that proceed without classical EMT?

2. Have your LLM explain the miR-200/ZEB feedback loop in EMT. Why does double-negative feedback produce bistability, and how does this connect to the EMT spectrum concept? Construct a simple mathematical model with the LLM and identify the parameter ranges that produce bistable versus graded behavior.

3. Use your LLM to assess the historical failure of broad-spectrum MMP inhibitors in cancer therapy. What specific clinical trials failed, what were the major reasons, and what lessons did the field learn? Then identify which more selective MMP-targeting strategies are still being developed.

4. Ask your LLM to compare single-cell, collective, amoeboid, and mesenchymal invasion modes. For each: which cancers use it predominantly, what molecular features distinguish it, and which therapies might block it? What is the experimental evidence for switching between modes?

5. Have your LLM explain how E-cadherin loss connects to β-catenin/Wnt signaling. What happens to the β-catenin that is released from disassembled junctions, how does it interact with the Wnt pathway, and what are the consequences for transcription of pro-invasive genes? Identify cancers where this connection is most consequential.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Lance Liotta** identified the laminin receptor in 1986 and built much of the molecular framework for how cancer cells break through basement membranes — the first step of invasion. His work brought biochemistry to a process previously described only morphologically.

**Run this:**

```
Who is Lance Liotta, and how does his work on basement membrane invasion connect to the tumor invasion biology we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Lance Liotta"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through the three-step model (attachment, degradation, locomotion) Liotta proposed for cancer invasion.
- Ask it about Liotta's pivot from basic invasion biology to clinical proteomics and biomarker discovery.

What changes? What gets better? What gets worse?
