# Chapter 14 — Antimicrobial Drugs

*Every antibiotic prescription is a small experiment in evolution.*

## The question before the answer

In 1928, Alexander Fleming returned from a vacation to find that one of his Petri dishes had been contaminated. A mold had grown on the plate, and around the mold, the bacteria he had been growing — *Staphylococcus aureus* — were dead. He recognized that the mold was producing something that killed the bacteria. He published the observation in 1929. He did not have the chemistry skills to purify the active compound. He did not develop it into a drug.

Twelve years later, Howard Florey and Ernst Chain at Oxford did the chemistry. They purified the active compound (which Fleming had named **penicillin**) and demonstrated that it cured experimental bacterial infections in mice. In 1941, they treated their first human patient, an Oxford constable named Albert Alexander who had a staphylococcal infection of the face. He improved dramatically. He died anyway, when they ran out of penicillin to give him. They had not yet figured out how to produce it at scale.

Industrial penicillin production was solved by 1943 — partly in the US, partly under wartime pressure — and the drug entered widespread clinical use. Bacterial infections that had been routine killers became routinely treatable. The bacterial pneumonia mortality rate dropped from 30% to about 5% within a decade.

Penicillin-resistant *Staphylococcus aureus* was reported in 1944. The first methicillin-resistant *S. aureus* (MRSA) was reported in 1960, a year after methicillin was introduced. Vancomycin-resistant *Enterococcus* was reported in 1986. Colistin-resistant bacteria, carrying a plasmid-borne resistance gene called mcr-1, were reported in 2015. Carbapenem-resistant Enterobacteriaceae now cause untreatable infections in hospitals across the world.

Every antibiotic in history has been followed within years by widespread resistance. We are losing the race. The point of this chapter is to understand the chemistry that makes antibiotics work, the biology that allows resistance to evolve, and the clinical practice that determines whether the few drugs we still have keep working.

## Learning objectives

By the end of this chapter, you will be able to:

1. Distinguish natural, semisynthetic, and synthetic antimicrobials and identify their typical mechanism categories.
2. Contrast bactericidal and bacteriostatic agents and explain when each is preferred.
3. Identify which antimicrobials target which cellular processes (cell wall, protein synthesis, nucleic acid synthesis, membrane, metabolic pathways).
4. Describe the four main mechanisms of acquired antibiotic resistance.
5. Read a Kirby-Bauer disk diffusion plate and interpret minimum inhibitory and minimum bactericidal concentrations.
6. Explain why antibiotic stewardship matters and what it looks like in practice.

Prerequisites: Chapters 1–13, especially Chapter 11.

## History, with names

Before Fleming, there was Paul Ehrlich, a German physician with a single radical idea: that there could be chemicals that bind selectively to a pathogen and kill it without harming the host. He called the concept the **magic bullet** — *Zauberkugel*. In 1909, with his collaborator Sahachiro Hata, Ehrlich identified Compound 606, later named **salvarsan** — an arsenic compound that cured syphilis. The first true chemotherapeutic agent for an infectious disease. The principle of selective toxicity, established as a working idea.

The 1930s brought **sulfa drugs**. Gerhard Domagk, working at I. G. Farben, found in 1932 that a red dye called Prontosil cured streptococcal infections in mice. Domagk's daughter Hildegard developed a streptococcal infection from a needle prick and was the first human treated. She lived. Sulfa drugs were the first broadly effective antimicrobials and dominated infectious disease therapy until penicillin became available. Domagk won the Nobel Prize in 1939, though Hitler forbade him from accepting it. [^1]

Penicillin in 1941. Streptomycin in 1944, by Selman Waksman and Albert Schatz, from a soil bacterium *Streptomyces griseus* — the first drug effective against tuberculosis. Chloramphenicol in 1947. Tetracycline in 1948. Erythromycin in 1952. Vancomycin in 1953. Most of these came from soil microbes — particularly *Streptomyces* species — which produce them as antimicrobial weapons against competitors. The pattern: bacteria evolved antibiotics to kill other bacteria, and humans noticed and packaged them.

The 1960s through 1980s saw the "golden age" of antibiotic discovery — semisynthetic derivatives of natural antibiotics, and entirely synthetic drugs (sulfonamides, fluoroquinolones, oxazolidinones). After about 1990, the discovery rate slowed dramatically. From 1962 to 2000, no new structural class of antibiotic reached the market for Gram-negative infections. The pipeline has been thin for thirty years.

## Three sources of antimicrobials

**Natural antibiotics** are produced by living organisms — mostly soil bacteria and fungi. Penicillin (from *Penicillium*). Streptomycin (from *Streptomyces*). Vancomycin (from *Amycolatopsis*). Most antibiotics in clinical use are either natural products or chemical modifications of them.

**Semisynthetic antibiotics** are natural products that have been chemically modified. The β-lactam antibiotics after penicillin (ampicillin, amoxicillin, methicillin, the cephalosporins, the carbapenems) are mostly semisynthetic — modifications of the basic penicillin scaffold to alter spectrum, stability, or pharmacokinetics.

**Synthetic antibiotics** are designed and built from scratch by medicinal chemistry. Sulfonamides. Fluoroquinolones. Linezolid. Trimethoprim. These do not occur in nature.

The distinction matters less than it once did — most modern antibiotic development blurs the lines. What matters is the mechanism.

## Bacteriostatic versus bactericidal

A **bactericidal** drug kills bacteria. A **bacteriostatic** drug stops them from growing but does not kill them; clearance depends on the host's immune system mopping up.

Examples: penicillins, cephalosporins, aminoglycosides, fluoroquinolones, vancomycin are bactericidal. Tetracyclines, erythromycin, chloramphenicol, sulfonamides are bacteriostatic.

The distinction matters clinically:

- For most infections in immunocompetent patients, bacteriostatic and bactericidal drugs are roughly equivalent — both will resolve the infection.
- For infections in immunocompromised patients, bactericidal drugs are preferred because the patient cannot rely on a robust immune response to finish the job.
- For infections in privileged sites with limited immune access (meningitis, endocarditis, prosthetic device infections), bactericidal drugs are strongly preferred and may be required.

The drug's classification can also depend on dose and organism. Many drugs are bacteriostatic at the typical clinical concentration but bactericidal at higher concentrations. The classification is a useful shorthand but is not always rigid.

## Spectrum

A **broad-spectrum** antibiotic acts against many different bacterial species. A **narrow-spectrum** antibiotic acts against a small number.

Broad-spectrum sounds better. It is not. Broader spectrum means killing more of the patient's normal microbiota along with the pathogen — disrupting gut flora, vaginal flora, skin flora, oral flora. The disruption opens niches for opportunistic pathogens that were being held in check.

**Superinfection** is what happens when broad-spectrum antibiotic use clears the normal flora and an opportunistic pathogen takes over. *Clostridioides difficile* infection of the colon is the most common example: broad-spectrum antibiotics knock back the gut anaerobes that compete with *C. difficile*, and the *C. difficile* — naturally resistant to many antibiotics, often picked up during a hospital stay — proliferates, producing toxins that cause severe colitis. *C. difficile* infections kill about 30,000 Americans per year. [^2] Most of those cases are downstream of antibiotic use.

This is one of the reasons antibiotic stewardship matters: use the narrowest-spectrum effective drug, for the shortest effective duration, with the right diagnosis to begin with. Broad-spectrum drugs are not free; they have ecological costs that show up in subsequent infections.

## Mechanisms — what antibiotics target

Antibiotics are selective because bacteria have features humans do not. The selectivity is never perfect — every drug has side effects — but it is what makes therapy possible at all.

The major bacterial targets:

### Cell wall

The bacterial cell wall contains peptidoglycan, which humans do not have (Chapter 7). Drugs that interfere with peptidoglycan synthesis are highly selective.

**β-Lactam antibiotics** — penicillins, cephalosporins, carbapenems, monobactams — all share a four-membered β-lactam ring. They bind to penicillin-binding proteins (PBPs), the enzymes that cross-link peptidoglycan strands. With PBPs inhibited, the cell wall cannot be properly assembled or repaired. As the bacterium grows and divides, it ruptures from internal turgor pressure.

↳ **Dig Deeper — The generations of cephalosporins**

*Cephalosporins are routinely described by "generation" (first through fifth). The generations are not random; they correspond to specific spectrum and resistance trade-offs.*

**Prompt:**
> Describe the five generations of cephalosporin antibiotics and what makes each generation distinct. For each generation, identify representative drugs, the spectrum of activity (Gram-positive vs Gram-negative coverage, CNS penetration, anti-pseudomonal activity, anti-MRSA activity), and the resistance considerations. Then explain why the generation framework, while useful as a teaching tool, oversimplifies the actual clinical decision-making.

**What to do with the output:** The cephalosporin generations are the most-asked piece of pharmacology in clinical infectious disease. Knowing them well is worth time. Save the answer for Chapter 25 (bloodstream infections).

β-Lactams are bactericidal but only against growing cells; cells that are not synthesizing new cell wall (stationary phase, persisters) are tolerant. β-Lactams are most effective against Gram-positives because Gram-negatives have an outer membrane that limits drug access.

**Vancomycin** binds directly to the D-Ala-D-Ala terminus of peptidoglycan precursors, preventing PBPs from cross-linking them. Active mainly against Gram-positives because it cannot cross the Gram-negative outer membrane. Vancomycin has historically been the "drug of last resort" for serious Gram-positive infections, including MRSA. Vancomycin-resistant *Enterococcus* (VRE) and vancomycin-resistant *S. aureus* (VRSA) have emerged.

**Bacitracin** interferes with cell wall precursor recycling. Topical use only; too toxic systemically.

### Protein synthesis

Bacterial ribosomes (70S) differ from eukaryotic ribosomes (80S). Drugs that bind selectively to 70S ribosomes block bacterial protein synthesis without affecting humans.

**Aminoglycosides** (gentamicin, tobramycin, amikacin, streptomycin) bind the 30S subunit and cause misreading of the mRNA. Bactericidal, broad-spectrum against Gram-negatives, but nephrotoxic and ototoxic. Reserved for serious infections.

**Tetracyclines** (tetracycline, doxycycline, minocycline) bind the 30S subunit and block tRNA binding. Bacteriostatic, broad-spectrum, used for *Chlamydia*, *Rickettsia*, Lyme disease, acne. Side effects include tooth discoloration (so avoided in children) and photosensitivity.

**Macrolides** (erythromycin, azithromycin, clarithromycin) bind the 50S subunit and block translocation. Bacteriostatic, broad-spectrum, used for respiratory infections, sexually transmitted infections, and atypical pathogens.

**Clindamycin** binds the 50S subunit. Anaerobic and Gram-positive coverage; associated with *C. difficile* colitis at significant rates.

**Chloramphenicol** binds the 50S subunit and inhibits peptidyl transferase. Bacteriostatic, broad-spectrum, but causes aplastic anemia in a fraction of patients — rare and unpredictable. Rarely used in the developed world; still used in resource-limited settings for typhoid and meningitis.

**Linezolid** binds the 50S subunit and prevents formation of the initiation complex. A newer class (oxazolidinones), one of the few completely synthetic antibiotic classes from the modern era. Used for resistant Gram-positive infections (MRSA, VRE).

### Nucleic acid synthesis

**Fluoroquinolones** (ciprofloxacin, levofloxacin, moxifloxacin) inhibit bacterial DNA gyrase and topoisomerase IV — enzymes that handle DNA supercoiling. Without functional gyrase, bacterial DNA cannot replicate. Bactericidal, broad-spectrum. Side effects include tendon rupture (rare but real), QT prolongation, neurological effects. The FDA has issued strong warnings about overuse for routine infections.

**Rifampin** inhibits bacterial RNA polymerase. Used in tuberculosis combination therapy and for meningococcal prophylaxis.

**Metronidazole** is activated by anaerobic metabolism to form DNA-damaging intermediates. Active only against anaerobes (and certain protozoa: *Trichomonas*, *Giardia*, *Entamoeba*).

### Membrane

**Polymyxins** (polymyxin B, colistin) disrupt the bacterial outer membrane by binding lipopolysaccharide. Active against Gram-negatives. Highly nephrotoxic; used only when nothing else works, against carbapenem-resistant *Enterobacteriaceae* and *Pseudomonas*. The 2015 discovery of mcr-1, a plasmid-borne colistin resistance gene now spreading globally, has made these drugs less reliable for last-resort use.

**Daptomycin** disrupts Gram-positive membranes by inserting into them, depolarizing the cell. Bactericidal against MRSA and VRE.

### Metabolic pathways

**Sulfonamides** inhibit dihydropteroate synthase, an enzyme in folic acid synthesis. Bacteria must make their own folate; humans get it from food. Selectivity is therefore good. Often used in combination with **trimethoprim**, which inhibits a different step in folate metabolism. The combination (TMP-SMX or co-trimoxazole, brand name Bactrim) is broadly used for urinary tract infections and *Pneumocystis* pneumonia.

**Isoniazid** inhibits mycolic acid synthesis — specific to mycobacteria. Cornerstone of TB therapy.

## Mechanisms of resistance

A bacterium can become resistant to an antibiotic by several mechanisms:

### Inactivating the drug

**β-lactamases** are enzymes that hydrolyze the β-lactam ring, destroying the drug. They are extremely common — most bacteria carry some β-lactamase activity. Different β-lactamases hydrolyze different β-lactams. Extended-spectrum β-lactamases (ESBLs) destroy most third-generation cephalosporins. Carbapenemases destroy carbapenems, formerly the last-resort drugs for ESBL-producers.

The arms race plays out here: every new β-lactam has been followed within a few years by a new β-lactamase that destroys it. β-Lactamase inhibitors (clavulanic acid, sulbactam, tazobactam, avibactam) are co-administered with β-lactams to protect them from β-lactamase, and these have themselves been countered by β-lactamases insensitive to the inhibitors.

↳ **Dig Deeper — The Ambler classification of β-lactamases**

*β-Lactamases are classified into four Ambler classes (A, B, C, D) by their structure. The classification predicts what they hydrolyze and how they're inhibited.*

**Prompt:**
> Describe the Ambler classification of β-lactamases. For each class, identify the catalytic mechanism (serine vs. metallo), example enzymes (TEM, SHV, CTX-M for class A; NDM, VIM, IMP for class B; AmpC for class C; OXA for class D), the substrate spectrum (which β-lactams the class hydrolyzes), and the inhibitor susceptibility (which class is blocked by clavulanic acid, by avibactam, etc.). End by discussing why metallo-β-lactamases (class B) are particularly concerning clinically.

**What to do with the output:** This is core clinical infectious disease pharmacology. The Ambler classes are how resistance is talked about in the literature; knowing them is essential for following antibiotic resistance updates.

**Aminoglycoside-modifying enzymes** acetylate, adenylate, or phosphorylate aminoglycosides at specific sites, destroying their activity. Different enzymes hit different drugs.

**Chloramphenicol acetyltransferase** acetylates chloramphenicol.

### Modifying the target

Mutations in the drug's binding target reduce drug binding without affecting target function.

**Penicillin-binding protein modifications** are how methicillin-resistant *S. aureus* (MRSA) resists β-lactams. MRSA has acquired the *mecA* gene, encoding PBP2a, a penicillin-binding protein with low affinity for most β-lactams. The bacterium can still synthesize its cell wall using PBP2a even when its native PBPs are inhibited.

**Ribosomal mutations** reduce binding of aminoglycosides, macrolides, or tetracyclines. Some are point mutations in rRNA; some are methylations of specific rRNA bases.

**Gyrase mutations** reduce fluoroquinolone binding. Common in *E. coli* resistant to ciprofloxacin.

### Reducing drug uptake or increasing efflux

**Porin loss** in Gram-negatives reduces the entry of hydrophilic drugs through the outer membrane. Carbapenem-resistant *Enterobacteriaceae* often combine carbapenemase production with porin loss.

**Efflux pumps** actively pump drugs out of the cell faster than they can accumulate. Many bacteria carry multidrug efflux pumps that handle several different antibiotic classes. The pumps are usually constitutively expressed at low levels and can be upregulated under selection.

### Bypassing the targeted pathway

**Alternative enzyme pathways** can bypass the inhibited step. Resistant bacteria sometimes acquire genes encoding alternative versions of the targeted enzyme that are insensitive to the drug.

For sulfonamides, some resistant bacteria acquire an alternative dihydropteroate synthase from a plasmid that has no affinity for the drug. For trimethoprim, similar story with dihydrofolate reductase.

## Routes of resistance acquisition

A bacterium can become resistant by **mutation** (chromosomal point mutations that change a target or enzyme) or by **horizontal gene transfer** (acquiring a resistance gene from another bacterium, often on a plasmid).

Mutation rates are low per cell per generation, but bacterial populations are large, and selection for mutants is strong when antibiotics are present. A single resistant mutant in a population of 10⁹ susceptible cells has a fitness advantage of essentially infinite when the antibiotic kills the susceptible ones.

Horizontal gene transfer is faster than waiting for mutations. Plasmids carrying resistance genes spread between bacteria in the gut, between bacteria in hospital environments, between bacteria in livestock and bacteria in humans. The same resistance gene shows up in multiple species, multiple plasmids, multiple geographic regions, because it has been moved around by HGT (Chapter 11).

Many resistance plasmids carry multiple resistance genes simultaneously. Selecting for resistance to one antibiotic by using it clinically can co-select for resistance to others that happen to be on the same plasmid. This is part of why broad-spectrum antibiotic use accelerates the spread of resistance against drugs the patient is not even receiving.

## Susceptibility testing

Before treating a serious infection with antibiotics, clinical labs typically test which drugs the bacterium is susceptible to.

**Disk diffusion (Kirby-Bauer)**: a standardized lawn of bacteria is grown on Mueller-Hinton agar. Paper disks impregnated with specific antibiotics at specific concentrations are placed on the plate. After overnight incubation, zones of clearing surround each disk. Zone diameter is compared to standardized cutoff values (CLSI or EUCAST guidelines) to classify the organism as susceptible (S), intermediate (I), or resistant (R) to each drug.

**Broth dilution** measures the **minimum inhibitory concentration (MIC)** — the lowest drug concentration that prevents visible growth in liquid culture. Doubling dilutions of the drug are tested. The MIC is reported in micrograms per milliliter. Lower MIC = more potent.

**MBC** (minimum bactericidal concentration) is the lowest concentration that kills 99.9% of the initial inoculum. Higher than MIC for bacteriostatic drugs; close to MIC for bactericidal drugs.

The clinical interpretation of MIC involves more than the absolute number. A drug with low MIC against an organism is not necessarily a good choice — the drug also has to reach therapeutic concentrations at the infection site, which depends on pharmacokinetics (absorption, distribution, metabolism, excretion). Some drugs have excellent MIC against *E. coli* but cannot penetrate the central nervous system, so they are useless for meningitis.

**E-test** (epsilometer test) is a hybrid: a plastic strip with a gradient of drug concentration placed on a bacterial lawn. The MIC is read from the point where the zone of inhibition intersects the strip.

For some organisms, **genotypic testing** is faster than phenotypic. PCR-based assays for *mecA* (MRSA), *vanA* (VRE), or specific β-lactamase genes can identify resistance within hours. The trade-off (as we discussed in Chapter 10) is that genotype and phenotype can disagree.

## Antibiotic stewardship

Antibiotic stewardship is the practice of using antibiotics responsibly:

- The right drug, narrow-spectrum when possible.
- The right dose, high enough to be effective.
- The right duration, no longer than necessary.
- The right indication, only when actually needed.

Hospital antibiotic stewardship programs include monitoring antibiotic use, reviewing prescriptions, providing prescribing guidance, and tracking resistance patterns. Hospitals with strong stewardship programs see lower rates of *C. difficile* infection, lower resistance rates, and equivalent or better patient outcomes.

The ecological argument: antibiotics are a shared resource. Using them effectively today means there are still some effective ones available tomorrow. Using them carelessly today accelerates the loss.

The clinical argument: many antibiotic prescriptions are unnecessary. Most upper respiratory infections are viral. Most sore throats are viral. Most sinusitis is viral. Antibiotics for these conditions provide no benefit and accelerate resistance. The CDC estimates that about 30% of outpatient antibiotic prescriptions in the US are unnecessary.

## New drug discovery

The pipeline of new antibiotics has been thin for decades. Pharmaceutical companies largely exited antibiotic development in the 1990s and 2000s because the economics are unfavorable: a new antibiotic is used briefly (a course of treatment) rather than chronically, is held in reserve to slow resistance, and may be obsolete within years of approval.

The pipeline has improved somewhat in the past decade through:

- **Public funding** (BARDA, CARB-X) supporting development of new agents.
- **Reuse of overlooked compounds** — drugs that were considered promising decades ago but never developed are being revisited.
- **Discovery from new sources** — bacteria that cannot be cultured in standard conditions are being grown using novel techniques. The iChip, developed by Slava Epstein and colleagues, allows growth of previously unculturable soil bacteria. **Teixobactin**, discovered using the iChip in 2015, is a new cell-wall-targeting antibiotic active against MRSA and other Gram-positives. [^3]

↳ **Dig Deeper — How AI is changing antibiotic discovery**

*Machine learning has been applied to the antibiotic discovery problem in the past five years. The most prominent result is halicin (2020), an antibiotic identified by AI from a chemical library.*

**Prompt:**
> Describe how machine learning is being applied to antibiotic discovery. Cover the Stokes et al. 2020 *Cell* paper on halicin, identified by training a deep neural network on antibiotic activity data and then screening compound libraries. What about abaucin (2023), the AI-discovered narrow-spectrum drug against *Acinetobacter baumannii*? What is the broader landscape of AI in antibiotic discovery, and what are the main limitations (training data quality, lab-to-clinic translation, novelty bias)? End by discussing whether AI is more likely to find truly new antibiotic classes or to find slightly different variants of existing ones.

**What to do with the output:** This is an active research area where the methods are changing fast. The pipeline still requires substantial bench validation; AI is not yet replacing experimental microbiology, but it is reshaping the early stages of discovery.
- **Engineering new mechanisms** — anti-virulence drugs that disarm pathogens without killing them, phage therapy, antimicrobial peptides, monoclonal antibodies against bacterial toxins.

None of these have yet produced an antibiotic that fundamentally changes the picture. The pace of resistance still outstrips the pace of discovery. The honest projection is that we will continue to lose drugs faster than we replace them for the foreseeable future, and that some clinical scenarios — pan-resistant *Pseudomonas*, untreatable *Acinetobacter*, post-antibiotic surgical recovery — will become more common.

## What the chapter is really about

An antibiotic is a tool that exploits a biochemical difference between bacterium and host. The tool works because the difference exists. The tool stops working when bacteria evolve to remove the difference, either by mutating the target, destroying the drug, pumping it out, or bypassing the pathway. The evolutionary distance from "drug works" to "drug doesn't" is much shorter than the medicinal-chemistry distance from "drug doesn't exist" to "drug exists." We can lose decades of work in a few years.

This is not a story with a heroic ending. It is a story with a difficult middle and an open future. The careful clinician, the careful pharmacist, the careful livestock manager, the careful patient — all of them affect the rate at which resistance spreads. The system requires cooperation across patients, prescribers, regulators, and industry, on a timescale that does not align well with any of their individual incentives.

For your training, I want you to carry one habit: when you read about an antibiotic, ask three questions. What does it target? What mechanism would let bacteria escape it? Has that escape already been observed in the literature? The answers will tell you both what the drug does today and how long it is likely to do it for.

## Still puzzling

I do not understand why some β-lactamases evolve so rapidly when others are evolutionarily stable. *Klebsiella pneumoniae* carbapenemase (KPC), first reported in 2001, now exists in dozens of clinically observed variants, each slightly different. The selection pressure (clinical use of carbapenems) is intense. The mutation rate is the usual bacterial rate. But the rate of new variant emergence seems higher than the model predicts. Some of it may be due to local hot spots in the gene, or to combinatorial recombination, but I have not seen a satisfying mechanistic account.

## What would change my mind

The narrative of "we are losing the race" against antibiotic resistance is widely accepted but rests partly on extrapolation. If new antibiotic discovery accelerates substantially in the next five years — through teixobactin-like discoveries from the uncultured majority, or through entirely new mechanisms not yet envisioned — the trajectory could change. As of this writing, the pipeline is improving but has not yet produced the next penicillin. `[verify: late-2020s status of WHO antibiotic pipeline and approved new mechanisms]`

## LLM exercises

1. **Drug-mechanism mapping.** Give the LLM eight antibiotics from different classes (penicillin, vancomycin, ciprofloxacin, gentamicin, doxycycline, sulfamethoxazole, metronidazole, linezolid). Ask it to identify each drug's target, the type of cells it works against, whether it is bactericidal or bacteriostatic, and one common side effect. Check against current references.
2. **Predicting resistance.** Ask the LLM to identify the mechanism most likely to produce clinical resistance to a hypothetical new antibiotic that inhibits a bacterial fatty-acid synthesis enzyme. Walk through the four resistance mechanism categories and rank by plausibility.
3. **Reading a Kirby-Bauer.** Describe a Kirby-Bauer plate result: an *E. coli* isolate shows large zones around ciprofloxacin and ampicillin, small zones around gentamicin and trimethoprim-sulfamethoxazole. Ask the LLM what antibiotic regimen would be appropriate for a UTI with this organism. Compare to standard clinical decision-making.
4. **Stewardship case.** A patient with a sore throat is prescribed amoxicillin. Ask the LLM whether this is appropriate, given that 80% of sore throats are viral. Walk through the decision logic: when is rapid strep testing indicated, when is empirical treatment justified, what are the costs of treating empirically versus not treating?
5. **A post-antibiotic future, modeled.** Ask the LLM to describe what a hospital looks like in a world where carbapenems no longer work. What procedures become more dangerous? What changes in clinical practice would be required? The exercise is to make the abstract loss concrete.

## References

[^1]: Otten, H. "Domagk and the development of the sulphonamides." *Journal of Antimicrobial Chemotherapy* 17, no. 6 (1986): 689–696. doi:10.1093/jac/17.6.689.
[^2]: CDC. "Clostridioides difficile (C. diff) Information for Healthcare Professionals." Updated 2024. https://www.cdc.gov/cdiff/clinicians/index.html
[^3]: Ling, L.L. et al. "A new antibiotic kills pathogens without detectable resistance." *Nature* 517, no. 7535 (2015): 455–459. doi:10.1038/nature14098.
---

## LLM Exercise — Chapter 14: Antimicrobial Drugs (Microbe Profile Database Project)

**Project:** Microbe Profile Database.
**What you're building this chapter:** antibiotic-treatment and resistance fields — the single most clinically-impactful addition.
**Tool:** **Cowork**.

---

**The Prompt:**

```
Chapter 14 of my Microbe Database project. Chapter 14 covered
antimicrobial drugs by class (cell wall — beta-lactams [penicillins,
cephalosporins, carbapenems], glycopeptides; protein synthesis —
aminoglycosides, tetracyclines, macrolides, oxazolidinones; nucleic
acid — fluoroquinolones, rifamycins; metabolic — sulfonamides;
membrane — polymyxins; antifungals — azoles, echinocandins;
antivirals — by mechanism); resistance mechanisms (enzymatic
degradation, efflux pumps, target modification, decreased
permeability); the AMR crisis.

Schema additions (this is the most important field expansion):
- **First_line_treatment**: standard treatment per current
  guidelines.
- **Alternative_treatments**: second-line options.
- **Resistance_mechanisms**: list (beta-lactamase, target
  modification, efflux pump, etc.).
- **Antibiotic_resistance_profile**: known resistance to specific
  drugs (e.g., MRSA → resistant to methicillin/nafcillin/oxacillin;
  MDR-TB → resistant to isoniazid + rifampin).
- **Reportable**: yes/no — is this a notifiable disease to public
  health (CDC, state)?

Backfill these for clinically-significant entries:
- *S. aureus*: cover both MSSA (cefazolin, nafcillin) and MRSA
  (vancomycin, daptomycin, linezolid). mecA is the resistance
  marker.
- *E. coli*: ESBL strains (ceftriaxone-resistant); CRE strains
  (carbapenem-resistant) emerging.
- *M. tuberculosis*: RIPE regimen (rifampin + isoniazid + pyrazinamide
  + ethambutol); MDR-TB and XDR-TB resistance patterns.
- *N. gonorrhoeae*: ceftriaxone-only currently recommended; rising
  resistance to that too.
- *C. difficile*: vancomycin (oral) or fidaxomicin; metronidazole
  no longer first-line for severe.
- *Candida albicans*: fluconazole; resistance increasing.
- *P. falciparum*: artemisinin combination therapy.
- HIV-1: combination antiretroviral therapy (cART) — typically
  3-drug regimen.

End with: query — "all organisms with multi-drug resistance in my
database." This list is your clinical attention list — the
organisms where empiric therapy may not work.
```

---

**What this produces:** Comprehensive antibiotic/treatment fields. Database becomes genuinely useful for clinical reasoning.

**Connection to previous chapters:** Ch 11 (HGT — how resistance spreads) + Ch 14 (specific resistance patterns) form the resistance-tracking spine.

**Preview of next chapter:** Chapter 15 covers pathogenicity mechanisms — virulence factors. Adds detailed virulence-factor fields.


---

## AI Wayback Machine

**Selman Waksman** was discovered streptomycin and coined "antibiotic" — pioneering the systematic search of soil microbes for antibacterial compounds.

**Run this:**

```
Who is Selman Waksman, and how does their work connect to antimicrobial drugs we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Selman Waksman"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Selman Waksman's ideas to a contemporary microbiology problem.
- Add a constraint: "Answer including criticisms or limits of Selman Waksman's framework."

What changes? What gets better? What gets worse?
