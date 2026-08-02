# Biology: Microbiology — CLI Video Ideas ("X with Claude")

## Candidate 01 — Simulate Bacterial Exponential Growth and the Doubling-Time Math with Claude
- Source: biology-microbiology/chapters/06-microbial-growth.md
- Lane: RESEARCH (Claude assistant)
- Hook: A four-hour phone call turned a safe pound of ground beef into a billion-cell hazard. The math behind that transformation is the same math behind septic shock — and it fits in one equation.
- The artifact: A Manim animation: two side-by-side growth curves (linear vs log scale), showing N = N0 × 2^n for ground beef scenario (N0=10, g=20 min, t=4 h → 41,000 cells/g) and blood-culture sepsis scenario (N0=100 CFU/mL, g=1 h, t=6 h → 6,400 CFU/mL). Animated point sweeping along the curve, with labeled milestones (1 hour, 4 hours, "septic shock threshold" annotated). Phase-curve panel showing the four standard growth phases (lag, exponential, stationary, death) as a segmented Manim curve.
- Prompt seed: `claude "Animate bacterial exponential growth in Manim. Scene 1: two panel plot. Left: N vs time (linear y-axis) for ground beef (N0=10 cells/g, g=20 min, 6h). Right: same on log10 y-axis. Animate a dot sweeping along both curves simultaneously. Annotate: 'After 4 h: ~41,000 cells/g'; 'After 6 h: ~2.6M cells/g'. Scene 2: blood culture sepsis scenario (N0=100 CFU/mL, g=1 h, 12h). Animate dot on log curve, annotate 'Septic shock threshold ~10^5 CFU/mL' as a horizontal dashed line. Scene 3: four-phase growth curve (lag, exponential, stationary, death) as a stylized Manim path with labeled regions. Verify: N at t=4h matches 10 × 2^12 ≈ 40960; N at t=6h matches 10 × 2^18 ≈ 2.6M."`
- Read / check: Verify the formula N = N0 × 2^(t/g) gives the annotated values; confirm log-scale curve is linear (hallmark of exponential growth); check that the four growth phases are in the correct order.
- Human supplies: Nothing — fully synthetic. Ground-beef and blood-culture scenarios are textbook worked examples using published doubling-time values.
- Output medium: Manim mp4.
- The change: Add a temperature slider (10 °C to 37 °C) that adjusts g (doubling time) based on a simplified Q10 relationship, showing that refrigeration at 4 °C would push g to ~4 h, making the 4-hour phone call safe.
- Teardown angle: The equation is not food-safety trivia. It is the same equation clinicians use to decide when a blood culture calls for immediate empiric antibiotics — before the organism is identified. The math of growth determines the math of treatment windows.
- Exclusions: Chemostat kinetics; quorum sensing; biofilm growth kinetics; exact Monod kinetics.
- Score: 10/10

---

## Candidate 02 — Research Antibiotic Resistance Mechanisms and the Selective Toxicity Ladder with Claude
- Source: biology-microbiology/chapters/09-antimicrobial-drugs.md
- Lane: RESEARCH (Claude assistant)
- Hook: Methicillin was designed specifically to defeat penicillin resistance. MRSA appeared two years after methicillin entered clinical use. Every antibiotic class has a clock on it.
- The artifact: A sourced synthesis document: a 5-row "selective toxicity ladder" table (target, drug class example, why bacteria-specific, best resistance mechanism, key organism), a timeline from Fleming 1929 → penicillin 1943 → MRSA 1961 → carbapenem resistance 2001, and a mechanistic explanation of three resistance strategies (drug destruction by beta-lactamase, target modification by mecA PBP2a, drug efflux by RND pumps) with one citable source for each.
- Prompt seed: `claude "Research antibiotic resistance mechanisms and selective toxicity. (1) Build a 5-row table: target (peptidoglycan / 70S ribosome / DNA gyrase / bacterial folate / ergosterol), drug class example, why target is bacteria-specific, dominant resistance mechanism, key resistant pathogen. (2) Explain the three main resistance strategies: enzymatic drug destruction (beta-lactamase), target modification (MRSA mecA/PBP2a), efflux pumps (RND family). For each, give a specific drug-organism pair and one citable source. (3) Why is the cell wall a 'gold-standard' target — what gives it the widest therapeutic window? (4) Build a timeline: Fleming penicillin effect 1929 → clinical use 1943 → methicillin 1959 → MRSA 1961 → KPC carbapenem resistance 2001 → global spread 2015."`
- Read / check: Verify that mitochondria are mentioned as the complication for 70S ribosome inhibitors; confirm PBP2a is described as a replacement target (not a destroyed enzyme); check that the timeline dates match the chapter's own chronology.
- Human supplies: Nothing — fully synthetic.
- Output medium: Slate (5-row table animated reveal; timeline as an animated horizontal bar; resistance mechanism diagrams as slate placeholders).
- The change: Extend the query to ask: if we discovered a new antibiotic targeting the unique bacterial lipid II flippase (MurJ), what resistance mechanisms would most likely emerge first — and what precedent (e.g., vancomycin vs VRE) informs that prediction?
- Teardown angle: Resistance does not evolve; it spreads. The gene existed before the drug. Selection reveals what was already there. Every new drug is a clock that starts the day it enters clinical use.
- Exclusions: Full pharmacokinetics; minimum inhibitory concentration determination methods; antiviral and antifungal mechanisms beyond the selective toxicity framing.
- Score: 9/10

---

## Candidate 03 — Research Koch's Postulates and Their Modern Failures with Claude
- Source: biology-microbiology/chapters/01-an-invisible-world.md
- Lane: RESEARCH (Claude assistant)
- Hook: Koch's postulates defined what it means to prove a germ causes a disease. HIV, Mycobacterium leprae, and SARS-CoV-2 each fail at least one postulate. What does that mean for the germ theory?
- The artifact: A sourced synthesis: Koch's four postulates stated precisely, a 4-column table (postulate, what it requires, which modern pathogen fails it, why), and a paragraph on molecular Koch's postulates (Falkow's revision) as the modern update. Four citable sources.
- Prompt seed: `claude "Research Koch's postulates and their modern limitations. (1) State Koch's four postulates precisely in modern language. (2) Build a 4-column table: Postulate number, What it requires, Modern pathogen that fails it, Mechanistic reason for failure. Include HIV (cannot be grown in pure culture from every patient; cannot be experimentally introduced into healthy volunteers), M. leprae (cannot be cultured in vitro), SARS-CoV-2 (animal models differ from human disease). (3) Explain Stanley Falkow's molecular Koch's postulates (1988) as the modern revision — what did Falkow add? (4) Does Koch's germ theory survive these revisions? Cite at least 4 sources including Falkow 1988 and one primary source on Koch's original work."`
- Read / check: Verify that HIV's culture limitation (requires living cells, not a simple medium) is correctly described; confirm that the molecular postulates add gene manipulation and virulence factor identification; check that the germ theory is described as surviving in revised, not refuted, form.
- Human supplies: Nothing — fully synthetic.
- Output medium: Slate (4-column table animated reveal; Falkow's molecular postulates as text card).
- The change: Extend the query to ask about the microbiome paradox — how do you apply Koch's postulates to a disease (obesity, IBD) where hundreds of species, not one, are implicated?
- Teardown angle: Koch's postulates are not a checklist to be filled; they are a logical structure for ruling out confounders. When the postulates fail, the failure reveals something about the biology — not a flaw in the framework. The revisions are the framework working.
- Exclusions: Full history of spontaneous generation debate; Pasteur's swan-neck flask in mechanistic detail; virology-specific Koch's modifications (Rivers' postulates).
- Score: 9/10

---

## Candidate 04 — Research Cholera Toxin Mechanism and the Seven-Step Infection Sequence with Claude
- Source: biology-microbiology/chapters/10-pathogenicity-disease.md
- Lane: RESEARCH (Claude assistant)
- Hook: Cholera toxin kills by turning the intestinal epithelium into a one-way pump. One protein, two subunits, one irreversible G-protein modification — and you lose a liter of fluid per hour. The mechanism is a graduate seminar in cell biology compressed into one toxin.
- The artifact: A sourced synthesis: the seven-step infection sequence table for Vibrio cholerae (exposure → adherence via TCP pili → colonization in small intestine → invasion absent → evasion via capsule absent but mucus penetration → damage via CT → systemic disease hypotension/hypovolemia → outcome), plus a mechanistic step-by-step of cholera toxin (B subunits bind GM1 ganglioside → A subunit cleaved → ADP-ribosylates Gs-alpha → adenylyl cyclase constitutively active → cAMP floods cell → CFTR opens → Cl- floods lumen → water follows → rice-water diarrhea). Four citable sources.
- Prompt seed: `claude "Research Vibrio cholerae pathogenesis with mechanistic detail. (1) Apply the seven-step infection sequence (exposure, adherence, colonization, invasion, evasion, damage, systemic disease) specifically to V. cholerae — for each step name the specific virulence factor or absence thereof. (2) Explain cholera toxin mechanism step by step: which subunit binds, which receptor, what ADP-ribosylation does to Gs-alpha, why cAMP accumulation causes Cl- efflux, and why water loss is so severe. (3) Why does V. cholerae require ~10^8 organisms as ID50 while Shigella requires ~10 — what does this imply about transmission? (4) Cite at least 4 primary or review sources including the original Finkelstein cholera toxin work."`
- Read / check: Verify that Gs-alpha ADP-ribosylation by the A subunit locks adenylyl cyclase ON (not the receptor); confirm the GM1 ganglioside receptor for the B subunit; check that the Cl-/H2O osmotic logic is correctly described.
- Human supplies: Nothing — fully synthetic.
- Output medium: Slate (step-by-step toxin mechanism as an animated cartoon-style reveal with text; seven-step table animated).
- The change: Extend the query to compare cholera toxin with E. coli heat-labile toxin (same mechanism) and pertussis toxin (same enzyme class, different G-protein substrate, opposite cAMP outcome) — showing that evolution has reused the ADP-ribosyl mechanism in different contexts.
- Teardown angle: The deepest insight is not "cholera kills by dehydration" — it is that the toxin works by commandeering a normal cell-signaling molecule (cAMP) and jamming it open. The pathogen doesn't break the machinery; it abuses the machinery. That is why the treatment is so simple: replace the water and salt.
- Exclusions: Snow's epidemiology and pump handle (covered in the invisible world chapter); full water-purification policy; cholera vaccine mechanisms.
- Score: 8/10

---

## Candidate 05 — Research Innate vs Adaptive Immunity: The Two-Layer Architecture with Claude
- Source: biology-microbiology/chapters/11-host-defenses.md
- Lane: RESEARCH (Claude assistant)
- Hook: A vaccinated person becomes immune to a disease they never had. The molecule that makes this possible is the same molecule that makes lupus and rheumatoid arthritis possible. The same machine that protects you can turn on you.
- The artifact: A sourced synthesis: a 2-layer table comparing innate vs adaptive (speed, specificity, memory, key cells, key molecules), the mechanism of toll-like receptor pattern recognition (with two specific examples: TLR4/LPS, TLR3/dsRNA), the MHC class I vs class II display pathway in one paragraph each, and a mechanistic explanation of why the smallpox vaccine worked (VV stimulates B cells → memory plasma cells → antibodies against Variola cross-reactive epitopes). Four citable sources.
- Prompt seed: `claude "Research the two-layer architecture of the human immune system. (1) Build a comparison table: Innate vs Adaptive — speed of response, specificity, memory, key cells (innate: neutrophils, macrophages, NK cells, dendritic cells; adaptive: T cells, B cells), key molecules (innate: TLRs, complement, cytokines; adaptive: BCR, TCR, MHC, antibody). (2) Explain TLR4/LPS signaling: what does TLR4 bind, what is LPS, what happens inside the macrophage? (3) Explain MHC class I vs class II: which cells display each, what peptides, which T cells recognize each, and what happens next? (4) Mechanistically explain why the smallpox vaccine (live vaccinia) produces protective immunity against smallpox. Cite at least 4 sources including Janeway's Immunobiology."`
- Read / check: Verify that TLR3 (not TLR4) binds dsRNA; confirm MHC class I presents endogenous/intracellular peptides to CD8 T cells and class II presents exogenous to CD4; check that the smallpox mechanism includes B cell memory and antibody cross-reactivity.
- Human supplies: Nothing — fully synthetic.
- Output medium: Slate (2-layer comparison table animated; MHC pathway diagram as slate for human to fill or Remotion schematic).
- The change: Extend the query to explain why HIV is not eradicable with the same vaccine logic as smallpox — specifically that HIV's mutation rate defeats memory-antibody cross-reactivity and that HIV directly infects and kills CD4 T cells (the very cells needed for adaptive immunity).
- Teardown angle: The two-layer architecture is a speed-specificity tradeoff. Innate acts in minutes but cannot distinguish E. coli from Salmonella. Adaptive acts in days but remembers every pathogen it has seen. The smallpox eradication story works because vaccinia is stable enough that antibodies raised against it stay cross-reactive to Variola for decades.
- Exclusions: Full B cell maturation and affinity maturation; complement cascade three pathways in mechanistic detail; T cell development in the thymus.
- Score: 8/10

---

## Candidate 06 — Research the Microbiome as a Defense System with Claude
- Source: biology-microbiology/chapters/11-host-defenses.md + chapters/01-an-invisible-world.md
- Lane: RESEARCH (Claude assistant)
- Hook: The best treatment for recurrent C. difficile infection — one that works in over 90% of cases — is transplanting someone else's stool. The microbiome is the immune system you can transplant.
- The artifact: A sourced synthesis: a mechanistic explanation of colonization resistance (the microbiome occupies every niche; broad-spectrum antibiotics remove the competition; C. difficile fills the vacuum), the fecal microbiota transplant (FMT) evidence base (one key RCT, success rate, mechanism), and a 3-column table of three other microbiome-disease associations (IBD, obesity, cancer immunotherapy response) with one source each. Four total citable sources.
- Prompt seed: `claude "Research the human gut microbiome as an innate defense system, focused on colonization resistance and C. difficile. (1) Explain colonization resistance mechanistically: how does normal flora prevent pathogen colonization, and what specific mechanisms does the microbiome use (nutrient competition, production of bacteriocins, bile acid metabolism, stimulation of IgA)? (2) Summarize the fecal microbiota transplant evidence for recurrent C. difficile: cite one RCT, give success rate, explain mechanistically how donor flora restores colonization resistance. (3) Build a 3-column table: Disease, Microbiome association, Mechanistic hypothesis — include IBD (dysbiosis), obesity (Firmicutes/Bacteroidetes ratio), cancer immunotherapy response (response correlates with baseline microbiome diversity). Cite at least 4 sources."`
- Read / check: Verify FMT success rate (~90% for recurrent CDI) is correctly cited; confirm bile acid metabolism is correctly described as one mechanism; check that all three microbiome-disease associations have a plausible mechanism, not just a correlation.
- Human supplies: Nothing — fully synthetic.
- Output medium: Slate (3-column table animated; FMT success rate as an animated bar vs conventional antibiotics).
- The change: Extend the query to ask what defines a "healthy" microbiome — is there a universal standard or is it population- and diet-specific? — and whether personalized microbiome-based diagnostics are clinically validated yet.
- Teardown angle: The microbiome is the oldest immune system — it predates the lymphocyte. It works not by killing pathogens but by ensuring there is no ecological room for them. FMT is the first microbiome-based therapy that works reproducibly, and it works by the same competitive-exclusion logic as the original.
- Exclusions: Probiotics and prebiotics market claims; microbiome sequencing methodology; germ-free mouse experimental evidence beyond what is needed to motivate the human clinical data.
- Score: 8/10

---

## Candidate 07 — Research Horizontal Gene Transfer and Antibiotic Resistance Spread with Claude
- Source: biology-microbiology/chapters/07-microbial-genome-genetics.md
- Lane: RESEARCH (Claude assistant)
- Hook: KPC-1 was a curiosity in a North Carolina hospital in 2001. By 2016 it was on six continents. Not because bacteria evolved the gene everywhere — because one plasmid carried it everywhere. Resistance does not evolve. It spreads.
- The artifact: A sourced synthesis: a 3-row table of horizontal gene transfer mechanisms (transformation, conjugation, transduction — source of DNA, requires physical contact?, notable pathogen example), the KPC timeline (2001 single isolate → 2015 six continents), the R100 plasmid as a case study of multi-drug resistance in one mobile element, and a comparison of vertical inheritance (slow, generational) vs horizontal transfer (instantaneous, species-crossing). Four citable sources.
- Prompt seed: `claude "Research horizontal gene transfer as the primary mechanism of antibiotic resistance spread. (1) Build a 3-row table: HGT mechanism (transformation, conjugation, transduction), source of DNA, requires direct contact, notable resistance example with organism. (2) Trace the KPC-1 carbapenem resistance gene: where/when was it first isolated, what plasmid type carries it, how did it spread globally by 2015? (3) Describe the R100 plasmid as a case study: what resistance genes does it carry, what is a conjugative plasmid, how is it transferred? (4) Compare Darwinian evolution by mutation (slow, requires many generations) vs HGT (instantaneous, crosses species boundaries) as mechanisms for resistance acquisition. Cite at least 4 primary or review sources."`
- Read / check: Verify transformation requires uptake of naked DNA (no direct contact); conjugation requires a conjugative pilus (direct contact); transduction uses a phage vector; confirm the KPC first isolation year and location (North Carolina, 2001); check that R100 is described as carrying at least 4–5 resistance determinants.
- Human supplies: Nothing — fully synthetic.
- Output medium: Slate (3-row table animated; KPC timeline as animated geographic spread map placeholder for human to fill).
- The change: Extend the query to ask what "resistome" means — the total reservoir of resistance genes in environmental bacteria — and what this implies for antibiotic development (you cannot design a drug for which resistance does not already exist in nature).
- Teardown angle: The distinction between resistance "evolving" and resistance "spreading" is not semantic. It is the difference between asking "how do we prevent mutations?" (impossible) and "how do we prevent plasmid transfer?" (partially tractable). Antibiotic stewardship is, at bottom, managing horizontal gene transfer ecology.
- Exclusions: Transposon mechanisms in detail; integron cassette structures; CRISPR-based phage resistance in bacteria; CRISPR-based resistance gene detection diagnostics.
- Score: 8/10

---

## Candidate 08 — Research the Virulence Factor Logic of E. coli O157:H7 with Claude
- Source: biology-microbiology/chapters/10-pathogenicity-disease.md
- Lane: RESEARCH (Claude assistant)
- Hook: The same E. coli living harmlessly in your gut right now became a lethal pathogen by acquiring a single prophage. One gene — Shiga toxin — shaved a single adenine off a ribosome in a kidney cell, and four children died in the 1993 Jack in the Box outbreak.
- The artifact: A sourced synthesis: the seven-step sequence for O157:H7 (exposure via undercooked beef, adherence via intimin, colonization in colon, no invasion, evasion by immune subversion, damage by Stx2 ribosome inactivation, HUS systemic disease), a molecular mechanism of Shiga toxin (B subunit binds Gb3 → A subunit cleaved → depurinates 28S rRNA → protein synthesis stops → cell dies), ID50 comparison (Shigella ~10 vs O157:H7 ~10-100 vs V. cholerae ~10^8), and the prophage origin of the Stx gene. Four citable sources.
- Prompt seed: `claude "Research E. coli O157:H7 as a case study in virulence factor biology. (1) Apply the seven-step infection sequence to O157:H7: name the specific virulence factor at each step (intimin for adherence, Shiga toxin Stx2 for damage, etc). (2) Explain Shiga toxin mechanism at the molecular level: B subunits, Gb3 receptor, endocytosis, A subunit cleavage, ribosome depurination, cell death. (3) Compare ID50 values: Shigella (~10), O157:H7 (~10-100), V. cholerae (~10^8) — what does this imply about transmission route and outbreak potential? (4) Explain the prophage origin of the stx gene — how did a normal E. coli become O157:H7, and what does this illustrate about pathogen emergence? Cite at least 4 sources including the 1993 Jack in the Box outbreak report."`
- Read / check: Verify Stx B subunit binds Gb3 (not GM1); confirm the ribosome depurination (removal of adenine from 28S rRNA) is correctly described; check that the prophage origin is stated as horizontal gene transfer.
- Human supplies: Nothing — fully synthetic.
- Output medium: Slate (7-step sequence table animated; Shiga toxin mechanism diagram as slate for human to fill or Remotion schematic).
- The change: Extend the query to compare Shiga toxin with diphtheria toxin (also an ADP-ribosyl transferase but targeting EF-2, not the ribosome directly) — showing that evolution has repeatedly discovered "disrupt the ribosome" as an effective cell-killing strategy.
- Teardown angle: O157:H7 demonstrates that a pathogen is not a species; it is a genetic configuration. The same species can be harmless or lethal depending on which mobile genetic elements it carries. Surveillance for E. coli is not enough — you need to know which E. coli.
- Exclusions: Full hemolytic uremic syndrome nephrology; Shiga toxin vs Shiga-like toxin nomenclature history; full outbreak epidemiology; policy implications of industrial meat processing.
- Score: 8/10

---

## Candidate 09 — Research Viral Evasion Strategies and Influenza Antigenic Variation with Claude
- Source: biology-microbiology/chapters/11-host-defenses.md + chapters/04-acellular-pathogens.md
- Lane: RESEARCH (Claude assistant)
- Hook: Influenza reinfects you every few years because it runs two escape strategies simultaneously — point mutations (antigenic drift) and wholesale gene-segment swaps (antigenic shift). The 1918 pandemic came from a shift. The 2009 swine flu came from a shift. Both look like "new" viruses because they are.
- The artifact: A sourced synthesis: a 2-column table (antigenic drift vs antigenic shift — mechanism, speed, example, pandemic potential), a mechanistic explanation of why influenza's segmented genome enables reassortment, the "original antigenic sin" phenomenon (why older antibodies misfire against new strains), and a case study of the 2009 H1N1 reassortant origin. Four citable sources.
- Prompt seed: `claude "Research influenza's immune evasion strategies of antigenic drift and shift. (1) Build a 2-column table: antigenic drift vs antigenic shift — molecular mechanism, rate of change, example strain, pandemic potential. (2) Explain why the segmented influenza genome specifically enables reassortment — what happens when two strains infect the same cell? (3) Explain 'original antigenic sin' (immunological imprinting): why do immune responses shaped by early childhood influenza infections sometimes misfire against novel strains? (4) Trace the 2009 H1N1 swine flu: which gene segments came from which animal reservoirs (human, swine, avian), and why did this constitute an antigenic shift? Cite at least 4 primary or review sources."`
- Read / check: Verify drift = RNA polymerase error-prone copying (point mutations); shift = reassortment of gene segments between two strains; confirm 2009 H1N1 had segments from human, North American swine, Eurasian swine, and avian lineages; check that "original antigenic sin" is correctly described as preferential boosting of memory over naive responses.
- Human supplies: Nothing — fully synthetic.
- Output medium: Slate (2-column table animated; 2009 H1N1 genome composition pie chart as Manim or slate).
- The change: Extend the query to compare influenza's segmented genome escape with HIV's single-genome escape (quasi-species error cloud, recombination) — showing that two viruses use different genomic architectures to achieve the same result: staying ahead of the immune system.
- Teardown angle: The flu vaccine fails not because the immune system fails — it fails because the target moved. Antigenic drift and shift are the pathogen's side of an evolutionary arms race in which the immune system has perfect memory of yesterday's virus and the virus has no memory at all — just variation and selection.
- Exclusions: Neuraminidase inhibitor pharmacology; mRNA flu vaccine development; influenza surveillance network operations; detailed hemagglutinin structure.
- Score: 7/10

---

## Candidate 10 — Research Herd Immunity Thresholds and Vaccine-Preventable Disease with Claude
- Source: biology-microbiology/chapters/11-host-defenses.md
- Lane: RESEARCH (Claude assistant)
- Hook: Smallpox was eradicated in 1977 — the last naturally acquired case was in Somalia. Measles nearly was, then vaccination rates dropped. The math of herd immunity has a threshold, and we crossed it in the wrong direction.
- The artifact: A sourced synthesis: the herd immunity threshold formula (p_c = 1 - 1/R0), a 3-row table (disease, R0, herd immunity threshold, current vaccination coverage, status), a mechanistic explanation of why herd immunity protects unvaccinated individuals through network effects, and a paragraph on why measles R0≈15 makes it one of the hardest diseases to eradicate. Four citable sources.
- Prompt seed: `claude "Research herd immunity thresholds and vaccine-preventable diseases. (1) State the herd immunity threshold formula p_c = 1 - 1/R0 and explain where it comes from (basic reproduction number definition, SIR model logic). (2) Build a 3-row table: Disease, R0 range, Herd immunity threshold %, approximate current global vaccination coverage, eradication status. Include measles (R0~12-18), polio (R0~5-7), smallpox (R0~5-7). (3) Explain mechanistically why high vaccination coverage protects unvaccinated individuals: what happens to transmission chains when most contacts are immune? (4) Why is measles R0~15 especially dangerous for elimination — what does this mean practically for required coverage? Cite at least 4 sources."`
- Read / check: Verify herd immunity threshold = 1 - 1/R0 formula is correctly applied (measles R0=15 → threshold ≈ 93%); confirm smallpox R0 and eradication status; check that the network-effect explanation is mechanistic (broken transmission chains), not just "collective protection."
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated bar chart showing R0 values and corresponding thresholds rising as a bar, with coverage percentage overlaid for comparison).
- The change: Add a sensitivity analysis: what happens to measles control if vaccination coverage drops from 95% to 85% — show how the effective reproduction number Re = R0 × (1 - p) rises above 1.0 and transmission restarts.
- Teardown angle: Herd immunity is not a property of individuals — it is a property of networks. The math only works if coverage is high enough to break every chain of transmission. The measles resurgences of the 2010s are a natural experiment in what happens when network coverage falls below the threshold.
- Exclusions: Full SIR model differential equations; vaccine adverse events epidemiology; cost-effectiveness of vaccination programs; herd immunity vs herd protection semantic debate.
- Score: 7/10
