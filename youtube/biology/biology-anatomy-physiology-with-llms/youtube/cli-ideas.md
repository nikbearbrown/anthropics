# Anatomy & Physiology with LLMs — CLI Video Ideas ("X with Claude")

---

## Candidate 01 — "Build a Cardiac Cycle Pressure-Volume Loop Animator with Claude Code"
- Source: biology-anatomy-physiology-with-llms/chapters/23-the-cardiovascular-system-the-heart.md (LLM Exercise 2)
- Lane: BUILD (Claude Code)
- Hook: A pressure-volume loop is the heart's signature written in physics — four phases (filling, isovolumetric contraction, ejection, isovolumetric relaxation) that trace a closed loop. Heart failure and hypertension distort that loop in predictable, visible ways. Claude can animate the distortion.
- The artifact: A Python script that plots pressure-volume loops for three conditions: normal heart, dilated cardiomyopathy (heart failure, EF ≈ 25%), and concentric hypertrophy (hypertension). Each loop is parameterized by end-diastolic volume, end-systolic volume, and filling/ejection pressures. Manim animates all three loops forming simultaneously, with labeled arrows showing how stroke volume (loop width) and ejection fraction (ratio) change across conditions.
- Prompt seed: `claude "Write a Python script that plots cardiac pressure-volume loops in Manim. Generate three loops: (1) normal heart (EDV 120 mL, ESV 50 mL, filling pressure 8 mmHg, peak systolic 120 mmHg); (2) dilated cardiomyopathy (EDV 200 mL, ESV 150 mL, EF=25%, reduced contractility shown as flattened upper left corner); (3) concentric hypertrophy (EDV 100 mL, ESV 40 mL, peak systolic 180 mmHg). Animate each loop forming, then display all three with EF labeled for each. Show how stroke volume is the width of the loop."`
- Read / check: Verify stroke volume = EDV − ESV for each case. Verify EF = SV/EDV: normal ~58%, failure ~25%, hypertrophy ~60%. Verify the loop shape reflects isovolumetric phases (vertical segments) and ejection/filling phases (curved segments with volume change).
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated pressure-volume loops forming for three cardiac conditions, EF labeled)
- The change: Add the Frank-Starling effect — show a sequence of loops where increasing preload (higher EDV) shifts the end-systolic pressure-volume relationship upward, demonstrating that a stretched heart contracts more forcefully.
- Teardown angle: The P-V loop is not a diagram of the heart — it is a theorem about what the heart must do to sustain pressure against a closed valve. Every clinical condition distorts it in a geometrically constrained way.
- Exclusions: Cut myocardial oxygen consumption derivation; cut dP/dt analysis; cut detailed aortic impedance modeling.
- Score: 9/10

---

## Candidate 02 — "Simulate the Pacemaker Dominance Hierarchy with Claude Code"
- Source: biology-anatomy-physiology-with-llms/chapters/23-the-cardiovascular-system-the-heart.md (LLM Exercise 1)
- Lane: BUILD (Claude Code)
- Hook: The SA node fires at 70 bpm, the AV node at 40-60 bpm, the ventricles at 20-40 bpm. Cut the SA node and the next fastest takes over — not silence, a different rhythm. This escape hierarchy is not a backup system; it is intrinsic automaticity at three levels, and Claude can simulate all three.
- The artifact: A Python script that models pacemaker automaticity using the funny current (If) mechanism: three oscillators (SA, AV, ventricular Purkinje) each with different spontaneous depolarization rates. Manim animates the membrane potential traces for all three simultaneously, then "cuts" the SA node and shows the AV node's slower rhythm take over after a pause. Then cuts AV — shows the ventricular escape rhythm. Displays bpm live for each active pacemaker.
- Prompt seed: `claude "Build a pacemaker automaticity simulation in Python. Model three pacemaker cells as simplified oscillators: SA node (70 bpm intrinsic rate, threshold at -40 mV), AV node (50 bpm), Purkinje fiber (30 bpm). Use a simple ramp-depolarization model with hyperpolarization reset after each action potential. In Manim, show all three membrane potential traces simultaneously. At t=3s, 'ablate' the SA node — flatten its trace. After a ~1.5s pause, the AV node takes over. At t=8s, ablate the AV node — ventricular escape rhythm begins. Display live bpm."`
- Read / check: Verify the pause duration between SA ablation and AV escape is physiologically plausible (1-2 cardiac cycles at AV rate). Verify the three rates are displayed correctly before and after each ablation. Verify that when each pacemaker is ablated, it stays flat (no more action potentials from that node).
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (three simultaneous pacemaker traces, sequential ablations, live bpm display)
- The change: Add sick sinus syndrome — show the SA node firing irregularly (random variation in cycle length) and the AV node providing compensatory beats when the SA node pauses too long. This is clinically the pattern that requires a pacemaker implant.
- Teardown angle: The escape hierarchy is a safety architecture. The body does not rely on one clock — it runs three clocks in series, each waiting for the faster one above it to fail before taking over.
- Exclusions: Cut ion channel kinetics (HH equations); cut full cardiac electrophysiology; cut pharmacological interventions.
- Score: 9/10

---

## Candidate 03 — "Build a Lung Fick's Law Surface Area Calculator with Claude Code"
- Source: biology-anatomy-physiology-with-llms/chapters/27-the-respiratory-system.md (LLM Exercise 1)
- Lane: BUILD (Claude Code)
- Hook: The lung achieves 70 square meters of gas exchange surface in a chest that holds 6 liters — by branching 23 times. Fick's law says diffusion rate is proportional to area divided by thickness. Pulmonary fibrosis thickens the membrane by micrometers and collapses gas exchange. Claude can animate the branching geometry and the Fick calculation simultaneously.
- The artifact: A Python script that models 23 generations of airway branching: each generation doubles the number of tubes and halves the radius. Computes total cross-sectional area per generation and plots the exponential rise. Computes diffusion rate via Fick's law with parameterized membrane thickness. Manim animates: left panel shows the bronchial tree branching generation by generation with total area displayed; right panel shows a Fick's law bar chart with area vs. thickness as sliders — sliding thickness from 0.5 μm (healthy) to 3 μm (fibrosis) shows diffusion rate collapse.
- Prompt seed: `claude "Write a Python script modeling 23 generations of airway branching. Starting radius = 1.25 cm (trachea). Each generation: radius halves, count doubles. Compute total cross-sectional area per generation (= count × π × r²). Plot the area curve. Then implement Fick's law: rate = A × D × ΔP / T, where D = oxygen diffusivity in tissue (1.5e-9 m²/s), ΔP = 64 mmHg = 8500 Pa, T = membrane thickness. Animate in Manim: branching tree on the left with area counter; Fick bar chart on the right showing rate as T varies from 0.5 μm (normal) to 3 μm (fibrosis)."`
- Read / check: Verify total alveolar surface area at generation 23 reaches roughly 70 m². Verify Fick's law is dimensionally consistent (output in mol/s or mL O₂/s). Verify the fibrosis scenario (3× thickness) produces roughly a 3-fold reduction in diffusion rate.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated branching tree + interactive Fick's law bar chart, fibrosis vs. normal)
- The change: Add dead space — show that generation 1-16 (conducting zone) contributes nothing to gas exchange. Shade these in gray and show the effective fraction of tidal volume that reaches alveoli (500 mL tidal − 150 mL dead = 350 mL alveolar ventilation).
- Teardown angle: The branching architecture is not just anatomy — it is the solution to the Fick's law surface area constraint. Every fork is an equation: more area, lower individual resistance, same total volume.
- Exclusions: Cut surfactant surface tension math; cut compliance derivation; cut spirometry calculations.
- Score: 9/10

---

## Candidate 04 — "Animate the Oxyhemoglobin Dissociation Curve Shifts with Claude Code"
- Source: biology-anatomy-physiology-with-llms/chapters/27-the-respiratory-system.md (LLM Exercise 3)
- Lane: BUILD (Claude Code)
- Hook: The oxyhemoglobin dissociation curve is S-shaped because of cooperativity — and it shifts right exactly where you need it to. Exercising muscle lowers pH, raises temperature, and raises BPG. All three push the curve right. All three cause hemoglobin to dump oxygen in muscle. Claude can animate each shift and show the oxygen delivery increase.
- The artifact: A Python script that implements the Hill equation for hemoglobin oxygen binding: SO₂ = PO₂ⁿ / (P₅₀ⁿ + PO₂ⁿ), where n is the Hill coefficient (~2.7) and P₅₀ is the half-saturation pressure (~26 mmHg). Parameterizes rightward shift via P₅₀ changes for pH, temperature, and BPG. Manim animates: the baseline sigmoid curve at rest, then during exercise — each Bohr effect factor (pH↓, temp↑, BPG↑) shifts the curve right one at a time, and a vertical marker at 20 mmHg (exercising muscle pO₂) shows saturation dropping from 65% to 40%, representing massively increased oxygen delivery.
- Prompt seed: `claude "Implement the oxyhemoglobin dissociation curve in Python using the Hill equation: SO2 = pO2^n / (P50^n + pO2^n), where n=2.7 (Hill coefficient). Baseline P50=26 mmHg. Model three rightward shifts: pH drop (P50 rises to 32 mmHg), temperature rise (P50 rises to 30 mmHg), BPG increase (P50 rises to 34 mmHg). Animate in Manim: draw the baseline curve, then apply each shift sequentially. At each step, show a vertical marker at pO2=20 mmHg (exercising muscle) and display the saturation value. Compute and display the oxygen unloaded per pass (saturation at 100 mmHg minus saturation at 20 mmHg)."`
- Read / check: Verify baseline saturation at 100 mmHg is ~97%. Verify at pO₂=20 mmHg, baseline saturation is ~65% and after full rightward shift is ~35-40%. Verify the Hill equation produces the correct sigmoid shape (nearly flat top, steep middle, leveling bottom).
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated rightward shifts of sigmoid curve, oxygen unloading marker at exercising pO₂)
- The change: Add the altitude scenario — show that at high altitude, alveolar pO₂ drops from 100 mmHg to 40 mmHg, landing on the steep part of the sigmoid. Demonstrate why altitude adaptation (higher hemoglobin concentration, modified P₅₀) is mechanistically necessary.
- Teardown angle: The S-shape is not an accident of protein chemistry — it is cooperativity exploited as a delivery mechanism. The curve is shaped so that loading is efficient (flat top) and unloading is responsive (steep middle). Evolution tuned P₅₀ to sit exactly in the middle of what tissues produce.
- Exclusions: Cut 2,3-BPG synthesis pathway; cut Haldane effect; cut fetal hemoglobin (HbF P₅₀ differences).
- Score: 9/10

---

## Candidate 05 — "Simulate the RAAS Cascade as a Control System with Claude Code"
- Source: biology-anatomy-physiology-with-llms/chapters/30-the-urinary-system.md (LLM Exercise 3)
- Lane: BUILD (Claude Code)
- Hook: The renin-angiotensin-aldosterone system is a hormonal cascade that begins in the kidney and ends by raising blood pressure — from three directions simultaneously: vasoconstriction, sodium retention, and water retention. Claude can build and animate the entire cascade as a control-systems diagram.
- The artifact: A Python script that models the RAAS as a negative feedback loop: blood pressure drop → renin release → angiotensin I → angiotensin II → [vasoconstriction + aldosterone + ADH] → sodium/water retention → blood pressure rises. Uses a simple differential equation model (dBP/dt = cardiac output × vascular resistance − sodium loss). Manim animates the cascade as a flowchart with each arrow activating sequentially when triggered, plus a blood pressure trace on a second panel showing the drop and recovery. Shows the effect of ACE inhibitors (breaking the angiotensin I → II arrow).
- Prompt seed: `claude "Build a RAAS cascade simulator in Python. Model the cascade as a network: blood_pressure → (if BP < 90 mmHg) → renin_release → angiotensinogen → angiotensin_I → (ACE) → angiotensin_II → [vasoconstriction: BP += 20; aldosterone: Na_retained += 1; ADH: water_retained += 1]. Model recovery as BP rising 5 mmHg per second while Na and water are retained. Animate in Manim: a flowchart on the left where each arrow lights up as it activates; a blood pressure trace on the right showing drop then recovery. Add an ACE inhibitor toggle that blocks the angiotensin I→II arrow and shows incomplete recovery."`
- Read / check: Verify the cascade nodes are in correct physiological order (renin → angiotensin I → ACE → angiotensin II → aldosterone, vasoconstriction, ADH). Verify the recovery curve shows BP returning to ~95-100 mmHg. Verify that blocking ACE shows partial recovery (vasoconstriction arm is cut but aldosterone/ADH arms depend on angiotensin II, so all three are impaired).
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated RAAS cascade flowchart + blood pressure recovery trace, ACE inhibitor toggle)
- The change: Show what happens when the RAAS is chronically overactive — as in renal artery stenosis, where the kidney senses falsely low blood pressure and activates RAAS permanently. BP rises, sodium overloads, edema forms. This is why ACE inhibitors are first-line for hypertension with renal involvement.
- Teardown angle: The RAAS is not a blood pressure regulator — it is a volume-depletion responder. It evolved to handle hemorrhage and dehydration. In a salt-rich modern diet, chronically activating it produces sustained hypertension. The system is working correctly in the wrong environment.
- Exclusions: Cut full pharmacokinetics; cut secondary hyperaldosteronism mechanisms; cut detailed renal tubule transport equations.
- Score: 8/10

---

## Candidate 06 — "Build a Cross-Bridge Cycle Animator with Claude Code"
- Source: biology-anatomy-physiology-with-llms/chapters/12-muscle-tissue.md (LLM Exercise 1)
- Lane: BUILD (Claude Code)
- Hook: The myosin head is literally a walking machine — it reaches forward, grabs actin, pivots ten nanometers, releases, and resets. It does this 20 times per second per head. Hundreds of millions of heads do it simultaneously. Claude can animate one cycle at molecular scale.
- The artifact: A Python script that animates the four-state cross-bridge cycle in Manim: (1) cocked myosin head at rest (ATP bound), (2) head binds actin, (3) phosphate release triggers power stroke — head pivots 10 nm, (4) ATP arrives, head releases actin and resets. Shows one actin filament sliding past one thick filament. Adds a second panel with a force trace showing each power stroke as a pulse. Shows rigor mortis state: if ATP is removed, heads lock in state 3 permanently.
- Prompt seed: `claude "Animate the cross-bridge cycle in Manim. Show: (1) cocked myosin head (high-energy state, ATP hydrolyzed to ADP+Pi); (2) head attaches to actin binding site; (3) Pi release triggers 10 nm power stroke — show the actin filament sliding leftward; (4) ATP binds, head detaches, cocked state returns. Run the cycle 5 times. Add a second panel showing a force trace: each power stroke adds a pulse to a cumulative force bar. Then show rigor mortis: ATP disappears, the cycle stops at state 3, the head is locked onto actin, actin cannot slide — label 'rigor.' Use molecular color coding: myosin head in blue, actin in red, ATP in yellow."`
- Read / check: Verify the sequence is (ATP → ADP+Pi as the cocking step, Pi release as the trigger for the power stroke — this is the counterintuitive point: ATP hydrolysis cocks the spring, Pi release fires it). Verify the force trace pulses match each power stroke. Verify rigor occurs at state 3 (post-power-stroke), not state 1.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (molecular-scale cross-bridge cycle animation, 5 cycles, force trace, rigor demonstration)
- The change: Show three muscle types using the same cycle — identical cross-bridge animation, but different calcium triggers: skeletal (troponin/tropomyosin + nerve signal), cardiac (longer AP + extracellular calcium), smooth (calmodulin + latch-bridge state). Same engine, three control systems.
- Teardown angle: The power stroke is driven by phosphate release, not ATP hydrolysis — the hydrolysis just cocks the spring. Most textbooks get this backwards. The force comes from conformational change after Pi leaves, not from ATP breaking.
- Exclusions: Cut latch-bridge kinetics; cut full Huxley sliding filament equations; cut titin mechanics.
- Score: 8/10

---

## Candidate 07 — "Simulate the Countercurrent Multiplier in the Loop of Henle with Claude Code"
- Source: biology-anatomy-physiology-with-llms/chapters/30-the-urinary-system.md (LLM Exercise 2)
- Lane: BUILD (Claude Code)
- Hook: The loop of Henle builds a salt gradient in the kidney medulla without concentrating the urine itself — it builds the conditions for concentration. The descending limb loses water, the ascending limb pumps out salt. Together they multiply a small concentration difference into a 4-fold gradient. Claude can animate the multiplication happening step by step.
- The artifact: A Python script that implements the countercurrent multiplier as a discrete grid: ascending and descending limbs as two columns of compartments. At each step, the ascending limb pumps 200 mOsm of salt out; osmotic equilibrium is reached between the two limbs; the loop shifts downward one compartment (tubular flow). After 6 iterations, the medullary gradient reaches 1200 mOsm at the hairpin turn from 300 mOsm at the top. Manim animates each iteration: compartment osmolarity values update, the gradient visualized as a color heatmap from cortex (blue) to papilla (red), with ADH effect shown by the collecting duct reabsorbing water.
- Prompt seed: `claude "Implement the countercurrent multiplier in Python. Use a 6-compartment model: two columns (descending and ascending limbs), numbered 1-6 top to bottom. At each step: (1) ascending limb pumps 200 mOsm of NaCl into the interstitium; (2) descending limb equilibrates with interstitium (water leaves until osmolarity matches); (3) fluid flows down the descending limb and up the ascending limb by one compartment. Run 20 iterations. Plot the osmolarity gradient that develops. Animate in Manim: show the two columns of compartments, with color-coded osmolarity (blue=300 mOsm, red=1200 mOsm), and the gradient building step by step. Add a collecting duct column on the right that reabsorbs water when ADH is present."`
- Read / check: Verify the final medullary gradient spans 300-1200 mOsm. Verify the descending limb becomes most concentrated at the hairpin turn (highest osmolarity, having lost the most water). Verify the ascending limb becomes hypotonic at the cortex (~100 mOsm) after pumping out salt. Verify the collecting duct only concentrates urine when ADH is shown as active.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated countercurrent multiplier with compartment osmolarity heatmap, ADH-controlled collecting duct)
- The change: Show the desert mammal comparison — increase loop length from 6 to 12 compartments and show the gradient reaching 4000 mOsm. Demonstrate that loop length is the evolutionary dial for urine concentration capacity.
- Teardown angle: The loop does not concentrate urine — it builds the gradient that allows the collecting duct to concentrate urine. These are two different processes. Confusing them is the most common misunderstanding of renal physiology.
- Exclusions: Cut vasa recta capillary gradient preservation; cut acid-base regulation in DCT; cut full Henle kinetics equations.
- Score: 8/10

---

## Candidate 08 — "Research the Ejection Fraction as a Clinical Metric with Claude"
- Source: biology-anatomy-physiology-with-llms/chapters/23-the-cardiovascular-system-the-heart.md (LLM Exercise 4)
- Lane: RESEARCH (Claude assistant)
- Hook: Ejection fraction is the single number that determines most cardiology treatment decisions — yet it is a volume ratio from a 1960s era catheterization lab, now measured by echocardiogram. Claude can trace how a simple ratio became the axis of heart failure classification.
- The artifact: A sourced 3-section research brief: (1) the measurement — how EF is computed (SV/EDV), what normal (55-70%) vs. reduced (HFrEF, <40%) vs. preserved (HFpEF, ≥50%) means clinically; (2) the HFrEF/HFpEF distinction — why preserved EF heart failure is mechanistically different and why most clinical trials historically excluded HFpEF patients; (3) one documented case where EF measurement changed a treatment decision — e.g., the threshold for prophylactic ICD implantation at EF <35%. Includes 4+ verifiable citations.
- Prompt seed: `claude "Research ejection fraction as a clinical metric in cardiology. Provide: (1) how EF is computed and what the normal vs. reduced vs. preserved thresholds are; (2) why HFrEF and HFpEF are mechanistically distinct — what is different at the cellular level between a dilated, weak ventricle (HFrEF) and a stiff, non-compliant one (HFpEF); (3) how EF thresholds drive clinical decisions — specifically, the ACC/AHA guideline for prophylactic ICD implant at EF ≤35% and the evidence base for that threshold. Include at least 4 verifiable citations."`
- Read / check: Verify EF = (EDV − ESV) / EDV × 100%. Verify HFrEF threshold is <40% by major guidelines. Verify the ICD implant threshold is ≤35% EF. Verify that HFpEF trials (TOPCAT, CHARM-Preserved) showed neutral primary endpoints — this is the basis for the mechanistic distinction claim.
- Human supplies: Nothing — fully researchable.
- Output medium: slate (3-section brief with citations; human fills with echocardiogram images showing EF measurement)
- The change: Add the problem with EF as a metric — it is load-dependent (changes with blood volume and vascular resistance), so the same heart can have different EF readings under different conditions. This has led to calls for load-independent indices.
- Teardown angle: EF is not a measurement of contractility — it is a measurement of the ratio of what the heart pumped to what it was holding. It conflates systolic function with loading conditions. The metric persisted because it is easy to measure, not because it is mechanistically ideal.
- Exclusions: Cut full echocardiography protocol; cut speckle-tracking strain analysis; cut molecular biomarker (troponin, BNP) discussion.
- Score: 8/10

---

## Candidate 09 — "Research the Asymmetric Autonomic Control of the Heart with Claude"
- Source: biology-anatomy-physiology-with-llms/chapters/23-the-cardiovascular-system-the-heart.md (LLM Exercise 5)
- Lane: RESEARCH (Claude assistant)
- Hook: The parasympathetic nervous system slows the heart rate markedly — but barely affects the force of contraction. The sympathetic nervous system increases both rate and force. This asymmetry is not a design flaw; it is a deliberate division of function with documented clinical consequences.
- The artifact: A sourced 2-section research brief: (1) the mechanism — acetylcholine from vagal fibers acts on M2 receptors on the SA/AV node (IKACh channels), slowing rate but having little effect on ventricular contractility because ventricular ACh receptor density is low; norepinephrine acts on β1 receptors throughout, increasing rate AND contractility; (2) clinical consequences — why vagal syncope (vasovagal) causes bradycardia without much contractility drop, why the β-blocker mechanism works differently for rate control vs. contractility reduction. Includes 3+ verifiable citations.
- Prompt seed: `claude "Research the asymmetric autonomic control of heart rate and contractility. Provide: (1) the cellular mechanism by which parasympathetic (vagal) stimulation slows heart rate via M2 receptors and IKACh channels, and why it has minimal effect on ventricular contractility (low receptor density, limited ventricular vagal innervation); (2) how sympathetic stimulation via β1 receptors increases both rate AND contractility (via cAMP → PKA → L-type Ca²⁺ channel phosphorylation); (3) one clinical scenario where this asymmetry matters — e.g., vasovagal syncope or β-blocker selection for rate control vs. contractility reduction. Include at least 3 verifiable citations."`
- Read / check: Verify IKACh (G-protein-gated inward rectifier K⁺ channel) is the mechanism for vagal slowing. Verify ventricular vagal innervation is sparse in humans. Verify β1 receptor activation increases both chronotropy and inotropy via cAMP-PKA pathway. Verify β-blocker selectivity (β1 vs. β1/β2) is the pharmacological basis for the clinical distinction.
- Human supplies: Nothing — fully researchable.
- Output medium: slate (2-section brief with citations; human fills with autonomic innervation diagram)
- The change: Contrast with fish and amphibian hearts — which have predominantly parasympathetic control and rely on vagal withdrawal for rate increases. The mammalian system added dense sympathetic innervation for higher metabolic demands. This is an evolutionary addition on top of the ancestral vagal control.
- Teardown angle: The asymmetry is not a side effect of how the nerves happen to be wired — it is a functional specialization. Parasympathetic controls clock speed; sympathetic controls both clock speed and engine power. Two different dials on the same system.
- Exclusions: Cut detailed autonomic ganglia anatomy; cut neurotransmitter reuptake pharmacology; cut adrenal medulla epinephrine contributions.
- Score: 7/10

---

## Candidate 10 — "Research the Malignant Hyperthermia Mechanism with Claude"
- Source: biology-anatomy-physiology-with-llms/chapters/12-muscle-tissue.md (LLM Exercise 5)
- Lane: RESEARCH (Claude assistant)
- Hook: Malignant hyperthermia is a pharmacogenetic emergency — a mutation in the ryanodine receptor that causes volatile anesthetics to trigger uncontrolled calcium release from the sarcoplasmic reticulum. Body temperature rises 1°C every 5 minutes. It is treatable with one drug (dantrolene) that works by closing the very channel that opened. Claude can reconstruct the mechanism from the cross-bridge cycle up.
- The artifact: A sourced 3-section research brief: (1) the normal ryanodine receptor mechanism — how RyR1 opens to release calcium during excitation-contraction coupling, and what normally closes it; (2) the MH mutation — how RYR1 mutations cause hypersensitivity to volatile anesthetics (halothane, sevoflurane), triggering sustained calcium release, sustained cross-bridge cycling, ATP depletion, and heat generation; (3) dantrolene — mechanism of action (RyR1 inhibitor), clinical protocol, and why it works. Includes 4+ verifiable citations.
- Prompt seed: `claude "Research the mechanism of malignant hyperthermia (MH) from the molecular level up. Provide: (1) the normal ryanodine receptor 1 (RyR1) mechanism in excitation-contraction coupling — how it opens during an action potential, how calcium is released and then re-sequestered; (2) how RYR1 gain-of-function mutations cause hypersensitivity to volatile anesthetics — what triggers uncontrolled calcium release, why this causes sustained cross-bridge cycling, ATP depletion, and hyperthermia (rate ≈ 1°C/5 min); (3) dantrolene's mechanism — it blocks RyR1, how quickly it works, and the clinical monitoring protocol. Include 4+ verifiable citations from pharmacology or anesthesiology literature."`
- Read / check: Verify RYR1 mutation is on chromosome 19q13.2. Verify dantrolene mechanism is RyR1 binding (not generalized calcium channel blocker). Verify the temperature rise rate of 1°C per 5 minutes is consistent with published case series. Verify that succinylcholine (depolarizing muscle relaxant) is a trigger alongside volatile anesthetics.
- Human supplies: Nothing — fully researchable.
- Output medium: slate (3-section brief with citations; human fills with RyR1 structure image and dantrolene mechanism diagram)
- The change: Compare with central core disease — another RYR1 mutation condition, but causing muscle weakness rather than hyperactivation, because the mutation in this case causes a channel that is constitutively open but with reduced calcium release capacity. Same gene, opposite functional direction.
- Teardown angle: MH is the cross-bridge cycle running with no off switch. Every myosin head keeps cycling because calcium never drops below the threshold to close the troponin gate. The result is a biochemical fire — ATP burning, temperature rising — from a single broken feedback control.
- Exclusions: Cut complete RYR1 genetic testing protocol; cut all other causes of perioperative hyperthermia; cut neuroleptic malignant syndrome comparison.
- Score: 7/10

---

## Candidate 11 — "Simulate Ventilation-Perfusion Mismatch with Claude Code"
- Source: biology-anatomy-physiology-with-llms/chapters/27-the-respiratory-system.md (LLM Exercise 5)
- Lane: BUILD (Claude Code)
- Hook: A pulmonary embolism ventilates alveoli but stops blood flow. Pneumonia perfuses alveoli but blocks gas diffusion. Both cause hypoxemia — but from opposite directions. The V/Q ratio is the single number that distinguishes them, and Claude can build a simulator that shows both failure modes.
- The artifact: A Python script that models a lung as N alveolar units, each with an independent V/Q ratio. Baseline: V/Q = 0.8 (matched). Pulmonary embolism scenario: one region V/Q → infinity (ventilation, no perfusion). Pneumonia scenario: one region V/Q → 0 (perfusion, no ventilation). Computes overall arterial pO₂ as a weighted average across units. Manim animates a schematic lung divided into three zones, with V (air, blue arrows) and Q (blood, red arrows) shown for each zone. When PE is triggered, blood flow arrows disappear from one zone. When pneumonia is triggered, air arrows disappear. Arterial pO₂ drops in both cases, displayed as a live number.
- Prompt seed: `claude "Build a V/Q mismatch simulator in Python. Model a lung as 3 zones, each with a V/Q ratio and a contribution to total arterial pO₂. Baseline: all zones V/Q = 0.8, total pO₂ = 95 mmHg. Pulmonary embolism mode: zone 2 V/Q → 10 (ventilated but no blood flow) — wasted ventilation, pO₂ drops slightly. Pneumonia mode: zone 2 V/Q → 0 (blood flow but no ventilation) — shunt, pO₂ drops severely. Compute total arterial pO₂ as a weighted sum. Animate in Manim: three alveolar compartments with V (blue) and Q (red) arrows. Toggle PE or pneumonia. Show how arterial pO₂ changes in each scenario and why pneumonia causes worse hypoxemia than PE."`
- Read / check: Verify that a pure shunt (V/Q = 0) contributes deoxygenated blood and cannot be corrected by supplemental oxygen (because ventilation to that unit is zero — more O₂ in the ventilated zone does not reach the shunted unit). Verify that V/Q = infinity (dead space) wastes ventilation but the unaffected zones can compensate more readily. Verify the baseline pO₂ is physiologically correct (~95 mmHg).
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated three-zone V/Q model, PE vs. pneumonia toggle, arterial pO₂ live display)
- The change: Add the 100% O₂ test — show that supplemental O₂ corrects PE-type hypoxemia (ventilated zones load more O₂) but not shunt-type (pneumonia, because blood bypasses ventilated zones). This is the clinical test for distinguishing the two causes at the bedside.
- Teardown angle: V/Q mismatch is not just a lung problem — it is a fundamental limitation of any gas exchange system where flow and ventilation are independent. The lung evolved hypoxic pulmonary vasoconstriction precisely as an automatic corrector for V/Q mismatch.
- Exclusions: Cut full alveolar gas equation; cut respiratory failure scoring systems; cut high-altitude V/Q changes.
- Score: 8/10

---

## Candidate 12 — "Research Jean Hanson and the Sliding Filament Theory with Claude"
- Source: biology-anatomy-physiology-with-llms/chapters/12-muscle-tissue.md (AI Wayback Machine)
- Lane: RESEARCH (Claude assistant)
- Hook: Jean Hanson and Hugh Huxley proposed the sliding-filament theory of muscle contraction in 1954. Textbooks usually credit Andrew Huxley alone. The correction is documented and verifiable — and Claude can reconstruct what Hanson actually contributed and why she was systematically left out.
- The artifact: A sourced 2-section research brief: (1) Hanson's specific contribution — what experiments she ran (X-ray diffraction and electron microscopy of muscle fibers), what she showed (that the thin filaments slide past the thick filaments, and neither set of filaments shortens itself), and how this differed from what was known before 1954; (2) the attribution problem — how the 1954 Nature papers were authored (Hanson & Huxley, Huxley & Niedergerke), what the Royal Society archive and secondary historical sources say about Hanson's role vs. Andrew Huxley's vs. Hugh Huxley's. Includes 3+ verifiable citations.
- Prompt seed: `claude "Research Jean Hanson's contribution to the sliding-filament theory of muscle contraction. Provide: (1) what experiments Hanson conducted with Hugh Huxley at the MRC Biophysics Unit in 1954 — her methods, her findings, and what she demonstrated that was new; (2) how credit for the sliding-filament theory has been distributed historically — why Andrew Huxley and Rolf Niedergerke's parallel 1954 Nature paper is often cited preferentially, and what historical and archival sources say about Hanson's scientific contribution relative to her recognition. Include at least 3 verifiable citations."`
- Read / check: Verify the two 1954 Nature papers: Huxley & Hanson (one paper) and Huxley & Niedergerke (parallel paper). Verify Hanson worked at the MRC Biophysics Unit, King's College London. Verify her technique involved phase contrast microscopy of isolated myofibrils (not just X-ray diffraction). Check that Andrew Huxley and Hugh Huxley are different people.
- Human supplies: Nothing — fully researchable.
- Output medium: slate (2-section brief with citations; human fills with 1954 Nature paper cover image and Hanson portrait)
- The change: Extend to Rosalind Franklin comparison — ask Claude to compare the pattern of attribution in the Hanson/Huxley and Franklin/Watson cases. Are there structural similarities in how credit flowed away from female scientists in mid-20th century British science?
- Teardown angle: The discovery of the mechanism of muscle contraction is one of the most important in physiology. The person who ran the experiments that demonstrated the sliding-filament mechanism is routinely omitted. This is not ancient history — it continues to affect whose work students read.
- Exclusions: Cut full gender bias in science literature review; cut comparison to Marie Curie; cut general scientific credit attribution theory.
- Score: 7/10
