# Chapter 16 — Modern Understandings of Inheritance
*Why genes on the same chromosome don't always travel together — and what that tells you about where they live.*

---

Here is a number that should puzzle you.

A human cell contains 46 chromosomes. Yet we inherit far more than 46 independent traits. Eye color, blood type, height, disease susceptibility, hundreds of other characteristics — all inherited, all varying between individuals, all following predictable rules. If each chromosome carried only one gene, the arithmetic would be wrong by orders of magnitude.

Something had to be missing from the picture. The missing piece turned out to be one of the more beautiful ideas in genetics: the fact that genes can be mapped — their positions on chromosomes determined — not by looking at the chromosomes directly, but by counting how often they travel together. The tool is recombination frequency. The result is a map. And the map revealed something Mendel never saw.

---

## When Two Sciences Collided

Mendel published his pea plant ratios in 1866. Chromosomes were first clearly observed during the 1880s. For two decades these were separate sciences — one mathematical, one microscopic — with no obvious connection.

The connection arrived in 1902. Theodor Boveri, watching sea urchin embryos, showed that missing or malformed chromosomes caused catastrophic failures in development. Chromosomes were not decorative. They were essential. Walter Sutton, watching grasshopper meiosis under a microscope, noticed something more specific: homologous chromosome pairs separated during meiosis I, just as Mendel's alleles appeared to segregate. The number of chromosome pairs matched the number of independently assorted traits Mendel had studied. The timing matched. The randomness matched.

Sutton made the inference: what if chromosomes *are* Mendel's particles? What if the invisible discrete factors Mendel inferred from ratios are physical objects we can now see through a lens?

The Chromosomal Theory of Inheritance followed: genes reside on chromosomes, and chromosome behavior during meiosis explains the sorting rules Mendel observed.

The evidence accumulated quickly. During meiosis, homologous pairs segregate independently of other pairs — matching Mendel's law of independent assortment. Each gamete receives half the chromosomal complement — matching the haploidy Mendel's ratios required. Male and female gametes carry equal numbers of chromosomes — matching the observation that both parents contribute equally. At fertilization, chromosome number restores itself in the offspring. The two sciences were describing the same machinery at different scales.

But the arithmetic problem remained. Forty-six chromosomes, thousands of genes. Chromosomes had to carry many genes each. And genes on the same chromosome, traveling together, should violate Mendel's prediction of independent assortment. The question became: do they? And if they do, by how much?

---

## Linkage and the Fruit Fly

Thomas Hunt Morgan began working with *Drosophila melanogaster* around 1908. Fruit flies were ideal: a two-week generation time, four pairs of chromosomes, and a willingness to produce hundreds of offspring per cross. Morgan could test Mendel's predictions rapidly and in large numbers.

He found something Mendel's peas had not revealed. Some traits violated independent assortment — they appeared together in offspring far more often than chance would allow. When Morgan crossed flies heterozygous for body color (gray dominant, black recessive) and wing shape (normal dominant, vestigial recessive), the parental combinations appeared far more frequently than the new combinations. The genes were not assorted independently. They were *linked* — carried on the same chromosome.

But they were not perfectly linked. In a test cross of a gray-normal heterozygous female against a black-vestigial male, Morgan expected four phenotypic classes if the genes assorted independently: gray-normal, black-vestigial, gray-vestigial, and black-normal, each at 25 percent. What he got instead was about 95 percent parental types (gray-normal and black-vestigial) and only 5 percent recombinant types (gray-vestigial and black-normal). The recombinants existed — but they were rare.

Where did the recombinants come from? The two genes were on the same chromosome. Yet some offspring carried allele combinations their parents never had. Something was separating linked genes.

<!-- → [TABLE: Morgan's test cross data — columns: Phenotype, Expected (independent assortment), Observed — rows: gray-normal (~250, ~950), black-vestigial (~250, ~950), gray-vestigial (~250, ~25), black-normal (~250, ~25) — student should see at a glance that the parental types are massively overrepresented and the recombinant types are rare, which is the signature of linkage] -->

---

## Crossing Over: The Physical Mechanism

In 1909, Frans Janssen observed something during prophase I of meiosis. When homologous chromosomes had paired up — a process called synapsis — they appeared at certain points to cross over each other. He called these points *chiasmata*. He proposed that the chromosomes were physically breaking and exchanging segments.

The idea was met with skepticism. Chromosomes breaking and rejoining without damage seemed mechanically implausible. For decades it remained controversial.

The proof came in 1931. Barbara McClintock working with corn, and Curt Stern working with *Drosophila*, independently used chromosomes with visible structural differences — unusual shapes, extra segments, missing pieces — and tracked whether the structural anomalies followed the genetic recombination. They did. Every time an offspring showed an allele combination neither parent had, the chromosome's physical structure had changed correspondingly. The exchange was real. Crossing over was not a metaphor. It was physical.

The mechanism is called homologous recombination. During synapsis, specialized enzymes cut both strands of DNA in both homologous chromosomes at the same position, hold the cut ends in alignment, and exchange them. The machinery uses matching sequences as a guide to ensure the exchange is precise. When the breaks rejoin, each chromosome carries a new combination of alleles — part original, part acquired from the homolog.

<!-- → [DIAGRAM: homologous recombination — two homologous chromosomes shown in synapsis, with alleles labeled (A/a, B/b) on each; chiasma shown at one point between the two gene loci; resulting recombinant chromosomes shown below with new allele combinations (A-b and a-B); student should see that a single crossover between the two loci produces the recombinant types Morgan observed] -->

This is why Morgan's recombinant flies existed. During meiosis in the heterozygous female, a crossover had occasionally occurred in the region of the chromosome between the body color gene and the wing shape gene. When a crossover landed between the two genes, it shuffled them onto opposite chromosomes. The further apart two genes are, the more chromosome lies between them, and the more likely a crossover will land in that interval. The closer together two genes are, the less likely.

Here is the key insight Morgan drew from this: recombination frequency is a measure of distance.

---

## Building the First Map

Alfred Sturtevant was an undergraduate in Morgan's laboratory when he realized what the recombination frequencies meant. He took home Morgan's data one evening and by morning had drawn the first genetic map — a linear representation of gene positions on a chromosome, derived entirely from breeding ratios.

The logic was elegant. If genes are arranged in a line on a chromosome, and if a crossover can occur anywhere along that line with roughly equal probability, then the frequency of recombination between two genes reflects how much chromosome separates them. Genes close together recombine rarely. Genes far apart recombine often.

Sturtevant defined one map unit as the distance that produces one percent recombination. If two genes recombine in five percent of offspring, they are five map units apart. These units were later renamed centimorgans (cM) in Morgan's honor.

Consider three genes. Gene A and gene B show eight percent recombination — they are 8 cM apart. Gene B and gene C show seven percent recombination — they are 7 cM apart. Gene A and gene C show fifteen percent recombination — they are 15 cM apart. The distances are additive: 8 + 7 = 15. This means the genes are arranged in order A — B — C, with B sitting between the other two. Change the observed distance for A to C and the map changes. The arithmetic is self-consistent, and self-consistency is evidence for the model.

<!-- → [IMAGE: linear genetic map — horizontal line representing a chromosome segment, with three labeled loci (A, B, C) marked as points; double-headed arrows between A and B labeled "8 cM", between B and C labeled "7 cM", between A and C labeled "15 cM"; student should see how pairwise recombination frequencies are combined to infer gene order and relative spacing] -->

The maps worked. They were not perfectly accurate — recombination hotspots and cold spots make distances non-uniform, and double crossovers could be invisible — but they were consistent enough to be useful and internally coherent enough to confirm that genes were indeed arranged linearly on chromosomes.

There was one limit. As two genes became farther apart on a chromosome, recombination frequency approached 50 percent — the same value as unlinked genes. Two crossovers between distant genes could restore the parental combination, making the double-crossover look like no crossover at all. At 50 map units, you could not distinguish genes on the same chromosome from genes on different chromosomes. Genetic maps worked well at short distances and broke down at long ones. This was not a failure of the logic — it was a limit of the measurement.

---

## Sex Linkage

Morgan's most famous discovery came from a single unusual fly. He found a white-eyed male in his red-eyed colony. He crossed it to normal red-eyed females. All the F1 offspring had red eyes — white appeared recessive, as expected. Then he crossed the F1 flies to each other. The F2 generation showed white eyes again, but only in males. All white-eyed flies were male. No white-eyed females appeared.

This was not Mendelian. In standard Mendelian inheritance, a recessive phenotype should appear in females and males at the same frequency. The white-eye phenotype was appearing exclusively in one sex.

The explanation required that the white-eye gene sit on the X chromosome. Males have one X and one Y. Females have two X chromosomes. A gene on the X chromosome is present in one copy in males and two copies in females. A female needs two copies of the recessive allele to show the recessive phenotype. A male needs only one.

When Morgan's F1 females (red-eyed, carrying one copy of the white allele on one X chromosome) were crossed to red-eyed males (carrying the normal allele on their single X), the daughters received one X from the mother and one X from the father. They had a 50 percent chance of being carriers and a 50 percent chance of being homozygous normal — but either way, they had a normal allele to mask the white. The sons received their single X from the mother. If they got the X carrying white, they would show white. If they got the X carrying normal, they would show red. Equal numbers of white and red sons. No white daughters.

This pattern — the phenotype appearing more often in males, daughters serving as carriers, the trait skipping generations in females — is the signature of X-linkage. Color blindness in humans follows exactly this pattern. The gene for red-green color vision sits on the X chromosome. A woman needs two non-functional copies to be color blind; a man needs only one. This is why color blindness is far more common in men than in women.

<!-- → [DIAGRAM: X-linkage inheritance pattern — two-generation pedigree showing carrier female (X+ X-) × normal male (X+ Y); F1 offspring shown as: daughters X+ X+ (normal) and X+ X- (carrier), sons X+ Y (normal) and X- Y (affected); student should see that the trait appears only in sons and that daughters can be carriers without showing the phenotype] -->

---

## Mitochondrial Inheritance: The Exception

There is one inheritance pattern that violates nearly everything discussed so far.

Mitochondria are organelles in the cytoplasm, not the nucleus. They carry their own DNA — a small circular chromosome, about 16,500 base pairs in humans, encoding a few dozen genes related to energy production. When a sperm fertilizes an egg, the egg's cytoplasm — packed with mitochondria — becomes the cytoplasm of the zygote. The sperm contributes almost no cytoplasm and almost no mitochondria. The offspring's mitochondria come almost entirely from the mother.

The result is maternal inheritance. If a mother carries a mitochondrial mutation, all her children inherit it. If a father carries one, none of his children inherit it. This breaks Mendel's rule of equal parental contribution, and it breaks the chromosomal theory's assumption that genes on nuclear chromosomes govern all traits.

Mitochondrial disorders are unpredictable in severity because mitochondria replicate and distribute randomly during cell division. A cell might receive mostly mutant mitochondria or mostly normal ones. Different tissues in the same individual might have different proportions. The penetrance of mitochondrial diseases varies accordingly.

---

## When Chromosomes Go Wrong

The chromosomal theory makes a prediction: if genes are on chromosomes, and chromosomes are inherited as units, then errors in chromosome distribution should have large effects. The errors exist. They are called aneuploidy.

During meiosis, homologous chromosomes should separate at meiosis I, and sister chromatids should separate at meiosis II. Sometimes they don't. This failure is called nondisjunction. One gamete receives an extra chromosome; another receives one too few.

When an extra chromosome is present at fertilization, the zygote has three copies of that chromosome instead of two. This is trisomy. When a chromosome is missing, the zygote has one copy instead of two. This is monosomy.

The consequences depend on which chromosome is affected. Monosomy of any autosome — any non-sex chromosome — is lethal. The missing genes create too severe an imbalance to allow development. Most trisomies are also lethal in utero, or produce live births that survive only weeks.

Trisomy 21 — Down syndrome — is the striking exception. Chromosome 21 is one of the smallest human chromosomes. An extra copy adds roughly 50 percent more dosage of a relatively small set of genes. This is tolerable, if barely: individuals with Down syndrome survive to adulthood but with intellectual disability, cardiac abnormalities, and other health challenges. The survival difference compared to other trisomies is simply chromosome size. Fewer extra genes means less dosage imbalance.

<!-- → [CHART: bar chart showing incidence of Down syndrome per 1,000 live births versus maternal age (ages 20–49) — student should see the steep increase in incidence with maternal age, particularly after 35, illustrating that nondisjunction risk rises with parental age] -->

Sex chromosome aneuploidy is generally less severe than autosomal aneuploidy for a different reason: X inactivation. Early in the development of female mammals, one X chromosome in each cell is inactivated — condensed into a silent structure called a Barr body. This process equalizes X-linked gene dosage between males (who have one X) and females (who have two). Individuals with extra X chromosomes can inactivate the excess copies, partially buffering the dosage imbalance.

Turner syndrome (one X, no second sex chromosome) produces a phenotypically female individual with short stature and infertility — the ovaries fail to develop without two X chromosomes, because some genes on the X escape inactivation and are needed in double dose during ovarian development. Klinefelter syndrome (two X chromosomes plus a Y) produces a phenotypically male individual with the extra X inactivated into a Barr body, small testes, and infertility. Both conditions are relatively mild compared to autosomal aneuploidy, because inactivation buffers the dosage.

---

## Chromosomal Rearrangements

Chromosomes can break and rejoin incorrectly in two major ways.

An inversion occurs when a segment of chromosome is excised, flipped 180 degrees, and reinserted. The genes are still present, still functional, just in reverse order. Most inversions are phenotypically silent in the carrier. The problem emerges during meiosis: a chromosome with an inversion and its normal homolog must still pair up. To do so, one must loop back on itself. This unusual topology can lead to unequal crossing over during that loop, producing gametes with duplicated or deleted segments — which are not silent.

A translocation occurs when a segment of one chromosome breaks off and attaches to a nonhomologous chromosome. In a reciprocal translocation, two nonhomologous chromosomes exchange segments with no net loss or gain. Carriers of balanced translocations are typically normal — the genes are all present. The problem is again in meiosis: the translocated chromosomes must still pair with their normal homologs, creating complex configurations that can produce aneuploid gametes.

Some translocations are not silent. The Philadelphia chromosome is a translocation between chromosomes 9 and 22, found in nearly all cases of chronic myelogenous leukemia. The break points put two genes — *BCR* and *ABL* — adjacent to each other, creating a fusion gene encoding an abnormal protein with unregulated kinase activity that drives uncontrolled cell division. The translocation does not just rearrange genes; it creates a new gene that didn't exist before.

---

## What the Map Reveals

Step back from the mechanisms and see the logic.

Mendel's laws were mathematical — abstract ratios derived from crosses. The chromosomal theory gave those ratios a physical explanation. The law of segregation became chromosome separation during meiosis I. The law of independent assortment became the independent segregation of chromosomes on different chromosome pairs.

But Mendel's laws were incomplete. They said nothing about genes on the same chromosome, because Mendel happened to study genes on different chromosomes or far enough apart to appear unlinked. Linkage and recombination filled the gap. They explained why some genes violate independent assortment, and they provided a tool — recombination frequency — to determine where genes sit relative to each other on a chromosome.

The map that Sturtevant drew in 1913 was the first attempt to assign physical locations to abstract hereditary factors. It was based entirely on counting offspring. No microscopy beyond what was already known. No chemistry. Just ratios, turned into distances, turned into a linear arrangement of points. It worked because chromosomes are linear, genes are fixed in position, and crossing over disrupts those positions with a frequency that reflects the distance between them.

The deeper point is about what measurement can reveal. Sturtevant could not see the chromosome directly in any useful detail. But he could measure recombination — a consequence of chromosome structure — and from that measurement infer the structure. This is the same logic that let physicists infer atomic structure from scattering experiments long before they could image atoms. You do not always need to see the thing directly. You need a measurement whose value depends on what you want to know. Recombination frequency depends on chromosomal distance. So recombination frequency measures chromosomal distance.

What Mendel began with invisible particles governed by elegant ratios, Sutton and Boveri connected to visible chromosomes, Morgan extended to linkage and mapping, and Sturtevant translated into a physical map. By 1920, inheritance had a physical address. Genes were not floating abstractions. They were points on lines — specific locations on specific chromosomes — that could in principle be found.

That is where the next chapter begins: what, physically, is a gene? What does it look like at the molecular level? How is its information encoded? The map tells you where to look. The next question is what you find when you look there.

---

## Exercises

**Warm-up**

1. A test cross of a doubly heterozygous fly (AaBb) with a homozygous recessive (aabb) produces offspring in these proportions: 44% AaBb, 44% aabb, 6% Aabb, 6% aaBb. Are genes A and B linked or unlinked? How do you know? What is the recombination frequency, and what map distance does this represent?

2. Morgan found white-eyed flies only among males in the F2 generation of his cross. A student suggests this is simply because white eyes are more likely to develop in males for developmental reasons — not because the gene is on the X chromosome. Design a single cross that would distinguish between these two explanations. What result would you expect under each hypothesis?

3. A woman is heterozygous for an X-linked recessive condition (one normal allele, one disease allele). Her partner is unaffected. What is the probability that their first son will be affected? Their first daughter? Their first child regardless of sex?

**Application**

4. Three genes on the same chromosome show the following pairwise recombination frequencies: gene 1 and gene 2 = 12 cM; gene 2 and gene 3 = 7 cM; gene 1 and gene 3 = 19 cM. Draw the most likely gene order on a linear map with distances labeled. Now suppose the observed distance between gene 1 and gene 3 were only 15 cM instead of 19 cM. What would that discrepancy suggest about what is happening between genes 1 and 3, and why would it cause underestimation of true map distance?

5. A carrier female for a mitochondrial disorder (one that affects energy production in muscle) has three children with an unaffected male. Predict which children, if any, will inherit the mitochondrial mutation. Now predict what would happen if the father were the mutation carrier instead. Explain the asymmetry.

6. A karyotype reveals an individual with 46 chromosomes, but one chromosome 21 is unusually long. Genetic testing reveals the individual has three functional copies of all chromosome 21 genes despite having 46 chromosomes total. What chromosomal rearrangement could explain this? How does this differ from standard trisomy 21 in terms of mechanism and inheritance risk to offspring?

**Synthesis**

7. The chapter argues that recombination frequency measures chromosomal distance using the same logic physicists used to infer atomic structure from scattering experiments. Identify the specific analogy: what corresponds to the "scattering event" in genetics, what corresponds to the "detector" measuring the outcome, and what structural property is being inferred from the measurement? Where does the analogy break down — what can scattering experiments reveal that recombination frequency mapping cannot?

8. The Philadelphia chromosome translocation puts *BCR* adjacent to *ABL*, creating a fusion protein with constitutively active kinase activity that drives uncontrolled cell division. Using what you know about the cell cycle from Chapter 12, classify the *BCR-ABL* fusion protein: is it behaving more like an oncogene product or a tumor suppressor loss? Explain your reasoning. Why would a targeted drug that specifically inhibits the BCR-ABL kinase be expected to slow leukemia progression?

9. Mendel's law of independent assortment holds when two genes are on different chromosomes or are far enough apart on the same chromosome to appear unlinked. The chapter notes that Mendel was fortunate: the seven traits he studied in peas happened to assort independently. Look up the seven traits and their chromosomal locations in *Pisum sativum*. Are any of them on the same chromosome? If so, why did Mendel not observe linkage? What does this tell you about the relationship between physical distance and apparent independence?

**Challenge**

10. The chapter says that at 50 map units, you cannot distinguish genes on the same chromosome from genes on different chromosomes. This is a fundamental limit of classical genetic mapping. Modern genomic sequencing, however, can directly determine the physical distance between any two genes in base pairs. But knowing the physical distance in base pairs does not directly tell you the recombination frequency — the relationship varies across the genome. Design an experiment that would use both classical genetic mapping and DNA sequencing to characterize a recombination hotspot: what would you measure, what would positive evidence for a hotspot look like, and why would a hotspot cause the genetic map distance to be larger than expected from the physical distance alone?

11. Turner syndrome (45,X) is the most common cause of primary amenorrhea in humans, yet it is also the most common chromosomal abnormality in spontaneous abortions — roughly 99% of 45,X conceptions are lost before birth. This means the 1 in 2,500 live-born females with Turner syndrome represents a tiny fraction of all 45,X conceptions. Using what you know about X inactivation and gene dosage, propose a hypothesis for why 45,X is nearly always lethal in utero despite being compatible with life in the rare survivors. What specific aspect of X-chromosome biology might explain why 45,X is more lethal than XXX or XXY, even though those conditions involve more chromosomal material?

---

*By Nik Bear Brown*

---

## LLM Exercises

The following exercises are designed for use with a large language model. Paste the prompt into any capable model and examine the response critically — not for correctness alone, but for whether the reasoning is mechanistic or merely verbal.

**Exercise 1 — Linkage and recombination frequency**
Prompt a model: *"Two genes are located on the same chromosome 18 centimorgans apart. In a test cross between a doubly heterozygous individual (genotype AaBb) and a doubly homozygous recessive individual (aabb), what proportion of offspring would you expect to show parental phenotypes versus recombinant phenotypes? Walk me through the relationship between recombination frequency and physical distance, and explain why this relationship breaks down at distances above approximately 50 centimorgans."*

Evaluate whether the model correctly calculates that 18 cM = 18% recombinant gametes, so 82% of offspring should show parental phenotypes (split equally between the two parental types) and 18% should be recombinant. The breakdown above 50 cM occurs because multiple crossovers between the loci begin to randomize inheritance, making the loci effectively unlinked.

**Exercise 2 — X-linked inheritance and the affected-male pattern**
Prompt: *"Hemophilia A is an X-linked recessive disorder. Walk me through the inheritance pattern when a carrier mother (X^H X^h) marries an unaffected father (X^H Y): what proportion of sons and daughters will be affected, what proportion will be carriers? Then explain why X-linked recessive disorders show a characteristic 'skip a generation' pattern and why affected fathers cannot pass the disease to their sons."*

Evaluate whether the model correctly determines that 50% of sons will be affected (X^h Y), 0% of daughters will be affected (all receive X^H from father), and 50% of daughters will be carriers (X^H X^h). The fathers-not-to-sons rule follows from sons receiving Y from father, not X — so X-linked alleles travel from carrier mothers to affected sons, then potentially to carrier granddaughters.

**Exercise 3 — Pedigree analysis as detective work**
Prompt: *"You are presented with a four-generation pedigree showing an autosomal dominant disorder with reduced penetrance (about 70%). Walk me through how you would distinguish this pattern from autosomal recessive (which would show different parent-offspring patterns) and from X-linked dominant (which would show different sex distributions). What single feature of the pedigree most decisively identifies the inheritance mode? What is the chance that an apparently 'unaffected' individual in a generation could carry the allele but not express it?"*

Evaluate whether the model engages with the male-to-male transmission diagnostic (rules out X-linked), the apparent skipping of generations (consistent with reduced penetrance autosomal dominant or autosomal recessive), and the calculation of carrier risk for unaffected offspring of affected parents (with 70% penetrance, 30% of carriers will appear unaffected).

**Exercise 4 — Polygenic inheritance and the bell curve**
Prompt: *"Human height is determined by hundreds to thousands of genetic variants, each contributing a small effect. Walk me through how this polygenic architecture produces a continuous (bell-curve) distribution rather than discrete categories, and explain how genome-wide association studies (GWAS) have identified specific height-associated variants. What fraction of the heritability of height has been accounted for by all known variants combined, and why does substantial 'missing heritability' remain?"*

Evaluate whether the model correctly identifies that the central limit theorem produces normal distributions when many small additive effects combine, and whether it engages with the missing-heritability problem (most GWAS-identified variants have very small effect sizes; rare variants, gene-gene interactions, and gene-environment interactions remain hard to capture). Currently identified variants account for roughly 25-40% of height heritability [verify].

**Exercise 5 — Mitochondrial inheritance as exception**
Prompt: *"Mitochondrial DNA is inherited exclusively from the mother — sperm contribute nuclear DNA but not mitochondria. Walk me through the consequences for inheritance of mitochondrial diseases (e.g., MELAS, Leber's hereditary optic neuropathy): what proportion of children of an affected mother will be affected? Why doesn't the same pattern apply to children of an affected father? Then explain why some mitochondrial diseases show variable expressivity even within siblings — the heteroplasmy phenomenon."*

Evaluate whether the model correctly identifies that all children of an affected mother inherit her mitochondria, but the variable expression depends on what proportion of mitochondria are mutant (heteroplasmy ratio) — a stochastic process during oogenesis. Children of affected fathers are unaffected because the father's mitochondria are not transmitted (with rare exceptions).

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Calvin Bridges** was Thomas Hunt Morgan's student in the Columbia "Fly Room" — and proved the chromosome theory of inheritance in 1916 by showing that rare nondisjunction events produce predictable inheritance anomalies. He helped build the first detailed Drosophila genetic map.

**Run this:**

```
Who was Calvin Bridges, and how does his nondisjunction work connect to the modern understandings of inheritance we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Calvin Bridges"** on Wikipedia. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one nondisjunction event in meiosis and show why the offspring's phenotype proves chromosomes carry genes.
- Ask it to describe what the Columbia "Fly Room" was actually like — the conditions, the records, the daily rhythm of the genetics that became standard.

What changes? What gets better? What gets worse?
