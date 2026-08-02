# Chapter 12 — Phylogenetics and the History of Life: Reading the Tree from the Speciation Events That Built It

## TL;DR

- The tree saw what the microscope could not.
- The chapter moves through How to read a tree without misreading it, Three ways to build a tree, Worked example — building a primate phylogeny from a short sequence, The three domains and the last universal common ancestor, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The tree saw what the microscope could not.*

---

In 1977, Carl Woese and George Fox published a five-page paper in *PNAS* with a deceptively quiet title: "Phylogenetic structure of the prokaryotic domain: The primary kingdoms." The paper reported that a class of microbes called methanogens — anaerobic single-celled organisms that respire by converting hydrogen and carbon dioxide into methane, found in cow rumens, swamp sediments, and the gut of every termite on Earth — were not bacteria.

The methanogens *looked* like bacteria. They had no nucleus, no mitochondria, no organelles. Under a microscope they were small, simple, prokaryote-shaped cells. Every textbook in microbiology placed them inside the prokaryotic kingdom alongside *Escherichia coli* and *Bacillus subtilis*.

Woese's evidence was a single molecule. The 16S ribosomal RNA — the structural RNA at the core of the bacterial ribosome, about 1,540 nucleotides long, performing the same job in every prokaryotic ribosome on Earth — turned out to look fundamentally different in methanogens than in *E. coli*. Woese had developed a laborious technique called oligonucleotide cataloguing: he digested 16S rRNA with a ribonuclease, separated the resulting short fragments by two-dimensional electrophoresis, and sequenced them by hand. By 1976 he had cataloged about 60 species' worth of rRNA fragments. Methanogens shared fewer fragments with *E. coli* than *E. coli* shared with human mitochondrial rRNA. The methanogens were as distantly related to typical bacteria as bacteria were to anything in the eukaryotic world.

The conclusion was not subtle. Life was not divided into prokaryotes and eukaryotes. Life was divided into three lineages of approximately equal evolutionary depth: the typical bacteria (**Bacteria**), the methanogens-and-relatives (**Archaea**), and the nucleated cells (**Eukarya**). The Archaea were as different from the Bacteria as either was from us. A century of textbooks was wrong at the deepest level the tree had.

Woese met enormous resistance. Salvador Luria — a Nobel laureate, the dean of American molecular biology — reportedly called Woese personally to demand he stop talking about a third kingdom. The microbiology establishment did not adopt the three-domain framework for nearly twenty years. The textbooks did not rewrite their introductions until the 1990s.

Here is the thing that matters for this chapter. *Woese never looked at a methanogen under a microscope and decided it was not a bacterium.* He could not have made the discovery that way. The methanogens are not visibly different from typical bacteria. The discovery was made by inference from a tree. Woese built a phylogenetic tree from 16S rRNA sequence data, applied the tree to the question "where do methanogens sit?", and got back an answer that contradicted every textbook. The tree saw what the microscope could not.

This is what phylogenetics does. It takes evidence that is local and present-tense — sequences in a database, characters scored on living specimens, fossils dated in rock columns — and infers history. Every branch on a phylogenetic tree is a hypothesis about who descended from whom. The methodology that produced Woese's conclusion has since shown us that whales are nested inside the artiodactyls, that birds are dinosaurs, that fungi are closer to animals than to plants, and that the human genome contains about 2% Neanderthal DNA inherited from a hybridization event roughly 60,000 years ago. None of these are visible to inspection. All of them are visible to phylogenetic inference.

The chapter walks the inference. Then it walks the tree — the four-billion-year history the methodology has revealed. Then it walks the limits — where the tree metaphor breaks down and what we use instead.

---

## How to read a tree without misreading it

Before we can build trees, we need to read them. This sounds trivial; it is not. A 2003 study found that about half of upper-level biology students could not correctly answer basic tree-reading questions on a published phylogeny. The mistakes are easy to make because trees look like simple drawings. The drawing carries a lot of information; misreading any piece of it produces a wrong claim about history.

A phylogenetic tree is a branching diagram representing inferred evolutionary relationships. Six features carry information.

**Tips** are the endpoints — the taxa the tree was built from. **Internal nodes** represent hypothetical common ancestors. The node linking chimpanzees and humans represents the population from which both descended roughly 6 million years ago. **Branches** connect nodes to other nodes or to tips; their length can encode time, evolutionary change, or nothing at all depending on whether the tree is a chronogram, a phylogram, or a cladogram. Always check the caption. **The root** is the most recent common ancestor of everything in the tree; it polarizes the branching so you know which way evolution ran. A tree without a root (an *unrooted tree*) shows topology but not direction. **Sister groups** are taxa that share a more recent common ancestor with each other than either shares with anything else in the tree. **Clades** — an ancestor plus all of its descendants — are the natural unit of evolutionary biology.

Three kinds of group, only one of which is real. A **monophyletic group** is an ancestor plus all its descendants: mammals, birds, primates. It is the thing the tree picks out as a real grouping — there is no biological grouping more fundamental than "a population's complete descendant set." A **paraphyletic group** is an ancestor plus *some but not all* descendants. "Reptiles" in the traditional sense — lizards, snakes, turtles, crocodiles, excluding birds — is paraphyletic; crocodiles are more closely related to birds than to lizards, so the traditional "reptile" category drops out one whole descendant branch. "Fish" is paraphyletic; every tetrapod is technically a lobe-finned fish. A **polyphyletic group** gathers members from different ancestors based on convergent features: "warm-blooded animals" groups mammals and birds, but their common ancestor was ectothermic; endothermy evolved independently in each lineage. Phylogenetic systematics accepts only monophyletic groups as valid biological units. Everything else is useful shorthand layered on top.

Three misreadings recur constantly and deserve specific defusing.

The leftmost or topmost taxon is *not* the most primitive. Trees can be drawn with tips in any order; you can rotate the branches around any internal node without changing what the tree says about relationships. The order of tips along the page is a visual convention, not biology.

"Older lineage" does not mean "more primitive organism." A sponge is not a primitive human. The lineage leading to sponges has been evolving for the same ~600 million years as the lineage leading to humans since their common ancestor. Sponges have changed less morphologically, but their genomes have accumulated mutations at comparable rates. The tree shows order of divergence, not order of complexity.

Humans did not evolve from chimpanzees. Humans and chimpanzees share a common ancestor approximately 6 million years ago, and both lineages have been evolving in parallel ever since. The common ancestor was not a modern chimp. The tree shows a sister relationship, not descent of one from the other.

---

## Three ways to build a tree

Given sequences or characters from a set of taxa, three main approaches infer the most likely tree. Modern phylogenetics typically runs more than one and asks whether they agree.

**Parsimony** prefers the tree requiring the *fewest evolutionary changes* across all branches. Each candidate tree is scored by counting how many character-state changes you must invoke to explain the data; the lowest score wins. The logic is Occam's razor applied to evolutionary inference: one origin event is more parsimonious than two independent ones. If two species share a complex character, the simplest explanation is inheritance from a common ancestor.

Where parsimony fails: when two lineages experience high evolutionary rates on long branches, parsimony can mistakenly group them together based on shared independent changes that happen to look identical — a failure mode called **long-branch attraction**. This was a primary motivation for model-based methods.

**Maximum likelihood** asks: given an explicit probabilistic model of how sequences evolve, which tree topology and set of branch lengths make the observed data most probable? The simplest model — the **Jukes-Cantor model** — treats all twelve possible nucleotide substitutions as equally likely. More elaborate models allow transitions to differ from transversions, allow rate variation across sites, and allow different base frequencies. ML handles long-branch attraction better than parsimony because the model explicitly accounts for the higher probability of convergent change on long branches.

**Bayesian inference** treats the tree itself, the branch lengths, and the model parameters as random variables, and computes the posterior distribution over trees using Bayes' theorem. Because the posterior is not computable in closed form for any real dataset, Bayesian phylogenetics uses Markov chain Monte Carlo (MCMC) sampling to draw a representative sample of trees from the posterior. The support on each node is the **posterior probability** — the fraction of sampled trees that contain that clade. A node with posterior probability 0.95 is found in 95% of the posterior sample.

**Bootstrap support** answers a separate question: how robustly do the data support each node? Resample sites with replacement to create a new alignment of the same size; build a tree from the resampled data; repeat a thousand times; the fraction of resampled trees that recover a given clade is the bootstrap support for that node. Values above 70% are moderate support; above 95% are very strong. Bootstrap support is not the same as the probability the clade is correct — under model misspecification, you can get high bootstrap support for a wrong clade — but it captures how much the result depends on specific sites in the alignment versus the overall signal.

---

## Worked example — building a primate phylogeny from a short sequence

Take four species — human, chimpanzee, gorilla, orangutan — and a 250-base-pair piece of the mitochondrial *COX1* gene. *COX1* is the standard barcode locus for animal species identification and is well-curated in GenBank. Mitochondrial sequences evolve roughly 10× faster than nuclear sequences and accumulate enough variation in a few million years to be informative for primate relationships.

The following pairwise differences are illustrative numbers in the range typical for great-ape *COX1* sequences:

| Pair | Observed differences | Raw p-distance |
|------|---------------------:|---------------:|
| Human – Chimp | 7 of 250 | 0.028 |
| Human – Gorilla | 11 of 250 | 0.044 |
| Human – Orangutan | 22 of 250 | 0.088 |
| Chimp – Gorilla | 11 of 250 | 0.044 |
| Chimp – Orangutan | 22 of 250 | 0.088 |
| Gorilla – Orangutan | 22 of 250 | 0.088 |

The **p-distance** — sites differing divided by total sites compared — underestimates the true number of substitutions per site, because some sites have been hit more than once over evolutionary time. A site that mutated A → C → A appears identical between species today even though two substitutions occurred. A site that mutated A → C → G looks like one substitution but was two. The longer since divergence, the worse the underestimate.

The correction is the **Jukes-Cantor distance**:

$$d_{JC} = -\frac{3}{4} \ln\left(1 - \frac{4}{3}p\right)$$

For the Human–Chimp pair: $p = 0.028$. Compute $1 - \frac{4}{3}(0.028) = 0.9627$. Take $\ln(0.9627) = -0.0380$. Multiply by $-3/4$: $d_{JC} = 0.0285$ — very close to raw p because the divergence is small and multiple hits are rare.

For the Human–Orangutan pair: $p = 0.088$. Compute $1 - \frac{4}{3}(0.088) = 0.8827$. $\ln(0.8827) = -0.1248$. $d_{JC} = 0.0936$ — about 6% higher than the raw p. At still greater divergence, say a human-fish comparison with $p \approx 0.45$, the Jukes-Cantor distance inflates to $d_{JC} \approx 0.85$, nearly double the raw value. *This is why uncorrected p-distances are not used in modern phylogenetics at deep evolutionary distances.*

**Neighbor-joining** takes the corrected distance matrix and joins taxa iteratively: find the pair that minimizes a corrected distance criterion, join them as sisters, replace the pair with a new internal node, repeat. Starting from Human–Chimp (closest at $d = 0.029$), the procedure joins Gorilla next, then Orangutan as the outgroup. The topology:

```
(((Human, Chimp), Gorilla), Orangutan)
```

This is the textbook great-ape topology, recovered from a 250-bp piece of one mitochondrial gene. Real published trees use thousands of base pairs from dozens of genes and converge on the same topology with bootstrap support of 100% at every internal node.

**Molecular clock calibration.** The orangutan–African ape split is conventionally calibrated to about 14 million years ago from Miocene fossil great apes — particularly *Sivapithecus* from Pakistan. The Human–Orangutan corrected distance is $d_{JC} \approx 0.094$. This distance accumulated along *both* lineages from their common ancestor, so per-lineage time is half the total. The substitution rate is:

$$r = \frac{0.094}{2 \times 14 \text{ Ma}} \approx 3.4 \times 10^{-9} \text{ substitutions per site per year}$$

Using this calibrated rate to date the Human–Chimp split:

$$t = \frac{d}{2r} = \frac{0.029}{2 \times 3.4 \times 10^{-9}} \approx 4.3 \text{ million years}$$

The published best estimate of the chimp–human split is 6–7 Ma; the 250-bp worked example undershoots by 2 million years, illustrating the noise in single-gene estimates. The discrepancy is expected: a 250-bp piece of one gene gives a noisy estimate, and the molecular clock assumption (constant rate across lineages) breaks down to some extent over millions of years.

Using the same rate to predict the macaque divergence: the fossil calibration puts Old World monkey/ape divergence at about 25–30 Ma. Predicted distance at 27.5 Ma: $d = 2 \times 3.4 \times 10^{-9} \times 27.5 \times 10^6 \approx 0.19$ substitutions per site, corresponding to a raw p-distance of about 17%. Observed human-macaque divergence in *COX1* is 14–18%. The calibrated clock recovers the macaque divergence approximately.

The deep lesson: phylogenetic inference is statistical inference about history. You start with sequence differences in the present, apply explicit models of how those differences accumulated, and recover both the branching pattern and the timing of the past — with quantifiable uncertainty. The molecular clock is an approximation that works better with more genes, relaxed-clock models that allow rate variation across branches, and multiple fossil calibrations.

---

## The three domains and the last universal common ancestor

Woese's 1977 paper proposed three primary kingdoms; the framework formalized in 1990 calls them three **domains**: Bacteria, Archaea, and Eukarya. The deepest split is between Bacteria on one side and (Archaea + Eukarya) on the other — Archaea are sisters to Eukarya.

The evidence that Archaea and Eukarya are sisters comes from multiple independent lines. Translation machinery — RNA polymerase subunits, initiation factors, ribosomal proteins — is more similar between Archaea and Eukarya than between either and Bacteria. Universal-gene analyses using 30 or more genes present in essentially every cellular organism robustly recover the (Archaea + Eukarya) clade.

The most recent and striking development: the **Asgard archaea**. Discovered from deep marine sediments beginning around 2015 — first described from a hydrothermal vent at Mid-Atlantic Loki's Castle, hence *Lokiarchaeota*, *Thorarchaeota*, *Odinarchaeota*, *Heimdallarchaeota* — this superphylum of uncultured archaea encodes a remarkable number of "eukaryotic signature proteins": actin-related cytoskeletal proteins, small GTPases, ubiquitin-like proteins, ESCRT-III homologs. When universal-gene trees are built with Asgard sequences, the Eukarya emerge from *inside* the Asgard radiation — not as the sister of all Archaea but as a nested branch within Archaea. The first cultured Asgard archaeon, *Prometheoarchaeum syntrophicum*, isolated in 2019–2020 from deep-sea sediment, showed long branching cellular protrusions consistent with the cellular architecture proposed for the archaeon-bacterium fusion event.

The current best phylogenetic reading: eukaryotes are *derived from Archaea* — specifically the Asgard lineage — through an early endosymbiotic event in which an archaeal cell engulfed a bacterium that became the proto-mitochondrion, about 2 billion years ago. The three-domain framework is approximately right with refinement: Archaea is paraphyletic as currently defined, and eukaryotes are a specialized derived archaeal lineage.

**The last universal common ancestor (LUCA).** Trace the three domains back to their root and you reach a population of cells whose descendants are everything alive today. LUCA is conventionally dated to about 3.5–4 billion years ago. Any gene present in all three domains with similar function must have been present in their common ancestor. LUCA had a DNA genome, a ribosome with essentially the universal genetic code, core metabolic pathways (glycolysis, the citric acid cycle), and a membrane — though the lipid chemistry is contested. The 2016 reconstruction by Weiss and colleagues, based on 355 protein families inferred to be present in LUCA, suggests an anaerobic chemolithoautotroph using H₂ and CO₂ — consistent with a hydrothermal vent environment.

---

## Endosymbiosis — how eukaryotes got their organelles

Inside the eukaryotic cell, the deepest history is recorded not by the nuclear genome alone but by the organelles. The **endosymbiotic theory**, developed by Lynn Margulis in a famously rejected 1967 paper (the manuscript was rejected by about fifteen journals before publication): mitochondria are descended from a free-living α-proteobacterium engulfed by an archaeal-or-proto-eukaryotic host cell roughly 1.5–2 billion years ago and gradually integrated as an obligate intracellular organelle. A similar engulfment involving a cyanobacterium gave rise to **chloroplasts** in the lineage leading to plants about 1 billion years ago.

The evidence is unusually direct.

Mitochondria have **double membranes**. The outer membrane is the host-derived phagocytic vesicle; the inner membrane is the original bacterial plasma membrane, including its characteristic cardiolipin lipid composition. The two-membrane architecture is the engulfment event preserved in cell structure.

Mitochondria have **their own circular DNA genome**. Human mitochondrial DNA is a single circular molecule of 16,569 base pairs encoding 13 proteins, 22 tRNAs, and 2 rRNAs. The circular organization is bacterial; the small size reflects extensive gene transfer from mitochondrion to nucleus during the 2 billion years of integration.

**Mitochondrial ribosomes are 70S**, like bacterial ribosomes — not 80S like the cytoplasmic eukaryotic ribosomes. This matters clinically: antibiotics targeting the 70S ribosome (aminoglycosides, tetracyclines, chloramphenicol) can have mitochondrial off-target effects in eukaryotic patients. The bacterial-style ribosome is direct evidence of bacterial ancestry.

Mitochondria **divide by binary fission**. They do not arise de novo; they replicate themselves by splitting, just as bacteria do. Cells that lose all mitochondria cannot make new ones.

**Mitochondrial rRNA sequences place them inside the α-proteobacteria**. When you build a tree from 16S/18S rRNA sequences across all three domains and include mitochondrial rRNA, the mitochondrial rRNA branches *inside the Bacteria*, specifically in the α-proteobacteria, alongside *Rickettsia*. The mitochondrion is a specific kind of α-proteobacterium that has been a host-cell resident for 2 billion years.

The same five lines of evidence apply to chloroplasts, placing them inside the Cyanobacteria. Secondary and tertiary endosymbiosis — where one eukaryote that already has a chloroplast is itself engulfed — produced the complex plastid organization of diatoms, kelp, and apicomplexan parasites (*Plasmodium falciparum*'s apicoplast, a non-photosynthetic relict plastid, is a target for antimalarial drugs).

The eukaryotic cell is mechanically a chimera: an Asgard-archaeal host genome, a mitochondrial component from an α-proteobacterium, and in plants a chloroplast component from a cyanobacterium. The tree-of-life metaphor breaks at the eukaryotic root — eukaryotes are not on a single branch but on a fusion of multiple branches.

---

## The four-billion-year timeline

With the methods and the major lineages in hand, walk the major events. The dates carry uncertainty of tens to hundreds of millions of years for events more than a billion years ago; the rough sequence is robustly supported by independent lines of evidence.

**~4 Ga** — Earth forms and cools. The oldest accepted biological evidence is ~3.7-billion-year-old graphite inclusions in metamorphosed Greenland sediment with isotopic carbon signatures consistent with biology. Life arose somewhere between 4.2 and 3.5 Ga.

**~3.5 Ga** — LUCA. The last universal common ancestor of all current life. Stromatolites from the Pilbara region of Western Australia show layered microbial mats from this era.

**~2.7 Ga** — Oxygenic photosynthesis evolves in cyanobacteria. Before cyanobacteria, photosynthesis was anoxygenic and produced no O₂. Cyanobacteria evolved water-splitting Photosystem II, releasing oxygen as a byproduct.

**~2.4 Ga** — The **Great Oxidation Event**. Atmospheric oxygen rises from approximately zero to roughly 1–2% of modern levels. Catastrophic for anaerobic life; revolutionary for what followed — aerobic respiration extracts roughly 18× more energy from glucose than fermentation, and the ozone layer begins forming.

**~2 Ga** — Eukaryotes appear, by the Asgard-archaeon plus α-proteobacterium fusion event. The oldest accepted eukaryotic fossils date to about 1.85 Ga.

**~1.5–1 Ga** — Chloroplasts evolve by cyanobacterial endosymbiosis. Major eukaryotic lineages diversify.

**~800–600 Ma** — Multicellularity evolves independently in at least 25–30 eukaryotic lineages — separately in plants, animals, fungi, brown algae, red algae, and several others.

**~540–520 Ma** — The **Cambrian explosion**. Most major animal phyla appear in the fossil record over about 10–30 million years. The Burgess Shale (~508 Ma) and the Chengjiang biota (~520 Ma) preserve arthropods, mollusks, echinoderms, chordates, and a diversity of stem-group lineages that do not survive. Whether this represents a true biological radiation following the evolution of body plans, an environmental trigger (rising oxygen), or a taphonomic effect (the first time mineralized skeletons made fossils possible at scale) is still debated — best current reading: all three, with genuine biological radiation dominant.

**The Big Five mass extinctions:**

- **~440 Ma (End-Ordovician)**: ~85% of marine species lost. Cause: glaciation and sea-level fall.
- **~370 Ma (End-Devonian)**: ~75% of species lost. Cause: contested; marine anoxia, climate cooling, possibly the rise of forests.
- **~252 Ma (End-Permian)**: *The largest mass extinction in Earth history.* ~96% of marine species lost. Cause: Siberian Traps volcanism — ~3 million cubic km of basalt, releasing CO₂, SO₂, and methane, driving rapid warming, ocean acidification, and anoxia. Recovery took 5–10 million years.
- **~200 Ma (End-Triassic)**: ~50% of species lost. Cause: Central Atlantic Magmatic Province volcanism associated with Pangaea breakup.
- **~66 Ma (End-Cretaceous, K-Pg)**: ~75% of species lost; all non-avian dinosaurs, all ammonites, all marine reptiles. Cause: the Chicxulub asteroid impact — a ~10 km body striking the Yucatán, ejecting a global dust-and-sulfate aerosol cloud that blocked sunlight for months to years, visible as the iridium layer in K-Pg boundary clay. Mammals, small nocturnal generalists for ~150 million years under dinosaur dominance, radiated into the empty niches over the next 10 million years. Modern primate lineages — the ancestors of humans — are descended from those survivors.

**Present** — The **Sixth Extinction**. Human-driven habitat destruction, climate change, overharvesting, and species introductions have produced background extinction rates 100–1,000× the pre-human rates inferred from the fossil record. Whether the current biodiversity loss reaches Big-Five magnitude depends on next-century trajectories, but the empirical case for an unprecedented anthropogenic extinction event is now well documented.

---

## When the tree breaks — horizontal gene transfer and the web of life

The tree metaphor works well for sexually reproducing eukaryotes. It breaks for prokaryotes.

In Bacteria and Archaea, genes move between organisms by mechanisms that have nothing to do with reproduction. Three pathways dominate.

**Transformation**: a bacterium takes up free DNA from its environment — released by dead, lysed cells — and incorporates it into its genome. *Streptococcus pneumoniae*, *Bacillus subtilis*, and *Haemophilus influenzae* are naturally competent.

**Transduction**: a bacteriophage accidentally packages some of the host's DNA into its capsid and injects it into the next cell it infects, where it can integrate into the new host's genome.

**Conjugation**: two bacteria physically connect via a protein pilus, and one transfers a plasmid — a small circular DNA molecule often carrying antibiotic resistance, heavy metal resistance, or metabolic genes — to the other. Conjugation can transfer plasmids across substantial phylogenetic distances.

Estimates of the horizontally transferred fraction of bacterial genomes average 5–20% for many species, with some pathogens showing much higher fractions in specific gene categories. The consequence for phylogenetic reconstruction: **different genes in the same bacterial genome can have different evolutionary histories.** Gene A places species X and Y as sisters; gene B places species X and Z as sisters; gene C places species Y and Z as sisters. The conflict is not a methodological problem to be resolved — it is the real biology. Each gene has its own history, partly vertical descent and partly horizontal transfer.

The alternative metaphor — the **web of life** — captures the network structure better than a strictly bifurcating tree. The pragmatic compromise modern phylogenetics adopts: build the species tree from a *core* of genes that are essential, conserved, and rarely transferred — the ribosomal RNAs are the classic example — and treat *accessory* genes (metabolism, antibiotic resistance, virulence) with explicit network methods. The 2016 tree-of-life paper by Hug and colleagues used 16 ribosomal protein genes across 3,083 genomes and resolved much of the bacterial diversity that was missing from earlier trees.

The HGT problem is severe at deep evolutionary time and at the prokaryote-eukaryote interface — endosymbiosis is itself a form of massive horizontal transfer, since the proto-mitochondrion brought ~2,000 genes into the eukaryotic ancestor. It is milder but not absent in modern animals: endogenous retroviruses are a clear recent example of horizontal gene transfer in vertebrates, and introgression between hybridizing animal species can shuffle genes across lineages in ways that produce phylogenetic conflict at specific loci.

The honest reading: the tree model is a good approximation for eukaryotic relationships at most depths, and an increasingly approximate model as you move into Bacteria and Archaea or into deep time. For the major branches — the three domains, the major eukaryotic supergroups, the major animal phyla — the tree captures the dominant evolutionary signal. For fine structure within bacteria, or for the deep tree below LUCA, the tree is a coarse approximation of a more complicated network.

---

## Three misconceptions, named and dismantled

**Humans evolved from chimpanzees.** No. The lineage leading to *Homo sapiens* and the lineage leading to *Pan troglodytes* diverged from a common ancestor approximately 6–7 million years ago and have been evolving independently ever since. The common ancestor was not a chimp; it was an African great ape — fossils of which are partial and contested. Modern chimps and modern humans are sister taxa. The mistake comes from misreading the tree as a ladder with humans at the top and other primates as stepping stones underneath. Every tip is a contemporary endpoint; every lineage has been evolving for the same elapsed time.

**Evolution has a direction or goal — toward complexity, toward humans.** No. Mutation, selection, drift, gene flow, and non-random mating operate locally on populations in specific environments. Selection optimizes locally for what enhances fitness in the current environment, without reference to any long-term direction. A lineage may become simpler (tapeworms have lost their digestive systems; *Mycoplasma* bacteria have reduced genomes), more complex (eukaryotes added organelles), or remain stable for hundreds of millions of years (horseshoe crabs have changed relatively little since the Ordovician). The tree records the history of what happened, not the history of what was supposed to happen.

**Extant "primitive" organisms are ancestors of "advanced" organisms.** No organism alive today is the ancestor of any other organism alive today. The bacterium in your gut has been evolving for four billion years since the last common ancestor with you. Every organism is at the tip of a branch; every branch is as long as every other. "Early-diverging" means a lineage split off near the base of the tree of the group you are looking at — it does not mean that lineage has not evolved since. Modern sponges have been evolving for ~600 million years since the base of the animal tree, accumulated substitutions at characteristic animal rates, and are modern animals with modern genomes. The tree shows order of divergence; it does not show that early-diverging lineages are static.

---

## The bridge to Chapter 13

Phylogenetics gave us the tree — the branching record of who descended from whom. Woese's tree told the world that a third domain existed; the same methodology has since placed whales inside artiodactyls, confirmed birds as dinosaurs, placed fungi as sister to animals, and recovered the Neanderthal admixture signal in modern human genomes. The methodology applies the same machinery from million-year-scale primate divergences up to four-billion-year-scale domain divergences, with quantifiable uncertainty growing as you go deeper.

Chapter 13 asks the next question: *what kinds of changes accumulated along the branches?* It walks the molecular evolution machinery — synonymous versus nonsynonymous substitutions, the dN/dS ratio as a diagnostic for selection, Kimura's neutral theory and the molecular clock at the mechanistic level, transposable elements as a source of novelty, and the Hox-gene machinery that explains why small changes in gene regulation produce large changes in morphology. The tree tells you that the human and chimp lineages have been diverging for 6 million years. The molecular evolution chapter tells you what kinds of changes happened, and where, and which ones mattered.

The methods inferred the past. The molecules tell you why the past looked the way it did.

---

## LLM exercises

The following exercises are designed for use with a large language model. Paste the prompt into any capable model and examine the response critically — not for correctness alone, but for whether the reasoning tracks mechanism rather than just labeling.

**Exercise 1 — Woese's inference**
Prompt: *"Carl Woese discovered the Archaea not by examining cells under a microscope but by comparing 16S ribosomal RNA sequences. (a) Why was molecular sequence comparison necessary — what would a microscopist have seen when comparing a methanogen to E. coli, and what conclusion would the microscopist have drawn? (b) What does it mean, mechanistically, that methanogens shared fewer 16S rRNA fragments with E. coli than E. coli shared with mitochondrial rRNA? What relationship does this imply? (c) Why is 16S rRNA specifically useful for deep phylogeny — what properties of this molecule make it a good phylogenetic clock at billion-year depths? (d) Woese's conclusion was resisted for nearly two decades. Construct the strongest mechanistic argument a skeptic in 1977 could have made, and then explain why the skeptic was wrong."*

Evaluate whether the model correctly explains that morphological convergence makes prokaryotes look identical under the microscope; correctly traces the implication of rRNA fragment sharing (fewer shared fragments means more distantly related); explains why 16S rRNA works for deep phylogeny (universal, functionally constrained, slowly evolving, rarely horizontally transferred); and constructs a genuine skeptical argument (single-molecule artifact, possible convergent rRNA evolution) before explaining why the accumulation of evidence from multiple independent analyses defeated it.

**Exercise 2 — Jukes-Cantor and multiple hits**
Prompt: *"Two DNA sequences differ at 35% of sites (p = 0.35). (a) Compute the Jukes-Cantor corrected distance d = -(3/4)ln(1 - (4/3)(0.35)). (b) Compare d_JC to p = 0.35. How much does the correction inflate the estimate, and why? (c) Now consider p = 0.70. Compute d_JC. (d) At what value of p does the Jukes-Cantor formula become undefined? What is happening biologically at that point? (e) A student argues: 'At low divergence (p = 0.01), the Jukes-Cantor correction barely changes the estimate, so why bother?' Explain when the correction becomes important and why."*

Evaluate whether the model correctly computes d_JC for p=0.35 ≈ 0.47 (compared to raw 0.35); explains the inflation as arising from multiple substitutions at the same site; correctly identifies that the formula is undefined when (4/3)p ≥ 1, i.e., p ≥ 0.75, because the logarithm of a non-positive number is undefined; and explains that the correction is negligible at p < 0.05 but becomes significant above p ≈ 0.20.

**Exercise 3 — Parsimony versus long-branch attraction**
Prompt: *"You are building a phylogeny of four taxa: A, B, C, and D. Taxa A and D have both evolved extremely rapidly — their branches are much longer than the branches to B and C. You run parsimony and it groups A and D as sisters, but maximum likelihood places A with B and D with C. (a) What is long-branch attraction, and why does parsimony suffer from it? (b) Why does maximum likelihood handle this better? (c) You check bootstrap support: parsimony gives 82% for the (A, D) clade; ML gives 91% for the (A, B) and (D, C) clades. Which result should you trust more, and what additional analysis could help distinguish the two topologies? (d) Name one gene category where long-branch attraction is a known problem in real phylogenetics, and why."*

Evaluate whether the model correctly explains long-branch attraction (high evolutionary rates produce convergent character states that parsimony misinterprets as shared ancestry); explains why ML is more resistant (the substitution model explicitly accounts for the higher probability of homoplasy on long branches); correctly interprets the bootstrap values (higher ML bootstrap is not automatically more trustworthy — both should be evaluated against the model); and gives a real example (early-diverging eukaryotes, microsporidia being attracted to the outgroup in early phylogenies before their fast-evolving genomes were recognized).

**Exercise 4 — Endosymbiosis evidence**
Prompt: *"List and explain five independent lines of evidence that mitochondria are descended from free-living α-proteobacteria. For each, explain what the evidence shows mechanistically and why it would be surprising if the endosymbiotic theory were false. Then: (a) Why do mitochondria still retain their own genome rather than transferring all genes to the nucleus? (b) The antibiotic chloramphenicol inhibits 70S ribosomes. What does this predict about its toxicity profile in eukaryotic cells, and is this prediction correct?"*

Evaluate whether the model lists all five (double membranes, circular DNA, 70S ribosomes, binary fission, rRNA sequence affinity inside α-proteobacteria); gives mechanistic explanations for each rather than just naming them; explains the gene-retention question (several hypotheses exist — hydrophobic membrane proteins are too difficult to import, redox regulation of local gene expression, etc.); and correctly identifies that chloramphenicol has mitochondrial toxicity in eukaryotes and that this is indeed observed clinically (aplastic anemia from chloramphenicol suppressing mitochondrial protein synthesis in bone marrow).

**Exercise 5 — Horizontal gene transfer and the web of life**
Prompt: *"A researcher sequences the genome of a pathogenic Staphylococcus aureus strain and finds that 20% of its genes have different evolutionary histories from the core ribosomal genes, with some genes phylogenetically clustering with Enterococcus and others with Clostridium. (a) What mechanism most likely explains this pattern? (b) The Hug et al. (2016) tree of life used only ribosomal protein genes to build the backbone tree. Why these genes specifically — what property makes them useful when most bacterial genes are not? (c) Is this bacterium's 'species tree' the same as the tree you would build from any of its individual genes? What does this imply about the meaning of 'species' in prokaryotes? (d) A clinician notes that the Staphylococcus strain is resistant to six different antibiotic classes. Predict whether the resistance genes are in the core genome or the accessory genome, and explain why."*

Evaluate whether the model correctly identifies horizontal gene transfer (most likely via plasmid conjugation for multiple-resistance genes); correctly explains why ribosomal proteins are useful for backbone trees (universally conserved, functionally essential, rarely subject to HGT because disrupting ribosome structure is lethal, syntenic in most organisms); correctly states that the species tree and gene trees can differ substantially in prokaryotes; and correctly predicts that antibiotic resistance genes are in the accessory genome (on plasmids or in genomic islands) where they can be rapidly transferred by conjugation.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Lynn Margulis** proposed the endosymbiotic origin of mitochondria and chloroplasts in a 1967 paper that was rejected by about fifteen journals before publication. The theory was treated as fringe biology for a decade before the molecular evidence made it undeniable.

**Run this:**

```
Who was Lynn Margulis, and how does her endosymbiotic theory connect
to the cell biology covered in this chapter? Keep it to three paragraphs.
End with the single most surprising thing about the reception of her work
or its eventual vindication.
```

→ Search **"Lynn Margulis endosymbiotic theory"** on Wikipedia. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain the specific molecular evidence — the rRNA sequence comparisons and the mitochondrial genome — that finally convinced the molecular biology community in the 1970s and 1980s.
- Ask it about the broader claim Margulis made about symbiosis as a general driver of evolutionary novelty, and how much of that broader claim the current literature accepts.

What changes? What gets better? What gets worse?

---

*By Nik Bear Brown*
