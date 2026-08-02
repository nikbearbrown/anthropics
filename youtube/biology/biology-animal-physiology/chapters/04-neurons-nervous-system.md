# Chapter 4 — Neurons and the Nervous System


## TL;DR

- Two physiologists in 1949 stuck electrodes inside a piece of squid, and what they found tells you everything about how a nervous system is built.
- The chapter moves through What a neuron actually is, The resting potential — disequilibrium on purpose, Graded potentials — the analog layer, The action potential — the discharge, ion by ion, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Two physiologists in 1949 stuck electrodes inside a piece of squid, and what they found tells you everything about how a nervous system is built.*

---

On a dock in Plymouth, England, in the summer of 1949, Alan Hodgkin and Andrew Huxley were threading a glass capillary down the inside of a single axon plucked from the mantle of a European common squid. That sounds modest until you put a number on it: the axon was about a millimeter thick — roughly a thousand times wider than a typical mammalian motor axon. You can see it without a microscope. That is why the action potential was first understood in a squid and not in you.

Why does a squid have an axon thick enough to see?

The squid uses it to escape predators. When a fish lunges, the squid triggers a synchronous contraction of the entire mantle musculature, jetting water out and rocketing the animal backward. For the contraction to be synchronous along the whole mantle, the motor command has to reach the head end and the tail end at the same time. The signal has to be fast. And the squid's solution — found independently in earthworms, crayfish, and cuttlefish — was to make the axon enormous.

A wider axon conducts faster, because the inside is a wider tube of cytoplasm and presents less resistance to longitudinal current flow. This is Ohm's law applied to a salt-water pipe. Make the pipe fatter, current spreads farther before leaking out through the membrane, the next region depolarizes sooner, the signal propagates more quickly. The squid giant axon conducts at roughly 25 meters per second [verify — values in the range 18–25 m/s are reported for *Loligo*].

Vertebrates do not have giant axons. A motor axon running from your spinal cord to your big toe is about 20 micrometers across — fifty times thinner than the squid's. And yet it conducts at about 120 meters per second, nearly five times *faster* than the squid axon. How?

That is the story of myelin. And the two solutions — giant unmyelinated axons in cephalopods, thin myelinated axons in vertebrates — are an evolutionary parallel: two distantly related lineages, faced with the same physical problem, arriving at two completely different cellular answers.

What I want to show in this chapter is how the same underlying machinery — ions moving across a membrane through gated channels — gives rise to both solutions, and then zoom out to ask how nervous systems built from this machinery come to be organized across the animal kingdom. We will start at the cell and end at the body plan.

---

## What a neuron actually is

The first thing to clear up: a neuron is not a wire.

A wire conducts electricity by letting electrons drift through metal. A neuron is mostly water and salt — no metal. What it has instead is a thin lipid membrane separating two compartments of salty fluid with carefully different compositions. The inside of a neuron is rich in potassium and poor in sodium. The outside is rich in sodium and poor in potassium. That difference — set up by an ATP-burning pump, maintained continuously — is the entire source of the signal. The neuron's signal is not electrons moving. It is ions briefly redistributing across a membrane.

A typical neuron has three named regions. The **cell body** (soma) contains the nucleus and the protein-making machinery. The **dendrites** are branched, tree-like extensions of the soma — the receiving end. A single cortical neuron in a mammal may carry thousands of dendritic branches, each receiving signals from a different upstream cell. The **axon** is the sending end — exactly one per neuron, running sometimes very far, splitting at its terminals into synaptic junctions with target cells. A sensory neuron in your back can have an axon over a meter long, anatomically continuous from spinal cord to toe.

Wrapped around many vertebrate axons, in segments, is a thick fatty layer called **myelin** — made not by the neuron itself, but by support cells called **glia**. In the peripheral nervous system, the myelinating glia are **Schwann cells**. In the central nervous system, they are **oligodendrocytes**, each sending arms to wrap several different axons simultaneously. Between each myelinated segment is a small bare patch of axon membrane: the **node of Ranvier**. These nodes are where the signal regenerates itself. The squid axon is one continuous bare tube. Its solution to speed is geometric. The vertebrate's solution is insulative. Hold both.

---

## The resting potential — disequilibrium on purpose

Stick a glass microelectrode into a resting neuron and you measure roughly **−70 millivolts** across the membrane — the inside seventy millivolts more negative than the outside. This is the **resting membrane potential**, and it is not zero, not equilibrium, not a passive state. The neuron is sitting at a steady electrical tension the way a drawn bow sits at a steady mechanical tension.

Two mechanisms hold the tension.

First, the **Na⁺/K⁺ ATPase**, a transmembrane pump that burns one ATP per cycle and moves three Na⁺ out of the cell for every two K⁺ it pulls in. The pump runs continuously in every neuron of every animal with a nervous system. It concentrates sodium outside (extracellular Na⁺ ends up about ten times higher than intracellular) and potassium inside (intracellular K⁺ ends up about thirty times higher than extracellular). Because three positive charges leave for every two that enter, it also leaves the inside slightly negative.

Second, the **K⁺ leak channels** — potassium-selective channels that are always open. Since the pump has concentrated K⁺ inside, K⁺ flows out down its concentration gradient, carrying positive charge with it. The inside grows more negative. But the more negative it gets, the more electrically the negative interior attracts the positive K⁺ back. There is a voltage at which the chemical force pushing K⁺ out and the electrical force pulling K⁺ in exactly balance. That voltage is the **equilibrium potential for potassium**, E_K, computable from the Nernst equation:

$$E_{ion} = \frac{RT}{zF} \cdot \ln\frac{[ion]_{out}}{[ion]_{in}}$$

For potassium at body temperature (310 K), with [K⁺]_out ≈ 5 mM and [K⁺]_in ≈ 140 mM:

$$E_K = \frac{8.314 \times 310}{96\,485} \cdot \ln\frac{5}{140} \approx 0.0267 \cdot (-3.33) \approx -89 \text{ mV}$$

If the membrane were permeable only to K⁺, the resting potential would sit at −89 mV. The actual RMP is around −70 mV — not quite at E_K. The membrane has a small permeability to Na⁺ as well, and Na⁺'s equilibrium potential is about +60 mV. The actual V_m is a weighted compromise between E_K and E_Na, with the weights set by relative permeabilities. At rest, K⁺ permeability dominates roughly thirty-to-one, so V_m sits close to E_K but pulled slightly toward zero.

This is not free. Roughly twenty percent of your whole-body resting energy budget goes to running brain Na⁺/K⁺ pumps, despite the brain being only about two percent of body mass [verify — Mink, Blumenschine & Adams (1981) is the canonical comparative source]. The resting potential is stored potential energy, paid for in ATP continuously.

Two words you need to feel: if V_m moves toward zero (less negative), the cell is **depolarized**. If it moves further from zero (more negative), it is **hyperpolarized**. Those two words do constant work in what follows.

![Resting membrane potential ](images/04-neurons-nervous-system-fig-01.png)
*Figure 4.1 — Resting membrane potential *

---

## Graded potentials — the analog layer

Before the action potential, there is something smaller and more continuous.

When a neurotransmitter arrives at a dendrite and opens a receptor channel, ions flow briefly through that channel and produce a small change in V_m — often less than a millivolt to a few millivolts. These are **graded potentials**: they are local (largest at the synapse, spreading passively outward and shrinking as they travel) and decremental.

An **excitatory postsynaptic potential (EPSP)** is a small depolarization — a nudge upward toward firing threshold. EPSPs are typically caused by neurotransmitters that open channels permeable to Na⁺, letting positive charge in. An **inhibitory postsynaptic potential (IPSP)** is a small hyperpolarization — a nudge downward, away from threshold. IPSPs are typically caused by neurotransmitters that open Cl⁻ channels (letting negative charge in) or K⁺ channels (letting positive charge out).

A single EPSP is far too small to make a neuron fire — typically about 0.5 mV, when firing threshold sits about 15 mV above rest. A cortical neuron has thousands of synapses; some fire as EPSPs, some as IPSPs; the cell body adds them up, a process called **summation**. Simultaneous EPSPs from different synapses add across space (**spatial summation**); rapid successive EPSPs from one synapse pile up in time (**temporal summation**).

The summed potential travels passively toward the **axon hillock** — the small region where the cell body meets the axon, and the site with the highest density of voltage-gated sodium channels in the cell. If V_m at the hillock reaches threshold (around −55 mV), the action potential fires. If not, silence.

The neuron's computation, in one sentence: thousands of weighted inputs, summed in continuous voltage, compared against a threshold, producing a discrete output. Analog in, digital out.

---

## The action potential — the discharge, ion by ion

V_m at the axon hillock has just crossed −55 mV. The voltage-gated sodium channels open.

These are different proteins from the always-open leak channels. A voltage-gated channel has a domain that physically responds to membrane voltage — when V_m crosses a threshold, the protein changes shape and the channel opens. Voltage-gated Na⁺ channels are present at high density at the hillock and at every node of Ranvier. When V_m crosses −55 mV, they pop open in a wave.

Sodium, concentrated ten times more outside than inside and electrically attracted to the negative interior, rushes in. Positive charge arrives. V_m climbs. As V_m climbs, more voltage-gated Na⁺ channels detect the depolarization and open. As more open, more sodium rushes in, and V_m climbs faster. This is a **positive feedback loop**: depolarization opens channels, open channels cause more depolarization. Once threshold is crossed, the loop runs away. V_m shoots from −55 mV to about +40 mV in roughly a millisecond.

This is the depolarization phase.

Why doesn't V_m stay at +40 mV? Because voltage-gated Na⁺ channels have three states, not two — and this is the cleverest thing in the whole story.

- **Closed.** At resting potential. Voltage too low to open.
- **Open.** When V_m crosses threshold, the channel's activation gate swings open. Sodium flows.
- **Inactivated.** About a millisecond after opening, a separate inactivation gate (a different domain of the same protein) swings shut, plugging the channel from the inside. The channel cannot conduct, even though V_m is still high.

After inactivation, the channel cannot reopen until V_m drops back down — the inactivation gate cannot be re-cocked until the membrane repolarizes.

So at the peak of the action potential, voltage-gated Na⁺ channels inactivate en masse. Sodium influx falls off. Simultaneously, a slower set of channels — **voltage-gated K⁺ channels** — has been opening. They respond to the same depolarization that opened the Na⁺ channels, but they open with a delay, peaking around when Na⁺ channels are inactivating. With Na⁺ channels closing and K⁺ channels opening, the flux reverses. K⁺, concentrated inside and electrically repelled by the now-positive interior, pours out. V_m falls.

This is repolarization.

V_m drops past resting potential and briefly undershoots to about −85 mV — the **afterhyperpolarization** — because the voltage-gated K⁺ channels are slow to close. Eventually they close, the Na⁺/K⁺ pump restores the small ion imbalance, and the membrane is ready to fire again.

The whole sequence — depolarization, peak, repolarization, afterhyperpolarization, return — takes about 2 to 5 milliseconds.

It is **all-or-nothing**: either threshold is crossed and the full cycle fires at its full amplitude, or nothing fires. A barely-suprathreshold stimulus produces the same spike as a wildly-suprathreshold one. How then does the nervous system distinguish a gentle touch from a painful pressure? By **frequency**. A strong stimulus makes the neuron fire many spikes per second; a weak stimulus makes it fire few. Information is encoded in firing rate, not spike size.

The inactivation gate has a second consequence: the **refractory period**. While Na⁺ channels are inactivated, no new action potential can fire regardless of stimulus strength — the **absolute refractory period**, about 1–2 ms. After that, while the membrane is still hyperpolarized and channels are still recovering, firing is possible but harder — the **relative refractory period**. The refractory period also ensures one-directional propagation: the patch of membrane that just fired is refractory, so the depolarizing wave spreading sideways cannot trigger a backward spike. The signal moves forward and only forward.

This was worked out in detail by Hodgkin and Huxley between 1939 and 1952, using voltage-clamp recordings on the squid giant axon. They built a quantitative mathematical model — the Hodgkin-Huxley equations — that reproduced the action potential's shape, threshold, and propagation velocity from the kinetics of just two channel types. The model is so accurate you can still run it today and get curves that match recordings from living axons. Hodgkin, Huxley, and John Eccles shared the 1963 Nobel Prize in Physiology or Medicine for the work.

![Action potential voltage vs](images/04-neurons-nervous-system-fig-02.png)
*Figure 4.2 — Action potential voltage vs*

---

## Two ways to make conduction fast

The action potential at one point on the axon does not stay there. It propagates. When one patch of membrane depolarizes, positive charge inside the axon spreads sideways to the next patch — passive cable conduction. The next patch depolarizes, fires its own action potential, and the cycle repeats one segment over.

The action potential is not a wave of ions traveling down the axon. The ions move locally, in and out across each segment of membrane. What travels is the *event* — a regenerating chain of local discharges, each one re-igniting the next. Think of dominoes falling. The dominoes do not move horizontally; the *pattern of falling* moves. Each domino tips locally; what propagates is the event.

How fast the chain propagates depends on two physical variables: axon diameter (wider means lower internal resistance, current spreads farther per cycle) and membrane resistance (higher resistance means current leaks less, spreads farther still). These are the two knobs evolution has available.

**The squid's strategy: giant axons.** The squid giant axon is roughly 1 mm across — about 1000 times wider than a typical mammalian motor axon. The width drops internal resistance enough to give about 25 m/s, even with no myelin. The cost: energy and space. A giant axon has enormous surface area, which means enormous numbers of Na⁺/K⁺ pumps running continuously to maintain the resting potential. It also takes up massive physical volume. The squid can afford one such axon per side of its mantle, dedicated to the escape jet. It cannot afford a million.

**The vertebrate strategy: myelin.** Each Schwann cell (in the PNS) or oligodendrocyte (in the CNS) wraps a segment of axon in fifty to a hundred concentric layers of fatty membrane. The myelinated segment is essentially impermeable to current. Between wrapped segments sit the nodes of Ranvier — short bare patches of membrane packed with voltage-gated Na⁺ channels at extraordinary density. The action potential fires only at the nodes. Between nodes, the depolarization spreads passively inside the axon — fast, because the myelin keeps the current confined — until it reaches the next node and re-fires.

This is **saltatory conduction**, from Latin *saltare*, to leap. The action potential appears to leap from node to node. A 20-μm-diameter myelinated mammalian axon conducts at about 120 m/s — five times faster than the squid giant axon, at one fiftieth the diameter. The same axon, demyelinated, would conduct at about 2 m/s; saltatory conduction is roughly a sixtyfold speedup over continuous conduction.

The vertebrate strategy is also vastly more economical. A myelinated axon exposes almost no membrane to extracellular fluid — only the node regions need pumps. And a million 20-μm axons take up roughly the same space as one 1-mm squid axon. Vertebrate nervous systems can carry many parallel signals through a compact bundle.

**Multiple sclerosis** is an autoimmune disease in which the immune system attacks CNS myelin. As myelin degrades, saltatory conduction fails — signals slow or block. Symptoms depend on which axons are demyelinated: optic neuritis if the optic nerve is hit; weakness if motor tracts; numbness if sensory tracts. The disease is one mechanism in many disguises.

---

## Worked example — three axons, one meter

Make the trade-off concrete.

**Squid giant axon.** Unmyelinated, ~1 mm diameter, ~25 m/s at 18°C.
Time to cross 1 m: 1 / 25 = **40 ms**.

**Frog sciatic nerve (large myelinated motor axon).** ~15 μm diameter, ~30 m/s.
Time to cross 1 m: 1 / 30 ≈ **33 ms**.

**Mammalian Aα motor axon.** ~20 μm diameter, myelinated, ~120 m/s.
Time to cross 1 m: 1 / 120 ≈ **8 ms**.

The mammal beats the squid by a factor of five, at one fiftieth the cross-section. Where does the squid pay the bill?

**Energy.** The metabolic cost of maintaining RMP scales with membrane surface area, because every square micrometer of bare membrane needs Na⁺/K⁺ pumps to offset ion leak. Surface area of a cylinder is 2π · r · L. For the same length L:

Squid axon, r = 500 μm: surface area ≈ 3,140·L μm²
Mammalian axon, r = 10 μm: surface area ≈ 63·L μm²

The squid axon has about **50 times more exposed membrane per unit length**. Worse, almost all of the mammalian axon's membrane is covered by myelin — only the short nodes are bare. The functional pump load on the myelinated axon is roughly another order of magnitude lower than the bare-surface ratio suggests. The squid's energy cost to carry one signal over one meter may be roughly 100 times the mammal's.

**Space.** One thousand 20-μm myelinated axons have a total cross-sectional area of roughly π · (10)² · 1000 ≈ 314,000 μm² — comparable to one squid axon (π · (500)² ≈ 785,000 μm²). One squid axon occupies the space of a thousand mammalian ones. That sets a hard ceiling on how many independent fast signals an invertebrate nervous system can carry in parallel.

Two lessons. Myelination is one of the major innovations in animal evolution — it allowed compact, fast-conducting nervous systems and made small body sizes neurally feasible. Without it, a creature the size of a mouse could not pack enough fast axons to coordinate its body. The second lesson: myelin is not the only answer. Cnidarians — jellyfish, sea anemones — have no myelin, no giant axons, and they do fine. Their behavioral repertoire (slow rhythmic contractions, tentacle stings) does not demand fast directional signaling. Thin, slow, unmyelinated fibers in a nerve net do exactly what those animals need. The "best" axon design is whatever matches the animal's behavioral demands.

![Comparison of squid giant axon vs](images/04-neurons-nervous-system-fig-03.png)
*Figure 4.3 — Comparison of squid giant axon vs*

---

## Crossing the gap — the synapse

The action potential reaches the end of the axon. There is a gap — the **synaptic cleft**, about 20 nanometers wide. Electrical current does not jump it effectively. Instead, the presynaptic neuron releases a chemical messenger — a **neurotransmitter** — which diffuses across the gap and binds to a receptor on the postsynaptic membrane.

The mechanism in five steps.

1. Action potential arrives at the axon terminal. The depolarization opens **voltage-gated Ca²⁺ channels** in the terminal membrane.
2. Ca²⁺ flows in. Calcium is concentrated about ten-thousand-fold outside the cell, and the inside is electrically attractive; even a brief channel opening lets calcium pour in.
3. Ca²⁺ triggers vesicle fusion. Inside the terminal are **synaptic vesicles** — small membrane-bound sacs each packed with thousands of neurotransmitter molecules. Calcium binds a sensor protein on the vesicle (synaptotagmin), causing the vesicle to fuse with the terminal membrane and dump its contents into the cleft. This takes microseconds.
4. Neurotransmitter diffuses across the cleft and binds postsynaptic receptors.
5. Receptor binding opens or modulates ion channels on the postsynaptic side, producing an EPSP or IPSP.

Two receptor flavors. **Ionotropic receptors** are themselves ion channels — binding neurotransmitter opens the channel directly. Fast (milliseconds), sharp EPSPs and IPSPs. **Metabotropic receptors** are not channels; they trigger an intracellular signaling cascade (G-protein, second messenger) that eventually modulates channels. Slow (tens of milliseconds to seconds), diffuse and longer-lasting.

A short tour of the neurotransmitters that matter most:

**Glutamate** — the dominant excitatory neurotransmitter in the vertebrate brain. Ionotropic glutamate receptors (AMPA, NMDA) open Na⁺-permeable channels and produce fast EPSPs. Most cortical synapses use glutamate.

**GABA** — the dominant inhibitory neurotransmitter in the vertebrate brain. GABA-A receptors open Cl⁻-permeable channels, hyperpolarizing the postsynaptic cell. Benzodiazepines (Valium, Xanax) are GABA-A agonists — they enhance GABA's inhibitory effect, producing sedation.

**Acetylcholine (ACh)** — the neurotransmitter at the vertebrate neuromuscular junction, where motor neurons command skeletal muscle, and throughout much of the brain. Acts on ionotropic nicotinic receptors (fast, at the NMJ) and metabotropic muscarinic receptors (slower, in brain and autonomic ganglia).

**Dopamine, serotonin, norepinephrine** — modulatory neurotransmitters acting mainly through metabotropic receptors, involved in reward, mood, arousal, and attention.

After transmission, the neurotransmitter must be cleared from the cleft or the postsynaptic cell will not reset. Three mechanisms: **diffusion** out of the cleft; **enzymatic degradation** (acetylcholinesterase hydrolyzes ACh in milliseconds — nerve agents like sarin work by irreversibly blocking this enzyme, so ACh accumulates, muscles fire uncontrollably, and the diaphragm stops); **reuptake** by transporter proteins in the presynaptic membrane (fluoxetine/Prozac blocks the serotonin reuptake transporter, so serotonin stays in the cleft longer; cocaine blocks dopamine reuptake, flooding reward circuits).

The chemical synapse converts a digital input (a spike arriving) back into an analog output (a graded postsynaptic potential). The whole nervous system runs on this analog-to-digital-to-analog conversion at every synapse.

![Chemical synapse mechanism ](images/04-neurons-nervous-system-fig-04.png)
*Figure 4.4 — Chemical synapse mechanism *

---

## From nerve net to brain — a comparative tour

Now zoom out. We have built a neuron, made it fire, made it talk to the next cell. How do animals arrange large numbers of these cells into a nervous *system*?

The animal kingdom shows a clear comparative progression — not a ladder of progress, but a series of architectural solutions, each matched to body plan and behavioral demands.

**Nerve net — Cnidaria.** Jellyfish, hydra, sea anemones, corals. Neurons form a diffuse mesh through the body wall, with no central organizing structure. Stimulate one part of the net, excitation spreads outward in all directions, intensity falling off with distance. No "front" or "behind" to a jellyfish; coordination is radial, not directional. Behavior is essentially body-wide rhythmic contractions, tentacle stings, and slow orientations — all of which a nerve net handles fine. No brain, because no behavior requires one. The body plan is radially symmetric, and so is the nervous system.

**Bilateral nerve cord with ganglia — Bilateria.** Once an animal has a front and back end, the front encounters the world first, and clusters of neurons accumulate there. We call those clusters **ganglia**. The front-end ganglion specialized for sensory processing is the beginning of a brain. The rest of the cord runs the length of the body, often with segmental ganglia at intervals.

The bilaterian theme plays out differently across groups. Flatworms have two parallel longitudinal nerve cords connected by transverse cross-bridges — a ladder-like pattern — plus a pair of cerebral ganglia at the head. Annelids (earthworms) have a **ventral nerve cord** with a ganglion in each body segment, plus head ganglia connected to the cord by a ring around the esophagus. Each segmental ganglion controls its own segment; the head ganglia integrate sensory information and bias the cord's activity. Arthropods (insects, crustaceans) have a ventral cord with substantial fusion: in insects several thoracic ganglia fuse into a single mass controlling walking and flight; the head ganglia fuse into a compact brain capable of learning and navigation.

**Dorsal hollow nerve cord — Chordata.** Vertebrates flip the layout. The nerve cord runs along the *back* (dorsal) and is *hollow* — it surrounds a fluid-filled central canal. This is one of the four defining traits of the phylum Chordata. During development, the front end of the dorsal hollow nerve cord swells into vesicles that become the brain. The rest stays the spinal cord, running through the bony spine.

**Encephalization.** The trend across many independent lineages — vertebrates, cephalopods, social insects — is the concentration of an increasing fraction of nervous tissue into a centralized brain. A common measure is the **encephalization quotient (EQ)**: the ratio of an animal's actual brain size to the brain size predicted for an animal of its body mass. Humans have an EQ around 7; dolphins around 4–5; chimpanzees around 2.5; cattle below 1 [verify — Jerison (1973) is the classical source]. EQ correlates roughly with behavioral flexibility but the correlation is loose. Corvids and parrots have small absolute brains but very high neuron *densities* in their forebrains, and behavioral capacities comparable to great apes. Cephalopods (octopuses, cuttlefish) have invertebrate nervous systems entirely independent of vertebrate evolution, showing problem-solving and tool use. Brains arose multiple times independently. Absolute size is only one of several variables that matter — neuron count, density, connectivity, and developmental plasticity all contribute.

![Comparative nervous-system architecture across five groups ](images/04-neurons-nervous-system-fig-05.png)
*Figure 4.5 — Comparative nervous-system architecture across five groups *

---

---

## Exercises

**Warm-up**

**1.** A neuron has [K⁺]_in = 140 mM and [K⁺]_out = 5 mM. Calculate E_K using the Nernst equation at body temperature (310 K). Then describe, without calculating, what happens to E_K if a patient's blood K⁺ rises to 8 mM (hyperkalemia). Does E_K become more or less negative? What does that predict about resting membrane potential and neuronal excitability? *(Tests: Nernst equation mechanics and ion gradient reasoning.)*

**2.** A student says: "The action potential is the same as electricity flowing through a wire." Correct this in two sentences. Be specific about what is actually moving in each case and where it moves. *(Tests: distinguishing electron drift from local ion flux across a membrane.)*

**3.** Order the following events from earliest to latest during a single action potential at the axon hillock: (a) voltage-gated K⁺ channels open; (b) V_m crosses −55 mV; (c) Na⁺ channels inactivate; (d) Na⁺ channels open; (e) V_m reaches +40 mV; (f) afterhyperpolarization occurs. *(Tests: sequence of channel states as a check on understanding the three-state model.)*

**Application**

**4.** Three drugs are being tested. Drug A blocks voltage-gated Na⁺ channels at low concentrations. Drug B blocks voltage-gated K⁺ channels. Drug C is a GABA-A receptor agonist that enhances GABA's effect. For each drug: predict the immediate effect on neuronal firing, explain the mechanism at the channel level, and name a clinical or pharmacological context in which a drug with this mechanism is actually used. *(Tests: applying channel physiology to predict drug effects, with real-world grounding.)*

**5.** Calculate and compare the exposed membrane surface area per centimeter for two axons: (a) squid giant axon, radius 500 μm, unmyelinated; (b) mammalian Aα motor axon, radius 10 μm, with myelin covering 99% of its surface (only the nodes are exposed). Compute the bare-membrane surface area for each, compute the ratio, and explain what this ratio says about the relative metabolic cost of maintaining resting potential for the two designs. *(Tests: geometric reasoning linking surface area to pump load to energy budget.)*

**6.** Cnidarians have nerve nets but no brains, and they function successfully for hundreds of millions of years. A student asks: why couldn't a vertebrate just use a much larger, denser nerve net instead of a centralized brain? Answer in three to five sentences. Your answer should engage the behavioral repertoire each architecture supports and the specific limits of decentralized signaling for directional, fast, integrated responses. *(Tests: connecting nervous system architecture to behavioral capacity.)*

**Synthesis**

**7.** A graduate student in Plymouth in 1949 wants to record from a single mammalian motor axon the way Hodgkin and Huxley recorded from the squid giant axon. List two specific technical reasons this is much harder than the squid experiment, and explain how Hodgkin and Huxley's results — derived from squid — turned out to apply to mammalian neurons anyway. What does this teach you about the conservation of cellular mechanisms across animal phyla? *(Tests: comparative reasoning and how science generalizes from a model system.)*

**Challenge**

**8.** Multiple sclerosis attacks CNS myelin, and patients often show partial recovery from acute attacks before later relapsing. Using your understanding of saltatory conduction, propose two distinct cellular mechanisms that could underlie partial recovery — think about node spacing, channel redistribution, and partial remyelination. Then propose one experiment at the cellular level that would distinguish your two mechanisms. *(Tests: mechanistic reasoning under uncertainty and experimental design from first principles.)*

---

## What the chapter is really arguing

Two ideas run through everything here.

The first: the action potential is a controlled discharge of stored chemical disequilibrium, not electricity flowing through a wire. The Na⁺/K⁺ ATPase builds the tension; voltage-gated channels release it in a stereotyped all-or-nothing pulse; the pulse propagates by re-igniting the same sequence at each successive patch of membrane. Everything else — the resting potential, the threshold, the refractory period, the directionality of propagation — follows from the three-state behavior of the voltage-gated Na⁺ channel.

The second: the same cellular toolkit — Na⁺/K⁺ ATPase, leak channels, voltage-gated Na⁺ and K⁺ channels, chemical synapses — appears in every animal nervous system from a cnidarian nerve net to a mammalian cortex. What changes across animal lineages is not the toolkit. It is the *architecture*: how the neurons are arranged, how much is centralized, how fast the signals travel. The squid and the mammal both needed fast conduction; they arrived at opposite points on the speed-energy-space trade-off surface, using the same underlying ion physics. Hodgkin and Huxley studied the squid and described every animal with a nervous system.

---

## LLM exercise — building the action potential simulator

You are going to build a single-file HTML simulator called `04-action-potential.html` that lets the user vary stimulus strength, axon diameter, myelination, and temperature, and shows the resulting membrane voltage trace, channel states, and conduction velocity. The goal is to make the squid-versus-mammal trade-off visible by direct manipulation.

### Show

Open Claude Code (or your LLM tool of choice) in the directory where you keep this book's simulators. Show it the relevant sections of this chapter — paste in the action-potential and conduction sections, including the worked example with the three axons. Tell the model what you are trying to build, in one paragraph. Do not ask for code yet. Ask: *"Before you write any code, summarize back to me what the simulator needs to do, and list three design questions you would need answered before starting."* If the model's summary misses something, correct it. If its questions are good, answer them. This step is not optional; skipping it produces a wrong simulator faster.

### Say

Now give the spec:

```
Build a single-file HTML simulator at 04-action-potential.html.

Controls (sliders/toggles in a left panel):
- Stimulus strength: 0 to 50 mV depolarization from rest
- Myelination toggle: ON / OFF
- Axon diameter: 1 to 1000 μm (logarithmic slider)
- Temperature: 5°C to 37°C

Display (right panel):
- Live Vm vs. t graph (last 20 ms, autoscrolling)
- Ion channel state indicators: Na+ closed / open / inactivated; K+ closed / open
- Computed conduction velocity (m/s), updated whenever diameter, myelination,
  or temperature changes
- Side-by-side comparison: same axon unmyelinated vs. myelinated, conduction time
  for 1 meter
- Preset buttons: "Squid giant axon" (1000 μm, unmyelinated, 18°C)
  and "Mammalian motor axon" (20 μm, myelinated, 37°C)

Physics (simplified Hodgkin-Huxley):
- Use the standard HH equations with INa, IK, IL currents
- Threshold ~-55 mV; resting potential -70 mV
- Conduction velocity approximation:
  - Unmyelinated: v ∝ sqrt(diameter), tune so 1 mm axon at 18°C gives ~25 m/s
  - Myelinated: v ∝ diameter, tune so 20 μm at 37°C gives ~120 m/s
- Temperature: Q10 = 3 for channel kinetics

No external libraries other than vanilla HTML/CSS/JS and the canvas API.
All physics in commented code so I can read what you did.
```

### Constrain

```
Constraints:
- Do not invent constants. Where you need values you do not have,
  insert /* VERIFY: source needed */ as a code comment.
- Do not write a "full Hodgkin-Huxley simulation" that pretends to be 
  the original — write a simplified version with parameters tuned to give
  the qualitative shape and the two target velocities above.
- The conduction velocity computation must be a clearly labeled function 
  with a comment explaining the relationship to axon physics.
- The simulator must run with zero installation — just open the .html file.
```

### Verify

After the model produces the code, verify it by running it and asking these specific questions:

1. Set diameter to 1000 μm, unmyelinated, temperature 18°C. Does the velocity readout show ~25 m/s? If not, where in the code is velocity computed?
2. Set diameter to 20 μm, myelinated, temperature 37°C. Does the velocity readout show ~120 m/s?
3. Decrease the stimulus below threshold (try 5 mV). Does the membrane return to rest without spiking? Does the response demonstrate all-or-nothing behavior?
4. Drop temperature from 37°C to 10°C with other parameters fixed. Do channel kinetics slow down visibly? The action potential should broaden and conduction should drop.
5. Inspect the code. Find every constant the model wrote. For each, ask: *"Where does this number come from? Cite a source or mark it as a fitting parameter."* Anything unsourced becomes a `[verify]` flag.

### Exploration

Once the simulator works, try these comparisons:

- Match the squid giant axon's conduction time over 1 meter using a myelinated axon. What is the smallest diameter that gets you to 25 m/s? To 120 m/s?
- Set to 1 μm diameter, unmyelinated, 37°C. What is the conduction velocity? This is roughly the regime of cnidarian neurons. What kinds of behaviors are accessible, and what kinds are not?
- Hold diameter fixed at 20 μm and toggle myelination on and off. Plot conduction time over 1 meter as a function of temperature, 10°C to 37°C, for both. Which axon is more temperature-sensitive in absolute terms? In relative terms? This is a real biophysical question with implications for cold-adapted animals.

### Extension toward Chapter 5

The simulator treats a single axon in isolation. Chapter 5 is about how billions of neurons are organized into brains. Ask your LLM: *"How could I extend this simulator to a small network — say, 100 neurons in a 10×10 grid — with each neuron's axon feeding into the next? What would I need to add to the code? What behaviors at the network level — synchrony, oscillation, propagation patterns — would I expect to see that the single-axon version cannot show?"* Save the conversation. We will come back to it in the next chapter.

---

## What would change my mind

If careful comparative recordings showed that cephalopod giant axons rely on a previously unrecognized form of subcellular insulation — some glial wrapping or membrane specialization functionally equivalent to myelin — the clean "two strategies" framing of this chapter would need to soften into "many strategies, more continuous than discrete." The case currently rests on the absence of insulating glia in squid; if absence turns into "we hadn't looked carefully enough," the story changes.

## Still puzzling

Why myelin evolved when it did — apparently in early jawed vertebrates, hundreds of millions of years after action potentials had already stabilized — rather than far earlier, when faster conduction would have been useful to any active swimmer. The developmental and genetic prerequisites for wrapping a glial cell around an axon are not obviously demanding, and I find the long delay between the action potential and its insulator hard to account for from current evidence.

---

*Tags: neurons, action-potential, hodgkin-huxley, squid-giant-axon, comparative-physiology*
