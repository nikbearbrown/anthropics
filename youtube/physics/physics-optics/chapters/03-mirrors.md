# Chapter 3 — Mirrors and Image Formation


## TL;DR

- Curved mirrors form images by redirecting many rays from one point to another.
- The chapter moves through Learning objectives, Opening case: the convex mirror at the parking exit, Core concept, Flat mirrors, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Curved mirrors form images by redirecting many rays from one point to another.*

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Understand)** Distinguish real and virtual images by where the reflected rays actually converge versus where they appear to diverge from.
2. **(Apply)** Use the mirror equation $1/f = 1/d_o + 1/d_i$ and magnification equation $m = -d_i/d_o$ to predict image properties.
3. **(Apply)** Trace the three principal rays for any object position to locate the image graphically.
4. **(Analyze)** Predict qualitatively (real/virtual, upright/inverted, larger/smaller) what happens to the image as the object moves through the focal point.
5. **(Apply)** Build a curved-mirror ray tracer that handles concave and convex mirrors with any object position.

---

## Opening case: the convex mirror at the parking exit

You back out of a parking garage. At the exit, a giant convex mirror on the wall reveals the lane to your left — including the car barreling toward your blind spot. Without the mirror, you wouldn't see it. With the mirror, the lane is visible — but everything in the mirror looks farther away than it is.

The mirror is doing two things at once: providing a *wide field of view* (so you can see what's behind to one side, not just behind), and making everything *appear smaller and farther away* than it really is. Both effects come from the same physics — the mirror is convex, focal length is negative, and the image is virtual, upright, and reduced.

This is why "Objects in mirror are closer than they appear" is on every passenger-side car mirror. The mirror is convex; the image is reduced. Drivers misjudge distance because their brain takes the image size as a cue to distance, and the image is smaller than a flat-mirror image would be.

This chapter teaches you to predict images from any curved mirror. The mirror equation is the algebra; the principal-ray rules are the geometry; the simulation lets you verify.

---

## Core concept

### Flat mirrors

A flat mirror produces a virtual image *as far behind the mirror as the object is in front*, same size, upright. Construction: each ray from the object reflects off the mirror with $\theta_r = \theta_i$; extending the reflected rays backward, they appear to converge at a point symmetric to the object. The image is virtual (the rays don't actually meet there; they only appear to).

### Curved mirrors: concave and convex

A **concave** (converging) mirror has its reflecting surface curved inward, like the inside of a sphere. Parallel rays from far away reflect and converge to a single point — the **focal point** F — at distance $f$ from the mirror.

A **convex** (diverging) mirror has its reflecting surface curved outward. Parallel rays reflect and appear to diverge from a focal point *behind* the mirror.

For a spherical mirror with radius of curvature $R$:
$$f = R/2$$

By sign convention, $f > 0$ for concave (focal point in front), $f < 0$ for convex (focal point behind).

### The mirror equation

For an object at distance $d_o$ from the mirror (always positive in this convention), the image distance $d_i$ satisfies:
$$\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i}$$

Sign convention: $d_i > 0$ means the image is *in front of* the mirror (real); $d_i < 0$ means behind (virtual).

**Magnification:**
$$m = \frac{h_i}{h_o} = -\frac{d_i}{d_o}$$

$h_i$ is image height; $h_o$ object height; $m > 0$ means upright; $m < 0$ means inverted. $|m| > 1$ means enlarged; $|m| < 1$ means reduced.

### The three principal rays

For a thin (small aperture) curved mirror, three rays from a point on the object construct the image:

1. **Parallel ray.** Travels parallel to the principal axis, reflects through F (concave) or appears to come from F (convex).
2. **Focal ray.** Travels through F before hitting the mirror, reflects parallel to the principal axis.
3. **Center ray.** Travels through the center of curvature C (= 2f from the mirror), reflects straight back along itself.

Any two of these locate the image; the third confirms. The simulation traces all three for visual verification.

### Object outside / at / inside the focal point — concave mirror

For a concave mirror ($f > 0$), the image properties depend on where the object sits:

- **$d_o > 2f$** (far from mirror): real, inverted, reduced. Image between F and C.
- **$d_o = 2f$**: real, inverted, same size. Image at C.
- **$f < d_o < 2f$**: real, inverted, enlarged. Image beyond C.
- **$d_o = f$**: rays emerge parallel; no image (or image at infinity).
- **$d_o < f$**: virtual, upright, enlarged. Image *behind* the mirror.

The last case — object inside the focal length — is the **shaving/makeup mirror**: you sit close, see an enlarged upright image of your face.

### Convex mirror: always virtual

For a convex mirror ($f < 0$), the image is *always* virtual, upright, and reduced, *regardless of object distance*. The mirror equation always gives $d_i < 0$, $|d_i| < d_o$, $0 < m < 1$.

This is why convex mirrors are used for blind-spot, security, and side mirrors: wide field of view, no inverted images to confuse the viewer.

---

## Worked example: a concave makeup mirror

A makeup mirror has $f = 15$ cm. You hold it so your face is 12 cm from the mirror. Find: (a) image distance, (b) magnification, (c) image type (real/virtual, upright/inverted).

**(a) Image distance.** Apply the mirror equation:
$$\frac{1}{15} = \frac{1}{12} + \frac{1}{d_i}$$
$$\frac{1}{d_i} = \frac{1}{15} - \frac{1}{12} = \frac{4 - 5}{60} = -\frac{1}{60}$$
$$d_i = -60 \text{ cm}$$

Negative $d_i$ means the image is virtual — behind the mirror.

**(b) Magnification:**
$$m = -\frac{d_i}{d_o} = -\frac{-60}{12} = +5$$

Image is 5× enlarged, upright (positive $m$).

**(c) Image properties.** Virtual (behind the mirror — can't be projected onto a screen, but you see it by looking into the mirror), upright, 5× enlarged. Your face's reflection appears 60 cm behind the mirror, five times larger than life. The mirror is doing exactly what a makeup mirror is supposed to do.

**The lesson.** When the object is inside the focal length of a concave mirror, you get a virtual, upright, enlarged image. Move the object *outside* the focal length and the image flips to real and inverted — try this with a concave mirror, hold it at varying distances, and watch the image jump.

**The limit.** This calculation assumes the mirror is *thin* (aperture small compared to radius of curvature). For a wide concave mirror, rays at the edges focus closer than rays near the center — **spherical aberration**. Solving spherical aberration is why telescope mirrors are parabolic, not spherical.

---

## Common misconceptions

**"Virtual images can't be seen."** They can be seen by your eye looking into the mirror. They just can't be projected onto a screen, because the reflected rays don't actually converge anywhere — they only *appear* to diverge from a point behind the mirror.

**"Convex mirrors always make things smaller."** True for distant objects, where the image is virtual, upright, reduced. For objects *very close* to a convex mirror, the magnification approaches 1 — the image is nearly life-size. (But still virtual and upright.) Try with a Christmas-tree ornament: stand close enough and your nose looks nearly normal-sized.

**"The mirror equation works for any mirror."** It works for *small-angle* approximation — paraxial rays. For wide-aperture mirrors, spherical aberration becomes significant. Parabolic mirrors (telescope optics) sidestep this by having the right shape to focus parallel rays exactly to a point.

**"The center of curvature is where the image forms."** No. The center of curvature is at distance $2f$ from the mirror. The image forms wherever rays converge, given by the mirror equation. Object at C gives an image at C — that's the only case where the image is also at C.

**"Light bounces back through the focal point on the way back from a far object."** The focal point is the *destination* of parallel rays after reflection — not the starting point of incident rays from a far object. Don't conflate the principal ray (a construction tool) with literal ray paths.

---

## Exercises

**Warm-up (Apply).** A concave mirror has $f = 20$ cm. An object sits 30 cm in front of the mirror. Find $d_i$ and $m$. Is the image real or virtual? Upright or inverted?

**Apply.** A convex mirror has $f = -25$ cm. An object 40 cm in front. Find $d_i$ and $m$. Verify the image is virtual, upright, and reduced.

**Apply.** Walk through every position for an object in front of a concave mirror with $f = 10$ cm: $d_o = 5, 10, 15, 20, 25, 30, 50$ cm. For each, compute $d_i$ and $m$. Notice the image jumps from virtual upright to real inverted as the object passes through the focal point.

**Apply + Analyze.** Your face is 8 cm from a makeup mirror, and the image is 3× enlarged, upright. Find the mirror's focal length. Is the mirror concave or convex?

**Challenge.** Two mirrors face each other 50 cm apart. A small object sits 10 cm from one of them. Trace the rays: how many images appear, and where? (Hint: the image in the first mirror serves as a virtual object for the second mirror, and vice versa, creating a series.)

---

## LLM Exercises

### Build the curved-mirror ray tracer (`03-curved-mirror.html`)

> **Show.** Mirror equation: $1/f = 1/d_o + 1/d_i$. Three principal rays construct the image graphically.
>
> **Say.** Build an interactive curved-mirror ray tracer with object positioning.
>
> **Constrain.** D3 v7. Mirror drawn as a curved arc (concave: opening toward the object; convex: opening away). Toggle: concave/convex. Slider for $|f|$. Object drawn as a vertical arrow on the optical axis, with slider for $d_o$. Trace the three principal rays from the *top* of the object. Image arrow drawn at the location where reflected rays converge (solid) or appear to diverge from (dashed for virtual). Numerical readouts: $d_i$, $m$, image-type (real/virtual, upright/inverted), $f$, location of focal point F and center C. Filename: `03-curved-mirror.html`.
>
> **Verify.** (a) Concave mirror $f = 10$, $d_o = 20$: real inverted image at $d_i = 20$ cm. (b) Concave $f = 10$, $d_o = 5$: virtual upright image at $d_i = -10$ cm, $m = +2$. (c) Convex $f = -15$, any $d_o > 0$: virtual upright reduced image, $|d_i| < d_o$.

### Exploration

- Slide the object from far away toward the mirror with a concave mirror. Watch the image:
  - Far away: small, real, inverted, near F.
  - At $2f$: same size, real, inverted, at $2f$ on the other side.
  - Between $f$ and $2f$: enlarged, real, inverted.
  - At $f$: image goes to infinity.
  - Inside $f$: virtual, upright, enlarged. (The jump is dramatic.)
- For a convex mirror, vary the object distance from far to close. Does the image always stay virtual? How does its size change?

### Extension prompt (chapter bridge)

> **Show.** Curved mirrors form images by reflection. Lenses form images by *refraction* — Snell's law applied at two curved surfaces.
>
> **Say.** Build a thin-lens ray tracer.
>
> **Constrain.** Lens drawn as a vertical line with standard convex (converging) or concave (diverging) marks. Same principal-ray rules but for refraction: parallel ray → through far focal point; ray through near focal point → parallel; ray through optical center → undeviated.
>
> **Verify.** Converging lens, object outside $f$: real inverted image. Inside $f$: virtual upright enlarged.

Save as `03b-lens-preview.html`. This is the bridge to Chapter 4.

---

## What would change my mind

The mirror equation $1/f = 1/d_o + 1/d_i$ is derived from the law of reflection plus the paraxial (small-angle) approximation. A confirmed image-formation phenomenon that doesn't fit this equation, in the regime where the paraxial approximation should hold, would force a re-derivation. None exists. Beyond the paraxial regime, *spherical aberration* and *coma* are real and well-modeled by higher-order corrections; the mirror equation remains the appropriate leading-order description.

## Still puzzling

- *Why parabolic mirrors and not spherical?* Parabolic mirrors focus parallel rays to a single point exactly, with no spherical aberration. Spherical mirrors only approximately focus to a point, with edge-rays focusing closer than center-rays. Why spherical mirrors persist in cheap optics: they're easier to manufacture. Modern precision telescopes use parabolic or more elaborate aspheric surfaces.
- *What happens at the focal point?* If the object is exactly at $f$, the mirror equation gives $1/d_i = 0$, i.e., $d_i \to \infty$. The image is "at infinity." Physically: reflected rays emerge parallel. Real but with no finite location.
- *Imaging beyond paraxial.* For wide-angle mirrors or fish-eye applications, the simple lens/mirror equation fails and you need full ray tracing — which is exactly what the simulation does. The chapter teaches the equation; the simulation reveals where it breaks.

---

**Tags:** concave mirror, convex mirror, mirror equation, magnification, principal rays, focal point, center of curvature, real image, virtual image

![Concave mirror on the right with focal point F and center of curvature C marked on the principal axis. Object as a vertical orange arrow on the left, between F and C. Three principal rays from the top of the object co...](images/03-mirrors-fig-01.png)
*Figure 3.1 — Three Principal Rays*

![Five panels showing the same concave mirror with the object at five distances. Case A: object beyond 2f gives a smaller inverted real image between F and 2f. Case B: object at 2f gives a same-size inverted real image...](images/03-mirrors-fig-02.png)
*Figure 3.2 — Five Image Cases*

![Convex mirror with the curve bowing outward to the right. Focal point F is behind the mirror (virtual focal point, dashed marker). Object as a vertical arrow on the left. Parallel ray reflects as if from F. Reflected...](images/03-mirrors-fig-03.png)
*Figure 3.3 — Convex Mirror*

![Two panels comparing parallel-ray focusing on spherical and parabolic mirrors. Left panel: spherical mirror, rays near the axis focus at F, rays farther out focus closer to the mirror, producing a circle of least conf...](images/03-mirrors-fig-04.png)
*Figure 3.4 — Spherical Aberration vs Parabolic Correction*

