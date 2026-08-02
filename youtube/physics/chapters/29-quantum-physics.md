# Chapter 29 — Quantum Physics

*The world at small scales is not classical. The corrections are not small.*

---

In 1927, Clinton Davisson and Lester Germer were bombarding a nickel crystal with electrons in a vacuum chamber at Bell Labs. They had been doing this for four years, studying nickel surfaces for telephone-relay applications. Then an accident: air leaked in, oxidizing the sample. They annealed the nickel to remove the oxide, and the annealing recrystallized the polycrystalline metal into a few large single-crystal regions.

When they resumed, the electrons no longer scattered diffusely. They produced sharp, peaked angular patterns — the unmistakable signature of diffraction.

Electrons were interfering with themselves. Like waves.

Three years earlier, a French doctoral student named Louis de Broglie had proposed that all matter has wave properties, with wavelength $\lambda = h/p$. His examining committee didn't know what to make of it. Einstein, consulted, said the idea was "of fundamental importance." They gave him the degree. Now, in 1927, Davisson and Germer measured the angles. They matched de Broglie's formula exactly. The Nobel Prize for de Broglie came in 1929. The Nobel for Davisson (and G. P. Thomson, who did the same thing with gold foil) came in 1937.

G. P. Thomson was the son of J. J. Thomson, who had discovered the electron in 1897 and proved it was a particle. Father wins Nobel Prize for showing the electron is a particle. Son wins Nobel Prize for showing the electron is a wave. Physics in the twentieth century.

![Spectral radiance vs wavelength for three temperatures: 3000 K, 5800 K (Sun), 8000 K. Each curve peaks (Wien displacement). Hotter peaks at shorter wavelength. Dashed classical Rayleigh-Jeans curve diverges at small λ — solved...](../images/29-quantum-physics-fig-02.png)
*Figure 29.2 — Blackbody Curves — Planck Fits Where Rayleigh-Jeans Diverges (UV Catastrophe)*

By the late 1920s, classical physics was in pieces. The pieces pointed toward the same fix: Planck's constant $h = 6.626 \times 10^{-34} \text{ J·s}$, a tiny number that set the scale of every failure. Light came in discrete packets with energy $E = hf$. Matter had wave properties with wavelength $\lambda = h/p$. Position and momentum could not simultaneously be sharp, their uncertainties bounded by $h$. Three experimental facts, one constant.

This chapter is about those three facts and what they require you to give up about the classical picture of the world.

---

## Photons: light in discrete packets

In December 1900, Max Planck stood before the German Physical Society with a result he found philosophically disturbing. For two years he had been trying to derive the spectrum of electromagnetic radiation from a hot body — the blackbody spectrum. Classical electromagnetism combined with classical statistical mechanics gave a catastrophic answer: total radiated energy diverged at short wavelengths. Hot objects don't emit infinite energy. The prediction was simply wrong.

Planck found the formula that fit the data. But getting it required an assumption he couldn't derive and didn't believe: the oscillating atoms in the body can only have energies that are integer multiples of $hf$, where $f$ is the oscillator's frequency. Take that, and the spectrum comes out right. He published it as a "purely formal" trick and spent years trying to make it go away. He could not.

In 1905, Einstein took Planck's assumption and made it physical. He proposed that electromagnetic radiation itself is quantized — not just the oscillators, but the field. Light comes in discrete bundles, each carrying

$$E = hf = \frac{hc}{\lambda}.$$

He called them *light quanta*. We call them **photons**.

![Plot of maximum kinetic energy of ejected electrons vs frequency of incident light, for two metals (sodium W=2.36 eV, copper W=4.7 eV). Lines start at threshold f_0 = W/h; slope = h (Planck's constant). Below threshold: no...](../images/29-quantum-physics-fig-03.png)
*Figure 29.3 — Photoelectric Effect — Linear Above Threshold, No Electrons Below*

His evidence was the **photoelectric effect**. Shine light on a metal and electrons are ejected. The puzzle, outstanding for two decades: the energy of individual ejected electrons depends on the *frequency* of the light, not its *intensity*. Bright low-frequency light ejects no electrons. Dim high-frequency light ejects electrons with substantial kinetic energy. Classical wave theory says intensity determines energy — louder wave, more energetic impact. Experiment said no.

Einstein's explanation is clean. A photon of frequency $f$ carries energy $hf$. When it hits the metal, it gives all of its energy to a single electron. If $hf$ exceeds the energy required to free the electron from the surface — the **work function** $\phi$ — the electron escapes with kinetic energy

$$KE_\text{max} = hf - \phi.$$

If $hf < \phi$, no electrons escape, regardless of intensity. More intensity means more photons per second, which means more electrons ejected per second, but each electron's energy is set by each individual photon. The intensity-energy decoupling follows immediately.

Einstein submitted this paper in 1905 — the same year as special relativity. It was the photoelectric paper, not relativity, that won him the 1921 Nobel Prize. The Nobel committee considered relativity still too controversial. The citation reads: "for his services to theoretical physics, and especially for his discovery of the law of the photoelectric effect."

A useful shorthand: $hc = 1240 \text{ eV·nm}$. A 500 nm green photon has energy $1240/500 = 2.48 \text{ eV}$. A 400 nm violet photon: $1240/400 = 3.10 \text{ eV}$. Working the photoelectric effect: if the work function is $2.20 \text{ eV}$ and the photon is $3.10 \text{ eV}$, then $KE_\text{max} = 0.90 \text{ eV}$. The threshold wavelength — below which no electrons escape — is $\lambda_0 = hc/\phi = 1240/2.20 = 564 \text{ nm}$. Any wavelength longer than yellow-green (yellow, orange, red, infrared) cannot free electrons from this metal regardless of beam brightness.

Photons also carry momentum:

$$p = \frac{h}{\lambda} = \frac{E}{c}.$$

This follows from the relativistic energy-momentum relation (Chapter 28): for a massless particle, $E = pc$, so $p = E/c = hf/c = h/\lambda$. Arthur Compton confirmed the momentum in 1923. He scattered X-rays off electrons and measured both the recoil of the electrons and the shift in the X-ray wavelength. The X-rays came back at longer wavelength — exactly the prediction if you treat the collision as a billiard-ball interaction between a photon with momentum $h/\lambda$ and an electron at rest. The Compton wavelength shift:

$$\Delta\lambda = \frac{h}{m_e c}(1 - \cos\theta),$$

where $h/m_e c \approx 2.43 \text{ pm}$ is the electron's Compton wavelength and $\theta$ is the scattering angle. The agreement with experiment was exact. Photons are particles with momentum. Not "sort of" particles. Particles with momentum, governed by relativistic collision kinematics.

<!-- → [CHART: photoelectric effect — two-panel diagram: left panel shows photon energy E = hf vs. frequency f as a straight line with slope h, with work function φ marked as the y-intercept of the KE_max axis; right panel shows KE_max of ejected electrons vs. photon frequency, a straight line starting at threshold frequency f₀ = φ/h with slope h; annotate that the slope of both lines is Planck's constant h, which Einstein's theory predicts and experiment confirms — student should see that measuring the slope gives h independently of the work function] -->

---

## Matter waves: de Broglie and the Davisson-Germer experiment

De Broglie's proposal is simple to state: every particle with momentum $p$ has a wavelength

$$\lambda = \frac{h}{p}.$$

For a slow particle, $p = mv$, so $\lambda = h/(mv)$. For a relativistic particle, use the full relativistic momentum from Chapter 28.

Why do we never notice this for everyday objects? A 3-kilogram bowling ball at 10 m/s has momentum 30 kg·m/s and de Broglie wavelength

$$\lambda = \frac{6.63 \times 10^{-34}}{30} \approx 2 \times 10^{-35} \text{ m}.$$

That is $10^{20}$ times smaller than a proton. To see diffraction, you need a slit comparable in width to the wavelength. No such slit exists or could. The bowling ball's wave nature is real and completely invisible.

For an electron accelerated through 100 V: kinetic energy $= 100 \text{ eV}$, momentum $p = \sqrt{2 m_e \cdot KE}$, wavelength

$$\lambda = \frac{h}{\sqrt{2 m_e eV}} \approx 0.123 \text{ nm}.$$

![Schematic of Davisson-Germer experiment: electron gun fires electrons at nickel crystal; detector measures scattered intensity vs angle. Peak at specific angle confirms Bragg condition for matter waves with λ = h/p. Detector...](../images/29-quantum-physics-fig-01.png)
*Figure 29.1 — Davisson-Germer (1927) — Electrons Diffract Through a Crystal: Matter Is Wave*

This is comparable to atomic spacings — roughly half an angstrom. When such electrons hit a crystal, the spacing between atomic planes is a natural diffraction grating at just the right scale. The Bragg condition $n\lambda = 2d\sin\theta$ predicts diffraction peaks at specific angles. Davisson and Germer measured those angles. They matched.

The same experiment was done with neutrons (thermal neutrons have $\lambda \sim$ a few angstroms, ideal for crystal studies), with atoms, with small molecules. In 1999, Anton Zeilinger's group at Vienna sent $C_{60}$ buckminsterfullerene molecules — sixty carbon atoms — through a diffraction grating and observed interference fringes. By 2019, the record was molecules of nearly 2,000 atoms. Wave-particle duality is universal and has no known upper size limit.

The modern transmission electron microscope, operating at 200 keV, has a de Broglie wavelength of roughly $2.5 \text{ pm}$ — smaller than atomic radii. This is why TEM achieves sub-angstrom resolution while the best optical microscope is limited to ~200 nm by the diffraction limit. The limit is not engineering; it is physics. Smaller wavelength, finer resolution.

![Two panels side by side. Photons through a double slit: interference fringes build up one photon at a time, statistical wave pattern. Electrons through the same double slit: identical interference. Matter is wave; light is...](../images/29-quantum-physics-fig-04.png)
*Figure 29.4 — Double-Slit With Photons OR Electrons — Same Interference Pattern*

The philosophical consequence is unavoidable. There is no sharp boundary between "wave" and "particle." Every quantum object is described by a **wavefunction** whose squared magnitude gives the probability of finding the object at any location. Send a single electron toward two slits: the electron is detected as a single localized dot on the far side — particle-like, one spot. But send many electrons, one at a time, and the accumulated pattern of dots builds an interference fringe — wave-like, from something that arrived one at a time, each hitting in a single spot.

The interference is not from one electron interacting with another. Each electron interferes with itself. Feynman described this as "the only mystery" in quantum mechanics. If you understand why it happens, you understand the theory. If you feel uncomfortable with it, that is the correct response — not because the theory is wrong, but because the theory is telling you that classical intuition simply does not apply at this scale.

<!-- → [INFOGRAPHIC: de Broglie wavelength vs. kinetic energy for electrons — log-log plot showing λ decreasing from ~12 Å at 1 eV to ~0.03 Å at 10 keV; mark key points: Davisson-Germer at 54 V (λ ≈ 1.67 Å, comparable to nickel lattice spacing 2.15 Å), TEM at 200 keV (λ ≈ 0.025 Å, sub-atomic resolution); draw a horizontal band for visible light wavelengths (400–700 nm) to show the enormous scale gap that gives electron microscopes their resolution advantage] -->

---

![Plot of Δp vs Δx with hyperbolic floor Δp = ℏ/(2 Δx). Three regimes labeled: localized particle (small Δx → large Δp), spread-out wave (large Δx → small Δp), trade-off frontier. Not a measurement limitation — a property of...](../images/29-quantum-physics-fig-05.png)
*Figure 29.5 — Heisenberg Uncertainty — Δx · Δp ≥ ℏ/2, A Hyperbolic Floor*

## The Heisenberg uncertainty principle

In March 1927, Werner Heisenberg — twenty-five years old at the Niels Bohr Institute in Copenhagen — published a paper that changed what it means to know something.

His starting observation was mundane: to measure where an electron is, you must bounce photons off it. A photon carries momentum $h/\lambda$. The shorter the wavelength (better position resolution), the higher the momentum kick to the electron. So measuring position disturbs momentum. There is a tradeoff.

But Heisenberg proved something stronger. The tradeoff is not a consequence of imperfect measurement technique. It is a property of quantum states themselves. There exists no quantum state in which position and momentum are simultaneously sharp. The bound is

$$\Delta x \cdot \Delta p \geq \frac{h}{4\pi}.$$

This is Heisenberg's position-momentum uncertainty principle. The same structure holds for energy and time:

$$\Delta E \cdot \Delta t \geq \frac{h}{4\pi}.$$

The principle is not a statement about our ignorance. It is a statement about what nature permits. A sharply localized state (small $\Delta x$) necessarily has a broad momentum distribution (large $\Delta p$), and vice versa. This is forced by the mathematics of wavefunctions: position and momentum are related by a Fourier transform, and a narrow Fourier transform in position space is a wide one in momentum space. The uncertainty is not a gap in knowledge; it is a gap in the structure of the state.

The energy-time version has a direct application: every excited atomic state has a finite lifetime $\tau$. The energy of the emitted photon is therefore uncertain by $\Delta E \geq h/(4\pi\tau)$. This spreads the emitted spectral line into a range of frequencies — the "natural linewidth" of the transition. For a typical atomic transition with $\tau \sim 10^{-8} \text{ s}$, the linewidth is $\Delta f \sim h/(4\pi\tau \cdot h) = 1/(4\pi\tau) \sim 8 \times 10^6 \text{ Hz}$ — about 8 MHz. This is not an instrumental artifact. It is the fundamental width of the line.

The most striking consequence is atomic stability. An electron confined to an atom of radius $r \sim 10^{-10} \text{ m}$ has momentum uncertainty

$$\Delta p \geq \frac{h}{4\pi \Delta x} \approx \frac{6.63 \times 10^{-34}}{4\pi \times 10^{-10}} \approx 5.3 \times 10^{-25} \text{ kg·m/s},$$

corresponding to kinetic energy

$$KE \sim \frac{p^2}{2m_e} \approx 0.95 \text{ eV}.$$

Now ask: what happens if the electron tries to collapse onto the proton? As $\Delta x \to 0$, the momentum uncertainty $\Delta p \to \infty$, and the kinetic energy grows without bound. The Coulomb attraction that pulls the electron toward the proton is eventually overwhelmed. The atom finds the radius where attractive Coulomb energy and repulsive confinement kinetic energy balance — and that radius is the Bohr radius, $a_0 \approx 0.5 \text{ Å}$. The ground-state energy is $-13.6 \text{ eV}$.

You can derive this from scratch in two lines. Write the total energy as

$$E = \frac{p^2}{2m_e} - \frac{ke^2}{r}.$$

Use $r \cdot p \sim \hbar$ to eliminate $p$. Minimize $E(r)$. The minimum is at $r = a_0 = \hbar^2/(m_e ke^2) \approx 0.53 \text{ Å}$, and the energy there is $-13.6 \text{ eV}$. These are the exact quantum-mechanical values, obtained from one inequality and one derivative.

Atoms are stable because of the uncertainty principle. This is not poetry. It is the calculation.

<!-- → [INFOGRAPHIC: atomic stability from the uncertainty principle — energy diagram showing the balance between the attractive Coulomb potential (V = -ke²/r, curves down as r decreases) and the uncertainty-driven kinetic energy (KE ~ ℏ²/2mₑr², curves up steeply as r → 0); the sum of the two has a minimum at the Bohr radius a₀ ≈ 0.5 Å, with ground-state energy -13.6 eV; student should see that the atom cannot collapse because the kinetic energy diverges faster than the potential energy drops] -->

---

## One constant, three consequences

Pull back. Every failure of classical physics in this chapter has the same source: Planck's constant $h$ is nonzero.

From $E = hf$: electromagnetic radiation is quantized. The photoelectric effect only makes sense if light comes in discrete packets. The threshold frequency is real. No intensity of red light will ever free an electron from a metal with a 2.5 eV work function. Solar cells work because photons above the silicon band gap (1.1 eV) can free electrons; photons below it cannot, no matter how many arrive. LEDs work because electrons falling across a semiconductor band gap release photons with energy $E = hf$ at exactly the gap frequency.

From $\lambda = h/p$: matter has wave properties. Electron microscopes resolve atoms. Neutron diffraction maps crystal structures that X-rays cannot reach. The periodic table has the structure it does because electrons in atoms are standing waves — only certain wavelengths fit in the atomic "box," giving discrete energy levels, which give discrete spectral lines, which give spectroscopy, which tells us what stars are made of.

![Particle with energy E approaches a rectangular potential barrier of height V₀ > E. Inside the barrier, the wave function decays exponentially; outside, it propagates. Nonzero transmission amplitude — the particle "tunnels"...](../images/29-quantum-physics-fig-06.png)
*Figure 29.6 — Quantum Tunneling — Wave Function Decays Through a Forbidden Barrier*

From $\Delta x \, \Delta p \geq h/4\pi$: there is no quantum state with simultaneously sharp position and momentum. Atoms have finite size. Nuclei have finite size. The zero-point energy of any confined particle is nonzero. Every solid has a ground-state vibration even at absolute zero.

The unifying question: when does quantum mechanics matter? When the relevant action — momentum times position, or energy times time — is comparable to $h$. For a baseball, relevant actions are $\sim 10^{33} h$. Classical physics is exact to one part in $10^{33}$. For an electron in an atom, the relevant action is order $h$. Classical physics is wrong by order one.

A complete example. Hydrogen: one proton, one electron. The uncertainty principle gives $a_0 \approx 0.5 \text{ Å}$ and $E_1 = -13.6 \text{ eV}$. De Broglie says the electron's ground-state wavelength equals $2\pi a_0$ — one complete wave around the orbit. When the electron drops from $n = 2$ to $n = 1$, it releases a photon of energy

$$\Delta E = 13.6 - 3.4 = 10.2 \text{ eV}, \quad \lambda = \frac{1240}{10.2} = 122 \text{ nm}.$$

This is Lyman-$\alpha$, a UV line in the hydrogen spectrum. It was measured to high precision in the nineteenth century, before quantum mechanics. The theory predicts it exactly. All three concepts, from one constant, getting the right number.

<!-- → [INFOGRAPHIC: hydrogen energy levels and the Lyman-α transition — vertical energy level diagram with n=1 at bottom (-13.6 eV), n=2 (-3.4 eV), n=3 (-1.5 eV), n=∞ (0 eV); draw a downward arrow from n=2 to n=1 labeled ΔE = 10.2 eV, λ = 122 nm (UV, Lyman-α); draw a second arrow from n=3 to n=2 labeled ΔE = 1.9 eV, λ = 656 nm (red, Hα, visible Balmer series); annotate that every spectral line is a photon carrying exactly the energy difference between two levels via E = hf; student should see how the three concepts — uncertainty principle giving the energy levels, de Broglie giving the standing-wave condition, and E = hf connecting energy differences to photon wavelengths — combine to predict lines that were measured decades before the theory existed] -->

Photons, matter waves, and the uncertainty principle are not three separate puzzles. They are three aspects of the same fact: $h \neq 0$. Everything that follows in the remaining chapters — atomic structure, nuclear physics, the standard model — is the elaboration of that single fact at increasing scales of energy and decreasing scales of distance.

---

## Exercises

### Warm-up

**29.1** *(LO 1, 2)* Compute the energy in eV and the momentum in kg·m/s of: (a) a $650 \text{ nm}$ red photon, (b) a $121 \text{ nm}$ UV (Lyman-$\alpha$) photon, (c) a $1.5 \text{ GHz}$ microwave photon. Use $hc = 1240 \text{ eV·nm}$.

**29.2** *(LO 1)* Light of wavelength $280 \text{ nm}$ shines on a metal with work function $\phi = 3.00 \text{ eV}$. (a) Compute the photon energy. (b) Compute the maximum kinetic energy of ejected electrons. (c) What is the threshold wavelength for this metal? (d) Would $400 \text{ nm}$ light eject any electrons?

**29.3** *(LO 3)* Compute the de Broglie wavelength of: (a) an electron at $100 \text{ eV}$, (b) a proton at $100 \text{ eV}$ (use $m_p = 1836 m_e$), (c) a $70 \text{ kg}$ person walking at $1.5 \text{ m/s}$.

**29.4** *(LO 4)* An electron is confined to a region of size $\Delta x = 5.0 \times 10^{-11} \text{ m}$ (half the Bohr radius). (a) Find the minimum momentum uncertainty. (b) Find the corresponding minimum kinetic energy in eV.

### Application

**29.5** *(LO 1)* The threshold frequency for ejecting electrons from cesium is $f_0 = 4.60 \times 10^{14} \text{ Hz}$. (a) Find cesium's work function in eV. (b) Green light at $530 \text{ nm}$ shines on cesium. Find the maximum KE of ejected electrons. (c) Why is cesium used in photocells (hint: compare its threshold to visible light frequencies)?

**29.6** *(LO 2)* A $1.00 \text{ MeV}$ gamma ray photon. (a) Compute its momentum. (b) An electron has the same momentum — find its kinetic energy (use relativistic $E^2 = (pc)^2 + (m_e c^2)^2$ with $m_e c^2 = 0.511 \text{ MeV}$). (c) For the electron, is a relativistic treatment necessary?

**29.7** *(LO 3)* Electrons in a TEM are accelerated through $200 \text{ kV}$. (a) Find the relativistic momentum using $KE = 200 \text{ keV}$ and $E_\text{total} = KE + m_e c^2$. Then $p = \sqrt{E_\text{total}^2 - (m_e c^2)^2}/c$. (b) Compute the de Broglie wavelength. (c) Compare to the diffraction-limited resolution of a visible-light microscope (~200 nm). By what factor does TEM improve on this?

**29.8** *(LO 4)* An atomic transition has a natural lifetime $\tau = 2.0 \times 10^{-9} \text{ s}$. (a) Use the energy-time uncertainty relation to find the minimum energy spread $\Delta E$ of the emitted photon. (b) For a transition at $\lambda = 589 \text{ nm}$ (sodium yellow), convert $\Delta E$ to a frequency spread $\Delta f$ and a wavelength spread $\Delta\lambda$.

### Synthesis

**29.9** *(LO 1, 5)* Explain quantitatively why we don't observe the quantization of light in everyday life. A 100 W light bulb radiates primarily at $\lambda \approx 700 \text{ nm}$. (a) Compute the energy per photon. (b) How many photons per second does it emit? (c) If you could detect individual photons at that rate, each at a random time, would the stream look continuous or discrete to you? At what photon rate would individual arrivals become detectable?

**29.10** *(LO 1, 3)* A silicon solar cell has a band gap of $1.12 \text{ eV}$. (a) What is the threshold wavelength — below which photons can free electrons and above which they cannot? (b) The solar spectrum peaks near $500 \text{ nm}$. Can those photons free electrons in silicon? (c) What fraction of the solar spectrum (by wavelength range) is above the threshold? Why doesn't the solar cell convert all incident energy?

**29.11** *(LO 3, 4)* A proton is confined to a nucleus of radius $r \sim 10^{-15} \text{ m}$. (a) Use $\Delta x \sim r$ to estimate the momentum uncertainty. (b) Estimate the kinetic energy in MeV. (c) Compare to the nuclear binding energy per nucleon (~8 MeV). (d) A free proton has de Broglie wavelength $\lambda$ at this kinetic energy — compute $\lambda$ and compare to nuclear size.

### Challenge

**29.12** *(LO 1, beyond chapter)* Construct a thought experiment that rules out the classical wave picture of the photoelectric effect. Suppose light is a continuous wave of intensity $I$ and the metal's surface atoms each present an absorbing area $A \sim (1 \text{ Å})^2$. (a) How long would an atom need to absorb $3.0 \text{ eV}$ of energy from a beam of intensity $10^{-3} \text{ W/m}^2$? (b) Does this match the observed immediate ejection of electrons? (c) What does this tell you about the classical wave picture?

**29.13** *(LO 3, 4, beyond chapter)* In 1999, Zeilinger's group showed that $C_{60}$ molecules (mass $\approx 1.2 \times 10^{-24} \text{ kg}$) passing through a grating with $d = 100 \text{ nm}$ slits produced interference fringes. The molecules were at temperature $T \approx 900 \text{ K}$. (a) Estimate the thermal momentum using $KE = \frac{3}{2}k_BT$, then $p = \sqrt{2mKE}$. (b) Compute the de Broglie wavelength. (c) Using Bragg's condition approximately ($\lambda \sim d\sin\theta$ for first maximum), estimate the angular position of the first fringe. (d) What does this experiment tell us about the upper size limit of quantum wave behavior?

---



By the end of this chapter you should be able to:

1. Explain why the photoelectric effect and blackbody radiation cannot be explained by classical wave physics, and compute photon energies using $E = hf = hc/\lambda$.
2. Apply photon momentum $p = h/\lambda$ and verify consistency with the relativistic $E = pc$ for massless particles.
3. Apply the de Broglie relation $\lambda = h/p$ to compute the wavelength of any particle, and explain why matter wave behavior is unobservable at macroscopic scales.
4. Apply the position-momentum uncertainty principle $\Delta x \, \Delta p \geq h/4\pi$ and the energy-time version $\Delta E \, \Delta t \geq h/4\pi$ to estimate fundamental measurement limits and explain atomic stability.
5. Use the correspondence principle to confirm that quantum predictions reduce to classical ones when $h$ is negligible compared to the action scales of the system.

**Prerequisites.** Chapter 24 (electromagnetic spectrum, $c = f\lambda$). Chapter 27 (diffraction, interference, the diffraction limit). Chapter 28 (relativistic energy-momentum, $E = pc$ for massless particles).

**Why this chapter matters.** Quantum mechanics is the foundation of chemistry, semiconductor physics, optics, and nuclear physics. Every transistor, LED, laser, solar cell, and MRI machine works because $h \neq 0$ and the theory built on that fact is correct. The next four chapters are applications of what this chapter installs.

---

## ↳ Dig Deeper — Compton scattering and photon momentum

*The chapter introduces photon momentum $p = h/\lambda$. Arthur Compton's 1923 experiment provides the cleanest evidence: X-rays scattered off electrons emerge at longer wavelength, exactly as predicted by treating the collision as a relativistic two-body interaction.*

**Prompt:**
> Walk through the Compton scattering experiment. (a) Set up the kinematics: an X-ray photon of wavelength $\lambda_0$ scatters off an electron at rest, deflecting by angle $\theta$ and emerging with wavelength $\lambda > \lambda_0$. The Compton formula gives $\Delta\lambda = (h/m_e c)(1 - \cos\theta)$, where $h/m_e c \approx 2.43 \text{ pm}$ is the Compton wavelength of the electron. (b) Sketch how this follows from energy and momentum conservation, treating the photon as a particle with $E = hc/\lambda$ and $p = h/\lambda$. (c) Compute the wavelength shift for $\theta = 90°$. End with one sentence on why this experiment was decisive evidence that photons carry momentum like particles.

**What to do with the output:** Save it. Compton scattering is the cleanest demonstration that photons are particles with momentum, and the calculation is a direct application of relativistic kinematics from Chapter 28.

---

## ↳ Dig Deeper — The single-electron double-slit experiment

*The chapter says electrons sent through two slits one at a time produce an interference pattern. The empirical build-up — each electron arrives as a single spot, but many together form fringes — is among the most direct demonstrations of quantum mechanics ever performed.*

**Prompt:**
> Describe the single-electron double-slit experiment. Walk through: (a) the setup — electron source, two slits, a detector recording single arrivals; (b) the observation — each electron is a single spot on the screen, but many electrons together build an interference pattern; (c) what happens when a "which-slit" detector is added (the interference pattern disappears). End with one sentence on the Tonomura 1989 experiment, which showed this build-up directly.

**What to do with the output:** Save it. Feynman called this "the only mystery" in quantum mechanics.

---

## ↳ Dig Deeper — Deriving atomic size from the uncertainty principle

*The chapter asserts that the uncertainty principle stabilizes atoms. The two-line derivation — express energy as a function of confinement radius, minimize — gives the Bohr radius and the hydrogen ground-state energy from one inequality and one derivative.*

**Prompt:**
> Derive the size and ground-state energy of the hydrogen atom from the uncertainty principle. Write the total energy as $E = p^2/(2m_e) - ke^2/r$. Use $r \cdot p \sim \hbar$ to eliminate $p$ in terms of $r$. Minimize $E(r)$ to find the equilibrium radius (Bohr radius $a_0 \approx 0.5 \text{ Å}$) and the ground-state energy ($\approx -13.6 \text{ eV}$). End with one sentence on why this estimate is so close to the exact quantum-mechanical answer.

**What to do with the output:** Save it. This is one of the most elegant order-of-magnitude estimates in physics: the size of an atom from one inequality and one derivative.

---

## LLM Exercise — Chapter 29: Quantum Physics in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A Logbook entry locating quantum physics in your phenomenon.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste your 1-sentence description].

For Chapter 29, I want to think about quantum physics. Most everyday phenomena are classical at the macroscopic level, but rely on quantum mechanics in their components (LEDs, screens, sensors, the eye's photoreceptors).

Please:

1. Identify ONE quantum-mechanical aspect of my phenomenon. Examples:
   - Bike commute: LED traffic signals (each photon is a quantum transition), silicon photodetectors, the chemical bonds in tires.
   - Coffee maker: the LED indicator light, the heating element's electrical behavior, the chemical bonds in coffee compounds.
   - Basketball shot: the gym lighting, the chemical bonds in the ball material, my retinal photoreceptors.
   - Marathon: the GPS watch display, chemical bonds in energy gels, retinal photoreceptors detecting the finish tape.

2. Apply ONE quantum equation. Compute photon energy from a relevant wavelength (an LED color, a silicon bandgap ~1.1 eV → ~1130 nm), or compute the de Broglie wavelength of an electron in a transistor.

3. Specify input numbers and uncertainty.

4. Run the calculation. Report with units.

5. One sentence on what would happen if quantum mechanics were "off" — what specific failures would occur in technology I depend on.

6. One sentence connecting to Chapter 30 (atomic physics) — quantum mechanics applied to atomic structure.

Save the output as logbook/chapter-29-quantum.md.
```

### What this produces

A Logbook entry locating the quantum physics in your phenomenon. Almost always: every chip and every LED is a quantum device.

### How to adapt this prompt

- *For phenomena heavy on chemistry:* every chemical bond is quantum mechanical. The Pauli exclusion principle (Chapter 30) is what gives atoms shells and chemistry structure.
- *For Claude Code:* if you have spectroscopic data, extract photon energies from observed wavelengths directly.

### Connection to previous chapters

Builds on Chapter 24 (EM spectrum), Chapter 27 (diffraction limit), and Chapter 28 (relativistic $E = pc$ for massless particles).

### Preview of next chapter

Chapter 30 applies quantum mechanics to atoms specifically — the Bohr model, hydrogen energy levels, quantum numbers, the Pauli exclusion principle, and the periodic table.

---

## What would change my mind

The chapter argues that quantum mechanics is the correct theory at small scales and that classical mechanics is its $h \to 0$ limit. The argument would need revision if a precision measurement found Planck's constant to vary, if an electron double-slit experiment produced no interference, or if the Heisenberg bound were violated. None of these has happened in a century of intense experimental scrutiny. The theory is exact, so far.

## Still puzzling

The deepest unresolved question: *what is the wavefunction physically?* Is it a real thing in the world, or a tool for computing probabilities? Copenhagen, many-worlds, hidden variables, QBism — all give different answers. No proposed experiment has distinguished them. The predictive success of quantum mechanics (the most precisely tested theory in the history of science) and conceptual clarity have come apart in a way that has no precedent in physics. The mathematics is not in doubt. What the mathematics means remains open.

---

## AI Wayback Machine

**Max Planck** introduced the quantum hypothesis in 1900 — proposing that energy comes in discrete packets to explain blackbody radiation. He spent decades afterward uncomfortable with what his idea had unleashed.

![Max Planck](../images/max-planck-6br.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who was Max Planck, and how does his quantum hypothesis connect to the quantum physics we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Max Planck"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how Planck's quantization assumption resolves the ultraviolet catastrophe.
- Ask it about Planck's quiet resistance to Nazi science policy during the war — and the personal tragedy that accompanied it.

What changes? What gets better? What gets worse?

---

## Connections forward

Chapter 30 (atomic physics) applies quantum mechanics to atoms: Bohr's model, the hydrogen energy levels, quantum numbers, the Pauli exclusion principle, and why the periodic table has the structure it does. Chapter 31 (nuclear physics) extends to nuclei: quantum tunneling for alpha decay, the strong force, binding energies, and $E = mc^2$ made concrete in mass defects. Chapter 33 (particle physics) extends further to the standard model. Every chapter that follows rests on the three facts — $E = hf$, $\lambda = h/p$, $\Delta x \, \Delta p \geq h/4\pi$ — installed here.

---

**Tags:** quantum-mechanics, photons, photoelectric-effect, de-Broglie, Heisenberg-uncertainty
