# Anatomy & Physiology — CLI Video Ideas ("X with Claude")

---

## Candidate 01 — "Research the Cardiovascular System's Four-Lever Master Equation with Claude"
- Source: biology-anatomy-physiology/chapters/09-the-cardiovascular-system.md
- Lane: RESEARCH (Claude assistant)
- Hook: Cardiac output = heart rate × stroke volume — and every clinical cardiovascular scenario is a story about which variable moved and why. Claude can build a sourced explainer of the Frank-Starling mechanism as the integrative core, with three worked clinical scenarios.
- The artifact: A sourced 4-section brief: (1) the master equation CO = HR × SV and its four adjustable levers (heart rate, preload, afterload, contractility), (2) the Frank-Starling mechanism — how EDV relates to SV and the molecular explanation (sarcomere length and cross-bridge formation), (3) three clinical scenarios traced through the equation (exercise: CO rises 4-fold; hemorrhage: Frank-Starling and compensation; heart failure: why diuretics help despite reducing preload), (4) the baroreflex — how the body detects and corrects blood pressure changes within seconds. Includes 5+ verifiable citations.
- Prompt seed: `claude "Research the Frank-Starling mechanism and cardiac output regulation. Include: (1) CO = HR × SV and the four levers that adjust SV (preload, afterload, contractility) and HR; (2) the Frank-Starling mechanism — molecular basis (sarcomere length, cross-bridge formation, calcium sensitivity), why resting sarcomeres sit below optimal length; (3) three scenarios: exercise (CO 5→20 L/min via all levers), hemorrhage (compensation fails if blood loss >30%), heart failure (diuretics reduce preload — explain the paradox); (4) the baroreflex circuit — sensing, center, effectors. Include at least 5 verifiable citations."`
- Read / check: Verify resting CO ≈ 5 L/min (HR 70 × SV 70 mL). Verify maximal exercise CO ~20-25 L/min in trained individuals. Verify hemorrhagic shock threshold (30% blood loss). Verify Frank-Starling molecular mechanism includes both sarcomere length and troponin-tropomyosin calcium sensitivity. Check baroreflex components (aortic arch + carotid sinus → medullary cardiovascular center → autonomic efferents).
- Human supplies: Nothing — fully researchable.
- Output medium: slate (4-section brief with equation framework, human fills with clinical Frank-Starling curve diagram)
- The change: Ask Claude to compare the Frank-Starling mechanism in a trained athlete vs. a heart failure patient — why does the athlete's curve sit higher, and why does the failure patient's curve shift right and down?
- Teardown angle: The heart is not a pump with a fixed output — it's a pressure-sensitive transducer that automatically matches output to input. Frank and Starling observed this in 1914; the molecular mechanism wasn't explained until the 1980s. The observation led the mechanism by 70 years.
- Exclusions: Cut full coagulation cascade; cut ECG interpretation in detail; cut RAAS pharmacology.
- Score: 9/10

---

## Candidate 02 — "Research the ECG as a Map of the Conduction System with Claude"
- Source: biology-anatomy-physiology/chapters/09-the-cardiovascular-system.md
- Lane: RESEARCH (Claude assistant)
- Hook: An ECG trace is not just voltage — it's a spatial map of where the conduction system is intact and where it isn't. The physician reading "anterior STEMI" in the chapter opener is reading anatomy from electrical squiggles. Claude can decode the map.
- The artifact: A sourced 3-section brief: (1) the three deflections and what anatomy they represent (P wave = atrial depolarization, QRS = ventricular depolarization, T wave = ventricular repolarization) and how the SA→AV node→bundle of His→Purkinje sequence creates this pattern, (2) four abnormal patterns and their anatomical diagnoses (prolonged PR = AV node delay; wide QRS = bundle branch block; absent P waves + irregular = atrial fibrillation; ST elevation = acute ischemia), (3) the opening physician's diagnosis — how lead placement localizes which coronary artery is blocked. Includes 4+ verifiable citations.
- Prompt seed: `claude "Research ECG interpretation as anatomical mapping of the cardiac conduction system. Include: (1) the three ECG deflections — P, QRS, T — and which anatomical events each represents, including the SA node→AV node→bundle of His→Purkinje fiber sequence; (2) four ECG abnormalities with anatomical interpretations: prolonged PR, wide QRS, absent P waves with irregular rhythm, ST-segment elevation; (3) how lead placement (12-lead ECG) localizes ST elevation to specific coronary artery territories — specifically, which leads show anterior STEMI and which artery is blocked. Include at least 4 verifiable citations."`
- Read / check: Verify PR interval normal range (120-200 ms). Verify prolonged PR = first-degree AV block = slow AV conduction. Verify anterior STEMI shows ST elevation in leads V1-V4 (left anterior descending artery territory). Verify wide QRS >120 ms = bundle branch block. Check atrial fibrillation characteristics (absent P waves, irregularly irregular QRS).
- Human supplies: Nothing — fully researchable.
- Output medium: slate (3-section brief, human fills with labeled normal ECG trace diagram — widely available in public medical education resources)
- The change: Ask Claude to trace what ECG changes would appear in a patient with progressive AV nodal disease — from first-degree block through Mobitz types to complete heart block, and what each means physiologically.
- Teardown angle: The ECG is a set of electrical measurements made from outside the body that reveal internal anatomy. It is a projection of 3D cardiac electrical activity onto 12 surface leads. The physician reading it is performing inverse problem solving — inferring the source from surface measurements.
- Exclusions: Cut full 12-lead ECG interpretation course; cut electrophysiology study procedures; cut implantable device therapy.
- Score: 9/10

---

## Candidate 03 — "Research Poiseuille's Fourth-Power Law and Why Arterioles Control Blood Pressure with Claude"
- Source: biology-anatomy-physiology/chapters/09-the-cardiovascular-system.md
- Lane: RESEARCH (Claude assistant)
- Hook: Resistance scales with the FOURTH power of radius. Cut a coronary artery's radius in half and resistance increases 16-fold. This is why a 50% stenosis that's silent at rest causes angina on exercise, and why a rupture causes infarction in minutes. Claude can trace the physics through to the clinical outcome.
- The artifact: A sourced 3-section brief: (1) Poiseuille's law derivation context (Jean-Louis Poiseuille, 1840s, blood flow in capillaries) and the fourth-power relationship: R = 8ηL/πr⁴, with two worked examples (50% radius reduction → 16× resistance; 20% reduction → 2.4×), (2) how this makes arterioles the primary pressure-control valves of the circulation (smooth muscle controlled, sympathetically innervated), (3) three clinical applications: hypertension (chronic arteriolar constriction), coronary artery disease (plaque reducing radius), and septic shock (vasodilation dropping TPR). Includes 4+ verifiable citations.
- Prompt seed: `claude "Research Poiseuille's law and its clinical application in cardiovascular medicine. Include: (1) the formula R = 8ηL/πr^4, two worked examples showing how a 50% and 20% radius reduction change resistance, and why the exponent is 4 (fluid dynamics derivation context); (2) how arterioles implement this law as pressure control valves — their smooth muscle content, sympathetic innervation, and ability to change lumen diameter by 50% or more; (3) three clinical applications: chronic hypertension (elevated TPR), coronary artery stenosis (angina on exertion, rupture → MI), and septic shock (vasodilation despite high CO). Include at least 4 verifiable citations."`
- Read / check: Verify Poiseuille's work was on capillaries in the 1840s. Verify that 50% radius reduction → 2⁴ = 16× resistance increase. Verify that septic shock is characterized by low TPR and HIGH CO (opposite of cardiogenic shock). Check that MAP = CO × TPR identity is correctly stated.
- Human supplies: Nothing — fully researchable.
- Output medium: slate (3-section brief with fourth-power examples, human fills with arteriole cross-section diagram)
- The change: Ask Claude to compute what viscosity change would be required to maintain the same flow rate if radius were reduced by 20% — connect this to why dehydration (increased viscosity) worsens hypertension.
- Teardown angle: A 20% change in radius produces a 2.4-fold change in resistance. This is the design principle of arteriolar tone — small adjustments produce large effects. The cardiovascular system uses the fourth-power relationship as a control lever.
- Exclusions: Cut elastic artery compliance; cut venous capacitance; cut lymphatic return system.
- Score: 8/10

---

## Candidate 04 — "Research the Muscle Twitch: From Action Potential to Calcium to Contraction with Claude"
- Source: biology-anatomy-physiology/chapters/05-muscle-tissue-muscular-system.md
- Lane: RESEARCH (Claude assistant)
- Hook: A skeletal muscle fiber goes from rest to full contraction in ~10 milliseconds — triggered by a single action potential. The calcium release mechanism that makes this happen is one of the fastest signal transduction events in biology. Claude can trace the complete pathway.
- The artifact: A sourced 3-section brief: (1) the complete excitation-contraction coupling sequence: motor neuron AP → NMJ → muscle AP → T-tubules → SR calcium release → troponin → cross-bridge cycling; (2) the sliding filament model — what actin, myosin, troponin, and tropomyosin do at each step of the cross-bridge cycle; (3) motor unit recruitment — why the nervous system uses multiple motor units rather than just turning one large motor unit up to full strength. Includes 4+ verifiable citations.
- Prompt seed: `claude "Research skeletal muscle excitation-contraction coupling. Include: (1) the complete sequence from motor neuron action potential through NMJ (ACh release, end-plate potential) through muscle action potential, T-tubule transmission, SR calcium release, and cross-bridge activation; (2) the sliding filament model — roles of actin, myosin heads (power stroke), troponin C (calcium binding), tropomyosin (block/unblock active sites); (3) motor unit recruitment — why smaller units are recruited first (Henneman size principle), and how recruitment vs. frequency coding together produce graded force. Include at least 4 verifiable citations."`
- Read / check: Verify the NMJ uses acetylcholine (not glutamate). Verify troponin C binds calcium specifically. Verify the power stroke involves myosin head flexing (not just pulling). Verify Henneman's size principle (1965) — small motor units recruited first. Check that the SR is the sarcoplasmic reticulum (not endoplasmic reticulum).
- Human supplies: Nothing — fully researchable.
- Output medium: slate (3-section brief, human fills with sliding filament model diagram from public medical education sources)
- The change: Ask Claude to explain rigor mortis using this mechanism — what happens when ATP is depleted (myosin stays bound to actin), and when and why rigor resolves (proteolytic enzyme activity days later).
- Teardown angle: Muscle contraction is a molecular motor converting chemical energy to mechanical work. The calcium switch is the on/off signal. The sarcomere is the force generator. The motor unit is the neural control unit. Three different levels of organization, each essential.
- Exclusions: Cut cardiac muscle differences (calcium-induced calcium release); cut smooth muscle mechanism; cut exercise-induced hypertrophy signaling.
- Score: 8/10

---

## Candidate 05 — "Research the Pacemaker Cell and Why the Heart Doesn't Need a Brain to Beat with Claude"
- Source: biology-anatomy-physiology/chapters/09-the-cardiovascular-system.md
- Lane: RESEARCH (Claude assistant)
- Hook: A single cardiac pacemaker cell isolated in a dish beats at 60-80 times per minute with no nerves and no neighbors. The mechanism is a membrane channel that never fully closes — sodium leaks in and slowly builds the next beat. Claude can document the autorhythmicity mechanism and its clinical failure modes.
- The artifact: A sourced 4-section brief: (1) autorhythmicity mechanism — the funny current (If, HCN channels), prepotential, and why SA node cells fire at 100 bpm vs AV node at 40-60 bpm; (2) overdrive suppression — how the SA node preempts slower pacemakers, what happens when it fails (AV nodal escape, Purkinje escape); (3) autonomic modulation — how vagus (ACh, M2 receptors) slows the prepotential and sympathetic input (NE, β1 receptors) steepens it; (4) clinical conditions — sick sinus syndrome, heart block, and pacemaker therapy. Includes 4+ verifiable citations.
- Prompt seed: `claude "Research cardiac pacemaker cell autorhythmicity. Include: (1) the mechanism — the HCN ('funny') channels responsible for the pacemaker potential, why Ca2+ channels (not Na+ as in neurons) produce the upstroke in pacemaker cells, the prepotential slope determines intrinsic rate; (2) overdrive suppression — why faster cells preempt slower ones, what happens when SA node fails (hierarchy of escape pacemakers); (3) autonomic modulation — vagal ACh slows rate (M2/GIRK channels → K+ leak → slower prepotential), sympathetic NE speeds rate (β1/cAMP → steeper prepotential); (4) clinical implications — sick sinus syndrome, AV block grades, artificial pacemaker indications. Include at least 4 verifiable citations."`
- Read / check: Verify pacemaker cell upstroke uses L-type Ca2+ channels (not fast Na+ channels). Verify HCN (hyperpolarization-activated cyclic nucleotide-gated) channels carry the If current. Verify intrinsic SA node rate is 60-100 bpm. Verify vagal M2 receptor activation opens GIRK channels (not closes them). Check AV nodal escape rate (40-60 bpm) and Purkinje escape rate (20-40 bpm).
- Human supplies: Nothing — fully researchable.
- Output medium: slate (4-section brief, human fills with SA node action potential trace diagram — widely available in physiology textbooks)
- The change: Ask Claude to trace what happens in complete heart block (no signal crosses the AV node) — which pacemaker takes over, at what rate, and why the patient needs an artificial pacemaker for anything above bed rest.
- Teardown angle: The heart beats because of ion channel physics, not neural commands. The brain modulates rate; it doesn't initiate beats. This distinction matters clinically — heart transplants work despite severed vagal nerves, because the SA node fires without them.
- Exclusions: Cut calcium cycling in cardiomyocytes; cut arrhythmia mechanisms in detail; cut pharmacology of antiarrhythmics.
- Score: 8/10

---

## Candidate 06 — "Research Respiratory Gas Exchange and the Oxygen-Hemoglobin Dissociation Curve with Claude"
- Source: biology-anatomy-physiology/chapters/11-the-respiratory-system.md
- Lane: RESEARCH (Claude assistant)
- Hook: The oxygen-hemoglobin dissociation curve is S-shaped — and the S-shape is not an accident. It means hemoglobin loads efficiently in the lungs and unloads efficiently in tissues, at exactly the oxygen tensions where each needs to happen. Claude can document the curve, the Bohr effect, and the clinical implications.
- The artifact: A sourced 3-section brief: (1) the S-shaped dissociation curve — why it's S-shaped (cooperative binding, 4 subunits), what P50 means (27 mmHg for normal hemoglobin), what the curve predicts at alveolar PO2 (~100 mmHg) vs. tissue PO2 (~40 mmHg); (2) the Bohr effect — how CO2, H+, temperature, and 2,3-BPG shift the curve right (lower affinity, more O2 delivery to active tissues); (3) three clinical applications: carbon monoxide poisoning (COHb shifts curve left and occupies binding sites), high-altitude adaptation (hyperventilation, increased 2,3-BPG, erythropoietin response), and fetal hemoglobin (HbF has higher O2 affinity — why). Includes 4+ verifiable citations.
- Prompt seed: `claude "Research the oxygen-hemoglobin dissociation curve and gas exchange. Include: (1) the S-shape — why hemoglobin shows cooperative binding (Hill coefficient ~2.7), what the flat upper portion and steep middle portion accomplish physiologically, P50 definition; (2) the Bohr effect — how CO2 (as H2CO3), H+, 2,3-BPG, and temperature shift the curve right, and why this is adaptive during exercise; (3) three clinical scenarios: CO poisoning (mechanism, why the curve shifts left AND sites are blocked), high altitude adaptation timeline, and fetal hemoglobin (HbF — why it must have higher O2 affinity than adult Hb for placental gas transfer). Include at least 4 verifiable citations."`
- Read / check: Verify P50 of adult hemoglobin (~27 mmHg). Verify alveolar PO2 ~100 mmHg and tissue PO2 ~40 mmHg. Verify Bohr effect: CO2 → H2CO3 → H+ → allosteric shift right. Verify fetal HbF has gamma chains (not beta) and lacks 2,3-BPG binding. Verify CO poisoning shifts curve left AND reduces total O2-carrying capacity.
- Human supplies: Nothing — fully researchable.
- Output medium: slate (3-section brief, human fills with O2-Hb dissociation curve diagram showing normal and shifted curves)
- The change: Ask Claude to predict what happens to the dissociation curve in a patient with iron-deficiency anemia — and whether the Bohr effect compensates or fails to compensate for reduced hemoglobin concentration.
- Teardown angle: The S-shape is not a compromise — it's a solution. Hemoglobin loads near-completely at 100 mmHg and delivers near-completely by 40 mmHg. The sigmoid curve is the key to efficient O2 delivery without requiring a perfect linear relationship across all tissues.
- Exclusions: Cut pulmonary mechanics (compliance, surfactant); cut CO2 transport as bicarbonate; cut ventilation-perfusion mismatch in detail.
- Score: 8/10

---

## Candidate 07 — "Research the Renal Countercurrent Multiplier and How the Kidney Concentrates Urine with Claude"
- Source: biology-anatomy-physiology/chapters/13-urinary-system-fluid-balance.md
- Lane: RESEARCH (Claude assistant)
- Hook: The kidney concentrates urine to 1200 mOsm/kg — four times plasma concentration — using a passive osmotic gradient built by a countercurrent multiplier in the loop of Henle. This is one of the most elegant engineering solutions in biology. Claude can reconstruct the mechanism.
- The artifact: A sourced 3-section brief: (1) the countercurrent multiplier — how the descending limb (permeable to water, impermeable to NaCl) and ascending limb (impermeable to water, active NaCl transport) create a medullary osmotic gradient of 300 → 1200 mOsm/kg, (2) the countercurrent exchanger (vasa recta) — how the capillary loops preserve the gradient rather than washing it away, (3) ADH's role — aquaporin insertion in the collecting duct, how ADH levels determine final urine concentration, and the three causes of diabetes insipidus. Includes 4+ verifiable citations.
- Prompt seed: `claude "Research the renal countercurrent multiplier and urine concentration mechanism. Include: (1) the loop of Henle countercurrent multiplier — how the descending limb (water permeable, NaCl impermeable) and ascending limb (water impermeable, NaCl actively transported) create a medullary osmotic gradient from 300 to 1200 mOsm/kg; (2) the vasa recta countercurrent exchanger — why the capillary loops preserve the gradient; (3) ADH and aquaporin-2 insertion into collecting duct principal cells, what determines final urine osmolality, and the three causes of diabetes insipidus (central, nephrogenic, dipsogenic). Include at least 4 verifiable citations."`
- Read / check: Verify the medullary gradient range (300 mOsm/kg at cortex, up to 1200 at papilla). Verify ascending limb is NaCl-impermeable (water stays) while it pumps NaCl out. Verify vasa recta descend parallel to loop of Henle (countercurrent flow). Verify ADH acts via V2 receptor → cAMP → aquaporin-2 insertion. Check diabetes insipidus types: central (no ADH), nephrogenic (no ADH receptor response), primary polydipsia.
- Human supplies: Nothing — fully researchable.
- Output medium: slate (3-section brief, human fills with loop of Henle diagram with osmolality gradient shown — widely available in physiology textbooks)
- The change: Ask Claude to trace what happens to urine concentration in a patient with heart failure who is on a loop diuretic (furosemide) — the diuretic blocks the NKCC2 transporter in the ascending limb, abolishing the gradient, producing dilute urine even if ADH is high.
- Teardown angle: The countercurrent multiplier is an engineering solution to concentrate solutes using only osmotic gradients and selective membrane permeability — no energy-intensive direct concentration step. The urine concentration is set not by how much you pump but by how well you maintain the gradient.
- Exclusions: Cut full nephron filtration and reabsorption details; cut acid-base balance; cut aldosterone mechanism.
- Score: 8/10

---

## Candidate 08 — "Research the Nervous System's Hierarchical Organization from Reflex to Consciousness with Claude"
- Source: biology-anatomy-physiology/chapters/06-nervous-system-structure.md + biology-anatomy-physiology/chapters/07-nervous-system-function-control.md
- Lane: RESEARCH (Claude assistant)
- Hook: A reflex happens before you're conscious of it. The spinal cord handles the fastest responses; the cortex handles the slowest and most abstract. Claude can document the hierarchy and show what happens at each level when it fails.
- The artifact: A sourced 4-section brief: (1) the reflex arc — sensory neuron → spinal interneuron → motor neuron, with the hot stove example (50ms response vs. 200ms conscious perception), (2) the brainstem hierarchy — what each structure controls (medullary reflex centers: cardiovascular, respiratory, swallowing; midbrain: eye movement, consciousness), (3) cerebellar function — what it controls and what cerebellar damage looks like (ataxia, past-pointing, intention tremor), (4) cortical organization — motor homunculus, somatosensory homunculus, and the principle that the amount of cortex reflects the precision requirement, not the body part size. Includes 4+ verifiable citations.
- Prompt seed: `claude "Research the hierarchical organization of the nervous system. Include: (1) the spinal reflex arc — anatomy of the monosynaptic stretch reflex and polysynaptic withdrawal reflex, with the 50ms vs 200ms timeline for reflex vs. conscious perception of a painful stimulus; (2) brainstem hierarchy — what each level controls (medullary: cardiovascular/respiratory centers; pontine: respiration rhythm; midbrain: consciousness, pupillary reflex); (3) cerebellum — function in motor coordination, three clinical signs of cerebellar damage (ataxia, dysmetria, intention tremor); (4) motor and somatosensory cortex organization — homunculus principle, why hands and lips have more cortex than the back. Include at least 4 verifiable citations."`
- Read / check: Verify monosynaptic stretch reflex (knee-jerk, Ia afferents → alpha motor neurons). Verify the ~50ms spinal withdrawal reflex timing. Verify that the brainstem controls consciousness (reticular activating system) and that midbrain lesions can cause coma. Verify cerebellar ataxia involves uncoordinated movement not weakness. Verify homunculus disproportionality reflects receptor density and precision, not body size.
- Human supplies: Nothing — fully researchable.
- Output medium: slate (4-section brief, human fills with brain cross-section diagram and motor homunculus — both widely available as public domain medical illustrations)
- The change: Ask Claude to compare what happens when each level of the hierarchy is damaged — spinal cord injury vs. brainstem stroke vs. cerebellar lesion vs. cortical stroke — and what functions are lost vs. preserved in each case.
- Teardown angle: The nervous system is built as a hierarchy where each higher level can override the lower — but the lower levels can still function after the upper levels are damaged. This explains why paraplegics have spinal reflexes but no voluntary movement, why brainstem-dead patients have no consciousness but may have some brainstem reflexes.
- Exclusions: Cut synaptic transmission mechanism; cut limbic system emotion processing; cut sleep physiology.
- Score: 8/10

---

## Candidate 09 — "Research the Immune System's Two-Strike Rule: Innate Then Adaptive with Claude"
- Source: biology-anatomy-physiology/chapters/10-lymphatic-immune-system.md
- Lane: RESEARCH (Claude assistant)
- Hook: The innate immune system buys 4-7 days while the adaptive immune system ramps up. Without innate immunity, bacteria could kill before the body learns to fight them. Claude can document the two-system logic and the interface where danger signals hand off to lymphocytes.
- The artifact: A sourced 3-section brief: (1) innate immunity — pattern recognition receptors (Toll-like receptors, NOD receptors), the response timeline (minutes to days), the five cardinal signs of inflammation and their cellular basis, (2) the adaptive handoff — how antigen-presenting cells (dendritic cells) transport processed antigen to lymph nodes, the MHC I/II distinction (MHC I presents to cytotoxic T cells, MHC II to helper T cells), (3) two clinical examples: septic shock as innate immunity gone systemic, and HIV as an adaptive immunity failure — what specifically is lost when CD4+ T helper cells drop below 200/μL. Includes 4+ verifiable citations.
- Prompt seed: `claude "Research innate and adaptive immunity as a two-phase system. Include: (1) innate immunity — Toll-like receptors (TLRs), PAMPs vs. DAMPs, the 4-7 day timeline before adaptive ramps up, and the five cardinal signs of inflammation (rubor, calor, tumor, dolor, functio laesa) with cellular basis; (2) the adaptive immune handoff — how dendritic cells capture antigen, process it, migrate to lymph nodes, and present on MHC I (to cytotoxic CD8+ T cells) vs. MHC II (to helper CD4+ T cells); (3) two clinical failures: septic shock (innate over-activation, cytokine storm) and AIDS (CD4+ T cell loss, why <200 CD4+ cells/μL defines AIDS and leads to opportunistic infections). Include at least 4 verifiable citations."`
- Read / check: Verify TLRs recognize PAMPs (pathogen-associated molecular patterns). Verify dendritic cells are the principal antigen-presenting cells for adaptive activation. Verify MHC I presents endogenous peptides to CD8+ cells, MHC II presents exogenous to CD4+. Verify AIDS definition: CD4+ <200/μL. Check five cardinal signs and their Latin roots.
- Human supplies: Nothing — fully researchable.
- Output medium: slate (3-section brief, human fills with innate-to-adaptive timeline diagram)
- The change: Ask Claude to explain why HIV specifically depletes CD4+ helper T cells rather than other lymphocytes, and trace the cascade from CD4+ loss to failure of both antibody and cytotoxic responses.
- Teardown angle: The immune system is a two-stage system because pattern recognition is fast but specific recognition takes time. The innate system buys time; the adaptive system delivers precision. Both are necessary; neither is sufficient.
- Exclusions: Cut complement system in detail; cut B cell activation and antibody isotypes; cut vaccine mechanism.
- Score: 7/10

---

## Candidate 10 — "Research the Endocrine System's Hierarchical Control: Hypothalamus-Pituitary-Target with Claude"
- Source: biology-anatomy-physiology/chapters/08-the-endocrine-system.md
- Lane: RESEARCH (Claude assistant)
- Hook: The hypothalamus controls the pituitary with releasing hormones, the pituitary controls target glands with tropic hormones, and the target glands feed back to suppress both. This three-tier axis is how the body controls thyroid, adrenal, gonadal, and growth functions through negative feedback loops.
- The artifact: A sourced 3-section brief: (1) the three-tier HPT (hypothalamic-pituitary-target) axis — releasing hormone → tropic hormone → target hormone → negative feedback to hypothalamus and pituitary, using the HPA (stress) axis as the worked example, (2) two clinical failure modes: primary hypothyroidism (high TSH because low T4 removes feedback) vs. secondary hypothyroidism (low TSH because pituitary is damaged), (3) the direct measurement principle — why laboratory tests measure different hormones depending on which level is suspected to be failing. Includes 4+ verifiable citations.
- Prompt seed: `claude "Research the hypothalamic-pituitary-target axis as a control system. Include: (1) the three-tier architecture — using the HPA (stress) axis as the worked example (CRH → ACTH → cortisol → negative feedback); (2) two clinical failure modes illustrating the diagnostic power of the axis: primary hypothyroidism (elevated TSH, low T4 — where is the lesion?) vs. secondary hypothyroidism (low TSH AND low T4 — where is the lesion?), and the clinical test for each; (3) how the direct measurement principle guides lab testing — what TSH alone tells you about thyroid function without measuring T4. Include at least 4 verifiable citations."`
- Read / check: Verify CRH → ACTH → cortisol axis (CRH from hypothalamus, ACTH from anterior pituitary, cortisol from adrenal cortex). Verify primary hypothyroidism has high TSH (no feedback from T4 → pituitary keeps releasing TSH). Verify secondary hypothyroidism has low TSH and low T4 (pituitary lesion removes the driver). Verify that TSH is the most sensitive test for thyroid function in primary disease.
- Human supplies: Nothing — fully researchable.
- Output medium: slate (3-section brief, human fills with HPT axis feedback diagram — widely available in endocrinology educational resources)
- The change: Ask Claude to apply the same logic to the HPA axis in Cushing's syndrome — where can the lesion be (adrenal cortex tumor, pituitary ACTH-secreting tumor, ectopic ACTH), and how does ACTH level distinguish them?
- Teardown angle: The three-tier axis is a feedback control system. The diagnostic power comes from measuring at multiple levels — TSH tells you where the axis is intact and where it's failing. This is the endocrinologist's version of electrical circuit diagnostics.
- Exclusions: Cut full thyroid hormone synthesis; cut insulin/glucagon regulation; cut growth hormone IGF-1 axis.
- Score: 8/10

---

## Candidate 11 — "Research Osmotic Regulation and Why the Kidney Is Also a Control System with Claude"
- Source: biology-anatomy-physiology/chapters/13-urinary-system-fluid-balance.md
- Lane: RESEARCH (Claude assistant)
- Hook: The kidney isn't just a filter — it's a feedback control system for plasma osmolality, blood volume, and acid-base balance simultaneously. Claude can document the three sensors (osmoreceptors, baroreceptors, chemoreceptors) and trace their effectors through to the clinical presentation of dehydration, hyponatremia, and acidosis.
- The artifact: A sourced 3-section brief: (1) the osmolality control loop — hypothalamic osmoreceptors detect 1-2% increase in plasma osmolality → ADH release → aquaporin insertion → water reabsorption → normalized osmolality; the thirst mechanism running in parallel, (2) the volume control loop — atrial stretch receptors → ANP (dilates, reduces reabsorption) vs. RAAS → aldosterone (retains sodium) — why these run in opposite directions, (3) clinical application: hyponatremia (sodium <135 mEq/L) — three different causes (SIADH, heart failure, vomiting) each with different volume status and treatment. Includes 4+ verifiable citations.
- Prompt seed: `claude "Research renal osmotic and volume regulation as control systems. Include: (1) the ADH control loop — hypothalamic osmoreceptors, 1-2% threshold for ADH release, aquaporin-2 insertion mechanism, and the parallel thirst mechanism; (2) the volume control systems in opposition — ANP (atrial stretch → natriuresis) vs. RAAS (low perfusion → aldosterone → sodium retention), and how the two systems are triggered differently; (3) hyponatremia as a diagnostic challenge — compare SIADH (euvolemic, concentrated urine), heart failure (hypervolemic, dilute urine due to baroreceptor paradox), and vomiting (hypovolemic, alkalotic). Include at least 4 verifiable citations."`
- Read / check: Verify ADH threshold is ~285-295 mOsm/kg plasma (any increase → ADH release). Verify aquaporin-2 is in the collecting duct (not proximal tubule). Verify ANP is released from atrial myocytes in response to stretch. Verify SIADH produces euvolemic hyponatremia with inappropriately concentrated urine (high urine osmolality despite low plasma osmolality).
- Human supplies: Nothing — fully researchable.
- Output medium: slate (3-section brief, human fills with osmolality control loop diagram)
- The change: Ask Claude to trace what happens to a marathon runner's electrolytes — why does overdrinking pure water without electrolytes cause hyponatremia (exercise-associated hyponatremia), and why is this more dangerous than dehydration?
- Teardown angle: The kidney simultaneously manages osmolality and volume, and the two systems can conflict — heart failure forces the kidney to retain sodium (volume depleted from the baroreceptors' perspective) even though the patient is already hypervolemic. The control system is defeating itself.
- Exclusions: Cut acid-base regulation in full; cut potassium regulation; cut renal handling of drugs.
- Score: 7/10

---

## Candidate 12 — "Research the Digestive System as a Factory with Autonomous Control with Claude"
- Source: biology-anatomy-physiology/chapters/12-digestive-system-metabolism.md
- Lane: RESEARCH (Claude assistant)
- Hook: The gut has its own nervous system (enteric nervous system, 100-500 million neurons) that coordinates digestion without consulting the brain. It's sometimes called "the second brain." Claude can document what the ENS actually controls and what happens when it fails.
- The artifact: A sourced 3-section brief: (1) the enteric nervous system — neuron count, location (myenteric plexus for motility, submucosal plexus for secretion), how it coordinates peristalsis without CNS input (Bayliss-Starling law of the intestine), (2) the gut-brain axis — vagal afferent fibers carry ~80% of signals from gut to brain (not brain to gut), and what those signals regulate (satiety, nausea, mood), (3) clinical failure modes: Hirschsprung's disease (absent enteric ganglia → no peristalsis → toxic megacolon), gastroparesis (failed gastric emptying, often from vagal neuropathy in diabetes), and the microbiome-ENS connection. Includes 4+ verifiable citations.
- Prompt seed: `claude "Research the enteric nervous system as an autonomous gut control system. Include: (1) ENS structure — 100-500 million neurons, myenteric plexus (motility) vs. submucosal plexus (secretion), how the Bayliss-Starling law of the intestine operates without CNS input; (2) the gut-brain axis — vagal afferents carry ~80% of gut-brain signals (not efferents), what the brain receives (satiety, nausea, mood-relevant signals), and the serotonin role (95% of body's serotonin is in the gut); (3) clinical failures — Hirschsprung's disease (absent ganglia → megacolon), diabetic gastroparesis (vagal neuropathy → failed gastric emptying), microbiome influence on ENS tone. Include at least 4 verifiable citations."`
- Read / check: Verify ENS neuron count range (100 million is the common estimate, up to 500 million in some sources — note the range). Verify Bayliss and Starling described the intestinal law of peristalsis in 1899. Verify ~80% of vagal fibers are afferent (gut to brain). Verify 95% of serotonin is in the gut (actually enterochromaffin cells). Verify Hirschsprung's is characterized by absent ganglia in the distal bowel.
- Human supplies: Nothing — fully researchable.
- Output medium: slate (3-section brief, human fills with ENS/enteric plexus diagram)
- The change: Ask Claude to explain the gut-brain axis in terms of specific diseases: why do IBS patients have altered pain sensitivity in the gut (visceral hypersensitivity), and what does this tell us about the ENS-CNS bidirectional connection?
- Teardown angle: The gut can digest food, coordinate peristalsis, and respond to nutrients without any brain input. The brain evolved to receive information from the gut, not just to send commands. The gut-brain axis is mostly gut-to-brain, not brain-to-gut.
- Exclusions: Cut pancreatic enzyme secretion; cut liver metabolism; cut colonoscopy and cancer screening.
- Score: 7/10
