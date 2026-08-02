# Anatomy & Physiology with LLMs — CLI Video Ideas ("X with Claude")

---

## Candidate 01 — "Research the Cardiac Pressure-Volume Loop with Claude" (LLM Exercise)
- Source: anatomy-physiology-with-llms/chapters/23-the-cardiovascular-system-the-heart.md; anatomy-physiology-with-llms/chapters/24-the-cardiovascular-system-blood-vessels-and-circulation.md — LLM Exercise 2 (fourth-power) + Chapter 23 cardiac cycle
- Lane: RESEARCH (Claude assistant)
- Hook: The pressure-volume loop of the left ventricle is not a diagram — it is a full cardiac cycle encoded as geometry. Researching its four phases with Claude, then asking what happens when the loop shifts in heart failure, reveals why echocardiographers call it the most information-dense single figure in cardiology.
- The artifact: A sourced 4-phase walkthrough of the left-ventricle PV loop (filling, isovolumic contraction, ejection, isovolumic relaxation) with EDV, ESV, stroke volume, and ejection fraction labeled, plus a comparison showing how the loop shifts in systolic heart failure (curve shifts down and right) vs. hypertensive heart disease (loop shifts up).
- Prompt seed: `claude "Walk me through the pressure-volume loop of the left ventricle for one complete cardiac cycle. For each of the four phases — filling, isovolumic contraction, ejection, and isovolumic relaxation — explain what is happening to pressure and volume, which valves are open or closed, and why the phase is necessary. Label the end-diastolic volume, end-systolic volume, stroke volume, and ejection fraction on the loop. Then explain how the loop changes in systolic heart failure versus hypertensive heart disease."`
- Read / check: All four phases must be correctly described (isovolumic = volume constant, valve events at corners of loop). EDV ~130 mL, ESV ~60 mL, SV ~70 mL, EF ~54% — verify against textbook. Heart failure curve should shift down (less SV at same EDV); hypertensive loop should shift up/left (stiffer ventricle, higher pressure needed).
- Human supplies: Nothing — fully synthetic. Spot-check EF range against standard clinical values (55–70% normal, <40% heart failure).
- Output medium: Manim (the PV loop traces clockwise in real time, each phase labeled as it draws; a second overlay shows the heart-failure curve shifting; the ejection fraction calculation animates as a shaded area fraction)
- The change: Ask Claude to trace the Frank-Starling relationship on the same diagram — how does increased preload (exercise) shift the loop, and where does the relationship plateau?
- Teardown angle: The loop encodes the entire cardiac cycle in two variables. Once you can read it, an echocardiogram report is not a list of numbers — it is the shape of a failing or thriving heart.
- Exclusions: Coronary anatomy, specific valve pathologies — separate cards.
- Score: 9/10

---

## Candidate 02 — "Research Poiseuille's Fourth Power with Claude" (LLM Exercise)
- Source: anatomy-physiology-with-llms/chapters/24-the-cardiovascular-system-blood-vessels-and-circulation.md — LLM Exercise 2
- Lane: RESEARCH (Claude assistant)
- Hook: Reducing a coronary artery's radius by 50% increases resistance by sixteen-fold — not twofold. The fourth-power relationship is why atherosclerosis produces sudden symptoms after years of silent progression, and Claude can make the cliff visible with a single calculation.
- The artifact: A sourced brief with: (1) the Poiseuille equation explained in plain language with the r⁴ term highlighted, (2) a resistance-vs-radius-reduction table (0%, 20%, 30%, 50%, 60%, 70% narrowing → fold increase in resistance), (3) the clinical explanation for why a coronary artery that is 60% narrowed in cross-sectional area (not radius) produces a different radius reduction than the naive reading suggests, (4) a 100-word brief on why symptoms appear suddenly at ~50–60% narrowing.
- Prompt seed: `claude "Explain Poiseuille's equation in plain language, with special attention to why resistance depends on the fourth power of the radius. Then calculate the change in resistance for these percent reductions in vessel radius: 0%, 20%, 30%, 50%, 60%, 70%. A patient's coronary artery is described as '60% narrowed in cross-sectional area' — what is the actual radius reduction, and what does that imply for resistance? Why do symptoms of coronary artery disease often appear suddenly after years of silent progression?"`
- Read / check: Resistance table: 20% → 2.4×, 50% → 16×, 60% → 39×. Cross-section area narrowing of 60% means radius = √(0.4) ≈ 63% of original, so radius reduced by 37%, resistance ≈ (1/0.63)⁴ ≈ 6.4×. The symptom-threshold explanation should name the cliff shape of the curve.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (resistance curve animates on a two-axis plot: x = percent radius reduction, y = fold resistance increase; the curve steepens dramatically at 50–60%; a vertical marker labeled "symptom threshold" appears; the curve's steep portion is highlighted)
- The change: Ask Claude to extend the analysis to viscosity — what happens to resistance in anemia (lower viscosity) vs. polycythemia (higher viscosity), and is the viscosity effect larger or smaller than a 20% radius change?
- Teardown angle: Physiology has cliffs, not slopes. The linear intuition — "narrower means proportionally less flow" — is wrong by a factor of 16 at the 50% mark. That is the difference between a warning sign and a heart attack.
- Exclusions: Plaque composition, statin mechanisms — tangents.
- Score: 9/10

---

## Candidate 03 — "Research Starling Forces and Edema with Claude" (LLM Exercise)
- Source: anatomy-physiology-with-llms/chapters/24-the-cardiovascular-system-blood-vessels-and-circulation.md — LLM Exercise 3
- Lane: RESEARCH (Claude assistant)
- Hook: Edema is never one thing. It is always a Starling imbalance — but the imbalance can originate from three completely different mechanisms: too much pressure pushing out, too few proteins pulling back, or a leaky wall. Researching all three through Claude's trace of right heart failure to ankle edema makes the diagnostic framework concrete.
- The artifact: A sourced 3-path comparison brief: (1) right-heart-failure edema traced from failing right ventricle → backed-up venous pressure → elevated capillary hydrostatic pressure → net filtration positive at venous end → ankle accumulation, (2) hypoalbuminemia edema (liver disease) traced through reduced oncotic pressure, (3) inflammatory edema traced through increased wall permeability — each path identifying which Starling force changed and in which direction.
- Prompt seed: `claude "Trace the development of ankle edema in a patient with right heart failure: start with the failing right ventricle and trace the pressure changes backward through the venous system to the capillary beds of the lower extremities. At each step, identify which Starling force is changing and in which direction. Then: how would the edema distribution differ in left heart failure compared to right? Give me the same Starling-force trace for a patient with liver cirrhosis causing hypoalbuminemia, and for a patient with acute inflammation in the lower leg."`
- Read / check: Right heart failure → systemic venous hypertension → raised CHP at venous capillary end → net filtration → ankle edema (gravity dependent). Left heart failure → pulmonary edema, not ankle edema (different circulation). Liver cirrhosis → low albumin → low BCOP → reduced reabsorption. All three mechanisms should be traceable through Starling forces, not just named.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (a single capillary diagram redraws three times: normal Starling balance, then each of the three failure modes — CHP arrow, BCOP arrow, or permeability annotation changes — and the resulting fluid accumulation animates)
- The change: Ask Claude which of the three edema types is most amenable to treatment and why — does targeting the Starling force that changed produce the most effective intervention for each?
- Teardown angle: Edema is the same mechanism failing in three different places. The treatment follows the failure mode, not the symptom. This is what pathophysiology is for.
- Exclusions: Lymphatic system anatomy, specific diuretic mechanisms — tangents.
- Score: 9/10

---

## Candidate 04 — "Research the Action Potential Mechanism with Claude" (LLM Exercise)
- Source: anatomy-physiology-with-llms/chapters/15-the-nervous-system-and-nervous-tissue.md
- Lane: RESEARCH (Claude assistant)
- Hook: Stimulate a neuron harder and you do not get a bigger signal — you get the same signal, or nothing. The all-or-nothing law is the strangest design choice in biology, and researching why it exists with Claude, then asking what saltatory conduction adds on top, reveals an elegance that a textbook list of phases cannot capture.
- The artifact: A sourced 4-phase walkthrough of the action potential (resting, depolarization, repolarization, hyperpolarization) with specific ion channels named (voltage-gated Na⁺, voltage-gated K⁺, Na⁺/K⁺ ATPase), plus a comparison of myelinated vs. unmyelinated conduction velocity (100 m/s vs. 0.5 m/s) and the structural explanation for the 200× difference.
- Prompt seed: `claude "Explain the action potential mechanism step by step, naming which specific ion channels open and close in each phase and what happens to membrane voltage. Why is the action potential all-or-nothing — why doesn't a stronger stimulus produce a bigger signal? Then explain saltatory conduction: why does myelination increase conduction velocity from 0.5 m/s to 100 m/s, and what structural feature of the myelin sheath makes this possible? What diseases cause conduction to slow, and why?"`
- Read / check: Depolarization = Na⁺ channels open, Na⁺ rushes in, membrane goes to +30 mV. Repolarization = K⁺ channels open, K⁺ exits, membrane returns negative. All-or-nothing = threshold mechanism, not graded response. Saltatory conduction = action potential jumps node-to-node at nodes of Ranvier, not along entire membrane. Demyelinating disease (MS) should appear in the pathology section.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (voltage trace animates in real time: resting at −70 mV, Na⁺ spike to +30 mV, K⁺ return, hyperpolarization; a parallel myelinated axon diagram shows the signal jumping node-to-node vs. continuous conduction on the unmyelinated axon)
- The change: Ask Claude what happens during the absolute refractory period and why it prevents the signal from traveling backward — then ask what the refractory period implies about the maximum firing rate of a neuron.
- Teardown angle: The all-or-nothing law is not a limitation — it is the design. Binary signals are noise-resistant. The nervous system chose digital over analog, and saltatory conduction is how it made digital fast enough to matter.
- Exclusions: Specific neurotransmitter mechanisms, synaptic integration — separate card.
- Score: 9/10

---

## Candidate 05 — "Research Homeostasis and Negative Feedback with Claude" (LLM Exercise)
- Source: anatomy-physiology-with-llms/chapters/02-an-introduction-to-the-human-body.md — LLM Exercise implicit; Chapter 2 negative feedback section
- Lane: RESEARCH (Claude assistant)
- Hook: Your core temperature does not stay at 37.0°C — it oscillates in a narrow band because feedback loops always lag. Researching three negative-feedback cases with Claude (temperature, blood glucose, blood pressure) and then asking what happens when each is overwhelmed reveals that homeostasis is not a guarantee — it is a design with failure modes.
- The artifact: A sourced 3-case comparison brief: (1) thermoregulation (sensor = skin/hypothalamus, effector = shivering + vasoconstriction, failure = hypothermia stages at 35°C/32°C/28°C), (2) blood glucose regulation (sensor = pancreatic beta cells, effector = insulin release, failure = diabetic hyperglycemia), (3) blood pressure regulation (sensor = aortic/carotid baroreceptors, effector = HR + arteriolar constriction, failure = hypertensive crisis) — each with the sensor→control center→effector loop drawn out and the failure mode named.
- Prompt seed: `claude "Explain negative feedback as the body's mechanism for homeostasis, using thermoregulation as your primary example. Name the sensor, control center, and effector for cold exposure, and trace the loop through to recovery. Then give me the same three-component loop for blood glucose regulation and for blood pressure regulation. For each system, identify the failure mode: what happens when the feedback loop is overwhelmed by a disturbance larger than it was built to handle?"`
- Read / check: Thermoregulation loop: skin thermoreceptors → hypothalamus → blood vessel constriction + shivering → heat generation. Glucose loop: beta cells detect low glucose → glucagon release → glycogenolysis. BP loop: baroreceptors detect drop → sympathetic activation → HR increase + arteriolar constriction. Failure modes should be clinically named (hypothermia, diabetic ketoacidosis, hypertensive crisis).
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (three animated loop diagrams appear in sequence, each as a labeled cycle: sensor → control center → effector → variable → back to sensor; failure mode shows the loop breaking down with an arrow going outside the normal range band)
- The change: Ask Claude to describe a positive feedback loop in physiology (childbirth oxytocin loop, blood clotting cascade) and explain why the body has both negative and positive feedback systems — what function does each serve?
- Teardown angle: Negative feedback is the rule; positive feedback is the exception. Wherever the body runs positive feedback, it needs a hard stop — and when the stop fails, the result is catastrophic.
- Exclusions: Specific endocrine pathways in detail, hormonal cascade names — save for endocrine card.
- Score: 8/10

---

## Candidate 06 — "Research Vessel Wall Architecture with Claude" (LLM Exercise)
- Source: anatomy-physiology-with-llms/chapters/24-the-cardiovascular-system-blood-vessels-and-circulation.md — LLM Exercise 1
- Lane: RESEARCH (Claude assistant)
- Hook: The wall of an artery and the wall of a vein are made of the same three layers — but the proportions are inverted, and the inversion tells you everything about the pressure each vessel carries. Researching vessel architecture with Claude as a "read the wall, guess the pressure" exercise makes the structure-function relationship visceral.
- The artifact: A sourced 3-column table (vessel type, wall composition and relative thickness, pressure range it carries) covering aorta/elastic artery, muscular artery, arteriole, capillary, venule, vein — plus a 150-word brief on why varicose veins form specifically in leg veins and not arm veins, derived from the wall-pressure relationship.
- Prompt seed: `claude "I'm going to describe three blood vessels to you. For each one, identify what type of vessel it is, state its typical blood pressure range, and explain why the wall composition matches that pressure. Vessel A: thick tunica media with wavy elastic fibers and thin tunica externa. Vessel B: thick tunica media with abundant smooth muscle, thin elastic layer, thin tunica externa. Vessel C: a single layer of endothelial cells resting on a thin basement membrane. Then: if you moved from the aorta to the arterioles to the capillaries, what happens to each wall layer and why does each change make physiological sense?"`
- Read / check: Vessel A = elastic artery (aorta), Vessel B = muscular artery, Vessel C = capillary. The aorta → arteriole → capillary sequence should show: elastic fibers decrease, smooth muscle increases then disappears, tunica externa thins progressively, lumen decreases. The varicose vein explanation should cite gravity + valve failure + venous compliance.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (three vessel cross-sections animate in sequence: each appearing as a labeled ring diagram with proportional layer thicknesses; then all three appear simultaneously to show the gradient from artery to capillary to vein)
- The change: Ask Claude what would happen if you transplanted a vein section into an arterial position — what would happen to the wall over days and weeks as it experienced arterial pressure? This is the clinical situation in coronary bypass surgery.
- Teardown angle: The wall is the pressure made visible. Every deviation from the normal architecture is a sign of a pressure that changed — either chronically elevated (arteriosclerosis) or chronically low (venous dilation and valve failure).
- Exclusions: Specific atherosclerosis plaques, lipid biochemistry — tangents.
- Score: 8/10

---

## Candidate 07 — "Research the Cardiac Conduction System with Claude" (LLM Exercise)
- Source: anatomy-physiology-with-llms/chapters/23-the-cardiovascular-system-the-heart.md — SA node, conduction pathway section
- Lane: RESEARCH (Claude assistant)
- Hook: The SA node fires 60–100 times per minute in an isolated dish — no nerves, no neighbors, no external input. Researching how a cell with no stable resting potential generates a heartbeat, and then asking what happens when each backup pacemaker takes over, reveals the hierarchy of a system designed to never stop.
- The artifact: A sourced 5-node conduction pathway brief (SA node → internodal pathways → AV node → bundle of His → Purkinje fibers) with: the prepotential mechanism explained ion-by-ion, timing annotations in milliseconds at each node, the backup pacemaker rates named (100–120 intrinsic, 40–60 AV, 20–40 Purkinje), and the clinical signatures on ECG of each level of conduction failure (prolonged PR = AV block, absent P = ectopic pacemaker, wide QRS = bundle branch block).
- Prompt seed: `claude "Explain the cardiac conduction system from SA node to ventricular apex, naming each node and pathway with timing in milliseconds. Why does the AV node delay the signal by 100 milliseconds — what would happen without that delay? Explain the pacemaker cell's prepotential mechanism: why does a cell with no stable resting potential depolarize spontaneously, and what does the autonomic system adjust to change heart rate? Then describe what happens on an ECG when the SA node fails, when the AV node conducts slowly, and when a bundle branch is blocked."`
- Read / check: SA node 0 ms → AV node ~50 ms (plus 100 ms delay) → bundle of His → apex ~175 ms → base ~225 ms. AV delay allows atrial emptying before ventricular contraction. Prepotential: Na⁺ leak slowly raises membrane from −60 mV to threshold (−40 mV), then Ca²⁺ channels open. ECG signatures: prolonged PR = first-degree AV block, absent P = atrial fibrillation, wide QRS = bundle branch block.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (heart schematic with conduction pathway lighting up node by node on a timeline; ECG trace animates simultaneously below, with each wave labeled as each electrical event reaches the surface; abnormal traces animate as overlays for each pathology)
- The change: Ask Claude what overdrive suppression is and why it means the fastest pacemaker always wins — then ask what happens during a 3-second pause when the SA node fails to fire before the AV node takes over.
- Teardown angle: The conduction system is a hierarchy of backups. Each backup is degraded — slower, less reliable — by design. The degradation is the diagnostic signal that tells you how far up the hierarchy the failure occurred.
- Exclusions: Ion channel pharmacology (lidocaine, beta-blockers) — separate card.
- Score: 8/10

---

## Candidate 08 — "Research the Sickle Cell Cascade with Claude" (LLM Exercise)
- Source: anatomy-physiology-with-llms/chapters/02-an-introduction-to-the-human-body.md; anatomy-physiology-with-llms/chapters/03-the-chemical-level-of-organization.md
- Lane: RESEARCH (Claude assistant)
- Hook: One amino acid substitution in hemoglobin changes the shape of a protein, which changes the shape of a red blood cell, which causes the cell to clog vessels, which causes pain crises that damage organs. Researching the sickle cell cascade with Claude — from single amino acid to systemic disease — makes the organizational hierarchy of the body viscerally real.
- The artifact: A sourced 6-level cascade brief: (1) the valine-for-glutamic-acid substitution at position 6 of the beta-globin chain, (2) how deoxygenated HbS polymerizes into fibers, (3) how fiber polymerization deforms the RBC membrane, (4) how sickled cells occlude capillaries, (5) the downstream vaso-occlusive crisis physiology, (6) the systemic organ damage pattern (spleen autoinfarction, stroke risk, renal disease) — each level connected causally to the next.
- Prompt seed: `claude "Trace the pathophysiology of sickle cell disease from the single amino acid mutation to systemic organ damage. At each level of biological organization — molecular, cellular, tissue, organ, system — explain what changes and why the change at that level causes the problem at the next level. Specifically: why does the valine substitution cause polymerization, why does polymerization cause sickling, why does sickling cause vaso-occlusion, and why does vaso-occlusion cause the specific organ-damage pattern seen in sickle cell disease (spleen, brain, kidney)?"`
- Read / check: Glutamic acid (hydrophilic) → valine (hydrophobic) at position 6: deoxygenated HbS has a hydrophobic sticky patch. HbS-HbS polymerization → fiber formation under low O₂. Rigid, crescent-shaped cells → capillary occlusion. Spleen autoinfarction by age 5 from repeated small infarcts. Stroke risk from large vessel involvement. Renal medullary infarction from low O₂ environment in renal medulla.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (six-panel cascade: each panel shows the level of organization with its specific failure animated — molecule polymerizing, cell deforming, capillary occluding, tissue infarcting — each panel feeding visually into the next)
- The change: Ask Claude to explain why sickle cell trait (one copy of the mutation) confers malaria resistance — how does the same mutation that causes severe disease in homozygotes provide an advantage in heterozygotes?
- Teardown angle: The organizational hierarchy of the body is not an abstract taxonomy — it is the propagation pathway of a disease. One amino acid does not stay at the molecular level. It climbs.
- Exclusions: Treatment options (hydroxyurea, gene therapy) — separate card.
- Score: 8/10

---

## Candidate 09 — "Research the Frank-Starling Relationship with Claude" (LLM Exercise)
- Source: anatomy-physiology-with-llms/chapters/23-the-cardiovascular-system-the-heart.md — stroke volume section
- Lane: RESEARCH (Claude assistant)
- Hook: The heart automatically matches its output to its input — without any neural signal — through the Frank-Starling relationship. Researching the three determinants of stroke volume with Claude (preload, afterload, contractility) and then asking what happens when each is chronically altered reveals the chain that connects hypertension to heart failure.
- The artifact: A sourced brief covering: (1) the Frank-Starling curve with normal, heart-failure, and sympathetic-activation versions compared, (2) preload (EDV → stretch → force) explained with a clinical example (exercise vs. dehydration), (3) afterload (aortic pressure) with the hypertension → LV hypertrophy → diastolic dysfunction cascade traced, (4) contractility (sympathetic activation via norepinephrine) with an athlete's trained-heart comparison.
- Prompt seed: `claude "Explain the three determinants of stroke volume: preload, afterload, and contractility. For each: define the term, explain the physiological mechanism, and give one clinical example of what happens when it increases chronically. Then explain the Frank-Starling relationship: why does increased preload cause increased stroke volume, and what does the Frank-Starling curve look like in a patient with systolic heart failure versus a highly trained athlete? What is the physiological reason a trained athlete can have a resting heart rate of 40 bpm and still maintain normal cardiac output?"`
- Read / check: Preload = EDV; Frank-Starling = stretch → longer sarcomere → greater cross-bridge overlap → more force. Afterload = aortic pressure; chronic elevation → LV hypertrophy → diastolic stiffness → diastolic failure. Contractility: sympathetic → norepinephrine → Ca²⁺ influx → stronger contraction. Athlete: larger ventricle → higher SV → lower HR needed for same CO.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (the Frank-Starling curve animates on a two-axis plot; a second curve labeled "heart failure" shifts down; a third labeled "athlete" shifts up; the athlete's resting point on the curve is marked — same cardiac output as untrained but at a different (HR, SV) combination)
- The change: Ask Claude what happens during hemorrhage: trace preload, afterload, contractility, heart rate, and cardiac output through the compensatory response, and identify at what blood loss percentage the compensation fails.
- Teardown angle: The Frank-Starling relationship is the heart's autonomous intelligence. It does not wait for the brain. That is why it works — and why it can overcompensate itself into failure.
- Exclusions: Specific drug mechanisms (digoxin, dobutamine) — separate card.
- Score: 8/10

---

## Candidate 10 — "Research Hypertension as a Systems Failure with Claude" (LLM Exercise)
- Source: anatomy-physiology-with-llms/chapters/24-the-cardiovascular-system-blood-vessels-and-circulation.md — LLM Exercise 5
- Lane: RESEARCH (Claude assistant)
- Hook: Hypertension is not just high blood pressure — it is a cascading systems failure that starts in arterioles, progresses to the heart wall, migrates to the coronary arteries, and ends in pulmonary edema. Researching the complete sequence with Claude, identifying which Poiseuille law or Starling force is operating at each step, makes the clinical picture coherent rather than memorized.
- The artifact: A sourced 7-step cascade brief (elevated SVR → LV works harder → LV hypertrophy → diastolic dysfunction → increased O₂ demand → coronary artery disease → pulmonary edema from left-heart failure) with: the specific physiological concept identified at each step (Poiseuille fourth power, Frank-Starling, wall compliance, Starling capillary forces), and an assessment of which step is most amenable to treatment and why.
- Prompt seed: `claude "Trace the complete sequence of physiological events that leads from chronic hypertension to left ventricular failure and pulmonary edema. Start with elevated systemic vascular resistance and end with fluid accumulation in the lungs. For each step in the sequence, identify which physiological concept is operating: Poiseuille's resistance law, the Frank-Starling relationship, vessel wall mechanics, or Starling capillary exchange forces. At which step in this sequence would treatment be most effective at preventing pulmonary edema, and what does that suggest about antihypertensive therapy?"`
- Read / check: Step 1: elevated SVR (Poiseuille — arteriolar constriction). Step 2: increased LV afterload → LV works harder. Step 3: LV hypertrophy (wall mechanics). Step 4: stiff wall → diastolic dysfunction → impaired filling. Step 5: higher O₂ demand → coronary supply insufficient. Step 6: LV systolic failure. Step 7: pulmonary venous hypertension → elevated pulmonary capillary CHP → pulmonary edema (Starling). Treatment intervention: antihypertensive therapy at Step 1 (before hypertrophy develops) is most preventive.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (a 7-node sequential diagram: each step appears and connects to the next; the specific physiological concept appears as a label above each arrow; a "treatment window" bracket highlights Steps 1–2 as the most effective intervention zone)
- The change: Ask Claude how the cascade differs if hypertension is treated at Step 3 (after hypertrophy has developed) vs. Step 5 (after coronary disease is established) — what can and cannot be reversed at each stage?
- Teardown angle: Hypertension kills through a cascade, not a single event. Treating the blood pressure number is intervention at Step 1. The clinical catastrophe happens at Step 7. The earlier the intervention, the more of the cascade is prevented — which is why blood pressure is screened, not waited for.
- Exclusions: Specific antihypertensive drug classes, renal mechanisms of BP regulation — separate cards.
- Score: 8/10
