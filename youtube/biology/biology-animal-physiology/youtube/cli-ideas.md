# Animal Physiology — CLI Video Ideas ("X with Claude")

## Candidate 01 — "Research the SA/V Paradox: Why Doesn't Kleiber's Law Come Out to 2/3?"
- Source: biology-animal-physiology/chapters/01-body-plans-homeostasis.md
- Lane: RESEARCH (Claude assistant)
- Hook: Surface-area-to-volume geometry predicts metabolic scaling at a 2/3 power law — but Kleiber's empirical law is 3/4. The gap has been argued over for ninety years with no settled winner.
- The artifact: A sourced three-argument brief comparing the three leading explanations (fractal supply networks, mitochondrial constraints, statistical convergence), with a summary table rating each argument's empirical support and a verdict on which is most defensible in 2025.
- Prompt seed: `claude "I'm researching why metabolic scaling in animals follows mass^(3/4) rather than the mass^(2/3) predicted by simple SA/V geometry. Gather the three leading explanations — fractal network models (West-Brown-Enquist), mitochondrial surface constraints, and statistical averaging — and produce a comparison table rating each on: (a) empirical fit, (b) falsifiability, (c) whether it predicts the exponent from first principles. Cite primary sources for each. End with a one-paragraph verdict on which explanation is most defensible today."`
- Read / check: Verify that the brief cites West, Brown & Enquist (1997) for the fractal model, Daan et al. for mitochondrial constraints, and at least one critique (e.g., Kozlowski & Konarzewski 2004). The verdict must engage the empirical exponent range (0.65–0.80 across taxa) rather than treating 3/4 as exact.
- Human supplies (Claude can't): Nothing — fully synthetic. The sourced brief is the deliverable; no wet-lab data needed. A real log-log dataset (e.g., from Savage et al. 2004) would strengthen but is not required for the video.
- Output medium: Manim (animated log-log scatterplot of mass vs. metabolic rate, curve drawing from 2/3 to 3/4 exponent with taxa dots appearing, then the three-argument comparison table assembling column by column)
- The change: Ask Claude to add a fourth argument — the "4th dimension of time" hypothesis — and re-rate the table.
- Teardown angle: The 3/4 vs. 2/3 debate shows that a number measured in thousands of species across a century can still be mechanistically unexplained. Empirical regularity is not the same as understanding.
- Exclusions: Developmental scaling, intraspecific scaling within a species, plant metabolic scaling (separate literature).
- Score: 8/10

## Candidate 02 — "Research Endotherm vs. Ectotherm: How Much Does Thermoregulation Really Cost?"
- Source: biology-animal-physiology/chapters/01-body-plans-homeostasis.md
- Lane: RESEARCH (Claude assistant)
- Hook: An ectotherm uses roughly one-tenth the energy of a same-sized endotherm. That single number means a lizard can go weeks without food that would kill a mouse in hours — but it also locks the lizard out of the polar world. Can Claude find the best-documented cost estimate and its caveats?
- The artifact: A sourced brief with (a) the best empirical estimate of the endotherm/ectotherm metabolic ratio across body masses, (b) two documented exceptions or complicating cases (e.g., tuna regional endothermy, torpor), and (c) a one-page cost-benefit table for each strategy across five ecological scenarios.
- Prompt seed: `claude "I'm studying the energetic cost of endothermy vs. ectothermy in vertebrates. Produce: (1) the best empirical estimate of the metabolic rate ratio (endotherm:ectotherm) at equivalent body mass, with citations; (2) two documented exceptions or hybrid strategies; (3) a cost-benefit table for each strategy across five scenarios: polar habitat, desert, tropical forest, ocean, high-altitude. Cite primary literature throughout."`
- Read / check: Confirm the ratio cited (~10:1 at rest) is sourced to Bennett & Ruben (1979) or equivalent. The exceptions should include tunas or lamnid sharks (regional endothermy) and at least one torpor-using mammal. The table should include specific named species.
- Human supplies (Claude can't): Nothing — fully synthetic. Real telemetry data on field metabolic rates (e.g., doubly-labeled water studies) would add authenticity but the synthesized brief is the video deliverable.
- Output medium: Manim (split-screen animated bar chart comparing basal metabolic rates, then scenario table assembling with color-coded pros/cons per cell)
- The change: Ask Claude to find one case where the cost-benefit flips — a scenario where ectothermy outperforms endothermy even in a cold environment.
- Teardown angle: The "endothermy is superior" narrative collapses on inspection: ectotherms dominate by species count and have outlasted most endotherm lineages in geological time. The strategy you call "primitive" is the one most of life uses.
- Exclusions: Invertebrate thermoregulation, plant thermogenesis, the debate about dinosaur physiology.
- Score: 8/10

## Candidate 03 — "Research the Action Potential: Build the Hodgkin-Huxley Simulator with Claude"
- Source: biology-animal-physiology/chapters/04-neurons-nervous-system.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: The Hodgkin-Huxley equations describe the action potential so precisely that a simulation built from two channel types still matches recordings from living neurons today. Can you build and run that model in under forty lines of Python?
- The artifact: A working Python script (`hh_sim.py`) that simulates a single action potential using simplified HH equations, plots Vm vs. time with Na+/K+ conductance traces, and prints conduction velocity for unmyelinated vs. myelinated modes at configurable diameter.
- Prompt seed: `claude "Build hh_sim.py: a Python script that simulates one action potential using simplified Hodgkin-Huxley equations (INa, IK, IL currents; resting potential -70 mV; threshold ~-55 mV). Plot Vm vs time (0-20 ms) with Na+ and K+ conductance on a second panel. Add a conduction velocity calculation: unmyelinated v ∝ sqrt(diameter), myelinated v ∝ diameter, with presets for squid giant axon (1000μm, 18°C) and mammalian Aα (20μm, 37°C). Temperature Q10=3 for channel kinetics. Comment every constant with its source or mark it VERIFY."`
- Read / check: Run the script. Verify: (1) Vm traces through depolarization, peak ~+40 mV, repolarization, afterhyperpolarization; (2) squid preset gives ~25 m/s; (3) mammalian preset gives ~120 m/s; (4) sub-threshold stimulus returns to rest without spiking; (5) every constant is commented with a source or VERIFY flag.
- Human supplies (Claude can't): Nothing — fully synthetic. The chapter provides all parameter values needed. Real patch-clamp recordings would validate the model but are not required for the video.
- Output medium: screen-recording mp4 (terminal showing Claude generating the script, then matplotlib window showing the animated Vm trace and conductance panels)
- The change: Ask Claude to add a temperature sweep from 10°C to 37°C and plot conduction velocity vs. temperature for both axon types, showing the crossover point.
- Teardown angle: Hodgkin and Huxley wrote the equations in 1952 from a squid nerve. They describe your neurons. The universality of the ion-channel toolkit across 600 million years of evolution is the real finding — not the squid.
- Exclusions: Full multi-compartment cable models, synaptic network dynamics, glial contributions.
- Score: 9/10

## Candidate 04 — "Research the Countercurrent Miracle: Why Fish Gills Extract More O₂ Than Mammal Lungs"
- Source: biology-animal-physiology/chapters/09-gas-exchange-respiratory.md
- Lane: RESEARCH (Claude assistant)
- Hook: Fish gills extract up to 80% of dissolved oxygen from water, while mammal lungs extract only 25% from air — yet water holds 25x less O₂ than air per liter. The countercurrent exchanger is the engineering reason. Can Claude explain and quantify it?
- The artifact: A sourced comparison document: (a) Fick's law applied to both media with actual numbers, (b) a diagram description of countercurrent vs. cocurrent exchange with extraction efficiency estimates, (c) a species table showing real O₂ extraction efficiencies for at least three fish and three terrestrial vertebrates.
- Prompt seed: `claude "Research the physics of countercurrent gas exchange in fish gills vs. tidal ventilation in mammalian lungs. Produce: (1) Fick's law applied to both systems with actual numbers (O2 solubility in air vs. water, surface area estimates, barrier thickness); (2) a prose description of why countercurrent flow produces higher extraction efficiency than concurrent or tidal flow; (3) a table of measured O2 extraction efficiencies for at least 3 fish species and 3 terrestrial vertebrates, with citations."`
- Read / check: Verify the O₂ solubility numbers (~8 mL/L water vs. ~210 mL/L air at sea level). The efficiency table should cite actual measurements (e.g., Randall et al. or Schmidt-Nielsen). The countercurrent explanation must include the partial-pressure gradient logic, not just label it "more efficient."
- Human supplies (Claude can't): Nothing — fully synthetic. Published efficiency measurements exist in the comparative physiology literature and Claude should be able to retrieve them with citations.
- Output medium: Manim (animated countercurrent exchanger schematic showing O₂ partial pressure in blood and water along the gill length, curves converging toward maximum extraction, then flip to a tidal-lung schematic showing dilution)
- The change: Ask Claude to find one aquatic animal that does NOT use countercurrent exchange and explain how it compensates (e.g., lungfish, air-breathing catfish).
- Teardown angle: The mammalian lung is not optimized for O₂ extraction — it is optimized for CO₂ clearance and tidal flexibility. Calling it "advanced" misses that fish have a more efficient gas-exchanger; mammals traded extraction for versatility.
- Exclusions: Bird parabronchial flow (separate system), hemoglobin chemistry, altitude physiology.
- Score: 8/10

## Candidate 05 — "Build the Osmoregulation Cost Calculator with Claude"
- Source: biology-animal-physiology/chapters/11-osmoregulation-excretion.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: A freshwater perch may spend 10–20% of its energy budget just pumping ions against the gradient the pond is constantly pushing through its gills. Can Claude build a script that calculates this cost across species?
- The artifact: A Python script (`osmo_cost.py`) that takes habitat osmolarity, blood osmolarity, body mass, and metabolic rate as inputs, estimates the osmotic work (in watts) required to maintain the gradient, and expresses it as a percentage of total metabolic budget. Includes presets for freshwater fish, marine teleost, desert mammal, and salmon (both life stages).
- Prompt seed: `claude "Build osmo_cost.py: a Python script that estimates the energetic cost of osmoregulation. Inputs: habitat osmolarity (mOsm/L), blood osmolarity (mOsm/L), gill/body surface area (cm²), ion permeability coefficient (nmol/cm²/s/mOsm), body mass (g), total metabolic rate (mW). Output: osmotic work in mW, percentage of total metabolic budget. Include presets: freshwater perch, marine tuna, Australian hopping mouse, salmon-freshwater stage, salmon-marine stage. Comment every equation with its physical basis."`
- Read / check: Verify the osmotic work equation uses thermodynamic principles (work = RT × flux × ln[gradient]). The freshwater fish preset should return 10–20% of metabolic budget. The salmon switchover between presets should show the sign reversal of the ion flux direction. All constants should be commented.
- Human supplies (Claude can't): The ion permeability coefficient varies by species and requires literature values — Claude should flag this with VERIFY and use a mid-range estimate. Real measurements (e.g., from Evans 1979 or Kirschner 1980) would be needed for strict accuracy.
- Output medium: screen-recording mp4 (terminal running the script, then a bar chart animating osmoregulation cost % across the five presets, with salmon shown in both stages side by side)
- The change: Ask Claude to add a slider-style sensitivity analysis: how much does the cost change if gill permeability doubles (e.g., during a parasitic infection)?
- Teardown angle: The hopping mouse and the salmon are solving the same equation in opposite directions. The osmoregulation cost is the price of geographic freedom — quantifiable, not metaphorical.
- Exclusions: Nitrogen excretion costs, urea synthesis in elasmobranchs, renal architecture modeling.
- Score: 8/10

## Candidate 06 — "Research the Three-Heart Octopus: Comparative Cardiovascular Engineering"
- Source: biology-animal-physiology/chapters/10-the-circulatory-system.md
- Lane: RESEARCH (Claude assistant)
- Hook: An octopus has three hearts. A crocodile has a four-chambered heart with a manual bypass valve. A giraffe pushes blood at twice human pressure. Each one is a hydraulic argument — and Claude can map all three in one session.
- The artifact: A sourced comparative brief covering: (a) the octopus three-heart circuit and why gill friction forced the solution, (b) the crocodile foramen of Panizza and its dive function, (c) the giraffe blood-pressure numbers and the rete mirabile mechanism, (d) a comparison table: species / cardiac pressure / key structural innovation / evolutionary pressure that drove it.
- Prompt seed: `claude "Research comparative cardiovascular engineering in three animals: (1) Octopus vulgaris — three-heart circuit, role of branchial hearts, gill hydraulics; (2) American alligator — four-chambered heart with foramen of Panizza, cardiac shunting during dives; (3) reticulated giraffe — systolic blood pressure measurements, rete mirabile, venous valve anatomy. For each: cite primary measurements, explain the engineering problem the anatomy solves, and flag any contested claims. End with a comparison table: species | cardiac pressure (mmHg) | key innovation | evolutionary driver."`
- Read / check: Verify octopus branchial heart anatomy against Wells (1983); alligator shunting against Farmer & Carrier (2000); giraffe pressure against Van Citters et al. (1968) or more recent telemetry. The comparison table should have specific mmHg values, not ranges.
- Human supplies (Claude can't): Nothing — fully synthetic. All three cases are well-documented in the comparative physiology literature.
- Output medium: Manim (three-panel animated schematic: octopus three-heart circuit with flow arrows, crocodile heart with foramen opening/closing during dive, giraffe body silhouette with pressure gradient annotated from heart to head)
- The change: Ask Claude to find a fourth case — the tuna with regional endothermy and its cardiovascular adaptations — and add it to the table.
- Teardown angle: "Primitive" open circulation in squids is not primitive — cephalopods independently evolved the most sophisticated invertebrate heart architecture to solve the same pressure problem vertebrates solved. Convergence is the signal.
- Exclusions: Insect open circulation, hagfish primitive features, lymphatic system comparisons.
- Score: 8/10

## Candidate 07 — "Research Endocrine Disruption: What Atrazine Does to a Frog's Sex"
- Source: biology-animal-physiology/chapters/07-the-endocrine-system.md
- Lane: RESEARCH (Claude assistant)
- Hook: Atrazine is a herbicide with no structural resemblance to any frog hormone — and yet it converted male frogs' testes into mixed-sex gonads by upregulating a single enzyme. Can Claude trace the mechanism from molecule to gonad?
- The artifact: A sourced mechanistic brief: (a) atrazine's effect on aromatase expression with the Hayes et al. 2002 data, (b) the steroid hormone pathway from testosterone to estradiol and its gonadal consequences, (c) a comparison to two other documented endocrine disruptors (e.g., BPA, DDT) with their mechanisms and affected species, (d) a brief on the regulatory status of atrazine in the US vs. EU.
- Prompt seed: `claude "Research the endocrine disruption mechanism of atrazine in amphibians. Produce: (1) a step-by-step mechanism from atrazine exposure to aromatase upregulation to gonadal feminization, citing Hayes et al. 2002 PNAS; (2) the normal testosterone→estradiol pathway and how aromatase disruption derails it; (3) comparison to two other endocrine disruptors (BPA, DDT or similar) — mechanism, receptor target, affected species; (4) current regulatory status of atrazine: US EPA vs. EU ban. Flag any contested findings."`
- Read / check: Verify the Hayes et al. 2002 citation (PNAS, male frogs with intersex gonads). The mechanism must correctly identify aromatase as a CYP19A1 enzyme. The regulatory comparison should note atrazine is banned in EU but still used widely in US as of 2024.
- Human supplies (Claude can't): Nothing — fully synthetic. The Hayes et al. controversy (industry-funded counter-studies) is documented and Claude should surface it.
- Output medium: slate (research brief rendered as an annotated document slate with the aromatase pathway diagram; the controversial Hayes vs. industry-counter-study timeline as a visual)
- The change: Ask Claude to find a case where endocrine disruption affects a non-reproductive axis (e.g., thyroid disruption by perchlorate in amphibians).
- Teardown angle: Atrazine's effect wasn't targeted — it hit a conserved enzyme. Steroid hormone pathways are so ancient and so conserved that a molecule that disrupts one vertebrate sex determination pathway disrupts them all. That's not a frog problem. That's a vertebrate problem.
- Exclusions: Human epidemiological data on atrazine (contested, different chapter), pesticide chemistry, regulatory economics.
- Score: 7/10

## Candidate 08 — "Research the Adaptive Immune System: Why Did It Only Evolve Once?"
- Source: biology-animal-physiology/chapters/12-the-immune-system.md
- Lane: RESEARCH (Claude assistant)
- Hook: Every animal phylum on Earth has innate immunity. Only vertebrates have adaptive immunity — antibodies, T cell receptors, memory — and within chordates only jawed vertebrates have the full system. An invention this useful, appearing exactly once. Why?
- The artifact: A sourced brief: (a) the RAG transposon hypothesis for V(D)J recombination origin, (b) why the sea urchin's 222 TLRs represent an alternative extreme — diversity without adaptive memory, (c) the jawless vertebrate (lamprey) adaptive-immunity workaround (VLR genes), (d) a timeline of immune system evolution with key lineage divergences.
- Prompt seed: `claude "Research the evolutionary origin of vertebrate adaptive immunity. Produce: (1) the RAG transposon hypothesis — how RAG1/RAG2 derived from a Transib transposon and enabled V(D)J recombination, with citations; (2) sea urchin genome data on TLR/NLR diversity as an alternative to adaptive immunity; (3) the lamprey variable lymphocyte receptor (VLR) system as a parallel adaptive solution; (4) a timeline of key immune system evolution events from the bilaterian ancestor to jawed vertebrates. Cite primary sources for each."`
- Read / check: Verify the RAG-transposon hypothesis against Kapitonov & Jurka (2005) or Huang et al. (2016). The sea urchin TLR number (222) should be sourced to the sea urchin genome paper (Sea Urchin Genome Sequencing Consortium, 2006). The VLR comparison should cite Pancer et al. (2004) or Guo et al.
- Human supplies (Claude can't): Nothing — fully synthetic. All cited findings are published in primary literature.
- Output medium: Manim (animated phylogenetic tree of vertebrates with immune system components lighting up at each branch: TLRs at bilaterian ancestor, VLRs at jawless vertebrates, V(D)J recombination at jawed vertebrates)
- The change: Ask Claude to explain why jawless vertebrates (lampreys) evolved a parallel adaptive-immunity system (VLRs) rather than inheriting RAG — and what that implies about the probability of adaptive immunity evolving independently.
- Teardown angle: "Complex" adaptive immunity is not the pinnacle — it's one solution that happened to win in jawed vertebrates. The sea urchin with 222 TLRs and the lamprey with VLRs are running equally functional immune programs by completely different mechanisms. The lock didn't demand one key.
- Exclusions: Autoimmunity, vaccine mechanisms, complement system evolution.
- Score: 7/10

## Candidate 09 — "Build the Hox Gene Body Plan Simulator with Claude"
- Source: biology-animal-physiology/chapters/14-development-capstone.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: Hox genes are address labels for the body — moving the boundary of one Hox domain can turn a leg into an antenna or double a fly's wings. Can Claude build a Python visualizer that shows how Hox domain shifts produce different body plans?
- The artifact: A Python script (`hox_sim.py`) that represents a linearized body axis divided into N segments, assigns Hox gene expression domains (from a configurable table), and shows the resulting body-plan structure. Allows the user to shift domain boundaries and instantly see the morphological consequence.
- Prompt seed: `claude "Build hox_sim.py: a Python/matplotlib script that visualizes Hox gene expression along a body axis. Input: N segments (default 15), a table of Hox genes (Hox1–Hox13) with their anterior and posterior expression boundaries. Output: a color-coded body-axis diagram showing which Hox gene is dominant in each segment, labeled with the structure that segment produces (head, cervical, thoracic, lumbar, sacral, caudal). Add three presets: mouse, Drosophila (10 Hox genes in 3 complexes), and a hypothetical homeotic mutant where Hox6 boundary shifts 2 segments anteriorly. Show the mutant phenotype in a side-by-side panel."`
- Read / check: Verify the Drosophila Hox complex structure (three complexes: ANT-C, BX-C). The mouse preset should show 39 Hox genes organized in 4 clusters. The mutant panel should show a vertebral transformation consistent with real Hox knockout phenotypes (e.g., cervical ribs from Hox5 expansion).
- Human supplies (Claude can't): Hox gene boundary tables require literature values — Claude should flag these with VERIFY and use canonical textbook values from Carroll's "Endless Forms Most Beautiful" or equivalent. Real ChIP-seq data on Hox expression boundaries would improve accuracy.
- Output medium: screen-recording mp4 (terminal running the script, then matplotlib window showing the body-axis color diagram with the homeotic mutant comparison)
- The change: Ask Claude to add an evolutionary comparison: show how the same Hox gene set produces an insect (few Hox domains), a fish (more segments), and a snake (hundreds of trunk segments with expanded Hox expression).
- Teardown angle: The diversity of animal body plans is not written in different genetic alphabets — it is written in the same alphabet, re-punctuated. Hox genes are the punctuation marks, and evolution changes where the marks fall.
- Exclusions: Hox gene regulatory networks, ParaHox genes, non-Hox patterning (Wnt, BMP gradients).
- Score: 7/10

## Candidate 10 — "Research the LTP Mechanism: From Synapse to Long-Term Memory"
- Source: biology-animal-physiology/chapters/05-brain-neural-integration.md
- Lane: RESEARCH (Claude assistant)
- Hook: Eric Kandel spent forty years showing that memory is a physical change at a synapse. Long-term potentiation — LTP — is now the best-documented candidate mechanism for learning in the vertebrate brain. Can Claude trace it from NMDA receptor to gene transcription in one research session?
- The artifact: A sourced mechanistic brief: (a) LTP induction — NMDA receptor as a coincidence detector, Ca²⁺ influx, CaMKII activation; (b) LTP maintenance — AMPA receptor trafficking, structural spine changes; (c) late-phase LTP — CREB-dependent gene transcription, new protein synthesis; (d) the Aplysia simple-system parallel (PKA, CREB) that Kandel used to establish the molecular logic.
- Prompt seed: `claude "Research the molecular mechanism of long-term potentiation (LTP) in the mammalian hippocampus. Produce: (1) early LTP — NMDA receptor as coincidence detector, Ca2+ influx mechanism, CaMKII autophosphorylation, AMPA receptor insertion; (2) structural LTP — dendritic spine enlargement, actin remodeling; (3) late LTP — PKA/MAPK pathway to nucleus, CREB phosphorylation, new protein synthesis requirement; (4) comparison to the Aplysia serotonin→PKA→CREB pathway that Kandel described. Cite primary sources throughout including Bliss & Lømo 1973 for LTP discovery."`
- Read / check: Verify the Bliss & Lømo 1973 citation (the LTP discovery paper). The NMDA receptor section must correctly identify Mg²⁺ block as the voltage-dependent coincidence mechanism. The late-LTP section must include protein synthesis dependence (cite Frey & Morris 1997 or equivalent).
- Human supplies (Claude can't): Nothing — fully synthetic. The LTP mechanism is thoroughly documented in primary literature and review articles.
- Output medium: Manim (animated synapse diagram: NMDA channel with Mg²⁺ block, coincident presynaptic and postsynaptic activity removing the block, Ca²⁺ flooding in, CaMKII activating, AMPA receptors inserting, then zoom out to show spine enlargement)
- The change: Ask Claude to find one documented case where LTP is blocked in a living animal and what the behavioral consequence is (e.g., NMDA receptor knockout mice and the Morris water maze).
- Teardown angle: Kandel's bet on a sea slug paid off for humans. The molecular logic of memory is conserved from a 20,000-neuron gastropod to a 86-billion-neuron primate brain. Biology's most sophisticated capability runs on a mechanism discovered in an animal you can see without a microscope.
- Exclusions: Long-term depression (LTD), hippocampal oscillations, systems consolidation, sleep and memory.
- Score: 7/10
