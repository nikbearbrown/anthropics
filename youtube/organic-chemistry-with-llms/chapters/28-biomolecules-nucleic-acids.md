# Chapter 28 — Biomolecules: Nucleic Acids

*The genetic code is written in just four letters — A, T, G, C — arranged in a polymer of staggering size. Decoding how that alphabet stores and transmits biological information is one of the great achievements of 20th-century science.*

In 1953, Watson and Crick published a one-page paper proposing that DNA is a double helix — two polynucleotide strands wound around each other, with hydrogen-bonded base pairs (A with T, G with C) on the inside. Sixty years later, we have sequenced the genomes of thousands of species, including the 3.2-billion-letter human genome. The structural model in that 1953 paper has held up to every subsequent test, and the genetic code (which letters spell which amino acids) is now known down to the level of every individual codon.

This chapter is about the chemistry of nucleic acids — how their components (nucleosides, nucleotides) are built, how they polymerize into DNA and RNA, and how they store and transmit genetic information. The chemistry is mostly chemistry we've covered: glycoside formation (Chapter 25), phosphate ester chemistry, hydrogen bonding (Chapter 2), aromatic heterocycle chemistry (Chapter 24). What's new is the *information* side: how a sequence of bases encodes a sequence of amino acids in a protein, and how that's read out by molecular machinery.

## Nucleosides and nucleotides

A *nucleoside* is a sugar (5-carbon, ribose for RNA or 2'-deoxyribose for DNA) glycosidically bonded to a heterocyclic base. The bond is from the C1' of the sugar to a nitrogen of the base.

A *nucleotide* is a nucleoside with a phosphate group attached, typically at the 5'-OH of the sugar. The phosphate can be a monophosphate, diphosphate, or triphosphate (mono, di, tri P).

The bases come in two types:

**Purines** (a fused 6+5 ring system with four N atoms):
- Adenine (A)
- Guanine (G)

**Pyrimidines** (a 6-membered ring with two N at 1,3-positions):
- Cytosine (C) — in both DNA and RNA
- Thymine (T) — only in DNA
- Uracil (U) — only in RNA (replaces thymine)

The structural difference between thymine and uracil: thymine has a methyl group on C5, uracil has H. The methyl group makes thymine slightly more chemically stable than uracil — relevant for DNA's role as long-term genetic storage versus RNA's role in shorter-lived processes.

Sugars:

**Ribose**: an aldopentose (C₅H₁₀O₅) with OHs at C1', C2', C3', C5'.

**2'-deoxyribose**: ribose with the C2' OH replaced by H.

The 2'-deoxy structure is what makes DNA more chemically stable than RNA. The 2'-OH in RNA can attack the adjacent 3'-phosphate intramolecularly, leading to chain cleavage. DNA, lacking that 2'-OH, can't do this — so DNA is hundreds of times more chemically stable than RNA in solution.

The naming convention with primes (3', 5', etc.) is to distinguish sugar carbons from base ring positions. The sugar carbons are numbered 1', 2', 3', 4', 5'.

## Polynucleotides

Nucleotides are linked into chains by *phosphodiester bonds* — the phosphate of one nucleotide connects to the 3'-OH of one sugar and the 5'-OH of the next. The polymer has directionality: the 5' end has a free phosphate (or HO-P-O-), and the 3' end has a free OH on the C3' carbon.

By convention, sequences are written from 5' to 3'. So the sequence "5'-AGCTGGAT-3'" describes a specific octanucleotide.

A *single strand of DNA* (or RNA) is a polymer of these nucleotides — typically thousands to millions of nucleotides long.

## The double helix

In 1953, Watson and Crick proposed (using crystallographic data from Rosalind Franklin and Maurice Wilkins, plus chemical understanding from Erwin Chargaff) that DNA is a double helix.

Two single strands run antiparallel — one runs 5' to 3' going up; the partner runs 5' to 3' going down. The two strands are wound around each other in a right-handed double helix with about 10.5 base pairs per turn and a pitch of about 34 Å.

The bases face inward, hydrogen-bonded to bases on the partner strand. The sugar-phosphate backbones are on the outside. The structure has two grooves: a *major groove* (about 22 Å wide) where most of the base-specific recognition by proteins happens, and a *minor groove* (about 12 Å wide) where some other recognition happens.

The base pairing is specific:
- A pairs with T (or U in RNA), through two hydrogen bonds.
- G pairs with C, through three hydrogen bonds.

Why? Because the sizes and hydrogen-bond donor/acceptor patterns match precisely for these pairings. A purine (size: 5+6 ring) must pair with a pyrimidine (size: 6 ring) to give a 1:1 width across the helix; pyrimidine-pyrimidine pairs are too narrow, purine-purine pairs are too wide. And among A-T vs A-C: A's two H-bond donors (the N6 amino group and the N1 imine nitrogen) match T's H-bond acceptors and donors, while they don't match C's. Similarly, G-C matches; G-T does not.

The strict Watson-Crick base pairing rules give DNA its information-storage capacity. The sequence of one strand uniquely determines the sequence of the other. This is the structural basis for DNA replication: each strand serves as a template to copy the other.

## DNA replication

To replicate DNA, the two strands separate (the H-bonds break locally, with help from helicase enzymes), and each strand serves as a template. DNA polymerase reads each strand and incorporates the complementary nucleotide. The result is two double-helical DNA molecules where there was one — *semiconservative replication*: each new molecule has one old strand and one new strand.

The chemistry of DNA polymerase: a deoxynucleotide triphosphate (dNTP, like dATP) is added to the growing strand. The 3'-OH of the growing strand attacks the α-phosphate of the dNTP. Pyrophosphate (PPᵢ) is released. A new phosphodiester bond is formed.

The reaction is energetically favorable because of the leaving group — pyrophosphate is a good leaving group, and its hydrolysis by another enzyme drives the reaction further forward.

Replication is fast: about 1000 nucleotides per second per polymerase molecule, with very high accuracy (about 1 error per 10⁹ nucleotides incorporated). The high accuracy is achieved by proofreading — DNA polymerase has a separate exonuclease activity that removes incorrectly incorporated bases.

## Transcription and translation

The flow of information from DNA to protein:

1. **Transcription**: a region of DNA is read by RNA polymerase to make a complementary RNA molecule (messenger RNA, mRNA). The RNA uses U instead of T, and it has the same sequence as the DNA's "coding strand" (with T → U).

2. **Translation**: the mRNA is read by ribosomes, which assemble proteins one amino acid at a time. The mRNA is read in codons (3-nucleotide groups). Each codon specifies one amino acid (or a stop signal).

The genetic code:

| First base | Second base ↓ | Third base | Amino acid |
|---|---|---|---|
| 64 codons total, 20 amino acids encoded plus 3 stop codons | | | |

Some examples:
- AUG → Met (also the start codon)
- UAA, UAG, UGA → stop
- UUU, UUC → Phe
- UCN (any) → Ser
- GGN (any) → Gly
- CGN (any) → Arg

The code is *redundant* — most amino acids have multiple codons (typically 2, 4, or 6). The redundancy is mostly in the third position (the "wobble" position) where multiple bases can be tolerated. This degeneracy means that most single-base mutations don't change the amino acid encoded.

The code is essentially universal across all known life — the same codon table works in bacteria, plants, animals, and archaea (with a handful of small exceptions in mitochondria and a few protozoa). This universality is one of the strongest pieces of evidence that all life on Earth shares a common ancestor.

The translation process: tRNAs (transfer RNAs) carry amino acids and read codons via complementary "anticodons." The ribosome, a giant ribonucleoprotein machine, holds the mRNA, brings in tRNAs in sequence, and catalyzes peptide bond formation.

## DNA sequencing

The first DNA sequencing methods were:
- **Sanger sequencing** (Frederick Sanger, Nobel Prize 1980). Uses a controlled chain-termination chemistry: dideoxynucleotides (ddNTPs) are mixed with regular dNTPs in DNA polymerase reactions. When a ddNTP is incorporated, the chain stops growing (because there's no 3'-OH to extend). By labeling each ddNTP differently and running the products on a gel (or now in a capillary), the sequence is read out. Capable of sequencing about 800 bases per run.

- **Maxam–Gilbert sequencing**. Uses chemical cleavage of a labeled DNA to give fragments that can be read on a gel. Mostly historical now.

Modern sequencing technologies are much faster and cheaper:
- **Illumina (sequencing by synthesis)**: uses fluorescent dye-terminated nucleotides and reads single bases as they're added. Throughput: billions of bases per run.
- **Pacific Biosciences (PacBio) single-molecule real-time (SMRT) sequencing**: reads long sequences (tens of kilobases) of single DNA molecules.
- **Oxford Nanopore**: passes DNA through a protein nanopore and detects bases by changes in electrical current. Long reads, but historically lower accuracy than other methods.

The cost of sequencing has dropped exponentially since 2005 — from about $100 million per genome (the Human Genome Project) to about $200 per genome today (in clinical settings). This drop is one of the most dramatic technology cost curves of any field.

## Polymerase chain reaction (PCR)

PCR (Kary Mullis, Nobel Prize 1993) amplifies a specific DNA sequence millions or billions of times. The reaction uses:
- A pair of *primers* (short DNA sequences, ~20 nucleotides each) that are complementary to the ends of the target sequence.
- A heat-stable DNA polymerase (Taq polymerase, originally isolated from a hot-spring bacterium).
- dNTPs.
- Template DNA.

Each cycle:
1. *Denature* (95°C): the double-stranded DNA separates.
2. *Anneal* (55–60°C): the primers bind to their complementary positions.
3. *Extend* (72°C): the polymerase extends from each primer to give a new copy.

Each cycle doubles the number of target molecules. After 30 cycles, you have 2³⁰ ≈ 10⁹ copies of the target sequence — enough to work with even from a tiny starting amount.

PCR is fundamental to:
- Forensics (DNA from a single hair).
- Diagnosis of pathogens (PCR-based COVID tests).
- Medical genetics.
- Cloning and molecular biology.

## CRISPR and gene editing

CRISPR-Cas9 is a more recent technology (Jennifer Doudna and Emmanuelle Charpentier, Nobel Prize 2020) for editing specific DNA sequences in a living cell. The Cas9 protein is a programmable DNA-cutting enzyme; a "guide RNA" tells it where to cut. After the cut, the cell's repair machinery can either repair the break (sometimes with errors that disrupt a gene) or be tricked into inserting a new sequence.

CRISPR is now used routinely in laboratories to make targeted mutations in any organism whose cells can be transfected. Therapeutic applications are emerging — in 2023, a CRISPR-based therapy (Casgevy) was approved for sickle-cell disease.

## Synthetic nucleic acids

Solid-phase oligonucleotide synthesis can build short DNA or RNA sequences efficiently. The chemistry uses *phosphoramidite chemistry*: a protected nucleotide is added to a growing chain on a solid support, the protecting group is removed, and the next nucleotide is added. About 30–60 nucleotides can be made cleanly per synthesis.

For longer sequences, individual oligonucleotides are made, then enzymatically joined (using DNA ligase) to make full genes or larger constructs. This is the basis of synthetic biology — designing and building DNA sequences (and the encoded proteins) from scratch.

The 2010 Nobel Prize in chemistry to John Polanyi was for related work on chemical reaction dynamics. The 2010 Nobel Prize in chemistry to Heck, Negishi, and Suzuki (palladium-catalyzed cross-coupling) is also indirectly related — many synthetic biology workflows use cross-coupling to make complex aromatic and heterocyclic substrates that are then used as nucleic acid mimetics.

↳ **Dig Deeper — Why DNA's information density is so high**

> A DNA double helix has about 0.34 nm per base pair. The human genome is 3 × 10⁹ base pairs. Calculate the storage density (in bytes per cubic meter), compare to other information storage media (silicon-based memory, magnetic tape), and explain why DNA is being explored as a long-term archival storage medium. Also discuss limitations: read/write speed, cost, error rates.

**What to do with the output:** Verify the calculation with the numbers above. The volume of DNA encoding the human genome is about 6 picoliters (6 × 10⁻¹⁵ m³). Compare to a hard drive of equivalent storage capacity (about 1.5 GB, or 0.5 TB-class drives — about 100 cm³). DNA is about 10¹⁵ times denser. Verify Claude correctly identifies the major limitations (read speed, cost of synthesis, ecological storage requirements like temperature and humidity).

## What this chapter does

Nucleic acids (DNA and RNA) are polymers of nucleotides, each of which is a sugar (ribose or 2'-deoxyribose) plus a base (purine or pyrimidine) plus a phosphate. The bases in DNA are A, T, G, C; in RNA they are A, U, G, C.

Two single strands of DNA pair through specific hydrogen-bonded base pairs (A-T, G-C) to form a right-handed double helix. The structure was deduced by Watson, Crick, Franklin, and Wilkins in 1953 from chemical and crystallographic evidence.

DNA is replicated semiconservatively: each strand templates a new partner strand. The chemistry is run by DNA polymerase, which adds dNTPs to a growing 3'-end with high accuracy (1 error per 10⁹ bases, including proofreading).

Information flow: DNA → RNA (transcription) → protein (translation), with a 64-codon genetic code that is essentially universal across all life.

Chemistry-based sequencing (Sanger) gave way to high-throughput technologies (Illumina, PacBio, Nanopore) that have dropped the cost of sequencing genomes by a factor of 10⁵ over two decades. PCR amplifies specific sequences using primers and a thermostable polymerase. CRISPR-Cas9 enables targeted gene editing in living cells.

The next chapter (29) covers metabolic pathways — how all of these biomolecules (carbohydrates, lipids, amino acids, nucleic acids) are made and broken down in cells, with the same chemistry we've covered throughout the book applied at biological scale.

---

*Source for all data, examples, and historical references: OpenStax* Organic Chemistry*, Chapter 28, modules m00319 through m00327.*
---

## LLM Exercise — Chapter 28: Biomolecules — Nucleic Acids (Synthesize a Target Molecule Project)

**Project:** Synthesize a Target Molecule.
**What you're building this chapter:** nucleotide/nucleic-acid analysis if applicable; otherwise structural commentary.
**Tool:** **Claude Project**.

---

**The Prompt:**

```
Chapter 28 of my Synthesis project. Chapter 28 taught: nucleotide
structure (nitrogenous base — purine ATG / pyrimidine CT-U + sugar
— deoxyribose for DNA, ribose for RNA + phosphate); phosphodiester
linkages connecting nucleotides in DNA and RNA chains; Watson-
Crick base pairing (A-T, G-C in DNA; A-U, G-C in RNA);
nucleoside vs. nucleotide (the phosphate is the difference).

Write the brief's "Nucleic Acid Analysis" section in 200–400
words.

If your target IS a nucleoside, nucleotide, or contains nucleic
acid features:

1. **Identify the components.** Which base? Which sugar (ribose
   or deoxyribose)? How many phosphates?

2. **Linkage analysis.** If multiple nucleotides are connected:
   the phosphodiester linkages.

3. **Antiviral/anticancer relevance.** Many nucleoside-mimic drugs
   exist (acyclovir, AZT, gemcitabine, ribavirin). Most work by
   incorporating into DNA/RNA and blocking further replication.
   If your target is one of these, briefly note the mechanism.

4. **Synthesis approach.** Nucleoside synthesis usually involves
   either:
   - Modification of an existing nucleoside.
   - Coupling of base + sugar (challenging due to stereochemistry
     at the anomeric carbon).
   - Total synthesis of base + sugar separately, then coupling.

If your target is NOT a nucleotide:

1. **State that.** Note that most drugs are not nucleotide-derived.

2. **Structural-fluency check.** Briefly: can you identify a
   purine vs. pyrimidine base on sight? Distinguish ribose from
   deoxyribose by the 2'-position? These are useful structural
   recognition skills even for non-nucleotide chemists.

End with: how would your target's behavior change if a phosphate
group were attached to one of its hydroxyl groups? (Phosphates
are highly polar and charged — they typically lock molecules out
of cell membranes unless the phosphate is enzymatically
generated inside the cell.)
```

---

**What this produces:** A 200–400 word section. For nucleoside-analog drugs (HIV antivirals, cancer drugs), central. For most drugs, brief.

**Connection to previous chapters:** Ch 25 (sugar chemistry) + Ch 26 (peptide nitrogen chemistry) + Ch 28 (combining sugar with N base) form the nucleic-acid backbone.

**Preview of next chapter:** Chapter 29 covers metabolic pathways. You'll trace your target's metabolic fate in the body (Phase I, Phase II metabolism), and see organic-mechanism analogs of enzyme-catalyzed reactions.


---

## AI Wayback Machine

**Phoebus Levene** was identified the components of DNA — sugar, phosphate, and base — and the structure of the nucleotide in the early 20th century.

**Run this:**

```
Who is Phoebus Levene, and how does their work connect to nucleic acids we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Phoebus Levene"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Phoebus Levene's key experiments or syntheses in detail.
- Add a constraint: "Answer including criticisms or limits of Phoebus Levene's framework."

What changes? What gets better? What gets worse?
