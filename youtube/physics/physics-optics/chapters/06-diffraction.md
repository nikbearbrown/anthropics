# Chapter 6 — Wave Optics: Diffraction


## TL;DR

- Waves bending around obstacles, and the resolution limit of every optical instrument.
- The chapter moves through Learning objectives, Opening case: the resolution of the Hubble Space Telescope, Core concept, Huygens' principle (1678), and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Waves bending around obstacles, and the resolution limit of every optical instrument.*

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Understand)** State Huygens' principle and explain how it accounts for wave propagation, reflection, refraction, and diffraction.
2. **(Apply)** Use the single-slit pattern $I(\theta) = I_0 [\sin(\alpha)/\alpha]^2$ with $\alpha = \pi a \sin\theta / \lambda$ to find minima and predict the angular width of the central maximum.
3. **(Apply)** Use the grating equation $d \sin\theta = m\lambda$ to compute principal-maximum angles and find resolving power $R = mN$.
4. **(Apply)** Apply the Rayleigh criterion $\theta_{\min} = 1.22 \lambda/D$ for circular apertures to find the angular resolution of telescopes and microscopes.
5. **(Apply)** Use Bragg's law $2d\sin\theta = m\lambda$ to compute X-ray diffraction angles for known crystal spacings.
6. **(Apply)** Build a diffraction simulator that shows single-slit, multi-slit, and grating patterns for varying parameters.

---

## Opening case: the resolution of the Hubble Space Telescope

The Hubble Space Telescope's main mirror is 2.4 m in diameter. From orbit (above Earth's atmosphere), the angular resolution it can achieve is set by the *diffraction limit*: $\theta_{\min} \approx 1.22 \lambda / D$.

For visible light at $\lambda = 550$ nm: $\theta_{\min} = 1.22 \times (5.5 \times 10^{-7})/2.4 \approx 2.8 \times 10^{-7}$ radians = 0.058 arcseconds.

At a distance of, say, the Moon (390,000 km), this corresponds to features as small as $390{,}000 \times 2.8 \times 10^{-7} = 110$ m across. For the Andromeda Galaxy (2.5 million light-years), $\sim 21,000$ light-hours per pixel — still resolving individual giant stars.

The diffraction limit isn't a flaw of the lens. It's not solvable by polishing the mirror more carefully or using better detectors. It's the *fundamental wave-optical limit set by the aperture size and the wavelength*. The only way to resolve finer detail is to make the aperture bigger or use shorter wavelengths.

This is why the James Webb Space Telescope has a 6.5 m mirror (2.7× wider, ~2.7× better resolution at the same wavelength) and observes mostly in the infrared. It's why electron microscopes (using electron de Broglie wavelengths ~picometers instead of light's hundreds of nanometers) resolve atoms. The Rayleigh criterion sets the rules of the game.

This chapter derives the diffraction patterns that govern resolution — and the X-ray diffraction technique that revealed the structure of DNA.

---

## Core concept

### Huygens' principle (1678)

Every point on a wavefront acts as a *secondary source* of spherical wavelets. The new wavefront at a later time is the envelope of all these secondary wavelets.

Huygens' principle works because Maxwell's wave equation is linear: superposing many spherical solutions gives the actual wavefront. For propagation through free space, the secondary wavelets construct exactly the next-instant wavefront. For propagation through a slit or around an obstacle, the wavelets from the unobstructed portion produce the *diffraction pattern* — interference of all the secondary sources.

Diffraction is, structurally, *interference of infinitely many sources*. Single-slit diffraction is what you get when every point across the slit width acts as a Huygens secondary source and they all interfere.

### Single-slit diffraction

A slit of width $a$ illuminated by a plane wave of wavelength $\lambda$. At an angle $\theta$ from the forward direction, the intensity pattern is

$$I(\theta) = I_0 \left[\frac{\sin\alpha}{\alpha}\right]^2$$

where $\alpha = \pi a \sin\theta / \lambda$.

**Minima:** $\sin\alpha = 0$ (excluding $\alpha = 0$), i.e., $\alpha = m\pi$ for $m = \pm 1, \pm 2, ...$. This gives
$$a \sin\theta = m\lambda$$

**Central maximum:** at $\theta = 0$. The angular *width* of the central maximum is the angular spread from $-\lambda/a$ to $+\lambda/a$ (the first minima on each side), so the full angular width is $2\lambda/a$.

Narrower slit ($a$ small) → wider central maximum.
Wider slit ($a$ large) → narrower central maximum.
As $a \to \infty$: $2\lambda/a \to 0$, recovering geometric optics (the wave passes through without diffracting).

### Double-slit revisited

A "real" double-slit experiment has slits of finite width $a$, separated by $d > a$. The total intensity pattern is the *product* of:
- The two-slit interference pattern: $\cos^2(\pi d \sin\theta / \lambda)$
- The single-slit diffraction envelope: $[\sin\alpha/\alpha]^2$ with $\alpha = \pi a \sin\theta / \lambda$.

$$I(\theta) = I_0 \cos^2\left(\frac{\pi d \sin\theta}{\lambda}\right) \cdot \left[\frac{\sin(\pi a \sin\theta / \lambda)}{\pi a \sin\theta / \lambda}\right]^2$$

The interference produces narrowly-spaced fringes; the diffraction envelope determines which interference fringes are visible. The first diffraction zero kills interference orders at $\sin\theta_{\text{diff}} = \lambda/a$. The visible interference fringes lie within this envelope.

### Diffraction gratings

A grating is many parallel slits with uniform spacing $d$. For $N$ slits, the intensity pattern is

$$I(\theta) = I_0 \left[\frac{\sin(N\pi d \sin\theta / \lambda)}{N \sin(\pi d \sin\theta / \lambda)}\right]^2 \cdot \text{(single-slit envelope)}$$

The two-slit pattern has broad maxima; the $N$-slit pattern has *sharp* principal maxima at the same locations:
$$d \sin\theta = m\lambda$$

But the maxima are now very narrow (width $\propto 1/N$), and there are $N - 2$ subsidiary maxima between principal ones. As $N$ grows, the principal maxima become extremely sharp.

**Resolving power.** The grating's ability to distinguish two close wavelengths is
$$R = \frac{\lambda}{\Delta\lambda} = mN$$

Larger grating (more lines) → higher resolving power. Higher diffraction order $m$ → higher resolving power.

For a grating with 1200 lines/mm over 1 cm (so 12,000 lines) used in $m = 1$: $R = 12{,}000$. At $\lambda = 500$ nm, you can resolve $\Delta\lambda = 500/12000 = 0.04$ nm. The sodium yellow doublet (589.0 and 589.6 nm, separation 0.6 nm) is easily resolved.

### Circular aperture: the Airy disk

A circular aperture of diameter $D$ produces an *Airy disk* — a central bright spot surrounded by concentric rings. The mathematics involves Bessel functions, but the key result is the angular position of the *first* dark ring:

$$\sin\theta_{\min} \approx 1.22 \frac{\lambda}{D}$$

The 1.22 factor comes from the first zero of the Bessel function $J_1(\pi x)$.

### The Rayleigh criterion

Two point sources are "just resolved" when the maximum of one Airy pattern falls on the first dark ring of the other. The angular separation is exactly
$$\theta_{\min} = 1.22 \frac{\lambda}{D}$$

For a telescope of diameter $D$ observing at wavelength $\lambda$, this is the *minimum angular separation* of two stars that can be distinguished.

For a 100 mm aperture at $\lambda = 550$ nm: $\theta_{\min} \approx 6.7 \times 10^{-6}$ rad ≈ 1.4 arcseconds. For an 8 m telescope (e.g., Subaru on Mauna Kea): $\theta_{\min} \approx 0.017$ arcseconds (without atmosphere; in practice atmospheric distortion limits it to ~1 arcsec without adaptive optics).

This is the *diffraction limit* — the fundamental limit of any imaging system. Bigger aperture → finer resolution.

### X-ray diffraction (Bragg's law)

Crystals are stacks of parallel atomic planes with spacing $d$ on the order of $10^{-10}$ m = 0.1 nm. X-rays of similar wavelength reflect off each plane; the reflections from different planes interfere.

**Bragg's law:** for X-rays of wavelength $\lambda$ incident at angle $\theta$ from the planes, constructive interference between reflections from adjacent planes:
$$2 d \sin\theta = m\lambda$$

Each set of planes in a crystal produces its own diffraction angle, mapping the crystal's structure to a pattern of diffraction spots. X-ray crystallography uses this to determine atomic structure.

Major achievements: Bragg's 1913 application (Nobel 1915), Watson-Crick-Franklin DNA structure (1953, partly via Franklin's X-ray diffraction images), every protein structure in the Protein Data Bank (>200,000+ structures as of 2024). Modern electron and neutron diffraction use the same principle for shorter wavelengths.

---

## Worked example: the smallest detail Hubble can see on Mars

Hubble's 2.4 m mirror at $\lambda = 550$ nm. Mars at closest approach is at distance $5.5 \times 10^{10}$ m. What's the smallest feature on Mars Hubble can resolve?

**Angular resolution:**
$$\theta_{\min} = 1.22 \lambda / D = 1.22 \times (5.5 \times 10^{-7})/(2.4) = 2.8 \times 10^{-7} \text{ rad}$$

**Linear resolution at Mars distance:**
$$L = R \times \theta = (5.5 \times 10^{10}) \times (2.8 \times 10^{-7}) \approx 15 \text{ km}$$

Hubble can resolve features about 15 km across on Mars. Compare to the giant Olympus Mons volcano (~600 km across, easily resolved) or the smallest Mars rover tracks (~3 m wide, never resolvable).

**The lesson.** Diffraction sets the limit. Resolution at a distance scales as $L = R \cdot 1.22 \lambda / D$. To resolve a 3 m feature at Mars distance would require $D = 1.22 \lambda R / L = 1.22 \times 5.5 \times 10^{-7} \times 5.5 \times 10^{10} / 3 = 12{,}000$ m — a 12 km telescope. Not built. Not coming soon. *Unless* we use shorter wavelengths (X-rays) or interferometric arrays (Very Large Array, Event Horizon Telescope) that simulate a much larger effective aperture.

**The limit.** This is the theoretical diffraction limit. In practice, Hubble's optics, detector noise, and orbital stability all impose additional limits. The Rayleigh criterion is the *floor* — you can't do better than this, but you can do worse.

---

## Common misconceptions

**"Diffraction only happens at edges."** It happens wherever a wave passes through a finite aperture or around any obstacle. The "edge" is the boundary of the aperture; the diffraction is the bending of the wave around it.

**"A larger aperture gives worse resolution."** The opposite. Larger aperture → smaller diffraction angle → finer resolution. The Airy disk shrinks; the Rayleigh criterion improves.

**"The grating equation is different from the double-slit equation."** It's the same equation $d \sin\theta = m\lambda$. The grating just has more slits, making the principal maxima sharper.

**"Diffraction is a different phenomenon from interference."** They're the same physics: wave superposition. Diffraction is what we call interference of infinitely many sources (Huygens secondary sources across an aperture).

**"X-ray diffraction works because crystals are like diffraction gratings."** True, but the gratings here are *3D*, not 1D. X-rays diffract from arrays of atomic planes; Bragg's law captures the simplest case. Real crystallographic analysis uses 3D diffraction theory (Laue conditions).

---

## Exercises

**Warm-up (Apply).** A single slit of width $a = 0.1$ mm is illuminated by $\lambda = 500$ nm. Find the angular width of the central maximum (full width to first dark fringes).

**Apply.** A diffraction grating has 600 lines/mm. Illuminated by $\lambda = 589$ nm (sodium yellow). Find the angles of the $m = 1, 2, 3$ principal maxima. Is $m = 4$ visible?

**Apply.** A telescope with aperture $D = 200$ mm observes at $\lambda = 550$ nm. (a) Find the angular resolution in arcseconds. (b) The full Moon is 31 arcminutes across. How many "resolvable spots" wide is the Moon, seen through this telescope?

**Apply + Analyze.** A grating with 1200 lines/mm is used to resolve the sodium doublet (589.0 nm and 589.6 nm). Find the minimum number of grating lines $N$ required. Hint: use $R = \lambda/\Delta\lambda = mN$, solve for $N$ in first order.

**Apply (X-ray crystallography).** Copper has a face-centered cubic structure with lattice constant $a = 0.362$ nm. X-rays of $\lambda = 0.154$ nm (Cu K-alpha line) hit a single crystal. The (200) planes have spacing $a/2 = 0.181$ nm. Find the Bragg angle for first-order reflection from these planes.

**Challenge.** Why is the Airy-disk factor 1.22 (not 1.0)? Show that the first dark ring of a circular aperture is at $\sin\theta = 1.22 \lambda/D$ by referring to the first zero of the Bessel function $J_1(x) = 0$ at $x \approx 3.832$, and noting that for a circular aperture of diameter $D$, the function is $J_1(\pi D \sin\theta / \lambda)/(\pi D \sin\theta / \lambda)$.

---

## LLM Exercises

### Build the diffraction simulator (`06-diffraction.html`)

> **Show.** Single slit: $I(\theta) = I_0 [\sin(\pi a \sin\theta/\lambda)/(\pi a \sin\theta/\lambda)]^2$. Multi-slit: combine with two-slit interference factor.
>
> **Say.** Build an interactive diffraction-pattern simulator.
>
> **Constrain.** D3 v7. Aperture mode toggle: single slit / double slit / grating ($N$ slits). Sliders for slit width $a$, slit separation $d$ (when relevant), number of slits $N$, wavelength $\lambda$. Display: intensity pattern $I(\theta)$ as a line plot on the right; sinc² envelope (single-slit pattern) as a dashed line when in multi-slit modes; positions of principal maxima labeled; angular width of central maximum displayed. For grating mode: resolving power $R = mN$ displayed for visible orders. Filename: `06-diffraction.html`.
>
> **Verify.** (a) Single slit, $a = 0.1$ mm, $\lambda = 500$ nm: first minimum at $\sin\theta = 0.005$ rad. (b) Double slit ($d = 0.5$ mm, $a = 0.1$ mm, $\lambda = 550$ nm): fringe spacing $\sim 1.1$ mrad; diffraction envelope first zero at $5.5$ mrad. (c) Grating ($N = 10$, $d = 1$ µm, $\lambda = 500$ nm): principal maxima at $\sin\theta = 0.5$ (first order); sharp peaks much narrower than the two-slit case.

### Exploration

- Compare single-slit ($N=1$) and multi-slit ($N=10$) patterns at the same $d$. The principal maxima appear at the same angles but the peaks are much narrower in the multi-slit case.
- For the double-slit ($N=2$), set $d/a$ ratio to 3: count the visible interference fringes within the diffraction envelope. (Answer: about 5 on each side of center.)
- For a grating with $d = 1$ µm, sweep $\lambda$ from 400 to 700 nm. Watch the principal maxima shift outward as $\lambda$ increases. This is *dispersion by a grating* — the basis of spectrometers.

### Extension prompt (chapter bridge)

> **Show.** Polarization is the orientation of the $\vec{E}$ field in a transverse wave. Diffraction and interference treat light as a scalar wave; polarization treats it as a vector.
>
> **Say.** Build a polarization-state visualizer.
>
> **Constrain.** Animated $\vec{E}$ tip tracing the polarization ellipse. Sliders for $E_x$ amplitude, $E_y$ amplitude, phase difference $\delta$ between them. Display: linear / circular / elliptical classification based on parameters; the polarization angle for linear; handedness for circular.
>
> **Verify.** $E_x = E_y$, $\delta = 0$: linear at 45°. $E_x = E_y$, $\delta = \pi/2$: right-circular.

Save as `06b-polarization-preview.html`. This is the bridge to Chapter 7.

---

## What would change my mind

Diffraction is a direct consequence of wave superposition. A confirmed violation of single-slit diffraction pattern at the predicted intensities, in the optical regime where wavelength is well-defined, would force re-examination of Maxwell's equations themselves. None exists. The Rayleigh criterion is engineering practice for every imaging system from telescopes to microscopes; the empirical confirmation is overwhelming. Beyond the diffraction limit, *super-resolution* techniques (STED, PALM, STORM — Chapter 8) get around the limit by using nonlinear or stochastic methods, not by violating wave optics.

## Still puzzling

- *Why is the Rayleigh criterion "just resolved" rather than a strict threshold?* The criterion is a convention; in practice, the "minimum resolvable separation" depends on signal-to-noise and detector resolution. Modern image-processing techniques can extract structure below the Rayleigh limit if you have enough photons and the right priors.
- *X-ray crystallography for non-crystalline samples.* Most biology happens in solution, not in crystals. Cryo-electron microscopy and single-particle imaging are extending structural biology to non-crystalline samples; resolution is approaching that of X-ray crystallography for many problems.
- *Diffraction-limited imaging beyond the visible.* Radio astronomy combines signals from many separated telescopes (interferometry, Very Large Array, Event Horizon Telescope) to simulate apertures of thousands of kilometers. Effective resolution: micro-arcseconds. The Event Horizon Telescope's image of the M87 black hole shadow rests on this.

---

**Tags:** Huygens' principle, single-slit diffraction, double-slit pattern, diffraction grating, Airy disk, Rayleigh criterion, X-ray diffraction, Bragg's law, Hubble Space Telescope

![Two panels. Left: a plane wavefront in free propagation, with many points along the wavefront each emitting a small spherical wavelet. The envelope of all the wavelets is the next-instant wavefront, also a plane. Righ...](images/06-diffraction-fig-01.png)
*Figure 6.1 — Huygens' Principle*

![Two stacked panels. Top: single-slit diffraction intensity versus angle, showing the central maximum and the smaller side lobes of the sinc-squared pattern. Zeros at a sine theta equal to integer multiples of lambda....](images/06-diffraction-fig-02.png)
*Figure 6.2 — Single-Slit Sinc² and Double-Slit with Diffraction Envelope*

![Three stacked intensity-versus-angle plots at the same wavelength and slit spacing. N equals 2: broad cosine-squared maxima. N equals 5: narrower peaks with small subsidiary lobes between. N equals 20: very sharp prin...](images/06-diffraction-fig-03.png)
*Figure 6.3 — Diffraction Grating*

![Two panels. Left: the diffraction pattern of a circular aperture — an Airy disk with bright central core and concentric rings. The first dark ring sits at angular radius 1.22 lambda over D. Right: two Airy disks place...](images/06-diffraction-fig-04.png)
*Figure 6.4 — Airy Disk and the Rayleigh Resolution Criterion*

![Two horizontal atomic planes with atoms shown as small filled circles. X-ray incident from upper left at glancing angle theta. Two reflected rays — one from the top plane, one from the lower plane. The extra path trav...](images/06-diffraction-fig-05.png)
*Figure 6.5 — Bragg's Law*

