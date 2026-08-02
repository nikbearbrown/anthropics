# Chapter 7 — Biotechnology and Genomics: We Learned to Read the Letters, and Then We Learned to Write Them

## TL;DR

- Four verbs, borrowed from bacteria, that changed medicine.
- The chapter moves through The four verbs, Copy: PCR and the thermophile from Yellowstone, Cut: restriction enzymes, then CRISPR, Restriction enzymes, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Four verbs, borrowed from bacteria, that changed medicine.*

---

On December 8, 2023, the FDA approved the first CRISPR-based medicine in the United States. It is called Casgevy. It treats sickle cell disease.

Victoria Gray was thirty-four years old when she received it — the first patient in the pivotal clinical trial, in Nashville, in July 2019. She had spent her life cycling through pain crises, acute chest syndrome, the slow organ damage that comes from oxygen-starved tissue. Sickle cell disease had defined her childhood, her adulthood, her capacity to be present for her children.

The therapy did not correct her sickle cell mutation. It did something more interesting. Every person who has sickle cell disease also carries, silently, the genes for *fetal* hemoglobin — the oxygen-carrying protein that works in the womb. After birth, a transcription factor called BCL11A switches fetal hemoglobin off. BCL11A does this work through an enhancer — a short stretch of regulatory DNA a few thousand base pairs from the BCL11A gene itself, active specifically in red-cell precursors. The Casgevy therapy takes a patient's own bone marrow stem cells, delivers a CRISPR editing complex into them by electroporation, cuts the BCL11A erythroid enhancer, and puts the cells back. BCL11A no longer turns on in red-cell precursors. Fetal hemoglobin de-represses. The patient starts making fetal hemoglobin in adult life, in their own red cells. Sickle hemoglobin is still there, but diluted by enough fetal hemoglobin to prevent the polymerization that causes the crises.

In the five years since her infusion, Victoria Gray has not had a single pain crisis.

Here is the question this chapter is built around. *How did we get from "DNA is a double helix" (Watson and Crick, 1953) to "we cut a patient's bone marrow stem cells at a chosen genomic position and put them back" (Casgevy, 2023) in seventy years?*

The answer is a stack of four tools. Each tool was discovered as some other organism's biology — a bacterium defending against viruses, a hot-spring microbe maintaining its enzymes at 70°C, a yogurt bacterium with a strange kind of immune memory. None of the people who found the underlying biology were trying to cure sickle cell disease. The cure emerged from the stack.

---

## The four verbs

Before mechanism, let me name the four primitives. Every technique in this chapter is a composition of these.

**Copy.** Take a tiny amount of DNA and make a billion copies of it. Polymerase chain reaction.

**Cut.** Cleave DNA at a specific sequence. Restriction enzymes for short palindromic sequences. CRISPR-Cas9 for arbitrary 20-nucleotide targets.

**Read.** Determine the sequence of bases. Sanger sequencing for short, accurate, single-locus work. Illumina for whole genomes at scale. PacBio and Nanopore for very long reads.

**Write.** Install a specific sequence at a specific position. CRISPR with homology-directed repair for precise replacement. Base editors for single-nucleotide changes without a double-strand break. Prime editors for small programmable edits.

That is the entire vocabulary of the molecular biology laboratory, distilled to its load-bearing operations. PCR amplifies the input. Restriction enzymes or CRISPR cut the substrate. Sequencing reads the result. Editing makes the change. Everything else — cloning, RNA-seq, GWAS, liquid biopsy — is a composition of these four. The rest of the chapter is mechanism for each verb, in the order they were invented.

---

## Copy: PCR and the thermophile from Yellowstone

In 1983, Kary Mullis was driving up Highway 128 toward Mendocino when he had the idea for the polymerase chain reaction. The problem was concrete. Suppose you have a single human genomic DNA molecule and you want to study a specific 500-base-pair region inside it. The 500 bp you care about is one part in six billion of the total DNA mass in the cell. You cannot do chemistry on something that dilute. You need to enrich — to copy that 500 bp specifically, ignoring the other three billion bases.

The idea is elegant. DNA polymerase extends a primer in the 5'→3' direction by reading the template strand. Design two short DNA primers, one matching each end of the region you want to amplify, on opposite strands. The primers hybridize at the boundaries of the target. DNA polymerase fills in the rest. After one round of replication, two copies. After two rounds, four. After *n* rounds, 2ⁿ copies. After thirty rounds, one billion copies — and almost no extra copies of anything else, because the primers only bind at the boundaries.

The math is clear. The chemistry was the hard part.

To run thirty cycles of denaturation at 94°C, you need a DNA polymerase that survives 94°C. Most enzymes denature — their folded structure unravels — well before that temperature. The DNA polymerase Mullis used in his original experiments, the Klenow fragment of *E. coli* polymerase I, dies at 60°C. You would have to open the tube and add fresh enzyme after every cycle. Thirty cycles, thirty additions, thirty chances for contamination. PCR was a clever idea that worked terribly.

The solution was sitting in a hot spring in Yellowstone National Park. In 1969, Thomas Brock isolated a thermophilic bacterium, *Thermus aquaticus*, from a spring that ran at 70°C. Its DNA polymerase — **Taq polymerase** — was stable at these temperatures because it had to be. When Mullis and colleagues at Cetus cloned the Taq gene, purified the enzyme, and substituted it into the PCR reaction, the problem vanished. Load the reaction once. Set the thermocycler to ramp through three temperatures thirty times. Walk away. Two hours later, a billion copies.

**The three temperature stages of one PCR cycle:**

**Denaturation at ~94°C.** Every double-stranded DNA molecule in the tube comes apart. Hydrogen bonds between complementary bases break. Single strands.

**Annealing at ~55°C.** The reaction cools to the temperature where the designed primers — typically 18–25 nucleotides, complementary to specific regions of the template — find their targets by Brownian motion and stick. The long genomic template strands are too floppy to easily re-anneal with each other at these concentrations, but the small, abundant primers find their targets.

**Extension at 72°C.** Taq polymerase's optimal temperature. Each primer is extended 5'→3', copying the template through the target region.

One cycle, starting from *N₀* template molecules: *N₀* × 2¹ molecules. After *n* cycles: *N₀* × 2ⁿ. Starting from a single molecule and running thirty cycles: approximately 10⁹ copies. The target region is now a billion times more concentrated than it was. Now you can do chemistry. Now you can sequence. Now you can clone.

Mullis received the 1993 Nobel Prize in Chemistry. Brock, who isolated the organism that made the technique possible, did not — the foundational basic-science work that enables applied breakthroughs is routinely invisible to prizes. The lesson worth pinning down: *the PCR idea is upstream; the Taq polymerase is the load-bearing innovation.* Most engineering breakthroughs look like this. The idea is decades old. The enabling material arrives later. Then suddenly the field changes.

![Three-stage thermal cycle diagram ](images/07-biotechnology-genomics-fig-01.png)
*Figure 7.1 — Three-stage thermal cycle diagram *

Variants of PCR are worth naming quickly because you will see them constantly.

**Quantitative PCR (qPCR)** adds a fluorescent readout — a dye or a probe that reports how much DNA is present each cycle. The cycle at which fluorescence first crosses a threshold is the **Ct value**. More starting template → lower Ct. The relationship is logarithmic: a Ct difference of 1 is a 2-fold difference in starting copy number. This is how a COVID nasal-swab test works: reverse transcriptase converts viral RNA to cDNA, PCR amplifies a viral gene, fluorescence detects it, the Ct value tells you whether virus was present and roughly how much.

**Reverse transcription PCR (RT-PCR)** adds a first step: reverse transcriptase — an enzyme borrowed from retroviruses like HIV, which evolved it to copy RNA into DNA in infected cells — converts RNA to cDNA. Then PCR proceeds on the cDNA. This lets you detect and quantify any RNA: viral RNA in a diagnostic test, gene expression in a research experiment.

**Digital PCR (dPCR)** partitions the reaction into thousands of tiny chambers. Each chamber gets approximately zero or one template molecule. After PCR, each chamber is positive or negative. The fraction positive, via Poisson statistics, gives an absolute count of starting molecules. Used for liquid biopsy where you might be detecting one tumor DNA molecule per hundred thousand normal ones.

Taq polymerase has no proofreading exonuclease. Its error rate is about 1 in 10⁵ bases. For applications where the sequence must be correct — sequencing a construct, amplifying for cloning — high-fidelity polymerases with 3'→5' proofreading (Pfu, Phusion) are used instead, bringing the error rate to ~10⁻⁷.

| variant name | what is added to basic PCR | readout | key application — |
| --- | --- | --- | --- |
| Basic PCR (nothing, gel band of amplified product, cloning | genotyping | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| qPCR (fluorescent dye or probe, real-time fluorescence curve + Ct value, gene expression | viral load | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| RT-PCR (reverse transcriptase step before PCR, cDNA then PCR product, RNA detection | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| RT-qPCR (RT + fluorescent readout, Ct value on cDNA, COVID diagnosis | quantitative expression | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| dPCR (partitioning into thousands of chambers, fraction positive chambers, absolute copy number | liquid biopsy at low abundance) | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |

---

## Cut: restriction enzymes, then CRISPR

To do almost anything with a DNA molecule, you need to cut it at a specific position.

### Restriction enzymes

Bacteria are continuously attacked by bacteriophages. One defense is a class of enzymes that recognize foreign DNA by a short sequence the bacterium's own DNA has been chemically marked to *not* match, and cleave it. These are the **restriction enzymes**. The 1978 Nobel Prize for their discovery and biochemistry went to Werner Arber, Hamilton Smith, and Daniel Nathans.

The useful ones have palindromic recognition sequences — the same sequence on both strands reading 5'→3'. *EcoRI* recognizes 5'-GAATTC-3'. *BamHI* recognizes GGATCC. *HindIII* recognizes AAGCTT. Each enzyme cuts at a defined position within its recognition sequence. EcoRI cuts between G and A on each strand, leaving four-nucleotide 5' overhangs — "sticky ends" that are complementary to each other. Mix two DNA fragments cut with the same enzyme; the sticky ends base-pair. Add DNA ligase; the fragments are joined into a stable recombinant molecule. This is molecular glue obeying the same Watson-Crick base-pairing rules as everything else in the cell.

![EcoRI cleavage diagram ](images/07-biotechnology-genomics-fig-02.png)
*Figure 7.2 — EcoRI cleavage diagram *

**Robert Swanson and Herbert Boyer** used this at the newly-founded Genentech in 1978 to produce the first recombinant human protein. They synthesized the human insulin A-chain and B-chain genes, cloned each into a bacterial expression plasmid, transformed *E. coli*, induced expression, purified the protein, and chemically reconstituted the mature insulin. By 1982, Eli Lilly's Humulin — recombinant human insulin from *E. coli* — was on the market, the first recombinant protein drug ever approved.

Before Humulin, diabetics injected insulin extracted from pig and cow pancreases — slightly different from human insulin, prone to allergic reactions, limited by the world's slaughterhouse industry. After Humulin, insulin was a virtually unlimited resource identical in sequence to human insulin. The supply problem disappeared in one product launch. The same general workflow produced human growth hormone (1985), erythropoietin (1989), G-CSF (1991), and the first wave of monoclonal antibodies — rituximab, trastuzumab, adalimumab — that form the core of modern oncology and immunology pharmacology. The biotechnology industry exists because of this workflow.

![Recombinant DNA cloning workflow ](images/07-biotechnology-genomics-fig-03.png)
*Figure 7.3 — Recombinant DNA cloning workflow *

Restriction enzymes have a fundamental limit: they cut at *fixed* sequences. EcoRI cuts every GAATTC in the genome. The set of usable enzymes is constrained by which palindromic sequences exist in the vicinity of your target. They are not programmable.

### CRISPR-Cas9

In the early 2000s, Francisco Mojica at the University of Alicante noticed that many bacterial genomes contained unusual clusters of short repeats interspersed with "spacer" sequences that matched, when BLASTed, the genomes of bacteriophages known to infect those bacteria. He hypothesized these were a record of past infections — a kind of adaptive immunity.

In 2007, Rodolphe Barrangou and Philippe Horvath at the yogurt company Danisco confirmed this directly, showing that *Streptococcus thermophilus* cells that survived phage attack acquired new spacers in their CRISPR loci matching the attacking phages. The system was adaptive immunity: the bacterium remembers viral attackers by capturing snippets of their genomes.

What made this a tool was the biochemistry. The CRISPR locus is transcribed into short RNAs, each containing one spacer. These guide a nuclease — most famously **Cas9** from *Streptococcus pyogenes* — to any DNA sequence matching the spacer, where it cuts both strands.

In 2012, Jennifer Doudna's lab at Berkeley and Emmanuelle Charpentier's lab showed that Cas9 and its associated RNAs could be simplified into a single **chimeric guide RNA (sgRNA)**. The Cas9-sgRNA complex would cut any DNA sequence matching the 20-nucleotide spacer in the sgRNA, as long as the target was followed by the short sequence 5'-NGG-3' (the **PAM**). Design the 20-nucleotide spacer portion of the sgRNA. Load it onto Cas9. Cut any genome, at a chosen position. Doudna and Charpentier shared the 2020 Nobel Prize in Chemistry.

The mechanism, step by step.

**Design the sgRNA.** Pick a 20-nucleotide target sequence in the gene, immediately followed by an NGG PAM. NGG sites occur every ~8 bp in the genome, so targets are abundant. Order the sgRNA from a commercial supplier — a few hundred dollars, delivered in days.

**Load Cas9.** Mix purified Cas9 protein with synthetic sgRNA. They form a stable **ribonucleoprotein (RNP)** complex. The RNP is the cutting machine.

**Deliver to the cell.** Electroporation for cell lines (most common for ex vivo editing of harvested cells, including the Casgevy bone-marrow workflow). Lipid nanoparticles for liver cells in vivo. Adeno-associated virus (AAV) for other tissues. The choice of delivery is one of the major bottlenecks for in vivo therapies.

**Search and cut.** In the nucleus, the Cas9-sgRNA complex scans the genome, pausing at each NGG site to test whether the adjacent 20 bp match the spacer. Most do not match. When a full match is found, the sgRNA invades the duplex, the helix unwinds, and Cas9's two nuclease domains — HNH and RuvC — each cleave one strand. A double-strand break appears at a precisely specified position, three base pairs upstream of the PAM.

**Cellular repair determines the outcome.** The cell cannot tolerate a double-strand break. Two competing pathways act.

**Non-homologous end joining (NHEJ)** is the dominant pathway in most cell types. It binds the broken ends, trims them slightly, and ligates them back together — usually introducing a small insertion or deletion (indel) at the junction. If the cut is inside a protein-coding exon, a frameshift indel disrupts the reading frame, produces a premature stop codon, and eliminates the protein. This is how you **knock out** a gene: cut in an early exon, let NHEJ repair, frameshifted gene, no protein. This is what Casgevy does to the BCL11A erythroid enhancer — NHEJ-mediated disruption of the enhancer's transcription-factor binding sites.

**Homology-directed repair (HDR)** uses a homologous template to repair the break accurately. If you provide an exogenous template with the sequence you want, HDR copies from your template and installs the change. This is how you make a **precise edit**: cut, provide a template, get the exact sequence you want. HDR is much less efficient than NHEJ — typically 1–10% of cuts in dividing cells, near-zero in non-dividing cells.

NHEJ for disruption. HDR for precision. The choice is the strategic decision of every CRISPR experiment.

![CRISPR mechanism diagram ](images/07-biotechnology-genomics-fig-04.png)
*Figure 7.4 — CRISPR mechanism diagram *

### CRISPR variants — editing without a double-strand break

Classical Cas9 with NHEJ is a blunt instrument. The indels are heterogeneous. Double-strand breaks occasionally trigger large genomic rearrangements. HDR is too inefficient for many therapeutic applications.

**Base editors** fuse a deaminase enzyme to a Cas9 variant that nicks only one strand. **Cytosine base editors** (CBEs) convert C to U (read as T) in the non-target strand: net effect C→T (or G→A on the opposite strand). **Adenine base editors** (ABEs) convert A to inosine (read as G): net effect A→G (or T→C). No double-strand break. No heterogeneous indels. Narrower editing scope — only two types of base transitions — but far safer for therapeutic use in non-dividing cells.

**Prime editors** fuse a reverse transcriptase to a Cas9 nickase, paired with an extended guide RNA (pegRNA) carrying the desired new sequence at its 3' end. The nickase cuts one strand; the reverse transcriptase copies the pegRNA's 3' extension into the nicked strand; the cell resolves the resulting heteroduplex to the new sequence. Any single-nucleotide change, plus small insertions and deletions up to ~80 bp. More complex mechanism, lower efficiency than base editing, but broader editing scope.

**CRISPRi/CRISPRa** use a catalytically dead Cas9 (no nuclease activity) fused to a transcriptional repressor or activator. Point at a promoter with a guide RNA, repress or activate the gene without touching the sequence. Reversible. Used heavily for functional screening and for dissecting regulatory elements.

| tool | mechanism | edit type | requires DSB? | typical efficiency |
| --- | --- | --- | --- | --- |
| Cas9 + NHEJ (frameshift indel, disruption of gene | enhancer, yes, high, knockout | A concrete checkpoint for applying the chapter concept. | A specific, evidence-linked version that readers can verify. | A concrete checkpoint for applying the chapter concept. |
| Cas9 + HDR (precise replacement using template, yes, low, correction | insertion | A concrete checkpoint for applying the chapter concept. | A specific, evidence-linked version that readers can verify. | A concrete checkpoint for applying the chapter concept. |
| Cytosine base editor (C→T or G→A, no DSB, moderate-high, point mutation correction | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A specific, evidence-linked version that readers can verify. | A concrete checkpoint for applying the chapter concept. |
| Adenine base editor (A→G or T→C, no DSB, moderate-high, point mutation correction | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A specific, evidence-linked version that readers can verify. | A concrete checkpoint for applying the chapter concept. |
| Prime editor (any SNP + small indels, no DSB, moderate, versatile correction | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A specific, evidence-linked version that readers can verify. | A concrete checkpoint for applying the chapter concept. |
| CRISPRi | a (transcription OFF | A concrete checkpoint for applying the chapter concept. | A specific, evidence-linked version that readers can verify. | A concrete checkpoint for applying the chapter concept. |

---

## Read: from Sanger to Illumina to the finished genome

A DNA molecule has a sequence. How do you read it?

### Sanger sequencing

The answer came from **Fred Sanger** in 1977 — the man who had already won the 1958 Nobel for protein sequencing, and would win a second Nobel in 1980 for this. The method is, once you see it, almost embarrassingly elegant.

DNA polymerase adds nucleotides to the 3' end of a growing strand. The 3'-OH of the last nucleotide is what the polymerase grabs for the next addition. Remove the 3'-OH — make a **dideoxynucleotide (ddNTP)** that has an H instead of an OH at the 3' position — and the polymerase can still incorporate it, but cannot add anything after. The chain terminates.

Mix a single-stranded template, a primer, DNA polymerase, all four normal dNTPs at high concentration, and a small amount of fluorescently labeled ddNTPs — one color per base (ddATP green, ddCTP blue, ddGTP yellow, ddTTP red). The polymerase extends the primer. At each position, it pulls from the nucleotide pool: usually the normal dNTP, occasionally the labeled ddNTP. The ddNTP terminates the chain at that position. Over many copies of the template, you generate a population of fragments, each terminated at a different position, each labeled with the color of the terminating base.

Separate by size on capillary electrophoresis. Smaller fragments migrate faster. A detector reads the fluorescence color of each fragment as it passes. Output: a **chromatogram** — colored peaks in order of fragment size. Each peak is one base position. The color is the identity. Read left to right: the sequence.

Sanger reads ~700–800 bp per reaction. Accuracy ~99.99% per base. The gold standard for short, accurate, single-locus work — confirming a plasmid construct, verifying a CRISPR edit, sequencing a candidate disease gene. Slow and expensive per base: each reaction takes an hour and costs a few dollars per kilobase. To sequence the human genome at Sanger rates took thirteen years and three billion dollars.

![Sanger sequencing output ](images/07-biotechnology-genomics-fig-05.png)
*Figure 7.5 — Sanger sequencing output *

### The Human Genome Project

The **Human Genome Project** was launched in October 1990 as a publicly-funded international consortium. Goal: complete, high-quality sequence of the entire human genome. Estimated cost: three billion dollars. Estimated timeline: fifteen years.

In 1998, Craig Venter's company Celera launched a competing private effort using whole-genome shotgun sequencing — fragment everything at random, sequence both ends, assemble computationally. A race ensued. On April 14, 2003 — fifty years to the day after Watson and Crick's *Nature* paper — the consortium declared completion of a "finished" sequence. Cost: roughly three billion dollars. Duration: thirteen years. Coverage: approximately 92% of the genome. The remaining 8% — centromeres, ribosomal DNA repeats, segmental duplications — were too repetitive to assemble from short Sanger reads.

The project produced the reference sequence. It identified ~20,000 protein-coding genes — far fewer than the ~100,000 some had predicted, a surprise that redirected the field toward regulatory complexity. It enabled the next generation of genome-wide work. Then the cost started to fall.

### Illumina: massively parallel sequencing

Sanger sequences one fragment per reaction. To cover a human genome at 30-fold depth means ~100 billion bases of raw reads — roughly 130 million Sanger reactions. Even running thousands of machines in parallel, there was a throughput ceiling.

Illumina's approach, commercialized starting in 2007, reads *millions* of fragments at once. Fragment the genome. Ligate adapter sequences to both ends. Apply to a glass **flow cell** whose surface carries short oligos complementary to the adapters. Each fragment lands at a random position and is amplified in place by "bridge amplification" into a tight cluster of identical copies. Millions of clusters per square millimeter.

Sequence all clusters simultaneously. Flood the flow cell with reversible-terminator nucleotides — each has a fluorescent label specific to its base, and a chemical blocking group at the 3' position that prevents further extension. Polymerase adds one nucleotide to each cluster's growing strand. Wash. Image the entire flow cell: each cluster's fluorescence reports the base just added. Remove the blocking group and fluorescent label. Repeat. Each cycle reads one base from every cluster at once. Typical runs produce a few billion reads of 150–300 bp each.

The cost per base dropped roughly 10,000-fold compared to Sanger. A whole human genome at 30× coverage costs about $200 in reagents on current high-output Illumina instruments. One genome that took thirteen years and three billion dollars in 2003 now takes two days and two hundred dollars.

Illumina reads have one weakness: they are short. The human genome has many repetitive regions — centromeres, segmental duplications, tandem repeat arrays — that are longer than 300 bp. Short reads from a repetitive region cannot be uniquely placed in the assembly. These regions remained unresolved.

![Illumina sequencing-by-synthesis diagram ](images/07-biotechnology-genomics-fig-06.png)
*Figure 7.6 — Illumina sequencing-by-synthesis diagram *

### Long reads close the gap

**Pacific Biosciences (PacBio)** uses a single DNA polymerase molecule in a tiny chamber, with fluorescently labeled nucleotides, to read single molecules in real time. Reads are typically 10–25 kb, with the recent "HiFi" mode achieving ~99.9% accuracy.

**Oxford Nanopore** threads DNA through a protein nanopore; the ionic current through the pore changes as different bases pass through, and a neural network interprets the current trace. Reads can exceed 1 Mb. Less accurate per base than PacBio HiFi, but the extraordinary length opens regions inaccessible to short reads. The MinION device is USB-stick sized, used for outbreak sequencing in the field.

In April 2022, Karen Miga and Adam Phillippy's T2T (Telomere-to-Telomere) consortium published the **first complete, gap-free human genome assembly** — T2T-CHM13 — using PacBio HiFi and Nanopore reads. The 8% of the genome that had remained unassembled since 2003 was finally resolved: centromeric satellite repeats, ribosomal DNA arrays, segmental duplications. About 200 million base pairs of newly readable sequence. More than 1,900 newly annotated genes.

### The cost-per-genome curve

Here is the headline statistic of this chapter. In 2001, sequencing one human genome cost approximately $95 million. In 2007, $1 million. In 2014, $1,000. In 2024, $200.

A reduction from ~$10⁸ to ~$200 in twenty-three years. Six to seven orders of magnitude. Plot it on a log scale against time, and two regimes emerge. From 2001 to roughly 2008, the cost fell along Moore's Law — halving every ~18 months, the rate of integrated-circuit transistor cost. From 2008 onwards, the cost fell *faster* than Moore's Law. Illumina's massively parallel chemistry was scaling on a steeper curve than semiconductor manufacturing.

![Cost-per-genome curve on log scale ](images/07-biotechnology-genomics-fig-07.png)
*Figure 7.7 — Cost-per-genome curve on log scale *

What has *not* fallen at the same rate is the cost of *interpretation*. We can read a genome for $200. We cannot yet, for most variants, tell a patient what their genome means for their health. Curated variant databases (ClinVar), trained genetic counselors, professional-society guidelines, and clinical-validation studies are expensive and slow to scale. The gap between sequence in hand and biology understood is where most of the friction in clinical genomics now lives.

---

## Write: CRISPR in practice and in the clinic

The four-verb stack is now complete. In practice, the four verbs combine into workflows. Let me make that concrete by tracing the Casgevy therapy through each one.

**Copy.** After harvesting bone marrow stem cells from the patient, the cell population is expanded in culture — essentially a cellular PCR, replacing one cell with millions. The CRISPR reagents themselves were discovered and validated by PCR-based screening.

**Cut.** Cas9 loaded with a guide RNA targeting the BCL11A erythroid enhancer is delivered into the stem cells by electroporation. The guide RNA was designed using the same CRISPR-design software any lab would use. The cut at the enhancer is NHEJ-repaired to a disruptive indel.

**Read.** After editing, the cells are Sanger-sequenced and Illumina-sequenced at the target site to verify that the BCL11A enhancer has been disrupted in the great majority of alleles, and at off-target sites to verify that no unintended cuts occurred. Only cells meeting quality standards are infused.

**Write.** The edit that was made — the disruption of the BCL11A enhancer — is a deliberate write to the patient's genome, intended to persist in all descendants of the edited stem cells for the patient's lifetime.

The regulatory approval in December 2023 is not the end of the story. It is the proof of concept that the verb *write*, applied to a patient's own bone marrow cells ex vivo, can be turned into a clinical product. What remains hard is in vivo editing of differentiated tissues — brain, muscle, retina — where cells cannot easily be harvested, edited, and replaced. The in vivo CRISPR-as-therapy field is in its first decade.

### The genome-scale layer

On top of the four verbs, a dense layer of genome-scale technologies now exists. **RNA-seq** applies Illumina sequencing to cDNA made from cellular RNA, producing a quantitative count of every transcript — the genome-wide expression state of any cell or tissue. **Single-cell RNA-seq** (10x Genomics and related platforms) profiles each cell separately, revealing heterogeneity invisible to bulk averaging; the Human Cell Atlas consortium is using it to catalog every cell type in the human body. **GWAS** (genome-wide association studies) genotypes hundreds of thousands of people at millions of SNP positions and tests each SNP for statistical association with disease — revealing the genetic architecture of complex traits. **Liquid biopsy** detects circulating tumor DNA (ctDNA) in plasma, enabling cancer detection and monitoring from a blood draw rather than a tissue biopsy.

The applications are clinical and already deployed. **Pharmacogenomics** — variants in drug-metabolizing enzymes like CYP2C19 and CYP2D6 — has large, actionable effects on how patients process medications; many health systems now run preemptive pharmacogenomic panels. **Tumor-agnostic drug approvals** — pembrolizumab for microsatellite-instability-high tumors (FDA, 2017); larotrectinib for NTRK-fusion tumors (2018) — use genomic signatures rather than tissue of origin as the indication. **Newborn screening** now uses sequencing alongside mass spectrometry to detect dozens of treatable genetic diseases in the first 48 hours of life. **Polygenic risk scores** aggregate thousands of small-effect GWAS hits into population-level predictors of disease risk, with real but bounded clinical utility concentrated at the tails of the distribution.

| technology | what it measures | scale | primary clinical or research application — |
| --- | --- | --- | --- |
| RNA-seq (gene expression per transcript, whole transcriptome, tumor profiling | drug response | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| scRNA-seq (expression per single cell, thousands of cells per experiment, cell atlas | tumor heterogeneity | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| GWAS (SNP frequency in cases vs. controls, genome-wide ~1M SNPs, disease-risk loci | polygenic risk scores | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| Liquid biopsy | ctDNA (tumor mutations in plasma, personalized mutation panel, MRD monitoring | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| Pharmacogenomics (drug-metabolizing enzyme variants, targeted gene panel, dose selection | drug avoidance | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| Tumor-agnostic approvals (genomic signature e.g. MSI-H or NTRK fusion, tumor sequencing, indication-agnostic drug matching) | student should see the full stack from measurement to clinical decision in one view | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |

---

## What the chapter built

The chapter started with Victoria Gray and ended with a survey of what genomic medicine looks like in 2024. The four verbs are the through-line.

PCR amplifies the input. Taq polymerase — borrowed from *Thermus aquaticus* in a Yellowstone hot spring — is the load-bearing innovation that turned a clever idea into an automatable laboratory tool. Restriction enzymes — borrowed from bacterial defense systems against bacteriophages — built recombinant DNA technology, producing recombinant insulin in 1982 and the modern biopharma industry. CRISPR-Cas9 — borrowed from bacterial adaptive immunity in *Streptococcus pyogenes* — replaced restriction enzymes as the general-purpose cut-and-edit tool, and became the basis for the first FDA-approved gene-editing therapy in December 2023. Sanger sequencing read the first genomes. Illumina broke Moore's Law and drove the cost of reading a human genome from three billion dollars to two hundred in twenty years. Long-read sequencing (PacBio, Nanopore) closed the last 8% that Sanger and Illumina could not assemble.

None of the organisms whose biology was borrowed were trying to solve a human problem. *Thermus aquaticus* was surviving a hot spring. *E. coli* was defending itself against phages. *Streptococcus pyogenes* was mounting an immune response to viral DNA. The biology was there. The biologists found it. The engineers borrowed it. The clinicians deployed it.

Reading DNA is now ordinary. Writing it, at the level of an entire person's body, is still hard. That asymmetry — between what we can measure and what we can change — is the chapter, in one sentence.

---

## LLM Exercise — Build your genomics tools simulator

### The simulation prompt

```
Show: Read CLAUDE.md and DESIGN.md from this project. Conform to them.

Say: Build 07-genome-tools.html — a genomics tools simulator
with three linked panels.

Panel 1 — PCR Animator. Show a fragment of double-stranded DNA
(20 bp visible). User inputs:
- Number of cycles (slider, 5–35, default 30)
- Starting template count (dropdown: 1, 10, 100)

Animate one complete cycle (denature → anneal → extend) with:
- Denaturation: strands visibly separate
- Annealing: two primers binding at the flanking positions
- Extension: new strand growing 5'→3' from each primer,
  shown base by base

Display: copy count after n cycles (exact: N₀ × 2ⁿ);
a bar chart showing copy count at cycles 5, 10, 15, 20, 25, 30;
a Ct simulator: given a fluorescence-detection threshold of
10⁹ copies, compute and display the Ct value.

Verify: at n=30, N₀=1: copies = 2³⁰ ≈ 1.07 × 10⁹ (PASS/FAIL
printed to console). At n=20: copies = 2²⁰ ≈ 1.05 × 10⁶
(PASS/FAIL).

Panel 2 — CRISPR Guide Designer. User inputs:
- A 60-bp DNA sequence (text field, editable)
- Edit mode: Knockout (NHEJ) or Precise edit (HDR)

The panel:
- Scans the input sequence for all NGG PAM sites on both strands
- Lists the 20-nt protospacer for each candidate guide
- Highlights each candidate on the sequence diagram
- For the selected guide: shows predicted cut site (3 bp
  upstream of PAM), predicted on-target activity (mock
  score based on GC content of the spacer), and the top
  3 mock off-target sites (random sequences with 2–3
  mismatches, shown as warnings)
- For HDR mode: shows a template input field for the
  desired sequence and animates the repair outcome

Display: a table of all candidate guides with columns:
guide sequence, PAM, cut position, GC%, mock on-target
score, NHEJ/HDR outcome label.

Verify: for a sequence with a known NGG at position 25,
the guide starting at position 5 (3 bp upstream of the
NGG) should be found and listed (PASS/FAIL to console).

Panel 3 — Cost-per-genome curve. A log-scale line chart
showing the NHGRI cost-per-genome data:
- x-axis: 2001–2024
- y-axis: cost in dollars, log scale (10² to 10⁸)
- Plot: the actual NHGRI cost curve as a solid blue line
- Overlay: a Moore's Law reference line (halving every
  18 months from $95M in 2001) as a dashed gray line
- Annotated events: HGP complete (2003), first $1,000
  genome (Illumina HiSeq X, 2014), T2T-CHM13 (2022),
  Casgevy approval (2023)
- Interactive: hover over any year to see the cost at
  that year and the ratio to Moore's Law

Display: "In 2024, a human genome costs ~$200 — six
orders of magnitude less than 2001."

Constrain: Three panels side by side, SVG canvas 600x400
each. Single self-contained HTML file, D3 v7 from CDN,
no other dependencies. Color palette: DNA strands dark
blue #1a5276 and medium blue #2980b9, primers orange
#e67e22, new synthesis green #27ae60, damaged/off-target
red #c0392b. Add at top of script:

// CLAIM: PCR amplifies a target exponentially: N₀ × 2ⁿ
// copies after n cycles from N₀ starting molecules.
// CRISPR-Cas9 cuts 3 bp upstream of the NGG PAM.
// Sequencing cost has fallen ~6-7 orders of magnitude
// since 2001, faster than Moore's Law from 2008 onward.
```

### Exploration tasks

Once the simulation runs:

1. **The exponential math.** Set starting templates to 1 and step the PCR cycle count from 5 to 35 in steps of 5. Record the copy count at each step. At which cycle does the count first exceed 10⁶? At which does it first exceed 10⁹? Where does the Ct value fall? Now set starting templates to 100 and repeat. Note that the Ct shifts by log₂(100) ≈ 6.6 cycles — which means starting with 100 copies versus 1 copy is detectable as a Ct difference of about 6.

2. **Guide design.** In Panel 2, type in a 60-bp sequence from a gene you care about (use the real sequence of *BCL11A* exon 2, easily found by searching "BCL11A exon 2 sequence" — a short exercise in using the NCBI tools you will use constantly in research). How many NGG-PAM candidate guides does the panel find? Which has the highest GC content in its spacer? What off-target warnings appear? This is the design step that takes a biologist from "I want to edit this gene" to "here is the specific 20-nucleotide sequence I will order."

3. **The cost curve.** In Panel 3, hover over 2007, 2008, 2009, and 2010. Note that the divergence from Moore's Law begins around 2007–2008, coinciding with Illumina's acquisition of Solexa. Calculate how far behind Moore's Law the actual cost was by 2014 (when the first sub-$1,000 genome was announced). At the current pace, what would a genome cost in 2030?

### Extension prompt

```
Extension: Add a fourth panel to 07-genome-tools.html —
Liquid Biopsy Simulator. The panel models circulating
tumor DNA (ctDNA) detection.

Parameters (sliders):
- Tumor burden: 0.01 cm³ to 100 cm³ (log slider)
- ctDNA fraction: fraction of cell-free DNA from tumor
  (0.001% to 10%, derived from tumor burden)
- Sequencing depth: 100x to 10,000x (slider)
- Number of tumor mutations in the panel: 1 to 50

The panel displays:
- Expected ctDNA copies per mL of plasma (use the
  empirical relationship: 1 cm³ tumor ≈ 5,000 copies
  ctDNA/mL plasma at average shedding rates, then
  scale with the ctDNA fraction)
- Probability of detecting at least one mutant molecule
  given the depth and panel size (use Poisson statistics:
  P(detect) = 1 - e^(-λ) where λ = copies × panel_size
  × depth / genome_copies_per_mL)
- Minimum detectable tumor burden at 95% detection
  probability for the current panel and depth settings
- A comparison bar chart showing: current test sensitivity,
  imaging sensitivity (fixed at tumor size 1 cm³ ~= 0.5 cm
  diameter, labeled), and CA-125 sensitivity (fixed at
  0.3 cm³ for ovarian, labeled)

Verify: at tumor burden 1 cm³, panel of 16 mutations,
depth 1000x, ctDNA fraction 0.05%, the detection
probability should exceed 99% (PASS/FAIL to console).
At tumor burden 0.001 cm³, same settings, probability
should be < 5% (PASS/FAIL).
```

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Kary Mullis** invented PCR in 1983 and received the 1993 Nobel Prize in Chemistry. Thomas Brock isolated *Thermus aquaticus* in 1969. Jennifer Doudna and Emmanuelle Charpentier published the CRISPR-Cas9 guide RNA system in 2012 and received the 2020 Nobel.

**Run this:**

```
Who was Francisco Mojica, and what did he observe in bacterial
genomes that eventually led to CRISPR-Cas9 gene editing? Keep it
to three paragraphs. End with the single most surprising thing
about his career or the circumstances of how his discovery was
recognized by the scientific community.
```

→ Search **"Francisco Mojica CRISPR"** on Wikipedia. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to trace the chain from Mojica's 2005 paper to Barrangou's 2007 experiment to Doudna and Charpentier's 2012 paper, explaining what each experiment added that the previous one could not have shown.
- Ask it to explain why the 2020 Nobel Prize was controversial within the CRISPR community — specifically the question of who first demonstrated CRISPR-Cas9 editing in human cells, and the ongoing patent dispute between the Broad Institute and Berkeley.

What changes? What gets better? What gets worse?
