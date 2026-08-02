# Chapter 7 — Epigenetics in Cancer: The Methylation and Histone Code

Two patients have glioblastoma. Same diagnosis, same surgery, same radiation, same chemotherapy — temozolomide, a drug that damages tumor DNA by attaching methyl groups to guanine bases. One survives far longer than the other. Their tumors look identical under the microscope and carry overlapping mutations. The decisive difference is a chemical mark on a single gene's promoter.

The gene is *MGMT*. Its protein's only job is to remove exactly the kind of DNA damage temozolomide causes. In the longer-surviving patient, the *MGMT* promoter is hypermethylated — silenced by a methyl group added to cytosine in the DNA — so the repair protein is never made, the drug's damage accumulates, and tumor cells die. In the other patient, *MGMT* is expressed, the damage is repaired, and the drug is largely wasted. No gene sequence differs between them. No mutation. The decisive variable is a layer of regulation written *on top of* the DNA.

This is the central fact of cancer epigenetics: cancer is not only a disease of broken genes but of misread ones. This chapter explains how that misreading happens, and whether reversing it is as tractable as it first appears.

---

## What epigenetics means, precisely

A neuron, a liver cell, and a skin cell carry the same roughly 20,000 protein-coding genes. What distinguishes them is not DNA sequence — it is the **epigenome**: the set of chemical marks layered onto DNA and onto the histone proteins that package it, controlling which genes are read and which are silenced.

**Epigenetics** refers to heritable changes in gene expression that do not involve changes to DNA sequence. The marks are chemical: methyl groups on cytosine bases, acetyl and methyl groups on histone tails. And they persist through cell division. The system has memory because the marks are enzymatically maintained. After DNA replicates, the new strand carries no methylation. The maintenance methyltransferase DNMT1 recognizes the resulting hemimethylated state — one strand marked, one not — and methylates the daughter strand to match the parent. A skin cell stays a skin cell across hundreds of divisions because its epigenetic state is faithfully copied each time the genome is copied.

That memory is why epigenetics matters for cancer. Once a tumor suppressor is silenced by methylation, the silencing is inherited by every daughter cell without any new mutation required. The lineage drifts from its tissue identity, and the changes accumulate the way mutations do — except that, in principle, they are reversible. The gene sequence is intact. The book is still there; someone has taped the covers shut.

<!-- → [DIAGRAM: same genome, three cell types — identical DNA sequence with different methylation/histone-mark patterns producing neuron, hepatocyte, skin cell] -->

---

## DNA methylation and cancer's paradox

In mammals, DNA methylation occurs overwhelmingly at **CpG dinucleotides** — cytosine followed by guanine — where a methyl group is added to the cytosine. Because CpG is palindromic across the two strands, the mark survives replication: DNMT1 reads the hemimethylated site and restores it.

Most CpG sites in the genome are methylated — necessary to keep repetitive, transposon-derived sequences silent and the genome stable. The exceptions are **CpG islands**: short, CpG-dense stretches near the transcription start sites of most genes, normally kept unmethylated so transcription can proceed. When a CpG island becomes hypermethylated, the gene downstream is reliably silenced.

In cancer, two opposite things happen to methylation simultaneously — and the paradox dissolves once you see that they involve different machinery and different regions of the genome.

**Global hypomethylation** of the bulk genome: the overall methylation level of a cancer cell is *lower* than normal, especially at repetitive and intergenic regions. Transposable elements that should be silent reactivate. The genome becomes more prone to recombination. Chromosomal instability rises. This was the first epigenetic abnormality observed in human tumors, described by Feinberg and Vogelstein in 1983 — before the promoter hypermethylation story was fully developed.

**Focal hypermethylation at CpG islands** at specific tumor suppressor promoters: individual cancer-relevant genes are silenced not by mutation but by methyl marks selectively deposited on their promoters. *CDKN2A* (encoding the CDK inhibitor p16) is silenced this way in many cancers. *MLH1* is methylated in roughly 15% of sporadic colorectal cancers — phenocopying the germline mismatch-repair loss of Lynch syndrome, producing microsatellite instability through an epigenetic route rather than a mutational one. *BRCA1* is methylated in some sporadic ovarian and breast cancers, mimicking the inherited mutation. Same functional outcome, different mechanism, no sequence change.

The two patterns reflect different machinery — failing maintenance on the bulk genome, versus selected silencing at specific promoters — and both favor the cancer. One destabilizes the genome broadly; the other removes specific brakes on proliferation.

![Methylation paradox: bulk genome loses marks while CpG-island promoters gain them](images/07-epigenetics-in-cancer-the-methylation-and-histone-code-fig-03.png)
*Figure 7.3 — The methylation paradox*

What makes promoter methylation therapeutically interesting is the reversibility. Remove the methyl groups and transcription can resume. **DNA methyltransferase inhibitors** — azacitidine and decitabine — are cytosine analogs that incorporate into replicating DNA, trap DNMT1 in a covalent complex, and let methylation be lost over a few divisions, reactivating some silenced genes. Azacitidine, approved for myelodysplastic syndrome in 2004, was the first epigenetic cancer drug. Both are now standard for MDS and elderly AML.

---

## The histone code

The second major layer of epigenetic control is on the histones. The structural unit of chromatin is the **nucleosome** — roughly 147 base pairs of DNA wrapped around an octamer of histone proteins (two each of H2A, H2B, H3, and H4). The histones are not passive packaging. Their N-terminal tails project out from the nucleosome surface and carry a dense set of chemical marks that are written by one class of enzymes, erased by another, and read by a third.

The vocabulary that recurs throughout cancer biology:

**Histone acetylation** adds an acetyl group to a lysine residue. Written by histone acetyltransferases (HATs), removed by histone deacetylases (HDACs). Acetylation neutralizes the lysine's positive charge, loosens histone–DNA contacts, and opens chromatin for transcription. Acetylation is generally activating. H3K27ac marks active enhancers.

**Histone methylation** adds methyl groups to lysines or arginines. Written by methyltransferases (KMTs), removed by demethylases (KDMs). Its meaning depends entirely on position and the degree of methylation. H3K4me3 marks active gene promoters. H3K27me3 marks Polycomb-repressed, silenced regions. H3K9me3 marks densely packed heterochromatin. The same chemical modification — methylation — means opposite things depending on which residue carries it.

**Reader** proteins recognize specific marks and recruit downstream machinery. Bromodomains read acetyl-lysines; chromodomains read methyl-lysines. A single nucleosome can carry many marks at once, and their combination is interpreted by multiple readers simultaneously. This is the combinatorial language — the histone code — and cancer frequently rewrites it.

![The histone code: writer enzymes add marks, readers recruit machinery, erasers remove marks](images/07-epigenetics-in-cancer-the-methylation-and-histone-code-fig-04.png)
*Figure 7.4 — The histone code: write / read / erase*

---

## When the code is corrupted

The enzymes that write, erase, and read histone marks are mutated at high frequency in cancer. Bladder cancer is the extreme case: roughly 80% carry mutations in chromatin-modifying genes. Most are loss-of-function — the cell loses the ability to maintain the correct marks — and the consequence is a transcriptome shifted toward proliferation or de-differentiation.

Three patterns recur across cancer types.

**Gain-of-function in repressive complexes.** The Polycomb Repressive Complex 2 writes H3K27me3, silencing developmental genes that should remain accessible. Activating mutations in *EZH2* — the PRC2 catalytic subunit — deepen and broaden this silencing in some lymphomas. This is directly druggable: tazemetostat, an EZH2 inhibitor, was approved in 2020 for EZH2-mutant follicular lymphoma. The drug works by blocking the enzyme that writes the repressive mark, allowing silenced tumor suppressors and differentiation genes to reactivate.

**Loss-of-function in activating complexes.** *KMT2A* (MLL1), which writes H3K4me3 at active gene promoters, is rearranged — fused to various partner genes — in infant leukemias, producing a chimeric protein that activates proliferative targets in a manner no longer subject to normal controls. The mark that supports normal transcription is turned into a constitutive activator.

**Chromatin-remodeler disruption.** The SWI/SNF complex uses ATP hydrolysis to reposition nucleosomes, making specific genomic regions accessible or inaccessible. Subunits of SWI/SNF — particularly *ARID1A*, *SMARCA4*, *SMARCB1* — are mutated in roughly 20% of all human cancers, making SWI/SNF the most frequently mutated chromatin complex in cancer. Loss-of-function in SWI/SNF impairs the opening of tumor-suppressor loci and differentiation-gene loci, locking cells in a more stem-like, proliferative state.

**HDAC inhibitors** — vorinostat and romidepsin were early approvals — hyperacetylate histones genome-wide to reactivate silenced genes. Their clinical activity has been concentrated in blood cancers. In solid tumors they have largely disappointed, partly because pan-HDAC inhibition hits many targets indiscriminately and produces toxicity out of proportion to benefit. Isoform-selective HDAC inhibitors are in development, hoping to capture the benefit while narrowing the mechanism.

---

## The metabolic connection

There is a subtlety that the enzyme-centric picture of epigenetics obscures: the enzymes that write and erase chromatin marks use small-molecule metabolites as cofactors, which means the cell's metabolic state directly shapes its epigenetic state.

S-adenosylmethionine is the methyl donor for all methyltransferases — DNA and histone. α-ketoglutarate (αKG) is the cosubstrate for the TET DNA demethylases and the Jumonji histone demethylases. Acetyl-CoA supplies the acetyl groups for histone acetyltransferases. NAD+ is required by sirtuin deacetylases. When metabolic enzyme activity changes, cofactor availability changes, and the epigenome shifts.

The cleanest example is IDH1/IDH2 mutation. Isocitrate dehydrogenase normally converts isocitrate to αKG in the TCA cycle. The cancer-associated IDH mutation creates a neomorphic enzyme that converts αKG to **2-hydroxyglutarate (2HG)** instead. 2HG is a structural mimic of αKG — close enough to compete for the active sites of αKG-dependent demethylases, but unable to complete the reaction. TET enzymes (which demethylate DNA) and Jumonji-domain histone demethylases are both inhibited. Methylation accumulates aberrantly across the genome. Tumor suppressors silence. Differentiation programs lock.

IDH mutations appear in roughly 70% of low-grade gliomas and about 10% of AML. And they are druggable in a way that makes the metabolic–epigenetic coupling therapeutically concrete: ivosidenib (targeting IDH1) and enasidenib (targeting IDH2) reduce 2HG levels by blocking the neomorphic enzyme. As 2HG falls, αKG-dependent demethylases regain function, methylation patterns normalize, and differentiation resumes. Leukemic blasts mature into functional cells. The epigenetic lock, caused by a metabolic enzyme carrying a single amino acid change, is released by a small molecule that reverses the metabolic error.

![IDH mutation makes 2HG, which blocks demethylases so methylation accumulates; an inhibitor reverses it](images/07-epigenetics-in-cancer-the-methylation-and-histone-code-fig-01.png)
*Figure 7.1 — IDH mutation to 2HG to demethylase blockade*

This is the sharpest demonstration that reversibility is real — that a methylation state accumulated over years can be cleared by removing its cause — and it grounds the optimism about epigenetic therapy in something more than aspiration.

---

## Back to MGMT, and what it teaches

Return to the opening case. Temozolomide attaches a methyl group to the O6 position of guanine. During replication, O6-methylguanine mispairs with thymine, introducing mismatches that, if abundant, trigger cell death. The *MGMT* protein's only job is to transfer that methyl group to its own cysteine residue and deactivate itself — one repair event per enzyme molecule, a suicide mechanism. So MGMT expression determines whether the drug's damage persists long enough to kill.

In a tumor with a hypermethylated, silenced *MGMT* promoter, no MGMT protein is made, the O6-methylguanine lesions accumulate, and the cells die. In a tumor with an expressed *MGMT* gene, the damage is repaired and the cells survive. The test is a methylation-specific PCR or bisulfite sequencing of the promoter region — technically straightforward, clinically decisive.

The intuition to resist here: "more DNA repair should be better for the patient." That intuition applies when the patient's normal tissue is being damaged. Here the drug is trying to damage the *tumor*, and MGMT protects the tumor. A patient whose tumor repairs efficiently is a patient whose drug is being neutralized. The methyl mark that silences the repair gene is, from the patient's perspective, a stroke of luck — and a predictive biomarker that guides how aggressively to use the drug.

MGMT methylation status is now standard in glioblastoma management. It is the clearest example in oncology of an epigenetic mark serving as a predictive biomarker: not prognostic (not predicting how long the patient will live regardless of treatment), but predictive (predicting differential benefit from a specific treatment based on a molecular feature of the tumor).

![MGMT methylation decision tree: methylated promoter means the drug works, unmethylated wastes it](images/07-epigenetics-in-cancer-the-methylation-and-histone-code-fig-02.png)
*Figure 7.2 — MGMT methylation decision tree*

<!-- → [DIAGRAM: MGMT methylation decision tree — methylated promoter → silenced repair → temozolomide damage accumulates → cell death (drug works); unmethylated → MGMT expressed → damage repaired → cell survives (drug wasted)] -->

---

## The limits of reversibility

Epigenetic marks are reversible in principle. The DNMT inhibitors and HDACi demonstrate reversibility in practice. So why is the epigenetic drug story not simpler than it has turned out to be?

The answer is that "reversible" does not mean "easily corrected." The same enzymes that establish cancer-associated marks also regulate normal gene expression genome-wide. DNMT inhibitors reactivate not just silenced tumor suppressors but also retrotransposons, inflammatory response genes, and imprinted loci. HDAC inhibitors deacetylate not one target but thousands. The breadth of effect is both why these drugs work — reactivating multiple silenced programs simultaneously — and why they produce broad toxicity and inconsistent benefit across solid tumors.

The success in blood cancers and the failure in most solid tumors likely reflects a difference in chromatin state entrenchment. Hematopoietic cancers are relatively early in their epigenetic drift — silenced genes can be reactivated by removing the marks. Solid tumors that have been accumulating epigenetic changes across years and many cell generations may have reached states where the mark is necessary but not sufficient: removing the methyl groups does not clear the dense heterochromatin machinery that has been recruited on top of them. The book's covers are no longer just taped; the pages have been glued.

The IDH inhibitor story is the exception because it works by removing the metabolic driver of hypermethylation, not just the methylation itself. When 2HG falls, the demethylases regain their normal activity and the system moves toward its default state. It is closer to removing the cause than to correcting the consequence.

---

## What would change this picture

The chapter's central claim is that epigenetic dysregulation is a genuine, independent driver of cancer — capable of silencing tumor suppressors and reshaping phenotype without sequence change — and that it is pharmacologically reversible under the right conditions. The findings that would force revision: convincing evidence that canonical epigenetic abnormalities (CpG-island hypermethylation, IDH-driven hypermethylation) are consistently *downstream consequences* of mutations rather than independent contributors; or robust evidence that demethylating and IDH-inhibiting drugs produce no durable reactivation of silenced genes and no phenotypic reversal across well-controlled trials. The IDH inhibitor response — tumors regressing and differentiation resuming as 2HG falls — is the strongest causal evidence that epigenetic state drives the disease independently. A reproducible failure to replicate that result would undercut the framework.

---

## Still open

Why DNMT inhibitors and HDAC inhibitors work in blood cancers but largely fail in solid tumors is not settled. Candidate explanations include chromatin-state entrenchment, microenvironmental differences, and drug delivery, but no clean discriminating experiment has been done.

Whether global hypomethylation and focal hypermethylation arise independently or whether one precipitates the other — and whether the order matters therapeutically — is an open question. They are products of different machinery, but they coexist in the same cell, and their interaction is not well mapped.

And if a tumor suppressor can be silenced by methylation or by mutation with the same functional result, what determines which route a given cancer takes in a given tissue? The answer probably involves the epigenetic landscape of the cell of origin and the available mutational and metabolic pressures, but the specific rules are not known.

---

## LLM Exercises

1. **(Paradox)** Explain why a cancer cell can simultaneously show global hypomethylation of the bulk genome and focal hypermethylation of CpG islands at tumor suppressor promoters. What machinery is responsible for each, and how does each contribute to the cancer phenotype? Construct the argument that these two patterns are not contradictory but complementary cancer mechanisms.

2. **(Epigenetic mimicry)** A sporadic ovarian cancer has wild-type *BRCA1* sequence by exome sequencing but no detectable BRCA1 protein. Propose an epigenetic explanation. Predict whether this tumor would respond to a PARP inhibitor, identify the mechanism of any response, and describe what evidence you would need to confirm the epigenetic explanation versus an alternative (e.g., post-translational regulation).

3. **(Histone code table)** For each of the following marks, identify the writer enzyme class, the eraser enzyme class, an example reader domain, and whether the mark generally indicates active or repressed transcription: H3K4me3, H3K9me3, H3K27me3, H3K27ac. Then predict the transcriptional consequence of simultaneously losing the H3K27me3 writer (EZH2) and gaining the H3K27ac writer (p300) at the same locus.

4. **(IDH chain)** Trace the complete chain from IDH mutation to epigenetic phenotype: name the neomorphic product, the enzymes it inhibits, the chromatin marks that accumulate as a result, and the gene-expression consequence. Then explain why an IDH inhibitor reverses an epigenetic phenotype even though IDH is a metabolic enzyme. Classify each step as established mechanism, established therapeutic implication, or still under investigation.

5. **(MGMT as predictive biomarker)** Distinguish a prognostic biomarker from a predictive biomarker, then classify MGMT methylation status and justify the classification. A glioblastoma patient has an unmethylated *MGMT* promoter. Their neuro-oncologist is considering forgoing temozolomide and enrolling them in a trial of an experimental drug. Using the mechanism developed in this chapter, construct the strongest argument for the trial enrollment decision and the strongest argument against it.

---

## References

- Signal Transduction and Targeted Therapy. *Epigenetic regulation in the tumor microenvironment.* 2023. https://www.nature.com/articles/s41392-023-01480-x
- Experimental & Molecular Medicine. *Metabolic reprogramming and epigenetic modifications in cancer.* 2023. https://www.nature.com/articles/s12276-023-01020-1
- National Cancer Institute. *What Is Cancer?* https://www.cancer.gov/about-cancer/understanding/what-is-cancer
- Hanahan, D. *Hallmarks of Cancer: New Dimensions.* Cancer Discovery, 2022. https://aacrjournals.org/cancerdiscovery/article/12/1/31/675608
- NCBI Bookshelf. *Molecular Biology of the Cell.* https://www.ncbi.nlm.nih.gov/sites/books/n/mboc4/

---

## Prompts

### Figure 7.1 — IDH mutation to 2HG to demethylase blockade
Build a horizontal left-to-right causal-chain flowchart with one competitive-block step and a reversal branch. Five numbered nodes: (1) Mutant IDH enzyme (sky-blue anchor); (2) alpha-ketoglutarate substrate; (3) 2-hydroxyglutarate (aKG mimic) (vermillion, negative); (4) DNA & histone demethylases switched off; (5) Methyl marks accumulate, gene silenced (transitional hue). Use straight arrows for steps 1→2, 2→3, 4→5, but render the 3→4 relation as a distinct blocking edge labeled "competitive block" (vermillion barrier glyph). Add a separate reversal callout beneath the main chain: "IDH inhibitor blocks mutant IDH → demethylases reactivate, gene re-expressed," drawn as a return arrow that lifts the block. Emphasize the oncometabolite (node 3) as the villain and the inhibitor reversal as the therapeutic payoff. Subtitle: "Oncometabolite blocks demethylases; inhibitor reverses it." Okabe-Ito semantics: sky-blue anchor for mutant IDH, vermillion for 2HG and the competitive block, transitional hue for the silenced-gene endpoint. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 7.2 — MGMT methylation decision tree
Build a top-down two-branch decision tree. Root node: "MGMT promoter status." Two branches descend. Left branch: "Methylated → repair silenced" (green, favorable) → child "DNA damage accumulates" (secondary) → child "Tumor cell dies (favorable)" (green). Right branch: "Unmethylated → repair expressed" (vermillion, unfavorable) → child "DNA repaired" (secondary) → child "Tumor cell survives (drug wasted)" (vermillion). Use clean parent-child link lines, two symmetric vertical chains. The teaching point is counterintuitive: the silenced-repair (methylated) branch is the good outcome for the patient under temozolomide. Make the two terminal outcomes visually opposed (green favorable vs vermillion wasted). Subtitle: "Methylated promoter means the drug works." Okabe-Ito semantics: green for the favorable methylated branch, vermillion for the unfavorable unmethylated branch, neutral secondary for intermediate steps. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 7.3 — The methylation paradox
Build a two-panel comparison of the same genome, left "Bulk / repetitive genome," right "CpG-island promoter," under axis label "Methylation change in cancer." Three aligned rows: (1) "Normal: densely methylated" vs "Normal: bare, gene active" (green, the healthy baseline); (2) "Cancer: hypomethylated, sparse" vs "Cancer: hypermethylated, dense" (transitional hue, the change); (3) "Transposon reactivated, genome destabilized" vs "Tumor suppressor silenced" (vermillion, negative outcome). Visually depict methylation density with dot/lollipop glyphs along a DNA strand: dense dots that thin out on the left under cancer, sparse dots that fill in on the right under cancer — the two panels moving in opposite directions. The paradox is the mirror-image change. Subtitle: "Bulk loses marks; islands gain marks." Okabe-Ito semantics: green for the normal baseline, transitional hue for the cancer state, vermillion for both harmful outcomes. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 7.4 — The histone code: write / read / erase
Build a node-edge systems diagram centered on a nucleosome. Central node: "Nucleosome (DNA on histone octamer) with N-terminal tail" (sky-blue anchor), drawn as DNA wrapped around a histone core with a projecting tail. Three enzyme-class nodes around it: "Writer enzyme adds a mark" (green, positive) with an arrow to the nucleosome labeled "deposit"; "Reader docks on a mark" (blue, dominant) with an arrow to the nucleosome labeled "dock" and a second arrow to a fourth node "Downstream machinery recruited" labeled "recruit"; "Eraser enzyme removes a mark" (vermillion, negative) with a blocking/removal edge to the nucleosome labeled "remove." Show the write/read/erase triad acting on the same nucleosome tail, with the reader as the relay to downstream effects. Subtitle: "Writers add, readers recruit, erasers remove." Okabe-Ito semantics: green writer, blue dominant reader, vermillion eraser, sky-blue anchor nucleosome. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.
