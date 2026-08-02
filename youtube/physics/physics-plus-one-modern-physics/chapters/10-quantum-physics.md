# Chapter 10 — Quantum Physics
*The three experiments that demolished classical physics, and what replaced it.*

In 1926, Erwin Schrödinger wrote down a wave equation that correctly predicted the behavior of electrons in atoms. Within two years, Paul Dirac had extended it to relativistic particles. Within a decade, the theory built on that equation — quantum mechanics — had explained the structure of every element in the periodic table, the nature of chemical bonds, the behavior of metals, the properties of semiconductors. It has since been tested to more decimal places than any other theory in the history of science.

Nobody fully understands it.

Not in the sense that we lack the equations. The equations are perfectly clear. Not in the sense that we can't use them — physicists and engineers use quantum mechanics every day to design transistors, lasers, and MRI machines. The mystery is what the equations mean: what is actually happening when an electron "passes through both slits" in an interference experiment, what the wavefunction physically *is*, why measurement plays a special role. Physicists have been arguing about this since 1927. They are still arguing.

What we do understand, completely, is the experimental evidence that forced quantum mechanics on us. Three sets of experiments between 1900 and 1927 broke classical physics at small scales in a way that could not be repaired. The same constant — Planck's constant $h = 6.626 \times 10^{-34}$ joule-seconds — appeared in all three. That is not coincidence. It is the signature of a single underlying theory.

This is the chapter about those three experiments and what they teach us.

---

## The Catastrophe

Start with something classical physics got catastrophically wrong.

Take a metal box, heat it to some temperature, drill a tiny hole in the side, and measure the spectrum of radiation coming out. This is a blackbody — an idealized object in thermal equilibrium with the radiation it emits. Every hot object is an approximation to one: the tungsten filament of a light bulb, the surface of the Sun, the iron in a blacksmith's forge that glows from red to orange to yellow-white as it heats. The color of a hot object tells you its temperature. This is well-established experimental fact.

Now ask classical physics to predict the spectrum.

Classical physics says that electromagnetic radiation inside a cavity is a collection of standing wave modes. Statistical mechanics says that in thermal equilibrium, each mode gets an equal average energy $k_BT$. Count the modes at each frequency — there are vastly more at high frequencies than low — multiply by the average energy per mode, and you get the predicted spectrum.

The prediction diverges. As frequency increases, the number of modes increases faster than the average energy per mode decreases, so the total radiated power at high frequencies climbs without bound. An object at any finite temperature should radiate infinite power, mostly in the ultraviolet and X-ray range. The sky should glow. Metal at room temperature should burn you with X-rays.

This is called the ultraviolet catastrophe, and it is not a subtle discrepancy requiring careful experiment to detect. It is a prediction of infinity where experiment measures a finite, well-behaved curve that peaks at one frequency and falls off on both sides.

<!-- → [CHART: blackbody spectrum — two curves on the same axes; horizontal axis: wavelength (100 nm to 3000 nm, with visible range shaded); vertical axis: spectral radiance (arbitrary units); curve 1 labeled "classical Rayleigh-Jeans prediction" — rises steeply toward short wavelengths, escaping off the top of the chart toward the UV with an annotation "→ infinity"; curve 2 labeled "Planck's formula (measured)" — rises, peaks near 500 nm for 5800 K, then falls; the two curves match at long wavelengths and diverge catastrophically at short ones; caption: "The catastrophe is not a small discrepancy. Classical physics predicts infinite power in the UV. The measured curve is well-behaved. Planck's formula matches the measured curve exactly."] -->

Max Planck fixed it in 1900 by making an assumption he did not believe. He assumed that the oscillating atoms in the walls of the cavity could not radiate arbitrary amounts of energy. Instead, they could only emit or absorb energy in discrete units — *quanta* — of size $hf$, where $f$ is the frequency of oscillation and $h$ is a new constant of nature. Planck called this a "purely formal" trick, useful for getting the right answer but probably not physically real.

Here is why the trick works. Classical physics says every mode gets average energy $k_BT$ regardless of frequency. Planck's quantization says a mode of frequency $f$ can only be excited if the system has enough thermal energy to create at least one quantum of size $hf$. At high frequencies, where $hf$ is much larger than $k_BT$, the mode almost never gets excited — the probability of having that much energy available is exponentially small. So the spectrum cuts off at high frequencies exactly where it does. The catastrophe disappears. The formula matches every measured blackbody curve.

Planck spent years trying to derive the same result without the quantization assumption. He could not. Neither could anyone else. The quantization is not a trick. It is real.

<!-- → [DIAGRAM: why quantization cuts off high-frequency modes — two side-by-side panels; left "classical": a continuous energy axis with modes at all frequencies receiving equal average energy kBT, annotated "every frequency costs the same to excite"; right "quantum (Planck)": an energy axis with discrete rungs spaced by hf — low-frequency rungs (small hf) are below the thermal energy kBT dashed line and get excited; high-frequency rungs (large hf) are far above kBT and almost never get excited; annotate "high-frequency modes starved of energy"; caption: "The quantization is not a fudge — it is a cost structure. High-frequency modes require more energy per quantum than the system typically has available."] -->

---

## The Electrons That Won't Eject

Five years after Planck, Einstein did something more radical. He took the quantization and applied it not to the oscillators in the wall but to the light itself.

The occasion was the photoelectric effect, which had been mysterious since Heinrich Hertz noticed it in 1887. Shine light on a metal surface and electrons are sometimes ejected. This is useful — it is the basis of every photodetector, solar cell, and camera sensor ever built. But the behavior was inexplicable.

Here is the mystery. Increase the intensity of the light and more electrons come out — but they come out at the same speed. Change the frequency of the light and the speed of the ejected electrons changes. Below a certain threshold frequency, no electrons come out at all, regardless of intensity. The threshold depends on the metal, not on the light.

<!-- → [DIAGRAM: the photoelectric effect — two experimental setups; left panel: intense red beam hitting a metal plate, zero electrons emerging, labeled "bright red light: nothing — ever"; right panel: faint violet beam hitting the same plate, electrons streaming out, labeled "dim violet light: electrons ejected immediately"; below both: a graph of maximum electron kinetic energy vs. light frequency — a straight line starting at threshold frequency f₀ with positive slope h; annotate "slope = h", "x-intercept = threshold frequency f₀ = ϕ/h", "y-intercept = −ϕ"; caption: "Millikan measured this graph in 1916 trying to disprove Einstein's 1905 paper. The slope gave him Planck's constant to high precision. He ended up confirming Einstein instead."] -->

Classical wave physics has a clear prediction: light is a wave carrying energy distributed across its wavefront. More intense light means more energy per unit area, which means electrons should receive more energy and come out faster. If the intensity is high enough, any frequency should eventually eject electrons — given enough time to accumulate the energy from the wave. Neither prediction is correct.

Einstein's 1905 paper proposed that light is not a continuous wave. It is a stream of discrete particles — photons — each carrying energy $E = hf$, where $f$ is the frequency of the light and $h$ is Planck's same constant. When a photon hits an electron in the metal, it delivers all its energy to that one electron in one instantaneous interaction. There is no accumulation, no waiting. Either the photon has enough energy to free the electron from the metal, or it does not. Increasing intensity sends more photons per second, which ejects more electrons per second — but the energy of each electron depends only on the frequency of each photon, because each interaction is between one photon and one electron.

Each metal has a characteristic binding energy $\phi$ — the minimum energy needed to free an electron from its surface. The ejected electron carries away whatever is left:

$$KE_{\max} = hf - \phi$$

Below the threshold frequency $f_0 = \phi/h$, every photon lacks the energy to free an electron. Above it, electrons emerge immediately, even in the dimmest light, because the relevant quantity is the energy per photon, not the total power of the beam.

A concrete case. Violet light at 400 nm has photon energy:

$$E = \frac{hc}{\lambda} = \frac{1240 \text{ eV·nm}}{400 \text{ nm}} = 3.10 \text{ eV}$$

On a metal with work function $\phi = 2.20$ eV, the ejected electrons carry $3.10 - 2.20 = 0.90$ eV of kinetic energy. Red light at 700 nm carries only 1.77 eV per photon. On the same metal, red light ejects nothing, no matter how bright, because $1.77 < 2.20$. One violet photon in the dimmest imaginable beam ejects an electron. A trillion red photons per second eject none.

The $hc = 1240$ eV·nm shortcut is worth memorizing: divide it by any wavelength in nanometers and you get the photon energy in electron volts.

Einstein received the Nobel Prize in 1921 for this explanation. Not for relativity. For the photoelectric effect. The committee was being careful — relativity was still considered controversial in some quarters — but they were also correct that this paper was the more fundamental contribution to physics. It established, for the first time, that electromagnetic radiation itself is quantized.

A photon also carries momentum. This was confirmed by Arthur Compton in 1923, who aimed X-rays at electrons and measured the scattered X-rays. If X-rays were purely waves, scattering off a stationary electron would change their direction but not their wavelength. Compton found the scattered X-rays had longer wavelengths — they had lost energy. The calculation that matched his data treated the collision as a billiard-ball interaction between a photon with momentum $p = h/\lambda$ and an electron with classical momentum. Conservation of relativistic energy and momentum, applied exactly, predicted the wavelength shift. The photon is a particle with both energy and momentum.

$$p = \frac{h}{\lambda} = \frac{E}{c}$$

<!-- → [DIAGRAM: Compton scattering — before: an X-ray photon (wavelength λ, labeled "incident photon: E = hc/λ, p = h/λ") approaching an electron at rest; after: scattered photon at angle θ with longer wavelength λ' > λ (labeled "energy lost: wavelength increased"), recoiling electron with kinetic energy and momentum; annotate the wavelength shift Δλ = (h/mₑc)(1 − cos θ); small inset graph: measured vs. predicted wavelength shift as a function of scattering angle — data points on a smooth curve; caption: "If X-rays were purely waves, scattering off an electron changes direction, not wavelength. Compton found the wavelength changed. The billiard-ball calculation matched. Photons have momentum."] -->

---

## The Electrons That Are Waves

In 1924, a French graduate student named Louis de Broglie submitted a doctoral thesis with a symmetrical proposal: if light, previously thought to be a wave, has particle properties, perhaps electrons, previously thought to be particles, have wave properties. He proposed that any particle with momentum $p$ has an associated wavelength:

$$\lambda = \frac{h}{p}$$

The thesis committee was uncertain whether to accept it. They sent it to Einstein, who replied that de Broglie's idea was "of fundamental importance." The doctorate was awarded.

Three years later, Clinton Davisson and Lester Germer at Bell Labs confirmed it by accident.

They had been studying the surface of nickel by bombarding it with electrons since 1923. An accident in the laboratory — air leaked into the vacuum chamber, oxidizing the nickel sample — forced them to heat the sample to remove the oxide. The heating recrystallized the polycrystalline nickel into a small number of large crystal domains. When they resumed the experiment, the diffuse scatter they had been measuring vanished and was replaced by sharp peaks at specific angles.

This is the unmistakable signature of diffraction. Waves passing through a regular array of obstacles produce constructive interference at angles given by Bragg's law: $n\lambda = 2d\sin\theta$, where $d$ is the spacing between planes of atoms. They calculated the electron wavelength from de Broglie's formula using the known electron momentum. The Bragg condition predicted peaks at exactly the angles where Davisson and Germer saw them. Electrons are waves.

<!-- → [DIAGRAM: Davisson-Germer electron diffraction — left: schematic of the experiment showing an electron gun, the nickel crystal at center, and a movable detector on an arc; right: the polar plot of scattered electron intensity vs. angle — a sharp peak at ~50° for 54 V electrons, contrasted with the smooth featureless scatter expected from a classical particle; annotate the de Broglie wavelength (0.167 nm) and the Bragg-predicted peak angle; caption: "The sharp peak is the signature of diffraction — constructive interference of the electron's wave at specific angles. Classical particles scatter smoothly. Waves do not."] -->

For an electron accelerated through 54 volts, the kinetic energy is 54 eV, the momentum is $p = \sqrt{2m_e \cdot 54\text{ eV}}$, and the de Broglie wavelength works out to about 0.167 nm — comparable to the atomic spacing in nickel, which is why diffraction was visible at all.

Why don't we see wave behavior in everyday objects? Because $h$ is tiny and macroscopic momenta are enormous. A bowling ball of mass 3 kg moving at 10 m/s has momentum 30 kg·m/s and de Broglie wavelength:

$$\lambda = \frac{6.63 \times 10^{-34}}{30} \approx 2 \times 10^{-35} \text{ m}$$

That is $10^{20}$ times smaller than the diameter of a proton. To see diffraction you need an aperture comparable to the wavelength. No such aperture exists. The wave nature of the bowling ball is real but completely undetectable.

For an electron at 100 eV, the wavelength is about 0.12 nm — comparable to atomic spacings. The wave nature is detectable and consequential. This is why transmission electron microscopes, which accelerate electrons to tens or hundreds of kilovolts, achieve resolution thousands of times better than optical microscopes. Visible light has wavelengths around 500 nm; a 200 keV electron has a de Broglie wavelength of about 0.003 nm. The diffraction limit — the fundamental resolution limit of any imaging system — scales with wavelength. Shorter wavelength means sharper images.

The de Broglie wavelength for an electron accelerated through voltage $V$ is:

$$\lambda = \frac{h}{\sqrt{2m_e eV}}$$

For $V = 100$ V, this gives $\lambda \approx 0.123$ nm. For $V = 200,000$ V (a typical electron microscope), relativistic corrections become necessary, but the principle is the same.

G. P. Thomson — son of J. J. Thomson, who had discovered the electron by measuring its particle properties — demonstrated electron diffraction independently in 1927 by passing electrons through thin gold foil, exactly as X-rays are diffracted. Davisson and G. P. Thomson shared the Nobel Prize in 1937. J. J. Thomson won the Nobel in 1906 for showing the electron is a particle. His son won it for showing the electron is a wave. The same object. Both descriptions correct.

By the 1990s and 2000s, diffraction and interference had been demonstrated with neutrons, atoms, and eventually molecules of hundreds of atoms — including buckminsterfullerene C₆₀ by Anton Zeilinger's group in Vienna in 1999. Wave-particle duality is not a quirk of electrons. It is universal.

<!-- → [CHART: de Broglie wavelength across scales — horizontal axis: objects ordered by mass (log scale, from electron ~10⁻³⁰ kg to baseball ~0.1 kg); vertical axis: de Broglie wavelength (m, log scale); plot the curve λ = h/mv at typical speeds for each; annotate: electron in atom (~0.5 Å, "comparable to atomic spacing — diffraction observable"), slow neutron (~1 Å, "neutron scattering, basis of materials science"), C₆₀ molecule (~0.003 Å, "interference demonstrated 1999"), baseball (~10⁻³⁴ m, "10²⁰ × smaller than a proton — undetectable"); shade the region "smaller than a proton" to mark where wave nature is physically meaningless at any practical scale] -->

---

## The Uncertainty That Is Not Ignorance

In March 1927, Werner Heisenberg, twenty-five years old, working at the Niels Bohr Institute in Copenhagen, derived a relation that changed what physics could even ask.

The starting point was a concrete thought experiment. To measure where an electron is, you illuminate it — bounce a photon off it and observe where the photon goes. But the photon has momentum $p = h/\lambda$. When it scatters off the electron, it transfers some of that momentum to the electron, disturbing its state. To locate the electron more precisely, you need a shorter wavelength photon — higher frequency, more energetic, more momentum — which disturbs the electron more violently. There is an irreducible trade-off.

Heisenberg showed that this trade-off is not an experimental limitation that better instruments could overcome. It is a structural property of quantum states themselves. Position and momentum cannot both be sharply defined simultaneously. The product of their uncertainties obeys:

$$\Delta x \cdot \Delta p \geq \frac{h}{4\pi}$$

The same relation holds for energy and time:

$$\Delta E \cdot \Delta t \geq \frac{h}{4\pi}$$

The notation $h/4\pi$ appears because $\hbar = h/(2\pi)$ is the natural unit in quantum mechanics, and the bound is $\hbar/2$. Different textbooks write it different ways; the content is identical.

These are not statements about our ignorance. They are statements about what quantum states exist. A particle cannot be in a state that has both definite position and definite momentum — because such a state does not exist. This follows from the mathematics of Fourier transforms: a wave with perfectly definite wavelength (perfectly definite momentum) has no definite position at all — it extends across all space. A wave with perfectly definite position is a spike that contains contributions from all possible wavelengths — all possible momenta. The relation between position-space and momentum-space representations of the wavefunction is a Fourier transform, and the uncertainty principle is a theorem about Fourier transforms. It has nothing to do with clumsy measurement. It is mathematics.

<!-- → [DIAGRAM: the Fourier uncertainty — two side-by-side pairs of waveforms; top pair: a plane wave (left, extends infinitely, perfectly definite wavelength = definite momentum) and its Fourier transform (right, a spike at one frequency = completely undefined position); bottom pair: a localized spike (left, completely defined position) and its Fourier transform (right, spread across all frequencies = completely undefined momentum); caption: "The uncertainty principle is a theorem about Fourier transforms. A wave with one definite wavelength has no definite position. A wave with one definite position contains all wavelengths. You cannot have both. This is mathematics, not measurement clumsiness."] -->

The most important application of the uncertainty principle is the one you carry with you every moment: the stability of atoms.

An electron bound to a proton in a hydrogen atom is confined to a region of roughly $10^{-10}$ m. The uncertainty in its position is therefore at most $\Delta x \sim 10^{-10}$ m. The minimum uncertainty in its momentum follows:

$$\Delta p \geq \frac{h}{4\pi \Delta x} = \frac{6.63 \times 10^{-34}}{4\pi \times 10^{-10}} \approx 5.3 \times 10^{-25} \text{ kg·m/s}$$

The corresponding kinetic energy is:

$$KE \sim \frac{p^2}{2m_e} = \frac{(5.3 \times 10^{-25})^2}{2 \times 9.11 \times 10^{-31}} \approx 1.5 \times 10^{-19} \text{ J} \approx 0.95 \text{ eV}$$

The hydrogen ground state actually has a kinetic energy of 13.6 eV — larger than this estimate, because the atom's size is about five times smaller than the $10^{-10}$ m we assumed. But the uncertainty principle gives the right order of magnitude, and more importantly, it explains why the electron does not collapse into the proton.

Classically, a negative charge orbiting a positive charge would radiate, lose energy, spiral inward, and collapse in about $10^{-11}$ seconds. This is not a subtlety of the model — it is a direct consequence of classical electromagnetism. Classical atoms cannot be stable. The argument was well-known in 1911 when Rutherford discovered the nuclear atom, and it was a genuine crisis: the observed fact that atoms exist contradicted classical physics directly.

The uncertainty principle resolves the crisis. Suppose the electron were confined to a region of size $r$ around the proton. Its minimum kinetic energy from the uncertainty principle is roughly $\hbar^2/(2m_e r^2)$. Its potential energy from Coulomb attraction is $-ke^2/r$. The total energy as a function of $r$ has a minimum at a finite value — the Bohr radius $a_0 \approx 0.53 \times 10^{-10}$ m. Below that radius, the kinetic energy from confinement grows faster than the electrostatic energy gained by getting closer, and the total energy increases. The atom is stable not despite quantum mechanics but because of it. The uncertainty principle is the reason you exist.

<!-- → [DIAGRAM: hydrogen atom total energy vs. electron confinement radius — horizontal axis: radius r from 0 to ~5 Å; vertical axis: energy (eV, from −15 to +10); plot three curves: kinetic energy from uncertainty principle (KE ~ ℏ²/2mₑr², falls as r increases), Coulomb potential energy (PE = −ke²/r, rises toward zero as r increases), and total energy E = KE + PE (has a minimum at r = a₀ ≈ 0.53 Å, labeled "Bohr radius — energy minimum"); annotate the minimum energy (−13.6 eV, the hydrogen ground state); caption: "Squeeze the electron closer and kinetic energy from confinement rises faster than Coulomb attraction falls. The atom's stable size is where total energy is minimized — a balance set by Planck's constant."] -->

---

## What It Adds Up To

Three experimental results. Three equations. One constant.

Blackbody radiation forced the quantization of oscillator energies: $\Delta E = hf$. The photoelectric effect confirmed that light itself is quantized: $E = hf$, $p = h/\lambda$. Electron diffraction confirmed that matter has wave properties: $\lambda = h/p$. The uncertainty principle showed that position and momentum are complementary: $\Delta x \, \Delta p \geq h/4\pi$.

In every case the same constant $h = 6.626 \times 10^{-34}$ joule-seconds. The smallness of this number is why we can do classical physics for cars and bridges — at macroscopic scales, $h$ is negligible compared to the relevant products of energy times time or momentum times position, and quantum effects vanish. The non-zero-ness of $h$ is why classical physics fails for atoms — at atomic scales, $h$ is not negligible, and quantum effects are everything.

There is a pattern worth noticing. Classical physics had two separate categories: waves (continuous, spread through space, superposable) and particles (discrete, localized, with definite trajectories). Quantum mechanics dissolves the distinction. Photons are quantized packets of what was previously a wave. Electrons are matter waves with particle-like detection. Neither classical category applies to either object. What applies to both is the same framework — the wavefunction, whose squared magnitude gives the probability of detecting the particle at any location — and the same constant governing the scale at which the classical categories break down.

The mathematical machinery that grew from these observations between 1925 and 1928 — Heisenberg's matrix mechanics, Schrödinger's wave equation, Dirac's relativistic extension — has made more correct predictions, tested more precisely, than any other theory in science. The spectrum of hydrogen: exact. The magnetic moment of the electron: exact to twelve decimal places. The properties of semiconductors: sufficient to build every transistor in every computer ever made. Lasers, LEDs, MRI, atomic clocks, solar cells: all quantum mechanical at their core.

We do not understand why the wavefunction is what it is. We do not know what the correct interpretation of quantum mechanics is — whether the wavefunction describes physical reality directly, or encodes our knowledge of it, or something else entirely. These questions remain open. They are not engineering questions. They are philosophy of physics questions, and honest physicists disagree about the answers.

What is not in doubt: the equations are correct, the predictions are verified, and the world at small scales is not classical. The corrections are not small.

---

## LLM Exercise — Chapter 10: Quantum Physics in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A Logbook entry for quantum physics. Like Chapter 28, most everyday phenomena don't visibly involve quantum effects, but every electronic device, every photon-detecting eye, every chemical bond does. You can either compute a quantum-mechanical correction to your phenomenon or write an "exception entry" identifying the most distant quantum connection (often LEDs, displays, or sensors).
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs.
My anchor phenomenon is [paste your 1-sentence description].

For Chapter 29, I want to think about quantum physics. Most everyday phenomena
are classical at the macroscopic level, but rely on quantum mechanics in their
components (LEDs, screens, sensors, the eye's photoreceptors).

Please:

1. Identify ONE quantum-mechanical aspect of my phenomenon. Examples: for a
bike commute — the LED traffic signals (each photon emission is a quantum
transition), the photoreceptors in my eye (single-photon detection), the
silicon in my smartphone display (quantum band structure). For a coffee maker —
the electric heating element (Ohm's law breaks down at quantum level), the LED
indicator lights, the chemical bonds in the coffee compounds. For a basketball
shot — the gym lighting, the chemical bonds in the basketball's polyurethane,
my visual system. For a marathon — the GPS watch's display, the chemical bonds
in the energy gels.

2. Apply ONE quantum equation. Compute photon energy from a relevant wavelength:
a chip's bandgap energy (silicon ~1.1 eV → ~1100 nm), an LED color, a UV-
protective coating. Or compute the de Broglie wavelength of an electron in a
transistor.

3. Specify input numbers and uncertainty.

4. Run the calculation. Report value with units.

5. One sentence on what would happen if quantum mechanics were "off" — what
specific failures would occur in technology I use.

6. One sentence connecting this to Chapter 30 (atomic physics) — atomic
structure is the next chapter.

Save the output as logbook/chapter-29-quantum.md.
```

### What this produces

A Logbook entry that locates the quantum physics in your phenomenon. Often the answer is "every chip and every LED is a quantum device."

### How to adapt this prompt

- *For phenomena heavy on chemistry (food, drink, materials):* Every chemical bond is quantum mechanical. The Pauli exclusion principle (which we'll meet in Chapter 30) is what makes atoms have shells.
- *For ChatGPT/Gemini:* Identical with interface substitutions.
- *For Claude Code:* If you have spectroscopic data (e.g., from a hyperspectral camera image), you can use Claude Code to extract photon energies from observed wavelengths.

### Connection to previous chapters

Builds directly on Chapter 24 (EM spectrum) and Chapter 27 (wave behavior of light). Uses Chapter 28's relativistic energy-momentum relation for massless particles ($E = pc$) and the correspondence principle.

### Preview of next chapter

Chapter 30 (atomic physics) applies quantum mechanics to atoms specifically — Bohr's model, the hydrogen spectrum, quantum numbers, the Pauli principle, and the periodic table.

---

## AI Wayback Machine

**Max Planck** introduced the quantum hypothesis in 1900 — proposing that energy comes in discrete packets to explain blackbody radiation. He spent the rest of his life uncomfortable with what his idea unleashed.

**Run this:**

```
Who was Max Planck, and how does his quantum hypothesis connect to the
quantum physics we covered in this chapter? Keep it to three paragraphs.
End with the single most surprising thing about his career or ideas.
```

→ Search **"Max Planck"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how Planck's quantization assumption resolves the ultraviolet catastrophe.
- Ask it about Planck's quiet resistance to Nazi science policy during the war.

What changes? What gets better? What gets worse?
