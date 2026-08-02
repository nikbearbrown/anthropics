# Chapter 2 — Mirrors and Lenses: How Light Bends and Focuses

## Three title options

- The Path of Light: Mirrors, Refraction, and the Eye
- How Glass and Curved Metal Shape What We See
- Building an Image: The Physics of Mirrors, Refraction, and Lenses

---

## TL;DR

Light travels straight through uniform material but bends when it crosses boundaries or reflects from surfaces. The angle at which it bends depends on the material's refractive index. Mirrors and lenses exploit these rules to create images—some you can project onto a screen, others that exist only in the space behind the glass, visible only to your eye.

---

## Chapter Opening: The Spoon Paradox

Hold a shiny metal spoon at arm's length and look at your reflection. Rotate it. On one side, your face appears upright, smaller, and farther away. Flip the spoon. Now your face is inverted, larger, and somewhere in front of the surface. The spoon hasn't changed. The light hasn't changed. Only the curvature separates one image from the other.

This is your entrance to geometric optics—the physics of how light travels in straight lines and bends when it encounters matter. For the next few sections, light will be well-behaved and predictable. It will move as rays (straight paths), obey simple angles, and follow mathematical rules that engineers use to design microscopes, telescopes, and the human eye itself.

The puzzle is simple to state: Why does a curve change where an image appears? The answer requires understanding three mechanisms—how light bounces, how it bends crossing between materials, and how both effects combine in a lens.

**Learning objectives**

By the end of this chapter you will understand:

- How the law of reflection governs what you see in a mirror, and why curved mirrors create real images while flat ones create only virtual ones.
- Why light bends when crossing between materials of different density, and how this bending (refraction) explains rainbows, fiber optics, and why a diamond sparkles.
- How lenses use refraction at both surfaces to form images, and why your eye focuses differently on objects at different distances.

**Prerequisites**

You should be comfortable with:

- Angles, measured in degrees, and how angles relate to perpendicular lines.
- The idea that light travels in straight lines (rays) through a uniform medium.
- Basic trigonometry (sine, cosine, and how they relate to angles in right triangles).

---

## Concept 1: Reflection and Curved Mirrors — Image Formation from Bouncing Light

### Cold Open: The Hall of Mirrors

In 1678, construction began on the Hall of Mirrors at the Palace of Versailles. The room was designed not to multiply light, but to create the illusion of infinite space by reflecting the gardens back into the interior. If you visit today and look at old photographs of the hall in use, you see dozens of images—most virtual (existing only in the glass), one real (the actual gardens). The question that would have faced the architect: Where does each image appear? And which ones can be photographed?

The answer comes from one rule: the angle at which light leaves a surface equals the angle at which it arrived. But the geometry of curved surfaces—and where rays converge after bouncing—changes everything.

### Mechanism: The Law of Reflection and the Mirror Equation

Light travels in straight lines until it hits a reflective surface. When it does, it bounces. The direction of the bounce follows a geometric rule measured from a perpendicular line (called the *normal*) drawn at the point where the light hits the surface.

$$\theta_r = \theta_i$$

This is the **law of reflection**: the angle of reflection equals the angle of incidence. Both angles are measured from the normal, not from the surface itself. This is why a mirror at a shallow angle can redirect light by a lot—even a tiny tilt of the normal changes where the light goes.

For a flat mirror, the geometry is straightforward. Two rays from your face hit the mirror at different angles. Both obey the law of reflection. When you trace both rays backward (behind the mirror where the light is not actually going), they converge at a point. That convergence point is your *virtual image*—it's the place your eye *infers* the light is coming from. It appears the same distance behind the mirror as you stand in front of it. Your eye cannot tell the difference between light that has actually come from a point and light that *appears* to come from that point when traced backward. This is why you see an image.

For a *curved mirror*, the geometry becomes more interesting. A **concave mirror** (curved inward, like the bowl of a spoon) concentrates rays. A **convex mirror** (curved outward, like the back of a spoon) spreads them.

In a concave mirror, imagine parallel rays entering parallel to the central axis. At each point where a ray hits the curved surface, there is a different normal (perpendicular to the mirror at that point). Each ray reflects according to the law: $\theta_r = \theta_i$ at its own point. Because the mirror is curved, these normals point in different directions. Yet the geometry is such that all the reflected rays converge at a single point called the *focal point*, F. The distance from the mirror to this point is the *focal length*, $f$. The relationship between focal length and the mirror's radius of curvature is simple:

$$R = 2f$$

This is a geometric fact: for a spherical mirror with radius of curvature $R$, the focal length is always half the radius. A tighter curve (smaller $R$) means a shorter focal length (rays converge closer to the mirror).

Where does the image appear? That depends on where the object sits relative to the focal point. If the object is farther from the mirror than the focal point ($d_o > f$), the rays diverging from the object are intercepted by the mirror. After reflecting, they converge *in front* of the mirror at a point where you can project the image onto a screen. This is a **real image**. Light actually passes through the image point; the rays converge there, carrying energy. If the object is closer than the focal point ($d_o < f$), the rays diverge after reflecting. They don't converge in front of the mirror. Tracing them backward behind the mirror, they converge. This is a **virtual image**—larger, upright, and visible only in the mirror itself. No light actually goes to this point.

A convex mirror always produces a virtual image, smaller and upright, no matter where the object is. The focal point is behind the mirror, and rays are always diverging when they leave the surface.

The mathematical relationship that connects object distance ($d_o$), image distance ($d_i$), and focal length ($f$) is derived from the ray-tracing geometry:

$$\frac{1}{f} = \frac{1}{d_i} + \frac{1}{d_o}$$

Rearranged to solve for image distance:

$$d_i = \frac{f \cdot d_o}{d_o - f}$$

The sign convention is important: positive $d_i$ means the image is in front of the mirror (real). Negative $d_i$ means the image is behind the mirror (virtual). For a concave mirror, $f$ is positive. For a convex mirror, $f$ is negative.

The *magnification* is the ratio of image size to object size:

$$m = \frac{h_i}{h_o} = -\frac{d_i}{d_o}$$

The negative sign carries information: if $m$ is negative, the image is inverted (upside down). If positive, it is upright. If $|m| > 1$, the image is magnified (larger). If $|m| < 1$, it is demagnified (smaller).

### Named Trade-off: Real Images vs. Virtual Images

**Real images** can be projected. Light rays actually converge at the image location. You can catch them on a screen, photographic film, or the retina of an eye. But they're inverted and appear only when the object is far from the mirror (beyond the focal point). Move the object closer to the focal point, and the image distance grows—the image gets farther away. Move it inside the focal point, and the image disappears from view; there is no real image to project.

**Virtual images** appear upright and magnified (in a concave mirror closer to the focal point) or shrunk (in a convex mirror). You see them by looking into the mirror. But you cannot project them because light rays never actually meet at the image location. The rays diverge, and your eye traces them backward, reconstructing where they came from. A camera placed behind the mirror would see nothing; the light never reaches there. Yet your eye perceives the image as vividly as if light had come from it.

The trade-off is immediate: magnification and upright orientation versus the ability to project and capture on film. This is why makeup mirrors are concave (producing upright, magnified virtual images when your face is near) and security mirrors are convex (showing a wide, demagnified field of view so nothing sneaks past).

### Worked Example 1: A Security Mirror

A person stands 6.0 m from a convex security mirror and sees their image appearing 1.0 m behind the mirror. What is the focal length?

For a virtual image in a convex mirror, $d_i$ is negative (behind the mirror): $d_i = -1.0$ m.

Using the mirror equation rearranged for focal length:

$$f = \frac{d_i \cdot d_o}{d_i + d_o} = \frac{(-1.0)(6.0)}{-1.0 + 6.0} = \frac{-6.0}{5.0} = -1.2 \text{ m}$$

The negative focal length confirms this is a convex mirror. The focal point is 1.2 m behind the mirror's surface. This convex geometry allows the mirror to show a wide area (anything within roughly a hemisphere in front) in a small mirror—a key feature of security mirrors.

### Worked Example 2: A Makeup Mirror

A concave mirror has a focal length of 15.0 cm. A woman's face is 10.0 cm from the mirror. Where does her image appear, and is it magnified or demagnified?

Since $d_o = 10.0$ cm and $f = 15.0$ cm, we have $d_o < f$. This should produce a virtual, magnified image.

Using the lens/mirror equation:

$$d_i = \frac{f \cdot d_o}{d_o - f} = \frac{(15.0)(10.0)}{10.0 - 15.0} = \frac{150}{-5.0} = -30.0 \text{ cm}$$

The negative image distance means the image is behind the mirror (virtual).

Magnification:

$$m = -\frac{d_i}{d_o} = -\frac{(-30.0)}{10.0} = +3.0$$

The positive magnification means the image is upright. The magnitude 3.0 means the image is three times the object's height. A 2 cm tall feature on her face appears 6 cm tall in the mirror—very useful for applying makeup.

### Common Misconceptions

**"A virtual image is less real than a real image."** No. A virtual image can be photographed—your camera can capture it through the mirror. Light enters your eye (or a camera) from the mirror after bouncing, and your eye reconstructs where it appears to come from. It is as real as any other image you see. The distinction is not about realness, but about whether light converges at the image location or only *appears* to diverge from it.

**"A curved mirror is just a flat mirror bent."** Partially true, but the geometry changes everything. A flat mirror produces no magnification ($|m| = 1$ always). A curved mirror's magnification varies with the object's position relative to the focal point. A large magnification is possible only near the focal point, and then only as a virtual image. The focal point is a consequence of curvature, not a feature of flatness.

---

## Concept 2: Refraction — Why Light Bends Crossing Between Materials

### Cold Open: The Bent Pencil

Fill a glass halfway with water. Place a pencil in the glass and look from the side. The pencil appears to bend at the water surface—kinked, as if broken. The pencil is straight. The water is clear. Only the light's path has changed.

This is refraction: the bending of light as it crosses a boundary between materials with different optical densities.

### Mechanism: The Index of Refraction and Snell's Law

Light travels at different speeds in different materials. In a vacuum, light moves at $c = 3.00 \times 10^8$ m/s. In water, it moves slower: about $2.25 \times 10^8$ m/s. In glass, slower still: about $2.0 \times 10^8$ m/s. The ratio of the vacuum speed to the speed in a material defines the *index of refraction*:

$$n = \frac{c}{v}$$

where $v$ is the light's speed in the material.

Because light always travels slower in matter than in vacuum, $n$ is always greater than 1. Water has $n = 1.333$. Crown glass has $n = 1.52$. Diamond has $n = 2.419$—so much denser optically that light travels less than half its vacuum speed.

Why does light slow in a material? Because electromagnetic waves interact with electrons in atoms. The light's electric and magnetic fields jostle the electrons, which absorb and re-emit the light. This back-and-forth delays the wave's propagation, making the effective speed lower.

When light crosses a boundary between two materials with different refractive indices, it bends. The amount it bends depends on both the angle at which it hits the boundary and the difference in indices. The law governing this relationship is **Snell's law**:

$$n_1 \sin \theta_1 = n_2 \sin \theta_2$$

Here, $n_1$ and $n_2$ are the refractive indices of the first and second materials, and $\theta_1$ and $\theta_2$ are the angles the light ray makes with the perpendicular (*normal*) to the boundary.

Think of it mechanically: imagine a wheel rolling from pavement onto grass, with one wheel hitting grass first. The wheel in grass slows more than the wheel still on pavement. The axle (perpendicular) is pulled toward the grass. The wheel's path curves. Light works the same way. When light enters a denser medium (higher $n$), it slows. One "side" of the wave slows before the other. The whole ray bends toward the perpendicular. When it leaves a denser medium, it speeds up, and the ray bends *away* from the perpendicular.

A critical case exists. If light travels from a dense medium (high $n$) to a less dense one (low $n$), there is an angle—the *critical angle*—beyond which light cannot escape into the second medium. Instead, all of it reflects back into the first medium. This is **total internal reflection**.

$$\theta_c = \sin^{-1}\left(\frac{n_2}{n_1}\right), \quad n_1 > n_2$$

Once the incident angle exceeds $\theta_c$, refraction stops. Only reflection occurs. This threshold exists because Snell's law demands that $\sin \theta_2 = (n_1/n_2) \sin \theta_1$. If $n_1 > n_2$, the sine on the right can exceed 1 for large enough $\theta_1$. Since sines of real angles never exceed 1, there is no solution—no refracted ray exists. The light must reflect instead.

### Named Trade-off: Refraction vs. Reflection; Dispersion

**Refraction** lets light pass through while bending. This is how lenses work and how light travels through optical fibers. The downside: different wavelengths bend by slightly different amounts (because the refractive index varies with wavelength). This *dispersion* separates white light into colors—useful for a prism, but a problem for optical devices that need to keep all colors focused at the same point.

**Total internal reflection** traps light inside a material. In a fiber optic cable, light bounces down the fiber by total internal reflection. No light escapes sideways. The advantage: perfect channeling of light with no energy loss (in an ideal case). The disadvantage: the fiber's shape, bends, and material composition become critical. A bent fiber or a crack can break the total internal reflection condition and let light escape.

**Dispersion** is why diamonds sparkle. The critical angle for a diamond-air boundary is only 24.4°. Light enters a diamond from many angles, but it can exit only where the angle to the surface is shallow enough. The facets are cut to make this unlikely, trapping light inside, bouncing it around, and concentrating it at specific points where it finally escapes. Each bounce separates colors slightly (because different wavelengths refract differently at entry), so white light exits as colored flashes. This is the "fire" of a good diamond.

### Worked Example 3: Finding an Unknown Material

Light enters an unknown substance submerged in water at an angle of 45.0° from the perpendicular and refracts to 40.3°. Water has $n = 1.333$. What is the substance?

Using Snell's law:

$$n_{\text{water}} \sin(45.0°) = n_{\text{unknown}} \sin(40.3°)$$

$$n_{\text{unknown}} = \frac{1.333 \times 0.7071}{0.6468} = 1.458$$

Checking a table of refractive indices, this matches fused quartz almost exactly.

Note: The ray bent toward the perpendicular (45.0° to 40.3°), indicating the unknown material is denser than water, consistent with the calculation.

### Worked Example 4: The Critical Angle for Water

What is the critical angle for light trying to escape from water (n = 1.333) to air (n = 1.0003)?

$$\theta_c = \sin^{-1}\left(\frac{n_{\text{air}}}{n_{\text{water}}}\right) = \sin^{-1}\left(\frac{1.0003}{1.333}\right) = \sin^{-1}(0.7505) = 48.6°$$

This means that if you're underwater looking up, you can see out at angles less than 48.6° from the vertical. Beyond that angle, the water-air interface becomes a mirror. This is why aquatic animals looking up see a compressed view of the world above (due to refraction) inside a cone of roughly 48.6° half-angle, and a mirror image of the underwater world at steeper angles.

### Common Misconceptions

**"Light always bends away from the normal when entering a denser medium."** No. It bends *toward* the normal. Think of the wheel analogy: the wheel slows, so the axle (perpendicular) is approached, not fled. The slowing of light in denser media causes it to bend toward the normal, concentrating the rays. This is why a lens (thicker at the center) converges light—light slows more in glass than air, so it bends toward the axis.

**"Total internal reflection happens at any boundary."** No. It requires light to travel from a denser medium to a less dense one. Light traveling from air into water cannot undergo total internal reflection at the air-water boundary; some always refracts into the water. The critical angle concept applies only when $n_1 > n_2$.

**"Rainbows are made by refraction alone."** No. A rainbow requires both refraction (bending as light enters the water droplet) and reflection (bouncing off the back of the droplet). Dispersion—the separation of colors by wavelength—completes the effect. Red light refracts less, reflects, and exits at a different angle than blue light.

---

## Concept 3: Lenses and the Thin-Lens Equation — Combining Refraction at Two Surfaces

### Cold Open: Why Your Eye Works

Hold a magnifying glass at arm's length and look at a distant tree. The image of the tree appears upside down on a piece of paper held on the opposite side of the lens. Move the paper closer to the lens. The image blurs, then sharpens. Move it closer still, and the image shrinks and becomes brighter. You have just traced the relationship between object distance, image distance, and focal length—the same relationship that your eye uses to focus on objects at different distances.

### Mechanism: Converging and Diverging Lenses

A *converging lens* (convex, thicker at the center) uses refraction at both surfaces to concentrate light. Parallel rays entering the lens bend toward the perpendicular as they enter (because glass is denser than air), then bend away from the perpendicular as they leave (because air is less dense). The two bends add. All rays end up crossing at a focal point $f$ on the far side.

The first surface (air-to-glass) causes all rays to converge somewhat toward the central axis. The second surface (glass-to-air) continues this convergence. Where the rays meet is the focal point. The distance to this focal point is the focal length.

A *diverging lens* (concave, thinner at the center) does the opposite. Parallel rays bend toward the perpendicular at entry, but bend so far away from the perpendicular at exit that they diverge. Tracing them backward, they appear to come from a focal point on the same side as the incoming rays. For a diverging lens, the focal length is negative.

The *power* of a lens is:

$$P = \frac{1}{f}$$

measured in *diopters* (D), or reciprocal meters. A lens with $f = 0.5$ m has power $P = 2$ D. Eyeglass prescriptions are written in diopters. A stronger (more converging) lens has shorter focal length and higher positive power. A diverging lens has negative power.

The thin-lens equation relates object distance, image distance, and focal length—the same equation as for mirrors:

$$\frac{1}{f} = \frac{1}{d_i} + \frac{1}{d_o}$$

Rearranged:

$$d_i = \frac{f \cdot d_o}{d_o - f}$$

Magnification is:

$$m = \frac{h_i}{h_o} = -\frac{d_i}{d_o}$$

The sign conventions are the same as for mirrors. Positive $d_i$ means a real image (convergent rays). Negative $d_i$ means virtual. Negative $m$ means inverted.

Three cases emerge:

1. **Case 1**: $f > 0$ (converging lens), $d_o > f$. Real, inverted image. The image distance is positive and increases as the object approaches the focal point.

2. **Case 2**: $f > 0$ (converging lens), $d_o < f$. Virtual, upright, magnified image. The image distance is negative (virtual). The magnification is greater than 1 in magnitude.

3. **Case 3**: $f < 0$ (diverging lens), any $d_o$. Virtual, upright, demagnified image. The image is always on the same side as the object, always smaller, and always upright.

### Named Trade-off: Real Images vs. Virtual; Chromatic Aberration

**Real images** from a converging lens can be projected (case 1). They are inverted. To get them, the object must be beyond the focal point. Move the object closer to the focal point, and the image distance grows—the image gets farther away and larger. Move it inside the focal point, and the image flips to virtual, upright, and magnified (case 2). This transition is sharp: at exactly the focal point, the image distance goes to infinity.

**Virtual images** from a diverging lens can never be projected (case 3). They are always smaller than the object. But they are upright and useful—this is how eyeglasses correct nearsightedness. A diverging lens in front of an eye that converges too much reduces the total converging power, allowing distant objects to focus correctly on the retina.

**Chromatic aberration** is the penalty of refraction. Because the refractive index depends on wavelength, different colors focus at different distances. Blue light (shorter wavelength) bends more, focusing closer. Red light focuses farther. A simple lens creates a rainbow fringe around the image—blurry and colored. This is solved by combining lenses of different materials: a converging lens of crown glass with a diverging lens of flint glass creates an *achromatic doublet* that corrects the problem. The two lenses are chosen so their chromatic aberrations cancel.

### Worked Example 5: A Projector Lens

A lightbulb sits 0.75 m from a converging lens with focal length 0.50 m. Where does the image form, and what is its magnification?

Since $d_o = 0.75$ m and $f = 0.50$ m, we have $d_o > f$. This is case 1, so we expect a real, inverted image.

Using the lens equation:

$$d_i = \frac{(0.50)(0.75)}{0.75 - 0.50} = \frac{0.375}{0.25} = 1.5 \text{ m}$$

The image forms 1.5 m on the far side of the lens (positive $d_i$ means real).

Magnification:

$$m = -\frac{1.5}{0.75} = -2.0$$

The image is twice the object's height and inverted. If the object is a lightbulb filament 1 cm tall, the image is 2 cm tall, upside down, and can be projected onto a screen 1.5 m away. This is the principle of a movie projector.

### Worked Example 6: A Magnifying Glass (Nearsightedness Correction)

Suppose a nearsighted person uses a concave lens with focal length $f = -10.0$ cm to read a book held 6.50 cm from the lens. What is the magnification?

Since $f < 0$, this is a diverging lens (case 3), so we expect a virtual, upright, demagnified image.

Using the lens equation:

$$d_i = \frac{f \cdot d_o}{d_o - f} = \frac{(-10.0)(6.50)}{6.50 - (-10.0)} = \frac{-65.0}{16.5} = -3.94 \text{ cm}$$

Magnification:

$$m = -\frac{(-3.94)}{6.50} = 0.606$$

The image is 60.6% the size of the object and upright, on the same side of the lens as the book. The image appears 3.94 cm away from the lens (closer than the object). This demagnification is not helpful for reading, but the diverging lens *reduces the total converging power of the eye*, allowing the light to focus farther back on the retina, where it should be for a nearsighted eye.

### Common Misconceptions

**"A stronger lens (higher power) always makes things bigger."** No. Power tells you the focal length, not magnification. Magnification depends on the object and image distances, not the lens alone. A diverging lens (negative power) always demagnifies, even though it has high absolute power. A converging lens can magnify or demagnify depending on where the object is placed.

**"Chromatic aberration is always bad."** Not in a prism. Dispersion into a spectrum is the whole point. But in a camera, telescope, or eye, you want all colors at the same focal point. Correction is essential. This is why high-quality optical instruments use multiple elements.

**"The eye focuses by moving the lens."** Partly true, but incomplete. The lens stays in place. Its *shape* changes, controlled by ciliary muscles, altering focal length. Ciliary muscles contract to flatten or bulge the lens. When contracted (ciliary muscles pulled tight), the lens bulges, shortening its focal length for near objects. When relaxed, the lens flattens, lengthening its focal length for distant objects. The cornea does about two-thirds of the focusing work; the lens adjusts for near and far.

---

## Integration and Synthesis: The Eye as an Optical System

Your eye is a working laboratory for everything in this chapter. The cornea is the primary optical element—a curved refractive surface between air and a denser medium (corneal tissue, $n = 1.38$). The lens is a secondary element that fine-tunes focus. Together, they act like a converging lens, projecting a real, inverted image onto the retina—a light-sensitive sheet at the back of the eye.

The retina sits at a fixed distance from the cornea-lens system, typically about 17 mm. For clear vision, the image must project exactly onto the retina. But objects at different distances require different image distances by the lens equation. The eye solves this by *accommodation*: the ciliary muscles adjust the lens shape, changing its focal length to match.

When you look at a distant object (essentially at infinity), the lens is flattened, giving it a long focal length (about 17 mm in total with the cornea). The image distance is nearly 17 mm. When you look at something close (say, 25 cm away—the near point of normal vision), the lens bulges, shortening its focal length. The image distance stays 17 mm (the retina's position), and the focal length adjustment makes the lens/mirror equation balance.

This system breaks down in two ways. In *myopia* (nearsightedness), the eye converges light too strongly—either because the cornea is too curved, the lens is too powerful, or the eye is slightly too long. Distant objects focus in front of the retina, producing a blurred image. Closer objects (which naturally require more convergence) may focus on the retina and appear sharp. Correction requires a *diverging* spectacle lens to reduce the eye's overall converging power, shifting the focal point back onto the retina. In *hyperopia* (farsightedness), the eye converges too weakly. Distant objects focus behind the retina. The eye is too short, or the cornea is too flat. Correction requires a *converging* spectacle lens to increase power.

The eye also demonstrates the limits of refraction-based optics. All colors refract slightly differently, creating chromatic aberration. The brain compensates by ignoring the fringe. But under close inspection—say, looking at a bright point of light through a magnifying lens—you see the color separation. This is why telescopes and high-quality cameras use mirrors (which have no chromatic aberration) or compensated lens systems instead of simple lenses.

---

## Exercises

### Warm-up

1. A flat mirror produces a virtual image of an object 2 m away. How far behind the mirror does the image appear? Why can you see it but not photograph it with a distant camera?

2. Light traveling in water ($n = 1.333$) hits a glass surface ($n = 1.52$) at an angle of 30° from the perpendicular. Does it bend toward or away from the perpendicular? Calculate the angle of refraction.

3. A converging lens has a focal length of 20 cm. An object is placed 30 cm away. Is the image real or virtual? Explain.

### Application

4. A concave mirror with focal length 15 cm is used as a makeup mirror. A woman's face is 25 cm from the mirror. Where does her image appear, and is it magnified or demagnified?

5. A critical angle for total internal reflection from glass ($n = 1.52$) to air is found to be about 41°. Using Snell's law, verify this value and explain what happens to light hitting the boundary at angles greater than the critical angle.

6. A microscope objective lens has a focal length of 5 mm. An object is placed 5.2 mm from the lens. Where is the image, and what is the magnification? Why does this configuration allow high magnification?

### Synthesis

7. Explain why a fiber optic cable can transmit light over long distances without significant energy loss, while a clear glass rod of the same dimensions would not work as well. What role does the critical angle play?

8. A person with myopia has a relaxed focal length (cornea and lens together) that converges light 22 mm from the eye. The retina is 17 mm back. How much optical power must corrective lenses provide? (Hint: use the lens equation to find the current focal length, then determine what power is needed to shift the focus to the retina.)

9. Why do diamonds sparkle more than glass, even if they are the same shape? Use the concept of critical angle in your answer.

---

## Summary

Light behaves predictably in geometric optics: it travels in straight lines, obeys the law of reflection (angle in equals angle out), and bends when crossing material boundaries according to Snell's law. Each behavior can be quantified.

Mirrors exploit reflection. Curved mirrors concentrate or disperse light, forming real images (when object is beyond focal point) or virtual images (when closer). A single mirror equation relates object distance, image distance, and focal length. Real images are inverted but can be projected. Virtual images are upright but cannot be projected onto a screen.

Refraction bends light as it crosses boundaries. The bending depends on the refractive index difference and the incident angle. Beyond a critical angle, total internal reflection traps light inside a denser medium—the principle behind fiber optics and what makes diamonds sparkle.

Lenses combine refraction at two surfaces. Converging lenses (convex) focus light; diverging lenses (concave) spread it. The same mirror-lens equation describes both mirrors and lenses. Magnification and image type (real/virtual, inverted/upright) depend on the object's position relative to the focal point.

The eye demonstrates all three mechanisms: refraction at the cornea and lens focus light on the retina; accommodation adjusts focal length via lens shape change; and the brain reconstructs an upright image from an inverted projection. Vision defects (myopia, hyperopia) arise from convergence mismatch and are corrected by placing spectacle lenses in front of the eye to adjust its total optical power.

---

## Connections Forward

**Diffraction and interference** (next chapter) occur when light encounters obstacles or slits comparable to its wavelength. Geometric optics assumes objects are much larger than the wavelength; those assumptions break down at small scales, and wave behavior emerges.

**The quantum nature of light** (Chapter 21) reveals that light is neither purely wave nor purely particle. Photons carry energy proportional to frequency. The refractive index—and why light slows in matter—finds its explanation in quantum interactions between light and electrons.

**The atom** (Chapter 22) explains why different materials have different refractive indices. The electrons in atoms respond to the oscillating electric field of light, absorbing and re-emitting it at slightly different phases. The index of refraction is a macroscopic consequence of atomic-scale interactions.

---

## What Would Change My Mind

If an experiment showed that the refractive index of a material depends on the intensity of light (not just the wavelength and material), it would suggest that light-matter interactions are nonlinear at higher intensities—a phenomenon that exists (nonlinear optics) but was not central to this chapter's account. Including it would require discussing energy and power flow, not just geometry.

---

## Still Puzzling

I do not fully understand why the index of refraction varies with wavelength in the precise way it does—what the quantum mechanics of oscillating electrons predicts. The phenomenology (that it happens, and in what direction for typical materials) is clear. The mechanism is not, to me, fully transparent without more quantum electrodynamics.

---

## Tags

#geometric-optics #mirrors #refraction #lenses #snells-law #image-formation #vision-correction #fiber-optics #total-internal-reflection #accommodation
---

## LLM Exercise — Chapter 16: Mirrors and Lenses (Physics Demonstrations Notebook Project)

**Project:** Physics Demonstrations Notebook.
**What you're building this chapter:** the camera obscura demo + the magnifying-glass focal-length measurement.
**Tool:** **Claude Project** for the entry.

---

**The Prompt:**

```
Chapter 16 demo. Notebook in this Claude Project. Chapter 16
taught: ray diagrams for mirrors and lenses; the mirror/lens
equation 1/p + 1/q = 1/f (object distance + image distance =
focal length, all reciprocals); magnification M = -q/p; concave
vs. convex mirrors and lenses; real vs. virtual images.

Two demos.

**Demo A — Camera Obscura (Pinhole "Lens")**

Materials:
- A cardboard box (shoebox or larger).
- Aluminum foil.
- A pin or needle.
- A piece of white paper or thin cloth (to act as the screen).
- Tape, scissors.
- A bright outdoor scene.

Procedure:
1. Cut a small hole (~5 cm square) in one end of the box.
2. Cover that hole with aluminum foil. Tape it tight.
3. Use the pin to make a small hole (~1 mm) in the center of
   the foil.
4. Cut a window in the OPPOSITE end of the box. Tape the white
   paper over the window from the outside (so you can look at
   the back of it from inside).
5. Point the pinhole at a bright outdoor scene.
6. Look at the paper from inside the box (or have someone else
   look while you point).
7. You should see an INVERTED image of the outdoor scene
   projected on the paper.

The image is upside-down because rays through a pinhole cross.
This is exactly what your eye does (through your pupil), but
your brain flips the image right-side-up.

**Demo B — Focal Length of a Magnifying Glass**

Materials:
- A magnifying glass (any convex lens — reading glasses, hand
  lens, even a thin water droplet on glass).
- A bright window or a candle.
- A white surface (paper, wall).

Procedure:
1. Hold the magnifying glass between the bright source and the
   wall.
2. Move the lens until you get a sharp image of the source on
   the wall.
3. Measure the distance from lens to wall — that's the focal
   length f when the source is far (sun, distant window).

Alternative: known object distance + known image distance →
solve for f using 1/p + 1/q = 1/f.

Compute magnification: M = -q/p. Verify by comparing image
size to object size.

**Use Claude as a thinking partner:**
- For A: "Why is the pinhole image inverted? What if I made the
  hole bigger — what changes?"
- For B: "I measured p = X cm, q = Y cm. Compute f. Then check
  the magnification: M = -q/p. Did the image come out right-
  side-up or inverted?"

**Notebook entry should include:**
- Photos: the camera obscura setup AND a photo of the projected
  inverted image (use a phone with long exposure).
- For B: lens, source, and screen distances; computed f;
  computed magnification; verification.
- One real-world application: a film camera's lens; eyeglasses
  for nearsighted vs. farsighted; a microscope.

End with: why does a magnifying glass produce an UPRIGHT image
when you hold it close to the object (object inside the focal
length) but an INVERTED image when you hold it far (object
outside the focal length)?
```

---

**What this produces:** A demo entry showing pinhole-camera image formation and lens focal-length measurement. The inverted-image observation is one of the most counterintuitive findings — why does the sky end up at the bottom?

**How to adapt this prompt:**

- *For your own project:* The camera obscura needs a darkish room. Try it at dusk if your daytime room is too bright.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* For ray diagrams, Claude Code can produce nicely formatted ones.
- *For a Claude Project:* Append.

**Connection to previous chapters:** Ch 15's refraction is what the lens does to bending light; Ch 16 traces it to image formation.

**Preview of next chapter:** Chapter 17 is diffraction and interference. You'll do a single-hair laser-pointer diffraction demo — the human hair acts as a thin obstacle producing a clear diffraction pattern.


---

## AI Wayback Machine

**Hans Lippershey** filed the first known telescope patent in 1608 — combining objective and eyepiece lenses.

**Run this:**

```
Who is Hans Lippershey, and how does their work connect to mirrors and lenses we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Hans Lippershey"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Hans Lippershey's experiments or arguments in detail.
- Add a constraint: "Answer including criticisms or limits of Hans Lippershey's framework."

What changes? What gets better? What gets worse?
