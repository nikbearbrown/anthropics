# Chapter 5 — Light and Spectra: Reading the Universe from a Distance

*How we learned to interrogate the universe using the only messenger it sends us.*

---

Here is the situation we are in. The nearest star beyond our Sun is 4.24 light-years away. The fastest spacecraft we have ever built would take over two million years to reach it. The Sun itself is hot enough to vaporize any material we could make a ship from before that ship got close. We cannot go to the stars. We cannot collect samples. We cannot run laboratory tests on stellar material. And yet we know what stars are made of. We know their temperatures, their masses, their ages, their motions. We know whether a star has a companion, how fast it rotates, how dense its atmosphere is.

We know all of this because of light.

What I want to explain in this chapter is not the list of facts we have learned. I want to explain the mechanism by which light carries information — how it encodes the story of its source in a way that we can decode from here, sitting on Earth, looking up. The story has three pieces, and they fit together like a lock and key: what light *is*, what temperature does to light, and what atoms do to light. Get those three pieces in order, and you can read a spectrum the way you read a page.

---

## What Light Actually Is

There is a genuine puzzle at the center of this, and I do not want to paper over it. Light behaves as a wave in some situations and as a particle in others. These two behaviors seem, at first, flatly contradictory. Let me show you why each is inescapable, and then what to make of it.

Drop two pebbles into a still pond a few inches apart. The circular ripples they produce spread outward and eventually overlap. Where a crest from one meets a crest from the other, you get a bigger crest. Where a crest meets a trough, they cancel. The result is a pattern of alternating strong and still regions spreading across the water. This is interference. It is what waves do. Nothing else does it.

Now shine two flashlights at the same spot on a wall. What do you get? You get more light. Not a pattern of bright and dark bands — just more light. Light, from this observation, behaves the way you would expect bullets to behave: two streams of bullets arriving at the same place just pile up. No cancellation.

So: light makes interference patterns in careful experiments with narrow slits. Light also adds without canceling when you shine two beams at a wall. Both observations are real. Neither is wrong. For two hundred years, physicists argued about which one captured the truth.

The resolution came from quantum mechanics, and it is uncomfortable: both pictures are true in their domain. When light propagates — travels from one place to another — it behaves as a wave. It has a wavelength, a frequency, and it interferes with itself. When light interacts with matter — gets absorbed, knocks an electron loose, hits a photographic plate — it arrives as a discrete packet of energy called a photon. There is no trajectory by which a photon travels from one spot to another that makes classical sense. The photon is in some sense everywhere along its path simultaneously, until it lands.

I do not expect this to feel satisfying. It should not yet. What I want you to take from it is a working rule: use the wave picture when you want to describe how light travels and what wavelength and frequency it has. Use the photon picture when you want to describe how light delivers energy to matter. Both pictures are necessary. Neither is complete alone.

The central relationship between them is this: every photon carries energy proportional to the frequency of the wave it corresponds to.

$$E = hf$$

Here $E$ is the photon's energy, $f$ is the frequency of the light, and $h$ is Planck's constant — about $6.63 \times 10^{-34}$ joule-seconds. This is a small number, which is why we do not notice individual photons in everyday life. But it captures something profound: a photon of high-frequency light (ultraviolet, X-ray) carries more energy than a photon of low-frequency light (infrared, radio). When ultraviolet light hits your skin, each photon packs enough energy to break a chemical bond in DNA. A radio wave photon, striking the same skin, carries so little energy it passes through without consequence.

Now: all electromagnetic waves — radio, microwave, infrared, visible light, ultraviolet, X-ray, gamma ray — are the same kind of thing. They are all oscillating electric and magnetic fields propagating through space. Maxwell worked this out in the 1860s. He noticed the deep symmetry between electricity and magnetism: a changing electric field produces a magnetic field, and a changing magnetic field produces an electric field. He wrote down the equations of that symmetry and found that they predicted a wave propagating at a speed he could calculate. The speed came out to about 300,000 kilometers per second. That was the known speed of light. Maxwell realized that light was an electromagnetic wave — that he had not discovered a new kind of radiation but had explained what light was.

<!-- → [INFOGRAPHIC: the full electromagnetic spectrum on a single horizontal log-scale axis from gamma rays (~10⁻¹² m) to radio (~10³ m) — mark wavelength, frequency, and photon energy on three parallel rows; highlight the narrow visible band (400–700 nm) and annotate representative sources at each band (nuclear decay, hot plasma, hot stars, sunlight, warm dust, cosmic microwave background, radio galaxies)] -->

All these waves travel at that same speed, $c \approx 3 \times 10^8$ meters per second. They differ only in wavelength and frequency. Since the speed is fixed, wavelength and frequency are locked together:

$$c = \lambda f$$

where $\lambda$ (lambda) is the wavelength — the distance from one crest to the next — and $f$ is the frequency — how many crests pass a fixed point per second. Longer wavelength means lower frequency; shorter wavelength means higher frequency. A radio wave with a wavelength of a few meters has a frequency in the hundreds of megahertz. Visible light with a wavelength of 600 nanometers has a frequency of about $5 \times 10^{14}$ cycles per second — 500 trillion oscillations every second. This is why you cannot see individual wave cycles. Your eye is far too slow to register them.

One more piece of mechanics, and then we can move to the interesting part. Light from a point source spreads outward equally in all directions, covering an expanding sphere. The total energy the source produces does not change, but that energy gets spread over an ever-larger surface. At distance $d$, the light covers a sphere of area $4\pi d^2$. The intensity — energy per unit area reaching you — therefore falls as $1/d^2$. This is the inverse square law, and it applies to anything that radiates uniformly in all directions: light, sound, gravity.

$$I \propto \frac{1}{d^2}$$

<!-- → [DIAGRAM: a point source at center with three concentric spheres at distances d, 2d, and 3d — shade one unit patch at the innermost sphere and project it outward to show it covering 4 and 9 patches at the outer spheres; annotate the 1/4 and 1/9 intensity ratios] -->

The practical consequence is dramatic. A star identical to our Sun but 270,000 times farther away appears $(270,000)^2 \approx 7 \times 10^{10}$ times fainter. 70 billion times fainter. Even nearby stars are reduced to pinpoints by the sheer distance. Everything we have learned about stars, we have had to extract from that small, faint signal.

---

## What Temperature Does to Light

Every object radiates. This is not something special that glowing things do — everything does it, all the time. The question is where in the spectrum the radiation falls.

When you heat a poker in a fire, at low temperatures it radiates only infrared — you feel warmth but see nothing. As it heats up, it begins to glow red. Hotter still, orange, then yellow, then white. The color changes because hotter objects radiate more intensely at shorter wavelengths. This is not a property of iron in particular. It is universal.

The idealized version of this — an object that absorbs all radiation that hits it and radiates equally efficiently at all wavelengths — is called a blackbody. Real objects deviate from the ideal, but not by much. Stars are close enough to blackbodies that the theory is remarkably accurate.

In 1900, Max Planck found the exact mathematical form of the blackbody spectrum — the distribution of intensity across all wavelengths for a given temperature. What he found, to his own discomfort, was that the derivation only worked if energy came in discrete packets proportional to frequency: E = hf. He had discovered quantum mechanics while trying to solve a problem in classical radiation theory. The irony is that the correct formula for blackbody radiation was the first indication that nature was fundamentally discontinuous at small scales.

We do not need the full Planck formula here, but we need its two consequences.

The first is Wien's displacement law. At any given temperature, there is a wavelength at which the radiation is most intense. Hotter objects peak at shorter wavelengths. The relationship is exact and simple:

$$\lambda_{\text{peak}} = \frac{b}{T}$$

where $\lambda_{\text{peak}}$ is the wavelength of peak emission, $T$ is the temperature in Kelvin, and $b$ is Wien's constant, about $2.9 \times 10^{-3}$ m·K.

<!-- → [CHART: overlapping Planck curves for three temperatures — 3,000 K (red dwarf), 5,800 K (Sun, yellow), 10,000 K (Sirius, blue-white) — intensity on y-axis, wavelength on x-axis (200–2000 nm); mark the visible band; show each curve's peak shifting left with increasing temperature; annotate peak wavelengths at 970 nm, 500 nm, 290 nm] -->

The Sun has a surface temperature of about 5,800 K. Plugging in: $\lambda_{\text{peak}} = 2.9 \times 10^{-3} / 5800 \approx 500$ nm. That is right in the middle of the visible spectrum, in the green-yellow range — which is why sunlight looks the way it does, and probably why human eyes evolved to be most sensitive there. Sirius, hotter at about 10,000 K, peaks at 290 nm, in the ultraviolet. A cool red dwarf at 3,000 K peaks at about 970 nm, in the near infrared.

The direction of the argument is the important part: measure where a star's radiation peaks, and you know its temperature. No contact required.

The second consequence is the Stefan-Boltzmann law. The total power radiated by a blackbody goes as:

$$P = \sigma A T^4$$

where $\sigma$ is the Stefan-Boltzmann constant, $A$ is the surface area, and $T$ is temperature. The fourth power is what makes this striking. Double the temperature, and the power output goes up by a factor of 16. The Sun, at 5,800 K, radiates $4 \times 10^{26}$ watts. That is enough to keep Earth warm at a distance of 150 million kilometers.

What the Stefan-Boltzmann law also tells you: a large, cool star can radiate as much total power as a small, hot one, if it is large enough. The fourth power dependence on temperature means that temperature dominates for similar-sized objects, but a very large area can compensate for lower temperature. This is why red giant stars — cool but enormous — can outshine smaller hot stars in total luminosity.

Put Wien's law and Stefan-Boltzmann together, and from the spectrum of a star you can read both temperature and, once you know the distance, the physical size. From light that has been traveling for years, you have reconstructed the star's basic physical properties.

---

## What Atoms Do to Light

In 1814, Joseph von Fraunhofer looked at sunlight through a prism. Light, passing through the prism, spread into a rainbow — continuous red through orange through yellow through green through blue through violet. But Fraunhofer saw, crossing this rainbow, hundreds of thin dark lines. Not an artifact. Not a defect in the prism. They were reproducible and always in exactly the same places. He catalogued them and was puzzled. He had no idea what they were.

We know now. They are the fingerprints of atoms.

To understand why, you need to know one thing about atomic structure: electrons in atoms do not occupy a continuous range of energies. They occupy discrete energy levels. The electron in a hydrogen atom can sit at energy level one, or level two, or level three — but not at 1.3 or 2.7. The levels are quantized, meaning they come in specific allowed values and nothing in between.

Why? This is where quantum mechanics is essential, and where I have to be honest: the full explanation requires a more sophisticated treatment than we will get to here. The rough picture — and it is roughly right — is that electrons in atoms behave as waves, and only certain wave patterns fit around the nucleus in stable configurations. The allowed orbits are the ones where the electron's wave fits exactly. Others destructively interfere with themselves and cannot persist.

<!-- → [DIAGRAM: hydrogen energy level diagram — horizontal lines at n=1 (−13.6 eV, ground state), n=2 (−3.4 eV), n=3 (−1.5 eV), n=4 (−0.85 eV), ionization limit at 0 eV; draw downward arrows for the first four Balmer transitions (n=3→2 at 656 nm red, n=4→2 at 486 nm blue-green, n=5→2 at 434 nm violet, n=6→2 at 410 nm deep violet); label each arrow with wavelength and color] -->

For our purposes, the consequence is this: when an electron drops from a higher energy level to a lower one, it must release the energy difference. It releases it as a photon. And since the energy difference between two specific levels is fixed, the photon has a specific energy, which means a specific frequency, which means a specific wavelength. Hydrogen always emits at 656 nm (the Balmer alpha line, red), 486 nm (blue-green), 434 nm (violet), and so on. Always exactly those wavelengths. Not similar wavelengths — those wavelengths, every time, because the energy levels of hydrogen are what they are.

This is what Fraunhofer saw in the solar spectrum. The Sun's interior is hot and dense, producing a continuous spectrum — the rainbow background. But the Sun has an outer atmosphere, cooler than the interior, where atoms are not so violently agitated. As the continuous light from the interior passes through this cooler gas, atoms in the gas absorb photons at their specific wavelengths and re-emit them in random directions. The light that reaches us in those specific wavelengths has been scattered sideways and is depleted. The result: a continuous rainbow with thin dark lines precisely at the wavelengths that hydrogen, calcium, iron, and every other element absorbs.

<!-- → [IMAGE: a reproduction or faithful rendering of the Fraunhofer solar absorption spectrum — a continuous visible-light rainbow crossed by prominent dark lines; label the major lines: H-alpha (656 nm, red), Ca K (393 nm, violet), Ca H (397 nm, violet), Na D (589 nm, yellow), Mg b (517–518 nm, green)] -->

The absorption line at 656 nm tells you hydrogen is present. The absorption line at 393 nm tells you calcium is present. Lines at specific wavelengths in the infrared tell you about iron, nickel, magnesium. The composition of the Sun — a body you cannot touch, you cannot sample, whose surface would vaporize any instrument — is readable from Earth, line by line.

But the lines tell you more than composition. The strength of a line — how dark it is, how much light has been removed — tells you how many atoms of that element are absorbing at that wavelength. And that depends not just on how much of the element is present, but on the temperature: at different temperatures, different fractions of atoms are in different energy states and absorbing at different wavelengths. By comparing the relative strengths of multiple lines from the same element, you can measure temperature independently of Wien's law. The two methods agree. This is how you know the measurement is not a coincidence.

The width of a spectral line tells you about pressure. In dense gas, atoms collide frequently, and those collisions slightly disturb the energy levels. The result is that each line is not perfectly sharp but slightly broadened. Measure the broadening, and you measure the density of the gas.

Then there is motion. In 1842, Christian Doppler made the following observation: when a source of waves moves toward you, the waves it emits are compressed — shorter wavelength, higher frequency. When it moves away, they are stretched — longer wavelength, lower frequency. You have heard this with sound. An approaching ambulance siren is higher pitched than a receding one.

Light does the same thing. If a star is moving toward us, all its spectral lines shift toward shorter wavelengths — a blueshift. If it is moving away, they shift toward longer wavelengths — a redshift. The size of the shift depends on the velocity:

$$\frac{\Delta \lambda}{\lambda} = \frac{v}{c}$$

where $\Delta\lambda$ is how much the wavelength has shifted, $\lambda$ is the rest wavelength, $v$ is the radial velocity (positive for recession, negative for approach), and $c$ is the speed of light. The formula is approximate for low velocities — much less than $c$ — and requires relativistic correction for the velocities of distant galaxies.

<!-- → [DIAGRAM: three panels showing the Doppler effect on a spectral line — left panel: source at rest, line at rest wavelength λ₀; center panel: source approaching, line blueshifted to λ₀ − Δλ; right panel: source receding, line redshifted to λ₀ + Δλ; annotate the shift magnitude Δλ and the velocity formula beneath each panel] -->

When Doppler shifts of distant galaxies were measured in the early twentieth century, astronomers found that almost all galaxies were redshifted — moving away from us. And more distant galaxies were moving away faster. This was the evidence for the expansion of the universe, and ultimately for the Big Bang. It came from measuring the positions of dark lines in starlight.

A rotating star adds one more layer. One side of the star rotates toward us, the other rotates away. The hydrogen-alpha line from the approaching side is slightly blueshifted; from the receding side, slightly redshifted. The net result is a spectral line that is not a sharp thin line but a slightly broadened one — the two shifted components blend together. Measure the width of this rotational broadening, and you know the rotation speed of the star.

---

## The Full Read

Let me now put all of this together and show you what a spectrum actually tells you.

You take the light from a star, pass it through a spectrograph (a prism or a diffraction grating), and project the resulting spectrum onto a detector. What you see is a rainbow of color — the continuum from the star's hot interior — crossed by dozens of dark lines.

First, you identify the lines. The wavelengths of the lines match the known wavelengths of hydrogen, helium, calcium, iron. You now know the composition of the star's outer atmosphere.

Second, you measure whether the lines are shifted from their rest positions. If the hydrogen-alpha line, which should be at 656.3 nm, appears at 656.8 nm, it is redshifted by 0.5 nm. The velocity calculation gives: $v = c \times (0.5 / 656.3) \approx 230$ km/s, receding. The star is moving away from you at 230 kilometers per second.

Third, you measure where the continuum radiation peaks and apply Wien's law. If the peak is at 290 nm, the surface temperature is about 10,000 K. If it peaks at 500 nm, about 5,800 K.

Fourth, you look at the relative strengths of the spectral lines. Lines from highly ionized atoms — atoms that have had electrons stripped away — require high temperatures. If you see ionized helium lines, the temperature must be above about 25,000 K, because that is what it takes to strip helium of its electrons. Lines from neutral calcium require cooler conditions. The ionization state of the elements tells you the temperature, independently of Wien's measurement.

Fifth, you look at the widths of the lines. Pressure broadening means dense atmosphere — large, high-gravity star. Narrow lines mean low pressure — thin atmosphere, maybe a giant star or a supergiant.

Sixth, you look for rotational broadening. A star spinning at 200 kilometers per second gives its lines a characteristic blurred shape quite different from the Doppler broadening of a binary companion.

<!-- → [TABLE: six-row summary of what each spectral measurement reveals — columns: what you measure, what it tells you, physical quantity extracted; rows: line wavelength identity (composition), line position shift (radial velocity), continuum peak wavelength (surface temperature via Wien), line strength ratios (temperature via ionization state), line width from pressure (atmospheric density/gravity), line width from rotation (stellar rotation speed)] -->

From a single spectrum — from light that has been traveling through empty space, that has told you nothing about the star directly — you have determined: composition, temperature (two independent ways), surface gravity, rotation speed, and motion toward or away from you. If you also know the distance (from other methods), you can combine Wien's law and the Stefan-Boltzmann law to determine the physical radius of the star.

You have never touched the star. You will never touch the star. You have read it completely in its light.

---

## The Architecture Behind the Method

The reason this works is a principle that is easy to overlook: the laws of physics are universal. The energy levels of hydrogen are the same here and in Proxima Centauri. The speed of light is the same near the Sun and near a quasar ten billion light-years away. The Planck constant is the same everywhere in the observable universe.

This is not obvious. It did not have to be true. But every test we have ever run confirms it. Spectral lines from distant galaxies appear at the wavelengths we expect, shifted only by the Doppler effect of their recession velocity — never at wrong wavelengths that would indicate the underlying atomic physics was different.

This universality is what makes spectroscopy work as a scientific tool. If atoms behaved differently under different conditions, or in different locations, the fingerprints would be unreadable. Instead, the fingerprints are the same everywhere. And so when we see the hydrogen-alpha line in a spectrum from a galaxy three billion light-years away, shifted by precisely the amount that implies the galaxy is receding at a certain fraction of light speed, we know we are reading something real about the physical universe.

---

## LLM Exercises

**1. The wave-particle tension.** Ask an LLM to explain why light must be both a wave and a particle — not just that it is, but why it must be. Then push back: ask it "Couldn't we just pick one and accept that the other picture is an approximation?" How does it handle the constraint that the photoelectric effect requires photons and interference requires waves, and that no single classical object does both? Does it reach for quantum mechanics to resolve the tension, or does it hedge?

**2. Wien's law in reverse.** Give an LLM a star's color description — say, "bright blue-white, like Rigel" — and ask it to infer the approximate surface temperature using Wien's law. Then ask it to predict which hydrogen spectral lines would be visible in such a star's spectrum, given that visible Balmer lines require temperatures roughly between 7,500 K and 10,000 K. Does it correctly identify that very hot stars show fewer visible hydrogen lines because hydrogen is ionized?

**3. The Doppler argument.** Ask an LLM to explain, from first principles, why the expansion of the universe was inferred from galaxy spectra rather than from any other observation. What specific feature of the spectra — and what pattern across many galaxies — forced the conclusion that the universe is expanding? Ask it to distinguish between "all galaxies happen to be moving away from us" and "space itself is expanding." Does it handle the difference carefully?

**4. Reading a fictional spectrum.** Describe to an LLM a fictional stellar spectrum: "The spectrum shows a continuous rainbow with dark lines identified as hydrogen, calcium, and ionized helium. The hydrogen-alpha line is at 659 nm instead of 656.3 nm. The lines are broad, with slight rotational broadening." Ask it to extract as much physical information as possible from this description. What can it infer about temperature, motion, atmospheric pressure, and rotation? Does it use all four pieces of information or overlook some?

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Cecilia Payne-Gaposchkin** showed in her 1925 PhD thesis that stars are made overwhelmingly of hydrogen — by analyzing stellar spectra and applying Saha's ionization equation. The result was so shocking she was talked into hedging her conclusions. She turned out to be right.

**Run this:**

```
Who was Cecilia Payne-Gaposchkin, and how does her discovery that stars are made of hydrogen connect to the radiation and spectra we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.
```

→ Search **"Cecilia Payne-Gaposchkin"** on Wikipedia. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to walk through Payne's spectral argument: what specifically about stellar spectra forced the hydrogen conclusion?
- Add a constraint: "Answer as Payne's 1925 thesis defense, in her voice."

What changes? What gets better? What gets worse?
