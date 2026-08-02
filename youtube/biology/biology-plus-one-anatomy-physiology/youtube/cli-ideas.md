# Biology Plus One: Anatomy & Physiology — CLI Video Ideas ("X with Claude")

## Candidate 01 — Research the Cardiac Output Equation and Four Levers of the Heart with Claude
- Source: biology-plus-one-anatomy-physiology/chapters/09-the-cardiovascular-system.md
- Lane: RESEARCH (Claude assistant)
- Hook: A physician looks at an ECG for five seconds and says "Cath lab. Now." She is reading the whole cardiovascular system in one electrical trace — because cardiac output, heart rate, stroke volume, and vascular resistance are one coupled equation.
- The artifact: A sourced synthesis: the master equation CO = HR × SV explained with the four levers (preload, afterload, contractility, HR), a table of normal values and pathological deviations for each lever (heart failure, hypertension, septic shock, hemorrhage), and a step-by-step mechanistic explanation of how an anterior STEMI produces the clinical signs described in the chapter opener. Four citable sources.
- Prompt seed: `claude "Research the cardiovascular physiology of cardiac output and its clinical applications. (1) State and explain the cardiac output equation CO = HR × SV, define preload, afterload, contractility, and heart rate as the four independent levers. (2) Build a 4-row table: Lever, Normal value/range, What increases it, What decreases it, Clinical consequence of pathological change (e.g. high afterload → hypertension → left ventricular hypertrophy). (3) Trace mechanistically how an anterior STEMI (LAD occlusion) produces each of the following: ST elevation in V1-V4, drop in stroke volume, drop in CO, drop in blood pressure, baroreceptor-mediated sympathetic surge, diaphoresis. (4) Explain the difference between systolic and diastolic heart failure at the level of preload/afterload/contractility. Cite at least 4 sources."`
- Read / check: Verify CO = HR × SV is correctly stated; confirm that an LAD occlusion produces anterior wall ST elevation (V1-V4); check that baroreceptor reflex is correctly described as increasing HR and vasoconstriction in response to low CO.
- Human supplies: Nothing — fully synthetic. ECG traces from published figures are desirable slate images (human fills).
- Output medium: Slate (4-row table animated; STEMI mechanism as a cause-effect flow diagram animated text card).
- The change: Extend the query to compare heart failure treatment logic: why does a diuretic (reduces preload) help, while beta-blockers (reduce HR) paradoxically help in chronic heart failure but worsen acute decompensated failure — what does each intervention do to the CO equation?
- Teardown angle: The ECG is not a picture of the heart; it is 12 simultaneous views of the heart's electrical field. The physician's diagnosis in the chapter opener works because every ECG deviation maps to a physiology deviation that maps to an anatomical location. The system is readable because it is a coupled equation.
- Exclusions: Full ECG interpretation primer; detailed pharmacology of each cardiac drug class; detailed valvular disease mechanics; electrophysiology of specific arrhythmias.
- Score: 9/10

---

## Candidate 02 — Research the Endocrine Negative Feedback Architecture and Diabetes Pathophysiology with Claude
- Source: biology-plus-one-anatomy-physiology/chapters/08-the-endocrine-system.md
- Lane: RESEARCH (Claude assistant)
- Hook: Two patients in the same ER. One has too little insulin and is dying from it. The other had too much synthetic cortisol for 14 months and is dying from an adrenal crisis when the stress hits. The same feedback architecture — broken in opposite directions — almost kills both.
- The artifact: A sourced synthesis: the HPA axis feedback loop diagram (CRH → ACTH → cortisol → negative feedback on hypothalamus and pituitary) with the prednisone suppression mechanism explained; a 2-column table comparing Type 1 vs Type 2 diabetes (pathophysiology, insulin level, insulin resistance, treatment logic); the water-soluble vs lipid-soluble hormone comparison with receptor location, timescale, and duration for each class. Four citable sources.
- Prompt seed: `claude "Research the endocrine negative feedback architecture and diabetes pathophysiology. (1) Diagram the HPA (hypothalamic-pituitary-adrenal) axis as a feedback loop in prose: what does CRH do, what does ACTH do, what does cortisol do, and where/how does negative feedback close the loop? Explain mechanistically why 14 months of daily prednisone causes adrenal atrophy. (2) Build a 2-column comparison table: Type 1 vs Type 2 diabetes — mechanism of insulin deficiency, insulin level in blood, insulin receptor responsiveness, beta cell status, treatment strategy. (3) Compare water-soluble and lipid-soluble hormones: receptor location, signal cascade type (G-protein/cAMP vs nuclear receptor/gene transcription), speed (minutes vs hours), duration, one example for each. Cite at least 4 sources."`
- Read / check: Verify cortisol negative feedback acts on both hypothalamus (CRH) and anterior pituitary (ACTH); confirm Type 1 has autoimmune beta-cell destruction (low/absent insulin) vs Type 2 has insulin resistance (high insulin early, low later); check that lipid-soluble hormones bind nuclear receptors and activate gene transcription.
- Human supplies: Nothing — fully synthetic.
- Output medium: Slate (HPA loop as an animated circular diagram; 2-column table animated).
- The change: Extend the query to explain the Cushing syndrome phenotype (central obesity, moon face, buffalo hump, thin skin, striae) as the consequence of chronic cortisol excess acting on each tissue — connecting the feedback architecture to the clinical appearance.
- Teardown angle: The HPA axis is one of the most elegant negative feedback loops in physiology — it is the blueprint that nearly every endocrine axis follows. Both patients in the opener are failures of this feedback loop, one from below and one from the brake being held too long. The architecture is not the failure; the conditions that broke it are.
- Exclusions: Full steroidogenesis pathway from cholesterol; detailed insulin receptor signaling cascade; other endocrine axes (HPT, HPG) beyond what is needed to motivate the comparison.
- Score: 9/10

---

## Candidate 03 — Research the Nervous System: Resting Potential, Action Potential, and Myelin with Claude
- Source: biology-plus-one-anatomy-physiology/chapters/06-nervous-system-structure.md
- Lane: RESEARCH (Claude assistant)
- Hook: Multiple sclerosis doesn't destroy the camera or the screen — it destroys the cable. A fatty sheath wrapped around a wire determines whether an electrical signal arrives at all. The entire MS phenotype follows from one failure of insulation.
- The artifact: A sourced synthesis: the resting membrane potential explained mechanistically (Na+/K+ ATPase creating the gradient, K+ leak channels setting E_K, Nernst equation for K+ giving −89 mV, actual −70 mV as a weighted average), the action potential sequence (depolarization to threshold → Na+ channels open → peak → K+ channels open → repolarization → undershoot → refractory period), saltatory conduction vs continuous conduction, and the MS demyelination mechanism connecting to clinical phenotypes. Four citable sources.
- Prompt seed: `claude "Research the biophysics of the resting membrane potential and action potential, with clinical application to multiple sclerosis. (1) Explain the resting membrane potential mechanistically: what does the Na+/K+ ATPase create, what is the Nernst potential for K+ (formula and approximate value −89 mV), why is actual RMP −70 mV not −89 mV? (2) Describe the action potential sequence: threshold, Na+ channel opening, peak depolarization, K+ channel opening, repolarization, hyperpolarization undershoot, refractory period. What makes it all-or-none? (3) Compare continuous conduction (unmyelinated) vs saltatory conduction (myelinated): which is faster, why, what is the node of Ranvier? (4) Explain how demyelination in MS disrupts conduction and produces the clinical presentation of optic neuritis: signal slows or fails, vision becomes grainy or lost. Cite at least 4 sources."`
- Read / check: Verify Nernst equation for K+ gives approximately −89 mV (check the ratio [K+]out/[K+]in ≈ 5/140); confirm saltatory conduction is faster than continuous conduction for a given axon diameter; check that MS demyelination correctly targets oligodendrocytes in the CNS.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated action potential waveform drawing in over time; Na+/K+ channel state diagrams as animated icons below the waveform).
- The change: Add a comparison of demyelination (MS: slow onset, remitting) vs axon transection (acute injury: permanent immediate loss) — showing that myelin loss reduces conduction velocity but does not destroy the axon, which is why MS symptoms can partially recover with remyelination.
- Teardown angle: The resting potential is not a passive state. It is a stored tension paid for in 20% of the brain's energy budget. Every action potential is a brief, controlled release of that tension, paid for again immediately by the Na+/K+ ATPase. MS is the slow unraveling of the insulation that makes that release efficient.
- Exclusions: Detailed Na+ channel structure and gating; all ion channel pharmacology; spinal cord anatomy; complete MS immunopathology.
- Score: 8/10

---

## Candidate 04 — Research Respiratory Mechanics, Gas Exchange, and COPD with Claude
- Source: biology-plus-one-anatomy-physiology/chapters/11-the-respiratory-system.md
- Lane: RESEARCH (Claude assistant)
- Hook: A COPD patient's breathing works by a completely different mechanism than a healthy person's. The hypoxic drive that normally triggers breathing has been replaced by a hypercapnic failure — and giving too much oxygen to the wrong patient can make them stop breathing.
- The artifact: A sourced synthesis: the Fick diffusion law applied to alveolar gas exchange (why thin alveolar wall and large surface area maximize O2 flux), the oxygen-hemoglobin dissociation curve with the Bohr effect explained, the three pathological patterns (obstructive like COPD vs restrictive like fibrosis vs gas-exchange like pneumonia) in a 3-column table, and the O2-therapy paradox in CO2 retainers. Four citable sources.
- Prompt seed: `claude "Research respiratory physiology and its clinical pathologies. (1) Apply Fick's law of diffusion to explain why alveolar gas exchange works: what variables does the law include, and how does alveolar anatomy (surface area ~70 m2, wall ~0.5 μm thick) optimize each? (2) Explain the oxygen-hemoglobin dissociation curve: why is it sigmoidal, what is the Bohr effect, why does the sigmoidal shape help both loading in lungs and unloading in tissues? (3) Build a 3-column table: obstructive disease (COPD), restrictive disease (pulmonary fibrosis), gas-exchange disease (pneumonia) — mechanism, spirometry finding (FEV1/FVC), PO2 and PCO2 pattern. (4) Explain the COPD oxygen paradox: why does supplemental O2 sometimes cause CO2 retention and respiratory depression in certain patients? Cite at least 4 sources."`
- Read / check: Verify Fick's law includes surface area, diffusion coefficient, partial pressure gradient, membrane thickness; confirm the O2-Hb curve is sigmoidal due to cooperative binding; check that COPD spirometry shows reduced FEV1/FVC (<0.7) while restrictive shows reduced total lung capacity with preserved ratio.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated O2-Hb dissociation curve with Bohr shift arrows; animated point sweeping from lungs to tissue along the curve).
- The change: Extend the query to compare high-altitude adaptation — why do people living at altitude have higher hematocrit and right-shifted dissociation curves, and how does the 2,3-BPG mechanism explain this — connecting to the chapter's oxygen-hemoglobin physiology.
- Teardown angle: The O2-Hb dissociation curve's sigmoidal shape is not an accident; it is cooperative binding engineering. The Bohr effect makes the same molecule release O2 preferentially where CO2 is highest (active muscle). The COPD paradox follows logically from this — if CO2 retention has replaced hypoxia as the breathing trigger, supplemental O2 removes the remaining stimulus.
- Exclusions: Full ventilator settings and modes; ARDS pathophysiology in detail; pulmonary vascular disease; pleural effusion mechanics.
- Score: 8/10

---

## Candidate 05 — Research Tissue Types, Wound Healing, and the Extracellular Matrix with Claude
- Source: biology-plus-one-anatomy-physiology/chapters/03-tissues.md
- Lane: RESEARCH (Claude assistant)
- Hook: When you cut yourself, four tissue types respond in a choreographed sequence that takes weeks. If any step fails — epithelial, connective, muscle, or nervous — healing stops. Diabetic wounds fail this sequence at the vascular step. Understanding why requires understanding what collagen does and how fibroblasts build it.
- The artifact: A sourced synthesis: the four tissue types in a comparison table (type, key cells, extracellular matrix?, function), the three phases of wound healing (hemostasis, inflammation, proliferation/remodeling) with the key cell and molecule at each phase, and a mechanistic explanation of why diabetic wounds fail (impaired neutrophil function, reduced growth factor signaling, altered collagen deposition). Four citable sources.
- Prompt seed: `claude "Research the four tissue types and wound healing physiology. (1) Build a 4-row table: tissue type (epithelial, connective, muscle, nervous), key cell type(s), extracellular matrix present? (yes/no/type), primary function. (2) Describe the three phases of wound healing: hemostasis (what triggers platelet plug, what is the coagulation cascade role), inflammation (which cells arrive first and why, what do they do), proliferation/remodeling (fibroblasts make what, keratinocytes do what, angiogenesis contributes how). (3) Explain mechanistically why diabetic wounds heal poorly: which step fails, what is the role of hyperglycemia-induced neutrophil dysfunction, and how does reduced VEGF signaling impair angiogenesis? (4) What is the ECM and what does collagen provide structurally? Cite at least 4 sources."`
- Read / check: Verify neutrophils arrive first in inflammation (within hours); confirm fibroblasts deposit collagen (type I/III) in the proliferative phase; check that diabetic wound failure correctly includes neutrophil dysfunction and impaired angiogenesis (not just "poor circulation" alone).
- Human supplies: Nothing — fully synthetic.
- Output medium: Slate (4-row table animated; three-phase wound healing timeline as an animated horizontal bar with cellular players appearing at each phase).
- The change: Extend the query to compare wound healing in a keloid-prone individual (excessive collagen deposition, continued inflammation past the remodeling phase) vs normal healing — showing that the same mechanisms that repair tissue can also overshoot.
- Teardown angle: Wound healing is the body's construction project run by the same tissue types that make up the original structure. The ECM is the scaffolding; fibroblasts are the builders; the immune cells are the demolition and inspection crew. When diabetes impairs the crew's communication, the building stays unfinished.
- Exclusions: Full blood coagulation cascade proteins in detail; mast cell degranulation mechanisms; bone fracture healing specifics; scar maturation timescales.
- Score: 8/10

---

## Candidate 06 — Research Kidney Filtration, Osmolarity Gradients, and Renal Failure with Claude
- Source: biology-plus-one-anatomy-physiology/chapters/13-urinary-system-fluid-balance.md
- Lane: RESEARCH (Claude assistant)
- Hook: The kidney filters your entire blood volume 60 times a day — but urine is less than 1% of the filtrate. The other 99% is reclaimed by one of the most elegant concentration gradients in physiology. When it fails, everything in the blood accumulates.
- The artifact: A sourced synthesis: the three processes of urine formation (filtration, reabsorption, secretion) with quantitative examples (GFR 180 L/day → urine 1.8 L/day → 99% reabsorbed), the countercurrent multiplier mechanism in the loop of Henle explained mechanistically, the three categories of acute kidney injury (prerenal, intrinsic, postrenal) in a 3-row table with mechanism and BUN/creatinine ratio pattern, and the feedback loop for ADH/aldosterone regulation of fluid balance. Four citable sources.
- Prompt seed: `claude "Research kidney physiology: filtration, reabsorption, and acute kidney injury. (1) Quantitatively describe urine formation: GFR ~180 L/day filtered, ~1.8 L excreted — where does the 99% reabsorption happen (proximal tubule, loop of Henle, distal tubule, collecting duct), and what drives each? (2) Explain the countercurrent multiplier mechanism in the loop of Henle: how does the descending limb (permeable to water, impermeable to NaCl) and ascending limb (impermeable to water, actively transports NaCl) create the medullary osmolarity gradient needed for concentrated urine? (3) Build a 3-row table: prerenal, intrinsic, postrenal AKI — mechanism, BUN/creatinine ratio (>20:1 vs <20:1), example cause. (4) Explain ADH and aldosterone: what triggers each, what does each act on, how do they coordinately restore euvolemia? Cite at least 4 sources."`
- Read / check: Verify GFR ≈ 180 L/day and urine ≈ 1.5–2 L/day are correct; confirm ascending loop of Henle is impermeable to water; check that prerenal AKI gives BUN/Cr ratio >20:1 while intrinsic gives ~10:1.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated nephron diagram with water/solute arrows drawing in along the tubule segments; medullary gradient forming as a color gradient).
- The change: Extend the query to explain how loop diuretics (furosemide) work by blocking Na+/K+/2Cl- cotransport in the ascending limb — showing they directly disrupt the countercurrent multiplier and reduce the medullary gradient, leading to dilute urine and diuresis.
- Teardown angle: The countercurrent multiplier is thermodynamically clever — it creates a high-osmolarity gradient by recycling the work done by one segment to potentiate the work done by the adjacent segment. This is why mammals can produce concentrated urine while fish cannot; the loop of Henle is the mammalian innovation.
- Exclusions: Full glomerular filtration barrier structure; podocyte biology; detailed acid-base handling by the tubule; dialysis mechanics.
- Score: 8/10

---

## Candidate 07 — Research the Immune System: MHC Display, T Cell Activation, and Autoimmunity with Claude
- Source: biology-plus-one-anatomy-physiology/chapters/10-lymphatic-immune-system.md
- Lane: RESEARCH (Claude assistant)
- Hook: Every cell in your body constantly displays a sample of its own protein contents on its surface, like a shop window, for CD8 T cells to inspect. The moment a virus hijacks the protein factory, the window display changes — and the T cell kills the cell. Autoimmune disease is what happens when the T cell makes a mistake about what is foreign.
- The artifact: A sourced synthesis: MHC class I vs class II pathways in a 2-column comparison table (what they display, which cells express them, which T cells respond, outcome), the two-signal model of T cell activation (TCR + costimulation; why anergy without Signal 2 prevents autoimmunity), three examples of autoimmune disease and the tolerance-breakdown mechanism for each (Type 1 diabetes/beta cell destruction, MS/myelin, rheumatoid arthritis/synovium). Four citable sources.
- Prompt seed: `claude "Research MHC antigen presentation and T cell activation with clinical application to autoimmunity. (1) Build a 2-column table: MHC class I vs class II — what proteins are displayed (endogenous/cytosolic vs exogenous/phagocytosed), which cells express (all nucleated vs APCs only), which T cells recognize (CD8 vs CD4), what the response is (cytotoxic killing vs cytokine help). (2) Explain the two-signal model: Signal 1 is TCR-MHC/peptide; Signal 2 is CD28-CD80/86 costimulation. What happens without Signal 2 (T cell anergy) and why does this normally prevent autoimmunity? (3) Give three autoimmune diseases: for each, name the target tissue, the autoreactive immune cell type, and the proposed mechanism of tolerance breakdown. Include T1D, MS, rheumatoid arthritis. (4) Explain why immunosuppressants used for autoimmunity also increase infection risk. Cite at least 4 sources."`
- Read / check: Verify MHC class I displayed on all nucleated cells, class II on dendritic cells/macrophages/B cells; confirm CD8 recognizes class I and CD4 recognizes class II; check that anergy (not deletion) is the primary outcome of Signal 1 without Signal 2 in peripheral tolerance.
- Human supplies: Nothing — fully synthetic.
- Output medium: Slate (2-column table animated; two-signal diagram as an animated cause-effect card).
- The change: Extend the query to explain checkpoint inhibitor-induced autoimmunity (anti-PD-1 drugs release the brake on T cells, causing them to attack self-tissues) as a pharmacological demonstration of the same two-signal model — the drug disables the inhibitory signal that normally keeps autoreactive T cells in check.
- Teardown angle: The MHC display system solves the "how does a CD8 T cell know a cell is infected" problem by making every cell a reporter of its own biochemistry. The system works by the same logic as a drug-checking booth: if everything displayed is self-peptide, walk through; if anything foreign appears, destroy the cell. Autoimmunity is a false positive in that checkpoint.
- Exclusions: Full T cell development in the thymus; central vs peripheral tolerance in mechanistic detail; complete B cell maturation and antibody class switching; hypersensitivity types I–IV.
- Score: 7/10

---

## Candidate 08 — Research the Skeletal System: Bone Remodeling, Osteoporosis, and Fracture Healing with Claude
- Source: biology-plus-one-anatomy-physiology/chapters/04-the-skeletal-system.md
- Lane: RESEARCH (Claude assistant)
- Hook: Bone is not static. It is demolished and rebuilt constantly — 10% of the adult skeleton is replaced each year. Osteoporosis is what happens when demolition outpaces construction by just a few percent per year, silently, for decades.
- The artifact: A sourced synthesis: the osteoblast/osteoclast coupling mechanism (RANKL-RANK-OPG axis) explained step by step, the role of PTH, calcitonin, and vitamin D as the three hormonal regulators in a 3-row table, the trabecular vs cortical bone architecture difference and which fails first in osteoporosis, and bisphosphonate mechanism of action (why they inhibit osteoclasts). Four citable sources.
- Prompt seed: `claude "Research bone remodeling physiology and osteoporosis. (1) Explain the osteoblast-osteoclast coupling: what is RANKL, what does it bind on osteoclasts (RANK), what does OPG do as a decoy receptor, and how does PTH tip the balance toward resorption? (2) Build a 3-row table: PTH, calcitonin, vitamin D — trigger for release, target cells in bone, effect on serum calcium, net effect on bone. (3) Compare trabecular (spongy) vs cortical (compact) bone: structure, distribution in the body, which is metabolically more active, which fractures first in osteoporosis (e.g., vertebral compression fracture vs femoral neck)? (4) Explain bisphosphonate mechanism: how do they accumulate in bone, what enzyme do they inhibit in osteoclasts (farnesyl pyrophosphate synthase), and why does this reduce resorption? Cite at least 4 sources."`
- Read / check: Verify RANKL binds RANK on osteoclast precursors (not mature osteoclasts only); confirm OPG is a decoy receptor that binds RANKL and prevents osteoclast activation; check that trabecular bone is more metabolically active and fails first in osteoporosis.
- Human supplies: Nothing — fully synthetic.
- Output medium: Slate (RANKL-RANK-OPG diagram as an animated cause-effect card; 3-row hormone table animated).
- The change: Extend the query to explain why postmenopausal women lose bone faster — estrogen normally suppresses RANKL expression; loss of estrogen increases RANKL → more osteoclast activation → net resorption exceeds formation — and how hormone replacement therapy (HRT) works in this context.
- Teardown angle: Bone remodeling is a supply-demand system regulated by a molecular conversation between builders and demolishers. The conversation is mediated by RANKL-RANK-OPG, and estrogen is one of the master regulators of that conversation. Osteoporosis is the slow drift of the conversation toward demolition, one menstrual cycle at a time.
- Exclusions: Calcium absorption in the gut in detail; rickets vs osteomalacia distinction; complete fracture healing stages; bone cancer biology.
- Score: 7/10

---

## Candidate 09 — Research the Digestive System and Cholera Toxin's Abuse of CFTR with Claude
- Source: biology-plus-one-anatomy-physiology/chapters/12-digestive-system-metabolism.md
- Lane: RESEARCH (Claude assistant)
- Hook: Barry Marshall drank a Petri dish of H. pylori in 1984, gave himself gastritis in ten days, and cured himself with antibiotics. Twenty-one years later: the Nobel Prize. Every peptic ulcer is now a bacterial diagnosis, not a stress diagnosis.
- The artifact: A sourced synthesis: the five-segment tube description (mouth to colon) with the specific hydrolase, pH, and absorption process for each segment in a 5-row table, the H. pylori mechanism (urease-mediated pH neutralization, adhesin-mediated adherence, CagA virulence factor, prostaglandin-mediated mucus depletion), and the comparison between peptic ulcer from H. pylori vs from NSAIDs (two different mechanisms, same downstream pathology). Four citable sources.
- Prompt seed: `claude "Research digestive system physiology and H. pylori pathogenesis. (1) Build a 5-row table: digestive segment (mouth, stomach, small intestine, large intestine, colon), primary hydrolase(s), approximate pH, main nutrient absorbed. (2) Explain mechanistically how H. pylori survives the stomach's pH 1.5-3.5 environment: urease reaction, ammonia production, local pH buffering. (3) Describe H. pylori virulence: how does it adhere (BabA adhesin binds Lewis b antigen), what does the CagA protein do inside the epithelial cell, and how does it deplete the protective mucus layer? (4) Compare peptic ulcer from H. pylori vs from NSAIDs: same downstream pathology (mucus barrier breach, acid-on-tissue), different mechanism — H. pylori triggers inflammation, NSAIDs inhibit COX-1 prostaglandin synthesis. Cite at least 4 sources including the Warren-Marshall Nobel Prize paper."`
- Read / check: Verify urease converts urea to ammonia and CO2 (not bicarbonate directly); confirm CagA is injected into the host cell via a type IV secretion system; check that NSAIDs work by COX-1 inhibition (systemic), not direct local mucosal damage.
- Human supplies: Nothing — fully synthetic.
- Output medium: Slate (5-row table animated; H. pylori mechanism as an animated step-by-step text card).
- The change: Extend the query to explain why treating H. pylori with "triple therapy" (proton pump inhibitor + 2 antibiotics) cures ulcers in >80% of cases — and why the PPI is needed if the antibiotics are doing the killing (hint: antibiotics need acid suppression for efficacy in the gastric environment).
- Teardown angle: Marshall's self-experiment is a perfect illustration of the Koch's postulate logic applied to a disease the entire gastroenterology establishment believed was stress-caused. The experiment worked because the mechanism was bacterial all along. The "stress causes ulcers" model had no mechanism; the H. pylori model has a very specific one.
- Exclusions: Complete coagulation cascade for hemostasis; detailed pancreatic enzyme regulation; celiac disease immune mechanism; detailed gut microbiome in digestion.
- Score: 7/10

---

## Candidate 10 — Research Reproductive Endocrinology and the HPG Axis with Claude
- Source: biology-plus-one-anatomy-physiology/chapters/14-reproductive-system-development.md
- Lane: RESEARCH (Claude assistant)
- Hook: The same hormonal axis — GnRH → FSH/LH → sex steroids → negative feedback — runs every menstrual cycle, every spermatogenesis cycle, and puberty. Disrupting one node produces an entirely predictable cascade of failures downward.
- The artifact: A sourced synthesis: the HPG axis as a feedback loop (GnRH pulse from hypothalamus → FSH and LH from anterior pituitary → ovarian follicle development → estrogen → negative feedback on GnRH/LH until the LH surge → ovulation → positive feedback mechanism explained), a comparison of spermatogenesis vs oogenesis timelines (continuous vs batch), and a 3-row table of three HPG-disrupting conditions (hypothalamic amenorrhea, PCOS, primary ovarian insufficiency) with the level of axis disruption for each. Four citable sources.
- Prompt seed: `claude "Research the HPG axis and reproductive endocrinology. (1) Trace the HPG axis for the menstrual cycle as a feedback loop: GnRH pulse → FSH → follicular growth → estradiol → negative feedback on GnRH/LH in the follicular phase → estradiol surge → positive feedback switch → LH surge → ovulation → corpus luteum → progesterone → negative feedback → menstruation. Explain why estradiol causes negative feedback at low levels but positive at high levels. (2) Compare spermatogenesis vs oogenesis: is either continuous, what is the timeline for each, when does the female lose all oocytes? (3) Build a 3-row table: hypothalamic amenorrhea, PCOS, primary ovarian insufficiency — level of axis disrupted (hypothalamus/pituitary/ovary), FSH level (high/low/normal), LH level, treatment approach. (4) Cite at least 4 sources."`
- Read / check: Verify that the LH surge is caused by positive feedback from high estradiol (not the usual negative feedback); confirm FSH is high in primary ovarian insufficiency (ovary not responding, pituitary drives harder); check spermatogenesis is described as continuous in adult males.
- Human supplies: Nothing — fully synthetic.
- Output medium: Slate (HPG axis feedback loop as an animated circular diagram; 3-row table animated).
- The change: Extend the query to explain oral contraceptive mechanism — progestin + estrogen at continuous low levels prevent the mid-cycle LH surge by maintaining steady negative feedback, preventing the positive-feedback switch — showing the pill works by keeping the axis in permanent "follicular phase without the surge."
- Teardown angle: The HPG axis is a positive feedback trigger sitting on top of a negative feedback loop — a design that normally fires once per month and then resets. The LH surge's logic (estradiol stops being inhibitory and becomes stimulatory above a threshold) is one of the most elegant bistable switches in physiology.
- Exclusions: Detailed gametogenesis cell stages; placental hormone production in pregnancy; menopausal physiology beyond the POI case; male hypogonadism clinical management.
- Score: 7/10
