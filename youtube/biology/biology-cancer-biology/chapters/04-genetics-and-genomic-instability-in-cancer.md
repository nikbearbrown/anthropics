# Chapter 4 — Genetics and Genomic Instability in Cancer


## TL;DR

- Cancer is a misspelling that copies itself.
- The chapter moves through DNA, briefly, Kinds of mutations, Driver vs. passenger mutations, Knudson's two-hit hypothesis, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

Cancer is a misspelling that copies itself.

That is the whole chapter in one sentence, and the rest of it is the elaboration. DNA encodes the instructions for everything a cell does. The instructions are copied every time a cell divides — about 3 billion letters, 10^16 times over a human lifetime. The copying is good but not perfect. Errors get caught, mostly. The errors that escape repair become mutations. Most mutations land in DNA that does nothing or in genes whose function is robust to the change. A few land in genes that matter — and a few of *those* confer a tiny growth advantage on the cell that carries them. That cell divides faster. Its descendants inherit the advantage and accumulate further mutations. Over years, sometimes decades, one lineage drifts away from the contract that holds tissues together.

The whole framework was crystallized by Bert Vogelstein and his colleagues in the late 1980s and 1990s, looking at colorectal cancer. They could see the same cells, biopsied at different stages — a normal colon mucosa, a small adenoma, a larger adenoma, an early carcinoma, a metastatic carcinoma — and read out which mutations had appeared at which stage. *APC* came first, in essentially every adenoma. Then *KRAS*. Then loss of chromosome 18q (carrying *DCC* and other tumor suppressors). Then *TP53*. Each mutation conferred a step-change advantage. The sequence was not perfectly fixed, but the pattern was: cancer is a sequence of mutations selected for in a clonal lineage, each one nudging the cell further from normal behavior.

The picture has gotten more complex since. Cancers carry mutations across many different genes, often in different orders. Some cancers are driven by a small number of dominant mutations; others by many smaller ones. Some carry massive structural rearrangements (chromothripsis, kataegis, chromoplexy — the field has invented colorful names for the violent reshufflings that some tumor genomes display). Some carry epigenetic changes that mimic mutations functionally without altering DNA sequence at all. But the underlying logic is Vogelstein's: cancer is *evolution*, in real time, inside your body, on the timescale of decades.

This chapter does five things. It walks through DNA structure and replication carefully enough that the rest of the book's molecular details will make sense. It separates the kinds of mutations that matter (point mutations, insertions/deletions, structural rearrangements, copy number changes, epigenetic alterations) and the kinds of genes they affect (oncogenes, tumor suppressors, DNA repair genes). It introduces Knudson's two-hit hypothesis — the clearest piece of cancer math ever written down. It describes the DNA repair pathways and what happens when they fail. And it explains why genomic instability is not just a consequence of cancer but is itself one of the enabling features that makes cancer possible at all.

---

## DNA, briefly

A human cell carries about two meters of DNA, compacted into the nucleus. The double helix you have seen pictures of is the universal storage medium for life on Earth. Two strands of nucleotides — sugar, phosphate, base — wound around each other, with the bases pairing in a specific way: A with T, G with C. The pairing is what makes copying possible. Separate the strands and each one carries enough information to reconstruct the other.

The information is in the sequence of bases. A human genome is about 3 billion base pairs. It is divided into 46 chromosomes — 23 pairs, one from each parent — that compact further when the cell prepares to divide. Most of the genome (about 99 percent) does not code for protein. About 20,000 genes encode proteins; many more loci encode RNAs that have regulatory or structural functions. The "junk DNA" framing of the 1980s has eroded as we have learned that much of the non-coding genome regulates how and when genes are expressed.

DNA replication runs during S phase of the cell cycle. The mechanism is conserved across all of life. *Helicase* unwinds the double helix. *DNA polymerase* reads each parent strand and synthesizes a complementary new strand, base by base. One strand (the leading strand) is synthesized continuously; the other (the lagging strand) is synthesized in short fragments called Okazaki fragments, which are then ligated together. Replication proceeds from multiple origins simultaneously — about 30,000 to 50,000 in a human cell — so that the entire 3-billion-base-pair genome is copied in roughly eight hours.

The fidelity is remarkable. DNA polymerase makes errors at a rate of about 1 in 10^5. It proofreads its own work — a 3'-to-5' exonuclease activity that checks each base and removes mismatches — and this brings the error rate down to about 1 in 10^7. Mismatch repair afterward catches most of the remaining errors. The final error rate is about 1 in 10^9 — one error per billion bases copied. Across 3 billion base pairs per division, that is about 3 errors per division.

Three errors per division, over a lifetime of cell divisions in many tissues, is the substrate cancer evolves from. Most errors are silent or neutral. The ones in the wrong places — at the wrong codons in the wrong genes — are not.

---

## Kinds of mutations

The vocabulary matters because the rest of the book uses it.

A **point mutation** is a single-base change. A → G is a transition; A → T is a transversion. *Missense* mutations change one amino acid in the encoded protein. *Nonsense* mutations create a premature stop codon, truncating the protein. *Silent* mutations change the DNA without changing the amino acid (because the genetic code is degenerate). *Splice site* mutations alter the boundaries between exons and introns, often disrupting mRNA processing. The most consequential cancer mutations are missense and nonsense changes at specific positions in specific genes.

An **insertion or deletion** (indel) adds or removes one or more bases. If the indel is not a multiple of three, it shifts the reading frame and typically produces a truncated, nonfunctional protein. Frameshift mutations are particularly common in tumor suppressor genes (because *losing* function is what cancers select for in those genes) and in DNA mismatch repair-deficient tumors (which generate indels at high rates throughout their genomes).

A **copy number variation (CNV)** is a gain or loss of genomic regions much larger than indels — from kilobases to entire chromosome arms. *Amplification* — increasing the copy number of a region from 2 to 5, 10, or 50 — is common for oncogenes (*MYC* amplification in neuroblastoma, *HER2* amplification in breast cancer, *EGFR* amplification in glioblastoma). *Deletion* of regions containing tumor suppressors — *9p21* deletion of *CDKN2A* in many cancers — is a common loss-of-function mechanism.

A **chromosomal translocation** moves a segment of one chromosome to another. The Philadelphia chromosome — the t(9;22) translocation joining *BCR* on chromosome 22 to *ABL1* on chromosome 9 — is the canonical case. The fusion gene produces a constitutively active tyrosine kinase that drives chronic myeloid leukemia. The Philadelphia chromosome was the first reproducible chromosomal abnormality in any human cancer, identified by Peter Nowell and David Hungerford in Philadelphia in 1960. Twenty years later, it became the molecular target of imatinib (Gleevec), the first truly targeted cancer therapy.

Other translocations rearrange regulatory elements rather than coding sequences. In Burkitt lymphoma, the t(8;14) translocation places *MYC* under the control of immunoglobulin heavy-chain enhancers — turning on *MYC* expression in a cell type and at a level it should not be expressed at. In follicular lymphoma, t(14;18) places *BCL2* under similar enhancer control. *Enhancer hijacking* is increasingly recognized as a common mechanism in many cancers, including some that lack the dramatic translocations of leukemias.

**Structural variants** — inversions, complex rearrangements, large-scale shuffling events — are increasingly visible in deep-sequencing studies. *Chromothripsis* (literally "chromosome shattering") is a phenomenon in which a chromosome appears to have been broken into many pieces and reassembled imperfectly. It is found in a substantial fraction of cancers and produces simultaneously many large-scale changes — possibly in a single catastrophic event.

**Epigenetic changes** — DNA methylation, histone modifications — are not mutations in the strict sense (they do not alter DNA sequence), but they alter gene expression and are inherited through cell divisions. Cancers commonly *hypermethylate* tumor suppressor gene promoters (silencing them) and *hypomethylate* the genome broadly (which can lead to genomic instability). Chapter 7 covers epigenetics in detail.

---

## Driver vs. passenger mutations

A typical solid tumor carries tens to hundreds of mutations in protein-coding regions. Most of those mutations do not contribute to the cancer phenotype. They are *passenger* mutations — incidental hitchhikers, accumulated by the cell during its evolution but selecting for nothing. A small number — typically 2 to 8 in any given tumor — are *driver* mutations. Drivers confer a selective advantage; they are the reason the cell's lineage outgrew its neighbors.

Distinguishing drivers from passengers is not always easy. Some clues help. Drivers tend to be mutations recurrent across many independent cancers (the same mutation showing up in patient after patient suggests selection); passengers tend to be unique to a single tumor. Drivers tend to land in functionally important parts of the protein (active sites, binding domains, regulatory regions); passengers are scattered. Drivers tend to produce specific gain-of-function or loss-of-function changes; passengers are usually neutral.

The list of recurrent driver genes is long but finite. *TP53* is mutated in roughly half of all human cancers. *KRAS* is mutated in around 30 percent of cancers (90 percent of pancreatic adenocarcinomas, 50 percent of colorectal, 25 percent of lung adenocarcinomas). *PIK3CA*. *PTEN*. *APC*. *BRAF*. *EGFR*. *MYC*. *RB1*. *NOTCH1*. *CDKN2A*. *VHL*. *BRCA1*. *BRCA2*. The Catalogue of Somatic Mutations in Cancer (COSMIC) and The Cancer Genome Atlas (TCGA) have systematically cataloged the recurrent driver mutations across cancer types and provided much of the genomic context for modern oncology.

Two functional categories matter. *Oncogenes* are normal cellular genes whose hyperactivation drives proliferation. Their cancer-causing mutations are *dominant gain-of-function* — a single mutated copy is enough to confer the phenotype. *KRAS* G12D is the canonical example; one mutated *KRAS* allele in a cell is sufficient to lock RAS in its active form. Chapter 5 covers oncogenes in detail.

*Tumor suppressor genes* are normal cellular genes whose proper function restrains proliferation or triggers death. Their cancer-causing mutations are *recessive loss-of-function* — both copies must be inactivated for the phenotype to manifest. *TP53*, *RB1*, *APC*, *PTEN*, *BRCA1/2* — these are all tumor suppressors. Chapter 6 covers them in detail.

A third functional category is *DNA repair genes*. These are technically tumor suppressors — losing them allows other mutations to accumulate faster — but the mechanism of action is one step removed from cancer itself. Mismatch repair genes (*MLH1*, *MSH2*, *MSH6*, *PMS2*) are mutated or silenced in Lynch syndrome and in sporadic cancers with microsatellite instability. Homologous recombination genes (*BRCA1*, *BRCA2*, *PALB2*) are mutated in hereditary breast and ovarian cancer. Loss of these genes does not directly drive proliferation; it drives mutation accumulation, which in turn enables other drivers to appear.

---

## Knudson's two-hit hypothesis

Alfred Knudson published a paper in 1971 that is probably the most beautifully argued piece of statistical reasoning in cancer biology. He was looking at retinoblastoma — a rare childhood eye cancer. About 60 percent of cases are sporadic; about 40 percent are familial. Familial cases tend to involve both eyes (bilateral) and appear earlier. Sporadic cases are usually unilateral and appear slightly later. Why?

Knudson reasoned mathematically. If retinoblastoma required two independent events in the same cell — two "hits" — then in *sporadic* cases, both hits would have to occur de novo in a single retinal cell. The probability of one rare event squared. If, however, an individual *inherited* one hit from a parent (already in every retinal cell), only a single second hit would be needed. The probability of one rare event, in any of the millions of retinal cells. The expected age of onset would be earlier (one event happens faster than two), and the probability of bilateral involvement would be high (independent second hits in either eye are likely over a few years).

The model fit the data quantitatively. Familial cases — bilateral, early — followed the kinetics of a single event. Sporadic cases — unilateral, slightly later — followed the kinetics of two events. Knudson's hypothesis, before any molecular evidence existed, predicted that retinoblastoma was caused by inactivation of *both copies* of a single gene — and that hereditary cases inherited one inactivated copy and acquired the second somatically.

Sixteen years later, the *RB1* gene was molecularly cloned. The predictions held: every retinoblastoma tumor carried two inactivated *RB1* alleles. In hereditary cases, one was in the germline (every cell carried it); the other was a somatic loss in the affected cells. In sporadic cases, both were somatic.

The two-hit hypothesis became the framework for understanding tumor suppressors in general. *TP53* fits. *APC* fits. *BRCA1* and *BRCA2* fit. *VHL* fits. *PTEN* fits with some nuance (haploinsufficiency — even one inactivated allele is enough in some contexts). The model is one of the few pieces of cancer biology that you can derive from first principles, on a chalkboard, with population statistics.

What Knudson's hypothesis also reveals is the family-screening logic. A person who carries a germline pathogenic variant in *BRCA1*, *BRCA2*, *RB1*, *APC*, *TP53*, *VHL*, or a Lynch syndrome gene already has the first hit. They need only one somatic event to start the process. They are at dramatically elevated cancer risk. Screening them early and aggressively is medically justified by Knudson's math.

---

## Chromosomes and the Boveri hypothesis

Long before Knudson, Theodor Boveri proposed in 1914 that cancer was caused by chromosomal abnormalities. Boveri was a German biologist studying sea urchin embryos, where he could watch chromosomes segregate unevenly during cell division — and saw that uneven segregation produced abnormal cells. He extrapolated. If a similar process happened in human tissues, the resulting cells might behave abnormally — and might grow into tumors.

Boveri's hypothesis was largely ignored for half a century. The early molecular cancer biology of the 1970s and 80s focused on specific genes, not on chromosome-level changes. But Boveri turns out to have been right at a larger scale than even he knew. Roughly 90 percent of solid tumors carry chromosomal abnormalities — extra chromosomes (aneuploidy), missing chromosomes, translocations, deletions, amplifications. The chromosomes of a cancer cell often look nothing like the orderly 46 of a normal cell. Some tumors have 60 chromosomes. Some have 80. Some have mixtures of cells with different chromosome numbers within the same tumor.

The mechanisms that produce chromosomal instability are several. Defects in the spindle assembly checkpoint allow chromosomes to be misdistributed during mitosis. Defects in centrosome regulation produce abnormal mitotic spindles that misalign chromosomes. Telomere dysfunction can fuse chromosome ends, producing dicentric chromosomes that break during division. Defects in DNA repair, particularly homologous recombination, lead to broken chromosomes that get rejoined incorrectly.

Aneuploidy is functionally consequential. A cell with three copies of chromosome 7 has 50 percent more of every gene on that chromosome (including any oncogene present). A cell with one copy of chromosome 17 has half as much of the tumor suppressors there (including *TP53*). The aggregate effect of widespread aneuploidy is to perturb gene expression at thousands of loci simultaneously. It is a brute-force way to drift away from normal regulation.

---

## DNA repair pathways

Cells repair DNA constantly. The damage rate is staggering — tens of thousands of lesions per cell per day, from a combination of endogenous metabolism (reactive oxygen species, spontaneous depurination, replication errors) and exogenous insult (UV, ionizing radiation, mutagenic chemicals). Without repair, the genome would degrade within days. The repair pathways are specialized; different kinds of damage are handled by different machinery.

**Base excision repair (BER)** handles small chemical modifications to single bases — oxidized bases (8-oxoguanine), deaminated bases, abasic sites. A specific glycosylase recognizes the damaged base and removes it, creating an abasic site. The site is cleaved, the gap filled by DNA polymerase, and the strand sealed by ligase. BER runs constantly in every cell.

**Nucleotide excision repair (NER)** handles bulkier lesions that distort the DNA helix — UV-induced thymine dimers, chemical adducts. A complex of proteins (XPA, XPB, XPC, XPD, XPF, XPG, ERCC1, and others) recognizes the distortion, excises a 25-30 nucleotide segment containing the lesion, and resynthesizes the strand. Inherited defects in NER cause *xeroderma pigmentosum* — a disease in which patients have severe UV sensitivity and develop multiple skin cancers in childhood and adolescence. Xeroderma pigmentosum is the canonical demonstration of how essential NER is.

**Mismatch repair (MMR)** handles errors that escape DNA polymerase proofreading — base mismatches and small indels at simple repeat sequences (microsatellites). The MMR machinery (MLH1, MSH2, MSH6, PMS2 in humans) identifies which strand is the newly synthesized one, excises the mismatch-containing region, and resynthesizes. Inherited defects in MMR cause *Lynch syndrome* (hereditary nonpolyposis colorectal cancer), which dramatically elevates the risk of colorectal, endometrial, and several other cancers. Lynch syndrome tumors typically exhibit *microsatellite instability* — variability in the length of simple repeat sequences — that is a diagnostic biomarker.

**Double-strand break (DSB) repair** is the most consequential. A double-strand break severs both DNA strands. If left unrepaired, the chromosome ends will be lost in the next division. Two main pathways handle DSBs.

*Homologous recombination (HR)* uses the sister chromatid (the other copy of the same chromosome, available during S and G2 phases) as a template to repair the break accurately. The machinery includes RAD51, BRCA1, BRCA2, PALB2, RAD52, and others. HR is high-fidelity; it restores the original sequence.

*Non-homologous end joining (NHEJ)* simply pastes the broken ends back together, sometimes with a few bases lost or added at the junction. NHEJ is faster than HR but lower fidelity; it works in any phase of the cell cycle but introduces small errors at the break site.

Inherited defects in HR — most importantly in *BRCA1* and *BRCA2* — cause hereditary breast and ovarian cancer. The mechanism is that, with HR compromised, double-strand breaks are repaired by error-prone NHEJ, accumulating mutations and genomic rearrangements over time. The consequence is also, beautifully, exploited therapeutically: *BRCA*-mutated tumors are exquisitely sensitive to *PARP inhibitors*, drugs that block an enzyme involved in single-strand break repair. PARP inhibition in normal cells produces single-strand breaks that HR-competent cells repair without problem; in *BRCA*-mutated cells, the unrepaired breaks are converted to double-strand breaks during replication, and HR cannot repair them. The cells die. The principle — *synthetic lethality* — has become a central concept in cancer therapy and is covered in detail in Chapter 19.

In 2015, the Nobel Prize in Chemistry was awarded to Tomas Lindahl, Paul Modrich, and Aziz Sancar for their work on the major DNA repair pathways. Lindahl for base excision repair, Modrich for mismatch repair, Sancar for nucleotide excision repair. The repair systems they characterized are the reason your cells can run for decades without falling apart, and the reason cancers — when they have lost a repair pathway — are uniquely vulnerable to drugs that exploit the loss.

---

## Genomic instability as an enabling feature

Hanahan and Weinberg listed genomic instability as an *enabling characteristic* in their 2011 update — not a hallmark in itself but a condition that allows the hallmarks to be acquired. The reasoning is direct. A normal cell mutates at a rate of about 3 errors per division. For the typical cell to acquire 5 to 10 driver mutations over a lifetime is statistically possible but slow. A cell that has lost a DNA repair pathway, or has lost the mitotic spindle checkpoint, or has shortened telomeres that fuse chromosome ends, mutates at 10 to 100 times the normal rate. The probability that any given cell in such a lineage acquires the needed combination of drivers, in a meaningful time, goes up dramatically.

This is the *mutator phenotype* hypothesis, articulated by Lawrence Loeb in 1991. Cancer cells, Loeb argued, must have elevated mutation rates to acquire enough drivers in a human lifetime. Modern genomics has largely confirmed this. Cancers with mismatch repair deficiency carry thousands of point mutations across the genome. Cancers with homologous recombination deficiency carry distinctive patterns of structural rearrangements. Cancers with damaged DNA polymerase ε ("POLE-ultramutated") carry tens of thousands of point mutations.

What is sometimes counterintuitive is that *high mutation burden* in a cancer can be therapeutically useful. Tumors with many mutations produce many *neoantigens* — abnormal proteins that the immune system can recognize as foreign. These tumors tend to respond well to immune checkpoint inhibitors (Chapter 18). Microsatellite-instability-high colorectal cancer, for example, has a much better response to pembrolizumab than microsatellite-stable colorectal cancer, even though it is in some sense a "worse" tumor genetically. The biology gives, and it takes; the same genomic instability that drove the tumor also makes it visible to the immune system.

---

## Telomeres and replicative limits

Each chromosome ends in a stretch of repetitive DNA — the telomere. The sequence (in humans, TTAGGG repeated thousands of times) does not encode protein. Its function is structural. Telomeres protect chromosome ends from being mistaken for double-strand breaks and inappropriately fused or chewed back. They also accommodate the *end-replication problem* — the geometric fact that DNA polymerase cannot quite replicate the very end of a linear chromosome, so a small piece is lost each division.

In most somatic cells, telomeres shorten with each division. After roughly 50 divisions, the telomeres become critically short, the chromosome ends become exposed, and the cell either enters senescence (a permanent non-dividing state) or undergoes apoptosis. This is the Hayflick limit, named for Leonard Hayflick, who described it in 1961. It is a built-in counter on how many divisions a cell can sustain.

Cancers almost universally circumvent the Hayflick limit, usually by reactivating telomerase — the enzyme that rebuilds telomeres. Normal stem cells express low levels of telomerase; differentiated somatic cells generally do not. In around 85 to 90 percent of cancers, telomerase has been turned back on. The remaining 10 to 15 percent maintain telomeres through an alternative mechanism (the ALT pathway, which uses recombination). Either way, the divisional counter is reset, and the cell becomes effectively immortal in division capacity.

The telomere story is also a story about the *crisis* that occurs just before telomerase reactivation in cancer evolution. As telomeres shorten in a pre-cancerous lineage, chromosome ends start fusing inappropriately. Fused chromosomes break during mitosis. Breaks get rejoined incorrectly. New fusions form. The result is a period of intense genomic instability — sometimes called *telomere crisis* — during which the cell is acquiring large numbers of structural rearrangements. Many cells die during crisis. The ones that emerge with telomerase reactivated and stable chromosomes are the ones that go on to become cancer. The dramatic karyotypes seen in many advanced cancers are partly the fossils of telomere crisis.

---

## What this chapter gives you

Cancer is a sequence of mutations selected for in a clonal lineage. The mutations come from imperfect replication, damaged repair, and exposure to mutagens. The sequence is loose but recognizable — driver genes recur across patients with the same cancer type, in patterns that tell you what biology is being selected for. Knudson's two-hit hypothesis tells you why some cancers run in families and why heritable cancer-susceptibility carriers benefit from early aggressive screening. The DNA repair pathways are the molecular wall against mutation accumulation, and when they fall, mutations accumulate faster and the cancer that emerges is often paradoxically more visible to the immune system. Genomic instability is not a side-effect of cancer; it is part of what enables cancer to exist on a human timescale.

Hold the picture. The rest of the molecular chapters of this book — oncogenes, tumor suppressors, cell cycle, apoptosis, epigenetics, metastasis — are about specific genes and pathways being modified by these mutational processes. Chapter 5 starts with the oncogenes themselves.

---

## LLM exercises

1. Ask your LLM to walk through Knudson's 1971 retinoblastoma analysis quantitatively. What probability values does the two-hit model predict for sporadic vs. familial cases? Can the LLM reproduce the math? Then push it: what aspects of the original model have been refined by molecular evidence since 1971?

2. Have your LLM list the top 20 most frequently mutated cancer genes (by COSMIC or similar) and classify each as oncogene, tumor suppressor, or DNA repair gene. Then ask it to explain why a single mutated copy is sufficient for oncogenes but not for tumor suppressors. Probe the cases where this classification breaks down (PTEN haploinsufficiency, for example).

3. Use your LLM to find a published whole-exome sequencing study of one cancer type and identify the recurrent drivers reported. Ask it to compare driver patterns across two related cancers (e.g., lung adenocarcinoma vs. small-cell lung cancer, or colorectal cancer with vs. without microsatellite instability). What biological logic do the differences reveal?

4. Generate, with your LLM, an explanation of synthetic lethality between BRCA mutations and PARP inhibition that would be clear to a medical student. Then ask the LLM to identify three other synthetic lethal interactions being explored in current cancer therapy and assess how much evidence supports each.

5. Have your LLM explain why microsatellite-instability-high tumors are paradoxically more responsive to immunotherapy than microsatellite-stable tumors. Then ask it to apply the same logic to other "high mutation burden" cancers (POLE-mutant, smoking-related lung cancers, melanoma). Are the predictions borne out in clinical data?

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Alfred Knudson** proposed the "two-hit hypothesis" in 1971 — explaining inherited retinoblastoma by requiring two mutational events to disable both copies of a tumor suppressor gene. The framework opened up cancer genetics as a field with predictive structure.

![Alfred G. Knudson](../images/alfred-g-knudson-81a.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who was Alfred Knudson, and how does his two-hit hypothesis connect to the cancer genetics and genomic instability we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Alfred G. Knudson"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through Knudson's epidemiological argument — how did the age distribution of retinoblastoma cases force the two-hit conclusion?
- Ask it to compare hereditary and sporadic retinoblastoma using Knudson's framework.

What changes? What gets better? What gets worse?
