# Chapter 5 — Microbial Biochemistry and Metabolism

*A small engine, and you can read its specifications.*

---

There is a fact about *Clostridium perfringens* that reorganizes how you think about infection, antibiotics, surgery, and beer — all at once. The fact is this: **a bacterium is a small chemistry experiment that pays its own electricity bill.**

That is not a metaphor. A microbe takes molecules apart, captures the electrons that fall out of them, and uses the energy of those falling electrons to make ATP — the universal currency of cellular work. The whole machinery of microbiology, from virulence to drug resistance to fermentation, is downstream of that one idea. A bacterium is an engine. Once you can read the engine's specifications, the field opens up.

Let me show you the specifications.

---

## What a microbe is made of

Squeeze the water out of a bacterial cell and what is left is, by mass: roughly half protein, a fifth nucleic acid, a tenth lipid, a tenth polysaccharide, and a few percent of small molecules. Four classes, four jobs.

**Carbohydrates** are the cell's energy and structure molecules. A monosaccharide — glucose, fructose, ribose — is the unit. Chain them and you get polysaccharides. The same glucose monomer in different bond geometry produces radically different materials: glucose in alpha bonds is starch (energy storage), glucose in beta bonds is cellulose (structural rigidity), and glucose-derived sugars cross-linked with short peptides is *peptidoglycan*, the bacterial cell wall. The chemistry is almost entirely in the bond, not the monomer. Penicillin exploits this: it attacks the enzymes that form the peptide cross-links in peptidoglycan. The drug is not killing the cell by some mysterious mechanism. It is punching out a structural fastener and watching the cell burst.

<!-- → [INFOGRAPHIC: glucose monomer → three bond-geometry variants → starch (coiled), cellulose (rigid linear), peptidoglycan (mesh with peptide crosslinks) — student should see that bond geometry, not monomer identity, determines material properties and antibiotic targets] -->

**Lipids** are the membrane and energy-reserve molecules. A phospholipid has a polar head and two nonpolar tails. Drop a million of them in water and they self-assemble into a bilayer, heads out, tails in, no assistance required. This is one of the most consequential pieces of chemistry in biology: life requires a boundary, and the bilayer provides one for free. Bacterial membranes use ester-linked fatty acids; archaeal membranes use ether-linked isoprenoids, which are more heat- and acid-stable. This is why archaea dominate hot springs. The membrane chemistry *is* the habitat chemistry.

<!-- → [IMAGE: phospholipid bilayer self-assembly diagram — left panel shows individual phospholipid molecules in water (disordered); right panel shows spontaneous bilayer formation with heads facing aqueous environment and tails sequestered inside — annotation should label polar head, nonpolar tails, aqueous interior/exterior; student should see that no energy input or enzymatic machinery is required for assembly] -->

**Proteins** are the workhorses. Enzymes, structural beams, transporters, motors, toxins. A protein is a chain of amino acids — twenty standard types, each with a different side chain. The side-chain sequence is set by the gene and determines how the chain folds. The fold determines the function. One amino acid substitution can destroy a protein entirely: sickle-cell hemoglobin is glutamate to valine at position 6 of the beta chain — one mutation, one devastating disease. [^2] Shape is function. This is not metaphor either.

**Nucleic acids** carry the instructions. DNA stores; RNA copies and translates. The sequence of bases in DNA encodes the sequence of amino acids in every protein the cell will make. Chapter 9 goes deeper on this. For now, the important point is that nucleic acids are also targets — fluoroquinolones attack the bacterial enzyme that manages DNA topology, rifampin attacks the bacterial RNA polymerase — and the reason these drugs have selective toxicity is that bacterial and human versions of these enzymes are structurally different enough to bind different molecules.

That is the inventory. The question is: how does the cell pay for building and maintaining it?

---

## Enzymes and the trick of selective toxicity

Before metabolism: a word about enzymes, because they are the machinery of everything that follows, and because the first synthetic antibiotics work through a mechanism elegant enough to explain once clearly and remember forever.

An enzyme is a folded protein with an *active site* — a pocket shaped so that a particular substrate fits inside it, correctly oriented for the chemical reaction the enzyme will catalyze. The acceleration factors are preposterous: a typical enzyme runs its reaction 10⁶ to 10¹² times faster than the same reaction would run in water alone. [^3] Without enzymes, glycolysis — ten steps to split glucose — would take hours per reaction rather than milliseconds. You would not survive your own biochemistry.

Two properties matter most.

**Specificity.** The active site fits one molecular shape. Lactase splits lactose; it will not touch sucrose. Penicillin-binding protein attacks peptidoglycan cross-links; it ignores human collagen. Geometry is what separates one enzyme from another, and geometry is what a drug designer is really exploiting when they design a selective antibiotic.

**Inhibitability.** A molecule that binds to an enzyme and slows it down is an *inhibitor*. If the inhibitor fits into the active site itself — taking the place the substrate would have occupied — it is a *competitive inhibitor*. Flood the enzyme with enough substrate and you can displace the inhibitor; the binding is a competition. If the inhibitor binds somewhere else on the enzyme and distorts the protein so the active site no longer works, it is a *noncompetitive inhibitor*. No amount of extra substrate helps, because the problem is not occupancy of the active site; it is the shape of the whole protein.

Here is the sulfonamide story, which is worth holding in your head as a model.

*Sulfonamides* — the first synthetic antibiotics, introduced in the 1930s — are competitive inhibitors of a bacterial enzyme called *dihydropteroate synthase*. [^4] This enzyme builds folate. The substrate it normally uses is para-aminobenzoic acid (PABA). Sulfonamides are molecules with almost identical structure to PABA. The enzyme cannot tell them apart. The sulfa slides into the active site, the enzyme is blocked, folate synthesis stops, and the bacterium starves for a vitamin it cannot now make.

Why doesn't the sulfa kill *you*? Because humans do not make folate. We eat it. We have no dihydropteroate synthase. The drug slides around our cells looking for an active site to bind and finds none. *Selective toxicity* in molecular detail: the drug does not have an off-switch for human cells. It has nothing to bind to in human cells.

Every selective antibiotic in use exploits the same logic. Penicillin attacks peptidoglycan synthesis (bacteria build it; you don't). Tetracycline and erythromycin attack the bacterial ribosome (structurally different from the human ribosome). Ciprofloxacin attacks bacterial DNA gyrase. Rifampin attacks bacterial RNA polymerase. The discovery process is always: find a chemical reaction the pathogen runs and you don't. The enzyme is the target.

<!-- → [INFOGRAPHIC: competitive vs. noncompetitive inhibition side-by-side — left panel: active site occupied by competitive inhibitor (sulfonamide shown as PABA mimic), substrate molecules blocked, label "high substrate concentration displaces inhibitor"; right panel: allosteric site occupied by noncompetitive inhibitor, active site distorted, label "adding more substrate does not help" — student should see the structural logic that determines whether the drug can be overcome by substrate flooding] -->

<!-- → [TABLE: antibiotic → enzyme target → bacterial reaction exploited → why human cells are spared — rows for penicillin, sulfonamides, TMP, ciprofloxacin, rifampin, tetracycline, erythromycin — student should be able to predict selectivity from mechanism] -->

---

## ATP — what the cell is actually after

A bacterium breaks down molecules not because it wants to demolish them, but because the demolition releases electrons, and the electrons can be captured and used to make ATP.

ATP — adenosine triphosphate — is the cell's universal energy currency. It has three phosphate groups linked in a row. The bond between the second and third phosphate stores energy. Hydrolyze that bond — break it with water, releasing inorganic phosphate plus ADP — and you release roughly 7.3 kcal per mole under standard conditions, enough to drive most of the cellular work that needs doing. [^6] The cell spends ATP to do work; it rebuilds ATP by capturing energy from catabolism.

The flux is staggering. A resting human cell uses roughly 10⁷ ATP molecules per second. An adult human turns over something like 65 kilograms of ATP per day — approximately body weight, every twenty-four hours. ATP is not stored. It is made and spent continuously. The cell is not a battery; it is a power grid.

The two electron carriers you need to meet: **NAD⁺** and **FAD**. When a molecule is oxidized — broken down, electrons stripped from it — NAD⁺ picks up the electrons (and a proton) and becomes NADH. FAD does the same, becoming FADH₂. These carriers then transport the electrons to where they can be used to make more ATP. NADH and FADH₂ are the wires. ATP is the cash at the other end.

The vocabulary: **catabolism** breaks things down and makes ATP. **Anabolism** builds things up and spends ATP. Microbial metabolism is the balance between the two. Every bacterium is solving the same problem: make enough ATP from catabolism to fund the anabolism that makes more bacterium.

---

## The universal opening move: glycolysis

Every cell in every domain of life that uses glucose starts with the same ten steps: **glycolysis** — Greek for "sugar splitting." The ten enzymes look almost identical in *E. coli*, in brewer's yeast, in human muscle, in a deep-sea hyperthermophile. This is one of the oldest biochemical pathways on Earth, and its conservation across all life says something about how fundamental it is.

I want to show you the bookkeeping, not the structures of the intermediates. The structures you can look up; the bookkeeping is the thing that tells you about energy.

A glucose molecule has six carbons. Glycolysis splits it, by ten steps, into two three-carbon molecules of **pyruvate**. Along the way the cell spends 2 ATP early — priming the glucose for splitting — and recovers 4 ATP later, for a net gain of 2 ATP. Two NAD⁺ are reduced to NADH in the process.

So: 1 glucose → 2 pyruvate + **2 net ATP** + **2 NADH**. No oxygen involved. No membrane. Glycolysis happens in the cytoplasm and it is the universal first move, independent of what atmosphere the cell is living in.

<!-- → [INFOGRAPHIC: glycolysis bookkeeping flow — single horizontal timeline from glucose to 2 pyruvate; above the line: ATP invested (−2) at the priming phase, ATP recovered (+4) at the payoff phase, net = +2; below the line: NAD⁺ reduced to NADH at step 6 (×2); annotations label "investment phase," "payoff phase," "substrate-level phosphorylation"; student should be able to reconstruct the net yield from this diagram without memorizing intermediates] -->

Pyruvate is a fork. What happens next depends entirely on what electron acceptors the cell has access to. There are three branches, and they are not equally rewarding.

---

## The three branches

### Branch one — aerobic respiration

If oxygen is available, the cell takes the high-yield path.

Each pyruvate loses a carbon as CO₂ and becomes **acetyl-CoA** — a two-carbon fragment attached to a carrier molecule. The acetyl-CoA then enters the **citric acid cycle** (also called the Krebs cycle, or TCA cycle): eight reactions that oxidize the acetyl group fully to two CO₂ molecules, turning out 3 NADH, 1 FADH₂, and 1 ATP per turn. Two turns per glucose. All the carbons from the original glucose have now been released as CO₂. The energy is sitting in the electron carriers.

Cashing in the electron carriers happens at the **electron transport chain** (ETC): four protein complexes embedded in the cell membrane (in bacteria) or the inner mitochondrial membrane (in your cells). NADH and FADH₂ deliver their electrons to the chain. The electrons flow down through the complexes, from lower to higher electron affinity, releasing a little energy at each step. That energy is used to pump protons across the membrane, building up an electrochemical gradient — protons concentrated on one side, depleted on the other.

That gradient is stored energy, and the cell extracts it with a turbine.

The turbine is **ATP synthase**, and it is a literal molecular motor. The proton gradient drives protons back through a ring of subunits embedded in the membrane; the ring rotates, and the rotation cranks a catalytic head that cycles through conformations that bind ADP and phosphate and release ATP. Peter Mitchell proposed this *chemiosmotic mechanism* in 1961. He was disbelieved for nearly a decade. He retreated to a private laboratory in a manor house in Cornwall, kept working, and won the Nobel Prize in Chemistry in 1978. [^7]

This is not a metaphor. The structure has been solved by cryo-electron microscopy. The rotor turns. You can watch it.

<!-- → [IMAGE: ATP synthase molecular motor diagram — cross-section of inner membrane showing F₀ ring embedded in lipid bilayer, proton flow through the ring driving rotation of the central stalk, F₁ catalytic head cycling three active sites (open/loose/tight conformations) to synthesize ATP from ADP + Pᵢ; arrows show proton gradient direction and direction of ring rotation; label "chemiosmotic mechanism (Mitchell, 1961)" — student should see that ATP synthesis is mechanical, not purely chemical, and that the gradient is the immediate energy source] -->

At the end of the electron transport chain, the terminal electron acceptor is oxygen: four electrons plus four protons plus O₂ combine at Complex IV to form two water molecules. This is where the oxygen goes. This is why aerobic respiration produces water as a byproduct.

The ATP yield per NADH — using modern stoichiometry, with proton-to-ATP ratios measured directly from ATP synthase structures — is about **2.5 ATP per NADH** and **1.5 ATP per FADH₂**. [^8] FADH₂ yields less because it feeds electrons into the chain one complex later, skipping one proton-pumping step.

The arithmetic for one glucose through full aerobic respiration:

- Glycolysis: 2 ATP + 2 NADH
- Pyruvate → acetyl-CoA (×2): 2 NADH
- Citric acid cycle (×2): 2 ATP + 6 NADH + 2 FADH₂
- ETC: 10 NADH × 2.5 = 25 ATP; 2 FADH₂ × 1.5 = 3 ATP

**Grand total: ~32 ATP per glucose.**

(The textbook number you sometimes see — 36 or 38 — uses older, rounded ratios that turned out to be slightly too high. The qualitative picture survives the revision. The number does not. Treat 38 the way you would a price from the 1970s: directionally informative, numerically outdated.)

<!-- → [TABLE: aerobic respiration ATP accounting per glucose — rows: glycolysis (substrate-level), pyruvate decarboxylation, citric acid cycle ×2 turns (substrate-level), ETC from 10 NADH, ETC from 2 FADH₂ — columns: ATP directly produced, NADH produced, FADH₂ produced, ATP from ETC (using 2.5 and 1.5 stoichiometry), running total — final row shows grand total ~32; footer note contrasts with textbook 38 and explains why stoichiometry changed] -->

### Branch two — anaerobic respiration

No oxygen — but there is some other molecule around that the cell can use as a terminal electron acceptor. Nitrate (NO₃⁻), sulfate (SO₄²⁻), carbon dioxide, ferric iron (Fe³⁺). Different organisms have ETCs designed around different acceptors.

The principle is identical to aerobic respiration: build a proton gradient by running an ETC, drive ATP synthase on the gradient. The yield is lower than aerobic because the alternative acceptors are weaker oxidants than oxygen — the energy gap between electron donor and acceptor is smaller, fewer protons get pumped per electron transferred. Estimates for *E. coli* running full denitrification (NO₃⁻ to N₂) put the yield somewhere around **24 ATP per glucose** `[verify: most recent ATP yield estimates for full denitrification in E. coli]` — still dramatically more than the third branch.

*Desulfovibrio* reduces sulfate to H₂S. Methanogens (Archaea) reduce CO₂ to methane — cow stomachs, rice paddies, anaerobic sewage digesters. *Geobacter* reduces Fe³⁺ to Fe²⁺. The electron donors and acceptors are different. The architecture is the same.

### Branch three — fermentation

No oxygen. No nitrate, no sulfate, no Fe³⁺. Nothing to put at the end of an ETC. The cell cannot run a chain. Cannot oxidize NADH back to NAD⁺. Cannot run glycolysis, because step six of glycolysis *requires* NAD⁺ as a reactant. No glycolysis, no ATP at all.

The escape is **fermentation**. The cell uses pyruvate — or a derivative of pyruvate — as its own electron acceptor. NADH dumps its electrons onto pyruvate, regenerating NAD⁺, and glycolysis can keep running. The reduced product is excreted.

Fermentation makes no new ATP. The only ATP the cell gets is the 2 net from glycolysis. But 2 ATP is better than zero, and it is enough to keep the cell alive in closed wounds, gut anaerobic pockets, sediment — wherever oxygen and alternative acceptors are absent.

Different organisms, different products:

- **Lactic acid fermentation:** pyruvate reduced to lactate. *Lactobacillus*, *Streptococcus*. Yogurt, cheese, sourdough, the burn in your muscles at the end of a sprint.
- **Ethanol fermentation:** pyruvate decarboxylated to acetaldehyde, then reduced to ethanol plus CO₂. *Saccharomyces cerevisiae*. Beer, wine, bread (CO₂ makes the dough rise; the ethanol bakes off).
- **Mixed-acid fermentation:** a cocktail of acetate, formate, ethanol, succinate, lactate, plus H₂ and CO₂. *E. coli* and other Enterobacteriaceae.
- **Butyric acid fermentation:** butyrate, acetate, H₂, CO₂. *Clostridium*. Foul-smelling, gas-producing — the chemistry of gas gangrene.
- **Propionic acid fermentation:** propionate plus CO₂. *Propionibacterium freudenreichii*. The holes in Swiss cheese (CO₂), the tang (propionate).

<!-- → [TABLE: fermentation type → organisms → products → diagnostic test or clinical context — rows for lactic, ethanol, mixed-acid, butyric, propionic, butanediol — student should be able to identify organism from product profile] -->

Fermentation products are diagnostic. The bench reference MacFaddin's *Biochemical Tests for Identification of Medical Bacteria* is essentially a catalog of which organism makes which product from which substrate. [^9] A bacterium that ferments glucose to acid and gas, ferments lactose, and produces indole is *E. coli* until the next test disproves it.

---

## The three-way comparison — and why it matters for a wound

Compare the three paths:

- **Aerobic respiration:** ~32 ATP / glucose
- **Anaerobic respiration (nitrate):** ~24 ATP / glucose
- **Fermentation:** 2 ATP / glucose

<!-- → [CHART: horizontal bar chart comparing ATP yield per glucose — aerobic respiration, anaerobic respiration (nitrate), fermentation — bars labeled with approximate values and annotated with "~15× more efficient than fermentation" for aerobic; student should immediately grasp the scale difference and understand why facultative anaerobes switch eagerly when oxygen returns] -->

Aerobic respiration extracts roughly **fifteen times more ATP per glucose** than fermentation does. This is why aerobic life dominates wherever oxygen is available. A facultative anaerobe like *E. coli* in your gut runs fermentation when oxygen is gone, but the moment oxygen returns, it switches to aerobic respiration. This is the *Pasteur effect*, one of the oldest observations in metabolic biochemistry: Pasteur noticed in the 1860s that yeast in air made less alcohol per glucose than yeast without air. They were getting more ATP from less sugar. They did not need to ferment as much.

Now hold the metabolic ladder next to a surgical textbook from 1916 and everything clicks.

A deep, closed wound — a bullet wound, a crush injury, tissue packed with dead muscle and sealed from the air — is *Clostridium perfringens* territory. Oxygen has been consumed by the patient's own cells and by aerobic bacteria. What remains is a sealed pocket of dead tissue and dissolved sugars with no electron acceptors except pyruvate. *Clostridium perfringens* is a **strict anaerobe** — it cannot run an ETC at all, kills it even when oxygen is present, and does not have the enzyme systems to detoxify reactive oxygen species. [^1]

So *Clostridium* ferments. It runs butyric acid fermentation: 2 ATP per glucose, dumping butyrate, acetate, hydrogen, and carbon dioxide into the wound. The gas inflates tissue planes — the crackle under the surgeon's fingers is gas in fascia. The toxins do the real damage. And *Clostridium* has to ferment enormous amounts of substrate to get enough ATP to grow, which is why gas gangrene lesions progress so fast.

The Allied surgeons on the Western Front called it *fermentation putride*, and they named it correctly. They did not know the biochemistry. They knew that closing the wound killed patients and opening the wound sometimes saved them. Now you can explain why: open the wound, let in oxygen, *Clostridium* dies.

The treatment is the same today. The reasoning is the same today. Debridement and exposure to air — or hyperbaric oxygen, which pressurizes dissolved O₂ in the wound tissue to levels toxic for strict anaerobes, while simultaneously powering the patient's own neutrophils (which use O₂ for the oxidative burst that kills bacteria). The randomized evidence on hyperbaric oxygen for clostridial myonecrosis is thin, but the metabolic logic is clean. [^10]

Open the wound. Bring the oxygen. The chemistry does the rest.

<!-- → [INFOGRAPHIC: sealed wound metabolic environment — cross-section of closed wound showing: O₂ depleted zone, dissolved sugars available, no alternative electron acceptors; C. perfringens fermenting glucose (2 ATP/glucose), excreting butyrate + H₂ + CO₂ into tissue planes, toxin release labeled separately; contrast panel shows same wound opened with O₂ restored and C. perfringens growth arrested — student should see the metabolic logic of debridement, not just the surgical act] -->

---

## Life beyond glucose

I have walked you through glucose because it is the most-studied substrate. But microbes will eat almost anything that has a thermodynamic gradient on it.

Group microbes by their energy source and their carbon source:

- **Chemoorganoheterotrophs** — carbon and energy from organic molecules. Every bacterium and fungus you've heard of. What I've been describing.
- **Chemolithotrophs** — energy from oxidizing *inorganic* molecules; carbon from CO₂ or organic compounds. Ammonia oxidizers (*Nitrosomonas*), nitrite oxidizers (*Nitrobacter*), sulfur oxidizers (*Thiobacillus*), iron oxidizers (*Acidithiobacillus ferrooxidans*), hydrogen oxidizers. Sergei Winogradsky discovered these organisms in the 1880s, and the discovery was a shock: a cell living on rust and air, with no organic input whatsoever.
- **Photoautotrophs** — carbon from CO₂, energy from light. Plants, algae, cyanobacteria, purple sulfur bacteria. Light drives electrons in the wrong thermodynamic direction, generating ATP and NADPH, which then fix CO₂ into sugar.
- **Photoheterotrophs** — energy from light, carbon from organic compounds. Purple nonsulfur bacteria. Small category, real category.

The taxonomy is functional, not evolutionary. Chemolithotrophs exist in Bacteria and Archaea. There are phototrophs only in Bacteria (and their descendants, the chloroplasts). There are heterotrophs in all three domains. The same metabolic trick — oxidize X, fix CO₂, use light — has been independently invented multiple times.

What unifies all of them is Mitchell's deepest insight: **the proton gradient.** Whether electrons come from glucose or ammonia or hydrogen or sunlight, whether the acceptor is oxygen or nitrate or CO₂ or NADP⁺, the cell almost universally uses the released energy to pump protons across a membrane and run a turbine on the gradient. The electron donors and acceptors vary wildly. The architectural solution is universal.

<!-- → [INFOGRAPHIC: four microbial energy strategies — chemoorganoheterotroph, chemolithotroph, photoautotroph, photoheterotroph — each shown as a flow diagram (electron source → ETC or photosystem → proton gradient → ATP synthase → ATP) with representative organisms labeled — student should see that the central ATP-synthase / proton-gradient motif is constant across all four] -->

---

## Three misconceptions worth dismantling

**"Anaerobes die in oxygen because they lack catalase."** Partially correct. Strict anaerobes generally lack catalase and superoxide dismutase, so reactive oxygen species accumulate when O₂ is present. But the picture is more complex: some anaerobes have partial defense systems and tolerate brief oxygen exposure; others die in seconds. The deeper reason is that the metalloenzymes at the heart of anaerobic metabolism — many of which have oxygen-sensitive iron-sulfur clusters — are inactivated directly by O₂, even before ROS accumulate. Saying "lacks catalase" is a first approximation. The real answer involves the core enzymes of the organism's metabolism.

**"Fermentation is glycolysis."** No. Glycolysis is the universal first step — it runs in fermenters and in aerobic respirers alike. Fermentation is what happens *after* glycolysis when there is no ETC to run. The fermentation reactions proper are the NADH-driven reductions that regenerate NAD⁺ so glycolysis can continue. Fermentation itself makes no ATP. The confusion arises because fermentation's net energy yield equals glycolysis's net yield (2 ATP per glucose), since fermentation adds nothing — it just prevents glycolysis from stalling.

**"The textbook number '38 ATP per glucose' is correct."** It was an estimate based on rounded ratios (3 ATP per NADH, 2 per FADH₂) from before the proton-to-ATP stoichiometry of ATP synthase was measured directly. Current estimates run around 30–32. The qualitative picture — aerobic respiration is dramatically more efficient than fermentation — survives the revision. The number does not. Treat 38 as a historical artifact.

---

## LLM Exercise — Chapter 5: Building a metabolism simulator

**Project:** `05-metabolism-simulator.html` — a single-page interactive that lets a student pick an organism type, a substrate, and an oxygen level, and watch ATP accumulate.

**Tool:** Claude Code (preferred) or any LLM that can write a static HTML/JS page.

### The prompt block — Show / Say / Constrain / Verify

**SHOW** (paste these references):

- Chapter 5 (this chapter), especially the three-branch metabolism section and the worked ATP-yield example
- The fermentation products table (lactic, ethanol, mixed-acid, butyric, propionic, butanediol)
- The three test organisms: strict aerobe (e.g., *Mycobacterium tuberculosis*), facultative anaerobe (*E. coli*), strict anaerobe (*Clostridium perfringens*), photoautotroph (*Anabaena*)

**SAY** (your instruction to the LLM):

> Build a single-file HTML page (no external dependencies except Chart.js from a CDN) called `05-metabolism-simulator.html`. The page lets the user:
>
> 1. Pick an organism type: strict aerobe, facultative anaerobe, strict anaerobe, phototroph.
> 2. Pick a substrate: glucose, acetate, inorganic sulfur (for chemolithotroph mode), light (for phototroph mode).
> 3. Toggle oxygen present / absent.
>
> The page should display:
> - A pathway diagram (SVG, simple boxes-and-arrows) showing which pathways are active for the current selection. Grey out inactive steps.
> - A live ATP counter that ticks up over time at a rate proportional to the predicted ATP yield (use 32 / glucose aerobic, 24 / glucose anaerobic-respiration, 2 / glucose fermentation, scaled to a sensible per-second rate).
> - A products panel showing what's being excreted (fermentation products if anaerobic + no respiration partner; CO₂ + H₂O if aerobic; etc.).
> - A bar chart (Chart.js) comparing the current condition's ATP yield to the other two main branches, updated live.
>
> Behavior rules:
> - Strict aerobe with oxygen off → no growth, ATP counter halts, display "obligate aerobe cannot respire anaerobically."
> - Strict anaerobe with oxygen on → "obligate anaerobe poisoned by oxygen — growth arrested."
> - Facultative anaerobe → smoothly switch between aerobic respiration (oxygen on) and fermentation (oxygen off). Show the switch in the diagram.
> - Phototroph with light → run photosynthesis (note: simplified — produce ATP at a phototrophic rate, output O₂).

**CONSTRAIN**:

- One file. No build step. Should open in any modern browser by double-clicking.
- ATP rates need not match real cells in absolute terms — they need to be in the right *ratios* (aerobic ≈ 15× fermentation).
- Chart.js loaded from CDN is fine. No other dependencies.
- All copy in the UI should match the chapter's vocabulary: substrate-level phosphorylation, ETC, ATP synthase, fermentation products by name.

**VERIFY** (what to check before you trust it):

- Run all four organism types in all relevant oxygen conditions. Do the impossible combinations (strict aerobe with O₂ off, strict anaerobe with O₂ on) actually halt growth?
- Confirm the aerobic-vs-fermentation ATP ratio in the bar chart sits around 15:1. If it shows 38:2 or 36:2, the LLM used old textbook numbers — push back with a follow-up prompt asking it to use 30–32 instead of 38.
- Stress-test: switch organism type mid-run. Does the diagram correctly reactivate / deactivate steps without leaving stale highlights?

### Exploration

Once the simulator runs:

1. Set the facultative anaerobe on glucose. Turn oxygen on, run thirty seconds, note ATP count. Turn oxygen off, run the same thirty seconds. Compute the ratio. Does it match 32:2 = 16:1, within reason?
2. Set the strict anaerobe on glucose, oxygen off. Watch what products accumulate. Now imagine the same cell in a wound. Connect what the simulator shows to the *Clostridium* case in this chapter.
3. Set the phototroph on light. Turn the light off. Predict what happens. Run it. Was your prediction right?

### Extension toward Chapter 6 (microbial growth)

Add a growth-curve panel to the simulator. The simulator already has an ATP rate per second. Convert that to a *biomass increase per hour* using a stoichiometric assumption (e.g., 10 ATP needed to build 1 picogram of new cell). Plot biomass over time as an exponential curve. Then compare the doubling time predicted by each metabolic mode. Use this to set up Chapter 6's discussion of generation time — the *quantitative* link between metabolism and growth rate.

---

## Exercises

**Warm-up 1 (ATP bookkeeping).** A single glucose molecule enters a bacterial cell running full aerobic respiration. Compute the ATP yield step by step: glycolysis, pyruvate decarboxylation, citric acid cycle (both turns), and electron transport chain. Use modern stoichiometry (2.5 ATP per NADH, 1.5 per FADH₂). Show each subtotal. Why does FADH₂ yield less ATP per mole than NADH? *Tests: ETC stoichiometry; understanding of why the chain entry point matters.*

**Warm-up 2 (Branch classification).** Classify each organism below as strict aerobe, facultative anaerobe, or strict anaerobe. For each, state which metabolic branch(es) it can run and what happens to its ATP yield when oxygen is removed:

a. *Mycobacterium tuberculosis*
b. *Escherichia coli*
c. *Clostridium perfringens*
d. *Desulfovibrio* (sulfate-reducer)

*Tests: aerobe/anaerobe classification; connection between oxygen availability and metabolic branch selection.*

**Application 1 (The wound).** A deep crush injury to a thigh is surgically closed before adequate debridement. Forty-eight hours later the patient develops gas gangrene. (a) Explain, in metabolic terms, why *Clostridium perfringens* — and not *Staphylococcus aureus* — predominates in this environment. (b) The surgeon opens and debrides the wound. Explain why this intervention is metabolically targeted, not merely hygienic. (c) Hyperbaric oxygen is added as adjunctive therapy. What does elevated dissolved O₂ do to *Clostridium*'s metabolism? *Tests: strict anaerobe metabolism; clinical application of the fermentation vs. respiration framework.*

**Application 2 (Selective toxicity, extended).** Trimethoprim (TMP) inhibits dihydrofolate reductase — the enzyme one step downstream of the sulfonamide target in folate biosynthesis. (a) TMP and sulfonamides are frequently co-prescribed as TMP/SMX. Why does the combination produce a larger antibacterial effect than either drug alone? (b) Humans also have a dihydrofolate reductase. Why doesn't TMP kill human cells? (c) Using what you know about fermentation products and organism classification, predict whether TMP/SMX would be equally effective against a strict anaerobe grown without oxygen. Explain your reasoning. *Tests: enzyme inhibition; selective toxicity mechanism; connection between metabolic state and antibiotic efficacy.*

**Application 3 (Fermentation fingerprinting).** A clinical isolate from a patient's urine produces gas and acid from glucose, ferments lactose, gives a positive indole test, and excretes acetate, formate, ethanol, succinate, and lactate when grown anaerobically. (a) What fermentation pattern is this? (b) Which genus is most consistent with these results? (c) What single additional test would you run to narrow the identification further, and what result would distinguish a positive from a negative? *Tests: fermentation product profiles as diagnostic tools.*

**Synthesis 1 (Pasteur effect, quantitative).** A facultative anaerobe is consuming 1 mmol glucose per hour under aerobic conditions. Oxygen is then removed. (a) Using 32 ATP/glucose (aerobic) and 2 ATP/glucose (fermentation), compute the factor by which glucose consumption must increase for the cell to maintain the same ATP production rate. (b) As a consequence, predict what happens to the concentration of fermentation products in the medium. (c) Pasteur observed that yeast in air made less alcohol per glucose than yeast without air. Connect this observation to your calculation. *Tests: integration of ATP yield differences with real metabolic consequences; the Pasteur effect as quantitative prediction.*

**Synthesis 2 (Design a chemolithotroph).** A hypothetical bacterium uses hydrogen gas (H₂) as its electron donor and oxygen as its terminal electron acceptor, fixing CO₂ for carbon. (a) Which of the four metabolic categories does this organism fall into? (b) Sketch the architecture of its energy metabolism — does it need glycolysis? A citric acid cycle? What does it need that *E. coli* doesn't? (c) The reduction of O₂ has a much higher redox potential than the oxidation of H₂. What does this tell you about the potential ATP yield relative to glucose-based aerobic respiration? (d) Look up *Knallgas bacteria* (hydrogen-oxidizing bacteria). How does the actual metabolism compare to your sketch? *Tests: functional metabolic taxonomy; ETC architecture; Mitchell's proton-gradient universality.*

**Challenge (Misconception audit).** A classmate argues: "Fermenters are metabolically inferior to aerobes — they make less ATP, grow more slowly, and will always be outcompeted when oxygen is present." Evaluate this claim. Identify what is correct in it, what is oversimplified, and at least one ecological context in which the fermenter has a decisive advantage over the aerobe. Your answer should address ATP yield, growth rate under oxygen-limited conditions, and the evolutionary success of obligate anaerobes in specific environments. *Tests: critical evaluation; understanding that metabolic strategy fitness is context-dependent, not absolute.*

---

## What would change my mind

If a substantial fraction of clinically important strict anaerobes turn out to die in oxygen primarily because their core fermentation metalloenzymes are oxygen-inactivated — rather than because of ROS damage from absent catalase / superoxide dismutase — then the *Clostridium* clinical reasoning in this chapter shifts toward metalloenzyme chemistry rather than antioxidant defense, and the hyperbaric oxygen rationale needs a partial rewrite. `[verify: current consensus on the molecular basis of strict-anaerobe oxygen sensitivity in clinical isolates]`

## Still puzzling

I do not understand why the proton motive force settled on roughly the values it has across all domains — about –200 mV transmembrane, give or take. There is presumably a physical optimum (higher gradients leak more; lower gradients cannot drive ATP synthase efficiently), but I have not seen a derivation from first principles that satisfies me.

I am also not satisfied with the standard explanation for why mitochondrial electron transport chains leak single electrons onto oxygen at the rate they do, producing reactive oxygen species the cell then has to detoxify. The system has the smell of an evolutionary kludge — but I cannot rule out that the leak is itself adaptive (ROS as signaling molecules) rather than a flaw to be lived with.

---

**Tags:** microbial-metabolism, glycolysis, electron-transport-chain, sulfonamides, clostridium-perfringens

---

## References

[^1]: Bryant, A. E. and Stevens, D. L., "Clostridial myonecrosis: new insights in pathogenesis and management," *Current Infectious Disease Reports* 12, no. 5 (2010): 383–391. doi:10.1007/s11908-010-0127-y. For First World War surgical context see Henry M. W. Gray, *The Early Treatment of War Wounds* (London: Henry Frowde / Hodder & Stoughton, 1919). `[verify: edition and pagination]`

[^2]: Ingram, V. M., "A specific chemical difference between the globins of normal human and sickle-cell anemia haemoglobin," *Nature* 178, no. 4537 (1956): 792–794.

[^3]: Wolfenden, R. and Snider, M. J., "The depth of chemical time and the power of enzymes as catalysts," *Accounts of Chemical Research* 34, no. 12 (2001): 938–945. doi:10.1021/ar000058i.

[^4]: Domagk, G., "Ein Beitrag zur Chemotherapie der bakteriellen Infektionen," *Deutsche Medizinische Wochenschrift* 61, no. 7 (1935): 250–253. Mechanism worked out by Donald Woods: Woods, D. D., "The relation of *p*-aminobenzoic acid to the mechanism of the action of sulphanilamide," *British Journal of Experimental Pathology* 21 (1940): 74–90.

[^6]: Standard free energy of ATP hydrolysis under cellular conditions is closer to –50 to –60 kJ/mol than the textbook –7.3 kcal/mol; the textbook figure is ΔG°' at standard conditions. See Nelson, D. L. and Cox, M. M., *Lehninger Principles of Biochemistry*, 8th ed. (W. H. Freeman, 2021), Chapter 13.

[^7]: Mitchell, P., "Coupling of phosphorylation to electron and hydrogen transfer by a chemi-osmotic type of mechanism," *Nature* 191 (1961): 144–148. doi:10.1038/191144a0.

[^8]: Hinkle, P. C., "P/O ratios of mitochondrial oxidative phosphorylation," *Biochimica et Biophysica Acta* 1706, no. 1–2 (2005): 1–11. doi:10.1016/j.bbabio.2004.09.004.

[^9]: MacFaddin, J. F., *Biochemical Tests for Identification of Medical Bacteria*, 3rd ed. (Lippincott Williams & Wilkins, 2000).

[^10]: Levett, D., Bennett, M. H., and Millar, I., "Adjunctive hyperbaric oxygen for necrotizing fasciitis," *Cochrane Database of Systematic Reviews* (2015), Issue 1. CD007937. doi:10.1002/14651858.CD007937.pub2. `[verify: most recent update through 2026]`

---

**Bridge to Chapter 6.** Metabolism determines how much ATP a cell can make per unit time. Chapter 6 turns that rate into a growth curve — the exponential, the lag, the plateau, and what each phase tells you about what the organism needs.
