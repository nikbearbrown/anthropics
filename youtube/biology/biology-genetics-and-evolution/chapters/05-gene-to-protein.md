# Chapter 5 — From Gene to Protein: Transcription and Translation


## TL;DR

- The ribosome does not care where the mRNA came from.
- The chapter moves through What Crick actually said, Transcription — the disposable copy, Finding the gene, Template versus coding strand, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The ribosome does not care where the mRNA came from.*

---

December 18, 2020. A nurse loads 0.3 mL of clear liquid into a syringe. Inside the liquid, wrapped in a lipid coat the size of a small virus, is roughly 30 micrograms of synthetic single-stranded RNA — about 4,300 nucleotides long. It codes for a protein the recipient has never made, from a virus the recipient has never encountered. The syringe goes into a deltoid muscle. The lipid coat fuses with cell membranes. The RNA spills into the cytoplasm. And then the recipient's own ribosomes find it, locate the AUG start codon, and begin reading it. Codon by codon. Three nucleotides at a time.

The vaccine works because the ribosome does not know the mRNA is foreign. The code in the synthetic transcript is the same code the ribosome was already using. AUG still means start. GCC still means alanine. UAA still means stop. The same machinery that built the recipient's actin and cytochrome and albumin now builds spike protein, without modification, without retraining, without knowing the difference.

That is the claim this chapter is built around. The genetic code is *universal* — not in a loose sense, but in the engineering sense: a protein-coding sequence from a virus, a bacterium, a human, or a synthesizer is readable by the same machinery. The universality is what made recombinant human insulin in *E. coli* possible in 1982. It is what made mRNA vaccines architecturally possible in 2020. It is also what makes a single A→T mutation in one β-globin gene catastrophic — because the same machinery that reads the healthy gene reads the mutated one, and produces a protein with one wrong amino acid, and that one wrong amino acid deforms a red blood cell and causes a pain crisis.

The question to hold: *how does a sequence of nucleotides become a sequence of amino acids?* The answer has two steps, each run by a molecular machine.

---

## What Crick actually said

The phrase "central dogma" is Francis Crick's, from a 1958 lecture. He later said he had not really known what "dogma" meant when he chose the word — he had used it the way a physicist might say "principle." The choice has confused students ever since.

Here is what Crick actually claimed. Once sequential information has passed into protein, it cannot get out again. Information flows from nucleic acid to nucleic acid freely — DNA to DNA in replication, DNA to RNA in transcription, RNA to DNA in retroviruses. It flows from nucleic acid to protein in translation. It does *not* flow from protein back to nucleic acid. There is no mechanism by which an amino acid sequence can be reverse-transcribed into DNA.

Note what this does not claim. It does not say information only ever flows in the direction DNA → RNA → protein. Reverse transcription — RNA to DNA — is allowed. Howard Temin and David Baltimore demonstrated reverse transcriptase in 1970 and shared the 1975 Nobel for it. RNA to DNA does not violate the central dogma. Protein to RNA would. Nobody has ever observed protein to RNA.

Prions sometimes get cited as an exception, but prion propagation is conformational — a misfolded protein templates its fold onto other proteins of the same type. The amino acid sequence does not change. The *fold* propagates, not the sequence. Crick's claim, which is a claim about sequence information, survives.

The reason to start here is that everything in this chapter — RNA polymerase, the ribosome, tRNAs, peptide bonds — only earns its place if the information flow it implements is actually what living systems do. The machinery is the substrate on which Crick's claim turns out to be true.

---

## Transcription — the disposable copy

Transcription is the process by which RNA polymerase uses one strand of DNA as a template to synthesize a complementary single-stranded RNA. The output is chemically similar to DNA but with three differences: the sugar is ribose (with a 2'-OH that deoxyribose lacks), uracil replaces thymine (same pairing with A, one less methyl group), and the molecule is single-stranded.

Why make a copy at all? Three reasons, each mechanically sound.

First, protection. DNA is the archive. Threading it through a ribosome thousands of times a day would tear it apart. The cell instead makes a disposable transcript, lets the ribosomes manhandle the transcript, and degrades it when it has served its purpose. The original stays in the nucleus, touched only by polymerases.

Second, multiplication. One gene can be transcribed into many mRNA copies simultaneously. Each mRNA copy can be translated by many ribosomes simultaneously — the structure of multiple ribosomes on one mRNA is called a polysome. One gene, dozens of mRNAs, hundreds of ribosomes. If ribosomes had to read DNA directly, only one could occupy each gene at a time.

Third, regulation. Every step in the path — making the transcript, processing it, exporting it, translating it, degrading it — is a control point. A cell that needs more protein can transcribe faster, translate faster, or degrade slower. A one-step DNA-to-protein system has one control point. The two-step system has at least five.

RNA polymerase reads the template strand 3'→5' and synthesizes RNA 5'→3', adding ribonucleoside triphosphates to the growing 3' end. The chemistry is the same as DNA polymerase: the 3'-OH of the growing chain attacks the α-phosphate of the incoming NTP; pyrophosphate leaves; a phosphodiester bond forms.

One critical difference from DNA polymerase: RNA polymerase can initiate. It can start a chain from scratch on a single-stranded template, using just two NTPs to make the first bond. DNA polymerase cannot initiate — it can only extend an existing chain with a free 3'-OH. This is why the cell uses RNA primers during DNA replication: primase, an RNA polymerase, starts the chain; DNA polymerase extends it. The ability to initiate is what makes RNA polymerase the right tool for transcription.

RNA polymerase is also less accurate than DNA polymerase — roughly one error per 10⁴ to 10⁵ nucleotides, versus one per ~10⁷ for the post-proofreading DNA polymerase. This is acceptable because transcripts are disposable. If one mRNA in a thousand carries an error, the other 999 produce correct protein. The fidelity that DNA replication requires — to preserve the archive across a lifetime — is not the fidelity transcription requires.

### Finding the gene

In bacteria, RNA polymerase holoenzyme (the core enzyme plus a sigma factor) scans DNA looking for a promoter. Bacterial promoters have two conserved sequence blocks: the **-10 box** (consensus **TATAAT**) and the **-35 box** (consensus **TTGACA**), located approximately 10 and 35 base pairs upstream of the transcription start site. Sigma factor recognizes these two elements. When holoenzyme finds them separated by the right distance (~17 bp), it clamps down, melts about 12–14 base pairs of DNA around the start site, and begins synthesizing.

Different sigma factors recognize different promoter sequences — this is how bacteria express different gene sets under different conditions. *E. coli* has seven sigma factors. σ⁷⁰ handles normal growth genes; σ³² directs heat-shock chaperones; σ⁵⁴ handles nitrogen starvation. Swapping sigma factor swaps which genes get transcribed.

In eukaryotes, RNA polymerase II — the enzyme that transcribes all protein-coding genes — does not bind promoters alone. A sequence of general transcription factors assembles first, and Pol II joins last. TFIID binds the TATA box (~25-35 bp upstream of the start site) and bends the DNA roughly 90°. TFIIA and TFIIB stabilize TFIID. TFIIF brings in Pol II. TFIIE and TFIIH join last — TFIIH melts the DNA and phosphorylates Pol II's carboxy-terminal domain to release it into elongation. The whole assembly is called the pre-initiation complex, and it is enormous — well over a megadalton of protein. Why the elaboration? Because each component is a potential regulatory target. The complexity is the price of fine-grained control.

Once elongating, RNA polymerase advances at roughly 50 nucleotides per second in bacteria, 25–50 in eukaryotes when actively moving (eukaryotic Pol II spends a lot of time paused). The polymerase maintains a transcription bubble of ~12–14 melted base pairs, moving with it. The nascent RNA is peeled off the back.

### Template versus coding strand

One vocabulary item that students confuse forever if it is not pinned down on first encounter. A gene's DNA is double-stranded. The **template strand** (antisense strand) is what RNA polymerase actually reads, 3'→5'. The **coding strand** (sense strand) is the strand whose sequence *matches* the mRNA — same letters, T instead of U.

When geneticists write a gene's sequence, they conventionally write the coding strand, 5'→3'. The mRNA sequence is identical to the coding strand with U replacing T. The template strand is the complement of both. The sickle-cell mutation is written as an A→T change on the *coding strand*. On the template strand it is T→A. On the mRNA it is A→U. Same mutation, three different notations. Pin this down now.

---

## mRNA processing — three modifications eukaryotes cannot skip

A bacterial mRNA emerges from RNA polymerase ready to translate — ribosomes attach while it is still being transcribed, sometimes before the 3' end has been synthesized. A eukaryotic mRNA is born in the nucleus and must reach the cytoplasm. Three processing steps prepare it.

**The 5' cap.** About 20–30 nucleotides into transcription, before Pol II has even cleared the promoter region, a 7-methylguanosine (m⁷G) is attached to the 5' end through an unusual 5'–5' triphosphate linkage — the guanosine is added backwards, head-to-head, unlike the normal phosphodiester backbone. Three enzymes carry out the reaction, all of them docked onto the phosphorylated CTD of Pol II so they can find the nascent RNA as soon as it emerges. The cap does three things: it protects the mRNA from 5'→3' exonucleases, marks the transcript for nuclear export, and serves as the ribosome landing pad in the cytoplasm — cap-recognition proteins recruit the small ribosomal subunit, which then scans downstream for the start codon.

**The 3' poly(A) tail.** As Pol II transcribes through the polyadenylation signal (**AAUAAA**) in the transcript, a cleavage complex cuts the RNA 10–30 nucleotides downstream. Pol II keeps transcribing briefly before being dislodged by the "torpedo" — an exonuclease that chases the polymerase down, chewing the leftover RNA as it goes. The newly cut transcript's 3' end gets ~200 adenines added by poly(A) polymerase — *without* a template. This non-templated addition is one of the rare reactions in nucleic acid biology where the enzyme just adds its preferred base repeatedly. The tail protects against 3'→5' exonucleases and, via proteins that bridge the tail-binding complex to the cap-binding complex, helps circularize the mRNA into a closed loop that promotes ribosome re-initiation.

**Splicing.** This is the strangest part of eukaryotic mRNA biology. Most eukaryotic genes are interrupted. The protein-coding sequence is broken into segments — exons — separated by non-coding stretches — introns — that must be physically cut out before the mRNA can be translated. The human β-globin gene has 3 exons and 2 introns; the pre-mRNA is ~1,600 nucleotides, but the mature mRNA is ~620 nucleotides. The introns are simply discarded. Many genes are far more intron-heavy: dystrophin has 79 exons and 78 introns, with introns accounting for over 99% of the gene's 2.4 million base pairs.

The machine that does splicing is the **spliceosome** — a huge ribonucleoprotein assembly built from five snRNPs (U1, U2, U4, U5, U6, each containing a small nuclear RNA plus proteins). The chemistry is elegant. Every intron has three landmarks: a **5' splice site** starting with GU; a **3' splice site** ending with AG; and a **branch point adenosine** 20–50 nucleotides upstream of the 3' end. Splicing happens in two transesterification steps, each breaking one phosphodiester bond and forming a new one simultaneously — no net energy input required.

In step 1, the 2'-OH of the branch-point adenosine attacks the 5' splice site, releasing the upstream exon and forming a lariat — the intron loops back on itself in a 2'–5' linkage. In step 2, the free 3'-OH of the upstream exon attacks the 3' splice site, joining the two exons and releasing the intron lariat, which is then degraded.

That 2'-OH of ribose — the chemical feature that makes RNA less stable than DNA — is the nucleophile that makes splicing possible. The same functional group that makes RNA disposable makes it catalytic.

Now the kicker: the cell does not always splice the same way. Many genes have **alternative splice sites** — multiple choices of which exons to include and which to skip. Different choices produce different mRNAs from the same pre-mRNA, encoding different proteins. About 95% of multi-exon human genes undergo alternative splicing in at least some context. The average human gene produces roughly 7 distinct protein isoforms. The human genome has ~20,000 protein-coding genes but over 100,000 distinct transcript isoforms. The *Drosophila* Dscam gene, a neural cell-surface receptor, can produce in principle 38,016 distinct protein isoforms through combinatorial alternative splicing of 95 alternative exons. One gene. More protein variants than many whole bacterial genomes have genes.

This is why the "20,000 human genes" headline from the Human Genome Project understated human complexity. We have fewer genes than expected; we have far more proteins than the gene count suggests.

---

## The genetic code — 64 codons, 20 amino acids, four billion years without a major edit

The ribosome reads mRNA three nucleotides at a time. Each three-nucleotide unit is a codon. With four possible bases at each of three positions: 4³ = 64 possible codons. With 20 amino acids to specify plus stop signals, 64 is more than enough. The mapping from codon to amino acid is the genetic code.

Five properties of the code are worth pinning down explicitly.

*Triplet.* Each codon is exactly three nucleotides. This was established by Crick, Brenner, and collaborators in 1961 using frameshift mutations in T4 phage — adding one base produced a defective protein, adding two produced a different defective protein, adding three produced a nearly functional one, demonstrating that the reading frame restores when three are added. The triplet result was inferred before any codon's meaning was known.

*Non-overlapping.* Once the ribosome starts at AUG, it reads codons sequentially, three bases at a time, with no overlap. Each base is part of exactly one codon. This is why frameshift mutations are catastrophic — inserting or deleting a single base shifts the reading frame for every codon downstream.

*Degenerate.* Most amino acids are specified by more than one codon. Methionine and tryptophan have single codons; serine, leucine, and arginine each have six. Synonymous codons typically differ at the **third position** — UCU, UCC, UCA, UCG all code for serine. A mutation at the third base of a codon is often silent. The code is shaped to absorb third-position mutations.

*Universal.* The same codon means the same amino acid in *E. coli*, in a tulip, in a shark, in you. Exceptions exist in mitochondria (UGA codes for tryptophan in vertebrate mitochondria, not stop) and a few unusual single-celled organisms. But the standard code holds across nearly all life. Recombinant insulin in bacteria and mRNA vaccines in human cells work *only* because the code is the same.

*Frozen.* Crick proposed in 1968 that the code is universal because any change would simultaneously break every protein in the cell. To swap one codon's meaning, you would need to change every gene that uses it, every tRNA that reads it, every aminoacyl-tRNA synthetase that charges those tRNAs — all at once, without killing the organism. There is no path through fitness space from one code to a slightly different one. The system is locked in by its own consistency.

### Why ~32 tRNAs suffice for 61 codons

A tRNA is a small RNA molecule (~76 nucleotides) folded into a cloverleaf shape — charged at one end with a specific amino acid, presenting a three-nucleotide anticodon at the other end. The codon-anticodon pairing is what connects the sequence of the mRNA to the sequence of the protein. tRNAs are the adapters.

Sixty-one sense codons. You might expect 61 tRNAs. Most organisms have closer to 32. Crick's wobble hypothesis from 1966 explains why. The first two positions of the codon pair with the anticodon by strict Watson-Crick rules. The third position is different — the geometry at this position is slightly relaxed, allowing non-standard pairings. A U at the anticodon's wobble position can pair with A *or* G at the codon's third position. A G at the wobble position can pair with U *or* C. An inosine (a modified base produced by deamination of adenosine in some tRNAs) at the wobble position can pair with U, C, *or* A. One tRNA with inosine in its anticodon wobble position can read three different codons. The code's third-position redundancy and the wobble mechanism are the same phenomenon seen from two angles.

---

## Translation — three steps, repeated

The ribosome is the largest, most conserved molecular machine in biology. It is roughly half RNA by mass — and the RNA half is doing the chemistry.

The bacterial ribosome (70S) has two subunits. The small subunit (30S) contains 16S rRNA plus ~21 proteins; it reads the mRNA codons. The large subunit (50S) contains 23S rRNA, 5S rRNA, and ~33 proteins; it catalyzes peptide bond formation. The eukaryotic ribosome (80S) has corresponding 40S and 60S subunits. Both architectures share a deeply conserved catalytic core. That conservation will matter when we reach antibiotics.

The most important single fact about the ribosome: **the active site that catalyzes every peptide bond in every protein you have ever made is RNA, not protein.** The peptidyl transferase center — at which every amino acid is joined to the growing chain — is in the 23S rRNA of the large subunit. The closest protein residue to the active site is ~18 Å away, far too distant to participate in catalysis. The structural proof came in 2000 with the atomic-resolution crystal structures of the ribosome solved by Thomas Steitz, Ada Yonath, and Venki Ramakrishnan, who shared the 2009 Nobel in Chemistry. The ribosome is a **ribozyme** — the largest known. Every peptide bond in your body was formed by a piece of RNA.

This is not merely a curiosity. It is the strongest evidence for the RNA world hypothesis — the idea that early life was based on RNA molecules that could both store information and catalyze reactions, before protein enzymes evolved. If proteins were required to make proteins, the origin of life has a chicken-and-egg problem. The ribosome's RNA core shows RNA *can* make proteins, which means RNA could have been both the original information molecule and the original catalyst. The ribosome is, in effect, a four-billion-year-old fossil of the world that preceded proteins.

The ribosome has three tRNA-binding sites: the **A site** (aminoacyl) where the next tRNA arrives; the **P site** (peptidyl) where the tRNA carrying the growing chain sits; the **E site** (exit) where an empty tRNA briefly dwells before leaving. The mRNA threads through a channel in the small subunit, with the codons in the A and P sites exposed for pairing.

### One elongation cycle, in order

**Step 1 — A-site entry.** A charged tRNA, complexed with elongation factor EF-Tu and GTP, diffuses into the A site. The anticodon is tested against the exposed codon. If the match is correct (strict Watson-Crick at the first two positions, wobble tolerated at the third), the tRNA fits cleanly; EF-Tu hydrolyzes its GTP and releases the tRNA into position. If the match is incorrect, the tRNA tends to fall out before GTP hydrolysis — it is rejected.

This is kinetic proofreading, a two-stage discrimination proposed by Hopfield in 1974. Initial selection is followed by a delay — GTP hydrolysis — before commitment. The delay allows a poorly-fitting tRNA to escape. The ribosome achieves a translation error rate of about one mistake per 10⁴ amino acids, far better than thermodynamics alone would predict from the energy difference between correct and incorrect codon-anticodon pairing (~3 kcal/mol, which gives an error rate of ~10⁻²). The proofreading step earns the extra two orders of magnitude.

**Step 2 — Peptide bond formation.** The A-site tRNA carries its amino acid attached via an ester bond to its 3' end. The P-site tRNA carries the growing peptide chain attached the same way. The peptidyl transferase center of the 23S rRNA holds the two tRNAs in precise geometry: the α-amino group of the A-site amino acid attacks the carbonyl carbon of the ester bond joining the peptide chain to the P-site tRNA. The peptide bond forms; the chain transfers from the P-site tRNA to the A-site tRNA; the P-site tRNA is now empty.

The ribosome provides no ATP or GTP at this step. It positions the reactants. The energy comes from the ester bond holding the amino acid to the tRNA, which was loaded using ATP back at the aminoacyl-tRNA synthetase step. The ribosome is a precise catalyst, not an energetic motor.

**Step 3 — Translocation.** Elongation factor EF-G, bound to GTP, enters the ribosome. GTP hydrolysis drives a conformational change that shifts everything by one codon: the empty P-site tRNA moves to the E site and falls off; the A-site tRNA (now carrying the elongated chain) moves to the P site; the mRNA slides through by exactly three nucleotides; the next codon is in the A site. The ribosome is back in the starting state, one amino acid longer.

Bacteria elongate at roughly 20 amino acids per second. Eukaryotes at 2–6 amino acids per second. A 300-amino-acid protein is finished in ~15 seconds in *E. coli*, ~1–2 minutes in a human cell. A single mRNA molecule, with a dozen ribosomes on it in a polysome, produces a dozen copies of the protein in that time.

### Termination

When the ribosome reaches a stop codon (UAA, UAG, or UGA) in the A site, no tRNA anticodon matches it. Instead, a release factor protein occupies the A site and triggers hydrolysis of the ester bond between the peptide chain and the P-site tRNA. Water attacks the bond instead of an amino group. The chain is released. The ribosome dissociates. The mRNA is either translated again or degraded.

---

## One base, one disease — from DNA to vaso-occlusion

The chapter's mechanistic spine is the sickle-cell mutation. It is the textbook case because it is clean: one base change → one wrong amino acid → one protein defect → one clinical syndrome. Most disease genetics is messier. This one is pure.

Adult hemoglobin is a tetramer of two α-globin chains and two β-globin chains, each wrapped around a heme group that binds oxygen. Codon 6 of the wild-type β-globin gene, written on the coding strand:

$$5'\text{-...GAG...-}3'$$

GAG codes for **glutamate (Glu)** — negatively charged, hydrophilic. The sickle allele carries a single A→T change at the second position of this codon:

$$5'\text{-...GTG...-}3'$$

GTG codes for **valine (Val)** — uncharged, hydrophobic.

Walk the chain. On the template strand, the corresponding change is T→A. RNA polymerase reads the template 3'→5' and produces mRNA 5'→3'. Wild-type mRNA at codon 6: GAG. Sickle mRNA at codon 6: GUG. (U replaces T.) The transcript gets capped, polyadenylated, and spliced — the mutation is in exon 1, not near any splice site, so processing is unaffected. The mature mRNA exports to the cytoplasm.

A ribosome scans from the 5' cap, finds the AUG start codon, and begins elongating. At codon 6, the A site reads GUG instead of GAG. EF-Tu delivers Val-tRNA instead of Glu-tRNA. The peptidyl transferase center of the 23S rRNA — the ribozyme — forms a peptide bond between valine and the growing chain instead of glutamate. The ribosome reads the remaining 140 codons without incident. The finished protein is 146 amino acids long and identical to wild-type at every position except position 6: valine instead of glutamate.

Now the chemistry. Glutamate's side chain ends in a carboxylate group — it is negatively charged at physiological pH and comfortable on the protein's surface, facing water. Valine's side chain is a branched alkyl group — hydrophobic, preferring to face the protein's interior, away from water. Substituting valine for glutamate at position 6 places a hydrophobic patch on the surface of β-globin, where a negative charge used to be. A hemoglobin tetramer with two mutant β-chains has two hydrophobic patches, symmetrically placed.

Hemoglobin in red cells exists in two states: the R state (oxygen-bound, relaxed) and the T state (oxygen-released, tense). When oxygen tension falls — in active capillaries, in the spleen, anywhere tissue is consuming oxygen — hemoglobin shifts toward the T state. The hydrophobic patch on HbS β-chains fits into a complementary pocket on a *different* HbS tetramer, but only when that adjacent molecule is in the T state. One HbS docks onto another; the bound molecule exposes its own pocket; the next HbS binds. The result is a long polymer — stiff fibers several micrometers long that distort the red cell from its normal flexible biconcave shape into a rigid sickle.

When the red cell returns to the lungs, the fibers depolymerize and HbS returns to solution. But every sickling-unsickling cycle damages the cell membrane. After enough cycles, the cell loses the ability to recover and becomes irreversibly sickled.

Three downstream consequences. First, hemolytic anemia: sickled cells survive only 10–20 days instead of the normal 120, and the bone marrow cannot replace them fast enough. Second, vaso-occlusion: rigid, angular sickle cells jam in capillaries and small venules, blocking blood flow and causing ischemia downstream — the pain crises that are the disease's signature, and the repeated organ damage that accumulates over years. Third, chronic end-organ damage: splenic infarction (the spleen auto-infarcts by adolescence in many patients, leaving them at high risk for encapsulated bacterial infections), pulmonary infarction, stroke, renal insufficiency.

Every step in that chain is traceable. Every step has a named mechanism. Every step is, in principle, a site for therapeutic intervention — and indeed, modern sickle cell therapies target different links. Hydroxyurea reactivates fetal hemoglobin, diluting the HbS pool. Voxelotor stabilizes the R state of HbS, reducing polymerization. Gene therapies edit the DNA — either restoring the wild-type codon or disrupting BCL11A to reactivate fetal hemoglobin. The chain from base to clinic is what makes targeted therapy thinkable.

One more layer. Carriers — heterozygotes with one β^A and one β^S allele — are largely asymptomatic because ~60% of their hemoglobin is normal HbA, which dilutes the HbS enough that polymerization rarely occurs under normal oxygen conditions. And heterozygotes are partially protected against severe malaria: *Plasmodium falciparum* has more difficulty completing its intracellular life cycle in HbS-containing red cells, and infected heterozygote cells are cleared more rapidly by the spleen. This heterozygote advantage keeps the allele at frequencies of 5–15% in populations from malarial regions, despite its devastating homozygous effect. The same A→T change that is catastrophic in two copies is *adaptive* in one copy in the right environment. That is why the allele has not been selected out of the human gene pool. Chapter 9 will formalize this as a worked example of balancing selection.

---

## Antibiotics — exploiting the 70S/80S difference

Bacterial ribosomes are 70S. Human ribosomes are 80S. The catalytic core is conserved — which is why the antibiotic target exists — but the surrounding architecture is different enough that small molecules can bind one and not the other. Most of the clinically important translation-targeting antibiotics exploit exactly this gap.

**Aminoglycosides** (streptomycin, gentamicin) bind the 30S subunit at the decoding center of the 16S rRNA. They distort the A-site geometry so that incorrect tRNAs are accepted as correct. The ribosome misreads codons; the resulting proteins are full of errors; the bacterium dies from accumulated misfolded membrane proteins. Side effects include ototoxicity — aminoglycosides also bind to mitochondrial 12S rRNA in hair cells of the inner ear, because mitochondria are evolutionary descendants of α-proteobacteria and still have ribosome architecture recognizable as bacterial.

**Tetracyclines** (doxycycline, tigecycline) also bind the 30S subunit at the A site, but by blocking tRNA entry rather than promoting misreading. Elongation halts because the next tRNA cannot arrive. Bacteriostatic rather than bactericidal.

**Chloramphenicol** binds the 50S subunit at the peptidyl transferase center, occupying the A-site amino acid pocket and preventing the attacking amino group of the incoming amino acid from reaching the carbonyl of the P-site peptide chain. Peptide bond formation is directly blocked. Bacteriostatic, with a rare but severe side effect of aplastic anemia — chloramphenicol affects mitochondrial ribosomes at high doses, and bone marrow cells with rapid turnover are sensitive.

**Macrolides** (erythromycin, azithromycin) bind the 50S subunit in the peptide exit tunnel, the channel through which the nascent chain leaves the ribosome. After ~6–8 amino acids, the growing chain bumps into the drug and cannot advance. Elongation aborts. Bacteriostatic.

The pattern: every one of these drugs binds rRNA, not ribosomal protein. This is expected — the catalytic sites and structural channels of the ribosome are RNA, and RNA surfaces have distinct geometries that small molecules can recognize. The protein scaffolding around those RNA surfaces differs between 70S and 80S, providing the selectivity that makes the drugs medically useful.

---

## The code as engineering substrate

The genetic code is universal. Here is what you can build with that fact.

In 1978, a team at Genentech synthesized the human insulin gene chemically — they wrote it from scratch using a DNA synthesizer, back-translating from the known amino acid sequence of human insulin. They inserted the synthetic gene into a plasmid, transformed the plasmid into *E. coli*, and the bacteria produced human insulin. One modification: the gene was rewritten using codons that *E. coli* prefers, because rare codons in bacteria are translated slowly and can stall ribosomes. A Shine-Dalgarno sequence was added upstream, because bacterial ribosomes find the start codon by base-pairing with the 16S rRNA, not by scanning from a cap as eukaryotic ribosomes do. Eli Lilly brought Humulin to market in 1982 — the first FDA-approved recombinant DNA product. The *E. coli* ribosome read AUG as Met, GCC as Ala, GAG as Glu, exactly as the human ribosome does. The protein was identical.

Now carry the same logic one step further. Instead of putting a gene into a cell and letting it transcribe and translate, put the mRNA directly into the cell. Skip transcription entirely. The cell's ribosomes do the rest.

The Pfizer-BioNTech and Moderna COVID-19 vaccines work this way. The mRNA encodes a proline-stabilized version of the SARS-CoV-2 spike protein — two prolines lock the protein in the pre-fusion conformation that presents the best immune target. The sequence is codon-optimized for human translation. Every uridine is replaced with N1-methylpseudouridine, a modified base that pairs with adenosine identically but evades the innate immune sensors (TLR3, TLR7, RIG-I) that would otherwise recognize the synthetic RNA as viral and destroy it before the ribosome could read it. The mRNA has a synthetic 5' cap and a poly(A) tail. It is wrapped in lipid nanoparticles that fuse with cell membranes and deliver the contents to the cytoplasm.

The mRNA enters the cytoplasm. The ribosome finds the cap, scans to the AUG, and reads the spike protein into existence. Codon by codon. Three nucleotides at a time. By the same machinery that builds actin and albumin. The vaccine is read because the genetic code — the dictionary the ribosome uses — is the same dictionary the synthetic mRNA was written in.

The mRNA is degraded within hours to days by normal cellular ribonucleases. It never enters the nucleus. It cannot integrate into DNA. The protein is produced, presented to the immune system, and the synthetic protein is degraded on its normal schedule. The modified pseudouridine stays modified — it does not convert back to uridine inside the cell.

The architecture of modern molecular medicine is the central dogma, used as an engineering specification. DNA encodes proteins through a universal code. Transcription writes the message. Translation reads it. The message is interoperable across all of life. That interoperability is not philosophy. It is the reason a nurse in 2020 could inject synthetic RNA into a deltoid muscle and have the patient's own ribosomes build protein from a pathogen the patient had never encountered — because the ribosome does not care where the mRNA came from.

---

*The next chapter asks how the cell decides which genes to transcribe and when. The machinery we have built here — RNA polymerase, the spliceosome, the ribosome — runs the same in every cell of your body. Every cell has the same genome. What differs between a liver cell and a neuron is which genes are on. The control of transcription is the logic of cell identity, development, and response to the environment. That is Chapter 6.*
