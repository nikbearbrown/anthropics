# Organic Chemistry with LLMs — CLI Video Ideas ("X with Claude")

> Scout date: 2026-07-12
> Source content: 34 .md files (32 content chapters + frontmatter + back matter). The book is the organic-chemistry text enriched with embedded "Dig Deeper" LLM prompts at key mechanism decision points (e.g., "Why basicity and nucleophilicity diverge," "Why protic solvents push the mechanism," "Explain why SAM is a better methyl donor than methanol"). These LLM exercise prompts are ready-made BUILD/RESEARCH candidates. Sampled: 00-intro, 05-stereochemistry, 06-overview-reactions, 11-alkyl-halides, 19-aldehydes-ketones, 22-alpha-substitution, 29-metabolic-pathways.
> Lane note: All "Dig Deeper" prompts are harvest-ready BUILD candidates (the prompt is already written; the video runs it and shows the output). RESEARCH candidates from mechanism chapters are also strong.

---

## Candidate 01 — "Run the SN1/SN2 Solvent Shift Dig Deeper with Claude"
- Source: organic-chemistry-with-llms/chapters/11-reactions-of-alkyl-halides-nucleophilic-substitutions-and-eliminations.md (LLM Exercise — "Dig Deeper: Why protic solvents push the mechanism")
- Lane: BUILD (Claude Code) + LLM Exercise
- Hook: The book's own "Dig Deeper" prompt is already written: "Explain how switching from DMSO to water shifts a 2° benzylic substrate from SN2 toward SN1." Run it live. The video *is* the exercise — showing what a good response looks like and how to verify it against the textbook rate data.
- The artifact: A screen-recording of the Claude terminal session: the Dig Deeper prompt entered → Claude's response (ΔG‡ for each mechanism, which intermediate is stabilized, why) → the student checks the response against Table 11.1 (relative rates flip with solvent) → a Manim energy diagram rendered from the response showing both mechanism energy profiles side-by-side.
- Prompt seed: `claude "Explain in detail how switching from DMSO (polar aprotic) to water (polar protic) shifts an alkyl halide reaction from SN2 toward SN1, holding everything else constant. Cover: which intermediate is being stabilized, why that matters for the reaction coordinate, and what happens to ΔG‡ for each mechanism. Use a 2° benzylic substrate as your example."`
- Read / check: Verify Claude correctly identifies that protic solvents stabilize the SN1 carbocation transition state (by solvating the developing charge) AND destabilize SN2 by solvating the nucleophile's ground state. Check that ΔG‡ for SN1 decreases and ΔG‡ for SN2 increases with protic solvent. Flag if Claude gives a one-sided answer (only one mechanism discussed).
- Human supplies: Nothing — the prompt is from the book. Anthropic API key. The human verifies against Table 11.1 in the book.
- Output medium: screen-recording mp4 (terminal showing the Dig Deeper prompt run, Claude response, then a Manim energy diagram generated from the response)
- The change: Follow the textbook's verification instruction: look up the rate data for the 2° benzylic substrate in both solvents and show that the ratio matches Claude's ΔG‡ predictions (the CHANGE beat is the numerical verification).
- Teardown angle: The solvent is not a container — it is a reagent. Five orders of magnitude in rate change from changing nothing but the solvent is the most important practical lesson in SN1/SN2 chemistry.
- Exclusions: Derivation of Marcus theory, full computational TS optimization.
- Score: 9/10

---

## Candidate 02 — "Run the Nucleophilicity vs Basicity Dig Deeper with Claude"
- Source: organic-chemistry-with-llms/chapters/11-reactions-of-alkyl-halides-nucleophilic-substitutions-and-eliminations.md (LLM Exercise — "Dig Deeper: Why basicity and nucleophilicity diverge")
- Lane: BUILD (Claude Code) + LLM Exercise
- Hook: HO⁻ is a strong base. I⁻ is a terrible base. Yet iodide is a far better SN2 nucleophile than hydroxide in most solvents. The book's Dig Deeper prompt is already written — run it live and then verify against the rate table.
- The artifact: A screen-recording showing: the Dig Deeper prompt entered → Claude's explanation (polarizability, solvation, kinetic vs thermodynamic) → a Manim animated comparison table showing nucleophilicity vs basicity for 5 anions, with bars growing in opposite orders for the two metrics.
- Prompt seed: `claude "Hydroxide is a much stronger base than iodide (the conjugate acid of HO⁻ is water, pKa = 15.7; the conjugate acid of I⁻ is HI, pKa ≈ −10), but iodide is a better nucleophile than hydroxide in many SN2 reactions. Explain why basicity (affinity for H⁺) and nucleophilicity (affinity for C in an SN2) diverge here. Cover at least: solvent effects in protic vs. aprotic media, polarizability, and the difference between thermodynamic and kinetic basicity."`
- Read / check: Verify Claude addresses all three required topics. Check that the polarizability argument is correct: larger atoms have looser electron clouds, distort more easily, lower kinetic barrier to bond formation. Confirm the solvation explanation is directional (protic solvates OH⁻ more than I⁻ because H-bonding). Flag if Claude mixes up kinetic and thermodynamic basicity.
- Human supplies: Nothing — the prompt is already written in the book. Anthropic API key.
- Output medium: screen-recording mp4 (terminal with Claude response) + Manim (animated dual-bar comparison: nucleophilicity vs basicity)
- The change: Extend to HSAB (Hard-Soft Acid-Base) theory: show how Pearson's classification predicts the same result (soft nucleophile prefers soft electrophile — carbon) and ask Claude to compare the two frameworks.
- Teardown angle: Nucleophilicity is kinetic; basicity is thermodynamic. They measure the same drive in different contexts. The divergence is a reminder that which measure applies depends on what the electrophile is — H⁺ vs C.
- Exclusions: Marcus theory of nucleophilicity, Mayr's electrophilicity scale, radical nucleophilicity.
- Score: 9/10

---

## Candidate 03 — "Build an SN1/SN2/E1/E2 Decision Engine with Claude"
- Source: organic-chemistry-with-llms/chapters/11-reactions-of-alkyl-halides-nucleophilic-substitutions-and-eliminations.md
- Lane: BUILD (Claude Code)
- Hook: Organic chemistry students memorize the SN1/SN2/E1/E2 competition rules — but applying them to a novel substrate requires juggling four variables simultaneously. Claude can build the decision engine that walks through each variable in sequence and outputs the predicted mechanism with confidence.
- The artifact: A Python CLI that takes substrate, nucleophile/base, solvent, and temperature as inputs, applies the decision rules in sequence (substrate sterics → nucleophile type → solvent → temperature → competition prediction), and outputs: (1) mechanism prediction with confidence (HIGH/MEDIUM/UNCERTAIN), (2) the decision path shown as a branching tree, (3) a Manim animation of the competing energy diagrams for the top 2 predicted mechanisms.
- Prompt seed: `claude "Write a Python CLI that predicts the dominant mechanism (SN1/SN2/E1/E2) for an alkyl halide reaction. Inputs: substrate (methyl/primary/secondary/tertiary), reagent (classify as: strong base, weak nucleophile, strong nucleophile+weak base, strong base+bulky, strong nucleophile+strong base), solvent (protic/aprotic), temperature (low <50°C / high >80°C). Apply these rules: tertiary+protic+any nucleophile→SN1/E1 competition (high T favors E1), tertiary+aprotic→E2, secondary+strong base+high T→E2, primary+strong nucleophile+aprotic→SN2. Output: mechanism, confidence, decision path as text tree. Use anthropic SDK to explain the reasoning."`
- Read / check: Verify the prediction is correct for: (a) tert-butyl bromide + H2O + protic → SN1/E1, (b) methyl bromide + CN⁻ + DMSO → SN2, (c) 2-bromopentane + NaOEt + EtOH + 80°C → E2. Check that UNCERTAIN fires when two mechanisms are genuinely competitive. Confirm the decision tree is printed as readable text.
- Human supplies: Nothing — fully synthetic. Anthropic API key.
- Output medium: screen-recording mp4 (terminal showing 3 substrates being classified) + Manim (competing energy diagrams for the top-2 mechanisms)
- The change: Add a "product distribution" output: for a secondary substrate where SN2 and E2 compete, estimate the SN2:E2 ratio based on temperature and base strength — using the principle that higher temperature and bulkier base shift toward elimination.
- Teardown angle: The four-mechanism competition is not four separate rules — it's two variables (substrate sterics → whether carbocation or SN2 TS forms; base/nucleophile → whether C attacks or H is removed) interacting with two levers (solvent, temperature). The decision tree makes the interaction visible.
- Exclusions: Absolute rate calculation (Arrhenius pre-exponentials), NMR stereochemical prediction, flow chemistry.
- Score: 9/10

---

## Candidate 04 — "Run the Stereochemistry R/S Assignment Trainer with Claude"
- Source: organic-chemistry-with-llms/chapters/05-stereochemistry-at-tetrahedral-centers.md
- Lane: BUILD (Claude Code)
- Hook: R/S assignment is a 4-step process with a specific failure mode at every step: wrong priority assignment (Rules 1–3), wrong orientation (step 4), and the double-inversion trap (if the lowest priority is pointing toward you, flip the rotation). Claude can generate unlimited practice substrates and check your assignment.
- The artifact: A Python CLI that generates a random chirality center from a library of substituents (H, CH3, CH2CH3, CH2OH, OH, Cl, Br, COOH, NH2), applies CIP rules to assign priority, determines R or S, and outputs: (1) the molecular formula with substituents labeled (a, b, c, d by priority), (2) the correct R/S assignment with step-by-step reasoning, (3) a check: if the user enters R or S, the program verifies and explains the error if wrong.
- Prompt seed: `claude "Write a Python CLI that: (1) randomly selects 4 substituents from [H, CH3, CH2CH3, CH2OH, OH, Cl, Br, COOH, NH2] for a chiral center, (2) assigns CIP priorities using atomic number and the next-sphere rule, (3) assigns R or S based on the 1→2→3 rotation with substituent 4 pointing away, (4) prints the step-by-step priority assignment and final R/S answer, (5) prompts the user to enter their answer and checks it. Use anthropic SDK to generate a human-readable explanation for each step."`
- Read / check: Verify the priority assignment correctly handles OH > CH2OH (O vs C in the second sphere). Check that the program correctly identifies when the lowest-priority group is wedged (toward viewer) and applies the flip rule. Confirm the step-by-step explanation is correct for at least 3 test cases.
- Human supplies: Nothing — fully synthetic. Anthropic API key.
- Output medium: screen-recording mp4 (terminal showing 3 practice problems generated, user entering answers, corrections displayed)
- The change: Add a "thalidomide mode" where the program generates the actual R and S enantiomers of thalidomide, assigns each, and shows the two structures side by side — connecting the practice to the biological consequence.
- Teardown angle: R/S assignment is the chiral center literacy test. The failure modes are specific and systematic — the program catches them at the step where they happen, not after the wrong answer is submitted.
- Exclusions: Multiple stereocenters (diastereomers), E/Z nomenclature, axial chirality.
- Score: 8/10

---

## Candidate 05 — "Build a Carbonyl Nucleophilic Addition Predictor with Claude"
- Source: organic-chemistry-with-llms/chapters/19-aldehydes-and-ketones-nucleophilic-addition-reactions.md
- Lane: BUILD (Claude Code)
- Hook: The Bürgi–Dunitz angle is 105° for nucleophilic attack on a carbonyl. But the reactivity varies 1000-fold across the carbonyl series — formaldehyde vs acetophenone. Claude can build the predictor that ranks addition favorability and shows the trajectory.
- The artifact: A Python script that takes a nucleophile (from a menu: H2O, HCN, RMgX, NaBH4, LiAlH4, RNH2, ROH) and a carbonyl compound (from a menu: formaldehyde, acetaldehyde, acetone, benzaldehyde, acetophenone) and outputs: (1) the product name and SMILES, (2) the relative reactivity rating (HIGH/MEDIUM/LOW) with electronic + steric reasoning, (3) a Manim animation of the Bürgi–Dunitz trajectory showing the nucleophile approaching at 105°.
- Prompt seed: `claude "Write a Python CLI that takes a nucleophile (from: water, HCN, Grignard, NaBH4, LiAlH4, primary amine, alcohol) and a carbonyl compound (from: formaldehyde, acetaldehyde, acetone, benzaldehyde, acetophenone) and: (1) names the product (gem-diol, cyanohydrin, alcohol, imine, hemiacetal), (2) rates reactivity (HIGH if formaldehyde/aldehyde + strong Nu; MEDIUM if ketone + mild Nu; LOW if aryl ketone + weak Nu), (3) gives electronic+steric reasoning in 2 sentences, (4) creates a Manim animation of the nucleophile approaching the carbonyl carbon at 105° (the Bürgi–Dunitz angle) with the π* orbital highlighted. Use anthropic SDK."`
- Read / check: Verify formaldehyde + Grignard → alcohol (HIGH reactivity), acetophenone + water → LOW reactivity (minimal hydration). Check that the product names are correct for each combination. Confirm the Manim animation shows the 105° trajectory explicitly.
- Human supplies: Nothing — fully synthetic. Anthropic API key.
- Output medium: screen-recording mp4 (terminal) + Manim (Bürgi–Dunitz approach animation)
- The change: Add a "competition mode": for cyclohexanone + NaBH4, show the axial vs equatorial hydride delivery preference (equatorial attack gives axial OH) — connecting the Bürgi–Dunitz trajectory to stereochemical outcome.
- Teardown angle: Every nucleophilic addition has the same first step — nucleophile approaches at 105°, π electrons move to oxygen. What changes is who wins the competition between reactivity and equilibrium. The predictor makes that competition explicit.
- Exclusions: Acid/base catalysis mechanism steps, Wolf-Kishner/Clemmensen reduction comparison, acetal formation equilibrium.
- Score: 8/10

---

## Candidate 06 — "Research Enolate Chemistry in Polyketide Biosynthesis with Claude"
- Source: organic-chemistry-with-llms/chapters/22-carbonyl-alpha-substitution-reactions.md + 29-the-organic-chemistry-of-metabolic-pathways.md
- Lane: RESEARCH (Claude assistant)
- Hook: The alpha-carbon of a thioester (like acetyl-CoA) has pKa ~14 — more acidic than a regular ketone. That single structural feature enables all polyketide biosynthesis, including the carbon skeletons of erythromycin, tetracycline, and lovastatin. Claude can trace the connection.
- The artifact: A sourced 3-section brief: (1) why thioesters are more acidic at the alpha-carbon than ketones (resonance argument for thioester, pKa comparison table), (2) the iterative Claisen condensation mechanism in fatty acid synthase (FAS) and polyketide synthase (PKS) — the decarboxylative condensation step explained mechanistically, (3) a natural product shortlist: 3 polyketide natural products with their therapeutic use and the number of Claisen condensations that built their carbon skeleton.
- Prompt seed: `claude "Research the connection between alpha-carbon acidity in thioesters and polyketide natural product biosynthesis. (1) Why is the alpha-carbon of a thioester more acidic (lower pKa) than a regular ketone? Include the resonance argument and a pKa comparison table (acetone vs thioester vs acetyl-CoA). (2) What is the mechanism of the decarboxylative Claisen condensation in fatty acid synthase (FAS)? Describe the malonyl-ACP decarboxylation step and why CO2 loss drives the reaction forward. (3) For 3 polyketide natural products (erythromycin, lovastatin, doxorubicin), state the therapeutic use and how many Claisen condensation steps built the carbon skeleton. Cite primary biochemistry sources."`
- Read / check: Verify the thioester pKa is lower than ketone (~14 vs ~20). Check that the decarboxylative Claisen mechanism is correct (CO2 loss is thermodynamically driven, not just kinetically). Confirm each natural product is correctly identified as a polyketide (not a terpenoid or alkaloid).
- Human supplies: Nothing — Claude synthesizes from biochemistry primary literature. A natural products chemist would validate the biosynthesis mechanism details.
- Output medium: slate (3-panel sourced brief with a pKa comparison table and natural product structure-origin table as Remotion)
- The change: Find the size of the known polyketide natural product space and how many are pharmaceutical drugs — framing the biosynthetic mechanism as a combinatorial platform rather than a specific pathway.
- Teardown angle: Polyketide biosynthesis is iterative alpha-carbon chemistry — the same Claisen condensation repeated with systematic variation. The pharmaceutical density of the polyketide chemical space is direct evidence that alpha-carbon reactivity is the cell's most productive synthetic strategy.
- Exclusions: Full PKS type I/II/III classification, synthetic biology PKS engineering, PKS crystal structure analysis.
- Score: 8/10

---

## Candidate 07 — "Build a Keto-Enol Tautomer Equilibrium Calculator with Claude"
- Source: organic-chemistry-with-llms/chapters/22-carbonyl-alpha-substitution-reactions.md
- Lane: BUILD (Claude Code)
- Hook: For most ketones, the enol content is <0.01%. For 1,3-diketones, it's >75%. The difference is a 6-membered intramolecular hydrogen bond — and Claude can compute the equilibrium for any beta-diketone from first principles.
- The artifact: A Python script that takes a carbonyl compound class (monoketone, aldehyde, ester, beta-diketone, beta-ketoester, beta-diester, nitroalkane), looks up or computes the pKa and Kenol, and outputs: (1) the percent enol at equilibrium in water and in non-polar solvent, (2) the structural reason (intramolecular H-bond availability, conjugation extent), (3) a Manim animation showing the keto-enol equilibrium arrow being drawn, with the enol percentage displayed and updating as the compound class changes.
- Prompt seed: `claude "Write a Python script that, for each compound class [monoketone, aldehyde, ester, beta-diketone, beta-ketoester, beta-diester, nitroalkane]: (1) looks up or computes the alpha-H pKa and the keto-enol equilibrium constant (Kenol = [enol]/[keto]) from standard tables, (2) computes the percent enol content in water vs non-polar solvent (enol stabilized more in non-polar by intramolecular H-bond), (3) gives the structural reason in 1 sentence. Create a Manim animation that displays a bar chart of percent enol content for all 7 compound classes, updating as each is added."`
- Read / check: Verify monoketone enol content is ~10⁻⁴ % (acetone: Kenol ~ 6×10⁻⁷). Check that 2,4-pentanedione enol content is ~76% in CDCl3. Confirm the structural reason for 1,3-diketones cites both intramolecular H-bond AND conjugation. Confirm Manim bar chart is visible and labeled.
- Human supplies: Nothing — the equilibrium constants are standard textbook values. Anthropic API key.
- Output medium: Manim (animated bar chart + terminal CLI output)
- The change: Add a "reaction mode" where the user picks a compound and asks whether alpha-substitution (alkylation or halogenation) would work — the program uses the pKa to predict whether NaOH, LDA, or only a strong base like NaH would achieve the enolate.
- Teardown angle: Keto-enol tautomerism looks like a curiosity until you see the 76% enol content of acetylacetone. The intramolecular H-bond is not decorative — it is the reason beta-diketones are practical synthetic handles while monoketones are not.
- Exclusions: Kinetic vs thermodynamic enolate selectivity (regioselectivity with LDA vs NaOEt), alpha-carbon racemization rates.
- Score: 8/10

---

## Candidate 08 — "Build a Glycolysis Mechanism Annotator with Claude"
- Source: organic-chemistry-with-llms/chapters/29-the-organic-chemistry-of-metabolic-pathways.md
- Lane: BUILD (Claude Code)
- Hook: Every step of glycolysis is a named organic reaction — retro-aldol, E1cB elimination, SN2-type phosphoryl transfer, oxidative phosphorylation. Claude can annotate each of the 10 steps with the organic mechanism type and animate the ATP bookkeeping.
- The artifact: A Manim animation of the 10 glycolysis steps: each step displays substrate → enzyme → product, with the organic mechanism type labeled below (in chemistry vocabulary, not biochemistry vocabulary), a running ATP/NADH tally in the corner, and a color coding: phosphorylation (blue), isomerization (gray), cleavage (red), oxidation (orange), phosphate transfer (green).
- Prompt seed: `claude "Create a Manim animation of the 10 glycolysis steps. For each step: display substrate name → enzyme name → product name (abbreviated), and annotate below with the organic mechanism type in chemistry vocabulary: step1 = 'SN2-type phosphoryl transfer (kinase)', step4 = 'retro-aldol cleavage', step5 = 'ketose-aldose isomerization', step6 = 'oxidative acyl phosphorylation', step9 = 'E1cB-type dehydration', step10 = 'dephosphorylation'. Include a corner counter: -2 ATP (steps 1,3), +2 NADH (step 6), +4 ATP (steps 7,10). Color code by mechanism type. Animate sequentially."`
- Read / check: Verify the mechanism annotations are correct: step 4 (aldolase) is retro-aldol, step 9 (enolase) is E1cB, step 6 (G3PDH) is oxidative acyl phosphorylation. Check that the ATP counter shows net +2 ATP and +2 NADH at the end. Confirm the color coding is consistent across all 10 steps.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (10-step sequential animation with mechanism labels and running counter)
- The change: Extend to the first 4 steps of the TCA cycle: citrate synthase (Claisen-type condensation), aconitase (dehydration/rehydration), isocitrate dehydrogenase (oxidative decarboxylation), alpha-ketoglutarate dehydrogenase (Claisen + CO2) — continuing the organic mechanism annotation.
- Teardown angle: Biochemistry is not a separate discipline — it is organic chemistry run by enzymes at 37°C. The moment you can see "retro-aldol" over the aldolase step, the barrier between the two subjects dissolves.
- Exclusions: Full regulation of glycolysis (PFK allosteric control), gluconeogenesis, pentose phosphate pathway.
- Score: 8/10

---

## Candidate 09 — "Build a Reaction Type Classifier with Claude"
- Source: organic-chemistry-with-llms/chapters/06-an-overview-of-organic-reactions.md
- Lane: BUILD (Claude Code)
- Hook: Every organic reaction is one of four types: addition, elimination, substitution, or rearrangement — plus the polar/radical electron movement axis. Claude can classify any reaction and show the curly arrow logic in one response.
- The artifact: A Python CLI that takes a reaction description (substrate + reagent + product) as text, uses Claude to classify it as addition/elimination/substitution/rearrangement + polar/radical, explains the electron movement, and generates a Manim animation showing the curly arrows for the rate-determining step.
- Prompt seed: `claude "Write a Python CLI that takes a reaction description (e.g., 'propene + HBr → 2-bromopropane') and: (1) classifies it as addition/elimination/substitution/rearrangement AND polar/radical, (2) identifies the nucleophile and electrophile (if polar) or radical center (if radical), (3) describes the electron movement in terms of curly arrows (e.g., 'pi electrons attack H, then Br- attacks the carbocation'), (4) generates a Manim animation showing the 2 curly arrows for the rate-determining step. Use anthropic SDK."`
- Read / check: Verify propene + HBr is classified as polar addition (not radical — no peroxides specified). Check that the Markovnikov product is identified (2-bromopropane, not 1-bromopropane). Confirm the Manim shows the two arrows: π → H (first, electrophilic) and then Br⁻ → carbocation (second).
- Human supplies: Nothing — fully synthetic. Anthropic API key.
- Output medium: screen-recording mp4 (terminal showing 3 reactions classified) + Manim (curly arrow animation for one reaction)
- The change: Add a "wrong classification" mode: give the program an incorrect classification and ask it to identify the specific rule violation — making the validator useful for checking student work.
- Teardown angle: The four-reaction framework is the entire organizing structure of organic chemistry. Slotting every new reaction into it is not optional — it is the act of understanding. The classifier makes that act visible.
- Exclusions: Pericyclic reactions (not covered in the overview chapter), sigmatropic rearrangements, photochemical pathways.
- Score: 8/10

---

## Candidate 10 — "Research the Walden Inversion Discovery Story with Claude"
- Source: organic-chemistry-with-llms/chapters/11-reactions-of-alkyl-halides-nucleophilic-substitutions-and-eliminations.md
- Lane: RESEARCH (Claude assistant)
- Hook: In 1896, Paul Walden ran two reactions and got back the same molecule — but with inverted configuration. It took 41 years and the work of Hughes and Ingold to explain what happened. Claude can reconstruct the discovery story and show why the SN2 mechanism is one of the most satisfying in all of chemistry.
- The artifact: A sourced 4-event timeline: (1) Walden's 1896 experiment — what he did, what he observed, why it was puzzling (same compound, inverted rotation), (2) the 40-year gap — what chemists hypothesized in between, (3) Hughes and Ingold's 1937 explanation — the backside attack geometry, the rate law evidence, the inversion mechanism, (4) the experimental confirmation — how inversion was ultimately proven with chiral substrates and stereospecific product analysis.
- Prompt seed: `claude "Research the discovery of the Walden inversion and the SN2 mechanism. (1) Walden's 1896 experiment: what substrates, what reactions, what optical rotation reversal was observed. (2) The 40 years between: what hypotheses were proposed to explain the inversion before Hughes and Ingold? (3) Hughes and Ingold's 1937 contribution: what evidence (kinetics and stereochemistry) led them to propose backside attack? What does 'bimolecular' mean in this context? (4) Experimental confirmation: how was the inversion mechanism definitively proven (cite the key experiment). Cite primary or historical sources."`
- Read / check: Verify Walden's 1896 date is correct. Check that Hughes and Ingold's contribution is correctly credited (not just "Ingold" alone). Confirm the key confirmatory experiment is cited — the use of chiral deuterium-labeled substrates or the Hughes 1935 kinetics work. Flag if the history is conflated with the mechanism derivation.
- Human supplies: Nothing — Claude synthesizes from history of chemistry literature. A historian of chemistry or physical organic chemist would improve the primary source citations.
- Output medium: slate (4-event timeline rendered as a Remotion animated horizontal timeline with structural diagrams at each event)
- The change: Extend the brief to compare the SN2 inversion to a biological SN2: SAM-dependent methylation with retention vs inversion — showing that the biological SN2 was identified as the same mechanism after the Ingold work.
- Teardown angle: The Walden inversion wasn't explained by intuition — it was explained by taking kinetics seriously. The rate law alone told you both species had to be in the transition state. That is the model for how mechanism is determined from experimental data.
- Exclusions: Full history of stereochemistry (Le Bel, van't Hoff), SN1 mechanism history, Winstein ion-pair discovery.
- Score: 8/10
