# Chapter 10 — Biochemistry of the Genome

*A molecule that codes for itself only because something else reads it.*

## The question before the answer

In 1944, three researchers at the Rockefeller Institute — Oswald Avery, Colin MacLeod, and Maclyn McCarty — published a paper that should have changed biology immediately. They had taken a strain of *Streptococcus pneumoniae* that was harmless and a related strain that caused fatal pneumonia in mice. They had purified material from the dead virulent bacteria and added it to the live harmless ones. The harmless bacteria became virulent. They could now kill mice.

The question was: what was the transforming substance? Avery and colleagues identified it. Not protein. Not lipid. Not polysaccharide. *DNA*. They had identified the molecule of heredity. [^1]

The scientific community was unimpressed. Most biologists assumed genes were made of protein — proteins had structural complexity, twenty amino acids, evidently rich enough to encode the variety of life. DNA had only four bases. It seemed too simple to be the carrier of inheritance.

It took until 1952 for the Hershey-Chase experiment — using bacteriophages with labeled DNA and labeled protein — to convince the field that genes were DNA. And it took until 1953 for Watson and Crick (building on Rosalind Franklin's X-ray diffraction data) to publish the double helix structure that explained how a molecule with only four chemical letters could encode the information for an entire organism.

This chapter is about the molecule of inheritance — what it is structurally, what it does mechanistically, and how the cell stores, organizes, and accesses it.

## Learning objectives

By the end of this chapter, you will be able to:

1. Describe the structure of a deoxyribonucleotide and explain why DNA's double helix is antiparallel.
2. Identify the base pairing rules and explain why they emerge from chemistry rather than being arbitrary.
3. Distinguish DNA from RNA and describe the three major types of RNA in protein synthesis.
4. Explain the difference between genotype and phenotype with examples.
5. Describe how bacterial chromosomes and plasmids are organized and replicated, and contrast with eukaryotic chromosome packaging.

Prerequisites: Chapters 1–9.

## The discovery, briefly

The history is worth pausing on, because it shows how slow scientific consensus can be when the evidence runs counter to expectation.

**1869**: Friedrich Miescher, a Swiss physician, isolated a new substance from the nuclei of pus cells. He called it *nuclein* — what we now call DNA. He did not know what it did. [^2]

**1928**: Frederick Griffith showed that some kind of "transforming principle" could transmit virulence between strains of *S. pneumoniae*. He did not identify the substance.

**1944**: Avery, MacLeod, McCarty identified the transforming principle as DNA. The paper was published in the *Journal of Experimental Medicine*. The reception was tepid.

**1952**: Alfred Hershey and Martha Chase used radioactively labeled bacteriophages to show that only the DNA, not the protein, entered the bacterial cell during infection. Phage progeny inherited only what came from the DNA. This was the decisive experiment.

**1953**: James Watson and Francis Crick, using diffraction data from Rosalind Franklin and Maurice Wilkins, proposed the double-helical structure of DNA. The structure immediately suggested a mechanism for replication: the two strands could separate, and each could template a new complementary strand. [^3]

**1957**: Matthew Meselson and Franklin Stahl demonstrated that replication was *semiconservative* — each new double helix contains one parent strand and one new strand. The Meselson-Stahl experiment is sometimes called the most beautiful experiment in biology.

The whole arc, from Miescher's nuclein to Meselson-Stahl, takes 88 years. The single most consequential molecule in biology was identified, characterized, and mechanistically understood across roughly a century of incremental work. None of it was inevitable. Each step required someone willing to look at a strange result and pursue it.

## What a nucleotide is

DNA is a polymer of nucleotides. A **nucleotide** has three parts:

1. A **five-carbon sugar**. In DNA, the sugar is *deoxyribose* — ribose with one fewer hydroxyl group. In RNA, the sugar is *ribose*.
2. One or more **phosphate groups**. Nucleotides incorporated into nucleic acid polymers retain one phosphate.
3. A **nitrogenous base**. The base is attached to carbon 1 of the sugar. There are five common bases: adenine (A), guanine (G), cytosine (C), thymine (T) — these four are in DNA — and uracil (U), which replaces thymine in RNA.

The bases come in two classes by shape. **Purines** (adenine and guanine) have a fused two-ring structure. **Pyrimidines** (cytosine, thymine, uracil) have a single ring.

Nucleotides link into a polymer via **phosphodiester bonds** between the 3' carbon of one sugar and the 5' carbon of the next, with a phosphate bridging them. The sugar-phosphate backbone is the same chemistry no matter which base is attached. The information is in the sequence of bases, not in the backbone.

## Base pairing

The key insight from the Watson-Crick model: the bases pair with each other in specific complementary patterns. Adenine pairs with thymine. Guanine pairs with cytosine. The pairing is held together by hydrogen bonds — two between A and T, three between G and C.

This is not arbitrary. The pairing emerges from the chemistry of the bases themselves. A purine paired with a pyrimidine gives the right geometry for the helix; two purines would be too wide, two pyrimidines too narrow. The hydrogen-bond donors and acceptors on adenine are positioned to match those on thymine. The hydrogen-bond donors and acceptors on guanine are positioned to match those on cytosine. A swap (A with G, say) would not form stable hydrogen bonds. The chemistry constrains the pairing.

In a DNA double helix, the two strands run **antiparallel** — one strand runs 5' to 3' while the other runs 3' to 5'. The antiparallel arrangement is necessary because the chemistry of the sugar-phosphate backbone only allows base pairing when the strands face each other in opposite orientations.

The information content of DNA is in the sequence of bases. A strand of length *n* has 4^n possible sequences. A 10-base strand has about a million possible sequences. A 20-base strand has about a trillion. A bacterial chromosome of 4 million base pairs encodes essentially unlimited information, given how exponential the combinatorics are.

## RNA, briefly

Ribonucleic acid (RNA) differs from DNA in three respects:

1. The sugar is **ribose**, with a hydroxyl group at the 2' position that DNA lacks. The extra hydroxyl makes RNA more chemically reactive and less stable than DNA. RNA is degraded by hydrolysis and by ubiquitous enzymes called ribonucleases.
2. The base **uracil** replaces thymine. Uracil pairs with adenine the same way thymine does. Why DNA uses thymine instead of uracil is interesting: cytosine spontaneously deaminates to uracil at low rates, and if uracil were a normal DNA base, the cell could not distinguish a deamination event from a normal U. By having thymine (which is structurally a methylated uracil), the cell can flag any uracil in DNA as a mutation to repair.
3. RNA is usually **single-stranded** rather than double-stranded. Single strands fold back on themselves to produce complex three-dimensional shapes — stems, loops, hairpins, pseudoknots. Some RNA molecules fold into structures that have catalytic activity, like proteins.

The three main types of RNA in protein synthesis:

- **Messenger RNA (mRNA)** carries the genetic information from a gene to the ribosomes, where it directs protein synthesis. The base sequence of mRNA, read in triplets called codons, specifies the sequence of amino acids in the resulting protein.
- **Transfer RNA (tRNA)** carries individual amino acids to the ribosome and matches them to the appropriate codon. Each tRNA molecule has an *anticodon* (three bases that base-pair with the mRNA codon) and a specific amino acid attached at its other end.
- **Ribosomal RNA (rRNA)** is part of the structure of the ribosome itself. About half of the ribosome's mass is rRNA. The catalytic activity of the ribosome — the formation of peptide bonds — is actually performed by rRNA, not by ribosomal proteins. The ribosome is a ribozyme. This was a major discovery; rRNA had been thought to be a structural scaffold. It is in fact the enzyme.

The discovery that RNA can be catalytic — by Sidney Altman and Thomas Cech in the early 1980s — suggested that RNA might have been the original molecule of life, both storing information and catalyzing reactions before DNA and proteins evolved. This is the **RNA world** hypothesis. There is no living example of an RNA-only organism; the hypothesis is supported by the catalytic competence of RNA, the centrality of rRNA in modern protein synthesis, and the fact that some viruses (with RNA genomes) demonstrate that RNA-based replication is possible. [^4]

↳ **Dig Deeper — Ribozymes and the catalytic competence of RNA**

*If RNA can catalyze, what does the modern repertoire of natural ribozymes look like, and what have we engineered in the lab?*

**Prompt:**
> Survey known ribozymes in modern biology. Start with the catalytic center of the ribosome (the peptidyl transferase center, which is RNA, not protein). Then describe at least four classes of natural ribozymes (group I introns, group II introns, RNase P, hammerhead and hairpin ribozymes, glmS riboswitch). End by describing in vitro evolution of ribozymes (Bartel and Szostak's work, the RNA polymerase ribozymes that can copy substantial RNA templates) and what these tell us about the plausibility of the RNA world.

**What to do with the output:** The "ribozymes exist in modern biology" result is part of why the RNA world hypothesis has held up. Save the answer; it bears on Chapter 6's discussion of viroids as living fossils of an RNA-world era.

## Some viruses use RNA as hereditary material

The central dogma in its classical form runs DNA → RNA → protein. Most cells use DNA as the hereditary molecule and use RNA as an intermediate.

But many viruses use RNA as their genome. Positive-sense RNA viruses (poliovirus, coronaviruses) use their genome directly as mRNA. Negative-sense RNA viruses (influenza, rabies) carry an RNA polymerase that transcribes their genome into messages. Retroviruses (HIV) use reverse transcriptase to copy their RNA genome into DNA, which integrates into the host's genome — running the central dogma backward.

Each of these strategies is a different solution to the problem of storing genetic information in RNA. We met them in Chapter 6. The point here is that RNA can serve as hereditary material in some lineages, and the central dogma is more flexible than the classical statement suggests.

## Genotype and phenotype

Two terms that get used loosely and matter precisely.

**Genotype**: the genetic constitution of an organism. The DNA sequence. The complete set of alleles for every gene.

**Phenotype**: the observable characteristics of an organism. The proteins it expresses, the structures it forms, the behaviors it exhibits.

The relationship is not one-to-one. The same genotype can produce different phenotypes in different environments. The same phenotype can arise from different genotypes (convergent traits). A bacterium with a particular antibiotic-resistance gene (genotype) may or may not be antibiotic-resistant in practice (phenotype) — the gene might not be expressed, or its product might be inactive in the conditions tested.

For clinical microbiology, the genotype-phenotype distinction matters because some diagnostic tests measure genotype (PCR detects DNA sequence) and others measure phenotype (susceptibility testing measures whether a drug actually inhibits growth). The two can disagree. A patient might be infected with bacteria carrying an MRSA gene that is not expressed under the test conditions, producing a sensitive phenotype despite the resistant genotype. Or a bacterium might be functionally resistant by a mechanism (efflux pump, slow growth) not detected by the genotype panel.

## Chromosome structure

A **chromosome** is the physical packaging of a cell's DNA. The packaging differs between prokaryotes and eukaryotes.

### Prokaryotic chromosomes

Most bacteria have a single, circular chromosome — a closed loop of double-stranded DNA. *E. coli* has a 4.6 million base-pair chromosome. The chromosome is far too long to fit inside the cell linearly: stretched out, it would be about 1 mm, while the cell is about 2 μm. The DNA has to be compacted by a factor of about 1000.

Bacterial DNA is compacted by **supercoiling** — twisting the helix on itself to make tighter coils. Topoisomerase enzymes introduce supercoils; gyrase introduces negative supercoils that pack the DNA tightly while keeping it accessible for replication and transcription. The supercoiled chromosome is organized into a relatively dense region of the cell called the **nucleoid**, but it is not bounded by a membrane.

Some antibiotics (the fluoroquinolones — ciprofloxacin and relatives) target bacterial gyrase. Inhibiting gyrase prevents proper DNA replication, killing the bacteria. The enzyme is different enough from human topoisomerases that the inhibition is selective. We will see this in Chapter 14.

### Eukaryotic chromosomes

Eukaryotes have multiple linear chromosomes inside a membrane-bounded nucleus. Each chromosome is a single linear DNA molecule. Human cells have 46 chromosomes. *Saccharomyces cerevisiae* has 16. Some plants have hundreds.

The packaging is more elaborate. Eukaryotic DNA wraps around protein cores called **histones** in a structure that resembles beads on a string. Each "bead" is a **nucleosome** — about 147 base pairs of DNA wrapped twice around a histone octamer (two copies each of four histone proteins). Nucleosomes coil into 30-nm fibers, which loop into larger structures, which condense further during cell division into the visible chromosomes you see in mitosis.

The histones do more than pack DNA. They regulate which genes are accessible to transcription. Modifications of histone tails (acetylation, methylation, phosphorylation) signal whether the local DNA should be available for transcription or kept silenced. This is the foundation of **epigenetics** — heritable changes in gene expression that don't involve changes in DNA sequence. Eukaryotic gene regulation is partly chromatin regulation.

↳ **Dig Deeper — Bacterial epigenetics, briefly**

*Bacteria lack histones. They do have epigenetic-like inheritance.*

**Prompt:**
> Describe what bacterial epigenetics looks like. Cover DNA methylation in bacteria (Dam and Dcm methylation in *E. coli*, restriction-modification systems, methylation-dependent gene regulation), the inheritance of regulatory states across cell divisions, and the relationship between epigenetics in bacteria and phase variation. How does the picture differ from the histone-based epigenetics of eukaryotes? Are there examples of bacterial epigenetic inheritance that affect pathogenicity?

**What to do with the output:** Bacterial epigenetics is rarely covered in microbiology textbooks. The phenomena are real and clinically relevant for some pathogens. Save the answer; carry it to Chapter 11 (gene regulation) and Chapter 15 (pathogenicity).

Archaea also have histone-like proteins that organize their DNA, more like eukaryotes than like bacteria. This is one of the threads that connects Archaea to Eukarya more closely than to Bacteria.

### Plasmids

In addition to the main chromosome, many bacteria carry **plasmids**: small, circular, extrachromosomal DNA molecules. Plasmids replicate independently of the chromosome and can be transferred between bacteria.

Plasmids typically carry genes that are useful but not essential — antibiotic resistance, virulence factors, the ability to use unusual carbon sources, conjugation machinery. A bacterium with a plasmid encoding ampicillin resistance is resistant to ampicillin; cure the bacterium of the plasmid (by various lab tricks) and it becomes susceptible again.

Plasmids matter clinically because they move. Plasmids transferred between bacteria carry resistance genes from one species to another. Hospital-acquired infections often involve resistance plasmids that have circulated through multiple bacterial species. We will detail the mechanisms of plasmid transfer in Chapter 11 (conjugation) and the resistance consequences in Chapter 14.

Plasmids are also the foundation of recombinant DNA technology. Cloning genes into plasmid vectors, transforming the plasmids into *E. coli*, and growing the bacteria as protein factories is how we make insulin, growth hormone, and many other recombinant therapeutics. We will detail this in Chapter 12.

↳ **Dig Deeper — Plasmid incompatibility and how the bacterial cell manages multiple plasmids**

*A bacterium often carries several plasmids simultaneously. Some plasmids cannot coexist with others. The rules of plasmid compatibility tell you something about how plasmids manage their own population dynamics.*

**Prompt:**
> Describe plasmid incompatibility — the observation that two plasmids of the same "incompatibility group" cannot stably coexist in the same cell. What is the molecular basis (shared replication or partitioning systems)? How do clinicians and researchers use Inc-typing to track resistance plasmids? What does the existence of incompatibility groups tell us about the population biology of plasmids within bacterial cells?

**What to do with the output:** This is one of the more practical bits of plasmid biology for tracking antibiotic resistance spread. Hold for Chapter 14 (antimicrobials).

## What the chapter is really about

DNA is a molecule that does only two things by itself: it sits there, and it base-pairs with complementary molecules. Everything else — replication, transcription, repair, packaging — is done by other molecules (proteins, mostly) that read the DNA. The DNA is the medium. The cell's protein machinery is the reader.

This is worth noticing because it explains a fact about heredity that is otherwise mysterious: the same DNA sequence, in different cells, can produce different behaviors. Liver cells and neurons in your body have the same genome. They behave entirely differently. They behave differently because they read different parts of the genome, at different times, in response to different signals. The information is in the DNA; the *interpretation* of the information is in the rest of the cell.

For microbiology, this means that a bacterium's behavior depends on its DNA but is not determined by it. A genome with virulence genes encodes the potential for pathogenicity. Whether and when the bacterium actually expresses those genes — and therefore actually causes disease — depends on signals from the environment, regulatory networks within the cell, and the state of the host. Genotype enables; phenotype is what actually happens.

I want you to carry this distinction. It will matter when we get to gene regulation (Chapter 11), pathogenicity (Chapter 15), and antimicrobial resistance (Chapter 14). The shorthand "the bacterium has the gene" is often less informative than "the bacterium expresses the gene under these conditions." Always ask which one you actually know.

## Still puzzling

I do not understand, mechanistically, why eukaryotic gene regulation is as elaborate as it is. Bacterial gene regulation is built on a small number of common mechanisms (operons, sigma factors, two-component systems). Eukaryotic gene regulation involves transcription factor combinatorics, histone modifications, DNA methylation, non-coding RNAs, three-dimensional chromosome architecture, and a great deal else. The added complexity presumably allows finer control of more genes across more cell types. But the marginal value of each layer of additional complexity is unclear to me. Some of it may be evolutionary baggage — old systems that never got cleaned up. Some of it is presumably essential. We do not have a good principled account of which is which.

## What would change my mind

The picture of the bacterial chromosome as a single circular molecule has held up well, but in the last decade some bacteria have been found to have linear chromosomes, multiple chromosomes, or both. *Borrelia burgdorferi*, the Lyme disease organism, has a linear chromosome and many linear and circular plasmids. *Vibrio cholerae* has two chromosomes. If the diversity of bacterial chromosome architectures turns out to be larger than the textbook treatment suggests, the "single circular chromosome" generalization will need to weaken. `[verify: current understanding of bacterial chromosome architecture diversity as of 2026]`

## LLM exercises

1. **Why thymine.** Ask the LLM to explain why DNA uses thymine instead of uracil, given that they're chemically very similar. Press for the deamination argument and ask whether it is the full story.
2. **Reading the strand.** Give the LLM a single-strand DNA sequence (say, 5'-ATGCCATGCATTGC-3') and ask it to write the complementary strand, identify the 5' and 3' ends correctly, and explain why antiparallel orientation is necessary for base pairing.
3. **Genotype vs phenotype puzzle.** Describe a clinical scenario where a bacterium tests positive for a *vanA* resistance gene but appears susceptible to vancomycin in lab testing. Ask the LLM to propose three different explanations for the genotype-phenotype mismatch. Critique each.
4. **The RNA world hypothesis, evaluated.** Ask the LLM to summarize the RNA world hypothesis and list five lines of supporting evidence. Then ask for three lines of counter-evidence or unresolved problems. Both should be specific enough to be checkable.
5. **Plasmid biology and resistance spread.** Ask the LLM to explain how a resistance plasmid carried by a harmless *E. coli* in your gut could end up in a hospital-acquired *Klebsiella pneumoniae* causing pneumonia. Trace the chain of events and identify which steps are most or least likely under typical conditions.

## References

[^1]: Avery, O.T., MacLeod, C.M., McCarty, M. "Studies on the chemical nature of the substance inducing transformation of pneumococcal types." *Journal of Experimental Medicine* 79, no. 2 (1944): 137–158. doi:10.1084/jem.79.2.137.
[^2]: Dahm, R. "Friedrich Miescher and the discovery of DNA." *Developmental Biology* 278, no. 2 (2005): 274–288. doi:10.1016/j.ydbio.2004.11.028.
[^3]: Watson, J.D. and Crick, F.H.C. "Molecular Structure of Nucleic Acids: A Structure for Deoxyribose Nucleic Acid." *Nature* 171, no. 4356 (1953): 737–738. doi:10.1038/171737a0.
[^4]: Gilbert, W. "Origin of life: the RNA world." *Nature* 319, no. 6055 (1986): 618. doi:10.1038/319618a0.
---

## LLM Exercise — Chapter 10: Biochemistry of the Genome (Microbe Profile Database Project)

**Project:** Microbe Profile Database.
**What you're building this chapter:** genome-level fields (size, GC%, plasmids, key genes) across all existing entries.
**Tool:** **Cowork**.

---

**The Prompt:**

```
Chapter 10 of my Microbe Database project. Chapter 10 covered
genome biochemistry — DNA replication mechanisms (semi-conservative,
bidirectional, key enzymes); transcription and translation in
bacteria vs. eukaryotes; genome organization (circular bacterial
chromosome, plasmids, eukaryotic linear chromosomes with telomeres
and histones); GC content as a microbial-classification metric.

Schema additions:
- **Genome_size_bp**: in base pairs (specific number where known).
- **GC_content_percent**: percentage of G+C in genome.
- **Plasmids**: known plasmids (especially clinically important
  ones like virulence or resistance plasmids).
- **Notable_genes**: short list of clinically relevant genes
  (mecA in MRSA, ctxA in V. cholerae, etc.).

Backfill these for existing entries. Most entries should have
genome size (well-characterized). Notable values:
- E. coli: ~4.6 Mb, ~50% GC, F-plasmid common.
- M. tuberculosis: ~4.4 Mb, ~65% GC (high — Actinobacteria
  characteristic).
- S. aureus: ~2.8 Mb, ~33% GC; mecA plasmid for MRSA.
- HIV-1: ~9.7 kb (very small for a complex pathogen).
- Plasmodium falciparum: ~23 Mb (large for parasitic; has 14
  chromosomes).

End with: query — "show me organisms grouped by genome size."
The pattern: viruses (kb-scale) < bacteria (Mb-scale) < eukaryotes
(10-100 Mb scale). Note any exceptions.
```

---

**What this produces:** Genome-level fields populated. Database remains ~26-31 entries but now richer.

**Connection to previous chapters:** Cell-structure (Ch 3) + biochemistry (Ch 7) + genome (Ch 10) form the molecular-architecture spine.

**Preview of next chapter:** Chapter 11 covers genetic mechanisms — mutation, transformation, transduction, conjugation, horizontal gene transfer. Adds horizontal-gene-transfer fields.


---

## AI Wayback Machine

**Oswald Avery** was showed in 1944 that DNA — not protein — is the transforming principle of bacterial heredity.

**Run this:**

```
Who is Oswald Avery, and how does their work connect to biochemistry of the genome we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Oswald Avery"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Oswald Avery's ideas to a contemporary microbiology problem.
- Add a constraint: "Answer including criticisms or limits of Oswald Avery's framework."

What changes? What gets better? What gets worse?
