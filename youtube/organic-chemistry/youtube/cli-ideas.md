# Organic Chemistry — CLI Video Ideas ("X with Claude")

> Scout date: 2026-07-12
> Source content: 31 substantive chapters (00-frontmatter through 31-synthetic-polymers) covering structure/bonding, stereochemistry, all major reaction classes (SN1/SN2/E1/E2, addition, elimination, substitution, condensation), spectroscopy, biomolecules, and metabolic pathways. Rich in mechanism-based reasoning. Mixed BUILD + RESEARCH lane.

---

## Candidate 01 — "Build an SN1 vs SN2 Reaction Rate Predictor with Claude"
- Source: organic-chemistry/chapters/11-reactions-of-alkyl-halides-nucleophilic-substitutions-and-eliminations.md
- Lane: BUILD (Claude Code)
- Hook: Changing nothing but the solvent can shift the reaction rate by 200,000-fold — five orders of magnitude from methanol to HMPA. Claude can build the predictor that shows exactly which mechanism wins for any alkyl halide + nucleophile + solvent combination.
- The artifact: A Python CLI that takes substrate type (methyl/primary/secondary/tertiary), nucleophile strength (strong base vs polarizable anion), and solvent (protic vs aprotic) as inputs, predicts SN1 vs SN2 vs E1 vs E2 preference with confidence score, and generates an animated Manim energy diagram showing ΔG‡ for each competing pathway.
- Prompt seed: `claude "Write a Python script that predicts SN1 vs SN2 vs E1 vs E2 preference given: substrate (methyl/primary/secondary/tertiary), nucleophile (list the 5 main classes with nucleophilicity and basicity ratings), and solvent (protic/aprotic). Use a decision-tree with explicit rules: tertiary → SN1 or E1, methyl/primary + strong nucleophile + aprotic → SN2, etc. Output: mechanism prediction with confidence (HIGH/MEDIUM/UNCERTAIN), reasoning chain, and a Manim scene showing the competing energy diagrams with ΔG‡ for each pathway labeled."`
- Read / check: Verify tertiary + protic + weak nucleophile predicts SN1 (HIGH confidence). Check that secondary + strong base + protic predicts E2 (not SN2). Confirm the Manim energy diagram shows at least 2 competing pathways with labeled transition states.
- Human supplies: Nothing — fully synthetic. A real rate measurement dataset (e.g., from Clayden's tables) would make the energy values more accurate, but the decision-tree logic is authentic.
- Output medium: Manim (animated competing energy diagram + terminal decision-tree output)
- The change: Add the Winstein ion-pair intermediate: show how incomplete ionization biases the stereochemical outcome toward inversion in SN1 — animate the two-step process (tight ion pair → solvent-separated → capture from either face).
- Teardown angle: The mechanism isn't fixed by the substrate alone — solvent is doing as much work as the leaving group. Five orders of magnitude from a solvent change is not a detail; it is the dominant variable in practical synthesis.
- Exclusions: Absolute rate calculation (Marcus theory), substituent effects beyond sterics/electronics, flow chemistry.
- Score: 9/10

---

## Candidate 02 — "Build a Curly Arrow Mechanism Validator with Claude"
- Source: organic-chemistry/chapters/06-an-overview-of-organic-reactions.md
- Lane: BUILD (Claude Code)
- Hook: Organic chemistry is the only undergraduate course where drawing the wrong arrow costs you the reaction. But arrow-pushing has strict rules — and Claude can check your mechanism against every one of them before you submit.
- The artifact: A Python CLI that takes a SMILES-format mechanism description (or a step-by-step text description of electron movements) and validates it against the 6 curly-arrow rules: arrows from lone pairs or bonds only, arrows point to electrophilic center, full head = 2 electrons, fishhook = 1 electron, no more than 2 arrows per step, electron count conserved. Outputs: step-by-step validation table with PASS/FAIL for each rule + a specific error message for each failure.
- Prompt seed: `claude "Write a Python CLI that validates a described organic mechanism against curly arrow rules. Input: a step-by-step mechanism as text (e.g., 'Step 1: HO- lone pair attacks carbonyl carbon, pi electrons move to oxygen'). For each step, check: (1) arrow source is lone pair or bond, (2) arrow destination is electrophile (empty orbital or antibonding), (3) full-head arrows represent 2 electrons, (4) no more than 2 arrows per step, (5) formal charges are consistent with electron movement, (6) electron count is conserved. Output a validation table. Use anthropic SDK."`
- Read / check: Verify the validator catches an arrow drawn from H on carbon to a neutral atom (not a valid source). Check that an SN2 mechanism with one incoming arrow and one leaving arrow passes. Confirm the validator flags a step with 3 arrows as invalid.
- Human supplies: A set of student-submitted mechanisms (text descriptions) to test. Anthropic API key. Ideally a real student mechanism with an error for demonstration.
- Output medium: screen-recording mp4 (terminal showing validation running against 3 mechanisms — 2 valid, 1 invalid — with error messages appearing)
- The change: Add a "suggest correction" output for each failed step — Claude identifies the incorrect arrow and proposes the correct one.
- Teardown angle: Arrow-pushing errors are the entry point for every wrong product prediction in undergraduate organic chemistry. The validator makes the invisible rules visible — and makes the student's error specific, not vague.
- Exclusions: 3D orbital visualization, computational mechanism confirmation (Gaussian/Jaguar), multi-step synthesis validation.
- Score: 8/10

---

## Candidate 03 — "Build a Carbonyl Reactivity Series Simulator with Claude"
- Source: organic-chemistry/chapters/19-aldehydes-and-ketones-nucleophilic-addition-reactions.md
- Lane: BUILD (Claude Code)
- Hook: The nucleophilic addition mechanism is the same for every carbonyl compound — but the rate differs by orders of magnitude across the series. Formaldehyde reacts in seconds; aryl ketones barely react at all. Claude can plot the entire reactivity series and show why.
- The artifact: A Python script that computes the relative electrophilicity (δ+ on carbonyl carbon) for 8 carbonyl compounds (formaldehyde, acetaldehyde, acetone, cyclohexanone, benzaldehyde, acetophenone, methyl acetate, acetyl chloride) from Hammett sigma and inductive/resonance parameters, then animates a Manim bar chart of relative reactivity with the electronic explanation annotated for each bar.
- Prompt seed: `claude "Compute the relative nucleophilic addition reactivity for these carbonyl compounds: formaldehyde, acetaldehyde, acetone, cyclohexanone, benzaldehyde, acetophenone, methyl acetate, acetyl chloride. Use Hammett sigma values and resonance/inductive arguments to rank them. Output: (1) a table with compound, sigma_p, steric factor (H/alkyl/aryl), resonance effect (none/partial/strong), and relative reactivity score, (2) a Manim animation of a bar chart that grows bar by bar in order of decreasing reactivity, with a one-line electronic explanation annotated above each bar."`
- Read / check: Verify formaldehyde ranks highest and methyl acetate lowest (or near lowest — resonance from ester oxygen reduces electrophilicity). Check that acetyl chloride ranks near the top (I-effect of Cl increases δ+). Confirm the Manim chart animates bars growing in reactivity order.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated growing bar chart with annotations)
- The change: Add a second chart: add water as the nucleophile and show the equilibrium hydration constant (Khydr) for each compound — demonstrating that formaldehyde is >99% hydrated while acetone is <0.1%.
- Teardown angle: The carbonyl reactivity series is not memorized — it is derived from two variables: how electrophilic the carbon is and how accessible it is. Understanding why the series exists is more useful than memorizing where each compound falls.
- Exclusions: Transition state theory derivation, solvent effects on carbonyl reactivity, enzyme active site enhancement.
- Score: 8/10

---

## Candidate 04 — "Research the Thalidomide Stereochemistry Story with Claude"
- Source: organic-chemistry/chapters/05-stereochemistry-at-tetrahedral-centers.md
- Lane: RESEARCH (Claude assistant)
- Hook: One enantiomer of thalidomide treats morning sickness. The other causes limb malformation. They differ only in the spatial arrangement of four atoms around a single carbon. And in the body, the safe enantiomer converts to the harmful one anyway. Claude can research what actually happened — and what it reveals about chiral drug development.
- The artifact: A sourced 4-section brief: (1) the thalidomide disaster — timeline, how many children affected, the regulatory failure, (2) the stereochemistry — which enantiomer is teratogenic, the R/S assignment, the mechanism of harm, (3) the in vivo racemization finding — the (R) enantiomer converts to (S) under physiological conditions, making separation futile, (4) what thalidomide's story changed in FDA/EMA drug approval policy — the requirement for chiral switch data.
- Prompt seed: `claude "Research the thalidomide story from a stereochemistry perspective. (1) Timeline: when marketed, what harm, how many children affected, regulatory response in US vs Europe. (2) Stereochemistry: which enantiomer (R or S) is teratogenic, the mechanism of teratogenicity (binding to cereblon/CRBN), the R/S assignment at the chiral center. (3) In vivo racemization: how quickly does the R enantiomer convert to S under physiological conditions, and what this means for any enantiomer-separation solution. (4) Regulatory change: what specific requirements did the FDA/EMA add for chiral drugs after thalidomide? Cite sources."`
- Read / check: Verify the R/S assignment is correct (S is teratogenic; R is the therapeutic enantiomer — but racemization makes this moot). Check that the cereblon binding mechanism is cited from a primary source. Confirm the FDA regulatory change is specific (cite the 1992 FDA policy statement on stereoisomers).
- Human supplies: Nothing — Claude can synthesize from published literature. A medicinal chemist or pharmacologist would validate the mechanism section.
- Output medium: slate (4-panel sourced brief with a structural diagram of (R) vs (S) thalidomide as a Remotion static image, and a timeline of regulatory events as animated sequence)
- The change: Find a second chiral drug story where the "wrong" enantiomer was beneficial (e.g., esomeprazole vs omeprazole) — contrasting the thalidomide cautionary tale with a case where stereoisomer separation was commercially, not just safety, motivated.
- Teardown angle: Chirality is not a pharmaceutical curiosity — it is the molecular basis of biological specificity. The thalidomide story shows what happens when chirality is treated as a packaging question rather than a mechanism question.
- Exclusions: Full history of drug regulation, all chiral drugs on the market, asymmetric synthesis methods.
- Score: 9/10

---

## Candidate 05 — "Build a Glycolysis Mechanism Mapper with Claude"
- Source: organic-chemistry/chapters/29-the-organic-chemistry-of-metabolic-pathways.md
- Lane: BUILD (Claude Code)
- Hook: Every step of glycolysis is a reaction from organic chemistry — aldol, elimination, oxidation, SN2. Biochemistry and organic chemistry are the same subject. Claude can build the mapper that annotates each glycolysis step with its organic mechanism type and animates the 10-step pathway.
- The artifact: A Manim animation of the 10 glycolysis steps: each step drawn as a substrate → product transformation, with the mechanism type annotated (retro-aldol, E1cB elimination, oxidation/phosphorylation, SN2-type phosphoryl transfer, substrate-level phosphorylation) and a running ATP/NADH tally in the corner.
- Prompt seed: `claude "Create a Manim animation of the 10 glycolysis steps: for each step, show substrate → enzyme → product, annotate the organic mechanism type (kinase phosphorylation = phosphoryl SN2, aldolase = retro-aldol, enolase = E1cB elimination, G3PDH = oxidation+acyl phosphate, pyruvate kinase = dephosphorylation). Include a corner counter tracking ATP investment (steps 1,3) and ATP yield (steps 7,10) and NADH yield (step 6). Draw each step sequentially with a 2s pause between."`
- Read / check: Verify the mechanism annotations are correct: aldolase step is retro-aldol (not SN2), enolase step is E1cB (loss of H2O from 2-phosphoglycerate), G3PDH is oxidative phosphorylation. Check the ATP counter: net yield is +2 ATP and +2 NADH per glucose. Confirm Manim renders 10 sequential steps.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (10-step sequential animation with mechanism annotations and running counter)
- The change: Add the TCA cycle in a second pass — annotate the first 4 steps with their organic mechanism type (thioester Claisen, dehydration, re-hydration, oxidation) and show how they echo the same moves as glycolysis.
- Teardown angle: Biochemistry is not a separate subject from organic chemistry — it is organic chemistry scaled up by evolution. Every enzyme is a catalyst for a reaction type you already know. Seeing the mechanism labels appear on each glycolysis step is the moment where the two subjects merge.
- Exclusions: Regulatory enzymes (PFK allosteric control), gluconeogenesis, pentose phosphate pathway.
- Score: 8/10

---

## Candidate 06 — "Research Nucleophilicity vs Basicity: Why They Diverge with Claude"
- Source: organic-chemistry/chapters/11-reactions-of-alkyl-halides-nucleophilic-substitutions-and-eliminations.md
- Lane: RESEARCH (Claude assistant)
- Hook: Iodide is a terrible base (pKa of HI = −10) but an excellent nucleophile. Fluoride is a strong base but a poor nucleophile in protic solvents. Basicity and nucleophilicity measure the same kind of reactivity with electrons — so why do they diverge so dramatically?
- The artifact: A sourced 3-section brief: (1) the operational definitions of basicity (pKa, affinity for H+) vs nucleophilicity (rate constant for SN2 on methyl iodide in a reference solvent), (2) the three factors that cause divergence — polarizability, solvation effects in protic vs aprotic media, and the thermodynamic vs kinetic distinction — with specific data from the literature (nucleophilicity vs basicity tables), (3) the practical rule: for SN2 in DMSO, rank the nucleophiles; for SN2 in MeOH, how does the ranking change and why?
- Prompt seed: `claude "Research why nucleophilicity and basicity diverge for halide anions and related nucleophiles. (1) Operational definitions: how is basicity measured (pKa) vs nucleophilicity (second-order rate constant for SN2 on methyl iodide). (2) Three divergence factors: polarizability (why iodide reacts faster than fluoride despite being a weaker base), solvation in protic vs aprotic solvents (why the ranking changes with solvent), and thermodynamic vs kinetic distinction. Include specific rate data (relative rates from standard tables). (3) Practical ranking: list the 5 main nucleophiles in order for SN2 in DMSO, then in water, and explain the difference. Cite textbook or primary sources."`
- Read / check: Verify the rate data (water vs cyanide should differ by ~5 orders of magnitude). Check that the solvation explanation distinguishes between cation solvation (aprotic does well) and anion solvation (protic wraps anions in H-bonds). Confirm the practical ranking reverses correctly for the two solvents.
- Human supplies: Nothing — Claude synthesizes from standard organic chemistry references (Clayden, March, Clayden Tables). A physical organic chemist would validate the rate data section.
- Output medium: slate (3-panel brief with the nucleophilicity ranking table in both solvents as a Remotion comparison table)
- The change: Extend the brief to soft-hard acid-base (HSAB) theory — show how the polarizability argument maps onto Pearson's softness classification, and what it predicts for iodide vs fluoride across reactions.
- Teardown angle: Basicity and nucleophilicity are the same drive in different contexts — thermodynamic vs kinetic, H+ vs carbon center. The divergence is not a contradiction; it is a reminder that context determines which measure predicts the outcome.
- Exclusions: Marcus theory of nucleophilicity, computational nucleophilicity indices (Mayr's scale in full), radical nucleophilicity.
- Score: 8/10

---

## Candidate 07 — "Build an Alkene Stability Visualizer with Claude"
- Source: organic-chemistry/chapters/07-alkenes-structure-and-reactivity.md
- Lane: BUILD (Claude Code)
- Hook: More substituted alkenes are more stable — but the energy differences are real and measurable from heat of hydrogenation data. Claude can build the visualizer that plots the stability ladder and shows exactly how much each alkyl group contributes.
- The artifact: A Python script that computes the relative stability of alkenes (ethylene through tetrasubstituted) from their experimental heats of hydrogenation, and produces a Manim animation of a stability ladder where each alkene is placed at its real ΔHhydr value, with the substituent count annotated and the stabilization energy per group calculated.
- Prompt seed: `claude "Using experimental heats of hydrogenation (ΔHhydr) from standard tables — ethylene: −137 kJ/mol, 1-butene: −127 kJ/mol, 2-butene (cis): −120 kJ/mol, 2-butene (trans): −116 kJ/mol, 2-methylpropene: −119 kJ/mol — compute: (1) relative stability (reference = ethylene = 0), (2) average stabilization per substituent, (3) cis-trans energy difference. Create a Manim animation of a vertical stability ladder with each alkene placed at its real energy level, substituents labeled, and the per-group stabilization annotated."`
- Read / check: Verify trans-2-butene is more stable than cis-2-butene by about 4 kJ/mol. Check that the stabilization per alkyl group calculation is consistent across the series (approximately 8–12 kJ/mol per substituent). Confirm the Manim ladder has proper y-axis scale.
- Human supplies: Nothing — fully synthetic. The heats of hydrogenation are standard textbook values.
- Output medium: Manim (animated vertical stability ladder with alkenes placed at real energy levels)
- The change: Add a third axis showing the degree of unsaturation formula and correlate it with the stability; then show how the most substituted alkene is also the thermodynamic product in E1 elimination (Saytzeff's rule as a direct consequence).
- Teardown angle: Alkene stability is not a memorized order — it's the quantitative consequence of hyperconjugation. The heat of hydrogenation data makes it experimentally real, not just theoretically tidy.
- Exclusions: Calculation of heats of hydrogenation from bond dissociation energies, Bredt's rule strained alkenes.
- Score: 7/10

---

## Candidate 08 — "Research the Role of SAM in Biological SN2 Reactions with Claude"
- Source: organic-chemistry/chapters/11-reactions-of-alkyl-halides-nucleophilic-substitutions-and-eliminations.md
- Lane: RESEARCH (Claude assistant)
- Hook: Every time your body makes adrenaline from norepinephrine, it runs a clean SN2 reaction with a sulfonium ion as the electrophile. S-adenosylmethionine (SAM) is the cell's methyl iodide. Claude can trace all the biological SN2 reactions that run on SAM — and find out how many there are.
- The artifact: A sourced 3-section brief: (1) the SAM methylation mechanism — the sulfonium electrophile, backside attack by the nucleophile, stereochemistry at the transferred methyl carbon, and why SAM is an excellent biological leaving group, (2) the scope — how many transmethylation reactions SAM participates in (the number is in the hundreds), and which biological categories they fall into (epigenetics/DNA methylation, neurotransmitter biosynthesis, lipid biosynthesis, protein methylation), (3) a comparison: why the cell uses SAM rather than a simpler methyl donor like methanol or methyl iodide — the thermodynamic and kinetic argument.
- Prompt seed: `claude "Research S-adenosylmethionine (SAM) as a biological SN2 agent. (1) The methylation mechanism: the sulfonium electrophile structure, why the C-S bond is activated (positive sulfur as EWG), the SN2 trajectory, stereochemistry at the methyl carbon, and SAH as leaving group. (2) Scope: how many SAM-dependent methyltransferase reactions are known? Categorize by type (DNA methylation, histone methylation, neurotransmitter biosynthesis, lipid biosynthesis). (3) Why SAM rather than a simpler methyl donor — the thermodynamic and kinetic argument (what makes the C-S bond in SAM more electrophilic than C-O in methanol). Cite primary or review sources."`
- Read / check: Verify the sulfonium electrophilicity argument is correct (positive charge on S makes carbon electrophilic by induction). Check that the scope claim (~200+ SAM-dependent reactions) is cited from a genome-scale study or database. Confirm the comparison to methanol uses a thermodynamic argument (not just "SAM is more reactive").
- Human supplies: Nothing — Claude synthesizes from biochemistry literature. A biochemist or structural biologist would validate the enzyme mechanism details.
- Output medium: slate (3-panel brief with a category table of SAM-dependent reactions as a Remotion visualization)
- The change: Find a clinical case where dysregulated SAM-dependent methylation causes disease (e.g., MTHFR mutation, cancer epigenetics) — connecting the mechanism to a therapeutic context.
- Teardown angle: SN2 is not just a reaction you learn in chapter 11 — it is running continuously in every cell in your body. The biological applications are not analogies; they are the same mechanism, in the same solvent, with the same stereochemical outcome.
- Exclusions: Full methylation cycle biochemistry (folate, cobalamin), SAM synthesis pathway, methylation-based therapeutics.
- Score: 8/10

---

## Candidate 09 — "Build a Degree of Unsaturation Calculator and Interpreter with Claude"
- Source: organic-chemistry/chapters/07-alkenes-structure-and-reactivity.md
- Lane: BUILD (Claude Code)
- Hook: A molecular formula from mass spectrometry gives you the molecular weight and the degree of unsaturation — and from that alone you can narrow a compound from millions to dozens. Claude can build the calculator that turns a molecular formula into a structural shortlist.
- The artifact: A Python CLI that takes a molecular formula (e.g., C6H6, C7H8NO), computes the degree of unsaturation (DoU), and generates: (1) the DoU value with formula derivation shown, (2) the structural interpretation: what combinations of rings and double/triple bonds are consistent, (3) a shortlist of 5 common organic structures matching the formula, ordered by likelihood (based on common functional groups). Formatted as a terminal output with the formula derivation animated in Manim as a secondary visual.
- Prompt seed: `claude "Write a Python CLI that takes a molecular formula (e.g., 'C6H6') and: (1) computes the degree of unsaturation using DoU = (2C+2+N-H-X)/2 (handle halogens and nitrogen), (2) lists all structurally consistent combinations of rings + double bonds + triple bonds, (3) generates a shortlist of 5 well-known organic structures matching the formula, ordered by how commonly they appear in natural products and pharmaceuticals. Display the formula derivation step-by-step. Also create a Manim animation showing the formula formula being applied step-by-step for the example given."`
- Read / check: Verify C6H6 gives DoU = 4 (3 double bonds + 1 ring = benzene, or other isomers). Check that C7H8NO gives the correct DoU accounting for N (+1) and O (ignored). Confirm the shortlist for C6H6 includes benzene as the first entry.
- Human supplies: A molecular formula from a real mass spectrum (the human provides the spectrum; the CLI provides the interpretation).
- Output medium: Manim (animated formula derivation) + screen-recording mp4 (terminal showing the shortlist)
- The change: Add a second mode: input a partial structure (e.g., "has a carbonyl and a ring") and filter the shortlist to only structures consistent with that additional constraint.
- Teardown angle: Degree of unsaturation is the first filter applied to any unknown compound. One number eliminates 99% of possibilities before any other data is collected. That is the power of knowing what the formula actually encodes.
- Exclusions: Full structure elucidation pipeline, NMR prediction, combinatorial enumeration of all isomers.
- Score: 7/10

---

## Candidate 10 — "Research the Enolate Chemistry of Natural Product Biosynthesis with Claude"
- Source: organic-chemistry/chapters/22-carbonyl-alpha-substitution-reactions.md + 29-the-organic-chemistry-of-metabolic-pathways.md
- Lane: RESEARCH (Claude assistant)
- Hook: The alpha-carbon of a carbonyl is acidic (pKa 19–25). That single fact enables all of fatty acid biosynthesis, polyketide natural product synthesis, and the Claisen condensations of the TCA cycle. Claude can map the connection between the undergraduate enolate chemistry and the biosynthetic pathways that run it at industrial scale in every living cell.
- The artifact: A sourced 3-section brief: (1) the enolate as biosynthetic nucleophile — the pKa of the alpha-carbon of acetyl-CoA (a thioester, lower pKa than ketone), the mechanism of the Claisen condensation in fatty acid biosynthesis (acetyl-ACP + malonyl-ACP), (2) the polyketide natural products — how iterative Claisen condensations build the carbon skeleton of erythromycin, lovastatin, and tetracycline, (3) a comparison: how does the in vitro enolate chemistry differ from the enzymatic version — what does the enzyme add beyond just pKa adjustment?
- Prompt seed: `claude "Research the enolate chemistry of natural product biosynthesis. (1) Acetyl-CoA as enolate precursor: why is the alpha-carbon of a thioester more acidic than a regular ketone (pKa comparison), and what is the Claisen condensation mechanism in fatty acid synthase (FAS)? (2) Polyketide biosynthesis: how do iterative Claisen condensations build the carbon skeleton of 3 major polyketide natural products (erythromycin, lovastatin, tetracycline)? (3) What does the enzyme add — how does FAS control regio- and stereo-chemistry vs the uncontrolled in vitro reaction? Cite biochemistry primary sources."`
- Read / check: Verify the thioester alpha-carbon pKa is lower than a ketone's (~14 vs ~20). Check that the Claisen mechanism is correct (decarboxylative condensation via malonyl-ACP). Confirm at least 2 of the 3 polyketides are correctly described as polyketide products.
- Human supplies: Nothing — Claude synthesizes from biochemistry/natural products literature. A natural products chemist would validate the biosynthesis details.
- Output medium: slate (3-panel brief with a comparative mechanism table — in vitro enolate vs FAS — as a Remotion visualization)
- The change: Find the total number of known polyketide natural products and what fraction are or were pharmaceutical drugs — framing the biosynthesis as a combinatorial chemistry engine.
- Teardown angle: Fatty acid biosynthesis is undergraduate enolate chemistry running in a protein factory. The enzyme doesn't change the mechanism — it controls the outcome. Understanding the mechanism means understanding the enzyme's job.
- Exclusions: Full FAS structure/function, modular PKS type I/II/III classification, synthetic biology applications.
- Score: 8/10
