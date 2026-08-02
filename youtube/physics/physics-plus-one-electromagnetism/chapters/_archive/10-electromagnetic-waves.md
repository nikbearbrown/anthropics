# Chapter 10 — Electromagnetic Waves

**Suggested titles**

1. Electromagnetic Waves
2. The Field That Carries Itself: Maxwell, Hertz, and the Unification of Light
3. Karlsruhe, 1887: Sparks Across an Empty Room

**TL;DR.** James Clerk Maxwell wrote down four equations in 1865 that, taken together, predicted a thing nobody had ever seen — a self-propagating wave of electric and magnetic fields traveling at exactly the speed of light. Twenty-two years later Heinrich Hertz coaxed sparks out of an empty loop of wire across his laboratory and proved Maxwell right. This chapter shows how the prediction works, how the same waves at different frequencies become radio, microwaves, infrared, light, ultraviolet, X-rays, and gamma rays, and how to compute the energy any of them carries.

---

## A spark across an empty laboratory, Karlsruhe, 1887

Heinrich Hertz, twenty-nine years old, professor of physics at the Karlsruhe Polytechnic, has wired up a small AC circuit on one bench. The circuit ends in a loop with a tiny gap. When he closes the switch, a spark jumps the gap. That's not the surprising part; spark gaps had been studied for decades. The surprising part is what's happening on the *other* bench, several meters away. A second loop, completely separate from the first, with no wires connecting them, contains its own little gap. And in that gap — when Hertz closes his switch — *another spark*.

Something has crossed the empty room.

For five years before this, Hertz had been chasing a prediction made by a Scottish theoretician named James Clerk Maxwell, who had died of cancer in 1879 at the age of forty-eight. Maxwell had argued, on purely mathematical grounds, that whenever electric charges accelerate they should radiate away a self-propagating wave of electric and magnetic fields, traveling at exactly the speed of light. Maxwell himself thought this was probably what light *was*. Nobody had proved it. Nobody had even seen one of these "electromagnetic waves" except as visible light, which they hadn't recognized as such.

Hertz's apparatus made the case directly. A current oscillating in the first loop accelerated charges in its wires. Those accelerating charges radiated a wave. The wave crossed the room. It hit the second loop. It accelerated charges in *that* loop too — enough to drive sparks across the receiver gap. Hertz measured the wavelength by setting up interference patterns. He measured the frequency from the resonant properties of his circuits. He multiplied them. The product was the speed of light.

What Hertz had built, without naming it that way, was the world's first radio transmitter and receiver. Within twenty years Marconi would be sending signals across the Atlantic. Within a century the entire planet would be wrapped in the same kind of waves at thousands of different frequencies — radio, television, GPS, Wi-Fi, microwave links, cell phones, deep-space communication. All of it Maxwell's prediction, all of it Hertz's discovery, all of it the same physics: an accelerating charge, a field that carries itself, a speed that turns out to be the speed of light.

**Learning objectives.** By the end of this chapter you should be able to:

1. State Maxwell's four equations in plain language and identify which experimental discovery each one captures.
2. Explain how an oscillating charge produces a self-propagating transverse wave of perpendicular electric and magnetic fields, and why the ratio $E/B = c$ in vacuum.
3. Use $c = f\lambda$ to convert between frequency and wavelength anywhere on the electromagnetic spectrum, and place named bands (radio, microwave, infrared, visible, UV, X-ray, gamma) in approximate order.
4. Calculate the average intensity of an electromagnetic wave from peak field strengths using $I_{\text{ave}} = c \varepsilon_0 E_0^2 / 2$ and convert intensity into the field amplitudes a real source must produce.
5. Apply the three rules of thumb relating frequency to penetration, information capacity, and resolvable detail to a real engineering or biological problem.

**Prerequisites.** Chapters 18–23 (electric fields, magnetic fields, Faraday's law of induction, AC circuits). The wave concepts of Chapter 16 (frequency, wavelength, transverse vs. longitudinal). Comfort with $\varepsilon_0$ and $\mu_0$ as physical constants.

**Why this chapter matters.** This is the chapter where electricity and magnetism become *light* — and where the entire spectrum from kilometer-long ELF waves to picometer gamma rays becomes one unified physics. Every later chapter on optics, vision, special relativity, quantum mechanics, and the structure of atoms uses something earned here. Without this chapter, Einstein's 1905 question — *what does a light wave look like if you ride alongside it?* — has no setting.

---

## Concept 1 — Maxwell's synthesis: how a moving charge makes a wave

### A blackboard in Cambridge, 1865

James Clerk Maxwell sits in his rooms at King's College London (he had been at Cambridge; he would move to Cambridge again as the first Cavendish Professor a few years later). Spread across his desk are the experimental laws that physicists have spent the previous half-century painstakingly extracting from electric and magnetic phenomena: Coulomb's inverse-square law for charges, Gauss's law for electric flux, Ampère's law tying current to magnetic field, Faraday's law tying changing magnetic flux to induced electric field. Each is a separate generalization of a different set of experiments.

Maxwell stares at the four equations and notices something is missing. Faraday's law says a *changing magnetic field* produces an electric field. By symmetry — and Maxwell took symmetry seriously, as a piece of physical reasoning, not just aesthetic taste — a *changing electric field* should produce a magnetic field. There was no experiment requiring this; the effect was too weak to detect with the instruments of the day. Maxwell added the term anyway, because the math was prettier and because Ampère's law without it gave inconsistent answers in some cases (charging capacitors, for example).

That one added term changed physics. Once you have it, the four equations fit together into a self-sustaining feedback loop: a changing electric field makes a magnetic field; the changing magnetic field makes an electric field; and the pair propagate forward. Solve the equations for empty space and they produce a wave equation whose wave speed comes out to

$$c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}}.$$

Plug in the measured values of the permittivity and permeability of free space — both quantities measured by people studying capacitors and inductors with no thought of light at all — and you get $c = 3.00 \times 10^8 \text{ m/s}$, which is the speed of light to within experimental error.

Maxwell's reaction, in a letter to a colleague: this is too close to be a coincidence. *Light is an electromagnetic wave.*

### The mechanism — Maxwell's four equations as a feedback loop

The full mathematical statement of Maxwell's equations uses vector calculus, which I won't write out here. But the physical content of each equation is sayable in a single sentence, and the four sentences together are the full theory. Here they are, paraphrased:

**1. Gauss's law for electricity.** Electric field lines start on positive charges and end on negative charges. The strength of the field around a charge is set by $\varepsilon_0$, the *permittivity of free space* — a constant that measures how readily empty space lets electric field lines spread out.

**2. Gauss's law for magnetism.** Magnetic field lines have no beginning and no end; they form closed loops. There are no isolated north or south magnetic poles ("magnetic monopoles"). Cut a bar magnet in half and you get two smaller bar magnets, never a separate north and south.

**3. Faraday's law of induction.** A changing magnetic field creates an electric field. The direction of the induced field is such that it opposes the change (Lenz's law). This is the principle behind every electric generator on Earth.

**4. Ampère-Maxwell law.** A magnetic field is created by two things: an electric current, *and* a changing electric field. The second part is Maxwell's addition. The constant $\mu_0$, the *permeability of free space*, sets the strength of the magnetic field a current produces.

Equations 3 and 4 are the engine. A wiggling charge produces a wiggling electric field. The wiggling electric field (equation 4) produces a wiggling magnetic field. The wiggling magnetic field (equation 3) produces a wiggling electric field a little farther on. The wiggling electric field there produces a wiggling magnetic field a little farther on. The pattern propagates outward at a speed set by how stiffly empty space supports each kind of field — that stiffness being captured by $\varepsilon_0$ and $\mu_0$. The result is a self-sustaining wave.

Two structural facts about the wave fall out of the equations:

- The electric field $\vec{E}$ and the magnetic field $\vec{B}$ are perpendicular to each other, and both are perpendicular to the direction of propagation. The wave is *transverse*.
- The field magnitudes are locked in a fixed ratio: $E/B = c$ at every point and every instant in vacuum.

### The trade-off

Maxwell's synthesis trades **physical intuition for mathematical inevitability.** Faraday could *see* magnetic field lines (he drew them, and his intuition for them was extraordinary). Maxwell turned those pictures into equations whose consequences he couldn't see — a wave that nobody had ever observed, traveling at a speed nobody had connected to electromagnetism. The cost was that the electromagnetic wave existed only on paper for two decades before Hertz cornered it. The benefit was that, once on paper, *the prediction was specific enough to be wrong* — and so was specific enough to be falsified or vindicated. Hertz vindicated it.

### Worked example — verifying the speed of light from $\mu_0$ and $\varepsilon_0$

Here is the calculation Maxwell did. The permittivity of free space, measured from electrostatic experiments long before Maxwell:

$$\varepsilon_0 = 8.85 \times 10^{-12} \text{ C}^2 / (\text{N} \cdot \text{m}^2).$$

The permeability of free space, measured (in modern terms) from the force between current-carrying wires:

$$\mu_0 = 4\pi \times 10^{-7} \text{ T} \cdot \text{m/A}.$$

Plug into Maxwell's prediction:

$$c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}} = \frac{1}{\sqrt{(8.85 \times 10^{-12})(4\pi \times 10^{-7})}} \approx 3.00 \times 10^8 \text{ m/s}.$$

This is the speed of light, to three significant figures. Two constants from completely different experiments — one from rubbing balloons on hair, in spirit; one from measuring the force between two parallel currents — combine to produce the speed at which light travels. The agreement is the argument. Maxwell didn't need a separate "and now let's check whether light is actually electromagnetic." The numbers had already done it.

### Common misconceptions

- *"Maxwell discovered four laws."* No — he wrote down four laws, three of which (Gauss, Faraday, Ampère) were already known. His original contribution was the *changing-electric-field-makes-magnetic-field* term in equation 4 and the synthesis showing that the four together imply electromagnetic waves at speed $c$. The brilliance was the unification, not the cataloguing.
- *"Electromagnetic waves need a medium to propagate, like sound waves."* No. Sound is a pressure wave in matter; with no air, no sound. EM waves are oscillations of fields in space itself; they propagate through vacuum, which is precisely why we can see the Sun and the stars. Nineteenth-century physicists *did* postulate a medium — the "luminiferous aether" — and the famous Michelson-Morley experiment of 1887 found no trace of it. We will return to this in Chapter 28.

↳ **Dig Deeper — Maxwell's missing term and the displacement current**

*The chapter describes Maxwell's added term in qualitative terms — "changing electric fields produce magnetic fields" — but the term has a name (the displacement current) and a clean physical motivation (it patches a contradiction in Ampère's law for circuits with capacitors). Working through the patch is one of the most satisfying half-hour exercises in undergraduate electromagnetism.*

**Prompt:**
> Show me, with one specific example involving a charging capacitor, why Ampère's law in its original form (only currents source magnetic fields) gives an inconsistent answer for the magnetic field around the wires. Explain how Maxwell's added "displacement current" term ($\mu_0 \varepsilon_0 \, \partial \vec{E} / \partial t$) restores consistency. Then state in one sentence why this added term is exactly what makes electromagnetic waves possible.

**What to do with the output:** Save it. The displacement current is the single most important "fix-it" term in classical physics — and recognizing the same kind of move (add a term to restore symmetry, get a wave equation out) is a pattern you will see again in quantum field theory.

---

## Concept 2 — From an oscillating charge to a wave

### KPHET, 91.5 MHz

A radio station's transmitter sits on a hilltop. Inside the antenna — for FM, a conducting rod usually a few meters long — an alternating current at the carrier frequency drives electrons up and down the rod. At the peak of one half-cycle, electrons pile up at the top of the rod; the rod's bottom is left positively charged. A quarter-cycle later, the charge separation is zero; the electrons are passing through the middle. A half-cycle later, the electrons have piled up at the bottom and the rod's top is positive. The pattern repeats $9.15 \times 10^7$ times per second.

Outside the antenna, the electric field follows the charge separation. When charges are split (top negative, bottom positive), the field around the antenna points upward in the air just outside. When the separation reverses, the field flips. The flipping pattern propagates outward at the speed of light. So does the magnetic field that the changing current generates around the rod, perpendicular to the electric field.

What leaves the antenna is a transverse electromagnetic wave whose frequency matches the oscillation in the antenna. A radio in your car, a few miles away, contains another antenna. The arriving electric field accelerates electrons in *that* antenna, producing a tiny alternating current at exactly the same frequency. The radio's circuitry isolates that frequency from the thousands of others arriving from other transmitters and converts it back into the audio signal the DJ broadcast.

That entire chain — from microphone to car speaker — is electromagnetic wave physics from one end to the other.

### The mechanism — what an EM wave looks like, and why $E/B = c$

Imagine a snapshot of the wave at one instant in time. Pick a point in space and look at what the fields are doing there. You see two arrows: an electric field arrow pointing one way (say, vertically), a magnetic field arrow pointing perpendicular to it (say, horizontally), and the wave moving in the third perpendicular direction (forward, into the page). A quarter-wavelength further along, both arrows are zero — the wave passes through a node. Another quarter-wavelength, and the arrows reappear pointing the *opposite* way. The whole pattern slides forward at speed $c$.

Several things are worth pinning down precisely:

- **The wave is transverse**, meaning the field oscillations are perpendicular to the direction of travel. (Sound waves, by contrast, are longitudinal — pressure varies *along* the direction of travel.) Try to make a longitudinal EM wave and you can't; the math forbids it in vacuum.
- **The wave is sinusoidal** for an antenna driven by a sinusoidal AC source. Real signals are usually sums of many sinusoids (Fourier components), but each component obeys the same physics.
- **The fields are in phase.** Where $E$ peaks, $B$ peaks. Where $E$ is zero, $B$ is zero. They oscillate together.
- **The fields are locked in ratio.** At every point, at every instant, in vacuum:

$$\frac{E}{B} = c.$$

That last point deserves a sentence of intuition. The amplitude of the electric field is set by the size of the charge separation in the antenna; the amplitude of the magnetic field is set by the size of the current those charges carry. Voltage relates to $E$, current to $B$, and the ratio of the two — through Ohm-like reasoning extended to free space — is fixed by the impedance of free space, which is a number ($\approx 377 \text{ ohms}$) that combines $\varepsilon_0$ and $\mu_0$. The fixed ratio is not a coincidence; it's a consequence of the wave equation.

In a medium with index of refraction $n$, the wave slows to $v = c/n$ and the field ratio becomes $E/B = c/n$. We meet this in detail in Chapter 25 (geometric optics).

### The trade-off

Antenna physics trades **frequency for size.** The most efficient antenna for a given wavelength has a length around $\lambda/2$ (a "half-wave dipole"). A 1530 kHz AM radio station broadcasts at $\lambda \approx 196 \text{ m}$, requiring a transmitting antenna nearly $100 \text{ m}$ tall. A 105.1 MHz FM station has $\lambda \approx 2.85 \text{ m}$ — a much smaller, more practical structure. A 1.90 GHz cell phone signal has $\lambda \approx 16 \text{ cm}$, which is why your phone's antenna fits inside the case. The physics is the same; the engineering is utterly different at each scale.

### Worked example — calculating $B_0$ from $E_0$

A radar pulse has a peak electric field strength of $E_0 = 1000 \text{ V/m}$ in vacuum. What is the peak magnetic field strength?

Use $E/B = c$, rearranged:

$$B_0 = \frac{E_0}{c} = \frac{1000 \text{ V/m}}{3.00 \times 10^8 \text{ m/s}} = 3.33 \times 10^{-6} \text{ T}.$$

A peak field of $3.33 \text{ }\mu\text{T}$ — about a tenth of Earth's surface magnetic field. Notice the asymmetry: a "strong" electric field of $1000 \text{ V/m}$ comes paired with a "weak" magnetic field that an everyday compass would barely notice. The ratio is $c$, and $c$ is enormous.

**Sanity check.** If you compute energy density in the two fields — using $u_E = \tfrac{1}{2} \varepsilon_0 E^2$ and $u_B = B^2 / (2\mu_0)$ — and substitute $B = E/c$, you find that $u_E = u_B$ exactly. The two fields carry equal energy in an EM wave even though their numerical strengths look wildly different. The "weakness" of the magnetic field is just a unit artifact.

### Common misconceptions

- *"Radio waves are different from light."* No, only the frequency is different. Same physics, same wave equation, same speed $c$.
- *"The magnetic field of an EM wave is negligible."* Quantitatively small compared to $E$ in SI units, but as just shown, it carries half the wave's energy. Don't confuse "small number" with "physically negligible."

↳ **Dig Deeper — Polarization and the orientation of the field**

*The chapter says EM waves are transverse, but doesn't pin down the direction of $\vec{E}$ within the plane perpendicular to propagation. That direction is the wave's polarization, and it's the property that polarized sunglasses, LCD displays, and quarter-wave plates exploit.*

**Prompt:**
> Explain what polarization of an electromagnetic wave means in physical terms, distinguishing linear, circular, and elliptical polarization. Walk me through how a polarizing filter (like the one in polarized sunglasses) works at the level of electric field components — why it transmits half of unpolarized light's intensity, and why two crossed polarizers transmit zero. End with one sentence on why polarization matters in radio antenna design (vertical vs. horizontal antennas).

**What to do with the output:** Save it. We meet polarization again in Chapter 27 (wave optics) — having worked through it once here makes that chapter much faster.

---

## Concept 3 — The spectrum and the energy it carries

### Penzias and Wilson, Holmdel, 1964

Arno Penzias and Robert Wilson are puzzled. They are radio astronomers at Bell Labs in Holmdel, New Jersey, trying to use a horn-shaped antenna built for early satellite communications to study faint radio sources in the sky. Every time they point the antenna anywhere — at the galactic plane, at empty sky, at the horizon — they hear the same faint hiss in their receiver, at a wavelength of about 7 centimeters. They check everything. They scrub pigeon droppings out of the horn. They recheck the electronics. The hiss persists. Whatever it is, it appears to be coming from everywhere in the sky at the same intensity.

What they had detected, without knowing it, was the cosmic microwave background — the cooled remnant of the Big Bang, a bath of microwave radiation that fills the universe at a temperature of about $2.7 \text{ K}$, peaked in the microwave region of the electromagnetic spectrum. Their accidental discovery, eventually awarded the 1978 Nobel Prize, is one of the most important pieces of evidence for the Big Bang model of cosmology. They found it by listening for noise on a radio antenna.

This is the spectrum's quiet point: the same equations that describe an FM broadcast from a hilltop describe the relic radiation from the early universe. Maxwell's waves don't care what frequency they are — only how energetic, how penetrating, how easily detected. Across forty orders of magnitude of frequency, from ELF to gamma rays, it is one physics.

### The mechanism — $c = f\lambda$ and the named bands

Every electromagnetic wave in vacuum satisfies

$$c = f\lambda,$$

where $f$ is the frequency (cycles per second, in hertz) and $\lambda$ is the wavelength (meters per cycle). Higher frequency means shorter wavelength; they are inversely proportional, and their product is fixed at the speed of light.

The full electromagnetic spectrum — historically named by the technology that first detected each band — runs:

| Band | Frequency range | Wavelength range | Typical source |
|---|---|---|---|
| Radio (incl. ELF) | $< 10^9 \text{ Hz}$ | $> 30 \text{ cm}$ to thousands of km | AC currents in wires, antennas, lightning |
| Microwave | $10^9$–$10^{12} \text{ Hz}$ | $1 \text{ mm}$–$30 \text{ cm}$ | Klystrons, magnetrons, thermal emission |
| Infrared | $10^{12}$–$4 \times 10^{14} \text{ Hz}$ | $750 \text{ nm}$–$1 \text{ mm}$ | Thermal motion of atoms, vibrational transitions |
| Visible | $4 \times 10^{14}$–$8 \times 10^{14} \text{ Hz}$ | $380$–$750 \text{ nm}$ | Electronic transitions in atoms |
| Ultraviolet | $8 \times 10^{14}$–$3 \times 10^{16} \text{ Hz}$ | $10$–$400 \text{ nm}$ | Higher-energy electronic transitions |
| X-ray | $3 \times 10^{16}$–$3 \times 10^{19} \text{ Hz}$ | $10 \text{ pm}$–$10 \text{ nm}$ | Inner-shell electron transitions, bremsstrahlung |
| Gamma | $> 3 \times 10^{19} \text{ Hz}$ | $< 10 \text{ pm}$ | Nuclear decay, particle annihilation |

The boundaries are conventional and overlap. There is nothing physically distinguishing a 10 nm "ultraviolet" photon from a 10 nm "X-ray" photon; the names reflect how each was discovered, not a physical discontinuity. The OpenStax table gives a useful three rules of thumb that hold *most* of the time across the spectrum:

1. **Higher frequency means more energetic and more penetrating.** Visible light is stopped by your skin; X-rays are not.
2. **Higher frequency carries more information per unit time.** This is why fiber-optic networks (visible/IR frequencies) carry vastly more data than AM radio.
3. **Shorter wavelength means smaller resolvable detail.** A microscope using ultraviolet sees finer structure than one using visible light. An MRI using radio waves resolves submillimeter features only because of clever resonance tricks — an exception to the rule, not a refutation.

### Energy and intensity

A wave carries energy in proportion to the square of its amplitude. For an electromagnetic wave, the average intensity (power per unit area) is

$$I_{\text{ave}} = \frac{c \varepsilon_0 E_0^2}{2},$$

where $E_0$ is the peak electric field strength. Equivalent forms:

$$I_{\text{ave}} = \frac{c B_0^2}{2 \mu_0} = \frac{E_0 B_0}{2 \mu_0}.$$

All three are the same physics in different bookkeeping. The factor of $1/2$ comes from time-averaging $\sin^2(\omega t)$ over a cycle; the peak intensity is twice the average.

### The trade-off

Designing antennas across the spectrum trades **resolution and information capacity for penetration and reach.** ELF radio waves (kilometer wavelengths) wrap around hills and dive into ocean water — submarine communication uses them — but carry essentially no information per second. Microwaves carry enormous bandwidth but require line-of-sight and get absorbed by atmospheric water. X-rays penetrate flesh but require shielded high-voltage equipment to produce safely. The right band for the job is always context-dependent.

### Worked example — intensity inside a microwave oven

A microwave oven on its highest setting puts $1.00 \text{ kW}$ of microwave power onto a heating area $30.0 \text{ cm} \times 40.0 \text{ cm} = 0.120 \text{ m}^2$.

**Question 1.** What is the average intensity?

Intensity is power per unit area:

$$I_{\text{ave}} = \frac{P}{A} = \frac{1000 \text{ W}}{0.120 \text{ m}^2} = 8.33 \times 10^3 \text{ W/m}^2.$$

For comparison, sunlight at noon is roughly $1000 \text{ W/m}^2$; the inside of a microwave is about eight times more intense.

**Question 2.** What is the peak electric field strength?

Rearrange $I_{\text{ave}} = c \varepsilon_0 E_0^2 / 2$ for $E_0$:

$$E_0 = \sqrt{\frac{2 I_{\text{ave}}}{c \varepsilon_0}} = \sqrt{\frac{2 (8.33 \times 10^3)}{(3.00 \times 10^8)(8.85 \times 10^{-12})}} \approx 2.51 \times 10^3 \text{ V/m}.$$

**Question 3.** What is the peak magnetic field strength?

$$B_0 = \frac{E_0}{c} = \frac{2510}{3.00 \times 10^8} \approx 8.35 \times 10^{-6} \text{ T}.$$

**Sanity check.** The peak $B_0 \approx 8 \text{ }\mu\text{T}$ is about twenty times Earth's surface magnetic field of $\sim 0.4 \text{ G} = 4 \times 10^{-5} \text{ T}$ — substantial but not extreme. The peak $E_0 \approx 2.5 \text{ kV/m}$ would arc a small spark across a centimeter of dry air (the breakdown field of air is about $3 \text{ MV/m}$), so we're three orders of magnitude below dielectric breakdown. The numbers are physically reasonable for a kitchen appliance.

### Common misconceptions

- *"Microwaves heat food because they 'excite the water molecules.'"* That's the right idea but the wrong mechanism in detail. Microwaves at 2.45 GHz drive an oscillating electric field that exerts torque on the dipole moments of water molecules. The molecules try to follow, lose energy to friction with their neighbors, and that frictional heating is what cooks the food. The frequency is *not* a resonance with water (water's main resonance is at much higher frequency); it's a compromise designed for good penetration depth.
- *"Higher-frequency EM waves are dangerous; lower-frequency ones aren't."* True only as a coarse generalization. The relevant question is whether the photon energy ($E = hf$, Chapter 29) is large enough to ionize molecules — break chemical bonds. UV, X-ray, and gamma rays do this; visible, IR, microwaves, and radio do not. *Non-ionizing* radiation can still cause damage by heating, but the mechanism is different and the dose-response curve is steeper before harm sets in.

↳ **Dig Deeper — Why the sky is blue and why sunsets are red**

*The chapter says different EM frequencies behave differently when they encounter matter, but doesn't say much about scattering. Rayleigh scattering — the preferential scattering of short wavelengths by particles much smaller than the wavelength — is the single mechanism behind both the blue sky and the red sunset. Working through the scaling makes both phenomena obvious.*

**Prompt:**
> Explain Rayleigh scattering and use it to derive (qualitatively) why the daytime sky is blue and why sunsets are red. The key fact is that the scattering cross-section scales as $1/\lambda^4$, so blue light (shorter wavelength) scatters far more strongly than red light from molecules in the atmosphere. Walk through the geometry: when you look at the sky away from the sun, you see scattered sunlight (favoring blue); when you look at the sun near the horizon, you see direct sunlight that has had its blue scattered out (favoring red). End with one sentence on why this same physics explains why the Sun looks yellow rather than white.

**What to do with the output:** Save it. The $1/\lambda^4$ scaling is one of the cleanest pieces of color physics in the book — and explains one of the more frequently-asked questions in casual conversation.

---

## Synthesis — one prediction, one spectrum

Step back and look at what you've walked through. Maxwell wrote down four equations in 1865 that *predicted* a self-propagating wave of perpendicular electric and magnetic fields, traveling at exactly $c = 1/\sqrt{\mu_0 \varepsilon_0}$. Hertz built the wave in 1887 and measured its speed. From that point forward, every kind of "ray" or "wave" or "radiation" that anyone has ever found anywhere in the universe — radio, microwave, IR, visible, UV, X-ray, gamma — has turned out to be the same wave, just at a different frequency.

The chapter's three concepts braid together. **Concept 1** gave you the equations and the physical mechanism: a changing electric field makes a magnetic field, a changing magnetic field makes an electric field, and the two together carry themselves through space at speed $c$. **Concept 2** told you what an EM wave looks like in detail — transverse, in-phase fields with $E/B = c$ — and how an oscillating charge produces one. **Concept 3** classified the spectrum by frequency, named the rules of thumb that hold across it, and gave you the three equivalent expressions for intensity that let you compute how much energy any wave carries.

The deepest single fact: **everything you know as "light," and everything you know as "radio," and everything that hits your retina or your antenna or your X-ray plate, is the same physics at a different wavelength.** Nineteenth-century physicists talked about "radiant heat" and "actinic rays" and "chemical rays" and so on as if they were separate phenomena; Maxwell's synthesis revealed them all as one thing.

### A worked example using all three concepts — designing an FM broadcast

A new FM radio station at 91.5 MHz wants to broadcast 50 kW of power.

**Concept 1 — Maxwell's equations license the design.** The station works because oscillating currents in the antenna radiate self-propagating EM waves at the carrier frequency. Maxwell's equations say this works in vacuum and approximately in air (whose $\varepsilon$ and $\mu$ are very close to $\varepsilon_0$ and $\mu_0$).

**Concept 2 — wavelength sets the antenna.** The wavelength is

$$\lambda = \frac{c}{f} = \frac{3.00 \times 10^8}{91.5 \times 10^6} \approx 3.28 \text{ m}.$$

Most efficient antenna length is $\lambda/2 \approx 1.64 \text{ m}$. A short broadcast tower with that-sized dipole at the top will radiate efficiently.

**Concept 3 — intensity and field strength at a distance.** Assume the station broadcasts uniformly over a hemisphere (the upward hemisphere, since the ground absorbs or reflects). The intensity at distance $r$ from the transmitter is

$$I = \frac{P}{2 \pi r^2}.$$

At $r = 10 \text{ km}$:

$$I = \frac{50{,}000}{2 \pi (10{,}000)^2} \approx 8.0 \times 10^{-5} \text{ W/m}^2.$$

The corresponding peak electric field strength:

$$E_0 = \sqrt{\frac{2I}{c \varepsilon_0}} = \sqrt{\frac{2 (8.0 \times 10^{-5})}{(3.00 \times 10^8)(8.85 \times 10^{-12})}} \approx 0.25 \text{ V/m}.$$

A receiver at 10 km from the transmitter sees a peak electric field of about a quarter volt per meter at its antenna — small, but easily amplified by tuned electronics.

**Scale shift.** That same radio station's signal, traveling outward at $3 \times 10^8 \text{ m/s}$, will reach the orbit of Mars about 12 minutes from now and the nearest star, Proxima Centauri, in 4.2 years. The intensity at Proxima will be $I = 50{,}000 / [2\pi (4 \times 10^{16})^2] \approx 5 \times 10^{-30} \text{ W/m}^2$ — too small for any imaginable Proxima receiver to detect, but the wave is still there, propagating onward forever. Maxwell's equations don't have a "stop" condition. Once launched, the wave goes until it's absorbed.

---

## Exercises

### Warm-up

**24.1** *(LO 1)* In one sentence each, state what experimental phenomenon each of Maxwell's four equations captures.

**24.2** *(LO 3)* Calculate the wavelength of (a) a 540 kHz AM radio signal, (b) a 2.45 GHz microwave, (c) a 600 nm orange-light photon expressed as a frequency, (d) a $5 \times 10^{18} \text{ Hz}$ X-ray expressed as a wavelength.

**24.3** *(LO 2)* The peak electric field in an EM wave is $300 \text{ V/m}$. Find the peak magnetic field strength.

**24.4** *(LO 4)* A laser pointer outputs $1.0 \text{ mW}$ over a $1.0 \text{ mm}^2$ beam. Find the average intensity in $\text{W/m}^2$.

### Application

**24.5** *(LO 3)* The most efficient half-wave dipole antenna for a 27 MHz CB radio band has what length? Compare to the antenna on a typical car.

**24.6** *(LO 4)* A microwave oven of 700 W is focused on a $20.0 \text{ cm}$ diameter circular area. Compute (a) the average intensity, (b) the peak electric field, (c) the peak magnetic field.

**24.7** *(LO 5)* MRI machines operate at radio frequencies near 100 MHz but can resolve submillimeter detail in tissue. Which of the three "rules of thumb" appears to be violated, and what physical mechanism allows the violation?

**24.8** *(LO 3)* A 50.0 Hz AC power line radiates an EM wave with peak $E_0 = 13.0 \text{ kV/m}$. Find (a) the wavelength, (b) the peak magnetic field strength.

### Synthesis

**24.9** *(LO 1, LO 4)* The Sun delivers about $1361 \text{ W/m}^2$ to the top of Earth's atmosphere (the *solar constant*). (a) What is the peak electric field strength of this radiation? (b) What is the peak magnetic field strength? (c) Compare $B_0$ to Earth's surface magnetic field of $\sim 5 \times 10^{-5} \text{ T}$.

**24.10** *(LO 3, LO 4)* A pulsed laser used for inertial-confinement fusion produces a peak electric field of $1.00 \times 10^{11} \text{ V/m}$ for $1.00 \text{ ns}$. Find (a) the peak magnetic field, (b) the intensity, (c) the energy delivered to a $1.00 \text{ mm}^2$ spot.

**24.11** *(LO 1, LO 3)* In Hertz's original 1887 experiment, his transmitter and receiver loops were each tuned to about 100 MHz. Compute the wavelength. If his laboratory was 5 m across, how many wavelengths fit between transmitter and receiver?

### Challenge

**24.12** *(beyond chapter)* The cosmic microwave background detected by Penzias and Wilson has a thermal spectrum corresponding to $T = 2.725 \text{ K}$ and peaks at a wavelength near $1 \text{ mm}$. (a) Convert this peak wavelength to a frequency. (b) Use Wien's law $\lambda_{\text{peak}} T = 2.898 \times 10^{-3} \text{ m} \cdot \text{K}$ to verify the peak position. (c) In one paragraph, explain in your own words why a microwave oven's 2.45 GHz frequency was chosen rather than a frequency closer to the thermal peak of body-temperature water.

**24.13** *(beyond chapter)* In the era before fiber optics, transatlantic phone calls were carried by HF radio (3–30 MHz) bouncing off the ionosphere. Modern fiber optic cables carry signals at near-IR wavelengths (~1550 nm). (a) Compute the bandwidth ratio between the two methods, assuming you can use roughly 10% of the carrier frequency as bandwidth. (b) Use Rule 2 from the chapter to explain qualitatively why the switch to optical was inevitable.

---

## LLM Exercise — Chapter 24: Electromagnetic Waves in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** One Logbook entry identifying the EM-wave content of your anchor phenomenon — the radio, microwave, IR, visible, or UV signals it emits, absorbs, or relies on — with a numerical estimate of frequency, wavelength, and (where possible) intensity.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste your 1-sentence description].

For Chapter 24, I want to apply electromagnetic wave physics — Maxwell's equations, the spectrum c = f λ, intensity I = c ε₀ E₀² / 2 — to my phenomenon.

Please:

1. Identify ONE electromagnetic-wave aspect of my phenomenon. Examples: for a bike commute — the visible light (sunlight, headlights, traffic signals) my eyes process, or the GPS L1 signal at 1.575 GHz my phone uses to navigate. For a coffee maker — the IR thermal radiation it emits when hot, or the microwave heating element if it has one. For a basketball shot — the sodium/halogen lighting in the gym, color temperature ~3000 K. For a marathon — the UV exposure from sunlight (relevant for skin damage and timing chips, which often use 433 MHz or 2.4 GHz radio).

2. Identify the relevant frequency band and estimate (a) the frequency, (b) the wavelength, (c) the typical intensity at the relevant location.

3. Apply at least one of the three rules of thumb (penetration, information capacity, or resolvable detail) to explain why that band is the right band for the phenomenon.

4. Compute one quantitative quantity using a chapter equation: peak field strength E₀, total power, or wavelength. Show units and propagate uncertainty using the percent-addition rule from Chapter 1.

5. Identify one place where the EM-wave behavior surprises you or where your previous mental picture was wrong.

6. One sentence connecting this to Chapter 25 (geometric optics).

Save the output as logbook/chapter-24-em-waves.md.
```

### What this produces

A Logbook entry naming the EM signals at play in your anchor phenomenon — possibly the first time you've thought about it as an electromagnetic system at all.

### How to adapt this prompt

- *For a phenomenon with no obvious EM content:* Almost everything visible relies on light. The exercise becomes about the visible-light intensity at the eye, color temperature of the illumination, and how that determines what you see.
- *For ChatGPT/Gemini:* Identical, with interface substitutions.
- *For Claude Code:* If your phenomenon involves a measurable signal (recorded sound, a video, a thermal image), use Claude Code to extract the spectrum or estimate intensity from pixel values.

### Connection to previous chapters

Builds directly on Chapters 18–23 (electric and magnetic fields, AC circuits) — Maxwell's equations are the synthesis of all of those. Uses the uncertainty propagation from Chapter 1.

### Preview of next chapter

Chapter 25 narrows in on visible light and the geometry of how it bends, reflects, and focuses through lenses and mirrors. The Chapter 25 LLM Exercise will ask you to identify a *lens* or *mirror* in your anchor phenomenon (your eye, a camera, a coffee-cup curve) and analyze its image-forming behavior.

---

## Chapter summary

Maxwell's four equations describe all of classical electromagnetism. Their most surprising consequence — buried until Maxwell added the displacement-current term — is that empty space supports self-propagating waves of perpendicular electric and magnetic fields, traveling at $c = 1/\sqrt{\mu_0 \varepsilon_0}$. Hertz proved this experimentally in 1887. Light is one such wave; radio, microwaves, IR, UV, X-rays, and gamma rays are others, distinguished only by frequency.

The one idea that matters most: **the entire electromagnetic spectrum is a single physics, not many physics.** Every band obeys $c = f\lambda$, every band has $E/B = c$ in vacuum, every band carries energy proportional to $E_0^2$. The names — radio, microwave, X-ray — track the human history of discovery, not separate phenomena.

The common mistake to watch for: **treating different bands as fundamentally different.** They aren't. The same equations describe a 60 Hz power-line hum and a $10^{20} \text{ Hz}$ gamma ray from cosmic ray decay. The differences are in how the wave interacts with matter, which is a quantum-mechanical question we'll start in Chapter 29.

What you should now be able to teach someone else: how Maxwell's symmetry argument predicted EM waves before anyone had seen one; why $E$ and $B$ are perpendicular and locked at the ratio $c$; how to convert between frequency and wavelength; and how to compute intensity from peak field strengths. If you can explain why your kitchen microwave operates at 2.45 GHz rather than 2 GHz or 5 GHz, you've understood this chapter.

---

## What would change my mind

The chapter argues that Maxwell's equations are a complete classical description of electromagnetic phenomena and that all observed EM waves fit this framework. The argument would need revision if a precision experiment found a deviation from $c = 1/\sqrt{\mu_0 \varepsilon_0}$ at any frequency, or if a magnetic monopole were found (Gauss's law for magnetism would need an extra source term), or if EM wave propagation in vacuum were shown to depend on direction of travel (which would imply a preferred frame and contradict Chapter 28's relativity). All three have been searched for; none has been found.

## Still puzzling

I do not understand at the deepest level *why* electromagnetism takes the form Maxwell wrote down. The four equations have a beautiful symmetry, and the addition of the displacement current restored it. But why electric charge exists, why $\varepsilon_0$ and $\mu_0$ have the values they do, and why empty space has the impedance it has — these are facts the standard model accepts as given rather than derives from a deeper principle. Explaining them is part of the unfinished business of physics.

---

## Connections forward

Chapter 25 (geometric optics) restricts to visible-light EM waves and asks how they bend and focus through lenses and mirrors — ray optics, where the wavelength is small compared to the apparatus. Chapter 26 (vision and instruments) uses geometric optics to build microscopes, telescopes, and the eye itself. Chapter 27 (wave optics) returns to the wave nature of light and shows where geometric optics breaks down — diffraction, interference, polarization. Chapter 28 (special relativity) revisits the speed of light as a postulate of the new physics. Chapter 29 (quantum mechanics) shows that EM waves come in discrete packets called photons, and that the photoelectric effect cannot be explained by Maxwell's equations alone — the first crack in the classical picture.

---

**Tags:** electromagnetic-waves, Maxwell-equations, Hertz-experiment, spectrum, intensity

---

## AI Wayback Machine

**James Clerk Maxwell** unified electricity, magnetism, and light in his 1865 paper — predicting that light is an electromagnetic wave from the equations alone. Einstein called him the most important physicist between Newton and himself.

**Run this:**

```
Who was James Clerk Maxwell, and how do Maxwell's equations connect to electromagnetic waves we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"James Clerk Maxwell"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how Maxwell's equations predict the speed of light from the electromagnetic constants alone.
- Ask it about Maxwell's contributions outside electromagnetism — color photography, Saturn's rings, kinetic theory.

What changes? What gets better? What gets worse?
