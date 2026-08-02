# Chapter 30 — Atomic Physics

*The periodic table is two rules. This chapter is where we get them.*

---

![Stylized alpha-particle scattering experiment. Alpha beam hits gold foil; most particles pass nearly straight through (atoms mostly empty), but rare large-angle deflections (and some backscatter) reveal a tiny, dense, positive...](../images/30-atomic-physics-fig-01.png)
*Figure 30.1 — Rutherford, 1909 — Most Alphas Pass; A Rare Few Bounce Back*

In 1909, Hans Geiger and Ernest Marsden were firing alpha particles at a thin gold foil in Rutherford's Manchester laboratory, expecting to confirm the prevailing picture of the atom — J. J. Thomson's "plum pudding," in which positive charge was spread diffusely through a soft cloud with electrons embedded like raisins. In that model, an alpha particle passing through the atom would encounter nothing hard enough to bounce it back. It should just keep going, perhaps deflected a little.

Mostly that's what they saw. But every so often — about one alpha in 8000 — one bounced back. Nearly the full way.

Rutherford said it was "as if you had fired a 15-inch shell at a piece of tissue paper, and it had come back and hit you."

His interpretation, published in 1911: the atom is almost entirely empty space. All the positive charge and nearly all the mass occupy a region about $10^{-15}$ m across — $10^5$ times smaller than the atom itself. Electrons fill the surrounding volume but contribute negligible mass. The atom is a solar system in miniature: a tiny dense nucleus, orbited by electrons in a vast surrounding emptiness.

<!-- → [FIGURE: Rutherford scattering diagram. Left: collimated beam of alpha particles heading toward a thin gold-foil target. Right: most alphas passing straight through or deflecting slightly (dense cluster of arrows continuing forward). A few arrows shown deflecting at large angles, including one arrow bent nearly 180°. Inset: nuclear atom cross-section showing tiny nucleus (labeled ~10⁻¹⁵ m) surrounded by electron cloud (labeled ~10⁻¹⁰ m). Caption: Rutherford's 1911 interpretation of the Geiger-Marsden results. The rare large-angle deflections could only be explained by a tiny, dense, positively charged nucleus. The atom is mostly empty space.] -->

This picture has one immediate, catastrophic problem. An orbiting electron is accelerating. Maxwell's equations say accelerating charges radiate. The electron should radiate away its kinetic energy and spiral into the nucleus in roughly $10^{-11}$ seconds. Atoms would be unstable. But they are not.

---

## Bohr's fix

Niels Bohr, a young Danish physicist working in Rutherford's lab, proposed a solution in 1913 that he freely admitted was a guess — but a precise, testable, numerically specific guess. He postulated two things:

First: electrons orbit only in certain allowed orbits and do not radiate while in those orbits. Second: radiation is emitted or absorbed only when an electron jumps between allowed orbits, releasing or absorbing a photon of energy $hf = |E_i - E_f|$.

The allowed orbits are those for which the electron's angular momentum is an integer multiple of $h/2\pi$:

$$L = m_e v r = n\frac{h}{2\pi}, \qquad n = 1, 2, 3, \ldots$$

Combine this with the Coulomb force providing centripetal acceleration, and the total energy comes out to:

$$E_n = -\frac{13.6 \text{ eV}}{n^2}.$$

The ground state ($n=1$) sits at $-13.6$ eV — the ionization energy of hydrogen. Level $n=2$ is at $-3.4$ eV. Level $n=3$ at $-1.51$ eV. The energies rise toward zero (free electron) as $n$ grows.

The orbital radii:

$$r_n = n^2 a_0, \qquad a_0 = 5.29 \times 10^{-11} \text{ m.}$$

![Three probability-density visualizations for hydrogen orbitals. 1s: spherical cloud densest near nucleus. 2p (px or py): dumbbell with node at origin. 3d (d_z²): cloverleaf with nodes. Color intensity proportional to |ψ|². The...](../images/30-atomic-physics-fig-04.png)
*Figure 30.4 — Hydrogen Atomic Orbitals — Probability Clouds, Not Planetary Orbits*

$a_0$ is the Bohr radius — the radius of the ground-state orbit, about half an ångström. This is the size of hydrogen, and agrees with what we know of atomic dimensions from chemistry.

### The Rydberg formula

When an electron drops from level $n_i$ to level $n_f < n_i$, it emits a photon of energy $E_i - E_f$. Using $E = hc/\lambda$:

$$\frac{1}{\lambda} = R\left(\frac{1}{n_f^2} - \frac{1}{n_i^2}\right), \qquad R = 1.097 \times 10^7 \text{ m}^{-1}.$$

This is the Rydberg formula, discovered empirically by Johann Balmer in 1885 for the visible hydrogen lines and by Johannes Rydberg in 1888 as the general pattern. They found the formula; Bohr derived it from Newton's laws plus one quantization condition and got the constant $R$ from fundamental physics:

$$R = \frac{m_e k^2 e^4}{4\pi h^3 c} = 1.097 \times 10^7 \text{ m}^{-1},$$

matching the experimental value to four significant figures. This was the triumph of the 1913 paper.

**The Balmer-α line** ($n_i = 3 \to n_f = 2$):

$$\frac{1}{\lambda} = (1.097\times10^7)\left(\frac{1}{4} - \frac{1}{9}\right) = (1.097\times10^7)(0.139) = 1.52\times10^6 \text{ m}^{-1},$$

$$\lambda = 656 \text{ nm.}$$

The red line of hydrogen. It's the characteristic red glow of every hydrogen discharge tube, every hydrogen plasma, every stellar corona. Astronomers see it in absorption in the Sun's spectrum (one of the original Fraunhofer lines, identified before Bohr, before Rydberg, before anyone understood what made it) and in emission from vast clouds of ionized hydrogen across the galaxy.

The **Lyman-α line** ($n_i = 2 \to n_f = 1$) gives $\lambda = 122$ nm, deep in the ultraviolet. The Paschen series ($n_f = 3$) is in the infrared.

<!-- → [FIGURE: Hydrogen energy level diagram. Horizontal lines at E_n = -13.6/n² eV for n=1 through n=6, plus E=0 (ionization limit). Energy values labeled on left. Vertical arrows showing transitions: Lyman series (all ending on n=1, labeled UV), Balmer series (all ending on n=2, labeled visible, with Balmer-α at 656 nm highlighted), Paschen series (ending on n=3, labeled IR). Caption: The hydrogen energy levels and the first three spectral series. Balmer-α (656 nm) is the bright red line seen in any hydrogen discharge. The series boundaries correspond to the ionization wavelengths for electrons starting in each level.] -->

### Why Bohr's orbits make physical sense

Bohr's quantization rule — $L = nh/(2\pi)$ — looked arbitrary in 1913. In 1924, de Broglie's matter-wave hypothesis gave it a physical interpretation. The electron has a de Broglie wavelength $\lambda = h/p = h/(m_e v)$. The quantization condition $m_e v r = nh/(2\pi)$ is equivalent to:

$$2\pi r = n\lambda.$$

![Three panels showing electron de Broglie waves around a nucleus. n=2: 2 wavelengths fit around the orbit (closed). n=3: 3 wavelengths (closed). Non-integer (n=2.5): wave doesn't close — destructive interference — orbit...](../images/30-atomic-physics-fig-03.png)
*Figure 30.3 — Standing-Wave Orbits — n·λ = 2π r, Only Some Orbits Are Stable*

An integer number of electron wavelengths must fit around the orbit's circumference. The allowed orbits are those where the electron's matter wave closes smoothly on itself — standing waves on a circle. Any orbit where the wave doesn't close interferes destructively with itself and is forbidden. The electron in a stable atom is a standing wave. Bohr's rules are the standing-wave conditions.

<!-- → [FIGURE: Two circular orbit diagrams side by side. Left (allowed): circle with n=3 standing wave drawn on it — sinusoidal wave fitting exactly 3 wavelengths around the circumference, closing on itself. Labeled "n=3, allowed: 3λ = 2πr." Right (forbidden): circle with a non-integer wave that doesn't close, showing destructive interference at the join point. Labeled "not allowed: wave doesn't close." Caption: Bohr's quantization condition has a physical interpretation as a standing-wave requirement. Allowed orbits are those in which an integer number of de Broglie wavelengths fit exactly around the circumference. Any other orbit's wave cancels itself.] -->

The limitation: for multi-electron atoms, this picture breaks down. Each electron perturbs the orbits of every other; the nice clean Bohr formula only works for one-electron systems (hydrogen, He+, Li2+, etc.). For everything else, you need the full Schrödinger equation. But the energy-level structure and the spectral series remain qualitatively correct.

---

## Four quantum numbers and the Pauli principle

Bohr's orbits described by a single integer $n$. Full quantum mechanics requires four quantum numbers to specify the state of each electron.

**Principal quantum number $n$**: sets the energy and approximate distance. Allowed values: $n = 1, 2, 3, \ldots$ For hydrogen, $E_n = -13.6\text{ eV}/n^2$.

**Angular momentum quantum number $\ell$**: sets the orbital shape (how the electron's probability cloud is distributed in space). Allowed values: $\ell = 0, 1, 2, \ldots, n-1$. The names: $\ell = 0$ (s, spherical), $\ell = 1$ (p, dumbbell-shaped), $\ell = 2$ (d, more complex), $\ell = 3$ (f).

**Magnetic quantum number $m_\ell$**: sets the orientation of the orbital angular momentum in space. Allowed values: $m_\ell = -\ell, -\ell+1, \ldots, 0, \ldots, +\ell$ — a total of $2\ell+1$ values. Each subshell has $2\ell+1$ distinct orbitals: one s orbital, three p orbitals, five d orbitals, seven f orbitals.

**Spin quantum number $m_s$**: the electron's intrinsic angular momentum, with no classical analogue. Allowed values: $m_s = +1/2$ or $-1/2$ only — "spin up" or "spin down."

### The Pauli exclusion principle

Wolfgang Pauli, in 1925, stated the rule that makes the periodic table work:

*No two electrons in an atom can simultaneously have the same four quantum numbers.*

Since each spatial orbital is specified by $(n, \ell, m_\ell)$, and spin adds one more binary label, each orbital can hold exactly two electrons — one with $m_s = +1/2$, one with $m_s = -1/2$. No more.

**Counting the shells.** In shell $n$, the allowed values of $\ell$ run from 0 to $n-1$. For each $\ell$, there are $2\ell+1$ values of $m_\ell$. The total number of spatial orbitals in shell $n$ is:

$$\sum_{\ell=0}^{n-1}(2\ell+1) = n^2.$$

With two electrons per orbital, shell $n$ holds $2n^2$ electrons: shell 1 holds 2, shell 2 holds 8, shell 3 holds 18, shell 4 holds 32.

![Periodic table colored by block (s, p, d, f), showing how each block corresponds to electrons filling specific quantum-number combinations (l=0,1,2,3). Pauli exclusion (2 per orbital) and Hund's rule explain the structure.](../images/30-atomic-physics-fig-06.png)
*Figure 30.6 — Periodic Table by Block — Quantum Numbers + Pauli Exclusion Build Chemistry*

These are the numbers of the periodic table. The magic-number shell closings (2, 8, 18, 32) — the noble gas configuration, the end of each period — are not a coincidence or an empirical regularity. They are $2n^2$, derived from the four quantum numbers and Pauli exclusion.

<!-- → [TABLE: Shell capacities from quantum numbers. Columns: n, allowed ℓ values, subshells (name + # orbitals), total spatial orbitals (n²), max electrons (2n²). Rows: n=1 (ℓ=0, 1s×1, 1, 2), n=2 (ℓ=0,1, 2s×1+2p×3=4, 4, 8), n=3 (ℓ=0,1,2, 3s×1+3p×3+3d×5=9, 9, 18), n=4 (ℓ=0,1,2,3, 4s×1+4p×3+4d×5+4f×7=16, 16, 32). Caption: Shell capacities follow from counting allowed quantum states and applying the Pauli exclusion principle. The 2, 8, 18, 32 electron limits — the magic numbers of the periodic table — are the result.] -->

### Building the periodic table

Electrons fill orbitals in order of increasing energy. The ordering:

$$1s < 2s < 2p < 3s < 3p < 4s < 3d < 4p < 5s < 4d < 5p < \ldots$$

(The 4s orbital falls below the 3d because of how multi-electron shielding shifts energies — this is why the transition metals start where they do.)

Reading the periodic table through this lens: each row corresponds roughly to a new principal shell being filled. Each block corresponds to a subshell type. The s-block (groups 1–2) fills $\ell = 0$ subshells. The p-block (groups 13–18) fills $\ell = 1$. The d-block (transition metals) fills $\ell = 2$. The f-block (lanthanides, actinides) fills $\ell = 3$. Hydrogen (1s¹) and helium (1s²) complete the first period. Lithium through neon complete the second (2s and 2p). Sodium through argon complete the third (3s and 3p). Potassium and calcium fill 4s; then scandium through zinc fill 3d; then gallium through krypton fill 4p.

**Carbon** (Z = 6): $1s^2\,2s^2\,2p^2$. The two 2p electrons go into separate 2p orbitals with parallel spins (Hund's rule — electrons in a partially filled subshell prefer to maximize unpaired spins, reducing their mutual repulsion). Carbon's outermost shell has four electrons — two in 2s, two in 2p — and can form four bonds. The entirety of organic chemistry follows.

**Oxygen** (Z = 8): $1s^2\,2s^2\,2p^4$. Six outer electrons. Two of the 2p electrons are paired; two are unpaired. Two available bonding sites — explaining why water is H₂O, not H₃O or H₁O.

**Neon** (Z = 10): $1s^2\,2s^2\,2p^6$. All orbitals in the first two shells are full. No available orbitals at the same energy as its outer electrons to bond with. Neon is chemically inert. So are helium, argon, krypton, xenon — every noble gas has a completely filled outer subshell. The Pauli principle, filling orbitals in order, gives chemical inertness for free.

**Sodium** (Z = 11): $1s^2\,2s^2\,2p^6\,3s^1$. One lonely 3s electron above the neon core. It's far from the nucleus and weakly bound. It wants to pair. Sodium is reactive. Every alkali metal — lithium, sodium, potassium, rubidium, cesium — has one s electron above a noble-gas core, and every one is reactive for exactly this reason.

The entire periodic table, every chemical property, follows from the same four quantum numbers and one exclusion rule.

<!-- → [FIGURE: Periodic table block diagram. Full periodic table shown with color coding: s-block (groups 1-2 + He) shaded one color, p-block (groups 13-18 except He) second color, d-block (transition metals, groups 3-12) third color, f-block (lanthanides/actinides) fourth color. Labels: "filling ℓ=0 (s)", "filling ℓ=1 (p)", "filling ℓ=2 (d)", "filling ℓ=3 (f)". Row numbers 1-7 labeled as n=1 through n=7. Caption: The periodic table organized by which subshell is being filled. Rows correspond to the principal quantum number n; blocks to the angular momentum quantum number ℓ. The 18-element fourth period includes the 10 d-block elements because 3d fills between 4s and 4p.] -->

---

## Characteristic X-rays and Moseley's law

In 1913 and 1914, Henry Moseley, age twenty-six, was at Oxford systematically firing high-energy electrons at metal targets and measuring the X-rays emitted. He found a clean pattern: the square root of the characteristic X-ray frequency is proportional to $Z-1$, where $Z$ is the atomic number. This is **Moseley's law**.

The physical mechanism: when a high-energy electron knocks out an inner-shell (1s) electron from a target atom, the vacancy is filled by an electron falling from a higher shell. The energy difference between the two shells is released as a photon — an X-ray — whose energy is characteristic of the element because inner-shell energies depend strongly on $Z$.

For the $K_\alpha$ line ($n = 2 \to n = 1$ transition), the energy is approximately:

$$E_{K_\alpha} \approx 13.6 \text{ eV} \times Z_{\text{eff}}^2 \times \left(\frac{1}{1^2} - \frac{1}{2^2}\right) = 13.6 \times (Z-1)^2 \times 0.75 \text{ eV},$$

where $Z_{\text{eff}} \approx Z - 1$ (the second 1s electron screens the nuclear charge by about one unit). The $\sqrt{f} \propto (Z-1)$ dependence Moseley observed follows immediately.

<!-- → [FIGURE: Moseley plot. Horizontal axis: Z (atomic number), 10 to 50. Vertical axis: √f (square root of characteristic X-ray frequency, arbitrary units). Data points for ~15 elements falling on a straight line. Line labeled √f = const × (Z-1). Elements labeled at their positions (e.g., Ca at Z=20, Mn at Z=25, Cu at Z=29). Caption: Moseley's law: the square root of the K_α X-ray frequency is linear in Z-1. Each element has a unique frequency fingerprint. Moseley used this to determine atomic numbers from X-ray spectra and to find gaps — undiscovered elements — in the periodic table.] -->

Moseley used this to reorder the periodic table by atomic number rather than atomic mass, correcting several inconsistencies (cobalt and nickel had been swapped because cobalt has the larger mass but smaller Z). He also found gaps — atomic numbers with no known element — and predicted where new elements should appear. His method, X-ray fluorescence spectroscopy, remains a routine analytical tool today for identifying elements in materials: forensics, archaeology, environmental monitoring, quality control in manufacturing.

Alongside the characteristic X-rays, the same high-energy electrons produce **bremsstrahlung** — a continuous spectrum of X-rays from electrons decelerating in the nuclear electric field. The maximum photon energy corresponds to an electron losing all its kinetic energy in a single emission:

$$E_{\max} = qV = hf_{\max},$$

where $V$ is the accelerating voltage. A 100 kV tube produces bremsstrahlung up to 100 keV, corresponding to a minimum wavelength of about 12.4 pm.

**Worked example — tungsten $K_\alpha$.** For tungsten ($Z = 74$):

$$E_{K_\alpha} \approx 13.6 \times (73)^2 \times 0.75 \approx 5.4 \times 10^4 \text{ eV} = 54 \text{ keV.}$$

The measured value is 59 keV — order-of-magnitude agreement, with the error coming from the crude screening approximation. This X-ray penetrates several centimeters of tissue: standard diagnostic chest X-ray energy.

<!-- → [FIGURE: X-ray tube spectrum diagram. Horizontal axis: photon energy (keV), 0 to 120. Vertical axis: intensity. Two components shown: smooth bremsstrahlung curve rising from zero to a maximum then falling to zero at E_max = qV = 100 keV (labeled "continuous bremsstrahlung"). Superimposed: two sharp vertical spikes at the K_α and K_β characteristic lines of the anode material (labeled "characteristic X-rays"). Caption: X-ray spectrum from a 100-kV tube with a tungsten anode. Bremsstrahlung is a continuous spectrum with a sharp high-energy cutoff at E = qV. Characteristic lines appear at element-specific energies set by inner-shell transitions. Both components are present simultaneously.] -->

---

## The chapter in one view

![Plot of total energy E_total = KE + PE for hydrogen as a function of orbit radius r. KE grows as 1/r² (Heisenberg: confine → momentum spreads → KE rises). PE = -ke²/r is attractive. Sum has a minimum at the Bohr radius a₀ ≈ 53 pm.](../images/30-atomic-physics-fig-05.png)
*Figure 30.5 — Uncertainty Stabilizes the Atom — Localizing the Electron Costs Kinetic Energy*

Start with Rutherford: the atom is empty space with a tiny dense nucleus. Add Bohr: the allowed electron orbits are those where the electron is a standing wave — integer numbers of de Broglie wavelengths around the orbit — and transitions between orbits produce the hydrogen spectrum exactly. Add Pauli: no two electrons share the same quantum state. Add four quantum numbers to label those states. The result is the entire periodic table, as a matter of counting.

![Energy-level diagram for hydrogen. E_n = -13.6 eV/n² gives levels at n=1 (−13.6), n=2 (−3.4), n=3 (−1.51), n=4 (−0.85), n=5 (−0.54), and continuum at 0. Transitions to n=2 (Balmer): Hα (656 nm), Hβ (486 nm), Hγ (434 nm), Hδ...](../images/30-atomic-physics-fig-02.png)
*Figure 30.2 — Bohr Energy Ladder — n=1 to ∞ for Hydrogen, Balmer Lines to n=2 Are Visible*

The deep fact is the unity of these ideas. The Rydberg formula — empirically discovered in 1885 — is a consequence of Bohr's quantization. The periodic table's magic numbers — 2, 8, 18, 32 — are the consequence of Pauli exclusion applied to states counted by four quantum numbers. Moseley's characteristic X-rays are inner-shell transitions governed by the same energy-level formula, scaled to $Z^2$ instead of 1. The red 656-nm line in a hydrogen discharge tube, the chemical inertness of argon, and the penetrating X-rays in a hospital radiology suite are all the same physics at different $Z$ and different $n$.

Feynman's favorite way to put it: if you were told that all of chemistry, all of materials, all of biology, came from one equation and two postulates, you would call it extraordinary. And then you would be told that's exactly what happened. The equation is Schrödinger's (the quantization follows automatically). The postulates are: particles have wavefunctions, and fermions obey Pauli exclusion. The rest — every element, every bond, every protein, every cell — is computation from these.

---

## Exercises

### Warm-up

**30.1** *(LO 1)* In Rutherford's gold-foil experiment, what experimental observation ruled out Thomson's plum-pudding model? What did the large-angle scattering establish about atomic structure?

**30.2** *(LO 2)* Compute the wavelength of the Balmer-β line of hydrogen ($n_i = 4$, $n_f = 2$).

**30.3** *(LO 3)* List the four quantum numbers, their allowed values for $n = 3$, and the physical property each describes.

**30.4** *(LO 3)* Maximum electrons in (a) the $n = 1$ shell, (b) the $n = 3$ shell, (c) the 3p subshell?

### Application

**30.5** *(LO 2)* The ionization energy of hydrogen is 13.6 eV. (a) Photon wavelength that just barely ionizes ground-state hydrogen. (b) Which spectral region?

**30.6** *(LO 4)* Ground-state electron configurations for (a) nitrogen (Z = 7), (b) silicon (Z = 14), (c) iron (Z = 26).

**30.7** *(LO 4)* Why are the noble gases chemically inert? Explain in terms of electron configuration.

**30.8** *(LO 5)* X-ray tube at 80 kV. (a) Maximum photon energy. (b) Corresponding minimum wavelength.

### Synthesis

**30.9** *(LO 2, LO 5)* The Sun's spectrum shows absorption at Balmer-α (656 nm), Balmer-β (486 nm), and Balmer-γ (434 nm). (a) Verify these wavelengths with the Rydberg formula. (b) What does the presence of Balmer absorption in the Sun's spectrum tell us?

**30.10** *(LO 3, LO 4)* Use the Pauli exclusion principle to explain why the second and third periods each contain 8 elements but the fourth contains 18.

**30.11** *(LO 5)* A sample emits characteristic X-rays at $E_{K_\alpha} \approx 8.0\text{ keV}$. Use $E_{K_\alpha} \approx 13.6\,(Z-1)^2 \times 0.75\text{ eV}$ to estimate $Z$. What element?

### Challenge

**30.12** *(beyond chapter)* Show that the combination $h^2/(m_e k e^2)$ has units of length. Estimate the order of magnitude, then compute $a_0 = h^2/(4\pi^2 m_e k e^2)$ explicitly.

**30.13** *(beyond chapter)* The Pauli exclusion principle applies to all fermions, including protons and neutrons in nuclei. (a) How many neutrons can occupy the ground-state shell of a nucleus, accounting for spin? (b) How does this lead to nuclear "magic numbers," analogous to noble gases in atomic physics?

---

## LLM Exercise — Chapter 30: Atomic Physics in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A Logbook entry connecting atomic physics — spectral lines, X-rays, electron configurations — to your anchor phenomenon.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste your 1-sentence description].

For Chapter 30, I want to apply atomic physics — Bohr's model, quantum numbers, the periodic table, characteristic spectra — to my phenomenon.

Please:

1. Identify ONE atomic-physics aspect of my phenomenon. Examples: for a bike commute — sodium street lamps emitting at 589 nm, LED traffic signals (semiconductor band gaps which derive from atomic structure), the iron in my bike's steel (3d subshell, ferromagnetic). For a coffee maker — spectroscopic identification of caffeine (C, H, N, O atoms), the sodium D-line in the dye of any colored cup, mineral content of water (calcium, sodium, etc.). For a basketball shot — the elements in human muscle (carbon-based chemistry), gym lighting (mercury vapor in fluorescent bulbs at 254 nm; LEDs based on band-gap engineering). For a marathon — caffeine in pre-race coffee, sodium and potassium in electrolyte drinks.

2. Apply ONE atomic-physics calculation. Compute a transition wavelength using the Rydberg formula, predict a spectral line, estimate ionization energy of a key element, identify the electron configuration of a specific atom.

3. Specify input numbers and uncertainty.

4. Run the calculation. Report value with units.

5. One sanity check: does the wavelength match a known spectral line of the right element?

6. One sentence connecting this to Chapter 31 (radioactivity) — moving from atomic to nuclear physics.

Save the output as logbook/chapter-30-atomic.md.
```

### What this produces

A Logbook entry connecting your phenomenon to specific atomic structure or spectroscopy.

### How to adapt this prompt

- *For a phenomenon involving any color:* Color is atomic physics. Identify the atom or molecule responsible.
- *For ChatGPT/Gemini:* Identical with interface substitutions.
- *For Claude Code:* If you have access to a smartphone spectroscope or a recorded spectrum, extract the dominant emission lines and identify them by element.

### Connection to previous chapters

Builds directly on Chapter 29 (photons, de Broglie, uncertainty). Uses Chapter 27 (interference for X-ray diffraction) and Chapter 24 ($c = f\lambda$).

### Preview of next chapter

Chapter 31 moves from electrons to nuclei — protons and neutrons bound by the strong force, with their own quantization, shell structure, and characteristic radiation at MeV rather than eV scales.

---

**Tags:** atomic-physics, Bohr-model, periodic-table, Pauli-exclusion, quantum-numbers
