# Chapter 09 — Microbial Growth

*A bacterium does not grow by getting larger. It grows by becoming more numerous.*

## The question before the answer

If you put a single bacterium into a tube of nutrient broth at body temperature and come back twelve hours later, the tube will be cloudy. Cloudy means there are now somewhere around a billion bacteria in it.

A billion bacteria from one bacterium in twelve hours. That works out to roughly thirty doublings. *E. coli* under ideal conditions divides about every 20 minutes. Twelve hours is 36 generations. Each generation roughly doubles the population. The math is exponential.

If exponential growth continued unimpeded — and it does not — a single bacterium dividing every 20 minutes would, in 48 hours, produce a mass of cells equal to the mass of the Earth. The reason this never happens is that nutrient runs out, waste accumulates, and the population enters a stationary phase long before it gets anywhere near astronomical numbers.

This chapter is about the dynamics of microbial populations in time, in space, and under environmental constraints. The same logic applies to a clinical infection (a single bacterium entering a wound can produce a lethal population in two days) and to a biofilm on a catheter (a population that has organized itself into a structured community resistant to antibiotics). Understanding microbial growth is understanding the timescales on which microbial life operates.

## Learning objectives

By the end of this chapter, you will be able to:

1. Define generation time and calculate population sizes after a given number of generations.
2. Describe the four phases of the bacterial growth curve and identify what is happening to the population in each.
3. Distinguish viable cell counts from total cell counts and pick the right method for a given purpose.
4. Describe biofilm formation and explain why biofilms are clinically problematic.
5. Match a microbe to its preferred range of oxygen, pH, temperature, salinity, and pressure based on a habitat description.
6. Choose a culture medium (defined vs. complex, selective vs. differential, enriched) appropriate to a target organism.

Prerequisites: Chapters 1–8.

## Binary fission and generation time

Most bacteria reproduce by **binary fission**: a single cell duplicates its DNA, elongates, and pinches in half, producing two cells where there was one. The whole process takes anywhere from 10 minutes (for the fastest *E. coli* under optimal conditions) to 24 hours (for *Mycobacterium tuberculosis*) or longer (for some soil archaea).

The **generation time** (or doubling time) is the average time between cell divisions. If the generation time is *g* and the starting population is *N₀*, after *t* hours the population is approximately:

$$ N = N_0 \times 2^{t/g} $$

For *E. coli* with *g* = 20 minutes, starting from one cell, after 12 hours: N = 1 × 2^(720/20) = 2^36 ≈ 7 × 10^10 cells. A billion-fold increase.

For *Mycobacterium tuberculosis* with *g* = 18 hours, starting from one cell, after the same 12 hours: N ≈ 2^(12/18) ≈ 1.6 cells. Less than one doubling. After two weeks: 2^(336/18) ≈ 4000 cells. This is why TB cultures take so long to grow and why a TB diagnosis sometimes takes weeks.

Generation time depends on temperature, nutrient availability, pH, oxygen, and a host of other factors that we will get to. Under ideal conditions in a lab, the times above are achievable. In real-world environments — a glass of milk on a counter, a wound, a soil — generation times are usually longer because conditions are not ideal.

## The growth curve

Put a small number of bacteria into a fresh batch of broth and watch the population over time. You will see four distinct phases.

### Lag phase

For some period after inoculation, the cell count does not increase. The cells are alive — they are synthesizing enzymes, repairing damage, adjusting to the new medium. They are getting ready to divide but have not started yet. The length of the lag phase depends on how different the new conditions are from the previous conditions; cells transferred from a stationary culture to fresh medium may have a long lag; cells transferred from one exponentially growing culture to another may have none.

### Exponential (log) phase

Once the population starts dividing, it divides at the fastest rate the conditions allow. Cell number doubles at intervals of one generation time. On a log scale, the cell count plotted against time is a straight line.

This is the phase microbiologists work in. Cells in log phase are doing the most metabolic activity, growing the fastest, and behaving most reproducibly. Most experiments in microbial physiology use log-phase cells.

### Stationary phase

Eventually, the population reaches a density at which growth rate equals death rate. New cells are being born; old cells are dying; the net change is zero. The total population is constant. The reasons for the plateau are usually some combination of nutrient depletion (the medium runs out of something the cells need) and waste accumulation (the cells produce something that inhibits further growth — for example, acid from fermentation lowering the pH).

For *E. coli* in standard broth, stationary phase typically peaks at around 10⁹ cells per milliliter — a billion cells in the volume of a thimble.

### Death phase

After enough time in stationary phase, the death rate exceeds the birth rate. The viable population declines. The decline is also typically exponential, though slower than the growth phase. Some bacteria can survive prolonged starvation by entering a dormant state; many cannot, and the population can collapse to a small fraction of its peak.

The growth curve is observable. You can plot it for any organism in any medium and the same four-phase shape appears. The shape is so robust that it has become a standard test of microbial physiology: pick an organism, pick a condition, plot the growth curve, compare.

## Counting bacteria

Several methods exist for measuring how many bacteria are in a sample. They are not interchangeable.

**Total cell count** measures every cell, alive or dead. The simplest method is direct microscopy with a counting chamber (a hemocytometer or Petroff-Hausser counter) — you spread the sample in a chamber of known volume and count visible cells under a microscope. Quick but tedious. A faster alternative is optical density (turbidity): cloudy cultures scatter more light, and a spectrophotometer at 600 nm gives you a number that correlates with cell density. The correlation is rough and depends on the organism. Optical density does not distinguish living from dead cells; it does not distinguish bacterial cells from cellular debris.

**Viable cell count** measures only cells capable of reproducing. The classical method is **dilution and plating**: you serially dilute the sample, plate measured volumes on agar plates, incubate until colonies appear, and count the colonies. Each colony represents one viable cell that landed on the plate. The result is reported in colony-forming units (CFU) per milliliter. This is the gold standard for clinical microbiology — when you want to know how many living bacteria are in a urine sample (Chapter 23) or a blood culture (Chapter 25), CFU is what you measure.

Viable plate counts have limitations. They count only the cells that grow on the medium and conditions used. Most environmental and even most clinical microbes cannot be cultured under standard lab conditions. We met the "great plate count anomaly" already in Chapter 4: in many environments, the number of cells visible by microscopy exceeds the number that grow on plates by two or three orders of magnitude. The unculturable majority is invisible to viable plate count.

Newer methods address this. **Quantitative PCR** (qPCR) measures the number of copies of a specific DNA sequence in a sample, giving an estimate of total genomes (and therefore total cells, if there is one copy per cell). It does not require culture but does require knowing what sequence to target. **Flow cytometry** counts individual cells passing through a laser beam, and can distinguish live from dead with appropriate stains. **MALDI-TOF mass spectrometry** (Chapter 7) identifies organisms in mixed samples.

↳ **Dig Deeper — Single-cell microbiology**

*Population averages hide individual variation. Single-cell techniques are revealing that "identical" bacteria in the same culture behave quite differently.*

**Prompt:**
> Describe modern single-cell microbiology techniques and what they have revealed. Cover microfluidic devices that track individual cells over time, single-cell RNA-Seq applied to bacteria, fluorescent reporter strains for measuring gene expression in individuals, and the discovery of phenotypic heterogeneity within clonal populations (persisters, division-of-labor in biofilms). What does this tell us about the limits of population-average measurements like growth curves?

**What to do with the output:** This is one of the active edges of microbiology. The chapter's growth-curve framework is the population average; single-cell techniques are revealing what the individuals are doing.

## Biofilms

If you imagine a bacterium, you probably imagine a single cell swimming through a liquid. That is not how most bacteria live.

In nature, most bacteria live in **biofilms** — structured, surface-attached communities embedded in a self-produced matrix of polysaccharides, proteins, and DNA. The matrix sticks the cells to the surface and to each other. The biofilm is a multicellular organization: cells in different layers experience different oxygen levels, different nutrient concentrations, different stresses, and they specialize accordingly.

Biofilm formation follows a stereotyped sequence:

1. **Initial attachment**: a free-swimming cell encounters a surface and reversibly attaches.
2. **Irreversible attachment**: the cell starts producing extracellular polymers that anchor it.
3. **Microcolony formation**: the attached cell divides; daughter cells stay associated.
4. **Maturation**: the colony develops three-dimensional structure, with channels for nutrient flow and waste removal.
5. **Dispersal**: some cells leave the biofilm to colonize new sites, sometimes triggered by environmental cues.

Biofilm formation involves **quorum sensing** — cells release small signal molecules that diffuse through the environment; once a threshold concentration is reached, the cells coordinate gene expression. The threshold gets crossed when enough cells are present, which is why biofilms organize themselves only at sufficient cell density. Quorum sensing is bacterial communication, and it controls biofilm maturation, virulence factor expression, and many other community-level behaviors.

### Why biofilms matter clinically

Biofilm cells are typically 10 to 1000 times more resistant to antibiotics than the same bacteria growing planktonically (free-swimming). The reasons are several: the matrix slows antibiotic diffusion; cells deep in the biofilm grow slowly and are less vulnerable to drugs that target dividing cells; a subset of cells (persisters) enter a dormant metabolic state that almost no antibiotic touches; and the close cell-cell contact in a biofilm increases horizontal gene transfer of resistance genes.

Biofilms cause many of the chronic and hard-to-treat infections in modern medicine:

- **Dental plaque** is a biofilm of oral bacteria, primarily *Streptococcus mutans*. It is responsible for tooth decay (Chapter 24) and periodontal disease.
- **Catheter-associated urinary tract infections** are biofilms of *E. coli* and *Pseudomonas* on the inner surface of indwelling catheters. The biofilm continuously releases bacteria into the urine, causing infection that recurs as soon as antibiotics are stopped.
- **Prosthetic joint infections** are biofilms of *Staphylococcus epidermidis* or *S. aureus* on the metal or polymer of an artificial knee or hip. They are nearly impossible to clear without removing the prosthesis.
- **Cystic fibrosis lung infections** are biofilms of *Pseudomonas aeruginosa* in the thickened mucus of CF airways. They establish in childhood and persist for life.
- **Endocarditis** can be a biofilm on a heart valve, with bacterial colonies attached to damaged valve tissue.

The clinical lesson: a biofilm infection is not a free-floating bacterial problem. It is a structured community that has to be physically disrupted or removed, often surgically. Antibiotic therapy alone is rarely sufficient.

↳ **Dig Deeper — Quorum sensing as bacterial language**

*The signals bacteria use to coordinate biofilm formation, virulence factor production, and other group behaviors are a genuine communication system. The molecules are simple. The information processing is not.*

**Prompt:**
> Describe quorum sensing in bacteria. Cover at least three different signal molecule families (acyl-homoserine lactones in Gram-negatives, autoinducing peptides in Gram-positives, AI-2 as an interspecies signal). Explain how the threshold density gets translated into gene expression changes via two-component signaling. Identify three medically important phenotypes regulated by quorum sensing (e.g., *Pseudomonas aeruginosa* virulence, *Vibrio cholerae* biofilm dispersal, *Staphylococcus aureus* virulence). End by discussing quorum quenching as a therapeutic strategy.

**What to do with the output:** Anti-quorum-sensing drugs are an active research area. Save the answer for Chapter 14 when we discuss the antibiotic pipeline; QS inhibitors are part of the post-antibiotic strategy.

## Environmental requirements

A given microbe grows within a particular envelope of environmental conditions. Outside the envelope, it grows slowly or not at all.

### Oxygen

Microbes are classified by how they handle oxygen.

- **Obligate aerobes** require oxygen. They have an electron transport chain that uses O₂ as the final acceptor. *Mycobacterium tuberculosis*, most fungi, most molds.
- **Obligate anaerobes** cannot tolerate oxygen. They lack the enzymes (superoxide dismutase, catalase, peroxidase) needed to detoxify reactive oxygen species. *Clostridium*, *Bacteroides*. They live in environments where oxygen is absent: deep mud, anaerobic digesters, the human large intestine.
- **Facultative anaerobes** prefer oxygen when it is available (because aerobic respiration is more efficient) but can switch to fermentation or anaerobic respiration when it isn't. *E. coli*, most enterobacteria, *Saccharomyces*.
- **Microaerophiles** require oxygen but at lower-than-atmospheric concentrations (around 2–10%). High oxygen damages them. *Helicobacter pylori*, *Campylobacter*.
- **Aerotolerant anaerobes** do not use oxygen but can survive in its presence. *Lactobacillus*, *Streptococcus*. They do fermentation regardless of oxygen.

The oxygen tolerance of a clinical isolate matters: anaerobes will not grow on aerobic cultures, which is why specialized anaerobic culture techniques are needed for samples from infected sites (abscesses, deep wounds, bowel) where anaerobes are likely.

### pH

Most bacteria grow best between pH 6 and 8 — close to neutral. Some grow at extremes.

- **Acidophiles** thrive at low pH. *Sulfolobus* and other acidophilic archaea grow at pH 1–3. *Lactobacillus* grows best around pH 5. The stomach (pH ~1.5) is a hostile environment for most microbes, which is part of the reason *Helicobacter pylori*'s ability to survive there was surprising.
- **Neutrophiles** prefer near-neutral pH. Most pathogens. Most environmental bacteria.
- **Alkaliphiles** thrive at high pH (above 9). *Vibrio cholerae* tolerates higher pH than most enterics, which is why alkaline peptone water is used as a selective enrichment medium for it.

### Temperature

- **Psychrophiles** grow at cold temperatures, with optima below 15°C. They live in polar oceans, deep sea, refrigerators. They have membrane lipids enriched in unsaturated fatty acids that stay fluid at low temperature.
- **Psychrotrophs** grow at refrigerator temperatures (4–10°C) but prefer warmer (~25°C). Many food spoilage organisms. *Listeria monocytogenes* is a notorious psychrotroph — it grows in refrigerated foods and causes listeriosis.
- **Mesophiles** prefer moderate temperatures (20–45°C). Most human pathogens are mesophiles, with optima near 37°C (body temperature).
- **Thermophiles** grow at 45–80°C. Hot springs, compost piles, hydrothermal vents.
- **Hyperthermophiles** grow above 80°C. Many are archaea. *Pyrolobus fumarii* grows at 113°C.

↳ **Dig Deeper — The upper temperature limit of life**

*Above what temperature does cellular life become impossible? The current record is around 122°C in laboratory conditions. The theoretical ceiling is higher.*

**Prompt:**
> Describe what is known and what is hypothesized about the upper temperature limit of cellular life. What is the current record-holder for highest growth temperature (*Methanopyrus kandleri* strain 116)? What molecular adaptations allow proteins and membranes to remain functional at >100°C (reverse gyrase, chaperones, ether lipids)? At what temperature do critical biomolecules (ATP, proteins, DNA) become unstable, and is there any cellular workaround? End by speculating on what temperatures life might survive at on other worlds or in extreme Earth environments not yet sampled.

**What to do with the output:** This is one of the more interesting questions in astrobiology and in the biophysics of life. The limit is not infinite, but it is higher than most people guess.

### Osmotic and barometric pressure

Some bacteria require high salt concentrations to grow (**halophiles** — *Halobacterium* needs at least 10% NaCl, with optimum around 25%). Some require high pressure (**barophiles** or **piezophiles** — deep-sea organisms that don't grow at atmospheric pressure).

### Nutritional requirements

Bacteria differ in what nutrients they need provided versus what they can make for themselves. A **defined** medium contains chemically known compounds; a **complex** medium contains undefined biological extracts (yeast extract, peptone, beef extract). Defined media are necessary for studying biochemistry; complex media are easier and grow more organisms.

Media can also be:

- **Enriched**: contains additional nutrients (blood, yeast extract) that fastidious organisms need.
- **Selective**: contains agents that inhibit some organisms while allowing others to grow. MacConkey agar contains bile salts and crystal violet, which inhibit Gram-positives, so only Gram-negatives grow.
- **Differential**: contains indicators that produce visible differences between organisms. MacConkey is also differential: it contains lactose and a pH indicator, so lactose-fermenting bacteria produce pink colonies while non-fermenters produce colorless colonies.

A good clinical microbiology medium is often selective *and* differential — it lets you grow your target organism and immediately distinguish it from related species.

## What the chapter is really about

Microbial growth is the dynamics of a population reacting to its environment. The growth curve, the biofilm life cycle, the temperature and pH and oxygen tolerances — these are not arbitrary details. They are the dimensions along which microbial populations live and die.

Clinically, the consequences are concrete:

- If a patient has a urinary tract infection at 10⁵ CFU/mL but you collect the sample wrong and there are 10⁸ CFU/mL by the time it reaches the lab, you cannot distinguish infection from contamination. Timing matters.
- If an antibiotic kills 99.9% of *Staphylococcus aureus* in a wound but the remaining 0.1% are in a biofilm, the surviving cells will repopulate the wound within days. The biofilm is the failure mode.
- If a patient with abdominal sepsis is empirically treated with an aerobic-spectrum antibiotic, the anaerobic bacteria in the abscess will not be touched. The abscess will not resolve. The patient will need anaerobic coverage and probably surgical drainage.

The growth-curve framework also matters for sterilization (Chapter 13). A killing process that reduces a population from 10⁶ to 10² is impressive on a log scale; in absolute numbers it leaves a hundred surviving cells, which is enough to repopulate the system if they have time. Killing has to be quantified, and the killing has to outpace the regrowth.

## Still puzzling

I do not fully understand the persister phenomenon. Within a clonal population of bacteria — genetically identical cells, in identical medium — a small fraction will be in a dormant metabolic state that makes them resistant to virtually all antibiotics. When the antibiotic is removed, persisters resume normal metabolism and can regrow the population. They are not genetically resistant; they are *phenotypically* resistant by virtue of being slow. Why a clonal population produces persisters at the rate it does, and what triggers an individual cell to enter the persister state, is not well understood. Some evidence points to stochastic gene expression — a few cells, by chance, have low ribosome content or particular stress responses active, and they happen to survive the antibiotic. The mechanism is being worked out; the clinical implications are large.

## What would change my mind

The conventional growth curve, with four discrete phases, is an idealization of what happens in a closed batch culture in a single environment. Real microbial populations in real environments rarely look this clean. If new high-throughput single-cell techniques (microfluidics, time-lapse microscopy of individual cells) substantially revise our picture of microbial growth dynamics — for example, by showing that most natural populations live in a continuous low-grade growth state rather than going through the textbook phases — the four-phase model will need to be replaced with something more nuanced for many contexts. `[verify: state of single-cell microbial growth dynamics literature as of 2026]`

## LLM exercises

1. **Doubling time, multiple ways.** Give the LLM three organisms with different generation times (*E. coli* 20 min, *M. tuberculosis* 18 hours, *Streptococcus mutans* 1 hour) and ask it to calculate how many cells each will produce starting from a single cell after 1 day, 1 week, and 1 month. Then ask which scenarios are biologically realistic and which are not, and why.
2. **The persister problem.** Ask the LLM what a persister is and why persisters are hard to kill with antibiotics. Then ask what experimental design would be needed to test whether a particular drug candidate works against persisters. Critique the design.
3. **Designing a selective medium.** Tell the LLM you want to selectively grow *Salmonella* from a stool sample. Ask it to design a culture medium (selective, differential, or both) and to justify each component. Compare to actual selective media for *Salmonella* (Hektoen Enteric agar, XLD).
4. **Reading a growth curve.** Describe a growth curve where the lag phase is unusually long, the log phase has a smaller slope than expected, and stationary phase is reached at a lower density. Ask the LLM what could be wrong with the conditions. The point is differential diagnosis of growth conditions.
5. **The biofilm matrix.** Ask the LLM what is in the biofilm matrix and what each component contributes to biofilm resistance. Then ask whether a treatment that targeted the matrix specifically — say, an enzyme that broke down the polysaccharides — would be useful clinically. What are the trade-offs?

## References

(This chapter draws on standard microbiology coverage of growth dynamics; the OpenStax source provides the consensus framework. Primary sources for biofilm research: Costerton, J.W. et al. "Bacterial biofilms: a common cause of persistent infections." *Science* 284, no. 5418 (1999): 1318–1322. doi:10.1126/science.284.5418.1318.)
---

## LLM Exercise — Chapter 9: Microbial Growth (Microbe Profile Database Project)

**Project:** Microbe Profile Database.
**What you're building this chapter:** growth-condition fields + 1-2 entries with notable growth characteristics.
**Tool:** **Cowork**.

---

**The Prompt:**

```
Chapter 9 of my Microbe Database project. Chapter 9 covered
microbial growth — generation time / doubling time; the growth
curve (lag, log/exponential, stationary, death); temperature
ranges (psychrophile, mesophile, thermophile, hyperthermophile);
pH ranges (neutrophile, acidophile, alkaliphile); osmotic
requirements (halophiles); nutrient requirements (autotrophs,
heterotrophs).

Schema additions:
- **Optimum_temperature**: in °C.
- **Temperature_range**: e.g., "20-45 °C" or "psychrophilic" or
  "mesophilic" or "thermophilic."
- **Optimum_pH**: neutral / acidic / alkaline / specific number.
- **Generation_time**: typical (in minutes/hours).
- **Special_growth_requirements**: any unusual ones (e.g., 5% CO2
  for Neisseria; chocolate agar for Haemophilus; iron for many
  pathogens).

Backfill these for existing entries. Notable:
- *Mycobacterium tuberculosis*: very slow generation time (~20
  hours); the reason TB treatment is months long.
- *Halobacterium salinarum*: requires 15-30% NaCl.
- *Helicobacter pylori*: microaerophilic; needs urea-rich environment
  to neutralize stomach acid.
- *Lactobacillus acidophilus*: acidophilic; thrives at pH 4-5.

Add 1-2 new entries:
1. **Listeria monocytogenes** — Gram-positive bacillus; grows at
   refrigerator temperatures (4°C — uniquely dangerous for
   refrigerated foods); causes listeriosis in pregnancy + immuno-
   compromised.
2. *(optional)* **Yersinia pestis** — Gram-negative, plague
   pathogen; optimal growth ~28°C (flea body temperature);
   slower at human body temp (37°C).

End with: query — "all organisms that grow at refrigerator
temperatures" (< 8°C). The answer should be a short list with
Listeria prominent. Why does this matter for food safety?
```

---

**What this produces:** Growth fields + 1-2 new entries. Database ~26-31 entries.

**Connection to previous chapters:** Ch 8's metabolism fields + Ch 9's growth fields describe how organisms thrive — clinical implications for which hospital surfaces and food handling matter.

**Preview of next chapter:** Chapter 10 turns to molecular biology — genome biochemistry. Adds genome fields (size, GC content, plasmids).


---

## AI Wayback Machine

**Jacques Monod** was French biologist whose work on bacterial growth curves and diauxic shift founded modern microbial growth physiology — Nobel 1965.

**Run this:**

```
Who is Jacques Monod, and how does their work connect to microbial growth we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Jacques Monod"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Jacques Monod's ideas to a contemporary microbiology problem.
- Add a constraint: "Answer including criticisms or limits of Jacques Monod's framework."

What changes? What gets better? What gets worse?
