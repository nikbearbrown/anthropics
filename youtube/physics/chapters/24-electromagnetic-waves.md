# Chapter 24 — Electromagnetic Waves

*In 1865, Maxwell predicted something nobody had seen. In 1887, Hertz found it.*

---

![Schematic of Hertz's 1887 experiment: induction coil drives a primary spark across a gap (transmitter). Across the room, a small loop with its own tiny gap (receiver) sparks in resonance. Confirmed Maxwell's prediction that EM...](../images/24-electromagnetic-waves-fig-06.png)
*Figure 24.6 — Hertz, 1887 — Generated and Detected EM Waves Across an Empty Room*

In 1887, Heinrich Hertz wired up a small AC circuit in his laboratory in Karlsruhe. The circuit ended in a loop with a tiny gap. When he closed the switch, a spark jumped. That wasn't the surprising part. The surprising part was what happened at the other bench, several meters away: a second loop, no wires connecting it to the first, with its own tiny gap — and when Hertz closed his switch, *another spark*.

Something had crossed the empty room.

For five years Hertz had been chasing a prediction made by James Clerk Maxwell, who had died in 1879 at forty-eight. Maxwell had argued, on purely mathematical grounds, that oscillating electric charges should radiate a self-propagating wave of electric and magnetic fields traveling at the speed of light, and that light itself was such a wave. Nobody had proved it. Hertz's apparatus proved it directly. He set up interference patterns, measured the wavelength, measured the frequency from the circuit's resonance, and multiplied. The product was the speed of light.

![3D perspective of a plane EM wave propagating in the +x direction. E oscillates in the y direction (vertical sinusoid). B oscillates in the z direction (horizontal sinusoid, depth). Both in phase. Energy flows along k̂ = +x....](../images/24-electromagnetic-waves-fig-03.png)
*Figure 24.3 — Plane EM Wave — E ⊥ B ⊥ k̂, All Mutually Perpendicular, In Phase*

What Hertz built was the world's first radio transmitter and receiver. Within twenty years Marconi was sending signals across the Atlantic. Within a century the planet was wrapped in these waves at thousands of frequencies — radio, television, GPS, Wi-Fi, cell phones, deep-space communication. All of it Maxwell's prediction, all of it Hertz's discovery, all of it the same physics.

---

## Maxwell's synthesis

![Reference card with Maxwell's four equations in integral form: Gauss for E (charges source E), Gauss for B (no monopoles), Faraday (changing B makes E), Ampère-Maxwell (currents and changing E make B). Plus the wave equation...](../images/24-electromagnetic-waves-fig-02.png)
*Figure 24.2 — Maxwell's Four Equations — All of Classical Electrodynamics on One Card*

James Clerk Maxwell, around 1865, was staring at four equations that summarized fifty years of experimental work on electricity and magnetism. Three were well-established: Gauss's law (electric field lines start on positive charges, end on negative), the magnetic equivalent of Gauss's law (magnetic field lines form closed loops — no isolated magnetic poles), and Faraday's law of induction (a changing magnetic field produces an electric field — this is how every generator on Earth works). The fourth — Ampère's law — said currents produce magnetic fields.

![A capacitor is charging. Choose an Ampèrian loop around the connecting wire. Two surfaces span it: a flat one cut by the wire (real current I) and a balloon-shaped one passing between the plates (no wire crossing, but changing...](../images/24-electromagnetic-waves-fig-01.png)
*Figure 24.1 — Maxwell's Paradox — Same Ampère Loop, Two Surfaces, Two Answers*

Maxwell noticed something was missing. Faraday's law said a changing magnetic field makes an electric field. By symmetry — and Maxwell took mathematical symmetry seriously as a piece of physical reasoning — a changing electric field should also make a magnetic field. There was no experiment that required this; the effect was too small to measure with the instruments of his day. He added the term anyway, because the equations were inconsistent without it (specifically: in a circuit with a charging capacitor, the old Ampère's law gave different answers depending on which surface you used to compute the magnetic field, which is a contradiction). One added term.

That one addition changed physics. With it, the four equations fit together into a feedback loop: a changing electric field makes a changing magnetic field, which makes a changing electric field a little further along, which makes a changing magnetic field a little further along. The pattern propagates outward. Solve the equations for empty space and they produce a wave equation. The wave's speed comes out to:

$$c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}}.$$

The permittivity of free space $\varepsilon_0$ had been measured from electrostatic experiments — rubbing charged rods and measuring forces. The permeability of free space $\mu_0$ had been measured from the force between current-carrying wires. Neither constant had anything to do with light in any way the experimenters intended. Plug them in:

$$c = \frac{1}{\sqrt{(8.85 \times 10^{-12})(4\pi \times 10^{-7})}} \approx 3.00 \times 10^8 \text{ m/s.}$$

That is the speed of light, to three significant figures. Two constants extracted from two completely different experiments — one from electric sparks, one from compass needles near wires — combine to produce the speed at which light travels. Maxwell's comment to a colleague: this is too close to be coincidence. Light must be an electromagnetic wave.

<!-- → [FIGURE: Maxwell's feedback loop diagram. Left side: "changing E-field" with arrow pointing to right side "changing B-field." Right side: "changing B-field" with arrow pointing back left to "changing E-field." Both arrows also point downward (direction of propagation). Labels: equation 4 (Ampère-Maxwell) over left arrow, equation 3 (Faraday) over right arrow. Caption: The feedback loop at the heart of electromagnetic waves. Faraday's law and the Ampère-Maxwell law produce each other's fields, sustaining a wave that propagates without any medium.] -->

The four equations in plain language:

**Gauss's law for electricity**: Electric field lines start on positive charges, end on negative charges. The constant $\varepsilon_0$ sets how readily space supports electric fields.

**Gauss's law for magnetism**: Magnetic field lines have no ends — they form closed loops. There are no magnetic monopoles.

**Faraday's law**: A changing magnetic field creates an electric field. Every generator ever built runs on this equation.

**Ampère-Maxwell law**: A magnetic field is created by electric current *and* by a changing electric field. The second part is Maxwell's addition. Without it, no electromagnetic waves.

<!-- → [TABLE: Maxwell's four equations — physical content. Columns: equation name, physical law captured, key constant, chapter where derived. Rows: Gauss (electricity) — field lines start/end on charges, ε₀, Chapter 18; Gauss (magnetism) — field lines form closed loops, none, Chapter 22; Faraday — changing B creates E, —, Chapter 23; Ampère-Maxwell — current AND changing E create B, μ₀ and ε₀, Chapters 22 + Maxwell. Caption: Three of the four equations were already known. Maxwell's contribution was the displacement current term in equation 4 and the recognition that together they imply a wave traveling at c = 1/√(μ₀ε₀).] -->

---

## What the wave looks like

An FM transmitter drives electrons up and down a rod at 91.5 MHz — $9.15 \times 10^7$ oscillations per second. The charge separation creates a changing electric field; the oscillating current creates a changing magnetic field. Together they radiate outward as a self-sustaining wave.

![EM wave hitting a solar sail. Energy flux S = (1/μ₀)(E × B) points along propagation. Radiation pressure P = I/c (absorbed) or 2I/c (reflected). Modern solar sails use this for slow but free acceleration in space.](../images/24-electromagnetic-waves-fig-05.png)
*Figure 24.5 — Poynting Vector S = (1/μ₀) E × B — Light Carries Energy and Momentum*

Freeze the wave at one instant and look at two perpendicular axes in space: along one, the electric field oscillates; along the perpendicular axis, the magnetic field oscillates; both fields are perpendicular to the direction of travel. The wave is **transverse** — the fields wiggle sideways, not back and forth along the direction of motion. This is unlike sound, which is longitudinal (air pressure varies along the direction of travel). Maxwell's equations in vacuum allow only transverse electromagnetic waves; trying to construct a longitudinal one leads to a contradiction.

Two structural facts:

**The fields are in phase.** Where $E$ is maximum, $B$ is maximum. Where one is zero, so is the other. They rise and fall together.

**The fields are locked in ratio:**

$$\frac{E}{B} = c$$

at every point, at every instant, in vacuum. A "strong" electric field of 1000 V/m comes paired with a magnetic field of $B = E/c = 1000/(3 \times 10^8) = 3.3 \times 10^{-6}$ T — a few microteslas. The magnetic field looks tiny in SI units, but here is the thing: the energy density in the two fields is *equal*. The electric and magnetic fields carry exactly half the wave's energy each. The apparent numerical asymmetry is a unit artifact.

<!-- → [FIGURE: 3D wave diagram. Three perpendicular axes: x (propagation direction, right), y (E-field oscillation, up/down), z (B-field oscillation, in/out of page). Sinusoidal E-field shown in y-z plane as vertical oscillation. Sinusoidal B-field shown in x-z plane as perpendicular oscillation. Both waves in phase. Speed c arrow along x-axis. Caption: An electromagnetic wave. E and B are perpendicular to each other and to the direction of propagation. They oscillate in phase; at every point E/B = c. The wave carries equal energy in both fields.] -->

### What sets the antenna size

The most efficient antenna for a given frequency has a length around $\lambda/2$ — the half-wave dipole. This is why antenna sizes scale directly with wavelength. A 540 kHz AM station (wavelength $\sim 556$ m) needs a transmitting antenna nearly a quarter-kilometer tall. A 91.5 MHz FM station ($\lambda \approx 3.28$ m) uses a tower with a $\sim 1.6$ m dipole at the top. A 1.9 GHz cell phone signal ($\lambda \approx 16$ cm) fits an antenna inside a phone case. The physics is the same; the engineering is completely different at each scale.

<!-- → [TABLE: Half-wave dipole lengths for common frequencies. Columns: application, frequency, wavelength λ = c/f, half-wave dipole length λ/2. Rows: AM broadcast (540 kHz, 556 m, 278 m), FM broadcast (91.5 MHz, 3.28 m, 1.64 m), Cell phone (1.9 GHz, 0.158 m, 7.9 cm), Wi-Fi (2.4 GHz, 0.125 m, 6.3 cm), GPS L1 (1.575 GHz, 0.190 m, 9.5 cm). Caption: Half-wave dipole length scales exactly with wavelength. The AM tower is hundreds of meters tall; the phone antenna is centimeters. Same physics, orders of magnitude different engineering.] -->

---

## The electromagnetic spectrum

All of this — radio waves, microwaves, infrared, visible light, ultraviolet, X-rays, gamma rays — is the same wave. Same $c = f\lambda$. Same $E/B = c$. Same Maxwell equations. Different only in frequency, and therefore in wavelength, and therefore in how the wave interacts with matter.

$$c = f\lambda,$$

with $c = 3.00 \times 10^8$ m/s fixed. Higher frequency, shorter wavelength; they are inversely proportional, their product always $c$.

![Horizontal spectrum showing wavelength (λ) and frequency (f) from radio (10³ m, kHz) through microwaves, infrared, visible (380–700 nm rainbow band), ultraviolet, X-rays, to gamma rays (10⁻¹⁵ m, 10²³ Hz). Photon energy in eV...](../images/24-electromagnetic-waves-fig-04.png)
*Figure 24.4 — Electromagnetic Spectrum — Radio to Gamma Rays Across 18 Orders of Magnitude*

<!-- → [TABLE: The electromagnetic spectrum. Columns: band name, frequency range (Hz), wavelength range, typical source, typical application. Rows: Radio/ELF (<10⁹ Hz, >30 cm, AC currents/lightning, broadcast radio/submarine communication), Microwave (10⁹–10¹² Hz, 1mm–30cm, magnetrons/thermal emission, radar/cooking/Wi-Fi), Infrared (10¹²–4×10¹⁴ Hz, 750nm–1mm, hot objects/atomic vibrations, thermal imaging/remote controls), Visible (4×10¹⁴–8×10¹⁴ Hz, 380–750nm, electronic transitions in atoms, vision/photography), Ultraviolet (8×10¹⁴–3×10¹⁶ Hz, 10–400nm, hotter stars/arc lamps, sterilization/sunburn), X-ray (3×10¹⁶–3×10¹⁹ Hz, 10pm–10nm, inner-shell transitions/bremsstrahlung, medical imaging/crystallography), Gamma (>3×10¹⁹ Hz, <10pm, nuclear decay/particle annihilation, cancer treatment/PET scans). Caption: The electromagnetic spectrum is one physics at different frequencies. The band names record the history of discovery, not physical discontinuities.] -->

The boundaries between bands are conventional, not physical. A 10 nm photon from an unusually hot star is called "ultraviolet"; the same-wavelength photon from a medical device is called a "soft X-ray." There is no physical difference. What changes across the spectrum is not the wave equations but how the wave interacts with matter — which is a quantum mechanical question we will reach in Chapter 29.

Three rules of thumb hold *most* of the time:

**Rule 1: Higher frequency means more penetrating.** Visible light is stopped by skin. X-rays are not. Gamma rays are not.

**Rule 2: Higher frequency carries more information per second.** This is why fiber-optic networks (operating at near-infrared frequencies) carry many orders of magnitude more data than AM radio.

**Rule 3: Shorter wavelength means finer resolvable detail.** An ultraviolet microscope sees finer structure than a visible-light one. The wavelength sets the diffraction limit on resolution.

These rules have exceptions — MRI machines operate at radio frequencies but resolve millimeter detail because of magnetic resonance tricks rather than pure diffraction physics. But as organizing principles for why we use each band for what we use it for, they are reliable.

---

## How much energy does a wave carry?

The intensity of an electromagnetic wave — power per unit area — is:

$$I_\text{ave} = \frac{c\varepsilon_0 E_0^2}{2},$$

where $E_0$ is the peak electric field strength. Equivalent forms:

$$I_\text{ave} = \frac{c B_0^2}{2\mu_0} = \frac{E_0 B_0}{2\mu_0}.$$

The factor of $1/2$ is time-averaging: the actual intensity oscillates between 0 and $c\varepsilon_0 E_0^2$ at twice the wave frequency, and the average is half the peak.

**A worked example: microwave oven.** A 1.00 kW microwave oven concentrates its power onto a $30.0 \text{ cm} \times 40.0 \text{ cm} = 0.120 \text{ m}^2$ tray.

Average intensity:

$$I_\text{ave} = \frac{P}{A} = \frac{1000}{0.120} = 8.33 \times 10^3 \text{ W/m}^2.$$

For comparison, sunlight at noon delivers about $1000 \text{ W/m}^2$. The inside of a microwave is roughly eight times more intense.

Peak electric field:

$$E_0 = \sqrt{\frac{2I_\text{ave}}{c\varepsilon_0}} = \sqrt{\frac{2(8.33\times10^3)}{(3.00\times10^8)(8.85\times10^{-12})}} \approx 2.51 \times 10^3 \text{ V/m.}$$

Peak magnetic field:

$$B_0 = \frac{E_0}{c} = \frac{2510}{3.00\times10^8} \approx 8.35 \times 10^{-6} \text{ T.}$$

About $8\,\mu\text{T}$ — twenty times Earth's surface magnetic field, but far from the dielectric breakdown threshold of air ($\sim 3 \text{ MV/m}$ for electric field). The numbers are physically sensible for a kitchen appliance.

<!-- → [FIGURE: Energy density comparison diagram. Two bars for the microwave oven example, equal height. Left bar: "Electric field energy density u_E = ½ε₀E₀²." Right bar: "Magnetic field energy density u_B = B₀²/2μ₀." Both labeled with numerical value ~3.5×10⁻⁵ J/m³. Caption: In an electromagnetic wave, the electric and magnetic fields carry equal energy. Although B₀ is numerically small (microteslas vs. thousands of V/m), the energy densities are identical. The apparent asymmetry is a consequence of SI units, not physics.] -->

---

## One spectrum, one physics

Pull back and look at what Maxwell's synthesis accomplished. Before 1865, physicists talked about "radiant heat," "actinic rays," "visible light," and various other names as if they were fundamentally different things. Maxwell showed they were all the same — a single wave, obeying four equations, propagating at $c$, with perpendicular in-phase fields locked at ratio $E/B = c$.

Hertz made the case experimentally. Penzias and Wilson, in 1964, found Maxwell's waves coming from every direction in the sky at the same intensity — the microwave background radiation left over from the Big Bang, at a temperature of 2.7 K. They were listening for noise in a Bell Labs radio antenna; they discovered one of the most important facts in cosmology. The same equations that describe your microwave oven describe the structure of the early universe.

The deep lesson: **the names are taxonomy, not physics.** Radio, infrared, visible, ultraviolet, X-ray, gamma — these record who discovered each band and what technology first detected it. The underlying phenomenon is one self-propagating wave of electric and magnetic fields, predicted from a symmetry argument, confirmed by a spark crossing an empty room, present everywhere in the universe.

**A synthesis example: designing an FM radio link.**

Station at 91.5 MHz broadcasts 50 kW over a hemisphere. Wavelength: $\lambda = c/f = 3.00\times10^8 / 91.5\times10^6 \approx 3.28$ m. Half-wave dipole antenna length: $\sim 1.64$ m. Intensity at 10 km:

$$I = \frac{P}{2\pi r^2} = \frac{50{,}000}{2\pi(10{,}000)^2} \approx 8.0 \times 10^{-5} \text{ W/m}^2.$$

Peak electric field at receiver:

$$E_0 = \sqrt{\frac{2I}{c\varepsilon_0}} = \sqrt{\frac{2(8.0\times10^{-5})}{(3.00\times10^8)(8.85\times10^{-12})}} \approx 0.25 \text{ V/m.}$$

A quarter volt per meter — small, but entirely detectable by tuned electronics. That signal is now spreading outward at $3\times10^8$ m/s. It will reach the orbit of Mars about 12 minutes from now. It will reach Proxima Centauri — the nearest star — in 4.2 years. The intensity at Proxima will be far too small to detect, but the wave is still there. Maxwell's equations have no "stop" condition. Once launched, the wave propagates until it's absorbed.

---

## Exercises

### Warm-up

**24.1** *(LO 1)* In one sentence each, state the physical phenomenon each of Maxwell's four equations captures.

**24.2** *(LO 3)* Calculate: (a) wavelength of a 540 kHz AM signal; (b) wavelength of a 2.45 GHz microwave; (c) frequency of 600 nm orange light; (d) wavelength of a $5\times10^{18}$ Hz X-ray.

**24.3** *(LO 2)* Peak electric field of an EM wave is 300 V/m. Find the peak magnetic field.

**24.4** *(LO 4)* A 1.0 mW laser pointer over a $1.0\text{ mm}^2$ beam. Average intensity in W/m²?

### Application

**24.5** *(LO 3)* Half-wave dipole length for a 27 MHz CB radio transmitter? Compare to a typical car antenna.

**24.6** *(LO 4)* A 700 W microwave oven focused on a 20.0 cm diameter circle. (a) Average intensity. (b) Peak electric field. (c) Peak magnetic field.

**24.7** *(LO 5)* MRI machines operate near 100 MHz but resolve submillimeter tissue detail. Which of the three rules of thumb appears violated, and what physical mechanism allows it?

**24.8** *(LO 3)* A 50.0 Hz AC power line with peak $E_0 = 13.0\text{ kV/m}$. (a) Wavelength. (b) Peak magnetic field.

### Synthesis

**24.9** *(LO 1, LO 4)* Solar constant: $1361\text{ W/m}^2$. (a) Peak electric field at top of atmosphere. (b) Peak magnetic field. (c) Compare $B_0$ to Earth's surface magnetic field $\sim 5\times10^{-5}$ T.

**24.10** *(LO 3, LO 4)* Pulsed fusion laser: peak electric field $1.00\times10^{11}\text{ V/m}$ for $1.00\text{ ns}$. (a) Peak magnetic field. (b) Intensity. (c) Energy to a $1.00\text{ mm}^2$ spot.

**24.11** *(LO 1, LO 3)* Hertz's 1887 transmitter and receiver were tuned to about 100 MHz. Wavelength? How many wavelengths fit across a 5 m laboratory?

### Challenge

**24.12** *(beyond chapter)* The cosmic microwave background peaks near 1 mm wavelength at $T = 2.725$ K. (a) Convert to frequency. (b) Verify using Wien's law $\lambda_\text{peak} T = 2.898\times10^{-3}\text{ m·K}$. (c) In one paragraph, explain why a microwave oven uses 2.45 GHz rather than the thermal peak frequency of body-temperature water.

**24.13** *(beyond chapter)* Pre-fiber transatlantic phone used HF radio (3–30 MHz); modern fiber uses near-IR (~1550 nm). (a) Bandwidth ratio if you can use ~10% of carrier frequency. (b) Explain qualitatively, using Rule 2, why the switch to optical was inevitable.

---

## LLM Exercise — Chapter 24: Electromagnetic Waves in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** One Logbook entry identifying the EM-wave content of your anchor phenomenon — the radio, microwave, IR, visible, or UV signals it emits, absorbs, or relies on — with a numerical estimate of frequency, wavelength, and (where possible) intensity.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste your 1-sentence description].

For Chapter 24, I want to apply electromagnetic wave physics — Maxwell's equations, the spectrum c = fλ, intensity I = cε₀E₀²/2 — to my phenomenon.

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

Chapter 25 narrows in on visible light and the geometry of how it bends, reflects, and focuses through lenses and mirrors. The Chapter 25 LLM Exercise will ask you to identify a *lens* or *mirror* in your anchor phenomenon and analyze its image-forming behavior.

---

**Tags:** electromagnetic-waves, Maxwell-equations, Hertz-experiment, spectrum, intensity
