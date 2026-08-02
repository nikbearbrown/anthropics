# Chapter 5 — Geometric Optics

**Suggested titles**

1. Geometric Optics
2. Why a Diamond Sparkles and a Fish Looks Closer Than It Is
3. Light as Lines: Reflection, Refraction, and the Lens

**TL;DR.** Geometric optics is the regime where the wavelength of light is small compared to whatever the light is interacting with — a mirror, a lens, a glass of water — and so the wave nature of light can be ignored and light can be treated as straight rays that bend at boundaries. From two laws (reflection: $\theta_{\text{r}} = \theta_{\text{i}}$; refraction: $n_1 \sin\theta_1 = n_2 \sin\theta_2$) we derive total internal reflection, fiber optics, the rainbow, ray tracing through lenses and mirrors, and the thin-lens equation that quantitatively predicts where any image will form.

---

## Karachi, 1276: a giant water drop in a darkened room

Kamal al-Din al-Farisi is in his early thirties, a student of the great Persian physicist and theologian Qutb al-Din al-Shirazi, working in what is now Iran. He is consumed by a question: why does a rainbow have the colors it has, in the order it has, in the position in the sky it occupies? Aristotle had a theory. Roger Bacon had a theory. Ibn al-Haytham, two and a half centuries earlier, had laid the foundations of modern optics in his *Book of Optics* — but no one had really pinned the rainbow down.

Farisi's solution is brilliantly direct. Water droplets in the atmosphere are too small to study individually with the instruments of his time. So he makes one. He takes a large spherical glass vessel, fills it with water, and places it inside a *camera obscura* — a darkened room with a single small aperture admitting sunlight. The water-filled sphere acts as a giant raindrop. By moving the sphere through the beam of light and watching where the colors emerge, he traces the path of light: it enters the drop, refracts (bends), reflects off the back interior surface of the drop, and refracts again on its way out. Each color bends by a slightly different amount. Different colors emerge from the drop at different angles. The rainbow is the geometry of that splitting, multiplied by every droplet in the sky.

Farisi's experiment, repeated independently a few years later by Theodoric of Freiberg in Germany, gave the world the first correct geometric explanation of the rainbow. It was the flagship demonstration of a research program — *light obeys precise geometric rules at boundaries between materials* — that would eventually be called geometric optics.

This chapter walks through that program. Two laws govern how light changes direction when it meets matter: the law of reflection (mirrors) and the law of refraction (transparent media). Everything else — total internal reflection, fiber optics, lenses, microscopes, telescopes, prisms, the rainbow, the apparent shallowness of a swimming pool — follows by working out the geometry.

**Learning objectives.** By the end of this chapter you should be able to:

1. State the law of reflection ($\theta_{\text{r}} = \theta_{\text{i}}$, both measured from the normal) and use it to construct image-forming diagrams for flat and curved mirrors.
2. Apply Snell's law ($n_1 \sin\theta_1 = n_2 \sin\theta_2$) to compute angles of refraction at any interface, and identify the index of refraction $n$ as the ratio $c/v$ of light's speed.
3. Compute the critical angle for total internal reflection ($\theta_c = \sin^{-1}(n_2/n_1)$ for $n_1 > n_2$) and use it to explain fiber optics, the diamond sparkle, and the apparent silvering of a glass surface viewed from below water.
4. Use the thin-lens equation ($1/d_o + 1/d_i = 1/f$) and the magnification equation ($m = -d_i/d_o$) to predict image position and size for a converging or diverging lens.
5. Construct a ray-tracing diagram for a thin lens or spherical mirror using the three principal rays and predict the image qualitatively (real/virtual, upright/inverted, larger/smaller).

**Prerequisites.** Chapter 24 (electromagnetic waves; the speed of light $c$ in vacuum). Right-triangle trigonometry — sines, cosines, the small-angle approximation. Comfort with the idea that the wavelength of visible light (~400–750 nm) is much smaller than any everyday object.

**Why this chapter matters.** Chapter 26 (vision and optical instruments) builds entirely on this chapter — the eye, the camera, the microscope, the telescope all use the equations of thin lenses and curved mirrors. Chapter 27 returns to the wave picture and examines what geometric optics gets wrong (diffraction limits the smallest detail any optical instrument can resolve). And every fiber-optic cable on Earth, every laser, every telescope, every pair of glasses runs on the physics of this chapter.

---

## Concept 1 — Two laws at a boundary: reflection and refraction

### A bathroom mirror, this morning

You stood in front of a mirror this morning. The light from a bulb above the sink hit your face, scattered off your skin in every direction (your skin is rough at the wavelength of light), and some fraction of those scattered rays struck the mirror. There they obeyed a single rule: the angle of reflection equals the angle of incidence, both measured from the *normal* (the perpendicular line to the surface). The reflected rays then traveled into your eyes, which traced them back along straight lines — and the lines, extrapolated *behind* the mirror, all appeared to converge at a point that looked like your face, sitting a foot behind the glass.

You see an image of yourself behind the mirror. There is no actual face there. There is just a bundle of straight rays whose backward extensions cross at a point. That is what an *image* is in geometric optics — a point where rays (or their extensions) converge.

Now look down into a sink half-full of water. Light from the bottom of the sink travels through water, hits the water/air boundary, and bends — *refracts* — as it exits into air. The bending makes the bottom of the sink look closer to the surface than it actually is. A coin sitting at the bottom of a swimming pool looks shallower because the same physics is happening across a few feet of water and a few feet of air.

Two laws — one for bouncing, one for bending. Together, they describe everything that happens at any boundary between transparent media. Let's pin them down.

### The mechanism — the law of reflection and Snell's law

**The law of reflection.** When a ray of light strikes a smooth surface, the angle of reflection equals the angle of incidence:

$$\theta_r = \theta_i.$$

Both angles are measured from the *normal* — the line perpendicular to the surface at the point where the ray strikes. The incident ray, the reflected ray, and the normal all lie in the same plane (called the plane of incidence). That's the entire law. It works for any wave — sound, water, light — and for any surface that is smooth on the scale of the wavelength.

If the surface is rough on the scale of the wavelength, the law still applies *locally* at every point — but every point has its normal pointing in a different direction, so the rays scatter in all directions. This is *diffuse reflection*, and it's why you can read this page from any angle: the page reflects light diffusely, not specularly.

**Snell's law of refraction.** When light passes from one transparent medium into another, it changes speed (because its wavelength changes; the frequency is set by the source and doesn't change at the boundary). The change of speed forces a change of direction. The relationship is

$$n_1 \sin\theta_1 = n_2 \sin\theta_2,$$

where $n_1$ and $n_2$ are the *indices of refraction* of the two media and $\theta_1$ and $\theta_2$ are the angles of incidence and refraction, both measured from the normal.

The index of refraction of a medium is defined as the ratio of the vacuum speed of light to the speed of light in the medium:

$$n = \frac{c}{v}.$$

In vacuum, $n = 1$ exactly. In air, $n \approx 1.000293$ — close enough to 1 that we usually approximate it as 1. In water, $n \approx 1.333$ — light moves at about $\frac{3}{4}$ of $c$ in water. In ordinary glass, $n \approx 1.5$. In diamond, $n \approx 2.42$ — light moves at less than half its vacuum speed inside a diamond.

The qualitative content of Snell's law: when light goes from a low-$n$ medium to a high-$n$ medium (e.g., air to water), it bends *toward* the normal. When it goes the other way (water to air), it bends *away* from the normal. The fish in your aquarium is not where it appears to be; the light from it bent away from the normal as it left the water, making the fish appear closer to the surface than it actually is.

### The trade-off

The geometric-optics description trades **wave detail for tractable geometry.** A real beam of light is an electromagnetic wave with diffraction effects, polarization, and interference fringes; geometric optics ignores all of that and treats light as straight rays. The cost: when the apparatus has features smaller than a wavelength (a slit a few hundred nanometers wide, a feature on a microchip), geometric optics fails and you need wave optics (Chapter 27). The benefit: for any everyday object — a lens, a mirror, an eye, a telescope — the rays-and-angles description is essentially exact and lets you compute image positions to millimeter precision with high-school trig.

### Worked example — looking at a fish from above

A fish is at a depth of $1.0 \text{ m}$ directly below where you're looking down into a still freshwater pond. How deep does the fish *appear* to be?

For a viewer looking nearly straight down, light from the fish travels nearly perpendicular to the water surface, and the small-angle version of Snell's law applies. Let $d_{\text{actual}} = 1.0 \text{ m}$ be the true depth and $d_{\text{apparent}}$ the depth at which the rays' backward extensions appear to originate.

For nearly normal viewing,

$$d_{\text{apparent}} = \frac{d_{\text{actual}}}{n_{\text{water}}} = \frac{1.0 \text{ m}}{1.333} \approx 0.75 \text{ m}.$$

The fish appears about $25 \text{ cm}$ shallower than it actually is.

**Sanity check.** This matches everyday experience — pools always look shallower than they are. Spearfishers learn to compensate; a heron snapping at a fish does too, by some combination of instinct and learning. The 0.75 ratio is just $1/n_{\text{water}}$ — the geometry of refraction.

### Common misconceptions

- *"Angles in Snell's law are measured from the surface."* No, from the *normal* (the perpendicular). At grazing incidence, the angle from the normal is near $90°$, not $0°$.
- *"Light slows down in water because it bumps into atoms and slows down between them."* The microscopic story is more subtle: photons interact with the bound electrons in the medium, get absorbed and re-emitted with phase shifts, and the *net* effect on the wave is a reduction in phase velocity. The simple "bumps into atoms" picture gives the right answer for the wrong reason. We meet the better picture in Chapter 29.

↳ **Dig Deeper — Why Snell's law has the form it does: Fermat's principle**

*The chapter states Snell's law as an empirical rule with a microscopic justification (different speeds in different media). The deeper derivation is geometrical: light follows the path that takes the least time between any two points. From this single principle ("Fermat's principle"), Snell's law falls out in three lines of calculus.*

**Prompt:**
> Derive Snell's law from Fermat's principle of least time. Set up the geometry: a ray going from point A in medium 1 (index $n_1$) to point B in medium 2 (index $n_2$), crossing the boundary at some point P whose horizontal position you'll vary to minimize total travel time. Write the time as a function of P's position, take the derivative, set it equal to zero, and show that the result is $n_1 \sin\theta_1 = n_2 \sin\theta_2$. End with one sentence on why the minimum-time formulation is more general than the wave picture (it works in classical mechanics too).

**What to do with the output:** Save it. Fermat's principle is one of the most beautiful "least-action" formulations in physics. The same logic — *systems take the path that minimizes some quantity* — recurs in classical mechanics (least action) and quantum field theory (Feynman's path integral).

---

## Concept 2 — Total internal reflection: trapping light

### The Atlantic floor, 1988

In December 1988, the first transatlantic fiber-optic cable, TAT-8, went into service. It carried 40,000 simultaneous telephone conversations between North America and Europe, a fivefold increase over the copper coaxial cables it replaced. The light pulses inside it traveled through hair-thin glass fibers at over $200{,}000 \text{ km/s}$, bouncing off the inside walls of the fiber thousands of times per kilometer and yet losing essentially none of their intensity over thousands of kilometers of seabed cable. By 2025, transatlantic fiber-optic systems carry essentially all transcontinental internet traffic at terabit-per-second rates. Submarine fiber bundles connect every continent except Antarctica.

The physics that makes a fiber-optic cable work is a single rule: when light inside a denser medium hits the boundary with a less-dense medium at a sufficiently glancing angle, *all* of it reflects back into the denser medium. None escapes. The boundary acts as a perfect mirror. This is *total internal reflection*, and it is the same physics that makes a diamond sparkle, lets you see fish-eye reflections of the bottom of a swimming pool from underwater, and powers the modern internet.

### The mechanism — the critical angle

Snell's law tells us that when light goes from a higher-$n$ medium to a lower-$n$ medium, it bends *away* from the normal. The angle of refraction $\theta_2$ is larger than the angle of incidence $\theta_1$. As we increase $\theta_1$, $\theta_2$ grows faster — and at some critical incidence angle, $\theta_2$ reaches $90°$, meaning the refracted ray skims along the boundary instead of crossing it.

For any larger angle of incidence, *no real refraction angle exists*. Snell's law cannot be satisfied. The ray cannot exit. It must reflect. Total internal reflection happens for any incidence angle greater than this critical angle.

The critical angle is given by setting $\theta_2 = 90°$ in Snell's law:

$$n_1 \sin\theta_c = n_2 \sin 90° = n_2,$$

$$\boxed{\theta_c = \sin^{-1}\left( \frac{n_2}{n_1} \right) \quad \text{for } n_1 > n_2.}$$

For light inside water hitting the air boundary, $\theta_c = \sin^{-1}(1.00/1.333) \approx 48.6°$. For light inside ordinary glass hitting air, $\theta_c \approx 41.8°$. For light inside diamond hitting air, $\theta_c \approx 24.4°$ — the smallest critical angle of any common material, which is exactly why diamonds sparkle.

### Why diamonds sparkle

Cut a diamond properly, and most light entering through the top face hits the back facets at angles greater than $24.4°$ from the normal. Those light rays cannot escape through the back; they totally internally reflect, bounce around inside the stone, and emerge through the top — bright and concentrated. Add dispersion (different wavelengths refract by slightly different amounts; we'll meet it again below) and the emerging light is split into spectral colors, producing the rainbow flashes of "fire" that are a diamond's visual signature. Cubic zirconia ($n \approx 2.16$) and glass ($n \approx 1.5$) sparkle less because their critical angles are larger and more light leaks out the back instead of internally reflecting.

### Fiber optics in three sentences

A fiber-optic cable is a cylinder of high-$n$ glass (the core, $n \approx 1.5$) surrounded by a thin sheath of slightly lower-$n$ glass (the cladding, $n$ slightly less than the core's). Light injected into one end of the core at an angle steeper than the core/cladding critical angle bounces back and forth between core and cladding, totally internally reflecting at every bounce, and so propagates the length of the fiber with essentially zero loss. Long-haul cables can carry signals for ~$100 \text{ km}$ before requiring amplification.

### The trade-off

Total internal reflection trades **directional flexibility for confinement.** A fiber-optic cable cannot bend more sharply than a certain radius before light starts hitting the cladding at angles smaller than the critical angle and leaking out — the "bend radius." Mirrors, by comparison, can be cut to any shape, but they reflect only ~95% of incident light at best (a few percent always absorbed). Total internal reflection gives you 100% reflection but only along directions that satisfy the critical-angle constraint.

### Worked example — critical angle for a polystyrene rod in air

A clear polystyrene rod ($n = 1.49$) is in air ($n = 1.00$). What is the critical angle for light inside the rod?

$$\theta_c = \sin^{-1}\left( \frac{1.00}{1.49} \right) = \sin^{-1}(0.671) \approx 42.2°.$$

Any ray inside the rod that hits the surface at more than $42.2°$ from the normal will totally internally reflect. The rod becomes a light pipe, conducting light along its length without leaking — the principle behind the lit-up displays of every illuminated logo and every fiber-optic Christmas tree.

**Sanity check.** The critical angle for water/air is $48.6°$ and the index of refraction of water is $1.333$. The critical angle for polystyrene/air is $42.2°$ and the index of refraction of polystyrene is $1.49$. Higher $n$ → lower $\theta_c$ → easier to trap light. Diamond's $n = 2.42$ gives the smallest critical angle ($24.4°$) of any common material and so the brightest sparkle.

### Common misconceptions

- *"Total internal reflection is a special property of certain materials."* No. It's a generic consequence of Snell's law. Any pair of materials with $n_1 > n_2$ produces total internal reflection above some critical angle.
- *"Fiber-optic cables work because light doesn't lose energy to the walls."* They work because light *never touches* the walls (in the cladding sense) — it reflects entirely within the core. Modern fibers have additional losses from absorption in the glass itself (~$0.2 \text{ dB/km}$ at $1550 \text{ nm}$), which is why amplifiers are needed for long hauls.

↳ **Dig Deeper — Dispersion and the rainbow geometry**

*The chapter mentions that different colors refract by slightly different amounts (dispersion) but doesn't work out the rainbow. Doing so is a satisfying half-hour of geometry: trace a single light ray entering a spherical drop, reflecting once off the back, exiting; compute the deflection angle as a function of incidence angle and wavelength; find the angle at which the deflection is stationary; that angle (about $42°$ from the antisolar point for red, $40°$ for violet) is where the rainbow lives.*

**Prompt:**
> Walk me through Descartes' geometric explanation of the primary rainbow. Set up a single spherical raindrop with sunlight entering parallel to the local horizontal. Trace one ray: refraction entering the drop, total or partial internal reflection off the back, refraction exiting. Use Snell's law with $n_{\text{water}} = 1.333$ for red light and $n_{\text{water}} = 1.343$ for violet light. Compute the deflection angle as a function of the impact parameter (where the ray strikes the drop). Show that there's a stationary angle of deflection — the *rainbow angle*, about $42°$ for red and $40°$ for violet from the antisolar point. End with one sentence explaining why this means the rainbow is always centered on the shadow of the observer's head.

**What to do with the output:** Save it. The rainbow is one of the most beautiful "everything-must-fit" calculations in classical physics — three pieces of geometry combine to produce a number ($42°$) you can verify with a protractor on a sunny rainy afternoon.

---

## Concept 3 — Lenses, mirrors, and the thin-lens equation

### Galileo's spyglass, Padua, 1609

Galileo Galilei is forty-five years old, a professor at the University of Padua, in chronic financial trouble. He hears a rumor — verified by colleagues — that a Dutch spectacle-maker named Hans Lippershey has built a tube containing two lenses that makes distant objects appear close. Within weeks, Galileo has reverse-engineered the device, improved its magnification from about three to about thirty, and is offering demonstrations on the bell tower of San Marco in Venice. The Senate is impressed enough to double his salary.

By December he has turned the spyglass on the night sky. He finds craters and mountains on the Moon (the Moon is *not* a perfect celestial sphere). He finds four moons of Jupiter (objects orbiting something other than Earth — a problem for the geocentric model). He finds spots on the Sun, phases of Venus, the Milky Way as a swarm of individual stars rather than a featureless glow. The spyglass — soon called a "telescope," from the Greek for "far-seeing" — turns into the instrument that breaks open the Copernican revolution.

Two lenses in a tube. That's all it took. The geometry of how lenses bend light, how rays from a distant object can be made to converge to a point, how a second lens can re-magnify the converged image — that geometry is what we'll work out now.

### The mechanism — converging and diverging lenses

A *thin lens* is a piece of transparent material (usually glass or plastic) with two carefully shaped surfaces — typically segments of spheres. The two surfaces refract incoming light twice (once entering, once leaving), and the net effect is to bend the rays.

A **converging (convex) lens** is fatter in the middle than at the edges. Rays entering parallel to the lens's optical axis converge — refract toward the axis — and cross at a point on the other side called the *focal point* $F$. The distance from the center of the lens to the focal point is the *focal length* $f$ (positive for converging lenses).

A **diverging (concave) lens** is thinner in the middle than at the edges. Parallel incoming rays diverge — refract away from the axis — as if they originated from a single point on the *same* side as the incoming light. That apparent point is the focal point of a diverging lens, and its focal length is taken to be *negative* by convention.

The *power* of a lens is the inverse of its focal length:

$$P = \frac{1}{f}.$$

The unit is the *diopter* (D), where $1 \text{ D} = 1 \text{ m}^{-1}$. A magnifying glass that focuses sunlight to a spot $8 \text{ cm}$ from its center has $f = 0.080 \text{ m}$ and $P = 1/0.080 = 12.5 \text{ D}$. Eyeglass and contact-lens prescriptions are written in diopters.

### Ray tracing: three principal rays

For any point on an object, you can locate the corresponding point on the image by drawing three special rays whose paths are easy:

1. A ray from the object point parallel to the optical axis. After the lens, this ray passes through the focal point on the far side (converging lens) or appears to come from the focal point on the same side (diverging lens).
2. A ray from the object point through the center of the lens. This ray passes straight through, undeflected (the two refractions at the front and back surfaces cancel for a thin lens at the center).
3. A ray from the object point through the focal point on the same side as the object. After the lens, this ray emerges parallel to the optical axis.

Where the three rays (or their extensions) cross on the far side is the image point. Repeat for every point on the object and you have constructed the image.

### The thin-lens and magnification equations

The geometry of similar triangles in a ray-tracing diagram gives a single equation that relates object distance $d_o$ (from object to lens), image distance $d_i$ (from lens to image), and focal length $f$:

$$\boxed{\frac{1}{d_o} + \frac{1}{d_i} = \frac{1}{f}.}$$

This is the *thin-lens equation*. It works for any thin lens — converging or diverging — and (with appropriate sign conventions) for spherical mirrors as well. The conventions:

- $d_o > 0$ if the object is on the incoming-light side of the lens (almost always).
- $d_i > 0$ if the image is on the outgoing-light side (a *real image*, which can be projected onto a screen).
- $d_i < 0$ if the image is on the incoming-light side (a *virtual image*, which only exists where the rays appear to originate; cannot be projected).
- $f > 0$ for converging lenses, $f < 0$ for diverging lenses.

The magnification is

$$m = \frac{h_i}{h_o} = -\frac{d_i}{d_o},$$

where $h_o$ and $h_i$ are object and image heights. A negative $m$ means inverted; positive means upright. $|m| > 1$ means enlarged; $|m| < 1$ means reduced.

### Mirrors: same equations, different setup

A spherical mirror obeys the same thin-lens equation if you take its focal length as half its radius of curvature:

$$f = \frac{R}{2}.$$

A *concave* mirror (curved like the inside of a bowl) is converging; $f > 0$. A *convex* mirror (curved like the outside of a ball) is diverging; $f < 0$. Concave makeup mirrors give a magnified upright image when your face is closer to the mirror than $f$. Concave parabolic dishes focus distant sunlight to a point and have been used to power solar generating stations — one in southern California (the Solar Energy Generating Systems facility, operating from 1984 to 2014) used parabolic-trough mirrors to focus sunlight onto fluid-carrying pipes for steam generation. Convex security mirrors in a store give a wide field of view at the cost of small, distorted images.

### The trade-off

Lens design trades **field-of-view for image quality.** A short-focal-length (high-power) lens lets you see at high magnification, but distorts objects far from the optical axis (off-axis aberrations). A long-focal-length lens has a narrow field of view but produces sharper images. Camera lens designers spend years balancing these constraints; eyeglass prescriptions are tuned to the specific eye they're worn on; telescopes use combinations of multiple lenses (and mirrors) to push past the limits of any single optical surface.

### Worked example — a heater with a concave reflector

An electric room heater uses a concave mirror to reflect infrared from its hot coils. The mirror has a radius of curvature $R = 50.0 \text{ cm}$, so its focal length is

$$f = R/2 = 25.0 \text{ cm}.$$

Suppose you want to project a real image of the coils $3.00 \text{ m}$ in front of the mirror — focusing the IR onto a particular spot. Where must you place the coils?

Apply the thin-lens equation, treating the mirror as a thin lens with $d_i = 3.00 \text{ m}$ and $f = 0.250 \text{ m}$:

$$\frac{1}{d_o} = \frac{1}{f} - \frac{1}{d_i} = \frac{1}{0.250} - \frac{1}{3.00} = 4.000 - 0.333 = 3.667 \text{ m}^{-1}.$$

Invert:

$$d_o = \frac{1}{3.667} \approx 0.273 \text{ m} = 27.3 \text{ cm}.$$

The coils must be just outside the focal length of the mirror (at $25.0 \text{ cm}$). Notice how sensitive the image distance is to the object distance when the object is near the focal point: at $d_o = 27.3 \text{ cm}$ the image is at $3.00 \text{ m}$; at $d_o = 25.5 \text{ cm}$ the image would be at over $12 \text{ m}$.

**Sanity check.** If you instead put the coils *exactly* at the focal point ($d_o = f = 25.0 \text{ cm}$), the equation gives $1/d_i = 0$, so $d_i = \infty$ — the rays exit parallel, producing a beam that doesn't focus anywhere. This is the geometry of a flashlight or searchlight (filament at the focal point of a parabolic mirror).

The magnification: $m = -d_i / d_o = -3.00/0.273 \approx -11.0$. The image is inverted (negative $m$) and 11 times the size of the coils. That's why heater coils are usually placed near (but not at) the focal point — you get a focused, intense, inverted image of the coils projected outward.

### Common misconceptions

- *"All images formed by lenses are real."* No. A converging lens with object inside its focal length ($d_o < f$) produces a virtual, upright, magnified image — the magnifying-glass case. A diverging lens always produces a virtual, upright, reduced image.
- *"The image is at the focal point."* Only when the object is at infinity. For any finite object distance, $d_i$ depends on $d_o$ via the thin-lens equation; it is not equal to $f$ unless the object is infinitely far away.

↳ **Dig Deeper — Aberrations: where the thin-lens equation fails**

*The thin-lens equation assumes paraxial rays — rays close to and nearly parallel to the optical axis. Real lenses have spherical aberration (rays far from the axis focus closer than rays near the axis), chromatic aberration (different colors focus at different points), and several other deviations from ideal behavior. Camera lens designers and astronomers spend careers correcting these.*

**Prompt:**
> Explain the three most important lens aberrations: spherical aberration, chromatic aberration, and coma. For each: (a) describe the physical cause in one or two sentences, (b) describe what the resulting image looks like, (c) name one technique used to correct or compensate for it (e.g., aspheric lenses, achromatic doublets, multi-element designs). End with one sentence on why expensive camera lenses (with many elements) are designed the way they are.

**What to do with the output:** Save it. The thin-lens equation is a useful idealization; understanding where it breaks down is half of practical optical engineering.

---

## Synthesis — geometry as the engine of optics

Step back. Two laws — reflection and refraction — and a regime where light's wavelength is small compared to the apparatus, give you everything in this chapter. The image in a flat mirror, the apparent shallowness of a swimming pool, the sparkle of a diamond, the workings of a fiber-optic cable, the ray-traced image through a converging lens, the focal length of a concave reflector — all of it falls out of geometry once the two boundary rules are in place.

The chapter's three concepts braid: **Concept 1** gave you the laws (reflection and Snell's law) and the underlying mechanism (light changes speed when it changes media; speed change causes direction change; the index of refraction $n = c/v$ packages the speed change into a single number). **Concept 2** showed what happens at the extreme: above the critical angle from a denser into a less-dense medium, refraction fails, and *all* the light reflects back. This single phenomenon powers diamond sparkle, fiber optics, and Galileo's apparent crisis if he had tried to look out of the bottom of a swimming pool. **Concept 3** put curvature into the boundary — lenses and mirrors are surfaces sculpted to control where rays converge — and gave you the thin-lens equation that quantitatively pins down image positions.

The deepest single fact: **light always takes the path that minimizes its travel time.** From this single rule (Fermat's principle, mentioned in the Dig Deeper above), both the law of reflection and Snell's law fall out as theorems. Geometric optics is a least-time theory; the rays we draw are paths that nature has already optimized.

### A worked example using all three concepts — a concentrating solar collector

A parabolic-trough solar collector uses a curved mirror to concentrate sunlight on a fluid-carrying pipe. Suppose the mirror is a section of a cylinder with radius of curvature $R = 80 \text{ cm}$, and the pipe runs along the focal line.

**Concept 1 — reflection.** Sunlight strikes the mirror's surface; each ray reflects so the angle of reflection equals the angle of incidence. For a properly curved (parabolic) mirror, all rays parallel to the axis reflect through a single line (the focal line of the trough).

**Concept 3 — focal length and ray tracing.** For a spherical (approximately parabolic) mirror, $f = R/2 = 40 \text{ cm}$. The pipe is placed at the focal line, $40 \text{ cm}$ from the mirror's vertex. All sunlight (effectively parallel rays from a source at infinity) converges onto the pipe.

**Concept 2 — refraction at the pipe wall.** When the concentrated sunlight enters the pipe (typically a glass tube around a black-coated absorber), it refracts at the glass surface, possibly experiences total internal reflection inside the absorber, and is absorbed as heat. The black coating ensures essentially no light escapes; what enters is absorbed.

**Computing the power per meter of pipe.** Assume insolation $I = 900 \text{ W/m}^2$ (a reasonable value for clear-day surface irradiance). The mirror is a quarter-cylinder of radius $R = 80 \text{ cm}$, so a 1-meter length of mirror has cross-sectional collection area

$$A = \frac{\pi R}{2} \cdot L = \frac{\pi (0.80)}{2} (1.00) \approx 1.26 \text{ m}^2.$$

(This treats the "quarter-cylinder" approximation from the OpenStax source.) The power collected per meter of pipe is then

$$P = I \cdot A = 900 \text{ W/m}^2 \times 1.26 \text{ m}^2 \approx 1.13 \text{ kW/m}.$$

Per meter of pipe, the system collects over a kilowatt of solar power — concentrated from over a meter of mirror down to a few centimeters of pipe.

**Scale shift.** That same physics, scaled up, runs every solar-thermal power plant in operation. Ivanpah in California's Mojave Desert (operational 2014, 392 MW peak) uses tens of thousands of computer-tracked mirrors (heliostats) to focus sunlight onto receivers atop three solar towers. Each mirror is doing the same geometric optics as a magnifying glass focusing sunlight on a leaf — just bigger, and aimed at a steam boiler instead of a fire-starter.

---

## Exercises

### Warm-up

**25.1** *(LO 1)* A ray of light strikes a mirror at $30°$ from the normal. What is the angle of reflection? What is the angle between the incident and reflected rays?

**25.2** *(LO 2)* Light traveling in air ($n = 1.00$) strikes a glass surface ($n = 1.52$) at an angle of incidence of $40°$. Find the angle of refraction.

**25.3** *(LO 3)* The critical angle for a certain liquid/air interface is $45°$. What is the index of refraction of the liquid?

**25.4** *(LO 4)* A converging lens has focal length $10.0 \text{ cm}$. An object is placed $15.0 \text{ cm}$ from the lens. Find (a) the image distance, (b) the magnification, (c) whether the image is real or virtual, upright or inverted.

### Application

**25.5** *(LO 2, LO 3)* A scuba diver shines a flashlight upward from $3.0 \text{ m}$ below the surface of a freshwater pool ($n = 1.33$). At what range of angles from the vertical does the light exit into the air? At what angles does it totally internally reflect?

**25.6** *(LO 4)* You stand $1.5 \text{ m}$ from a concave makeup mirror with focal length $0.60 \text{ m}$. Where is your image? Is it upright or inverted? What is the magnification?

**25.7** *(LO 4, LO 5)* A diverging lens of focal length $-25.0 \text{ cm}$ has an object placed $50.0 \text{ cm}$ in front of it. Find the image distance and magnification. Sketch a ray-tracing diagram showing the three principal rays.

**25.8** *(LO 4)* Eyeglasses are prescribed at $-2.5 \text{ D}$. (a) What kind of lens is this (converging or diverging)? (b) What is the focal length in cm? (c) For what kind of vision defect would this prescription be appropriate? (Foreshadowing Chapter 26.)

### Synthesis

**25.9** *(LO 1, LO 2)* A coin sits at the bottom of a glass of water $20.0 \text{ cm}$ deep. You look down at it from directly above. (a) How deep does the coin appear to be? (b) How far is the apparent image displaced (vertically) from the actual coin position?

**25.10** *(LO 4, LO 5)* A 35-mm camera uses a lens with focal length $50.0 \text{ mm}$. To photograph an object $2.00 \text{ m}$ away, where must the lens be focused (i.e., where is the image)? What is the magnification?

**25.11** *(LO 2, LO 3, LO 4)* The endoscope used in arthroscopic knee surgery uses a fiber-optic bundle to deliver light to and image from the surgical site. (a) Explain in two sentences how total internal reflection allows the bundle to bend through the joint. (b) If the core glass has $n = 1.55$ and the cladding has $n = 1.45$, what is the critical angle at the core/cladding interface?

### Challenge

**25.12** *(beyond chapter)* Derive the focal-length-half-the-radius-of-curvature relation $f = R/2$ for a spherical concave mirror. Use ray tracing for a paraxial ray (a ray close to and parallel to the optical axis) striking the mirror at small angle, applying the law of reflection at the point of contact, and using small-angle trigonometry to identify where the reflected ray crosses the axis. State explicitly where the small-angle approximation enters.

**25.13** *(beyond chapter)* The Hubble Space Telescope's primary mirror has a diameter of $2.4 \text{ m}$ and a focal length of $57.6 \text{ m}$. (a) What is the f-ratio (focal length divided by diameter)? (b) Why might astronomers prefer a high f-ratio (longer focal length per unit diameter)? (c) The Hubble was launched in 1990 with a now-famous flaw in the primary mirror — spherical aberration of about $2.2 \, \mu\text{m}$ at the edge. Why does even a sub-millimeter manufacturing error matter so much? (Forward-pointing to Chapter 27 on diffraction limits.)

---

## LLM Exercise — Chapter 25: Geometric Optics in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** An entry analyzing the geometric optics of your anchor phenomenon — a lens, mirror, prism, refracting boundary, or fiber that the phenomenon involves, with one quantitative prediction (image position, critical angle, magnification, or path of a ray).
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste your 1-sentence description].

For Chapter 25, I want to apply geometric optics — reflection, refraction, total internal reflection, and the thin-lens equation — to one optical element involved in my phenomenon.

Please:

1. Identify ONE geometric-optics element in my phenomenon. Examples: for a bike commute — the lenses in my eyes, my sunglasses (especially polarized), the curved windshield of an oncoming car that briefly reflects sun in my face, the prismatic effect of rain on the road. For a coffee maker — the curved glass of the carafe (a converging lens for the writing on the back), the reflective interior of a thermal carafe. For a basketball shot — the gym lighting reflected in the polished floor, the lens of my eye. For a marathon — the lens of my eye, my sunglasses, the apparent shimmering of the road in heat.

2. Identify which equations apply: reflection ($\theta_r = \theta_i$), Snell's law, critical angle, thin-lens equation, magnification.

3. Make ONE quantitative prediction. For a lens in your eye/sunglasses, compute focal length from prescription. For a curved reflective surface, compute image position. For a refracting boundary (water in a cup), compute the apparent shift.

4. Specify input numbers, where they come from, and what uncertainty to expect.

5. Run the calculation. Report with units and uncertainty.

6. Verify with one Fermi-style sanity check (e.g., does your computed image position match what you actually see?).

7. One sentence connecting this to Chapter 26 (vision and instruments) — you'll be analyzing the eye in detail next.

Save the output as logbook/chapter-25-geometric-optics.md.
```

### What this produces

A Logbook entry naming the optical elements in your phenomenon and pinning down at least one of them quantitatively.

### How to adapt this prompt

- *For phenomena with no obvious optics:* Default to the lens of your eye observing the phenomenon. Even reading a screen relies on geometric optics.
- *For ChatGPT/Gemini:* Identical, with interface substitutions.
- *For Claude Code:* If you have a photograph of your phenomenon, you could measure pixel positions to test ray-tracing predictions — magnification, distortion, etc.

### Connection to previous chapters

Builds directly on Chapter 24 — visible light is one band of the electromagnetic spectrum, and geometric optics is the regime where the wavelength is small compared to apparatus. Uses uncertainty propagation from Chapter 1.

### Preview of next chapter

Chapter 26 (vision and optical instruments) applies this chapter's equations specifically to the human eye, the camera, the microscope, and the telescope. The Chapter 26 LLM Exercise will ask you to model your eye — or the eye of someone observing your phenomenon — as an optical system.

---

## Chapter summary

Geometric optics treats light as straight rays that bend at boundaries between media. Two laws govern the bending: the law of reflection ($\theta_r = \theta_i$, both from the normal) and Snell's law of refraction ($n_1 \sin\theta_1 = n_2 \sin\theta_2$). The index of refraction $n = c/v$ measures how much the medium slows the light. Above a critical angle, light going from a high-$n$ to a low-$n$ medium totally internally reflects — the principle behind fiber optics and the sparkle of diamonds. Lenses and curved mirrors apply the same boundary physics to a curved surface to produce images at predictable positions, given by the thin-lens equation $1/d_o + 1/d_i = 1/f$.

The one idea that matters most: **light obeys geometric rules at boundaries, and from those rules everything in this chapter is derivable.** No new physics is needed for fiber optics, the rainbow, the lens of your eye, or the Hubble telescope — just the two boundary laws and patient geometry.

The common mistake to watch for: **measuring angles from the surface instead of from the normal.** Snell's law and the law of reflection both use the normal as their reference; angles measured from the surface give you nonsense answers (and were a frequent freshman lab error during the author's own undergraduate days).

What you should now be able to teach someone else: why a swimming pool looks shallower than it is, why diamonds sparkle, how a fiber-optic cable transmits light around bends with essentially no loss, and how to compute where the image of an object will appear given the focal length of a lens. If you can teach those four things to a friend, you've understood this chapter.

---

## What would change my mind

The chapter argues that geometric optics is essentially exact whenever the wavelength of light is small compared to the apparatus — that the ray picture captures all observable phenomena in this regime. The argument would need revision if a precision experiment found image positions deviating from the thin-lens equation by amounts larger than aberration corrections can account for, or if total internal reflection were observed to leak above the critical angle in vacuum (it does, slightly, in some quantum-mechanical setups — the *evanescent wave* — but not at scales geometric optics is meant to describe).

## Still puzzling

The deepest unresolved question this chapter raises and does not answer: **why does light travel at exactly $c$ in vacuum, and exactly $c/n$ in a medium with index of refraction $n$?** The microscopic explanation involves photons interacting with bound electrons in the medium, getting absorbed and re-emitted with phase shifts. But the resulting wave-equation derivation has $\varepsilon$ and $\mu$ as inputs, and *why* those constants take the values they do — for vacuum or for any specific material — remains a question for a deeper theory than classical electromagnetism.

---

## Connections forward

Chapter 26 (vision and optical instruments) applies this chapter's lens equations specifically to the eye, the camera, the microscope, and the telescope — including the corrections of common vision defects (myopia, hyperopia, presbyopia, astigmatism) using prescription lenses. Chapter 27 (wave optics) returns to the wave nature of light and shows where geometric optics breaks down — interference, diffraction, polarization. Chapter 29 (quantum mechanics) reveals that light is also discrete photons, and that the index of refraction has a microscopic explanation rooted in atomic-scale electron dynamics. Chapter 32 (medical applications of nuclear physics) uses fiber-optic endoscopes — direct descendants of the principles in this chapter — for in-body imaging and surgery.

---

**Tags:** geometric-optics, Snell-law, total-internal-reflection, thin-lens-equation, fiber-optics

---

## AI Wayback Machine

**Willebrord Snell** discovered the law of refraction in 1621 — the sine relation between angles in different media. The discovery sat unpublished in his notebooks; Descartes published the law a generation later, often without crediting Snell.

**Run this:**

```
Who was Willebrord Snell, and how does Snell's law connect to the geometric optics we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Willebrord Snellius"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to derive Snell's law from Fermat's principle of least time.
- Ask it about the priority dispute between Snell and Descartes — and how the law is named in different countries.

What changes? What gets better? What gets worse?
