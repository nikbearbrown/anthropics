# Chapter 08 — Microbial Metabolism

*Metabolism is what a cell does so it can keep doing it.*

## The question before the answer

Hold a glucose molecule in your hand. (Imagine one. They are too small to actually hold.) The molecule has six carbon atoms, twelve hydrogens, six oxygens. It contains, in the energetic relationships between those atoms, about 686 kilocalories of chemical energy per mole — energy that becomes available when the molecule is broken down to carbon dioxide and water.

A cell that wants to use that energy has a problem. Burning the glucose directly would release the energy all at once as heat, which is fine for a fire but useless for a cell. The cell needs the energy to be released in small steps, each step pulling off a manageable amount of energy that can be captured and stored, with as little wasted as heat as possible.

That is what cellular metabolism is. It is a procedure for taking a high-energy molecule apart in small, controlled steps, capturing the released energy in a form the cell can use (ATP), and using the resulting electrons to build other molecules the cell needs or to drive the engine that makes more ATP.

This chapter walks through that procedure for the most studied case — the oxidation of glucose to CO₂ and water — and shows how the same logic, in modified form, applies to every metabolism known: from a methanogen in a cow's gut making energy from CO₂ and H₂, to a photosynthetic cyanobacterium making sugar from light, to your own muscle cells running a marathon.

If you understand glycolysis, the Krebs cycle, the electron transport chain, and chemiosmosis, you understand maybe 80% of the energy economy of life on Earth.

## Learning objectives

By the end of this chapter, you will be able to:

1. Distinguish autotrophs from heterotrophs and explain how each gets carbon and energy.
2. Describe the role of ATP, NAD⁺/NADH, and FAD/FADH₂ as energy currency and electron carriers.
3. Trace one glucose molecule through glycolysis, the Krebs cycle, and the electron transport chain, and count the ATP produced.
4. Explain chemiosmosis as the mechanism by which an electrochemical gradient produces ATP.
5. Describe fermentation as a strategy when oxygen is unavailable and identify which microbial pathways produce which fermentation end products.
6. Describe the light-dependent and light-independent reactions of photosynthesis.

Prerequisites: Chapter 7 in particular, plus Chapters 1–6.

## How to classify a metabolism

Living things differ in two metabolic variables that turn out to matter most: where they get their **carbon**, and where they get their **energy**.

For carbon, there are two strategies:

- **Autotrophs** ("self-feeders") build their own organic molecules from inorganic carbon — mostly CO₂. They include all plants, all algae, the photosynthetic bacteria, and chemoautotrophs that use inorganic chemical reactions to fix carbon.
- **Heterotrophs** ("other-feeders") cannot fix CO₂; they take in preformed organic molecules and break them down. They include all animals, all fungi, most protists, and most bacteria.

For energy, there are also two strategies:

- **Phototrophs** harvest light. Plants, algae, cyanobacteria, and various other photosynthetic bacteria.
- **Chemotrophs** harvest chemical energy by oxidizing reduced compounds. Most heterotrophs are chemoorganotrophs (they oxidize organic compounds — glucose, fatty acids, amino acids). Some bacteria are chemolithotrophs (they oxidize inorganic compounds — ammonia, sulfide, hydrogen, iron).

Combine the two axes and you get four metabolic types: photoautotroph (cyanobacteria, plants), photoheterotroph (purple nonsulfur bacteria), chemoautotroph (nitrifying bacteria, sulfur oxidizers), chemoheterotroph (you, *E. coli*, *Saccharomyces*, fungi).

This taxonomy is functional. It does not align with the three-domain phylogenetic taxonomy from Chapter 1. There are autotrophs and heterotrophs in all three domains. There are chemotrophs in all three. Metabolism evolved many times in many lineages, and similar strategies appear in distant relatives. It is the metabolism, more than the phylogeny, that determines where an organism can live.

## Redox: where the energy is

All metabolism is, at the chemistry level, electron transfer.

A molecule that loses an electron is **oxidized**. A molecule that gains an electron is **reduced**. Electrons do not move in solution alone; they are transferred from one molecule to another in coupled redox reactions. The molecule that loses electrons is the *reductant* (or electron donor); the one that gains them is the *oxidant* (or electron acceptor).

When a reduced molecule (with many high-energy electrons) is oxidized to a less reduced form, energy is released. The energy released depends on the difference in electron affinity between the donor and acceptor — the larger the gap, the more energy. Oxygen is a particularly good electron acceptor; the reduction of O₂ to water has a large electron-affinity gap, which is why aerobic respiration extracts more energy per glucose than any anaerobic alternative.

A cell does not just dump electrons onto oxygen, though. That would release all the energy as heat. The trick is to pass electrons through a chain of intermediate carriers, each of which has an electron affinity intermediate between the donor and the final acceptor. Each transfer releases a small amount of energy, which the cell can capture.

The most important electron carriers are NAD⁺ and FAD. **NAD⁺** (nicotinamide adenine dinucleotide) accepts two electrons and a proton to become NADH. **FAD** (flavin adenine dinucleotide) accepts two electrons and two protons to become FADH₂. The reduced forms — NADH and FADH₂ — are mobile electron carriers; they pick up electrons from one place in the cell and deliver them to another. NADH carries about 53 kcal/mol of usable energy in its electrons; FADH₂ carries about 45 kcal/mol.

The energy currency itself is **ATP** (adenosine triphosphate). ATP has three phosphate groups. The bonds between phosphates are high-energy bonds; hydrolyzing the terminal one to release ADP plus inorganic phosphate releases about 7.3 kcal/mol — enough to drive most cellular work. The reverse reaction — adding a phosphate back to ADP to make ATP — requires that 7.3 kcal/mol be supplied from somewhere else, and this is exactly where metabolism's released energy goes.

A cell at rest uses something like 10⁷ molecules of ATP per second per cell. The pool of ATP is small; the turnover is fast. ATP is not stored; it is constantly being made and used.

## Glycolysis

The breakdown of glucose begins with **glycolysis** — from the Greek for "sugar splitting." It happens in the cytoplasm of every cell on Earth that uses glucose, which is most cells. It does not require oxygen. It is one of the most universal biochemical pathways known.

Glycolysis has ten enzymatic steps. The net result is one molecule of glucose (6 carbons) being split into two molecules of pyruvate (3 carbons each), with a net production of 2 ATP and 2 NADH per glucose.

The first half of glycolysis costs energy: the cell invests 2 ATP to phosphorylate glucose and a subsequent intermediate, priming the molecule for the splitting reaction. The second half pays off: pyruvate kinase and the other downstream enzymes generate 4 ATP, and the oxidation of a key intermediate (glyceraldehyde-3-phosphate) reduces 2 NAD⁺ to 2 NADH. Net: 2 ATP and 2 NADH per glucose.

ATP made directly by an enzymatic reaction, as in glycolysis, is called **substrate-level phosphorylation**. The enzyme transfers a phosphate directly from a high-energy substrate to ADP. It is one of two ways ATP gets made in cells. The other, much more productive way, is **oxidative phosphorylation** — see below.

Pyruvate is a fork in the road. What happens to it next depends on whether oxygen is available.

## With oxygen: pyruvate to the Krebs cycle

If oxygen is available, pyruvate is taken up by mitochondria (in eukaryotes) or processed at the plasma membrane (in prokaryotes), and converted into a two-carbon molecule called **acetyl-CoA**, releasing CO₂ and reducing NAD⁺ to NADH in the process.

Acetyl-CoA enters the **Krebs cycle** (also called the citric acid cycle or TCA cycle), a series of eight reactions that completely oxidize the acetyl group to two molecules of CO₂. Each turn of the Krebs cycle produces 3 NADH, 1 FADH₂, and 1 ATP (or GTP, an equivalent currency). Two turns of the cycle per glucose, since each glucose produces two pyruvates and therefore two acetyl-CoAs.

So far, per glucose, the cell has made:

- 2 ATP and 2 NADH from glycolysis
- 2 NADH from pyruvate → acetyl-CoA
- 6 NADH, 2 FADH₂, 2 ATP from two turns of the Krebs cycle

The carbons of glucose have all been released as CO₂. The energy of glucose has been captured almost entirely in the reduced electron carriers (10 NADH, 2 FADH₂) and a small amount in ATP (4 total so far). The next step is to convert the electron-carrier energy to ATP.

## The electron transport chain and chemiosmosis

Here is where it gets beautiful.

The reduced electron carriers (NADH, FADH₂) deliver their electrons to a series of protein complexes embedded in the inner membrane of the mitochondrion (in eukaryotes) or in the plasma membrane (in prokaryotes). These complexes are the **electron transport chain** (ETC).

The ETC has four major complexes (Complexes I, II, III, IV) connected by mobile electron carriers (ubiquinone, cytochrome c). Electrons enter at Complex I (from NADH) or Complex II (from FADH₂) and pass down a chain of carriers with progressively higher electron affinity. At the end, Complex IV transfers four electrons to molecular oxygen plus four protons to make two water molecules. Oxygen is the final electron acceptor; water is the byproduct.

As electrons flow down the chain, the complexes (I, III, and IV) use the released energy to pump protons from the matrix side of the membrane to the outer side. The proton pumping is the crucial move. It creates an electrochemical gradient across the inner membrane — protons accumulate on the outer side (the intermembrane space, in mitochondria), making it more positive and more acidic than the matrix side.

That gradient — the difference in proton concentration and electrical charge across the membrane — is **stored energy**. Peter Mitchell, in 1961, proposed that this proton gradient was the link between electron transport and ATP synthesis. The hypothesis was called **chemiosmosis**, and it was so heretical that Mitchell could not get a grant to test it for ten years. He set up his own private laboratory in a converted manor house and pursued the work himself. By the late 1970s, his hypothesis was confirmed. He won the Nobel Prize in 1978. [^1]

The mechanism is this: the inner membrane contains an enzyme called **ATP synthase**, a stunning piece of biological machinery. It has two parts: a hydrophobic stalk embedded in the membrane (Fo) and a hydrophilic head exposed to the matrix (F1). Protons flow back across the membrane down their concentration gradient through the Fo part. The flow causes the Fo to rotate. The rotation is mechanically coupled to the F1 head, which contains three active sites that bind ADP and inorganic phosphate. The rotation drives the active sites through a sequence of conformations that catalyzes the synthesis of ATP.

Read that again. ATP synthase is a molecular motor. The flow of protons turns a rotor. The rotor drives ATP synthesis. The cell is running a turbine.

↳ **Dig Deeper — The mechanical detail of ATP synthase**

*ATP synthase is one of the most beautiful molecular machines in biology. The rotational mechanism was inferred in the 1990s and later visualized directly.*

**Prompt:**
> Describe the structure and rotational mechanism of ATP synthase in detail. Cover the F0 portion (membrane-embedded c-ring rotor), the F1 portion (alpha-3 beta-3 catalytic head), the central stalk (gamma subunit), and the peripheral stalk (b subunit). Explain how proton flow drives c-ring rotation and how that mechanical motion converts to chemical bond formation in the F1 head. End by describing the Boyer "binding change" mechanism and the experimental evidence for it.

**What to do with the output:** This is one of those mechanisms that becomes more impressive the more you understand it. Read it with the chapter's "the cell is running a turbine" line in mind — the turbine analogy is literal, not metaphorical.

The yield is approximately 1 ATP per 4 protons pumped through ATP synthase. Each NADH produces enough proton pumping to make about 2.5 ATP. Each FADH₂ produces about 1.5 ATP.

Adding it up for a single glucose, completely oxidized aerobically:

- Glycolysis: 2 ATP (substrate-level) + 2 NADH (→ ~5 ATP through ETC) = 7
- Pyruvate to acetyl-CoA: 2 NADH (→ 5 ATP) = 5
- Krebs cycle: 2 ATP (substrate-level) + 6 NADH (→ 15) + 2 FADH₂ (→ 3) = 20

Total: about 32 ATP per glucose under ideal conditions. The textbook number you sometimes see (36 or 38) is older and uses rounded ratios. The current estimate, with better proton-to-ATP measurements, is around 30–32.

Glycolysis on its own — without oxygen — produces 2 ATP per glucose. With oxygen and full oxidative phosphorylation, the cell produces 30–32. The yield is fifteen to sixteen times higher with oxygen than without. This is why aerobic life dominates wherever oxygen is available.

## Without oxygen: fermentation

When oxygen is unavailable — in a flooded soil, in the depths of a cheese, in your muscle during sprinting — the electron transport chain cannot run. Without ETC, the cell cannot regenerate NAD⁺ from NADH. Without NAD⁺, glycolysis stops. Without glycolysis, the cell makes no ATP at all.

The solution is **fermentation**: a way of regenerating NAD⁺ without using the ETC.

In fermentation, pyruvate (or a derivative of it) is reduced by NADH, regenerating NAD⁺. The reduced product is excreted. The cell makes no new ATP from this step; the only ATP made is the 2 per glucose from glycolysis. But glycolysis can keep running, which is better than no ATP at all.

Different organisms use different fermentation products. The product depends on what enzymes the organism has.

- **Lactic acid fermentation**: pyruvate is reduced to lactate. Used by *Lactobacillus* (yogurt), *Streptococcus* (cheese), and by your muscle cells under heavy exertion. The lactate that accumulates in your muscles during sprinting is from this pathway. It is also what makes sourdough sour.

↳ **Dig Deeper — The Warburg effect and cancer metabolism**

*Many cancer cells preferentially use glycolysis with lactate fermentation even when oxygen is available. Otto Warburg noticed this in the 1920s. The explanation is still incomplete.*

**Prompt:**
> Describe the Warburg effect — aerobic glycolysis in cancer cells — and the leading hypotheses for why cancer cells choose this less energetically efficient pathway. Cover Warburg's original observations, the modern reframing in terms of biosynthetic precursors (glycolytic intermediates feeding lipid and nucleotide synthesis), and the proposed therapeutic implications (targeting cancer metabolism with drugs like 2-deoxyglucose). End by noting where the field is currently — is the Warburg effect a cause, a symptom, or a side effect of cancer cell biology?

**What to do with the output:** Microbial metabolism and human cancer metabolism share more vocabulary than the chapter implies. The pathways are the same; the regulation is what differs.
- **Ethanol fermentation**: pyruvate is decarboxylated (losing CO₂) and then reduced to ethanol. Used by *Saccharomyces cerevisiae* (yeast). The CO₂ released is what makes bread rise. The ethanol is what makes beer.
- **Propionic acid fermentation**: produces propionic acid and CO₂. *Propionibacterium freudenreichii* in Swiss cheese produces these as byproducts; the CO₂ makes the holes, and the propionic acid contributes to the flavor.
- **Mixed-acid fermentation**: produces a mix of acetate, ethanol, lactate, succinate, formate, plus H₂ and CO₂. *E. coli* and other enterics.
- **Butanediol fermentation**: produces 2,3-butanediol plus other products. Used by *Klebsiella* and *Enterobacter*.

The fermentation products are useful diagnostically. The classic IMViC tests (Indole, Methyl Red, Voges-Proskauer, Citrate) used to distinguish *E. coli* from *Enterobacter* depend on differences in fermentation pathways.

Some bacteria can do **anaerobic respiration**: using something other than oxygen as the final electron acceptor in an ETC. Common alternative acceptors include nitrate (reduced to nitrite, nitrous oxide, or N₂), sulfate (reduced to hydrogen sulfide), or CO₂ (reduced to methane, by methanogens). The energy yield is less than aerobic respiration but more than fermentation, because there is still an ETC and chemiosmosis, just with a less powerful final acceptor.

## Photosynthesis, briefly

Phototrophic organisms reverse the energy flow. They use light to drive an electron transport chain in the wrong direction — pumping electrons from water (a poor electron donor) up to NADP⁺ (a strong reductant), producing NADPH and ATP. The NADPH and ATP are then used to fix CO₂ into sugars.

Photosynthesis has two halves:

**Light-dependent reactions**. Two photosystems (PSII and PSI) absorb photons. PSII strips electrons from water (releasing O₂ as a byproduct) and pumps them through an ETC, generating ATP via chemiosmosis. The electrons emerge from PSI with enough energy to reduce NADP⁺ to NADPH. The output: ATP and NADPH; the byproduct: O₂. This is *non-cyclic photophosphorylation*. Some bacteria can run a cyclic version (PSI only) that makes ATP without NADPH.

**Light-independent reactions** (the Calvin cycle). The ATP and NADPH from the light reactions power the fixation of CO₂. Rubisco — ribulose-1,5-bisphosphate carboxylase/oxygenase — catalyzes the addition of CO₂ to a five-carbon sugar, producing two three-carbon molecules. These are then rearranged, with more ATP and NADPH consumed, into glucose. Rubisco is one of the most abundant proteins on Earth, possibly the most abundant single protein.

In cyanobacteria, both halves happen in one cell. In plants and algae, the light reactions happen in chloroplast thylakoid membranes; the Calvin cycle happens in the chloroplast stroma. The mitochondrion-style and chloroplast-style ETCs are evolutionarily related — both descended from the proton-pumping machinery of bacterial ancestors.

## Other catabolic pathways

Cells do not only oxidize glucose. They oxidize fatty acids (via beta-oxidation, which chops two carbons off the end of a fatty acid chain and feeds each fragment into the Krebs cycle as acetyl-CoA). They oxidize amino acids (by removing the amino group and feeding the carbon skeleton into glycolysis or the Krebs cycle). They can metabolize polysaccharides (broken down to monomers, then into glycolysis), lipids, even some unusual sources like phenolic compounds or hydrocarbons.

The unifying principle: most catabolic pathways funnel into either glycolysis or the Krebs cycle. Once a molecule is converted to glucose-6-phosphate or to acetyl-CoA, it follows the same downstream chemistry as everything else.

This convergence is why microbial metabolism is so flexible. A bacterium that can break down lipids and a bacterium that can ferment lactose are both, after the substrate-specific first few enzymatic steps, using the same downstream machinery. Evolutionarily, this means a small genetic change — acquiring a new enzyme for the first few steps — can give a bacterium access to a new substrate. We will see this in Chapter 11.

## Biogeochemical cycles

The metabolic activities of microorganisms drive the planetary cycles of carbon, nitrogen, sulfur, and other elements.

**Carbon cycle**. Photosynthesis fixes atmospheric CO₂ into organic carbon. Respiration (by all aerobic organisms, including bacteria and fungi) returns CO₂ to the atmosphere. Methanogens convert organic carbon to methane. Methanotrophs convert methane back to CO₂. The cycle is in dynamic equilibrium; human burning of fossil fuels has perturbed it on a timescale faster than the natural cycle can adjust.

**Nitrogen cycle**. Atmospheric N₂ is biologically inert. Nitrogen fixation — converting N₂ to ammonia (NH₃) — is done almost exclusively by prokaryotes (some free-living, some symbiotic with plant roots like *Rhizobium*). Nitrification converts ammonia through nitrite to nitrate. Denitrification reduces nitrate back to N₂, returning it to the atmosphere. The Haber-Bosch industrial process — which fixes about half of all the nitrogen now used by humans — was an industrial replacement for biological nitrogen fixation; it consumes about 1% of global energy production.

↳ **Dig Deeper — Nitrogenase, the enzyme we still haven't reproduced**

*Biological nitrogen fixation happens at room temperature and atmospheric pressure. Haber-Bosch requires 400°C and 200 atmospheres. Why is the enzyme so much better than the industrial process?*

**Prompt:**
> Describe the structure and mechanism of the nitrogenase enzyme. Cover the iron-molybdenum cofactor (FeMoco), the electron transfer required (8 electrons per N₂), the ATP consumption (16 ATP per N₂), and the strict oxygen sensitivity. Why has it been so difficult to make a biomimetic nitrogen-fixing catalyst that works under mild conditions? What are the current frontiers (synthetic biology approaches to engineering nitrogen fixation into cereals, alternative cofactors)?

**What to do with the output:** This is one of the great unfinished problems in catalysis. The agricultural and climate implications of a low-energy nitrogen fixation catalyst would be enormous. Save the answer; come back when biotechnology in Chapter 12 is discussed.

**Sulfur cycle**. Sulfur-reducing and sulfur-oxidizing bacteria interconvert sulfate, elemental sulfur, and hydrogen sulfide. These are not visible to most of biology but are major players in deep-ocean and sediment ecology.

Bioremediation — using microorganisms to clean up pollutants — works because some bacteria can degrade unusual compounds. Oil-eating bacteria break down hydrocarbons. Some bacteria can transform toxic mercury into a less toxic form. The capacities of microbial metabolism are wider than the capacities of any other class of organisms, by a wide margin, and bioremediation is the engineering application of that fact.

## What the chapter is really about

Metabolism is the chemistry of staying alive. Every cell is constantly extracting energy from its environment — either from light or from reduced chemicals — and using that energy to build the molecules it needs, to maintain its boundaries, and to make more of itself. The chemistry of glycolysis and the Krebs cycle and the ETC are not arbitrary; they are the best procedures evolution has found for extracting energy from glucose, and they have been conserved across all three domains of life for over three billion years.

The Mitchell chemiosmotic hypothesis is, in my view, the single most beautiful idea in biology. The thought that a cell builds an electrochemical gradient across a membrane and then runs a turbine on the gradient to make ATP is — there is no better word — clever. It is the kind of trick a brilliant engineer might come up with. The fact that this trick is the same in mitochondria, in chloroplasts, and in the bacterial ancestors of both, across all three domains, suggests that it arose very early and has been good enough that nothing else has displaced it.

When you read about a new metabolism — chemolithotrophic iron oxidizers, sulfate reducers, ammonia oxidizers — look for the proton gradient. It is almost always there. Different electron donors, different electron acceptors, different membranes, but the same mechanism: an electron flow that produces a proton gradient that produces ATP. The chemistry is universal.

## Still puzzling

I do not understand why cells produce reactive oxygen species (ROS) at the rate they do. Mitochondrial respiration leaks single electrons onto oxygen periodically, producing superoxide and hydrogen peroxide as byproducts. These are damaging; cells have evolved extensive antioxidant defenses (superoxide dismutase, catalase, glutathione) to deal with them. The system has the smell of a kludge — a metabolism that mostly works elegantly but generates dangerous intermediates that have to be mopped up. Why didn't evolution find a tighter coupling? I would expect that, given billions of years, a less leaky electron transport chain would be possible. I do not know whether the leakiness is unavoidable physical chemistry or just an evolutionary accident.

## What would change my mind

The bookkeeping of how many ATP per glucose are produced under aerobic respiration has been revised downward over the past few decades — from 38 to 36 to about 30–32 — as the actual proton-pumping stoichiometries have been measured more carefully. If the next round of measurements yields significantly different numbers (say, 25 or 35), I would have to update the energy comparisons I have made between aerobic and anaerobic metabolism. The qualitative picture (aerobic is much better) would survive; the quantitative numbers would change. `[verify: most recent consensus on ATP yield per glucose in aerobic respiration]`

## LLM exercises

1. **Counting ATP, the hard way.** Have the LLM trace one glucose molecule through glycolysis, pyruvate oxidation, the Krebs cycle, and oxidative phosphorylation. Ask it to identify, at each step, how many ATP, NADH, and FADH₂ are produced, then convert the electron carriers to ATP. Compare its total to the textbook number and discuss the assumptions.
2. **Why chemiosmosis.** Ask the LLM to explain why a cell makes ATP via chemiosmosis rather than directly coupling electron transport to ATP synthesis. Press on what advantages the gradient-and-turbine arrangement has over a direct mechanism. Then ask what disadvantages.
3. **A new metabolism.** Tell the LLM that a hypothetical bacterium uses iron(II) as its electron donor and oxygen as its electron acceptor. Ask it to sketch the electron transport chain for this organism, calculate roughly how much energy is available per iron oxidation, and estimate ATP yield per electron. Then look up *Acidithiobacillus ferrooxidans* and compare.
4. **The brewing yeast.** Ask the LLM what fermentation products *Saccharomyces cerevisiae* makes from glucose under anaerobic conditions. Then ask what happens to the yeast if you add oxygen — does it switch to aerobic respiration? Why or why not? (This is the Pasteur effect; the LLM may or may not name it.)
5. **Bioremediation.** Ask the LLM to design a microbial consortium for cleaning up an oil spill on a beach. What organisms would you want? What conditions would you need to provide? What are the limits of the approach? Compare to actual oil-spill cleanup efforts.

## References

[^1]: Mitchell, P. "Coupling of phosphorylation to electron and hydrogen transfer by a chemi-osmotic type of mechanism." *Nature* 191 (1961): 144–148. doi:10.1038/191144a0. Nobel Lecture: Mitchell, P. "David Keilin's Respiratory Chain Concept and Its Chemiosmotic Consequences." Nobel Lecture, 8 December 1978. https://www.nobelprize.org/prizes/chemistry/1978/mitchell/lecture/
---

## LLM Exercise — Chapter 8: Microbial Metabolism (Microbe Profile Database Project)

**Project:** Microbe Profile Database.
**What you're building this kapter:** metabolism fields + 2 entries with notable metabolism (anaerobic + fermentation).
**Tool:** **Cowork**.

---

**The Prompt:**

```
Chapter 8 of my Microbe Database project. Chapter 8 covered
microbial metabolism — chemoheterotrophs (energy from chemicals,
carbon from organic), photoautotrophs (energy from light, carbon
from CO2), chemoautotrophs (energy from inorganic chemicals);
aerobic respiration (full oxidation, 38 ATP per glucose); anaerobic
respiration (electron acceptors other than O2 — nitrate, sulfate,
ferric iron); fermentation (no ETC, partial oxidation, alcoholic vs.
lactic acid vs. mixed acid).

Schema additions:
- **Metabolism_type**: chemoheterotroph / photoautotroph /
  chemoautotroph / chemoorganotroph etc.
- **Energy_strategy**: aerobic-respiration / anaerobic-respiration
  (specify electron acceptor) / fermentation (specify products) /
  combination.
- **Fermentation_products**: lactic acid / ethanol / mixed acids /
  butyric acid / etc. (only fill if fermentation is used).

Backfill these for existing entries. Notable ones to populate:
- *S. cerevisiae*: chemoheterotroph; aerobic respiration; alcoholic
  fermentation (anaerobic).
- *E. coli*: facultative anaerobe; mixed-acid fermentation.
- *Mycobacterium tuberculosis*: obligate aerobe; chemoheterotroph.
- *Halobacterium salinarum*: chemoheterotroph but has bacterio-
  rhodopsin (light-driven proton pump); unique strategy.

Add 2 new entries with notable metabolism:
1. **Clostridium difficile** — obligate anaerobe (dies in O2);
   spore-former; butyric acid + other mixed-acid fermentation;
   pseudomembranous colitis pathogen.
2. **Lactobacillus acidophilus** — Gram-positive, microaerophilic,
   lactic-acid fermentation; component of probiotics + vaginal
   microbiome.

End with: query test — "all obligate anaerobes in my database."
How many? Does the answer reveal anything about clinical contexts
where anaerobic infection should be suspected (deep wounds,
abscesses, etc.)?
```

---

**What this produces:** Metabolism fields + 2 new entries. Database ~25-29 entries.

**Connection to previous chapters:** Ch 4's bacterial entries get their metabolism populated.

**Preview of next chapter:** Chapter 9 adds growth fields (temperature optima, pH, nutrient requirements, generation time) and 1-2 entries notable for unusual growth conditions.


---

## AI Wayback Machine

**Sergei Winogradsky** was founded microbial ecology in the 1880s — discovering chemolithotrophy and showing bacteria could fix CO2 without sunlight.

**Run this:**

```
Who is Sergei Winogradsky, and how does their work connect to microbial metabolism we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Sergei Winogradsky"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Sergei Winogradsky's ideas to a contemporary microbiology problem.
- Add a constraint: "Answer including criticisms or limits of Sergei Winogradsky's framework."

What changes? What gets better? What gets worse?
