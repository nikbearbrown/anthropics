# Chapter 8 — Statistical Mechanics

*The bridge between microscopic mechanics and macroscopic thermodynamics. The Boltzmann distribution, the partition function, and the path to quantum statistics.*

---

## The Question Thermodynamics Refuses to Answer

Thermodynamics is a remarkably successful science. It tells you that entropy increases, that no engine beats Carnot, that heat flows from hot to cold. It tells you all this without ever asking what a molecule is, or whether matter is made of atoms at all. Clausius and Carnot did their best work before atomic theory was on firm ground. The laws they found are so general they don't need atoms.

But that generality is also a limitation. Thermodynamics tells you that the entropy of a gas increases when it expands into a vacuum. It doesn't tell you *why*. It tells you that a hot object cools when placed next to a cold one. It doesn't tell you the mechanism. It gives you the ledger without the bookkeeper.

Statistical mechanics is the bookkeeper. It starts from atoms — from the actual mechanics of actual particles — and derives thermodynamics from the bottom up. The temperature you measure with a thermometer is the average kinetic energy of the molecules. The entropy that always increases is the logarithm of the number of ways the molecules can be arranged. The laws of thermodynamics aren't axioms handed down from nowhere; they're consequences of mechanics applied to very large numbers of particles.

The key idea, the one that unlocks everything, is almost embarrassingly simple: in equilibrium, all microscopic configurations with the same energy are equally probable.

That's it. That's the postulate. Everything else follows by counting.

---

## Microstates, Macrostates, and the Fundamental Postulate

Let me be precise about what "configurations" means.

A **microstate** is the complete specification of a system at the molecular level — every particle's position and momentum, every spin's orientation, every quantum state's occupation number. For a gas of $N$ molecules, a microstate specifies all $6N$ position and momentum coordinates simultaneously. The number of microstates is astronomical.

A **macrostate** is the coarse-grained description we actually measure — temperature, pressure, volume, total energy. Many microstates correspond to one macrostate. A gas in a box at 300 K and 1 atm is consistent with an unimaginable number of arrangements of its molecules; we can't tell which one the gas is actually in, and we don't need to.

The **fundamental postulate** of statistical mechanics: in thermal equilibrium, all microstates consistent with the macroscopic constraints (fixed total energy, fixed particle number, fixed volume) are equally probable.

This is not obvious. It's a postulate, justified by its consequences. And its consequences are extraordinary.

If all accessible microstates are equally likely, then the most probable macrostate is simply the one with the most microstates. The equilibrium state — the state the system naturally reaches and stays in — is the most probable macrostate. Entropy, $S = k_B \ln \Omega$ where $\Omega$ is the number of microstates, is just the logarithm of this count. Maximizing entropy means finding the most probable macrostate.

The second law of thermodynamics — entropy increases in any spontaneous process — now has a mechanical explanation. The gas that expands to fill its container isn't obeying some mystical law about disorder. It's moving toward the configuration with more microstates, because that's overwhelmingly the most probable thing to happen. The probability of a gas spontaneously concentrating into half its container isn't zero — it's just so small for macroscopic quantities of gas that it has never been observed and never will be.

<!-- → [DIAGRAM: Two columns — left labeled "Macrostate: Gas fills box", right labeled "Macrostate: Gas in half the box"; under each column, a set of dots representing microstates (many dots on the left, very few on the right); an arrow labeled "Ω left >> Ω right" pointing from right to left; caption: "Equilibrium is not a special state — it's simply the macrostate with the most microscopic arrangements. The second law is probability, not magic."] -->

---

## The Boltzmann Distribution

Now consider a small system in contact with a large thermal reservoir at temperature $T$. The system can exchange energy with the reservoir, but the reservoir is so large that its temperature doesn't change when the system's energy fluctuates. What's the probability of finding the system in a particular microstate $i$ with energy $E_i$?

The answer is the Boltzmann distribution:

$$P_i = \frac{e^{-E_i / k_B T}}{Z}$$

where $Z$ is the **partition function**, defined as the sum over all microstates:

$$Z = \sum_i e^{-E_i / k_B T}.$$

The derivation is short. From the fundamental postulate applied to the combined system-plus-reservoir: the probability of finding the system in state $i$ is proportional to the number of microstates available to the reservoir when the system has energy $E_i$. That's $\Omega_{\text{res}}(E_{\text{total}} - E_i)$. Taking the logarithm and expanding around $E_{\text{total}}$, we identify the reservoir temperature as $1/k_B T = \partial \ln \Omega_{\text{res}} / \partial E$. The result is the Boltzmann exponential.

The factor $Z$ in the denominator is just normalization — the probabilities must sum to one. But $Z$ turns out to be far more than a normalization constant. It's the master object of statistical mechanics.

Notice what the Boltzmann distribution says. Lower-energy states are more probable by a factor of $e^{-\Delta E / k_B T}$. At low temperature ($k_B T \ll \Delta E$ for typical energy gaps), the exponential suppression is severe and nearly everything is in the ground state. At high temperature ($k_B T \gg \Delta E$), the exponentials become nearly equal and all states are roughly equally occupied. Temperature controls the width of the distribution over energy states.

<!-- → [DIAGRAM: Three side-by-side energy-level diagrams for the same set of 5 equally-spaced levels, labeled low T, medium T, high T; occupation probability shown as horizontal bar width at each level; at low T, the bottom level is nearly fully occupied and upper levels are nearly empty; at high T, bars are nearly equal; at medium T, intermediate distribution; caption: "Temperature controls how far up the energy ladder the Boltzmann distribution reaches. k_BT is the characteristic energy scale."] -->

---

## The Partition Function: Master Object

Once you have $Z$ as a function of temperature, you have complete thermodynamic information about the system. Everything follows by differentiation.

Let $\beta = 1/k_B T$. Then:

**Average energy:**
$$\langle E \rangle = -\frac{\partial \ln Z}{\partial \beta}$$

This follows directly from differentiating $\ln Z = \ln \sum_i e^{-\beta E_i}$ with respect to $\beta$.

**Helmholtz free energy:**
$$F = -k_B T \ln Z$$

**Entropy:**
$$S = -\frac{\partial F}{\partial T} = k_B \left( \ln Z + \beta \langle E \rangle \right)$$

**Heat capacity:**
$$C_V = \frac{\partial \langle E \rangle}{\partial T} = \frac{\langle E^2 \rangle - \langle E \rangle^2}{k_B T^2}$$

That last relation deserves a pause. The heat capacity — a macroscopic response function, how much energy you need to add to raise the temperature by one degree — equals the variance of the energy fluctuations in the equilibrium ensemble, divided by $k_B T^2$. Response equals fluctuation. This is the fluctuation-dissipation theorem, and it's one of the deep connecting threads in statistical physics.

The partition function is the statistical mechanics analogue of the action in classical mechanics or the wave function in quantum mechanics — the object you compute first, from which everything else follows.

---

## The Two-Level System and the Schottky Anomaly

Let's work out the simplest possible example: a system with exactly two energy levels, $E_0 = 0$ and $E_1 = \varepsilon > 0$.

The partition function:
$$Z = e^{-\beta \cdot 0} + e^{-\beta \varepsilon} = 1 + e^{-\beta \varepsilon}.$$

Occupation probabilities:
$$P_0 = \frac{1}{1 + e^{-\beta \varepsilon}}, \qquad P_1 = \frac{e^{-\beta \varepsilon}}{1 + e^{-\beta \varepsilon}}.$$

Average energy:
$$\langle E \rangle = 0 \cdot P_0 + \varepsilon \cdot P_1 = \frac{\varepsilon}{e^{\beta \varepsilon} + 1}.$$

At low temperature ($\beta \varepsilon \gg 1$): $P_1 \approx e^{-\beta \varepsilon} \to 0$. Nearly everything in the ground state.

At high temperature ($\beta \varepsilon \ll 1$): $P_1 \approx 1/2$. Both states equally occupied.

Now take the derivative to get the heat capacity per atom, $C_V = d\langle E \rangle / dT$. The result has a shape worth describing carefully. At very low $T$, the heat capacity is nearly zero — the upper level is essentially inaccessible, and small temperature changes don't change the populations. At very high $T$, the heat capacity is also nearly zero — both states are already equally occupied, and small temperature changes barely shift the populations. In between, at $k_B T \sim \varepsilon / 2.4$, the heat capacity peaks. This is the **Schottky anomaly**.

The physics is transparent once you see it. Heat capacity measures how much energy a system absorbs per degree of temperature change. The system absorbs energy by promoting atoms from the lower level to the upper level. This promotion is most efficient when the populations are changing most rapidly with temperature — which happens at intermediate temperature, where neither level is fully occupied nor fully empty. Below that temperature, you can't get atoms into the upper level. Above it, both levels are already full. The peak occurs where the action is.

The Schottky anomaly is observed in real materials — spin systems in magnetic fields, defect states in crystals, certain molecular energy levels. It confirms the two-level statistical mechanics picture with quantitative precision.

<!-- → [CHART: Two panels — left: P_1 (occupation of upper level) vs. k_BT/ε, showing S-curve from 0 to 0.5; right: C_V vs. k_BT/ε, showing the Schottky peak at k_BT ≈ 0.4ε with C_V → 0 on both sides; annotate the peak location; caption: "Left: populations equilibrate as temperature rises. Right: heat capacity peaks exactly where population is changing fastest — the Schottky anomaly. Both curves are exact results from Z = 1 + e^{-βε}."] -->

---

## The Ideal Gas: Recovering Equipartition

The partition function machinery reproduces the classical ideal gas as a limiting case. This is a good sanity check, and the calculation shows where the $3/2$ in $\langle E \rangle = \frac{3}{2} k_B T$ actually comes from.

For a single particle in three dimensions with energy $E = p^2 / 2m$, the quantum states are so closely spaced at ordinary temperatures that we can treat momentum as continuous. The single-particle partition function is:

$$Z_1 = \frac{V}{h^3} \int d^3p \, e^{-p^2 / (2mk_BT)}.$$

The integral is a product of three identical Gaussians, one for each momentum component:

$$Z_1 = \frac{V}{h^3} \left( \int_{-\infty}^{\infty} e^{-p_x^2 / (2mk_BT)} \, dp_x \right)^3 = \frac{V}{h^3} (2\pi m k_B T)^{3/2}.$$

Now compute $\langle E \rangle = -\partial \ln Z_1 / \partial \beta$. Since $\ln Z_1 = \text{const} - \frac{3}{2} \ln \beta$:

$$\langle E \rangle = -\frac{\partial}{\partial \beta} \left( -\frac{3}{2} \ln \beta \right) = \frac{3}{2\beta} = \frac{3}{2} k_B T.$$

Each of the three translational degrees of freedom contributes $\frac{1}{2} k_B T$ — the equipartition theorem, derived from the partition function rather than postulated.

For $N$ particles, $\langle E \rangle = \frac{3}{2} N k_B T$, and $C_V = \frac{3}{2} N k_B$. These are the results you used in kinetic theory and thermodynamics. They fall out automatically from the partition function, applied to the correct energy spectrum.

The $1/h^3$ factor is the quantum-mechanical phase-space cell size — the smallest distinguishable region of position-momentum space. Even in the "classical" limit, Planck's constant appears. Statistical mechanics knows about quantum mechanics even when we pretend it doesn't.

---

## Quantum Statistics: When Boltzmann Fails

The Boltzmann distribution works beautifully for dilute classical gases, but it fails for two important classes of particles: fermions and bosons.

The distinction comes from quantum mechanics. Particles of the same type are fundamentally indistinguishable — there is no label you can put on electron number 47 to distinguish it from electron number 831. This indistinguishability has dramatic statistical consequences depending on the particle's spin.

**Fermions** — particles with half-integer spin (electrons, protons, neutrons) — obey the **Pauli exclusion principle**: at most one fermion can occupy any single quantum state. This single rule changes everything for dense systems of electrons.

The distribution function for fermions is the **Fermi-Dirac distribution**:

$$f_{\text{FD}}(E) = \frac{1}{e^{(E - \mu)/k_BT} + 1},$$

where $\mu$ is the chemical potential, the energy cost of adding one more particle to the system. At zero temperature, this distribution is a step function: all states below $\mu$ are fully occupied ($f = 1$), all states above are empty ($f = 0$). The chemical potential at zero temperature is called the **Fermi energy** $E_F$.

The key thing to understand about the Fermi-Dirac distribution is how different it is from Boltzmann at low temperatures. Boltzmann says: distribute particles so that lower-energy states are exponentially more probable. Fermi-Dirac says: fill states from the bottom up, one particle per state, until you run out of particles. The top of the filled stack is the Fermi energy. At room temperature, the thermal smearing of the step function extends over only a few $k_B T$ around $E_F$ — for electrons in a metal with $E_F \sim 5$ eV and $k_B T \sim 0.025$ eV at room temperature, only about 1% of electrons are thermally excited. The vast majority are locked into states they can't leave because everything below them is already full.

This is why metals have such small electronic heat capacities. The equipartition theorem would predict $\frac{3}{2} N k_B$ for the electronic contribution, which would be enormous. The actual electronic heat capacity in metals is proportional to $T$ and is about a hundredth of the equipartition value at room temperature. The Pauli exclusion principle freezes out nearly all the electrons.

<!-- → [DIAGRAM: Fermi-Dirac step function — f_FD(E) vs E, shown at T=0 (perfect step at E_F), T small (softened step, smeared over ~k_BT around E_F), and T large (broader smearing); shade the region where f differs from the T=0 step; caption: "At room temperature in a metal, only electrons within ~k_BT of the Fermi energy can be thermally excited. For copper, E_F ≈ 7 eV and k_BT ≈ 0.025 eV — less than 1% of electrons are available to absorb heat."] -->

**Bosons** — particles with integer spin (photons, helium-4 atoms) — have no exclusion principle. Any number of bosons can crowd into the same quantum state. Their distribution function is the **Bose-Einstein distribution**:

$$f_{\text{BE}}(E) = \frac{1}{e^{(E-\mu)/k_BT} - 1}.$$

The minus sign in the denominator (versus plus in Fermi-Dirac) means boson occupation numbers can become large without limit. For photons, $\mu = 0$ always (photons can be created and destroyed freely), and the Bose-Einstein distribution becomes Planck's formula for blackbody radiation:

$$\langle n \rangle = \frac{1}{e^{\hbar\omega/k_BT} - 1}.$$

This is the distribution Planck introduced in 1900 to fix the ultraviolet catastrophe — the prediction by classical physics that a blackbody would radiate infinite energy at short wavelengths. Planck's formula fits the measured spectrum perfectly. Deriving it from the Bose-Einstein distribution shows why: photons are bosons, and bosons crowd into low-energy states at low temperature rather than spreading out classically.

At sufficiently low temperatures and high densities, bosons undergo **Bose-Einstein condensation**: a macroscopic fraction of the particles pile into the single lowest-energy quantum state. For helium-4, this happens below 2.2 K and produces superfluidity — flow with zero viscosity. For cold atoms in traps, Bose-Einstein condensation was first achieved in 1995 by Cornell, Wieman, and Ketterle, who received the 2001 Nobel Prize.

---

## When Do Quantum Statistics Matter?

The Boltzmann distribution is the high-temperature, low-density limit of both quantum statistics. Quantum effects become important when the thermal de Broglie wavelength,

$$\lambda_{\text{dB}} = \frac{h}{\sqrt{2\pi m k_B T}},$$

becomes comparable to or larger than the average interparticle spacing $n^{-1/3}$, where $n$ is the number density.

For atoms in a gas at room temperature: $\lambda_{\text{dB}} \sim 0.1$ Å, interparticle spacing $\sim 30$ Å. Boltzmann is fine.

For electrons in a metal at room temperature: $\lambda_{\text{dB}} \sim 5$ Å, interparticle spacing $\sim 2$ Å. Quantum statistics are essential.

For helium-4 atoms near 2 K: $\lambda_{\text{dB}} \sim$ interparticle spacing. Bose-Einstein condensation.

The criterion isn't the absolute temperature — it's the ratio of the de Broglie wavelength to the particle spacing. Electrons in metals require Fermi-Dirac statistics at room temperature because they're dense and light. Helium requires Bose-Einstein statistics at 2 K because it's light and cold. The physics is the same in both cases: quantum indistinguishability, applied to particles closely enough spaced that their wave functions overlap.

<!-- → [TABLE: Three-column comparison — rows: "Atoms in air at 300 K", "Electrons in copper at 300 K", "He-4 at 2 K"; columns: λ_dB (Å), interparticle spacing (Å), λ_dB / spacing, statistics needed; values filled in from text; last column: Boltzmann, Fermi-Dirac, Bose-Einstein; caption: "The quantum/classical boundary is λ_dB ~ n^{-1/3}. Electrons in metals cross it at room temperature; gas atoms don't cross it until millikelvin temperatures."] -->

---

## What the Connection Actually Achieves

Step back and look at what statistical mechanics accomplishes.

Thermodynamics gave us laws without mechanisms. It told us entropy increases, engines have limits, heat flows one way. It was correct and powerful, but silent about why.

Statistical mechanics gives us mechanisms. Temperature is mean kinetic energy. Entropy is the logarithm of microstate count. The second law is probability — disordered states are more numerous, so systems drift toward them. The Carnot limit falls out of the entropy bookkeeping, now derived rather than postulated. Equipartition is a theorem, not an assumption. The heat capacities of real materials — with their quantum anomalies and low-temperature freeze-outs — are predictions that can be computed and tested.

The partition function is the instrument that makes this work. Specify the energy spectrum of your system, compute $Z(T)$, differentiate. Out come $\langle E \rangle$, $F$, $S$, $C_V$ — every thermodynamic property of the system, derived from first principles.

This is Feynman's favorite kind of physics: a single simple idea (count microstates; all equal-energy microstates are equally likely) that, pursued with mathematics, reproduces and explains an entire prior science.

---

## Common Misconceptions

*"The Boltzmann distribution says only low-energy states are occupied."* It says lower-energy states are occupied with higher probability — specifically, a factor of $e^{-\Delta E / k_B T}$ higher. At finite temperature, every state has nonzero probability. High-energy states are exponentially suppressed, not forbidden.

*"Statistical mechanics is an approximation."* For systems with many particles ($N \to \infty$), statistical mechanics gives exact thermodynamic results. Fluctuations scale as $1/\sqrt{N}$, negligible for thermodynamic-scale systems. Statistical mechanics doesn't approximate thermodynamics — it derives it.

*"Quantum statistics only matter at very low temperatures."* They matter when $\lambda_{\text{dB}} \gtrsim n^{-1/3}$ — when particle wave functions overlap. For electrons in metals, this condition holds at room temperature. For atoms in a gas, it doesn't. The relevant temperature scale is set by the density, not by any absolute number.

*"$\mu$ in Fermi-Dirac is a kind of energy."* The chemical potential $\mu$ is the free energy cost of adding one more particle: $\mu = \partial F / \partial N$. At zero temperature it equals the Fermi energy. For photons it's zero because photons aren't conserved. It controls the total particle number, not the temperature.

---

## What Would Change My Mind

The Boltzmann distribution and partition function framework have been tested in every thermal system accessible to measurement for over a century. Quantum statistics — Fermi-Dirac for metals and semiconductors, Bose-Einstein for photons and cold atoms — are confirmed at quantitative precision. A reproducible deviation from the Boltzmann distribution in a genuine equilibrium system would be the most dramatic result in physics since 1905. None has appeared.

The genuinely open frontier is non-equilibrium statistical mechanics — systems driven far from equilibrium, small systems where fluctuations are large, and biological systems that maintain order by continuously consuming energy. Fluctuation theorems (Jarzynski, Crooks) are recent exact results that extend equilibrium statistical mechanics to specific non-equilibrium contexts. This is active research, not settled physics.

---

## Still Puzzling

*Why does $S = k_B \ln \Omega$?* Boltzmann derived it; thermodynamics is consistent with it. But the factor $k_B$ is a conversion between natural units of entropy (dimensionless logarithm of microstate count) and SI units of joules per kelvin. That conversion requires choosing to measure temperature in kelvin rather than in energy units directly. There's nothing sacred about the choice — information theorists work with entropy in bits, setting $k_B = 1$. The physics is the same.

*The ergodic hypothesis.* The fundamental postulate says all microstates are equally probable in equilibrium. This requires the system to actually visit all its microstates over time — the ergodic hypothesis. Most systems are ergodic for practical purposes. Glasses are not: they get stuck in metastable configurations and never reach true equilibrium on observable timescales. Gravitational systems are not: they don't sample uniformly due to the long-range nature of gravity. Ergodicity breaking is an active research area in condensed matter physics.

*Quantum entropy.* For quantum systems, the correct entropy is the von Neumann entropy, $S = -k_B \text{Tr}(\rho \ln \rho)$, where $\rho$ is the density matrix. For systems in pure quantum states, this entropy is zero even when the Boltzmann entropy is large — which raises deep questions about the relationship between quantum information and thermodynamic entropy. This connects to black hole thermodynamics and the information paradox. Chapter 10 gestures toward it.

---

## Exercises

**Warm-up 1** *(Apply — two-level occupation)*. A two-level system has $E_0 = 0$ and $E_1 = 0.02$ eV. Find the occupation probabilities $P_0$ and $P_1$ at $T = 100$ K, $T = 300$ K, and $T = 1000$ K. At which temperature are the two levels closest to equally occupied?

**Warm-up 2** *(Apply — partition function)*. A system has three non-degenerate energy levels: $E_0 = 0$, $E_1 = k_B \cdot (200 \text{ K})$, $E_2 = k_B \cdot (400 \text{ K})$. Compute $Z$ at $T = 200$ K. Find the probability of each level. Find $\langle E \rangle$.

**Warm-up 3** *(Apply — Boltzmann and entropy)*. Using $F = -k_BT \ln Z$ and $S = -\partial F / \partial T$, compute the entropy of the two-level system from Warm-up 1 at $T = 300$ K. Check that your answer is between 0 (one state certain) and $k_B \ln 2$ (two states equally probable). Which limit does it approach, and why?

**Application 1** *(Apply — Schottky peak location)*. A paramagnetic salt has spin-up and spin-down states split by $\varepsilon = k_B \cdot (500 \text{ K})$ in an applied magnetic field. (a) At what temperature does the Schottky heat capacity peak? (b) Write the expression for $C_V(T)$ per atom as a function of $\varepsilon$ and $T$. (c) Sketch the expected shape without computing every value.

**Application 2** *(Apply — equipartition from partition function)*. A diatomic gas molecule has translational kinetic energy $E = p^2/2m$ in three dimensions plus rotational kinetic energy $E_\text{rot} = L^2/2I$ in two dimensions ($L$ is angular momentum, $I$ is moment of inertia). Treating both classically and using the Gaussian integral result $\int e^{-ax^2} dx = \sqrt{\pi/a}$, show that $\langle E_\text{total} \rangle = \frac{5}{2} k_B T$. Identify the five degrees of freedom.

**Application 3** *(Analyze — Fermi-Dirac vs. Boltzmann)*. Copper has a Fermi energy $E_F = 7.0$ eV. (a) At room temperature ($k_BT = 0.025$ eV), what fraction of the Fermi energy is the thermal energy? (b) Using the Fermi-Dirac distribution, find the probability that a state at $E_F + 0.1$ eV is occupied. (c) What would the Boltzmann distribution predict for this same state, using $E_F$ as the reference energy? (d) Why are the two answers so different despite 0.1 eV being much larger than $k_BT$?

**Synthesis 1** *(Analyze — heat capacity crossover)*. A solid at low temperature has two contributions to its heat capacity: an electronic term $C_e = \gamma T$ (from Fermi-Dirac statistics of conduction electrons) and a phonon term $C_p = \alpha T^3$ (from Bose-Einstein statistics of lattice vibrations, the Debye model). (a) At what temperature do the two contributions cross over, i.e., when is $C_e = C_p$? Express as $T^* = \sqrt{\gamma/\alpha}$. (b) Below $T^*$, which term dominates? (c) For copper, $\gamma \approx 7 \times 10^{-4}$ J/(mol·K²) and $\alpha \approx 5 \times 10^{-5}$ J/(mol·K⁴). Estimate $T^*$ in kelvin.

**Synthesis 2** *(Analyze — the classical limit)*. The Fermi-Dirac and Bose-Einstein distributions both reduce to the Boltzmann distribution in the limit where $e^{(E-\mu)/k_BT} \gg 1$. (a) Show algebraically that $f_\text{FD}(E) \to e^{-(E-\mu)/k_BT}$ and $f_\text{BE}(E) \to e^{-(E-\mu)/k_BT}$ when this condition holds. (b) Interpret the condition physically: when does it hold, and when does it break down? (c) For photons with $\mu = 0$, at what frequency does the Bose-Einstein photon distribution deviate significantly from the classical Boltzmann form at room temperature?

**Challenge** *(Apply + Analyze — the harmonic oscillator)*. A quantum harmonic oscillator has energy levels $E_n = (n + \frac{1}{2})\hbar\omega$ for $n = 0, 1, 2, \ldots$ The partition function is a geometric series:

$$Z = e^{-\hbar\omega/2k_BT} \sum_{n=0}^{\infty} e^{-n\hbar\omega/k_BT} = \frac{e^{-\hbar\omega/2k_BT}}{1 - e^{-\hbar\omega/k_BT}}.$$

(a) Compute $\langle E \rangle = -\partial \ln Z / \partial \beta$. (b) Show that for $k_BT \gg \hbar\omega$, $\langle E \rangle \to k_BT$ (classical equipartition). (c) Show that for $k_BT \ll \hbar\omega$, $\langle E \rangle \to \frac{1}{2}\hbar\omega$ (zero-point energy only). (d) From $\langle E \rangle$, derive $C_V(T)$ and show it drops to zero at low $T$. This is Einstein's 1907 result explaining why diamond has low heat capacity at room temperature — its vibrational frequency $\omega$ is high enough that $\hbar\omega \gg k_BT$ at 300 K.

---

## LLM Exercises

### Build the Boltzmann-distribution explorer (`08-boltzmann-distribution.html`)

> **Show.** Boltzmann distribution: $P_i = e^{-E_i/k_BT}/Z$, $Z = \sum e^{-E_i/k_BT}$. Average energy $\langle E\rangle$, heat capacity $C_v = (\langle E^2\rangle - \langle E\rangle^2)/(k_BT^2)$.
>
> **Say.** Build a Boltzmann-distribution and partition-function explorer.
>
> **Constrain.** D3 v7. Controls: number of energy levels $N_{\text{levels}}$ (slider 2–10), energy spacing $\Delta E$ (in units of $k_B$ — so $\Delta E = 1$ means $\varepsilon = k_B$ which corresponds to $T_{\text{anomaly}} \sim 1$ K), temperature $T$ (slider 0.1 to 100). Display: energy level diagram with occupation probability shown as bar width at each level; $Z$ computed; $\langle E\rangle$ vs. $T$ curve; $C_v$ vs. $T$ curve showing Schottky peak. Filename: `08-boltzmann-distribution.html`.
>
> **Verify.** (a) Two-level system: $C_v$ peaks at $k_BT \approx 0.4\varepsilon$. (b) As $T \to 0$, all probability concentrates in the ground state. (c) As $T \to \infty$, occupation is nearly uniform.

### Exploration

- Watch the Schottky peak emerge as you vary $\Delta E$ for a two-level system. The peak's location in $T$ is proportional to $\Delta E$.
- For an N-level system (e.g., 10 levels), look at how $\langle E\rangle$ grows: nearly linear in $T$ for $k_BT > \Delta E$ (classical equipartition), but with quantum corrections at low $T$.
- Compare a two-level system (single Schottky peak) to a 5-level system. The 5-level system's heat capacity is broader and has no single sharp peak.

### Extension prompt (chapter bridge)

> **Show.** Statistical mechanics gives me the partition function. I can now compute equilibrium thermodynamic quantities. But real engines operate out of equilibrium — irreversibly. Where do these losses come from?
>
> **Say.** Build a heat-engine simulator showing how real-engine irreversibility costs efficiency.
>
> **Constrain.** Display a thermodynamic cycle (Rankine, Brayton, etc.) with adjustable irreversibility parameters: finite $\Delta T$ at heat exchangers, isentropic efficiency of turbines and compressors. Compute the actual cycle efficiency and entropy generation rate.
>
> **Verify.** As irreversibilities increase, efficiency drops below Carnot bound; entropy generation rises.

Save as `08b-real-engine-preview.html`. Bridge to Chapter 9.

---

**Tags:** statistical mechanics, fundamental postulate, Boltzmann distribution, partition function, Helmholtz free energy, Schottky anomaly, classical limit, Fermi-Dirac distribution, Bose-Einstein distribution, equipartition
