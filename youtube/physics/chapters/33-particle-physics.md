# Chapter 33 — Particle Physics

*The inventory of everything, and what it leaves out.*

---

![Schematic diphoton invariant-mass distribution from ATLAS/CMS 2012. Smooth falling continuum background from QCD; sharp Gaussian-like peak at m_γγ ≈ 125 GeV. Bump corresponded to Higgs boson decay H → γγ. 5σ significance.](../images/33-particle-physics-fig-01.png)
*Figure 33.1 — Higgs Discovery (July 4, 2012) — A 5σ Bump in the Diphoton Spectrum at 125 GeV*

On July 4, 2012, Peter Higgs, age 83, sat in an auditorium at CERN and watched two experimental collaborations — each comprising roughly three thousand physicists — present data from the Large Hadron Collider. Both experiments showed the same thing: a clear bump in their data at an invariant mass of about 125 GeV, with a combined statistical significance of five sigma, corresponding to a probability smaller than one in three million that it was a random fluctuation.

Higgs wipes tears from his eyes. He had predicted this particle in 1964. The hunt had taken 48 years and two continents of accelerator experiments.

The Higgs boson — the last unobserved piece of the Standard Model of particle physics — had been found.

![Comparison table for the four forces. Strong: 1 (relative), range ~1 fm, gluon, holds nuclei. Electromagnetic: 10⁻², infinite, photon, atoms. Weak: 10⁻⁶, ~10⁻¹⁸ m, W/Z, beta decay. Gravity: 10⁻³⁹, infinite, graviton...](../images/33-particle-physics-fig-02.png)
*Figure 33.2 — Four Fundamental Forces — Strength, Range, Carrier, Example*

The Standard Model is the theory that describes what the fundamental particles are, what forces act between them, and where particle masses come from. It is the most precisely tested physical theory in the history of science. Every particle it predicts has been observed. Every quantitative prediction it has made has been confirmed by experiment.

It is also clearly not the final theory. This chapter is about what the Standard Model contains, how we know it, and where it stops working.

---

## Forces and their carriers

The story of particle physics begins not with particles but with forces — and with a question Hideki Yukawa asked in 1935.

Protons in a nucleus are positively charged and pack together at distances of about $10^{-15}$ m (a femtometer). Their Coulomb repulsion at that distance is enormous — far larger than any attractive force known in 1935. And yet nuclei are stable. Something holds them together, something stronger than electromagnetism at short range. Yukawa asked: what kind of force could do that, and could we estimate the mass of whatever mediates it?

He reasoned by analogy with electromagnetism, where forces are mediated by photon exchange. If a nuclear force were mediated by some massive particle, the Heisenberg uncertainty principle sets how far the particle can travel before it must be absorbed: a virtual particle of mass $m$ "borrows" energy $\Delta E = mc^2$ from the vacuum for time $\Delta t \sim \hbar/(mc^2)$, traveling at most a distance $c\,\Delta t = \hbar/(mc)$. Setting this equal to the known strong-force range of $\sim 1$ fm:

$$mc^2 \sim \frac{\hbar c}{R} = \frac{197 \text{ MeV}\cdot\text{fm}}{1\text{ fm}} \approx 200 \text{ MeV.}$$

Yukawa predicted a mediator particle of about 200 MeV/$c^2$. In 1947, Cecil Powell found it in cosmic rays — the pion, with mass 140 MeV/$c^2$. The prediction was right to within a factor of 1.4. The 1949 Nobel went to Yukawa; the 1950 Nobel to Powell.

This was the template. Every force is mediated by carrier particles. The properties of the carriers determine the properties of the force. Massive carriers give short-range forces; massless carriers give long-range ($1/r^2$) forces.

The complete inventory of forces and their carriers:

| Force | Relative strength | Range | Carriers |
|---|---|---|---|
| Strong nuclear | 1 | $< 10^{-15}$ m | 8 gluons |
| Electromagnetic | $10^{-2}$ | $\infty$ | photon |
| Weak | $10^{-13}$ | $< 10^{-18}$ m | $W^+, W^-, Z^0$ |
| Gravity | $10^{-38}$ | $\infty$ | graviton (conjectured) |

<!-- → [FIGURE: Force range vs. carrier mass diagram. Horizontal axis: carrier mass (MeV/c²), logarithmic, from 0 (photon) to 10⁵ (W boson). Vertical axis: force range (m), logarithmic, from 10⁻¹⁸ m to ∞. Four points plotted: photon (mass 0, range ∞), gluon (effectively confined, labeled separately), W/Z bosons (80,000 MeV/c², range ~10⁻¹⁸ m), pion (140 MeV/c², range ~10⁻¹⁵ m). Hyperbola R = ℏc/(mc²) drawn through pion and W/Z points. Caption: Force range scales inversely with carrier mass, as predicted by the Heisenberg uncertainty principle. Yukawa's 1935 prediction of the pion mass from the strong-force range was the template for all subsequent force-carrier predictions.] -->

![Four-panel sequence: quark and antiquark connected by a flux tube of gluon field. Pull apart: tube stretches, energy density grows. Reach a threshold: tube snaps and a new q-q̄ pair forms from the vacuum. Two pairs of mesons...](../images/33-particle-physics-fig-05.png)
*Figure 33.5 — Quark Confinement — Pull a Quark, Pay With a New Quark-Antiquark Pair*

The strong force behaves unusually: it grows *stronger* as quarks are pulled farther apart (asymptotic freedom). This is why quarks are confined — you can never isolate one. Pull two quarks apart and the field energy between them eventually exceeds the energy needed to create a new quark-antiquark pair. The field produces new particles instead of allowing free quarks. This has been verified in countless accelerator experiments.

Electromagnetism is mediated by photons and is the force responsible for all atomic physics — every chemical bond, every biological molecule. Its quantum theory (QED) predicts the electron's magnetic moment to 13 significant figures, in agreement with measurement. This is the most precisely tested calculation in science.

The weak force mediates beta decay — the process by which a neutron becomes a proton, an electron, and an antineutrino. The $W^\pm$ and $Z^0$ bosons that carry it were predicted by electroweak unification and found at exactly the predicted masses (80 and 91 GeV/$c^2$) at CERN in 1983. The 1979 Nobel went to Glashow, Weinberg, and Salam for the unified theory; the 1984 Nobel to Rubbia and van der Meer for the experimental discovery.

Gravity is different. The hypothetical graviton has never been detected, and there is no quantum theory of gravity that is consistent with the Standard Model. Gravity is so feeble at the particle scale ($10^{-38}$ times the strong force between two protons) that its quantum effects are unobservably small in any foreseeable experiment. Chapter 34 returns to this.

---

## Antimatter and leptons

![Pie chart of cosmic composition: 5% ordinary baryonic matter (Standard Model), 27% dark matter (unknown particle), 68% dark energy (unknown cause). Annotation: SM is complete for what it covers, but covers only 5% of the...](../images/33-particle-physics-fig-06.png)
*Figure 33.6 — Cosmic Energy Budget — Standard Model Explains Only 5%*

In 1928, Paul Dirac wrote down a relativistic wave equation for the electron. It worked — but it predicted negative-energy solutions. Dirac reinterpreted these as positively charged electrons: antielectrons, or positrons. In 1932, Carl Anderson found one in a cloud chamber, looking at cosmic rays. The track curved the wrong way for an electron and had the wrong sign of curvature for a proton. Same mass as the electron, opposite charge.

Every particle has an antiparticle. Same mass, opposite quantum numbers (charge, lepton number, baryon number). When a particle meets its antiparticle, they annihilate: their combined rest-mass energy converts entirely into photons or into other particle-antiparticle pairs. An electron-positron pair at rest produces two photons, each of energy 511 keV = $m_e c^2$.

<!-- → [FIGURE: Cloud chamber track photograph schematic. Magnetic field into page. Two curved tracks emerging from a central point. One curves left (electron, labeled e⁻, negative charge). One curves right (positron, labeled e⁺, positive charge, same curvature radius → same mass). Arrow showing magnetic field direction. Caption: Anderson's 1932 cloud chamber observation of the positron. A cosmic-ray photon converted to an electron-positron pair. Both tracks have the same curvature radius (same mass), but they curve in opposite directions (opposite charges). This confirmed Dirac's 1928 prediction of the antielectron.] -->

The matter in your body is made entirely of particles, not antiparticles. We live in a universe that is asymmetrically matter-dominated. Why that is — why the Big Bang produced slightly more matter than antimatter, leaving the residual matter after annihilation — is one of the great open questions. The Standard Model contains the seeds of an answer (CP violation in weak-force decays) but not a quantitative solution.

**Leptons** are the fundamental particles that feel electromagnetism and the weak force but not the strong force. There are six, in three generations:

| Generation | Charged lepton | Neutrino |
|---|---|---|
| 1 | electron ($e^-$, 0.511 MeV) | $\nu_e$ (< 1 eV) |
| 2 | muon ($\mu^-$, 106 MeV) | $\nu_\mu$ |
| 3 | tau ($\tau^-$, 1777 MeV) | $\nu_\tau$ |

Each has its antiparticle. The muon is an electron in every observable way, just 207 times heavier. The tau is heavier still — 3500 electron masses. Why three generations? Unknown. Why these masses? Unknown. The Standard Model accommodates the values; it does not explain them.

Neutrinos were assumed massless until the late 1990s, when the Super-Kamiokande experiment in Japan and the Sudbury Neutrino Observatory in Canada detected neutrino oscillations — quantum mechanical mixing between the three types — which requires nonzero mass. The masses are tiny (less than an eV) but not zero. The mechanism for neutrino mass is still unsettled.

---

## Quarks and the Standard Model

By the early 1960s, accelerator experiments had discovered hundreds of particles: pions, kaons, lambdas, sigmas, omegas — a "particle zoo" that seemed to grow with every new accelerator. In 1963, Murray Gell-Mann (and independently George Zweig) proposed that all these hadrons are built from a small set of elementary constituents he called *quarks*.

The original three: up (u), down (d), and strange (s), with electric charges $+2/3, -1/3, -1/3$ in units of the proton charge. Fractional charges — never observed in isolation — demanded that quarks be permanently confined inside hadrons. By the early 1990s, six quark flavors had been established:

| Generation | Quark | Charge | Mass |
|---|---|---|---|
| 1 | up (u) | $+2/3$ | ~2 MeV/$c^2$ |
| 1 | down (d) | $-1/3$ | ~5 MeV/$c^2$ |
| 2 | charm (c) | $+2/3$ | ~1.3 GeV/$c^2$ |
| 2 | strange (s) | $-1/3$ | ~95 MeV/$c^2$ |
| 3 | top (t) | $+2/3$ | ~173 GeV/$c^2$ |
| 3 | bottom (b) | $-1/3$ | ~4.2 GeV/$c^2$ |

<!-- → [FIGURE: Standard Model particle table. Grid layout. Three columns for three generations. Top half: quarks (up-type row: u, c, t with charges +2/3; down-type row: d, s, b with charges -1/3). Bottom half: leptons (charged row: e, μ, τ; neutrino row: νe, νμ, ντ). Right column: force carriers (photon γ, gluons g×8, W⁺ W⁻ Z⁰, H Higgs). Masses labeled where known. Caption: The Standard Model particle content. Twelve matter fermions (6 quarks + 6 leptons) in three generations, 13 force carriers (photon + 8 gluons + W⁺W⁻Z⁰), and the Higgs boson. Every particle listed has been experimentally confirmed.] -->

**Hadrons** are particles built from quarks. *Baryons* contain three quarks (proton = uud, neutron = udd). *Mesons* contain one quark and one antiquark (pion $\pi^+ = u\bar{d}$). All the hundreds of particles in the 1960s zoo are simply different combinations of the six quarks, bound by the strong force.

Verify: the proton (uud) has charge $+2/3 + 2/3 - 1/3 = +1$. The neutron (udd) has charge $+2/3 - 1/3 - 1/3 = 0$. The $\pi^+$ has charge $+2/3 - (-1/3) = +1$. All correct.

**The proton's mass paradox.** The up quark has mass ~2 MeV/$c^2$ and the down quark ~5 MeV/$c^2$. The proton (uud) has mass 938 MeV/$c^2$. The sum of its three valence quarks is about 9 MeV/$c^2$ — barely 1% of the proton's mass. Where does the other 99% come from?

It comes from the energy of the strong force field holding the quarks together. By $E = mc^2$, this confinement energy is the proton's mass. Almost all the mass in your body — every atom, every nucleus — is not the mass of elementary particles. It is the energy stored in the strong nuclear field.

<!-- → [FIGURE: Proton mass composition diagram. Circle representing the proton. Inside: three small labeled circles (u, u, d) connected by wavy gluon lines. Bar chart alongside: total proton mass 938 MeV/c² shown as full bar. Subdivision: quark rest masses (~9 MeV/c², ~1% of bar, shaded dark), QCD field energy (~929 MeV/c², ~99% of bar, shaded light). Caption: The proton's mass is 938 MeV/c², but the sum of its three valence quark masses is only ~9 MeV/c². The remaining 99% is the energy of the strong-force field (QCD field energy) stored between the confined quarks. By E = mc², field energy contributes to mass. Most of your body mass is gluon field energy.] -->

**Beta decay at the quark level.** The "neutron decays to proton" process is really a down quark converting to an up quark. A $W^-$ boson is emitted and immediately decays to an electron and an antineutrino:

$$d \to u + W^-,\quad W^- \to e^- + \bar{\nu}_e.$$

Charge balance: $-1/3 \to +2/3 + (-1)$. Yes. The maximum electron kinetic energy is $m_n c^2 - m_p c^2 - m_e c^2 \approx 939.6 - 938.3 - 0.5 = 0.78$ MeV — which matches the observed beta-decay endpoint to within experimental precision.

---

## The Higgs and what the Standard Model doesn't explain

The Standard Model's three components together:

**Matter fermions** (spin-1/2): six quarks and six leptons in three generations. **Force-carrier bosons** (spin-1): the photon, eight gluons, and the $W^\pm, Z^0$. **The Higgs boson** (spin-0): the excitation of a scalar field that permeates all of space.

The Higgs field does something strange. Unlike all other fields in the Standard Model, it has a nonzero value in the vacuum — space is filled with it. Particles that interact strongly with this background field behave as if they have large masses; particles that don't interact with it (the photon, gluons) are massless. The Higgs *boson* is the quantum ripple in this background field, the oscillation you can excite when you collide protons at high enough energy. Finding it — at 125 GeV, at CERN in 2012 — confirmed that the mechanism is real.

![Three panels: photon (massless) glides through Higgs field unobstructed. Electron (light) drags slightly. Top quark (heaviest fermion) drags massively. Visualized as objects in a viscous fluid; "drag coefficient" = coupling...](../images/33-particle-physics-fig-04.png)
*Figure 33.4 — Higgs Mechanism — Mass Is Drag From the Higgs Field*

The Standard Model predicts this mechanism but does not predict *why* each particle has the coupling to the Higgs that it does. The top quark couples $3 \times 10^5$ times more strongly than the electron. Why? Unknown. These coupling strengths are free parameters, fitted from experiment. The Standard Model can accommodate whatever values are measured; it cannot predict them.

That gap is representative of the Standard Model's deeper problem. It contains roughly 19 free parameters — particle masses, mixing angles, coupling constants — whose values come from measurement rather than theory. The framework is exact; the numbers are inputs.

And there are phenomena the Standard Model simply cannot address at all:

**Gravity** has no place in the Standard Model. Attempts to quantize general relativity in the same way as electromagnetism fail — the resulting theory is non-renormalizable at high energies. We have two theories (quantum field theory and general relativity) that each work brilliantly in their domains and are mathematically incompatible.

**Dark matter** constitutes roughly 27% of the total energy content of the universe, inferred from galaxy rotation curves, gravitational lensing, and structure formation. The Standard Model has no candidate for it.

**Dark energy** constitutes roughly 68% of the universe's energy content and drives the accelerating expansion of the universe. The Standard Model cannot explain it.

**Matter-antimatter asymmetry** — the fact that we live in a universe dominated by matter — requires some process that produced slightly more baryons than antibaryons in the early universe. The Standard Model has CP violation (slight difference between matter and antimatter behavior in weak decays), but not enough by a factor of roughly $10^9$ to explain the observed asymmetry.

The Standard Model is not wrong. It is incomplete. Every experimental measurement within its domain agrees with its predictions. The failures are questions it doesn't address, not predictions that contradict measurement.

---

## The scale of this

Feynman used to say that if you wanted to summarize the most compressed form of physics knowledge to pass down through some disaster, you could do it in one sentence: "All things are made of atoms." The fact that there is a rule — that everything is made of the same small number of elements — is the deepest insight of 19th-century physics.

![Standard Model particle chart. Three generations of quarks (u/d, c/s, t/b) and leptons (e/νe, μ/νμ, τ/ντ). Four gauge bosons (γ, g, W, Z). Higgs (H) gives mass. All fundamental particles found in 17 boxes.](../images/33-particle-physics-fig-03.png)
*Figure 33.3 — Standard Model — 6 Quarks + 6 Leptons in 3 Generations + 4 Force Carriers + Higgs*

The Standard Model is the 20th-century extension of that idea. All things are made of six quarks and six leptons, interacting via four forces mediated by 13 bosons. The inventory is short. The consequences are everything.

Two protons in the LHC collide at 13 TeV. Hundreds of particles come out — pions, kaons, electrons, muons, photons. The Higgs boson appears rarely, in one collision in a billion, living for $10^{-22}$ seconds before decaying to two photons or two Z bosons. The ATLAS and CMS detectors, each containing $10^8$ sensors, record every track and every photon and reconstruct the event.

Every collision, every particle, every decay: the Standard Model predicts it. The agreement is not qualitative; it is precise. The $W$ boson mass: predicted 80.379 GeV, measured 80.379 ± 0.012 GeV. The $Z$ boson width: predicted 2.4952 GeV, measured 2.4952 ± 0.0023 GeV. The anomalous magnetic moment of the electron, the most precisely tested prediction in physics: theory and experiment agree to 13 significant figures.

We know what everything is made of. We don't know why. We don't know where mass values come from, what dark matter is, how gravity fits in, or why there is more matter than antimatter. These are not small gaps. Chapter 34 is about them.

---

## Exercises

### Warm-up

**33.1** *(LO 1)* List the four fundamental forces and rank them by relative strength at nuclear energies.

**33.2** *(LO 1)* The photon has mass 0; the $W$ boson has mass ~80 GeV/$c^2$. Use the uncertainty principle to estimate the range of each corresponding force.

**33.3** *(LO 2)* Antiparticle of (a) the electron, (b) the up quark, (c) the photon, (d) the neutron?

**33.4** *(LO 3)* List the six quark flavors. Quark content of the proton? The neutron? The $\pi^+$?

### Application

**33.5** *(LO 1)* Estimate the range of a force mediated by a particle of mass 50 GeV/$c^2$. Compare to the strong-force range mediated by the pion.

**33.6** *(LO 3)* Verify the charges of (a) proton (uud), (b) neutron (udd), (c) $\pi^+$ ($u\bar{d}$), (d) lambda baryon $\Lambda^0$ (uds).

**33.7** *(LO 4)* The LHC achieves 13 TeV center-of-mass energy. Express this (a) in joules, (b) as a mass in GeV/$c^2$, (c) as a multiple of the proton mass.

**33.8** *(LO 5)* Name one confirmed Standard Model prediction and one phenomenon it cannot explain.

### Synthesis

**33.9** *(LO 1, LO 3)* Write the quark-level reaction for beta-minus decay and verify charge conservation at each step.

**33.10** *(LO 2, LO 4)* Electron-positron annihilation at rest produces two photons. Compute the wavelength of each photon. Why must there be two?

**33.11** *(LO 1, LO 5)* Gravity is $10^{-38}$ times the strong force at the particle scale, yet gravity dominates the universe at large scales. Explain why. Similarly: the strong force is the strongest but is confined to nucleon scales. Explain why.

### Challenge

**33.12** *(beyond chapter)* The Higgs boson has a natural width of about 4 MeV. Using $\Delta E \Delta t \sim \hbar$, estimate its lifetime.

**33.13** *(beyond chapter)* The proton mass is 938 MeV/$c^2$. The sum of its three valence quark masses is ~9 MeV/$c^2$. Explain where the remaining 99% comes from in terms of QCD field energy and $E = mc^2$.

---

## LLM Exercise — Chapter 33: Particle Physics in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A Logbook entry connecting particle physics to your anchor phenomenon — often via cosmic-ray muons, the underlying quark/electron composition of matter, or medical/industrial particle technology.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste your 1-sentence description].

For Chapter 33, I want to apply particle physics — quarks, leptons, the Standard Model — to my phenomenon.

Please:

1. Identify ONE particle-physics aspect connected to my phenomenon. Examples: for a bike commute — cosmic-ray muons (the same ones from Chapter 28) generated by primary cosmic rays interacting with atmospheric nuclei; the LCD/OLED display in any smartphone or screen relies on electron transitions but the screens also rely on Standard Model particles all the way down; medical PET imaging if I've ever had one. For a coffee maker — every quark and electron in the coffee, the espresso machine's metal alloys, the specific isotopes any radioactive carbon (C-14) might have. For a basketball shot — every fundamental particle in the ball + my body + the air; cosmic-ray muons passing through the gym every second. For a marathon — cosmic-ray muon flux during the run (~1/cm²/min at sea level); the GPS watch uses Cesium atomic clocks.

2. Compute ONE quantitative quantity. Examples: the number of muons passing through a particular volume during a specific time; the energy carried by a typical proton in a hospital proton-therapy beam; the mass of the proton at quark level.

3. Specify input numbers and uncertainty.

4. Run the calculation. Report value with units.

5. One sentence on what would happen if the Standard Model were wrong — what specific failures would occur in technology I use.

6. One sentence connecting this to Chapter 34 (frontiers) — open questions and unsolved problems.

Save the output as logbook/chapter-33-particle.md.
```

### What this produces

A Logbook entry connecting your phenomenon to particle physics, often via cosmic-ray muons or via medical/industrial particle technology.

### How to adapt this prompt

- *For phenomena with no obvious particle-physics content:* Cosmic-ray muons or the underlying quark/electron composition of all matter is always available.
- *For ChatGPT/Gemini:* Identical with interface substitutions.

### Connection to previous chapters

Builds on Chapter 28 (relativistic kinematics for high-energy particles), Chapter 29 (uncertainty principle for virtual particles), Chapter 31 (nuclear physics, weak decay), and Chapter 32 (medical particle therapy).

### Preview of next chapter

Chapter 34 (frontiers) considers what the Standard Model leaves unexplained — dark matter, dark energy, quantum gravity, matter-antimatter asymmetry — and the frontier experiments and theories addressing these questions.

---

**Tags:** particle-physics, Standard-Model, quarks, Higgs-boson, fundamental-forces
