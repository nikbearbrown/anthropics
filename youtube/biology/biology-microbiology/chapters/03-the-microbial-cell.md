# Chapter 3 — The Microbial Cell


## TL;DR

- The reason we can cure bacterial pneumonia with grams of penicillin and struggle to cure fungal pneumonia with milligrams of anything.
- The chapter moves through The most useful distinction in all of microbiology, The bacterial envelope: where almost all the good drug targets live, The other structures, and what they do, Archaea: the domain that doesn't make us sick, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The reason we can cure bacterial pneumonia with grams of penicillin and struggle to cure fungal pneumonia with milligrams of anything.*

---

A 58-year-old man is admitted with fever, productive cough, and a chest X-ray that lights up the lower right lung. The team starts intravenous penicillin. He gets several grams of it a day. He is fine.

Three weeks later, the same man — now neutropenic from chemotherapy — develops a new fever and a cavitating lung lesion. The bronchoscopy washings grow *Aspergillus fumigatus*, a mold. The team starts intravenous amphotericin B. The dose is measured in milligrams per kilogram. His kidneys take a hit anyway. Every clinician in the room calls the drug "ampho-terrible" while watching his creatinine climb.

Two infections. Two drugs. One patient. The difference between gram-doses-of-penicillin and milligram-doses-of-amphotericin is not a pharmacology footnote. It is the single most important idea in the treatment of infectious disease, and it lives entirely inside cell biology.

Penicillin attacks a molecule the bacterium has and the patient does not. Amphotericin attacks a molecule the fungus has — but the patient has something chemically similar. That "chemically similar" is what makes the drug dangerous. It is what fills every clinician's head when the creatinine climbs.

Why does the bacterium have something the patient doesn't? Why does the fungus not? The answer is the old binary at the center of all biology: prokaryote versus eukaryote.

![Two-column summary of the opening case ](images/03-the-microbial-cell-fig-01.png)
*Figure 3.1 — Two-column summary of the opening case *

---

## The most useful distinction in all of microbiology

Cells come in two kinds. There are cells with a membrane-bound nucleus, and there are cells without one. Cells without a nucleus are *prokaryotes* — from the Greek *pro-* (before) and *karyon* (kernel). Cells with one are *eukaryotes* — *eu-* (true). The distinction is older than any other classification scheme in biology and survives every revision of the evolutionary tree.

But the nucleus is just the headline. The two cell types differ along an entire suite of features:

| feature | prokaryote | eukaryote |
| --- | --- | --- |
| nucleus (no | yes | A concrete checkpoint for applying the chapter concept. |
| chromosome (circular one | linear multiple | A concrete checkpoint for applying the chapter concept. |
| ribosome (70S | 80S | A concrete checkpoint for applying the chapter concept. |
| membrane-bound organelles (none | yes | A concrete checkpoint for applying the chapter concept. |
| cell wall (peptidoglycan for bacteria | chitin for fungi or none for animals | A concrete checkpoint for applying the chapter concept. |
| membrane sterol (generally none | ergosterol in fungi, cholesterol in animals | A concrete checkpoint for applying the chapter concept. |
| cell size (0.5–5 μm | 10–100 μm). Student should return to this table after reading the chapter and annotate each row with: "drug target here?" and which drug. | A concrete checkpoint for applying the chapter concept. |

Every row in that table is a potential drug target. The clinician's goal is always the same: find a feature the microbe has that the patient does not, and attack it. The wider the structural difference, the safer the drug. The narrower the difference, the more collateral damage.

Ribosomes make the clearest example. Bacterial ribosomes are 70S — a unit called the Svedberg, which measures how fast a particle settles in a centrifuge. Eukaryotic ribosomes are 80S. The two are structurally different enough that a molecule can be designed to fit inside the 70S ribosome's active site and not the 80S. Tetracyclines do this. Macrolides do this. Aminoglycosides do this. Chloramphenicol does this. Linezolid does this. An entire pharmacy shelf of antibiotics works because of a single structural difference between two types of ribosome.

There is a wrinkle — and Feynman would insist I tell you about it now rather than bury it in a footnote. Your mitochondria still have 70S ribosomes. Mitochondria are descended from a bacterium your ancestor swallowed roughly two billion years ago and never digested. The mitochondria kept their bacterial ribosomes. So when an antibiotic targets the 70S ribosome, it doesn't only hit the bacterium. It occasionally nicks your mitochondria too. This is why chloramphenicol can suppress bone marrow. Why aminoglycosides can damage the inner ear. Why the 70S/80S story is the cleanest selectivity story in microbiology and still has edges.

!["The 70S exception" ](images/03-the-microbial-cell-fig-02.png)
*Figure 3.2 — "The 70S exception" *

The rest of this chapter is an inventory of what bacterial cells — and then eukaryotic microbial cells — have that you do not, and what each structure costs the patient when a drug attacks it.

---

## The bacterial envelope: where almost all the good drug targets live

Wrap the outside of a bacterial cell and you find two layers doing most of the structural work: the plasma membrane and the cell wall.

The **plasma membrane** is a phospholipid bilayer, the same basic architecture as yours. Two sheets of lipid molecules, water-loving heads facing outward, water-hating tails buried in the middle. The difference: bacteria have no mitochondria. The electron transport chain — the machinery that generates ATP by pushing protons across a membrane — sits in the plasma membrane itself. The whole power grid is in the outer skin.

Outside the membrane sits the **cell wall**, built from a polymer called **peptidoglycan**. The name is worth taking apart once. *Peptido-* refers to short amino-acid chains. *Glycan* refers to a sugar polymer. Peptidoglycan is a mesh of sugar chains cross-linked by peptide bridges — like a chainlink fence where the chains are sugars and the links are amino acids. The mesh is strong enough to resist the osmotic pressure inside the cell, which is far more concentrated than the surrounding medium. Without the wall, the bacterium would swell and burst.

Two ways of building this wall sort bacteria into the two Gram categories:

**Gram-positive** bacteria build a thick wall — twenty or more layers of peptidoglycan mesh — wrapped around a single membrane. The thickness holds onto crystal violet dye in the Gram stain. You get purple.

**Gram-negative** bacteria build a thin wall — sometimes only a molecule or two thick — sandwiched between two membranes. The outer membrane contains **lipopolysaccharide** (LPS), the molecule responsible for the fever, hypotension, and sometimes death of gram-negative sepsis. The thin peptidoglycan loses the crystal violet when washed with alcohol; safranin counterstain turns it pink.

![Cross-section diagrams of Gram-positive and Gram-negative envelopes](images/03-the-microbial-cell-fig-03.png)
*Figure 3.3 — Cross-section diagrams of Gram-positive and Gram-negative envelopes*

Now here is where the drug story begins to click.

**Beta-lactam antibiotics** — penicillin, amoxicillin, the cephalosporins, the carbapenems — work by jamming the enzyme that builds the peptide cross-links. The enzyme is called a *transpeptidase*, sometimes a penicillin-binding protein. It has a serine in its active site that normally forms a temporary covalent bond with the peptide it's cross-linking. Penicillin fits the active site, forms that covalent bond, and never lets go. The cross-linking stops. The mesh can't grow. The cell tries to expand anyway and ruptures.

You have no transpeptidase. You make no peptidoglycan. There is no structural analogue in any human cell for penicillin to accidentally bind. The drug distributes through your bloodstream and tissues, is filtered by your kidneys, and exits in your urine without finding anything meaningful to attach to. This is why a patient can receive grams per day. The therapeutic window isn't wide — it's essentially infinite for most people.

**Glycopeptides** — vancomycin — work differently but on the same target. Rather than jamming the enzyme, vancomycin grabs the peptide chains directly before they can be cross-linked, physically blocking the reaction. The result is the same: no cross-links, wall fails, bacterium dies. And again: useless against human cells, because there are no peptide chains to grab.

Three bacteria break this picture in instructive ways.

**Mycoplasma** has no cell wall at all. It lives as a bare membrane, supported osmotically by surrounding tissue fluid. Penicillin does nothing to it — there's no peptidoglycan to attack. *Mycoplasma pneumoniae* causes "walking pneumonia," and it's treated with macrolides or tetracyclines: drugs that hit the 70S ribosome, not the wall. One misconception worth correcting immediately: *Mycoplasma is not a virus*. It is a fully cellular bacterium with its own ribosomes, its own metabolism, its own membrane. It just discarded its wall during evolution. The confusion arises because it's unusually small and dodges cell-wall antibiotics, but the similarity ends there.

**Mycobacterium** — the genus that includes *M. tuberculosis* — has a standard peptidoglycan wall plus an outer coating of **mycolic acids**: waxy, long-chain lipids that make the cell acid-fast and turn it into something close to a biological submarine. The waxy coat is why the Gram stain barely works on *Mycobacterium* and why an acid-fast stain is used instead. It is also why tuberculosis requires six months of combination therapy: the drugs have to penetrate a layer of wax that most molecules bounce off. The bacterium is slow to kill not because it's inherently resistant, but because getting anything inside it at therapeutic concentrations is genuinely hard.

**MRSA** — methicillin-resistant *Staphylococcus aureus* — uses a different trick. It hasn't gotten rid of peptidoglycan. It has acquired a modified transpeptidase — PBP2a — with a changed active site that beta-lactam drugs can't bind well. The target is still there. The key no longer fits the lock. This is resistance through target modification, and it renders the entire beta-lactam class near-useless against MRSA.

---

## The other structures, and what they do

A bacterial cell is doing several things simultaneously: moving, sticking, hiding, storing genetic material, and occasionally building a structure that can wait out the apocalypse. Each of those functions has a physical structure behind it.

**Flagella** are helical filaments made of a protein called flagellin, driven by a molecular rotary motor anchored in the cell envelope. The motor is powered by proton flow — the same electrical gradient the membrane uses for ATP synthesis. Spin one direction, the cell swims forward. Reverse, the cell tumbles and reorients. The combination of swimming and tumbling lets bacteria navigate chemical gradients — a behavior called *chemotaxis*. When you see "*E. coli* O157:H7," the H7 part names the seventh recognized flagellin variant; flagellin is the H antigen used to serotype strains.

**Fimbriae and pili** are shorter attachment structures. Fimbriae are fine hairs — often hundreds per cell — that let bacteria adhere to host cells, catheters, and each other. Uropathogenic *E. coli* colonizes the bladder wall via specialized fimbriae. Without them, the bacterium washes through. With them, it holds on long enough to cause a urinary tract infection. Longer, fewer sex pili form bridges between bacteria for DNA transfer — which brings us to antibiotic resistance.

**Plasmids** are small circular DNA molecules that replicate independently of the chromosome. They often carry antibiotic resistance genes. The same plasmid can carry resistance to several antibiotics simultaneously. And plasmids move — through conjugation via sex pili, through uptake from the environment (transformation), through bacterial viruses (transduction). This means resistance does not need to evolve freshly in every bacterium. A resistance gene that arises once can spread horizontally across bacterial species, across hospitals, across countries. It is the main reason resistance has been outrunning antibiotic discovery for decades.

![Horizontal gene transfer ](images/03-the-microbial-cell-fig-04.png)
*Figure 3.4 — Horizontal gene transfer *

**The capsule** is a layer of polysaccharide sitting outside the cell wall. It traps water. It hides bacterial surface molecules from immune recognition. Most importantly, it makes the cell slippery — macrophages and neutrophils that try to engulf it cannot get a grip. This is a major virulence factor. *Streptococcus pneumoniae* with a capsule kills mice readily; without one, it's nearly harmless. The pneumococcal conjugate vaccines (PCV13, PCV20) work by teaching the immune system to recognize and target the capsule. Capsules are not universally virulent — many environmental bacteria have them for desiccation resistance — but in a host with a functioning immune system trying to phagocytose bacteria, a capsule is a shield.

![Diagram of an encapsulated bacterium being approached by](images/03-the-microbial-cell-fig-05.png)
*Figure 3.5 — Diagram of an encapsulated bacterium being approached by*

**Endospores** are the extreme case of bacterial survival. When *Bacillus* or *Clostridium* runs out of nutrients, it does something unusual: it packages a copy of its chromosome inside multiple protective coats, along with minimal repair proteins, and lets the parent cell die around it. The spore is dehydrated to a fraction of normal cell water content. It contains high concentrations of dipicolinic acid complexed with calcium, which stabilizes proteins. The DNA is wrapped in protective proteins. The outer coat is layered like an onion. The result survives boiling, drying, ionizing radiation, alcohol, hydrogen peroxide, and most disinfectants. *Bacillus anthracis* endospores persist in soil for a century. This is why hospitals autoclave at 121°C under pressure rather than boiling at 100°C — boiling doesn't reliably kill spores; autoclaving does.

The clinical consequences are direct. *Clostridium tetani* spores enter wounds and germinate into toxin-producing cells. *Clostridioides difficile* spores survive hospital cleaning protocols and persist on surfaces, re-infecting patient after patient. C. diff is one of the most common hospital-acquired infections specifically because of the spore — everything else about infection control can be done right, and the spore is still there.

---

## Archaea: the domain that doesn't make us sick

Bacteria are one prokaryotic domain. Archaea are the other, discovered by Carl Woese in 1977 by sequencing ribosomal RNA. Under a microscope they look like bacteria. Everything else about them is different in ways that should matter clinically — and yet, as far as we can tell, not a single archaeon has been confirmed as a human pathogen.

Archaeal walls don't contain peptidoglycan. They use an S-layer (a regular crystalline array of surface proteins) or a chemically distinct polymer called pseudopeptidoglycan. Beta-lactams do nothing to them. Vancomycin does nothing. Their membranes are also different: where bacteria and eukaryotes attach fatty acids to glycerol via ester bonds, archaea use isoprenoid chains connected by ether bonds — more chemically stable, which is part of why thermophilic archaea survive at temperatures that would liquefy a bacterial membrane. Some thermophiles have membranes made of a single lipid layer that spans the full thickness rather than a bilayer.

And yet. Archaea live in the human gut. Methanogens — archaea that produce methane from CO₂ and hydrogen — are present in the large intestine of most people. Their biochemistry is alien enough that much of the innate immune system shouldn't recognize them. They have no confirmed pathogen in the clinical record.

The honest answer is that we don't know why. Several hypotheses circulate: archaeal surface molecules may not bind mammalian cell receptors; archaeal metabolism may not get a foothold at body temperature and oxygen tension; we may simply be missing them because clinical diagnostics don't look for archaea systematically. I find none of these fully satisfying. This is a gap — real, open, and worth naming.

---

## Eukaryotic microbes: when the drug gets harder

Cross the nuclear membrane and the picture changes fundamentally. Fungi, protozoa, and other eukaryotic microbes are not one phylogenetic group — the category is a teaching convenience. What they share is a cell architecture much closer to yours than bacteria are.

**Fungi** have cell walls made of chitin — the same polymer in insect exoskeletons. Not peptidoglycan. Beta-lactams are useless. Their membranes contain **ergosterol** — a sterol that modulates membrane fluidity, the way cholesterol does in your membranes. Ergosterol and cholesterol are chemical cousins. Both are sterols. They differ by two methyl groups and a double bond.

That small structural difference is where every antifungal drug has to live.

Amphotericin B binds ergosterol and forms a pore through the fungal membrane. Ions and small molecules leak out. The fungus can't osmoregulate and dies. Amphotericin binds ergosterol roughly ten times more tightly than cholesterol — but "ten times" is not "infinity." [verify exact selectivity ratio] A meaningful fraction of the drug also binds the cholesterol in your kidney tubular cells. Those cells leak. Creatinine rises. The clinicians watching the patient in our opening case already know this before they write the order.

Azole antifungals (fluconazole, itraconazole, voriconazole) take a different approach: they block the enzyme that *synthesizes* ergosterol, starving the fungal membrane of its structural component. This is more selective — the human homolog enzyme exists but binds the drug far less well — but again, the selectivity is incomplete.

One antifungal class does achieve the kind of safety bacteria offer: the echinocandins (caspofungin, micafungin). They target **β-glucan synthase**, the enzyme that builds β-glucan, a major component of the fungal cell wall. Human cells have no β-glucan. Human cells have no β-glucan synthase. The therapeutic window is substantially wider. The echinocandins, invented in the 1990s, are as close as antifungal pharmacology has gotten to the penicillin situation — and they work only against certain fungi (*Candida* and *Aspergillus*). They don't touch *Cryptococcus*.

| drug or class | target structure | present in bacterium? | present in fungus? | present in human cell? |
| --- | --- | --- | --- | --- |
| penicillin (transpeptidase | peptidoglycan | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| vancomycin (peptidoglycan chains | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| macrolides (70S ribosome | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| amphotericin B (ergosterol | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| azoles (ergosterol synthesis | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| echinocandins (β-glucan synthase). Student should be able to fill in the selectivity column from the chapter alone. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |

Fungi themselves come in two body plans. **Yeasts** are single-celled and reproduce by budding — a smaller daughter cell pinches off from the parent. **Molds** are filamentous: long branching tubes of cytoplasm called hyphae, woven into a mass called a mycelium. Some fungi are **dimorphic** — they grow as molds in the environment and as yeasts inside a host. *Histoplasma capsulatum*, *Blastomyces dermatitidis*, *Coccidioides immitis* all do this. The mold form is what you inhale. The yeast form is what your immune system fights.

The clinically important yeasts: *Candida albicans* and its relatives are normal residents of human skin, mouth, gut, and vagina. In healthy people they cause minor infections. In neutropenic patients they invade the bloodstream. *Cryptococcus neoformans* causes meningitis in AIDS patients and other immunocompromised hosts; it's diagnosed by India-ink stain of cerebrospinal fluid, where the capsule of the yeast (yes — a capsule, like bacteria have) shows up as a clear halo around the dark background.

The medically important molds: *Aspergillus fumigatus*, which the patient in our opening case contracted. *Penicillium* species — the genus whose contamination of a bacterial plate led Alexander Fleming to notice, in 1928, that something from the mold was killing the *Staphylococcus* around it. The observation that became penicillin.

---

## Protozoa: eukaryotes that hunt

Protozoa are single-celled eukaryotes that live by predation or parasitism. The group is defined by lifestyle, not ancestry — *Plasmodium*, *Giardia*, *Trypanosoma*, and *Entamoeba* are not closely related. They have in common a eukaryotic cell, a small size, and a medical importance.

The drugs for protozoa are, almost without exception, more toxic than the drugs for bacteria. The reason is the same structural logic we've been building: the protozoan has a nucleus, mitochondria, an endoplasmic reticulum, 80S ribosomes. There is less to attack that isn't also present in the patient.

*Plasmodium falciparum*, the deadliest malaria parasite, compounds this problem with a seven-stage life cycle spanning two hosts. Sporozoites from a mosquito bite enter the bloodstream and invade liver cells. Inside, they divide asexually, burst the hepatocytes, enter red blood cells, divide again, burst the red blood cells — this is the periodic fever — and some differentiate into sexual forms the next mosquito picks up. The mosquito completes the sexual cycle in its gut, and sporozoites form again. Seven stages. Different proteins expressed at each stage. A vaccine that targets one phase may fail at another, and the parasite has been an evolutionary arms race partner for as long as humans have lived in the tropics.

![Plasmodium falciparum life cycle ](images/03-the-microbial-cell-fig-06.png)
*Figure 3.6 — Plasmodium falciparum life cycle *

*Giardia lamblia* causes the most common waterborne protozoal infection worldwide. *Trypanosoma brucei* causes African sleeping sickness. *Toxoplasma gondii* infects roughly a third of all humans asymptomatically, waits in tissue cysts, and activates dangerously in immunocompromised hosts. Each of these is a eukaryote. Each is, in the relevant sense, more like you than any bacterium is.

---

## What the first cut actually tells us

Return to the opening case. The patient receives grams of penicillin without meaningful toxicity. His bacterial target — peptidoglycan — is completely absent from his own cells. Three weeks later, he receives milligrams of amphotericin B and his kidneys suffer for it. His fungal target — ergosterol — is chemically similar enough to his own membrane sterols that the drug bleeds over.

The difference is not in the drugs' potency or in the severity of the infections. The difference is in *how different the target is from anything in the patient*. That gap — structural distance between microbe and host — is what sets the therapeutic window. Large gap: grams, cheap, nearly safe. Small gap: milligrams, expensive, careful monitoring.

This is why we have dozens of antibiotic classes and a handful of antifungals. It is why drugs for protozoa and parasitic worms tend to have side-effect profiles that patients remember. It is why the history of antimicrobial pharmacology is, at its root, a history of structural comparison between cell types.

Once you can read a cell the way this chapter reads it — membrane, wall, ribosome, sterol, appendages, dormancy structures — you can look at any new pathogen and ask: what does it have that we don't? The answer tells you where to put the drug.

---

## LLM Exercise — Cell Comparator (Show / Say / Constrain / Verify)

**What you're building:** `03-cell-comparator.html` — an interactive widget that lets a student toggle between five labeled cell diagrams (Gram-positive bacterium, Gram-negative bacterium, fungal cell, protozoan, human cell) and click on individual structures to see (a) their function and (b) their clinical relevance.

Clicking the peptidoglycan layer of the Gram-positive bacterium should show: *"Polymer of sugars cross-linked by peptide bridges. Provides osmotic strength. Antibiotic targets: penicillin and other beta-lactams (block cross-linking enzyme), vancomycin (binds sugar chains directly). Absent from human cells — the basis of selective toxicity for these drug classes."*

Clicking ergosterol in the fungal membrane should show: *"Dominant sterol in fungal cell membranes; analog of cholesterol in human membranes. Drug targets: azoles (block ergosterol synthesis), polyenes such as amphotericin B (bind ergosterol and form pores). Selectivity is imperfect — amphotericin B also binds cholesterol weakly, causing kidney toxicity."*

The widget should also have a **side-by-side compare** mode where the student picks any two cell types and the comparator highlights structural differences and shared features.

**Tool:** Claude Code for the build. ChatGPT or Claude for the cross-check.

### Show

```
I'm building an interactive HTML/JS widget that lets a microbiology
student compare five cell types side by side:

1. Gram-positive bacterium (e.g., Staphylococcus aureus)
2. Gram-negative bacterium (e.g., Escherichia coli)
3. Fungal cell (e.g., Candida albicans)
4. Protozoan (e.g., Plasmodium falciparum trophozoite)
5. Human cell (for reference)

For each cell type, I need labeled structures (clickable). Each
click pops up a panel with two fields:
- Function: what this structure does for the cell.
- Clinical relevance: drug targets, diagnostic value, or virulence
  role. If none, say "no current clinical drug target."

The widget also needs a "compare mode" where the student picks
any two cell types and sees a structural diff.
```

### Say

```
Generate (a) a JSON data file with one record per cell type, each
containing a list of structures with {name, function,
clinical_relevance}, and (b) a single self-contained HTML file
that renders the diagrams as SVG, handles clicks, and supports
compare mode.

Use a clean, accessible design. No external libraries beyond
vanilla JS. Inline CSS. Color-code by Gram reaction where
relevant.
```

### Constrain

```
Hard constraints:

1. Every drug claim must name a specific drug or drug class. Not
   "antibiotics." Penicillin, vancomycin, ciprofloxacin, etc.
2. For each structure where you claim a drug target, give one
   sentence on the structural reason the drug is selective. If
   you cannot give a structural reason, mark the claim
   [needs verification] and do not assert it.
3. Do not invent drugs. If you are uncertain, use [verify].
4. Peptidoglycan must appear only on bacteria. Chitin must
   appear only on fungi. Ergosterol on fungi, cholesterol on
   the human cell.
5. The protozoan cell must include mitochondria (or in the
   special case of organisms like Giardia, an explicit note that
   it has remnant mitosomes — and a [verify] tag).
6. The widget must work without internet access once loaded.
```

### Verify

After Claude Code produces the widget, paste the JSON data file into a second LLM with this prompt:

```
This is a JSON file describing five cell types for a microbiology
teaching widget. For each structure listed, evaluate:
(a) Is it correctly placed in the right cell type?
(b) Is the function description accurate?
(c) Are the drug-target claims accurate? Flag any drug-target
    claim where the drug listed does not actually target that
    structure in clinical practice.
(d) Anything missing that an introductory clinical
    microbiology course would expect?

Output a list of corrections.
```

Apply the corrections. Reload the widget. Test by clicking through every structure in every cell type and asking: *if a student clicked this, would the answer be wrong in any way that matters?*

### Extension — connection to Chapter 4

Once the widget is working, ask Claude:

```
A virus particle is not in this widget. Why not? List the
features of the comparator that would have to be modified or
omitted for a virus, and explain what this tells us about the
classification of viruses as living or non-living.
```

The answer is the bridge to the next chapter. Bacteria and eukaryotic microbes are cells. Chapter 4 introduces the things that aren't.

---

**What would change my mind.** If a confirmed archaeal human pathogen were identified — and the mechanism involved a structural feature absent from bacteria — the framing of archaea as clinically absent would need substantial revision. As of writing this, the gap remains. `[verify: any confirmed archaeal human pathogens as of 2026]`

**Still puzzling.** I do not understand why mitochondrial inheritance is exclusively maternal in most multicellular eukaryotes. The hypotheses involve mitochondrial-nuclear coevolution and the suppression of selfish mitochondrial elements; none is fully settled. I also do not understand the energetics of *Mycoplasma*'s wall-less existence well enough to say why some bacterial lineages successfully discarded their walls while most did not.

---

*The patient in the opening case survived the bacterial pneumonia and, eventually, the fungal infection too. What made the second one harder was not the virulence of the mold or the weakness of the drug. It was the structure of the cell — and the fact that a eukaryotic pathogen runs out of things to attack that aren't also you. Chapter 4 describes the entities that have taken this logic to its extreme: organisms so stripped down that they have almost nothing you can target at all.*

---

## Exercises

### Warm-up

**1.** A patient develops food poisoning from home-canned vegetables that sat sealed at room temperature for six weeks. The pathogen is *Clostridium botulinum*. Which bacterial structure best explains how it survived the canning process — the capsule, the plasmid, or the endospore? State the structural reason in one sentence.

**2.** A patient has "walking pneumonia" caused by *Mycoplasma pneumoniae*. Which of the following antibiotics has no chance of working, and why: (a) penicillin, (b) vancomycin, (c) azithromycin, (d) doxycycline? Name the structural reason behind your answer.

**3.** For each organism below, give the Gram reaction (positive, negative, or not applicable) and morphology (coccus, rod, spiral, or other): *Staphylococcus aureus*, *Escherichia coli*, *Streptococcus pneumoniae*, *Pseudomonas aeruginosa*, *Mycobacterium tuberculosis*, *Mycoplasma pneumoniae*.

### Application

**4.** *Mycobacterium tuberculosis* infections require six months of combination antibiotic therapy. A *Streptococcus pyogenes* throat infection clears with ten days of penicillin. Using cell-envelope structure only, explain the difference. Where do the drugs have to get to, and what is physically in the way in each case?

**5.** A researcher proposes a new antifungal that targets the ribosome of *Candida albicans*. What is the structural problem with this proposal? Name a fungal-specific target that would be better, and explain why it produces a wider therapeutic window.

**6.** Return to the opening case. Walk through the cell-structure reasoning for why the patient tolerates grams of penicillin per day but develops renal injury on 1 mg/kg/day of amphotericin B. Then answer: the echinocandins (caspofungin, micafungin) target β-glucan synthase. Based on the selective-toxicity logic in this chapter, would you expect their therapeutic window to be closer to penicillin's or to amphotericin's? Why?

### Synthesis

**7.** MRSA carries a modified transpeptidase (PBP2a) that beta-lactams can't bind. A *Mycoplasma* strain is intrinsically resistant to all beta-lactams. The resistance mechanism is completely different in each case. Describe both mechanisms, name the structural difference that makes each one work, and explain which type of resistance is more concerning from a public-health standpoint — and why.

**8.** The chapter claims that the small structural difference between ergosterol and cholesterol is "where every antifungal drug has to live." Construct the argument as a chain: (a) what ergosterol and cholesterol have in common structurally, (b) what they differ in, (c) why that difference is exploited by amphotericin B but imperfectly, (d) what the echinocandins do instead, and (e) why the echinocandin approach still doesn't cover all fungal pathogens.

### Challenge

**9.** Not a single archaeon has been confirmed as a human pathogen, despite archaea living in the human gut. The chapter names three hypotheses and says none is fully satisfying. Pick the hypothesis you find most plausible, state the specific evidence that would confirm or refute it, and explain what diagnostic test — one that doesn't currently exist in routine clinical practice — would be needed to close the gap. *(There is no settled answer. The goal is to sharpen the question.)*
