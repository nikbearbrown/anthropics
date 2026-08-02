# Chapter 7 — Epigenetics in Cancer: The Methylation and Histone Code


## TL;DR

- Cancer is not only a disease of broken genes.
- The chapter moves through What "epigenetics" actually means, DNA methylation, briefly, Worked example: MGMT and temozolomide in glioblastoma, Histones, briefly, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

Cancer is not only a disease of broken genes. It is a disease of misread genes.

That distinction matters. For most of the late twentieth century, cancer was framed as a disease of DNA sequence — mutations in genes, copy-number changes, translocations. The sequence-centric view turned out to be necessary but incomplete. A cell carries roughly 20,000 protein-coding genes in its genome. A neuron, a hepatocyte, and a skin cell all have the *same* 20,000 genes — and yet they are recognizably different cell types, doing different work, expressing different protein repertoires. What distinguishes them is not the DNA sequence. It is the *epigenome* — the set of chemical marks layered on top of DNA and on the histone proteins that package it, controlling which genes are read and which are silenced in any given cell at any given time.

Cancers don't just mutate genes. They rewrite this layer. Tumor suppressor genes that should be expressed get silenced by promoter methylation. Genes that should be quiet get activated by inappropriate histone marks. The chromatin landscape shifts. Entire transcriptional programs reorganize. The cell's identity drifts away from the tissue it came from. In many cancers, the epigenetic changes are as consequential as the genetic ones — and in some cancers, they are the *first* events, preceding any mutation we can detect.

The reframing has been a slow burn over thirty years. In the late 1980s, Andrew Feinberg and Bert Vogelstein noticed that tumor DNA was, on average, less methylated than normal DNA — a finding that did not fit the dominant gene-mutation framework. In 1989, Stephen Baylin's group identified promoter hypermethylation of the *CDKN2A* tumor suppressor in cancer cells, showing that specific genes could be silenced without sequence change. Through the 1990s and 2000s, the histone code, the polycomb and trithorax complexes, the noncoding RNAs, and the chromatin remodelers came into focus. By 2011, Hanahan and Weinberg listed epigenetic reprogramming as an emerging hallmark; by 2022, they made it a full one.

This is the first of two chapters on epigenetics. This one — 7A — covers the molecular mechanisms: DNA methylation and histone modifications. The next — 7B — covers the systems-level epigenetics (noncoding RNAs, polycomb/trithorax, reprogramming) and the therapeutics that exploit it.

Hold the question that organizes both chapters: *if cancer is a disease of misread genes, how does the misreading happen, and can we reverse it?*

---

## What "epigenetics" actually means

The term is sometimes used loosely. Specify it.

*Epigenetics* refers to heritable changes in gene expression that do not involve changes to DNA sequence. The marks are chemical — methyl groups on cytosine bases, acetyl groups on histone lysines, methylation on histone arginines and lysines, ubiquitin tags on histone tails — and they propagate through cell division. A daughter cell inherits not just the parent cell's DNA sequence but the parent cell's pattern of methylation, the parent cell's histone modification landscape, the parent cell's transcriptional state.

The system works because the marks are *enzymatically maintained*. DNA methyltransferases (DNMT1 in particular) recognize the hemimethylated DNA produced after replication — where the parent strand carries methylation but the newly synthesized daughter strand does not — and methylate the daughter strand to match. Histone marks are propagated by the assembly of histones onto new DNA strands and by enzymes that recognize existing marks and propagate them to neighboring nucleosomes. The system has *memory*. A skin cell stays a skin cell across hundreds of divisions because the epigenetic state that defines "skin cell" is faithfully copied each time.

This memory is what makes epigenetics consequential for cancer. Once a tumor suppressor is silenced by methylation, the silencing inherits. The daughter cells inherit the silenced state without needing to acquire new mutations. The lineage moves further from its original tissue identity over time, and the changes accumulate the same way mutations do, except they are reversible in principle if you can remove the marks.

The three pillars of epigenetic regulation are DNA methylation, histone modifications, and noncoding RNAs. The interplay between them is dense — DNA methylation recruits histone-modifying enzymes; histone modifications affect DNA methylation; noncoding RNAs influence both. Cancer perturbs all three in mutually reinforcing ways.

---

## DNA methylation, briefly

DNA methylation in mammals is overwhelmingly at *CpG dinucleotides* — a cytosine followed by a guanine — where the cytosine carries a methyl group on its 5-position carbon (5-methylcytosine, 5mC). The asymmetry of CpG context is important: when the methylated CpG is replicated, the new daughter strand has an unmethylated cytosine paired with a methylated parent-strand cytosine. DNMT1 reads this hemimethylated state and adds a methyl group to the daughter strand, restoring symmetry. The mark is faithfully propagated.

Most CpG dinucleotides in the human genome are methylated. There are roughly 28 million CpG sites in the human genome; about 70 to 80 percent are methylated in a typical cell. Methylation is the *default* state in mammalian genomes, partly because much of the genome is repetitive DNA derived from transposable elements that need to be kept silent.

The exceptions are *CpG islands* — short regions (typically 200 to 1000 base pairs) of unusually high CpG density, located near the transcription start sites of about 70 percent of human protein-coding genes. CpG islands are usually *unmethylated* in normal cells, regardless of whether the associated gene is being expressed. The unmethylated state is permissive for transcription. When a CpG island becomes hypermethylated, the gene downstream is reliably silenced.

In cancer, two things happen to the methylation landscape, and they are pointed in opposite directions.

First, *global hypomethylation*. The bulk genome of cancer cells is less methylated than that of normal cells, particularly at repetitive elements and intergenic regions. The hypomethylation has consequences. Transposable elements that should be silenced can be reactivated. Genomic regions become more fragile, more prone to recombination and breakage. Chromosomal instability increases. The 1983 paper by Feinberg and Vogelstein was the first to show this hypomethylation in human tumors; the finding has been replicated thousands of times since.

Second, *focal hypermethylation of CpG islands*. Specific tumor suppressor genes are silenced by promoter methylation. The list is long. *CDKN2A* (encoding p16) is methylated in many cancers. *MLH1*, the mismatch-repair gene, is methylated in roughly 15 percent of sporadic colorectal cancers — and the methylation phenocopies the germline mutations seen in Lynch syndrome (microsatellite instability, hypermutation, but no inherited cancer). *MGMT*, encoding a DNA repair enzyme, is methylated in some gliomas — and *MGMT* methylation status is a clinical biomarker that predicts response to the alkylating agent temozolomide. *BRCA1* is methylated in some sporadic ovarian and breast cancers, mimicking the germline mutations seen in hereditary cases. *RASSF1A*, *VHL* (in non-VHL-syndrome kidney cancers), *DAPK*, *p15* — the list is extensive.

The combination — global hypomethylation plus focal hypermethylation — is paradoxical only on first encounter. The two patterns reflect different machinery and different selection pressures. The bulk genome loses methylation because the maintenance machinery (DNMT1) is failing or because the targeted methylation of repetitive elements is incomplete. The CpG islands gain methylation because the cell has acquired a selection advantage from silencing specific tumor suppressors. Both directions of change favor the cancer.

What makes promoter methylation interesting therapeutically is that it is *reversible*. A mutated gene is gone — you cannot undo a missense mutation with a drug. A methylated gene is intact at the sequence level; remove the methyl groups, and transcription can resume. The DNA methyltransferase inhibitors — azacitidine (5-azacytidine) and decitabine (5-aza-2'-deoxycytidine) — exploit this. Both drugs are cytosine analogs that incorporate into DNA during replication, get captured by DNMT1 as if they were normal cytosine substrates, and then trap the enzyme in a covalent complex. DNMT1 is degraded. Methylation is not maintained. Over a few divisions, the genome loses methylation, including at the silenced tumor suppressor promoters, and some of those genes reactivate.

Azacitidine was approved by the FDA in 2004 for myelodysplastic syndrome — the first epigenetic drug. Decitabine followed in 2006. Both are now standard care for MDS and elderly AML patients. Their efficacy in solid tumors has been more modest, partly because solid tumors carry more complex epigenetic states and partly because the drugs have significant toxicity. But the principle holds: methylation marks can be erased, and erasure can restore function.

---

## Worked example: MGMT and temozolomide in glioblastoma

Hold the *MGMT* story for a moment because it is the cleanest example of how methylation status changes clinical decisions.

Glioblastoma is the most common and most lethal primary brain cancer. Standard therapy includes surgical resection, radiation, and chemotherapy with temozolomide — an alkylating agent that methylates guanine bases in DNA, producing O6-methylguanine. The lesion mispairs with thymine during replication, causing mutations that, if numerous enough, kill the cell.

*MGMT* — O6-methylguanine DNA methyltransferase — is a DNA repair enzyme whose only job is to remove methyl groups from the O6 position of guanine. It works by transferring the methyl group from guanine to a cysteine residue on itself, then being degraded. Each MGMT molecule can repair one lesion before destruction.

In a glioblastoma with active *MGMT* expression, the cell repairs temozolomide-induced lesions efficiently and survives the drug. In a glioblastoma with *MGMT* promoter hypermethylation, the gene is silenced, MGMT protein is not made, the alkylation damage accumulates, and the cell dies.

This is observable in patients. The Stupp protocol clinical trial showed that glioblastoma patients with methylated *MGMT* promoters survive significantly longer on temozolomide-based therapy than those with unmethylated *MGMT*. The methylation status is now routinely tested in glioblastoma biopsies — bisulfite sequencing or methylation-specific PCR — and the result informs treatment decisions and prognosis.

The general principle: a methylation mark on a single gene's promoter can determine whether a specific drug works. The biology is mechanistic and predictive. Epigenetic biomarkers are now part of standard oncology workups for several cancers.

---

## Histones, briefly

The other major mark on chromatin is on the histone proteins themselves. The structural unit of chromatin is the *nucleosome* — about 147 base pairs of DNA wrapped around a histone octamer composed of two copies each of H2A, H2B, H3, and H4. Linker DNA connects nucleosomes; H1 stabilizes the structure. Higher-order folding compacts chromatin further, and at the highest level produces the visible chromosomes of mitosis.

The histones are not just passive packaging. They are densely modified. The N-terminal tails of H3 and H4 in particular project outward from the nucleosome and carry a thicket of chemical marks — acetylation, methylation, phosphorylation, ubiquitination, sumoylation. The marks are written by *writer* enzymes, removed by *eraser* enzymes, and recognized by *reader* proteins. Different marks correlate with different transcriptional states.

The vocabulary:

*Histone acetylation* — addition of an acetyl group to a lysine residue, written by histone acetyltransferases (HATs, also called KATs), removed by histone deacetylases (HDACs). Acetylation neutralizes the positive charge on the lysine, weakening histone-DNA interactions and opening chromatin. Acetylation is generally *activating* — acetylated regions tend to be transcriptionally active. H3K27ac (acetylation at lysine 27 of histone H3) is a classic active enhancer mark.

*Histone methylation* — addition of methyl groups to lysines or arginines on histone tails, written by histone methyltransferases (HMTs/KMTs), removed by histone demethylases (HDMs/KDMs). Methylation can be mono-, di-, or tri-methylation, and the meaning depends on the specific position and degree. H3K4me3 (trimethylation at lysine 4 of histone H3) marks active promoters. H3K27me3 marks repressed regions and is the canonical Polycomb-repressive mark. H3K9me3 marks heterochromatin — densely packed, transcriptionally silent regions.

*Histone phosphorylation* — addition of phosphate groups to serine or threonine residues. H3S10ph (phosphorylation at serine 10 of H3) marks mitotic chromatin.

*Histone ubiquitination* — H2A K119ub is a Polycomb-associated repressive mark. H2B K120ub is associated with transcription elongation.

The combinatorial code matters. A nucleosome can carry many marks simultaneously, and the same lysine can carry different marks at different times. The reader proteins — chromodomains, bromodomains, PHD fingers, Tudor domains — recognize specific marks and recruit downstream machinery. Bromodomains read acetyl-lysines and recruit transcriptional activators. Chromodomains read methylated lysines and can recruit either activators or repressors depending on the position. The whole system is a layered language of regulation, and cancer cells frequently misregulate it.

---

## Histone modifications in cancer

The chromatin-modifying enzymes are mutated at high frequency in many cancers. Bladder cancer is the extreme case — roughly 80 percent of bladder cancers carry mutations in chromatin-modifying genes. *ARID1A* (a subunit of the SWI/SNF chromatin remodeling complex) is mutated in 25 percent. *KDM6A* (a histone demethylase that removes H3K27me3) is mutated in 24 percent. *KMT2D* (a histone methyltransferase that writes H3K4me1) is mutated in 27 percent. *EP300* (a histone acetyltransferase) is mutated in 15 percent. Other cancers carry similar enrichment: hematological malignancies frequently have mutations in *MLL1/KMT2A*, *EZH2*, *DOT1L*, *CREBBP*, and the SWI/SNF subunits.

The mutations are mostly loss-of-function. The cell loses the ability to write a specific mark, or to read it, or to remove it. The consequences are global: the transcriptome shifts in ways that favor proliferation or de-differentiation.

Three patterns recur.

First, *gain-of-function in repressive complexes*. EZH2 is the catalytic subunit of Polycomb Repressive Complex 2 (PRC2), which writes the H3K27me3 mark. Activating mutations in EZH2 (Y641F, Y641N, A677G) appear in a subset of follicular and diffuse large B-cell lymphomas. The mutant enzyme preferentially generates the trimethylated form, deepening repression of PRC2 target genes — including tumor suppressors. Tazemetostat, an EZH2 inhibitor, was approved by the FDA in 2020 for follicular lymphoma with EZH2 mutations and for epithelioid sarcoma.

Second, *loss-of-function in active marks*. KMT2A (MLL1) writes the H3K4me3 mark at active promoters. KMT2A is frequently rearranged in acute leukemias — particularly infant acute lymphoblastic leukemia, where t(4;11) and other translocations create KMT2A fusions. The fusions place KMT2A in proximity to DOT1L, a different methyltransferase, and inappropriate methylation patterns drive aberrant gene expression. DOT1L inhibitors (pinometostat) are being explored therapeutically.

Third, *chromatin remodeling complex disruption*. The SWI/SNF complex uses ATP hydrolysis to slide nucleosomes along DNA, opening or closing access to transcription factors. Roughly 20 percent of all cancers carry SWI/SNF mutations. *SMARCB1* loss in pediatric rhabdoid tumors. *ARID1A* loss in ovarian clear cell carcinoma, endometrial carcinoma, and others. *SMARCA4* loss in lung cancer and small-cell carcinoma of the ovary, hypercalcemic type. The mutations create transcriptional landscapes that the cell cannot easily reorganize, and the resulting fixed states often favor cancer.

Histone deacetylase inhibitors (HDAC inhibitors) were the second class of epigenetic drug to gain FDA approval. Vorinostat (SAHA) was approved in 2006 for cutaneous T-cell lymphoma. Romidepsin, belinostat, panobinostat followed. The drugs block HDAC enzymes, leading to hyperacetylation of histones and activation of silenced genes. The clinical activity is real but has been concentrated in hematological malignancies — solid tumors have been more resistant, partly because the drugs are pan-HDAC inhibitors and hit many targets at once, producing more toxicity than benefit. Selective HDAC inhibitors targeting specific HDAC isoforms (HDAC6, for instance) are in development.

---

## Metabolic-epigenetic coupling

A subtle and consequential connection: many chromatin-modifying enzymes use small-molecule metabolites as cofactors. The cellular metabolic state shapes the epigenetic state.

*S-adenosylmethionine (SAM)* is the methyl donor for nearly all methyltransferases — both DNA methyltransferases and histone methyltransferases. SAM is generated from methionine in the one-carbon metabolic pathway. When SAM availability is low, methylation reactions slow.

*α-Ketoglutarate (αKG)* is the cosubstrate for the TET family DNA demethylases and the Jumonji-family histone demethylases. When αKG levels drop, demethylation slows.

*Acetyl-CoA* is the source of acetyl groups for histone acetyltransferases.

*NAD+* is required by sirtuin-family deacetylases.

The coupling means metabolic perturbations directly perturb chromatin. The cleanest case is *IDH1/IDH2* mutations. Normally, isocitrate dehydrogenase converts isocitrate to αKG. The cancer-associated R132H mutation in IDH1 (and equivalent mutations in IDH2) creates a neomorphic enzyme that converts αKG to *2-hydroxyglutarate (2HG)*. 2HG is structurally similar to αKG but functions as a competitive *inhibitor* of αKG-dependent enzymes — including the TET demethylases and the histone demethylases. The cell accumulates DNA methylation and histone methylation aberrantly. Tumor suppressor genes silence. Differentiation programs lock up.

IDH1/IDH2 mutations are found in roughly 70 percent of low-grade gliomas and in 10 percent of acute myeloid leukemias. They produce a characteristic *CpG island methylator phenotype (CIMP)* that is detectable on methylation arrays. And — beautifully — they are druggable. Ivosidenib (IDH1 inhibitor) and enasidenib (IDH2 inhibitor) have been FDA-approved for IDH-mutant AML, and they work by reducing 2HG production, restoring αKG levels, and allowing the demethylases to function again. Tumors regress. Differentiation resumes. Patients respond. The IDH inhibitors are one of the cleanest demonstrations that epigenetic dysregulation can be pharmacologically reversed.

---

## What this chapter gives you

DNA methylation and histone modifications are the two main layers of the epigenome. Both are dynamic, both are propagated through cell division, and both are profoundly perturbed in cancer. DNA methylation in cancer follows a paradoxical pattern: bulk hypomethylation across the genome, focal hypermethylation at the CpG islands of tumor suppressor gene promoters. Histone modifications go awry through mutations in the writers, erasers, and readers of the histone code — and a substantial fraction of all human cancers carry such mutations.

The therapeutic significance is large because epigenetic marks are *reversible* in ways that mutations are not. DNMT inhibitors (azacitidine, decitabine) can demethylate the genome and reactivate silenced tumor suppressors. HDAC inhibitors (vorinostat, romidepsin, others) can hyperacetylate histones and reactivate silenced genes. EZH2 inhibitors (tazemetostat) can reduce repressive H3K27me3 marks in cancers with EZH2 mutations. IDH inhibitors (ivosidenib, enasidenib) can restore demethylase activity by suppressing the oncometabolite 2-hydroxyglutarate.

The fields of metabolism and epigenetics intersect: the cofactors that chromatin-modifying enzymes need are metabolic intermediates, and disruptions to metabolism (such as IDH mutations producing 2HG) propagate directly into the chromatin landscape. Chapter 7B continues the story with the noncoding RNAs, the Polycomb-Trithorax balance, and the full landscape of epigenetic therapy.

---

## LLM exercises

1. Ask your LLM to explain the difference between *global hypomethylation* and *focal hypermethylation* in cancer. Why do both happen in the same tumor, and how do they each contribute to cancer phenotype? Then ask: which is the better therapeutic target, and why have DNMT inhibitors been more useful in liquid tumors than solid?

2. Have your LLM walk through the MGMT-temozolomide story in glioblastoma. What is the underlying mechanism? What does methylation status of MGMT predict, and how is it tested clinically? Then ask the LLM to identify other examples where epigenetic biomarkers guide treatment choice.

3. Use your LLM to construct a table of the writer/eraser/reader enzymes for the major histone marks — H3K4me3, H3K9me3, H3K27me3, H3K27ac, H3K36me3. For each mark: writer enzyme, eraser enzyme, reader proteins, and what the mark generally indicates about transcription state. Cross-check with a recent review.

4. Ask your LLM to explain the metabolic-epigenetic coupling through SAM, α-ketoglutarate, acetyl-CoA, and NAD+. Then ask: how do IDH mutations break this coupling, and what does the IDH-inhibitor story say about the broader strategy of targeting oncometabolites?

5. Have your LLM analyze the FDA approvals of epigenetic drugs from 2004 (azacitidine) through the most recent. What patterns appear — which classes have produced the most approvals, which cancers respond, what are the failure modes? Then ask the LLM to forecast which epigenetic targets are most likely to yield the next wave of approved drugs.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Stephen Baylin** and **Andrew Feinberg** in the 1980s established that aberrant DNA methylation patterns — not just mutations — could silence tumor suppressors and drive cancer. Their work made epigenetics a serious cancer field.

**Run this:**

```
Who are Stephen Baylin and Andrew Feinberg, and how does their work on DNA methylation in cancer connect to the epigenetics we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their careers or ideas.
```

→ Search **"Stephen Baylin"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how CpG island hypermethylation silences a tumor suppressor gene without changing its DNA sequence.
- Ask it to compare epigenetic and genetic drivers of cancer — when does each dominate?

What changes? What gets better? What gets worse?
