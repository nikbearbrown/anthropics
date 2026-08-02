# Chapter 3 — Radiation and Spectra

*A glass prism in 1814, a Munich optician with no university degree, and the discovery that starlight carries its own composition label.*

---

In 1814 Joseph von Fraunhofer was making glass prisms in a Bavarian workshop. He needed a reliable, single-wavelength light source for testing his lenses — a fixed color he could use as a reference. Sunlight, spread through one of his high-quality prisms, produced the usual rainbow. But Fraunhofer had better prisms than anyone before him, and he spread the light further. When he looked carefully, he saw something that had never been clearly documented: hundreds of thin dark lines, fixed in position, crossing the rainbow at precise wavelengths.

They were not dust. They were not instrument artifacts. They appeared every time, at the same positions, reproducibly. Fraunhofer catalogued 574 of them and labeled the prominent ones with letters — A, B, C, D, E, F, G, H — a notation astronomers still use. He had no theory of what they were. He measured them, mapped them, and moved on. He died in 1826 at age 39 without ever knowing what he had found.

What Fraunhofer was staring at was a chemical analysis of the Sun's outer atmosphere, encoded in light, available to anyone who looked carefully enough through a piece of glass. The physics that explains those lines — quantum mechanics, atomic energy levels, the interaction of radiation and matter — would take another century to work out fully. But the payoff, when it came, was spectacular: a single spectrum of a star tells you its composition, its surface temperature (by two independent methods that agree), the pressure in its atmosphere, how fast it is moving toward or away from you, and how fast it is rotating. Every bit of that information arrives free of charge with every photon.

This chapter is the theory that made Fraunhofer's dark lines make sense.

---

## What light actually is

There is a genuine puzzle at the center of this chapter, and I want to name it honestly rather than paper over it.

Drop two pebbles into a still pond a few inches apart. The ripples spread, overlap, and produce a pattern of reinforcement and cancellation — bright rings where crests meet, dark rings where crests meet troughs. This is interference, and it is specifically what waves do. Nothing but waves does it.

Now shine two flashlights at a wall. You get more light. Not alternating bright and dark — just more light everywhere. Particles pile up wherever they land.

Light does both things. In Young's double-slit experiment (1803), light produces interference patterns — unmistakably wave behavior. In the photoelectric effect (Einstein, 1905), light kicks electrons out of metal, and the energy of each ejected electron depends on the *frequency* of the light, not the brightness. Turn up the brightness and more electrons are ejected, but each carries the same energy. Lower the frequency below a threshold and no electrons come out at all, no matter how bright the beam. This is particle behavior — energy arriving in discrete packets, each packet sized by frequency, not by intensity.

The working resolution from quantum mechanics: use the wave picture to describe how light propagates through space, and the photon picture to describe how light exchanges energy with matter. Both descriptions are needed. Neither is complete alone. They are joined by one equation:

$$E = hf$$

Every photon carries energy $E$ proportional to its frequency $f$. Planck's constant $h \approx 6.63 \times 10^{-34}$ J·s is tiny, which is why individual photon energies are imperceptible at everyday brightness levels — a 100-watt bulb emits around $10^{20}$ photons per second, and you never notice the granularity. But the proportionality is real and consequential: ultraviolet photons carry enough energy per packet to break chemical bonds, including in DNA. Radio photons carry so little energy they pass through tissue without depositing anything noticeable.

Maxwell worked out in the 1860s that radio waves, microwaves, infrared, visible light, ultraviolet, X-rays, and gamma rays are all the same phenomenon — oscillating electric and magnetic fields propagating through space — distinguished only by wavelength. All travel at the same speed $c \approx 3.00 \times 10^8$ m/s in vacuum. The relation

$$c = \lambda f$$

locks wavelength and frequency together: short wavelengths mean high frequencies, which mean high-energy photons. Visible light occupies a narrow window from about 400 nm (violet) to 700 nm (red) — roughly one octave of frequency. The full electromagnetic spectrum spans twenty orders of magnitude. Everything we call "color" is a single octave within that span.

<!-- → [INFOGRAPHIC: The electromagnetic spectrum from radio (10⁶ m) to gamma rays (10⁻¹² m), with frequency increasing left to right, the visible band (~400–700 nm) highlighted as a narrow sliver, and the energy per photon increasing left to right with notable examples: radio (cell phones, 10⁻⁷ eV), microwave (3 cm, CMB), infrared (room temperature objects), visible (human eye), UV (DNA damage), X-ray (medical imaging), gamma (nuclear decays)] -->

![Horizontal log scale of frequency from radio to gamma. The seven bands span 10²⁰. Human vision occupies one octave near the middle; astronomy uses all of it.](../images/03-radiation-and-spectra-fig-02.png)
*Figure 3.2 — Electromagnetic Spectrum: 20 Orders of Magnitude*

One more piece before we can talk about stars. Light from a point source spreads outward as an expanding sphere. The total energy is fixed; the surface area at distance $d$ grows as $4\pi d^2$, so the energy per unit area at an observer — the intensity — falls as:

$$I \propto \frac{1}{d^2}$$

This is the inverse-square law. A star identical to the Sun but at the distance of Alpha Centauri (~270,000 AU) appears $(270{,}000)^2 \approx 7 \times 10^{10}$ times fainter than the Sun. Seventy billion times. That is what we work with. Every measurement of a distant star is made from an almost negligibly small sample of the light it emits, with most of the photons having gone in other directions. It is remarkable that we learn anything at all.

![A point source radiates outward. The same total energy passes through nested spheres at distances r, 2r, 3r — but each sphere's area grows as r². Intensity therefore falls as 1/r².](../images/03-radiation-and-spectra-fig-03.png)
*Figure 3.3 — Inverse-Square Law: Why Distant Stars Are Faint*

<!-- → [CHART: Two-panel diagram — left panel shows a point source radiating outward with concentric spheres at distances d, 2d, 3d, shading showing the same energy spread over 1×, 4×, 9× the area; right panel shows a log-log plot of intensity vs. distance with slope −2, confirming the inverse-square relationship — student should see why a star 10× further away appears 100× fainter] -->

---

## What temperature does to light

Every object radiates. Not just glowing ones — every object, all the time, by virtue of having a temperature above absolute zero. Your body radiates infrared (peak near 9.4 µm) at roughly 100 watts. A metal poker heated in a fire starts in the infrared, then glows red, then orange, then yellow, then white — not because different materials glow differently but because temperature shifts the peak of the emission toward shorter wavelengths.

The idealized version of this — an object that absorbs and re-emits all incident radiation perfectly — is called a **blackbody**. Stars are not perfect blackbodies, but they are close enough that the theory works well.

In 1900 Max Planck worked out the exact shape of the blackbody spectrum at any temperature. To make the derivation work mathematically, he was forced to assume that energy came in discrete chunks: $E = hf$, the same equation we just used for photons. Planck was uncomfortable with this assumption. He called it a mathematical trick and spent years trying to remove it. It could not be removed. The trick was physics. Planck had accidentally founded quantum mechanics while trying to solve what seemed like a classical problem in thermodynamics.

We need two consequences of the full Planck spectrum.

**Wien's displacement law.** The wavelength at which a blackbody's emission is strongest:

$$\lambda_{\text{peak}} = \frac{b}{T}, \quad b \approx 2.9 \times 10^{-3} \text{ m·K}$$

where $T$ is the temperature in Kelvin. The Sun, at $T \approx 5{,}772$ K, peaks near $\lambda_{\text{peak}} \approx 500$ nm — green-yellow, the center of the visible band. This is not a coincidence: our eyes evolved in sunlight and are most sensitive where the available illumination is strongest. Sirius ($T \approx 10{,}000$ K) peaks at 290 nm, in the ultraviolet — invisible, but detectable with the right instruments. A cool red dwarf at 3,000 K peaks near 970 nm, just outside what the eye can see. Measure where a star's spectrum peaks; you know its surface temperature without setting foot anywhere near it.

**Stefan-Boltzmann law.** The total power radiated by a blackbody of surface area $A$ at temperature $T$:

$$P = \sigma A T^4, \quad \sigma \approx 5.67 \times 10^{-8} \text{ W m}^{-2} \text{K}^{-4}$$

The $T^4$ dependence is not intuitive and it matters enormously. Double the temperature and total radiated power increases by a factor of sixteen. The Sun emits $3.83 \times 10^{26}$ W continuously. The fourth-power law also resolves a puzzle that confused astronomers for decades: how can a red giant — cool surface, only around 3,500 K — outshine a much hotter white dwarf? The lower temperature reduces emission per unit area, but the surface area of a red giant is hundreds of millions of times larger than the Sun's. The $A$ factor wins. From the luminosity and temperature of a star, both measurable in principle from its spectrum and its apparent brightness, you can recover the physical radius of an object you will never visit.

<!-- → [CHART: Three Planck blackbody curves on a single set of log-scale axes — 3,000 K (red dwarf), 5,800 K (Sun), 10,000 K (A-type star) — intensity vs. wavelength from 100 nm to 3,000 nm; visible band (400–700 nm) highlighted; each curve's peak labeled with temperature and wavelength; student should see peak shifting left and total area growing sharply with temperature] -->

![Three blackbody curves at 3000 K, 5800 K, and 10000 K. As temperature rises, the peak shifts toward shorter wavelengths (Wien) and the total area grows as T⁴ (Stefan-Boltzmann). The visible band is highlighted.](../images/03-radiation-and-spectra-fig-04.png)
*Figure 3.4 — Planck Curves: Wien's Law and Stefan-Boltzmann*

---

## What atoms do to light

Now we can explain Fraunhofer's dark lines. The mechanism requires one fact about atomic structure.

In the early twentieth century, physicists established that electrons in atoms do not occupy a continuous range of energies. They occupy **discrete energy levels** — specific allowed values with nothing in between. Hydrogen, the simplest case: the electron can sit at the ground state ($-13.6$ eV), the first excited state ($-3.4$ eV), the second excited state ($-1.5$ eV), and so on. Not at $-2.0$ eV. Not at $-1.9$ eV. The levels are fixed by the physics of the atom — only certain electron wave patterns fit around a proton without destructively interfering with themselves, the same way only certain wavelengths fit cleanly on a guitar string of fixed length. The atom is a quantum resonator with a specific set of resonant frequencies.

The consequence for light follows immediately. When an electron drops from a higher level to a lower one, it releases the energy difference as a single photon. Since the energy gap between any two specific levels is always the same exact number, the photon always has the same frequency, hence the same wavelength. Hydrogen emits at 656.3 nm ($n=3 \to 2$, deep red), 486.1 nm ($n=4 \to 2$, blue-green), 434.0 nm ($n=5 \to 2$, violet), and a handful of other specific wavelengths. Not approximately — exactly, because the energy levels are what they are. This spectrum is hydrogen's fingerprint. No other element has the same set of levels; every element has a unique pattern.

![Left: hydrogen's energy levels and the Balmer transitions. Right: light from the photosphere passes through cooler outer gas; atoms absorb at exactly the wavelengths of those transitions; the spectrum the observer see...](../images/03-radiation-and-spectra-fig-05.png)
*Figure 3.5 — Atomic Energy Levels: How Absorption Lines Form*

The process runs in reverse: a photon of exactly the right energy can be absorbed, kicking an electron from a lower level to a higher one. Absorption happens at the same wavelengths as emission, for the same reason — same energy gaps.

<!-- → [IMAGE: Energy level diagram for hydrogen — horizontal lines at n=1 (−13.6 eV), n=2 (−3.4 eV), n=3 (−1.5 eV), n=4 (−0.85 eV), n=∞ (0 eV, ionization); downward arrows showing the Balmer series transitions n=3→2 (656.3 nm, red), n=4→2 (486.1 nm, blue-green), n=5→2 (434.0 nm, violet); upward arrows of same color showing absorption of same wavelengths; caption should make clear that emission and absorption are the same transitions in opposite directions] -->

Now Fraunhofer's dark lines make sense. The Sun's deep interior is hot and dense enough to produce a continuous spectrum — every wavelength, an unbroken rainbow. That light travels outward through the Sun's cooler outer atmosphere. Atoms in the cooler gas absorb photons at their characteristic wavelengths and re-emit them in random directions; most of the re-emitted photons scatter sideways rather than continuing toward Earth. The light that reaches us is depleted at precisely those characteristic wavelengths. The result: a continuous spectrum crossed by thin dark gaps at the absorption wavelengths of every element present in the solar atmosphere.

![The solar spectrum, with the prominent dark absorption lines Joseph von Fraunhofer cataloged in 1814. Each line is the fingerprint of an element in the Sun's outer atmosphere.](../images/03-radiation-and-spectra-fig-01.png)
*Figure 3.1 — Fraunhofer's Dark Lines (1814)*

The dark line at 656.3 nm is hydrogen. The prominent pair near 393 and 397 nm is ionized calcium (Fraunhofer's H and K lines). The line at 589 nm is sodium (Fraunhofer's D). Iron, magnesium, nickel — dozens of elements, each identified by matching the pattern of dark lines against laboratory measurements of the same elements on Earth. The same atomic physics, confirmed in the lab, readable in starlight.

<!-- → [IMAGE: Simulated solar spectrum from ~390 nm to 700 nm showing continuous rainbow background with dark Fraunhofer absorption lines; major lines labeled: H and K (Ca II) at 393/397 nm, G-band (CH/Fe) at 430 nm, H-beta (H) at 486 nm, Mg b triplet at 517–518 nm, D (Na) at 589 nm, H-alpha (H) at 656 nm; caption should note that each dark line is the signature of a specific atom or ion absorbing photons in the solar atmosphere] -->

Composition is only the beginning of what a spectrum contains.

**Temperature** — by two independent methods. The first is Wien's law: measure where the continuous spectrum peaks. The second uses the spectral lines themselves. At different temperatures, the same element is present in different ionization states — one, two, three electrons stripped away — and different states have different characteristic lines. At 6,000 K, hydrogen is mostly neutral; its Balmer absorption lines (the red, blue-green, and violet lines from transitions to level 2) are prominent. At 20,000 K, hydrogen is mostly ionized and its lines weaken. At 50,000 K, helium is ionized and *its* lines dominate. The Saha equation (1920) quantifies exactly how much of each element is in each ionization state at any temperature. Compare the observed line strengths across ionization states; recover the temperature. Then compare that temperature to the Wien-law temperature. The two methods agree. That agreement is not guaranteed by the theory — it is a test of the theory, and the theory passes.

**Pressure.** In dense gas, atoms collide frequently. Each collision interrupts an atom mid-absorption, briefly perturbing the energy levels and allowing absorptions at wavelengths slightly off the central value. This pressure broadening smears the otherwise razor-sharp absorption line into a broader feature. Wide lines mean dense atmosphere; narrow lines mean thin atmosphere. Giant and supergiant stars have diffuse outer envelopes; their spectral lines are sharp. Main-sequence dwarfs have denser atmospheres; their lines are broader. A spectrum distinguishes a supergiant from a dwarf of the same surface temperature.

![A single stellar spectrum yields temperature (from the continuous shape), radial velocity (from Doppler), composition (from line identification), surface gravity (from line sharpness), and rotation (from symmetric bro...](../images/03-radiation-and-spectra-fig-07.png)
*Figure 3.7 — Reading a Star from One Spectrum*

**Radial velocity.** When a source of waves moves toward you, successive wave crests arrive more frequently — the wavelength is compressed, shifted toward blue. When it moves away, the wavelength is stretched, shifted toward red. For motion at speeds small compared to light, the non-relativistic Doppler formula gives the shift:

![The Hα absorption line (rest wavelength 656.3 nm) at three states of source motion: stationary, receding (redshifted), approaching (blueshifted). The shift in wavelength gives the radial velocity through Δλ/λ = v/c.](../images/03-radiation-and-spectra-fig-06.png)
*Figure 3.6 — Doppler Shift in a Spectral Line*

$$\frac{\Delta\lambda}{\lambda} = \frac{v}{c}$$

If hydrogen's 656.3 nm line appears at 656.5 nm, $\Delta\lambda = 0.2$ nm, and $v = c \times 0.2/656.3 \approx 91$ km/s, receding. The direction — blueshift or redshift — tells you which way the source is moving along your line of sight. The Milky Way's rotation, the motion of galaxies in clusters, the expansion of the universe — all measured by Doppler shifts in spectra.

**Rotation.** One limb of a rotating star moves toward you; the other moves away. Both halves of the disk are contributing light simultaneously. The Doppler shift from one limb blueshifts its absorption features slightly; the shift from the other limb redshifts the same features. The net result is that what would otherwise be a single narrow line is broadened symmetrically — the line's width encodes the star's equatorial rotation speed.

<!-- → [IMAGE: Three versions of the same spectral line side by side — left: narrow, unbroadened (no rotation, low pressure); center: symmetrically broadened (rotational broadening, both limbs contributing); right: asymmetrically shifted (Doppler shift from radial velocity, whole line displaced); caption should make clear these are three different physical effects that can be distinguished by the shape and position of the line] -->

A single spectrum of a star that took years to arrive, produced by a source you cannot visit or perturb, contains all of this at once.

---

## Reading a spectrum

Let me work through what this looks like in practice.

Suppose you observe a star and measure: continuous spectrum peaks at 290 nm; hydrogen-alpha line appears at 656.5 nm instead of its rest wavelength of 656.3 nm; ionized helium lines are prominent; neutral calcium lines are absent; lines are narrow with slight symmetric broadening.

**Temperature (Wien's law).** $T = b/\lambda_{\text{peak}} = (2.9 \times 10^{-3})/(290 \times 10^{-9}) = 10{,}000$ K.

**Temperature (ionization).** Strong ionized helium at 10,000 K is borderline — helium ionization requires roughly 25,000 K to produce strong He II lines, while He I (neutral helium) appears from about 8,000 K to 20,000 K. A spectrum showing prominent hydrogen Balmer lines and He I but no He II is characteristic of an A-type star near 10,000 K. The two temperature methods agree at the order of magnitude; the ionization pattern is consistent.

**Radial velocity.** $\Delta\lambda = 0.2$ nm at $\lambda_0 = 656.3$ nm gives $v = (0.2/656.3) \times 3 \times 10^5 \approx 91$ km/s, receding (shift to longer wavelength).

**Atmosphere density.** Narrow lines mean low pressure — a thin outer atmosphere, characteristic of giants and supergiants rather than main-sequence dwarfs.

**Rotation.** Slight symmetric broadening means moderate equatorial rotation, tens of km/s.

From light that crossed interstellar space: a 10,000 K giant, receding at ~91 km/s, with a thin atmosphere and moderate rotation. If we also know its distance (from Chapter 7's distance ladder), Stefan-Boltzmann delivers the physical radius. A star we know in reasonable detail without going anywhere near it.

---

## The thing Fraunhofer missed, and what it cost Cecilia Payne-Gaposchkin

Fraunhofer had no theory, so his lines were a curiosity. By the 1920s the theory existed, and Cecilia Payne-Gaposchkin used it. In her 1925 doctoral thesis, she applied the Saha equation to the hydrogen and other spectral lines of dozens of stars and arrived at a clear conclusion: stars are overwhelmingly made of hydrogen. Not roughly like Earth's composition — *overwhelmingly*. Hydrogen was orders of magnitude more abundant than anything else.

This was so contrary to the prevailing assumption — that stars were like the Earth, only hotter — that her advisor, Henry Norris Russell, pressured her to hedge. She added a line calling the result "almost certainly not real." A few years later, Russell himself repeated the analysis and arrived at the same conclusion. He then published it and received much of the credit. Payne-Gaposchkin was later recognized as having been right; she became the first woman to chair a department at Harvard.

The story matters for the same reason the GW170817 story in Chapter 1 matters. Good evidence and correct theory are not always enough. The social machinery of science — who gets believed, who gets pressured to doubt their own conclusions — is part of the history. The spectroscopic method was right. The result was right. The theory of atomic energy levels was right. It still required someone willing to follow the evidence to an unpopular conclusion, and someone with institutional power who was not.

---

## What would change my mind

The mechanism in this chapter rests on one universality claim: the energy levels of hydrogen — and every other atom — are the same everywhere in the observable universe. We know this because distant-galaxy spectral lines appear at exactly the expected wavelengths, shifted only by the cosmological redshift, never at wrong wavelengths that would indicate altered atomic physics. The relevant constraint is on the fine-structure constant α, which sets the scale of electromagnetic interactions and therefore the scale of atomic energy levels. Current bounds put the variation in α over the last 10 billion years at less than about one part in $10^7$ — a number that has been actively contested (Webb et al., 2011, found a hint of variation; follow-up analyses have not confirmed it). A reproducible, systematic measurement of fine-structure-constant variation with cosmic time, with all instrumental effects ruled out, would require rewriting this chapter and most of cosmology with it. Watch the literature on this; it is genuinely open.

---

## Exercises

**Warm-up.** Light A has wavelength 400 nm; light B has wavelength 700 nm. (a) Which has higher frequency? Show the calculation using $c = \lambda f$. (b) Which carries more energy per photon? Use $E = hf$. (c) By what factor does the energy per photon of A exceed that of B? *(Tests: wave-photon relationships, $E = hf$ and $c = \lambda f$.)*

**Warm-up.** Your skin temperature is approximately 307 K. (a) Use Wien's law to find the peak wavelength of your body's thermal emission. (b) In what part of the electromagnetic spectrum does this fall? (c) Why can you not see another person's body heat with the naked eye, even though they are radiating continuously? *(Tests: Wien's law, electromagnetic spectrum regimes.)*

**Warm-up.** Two stars have the same surface temperature but one has twice the radius of the other. (a) How does the surface area of the larger star compare to the smaller? (b) Use Stefan-Boltzmann to find the ratio of their luminosities. (c) If both are the same distance from Earth, which appears brighter and by how much? *(Tests: Stefan-Boltzmann, area scaling.)*

**Application.** A star's continuous spectrum peaks at 145 nm. (a) Calculate its surface temperature using Wien's law. (b) In what spectral class does this place the star (O, B, A, F, G, K, or M)? (c) Would hydrogen Balmer absorption lines be strong or weak in this star's spectrum — and why? *(Tests: Wien's law, spectral classification, ionization reasoning.)*

**Application.** The calcium H line has a rest wavelength of 396.8 nm. A distant galaxy shows this line at 423.0 nm. (a) Calculate the recession velocity using the Doppler formula. (b) Express this as a fraction of the speed of light. (c) Is the non-relativistic Doppler formula valid here? What condition must hold for it to apply? *(Tests: Doppler formula, validity conditions.)*

**Application.** Star X and Star Y have identical surface temperatures. Star X shows very narrow spectral lines; Star Y shows broad lines of the same elements. (a) What does this difference in line width tell you about each star's atmosphere? (b) Which star is more likely to be a supergiant, and why? (c) Name the physical process responsible for the line broadening in Star Y. *(Tests: pressure broadening, giant vs. dwarf luminosity classification.)*

**Synthesis.** A star shows the following spectral features: continuous emission peaks at 970 nm; hydrogen Balmer lines are weak; strong neutral titanium oxide (TiO) molecular bands appear. (a) Estimate the surface temperature from the Wien peak. (b) Explain why hydrogen lines are weak at this temperature (use ionization reasoning, not just "it's cool"). (c) Why do molecular bands appear in cool stellar spectra but not hot ones? (d) What spectral class is this star? *(Tests: Wien's law, Saha equation reasoning, spectral classification, why molecules survive in cool atmospheres.)*

**Synthesis.** You observe two stars with the same apparent brightness. Star A has a surface temperature of 3,000 K and is 10 pc away. Star B has a surface temperature of 30,000 K and is also 10 pc away. (a) By what factor does their luminosity differ, considering temperature alone (same radius assumed)? (b) Given the same apparent brightness, what must be true about their actual radii? (c) Use $L = 4\pi R^2 \sigma T^4$ to find the ratio $R_A / R_B$. *(Tests: Stefan-Boltzmann, inverse-square law, radius inference from observables.)*

**Challenge.** The Saha equation predicts that the fraction of hydrogen in the first excited state (from which Balmer absorption occurs) peaks around 9,000–10,000 K. Below this temperature there is too little thermal energy to populate the excited state; above it, hydrogen becomes ionized and the neutral Balmer absorbers disappear. (a) In plain language, explain why both conditions reduce the strength of hydrogen Balmer lines — even though hydrogen is present at both temperatures. (b) Sketch (no calculation required) the expected strength of Balmer lines as a function of stellar temperature from 3,000 K to 50,000 K. What shape does the curve have and why? (c) Cecilia Payne-Gaposchkin used this argument — that weak Balmer lines do not mean little hydrogen — to conclude that stars are mostly hydrogen. Explain in two sentences why her critics' intuition (weak lines = little hydrogen) was wrong. *(Tests: Saha equation reasoning, ionization vs. abundance, Payne-Gaposchkin result.)*

---

## LLM Exercises

### Build the Planck-curve simulator (`03-planck-curves.html`)

With `CLAUDE.md` and `DESIGN.md` loaded:

> **Show.** Three Planck blackbody curves on a single set of axes — intensity vs. wavelength in nm — for temperatures controlled by a slider from 2,000 K to 30,000 K. The visible band (400–700 nm) is highlighted with a colored vertical strip behind the curves. Each curve's peak is annotated with its temperature and peak wavelength.
>
> **Say.** Build an interactive D3 v7 visualization. Compute the Planck spectral radiance $B_\lambda(T) = (2hc^2/\lambda^5) \cdot 1/(e^{hc/\lambda k_B T} - 1)$ on a wavelength grid from 100 nm to 3,000 nm. Display three temperature-labeled curves: a cool reference (3,000 K), a user-controlled middle slider, and a hot reference (10,000 K). Mark each peak with a dashed vertical line and a numeric label. Use a logarithmic intensity axis so all three curves are visible simultaneously.
>
> **Constrain.** D3 v7 only. No external blackbody libraries. Filename: `03-planck-curves.html`. Slider value updates the middle curve in real time.
>
> **Verify.** (a) Set the slider to 5,800 K; the peak should land at ~500 nm. (b) Set it to 10,000 K; the peak should jump to ~290 nm. (c) Set it to 2,000 K; the peak should leave the visible band entirely, landing near 1,450 nm in the near-infrared.

### Exploration

- Increase the slider temperature from 3,000 K to 10,000 K and watch where the peak moves. Confirm by reading the annotation that $\lambda_{\text{peak}} \times T$ stays constant at $\approx 2.9 \times 10^{-3}$ m·K. You have just verified Wien's law numerically.
- At what slider temperature does the curve's value at 656 nm peak? (This is the temperature at which the H-alpha line is strongest in stellar atmospheres — a hint at why A-type stars show the most prominent hydrogen features.)
- Compare the area under the curve from 2,000 K to 4,000 K. By the Stefan-Boltzmann law it should grow by a factor of $(4{,}000/2{,}000)^4 = 16$. Does your simulation reproduce this when you numerically integrate?

### Bridge to Chapter 4

> **Show.** I now know how to read a spectrum. Time to read the spectra of objects in our own solar system — and learn what those readings revealed about how the solar system formed.
>
> **Say.** Modify the simulator: add a second panel showing the reflectance spectra of three real solar-system bodies — the Moon, Mars, and a typical C-type asteroid — at visible wavelengths, with absorption bands labeled.
>
> **Verify.** Mars' reflectance dips in the blue (it is red because it absorbs blue, not because it emits red). The Moon's spectrum is nearly flat across the visible. The C-type asteroid is dark across the band — that flatness and darkness is what "carbonaceous" looks like in light.

Save as `03b-solar-system-reflectance-preview.html`. Lead-in to Chapter 4 — *The Solar System*.

---

**Tags:** electromagnetic spectrum, photons, blackbody, Wien's law, Stefan-Boltzmann, spectral lines, Fraunhofer, Doppler shift, Payne-Gaposchkin, spectroscopy
