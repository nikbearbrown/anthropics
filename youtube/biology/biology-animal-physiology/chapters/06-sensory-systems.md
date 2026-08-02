# Chapter 6 — Sensory Systems

## TL;DR

- A receptor protein, a voltage change, and a world that only that animal lives in.
- The chapter moves through The universal three-step machine, Mechanoreception — bending a channel open, Echolocation — what physics allows, Thermoreception — the TRP channels, and what a chili pepper proves, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*A receptor protein, a voltage change, and a world that only that animal lives in.*

---

Here is a fact worth sitting with. A male *Bombyx mori* moth, standing on a perch in the dark, extends feathery antennae into the air. Each antenna is studded with about 17,000 chemosensory hairs. Each hair contains two olfactory neurons whose dendrites press against pores in the cuticle. The whole arrangement is built to one specification: catch bombykol, the molecule a female releases from glands at the tip of her abdomen. Not other molecules. Not similar molecules. Bombykol.

A female releases bombykol at roughly $10^{11}$ molecules per second. Diffuse that through a kilometer of night air on a faint breeze and the male, at the far end of the plume, is sampling air in which bombykol is present at parts per quintillion. He flies upwind. He finds her.

Karl-Ernst Kaissling showed that a single olfactory neuron in that antenna will fire one extra action potential when a single bombykol molecule binds its receptor protein. One molecule. One additional spike. The moth has reached the floor that chemistry sets — you cannot detect anything more dilute than a single molecule, and the moth is there.

Hold that, and take a second fact. A mantis shrimp — *Odontodactylus scyllarus*, the carnival-colored stomatopod — looks at the world through compound eyes containing sixteen distinct photoreceptor types. Twelve are tuned to different wavelengths, from deep UV to far red. Four more detect the orientation of polarized light, including circularly polarized light that essentially no other animal detects. Sixteen channels, against your three.

And yet: when Hanne Thoen trained mantis shrimp to associate wavelengths with food and tested how finely they could distinguish adjacent wavelengths, they were *worse* than humans. Sixteen receptor types, worse discrimination than three. What they appear to be doing is a parallel pattern code — reading color as a fast classification rather than a ratio comparison — something fundamentally different from what a vertebrate brain does with color information.

These two animals are not experiencing a fuller or an impoverished version of the same world. They are living in *different* worlds — different inventories of what physical and chemical reality they can convert into neural signals. Jakob von Uexküll gave this idea a name in 1934: **Umwelt** — the sensed world, the specific slice of reality that a particular animal's receptor proteins can detect. The tick's Umwelt is butyric acid, warmth, and a hairy surface. The bat's Umwelt is echoes. The bee's Umwelt is ultraviolet patterns on flowers and the sky's polarization pattern. Yours is a particular band of electromagnetic wavelengths, a particular range of pressure waves in air, and a modest vocabulary of volatile molecules.

Everything in this chapter follows from that idea. A sensory system is a machine for carving one Umwelt out of physical reality. Let me show you how the machine works.

---

## The universal three-step machine

Every sensory system in every animal does the same three things, in the same order.

**Reception.** A specialized cell sits where the signal arrives. A fingertip mechanoreceptor sits in the dermis, near the surface. A retinal photoreceptor sits at the back of the eye, where focused light lands. An olfactory neuron sits in the nasal epithelium, where volatile molecules dissolve into mucus. Location is part of the design — a receptor in the wrong place receives no signal.

**Transduction.** The environmental signal — a photon, a pressure wave, a molecule, an electric field — is converted into a change in the receptor cell's membrane voltage. This change is the **receptor potential**: local, graded, decremental, the same kind of signal as an EPSP. *Which* ion channels open, and *how* the stimulus opens them, is what defines the modality. A mechanoreceptor opens channels by physically deforming the membrane. A photoreceptor closes channels through a molecular cascade launched by a photon. A chemoreceptor opens channels because a ligand binds a receptor protein and triggers a second messenger. The transduction step is *the* place of specialization — the place where this sensory system differs from every other sensory system.

**Encoding and transmission.** The receptor potential, if large enough, drives action potentials — either in the receptor cell itself or in a postsynaptic neuron. Those action potentials travel up a dedicated nerve to the brain. The brain interprets them by *which* fiber is firing (the labeled-line principle: auditory nerve fibers always register as sound, no matter what physically made them fire) and at *what rate* (intensity is encoded in firing frequency). Quality — red vs. green, sweet vs. salty — is encoded as which population of receptor types is active.

Two properties are universal across this architecture.

**Adaptation.** A receptor's response to a sustained stimulus falls off with time. A **tonic** receptor fires throughout the duration of a stimulus — your proprioceptors keep telling your brain where your elbow is right now, not just where it moved a moment ago. A **phasic** receptor fires only when the stimulus changes, then goes quiet — Pacinian corpuscles in your skin report the onset of pressure and then adapt out; you stop feeling your clothes roughly thirty seconds after putting them on. Tonic receptors waste spikes on information that hasn't changed; phasic receptors miss steady states but allocate their firing budget to events. Both designs are useful; most nervous systems carry a mix.

**Logarithmic compression.** Sensory stimuli span enormous dynamic ranges — the ratio between the faintest visible light and the brightest is about $10^{10}$; between the softest audible sound and the threshold of pain is $10^{12}$. No receptor can encode twelve orders of magnitude in a firing rate that tops out around a few hundred spikes per second. So sensory systems compress logarithmically: firing rate scales roughly with the *log* of stimulus intensity. This is why decibels, stellar magnitudes, and pH are all log scales — they match the logarithmic encoding of the nervous systems that evolved to detect sound, light, and acidity. You feel the ratio between stimuli, not their absolute difference.

That is the whole machine: reception, transduction, encoding, with adaptation and log compression built in. Now the modalities.

---

## Mechanoreception — bending a channel open

The oldest transduction is also the simplest. A mechanoreceptor has, embedded in its membrane, an ion channel whose gate is pulled open by physical force. Deform the membrane, deflect a structure tethered to the channel, and the channel opens. No second messengers. No molecular cascade. The force is the gate-opener.

The cell that has perfected this is the **hair cell**. Hair cells have a tuft of projections called stereocilia arranged in a staircase, shortest to tallest, connected by protein filaments called tip links. When the bundle deflects toward the tallest stereocilium, the tip links pull taut, the channel gate opens, and ions flow in. Here is the thing worth noticing: the fluid bathing the apical surface is *high* in potassium (this is endolymph, and the cells that maintain it spend ATP keeping K⁺ pumped in), so K⁺ flowing *into* the hair cell depolarizes it — opposite to what potassium does at a resting axon. Deflect the bundle the other way and the tip links slacken, the channels close, the cell hyperpolarizes. The hair cell is a bidirectional transducer, sitting at an intermediate voltage at rest, releasing neurotransmitter tonically and modulating that release with deflection.

This one design is reused everywhere mechanosensation matters. In the **cochlea** it reads sound: hair cells are arrayed along the basilar membrane, which is tuned by its mechanical properties — stiff and narrow at the base, floppy and wide at the apex. High frequencies maximally deflect the base; low frequencies deflect the apex. The brain reads pitch as which hair cells are firing, a **tonotopic map** — a frequency-place code. In the **vestibular organs** the same cells are weighted with calcium carbonate crystals (otoliths) that pull on them under gravity, or embedded in gel that resists rotational acceleration. Same cell, different mechanical environment, different stimulus.

And the same cell — almost exactly — lines the **lateral line** of fish and aquatic amphibians: a row of mechanosensory clusters along the flank, each containing hair cells with stereocilia embedded in a gelatinous flag called the cupula. Water flowing past deflects the cupula and the fish reads pressure waves, water currents, and the displacement fields of nearby animals. The lateral line is essentially directional hearing in water. When fish ancestors moved onto land the lateral line was lost — but the hair cells migrated inward and became the inner ear. The molecular logic of how you hear music is the molecular logic of how a fish senses a predator's wake.

The cochlea is doing something computationally notable. A complex sound — a chord, a human voice — is a sum of pure-frequency components. As the pressure wave travels down the basilar membrane, each frequency component deposits its energy where the membrane resonates at that frequency. The cochlea has performed a **Fourier decomposition** — separation of a complex signal into its frequency components — in hardware, mechanically, before any neuron has fired. The auditory nerve carries a place code, not a waveform. Bats extend this to frequencies around 100 kHz; some species exceed 120 kHz. Elephants extend the other end, hearing infrasound below 20 Hz that travels for kilometers through ground and air. Same cochlear architecture, scaled to different frequency windows.

![Unrolled basilar membrane showing frequency-to-place mapping ](images/06-sensory-systems-fig-01.png)
*Figure 6.1 — Unrolled basilar membrane showing frequency-to-place mapping *

---

## Echolocation — what physics allows

In the late 1930s, Donald Griffin at Harvard proved what Lazzaro Spallanzani had suggested in 1793: bats navigate by emitting ultrasonic pulses and detecting the echoes. Griffin coined the word *echolocation* in 1944. The physics of the system explains both what bats can do and why they cannot do more.

A big brown bat, *Eptesicus fuscus*, emits a pulse: a frequency-modulated sweep from roughly 60 kHz down to 25 kHz, lasting about 2 milliseconds. A moth is 2 meters away. The pulse travels to the moth and back — 4 meters total. At 343 m/s:

$$t = \frac{4 \text{ m}}{343 \text{ m/s}} \approx 11.7 \text{ ms}$$

The echo returns about 11.7 milliseconds after emission. That time delay encodes the target's range. Specialized **delay-tuned neurons** in the bat's auditory cortex — characterized by Nobuo Suga in the moustached bat — fire maximally for specific pulse-echo delays. One neuron fires for echoes at 5 ms (target 0.86 m away); another for echoes at 20 ms (3.4 m). The population across these neurons gives the bat a range map.

Now look at resolution. A sound wave's wavelength is:

$$\lambda = \frac{v}{f}$$

At 60 kHz:

$$\lambda = \frac{343}{60{,}000} \approx 5.7 \text{ mm}$$

Features smaller than the wavelength scatter sound diffusely rather than reflecting coherently. A wavelength of 5.7 mm sets the resolution floor. *Eptesicus* can detect a wire about 0.5 mm in diameter at close range — approximately what the diffraction limit predicts.

Here is the trade-off. Raise the frequency to 200 kHz: wavelength drops to 1.7 mm, resolution improves, but atmospheric absorption of ultrasound rises sharply with frequency — at 100 kHz, roughly 4 dB per meter, compared to negligible absorption at 1 kHz. A 200 kHz call can barely reach a target 1 meter away. A 20 kHz call reaches tens of meters but resolves only objects larger than 17 mm. **No single frequency optimizes both resolution and range.** High frequency buys spatial precision and sacrifices distance; low frequency gives range and sacrifices detail.

Real bats negotiate the trade-off adaptively. In open search, many species use lower-frequency calls for detection range. As they close on prey, they switch to a **terminal buzz** — pulses that are shorter, higher-frequency, and far more frequent (up to 200 per second), sacrificing range for the spatial precision needed to intercept a specific moth. The bat modulates its own Umwelt as the hunt progresses.

The same physics runs in water at different scale factors. Dolphins echolocate with clicks up to roughly 200 kHz. Sound travels about 1500 m/s in water — four times faster — so the same frequency has four times the wavelength. But dolphins are hunting fish and squid, not 5 mm moths, and can afford the relaxed resolution. The design is isomorphic; the parameters differ.

The hard limit — why no animal echolocates at 1 MHz, which would resolve sub-millimeter features — is atmospheric absorption. At 1 MHz, sound in air is absorbed nearly completely within centimeters. Selection cannot push the call frequency past what the medium permits. The Umwelt of the echolocator is bounded by physics, not biology.

---

## Thermoreception — the TRP channels, and what a chili pepper proves

A **TRP channel** (transient receptor potential) is an ion channel gated by some combination of temperature, ligand, and membrane voltage. Several members of the family are thermosensors with sharp threshold responses.

**TRPV1** opens at temperatures above about 43 °C — the threshold at which heat shifts from "warm" to "noxious," the temperature at which tissue damage begins. **TRPM8** opens below about 25 °C. The thresholds are not arbitrary; they appear to be set by selection at exactly the temperatures an animal needs to detect.

TRPV1 is also opened by **capsaicin**, the molecule in chili peppers. The plant evolved capsaicin as a defense against mammals that would crush and destroy seeds in digestion; it specifically activates *mammalian* TRPV1, not avian TRPV1 (birds disperse seeds intact and feel nothing). When you eat a chili, capsaicin binds TRPV1 on trigeminal nerve endings in your mouth. The channel opens. The neuron fires. And the brain — which has no way of knowing whether TRPV1 was opened by heat or by a molecule — reads "TRPV1 firing" as *hot*. There is no temperature change in your mouth. The labeled-line principle does not require ground truth; it only requires which wire fired.

TRPM8 is opened by menthol. The brain reads cold when nothing has cooled.

This is, I think, one of the most useful demonstrations in the entire chapter. The labeled-line principle, which can sound like an abstract rule, has consequences you can directly taste.

Pit vipers — rattlesnakes, copperheads — apply thermal machinery to a different problem. Each side of the head has a **pit organ**: a small cavity lined with a membrane roughly 15 micrometers thick, densely innervated by trigeminal neurons. The membrane absorbs infrared radiation emitted by warm-blooded prey and warms slightly; the warming opens **TRPA1** channels in the neurons, which fire, and the snake's brain integrates the signals from its two pits stereoscopically to build a spatial image. A rattlesnake can strike accurately at a mouse in complete darkness. The image is not formed by a lens focusing photons — it is a thermal map of a thin membrane. Same task as a vertebrate eye (map the positions of objects in space); completely different transduction mechanism.

The receptor protein decides what counts as the world.

---

## Chemoreception — the moth's floor and the dog's library

Chemoreception splits along a range axis. **Contact chemoreception** (taste) detects dissolved chemicals in fluid at the receptor surface — short range, high concentration. **Distance chemoreception** (smell) detects volatiles carried through air or water — long range, vanishingly low concentration.

Taste uses a small vocabulary of receptor types. Most mammals have receptors for sweet, sour, salty, bitter, and umami. Cats lack functional sweet receptors (obligate carnivores, no need to detect carbohydrates). Several mammalian groups have lost umami receptors after dietary shifts. The vocabulary is edited by ecology.

Smell uses combinatorial coding. A human has about 400 functional olfactory receptor types; a mouse has about 1100; a dog has roughly 800. Each olfactory sensory neuron expresses exactly one receptor type. An odorant molecule binds multiple receptor types with different affinities, producing a pattern across the receptor population. The brain reads the pattern. A coffee aroma is not "the coffee receptor firing"; it is a specific signature across hundreds of types. With 400 receptor types the number of distinguishable patterns is astronomical, which is why you can identify thousands of distinct odors despite having far fewer receptor types.

Dogs outperform humans partly through receptor diversity (more types), partly through volume (roughly 220 million olfactory neurons versus your 5 to 10 million), and partly through anatomy (the wet, drooping muzzle and long ear flaps that funnel scent to the nose). It is not a different system. It is the same system, scaled in several independent dimensions simultaneously.

The moth from the opening is the limit case. One molecule. One receptor type on each of 17,000 neurons per antenna. No competing signals to confuse the read. Chemoreception stripped down to a single channel and pushed to the detection floor. Every step of the sensory-system architecture is present — receptor protein, transduction to a voltage change, action potential train, labeled line to the brain — but specialized to an extreme that your own olfactory system, with its 400-type combinatorial palette, is not attempting.

---

## Photoreception — the dark current, and two ways to build an eye

A photon hits a rod photoreceptor. It is absorbed by **retinal** — an aldehyde of vitamin A — sitting in the binding pocket of the protein **opsin**. The photon's energy isomerizes retinal from its kinked form (11-*cis*) to a straight form (all-*trans*). The shape change snaps opsin into an active conformation, and active opsin is a G-protein-coupled receptor. It activates transducin, which activates phosphodiesterase, which destroys the second messenger cGMP.

In darkness, cGMP keeps sodium channels open, sodium flows in continuously (the **dark current**), and the photoreceptor sits at roughly −40 mV — partially depolarized, releasing neurotransmitter tonically. When light arrives and cGMP is destroyed, the sodium channels close, the dark current stops, and the cell **hyperpolarizes** toward −70 mV. Less neurotransmitter. More light, less signal — an inversion that the downstream wiring corrects.

One activated rhodopsin activates many transducins; each transducin activates many phosphodiesterases; each phosphodiesterase destroys many cGMP molecules. The cascade amplifies a single photon's event into a measurable voltage change. A vertebrate rod can detect a single photon. The same floor the moth reaches by a completely different path.

Color arises from having multiple opsin variants with different wavelength sensitivities. Your three cone opsins — short (~420 nm), medium (~530 nm), long (~560 nm) — produce color by ratio comparison. Most other mammals have two (dichromats), because ancestral mammals passed through a long nocturnal phase during the Mesozoic in which selection for color vision relaxed and one cone type was lost. Old World primate trichromacy is a **re-evolution** — a gene duplication of the longer-wavelength opsin that restored a third channel, likely selected for detecting ripe fruit against green leaves. **Trichromacy in humans is the recovered version, not the original.**

Birds, fish, and reptiles, whose lineages did not pass through the mammalian nocturnal bottleneck, generally kept four cone types and can see ultraviolet. A budgerigar looking at another budgerigar sees UV patterning on the feathers that we cannot perceive. Bees see UV bullseyes on flowers invisible to any mammal in the vicinity.

The mantis shrimp's sixteen-channel system is the cautionary tale. More receptor types is not automatically better color discrimination. Thoen's experiments show the shrimp discriminates wavelengths poorly — worse than a human. What the sixteen channels appear to do is rapid parallel classification rather than ratio-based comparison: a different algorithm for a different ecological task. Receptor count and behavioral capacity must be measured separately. Do not read the inventory and assume you know what the brain does with it.

Two eye architectures evolved independently and are worth knowing as a case study in convergent engineering.

The **camera eye** — vertebrates and cephalopods — uses a single lens to project an image onto a photoreceptor sheet. Vertebrate retinas are "inside-out" (photoreceptors face away from incoming light, axons project toward the lens, creating a blind spot where the optic nerve pierces the retina). Cephalopod retinas are "right-side-out" (photoreceptors face the light). Same task, slightly different assembly. Two independent evolutionary paths to the same geometry.

The **compound eye** of insects and crustaceans arrays many small lenses (ommatidia), each providing a narrow-angle sample of the visual field; the brain assembles the whole from the array. A dragonfly has up to 30,000 ommatidia per eye. Compound eyes give up some spatial resolution compared to a camera eye of equivalent diameter, but they can subtend much wider fields of view and achieve temporal resolutions that let a fly detect flicker at hundreds of hertz — where your eye saturates around 60 Hz. Different trade-offs for different ecologies.

![Comparison of vertebrate camera eye (inside-out retina, blind](images/06-sensory-systems-fig-02.png)
*Figure 6.2 — Comparison of vertebrate camera eye (inside-out retina, blind*

---

## Electroreception — sensing the field of a muscle

In the early 1960s, Hans Lissmann at Cambridge showed that African weakly electric fish generate and detect electric fields around their bodies. The fish carries a modified muscle organ — tissue that has lost its contractile ability but retained synchronized depolarization — that produces a continuous train of weak pulses. The pulses create a stereotyped field, and objects in the water with different conductivity distort it. Electroreceptors in the skin detect the distortion. This is **active electroreception**: the animal generates the probe signal and reads its perturbation, exactly as a bat generates pulses and reads echoes.

**Passive electroreception** is older. Sharks and rays carry **ampullae of Lorenzini** — gel-filled pits in the snout, each ending in a cluster of receptor cells that detect voltage gradients as small as a few nanovolts per centimeter. That sensitivity is enough to detect the bioelectric fields produced by the muscles of a fish hiding motionless under sand. The receptor cell is close in design to a hair cell: a tonically releasing sensory cell whose transmitter release rate is modulated by the incoming signal. The conductive gel that fills the ampulla acts as a low-impedance path for the external field directly to the receptor membrane.

Electroreception is mostly an aquatic trick because water conducts electric fields; air does not. The platypus and echidna carry electroreceptors in their bills — and hunt prey underwater. The exception confirms the rule.

---

## Magnetoreception — the honest account

Many animals navigate using the Earth's magnetic field. European robins use a magnetic compass for their trans-continental migrations. Sea turtles imprint on the geomagnetic field at their natal beach and return to it decades later. Monarch butterflies use a magnetic compass. The behavioral evidence is solid across many species.

How the receptor works is not settled. Three hypotheses have serious experimental support.

The **cryptochrome radical-pair hypothesis**: cryptochromes are blue-light-absorbing flavoproteins in bird retinas that, upon photon absorption, produce a pair of radicals with unpaired electron spins. The energy levels of those radicals — and therefore the rate of their recombination — depend on the orientation of the cryptochrome relative to Earth's magnetic field, because weak magnetic fields perturb unpaired electron spins. This would modulate the visual signal from the retina in a field-dependent way, giving the bird an effective magnetic overlay on its visual scene. The hypothesis invokes quantum coherence on the order of microseconds, which is just long enough for the field to act. European robins cannot orient when caged under monochromatic red light (which cryptochromes don't absorb); they orient normally under blue light. The behavioral result is consistent with the cryptochrome hypothesis. It does not confirm it — several alternative explanations remain.

The **magnetite hypothesis**: small crystals of magnetite (Fe₃O₄) embedded in nerve endings or specialized cells rotate slightly in the geomagnetic field, mechanically pulling on ion channels the way an otolith pulls on a hair cell. Magnetite has been found in pigeons, salmon, sea turtles, honey bees. The mechanism is simple. The problem: no one has unambiguously identified the specific cell containing the specific crystal connected to the specific nerve fiber whose ablation eliminates the magnetic sense. The receptor cell has not been found.

The **induction hypothesis**: a shark or ray swimming through Earth's magnetic field generates, by Lorentz forces on charged particles in its blood, very weak electric fields in its tissues. The ampullae of Lorenzini detect them. This requires no novel receptor — the animal's existing electroreceptors could double as a magnetic compass. It applies only to electroreceptive aquatic animals.

I list all three because the matter is genuinely unresolved. The behavioral evidence for magnetic sensing is excellent. The molecular identity of the receptor is not established. This is where the field is.

---

## What the chapter is really about

Return to the moth. A receptor protein specific to one molecule. One extra action potential per binding event. Detection at the chemical floor set by physics.

The bat: a call frequency that sets a spatial resolution floor by the diffraction limit of sound. No bat can echolocate more precisely than its wavelength permits; no bat can echolocate at a wavelength that atmospheric absorption prevents from traveling.

The vertebrate rod: a cascade that amplifies a single photon into a measurable voltage change. Detection at the photon floor.

Selection has driven each sensory modality, in some lineage, to the limit physics will allow. The moth's olfaction, the rod's photosensitivity, the shark's nanovolt electroreception, the bat's sub-millimeter echolocation — all of them are at or near the physical floor for their modality in their medium.

But every sensory system is also expensive. Photoreceptors spend ATP running the dark current. Olfactory neurons require continuous turnover. A bat's 110 dB call costs real metabolic energy — roughly 1 mJ per pulse, ten pulses per second in search, two hundred in a terminal buzz. The Umwelt an animal can maintain is bounded not only by physics but by what it can afford to power.

And no animal carries everything. The human Umwelt is a particular bet: strong on vision and vocal-auditory communication, weak on olfaction, apparently absent for electroreception and magnetoreception, blind above 740 nm and below 380 nm. We are unusual mammals. Most mammals lean heavily on olfaction; a dog's Umwelt is primarily an odor landscape that you will never perceive. A shark's Umwelt includes electric fields you will never sense. A bee's Umwelt includes ultraviolet patterns you will never see.

The point is not that these animals have more or better senses. Each Umwelt is a selection of which physical signals are worth the cost of the protein machinery to detect them, filtered by 500 million years of specific ecological pressure. The moth's antenna was not built to smell coffee; it was built to find females. The bat's cochlea was not built to hear music; it was built to catch moths in the dark. Different problems. Different solutions. Different worlds.

---

## Exercises

| receptor cell type | transduction mechanism (what opens | closes the channel) | key protein involved | example species at or near the physical limit — to be placed at start of exercises as a working reference |
| --- | --- | --- | --- | --- |
| mechanoreception, thermoreception, chemoreception, photoreception, electroreception, magnetoreception | columns: receptor cell type, transduction mechanism (what opens | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | Use the chapter example as the concrete test case. |
| key protein involved, example species at or near the physical limit | to be placed at start of exercises as a working reference | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | Use the chapter example as the concrete test case. |

**Warm-up 1.** You briefly touch a hot stove and pull your hand away. Identify two distinct TRP channels that are likely activated in this event, state the threshold temperature of each, and classify each receptor as tonic or phasic (adaptive rate). Then explain why the hand's withdrawal reflex works even when attention is elsewhere — name the level of the nervous system where the reflex arc closes, and explain why this is faster than a consciously directed response. *Tests: TRP channel thermoreception thresholds and the labeled-line principle applied to a familiar event.*

**Warm-up 2.** Your Pacinian corpuscle (a deep skin mechanoreceptor) fires when you first pick up a cup of coffee but goes quiet within two seconds while you are still holding it. (a) Classify this receptor as tonic or phasic and explain the adaptive logic: what information does this receptor's silence save the nervous system from processing? (b) You now shift the cup to the other hand. The Pacinian corpuscle fires again. Explain mechanistically why the receptor fires on the change but not during the steady hold. (c) Name one sensory modality where *tonic* receptors are essential and explain what would go wrong if they adapted rapidly. *Tests: tonic vs. phasic adaptation and its functional significance.*

**Warm-up 3.** A bat emits a call at 40 kHz and detects an echo from a target 3 meters away. (a) Compute the round-trip distance and the echo delay in milliseconds (use v = 343 m/s). (b) Compute the wavelength of the 40 kHz call and state the approximate minimum target size the bat could resolve. (c) This bat switches from a 40 kHz search call to a 90 kHz terminal buzz. State one thing that improves and one thing that gets worse, with a mechanistic explanation for each. *Tests: applying the echolocation physics — time delay for range, wavelength for resolution, the resolution-range trade-off.*

**Application 1.** A cat and a fruit bat both have excellent nocturnal vision, but they achieve it through different means. (a) Both animals have rod-dominated retinas; explain what property of rods makes them suited to low-light conditions, tracing from the single-photon sensitivity of rhodopsin to behavioral low-light performance. (b) The cat also has a *tapetum lucidum* — a reflective layer behind the retina that bounces light back through the photoreceptors, giving each photon a second chance to be absorbed. Predict one benefit and one cost of this adaptation at the level of spatial resolution. (c) The fruit bat uses olfaction and vision to find fruit; an insectivorous bat uses echolocation to catch moths. Predict how their olfactory receptor gene counts compare, and state the trade-off logic behind the prediction. *Tests: rod photoreceptor physics, the tapetum lucidum as a resolution-sensitivity trade-off, and receptor gene count as a proxy for Umwelt investment.*

**Application 2.** The European robin (*Erithacus rubecula*) cannot orient using its magnetic compass under monochromatic red light but orients normally under blue or full-spectrum light. (a) Explain this finding using the cryptochrome/radical-pair hypothesis: what does cryptochromes absorb, what does that absorption produce, and how does the magnetic field influence the outcome? (b) State specifically what this behavioral experiment does *not* prove — what alternative hypotheses remain consistent with the red-light finding? (c) A second experiment shows that magnetic compass orientation is disrupted by a radiofrequency electromagnetic field oscillating at a specific frequency (around 1.4 MHz). Explain why this result is considered additional evidence for the radical-pair mechanism rather than for the magnetite hypothesis. *Tests: evaluating evidence for a contested mechanistic hypothesis — what confirms vs. what is merely consistent with.*

**Application 3.** A hammerhead shark detects a ray buried under sand by sensing the ray's muscle bioelectric fields using its ampullae of Lorenzini. (a) The ampullae can resolve voltage gradients of a few nanovolts per centimeter. Explain the anatomical and physical features that make this sensitivity possible: what fills the ampullary canal, why does that matter, and what is the receptor cell doing to translate a voltage gradient into a neural signal? (b) Active electroreception (as in mormyrid electric fish) and passive electroreception (as in sharks) solve different problems. State what each system is optimized for and why the active system requires the fish to "know" what its own field looks like in a neutral environment. (c) The platypus uses electroreception to hunt in streams. Predict why this electroreceptive ability evolved in a terrestrial mammal lineage, and why it is restricted to aquatic hunting rather than being used on land. *Tests: passive vs. active electroreception, the physical requirement for the aquatic medium, and the ecological context for an unusual mammalian sense.*

**Synthesis 1.** The mantis shrimp has sixteen photoreceptor types but worse wavelength discrimination than a human with three. The dog has roughly twice the olfactory receptor gene count of a human but does not smell twice as many odors. Using these two examples, construct a general argument about the relationship between receptor diversity and perceptual capacity. Your argument must: (a) explain what receptor diversity *does* contribute (it is not irrelevant); (b) explain what receptor diversity alone *cannot* tell you about the animal's sensory world; and (c) propose what additional measurement would be necessary to characterize the full sensory capacity of an unknown species. *Tests: distinguishing receptor inventory from perceptual capacity — the core conceptual move of the Umwelt framework.*

**Synthesis 2.** The chapter argues that selection has driven each sensory modality, in some lineage, to the physical floor for detection. The moth reaches the single-molecule floor; the rod reaches the single-photon floor; the shark reaches the nanovolt electroreception floor. (a) For each of these three cases, identify the specific physical constraint that sets the floor — what property of chemistry, optics, or electrostatics defines the minimum detectable signal? (b) The bat's echolocation is argued to be near the diffraction limit. Explain what the diffraction limit is, why it is a floor, and what would happen to the bat's Umwelt if atmospheric physics allowed 1 MHz ultrasound to propagate without absorption. (c) All four of these systems are also expensive to run. For any two of them, identify the specific metabolic cost and explain what evolutionary pressure would maintain high sensitivity despite that cost. *Tests: identifying the physical floors across modalities and integrating the cost-benefit logic that defines the Umwelt each animal can afford.*

**Challenge.** You are studying a newly discovered cave-dwelling fish that has been isolated from surface populations for approximately 2 million years. It has no eyes — the optic nerves are absent. However, it has an unusually elaborate lateral line system with mechanoreceptor density roughly three times higher than its surface-dwelling relatives, and genetic analysis shows expansion of the gene family encoding olfactory receptors (from about 100 genes in surface fish to about 350 in the cave population). (a) Explain each of these three changes (eye loss, lateral line expansion, olfactory gene expansion) as a cost-benefit trade-off rather than as passive degradation. For each, identify what selection pressure would maintain the change and what metabolic resource the change reallocates. (b) The lateral line expansion is particularly strong in the region of the head near the snout. Propose a specific behavioral function this expanded lateral line region might serve in a lightless environment, and design a behavioral experiment to test your proposal. (c) A colleague argues that eye loss is "neutral drift" — random mutation accumulating in an unused structure — rather than active selection. Propose one prediction that would distinguish active selection for eye loss from neutral drift, and describe how you would test it. *Tests: applying the Umwelt framework to evolutionary change — reading sensory system shifts as cost-benefit reallocations rather than degradation, and distinguishing adaptive from neutral hypotheses.*

---

## LLM Exercise — Sensory Range Comparator

Build **`06-sensory-range-comparator.html`**: a side-by-side display of hearing range, visual spectrum, and (for bats) echolocation parameters across seven species — human, dog, bat (*Eptesicus fuscus*), eagle, shark, electric fish (mormyrid), mantis shrimp.

### Show / Say / Constrain / Verify — first pass

**Show** the LLM any simulator already in this book's file set so it knows the house style: single-file HTML, inline CSS and JS, no external dependencies.

**Say:**

> Build `06-sensory-range-comparator.html`. A dropdown selects a sensory modality (hearing, vision, smell, electroreception). A panel of checkboxes selects species. The display shows a horizontal bar on a log axis for hearing (1 Hz to 200 kHz) or a linear axis for vision (300 to 800 nm) for each selected species.
>
> Hearing bars: human 20 Hz–20 kHz; dog 67 Hz–45 kHz; bat 1 kHz–110 kHz; eagle 20 Hz–12 kHz; elephant 5 Hz–10 kHz.
>
> Vision bars: human 380–740 nm; dog 430–620 nm; eagle 300–750 nm; honey bee 300–650 nm; mantis shrimp 300–720 nm (annotate: "16 receptor types, parallel coding"). Mark cone peak wavelengths on the human bar (S 420 nm, M 530 nm, L 560 nm).
>
> Echolocation bonus panel (bat only): a pulse-and-echo timeline. A slider sets target distance (10 cm to 10 m). Display the 2 ms call pulse at 60 kHz, the echo delay computed as `2 × distance / 343` ms, and resolution in mm as `343 / 60000 × 1000`.

**Constrain:**

> All numeric values must be named constants in the code with a comment citing the source (or marked TODO/verify if uncertain). No external API calls. All rendering in SVG. Must work offline. Total file under 30 KB. No frameworks. Log scale for hearing, linear scale for vision. Background `#1a1a1a`, white monospace text, one color per species with a legend.

**Verify:**

> After generating the code, list every numeric range value you used and where it came from. If you guessed any of them, say so explicitly. Do not invent citations.

This verify step is the most important. Most LLM-generated educational content fails not at code but at facts. If the dog's upper hearing limit is displayed as 50 kHz instead of 45 kHz, every student who sees it will internalize the wrong number. The fact is part of the deliverable.

### Second pass — extension

Once the comparator runs, ask for two extensions:

1. **Body-mass ordering.** A toggle rescales the hearing display so species are stacked vertically in order of body mass. The pedagogical question: does hearing range correlate with body size? (Roughly yes — larger animals tend to hear lower frequencies — but bats and dolphins violate the pattern spectacularly. The visualization should make the correlation and its exceptions both visible.)

2. **What-if mode.** The user can drag the endpoints of any species' hearing bar. A small library of representative sounds (human speech ~100–8000 Hz, truck rumble ~30–200 Hz, dog whistle ~16–22 kHz, bat call ~25–110 kHz) is plotted on the same axis. Dragging a bar endpoint reveals which sounds that hypothetical animal would miss. Students can explore what conversations a dog hears that humans at 67 Hz lower bound do not — and also what the dog misses that a bat hears.

### Extension to Chapter 7

Chapter 7 covers endocrine signaling — chemical messengers broadcast in blood rather than the fast electrical signals we have spent two chapters on. Before arriving, ask the LLM to draft a comparison figure contrasting one neural signaling chain (sensory neuron → synapse → motor response, timescale: milliseconds) with one endocrine signaling chain (stimulus → hormone release → distant target tissue → response, timescale: minutes to hours). Have it identify, in the figure, where the analogous receptor, transducer, and encoder steps live in each system.

Both are solutions to the same problem class — detect a signal, convert it to information, route that information to an effector. The nervous system does it fast, point-to-point, and transiently. The endocrine system does it slowly, broadcast, and persistently. Same architecture, different operating parameters.

---

**What would change my mind.** If an unambiguous magnetoreceptor cell were identified — specific cell, specific protein, specific nerve fiber whose ablation eliminates the magnetic compass without disrupting any other sense — and the molecular mechanism turned out to be none of the three candidates I described, I would revise the magnetoreception section substantially. The current uncertainty reflects the real state of the field. A clean answer would change the story.

**Still puzzling.** The mantis shrimp's sixteen-channel visual system: if not for wavelength discrimination, then for what, exactly? The parallel pattern-coding hypothesis is consistent with the behavioral data but not yet directly demonstrated at the level of central processing. And why do pit vipers use thermal (TRPA1-based) machinery for infrared imaging rather than evolving a longer-wavelength opsin? Opsins clearly have the flexibility to span hundreds of nanometers in peak absorption, but no opsin is known that absorbs in the deep infrared. There must be a constraint; I don't know what it is.

---

**Tags:** sensory-physiology, umwelt, comparative-biology, transduction-mechanisms, echolocation
