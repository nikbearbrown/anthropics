# Chapter 7 — The Microbial Genome and Genetics

*Resistance does not evolve. It spreads. The difference is everything.*

---

In 2001, a hospital in North Carolina isolated a strain of *Klebsiella pneumoniae* carrying an enzyme nobody had seen before. The enzyme — KPC-1 — could destroy carbapenems, the antibiotic class that clinicians had been treating as a last resort, the drugs you reach for when everything else has failed. The isolate was unusual. A curiosity. A single case report in a minor journal.

Fifteen years later, KPC was on six continents.[^1]

Not fifteen years of gradual Darwinian spread. Fifteen years of a gene — a single stretch of about 860 base pairs — jumping from cell to cell, species to species, city to city, contained inside a plasmid that did not care which organism it ended up in as long as that organism could copy it. The gene did not evolve fresh in each new location. It moved. There is a difference, and understanding the difference is the whole point of this chapter.

---

## What the genome actually is

A bacterial cell carries its genetic information in a form that looks, at first, almost insultingly spare.

One chromosome. A single closed loop of double-stranded DNA. In *E. coli*, 4.6 million base pairs — about a millimeter long if you stretched it out, in a cell two micrometers end to end. The DNA has to be compacted by a factor of roughly a thousand to fit. Bacteria manage this without histones, the spool proteins eukaryotes use. Instead they use **supercoiling** — the helix twists on itself like a phone cord left to curl, packing tight while remaining accessible to the machinery that has to read it. The enzyme that maintains this supercoiling is called **gyrase**. The DNA sits in a region called the **nucleoid** — not a walled-off nucleus, just a dense neighborhood in an unwalled cell.[^2]

Gyrase matters for a reason we will return to: it is one of the targets of the fluoroquinolone antibiotics. Ciprofloxacin, levofloxacin, moxifloxacin all bind gyrase, trap it while the DNA strand is cut, and prevent the resealing step. The bacterium effectively shreds its own chromosome trying to replicate. The selectivity — the reason the drug kills the bacterium without killing the patient — is that human topoisomerases are sufficiently different from gyrase that the drug cannot grab them. Bacterial genome architecture, and the specific enzyme that maintains it, is directly the reason a drug works.

Beyond the chromosome, many bacteria carry **plasmids** — small, circular, extrachromosomal DNA molecules that replicate on their own schedule. You can often cure a bacterium of its plasmid by various tricks in the lab, and the bacterium goes on living. So in some sense plasmids are optional. In another sense they are anything but. They carry genes that earn their keep: antibiotic resistance, virulence factors, metabolic capabilities, and — crucially — the machinery for moving themselves between cells.

Three plasmid families keep showing up:

**F plasmids** (F for fertility) encode the cell-to-cell transfer apparatus. **R plasmids** (R for resistance) carry antibiotic resistance genes. The R plasmid R100, first characterized in the 1960s, carries resistance to tetracycline, chloramphenicol, streptomycin, sulfonamide, and mercury — five different mechanisms on one molecule, transferable as a single package.[^3] **Virulence plasmids** carry the toxin and adhesion genes that convert a harmless bacterium into a pathogen. *Bacillus anthracis* without pXO1 cannot cause anthrax. The chromosome is the cell's identity. The plasmid is the cell's circumstances — and circumstances can change in a single generation.

<!-- → [DIAGRAM: Bacterial cell with chromosome (nucleoid), one large plasmid, one small plasmid — annotated with gyrase acting on the chromosome, plasmid sizes relative to chromosome, and callout showing that multiple plasmids can coexist in one cell] -->

---

## Reading the genome: the central dogma, microbial style

DNA → RNA → protein. The same three-step arrow runs through every cell on Earth. What varies between bacteria and eukaryotes is the machinery, the speed, and — in clinically important ways — the points where antibiotics can interrupt.

Replication runs on a familiar cast of enzymes. Helicase unwinds. Gyrase handles the topological stress ahead of the fork. Primase lays down RNA primers, because DNA polymerases cannot start from nothing. DNA polymerase III does the bulk synthesis, adding about a thousand nucleotides per second with an error rate around one in ten million. Polymerase I chews out the primers and fills in. Ligase seals the nicks. Two forks, moving in opposite directions from a single origin, replicate the entire *E. coli* chromosome in about forty minutes.

The error rate of one in ten million sounds small. For a single cell dividing once, it is: zero or one mutation per genome per generation. But bacterial populations are not single cells. A gram of gut contents contains roughly 10⁹ bacteria. One round of division introduces roughly 10⁹ × (4.6 × 10⁶ / 10⁷) ≈ 4.6 × 10⁸ new mutations across that population. Most are harmless or lethal to the cell that carries them. Some, by accident, land in a gene where they confer an advantage. Mutation rate is small per cell but inexhaustible across a population.

Transcription in bacteria is done by a single RNA polymerase that handles all genes. But the polymerase by itself is promiscuous — it does not know which genes to start reading. To find the right promoters, it needs a **sigma factor**, a subunit that gives the complex its sequence specificity. The standard "housekeeping" sigma factor in *E. coli* (σ⁷⁰) recognizes the familiar −10 and −35 promoter elements. But there are others: σ³² for heat-shock genes, σ²⁸ for flagellar genes, σ^S for stationary-phase genes. By changing which sigma factor is available, the cell changes which entire set of genes gets transcribed — a wholesale switch rather than a million individual toggles. Heat arrives, σ³² accumulates, the heat-shock program turns on as a coordinated wave. The bacterial solution to "respond to a new environment" is often "swap the reading head on the transcription machine."

Translation happens on a **70S ribosome** — the bacterial ribosome, assembled from a 30S small subunit and a 50S large subunit. Eukaryotic cytoplasmic ribosomes are 80S (40S + 60S). The subunit numbers do not add sensibly because sedimentation coefficients are not additive, but the naming convention persists, and what matters is that the structures are different enough at the molecular level for drugs to discriminate between them.

That discriminability is the pharmacological foundation of an entire class of antibiotics:

Aminoglycosides bind the 30S subunit and cause misreading of codons — the ribosome incorporates the wrong amino acid. Tetracyclines also target the 30S subunit, blocking the arrival of charged tRNAs. Chloramphenicol binds the 50S subunit at the peptidyl transferase center — the step where the new peptide bond forms. Macrolides (erythromycin, azithromycin) bind the 50S near the exit tunnel and physically block the growing peptide chain from leaving.

Every one of these drugs is selective because the bacterial ribosome differs from the host ribosome at exactly the binding site. The 70S is not a curiosity of bacterial cell biology. It is a clinical target — the structure four major antibiotic classes are designed to hit, and any mechanism that changes it, by mutation or by modification, is a candidate resistance mechanism.

<!-- → [TABLE: Ribosome-targeting antibiotics — columns for drug class, ribosome subunit targeted, specific mechanism, and one example drug — rows for aminoglycosides (30S, misreading), tetracyclines (30S, tRNA block), chloramphenicol (50S, peptidyl transferase), macrolides (50S, exit tunnel)] -->

---

## Horizontal gene transfer — the mechanism that actually runs the problem

Bacteria reproduce vertically, parent to offspring, the same way eukaryotes do. Variation accumulates by mutation, the way I just described. And if that were all bacteria did, antibiotic resistance would spread at roughly the rate of Darwinian evolution — slow enough that drug development could, in principle, stay ahead of it.

But bacteria also have something vertebrates do not: three routes for moving DNA *sideways*, between cells, often between unrelated species, sometimes in a single event. This is **horizontal gene transfer**, and it is the clearest explanation we have for why resistance spreads as fast as it does clinically. The KPC gene did not evolve fresh in each new *Klebsiella* isolate on six continents. It moved — on a plasmid, by a mechanism we can identify and trace.

There are three mechanisms. The differences between them have clinical consequences.

### Transformation — naked DNA, taken up from the environment

The simplest mechanism. A piece of DNA — released when a cell dies and lyses, free-floating in whatever environment the bacteria inhabit — gets taken up by a living cell and incorporated into its genome. No vector, no direct contact, no machinery beyond the recipient's own DNA-uptake apparatus.

A cell capable of this is called **competent**. Some species are naturally competent: *Streptococcus pneumoniae*, *Bacillus subtilis*, *Haemophilus influenzae*, *Neisseria gonorrhoeae*. Others can be made competent in the lab by chemical or electrical treatment. This is the mechanism behind Griffith's 1928 experiment — the one that, sixteen years later, let Avery, MacLeod, and McCarty identify DNA as the molecule of heredity.[^6] The "transforming principle" was literal: pieces of DNA from dead virulent pneumococci, taken up by living harmless ones, which then expressed virulence genes. The DNA was the information. The cell that absorbed it was transformed by it.

Transformation has constraints. The incoming DNA generally needs to find a region of sequence homology in the recipient chromosome to integrate stably. Plasmids that replicate autonomously can skip this, but chromosomal genes tend to move between related species where homology exists. *N. gonorrhoeae* is a notable exception — it takes up DNA from any source, with essentially no sequence preference, and its rapid evolution of resistance is partly a consequence.

### Transduction — phage as accidental courier

A bacteriophage normally packages its own genome into a protein capsid and injects it into a new host. Occasionally it makes a mistake: it packages a piece of the bacterial host's DNA instead. That aberrant particle carries bacterial DNA — potentially including resistance genes — into the next cell it infects.

This is **transduction**. Generalized transduction packages essentially random bacterial DNA. Specialized transduction, which occurs when a temperate prophage excises and occasionally takes flanking bacterial genes with it, moves only DNA near the phage's integration site.

The clinical constraint: phages are usually species-specific or genus-specific. A phage that infects *Staphylococcus aureus* will not ordinarily infect *E. coli*. So transduction tends to move genes between closely related bacteria. This is part of the story of MRSA — the methicillin-resistant *S. aureus* lineages are believed to have spread the *mecA* resistance gene partly through phage transduction between staphylococci. But it cannot account for inter-genus jumps. For that you need the third mechanism.

### Conjugation — the cell-to-cell connection, and the clinical headline

The most powerful HGT mechanism. Conjugation is direct DNA transfer from one bacterium to another through a physical connection, mediated by a **pilus** — a hollow protein tube that the donor cell extends, contacts the recipient, and through which one strand of the plasmid is pumped.

The steps: the donor carries a conjugative plasmid. The plasmid encodes a pilus, which extends and makes contact with a recipient cell. A pore forms between them. One strand of the plasmid is nicked, unwound, and transferred. Both cells synthesize the complementary strand. Both now have the plasmid. The recipient is now a donor. The cycle propagates.

The whole event takes minutes. In a dense population, a single conjugation event can become an epidemic of plasmid spread within hours.

What makes conjugation clinically catastrophic is what it moves and to whom. A conjugative plasmid carries many genes — multiple resistance mechanisms — and transfers the *whole plasmid as a unit*. One transfer event, three drug resistances, as a package. Not three separate evolutionary events. One. And conjugative plasmids are not fussy about species. R100 transfers between *E. coli*, *Klebsiella*, *Salmonella*, *Shigella*, *Proteus*, and *Pasteurella* — six genera. The narrow host range that limits transduction does not apply. A plasmid in a harmless gut commensal can end up, through a chain of conjugation events, in whatever pathogen happens to be sharing a patient's gut with it.

There is one further mechanism worth naming because it interacts with the others. **Transposons** are pieces of DNA that excise themselves from one location in a genome and insert at another — "jumping genes." Some carry cargo: resistance genes, virulence factors. A transposon can pick up a resistance gene from one plasmid and deposit it on another, rearranging the plasmid pool over time. The extended-spectrum β-lactamases — enzymes that destroy a broad range of penicillins and cephalosporins — are commonly transposon-borne. Transposon mobility within cells, combined with conjugative plasmid mobility between cells, is why ESBL resistance has spread across clinical settings as fast as it has.

<!-- → [TABLE: Three HGT mechanisms compared — columns for mechanism, DNA source, vector required, host-range breadth, clinical example — rows for transformation (free DNA, no vector, limited by homology, GC resistance in Neisseria), transduction (phage-borne DNA, phage vector, narrow/genus-specific, MRSA mecA spread), conjugation (plasmid, pilus, broad inter-genus, KPC plasmid spread)] -->

---

## Four ways resistance actually works

When a resistance gene arrives in a cell — by any of the three routes above — it has to do something to protect the cell. There are essentially four mechanisms, and most clinical resistance falls into one of them. Being able to name the mechanism from the phenotype is half of understanding what you're dealing with.

### Enzymatic inactivation

The bacterium produces a protein that chemically destroys or modifies the antibiotic before it can act. The canonical example is **β-lactamase** — an enzyme that hydrolyzes the strained four-membered ring at the core of penicillins, cephalosporins, and carbapenems. The ring strain is what makes the molecule reactive and pharmacologically active. Crack the ring, and you have an inert hydrolysis product. The mechanism of action — covalently binding penicillin-binding proteins to prevent cell-wall synthesis — requires an intact ring. There are now hundreds of β-lactamases with overlapping substrate ranges: penicillinases destroy penicillin; extended-spectrum β-lactamases (ESBLs) destroy most cephalosporins; carbapenemases like KPC destroy carbapenems. The same small protein, roughly 30 kilodaltons, has evolved to pick off drug class after drug class as each class was introduced.[^7]

Aminoglycosides have an equivalent. Aminoglycoside-modifying enzymes chemically tag the drug at specific positions, reducing its affinity for the ribosome. The drug is not destroyed — it is functionally inactivated by a small chemical addition.

### Target modification

The bacterium alters the molecular target of the drug, so the drug no longer binds with enough affinity to be lethal. **Erm methyltransferases** methylate a specific adenine in the 23S rRNA of the 50S ribosome — the binding site for macrolides. The methylated ribosome translates normally. The drug cannot grab its target. MRSA works similarly: the *mecA* gene encodes an alternative penicillin-binding protein (PBP2a) with very low affinity for β-lactams. The cell builds its wall using PBP2a. The drugs are present; they just cannot bind. Vancomycin resistance in enterococci is another example: the *vanA* cluster produces a cell-wall precursor terminating in D-Ala-D-lactate instead of D-Ala-D-Ala. A single hydroxyl-for-amine swap reduces vancomycin binding by about a thousand-fold. The keyhole has changed by one atom, and the key no longer fits.

### Efflux pumps

The bacterium produces a membrane protein that actively pumps the drug out, keeping intracellular concentrations below lethal threshold. The *tet*(A) gene encodes an inner-membrane antiporter that exchanges intracellular tetracycline for an extracellular proton. *Pseudomonas aeruginosa* carries multiple broad-spectrum efflux pumps (MexAB-OprM, MexXY-OprM) that export β-lactams, fluoroquinolones, aminoglycosides, and macrolides — a major reason *P. aeruginosa* is so reliably multidrug-resistant. A conceptual consequence: efflux resistance can sometimes be overwhelmed by raising the drug concentration. The pump has finite capacity. This is part of why higher-dose regimens occasionally restore activity against borderline-resistant strains.

### Reduced permeability

The bacterium reduces the rate at which the drug enters in the first place. Gram-negative bacteria bring most hydrophilic antibiotics through outer-membrane channels called **porins**. Mutations that reduce porin expression cut drug uptake. *Klebsiella* strains that are highly carbapenem-resistant often carry both a carbapenemase (enzymatic inactivation) *and* porin loss (reduced permeability). Either mechanism alone is sometimes beatable at clinical drug concentrations. The combination is not.

<!-- → [TABLE: Four resistance mechanism classes — columns for class, what the mechanism does, example gene or protein, drug classes affected, and the clinical tell that suggests this mechanism] -->

---

## How fast resistance fixes: the calculation worth doing

The argument that connects everything so far is quantitative, and worth running explicitly because it shows why clinical outcomes are not just a matter of choosing the right antibiotic.

Suppose a *Klebsiella* population in an ICU patient's gut contains 10⁸ cells. A conjugation event from a commensal donor has seeded the plasmid into 0.1% of them: starting frequency *p₀* = 0.001. Meropenem (a carbapenem) is started. Susceptible cells die. Resistant cells divide. Under strong selection the frequency dynamics follow approximately:

$$p_t = \frac{p_0 e^{st}}{1 - p_0 + p_0 e^{st}}$$

where *s* is the selection coefficient — the fitness advantage of a resistant cell relative to a susceptible one under drug pressure.

<!-- → [CHART: Logistic sweep curves — two panels side by side, same axes (x = generations 0–20, y = resistant fraction 0–1): left panel shows three curves for p₀ = 0.001, 0.01, 0.1 all with s=1, illustrating how starting frequency shifts the curve left or right but not its shape; right panel shows same p₀ = 0.001 with s = 0.5, 1.0, 1.5, illustrating how selection strength changes the steepness — student should see that once selection starts, fixation is rapid regardless of p₀] -->

With *s* = 1:

- After 5 generations: *p₅* ≈ 0.13 (13% resistant)
- After 10 generations: *p₁₀* ≈ 0.96 (96% resistant)
- After 15 generations: essentially fixed

*Klebsiella* can divide every 30 minutes under favorable conditions. In vivo it is slower, but the direction is the same. The resistant fraction goes from 0.1% to near 100% on a timescale of days. This is not a failure mode of the drug. It is the predictable outcome of selection acting on a pre-existing variant.

The calculation clarifies several things. First: the starting frequency *p₀* matters enormously in the early generations, but once selection is operating, the sweep is rapid regardless. The question is not "will resistance arise?" — it may already be there. The question is "what is its starting frequency, and have you applied the selection pressure that will drive it to fixation?"

Second: combination therapy works by a different logic. If resistance to drug A is at frequency 10⁻⁶ and resistance to drug B is at frequency 10⁻⁶, then *simultaneous* resistance to both — assuming the traits are independent — is at 10⁻¹². A population of 10⁸ cells almost certainly contains no double-resistant cells. Each drug alone has the starting frequency above its own fixation threshold. Together, neither does. This logic breaks when both resistances are pre-linked on a single mobile element — exactly what an MDR plasmid is. The implication: combination therapy is reliable only when the resistances are not already packaged together.

Third: antibiotic stewardship — using antibiotics only when necessary, at the right dose, for the minimum effective duration — works because selection cannot sweep a resistance allele that is not under selection pressure. Every unnecessary prescription is an opportunity for a plasmid to fix in a patient's microbiota and become transmissible.

---

## Two tools that came out of the same biology

Nearly every important tool of molecular biology was discovered in microorganisms and adapted as a reagent second. Two are worth pausing on because they appear throughout the rest of this book.

**PCR** — the polymerase chain reaction — amplifies a specific region of DNA exponentially. The idea is simple: denature the double helix (heat to 95°C), anneal short primers flanking the target region, extend them with a DNA polymerase (warm to 72°C), repeat. Thirty cycles gives about a billion-fold amplification of the target.[^8] The enabling ingredient was *Taq* polymerase, from *Thermus aquaticus*, a bacterium living in Yellowstone hot springs. Its polymerase is heat-stable enough to survive the 95°C denaturation step — so you load everything once and let a thermocycler run. Without a heat-stable polymerase from a hot-spring bacterium, discovered with no commercial application in mind, the PCR test you got for COVID would not exist.

**CRISPR-Cas** is a bacterial adaptive immune system. When a phage infects a CRISPR-carrying bacterium, the bacterium incorporates a short piece of the phage's DNA into a specialized chromosomal array. That sequence is the memory of the attack. On reinfection, the bacterium produces an RNA copy of the recorded sequence, which guides a Cas nuclease to cut DNA that matches it. The phage is destroyed.[^9] The Doudna-Charpentier insight was that by providing an artificial guide RNA, you can direct Cas9 to cut *any* sequence you specify. The first CRISPR-based human therapy was FDA-approved in 2023, about a decade from "this system can be programmed" to "we have used it on patients." That pace is unprecedented in gene therapy. But the biology is bacterial. The mechanism was not invented — it was discovered in bacteria that had been using it for hundreds of millions of years to fight phages.

---

## The honest picture

I want to name what the HGT story does and does not explain, because the chapter is not complete without it.

HGT through conjugation is the best account we have for how novel resistance genes — KPC, NDM-1, ESBLs — appear in clinical settings across continents on short timescales. No Darwinian mutation rate can account for the speed. The plasmid-transfer account can.

But much of antibiotic resistance in hospitals also spreads by **clonal expansion**: a single resistant strain proliferating and transmitting patient to patient. The CC258 *Klebsiella* lineage carrying KPC, the ST131 *E. coli* lineage carrying ESBLs, the dominant MRSA lineages — these are clonal success stories layered on top of the plasmid story. In many real outbreaks, both operate simultaneously. Genomic surveillance, which is becoming routine for MDR pathogens, can distinguish them: clonal spread shows near-identical core genomes; independent plasmid transfer shows core genomes that differ substantially while the plasmid sequence is conserved. Both signals appear in real data, often in the same patient cohort.

`[verify: current estimates of clonal vs. horizontal contribution to resistance spread for major MDR pathogens as of 2026]`

The picture that is accurate is: resistance genes move by HGT, and resistant lineages spread by clonal transmission, and both processes operate at once, and the relative balance varies by pathogen and setting. Any account that relies on only one mechanism is incomplete.

---

## Still puzzling

I do not fully understand why some conjugative plasmids transfer between six genera and others are restricted to a single species. The molecular determinants of host range — replication machinery compatibility, pilus-receptor specificity, restriction-modification evasion — are partially mapped, but no one can take a plasmid sequence and reliably predict which species it will conjugate into. That is a significant gap for anyone trying to model resistance spread.

I am also unsettled by how variable HGT rates are in natural microbial communities — orders of magnitude between similar-looking environments, with no satisfying predictive model. Some of the variation is ecological (cell density, antibiotic pressure, nutrient availability), but each variable explains only a fraction of the range. The field's models of HGT rate in the wild are still rough approximations.

---

## LLM Exercise — Building the HGT Simulator

**Project:** `07-hgt-simulator.html` — a horizontal gene transfer simulator.
**What you're building:** an interactive model of resistance spread through a bacterial population under HGT and antibiotic selection.
**Tool:** Claude Code (or your preferred coding LLM).

The simulator should let you choose a transfer mechanism (transformation / transduction / conjugation), pick a resistance gene (β-lactamase, tetracycline efflux, vancomycin target modification), set the starting population (default: 100 bacteria with 1 resistant), watch the population evolve over generations with HGT events drawn as connections between cells, and optionally challenge the population with an antibiotic — watching only resistant cells survive.

### Show

```
I'm building 07-hgt-simulator.html, a single-file interactive web visualization
of horizontal gene transfer and antibiotic selection in a bacterial population.

Specification:
- 100 bacteria as circles arranged in a 2D simulation area, each representing one cell.
- Each cell has a state: SENSITIVE (default) or RESISTANT (carries the resistance gene).
- Start: 99 sensitive (one color), 1 resistant (different color).
- User selects:
  (a) Transfer mechanism — radio buttons for "transformation," "transduction," "conjugation."
  (b) Resistance gene — radio buttons for "beta-lactamase," "tet efflux pump," "vanA cluster."
- Each generation, simulate HGT events appropriate to the chosen mechanism:
  - Transformation: random cells take up DNA from "dying" cells (draw a brief line from
    a randomly-chosen resistant cell to a randomly-chosen sensitive cell, with a small
    probability per generation of conversion).
  - Transduction: phage-mediated; only transfers to nearby cells of the same "species"
    (visualize as a small particle moving from resistant to sensitive, narrower spread radius).
  - Conjugation: pilus-mediated; resistant cells extend a brief line to neighboring sensitive
    cells; high transfer probability on contact.
- Animate transfer events as transient connections (lines or particles) between cells.
- Update a counter at the top showing total cells, % resistant, generation number.
- Optional "antibiotic challenge" button: applies selection, sensitive cells fade out
  (death animation), resistant cells remain and divide to repopulate the area.
- After repopulation, show new resistance fraction.

Use vanilla JavaScript and HTML5 canvas. Single file. No external dependencies.
```

### Say

Tell the LLM what kind of help you want. Examples:

- "Build the full simulator end-to-end."
- "I have the cell-rendering loop working; help me implement the conjugation mechanism with a pilus animation between cells."
- "The transformation mechanism is firing too fast — help me tune the per-generation probability so it's qualitatively slower than conjugation."

### Constrain

- Single HTML file, no external libraries.
- Each transfer mechanism must produce visibly different *patterns* of spread: transformation should look diffuse and random, transduction local and clustered, conjugation contact-mediated.
- The antibiotic challenge must be visually clean — sensitive cells fade out, resistant cells survive and repopulate.
- Don't fake the simulation by hard-coding a final resistance fraction. Compute it from the actual dynamics.

### Verify

Before accepting the LLM's code:

1. Read every transfer-event function. Does each mechanism actually behave qualitatively differently? If conjugation and transformation produce indistinguishable spread patterns, the simulation is wrong.
2. Set the resistant starting population to zero. Does resistance stay at zero, or does it spuriously grow?
3. Run with conjugation selected. Does resistance spread by contact between adjacent cells, or does it jump randomly?
4. Trigger the antibiotic challenge with a tiny resistant fraction — one or two cells. Do they survive and repopulate, or does the simulation crash?
5. Check the math on the resistance counter. Is it computed from actual cell states, or did the LLM hard-code a number?

### Explore

Once it's working:

- Change starting resistant fraction from 1/100 to 5/100. How does time to 50% resistance change?
- Switch from conjugation to transformation on the same starting population. Faster or slower to 50%?
- Apply the antibiotic before HGT has had time to spread. What is the population fate?
- Add a second resistance gene (tetracycline) with a different transfer rate. Can you produce a double-resistant population from two independent transfers?

### Extension to Chapter 8

In Chapter 8 we look at how to stop microbial growth — sterilization, disinfection, antimicrobial drugs in detail. Your simulator already has the most important dynamic: a resistant subpopulation fixed under selection. Carry it into Chapter 8 and add antibiotic stewardship as a mode: short courses, long courses, combination therapy. Which strategies slow resistance fixation, and which make it worse? Once you can compute the answer, the policy debate stops being a matter of opinion and starts being a matter of dynamics.

---

## Exercises

### Warm-up

1. **Supercoiling and its target.** Explain in your own words why bacterial DNA must be supercoiled to fit inside the cell, what enzyme maintains that supercoiling, and why fluoroquinolone antibiotics are selectively toxic to bacteria rather than to the human cells they inhabit. Your answer should name the bacterial enzyme, describe what the drug does to it, and explain the structural difference that gives the drug its selectivity.

2. **Sigma factors as a switch.** A bacterium growing at 37°C is suddenly shifted to 42°C. Describe what happens to its transcription program in the next few minutes. Name the sigma factor involved, the class of genes it activates, and explain why this is a more efficient regulatory strategy than changing the binding affinity of every heat-shock gene's promoter individually.

3. **Plasmid arithmetic.** The R plasmid R100 transfers between at least six bacterial genera and carries resistance to five drug classes simultaneously. Explain how a single conjugation event can convert a fully susceptible recipient into a five-drug-resistant donor — without any mutation. What does this tell you about the relationship between plasmids and the bacterial chromosome?

### Application

4. **Predict the HGT mechanism.** A clinical outbreak investigation finds that *Staphylococcus aureus* isolates from seven patients on the same ward all carry a new resistance gene. Whole-genome sequencing shows the core chromosomes are 98.5% identical — consistent with a single ancestral strain. A second investigation finds *Klebsiella pneumoniae* and *Enterobacter cloacae* isolates from patients in a different hospital also carrying the same resistance gene, but their core chromosomes differ by 12%. For each outbreak, state which HGT mechanism is most likely responsible, give your reasoning, and explain what genomic feature distinguishes the two scenarios.

5. **From phenotype to mechanism class.** A clinical lab reports the following: an *E. coli* isolate is resistant to ceftriaxone (third-generation cephalosporin) and aztreonam (monobactam) but remains susceptible to imipenem (carbapenem) and cefoxitin (a cephamycin). The resistance transfers by conjugation. Assign this to one of the four mechanism classes. Name the most likely gene family responsible. Predict what would happen if you added clavulanate (a β-lactamase inhibitor) to the ceftriaxone — would activity be restored? Explain your prediction.

6. **The stewardship calculation.** A hospital infectious disease team is debating whether to treat a patient's asymptomatic bacteriuria with an antibiotic. The causative organism is *E. coli* with a plasmid-borne resistance gene at estimated frequency 10⁻⁵ in the patient's gut microbiota. Using the selection dynamics framework from the chapter, explain quantitatively why treating an asymptomatic infection — one that does not require treatment — is likely to harm future patients, not just the individual being treated. What would need to be true about the selection coefficient *s* and the timescale of treatment for the risk to be negligible?

### Synthesis

7. **Combination therapy and its limits.** The chapter argues that combination therapy prevents resistance by making the probability of double resistance ≈ 10⁻¹². But this logic has an explicit failure condition. State what that condition is, give a real-world example of a mobile element that violates it, and explain what the existence of MDR plasmids implies for combination therapy design. What information about a pathogen's plasmid biology would you want before choosing a combination regimen?

8. **Tracing KPC across six continents.** Design a genomic surveillance study that would determine whether the global spread of KPC carbapenemase is best explained by (a) independent emergence through convergent mutation in multiple lineages, (b) clonal expansion of a single resistant strain, or (c) horizontal transfer of the KPC plasmid into locally distinct bacterial lineages. For each hypothesis, state the genomic pattern you would expect (what would the core genome phylogeny look like? what would the plasmid phylogeny look like?), and describe what finding would definitively rule out each one.

### Challenge

9. **Design an antibiotic that resists resistance.** You are asked to propose a design principle for a new antibiotic class that would be slower to acquire resistance than current β-lactams. The constraint: the drug must target a bacterial structure that is (a) essential for bacterial survival, (b) not present in human cells, and (c) difficult to modify without losing function. Name one candidate target, explain why modifications to it would be poorly tolerated by the bacterium, and predict which of the four resistance mechanism classes is least likely to work against your proposed target — and why. Your answer should draw on the structural logic of the four mechanisms discussed in this chapter.

---

## Tags

`microbial-genetics` `antibiotic-resistance` `horizontal-gene-transfer` `plasmids` `central-dogma`

---

**What would change my mind:** If high-resolution genomic surveillance consistently showed that clonal expansion of a small number of resistant lineages — rather than repeated plasmid transfer between strains — accounted for most clinical resistance in a given hospital or region, the relative emphasis on HGT vs. vertical spread would need to be revised toward clones. As of this writing, the data support both operating in parallel, with the balance varying by pathogen and setting.

**Still puzzling:** Why some conjugative plasmids have broad inter-genus host ranges while others are species-restricted — the molecular determinants are partially known but not predictive. And why HGT rates vary by orders of magnitude between similar-looking natural environments, with no satisfying mechanistic model of the variation.

---

[^1]: Yigit, H. et al. "Novel carbapenem-hydrolyzing β-lactamase, KPC-1, from a carbapenem-resistant strain of *Klebsiella pneumoniae*." *Antimicrobial Agents and Chemotherapy* 45, no. 4 (2001): 1151–1161. doi:10.1128/AAC.45.4.1151-1161.2001.
[^2]: Dame, R.T., Rashid, F.-Z.M., Grainger, D.C. "Chromosome organization in bacteria." *Nature Reviews Genetics* 21, no. 4 (2020): 227–242. doi:10.1038/s41576-019-0185-4.
[^3]: Watanabe, T. "Infective heredity of multiple drug resistance in bacteria." *Bacteriological Reviews* 27, no. 1 (1963): 87–115. doi:10.1128/br.27.1.87-115.1963.
[^6]: Griffith, F. "The significance of pneumococcal types." *Journal of Hygiene* 27, no. 2 (1928): 113–159. doi:10.1017/S0022172400031879.
[^7]: Bush, K., Bradford, P.A. "β-Lactams and β-lactamase inhibitors: an overview." *Cold Spring Harbor Perspectives in Medicine* 6, no. 8 (2016): a025247. doi:10.1101/cshperspect.a025247.
[^8]: Mullis, K.B. "The unusual origin of the polymerase chain reaction." *Scientific American* 262, no. 4 (1990): 56–65.
[^9]: Jinek, M. et al. "A programmable dual-RNA–guided DNA endonuclease in adaptive bacterial immunity." *Science* 337, no. 6096 (2012): 816–821. doi:10.1126/science.1225829.
