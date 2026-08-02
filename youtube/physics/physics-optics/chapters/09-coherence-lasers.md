# Chapter 9 — Coherence, Lasers, and Modern Optics


## TL;DR

- What makes laser light different from ordinary light — and the engineering it enables.
- The chapter moves through Learning objectives, Opening case: LIGO at the limit of measurement, Core concept, Coherence, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*What makes laser light different from ordinary light — and the engineering it enables.*

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Understand)** Distinguish temporal and spatial coherence and explain how each affects an interference experiment.
2. **(Apply)** Compute the coherence length $\ell_c = c/\Delta f$ for a source given its spectral bandwidth.
3. **(Understand)** State Einstein's 1917 relations and identify what stimulated emission means (same direction, phase, frequency as the stimulating photon).
4. **(Apply)** Compute cavity mode spacing $\Delta\nu = c/(2L)$ for a Fabry-Perot resonator of length $L$.
5. **(Apply)** Compute Gaussian-beam parameters: Rayleigh range $z_R = \pi w_0^2/\lambda$ and divergence $\theta \sim \lambda/(\pi w_0)$.
6. **(Apply)** Build a laser-cavity-mode and Gaussian-beam visualizer.

---

## Opening case: LIGO at the limit of measurement

LIGO measures arm-length differences of $10^{-18}$ m — one-thousandth of a proton's diameter. This is impossibly small *unless* you have a light source with extraordinary coherence. The reason: at this precision, the interferometer must reliably *compare phases* of light that has traveled along two separate paths of about 4 km. The path-length difference of $10^{-18}$ m corresponds to a phase difference of $10^{-18} / \lambda \approx 10^{-12}$ radians at $\lambda = 1$ µm.

To measure phases this precisely, you need light that *has a phase* — that is monochromatic enough for "phase" to be a meaningful quantity over the time it takes to traverse the interferometer. This requires **temporal coherence** over at least the round-trip time (~30 µs for a 4 km arm), corresponding to a coherence length of at least ~10 km.

A laser with stabilization can deliver this. A thermal source (light bulb, Sun) absolutely cannot — its coherence length is microns.

The laser is the device that made coherence at this scale possible. This chapter explains *why* lasers are coherent (stimulated emission + cavity selection), how the cavity defines lasing frequencies, and how Gaussian beams describe the spatial profile of laser output.

---

## Core concept

### Coherence

**Coherence** is the property that determines whether two parts of a light field can interfere. There are two flavors.

**Temporal coherence** measures how monochromatic the light is. A perfectly monochromatic source has infinite coherence time. Real sources have a finite bandwidth $\Delta f$. The **coherence time** is
$$\tau_c \sim \frac{1}{\Delta f}$$
and the **coherence length** is
$$\ell_c = c \tau_c$$

Two beams can interfere only if their path-length difference is less than $\ell_c$.

| Source | Bandwidth $\Delta f$ | Coherence length $\ell_c$ |
|---|---|---|
| White light (full visible) | ~3 × 10¹⁴ Hz | ~1 µm |
| Sodium lamp (narrow line) | ~10⁹ Hz | ~30 cm |
| HeNe laser (typical) | ~10⁹ Hz | ~30 cm |
| Stabilized HeNe | ~10⁵ Hz | ~3 km |
| Nd:YAG, frequency-stabilized | ~10² Hz | ~3000 km |

**Spatial coherence** measures how uniform the wavefront is across the beam at any instant. A point source is perfectly spatially coherent; an extended source (Sun, fluorescent tube) has limited spatial coherence — different points emit independently. The coherence width depends on source size and propagation distance.

Lasers are *both* temporally and spatially coherent. That's the defining feature.

### Stimulated emission

Einstein, "Zur Quantentheorie der Strahlung" (Phys. Z. 18, 121, 1917). For two atomic energy levels $E_1 < E_2$, three radiative processes connect them:

1. **Absorption.** Atom in $E_1$ absorbs a photon of energy $hf = E_2 - E_1$, transitions to $E_2$. Rate $\propto B_{12} \rho(\nu) N_1$.
2. **Spontaneous emission.** Atom in $E_2$ spontaneously emits a photon, falls to $E_1$. Random direction and phase. Rate $\propto A_{21} N_2$.
3. **Stimulated emission.** Atom in $E_2$, in the presence of a photon of the right frequency, is *stimulated* to emit a second photon — **in the same direction, with the same phase, and the same frequency** as the stimulating photon. Rate $\propto B_{21} \rho(\nu) N_2$.

Einstein's identities (derived from thermodynamic balance with Planck's distribution):
$$B_{12} = B_{21}, \qquad \frac{A_{21}}{B_{21}} = \frac{8\pi h\nu^3}{c^3}$$

The stimulated photon is in the *same quantum state* as the stimulating photon. This is the coherent "amplification" the laser exploits.

### Population inversion

For a beam of light passing through a medium, each photon either gets absorbed (rate $\propto N_1$) or stimulates emission (rate $\propto N_2$). Net amplification requires
$$N_2 > N_1$$

This is **population inversion** — more atoms in the upper state than the lower. In thermal equilibrium, Boltzmann puts most atoms in the lower state; inversion is impossible without pumping.

Inversion is achieved by *pumping*: external energy excites atoms to a higher level, from which they decay quickly to the upper laser level.

**Three-level laser** (e.g., ruby): the lower laser level is the ground state. Achieving inversion requires pumping > 50% of atoms to the upper state. Difficult.

**Four-level laser** (e.g., Nd:YAG, HeNe, most commercial lasers): the lower laser level is an excited state that empties quickly to the ground state. Inversion is much easier.

### The laser cavity

A laser cavity is two mirrors forming a Fabry-Perot resonator. The gain medium sits between them. Light bounces back and forth, gaining intensity each pass through the gain medium via stimulated emission. One mirror is partially transmissive; the output is what escapes.

The cavity defines which frequencies *resonate*: standing-wave condition requires an integer number of half-wavelengths between the mirrors:
$$L = m\lambda/2 \implies \nu_m = mc/(2L)$$

**Mode spacing:**
$$\Delta\nu = \frac{c}{2L}$$

For a 30 cm cavity: $\Delta\nu = 500$ MHz. The gain medium has a bandwidth $\Delta\nu_{\text{gain}}$ — only modes within this bandwidth can lase.

If gain bandwidth is broader than mode spacing: multimode operation (many simultaneous frequencies). If narrower: single-mode (one frequency only). Most HeNe lasers run multimode; high-precision applications (interferometry, atom physics) require single-mode operation, achieved with longer cavities or additional filters.

### Gaussian beams

A laser cavity made of finite-aperture mirrors doesn't produce a plane wave. The fundamental mode is a **Gaussian beam** (TEM₀₀ mode). At any cross-section, the intensity profile is
$$I(r) = I_0 e^{-2r^2/w^2}$$

$w$ is the beam radius — where intensity drops to $1/e^2 = 13.5\%$ of peak.

The beam *waist* $w_0$ is the narrowest point. The **Rayleigh range** is the distance over which the beam stays nearly collimated:
$$z_R = \frac{\pi w_0^2}{\lambda}$$

For $z \gg z_R$, the beam radius grows nearly linearly:
$$w(z) = w_0 \sqrt{1 + (z/z_R)^2}$$

The **divergence angle** (far field):
$$\theta_{\text{div}} \approx \frac{\lambda}{\pi w_0}$$

**The trade-off**: smaller waist → faster divergence. A tightly focused beam doesn't stay tight; the diffraction limit (Ch 6) forces this trade-off.

For $w_0 = 1$ mm at $\lambda = 633$ nm (HeNe): $z_R = \pi \times (10^{-3})^2 / (6.33 \times 10^{-7}) \approx 4.96$ m. The beam stays approximately 1 mm wide for about 5 m, then begins to diverge.

### Common laser types

| Type | Wavelength | Notable | Application |
|---|---|---|---|
| HeNe | 633 nm | Long coherence, low power | Teaching, alignment, interferometry |
| Nd:YAG | 1064 nm (also 532 nm doubled) | Solid-state, high power | Industrial cutting, marking, LIGO |
| Diode (semiconductor) | various 400 nm – 2 µm | Most-manufactured laser type | CD/DVD/Blu-ray, fiber comm, pointers |
| Ti:sapphire | 700–1000 nm tunable | Femtosecond pulses | Ultrafast science, eye surgery |
| Excimer (KrF, ArF) | UV (~200 nm) | High-energy pulses | Lithography, LASIK |
| Fiber lasers (Er, Yb) | 1.5 µm | Telecom band | Internet backbone |
| CO₂ | 10.6 µm | High continuous power | Industrial cutting, welding |

Laser technology is roughly a $20+ billion industry: industrial processing, telecom, defense, medical, research.

### Maiman's first laser (1960)

Theodore Maiman at Hughes Research Labs in Malibu, California, built the first working laser on **16 May 1960**. The medium: a synthetic pink ruby rod (~1 cm long). A coiled flash lamp pumped the chromium ions in the ruby; the output was red pulses at 694.3 nm.

Curious history: Maiman submitted to *Physical Review Letters*. PRL rejected it as "another laser paper" (the editor was apparently saturated with maser papers). Maiman published in *Nature*: "Stimulated Optical Radiation in Ruby," Nature 187, 493 (6 August 1960).

The Nobel for laser physics went to Townes, Basov, and Prokhorov in 1964 — for the *maser* (microwave version, 1953–1954) which preceded the optical laser. Maiman was repeatedly considered for the Nobel but never received it.

### Applications

- **Holography** (Gabor 1948, Nobel 1971; practical after lasers): records 3D interference patterns between an object beam and a reference beam.
- **Fiber-optic communication**: every long-haul Internet packet rides on near-infrared laser light through optical fiber. Telecom uses 1.55 µm (the minimum-loss wavelength in standard fiber).
- **LiDAR**: laser ranging, used in autonomous vehicles, atmospheric profiling, archaeology.
- **Optical tweezers** (Ashkin Nobel 2018): focused laser beams trap and manipulate microscopic objects.
- **Laser cooling** (Phillips, Chu, Cohen-Tannoudji Nobel 1997): lasers cool atoms to nanokelvin temperatures. Foundation of Bose-Einstein condensates, atomic clocks, atom interferometers.
- **LIGO**: stabilized laser interferometry for gravitational-wave detection (Weiss, Barish, Thorne Nobel 2017).

---

## Worked example: cavity modes and gain bandwidth

A HeNe laser cavity is 30 cm long. The gain medium (helium-neon mixture) has a gain bandwidth of about 1.5 GHz. How many cavity modes can lase simultaneously?

**Mode spacing:**
$$\Delta\nu = c/(2L) = (3 \times 10^8)/(2 \times 0.30) = 5.0 \times 10^8 \text{ Hz} = 500 \text{ MHz}$$

**Number of modes within gain bandwidth:**
$$N = \Delta\nu_{\text{gain}} / \Delta\nu = (1.5 \times 10^9) / (5.0 \times 10^8) = 3$$

About three cavity modes lase simultaneously. The laser is *multimode* — three independent frequencies, each at a slightly different wavelength near 633 nm.

**The lesson.** The cavity selects discrete frequencies. The gain bandwidth selects which of those frequencies can actually lase. For single-mode operation: either shorten the cavity (longer mode spacing) or narrow the gain bandwidth (frequency-stabilization).

**The limit.** This treats the gain bandwidth as a flat function. In reality, gain is a Lorentzian profile; modes near the peak lase more strongly than modes at the edges. For high-precision applications, an *etalon* (a thin Fabry-Perot inside the main cavity) is added to filter to one mode.

---

## Common misconceptions

**"Laser light is special because it is intense."** Many flames are brighter than HeNe lasers. The laser's defining feature is *coherence*, not intensity. Industrial lasers can be very intense; teaching lasers are usually mW-class.

**"Stimulated emission means the atom is copied."** The *photon* is copied (same state — same direction, phase, frequency). The atom transitions from $E_2$ to $E_1$ — it loses its energy. Two photons emerge from one.

**"The cavity selects the wavelength on its own."** The cavity selects *frequencies* (mode spacing $c/2L$). The gain medium selects which frequencies actually have enough gain to lase. Both contribute.

**"A laser is just a brighter version of a flashlight."** A laser is fundamentally different in that the light is *coherent* — all photons in the beam are in the same state. A flashlight is bright but thermal; the photons are uncorrelated.

**"You can focus a laser to arbitrarily small spots."** Limited by diffraction: minimum waist $w_0 \sim \lambda$. Below that, the beam diverges immediately; no useful tight focus exists.

---

## Exercises

**Warm-up (Apply).** A laser has bandwidth $\Delta f = 100$ MHz. Find the coherence time and coherence length.

**Apply.** A HeNe laser cavity is 40 cm long. The HeNe gain bandwidth is about 1.5 GHz. How many modes lase?

**Apply.** A Gaussian beam has waist $w_0 = 0.5$ mm at $\lambda = 633$ nm. (a) Find the Rayleigh range. (b) Find the beam radius at $z = 100$ m. (c) Find the divergence angle in milliradians.

**Apply + Analyze.** You want a laser with a coherence length of 100 km. The center wavelength is 1064 nm. Find the maximum bandwidth allowed. Express in both Hz and in nm.

**Apply (Einstein A and B).** Stimulated emission rate $\propto B_{21} \rho(\nu) N_2$. Spontaneous emission rate $\propto A_{21} N_2$. Find the ratio of stimulated to spontaneous emission at: (a) $\lambda = 633$ nm with $\rho(\nu)$ corresponding to a HeNe laser intracavity intensity of $10^4$ W/m² (laser intensity within the cavity); (b) the same wavelength but $\rho(\nu)$ corresponding to thermal blackbody emission at $T = 300$ K.

**Challenge.** Derive Einstein's identity $A_{21}/B_{21} = 8\pi h\nu^3/c^3$ from the thermal-equilibrium balance: $B_{12} \rho(\nu) N_1 = (A_{21} + B_{21} \rho(\nu)) N_2$, with $N_2/N_1 = e^{-h\nu/k_BT}$ (Boltzmann) and $\rho(\nu)$ the Planck distribution. Show that $B_{12} = B_{21}$ falls out for the equation to hold at all temperatures.

---

## LLM Exercises

### Build the laser cavity simulator (`09-laser-cavity.html`)

> **Show.** Cavity mode spacing $\Delta\nu = c/(2L)$. Gaussian beam $w(z) = w_0\sqrt{1 + (z/z_R)^2}$ with $z_R = \pi w_0^2/\lambda$.
>
> **Say.** Build a laser cavity mode and Gaussian beam visualizer.
>
> **Constrain.** D3 v7. Panel 1: cavity mode display. Schematic of two mirrors forming a cavity (length $L$). Frequency axis showing cavity modes as vertical lines spaced by $c/2L$. Gain profile as a Gaussian envelope. Modes within gain bandwidth highlighted. Numerical readouts: $\Delta\nu$ in MHz, number of lasing modes. Sliders: cavity length $L$, gain bandwidth $\Delta\nu_{\text{gain}}$, center wavelength.
> Panel 2: Gaussian beam display. Beam profile $w(z)$ as two curves $\pm w(z)$. Slider for $w_0$. Mark beam waist and Rayleigh range. Display divergence angle.
> Filename: `09-laser-cavity.html`.
>
> **Verify.** (a) $L = 30$ cm: $\Delta\nu = 500$ MHz. (b) Gain bandwidth 1.5 GHz: about 3 lasing modes. (c) $w_0 = 1$ mm, $\lambda = 633$ nm: $z_R \approx 5$ m. (d) At $z = z_R$, $w(z) = w_0\sqrt{2}$.

### Exploration

- Sweep cavity length from 10 cm to 1 m. Watch the mode spacing change inversely. At what length is only one mode within the 1.5 GHz HeNe gain bandwidth? (Answer: $L > 10$ m, much longer than commercial HeNe lasers.)
- For a Gaussian beam, set $w_0 = 0.1$ mm. Where is the beam radius 1 mm? (Answer: $z = z_R \sqrt{99} \approx 10 z_R$, far beyond Rayleigh range.)
- Compare a HeNe laser ($\lambda = 633$ nm) and an Nd:YAG ($\lambda = 1064$ nm) with the same $w_0 = 1$ mm. The Nd:YAG has $z_R$ about 60% smaller. Why? (Answer: $z_R \propto 1/\lambda$, so longer wavelength has smaller Rayleigh range.)

### Extension prompt (chapter bridge)

> **Show.** Laser light is the most classical-wave-like light. But what happens in a *single-photon* experiment, where one photon at a time goes through the apparatus?
>
> **Say.** Build a single-photon double-slit accumulation simulator.
>
> **Constrain.** Generate photons one at a time. Each photon lands at a position drawn from the intensity distribution $I(y) \propto \cos^2(\pi d y / \lambda L)$ (random sampling). Accumulate dots over many shots. Show the interference pattern emerging from accumulated dots.
>
> **Verify.** After ~100 photons: random-looking scatter. After ~10,000 photons: clear interference fringes. The pattern is the same as classical wave optics predicts, but each individual photon is a discrete point.

Save as `09b-single-photon-preview.html`. This is the bridge to Chapter 10.

---

## What would change my mind

Einstein's 1917 framework is the bedrock of laser physics; no controversy remains at intro level. The Gaussian-beam description rests on the paraxial wave equation, an excellent approximation for narrow beams. Cavity selection follows from the resonance condition on standing waves, exact in the appropriate limit.

What's contested is at the frontier: *topological lasers*, *plasmonic lasers*, lasers with quantum advantages from squeezed light. These extend the classical picture; they don't replace it.

## Still puzzling

- *What is the ultimate noise floor of laser interferometry?* Shot noise from photon statistics sets the classical limit. *Squeezed light* (used in LIGO's recent upgrade) pushes below this limit. The theoretical and engineering frontier is moving.
- *Can lasers be built at X-ray wavelengths?* Yes, with difficulty. X-ray free-electron lasers (LCLS at SLAC, European XFEL, others) use accelerated electrons in magnetic undulators rather than atomic transitions, producing coherent X-rays for materials science and biology.
- *Why is laser cooling possible?* The Doppler-shifted absorption of laser photons by a moving atom robs the atom of kinetic energy. The detailed physics is fascinating; the headline is that atom optics, BEC, and high-precision metrology all rest on laser cooling.

---

**Tags:** coherence, temporal coherence, spatial coherence, stimulated emission, population inversion, cavity modes, Gaussian beam, Rayleigh range, Maiman, ruby laser, HeNe, Nd:YAG

![Three side-by-side panels of a two-level atom interacting with light. Absorption: incoming photon vanishes, atom jumps from E_1 to E_2. Spontaneous emission: atom in E_2 decays randomly, emitting one photon in a rando...](images/09-coherence-lasers-fig-01.png)
*Figure 9.1 — Einstein's Three Processes*

![Two energy-level diagrams. Left: 3-level scheme (ruby). Pump excites E_0 to E_2, fast non-radiative decay to upper laser level E_1, laser transition from E_1 back down to E_0 (ground). The lower laser level IS the gro...](images/09-coherence-lasers-fig-02.png)
*Figure 9.2 — Population Inversion*

![Top: laser cavity with two parallel mirrors and a gain medium between them. The left mirror is fully reflective, the right mirror partially transmissive (output coupler). Standing-wave intensity inside the cavity draw...](images/09-coherence-lasers-fig-03.png)
*Figure 9.3 — Laser Cavity*

![Side-view of a Gaussian laser beam (TEM00). Beam envelope symmetric about the propagation axis. The waist w_0 is the narrowest point. Within plus or minus the Rayleigh range z_R, the beam stays approximately collimate...](images/09-coherence-lasers-fig-04.png)
*Figure 9.4 — Gaussian Beam*

![Schematic of Theodore Maiman's first working laser. A pink synthetic ruby rod is wrapped by a helical flash lamp. Mirrors at each end of the rod — one fully reflective, one partially silvered as the output coupler. Th...](images/09-coherence-lasers-fig-05.png)
*Figure 9.5 — Maiman's First Laser*

