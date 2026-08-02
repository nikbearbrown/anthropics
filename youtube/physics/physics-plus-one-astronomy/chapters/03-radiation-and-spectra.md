# Chapter 3 — Radiation and Spectra

*A glass prism in 1814, a Munich optician with no university degree, and the discovery that starlight carries its own composition label.*

---

## Suggested titles

1. Radiation and Spectra
2. How Light Tells You Everything
3. Reading the Universe from a Distance

## TL;DR

Light arriving from a star encodes its source's composition, temperature, density, motion, and rotation — all at once, in a pattern of bright and dark lines that follows from the quantization of atomic energy levels. Spectroscopy is the entire reason astronomy is a quantitative science instead of a survey of pretty pictures.

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Understand)** State the wave-particle relationship for light using $E = hf$ and $c = \lambda f$, and describe in plain language why both descriptions are needed.
2. **(Apply)** Use Wien's displacement law to convert a measured spectral peak into a surface temperature, and Stefan-Boltzmann ($P = \sigma A T^4$) to relate temperature and area to luminosity.
3. **(Apply)** Use the non-relativistic Doppler formula $\Delta\lambda/\lambda = v/c$ to extract a radial velocity from a measured wavelength shift.
4. **(Analyze)** Read a stellar spectrum and extract: composition, surface temperature (two ways), radial velocity, atmospheric density, and rotation.
5. **(Apply)** Build an interactive D3 simulation of Planck blackbody curves at variable temperature, with the visible band highlighted.

**Prerequisites.** Chapter 2 (celestial coordinates, what the sky actually shows). Basic algebra; small-angle and small-fractional reasoning. No quantum mechanics — the relevant facts are stated where needed.

---

## Opening case: Fraunhofer's dark lines, Munich, 1814

In 1814 Joseph von Fraunhofer was making glass prisms in a Bavarian workshop. He needed a reliable light source for testing his lenses — a single, fixed wavelength would let him measure how his glass bent light. Sunlight, dispersed through a high-quality prism, produced a beautiful broad rainbow. Spread it across enough degrees, look closely, and Fraunhofer saw something nobody had quite seen before: hundreds of thin dark lines, at fixed positions in the spectrum, every time he looked.

They were not dust. They were not artifacts of the prism. They were features of the light itself. Fraunhofer catalogued 574 of them, labeling the prominent ones with letters — the "Fraunhofer lines" A, B, C, D, E, F, G, H — that astronomers still use. He had no theory of what they were. He died in 1826 at 39 without knowing.

What Fraunhofer was looking at was a chemical analysis of the Sun's outer atmosphere, printed in light, delivered for free, requiring only a piece of glass to read. He could not know that. The atomic theory that would make sense of the lines did not yet exist. The mechanism — that atoms absorb light at specific, quantized wavelengths — would take another century to work out.

This chapter is what those hundred years of work bought us. By the end of it, you will be able to look at a stellar spectrum and read off the star.

---

## Core concept

### What light actually is

There is a genuine puzzle here, and the chapter will not pretend it away.

Drop two pebbles into a still pond a few inches apart. The ripples spread, overlap, and produce a pattern of alternating reinforcement and cancellation — interference. It is specifically what waves do. Nothing else does it.

Now shine two flashlights at a wall. You get more light. Not alternating bright and dark bands — just more light. Two streams of particles arriving at the same place pile up. No cancellation.

Light does both. In experiments with narrow slits ([Young, 1803](https://royalsocietypublishing.org/doi/10.1098/rstl.1804.0001)), light produces interference patterns identical to water waves. In experiments where light kicks electrons out of metal ([Einstein, 1905](https://doi.org/10.1002/andp.19053220607)), each electron's energy depends on the *frequency* of the light, not the brightness — exactly as if the light arrived in discrete energy packets.

The working rule from quantum mechanics: use the wave picture to describe how light travels, and the photon picture to describe how light delivers energy to matter. Both are necessary. Neither is complete alone. The connection is:

$$E = hf$$

Every photon carries energy $E$ proportional to the frequency $f$ of its corresponding wave. Planck's constant $h \approx 6.63 \times 10^{-34}$ J·s is small enough that individual photons are imperceptible at everyday brightnesses — but the proportionality is real. Ultraviolet photons (high frequency) carry enough energy per packet to break DNA bonds. Radio photons (low frequency) carry so little energy they pass through tissue unnoticed.

Maxwell worked out in the 1860s ([*A Dynamical Theory of the Electromagnetic Field*, 1865](https://royalsocietypublishing.org/doi/10.1098/rstl.1865.0008)) that radio, microwave, infrared, visible light, ultraviolet, X-rays, and gamma rays are all the same phenomenon — propagating disturbances in coupled electric and magnetic fields — distinguished only by wavelength. All travel at the same speed $c \approx 3.00 \times 10^8$ m/s. The relation:

$$c = \lambda f$$

locks wavelength and frequency together. Visible light spans roughly 400 nm (violet) to 700 nm (red), corresponding to frequencies near $5 \times 10^{14}$ Hz. The entire electromagnetic spectrum spans about twenty orders of magnitude. Human vision occupies one octave of it.

One more piece. Light from a point source spreads outward as an expanding sphere. The energy is fixed; the surface area at distance $d$ grows as $4\pi d^2$, so intensity (energy per unit area at the observer) falls as:

$$I \propto \frac{1}{d^2}$$

This is the inverse-square law. A star identical to the Sun but at the distance of Alpha Centauri (about 270,000 AU) appears $(270{,}000)^2 \approx 7 \times 10^{10}$ times fainter than the Sun — seventy billion times fainter. Everything we know about stars, we extracted from that diminished signal.

### What temperature does to light

Every object radiates. Not just glowing ones — every object, all the time, by virtue of having a temperature. Your body radiates infrared (peak around 9.4 μm) at about 100 watts. A poker in a fire radiates infrared at first; heated more, it glows red, then orange, then yellow, then white. The color shifts because hotter objects radiate more at shorter wavelengths.

The idealized version — a perfect absorber and emitter — is called a **blackbody**. Stars are close enough to blackbodies that the theory works.

In 1900, Max Planck worked out the exact mathematical form of the blackbody spectrum at any temperature ([Planck, 1901](https://doi.org/10.1002/andp.19013090310)). To make the calculation work, he had to assume that energy came in discrete packets proportional to frequency: $E = hf$. He was uncomfortable with the assumption and described it as a mathematical convenience. It turned out to be physics. Planck had accidentally founded quantum mechanics while trying to solve a problem in classical radiation theory.

We do not need the full Planck spectrum here. We need its two consequences.

**Wien's displacement law.** For temperature $T$ in Kelvin, the wavelength of peak emission is:

$$\lambda_{\text{peak}} = \frac{b}{T}, \quad b \approx 2.9 \times 10^{-3} \text{ m·K}$$

The Sun, $T \approx 5{,}772$ K, peaks at $\lambda_{\text{peak}} \approx 500$ nm — green-yellow, middle of the visible band. Human eyes are most sensitive near this wavelength; the available light is most concentrated there. Sirius, $T \approx 10{,}000$ K, peaks at 290 nm in the ultraviolet — invisible. A cool red dwarf at 3,000 K peaks near 970 nm, in the near-infrared. Measure where a star's spectrum peaks; you know its temperature, no contact required.

**Stefan-Boltzmann law.** Total power radiated by a blackbody of surface area $A$ at temperature $T$:

$$P = \sigma A T^4, \quad \sigma \approx 5.67 \times 10^{-8} \text{ W/m}^2/\text{K}^4$$

The fourth power makes the law lethal. Double the temperature and total power increases sixteenfold. The Sun radiates $3.83 \times 10^{26}$ W — enough to keep a planet warm at 150 million kilometers ([NASA Sun Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html)).

The $T^4$ also explains a confusion that lasted into the early twentieth century. A red giant — surface temperature only 3,500 K but radius hundreds of times the Sun's — can outshine a much hotter dwarf. The small $T^4$ factor is overwhelmed by the enormous $A$ factor. From light alone, knowing distance, you can recover the physical radius of an object you cannot visit.

### What atoms do to light

Now we can explain Fraunhofer's dark lines. The mechanism requires one fact about atomic structure.

The electrons in an atom do not occupy a continuous range of energies. They occupy **discrete energy levels** — quantized states with specific allowed values and nothing in between. The hydrogen electron can sit at level 1 ($-13.6$ eV), level 2 ($-3.4$ eV), level 3 ($-1.5$ eV), and so on. Not at $-2.0$ eV. Not at $-1.8$ eV. The allowed states are fixed by the geometry of the atom — only certain electron wave patterns fit around a nucleus without canceling themselves out, the same way only certain wavelengths fit on a guitar string of fixed length.

The consequence for light:

When an electron drops from a higher level to a lower one, it releases the energy difference as a single photon. Since the energy difference between any two specific levels is *the same exact number every time*, the photon has the same frequency, hence the same wavelength, every time. Hydrogen emits at 656.3 nm (deep red, Balmer series $n=3 \to 2$), 486.1 nm (blue-green, $n=4 \to 2$), 434.0 nm (violet, $n=5 \to 2$), and a handful of other specific wavelengths. Not approximately — exactly, because the energy levels are what they are.

The process runs in reverse. A photon of exactly the right energy can be absorbed, kicking an electron from a lower level to a higher one. Hydrogen absorbs at the same wavelengths at which it emits.

Now Fraunhofer's dark lines make sense. The Sun's hot, dense interior produces a continuous spectrum — all wavelengths at once, an unbroken rainbow. The continuous light passes outward through the Sun's cooler outer atmosphere (the photosphere). Atoms in that cooler gas absorb photons at their characteristic wavelengths and re-emit them in random directions; most of the re-emitted light scatters sideways rather than toward Earth. The light reaching us is *depleted* at exactly those characteristic wavelengths. The result: a continuous rainbow crossed by thin dark lines at precisely the absorption wavelengths of every element present in the solar atmosphere.

The line at 656.3 nm is hydrogen. The pair at 393/397 nm is ionized calcium (Fraunhofer's H and K). The line at 589 nm is sodium (Fraunhofer's D). Iron, magnesium, nickel — dozens of elements, each identified by a unique fingerprint of wavelengths matched against laboratory measurements. The Sun's composition is readable from Earth, line by line.

Composition is only the start. **Line strength** — how much light has been removed — depends on how many atoms are absorbing, which depends on both abundance and temperature (different ionization states are populated at different temperatures, following the [Saha equation](https://en.wikipedia.org/wiki/Saha_ionization_equation), 1920). Comparing line strengths from one element across different ionization states gives a temperature measurement independent of Wien's law. The two methods agree. That agreement is the kind of check that tells you the theory is right, not just consistent.

**Line width** measures pressure. In dense gas, atoms collide frequently; collisions blur the energy levels slightly, smearing the otherwise infinitely sharp line. Wider lines mean denser atmosphere.

**Line position** measures motion. When a source of waves moves toward you, the emitted waves are compressed (blueshift); when it moves away, stretched (redshift). The non-relativistic Doppler formula:

$$\frac{\Delta\lambda}{\lambda} = \frac{v}{c}$$

A 1 nm shift in a 500 nm line ($\Delta\lambda/\lambda = 0.002$) corresponds to $v = 0.002c \approx 600$ km/s — a large stellar velocity. Most stars in the solar neighborhood drift at tens of km/s relative to us; measured shifts are tiny fractions of a nanometer.

A rotating star adds one more layer. One limb of the disk rotates toward you (blueshifted), the other away (redshifted). The two Doppler-shifted components blur together into a line wider than it would be from a non-rotating star. Measure the rotational broadening; you have the equatorial rotation speed.

---

## Worked example: reading a star, all of it, from one spectrum

Suppose you observe a star and measure:

1. Continuous spectrum peaks at $\lambda_{\text{peak}} = 290$ nm.
2. Hydrogen-alpha line (rest wavelength 656.3 nm) appears at 656.5 nm.
3. Ionized helium lines are strong; neutral calcium lines are absent.
4. Lines are sharp, with slight symmetric broadening.

What is the star?

**Temperature, method 1 (Wien's law).** $T = b/\lambda_{\text{peak}} = (2.9 \times 10^{-3} \text{ m·K}) / (290 \times 10^{-9} \text{ m}) = 10{,}000$ K.

**Temperature, method 2 (ionization).** Strong He II requires temperatures above $\sim 25{,}000$ K to ionize helium, while strong He I lines (singly ionized appears at lower temperatures). [verify: He II vs He I temperature thresholds] If He II is "strong" but the Wien temperature is only 10,000 K, the two methods disagree — meaning either the spectrum description is fictional (it is — this is a worked example) or one of the methods is misapplied. For consistency take $T \approx 10{,}000$ K; the He pattern then implies hot enough for Balmer hydrogen and mostly-neutral He, characteristic of an A-type star.

**Velocity.** $\Delta\lambda = 0.2$ nm at $\lambda = 656.3$ nm gives $v = c \times 0.2/656.3 \approx 91$ km/s, receding (redshifted).

**Pressure.** Sharp lines mean low atmospheric pressure — characteristic of giants or supergiants, where the atmosphere is thinly spread.

**Rotation.** Slight symmetric broadening means moderate rotation speed — tens of km/s at the equator.

From a single spectrum: a 10,000 K A-type giant, retreating at about 91 km/s, with a thin atmosphere and modest rotation. If we also knew its distance, Stefan-Boltzmann ($L = 4\pi R^2 \sigma T^4$) would deliver the radius. We have characterized a star we have never visited from light that spent years crossing empty space.

---

## Common misconceptions

- **"The Sun is yellow."** The Sun's spectrum peaks in green, and its visible light is broadly white. The yellow tint comes from Earth's atmosphere scattering blue light away (the same scattering that makes the sky blue). Above the atmosphere the Sun appears white. Calling the Sun "yellow" is a sea-level optical illusion, not a stellar property.
- **"Wave-particle duality means light is sometimes a wave and sometimes a particle."** Closer to: light is neither, and both descriptions are useful approximations to a single quantum-mechanical object. The wave picture predicts where it goes; the photon picture predicts how it interacts. They do not contradict because they describe different aspects of the same thing.
- **"Spectral lines come from elements glowing."** Most stellar lines are *absorption* lines — gaps in the continuous spectrum produced by cooler atmospheric gas removing specific wavelengths from the hotter continuum below. Hot, thin gas in emission (a nebula, a fluorescent tube) shows *emission* lines — bright at the same characteristic wavelengths. Same atomic transitions, different geometry of where the gas sits relative to the continuum source.
- **"Redshift always means the universe is expanding."** Redshift means *something* is stretching the wavelength: motion of the source away from you (Doppler), cosmic expansion of space (cosmological redshift), or strong gravity at the source (gravitational redshift). Local stellar redshifts in our galaxy are almost entirely Doppler. Cosmological redshifts of distant galaxies are mostly expansion. The mechanism matters; the term does not distinguish.

---

## Exercises

**Warm-up (Understand).** Light A has wavelength 400 nm; light B has wavelength 700 nm. (a) Which has higher frequency? (b) Which carries more energy per photon? (c) State the relationships you used.

**Application (Apply).** A star's continuous spectrum peaks at 580 nm. (a) Use Wien's law to estimate its surface temperature. (b) Compared to the Sun (peak 500 nm), is it hotter or cooler? (c) By what fraction does its peak wavelength differ from the Sun's?

**Synthesis (Analyze).** The hydrogen-alpha line of a galaxy is measured at 692 nm instead of its rest wavelength of 656.3 nm. (a) Compute the implied recession velocity. (b) State two distinct physical mechanisms that could produce this redshift. (c) For each mechanism, describe one additional observation that would help distinguish it from the others.

**Challenge (Analyze).** A red giant has $T = 3{,}500$ K and radius 100 $R_\odot$. The Sun has $T = 5{,}772$ K and radius 1 $R_\odot$. (a) Use $L = 4\pi R^2 \sigma T^4$ to compute the ratio of the giant's luminosity to the Sun's. (b) Which factor — temperature or radius — dominates the answer? (c) State one observational consequence: would the giant or the Sun be brighter at 290 nm? At 5 μm? Justify with Wien's law.

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
> **Verify.** (a) Set the slider to 5,800 K; the peak should land at $\sim 500$ nm. (b) Set it to 10,000 K; the peak should jump to $\sim 290$ nm. (c) Set it to 2,000 K; the peak should leave the visible band entirely, landing near 1,450 nm in the near-infrared.

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

## What would change my mind

The mechanism in this chapter rests on one universality claim: the energy levels of hydrogen and every other atom are the same everywhere in the observable universe. Every test for a century has confirmed it — distant-galaxy spectral lines appear at the right wavelengths, shifted only by redshift, never at wrong wavelengths that would indicate the underlying physics had changed. A reproducible measurement of *fine-structure-constant variation* with cosmic distance, after every known systematic has been ruled out, would force a serious rewriting of the chapter and most of cosmology with it. The current observational constraint is that the fine-structure constant has varied by less than about one part in $10^7$ over the last 10 billion years ([Webb et al. 2011](https://arxiv.org/abs/1008.3907) and subsequent follow-ups). Watch this number; it has been claimed once and not confirmed.

## Still puzzling

- *Why is the speed of light what it is?* In SI units it is exactly $299{,}792{,}458$ m/s by definition since 1983 — but the metre is now defined from $c$, not the other way around. The numerical value is a unit choice. What the value of $c$ in some absolute sense means, or whether the question is even coherent, remains unsettled.
- *Why are atomic energy levels everywhere the same?* The deeper answer is that the Standard Model has the same Lagrangian everywhere — but *why* it does, and whether that has always been true in cosmic history, is an open question rather than a derived result.
- *What does Cecilia Payne-Gaposchkin's 1925 thesis show us?* She used the Saha equation and stellar spectra to demonstrate that stars are overwhelmingly hydrogen. The result was so contrary to the prevailing assumption (that stars had Earth-like composition) that her advisor pressured her to call it "almost certainly not real." She bent — and was vindicated a few years later when others repeated her analysis. The episode is a useful reminder that good evidence and a correct theory still require willingness to publish the conclusion they imply.

---

**Tags:** electromagnetic spectrum, photons, blackbody, Wien's law, Stefan-Boltzmann, spectral lines, Fraunhofer, Doppler shift, Payne-Gaposchkin, spectroscopy
