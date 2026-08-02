# Chapter 4 — Lenses and Image Formation


## TL;DR

- Converging and diverging lenses; two-lens systems; the foundation of every camera, eye, and telescope.
- The chapter moves through Learning objectives, Opening case: the eye that doesn't focus, Core concept, Converging and diverging lenses, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Converging and diverging lenses; two-lens systems; the foundation of every camera, eye, and telescope.*

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Apply)** Use the thin-lens equation $1/f = 1/d_o + 1/d_i$ to predict image positions for any object placement.
2. **(Apply)** Use the lensmaker's equation $1/f = (n-1)[1/R_1 - 1/R_2]$ to find the focal length of a lens given its geometry and material.
3. **(Apply)** Trace the three principal rays through a thin lens to construct images graphically.
4. **(Apply)** Compute the image of an object through a two-lens system by using the first lens's image as the second lens's object.
5. **(Understand)** Identify the major lens aberrations (spherical, chromatic) and explain how they limit real lens performance.
6. **(Apply)** Build a two-lens ray tracer simulating any combination of converging and diverging lenses.

---

## Opening case: the eye that doesn't focus

A 50-year-old who was nearsighted in her teens now wears reading glasses on top of her distance prescription. She is *also* presbyopic — her crystalline lens has stiffened and can no longer accommodate to focus on near objects. Her optical system is too long for distance (corrected by a diverging lens) and too short for near reading (corrected by a converging "add" in the lower part of progressive lenses). Two different corrections for two different distances, in the same eye, made possible by understanding how lens systems compose.

The optometrist who prescribes her lenses is computing image distances and powers using exactly the equations of this chapter. The mathematics behind your glasses, every camera, every microscope, and every telescope are these few lines of algebra.

---

## Core concept

### Converging and diverging lenses

A **converging (convex) lens** is thicker in the middle than at the edges. Parallel rays passing through it converge to the focal point F on the other side. Focal length $f > 0$.

A **diverging (concave) lens** is thinner in the middle. Parallel rays passing through it appear to diverge from a focal point on the *same side as the incident rays*. Focal length $f < 0$.

The lens has two focal points, one on each side, at equal distances $|f|$ from the lens (assuming the same medium on both sides — typically air).

### The thin-lens equation

For a thin lens (one whose thickness is small compared to the radii of curvature of its surfaces), the **thin-lens equation** is

$$\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i}$$

Sign conventions:
- $d_o > 0$: object on the incoming side of the lens (the usual case)
- $d_i > 0$: image on the *outgoing* side (real image, on the opposite side of the lens from the object)
- $d_i < 0$: image on the *incoming* side (virtual image, on the same side as the object)
- $f > 0$: converging lens
- $f < 0$: diverging lens

Magnification:
$$m = -\frac{d_i}{d_o}$$

Same as for mirrors — the structure is the same. Different sign convention details (whether $d_i$ positive means in front or behind) but the algebra is identical.

### The three principal rays

For a thin lens, three rays from a point on the object construct the image:

1. **Parallel ray.** Travels parallel to the optical axis. After the lens: passes through the *far* focal point (converging) or appears to come from the *near* focal point (diverging).
2. **Center ray.** Passes through the optical center of the lens. Undeviated (no bending).
3. **Focal ray.** Passes through the *near* focal point on the way in. After the lens: emerges parallel to the optical axis.

Any two locate the image; the third confirms. The simulation traces all three.

### The lensmaker's equation

For a thin lens made of material with refractive index $n$ (relative to the surrounding medium, typically air), with two curved surfaces of radius of curvature $R_1$ (facing the incoming light) and $R_2$ (facing the outgoing light):

$$\frac{1}{f} = (n - 1)\left[\frac{1}{R_1} - \frac{1}{R_2}\right]$$

Sign conventions for radii: $R > 0$ if the center of curvature is on the *outgoing* side of the lens; $R < 0$ if on the *incoming* side. A biconvex lens has $R_1 > 0$ and $R_2 < 0$; both terms add, making $1/f$ large and positive. A biconcave lens has $R_1 < 0$ and $R_2 > 0$; both terms add negatively, making $1/f$ negative.

The lensmaker's equation connects the lens's *geometry* and *material* to its focal length. Glass lenses (n = 1.5) need more curvature than diamond lenses (n = 2.42) for the same focal length, but no one makes glasses of diamond.

### Two-lens systems

The whole point of multiple lenses. The procedure:

1. Apply the thin-lens equation to **lens 1** with the original object: find $d_{i1}$ and $m_1$.
2. The image of lens 1 becomes the *object for lens 2*. Object distance for lens 2: $d_{o2} = d_{12} - d_{i1}$, where $d_{12}$ is the separation between the lenses.
3. Apply the thin-lens equation to **lens 2**: find $d_{i2}$ and $m_2$.
4. **Total magnification:** $m_{\text{total}} = m_1 \times m_2$.

This is how **microscopes** work (two converging lenses, total magnification = product), how **telescopes** work (one large converging objective + one short converging eyepiece, angular magnification), and how the human eye works (the cornea is one refracting surface, the crystalline lens is another, both contributing to the total focal length).

### Lens power

In optometry, lenses are characterized by **power**:
$$P = 1/f \text{ (in diopters, D = m}^{-1}\text{)}$$

A +2 D lens has $f = +50$ cm (converging). A −1 D lens has $f = -100$ cm (diverging). Powers add when lenses are in contact: two lenses in contact behave like one lens with $P = P_1 + P_2$.

### Lens aberrations

Real lenses depart from the thin-lens ideal in several ways:

- **Spherical aberration.** Rays at different heights focus at different points. Rays closest to the axis focus at $f$; rays at the edge focus closer. Solved by aspheric lens designs (or by stopping down the aperture).
- **Chromatic aberration.** Different wavelengths have different $n$, so different focal lengths. A *doublet* — a converging crown-glass lens cemented to a diverging flint-glass lens with carefully chosen properties — cancels much of the chromatic aberration. (Pierre Louis Guinand, c. 1800.)
- **Astigmatism, coma, distortion.** Off-axis aberrations affecting image quality for objects far from the optical axis.

Photographic lenses are designed to balance all these aberrations. Modern multi-element lens designs are engineering achievements.

### The human eye

The human eye is a two-lens system: the cornea (refractive index ~1.376, mostly responsible for refraction) and the crystalline lens (variable refractive index ~1.41, mostly responsible for accommodation — changing focal length to focus at different distances). Total focal length when relaxed: ~2.4 cm.

Near point: closest object the eye can focus on, typically 25 cm for young adults, recedes with age.
Far point: farthest object the eye can focus on. For normal vision: infinity.

Vision corrections:
- **Myopia (nearsightedness).** Eye too long; far point < ∞. Corrected by a diverging lens ($f < 0$).
- **Hyperopia (farsightedness).** Eye too short; near point > 25 cm. Corrected by a converging lens.
- **Presbyopia.** Crystalline lens stiff with age; near point recedes. Corrected by reading glasses (converging) or progressive lenses.

---

## Worked example: a Keplerian telescope

A simple refracting telescope has an *objective* lens (the front lens facing the sky) with focal length $f_1 = 500$ mm and an *eyepiece* (the lens you look through) with focal length $f_2 = 20$ mm. The two are separated by $f_1 + f_2 = 520$ mm. Find the angular magnification.

**Setup.** For a distant object at $d_o = \infty$, lens 1 (objective) forms an image at $d_{i1} = f_1 = 500$ mm (in the focal plane). This image is at distance $f_2 = 20$ mm from the eyepiece — *exactly at the eyepiece's focal point*. So the eyepiece sends out parallel rays to the eye, which the eye then focuses.

**Angular magnification.** For a telescope viewing a distant object, the angular magnification is
$$M = -\frac{f_1}{f_2} = -\frac{500}{20} = -25$$

Image appears 25× larger angularly (covers 25× the angular extent in the field of view). Negative because the image is inverted (relative to the actual object's orientation in the sky).

**The lesson.** The telescope's job is to enlarge the *angular size* of distant objects, not to form a real image at finite distance. The objective takes a distant object and images it at finite distance; the eyepiece relays that intermediate image to your eye at infinity. Two lenses, two roles, one combined system.

**The limit.** This calculation assumes the eye is at the eyepiece's exit pupil and that both lenses are paraxial. Real telescopes have spherical and chromatic aberrations, vignetting, and the eye contributes its own focal length to the system. The simple formula $M = -f_1/f_2$ is the right leading-order description for an intro telescope.

---

## Common misconceptions

**"Thicker lenses are always more powerful."** Power depends on the *curvatures* of the surfaces and the index of refraction, not on thickness. The thin-lens approximation explicitly ignores thickness. Very thick lenses must be treated as two-surface systems with their own ray tracing.

**"A diverging lens cannot form a real image."** A *single* diverging lens with a real object cannot — the image is always virtual. But in a *two-lens system* where the first lens forms a real image *behind* the second lens (i.e., $d_{o2} < 0$, a virtual object for lens 2), a diverging lens 2 *can* contribute to a real final image. The two-lens formula handles this case correctly.

**"The eye focuses by changing the shape of the cornea."** The cornea is fixed. The crystalline lens changes shape (via the ciliary muscles) — flatter for distant focus, more curved for near focus. This is *accommodation*. The cornea provides most of the eye's optical power but is not adjustable.

**"You can see your image directly *at* the focal point of a converging lens with the object far away."** What's at the focal point is the image, which is *behind* the lens from the object's side. To see it, you either project it onto a screen (real image) or look at it through an additional lens (eyepiece-style — that's the telescope geometry).

**"All lenses are made of glass."** Modern lenses can be plastic (polycarbonate, acrylic), fluorite, lithium fluoride (UV optics), zinc selenide (IR optics). Even fluid lenses (oil + water in a microfluidic cell) and liquid-crystal-based variable-focus lenses exist.

---

## Exercises

**Warm-up (Apply).** A converging lens has $f = +10$ cm. An object 15 cm away. Find $d_i$ and $m$. Move the object to 5 cm. Find $d_i$ and $m$.

**Apply.** A diverging lens with $f = -20$ cm has an object 30 cm in front. Find $d_i$. Verify the image is virtual, upright, reduced.

**Apply.** A camera has a 50 mm lens (converging, $f = 50$ mm). It is focused on an object 1 meter away. Where is the image (relative to the lens)? How far is the film/sensor from the lens?

**Apply + Analyze.** A Galilean telescope (used for opera glasses) consists of a converging objective $f_1 = +30$ cm and a diverging eyepiece $f_2 = -10$ cm. They are separated by 20 cm (so that the focal points coincide). For a distant object: find the angular magnification. (Hint: the image of the objective is "after" the eyepiece, making it a virtual object — handle the sign conventions carefully.)

**Apply (optometry).** A nearsighted person has a far point of 50 cm. They want to see distant objects clearly (i.e., the corrective lens should image objects at infinity to a virtual image at 50 cm — the eye's far point). Find the required lens power in diopters. Is it converging or diverging?

**Challenge.** A compound microscope has objective $f_1 = 4$ mm and eyepiece $f_2 = 25$ mm, separated by 16 cm. (a) Where must the object be placed so that the objective forms a real intermediate image just inside the eyepiece's focal point? (b) What is the total magnification?

---

## LLM Exercises

### Build the two-lens ray tracer (`04-lens-simulator.html`)

> **Show.** Thin-lens equation: $1/f = 1/d_o + 1/d_i$. Magnification: $m = -d_i/d_o$. For a two-lens system, the image of lens 1 is the object of lens 2.
>
> **Say.** Build an interactive two-lens ray tracer with object positioning.
>
> **Constrain.** D3 v7. Two lenses on the optical axis, each shown as a vertical line with convex (converging) or concave (diverging) symbol. Toggles for each lens (converging/diverging). Sliders for $f_1$, $f_2$, lens separation $d_{12}$, object distance $d_o$, and object height $h_o$. Trace the three principal rays through both lenses: each ray refracts at each lens plane. Show intermediate image (dashed if virtual) and final image (solid if real). Numerical readouts: $d_{i1}, m_1, d_{i2}, m_2, m_{\text{total}}, h_{i,\text{final}}$. Filename: `04-lens-simulator.html`.
>
> **Verify.** (a) Single converging lens ($d_{12} = \infty$ effectively, or hide lens 2): object outside $f$, real inverted image. (b) Two-lens Keplerian telescope ($f_1 = 100$ mm, $f_2 = 10$ mm, separation 110 mm, distant object): angular magnification $\approx 10$. (c) Galilean configuration ($f_2 < 0$): final image is virtual and upright.

### Exploration

- Configure the Keplerian telescope. Verify the magnification formula by measuring image sizes for known object angular sizes.
- Try a microscope configuration: object just outside $f_1$ (very close to the objective), eyepiece focuses the intermediate image to be just inside its focal length. Find the total magnification.
- For a single converging lens, sweep the object distance from $0$ to $5f$. Plot $d_i$ vs $d_o$. The plot should show the asymptote at $d_o = f$ where $d_i \to \infty$.

### Extension prompt (chapter bridge)

> **Show.** A lens forms an image because each ray bends predictably. But what if I send a *wave* through a narrow slit? Does it produce an image, or something else?
>
> **Say.** Build a single-slit diffraction pattern simulator.
>
> **Constrain.** A vertical slit of width $a$ illuminated by light of wavelength $\lambda$. Display: intensity pattern on a screen at distance $L$ from the slit, computed as $I(\theta) = I_0 [\text{sinc}(\pi a \sin\theta / \lambda)]^2$.
>
> **Verify.** Narrower slit produces wider diffraction pattern. Wider slit produces narrower pattern (more "ray-like").

Save as `04b-diffraction-preview.html`. This is the bridge from geometric optics (Act One) to wave optics (Act Two).

---

## What would change my mind

The thin-lens equation is derived from Snell's law applied at two curved surfaces under the paraxial approximation. It has been confirmed in every optical instrument from Newton's day forward. A confirmed image-formation discrepancy in the paraxial regime would force a re-derivation. None exists. Beyond the paraxial regime, lens aberrations are real and quantitatively predicted by ray-tracing software using Snell's law at every surface. The thin-lens equation is the leading-order approximation, not the full truth.

## Still puzzling

- *Why are eyes such good imaging systems despite their wet biology?* The eye has aberrations and aging-related problems (presbyopia), but the brain compensates extensively. Visual processing routinely sharpens the slightly blurry retinal image. The biology is good enough; the visual processing makes it better.
- *Adaptive optics.* Modern astronomical telescopes correct for atmospheric distortion using deformable mirrors that adjust hundreds of times per second. The math is lens-system theory plus real-time control theory. Worth knowing as a research direction.
- *Beyond geometric optics for imaging.* When wavelengths approach feature sizes, diffraction dominates and the lens equation breaks. The Airy disk at the focus of a lens (Chapter 6) is the diffraction-limited point spread function — the *fundamental* resolution limit, not avoidable by better lens design.

---

**Tags:** converging lens, diverging lens, thin lens equation, lensmaker's equation, principal rays, magnification, two-lens system, telescope, microscope, accommodation, presbyopia

![Two-panel comparison of principal-ray construction. Left panel: converging biconvex lens with object outside focal length. Parallel ray refracts through far focal point. Center ray passes undeviated. Focal ray refract...](images/04-lenses-fig-01.png)
*Figure 4.1 — Three Principal Rays*

![Schematic of a Keplerian telescope. Parallel rays from a distant object enter from the left. The objective lens with focal length f1 forms a real inverted intermediate image at its focal plane. The intermediate image...](images/04-lenses-fig-02.png)
*Figure 4.2 — Keplerian Telescope*

![Two panels comparing a single converging lens with an achromatic doublet. Single lens: parallel white light separates into red, green, and violet rays, each focusing at a different point along the axis because n depen...](images/04-lenses-fig-03.png)
*Figure 4.3 — Chromatic Aberration and the Achromatic Doublet*

![Cross-section of the human eye showing the optical components. Cornea at the front provides most of the refractive power because air-tissue is the biggest index step. Crystalline lens behind iris provides variable acc...](images/04-lenses-fig-04.png)
*Figure 4.4 — Human Eye*

![Three panels showing common vision defects and their lens corrections. Myopia: eyeball too long, distant images focus in front of the retina, corrected by a diverging lens. Hyperopia: eyeball too short, near images wo...](images/04-lenses-fig-05.png)
*Figure 4.5 — Vision Corrections*

