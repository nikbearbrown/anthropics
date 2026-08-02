# Chapter 3 — Extensions of Mendelian Genetics

## TL;DR

- When the genotype-to-phenotype rule gets more interesting.
- The chapter moves through The six assumptions, and where they break, Incomplete dominance — pink snapdragons and the dosage model, Codominance and the ABO blood groups, The Bombay phenotype — epistasis worked end to end, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*When the genotype-to-phenotype rule gets more interesting.*

---

Boston, 2018. A forty-two-year-old woman walks into a high-risk breast-and-ovarian clinic. Her mother had ovarian cancer at fifty-one. Her maternal aunt had breast cancer at forty-six. She carries her family's pathogenic *BRCA1* mutation. The lifetime risk of breast cancer in *BRCA1* mutation carriers, by age eighty, has been estimated at roughly 60–72% in large international cohort studies. She begins intensive screening.

Her younger sister, thirty-nine, comes in three months later. Same pedigree. Same test. Same result — the identical *BRCA1* mutation, from the same mother.

Eight years pass.

The older sister, now fifty, develops triple-negative breast cancer — the most aggressive *BRCA1*-associated subtype. She survives.

The younger sister, now forty-seven, has had nothing. Annual MRIs clean. She carries the same mutation. She has had no cancer.

This is not a violation of Mendelian inheritance. It is what Mendelian inheritance actually looks like when you stop treating "having the dominant disease allele" and "having the disease" as the same sentence. The technical term for the gap between them is **penetrance** — the fraction of genotype-carriers who develop the phenotype. *BRCA1* mutations are highly penetrant by population-genetics standards. They are not 100% penetrant. The arithmetic of genetic counseling, done honestly, requires knowing the difference.

The counselor who tells the younger sister "your BRCA1 mutation means you will get breast cancer" is doing genetics wrong. So is the counselor who says "you might not, so don't worry." The honest counselor walks through the actual penetrance numbers — 60–72% by age eighty, meaning roughly one in three carriers will not develop breast cancer in their lifetime — and lets the patient decide what to do with that. This conversation requires a framework that Chapter 2 does not fully supply. Building that framework is what this chapter does.

---

## The six assumptions, and where they break

Chapter 2's 3:1 and 9:3:3:1 ratios are not facts of nature. They are consequences of a model with six assumptions. List the assumptions, and you can read every extension in this chapter as a story about which assumption fails.

**Assumption 1 — Complete dominance.** The heterozygote is phenotypically indistinguishable from the homozygous dominant. Mendel's tall × dwarf F₁ peas were full height, not intermediate. Broken by *incomplete dominance* (heterozygote shows intermediate phenotype) and *codominance* (both alleles fully expressed simultaneously).

**Assumption 2 — Two alleles per gene.** Every individual carries one of three genotypes at each locus: AA, Aa, or aa. Broken by *multiple alleles* — more than two alleles segregating in the population, as in the ABO blood-group system with three common alleles and the HLA system with thousands.

**Assumption 3 — One gene per trait.** Broken by *polygenic inheritance* (many genes contribute additively to one trait — human height is influenced by thousands of loci) and *epistasis* (one gene's product modifies another's, so the trait depends on the combined genotype at multiple loci).

**Assumption 4 — One trait per gene.** Broken by *pleiotropy* — one gene affecting multiple traits. The sickle-cell hemoglobin allele changes red-cell shape, oxygen-carrying capacity, pain-crisis risk, organ damage, infection susceptibility, and resistance to malaria, all from one base substitution.

**Assumption 5 — No environmental modification.** Broken by PKU (same genotype, severe intellectual disability on a normal diet, near-normal development on a restricted one), G6PD deficiency (asymptomatic unless exposed to specific oxidative triggers), and broadly by the probabilistic nature of *incomplete penetrance* and *variable expressivity*.

**Assumption 6 — Autosomal loci on different chromosomes.** Broken by linkage (Chapter 1), sex-linked and sex-influenced inheritance, *mitochondrial inheritance* (the gene is not on a nuclear chromosome at all), and *genomic imprinting* (the same DNA region produces different phenotypes depending on which parent contributed it).

These are not refutations of Mendel. Each one, once specified, fits into Mendelian arithmetic with a modified rule. Mendel's apparatus — gametes carry alleles, gametes combine at fertilization, the product rule gives joint probabilities — survives every extension intact. What changes is the *genotype-to-phenotype function*: the rule that says, given genotype AaBb, what does the organism look like? In strict Mendelian inheritance the function is "look up dominance per locus and combine." In extended Mendelian inheritance it gets more interesting. The chapter is a tour through how.

---

## Incomplete dominance — pink snapdragons and the dosage model

Cross a pure-breeding red snapdragon (R^R R^R) with a pure-breeding white snapdragon (R^W R^W). The F₁ flowers are pink — uniformly, every plant, indistinguishably pink. Self-pollinate the F₁. The F₂ phenotype distribution is *1 red : 2 pink : 1 white* — not 3:1. This is **incomplete dominance**: the heterozygote shows an intermediate phenotype between the two homozygotes.

The 1:2:1 phenotype ratio equals the genotype ratio exactly, because every distinct genotype produces a distinct phenotype. The Mendelian 3:1 is what you get when heterozygotes "look like" the dominant homozygote and get counted together. Take away the dominance and the heterozygotes appear as their own class.

The molecular point is easy to get wrong. Incomplete dominance does not mean the alleles are weaker. It means the phenotype depends quantitatively on the amount of functional protein. A homozygous-red plant makes a full dose of the pigment enzyme. A homozygous-white plant makes none — the R^W allele encodes a non-functional version. The heterozygote makes half the dose, half the pigment, and the flower is pink. The model is called *haploinsufficiency*: one functional copy is not enough to produce the full phenotype. The recessive allele is not weak. It contributes nothing, and there is nothing weak about contributing nothing.

The clinical anchor is **familial hypercholesterolemia** (FH), caused by mutations in the LDL-receptor gene *LDLR*. Heterozygotes have LDL levels roughly twice normal — about 300–400 mg/dL — and are at substantially elevated risk of premature coronary artery disease. Homozygotes have LDL above 500 mg/dL, with severe atherosclerosis in childhood. The heterozygote is exactly intermediate in the biochemical phenotype: half the LDL-receptor activity, roughly double the LDL. Pink snapdragons, in a cardiology ward. The dosage is what differs.

A quick consequence: with incomplete dominance, the heterozygote can never breed true. Cross two pink snapdragons and the F₂ is 1 red : 2 pink : 1 white. If a phenotype refuses to breed true across many generations of selection, you may be looking at incomplete dominance rather than a simple recessive.

---

## Codominance and the ABO blood groups

**Codominance** is incomplete dominance's loud cousin: *both alleles are fully expressed simultaneously* in the heterozygote, producing a combined phenotype rather than a blended intermediate. The example is the human ABO blood-group system, worked out by Karl Landsteiner in Vienna in 1900 — the same year Mendel was rediscovered, and Landsteiner won the Nobel Prize for it in 1930.

Human red blood cells carry surface carbohydrate antigens that determine ABO blood type. The relevant gene encodes a glycosyltransferase enzyme that modifies a precursor molecule on the red-cell surface called the *H antigen*. Three common alleles:

- **I^A** — adds *N-acetylgalactosamine* to the H antigen, producing the A antigen.
- **I^B** — adds *galactose* to the H antigen, producing the B antigen.
- **i** — encodes a non-functional enzyme; H antigen is left unmodified.

In the I^A I^B heterozygote, *both* transferase enzymes are made, *both* sugars get added on different red-cell surface molecules, and the cell expresses *both* A and B antigens simultaneously. The two alleles do not blend — they coexist without mixing. That is codominance.

The clinical importance is transfusion compatibility. Every person makes antibodies against the ABO antigens they do not themselves have. Transfuse type-A blood into a type-B recipient, and the recipient's anti-A antibodies trigger acute hemolytic transfusion reaction — agglutination, red-cell lysis, kidney failure, possible death. Blood-typing before transfusion is built entirely on this arithmetic.

A note on terminology that confuses students: codominance is not the same as incomplete dominance. Incomplete dominance produces a blended intermediate (less pigment → pink). Codominance produces a both-at-once phenotype (both surface sugars on the same cell). The F₂ ratio in both cases is 1:2:1, because in both cases the heterozygote phenotype is distinct from both homozygotes. The ratio alone cannot distinguish them; you have to look at what the heterozygote actually is.

---

## The Bombay phenotype — epistasis worked end to end

The H antigen is itself produced by a *separate* gene on a *separate* chromosome. The **H gene** on chromosome 19 encodes fucosyltransferase 1 (FUT1), which creates the H antigen on the red-cell surface — the substrate that the I^A and I^B enzymes modify. The H gene has two alleles: the functional **H** allele and the rare non-functional **h**. Homozygous *hh* individuals produce no H antigen, so the I^A and I^B enzymes have no substrate to act on. Their red cells display no A antigen, no B antigen, and no H antigen — even if their ABO genotype is I^A i or I^B i, which would ordinarily produce type-A or type-B blood.

This is the **Bombay phenotype**, first described by Bhende, Deshpande, Bhatia and colleagues in 1952 in three families in Bombay, India. On standard blood-typing reagents, a Bombay individual tests as type O — no agglutination with anti-A or anti-B serum. But they are not ordinary type O. They produce a fourth antibody — anti-H — against the H antigen that ordinary type-O cells display. Transfuse ordinary O blood into a Bombay patient and the anti-H antibodies attack the donor's red cells. Acute hemolytic transfusion reaction. A Bombay individual can be safely transfused only with blood from another Bombay individual — perhaps one in ten thousand in India, far rarer worldwide. Bombay donor registries exist for this purpose.

This is **recessive epistasis**: a homozygous-recessive genotype at one locus (*hh* at the H locus) masks the expression of alleles at another locus (the ABO locus). The H gene is *epistatic* to ABO; ABO is *hypostatic* to H. The molecular reason is clean: the H-gene product is the substrate that the ABO-gene products act on. No substrate, no product, no phenotype — regardless of ABO genotype.

Now work the arithmetic. Consider two doubly heterozygous parents who appear as ordinary blood types: **Hh I^A i × Hh I^B i**. The mother is type A (has at least one H allele; is I^A i at ABO). The father is type B (same logic). Each parent produces four gamete types under independent assortment (H is on chromosome 19, ABO on chromosome 9):

$$\text{Mother's gametes: } H I^A \ (1/4), \quad H i \ (1/4), \quad h I^A \ (1/4), \quad h i \ (1/4)$$

$$\text{Father's gametes: } H I^B \ (1/4), \quad H i \ (1/4), \quad h I^B \ (1/4), \quad h i \ (1/4)$$

Rather than enumerate all 16 cells of the 4×4 grid, use the product rule. The two loci segregate independently, so:

- P(at least one H) = P(H\_) = 3/4. These individuals produce H antigen; their ABO type is visible.
- P(hh) = 1/4. These individuals are Bombay regardless of their ABO genotype.

For the offspring with at least one H allele (3/4 of the total), the ABO distribution from I^A i × I^B i is:

$$P(I^A I^B) = \frac{1}{4}, \quad P(I^A i) = \frac{1}{4}, \quad P(I^B i) = \frac{1}{4}, \quad P(ii) = \frac{1}{4}$$

Combining with the H-locus distribution:

$$P(\text{type AB}) = \frac{3}{4} \times \frac{1}{4} = \frac{3}{16}$$

$$P(\text{type A}) = \frac{3}{4} \times \frac{1}{4} = \frac{3}{16}$$

$$P(\text{type B}) = \frac{3}{4} \times \frac{1}{4} = \frac{3}{16}$$

$$P(\text{ordinary type O}) = \frac{3}{4} \times \frac{1}{4} = \frac{3}{16}$$

$$P(\text{Bombay}) = \frac{1}{4} \times 1 = \frac{4}{16}$$

What a blood-typing lab reports: the Bombay individuals (4/16) and the genuine type-O individuals (3/16) are indistinguishable by standard typing, both reading as "O." The apparent-O class is 7/16. The full F₂ ratio, in the order AB : A : B : "type O," is **3 : 3 : 3 : 7**.

Not 9:3:3:1. The epistasis modifies the ratio because it reassigns the 1/16 genuine-O class *and* the 4/16 Bombay class into the same serological bucket. The gametogenesis is Mendelian throughout. The product rule gives the gamete frequencies correctly. What changes is the phenotype-assignment rule — the function that maps a genotype like *hh I^A i* to an observable blood type.

The clinical consequence of this arithmetic: a trauma patient with Bombay phenotype types as O, receives O-negative blood, and has a hemolytic reaction. The blood bank runs additional testing, finds anti-H antibodies, confirms Bombay. The remaining transfusion is canceled. The bank initiates an urgent search for Bombay-compatible donors, who may need to be located across international registries. One allele state at the H locus — *hh*, frequency roughly 1/10,000 in India — can override a patient's ABO genotype entirely, and routine serological screening will not see it.

---

## Other epistasis patterns

The Bombay phenotype is one example of recessive epistasis. Other patterns modify the standard 9:3:3:1 dihybrid ratio in characteristic ways that serve as diagnostic signatures. The clearest non-clinical example is coat color in Labrador retrievers.

Two loci control the relevant portion of Lab coat color. The **B locus** (gene *TYRP1*, chromosome 11) determines whether eumelanin is black (B, dominant) or brown (b, recessive). The **E locus** (gene *MC1R*, chromosome 5) determines whether eumelanin is deposited in the coat at all (E, dominant) or replaced by yellow phaeomelanin (e, recessive homozygote). When a dog is *ee*, no eumelanin reaches the coat regardless of the B-locus genotype — the yellow coat masks whatever the B locus would produce. E is epistatic to B.

From a dihybrid cross BbEe × BbEe:

- 9/16 B\_E\_ → black
- 3/16 bbE\_ → chocolate
- 3/16 B\_ee → yellow
- 1/16 bbee → yellow

The two yellow classes combine: **9 : 3 : 4**. The 9:3:3:1 collapses by merging the *ee* classes regardless of B-locus genotype.

The pattern of how each epistasis type modifies the standard dihybrid ratio is systematic:

| Pattern | Mechanism | Modified F₂ ratio |
|---------|-----------|-------------------|
| No epistasis | Standard Mendelian | 9 : 3 : 3 : 1 |
| Recessive epistasis | Homozygous recessive at one locus masks the other | 9 : 3 : 4 |
| Dominant epistasis | Dominant allele at one locus masks the other | 12 : 3 : 1 |
| Duplicate recessive epistasis | Homozygous recessive at *either* locus produces the same phenotype | 9 : 7 |
| Duplicate dominant epistasis | Dominant allele at *either* locus is sufficient | 15 : 1 |
| Dominant suppression | Dominant allele at one locus suppresses the other's dominant phenotype | 13 : 3 |

All of these are produced by the same operation: take the standard 9:3:3:1 genotype-class frequencies and apply a phenotype-assignment rule that combines or reassigns specific classes. The Punnett square does not change. The arithmetic does not change. The function changes.

---

## Polygenic inheritance — when many genes produce one trait

The preceding sections kept the number of genes per trait small. Most quantitative traits in real populations are not like that. **Polygenic inheritance** is the pattern in which many genes — often hundreds or thousands — each contribute a small additive effect to one continuously varying trait. Human height, blood pressure, body mass index, cardiovascular risk, neuropsychiatric disease susceptibility. These traits do not show 1:2:1 or 9:3:3:1 ratios, and the reason is not that they are "non-Mendelian." They are Mendelian exactly, at each individual locus. What changes is that the trait is the *sum* of many small Mendelian contributions, and summing many random variables produces a different-looking distribution.

Herman Nilsson-Ehle at Lund, Sweden, worked this out in 1908 from experiments on wheat kernel color. He crossed dark-red wheat with white wheat, got uniformly medium-red F₁, and then grew F₂. The F₂ showed not three classes but five or seven, fitting a model in which two or three genes contributed additively — each "red" allele adding a fixed increment of pigment.

Here is the model for two additive loci, both parents doubly heterozygous (AaBb), each "effect" allele adding one unit and each non-effect allele adding zero:

- AABB (4 effect alleles): darkest — frequency 1/16
- Three-effect-allele genotypes (AABb, AaBB): frequency 4/16
- Two-effect-allele genotypes (AAbb, AaBb, aaBB): frequency 6/16
- One-effect-allele genotypes (Aabb, aaBb): frequency 4/16
- aabb (0 effect alleles): lightest — frequency 1/16

The F₂ distribution is 1 : 4 : 6 : 4 : 1 — five phenotype classes in binomial-coefficient proportions. The pattern generalizes: for $n$ additive loci with two alleles each, the F₂ phenotype distribution follows the binomial expansion of $(1+1)^{2n} = 4^n$, with $2n+1$ phenotype classes and frequencies proportional to $\binom{2n}{0}, \binom{2n}{1}, \ldots, \binom{2n}{2n}$.

The key consequence: as the number of contributing loci grows, the F₂ phenotype distribution converges to a normal bell curve. The number of classes grows, the spacing between adjacent classes shrinks, and the binomial coefficients converge to the Gaussian shape predicted by the central limit theorem — the sum of many independent random variables, each with bounded variance, approaches a normal distribution as the number of variables grows. Human height is the sum of contributions from more than 12,000 identified genetic variants, each with an individual effect typically below a centimeter, collectively accounting for roughly 40–50% of height variance in large samples (Yengo et al. 2022, *Nature* 610:704–712). The smooth bell curve of height in a population is not non-Mendelian. It is Mendelian, summed up at scale.

**Polygenic risk scores** in clinical medicine are the direct application: computing a weighted sum of many trait-associated variants to estimate an individual's disease risk. The arithmetic is the Mendelian product rule applied to many loci simultaneously, with each locus contributing a small additive effect. The framework does not break. It gets used at scale.

---

## Pleiotropy — one gene, many traits

**Pleiotropy** is the mirror image of polygenic inheritance: one gene affecting many traits. The canonical example is sickle-cell disease. A single nucleotide substitution in the *HBB* gene (Glu6Val in the β-globin sequence, identified by Linus Pauling and colleagues in 1949 as the first "molecular disease") causes hemoglobin S to polymerize into fibers under low oxygen, distorting red cells into the sickle shape. From one base change:

- Red-cell sickling
- Hemolytic anemia (hemoglobin ~7–8 g/dL versus normal ~14)
- Painful vaso-occlusive crises
- Organ damage from chronic hemolysis
- Increased infection risk from functional asplenia
- Resistance to *Plasmodium falciparum* malaria in heterozygotes — the reason the allele is common in historically malaria-exposed populations (Anthony Allison demonstrated the heterozygote advantage in 1954)

One mutation. Many phenotypes. They are not independent extensions of the genetic apparatus; they all flow from one upstream molecular change, cascading through tissues and physiological systems that use hemoglobin S. The genotype-phenotype map is one-to-many.

Marfan syndrome is another: mutations in *FBN1* (fibrillin-1) affect the aortic wall, the suspensory ligament of the lens, the periosteum of long bones, the heart valves, the lung — all because fibrillin-1 is a structural protein found in elastic tissues throughout the body. One mutation, many clinical features, all because the affected protein is everywhere.

The distinction from polygenic inheritance is sharp and worth stating clearly: polygenic means *many genes → one trait*; pleiotropic means *one gene → many traits*. They are orthogonal. A pleiotropic gene can also be one of many contributors to a polygenic trait. The Mendelian framework handles pleiotropy without modification — a pleiotropic allele segregates exactly like any other allele, and the offspring's genotype determines a *suite* of phenotypes rather than a single one.

---

## Penetrance and expressivity — the two-sister problem, solved

We are back where we started. The two sisters, same mutation, different lives.

**Penetrance** is the fraction of individuals carrying a particular genotype who actually display the corresponding phenotype. *BRCA1* breast-cancer penetrance is roughly 60–72% by age 80 in current best estimates — meaning that 28–40% of carriers will not develop the disease in their lifetime. Penetrance is a population-level property: a probability, averaged across many carriers.

**Expressivity** is the severity or form of the phenotype among those who do display it. Two individuals with the same genotype can have very different clinical presentations. Marfan syndrome is the canonical example: some carriers have mild lens dislocation and modest aortic root dilation; others have catastrophic aortic dissection before thirty. Same mutation. Very different expression.

The relationship: penetrance is *whether* the phenotype appears; expressivity is *how severely* it appears when it does. The two can vary independently. An autosomal-dominant disorder can have high penetrance with variable expressivity (Marfan), reduced penetrance with relatively consistent expressivity (some dominant epilepsies), or both (BRCA1: not every carrier develops cancer, and among those who do, age, subtype, and prognosis vary).

The pedigree consequence of reduced penetrance is that an autosomal-dominant disorder can appear to skip generations. The grandfather has the disease, the father is a carrier but unaffected, the son has the disease. This looks superficially like autosomal recessive inheritance. The distinguishing feature is the transmission pattern: in autosomal dominant with reduced penetrance, an affected parent has a (penetrance × 1/2) probability per pregnancy of a clinically affected child *plus* a (1 − penetrance) × 1/2 probability of an unaffected carrier child. For a 70%-penetrant autosomal-dominant condition, an affected parent has a 35% chance of a clinically affected child and a 15% chance of an unaffected carrier child — a 50% chance of transmitting the allele in total, exactly as Mendel's first law requires, with the penetrance determining how many of those transmissions become visible.

The arithmetic in the genetic-counseling office is the same Mendelian apparatus from Chapter 2, with one extra parameter inserted into the phenotype-assignment rule. The Punnett square is unchanged. Penetrance is a modifier of the function, not of the segregation.

---

## Environmental modification — PKU, G6PD, and the genotype × environment phenotype

Phenylketonuria (PKU) makes the environmental-modification point as sharply as possible. PKU is autosomal recessive, caused by mutations in *PAH* (phenylalanine hydroxylase). Without functional PAH, phenylalanine accumulates and is toxic to the developing brain: on a normal-protein diet, untreated PKU causes severe intellectual disability, microcephaly, and seizures. But an infant identified by newborn screening and placed on a phenylalanine-restricted diet develops with near-normal cognition. The same homozygous-recessive genotype, two different environments, two dramatically different phenotypes. The Mendelian transmission — 1/4 affected offspring of two carrier parents — is intact. The *clinical phenotype* depends on what the family does with the diagnosis.

G6PD deficiency (glucose-6-phosphate dehydrogenase deficiency, X-linked) is the same principle in a different direction: affected individuals are *asymptomatic in the absence of oxidative challenge*. On exposure to certain triggers — fava beans, sulfa antibiotics, primaquine — they develop acute hemolytic anemia. Same genotype, different exposures, different outcomes. Public-health guidance for G6PD-deficient patients is a list of triggers to avoid; with avoidance, most live unremarkable lives.

The conceptual model: **phenotype = genotype × environment**, with a multiplication sign rather than an addition sign — the *interaction* between the two is sometimes essential. Different genotypes have different *norms of reaction*: curves plotting phenotype across a range of environmental conditions. Some norms are flat (genotype dominates); some are steep (environment dominates); some cross (one genotype has higher phenotype in one environment but lower in another). The strict Mendelian framework assumes a flat norm of reaction — one genotype, one phenotype. The extended framework treats the norm of reaction as an empirical property of each genotype that has to be characterized, not assumed.

---

## Mitochondrial inheritance and genomic imprinting

Two extensions that genuinely step outside the Mendelian nuclear-chromosome framework.

**Mitochondrial inheritance.** Mitochondria are cytoplasmic organelles with their own small circular genome — 16,569 base pairs in humans, encoding 37 genes. When sperm fertilizes egg, only the nuclear DNA of the sperm enters the zygote; the sperm's mitochondria are excluded. The zygote's mitochondria come from the egg. This produces *maternal inheritance*: all children of an affected mother inherit the mitochondrial mutation; no children of an affected father do. The trait passes through the maternal line generation after generation. The pedigree signature is unmistakable — and unmistakably unlike Mendelian patterns.

An added complication: a mutation may be present in some mitochondria but not others within the same cell, a state called *heteroplasmy*. When a cell divides, mitochondria are distributed stochastically between daughter cells. Two siblings inheriting the same mutation from the same mother can have very different proportions of mutant mitochondria and consequently very different phenotypes. There is no Mendelian ratio for this — the inheritance is fundamentally stochastic at the organelle level. If a pedigree shows the trait transmitted from an affected father to even one child, mitochondrial inheritance is effectively ruled out.

**Genomic imprinting.** A small number of genes (roughly 100–200 in humans) are expressed from only one parental copy — which copy is silenced depends on which parent it came from, enforced by parent-of-origin-specific epigenetic marks. The canonical example is the Prader-Willi / Angelman pair, both caused by abnormalities in the same chromosomal region (15q11-q13). Deletion of the *paternal* copy produces Prader-Willi syndrome: hypotonia at birth, hyperphagia and severe obesity in childhood, intellectual disability, hypogonadism. Deletion of the *maternal* copy of the same region — specifically affecting the gene *UBE3A*, which is expressed only from the maternal copy — produces Angelman syndrome: severe intellectual disability, seizures, ataxia, minimal speech, characteristic gait. Same chromosomal region. Same type of mutation. Two different syndromes, defined entirely by which parent's copy is affected.

The Mendelian framework, on its own, cannot represent this: Mendel's dominance law does not depend on which parent provided the dominant allele. The extension required is to add a parent-of-origin tag to the allele and to make the phenotype depend on the combination of allele identity and parental origin. Gametogenesis is still Mendelian. The genotype-to-phenotype function, again, is what differs.

---

## The pattern

Look across the twelve extensions — incomplete dominance, codominance, multiple alleles, epistasis, polygenic inheritance, pleiotropy, penetrance and expressivity, environmental modification, sex influence, sex limitation, mitochondrial inheritance, genomic imprinting — and one pattern appears in almost all of them. The underlying gametogenesis is Mendelian throughout. Alleles segregate at meiosis. Gametes combine at fertilization. The product rule gives gamete frequencies correctly. What changes, extension by extension, is the *rule that turns genotype into phenotype*.

In incomplete dominance the rule adds dosage-sensitivity. In codominance it adds "both expressed simultaneously." In multiple alleles it enlarges the space of possible genotypes. In epistasis it makes the rule at one locus conditional on the genotype at another. In polygenic inheritance it sums many small Mendelian rules into one continuous distribution. In pleiotropy the rule becomes one-to-many. In penetrance it becomes probabilistic. In environmental modification it adds environment as an input. In mitochondrial inheritance it exits the nuclear-Mendelian framework entirely. In imprinting it adds a parent-of-origin tag.

The Mendelian skeleton survives every extension. What the sister with *BRCA1* needed was not a replacement for Mendel's framework but an honest accounting of one parameter — penetrance — that strict Mendelian inheritance assumed away. The mutation is real. The risk is real. The uncertainty is also real. All three things are true simultaneously, and the arithmetic of the extended framework is what lets a counselor say them out loud without contradiction.

---

## LLM exercises

The following exercises are designed for use with a large language model. Paste the prompt into any capable model and examine the response critically — not for correctness alone, but for whether the reasoning handles the genotype-to-phenotype function correctly rather than collapsing back into strict Mendelian bookkeeping.

**Exercise 1 — Dominance versus frequency**
Prompt: *"I keep hearing that dominant alleles are more common in populations. Is that true? Use Huntington's disease and ABO blood group O as contrasting examples. Explain what 'dominant' actually means at the molecular level, and what it does and does not predict about allele frequency. Then give me a third example of a rare dominant or common recessive allele from human genetics."*

Evaluate whether the model correctly distinguishes phenotypic dominance (property of the heterozygote phenotype) from allele frequency (a population-genetics quantity), and whether its third example is real and correctly characterized.

**Exercise 2 — Epistasis arithmetic from phenotype ratio**
Prompt: *"A dihybrid F₂ cross produces offspring in the ratio 9 : 7. What kind of epistasis does this suggest? Draw the modified Punnett square phenotype assignment, identify which genotype classes from the standard 9:3:3:1 are being combined, and explain the biological mechanism that could produce this pattern. Then tell me: if the ratio were 9 : 3 : 4 instead, what changes?"*

Evaluate whether the model correctly identifies duplicate recessive epistasis for 9:7 (both loci redundantly required — homozygous recessive at either locus produces the same recessive phenotype) and recessive epistasis at one locus for 9:3:4, and whether its biological mechanism is mechanistically coherent rather than just a verbal label.

**Exercise 3 — Bombay phenotype in a family**
Prompt: *"A type-A mother and a type-B father have four children: A, B, AB, and a child who tests as type O. The type-O child later tests anti-H positive and is confirmed as Bombay phenotype. What does this tell us about the parents' genotypes at both the ABO locus and the H locus? Enumerate all possible parental genotype combinations that could produce this family, and state which is most likely and why."*

Evaluate whether the model correctly concludes that both parents must carry at least one h allele (to produce an hh child), infers the ABO genotypes from the non-Bombay sibling phenotypes, and handles the distinct possibility that one or both parents might themselves be heterozygous Bombay carriers.

**Exercise 4 — Penetrance arithmetic in a pedigree**
Prompt: *"An autosomal-dominant disorder has 70% penetrance by age 60. An affected parent (who developed the disease at age 52) has three children, now ages 30, 35, and 40, all currently unaffected. (a) What is the probability that each child inherited the mutation? (b) For each child, conditional on being currently unaffected at their current age, what is the updated probability that they carry the mutation? (c) As a genetic counselor, what would you tell the 40-year-old, who is approaching the median age of onset and remains unaffected?"*

Evaluate whether the model correctly applies conditional probability (Bayesian updating on current unaffected status) to modify the prior mutation-carrier probability, and whether the counseling advice is appropriately probability-based rather than either catastrophizing or falsely reassuring.

**Exercise 5 — Polygenic to Gaussian**
Prompt: *"A trait is controlled by 2 additive loci, 5 additive loci, and 20 additive loci — three separate thought experiments. In each case, both parents are fully heterozygous at all contributing loci. (a) How many distinct phenotype classes does the F₂ show in each case? (b) What are the frequencies of the extreme phenotype classes (highest and lowest) in each case? (c) Why does the distribution converge toward a bell curve as the number of loci increases? Invoke the central limit theorem explicitly."*

Evaluate whether the model gives the correct number of phenotype classes (2n+1 for n loci), the correct extreme-class frequencies ($(1/4)^n$ each), and whether the central limit theorem explanation is mechanistically accurate (sum of independent random variables converges to Gaussian) rather than just asserting "it looks bell-shaped."

---

##  AI Wayback Machine
The genetics in this chapter didn't appear from nowhere. **Karl Landsteiner** was a Viennese physician who, in 1900, performed a deceptively simple experiment: he mixed blood from different individuals and observed which combinations agglutinated. The experiment he ran in one afternoon rearranged the safety of surgery forever.

**Run this:**

```
Who was Karl Landsteiner, and how does his 1900 discovery of the ABO
blood groups connect to the genetics of codominance and multiple alleles
covered in this chapter? Keep it to three paragraphs. End with the single
most surprising thing about his career or the history of blood typing.
```

→ Search **"Karl Landsteiner"** on Wikipedia. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to trace the path from Landsteiner's 1900 observation to the first successful blood transfusion using ABO typing — who did it, when, and what the patient outcome was.
- Ask it why it took until the 1930s for blood typing to become routine in surgical practice, even though Landsteiner published in 1900.

What changes? What gets better? What gets worse?

---

*By Nik Bear Brown*
