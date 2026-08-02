# Chapter 5 — Oncogenes
*The Accelerator Was Already There.*

In 1973, Janet Rowley looked at the chromosomes of a chronic myeloid leukemia patient under a microscope and noticed that two chromosomes — 9 and 22 — had traded pieces. Chromosome 22 came out shorter. That shortened chromosome 22 became known as the Philadelphia chromosome, and it turned out to be present in nearly every CML patient ever examined. Something about that swap was driving the disease.

It took another decade to understand what the swap actually did. The traded piece of chromosome 9 carried a gene called *ABL1*, a kinase — an enzyme that attaches phosphate groups to other proteins and thereby switches them on. When *ABL1* landed on chromosome 22, it fused to a gene there called *BCR*. The fusion protein that resulted was an ABL kinase that could not turn off. Normally ABL is held in an autoinhibited state, kept quiet until needed. The BCR fusion removed the inhibition. The kinase fired continuously. That signal told myeloid precursor cells to keep dividing, and they did — endlessly, flooding the blood.

Here is what makes the story strange. *ABL1* is not a cancer gene in any ordinary sense. It is a gene that healthy cells need, doing ordinary cellular work. The cancer did not arise because a new, dangerous gene was introduced. It arose because an existing gene was jammed into the active position. The accelerator was already built into the car. The mutation just held it down.

---

The conceptual revolution happened in the 1970s, and it ran directly counter to what people thought cancer was. The prevailing idea was that cancer came from something foreign — a virus, a carcinogen, an external principle that corrupted normal cells from outside. Then Harold Varmus and Michael Bishop, studying the Rous sarcoma retrovirus, discovered that the viral gene responsible for transforming normal cells — the *v-src* oncogene — was not a viral invention. It was a slightly altered copy of a gene already present in normal vertebrate cells, which they called *c-src* (NCBI Bookshelf, *Development and Causes of Cancer*). The virus had picked up a cellular gene, mutated it slightly, and was using it as a weapon. Bishop and Varmus won the 1989 Nobel Prize for the framework that followed: cells carry in their own genomes the genes that, when altered, cause cancer. The first human oncogene — a mutant *HRAS* isolated from a bladder carcinoma by transfection assay — was identified in 1982, confirming that these alterations arise spontaneously, without any virus.

The terminology that emerged: a **proto-oncogene** is the normal, functional version — a gene that promotes cell growth, survival, or signaling as part of healthy tissue operation. An **oncogene** is the altered version — the same gene after a mutation, amplification, or rearrangement has locked it into excessive or inappropriate activity. The mutation does not give the gene a new purpose. It removes the controls on the old one. The *KRAS* gene driving roughly 90 percent of pancreatic cancers is the same *KRAS* that mediates normal growth-factor signaling in dividing cells throughout the body (NCI, *The Genetics of Cancer*). One amino acid changed is all that separates the useful protein from the cancer driver.

About 100 human proto-oncogenes are known. They cluster in a few functional categories — growth factors, growth-factor receptors, cytoplasmic kinases, GTP-binding switch proteins, transcription factors, cell-cycle regulators — and the clustering makes sense. A cell that is growing without permission is misfiring the same machinery that controls normal growth. The cancer is not running a different program; it is running the same program with the governor removed.

![Seven proto-oncogene categories arranged along one growth-signaling pathway](images/05-oncogenes-fig-03.png)
*Figure 5.3 — Proto-oncogene categories along a growth-signaling pathway*

<!-- → [DIAGRAM: proto-oncogene categories arranged along a growth-factor signaling pathway — secreted growth factor → receptor tyrosine kinase → cytoplasmic kinase → RAS GTPase → MAPK cascade → transcription factor → cell-cycle gene; each node labeled with a canonical proto-oncogene name] -->

---

The genetic signature of an oncogene is that a single altered allele is usually sufficient to cause the problem. The reason follows directly from what the problem is: too much activity. One overactive copy provides the excess signal. This is **gain of function**, and it makes oncogene mutations behave as **dominant** at the cellular level — one mutated allele overrides the normal copy sitting beside it.

This is the opposite of how tumor suppressors work (Chapter 6). A tumor suppressor holds growth in check; losing it means losing a restraint, and usually both copies must be inactivated before the restraint fails — the two-hit logic Knudson formalized (Hino, 2017). Oncogenes are not two-hit. The Philadelphia chromosome patient has one *BCR-ABL* fusion allele and one normal *ABL1* on the other chromosome. The normal *ABL1* is doing its ordinary job, but it does not rescue the situation. One stuck kinase is enough.

A clean illustration of how dosage alone can be sufficient: **HER2**, a growth-factor receptor encoded by *ERBB2*, is amplified in about 15–20 percent of breast cancers `[verify — specific percentage]`. The protein itself is not mutated. There is simply far too much of it — dozens of extra gene copies mean the cell surface is dense with receptor, and even low levels of ligand produce an overwhelming proliferative signal. One normal copy of HER2 would be fine. Fifty amplified copies are not.

---

A proto-oncogene becomes an oncogene by one of three routes, and each produces a different kind of excess.

**Point mutation** alters a single amino acid and locks the protein active. *KRAS* G12D — glycine changed to aspartate at codon 12 — is the prototype. *BRAF* V600E, present in roughly half of melanomas, is another (NCBI Bookshelf, *Development and Causes of Cancer*). The mutations that cause cancer cluster at specific positions — the hot spots — and they cluster there because only mutations at the regulatory region produce the constitutively active protein. A substitution elsewhere in *KRAS* might be neutral or destabilizing; the hot spots are where selection finds the useful change. The pattern is not chemistry driving mutation — it is selection amplifying the rare events that confer growth advantage.

**Gene amplification** increases copy number, raising expression without altering the protein. *MYCN* is amplified in about 25 percent of neuroblastomas, where it strongly predicts poor prognosis. *HER2* is amplified in breast and gastric cancers. *EGFR* is amplified in roughly half of glioblastomas. The protein is normal in sequence; the problem is that ten or a hundred times the usual amount is present. The signal is normal in kind but overwhelming in magnitude.

**Chromosomal rearrangement** creates either hybrid proteins or inappropriate expression of normal ones. The Philadelphia chromosome is the canonical fusion: the *ABL1* kinase and the *BCR* gene join, and the fusion protein lacks the regulatory domain that normally keeps ABL autoinhibited. The kinase is constitutively active — not because its catalytic site changed, but because the molecular leash was removed. Rearrangements can also work through **enhancer hijacking**: in Burkitt lymphoma, the t(8;14) translocation moves *MYC* next to the immunoglobulin heavy-chain enhancers, which are among the most powerful transcriptional activators in B cells. The MYC protein is completely normal. It is just expressed at extreme levels in a cell type that responds to MYC by proliferating.

![Three routes to oncogene activation: point mutation, amplification, and rearrangement](images/05-oncogenes-fig-01.png)
*Figure 5.1 — Three routes to oncogene activation*

<!-- → [DIAGRAM: three-panel comparison — left panel: point mutation showing single base change in codon 12 and the resulting stuck G12D protein with GTP permanently bound; middle panel: amplification showing many gene copies in the nucleus and excess protein on the membrane; right panel: translocation showing chromosomal exchange and the resulting fusion protein with active kinase domain and no autoinhibitory domain] -->

---

RAS deserves a close look because it is the most commonly mutated oncogene family in human cancer — *KRAS*, *HRAS*, and *NRAS* together are altered in perhaps a quarter of all human tumors — and because the molecular logic is unusually transparent.

RAS proteins are small GTPases, membrane-bound molecular switches. The switch is loaded into the **active state** when a guanine nucleotide exchange factor (GEF) displaces GDP and allows GTP to bind. The switch is **reset to inactive** when GTP is hydrolyzed to GDP by the protein's own GTPase activity, a reaction accelerated by GTPase-activating proteins (GAPs). Active RAS — GTP-bound — signals through the RAF→MEK→ERK cascade (the MAPK pathway, which drives proliferation) and through PI3K→AKT (which drives survival). The canonical circuit: a growth factor binds its receptor, the receptor recruits a GEF, the GEF activates RAS, RAS fires the downstream cascades, the signal propagates, and then GAP brings RAS back to the GDP-bound resting state (NCBI Bookshelf, *Development and Causes of Cancer*).

Oncogenic mutations at codons 12, 13, or 61 interfere with GTP hydrolysis. The mutant protein can still bind GTP; it simply cannot hydrolyze it efficiently — even with GAP assistance, the hydrolysis rate is roughly a hundred times slower. The switch stays locked active. The cell keeps receiving the "grow" signal regardless of whether any growth factor is present. The growth-factor receptor above RAS can be completely normal; it does not matter. The signal pathway has been short-circuited at the switch.

![The RAS switch cycle, with oncogenic mutation blocking GTP hydrolysis and locking RAS active](images/05-oncogenes-fig-02.png)
*Figure 5.2 — The RAS switch cycle (and where mutation jams it)*

For decades, RAS was considered undruggable. The protein has no obvious pocket for a small molecule to occupy, and attempts to block the GTP-binding site failed because RAS binds GTP with extraordinarily high affinity — no drug could compete. This changed when a specific covalent approach was found for the *KRAS* G12C mutation, common in lung adenocarcinoma: the mutant cysteine at position 12 presents a reactive surface that an electrophilic small molecule can attack irreversibly. Sotorasib and adagrasib, both G12C-specific covalent inhibitors, are now FDA-approved — modest but real benefits, and conceptually important as proof that the "undruggable" label was a statement about our chemistry at a moment in time, not a permanent verdict. The far more common G12D mutation (the dominant driver in pancreatic cancer) lacks that reactive cysteine, which is precisely why the same approach does not transfer, and why a G12D inhibitor required a different chemical strategy. The boundary condition is molecular: one nucleotide difference in the mutation changes what chemistry is possible.

---

Transcription factors are a second major oncogene category, and they illustrate a different kind of problem. The **MYC** family — *MYC*, *MYCN*, *MYCL* — drives expression of thousands of genes involved in proliferation, ribosome biogenesis, and metabolism. MYC is deregulated in a large fraction of human cancers: amplified in neuroblastoma, translocated in Burkitt lymphoma, hyperactivated downstream of RAS in many epithelial cancers (Hanahan, 2022).

In healthy cells, MYC is produced in brief pulses. Both the mRNA and the protein have very short half-lives — the wave of MYC expression that follows a growth signal rises quickly and then falls. Cancers that have amplified or translocated *MYC* keep it high continuously, locking the cell in a state where thousands of growth and metabolic genes are always turned on.

MYC is also undruggable by direct approaches, for a different reason than RAS: transcription factors bind DNA, not small-molecule substrates, and they have no enzymatic active site to inhibit. The productive strategies have been indirect — targeting what MYC-driven cells depend on. The BET bromodomain reader BRD4 is required for MYC-dependent transcription at many loci; BET inhibitors (drugs that block BRD4's interaction with acetylated histones) suppress MYC-driven programs without touching MYC directly. The principle is general: if you cannot block the oncogene, identify what the oncogene-addicted cell cannot live without.

---

A 55-year-old never-smoker is diagnosed with lung adenocarcinoma. Tumor sequencing shows an *EGFR* exon-19 deletion — a small in-frame indel that removes part of the kinase domain regulatory loop and locks EGFR in a constitutively active, ligand-independent state. EGFR signals through RAS/MAPK and PI3K/AKT, the same downstream pathways that RAS mutations activate. The tumor is **oncogene-addicted**: its proliferation and survival depend on continuous EGFR output, and when that output is blocked, the cells have no alternative.

She starts osimertinib, a third-generation EGFR inhibitor, and within three months her tumors have shrunk dramatically. This looks, for a moment, like a cure.

It is not. Eighteen months later, imaging shows new growth. Resequencing of the resistant tumor finds the original *EGFR* deletion still present — the drug is still blocking that target — but now the cancer has also amplified *MET*, a different receptor tyrosine kinase. MET can activate RAS/MAPK and PI3K/AKT independently of EGFR. The cancer has rewired itself: it no longer cares whether EGFR is blocked, because the signal it needs arrives through a different receptor.

This is the **bypass track**, one of the canonical resistance mechanisms. The others are: secondary mutation within the target that prevents the drug from binding (the *EGFR* T790M "gatekeeper" mutation, or the *BCR-ABL* T315I mutation that made some CML patients resistant to imatinib), amplification of the target so that drug concentrations that were sufficient no longer are, and phenotypic switching to a completely different cell state that no longer depends on the oncogene at all — EGFR-mutant adenocarcinomas occasionally transform to small-cell histology and shed their EGFR dependence entirely.

Her therapy changes to combine EGFR and MET inhibition, and control is restored for a further period. The logic of her treatment is now chasing evolution: each resistance mechanism is a selected subclone that survived the last therapy, and the next therapy must address it while anticipating the one after.

The lesson from CML is that oncogene addiction creates a genuine vulnerability — the cancer has, in effect, concentrated its dependency onto one signal, and blocking that signal can produce responses that look like cures. The lesson from lung adenocarcinoma is that the same concentration of dependency makes the cancer exquisitely motivated to find an alternative, and it has billions of cells, continuous mutation, and time to search.

---

The Philadelphia chromosome patient who started imatinib in the early 2000s is, in many cases, alive today. CML was nearly always fatal within a few years; it is now, for most patients, a manageable chronic condition. That outcome traces directly to the clarity of the molecular target: one fusion protein, one drug, one blocked active site. The cancer had bet everything on BCR-ABL, and imatinib called the bet.

Most oncogene-driven cancers are not so simple. RAS in pancreatic cancer has resisted targeted therapy for forty years. MYC drives many tumors and has no direct inhibitor. EGFR-mutant lung cancer responds brilliantly and then escapes. The principle — find the gene the cancer depends on, block it — is sound, and it has produced some of the most dramatic responses in oncology. The challenge is that cancer is a population under selection, and the drug is the selection pressure. Whatever the pre-existing resistant minority turns out to be, it will expand.

The accelerator was already there. Blocking it works, until the car finds another way to move.

---

## Exercises

**Warm-up**

1. *[Recall — moderate]* For each mechanism of oncogene activation — point mutation, gene amplification, and chromosomal rearrangement — name one canonical example from this chapter and state in one sentence what the alteration does to the protein's activity. Your answer should distinguish between changes that alter the protein's structure and changes that increase the amount of a normal protein.
*What this tests: whether you can connect activation mechanism to molecular consequence — not just list examples.*

2. *[Recall — moderate]* Explain in three sentences why oncogene mutations are dominant at the cellular level — why a single mutant allele is sufficient to drive the cancer phenotype — and contrast this with the two-hit logic that applies to tumor suppressors.
*What this tests: gain-of-function versus loss-of-function logic; applying the correct genetic model to the correct class of cancer gene.*

3. *[Recall — moderate]* Describe the RAS switch cycle: what loads it into the active state, what resets it to inactive, and what mutation at codon 12 does to that cycle. Name the two major downstream signaling cascades that active RAS feeds.
*What this tests: mechanistic understanding of GTPase biochemistry — the molecular basis of the "stuck accelerator," not just the analogy.*

**Application**

4. *[Apply — moderate-hard]* A tumor carries a *KRAS* G12D mutation. Explain step by step why a competitive inhibitor targeting the GTP-binding site has historically been impossible to develop, and why a covalent inhibitor targeting the G12C mutant became possible while G12D required a different approach. Your answer should name the chemical property of each mutant residue that determines what chemistry is available.
*What this tests: translating the biochemistry of the RAS switch into the constraints on drug design — moving from mechanism to therapeutic implication.*

5. *[Apply — moderate-hard]* A 48-year-old woman with HER2-amplified breast cancer responds to trastuzumab (an antibody that blocks HER2) but progresses after fourteen months. Resequencing shows the HER2 amplification is unchanged. Generate two distinct resistance mechanisms that could explain the progression without any change in HER2 status, and for each name a rational next therapeutic approach.
*What this tests: applying the bypass-track and downstream-reactivation resistance logic to a specific oncogene context; distinguishing target-level from pathway-level escape.*

6. *[Apply — hard]* Compare two lung adenocarcinoma patients: Patient A has an *EGFR* exon-19 deletion as a truncal, clonal driver (present in essentially all tumor cells); Patient B has the same deletion in only a subset of cells (a subclonal alteration), with other subclones driven by *KRAS* G12C. Both start osimertinib. Predict the depth and durability of response for each, explaining your prediction using both the oncogene addiction concept and the clonal architecture of each tumor.
*What this tests: integrating oncogene biology with the clonal evolution framework from Chapter 8; understanding that addiction applies to the tumor population, not just individual cells.*

**Synthesis**

7. *[Synthesis — hard]* Build a mechanism map for Burkitt lymphoma using four nodes: (1) the normal regulation of *MYC* expression in B cells; (2) the t(8;14) translocation and what it does to that regulation; (3) the resulting cellular phenotype; (4) one therapeutic approach that targets a dependency created by chronic MYC overexpression rather than MYC itself. Label each arrow with the molecular mechanism linking the nodes. Then write two sentences explaining why targeting MYC directly is difficult and why the indirect strategy at node 4 is theoretically sound.
*What this tests: applying the enhancer-hijacking mechanism to a transcription-factor oncogene; understanding indirect targeting logic for undruggable oncogenes.*

8. *[Synthesis — hard]* The BCR-ABL T315I mutation in CML and the EGFR T790M mutation in lung adenocarcinoma are both called "gatekeeper" mutations. Explain what structural feature these mutations share, why they arise under targeted therapy, and why they are almost always present as pre-existing resistant clones rather than arising de novo during treatment. Then explain what the existence of pre-existing gatekeeper mutations implies for the design of first-line therapy in oncogene-addicted cancers.
*What this tests: integrating resistance mechanism, clonal evolution logic, and therapeutic design — connecting oncogene biology to the evolutionary framework of Chapter 8.*

**Challenge**

9. *[Challenge — very hard]* The "Still Puzzling" section asks why the same *KRAS* G12D mutation drives aggressive, nearly untreatable pancreatic cancer but is less common and less dominant in other tissue types. Design a research program — using cell lines, organoids, mouse models, and human tumor data — that would systematically test which tissue-specific factors determine whether an oncogenic *KRAS* mutation transforms a cell, and what those factors imply for tissue-specific therapy. Specify the experimental logic at each stage, the confounders you would need to control, and the finding that would most dramatically change current clinical strategy for pancreatic cancer if it turned out to be true.
*What this tests: moving from a mechanistic puzzle to a translational research design; reasoning about tissue context as a modifier of oncogene function.*

---

## What Would Change My Mind

The chapter's central claim is that oncogene activation is gain-of-function and dominant — one altered allele drives the phenotype. A finding that would force revision: convincing evidence that the canonical oncogenic alterations — KRAS G12, BCR-ABL, HER2 amplification — routinely require biallelic inactivation of the normal copy to transform cells, or that single-allele oncogene activation reproducibly fails to confer a growth advantage in well-controlled systems. The transfection assays that identified the first human oncogene specifically detected single-allele dominant transformation; a robust failure to replicate that result across modern model systems would undermine the gain-of-function framework.

## Still Puzzling

- Why do some oncogenes (KRAS, MYC) remain so hard to drug directly even though we have known their sequence for decades, while others (BCR-ABL, EGFR) yielded almost immediately? Is druggability a property of the protein structure, the pathway architecture, or the chemistry we have available?
- Why does the same mutation — KRAS G12D — drive aggressive pancreatic cancer but is far less common in other tissues? What tissue context determines whether a stuck accelerator transforms a cell, and how much of that context is epigenetic rather than genetic?
- When a cancer escapes targeted therapy by phenotypic switching rather than mutation, is the change genetic, epigenetic, or both? This question hands directly to the following chapters on epigenetic reprogramming.

## References

- National Cancer Institute. *The Genetics of Cancer.* https://www.cancer.gov/about-cancer/causes-prevention/genetics
- National Cancer Institute. *What Is Cancer?* https://www.cancer.gov/about-cancer/understanding/what-is-cancer
- Hino, O., et al. (2017). The two-hit hypothesis, the driver of cancer. *Cancer Science.* https://onlinelibrary.wiley.com/doi/10.1111/cas.13116
- NCBI Bookshelf. *The Development and Causes of Cancer.* https://www.ncbi.nlm.nih.gov/books/NBK9963/
- Hanahan, D. (2022). Hallmarks of Cancer: New Dimensions. *Cancer Discovery*, 12, 31–46.
- NCBI Bookshelf. *Molecular Biology of the Cell.* https://www.ncbi.nlm.nih.gov/sites/books/n/mboc4/

---

## Prompts

### Figure 5.1 — Three routes to oncogene activation
Build a three-panel comparison, each panel pairing a genetic change (left) with its protein consequence (right) under axis label "Route to activation." Rows: (1) "Point mutation at codon hot spot (KRAS G12D)" → "protein locked active, nucleotide permanently bound" (sky-blue anchor); (2) "Amplification, one copy → many (HER2)" → "dense excess of structurally normal receptor" (secondary); (3) "Rearrangement, two segments fuse (BCR-ABL)" → "fusion protein: active kinase, regulatory domain lost" (green). Use a small schematic glyph on each genetic-change side: a single base flag for the point mutation, a stack of repeated gene-copy boxes for amplification, two differently-shaded chromosome segments joining for rearrangement. The right side shows the resulting active/excess/fusion protein. Emphasis is the parallel structure: three different genetic causes, three different excess-activity outcomes. Subtitle: "Point mutation, amplification, or rearrangement." Okabe-Ito semantics: sky-blue anchor for the locked-active point mutant, neutral secondary for amplification, green for the active fusion. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 5.2 — The RAS switch cycle (and where mutation jams it)
Build a closed-loop cycle diagram of the RAS GTPase switch with one blocked return path and a downstream branch. Six nodes arranged around the loop: (1) Inactive RAS (GDP-bound, neutral); (2) GEF loads GTP (secondary); (3) Active RAS (GTP-bound, green/positive); (4) Downstream: RAF-MEK-ERK & PI3K-AKT (blue, dominant — drawn as a branch off the active node); (5) GAP-accelerated GTP hydrolysis / reset (neutral, the off-step); (6) Mutant: hydrolysis blocked, locked active (vermillion, negative). Curved arrows drive the loop clockwise from inactive → loaded → active → reset → inactive. Mark node 6 as a red X or barrier on the reset arrow, showing the off-switch is jammed so the cycle is trapped at the active state. The downstream cascade branches outward from active RAS. Subtitle: "Mutation blocks the off-switch, the stuck accelerator." Okabe-Ito semantics: green for active RAS, blue for the dominant downstream cascade, vermillion for the blocking mutation. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 5.3 — Proto-oncogene categories along a growth-signaling pathway
Build a horizontal left-to-right linear pathway with seven sequential category nodes connected by directional arrows. Nodes in order: (1) Secreted growth factor (secondary); (2) Receptor tyrosine kinase (membrane, neutral); (3) Cytoplasmic kinase (green); (4) RAS GTPase switch (sky-blue anchor); (5) MAPK kinase cascade (green); (6) Transcription factor — enters nucleus (secondary); (7) Cell-cycle target gene (neutral). Show the signal flowing inward: extracellular factor → membrane receptor → cytoplasmic relays → RAS → cascade → nucleus → target gene. Optionally mark a vertical membrane line between nodes 1 and 2 and a nuclear boundary before node 6 to convey compartment crossings. Each node is a labeled box; arrows convey one-directional signal propagation. Subtitle: "One signaling axis, seven proto-oncogene categories." Okabe-Ito semantics: sky-blue anchor for the central RAS switch, green for the kinase steps, neutral/secondary for the rest. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.
