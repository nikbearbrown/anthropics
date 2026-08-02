# Chapter 6 — The Nervous System I: Structure
*One mechanism at two scales — the membrane and the brain.*

---

Here is something worth sitting with. A woman wakes up and the vision in her right eye has gone grainy. Not dark — grainy, as though the channel has lost half its signal. By the next day, the center of that visual field is a soft gray patch that moves when she moves her gaze. A neurologist finds nothing wrong with her eye. An MRI shows a bright spot along the right optic nerve, and three older, smaller spots scattered through the white matter of her cerebrum. The diagnosis is a first attack of multiple sclerosis.

The axons are intact. The retinal cells are firing. The visual cortex is fine. What has gone wrong is the insulating wrap around the axon — a fatty sheath made by support cells called oligodendrocytes — and the consequence is that the electrical signal carrying visual information no longer arrives cleanly. Some of it is arriving slowly. Some of it is not arriving at all. The problem is the cable, not the camera or the screen.

Three months later, with steroids and time, her vision mostly returns. But the diagnosis carries a forecast: more attacks, in different places, over years. Each will produce a different symptom, because the same kind of damage in a different location produces a different clinical picture. Optic nerve plaque: vision loss. Brain stem plaque: double vision or vertigo. Spinal cord plaque: numbness or weakness below the level of the lesion.

Why? Because a sheath of fat around a wire determines how fast the wire conducts. And conduction speed turns out to matter, at the scale of milliseconds, to whether a signal arrives at all.

To understand any of this — why the sheath matters, why the signal exists, what "a signal traveling down an axon" even means — you have to start smaller. You have to start at a single membrane.

---

## What a neuron actually is

The first thing to clear up: a neuron is not a wire.

A wire conducts electricity by letting electrons drift through metal. A neuron conducts a signal by letting ions — sodium, potassium, calcium, chloride — flow briefly across a membrane, and by letting that flow trigger more flow next door. The medium is not electron movement. It is the controlled collapse of a chemical disequilibrium across a thin lipid film.

Picture a neuron as a long, sealed bag of saltwater. The membrane of that bag is slightly leaky, selectively permeable, and studded with protein machines that spend metabolic energy maintaining a chemical tension across it. The tension is the battery. Everything the neuron does is built on top of maintaining and then briefly releasing that tension.

The geometry has three named regions, each doing a different job. The **cell body (soma)** contains the nucleus and most of the metabolic machinery — it is the manufacturing center. The **dendrites** are branching extensions that receive signals from upstream neurons; the word comes from the Greek for tree, and a single cortical neuron may have thousands of dendritic branches. The **axon** is the outgoing signal line — one per neuron, running sometimes a very long way to its target. At the far end it splits into terminals that form chemical junctions with the next cell. A sensory neuron with its cell body near the spinal cord can have an axon over a meter long: one cell, thinner than anything visible to the naked eye, running continuously from lumbar spine to the skin of the big toe.

Wrapped around many axons, in segments, is **myelin** — a thick fatty insulating layer made not by the neuron but by dedicated support cells. In the peripheral nervous system these are **Schwann cells**, each wrapping one segment of one axon. In the central nervous system they are **oligodendrocytes**, each sending arms to myelinate segments of several different axons. The wrapping is not continuous. Between each myelinated segment is a small bare patch of axon called a **node of Ranvier**, named for the French histologist who described them in the 1870s. The nodes are where the signal regenerates. Why that matters will become clear when we get to conduction.

The other glial cells are worth naming because they appear in clinical contexts constantly. **Astrocytes** buffer the chemical environment around neurons, regulate blood flow to active tissue, and form part of the blood-brain barrier. **Microglia** are the immune cells of the brain — the inflammatory responders that, when chronically activated, contribute to neurodegeneration. **Ependymal cells** line the fluid-filled ventricles and produce cerebrospinal fluid. Glia match neurons roughly in number, the ratio varying by region; older estimates of 10:1 glia-to-neuron have been substantially revised downward by more careful counting. [verify — Azevedo et al., 2009, *J Comp Neurol*]

---

## The resting potential — stored disequilibrium

A neuron at rest holds a voltage of roughly −70 millivolts across its membrane. Inside is 70 mV more negative than outside. This is not equilibrium. The cell is sitting at a steady electrical tension — a stretched spring — that it spends a significant fraction of its metabolic budget maintaining.

Two things together create and hold this tension.

The first is the **Na⁺/K⁺ ATPase**, a protein pump that burns one ATP per cycle. Each cycle pumps three sodium ions out of the cell and two potassium ions in. The pump runs continuously. The result, over time: sodium is concentrated outside (extracellular Na⁺ is about ten times higher than intracellular), and potassium is concentrated inside (intracellular K⁺ is about thirty times higher than extracellular). The membrane potential is not free. The brain spends roughly 20% of the body's resting energy budget running these pumps. [verify]

The second is the **K⁺ leak channels** — potassium-selective channels in the membrane that are always open. With potassium concentrated inside, K⁺ flows out through these channels, down its concentration gradient. As it leaves, it carries positive charge with it. The inside becomes more negative. But that negative inside now pulls the positively-charged K⁺ back in. At some voltage, the chemical force pushing K⁺ out exactly balances the electrical force pulling it back. That voltage is the equilibrium potential for potassium, written E_K, and it sits around −90 mV.

The actual resting potential is −70 mV, not −90 mV, because the membrane is not perfectly impermeable to everything else. A small sodium permeability pulls V_m a few tens of millivolts toward E_Na (which is around +60 mV). The resting potential is a weighted average of the equilibrium potentials of all the ions the membrane is permeable to, weighted by their relative permeabilities. At rest, K⁺ dominates, so the membrane sits close to E_K but not at it.

This has an immediate clinical consequence. A patient comes in with low extracellular potassium — hypokalemia, from diuretics or vomiting. The K⁺ gradient across the membrane is now steeper than normal, which means E_K is more negative than usual, which means the resting potential is more negative than usual. The cell is hyperpolarized. It now needs a larger depolarization to reach threshold. Excitable cells — muscle especially — become sluggish. The patient is weak. The heart's electrical rhythm changes. Correct the potassium, the resting potential normalizes, the weakness resolves. The whole clinical syndrome is a consequence of one ion's concentration changing by a small amount on one side of a membrane.

The vocabulary: when V_m moves toward zero (less negative), the cell is **depolarized**. When it moves further from zero (more negative), the cell is **hyperpolarized**. These words do constant work in what follows.

---

## Graded potentials — the analog input

Before the action potential, something smaller happens. When a neurotransmitter arrives at a dendrite and opens a receptor channel, ions flow briefly and produce a small local change in V_m — a fraction of a millivolt to a few millivolts. This is a **graded potential**.

Two defining properties. It is **local** — largest at the synapse, diminishing with distance. It is **graded** — proportional to the strength of the input, not all-or-nothing. A stronger stimulus produces a larger graded potential.

Two types. An **EPSP** (excitatory postsynaptic potential) is a small depolarization — it nudges V_m toward threshold, typically by letting Na⁺ in. An **IPSP** (inhibitory postsynaptic potential) is a small hyperpolarization — it nudges V_m away from threshold, typically by letting Cl⁻ in or K⁺ out.

A single EPSP of 0.5 mV cannot fire a neuron whose threshold sits 15 mV above its resting potential. The cell body adds them up. **Spatial summation**: multiple synapses fire simultaneously, their graded potentials are added across the cell. **Temporal summation**: one synapse fires repeatedly, each EPSP arriving before the last has fully decayed, the voltages piling up.

The summed potential travels passively to the **axon hillock** — the junction between cell body and axon, which carries the highest density of voltage-gated sodium channels in the cell. This is the trigger zone. If the summed potential here reaches threshold (~−55 mV), an action potential fires. If not, nothing happens.

The computation: take analog inputs — thousands of weighted EPSPs and IPSPs — sum them continuously, compare to a threshold, produce a discrete output. Inputs analog. Output digital. The action potential is the output.

<!-- → [CHART: V_m vs. time showing subthreshold summation of EPSPs and IPSPs at the soma, with threshold line marked — student should see how multiple small inputs build toward or fail to reach the trigger] -->

---

## The action potential — positive feedback to completion

The axon hillock reaches −55 mV. Voltage-gated sodium channels begin to open.

These are not the leak channels of the resting potential. They are gated by voltage: closed at −70 mV, increasingly likely to open as V_m rises. Around −55 mV, enough open that sodium begins flooding in faster than potassium can flow out. The inward sodium current depolarizes the membrane further. More channels open. More sodium in. V_m rises faster. More channels open.

This is positive feedback. Once it starts, it runs to completion. The membrane rockets from threshold toward the sodium equilibrium potential E_Na (+60 mV), but it never gets there.

Why not? Because voltage-gated sodium channels have three states, not two. **Closed** at rest. **Open** on depolarization. **Inactivated** within about a millisecond of opening — a ball-and-chain segment on the cytoplasmic face of the channel swings up and plugs the pore from the inside. In the inactivated state, the channel cannot conduct, no matter how depolarized the membrane is. It cannot return to the openable closed state until V_m repolarizes back below roughly −65 mV and the inactivation gate reopens.

So as the AP climbs, the sodium channels that started it begin shutting themselves off — not by reversing the way they opened, but by inactivating, which is a deeper kind of off. The inward sodium current peaks and falls. The membrane peaks around +30 mV, far short of E_Na.

Meanwhile, **voltage-gated potassium channels** have been opening — the same depolarization that opened the sodium channels also opens the potassium channels, but with a delay of about a millisecond. By the time the membrane is near its peak, these channels are fully open. Potassium rushes out: driven by the concentration gradient (more inside than outside) and by the now-positive interior pushing positive ions out. V_m falls. This is **repolarization**.

The K⁺ channels are slow to close. V_m overshoots the resting potential on the way down, briefly reaching around −80 mV. This **after-hyperpolarization** is the fingerprint of the delayed K⁺ current still running after the sodium current has ended. The K⁺ channels finally close. The pump restores the gradients in the background, as always. V_m drifts back to −70 mV.

The whole event — depolarization, peak, repolarization, undershoot, return — takes two to three milliseconds.

<!-- → [CHART: V_m vs. time for a single action potential, labeled with: threshold, peak, repolarization, after-hyperpolarization, absolute refractory period (shaded), relative refractory period (lighter shading), return to resting potential] -->

Now the most important property: the AP shape is fixed. A weak suprathreshold stimulus produces the same waveform as a strong one — same peak, same duration, same undershoot. **The action potential is all-or-nothing.** This means stimulus strength cannot be encoded in AP amplitude; amplitude is fixed. Stimulus strength is encoded in **firing frequency** — a weak input produces a few APs per second, a strong one produces hundreds.

One more piece. After the AP, there is a window during which the neuron cannot fire again. The **absolute refractory period** — while the Na⁺ channels are inactivated — lasts roughly a millisecond. No stimulus, no matter how strong, can fire a new AP during this window. The **relative refractory period** follows, when some channels have recovered but the K⁺ channels are still open and the membrane is hyperpolarized; a new AP requires a larger-than-usual depolarization to reach threshold.

The refractory period does two things: it enforces directionality (the membrane behind the traveling wave is refractory, so the wave can only move forward into fresh membrane), and it caps the maximum firing frequency at a few hundred hertz.

---

## Conduction — why the sheath is the fast lane

The AP fires at the axon hillock. It has to travel to the terminal, possibly a meter away.

In an unmyelinated axon, the AP propagates by regenerating at every patch of membrane. Na⁺ influx at one location depolarizes the neighboring patch through the cytoplasm. That patch's voltage-gated Na⁺ channels open. The cycle repeats. Velocity depends on diameter — fatter axons have lower cytoplasmic resistance and conduct faster — but typical unmyelinated mammalian axons conduct at 0.5 to 2 m/s. Slow.

In a myelinated axon, the myelin sheath is electrically insulating. The AP *cannot* regenerate in the wrapped segments — the voltage-gated channels are not there, and current cannot cross the insulated membrane. Instead, the depolarization at one node of Ranvier spreads *passively* through the cytoplasm under the myelin to the next node, where voltage-gated channels are concentrated and the signal regenerates. Then to the next. And the next.

This is **saltatory conduction** — from the Latin *saltus*, to leap. The signal is not actually jumping; the *regeneration* of the signal is jumping. Passive spread through cytoplasm is fast. Active regeneration at each node of Ranvier is the slow step. By skipping the regeneration to just the nodes, the signal travels far faster than it could by regenerating continuously. A large myelinated axon conducts at roughly 100 m/s — two orders of magnitude faster than the unmyelinated equivalent.

The apparent paradox: faster conduction despite *less* membrane available for ion flux, because the active regeneration step — the slow part — has been reduced to discrete nodes. The myelin pays a metabolic and developmental price (each Schwann cell or oligodendrocyte is an entire support cell devoted to wrapping a segment of axon), and the nervous system pays it only where speed matters. Motor commands, proprioception, fast touch: heavily myelinated. Slow pain, autonomic signals: unmyelinated or thin.

Now the MS patient makes sense. The immune system has destroyed oligodendrocyte myelin in patches. The axons underneath are intact. But the affected segments now have to attempt continuous propagation across membrane that lacks the voltage-gated channel density required for reliable regeneration. Conduction velocity drops from 100 m/s to perhaps 5 m/s or less. Some signals get through late. Some fail entirely. Where the plaques are is what determines the symptoms — the same lesion type, different location, different deficit.

<!-- → [INFOGRAPHIC: Side-by-side comparison of continuous (unmyelinated) vs. saltatory (myelinated) conduction — showing AP regenerating at every point vs. jumping between nodes, with conduction velocity labeled for each] -->

---

## The synapse — electrical becomes chemical

The AP reaches the axon terminal. The terminal does not touch the next cell. Between the presynaptic terminal and the postsynaptic membrane is a gap — the **synaptic cleft** — about 20 nanometers wide. The electrical signal cannot cross it directly.

The terminal contains hundreds of **synaptic vesicles**, each packed with thousands of neurotransmitter molecules, clustered near the **active zone** of the terminal membrane.

The arriving AP depolarizes the terminal. Voltage-gated **calcium channels** open. Ca²⁺ floods in — intracellular calcium is normally kept at nearly zero, roughly ten thousand times lower than extracellular. The incoming Ca²⁺ binds to SNARE proteins on the vesicle membrane. The vesicle zippers to the terminal membrane and fuses. Neurotransmitter is released into the cleft. Milliseconds from AP arrival to release.

The neurotransmitter diffuses across the cleft and binds receptors on the postsynaptic membrane. **Ionotropic receptors** are themselves ion channels — binding opens the channel directly. **Metabotropic receptors** activate intracellular signaling cascades that eventually open or close channels indirectly. The result is a graded postsynaptic potential: EPSP if cations enter (depolarizing), IPSP if anions enter or cations leave (hyperpolarizing).

Termination: **reuptake** by transporters on the presynaptic terminal or nearby glia; **enzymatic degradation** in the cleft; **diffusion** away. Without termination, the signal would persist indefinitely.

The major neurotransmitters and their primary roles: **acetylcholine (ACh)** at the neuromuscular junction and in the parasympathetic system; **norepinephrine (NE)** from sympathetic postganglionic neurons; **dopamine** in pathways linking brain stem to basal ganglia, limbic regions, and prefrontal cortex — its loss in the substantia nigra produces Parkinson's disease; **serotonin** from the raphe nuclei, influencing mood, sleep, appetite; **GABA**, the brain's main inhibitory neurotransmitter; **glutamate**, the brain's main excitatory neurotransmitter. Between them, GABA and glutamate handle the bulk of fast synaptic communication.

A concrete demonstration of what the synapse is for. Certain snake venoms contain α-bungarotoxins that bind nearly irreversibly to the acetylcholine receptor at the neuromuscular junction. The motor neurons are firing. ACh is being released. The cleft is full of the transmitter. But the receptor is blocked. The muscle receives no signal. The diaphragm stops. The patient dies of respiratory failure within hours unless ventilated. The same venom also shows why "neurotransmitter is excitatory or inhibitory" is not quite right — the effect depends on the *receptor*, not the transmitter. ACh excites the neuromuscular junction via nicotinic receptors, but inhibits the heart's pacemaker cells via muscarinic receptors that open K⁺ channels and hyperpolarize the tissue. Same molecule, opposite effect, because the postsynaptic machinery is different.

---

## The central nervous system — one tube, folded

All of the above — resting potential, AP, synapse — is happening in roughly 86 billion neurons [verify — Azevedo et al., 2009]. They are not scattered randomly. The organization follows directly from how the embryo built the system.

Three weeks after fertilization, a groove forms on the back surface of the embryo. The edges fold upward, curl toward each other, fuse. The result is the **neural tube** — the entire central nervous system before it is anything else. The front end of the tube swells and divides into regions. The long straight back portion becomes the spinal cord. The connected hollow center of the tube persists as the ventricles and central canal, filled with cerebrospinal fluid. Every named brain structure is a differentiated region of this one tube.

The front end resolves into four major regions. The **cerebrum** — about 80% of adult brain mass — is where conscious operations happen. Its surface, the **cerebral cortex**, is folded into ridges (**gyri**) and grooves (**sulci**) because the surface area required to house the required number of neurons far exceeds what the skull could accommodate flat. The cortex is divided into four lobes per hemisphere: **frontal** (motor planning, executive function, language production in most people's left hemisphere), **parietal** (touch, proprioception, body spatial sense), **temporal** (hearing, language comprehension, memory formation via the hippocampus deep within it), **occipital** (vision). Deep beneath the cortex, the **basal ganglia** gate movement — running a "go" pathway that facilitates intended movement and a "no-go" pathway that suppresses unwanted movement, using dopaminergic input from the brain stem. The **limbic system** handles emotion, motivation, and memory formation.

The **diencephalon** sits at the center. Its **thalamus** is the relay station for nearly all sensory information on its way to cortex — vision, hearing, touch, taste, proprioception all pass through specific thalamic nuclei before reaching the appropriate cortical region. Smell is the exception, projecting directly to cortex. The **hypothalamus**, size of a pea, controls feeding, drinking, body temperature, hormonal output through the pituitary, and most of the autonomic nervous system. It is the homeostatic center of the brain.

The **brain stem** — midbrain, pons, medulla — is roughly 3% of brain mass but carries every ascending sensory and descending motor pathway between brain and body, runs the nuclei for ten of twelve cranial nerves, and contains the circuits that control breathing, heart rate, blood pressure, and the sleep-wake cycle. Destroy the brain stem and nothing else survives, because the autonomic functions it runs are not optional.

The **cerebellum** sits behind the brain stem, contains roughly half the neurons in the entire brain (they are very small and densely packed), and does one thing: comparison and correction. The motor cortex sends a copy of its movement command to the cerebellum. The cerebellum simultaneously receives sensory feedback about what the body is actually doing. It computes the discrepancy and sends a correction back through the thalamus to the motor cortex. It does not originate movement and does not contain the final pathway to muscle. It is the error-correction loop running in parallel. Cerebellar damage produces **ataxia** — movements are present, sometimes forceful, but uncoordinated: reach for a glass and overshoot, try to walk and stagger. This is also what alcohol does at moderate doses, which is why coordination tests work better than strength tests as field sobriety measures.

<!-- → [INFOGRAPHIC: Sagittal section of the brain with the four major divisions labeled — cerebrum, diencephalon, brain stem (midbrain/pons/medulla), cerebellum — with one key function listed for each] -->

The **spinal cord** extends from the base of the skull to about L1–L2, where it ends as the conus medullaris. Below that, nerve roots continue downward as the **cauda equina** before exiting through their respective vertebral foramina — which is why a lumbar puncture below L2 is safe; there is no cord to injure, only free-floating roots.

A cross-section shows two zones. Central **gray matter** (neuronal cell bodies) is H-shaped: the posterior arms (**dorsal horns**) receive sensory input, the anterior arms (**ventral horns**) contain the motor neurons whose axons exit to innervate skeletal muscle. In thoracic and upper lumbar segments a **lateral horn** contains sympathetic preganglionic neurons. Surrounding the H is **white matter** — myelinated axons in organized tracts running up (sensory) and down (motor) the cord.

The cord also runs **reflex arcs** that bypass the brain entirely. The knee-jerk reflex: patellar tendon struck → quadriceps muscle stretched → spindle afferents fire → axons enter dorsal root and synapse directly on motor neurons in the ventral horn → motor neurons fire → quadriceps contracts → leg kicks. Sensor, one synapse, motor neuron, effector. No brain involved. The brain receives the information afterward. The reflex runs because waiting for the round-trip to the brain would cost fifty to a hundred milliseconds, and the cord can run the correction in a fraction of that.

---

## Protection — meninges, CSF, and the blood-brain barrier

The CNS sits inside bone, but bone is not enough. Three meningeal layers wrap it: the **dura mater** (thick fibrous outer layer lining the skull and vertebral canal), the **arachnoid mater** (thin web-like middle layer), and the **pia mater** (pressed against every gyrus and sulcus of the brain surface). The **subarachnoid space** between arachnoid and pia is filled with cerebrospinal fluid.

CSF is produced by the **choroid plexus** lining the ventricles, circulates through the ventricular system and subarachnoid space, and is reabsorbed into venous blood. Volume roughly 150 mL, turned over several times daily. [verify] It cushions the brain mechanically and maintains the chemical environment around the neural tissue.

The **blood-brain barrier** is separate: a property of the brain's capillaries themselves. The endothelial cells lining cerebral capillaries are joined by tight junctions that block free diffusion between blood and brain. Specific transporters mediate entry of glucose and necessary amino acids. Most drugs, most pathogens, most molecules circulating in blood — excluded. This protects neurons from the chemical variability of blood and from circulating toxins. The cost: getting a therapeutic drug into the brain is hard, which is why bacterial meningitis is treated with antibiotics chosen specifically for CNS penetration. The BBB has intentional gaps — the area postrema in the medulla samples blood directly to trigger vomiting in response to circulating toxins. The exceptions are functional, not accidental.

---

## The peripheral nervous system — nerves in, nerves out

Everything outside brain and spinal cord is the **peripheral nervous system**: bundles of axons wrapped in connective tissue, running signals between CNS and body.

Twelve pairs of **cranial nerves** emerge from the brain, mostly from the brain stem. The clinically essential ones: CN II (**optic**, vision), CN III/IV/VI (**oculomotor, trochlear, abducens**, eye movement), CN V (**trigeminal**, facial sensation and jaw muscles), CN VII (**facial**, facial expression and anterior taste), CN VIII (**vestibulocochlear**, hearing and balance), CN X (**vagus**, parasympathetic control of heart, lungs, and most abdominal viscera plus visceral sensory return), CN XII (**hypoglossal**, tongue movement). The vagus is worth dwelling on: it runs from the hindbrain, through the thorax, into the abdomen, supplying parasympathetic innervation to the heart and gut and carrying sensory information from the viscera back to the brain. It is the major pathway by which the state of the gut is communicated upward — one biological substrate of what gets called "gut feelings."

Thirty-one pairs of **spinal nerves** emerge from the cord. Each forms from two roots: the **dorsal root** carries sensory axons from the periphery into the dorsal horn (cell bodies in the dorsal root ganglion), and the **ventral root** carries motor axons from the ventral horn out to muscle. The two roots merge just lateral to the cord.

Most spinal nerves pass through a **plexus** — a network that mixes axons from different spinal levels into the named peripheral nerves. The brachial plexus (C4–T1) becomes the radial, median, and ulnar nerves of the arm. The lumbosacral plexus (L1–S4) becomes the femoral and sciatic nerves of the leg.

Two maps follow: a **dermatome** is the band of skin innervated by sensory axons of a single spinal nerve (C4 to shoulder, T4 to chest at nipple level, L1 to groin, S1 to heel). A **myotome** is the set of muscles innervated by motor axons from a single nerve root. Sensory loss in a dermatomal pattern localizes a lesion to that nerve root. Weakness in a myotome localizes it the same way. These maps are how clinicians read lesion location from clinical presentation — the same principle as the MS patient, played out at the spinal rather than the cranial level.

The organizing split: **afferent** axons carry signals toward the CNS (sensory). **Efferent** axons carry signals away from the CNS (motor and autonomic). Dorsal roots are afferent. Ventral roots are efferent. Chapter 7 traces what the efferent side does in detail: how a motor command becomes a muscle contraction, and how the autonomic system runs the viscera.

---

## Exercises

<!-- → [TABLE: Ion concentration and equilibrium potential reference table — rows: Na⁺, K⁺, Cl⁻, Ca²⁺ — columns: intracellular concentration, extracellular concentration, equilibrium potential, direction of flow when channel opens at rest — to be placed at the start of exercises as a working reference] -->

**Warm-up 1.** A neuron's resting membrane potential is −70 mV. A drug is applied that selectively blocks all K⁺ leak channels while leaving the Na⁺/K⁺ pump running. Predict: (a) which direction V_m will shift in the seconds after the drug is added, and why; (b) what happens to the threshold for firing an action potential relative to the new resting potential; (c) whether the neuron becomes more or less excitable. Trace each prediction back to the ion movements that cause it. *Tests: understanding how K⁺ permeability sets the resting potential and how resting potential shift affects excitability.*

**Warm-up 2.** Trace the ionic events of a single action potential by filling in this sequence: at threshold, \_\_\_\_ channels open and \_\_\_\_ flows \_\_\_\_ (in/out), driving V_m toward \_\_\_\_ mV. Within ~1 ms those channels \_\_\_\_ (state), ending the inward current. Meanwhile, delayed \_\_\_\_ channels have opened, driving \_\_\_\_ \_\_\_\_ (in/out) and pulling V_m back down. The resulting undershoot to ~−80 mV is called the \_\_\_\_. Return the completed sequence in prose, not blanks. *Tests: ability to narrate the AP as a sequence of channel states and ion movements.*

**Warm-up 3.** A patient presents with muscle weakness. Blood work shows hypokalemia (low extracellular K⁺). Without using the words "the cell is less excitable," explain in mechanistic terms — from E_K through resting potential through threshold distance — why low extracellular potassium makes excitable cells harder to fire. Then predict what hyperkalemia does to the same chain and explain why severe hyperkalemia can cause cardiac arrest. *Tests: applying the weighted-average resting potential model to a clinical perturbation.*

**Application 1.** A small unmyelinated axon (1 μm diameter) conducts at about 1 m/s. A large myelinated axon (20 μm outer diameter) conducts at about 100 m/s. The myelinated axon has *less* membrane in contact with the extracellular fluid per unit length than the unmyelinated axon. Explain the apparent paradox: how does restricting ion flux to a small fraction of the axon length make the signal travel *faster*? Your answer must identify which step in conduction is fast and which is slow, and explain what role the node of Ranvier plays. *Tests: saltatory conduction logic — passive spread vs. active regeneration.*

**Application 2.** The five-step chain of synaptic transmission is: AP arrives at terminal → Ca²⁺ enters → vesicle fuses → neurotransmitter binds receptor → postsynaptic ion channel opens. For each step, name the specific protein or structure responsible and predict what happens to synaptic transmission if that step is blocked. (Example: blocking voltage-gated Ca²⁺ channels at the terminal → no vesicle fusion → no transmitter released → no postsynaptic potential.) Complete the same analysis for the remaining four steps. *Tests: mechanistic understanding of each link in the transmission chain.*

**Application 3.** Acetylcholine is excitatory at the neuromuscular junction (nicotinic receptors open Na⁺ channels) and inhibitory at the heart's sinoatrial node (muscarinic receptors open K⁺ channels). Using only what you know about how ion flow produces EPSPs vs. IPSPs, explain why the same molecule produces opposite effects in the two locations. Then generalize: what determines whether a neurotransmitter is excitatory or inhibitory at a given synapse? *Tests: the receptor-determines-effect principle; not confusing transmitter identity with transmitter effect.*

**Synthesis 1.** A patient with multiple sclerosis has a new spinal cord plaque at the T6 level of the dorsal columns (ascending sensory tract). Predict: (a) what sensory modalities will be affected and in what body regions; (b) whether motor function will be affected by this specific plaque, and why or why not; (c) how the clinical presentation of this lesion differs from a lesion at the same level in the ventral horn. Use the anatomical organization of the spinal cord gray and white matter to justify each prediction. *Tests: integrating spinal cord anatomy with conduction failure to generate a clinical prediction.*

**Synthesis 2.** Compare the action potential and the graded postsynaptic potential on five dimensions: amplitude range, distance of propagation, decay with distance, summation, and all-or-nothing vs. graded. Then answer this design question: why does the nervous system use both signal types rather than just one? What would fail if action potentials were graded, and what would fail if postsynaptic potentials were all-or-nothing? *Tests: understanding the complementary roles of two signal types and the design logic that requires both.*

**Challenge.** A genetic mutation removes the inactivation gate from all voltage-gated Na⁺ channels. The channels can still open in response to depolarization, but instead of entering the inactivated state, they return directly to the closed-but-openable state when V_m repolarizes. Predict the consequences for each of the following, and for each prediction explain the mechanism by which the missing inactivation gate produces the change: (a) the shape of the action potential waveform; (b) the absolute refractory period; (c) the directionality of AP propagation along the axon; (d) the maximum firing frequency; (e) whether the neuron could generate a sustained tetanic depolarization or would reset normally between APs. *Tests: precise causal reasoning from Na⁺ channel states through AP properties — the inactivation gate as a structural basis for refractory period, directionality, and frequency ceiling.*

---

## LLM Exercise — Build `06-action-potential.html`

Build an interactive action potential simulator using the Show / Say / Constrain / Verify pattern. Target: a single-page HTML file that simulates the Hodgkin-Huxley action potential and lets you change parameters in real time.

### Show

Point the LLM at this chapter and specify the file name and purpose:

```
I am a student in an anatomy and physiology course. I want to build a
single-file HTML tool called 06-action-potential.html that simulates a
Hodgkin-Huxley action potential interactively. The file should run by
being opened directly in a browser, no build step. Read the chapter I
have attached for the physiological details.
```

### Say

```
Build 06-action-potential.html with:

1. A real-time plot of membrane potential (V_m, y-axis from −90 mV
   to +50 mV) vs. time (x-axis, 0 to 20 ms).

2. Three controls:
   - Stimulus strength slider (0 to ~1.5× threshold). Below threshold:
     small subthreshold depolarization only. At or above threshold:
     a full stereotyped AP fires.
   - Myelination toggle (unmyelinated / myelinated) that changes the
     displayed conduction velocity.
   - Axon diameter slider (1 to 20 μm) that also affects conduction
     velocity.

3. Below the plot:
   - Na⁺ channel state indicator: closed / open / inactivated, updating
     in real time during the AP.
   - K⁺ channel state indicator: closed / open.
   - Arrows showing direction and magnitude of Na⁺ and K⁺ currents at
     the current moment.
   - Computed conduction velocity (m/s) based on diameter and myelination.
   - Shaded regions marking absolute refractory period (darker) and
     relative refractory period (lighter) on the V_m graph.
   - Side-by-side mini-graphs comparing AP propagation along an
     unmyelinated vs. myelinated axon as a moving wave.

Plain HTML, CSS, vanilla JavaScript. Canvas or SVG for plotting.
No external libraries. Single self-contained file.
```

### Constrain

```
Constraints:
- All-or-nothing behavior is mandatory. Stimulus below threshold must
  produce only a small subthreshold deflection. Stimulus at or above
  threshold must produce the same AP shape regardless of how far above
  threshold the stimulus is. The AP must not get taller with stronger
  stimuli.
- The Na⁺ channel must explicitly display three states (closed, open,
  inactivated), not two.
- Conduction velocity scale must be approximately correct: unmyelinated
  ~0.5 × diameter (μm) m/s; myelinated ~5 × diameter m/s. A 20 μm
  myelinated axon should show roughly 100 m/s.
- The AP waveform must show the after-hyperpolarization (undershoot below
  resting potential during the delayed K⁺ current phase).
- Refractory periods must be enforced: the simulation cannot fire a
  second AP while Na⁺ channels are inactivated, no matter the stimulus.
```

### Verify

Once the file runs:

1. **All-or-nothing test.** Move the stimulus slider from zero upward. Below threshold: small deflection, return to rest, no AP. At threshold: full AP fires. Increasing the slider further must not make the AP taller. If it does, the simulation is wrong — report the specific failure.

2. **Refractory test.** Set stimulus high enough for rapid AP firing. The frequency should saturate at a few hundred Hz; the simulation cannot fire arbitrarily fast. If it does, the refractory period is not being enforced.

3. **Myelination test.** Toggle myelination at a fixed diameter. Conduction velocity should jump by roughly 10×. Less than 5× or more than 50× — ask for recalibration.

4. **Channel state test.** Watch the state indicators through one full AP: Na⁺ should go closed → open (during depolarization) → inactivated (near peak and early repolarization) → closed (during hyperpolarization recovery). K⁺ should go closed → open (repolarization) → closed (return to rest). If the sequence is wrong, report the specific mismatch.

### Extension — toward Chapter 7

Once the simulator works, add a neuromuscular junction module: when an AP reaches the terminal, release a packet of ACh into a small cleft and produce a graded depolarization in a simulated muscle fiber membrane. If the muscle fiber depolarization reaches its threshold, fire a muscle action potential. This makes visible the chain — nerve AP → chemical signal → muscle AP — that Chapter 7 follows all the way through to contraction.

---

Chapter 7 takes the structure we have built and asks what it does. The motor side: how does a motor command become muscle contraction? The autonomic side: how does the sympathetic and parasympathetic system regulate the viscera? The sensory side: how is information from the body encoded and routed back upward? Structure is in place. Chapter 7 is the machinery in motion.

---

**What would change my mind.** If fast neural signaling in vertebrates turned out to depend on mechanisms other than voltage-gated ion channels — if the Hodgkin-Huxley framework turned out to be a poor approximation for most mammalian axonal conduction at behaviorally relevant scales — I would revise everything in this chapter. The framework has held for seventy years and has been refined continuously by careful channel-level measurement. The refinements have always been additive — more channel types, richer kinetics — not replacements of the basic mechanism.

**Still puzzling.** How does the nervous system encode meaning in a signal whose alphabet has only one letter — the stereotyped AP — distinguishing every distinct downstream effect purely by which axon carries the signal and which target it reaches? The "address is the message" framing is correct but is not, by itself, an explanation of how meaning is built. And how does the brain coordinate the electrochemical activity of 86 billion cells into the kind of integrated, continuous experience of a single moment of awareness? This chapter reaches the bottom of the stack. The top is still genuinely open.

---

**Tags:** nervous-system, action-potential, hodgkin-huxley, neuroanatomy, multiple-sclerosis
