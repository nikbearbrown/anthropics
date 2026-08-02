# Chapter 5 — Wave Optics: Interference


## TL;DR

- Light waves superpose; two beams can add to brightness — or to darkness.
- The chapter moves through Learning objectives, Opening case: the LIGO detector, Core concept, Superposition: amplitudes add, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Light waves superpose; two beams can add to brightness — or to darkness.*

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Understand)** State the superposition principle for light waves and explain that amplitudes (not intensities) add.
2. **(Apply)** Derive the conditions for constructive ($\Delta = m\lambda$) and destructive ($\Delta = (m+\frac{1}{2})\lambda$) interference from path-length difference.
3. **(Apply)** Compute fringe spacing $\Delta y = \lambda L / d$ for a two-slit experiment.
4. **(Analyze)** Apply thin-film interference to predict the colors seen in soap films and the design of anti-reflection coatings.
5. **(Understand)** Explain what coherence means and why two ordinary light bulbs cannot produce stable interference fringes.
6. **(Apply)** Build a double-slit interference pattern simulator that updates in real time with wavelength, slit separation, and screen distance.

---

## Opening case: the LIGO detector

On 14 September 2015, the two LIGO interferometers (in Hanford, Washington and Livingston, Louisiana) detected a gravitational wave from two merging black holes 1.3 billion light-years away. The detection consisted of a difference in arm length between the two perpendicular 4 km arms of about $10^{-18}$ m — *one ten-thousandth of the diameter of a proton*.

How could anyone measure such a tiny difference? The answer is *interferometry*. Laser light is split into two beams, one for each arm. Each beam reflects off a mirror at the end of the arm and returns. The two returning beams recombine, and the resulting brightness on the detector depends sensitively on the difference in path lengths.

If the two paths differ by an integer number of wavelengths, the beams add constructively and the detector sees bright. If they differ by a half-integer, they cancel and the detector sees dark. In between, the brightness varies smoothly.

A passing gravitational wave changes the arm length by a tiny amount — but enough to shift the interference pattern measurably. The 2017 Nobel Prize went to Weiss, Barish, and Thorne for this detection. The chapter's physics — wave superposition, path-length difference, constructive and destructive interference — is the same physics LIGO uses, scaled to extraordinary precision.

---

## Core concept

### Superposition: amplitudes add

When two light waves arrive at the same point in space, the total electric field is the *vector sum* of the individual fields:
$$\vec{E}_{\text{total}} = \vec{E}_1 + \vec{E}_2$$

The total *intensity* is proportional to $|\vec{E}_{\text{total}}|^2$, which is *not* the sum of $|\vec{E}_1|^2$ and $|\vec{E}_2|^2$. Cross terms appear; these are the *interference terms*.

For two scalar waves of equal amplitude $E_0$ at the same frequency:
$$E_1 = E_0 \cos(\omega t), \quad E_2 = E_0 \cos(\omega t + \phi)$$
$$E_{\text{total}} = E_0 [\cos(\omega t) + \cos(\omega t + \phi)] = 2 E_0 \cos(\phi/2) \cos(\omega t + \phi/2)$$

The time-averaged intensity is
$$I = \langle E^2 \rangle = 2 E_0^2 [\cos(\phi/2)]^2 = I_0 [1 + \cos\phi] = 4 I_1 \cos^2(\phi/2)$$
where $I_1$ is the intensity of each beam alone.

For $\phi = 0$: $I = 4 I_1$. Constructive interference. Brightness is *four times* a single beam, not two. The intensity is on the field-amplitude scale, not the photon-count scale.

For $\phi = \pi$: $I = 0$. Destructive interference. Total darkness.

This is the algebraic heart of wave optics: amplitudes add, and the intensity depends on the phase relationship.

### Path-length difference

When two waves travel different physical paths to reach the same point, the phase difference is determined by the difference in optical path length:
$$\Delta = $$ path 2 length $-$ path 1 length

Phase difference: $\phi = 2\pi \Delta / \lambda$.

**Constructive** when $\Delta = m\lambda$ (integer multiples): bright fringes.

**Destructive** when $\Delta = (m + \frac{1}{2})\lambda$ (half-integer): dark fringes.

This single relationship — path-length difference in wavelengths, decoding to bright or dark — governs every interference phenomenon: double-slit, thin films, Michelson interferometer, gratings.

### Young's double-slit experiment (1801)

Two narrow slits, separated by distance $d$, illuminated by a single coherent source (or each by light from the same point source for spatial coherence). A screen at distance $L$ ($L \gg d$).

For a point on the screen at angular position $\theta$ from the perpendicular bisector of the slits, the path-length difference is approximately
$$\Delta = d \sin\theta$$

(Small-angle approximation: $\sin\theta \approx \tan\theta = y/L$, where $y$ is the linear distance from the screen center.)

**Bright fringes:** $d \sin\theta = m\lambda$, equivalently $y = m\lambda L / d$.

**Dark fringes:** $d \sin\theta = (m + \frac{1}{2})\lambda$.

**Fringe spacing:** $\Delta y = \lambda L / d$.

For $\lambda = 550$ nm, $d = 0.1$ mm, $L = 1$ m: $\Delta y = 5.5$ mm. Visible to the eye.

**Source:** Young, T. "An Account of Some Cases of the Production of Colours, not Hitherto Described." Phil. Trans. R. Soc. 92, 387 (1802).

### Intensity formula for two slits

If the two slits emit waves of equal amplitude:
$$I(\theta) = I_0 \cos^2\left(\frac{\pi d \sin\theta}{\lambda}\right)$$

This is the *interference factor*. For a real double-slit with slits of finite width, you also get a *diffraction envelope* (Chapter 6) that modulates this oscillation.

### Thin-film interference

A thin transparent film (soap film, oil slick, anti-reflection coating) has two reflecting surfaces — the top and the bottom of the film. Light that reflects off the top surface superposes with light that *transmits* through the top, reflects off the bottom, and *transmits* back out through the top.

The two reflected waves have a path-length difference of approximately $2nt$ (twice the film thickness times the index of the film), where $n$ is the film's refractive index.

There are also *phase shifts on reflection*: when a wave reflects off a *denser* medium (higher $n$ than what it's coming from), it gets a $\pi$ phase shift; off a *less dense* medium, no shift. For a soap film in air:
- Top surface (air-to-water reflection): $\pi$ shift.
- Bottom surface (water-to-air reflection): no shift.

Net phase shift between the two reflected waves: $\pi$. Combining the path-length difference with the phase shift:

**Constructive (bright) reflection:** $2nt = (m + \frac{1}{2})\lambda$ for $m = 0, 1, 2, ...$

**Destructive (dark) reflection:** $2nt = m\lambda$.

The interference is wavelength-dependent: a single thickness selects which wavelengths brighten in reflection and which darken. Different thicknesses across a non-uniform film produce the rainbow colors of soap bubbles and oil slicks.

**Anti-reflection coatings.** A thin coating ($n_{\text{coat}}$) on a glass lens ($n_{\text{glass}}$) is chosen so that:
- Reflections from top and bottom of the coating cancel destructively.
- For an air-to-coating-to-glass system, both reflections gain $\pi$ phase shifts (both at denser interfaces). Path difference: $2 n_{\text{coat}} t$. For destructive interference: $2 n_{\text{coat}} t = (m + \frac{1}{2})\lambda$.
- For best results, $n_{\text{coat}} = \sqrt{n_{\text{glass}}}$. For glass $n = 1.5$, the ideal coating has $n = 1.22$.

Modern lenses have multi-layer anti-reflection coatings reducing reflection from ~4% per surface (uncoated) to < 0.5% per surface. This is why high-end camera lenses look almost invisible from the front.

### The coherence requirement

For interference fringes to be observable, the two sources must be **coherent** — they must have a stable phase relationship over the time of observation.

**Temporal coherence** (Chapter 9): how long the phase relation remains predictable. A monochromatic source has long temporal coherence; broadband (like a thermal source) has short. For interference fringes, the path-length difference must be less than the **coherence length** $\ell_c = c \tau_c$.

**Spatial coherence**: how the phase varies across the wavefront. Light from a single point source is spatially coherent; light from an extended source (Sun, light bulb) is not — different points of the source emit independently.

Two separate light bulbs cannot produce stable interference because their phases drift independently and rapidly. A single laser, or two beams derived from the same source (via a beam splitter or two slits illuminated by one source), gives coherent beams.

### The Michelson interferometer

A laser beam is split into two by a half-silvered mirror. Each beam travels to a mirror, reflects, and returns. The two returning beams recombine at the half-silvered mirror; the recombined beam goes to a detector.

If the two arms have lengths $L_1$ and $L_2$, the path-length difference between the two recombined beams is $2(L_1 - L_2)$.

Detector intensity: $I = I_0 \cos^2(2\pi (L_1 - L_2)/\lambda)$.

By changing one arm's length, you walk through the interference pattern. The Michelson interferometer was the device Michelson and Morley used in 1887 to look for "ether drift" — and got a null result that contributed to Einstein's 1905 paper.

LIGO is the modern descendant: 4 km arms, laser power buildup in resonant cavities, and the most precise displacement measurement ever made.

---

## Worked example: soap film

A soap film $(n = 1.34)$ is illuminated by white light. Looking at one spot on the film, you see a strong reflection of *green* light ($\lambda = 550$ nm in air). Find the thinnest film that can produce this.

**Conditions.** Air-to-water reflection at top: $\pi$ phase shift. Water-to-air reflection at bottom: no phase shift. Net phase shift between the two reflected waves: $\pi$.

For constructive interference in reflection, the path-length difference must compensate the phase shift:
$$2 n t = (m + \tfrac{1}{2})\lambda$$
with $m = 0$ for the thinnest case:
$$2 (1.34) t = (1/2)(550 \text{ nm})$$
$$t = 275 / (2 \times 1.34) = 102.6 \text{ nm}$$

The thinnest soap film that produces a green reflection is about 103 nm — roughly a fifth of a wavelength of green light.

**The lesson.** Thin-film thickness, on the order of 100 nm, selects a visible color. Films thinner than a quarter-wavelength can also produce *destructive* interference in reflection, where the film essentially disappears. (Anti-reflection coatings exploit this.)

**The limit.** This works for normal incidence. At oblique angles, the path difference increases by a factor of $1/\cos\theta_{\text{transmit}}$, which shifts the colors. That's why a soap bubble shows different colors at different angles. The chapter's formula is the leading-order approximation.

---

## Common misconceptions

**"Interference destroys energy."** No. Energy is conserved. Where the bright fringes appear, the light gets brighter than the single-beam intensity would predict; where the dark fringes appear, the light is darker. The total integrated over the screen equals what you'd get from two independent sources. The interference moves the energy around in space, doesn't destroy it.

**"Any two light sources will interfere."** Only coherent sources produce *stable* fringes. Two independent sources (two flashlights, two LEDs) average out the phase relationship — the fringes are there momentarily, but they shift and blur so fast no detector can see them.

**"Thin film colors are due to absorption."** No, they're from interference. A soap film is nearly transparent; the colors come from constructive interference in the reflected light at specific wavelengths.

**"The Michelson-Morley experiment proved the speed of light is constant."** It showed the speed of light is the same in different reference frames (no ether drift); this was a major step toward special relativity. But the experimental result was technical — a null observation that gave Einstein motivation, not a direct proof.

**"Light bulbs are incoherent because their bulbs are hot."** Thermal radiation has many independent emitters at many phases. Coherence is reduced because the source is extended (each emitter is at a different position, partial spatial decoherence) and because each emission has a random phase (temporal decoherence). The temperature is incidental.

---

## Exercises

**Warm-up (Apply).** A double-slit experiment uses $\lambda = 633$ nm (red HeNe laser), $d = 0.2$ mm, and a screen at $L = 1$ m. Find the fringe spacing.

**Apply.** Two coherent sources separated by 1 mm illuminate a screen 2 m away. For green light ($\lambda = 550$ nm), find: (a) angular position of the 3rd bright fringe (small angle), (b) linear position on the screen.

**Apply.** A soap film has $n = 1.33$. White light illuminates it. (a) Find the thinnest film that gives constructive reflection for $\lambda = 480$ nm (blue). (b) For the same thickness, is the reflection for $\lambda = 640$ nm (red) constructive, destructive, or in between?

**Apply + Analyze.** A glass lens ($n = 1.52$) has an anti-reflection coating ($n_{\text{coat}} = 1.38$). For minimum reflection at $\lambda = 550$ nm (green), find the minimum coating thickness. (Hint: both reflections get $\pi$ phase shifts because both interfaces are denser-than-the-medium-above; you need destructive interference between the two reflected waves.)

**Apply (Michelson).** A Michelson interferometer is illuminated by light of $\lambda = 633$ nm. One mirror is slowly moved 5 µm. How many bright-dark cycles pass the detector?

**Challenge.** Two coherent sources at slightly different frequencies $f_1, f_2$ illuminate a fixed point. Show that the intensity at that point oscillates in time at the *difference frequency* $f_1 - f_2$. This is the "beat note" effect; it's how optical heterodyne detection works.

---

## LLM Exercises

### Build the double-slit interference simulator (`05-double-slit.html`)

> **Show.** Two-slit interference: intensity $I(\theta) = I_0 \cos^2(\pi d \sin\theta / \lambda)$. Fringe spacing $\Delta y = \lambda L / d$.
>
> **Say.** Build an interactive double-slit interference simulator.
>
> **Constrain.** D3 v7. Display two slits on the left of the canvas, screen on the right. Sliders: wavelength $\lambda$ (400–700 nm, color-mapped), slit separation $d$ (0.05 mm to 1 mm), screen distance $L$ (50 cm to 5 m), number of slits $N$ (2 to 10 — multi-slit/grating mode). Compute intensity pattern $I(y)$ on the screen using the appropriate formula for $N$ slits. Render as a vertical color band (intensity → brightness, hue → wavelength). Overlay the analytical formula as a dashed line plot. Display computed fringe spacing. Animate wavefronts emerging from each slit. Filename: `05-double-slit.html`.
>
> **Verify.** (a) Doubling $\lambda$ doubles fringe spacing. (b) Doubling $d$ halves fringe spacing. (c) Increasing $N$ from 2 to 10 makes the principal maxima sharper (grating regime).

### Exploration

- Set $d = 0.1$ mm, $\lambda = 550$ nm, $L = 1$ m. Measure the predicted fringe spacing. Verify with the displayed formula.
- Set $N = 5$. The principal maxima are at the same angles as for the two-slit case, but they're much sharper. Why? (Answer: more slits means more contributions, so the destructive zeros in between are deeper.)
- Try $\lambda = 633$ nm (red HeNe laser). Compare fringe spacing to $\lambda = 405$ nm (violet diode laser). Red fringes are about 1.6× wider than violet.

### Extension prompt (chapter bridge)

> **Show.** Interference happens between waves from multiple sources. *Diffraction* is interference of waves from a single, finite-width aperture.
>
> **Say.** Build a single-slit diffraction pattern simulator.
>
> **Constrain.** Single slit of width $a$, illuminated by light of wavelength $\lambda$. Display intensity pattern $I(\theta) = I_0 [\sin(\pi a \sin\theta / \lambda) / (\pi a \sin\theta / \lambda)]^2$.
>
> **Verify.** Narrower slit → wider central maximum. First dark fringe at $a \sin\theta = \lambda$.

Save as `05b-single-slit-preview.html`. This is the bridge to Chapter 6.

---

## What would change my mind

Wave optics rests on the superposition principle — amplitudes add — which is a direct consequence of Maxwell's equations being linear. A confirmed deviation from superposition in linear media would force a fundamental rewriting. None has been observed. Nonlinear optics is a real and rich field (frequency doubling, the laser itself relies on it), but the nonlinearity is in the medium's response, not in the underlying equations.

Thin-film interference is exact in the appropriate geometry. Anti-reflection coatings are designed and manufactured precisely on the basis of this physics; every camera lens, eyeglass coating, and reflective-medium engineering project confirms the predictions empirically.

## Still puzzling

- *What is "the" phase of a light wave?* For a single classical wave, phase is well-defined. For light from a thermal source (broadband, multiple independent emitters), phase varies rapidly and randomly. Coherence quantifies how much.
- *How does interference work for single photons?* Each photon makes a dot on the screen. The accumulated pattern is the interference pattern. Each photon "interferes with itself" — but only in the statistical sense. The deep version is in Chapter 10.
- *Anti-reflection coatings and the wavelength they're optimized for.* They reduce reflection at one specific wavelength (typically green for camera lenses). At other wavelengths, the reduction is partial. Multi-layer coatings extend the reduction across the visible spectrum but never completely eliminate reflections everywhere. There's a fundamental trade-off in coating design.

---

**Tags:** interference, superposition, Young's experiment, double slit, path length difference, thin film, anti-reflection coating, coherence, Michelson interferometer, LIGO

![Three stacked panels showing two sinusoidal waves at different phase relationships. In phase: sum has double the amplitude, intensity is four times that of one beam. Quadrature: sum has intermediate amplitude. Out of...](images/05-interference-fig-01.png)
*Figure 5.1 — Wave Superposition*

![Schematic of Young's 1801 experiment. A laser source on the left passes through a single slit, then through a double slit separated by distance d. Rays from the two slits travel to a screen at distance L. The path-len...](images/05-interference-fig-02.png)
*Figure 5.2 — Young's Double-Slit*

![Cross-section of a thin soap film of thickness t and index 1.34, with air above and below. A light ray incident from the upper left partially reflects at the top surface with a pi phase shift (denser interface) and pa...](images/05-interference-fig-03.png)
*Figure 5.3 — Thin-Film Interference*

![Schematic of a Michelson interferometer. A laser enters from the left and hits a half-silvered beam splitter at 45 degrees. The beam splits into two perpendicular arms with mirrors at the ends. Both beams reflect back...](images/05-interference-fig-04.png)
*Figure 5.4 — Michelson Interferometer*

![Two panels. Left: temporal coherence. A laser produces a long, continuous wave train with stable phase, long coherence length. A thermal source produces short wave packets with random phase between packets, short cohe...](images/05-interference-fig-05.png)
*Figure 5.5 — Coherence*

