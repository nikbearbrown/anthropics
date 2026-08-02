# Chapter 0 — How to Use the Simulations
*Three files, one prompt structure, and why the napkin runs out of room.*

---

Brno, Moravia, summer of 1856. A 34-year-old Augustinian friar kneels at the edge of a rectangular plot of pea plants and, with a small pair of forceps, removes the immature anthers from a flower before its own pollen can ripen. His name is Gregor Mendel. He is not the abbot. He is not famous. He has failed his teaching certification exam in natural science twice — in 1850 and again this year — and he is back from a stint at the University of Vienna where he picked up probability from Andreas von Ettingshausen. He has chosen peas because they self-fertilize when left alone and come in pairs of contrasting traits a person can sort at a glance: round seeds versus wrinkled, yellow versus green, tall plants versus short.

Over the next eight years he will grow, by the standard count he reported, on the order of 28,000 plants and write what he sees in columns of integers. *5,474 round seeds. 1,850 wrinkled.* That is a 2.96 : 1 ratio. He rounds it to 3:1.

In 1865 he reads his results aloud to forty members of the Brno Natural History Society. They are polite. They do not understand what they have heard. The paper is published the next year and accumulates dust for thirty-four years, until three botanists independently rediscover the same ratios in 1900 and Mendel becomes Mendel.

Now imagine you are a genetic counselor in a hospital in 2024. A couple sits across from you. Both carry one copy of a recessive allele at the *CFTR* gene — the gene whose protein product is a chloride channel, and whose failure is cystic fibrosis. Both are healthy heterozygotes, Aa. You take out a piece of paper. You draw a 2×2 grid. You label the rows with the mother's gamete types — A and a — and the columns with the father's — A and a. You fill in four cells: AA, Aa, Aa, aa. You circle the aa. *One in four*, you say. *Each pregnancy, independent of the last.*

The grid you just drew is a Punnett square. The arithmetic underneath it is Mendel's, from sixty years earlier and four hundred miles away. The clinical decision in front of you depends on getting it right.

A monohybrid cross — one locus, both parents heterozygous — is a 2×2 grid you can sketch on a napkin. A dihybrid is a 4×4. A trihybrid is an 8×8. Add a fourth locus and the grid is 16×16 — 256 cells. Add Mendel's remaining three traits and the grid is 128×128 — 16,384 cells. The arithmetic is the same arithmetic. What fails is the napkin.

This chapter is about replacing the napkin with a simulation, and about the prompt discipline required to build one that is actually correct.

---

## The vocabulary, in one pass

Before we touch any code, I want to lay down four words precisely, because everything that follows depends on them.

A **gene** is a stretch of DNA at a specific location on a chromosome that encodes something — often a protein. The location itself is called a **locus**. An **allele** is a particular version of the gene that lives at that locus — one variant out of however many variants exist in the population. *CFTR* is a gene; the wild-type sequence is one allele; the ΔF508 deletion is another; more than two thousand catalogued variants are others. A diploid organism carries two alleles at each locus, one inherited from each parent.

The pair of alleles a person carries at a locus is their **genotype**. We write it as two letters — *AA*, *Aa*, *aa* — where uppercase is the dominant allele and lowercase is the recessive. The observable trait is the **phenotype**. Dominant means the allele's effect is what you see in the heterozygote — Aa looks like AA. Recessive means the allele's effect is hidden in the heterozygote and visible only when both copies are recessive — aa is the only genotype that shows the recessive phenotype.

One of these words misleads, and it misleads badly enough to deserve its own correction right now. *Dominant* sounds like *strong* or *common*. It is neither. The allele that causes Huntington's disease is dominant and rare — roughly one carrier in ten thousand in most populations of European descent. The allele for blood type O is recessive and common — frequency above 0.6 worldwide and above 0.8 in some Indigenous American populations. Dominance is a statement about phenotype in the heterozygote. Frequency is a statement about how many copies of the allele exist in the population. They are independent facts. Conflating them is one of the most durable misconceptions in introductory genetics, and we will encounter it again.

---

## Two principles and a combinatorial engine

In 1865 Mendel could not see chromosomes. He could not see DNA. He could not see meiosis. He could see seeds and count them. From the counts he inferred two principles that we now know describe how chromosomes behave during cell division — but he described them without knowing that.

**The principle of segregation** says: when a parent makes gametes, the two alleles at each locus separate, and each gamete carries exactly one. A heterozygote Aa produces gametes that are 50% A and 50% a. Not a blend. One allele per gamete, drawn cleanly from the pair.

**The principle of independent assortment** says: when a parent makes gametes for two or more loci on different chromosomes, the alleles at one locus assort independently of the alleles at the other. A heterozygote AaBb produces four kinds of gametes — AB, Ab, aB, ab — each at equal frequency. The choice of A versus a does not constrain the choice of B versus b.

For N independently assorting heterozygous loci, the gamete count is $2^N$. Each locus contributes a factor of 2, and the loci are independent, so the choices multiply. One locus, two gametes. Two loci, four. Three loci, eight. Seven loci — Mendel's count — 128.

This is the engine of the Punnett square. Lay the $2^N$ gametes from one parent across the top of the grid; lay the $2^N$ gametes from the other down the side; the grid has $2^N \times 2^N = 4^N$ cells; each cell is one possible offspring genotype, equally weighted because every gamete combination is equally likely under independent assortment. Count the cells by genotype. Count them by phenotype. The ratios fall out.

Let me do the combinatorics in full for three cases, because the trihybrid is where a human runs out of patience and the simulation earns its place.

**Monohybrid: Aa × Aa.** Each parent makes two gametes, A and a, each with probability 1/2. The grid is 2×2:

|               | A (1/2)   | a (1/2)   |
|---------------|-----------|-----------|
| **A (1/2)**   | AA (1/4)  | Aa (1/4)  |
| **a (1/2)**   | Aa (1/4)  | aa (1/4)  |

Genotype probabilities: P(AA) = 1/4, P(Aa) = 2/4, P(aa) = 1/4. Genotype ratio: **1 : 2 : 1**. Under complete dominance, AA and Aa share a phenotype. Phenotype ratio: **3 : 1**. This is the cystic-fibrosis number from the counseling scene.

**Dihybrid: AaBb × AaBb.** Each parent makes $2^2 = 4$ gametes — AB, Ab, aB, ab — each with probability 1/4. The grid is 4×4 = 16 cells. Under complete dominance, the phenotype classes factor cleanly, because independent assortment means probabilities multiply:

$$P(\text{A\_ B\_}) = \frac{3}{4} \cdot \frac{3}{4} = \frac{9}{16}, \quad P(\text{A\_ bb}) = \frac{3}{4} \cdot \frac{1}{4} = \frac{3}{16}$$

$$P(\text{aaB\_}) = \frac{1}{4} \cdot \frac{3}{4} = \frac{3}{16}, \quad P(\text{aabb}) = \frac{1}{4} \cdot \frac{1}{4} = \frac{1}{16}$$

Phenotype ratio: **9 : 3 : 3 : 1**. The only sentence in this section that matters: *independent assortment means probabilities multiply*. The dihybrid ratio is the product of two monohybrid ratios.

**Trihybrid: AaBbCc × AaBbCc.** Each parent makes $2^3 = 8$ gametes. The grid is 8×8 = 64 cells. The phenotype classes are $(3/4 + 1/4)^3$ expanded:

$$\text{A\_B\_C\_}: \left(\frac{3}{4}\right)^3 = \frac{27}{64}, \quad \text{A\_B\_cc}: \left(\frac{3}{4}\right)^2 \cdot \frac{1}{4} = \frac{9}{64}$$

And so on across eight phenotype classes: **27 : 9 : 9 : 9 : 3 : 3 : 3 : 1**, summing to 64. Each term is $3^{N-k}$ where k is the number of recessive-homozygous loci in that class. The whole ratio is the binomial expansion $(3 + 1)^N = 4^N$ for N = 3, sliced apart by which loci take the 1 and which take the 3.

For general N — both parents heterozygous at all N independently assorting loci, complete dominance — there are $2^N$ gametes per parent, $4^N$ cells in the grid, and $2^N$ phenotype classes in the ratio. At N = 7, the grid is 16,384 cells. The all-dominant phenotype class has count $3^7 = 2,187$ out of $4^7 = 16,384$. If you grew 100,000 offspring from a 7-locus heterozygous cross, the expected number with every recessive trait is $100{,}000 \times (1/16{,}384) \approx 6.1$ plants. Six plants out of a hundred thousand. This is the kind of number Mendel needed 28,000 plants to approach — and the kind a human cannot extract from a hand-drawn grid the size of a small room.

The simulation does it in milliseconds.

---

## Three files

Before any code, you write three text files. They go in the same folder as every simulation in this book. The LLM reads them in every prompt. This is the entire project infrastructure — no build tools, no package manager, no framework.

**CLAUDE.md** is the coding constitution. It tells the LLM what stack to use (single HTML file, D3 v7 from CDN, plain JavaScript), how to draw things (a 2D array of `<rect>` elements for grid-based diagrams, `d3.scaleLinear` for axes, 250ms transitions on parameter changes), what size canvas to default to (720×480), and crucially: how to verify. Every simulation includes a `console.log` block that prints the result of one or more biology checks the moment the file loads. For Punnett squares, those checks are the monohybrid 1:2:1, the dihybrid 9:3:3:1, and the trihybrid 27:9:9:9:3:3:3:1 — each reported as a PASS/FAIL line with measured and expected values.

**DESIGN.md** is the visual constitution. It fixes the color palette for the entire book: homozygous dominant (#1a5276, dark blue), heterozygous (#2980b9, medium blue), homozygous recessive (#85c1e9, light blue). It fixes the chart styling, the slider dimensions, the typeface. It says nothing about biology. Keeping the two files separate matters — when you change a color, you do not touch the biology; when you fix a biology bug, you do not touch the colors. The blue triad is the visual contract of the book. Every cross in every chapter shades the same way.

**PROJECT.md** is the state file. It lists what has been built (by chapter, filename, and what it models), what is in progress, and what comes next. This is the only file you actually edit chapter to chapter. The other two stay fixed.

Three plain-text files. No frameworks. Brutalist in the architectural sense — nothing decorative, every element structural.

---

## Four moves

Most students paste vague requests into Claude — *"make me a Punnett-square thing"* — and spend an hour cleaning up output that looks plausible and sums to 13. The four-move structure skips that hour.

**Show.** Point at the governing files. *"Read CLAUDE.md and DESIGN.md. Conform to them."* If you are working in Claude.ai, attach the files. If you are working in Claude Code, they are on disk and the LLM reads them automatically.

**Say.** One paragraph describing the artifact in biological terms. Not in code terms — in biology terms. *"Build a Punnett-square generator. Two parent genotypes are entered as strings of letters. The simulation enumerates the $2^N$ gametes for each parent, builds the $2^N \times 2^N$ grid, fills each cell with the offspring genotype, and shades the cell by genotype class. A readout panel reports the genotype ratio, the phenotype ratio under complete dominance, and a comparison to the theoretical expectation."*

**Constrain.** The rules beyond CLAUDE.md. The slider ranges. The input formats. The cell-size formula. The color mapping. These are the details that collapse the LLM's interpretation space — the difference between a simulation that works and one that almost works.

**Verify.** One or several falsifiable biology checks the simulation must pass, expressed as exact integers. *"On load, run three checks. (1) For Aa × Aa, genotype counts must be 1 AA, 2 Aa, 1 aa, summing to 4. (2) For AaBb × AaBb, phenotype counts must be 9 A\_B\_, 3 A\_bb, 3 aaB\_, 1 aabb, summing to 16. (3) For AaBbCc × AaBbCc, phenotype counts must be 27, 9, 9, 9, 3, 3, 3, 1, summing to 64."*

Four moves. The Verify clause is the one that does the work. The check is not "does the output look like a Punnett square" — Punnett squares are a recognizable image and an LLM will reliably produce something that looks like one even when the underlying counts are off by a cell. The check is *do the integers add up to the integers the biology requires*. Sixty-four cells in the trihybrid. Sixteen thousand three hundred eighty-four in the seven-locus cross. Twenty-seven in the all-dominant phenotype class. Numbers that have to be exact. That is what makes the verification falsifiable — and that is why it works as a firewall against fluent-but-wrong output.

You are not delegating biological judgment to the LLM. You are delegating typing. The biological judgment is yours, expressed in the integer checks the console must print on load.

---

## What the simulation does — and what it doesn't

When the verification passes — and with a complete four-move prompt it usually does on the first try, because specific integer checks are hard to fake — you have a working tool you can probe for the rest of the course.

Set N to 1 and the grid shrinks to 2×2: one dark-blue AA cell, two medium-blue Aa cells, one light-blue aa cell. The readout reports 1:2:1 genotype and 3:1 phenotype with a green match badge. This is the cystic-fibrosis case.

Drag to N = 2. The grid expands to 4×4, sixteen cells. The phenotype readout reports 9 : 3 : 3 : 1.

Drag to N = 7. The grid is 128×128 — 16,384 cells, each a few pixels wide. The colors form a fractal-like pattern: dark-blue cells are rare, light-blue cells are rare, medium-blue cells dominate, exactly as you would expect when seven independent loci each contribute a one-quarter chance of all-dominant or all-recessive. The phenotype readout has 128 entries summing to 16,384. The all-dominant class is 2,187. The all-recessive class is 1. The ratio of all-dominant to all-recessive is 2,187 : 1. Six plants out of a hundred thousand. The simulation computes it in twenty milliseconds.

But the simulation is wrong about several things, and naming exactly how it is wrong is as important as building it.

It assumes **independent assortment**. When two loci are physically close on the same chromosome, they do not assort independently — the dihybrid ratio is not 9:3:3:1. Linkage is Chapter 3.

It assumes **complete dominance**. When the heterozygote has a distinct intermediate phenotype — pink snapdragons, the blended blood types in some systems — the genotype-to-phenotype map changes and the phenotype ratios change. Also Chapter 3.

It assumes **no epistasis** — one locus's expression does not depend on another locus's genotype. Epistasis produces modified dihybrid ratios like 9:3:4, 12:3:1, or 9:7 instead of 9:3:3:1. Chapter 3 again.

It treats the offspring counts as **exact expectations**. Real offspring are a finite sample, and finite samples deviate from expectation by random fluctuation. The simulation reports the deterministic ratio. The noise is real and it matters — it is the same statistical sampling that gives genetic drift its teeth in Chapter 10.

And it is worth saying clearly: the simulation is not the biology. The Punnett-square grid is a bookkeeping device — a finite, deterministic representation of the probabilities that result from one specific kind of cross under five specific assumptions. The actual process is happening at the level of chromosomes in meiosis, sperm-egg fusion, gene expression during development, and an enormous downstream causal cascade. The Punnett square skips all of it and just reports the expected gamete combinations. When the assumptions hold, this is a brilliant economy. When the assumptions fail, the gap between the grid and the biology is where the interesting science lives. Every chapter from here forward is, in some sense, about a place where the grid's bookkeeping diverges from what real organisms actually do — and about understanding why.

---

## A note on sample size

There is one more thing the deterministic simulation hides, and it connects directly to Mendel's choice to grow 28,000 plants.

The 3:1 phenotype ratio is not a prediction about any particular family of four offspring. It is a prediction about what averages to be true across many families. Each individual offspring is the result of an independent random draw — one allele sampled from each parent — with underlying probabilities 1/4, 1/2, 1/4. With four offspring you might get exactly 1 AA : 2 Aa : 1 aa. You might also get 0 : 4 : 0, or 3 : 1 : 0, or any other combination consistent with the binomial distribution.

The formal statement: the count of aa offspring in n trials is binomially distributed $\text{Bin}(n, 1/4)$, with mean $n/4$ and standard deviation $\sqrt{n \cdot (1/4) \cdot (3/4)}$. For n = 4, the standard deviation of the aa count is about 0.87 — nearly as large as the expected value (1). For n = 1,000, the standard deviation is about 13 while the expected count is 250. For n = 28,000, the fluctuations are small enough to expose the underlying law. Mendel was not being obsessive. He was doing statistics.

This is also, in miniature, the setup for Chapter 10. When populations are finite, allele frequencies do not hold steady at their Hardy-Weinberg expectations — they drift. The larger the population, the slower the drift. The smaller, the faster. The Punnett square assumes infinite sample size and sees no drift at all. Real populations are finite. The gap is the subject of genetic drift.

---

## What connects to what

The Punnett-square simulation you will build from this chapter's prompt tells you the *outcomes* of a cross — which genotypes appear, in what proportions, producing which phenotypes. It does not tell you why those outcomes occur.

The why is meiosis. Chapter 1 takes the $2^N$ gamete count the Punnett square assumes and derives it from chromosome behavior — from homologous chromosomes pairing and separating at meiosis I, with N independently orienting chromosome pairs producing $2^N$ combinations. The simulation assumed the gametes. Chapter 1 shows where they come from.

Chapter 3 takes the simulation's five assumptions and breaks them one at a time: linkage, incomplete dominance, codominance, multiple alleles, epistasis, incomplete penetrance. The same scaffolding — gametes, grid, count, ratio — handles every extension once the genotype-to-phenotype map is generalized. The simulation does not change. The map does.

Chapter 10 adds the noise the simulation leaves out. Hardy-Weinberg is the population-scale extension of the same arithmetic — what happens when you sum Punnett squares across an entire randomly mating population and ask what allele frequencies you expect in the next generation. Genetic drift is what happens when the population is finite and that sum is replaced by a sample.

Every chapter that follows is, in one way or another, an extension of the combinatorics you are about to put on the screen.

The first time Chapter 1 talks about a chromosome, a bivalent, or an anaphase — the first time it says the words *independent assortment* with a mechanism behind them — pull up `00-punnett-square.html`, set N = 7, and watch the 16,384 cells of a fully-loaded pea-plant cross, knowing now where every one of those cells came from.

---

## LLM Exercise — Build your Punnett-square generator

This block is the one you actually do. The prompt below is ready to paste at Claude (or ChatGPT, or Gemini) once you have CLAUDE.md and DESIGN.md saved in the same folder.

### The simulation prompt

```
Show: Read CLAUDE.md and DESIGN.md from this project. Conform to them.

Say: Build 00-punnett-square.html — a generalized Punnett-square
generator. The user enters two parent genotypes as strings of letters:
uppercase = dominant allele, lowercase = recessive. "Aa" is a
monohybrid heterozygote. "AaBb" is a dihybrid. "AaBbCc" is a
trihybrid. Accept up to seven loci using letters A through G in
alphabetical order. For each parent, enumerate the 2^N gamete
strings under independent assortment (each gamete carries one allele
from each locus; all 2^N combinations equally likely). Build the
2^N x 2^N grid. Each cell combines the row gamete from parent 1 with
the column gamete from parent 2 to produce a diploid offspring
genotype. Color each cell by genotype class: homozygous-dominant at
every locus = #1a5276 (dark blue); homozygous-recessive at every
locus = #85c1e9 (light blue); anything else (heterozygous at one or
more loci) = #2980b9 (medium blue). Label each cell with the
offspring genotype string in monospace text sized to fit. A readout
panel below the grid lists: (a) the exact-genotype count summary
grouped by genotype string; (b) the phenotype count summary under
complete dominance using the A_ underscore convention; (c) the
theoretical expectation — 1:2:1 and 3:1 at N=1, 9:3:3:1 at N=2,
27:9:9:9:3:3:3:1 at N=3, the binomial expansion (3+1)^N for general
N — with a green "match" or red "mismatch" badge.

Constrain: Slider — N (1 to 7, default 3). Two text inputs accept
parent-genotype strings, validated to length 2N and format
[A-G][a-g] pairs in alphabetical order. Cell size =
min(40, 600 / 2^N) px. Grid centered horizontally. Single
self-contained HTML file. D3 v7 from CDN. Add at the top of script:
// CLAIM: For N independently assorting loci, both parents
// heterozygous, the Punnett-square grid has 2^N x 2^N cells and the
// phenotype ratio under complete dominance is the binomial expansion
// (3+1)^N.

Verify: Biology check — print to the console on every parameter
change, as PASS/FAIL lines with measured values, expected values,
and the cross:
  (1) For Aa x Aa: genotype counts must be {AA:1, Aa:2, aa:1},
      sum = 4.
  (2) For AaBb x AaBb: phenotype counts must be
      {A_B_:9, A_bb:3, aaB_:3, aabb:1}, sum = 16.
  (3) For AaBbCc x AaBbCc: phenotype counts must be
      {A_B_C_:27, A_B_cc:9, A_bbC_:9, aaB_C_:9, A_bbcc:3,
       aaB_cc:3, aabbC_:3, aabbcc:1}, sum = 64.
  (4) For arbitrary N: total cell count = 4^N; all-dominant
      phenotype class count = 3^N.
```

### Exploration tasks

Once the file runs, work through these. Each one is a small experiment.

1. **The integer-check test.** Set N = 3 with both parents *AaBbCc*. Open the console. The third verification line should read PASS with the eight-number ratio summing to 64. Now manually edit the LLM-generated code to introduce a deliberate bug — replace a `>=` with `>` in the genotype-to-phenotype mapping. Reload. The console should now report FAIL with a ratio that does not sum to 64. Reverse the edit. The point: verification is real. It catches errors when they exist and passes only when the counts are exactly right.

2. **The locus-doubling test.** Hold both parents at full heterozygosity and step N from 1 to 7 in unit increments. At each value, write down the total cell count, the all-dominant phenotype count, the all-recessive phenotype count, and the ratio of all-dominant to all-recessive. The cell counts should be 4, 16, 64, 256, 1024, 4096, 16,384 — powers of four. The all-dominant counts should be 3, 9, 27, 81, 243, 729, 2,187 — powers of three. The all-recessive count should always be 1.

3. **The dominance-versus-frequency test.** Set N = 1 with one parent *Aa* and the other *aa*. This is a testcross. The phenotype ratio is 1:1 — half dominant, half recessive — even though A is the dominant allele. Now change the second parent to *AA*. The phenotype ratio is 1:0 — all dominant. Same dominant allele. Different ratio. Dominance is not a statement about ratio. It is a statement about how an allele expresses in the heterozygote. The testcross is the standard tool for determining whether an individual with the dominant phenotype is homozygous (all offspring dominant) or heterozygous (offspring split 1:1).

4. **The sample-size test.** This is the most important exercise in the chapter — and the move that previews Chapter 10's drift simulation. Modify the prompt with this extension:

> *"Add a stochastic mode. When stochastic mode is enabled, instead of displaying the full deterministic grid, generate n actual offspring by sampling, for each offspring, one gamete from parent 1 (uniformly at random over the 2^N gamete types) and one gamete from parent 2 (the same), then combining to produce a diploid genotype. Tally the observed genotype and phenotype counts and display them next to the theoretical expectations. A slider sets n (range 4 to 10,000, default 100)."*

Run this with N = 1, both parents *Aa*, and n = 4. Look at the observed counts. Resample ten times. You will see ratios like 1:3:0, 0:2:2, 2:1:1 — all consistent with the underlying probabilities, none of them exactly 1:2:1. Now set n = 10,000. The observed counts will be tight around 2,500 AA, 5,000 Aa, 2,500 aa. Sample size is everything. This is what Mendel was doing across 28,000 plants. This is also the seed of Chapter 10, where the finite size of real populations causes allele frequencies to wander stochastically across generations.

### Extension prompt

Once the basic simulator works, extend it to handle incomplete dominance at a designated locus:

```
Extension: Modify 00-punnett-square.html to support incomplete
dominance at a designated locus. Add a dropdown next to the
parent-genotype input that lets the user mark each locus as either
"complete dominance" (default; heterozygote phenotype = dominant
homozygote phenotype) or "incomplete dominance" (heterozygote
phenotype = a third intermediate category, distinct from both
homozygotes). When a locus is marked incompletely dominant, the
phenotype ratio for crosses involving that locus changes: a
monohybrid Aa x Aa cross now gives 1:2:1 phenotype (not 3:1); a
dihybrid AaBb x AaBb cross with the A locus incompletely dominant
and the B locus fully dominant gives the outer product of (1:2:1)
x (3:1) = 3:6:3:1:2:1, summing to 16.
Verification: for a monohybrid incompletely-dominant cross Aa x Aa,
phenotype counts must be 1 red : 2 pink : 1 white, summing to 4.
For a dihybrid cross with A locus incompletely dominant and B locus
fully dominant (AaBb x AaBb), phenotype counts must be 3:6:3:1:2:1,
summing to 16.
```

This is the simulation you will reach for when Chapter 3 introduces extensions to Mendelian inheritance. The scaffolding does not change. The genotype-to-phenotype map does.

---

*By Nik Bear Brown*
