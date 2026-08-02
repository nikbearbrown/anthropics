# Chapter 5 — Oncogenes


## TL;DR

- Most oncogenes are not cancer genes.
- The chapter moves through How we found them, What proto-oncogenes do, normally, Three mechanisms of activation, RAS in depth, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

Most oncogenes are not cancer genes. They are normal cellular genes, doing useful work, that have been jammed into the "on" position.

Hold the distinction. There is a tendency in the popular framing to think of oncogenes as foreign — mutant invaders introduced into a cell. They are not. The *KRAS* gene that drives 90 percent of pancreatic cancers is the same *KRAS* that signals embryonic development, that transmits growth-factor signals across every dividing cell in your body, that is required for normal cellular life. A single point mutation — typically a glycine-to-aspartate substitution at position 12 — is what turns the useful gene into the cancer-causing one. The mutation does not change *what RAS does*. It changes *whether RAS turns off when it should*.

This is the deep move that the discovery of oncogenes made. Before the 1970s, the dominant model of cancer was that some external thing — a virus, a carcinogen, a "cancer principle" — converted normal cells to cancer. The discovery that cancer cells carried *altered versions of their own normal genes* was a conceptual revolution. The genes that drive cancer turned out to be the genes that, in unaltered form, drive normal proliferation, normal differentiation, normal survival. Cancer is what happens when those genes are stuck.

There are about 100 known human oncogenes. They fall into a small number of functional categories — growth factors, growth factor receptors, intracellular signaling molecules, transcription factors, cell-cycle regulators. The categories make sense because the cells that grow inappropriately are doing so by misfiring the same machinery that controls normal growth. The mutations cluster in the same hot spots across patient after patient because there are only so many ways to turn a particular protein on inappropriately.

This chapter does five things. It tells you how oncogenes were discovered — through retrovirus research, in a chain of insights that won several Nobel Prizes and reframed cancer biology. It walks through the three main mechanisms by which proto-oncogenes become oncogenes — point mutation, gene amplification, chromosomal rearrangement. It introduces the major oncogene families — RAS, MYC, the receptor tyrosine kinases, the non-receptor tyrosine kinases. It explains how oncogene addiction creates therapeutic opportunities. And it shows how the first generation of targeted cancer drugs — imatinib, trastuzumab, the EGFR inhibitors — are direct descendants of basic oncogene biology.

---

## How we found them

The retrovirus story is one of the great chains of insight in biology, and it deserves to be told carefully because the conceptual moves still organize the field.

In 1911, Peyton Rous, a young researcher at the Rockefeller Institute in New York, isolated a transmissible agent from a sarcoma in a chicken. He could pass a cell-free filtrate from the tumor into healthy chickens and induce new tumors. The filterability told him the agent was smaller than a cell — a virus. The implication was enormous: a virus could cause cancer.

Rous's work was largely ignored for forty years. Mammalian cancers did not behave like the chicken sarcoma; transmissible cancer-causing agents could not be found for the cancers that mattered medically. The reframing took until the 1950s and 60s, when techniques to grow viruses in tissue culture allowed systematic study of the tumor viruses. Rous finally received the Nobel Prize in 1966, for work done 55 years earlier.

The Rous sarcoma virus turned out to be a retrovirus — an RNA virus whose genome is reverse-transcribed into DNA after infection and integrated into the host chromosome. By the late 1960s and early 70s, researchers were systematically dissecting how these viruses transformed cells. The breakthrough came in 1976. Harold Varmus and Michael Bishop, working at UCSF, asked a specific question: where does the *v-src* gene — the transforming gene of the Rous sarcoma virus — come from?

Using molecular hybridization, they discovered that *v-src* had a near-identical counterpart in normal chicken DNA. The viral oncogene was not really a viral gene at all. It was a captured and slightly altered version of a normal cellular gene — a *proto-oncogene*. The virus had picked up the gene during its evolution and rearranged it in a way that drove cancer. The cellular version, *c-src*, was already there, doing normal cellular work.

The implication unfolded over the next decade. If retroviruses carry altered versions of normal cellular genes, then the cellular genes themselves must be capable of causing cancer when altered in similar ways. Non-virally caused cancers — the great majority of human cancers — might involve alterations to the same cellular genes.

The prediction was confirmed in 1982. Three independent groups — Robert Weinberg's at MIT, Michael Wigler's at Cold Spring Harbor, Mariano Barbacid's at NIH — were using DNA transfection assays to identify cancer-causing genes in human tumors. They could take DNA from a human bladder cancer cell line (T24), introduce it into mouse fibroblasts (NIH-3T3 cells), and select for transformed colonies — cells that had taken up the cancer-causing gene. Sequencing identified the gene as a mutated *HRAS* — and the mutation was a single base change converting glycine 12 to valine. The first human oncogene was found. It was a member of the same RAS family that retroviruses had been carrying around for decades.

Bishop and Varmus shared the 1989 Nobel Prize. The conceptual framework they established is now textbook: *proto-oncogenes are normal cellular genes that, when altered by mutation, amplification, or rearrangement, become oncogenes that drive cancer*. About 100 such proto-oncogenes are now known. Almost every signaling pathway that controls cell growth has at least one member that can be turned into an oncogene.

---

## What proto-oncogenes do, normally

The proto-oncogenes are not random genes. They cluster in particular functional categories — the categories that control proliferation. Here is the catalog at the cellular signaling level.

**Growth factors** are secreted proteins that bind receptors on target cells and instruct them to divide. Platelet-derived growth factor (PDGF), epidermal growth factor (EGF), fibroblast growth factor (FGF), vascular endothelial growth factor (VEGF) — these are normal cellular products whose function is to signal proliferation in specific tissues. Their proto-oncogene status comes from the fact that abnormal expression (the cell making its own growth factor and responding to it — *autocrine signaling*) can drive uncontrolled growth. The *v-sis* oncogene of simian sarcoma virus is a viral version of PDGF; its expression in infected cells creates an autocrine loop.

**Growth factor receptors** are transmembrane proteins that detect growth factors and translate that detection into intracellular signaling. Most cancer-relevant ones are *receptor tyrosine kinases (RTKs)* — they have a kinase domain that phosphorylates substrates upon ligand binding. The EGFR family (EGFR, HER2/ERBB2, HER3, HER4), the PDGFR family, the FGFR family, the insulin receptor family, RET, MET, KIT, FLT3 — these are receptors. Their proto-oncogene status comes from the fact that mutations or amplifications can lock the receptor in an active state independent of ligand. The transformation from useful receptor to oncogene typically involves either loss of the ligand-binding regulatory region or amplification to so many copies that even weak signaling becomes overwhelming.

**Non-receptor tyrosine kinases** are intracellular kinases that participate in signaling downstream of receptors. *ABL* (the c-abl gene), *SRC*, *JAK1/2/3* are examples. They are normally controlled by regulatory domains that hold them in an autoinhibited state until the right upstream signal arrives. Cancer mutations frequently disrupt the regulatory domains, freeing the kinase to fire constitutively.

**GTP-binding proteins** are molecular switches. They are active when bound to GTP and inactive when bound to GDP. GTPase-activating proteins (GAPs) hydrolyze GTP to GDP and turn the switch off; guanine nucleotide exchange factors (GEFs) swap GDP for GTP and turn it on. The RAS family — KRAS, HRAS, NRAS — is the most important. RAS proteins are inactive in their GDP-bound form and active in their GTP-bound form. The active form transmits proliferative signals through the RAF/MEK/ERK pathway (the MAPK pathway) and through PI3K/AKT. RAS proteins normally hydrolyze their own GTP slowly; GAPs accelerate the hydrolysis dramatically. Cancer mutations in RAS — most famously at positions 12, 13, and 61 — interfere with GTP hydrolysis, leaving RAS stuck in its GTP-bound active state. The classical analogy is a stuck accelerator: the cell keeps receiving the "grow" signal even when no upstream growth factor is present.

**Serine/threonine kinases** include the RAF family (ARAF, BRAF, CRAF), the AKT family, the mTOR complex, and others. *BRAF V600E* is one of the most common cancer mutations, found in roughly half of all melanomas and in significant fractions of thyroid and colorectal cancers. The mutation locks BRAF in its active state.

**Transcription factors** are proteins that bind DNA at specific sequences and turn target genes on or off. The MYC family (MYC, MYCN, MYCL) is the most cancer-relevant. MYC normally drives expression of genes involved in proliferation and metabolism. Its expression is tightly regulated — MYC protein has a half-life of about 30 minutes, and the mRNA half-life is similar. In normal cells, MYC pulses transiently in response to growth signals and is then turned off. In cancer cells, MYC is often constitutively expressed at high levels, driving constant proliferation and metabolic reprogramming.

**Cell-cycle regulators** include the cyclins, the cyclin-dependent kinases, and the negative regulators of those kinases. *CCND1* (cyclin D1) is amplified or translocated in many cancers. *CDK4/6* are amplified in others. These are points at which the cell-cycle machinery introduced in Chapter 1 can be perturbed in cancer-favoring ways.

**Apoptosis regulators** can also act as oncogenes when they suppress death rather than promote proliferation. *BCL2*, originally identified as the gene at the t(14;18) translocation in follicular lymphoma, is the canonical example. Overexpressed BCL2 prevents mitochondrial release of cytochrome c, blocking the intrinsic apoptosis pathway and letting damaged cells survive when they should die.

The pattern is consistent. Every proto-oncogene is doing normal regulatory work. Every oncogenic mutation locks that work in the "on" position.

---

## Three mechanisms of activation

A proto-oncogene can become an oncogene by any of three main mechanisms.

**Point mutation.** A single base change alters one amino acid in the protein, locking it in a constitutively active state. KRAS G12D — glycine to aspartate at position 12 — is the prototype. The position-12 residue lies near the bound guanine nucleotide; substituting glycine for a bulkier amino acid prevents the side chain from accommodating the GAP-mediated transition state for GTP hydrolysis. The result is a RAS protein that hydrolyzes GTP about 100 times more slowly than normal. It stays GTP-bound. It stays signaling.

The KRAS hot spots — codons 12, 13, and 61 — are mutated in roughly 90 percent of pancreatic ductal adenocarcinomas, 50 percent of colorectal cancers, and 25 percent of lung adenocarcinomas. BRAF V600E in melanoma is another classic point-mutation oncogene. EGFR L858R and EGFR exon-19 deletions in non-small-cell lung cancer (especially in non-smokers and in East Asian populations) are point/indel oncogenes that respond beautifully to EGFR inhibitors. PIK3CA hot-spot mutations (H1047R, E545K) lock the PI3K catalytic subunit in an active state in many breast, endometrial, and colorectal cancers.

What is striking about point-mutation oncogenes is the *narrowness* of where the mutations land. KRAS in pancreatic cancer is essentially always mutated at codon 12 (rarely 13 or 61). Other codons in the gene are not mutated. The reason is selection: only mutations at the GTP-binding regulatory region produce the constitutively active phenotype that confers a growth advantage. Random mutations elsewhere in KRAS are likely neutral or loss-of-function and are not selected.

**Gene amplification.** Multiple copies of the gene appear in the cell, dramatically increasing expression. *MYCN* is amplified in about 25 percent of neuroblastomas and strongly correlates with advanced stage and poor prognosis. *MYC* is amplified in 20 to 30 percent of breast and ovarian cancers. *HER2/ERBB2* is amplified in about 15 to 20 percent of breast cancers and a similar fraction of gastric cancers. *EGFR* is amplified in roughly 50 percent of glioblastomas. *MET* is amplified in a fraction of gastric cancers and acquired-resistance lung cancers.

Amplification produces oncogene activation without mutation — the protein itself is normal but is present at 10, 50, or 100 times the normal level. The cell behaves as if it is receiving overwhelming growth signal from that pathway. Trastuzumab (Herceptin), an antibody against HER2, is one of the first and most successful targeted therapies; it works specifically in HER2-amplified breast cancers, where the elevated receptor density is what makes the tumor growth-dependent.

**Chromosomal rearrangement.** Translocations or fusions create either novel hybrid proteins or place oncogenes under inappropriate regulatory control. The Philadelphia chromosome — the t(9;22) translocation in chronic myeloid leukemia — fuses the *BCR* gene on chromosome 22 to the *ABL1* gene on chromosome 9. The resulting BCR-ABL fusion protein is a constitutively active tyrosine kinase. The ABL kinase, normally tightly regulated by an autoinhibitory domain, loses that regulation in the fusion and fires continuously.

BCR-ABL became one of the most consequential targets in cancer biology because the kinase activity is *the thing the cell now depends on*. Imatinib (Gleevec), approved by the FDA in 2001, is a small-molecule ATP-competitive inhibitor of the ABL kinase. In CML, imatinib produces remission in over 90 percent of patients. The disease that, in 1990, killed most patients within a few years became a chronic condition managed by a daily pill. The story is regularly used as the canonical example of how molecular understanding of an oncogene can lead directly to a cure-like therapy.

Other oncogenic fusions: *ALK* fusions in non-small-cell lung cancer (driven by EML4-ALK and other partners), *ROS1* fusions in lung cancer, *NTRK* fusions in a range of rare tumors. Each is targetable with kinase inhibitors. EML4-ALK lung cancers respond to crizotinib, ceritinib, alectinib, lorlatinib in sequence; NTRK fusions respond to larotrectinib and entrectinib across multiple tumor types.

Translocations can also drive oncogene activation by *enhancer hijacking* without making a fusion protein. In Burkitt lymphoma, the t(8;14) translocation places MYC next to the immunoglobulin heavy-chain enhancers, where it is expressed at the very high levels typical of B-cell genes. The MYC protein is normal; it is its inappropriate expression in inappropriate cell types that drives the cancer. In follicular lymphoma, t(14;18) places BCL2 under similar control. In mantle cell lymphoma, t(11;14) does the same for cyclin D1.

---

## RAS in depth

The RAS family deserves a closer look because it is the most commonly mutated oncogene in cancer and because its biology illustrates several deep principles.

Three RAS genes — *KRAS*, *HRAS*, *NRAS* — encode closely related GTPases. They are membrane-bound proteins about 21 kilodaltons each. They sit at the cytoplasmic face of the plasma membrane, where they receive signals from receptor tyrosine kinases and transmit them downstream. The downstream pathways are several, and they are why RAS matters.

The *RAF/MEK/ERK pathway* (the MAPK pathway) is the major downstream arm. Active RAS recruits RAF (a serine/threonine kinase) to the membrane and activates it. RAF phosphorylates and activates MEK, which phosphorylates and activates ERK. ERK enters the nucleus and phosphorylates transcription factors (FOS, JUN, MYC and others) that drive proliferation-associated gene expression. The pathway is a kinase cascade that amplifies the signal — one active RAS can activate many RAF molecules, each of which can activate many MEK molecules, and so on.

The *PI3K/AKT/mTOR pathway* is the other major arm. Active RAS binds and activates PI3K, which phosphorylates membrane PIP2 to PIP3. PIP3 recruits AKT, which is phosphorylated and activated. AKT phosphorylates dozens of substrates that promote cell survival, glucose uptake, protein synthesis, and growth.

RAS mutations at codon 12 (most common), 13, or 61 lock the protein in its GTP-bound state. The downstream pathways fire constitutively. Cells acquire the proliferative signals they would normally receive only when growth factors are present.

The clinical reality of RAS is that, for decades, it was considered "undruggable." The protein has no obvious druggable pockets — no ATP-binding site like a kinase, no allosteric site that small molecules could plausibly bind. Multiple programs to drug RAS over the 1990s and 2000s failed. Then, in 2013, Kevan Shokat's lab at UCSF discovered that the KRAS G12C mutant — found in about 13 percent of lung adenocarcinomas — has a surface cysteine residue that can be covalently bound by a small molecule. Sotorasib and adagrasib, both G12C-specific inhibitors, were approved by the FDA in 2021 and 2022 respectively for KRAS G12C-mutant lung cancer. The drugs work — modest responses, modest survival benefits — and they prove a principle: even the most undruggable targets can yield to enough creativity and enough biology.

The next frontiers in RAS drugging are G12D inhibitors (the most common pancreatic-cancer mutation), pan-KRAS inhibitors that hit multiple variants, and pan-RAS inhibitors that work across HRAS, KRAS, and NRAS. The pipeline is active. Pancreatic cancer, which is essentially universally KRAS-mutant and has resisted every therapy thrown at it, is the highest-stakes target.

---

## MYC and the transcription factor problem

MYC is arguably the most consequential oncogene in human cancer. It is deregulated in roughly 70 percent of all human cancers — by mutation, amplification, translocation, or upstream pathway activation. It drives expression of thousands of target genes involved in proliferation, ribosome biogenesis, metabolism, and survival. MYC-high cells grow fast and metabolize aggressively.

MYC is also, like RAS, considered classically undruggable. It is a transcription factor — a protein that binds DNA and partners with other transcription factors to recruit RNA polymerase. There is no enzymatic active site to inhibit. The protein is intrinsically disordered for much of its length, which makes structure-based drug design difficult. Several decades of attempts to drug MYC directly have produced little.

The alternative strategy is to drug the things MYC depends on. Cancers driven by MYC are often particularly dependent on specific metabolic pathways, on specific transcriptional cofactors (BRD4, the BET bromodomain protein, has been pursued), on specific translation machinery, on specific stress-response pathways. The synthetic-lethal logic — find what MYC-driven cells need that normal cells do not — has been the productive direction.

The MYC family also illustrates how proto-oncogenes are normally regulated. MYC mRNA has a short half-life (around 30 minutes). MYC protein has a short half-life (also around 30 minutes). Normal cells produce MYC in transient pulses in response to growth signals. The pulses drive a wave of target gene expression and then subside. Cancers that have lost the regulation — either by transcriptional deregulation (translocation, amplification) or by stabilization of the protein (mutations that prevent its degradation) — produce constant high levels of MYC, and the cell is permanently in proliferation mode.

---

## Oncogene addiction and the principle of targeted therapy

One of the most useful concepts in cancer therapeutics is *oncogene addiction*. A cancer cell that has acquired a particular driver mutation often becomes dependent on the signaling from that mutated gene. The downstream pathways that the oncogene activates are wired into nearly every aspect of the cell's behavior. If you inhibit the oncogene, the cell collapses.

The clinical reality of oncogene addiction is dramatic. A CML patient on imatinib goes from rapidly dying leukemia to a stable hemogram within weeks. A *BRAF V600E* melanoma patient on vemurafenib watches large tumors shrink in months. A *EGFR*-mutant lung cancer patient on osimertinib achieves a response that classical chemotherapy never produced. The targeted drugs work because the cancer cell *needs* the oncogene's output. Take it away, and the cell has nothing to fall back on.

Oncogene addiction is not unlimited. Resistance emerges, almost always, eventually. The mechanisms are several: a *secondary mutation* in the target that prevents drug binding (the gatekeeper T790M mutation in EGFR, the T315I mutation in BCR-ABL); *amplification* of the target to overwhelm the drug; *bypass activation* of a parallel signaling pathway (MET amplification as a resistance mechanism in EGFR-mutant lung cancer); *phenotypic switching* (small-cell transformation in EGFR-mutant lung adenocarcinoma; mesenchymal transition); *loss of the target* by epigenetic or genetic means. Modern targeted therapy increasingly uses sequential drugs that anticipate likely resistance mutations — first-generation EGFR inhibitor, second-generation, third-generation; first-line BCR-ABL inhibitor, second-line for T315I, third-line.

The deeper principle is that oncogene-driven cancers behave as if they have placed a large bet on a particular biological strategy. The bet works while the environment cooperates. The bet fails when the environment changes. Targeted therapy *is* the environmental change — a sudden inability to use the oncogene's output. The cancer either dies (response), evolves around the obstacle (resistance), or, in some cases, adapts in ways that buy time but eventually fail.

---

## What this chapter gives you

Oncogenes are normal cellular genes — proto-oncogenes — that drive proliferation in healthy tissues and that become cancer drivers when mutated, amplified, or rearranged in ways that lock them in their active state. They fall into a small number of functional categories — growth factors, receptors, signaling kinases, transcription factors, cell-cycle regulators, apoptosis regulators — and the mutations that activate them cluster in predictable places. The categories make sense because cancer is, at one level, just the cell receiving too much "grow" signal through one or more of the normal pathways.

The targeted therapy revolution of the last 25 years — imatinib, trastuzumab, the EGFR inhibitors, the BRAF inhibitors, the ALK inhibitors, the RAS inhibitors — is the direct clinical application of oncogene biology. The conceptual structure is identical across all of them: identify the driver mutation in the patient's tumor, identify the protein product the cell now depends on, design a drug that specifically blocks that protein, treat the tumor that carries the mutation. The list of druggable oncogenes is still expanding. Pan-cancer genomic profiling — sequencing every tumor's driver mutations and matching them to the targeted therapies most likely to work — has become standard practice in many cancer centers.

The other half of the cancer-genetics picture — what happens when the *brakes* are lost rather than the *accelerators* stuck — is Chapter 6.

---

## LLM exercises

1. Ask your LLM to walk you through the original Bishop-Varmus experiments that identified c-src as the cellular counterpart of the Rous sarcoma virus oncogene. What experimental techniques did they use? Then probe the LLM on why these experiments were considered conceptually revolutionary rather than just technically clever.

2. Have your LLM list the top 15 oncogenes by frequency of mutation in human cancers. For each, ask it to identify the canonical hot-spot mutations, the cancers most affected, and any FDA-approved targeted therapy. Then ask it which oncogenes on the list are still considered "undruggable" and what current therapeutic approaches are being pursued for them.

3. Use your LLM to construct a clinical case: a 55-year-old with newly diagnosed non-small-cell lung cancer. Ask the LLM to walk through the molecular workup — what genes get tested, what targeted therapies match which mutations, what the expected response rates and survival benefits are. Then probe: which of the LLM's recommendations are evidence-based and which are extrapolations?

4. Ask your LLM to explain oncogene addiction using an analogy from outside biology (engineering, economics, sports, anything else that works). Evaluate the analogy: does it illuminate the dependence on the driver, or does it just decorate the concept? What aspects of oncogene addiction does the analogy miss?

5. Have your LLM identify three recent (post-2020) approvals of targeted oncology drugs for specific oncogene-driven cancers. For each, ask it to describe the path from initial discovery of the oncogenic alteration to the FDA approval — how long it took, what evidence was needed, what the response rates and survival benefits looked like. Note any patterns about how fast (or slow) the translational pipeline runs.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Peyton Rous** discovered in 1911 that a chicken sarcoma could be transmitted by a cell-free filtrate — implying a viral cause of cancer. The field rejected the idea for decades. He won the Nobel Prize in 1966 at age 87, for the work he had done at 30.

**Run this:**

```
Who was Peyton Rous, and how does his discovery of the Rous sarcoma virus connect to the oncogene biology we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Peyton Rous"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to trace the path from Rous's 1911 chicken sarcoma virus to the 1976 discovery that *src* is a normal cellular gene hijacked by a retrovirus.
- Ask it about why Rous's discovery was rejected for so long — what does it say about disciplinary resistance?

What changes? What gets better? What gets worse?
