# Chapter 2 — Reflection and Refraction


## TL;DR

- The law of reflection, Snell's law, and the cleanest demo of Fermat's principle.
- The chapter moves through Learning objectives, Opening case: fiber-optic cable, Core concept, The law of reflection, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The law of reflection, Snell's law, and the cleanest demo of Fermat's principle.*

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Apply)** Use the law of reflection ($\theta_r = \theta_i$) to predict reflected-ray directions for any incident geometry.
2. **(Apply)** Apply Snell's law $n_1 \sin\theta_1 = n_2 \sin\theta_2$ to compute refraction angles at any interface.
3. **(Apply)** Compute the critical angle for total internal reflection given two indices.
4. **(Analyze)** Predict the direction of bending qualitatively (toward or away from normal) given the relative indices of the two media.
5. **(Apply)** Compute Brewster's angle for a given pair of indices and explain why reflected light at $\theta_B$ is fully polarized.
6. **(Apply)** Build a refraction simulator showing incident, reflected, and refracted rays with total-internal-reflection mode.

---

## Opening case: fiber-optic cable

A single strand of optical fiber, about the thickness of a human hair, runs from your phone's WiFi router, across your town, across an ocean floor, and into the laptops of people in another hemisphere. Inside the fiber, light travels by *total internal reflection* — bouncing off the boundary between the dense glass core and the slightly less-dense glass cladding at every fraction of a millimeter, never escaping, never absorbed (much), for tens of kilometers between optical amplifiers.

Why doesn't the light leak out? The answer is one inequality and one law. The inequality: the light's angle of incidence at the core-cladding boundary exceeds the *critical angle*. The law: above the critical angle, Snell's law has no solution for the transmitted ray — and all the light is reflected back into the core.

Fiber optics built modern telecommunications. Charles Kao's 1966 paper proposing it earned him the 2009 Nobel Prize. Every internet packet you send rides on the physics this chapter teaches.

---

## Core concept

### The law of reflection

When a ray hits a smooth surface, the angle of reflection equals the angle of incidence (both measured from the normal to the surface):

$$\theta_r = \theta_i$$

Both rays and the normal lie in a single plane (the *plane of incidence*).

The law applies to specular (smooth) reflection. For a rough surface, the same law applies *at each microscopic facet*; the macroscopic result is diffuse reflection in many directions.

The law of reflection has the same form whether the surface is a flat mirror, a curved mirror, or any local element of a curved surface — the local normal determines the reflection geometry. Chapter 3 uses this to derive image formation by curved mirrors.

### Snell's law of refraction

When a ray crosses from medium 1 (index $n_1$) into medium 2 (index $n_2$), the transmitted (refracted) ray obeys:

$$n_1 \sin\theta_1 = n_2 \sin\theta_2$$

Both angles measured from the normal. The incident, reflected, and refracted rays all lie in the plane of incidence.

**Direction of bending.** From a less-dense to a denser medium ($n_2 > n_1$): the ray bends *toward* the normal ($\theta_2 < \theta_1$). From dense to less dense: bends *away* from the normal.

**Source:** Snell's law was empirically discovered by Ibn Sahl (~984 CE), independently by Willebrord Snell (1621), and given the famous derivation via Fermat's principle of least time by Pierre de Fermat (1662). 

### Fermat's principle

Light travels from one point to another along the path that *minimizes the optical path length* — the integral of $n \, d\ell$ along the path:

$$\delta \int n \, d\ell = 0$$

Or, since optical path length / $c$ is travel time: light takes the path of *least travel time* (more precisely, the path of stationary time — minimum or saddle point).

**Why this gives Snell's law.** Two media with indices $n_1, n_2$ separated by a flat boundary. A ray must go from point A in medium 1 to point B in medium 2. The travel time is
$$t = \frac{L_1}{c/n_1} + \frac{L_2}{c/n_2} = \frac{n_1 L_1 + n_2 L_2}{c}$$
where $L_1, L_2$ are the path lengths in each medium. Minimize over the location where the ray crosses the boundary: set $dt/dx = 0$ where $x$ is the boundary-crossing point. The result is exactly $n_1 \sin\theta_1 = n_2 \sin\theta_2$.

Fermat's principle generalizes beautifully: for curved interfaces, anisotropic media, and even general relativity (light follows geodesics in spacetime, which is the optical-path version of Fermat in a curved metric). For intro purposes, the simple two-medium case is the lesson.

### Total internal reflection

From a denser medium $n_1$ to a less-dense medium $n_2 < n_1$ (e.g., glass to air): there's a *critical angle* beyond which Snell's law gives $\sin\theta_2 > 1$, which is impossible. No transmitted ray exists; *all* the light reflects back into the dense medium.

The critical angle:
$$\sin\theta_c = \frac{n_2}{n_1}$$

For glass-to-air ($n_1 = 1.5$, $n_2 = 1.0$): $\theta_c = \arcsin(2/3) \approx 41.8°$.

For water-to-air ($n_1 = 1.33$): $\theta_c \approx 48.6°$.

Total internal reflection is the operating principle of:
- **Optical fibers**: light entering at appropriate angle reflects off the core-cladding boundary repeatedly.
- **Prisms in binoculars**: a single prism replaces multiple mirrors with no metallic reflective losses.
- **Diamond brilliance**: high index of refraction ($n = 2.42$) gives a critical angle of only 24°, so most internal light reflects back rather than escaping — making diamonds sparkle.

### Dispersion

The refractive index depends slightly on wavelength: $n = n(\lambda)$. Blue light has a higher index in most materials, so it bends *more* than red light at any interface.

In a glass prism, this separates white light into a spectrum (red on one side, violet on the other). This is the physics of the rainbow: water droplets refract sunlight, internal-reflect it once, refract it again on exit; different wavelengths bend by different amounts, separating the colors.

Cauchy's empirical equation: $n(\lambda) = A + B/\lambda^2$. For ordinary glass: $A \approx 1.5$, $B \approx 0.01\,\mu\text{m}^2$.

### Brewster's angle

At one specific angle of incidence — **Brewster's angle**:
$$\tan\theta_B = \frac{n_2}{n_1}$$
the reflected ray is *completely polarized*. Specifically, the reflected light is fully *s-polarized* (perpendicular to the plane of incidence); the p-polarized component is entirely transmitted.

For glass at $n = 1.5$: $\theta_B \approx 56.3°$. This is why polarizing sunglasses work — they're oriented to block horizontally-polarized glare reflected off horizontal surfaces (water, road) at angles near Brewster's. We return to polarization in Chapter 7.

---

## Worked example: a fiber-optic cable

A multimode optical fiber has a glass core with $n_{\text{core}} = 1.62$ and cladding with $n_{\text{clad}} = 1.52$. (a) Find the critical angle at the core-cladding boundary. (b) Find the acceptance angle — the maximum angle (from the fiber's axis) at which light entering the end face will be guided.

**(a) Critical angle.**
$$\sin\theta_c = n_{\text{clad}} / n_{\text{core}} = 1.52 / 1.62 = 0.938$$
$$\theta_c = \arcsin(0.938) \approx 69.8°$$

So if light inside the core hits the cladding boundary at an angle of incidence > 69.8°, it totally internally reflects.

**(b) Acceptance angle.** Light entering the end face of the fiber refracts (air-to-core boundary) and then travels at some angle inside the core. For total internal reflection to occur at every subsequent core-cladding bounce, the *angle inside the core from the axis* must be less than $90° - \theta_c = 20.2°$.

Applying Snell's law at the end face: $n_{\text{air}} \sin\theta_{\text{accept}} = n_{\text{core}} \sin(20.2°)$
$$\sin\theta_{\text{accept}} = 1.62 \cdot 0.346 = 0.561$$
$$\theta_{\text{accept}} \approx 34.1°$$

Light entering the fiber's end face within 34° of the axis will be guided. Light entering at greater angles escapes through the cladding. This 34° is the *numerical aperture* of the fiber.

**The lesson.** Snell's law at the air-core boundary plus the critical-angle inequality at the core-cladding boundary together determine which light propagates. The acceptance angle is the product of both — it's why fibers are designed with very specific core-cladding index differences.

**The limit.** This is the geometric-optics treatment. Real fiber-optic communication uses *single-mode* fibers (core ~9 µm) where wave-optics effects (modes of the cylindrical wave equation) dominate. The geometric picture works for thicker multimode fibers (core ~50 µm) and as a conceptual foundation.

---

## Common misconceptions

**"Light always bends toward the normal."** It bends toward the normal only when entering a denser medium ($n_2 > n_1$). Going from glass to air, it bends *away* from the normal.

**"Total internal reflection requires a mirror."** It requires only that the angle exceed the critical angle at a dense-to-less-dense interface. No mirror is involved.

**"At Brewster's angle, all the light is reflected."** No — at Brewster's angle, all the *p-polarized* light is transmitted, and only the s-polarized component is reflected. Most of the light still refracts; just one polarization is filtered out from the reflection.

**"Snell's law was discovered by Snell."** Ibn Sahl had the relation roughly 600 years earlier (~984 CE in Baghdad). The Western attribution is the historical convention; the discovery was multiple times.

**"Refraction means the light is slowing down."** True — speed drops to $c/n$. But the *frequency* stays the same (set by the source). The wavelength inside is $\lambda/n$, shorter.

---

## Exercises

**Warm-up (Apply).** Light at 30° from the normal in air hits a smooth water surface ($n = 1.33$). (a) Find the refracted angle in the water. (b) Find the reflected angle.

**Apply.** A glass slab ($n = 1.52$) with parallel faces is illuminated by light at 40° from the normal. (a) Find the refraction angle on entry. (b) Find the angle inside as the ray travels across the slab. (c) Show that the ray exits the slab parallel to the original ray (just offset).

**Apply.** Find the critical angle for total internal reflection at the boundaries: (a) water-to-air, (b) glass-to-air with $n = 1.5$, (c) glass-to-water with $n_{\text{glass}} = 1.5$.

**Apply + Analyze.** White light enters a glass prism (apex angle 60°) at angle of incidence 50°. Use $n_{\text{red}} = 1.515$, $n_{\text{violet}} = 1.532$. Find the angular separation between the red and violet rays after exiting the prism.

**Challenge.** Derive Snell's law from Fermat's principle of least time. Setup: point A in medium 1 (index $n_1$), point B in medium 2 (index $n_2$), interface in between. Vary the crossing point and set the derivative of total travel time to zero.

---

## LLM Exercises

### Build the refraction simulator (`02-refraction.html`)

> **Show.** Snell's law: $n_1 \sin\theta_1 = n_2 \sin\theta_2$. Total internal reflection when $n_1 > n_2$ and $\theta_1 > \theta_c$.
>
> **Say.** Build an interactive refraction simulator showing incident, reflected, and refracted rays.
>
> **Constrain.** D3 v7. Horizontal interface in the middle of the canvas. Top half: medium 1 with slider for $n_1$ (1 to 2.5). Bottom half: medium 2 with slider for $n_2$. Slider for angle of incidence $\theta_1$ (0 to 89°). Render: incident ray (orange, above interface), reflected ray (blue, above), refracted ray (green, below — *or* disappears with a visual flash when TIR occurs). Numerical readouts: $\theta_1$, $\theta_2$ (or "TIR" if total internal reflection), $\theta_c$ if $n_1 > n_2$. Filename: `02-refraction.html`.
>
> **Verify.** (a) Air-to-glass at 30°: refracted ray bends toward the normal. (b) Glass-to-air at $\theta_1 > \theta_c$: refracted ray disappears, all light reflected. (c) Brewster's angle: at $\theta_1 = \arctan(n_2/n_1)$, reflected and refracted rays are perpendicular to each other (verify by inspection).

### Exploration

- Find the critical angle for the simulator's default $n_1 = 1.5, n_2 = 1.0$. Verify by setting $\theta_1$ just below and just above.
- Add a "dispersion mode" that shows three rays (red, green, violet) bending by different amounts because $n$ depends on wavelength.
- At what angle of incidence (for air-to-glass) does the reflected ray become *completely* polarized? (Answer: Brewster's angle.)

### Extension prompt (chapter bridge)

> **Show.** Snell's law tells me how a single ray bends. A curved mirror redirects *many* rays from one point to another.
>
> **Say.** Build a curved-mirror ray tracer (concave/convex).
>
> **Constrain.** Mirror drawn as a curved arc. Object as an arrow on the optical axis. Three principal rays traced from the top of the object: (1) parallel to axis → reflects through focal point; (2) through focal point → reflects parallel; (3) through center of curvature → reflects straight back. Sliders for focal length and object distance.
>
> **Verify.** Object outside focal length: real, inverted image. Inside focal length: virtual, upright, enlarged image.

Save as `02b-curved-mirror-preview.html`. This is the bridge to Chapter 3.

---

## What would change my mind

Snell's law is one of the most precisely measured laws in physics. From the experimental side it has been tested to extraordinary precision, including in cases where the speed of light in a medium has been measured directly. A confirmed deviation at any tested wavelength would force the rewriting of much of the optics curriculum. None exists. Variations of refractive index near absorption bands or in *active* media (laser gain media, near-resonance) are real and well-modeled by the dispersion relation $n(\omega)$. These are corrections to the simple Snell's-law geometry, not falsifications.

## Still puzzling

- *Why does refractive index depend on wavelength?* Dispersion arises from atomic resonances at higher frequencies; the classical Lorentz oscillator model gives a derivation but ultimately the answer lives in quantum electrodynamics.
- *What's happening "inside" the boundary?* The classical wave picture treats the boundary as a sharp discontinuity. In reality, the field inside the boundary region (subwavelength) involves rapid spatial variation; the textbook answer (Snell's law) emerges from the appropriate boundary conditions on the fields. Beautiful, beyond intro scope.
- *Total internal reflection isn't quite total.* At a glass-air boundary above the critical angle, an *evanescent wave* (exponentially decaying into the less-dense medium) carries no net energy but exists. Frustrated total internal reflection — bringing another piece of glass within a wavelength — *does* let light through. The chapter's geometric-optics picture is a leading-order approximation.

---

**Tags:** law of reflection, Snell's law, Fermat's principle, total internal reflection, critical angle, optical fiber, dispersion, Brewster's angle, refractive index

![Three-panel comparison of light at an interface. Panel A: light entering a denser medium bends toward the normal, refracted angle less than incident. Panel B: light leaving a denser medium bends away from the normal,...](images/02-reflection-refraction-fig-01.png)
*Figure 2.1 — Snell's Law*

![Longitudinal cross-section of an optical fiber. A central core of refractive index 1.62 is surrounded by cladding of index 1.52, so the critical angle is 70 degrees. A light ray enters from the left within the accepta...](images/02-reflection-refraction-fig-02.png)
*Figure 2.2 — Fiber Optic*

![A triangular glass prism with apex up sits at the center of the figure. White light enters the left face, the wavelengths bend by slightly different amounts because the refractive index depends on wavelength, and a sp...](images/02-reflection-refraction-fig-03.png)
*Figure 2.3 — Prism Dispersion*

![Geometric diagram of light traveling from point A in a less dense medium to point B in a denser medium. Three candidate paths are shown crossing the boundary at different points. The optimal path is in orange — the on...](images/02-reflection-refraction-fig-04.png)
*Figure 2.4 — Fermat's Principle*

![Geometric diagram of light hitting a glass surface at the Brewster angle of 56.3 degrees. The incident ray contains both s-polarization perpendicular to the plane of incidence (shown as dots) and p-polarization in the...](images/02-reflection-refraction-fig-05.png)
*Figure 2.5 — Brewster's Angle*

