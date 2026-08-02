# Chapter 4 — DNA Structure, Replication, and Repair
*Why accuracy is not a property of the molecule.*

---

A human cell copies three billion base pairs every time it divides and gets it almost right.

The "almost" matters in both directions. If copying were perfect, evolution would stop — natural selection requires variation, and variation requires mistakes. If copying were sloppy by a factor of a thousand, no human would survive infancy. The actual error rate — about one mistake per billion base pairs per replication — sits in a narrow range where cells stay viable across thousands of divisions, populations stay variable enough to evolve, and cancer is possible but rare. That number is not a property of DNA the molecule. It is the product of three nested error-correction systems acting on the same template, layered on top of each other over three billion years of evolution. Understanding this chapter means understanding how those layers work, what disease appears when each one is removed, and why the architecture is the way it is.

We will get there by the same route biology had to take — starting with what DNA actually is.

---

## How we found out what genes are made of

Before 1944, most biochemists thought proteins carried genetic information. The reasoning was almost defensible. Proteins are built from twenty amino acids; DNA is built from four nucleotides. Information density seemed to favor the more complex alphabet. DNA looked like a structural scaffold. The vote was for protein.

The vote was wrong, and it took three experiments spread across twenty-four years to overturn it.

The first was **Frederick Griffith's** in 1928. *Streptococcus pneumoniae* comes in two forms: a smooth virulent strain (S) and a rough avirulent strain (R). Inject live S into a mouse — the mouse dies. Inject live R — the mouse lives. Inject heat-killed S — the mouse lives; dead bacteria are dead. Now mix heat-killed S with live R and inject the mixture. The mouse dies. From the dead mouse, Griffith recovered live S bacteria. Something had moved from the dead smooth cells into the living rough cells and transformed their phenotype. He called it the "transforming principle" and did not know what it was.

The second was **Avery, MacLeod, and McCarty's** in 1944. They spent a decade purifying the transforming principle and asking, chemically, what it was. Their strategy was elimination by enzyme. Treat the extract with proteases — transformation still works. Treat it with RNase — transformation still works. Treat it with DNase — transformation stops. The transforming principle was DNA. The paper landed quietly. The field needed one more blow.

The third was **Hershey and Chase's** in 1952. They worked with bacteriophage — viruses that inject something into *E. coli* and then burst the cell open with hundreds of new copies of themselves. What does the phage inject? They labeled the protein coats of one phage batch with ³⁵S and the DNA cores of another with ³²P. Each batch infected bacteria. They sheared the empty protein coats off the cells with a blender, centrifuged the bacteria into a pellet, and measured the radioactivity. ³²P went into the bacteria. ³⁵S stayed in the supernatant. The phage injected DNA, not protein. The argument was finished.

Why three experiments? Because each ruled out something the previous one had not. Griffith showed that *something* could transfer heritable information, but the something could have been protein, RNA, or DNA. Avery showed it was destroyed by DNase but skeptics argued the DNase was contaminated or DNA was merely a carrier. Hershey and Chase separated protein and DNA *during the act of transmission* and showed only DNA crossed the membrane. The standard for overturning a prevailing model is not a suggestive paper — it is a specific alternative explanation and an experiment that rules it out. That is what twenty-four years produced.

---

## The double helix — geometry enforces fidelity

In 1950, **Erwin Chargaff** measured the base composition of DNA from many organisms and found a persistent oddity: the amount of adenine always equaled the amount of thymine, and the amount of guanine always equaled the amount of cytosine, across every species he tested. The ratio A+T versus G+C varied between species, but A=T and G=C held universally. Chargaff did not know why.

In April 1953, Watson and Crick published a one-page paper in *Nature* that explained why. DNA is a right-handed double helix in which two sugar-phosphate strands run **antiparallel** and the bases pair across the interior: adenine with thymine, guanine with cytosine. The equalities Chargaff found are the equalities of complements — every A on one strand requires a T on the other, so the counts must be equal.

Their model had three sources. The first was Chargaff's rules, which demanded an explanation. The second was **Rosalind Franklin's** X-ray diffraction work, specifically Photograph 51 — taken in late 1952 by Franklin and her graduate student Raymond Gosling at King's College London — which showed the unmistakable cross-shaped diffraction pattern of a helix and permitted measurement of the helical dimensions. Watson saw the photograph through Franklin's colleague Maurice Wilkins without her permission; this is part of the history and should be said plainly. Franklin died of ovarian cancer in 1958 at 37, four years before the 1962 Nobel Prize went to Watson, Crick, and Wilkins. The third source was working out which base-pairing geometries actually fit.

Let me unpack the structure, because the geometry returns at every repair step.

A nucleotide has three parts: a phosphate group, a five-carbon sugar (deoxyribose in DNA), and a nitrogenous base. **Purines** (adenine and guanine) are two-ring molecules. **Pyrimidines** (thymine and cytosine) are one-ring molecules. Nucleotides link to each other via phosphodiester bonds between the 3'-OH of one sugar and the 5'-phosphate of the next, creating a directional chain with a 5' end and a 3' end. We read sequences 5'→3' because directionality is built into the chemistry.

<!-- → [IMAGE: A single nucleotide showing the three components (phosphate, deoxyribose sugar, nitrogenous base) with the 5' and 3' positions labeled on the sugar — then a short four-nucleotide chain showing the 3'→5' phosphodiester linkages and the resulting 5' end (free phosphate) and 3' end (free hydroxyl)] -->

Two single strands wind around each other in specific orientation: antiparallel, meaning one strand's 5'→3' direction points up the helix and the other points down. This is not optional — the hydrogen-bond geometry of A-T and G-C base pairs only works when the strands are antiparallel. Parallel strands cannot pair correctly. Antiparallelism is the single structural fact that forces every awkward feature of DNA replication. Keep it in mind.

The base-pairing rules are physically enforced by hydrogen-bond geometry. **Adenine pairs with thymine via two hydrogen bonds.** **Guanine pairs with cytosine via three.** A purine never pairs with a purine — too wide for the helix to maintain its diameter. A pyrimidine never pairs with a pyrimidine — too narrow. The specific donor-acceptor patterns mean A cannot pair with C (wrong geometry) and G cannot pair with T (wrong geometry). Four bases, two pairing rules, both enforced by physics.

<!-- → [IMAGE: Side-by-side diagrams of A-T and G-C base pairs — each showing the hydrogen bonds as dashed lines with donor/acceptor labels, the bond counts (2 for A-T, 3 for G-C), and the approximately equal width of the two pairs (~10.85 Å between sugar attachment points) — annotated to show why a purine-purine pair would be too wide and a pyrimidine-pyrimidine pair too narrow] -->

Three structural numbers matter for everything that follows. **~2 nm diameter** — uniform regardless of sequence, because every base pair is one purine plus one pyrimidine. **~10 base pairs per turn, ~3.4 nm per turn** — the bases stack on each other like coins, with the stacking interaction providing most of the helix's thermodynamic stability. **Major and minor grooves** — because the two backbones are not diametrically opposite, the spaces between them come in two sizes; proteins read DNA sequence by inserting side chains into the major groove, where A-T and G-C are chemically distinguishable without melting the helix open.

Watson and Crick ended their paper with one of the most famously understated sentences in twentieth-century biology: "It has not escaped our notice that the specific pairing we have postulated immediately suggests a possible copying mechanism for the genetic material." Here is what they meant. If every A must pair with T and every G with C, then each strand contains all the information needed to specify its complement. Separate the strands, provide free nucleotides, add an enzyme that can synthesize a new strand by reading a template — and each parental strand will direct the synthesis of a new complementary partner. You end up with two double helices, each one parental strand plus one newly synthesized strand. This is **semiconservative replication**: each original strand is conserved into a daughter duplex, paired with a fresh complement.

---

## Meselson and Stahl prove it

The Watson-Crick paper proposed the model. It did not prove it. There were two other possibilities.

**Conservative replication** would keep both parental strands together in one daughter duplex and produce an entirely new duplex alongside it — old-old plus new-new.

**Dispersive replication** would chop both strands into segments and scramble parental and new material throughout both daughter duplexes — every strand a mosaic.

In 1958, **Matthew Meselson** and **Franklin Stahl** designed what has been called "the most beautiful experiment in biology." The design is so clean it is worth reconstructing exactly.

Start with two stable isotopes of nitrogen. ¹⁴N is ordinary; ¹⁵N is slightly heavier — about 1% denser per nitrogen atom. DNA built from ¹⁵N-containing precursors is measurably denser than DNA built from ¹⁴N. **Measurably** means: spin a sample in a cesium chloride density gradient at high speed for many hours, and the two kinds of DNA settle at different depths. The density difference is small but the resolution is crisp enough to separate them cleanly.

The protocol. Grow *E. coli* for many generations in ¹⁵N medium until all DNA is fully heavy. Transfer to ¹⁴N medium. Let the cells divide. Take samples at one generation, two generations, three. Spin each. Look at the bands.

Here is what each model predicts.

**Conservative:** After one generation — two bands, heavy and light (the original parental duplex intact, and an entirely new light duplex). After two generations — the same two bands, different proportions.

**Semiconservative:** After one generation — one band, at *intermediate* density (every duplex is one heavy strand plus one new light strand, so every duplex has the same intermediate density). After two generations — two bands, one intermediate and one light, in equal amounts (the hybrid duplexes each generated one new hybrid and one fully light daughter).

**Dispersive:** After one generation — one band at intermediate density, *same as semiconservative*. But after two generations — the band gradually drifts lighter without ever splitting into two distinct bands (the parental material keeps getting diluted into new synthesis, never fully separating).

<!-- → [CHART: Three-panel diagram showing the density-gradient band patterns predicted by conservative, semiconservative, and dispersive models at generation 0, 1, and 2 — each panel shows a tube with band positions; the conservative panel shows two bands at 0 and 1; the semiconservative panel shows one intermediate band at 1 then two bands (intermediate + light) at 2; the dispersive panel shows one band gradually shifting lighter at 2 without splitting — annotated to show which observations rule out which models] -->

What Meselson and Stahl actually saw, after one generation: one band, exactly at intermediate density. Conservative ruled out. After two generations: two bands, one at intermediate density and one at fully light density, in approximately equal amounts. Dispersive ruled out. Semiconservative confirmed.

The experiment is beautiful for a specific reason: the same design discriminates among all three competing models simultaneously. One density-gradient series, one protocol, three models separated. The predictions are quantitative and specific. Vague predictions cannot be sharply falsified; sharp predictions can.

---

## The replication fork — why the lagging strand is awkward

Semiconservative replication, settled in 1958, raised a new question. *How* does it actually work? A replication fork is a moving Y-shaped junction. The parental duplex enters from one side; two daughter duplexes emerge from the other. At the cusp of the Y, the parental strands are being separated; behind the fork, two new complementary strands are being assembled.

Here is the constraint that creates all the awkwardness. DNA polymerase — the enzyme that builds new strands — can only synthesize in the **5'→3' direction**. It extends an existing chain by adding nucleotides to a free 3'-OH. It cannot run 3'→5'. But the two parental template strands run antiparallel. So one template presents itself in the right orientation (3'→5' as the fork moves), and synthesis there can proceed continuously, always extending in the direction the fork is moving. This is the **leading strand**. The other template presents itself in the wrong orientation (5'→3' as the fork moves), and synthesis there cannot keep up with the fork — the polymerase has to keep stopping, releasing, and restarting at a new primer behind the fork's motion. The result is a series of short fragments that later get stitched together. This is the **lagging strand**.

The players, in the order they act:

**Helicase** pries the two parental strands apart, hydrolyzing ATP to move. It tracks 5'→3' along the lagging-strand template, opening roughly 1,000 base pairs per second in *E. coli*.

**Single-strand binding proteins** (SSBs in bacteria; RPA in eukaryotes) coat the separated strands and prevent them from re-annealing into hairpins that would block synthesis.

**Topoisomerase** relieves the positive supercoiling that accumulates ahead of the helicase. A closed double helix cannot simply rotate when you unwind part of it — the twist has to go somewhere. Topoisomerases temporarily cut one or both strands, let the DNA rotate, and reseal. Bacterial **DNA gyrase** (a type II topoisomerase) is also the target of fluoroquinolone antibiotics — ciprofloxacin traps bacterial gyrase in its cut state and kills the bacterium, a mechanism that works because bacterial and human topoisomerases differ enough to be selectively poisoned.

**Primase** lays down a short RNA primer (~10 nucleotides) on each template. DNA polymerase cannot initiate a new chain from scratch — it needs a pre-existing 3'-OH to extend. Primase can initiate without one, so the cell uses RNA primers as starters. Why RNA and not DNA? Because the cell needs to be able to remove the primers later and recognize them as distinct from finished product. If primers were DNA, the cell would have no way to tell starter from final strand.

**DNA polymerase** extends from the RNA primer, reading the template 3'→5' and building the new strand 5'→3'. In *E. coli*, **DNA polymerase III** synthesizes at ~1,000 nucleotides per second with an intrinsic error rate of about 1 per 10⁵ bases before proofreading. In eukaryotes, **polymerase ε** handles the leading strand and **polymerase δ** handles most of the lagging strand, both slower (~50 nucleotides per second), but mammalian cells fire 30,000–50,000 replication origins simultaneously — parallelism compensating for individual speed — and replicate the full 3-billion-base-pair genome in about six hours.

**RNase H and FEN1** (or in bacteria, **DNA polymerase I**) remove the RNA primers once synthesis has proceeded past them. **DNA polymerase** fills the resulting gap. **DNA ligase** seals the final nick — without it, the new strand would be fragments held together only by base pairing to the parental strand, not covalently connected.

<!-- → [IMAGE: Diagram of a moving replication fork — the parental duplex enters from the right, helicase at the apex, SSBs coating the single strands; on the upper template (leading strand), one RNA primer at the start and continuous synthesis extending leftward with the fork; on the lower template (lagging strand), three successive RNA primers placed at intervals, with Okazaki fragments growing rightward (away from the fork) between them, RNase H removing the primers of older fragments, DNA polymerase filling gaps, ligase sealing; all players labeled] -->

On the lagging strand, the repeated primer-extend-stop-restart cycle produces what **Reiji Okazaki** and his colleagues showed in 1968: short, discontinuous pieces of new DNA, roughly 1,000–2,000 nucleotides in *E. coli* and 100–200 in eukaryotes, before they are joined into a continuous strand. These are **Okazaki fragments**.

Why does the cell tolerate this? Because the alternative is worse. A 3'→5' polymerase — which would let the lagging strand synthesize continuously in the direction of fork movement — is thermodynamically impossible. In 5'→3' synthesis, the energy driving each bond formation comes from the incoming nucleotide (the triphosphate that gets cleaved). If the polymerase makes a mistake, it can remove the misincorporated nucleotide and try again — the 3' end of the chain is still intact. In hypothetical 3'→5' synthesis, the energy is on the growing chain, and removing a misincorporated nucleotide would destroy the terminus needed for the next addition. The geometry of chemistry rules out 3'→5' polymerization. The cell pays the cost of Okazaki fragments to get high-fidelity 5'→3' synthesis on both strands. The awkwardness is the price of accuracy.

---

## Three layers of accuracy

Four numbers, in the order the cell uses them.

**Naive base pairing without an enzyme:** wrong nucleotides bind across from templates roughly once every 10² to 10³ pairings. The energetic difference between a correct A-T pair and a mismatched A-C pair is small enough that thermal noise often defeats it.

**DNA polymerase nucleotide selection:** the active site is shaped so that only a correctly paired incoming nucleotide fits cleanly. An incorrect nucleotide creates a slight distortion that slows the bond-formation rate by orders of magnitude. Error rate after this step: about **1 per 10⁵ bases**.

**Plus 3'→5' proofreading exonuclease:** the same polymerase has a second active site that cuts nucleotides off the 3' end of the growing strand. When a wrong nucleotide is incorporated, the misshapen 3' end fits poorly in the synthesis active site and is shunted to the exonuclease, which cleaves the error off. The polymerase tries again. Error rate after proofreading: about **1 per 10⁷ bases**.

**Plus post-replication mismatch repair:** a separate scanning machinery detects mismatches in newly synthesized DNA and excises them. This layer reduces the rate by another ~100-fold, to about **1 per 10⁹ to 10¹⁰ bases**.

Each layer reduces the error rate by roughly 100-fold. Three layers compounding give ~10⁶-fold reduction from naive base pairing. The accuracy is not magic. It is the product of three independent error-correction steps, each acting on the residue the previous step missed.

The human genome is about 3 × 10⁹ base pairs. A mutation rate of 10⁻⁹ per base per replication implies about **3 mutations per cell division**. Most fall in non-coding sequence and are harmless. A few will eventually hit tumor-suppressor or oncogene loci. Chapter 8 will pick up this thread. The point for now is that the mutation rate is not zero, and it is not accidental — it is engineered to be small but nonzero, and the engineering is the three layers just described.

---

## One corrected error, step by step

Let me slow down and trace a single error all the way through the correction pipeline. Everything abstract in the previous section becomes concrete here. I am using *E. coli* because the prokaryotic version is cleaner — fewer proteins, same logic.

**Setup.** A replication fork is moving at ~1,000 bp/sec. DNA polymerase III is extending the leading strand. At some position the template reads ...3'-A-5'... and the correct base to incorporate is T.

**Step 1 — Wrong nucleotide incorporated.** The polymerase incorporates dGTP instead of the correct dTTP. A G now sits across from an A — an A•G mispair. Wrong hydrogen-bonding pattern, wrong width; the daughter strand's 3' end is distorted.

**Step 2 — Proofreading.** The misshapen 3' end fits poorly in the synthesis active site. The strand's terminus is shunted to the **3'→5' exonuclease** site on the same polymerase. The misincorporated G is excised. The polymerase now has a clean 3' end and tries again, this time incorporating the correct T. Error corrected at the moment of synthesis. Error rate drops to ~10⁻⁷.

**Step 3 — Error escapes.** At some other position, a mispair slips past proofreading — this happens roughly once per hundred mispair events. The fork continues moving. The mispair is now several bases behind the polymerase, embedded in double-stranded DNA. Proofreading no longer has access.

**Step 4 — MutS recognition.** A protein called **MutS** slides along the newly replicated DNA, feeling the helix for small distortions that mispairs cause. When it finds one, it clamps down and recruits **MutL** as a scaffold. The MutS–MutL complex now sits at the lesion.

**Step 5 — The parent/daughter problem.** The mispair has one correct base (on the parental template) and one wrong base (on the daughter strand). MMR must remove the wrong one, which means it must distinguish which strand is the daughter. In *E. coli*, the answer is methylation. A maintenance methyltransferase called **Dam** adds a methyl group to every GATC sequence in the genome. After replication, the parental strand is fully methylated; the daughter strand is not yet — Dam has not had time to find and methylate it. A protein called **MutH** binds a nearby hemimethylated GATC site and cuts the *unmethylated* (daughter) strand only. The repair machinery now knows which strand to fix, and where to enter it.

In eukaryotes, methylation is not used for this purpose. Instead, eukaryotic MMR uses **nicks left in the daughter strand by ongoing replication** — the nicks between Okazaki fragments on the lagging strand, and nicks left by ribonucleotide excision on the leading strand — as the strand-discrimination signal. Different biology, same logic: find an asymmetry between parent and daughter, use the asymmetry to identify which strand to cut.

**Step 6 — Excision and resynthesis.** An exonuclease chews back from the nick through the mismatch. A single-stranded gap, several hundred to a couple of thousand nucleotides long, is left on the daughter strand. DNA polymerase III fills the gap using the parental strand as template, this time with the correct base. Ligase seals the final nick. The mispair is gone. Final error rate: ~10⁻⁹ per base per replication.

**The clinical sequel.** **Lynch syndrome** — hereditary nonpolyposis colorectal cancer — is what happens when a person inherits a defective copy of one of the human MMR genes, most commonly **MLH1** (human homolog of *E. coli* MutL) or **MSH2** (homolog of MutS). Heterozygotes have one good copy and are largely protected. But in any rapidly dividing tissue — the colon epithelium replaces its entire surface every few days — the second copy can be lost by somatic mutation, and the resulting MMR-deficient cell now accumulates mutations ~100-fold faster than its neighbors.

The fastest-mutating sequences in the genome are **microsatellites** — short tandem repeats like (CA)ₙ where replication slippage generates length changes that MMR ordinarily corrects. Without MMR, microsatellite lengths fluctuate wildly, producing the diagnostic phenotype called **microsatellite instability (MSI-high)**. About 3% of all colorectal cancers in the general population arise from Lynch-syndrome inheritance. The **2015 Nobel Prize in Chemistry** recognized Paul Modrich for working out this pathway, alongside Tomas Lindahl (base excision repair) and Aziz Sancar (nucleotide excision repair).

The mechanism that corrects one misincorporated G is the same mechanism that protects you from colorectal cancer at 35. The molecular biology and the clinical genetics are not separate stories. They are the same story at different scales.

---

## Three more pathways for damage that isn't a mispair

Mismatch repair handles errors made during replication. But DNA is also chemically attacked constantly, regardless of whether the cell is dividing. Estimates put the rate of spontaneous DNA damage at tens of thousands of events per cell per day. Three more repair pathways clean up most of this.

### Base excision repair

The smallest lesions are individual chemically modified bases. **Depurination** — a purine (A or G) spontaneously falling off its sugar, leaving an abasic site — occurs perhaps 10,000 times per cell per day. **Deamination** of cytosine to uracil — a C-G pair converted to something that reads as U-G, which on replication would become T-A — is the reason DNA uses thymine rather than uracil. If DNA used uracil, every spontaneous deamination of cytosine would be invisible. Because DNA uses thymine, any uracil in DNA is recognizable as damage. **Oxidation** of guanine to 8-oxoguanine creates a lesion that mispairs with adenine, generating G→T mutations on the next replication round.

**Base excision repair** handles these one base at a time. A family of **DNA glycosylases** — each specific for a particular damaged base — slide along the helix, flip suspect bases out into a pocket in the enzyme, and test them. If the base is a target, the glycosylase cleaves the bond between it and the sugar, leaving an abasic site. An **AP endonuclease** then cuts the backbone next to the abasic site. DNA polymerase fills in the correct nucleotide. Ligase seals the nick.

**What goes wrong when BER fails.** Mutations in the glycosylase **MUTYH** — which corrects 8-oxoG•A mispairs — cause **MUTYH-associated polyposis (MAP)**, an autosomal-recessive predisposition to colorectal cancer.

### Nucleotide excision repair

Larger lesions — ones that distort the helix — are handled by a pathway that operates on a longer length scale. The canonical example is the **thymine dimer**: adjacent thymines on the same strand fused into a covalent ring by UVB photons, creating a kink that no replicative polymerase will read accurately. Other bulky lesions include adducts formed by benzo[a]pyrene from cigarette smoke, aflatoxin from moldy peanuts, and cisplatin.

**Nucleotide excision repair** scans the genome for distortions rather than for specific chemical modifications. A complex led by **XPC** in mammals finds the aberrant geometry, recruits a larger machine that opens the helix around the lesion, makes two cuts — one on each side — and excises a single-strand patch of roughly 25–30 nucleotides containing the damage. DNA polymerase fills the gap from the undamaged opposite strand. Ligase seals.

The key NER proteins are named after the disease they cause when lost: **XPA, XPB, XPC, XPD, XPE, XPF, XPG** — all for **xeroderma pigmentosum**. The boy in Chicago who has to wear UV-blocking gloves and a face visor to walk three blocks to the clinic — the one from the opening of this chapter, who has already had two skin carcinomas removed at age four — has a loss-of-function mutation in one of these genes. Every UV photon that reaches his skin drives the thymine dimers his cells cannot repair. The dimers persist. The next time the cell divides, errors accumulate opposite the damage, mutations accumulate in tumor-suppressor genes, and skin cancers appear. Same sun. Same DNA. Different repair status. Vastly different outcome.

<!-- → [TABLE: Four repair pathways in one reference table — columns: pathway name, type of damage recognized, key recognition protein(s), excision size, disease when pathway is lost — rows: MMR (mismatched bases, MutS/MSH2, ~100–2000 nt, Lynch syndrome), BER (single modified bases, DNA glycosylases, 1 nt, MUTYH-associated polyposis), NER (bulky helix-distorting lesions, XPC, ~25–30 nt, xeroderma pigmentosum), HR (double-strand breaks S/G2, RAD51/BRCA1/BRCA2, variable, HBOC syndrome), NHEJ (double-strand breaks G1, Ku70/80, variable, chromosomal instability)] -->

### Double-strand break repair

The most dangerous lesion is a **double-strand break** — both strands of the helix severed at the same position. A DSB can be caused by ionizing radiation, certain chemicals, mechanical stress on replicating chromosomes, or, surprisingly often, by the cell deliberately cutting its own DNA (V(D)J recombination in lymphocytes; meiotic crossover; CRISPR-Cas9). A single unrepaired DSB can kill a cell. Multiple misrepaired DSBs are how chromosomal rearrangements in cancer arise.

There are two main pathways for DSB repair in mammals, with very different fidelity profiles.

**Homologous recombination** is the high-fidelity pathway, available only in S and G2 phases when a **sister chromatid** exists as an identical template. The broken ends are resected by nucleases — one strand is chewed back, leaving a long single-stranded overhang. The **RAD51** protein coats the overhang and directs it to search the genome for matching sequence — it finds the sister chromatid, invades the intact duplex there, and copies over the broken region using the sister as template. The break is repaired with no loss of information. HR requires **BRCA1** and **BRCA2** to function properly.

**Non-homologous end joining** is available throughout the cell cycle, including G1 when no sister chromatid exists. The **Ku70/Ku80** complex binds the broken ends and, together with **DNA-PKcs** and **DNA ligase IV**, ligates them back together directly, without a homologous template. The broken ends often have small chemical modifications and need to be trimmed or filled before they can be ligated; this trimming and filling introduces small insertions or deletions at the junction. NHEJ repairs the chromosome in the sense that the ends are no longer drifting — it does not necessarily preserve the original sequence. NHEJ is also how CRISPR-Cas9 editing works: Cas9 makes a targeted double-strand break, and NHEJ repairs it with a small insertion or deletion that disrupts the targeted gene.

The clinical consequence of losing HR is **hereditary breast and ovarian cancer syndrome**. Germline loss-of-function mutations in **BRCA1** or **BRCA2** leave cells dependent on NHEJ for double-strand break repair. In rapidly dividing tissues — breast and ovarian epithelium in particular — somatic loss of the second allele generates HR-deficient cells that accumulate chromosomal damage rapidly. The estimated lifetime breast cancer risk in BRCA1 carriers is around 60–72% by age 80; ovarian risk is around 40–44%.

Why the cancers cluster in breast and ovarian tissue specifically, rather than appearing uniformly across tissues, is not yet fully understood. It is an active research area. The right answer when a student asks is: it is a known unresolved problem.

**Synthetic lethality and PARP inhibitors.** Here is where this chapter's repair logic cashes out in the clinic. **PARP1** is an enzyme involved in detecting single-strand breaks and recruiting BER machinery. Inhibit PARP1 in a normal cell — the cell survives, because HR can repair any single-strand breaks that escape BER and become double-strand breaks during replication. Lose BRCA1/2 in a normal cell — the cell survives most of the time, because BER and NHEJ handle most damage. But lose *both* simultaneously: single-strand breaks that escape BER become double-strand breaks during replication, HR is unavailable, NHEJ is error-prone, and the cell either dies from accumulated damage or undergoes catastrophic chromosomal rearrangement.

This is the mechanism of **olaparib** and the other PARP inhibitors approved for BRCA-mutated cancers. The drug does not directly kill BRCA-deficient cells. It blocks a repair pathway (BER, by trapping PARP1 on damaged DNA), and that block forces cells to use the pathway they cannot use (HR, missing because BRCA was lost). Tumor cells die from a repair-pathway dependency the surrounding normal cells do not share — the normal cells retain one good BRCA allele and can do HR; the tumor cells lost the second copy somatically and cannot. **Synthetic lethality** turns the tumor's defect into its vulnerability. This is one of the cleanest targeted-therapy mechanisms in oncology, and it traces directly to the molecular logic of DNA repair we have spent this chapter building.

<!-- → [INFOGRAPHIC: Synthetic lethality diagram — two-by-two grid with PARP1 status on one axis (functional / inhibited) and BRCA1/2 status on the other (functional / deficient); three cells of the grid labeled "viable" (PARP functional + BRCA functional; PARP inhibited + BRCA functional; PARP functional + BRCA deficient) and one cell labeled "lethal" (PARP inhibited + BRCA deficient); arrows labeled with the repair-pathway logic for each cell — caption: "Synthetic lethality: the tumor's defect becomes its vulnerability"] -->

---

## Telomeres — one more problem the cell had to solve

There is one more replication problem worth naming, because it matters for cancer in Chapter 8. Linear chromosomes have ends. Every time the lagging strand is synthesized, a terminal RNA primer is removed — and there is no upstream DNA to extend from once the primer at the very end of the chromosome is removed. The lagging strand shortens by the length of the terminal primer every round.

Without a fix, chromosomes would shorten with every cell division until they ran out of essential genes. The fix is **telomeres** — long, repetitive, non-coding sequences at chromosome ends (in vertebrates, the hexamer TTAGGG repeated thousands of times). Telomeres are a buffer: they shorten with each division, but the shortening hits non-coding sequence, not genes. When the buffer is exhausted, the cell detects critically short telomeres as DNA damage and enters permanent growth arrest — **senescence** — or dies. This mechanism puts a counter on the number of times a normal somatic cell can divide, around 50 population doublings in cultured human fibroblasts: the **Hayflick limit**.

Some cell types maintain telomeres by expressing **telomerase**, an enzyme that carries its own RNA template and adds telomeric repeats back onto chromosome ends. Germline cells, stem cells, and most cancer cells express telomerase; most somatic cells do not. Most human cancers reactivate telomerase somatically, escaping the Hayflick limit, which is exactly what you would expect if cancer requires cells that can divide without limit. We will pick this up in Chapter 8.

---

## What the chapter built

Step back and look at what we have assembled.

Mendel had factors that segregated. By 1944 we knew they were DNA. By 1953 we knew DNA was a double helix — antiparallel, complementary strands, A-T and G-C paired across the interior. By 1958 we knew replication was semiconservative. By 1968 we had Okazaki fragments. By the 2015 Nobel, we had the full repair-pathway architecture: mismatch repair, base excision repair, nucleotide excision repair, homologous recombination, non-homologous end joining.

The mutation rate — ~10⁻⁹ per base per replication, ~3 mutations per cell division — is the product of all these layers. It is not a property of DNA. It is the property of DNA plus its defenders. Take away one defender — MMR, NER, or HR — and the mutation rate rises by roughly 100-fold. Take away the right two simultaneously — HR and BER — and the cell dies. The defenders are not optional. They are the genome.

This is also where Mendel's framework finally meets molecular biology. The "factors" Mendel inferred from pea phenotypes are stretches of DNA whose sequence specifies the proteins that build the organism. The mutations that produce Mendel's alleles are sequence changes that survived all three layers of replication fidelity and all four repair pathways. The dominance relationships from Chapter 2 and the penetrance discussions from Chapter 3 are downstream of what specific sequence change happened where, and how the cell handled it. The transmission genetics framework — alleles, gametes, ratios — is the macroscopic shadow of the machinery we just walked through.

---

## LLM Exercise — Build your DNA replication and repair simulator

### The simulation prompt

```
Show: Read CLAUDE.md and DESIGN.md from this project. Conform to them.

Say: Build 04-dna-replication-repair.html — a DNA replication
and repair simulator with two panels.

Panel 1 — Replication fork. Animated top-down view of a moving
fork. Show helicase as a wedge prying open the parental duplex;
SSBs coating the separated strands; topoisomerase visible ahead
of the fork. Show primase laying down RNA primers (contrasting
color from DNA). DNA polymerase synthesizing the leading strand
continuously in the direction of fork motion. On the lagging
strand: primase placing a new primer every ~1,000 bases of fork
progress, polymerase extending each primer backward to form an
Okazaki fragment, primer removal, gap fill, ligation.

Sliders: fork speed (1x, 5x, 25x). Error-injection toggle: when
on, the polymerase incorporates wrong bases at ~1e-5 rate, with
proofreading catching most and MMR catching the rest. Two
counters: errors made, errors corrected, residual errors per
simulated replication round.

Panel 2 — Damage and repair. Static fragment of double-stranded
DNA. Damage-type selector dropdown:
- Mismatched base (G across from A) → MMR pathway: MutS-MutL
  finding mismatch, MutH nicking daughter strand, exonuclease
  excising, polymerase resynthesizing, ligase sealing.
- Depurination → BER: AP endonuclease cutting, short patch
  repaired, ligated.
- Deaminated cytosine (C→U) → BER: UDG removing U, AP
  endonuclease cutting, gap filled with correct C, ligated.
- Thymine dimer → NER: XPC recognizing distortion, ~25-30 nt
  patch excised, resynthesized, ligated.
- Double-strand break, S phase → HR: resection, RAD51 filament,
  sister-chromatid invasion, copy-over, resolution. Error-free.
- Double-strand break, G1 phase → NHEJ: Ku70/80 binding ends,
  ligation with occasional small insertions/deletions.

Failure-mode toggles:
- MMR off → Lynch phenotype: mutation counter accumulates ~100x
  faster, microsatellite instability shown.
- NER off → XP phenotype: under UV exposure button, mutations
  accumulate proportionally to UV dose.
- HR off → BRCA-deficient phenotype: DSBs shunt to NHEJ,
  chromosomal-rearrangement counter ticks up.
- HR off + PARP inhibition toggle → synthetic lethality: cell
  dies (shown visually).

Lifetime mutation counter: side display showing total mutations
under current settings vs. wild-type accumulation.

Constrain: Two panels side by side, SVG canvas 720x480 each.
Single self-contained HTML file, D3 v7 from CDN. Color palette:
wild-type cells green #27ae60, damaged/mutant red #c0392b,
repair proteins gray-blue #5d6d7e, parental strand dark blue
#1a5276, daughter strand medium blue #2980b9, RNA primers
orange #e67e22. Add at top of script:
// CLAIM: The ~1e-9 per-base error rate is produced by three
// nested layers: polymerase fidelity (~1e-5), 3'->5'
// proofreading (~1e-7), and mismatch repair (~1e-9). Each
// repair pathway failure raises mutation rate ~100-fold.

Verify: Print to console on each parameter change as PASS/FAIL:
(1) With all repair active: residual error rate ~1e-9, ~3
    mutations per simulated 3e9-bp genome.
(2) MMR off: error rate ~1e-7, ~300 mutations per genome.
(3) NER off + UV exposure: thymine-dimer accumulation
    proportional to UV dose, mutation rate elevated.
(4) HR off + PARP inhibited: cell-death event triggered within
    a configurable number of division cycles.
(5) NHEJ repair of G1 DSB: junction-mutation counter increments
    with non-zero probability per repair event.
```

### Exploration tasks

Once the simulation runs:

1. **The accuracy stack.** Enable all repair pathways. Run 10 simulated replication rounds. Record the residual mutations per round. Then disable MMR only and run 10 more. Note the ~100-fold increase. Then re-enable MMR and disable proofreading only. Compare. The point: each layer is independent, and the total accuracy is the product of all layers.

2. **Synthetic lethality.** Enable the HR-off toggle. Run 50 division cycles. Note the elevated chromosomal-rearrangement rate but that the cell survives. Then add PARP inhibition. Note the generation at which the simulation calls cell death. This is the mechanism olaparib exploits.

3. **The XP dose-response.** Enable NER-off. Press the UV-exposure button 1 time, 5 times, 20 times. Plot mutations accumulated versus UV doses. The relationship should be roughly linear — each dose adds a fixed number of thymine dimers, each of which has a fixed probability of being converted to a mutation at the next division. This is the dose-response curve that underlies population epidemiology of UV exposure and skin cancer.

### Extension prompt

```
Extension: Add a third panel — Telomere Dynamics. Show a
chromosome end as a linear DNA segment with a TTAGGG-repeat
telomere region on the right. Animate one replication cycle:
the lagging strand shortens by ~50–200 bp (the length of the
terminal primer) per round. Add a division counter. At each
division, the telomere shrinks visibly. Add a telomerase toggle:
when on, telomerase adds repeats back to the 3' end at each
cycle, maintaining telomere length. When off, show the telomere
reaching a minimum threshold (configurable, default 50 repeats)
and triggering either senescence (cell stops dividing, gray
out the cell) or crisis (cell continues dividing, telomere
length turns red, chromosomal fusions begin appearing as lines
connecting chromosome ends). Add a "cancer cell" mode that
automatically enables telomerase reactivation after 5 divisions
in crisis, allowing the cell to escape senescence and divide
indefinitely. This demonstrates the Hayflick limit and telomerase
reactivation as cancer-enabling events.
```

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Rosalind Franklin** produced the X-ray diffraction data — Photograph 51 — that confirmed the helical structure of B-form DNA and provided the dimensional measurements Watson and Crick used to build their model. She did this work in 1952 at King's College London, without being credited in the papers that won the Nobel Prize.

**Run this:**

```
Who was Rosalind Franklin, and what was her specific contribution
to the discovery of DNA structure? Keep it to three paragraphs.
End with the single most surprising thing about her career or
the circumstances of the Nobel Prize attribution.
```

→ Search **"Rosalind Franklin DNA"** on Wikipedia. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain what X-ray crystallography reveals about molecular structure, and specifically what the cross-shaped diffraction pattern of Photograph 51 told researchers about DNA's geometry.
- Ask it to compare what Franklin's lab notebooks and published papers said she had concluded about DNA structure versus what Watson and Crick claimed they derived independently.

What changes? What gets better? What gets worse?
