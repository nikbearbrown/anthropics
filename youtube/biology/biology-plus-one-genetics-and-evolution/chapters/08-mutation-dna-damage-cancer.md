# Chapter 8 — Mutation, DNA Damage, and Cancer Genetics: The Hinge Between Disease and Evolution

*The same molecular event. Two completely different fates. The fate is decided by which cell carries it forward.*

---

Here is the thing to hold at the start.

Three generations of women in one family carry the same one-letter change — a frameshift in *MSH2*, one of the four mismatch repair proteins. The grandmother was diagnosed with colorectal cancer at 46. Her daughter developed endometrial cancer at 44 and a second colorectal cancer at 50. The grandson came to a genetic counselor at 25 and confirmed: the same frameshift, inherited from his mother, inherited from hers before her. He has not developed any cancer. He may be 20 years from the median age at which Lynch syndrome carriers do.

Now look at this family with two different eyes.

With the genetics eye — trained by everything before this chapter — the family is a Mendelian pedigree. One allele of *MSH2* is broken. Autosomal dominant at the level of carrier risk (50% per child); recessive at the level of cell phenotype (one good copy is enough). A hereditary cancer syndrome, transmitted vertically, conferring elevated lifetime risk that may approach 70–80% but is not 100%.

With the evolution eye — which this chapter is going to train — the family is something else. Every cell in every carrier starts life with one defective *MSH2* allele. In the colon, where stem cells divide roughly every four days, there is constant opportunity for the second allele to be lost. When it is lost in a given cell, that cell's descendants have lost mismatch repair entirely. Their per-division mutation rate jumps roughly a hundredfold. Mutations accumulate — mostly silent, occasionally not. A rare one hits *APC*. A cell descended from that hit forms a hyperproliferative crypt. Another mutation activates *KRAS*. The crypt becomes an adenoma. Another takes out *SMAD4*. Another knocks out *TP53*. Forty years after inheriting the frameshift, a single cell lineage somewhere in the colon may have run all the way down this path.

That is somatic evolution. Inside the body. On the timescale of decades. By exactly the three ingredients — variation, differential reproduction, heredity — that, scaled up twelve orders of magnitude in body count and seven in time, produced every species on Earth.

The same frameshift. In the germline, it is inherited variation — the raw material that passes between generations, the thing that selection in a population gene pool acts on. In a somatic colonic stem cell that loses its second *MSH2* allele, it is disease mechanism. The chemistry of the change is identical. The fate depends entirely on which cell lineage carries it forward.

That is the bridge this chapter is built on.

---

## The typology of change

Before causes, before consequences, the vocabulary. Two axes matter.

**How big is the change?** A point mutation is a change to a single base pair. If it swaps one base for another, it is a substitution. Substitutions that swap one purine for the other (A↔G) or one pyrimidine for the other (C↔T) are **transitions** — the chemical structure stays in the same ring-count class. Substitutions that swap a purine for a pyrimidine are **transversions** — a two-ringed base becomes a one-ringed base or vice versa. There are 4 possible transitions and 8 possible transversions, but in real genomes transitions outnumber transversions roughly two to one. The Ts/Tv ratio is skewed because the chemistry that generates mutations is not uniform across the twelve possibilities. Deamination of 5-methylcytosine at CpG dinucleotides — one of the dominant spontaneous mutation processes — produces C→T, a transition. The empirical ratio falls out of chemistry, not coincidence.

An **indel** adds or removes one or a few base pairs, usually at repetitive sequences where the polymerase slips: the daughter strand briefly unpairs from the template, re-pairs one unit out of register, and the polymerase continues. The MMR pathway's signature failure mode — microsatellite instability in Lynch syndrome — is precisely uncorrected slippage at short tandem repeats.

Beyond point mutations lie **chromosomal mutations**: deletions of segments, duplications, inversions, translocations. The Philadelphia chromosome — t(9;22), fusing *BCR* on chromosome 22 to *ABL1* on chromosome 9 — produces a constitutively active BCR-ABL kinase that drives chronic myeloid leukemia. Imatinib, designed to inhibit BCR-ABL, turned CML from a death sentence into a manageable chronic condition. Chromosomal rearrangements produce oncogenes by juxtaposition, not by changing any base.

**What happens to the protein?** When a point mutation falls in a coding region, four outcomes:

A **silent** mutation changes the codon but not the amino acid — the code's redundancy absorbs it. Silent does not always mean invisible: codon usage affects translation rate, and some silent changes disrupt splicing enhancers. The category names the codon-level event, not the organismal consequence.

A **missense** mutation changes the amino acid. Whether the change matters depends on which amino acid is where. The sickle-cell substitution — GAG→GTG at codon 6 of β-globin, glutamate to valine — is a missense mutation. A conservative substitution at a tolerant residue may be indistinguishable from wild-type. A non-conservative substitution at an active site may be devastating. The category says nothing about which.

A **nonsense** mutation changes a sense codon to a stop codon. The protein is truncated. Most truncated proteins are non-functional — they lack downstream domains, misfold, and are targeted by nonsense-mediated decay, which recognizes premature stop codons and destroys the mRNA before much protein is made.

A **frameshift** indel shifts the reading frame. Every codon downstream of the indel is wrong. A new stop codon — statistically present every ~21 codons in random sequence — usually terminates translation prematurely. Frameshifts are typically the most destructive category. The *MSH2* frameshift in the Lynch family above is one.

The pedagogical move: β-globin, one gene, four mutations, three diseases. GAG→GTG at codon 6 is missense (sickle cell). AAG→TAG at codon 17 is nonsense (β⁰-thalassemia). A single-base insertion in exon 1 is frameshift (thalassemia from truncation). A G→A at the 5' splice site of intron 1 is a splice-site mutation — the intron is not removed, the reading frame is disrupted, the protein is absent. Same gene. Four molecular categories. One gene does not care which happens; the chemistry of each change determines the outcome.

<!-- → [TABLE: four-row summary of the β-globin mutation examples — columns: mutation name, DNA change, mutation type (missense/nonsense/frameshift/splice-site), protein consequence, disease. Rows: HbS (GAG→GTG at codon 6, missense, Glu→Val, sickle cell); β⁰-thalassemia (AAG→TAG at codon 17, nonsense, truncation via premature stop, β-thalassemia); β-thalassemia frameshift (single-base insertion exon 1, frameshift, scrambled sequence + premature stop, β-thalassemia); β-thalassemia splice-site (G→A at 5' splice site intron 1, splice-site, intron retained, protein absent). Student should see that the same gene produces four distinct molecular categories of change with different protein consequences.] -->

---

## Where mutations come from

**Spontaneous sources** are the body's chemistry doing it to itself, every day.

*Replication error.* DNA polymerase makes mistakes. Even after the 3'→5' proofreading exonuclease and mismatch repair, the residual per-base error rate in bacteria is roughly 2 × 10⁻¹⁰. In humans the comparable per-nucleotide-per-generation rate is about 1.2 × 10⁻⁸ — a hundred-fold higher, mostly because of the greater number of cell divisions between germline generations and the larger genome.

*Tautomeric shifts.* Each DNA base has a rare alternate form — a tautomer — in which a hydrogen has moved. In the rare imino form, adenine pairs with cytosine rather than thymine. The tautomers are short-lived (microseconds), but if the polymerase arrives at the wrong moment, the incorrect partner gets incorporated. This is a quantum-mechanical, irreducibly stochastic source of error. No proofreading can catch it, because the misincorporated base looks correct at the moment it enters.

*Depurination.* The glycosidic bond between adenine or guanine and deoxyribose breaks spontaneously — about 10,000 times per mammalian cell per day. Most abasic sites are repaired by base excision repair. Those that reach the replication fork before repair get adenine inserted opposite them by default (the "A rule"), generating a transversion if the lost base was G or C.

*Deamination.* Cytosine spontaneously loses its amino group and becomes uracil. Uracil pairs with adenine — if not repaired, the C:G pair becomes a T:A pair after one more replication. Uracil-DNA glycosylases catch most of these because uracil is wrong in DNA. But 5-methylcytosine, the methylated cytosine at CpG dinucleotides, deaminates to *thymine* — which is a normal base. The repair machinery cannot distinguish the deaminated product from a real T. The change slips through. This is why CpG→TpG is the single most common substitution in the human genome, and why the most universal cancer mutational signature — SBS1, accumulating at a roughly constant rate per year in every tissue — is essentially a clock counting 5-methylcytosine deaminations.

**Induced sources** are the world doing it to you.

*UV light* creates covalent crosslinks between adjacent pyrimidines — cyclobutane pyrimidine dimers. The nucleotide excision repair pathway removes them. When NER fails — in xeroderma pigmentosum (XP) patients, or simply when there is more damage than the cell can repair in time — translesion synthesis past the dimer produces C→T transitions at dipyrimidine sites. This is the fingerprint of sun exposure: skin cancers are littered with C→T at CC, CT, TC, TT contexts.

*Tobacco smoke* contains over 70 carcinogens, including polycyclic aromatic hydrocarbons that, after metabolic activation in the lung, form bulky adducts on guanine. Translesion synthesis past these adducts produces G→T transversions (C→A on the complementary strand). This is signature SBS4 — pervasive in lung cancers of smokers, absent in lung cancers of never-smokers.

*Alkylating agents* add methyl or other carbon groups to bases. Methylation at O⁶ of guanine causes it to pair preferentially with thymine, generating G:C→A:T transitions. Temozolomide, used in glioblastoma therapy, is a designed alkylator — it mutates tumor DNA enough to kill tumor cells.

*Intercalating agents* — flat aromatic molecules like ethidium bromide and acridines — slide between base pairs and distort the helix, causing the polymerase to slip. The product is frameshifts, not substitutions.

*Ionizing radiation* breaks DNA directly. Double-strand breaks, the most dangerous lesions, are repaired by homologous recombination (high fidelity, uses a sister chromatid as template) or non-homologous end joining (faster, error-prone, often leaving small indels at the ligation site). The NHEJ signature is short indels at break sites.

**The Ames test.** Bruce Ames's 1973 assay closes the chain from molecular event to public-health concern. Strains of *Salmonella typhimurium* carry specific mutations in the histidine biosynthesis operon that prevent growth without histidine. A single back-mutation can revert each. Plate the bacteria on minimal medium without histidine, add the test chemical, and count colonies — each colony is a cell that reverted its *his* mutation because the chemical mutated it back to functional. Different strains detect different mutation types: TA98 has a frameshift mutation, TA100 has a base-substitution mutation. A chemical that produces colonies on TA100 but not TA98 is a base-substitution mutagen; one that works on TA98 is a frameshift mutagen.

The further brilliance: many carcinogens are not active in their parent form — they need metabolic activation by liver cytochrome P450 enzymes to become reactive electrophiles. Bacteria have no liver. Ames added rat liver homogenate (the S9 fraction) to the plate. Now the bacteria see whatever the rat liver makes from the test chemical. The assay tests pre-carcinogens as well as carcinogens. Roughly 90% concordance between bacterial mutagenicity and animal carcinogenicity was the result. "Carcinogens are mutagens" was earned, not assumed. The Ames test is now a regulatory standard worldwide for consumer chemical screening.

<!-- → [INFOGRAPHIC: Ames test workflow — left panel shows plates for TA98 (frameshift tester strain) and TA100 (base-substitution tester strain) without test chemical (background revertant colonies only); center panel shows the same plates with test chemical added (elevated colony counts on one or both); right panel shows S9 fraction addition for pre-carcinogen activation. Student should see how running the chemical on both strains simultaneously identifies not just mutagenicity but mutation type, and how the S9 liver fraction extends the assay to metabolically activated carcinogens.] -->

---

## Mutation rates — the arithmetic matters

Mutation rate is a probability per unit of opportunity. The units must be stated; the literature contains many apples-to-oranges comparisons.

SARS-CoV-2: ~1.3 × 10⁻⁶ per site per replication cycle. RNA-dependent RNA polymerase has essentially no proofreading. HIV reverse transcriptase: ~3 × 10⁻⁵ per site per replication. *E. coli*: 2.2 × 10⁻¹⁰ per base pair per generation. Humans: 1.2 × 10⁻⁸ per nucleotide per generation.

<!-- → [CHART: log-scale bar chart of mutation rates across organisms — x-axis: organism (RNA viruses, HIV, bacteria, Drosophila, humans); y-axis: mutation rate per base pair per replication or generation (log scale from 10⁻¹¹ to 10⁻⁴). Bars sorted from lowest to highest rate. A bracket annotation on the human bar should indicate the ~70 de novo SNVs per child that result from the per-nucleotide rate × genome size × 2 copies. Student should see the four-order-of-magnitude range across life and recognize that RNA viruses are the outliers at both ends of the biological logic (fastest per site despite large populations).] -->

The cross-organism range spans four orders of magnitude. Michael Lynch's drift-barrier hypothesis explains the pattern: natural selection should push mutation rates down, because most mutations are deleterious and any allele improving replication fidelity should be favored. But selection on mutation rate is second-order — it depends on the fitness consequences of future mutations the allele would prevent. In small effective populations, drift overwhelms second-order selection, and mutation rates cannot fall further. Large-population organisms (bacteria, RNA viruses) should have the lowest rates — but RNA viruses are an exception, because high mutation rate is itself selected to generate immune-escape variants. Vertebrates, with small effective population sizes, have higher per-base rates.

Now do the human arithmetic. Take 1.2 × 10⁻⁸ per nucleotide per generation. Multiply by the haploid genome size, ~3 × 10⁹ bp. Multiply by two (the diploid child receives one haploid copy from each parent). Result: **roughly 70 new single-nucleotide variants per human child per generation**. The exact count depends on parental age — it rises linearly with paternal age by about 2 mutations per year, because spermatogonial stem cells keep dividing throughout a man's life while oocytes are largely arrested.

Every person you have ever met carries dozens of point mutations that neither parent had. Some are silent. Some affect splicing. A small fraction hit genes where the amino acid change matters — these are the *de novo* mutations responsible for dominant developmental disorders (some autism-spectrum conditions, certain rare intellectual disabilities) that appear in families with no prior history. The clinical genome-sequencing revolution of the past 15 years rests on this arithmetic: *de novo* mutations explain a substantial fraction of severe pediatric disease that does not run in families.

Now move from per-generation to per-cell-division, which is the unit that matters for cancer. A normal somatic cell, dividing, generates roughly **3–6 new point mutations** per daughter cell — about 10⁻⁹ per base pair per replication, times the 3 × 10⁹ bp genome. Over an 80-year lifespan, the human body executes very roughly 10¹⁶ total cell divisions. At ~3 mutations per division: ~3 × 10¹⁶ mutational events in your body over your lifetime. The genome has 3 × 10⁹ bases. Every base in your genome has been mutated, in some cell, hundreds of times over. Cancer is not a rare accident. It is the inevitable consequence of stochastic mutation in cells that keep dividing. The question is not why cancer happens. It is why it doesn't happen more often.

The answer to that question is the rest of this chapter.

---

## Cancer as somatic evolution

Peter Nowell's foundational 1976 paper is one page long. Its central claim — that most tumors arise from a single cell of origin and that progression reflects acquired genetic variability with sequential selection — has held up across 50 years of increasingly deep sequencing. Let me make the claim mechanistic.

Natural selection requires exactly three ingredients:

**Variation.** Mutations produce heritable differences among cells. A typical adult tissue is a mosaic — different patches descend from different lineages, each with its own accumulated mutations. This has been directly confirmed by sequencing normal tissue: Martincorena and colleagues found that normal sun-exposed skin carries 2–6 mutations per megabase, and that 18–32% of cells harbor driver mutations in known cancer genes. Normal esophagus showed NOTCH1 mutations colonizing up to 80% of cells in middle-aged donors. The normal body is full of clonal expansions. Most stay benign.

**Differential reproduction.** Mutations that increase proliferation, decrease apoptosis, or evade immune detection allow some clones to outgrow their neighbors. A clone that divides 20% faster than the average systematically takes over its patch of tissue. This is selection — the cell analogue of differential reproductive success.

**Heredity.** Mitosis passes DNA from mother cell to daughter cell with high fidelity. The daughter cell inherits the mother's full mutational complement plus its own new mutations. Heritability of cell phenotypes across mitotic generations is essentially 1.

That is the full Darwinian recipe. The body is the environment. Mutations are the variation. Selection pressures include nutrient availability, oxygen tension, immune surveillance, and — once treatment begins — chemotherapy and targeted drugs. Therapy resistance is just selection in another direction: the clones that happen to carry a resistance mutation outgrow the sensitive ones. This is not a metaphor. The math of clonal expansion in a tumor and the math of allele frequency increase in a population are both of the form *p(t+1) = p(t) × (1 + s)*. The equations are literally the same.

---

## Knudson's two-hit hypothesis — the arithmetic worked through

Alfred Knudson published in 1971 the statistical paper that founded tumor suppressor biology. The data were simple: 48 retinoblastoma cases at MD Anderson, some hereditary (bilateral, early-onset), some sporadic (unilateral, later-onset). Knudson noticed that hereditary cases followed one-hit kinetics — onset rate linear with the number of retinoblasts — and sporadic cases followed two-hit kinetics — rate quadratic. He inferred retinoblastoma requires two genetic events at a single locus.

The arithmetic falls out directly. Define:
- *μ* ≈ 10⁻⁶ per locus per division (the per-base rate of ~10⁻⁹, times ~1,000 relevant base pairs in a gene)
- *N* ≈ 10⁶ retinoblasts per eye
- *D* ≈ 30 divisions during retinal development

**Hereditary case.** One *RB1* allele is already broken in every cell. Probability that any given retinoblast loses the second allele: *μ × D* ≈ 10⁻⁶ × 30 = 3 × 10⁻⁵. Expected cells losing the second allele per eye: *N × μ × D* ≈ 10⁶ × 3 × 10⁻⁵ ≈ 30. Essentially guaranteed to occur in both eyes. Hence bilateral, multifocal, early onset.

**Sporadic case.** Both alleles intact in every cell. Probability of losing both in one lineage: *(μ × D)²* ≈ (3 × 10⁻⁵)² ≈ 10⁻⁹. Expected events per eye: *N × (μ × D)²* ≈ 10⁶ × 10⁻⁹ = 10⁻³. About one in a thousand eyes develops a tumor. When it does, one tumor, one eye, late in development.

Knudson made this prediction in 1971 with a slide rule and a small clinical dataset. The *RB1* gene was cloned in 1986; whole-genome sequencing of retinoblastomas confirmed every detail decades later. The lesson generalizes immediately: any loss-of-function tumor suppressor follows two-hit kinetics; any gain-of-function oncogene follows one-hit kinetics. This asymmetry is not convention — it is Mendel's dominance logic applied to single cells.

<!-- → [INFOGRAPHIC: two-panel Knudson diagram — left panel: hereditary retinoblastoma (one hit pre-installed in germline, second hit occurs somatically in many retinoblasts; arrows show both eyes affected, early onset); right panel: sporadic retinoblastoma (both hits must occur somatically in same lineage; probability product (μ×D)² is tiny; one eye affected, later onset). Each panel should show a schematic retina with colored cells indicating which cells have lost one vs. two RB1 alleles. Student should see why the product-of-probabilities arithmetic forces the bilateral/unilateral and early/late-onset pattern.] -->

---

## Proto-oncogenes and tumor suppressors — the dominance asymmetry

A common confusion: students think "oncogene mutation" and "tumor suppressor mutation" are different *kinds* of DNA changes. They are not. The same substitutions, indels, and frameshifts fall in both categories. What differs is which gene is hit and what the change does to that gene's product.

**Proto-oncogenes** encode proteins that promote growth: receptor tyrosine kinases, cytoplasmic kinases, transcription factors. KRAS — the small GTPase that relays signals from growth-factor receptors to downstream cascades — is mutated in roughly 90% of pancreatic cancers. Specific point mutations at codons 12, 13, or 61 lock KRAS in its GTP-bound, constitutively active form. One mutant allele is enough — the constitutively active protein produces continuous growth signal regardless of what the wild-type allele is doing. One hit; dominant at the cellular level.

**Tumor suppressors** encode proteins that restrain growth: checkpoint proteins, DNA repair components, pro-apoptotic regulators. RB1 gates the G1/S checkpoint. TP53 responds to DNA damage by arresting the cell cycle, driving repair, or triggering apoptosis. APC restrains β-catenin signaling. Both alleles must be lost to remove the restraint — one functional copy provides enough protein. Two hits; recessive at the cellular level.

The dominance asymmetry is not arbitrary. A gain of function requires only one productive allele making the constitutively active product. A loss of function requires eliminating all productive copies. Dominance follows function follows mechanism.

The clinical implication is sharp: **inherited cancer predispositions are almost entirely germline mutations in tumor suppressors, not oncogenes.** A constitutively active RAS in every cell of the embryo would abort development. Carriers of BRCA1, Lynch, Li-Fraumeni, and FAP germline mutations are recessive at the cellular level — every cell still has one working copy, and most cells keep it for life. What the carrier has is a dramatically elevated probability of losing the second allele somewhere in some dividing tissue. The germline mutation is one hit already taken; the somatic second hit is the disease event. That is why Lynch syndrome carriers begin their colorectal cancer trajectory 20 years earlier than the general population — the first hit was pre-installed at conception.

---

## Multi-step carcinogenesis — the colorectal model

Fearon and Vogelstein's 1990 synthesis of the colorectal cancer literature remains the most influential model of cancer progression. Here is the sequence.

**Normal epithelium.** Stem cells at the crypt base divide; daughters migrate up, differentiate, and are shed. Homeostasis.

**APC loss → small adenoma.** APC normally targets β-catenin for degradation. Lose both copies and β-catenin accumulates, driving Wnt-pathway targets including MYC and cyclin D1. The crypt becomes hyperproliferative. A small polyp forms.

**KRAS activation → large adenoma.** A point mutation at codon 12 locks KRAS on. Constitutive proliferative signaling compounds with the Wnt-driven cell-cycle entry. The polyp grows.

**SMAD4 loss → late adenoma.** TGF-β pathway components, especially SMAD4, provide growth restraint. Lose them and dysplasia deepens.

**TP53 loss → invasive carcinoma.** Without p53, cells with damaged DNA do not die — they divide. This is the transition from adenoma to invasive cancer, the moment cells break through the basement membrane.

**Further mutations → metastasis.** Immune evasion, vascular invasion, and survival in the circulation require additional hits whose identity varies by patient.

The timeline is approximately 10–30 years from initial APC loss to clinical cancer. Hence colonoscopy screening starting at 45–50: most adenomas are detectable and removable during the long latent phase. Polypectomy is curative early; the same disease undetected for a decade more may be terminal.

The pan-cancer generalization: the typical adult solid tumor carries 2 to 8 driver mutations embedded among hundreds to thousands of passengers. Most of the mutational burden is noise. A handful of driver hits, accumulated sequentially under selection, is the signal. The process is iterative, stepwise, evolutionary.

<!-- → [INFOGRAPHIC: Fearon-Vogelstein colorectal cancer progression timeline — a horizontal arrow spanning 10–30 years, with five labeled steps: (1) normal epithelium → (2) small adenoma (APC loss, crypt hyperproliferation) → (3) large adenoma (KRAS activation) → (4) late adenoma/dysplasia (SMAD4 loss) → (5) invasive carcinoma (TP53 loss) → (6) metastasis (additional hits). Each step should show the histological stage name, the key driver gene hit, and the protein pathway affected (Wnt, MAPK, TGF-β, DNA damage checkpoint). A secondary timeline below should indicate the colonoscopy screening window (adenoma detectable and removable at steps 2–4, before invasion at step 5). Student should see why the long latency makes screening effective.] -->

---

## Mutational signatures — the tumor's archaeological record

Different mutagens leave different chemical fingerprints. This is the most beautiful recent development in cancer genomics.

UV produces C→T transitions at dipyrimidine sites — wherever two adjacent pyrimidines are crosslinked by UV, translesion synthesis errors in that specific context. Tobacco polycyclic aromatic hydrocarbons produce C→A transversions (from G-adducts read opposite adenine). APOBEC cytidine deaminases act at TCW contexts (W=A/T) and produce C→T and C→G. MMR failure produces indels at microsatellites. Each mutagen leaves a different spectrum across the 96 possible trinucleotide-context substitution categories.

In 2013, Alexandrov, Stratton, and colleagues asked: can these signatures be extracted from cancer data alone, with no prior knowledge of exposure? They took ~5 million mutations from 7,042 tumors and used non-negative matrix factorization to find recurring patterns. They found more than twenty distinct signatures; the 2020 update expanded the catalog to 49 single-base substitution signatures, each with a specific inferred cause. The COSMIC database maintains the full reference set.

Key signatures:

**SBS1** — C→T at CpG. Clock-like; accumulates at a roughly constant rate per cell per year regardless of tissue. Cause: spontaneous 5-methylcytosine deamination. Present in every tumor in proportion to the time elapsed and division rate of the tissue of origin. SBS1 burden is essentially the molecular clock of cell-division history.

**SBS4** — C→A transversions throughout the genome. Cause: tobacco polycyclic aromatic hydrocarbons. Dose-dependent on pack-years. Found in lung cancers of smokers; absent in those of never-smokers.

**SBS7a/b** — C→T at dipyrimidines. Cause: UV. Pervasive in skin cancers.

**SBS2/SBS13** — C→T and C→G at TCW. Cause: APOBEC activity. Common in bladder, breast, cervical, and head-and-neck cancers.

**SBS6, SBS15, SBS20, SBS26** — broad substitution patterns plus indels at microsatellites. Cause: mismatch repair deficiency. Diagnostic of MSI-high tumors.

**SBS3** — broad genome-wide pattern. Cause: homologous recombination deficiency (BRCA1/BRCA2 loss). Predicts PARP-inhibitor response.

<!-- → [IMAGE: COSMIC-style mutational signature spectrum for SBS4 (tobacco) and SBS7a (UV) side by side — each spectrum shows 96 trinucleotide-context mutation categories (x-axis) with bar height indicating relative contribution (y-axis); SBS4 should show dominant C>A bars concentrated in NCC contexts; SBS7a should show dominant C>T bars concentrated at dipyrimidine contexts. Labels should indicate which bars correspond to which exposures. Student should see that the two spectra are visually distinct and that reading a tumor's spectrum against these references allows exposure inference.] -->

A clinical example. A 62-year-old former smoker presents with a lung adenocarcinoma. Sequencing returns ~22,000 total point mutations — very high. About 60% are SBS4 (tobacco); 15% are SBS1 (clock); 10% are SBS2/SBS13 (APOBEC). The driver mutations include KRAS G12C, TP53 R175H, and STK11 truncation. Two things this profile teaches.

First, the tumor remembers. Quitting smoking 10 years before diagnosis does not erase the SBS4 signature. Those mutations were installed during active smoking, copied through every subsequent cell division, and remain in the cancer that eventually emerged. Smoking cessation reduces the rate of new damage but does not reverse accumulated damage. The risk curve after quitting is exponentially decaying but never reaches zero.

Second, the mutagen specified the driver. KRAS G12C is a C→A transversion — exactly the change SBS4 produces. Smokers enrich for KRAS G12C in lung cancers because tobacco generates C→A transversions; never-smokers enrich for EGFR mutations (which arise from different substitution types). The exposure shapes which drivers are possible. KRAS G12C is now druggable (sotorasib, adagrasib), so the mutational signature predicts both the cause and the targeted therapy.

The broader point: a tumor genome is an archaeological record of the exposures that produced it. The conceptual move that lets oncologists infer carcinogen history from tumor mutation spectra is the same move that lets evolutionary biologists infer ancestral environments from mutation patterns in extant species. The same molecular clock — SBS1, deamination at CpG — that measures cell-division history in a tumor will measure evolutionary divergence times in Chapter 13.

---

## The two faces of mutation

Now the bridge the chapter was built to cross.

**Face one: somatic mutation.** A change occurred in a dividing cell of an adult tissue. Mitosis copies it to daughter cells; they copy it to theirs. If it confers a growth advantage, the lineage expands. If it is a strong driver in combination with enough other drivers, it eventually produces clinical cancer. The mutation is disease mechanism. It dies when the body dies.

**Face two: germline mutation.** A change occurred in a cell that ultimately gives rise to a gamete. Meiosis copies it into the sperm or egg. If that gamete fertilizes another, the resulting zygote carries the mutation in every cell — every tissue, every organ, every dividing cell in the new organism's body. If the offspring reproduces, half their gametes carry it. With sufficient generations, the allele drifts to fixation, drifts to loss, or settles into intermediate frequency — depending on its fitness effect and the population's demographics.

The mutation is now evolutionary raw material. It is one of the alleles Chapter 9 will treat as the input to selection. The same mutation can drive adaptation, balanced polymorphism, speciation. It is the variation Mendel inferred but had no mechanism for, the variation Darwin needed but could not derive, the variation the modern synthesis connected to both.

**The connecting machinery is identical.** Mitosis and meiosis both copy DNA with high fidelity. Mutations happen at characteristic rates in both. Selection acts in both — at the cellular level in the soma; at the organismal level in the germline. The math of clonal expansion in a tumor and the math of allele frequency change in a population are both of the form *p(t+1) = p(t) × (1 + s)*. The difference is quantitative:

*Timescale.* Somatic evolution runs over months to decades — cell generations of hours to days. Germline evolution runs over thousands to millions of organism generations of years to centuries.

*Population size.* A tumor contains 10⁶ to 10¹² cells. The effective population of a sexual species is typically 10³ to 10⁹ organisms.

*Bound.* The somatic population is bounded by the body and dies with the body. The germline population is bounded only by extinction.

These are differences of scale, not of kind. The equations are the same. What changes is which level of biological organization those equations are applied to.

The Lynch family makes this concrete. The *MSH2* frameshift in the grandson's genome occupies both roles simultaneously. In his germline — in any gametes he produces — the allele is inherited variation that will pass to his children and, if he is a carrier like his mother and grandmother, elevate their cancer risk in turn. In any somatic colonic stem cell that loses the second *MSH2* allele, the frameshift is the proximate cause of the disease mechanism that will unfold over decades. Same nucleotide change. Same cell in his body. One face looking backward through inheritance, the other looking forward through somatic progression.

This is the chapter's central claim, stated plainly: **mutation in a somatic cell is the proximate cause of cancer; mutation in a germ cell is the ultimate source of evolutionary variation; the molecular event is the same in both.** The genetics half of this book has been about the first face. The evolution half, starting now, will be about the second. Cancer sits in the middle showing both at once.

When you reach Chapter 10 and work through Hardy-Weinberg allele-frequency dynamics, you will use the same selection coefficient *s* you would use to model clonal expansion in a tumor. When Chapter 13 introduces molecular clocks, the clock mechanism is the same SBS1 deamination process that appears in every tumor sequenced and accumulates at a constant rate per year. The continuity is exact.

Mutation is neither good nor bad. Mutation is change. What it does depends entirely on which cell carries it forward.

---

## Exercises

**Warm-up**

1. **Classify the mutation.** For each of the following DNA changes, state (a) the mutation type at the DNA level (transition, transversion, indel, or chromosomal), (b) the protein-level consequence (silent, missense, nonsense, or frameshift), and (c) whether the consequence is more likely to be tolerated or disruptive, and why: (i) *HBB* codon 6: GAG→GTG; (ii) *HBB* codon 17: AAG→TAG; (iii) a single-G insertion after codon 25 of *BRCA1*; (iv) *BCR–ABL1* translocation t(9;22). *Tests: mutation typology and protein-level consequence prediction.*

2. **Spontaneous vs. induced.** A C→T substitution is found at a CpG dinucleotide in a colon tumor from a patient with no known carcinogen exposures. (a) Name the most likely spontaneous source of this change and describe the chemistry at the base level. (b) Assign this change to its most probable mutational signature (SBS1, SBS4, SBS7, or SBS2/13) and explain the assignment. (c) If the same substitution were found at a dipyrimidine site in a melanoma, would your signature assignment change? Why? *Tests: connecting mutation chemistry to signatures.*

3. **Human mutation rate arithmetic.** The human per-nucleotide mutation rate is approximately 1.2 × 10⁻⁸ per generation. The haploid genome is ~3 × 10⁹ bp. (a) How many *de novo* single-nucleotide variants does a typical child carry? (b) Approximately how many of those land in protein-coding sequence, given that coding regions are ~1.5% of the genome? (c) A father is 50 years old at conception; at 25 years old paternal age, the baseline count would have been ~65 SNVs, and the rate increases by ~2 per year of paternal age. How many extra mutations does this child carry compared to the child of a 25-year-old father? *Tests: unit conversion, order-of-magnitude arithmetic, paternal age effect.*

**Application**

4. **Knudson's arithmetic.** Apply the two-hit model to a hypothetical hereditary colorectal cancer syndrome caused by a germline tumor-suppressor mutation, with parameters: μ = 10⁻⁶ per locus per division, N = 10⁸ stem cells in the colorectal epithelium, D = 1,000 divisions per stem-cell lineage over a lifetime. (a) Calculate the expected number of cells that lose the second allele in a carrier's lifetime. (b) In a sporadic case (both hits somatic), calculate the expected number of cells that lose both alleles. (c) Based on your calculations, predict whether hereditary cases would present earlier or later than sporadic, and whether they would be more likely to be multifocal. (d) How would a 100-fold elevated mutation rate (as in Lynch syndrome) change the calculation for carriers? *Tests: applying Knudson arithmetic beyond retinoblastoma; connecting mutation rate to clinical presentation.*

5. **Oncogene vs. tumor suppressor logic.** A patient's tumor carries two mutations: a KRAS G12D substitution and a homozygous deletion of *TP53*. (a) Classify each change as oncogenic or tumor-suppressive. (b) For each, state whether one mutant allele is sufficient for the phenotypic change or whether both copies must be altered, and explain why the answer differs. (c) A close relative of this patient is found to carry a germline *TP53* R248W missense mutation (Li-Fraumeni syndrome). Why does this germline mutation predispose to cancer, and why does the relative not currently have cancer even though the mutation is in every cell? *Tests: dominance logic applied to cancer genetics; two-hit reasoning in a clinical context.*

6. **Reading a mutational signature.** A tumor's sequencing report shows: 8,400 total somatic mutations; 74% are C→A transversions with strong enrichment at GCC and ACC contexts; 18% are SBS1 (C→T at CpG); 8% other. The patient's KRAS status is G12C. (a) Name the most likely environmental exposure driving the dominant signature, and name the specific carcinogen class responsible. (b) Explain why KRAS G12C is the expected driver in this tumor, connecting the nucleotide change at KRAS codon 12 (GGT) to the dominant signature. (c) If this patient quit their exposure 8 years before diagnosis, would the SBS4 signature be diminished in the tumor compared to a current active exposure case? Explain. *Tests: signature-to-cause inference; connecting dominant mutagen to driver mutation specificity; exposure history.*

**Synthesis**

7. **Lynch syndrome, both eyes.** A 30-year-old woman is found to carry a germline *MSH2* frameshift (Lynch syndrome). Describe her cancer risk and timeline using both lenses the chapter introduces. (a) With the genetics eye: what is her per-pregnancy probability of passing the allele to a child? What is her approximate lifetime colorectal cancer risk? Why is the syndrome inherited as autosomal dominant at the pedigree level even though MMR loss is recessive at the cell level? (b) With the evolution eye: describe the somatic evolutionary process that will unfold if a colonic stem cell loses its second *MSH2* allele. Name the sequential driver hits likely involved and estimate how the mutation-rate elevation changes the timeline relative to a sporadic case. (c) Her tumor, if she develops one, will be MSI-high. Why does MSI-high predict response to immune checkpoint inhibition? Connect mutation rate → neoantigen load → immune recognition. *Tests: integrating the two-eye framing; Knudson logic; mutational signatures in clinical decision-making.*

8. **The colorectal cancer timeline.** A 48-year-old patient is found on screening colonoscopy to have a 1.2 cm tubular adenoma with low-grade dysplasia. Molecular analysis shows APC loss (both alleles) and a KRAS G12D mutation, but no SMAD4 or TP53 alterations. (a) Where on the Fearon-Vogelstein progression model does this adenoma sit? (b) Estimate how long the process may have been underway. (c) If the adenoma is removed completely (polypectomy), is the patient cured? What residual risk remains and why? (d) If the KRAS G12D were present without APC loss, what would that imply about the order of events in the Vogelstein model and why does order matter? *Tests: locating a patient in the multi-step model; reasoning about incomplete progression; driver-hit ordering.*

**Challenge**

9. **The bridge, made quantitative.** The chapter claims that somatic evolution and germline evolution are the same process at different scales, with the selection equation *p(t+1) = p(t) × (1 + s)* applying to both. (a) In a tumor with a clone carrying a driver mutation conferring a 15% per-division growth advantage (s = 0.15), starting from a single mutant cell in a tissue of 10⁷ cells, roughly how many cell divisions does it take for the mutant clone to reach 50% of the population? (assume exponential growth of the mutant clone; approximate). (b) In a population genetics context, an allele with s = 0.015 (a typical strong selection coefficient for organisms) in a population of N = 10⁴ individuals takes approximately 1/s generations to go from low frequency to near-fixation. Compare the timescales for the tumor clone and the population allele. What does this comparison tell you about why somatic evolution can appear "fast"? (c) Name one prediction the somatic-evolution framework makes that a purely mechanistic "cancer is broken machinery" view would not make — specifically about tumor behavior under treatment. *Tests: quantitative connection between somatic and germline evolution; translating the selection equation; predictive power of the evolutionary framing.*

---

---

*The next chapter crosses the bridge. Darwin's mechanism of natural selection — the conditions that make evolution possible, the evidence that it has occurred, the modern synthesis that connected Darwin to Mendel through population genetics. Mutation is the input. Every variant that selection has ever acted on arrived by the same chemistry described in this chapter. You have just been inside the mechanism that feeds the whole of evolutionary biology.*
