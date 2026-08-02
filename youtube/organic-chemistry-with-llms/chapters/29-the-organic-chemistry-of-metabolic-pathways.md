# Chapter 29 — The Organic Chemistry of Metabolic Pathways

*Every reaction in metabolism is a reaction we've already covered. The remarkable thing is how cells stitch them together — into ten-step pathways with regulated flow, controlled by enzymes that turn on and off in response to demand.*

A typical cell is running thousands of chemical reactions simultaneously. Together they constitute *metabolism* — the network of reactions that extracts energy from food, builds the molecules a cell needs, and disposes of waste. If you traced one carbon atom from a slice of bread through your body, you'd watch it move through dozens of enzymes and transformations: starch → glucose → glucose-6-phosphate → fructose-6-phosphate → fructose-1,6-bisphosphate → glyceraldehyde-3-phosphate → pyruvate → acetyl-CoA → citrate → α-ketoglutarate → succinyl-CoA → ... and eventually CO₂ exhaled out the lungs, with the energy released along the way captured as ATP and used to do biological work.

This chapter walks through a few major metabolic pathways and shows how they are, mechanistically, just sequences of organic reactions we've covered in earlier chapters. The aldol condensations of Chapter 23. The β-elimination of Chapter 11 (E1cB, in fatty acid biosynthesis). The reductions of Chapter 19 (NADH delivers hydride). The acyl substitutions of Chapter 21 (claisen condensations are everywhere). When you see it framed this way, biochemistry stops being a distinct subject and becomes organic chemistry applied at scale, with enzymes as catalysts.

## Catabolism vs. anabolism

*Catabolism*: the breakdown of large molecules into smaller ones, with release of energy. Glucose → CO₂ + H₂O + energy.

*Anabolism*: the synthesis of larger molecules from smaller ones, with consumption of energy. Amino acids → protein, requiring ATP.

The two flow in opposite directions but share many intermediates — the same metabolites can be in catabolic or anabolic pathways depending on cell state and regulation.

Most catabolic pathways converge on a small set of common intermediates:
- Acetyl-CoA (a thioester of acetate with coenzyme A): the "fuel molecule" that enters the citric acid cycle.
- Pyruvate: the end product of glycolysis.
- α-Ketoglutarate, oxaloacetate, succinyl-CoA: TCA cycle intermediates.

Most anabolic pathways branch off from these same intermediates — using them as starting materials to build new biomolecules.

The energy of metabolism is captured in two main forms:
- ATP (adenosine triphosphate): the cellular "energy currency." The bond between the second and third phosphates has a high energy of hydrolysis (about 30 kJ/mol). Hydrolysis to ADP releases energy that can drive other reactions.
- NADH (and FADH₂): the electron carriers. Reduced from NAD⁺ (and FAD) during catabolic oxidations. Re-oxidized in oxidative phosphorylation, producing more ATP.

## ATP and how it powers reactions

ATP has three phosphate groups in series — α (closest to the ribose), β, γ. The β-γ bond is a phosphoric acid anhydride bond (P-O-P), with high energy of hydrolysis. When a reaction needs energy, ATP can transfer:
- A phosphate group (γ-P), giving ADP and a phosphorylated substrate. Used for protein kinase reactions, glucose phosphorylation in glycolysis, etc.
- An adenosyl group (the AMP minus the α-phosphate), giving PPᵢ. Used to activate substrates for further chemistry (e.g., amino acids being attached to tRNAs).
- The whole AMP group, giving inorganic phosphate. Less common.

The hydrolysis ΔG° of ATP to ADP + Pᵢ is about –30 kJ/mol. Any reaction that costs less than 30 kJ/mol can be driven forward by coupling it to ATP hydrolysis. This is how ATP "powers" the cell — it provides a thermodynamic crank.

## Glycolysis

The breakdown of one glucose molecule into two pyruvates. Ten enzymatic steps. Net energy yield: 2 ATP and 2 NADH per glucose.

The steps (simplified):

1. Glucose + ATP → glucose-6-phosphate (G6P). Phosphorylation by hexokinase. Traps glucose in the cell.
2. G6P ↔ fructose-6-phosphate (F6P). Isomerization (an aldose to a ketose) by phosphoglucose isomerase.
3. F6P + ATP → fructose-1,6-bisphosphate (F1,6BP). Second phosphorylation, by phosphofructokinase. The committed step of glycolysis.
4. F1,6BP → DHAP + G3P. Cleavage by aldolase — a *retro-aldol* reaction. The 6-carbon sugar splits into two 3-carbon halves.
5. DHAP ↔ G3P. Isomerization by triose phosphate isomerase, ensuring both halves continue.
6. G3P + NAD⁺ + Pᵢ → 1,3-BPG + NADH. Oxidation and phosphorylation by glyceraldehyde-3-phosphate dehydrogenase.
7. 1,3-BPG + ADP → 3-PG + ATP. Substrate-level phosphorylation (the first ATP made).
8. 3-PG → 2-PG. Phosphate transfer.
9. 2-PG → PEP + H₂O. Dehydration (an E2-like elimination).
10. PEP + ADP → pyruvate + ATP. Second substrate-level phosphorylation.

Net: glucose + 2 NAD⁺ + 2 ADP + 2 Pᵢ → 2 pyruvate + 2 NADH + 2 ATP + 2 H₂O.

The chemistry of each step is recognizable: phosphorylation (acyl substitution at phosphorus), isomerization (proton transfer at the α-carbon), aldol cleavage (Chapter 23), oxidation (NAD⁺ as the oxidant, accepting hydride), elimination (E2 or E1-like).

Pyruvate's fate depends on conditions:
- Aerobic (oxygen present): pyruvate → acetyl-CoA → citric acid cycle.
- Anaerobic in muscle: pyruvate → lactate. Regenerates NAD⁺.
- Anaerobic in yeast: pyruvate → ethanol + CO₂. The fermentation reaction used in beer and bread.

## The citric acid cycle (TCA cycle)

Acetyl-CoA enters the cycle by condensing with oxaloacetate (a 4-carbon dicarboxylate) to give citrate (a 6-carbon tricarboxylate). The chemistry: an aldol-like reaction, where the methyl of acetyl-CoA serves as the enolate, attacking the α-keto group of oxaloacetate. This is citrate synthase.

Citrate is then oxidized in seven more steps, releasing 2 CO₂ molecules, generating 3 NADH and 1 FADH₂, and producing 1 GTP (which is interconvertible with ATP). At the end, oxaloacetate is regenerated, ready to start the cycle again.

The cycle is "catalytic" in oxaloacetate: each turn consumes acetyl-CoA, produces 2 CO₂, and regenerates oxaloacetate. The acetyl group has been fully oxidized to two CO₂. The energy released is captured as NADH/FADH₂/GTP.

Every chemical step in the TCA cycle is recognizable:
- Aldol condensation (citrate synthase).
- Dehydration + rehydration (aconitase: citrate → cis-aconitate → isocitrate).
- Oxidative decarboxylation (isocitrate → α-ketoglutarate, with NAD⁺).
- α-Ketoglutarate to succinyl-CoA (oxidative decarboxylation, with NAD⁺ and CoA).
- Substrate-level phosphorylation (succinyl-CoA → succinate + GTP).
- Oxidation (succinate → fumarate, with FAD).
- Hydration (fumarate → malate).
- Oxidation (malate → oxaloacetate, with NAD⁺).

The cycle as a whole: an elegant solution to the problem of how to oxidize acetate to CO₂ while capturing the energy. The 8-step pathway has stood up to billions of years of evolution; essentially every aerobic organism on Earth runs this cycle.

## Oxidative phosphorylation

The NADH and FADH₂ produced in glycolysis and the TCA cycle don't directly make ATP. They're carriers of high-energy electrons. The electrons are passed to oxygen through the *electron transport chain* (a series of membrane-embedded proteins in mitochondria), with the energy released used to pump protons across the inner mitochondrial membrane.

The proton gradient (high outside, low inside) is the proximal energy source. Protons flow back into the matrix through the *F₁F₀ ATP synthase*, an enzyme that couples proton flow to ATP synthesis. About 2.5 ATP per NADH and 1.5 ATP per FADH₂ are produced.

Net energy accounting from one glucose molecule:
- Glycolysis: 2 ATP + 2 NADH (glycolysis-NADH varies in yield, ~3-5 ATP).
- 2 Pyruvate dehydrogenase: 2 NADH (5 ATP).
- 2 Turns of TCA cycle: 6 NADH + 2 FADH₂ + 2 GTP (15 + 3 + 2 = 20 ATP).
- Total: about 30-32 ATP per glucose, depending on assumptions.

This is roughly 40% efficient at capturing the chemical energy of glucose oxidation. The rest is heat.

## Lipid metabolism

**Catabolism (β-oxidation).** Fatty acids enter mitochondria (after activation as fatty acyl-CoA) and undergo cycles of β-oxidation. Each cycle:
1. Oxidation: fatty acyl-CoA → α,β-unsaturated acyl-CoA (with FAD).
2. Hydration: α,β-unsaturated acyl-CoA → β-hydroxy acyl-CoA.
3. Oxidation: β-hydroxy acyl-CoA → β-keto acyl-CoA (with NAD⁺).
4. Thiolytic cleavage: β-keto acyl-CoA + CoA → acetyl-CoA + acyl-CoA (two carbons shorter).

Each cycle gives one acetyl-CoA, one NADH, and one FADH₂. The shortened acyl-CoA goes through another cycle. After enough cycles, the entire fatty acid is converted to acetyl-CoA, which then enters the TCA cycle.

A 16-carbon palmitic acid undergoes 7 cycles of β-oxidation, giving 8 acetyl-CoA. Net energy yield (after TCA + oxidative phosphorylation): about 106 ATP per palmitate. Per gram, fats give more than twice the ATP that carbohydrates do — which is why fat is energy-dense storage.

**Anabolism (fatty acid biosynthesis).** Roughly the reverse of β-oxidation, but with different cofactors and a different protein machine (fatty acid synthase). Acetyl-CoA + malonyl-CoA → β-keto acyl-CoA → β-hydroxy acyl-CoA → α,β-unsaturated acyl-CoA → saturated acyl-CoA (extended by two carbons). The Claisen condensation of Chapter 23 is the backbone of each cycle.

After 7 cycles, palmitic acid (C16) is the typical product. Different organisms make slightly different fatty acid chains, but the basic chemistry is the same.

## Amino acid metabolism

Amino acids are made (anabolism) and broken down (catabolism) in pathways that are organism- and amino-acid-specific. Some general patterns:

**Catabolism of amino acids.** The α-amino group is removed (often by transamination — pyridoxal-phosphate-mediated transfer to α-ketoglutarate, giving glutamate). The remaining carbon skeleton enters the TCA cycle as one of its intermediates (acetyl-CoA, α-ketoglutarate, succinyl-CoA, fumarate, oxaloacetate, or pyruvate, depending on the amino acid). The amino group is eventually excreted as urea (in mammals) or ammonia (in fish).

**Anabolism of amino acids.** The carbon skeleton comes from a TCA-cycle intermediate (or other metabolite); the amino group is added by transamination (from glutamate, typically). Some amino acids are made through long pathways (tryptophan, phenylalanine, lysine — the aromatic amino acids and lysine are made by complex routes in plants and bacteria). Mammals can make 11 of the 20 amino acids; the others are dietary essentials.

## Nucleic acid metabolism

Nucleotides are built up from amino acids and small one-carbon donors (formate, glycine, glutamine). The pathways are particularly pretty: the purine ring is built up step by step on the ribose-5-phosphate, with each ring atom contributing from a different small precursor. Pyrimidines are built first as the ring, then attached to the ribose.

Nucleotides are degraded back to their amino acid and one-carbon precursors when not needed. The breakdown of purines goes through xanthine to uric acid; high uric acid in blood causes gout (when uric acid crystals deposit in joints).

## The big picture

Metabolism is organic chemistry applied at scale, with enzymes as catalysts. The dozens of distinct reactions you encounter in a biochemistry textbook reduce to a smaller number of mechanism types:

- **Phosphorylation** (acyl-substitution at phosphorus): ATP transfers a phosphate.
- **Aldol condensations and retro-aldols** (citrate synthase, aldolase).
- **Claisen condensations** (fatty acid synthesis, polyketide biosynthesis).
- **Hydrations and dehydrations** (fumarase, enolase, fatty acid synthase β-step).
- **Oxidations and reductions** (NAD⁺/NADH, FAD/FADH₂, NADP⁺/NADPH).
- **Isomerizations** (proton transfer at α-carbons; sugar interconversions).
- **Transaminations** (PLP-mediated amino group transfer).
- **Decarboxylations** (β-ketoacid decarboxylation, often pyruvate-decarboxylase-like).
- **Hydrolytic cleavages** (proteases, lipases, glycosidases).

Each of these is a reaction we've covered, run in the active site of an enzyme, with the enzyme providing rate enhancement and selectivity.

Pathway organization is what makes metabolism interesting beyond just the chemistry. Pathways are *regulated* — feedback inhibition, allosteric activation, hormonal control, gene expression — so that flow is matched to demand. This regulation is a layer of biology on top of the chemistry; it's where metabolism stops being just organic chemistry and becomes physiology.

↳ **Dig Deeper — Why most metabolism uses thioesters instead of regular esters**

> Acetyl-CoA, malonyl-CoA, succinyl-CoA, and many other key metabolic intermediates are *thioesters* (RCOSCoA), not regular oxygen esters. Walk through why biology uses the thioester form. Cover: the higher energy of hydrolysis of thioesters compared to oxygen esters (~30 kJ/mol vs. 20 kJ/mol), the lower α-pKa of thioesters (about 21 vs. 25 for oxygen esters) which makes Claisen condensations work more easily, and the resonance argument that explains both effects (sulfur is less effective than oxygen at donating lone pairs into the C=O).

**What to do with the output:** Verify by checking biochemistry textbook treatments of acetyl-CoA chemistry. The thioester's higher energy is what makes acetyl-CoA a "high-energy intermediate" — its hydrolysis to acetate + CoA is favorable, and that energy can be coupled to other reactions.

## What this chapter does

Metabolism is the network of chemical reactions that extracts energy from food and builds the molecules cells need. It comes in two flavors: catabolism (breakdown, energy-releasing) and anabolism (synthesis, energy-consuming).

The chemistry of metabolic pathways is the chemistry we've covered:
- Phosphorylation (acyl substitution at phosphorus, by ATP).
- Aldol/retro-aldol (citrate synthase, aldolase).
- Claisen condensation (fatty acid synthase).
- Oxidation/reduction (NAD⁺/NADH, FAD/FADH₂, with hydride transfer).
- Isomerization (proton transfer at α-carbon).
- Hydration/dehydration (often E1cB for biological dehydration).
- Hydrolytic cleavage (esterase, peptidase, glycosidase).

Major pathways:
- **Glycolysis**: glucose → 2 pyruvate, +2 ATP, +2 NADH.
- **Citric acid cycle**: acetyl-CoA → 2 CO₂, +3 NADH, +1 FADH₂, +1 GTP.
- **Oxidative phosphorylation**: NADH/FADH₂ → ATP via mitochondrial electron transport chain.
- **β-Oxidation**: fatty acids → acetyl-CoA + reduced cofactors.
- **Fatty acid synthesis**: acetyl-CoA → palmitic acid + ... (essentially β-oxidation reversed).
- **Amino acid metabolism**: each amino acid has its own catabolic and anabolic pathway, usually linked to a TCA-cycle intermediate.

ATP is the cellular energy currency. Most reactions that need energy are coupled to ATP hydrolysis; most reactions that release energy generate ATP (or NADH/FADH₂ that can be used to make ATP).

The next two chapters cover special topics: pericyclic reactions (Chapter 30) and synthetic polymers (Chapter 31). These complete the standard organic chemistry curriculum.

---

*Source for all data, examples, and historical references: OpenStax* Organic Chemistry*, Chapter 29, modules m00328 through m00338.*
---

## LLM Exercise — Chapter 29: The Organic Chemistry of Metabolic Pathways (Synthesize a Target Molecule Project)

**Project:** Synthesize a Target Molecule.
**What you're building this chapter:** trace your target's likely metabolic fate in the body (Phase I, Phase II metabolism).
**Tool:** **Claude Project**.

---

**The Prompt:**

```
Chapter 29 of my Synthesis project. Chapter 29 taught: the major
metabolic pathways (glycolysis, citric acid cycle, fatty-acid
oxidation and synthesis); cofactors (NAD⁺, FAD, CoA, ATP) and
their organic-chemistry roles (NAD⁺/FAD are electron acceptors in
oxidation reactions; CoA carries acyl groups in condensations;
ATP donates phosphate); key reaction types repeating across
pathways (Claisen-like condensations build C-C bonds; aldol-like
condensations build aldol intermediates; oxidations and reductions
shuttle electrons via cofactors); drug metabolism's Phase I
(functionalization — oxidation, reduction, hydrolysis, often by
cytochrome P450 enzymes) and Phase II (conjugation — sulfation,
glucuronidation, glutathione conjugation).

Write the brief's "Metabolic Fate" section in 300–500 words.

If your target is a drug:

1. **Predict Phase I metabolism.** Where will the body modify
   your target?
   - Aromatic positions are common P450 oxidation sites
     (hydroxylation).
   - Methyl groups can be demethylated.
   - Amines can be N-demethylated.
   - Aldehydes can be oxidized to acids.
   - Esters and amides can be hydrolyzed (if not too sterically
     hindered).

2. **Predict Phase II metabolism.** Once Phase I produces a
   hydroxyl, amine, or carboxylic acid, Phase II conjugates it:
   - Sulfation (–OSO₃H).
   - Glucuronidation (attached to glucuronic acid).
   - Methylation (less common in humans).
   - Glutathione conjugation (for reactive electrophiles).

3. **The half-life implication.** Faster Phase I/II metabolism =
   shorter half-life in body. Many drugs are deliberately designed
   to resist common P450 sites (fluorine substitution at vulnerable
   positions; replacing methyl with trifluoromethyl).

4. **The active-metabolite question.** Some drugs are actually
   prodrugs — they enter the body inactive and get metabolized
   into the active form. Codeine → morphine. Cyclophosphamide →
   active alkylating agent. If your target is a prodrug, the
   metabolic activation step IS the mechanism of action.

If your target is a natural biological molecule (sugar, amino
acid, fatty acid, nucleotide): trace its biosynthetic origin
back to acetyl-CoA, glucose, or another building block. Many
natural products have known biosynthetic routes that informed
total synthesis approaches.

End with: how does the metabolic fate of your target influence
its dosing? (Drugs metabolized quickly need higher or more-
frequent dosing.)
```

---

**What this produces:** A 300–500 word section. For drug targets, this is the chapter most useful for connecting organic chemistry to pharmacology.

**Connection to previous chapters:** Ch 22-23's condensation reactions are precisely what biosynthesis uses (just enzyme-catalyzed instead of chemically). Ch 28's nucleotides include ATP, the major energy currency.

**Preview of next chapter:** Chapter 30 covers pericyclic reactions — orbital-symmetry-controlled reactions like the Diels-Alder. If your synthesis uses any of these, you'll deepen the analysis.


---

## AI Wayback Machine

**Hans Krebs** was worked out the citric acid cycle in 1937 — Nobel 1953.

**Run this:**

```
Who is Hans Krebs, and how does their work connect to metabolic pathway chemistry we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Hans Krebs"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Hans Krebs's key experiments or syntheses in detail.
- Add a constraint: "Answer including criticisms or limits of Hans Krebs's framework."

What changes? What gets better? What gets worse?
