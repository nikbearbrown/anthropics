# Chapter 26 — Biomolecules: Amino Acids, Peptides, and Proteins

*Twenty amino acids in different sequences and three-dimensional arrangements account for essentially every protein in biology — about 50,000 enzymes, plus structural proteins, antibodies, hormones, and transporters. The chemistry that governs how amino acids combine and fold is the chemistry of organic functional groups, applied at scale.*

A typical mammalian cell contains about 10⁹ protein molecules, in roughly 10,000–20,000 distinct types. Each one is built from a sequence of amino acids — selected from a pool of 20 — connected by peptide bonds (amides). The sequence determines everything: which protein it is, how it folds in three dimensions, what it does. A change of one amino acid in a sequence of 300 can be completely silent, can subtly alter activity, or can produce a serious genetic disease. The information density of protein sequences is enormous, and the chemistry is — at the level of bonds and reactions — chemistry we've already covered.

This chapter introduces the amino acid building blocks, the peptide bonds that join them, the four levels of protein structure, and a brief survey of how proteins are sequenced and synthesized. Most of the chemistry is amide formation and amine reactions (Chapters 21 and 24). What's new here is the *scale* and the *folding* — how 100+ amino acid sequences become functioning machines that catalyze chemical reactions or generate antibody diversity or hold tissues together.

## The 20 amino acids

Every amino acid in proteins has the same general structure: an α-amino group (–NH₂) and an α-carboxylic acid (–COOH) on the same carbon (the α-carbon), with one of 20 different side chains (R groups) also attached.

$$\text{H}_2\text{N-CH(R)-COOH}$$

The α-carbon is a chirality center (except for glycine, where R = H). Almost all naturally occurring amino acids are L- (or, in CIP nomenclature, S-, except for cysteine, which is R because of the priority of S vs. C — cysteine is L by historical convention).

The 20 amino acids are usually grouped by side chain character:

**Nonpolar / hydrophobic:**
- Glycine (Gly, G): R = H
- Alanine (Ala, A): R = CH₃
- Valine (Val, V): R = CH(CH₃)₂
- Leucine (Leu, L): R = CH₂CH(CH₃)₂
- Isoleucine (Ile, I): R = CH(CH₃)CH₂CH₃
- Proline (Pro, P): R cyclizes to N (secondary amine)
- Methionine (Met, M): R = CH₂CH₂SCH₃
- Phenylalanine (Phe, F): R = CH₂C₆H₅
- Tryptophan (Trp, W): R = CH₂(indole)

**Polar uncharged:**
- Serine (Ser, S): R = CH₂OH
- Threonine (Thr, T): R = CH(OH)CH₃
- Cysteine (Cys, C): R = CH₂SH
- Tyrosine (Tyr, Y): R = CH₂C₆H₄OH
- Asparagine (Asn, N): R = CH₂CONH₂
- Glutamine (Gln, Q): R = CH₂CH₂CONH₂

**Acidic (negatively charged at pH 7):**
- Aspartate (Asp, D): R = CH₂COOH (pKa ≈ 3.9)
- Glutamate (Glu, E): R = CH₂CH₂COOH (pKa ≈ 4.1)

**Basic (positively charged at pH 7):**
- Lysine (Lys, K): R = (CH₂)₄NH₂ (pKa of NH₃⁺ ≈ 10.5)
- Arginine (Arg, R): R = (CH₂)₃NH-C(=NH)-NH₂ (pKa ≈ 12.5)
- Histidine (His, H): R = CH₂(imidazole) (pKa ≈ 6.0)

Each amino acid has a one-letter code and a three-letter code; both are widely used. Sequences of proteins are written as strings of one-letter codes (e.g., GVLEW... is the start of one specific protein).

## Zwitterions and isoelectric point

In water at neutral pH, an amino acid exists as a *zwitterion* — the carboxyl is deprotonated (–COO⁻) and the amino group is protonated (–NH₃⁺). The net charge is zero, but the molecule has both positive and negative charges:

$$\text{H}_3\text{N}^+\text{-CH(R)-COO}^-$$

The zwitterion is the predominant form because:
- The carboxyl pKa is about 2 (so at pH 7, it's deprotonated).
- The amine pKa (of the protonated form) is about 9 (so at pH 7, it's protonated).

The pH at which the molecule has zero *net* charge — even though it has both positive and negative regions — is called the *isoelectric point* (pI). For amino acids with neutral side chains, pI is the average of the two pKas: about (2 + 9)/2 = 5.5. For acidic amino acids (Asp, Glu), the side chain is also negatively charged at neutral pH, so the molecule has a net negative charge at pH 7; its pI is around 3 (where the side chain is protonated to give zero net charge). For basic amino acids (Lys, Arg), the side chain is positively charged at neutral pH; the pI is around 10.

The pI is useful in protein purification: at the pI, the molecule has no net charge and won't migrate in an electric field. Isoelectric focusing is a separation technique that uses this property to identify proteins by their pI.

## Acid-base properties of amino acids

The titration curve of an amino acid has plateau regions at each of its pKas. For glycine: pKa₁ = 2.34 (the carboxyl group), pKa₂ = 9.60 (the amino group). At pH below 2.34, the molecule is fully protonated (cation, +1). Between 2.34 and 9.60, it's the zwitterion (zero net charge). Above 9.60, it's fully deprotonated (anion, –1).

For amino acids with ionizable side chains, there's an additional pKa. Aspartate has pKa₁ = 1.99 (α-COOH), pKa₂ = 3.90 (side-chain –COOH), pKa₃ = 9.90 (α-NH₃⁺). The side chain's pKa controls how the molecule behaves around physiological pH.

Histidine's side chain pKa of about 6 is special — it's the only amino acid with a side chain in the physiological pH range. Because its imidazole has pKa 6, histidine residues in proteins are sometimes protonated and sometimes not at pH 7, and they can act as both proton donors and proton acceptors. This is why histidine is so common at active sites of acid-base catalytic enzymes.

## Peptide bonds and primary structure

Two amino acids combine by reaction of the carboxyl of one with the amino of the other, releasing water. The product is an amide bond, conventionally called a *peptide bond* in the protein context.

$$\text{H}_3\text{N}^+\text{-CHR}_1\text{-COO}^- + \text{H}_3\text{N}^+\text{-CHR}_2\text{-COO}^- \longrightarrow \text{H}_3\text{N}^+\text{-CHR}_1\text{-C(=O)-NH-CHR}_2\text{-COO}^- + \text{H}_2\text{O}$$

(Drawn with zwitterions; the actual termini are typically charged at physiological pH.)

A short chain (2–50 amino acids) is a *peptide*. A longer chain is a *protein*. The primary structure of a protein is its linear amino acid sequence, written N-terminus to C-terminus.

Chemical synthesis of peptide bonds requires activation of the carboxyl group (Chapter 21). Free amino acids don't combine spontaneously; under normal conditions, the amine deprotonates the acid and the salt forms instead. Peptide synthesis uses coupling reagents (DCC, EDC, HATU) that activate the carboxyl by converting the OH to a better leaving group.

## Peptide bond geometry

The peptide bond has substantial double-bond character due to amide resonance (Chapter 21). The C–N bond is shorter than a typical C–N (about 132 pm vs. 147 pm for C–N in an amine). The amide bond is essentially planar — six atoms (the α-C of the first residue, the carbonyl C and O, the N, the H on N, and the α-C of the next residue) all lie in a plane.

Rotation around the C–N is hindered by about 80 kJ/mol — slow on the seconds-to-minutes timescale at room temperature, but locked at biologically relevant timescales. The peptide bond exists in two configurations: trans (the two α-carbons on opposite sides of the C–N bond) and cis (on the same side). Trans is much more stable for almost all peptide bonds; only proline-containing bonds have a substantial cis content (about 5–10%).

This planar peptide bond is the structural unit of all protein folding. The φ (phi) angle around the N-Cα bond and the ψ (psi) angle around the Cα-C bond are the two degrees of freedom in the protein backbone. A *Ramachandran plot* shows allowed combinations of φ and ψ — most combinations are sterically forbidden, leaving the molecule with constrained backbone geometry.

## Secondary structure

Patterns of hydrogen bonding among backbone amides give protein backbones their secondary structure. The two major classes:

**α-Helix.** A right-handed helical structure with about 3.6 amino acid residues per turn. Each backbone N–H hydrogen-bonds to the C=O of the residue four positions back (i.e., i+4). The result is a tightly wound helix with a characteristic 5.4 Å pitch. α-helices are common in globular proteins (myoglobin and hemoglobin are largely α-helical) and they're the structure of many membrane-spanning protein domains. The helix is stable because the backbone is extensively hydrogen-bonded; side chains stick out radially.

**β-sheet.** Two or more peptide strands lying side by side, with the C=O of each strand H-bonded to the N–H of the next. Strands can be parallel (running the same direction N to C) or antiparallel (running in opposite directions). β-sheets are flat, with side chains alternating above and below the plane. Most globular proteins have at least some β-sheet content.

**Loops and turns.** Backbone segments that change direction, often using prolines and glycines (which provide flexibility) and sometimes specific four-residue β-turn motifs.

The α-helix and β-sheet were both predicted by Linus Pauling and Robert Corey in 1951, before any protein structures had been determined. They reasoned from the geometry of peptide bonds, hydrogen bonding rules, and steric constraints. The first experimental structures (Pauling's predicted α-helix in myoglobin, then β-sheets in silk fibroin) confirmed the models.

## Tertiary and quaternary structure

The *tertiary structure* of a protein is its complete three-dimensional shape — how the secondary structure elements (helices and sheets) are arranged in space, and how all the loops and turns connect them.

Tertiary structure is determined by:
- Hydrophobic interactions (nonpolar side chains cluster in the protein interior, away from water).
- Hydrogen bonds (side chain to backbone or side chain to side chain).
- Disulfide bonds (covalent S–S between two cysteines).
- Salt bridges (electrostatic between charged side chains, like Glu⁻ to Lys⁺).
- Coordinative bonds (with metal ions, in proteins like cytochromes).

The *quaternary structure* is the arrangement of multiple polypeptide chains (subunits) into a complex. Hemoglobin is four subunits (2α + 2β); cytochrome c oxidase is 13 subunits. Many enzymes are dimers, tetramers, or larger complexes.

## Protein folding

Each protein folds spontaneously to a specific three-dimensional structure determined by its amino acid sequence. The *folding code* is the question of how this happens in detail — how the sequence determines the structure.

For most proteins, folding takes seconds to minutes. The folding rate is typically far faster than the time required for an exhaustive search of all possible conformations (the *Levinthal paradox*). Folding is biased: certain partial structures form first (folding nuclei), then others assemble around them, in something like a parallel, biased search through conformational space.

Misfolding causes diseases. Cystic fibrosis arises from a single deletion in the CFTR protein that prevents proper folding. Many neurodegenerative diseases (Alzheimer's, Huntington's, Parkinson's) involve protein aggregates of misfolded forms.

The rules of protein folding are now substantially understood, and computational methods (most prominently, AlphaFold by DeepMind in 2020) can predict folded structures from sequence with high accuracy. This is one of the major recent breakthroughs in molecular biology.

## Sequencing and synthesis

**Edman degradation** (developed by Pehr Edman in the 1950s) sequences a peptide one amino acid at a time from the N-terminus. The N-terminal residue is labeled with phenyl isothiocyanate, which forms a thiazolinone derivative; the labeled residue is cleaved off and identified, leaving the rest of the chain ready for another round. About 30 cycles can be done before signal becomes limited.

Modern protein sequencing is mostly done by *mass spectrometry* — a peptide is fragmented along its backbone, and the masses of the fragments are used to deduce the sequence. This is much faster than Edman degradation and gives sequences for entire proteomes.

**Solid-phase peptide synthesis** (developed by Bruce Merrifield, Nobel Prize 1984) builds a peptide one residue at a time from the C-terminus. The C-terminal amino acid is anchored to a solid resin; the next residue is coupled to the free α-amino group; the cycle repeats. Each step uses a protecting group strategy (typically Fmoc for the α-amino, plus various protections for side chains) to prevent over-coupling. After all residues are added, the peptide is cleaved from the resin and the protecting groups are removed.

Modern automated peptide synthesizers can build peptides up to ~50 residues efficiently. Larger proteins are typically expressed in bacteria, yeast, or mammalian cells using recombinant DNA technology — synthesizing the gene encoding the protein and letting the cell make the protein for you.

## Enzyme catalysis

About 50,000 enzymes catalyze the reactions of metabolism in the human body. Each is a protein. Each has a specific *active site* — a pocket in the folded structure where the substrate binds and the reaction occurs.

Enzymes accelerate reactions by:
- Bringing reactants close together (intramolecular vs. intermolecular reaction).
- Orienting substrates correctly for reaction.
- Stabilizing transition states (the most important effect).
- Providing nearby acid/base groups for general acid-base catalysis (histidines!).
- Providing nucleophilic side chains (Ser, Cys, Lys) for covalent catalysis.

Rate enhancements of 10⁶ to 10¹⁷ are common. Without enzymes, life as we know it would not be possible — most metabolic reactions are too slow at body temperature to support a living organism.

The chemistry of enzyme catalysis is the chemistry we've covered, run in the active site of a protein. SN2 reactions, additions to carbonyls, condensations, hydride transfers — all the standard functional group reactions, accelerated and constrained by protein structure.

↳ **Dig Deeper — How AlphaFold predicts protein structure**

> Until 2020, predicting a protein's three-dimensional structure from its sequence was an unsolved problem after fifty years of work. AlphaFold by DeepMind solved it. Walk through what AlphaFold does. Cover: the input (sequence + multiple sequence alignment of related proteins from across evolution), the deep neural network architecture that processes pairwise residue distances, the iterative refinement, and what AlphaFold cannot do (predict effects of post-translational modifications, predict folding kinetics, handle proteins without homologs in the training set).

**What to do with the output:** Compare against the AlphaFold methods paper (Nature, 2021) for the deep learning architecture details. Verify that Claude correctly identifies that AlphaFold uses evolutionary information (multiple sequence alignment) as a key input — it's not a pure ab initio prediction.

## What this chapter does

The 20 amino acids combine via amide (peptide) bonds to form proteins. Each amino acid has an α-amino group, an α-carboxyl, and one of 20 distinct side chains. At neutral pH, amino acids exist as zwitterions (α-amino protonated, α-carboxyl deprotonated). The isoelectric point is the pH at which the molecule has zero net charge.

The peptide bond is planar, with substantial double-bond character due to amide resonance. This planar geometry is the structural unit of protein folding. Backbone hydrogen bonding gives rise to secondary structure: α-helices (i+4 H-bonds) and β-sheets (between strands, parallel or antiparallel).

Tertiary structure is the complete 3D fold of a single chain, determined by hydrophobic clustering, hydrogen bonds, disulfides, salt bridges, and coordinate bonds. Quaternary structure is the arrangement of multiple subunits.

Edman degradation sequenced peptides one residue at a time from the N-terminus; modern sequencing uses mass spectrometry. Solid-phase synthesis (Merrifield) builds peptides one residue at a time from the C-terminus.

Enzymes are proteins that catalyze the reactions of metabolism. Their chemistry is the chemistry of organic functional groups, run in the controlled environment of an active site.

The next chapters cover lipids (Chapter 27), nucleic acids (Chapter 28), and metabolic pathways (Chapter 29) — completing the survey of biomolecules.

---

*Source for all data, examples, and historical references: OpenStax* Organic Chemistry*, Chapter 26, modules m00299 through m00310.*
---

## LLM Exercise — Chapter 26: Amino Acids, Peptides, and Proteins (Synthesize a Target Molecule Project)

**Project:** Synthesize a Target Molecule.
**What you're building this chapter:** peptide/amino-acid analysis if applicable; otherwise structural commentary.
**Tool:** **Claude Project**.

---

**The Prompt:**

```
Chapter 26 of my Synthesis project. Chapter 26 taught: 20 standard
amino acids (each has -COOH, -NH₂, and a side chain R; classified
by side chain — nonpolar, polar, acidic, basic); pKa values
relevant to physiological state (carboxyl ~2, amine ~9, side
chains variable); isoelectric point (pI) where net charge = 0;
peptide bond formation (amine + carboxylic acid + activation →
amide); primary, secondary (alpha helix, beta sheet), tertiary,
quaternary structure; protein folding.

Write the brief's "Peptide/Amino Acid Analysis" section in 300–500
words.

If your target IS or contains a peptide:

1. **Identify the amino acid sequence.** List each amino acid
   from N-terminus to C-terminus.

2. **Predict the isoelectric point (pI).** Acidic side chains
   (Asp, Glu) and basic side chains (Lys, Arg, His) determine pI.

3. **Peptide synthesis approach.** Modern peptide synthesis is
   typically solid-phase peptide synthesis (SPPS, Merrifield
   method). For each peptide bond, propose:
   - Activation method (HATU, EDC, DCC).
   - Protecting groups (Boc for N-terminus during chain
     extension; Cbz alternative; side chain protections like
     Trt for Cys, Pbf for Arg).
   - Coupling conditions.

4. **Secondary structure preferences.** If your peptide is long
   enough to have secondary structure: which amino acids favor
   helices (Glu, Ala, Leu) vs. sheets (Val, Ile, Phe) vs. turns
   (Gly, Pro)?

If your target is NOT a peptide but contains amides:

1. **Note the amide linkages.** Each amide is essentially a
   peptide-bond analog. Was each amide bond formed by methods
   from Ch 21 (acid + amine activation) or could it have been
   made by amino-acid coupling?

2. **Pseudopeptides.** Many drugs are pseudopeptides — peptide-
   like structures with non-amino-acid building blocks. If your
   target is one of these, briefly identify what's "peptide-
   like" and what isn't.

End with: how does the protonation state at physiological pH
affect your target's solubility, transport, and binding?
```

---

**What this produces:** A 300–500 word section. For peptide drugs (insulin, oxytocin, vasopressin, GLP-1 agonists like semaglutide), this is central.

**Connection to previous chapters:** Ch 21 (amide formation) and Ch 24 (amine basicity) underpin amino acid chemistry.

**Preview of next chapter:** Chapter 27 covers lipids — fatty acids, triglycerides, phospholipids, steroids. If your target is a steroid (cortisol, cholesterol, sex hormones) or contains lipid features, this is central.


---

## AI Wayback Machine

**Frederick Sanger** was first sequenced insulin in 1955 and DNA in 1977 — only person to win two chemistry Nobels (1958, 1980).

**Run this:**

```
Who is Frederick Sanger, and how does their work connect to peptides and proteins we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Frederick Sanger"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Frederick Sanger's key experiments or syntheses in detail.
- Add a constraint: "Answer including criticisms or limits of Frederick Sanger's framework."

What changes? What gets better? What gets worse?
