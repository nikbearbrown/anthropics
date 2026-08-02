# Chapter 10 — Capstone: From Geometric to Quantum Optics


## TL;DR

- Three levels of optics, three regimes of validity, and where the photon takes over.
- The chapter moves through Learning objectives, Opening case: a photon at a time, Core concept, The three levels of optics, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Three levels of optics, three regimes of validity, and where the photon takes over.*

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Understand)** State the three levels of optics — geometric, wave, quantum — and identify the regime in which each is the appropriate description.
2. **(Analyze)** Explain why the photoelectric effect cannot be accounted for by classical wave optics, and state Einstein's photon hypothesis $E = hf$.
3. **(Apply)** Compute photon-energy results for the photoelectric effect: threshold frequency, maximum kinetic energy of ejected electrons.
4. **(Understand)** Describe single-photon interference experiments (Tonomura, Grangier-Roger-Aspect) and the complementarity principle.
5. **(Understand)** Sketch the BB84 protocol for quantum key distribution.
6. **(Apply)** Build a single-photon double-slit simulator that builds up the interference pattern dot by dot.

---

## Opening case: a photon at a time

Lower the intensity of a double-slit experiment until photons arrive *one at a time* — so few that, on average, only one photon is in the apparatus at any moment. What do you observe?

Each photon makes a single dot on the screen. After a few photons, the screen looks like random scatter. After a few thousand, the pattern of dots starts looking like the interference pattern. After 50,000, it's the classical interference pattern in full clarity — *but composed entirely of discrete dots*.

This is one of the cleanest demonstrations of wave-particle duality. Each photon is a particle that lands at one place. The statistical distribution over many photons is wave-like. Neither classical picture is sufficient alone.

Akira Tonomura's group at Hitachi did this with electrons in 1989. The optical version with photons has been done many times; Grangier, Roger, and Aspect's 1986 experiment is the cleanest demonstration of single-photon character.

This chapter traces the boundary between classical optics (wave or ray) and quantum optics (photons). It is the capstone connecting everything you've learned in this book to the modern physics you'll encounter next.

---

## Core concept

### The three levels of optics

| Level | Description | Valid when | Examples |
|---|---|---|---|
| **Geometric optics** | Rays | $\lambda \ll$ all sizes | Cameras, telescopes (image formation) |
| **Wave optics** | Classical waves, superposition | Wave behavior matters, many photons | Interference, diffraction, polarization |
| **Quantum optics** | Photon field, probability amplitudes | Single-photon counting, anti-bunching | Photoelectric, single-photon double-slit, quantum cryptography |

Each level is the *appropriate-limit* description for its regime. Geometric optics is the high-$\lambda/\ell$ limit of wave optics. Wave optics is the *coherent-state, many-photon* limit of quantum optics. None of them is "more right" than the others; each works in its appropriate domain.

A textbook that says "light is *really* a wave (or *really* a particle)" misses the structural point. Light is a photon field; the classical wave is the many-photon coherent-state limit; the ray is the short-wavelength limit of the wave. The three levels are related by taking different limits.

### The photoelectric effect: classical wave optics breaks

Shine light on a clean metal surface; electrons emerge. Three experimental facts:

1. **Threshold frequency.** Below some frequency $f_0$, no electrons emerge — *regardless of intensity*. Above threshold, electrons emerge *immediately*, even at vanishingly low intensities.
2. **Frequency, not intensity, sets electron energy.** The maximum kinetic energy of ejected electrons is *linear in frequency*. Intensity controls the *count rate* of emerging electrons, not the energy per electron.
3. **Effectively instantaneous emission.** At any intensity above threshold, electrons emerge within $\sim 10^{-9}$ s of light arrival.

Classical wave optics predicts the opposite:
- Energy is in the field, so a brighter wave should deliver more energy.
- At low intensity, electrons should need time (minutes, even hours) to accumulate enough energy.
- There should be no frequency threshold — only an intensity threshold.

All three classical predictions fail. The experimental facts demand a different description.

**Einstein 1905:** Light arrives in *quanta* of energy
$$E_{\text{photon}} = hf$$
where $h = 6.626 \times 10^{-34}$ J·s. An electron absorbs one photon. If $hf > \phi$ (the metal's work function), the electron escapes with kinetic energy
$$K_{\max} = hf - \phi$$

Below $f_0 = \phi/h$: no ejection, no matter how bright. Above: intensity controls how many photons arrive per second and therefore how many electrons emerge per second.

The 1921 Nobel Prize went to Einstein for the photoelectric paper (not for relativity — that was still considered too speculative). Millikan, who spent years trying to *disprove* Einstein's photon hypothesis, ended up confirming $E = hf$ to 0.5% precision in 1916.

**Source:** Einstein, A. "Über einen die Erzeugung und Verwandlung des Lichtes betreffenden heuristischen Gesichtspunkt." Ann. Phys. 17, 132 (1905).

### Single-photon double-slit

Run an interference experiment so that, on average, only one photon is in the apparatus at a time. Each photon makes a discrete detection event on the screen. After many photons, the pattern of detections is the interference pattern from classical wave optics.

Each photon "interferes with itself" — but only in the *statistical* sense. There is no classical particle trajectory that explains it (a particle going through one slit wouldn't know about the other). There is no classical wave that explains it (the photon arrives as a point, not a smear).

**Akira Tonomura's group at Hitachi (1989)** did this with electrons. They recorded each detection and watched the interference pattern build up from dots. The optical version with photons has been done independently many times.

**Source:** Tonomura, A. et al. "Demonstration of single-electron buildup of an interference pattern." Am. J. Phys. 57, 117 (1989). Donati, O., Missiroli, G. F. & Pozzi, G. "An experiment on electron interference." Am. J. Phys. 41, 639 (1973). Optical analogues replicated many times since.

### The Grangier-Roger-Aspect anticoincidence experiment (1986)

The deepest demonstration that a single photon is a particle, not a wave. A single-photon source illuminates a 50/50 beam splitter. Two detectors monitor the two output ports.

Classical wave picture: an incoming wave splits into two waves, each at half amplitude. Both detectors should fire (in coincidence) at *quarter* the rate of the input.

Experiment: detectors fire *anticorrelated* — either one or the other, but never both for the same photon. The "wave" cannot have split. Each photon went to one detector or the other, with 50% probability each.

This is the cleanest classical-wave rejection. Single photons are particles in the sense that they are *indivisible* — they don't split between two detectors. But they exhibit *wave-like* statistical behavior in multi-photon ensembles.

**Source:** Grangier, P., Roger, G. & Aspect, A. "Experimental Evidence for a Photon Anticorrelation Effect on a Beam Splitter: A New Light on Single-Photon Interferences." Europhys. Lett. 1, 173 (1986).

### Complementarity

Niels Bohr's complementarity principle: a quantum system exhibits either wave-like *or* particle-like behavior, depending on the experimental setup. Both pictures are necessary; neither is sufficient alone.

For the double-slit:
- *No which-way information*: interference pattern visible. Wave description.
- *Full which-way information* (which slit each photon went through): no interference; you see a single-slit pattern. Particle description.
- *Partial which-way information*: partial interference. Fringe visibility is exactly complementary to certainty of which-way knowledge.

The which-way measurement *destroys the interference pattern*. Not because the apparatus is clumsy; because *the act of distinguishing slits changes the quantum state*. The deeper issue is that "which slit" and "interference" are *complementary* properties — gathering information about one necessarily disturbs the other.

### BB84 quantum key distribution

The BB84 protocol (Bennett & Brassard, 1984) uses single-photon polarization to share a secret cryptographic key between two parties (Alice and Bob).

Alice sends photons polarized in one of four states, choosing randomly from two bases:
- Basis 1: H (0°) or V (90°)
- Basis 2: D (45°) or A (135°)

Bob measures each photon in *one of the two bases at random*. After the transmission, Alice and Bob publicly compare which basis they used for each photon (but not the outcome). They keep only the photons where they happened to use the *same* basis. These bits form the shared key.

**Security argument.** Any eavesdropper Eve must measure the photons. But Eve doesn't know which basis Alice used. If Eve measures in the wrong basis, she destroys the photon's quantum state and introduces errors detectable by Alice and Bob. The no-cloning theorem of quantum mechanics prevents Eve from copying photons without disturbing them.

BB84 has commercial implementations. The 2017 Chinese Micius satellite demonstrated QKD over more than 1000 km in free space. Bandwidth is limited compared to classical cryptography, but the security guarantee is *information-theoretic* — based on physics, not computational complexity.

**Source:** Bennett, C. H. & Brassard, G. "Quantum cryptography: Public key distribution and coin tossing." Proc. IEEE Int. Conf. on Computers, Systems and Signal Processing, 175 (1984).

### Entangled photons and Bell tests

Two photons can be in an *entangled* state where measuring one instantly determines the result of measuring the other, regardless of distance. The polarization Bell state $|\Phi^+\rangle = (|HH\rangle + |VV\rangle)/\sqrt{2}$: measuring polarization on photon 1 collapses photon 2 into the matching polarization state.

This non-local correlation violates **Bell's inequality** — a bound that any classical local-hidden-variable theory must satisfy. Aspect, Grangier, Dalibard, and Roger demonstrated the violation experimentally in 1981–82. Three loophole-free experiments in 2015 closed remaining experimental issues. The **2022 Nobel Prize** to Aspect, Clauser, and Zeilinger sealed the case.

Bell inequality violations rule out local realism. The implications for the philosophy of physics are deep and contested; the experimental facts are settled.

### Photon statistics

The probability distribution of photon counts in a fixed time interval distinguishes light sources at the quantum level:
- **Coherent light** (laser): Poisson distribution. $\langle (\Delta n)^2 \rangle = \langle n \rangle$. $g^{(2)}(0) = 1$.
- **Thermal light** (Sun, light bulb): super-Poissonian. Photons are *bunched* — more likely to arrive together. $g^{(2)}(0) = 2$.
- **Single-photon source** (anti-bunched): $g^{(2)}(0) = 0$ in the limit. Used in QKD.

The second-order correlation function $g^{(2)}(0)$ distinguishes these regimes by measuring the probability of coincident detection. Modern quantum-optics experiments routinely measure $g^{(2)}(0)$ to characterize their light sources.

### The wave function and the optical amplitude

Quantum mechanics's wave function $\psi(\vec{r}, t)$ obeys the Schrödinger equation, which is structurally similar to the wave equation classical optics uses. The Born rule says $|\psi|^2$ is a probability density — exactly the way optical intensity $|E|^2$ governs detection probability for many photons.

The *form* of quantum mechanics — wave equation, superposition, probabilistic outcomes — was anticipated in optics. The crucial differences: $\psi$ is fundamentally complex; superposition is over states, not just fields; and measurement collapses the state. The Modern Physics volume of this series develops the full quantum theory.

---

## Worked example: photoelectric effect

Sodium has work function $\phi = 2.36$ eV [NIST clean-surface value]. (a) Find the threshold wavelength. (b) Illuminate with $\lambda = 400$ nm (violet). Find the maximum kinetic energy of ejected electrons and the stopping voltage.

**(a) Threshold wavelength.** $\lambda_0 = hc/\phi$. Use $hc = 1240$ eV·nm:
$$\lambda_0 = 1240/2.36 \approx 525 \text{ nm}$$

That's green light. Frequency: $f_0 = c/\lambda_0 = (3 \times 10^8)/(525 \times 10^{-9}) \approx 5.7 \times 10^{14}$ Hz.

**(b) Violet light at $\lambda = 400$ nm.** Photon energy:
$$hf = 1240/400 = 3.10 \text{ eV}$$

Maximum kinetic energy of ejected electrons:
$$K_{\max} = hf - \phi = 3.10 - 2.36 = 0.74 \text{ eV}$$

Stopping voltage: $V_s = K_{\max}/e = 0.74$ V. Apply $-0.74$ V to a collector facing the metal and the most energetic electrons just barely fail to reach it.

**The lesson.** Light at $hf < \phi$ (below threshold) produces no electrons regardless of how bright. Light at $hf > \phi$ produces electrons regardless of how dim. Both facts are quantum-mechanical, not classical.

**The limit.** This treats light as a stream of independent particles (photons) and ignores the wave description entirely. Modern QED resolves the wave-particle tension: light is the quantized excitation of the EM field. For most everyday optics, the classical wave picture is fine; for the photoelectric effect, the photon picture is required.

---

## Common misconceptions

**"Light is *really* a wave, or *really* a particle."** Both are partial descriptions, valid in different regimes. The deepest description is the quantized EM field of quantum electrodynamics; classical wave optics is the large-photon-number limit, and the particle picture applies for individual photon detections.

**"The photoelectric effect is the only thing that requires the photon."** It was the first experimental confirmation, but many other effects (Compton scattering, anti-bunching, single-photon interference) all require the photon picture. The photoelectric effect is the historical introduction; the deeper reason is field quantization in QED.

**"Entangled photons can transmit information faster than light."** No. The *correlation* between measurements is non-local; the *outcomes* themselves are random and cannot be controlled. Alice's measurement outcome is unpredictable; Bob sees random outcomes regardless of what Alice does. The no-signaling theorem of quantum mechanics is rigorous.

**"In the double-slit, the photon goes through both slits."** This phrasing is misleading. The photon is described by a wave function that has nonzero amplitude at both slits; the interference happens *between contributions from both slits*. "Going through both" is one classical attempt to capture this; the precise statement is that the photon's state is a superposition of the "through slit 1" and "through slit 2" possibilities.

**"You can copy a photon."** The no-cloning theorem (Wootters & Zurek, 1982) says you cannot. This is the foundation of quantum cryptography. Classical light, with millions of photons, can be "copied" in the sense of duplicating the beam at a beam splitter; individual quantum photon states cannot be cloned.

---

## Exercises

**Warm-up (Apply).** Copper has work function $\phi = 4.65$ eV. (a) Find the threshold wavelength. (b) Find the maximum kinetic energy of ejected electrons for incident UV light at $\lambda = 200$ nm.

**Apply.** A laser pointer at 633 nm emits 1 mW. (a) How many photons per second does it emit? (b) If you cut the power to 1 nW (a million-fold reduction), how many photons per second? Is this still "many photons per second" in the classical-limit sense?

**Apply.** A single-photon source at 800 nm emits one photon every 100 ns (10⁷ photons/second). Express the photon-arrival rate as an intensity flux at a 1 mm² detector. Is this a "weak" or "strong" beam by intuition?

**Apply + Analyze.** The photoelectric experiment with sodium ($\phi = 2.36$ eV). Plot the maximum kinetic energy $K_{\max}$ vs. frequency $f$ for $f > f_0$. What is the slope? What is the x-intercept (where $K_{\max} = 0$)? (Answer: slope = $h$; intercept = $f_0$.)

**Apply (BB84).** Alice sends 1000 photons in random polarizations. Bob measures each in a random basis. (a) On average, how many photons do Alice and Bob measure in the *same* basis? (b) These photons form the shared raw key. After classical error-correction and privacy-amplification, how many of these become the final secret key bits? (Hint: this is half the raw key; in practice losses are larger.)

**Challenge.** The Grangier-Roger-Aspect 1986 experiment. A single-photon source illuminates a 50/50 beam splitter; two detectors $D_1, D_2$ monitor the two outputs. Classical wave: amplitude splits, both detectors should fire with probability 1/4 each. Quantum: each photon goes to one detector or the other; the joint detection rate $R_{D_1 \cap D_2}$ should be near zero for genuine single photons. (a) Write the classical and quantum predictions for the ratio $R_{D_1 \cap D_2} / (R_{D_1} R_{D_2})$ — the *coincidence enhancement factor*. (b) Explain how this experiment distinguishes the two predictions.

---

## LLM Exercises

### Build the single-photon double-slit simulator (`10-single-photon-interference.html`)

> **Show.** Each photon is a discrete particle that lands at a single point. The statistical distribution over many photons is the classical wave interference pattern $I(y) = I_0 \cos^2(\pi d y/\lambda L)$.
>
> **Say.** Build a single-photon double-slit interference simulator with detection rate control.
>
> **Constrain.** D3 v7. Display the screen on the right of the canvas. Sliders for wavelength $\lambda$, slit separation $d$, screen distance $L$. The detection rate (photons/second) controls the speed at which photons arrive. Each photon arrival: draw a random $y$ position from the probability distribution $|\psi|^2 \propto \cos^2(\pi d y / \lambda L)$ (use inverse-CDF sampling). Render each detection as a single small dot on the screen at its $y$ position; let dots accumulate. Counter showing total photons detected. Filename: `10-single-photon-interference.html`.
>
> Optional: which-way mode toggle. When enabled, each photon is tagged with a slit (1 or 2 at random); the position is then drawn from the single-slit pattern (no interference). Watch the interference pattern *disappear* when which-way information is available.
>
> **Verify.** (a) At 100 photons: random-looking scatter. (b) At 10,000 photons: clear interference pattern. (c) The accumulated pattern matches the classical formula $I(y) \propto \cos^2(\pi d y / \lambda L)$.

### Exploration

- Run the simulation with detection rate = 100 photons/second. Watch the pattern build up dot by dot.
- Toggle which-way mode on. Watch the interference pattern disappear after enough dots accumulate.
- Predict what happens if you make $d$ very small (wide fringes) or very large (narrow fringes). Verify.

### Final-project options

Choose one of the three options below for your end-of-term project:

- **(A) Annotated simulation gallery.** Annotate all 10 chapter simulations with 100–200 words each on what you explored, what you observed, and what physics it taught you. Submit as a folder of HTML files plus an index README.
- **(B) Virtual optical instrument design.** Design a virtual optical instrument (spectrometer, interferometer, microscope) using the simulations from Chapters 4–9. Written report explaining design choices, resolution limits, and key trade-offs.
- **(C) Modern optics exploration.** Pick a modern optics application (adaptive optics, LIDAR, fiber optic communication, super-resolution microscopy, quantum cryptography) and connect it to the chapters of this book through a written report + simulation extension.

---

## What would change my mind

The three-level hierarchy of optics is the contemporary best understanding. Geometric optics is exact in the appropriate limit ($\lambda \to 0$); wave optics is exact in the classical-EM-field regime; quantum optics is required for single-photon phenomena.

The photoelectric effect's quantum interpretation has been overwhelmingly confirmed (Millikan 1916 and countless subsequent experiments). The single-photon double-slit experiment has been replicated since the 1970s with various particles (photons, electrons, neutrons, atoms, molecules). Bell inequality violations were sealed by the 2015 loophole-free experiments and the 2022 Nobel Prize.

What would change my mind: a confirmed deviation from the photon picture at single-photon level; a confirmed Bell-inequality experiment that *agrees* with local hidden-variable predictions; a violation of the no-cloning theorem. None of these has happened. Quantum mechanics is the most precisely tested theory in physics.

## Still puzzling

- *Interpretation of quantum mechanics.* The experimental facts are settled. What they "mean" (Copenhagen, Many-Worlds, Bohmian, QBism, etc.) is genuinely contested. See the QM companion guide in this series for fuller treatment.
- *Practical quantum advantage.* Quantum computing has demonstrated technical feats (50+ qubit machines, sampling problems beyond classical reach) but no decisively useful quantum advantage on practical problems as of 2026. The frontier is moving rapidly.
- *Photonic quantum computing.* Increasingly competitive with superconducting qubits. Xanadu's Borealis (2022) demonstrated quantum advantage on Gaussian Boson Sampling using photonic chips. PsiQuantum has commercial ambitions. The hardware physics is exactly the photonics this book teaches, applied at the quantum level.
- *Complementarity as foundational principle vs. computational shortcut.* Bohr argued complementarity was a *philosophical* principle of quantum mechanics. Modern interpretations (Many-Worlds, QBism) often replace it with more specific accounts of measurement. The operational content — which-way information vs. interference visibility — is uncontroversial.

---

**Tags:** photoelectric effect, photon, wave-particle duality, single-photon double slit, Grangier-Roger-Aspect, complementarity, Bell inequality, BB84, quantum key distribution, photon statistics

![Left: photoelectric apparatus. Light hits a metal cathode in a vacuum tube; ejected electrons travel to a collector anode. A variable stopping voltage measures the maximum kinetic energy of ejected electrons. Right: K...](images/10-capstone-quantum-optics-fig-01.png)
*Figure 10.1 — Photoelectric Effect*

![Four panels showing the same detector screen at increasing photon counts. N=10 photons: random scatter. N=100: still mostly random. N=1000: vertical bands of higher dot density begin to form. N=50000: clear interferen...](images/10-capstone-quantum-optics-fig-02.png)
*Figure 10.2 — Single-Photon Double-Slit Buildup*

![Top: experimental schematic. A heralded single-photon source sends a photon to a 50/50 beam splitter. Two detectors at the output ports. Bottom: histograms of coincidence rate. Classical wave prediction: photons shoul...](images/10-capstone-quantum-optics-fig-03.png)
*Figure 10.3 — Grangier-Roger-Aspect 1986*

![Three-row protocol diagram. Top: Alice randomly chooses a basis (rectilinear or diagonal) for each bit and encodes it as a polarized photon. Middle: photon travels through the quantum channel; Bob randomly chooses a b...](images/10-capstone-quantum-optics-fig-04.png)
*Figure 10.4 — BB84 Quantum Key Distribution*

![Three stacked time-series plots of photon arrival times as vertical ticks. Coherent laser: Poisson distribution, random independent arrivals, g²(0) = 1. Thermal source (Sun, light bulb): bunched arrivals, photons clus...](images/10-capstone-quantum-optics-fig-05.png)
*Figure 10.5 — Photon Statistics*

