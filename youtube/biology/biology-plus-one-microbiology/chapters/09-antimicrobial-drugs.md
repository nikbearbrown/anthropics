# Chapter 9 — Antimicrobial Drugs

*Every antibiotic has a clock on it. The clock starts the day the drug enters clinical use. You can slow it down. You cannot stop it.*

---

Fleming reported penicillin's antibacterial effect in 1929. The drug entered widespread clinical use around 1943. Methicillin — a chemical modification of penicillin specifically designed to defeat the first wave of penicillin-destroying bacterial enzymes — was introduced in 1959. Methicillin-resistant *Staphylococcus aureus* was reported in 1961. Two years after the fix, the fix was broken.

That is the story of every antibiotic class we have ever deployed. Not the story of one unlucky drug. The story of all of them. And the reason is sitting inside the basic biology of how these drugs work — and how bacteria respond to selection pressure at a billion cells per milliliter.

This chapter walks through the major drug classes, one target at a time. The drugs are not the point. The pattern behind the drugs is the point.

---

## The frame: selective toxicity, made specific

In Chapter 3 we established the master observation: every useful antimicrobial drug works by attacking a structure the microbe has and you do not — and the therapeutic window is set by how structurally different the microbial target is from anything in the host.

I want to force that observation more specific before we use it for a dozen drug classes. *Selective toxicity* is a property of a *target*, not of a drug. Some targets give almost-free selectivity. Others give almost none. The differences that matter, listed from most to least exploitable:

**Peptidoglycan** — the bacterial cell wall polymer, assembled by enzymes called transpeptidases. There is no peptidoglycan in any human cell. No transpeptidase. Drugs that target peptidoglycan synthesis have the largest therapeutic windows in medicine.

**The 70S ribosome** — the bacterial protein-synthesis machine. Structurally different from the eukaryotic 80S ribosome in rRNA sequences, ribosomal proteins, and shape. Drugs that fit the 70S and not the 80S block bacterial translation while leaving yours alone — with one complication: your mitochondria still carry 70S ribosomes, because mitochondria are descended from a bacterium. Some 70S-targeting antibiotics have mitochondrial side effects. The selectivity is real, but it has edges.

**Bacterial DNA gyrase and topoisomerase IV** — enzymes that handle DNA supercoiling during replication. Humans have topoisomerases, but the bacterial enzymes have a different active-site geometry. Fluoroquinolones bind one and not the other — though the selectivity is less clean than for peptidoglycan drugs, which is why ciprofloxacin has more side effects than penicillin.

**Bacterial RNA polymerase** — different enough from eukaryotic RNA polymerases that rifampin can bind one and not the other.

**The bacterial folate synthesis pathway** — bacteria make folate from scratch. Humans cannot; we eat it. The pathway exists in the bug and is absent from you. Selectivity is excellent, because there is nothing in you for these drugs to hit.

**Ergosterol** — the dominant sterol in fungal cell membranes, analogous to cholesterol in yours. They differ by two methyl groups and a double bond. That small structural difference is where every antifungal drug lives — and because the difference is small, the selectivity is imperfect.

<!-- → [INFOGRAPHIC: Selective toxicity ladder — vertical axis from "widest window" (top) to "narrowest window" (bottom). Six rungs: (1) Peptidoglycan — "target absent from all human cells, window essentially infinite"; (2) Bacterial 70S ribosome — "different from 80S but shares mitochondrial ribosomes, some off-target effects"; (3) Bacterial folate synthesis — "pathway absent from humans, window wide"; (4) Bacterial gyrase/topo IV — "human topoisomerases present but structurally distinct, moderate selectivity"; (5) Ergosterol — "structural cousin of cholesterol, narrow window"; (6) Viral enzymes — "viruses use host enzymes, window very narrow." Each rung annotated with representative drug.] -->

There is a pattern here. Bacterial targets tend to be very different from anything in you, because bacteria and humans last shared a common ancestor several billion years ago. Fungal targets are less different — fungi are eukaryotes, in your kingdom, with membranes and ribosomes more like yours. Viral targets are worst of all: viruses use *your* enzymes for almost everything, and the few viral-specific proteins are small, variable, and hard to target without collateral damage. This structural logic explains the entire shape of the antimicrobial pharmacopoeia. We have many antibacterials, fewer antifungals, and very few antivirals. The selectivity story is the pharmacology story.

---

## Cell wall: the best target we have

The cell wall is the highest-leverage target in microbiology. Block its assembly while the bacterium is trying to grow, and the bug ruptures from its own internal osmotic pressure — several atmospheres against the surrounding medium. Without an intact wall, the cell swells and lyses.

**Beta-lactams** are the largest, most-prescribed antibiotic family. The chemistry is a four-membered nitrogen-containing ring — the beta-lactam ring — fused to a second ring. Different fusions and substituents give penicillins (penicillin G, amoxicillin), cephalosporins (cephalexin, ceftriaxone, ceftaroline), carbapenems (meropenem, ertapenem), and monobactams (aztreonam). They all share one mechanism.

The **penicillin-binding proteins** (PBPs) are bacterial enzymes that perform the final cross-linking step of peptidoglycan assembly — stitching adjacent sugar chains together through short peptide bridges. The beta-lactam ring is a structural mimic of the D-Ala-D-Ala dipeptide the enzyme normally grabs. The PBP grabs the drug instead, gets covalently trapped, and stops cross-linking. Wall assembly stops. The cell tries to grow, can't seal up, and lyses.

Two consequences fall out immediately. Beta-lactams are **bactericidal** — they kill, not merely inhibit — because wall failure is catastrophic in a growing cell. And they are bactericidal only against *growing* cells, because a cell not actively building wall is tolerant to them. A stationary-phase bacterium, a persister, a cell sitting dormant inside a biofilm — all are tolerant. The drug needs the bug to be in the act of growing.

**Vancomycin** attacks the same biology from a different angle. Rather than jamming the enzyme, it grabs the D-Ala-D-Ala substrate directly — physically blocking the cross-linking reaction before the PBP has a chance to attempt it. Same result: wall fails, bacterium lyses. One key consequence: vancomycin is too large to cross the Gram-negative outer membrane, so it is a **Gram-positive-only** drug. It cannot touch *E. coli*, *Klebsiella*, or *Pseudomonas*.

The MRSA case reveals the most important resistance mechanism for this entire class. MRSA does not destroy the drug. It acquires, by horizontal gene transfer, an *additional* PBP — called PBP2a, encoded by the *mecA* gene — with an active site too narrow for almost all beta-lactams to enter. When the normal PBPs are inhibited, PBP2a takes over wall-building. The wall gets made. The bug survives. This is resistance through target replacement, and it renders every conventional beta-lactam near-useless against MRSA.

Vancomycin resistance works differently again. *Enterococcus faecium* carrying the *vanA* gene cluster rewires its peptidoglycan precursor, replacing the D-Ala-D-Ala terminus with D-Ala-D-lactate. One nitrogen replaced by one oxygen. That single-atom substitution drops vancomycin binding affinity by roughly a thousand-fold. The cross-link forms anyway, because the bacterium has switched to a substrate the drug no longer recognizes.

<!-- → [IMAGE: Three-panel diagram of beta-lactam resistance mechanisms. Panel 1 "Susceptible": beta-lactam enters periplasm, binds PBP active site, wall cross-linking stops, cell lyses. Panel 2 "Beta-lactamase resistance": enzyme in periplasm hydrolyzes the beta-lactam ring before it reaches the PBP; drug is destroyed, wall assembly continues. Panel 3 "PBP2a resistance (MRSA)": beta-lactam binds normal PBP, but PBP2a (narrow active site) continues cross-linking; wall is built, cell survives. Caption: "Two different answers to the same drug — each requires a different clinical response."] -->

---

## Protein synthesis: fitting one ribosome and not the other

The 70S bacterial ribosome has two subunits. The **30S** subunit handles the decoding step — matching mRNA codon to tRNA anticodon. The **50S** subunit handles peptide-bond formation and translocation — moving the ribosome along the mRNA. Drugs that target each subunit block translation at different steps, with different consequences for whether the drug kills or only inhibits.

<!-- → [IMAGE: Bacterial 70S ribosome cross-section — 30S subunit (top, lighter color) and 50S subunit (bottom, darker). Drug binding sites annotated with colored arrows: aminoglycosides → 30S decoding site (red, labeled "misreading → bactericidal"); tetracyclines → 30S A-site (orange, labeled "tRNA entry blocked → bacteriostatic"); macrolides → 50S exit tunnel (green, labeled "translocation blocked → bacteriostatic"); chloramphenicol → 50S peptidyl transferase center (blue, labeled "peptide bond blocked → bacteriostatic"); linezolid → 50S initiation complex (purple, labeled "initiation blocked → bacteriostatic"). Caption: "One ribosome, five drug binding sites, four bacteriostatic and one bactericidal — and the mechanism explains why."] -->

**Aminoglycosides** (gentamicin, tobramycin, amikacin) bind the 30S subunit at the decoding site and cause misreading — the ribosome inserts the wrong amino acid. The bacterium accumulates garbled proteins, including broken membrane proteins that damage the cell envelope. That membrane damage is why aminoglycosides are **bactericidal**: it is not that protein synthesis stops, it is that the misread proteins are themselves destructive. Resistance: aminoglycoside-modifying enzymes that acetylate, adenylate, or phosphorylate the drug, preventing it from binding the ribosome.

**Tetracyclines** (doxycycline, minocycline) also bind the 30S subunit, but at a different site — they block the aminoacyl-tRNA from entering the A-site, so the ribosome stalls. Protein synthesis stops; existing proteins keep working. The cell doesn't die; it just stops growing. **Bacteriostatic.** Coverage of atypical pathogens — *Chlamydia*, *Rickettsia*, *Borrelia*, *Mycoplasma* — that beta-lactams cannot touch because those organisms lack peptidoglycan. Resistance: efflux pumps that actively expel the drug (tet genes) and ribosomal protection proteins that physically push it off the 30S.

On the **50S** subunit, three drug classes work at different steps of the translation cycle.

**Macrolides** (azithromycin, erythromycin, clarithromycin) block the exit tunnel and prevent translocation — the ribosome cannot advance along the mRNA. **Bacteriostatic.** Unusually important for community-acquired pneumonia because they cover *Mycoplasma pneumoniae* and *Legionella* where beta-lactams fail. Resistance: methylation of the 50S ribosomal RNA (erm genes) that prevents drug binding — and because the methylated site is shared across macrolides, one erm gene confers resistance to the entire class simultaneously.

**Chloramphenicol** inhibits the peptidyl transferase activity of the 50S — the actual step that forms the peptide bond. Bacteriostatic, broad-spectrum, and cheap. Used in resource-limited settings where it remains essential. Two side effects define its use: a dose-related, reversible bone marrow suppression, and a rare, idiopathic, irreversible aplastic anemia — a patient can take it uneventfully for years and then develop fatal aplasia unpredictably. The unpredictability is why it is rarely used in wealthy countries despite its pharmacological merits.

**Linezolid** prevents assembly of the ribosomal initiation complex — the ribosome cannot even begin translation. Bacteriostatic against most organisms, but clinically irreplaceable because it is active against MRSA and vancomycin-resistant *Enterococcus* (VRE), the two Gram-positive nightmares.

A pattern across the protein-synthesis drugs: almost all of them are bacteriostatic. The one exception is the aminoglycoside class, which is bactericidal because the misread proteins damage the cell membrane. The rule "block translation = bacteriostatic" almost always holds — and the exception tells you why: it is not the translation block that kills, it is what the garbled output does to the membrane.

---

## Nucleic acid synthesis: fluoroquinolones, rifampin, metronidazole

**Fluoroquinolones** (ciprofloxacin, levofloxacin) inhibit **DNA gyrase** and **topoisomerase IV** — the bacterial enzymes that manage supercoiling ahead of the replication fork and separation of daughter chromosomes after replication. Block both, replication forks collapse, double-strand breaks accumulate, the cell dies. **Bactericidal.** Excellent oral bioavailability. Resistance: point mutations in the *gyrA* and *parC* genes that reduce drug binding to each enzyme in turn. A single *gyrA* mutation cuts ciprofloxacin susceptibility substantially. A second mutation in *parC* finishes the job — and because both mutations can accumulate stepwise during a course of therapy in a patient with a large bacterial population, fluoroquinolones select for resistance faster than most antibiotic classes.

**Rifampin** inhibits the bacterial **RNA polymerase** β-subunit — physically blocking RNA chain elongation after the first few nucleotides. The catch: a single point mutation in *rpoB* (the β-subunit gene) confers high-level rifampin resistance immediately. This is why rifampin is *never* used alone for an active infection. In tuberculosis therapy, it is always combined with isoniazid, pyrazinamide, and ethambutol. Any *rpoB* mutant that arises under rifampin pressure gets killed by one of the other three drugs before it can take over. The combination is not a matter of covering more organisms; it is a matter of preventing resistance from emerging within the patient during the course.

**Metronidazole** exploits anaerobic metabolism. Inside an anaerobic bacterium, the drug is reduced to a reactive intermediate that breaks DNA. Aerobic bacteria do not reduce the drug, so they are unaffected. This is one of the clearest examples in pharmacology of mechanism defining spectrum: metronidazole works only where there is no oxygen to prevent the reduction. Anaerobic bacteria, and certain protozoa (*Trichomonas*, *Giardia*, *Entamoeba*), are susceptible. Everything aerobic is not.

---

## Membrane, metabolic, and antifungal drugs

**Polymyxins** (colistin, polymyxin B) are detergent-like cyclic peptides that bind the lipopolysaccharide of the Gram-negative outer membrane and disrupt it. Gram-positive-ineffective — they need the outer membrane to attack. Nephrotoxic and neurotoxic enough that they were largely abandoned in the 1970s, then resurrected in the 2000s when nothing else worked against carbapenem-resistant *Acinetobacter*, *Pseudomonas*, and *Klebsiella*. In 2015, the *mcr-1* gene — a plasmid-borne colistin resistance mechanism — was reported spreading globally. A horizontally transferable resistance gene against the drug of last resort. [verify: Liu et al., Lancet Infect Dis, 2016]

**Daptomycin** is a lipopeptide that inserts into the Gram-positive cell membrane in a calcium-dependent manner and depolarizes it — ions leak, membrane potential collapses, the cell dies. Bactericidal, Gram-positive only, active against both MRSA and VRE. One critical limitation: pulmonary surfactant inactivates it, so it cannot be used for pneumonia. The drug in the chapter-opening case — the drug that broke the fever when vancomycin was failing — is this one.

**The folate inhibitors** — sulfonamides and trimethoprim — target adjacent steps in the bacterial folate synthesis pathway. Bacteria make folate from scratch using dihydropteroate synthase (sulfonamides inhibit this) and dihydrofolate reductase (trimethoprim inhibits this). Humans eat folate; neither enzyme exists in us. Combined into **TMP-SMX** (trimethoprim-sulfamethoxazole), the two drugs hit the same pathway at two different points — resistance must defeat both targets simultaneously, which is harder than either alone.

Antifungals deserve a separate note. The toolbox is thin because fungi are eukaryotes.

**Polyenes** (amphotericin B) bind ergosterol in the fungal membrane and aggregate into pores that depolarize and kill the cell. We did this calculation in Chapter 3: ergosterol and cholesterol differ by two methyl groups and a double bond, amphotericin binds ergosterol roughly ten times more tightly than cholesterol, and that "roughly ten times" is not infinity — the drug damages kidneys at therapeutic doses because it binds your membrane sterol too, weakly.

**Azoles** (fluconazole, voriconazole) block ergosterol synthesis by inhibiting a fungal cytochrome P450 enzyme. Better tolerated than amphotericin, available orally, the standard for most *Candida* infections.

**Echinocandins** (caspofungin, micafungin) inhibit β-1,3-glucan synthase, the enzyme that builds the fungal cell wall. Fungi have a cell wall — chitin and glucan — that you do not. Selectivity here is genuinely good, which is why echinocandins have the widest therapeutic window of any antifungal class.

The antifungal toolbox is thin because fungal molecular machinery resembles yours. Every new target we find is a compromise. The bacterial toolbox is deep because bacterial molecular machinery is genuinely alien.

---

## Bactericidal versus bacteriostatic: what the distinction actually does

This distinction gets stated as if it settles clinical practice. It does not, and the ways it misleads are worth naming.

A **bactericidal** drug kills bacteria — drops the viable count by 99.9% or more at clinically achievable concentrations. Beta-lactams, vancomycin, aminoglycosides, fluoroquinolones, daptomycin, metronidazole.

A **bacteriostatic** drug stops bacteria from growing without killing them. The immune system handles the mop-up. Tetracyclines, macrolides, chloramphenicol, linezolid, sulfonamides, trimethoprim.

The clinical intuition that "bactericidal is always better" is mostly wrong. For most infections in immunocompetent patients, bactericidal and bacteriostatic drugs produce equivalent outcomes in head-to-head trials — the immune system mops up reliably. The places the distinction genuinely matters are **immunocompromised patients** (where the immune system cannot be trusted to finish the job), **infections in immune-privileged sites** (endocarditis on a heart valve, meningitis behind the blood-brain barrier, prosthetic joint infections), and specific organism-drug combinations where killing speed predicts mortality. In those settings, bactericidal drugs are preferred, sometimes required. In most other settings, the distinction is a teaching shorthand.

<!-- → [TABLE: Bactericidal vs. bacteriostatic — when it matters. Columns: clinical scenario, bactericidal required?, why. Rows: (1) Outpatient community UTI in healthy adult / No / immune system handles mop-up; (2) Bacterial endocarditis on a native valve / Yes / poor blood supply, immune cells excluded from vegetation; (3) Gram-positive bacteremia in neutropenic patient / Yes / no immune backup; (4) Atypical pneumonia in immunocompetent adult / No / doxycycline or azithromycin equally effective; (5) MRSA prosthetic joint infection / Yes / biofilm + immune-privileged site + slow-growing cells. Caption: "The distinction matters in exactly these contexts. Outside them, it is a classification, not a prescription."] -->

Two additional caveats. The classification is organism-dependent: linezolid is bacteriostatic against most organisms but bactericidal against streptococci. And it is dose-dependent: many bacteriostatic drugs become bactericidal at concentrations above the clinical range. The shorthand is useful. The shorthand is not the answer.

---

## Worked example — the beta-lactam arms race

Pick one drug. Watch the mechanism. Watch the resistance. Watch the counter-resistance. Watch what happens next.

**Round 1: penicillin G.** A natural product from *Penicillium*, the beta-lactam ring is a structural mimic of D-Ala-D-Ala. The transpeptidase of *S. aureus* grabs it, gets covalently trapped, stops cross-linking. Wall fails. Cell lyses.

**Round 2: penicillinase.** *S. aureus* acquires a gene encoding a serine beta-lactamase — an enzyme that grabs the beta-lactam ring and hydrolyzes it open before it reaches the PBP. One beta-lactamase molecule destroys many drug molecules per second. By 1944, four years after penicillin entered clinical use, penicillin-resistant *S. aureus* was appearing in hospitals. By the early 1960s, the majority of clinical isolates carried penicillinase.

**Round 3: methicillin.** Chemists add bulky side chains around the beta-lactam ring — large enough that the beta-lactamase cannot fit the drug into its active site. The PBP, with its more open architecture, still binds the drug. Penicillinase-resistant penicillins (methicillin, nafcillin, oxacillin) introduced in 1959.

**Round 4: PBP2a.** *S. aureus* acquires an additional PBP — PBP2a, encoded by *mecA* — with an active site too narrow for almost all beta-lactams. When native PBPs are inhibited, PBP2a builds the wall. MRSA reported in 1961. Two years after the fix.

**Round 5: beta-lactamase inhibitors.** Combine a beta-lactam antibiotic with a second molecule that is a suicide substrate for beta-lactamases — it occupies the enzyme, gets stuck, and the real drug passes safely. Clavulanic acid, sulbactam, tazobactam. Amoxicillin-clavulanate (Augmentin), piperacillin-tazobactam (Zosyn).

**Round 6: ESBLs and carbapenemases.** Bacteria evolve beta-lactamases with expanded active sites that hydrolyze third-generation cephalosporins (extended-spectrum beta-lactamases, CTX-M family). Then carbapenemases — enzymes that hydrolyze carbapenems, the drugs being held in reserve. Some are serine carbapenemases (KPC). Some are metallo-beta-lactamases (NDM, VIM, IMP) with zinc ions in their active sites; these are not inhibited by clavulanate or tazobactam at all.

**Round 7: newer inhibitors.** Avibactam, vaborbactam, relebactam — inhibitors with coverage of serine carbapenemases. Combinations like ceftazidime-avibactam. Work against KPC. Do not work against NDM.

**Round 8: the metallo gap.** NDM-type carbapenemases remain largely uninhibitable by current clinical agents. New metallo-inhibitors are in development.

<!-- → [CHART: Beta-lactam arms race timeline — x-axis: years 1940–2025. Two lines: upper line "drug introduced" (dots at penicillin G 1943, methicillin 1959, cephalosporins 1964, carbapenems 1985, beta-lactamase inhibitor combinations 1984, ceftazidime-avibactam 2015), lower line "resistance reported" (dots at penicillinase 1944, MRSA 1961, ESBL 1983, KPC 2001, NDM 2008, mcr-1 2015). Gap between the two lines: narrow and getting narrower. Callout: "Resistance now outruns discovery."] -->

Pause here and look at the timeline. The first penicillin resistance appeared four years after clinical introduction. Methicillin resistance appeared two years after introduction. By the time we reached the carbapenem era, resistance was emerging within months to years of clinical deployment for some organisms.

The asymmetry is structural. A pharmaceutical company designs one molecule at a time, in a lab, with budgets and regulatory timelines measured in years to decades. A bacterial population being treated in an ICU generates billions of mutation events per day and enriches any variant that survives. The evolution does not need to be clever. It just needs to be cheap and continuous. It is both.

There is one counterpoint worth stating honestly. Some resistance mechanisms carry a **fitness cost** — the resistant variant grows slower than the susceptible parent in the absence of drug pressure, and susceptibility can recover if drug use is restricted. If a resistance mechanism is costly, stewardship helps. If it is not costly, restriction does not bring susceptibility back. Methicillin resistance in *S. aureus* has very low fitness cost — MRSA persists in hospitals and communities regardless of local antibiotic pressure. KPC carbapenemase in *Klebsiella* also appears to have low fitness cost in the strains where it is most clinically problematic. This is why antibiotic stewardship alone cannot solve the resistance crisis — it is necessary but not sufficient.

---

## The clock, and what slows it

Everything in this chapter follows from one observation: every antibiotic difference we exploit is a difference evolution can erase. The therapeutic window is set by structural distance between the microbial target and anything in the host; the duration of effectiveness is set by how long it takes bacterial evolution to find a work-around. Those are two independent variables, and both have to be favorable for a drug to remain useful for decades.

**Stewardship** is what slows the clock. Four principles:

Use the *narrowest effective spectrum*. A broad-spectrum drug hits more of the patient's own microbiota along with the pathogen — disrupting gut flora, vaginal flora, skin flora. *Clostridioides difficile* colitis is the canonical downstream consequence: broad-spectrum antibiotics knock back the anaerobic flora that keeps *C. diff* in check, and *C. diff* — naturally resistant to many of those same antibiotics — takes over the colon. Tens of thousands of deaths per year in the United States, most of them downstream of antibiotic use. [verify: CDC C. difficile estimates]

Use the *right dose*. Sub-therapeutic dosing gives resistance the best possible environment: drug present, selective pressure operating, but low enough that partially resistant mutants can survive and be enriched.

Use the *right duration*. Premature discontinuation selects for the small subpopulation of less-susceptible bacteria that survived the early part of the course. But treating longer than necessary is also harmful — more collateral damage to the microbiome, more resistance selection. The right duration is the one the evidence supports for this specific infection, which is often shorter than tradition.

Use only when the infection *requires* it. The largest driver of antibiotic resistance is antibiotic use for viral respiratory infections that antibiotics cannot treat. Not malpractice — reflex prescribing in response to patient expectation. The drugs we use on viral infections select resistance in the bacteria riding along in the same patient and household.

<!-- → [INFOGRAPHIC: Four stewardship levers and what each one does to the clock. Four rows: (1) Narrowest effective spectrum → "fewer off-target bacteria selected, microbiome disruption reduced"; (2) Right dose → "sub-therapeutic dosing enriches partially resistant mutants — avoid"; (3) Right duration → "too short selects survivors; too long increases collateral damage — match evidence"; (4) Right indication → "viral infections don't respond; resistance pressure is paid anyway — avoid". Each row has a one-sentence consequence of getting it wrong. Callout: "All four levers slow the clock. None of them stops it."] -->

The clock cannot be stopped. But a drug introduced thoughtfully, reserved for cases that require it, given at the right dose for the right duration — that drug's clinical life is measurably longer than one deployed promiscuously. Penicillin, used conservatively for penicillin-susceptible infections, is still useful. The drugs that lose utility fastest are the broad-spectrum agents used by reflex. That is not a coincidence.

---

## LLM Exercises — Show / Say / Constrain / Verify

**1. Drug-mechanism mapping.**

> *Show* the model this list: penicillin G, vancomycin, gentamicin, doxycycline, azithromycin, chloramphenicol, ciprofloxacin, rifampin, daptomycin, trimethoprim-sulfamethoxazole.
>
> *Say:* "For each drug, identify (a) the bacterial structure or pathway targeted, (b) bactericidal or bacteriostatic and why, (c) spectrum, (d) most common acquired resistance mechanism. Return as a table."
>
> *Constrain:* "Cite a primary or canonical reference for each row. If uncertain, say so explicitly — do not guess."
>
> *Verify:* For three randomly chosen rows, pull the FDA package insert or a current infectious disease reference (*Mandell, Douglas, and Bennett's*) and check the answer. Note any drift between the model's output and the primary source.

**2. Resistance prediction.**

> *Show* the model this description: "A new antibiotic targets a bacterial enzyme essential for cell-membrane lipid synthesis. The enzyme exists in all bacteria and not in humans. The drug is bactericidal, narrow-spectrum (Gram-positive only), MIC 0.25 µg/mL against MRSA and VRE."
>
> *Say:* "Predict the most likely resistance mechanism that will emerge in clinical use. Justify by analogy to the four mechanism categories: drug inactivation, target modification, reduced uptake or efflux, pathway bypass."
>
> *Constrain:* "Limit to mechanisms with a published precedent in another antibiotic class. Cite the precedent."
>
> *Verify:* Compare predictions against published reports for structurally adjacent drugs (daptomycin, lipid A inhibitors). Does the model's reasoning generalize, or is it pattern-matching on surface features?

**3. Stewardship case.**

> *Show* the model: "A 28-year-old presents to urgent care with three days of sore throat, mild fever, and cough. No exudate, no anterior cervical lymphadenopathy, no recent strep exposure. Patient is asking for amoxicillin because 'it always helps.'"
>
> *Say:* "Walk through the Centor criteria, the role of rapid antigen testing, and the antibiotic decision. Argue for a specific course of action and identify the evidence base."
>
> *Constrain:* "Quote the current IDSA guideline language verbatim where it applies and provide the citation."
>
> *Verify:* Pull the actual IDSA guideline. [verify: most recent IDSA group A strep guideline] Confirm whether the quotation is accurate and whether the management recommendation matches the standard of care. Note any wording the model invented.

**4. Bridge to Chapter 10.**

> *Show* the model this chapter's summary.
>
> *Say:* "Chapter 10 covers virulence mechanisms — adherence, invasion, immune evasion, toxin production. Generate five specific predictions for which virulence mechanisms a clinical MRSA isolate is likely to deploy, based on the organism and the chapter just covered."
>
> *Constrain:* "Each prediction must name a specific virulence factor (Panton-Valentine leukocidin, alpha-hemolysin, protein A, staphyloxanthin, biofilm) with a one-sentence mechanism. No more than five."
>
> *Verify:* When Chapter 10 is available, check which predictions are confirmed, which are partly right, and which are wrong. Use the misses as a guide to what about Gram-positive virulence is not yet intuitive to you.

---

**What would change my mind.** If a new antibiotic class with a genuinely novel target — not a modification of an existing scaffold — enters widespread clinical use in the next decade and shows a substantially longer pre-resistance interval than the historical pattern, the chapter's framing of an unwinnable arms race will need revising. Teixobactin and AI-discovered scaffolds (halicin, abaucin) are candidates. [verify: 2025–2026 clinical status of teixobactin/halicin/abaucin] As of writing, none has shifted the resistance trajectory at the population level.

**Still puzzling.** I do not understand why so few structurally novel antibiotic classes have emerged since 1980 — whether the natural-products library was substantially exhausted by the first generation of screens, whether the economics of clinical development broke and the discovery problem is downstream of that, or whether the easy selective-toxicity differences are mostly known and the remaining ones come with inherent trade-offs we have not yet learned to engineer around. The historical pattern looks both biological and economic. I cannot yet read which force is dominant.

---

*The drugs in this chapter work on pathogens that are, in some sense, just sitting there to be killed. Chapter 10 looks at what the pathogen is actually doing while we are trying to kill it — how it adheres, invades, evades the immune response, and produces the toxins that make it dangerous. Pharmacology assumed a stationary target. Pathogenesis describes a moving one.*

---

## Exercises

### Warm-up

**1.** For each drug, name (a) the bacterial structure or pathway targeted and (b) whether it is bactericidal or bacteriostatic — and give the one-sentence mechanistic reason why: penicillin G, vancomycin, gentamicin, doxycycline, azithromycin, ciprofloxacin, rifampin, daptomycin, TMP-SMX, metronidazole. *(Tests: drug-target mapping across all major classes.)*

**2.** Why is vancomycin useless against *E. coli*, and why is metronidazole useless against *Streptococcus pyogenes*? Give a structural or mechanistic reason for each — not a list, an argument. *(Tests: spectrum follows from mechanism, not from memorization.)*

**3.** A clinical report returns: "*Klebsiella pneumoniae*, meropenem MIC 32 µg/mL, KPC-positive." Translate this into plain English: what does each piece of information mean, and what does it imply for empirical therapy of a serious infection caused by this isolate? *(Tests: MIC interpretation, carbapenem resistance, clinical reasoning.)*

### Application

**4.** A previously healthy adult presents with leg cellulitis — no pus, no abscess, no recent hospitalization, no prior antibiotics. The two most likely organisms are *Streptococcus pyogenes* and methicillin-susceptible *S. aureus*. Pick a narrow-spectrum drug and explain why you would not use a broader one. Now change the case: the patient has a fluctuant abscess, was hospitalized two months ago, and has had three antibiotic courses in the past year. What changes about your drug choice and why? *(Tests: stewardship reasoning, spectrum selection, MRSA risk stratification.)*

**5.** A clinical *E. coli* isolate carries a CTX-M-15 ESBL and is reported resistant to ceftriaxone, cefepime, ceftazidime, ampicillin, amoxicillin-clavulanate, piperacillin-tazobactam, ciprofloxacin, and TMP-SMX. The ESBL accounts for the beta-lactam resistance. Propose a mechanism for the co-resistance to ciprofloxacin and TMP-SMX, explain why these resistances travel together on clinical isolates, and name the drug class that retains activity and why. *(Tests: multi-drug resistance mechanisms, plasmid co-resistance, carbapenem indication.)*

**6.** A patient with *Pseudomonas aeruginosa* pneumonia is treated with intravenous ciprofloxacin. After five days, the patient is clinically worse. Repeat sputum culture grows *Pseudomonas* with a ciprofloxacin MIC that has risen from 0.5 µg/mL to 8 µg/mL. Using the *gyrA*/*parC* stepwise mutation model, explain how this happened during treatment. What does this tell you about fluoroquinolone monotherapy for serious *Pseudomonas* infections? *(Tests: stepwise resistance selection within a patient, clinical consequence.)*

### Synthesis

**7.** The chapter states: "A pharmaceutical company designs one molecule at a time; a bacterial population generates billions of mutation events per day." Use this asymmetry to explain why combination therapy (e.g., RIPE for tuberculosis) slows the clock, while monotherapy accelerates it. Then: why does the same logic apply to HIV antiretroviral therapy but not to most straightforward bacterial infections treated with a single antibiotic? *(Tests: evolutionary logic of combination therapy, when monotherapy is safe.)*

**8.** Daptomycin is inactivated by pulmonary surfactant. Vancomycin penetrates poorly into lung tissue. MRSA pneumonia is one of the most challenging infections to treat. Using only the mechanistic information in this chapter, explain why these two gaps exist and what class of drug you would reach for instead — and what its limitations are. *(Tests: mechanism-to-clinical-gap reasoning, no new facts required beyond the chapter.)*

### Challenge

**9.** A pharmaceutical company announces a new antibiotic targeting a bacterial enzyme essential for cell-membrane lipid synthesis — present in all bacteria, absent from humans, narrow Gram-positive spectrum, MIC 0.25 µg/mL against MRSA and VRE. Before accepting this as a major clinical advance, list four specific questions you would want answered. For each question, name the resistance mechanism, toxicity concern, ecological consequence, or pharmacokinetic problem it is designed to surface — and what experiment or data would resolve it. *(Tests: critical appraisal of a novel drug, translating mechanistic understanding into the right skeptical questions.)*
