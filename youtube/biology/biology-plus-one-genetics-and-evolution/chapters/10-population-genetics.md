# Chapter 10 — Population Genetics and Natural Selection: How Allele Frequencies Change, and How to Predict Them
*The null hypothesis that answers a creationist.*

---

In 1908, the British mathematician G. H. Hardy received an annoying question at a dinner party. Hardy was a number theorist at Cambridge, professional aesthete on the subject of pure mathematics, and faintly embarrassed when his work touched the real world. The question came from his friend, the geneticist Reginald Punnett. Punnett had been put in an awkward position by a critique of Mendelism then circulating in the biological community.

The critic was a statistician named George Udny Yule, and his argument ran like this. If dominant alleles are truly dominant, and if dominance has any effect on inheritance, then over generations the dominant phenotype should rise until it saturates the population at a 3:1 ratio. Brown eyes are dominant over blue. Why haven't brown eyes taken over? Isn't something wrong with Mendel?

Hardy worked it out in an afternoon, sent a letter to *Science*, and got back to number theory. The letter is three pages, almost contemptuously brief. The proof fits on an index card.

Hardy's answer: consider a population where allele A has frequency *p* and allele a has frequency *q*, with p + q = 1. Assume mating is random. Then each offspring draws one allele from mom and one from dad independently. The probability of drawing two A alleles is p × p = p². Two a alleles: q². One of each, in either order: 2pq. So genotype frequencies are p², 2pq, q² — and they sum to 1 because (p + q)² = 1.

Now compute the allele frequency in the *next* generation. Every AA individual contributes 100% A alleles to the gamete pool; every Aa contributes 50%; every aa contributes 0%. So the new frequency of A is:

p(next) = p² × 1 + 2pq × ½ + q² × 0 = p² + pq = p(p + q) = p

Nothing changed. The allele frequencies sit at *p* and *q* forever. The genotype frequencies sit at p², 2pq, q² forever. Brown eyes are not going anywhere, because dominance is a fact about *expression*, not about *frequency*. An allele rises in frequency only if something is actually driving it — selection, drift, migration, mutation. Without any such force, the population sits still.

<!-- → [IMAGE: Hardy-Weinberg random mating diagram — a gene pool shown as a bucket of alleles (fraction p labeled A in dark blue, fraction q labeled a in light blue); two arrows drawing one allele each to form an offspring; four possible combinations shown below: A+A = AA (probability p²), A+a = Aa (probability pq), a+A = Aa (probability qp), a+a = aa (probability q²); boxes for Aa and aA collapsed into one labeled 2pq; final genotype frequencies p², 2pq, q² labeled below with the note "these sum to 1 because (p+q)² = 1"] -->

Weinberg in Germany derived the same result the same year, from medical-genetics data on twins and color blindness. For decades it was called "Hardy's law" in English and "Weinberg's law" in German. Eventually the joint attribution settled in: **Hardy-Weinberg equilibrium**.

I want to be careful about making the dinner-party origin sound smaller than it is. The Hardy-Weinberg equilibrium is the null hypothesis of population genetics. It is the reference point against which all departures get measured. Every claim about evolution at the population level — every claim of selection, drift, gene flow, mutation, or non-random mating — is, at bottom, a claim about a deviation from Hardy-Weinberg. The principle does for population genetics what *F* = *ma* does for mechanics: it tells you what the system does when nothing is happening, so you can recognize the thing you care about when it shows up.

---

## What we are counting

A population is a group of interbreeding individuals of the same species. They share a **gene pool** — the totality of alleles at every locus, summed across all individuals. For a diploid species, each individual carries two alleles per gene, so a population of *N* individuals contains 2*N* copies of any given gene.

The **allele frequency** of a given allele is its count divided by 2*N*. Call the two alleles A and a, their frequencies *p* and *q*. By definition p + q = 1.

The **genotype frequency** of, say, AA is the number of AA individuals divided by *N*.

These are related but different quantities, and population genetics tracks allele frequencies more carefully. The reason: genotypes last one generation. An AA individual passes individual A alleles into gametes; it does not pass on its diploid identity. Whatever diploid combinations arise in the next generation depend on which alleles are in the gene pool, not on which combinations existed in the parents. If you want to know what the population will look like next generation, track allele frequencies.

This is exactly where Yule went wrong. He tracked genotype frequencies — the brown-eyed ratio — and expected them to drift upward. Hardy saw that what matters is the allele frequency underneath, and that allele frequency, under random mating alone, stays put.

<!-- → [IMAGE: Numerical worked example of allele frequency counting — a population of 10 individuals shown as circles, each divided into two halves representing their two alleles: 4 circles show AA (both halves dark blue), 4 show Aa (one half each), 2 show aa (both halves light blue); below the circles, tally: A alleles = (4×2) + (4×1) = 12; a alleles = (4×1) + (2×2) = 8; total alleles = 20; p = 12/20 = 0.60; q = 8/20 = 0.40; annotated: "genotype frequencies: AA = 4/10, Aa = 4/10, aa = 2/10; allele frequencies: p = 0.60, q = 0.40; shortcut: p = f(AA) + ½f(Aa) = 0.40 + 0.20 = 0.60"] -->

---

## The five forces

The Hardy-Weinberg equilibrium holds if five conditions are met: large population, random mating, no mutation, no migration, no selection. No real population satisfies all five. The violation of each condition corresponds to one force that moves allele frequencies. There are exactly five:

**Mutation** — new alleles enter the gene pool.  
**Natural selection** — some alleles propagate more reliably than others.  
**Genetic drift** — finite populations show sampling error in who reproduces.  
**Gene flow** — migrants carry alleles in or out.  
**Non-random mating** — who mates with whom is not independent of genotype.

The chapter takes each in turn, with its equation and its example. Then the longest section — a worked example of natural selection — shows all the pieces in motion simultaneously.

---

## Force 1: Mutation

Mutation is the only force that creates new alleles. Selection can sort among variants; drift moves frequencies; gene flow imports alleles from elsewhere; non-random mating reshuffles. Mutation is where the variation comes from in the first place.

The per-generation mutation rate at a typical protein-coding gene is on the order of 10⁻⁵. That is too slow to move allele frequencies appreciably on its own — a new mutation starts at frequency 1/(2N) and would need thousands of generations of mutation input to shift the population average. What mutation does is *supply the menu* of variants that the other forces then act on.

There is one special case where mutation does drive a stable frequency: **mutation-selection balance** for a deleterious recessive. If selection removes copies of allele a at rate *s*, and mutation creates them at rate *μ*, the equilibrium frequency is:

q* ≈ √(μ/s)

For μ = 10⁻⁵ and *s* = 0.5, that is about q* ≈ 0.0045, giving disease incidence q*² ≈ 2 × 10⁻⁵ — 1 in 50,000. Many rare recessive diseases sit near frequencies consistent with mutation-selection balance: every generation, selection eliminates the allele from homozygotes; every generation, mutation regenerates it. The disease persists forever at low frequency, neither going extinct nor rising to common levels.

The peppered moth *Biston betularia* illustrates the other direction. A single transposable-element insertion into the cortex gene created the *carbonaria* dark allele in industrial England. Without that mutation, there was no variant for selection to act on and no adaptation was possible. Without selection, the mutation would have vanished from drift almost immediately. Mutation supplied; selection sorted.

<!-- → [CHART: Mutation-selection balance — x-axis: selection coefficient s (0.01 to 1.0, log scale); y-axis: equilibrium allele frequency q* (0.0001 to 0.1, log scale); three curves shown for μ = 10⁻⁶, 10⁻⁵, and 10⁻⁴, each following q* = √(μ/s); annotated with reference points: μ = 10⁻⁵, s = 0.5 → q* ≈ 0.0045, disease incidence q*² ≈ 1/50,000; caption: "Stronger selection (higher s) drives q* lower; higher mutation rate (higher μ) raises q* — the disease frequency is set by their ratio"] -->

---

## Force 2: Natural selection

**Fitness** (*w*) is expected relative reproductive success — expected offspring count, normalized to the fittest genotype in the population. The fittest genotype gets *w* = 1; all others get *w* ≤ 1.

The **selection coefficient** (*s*) is 1 − *w*. It captures the fitness reduction. *s* = 0 means no reduction; *s* = 1 means the genotype leaves no offspring.

For a locus with alleles A and a, there are three genotypes and three fitnesses — one pattern of selection coefficients for each biological scenario. The pattern determines the outcome.

**Selection against a recessive.** If aa homozygotes have reduced fitness (waa = 1 − *s*) and Aa and AA are equally fit, then allele a declines each generation. The change per generation follows:

q' = q(1 − sq) / (1 − sq²)

The important behavior: **selection against a rare recessive is very slow**. When q is small, most copies of a sit hidden in Aa heterozygotes — fraction ~2q of the population — where selection cannot see them. Only the small fraction q² of aa homozygotes are exposed. To halve the frequency of a rare recessive from q = 0.01 to q = 0.005 takes hundreds of generations even at *s* = 0.5.

This is why historic proposals to "eliminate" recessive disease by preventing affected homozygotes from reproducing were mathematically futile — even setting aside their profound ethical failures. At a carrier frequency of 2pq ≈ 0.02 and disease incidence of q² = 10⁻⁴, roughly 200 carriers exist for every affected individual. Removing the homozygotes trims the allele's frequency at a glacial rate; the carriers replenish it each generation.

**Selection against a dominant.** If the A allele is dominant and deleterious — both AA and Aa pay the fitness cost — then selection acts much faster, because every copy of A is exposed in both homozygotes and heterozygotes. Dominant deleterious alleles disappear within tens of generations without recurrent mutation to sustain them.

**Heterozygote advantage (overdominance).** When the heterozygote has higher fitness than either homozygote — wAa > wAA and wAa > waa — selection produces a *stable polymorphism*. Both alleles are maintained at intermediate frequencies indefinitely. The equilibrium and the math are in the sickle cell section below.

---

## Force 3: Genetic drift

Drift is the strange force. It has nothing to do with fitness, adaptation, or biological function. It is statistical sampling error in who happens to reproduce, accumulated generation after generation.

Here is the picture. A population of *N* diploid individuals produces gametes. The next generation samples 2*N* alleles from that pool. The sampling is random. The new allele frequency is not exactly equal to the old one — it differs by a random amount whose variance is:

Var(p') = pq / (2N)

The standard deviation is √(pq / 2N). At N = 10,000, the standard deviation of allele frequency change per generation is about 0.5%. At N = 100, it is about 5%. At N = 10, it exceeds 15%.

<!-- → [CHART: Genetic drift trajectories — three panels side by side, each showing 10 replicate runs of allele frequency over 200 generations starting at p = 0.5; left panel: Ne = 10,000 (all lines stay near 0.5, narrow band); middle panel: Ne = 100 (lines wander substantially, some reaching 0 or 1); right panel: Ne = 10 (nearly all lines reach fixation or loss within 100 generations); x-axis: generation; y-axis: allele frequency 0–1; caption: "Drift magnitude scales as 1/√Ne — in small populations, allele frequencies wander and alleles are lost; in large populations, they barely move"] -->

Three consequences dominate the chapter.

**(1) Fixation or loss is the long-term endpoint.** Without mutation, balancing selection, or gene flow, drift eventually pushes every locus to either fixation (p = 1) or loss (p = 0). A neutral new mutation starting at 1/(2N) has a 1/(2N) probability of eventually fixing. Most new mutations are lost almost immediately.

**(2) The decisive parameter is Ne × s.** In real populations, the relevant *N* is the **effective population size** *Ne* — the size of an idealized equal-sex-ratio random-breeding population that would show the same drift. *Ne* is usually smaller than census size, sometimes much smaller, because of unequal sex ratios, variance in reproductive success, and past bottlenecks. For humans, *Ne* ≈ 10,000 despite billions of census individuals, reflecting the severe bottleneck during the Out-of-Africa migration ~60,000 years ago. When *Ne* × *s* >> 1, selection dominates; when *Ne* × *s* << 1, drift dominates. At *Ne* = 10,000, an allele with s = 0.001 has *Ne* × *s* = 10 — selection wins. An allele with s = 0.00005 has *Ne* × *s* = 0.5 — drift wins, and the allele behaves as if it were neutral.

**(3) Drift erodes variation.** Expected heterozygosity decays at rate 1/(2*Ne*) per generation. Small populations lose variation fast.

**Bottleneck effect.** A bottleneck is a temporary severe reduction in population size — a disease epidemic, a habitat collapse, a chance disaster. During the bottleneck, drift is intense; many alleles are lost. The survivors carry only a fraction of the source population's variation. Population recovery does not restore lost alleles; only mutation can, slowly. The cheetah passed through a severe bottleneck ~10,000 years ago. Modern cheetahs show genetic variation roughly 95% lower than typical mammals. The MHC — the most polymorphic gene complex known — is essentially monomorphic in cheetahs; skin grafts between unrelated individuals are not rejected because their immune systems cannot distinguish self from other-cheetah.

**Founder effect.** A founder effect is a bottleneck compressed into the founding of a new population. Whatever alleles the founders happen to carry — including rare alleles that may have been at low frequency in the source — become the starting point for the new population. The Old Order Amish of Lancaster County, Pennsylvania, descend from about 200 founders from Switzerland and Germany who arrived in the 1700s and have remained largely endogamous since. Ellis-van Creveld syndrome — a recessive condition causing short-limbed dwarfism, polydactyly, and heart defects — affects about 1 in 200 Lancaster Amish births, compared to 1 in 60,000 in the general population. The disease allele was almost certainly carried by one or a few of the 200 founders; drift and endogamy raised its frequency by an order of magnitude over three centuries.

Different Amish settlements have different elevated diseases, depending on which alleles their specific founders happened to carry. Ohio settlements have elevated maple syrup urine disease. The Pennsylvania settlement has Ellis-van Creveld. Each settlement's medical profile is its founders' hand of cards.

**One distinction worth insisting on.** A bottleneck and a sustained small population are not the same. A population that crashes from a million to 50 for *one generation* and then recovers loses most of its variation in a single catastrophic event; it recovers only as fast as mutation generates new variation, which takes hundreds of thousands of generations. A population that has been at Ne = 50 for 1,000 generations has much lower variation than a large population, but it has reached a mutation-drift equilibrium where some variation persists. The bottleneck is worse than the sustained small population because the allele loss is instantaneous and permanent. Conservation managers who face species that have recently bottlenecked face a very different genetic-management problem than those managing species at chronically low population sizes.

---

## Force 4: Gene flow

**Gene flow** is allele movement between populations via migration. If a fraction *m* of a population are recent migrants carrying allele frequency p₂, and the resident population has frequency p₁, the new frequency in the receiving population is:

p₁' = (1 − m) × p₁ + m × p₂

Gene flow's main effect is **homogenization**. Even small migration rates — m = 0.01, one migrant per hundred per generation — are usually enough to prevent two populations from diverging substantially by drift, as long as selection is also weak. The competition is between *m* and *s*: if *m* >> *s*, populations stay similar; if *s* >> *m*, they diverge.

Gene flow can also rescue an inbreeding-depressed isolated population. The Florida panther was reduced to 20–30 individuals by the 1990s, showing kinked tails, cardiac defects, and low sperm motility — the signatures of inbreeding depression. In 1995, eight Texas puma females were introduced to restore gene flow. The introgression worked; the population has since grown to over 200, and the inbreeding signatures have largely disappeared. Genetic rescue is one of the rare unambiguous conservation success stories.

Gene flow can work against local adaptation. If migrants from a neighboring population keep importing an allele that selection is trying to remove locally, the local population may never reach fixation. This **migration load** sets a floor on local adaptation in connected populations.

For human populations: the major continental groups have *F*ST ≈ 0.10–0.15 — meaning about 85–90% of human genetic variation is *within* groups, not between them. Gene flow has kept human populations far more homogeneous than the visible phenotypic differences in skin color, hair texture, and facial morphology might suggest. Human continental populations are not biologically discrete races.

---

## Force 5: Non-random mating

Non-random mating is the odd one out. It can change *genotype* frequencies without changing *allele* frequencies at all.

**Assortative mating** — preference for phenotypically similar partners — increases homozygote frequencies and decreases heterozygote frequencies, while p and q stay unchanged.

**Inbreeding** — mating with close relatives — increases homozygosity at *every* locus simultaneously. The effect is quantified by the **inbreeding coefficient** *F*, the probability that an individual's two alleles at a locus are identical by descent from a common ancestor. For an offspring of first cousins, F = 1/16. For an offspring of full siblings, F = 1/4.

With inbreeding, genotype frequencies depart from Hardy-Weinberg:

*f*(AA) = p² + Fpq  
*f*(Aa) = 2pq(1 − F)  
*f*(aa) = q² + Fpq

The heterozygote frequency drops by Fpq; that deficit is split evenly between the two homozygote classes. Allele frequencies are unchanged; it is the diploid pairings that are reshuffled.

<!-- → [IMAGE: Inbreeding effect on genotype frequencies — two stacked bar charts side by side, both at p = 0.7, q = 0.3: left bar (F = 0, random mating) shows AA = 0.49, Aa = 0.42, aa = 0.09 in dark/medium/light blue; right bar (F = 0.25, offspring of full siblings) shows AA = 0.49 + 0.25×0.21 = 0.543, Aa = 0.42×0.75 = 0.315, aa = 0.09 + 0.25×0.21 = 0.143; arrows showing the deficit in Aa and surplus in AA and aa; annotated: "Allele frequencies unchanged: p = 0.70, q = 0.30 in both — only the diploid pairings shift"] -->

The consequence is **inbreeding depression**. Deleterious recessive alleles that were hiding in heterozygotes are now exposed in homozygotes. Offspring of first-cousin marriages carry about 1.7–2.8% additional risk of severe genetic disease above the baseline ~2% — approximately doubling the background risk. In experimentally inbred *Drosophila* lines, inbreeding depression on fitness can reach 30–80% within a few generations.

Inbreeding does *not* cause mutations. This misconception recurs: the diseases that emerge in inbred populations are pre-existing alleles becoming homozygous, not newly created mutations. The alleles were already there, silent in carriers. Inbreeding just paired them with themselves more often than random mating would.

---

## Worked example: sickle cell in West Africa — the math of a balanced polymorphism

The HbS allele is a single point mutation in the β-globin gene — the A→T transversion at codon 6 that we traced end-to-end in Chapter 05, changing glutamate to valine. The substituted valine creates a sticky hydrophobic patch on deoxygenated hemoglobin S; under low oxygen, HbS molecules polymerize into fibers that distort red cells into the sickle shape. The three genotypes have radically different fates in a malaria-endemic environment.

**HbAA** (normal): full susceptibility to falciparum malaria, the most lethal *Plasmodium* species. Historical childhood mortality from severe malaria in unsupplemented endemic areas: roughly 10%. Fitness wAA ≈ 0.9, selection coefficient sAA ≈ 0.10.

**HbAS** (sickle trait, heterozygote): ~40% of hemoglobin is HbS. Cells sickle only under extreme physiological stress. Crucially, the parasite cannot complete its intra-erythrocytic life cycle in HbAS red cells nearly as efficiently. Protection from severe malaria: roughly 90% reduction in severe-malaria mortality. Fitness wAS ≈ 1.0, the reference. sAS ≈ 0.

**HbSS** (sickle cell disease, homozygote): severe chronic anemia, vaso-occlusive crises, splenic infarcts, stroke, organ damage. Historical childhood mortality without treatment: up to 80%. Fitness wSS ≈ 0.2, sSS ≈ 0.80.

The heterozygote is fitter than either homozygote. This is heterozygote advantage, and it produces a stable polymorphism. Here is the math.

Let *q* be the frequency of HbS and *p* = 1 − *q* the frequency of HbA. Under Hardy-Weinberg, pre-selection genotype frequencies are p², 2pq, q². After selection, each genotype's contribution to the next gene pool is frequency × fitness:

- HbAA contributes: p² × (1 − sAA) = p² × 0.9
- HbAS contributes: 2pq × 1.0 = 2pq
- HbSS contributes: q² × (1 − sSS) = q² × 0.2

At equilibrium, *q* is not moving — the allele frequency change Δq = 0. Setting up and solving (standard Hartl & Clark derivation), the equilibrium HbS frequency is:

> **q\* = sAA / (sAA + sSS)**

Plug in numbers:

q\* = 0.10 / (0.10 + 0.80) = 0.10 / 0.90 = **0.111**

The model predicts HbS should sit at about 11% in malaria-endemic West Africa. The observed frequency: roughly 0.08–0.12 across the malaria belt. The agreement is within the rounding error of the selection coefficients.

That is the chapter's deep-dive result. *One division predicts the equilibrium frequency of a clinically significant allele in a real human population to within a percentage point.* The math works because the biology is exactly what the model says: heterozygotes have a fitness advantage in the malarial environment, both homozygotes pay a cost, and selection balances the two costs at the predicted equilibrium.

<!-- → [CHART: Two-panel figure — left panel: fitness landscape showing wAA, wAS, wSS on the y-axis and the three genotypes on the x-axis, with wAS highest and an arrow labeled "heterozygote advantage"; right panel: allele-frequency dynamics over 100 generations starting from three different values of q (0.01, 0.50, 0.99), all converging to q* ≈ 0.111 — arrows showing convergence from above and below; annotated with the equilibrium equation q* = sAA/(sAA + sSS)] -->

The equilibrium is **stable** — if *q* is perturbed above 0.111, selection against HbSS homozygotes increases faster than selection against HbAA decreases, pulling *q* back down. If *q* drifts below 0.111, selection against HbAA homozygotes via malaria pulls it back up.

Now change the environment. Eradicate falciparum malaria. The malaria cost sAA drops toward zero. The equation becomes:

q\* = 0 / (0 + sSS) = 0

There is no longer any equilibrium maintaining HbS. With malaria gone, every HbS allele is purely deleterious: heterozygotes are no better off than HbAA, and HbSS homozygotes still pay a severe fitness cost. The HbS allele is now under classical directional selection against a mostly-recessive. Expected trajectory: slow decline toward loss.

How slow? With sSS = 0.8 and starting *q* = 0.10, the per-generation change is roughly Δq ≈ −sSS × q² × p ≈ −0.8 × 0.01 × 0.9 ≈ −0.007. The allele frequency drops about 0.7% per generation. It takes 10–15 generations to halve from 0.10 to 0.05.

Test the prediction against a real population that has recently moved out of malaria endemicity. African Americans are descended primarily from West Africans, with the majority of the gene flow occurring 10–15 generations ago. North America has had much less endemic falciparum malaria than West Africa. The observed HbS allele frequency in African Americans today is approximately 0.04 — about 40% of the West African ancestral value. That decline is roughly what the directional-selection equation predicts for 10–15 generations of relaxed malaria selection while the HbSS mortality cost continues.

The framework predicts not just the equilibrium in West Africa but the *decline in a population that moved away from the selecting environment*. Both predictions roughly match. Population genetics works.

<!-- → [IMAGE: Geographic map overlay — HbS allele frequency plotted on a map of Africa and neighboring regions, color-coded from low (blue, ~0.01) to high (red, ~0.15); overlaid contour lines showing historical malaria endemicity; the near-perfect spatial correlation between HbS frequency and malaria burden visible as aligned gradients — annotated: "The distribution of HbS mirrors the historical distribution of P. falciparum"] -->

---

## Which force wins where

The five forces all act simultaneously in any real population. The question is which dominates.

**Selection vs. drift.** The parameter *Ne* × *s* decides. When *Ne* × *s* >> 1, selection controls the outcome. When *Ne* × *s* << 1, drift controls it. For humans at *Ne* = 10,000, an allele with s = 10⁻⁵ has *Ne* × *s* = 0.1 — effectively neutral. An allele with s = 0.01 has *Ne* × *s* = 100 — selection wins decisively.

This explains the neutral theory: most molecular variation has very small fitness effects. For typical *Ne* and typical per-locus selection coefficients, drift accounts for more of the observed molecular variation than selection does. Kimura's 1968 insight — most molecular evolution is drift on neutral mutations, not selection — transformed the field.

**Selection vs. gene flow.** If local selection favors an allele but migration keeps importing the alternative allele, the local population stabilizes at a balance. The competition is *s* vs. *m*: if *m* >> *s*, migration prevents local adaptation. The peppered moth at intermediate pollution levels showed intermediate dark-allele frequencies — selection pulling one way, gene flow from adjacent populations diluting it.

**Mutation-selection balance.** For deleterious recessive alleles, q* ≈ √(μ/s). Many rare recessive diseases sit at frequencies consistent with this balance — neither going extinct (because mutation regenerates them) nor rising to common levels (because selection removes them). The disease persists forever at low frequency.

The summary: **large populations with strong selection produce deterministic directional change or stable polymorphisms. Small populations wander by drift. Intermediate populations show a mix, and which force dominates depends on *Ne* × *s* for selection/drift and *m* vs. *s* for gene flow/selection.** Most real-world cases are in the intermediate regime, with multiple forces contributing. The framework handles all of them with the same five equations.

<!-- → [TABLE: Five forces of evolution — columns: force, violated HWE assumption, what it does to allele frequencies, key parameter, worked example from this chapter — rows: Mutation (no mutation assumed, introduces new alleles, μ per locus per generation, peppered moth cortex insertion), Natural selection (equal fitness assumed, directional change or equilibrium, selection coefficient s, sickle cell balanced polymorphism), Genetic drift (infinite population assumed, random walk toward fixation/loss, 1/Ne, Amish founder effect / cheetah bottleneck), Gene flow (closed population assumed, homogenization between populations, migration rate m, Florida panther genetic rescue), Non-random mating (random mating assumed, genotype frequencies change without allele frequency change, inbreeding coefficient F, Ellis-van Creveld in Lancaster Amish)] -->

---

## What the chapter built

Hardy answered Yule's question in an afternoon, and the answer was: allele frequencies do not change because dominance doesn't drive frequency. They change only when one of five forces acts. The equation — p² + 2pq + q² = 1 — is where you start, and every real population deviates from it by the amount and direction that the five forces predict.

Mutation supplies the variation. Selection sorts among variants — directionally if one homozygote dominates, toward a stable balance if the heterozygote wins. Drift moves frequencies randomly, more strongly as *Ne* shrinks, pushing populations toward fixation or loss in the long run. Gene flow homogenizes neighboring populations, rescues isolated ones, and sets a floor on local adaptation. Non-random mating reshuffles the diploid combinations, exposing the recessive alleles that random mating would hide in perpetual heterozygosity.

The sickle cell case is the chapter's deep-dive because it is clean: one locus, two alleles, large effects, measurable selection coefficients, a real population with real data. The equilibrium frequency q\* = sAA / (sAA + sSS) ≈ 0.111 matches the observed 0.08–0.12. The decline in the African-American population over 10–15 generations roughly matches the relaxed-selection prediction. The geographic distribution of HbS mirrors the historical distribution of falciparum malaria.

The framework works on a case where we can check it. The same framework — with messier parameters — applies everywhere else.

---

## LLM Exercise — Build your population genetics simulator

### The simulation prompt

```
Show: Read CLAUDE.md and DESIGN.md from this project. Conform to them.

Say: Build 10-population-genetics.html — a Hardy-Weinberg +
five-forces population genetics simulator.

Controls:
- Starting allele frequency p₀ (slider 0.01 to 0.99, default 0.5)
- Effective population size Ne (log slider: 10 to 100,000)
- Selection coefficients sAA, sAa, sSS (each 0 to 1, independent
  sliders) where wAA = 1 - sAA, wAa = 1 - sAa, wSS = 1 - sSS
- Mutation rate μ (slider, default 1e-5)
- Gene flow rate m from external population with allele frequency
  p_external (slider 0 to 0.5)
- Number of generations (slider 50–500, default 200)
- Number of replicates (slider 1–20, default 10)

Display:
Primary panel: line plot of allele frequency p vs. generation.
One semi-transparent line per replicate. Solid black line: the
deterministic expectation (selection + gene flow, no drift).
Dashed horizontal line: theoretical equilibrium q* = sAA /
(sAA + sSS) when sAA > 0 and sSS > 0 and sAa = 0.

Secondary panel: at user-selected generation, a bar chart of
observed genotype frequencies vs. Hardy-Weinberg expected
values side by side (AA in dark blue, Aa in medium blue,
aa in light blue, expected as outlined bars).

Force-balance indicator: a small labeled gauge showing which
force is currently dominant (selection / drift / gene flow /
mutation) based on the parameter magnitudes: selection dominant
when Ne × max(sAA, sSS) > 10; drift dominant when Ne <
1 / max(sAA, sSS, m); gene flow dominant when m > max(sAA,
sSS) / 10.

Three preset buttons:
1. "Pure drift (small pop)": Ne=50, all s=0, μ=0, m=0, p₀=0.5.
   Should show stochastic wandering; some replicates fix at 1,
   others at 0; mean stays near 0.5.
2. "Directional selection (large pop)": Ne=10,000, sAA=0,
   sAa=0, sSS=0.5, μ=0, m=0, p₀=0.1. Should show the q allele
   declining toward loss along the deterministic trajectory.
3. "Sickle cell balanced polymorphism": Ne=10,000, sAA=0.1,
   sAa=0, sSS=0.8, μ=0, m=0, p₀=0.5. Should converge to
   q* = 0.10/0.90 ≈ 0.111 from any starting frequency.

Constrain: Single SVG canvas 800×500 for primary panel, 400×300
for secondary and force-balance panels. Single self-contained
HTML file, D3 v7 from CDN, no other dependencies. Color palette:
replicate lines #85c1e9 (semi-transparent), deterministic line
#1a5276 (solid), equilibrium line #e67e22 (dashed). Genotype
colors: AA #1a5276, Aa #2980b9, aa #85c1e9.

Add at top of script:
// CLAIM 1: At HWE, genotype frequencies are p², 2pq, q².
// CLAIM 2: Equilibrium under heterozygote advantage:
//   q* = sAA / (sAA + sSS), stable.
// CLAIM 3: Drift variance per generation = pq / (2Ne).
// CLAIM 4: Selection dominates drift when Ne × s >> 1.

Verify: Print to console on each parameter change as PASS/FAIL:
(1) Preset 3 (sickle cell): after 500 generations in a large
    population (Ne=10,000), mean allele frequency across
    replicates should be within 0.02 of q* = 0.111.
(2) Preset 1 (pure drift): after 200 generations at Ne=50,
    the fraction of replicates fixed at 0 or 1 should exceed
    0.3 (approximately expected from theory: 1 - e^(-t/2Ne)
    after t generations).
(3) Hardy-Weinberg genotype frequencies at generation 0 in
    secondary panel should equal p₀², 2p₀q₀, q₀² (PASS if
    within 0.001 of expectation in a large population preset).
```

### Exploration tasks

Once the simulation runs:

1. **Hardy-Weinberg baseline.** Set all selection coefficients to 0, μ = 0, m = 0, Ne = 100,000. Run 200 generations from p₀ = 0.3. Observe that the allele frequency lines are essentially flat at 0.3, and the secondary-panel genotype frequencies match p² : 2pq : q² = 0.09 : 0.42 : 0.49 throughout. This is Hardy's point: without any force, nothing moves.

2. **Drift vs. selection.** Set sAA = 0, sSS = 0.1. Run the simulation at Ne = 100 and Ne = 10,000 for 200 generations, p₀ = 0.5. At Ne = 100, many replicates will drift to fixation or loss; the deterministic prediction (q allele declining) is present but masked by noise. At Ne = 10,000, the replicates cluster tightly around the deterministic prediction. The transition from "drift wins" to "selection wins" is visible at around Ne × sSS ≈ 1, i.e., Ne ≈ 10 for sSS = 0.1.

3. **The sickle cell convergence.** Load the sickle cell preset. Run 10 replicates from p₀ = 0.5. Watch the allele frequency converge to q* ≈ 0.111. Now change p₀ to 0.01 and run again — convergence from below. Now change p₀ to 0.95 and run — convergence from above. The equilibrium is an attractor: it pulls the population in from any starting point. Now reduce Ne to 100 with the same selection coefficients. Observe that drift can now pull replicates away from the equilibrium and occasionally drive the allele to fixation or loss despite the heterozygote advantage.

4. **Mutation-selection balance.** Set sAA = 0, sSS = 0.5, μ = 1e-5, Ne = 100,000, p₀ = 0.999 (nearly all A). Run 500 generations. The q allele should drift up from near zero and stabilize around q* ≈ √(μ/sSS) = √(2 × 10⁻⁵) ≈ 0.0045. This is mutation-selection balance: new mutations continually feed the a allele in while selection against aa removes it.

### Extension prompt

```
Extension: Add a fourth panel — Sickle Cell in Changing
Environment. Runs automatically in sequence:
Phase 1 (generations 1–200): sAA=0.1, sSS=0.8, Ne=10,000,
  p₀=0.5. Population converges to q* ≈ 0.111.
Phase 2 (generations 201–400): sAA drops to 0 (malaria
  eradicated). sSS remains 0.8. Label the phase boundary
  with a vertical dashed line annotated "malaria eradicated."
  The HbS allele should now decline as directional-selection-
  against-recessive with rate Δq ≈ -sSS × q² × p per generation.
Phase 3 (optional, button-activated): Add gene flow m=0.05
  from a population still at HbS frequency 0.10 (migrants
  from a still-endemic region). Observe that gene flow
  slows the decline.

Display the theoretical prediction as a solid black line
throughout all three phases. Annotate the observed African-
American HbS frequency (~0.04 at generation 215, i.e., ~15
generations after phase 1 ends) as a data point with error bars.

This extension makes the historical prediction testable: the
model predicts both the West African equilibrium AND the
African-American decline, using the same selection coefficients.
```

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Godfrey Harold Hardy** sent his three-page letter to *Science* in 1908, proving that allele frequencies do not change under random mating alone. **Wilhelm Weinberg** derived the same result independently the same year, from medical-genetic data in Germany.

**Run this:**

```
Who was G. H. Hardy, and what was his attitude toward applied
mathematics and biology? Keep it to three paragraphs. End with
the single most surprising thing about his career or his famous
views on the usefulness of mathematics.
```

→ Search **"G. H. Hardy mathematician"** on Wikipedia. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain the difference between Yule's 1902 argument (dominant alleles should take over) and Hardy's 1908 reply, at the level someone with a high-school biology course could follow.
- Ask it to compare the Hardy-Weinberg equilibrium to other "null models" in science — what other null models in physics, chemistry, or ecology play the same logical role?

What changes? What gets better? What gets worse?
