# Chapter 15 — Three Angles on Nervous Tissue: Wiring, Signaling, and Conversation
*The Signal That Cannot Be Made Louder — Only Repeated.*

In the 1950s, a researcher slid a thin electrode into a single axon — not from a human, not from a mouse, but from a squid. The giant squid *Loligo* has an axon nearly a millimeter in diameter, visible to the naked eye, which is why it became the instrument that unlocked one of biology's deepest puzzles. The researcher watched the voltage across the axon membrane shift from roughly negative seventy millivolts to positive thirty millivolts in under two milliseconds, then slam back down. He stimulated it again. Same thing. Same peak, same timing, same return. He stimulated harder. Same thing.

That last result is the important one. Stimulate a neuron harder and you do not get a bigger signal. You get the same signal, or nothing at all.

This is so unlike almost everything else in physics and engineering that it stopped people cold. A microphone produces a bigger electrical signal when you shout into it. A pressure sensor deflects more when you press harder. But the neuron — the fundamental signaling unit of every nervous system on Earth — does not work this way. It fires fully or it does not fire. The size of the stimulus, beyond a threshold, is irrelevant. What matters is whether the threshold is crossed.

Alan Hodgkin and Andrew Huxley worked out the mechanism from squid axon data in 1952, built a mathematical model of the ion currents involved, and won the Nobel Prize for it. Their model explained not just the all-or-nothing character of the signal but why it propagates at all, how it travels one direction and not the other, and why some axons carry signals two hundred times faster than others. The model has held up for seventy years. What it describes is the subject of this chapter.

---

## The Shape of a Neuron Is Its Function

Before the electrical mechanism can make sense, the geometry has to make sense.

<!-- → [IMAGE: labeled diagram of a multipolar neuron — show soma (cell body) with nucleus, multiple branching dendrites extending from soma, single axon emerging from axon hillock, myelin sheath in segments along axon with nodes of Ranvier labeled at gaps, axon terminal with synaptic vesicles; arrows showing direction of signal flow from dendrites → soma → axon → terminal; student should see the one-directional architecture before encountering the electrical mechanism] -->

A neuron is a cell with a problem: it needs to receive information at one end, process it in the middle, and send a signal out the other end. The solution is a body plan found nowhere else in biology. From the cell body — the soma, which contains the nucleus and most of the metabolic machinery — multiple branches extend outward. Most of these are dendrites, from the Greek word for tree, and they are named well: they branch and rebranch into a structure that can intercept signals arriving from dozens or hundreds of neighboring cells. One branch, and only one, extends in a different direction from the soma. This is the axon. It does not branch at its origin. It runs, sometimes for extraordinary distances, to whatever target the neuron is built to reach.

A sensory neuron with its soma near the base of your spine has an axon that extends down the entire length of your leg. That is a single cell more than a meter long, thinner than anything visible to the naked eye, running continuous from cell body to the skin of your foot.

The asymmetry is the point. Dendrites are the input end. The soma is where integration happens — where the cell adds up all the signals arriving from all the dendrites simultaneously. The axon is the output end. If the sum of inputs at the soma reaches a critical voltage — a threshold, located precisely at the base of the axon where it emerges from the cell body — an action potential begins. That signal then travels down the axon to its terminal, where it triggers the release of chemicals into the gap between this neuron and the next.

This creates directed flow. Information can only move one way: dendrites in, axon out. The architecture enforces it.

The length of the axon creates a problem. Electrical signals dissipate as they travel. A voltage change in a simple wire fades with distance. An axon a meter long, without some solution to this problem, would attenuate its signal to nothing before it reached the end.

The solution is the action potential itself: a signal that is actively regenerated along the entire length of the axon, not passively conducted. But even active regeneration takes time, and time spent regenerating is time the signal is not moving. For a body that needs to coordinate muscles and sensors separated by a meter, the speed matters.

Enter myelin. Glial cells — oligodendrocytes in the brain and spinal cord, Schwann cells in the peripheral nerves — wrap around segments of axons in thick layers of lipid-rich membrane. This wrapping is not continuous. It is segmented, with gaps left exposed at regular intervals called nodes of Ranvier. The insulated segments are called internodes.

On a naked, unmyelinated axon, the action potential must be regenerated at every patch of membrane along the length. On a myelinated axon, the insulating sheath prevents the voltage change from leaking out through the membrane between nodes. The voltage change instead spreads electrically through the interior of the axon — fast, passive, like a wire — until it reaches the next exposed node, where the action potential is regenerated and jumps forward to the next.

<!-- → [IMAGE: comparison diagram of unmyelinated vs. myelinated axon — left: unmyelinated axon showing action potential regenerating continuously at every membrane patch, labeled "0.5 m/s"; right: myelinated axon with Schwann cells/oligodendrocytes wrapped around internodes, nodes of Ranvier labeled, action potential jumping node to node, labeled "100 m/s"; student should see saltatory conduction as spatial skipping enabled by insulation, and appreciate the 200× speed difference] -->

This is saltatory conduction, from the Latin for leap. The action potential does not travel continuously; it skips from node to node. The difference in speed is not marginal. An unmyelinated axon conducts at roughly half a meter per second. A large, fully myelinated axon conducts at a hundred meters per second. Two hundred times faster. The signals controlling your voluntary movements travel at a hundred meters per second. The signals controlling your digestion travel at a fraction of that. The nervous system has decided that speed is worth the metabolic cost of maintaining all those glial cells, but only where speed matters enough.

---

## The Mechanism That Hodgkin and Huxley Found

Now to the mechanism. What actually happens when a neuron fires?

The membrane of a resting neuron is not at electrical equilibrium. It is held in a state of tension. On the outside of the membrane, sodium ions are abundant. On the inside, potassium ions are abundant. The Na⁺/K⁺ ATPase — a pump embedded in the membrane — maintains these gradients by continuously moving three sodium ions out for every two potassium ions it pulls in, powered by ATP. More positive charges pumped out than pulled in means the inside of the cell accumulates a slight negative charge. The resting potential is approximately negative seventy millivolts.

This is not a passive state. It costs energy to maintain, and it is the stored potential that makes signaling possible.

The membrane is also studded with voltage-gated ion channels — protein structures that open and close in response to the voltage across the membrane. Two types matter most: fast sodium channels and slower potassium channels.

Here is what happens when a stimulus depolarizes the membrane enough to reach threshold — approximately negative fifty-five millivolts:

The voltage-gated sodium channels snap open. Sodium ions, driven by both their concentration gradient (more outside than inside) and by the electrical gradient (the inside is negative), rush into the cell. The inside of the membrane becomes less negative, then briefly positive — reaching about positive thirty millivolts. This is the peak of the action potential.

At this point, the sodium channels inactivate. They close in a way that is different from their resting-closed state: they are now locked shut, unresponsive to voltage, for a period of milliseconds. They cannot be reopened, no matter how strong the stimulus. This is the absolute refractory period — a window during which another action potential is physically impossible.

Meanwhile, the voltage-gated potassium channels, which respond to the same voltage change that opened the sodium channels but more slowly, are now fully open. Potassium ions, abundant inside the cell, flow outward. The inside becomes negative again. The membrane repolarizes. In fact, it briefly overshoots the resting potential — hyperpolarizes — before the potassium channels close and the Na⁺/K⁺ pump restores the gradients.

The whole event takes one to two milliseconds.

<!-- → [CHART: action potential waveform — x-axis: time in milliseconds (0–5 ms); y-axis: membrane voltage (−70 mV to +30 mV); label: resting potential (−70 mV), threshold (−55 mV), rising phase with annotation "Na⁺ channels open / Na⁺ rushes in", peak (+30 mV), falling phase with annotation "Na⁺ channels inactivate / K⁺ channels open / K⁺ rushes out", undershoot (hyperpolarization) with annotation "K⁺ channels close", return to resting; bracket showing absolute refractory period during Na⁺ inactivation; student should connect each phase of the waveform to the specific channel events causing it] -->

Now here is the propagation. The sodium influx at one location depolarizes the neighboring patch of membrane. That patch's voltage-gated sodium channels open. Sodium rushes in there too. That patch depolarizes the next patch. The wave moves down the axon.

But behind the wave, the sodium channels are inactivated — in their locked-shut refractory state. The wave cannot move backward into already-fired membrane. It can only move forward, into membrane that is still at rest. The refractory period is not a flaw. It is what makes the action potential directional.

The all-or-nothing character follows from the same mechanism. If a stimulus depolarizes the membrane to threshold, sodium channels open, sodium rushes in, the membrane depolarizes further, more sodium channels open. This is a positive feedback loop. Once it begins, it runs to completion — always to the same peak voltage, always following the same time course. If the stimulus does not reach threshold, the positive feedback never starts. The membrane returns to resting. There is no middle state.

---

## Electricity Becomes Chemistry: The Synapse

The action potential reaches the axon terminal. What happens there?

The terminal does not physically touch the next cell. It is separated from the receiving membrane by a gap of about twenty nanometers — the synaptic cleft. Twenty nanometers is less than the wavelength of visible light, so this gap is not something you can see, but it is a true physical separation, not a connection. Across this gap, an electrical signal cannot simply continue. The communication must become chemical.

<!-- → [IMAGE: cross-section diagram of a chemical synapse — show presynaptic terminal with mitochondria, synaptic vesicles clustered near active zone, voltage-gated Ca²⁺ channels at membrane; synaptic cleft labeled (20 nm); postsynaptic membrane with ligand-gated ion channels (receptors); arrows showing: action potential arrives → Ca²⁺ enters → vesicles fuse (exocytosis) → neurotransmitter released into cleft → diffuses to receptors → ion channels open → postsynaptic potential; student should trace the complete electrical-to-chemical-to-electrical conversion] -->

The terminal is packed with synaptic vesicles — tiny pouches filled with neurotransmitter molecules. When the action potential arrives, it opens voltage-gated calcium channels in the terminal membrane. Calcium ions flow in. Calcium is the trigger. It activates proteins called SNAREs, which zipper the vesicle membrane to the terminal membrane and force the contents of the vesicle into the synaptic cleft. This is exocytosis, and it happens within a hundred microseconds of the calcium influx.

The neurotransmitter molecules diffuse across the cleft and bind to receptor proteins on the postsynaptic membrane — the membrane of the receiving cell. Some of these receptors are ion channels themselves: when the neurotransmitter binds, they open. Others trigger second-messenger cascades that open channels indirectly.

If the channel that opens allows sodium in, the postsynaptic membrane depolarizes slightly. This is an excitatory postsynaptic potential, or EPSP — a small nudge toward firing. If the channel that opens allows chloride in or potassium out, the membrane hyperpolarizes slightly. This is an inhibitory postsynaptic potential, or IPSP — a small push away from firing.

The critical word is small. A single EPSP is typically about half a millivolt. The threshold for firing is fifteen millivolts above resting. One synapse cannot make a neuron fire. This is by design.

A typical neuron in the brain receives input from thousands of synapses simultaneously. Some are excitatory; some are inhibitory. The soma continuously adds up all of these small voltage changes, accounting for where on the dendrite each one arrived (synapses near the soma have more influence than synapses at the dendritic tips), and how recently each one occurred (voltage changes fade over time, so signals that arrive close together in time add their effects more fully than signals that arrive far apart).

If the sum at any moment exceeds threshold at the axon hillock — the trigger zone — an action potential fires. If not, silence.

This is the fundamental computation of the nervous system. Not a binary switch but a continuous weighted sum, converted to a binary output — fire or not fire — thousands of times per second. The neuron is integrating information from hundreds of sources and making a decision.

---

## Why Inhibition Is Not Optional

It is tempting to think of inhibitory synapses as a brake — something that slows the system down when needed. This misses how central inhibition is to every computation the nervous system performs.

Consider the motor neuron that controls a muscle in your forearm. At any moment, this neuron is receiving signals from the brain telling it to contract the muscle, and simultaneously receiving signals from the spinal cord telling it not to. The balance of these signals — excitatory drive from the brain versus inhibitory restraint from interneurons — determines whether the muscle contracts and how strongly.

Without inhibition, motor neurons fire uncontrollably. This is exactly what happens in tetanus. The bacterium *Clostridium tetani* produces a toxin — a protease — that cuts the SNARE proteins at inhibitory synapses in the spinal cord. GABA and glycine, the primary inhibitory neurotransmitters of the spinal cord, can no longer be released. The brake is gone. Motor neurons fire without restraint. Muscles lock in rigid, uncoordinated spasm. The jaw cannot open. The back arches. The patient cannot breathe.

Tetanus kills not because neurons fire too weakly, but because they cannot stop firing. The inhibitory synapses were doing essential work at every moment, and their absence is immediately catastrophic.

---

## How Synapses Change: The Cellular Basis of Memory

The architecture described so far — action potentials traveling down axons, neurotransmitters crossing synaptic clefts, postsynaptic potentials summing in somas — is the mechanism of moment-to-moment signaling. But the nervous system also learns. The same cellular machinery supports both.

The key is that synapses are not fixed in strength. A synapse that has been recently active can become stronger or weaker depending on the circumstances of its recent use.

The best-understood form of synaptic strengthening is long-term potentiation, or LTP. At glutamate synapses — the primary excitatory synapses of the brain — a particular receptor called the NMDA receptor has an unusual property. It can only open if two conditions are satisfied simultaneously: the presynaptic neuron must release glutamate, and the postsynaptic membrane must already be depolarized. In other words, the NMDA receptor is a coincidence detector. It reports that two events happened at the same time.

When both conditions are met, the NMDA receptor allows calcium into the postsynaptic cell. That calcium triggers a cascade that inserts more glutamate receptors into the postsynaptic membrane. The synapse is now stronger. The next time the presynaptic neuron fires, it will have a larger effect on the postsynaptic neuron than it did before.

The logic is this: if a synapse was active while the postsynaptic neuron was firing, that synapse probably contributed to the decision to fire. Strengthen it. If a synapse fires while the postsynaptic neuron is quiet, it did not contribute. Weaken it. This is Hebb's rule — neurons that fire together wire together — implemented in calcium chemistry.

<!-- → [INFOGRAPHIC: LTP mechanism — two panels side by side; left panel (before LTP): presynaptic neuron releases glutamate, NMDA receptors on postsynaptic membrane blocked by Mg²⁺ (postsynaptic not depolarized), only AMPA receptors open, small EPSP results; right panel (during/after LTP): presynaptic fires while postsynaptic is already depolarized, Mg²⁺ block removed from NMDA receptor, Ca²⁺ enters via NMDA, Ca²⁺ triggers insertion of additional AMPA receptors into postsynaptic membrane, same presynaptic firing now produces larger EPSP; student should see the coincidence-detection logic: NMDA opens only when both neurons are active simultaneously] -->

The consequence is that the pattern of activity in a neural circuit is self-reinforcing. Pathways that are used become easier to use. Pathways that are not used become harder to use. What we experience as memory and learning is, at the cellular level, the gradual reshaping of synaptic weights across billions of neurons.

---

## The Three Mechanisms Together

The architecture, the action potential, and synaptic transmission are not three separate features of nervous tissue. They are one integrated system.

The dendrites' job is to collect. They present a large surface area to the local environment, intercepting signals from hundreds of neighbors. The soma's job is to integrate. It holds all the incoming postsynaptic potentials simultaneously, weighing them by their strength and timing. The axon hillock's job is to decide. At every moment, it compares the summed input to threshold. If the threshold is crossed, the axon fires.

The action potential's job is to transmit. It carries the decision — fire or not fire — down the axon at speeds that allow the body to coordinate across its full length. Myelin extends that speed where it is needed most. The refractory period ensures the signal moves in one direction and does not interfere with itself.

The synapse's job is to translate. Electrical signal becomes chemical release. Chemical release becomes electrical signal in the next cell. This translation is where the computation continues: the synapse is not just a relay but a site of integration, modulation, and modification. Synaptic weights change with use. History is encoded in which synapses are strong and which are weak.

Put all of this together and you have the machinery that underlies everything the nervous system does: every sensation, every movement, every thought, every memory. The Hodgkin-Huxley model, derived from a squid in a tank in Cambridge in 1952, describes the foundation. The squid axon was chosen for its size, not its sophistication. But the mechanism it revealed turns out to be universal — conserved across virtually every nervous system on Earth, from the simplest worm to the human brain that wrote this sentence.

That is what makes it worth understanding precisely. Not as a catalog of parts but as a mechanism — a machine whose behavior follows necessarily from the properties of its components. Once you see how the voltage-gated channels produce the all-or-nothing signal, how the refractory period enforces directionality, how calcium links electrical arrival to chemical release, how coincidence detection at the NMDA receptor implements synaptic learning — once you see all of this clearly — the rest of neuroscience becomes a matter of understanding how these mechanisms are organized, combined, and scaled.

---

## Exercises

**Warm-up**

1. A neuron receives a stimulus that depolarizes its membrane from −70 mV to −60 mV. No action potential fires. The stimulus is then doubled in strength, depolarizing the membrane to −50 mV. This time the neuron fires. Explain why doubling the stimulus produced a qualitatively different outcome, not merely a larger version of the same outcome. What property of the voltage-gated sodium channels accounts for this? *(Tests: threshold, all-or-nothing character, positive feedback)*

2. Explain why the action potential can only travel from the soma toward the axon terminal, not in reverse. Your answer should refer to a specific property of the sodium channels immediately after they open. *(Tests: refractory period, directional propagation)*

3. A patient is diagnosed with multiple sclerosis, a disease in which the immune system destroys myelin around axons in the central nervous system. Predict two consequences for nerve signal transmission — one involving speed and one involving reliability — and explain the mechanism behind each prediction. *(Tests: saltatory conduction, role of myelin in signal integrity)*

**Application**

4. A neuron in the brain receives 80 excitatory synaptic inputs simultaneously, each producing an EPSP of 0.5 mV, and 40 inhibitory inputs simultaneously, each producing an IPSP of 0.5 mV. The neuron's firing threshold is 15 mV above resting. Show whether the neuron fires. Then explain why a single strong excitatory synapse producing a 15 mV EPSP on its own would be an unreliable design for the nervous system, even though it would technically reach threshold. *(Tests: spatial summation, integration logic, robustness of distributed computation)*

5. The tetanus toxin cuts SNARE proteins specifically at inhibitory synapses in the spinal cord, leaving excitatory synapses intact. A different hypothetical toxin cuts SNARE proteins only at excitatory synapses. Predict the symptoms of poisoning by this second toxin. How would they differ from tetanus? Explain the mechanism behind each. *(Tests: inhibitory vs. excitatory balance, SNARE-mediated exocytosis, consequences of disrupting each side of synaptic balance)*

6. Local anesthetic drugs (such as lidocaine) block voltage-gated sodium channels in peripheral axons, preventing them from opening. Explain why this eliminates pain sensation while still allowing the patient to feel pressure and temperature in some cases, given that different axon types have different diameters and myelination. *(Tests: voltage-gated sodium channels, axon diameter and myelination, differential sensitivity)*

**Synthesis**

7. A neuroscientist stimulates a presynaptic neuron repeatedly while simultaneously holding the postsynaptic neuron at a depolarized voltage. After this pairing protocol, she finds that the same presynaptic stimulus now produces a larger EPSP in the postsynaptic neuron than it did before. She then applies a drug that blocks NMDA receptors before repeating the pairing protocol in a second neuron pair, and finds no potentiation. Explain both results — the potentiation and its blockade — tracing the complete mechanism from the pairing protocol through to the increased EPSP. What does this experiment demonstrate about the role of coincidence detection in synaptic plasticity? *(Tests: LTP mechanism, NMDA receptor as coincidence detector, calcium cascade, AMPA receptor insertion)*

8. Compare the design logic of the all-or-nothing action potential with the graded postsynaptic potential. Why does the nervous system use both? What problem would arise if action potentials were graded (larger stimulus → larger signal)? What problem would arise if postsynaptic potentials were all-or-nothing? *(Tests: integrative reasoning about signal encoding, why two different signal modes are necessary)*

**Challenge**

9. A mutation eliminates the inactivation gate of voltage-gated sodium channels — the channels can still open in response to depolarization, but they cannot enter the inactivated (locked-shut) state. They simply return directly to the resting-closed state when repolarization occurs. Predict the consequences for: (a) the action potential waveform; (b) the refractory period; (c) the direction of action potential propagation along the axon; and (d) the maximum firing frequency of the neuron. For each, explain the mechanism by which the missing inactivation gate produces the predicted change. *(Tests: deep mechanistic understanding of Na⁺ channel states, refractory period, directionality, frequency coding)*

---

*Byline: Nik Bear Brown*
