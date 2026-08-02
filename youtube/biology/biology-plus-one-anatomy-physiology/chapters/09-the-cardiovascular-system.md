# Chapter 9 — The Cardiovascular System
*One loop, four levers, and the equation that ties them together.*

---

A physician looks at an ECG printout for five seconds and says: "Cath lab. Now. Anterior STEMI." She has not examined the patient, not felt his pulse, not ordered a blood test. She has read twelve electrical perspectives on one heart, and from the pattern of ST elevation in leads V1 through V4 she has concluded that a specific artery is blocked, that a specific region of muscle is dying, and that an interventional cardiologist needs to be called immediately.

How does she get from squiggles to coronary anatomy?

She gets there because the electrical activity of the heart, the mechanical contraction of the heart, the blood the heart is pumping, and the vessels it pumps through are all parts of one system. A blocked coronary artery starves a region of myocardium of oxygen. The oxygen-starved cells lose their ion gradients. The ECG records that loss as a specific pattern at specific electrode positions. The mechanical consequence — that region cannot contract — drops stroke volume. The dropped stroke volume drops cardiac output. The dropped cardiac output drops blood pressure. The baroreceptors fire the sympathetic system. The sympathetic system raises heart rate and constricts vessels. The patient in the opening case is sweating and looks gray because all of this is happening simultaneously.

To read the ECG is to read the whole system. This chapter builds the whole system.

Four moves. What is being pumped — blood. What does the pumping — the heart as two pumps sharing one electrical signal. The master equation — cardiac output equals heart rate times stroke volume — and the four levers that move it. Where the blood goes — vessels graded from elastic pressure reservoirs to single-cell-thick exchange surfaces, with Poiseuille's law governing how a small change in radius produces an enormous change in flow.

---

## What is being pumped

Spin a tube of blood in a centrifuge. Two layers separate cleanly. The bottom, deep red, fills about 45 percent of the tube: **erythrocytes** — red cells. The top, straw-colored, fills the other 55 percent: **plasma**. Between them, barely a millimeter of pale material — white cells and platelets, less than one percent of the volume.

That proportion — 45 percent cells — is the **hematocrit**, and it is the first number on any blood panel for a reason. Too low, and oxygen-carrying capacity drops. Too high, and blood becomes viscous, and viscosity raises the heart's workload by Poiseuille's law (we will get there). The healthy range negotiates between these two failure modes.

**Plasma** is 92 percent water, but the 8 percent that is not water is doing structural work. **Albumin**, made by the liver, creates most of the osmotic pull that keeps fluid inside blood vessels. Without albumin, water leaks into tissues — one mechanism of edema. **Fibrinogen** is the soluble precursor to fibrin, the mesh of a blood clot. Globulins carry the antibodies of the immune system. The rest of plasma carries dissolved electrolytes, nutrients, and metabolic wastes on their way to the kidney or liver.

**Erythrocytes** have no nucleus, no mitochondria, no ribosomes — every organelle stripped out to make room for **hemoglobin**. One red cell holds roughly 300 million hemoglobin molecules, each capable of binding four oxygen atoms. The biconcave disk shape does two things at once: it maximizes surface-to-volume ratio for diffusion, and it lets the cell deform enough to squeeze single-file through capillaries narrower than its own resting diameter. Without a nucleus, the cell cannot repair itself. After 120 days the membrane proteins fail, the cell becomes rigid, and macrophages in the spleen eat it. You make about two million new red cells every second to replace them.

The signal driving that production is **erythropoietin (EPO)**, released by the kidneys when they detect low oxygen. EPO travels to bone marrow and accelerates red cell production. Climbers spend days at intermediate altitude waiting for EPO to raise their red cell counts before pushing higher — the same feedback loop, pushed past its design range with synthetic EPO injection, thickens blood enough to kill cyclists.

**White cells** — five to ten thousand per microliter against five million red cells — each do immune work no red cell can do. **Neutrophils** are first responders to bacterial infection. **Eosinophils** attack parasites. **Lymphocytes** are the B and T cells that remember pathogens and produce antibodies. **Monocytes** leave blood and become tissue macrophages. Blood is the immune system's highway, not its destination; white cells do their actual work after squeezing out of capillaries into tissues.

**Platelets** are not cells — they are cytoplasmic fragments shed by enormous bone-marrow cells called megakaryocytes. Their job is **hemostasis**: sealing vessel wall breaches. Three stages. Vascular spasm — smooth muscle in the damaged wall contracts immediately. Platelet plug — platelets bind exposed collagen, activate, change shape, and recruit more platelets within seconds. Coagulation cascade — twelve clotting factors activate each other in sequence until thrombin converts soluble fibrinogen into insoluble fibrin mesh, trapping platelets and red cells into a durable clot. The same cascade that saves you from bleeding can kill you when it fires inside an intact coronary artery. That trade-off — fast clotting versus dangerous internal clotting — is not a design flaw. It is the price of having a system fast enough to work.

---

## The heart — two pumps sharing one signal

The body needs blood delivered at two incompatible pressures.

The lungs are delicate. Their air sacs are separated from capillaries by membranes only one or two cells thick — a structural compromise that exists because oxygen must diffuse over short distances or it does not diffuse fast enough. The pressure that perfuses systemic organs (around 120 mmHg) would rupture those membranes. The lungs require about 25 mmHg. The rest of the body requires 120 mmHg.

A single pump cannot deliver both. So the heart became two pumps in series. The **right side** collects deoxygenated blood from the body and pushes it to the lungs at low pressure. The **left side** collects oxygenated blood from the lungs and pushes it to the body at high pressure. The right ventricular wall is about 3 mm thick. The left ventricular wall is about 15 mm thick. Five times the muscle, because it faces five times the resistance. The anatomy announces the pressure difference before any measurement is taken.

One rule governs all flow through the four chambers and four valves: *blood flows only when a pressure gradient permits, and the one-way valves enforce direction.* Two **atrioventricular valves** (tricuspid on the right, mitral on the left) prevent backflow from ventricles to atria. Two **semilunar valves** (pulmonary on the right, aortic on the left) prevent backflow from arteries into ventricles.

Both ventricles must eject exactly the same volume per beat. If the left ejected more, blood would drain from the pulmonary circuit into the systemic arteries. If the right ejected more, blood would back up in the lungs. This is not a design goal — it is a mechanical constraint of a closed loop. When the left ventricle weakens and fails to match the right's output, fluid backs up into the pulmonary capillaries, capillary pressure rises, and fluid leaks into the alveoli. The patient drowns slowly in their own edema.

<!-- → [INFOGRAPHIC: Diagram of the heart's two circuits in series — right heart to pulmonary circuit to left heart to systemic circuit — with pressure values labeled at each stage (right ventricle ~25 mmHg, left ventricle ~120 mmHg, capillaries ~30 mmHg, venous return ~5 mmHg)] -->

### The pacemaker that needs no wiring

Isolate one cardiac conduction cell in a dish with no nerves and no neighbors. It depolarizes, fires, recovers, and fires again — about 60 to 80 times per minute. The next beat is built into the recovery from the last one.

The mechanism is in the membrane. These cells have sodium channels that are never fully closed. Sodium drifts inward continuously, and the membrane potential drifts upward from about −60 mV toward −40 mV — the **prepotential**, sometimes called the pacemaker potential. At threshold around −40 mV, calcium channels open, calcium rushes in, the cell fires, then potassium channels repolarize it back to −60 mV. The cycle begins again. No external trigger required.

The **sinoatrial (SA) node**, in the right atrial wall, has the steepest prepotential and fires fastest: 60 to 100 bpm. The **AV node** at the junction of atria and ventricles fires at 40 to 60 bpm. The **Purkinje fibers** in ventricular muscle fire at 20 to 40 bpm. In a healthy heart the SA node fires first every time, its impulse resets every slower cell before it can fire independently, and no backup pacemaker is ever needed. This is **overdrive suppression**. If the SA node fails, the AV node takes over at its slower rate. If both fail, the Purkinje fibers generate an escape rhythm — enough to keep blood moving, not enough to sustain normal activity. The backups exist; they are degraded.

The conduction pathway after the SA node is choreographed. Atrial depolarization spreads to the **AV node**, where conduction slows by design — about 100 milliseconds. This gap lets the atria finish emptying into the ventricles before the ventricles start contracting. After the AV node, the signal accelerates down the **bundle of His**, splits into **bundle branches**, and fans out through **Purkinje fibers** to reach the ventricular apex before the base. The ventricle contracts from apex upward, squeezing blood toward the outflow valves at the base. A ventricle contracting in random order would be far less efficient.

### The ECG

Electrodes on the skin surface record the summed electrical activity of the heart's millions of cells. Three deflections per beat: the **P wave** (atrial depolarization), the **QRS complex** (ventricular depolarization — tall because the ventricles are massive), and the **T wave** (ventricular repolarization). Every deviation from the normal trace localizes a failure. A prolonged PR interval means the AV node is conducting slowly. A wide QRS means a bundle branch is blocked. Absent P waves with irregular ventricular rhythm means atrial fibrillation. **ST elevation** — the physician's five-second read in the opening case — means a region of myocardium is acutely ischemic, and which leads show the elevation localizes which coronary artery is blocked.

### The mechanical cycle

The electrical impulse triggers contraction. Contraction changes pressure. Pressure opens and closes valves. Follow the left ventricle through one beat.

During **diastole**, the ventricle relaxes. Blood flows passively from the left atrium because atrial pressure slightly exceeds ventricular pressure. The atrium then contracts (atrial systole) and delivers a final boost — about 20 to 30 percent of total filling. The ventricle contains about 130 mL at end-diastole: the **end-diastolic volume (EDV)**.

**Ventricular systole** begins. Pressure rises rapidly. When ventricular pressure crosses atrial pressure, the mitral valve slams shut — the first heart sound, the "lub" (S1). The ventricle is now sealed, pressure climbing, but aortic pressure (about 80 mmHg) still exceeds ventricular. No flow yet. This is **isovolumic contraction**. When ventricular pressure crosses aortic pressure and reaches about 120 mmHg, the aortic valve opens. About 70 mL leave; about 60 remain. **Stroke volume = EDV − ESV**, where ESV is the end-systolic volume. The **ejection fraction** (SV/EDV) is normally 55–70 percent; below 40 percent is heart failure.

Contraction stops. Pressure falls. When it drops below aortic pressure, the aortic valve slams shut — the second heart sound, the "dub" (S2). The ventricle is sealed again, pressure falling but mitral valve still closed. This is **isovolumic relaxation**. When ventricular pressure finally drops below atrial pressure, the mitral valve opens and filling begins.

The heart sounds are produced by valve *closure*, not valve opening. Turbulence from sudden reversal of flow against a closing valve creates the sound. S1 marks the start of systole; S2 marks the start of diastole.

<!-- → [CHART: Pressure-volume loop for the left ventricle — counterclockwise rectangle with corners labeled: filling (diastole), isovolumic contraction, ejection, isovolumic relaxation — with stroke volume readable as the width and mechanical work as the area enclosed; inset showing a depressed loop for heart failure and a taller narrower loop for hypertension] -->

---

## The master equation and four levers

$$\text{CO} = \text{HR} \times \text{SV}$$

Cardiac output is heart rate times stroke volume. A resting 70 kg adult: HR = 70 bpm, SV = 70 mL per beat, CO = 4.9 L/min. Every clinical scenario in cardiovascular physiology is a story about which term in this equation moved, and why.

There are four adjustable levers. Heart rate is one. Stroke volume is controlled by three: preload, afterload, and contractility.

**Heart rate** is set by the SA node's prepotential slope and modulated by the autonomic system. Parasympathetic input (vagus nerve, acetylcholine) slows the prepotential and slows the heart. Sympathetic input (cardiac nerves, norepinephrine) steepens it and speeds the heart. There is a ceiling: above about 180 bpm, diastolic filling time is so short that EDV falls, SV falls, and CO plateaus or even declines. The bottleneck shifts from contraction to filling.

**Preload** is the stretch on ventricular muscle fibers just before contraction — approximated by EDV. It depends on venous return: dehydration drops it, exercise raises it (the contracting skeletal muscle squeezes leg veins and pushes blood back toward the heart), lying down raises it relative to standing.

Preload feeds the **Frank-Starling mechanism**, and the Frank-Starling mechanism is the integrative core of how the heart matches output to input. Within physiological limits, *the more the ventricle is stretched before contraction, the more forcefully it contracts and the more blood it ejects.* If you give 500 mL of saline intravenously, EDV rises, SV rises on the next beat, CO rises — automatically, with no external signal required. If you lose 500 mL of blood, EDV falls, SV falls, CO falls.

Why does Frank-Starling work? Cardiac muscle, like skeletal muscle, contracts when actin and myosin filaments slide past each other. Each sarcomere — the repeating contractile unit — has an optimal length at which the overlap between actin and myosin is maximal, the most cross-bridges can form simultaneously, and force is greatest. Stretch the sarcomere too little and actin filaments from opposite ends interfere. Stretch it too far and the filaments pull apart. There is a Goldilocks length where force is maximal.

Resting cardiac sarcomeres sit *below* that optimum. When the ventricle fills more, the fibers stretch toward the optimum, more cross-bridges align favorably, contraction is stronger. There is also a calcium-sensitivity component: stretched fibers respond more strongly to the same calcium release, because tension changes the conformation of the troponin-tropomyosin regulatory complex on the actin filament. Frank and Starling observed the whole-organ consequence — more stretch, more force — decades before the molecular mechanism was understood. The molecular biology explains why their observation had to be true.

**Afterload** is the pressure the ventricle must overcome to eject blood — primarily aortic pressure for the left ventricle. The relationship is inverse: higher afterload, lower stroke volume, all else equal. In chronic hypertension, the left ventricle compensates by hypertrophying — thickening its wall to generate higher pressures. The adaptation carries a cost: a thicker wall is stiffer, fills less easily, and eventually fails at filling before it fails at ejection. The compensation plants the seed of its own failure.

**Contractility** is the intrinsic strength of the cardiac muscle at any given preload and afterload. Sympathetic activation raises the calcium released per action potential, which directly increases force. The same EDV now produces a larger SV. On the Frank-Starling curve, increased contractility shifts the entire curve upward: more SV at any preload. This is what exercise exploits: resting CO is 5 L/min; maximal exercise CO in a fit person reaches 25 L/min. HR rises from 70 to 180 (roughly 2.5×). SV rises because both preload and contractility rise simultaneously (roughly 1.8×). CO increases by recruiting all three SV levers plus HR at the same time.

<!-- → [CHART: Frank-Starling curves — two curves on one plot: normal curve and depressed curve (heart failure) — x-axis: end-diastolic volume; y-axis: stroke volume — with operating points marked for rest, exercise, and fluid-loaded heart failure; arrow showing upward shift of curve with increased contractility] -->

---

## Where the blood goes — vessels and the fourth power

The heart ejects blood into the aorta at about 120 mmHg. By the capillaries, pressure is around 30 mmHg. At the venous return to the right atrium it is near zero. Something extracted that pressure. The extraction was not accidental — it was engineered into the vessel walls.

Cut across an artery near the heart and look at the cross-section. Three concentric layers. The innermost **tunica intima** is the endothelium — a single layer of flat cells that blood contacts directly. The thick middle layer **tunica media** is wound smooth muscle and elastic fibers. The outer **tunica externa** is connective tissue anchoring the vessel.

Cut a vein. Same three layers, inverted proportions. Thick tunica externa, thin tunica media. The artery looks like a coiled spring; the vein looks like a deflated balloon. This is the pressure difference made visible in architecture.

The large arteries near the heart — aorta, common carotid, subclavian — are **elastic arteries**. When the ventricle ejects a pulse of blood, the elastic wall stretches, storing the energy. During diastole, the wall recoils and pushes blood forward. Without elastic recoil, pressure between heartbeats would drop nearly to zero and flow would be intermittent. The elastic arteries convert pulsatile ejection into continuous flow.

Farther from the heart, elastic fibers thin out and smooth muscle dominates. **Arterioles** — 30 to 100 micrometers across — are almost entirely smooth muscle relative to their lumen diameter. These are the resistance vessels, and most of the pressure drop in the entire systemic circulation happens here. The reason is one equation.

**Poiseuille's law**, derived in the 1840s by a French physician studying blood flow:

$$\text{Flow} = \frac{\pi \Delta P \, r^4}{8 \eta L}$$

Flow is proportional to the fourth power of the radius. Resistance is:

$$\text{Resistance} = \frac{8 \eta L}{\pi r^4}$$

Viscosity and tube length change slowly or not at all. Radius changes constantly, every time smooth muscle in an arteriole contracts or relaxes. And because radius is to the *fourth* power, a small change in radius produces an enormous change in resistance.

Halve the radius: resistance increases by $2^4 = 16$. Flow drops to one-sixteenth. A 20 percent reduction in radius — straightforward for smooth muscle — changes resistance by $(1/0.8)^4 \approx 2.4$, cutting flow by more than half. Atherosclerotic plaque that reduces a coronary artery's radius by 50 percent creates 16 times the resistance. Ischemia at rest may not yet appear — the heart has reserve capacity. But during exercise, when the myocardium needs four times its resting blood supply and the narrowed artery cannot deliver it, the patient feels the chest pain of angina. When the plaque ruptures and an acute clot completes the occlusion, the patient has a myocardial infarction.

This fourth-power dependence is why arterioles are the primary pressure-control valves of the circulation. Small radius changes, large flow effects. Thousands of these valves, each independently adjustable by sympathetic nerves and local chemical signals, direct blood away from resting tissue and toward active muscle, skin, or gut depending on the body's current needs.

**Capillaries** are the exchange surface. No tunica media. No tunica externa. Just one layer of endothelial cells on a thin basement membrane. The wall is thin enough that oxygen, glucose, and carbon dioxide can diffuse across it in milliseconds. Blood velocity through capillaries is the slowest in the entire circulation — about 0.04 cm/s — because velocity is inversely proportional to total cross-sectional area, and the aggregate cross-section of all capillaries in the body is far larger than the aorta's. Slow flow is what capillaries need: time for diffusion.

**Veins** carry low pressure but contain about 64 percent of total blood volume. They are reservoirs. When the body needs to return blood quickly — exercise, hemorrhage — sympathetic stimulation stiffens venous walls and pushes blood toward the heart. Leg veins have one-way valves; every step you take squeezes leg veins and drives blood upward. Stand still for an hour and venous return drops, preload drops, cardiac output drops, and you may feel dizzy or faint.

### Blood pressure: MAP, the real number

Systolic pressure is the peak (120 mmHg in a healthy adult). Diastolic is the trough (80 mmHg). Neither alone tells you what is perfusing organs. The number that matters is **mean arterial pressure (MAP)**, the time-weighted average over one cardiac cycle. Because the heart spends more time in diastole than in systole at normal rates:

$$\text{MAP} \approx \text{DBP} + \frac{1}{3}(\text{SBP} - \text{DBP})$$

For 120/80: MAP ≈ 80 + (40/3) ≈ 93 mmHg. Below 60, organ perfusion is inadequate. The kidneys will begin to fail.

And the governing identity:

$$\text{MAP} = \text{CO} \times \text{TPR}$$

Blood pressure equals cardiac output times total peripheral resistance — Ohm's law for fluid. Whenever blood pressure changes, CO or TPR has changed, or both. Most chronic hypertension is a vessel problem: arterioles are too constricted, TPR is too high, and the heart is pumping against a chronically elevated load.

### Regulation: fast and slow

The **baroreflex** operates in seconds. Stretch-sensitive nerve endings in the aortic arch and carotid sinuses fire at a rate proportional to blood pressure. Their signals reach the cardiovascular control center in the medulla, which adjusts autonomic outflow. Pressure rises: parasympathetic activity increases, sympathetic decreases, HR slows, vessels dilate, pressure falls. Pressure falls: the reverse. The reflex catches orthostatic drops in blood pressure when you stand, raises HR when you hemorrhage, and is the circuit the opening patient's body was running while the physician was reading his ECG.

The **RAAS** operates over hours to days by adjusting blood volume. Kidneys detecting low perfusion pressure release **renin**, which initiates a cascade: angiotensinogen → angiotensin I → angiotensin II (by ACE in lung capillaries) → vasoconstriction, aldosterone release, and ADH release. Aldosterone tells the kidneys to retain sodium and water, expanding blood volume, raising preload, raising CO, raising pressure. ACE inhibitors and angiotensin receptor blockers interrupt this cascade — among the most prescribed drugs in medicine.

The counterregulator is **atrial natriuretic peptide (ANP)**, released by stretched atrial muscle when blood volume is high. ANP promotes sodium and water loss through the kidneys, drops volume, drops pressure. RAAS is the accelerator. ANP is the brake.

<!-- → [INFOGRAPHIC: RAAS cascade — linear chain from low renal perfusion → renin release → angiotensin I → ACE conversion → angiotensin II → three downstream effects (vasoconstriction, aldosterone, ADH) — with drug intervention points labeled (ACE inhibitor, ARB)] -->

---

## Three scenarios, one set of levers

The Frank-Starling mechanism and the four levers are easier to hold onto through worked examples than through general principles. Three scenarios, same patient.

**Standing up.** The patient rises from a chair. Gravity pulls 500 mL into leg veins. Venous return drops. EDV falls from 130 mL to about 110. By Frank-Starling, SV falls from 70 to about 55 mL. Without compensation: CO = 70 × 55 = 3.85 L/min, a 21 percent drop. The baroreflex catches it in one second: HR rises from 70 to about 90, arteriolar tone increases. New CO: 90 × 55 ≈ 4.95 L/min. Nearly identical to resting. The system has rebalanced on a different combination of HR and SV. When this fails — in dehydration, autonomic neuropathy, some elderly patients on antihypertensives — the patient faints on standing.

**Exercise.** The patient starts running. Skeletal muscle pump increases venous return. Preload rises. Sympathetic activation raises HR and contractility simultaneously. Local metabolites dilate arterioles in working muscle while sympathetic constriction reduces flow to the gut and kidney. After a few minutes at high intensity: HR = 170, SV = 120 mL. CO = 170 × 120 = 20.4 L/min. Four-fold increase, with the elevated output directed disproportionately to working muscle by local arteriolar dilation. Without Frank-Starling, increased venous return would not translate to increased SV. The mechanism is not optional for exercise.

**Hemorrhage.** The patient loses 1.5 liters from a femoral artery laceration — about 30 percent of total blood volume. Venous return crashes. EDV falls to about 80 mL. SV falls to about 35 mL. The baroreflex fires hard: HR climbs to 130, arterioles constrict aggressively, skin goes pale, gut perfusion drops. Despite all of this: CO = 130 × 35 = 4.55 L/min. Near resting — but only through maximal sympathetic compensation. If bleeding continues, EDV falls below the minimum Frank-Starling requires, and no amount of HR or contractility increase compensates. SV craters. CO collapses. This is hemorrhagic shock. Fluid resuscitation works because it restores preload; the contractile machinery is intact, it just has nothing to pump.

A fourth scenario worth naming: **heart failure**. Contractility is depressed — the Frank-Starling curve is shifted downward at every preload. The body cannot distinguish low CO from low blood volume. RAAS activates chronically. Aldosterone retains sodium and water. Blood volume expands. Preload rises. But the failing ventricle has used up its Frank-Starling reserve; it is already near the top of its depressed curve, and further preload increases produce almost no increase in SV. The excess fluid backs up into the pulmonary capillaries (left-sided failure) and peripheral tissues (right-sided failure). The patient has ankle edema and shortness of breath. This is why diuretics — which *reduce* preload — improve symptoms in heart failure. Reducing one of the levers that normally raises CO actually helps a failing heart, because the lever it removes (excess fluid volume) had stopped producing SV and was only producing edema.

---

## Exercises

<!-- → [TABLE: Four-lever reference table — rows: heart rate, preload, afterload, contractility — columns: what it represents, what raises it, what lowers it, effect on CO when raised — to be placed at the start of exercises as a working reference] -->

**Warm-up 1.** A resting adult has a heart rate of 70 bpm and a stroke volume of 70 mL. Calculate cardiac output. Now the heart rate rises to 110 bpm but stroke volume falls to 50 mL because diastolic filling time has shortened. Calculate the new cardiac output. Is the net change positive, negative, or roughly neutral? What does this tell you about the ceiling on using heart rate alone to raise cardiac output? *Tests: the CO = HR × SV equation and the filling-time ceiling on heart rate.*

**Warm-up 2.** The right ventricular wall is 3 mm thick; the left is 15 mm thick. Explain the difference using exactly one physiological concept — afterload — without using the words "right" or "left." Then predict what would happen to the right ventricular wall thickness in a patient with chronic pulmonary hypertension (elevated pulmonary artery pressure). *Tests: connecting wall thickness to the pressure the ventricle must overcome, and applying that logic to a non-standard scenario.*

**Warm-up 3.** The first heart sound (S1) and second heart sound (S2) are produced by valve closure, not valve opening. For each sound: name which valve(s) close to produce it, state whether it marks the start of systole or diastole, and explain why turbulence from sudden flow reversal produces an audible sound while the valve opening does not. *Tests: valve mechanics, cardiac cycle timing, and the physical basis of heart sounds.*

**Application 1.** A patient receives 750 mL of intravenous saline rapidly. Trace the consequence through the cardiovascular system step by step: (a) what happens to venous return; (b) what happens to EDV; (c) what does the Frank-Starling mechanism predict for SV on the next beat; (d) what happens to CO; (e) what happens to MAP. Then explain why this same intervention in a patient with advanced heart failure, already operating near the top of a depressed Frank-Starling curve, could worsen rather than help — and what clinical sign would tell you you had crossed that threshold. *Tests: tracing a fluid bolus through the Frank-Starling mechanism and its limits.*

**Application 2.** A patient has a 60 percent narrowing (by radius) of her left anterior descending coronary artery from atherosclerotic plaque. Using Poiseuille's law, calculate how much this narrowing changes the resistance in that artery. At rest, her myocardial oxygen demand is met. During moderate exercise, she develops chest pain (angina). Explain why the same narrowing is silent at rest but symptomatic on exertion, using the relationship between cardiac output and myocardial oxygen demand. Then explain what happens when the plaque suddenly ruptures — why does the clinical situation change from stable angina to myocardial infarction in minutes? *Tests: applying the fourth-power law to a clinical scenario and connecting hemodynamics to ischemia.*

**Application 3.** A patient's ECG shows the following: normal P waves at regular intervals, a PR interval of 320 ms (normal: 120–200 ms), and normal QRS complexes. (a) Name this conduction abnormality. (b) Localize where in the conduction system the problem lies. (c) Explain the mechanism — what normally happens at this anatomical location, and what is happening instead? (d) At what point does this abnormality become clinically significant, and what can it progress to? *Tests: reading the ECG as a map of the conduction system.*

**Synthesis 1.** A 28-year-old marathon runner has a resting heart rate of 45 bpm and a resting cardiac output of 5 L/min. A sedentary 28-year-old has a resting heart rate of 75 bpm and the same resting cardiac output. Calculate each person's resting stroke volume. Then explain, at the level of the Frank-Starling mechanism and cardiac chamber remodeling, what structural adaptations account for the athlete's higher stroke volume. Finally, predict how each person's cardiovascular response to standing up will differ — who is more vulnerable to orthostatic hypotension, and why? *Tests: integrating cardiac output arithmetic with structural adaptation and clinical prediction.*

**Synthesis 2.** A patient with chronic heart failure has the following profile: depressed contractility, reduced ejection fraction (35%), elevated resting heart rate (92 bpm), and bilateral ankle edema. His cardiologist adds a diuretic to his regimen. (a) What does the diuretic do to blood volume and preload? (b) Why would reducing preload — a lever that normally raises CO — improve rather than worsen his symptoms? (c) His edema improves but his fatigue worsens slightly. Explain why these two changes can occur simultaneously in a patient with a depressed Frank-Starling curve. *Tests: the paradox of diuretic therapy in heart failure — using the Frank-Starling curve to show why reducing preload helps a failing ventricle that has run out of reserve.*

**Challenge.** A patient in septic shock has a blood pressure of 75/40 (MAP ≈ 52 mmHg) and a cardiac output of 9 L/min — well above the resting normal of 5 L/min. Using the identity MAP = CO × TPR, calculate her total peripheral resistance and compare it to a rough normal value of 1100 dyne·s·cm⁻⁵. Then answer: (a) Why is her cardiac output elevated despite low blood pressure? (b) Why is fluid resuscitation alone insufficient to restore her MAP, even though it raises preload? (c) Why are vasopressors (drugs that constrict arterioles) required as an additional treatment? (d) What does this scenario reveal about which term in the MAP = CO × TPR identity is the primary problem in septic shock, versus in cardiogenic shock (low CO, high TPR)? *Tests: applying MAP = CO × TPR to distinguish shock states by mechanism — the equation as a diagnostic tool, not just a formula.*

---

## LLM Exercises

The integrative core of this chapter — that cardiac output is governed by four levers acting through the Frank-Starling mechanism — is hard to feel from a static page. Build it as a simulator and use it to interrogate the scenarios.

### Build it — `09-cardiac-output.html`

**Show.** Paste this into Claude or ChatGPT or Gemini:

```
I want to build a cardiac output simulator as a single self-contained
HTML file (09-cardiac-output.html). It should let me adjust four sliders:
heart rate (40–200 bpm), preload (proxied as venous return on a 0–100
scale where 50 is normal), afterload (proxied as total peripheral
resistance on a 0–100 scale where 50 is normal), and contractility
(sympathetic tone on a 0–100 scale where 50 is normal). Display in real
time: (1) the Frank-Starling curve as a plot of stroke volume vs.
end-diastolic volume with the operating point marked, (2) the calculated
cardiac output in L/min, (3) an animated pressure-volume loop for the
left ventricle, and (4) a live ECG trace whose rate matches the heart
rate setting. Include three preset clinical scenarios: "Exercise" (high
HR, high preload, high contractility), "Hemorrhage" (low preload, high HR
compensation), and "Heart failure" (depressed Frank-Starling curve, high
fluid-retained preload). Before revealing the result of any slider change,
prompt me to predict the new cardiac output — then reveal the actual value.
Plain HTML, CSS, vanilla JavaScript. Canvas API for plots. No frameworks.
No external libraries.
```

**Say.** After the model builds it, ask it to walk you through what equation it used to relate each slider to each output, and where in the code each lever appears. Push back specifically: *Where does the Frank-Starling mechanism live in your simulation? Show me the actual function that converts EDV to SV, and show me how the contractility slider shifts that function. I want the math, not the slider.* A vague answer means the physiology was glossed over. Make it specific.

**Constrain.** Add these constraints one at a time and note which the model handles cleanly and which it fudges:

```
1. Cap the heart rate at which CO continues to rise at about 180 bpm.
   Above that, CO should fall because diastolic filling time becomes
   too short. If the simulator raises CO indefinitely with HR, this
   constraint is not implemented.

2. On the Frank-Starling curve, add a tooltip showing the current
   sarcomere length in the operating range. Turn the operating point
   red if it crosses onto the descending limb (very high preload,
   beyond physiological).

3. When preload is raised above 85 in the Heart Failure preset, the
   simulator should display a warning: "Operating point past Frank-
   Starling optimum — further preload increase will not improve SV."
```

The fudges are diagnostic. They show you where your prompt was underspecified, and where the physiology has subtleties without a clean computational shortcut.

**Verify.** Three tests:

1. Set everything to baseline (HR 70, preload 50, afterload 50, contractility 50). CO should be approximately 5 L/min. The P-V loop should be roughly rectangular with EDV around 130 mL and ESV around 60 mL.

2. Load "Exercise." CO should rise to 18–22 L/min. The Frank-Starling curve should shift upward. The P-V loop should widen and the ejection fraction should rise.

3. Load "Heart failure." CO should be marginally low. Now raise preload from 50 to 90. CO should rise initially, plateau, then fail to rise further — and the simulator should flag that you have pushed the operating point past the optimum. If raising preload simply raises CO indefinitely, the Frank-Starling mechanism is not actually implemented.

### Explore — three open questions

Once the simulator works, use it to investigate these:

**The exercise ceiling.** Try to drive CO above 30 L/min. You will fail. What is the binding constraint? Maximize HR, preload, contractility, and minimize afterload. Where does the simulator stop? Ask Claude *and* one other model how this constraint maps onto the real-world observation that VO₂ max correlates closely with peak cardiac output, and that it is the single best predictor of endurance performance. Compare the answers.

**The Frank-Starling logic of orthostatic hypotension.** Drop preload by 25 percent suddenly — modeling standing up. Predict what happens to CO before pressing the button. Then clamp HR at 70 and repeat. Why does the patient with autonomic neuropathy faint on standing while a healthy person does not? Ask the model which lever is broken and what drug class restores it.

**The vicious cycle of heart failure.** Load "Heart failure." Slowly increase preload to model RAAS-driven fluid retention. What happens to CO over the first few increments? What happens past a certain point? Connect this to the observation that diuretics improve symptoms in heart failure. Ask the model to explain why reducing preload helps a patient whose CO is already low. If the model cannot explain the apparent paradox — reducing a lever that normally raises CO actually improves the patient — it has not understood the Frank-Starling mechanism.

### Extend — forward to Chapter 10

The cardiovascular system delivers blood. Chapter 10 examines what runs alongside it — the lymphatic system and the immune network it carries. Two questions to put to a model before you arrive:

```
I learned that about 4 liters of fluid filter out of capillaries per
day and are not reabsorbed. Where does that fluid go, and what would
happen if lymphatic drainage were completely blocked?
```

```
White blood cells use the bloodstream as a highway but do their immune
work in tissues. What structural features must the lymphatic system
have to gather pathogens from tissues, present them to lymphocytes, and
route activated lymphocytes back into the bloodstream?
```

The cardiovascular system you have just built is the medium. The lymphatic system is what listens for trouble.

---

Chapter 10 extends the loop — the same blood that this chapter pushes through vessels is also the vehicle for the immune system's surveillance network, and the capillary exchange that Poiseuille's law governs is also where pathogens and immune cells encounter each other.

---

**What would change my mind.** If a normally functioning mammalian heart were shown to routinely operate on the descending limb of the Frank-Starling curve under physiological conditions — not just in dilated cardiomyopathy — the claim that the healthy heart operates entirely on the ascending limb would need revision. If the calcium-sensitivity component of Frank-Starling turns out to be better explained by lattice-spacing changes than by troponin-tropomyosin conformational change, the molecular account would need updating.

**Still puzzling.** Why the two-pump series design rather than a three- or four-chamber serial pump that would offer finer pressure control. Whether the descending limb of the Frank-Starling curve represents a real physiological failure mode or an artifact of isolated-heart preparations. And why EPO blood doping increases oxygen-carrying capacity but, past a hematocrit threshold, reduces the net oxygen delivery it was supposed to enhance — the fourth-power viscosity cost overtaking the linear hemoglobin gain.

---

**Tags:** cardiovascular-system, frank-starling-mechanism, cardiac-output, blood-pressure-regulation, electrocardiography
