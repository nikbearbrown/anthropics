# Chapter 14 — Capstone: From Genes to Evolutionary Change

## TL;DR

- The same algorithm, three timescales, one mechanism stack.
- The chapter moves through Three timescales, one stack, Case 1 — Antibiotic resistance as rapid evolution, The molecular mechanism, The selective sweep, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The same algorithm, three timescales, one mechanism stack.*

---

In May 2010 Svante Pääbo's group in Leipzig published a 3-billion-base-pair draft assembly of the Neanderthal genome, built from three bone fragments from Vindija Cave in Croatia. The paper's central biological claim was that non-African modern humans carry roughly 1 to 4 percent Neanderthal ancestry. We are partial hybrids of an extinct hominin lineage, and the evidence is in our genomes.

To read that paper you have to bring meiosis and recombination from Chapter 1 — the Neanderthal ancestry is broken into chromosomal blocks whose lengths give the date of admixture, because each generation of recombination breaks the blocks shorter, and the surviving length is a clock. You have to bring DNA structure and damage from Chapter 4, because ancient DNA is post-mortem deaminated cytosine to uracil at characteristic positions, and the lab corrects for that. You have to bring mutation rates from Chapter 8 to date the human-Neanderthal split. You have to bring population genetics from Chapter 10 to estimate the admixture proportion from allele frequencies in non-African versus African populations. You have to bring speciation from Chapter 11, because Neanderthals and modern humans were not fully reproductively isolated. You have to bring the phylogenetic methods of Chapter 12 to place the Neanderthal lineage on the tree.

The Pääbo paper requires all thirteen prior chapters of this book.

Now consider two other moments. In a Chennai hospital in 2008, a *Klebsiella pneumoniae* strain was found carrying a previously undescribed metallo-β-lactamase, named NDM-1 after the city. NDM-1 hydrolyzes carbapenems — the last-resort β-lactam antibiotics — and it sits on a plasmid that has spread through Enterobacteriaceae across the world in under five years. Twenty years before that paper, NDM-1 did not exist. Now it is on every continent. The Murray et al. 2022 *Lancet* systematic analysis estimates that bacterial antimicrobial resistance caused **1.27 million deaths attributable in 2019** — more than HIV/AIDS or malaria in that year.

And consider a Maasai pastoralist boma in the Rift Valley, where people were asking why some adult humans digest milk and others get sick from it. The genetic answer took four decades to work out: a regulatory variant in an intron of *MCM6* keeps lactase expression on through adulthood, against the mammalian default of weaning-time shutoff. The variant arose independently *at least four times* in pastoralist populations on two continents. The same biochemical outcome — adult lactase expression — produced by the same selection pressure — cattle pastoralism — through different mutations in the same regulatory element.

Three cases. Three timescales. The Neanderthal genome runs at millions of years. The lactase variant runs at thousands. The carbapenem-resistant Klebsiella runs at weeks. The same mechanism stack operates in all three. That is the synthesis this book has been building toward.

---

## Three timescales, one stack

Before opening the cases, the organizing principle belongs on the page. Evolution is not one phenomenon. It is the same machinery — mutation, drift, selection, gene flow — running at very different rates in very different contexts. The contexts differ in three ways.

**Population size.** Bacteria live in populations of $10^9$ to $10^{12}$ cells per gram of gut content. Modern humans have a census of 8 billion but an effective population size relevant to drift closer to $10^4$. The difference is five orders of magnitude. Drift is feeble in bacteria and powerful in humans.

**Generation time.** Bacteria divide every 20 minutes to a few hours. Humans reproduce roughly every 25 years. The ratio is roughly $10^6$. A bacterial population passes through 50 generations in a day. Human populations pass through 50 generations in 1,250 years.

**Mutation rate per generation.** Bacteria are more accurate per base ($\sim 10^{-10}$ per base per generation); humans are less accurate ($\sim 1.2 \times 10^{-8}$). But bacteria have so many more chances per unit time that absolute mutation production rates in a bacterial infection vastly exceed those in a human pedigree.

When you multiply through: **bacteria explore sequence space about a million times faster than humans do per unit clock time.** Evolution looks fast in bacteria because bacterial evolution *is* fast in any units you choose. The mechanism is identical. The parameters differ.

---

## Case 1 — Antibiotic resistance as rapid evolution

### The molecular mechanism

A β-lactam antibiotic — penicillin, meropenem — shares a four-membered β-lactam ring that mimics the D-alanyl-D-alanine terminus the bacterial cell-wall transpeptidases (penicillin-binding proteins, PBPs) recognize as they cross-link peptidoglycan. The PBP grabs the β-lactam thinking it is substrate, the ring opens, the active-site serine is acylated, the enzyme is locked dead. Without functional PBPs the bacterium cannot maintain its wall and lyses.

Resistance happens by a few canonical molecular routes.

**Point mutation in the PBP active site.** Substitutions in PBP2x and PBP2b of *Streptococcus pneumoniae* lower the affinity of the active-site pocket for the antibiotic without breaking the enzyme's transpeptidase function. Each substitution is a point mutation from Chapter 8; selection from Chapters 9 and 10 picks the ones that work.

**Acquisition of an altered PBP.** *Staphylococcus aureus* acquired *mecA*, encoding PBP2a, an alternative transpeptidase with vastly reduced β-lactam affinity. PBP2a does the cross-linking job that the methicillin-targeted native PBPs can no longer perform under drug pressure. *mecA* sits on a mobile genetic element, SCC*mec*, that integrates into the chromosome at a defined site — a gene acquired by horizontal transfer, not evolved by point mutation.

**Production of a β-lactamase.** Instead of protecting the target, destroy the antibiotic. The β-lactamases hydrolyze the β-lactam ring, opening it and inactivating the drug. Over 200 TEM variants are now catalogued; each variant differs from the last by a handful of substitutions that expand the substrate range to newer cephalosporins. The TEM family is the textbook example of iterative adaptive evolution under repeated waves of antibiotic selection. NDM-1 uses a zinc cofactor rather than a serine and so is unaffected by the inhibitors that work on serine β-lactamases. It sits on a plasmid that jumps between Enterobacteriaceae. The gene whose name was invented within a living person's lifetime.

### The selective sweep

When a cell carrying a resistance allele finds itself at a bactericidal antibiotic concentration, the susceptible neighbors have fitness near zero; the resistant cell has fitness near one. The selection coefficient $s$ — the fitness advantage of resistant over susceptible — is close to 1. There are very few real-world selection coefficients this large outside the test tube.

In a population of effective size $N_e$, a beneficial allele that escapes initial drift loss reaches fixation in approximately:

$$T_{fix} \approx \frac{2}{s} \ln(2 N_e)$$

For a bacterial gut population with $N_e \approx 10^9$ and $s = 1$:

$$T_{fix} \approx 2 \times \ln(2 \times 10^9) \approx 2 \times 21.4 \approx 43 \text{ generations}$$

At 30 minutes per generation under good conditions: **fixation in roughly 22 hours.** The susceptible strain that filled a patient's gut yesterday is replaced by a resistant strain today, before the next dose of antibiotic has worn off. A clinician with a Petri dish and a course of antibiotics is running a selective sweep on the floor of the ward.

For comparison: the lactase persistence sweep in human populations has $s \approx 0.05$ and $N_e \approx 10^4$. Then $T_{fix} \approx (2/0.05) \times \ln(2 \times 10^4) \approx 40 \times 9.9 \approx 400$ generations. At 25 years per generation: **10,000 years.** The same equation, the same machinery, six orders of magnitude apart on the time axis.

### Horizontal gene transfer — gene flow without reproduction

Chapter 10 introduced gene flow as movement of alleles between populations through migration and reproduction. Bacteria do not respect this framework.

**Transformation**: a bacterium takes up naked DNA released by lysed cells and incorporates it into its chromosome. The 1928 Griffith experiment — virulent pneumococcus in heat-killed form transforming live avirulent pneumococcus to kill mice — was a transformation experiment, though no one knew it yet.

**Transduction**: a bacteriophage accidentally packages host DNA into its capsid and carries it to the next cell it infects. Phages are everywhere; some marine ecosystems have roughly $10^7$ phages per milliliter.

**Conjugation**: direct cell-to-cell transfer through a protein pilus, mediated by a plasmid. One bacterium extends a pilus, contacts a recipient, and threads a copy of the plasmid through. A single IncF plasmid can carry resistance to five antibiotic classes simultaneously. *One transfer event can move resistance to five drug classes at once.*

**Conjugation is gene flow without reproduction.** A new bacterium does not have to be born for the resistance gene to spread. Alleles move between living cells, between species, inside one patient's colon. This breaks the Mendelian framework — which assumes alleles move only through gametes between compatible species. Bacterial population genetics is the more general framework; Mendelian inheritance is its special case.

### Fitness cost and compensatory mutation

Many resistance mutations carry a fitness cost in the absence of antibiotic. PBP2a cross-links less efficiently than native PBPs; MRSA grows slower in antibiotic-free medium than susceptible *S. aureus*. Why doesn't resistance disappear once antibiotic use stops?

The toy model. Suppose the resistance allele R has fitness 0.8 in antibiotic-free medium — a 20% cost. A **compensatory mutation** C arises elsewhere in the genome. C has fitness 1.0 on the R background (fully restores the cost) but fitness 0.9 on the wild-type background (mildly deleterious alone). The joint genotype R+C has fitness 1.0. The compensated resistant strain has lost its cost. There is no longer any force returning the population to wild-type, because R+C is not at a disadvantage anywhere. The compensated resistant strain is stable indefinitely. Withdrawing antibiotic use rarely leads to disappearance of resistant strains — resistance is locked in by compensation, and selection no longer cares.

**Antibiotic stewardship is evolutionary management.** Restricting antibiotic use to cases that need it, using the narrowest spectrum that works, treating for the shortest effective duration, rotating drug classes — this is the same logic that fishery managers use to avoid evolutionary overharvesting. Each time we use an antibiotic, we accelerate the evolution of resistance to it. The total useful lifetime of meropenem in clinical medicine is set by how aggressively we use it. The mechanism is the chapter. The chapter is the policy.

---

## Case 2 — Human population genetics

### Out of Africa, with a bottleneck

Every present-day non-African human population descends from a small group that left Africa roughly 60,000–70,000 years ago. The genomic signal is striking. At any given polymorphic site, **the alleles present in non-African populations are a subset of the alleles present in African populations**. Genome-wide heterozygosity decreases approximately monotonically with geographic distance from East Africa, reaching minima in Native American and remote Pacific Island populations.

This is the **serial-founder pattern**. As the ancestral non-African population dispersed, each new founding subpopulation carried only a subset of the previous population's genetic diversity, losing a bit more variation at each step. The cumulative effect is that distance-from-Africa correlates negatively with within-population genetic diversity — one of the cleanest demographic signals in any species' population genetics. The bottleneck effective population size inferred from whole-genome analyses is in the few thousands — which is an *effective* size, not a census, but it tells you drift was loud in those generations.

Many allele-frequency differences between non-African and African populations reflect drift from that bottleneck, not selection. Confusing drift with selection is one of the most common interpretive errors in human population genetics, and Chapter 10's Hardy-Weinberg derivation gave you the tools to avoid it.

### Founder effects in named populations

**Ashkenazi Jews** carry elevated carrier frequencies for Tay-Sachs (~1/30 in Ashkenazim vs. ~1/300 generally), Gaucher disease (~1/10–15), and several other lysosomal storage disorders. Demographic analysis dates the relevant bottleneck to roughly 1100–1400 CE, with a small number of founders followed by endogamy.

**Old Order Amish of Lancaster County** have an Ellis-van Creveld syndrome frequency of about 1 in 200 — roughly 300-fold elevated — traceable by genealogy to a single ancestral couple, Samuel King and his wife, who carried the *EVC* mutation. This is the canonical clean case: founder effect by genealogy.

**Finnish disease heritage** — roughly 40 rare recessive disorders at 10–100× elevated frequency. Two bottlenecks: initial Finnish settlement ~2,000 years ago, and an internal late-medieval contraction as a small population expanded to colonize the interior.

The teaching point is the same in all three cases. Drift is not a punishment for inbreeding. It is a statistical fact about small samples. When a small number of individuals are the ancestors of a large later population, the random allele sample they happened to carry becomes the founding gene pool. Some recessive disease alleles end up at elevated frequency by chance, not by any advantage they confer. The phenomenon is a *measurement* about a demographic history, not a moral judgment about a group.

### Recent selection in human populations

**Lactase persistence.** A regulatory variant at position −13910 upstream of *LCT* keeps the gene transcribed throughout adult life. The European T allele at this site shows one of the strongest selection signals ever documented in the human genome — estimated selection coefficient 0.05–0.10, selective sweep within the last 5,000–10,000 years. Tishkoff et al. 2007 *Nature Genetics* showed that in African pastoralist populations — Maasai, Beja, Tutsi — the same biochemical outcome (adult lactase expression) is conferred by *three different SNPs* on different haplotypes in the same *MCM6* enhancer. At least four independent mutations, same regulatory element, same selective pressure, different continents.

This is one of the cleanest cases of **convergent evolution at a regulatory element** in any organism. The protein-coding sequence of lactase did not need to change; what changed is the enhancer module deciding when *LCT* gets transcribed. The same module is the available target in multiple populations because regulatory modularity makes it the natural unit of evolutionary modification — exactly the King and Wilson 1975 prediction, and exactly what Chapter 13 showed in sticklebacks.

**Malaria resistance.** Already fully worked below in the sickle-cell example. To add here: malaria has driven multiple independent adaptations. G6PD deficiency (X-linked, multiple variant alleles) confers partial protection. α-thalassemia and β-thalassemia are widespread in Mediterranean, Middle Eastern, and Southeast Asian populations. Hemoglobin C is common in West Africa. Duffy antigen negativity — a regulatory mutation eliminating DARC expression on red cells — is near-fixation in sub-Saharan Africa and protects against *Plasmodium vivax* invasion. The pattern: same selecting agent (malaria), different molecular routes to protection, often with significant homozygote costs maintaining balanced polymorphism. Convergent evolution to the same pathogen, several different addresses in the genome.

**High-altitude adaptation.** Tibetans, Andean populations, and Ethiopian highlanders have each independently evolved adaptations to chronic high-altitude hypoxia, via different loci and different physiological strategies. The Tibetan story is the cleanest: EPAS1 (encoding HIF-2α, a hypoxia-induced transcription factor) is the major locus under selection. Huerta-Sánchez et al. 2014 *Nature* showed that the Tibetan EPAS1 haplotype was **introgressed from Denisovans**. The ancestors of modern Tibetans interbred with Denisovans in central Asia tens of thousands of years ago; the Denisovan EPAS1 variant was advantageous at altitude; selection retained it. Today ~80% of Tibetan EPAS1 haplotypes carry this archaic variant. *A high-altitude adaptation acquired from an extinct cousin species who already had it.*

### Race, ancestry, and population structure — the careful framing

Two claims are both true, and both must be held simultaneously without collapsing one into the other.

**Population structure is real and medically relevant.** Allele frequencies differ on average across populations. APOL1 G1 and G2 variants associated with chronic kidney disease are at >20% frequency in West African populations and near zero in non-Africans; they are clinically relevant for kidney disease risk and transplant outcomes. CYP2C19 rapid/slow metabolizer alleles affect clopidogrel dosing. Sickle-cell carrier frequencies differ by an order of magnitude between West African and Northern European populations. Population structure is medically real.

**Race as a social category does not map cleanly onto biological clusters.** Lewontin 1972 found that approximately **85% of human genetic variation is within populations**, about 15% between. Modern whole-genome data confirm this apportionment. Human autosomal FST between major continental groups is roughly 0.10–0.15. FST = 0 means no between-group differentiation; FST = 1 means complete differentiation. Human FST of 0.10–0.15 is *low* compared to most species; it means 85–90% of human variation is *within* populations, not between them. Knowing a person's continental population assignment tells you very little about their specific genotype.

These two claims are not in tension. Both are true. The synthesis: population structure exists and is detectable; the clusters are continuous gradients rather than discrete boundaries; any specific variant's frequency is a statistical statement about a distribution, not a verdict on an individual; race is a social category that approximately tracks some ancestry signals but is not itself a biological natural kind; and the clinical move is increasingly to replace race as a proxy with direct ancestry estimation from genetic data. *Race is a social category. Ancestry is a continuous genetic gradient. Population structure is a biological phenomenon.* They correlate; they are not the same thing.

### The sickle-cell worked example — end to end

The HbS allele is a single-nucleotide substitution at codon 6 of β-globin: GAG (glutamic acid) → GTG (valine). One A becomes one T in the DNA template; the messenger RNA changes one letter; a different tRNA is loaded; the β-globin protein has valine at position 6 instead of glutamic acid. Valine is hydrophobic. Glutamic acid is charged and hydrophilic. In deoxygenated T-state hemoglobin, the valine of one tetramer fits into a complementary hydrophobic pocket on a neighboring tetramer. Tetramers polymerize into long fibers. Red blood cells distort from flexible biconcave discs into rigid sickles, clog small vessels, cause pain crises, damage organs, shorten lifespan.

HbA/HbS heterozygotes are clinically nearly normal and have substantial protection against severe *Plasmodium falciparum* malaria. From Chapter 10's Hardy-Weinberg under selection, with heterozygote fitness 1, homozygous-normal fitness $1 - t$, and homozygous-sickle fitness $1 - s$, the equilibrium HbS allele frequency is:

$$p_S^* = \frac{t}{s + t}$$

In historical West African malaria-endemic populations, with $t \approx 0.1$ (malaria mortality penalty for non-carriers) and $s \approx 0.5$ (disease cost in homozygotes without modern care):

$$p_S^* = \frac{0.1}{0.5 + 0.1} = 0.167$$

Much of West and Central Africa shows allele frequencies of 0.08–0.16 — close to this theoretical equilibrium. In African Americans, after roughly 15 generations of relaxed $t$ (no malaria in North America since the 19th century), the frequency has dropped to about 0.04 — predictable from selection-relaxation arithmetic over 350 years.

The HbS allele has arisen at least five times independently across malaria-endemic populations, on five different chromosomal haplotype backgrounds — Bantu, Benin, Senegal, Cameroon, Arab-Indian — each with the same A→T at HBB codon 6 sitting on different surrounding sequence contexts. The same point mutation, the same phenotype, the same selection pressure, in different populations. Convergent evolution at the level of identical mutations in separate populations.

Victoria Gray received the first FDA-approved CRISPR therapy for sickle-cell disease in 2023 (exa-cel, Casgevy). Cas9 ribonucleoprotein was electroporated into her bone marrow stem cells *ex vivo*; the guide RNA directed Cas9 to disrupt the BCL11A erythroid enhancer; her edited stem cells were reinfused; her erythroid lineage now expresses fetal hemoglobin at levels sufficient to outcompete HbS polymerization. The mutation she carries is a one-base substitution in a Chapter 5 gene. The genetics of her disease is Chapter 10. The population genetics that made her allele common is Chapter 10 and 13. The engineering that cured her is Chapter 7. Four billion years of evolution that started with a bacterium swallowing another bacterium reached, in 2023, a woman in Mississippi who no longer has sickle-cell disease.

---

## Case 3 — The molecular basis of human evolution

### How much of the genome differs

Humans and chimpanzees share approximately 98.8% of protein-coding DNA in alignable regions. Indels account for another ~3%. Lineage-specific duplications and structural variants account for several more percent. The most inclusive measure of divergence is roughly 4–5%. The 98.8% figure is correct for what it measures — single-nucleotide identity in alignable coding regions — and misleading as a summary of total genomic difference.

More importantly: very few of the human-chimp coding differences are obviously functional. King and Wilson 1975 *Science* proposed this before anyone had a genome: if protein-coding sequences are this similar but the two species are this different, then most evolution must be in regulatory DNA. Fifty years of subsequent data have largely vindicated the inference. Most of what makes us different from chimps is not in the coding differences. It is in the regulatory elaboration those small percentages hide.

### Human Accelerated Regions

Pollard et al. 2006 *Nature* introduced **Human Accelerated Regions (HARs)** — genomic regions that are highly conserved across vertebrates (slow molecular clock, strong purifying selection) but show accelerated substitution rates specifically on the human lineage since the human-chimp split. Regions under conservation across hundreds of millions of vertebrate evolution have functions that purifying selection has maintained; regions where the human branch suddenly accelerated are candidates for functional changes specific to our lineage.

**HAR1** is the most accelerated of the original set — a 118-bp region containing part of a non-coding RNA gene, *HAR1F*, expressed specifically in Cajal-Retzius neurons in the developing human neocortex between gestational weeks 7 and 19, a window critical for cortical layering. HAR1 has 18 substitutions on the human lineage versus 2 on the chimp lineage; under neutral evolution the expected count would be about 0.27. The substitution rate is ~70× faster than neutral expectations. Subsequent work has shown that many HARs function as developmental enhancers in the developing human cortex. The changes are largely regulatory.

### FOXP2 — the textbook story, revised

The 2002 Enard et al. paper proposed: FOXP2 has two human-derived amino acid substitutions; the KE family with disrupted FOXP2 has severe speech and orofacial motor deficits; a selective sweep on FOXP2 within the past 200,000 years drove these substitutions in modern humans. The story circulated as "FOXP2 is the language gene that evolved 200,000 years ago."

Three subsequent findings have revised both halves.

**Neanderthals share the substitutions.** Krause et al. 2007 *Current Biology* recovered FOXP2 sequence from a Neanderthal specimen and found that *Neanderthals carry both derived substitutions*. The changes predate the human-Neanderthal split — at least 500,000–700,000 years old, not 200,000. They are not specific to modern humans.

**The selection signal does not survive larger samples.** Atkinson et al. 2018 *Cell* re-examined the population genetics of FOXP2 in a much larger, more diverse sample with updated demographic models. The apparent selection signal from Enard 2002 does not survive. The original signal was probably a demographic artifact of limited sampling.

**FOXP2 is a transcription factor with many downstream targets.** Disruption produces severe speech and orofacial *motor* deficits, not loss of language per se. Calling FOXP2 "the language gene" was shorthand that became distorting.

The chapter's framing: FOXP2 is a useful example of how the field corrects itself. The original result was foundational; it got enormous media attention; subsequent data have revised the interpretation in two specific ways. The dN/dS calculation from Chapter 13 still works as a methodological tool. The lesson is that "X is the gene for Y" claims in human evolution should be greeted with skepticism, especially when X is a transcription factor and Y is a complex cognitive trait.

### NOTCH2NL and cortical expansion

Fiddes et al. 2018 and Suzuki et al. 2018 *Cell* characterized human-specific paralogs — NOTCH2NLA, NOTCH2NLB, NOTCH2NLC — that arose by partial duplication from the parental NOTCH2 gene in the hominin lineage roughly 3–4 million years ago. NOTCH2NL paralogs are expressed in radial glia in the developing human neocortex; they delay neural progenitor cell differentiation, prolong the proliferative phase, and increase total neuron output. Knockdown in human cortical organoids reduces neuron output.

The remarkable feature: **the same chromosomal instability that enabled the human-specific innovation continues to generate disease today**. The NOTCH2NL locus at 1q21.1 is unstable — recurrent deletions cause microcephaly and increased risk of schizophrenia; recurrent duplications cause macrocephaly and increased risk of autism. The duplication architecture that made the locus available for evolutionary innovation also makes it fragile in present-day individuals. *The same molecular event runs in both directions — adaptive innovation 3 million years ago, disease syndrome today.* This is the cleanest case in human evolutionary genetics of an innovation persisting as disease through the chromosomal architecture that made it possible.

### The Neanderthal genome — what it tells us

Non-African modern humans carry roughly 1–4% Neanderthal ancestry, distributed across the genome in detectable haplotype blocks. Africans carry essentially zero. The interbreeding occurred shortly after the out-of-Africa dispersal, probably in the Middle East, between ~50,000 and 60,000 years ago.

The D-statistic (ABBA-BABA test) compares allele-sharing patterns across four populations to test for excess derived-allele sharing with Neanderthals. The test is positive in non-Africans and zero in Africans; the excess sharing is not explained by any demographic model that doesn't include hybridization. Sankararaman et al. 2014 *Nature* showed that pooled across many non-African individuals, roughly 40% of the Neanderthal genome can be reconstructed from present-day humans.

Neanderthal ancestry is **depleted on the X chromosome** and near genes in present-day humans — consistent with weak but pervasive purifying selection against Neanderthal-derived alleles after introgression. But selected cases were retained: EPAS1 in Tibetans (worked in Case 2), HLA class I alleles broadening the human immune repertoire, keratin loci possibly involved in cold-climate adaptation, toll-like receptor variants tuning innate immune responses. Some Denisovan ancestry, contributing ~5% to Melanesian and Australian Aboriginal genomes, contributed the EPAS1 haplotype.

The synthesis: **speciation is not always reproductively complete.** Neanderthals and modern humans were morphologically and probably behaviorally distinct, geographically separated for hundreds of thousands of years, and yet not fully reproductively isolated. The biological species concept from Chapter 11, applied strictly, would call them one species; common usage calls them two; the genomes say they interbred during a window of contact and the offspring were fertile enough to leave detectable ancestry in populations living today. The species concept stretches at the edges. The Pääbo data are the cleanest mammalian case where it stretches.

Pääbo won the 2022 Nobel Prize in Physiology or Medicine "for his discoveries concerning the genomes of extinct hominins and human evolution." Every tool the Nobel cited — ancient DNA recovery, contamination filtering, population-genetic inference of admixture — required all thirteen prior chapters of this book.

---

## What every chapter contributed

This is the synthesis: every chapter contributed a piece of machinery that the three cases require. Reading them back into the cases is the integrative move.

**Chapter 1 (meiosis)**: the Neanderthal ancestry blocks' lengths are a molecular clock because recombination shortens them every generation. Block length = 1/(recombination rate × time). Without meiosis, there is no block.

**Chapter 2 (Mendel)**: Hardy-Weinberg is Mendel extended to populations. The sickle-cell equilibrium frequency is Mendel with non-equal fitnesses. The 3:1 ratio is the null from which all three cases deviate in named ways.

**Chapter 3 (complex inheritance)**: polygenic traits, penetrance, epistasis. The GWAS architecture of height and educational attainment is complex inheritance at population scale.

**Chapter 4 (DNA)**: mutation rates are the inputs to every selection calculation. Ancient DNA's cytosine-to-uracil deamination is the damage chemistry of Chapter 4 applied to 50,000-year-old bones.

**Chapter 5 (gene to protein)**: the A→T at HBB codon 6 changes a codon, changes a tRNA, changes an amino acid, changes a protein surface, changes a cellular phenotype. Five steps connecting one base to one clinical outcome. Every translational therapy in this book lives in Chapter 5's substrate.

**Chapter 6 (regulation)**: lactase persistence is a regulatory variant. HAR1 is a non-coding RNA expressed through regulatory machinery. Casgevy works by editing the BCL11A erythroid enhancer. Most of what evolves in mammalian morphology is not what proteins are; it is when and where they are made.

**Chapter 7 (biotechnology)**: the Pääbo genome was assembled with next-generation sequencing. The Murray AMR estimate was built from genomic surveillance databases. Casgevy is CRISPR therapy. Without Chapter 7's tools, none of the three cases would be possible.

**Chapter 8 (mutation and cancer)**: cancer is somatic evolution — the same clonal expansion math as Case 1's selective sweep, working in one body on somatic cells instead of a hospital ward on bacterial cells. Mutation in the germline is Case 2 and Case 3. Same event, two fates.

**Chapter 9 (evolution and speciation)**: the four prerequisites of natural selection — variation, excess offspring, differential reproduction, time — are present in all three cases. The mode-of-selection vocabulary. The species concept stretched at the Neanderthal edge.

**Chapter 10 (population genetics)**: Hardy-Weinberg as the null; the five forces as the deviations; the fixation-time equation; FST; the sickle-cell equilibrium. Chapter 10 is the quantitative apparatus that the capstone uses most heavily.

**Chapter 11 (speciation)**: Neanderthal-modern human admixture is the cleanest mammalian case where the BSC stretches at the edges. Speciation is a process, not always a completed event.

**Chapter 12 (phylogenetics)**: the molecular clock dates the events. The tree-building methods place the lineages. Ancient DNA pushes the resolvable tree back to specific specimens with specific dates.

**Chapter 13 (molecular evolution)**: dN/dS identifies the coding changes that matter. Selective sweeps carve diversity valleys. Gene duplication produces NOTCH2NL. Regulatory evolution produces the lactase enhancer. The chapter's machinery is what every "recently selected in humans" claim is testing.

---

## The closing thought

Pääbo's lab took three Neanderthal bones from a cave in Croatia and reconstructed a 3-billion-base-pair genome, and the genome told us that we — non-African modern humans — are partial hybrids of an extinct hominin lineage. He won the Nobel for it. A patient walks into an ICU with a *Klebsiella* infection and NDM-1. The antibiotic that worked five years ago does not work today. A Maasai pastoralist, a Dutch pastoralist, and a Beja pastoralist each drink milk as adults, and the regulatory variant that allows each of them to do it is a different mutation in the same enhancer module of the same gene.

Three cases. Three timescales. Same machinery.

Every chapter of this book has been the same algorithm at a different scale. Mutation. Drift. Selection. Gene flow. The chapters are not separate subjects with different equations; they are different *applications* of one mechanism stack. The bacterial culture, the human pedigree, and the hominin lineage are all running the same algorithm with different parameters.

*Genetics is evolution one generation at a time. Evolution is genetics many generations at once.*

You inherited a four-billion-year-old algorithm and ran it forward for one generation more, with your own substitutions, your own recombinations, your own meioses. Some of what you inherited came from Neanderthals. Some came from Denisovans, if you have Pacific ancestry. Some came from a bacterium that swallowed another bacterium four billion years ago and turned it into a mitochondrion. The algorithm has been running continuously since then.

*You are the algorithm's most recent line of output.*

The next line is up to your gametes and whatever they encounter. The chapters are over. The mechanism is yours.

---

## LLM exercises

The following exercises are designed for use with a large language model. Paste the prompt into any capable model and examine the response critically — not for whether it sounds confident, but for whether the reasoning is mechanistically grounded and correctly identifies which chapter's machinery applies.

**Exercise 1 — Selective sweep timescale comparison**
Prompt: *"Using the fixation-time equation T_fix ≈ (2/s) × ln(2 N_e), compare the time for a resistance allele with s=1 to sweep through a bacterial population (N_e = 10^9, generation time = 30 minutes) versus the time for a lactase-persistence allele with s=0.07 to sweep through a human pastoralist population (N_e = 10^4, generation time = 25 years). (a) Compute T_fix in generations for each. (b) Convert to real time units (hours for bacteria, years for humans). (c) Explain what population parameters produce the roughly million-fold difference in real time. (d) In both cases, what has to happen before the fixation calculation even begins — what must the allele 'survive' to enter the sweep phase?"*

Evaluate whether the model correctly computes ~43 bacterial generations (~22 hours) and ~400 human generations (~10,000 years); identifies N_e and generation time as the dominant parameters; and correctly addresses genetic drift as the initial barrier — the allele must escape stochastic loss when rare before deterministic selection takes over.

**Exercise 2 — Balanced polymorphism versus hard sweep**
Prompt: *"The HbS (sickle cell) allele in West Africa sits near equilibrium at ~15% frequency; the lactase-persistence allele in European pastoralists has been sweeping toward fixation. Both alleles are under positive selection in their respective populations. (a) Explain mechanistically why one reaches a stable intermediate frequency and the other sweeps to fixation. (b) Compute the expected HbS equilibrium frequency given s(SS) = 0.5 (sickle-cell disease cost) and t(AA) = 0.10 (malaria cost to homozygous-normal). (c) What would happen to the HbS frequency in a West African population that eliminated malaria completely? Show the reasoning. (d) What does the HbS story tell you about why recessive disease alleles can persist at high frequency in a population — is it always genetic drift?"*

Evaluate whether the model correctly identifies that HbS is under balancing selection (heterozygote advantage maintaining both alleles) while lactase persistence is under directional selection (one allele strictly better than the other); correctly computes p* = 0.1/(0.5+0.1) ≈ 0.167; correctly predicts that removing malaria removes t, so the new equilibrium collapses toward zero (only the s term remains, disfavoring HbS); and explains that high-frequency recessive alleles can reflect either drift (founder effects) or selection (heterozygote advantage) — the two need to be distinguished.

**Exercise 3 — FST interpretation**
Prompt: *"Human autosomal FST between continental populations is approximately 0.10–0.15. (a) Explain in plain language what FST measures and what FST = 0.12 means about the distribution of genetic variation within versus between populations. (b) FST of 0.12 is lower than FST between subspecies of chimpanzee (which can reach 0.30+). What does this tell you about human demographic history? (c) A journalist writes: 'Genetic differences between races are real, as shown by the FST values.' A second journalist writes: 'There are no meaningful genetic differences between races, since 85% of variation is within populations.' Explain what is wrong with each framing, and give the more accurate synthesis. (d) For which medically relevant question would FST = 0.12 be large enough to matter, and for which would it be essentially irrelevant?"*

Evaluate whether the model correctly explains FST as the fraction of total variance between groups (0.12 means 12% between, 88% within); correctly notes that low human FST compared to other primates reflects a recent common ancestry and/or bottleneck history; correctly identifies that both journalistic framings are partially wrong (population structure is real and detectable, but most variation is within populations and race doesn't map cleanly to discrete biological clusters); and gives a concrete example where FST-level differences matter clinically (APOL1, sickle cell, pharmacogenomics) versus where they don't (height, most complex traits where polygenic architecture means within-population variance dominates).

**Exercise 4 — Ancient DNA and the species concept**
Prompt: *"Non-African modern humans carry approximately 2% Neanderthal ancestry on average, detectable as haplotype blocks distributed across the genome. (a) How does the D-statistic (ABBA-BABA test) work, and what pattern would you expect to see in a population with zero Neanderthal ancestry versus 2% Neanderthal ancestry? (b) Why are the Neanderthal-derived haplotype blocks shorter in present-day humans than they would have been immediately after the hybridization event? What does average block length tell you about timing? (c) The biological species concept defines a species as populations that are reproductively isolated from each other. Evaluate whether modern humans and Neanderthals were one species or two, given the admixture evidence. (d) Neanderthal ancestry is depleted on the X chromosome relative to autosomes, and depleted near genes. What evolutionary force best explains this pattern?"*

Evaluate whether the model correctly explains ABBA-BABA as a test for asymmetric allele sharing (excess derived allele sharing between test population and Neanderthal relative to an African reference suggests admixture); correctly explains block shortening through recombination as a molecular clock (longer elapsed time = shorter average blocks); correctly identifies that the BSC gives an ambiguous answer here (the populations were distinct but not fully isolated, consistent with the BSC's known limits for hybridizing taxa); and correctly identifies purifying selection as the explanation for depletion near genes (Neanderthal-derived alleles that were mildly deleterious in the modern human genetic background were gradually removed by selection, with autosomal depletion > X because hemizygous X alleles are immediately exposed to selection in males).

**Exercise 5 — Integrative case: convergent regulatory evolution**
Prompt: *"Lactase persistence in humans and the pelvic spine reduction in stickleback fish (from Chapter 13) have both been cited as examples of convergent regulatory evolution. (a) For each case, describe the molecular mechanism — what specific regulatory change occurred, in what gene or regulatory element, and what was the phenotypic result? (b) Why do both cases involve regulatory rather than coding changes? What property of regulatory elements makes them the 'preferred' target of repeated selection in different populations? (c) Both cases involve the same regulatory element being independently modified in multiple populations. What does this suggest about the structure of the genotype-phenotype map for complex traits? (d) Lactase persistence has risen toward fixation in European and African pastoralist populations within the last 10,000 years. Using the selective-sweep framework, estimate roughly how strong selection would need to be to achieve this from an initial frequency of 1% in 400 generations. Show the reasoning."*

Evaluate whether the model correctly describes lactase persistence (MCM6 intron enhancer variants keeping LCT active) and stickleback (Pitx1 pelvic enhancer deletion reducing hind limb development); correctly explains that regulatory modularity means cis-regulatory elements control specific tissues/times, so modifying them changes one trait without pleiotropic coding consequences; correctly infers that repeated independent targeting of the same element suggests it is the most 'accessible' or 'least costly' target for this particular phenotypic change; and attempts the selection-strength calculation using Δp ≈ s·p·(1−p) or the fixation-time equation in reverse, recovering s in the range 0.05–0.10 consistent with published estimates.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Svante Pääbo** began his career in paleoanthropology trying to extract DNA from Egyptian mummies in the 1980s — mostly contamination. The path from those failed mummy experiments to a Nobel Prize in 2022 is one of the more remarkable stories in modern science.

**Run this:**

```
Who is Svante Pääbo, and how does his work on ancient DNA and
Neanderthal genomes connect to the genetics and evolution concepts
in this capstone chapter? Keep it to three paragraphs. End with
the single most surprising thing about his career, his methods,
or what the Neanderthal genome revealed.
```

→ Search **"Svante Pääbo Nobel Prize"** on Wikipedia. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain what cytosine deamination is, why ancient DNA is full of it, and how Pääbo's lab developed chemical and computational methods to distinguish authentic ancient DNA from modern contamination.
- Ask it about the Denisovans specifically — what was unusual about the discovery, what we know about their range and biology, and why a single finger bone led to a complete genome.

What changes? What gets better? What gets worse?

---

*By Nik Bear Brown*
