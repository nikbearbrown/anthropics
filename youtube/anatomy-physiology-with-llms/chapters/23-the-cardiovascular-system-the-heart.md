# Chapter 23 — The Heart: A Pump Built from Muscle
*Three systems, one fist-sized muscle, 100,000 beats a day without being asked.*

The heart beats roughly 100,000 times per day without being told to. No signal arrives from the brain. No external pacemaker sends the command. The muscle generates its own electrical rhythm, sustains it for a lifetime, and modulates it in response to demand — all without waiting for instructions.

That is remarkable enough. But the machinery behind it is even more interesting than the autonomy. The heart is not one pump but two, running in series, solving a pressure problem that a single pump cannot solve. It generates its own electrical signal through a property unique to cardiac muscle cells. And it translates that electrical signal into mechanical force through a cycle so precisely timed that every phase depends on the one before it. This chapter is the machinery behind those 100,000 beats.

---

## Why There Are Two Pumps

The problem is pressure. The lungs are delicate — air sacs separated from capillaries by membranes only a cell or two thick. A pressure of 120 millimeters of mercury would rupture them. But the body's tissues — muscles, kidneys, liver, brain — demand high pressure to force blood through capillary beds against the resistance of narrow vessels. The arterial system routinely carries 120 mmHg. The pulmonary circuit needs to operate around 25 mmHg. These two requirements are incompatible in a single pump.

The heart's solution is to become two pumps, arranged in series, sharing one electrical signal. The right side — right atrium and right ventricle — collects deoxygenated blood from the body and pushes it to the lungs at low pressure. The left side — left atrium and left ventricle — collects oxygenated blood returning from the lungs and pushes it to the body at high pressure. The wall of the right ventricle is about 3 millimeters thick. The wall of the left ventricle is about 15 millimeters thick. Five times the muscle, because it faces five times the resistance. The anatomy announces the pressure difference before any measurement is taken.

<!-- → [DIAGRAM: cross-section of the heart showing all four chambers — label right atrium, right ventricle, left atrium, left ventricle, pulmonary trunk, aorta, superior and inferior venae cavae, pulmonary veins, and all four valves; highlight the wall thickness difference between right and left ventricle with a measurement callout; use arrows to show direction of blood flow through the pulmonary and systemic circuits; caption: "the wall thickness is the anatomy announcing the pressure difference — 3 mm on the right for 25 mmHg, 15 mm on the left for 120 mmHg"] -->

The two circuits are in series — the output of the right side becomes the input to the left, and the output of the left becomes the input to the right. This has a critical consequence: both ventricles must eject exactly the same volume per beat. If the left ventricle ejected more blood per cycle than the right, blood would drain from the pulmonary circuit and accumulate in the systemic arteries. If the right ejected more, blood would back up in the lungs. This is not a design goal written into a specification — it is a mechanical constraint. The circuits are physically linked, and the volumes must balance.

This constraint also explains one of the classic presentations of heart failure. When the left ventricle weakens and cannot eject blood efficiently, blood backs up into the pulmonary circuit. Pressure in the pulmonary capillaries rises. Fluid leaks through the thin membranes into the air sacs. The person drowns, slowly, in their own fluid. The right ventricle continues pumping into a system whose downstream pump is failing. The failure of one side reverberates through both circuits because the circuits are one closed loop.

---

## The Pacemaker That Needs No Wiring

Take a single cardiac conductive cell and isolate it — place it in a dish with a nutrient solution, remove every nerve, every neighboring cell, every external electrical input. The cell depolarizes. It fires. It recovers. It fires again. At roughly 60 to 80 beats per minute, alone in a dish, it maintains its rhythm. This is autorhythmicity, and it is a property cardiac muscle cells possess that skeletal muscle cells do not.

The mechanism is in the membrane. Most cells — including the cardiac muscle cells that actually contract — maintain a stable resting potential around −80 to −90 millivolts. They sit at that potential until an external stimulus arrives. Conductive cells are different. They have sodium channels that are never fully closed: sodium leaks continuously inward, and the membrane potential drifts upward from about −60 mV toward −40 mV. This slow upward drift is called the prepotential or spontaneous depolarization. When the membrane reaches about −40 mV, calcium channels open, calcium rushes in, and the cell depolarizes fully — reaching about +15 mV. Potassium channels then open, the cell repolarizes back toward −60 mV, and the cycle begins again. No stimulus required. The next beat is built into the recovery from the last one.

<!-- → [DIAGRAM: action potential trace for a pacemaker cell (SA node) vs. a contractile cell — pacemaker shows the characteristic slowly rising prepotential from -60 mV to -40 mV before the rapid upstroke; contractile cell shows flat resting potential at -90 mV followed by rapid depolarization only when externally triggered; label the prepotential, threshold, rapid depolarization, and repolarization phases on the pacemaker trace; caption: "the pacemaker cell has no stable resting potential — the prepotential is why it fires without being asked, and its slope is what the autonomic system adjusts to change heart rate"] -->

The heart contains many populations of these conductive cells, distributed through a circuit from the top of the right atrium down to the tips of both ventricles. Each population can generate its own rhythm. But they do not all generate it at the same rate. The sinoatrial node — a cluster of cells in the wall of the right atrium near where the superior vena cava enters — has the fastest prepotential. It reaches threshold most quickly, typically 60 to 100 times per minute. The atrioventricular node is slower, perhaps 40 to 60 times per minute. The bundle of His and Purkinje fibers are slower still, 20 to 40 times per minute.

In a healthy heart, the SA node fires before any other pacemaker site has reached threshold. Its impulse spreads outward and depolarizes the slower cells before they can fire on their own. Those cells are reset to their post-depolarization state, and the prepotential begins again from a reset baseline. They never get the chance to reach threshold independently. This is called overdrive suppression: the fastest pacemaker continuously preempts all slower ones.

The vulnerability in this system is elegant to see. If the SA node fails — through ischemia, fibrosis, or progressive disease — the suppression disappears. The next fastest pacemaker, the AV node, takes over. But it fires at 40 to 60 beats per minute rather than 60 to 100. The person feels the difference. If the AV node also fails, the Purkinje fibers generate an escape rhythm at 20 to 40 beats per minute — enough to keep blood moving, not enough to sustain normal function. The backup systems exist but they are degraded backups, and their slower rates are a diagnostic signal of how far up the conduction hierarchy the failure has occurred.

The path the electrical impulse takes once the SA node fires is not random diffusion. Three internodal pathways carry the signal preferentially toward the AV node while the impulse also spreads through the atrial muscle directly, triggering atrial contraction. The signal arrives at the AV node and slows. The cells of the AV node are small and conduct slowly — by design. The delay they introduce is about 100 milliseconds. This pause is not a flaw; it is the gap between atrial contraction finishing and ventricular contraction beginning. Without it, the ventricles would start contracting while still filling from the atria, and the stroke volume would decrease.

After the AV node, the impulse accelerates. It travels down the bundle of His, splits into left and right bundle branches that run along the interventricular septum, and fans out through the Purkinje fiber network into the ventricular myocardium. The signal reaches the apex — the bottom of the heart — before it reaches the base. This sequencing is not accidental. A ventricle that contracts from the apex upward squeezes blood toward the outflow valves at the base. A ventricle that contracted randomly, or from the base down, would be less efficient at ejecting blood through the aortic and pulmonary valves. The conduction geometry shapes the mechanics.

<!-- → [DIAGRAM: conduction system pathway through the heart — label SA node (right atrium wall), internodal pathways, AV node, bundle of His, left and right bundle branches, and Purkinje fiber network; add timing annotations in milliseconds at each node (SA node: 0 ms, AV node: ~50 ms with a pause label, ventricular apex: ~175 ms, ventricular base: ~225 ms); caption: "the 100 ms AV node delay is not a flaw — it is the gap that lets the atria finish emptying before the ventricles begin contracting"] -->

The entire sequence from SA node firing to ventricular depolarization takes about 225 milliseconds — a little less than a quarter of a second. At a resting heart rate of 70 beats per minute, one complete cycle takes about 857 milliseconds. The electrical events occupy roughly a quarter of that; the mechanical events fill the rest.

Electrodes on the skin surface record the summed electrical activity of millions of cells as the wave of depolarization and repolarization sweeps through the heart. The P wave is atrial depolarization. The QRS complex — a rapid three-part deflection — is ventricular depolarization. The T wave is ventricular repolarization. Each represents a mechanical event: P wave signals atrial contraction, QRS signals ventricular contraction, and the interval from QRS to the next P wave encodes heart rate. A prolonged PR interval means the AV node is conducting slowly — perhaps from inflammation or scar tissue. A wide QRS means the impulse is not traveling the normal fast pathways — perhaps a bundle branch has been blocked by ischemia. An absent P wave may mean an ectopic pacemaker in the atria has taken control from the SA node. The pattern on the surface of the body is a map of where the conduction system is intact and where it is not.

<!-- → [DIAGRAM: normal ECG trace with labeled components — P wave, PR interval, QRS complex, ST segment, T wave, and RR interval (one full cardiac cycle); below it show three abnormal traces side by side: prolonged PR interval (AV block), wide QRS (bundle branch block), absent P waves (atrial fibrillation); caption: "the ECG is a map of the conduction system's health — each deviation corresponds to a specific anatomical location where conduction is failing"] -->

---

## The Mechanical Cycle: Pressure, Volume, and Valves

The electrical impulse causes contraction. The contraction changes pressure. The pressure changes open and close valves. The valves determine when blood flows and when it does not. The mechanical cycle is this sequence of pressure changes choreographed by the electrical one, and understanding it requires following what happens to pressure and volume in the left ventricle over one beat.

Begin with the ventricle relaxed and filling. Blood flows passively from the left atrium into the ventricle because atrial pressure is slightly higher than ventricular pressure. About 70 to 80 percent of ventricular filling happens this way, purely passively. The atrium then contracts — atrial systole — and delivers the remaining 20 to 30 percent as a final boost. By the end of this filling phase, the ventricle contains about 130 milliliters of blood. This is the end-diastolic volume (EDV), the starting volume for the ejection to come.

Now the ventricle begins to contract. Pressure inside rises rapidly. As soon as ventricular pressure exceeds atrial pressure — which happens almost immediately — blood tries to flow backward into the atrium. The mitral valve snaps shut. This is the first heart sound, the "lub." The ventricle is now a closed chamber, contracting and raising pressure, but with nowhere for the blood to go — because the pressure in the aorta is still about 80 mmHg, and the ventricle hasn't yet exceeded it. The ventricle continues to generate pressure against closed valves, at constant volume. This is isovolumic contraction. On a graph of pressure versus volume, it appears as a vertical line: pressure rising, volume unchanged.

When ventricular pressure finally exceeds aortic pressure — crossing 80 mmHg and continuing to rise toward 120 — the aortic valve opens. Blood flows out. The ventricle continues contracting, shrinking in volume as it ejects blood into the aorta. Pressure rises slightly with the initial ejection, then falls as the ejection continues and the ventricle shortens. The ventricle ejects about 70 milliliters. About 60 milliliters remain — the end-systolic volume (ESV). The ejection fraction is the fraction of the EDV that was ejected: 70 divided by 130, or about 54 percent. A healthy ejection fraction is 55 to 70 percent. Below 40 percent begins to constitute heart failure.

Then the ventricle stops contracting. Pressure inside falls. When it drops below aortic pressure, the aortic valve snaps shut. This is the second heart sound, the "dub." Now the ventricle is again a closed chamber — pressure falling, but valves still closed because ventricular pressure hasn't yet dropped below atrial pressure. The volume is temporarily unchanged as pressure falls. This is isovolumic relaxation, the mirror of isovolumic contraction.

When ventricular pressure finally drops below atrial pressure, the mitral valve opens again and filling begins. The cycle closes.

<!-- → [DIAGRAM: pressure-volume loop for the left ventricle — x-axis: ventricular volume (mL), y-axis: ventricular pressure (mmHg); trace the loop clockwise through all four phases labeled: (1) filling (bottom right, moving right as volume increases at low pressure); (2) isovolumic contraction (vertical line upward, volume constant); (3) ejection (top, moving left as volume decreases); (4) isovolumic relaxation (vertical line downward, volume constant); mark EDV (~130 mL), ESV (~60 mL), stroke volume (70 mL = EDV - ESV), and the two valve events (mitral valve closes at start of isovolumic contraction, aortic valve opens at end, aortic valve closes at end of ejection, mitral valve opens at end of isovolumic relaxation); caption: "the area enclosed by the loop equals the mechanical work done per beat — a rightward shift signals incomplete ejection; an upward shift signals a stiff ventricle that cannot relax"] -->

Two features of this cycle deserve emphasis. First, the valve closures — not openings — create the heart sounds. When blood flow reverses direction as a valve closes, the turbulence creates the sounds a stethoscope detects. The first sound marks the start of ventricular systole; the second marks its end. The gap between them is systole; the gap from the second sound to the next first sound is diastole.

Second, isovolumic contraction and relaxation are not wasted effort. They are the pressure-building and pressure-releasing phases that time the valve openings precisely. Without isovolumic contraction, the aortic valve would open before sufficient pressure was generated to maintain aortic flow. Without isovolumic relaxation, filling would begin before the ventricle had time to relax enough to receive blood at low pressure.

---

## What Governs Stroke Volume

Every beat the heart ejects a certain volume of blood — the stroke volume. Multiplied by heart rate, this gives cardiac output: the liters per minute the heart delivers to the circulation. At rest, roughly 5 liters per minute. During maximal exercise, 20 liters per minute or more. Three factors determine stroke volume at any given moment.

The first is preload: the volume of blood in the ventricle at the end of filling, just before contraction begins. This is the end-diastolic volume. A ventricle that fills with more blood — because venous return has increased, because exercise has sent more blood flowing back from the muscles — begins contraction with stretched fibers. Stretched fibers generate more force. This is the Frank-Starling relationship: within physiological limits, the more you fill the ventricle, the more forcefully it contracts and the more blood it ejects. The heart automatically adjusts its output to match its input, without needing any neural signal to do so. Increased venous return causes increased stroke volume; reduced venous return (from dehydration, from hemorrhage) causes reduced stroke volume.

The second is afterload: the pressure the ventricle must overcome to eject blood. In the left ventricle, this is primarily the pressure in the aorta. In hypertension, aortic pressure is chronically elevated. The left ventricle must generate higher pressures to open the aortic valve and maintain ejection. Over years, the ventricle responds by hypertrophying — the wall thickens. A thicker wall is stiffer, and a stiffer ventricle relaxes more slowly. The very adaptation that helps the ventricle pump against high pressure eventually impairs its ability to fill — the chamber becomes less compliant, diastolic function deteriorates. Chronic elevated afterload creates a cascade of compensations, each with its own cost.

The third is contractility: the intrinsic strength of the muscle at a given preload and afterload. Sympathetic nervous system activation — through norepinephrine and epinephrine — increases contractility directly. The same stroke volume can now be ejected against greater afterload, or a higher fraction of the end-diastolic volume can be ejected. During exercise, sympathetic activation increases both heart rate and contractility simultaneously. The combination of increased preload (from higher venous return), increased heart rate, and increased contractility allows cardiac output to rise fourfold or more above resting levels.

<!-- → [DIAGRAM: Frank-Starling curve — x-axis: end-diastolic volume (mL); y-axis: stroke volume (mL); show the normal curve rising steeply then plateauing; overlay a second curve shifted downward labeled "heart failure" (same EDV produces less stroke volume); overlay a third curve shifted upward labeled "increased contractility/sympathetic activation" (same EDV produces more stroke volume); caption: "the Frank-Starling relationship means the heart automatically matches output to input — but in heart failure the curve shifts down, so the same filling produces less ejection"] -->

---

## The Autonomic System as Volume Control

The heart sets its own rhythm, but the autonomic nervous system turns a dial on that rhythm. At rest, the parasympathetic nervous system — via the vagus nerve releasing acetylcholine — slows the SA node's spontaneous depolarization. The SA node's intrinsic rate, without any autonomic input, is about 100 to 120 beats per minute. At rest, parasympathetic tone reduces this to 60 to 80 beats per minute. Sympathetic activation counteracts this, increasing the rate of spontaneous depolarization and thereby increasing heart rate.

The cardiovascular control center in the medulla orchestrates this balance. It receives input from baroreceptors in the aortic arch and carotid arteries that detect blood pressure, and from chemoreceptors that detect oxygen, carbon dioxide, and pH. If blood pressure drops, baroreceptor firing decreases, sympathetic activity increases, parasympathetic activity decreases, and the heart rate rises to restore pressure. If blood oxygen falls, chemoreceptors trigger sympathetic activation. The control center integrates these signals and adjusts the balance of autonomic outflow continuously, moment to moment.

During exercise, multiple signals converge simultaneously: neural signals from moving muscles, rising carbon dioxide, falling oxygen, decreasing baroreceptor firing as cardiac output begins increasing. The sympathetic system accelerates the heart, increases contractility, and constricts blood vessels in the gut and skin while dilating vessels in the active muscles. The result is a heart pushing 20 liters per minute to muscles receiving the majority of that flow.

A resting heart rate of 40 beats per minute in a trained athlete is not a sign of a slow heart — it is a sign of a heart capable of ejecting 100 to 130 milliliters per beat instead of 70. Cardiac output at rest is the same 5 liters per minute regardless of whether the rate is 40 or 80; the trained heart achieves it with half the beats. When exercise begins, the trained heart can increase stroke volume dramatically — because years of training have enlarged the ventricles, increasing end-diastolic volume — and can raise heart rate from 40 to 180, achieving peak cardiac outputs of 25 to 35 liters per minute. The untrained heart reaches 180 beats per minute from a starting point of 75, and with a smaller stroke volume, achieves 20 liters per minute or less.

---

## The System as a Whole

The heart's three systems — the dual-pump architecture, the self-generating electrical circuit, and the mechanical valve-and-pressure cycle — are not independent features. They are three aspects of one design.

The dual-pump architecture exists because one pump cannot simultaneously maintain the low pressure the lungs require and the high pressure the body demands. The consequence is that both sides must eject identical volumes per beat, which is why failure of one side immediately affects the other.

The autorhythmic electrical system exists because cardiac output cannot be allowed to stop while waiting for neural input. The heart must beat even if the brainstem is injured, even if autonomic signals are interrupted, even in an isolated culture dish. The SA node's intrinsic rhythm is the failsafe; the autonomic system is the modulator.

The mechanical cycle of isovolumic contraction and relaxation, valve openings, and ejection exists because pressure must be built before flow can occur, and pressure must be released before filling can resume. Every phase serves the one that follows.

When any of these systems fails — when the conduction pathway is interrupted by scar tissue, when a valve fails to open or fails to close, when the myocardium is weakened by ischemia and cannot generate sufficient pressure — the failure propagates through all three. A blocked left bundle branch changes the timing of ventricular activation, reducing ejection efficiency. A diseased mitral valve that fails to close completely allows blood to flow backward into the atrium during systole, reducing stroke volume. A weakened myocardium that cannot complete isovolumic contraction adequately never achieves sufficient pressure to open the aortic valve against normal afterload.

The heart that beats 100,000 times per day without instruction is not simple. It is the solution to several simultaneous constraints — maintaining two pressures, generating its own rhythm, and timing the mechanical events of each beat precisely — solved by a single fist-sized muscle working continuously from before birth until death.

---

## Exercises

**Warm-up**

1. The right ventricle wall is 3 mm thick; the left is 15 mm thick. Explain this difference using one concept only — afterload — without using the words "right" or "left."

2. The AV node introduces a 100 ms delay in conduction. A student claims this is an inefficiency that slows the heart rate unnecessarily. Explain why the student is wrong, using what you know about the mechanical consequence of removing the delay.

3. The SA node's intrinsic rate is 100–120 bpm, but healthy resting heart rate is 60–80 bpm. What is suppressing the SA node's intrinsic rate, and what would happen to heart rate if that suppression were suddenly removed?

**Application**

4. A patient with severe dehydration arrives in the emergency department with a heart rate of 120 bpm and low blood pressure. Trace the physiological chain: how does reduced blood volume lead to the elevated heart rate, naming the sensors, pathways, and effectors involved?

5. During atrial fibrillation, the atria contract chaotically and the "atrial kick" (the final 20–30% of ventricular filling) is lost. Using the Frank-Starling relationship, explain why this reduces stroke volume — and predict whether the effect would be worse during exercise or at rest.

6. A 55-year-old with a 20-year history of hypertension is found to have a thickened left ventricular wall (left ventricular hypertrophy) and an ejection fraction of 60% — technically normal. Yet he is breathless on exertion. Explain how chronic elevated afterload produces a structurally adapted but functionally impaired heart, and why his symptoms are diastolic in origin.

**Synthesis**

7. A patient has a complete left bundle branch block — the left bundle branch is non-conducting. The right ventricle depolarizes normally via its bundle branch, but the left ventricular myocardium must depolarize via slower cell-to-cell conduction. Predict the consequences for: (a) the QRS complex width on ECG, (b) the timing of left vs. right ventricular contraction, and (c) stroke volume. Explain the mechanism behind each prediction.

8. A trained endurance cyclist has a resting heart rate of 42 bpm and a maximum heart rate of 178 bpm. A sedentary person of the same age has a resting HR of 78 bpm and a maximum HR of 178 bpm. If the cyclist's resting cardiac output is 5 L/min (same as the sedentary person), calculate her resting stroke volume and compare it to the sedentary person's. Then calculate the maximum cardiac output of each, assuming the cyclist's maximum stroke volume is 155 mL and the sedentary person's is 95 mL. Explain what structural adaptation accounts for the difference in stroke volume.

9. In left-sided heart failure, the left ventricle cannot eject blood efficiently. The right ventricle continues to pump normally. Trace the consequences of this asymmetry through the pulmonary circulation — explaining what happens to pulmonary capillary pressure, fluid balance in the alveoli, and gas exchange — and explain why the patient's primary symptom is breathlessness rather than reduced blood pressure in the systemic circulation.

**Challenge**

10. The Frank-Starling relationship states that increased preload leads to increased stroke volume — up to a point. Beyond a critical end-diastolic volume, further stretching of the myocardium reduces contractile force rather than increasing it (the descending limb of the Starling curve). This is rarely seen clinically in healthy hearts. Using what you know about the molecular basis of actin-myosin cross-bridge cycling and the optimal sarcomere length for force generation, propose a mechanism for why overstretching reduces force — and then propose a reason why the healthy heart's operating range is calibrated to avoid the descending limb under normal physiological conditions.
