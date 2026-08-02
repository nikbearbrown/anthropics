# Chapter 2 — Mendel's Laws and Mendelian Inheritance

*The garden was the apparatus. The counting was the experiment.*

---

Here is what Gregor Mendel actually did that nobody before him had done.

He did not discover that traits are inherited — everyone knew that. He did not discover that offspring resemble parents — farmers had been selecting on that for ten thousand years. He did not even discover that hybrids sometimes revert to parental types in later generations — Charles Naudin in Paris had published nearly the same observation in 1862, three years before Mendel gave his talk. What Mendel did was count. He counted at a scale — something like 28,000 individual plants over eight years — that turned a pattern nobody else had noticed into a number so clean it demanded a mechanism. The number was 3:1. The mechanism he proposed for it is the foundation of genetics.

The question to hold through this chapter: *why does a 3:1 ratio force a particular model of inheritance?* When you understand that, you understand what Mendel actually discovered.

---

## The apparatus

Before Mendel made a single cross, he spent two years doing something that looks, from outside, like gardening. He was not gardening. He was building his experimental apparatus.

The apparatus was *Pisum sativum*, the common garden pea, and the reason it worked is three properties it has that most organisms do not.

First, reproductive control. Pea flowers are normally self-pollinating — each flower fertilizes itself before it opens. Left alone, a pea plant breeds true: all its offspring are genetically identical to it (setting aside mutation). When you want to cross two plants deliberately, you pry the flower open before it matures, clip out the anthers with tweezers before they release pollen, and then apply pollen from your chosen donor plant with a brush. The plant has no way to resist; it accepts whatever pollen you give it. This lets you specify exactly which two plants mate. Without this control, you are counting offspring from random crosses and the ratios are noise.

Second, pure-breeding lines with binary traits. Mendel chose seven characters, each appearing in exactly two forms: round or wrinkled seeds, yellow or green seeds, violet or white flowers, tall or dwarf stems, and three others. Every plant is unambiguously one or the other — no "medium-tall," no "slightly wrinkled." This binary classification is what makes counting ratios meaningful. If you try to measure stem height as a continuous number, you get a bell curve in the offspring, and there is no ratio to see. Mendel tested many traits before settling on these seven because most traits are not binary. The binary ones are rare and he found them.

<!-- → [TABLE: Mendel's seven pea traits — columns: character, dominant state (with symbol), recessive state (with symbol); rows: seed shape, seed color, pod shape, pod color, flower color, flower position, stem length. Student should see that every trait snaps between exactly two states with no intermediate category, which is what makes counting ratios possible.] -->

He then spent two years establishing *pure-breeding lines* — letting plants self-pollinate for generation after generation until the offspring of a tall plant were always tall and the offspring of a dwarf plant were always dwarf, with no exceptions. A pure-breeding line is, in modern language, homozygous: both copies of the relevant gene carry the same allele. Cross a pure-breeding tall plant (TT) with a pure-breeding dwarf plant (tt), and you know exactly what each parent contributed. There is no hidden third allele lurking in the background to mess up the ratios.

Third, fast generation time and large brood size. Each pea plant flowers and sets seed in one growing season. Each plant produces dozens of pods. Each pod contains five to nine seeds. Self-pollinate a single F₁ plant and you get hundreds of F₂ seeds. Mendel grew thousands of F₁ plants per cross. The total F₂ counts in his 1866 paper: 7,324 seeds for the seed-shape cross; 8,023 for seed color; across all seven traits, something close to 20,000 individual plants and seeds. The 3:1 ratio is invisible in a sample of ten. At 7,000, it is unmissable.

Kölreuter and Naudin had done hybridization experiments before Mendel. Neither extracted laws. The difference was not cleverness — they were sharp observers. The difference was that Mendel turned the garden into an apparatus that could produce numbers sharp enough to force a theory.

---

## The first experiment — and why the result is strange

Take the seed-shape character. Establish a pure-breeding round line (RR) and a pure-breeding wrinkled line (rr). Cross them. Collect the seeds. Every F₁ seed is round.

Not "mostly round." Not "round on average." Every single one. The wrinkled character vanished completely.

This contradicted the dominant theory of inheritance of the time, which was blending inheritance: the intuition that offspring are mixtures of their parents, the way mixing red paint with white paint gives pink. Blending inheritance predicts a blend. Mendel got one parent's trait, complete, in every offspring. The wrinkled character was not diluted. It was gone.

Now Mendel had to decide: was the wrinkled character *destroyed* by crossing with round, or was it *hidden*? If destroyed, selfing the F₁ plants should produce only round offspring forever — there is no wrinkled left to come back. If hidden, selfing the F₁ plants should show some wrinkled offspring — and the proportion in which they returned would tell you something about what was going on inside.

He grew 929 F₂ plants from the flower-color cross: 705 violet, 224 white. Ratio: 3.15 to 1. For seed shape, 7,324 F₂ seeds: 5,474 round, 1,850 wrinkled. Ratio: 2.96 to 1. Across all seven traits, the same pattern: the recessive trait comes back in exactly one out of four offspring. Not approximately one in four. *Exactly* one in four, to the precision that 7,000 seeds can measure.

The number 1/4 demands a mechanism that produces 1/4.

<!-- → [TABLE: Mendel's published F₂ counts across all seven traits — columns: character, dominant count, recessive count, observed ratio, expected ratio; one row per trait. Student should see that all seven ratios cluster around 3:1 and that the deviations are small relative to the sample sizes, which is the statistical argument that forces the model.] -->

---

## The mechanism that produces 1/4

Here is Mendel's model, stated as a physicist would state it: each organism carries *two* hereditary factors for each character, one from each parent. When gametes form, the two factors *separate* — each gamete gets exactly one. When fertilization happens, two gametes combine and the organism has two factors again. In a heterozygote carrying one dominant factor and one recessive factor, the dominant one determines the phenotype. The recessive one sits there, invisible, undestroyed.

Now run the cross. A pure-breeding round plant is RR — two copies of the round factor. A pure-breeding wrinkled plant is rr — two copies of the wrinkled factor. Cross them: every F₁ plant gets one R from one parent and one r from the other. Every F₁ is Rr. Because R is dominant over r, every F₁ shows the round phenotype. The wrinkled character is hidden, not destroyed.

Now self-pollinate the F₁: Rr × Rr. The Rr plant makes gametes in a 1:1 ratio of R to r (the two factors separate equally at gamete formation). When gametes combine at random, four equally likely combinations:

- R from one parent × R from the other: probability 1/2 × 1/2 = **1/4** — gives RR
- R × r: probability 1/2 × 1/2 = **1/4** — gives Rr
- r × R: probability 1/2 × 1/2 = **1/4** — gives Rr
- r × r: probability 1/2 × 1/2 = **1/4** — gives rr

Genotype ratio in F₂: 1 RR : 2 Rr : 1 rr. Under dominance, RR and Rr both show the round phenotype. So phenotype ratio: 3 round : 1 wrinkled. The model produces 3:1. The observation was 3:1. There is no other model that produces exactly 3:1 from two Rr parents — the equal segregation (1:1 gamete ratio) and random fertilization are required.

The Punnett square is just this calculation written as a table. Each row is one parent's possible gamete (R or r, equally likely). Each column is the other parent's possible gamete. Each cell is the resulting zygote — one of four equally likely outcomes. Three cells show at least one R (dominant phenotype); one cell shows rr (recessive phenotype). This is not a new calculation; it is the same 1/2 × 1/2 = 1/4 product rule written in boxes. The table is the arithmetic, drawn out.

<!-- → [INFOGRAPHIC: 2×2 Punnett square for Rr × Rr — rows and columns labeled with gametes (R and r), cells showing genotypes (RR, Rr, Rr, rr), cells color-coded by phenotype class (three cells shaded for dominant/round, one cell shaded for recessive/wrinkled). A bracket groups the three dominant cells with "3/4" and labels the one recessive cell "1/4". Student should see that the Punnett square is the product-rule calculation laid out as a grid, not a separate method.] -->

---

## The three laws — what they say and what they assume

Mendel's 1866 paper does not number his laws. That was later tidying by others. But all three patterns are in the paper, derived from the data. Here they are, stated in the most direct language I can manage, with the modern cellular underpinning where it belongs.

**Law of Dominance.** In a heterozygote carrying one dominant allele and one recessive allele, the phenotype is determined by the dominant allele. The recessive allele is present, transmitted to half the gametes, and reappears unchanged in subsequent generations. The dominant allele does not destroy it. This is a statement about the phenotype of the heterozygote, nothing else.

One thing this law does *not* say: dominant means common. This is the most frequently wrong thing students say about dominance. The dominant Huntington's disease allele has a population frequency of about 1 in 20,000. The recessive wild-type allele is overwhelmingly the common one. Dominance describes what happens in the heterozygote. Population frequency depends on mutation rates, selection, and history — topics for Chapter 10.

**Law of Segregation.** The two alleles at any locus separate cleanly during gamete formation, so each gamete carries exactly one — and a heterozygote's alleles enter the gamete pool in exactly equal proportions, 1:1. In modern language, this is the cellular event of anaphase I in meiosis: the two homologous chromosomes move to opposite poles, and the two alleles riding those chromosomes end up in different daughter cells. The 50:50 ratio is exact in expectation. Any individual meiosis produces cells in which the segregation is perfect; across many gametes from many meioses, the average approaches 1:1 with precision that grows with sample size.

**Law of Independent Assortment.** The alleles at one locus assort independently of the alleles at any other locus. In a doubly heterozygous individual (AaBb), the four possible gamete types — AB, Ab, aB, ab — appear in equal proportions, 1/4 each. There is no statistical relationship between which A-allele a gamete carries and which B-allele it carries. The cellular basis is the independent orientation of different bivalents at metaphase I: each chromosome pair makes its own random choice of which pole to move toward, independently of every other chromosome pair.

This law has the most important asterisk. It holds only when the two genes are on different chromosomes, or far enough apart on the same chromosome that crossing over effectively randomizes their association. Genes on the same chromosome are *linked* — they travel together at rates higher than 50%, and the dihybrid F₂ ratio deviates from 9:3:3:1 toward an excess of parental-type offspring. Mendel got lucky: his seven pea traits behave as if independently assorting, even though we now know two of them sit on chromosome 4 (they are far enough apart that linkage is weak at his sample sizes). The conditions under which the third law holds are exactly what the chromosomal theory, worked out by Sutton and Boveri in 1902–1903, explains.

---

## The product rule and why the Punnett square is just a table

The 9:3:3:1 ratio for a dihybrid cross — two traits at once — is the calculation that shows most clearly that Mendel's framework is probability arithmetic.

Mendel's dihybrid cross: pure-breeding yellow round (YYRR) × pure-breeding green wrinkled (yyrr). Every F₁ is YyRr — heterozygous at both loci. Now self-pollinate: YyRr × YyRr.

The product rule for independent events: the probability that event A *and* event B both occur is P(A) × P(B), when A and B are independent.

At the Y/y locus alone, a Yy × Yy cross produces 3 yellow : 1 green in F₂. P(yellow) = 3/4, P(green) = 1/4. At the R/r locus alone, an Rr × Rr cross produces 3 round : 1 wrinkled. P(round) = 3/4, P(wrinkled) = 1/4. Because the two genes are on different chromosomes — Mendel's third law applies — the two probabilities multiply:

- P(yellow *and* round) = 3/4 × 3/4 = **9/16**
- P(yellow *and* wrinkled) = 3/4 × 1/4 = **3/16**
- P(green *and* round) = 1/4 × 3/4 = **3/16**
- P(green *and* wrinkled) = 1/4 × 1/4 = **1/16**

Ratio: 9:3:3:1.

The Punnett square for this cross is a 4 × 4 grid (each parent makes four gamete types: YR, Yr, yR, yr, each at 1/4). Sixteen cells. Count the cells with at least one Y *and* at least one R: 9. Cells with at least one Y but homozygous rr: 3. Cells with homozygous yy but at least one R: 3. Cells homozygous yy *and* rr: 1. The ratio: 9:3:3:1.

Both methods give identical answers because they are identical calculations in different notation. The Punnett square enumerates all 4 × 4 = 16 outcomes explicitly. The product rule reaches the same answer by multiplying the marginal probabilities. For two loci, the table is a useful visual. For three loci, the Punnett square is 8 × 8 = 64 cells — cumbersome but manageable. For four loci, it is 16 × 16 = 256 cells — you would not build it by hand.

<!-- → [INFOGRAPHIC: side-by-side comparison of the 4×4 dihybrid Punnett square (YyRr × YyRr) and the product-rule calculation — left panel shows the 16-cell grid with cells grouped and counted by phenotype class (9 yellow round, 3 yellow wrinkled, 3 green round, 1 green wrinkled); right panel shows the four product-rule multiplications (3/4 × 3/4 = 9/16, etc.). An equals sign between the two panels. Student should see that both panels produce identical numbers and that the product rule is the algebra underlying the Punnett-square count.] --> The product rule for three independently assorting loci is three multiplications:

- P(dominant at all three) = 3/4 × 3/4 × 3/4 = **27/64**
- P(dominant at exactly two) = 3 × (3/4 × 3/4 × 1/4) = **9/64** per class
- P(dominant at exactly one) = 3 × (3/4 × 1/4 × 1/4) = **3/64** per class
- P(recessive at all three) = 1/4 × 1/4 × 1/4 = **1/64**

Trihybrid F₂ ratio: 27:9:9:9:3:3:3:1. The eight classes sum to 64 = 4³. Mendel's framework generalizes cleanly to any number of independently assorting loci. The Punnett square scales as 4ⁿ. The product rule scales as *n* multiplications. The intelligence in the framework is that the product rule *is* Mendel's third law, written as arithmetic.

<!-- → [CHART: bar chart showing the eight phenotype-class probabilities for a trihybrid F₂ cross (27/64, 9/64, 9/64, 9/64, 3/64, 3/64, 3/64, 1/64) — bars labeled by which loci are dominant and which are recessive in each class, bars color-coded by number of dominant loci (dark for all-dominant, progressively lighter for fewer dominant loci). Student should see the pattern: each step down from 3 dominant loci to 2 to 1 to 0 multiplies the probability by 1/3.] -->

---

## From pea seeds to genetic counseling

The most important modern application of this arithmetic has nothing to do with peas.

A couple comes to a genetic counselor because their first child has cystic fibrosis. Both parents are phenotypically normal. Cystic fibrosis is autosomal recessive — caused by two defective copies of the *CFTR* gene. If the child has two defective copies (Cf⁻/Cf⁻), each parent must have contributed one, which means each parent is a carrier: Cf⁺/Cf⁻. Heterozygous carriers do not develop CF. They look entirely healthy. Now the couple wants to know: what is the probability that their next child has cystic fibrosis?

The cross is Cf⁺/Cf⁻ × Cf⁺/Cf⁻. This is exactly Mendel's monohybrid Aa × Aa cross, with different labels. The Punnett square — or the product rule, same answer — gives:

- P(Cf⁺/Cf⁺, unaffected non-carrier) = **1/4**
- P(Cf⁺/Cf⁻, unaffected carrier) = **1/2**
- P(Cf⁻/Cf⁻, affected with CF) = **1/4**

<!-- → [TABLE: binomial probability table for cystic fibrosis recurrence — rows: number of affected children (0 through 4); columns: N = 1, 2, 3, 4 total pregnancies; each cell shows P(exactly k affected of N). Student should see that the per-pregnancy risk of 1/4 compounds differently depending on family size, and that 31.6% of 4-child families with two carriers will have zero affected children.] -->

The genetic counselor tells the couple: per pregnancy, there is a 25% chance of an affected child, a 50% chance of an unaffected carrier, and a 25% chance of an unaffected non-carrier. Those are the exact numbers. They are the 1:2:1 genotype ratio from Mendel's 1865 paper, with Cf⁺ and Cf⁻ in place of R and r. The arithmetic is unchanged. Only the labels have changed.

If the couple wants to know the probability that exactly two of their four planned children will be affected, that requires the binomial distribution — a separate piece of arithmetic that compounds the per-pregnancy probability across multiple independent pregnancies:

$$P(k \text{ affected of } n) = \binom{n}{k} p^k (1-p)^{n-k}$$

For *n* = 4, *k* = 2, *p* = 1/4:

$$P(2 \text{ of } 4) = \binom{4}{2} (1/4)^2 (3/4)^2 = 6 \times \frac{1}{16} \times \frac{9}{16} = \frac{54}{256} \approx 21\%$$

The binomial distribution is built directly on the product rule: each pregnancy is independent, so the probability of any specific sequence of outcomes is a product of per-pregnancy probabilities; the binomial coefficient counts how many sequences produce exactly *k* affected children. The counselor's calculation room and Mendel's monastery garden are running the same arithmetic.

The catalog of disorders where this arithmetic applies — single-gene disorders with predictable Mendelian inheritance — now runs to more than 7,000 named conditions in the OMIM database. Cystic fibrosis, sickle-cell disease, Tay-Sachs, phenylketonuria: autosomal recessive, 1/4 per-pregnancy risk for a carrier couple. Huntington's disease, achondroplasia: autosomal dominant, 1/2 per-pregnancy risk if one parent is heterozygously affected. Hemophilia A, Duchenne muscular dystrophy: X-linked recessive, affecting sons of carrier mothers at a 1/2 rate. Every one of these is a Punnett square. The genotypes change; the arithmetic does not.

---

## The test cross

One more tool Mendel developed that clinical genetics still uses: the test cross.

Suppose you have a pea plant with round seeds — dominant phenotype — and you want to know whether it is homozygous (RR) or heterozygous (Rr). You cannot tell by looking at it; both genotypes produce round seeds. You need an experiment.

Cross it with a homozygous recessive tester — a pure-breeding wrinkled plant (rr). The tester contributes only r gametes. Whatever the unknown plant contributes determines the outcome.

If the unknown is RR: every offspring gets R from the unknown and r from the tester. Every offspring is Rr. Every offspring is round. Zero wrinkled. The absence of any recessive offspring tells you the unknown was homozygous dominant.

If the unknown is Rr: half the unknown's gametes are R, half are r. The offspring are half Rr (round) and half rr (wrinkled). A 1:1 ratio. The presence of wrinkled offspring at that ratio tells you the unknown was heterozygous.

The test cross forces the hidden allele in the heterozygote to reveal itself in the next generation by removing the masking dominant allele from the other parent. It is a resolution device. It is also the logic behind modern molecular carrier testing, where the same question — is this person homozygous wild-type or heterozygous carrier? — is now answered by sequencing rather than by crossing, but the underlying conceptual framework is Mendel's.

<!-- → [INFOGRAPHIC: two-panel test cross diagram — left panel: unknown RR plant × rr tester, showing all-round offspring with label "all dominant → genotype was RR"; right panel: unknown Rr plant × rr tester, showing 1:1 round:wrinkled offspring with label "half recessive → genotype was Rr". Student should see that the tester's r gametes act as a transparent background that makes the unknown plant's gamete contribution directly visible in the offspring phenotype.] -->

One practical note: the test cross gives ambiguous results at small sample sizes. If your unknown is Rr and you cross it with rr and happen to get five round offspring and zero wrinkled, you might conclude — wrongly — that it was RR. The probability of five dominant offspring in a row from an Rr parent is (1/2)⁵ = 1/32 ≈ 3%. Not negligible. To distinguish RR from Rr reliably, you want 20 to 50 offspring — enough that the binomial sampling fluctuations cannot credibly fake either result. This is the same problem of sample size that drove Mendel to 28,000 plants. Statistical laws are only visible at statistical scales.

---

## Why Mendel succeeded and his predecessors did not

Kölreuter, working in the 1760s, did extensive hybridization studies. Naudin, in 1862, published hybrid data with ratios in his tables that, retrospectively, contain the 3:1 signal. Neither extracted laws. Why?

Kölreuter worked with many plant species, several of which have complicated genetics — partial fertility in hybrids, sex-linked traits, multiple alleles at key loci — that would have obscured clean ratios even at large sample sizes. He also did not consistently use binary traits or pure-breeding lines.

Naudin was closer. His 1862 paper included hybrid data from several species. He noticed that hybrids sometimes reverted to parental types in later generations. He did not count at a scale that made the 3:1 visible as a number. He had hundreds of plants, not thousands. The signal was in his data; it was below the noise floor of his sample size.

Mendel had three things they did not: an organism with cleanly binary traits, pure-breeding lines that gave him known homozygous parents, and a physicist's instinct to count until the noise dropped below the signal. He was trained in physics and mathematics at the University of Vienna, which gave him the expectation that nature produces numerical regularities — and the habit of counting enough replicates to see them. The discovery was not fundamentally about biology. It was about experimental design and sample size.

There is a deeper point here. Mendel's discovery was made *before* anyone knew what chromosomes were. It was made before Boveri and Sutton connected his segregation ratios to the mechanics of meiosis in 1902. It was made before Morgan traced genes to specific chromosomal locations in 1910. Mendel inferred the behavior of discrete hereditary units from offspring counts alone. He inferred that each organism carries two copies and contributes one to each gamete — from the 3:1 ratio. He inferred that the two copies segregate equally — from the 3:1 ratio. He inferred that different characters assort independently — from the 9:3:3:1 ratio. He never saw a chromosome. He never saw an allele. He reasoned from the statistics of the garden to the mechanics of the cell, the way a physicist reasons from observable outcomes to unobservable mechanisms. The chromosomal theory, built by others thirty years later, found that Mendel had it right in every essential respect.

---

## The Fisher controversy

There is an unromantic part of this story that the chapter would be dishonest to skip.

In 1936, R. A. Fisher — the British statistician who is one of the founders of modern population genetics — published an analysis of Mendel's 1866 data. His conclusion: Mendel's published ratios are *too close* to the theoretical predictions. They fit the expected 3:1 and 9:3:3:1 ratios better than random sampling from a genuinely Mendelian population should produce. Aggregating across all of Mendel's published crosses, the probability of the data fitting the model as well as they do, by chance alone, is roughly 1 in 25,000.

In plain English: Mendel's data are suspiciously good.

Fisher himself wrote that he found no evidence of deliberate falsification, but that the data had apparently been systematically biased toward the expected values. His proposed mechanism: unconscious bias in classification. When a seed is marginal — not quite obviously round and not quite obviously wrinkled — the classifier (Mendel, or one of his unnamed assistants) may have a tendency to assign it to the category that better fits the expected ratio. Over thousands of marginal cases, this produces data that look cleaner than honest counting would.

Other explanations have been proposed: publication selection (Mendel may have chosen to publish only the crosses that gave clean results, suppressing those that were off); the inherent ambiguity of phenotypic classification for some of his seven traits (we now know that Rr seeds can sometimes appear slightly less round than RR seeds, so the line between "round" and "wrinkled" is genuinely blurry at the margins).

The controversy has not been fully resolved. Mendel's notebooks were burned after his death — his successor as abbot ordered them destroyed — so there is no primary record to check the published counts against. Fisher's statistical observation is real: the data are statistically too clean, and the aggregate chi-square is significant at any conventional threshold. The explanation of that observation is uncertain.

The broader point: this is a flag on the data, not a debunking of the laws. Mendel's three laws are correct in their content. They have been confirmed in every model organism biologists have tried them in, in hundreds of independent experiments, in every sexually reproducing species on Earth. The laws are fine. The question of exactly how Mendel got there — whether some unconscious classification bias crept into the published numbers, whether he selected which crosses to report, or some combination — is a historical-statistical question that does not change what he discovered. It is also a reminder that experimentalists must guard against their own expectations, including the expectation of confirming a beautiful prediction.

Naming the wrinkle is part of intellectual honesty about the discipline's history. Mendel was right. His published numbers may be too clean. Both of these things can be true at once.

---

## What this chapter gives you

Mendel's framework is mathematical. It is the application of independent-probability arithmetic to a biological problem. The 3:1 ratio is not a biological fact in the way that "peas produce seeds" is a biological fact — it is the output of a probability calculation, visible only at large sample sizes, and explainable only by a model in which hereditary units segregate equally and recombine randomly. The 9:3:3:1 ratio is the product rule applied to two independent loci. The clinical recurrence-risk calculation is the monohybrid 1:2:1 with different labels. All the same arithmetic.

What Mendel gave biology is not a list of facts about peas. He gave it a *framework* — a set of rules for predicting the statistical distribution of phenotypes in offspring from known parental genotypes. That framework works. It is the operating arithmetic of clinical genetic counseling for monogenic disorders today, unchanged from 1866. It is the foundation on which the chromosomal theory, molecular genetics, and population genetics were built.

The chapters ahead will show where the framework needs extending — incomplete dominance, polygenic traits, linkage — but every extension is a refinement of Mendel's model, not a replacement. The mechanism he inferred from 28,000 peas, with no microscope and no molecular tools, was right. That is a remarkable thing to say. It is also true.

---

## Exercises

**Warm-up**

1. **The monohybrid cross.** A pure-breeding tall pea plant (TT) is crossed with a pure-breeding dwarf plant (tt). Tall (T) is dominant. (a) What is the genotype of every F₁ plant? (b) What is the F₁ phenotype? (c) Self-pollinate the F₁: draw the 2×2 Punnett square, state the F₂ genotype ratio, and state the F₂ phenotype ratio. (d) If the F₂ generation contains 800 plants, how many are expected to be dwarf? *Tests: the monohybrid cross mechanics and the distinction between genotype ratio and phenotype ratio.*

2. **Reading a ratio.** A geneticist crosses two plants heterozygous for flower color (Vv × Vv, where violet V is dominant over white v) and grows 1,000 F₂ plants. She counts 730 violet and 270 white. (a) What ratio is she observing? (b) Is this consistent with Mendelian expectation? (c) What genotype are the 270 white plants? (d) What fraction of the violet plants are heterozygous? *Tests: connecting observed counts to the 1:2:1 genotype ratio underlying the 3:1 phenotype ratio.*

3. **The product rule, applied directly.** Two parents are both YyRr × YyRr, where Y (yellow) is dominant over y (green) and R (round) is dominant over r (wrinkled), genes on different chromosomes. Using the product rule only — no Punnett square — calculate: (a) P(yellow round); (b) P(green wrinkled); (c) P(yellow wrinkled); (d) P(green round). State the full dihybrid phenotype ratio. *Tests: applying the product rule to two independently assorting loci.*

**Application**

4. **The test cross as a diagnostic.** A pea plant has round seeds but unknown genotype — it could be RR or Rr. You cross it with a wrinkled-seeded plant (rr) and grow 40 offspring. All 40 are round-seeded. (a) Which genotype does this result favor, and why? (b) What is the probability of getting 40 round-seeded offspring if the unknown plant is actually Rr? (c) How many offspring would you need to reduce this probability below 1 in 1,000? *Tests: the test cross as a resolution device, and the relationship between sample size and confidence.*

5. **Cystic fibrosis recurrence risk.** Two carrier parents (Cf⁺/Cf⁻ × Cf⁺/Cf⁻) plan to have children. (a) What is the per-pregnancy probability of an affected child? (b) What is the probability that their first two children are both unaffected? (c) What is the probability that exactly one of their three children is affected? Use the binomial formula and show your work. (d) If their first child is affected, does this change the probability that their second child will be affected? Explain. *Tests: autosomal recessive recurrence risk, the binomial distribution, and the memoryless property of Mendelian probability.*

6. **Extending to three loci.** Two parents are AaBbCc × AaBbCc, all three genes on different chromosomes. Using the product rule: (a) How many distinct gamete types does each parent produce? (b) What is the probability that an F₂ offspring is homozygous recessive at all three loci? (c) What is the probability that an offspring is dominant at exactly two loci and recessive at one — and how many distinct phenotype classes have this structure? (d) Verify that all eight phenotype-class probabilities sum to 1. *Tests: the product rule generalized to three loci and the 27:9:9:9:3:3:3:1 ratio.*

**Synthesis**

7. **A pedigree.** Two unaffected parents have four children: two unaffected daughters, one unaffected son, one affected son. The affected son later has children with an unaffected woman; two of their three children are affected (one boy, one girl). (a) What is the most likely inheritance pattern? List the features of the pedigree that support your answer and rule out alternatives. (b) What are the most likely genotypes of the original two parents? (c) What is the per-pregnancy recurrence risk for the affected son's children? *Tests: pedigree analysis and the diagnostic logic of Mendelian inheritance patterns.*

8. **What Mendel's data actually show.** Mendel reported 5,474 round and 1,850 wrinkled F₂ seeds from the seed-shape cross (total 7,324). (a) Under the 3:1 hypothesis, how many round and wrinkled seeds are expected? (b) Compute the chi-square statistic with 1 degree of freedom. The critical value at p = 0.05 with 1 df is 3.84 — is Mendel's data consistent with the 3:1 model? (c) Fisher's 1936 analysis found that Mendel's data across all seven traits fit the expected ratios *too well* — aggregate p ≈ 0.00004. What does this mean, and what are the proposed explanations? *Tests: chi-square testing and the Fisher controversy as an application of the same statistical tool.*

**Challenge**

9. **Reverse engineering the cross.** A geneticist crosses two plants of unknown genotype, both showing dominant phenotypes for two traits. The offspring are: 453 dominant-dominant, 148 dominant-recessive, 151 recessive-dominant, 48 recessive-recessive. (a) What were the parental genotypes? Justify by identifying which Mendelian ratio these counts approximate. (b) Apply a chi-square test to confirm. (c) What single follow-up cross would verify the parental genotypes most efficiently? *Tests: reasoning backward from offspring counts to parental genotypes, and the diagnostic role of chi-square.*

10. **The limits of independent assortment.** Two genes A/a and B/b are on the same chromosome, 20 centimorgans apart (recombination frequency r = 0.20). An AaBb individual in coupling phase produces gametes: AB = 0.40, ab = 0.40, Ab = 0.10, aB = 0.10. (a) Explain why these proportions deviate from the 1:1:1:1 expected under Mendel's third law. (b) If this individual is crossed with an aabb tester, what phenotype ratio do you expect? (c) How does this differ from the 1:1:1:1 expected for unlinked genes in a test cross? (d) At what recombination frequency would two genes behave as if they assort independently? *Tests: the conditions under which the Law of Independent Assortment holds and fails, and the meaning of genetic distance.*

---

## LLM Exercise — Build your Mendelian-crosses simulator

This block is the one you actually do. The prompt below is ready to paste at Claude (or ChatGPT, or Gemini) once you have CLAUDE.md and DESIGN.md saved in the same folder from Chapter 00 and the meiosis simulator from Chapter 01.

### The simulation prompt

```
Show: Read CLAUDE.md and DESIGN.md from this project. Conform to
them. The genetics palette: dominant allele dark blue #1a5276;
heterozygous medium blue #2980b9; recessive light blue #85c1e9;
wild-type green #27ae60; mutant red #c0392b; dark mode background
#1a1a1a.

Say: Build 02-mendelian-crosses.html — an extended Punnett-square
simulator for 1- to 4-locus Mendelian crosses with both Punnett-
square and product-rule calculations side by side, plus a stochastic
sampling experiment, a chi-square calculator, and a recurrence-risk
panel.

Panel 1 — Cross setup and ratio computation.
- Number-of-loci selector: 1, 2, 3, or 4 (default 2).
- For each locus, two dropdowns: maternal genotype and paternal
  genotype, each with options homozygous dominant (AA), heterozygous
  (Aa), homozygous recessive (aa).
- A trait-expression toggle for each locus: complete dominance
  (default), incomplete dominance, codominance.
- Display: the cross written out (e.g., "AaBbCc × AaBbCc"); the
  expected genotype ratio computed via the product rule (e.g.,
  "1 AABBCC : 2 AABBCc : ... : 1 aabbcc"); the expected phenotype
  ratio (e.g., "27:9:9:9:3:3:3:1" for a trihybrid with complete
  dominance at each locus); the count of distinct gamete types per
  parent (2^n); the total cells in the corresponding Punnett square
  (4^n).
- For 1 and 2 locus crosses, also display the actual Punnett-square
  grid (2x2 or 4x4) with cells color-coded by genotype class. For
  3 and 4 locus crosses, suppress the grid (too large to be useful)
  and show only the product-rule ratios.

Panel 2 — Sampling experiment.
- Sample-size slider (10 to 100,000 offspring, log scale, default
  1000).
- A "Generate offspring" button that randomly samples N offspring
  from the cross according to the computed gamete-combination
  probabilities (independent draws from the gamete pool, exactly as
  in a real Mendelian cross).
- Display: a bar chart of phenotype counts (D3, bars colored by
  phenotype class per DESIGN.md); the observed ratio printed
  numerically next to each bar; the expected ratio printed for
  comparison; a "convergence-to-expectation" diagnostic showing the
  deviation in each phenotype class as a percentage of the expected
  count.
- A second toggle, "Run 10 replicate experiments at this N," that
  runs 10 independent samples and overlays the histograms — students
  see the spread of observed ratios at any given sample size.

Panel 3 — Chi-square calculator.
- Input: the observed counts from Panel 2 (or manually entered
  counts for analysis of textbook problems).
- Display: the chi-square statistic computed via Σ (O − E)² / E,
  the degrees of freedom (categories − 1), and the corresponding
  p-value (compute from chi-square distribution).
- A horizontal bar showing the p-value, with a vertical line at
  p = 0.05; the bar is colored green (consistent with model) if
  p > 0.05, red (inconsistent with model) if p < 0.05.

Panel 4 — Recurrence-risk calculator.
- Inputs: single locus; mother's genotype (dropdown); father's
  genotype (dropdown); disease model (autosomal recessive,
  autosomal dominant, X-linked recessive).
- Display: per-pregnancy probability of each genotype and phenotype
  outcome; binomial distribution of "fraction of N children
  affected" for N = 1, 2, 3, 4, 5, 10 (small table showing the
  probability of 0 through N affected at each N).
- A "Compare to specific Mendelian disorders" dropdown: cystic
  fibrosis (autosomal recessive, carrier frequency 1/25 in European
  ancestry), Tay-Sachs (autosomal recessive, carrier frequency
  1/30 in Ashkenazi Jewish ancestry), sickle-cell (autosomal
  recessive, carrier frequency varies by ancestry), Huntington's
  (autosomal dominant), hemophilia A (X-linked recessive). When
  selected, populate the recurrence-risk calculator with the
  appropriate parameters and walk through a typical genetic-
  counseling scenario.

Constrain: Four panels stacked vertically on desktop, single-column
on mobile. SVG canvas 720 x 400 per panel where applicable. Use D3
v7 from CDN, no other dependencies. Single self-contained HTML
file. Add at the top of the script:
// CLAIM: For n independently assorting heterozygous loci in an
// F2 cross between two doubly-heterozygous parents, the phenotype-
// class proportions are products of 3/4 and 1/4 according to which
// loci are dominant and recessive in the class. The Punnett-square
// method gives identical answers to the product-rule method but
// scales as 4^n cells while the product rule scales as n
// multiplications.

Verify: Print to the console on every parameter change, as PASS/FAIL
lines with measured values, expected values, and the case:
  (1) Monohybrid Aa × Aa: phenotype ratio = 3:1 (under complete
      dominance) or 1:2:1 (under incomplete dominance/codominance).
  (2) Dihybrid AaBb × AaBb: phenotype ratio = 9:3:3:1 (complete
      dominance both loci); Punnett-square and product-rule
      results must match exactly.
  (3) Trihybrid AaBbCc × AaBbCc: phenotype ratio = 27:9:9:9:3:3:3:1;
      product-rule method must produce the right 8-class
      distribution.
  (4) Sampling experiment at N = 100,000 for a dihybrid cross: the
      observed ratio for each phenotype class must be within ±1%
      of the expected; the chi-square test must give p > 0.05 with
      probability about 95% across replicate runs.
  (5) Recurrence-risk for cystic fibrosis carrier × carrier:
      probability of affected child per pregnancy = 0.25; binomial
      probability of 2 of 4 children affected = (6)(0.25)²(0.75)²
      ≈ 0.2109.
```

### Exploration tasks

Once the simulation runs:

1. **The sampling-size effect.** Set Panel 1 to a monohybrid Aa × Aa cross. Run the sampling experiment in Panel 2 at N = 20, then at N = 200, then at N = 2,000, then at N = 20,000. At each step, look at the observed vs. expected ratios and the chi-square *p*-value. At N = 20, you will frequently see chi-square *p*-values well below 0.05 — apparent "violations" of Mendel's First Law that are nothing but sampling fluctuation. At N = 20,000, the *p*-values will cluster near 1 — the data nearly always fit the model within sampling noise. This is the same effect that made Mendel's 28,000-plant sample size so important. The take-home: ratios are statistical regularities, and you cannot evaluate them on small samples.

2. **The trihybrid product rule.** Set Panel 1 to a trihybrid AaBbCc × AaBbCc cross. Verify by hand that the product rule gives 27/64 for the all-dominant phenotype class, 9/64 each for the three "dominant at two, recessive at one" classes, 3/64 each for the three "dominant at one, recessive at two" classes, and 1/64 for the all-recessive class. Verify that they sum to 64/64 = 1. Now imagine trying to do this with an 8 × 8 Punnett square — you would have to fill in 64 cells, group them by phenotype, and count. The product rule reduces this to four multiplications.

3. **A simulated cystic-fibrosis counseling session.** Set Panel 4 to "cystic fibrosis" with both parents as carriers. Note the per-pregnancy risks (1/4 affected, 1/2 carrier, 1/4 unaffected non-carrier). Look at the binomial table for "fraction of children affected at N = 4." You should see: P(0 affected) ≈ 0.316, P(1 affected) ≈ 0.422, P(2 affected) ≈ 0.211, P(3 affected) ≈ 0.047, P(4 affected) ≈ 0.004. This is the actual table a genetic counselor walks a couple through. The 31.6% probability of no affected children across four planned pregnancies is the optimistic case; the 47% probability of *at least one* affected child (1 minus 0.316) is the more clinically relevant number. The simulator computes the same numbers a counselor would, by direct application of the Mendelian arithmetic we developed in this chapter.

### Extension prompt

Once the basic Mendelian-crosses simulator works, the obvious extension is to add a pedigree-recognizer: a small interactive panel where the user draws a three-generation family pedigree (square = male, circle = female, filled = affected, half-filled = carrier), and the simulator outputs the most-likely Mendelian inheritance pattern (autosomal dominant, autosomal recessive, X-linked dominant, X-linked recessive) and the per-pregnancy recurrence risk. Paste this:

```
Extension: Add a fifth panel to 02-mendelian-crosses.html — a
pedigree-recognizer for three-generation family pedigrees.

The user draws the pedigree by clicking to add individuals (square
or circle), drawing lines to indicate mating and offspring
relationships, and clicking individuals to toggle affected/unaffected
status. The pedigree should support at least three generations and
families of up to ~20 individuals.

Once the pedigree is drawn, the simulator analyzes it and outputs:
- The most likely inheritance pattern. Use the standard diagnostic
  features: no father-to-son transmission of an affected trait
  (X-linked recessive); affected females in most pedigrees with
  every generation affected (autosomal dominant); affected children
  born to unaffected parents (autosomal recessive); etc.
- A goodness-of-fit score for each of the four standard patterns,
  showing which is most consistent with the observed pedigree.
- The per-pregnancy recurrence risk for the next child of the
  bottom-generation couple (assuming standard Mendelian
  inheritance), accounting for the inferred carrier status of
  unaffected parents based on their family history.
```

This extension is what makes the Mendelian framework *clinically usable* — the same arithmetic the chapter has developed, applied to a real family's pedigree, generates the recurrence-risk numbers that genetic counselors give patients.

---

*The next chapter takes up what happens when Mendel's assumptions break. Incomplete dominance, where heterozygotes show an intermediate phenotype — pink snapdragons from a red × white cross. Codominance, where both alleles are fully expressed simultaneously — AB blood type. Polygenic inheritance, where many genes contribute to one continuous trait — human height, skin color. Epistasis, where one gene's expression depends on another gene's genotype. Linkage, where two genes on the same chromosome refuse to assort independently. Each of these is a refinement of Mendel's model, not a refutation. The arithmetic stays the same. The inputs change.*
