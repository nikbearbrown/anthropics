# Chapter 13 — Molecular Evolution and Evo-Devo: How Sequences Change and How Bodies Get Built From the Same Toolbox
*Why the fish that lost its spines always lost them at the same address.*

---

Three-spined sticklebacks are small armored fish about the length of a thumb. The marine form carries a pair of bony pelvic spines projecting downward from the body wall like a switchblade. A predator trying to swallow a stickleback gets a mouthful of spines. The armor is expensive in calcium and drag but pays off in survival. Marine sticklebacks have carried it for millions of years.

After the last ice age, marine sticklebacks repeatedly colonized newly-formed freshwater lakes across the northern hemisphere — Iceland, British Columbia, Alaska, Scotland. In many of these lakes, the pelvic spines were lost. Not loosely lost. *Lost.* Some lake populations have only a vestigial pelvic girdle; some have nothing at all. The same morphological change shows up in lake after lake, on different continents, in genetically distinct fish stocks, on a time scale of roughly the last 10,000 years.

In freshwater, the piscivorous fish that the pelvic spines defend against are largely absent; the dominant predators are invertebrates that *prefer* prey with grippable spines. Calcium is scarce in many freshwater lakes, so building bony armor is expensive. The spines stop being useful and start being costly, and fish born without them outreproduce fish that have them. Natural selection runs in reverse.

But which mutation produces a spineless stickleback?

David Kingsley's lab crossed marine and freshwater sticklebacks and mapped the trait. It mapped to a single locus containing a gene called *Pitx1* — a transcription factor known from mouse and chick work to be essential for hindlimb development. They sequenced the *Pitx1* coding region in spine-bearing and spineless fish. The coding sequences were identical. Whatever had changed was not the protein.

The change was a few thousand base pairs upstream, in a tissue-specific enhancer — a regulatory sequence that drives *Pitx1* expression specifically in the developing pelvic region of the embryo. In freshwater fish, this enhancer was deleted. Pitx1 protein still formed in the jaw, in the pituitary, in the developing fin — the other enhancers controlling those domains were intact. But Pitx1 protein no longer formed in the pelvic primordium, the pelvic structures failed to develop, and the spines never grew.

The remarkable part came next. Sequencing the pelvic enhancer across many independent freshwater populations on different continents revealed different specific deletions in different lakes. One lake's fish had a 1.5-kilobase deletion; another lake had a 600-base-pair deletion; a third lake had a deletion with a slightly different boundary. The address was the same. The specific letters removed were different. Convergent regulatory evolution at one regulatory element, driven by the same shared selection pressure, using whatever local mutational accident happened to be available.

This case answers, in one fish, almost every question this chapter has to ask. What kinds of DNA changes matter for morphological evolution? Often regulatory, not protein-coding. How can selection produce the same phenotype repeatedly in independent populations? By attacking the same regulatory element with different specific mutations. Why doesn't the change have catastrophic side effects? Because the modularity of enhancers means losing one tissue-specific element doesn't disrupt the others. Why is the Pitx1 protein conserved if so much evolution happens at this locus? Because the protein still does the same molecular job everywhere else it needs to — and only its deployment to one tissue has been edited away.

The chapter unpacks each of these. First the molecular machinery of how DNA sequences evolve. Then the developmental machinery of how regulatory changes turn into morphology. Then the stickleback again, with all the vocabulary in place.

---

## Part 1: How sequences evolve

### Kimura's neutral theory

The neutral theory is the most misremembered idea in evolutionary biology. Students remember it as "evolution is mostly neutral" or "Kimura said natural selection doesn't matter." The actual claim is narrower, sharper, and more interesting.

In 1968, Motoo Kimura observed that homologous proteins accumulated amino acid changes at a roughly constant rate per year across very different lineages. If most substitutions were beneficial, the rate should vary with environment — different lineages live in different environments. The constancy was hard to explain. Kimura's resolution: maybe most substitutions aren't beneficial. Maybe most are *neutral* — neither beneficial nor harmful — and they go to fixation by genetic drift. If so, the fixation rate would be set by mutation, not by environment, and the clock would tick at roughly the same rate everywhere.

The algebra is three lines.

A diploid population of effective size *Ne* contains 2*Ne* gene copies. Each generation, new neutral mutations enter the population at rate:

new mutations per generation = 2*Ne* × μ

Each new mutation starts at frequency 1/(2*Ne*). Its probability of eventually fixing by drift equals its current frequency — a standard result from Chapter 10. So:

P(a specific new neutral mutation fixes) = 1/(2*Ne*)

The rate at which neutral mutations go to fixation:

K = 2*Ne* × μ × 1/(2*Ne*) = **μ**

The two 2*Ne* factors cancel exactly. The rate at which neutral molecular evolution proceeds equals the mutation rate. It does not depend on population size. It does not depend on environment. This is the molecular clock: the rate is set by mutation, not by selection.

Several things follow that are easy to miss.

The neutral theory is a *null model*, not a denial of adaptation. Adaptive evolution at the molecular level is real — sometimes a beneficial mutation arises and is driven to fixation by positive selection, and the fixation rate for those mutations is *not* μ. But the neutral theory says: most substitutions you see in a genome are neutral, and you should not invoke selection without evidence. The burden of proof falls on the claim that requires more.

"Neutral" is conditional, not absolute. A nucleotide change is neutral in the current environment, at the current population size, against the current genetic background. Change any of those and a previously neutral site can become selected.

Tomoko Ohta's refinement: many mutations are not strictly neutral but **slightly deleterious** — with a selection coefficient on the order of 1/*Ne*. For these, drift and weak selection both matter, and the population-size dependence comes back. Small populations fix slightly-deleterious mutations more often than large populations do, because drift can overwhelm weak negative selection. Small *Ne* is its own genetic hazard.

The clean framing: *the neutral theory wins the methodological battle even when it loses individual cases.* It is the baseline against which every claim of "selection acted here" must be tested.

### dN/dS — measuring selection through the genetic code

Most of what is interesting about selection on a protein-coding gene comes from one feature of the genetic code: it is **degenerate**. Sixty-four codons encode twenty amino acids. The redundancy is not uniform, but on average a single random nucleotide change in a random codon has roughly a 1-in-4 chance of being silent at the protein level. `GAA` and `GAG` both encode glutamic acid. A substitution at the third position changing `GAA` to `GAG` doesn't change the protein.

A substitution that doesn't change the encoded amino acid is **synonymous**. A substitution that does is **nonsynonymous**. The two categories are different things to natural selection. Selection can see a nonsynonymous change through the function of the changed protein. Selection generally cannot see a synonymous change, because the protein is identical. Synonymous sites are, to a good first approximation, selectively neutral — they act as an internal control, telling you what neutral evolution looks like in this gene.

For a given gene compared between two species, compute:

- **dS** = number of synonymous substitutions per synonymous site
- **dN** = number of nonsynonymous substitutions per nonsynonymous site

The "per site" normalization matters because different codons have different numbers of synonymous versus nonsynonymous opportunities. The Nei-Gojobori method handles this bookkeeping. The interpretive rule:

**dN/dS ≈ 1 → neutral evolution.** Nonsynonymous changes accumulate at the same rate as synonymous ones. Selection isn't filtering them out and isn't pushing them in. Classic signature of a pseudogene that has lost function and is now free to drift.

**dN/dS < 1 → purifying selection.** Most nonsynonymous changes get eliminated because they disrupt function. This is the modal pattern for protein-coding genes. Strongly constrained genes — histones, ribosomal proteins, the Hox homeodomains — sit at dN/dS around 0.01–0.1.

**dN/dS > 1 → positive selection.** Beneficial amino acid changes are being fixed faster than neutral synonymous ones can drift in. This is rare over whole genes; even genes well known to be under positive selection usually show dN/dS > 1 only over specific codons or specific branches of the tree.

A few concrete examples show the spectrum.

**Histones (H3, H4).** H4 differs by only two amino acids between cows and peas, separated by roughly 1.5 billion years of evolution. dN/dS near zero. The histone-DNA wrapping geometry is unforgiving — almost every nonsynonymous change breaks function.

**HIV envelope (Env / gp120), V3 loop.** Within a single infected patient, the V3 loop evolves to escape host antibody responses. The dN/dS at V3 codons is often well above 1, sometimes above 5. The antibody-targeted epitope is being actively pushed away from whatever shape the immune system has just learned to recognize.

**MHC class I and II peptide-binding sites.** The antigen-recognition residues of MHC proteins show dN > dS. Consistent with balancing selection — individuals carrying two different MHC alleles present a broader range of peptides to T cells and have higher fitness in environments with pathogen diversity. The MHC region is one of the most polymorphic regions of any mammalian genome.

**Olfactory receptors in dolphins.** Humans have about 400 functional olfactory receptors and another 600 pseudogenes. Dolphins and whales have lost nearly all of theirs — airborne odorant detection is useless underwater. The pseudogenes have dN/dS near 1 because selection no longer cares what they do. The contrast between the functional receptors (dN/dS < 1) and the pseudogenes (dN/dS ≈ 1) in the same gene family is one of the cleanest demonstrations that dN/dS responds to actual function.

The summary sentence: *dN/dS is the answer to a single question — among the substitutions that have already gone to fixation, what fraction changed the protein? The answer tells you whether the protein has been free to drift, forced to stay still, or pushed to change.*

Three honest caveats. First, dN/dS > 1 over a whole gene is uncommon even for genes "under positive selection" — most positive selection acts on a handful of codons. Averaging drowns the signal; branch-and-site models are the modern refinement. Second, dS is not strictly neutral: codon-usage bias affects translation speed, some synonymous changes alter splicing, and synonymous sites near a swept nonsynonymous site can have their diversity reduced by hitchhiking. Third, demography can mimic selection. A population bottleneck followed by expansion can produce haplotype patterns that look like a selective sweep, and several early-2000s "human selective sweep" claims did not survive better demographic models.

### Selective sweeps

When a beneficial mutation rises to fixation by positive selection, it does not travel alone. It sits on a specific chromosome at a specific location, and the alleles at nearby loci on the same haplotype rise in frequency with it — simply because recombination has not yet had time to break up the linked arrangement. The result is a **selective sweep**: a local valley of reduced polymorphism around the selected site, embedded in a sea of normal genetic diversity.

The width of the valley scales with the strength of selection and the local recombination rate. Stronger selection drives the allele to fixation faster, leaving less time for recombination to break up the linked haplotype. A strong sweep at low recombination rate carves a wide, deep valley. A weak sweep at high recombination rate carves a narrow, shallow one.

**Hard sweep:** a single new beneficial mutation rises to fixation. The local signature is dramatic — a long shared haplotype reaching high frequency, elevated linkage disequilibrium between nearby loci, a dip in nucleotide diversity. Lactase persistence in northern Europeans is the textbook example: a single regulatory variant upstream of *LCT* appears on a long shared haplotype reaching roughly 80% frequency in northern Europeans, with the sweep dated to the last 5,000–10,000 years.

**Soft sweep:** selection acts on standing variation, or on multiple independent mutations rising in parallel. Multiple haplotypes carry the favored allele; no single long shared haplotype dominates; the diversity dip is shallower or absent. Soft sweeps are harder to detect but probably more common.

### Transposable elements — selfish DNA, domesticated repeatedly

About 45–54% of the human genome consists of recognizable transposable elements — sequences that can move from one chromosomal location to another. Two classes dominate.

**LINE-1 (L1):** Long interspersed nuclear element. About 17% of the genome. An *autonomous* retrotransposon — it encodes its own reverse transcriptase and endonuclease, machinery sufficient to copy itself out as RNA, reverse-transcribe back to DNA, and insert the copy somewhere else. Some L1s are still active in human germ cells.

**Alu:** A primate-specific short element, about 300 base pairs long, roughly a million copies (~11% of the genome). Non-autonomous — it borrows L1's machinery to move. Derived from a signal recognition particle RNA that got captured into the genome.

The reflex is to call this "junk DNA." The actual picture is more interesting. The genome has repeatedly *exapted* transposable elements for useful function. Three cases are worth naming because each is clean.

**Syncytin and the placenta.** Placental mammals form a fused multinucleated trophoblast layer at the maternal-fetal interface. The fusion is mediated in humans and great apes by **syncytin-1**, encoded by a gene that is the **envelope gene of an endogenous retrovirus**. Retroviral envelope proteins naturally encode fusogenic activity — the virus uses them to fuse with target cell membranes during infection. The mammalian placenta needed a cell-fusion machinery; rather than evolving one from scratch, it co-opted a retroviral one lying in the genome. The remarkable comparative pattern: different placental mammal lineages independently captured *different* ERV envelope genes for the same function. Humans use HERV-W; mice use a different ERV family entirely. Carnivores, rabbits, and lemurs each have their own independently captured syncytin. Convergent domestication of whatever ERV happened to be available — the same function invented from different source material in different lineages.

**V(D)J recombination from a transposon.** The vertebrate adaptive immune system rearranges immunoglobulin and T-cell receptor gene segments by an enzymatic process called V(D)J recombination. The enzymes RAG1 and RAG2 are derived from an ancient Transib-family DNA transposase. The entire vertebrate adaptive immune system traces to a single domesticated transposon. This is the cleanest example of transposable elements as a source of novelty — programmed somatic DNA rearrangement is a function a vertebrate immune system could not have without somebody having first invented a way to cut and rejoin DNA. A transposon already had.

**ERV-derived enhancers in innate immunity.** In mammalian cells, a large fraction of the interferon-stimulated genes — turned on in response to viral infection — are driven by enhancers derived from endogenous retroviral families. Different mammalian lineages co-opted different ERV families for this purpose; primate immune cells use one set, mouse immune cells use another. When a virus integrates into the germline, the host eventually silences most of the inserted sequence; occasionally the regulatory elements inside the viral promoter region are useful — they drive expression in response to interferon, say — and they get retained and wired to nearby host genes.

Transposable elements are neither pure parasites nor purely useful regulatory contributors. They are both, at different times, in different contexts. The genome's relationship to its TEs is one of long-running conflict — the host suppresses most of them with DNA methylation, KRAB-zinc-finger proteins, and piRNAs — punctuated by occasional domestications when a particular element's machinery turns out to be exploitable.

### Gene duplication — the genome buys itself a free copy

A single-copy essential gene cannot accumulate function-altering mutations, because every such mutation gets weeded out by purifying selection. The gene is busy doing its essential job, and any change that breaks the job kills the carrier. But suppose the gene gets duplicated. One copy keeps doing the original job. The other is free to drift — selection no longer cares whether it is functional, because the original copy is covering for it. Three fates follow.

**Pseudogenization.** The most common outcome. The duplicate accumulates stop codons, frameshifts, and deletions, and becomes a molecular fossil — a pseudogene. The human genome contains thousands.

**Subfunctionalization.** The ancestral gene was expressed in tissues A, B, and C. After duplication, each copy loses some regulatory elements. If copy 1 loses the element for tissue C and copy 2 loses the element for tissue A, both copies together still cover all three tissues. Both are now required by purifying selection. Neither copy was "adapted" — the function was just partitioned. This duplication-degeneration-complementation model is the most common route by which duplicates are preserved without invoking new adaptation.

**Neofunctionalization.** The duplicate evolves a function the ancestor did not have. Rare in any specific case; cumulatively the engine by which gene families expand into new functional territory over evolutionary time.

The textbook worked case is the hemoglobin gene family. Successive duplications of a single ancestral globin gene produced the α-cluster (chromosome 16) and β-cluster (chromosome 11), each containing paralogs expressed at different developmental stages. Embryonic hemoglobin in the early embryo. Fetal hemoglobin from 8 weeks of gestation — the fetal form binds oxygen more tightly than the adult form, which is how the fetus extracts oxygen from the maternal bloodstream across the placenta. Adult hemoglobin after birth. One long story of duplication, subfunctionalization across developmental stages, and tuning of each paralog's oxygen-binding curve to the niche it occupies.

---

## Part 2: How regulatory change builds bodies

### Hox genes — the same protein, different bodies

In 1984, William McGinnis was searching for vertebrate equivalents of the *Drosophila* homeotic genes. These genes control segment identity in the fly; mutations produce grotesque phenotypes — *Antennapedia*, a leg growing where the antenna should be; *Ultrabithorax*, a halter transformed into a wing. He used a piece of fly DNA as a probe and screened mouse and frog libraries under low-stringency conditions, expecting vertebrate homologs to have diverged significantly from their fly counterparts.

They had not. The hybridization signal was strong. The 60-amino-acid DNA-binding domain — the **homeodomain**, encoded by the **homeobox** — was essentially unchanged from flies to mice. Subsequent experiments showed the proteins are functionally interchangeable across staggering evolutionary distances: a mouse HoxB6 protein, expressed in a *Drosophila* embryo, can substitute for the fly's *Antennapedia* and rescue the mutant. The DNA-binding specificity has not measurably diverged in roughly 600 million years since the last common ancestor of flies and vertebrates.

Hox genes are a specific class of homeobox-containing transcription factors that control anterior-posterior body axis identity in animals. Flies have eight Hox genes in two clusters. Humans have 39 Hox genes in four clusters — the product of two whole-genome duplications early in vertebrate evolution. The most striking property is **collinearity**: the order of the genes on the chromosome matches the order of their expression along the body. The 3′-most genes are expressed in the anterior (head); the 5′-most genes are expressed in the posterior (tail). This property holds from flies to humans.

<!-- → [IMAGE: Collinearity diagram — a horizontal line representing the HoxA cluster on human chromosome 7, with genes labeled Hoxa1 through Hoxa13 from left (3') to right (5'); below it, a stylized vertebral body plan from cervical (C1) to sacral regions, with bracket annotations showing which Hox genes are expressed at each axial level; the 3'-to-5' gene order on the chromosome mirrors the anterior-to-posterior expression along the body axis; an equivalent Drosophila row above showing the same collinear property with the eight Drosophila Hox genes and a stylized fly body plan below] -->

Here is the question that organizes everything. *If the Hox protein is virtually unchanged between a fly and a vertebrate, how does it produce such different bodies?*

The protein is the same. Where, when, and how much each Hox protein is expressed differs across phyla. The fly *Ultrabithorax* protein is expressed in abdominal segments and represses the limb-promoting target genes; those segments don't grow walking legs. A centipede has limbs on most segments because the Ubx ortholog in the centipede is deployed differently — its expression boundaries are different and its regulatory connection to the limb-promoting genes is different. A snake has lost limbs because the limb-bud-inducing expression of HoxC6/HoxC8 has expanded along the body axis, producing a long thoracic field with no transition to a limb-bearing region. The protein is the same. The regulatory deployment is different. The morphology follows the deployment.

This is the central evo-devo insight: **morphological evolution among animals happens largely through changes in regulatory deployment of a conserved toolkit, not through changes in the toolkit itself.**

### The developmental toolkit — the same five signaling pathways, used everywhere

Hox genes are one element of the animal developmental toolkit. The rest consists of a handful of conserved transcription-factor families and five intercellular signaling pathways: **Wnt**, **Notch**, **Hedgehog**, **BMP/TGF-β**, and **FGF**. Each pathway was already present in the last common ancestor of bilaterian animals. Each is universal from sponges to humans, with the same core components. What changes across animal phyla is how the pathways are wired into the regulatory networks that pattern any given structure. The same instruments; different connections.

A single example makes the reuse visible. Sonic Hedgehog (Shh) patterns the ventral neural tube in vertebrates, controls digit identity in the limb, and organizes the developing gut. In *Drosophila*, its ortholog *hedgehog* patterns segment boundaries and wing veins. Same pathway; different contexts; different outcomes. The outcome is determined by what downstream targets are active in that tissue at that time — which is determined by the regulatory network downstream of the Hedgehog signal, which is different in a vertebrate limb bud and a fly wing imaginal disc.

### Modularity — how an enhancer lets evolution edit one tissue at a time

A typical metazoan gene is regulated by multiple enhancers, each driving expression in a specific tissue or developmental stage. *Pitx1* in fish has separate enhancers for the pelvic primordium, the jaw, the pituitary, and the developing fin. A mutation knocking out the pelvic enhancer eliminates Pitx1 expression in the pelvis without disrupting Pitx1 expression anywhere else. This is what made the stickleback story work.

**Cis-regulatory elements** are DNA sequences on the same chromosome as the gene they regulate — promoters, enhancers, silencers — that control transcription by binding transcription factors. An **enhancer** is a stretch of cis-regulatory DNA, typically a few hundred base pairs long, that binds a combination of transcription factors and drives expression of a target gene in a specific context.

The mechanism that makes enhancers act modularly: each enhancer binds a distinct combination of transcription factors. The pelvic enhancer of *Pitx1* binds factors present in the pelvic primordium and absent elsewhere. The jaw enhancer binds factors present in the jaw primordium and absent elsewhere. The two enhancers are physically separate stretches of DNA, often kilobases apart, and a mutation in one does not affect the other.

This is the structural feature that makes regulatory evolution possible without massive collateral damage. Without modular cis-regulation, every change to a gene's expression would either change the protein (usually breaking it) or change the transcription factor (usually breaking dozens of other genes). With modular cis-regulation, evolution can edit one expression domain at a time. The cost in pleiotropy is reduced by orders of magnitude.

<!-- → [IMAGE: Modular enhancer diagram — a gene shown as a horizontal line with its coding exons (gray boxes) in the center; to the left and right of the coding region, four enhancer elements shown as colored segments on the DNA: "pelvic enhancer" (red, deleted in freshwater sticklebacks), "jaw enhancer" (blue, intact), "pituitary enhancer" (green, intact), "fin enhancer" (orange, intact); below each enhancer, a small tissue diagram showing where it drives expression; an X through the pelvic enhancer with the annotation "deleted in freshwater fish"; arrows from the intact enhancers to the tissues where Pitx1 expression continues unaffected] -->

This is why the King-Wilson conjecture from 1975 worked out. King and Wilson computed from protein-electrophoresis data that humans and chimpanzees share roughly 99% of their protein sequences, and proposed that the morphological differences between us must therefore lie primarily in regulatory sequences controlling when and where each shared protein is expressed. The proposal was speculative in 1975. Forty years of comparative genomics have largely vindicated it: most large morphological differences between closely related vertebrate species map to changes in cis-regulatory elements rather than to changes in the coding sequences of the genes those elements regulate. The strong-form claim that *all* morphological evolution is regulatory has been challenged by Hoekstra and Coyne (2007), who argue that protein-coding changes have been underestimated. The modern consensus is mixed — both kinds of change matter, and regulatory change probably dominates for tissue-specific morphological differences while protein-coding change dominates for biochemical and physiological differences.

### Heterochrony and heterotopy

Two pieces of vocabulary that mean something concrete.

**Heterochrony** is evolutionary change in the *timing* of developmental events. If a developmental process runs longer in a descendant, structures end up larger or more elaborate. If it runs shorter, structures stay simpler or more juvenile-looking. The axolotl (*Ambystoma mexicanum*) is the textbook neotenic vertebrate: it reaches sexual maturity while keeping larval gills and an aquatic body, because the thyroid hormone signaling that drives metamorphosis in related salamanders never fires. The change is in timing — the metamorphic transition simply does not happen.

**Heterotopy** is evolutionary change in the *location* of developmental events. A gene normally expressed in tissue A acquires expression in tissue B, producing a new structure. Butterfly wing eyespots are the showcase. Sean Carroll's lab traced eyespot evolution to a heterotopic deployment of the *Distalless* gene network — the same genes that pattern appendage outgrowth in arthropods, redeployed at specific points on the wing surface to mark eyespots. The eyespot is not built by a new gene network; it is an old gene network used in a new place.

Heterochrony (when) and heterotopy (where) are the two levers by which regulatory evolution turns a conserved toolkit into divergent morphologies. The toolkit is the same. What changes is the schedule and the address.

---

## The stickleback, with all the vocabulary in place

Return to the fish. Marine sticklebacks colonize freshwater lakes after the last glaciation. In freshwater, the predator regime changes and calcium is scarce. Selection favors fish with reduced pelvic armor. The trait maps to a single major-effect locus containing *Pitx1*. The coding sequence of *Pitx1* is identical between spine-bearing and spineless fish. The change is a deletion of a pelvic-specific enhancer about 30 kilobases upstream. *Pitx1* expression is lost in the pelvic primordium. The spines do not form. In dozens of independently colonized freshwater lakes on different continents, different specific deletions knock out the same enhancer.

Here are the concepts the case illustrates, in order.

**Regulatory evolution as the mode of morphological change.** The Pitx1 protein is unchanged; the regulatory element is deleted; the morphology follows the regulatory deployment. This is the King-Wilson prediction, confirmed in one fish at the molecular level.

**Modularity of enhancers.** The pelvic enhancer is one of multiple Pitx1 enhancers. Losing the pelvic one does not disrupt the others. The fish loses its spines without losing anything else Pitx1 does — because those other functions are controlled by separate enhancers.

**Convergent evolution by regulatory change.** The same morphological outcome reached repeatedly in independent populations, at the same regulatory address, by different specific mutations. The address is convergent; the specific letters are not.

**Selective sweep.** Each independent deletion sweeps to fixation in its local population on a time scale of thousands of generations, driven by strong selection in the freshwater environment.

**Why the regulatory route survives selection.** If the pelvic morphology change were instead encoded in a protein-coding change to Pitx1, the same amino acid substitution would affect every tissue where Pitx1 functions — jaw, pituitary, fin. The pleiotropy would be catastrophic. The regulatory route avoids this because of the modular architecture of the enhancers.

The experimental ladder is fully climbed: the phenotype is named, the locus is mapped, the responsible enhancer is identified, the specific deletions are sequenced across populations, and the developmental mechanism is understood. There is no point on the chain where you have to take it on faith. This is what an evolutionary explanation looks like when it works.

---

## Worked example: dN/dS on FOXP2

Let me walk one full dN/dS analysis on a contested case — the gene FOXP2, and whether the protein-coding changes on the human lineage since the chimp-human split show evidence of positive selection.

### The data

The human FOXP2 protein is 715 amino acids long. The human and chimpanzee proteins differ at **two amino acid positions** on the human lineage — two nonsynonymous substitutions between the human-chimp common ancestor and modern humans. There is one synonymous substitution on the human branch in this gene.

### Computing dN/dS

A protein-coding gene of 715 codons has 2,145 nucleotide sites. Using the rough rule that about 25% of sites in a typical coding gene are synonymous:

- Synonymous sites: ~0.25 × 2,145 ≈ 536
- Nonsynonymous sites: ~0.75 × 2,145 ≈ 1,609

```
dN = 2 / 1,609 ≈ 0.00124
dS = 1 / 536 ≈ 0.00187
dN/dS = 0.00124 / 0.00187 ≈ 0.67
```

For a whole-gene average, dN/dS ≈ 0.67 — less than 1, consistent with purifying selection on the gene as a whole. FOXP2 is a tightly conserved transcription factor; most of its sequence is not free to change. The two specific human-lineage substitutions represent an interesting departure from the overall constraint, but averaging over 715 amino acids dilutes that signal enormously. The right question to ask is not what the whole-gene average is but whether specific codons on the human branch show elevated dN/dS — which requires branch-and-site models that the original 2002 Enard paper did not use.

### What the original 2002 claim was

Enard and colleagues in 2002 used patterns of intronic variation in modern human populations to look for the haplotype-tree signature of a recent selective sweep on the human FOXP2 locus. They observed reduced polymorphism near the relevant coding substitutions and an excess of rare variants — consistent with a recent positive-selection sweep. They estimated the sweep occurred within roughly the last 200,000 years and argued FOXP2 may have been a target of positive selection during the emergence of human language capacity.

The story got told widely as "the gene for human language."

### What complicated it

Three subsequent findings weakened the claim.

Neanderthals had the same two FOXP2 substitutions. The two amino acid changes are therefore older than the modern-human–Neanderthal split — roughly 500,000 to 800,000 years ago, not unique to modern humans.

A 2018 reanalysis by Atkinson and colleagues, using larger datasets and updated demographic models, found that the original signal of recent positive selection on FOXP2 may have been a methodological artifact — attributable to demographic structure that the 2002 analysis did not adequately model. The molecular evidence for an adaptive fixation of the two amino acid substitutions on the human lineage is **weaker than initially reported**.

FOXP2 is not "the language gene." It is a transcription factor expressed broadly in brain, lung, and gut during development. The KE-family patients carrying a missense FOXP2 mutation have orofacial motor coordination deficits, syntactic and comprehension impairments, and reduced nonverbal IQ — not a pure language deficit. Mouse Foxp2 knock-ins of the human form modestly alter striatal neuron dendritic morphology — not language.

### What the case shows

The two amino acid substitutions are real. The Neanderthal sharing of those substitutions is real. The strong-form "recent positive selection on FOXP2 in modern humans" reading is no longer well-supported. The weaker-form "FOXP2 underwent some molecular change on the hominin lineage" is supported.

The case is in the chapter for a specific pedagogical reason. It is a worked example of how a molecular-evolution claim self-corrects. The original analysis was state-of-the-art in 2002; better data and better methods in 2018 produced a different answer. A student who walks away believing "FOXP2 is the language gene" has not learned the chapter. A student who walks away saying "FOXP2 underwent two amino acid changes on the hominin lineage, and what those changes mean is an active research question with the original strong claim no longer well-supported" has learned the chapter.

The methodological lesson generalizes. A single dN/dS number averaged over a whole gene is not a finding; it is a starting point. Branch-and-site models that partition the analysis by codon and by branch are what you would use today. Demographic alternatives need to be excluded before a sweep signal can be confidently called selection. And the link from a selection signal to a functional claim — from "this gene was selected" to "this gene does X in the trait we care about" — requires independent functional evidence beyond the sequence comparison.

---

## What the chapter built

The chapter asked one question and answered it in a fish. Why does the fish that lost its pelvic spines always lose them at the same address?

Because morphological evolution among animals happens largely through changes in *regulatory deployment* of a conserved toolkit. The Pitx1 protein is unchanged between marine and freshwater sticklebacks, between fish and mice, in any meaningful sense between phyla. What changes is which tissues get the protein, when, and how much. The pelvic enhancer is the address that controls the pelvic deployment. Lose the enhancer, lose the spines — and because the enhancer is physically separate from the others, nothing else is disturbed. The modularity of cis-regulatory architecture is what makes this possible.

The molecular-evolution machinery in Part 1 — neutral theory, dN/dS, selective sweeps, transposable element exaptation, gene duplication — describes how *sequences* accumulate substitutions and what those substitutions tell us about selection. The developmental-evolution machinery in Part 2 — Hox collinearity, the toolkit signaling pathways, modular enhancers, heterochrony, heterotopy — describes how *regulatory changes in those sequences* turn into morphology.

The two halves meet in the stickleback. A deletion at one regulatory address. Convergent in every freshwater lake on Earth. The sequence changes are at the regulatory level, detectable as deletions of a tissue-specific enhancer. The morphological change is at the body-plan level, detectable as a spine missing from the pelvis. The connection is direct, molecular, and fully understood. Population genetics, molecular evolution, and developmental biology are not three different stories. They are one story told at three different scales.

---

## LLM Exercise — Build your molecular evolution simulator

### The simulation prompt

```
Show: Read CLAUDE.md and DESIGN.md from this project. Conform to them.

Say: Build 13-molecular-evolution.html — a two-panel molecular
evolution and evo-devo simulator.

Panel 1 — dN/dS accumulator with selective sweep. Simulate
evolution of a coding sequence under three conditions:

Controls:
- Mutation rate μ (slider, default 1e-5 per site per generation)
- Selection coefficient for nonsynonymous variants (slider:
  -1 to +1, where 0 = neutral, negative = deleterious,
  positive = beneficial)
- Population size Ne (log slider: 100 to 100,000)
- Fraction of sites that are synonymous (slider: 0.15 to 0.35,
  default 0.25)
- Generations to simulate (slider: 100 to 10,000)

Display:
- Real-time dN/dS ratio as a gauge (0 to 2+)
- Separate running counts of dN and dS substitutions
- Time series plot of the frequency of the most recent
  nonsynonymous variant to arise; if selection coefficient
  is positive, animate the sweep to fixation
- When a sweep occurs, show a "diversity landscape": a bar
  chart of site-heterozygosity across 100 flanking sites,
  with a visible trough around the swept site

Three preset buttons:
1. "Pure neutral": selection = 0, Ne = 10,000, μ = 1e-5.
   Should produce dN/dS ≈ 1 over time, K ≈ μ = 1e-5.
2. "Strong purifying selection": selection = -0.8 on
   nonsynonymous changes. Should produce dN/dS << 1.
3. "Positive selection sweep": selection = +0.2 for one
   nonsynonymous variant. Should show the variant sweeping
   to fixation and a diversity trough in the flanking region.

Verify: Print to console as PASS/FAIL:
(1) Neutral preset: after 10,000 generations, dN/dS should
    be in [0.8, 1.2] (within 20% of 1).
(2) Neutral preset: fixation rate K should be within 50% of μ.
(3) Purifying selection: after 10,000 generations, dN/dS
    should be < 0.5.
(4) Positive selection: the beneficial variant should reach
    fixation within 5 × Ne generations from arising.

Panel 2 — Hox boundary shift and morphological outcome.
A stylized vertebrate body plan shown as a horizontal row
of 20 segments. Each segment is colored by which Hox gene
"dominates" it, using a gradient palette (5 colors for
anterior to posterior Hox expression). Below each segment,
a small morphological label (e.g., "cervical," "thoracic-rib,"
"thoracic-no-rib," "lumbar," "sacral").

Controls:
- Hox posterior boundary slider: move the transition between
  "thoracic-rib" and "thoracic-no-rib" expression from
  segment 7 through segment 15 (default: segment 10)
- "Knockout" toggle: removes expression of the selected Hox
  gene from all segments (simulates a null mutation)

Display:
When the slider moves, the morphological labels update: moving
the boundary posteriorly adds rib-bearing segments (like
snake body elongation); moving it anteriorly reduces rib-
bearing segments. When "knockout" is toggled, all segments
that relied on that Hox gene for patterning show "FAIL"
(developmental failure) — to contrast the knockout effect
(global failure) with the boundary shift (local, viable change).

Annotate the panel:
- Boundary shift: "Regulatory change — shifts expression
  domain; local morphological effect"
- Knockout: "Protein-coding null — removes function globally;
  developmental failure"

Verify: Print to console:
(1) Moving boundary from segment 10 to segment 14 should
    produce 4 additional rib-bearing segments (PASS/FAIL).
(2) Knockout toggle: all segments where the knocked-out Hox
    gene dominated should show FAIL status (PASS if 100%
    of those segments change to FAIL).

Constrain: Single self-contained HTML file, D3 v7 from CDN,
no other dependencies. Color palette: synonymous substitutions
green #27ae60; nonsynonymous substitutions red #c0392b; neutral
dN/dS zone (0.8–1.2) shaded in light gray; sweep trough in
the diversity landscape in orange #e67e22. Hox expression
gradient: anterior blue #1a5276 through posterior red #c0392b.

Add at top of script:
// CLAIM 1: Neutral fixation rate K = μ (population size cancels).
// CLAIM 2: dN/dS < 1 = purifying selection; > 1 = positive
//   selection; ≈ 1 = neutral drift.
// CLAIM 3: Selective sweep carves a diversity trough in
//   linked sites; width proportional to selection strength.
// CLAIM 4: Hox boundary shifts (regulatory change) produce
//   viable morphological variation; Hox knockouts (coding
//   change) produce developmental failure.
```

### Exploration tasks

Once the simulation runs:

1. **The neutral rate equals the mutation rate.** Load the neutral preset and run 10,000 generations. Record the final dN/dS. Run three times with Ne = 100, 1,000, and 10,000. Note that the final dN/dS hovers near 1 in all three cases regardless of population size. This is the cancellation: large populations generate more mutations, but each has a lower fixation probability, and the two factors cancel exactly.

2. **The sweep and the diversity trough.** Load the positive selection preset. Pause just before the favored nonsynonymous variant reaches fixation. Note the diversity landscape — the flanking sites still have normal heterozygosity. Let the sweep complete. Observe the trough that appears around the fixed variant. This is the hitchhiking effect in miniature.

3. **The Hox boundary shift vs. knockout contrast.** In Panel 2, start with the boundary at segment 10. Move it to segment 14, producing snake-like elongation of the rib-bearing thorax — a viable, morphologically distinct animal. Now toggle the knockout on the same Hox gene. All segments that were patterned by that gene show FAIL. The boundary shift is a model of regulatory evolution; the knockout is a model of what a protein-coding loss-of-function mutation does. The same gene; very different evolutionary consequences depending on which level of the regulatory hierarchy is disrupted.

4. **Purifying selection slowing morphological change.** Set the selection coefficient to -0.2 and run for 5,000 generations. Watch the dN/dS accumulator. Compare the rate at which nonsynonymous substitutions accumulate to the rate in the neutral preset. Calculate roughly what fraction of nonsynonymous mutations are escaping purifying selection. This is the constraint on Hox homeodomain sequences — essentially zero nonsynonymous changes escape over millions of years — and it is what makes the homeodomain usable as a cross-phylum conservation marker.

### Extension prompt

```
Extension: Add a third panel to 13-molecular-evolution.html —
Enhancer Evolution Simulator.

Show a gene with four independent tissue-specific enhancers
(pelvic, jaw, pituitary, fin — explicitly modeled on the
Pitx1 stickleback case). Each enhancer is represented as a
short horizontal bar labeled with its tissue. Each has an
independent deletion rate slider (default: 1e-4 per generation)
and a fitness consequence selector (neutral / deleterious /
beneficial-in-freshwater).

When a deletion occurs in the "pelvic enhancer":
- The pelvic tissue loses the gene's expression (shown as the
  tissue bar going gray)
- The other three tissues continue expressing the gene normally
- If "beneficial-in-freshwater" is selected, the deletion sweeps
  to fixation; animate the sweep
- Show the resulting morphology label change: "pelvic spines:
  present → absent"

When a deletion occurs in any other enhancer:
- If "deleterious" is selected for that enhancer, the deletion is
  purged and does not fix
- The gene's expression in other tissues is unaffected

Run the simulation across 10 independent "freshwater lake"
populations simultaneously (10 side-by-side replicates). Show
that each population independently loses the pelvic enhancer,
but the specific deletion (start/end coordinates, labeled in
arbitrary base-pair coordinates) differs across populations.
Annotate: "Convergent regulatory evolution — same address,
different specific deletion, same morphological outcome."

Verify: After 50,000 generations with "pelvic = beneficial-in-
freshwater" and "jaw/pituitary/fin = deleterious," all 10
replicate populations should have lost the pelvic enhancer
(frequency 1.0) while retaining the other three enhancers
at frequency ≈ 1.0 (PASS if at least 9/10 replicates show
this pattern, allowing for drift in small populations).
```

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Motoo Kimura** published "Evolutionary rate at the molecular level" in *Nature* in 1968 — five pages that overturned the assumption that most molecular evolution was adaptive. **Mary-Claire King and Allan Wilson** published "Evolution at two levels in humans and chimpanzees" in *Science* in 1975, proposing from protein-electrophoresis data that the morphological differences between humans and chimps must lie mostly in regulatory sequences. Both papers were written before anyone could directly sequence DNA. Both turned out to be largely right.

**Run this:**

```
Who was Motoo Kimura, and what was controversial about his
neutral theory of molecular evolution when he proposed it
in 1968? Keep it to three paragraphs. End with the single
most surprising thing about how the field's attitude toward
the neutral theory changed between 1968 and today.
```

→ Search **"Motoo Kimura neutral theory"** on Wikipedia. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to walk through the three-line algebraic derivation showing that the fixation rate for neutral mutations equals the mutation rate, and explain why the population-size terms cancel.
- Ask it to compare the King-Wilson 1975 prediction to what the post-2000 genome era found — which parts of their argument held up, and which needed revision?

What changes? What gets better? What gets worse?
