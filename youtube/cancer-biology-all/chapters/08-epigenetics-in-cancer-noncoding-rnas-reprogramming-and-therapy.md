# Chapter 8 — Epigenetics in Cancer: Noncoding RNAs, Reprogramming, and Therapy


## TL;DR

- The genome was supposed to encode proteins.
- The chapter moves through MicroRNAs in cancer, Long noncoding RNAs, Polycomb and Trithorax: cellular memory, Reprogramming and cancer stem cells, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

The genome was supposed to encode proteins. Then we counted, and the math didn't work.

When the Human Genome Project finished in 2003, the count of protein-coding genes came in at around 20,000 — surprising on the low side. *Drosophila melanogaster* has roughly 14,000 protein-coding genes. *Caenorhabditis elegans* has 20,000. A roundworm and a human, by protein-coding count, are nearly tied. But humans are obviously more complicated than roundworms in any meaningful sense. The extra complexity had to be encoded somewhere — and the obvious place to look was the 98 percent of the genome that does *not* encode protein.

That 98 percent turned out to be active. It transcribes RNA — much of it, all the time. Most of the RNA is never translated into protein. Some is structural (ribosomal RNA, transfer RNA). Most is regulatory. The regulatory RNAs come in many flavors: microRNAs (miRNAs) of 18 to 25 nucleotides; small interfering RNAs (siRNAs); long noncoding RNAs (lncRNAs) of hundreds to thousands of bases; small nucleolar RNAs (snoRNAs); piwi-interacting RNAs (piRNAs); circular RNAs; enhancer RNAs. The list keeps growing as sequencing technology gets better at detecting low-abundance transcripts.

For cancer biology, the noncoding RNAs matter because they regulate gene expression, and cancer is in large part a disease of misregulated gene expression. miRNAs targeting tumor suppressor mRNAs are upregulated in many cancers; miRNAs targeting oncogene mRNAs are downregulated. Long noncoding RNAs participate in transcription, splicing, chromatin organization, and post-transcriptional control. Cancers reprogram the noncoding RNA landscape extensively, and increasingly the field is finding diagnostic biomarkers, prognostic signatures, and therapeutic targets in this layer of the transcriptome.

This chapter — the second on epigenetics — picks up where 7A left off. It covers the noncoding RNAs and what they do in cancer. It introduces the Polycomb-Trithorax system that maintains cellular identity. It walks through the bigger picture of *epigenetic reprogramming* in cancer — how the chromatin landscape of a cancer cell as a whole differs from that of its tissue of origin. And it surveys epigenetic therapy: the drugs already in clinic, the targets under development, and the principle that epigenetic therapy is most powerful when paired with other modalities.

---

## MicroRNAs in cancer

MicroRNAs are short RNAs — 18 to 25 nucleotides long — that bind partially complementary sites in the 3' untranslated regions of target messenger RNAs and silence them, either by causing translational repression or by recruiting mRNA degradation machinery. The miRNA-Argonaute complex (the RNA-induced silencing complex, or RISC) is the agent of silencing.

The biogenesis pathway is conserved across animals. A long primary transcript (pri-miRNA) is cleaved in the nucleus by the Drosha-DGCR8 complex to produce a 60-80 nucleotide pre-miRNA hairpin. The hairpin is exported to the cytoplasm by Exportin-5 and cleaved by Dicer to release the mature miRNA duplex. One strand (the guide strand) is loaded into Argonaute; the other strand is degraded. The loaded RISC then scans cytoplasmic mRNAs for matching sequences.

The first miRNA was discovered in *C. elegans* in 1993. By the early 2000s, miRNAs had been found in mammals; by the mid-2000s, miRNA dysregulation in cancer was an established phenomenon. The human genome encodes roughly 2,000 miRNAs, and a single miRNA can target hundreds of mRNAs. The regulatory reach is enormous.

In cancer, miRNAs are deregulated in characteristic patterns. *miR-21*, the most extensively studied oncogenic miRNA, is upregulated in essentially every solid cancer studied — breast, colorectal, lung, pancreatic, ovarian, brain, prostate. Its targets include the tumor suppressors PTEN, PDCD4, and TPM1. Upregulation of miR-21 silences these tumor suppressors and contributes to invasion and metastasis. *miR-155* is upregulated in many hematologic cancers and some solid tumors and is implicated in B-cell lymphomagenesis. *miR-17~92* (a cluster of six miRNAs from a single transcript) is amplified or overexpressed in many lymphomas and is a *MYC* target.

Other miRNAs function as tumor suppressors. The *let-7* family targets several oncogenes including *RAS* and *MYC*. Loss of *let-7* expression is common in lung adenocarcinoma and other cancers. *miR-34a* is a p53 target and contributes to p53's tumor-suppressive function by targeting pro-proliferative and anti-apoptotic genes; loss of *miR-34a* is common in cancers with p53 mutations and contributes to the phenotype.

The clinical applications of miRNAs have been pursued on two fronts.

*Diagnostic and prognostic biomarkers.* miRNAs are stable in blood, plasma, and other body fluids. They survive degradation that destroys mRNA. Specific miRNA signatures in plasma have been proposed for early detection of lung cancer, colorectal cancer, breast cancer, and others. The performance in clinical practice has been modest — sensitivity and specificity are not yet adequate for screening — but the principle is sound, and continued refinement is ongoing.

*Therapeutic targeting.* Two approaches: deliver miRNA mimics for tumor-suppressive miRNAs that the cancer has lost, or deliver anti-miRs (locked nucleic acids or other inhibitors) for oncogenic miRNAs that the cancer has upregulated. Clinical trials of miRNA-based therapies have produced mixed results, mainly because of delivery challenges — getting nucleic acids into solid tumors at therapeutic doses is hard. MRX34, a miR-34a mimic, entered early clinical trials in 2013 but was halted in 2016 due to immune-related toxicity. Other miRNA-targeting drugs remain in development. The therapeutic potential is plausible; the delivery problem is harder than it looks.

---

## Long noncoding RNAs

Long noncoding RNAs (lncRNAs) are transcripts longer than 200 nucleotides that lack protein-coding potential. The human genome encodes tens of thousands of them — the count keeps rising as detection improves. Functionally they are heterogeneous. Some operate as scaffolds for protein complexes. Some guide chromatin-modifying enzymes to specific genomic loci. Some sponge miRNAs, removing them from the regulatory pool. Some compete with mRNAs for ribosomes. Some are intrinsically disordered and form phase-separated condensates.

The first cancer-implicated lncRNA was *H19*, an imprinted lncRNA expressed from the maternal allele at chromosome 11p15. *H19* is overexpressed in many cancers — bladder, breast, hepatocellular, pancreatic — and promotes invasion, metastasis, and resistance to therapy. Some early reports framed *H19* as a tumor suppressor; the bulk of subsequent evidence supports an oncogenic role in most contexts.

*HOTAIR* is a lncRNA transcribed from the HOXC locus that interacts with the Polycomb Repressive Complex 2 (PRC2) and guides it to specific genomic sites. *HOTAIR* overexpression is found in breast, colorectal, hepatocellular, lung, gastric, and many other cancers, and correlates with aggressive disease and poor prognosis. The mechanism is straightforward: *HOTAIR* directs PRC2 to silence tumor suppressor genes that would normally be expressed.

*MALAT1* is one of the most abundant lncRNAs in mammalian cells, conserved across vertebrates, and overexpressed in lung adenocarcinoma and many other cancers. Its functions in cancer are partly understood — it appears to regulate alternative splicing, transcriptional regulation, and metastatic behavior.

*NEAT1* is a structural lncRNA required for the assembly of paraspeckles (membrane-less nuclear bodies). NEAT1 is upregulated in many cancers and contributes to stress tolerance and survival.

The catalog of cancer-relevant lncRNAs runs into the hundreds. Their functions are increasingly resolved but the field is still developing. Therapeutic targeting of lncRNAs is in early stages — antisense oligonucleotides targeting specific lncRNAs are in preclinical development, and one (in non-cancer applications, eteplirsen for Duchenne muscular dystrophy) has set a precedent for FDA approval of antisense drugs in human disease.

---

## Polycomb and Trithorax: cellular memory

A cell's identity must persist through cell division. A skin cell's daughters must be skin cells, not neurons. The transcriptional pattern that defines a cell type — which genes are on, which are off — has to copy faithfully through mitosis. The question of *how* cellular memory is maintained turns out to be one of the deep questions in developmental biology, and the answer involves two conserved chromatin-modifying systems with opposing functions: the *Polycomb group (PcG)* and the *Trithorax group (TrxG)*.

Both groups were originally identified in *Drosophila* genetics in the 1950s through 1980s. Polycomb mutations cause inappropriate expression of homeotic genes (genes that specify body-part identity); Trithorax mutations cause failure to maintain the active state of those same genes. The two groups maintain *opposite* states — Polycomb maintains silencing, Trithorax maintains activation — at the same target loci. Through decades of subsequent work, the molecular details have been worked out, and the systems turn out to operate in essentially every multicellular animal.

The Polycomb system has two main complexes. *PRC2* (Polycomb Repressive Complex 2) contains the catalytic subunit EZH2 (or its paralog EZH1) along with EED, SUZ12, and others; PRC2 writes the repressive mark H3K27me3. *PRC1* (Polycomb Repressive Complex 1) recognizes H3K27me3 through its CBX subunits, then writes another repressive mark (H2AK119ub via the RING1A/B subunits) and compacts chromatin. Together, PRC1 and PRC2 maintain stable repression of target genes — typically genes involved in differentiation programs that should not be expressed in the current cell type.

The Trithorax system includes the KMT2/MLL family of methyltransferases (MLL1, MLL2, MLL3, MLL4) that write the activating mark H3K4me3, the SET1A/B complexes, and the SWI/SNF chromatin remodeling complex that opens nucleosomal structures. Together, the Trithorax-group proteins maintain stable activation of target genes — typically genes that the cell needs to keep expressing.

In cancer, both systems get hit. EZH2 is hyperactivated in lymphomas (the Y641 mutations mentioned in 7A) and overexpressed in many solid tumors. EZH2 inhibition (tazemetostat) works because EZH2-dependent tumor cells need the silencing for their phenotype. MLL1 is rearranged in infant leukemias (the t(4;11) and related translocations create MLL fusion proteins that drive aberrant gene expression). KMT2D loss-of-function mutations are common in lymphomas and several solid tumors. The SWI/SNF complex is mutated in roughly 20 percent of all cancers, as noted in 7A.

The *bivalent chromatin* concept connects Polycomb and Trithorax with cancer cell biology. In embryonic stem cells, many developmental genes carry both H3K27me3 (Polycomb-deposited repressive mark) *and* H3K4me3 (Trithorax-deposited active mark) simultaneously. These bivalent genes are *poised* — kept low-expression but ready to be activated when the cell commits to a lineage. As the cell differentiates, the bivalent state resolves to either pure repression (H3K27me3 only, with DNA methylation often added) or pure activation (H3K4me3 only).

Cancer cells, particularly the more aggressive ones, often regain bivalent chromatin patterns that resemble stem cells. The differentiation programs that should have been locked in stay accessible. The cell can shift between phenotypes more easily. This is one molecular basis for the *plasticity* that allows cancer cells to dedifferentiate, switch between proliferative and quiescent states, and evade targeted therapies by switching identities.

---

## Reprogramming and cancer stem cells

There is increasingly strong evidence that some cancers arise from cells that have been *epigenetically reprogrammed* — that have reactivated stem-cell-like transcriptional programs without the prior mutations that the classical cancer-evolution model expects. Whether this is the dominant mode or one of several modes is still debated. The mechanistic claim is striking: an environmental insult (chronic inflammation, an oncogenic virus, an exposure that doesn't directly damage DNA) might reset the chromatin landscape of a cell in ways that mimic the effects of mutation, and the resulting cell may go on to acquire mutations downstream.

The most-discussed example is *DNA methylation drift* in aging. As tissues age, the methylation patterns of stem cells drift — some CpG islands gain methylation, some lose it — and the drift correlates with cancer incidence. The Horvath clock and related epigenetic clocks measure this drift and use it to estimate biological age. Cells whose epigenetic age is older than their chronological age are at elevated cancer risk. The biology is correlative, but it suggests that epigenetic drift may be a *cause* of cancer, not merely a *consequence*.

*Cancer stem cells* are a related concept. The hypothesis is that tumors are hierarchically organized — a small population of *cancer stem cells* sustains the tumor, with the bulk of tumor cells being more differentiated descendants that cannot indefinitely propagate the cancer. Cancer stem cells share certain markers and transcriptional features with normal tissue stem cells, including high expression of certain Polycomb-group proteins and bivalent chromatin patterns. The model is supported by some xenotransplantation experiments (where only certain marker-defined cell populations from a tumor can re-establish the cancer in immunodeficient mice) and contested by others (where most or all cells in a tumor have stem-cell potential under sufficiently permissive conditions).

The therapeutic significance of cancer stem cells, if they exist as a separate population, is that conventional chemotherapy may kill the bulk of the tumor while leaving the stem cells alive, leading to recurrence. Drugs targeting cancer stem cells specifically — for example, inhibitors of the Wnt, Notch, or Hedgehog pathways that maintain stem cell identity — are in development for many cancer types. The clinical results so far have been mixed.

---

## Epigenetic therapy: state of the art

Epigenetic drugs are now FDA-approved for several cancers, and the pipeline is growing. The current state:

**DNA methyltransferase inhibitors (DNMT inhibitors).** Azacitidine and decitabine, both approved in the mid-2000s for myelodysplastic syndrome (MDS), have become standard first-line therapy for elderly AML and high-risk MDS patients. They work in part by demethylating silenced tumor suppressor genes and reactivating them, and in part by inducing cellular differentiation. The drugs have been combined with venetoclax (a BCL2 inhibitor — Chapter 10B) in AML with dramatic improvements in response rates. Second-generation DNMT inhibitors (guadecitabine, oral azacitidine) extend the dosing window and improve pharmacokinetics. In solid tumors, the activity has been more modest, but combination strategies (DNMT inhibitor plus immune checkpoint inhibitor) have shown promise — the demethylation appears to reactivate dormant immune-recognition genes, making the tumor more visible to the immune system.

**Histone deacetylase inhibitors (HDAC inhibitors).** Vorinostat (SAHA), romidepsin, belinostat, panobinostat, and tucidinostat are approved for various indications — cutaneous T-cell lymphoma, peripheral T-cell lymphoma, multiple myeloma. The drugs hyperacetylate histones and reactivate silenced genes, but they also have off-target effects on non-histone substrates (many transcription factors and signaling proteins are acetylated). The toxicity profile of pan-HDAC inhibitors has limited their use. Isoform-selective HDAC inhibitors (HDAC6 inhibitors, for instance) are in development with the hope of preserving efficacy while reducing toxicity.

**EZH2 inhibitors.** Tazemetostat, approved in 2020, is the first selective EZH2 inhibitor. It works in EZH2-mutant follicular lymphoma and in epithelioid sarcoma (a rare soft-tissue cancer characterized by loss of SMARCB1, which leads to EZH2 dependency through synthetic lethal logic). Other EZH2 inhibitors (valemetostat, others) are in clinical trials, and the broader concept of *PRC2-dependent cancers* is being mapped.

**IDH inhibitors.** Ivosidenib (IDH1 inhibitor) and enasidenib (IDH2 inhibitor) are approved for IDH-mutant AML and other IDH-mutant cancers. They are arguably the cleanest demonstration that *targeting an oncometabolite* — the 2-hydroxyglutarate produced by mutant IDH — restores epigenetic function and reverses the cancer phenotype. The story is among the most satisfying in modern oncology.

**BET inhibitors.** BET (bromodomain and extra-terminal) proteins (BRD2, BRD3, BRD4) read acetylated histones and recruit transcriptional machinery to chromatin. BET inhibitors (JQ1, OTX015, others) disrupt this reading and downregulate genes driven by acetylated chromatin — including the proto-oncogene MYC in many cancers. BET inhibitors are in clinical trials for hematologic and solid tumors. The activity is modest but biologically interesting; the drugs validate the *reader* layer of the histone code as a therapeutic target.

**Newer targets in development.** PRMT5 (a protein arginine methyltransferase) is a synthetic-lethal target in MTAP-deleted cancers — a common deletion that affects roughly 15 percent of all cancers. PRMT5 inhibitors are in clinical trials. DOT1L inhibitors (pinometostat) target the methyltransferase that supports MLL-fusion leukemias. Menin-MLL inhibitors disrupt the protein-protein interaction that supports MLL-fusion AML. The pipeline is broad and growing.

What unifies the epigenetic therapy field is the principle that *epigenetic states are reversible*. Mutations are not. Drugs that can demethylate genomes, reset histone landscapes, or unblock transcriptional programs offer something genetic therapies cannot — the possibility of restoring a function rather than blocking one. The clinical results so far have been most dramatic in hematologic malignancies, where the chromatin states are more accessible and the tumor biology more permissive. Solid tumors have been harder, partly because the chromatin landscapes are more entrenched and partly because the tumor microenvironment provides survival signals that epigenetic drugs alone cannot overcome.

---

## What this chapter gives you

Beyond DNA methylation and histones, the epigenome includes noncoding RNAs that operate at multiple levels — miRNAs silencing target mRNAs, lncRNAs scaffolding chromatin complexes, circular RNAs and others modulating gene expression. Cancers reshape this RNA layer extensively, generating signatures that serve as diagnostic and prognostic biomarkers and offering targets for therapeutic intervention.

The Polycomb-Trithorax system maintains cellular memory across cell divisions, and its components — EZH2, MLL1, KMT2D, SWI/SNF — are mutated or hyperactivated in many cancers. Cancers often regain stem-cell-like bivalent chromatin patterns, which contributes to phenotypic plasticity and therapy resistance.

Epigenetic therapy has become a real clinical option, with FDA-approved drugs across DNMT inhibition, HDAC inhibition, EZH2 inhibition, IDH inhibition, and (in development) BET, PRMT5, DOT1L, and Menin-MLL inhibition. The field's clinical impact has been concentrated in hematological malignancies; the solid-tumor opportunity is large and partially realized. Combination strategies — epigenetic drugs with chemotherapy, targeted therapy, or immunotherapy — are where the next wave of progress is most likely to come from.

The bigger picture for cancer biology is that the epigenome is not a passive recipient of genetic damage. It is an active layer of regulation that cancers reshape extensively and that medicine can, increasingly, edit. Chapter 8 returns to causation — the chemical, radiation, viral, and bacterial exposures that produce the genetic and epigenetic changes characterized in chapters 4-7.

---

## LLM exercises

1. Ask your LLM to explain the miRNA biogenesis pathway in detail. Then have it identify three oncogenic miRNAs ("oncomiRs") and three tumor-suppressive miRNAs, with their primary targets and the cancers in which they are most strongly implicated. Probe: which miRNAs have most reliably translated from observational findings to clinical applications?

2. Have your LLM compare HOTAIR, MALAT1, NEAT1, and H19 in their mechanisms of action and cancer associations. What makes a lncRNA "actionable" — by clinical biomarker standards, by therapeutic standards? Which of these four is closest to clinical translation?

3. Use your LLM to explain the bivalent chromatin concept. Then ask: how does bivalent chromatin connect cancer stem cells to phenotypic plasticity and therapy resistance? Probe the LLM on the strongest and weakest evidence for the cancer stem cell hypothesis.

4. Ask your LLM to walk through the IDH-2HG-demethylase story from cellular metabolism through to clinical drug approval. What was the order of discoveries, and where in that chain was the therapeutic logic established? Then ask: what other oncometabolites are now being investigated, and what would the next IDH-class success look like?

5. Have your LLM survey current trials combining epigenetic drugs with immune checkpoint inhibitors. What is the mechanistic rationale (think about how demethylation might affect immune recognition), and what are the early results saying? Identify the studies with the strongest signal and the strongest counterarguments.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Carlo Croce** linked microRNAs to cancer in 2002 — discovering that miR-15 and miR-16 are frequently deleted in chronic lymphocytic leukemia. The result reframed noncoding RNAs from biological curiosity to clinical cancer drivers.

![Carlo M. Croce](../images/carlo-m-croce-t3e.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who is Carlo Croce, and how does his work on microRNAs in cancer connect to the noncoding RNA biology we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Carlo M. Croce"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how a single deleted microRNA can disable an entire network of tumor suppressor mRNAs.
- Ask it about the misconduct allegations that complicated Croce's legacy in cancer biology.

What changes? What gets better? What gets worse?
