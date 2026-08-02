# Chapter 8 — Epigenetics in Cancer: Noncoding RNAs, Reprogramming, and Therapy
*The Instructions Were Never in the Genes.*

In 2002, a team studying chronic lymphocytic leukemia went looking for the tumor suppressor that ought to sit in a region of chromosome 13 that is frequently deleted in these patients. They searched for protein-coding genes. They found none. What they found instead were two tiny RNA molecules — *miR-15* and *miR-16* — that encode no protein but silence the messenger RNAs of other genes. The deletion was not removing a protein; it was removing a brake made of RNA, and without that brake, a network of pro-survival transcripts ran unchecked (Croce et al., 2002, summarized in the chapter archive).

The result forced a conceptual adjustment. The genome had been understood, for most of molecular biology's history, as a protein-encoding document with some regulatory annotations. The 98 percent that does not encode protein was called "junk" — and not entirely seriously, because everyone knew that some of it was regulatory, but the regulatory layer was not well mapped. Here was a case where deleting two RNA molecules, neither of which made any protein, was sufficient to drive leukemia. Something real lived in that 98 percent.

A human has roughly the same number of protein-coding genes as a roundworm. The extra complexity must be encoded somewhere else. Much of it is in the regulatory RNA transcribed from the non-coding majority — a layer of biology that cancer deranges as reliably as it deranges the protein layer.

---

A **microRNA** is a short RNA, 18–25 nucleotides, that binds partially complementary sites in the 3' untranslated regions of target messenger RNAs and silences them — blocking translation or triggering mRNA degradation. The binding is partial, which is the key mechanical detail: because perfect complementarity is not required, a single microRNA can match dozens or hundreds of different target sequences and silence all of them simultaneously. The regulatory reach is enormous compared to a transcription factor, which typically binds one specific sequence and regulates one gene at a time (Signal Transduction and Targeted Therapy, 2023).

The processing pathway is: a long primary transcript in the nucleus is cleaved by the enzyme Drosha, exported, cleaved again by Dicer in the cytoplasm, and one strand of the resulting 22-nucleotide duplex is loaded into an Argonaute protein to form the RNA-induced silencing complex (RISC). RISC, guided by the microRNA, finds and silences its targets. The whole pathway is conserved from worms to humans.

In cancer, microRNAs deregulate in two distinct directions, and the direction tells you what the microRNA normally does.

An **oncomiR** is a microRNA whose overexpression promotes cancer by silencing tumor suppressor mRNAs. *miR-21* is the most-studied example — upregulated in nearly every solid cancer — and its targets include PTEN, the phosphatase that opposes PI3K/AKT survival signaling, and PDCD4, a translation regulator that restrains invasion. Silence PTEN and you get constitutively active AKT; silence PDCD4 and you get increased invasive potential. One microRNA, silencing both targets simultaneously, contributing to two hallmark capabilities at once.

The *miR-17~92* cluster is a six-microRNA unit that is a direct transcriptional target of MYC — MYC is the oncogene, and *miR-17~92* is one of the downstream effectors that executes its program. The cluster is overexpressed in many lymphomas. MYC produces it, and it helps maintain the proliferative state MYC induces.

In the other direction: some microRNAs are tumor suppressors. The *let-7* family targets the mRNAs of *RAS* and *MYC* directly — it is one of the molecular brakes that keeps those proto-oncogenes under control in normal cells. Its loss is common in lung adenocarcinoma, and when it is lost, RAS and MYC levels rise. *miR-34a* is part of the p53 tumor-suppressive program: p53 transcriptionally activates *miR-34a*, which then silences genes that promote cell-cycle progression and block apoptosis. A cancer that has lost p53 has often also lost *miR-34a*, and the network p53 would have executed through it goes dark.

The opening case's *miR-15* and *miR-16* are tumor suppressors of this kind: their primary target is the anti-apoptotic mRNA *BCL2*. Normal B cells maintain a balance between pro- and anti-apoptotic signals; *miR-15/miR-16* keep BCL2 in check. Delete the chromosome region carrying them, and BCL2 protein rises, cells resist apoptosis, and a clone that should have died keeps accumulating. That is CLL.

![oncomiR silences a tumor suppressor to drive survival; tumor-suppressive miR silences an oncogene](images/08-epigenetics-in-cancer-noncoding-rnas-reprogramming-and-therapy-fig-01.png)
*Figure 8.1 — oncomiR vs tumor-suppressive microRNA*

<!-- → [DIAGRAM: two-panel microRNA mechanism — left panel: oncomiR (miR-21) loaded into RISC silencing PTEN mRNA, resulting in elevated AKT activity and survival; right panel: tumor-suppressive miRNA (let-7) silencing RAS mRNA, resulting in reduced proliferation; arrows and phenotypic outcomes labeled] -->

The clinical potential is real and the bottleneck is honest: microRNAs are unusually stable in blood, surviving conditions that destroy messenger RNA, which makes them attractive as biomarkers. As therapeutics, the logic is sound — deliver a mimic of a lost tumor-suppressive microRNA, or an antisense oligonucleotide (anti-miR) to inhibit an oncomiR. The first microRNA mimic to reach clinical trials, MRX34 (a *miR-34a* mimic), was halted in 2016 because of immune toxicity. Getting nucleic acids into solid tumors at therapeutic doses without triggering immune reactions is the hard problem, and it is still largely unsolved.

---

**Long noncoding RNAs** are transcripts longer than 200 nucleotides with no protein-coding potential. The genome encodes tens of thousands of them — the exact number depends on how you define a functional transcript versus transcriptional noise, which is itself a contested question. Their mechanisms are heterogeneous: some scaffold protein complexes, some guide chromatin-modifying enzymes to specific loci, some act as sponges that titrate microRNAs out of circulation so their targets are de-repressed.

The mechanistic example worth holding is *HOTAIR*, because it connects lncRNA biology directly to the chromatin-maintenance machinery. *HOTAIR* binds the Polycomb Repressive Complex 2 — an enzyme system (catalytic subunit EZH2) that writes the repressive chromatin mark H3K27me3 — and guides it to specific genomic loci that PRC2 would not otherwise reach. The result is silencing of tumor suppressor genes at those loci, silencing that persists through cell divisions. *HOTAIR* overexpression appears in breast, colorectal, liver, lung, and gastric cancers and correlates with poor prognosis. The protein-coding sequence of those tumor suppressors is intact; the DNA is unmutated. The gene is simply kept off by a recruited silencing complex, guided there by a noncoding RNA. That is a different kind of genetic catastrophe than the ones Chapter 5 and Chapter 6 describe.

*MALAT1* regulates alternative splicing and contributes to metastatic behavior. *NEAT1* assembles nuclear paraspeckles — protein-RNA bodies involved in stress response — and its overexpression promotes cell survival under hypoxic conditions. The catalog of cancer-relevant lncRNAs runs into the hundreds; therapeutic targeting through antisense oligonucleotides is early-stage.

---

A cell's identity must survive division. When a liver cell divides, its daughters must be liver cells — not muscle cells, not neurons. The transcriptional pattern that defines a cell type has to be remembered and propagated, even though the chromatin is largely disassembled and reassembled with each replication cycle. This is the problem that two opposing chromatin systems solve, first identified in fruit flies and conserved to humans: the **Polycomb group**, which maintains silencing, and the **Trithorax group**, which maintains activation.

Polycomb works through two complexes in sequence. **PRC2** — with EZH2 as its catalytic engine — writes the repressive mark H3K27me3 on histone tails. **PRC1** reads that mark, adds a second layer of compaction, and blocks the transcriptional machinery from accessing the underlying DNA. Together they keep developmental programs that should be permanently off, reliably off, in every daughter cell. The Trithorax group — the KMT2/MLL methyltransferases that write the activating H3K4me3 mark, and the SWI/SNF chromatin remodeling complex — maintains the opposing state at genes that should stay on.

![Polycomb maintains repressive memory while Trithorax maintains activating memory at one locus](images/08-epigenetics-in-cancer-noncoding-rnas-reprogramming-and-therapy-fig-03.png)
*Figure 8.3 — Polycomb vs Trithorax: opposing memory systems*

In embryonic stem cells, a specific class of developmental genes carries *both* marks simultaneously: H3K27me3 (repressive) and H3K4me3 (activating), stacked on the same histone tail. These are called **bivalent** genes — poised, kept at low expression but ready to be fully activated when the cell commits to a differentiation lineage. As differentiation proceeds, the bivalent state resolves: the differentiation genes for the chosen lineage lose their repressive mark and fire; the others consolidate their repression.

In aggressive cancer cells, bivalent chromatin patterns resembling embryonic stem cells reappear. Differentiation programs that should have been resolved and locked shut are accessible again. The cell can shift between phenotypic states more readily — de-differentiating under stress, accessing stem-like transcriptional programs, adopting a different identity under therapeutic pressure. This chromatin-level plasticity is one of the molecular underpinnings of why cancers that look homogeneous can harbor cells capable of becoming something different when survival pressure is applied (Hanahan, 2022).

![Bivalent chromatin: a poised gene resolves one way in differentiation and is re-acquired in cancer](images/08-epigenetics-in-cancer-noncoding-rnas-reprogramming-and-therapy-fig-02.png)
*Figure 8.2 — Bivalent chromatin: poised, resolved, re-acquired*

In cancer, both systems are disrupted. EZH2 is hyperactivated in diffuse large B-cell lymphoma and follicular lymphoma — too much repression, silencing tumor suppressors that should be active. MLL1 is rearranged in about 5–10 percent of acute leukemias, particularly infant leukemias, producing fusion proteins that aberrantly activate developmental transcription factor programs. SWI/SNF, the Trithorax-side chromatin remodeling complex, is mutated in roughly 20 percent of all human cancers — making it one of the most frequently altered chromatin regulators in the genome. When SWI/SNF fails, genes that require active chromatin remodeling to stay expressed cannot maintain their open state.

---

The most contested section of this chapter deserves the most careful framing.

**Epigenetic reprogramming** is the claim that some cancers arise when a cell's chromatin landscape resets toward a stem-like state — reactivating stem-cell transcriptional programs — without necessarily requiring the prior accumulation of genetic mutations the classical clonal evolution model expects. The supporting observation is **methylation drift**: the DNA methylation patterns of aging stem cells drift over time, the drift correlates quantitatively with cancer incidence, and epigenetic "clocks" built on this drift predict biological age and cancer risk (Hanahan, 2022). This is correlative evidence. Whether drift *causes* cancer by creating a permissive epigenetic landscape, or merely accompanies it as a parallel consequence of the same cellular stresses that cause mutation, has not been resolved.

The **cancer stem cell hypothesis** proposes that tumors are hierarchically organized — sustained by a small population of cells with stem-like self-renewal capacity, while the majority of tumor cells are more differentiated and limited in their capacity to propagate the tumor. The evidence is real but contested. Xenotransplantation experiments showed that only specific marker-defined populations from some tumors could establish tumors when transplanted into immunocompromised mice — suggesting a hierarchy. But under more permissive transplantation conditions, a much higher fraction of cells showed tumor-initiating capacity, suggesting the hierarchy is not as fixed as the original experiments implied. Whether cancer stem cells are a distinct, stably defined population or a transient state that many cells can enter and exit is genuinely unsettled `[contested — see pantry flag]`.

The therapeutic stakes are real: if a stem-cell-like subpopulation survives the chemotherapy that kills the bulk tumor, it could drive recurrence. Drugs targeting the pathways associated with stemness — Wnt, Notch, Hedgehog inhibitors — have been tested in clinical trials. The results have been mixed, which is not a refutation of the hypothesis but is also not confirmation. The cancer stem cell model is active synthesis, not settled dogma.

---

Several epigenetic drug classes are FDA-approved, and what unifies them is a property that distinguishes them from essentially every other class of cancer drug: **epigenetic states are reversible while mutations are not**.

A kinase inhibitor blocks an enzyme. A targeted therapy kills cells that depend on a pathway. But an epigenetic drug can, in principle, restore a gene to its proper expression state — turning on a tumor suppressor that has been silenced by DNA methylation, or reactivating a differentiation program that has been locked off by aberrant histone modification. It is not blocking a function; it is recovering one (Experimental & Molecular Medicine, 2023).

**DNMT inhibitors** — azacitidine and decitabine — inhibit the DNA methyltransferases responsible for maintaining methylation patterns at CpG sites. When DNMT activity falls, methylation is passively diluted with each cell division, and genes silenced by promoter hypermethylation can be re-expressed. In myelodysplastic syndrome and older patients with acute myeloid leukemia, they induce differentiation and improve survival. Combined with venetoclax, a BCL2 inhibitor, in AML, they have become a standard-of-care regimen — one of the most significant advances in AML treatment in decades. In solid tumors, they are most active in combination with immune checkpoint inhibitors: demethylation reactivates dormant immune-recognition genes, increases neoantigen presentation, and makes the tumor microenvironment more immunologically active.

**HDAC inhibitors** — vorinostat, romidepsin, panobinostat — inhibit the histone deacetylases that remove acetyl groups from histone tails. Hyperacetylation opens chromatin and reactivates silenced genes. These drugs have FDA approvals in cutaneous and peripheral T-cell lymphoma. Their clinical activity is largely confined to hematologic malignancies; in solid tumors, off-target deacetylation of non-histone proteins produces toxicity that limits dose and, with it, efficacy.

**EZH2 inhibitors** — tazemetostat, approved 2020 — block the PRC2 catalytic subunit that writes H3K27me3. In follicular lymphoma with activating EZH2 mutations, inhibiting the hyperactive enzyme reduces aberrant silencing of differentiation genes. In *SMARCB1*-deleted epithelioid sarcoma, the mechanism is different and elegant: SWI/SNF loss makes these tumors paradoxically dependent on PRC2 activity (synthetic lethality), so blocking EZH2 kills a cancer defined by the *absence* of a chromatin regulator.

**IDH inhibitors** — ivosidenib and enasidenib — address the cleanest mechanistic story in epigenetic oncology. Mutant IDH1 and IDH2 enzymes produce a metabolite, 2-hydroxyglutarate, that is structurally similar to alpha-ketoglutarate and competitively inhibits the TET demethylases and KDM histone demethylases that require it. The result is hypermethylation of CpG islands and silencing of differentiation genes — an **epigenetic block** to differentiation. Block the mutant IDH enzyme, 2-HG falls, demethylase activity recovers, methylation patterns normalize, and leukemic cells differentiate. In IDH-mutant AML, this is not killing the cell; it is releasing an epigenetic lock. The clinical responses include patients whose leukemic blasts differentiate into mature neutrophils — the disease resolving through differentiation rather than cytotoxicity.

**BET inhibitors** are not yet approved but are in clinical trials. BET bromodomain proteins (BRD4 is the best-studied) are chromatin readers that recognize acetylated histones and recruit the transcriptional machinery to active gene loci. At super-enhancers — the large, densely acetylated regulatory elements that drive high-level expression of key oncogenes including MYC — BRD4 occupancy is especially high. BET inhibitors displace BRD4 from super-enhancers and disproportionately suppress MYC-driven transcriptional programs. They validate the reader layer as a therapeutic target and offer an indirect path to suppressing MYC — the transcription factor that has resisted direct targeting for decades.

The pattern across all of these: hematologic malignancies respond more readily than solid tumors. Blood cancer cells are less differentiated, their chromatin states more accessible and less entrenched, and the tumor microenvironment is less of a barrier to drug delivery. In solid tumors, combination strategies — epigenetic drugs plus chemotherapy, plus immunotherapy, plus targeted agents — are where the next progress will most likely come.

<!-- → [TABLE: epigenetic drug classes — columns: drug class, example agents, molecular target, mechanism of action, approved indication(s), key combination strategy] -->

---

An EGFR-mutant lung adenocarcinoma responds beautifully to osimertinib and then regrows eighteen months later. Resequencing the resistant tumor finds the original EGFR deletion unchanged, no new resistance mutation in EGFR, and no new bypass mutation in a parallel pathway — and the tumor now looks histologically like small-cell lung cancer rather than adenocarcinoma.

The genetic model predicts a mutation that is not there. The sequencing found nothing useful, and by the logic of Chapter 5 — targeted drug, secondary mutation in the target, bypass track — there is no explanation. Something happened that left no genetic footprint.

The clue is in the histology. The cell changed identity. It is no longer an adenocarcinoma — the glandular, EGFR-dependent cell type it was at diagnosis. It has become a neuroendocrine small-cell phenotype in which EGFR signaling is not required for survival. The drug still blocks EGFR perfectly. The cell no longer depends on EGFR.

This is phenotypic switching driven by epigenetic reprogramming. The founding EGFR mutation is still present. No new mutation directed the change. Instead, under the sustained selection pressure of EGFR blockade, a subpopulation accessed bivalent chromatin — developmental programs that were poised, not locked — and resolved them toward a neuroendocrine identity. The chromatin landscape shifted, the neuroendocrine transcription program activated, and a cell that had been an adenocarcinoma became something functionally different, in the same body, without changing its DNA sequence.

The treatment path is not a better EGFR inhibitor. The target is gone — not mutated, not bypassed, simply no longer the driver. The path forward is matching therapy to the new phenotype: platinum-etoposide for small-cell, or a combination strategy addressing the reprogrammed state directly. The genetic-only resistance assay misses this escape because it looks for mutations in a process that proceeded without them.

The lesson runs past this specific case: cancer cell identity is not fixed by its founding mutation. Under pressure, cells with accessible chromatin can move. A treatment strategy that assumes the cancer at relapse is the same cell type it was at diagnosis will be wrong whenever epigenetic reprogramming was the escape route.

---

The 98 percent of the genome that does not encode protein is not filler. It encodes the regulatory layer that determines which proteins are made, when, in what amounts, and in which cells. Cancer deranges this layer as thoroughly as it deranges the coding layer — microRNAs silenced or overexpressed, lncRNAs misdirecting chromatin complexes to the wrong targets, Polycomb-Trithorax balance disrupted, bivalent states left unresolved, cells slipping between identities under therapeutic pressure.

What makes epigenetic cancer biology both promising and difficult is the reversibility that defines it. A mutation is permanent; it can be targeted but not corrected. An epigenetic state can, in principle, be returned to normal — a silenced tumor suppressor re-expressed, a blocked differentiation program released, a cancer cell induced to become something that behaves less like a cancer. IDH inhibitors in AML are the clearest proof that this is not theoretical. The differentiated neutrophils are real.

The difficulty is that not all epigenetic states are equally accessible, the cancer microenvironment is a constant source of signals that maintain the malignant state, and the cancer stem cell question — whether a stable, identifiable population maintains the tumor against every epigenetic drug — is still open. The tools are real. The target layer is real. The clean victories are fewer and smaller than the biology suggests they should be, which is the honest state of the field.

---

## Exercises

**Warm-up**

1. *[Recall — moderate]* Explain how a single deleted microRNA can disable an entire network of target mRNAs, and why that regulatory reach is structurally different from losing one protein-coding tumor suppressor gene. Your answer should explain why the partial complementarity requirement is mechanistically important.
*What this tests: whether you understand the one-to-many targeting logic of microRNAs, not just the fact that they silence genes.*

2. *[Recall — moderate]* Describe bivalent chromatin: what two marks are present, in what cell type it is found normally, what resolves it during differentiation, and why its persistence or re-acquisition in cancer cells contributes to phenotypic plasticity.
*What this tests: the mechanistic link between Polycomb-Trithorax biology and cancer cell identity flexibility.*

3. *[Recall — moderate]* Name four FDA-approved epigenetic drug classes, give one example agent for each, and state in one sentence each the molecular target and why reversibility is the unifying therapeutic principle.
*What this tests: whether you can distinguish the drug classes by mechanism and connect the mechanism to the argument for epigenetic therapy as a category.*

**Application**

4. *[Apply — moderate-hard]* A lncRNA, *HOTAIR*, is overexpressed in a patient's breast cancer. The tumor shows silencing of several tumor suppressor genes whose coding sequences are intact and whose promoters show no mutation. Propose a mechanism linking *HOTAIR* overexpression to the silencing, name the complex involved, and describe the experiment that would test whether *HOTAIR* is necessary for silencing at one specific locus.
*What this tests: applying lncRNA-as-chromatin-guide mechanism to a clinical observation; designing a causal rather than correlative experiment.*

5. *[Apply — moderate-hard]* For each statement, classify it as established mechanism, plausible mechanism, or therapeutic speculation, and justify your classification in one sentence: (a) "IDH inhibitors reverse hypermethylation by lowering 2-hydroxyglutarate." (b) "Cancer stem cells are a distinct, drug-resistant population in every solid tumor." (c) "An m6A RNA modification drives metastasis and is a validated drug target." (d) "miR-15/miR-16 loss releases BCL2 from silencing and promotes CLL cell survival."
*What this tests: calibrating evidentiary confidence — distinguishing a documented causal mechanism from a correlation or a therapeutic hypothesis.*

6. *[Apply — hard]* An EGFR-mutant lung adenocarcinoma progresses on osimertinib. Resequencing finds no new mutation in EGFR and no bypass-pathway mutation. Histology shows transformation to a small-cell neuroendocrine phenotype. Explain step by step why a genetic resistance assay failed to detect the escape mechanism, what epigenetic process drove the transformation, and why the correct next therapeutic step is not a next-generation EGFR inhibitor. Your answer should name the chromatin state that enabled the switch and the transcriptional program that was activated.
*What this tests: integrating phenotypic switching, bivalent chromatin, and the limits of genetic resistance assays into a unified mechanistic account.*

**Synthesis**

7. *[Synthesis — hard]* Build a mechanism map for CLL driven by *miR-15/miR-16* deletion using five nodes: (1) normal B-cell regulation of BCL2 expression; (2) the chromosomal deletion and what it removes; (3) the immediate molecular consequence (BCL2 levels); (4) the cellular phenotype (apoptosis resistance); (5) a therapeutic implication. Label each arrow with the molecular mechanism, and write two sentences explaining why a drug that directly inhibits BCL2 protein (venetoclax) is a rational therapy for this disease, connecting back to node 1.
*What this tests: tracing a regulatory circuit from deleted microRNA to clinical consequence; connecting mechanism to approved therapy.*

8. *[Synthesis — hard]* The IDH-mutant AML case is described as the cleanest mechanistic story in epigenetic oncology because the mutant enzyme produces an oncometabolite that blocks normal demethylase function, and blocking the enzyme restores it. Compare this mechanistic clarity to the cancer stem cell hypothesis: identify what additional evidence would be needed to make the cancer stem cell model equally mechanistically clear, and explain why the current xenotransplantation evidence falls short of that standard.
*What this tests: evaluating mechanistic evidence at different levels of certainty; applying the established-mechanism/plausible-mechanism/speculation framework to a prominent hypothesis.*

**Challenge**

9. *[Challenge — very hard]* The "Still Puzzling" section asks whether therapy-induced phenotypic switching is the *selection* of a rare pre-existing drug-tolerant cell or the *induction* of a new epigenetic state in many cells — and notes that current evidence supports both in different settings. Design a study that would definitively distinguish between these two mechanisms in EGFR-mutant lung adenocarcinoma treated with osimertinib. Specify the experimental system (cell lines, organoids, mouse model, or patient material), the key measurements (single-cell epigenomics, clonal barcoding, live imaging, or others), the critical timepoints, and the result pattern that would support each hypothesis. Then explain why distinguishing selection from induction matters for the clinical strategy of preventing the transformation in the first place.
*What this tests: designing a mechanistically discriminating experiment; connecting the selection-versus-induction distinction to a therapeutic prevention strategy.*

---

## What Would Change My Mind

The chapter's central claim is that the noncoding and reprogramming layer of the epigenome is a genuine, sometimes independent driver of cancer behavior — not merely a readout of upstream genetic events — and that epigenetic states' reversibility makes them therapeutically exploitable. Findings that would force revision: convincing evidence that noncoding RNA changes and phenotypic switches are consistently downstream of and fully explained by genetic alterations; or that therapy-induced reprogramming is in every case driven by a selectable pre-existing mutation rather than an epigenetic state change. The cancer stem cell and reprogramming claims are the most contestable here; stronger lineage-tracing evidence either way would substantially revise this chapter.

## Still Puzzling

- Is therapy-induced reprogramming the selection of a rare pre-existing drug-tolerant cell or the induction of a new epigenetic state in many cells? The answer changes how we would prevent it, and current evidence supports both in different settings.
- Are cancer stem cells a fixed, distinct population or a transient state any cell can enter? The xenotransplant evidence points one way, the plasticity evidence the other.
- How much of the regulatory noncoding RNA we now detect is functional versus transcriptional noise? As detection improves, distinguishing load-bearing lncRNAs from background remains genuinely hard — and bears directly on which are worth targeting therapeutically.

## References

- Signal Transduction and Targeted Therapy. *Epigenetic regulation in the tumor microenvironment.* 2023. https://www.nature.com/articles/s41392-023-01480-x
- Experimental & Molecular Medicine. *Metabolic reprogramming and epigenetic modifications in cancer.* 2023. https://www.nature.com/articles/s12276-023-01020-1
- Hanahan, D. *Hallmarks of Cancer: New Dimensions.* Cancer Discovery, 2022. https://aacrjournals.org/cancerdiscovery/article/12/1/31/675608
- National Cancer Institute. *What Is Cancer?* https://www.cancer.gov/about-cancer/understanding/what-is-cancer
- NCBI Bookshelf. *Molecular Biology of the Cell.* https://www.ncbi.nlm.nih.gov/sites/books/n/mboc4/

---

## Prompts

### Figure 8.1 — oncomiR vs tumor-suppressive microRNA
Build a two-panel mechanism comparison of mirrored silencing chains, left "oncomiR (miR-21 → PTEN)," right "Tumor-suppressive miR (let-7 → RAS)," under axis label "RISC-loaded silencing." Three aligned rows: (1) "miR loaded into RISC" vs "miR loaded into identical RISC" (secondary — emphasize the machinery is the same on both sides); (2) "Silences tumor-suppressor mRNA (PTEN)" vs "Silences oncogene mRNA (RAS)" (sky-blue anchor, the divergence point); (3) "Survival signaling elevated → cell survives" vs "Proliferation reduced → cell held in check" (vermillion, the opposite outcomes). Draw each panel as a small chain: miR + RISC complex → target mRNA → phenotype. The point is identical machinery aimed at opposite target classes produces opposite cancer-relevant outcomes. Subtitle: "Same machinery, opposite directions." Okabe-Ito semantics: neutral secondary for the shared RISC step, sky-blue anchor for the target row, vermillion for the divergent outcomes. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 8.2 — Bivalent chromatin: poised, resolved, re-acquired
Build a top-down hierarchy tree with one root and three branch outcomes, including a re-acquisition loop. Root node: "Bivalent: H3K27me3 + H3K4me3, gene poised (low)" (sky-blue anchor), drawn carrying both a repressive and an activating mark glyph stacked on one histone tail. Three child branches: (1) "Repressive mark lost → gene fires fully" (green, positive resolution); (2) "Activating mark lost → gene silenced" (vermillion, negative resolution); (3) "Cancer re-acquires the poised bivalent pattern" (transitional hue). Draw branches 1 and 2 as normal differentiation forks; draw branch 3 as a curved return/loop arrow back toward the poised root state to convey re-acquisition. Show the dual-mark root resolving to single-mark states, then cancer restoring the dual-mark poised state. Subtitle: "Poised state resolves, then cancer re-acquires it." Okabe-Ito semantics: sky-blue anchor for the poised root, green for activation, vermillion for silencing, transitional hue for the cancer re-acquisition loop. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 8.3 — Polycomb vs Trithorax: opposing memory systems
Build a two-side opposition diagram (mirrored two-column comparison) with a shared central locus, left "Polycomb (repressive)," right "Trithorax (activating)," under axis label "Chromatin memory at the central locus." Three aligned rows: (1) "PRC2 writes repressive mark" vs "KMT2/MLL writes activating mark" (secondary); (2) "PRC1 reads mark, compacts chromatin" vs "SWI/SNF remodels, keeps region open" (secondary); (3) "Gene silenced (off)" vs "Gene active (on)" (vermillion, the opposite endpoints). Place a single shared locus glyph in the center being pulled toward compaction on the left and openness on the right — two opposing arrows converging on one gene. Convey that these are competing memory systems propagating opposite states through division. Subtitle: "Repressive memory vs activating memory at one locus." Okabe-Ito semantics: neutral secondary for the write/read steps, vermillion for the opposed on/off endpoints; keep left (repressive) and right (activating) visually distinct. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.
