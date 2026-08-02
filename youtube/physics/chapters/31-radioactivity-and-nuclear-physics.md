# Chapter 31 — Radioactivity and Nuclear Physics

*A million times more energy than chemistry knew about, locked in a layer of matter nobody had looked at yet.*

---

In 1898, Marie Curie was dissolving tonnes of uranium ore in a shed in Paris, separating and re-separating the elements by precipitation and recrystallization, looking for whatever was producing Becquerel's mysterious rays. She had no ventilation. Her hands were developing sores that would not heal. Her notebooks — still in lead-lined boxes at the Bibliothèque Nationale, too radioactive to handle without signing a liability waiver — record a typical day's work: no money, no proper laboratory, no help.

![Two side-by-side scale comparisons. Left: atom at radius 10⁻¹⁰ m with tiny nucleus 10⁻¹⁴ m at center — ratio shown to scale (not actually visible). Right: nuclear density factoid — a teaspoon of pure nucleus weighs ~10⁹ tonnes.](../images/31-radioactivity-and-nuclear-physics-fig-01.png)
*Figure 31.1 — Atom vs Nucleus — 100,000:1 in Radius, Yet 99.97% of the Mass*

What she was tracking came from a different layer of matter than chemistry knew about. Atomic physics — the electrons and their shells — involves energies of a few electron-volts. The rays she was measuring involved energies of *millions* of electron-volts. The source was not the electrons. It was the nucleus: a tiny dense object at the atom's center, containing most of the atom's mass and all of its positive charge, held together by a force that was at that point completely unknown.

The energy difference — MeV versus eV, a factor of a million — is the central fact of this chapter. It is why the Sun has been burning for five billion years. It is why nuclear weapons are so destructive. It is why a gram of uranium contains more usable energy than a tonne of coal. And it is why Marie Curie's notebooks will still be radioactive in a thousand years.

---

## What is a nucleus

A nucleus contains *protons* (charge $+e$, mass $1.0073$ u) and *neutrons* (charge 0, mass $1.0087$ u). Together, protons and neutrons are *nucleons*. The standard notation:

$$^A_Z X$$

where $Z$ is the number of protons (the atomic number — determines which element it is), $A$ is the total number of nucleons (mass number), and $N = A - Z$ is the number of neutrons. Different *isotopes* of an element have the same $Z$ but different $N$. Carbon-12 and carbon-14 are both carbon ($Z = 6$); they differ in neutron count.

One atomic mass unit: $1 \text{ u} = 931.5 \text{ MeV}/c^2$. So one u of mass, fully converted to energy, gives 931.5 MeV — about 250 million times the energy of a typical chemical bond.

Nuclear radii follow $r \approx (1.2 \text{ fm}) A^{1/3}$, where $1 \text{ fm} = 10^{-15}$ m. Nuclear density is roughly constant across the periodic table at about $2 \times 10^{17}$ kg/m³. A teaspoon of nuclear matter would weigh a billion tonnes.

What holds a nucleus together against the electrostatic repulsion of its protons? The *strong nuclear force* — short-range (acts only within about 2 fm), attractive between any pair of nucleons, roughly 100 times stronger than electromagnetism at nuclear scales. Beyond a few fm, it is effectively zero. Below that distance, it is the dominant force in the universe.

<!-- → [INFOGRAPHIC: Nuclear scale comparison — four panels at increasing magnification: (1) atom (~10⁻¹⁰ m) with electron cloud and tiny dot at center; (2) nucleus (~10⁻¹⁴ m) showing protons and neutrons packed together; (3) single nucleon (~10⁻¹⁵ m = 1 fm); (4) force vs. distance graph showing strong force (attractive, dominant below ~2 fm, zero beyond ~3 fm) vs. Coulomb repulsion (falling as 1/r², present at all distances); caption: the strong force acts only at fm scales — it is what keeps protons from flying apart, but it cannot reach across a large nucleus, which is why heavy nuclei become unstable] -->

---

## Three ways a nucleus can decay

![Radioactive source emits three rays into a magnetic field (B into page). α (positive, heavy): slight deflection right. β (negative electron, light): strong deflection left. γ (neutral, massless EM): no deflection. First...](../images/31-radioactivity-and-nuclear-physics-fig-02.png)
*Figure 31.2 — Rutherford 1899 — Magnetic Field Sorts α, β, γ by Charge and Mass*

Ernest Rutherford, in 1899, placed a radioactive sample in a magnetic field and watched the emitted radiation separate into three beams. One beam was undeflected — gamma rays, eventually identified as high-energy photons. One beam bent as if positively charged — alpha particles, helium nuclei with two protons and two neutrons. One beam bent the other way, indicating negative charge and very small mass — beta particles, high-energy electrons (or, in $\beta^+$ decay, positrons).

That's the taxonomy. Three modes. Each corresponds to a specific mechanism in the nucleus.

**Alpha decay.** The nucleus emits a $^4_2\text{He}$ nucleus — two protons, two neutrons:

$$^A_Z X \to {^{A-4}_{Z-2}} Y + {^4_2\text{He}}.$$

Mass number drops by 4, atomic number drops by 2. Example: $^{238}_{92}\text{U} \to {^{234}_{90}\text{Th}} + \alpha$. The Q-value — energy released — is the mass difference times $c^2$:

$$Q = [m(^{238}\text{U}) - m(^{234}\text{Th}) - m(^4\text{He})] \times 931.5 \text{ MeV/u} \approx 4.27 \text{ MeV}.$$

About a million times the energy of a chemical bond, from a single nuclear event.

**Beta-minus decay.** A neutron inside the nucleus converts to a proton, emitting an electron and an antineutrino:

$$n \to p + e^- + \bar{\nu}_e.$$

Mass number unchanged, atomic number increases by 1. Example: $^{14}\text{C} \to {^{14}\text{N}} + e^- + \bar{\nu}_e$ — the decay that makes carbon-14 dating possible.

![Plot of electron-count vs kinetic energy in beta decay. Expected: sharp peak at Q-value (delta function), conservation of energy. Observed: broad continuous distribution up to Q. Missing energy carried away by undetected...](../images/31-radioactivity-and-nuclear-physics-fig-03.png)
*Figure 31.3 — Beta Decay — Continuous Energy Spectrum Predicted the Neutrino*

The electron didn't exist before the decay. It was *created* in the conversion. The antineutrino was also created — a nearly massless, electrically neutral particle that interacts only via the weak force, capable of passing through light-years of lead without interacting. Wolfgang Pauli postulated the neutrino in 1930 because the energy spectrum of beta electrons was continuous, not discrete — something was carrying off a variable amount of energy unseen. Conservation of energy demanded the neutrino exist. Frederick Reines and Clyde Cowan detected it experimentally in 1956.

**Beta-plus decay.** A proton converts to a neutron, emitting a positron and a neutrino: $p \to n + e^+ + \nu_e$. Atomic number decreases by 1. This is the mechanism exploited in PET imaging (Chapter 32): the emitted positron immediately annihilates with a nearby electron, producing two 511-keV gamma photons back-to-back — which detectors locate to reconstruct the emission site.

**Gamma decay.** A nucleus in an excited state drops to a lower energy level, emitting a photon. No change in $Z$ or $A$. The photon's energy — typically MeV — is the gap between nuclear energy levels.

In every decay, charge is conserved (total $Z$ unchanged across the equation), mass number is conserved (total $A$ unchanged), and energy is conserved (the kinetic energy of products equals the mass-energy released, the Q-value).

<!-- → [TABLE: Summary of three decay modes — columns: decay type, particle emitted, change in Z, change in N, change in A, typical energy (MeV), conservation laws; rows: alpha (helium-4 nucleus, −2, −2, −4, 4–9 MeV), beta-minus (electron + antineutrino, +1, −1, 0, 0–3 MeV), beta-plus (positron + neutrino, −1, +1, 0, 0–3 MeV), gamma (photon, 0, 0, 0, 0.1–10 MeV); caption: all three modes conserve charge and mass number; the emitted particle is created in the decay, not stored in advance] -->

---

## The decay law

A radioactive nucleus doesn't remember how old it is. Each nucleus has the same probability per unit time of decaying, regardless of how long it has been sitting there. This is a purely quantum-mechanical property — the nucleus has no internal clock. The consequence: if $N(t)$ is the number of undecayed nuclei at time $t$,

$$\frac{dN}{dt} = -\lambda N,$$

where $\lambda$ is the decay constant (probability per unit time per nucleus). This is the same equation as any first-order decay process, and the solution is the same:

$$\boxed{N(t) = N_0 e^{-\lambda t}.}$$

The *half-life* $t_{1/2}$ — the time after which half the sample remains — satisfies $e^{-\lambda t_{1/2}} = 1/2$, so

$$\boxed{t_{1/2} = \frac{\ln 2}{\lambda} \approx \frac{0.693}{\lambda}.}$$

After $n$ half-lives, $N = N_0 / 2^n$. After 10 half-lives, $1/1024$ of the original remains.

The range of half-lives is staggering: from about $10^{-23}$ seconds (some excited nuclear states, about the time for light to cross a nucleus) to $2.2 \times 10^{24}$ years for tellurium-128 (roughly $10^{14}$ times the age of the universe). The existence of uranium-238 on Earth ($t_{1/2} = 4.5$ billion years) tells you something: it was made in a supernova explosion not long before the solar system formed. If its half-life were much shorter, it would already be gone.

*Activity* is the decay rate $A = \lambda N$, measured in becquerels (1 Bq = 1 decay per second). The curie (1 Ci = $3.7 \times 10^{10}$ Bq) was defined as the decay rate of one gram of radium-226 — Marie Curie's isotope.

<!-- → [TABLE: Half-life spectrum across isotopes — columns: isotope, decay mode, half-life, practical use; rows: Po-214 (alpha, 164 μs, decay chain intermediate), Na-24 (beta, 14.96 h, medical tracer), I-131 (beta/gamma, 8.02 days, thyroid therapy), C-14 (beta, 5730 y, archaeological dating), K-40 (beta/gamma, 1.25 Gy, geological dating), U-238 (alpha, 4.47 Gy, Earth-age dating), Te-128 (beta, 2.2 × 10²⁴ y, longest known); caption: half-lives span 46 orders of magnitude; isotopes useful for dating must have half-lives comparable to the age being measured — C-14 for millennia, U-238 for billions of years] -->

---

## Carbon-14 dating: a clock built into matter

Cosmic-ray neutrons in the upper atmosphere strike nitrogen-14, producing carbon-14: $n + {^{14}\text{N}} \to {^{14}\text{C}} + p$. The C-14 is radioactive ($t_{1/2} = 5730$ years) and decays back to nitrogen, but is continuously replenished by the cosmic-ray flux. A steady-state equilibrium is established in the atmosphere: about 1 C-14 atom per $10^{12}$ C-12 atoms.

Living organisms exchange carbon with the atmosphere — by breathing, eating, photosynthesizing. Their internal C-14/C-12 ratio matches the atmospheric ratio. When an organism dies, the exchange stops. The C-14 starts decaying away. The ratio falls exponentially.

To date a sample: measure its current C-14/C-12 ratio. Compute what fraction of the original C-14 remains. Apply $N(t) = N_0 e^{-\lambda t}$ backward to find $t$.

In 1988, three independent laboratories dated a small sample of the Shroud of Turin. The C-14 activity was consistent with cloth woven between 1260 and 1390 AD. The technique works for any organic material up to about 10 half-lives — roughly 50,000 years. For rocks billions of years old, potassium-40 ($t_{1/2} = 1.25$ Gy) or uranium-238 ($t_{1/2} = 4.5$ Gy) serve as the clocks instead.

Clair Patterson used uranium-lead ratios in iron meteorites to measure the age of the solar system in 1956: $4.55 \pm 0.07$ billion years. This number has been confirmed repeatedly to four significant figures. The Earth's age is not a guess; it is a measurement, made with the radioactive-decay law and atomic-mass data.

<!-- → [CHART: Carbon-14 decay curve — x-axis: time in thousands of years (0 to 60 ky); y-axis: fraction of original C-14 remaining (1.0 to 0); smooth exponential decay curve with half-life markers at 5730, 11460, 17190 years labeled; shaded region beyond 50,000 years labeled "dating limit — too little C-14 remains"; annotations showing: 1300 AD cloth (~700 y, ~92% remaining), Egyptian mummy sample (~3,000 y, ~70% remaining), Lascaux cave paintings (~17,000 y, ~12% remaining); caption: each half-life removes half the remaining C-14; the clock reads the current ratio against the known initial value] -->

---

## Binding energy: why MeV, not eV

Here is the calculation that reveals the energy scale of nuclear physics.

Take a helium-4 nucleus: 2 protons and 2 neutrons. Weigh it precisely. Now separately weigh 2 free protons and 2 free neutrons, and add up their masses. The two masses are not equal. The helium nucleus is lighter — by about 0.030 u. This is the *mass defect* $\Delta m$.

The missing mass became *binding energy* — the energy that was released when those four nucleons came together and is now required to pull them apart. By $E = mc^2$:

$$\text{BE} = \Delta m \cdot c^2 = 0.0306 \text{ u} \times 931.5 \text{ MeV/u} \approx 28.5 \text{ MeV}.$$

In practice, we use atomic masses (which include the electron masses), so:

$$\text{BE} = [Z \cdot m(^1\text{H}) + N \cdot m_n - m(^A X)] \times 931.5 \text{ MeV/u}.$$

For helium-4: BE/nucleon $\approx 7.1$ MeV. For iron-56, the calculation gives about 8.8 MeV/nucleon. For uranium-238, about 7.6 MeV/nucleon.

Plot BE/nucleon versus mass number $A$ for every stable isotope and you get a curve that rises from hydrogen, peaks near iron ($A \approx 56$, at about 8.8 MeV/nucleon), and gently falls off toward heavy nuclei. This is the most consequential graph in nuclear physics.

The shape of the curve tells you two things immediately.

**Fusion releases energy** for nuclei lighter than iron: combining light nuclei into heavier ones moves you up the curve, releasing the energy difference. Hydrogen fusing into helium releases about 6.3 MeV/nucleon of combined mass. This is what stars do. The Sun converts about $4 \times 10^9$ kg of mass into energy every second — pure $E = mc^2$ — by fusing hydrogen into helium in its core. It will continue for another 5 billion years before exhausting its hydrogen supply.

**Fission releases energy** for nuclei heavier than iron: splitting a heavy nucleus into two medium-weight fragments moves both fragments up the curve, releasing roughly 0.9 MeV/nucleon. Splitting uranium-235 releases about 200 MeV per fission event. A gram of uranium-235 contains $2.6 \times 10^{21}$ atoms; fully fissioned, they release roughly $8 \times 10^{10}$ joules — the energy in about 2,500 tonnes of coal.

*Stars stop burning at iron.* Once the stellar core is iron, there is no energy to be gained from further fusion or further fission. The iron core collapses, triggering a supernova — the event that forges elements heavier than iron by rapid neutron capture and scatters them into the interstellar medium. Your gold ring was made in a neutron-star merger. Your phosphorus was made in a supernova. Carl Sagan's "we are made of star stuff" is quantitative nuclear physics.

<!-- → [CHART: Binding energy per nucleon vs. mass number — x-axis: mass number A from 0 to 240; y-axis: binding energy per nucleon in MeV from 0 to 9; smooth curve rising steeply from H (0) to He-4 (~7.1), leveling off near Fe-56 peak (~8.8 MeV), gently declining to U-238 (~7.6); annotations: left side labeled "fusion releases energy" with arrow pointing right, right side labeled "fission releases energy" with arrow pointing left, peak labeled "Fe-56 — most tightly bound"; selected nuclei labeled: H-1, He-4, C-12, Fe-56, U-238; caption: the peak near iron explains both why stars stop fusing at iron and why heavy nuclei can be split for energy — all roads on this curve lead to iron] -->

---

## Quantum tunneling: how alphas escape

![Potential energy U(r) for an alpha inside the parent nucleus. Strong-force well at r < R; Coulomb barrier rises sharply above the alpha's energy E_α. Classically forbidden — alpha tunnels through the barrier. Probability ~...](../images/31-radioactivity-and-nuclear-physics-fig-06.png)
*Figure 31.6 — Alpha Decay — Coulomb Barrier Tunneled, Not Climbed*

Here is the puzzle of alpha decay. An alpha particle inside a large nucleus has kinetic energy of about 5 MeV. Outside the nucleus, if it were free, it would be repelled by the Coulomb force of the remaining protons. The Coulomb barrier — the potential energy at the nuclear surface — is typically 20–30 MeV for heavy nuclei, much higher than the alpha's kinetic energy.

Classically, the alpha cannot escape. It has insufficient energy to climb over the wall. Yet alpha decay happens — and happens at rates that vary enormously from nucleus to nucleus.

The resolution is quantum mechanics. The alpha is not a point particle following a classical trajectory; it is a quantum-mechanical object described by a wavefunction. Inside the classically forbidden region — the barrier — the wavefunction does not drop to zero. It decays exponentially, but it does not vanish. The alpha's probability amplitude extends through the barrier and emerges on the other side. Given enough attempts (and the alpha is bouncing around inside the nucleus at roughly $10^{21}$ times per second), eventually it tunnels through.

George Gamow worked this out in 1928, in one of the first applications of the Schrödinger equation to nuclear physics. The tunneling probability depends exponentially on the barrier height and width — both of which depend sensitively on the alpha's kinetic energy and the nuclear charge $Z$. A small increase in the alpha's energy means a shorter, lower barrier to tunnel through, and an exponentially larger tunneling probability, which means an exponentially shorter half-life.

![Plot of log₁₀(half-life in seconds) vs 1/√E_α for alpha emitters. From Po-212 (t½ = 0.3 µs, E_α = 8.95 MeV) to U-238 (t½ = 1.4×10¹⁷ s, E_α = 4.27 MeV). Linear relationship — direct evidence for Gamow's tunneling formula. 17...](../images/31-radioactivity-and-nuclear-physics-fig-07.png)
*Figure 31.7 — Geiger-Nuttall — Log Half-Life Plotted Against 1/√E_α Is Linear, 17 Decades Wide*

This explains one of the more striking empirical patterns in nuclear physics: alpha-decay half-lives span 17 orders of magnitude (from about a microsecond to about $10^{10}$ years) while the corresponding alpha-particle kinetic energies vary only over a factor of 2 or 3, from about 4 MeV to about 9 MeV. The *Geiger-Nuttall law* (1911) observed this dependence empirically; Gamow's tunneling calculation derived it from first principles in 1928. The agreement between theory and experiment is exact. Quantum tunneling is not a metaphor — it is a precise, calculable, experimentally confirmed phenomenon.

<!-- → [INFOGRAPHIC: Alpha decay Coulomb barrier diagram — x-axis: distance from nuclear center; y-axis: potential energy in MeV; inside the nucleus (r < R_nucleus): flat potential well at ~0 MeV (strong-force binding); at nuclear surface: sharp rise of Coulomb barrier to ~25 MeV peak; outside nucleus: Coulomb repulsion falling as 1/r toward 0 at infinity; horizontal dashed line at ~5 MeV labeled "alpha kinetic energy — classically forbidden to escape"; exponentially decaying wavefunction drawn inside the barrier region, with small nonzero amplitude emerging outside; arrow labeled "tunneling probability ∝ e^(−2κL)" where κ depends on barrier height and L on barrier width; caption: the alpha's wavefunction doesn't vanish inside the barrier — it decays exponentially but leaks through, giving a small but nonzero probability of escape per unit time] -->

---

## A calculation worth doing: the Sun's fuel supply

The Sun runs on the proton-proton chain, which net-converts four protons into one helium-4 nucleus:

$$4 \,{^1\text{H}} \to {^4\text{He}} + 2e^+ + 2\nu_e + 26.7 \text{ MeV}.$$

The 26.7 MeV comes from the mass defect. Let's check.

Four hydrogen atoms weigh $4 \times 1.00794 = 4.03176$ u. One helium-4 atom weighs $4.00260$ u. Two electron masses (the $e^+$ annihilate with electrons in the surrounding plasma, releasing additional energy, but we'll focus on the nuclear cycle): total mass difference is roughly

$$\Delta m \approx 4.03176 - 4.00260 = 0.02916 \text{ u}.$$

In energy: $0.02916 \times 931.5 \approx 27.2$ MeV per fusion cycle — close to the tabulated $26.7$ MeV (the small difference involves the positron annihilation and neutrino energy loss).

The Sun's luminosity is $3.86 \times 10^{26}$ W. At 26.7 MeV per cycle and $4.27 \times 10^{-12}$ J/MeV:

$$\text{Cycles/second} = \frac{3.86 \times 10^{26}}{26.7 \times 4.27 \times 10^{-12}} \approx 3.4 \times 10^{38}.$$

Four protons consumed per cycle, mass $4 \times 1.67 \times 10^{-27}$ kg:

$$\text{Mass consumed/second} = 3.4 \times 10^{38} \times 4 \times 1.67 \times 10^{-27} \approx 2.3 \times 10^{12} \text{ kg/s}.$$

About 2.3 billion kg of hydrogen converted to helium every second — roughly the mass of a small mountain, every second, for five billion years and counting. But only 0.7% of that mass actually converts to energy (the binding-energy difference per nucleon); the rest remains as helium. The Sun's total mass is $2 \times 10^{30}$ kg, about 75% hydrogen. At this burn rate, it has enough hydrogen fuel for about $10^{10}$ years. We're about halfway through.

That same physics, run backward — splitting heavy nuclei rather than fusing light ones — powers every nuclear reactor and was the mechanism in every nuclear weapon test between 1945 and the 1996 Comprehensive Test Ban Treaty. The binding-energy curve, and $E = mc^2$, are the complete quantitative explanation.

<!-- → [TABLE: Energy density comparison — columns: fuel/source, energy release per kg (J/kg), mechanism, notes; rows: wood combustion (~1.5 × 10⁷ J/kg, chemical bond breaking), coal (~3 × 10⁷ J/kg, chemical), gasoline (~4.7 × 10⁷ J/kg, chemical), uranium-235 fission (~8 × 10¹³ J/kg, nuclear — 0.09% mass converted), hydrogen fusion to helium (~6 × 10¹⁴ J/kg, nuclear — 0.7% mass converted), matter-antimatter annihilation (~9 × 10¹⁶ J/kg, 100% mass converted); caption: nuclear fuel delivers 10⁶–10⁷ times more energy per kilogram than chemical fuel because MeV >> eV by exactly that factor — the binding-energy curve in action] -->

---

## Three commitments

**Nuclei decay in three modes.** Alpha ($^4$He emission, $Z$ drops by 2), beta (neutron ↔ proton conversion, $Z$ changes by 1, $A$ fixed), gamma (photon from nuclear de-excitation, nothing changes). Charge and mass number are conserved in every decay.

![Log time axis showing useful dating ranges for three isotopes. C-14 (T½ = 5,730 yr): useful 100 yr–50,000 yr. K-40 (T½ = 1.25 Gyr): 100,000 yr–4 Gyr. U-238 (T½ = 4.5 Gyr): 1 Myr to age of solar system. Each isotope: 1–10...](../images/31-radioactivity-and-nuclear-physics-fig-04.png)
*Figure 31.4 — Radioactive Dating — Pick the Right Isotope for the Right Era*

**Decay is exponential.** $N(t) = N_0 e^{-\lambda t}$, with $t_{1/2} = \ln 2 / \lambda$. Each nucleus decays independently, with fixed probability per unit time. Half-lives range over 46 orders of magnitude. Radioactive dating works because the decay law is exact, precise, and immune to chemical environment, temperature, or pressure.

![Plot of binding energy per nucleon vs mass number A. Sharp rise from H, peak around 8.8 MeV at Fe-56, gradual decline to U-238. Light nuclei fuse to reach higher BE/A; heavy nuclei fission. Iron is the most-bound nucleus and...](../images/31-radioactivity-and-nuclear-physics-fig-05.png)
*Figure 31.5 — Binding Energy per Nucleon — Peak at Iron-56, Fusion to Left, Fission to Right*

**Nuclear energies are MeV; atomic energies are eV.** The mass defect — measured in hundredths of an atomic mass unit — converts to binding energies of 7–9 MeV per nucleon via $E = mc^2$. Fusion of light nuclei and fission of heavy nuclei both move toward iron on the binding-energy-per-nucleon curve, releasing the difference. Quantum tunneling makes alpha decay possible despite classically insurmountable Coulomb barriers.

The single fact that matters most: **the energy scale of nuclear physics is a million times the energy scale of chemistry, because the strong nuclear force is enormously more powerful than the electromagnetic force at short range.** Everything else in this chapter follows from that one number.

---

## Exercises

### Warm-up

**31.1** *(Nuclear notation)* For each of the following nuclei, state the number of protons, neutrons, and nucleons: (a) $^{12}_6\text{C}$, (b) $^{14}_6\text{C}$, (c) $^{238}_{92}\text{U}$, (d) $^{4}_2\text{He}$. Which pair are isotopes of the same element?

**31.2** *(Alpha decay)* Write the complete alpha-decay equation for radium-226 ($^{226}_{88}\text{Ra}$). Identify the daughter nucleus. Verify that both $Z$ and $A$ are conserved.

**31.3** *(Beta-minus decay)* Write the complete beta-minus decay equation for carbon-14 ($^{14}_6\text{C}$). What is the daughter nucleus? Why does $A$ not change?

**31.4** *(Half-life arithmetic)* An isotope has a half-life of 8.0 days. A sample initially contains $6.4 \times 10^{10}$ atoms. How many remain after (a) 8 days, (b) 24 days, (c) 40 days?

**31.5** *(Decay constant)* Iodine-131 has $t_{1/2} = 8.02$ days. Compute its decay constant $\lambda$ in units of day$^{-1}$ and s$^{-1}$.

### Application

**31.6** *(Carbon-14 dating)* A wooden artifact has $38\%$ of the C-14 activity of a living sample. Estimate its age. ($t_{1/2} = 5730$ y for C-14.)

**31.7** *(Q-value for alpha decay)* Using the atomic masses given — $m(^{226}\text{Ra}) = 226.0254$ u, $m(^{222}\text{Rn}) = 222.0176$ u, $m(^4\text{He}) = 4.0026$ u — compute the Q-value for the alpha decay of radium-226. Express in MeV.

**31.8** *(Binding energy of helium-4)* Compute the total binding energy and binding energy per nucleon for $^4_2\text{He}$, using $m(^1\text{H}) = 1.00794$ u, $m_n = 1.00867$ u, $m(^4\text{He}) = 4.00260$ u. Express BE in MeV.

**31.9** *(Activity)* A sample of $^{131}\text{I}$ ($t_{1/2} = 8.02$ days) has initial activity $3.7 \times 10^{10}$ Bq. (a) How many atoms does it initially contain? (b) What is the activity after 24 days?

### Synthesis

**31.10** *(Binding energy per nucleon — fission energy)* Uranium-235 has BE/nucleon $\approx 7.59$ MeV. Typical fission products (barium-141 and krypton-92) have BE/nucleon $\approx 8.39$ MeV and $8.15$ MeV respectively. (a) Estimate the energy released per fission by computing the difference in total binding energy before and after. (b) Compare your estimate to the standard value of $\sim 200$ MeV per fission.

**31.11** *(Uranium-lead dating)* Uranium-238 decays to lead-206 with $t_{1/2} = 4.47 \times 10^9$ years. A rock sample contains a Pb-206/U-238 molar ratio of 0.35. Assuming all the Pb-206 came from U-238 decay and there was no initial Pb-206, estimate the age of the rock.

**31.12** *(The neutrino argument)* Early beta-decay experiments found that beta electrons had a continuous energy spectrum from 0 up to a maximum value $Q$, rather than a single discrete energy $Q$. (a) Explain why a two-body decay (nucleus → daughter + electron) would produce a discrete electron energy. (b) Explain how a three-body decay (nucleus → daughter + electron + antineutrino) produces a continuous spectrum. (c) State Pauli's 1930 conclusion and what conservation law he was preserving.

### Challenge

**31.13** *(Gamow tunneling — qualitative scaling)* The tunneling probability through the Coulomb barrier scales as $P \propto e^{-2G}$, where $G \propto Z/\sqrt{E_\alpha}$ ($Z$ is the daughter nucleus charge, $E_\alpha$ is the alpha kinetic energy). (a) Two alpha emitters have $E_\alpha = 4.2$ MeV and $E_\alpha = 8.8$ MeV, both with the same $Z$. By what factor does the exponent $G$ change? (b) If $G_1 = 40$ for the 4.2 MeV emitter, estimate $G_2$ for the 8.8 MeV emitter. (c) Estimate the ratio of half-lives $t_{1/2,1}/t_{1/2,2}$ using $t_{1/2} \propto e^{2G}$. (d) Compare to the observed range of alpha-decay half-lives spanning $\sim 10^{17}$ and comment on whether your estimate is in the right ballpark.

**31.14** *(Stellar nucleosynthesis)* The triple-alpha process, by which stars fuse three helium-4 nuclei into carbon-12, requires an excited state of C-12 (the "Hoyle state") at 7.65 MeV above the ground state. Fred Hoyle predicted this state must exist in 1953 before it was found experimentally, because without it the solar abundance of carbon would be negligible. (a) Using the BE/nucleon values: He-4 ($\approx 7.07$ MeV/nucleon) and C-12 ($\approx 7.68$ MeV/nucleon), compute the total energy difference between $3 \times ^4\text{He}$ and $^{12}\text{C}$ ground state. (b) Why must the reaction pass through a resonance (excited state) near this energy for the rate to be significant? (c) What does it mean physically that the existence of carbon-based life required a nuclear energy level at almost exactly the right value?

---

## Still puzzling

The deepest unresolved question this chapter raises: *why do the proton and neutron have the masses they do?* They differ by only 0.14% — the neutron is slightly heavier — and that small difference is why free neutrons are unstable while free protons are not. If the mass difference were reversed, neutrons would be stable, protons would decay, and there would be no atoms. These masses depend on quark masses and the strong-force coupling constant (Chapter 33), but why those constants have the values they do is not explained by any current theory. The fact that they happen to be in the range that allows nuclear stability, and hence chemistry, and hence life, is either a profound accident or a hint at something we do not yet understand.

---

## LLM Exercise — Chapter 31: Radioactivity in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A Logbook entry for nuclear physics. Most everyday phenomena involve no obvious radioactivity, but background radiation, GPS clock physics (Cs-137 and other isotopes), smoke detectors (Am-241), bananas (K-40), all touch nuclear physics. You can compute one quantitative property or write an "exception entry" identifying the nearest radioactive connection.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste your 1-sentence description].

For Chapter 31, I want to think about radioactivity and nuclear physics. Most everyday phenomena are not directly nuclear, but background radiation is everywhere (cosmic rays, K-40 in bananas, radon from soil, terrestrial gamma background).

Please:

1. Identify ONE nuclear or radioactivity aspect connected to my phenomenon. Examples: for a bike commute — cosmic-ray muons hitting me (Chapter 28!), terrestrial gamma background from soil, possible radon exposure in poorly ventilated areas, Am-241 in any smoke detectors I pass. For a coffee maker — K-40 in any banana I eat with my coffee (about 15 Bq per medium banana), trace radium in some heating elements, cosmic-ray background. For a basketball shot — K-40 in my own muscle tissue (~50 Bq/kg), cosmic-ray background. For a marathon — additional cosmic-ray exposure from longer outdoor time, possible commercial-flight exposure if I'm running a destination race.

2. Apply ONE chapter equation. Compute total radiation dose (multiply activity × time × energy per decay × biological factor), or estimate decay rate of a specific isotope at known concentration, or estimate half-life-derived activity.

3. Specify input numbers (look up the isotope's half-life, decay energy, and natural abundance).

4. Run the calculation. Report value with units.

5. One sanity check: does your computed dose agree with the typical natural-background dose of ~$0.1$ μSv/hour at sea level?

6. One sentence connecting this to Chapter 32 (medical applications of nuclear physics) — radiotherapy and medical imaging are next.

Save the output as logbook/chapter-31-radioactivity.md.
```

### What this produces

A Logbook entry connecting your phenomenon to natural radioactivity (which is everywhere) or to specific isotopes used in nearby technology.

### How to adapt this prompt

- *For phenomena indoors:* Radon is often the dominant exposure (especially in basements). Look up your local radon levels.
- *For phenomena involving travel:* Aircraft flight at $10$ km altitude increases cosmic-ray dose by ~$50\times$.
- *For ChatGPT/Gemini:* Identical with interface substitutions.

### Connection to previous chapters

Builds on Chapter 28 ($E = mc^2$ for binding energies) and Chapter 29 (quantum tunneling for alpha decay; photons for gamma rays).

### Preview of next chapter

Chapter 32 (medical applications of nuclear physics) shows how the principles of this chapter — specific isotopes, half-lives, decay modes — power X-ray imaging, CT scans, PET scans, MRI, radiotherapy, and radioisotope-based diagnostics.

---

## Connections forward

Chapter 32 uses the isotopes, half-lives, and decay modes of this chapter for diagnostic imaging (PET, SPECT, gamma-knife) and therapy (brachytherapy, proton therapy). Chapter 33 (particle physics) breaks the proton and neutron into quarks, explains the strong force as gluon exchange, and shows the Standard Model of which the strong nuclear force is one sector. Chapter 34 (frontiers) considers the open questions — why proton and neutron masses have the values they do, the matter-antimatter asymmetry of the universe, and the search for a theory that unifies gravity with the other three forces.

---

**Tags:** nuclear-physics, radioactivity, half-life, binding-energy, quantum-tunneling, Feynman-style
