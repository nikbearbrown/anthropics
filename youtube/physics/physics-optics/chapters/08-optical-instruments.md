# Chapter 8 — Optical Instruments and Resolution


## TL;DR

- Telescopes, microscopes, spectrometers, and the eye — each with a fundamental resolution limit.
- The chapter moves through Learning objectives, Opening case: looking at Jupiter through different telescopes, Core concept, The refracting telescope, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Telescopes, microscopes, spectrometers, and the eye — each with a fundamental resolution limit.*

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Apply)** Compute the angular magnification of a refracting telescope from objective and eyepiece focal lengths.
2. **(Apply)** Compute the total magnification of a compound microscope from objective magnification and eyepiece angular magnification.
3. **(Apply)** Apply the Rayleigh criterion to find the angular resolution of any aperture.
4. **(Apply)** Compute the spectral resolving power of a diffraction grating.
5. **(Understand)** Describe the human eye as an optical system and explain how myopia and hyperopia are corrected.
6. **(Apply)** Build a telescope-resolution simulator showing the Rayleigh limit as two stars merge with decreasing angular separation.

---

## Opening case: looking at Jupiter through different telescopes

Take three different telescopes on a clear night and point each at Jupiter. The 4-inch (100 mm) backyard refractor: shows a small disk and two or three of the Galilean moons as points. The 14-inch (350 mm) advanced amateur scope: shows the disk clearly, the two main equatorial cloud bands, all four Galilean moons as small disks. The 8 m Subaru telescope on Mauna Kea: resolves features on Jupiter at hundreds-of-kilometers scale, finds new moons, detects the chemistry of Io's volcanoes.

Each step in aperture size is a step in *resolution*. The 14-inch is 3.5× wider than the 4-inch, so it resolves features 3.5× finer. The 8 m is 80× wider, so 80× finer. The Rayleigh criterion is the governing relation: $\theta_{\min} = 1.22 \lambda/D$.

This chapter ties geometric optics (Chs 2–4) and wave optics (Chs 5–7) together into the design of real instruments. Every telescope, every microscope, and every spectrometer is governed by the same combination of lens equations and diffraction limits. The simulation lets you experience the Rayleigh criterion by watching two point sources merge as their angular separation drops below it.

---

## Core concept

### The refracting telescope

A simple refracting telescope is two converging lenses on a common axis: an **objective** of focal length $f_{\text{obj}}$ (large) and an **eyepiece** of focal length $f_{\text{eye}}$ (short).

For a distant object (at infinity), the objective forms a real image at $d_{i1} = f_{\text{obj}}$. The two lenses are separated by $f_{\text{obj}} + f_{\text{eye}}$, so this image is at the eyepiece's focal point. The eyepiece then sends parallel rays to the observer's eye, which focuses them onto the retina.

**Angular magnification** for viewing distant objects:
$$M = -\frac{f_{\text{obj}}}{f_{\text{eye}}}$$

Negative sign: image is inverted.

For a 1000 mm objective and 20 mm eyepiece: $M = -50$. The object appears 50× larger angularly.

### Reflecting telescopes

A converging mirror replaces the objective lens. Advantages:
- No chromatic aberration (mirrors reflect all wavelengths equally; lenses bend different wavelengths by different amounts).
- Easier to manufacture in very large sizes (the back of a mirror need only be supported; a lens must be supported only at the edge).
- Lighter for large apertures.

Designs:
- **Newtonian** (Newton 1668): A flat secondary mirror diverts light to the side eyepiece. Simple, classic amateur design.
- **Cassegrain**: A convex secondary mirror sends light back through a hole in the primary. Compact, longer effective focal length.

Modern professional telescopes (Subaru, VLT, Keck, JWST) all use mirror designs. The JWST has 18 hexagonal mirror segments forming a 6.5 m total aperture.

### The compound microscope

Two converging lenses with the *object* placed *just outside the focal point* of the objective. The objective forms a magnified real intermediate image inside the tube. The eyepiece treats this intermediate image as its object and produces a virtual, enlarged image at infinity (or comfortable viewing distance) for the eye.

**Objective magnification:**
$$m_{\text{obj}} = -\frac{L}{f_{\text{obj}}}$$
where $L$ is the tube length (typically 160 mm in standard microscopes — the distance from the back focal point of the objective to the intermediate image plane).

**Eyepiece angular magnification:**
$$m_{\text{eye}} = \frac{25 \text{ cm}}{f_{\text{eye}}}$$
The factor 25 cm is the near point of a relaxed adult eye.

**Total magnification:**
$$M = m_{\text{obj}} \cdot m_{\text{eye}}$$

For a standard microscope with $f_{\text{obj}} = 4$ mm, $f_{\text{eye}} = 25$ mm, $L = 160$ mm:
$$M = (160/4) \times (25/2.5) = 40 \times 10 = 400$$

400× magnification. Standard for biological microscopy.

### Numerical aperture and microscope resolution

A microscope's resolution is set by *diffraction at the objective lens*. The relevant quantity is the **numerical aperture (NA)**:
$$\text{NA} = n \sin\alpha$$
where $\alpha$ is the half-angle of the cone of light the objective accepts and $n$ is the refractive index of the medium between sample and objective.

**Abbé resolution limit:**
$$d_{\min} = \frac{0.61 \lambda}{\text{NA}}$$

For $\lambda = 500$ nm and a dry objective (air, $n = 1$) with $\alpha = 60°$: NA = 0.87, $d_{\min} \approx 350$ nm.

For an **oil-immersion objective** (oil between sample and objective, $n \approx 1.5$): NA can exceed 1.0 (typically 1.25 or 1.40), $d_{\min}$ drops to ~250 nm.

Light microscopy is *diffraction-limited* to about half the wavelength. Below that, you need either shorter-wavelength imaging (electron microscope, atomic-force microscope) or nonlinear tricks (super-resolution microscopy — see "Modern Developments" below).

### Spectrometer (grating-based)

A spectrometer separates light by wavelength. Standard design:
1. **Slit**: defines a sharp input line of light.
2. **Collimating lens**: makes the light parallel.
3. **Diffraction grating**: separates wavelengths by sending each at a different angle ($d \sin\theta = m\lambda$).
4. **Focusing lens (or imaging spectrograph)**: focuses each wavelength to a different position on the detector.

**Resolving power:**
$$R = \frac{\lambda}{\Delta\lambda} = mN$$
where $m$ is the diffraction order and $N$ is the number of lines on the grating.

For a 2 cm grating with 1200 lines/mm: $N = 24{,}000$. In first order: $R = 24{,}000$. At $\lambda = 500$ nm: $\Delta\lambda = 500/24{,}000 = 0.02$ nm — easily resolves the sodium doublet at 589.0 / 589.6 nm.

### The human eye

The eye is a two-element optical system: cornea + crystalline lens.

- **Cornea**: refractive index ~1.376, mostly responsible for the eye's refraction. Fixed.
- **Crystalline lens**: refractive index ~1.41, variable. The ciliary muscles change its shape (accommodation). Relaxed = flat = distant focus; contracted = more curved = near focus.
- **Retina**: the detector. Rod cells (low light, no color) and cone cells (color, daylight). Density at the fovea (the center of the retina, where vision is sharpest): ~150,000 cones/mm² — corresponding to an angular density of ~1 arcminute per cone.

The eye's angular resolution: about 1 arcminute (60 arcseconds). The Rayleigh criterion for the eye's ~3 mm pupil at $\lambda = 550$ nm: ~0.5 arcminute. So the eye's resolution is slightly *worse* than the diffraction limit — the limiting factor is the retina's cone density, not the optics.

**Common vision defects:**

- **Myopia (nearsightedness)**: Eye is too long; far point < ∞. Distant objects don't focus on the retina (the image forms in front of it). Corrected by a *diverging* lens that shifts the image back. Power: $P = -1/d$, where $d$ is the far point.

- **Hyperopia (farsightedness)**: Eye is too short. Near objects don't focus (image forms behind retina). Near point > 25 cm. Corrected by a *converging* lens. Power: depends on the specific near-point distance and the desired near point.

- **Presbyopia**: Age-related stiffening of the crystalline lens. Accommodation range shrinks. Near point recedes. Corrected by *reading glasses* (converging) or progressive (multifocal) lenses.

- **Astigmatism**: The cornea or lens is not rotationally symmetric — has different curvatures in different meridians. Causes blurred vision in some directions. Corrected by *cylindrical* lenses.

### Aberrations in real instruments

Every real optical instrument has aberrations. The main ones:

- **Spherical aberration**: rays at different heights focus at slightly different points. Reduced by aspheric lens designs.
- **Chromatic aberration**: different wavelengths focus at different points (because $n$ varies with wavelength). Reduced by *achromatic doublets* (one converging crown-glass lens cemented to a diverging flint-glass lens). 
- **Coma**: off-axis objects produce comet-shaped images.
- **Astigmatism**: different focal lengths in different directions.
- **Distortion**: barrel or pincushion image deformation.

High-end photographic lenses use 10+ elements to control these. Modern manufacturing (computer-aided design + precision grinding) makes complex lens designs practical.

### Modern developments

**Adaptive optics**: ground-based telescopes deform their secondary mirror in real-time (hundreds of times per second) to compensate for atmospheric turbulence. With a laser-guide star (a sodium-fluorescence point in the upper atmosphere), modern ground-based scopes approach diffraction-limited resolution from the surface of the Earth. Several research telescopes (Keck, Subaru, VLT) routinely deliver 0.05–0.1 arcsec imaging.

**Super-resolution microscopy** (Nobel 2014 to Hell, Betzig, Moerner): A class of techniques that beat the diffraction limit using *nonlinear* or *stochastic* tricks rather than just shorter wavelengths. STED, PALM, STORM are the main variants. Routinely image biological structures at ~20 nm resolution — well below the ~250 nm Abbé limit.

**Event Horizon Telescope**: a planet-wide array of radio telescopes simulating a 12,000 km aperture. Produced the first direct images of supermassive black holes (M87* in 2019, Sgr A* in 2022) at microarcsecond resolution.

---

## Worked example: telescope angular resolution

You're building a 200 mm Newtonian reflecting telescope for amateur astronomy. (a) Find the theoretical Rayleigh resolution at $\lambda = 550$ nm. (b) Can it resolve a binary star system 50 light-years away where the two stars are separated by 10 AU (1.5 × 10¹² m)?

**(a) Rayleigh resolution:**
$$\theta_{\min} = 1.22 \lambda / D = 1.22 \times (5.5 \times 10^{-7}) / 0.2 = 3.36 \times 10^{-6} \text{ rad}$$

Convert to arcseconds: $3.36 \times 10^{-6} \times (180/\pi) \times 3600 \approx 0.69$ arcsec.

**(b) Binary star separation at 50 ly.** Distance: $50$ ly $\times 9.46 \times 10^{15}$ m/ly $= 4.73 \times 10^{17}$ m.
Angular separation: $\theta = $ separation/distance $= 1.5 \times 10^{12} / 4.73 \times 10^{17} \approx 3.2 \times 10^{-6}$ rad $\approx 0.65$ arcsec.

The angular separation (0.65 arcsec) is *just below* the Rayleigh limit (0.69 arcsec). The two stars are just at — or barely past — the limit of resolution. With careful technique and good seeing conditions, you might just split them; in poor conditions, they'd merge into one.

**The lesson.** The Rayleigh limit is a quantitative criterion. Two stars at exactly the Rayleigh angle: just resolved. Below: merged. Bigger aperture brings finer resolution. To definitely resolve this binary, an 8-inch (200 mm) scope is *marginal*; a 12-inch would have it easily.

**The limit.** This is the *diffraction* limit. In practice, atmospheric seeing limits ground-based amateur telescopes to ~1 arcsec on a good night (often worse). For sub-arcsec resolution you need adaptive optics (research telescopes) or space (Hubble, JWST).

---

## Common misconceptions

**"Larger telescopes are better because they collect more light."** They do collect more light (light gathering ∝ $D^2$), but they also *resolve finer detail* (resolution ∝ $1/D$). Both effects favor large apertures.

**"Magnification is the most important specification of a telescope."** Resolution and light gathering matter more. An amateur with a poor 6-inch telescope at 600× will see less detail than the same amateur with a good 6-inch at 100× — because at 600× they're magnifying noise and atmospheric turbulence as much as image detail.

**"A microscope's resolution is set by its magnification."** It's set by the numerical aperture and wavelength (Abbé limit). Higher magnification beyond the diffraction limit just makes details bigger but no clearer ("empty magnification").

**"The Hubble Space Telescope is special because it's bigger than ground-based telescopes."** It's not — the 8 m Keck and Subaru are much bigger. Hubble's advantage is *above the atmosphere*, so it's diffraction-limited at 0.05 arcsec instead of seeing-limited at 1 arcsec.

**"The human eye is a poorly designed optical system."** The eye is the result of evolution, not engineering, but it's well-matched to its task — diffraction-limited at the cone density, color-discriminating, large dynamic range. What it isn't is a *uniformly* sharp imager; vision is sharpest at the fovea and increasingly blurry toward the periphery.

---

## Exercises

**Warm-up (Apply).** A refracting telescope has $f_{\text{obj}} = 1500$ mm and $f_{\text{eye}} = 25$ mm. Find the angular magnification. What's the minimum length of the telescope?

**Apply.** A microscope has $f_{\text{obj}} = 4$ mm, $f_{\text{eye}} = 20$ mm, and tube length $L = 160$ mm. Find the total magnification.

**Apply.** Find the Rayleigh angular resolution in arcseconds for:
- (a) 10 cm amateur scope, $\lambda = 550$ nm
- (b) 2.4 m Hubble, $\lambda = 550$ nm
- (c) 6.5 m JWST, $\lambda = 2$ µm (near-infrared, where JWST does most of its work)

**Apply + Analyze.** A spectrometer uses a grating with 600 lines/mm over 5 cm. Used in first order. (a) Find the resolving power. (b) At $\lambda = 656$ nm (hydrogen H-alpha), find the minimum $\Delta\lambda$ it can resolve. (c) Can it separate the H-alpha line from any other prominent emission line within ~1 nm of it?

**Apply (optometry).** A nearsighted person has a far point of 80 cm. (a) Find the lens power they need to see distant objects clearly. (b) For the same person, the near point is 12 cm (which is closer than normal — many myopes are also able to see very close). Find the accommodation range in diopters.

**Challenge.** Adaptive optics correct atmospheric distortion in real time. Estimate the rate at which the correction needs to update if the atmospheric "seeing" coherence time is ~10 ms and the deformable mirror has 1000 actuators arranged in a 32×32 grid. (Hint: think of how many sample points you need to track to correct a coherence-scale distortion, and at what rate.)

---

## LLM Exercises

### Build the telescope resolution simulator (`08-telescope-resolution.html`)

> **Show.** Rayleigh criterion: $\theta_{\min} = 1.22 \lambda/D$. Two stars closer than $\theta_{\min}$ appear as one merged blob; farther apart, they appear as two distinct points.
>
> **Say.** Build a telescope resolution simulator with adjustable aperture, wavelength, and star separation.
>
> **Constrain.** D3 v7. Display two Airy disk patterns separated by angular separation × focal length on a virtual focal plane. Sliders: aperture $D$ (50 mm to 500 mm), wavelength $\lambda$ (400 nm to 700 nm), star angular separation $\Delta\theta$ (0 to 5 arcseconds). Compute Rayleigh limit, display as a horizontal reference line. Render Airy disks with proper Bessel-function profile or close approximation. Filename: `08-telescope-resolution.html`.
>
> **Verify.** (a) Default $D = 100$ mm, $\lambda = 550$ nm: $\theta_{\min} \approx 1.4$ arcsec. (b) Stars at 2 arcsec: clearly resolved. (c) Stars at 0.5 arcsec: merged. (d) Doubling $D$ halves $\theta_{\min}$.

### Exploration

- Build a 100 mm scope and see what's resolvable at solar-system distances: at Saturn (distance ~9 AU), can you resolve a 1000 km feature?
- For radio interferometry simulating a planet-wide aperture: try $D = 1.2 \times 10^7$ m (Earth-sized) at $\lambda = 1.3$ mm. The resolution is the Event Horizon Telescope's ~20 µarcsec. Use this to estimate the resolved size of M87's central black hole.
- Compare scenarios: the same telescope used at the visible 550 nm vs. the near-IR at 2 µm. Resolution changes by a factor of 2/0.55 ≈ 3.6. This is why JWST gets less resolution than Hubble for the same aperture size.

### Extension prompt (chapter bridge)

> **Show.** Real telescopes use coherent laser light for some applications (LIDAR, laser-guide stars). What's special about laser light?
>
> **Say.** Build a Gaussian-beam profile visualizer.
>
> **Constrain.** Display a Gaussian beam $w(z) = w_0 \sqrt{1 + (z/z_R)^2}$ with sliders for $w_0$ and wavelength. Show beam radius vs. distance, marking the Rayleigh range $z_R$.
>
> **Verify.** Smaller waist → larger divergence beyond Rayleigh range. The waist-divergence trade-off matches diffraction.

Save as `08b-gaussian-beam-preview.html`. This is the bridge to Chapter 9.

---

## What would change my mind

The Rayleigh criterion is geometric optics + diffraction. Every test of the diffraction limit confirms it. Super-resolution techniques get below the limit by using *nonlinear* or *stochastic* methods, not by violating wave optics. A confirmed result of imaging at sub-Rayleigh resolution using purely linear, classical optics would force re-examination — none has appeared.

Aberrations are real and well-modeled by ray-tracing. The Abbé limit for microscopes is empirical and theoretical bedrock. Any sub-Abbé classical-imaging claim would shake everything; super-resolution work is *quantum* or *fluorescence-based*, not classical-linear imaging.

## Still puzzling

- *Why is the eye's resolution slightly worse than diffraction-limited?* Cone density on the retina is the limit, not the pupil. Higher cone density would mean larger photoreceptor cells (each cone is roughly diffraction-limited in its own size). Evolution made a trade-off.
- *Will super-resolution microscopy fundamentally replace classical optical microscopy?* It already has for many biological applications. Classical microscopy is faster, simpler, and good for many tasks; super-resolution is essential for sub-200 nm imaging.
- *Quantum imaging and ghost imaging.* Recent research uses entangled-photon states to image objects without conventional cameras. Whether these techniques have practical applications beyond cryptography is open.

---

**Tags:** refracting telescope, reflecting telescope, microscope, numerical aperture, Abbé limit, Rayleigh criterion, spectrometer, resolving power, human eye, adaptive optics, super-resolution

![Two side-by-side telescope optical diagrams. Newtonian: light enters from top, reflects off a parabolic primary mirror at the bottom, hits a flat secondary at 45 degrees near the top, and exits the side of the tube to...](images/08-optical-instruments-fig-01.png)
*Figure 8.1 — Reflecting Telescopes*

![Optical layout for a compound microscope. Object just outside the focal point of the objective lens. Objective forms a real inverted enlarged intermediate image at tube length L from the lens, around 160 millimeters....](images/08-optical-instruments-fig-02.png)
*Figure 8.2 — Compound Microscope*

![Optical pipeline of a grating spectrometer. Light from a sample enters through a narrow slit. A collimating lens makes it parallel. A diffraction grating splits the beam by wavelength — red, green, and violet emerge a...](images/08-optical-instruments-fig-03.png)
*Figure 8.3 — Grating Spectrometer*

![Two panels comparing fluorescence microscopy of the same biological sample. Left: classical microscopy at the Abbé diffraction limit, around 250 nanometers. Individual features blur together. Right: super-resolution m...](images/08-optical-instruments-fig-04.png)
*Figure 8.4 — Super-Resolution vs Abbé Classical Limit*

