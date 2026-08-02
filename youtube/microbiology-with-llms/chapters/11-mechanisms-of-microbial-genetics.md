# Chapter 11 — Mechanisms of Microbial Genetics

*Reproduction is the slow road. Microbes have many faster ones.*

## The question before the answer

Imagine a population of *E. coli* in your gut. There are perhaps 10⁹ of them per gram of intestinal contents. They are dividing slowly under your nutrient and oxygen conditions — maybe once every several hours — but the population is still doubling on a timescale you can measure in days.

Now imagine that, by chance, one of those cells encounters a fragment of DNA released by a dying bacterium of a different species — a fragment that happens to carry a gene for resistance to a common antibiotic. The encountering cell takes up the DNA. The new gene integrates into its chromosome. The cell now resists the antibiotic. It divides. Its descendants are all resistant.

Two weeks later, you take a course of that antibiotic for an unrelated infection. The susceptible *E. coli* die. The resistant ones do not. The resistant population blooms. By the end of the week, the *E. coli* in your gut are almost entirely descended from that one cell that took up the random DNA fragment two weeks ago.

That story is not hypothetical. It happens, in some form, constantly. It is the central reason antibiotic resistance spreads as fast as it does. And it requires understanding two intertwined things: how microbes inherit genes from parent to offspring (vertical transfer, the same way you inherit genes from your parents), and how microbes acquire genes from other microbes that are not their parents (horizontal transfer, which does not exist in the strict sense in animals).

This chapter is about both. The vertical part covers DNA replication, transcription, translation, mutation, and repair. The horizontal part covers transformation, transduction, and conjugation. The horizontal part is the one that makes microbial evolution faster — sometimes much faster — than vertical transfer alone can explain.

## Learning objectives

By the end of this chapter, you will be able to:

1. Explain semiconservative DNA replication and identify the role of each major enzyme in the replication fork.
2. Describe transcription in bacteria and explain how it differs from eukaryotic transcription.
3. Read the genetic code and explain why it is described as nearly universal.
4. Distinguish the major mutation types (point, frameshift, missense, nonsense, silent) and predict their effects on protein function.
5. Describe the three mechanisms of horizontal gene transfer (transformation, transduction, conjugation) and how each spreads antibiotic resistance.
6. Explain inducible and repressible operons and the logic of bacterial gene regulation.

Prerequisites: Chapter 10 especially, plus Chapters 1–9.

## DNA replication, step by step

Watson and Crick's 1953 paper closed with one of the most understated sentences in the history of biology: "It has not escaped our notice that the specific pairing we have postulated immediately suggests a possible copying mechanism for the genetic material."

The copying mechanism, worked out over the following decade, is **semiconservative replication**: the two strands of the double helix separate, and each serves as a template for the synthesis of a new complementary strand. The two resulting double helices each contain one parental strand and one new strand.

Meselson and Stahl, in 1958, confirmed this elegantly. They grew bacteria in medium containing heavy nitrogen (¹⁵N) for many generations, so that all the DNA was heavy. Then they switched to medium with normal (light) nitrogen and let the bacteria divide. After one round of replication, the DNA was a uniform intermediate density — exactly what semiconservative replication predicts (each helix containing one heavy and one light strand). After two rounds, half the DNA was intermediate and half was fully light. Other models of replication (fully conservative, or dispersive) predicted different bands. The intermediate band was the smoking gun.

### The enzymes

DNA replication requires a small set of enzymatic machines working together at the **replication fork** — the point where the parental DNA is unwound and the new strands are being synthesized.

**Helicase** unwinds the double helix at the fork, separating the two strands so they can be copied. The energy for unwinding comes from ATP hydrolysis.

**Single-strand binding proteins (SSBs)** coat the unwound single strands, preventing them from re-annealing or forming secondary structures that would block replication.

**Topoisomerase** (in bacteria, the version is called gyrase) handles the topological problem that unwinding the helix creates ahead of the fork. As the fork moves forward, it accumulates positive supercoils ahead of it; without relief, the helix would become impossibly tight. Topoisomerase cuts one or both strands, allows them to unwind, and reseals them.

**Primase** synthesizes short RNA primers complementary to the template strand. DNA polymerases cannot initiate synthesis from scratch — they can only extend an existing strand — so a short RNA primer is needed at the start of each new strand.

**DNA polymerase III** (in bacteria) is the main enzyme. It adds nucleotides to the 3' end of the new strand, reading the template strand in the 3' to 5' direction. The polymerase has remarkable accuracy — about one error per 10⁷ bases added — partly because of substrate specificity and partly because the enzyme has a proofreading function that removes incorrectly added nucleotides.

**DNA polymerase I** removes the RNA primers and fills in the gaps with DNA.

**DNA ligase** seals the gaps between fragments by forming the final phosphodiester bonds.

The geometry of the replication fork creates a complication. The two template strands run antiparallel, but DNA polymerase can only synthesize in the 5' to 3' direction. On one template strand (the leading strand), the polymerase can synthesize continuously as the fork moves forward. On the other template strand (the lagging strand), the polymerase has to synthesize *away* from the fork — which means it has to repeatedly restart, producing short fragments. These short fragments, called **Okazaki fragments**, are then joined together by ligase.

The whole machinery is a coordinated assembly: helicase opens the fork, primase adds primers, polymerase III extends, polymerase I cleans up primers, ligase seals gaps. The bacterial replication fork moves at roughly 1000 nucleotides per second. The *E. coli* chromosome (4.6 million base pairs) is replicated in about 40 minutes by two forks moving in opposite directions from a single origin of replication.

↳ **Dig Deeper — Replication faster than the cell can divide**

*E. coli under good conditions divides every 20 minutes. But the chromosome takes 40 minutes to replicate. How can the cell divide faster than its own DNA replication?*

**Prompt:**
> Explain the "multifork replication" strategy used by fast-growing *E. coli* to divide faster than its replication time. How do nested replication forks work? At what point in the cell cycle does the next round of replication initiate? Why does this require careful regulation, and what happens if multifork replication goes wrong? Then describe how slower-growing bacteria (e.g., *M. tuberculosis* with its 18-hour doubling time) handle replication and division differently.

**What to do with the output:** This is a counter-intuitive piece of bacterial biology. The 20-minute doubling time of *E. coli* requires a clever cheat that violates the naive picture of cell cycle.

### Differences in eukaryotes

Eukaryotic chromosomes are linear and longer, so they have multiple origins of replication firing in parallel. Eukaryotic DNA polymerases (alpha, delta, epsilon, primarily) are different enzymes from the bacterial ones, with different domain architectures. Eukaryotes have a special enzyme, **telomerase**, that handles the linear-chromosome problem: at the end of each chromosome, the lagging-strand mechanism cannot finish all the way to the tip, and without telomerase the chromosome would shorten with each round of division. Telomerase adds a short repeat sequence to the chromosome ends to compensate. Most adult cells lack active telomerase, which is why somatic cells have a limited replicative lifespan. Cancer cells frequently express telomerase as one of the mutations that lets them divide indefinitely.

### Rolling circle replication

Some bacterial plasmids and some viral genomes replicate by a different mechanism, **rolling circle replication**. A nick is made in one strand of the circular DNA. The intact strand serves as a template; the nicked strand is displaced as a new strand is synthesized, growing from the nick. The displaced strand can be longer than one full circle — it "rolls" around the template multiple times — and the resulting concatemer is later cut into single-genome-length pieces. This mechanism is used by F factor plasmids during conjugation and by some bacteriophages (lambda, M13).

## Transcription

DNA is transcribed to RNA by **RNA polymerase**. The bacterial RNA polymerase is a single enzyme made of multiple subunits. It binds to a region called a **promoter** upstream of the gene, unwinds a short stretch of DNA, and synthesizes RNA complementary to one strand of the DNA (the template strand). The other strand (the coding strand) has the same sequence as the RNA, except with T instead of U.

Bacterial promoters have characteristic sequences. The -10 element (about ten bases upstream of the transcription start site) typically has the consensus TATAAT. The -35 element has the consensus TTGACA. RNA polymerase binds these consensus sequences with the help of a **sigma factor** — a subunit that gives the polymerase its promoter specificity. Different sigma factors recognize different promoters, which lets the cell turn on different gene sets under different conditions.

Transcription proceeds at about 50 nucleotides per second. It terminates at specific sequences — either by intrinsic termination (an RNA hairpin causing the polymerase to fall off) or by rho-dependent termination (an enzyme called rho that catches up to the polymerase and dislodges it).

### Eukaryotic transcription

Eukaryotes have three different RNA polymerases (I, II, and III) for different RNA classes. Polymerase II synthesizes mRNAs and is the most important for protein-coding genes.

Eukaryotic transcription has elaborate regulatory machinery: transcription factors that bind enhancer regions far from the gene, mediator complexes that bridge enhancers to the polymerase, chromatin remodelers that expose DNA for transcription. The promoter region contains a TATA box analogous to the bacterial -10 element.

Eukaryotic mRNAs are also processed before they leave the nucleus: a 5' cap is added (a modified guanine that protects the mRNA from degradation and helps ribosome binding), a 3' poly-A tail is added (which also affects stability), and **introns** are removed by splicing. Introns are non-coding sequences embedded within genes; the protein-coding parts are called **exons**, and splicing assembles a mature mRNA from the exons. Bacterial genes generally have no introns, which is one reason bacterial transcription and translation can happen simultaneously — there is no waiting for splicing.

## Translation and the genetic code

The mRNA produced by transcription is translated to protein by the ribosome. The ribosome reads the mRNA in groups of three nucleotides called **codons**. Each codon specifies an amino acid (or a stop signal). There are 4³ = 64 possible codons, and 20 amino acids, plus three stop codons (UAA, UAG, UGA). The code is therefore **degenerate** — most amino acids are specified by more than one codon.

The genetic code is **nearly universal** across all known life. The same codons specify the same amino acids in *E. coli*, in *Saccharomyces*, in plants, in humans. There are a few exceptions — some mitochondria and some ciliates use slightly modified codes — but the broad universality argues that the code was fixed early in evolution and has resisted change ever since.

↳ **Dig Deeper — Genetic code variants and why they exist**

*The "universal" code has documented exceptions. Some make obvious evolutionary sense; some are unexplained.*

**Prompt:**
> Catalog the major known variants of the genetic code. Cover mitochondrial codes (vertebrate, yeast, plant) and how they differ from the standard table; the *Mycoplasma* and *Spiroplasma* codes; the Candida CTG clade reading CUG as serine instead of leucine; and the inclusion of unusual amino acids (selenocysteine via UGA recoding, pyrrolysine via UAG recoding in some archaea). For each, identify whether the variant appears to have arisen by drift, by selection, or by some other mechanism.

**What to do with the output:** The "universal" code is only mostly universal. The exceptions are interesting in their own right and tell you about how robust molecular biology actually is.

The translation machinery has three main players:

- **The ribosome**: two subunits (small and large) that come together on the mRNA, with three binding sites (A, P, E) for tRNAs. The peptide-bond-forming activity is performed by ribosomal RNA — the ribosome is a ribozyme, as I mentioned in Chapter 10.
- **tRNAs**: each tRNA carries one amino acid and has an anticodon that pairs with one codon on the mRNA. The tRNA structure is a small molecule (about 80 nucleotides) folded into a characteristic L-shape, with the amino acid attached at one end and the anticodon loop at the other.
- **Aminoacyl-tRNA synthetases**: enzymes that charge each tRNA with its correct amino acid. There are 20 of these enzymes, one for each amino acid, and they implement the link between the genetic code and the amino acid identity. The synthetases are where the abstract code gets read into the physical world.

Translation proceeds at about 20 amino acids per second in bacteria. Protein synthesis is one of the most energy-expensive processes in the cell — synthesizing a single peptide bond costs four high-energy phosphate bonds.

In bacteria, **transcription and translation are coupled**: ribosomes can attach to an mRNA and start translating it while it is still being transcribed. This is possible because bacteria have no nucleus separating the two processes. In eukaryotes, transcription happens in the nucleus, mRNA processing happens in the nucleus, and translation happens in the cytoplasm after the mature mRNA is exported.

## Mutations

A **mutation** is a change in DNA sequence. Mutations happen during replication (when polymerase makes an error), from environmental damage (radiation, chemicals), and from spontaneous chemical events (deamination of cytosine to uracil, oxidation of bases). Most cells have repair systems that fix most damage, but some events escape repair and become permanent.

### Types of point mutations

A **point mutation** is a change to a single nucleotide. It can be:

- **Silent**: the new codon still codes for the same amino acid (due to code degeneracy). No effect on the protein.
- **Missense**: the new codon codes for a different amino acid. The protein has one amino acid substitution. The effect ranges from nothing (if the substitution is conservative — say, leucine for isoleucine) to catastrophic (if it disrupts the active site or the fold).
- **Nonsense**: the new codon is a stop codon. The protein is truncated. Usually nonfunctional.

A **frameshift mutation** is an insertion or deletion of one or two nucleotides (but not three). It shifts the reading frame of all downstream codons. The protein sequence becomes garbled from the point of the mutation onward, usually producing a nonfunctional truncated protein.

A **chromosomal mutation** is a larger change — a deletion of many nucleotides, an inversion, a translocation, a duplication. These can have effects ranging from loss of a gene to wholesale rearrangement of chromosomal structure.

### Mutagens

Mutations occur spontaneously at a low background rate. **Mutagens** are agents that increase the rate.

Chemical mutagens act by various mechanisms. Base analogs (5-bromouracil) substitute for normal bases and mispair. Alkylating agents (mustard gas, N-methyl-N'-nitro-N-nitrosoguanidine) add chemical groups to bases that change their pairing properties. Intercalating agents (ethidium bromide, acridines) insert themselves between bases in the DNA, causing the polymerase to slip and introduce frameshifts.

Radiation mutagenizes by causing direct chemical damage. Ultraviolet light produces thymine dimers — adjacent thymines covalently linked, distorting the DNA. Ionizing radiation (X-rays, gamma rays) breaks DNA strands, often both strands at once.

The **Ames test** uses mutagenicity in bacteria as a proxy for carcinogenicity in humans. The principle: a strain of *Salmonella* that requires histidine to grow is exposed to a test compound. If the compound induces back-mutation to histidine independence, the compound is mutagenic. About 90% of known carcinogens are mutagenic in the Ames test, and most Ames-positive compounds turn out to be carcinogenic, so the test serves as an inexpensive first screen. [^1]

### DNA repair

Cells have multiple repair systems:

- **Direct repair**: enzymes that reverse specific damage. *Photolyase* uses light energy to break thymine dimers. *Methyltransferases* remove abnormal methyl groups added by alkylating agents.
- **Excision repair**: damaged regions are cut out and resynthesized. **Nucleotide excision repair** removes bulky lesions like thymine dimers; **base excision repair** removes individual damaged bases.
- **Mismatch repair**: after replication, special enzymes scan the new DNA for mismatches (base pairs that don't pair correctly) and replace the wrong nucleotide on the new strand.
- **Recombination repair**: double-strand breaks are repaired using the sister chromatid or a homologous chromosome as a template.

The fidelity of DNA replication (one error per 10⁷ bases) and the existence of repair systems are why mutations are rare events. They are rare per cell per generation, but bacterial populations are so large that mutations accumulate quickly. A population of 10⁹ cells in your gut, each with a 10⁻⁷ mutation rate per base per generation, will produce many thousands of mutant cells per generation. Some of those mutations will, by chance, confer antibiotic resistance, virulence, or other selectable traits.

## Horizontal gene transfer

The other major source of genetic change in bacteria is the acquisition of DNA from other bacteria. There are three main mechanisms.

### Transformation

Some bacteria can take up DNA fragments directly from their environment. This is **transformation**. The cell incorporates the foreign DNA into its chromosome (or maintains it as a plasmid) by homologous recombination.

Bacteria that are competent for transformation include *Streptococcus pneumoniae* (the original Avery-MacLeod-McCarty experiment), *Bacillus subtilis*, *Haemophilus influenzae*, *Neisseria*. Some bacteria are naturally competent; others require treatment (calcium chloride, heat shock, electroporation) to become competent in the lab.

Transformation matters clinically: free DNA from dead bacteria is present in many environments, and uptake of resistance genes from environmental DNA is a documented route of resistance acquisition.

### Transduction

DNA can be transferred between bacteria by bacteriophages (Chapter 6). When a phage packages its progeny, it occasionally packages a piece of bacterial DNA by mistake — either a random piece (generalized transduction) or a specific piece adjacent to the prophage integration site (specialized transduction). When this defective phage infects a new bacterial cell, it injects the bacterial DNA instead of phage DNA, and the recipient cell incorporates it.

Transduction can transfer plasmids, including resistance plasmids. *Staphylococcus aureus* uses transduction extensively, and many of the antibiotic resistance genes in *S. aureus* — including the famous *mecA* gene that makes MRSA — are believed to have been spread, at least in part, by phage transduction.

### Conjugation

The third and arguably most important mechanism. **Conjugation** is the direct transfer of DNA from one bacterial cell to another through a physical connection between them.

The mechanism: a donor bacterium has a special plasmid (the F factor in *E. coli*) that encodes a **sex pilus** — a long, hollow appendage that extends from the donor cell, contacts a recipient cell, and pulls the two cells together. A pore forms between the cells. The donor copies its plasmid by rolling circle replication, and one strand is transferred through the pore into the recipient. The recipient assembles a complementary strand, producing a functional plasmid. The recipient is now a donor.

Conjugation is the most efficient mechanism for transferring large pieces of DNA between bacteria. It can transfer plasmids between very distantly related species. The conjugative plasmid R100, for example, can transfer between *E. coli*, *Klebsiella*, *Salmonella*, *Shigella*, *Proteus*, and *Pasteurella*. The resistance genes carried by R100 spread accordingly.

Some conjugative plasmids integrate into the bacterial chromosome, becoming **Hfr** (high-frequency recombination) strains. An Hfr donor can transfer chromosomal genes to a recipient. The Hfr mechanism is how the first genetic maps of *E. coli* were made in the 1950s — by interrupting conjugation at different time points and seeing which genes had been transferred.

↳ **Dig Deeper — Conjugation as bacterial sex (and the politics of that metaphor)**

*Calling conjugation "bacterial sex" is a useful pedagogical shortcut and a misleading one.*

**Prompt:**
> Compare and contrast bacterial conjugation with eukaryotic sexual reproduction. In what ways is the "bacterial sex" analogy accurate? In what ways does it mislead? Cover at minimum: who initiates, what genetic material moves, whether there's recombination after transfer, what role recombination plays in adaptation, and the differences in offspring production. End by discussing whether the metaphor has helped or hindered scientific understanding of bacterial evolution.

**What to do with the output:** This is one of those teaching analogies that needs careful unpacking. The mechanisms differ enough that the analogy can confuse if applied too literally.

### Transposons

A different mechanism of moving DNA around: **transposons** are pieces of DNA that can excise themselves from one location and insert themselves at another, within the same cell. Some transposons carry extra genes — antibiotic resistance, virulence factors — and can move these between plasmids and the chromosome. **Composite transposons** carry one or more genes between two flanking insertion sequences and can jump as a unit.

Transposons matter because they can pick up resistance genes from one plasmid and deposit them on another, accelerating the spread of resistance. The genes encoding extended-spectrum beta-lactamases (ESBLs) — enzymes that destroy a broad range of beta-lactam antibiotics — are commonly transposon-borne, which is part of why ESBLs spread so rapidly through clinical settings.

## Gene regulation: the operon

Bacteria do not constitutively express all their genes. They turn genes on and off in response to environmental signals. The basic unit of bacterial gene regulation is the **operon** — a cluster of genes transcribed together as a single mRNA, controlled by a single promoter and a single regulatory element.

### Inducible operons: the lac operon

The classic example is the **lac operon** of *E. coli*, worked out by François Jacob and Jacques Monod in 1961. The operon encodes three genes for lactose metabolism: lacZ (β-galactosidase, which hydrolyzes lactose), lacY (lactose permease, which transports lactose into the cell), and lacA (a transacetylase whose function is still incompletely understood).

When lactose is absent, a regulatory protein called the **lac repressor** binds to a sequence near the promoter and blocks transcription. The operon is off. When lactose is present, a derivative of lactose (allolactose) binds the repressor, changing its shape so it can no longer bind DNA. Transcription proceeds. The operon is on.

The system makes sense economically: the cell only synthesizes the lactose-metabolism machinery when lactose is available to metabolize. The cell saves the substantial cost of making three enzymes when they would have nothing to do.

The lac operon has an additional layer: a positive regulator called **CAP** (catabolite activator protein) binds upstream of the promoter when glucose is *low*. CAP-bound DNA recruits RNA polymerase more effectively. So the lac operon is fully on only when glucose is low AND lactose is high — when lactose is the only available carbon source. If glucose is high, the cell uses glucose preferentially and the lac operon stays mostly off even with lactose present. This is **catabolite repression** — the cell's way of prioritizing its preferred carbon source.

The Jacob-Monod operon model won them the Nobel Prize in 1965 and established the framework for thinking about gene regulation that the field still uses. [^2]

### Repressible operons: the trp operon

The trp operon encodes enzymes for tryptophan biosynthesis. The logic is reversed: the operon should be on when tryptophan is *needed* (low intracellular tryptophan) and off when it isn't (high tryptophan).

The mechanism: when tryptophan is present, it binds to a regulatory protein (trp repressor) and *activates* it. The activated repressor binds the operator and blocks transcription. When tryptophan is absent, the repressor is inactive, and transcription proceeds.

The contrast is informative. The lac operon's repressor is active by default and inactivated by lactose. The trp operon's repressor is inactive by default and activated by tryptophan. The same molecular logic, configured differently for opposite outcomes.

### Other regulatory mechanisms

Beyond operons, bacteria use:

- **Sigma factors**: different sigma factors recognize different promoter sequences. Switching sigma factors can turn on different sets of genes — heat shock response, sporulation, stationary phase response.
- **Two-component systems**: a sensor protein in the membrane detects an environmental signal and phosphorylates a response regulator inside the cell, which then activates or represses transcription. *Bordetella pertussis* uses a two-component system to switch between virulent and avirulent states.
- **Riboswitches**: regions of mRNA that bind small molecules and change their structure, affecting translation or transcription termination. The cell uses the metabolite itself as a regulatory signal, without needing a protein intermediary.
- **Quorum sensing**: the cell-density-dependent regulation we mentioned in Chapter 9, mediated by secreted signal molecules.

The combinatorial logic of these systems lets bacteria regulate gene expression in response to many different environmental conditions. It is one of the things that makes bacteria so adaptable.

## What the chapter is really about

Microbial genetics is faster than vertebrate genetics because microbes have three things vertebrates do not: short generation times, large population sizes, and horizontal gene transfer. A population of *E. coli* can evolve as much in a week as a vertebrate population can evolve in a million years.

This is not metaphor. Antibiotic resistance is a literal example. Penicillin entered clinical use in 1943. Penicillin-resistant *Staphylococcus aureus* was detected in 1944. Methicillin was introduced in 1959. Methicillin-resistant *S. aureus* (MRSA) was detected in 1960. Each new antibiotic has been followed within a few years by widespread resistance. The resistance does not have to evolve from scratch in the relevant pathogen; it can be transferred from another bacterium that already has it, via plasmids, phages, or naked DNA.

The honest conclusion is that bacterial populations evolve as fast as we apply selective pressure to them. The mechanisms that make this possible — the replication accuracy that produces just enough mutation, the repair systems that prevent too much, the horizontal transfer systems that share innovations across species — are not separate topics. They are pieces of the same evolutionary engine.

When we get to antibiotic resistance in Chapter 14, you will see the engine at work. The mechanisms in this chapter are the framework. The clinical consequences are what the rest of the book is about.

## Still puzzling

I do not fully understand why horizontal gene transfer happens at the rates it does. Conjugation has obvious benefits to the recipient (acquires new capabilities). The benefit to the donor is less obvious — the donor invests substantial energy in conjugation machinery and gives away a copy of its plasmid. One hypothesis is that the conjugation machinery is essentially a parasitic system run by the plasmid itself, which "wants" to spread to new hosts and uses the donor cell as a vehicle. Another is that donor and recipient eventually exchange genes both ways, producing a long-term mutual benefit. The selfish-plasmid view has more support, but the picture is incomplete.

## What would change my mind

The picture I have given of horizontal gene transfer as a major driver of bacterial evolution rests heavily on genome comparisons that infer transfer events from sequence patterns. If those inference methods turn out to systematically overestimate transfer rates, the picture would shift. As of this writing, genome-comparison data, direct laboratory demonstration of transfer, and ecological studies of plasmid spread all converge on the importance of HGT, so the picture seems robust. But the field's models of HGT rates and mechanisms are still being refined. `[verify: current estimates of HGT rates in natural bacterial populations as of 2026]`

## LLM exercises

1. **Replication fork engineering.** Ask the LLM to describe what would happen at the replication fork if helicase were inhibited. Then if topoisomerase were inhibited. Then if ligase were inhibited. The point is mechanistic — each enzyme has a specific consequence when blocked, and several antibiotics work this way.
2. **Reading the code.** Give the LLM a 30-base mRNA sequence and ask it to translate it to a 10-amino-acid peptide. Then introduce a single point mutation and ask what kind of mutation it is and what protein change it causes. Try several mutations.
3. **Tracing a resistance plasmid.** A patient develops a urinary tract infection with a multi-drug-resistant *E. coli* carrying a plasmid encoding several resistance genes. Ask the LLM to trace plausible origins for that plasmid in the gut microbiota and identify three different ways the patient might have acquired it. Evaluate plausibility.
4. **The lac operon in detail.** Ask the LLM to draw out (in text) the lac operon's behavior under all four combinations of high/low glucose and high/low lactose. Compare with the textbook treatment. Where does the LLM's explanation match, and where does it oversimplify?
5. **An organism with no horizontal gene transfer.** Ask the LLM to imagine a bacterial species that has somehow lost all capacity for horizontal gene transfer — no transformation, no transduction, no conjugation. What would constrain its evolution? Would it survive in a world of resistant competitors? The point is to clarify what HGT does for bacterial populations.

## References

[^1]: Ames, B.N., McCann, J., Yamasaki, E. "Methods for detecting carcinogens and mutagens with the Salmonella/mammalian-microsome mutagenicity test." *Mutation Research/Environmental Mutagenesis and Related Subjects* 31, no. 6 (1975): 347–363. doi:10.1016/0165-1161(75)90046-1.
[^2]: Jacob, F., Monod, J. "Genetic regulatory mechanisms in the synthesis of proteins." *Journal of Molecular Biology* 3, no. 3 (1961): 318–356. doi:10.1016/S0022-2836(61)80072-7.
---

## LLM Exercise — Chapter 11: Mechanisms of Microbial Genetics (Microbe Profile Database Project)

**Project:** Microbe Profile Database.
**What you're building this chapter:** horizontal gene transfer fields + cross-linking of resistance/virulence genes.
**Tool:** **Cowork**.

---

**The Prompt:**

```
Chapter 11 of my Microbe Database project. Chapter 11 covered
mutation (point, frameshift, silent, missense, nonsense); genetic
transfer in prokaryotes (vertical = parent-to-daughter; horizontal
= cell-to-cell), with three mechanisms — transformation (uptake of
naked DNA), transduction (bacteriophage-mediated), conjugation
(direct contact via pilus); the Lederberg-Tatum experiment.

Schema additions:
- **Horizontal_gene_transfer_mechanisms**: list (transformation /
  transduction / conjugation) where applicable.
- **Mobile_genetic_elements**: plasmids, transposons, integrons,
  bacteriophage prophages that contribute to virulence or
  resistance.

Backfill these for existing entries. Notable:
- *Streptococcus pneumoniae* (add if not present): naturally
  competent, frequent transformation; this is the Griffith
  experiment organism.
- *E. coli*: F-plasmid conjugation classic.
- *V. cholerae*: CTXphage (filamentous bacteriophage) carries
  cholera toxin gene by transduction.
- *S. aureus*: mecA gene (methicillin resistance) on SCCmec
  cassette transferred by conjugation/transformation.
- Most clinical pathogens: have some HGT history relevant to
  resistance.

End with: which organism in your database has gained virulence
factors through HGT in a clinically-significant way? (Many — but
*V. cholerae* and *S. aureus* are the most famous teaching
examples.)
```

---

**What this produces:** HGT fields added + cross-linking begun. Database ~26-31 entries with richer connections.

**Connection to previous chapters:** Genome fields (Ch 10) + HGT fields (Ch 11) explain how virulence and resistance spread between species.

**Preview of next chapter:** Chapter 12 covers modern molecular methods (CRISPR, PCR, sequencing). Adds diagnostic-tool fields and notes which tools work best for which organisms.


---

## AI Wayback Machine

**Esther Lederberg** was discovered lambda phage and invented replica plating in 1952 — the technique foundational to bacterial genetics.

**Run this:**

```
Who is Esther Lederberg, and how does their work connect to microbial genetic mechanisms we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Esther Lederberg"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Esther Lederberg's ideas to a contemporary microbiology problem.
- Add a constraint: "Answer including criticisms or limits of Esther Lederberg's framework."

What changes? What gets better? What gets worse?
