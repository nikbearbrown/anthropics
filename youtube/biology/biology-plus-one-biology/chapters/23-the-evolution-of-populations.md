# Chapter 23 — Evolution of Populations: The Invisible Hand of Allele Frequencies
*How to watch evolution happen by counting.*

---

In 1848, a single dark moth appeared in Manchester, England.

Every other peppered moth in the region was pale and speckled — patterned to disappear against the lichen-covered bark of trees. This one individual was dark. One insect, one mutation, in a population of thousands.

By 1895, nearly all the peppered moths in Manchester were dark.

I want you to hold that fact for a moment. Forty-seven years. One variant goes from vanishingly rare to nearly universal. Not because dark moths decided to become dark. Not because they learned anything. Because soot from factories coated the trees, pale bark disappeared, pale moths became visible to birds, and pale moths got eaten. The dark ones did not. The dark ones bred. Their dark offspring bred. A rare allele — a variant form of a gene — went from one copy to common to dominant.

This is evolution. Not the evolution of a new species, not the transformation of one body plan into another — that comes later and over much longer timescales. This is evolution as it is actually measurable: a change in allele frequencies in a population over time.

That is the whole definition. Not a metaphor, not a narrative arc about progress or improvement. A number — the proportion of some genetic variant in a population — changes from one generation to the next. When that happens, the population has evolved.

Everything in this chapter rests on that definition. Let me show you what you can do with it.

---

## Counting Alleles

Every gene in a diploid organism exists in two copies. One from the mother, one from the father. A population is the sum of all the copies of all the genes in all the individuals. That collection is the gene pool.

Take a simple gene with two variants: allele A and allele a. A population of 500 individuals contains 1,000 copies of this gene in total. Count the As. Divide by 1,000. That is the frequency of A — call it p. Count the as. Divide by 1,000. That is the frequency of a — call it q. By definition, p + q = 1. The two frequencies must sum to one because every allele is either A or a.

If you return to this population a generation later and count again, and p has changed, the population has evolved. This is not a metaphor. Evolution is visible in those numbers.

The ABO blood type system makes this concrete. Three alleles exist for the ABO gene in humans: I^A, I^B, and I^0. A survey of Jordanians found that I^A made up 26.1 percent of all ABO alleles in that population. I^B: 13.4 percent. I^0: 60.5 percent. If those percentages shift over generations — if I^0 becomes more common, if I^A becomes rarer — that population's genetics are changing. It is evolving.

<!-- → [INFOGRAPHIC: Two bar charts side by side — left: ABO allele frequencies in the Jordanian population (I^A: 26.1%, I^B: 13.4%, I^0: 60.5%) labeled as "Generation 1"; right: a hypothetical shifted distribution labeled "Generation 2" with I^0 slightly higher — annotated to show that a change in bar heights between generations is the literal definition of evolution at the population level] -->

Allele frequencies matter more than genotype frequencies for a reason that is easy to miss. Genotypes are temporary. They exist in one individual, for one lifetime, and disappear. Alleles persist across generations, passed from parent to offspring, reshuffling in new combinations but persisting in the gene pool as long as they are not lost. If you want to track what a population is doing, track the alleles.

Now the question: what makes allele frequencies change?

---

## The Baseline: What Happens When Nothing Happens

Before you can measure change, you need a reference point for no change. In 1908, a mathematician named Godfrey Hardy and a physician named Wilhelm Weinberg independently worked out what should happen to allele frequencies in a population if nothing is acting to change them.

Their answer: nothing changes. If the population is large, mates randomly, experiences no mutation, receives no migrants, and is subject to no natural selection, then allele frequencies stay exactly the same generation after generation.

The algebra is simple. Let p be the frequency of allele A and q be the frequency of allele a, with p + q = 1. If individuals mate randomly, the probability of inheriting A from one parent is p. The probability of inheriting A from the other parent is also p. So the probability of being AA is p². The probability of being aa is q². The probability of being Aa is 2pq — you can get A from the first parent and a from the second, or a from the first and A from the second.

Thus the genotype frequencies should be:

$$p^2 + 2pq + q^2 = 1$$

This is the Hardy-Weinberg equation. It is a prediction: if the five conditions hold, genotype frequencies follow this formula, and allele frequencies stay constant from generation to generation.

The five conditions are: large population size, random mating, no mutation, no migration, no natural selection.

No real population satisfies all five. Every real population is finite. All have mutation. Most have some migration. Mating is rarely fully random. Selection is omnipresent.

That is exactly the point. Hardy-Weinberg is not a description of what populations do. It is a null hypothesis — a baseline of what populations would do if evolution were not happening. Compare a real population to the prediction. If the numbers match, nothing detectable is changing. If they deviate, something is shifting the allele frequencies. Your job is to figure out what.

Here is how to use it. Suppose violet flower color (V) is dominant over white (v) in a plant population. You observe 400 white flowers out of 500 plants. White flowers must be vv, so q² = 400/500 = 0.8. Square root: q ≈ 0.894. Then p ≈ 0.106.

Hardy-Weinberg predicts: about 5.6 VV plants, about 94.4 Vv plants, about 400 vv plants. You observed 100 violet and 400 white — consistent with the prediction. This locus is in equilibrium. No detectable evolution.

Return in ten years. Now 350 white and 150 violet. Recalculate: q² = 350/500 = 0.7, q ≈ 0.837. The allele frequency has shifted. Something is changing the numbers. Evolution is occurring. Now you investigate which mechanism is responsible.

<!-- → [TABLE: Hardy-Weinberg worked example laid out as a two-column comparison — "Year 1 observation" vs. "Year 10 observation" — rows: observed phenotype counts, calculated q², calculated q, calculated p, expected genotype frequencies (p², 2pq, q²), conclusion (equilibrium vs. deviation) — annotated to show the detective logic: observed deviation → something is changing allele frequencies → investigate which mechanism] -->

---

## The Mechanisms

There are exactly five ways allele frequencies can change. Understanding each one means understanding what signature it leaves in the population's genetics.

<!-- → [TABLE: Five-mechanism summary — rows: natural selection, genetic drift, gene flow, mutation, nonrandom mating — columns: what it changes, direction/predictability, strongest in which conditions, signature deviation from Hardy-Weinberg — designed as an orientation reference before the detailed sections below] -->

**Natural selection** is the only mechanism that tends to produce adaptation. It works because some individuals survive and reproduce more than others, and that survival is partly heritable — tied to the alleles they carry.

The key concept is relative fitness. You do not care how many offspring an individual produces in absolute terms. You care whether it produces more or fewer than the population average. An individual producing five offspring when the average is three has a relative fitness above one. Natural selection favors it. Its alleles become more common.

Selection takes three forms, and they produce measurably different outcomes.

Stabilizing selection favors the middle and culls the extremes. Human birth weight is the classic example: very small babies and very large babies face higher mortality; intermediate-weight babies survive best. Over generations, the distribution of birth weights narrows. Variation decreases. The population becomes more uniform.

Directional selection favors one extreme. The peppered moth story is directional: industrial soot shifted the environment, and one end of the spectrum — dark moths — suddenly had the advantage. The population's average shifted toward that end. The pale allele became rare.

Diversifying selection favors both extremes over the middle. Side-blotched lizards in California carry three male throat colors: orange, blue, and yellow. Orange males are aggressive and take territories. Blue males form pair bonds and guard mates. Yellow males mimic females and sneak matings. Orange beats blue in fights, but blue males guard against orange. Yellow sneaks past orange, but blue males guard against yellow. The system cycles like rock-paper-scissors: when orange is common, blue does well; when blue is common, yellow does well; when yellow is common, orange does well. No single morph ever wins permanently. The population maintains all three types, cycling through changing frequencies.

<!-- → [INFOGRAPHIC: Three bell-curve diagrams showing the effect of each selection mode on a trait distribution — stabilizing: original broad bell narrows over time, mean unchanged; directional: bell shifts left or right over time; diversifying: single bell splits into two peaks over time — annotate what happens to genetic variation in each case (decreases / shifts / increases)] -->

What selection cannot do is equally important. It can only act on variation that already exists. If a beneficial allele is absent, selection cannot create it. Selection shapes what is there — it does not conjure new options.

**Genetic drift** is the one that surprises people most, because it has nothing to do with fitness or adaptation. It is random sampling error, and it is always present.

Think of it this way. A population of ten individuals contains some number of copies of each allele. By pure chance, some individuals reproduce more than others this generation — not because they are better, but because accidents happen. An animal gets struck by lightning. A plant's seeds land in a dry patch. A fish gets caught in a net. The survivors are a random subsample of the population, and their alleles are a random subsample of the gene pool. In the next generation, the allele frequencies reflect that random draw.

In a large population, the random errors average out. One unlucky individual does not much change the frequencies out of thousands. But in a small population, every individual death or reproductive success is a large fraction of the gene pool. Drift dominates. Allele frequencies lurch unpredictably. Beneficial alleles can be lost by bad luck. Harmful alleles can spread by good luck. There is no directionality, no goal, no adaptation. Just noise.

The bottleneck effect is drift at its most brutal. A disaster — a disease, a volcanic eruption, a severe winter — kills most of the population randomly. The survivors are not the fittest; they are the lucky. Their alleles now represent the entire gene pool. Cheetahs passed through such a bottleneck thousands of years ago and today are so genetically uniform that skin grafts between unrelated individuals are rarely rejected — the immune system cannot recognize them as foreign.

The founder effect is bottleneck in miniature. A small group of individuals colonizes a new location. Whatever alleles those few founders carry become the basis of the new population's gene pool. Rare alleles in the source population can become common in the new one simply because a founder happened to carry them. The Amish in Pennsylvania show elevated rates of certain rare genetic diseases — not because those diseases are advantageous, but because the founders of the community happened to carry the responsible alleles at elevated frequency, and the community has remained largely isolated since.

<!-- → [INFOGRAPHIC: Bottleneck effect diagram — large diverse population on the left (many different colored dots representing alleles); a narrow bottleneck in the middle (labeled "disaster: survivors are a random sample"); small, less diverse surviving population on the right — annotate that the right side reflects chance, not fitness; include a second panel showing the founder effect: a few individuals dispersing from a large population to colonize a new island, carrying only the alleles they happened to possess] -->

**Gene flow** is the movement of alleles between populations via migration. Animals move, pollen drifts, seeds travel. When an individual migrates to a new population and breeds, it introduces its alleles. The frequencies in both the source and destination populations shift.

The main effect of gene flow is homogenization. Neighboring populations that exchange migrants become more genetically similar over time. This is why species distributed across large geographic areas often show gradual variation rather than sharp boundaries — alleles diffuse slowly from one region to the next, producing clines instead of walls. It is also why conservation biologists sometimes deliberately move individuals between isolated wildlife populations: to prevent drift from impoverishing each population's genetics, and to provide the benefits of new allele combinations.

**Mutation** introduces genuinely new alleles — variants that have never existed before in any individual. DNA replication is not perfect. Occasionally a base is copied incorrectly. Occasionally a segment is deleted or duplicated. The resulting allele may be harmful, neutral, or rarely beneficial. Mutation rates are slow — roughly one error per hundred million base pairs per replication — but over billions of individuals and thousands of generations, mutations are constant. They are the ultimate source of all genetic variation. Without mutation, selection and drift would grind populations down to fixation at every locus, and there would be no variation left to act on.

**Nonrandom mating** changes genotype frequencies without necessarily changing allele frequencies. If individuals preferentially mate with others like themselves — which happens often, since many organisms choose mates based on observable traits — then homozygotes become more common than Hardy-Weinberg predicts, and heterozygotes become rarer. This has consequences. Rare recessive alleles that hide safely in heterozygotes become exposed in homozygotes, where their effects can be seen by selection. Inbreeding depression — reduced fitness in inbred populations — is the result. Zoo managers meticulously avoid mating closely related individuals for exactly this reason.

Sexual selection is a special case of nonrandom mating. One sex — usually females in animals with large investment in offspring — chooses mates based on traits. The peacock's tail is the famous example. The tail is metabolically costly to grow, physically cumbersome, and makes the male more visible to predators. By every survival measure, it is harmful. Yet peahens prefer males with larger tails, and so larger-tailed males reproduce more, and the alleles for large tails persist and spread.

Why would females evolve to prefer a trait that harms its bearer? The handicap principle offers an answer: a male who can survive despite carrying such a costly ornament must be extraordinarily healthy. The tail is an honest signal of genetic quality, because only a genuinely fit male can afford it. Females who choose those males give their offspring better genes. The preference and the ornament co-evolve, each driving the other.

---

## How the Mechanisms Interact

In the real world, all five mechanisms operate simultaneously, and the outcome depends on which is strongest.

Selection wins when the population is large and fitness differences between alleles are large. When Manchester trees were coated in soot, the fitness difference between dark and pale moths was enormous. Selection was so strong that in fewer than fifty generations the dark allele went from rare to nearly universal. Drift could not resist it — the population was too large and the selective advantage too great.

Drift wins when the population is small or when alleles are nearly neutral. In the Amish community, rare deleterious mutations persist not because they provide any advantage, but because drift in a small isolated population is strong enough to prevent selection from eliminating them. A mutation that reduces fitness by 0.1 percent is nearly invisible to selection in a population of a few thousand. Drift can easily fix it.

Gene flow can counteract local selection. A local population experiencing selection toward a particular allele might never achieve it if migrants constantly arriving from other populations carry different alleles. Conversely, gene flow can rescue a small population from inbreeding depression, bringing new alleles that reduce the concentration of harmful recessives.

The interaction between selection and drift is especially important for conservation. An endangered species reduced to a few hundred individuals loses alleles to drift regardless of selection. Beneficial alleles can vanish by chance before selection has a chance to spread them. Harmful alleles can become fixed. If the population cannot be enlarged, its evolutionary potential erodes. This is why wildlife managers track not just the number of individuals in a population but the effective population size — the number that actually contribute genes to the next generation — and work to maintain genetic diversity as a hedge against future environmental change.

<!-- → [CHART: Conceptual diagram showing selection strength vs. population size as two axes — four quadrants labeled: large population + strong selection = "selection dominates, rapid adaptation"; large population + weak selection = "slow drift and selection both matter"; small population + strong selection = "selection may overcome drift if advantage is large enough"; small population + weak selection = "drift dominates, random walk" — annotated with real examples in each quadrant: peppered moths (large/strong), neutral mutations (large/weak), Amish rare alleles (small/weak)] -->

---

## What Evolution Is Not

The peppered moth story is sometimes told as a story of progress: moths getting better. The implication is that evolution moves toward improvement, toward fitness, toward some optimum.

This is wrong.

Evolution is a change in allele frequencies. Drift changes allele frequencies randomly — no direction, no improvement, no goal. Gene flow changes allele frequencies by mixing — indifferent to whether the arriving alleles are beneficial or harmful in the new context. Mutation introduces new alleles randomly — most of them neutral or harmful. Nonrandom mating rearranges alleles without caring whether the resulting genotypes are fitter.

Only selection tends toward adaptation, and even selection is constrained. It can only work with existing variation. It acts on the whole organism, not individual genes — a beneficial allele linked to a harmful one will rise or fall with its neighbor. It can trap populations in local optima where the intermediate phenotype between two well-adapted forms is worse than either, making it impossible to traverse from one to the other.

Evolution is the net result of all five mechanisms acting simultaneously. Sometimes the net result is a beautifully adapted organism. Sometimes it is a population accumulating harmful mutations because drift is too strong to allow selection to clean them out. Sometimes it is a population becoming genetically impoverished through bottlenecks and founder effects. The machinery is mechanistic, not teleological. It has no destination.

---

## Reading a Population

Here is what I want you to take away: a population is a distribution of alleles, not a collection of individuals. Its future depends on how those allele frequencies change, which depends on the balance of five forces.

Count the alleles. Compare to Hardy-Weinberg. If they match, no detectable evolution is occurring at that locus. If they deviate, something is changing the numbers. Then ask: what? Is the population small? Drift may dominate. Has the environment changed? Selection may be driving a shift. Is migration high? Gene flow may be homogenizing nearby populations. Are mating patterns skewed? Nonrandom mating may be exposing recessive alleles.

The machinery is visible if you know how to look. And the way to look is to count.

When I find myself thinking about this carefully, what strikes me is the same thing that strikes me about every powerful framework in biology: the simplicity of the underlying logic given the complexity of the outcome. Two numbers — p and q — constrained to sum to one. Five mechanisms that can change them. An equation that predicts stability when nothing acts. Everything else — the dark moths, the spotted lizards, the cheetah's lost diversity, the Amish farmer with a rare disease — follows from those simple facts.

It is, in the end, just arithmetic. The arithmetic of who is alive, who breeds, and what they carry.

---

## Exercises

**Warm-up**

1. A gene has two alleles, B and b. In a population of 200 individuals, you count 280 copies of B and 120 copies of b. Calculate p (frequency of B) and q (frequency of b). Verify that p + q = 1. *Tests: basic allele frequency calculation from a count.*

2. Using the allele frequencies from question 1, calculate the expected genotype frequencies (BB, Bb, bb) under Hardy-Weinberg equilibrium. How many individuals of each genotype would you expect in a population of 200? *Tests: applying the Hardy-Weinberg equation to produce expected values.*

3. You observe the actual genotypes in that population: 90 BB, 100 Bb, 10 bb. Do the observed values match the Hardy-Weinberg expectations? Calculate the observed allele frequency from these genotype counts and compare it to the p you calculated from the original count. *Tests: detecting deviation from equilibrium and interpreting it as a signal of evolution.*

**Application**

4. A population of 20 mice lives on a small island. By chance, three mice die in a storm — not the weakest mice, just three unlucky ones. Explain why this event would change allele frequencies even if no allele confers any survival advantage. What would happen differently if the same storm hit a population of 20,000 mice? *Tests: applying the logic of genetic drift and understanding its relationship to population size.*

5. A rare recessive allele (frequency q = 0.02) causes a metabolic disease when homozygous. In a large outbred population, calculate the expected frequency of affected individuals (q²). Now suppose the population passes through a bottleneck and the allele frequency rises to q = 0.15 in the survivors. Recalculate the expected frequency of affected individuals. What does this illustrate about the relationship between bottlenecks and genetic disease? *Tests: quantitative application of drift and bottleneck effects using Hardy-Weinberg.*

6. Two neighboring bird populations have different frequencies of a wing-color allele: population A has 70% dark allele, population B has 20% dark allele. Over ten generations, birds regularly migrate between the populations. Predict the direction of change in each population's allele frequency, and describe what the long-term outcome of sustained gene flow would be. *Tests: applying gene flow logic to a specific scenario.*

**Synthesis**

7. Peppered moths in Manchester showed rapid directional selection toward dark coloration during industrialization, then reversed toward pale coloration when air pollution decreased. Explain why selection could reverse the direction of allele frequency change, but drift alone could not reliably reverse it. Under what conditions might drift have reversed the direction — and why would that outcome be less predictable? *Tests: comparing the directionality of selection vs. the randomness of drift in the same population.*

8. A conservation biologist is managing a captive population of 50 mountain gorillas for eventual reintroduction to the wild. She is concerned about both inbreeding depression and loss of genetic diversity over time. Using the mechanisms covered in this chapter, explain which mechanisms threaten this population and propose two practical interventions — one addressing genetic drift and one addressing nonrandom mating — that could improve the population's long-term viability. *Tests: applying multiple mechanisms simultaneously to a conservation scenario.*

**Challenge**

9. The side-blotched lizard maintains three male color morphs (orange, blue, yellow) in stable cycling frequencies through a rock-paper-scissors dynamic. From a Hardy-Weinberg perspective, this population is not in equilibrium — frequencies cycle rather than stabilize. Yet the three morphs persist indefinitely. This seems to contradict the expectation that directional selection should eventually fix one allele. Explain why this cycling pattern represents a form of long-term stability, and what would have to change in the environment or the fitness relationships to break the cycle and allow one morph to become fixed. *Tests: applying selection logic to a frequency-dependent fitness system, reasoning about conditions for fixation.*

10. A human population on a remote island has been isolated for 200 generations. A researcher finds that one allele at a particular locus has risen from a frequency of 0.01 (estimated from the founding population) to 0.35 today. The allele appears to have no effect on survival or reproduction in lab studies. Propose two different mechanisms that could explain this increase, explain how you would distinguish between them empirically, and describe what evidence would allow you to rule out natural selection as a cause. *Tests: designing an inference strategy to distinguish drift from selection using allele frequency data and population history.*

---

## LLM Exercises

The following exercises are designed for use with a large language model. Paste the prompt into any capable model and examine the response critically — not for correctness alone, but for whether the reasoning is mechanistic or merely verbal.

**Exercise 1 — Hardy-Weinberg as null hypothesis**
Prompt a model: *"The Hardy-Weinberg equilibrium states that in a population not undergoing selection, mutation, gene flow, drift, or non-random mating, allele frequencies remain constant across generations and genotype frequencies follow p² + 2pq + q². Walk me through why this equilibrium serves as the null hypothesis for population genetics: what does it mean to test 'whether evolution is occurring' by checking departures from Hardy-Weinberg? Identify one specific allele in human populations and predict whether you would find Hardy-Weinberg equilibrium for it."*

Evaluate whether the model correctly identifies that Hardy-Weinberg provides a null model, and that departure from the predicted genotype frequencies indicates one or more of the five forces is at work. The CCR5-Δ32 deletion in European populations is a classic example of departure from equilibrium due to historical selection (possibly plague-related).

**Exercise 2 — Computing allele frequency changes from fitness**
Prompt: *"In a population, the AA genotype has fitness 1.0, Aa has fitness 1.0, and aa has fitness 0.5 (the recessive allele a is partially deleterious). If the starting allele frequency of a is 0.3, predict the frequency of a after one generation of selection. Walk me through the calculation, including the average fitness of the population and the post-selection allele frequencies. After how many generations would a drop to 0.1, approximately?"*

Evaluate whether the model correctly applies the selection equations: q' = (q² × 0.5 + pq × 1.0) / mean fitness, with mean fitness = p² + 2pq + 0.5q². For q=0.3: q² = 0.09 contributes 0.045 to mean fitness; 2pq = 0.42 contributes 0.42; p² = 0.49 contributes 0.49 — mean fitness = 0.955. q' ≈ (0.09×0.5 + 0.21) / 0.955 ≈ 0.267. Approximately 5-7 generations to reach 0.1 [check arithmetic].

**Exercise 3 — Heterozygote advantage and balanced polymorphism**
Prompt: *"Sickle cell disease is the textbook example of heterozygote advantage maintaining a deleterious allele in a population. In malaria-endemic regions, HbA/HbS heterozygotes have higher fitness than either homozygote (HbA/HbA susceptible to malaria, HbS/HbS suffer sickle cell disease). Walk me through how to compute the equilibrium allele frequency in such a system, given specific fitness values. What happens to the equilibrium when malaria is eradicated?"*

Evaluate whether the model correctly identifies that the equilibrium frequency depends on the relative fitness disadvantages of the two homozygotes: q_eq = s_AA / (s_AA + s_aa), where s values are the selection coefficients against each homozygote. After malaria eradication, s_AA drops to ~0 and the HbS allele decays at the rate determined by s_aa.

**Exercise 4 — Effective population size as the relevant N**
Prompt: *"The effective population size (Nₑ) is typically much smaller than the census population size (N) — often 10-25% [verify]. Walk me through the factors that reduce Nₑ below N: unequal sex ratios, variance in reproductive success, population bottlenecks, and overlapping generations. Why does drift respond to Nₑ rather than N? For a hypothetical population of 10,000 individuals where only 100 effectively reproduce, what is Nₑ?"*

Evaluate whether the model correctly identifies that Nₑ measures the rate of genetic drift, which depends on the variance in offspring number rather than the total population. For the example, Nₑ ≈ 100 (limited by the 100 reproducers), so drift would be 100× faster than the naive N estimate would predict.

**Exercise 5 — Adaptation and the question of 'fitness'**
Prompt: *"In evolutionary biology, 'fitness' is defined as relative reproductive success — not strength, intelligence, or survival per se. Walk me through three specific cases where this distinction matters: (1) sexual selection producing traits that hinder survival but enhance mating, (2) genomic conflicts where a 'selfish' gene element spreads despite reducing organismal fitness, (3) longer-lived organisms with lower lifetime reproductive output than shorter-lived ones. For each, identify what 'fitness' means at the level of the gene vs. the organism."*

Evaluate whether the model engages with the gene-centered view (Dawkins) — fitness ultimately means the rate of allele transmission to subsequent generations, which can diverge from organismal interests (selfish genetic elements like meiotic drivers, transposons) — and the sexual-selection puzzle (peacock tails, elaborate bird-of-paradise displays) where traits that reduce survival increase mating success.

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Sewall Wright** built much of population genetics in the 1930s — including the concept of genetic drift, the F-statistics that quantify population structure, and the "adaptive landscape" metaphor that lets you visualize fitness across genotypes.

**Run this:**

```
Who was Sewall Wright, and how does his population genetics work — genetic drift, F-statistics, and adaptive landscapes — connect to the evolution of populations we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Sewall Wright"** on Wikipedia. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to draw an adaptive landscape with two peaks separated by a valley — and explain why a population might be stuck on the lower peak.
- Ask it to compare Wright's drift-focused view with R. A. Fisher's selection-focused view of how populations evolve.

What changes? What gets better? What gets worse?
