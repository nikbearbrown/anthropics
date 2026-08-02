# Chapter 12 — Capstone: Light, Radiation, and the Unified Field

*Five threads connecting Maxwell to optics, antennas, the photoelectric effect, relativity, and wireless communication.*

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Apply)** Apply Snell's law to compute refraction angles and identify total internal reflection.
2. **(Apply)** Predict the fringe spacing in a two-slit interference experiment using $d\sin\theta = m\lambda$.
3. **(Understand)** Describe a dipole antenna's radiation pattern (sin²θ donut) and identify where intensity is maximum.
4. **(Analyze)** Explain why the photoelectric effect cannot be accounted for by classical EM and state Einstein's quantum hypothesis $E = hf$.
5. **(Understand)** State the historical motivation for special relativity: Maxwell's equations predict a unique $c$ in all reference frames.
6. **(Apply)** Build a two-slit interference simulator OR an antenna radiation pattern visualizer.

---

## Opening case: WiFi is Maxwell

Right now, in the room where you are reading this, there are probably between five and twenty radio-frequency signals propagating around you. WiFi at 2.4 GHz and 5 GHz. Cellular at 700 MHz to 5 GHz. FM radio at 88–108 MHz. AM at 530–1700 kHz. Bluetooth at 2.4 GHz. GPS at 1.5 GHz. They are all electromagnetic waves: oscillations of the electric and magnetic fields, propagating at the speed of light, governed by Maxwell's four equations.

Your phone has a small antenna that emits EM waves in a known frequency band when transmitting, and that responds to incoming EM waves by developing a small current that the receiver electronics decode. The whole apparatus — the antenna geometry, the modulation scheme, the path loss between phone and tower, the encoding of bits into RF — is engineering applied to one set of equations. The equations are the ones you finished deriving in Chapter 11.

This capstone does not introduce new fundamental physics. It uses Maxwell's equations to understand five threads of the world that the previous eleven chapters have prepared you for: optics, antennas, the photoelectric effect (where classical EM breaks down), the historical link from Maxwell to special relativity, and wireless communication.

By the end, you should be able to recognize Maxwell at work in the systems around you and explain why classical EM is *almost* the whole story — and where it has to hand off to quantum mechanics.

---

## Core concept

### Thread 1: Geometric optics from Maxwell

When the wavelength is much shorter than every feature of the system, EM waves behave *ray-like*. Two laws govern reflection and refraction at a boundary:

**Reflection.** Angle of incidence = angle of reflection, both measured from the normal.

**Refraction (Snell's law).** Light passing from medium 1 (refractive index $n_1$) to medium 2 ($n_2$):
$$n_1 \sin\theta_1 = n_2 \sin\theta_2$$

The refractive index $n = c/v = \sqrt{\kappa}$ for non-magnetic materials. Glass: $n \approx 1.5$. Water: 1.33. Diamond: 2.42. Vacuum: 1 (definition).

The wave's frequency stays fixed in any medium; its *speed* (and hence wavelength) drops to $v = c/n$ and $\lambda = \lambda_0/n$ inside the medium. The wavefront bends because the part of the wave in the denser medium moves slower.

**Total internal reflection** when going from dense to less-dense: above a critical angle $\theta_c$ where $\sin\theta_c = n_2/n_1$, the wave reflects entirely back. Glass-air: $\theta_c \approx 42°$. This is the principle of fiber-optic communication — light bounces along the fiber by total internal reflection, traveling kilometers with low loss.

### Thread 2: Wave optics — interference and diffraction

When wavelengths are comparable to features (slits, obstacles), wave behavior dominates.

**Two-slit interference** (Young 1801). Two coherent point sources separated by distance $d$ illuminate a screen at distance $L \gg d$. Bright fringes appear where the path-length difference is an integer wavelength:
$$d \sin\theta = m\lambda$$

Fringe spacing on the screen (small angle approximation): $\Delta y = \lambda L/d$. For green light ($\lambda = 500$ nm), $d = 0.1$ mm, $L = 1$ m: $\Delta y \approx 5$ mm. Visible to the naked eye.

Young's 1801 experiment was the decisive evidence that light is a wave. Maxwell explains *why*: superposing two plane-wave solutions of his linear wave equation gives interference, exactly as observed.

**Single-slit diffraction.** A single slit of width $a$ produces a diffraction pattern with first dark fringes at:
$$a \sin\theta = m\lambda \quad (m = \pm 1, \pm 2, ...)$$

**Rayleigh criterion** for resolving two point sources separated by angle $\theta$ with a circular aperture of diameter $D$:
$$\sin\theta_{\min} \approx 1.22 \lambda/D$$

For a 200 mm telescope at 500 nm: $\theta_{\min} \approx 3$ µrad — about 0.6 arcsec. This is why bigger telescopes resolve more detail; it's also why your eye (pupil ~3 mm) resolves about 1 arcmin.

### Thread 3: Antenna radiation

An oscillating charge or current radiates EM waves. The simplest model: a *dipole antenna*, two opposing currents oscillating sinusoidally.

**Larmor formula** (1897). A non-relativistic point charge with acceleration $a$ radiates total power:
$$P_{\text{rad}} = \frac{q^2 a^2}{6\pi\varepsilon_0 c^3}$$

Power $\propto a^2$. A charge moving at constant velocity does not radiate; an accelerating one does.

**Dipole radiation pattern.** A short dipole antenna oscillating along $\hat{z}$ has radiation intensity per solid angle:
$$\frac{dP}{d\Omega} \propto \sin^2\theta$$

where $\theta$ is the polar angle from the antenna axis. Maximum radiation at $\theta = 90°$ (perpendicular to the antenna); zero along the axis ($\theta = 0, 180°$). This "donut" pattern is why a vertical broadcast antenna radiates strongly toward the horizon and weakly straight up.

Phased arrays (multiple dipoles with controlled phase relationships) produce directional beams used in radar, cell-tower sectors, and beamforming for 5G.

### Thread 4: The photoelectric effect

Shine light on a clean metal surface; electrons emerge. Two experimental facts that classical EM cannot explain:

1. **Threshold frequency.** Below some frequency $f_0$, no electrons emerge at any intensity. Above $f_0$, electrons emerge immediately.
2. **Frequency, not intensity, sets electron energy.** The maximum kinetic energy of ejected electrons grows linearly with $f$, but is independent of intensity. Intensity controls *how many* electrons emerge, not how energetic each one is.

Classical EM predicts the opposite. A wave's energy is in the field; more intensity = more field energy = more electron energy. Threshold should depend on energy delivered (so on intensity × time), not on frequency.

**Einstein (1905).** Light arrives in *quanta* — photons — each carrying energy $E = hf$ where $h = 6.626 \times 10^{-34}$ J·s is Planck's constant. An electron absorbs one quantum. If $hf > \phi$ (the work function, an empirical property of the metal), the electron escapes with kinetic energy
$$K_{\max} = hf - \phi$$

Below the threshold $f_0 = \phi/h$, no ejection. The 1921 Nobel Prize was awarded to Einstein for this paper (not for relativity, which was still considered too speculative).

The photoelectric effect is where classical Maxwell breaks down. The deeper theory — quantum electrodynamics (QED) — recovers Maxwell in the classical limit and predicts the photon in the quantum limit. The chapter's job is to point to this boundary, not cross it.

### Thread 5: Maxwell to special relativity

Maxwell's equations have a hidden symmetry. They are **Lorentz-covariant** — invariant under the coordinate transformations Einstein would write down in 1905. Maxwell wrote his equations in 1865; the relativity was already there.

The physical issue: Maxwell's equations predict a unique speed $c$ for EM waves. *In what reference frame?* Galilean intuition (the inherited Newtonian relativity) says different observers in relative motion should see light at different speeds.

Michelson and Morley (1887), trying to measure Earth's motion relative to the supposed luminiferous ether, found *no difference* — Earth seemed to move at the same speed relative to the ether regardless of its orbital direction. The ether hypothesis collapsed.

**Einstein (1905, "On the Electrodynamics of Moving Bodies"):** drop Galilean relativity; keep Maxwell. The speed of light is the same in all inertial frames. Derive the consequences: time dilation, length contraction, $E = mc^2$.

The deepest consequence: $\vec{E}$ and $\vec{B}$ are not separate fields. They are components of a single antisymmetric tensor $F^{\mu\nu}$ in spacetime. Different observers in relative motion see different mixtures of $\vec{E}$ and $\vec{B}$ from the same physical situation. A current-carrying wire (only $\vec{B}$ in its rest frame) appears, to an observer moving along the wire, as a moving line of charges (with $\vec{E}$ and $\vec{B}$).

This unification was discovered before relativity itself; the framework just needed Einstein's 1905 reorganization to be recognized.

### Thread 6: Wireless communication

EM waves at radio and microwave frequencies are the substrate of every wireless system. Information rides on a **carrier wave** via modulation:
- **AM** (amplitude modulation): the carrier's amplitude varies with the signal.
- **FM** (frequency modulation): the carrier's frequency varies.
- **Digital** (BPSK, QAM, OFDM): both amplitude and phase encode bits.

WiFi (2.4 / 5 / 6 GHz), 5G (sub-6 GHz, mmWave 24–47 GHz), Bluetooth (2.4 GHz), GPS (~1.5 GHz), AM/FM radio (kHz–MHz), satellite TV (GHz) — all are Maxwell's equations engineered into protocols.

Practical example: a phone–tower link. Tower transmits at 5 W; antenna gain 10 dBi (factor 10); distance 1 km. Free-space path loss at 2 GHz: about $20 \log_{10}(4\pi r / \lambda) = 20\log_{10}(4\pi \cdot 1000/0.15) = 98$ dB. Received power: 5 W × 10 / 10^{9.8} ≈ $8 \times 10^{-9}$ W = 8 nW. A modern phone receiver detects signals down to about $10^{-13}$ W. Plenty of margin.

The whole calculation is Maxwell, engineered.

---

## Worked example: the photoelectric effect

Sodium has work function $\phi = 2.36$ eV. (a) Find the threshold frequency and wavelength. (b) Illuminate with 400 nm violet light. Find the maximum kinetic energy of ejected electrons and the stopping voltage needed to halt them.

**(a) Threshold frequency.** $f_0 = \phi/h$. Using $hc = 1240$ eV·nm:
$$\lambda_0 = hc/\phi = 1240/2.36 \approx 525 \text{ nm}$$
That's green light. Frequency: $f_0 = c/\lambda_0 = (3 \times 10^8)/(525 \times 10^{-9}) \approx 5.7 \times 10^{14}$ Hz.

**(b) Violet light, $\lambda = 400$ nm.** Photon energy:
$$hf = hc/\lambda = 1240/400 = 3.10 \text{ eV}$$
Maximum kinetic energy of ejected electrons:
$$K_{\max} = hf - \phi = 3.10 - 2.36 = 0.74 \text{ eV}$$
Stopping voltage: $V_s = K_{\max}/e = 0.74$ V. Apply $-0.74$ V to a collector facing the metal and the most energetic electrons just barely fail to reach it.

**The lesson.** Light at $hf < \phi$ (below threshold) produces no electrons regardless of how bright. Light at $hf > \phi$ produces electrons regardless of how dim — with kinetic energy set by $f$, not intensity. Both facts are quantum-mechanical, not classical.

**The limit.** This treats light as a stream of independent particles (photons) and ignores the wave description entirely. Modern QED resolves the wave-particle tension: light is the quantized excitation of the EM field. For most everyday optics, the classical wave picture is fine; for the photoelectric effect, the photon picture is required.

---

## Common misconceptions

**"Snell's law angles are measured from the surface."** No — from the *normal* to the surface. Easy to confuse.

**"In the photoelectric effect, intensity controls the energy per electron."** Backwards. Intensity controls the *number* of electrons emitted per second; frequency controls the *energy* per electron.

**"Relativity replaces Maxwell."** It doesn't. Maxwell's equations are *already relativistic* — they were Lorentz-covariant before Lorentz was born. Einstein's 1905 paper recognized this and reorganized mechanics to be compatible with Maxwell.

**"$E$ and $B$ are independent fields."** They are components of one electromagnetic field in spacetime. Different observers in different inertial frames see different mixtures. A pure-$\vec{B}$ field in one frame has $\vec{E}$ components in another.

**"WiFi is just radio waves."** WiFi *is* radio waves — EM waves in the microwave band. The engineering (modulation, antennas, MIMO arrays, error correction) is what makes the link useful. The physics is Maxwell's.

**"Photon energy is $hf$, so light intensity equals photon energy."** Intensity (W/m²) is photon energy × photon rate × ... carefully. Intensity has units of power per area; photon energy is per photon. The bridge is the *flux* of photons, not their energy individually.

---

## Exercises

**Warm-up (Apply).** Light at 600 nm enters water ($n = 1.33$) from air at 30° from the normal. Find the refraction angle and the wavelength in water.

**Apply.** Two-slit interference: slit separation $d = 50$ µm, screen distance $L = 2$ m, light $\lambda = 500$ nm. Find the fringe spacing. Predict the color you'd see if the wavelength were 700 nm instead.

**Apply.** Sodium work function 2.36 eV. (a) Threshold wavelength? (b) UV light at $\lambda = 200$ nm. Find $K_{\max}$. (c) The intensity doubles. Does $K_{\max}$ change? Does anything change?

**Apply + Analyze.** A vertical dipole antenna with radiation pattern $\propto \sin^2\theta$. (a) Sketch the radiation pattern in a vertical plane through the antenna. (b) Where is intensity maximum? (c) At what angle from the axis does the intensity drop to half its maximum?

**Apply (link budget).** A WiFi router transmits 100 mW (20 dBm). The path loss from router to a phone 10 m away (2.4 GHz) is about 60 dB. (a) What is the received power in dBm? (b) WiFi receivers can detect down to about –90 dBm. By how many dB does the received signal exceed the receiver sensitivity?

**Challenge.** Show that Maxwell's equations imply the same speed $c$ for EM waves in vacuum regardless of the observer's frame, *provided* the equations themselves transform correctly. (This is the historical motivation for Einstein's 1905 postulate.)

---

## LLM Exercises

### Build a two-slit interference visualizer (`12-two-slit-interference.html`)

> **Show.** Two coherent point sources separated by $d$, on a screen at distance $L$. Interference maxima at angles where $d\sin\theta = m\lambda$.
>
> **Say.** Build a two-slit interference simulator.
>
> **Constrain.** D3 v7. Animated 2D view: two slits on the left, screen on the right. Sliders for slit separation $d$ (10 µm to 1 mm), wavelength $\lambda$ (400 nm to 700 nm, color-mapped to visible spectrum), single-slit width $a$ (for the diffraction envelope), screen distance $L$. Wavefronts from each slit shown as expanding circles, animated. Intensity pattern on the screen as I(y); overlay the single-slit diffraction envelope $|\text{sinc}(\pi a \sin\theta/\lambda)|^2$. Filename: `12-two-slit-interference.html`.
>
> **Verify.** (a) Doubling $d$ halves the fringe spacing. (b) Doubling $\lambda$ doubles fringe spacing. (c) Increasing single-slit width $a$ narrows the diffraction envelope.

### Alternative: antenna radiation pattern (`12-antenna-pattern.html`)

> **Show.** Vertical dipole antenna with current oscillating along $\hat{z}$. Radiation pattern: intensity per solid angle $dP/d\Omega \propto \sin^2\theta$.
>
> **Say.** Build a radiation-pattern visualizer for a vertical dipole.
>
> **Constrain.** D3 v7. Polar plot of $\sin^2\theta$ in a vertical plane. Animated phase. Compass-style view: antenna at center, radiation lobes extending outward. Filename: `12-antenna-pattern.html`.
>
> **Verify.** Pattern is donut-shaped: maximum perpendicular to the antenna axis, zero along the axis.

### Final project options

Choose one of:
- **(A)** Annotated simulation gallery for all 12 chapters. Each simulation accompanied by 100–200 words on what you changed and what you observed. Submit as a folder of HTML files plus a single README.
- **(B)** Simulation of an E&M application from your intended field (electrical engineering, medical physics, materials science, etc.). Must use the +1 simulation stack. Written explanation: how does this connect to Maxwell's equations?
- **(C)** Simulation-based numerical verification of one of Maxwell's equations for a specific configuration. Pick a configuration where you can compute both sides (e.g., Gauss's law for a particular charge distribution); show numerically that they match.

---

## What would change my mind

The threads in this chapter rest on twelve chapters of foundation. If any of them turned out to be wrong, the chapter would change. The photoelectric effect's quantum interpretation has been overwhelmingly confirmed by Millikan (1916), single-photon double-slit experiments (post-2000), and ongoing QED measurements. The Maxwell-relativity covariance has been the basis of all relativistic physics since 1905. Wireless engineering is a $10^{12}$-dollar industry built on Maxwell; if the physics were wrong, the industry would have noticed.

What *would* change my mind: a confirmed deviation from Maxwell's equations at any tested scale, or a confirmed alternative to quantum mechanics that doesn't recover the photoelectric effect. Neither has happened in 130+ years.

## Still puzzling

- *Why is the speed of light invariant?* Special relativity is built on the empirical fact, not a deeper derivation. Why nature chose $c$ as a universal speed limit is unresolved.
- *Are there phenomena at energies beyond known particle physics where Maxwell needs corrections?* In quantum field theory, $\vec{E}$ and $\vec{B}$ emerge from a U(1) gauge theory. Grand unified theories link this gauge structure to other forces. At very high energies, Maxwell may not be the whole story. We don't know yet.
- *The light-as-wave vs. light-as-particle tension.* Resolved at QED's level; conceptually still strange. The photoelectric effect requires the photon picture; double-slit interference requires the wave picture. Both pictures are correct in their domain; QED reconciles them.

---

**Tags:** Snell's law, interference, diffraction, antenna, Larmor, photoelectric effect, Einstein, special relativity, wireless, photon

