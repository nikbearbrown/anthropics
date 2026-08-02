# Chapter 12 — Capstone: Light, Radiation, and the Unified Field

*Five threads connecting Maxwell to optics, antennas, the photoelectric effect, relativity, and wireless communication.*

---

Right now, in the room where you are reading this, there are between five and twenty electromagnetic fields propagating through you.

WiFi at 2.4 GHz and 5 GHz. Cellular at 700 MHz to 5 GHz. FM radio at 88–108 MHz. AM at 530–1700 kHz. Bluetooth at 2.4 GHz. GPS at 1.5 GHz. They are passing through the walls, through the air, through your body, at the speed of light. You cannot feel them. They have been there, more or less, since the 1880s when Hertz first detected the radio waves Maxwell had predicted.

Every one of those signals is a solution to four equations — Maxwell's equations, which you finished deriving in Chapter 11. The antenna in your phone is designed using those equations. The path loss from tower to handset is calculated from those equations. The modulation scheme encodes bits onto those waves using properties of those equations. The whole apparatus is engineering applied to one set of differential equations.

This capstone does not introduce new fundamental physics. It uses what you have to follow five threads outward: into optics, into antenna design, into the place where classical Maxwell breaks down at the quantum level, into the historical link from Maxwell to Einstein's special relativity, and back into the wireless world around you. By the end of the chapter, you should be able to look at any electromagnetic system — a fiber-optic cable, a telescope, a phone call, an X-ray — and recognize Maxwell at work.

---

## Thread one: geometric optics

When the wavelength is much shorter than every feature of a system — every lens, mirror, slit, aperture — electromagnetic waves behave like rays. The wave nature is still there, but it only matters when dimensions approach the wavelength. For most of everyday optics, rays are an excellent description.

Two laws govern what happens at a boundary between two media.

**Reflection.** The angle of incidence equals the angle of reflection. Both measured from the *normal* to the surface, not from the surface itself — the single most common error in this material.

**Refraction** (Snell's law). Light crossing from medium 1 to medium 2:

$$n_1\sin\theta_1 = n_2\sin\theta_2$$

The refractive index $n = c/v$ — the ratio of $c$ to the wave's speed in that medium. Vacuum: $n = 1$. Water: 1.33. Glass: approximately 1.5. Diamond: 2.42. The higher the index, the slower the wave and the more steeply it bends toward the normal when entering.

The wave's *frequency* does not change at a boundary. What changes is the speed, and therefore the wavelength: $\lambda = \lambda_0/n$ inside a medium. The wavefront bends because one part of it enters the denser medium and slows down before the rest of the wavefront does — it pivots, like a line of marching soldiers stepping into mud on one end.

![Snell's law diagram — a ray crossing from medium n₁ (above) to medium n₂ > n₁ (below), with the normal perpendicular to the boundary, angles θ₁ and θ₂ labeled from the normal, showing the ray bending toward the normal...](../images/12-capstone-unified-field-fig-01.png)
*Figure 12.1 — Snell's Law and Total Internal Reflection*

<!-- → [IMAGE: Snell's law diagram — a ray crossing from medium n₁ (above) to medium n₂ > n₁ (below), with the normal perpendicular to the boundary, angles θ₁ and θ₂ labeled from the normal, showing the ray bending toward the normal in the denser medium — plus a second diagram showing total internal reflection when the ray exceeds the critical angle going from dense to less dense] -->

**Total internal reflection.** Going from a denser medium to a less dense one — glass to air, water to air — there is a critical angle $\theta_c$ where $\sin\theta_c = n_2/n_1$. At angles larger than $\theta_c$, no transmitted ray exists; the wave reflects entirely back. For glass-air, $\theta_c \approx 42°$. This is fiber-optic communication: a light pulse enters a glass fiber and bounces along it by total internal reflection for kilometers, with losses measured in dB/km rather than the catastrophic losses of free-space propagation at optical frequencies.

---

## Thread two: wave optics and interference

When wavelengths are comparable to the geometry — slits, apertures, gratings — the ray picture breaks down and wave phenomena appear. The most important is interference.

**Young's two-slit experiment, 1801.** Two slits, separated by distance $d$, illuminated by coherent monochromatic light. On a screen at distance $L$, bright fringes appear wherever waves from the two slits arrive with a path-length difference that is an integer multiple of the wavelength:

$$d\sin\theta = m\lambda$$

Fringe spacing on the screen: $\Delta y = \lambda L/d$. For green light ($\lambda = 500$ nm), 0.1 mm slit separation, 1 m to the screen: $\Delta y \approx 5$ mm. Visible to the naked eye.

![two-slit interference diagram — two slits separated by d, screen at distance L, path-length difference from the two slits shown for the first bright fringe (m = 1), the interference pattern on the screen showing alter...](../images/12-capstone-unified-field-fig-02.png)
*Figure 12.2 — Two-Slit Interference Modulated by Diffraction Envelope*

<!-- → [IMAGE: two-slit interference diagram — two slits separated by d, screen at distance L, path-length difference from the two slits shown for the first bright fringe (m = 1), the interference pattern on the screen showing alternating bright and dark fringes — with fringe spacing Δy = λL/d labeled] -->

Young's experiment was the decisive evidence that light is a wave. It resolved a century-long debate between Newton (who favored particles) and Huygens (who favored waves). The experiment produced the characteristic interference fringes that are simply not possible if light were a stream of independent particles — they require that the "something" passing through both slits simultaneously can add constructively in some places and cancel in others.

Maxwell explains *why*: his linear wave equation allows solutions to be superposed, and the superposition of two plane waves of the same frequency and phase produces exactly the interference pattern Young observed. The calculation is the same calculation we did in any wave context, applied to the electric field.

The single-slit diffraction pattern limits how bright the fringes can be as a function of angle — the diffraction envelope $|\text{sinc}(\pi a\sin\theta/\lambda)|^2$ modulates the interference. And the **Rayleigh criterion** for angular resolution of a circular aperture of diameter $D$:

$$\theta_{\min} \approx \frac{1.22\lambda}{D}$$

This is why telescopes need to be large. A 200 mm telescope at 500 nm has $\theta_{\min} \approx 3$ µrad — about 0.6 arcseconds. The human eye (pupil $\approx 3$ mm) resolves about 1 arcminute. It's not a failure of design; it's a consequence of diffraction, set by $\lambda/D$.

![Rayleigh criterion visualization — two point sources at increasing angular separation shown through a circular aperture: (1) unresolved — single merged blob; (2) just resolved — Rayleigh limit, first minimum of one Ai...](../images/12-capstone-unified-field-fig-03.png)
*Figure 12.3 — Dipole Antenna Pattern*

<!-- → [IMAGE: Rayleigh criterion visualization — two point sources at increasing angular separation shown through a circular aperture: (1) unresolved — single merged blob; (2) just resolved — Rayleigh limit, first minimum of one Airy disk on center of other; (3) clearly resolved — two distinct Airy disks — with the criterion θ_min = 1.22λ/D labeled at the transition] -->

---

## Thread three: antennas and radiation

An accelerating charge radiates electromagnetic energy. This is the source of all electromagnetic waves: the electrons in an antenna are driven by an AC current into oscillating motion; their acceleration produces an outward-propagating EM wave.

The **Larmor formula** gives the total radiated power from a non-relativistic charge of magnitude $q$ with acceleration $a$:

$$P_{\text{rad}} = \frac{q^2 a^2}{6\pi\varepsilon_0 c^3}$$

Notice: power goes as $a^2$. A charge moving at constant velocity does not radiate — no acceleration, no radiation. This is consistent with the electrostatics and magnetostatics of previous chapters, where steady configurations produce static fields, not waves. Radiation requires *change*, in the same sense that Faraday's law required a *changing* flux to produce an EMF.

The simplest radiating structure is the **dipole antenna** — two conductors carrying oscillating currents in opposite directions along $\hat{z}$. The radiation pattern (power per unit solid angle as a function of direction) is:

$$\frac{dP}{d\Omega} \propto \sin^2\theta$$

where $\theta$ is the polar angle measured from the antenna axis. This is a **donut shape**: maximum radiation in the plane perpendicular to the antenna ($\theta = 90°$), zero along the axis ($\theta = 0°$ and $180°$). A vertical broadcast antenna radiates strongly toward the horizon and not at all straight up or straight down.

![dipole radiation pattern — antenna shown as a vertical line, the sin²θ donut pattern shown as a 3D toroidal shape around it, with the equatorial maximum labeled and the zero on the axis labeled — also a cross-sectiona...](../images/12-capstone-unified-field-fig-04.png)
*Figure 12.4 — Photoelectric Effect*

<!-- → [IMAGE: dipole radiation pattern — antenna shown as a vertical line, the sin²θ donut pattern shown as a 3D toroidal shape around it, with the equatorial maximum labeled and the zero on the axis labeled — also a cross-sectional polar plot in a vertical plane showing the figure-eight shape] -->

Phased arrays control the direction of radiation by adjusting the phase of the signal fed to each element: constructive interference in the desired direction, destructive everywhere else. 5G base stations use phased arrays to focus beams toward individual user devices — "beamforming" — rather than broadcasting uniformly in all directions. The physics is exactly Young's two-slit interference, applied to antenna elements.

![phased array beamforming diagram — four antenna elements in a row, each fed with a slightly different phase delay shown as shifting sinusoidal signals; the resulting constructive interference lobe shown pointing at an...](../images/12-capstone-unified-field-fig-05.png)
*Figure 12.5 — Maxwell to Relativity*

<!-- → [IMAGE: phased array beamforming diagram — four antenna elements in a row, each fed with a slightly different phase delay shown as shifting sinusoidal signals; the resulting constructive interference lobe shown pointing at angle θ away from broadside — contrasted with a single antenna broadcasting equally in all directions, to show the gain from phasing] -->

---

## Thread four: where Maxwell breaks down

In 1887, Heinrich Hertz confirmed Maxwell's prediction of radio waves — a triumph of the theory. In the same experimental setup, he also observed something odd: ultraviolet light falling on a metal surface made it easier to produce sparks. He noted the effect and moved on.

Eleven years later, Philipp Lenard investigated it carefully. He found that light shining on a clean metal surface could eject electrons. Two facts emerged that made no sense with classical electromagnetic wave theory.

**First: there is a threshold frequency.** Below some frequency $f_0$, no electrons are emitted no matter how bright the light. Above $f_0$, electrons come out immediately, even in very dim light.

**Second: frequency, not intensity, sets how energetic the electrons are.** The maximum kinetic energy of ejected electrons grows linearly with frequency. Intensity — the wave amplitude squared — controls how *many* electrons come out, but not how energetic each one is.

Classical electromagnetic theory predicts the opposite behavior. A wave's energy is distributed continuously across its field. More intensity means more energy per unit area per unit time delivered to the surface. Given enough time, or enough intensity, any electron should eventually accumulate enough energy to escape, regardless of frequency. There should be no threshold. And more intensity should produce more energetic electrons.

The data said otherwise.

**Einstein's 1905 explanation.** Light comes in discrete quanta — what we now call photons. Each photon carries energy:

$$E = hf$$

where $h = 6.626 \times 10^{-34}$ J·s is Planck's constant. Each ejected electron absorbs exactly one photon. If the photon's energy exceeds the metal's **work function** $\phi$ — the minimum energy needed to pull an electron free — the electron escapes with kinetic energy:

$$K_{\max} = hf - \phi$$

If $hf < \phi$, no ejection, regardless of intensity. The threshold frequency is $f_0 = \phi/h$.

![photoelectric effect diagram — left: low-frequency light (hf < φ) hitting a metal surface, no electrons ejected; right: high-frequency light (hf > φ) hitting the same surface, electrons ejected with kinetic energy K =...](../images/12-capstone-unified-field-fig-06.png)
*Figure 12.6 — Wireless Link Budget*

<!-- → [IMAGE: photoelectric effect diagram — left: low-frequency light (hf < φ) hitting a metal surface, no electrons ejected; right: high-frequency light (hf > φ) hitting the same surface, electrons ejected with kinetic energy K = hf − φ — with the work function φ shown as a potential barrier the electron must climb — bottom panel: graph of K_max vs. frequency showing a straight line with slope h and x-intercept f₀ = φ/h] -->

This is not a modification of Maxwell's equations. It is a place where they genuinely fail — where the continuous-wave description of light is inadequate and the photon description is required. The 1921 Nobel Prize went to Einstein for this paper. (Not for relativity, which the Nobel committee considered too theoretical.)

The resolution lives in quantum electrodynamics: light is the quantized excitation of the electromagnetic field. For most phenomena — propagation, reflection, refraction, interference — the classical Maxwell description is excellent. For the photoelectric effect, Compton scattering, and the emission and absorption of light by atoms, the photon picture is required. Both pictures are correct in their domains. The tension between them is not a contradiction; it is the empirical fact that drove the development of quantum mechanics.

---

## Thread five: Maxwell to Einstein

Here is something remarkable about Maxwell's equations: they were already relativistic in 1865, forty years before Einstein.

Maxwell's equations predict a unique speed for electromagnetic waves in vacuum:

$$c = \frac{1}{\sqrt{\mu_0\varepsilon_0}}$$

The constants $\mu_0$ and $\varepsilon_0$ were measured from static electric and magnetic experiments. They give $c = 3 \times 10^8$ m/s — the measured speed of light. But the equations say nothing about *which reference frame* this speed is measured in. This was deeply disturbing to 19th-century physicists, because Galilean relativity — the Newtonian rule for adding velocities — said that if light travels at $c$ in one frame, it should travel at $c + v$ or $c - v$ in a frame moving at $v$. But Maxwell's equations had no preferred frame.

Michelson and Morley's 1887 experiment tried to measure Earth's velocity through the hypothetical "luminiferous ether" — the medium light was supposed to wave in. They split a light beam, sent the halves in two perpendicular directions, and looked for an interference shift as Earth moved through the ether in different directions at different times of year. The shift should have been detectable. They found nothing.

The ether hypothesis failed. Light apparently traveled at the same speed regardless of the observer's motion.

**Einstein's 1905 step.** He took Maxwell's equations seriously and followed the logic. If Maxwell's equations are the correct description of light, and if they predict a unique $c$, then $c$ is the same in all inertial frames. Period. Drop the ether. Drop Galilean velocity addition. Accept the consequences and derive them carefully.

The consequences: time dilation, length contraction, the relativity of simultaneity, mass-energy equivalence $E = mc^2$. The whole structure of special relativity falls out of taking Maxwell's equations at face value.

The deepest consequence for electromagnetism itself: $\vec{E}$ and $\vec{B}$ are not independent fields. They are components of a single **electromagnetic field tensor** $F^{\mu\nu}$ in four-dimensional spacetime. What one observer calls a pure magnetic field, a different observer moving relative to the first will see as a mixture of electric and magnetic fields. A current-carrying wire — which in its rest frame produces only a magnetic field — will appear, to an observer moving along the wire, as a line of charges whose Lorentz contraction creates a net charge density, producing an electric field. The two observers are seeing the same physical situation through different coordinate systems.

This was implicit in Maxwell's 1865 equations. It took Einstein to make it explicit.

<!-- → [INFOGRAPHIC: two reference frames for a current-carrying wire — left frame (wire at rest): wire is electrically neutral, B field shown circling the wire, no E field; right frame (observer moving along wire): Lorentz contraction makes the electron spacing slightly different from the ion spacing, net charge density appears, E field shown radiating outward — same physics, different decomposition into E and B] -->

---

## Thread six: wireless

Everything in the previous five threads converges in a wireless link.

A phone transmitting a call accelerates electrons in its antenna (Thread three) at roughly 2.4 GHz. Those accelerating electrons radiate EM waves (Maxwell, Larmor). The waves propagate at $c$ (Thread five, the invariant speed). They arrive at a receiving antenna and accelerate electrons there, producing an induced current (Chapter 10, Faraday). The electronics decode the signal from that current.

The link budget is a calculation that tracks the power from transmitter to receiver using Maxwell's equations all the way through. Start with the transmitter power. Apply the antenna gain — the directional enhancement from shaping the radiation pattern (Thread three). Calculate the spreading loss as the wave expands through space — intensity falls as $1/r^2$ because the same power spreads over a sphere of area $4\pi r^2$. Apply any atmospheric or obstruction losses. What arrives at the receiving antenna is typically nanowatts or less; modern receivers detect signals down to $10^{-13}$ W.

At 2.4 GHz over 1 km in free space, the path loss is about 98 dB — the received power is a factor of $10^{9.8}$ smaller than the transmitted power. A 5 W transmitter with a 10 dBi antenna (factor-10 directional gain) delivers about 8 nW to a receiver 1 km away. A phone's receiver sensitivity is around $10^{-13}$ W = 0.1 pW. The margin is comfortable: the received signal is roughly $10^4$ times the minimum detectable level.

The whole calculation is engineering applied to Maxwell's equations. The distance scaling, the antenna pattern, the frequency dependence of path loss — all derivable from the Poynting vector $\vec{S} = \frac{1}{\mu_0}\vec{E}\times\vec{B}$ and the radiation pattern of the antenna.

<!-- → [CHART: link budget waterfall diagram — starting bar at transmitted power (e.g. 37 dBm = 5 W), adding antenna gain (+10 dBi), subtracting free-space path loss (−98 dB at 1 km, 2.4 GHz), showing received power (about −51 dBm = 8 nW), with receiver sensitivity floor (−103 dBm) shown as a horizontal line and the link margin labeled as the gap — makes the dB arithmetic visual and shows why the link works] -->

---

## The worked numbers: photoelectric effect on sodium

Sodium has work function $\phi = 2.36$ eV. Illuminate it with 400 nm violet light.

**Threshold.** Using the convenient conversion $hc = 1240$ eV·nm, the threshold wavelength is:

$$\lambda_0 = \frac{hc}{\phi} = \frac{1240}{2.36} \approx 525 \text{ nm}$$

That's green light. Sodium's threshold is in the visible — longer wavelengths (red, orange, yellow) produce no electrons; shorter ones (green, blue, violet) do.

**Violet light at 400 nm.** Photon energy:

$$hf = \frac{hc}{\lambda} = \frac{1240}{400} = 3.10 \text{ eV}$$

Maximum kinetic energy of ejected electrons:

$$K_{\max} = hf - \phi = 3.10 - 2.36 = 0.74 \text{ eV}$$

**Stopping voltage.** Apply $-0.74$ V to a collector facing the sodium surface and the most energetic electrons just barely fail to reach it. That voltage directly measures $K_{\max}/e$.

**What happens if you double the intensity?** Twice as many photons arrive per second. Twice as many electrons are ejected. $K_{\max}$ is unchanged — it depends only on $hf$, not on how many photons there are. This is the anti-intuitive heart of the photoelectric effect: the energy budget per event is set by frequency, not by brightness.

---

## What all five threads have in common

There is a single conceptual thread running through all five.

In Chapter 2, we learned that charges produce electric fields. In Chapter 8, that moving charges produce magnetic forces. In Chapter 9, that currents produce magnetic fields. In Chapter 10, that changing magnetic fields produce electric fields. In Chapter 11, that Maxwell closed the loop: changing electric fields also produce magnetic fields, and together the two sustain each other as propagating waves at speed $c$.

Everything in this capstone is consequence.

Optics follows from the wave nature of Maxwell's solutions, specialized to the short-wavelength limit. Interference follows from the linearity of Maxwell's equations — solutions superpose. Radiation follows from the fact that accelerating charges produce waves that carry energy away from the source. The photoelectric effect marks the boundary where Maxwell's classical description must be extended to quantum mechanics — where the discreteness of the photon becomes unavoidable. And special relativity is what you get when you take Maxwell's equations seriously in all inertial frames and demand consistency.

The five threads are not separate subjects. They are five views of the same underlying structure.

---

## The thing that is still not understood

Light is simultaneously a wave and a particle. That sentence was not understood in 1905 and it is still, in some sense, not understood today — not because we lack the mathematics (quantum field theory handles it), but because no one has a satisfying physical picture that is simpler than the mathematics.

In a double-slit experiment, a single photon produces an interference fringe. But a photon is supposed to be a particle — a localized quantum of energy. How does a single particle "know" about both slits? The answer, formally, is that we track probability amplitudes rather than classical trajectories, and amplitudes interfere even when the corresponding probabilities would not. That is QED's answer, and it is correct in the sense of producing predictions that match every experiment ever done.

Whether it is a satisfying *explanation* is a question physicists have argued about since 1927 and have not resolved. Feynman himself said, repeatedly, that nobody really understands quantum mechanics — that we only know how to calculate with it. That is not false modesty. It is an accurate description of where the subject stands.

Maxwell took us to the edge. Quantum mechanics is the jump beyond. The book ends here.

---

## Exercises

**Warm-up.** Light at $\lambda = 600$ nm travels in air and strikes a water surface ($n = 1.33$) at an angle of incidence of 30° from the normal. (a) Find the refraction angle in water using Snell's law. (b) Find the wavelength of the light *inside* the water. (c) Does the frequency change? Explain in one sentence why or why not. *Tests: Snell's law, wavelength in a medium, frequency invariance.*

**Warm-up.** A two-slit setup has slit separation $d = 50$ µm and a screen at distance $L = 2$ m. Illuminated with green light at $\lambda = 500$ nm: (a) find the fringe spacing $\Delta y$; (b) predict how $\Delta y$ changes if $d$ is doubled; (c) predict how $\Delta y$ changes if $\lambda$ is changed to red light at 700 nm. *Tests: two-slit fringe spacing formula, parameter scaling.*

**Warm-up.** Sodium's work function is $\phi = 2.36$ eV. (a) Find the threshold wavelength $\lambda_0$. (b) Illuminate with UV at $\lambda = 200$ nm; find $K_\text{max}$ in eV. (c) The intensity is now doubled at the same 200 nm wavelength. What happens to $K_\text{max}$? What happens to the number of electrons ejected per second? (d) Now switch to infrared at $\lambda = 1000$ nm at very high intensity. Do any electrons emerge? *Tests: photoelectric threshold, $K_\text{max} = hf - \phi$, intensity vs. frequency distinction.*

**Application.** A glass fiber has core refractive index $n_1 = 1.50$ and cladding index $n_2 = 1.46$. (a) Find the critical angle $\theta_c$ for total internal reflection at the core-cladding interface. (b) A light ray enters the fiber end-face and hits the core-cladding interface at 82°. Does it undergo total internal reflection? (c) A ray at 70° — does it? (d) Explain in one sentence why fiber-optic cables must keep bend radii above a minimum value. *Tests: critical angle formula, comparison to threshold, physical reasoning about bend losses.*

**Application.** A vertical dipole antenna has radiation pattern $dP/d\Omega \propto \sin^2\theta$. (a) At what angle $\theta$ from the antenna axis is the radiated intensity maximum? (b) At what angle does it fall to half the maximum? (c) A broadcast station wants to cover listeners on the ground, not satellites overhead. Should the antenna be vertical or horizontal? Justify using the radiation pattern. (d) If a second identical antenna is placed parallel to the first, separated by $\lambda/2$, and driven 180° out of phase, qualitatively describe how the combined pattern changes compared to a single antenna. *Tests: reading the radiation pattern, zero-intensity axis, phased array intuition.*

**Application.** A WiFi router transmits 100 mW at 2.4 GHz. The free-space path loss to a laptop 10 m away is approximately 60 dB. (a) What is the received power in milliwatts? In dBm (where 0 dBm = 1 mW)? (b) If the router's antenna has a gain of 3 dBi (factor ~2 directional enhancement), what is the effective transmitted power? (c) WiFi receivers detect down to about −90 dBm. How much margin (in dB) does the received signal have above the sensitivity floor? (d) If the distance doubles to 20 m, by how many dB does the received power drop, and why? *Tests: dB arithmetic, free-space path loss, $1/r^2$ spreading.*

**Synthesis.** The Larmor formula says $P_\text{rad} \propto q^2 a^2$. (a) A charge oscillates sinusoidally: $x(t) = x_0\cos(\omega t)$. Find its acceleration as a function of time. (b) Find the time-averaged radiated power $\langle P_\text{rad}\rangle$ in terms of $q$, $x_0$, $\omega$, and physical constants. (c) Show that $\langle P_\text{rad}\rangle \propto \omega^4$ — radiated power grows as the fourth power of frequency. (d) This $\omega^4$ dependence is also responsible for Rayleigh scattering, the reason the sky is blue. Blue light ($\lambda \approx 450$ nm) scatters roughly how many times more strongly than red light ($\lambda \approx 700$ nm) as it passes through the atmosphere? *Tests: kinematics of oscillation, time-averaging, frequency scaling, application to natural phenomenon.*

**Synthesis.** A Michelson interferometer splits a light beam into two perpendicular arms of length $L$ each, reflects both back, and recombines them. If the apparatus moves at velocity $v$ relative to the ether, classical physics predicts a round-trip time difference of $\Delta t \approx Lv^2/c^3$ between the two arms. (a) For $L = 11$ m (the Michelson-Morley setup), Earth's orbital velocity $v \approx 3 \times 10^4$ m/s, and $\lambda = 590$ nm, compute the expected fringe shift $\Delta\phi = c\Delta t/\lambda$ in units of fringe widths. (b) Michelson and Morley measured a shift of less than 0.01 fringes. Compare this to your answer. (c) State in one sentence what this null result implies about the ether hypothesis, and what it forced Einstein to assume. *Tests: the Michelson-Morley calculation, null result interpretation, bridge to special relativity.*

**Challenge.** Starting from the two-slit condition $d\sin\theta = m\lambda$ and the single-slit envelope $|\text{sinc}(\pi a\sin\theta/\lambda)|^2$, find the conditions under which an interference maximum is *missing* — i.e., falls exactly on a single-slit diffraction minimum. (a) Derive the general condition on the ratio $d/a$ for the $m$-th order maximum to be missing. (b) For $d/a = 3$, which orders are missing? Sketch the resulting intensity pattern. (c) A student claims that the central maximum is never missing. Prove this claim using your condition. *Tests: combining two-slit and single-slit formulas, missing orders, mathematical proof.*

<!-- → [TABLE: the six threads of Chapter 12 — columns: thread, key phenomenon, the Maxwell connection, where classical EM is sufficient, where it must be extended — rows: geometric optics (Snell's law, n = c/v, short-wavelength limit of Maxwell, always), wave optics (interference, linear superposition, always), antenna radiation (Larmor, accelerating charges, always), photoelectric effect (E = hf, classical prediction is wrong, needs photon/QED), special relativity (E and B as one tensor, Maxwell already covariant, Einstein recognized it), wireless (link budget, Poynting vector + radiation pattern, always) — to show which threads stay within Maxwell and which point beyond] -->

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

**Tags:** Snell's law, interference, diffraction, antenna, Larmor, photoelectric effect, Einstein, special relativity, wireless, photon
