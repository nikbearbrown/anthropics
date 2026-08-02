# Chapter 25 — Geometric Optics

*Two rules at a boundary, and the whole visible world falls out.*

---

Here is something worth noticing before we start: visible light has a wavelength between 400 and 750 nanometers. The lens in your eye is about 9 millimeters across. The ratio is roughly 20,000 to 1. When the wavelength of a wave is that much smaller than whatever it's interacting with, the wave behaves, for almost all practical purposes, exactly like a ray — a straight geometric line that bends at boundaries according to simple rules.

This is the regime of geometric optics. We are not ignoring wave effects because they don't exist; we are ignoring them because they are completely negligible at the scale of any object you can see with your naked eye. The error introduced by treating light as a ray rather than a wave, for a glass lens a centimeter across, is smaller than the width of a human hair. Geometric optics is not an approximation that makes the physics tractable — it is an approximation that is simply true, to the precision of any experiment you can do in a teaching laboratory.

And from two rules — one for bouncing, one for bending — everything visible follows.

---

## The two rules

**Reflection.** When a ray of light strikes a smooth surface, the angle it makes with the normal to the surface on the way in equals the angle it makes with the normal on the way out:

$$\theta_r = \theta_i.$$

Both angles measured from the *normal* — the line perpendicular to the surface at the point of impact. The incident ray, the normal, and the reflected ray all lie in one plane. That is the complete law. It works for any wave on any smooth surface.

**Refraction.** When light passes from one transparent medium into another, it changes speed. If the medium is denser (higher index of refraction), it slows down; if less dense, it speeds up. The frequency is fixed by the source — only the wavelength changes. When the wave slows down, its wavefronts crowd together, which means the direction of travel bends toward the normal. When it speeds up, the wavefronts spread apart, and the ray bends away from the normal.

The **index of refraction** is defined as

$$n = \frac{c}{v},$$

![Bar chart of refractive index n for common materials: vacuum 1.000, air 1.0003, water 1.33, glass 1.5, diamond 2.42. Speed of light v = c/n labeled on each. Inset: n varies slightly with wavelength (dispersion).](../images/25-geometric-optics-fig-05.png)
*Figure 25.5 — Refractive Index — Vacuum to Diamond, and Why Diamonds Sparkle*

the ratio of the vacuum speed of light to the speed of light in the medium. In vacuum, $n = 1$ exactly. In air, $n \approx 1.0003$ — we'll treat it as 1. In water, $n \approx 1.333$. In ordinary glass, $n \approx 1.5$. In diamond, $n \approx 2.42$.

The relation between the angles on both sides of a boundary — Snell's law — follows from requiring that the wavefronts match up continuously at the interface:

$$n_1 \sin\theta_1 = n_2 \sin\theta_2.$$

Both angles measured from the normal. When light goes from air into water ($n$ increases), $\sin\theta_2 < \sin\theta_1$, so $\theta_2 < \theta_1$: the ray bends toward the normal. When light goes from water into air, the opposite: it bends away.

That's the entire foundation of this chapter. Everything else is geometry.

![Light incident on a glass surface at angle θ₁ from the normal. Reflected ray at θ_r = θ₁. Refracted ray bends toward the normal in denser medium (n₂ > n₁). Snell: n₁ sin θ₁ = n₂ sin θ₂. Air n=1.00; glass n=1.5.](../images/25-geometric-optics-fig-02.png)
*Figure 25.2 — Reflection & Snell's Law — Two Rules That Run All of Geometric Optics*

<!-- → [INFOGRAPHIC: Two-panel diagram — (1) reflection: incident ray, normal, reflected ray at equal angles θᵢ = θᵣ from normal, labeled clearly; (2) refraction: ray in medium n₁ bending at boundary into medium n₂, with θ₁ and θ₂ labeled from the normal, n₂ > n₁ so ray bends toward normal; caption: both angles are always measured from the normal, never from the surface — the single most common error in applying these laws] -->

---

## Why a swimming pool lies to you

Light from a coin at the bottom of a pool travels upward through water, hits the water/air boundary, and bends away from the normal as it enters the less dense medium. To the observer looking down, the rays appear to originate from a point that is *shallower* than the actual coin. For nearly vertical viewing, the small-angle version of Snell's law gives the apparent depth directly:

$$d_\text{apparent} = \frac{d_\text{actual}}{n_\text{water}} = \frac{d_\text{actual}}{1.333}.$$

A pool 4 feet deep looks about 3 feet deep. Every swimming-pool sign warning "4 FEET" is telling you the actual depth, not what your eyes report. Herons have learned, by some combination of instinct and experience, to compensate. Spearfishers learn it too, as a skill.

The image the observer sees is a *virtual image* — a point from which the rays appear to diverge, but where no physical ray actually converges. The coin is not there. There is only the geometry of bent light, and the brain's insistence on projecting rays back in straight lines.

![Glass of water with submerged straw. Light from the submerged portion refracts as it exits the water-air interface, bending away from the normal. The eye traces the refracted rays straight back, placing the apparent submerged...](../images/25-geometric-optics-fig-06.png)
*Figure 25.6 — Why a Straw Looks Bent — Brain Traces Light Rays in Straight Lines*

The same displacement applies everywhere the boundary is flat and the media are uniform. A glass of water makes the printed text below it appear closer. Your aquarium fish is not where it looks. The bent-straw illusion is refraction at the air/water boundary. One law, many consequences.

<!-- → [IMAGE: Side-view diagram of a coin at the bottom of a pool — actual ray paths from the coin bending away from the normal at the water surface, with dashed extensions showing the virtual image location at apparent depth d_actual/n; observer eye above the surface; labels: "actual depth," "apparent depth = actual/n," "virtual image"; caption: the brain traces rays backward in straight lines, placing the coin where the dashed extensions cross — shallower than it actually is] -->

---

## Total internal reflection: when the boundary becomes a perfect mirror

Now for something more dramatic. Snell's law says

$$\sin\theta_2 = \frac{n_1}{n_2}\sin\theta_1.$$

When light travels from a denser medium into a less dense one ($n_1 > n_2$), the factor $n_1/n_2 > 1$. As $\theta_1$ increases, $\sin\theta_2$ grows faster. At some critical angle $\theta_c$, we get $\sin\theta_2 = 1$, meaning $\theta_2 = 90°$ — the refracted ray skims along the boundary, going nowhere useful.

For any $\theta_1 > \theta_c$, there is no real solution for $\theta_2$. The mathematics has no answer. The physics does: the light cannot exit. It reflects back into the dense medium with 100% efficiency. This is **total internal reflection**.

The critical angle is

$$\theta_c = \sin^{-1}\!\left(\frac{n_2}{n_1}\right).$$

For water/air: $\theta_c = \sin^{-1}(1/1.333) \approx 48.6°$. For glass/air: $\theta_c \approx 41.8°$. For diamond/air: $\theta_c \approx 24.4°$.

That last number is why diamonds sparkle. Cut a diamond so that most light entering the top face strikes the back facets at angles steeper than $24.4°$ from the normal, and none of it can leak out the back. It bounces. It bounces again. Eventually it emerges through the top, concentrated and bright. Add the fact that different wavelengths refract by slightly different amounts (dispersion — red bends less than violet, giving slightly different critical angles), and the emerging light separates into spectral colors: the fire of a cut diamond.

Glass has $\theta_c \approx 42°$, which is large enough that many light rays entering the top of a glass stone *can* escape through the back. Glass imitations of diamond are noticeably duller. The sparkle is a consequence of a number — $n = 2.42$ — and the geometry that follows from it.

<!-- → [INFOGRAPHIC: Sequence of three rays hitting a glass/air boundary from inside — (1) angle below critical angle: most light refracts out, small reflected ray; (2) at critical angle: refracted ray grazes boundary at 90°; (3) above critical angle: no refracted ray, all light reflects back into glass; the three panels make the transition to total internal reflection visually clear] -->

---

## Fiber optics in three sentences

A fiber-optic cable is a cylinder of high-$n$ glass (the core, $n \approx 1.5$) surrounded by a thin sheath of slightly lower-$n$ glass (the cladding). Light injected into one end of the core at an angle steeper than the core/cladding critical angle bounces back and forth between core and cladding, totally internally reflecting at every bounce, and propagates the length of the fiber with essentially zero geometric loss. Modern long-haul submarine cables carry essentially all transcontinental internet traffic at terabit-per-second rates — starting in 1988 with TAT-8 across the Atlantic, running at a then-staggering 40,000 simultaneous phone calls, and scaling by orders of magnitude every decade since.

The bend radius of a fiber cable is limited by the critical angle: bend the fiber too sharply and some rays hit the cladding at angles below $\theta_c$, leak out, and the signal degrades. This is why fiber-optic cables have minimum bend-radius specifications, and why bending them sharply in a router cabinet is a genuine engineering failure mode, not a cosmetic concern.

---

## Lenses: curvature as a tool

The flat-boundary cases — mirrors, refraction at a water/air interface, fiber walls — are one application of the two rules. The really powerful application is the curved boundary: a lens.

A **lens** is a piece of transparent material bounded by two curved surfaces (typically spherical). When a ray enters the lens, it refracts at the first surface; when it exits, it refracts at the second. The combined effect, for a thin lens with appropriate curvature, is to redirect all rays from a single object point through a single image point.

The focal length $f$ of a lens is the image distance when the object is infinitely far away — when the incoming rays are parallel. Parallel rays entering a **converging (convex) lens** — fatter in the middle — cross at the focal point on the far side. Parallel rays entering a **diverging (concave) lens** — thinner in the middle — diverge as if they came from a focal point on the *same* side as the incoming light. The focal length of a converging lens is positive; of a diverging lens, negative.

The **lens power** is $P = 1/f$, measured in diopters (D) where $1 \text{ D} = 1 \text{ m}^{-1}$. Eyeglass and contact prescriptions are written in diopters. A $-2.5$ D prescription means a diverging lens with $f = -40$ cm; the negative sign tells you the person is nearsighted and the lens must spread rays out before the eye converges them.

---

## The thin-lens equation

The geometry of similar triangles inside a ray diagram produces a single algebraic relation:

$$\frac{1}{d_o} + \frac{1}{d_i} = \frac{1}{f},$$

where $d_o$ is the distance from the object to the lens and $d_i$ is the distance from the lens to the image. This is the **thin-lens equation**.

Sign conventions: $d_o > 0$ for a real object (on the incoming side). $d_i > 0$ for a real image (on the outgoing side, where the rays actually converge — can be projected on a screen). $d_i < 0$ for a virtual image (on the same side as the incoming light, where rays only appear to originate — like your bathroom mirror). $f > 0$ for converging, $f < 0$ for diverging.

The lateral **magnification** is

$$m = -\frac{d_i}{d_o}.$$

Negative magnification means the image is inverted. A camera forms a real, inverted, diminished image of the scene in front of it. A magnifying glass held close to text forms a virtual, upright, enlarged image behind the lens.

The same equation — same form, same sign conventions — applies to spherical mirrors, with the focal length $f = R/2$ where $R$ is the radius of curvature. Concave mirrors are converging ($f > 0$); convex mirrors are diverging ($f < 0$). The concave makeup mirror that gives you a magnified upright image of your face is doing the same algebra as the glass microscope objective above a specimen slide.

![Two side-by-side ray diagrams. Converging lens (f > 0): parallel ray refracts through far focal point; ray through center continues straight; ray through near focal point exits parallel. Real, inverted image. Diverging lens:...](../images/25-geometric-optics-fig-04.png)
*Figure 25.4 — Thin-Lens Ray Diagrams — Three Principal Rays Locate the Image*

<!-- → [TABLE: Thin-lens equation cases — columns: object position, image position (from equation), real or virtual, upright or inverted, magnified or diminished, everyday example; rows: object at infinity (d_i = f, real), object beyond 2f (f < d_i < 2f, real, inverted, reduced, camera), object at 2f (d_i = 2f, real, inverted, same size), object between f and 2f (d_i > 2f, real, inverted, enlarged, projector), object inside f (d_i < 0, virtual, upright, enlarged, magnifying glass), diverging lens any position (d_i < 0, virtual, upright, reduced, eyeglass for myopia)] -->

---

## Three principal rays

You don't always need the equation. For a quick qualitative picture, three special rays through a converging lens are enough:

1. A ray entering parallel to the axis passes through the focal point on the far side.
2. A ray through the center of the lens continues straight through, undeviated.
3. A ray through the focal point on the incoming side exits parallel to the axis.

Where these three rays converge (or appear to converge, when extended backward) is the image point. Draw them for one point on the object — the tip of an arrow, say — and the character of the image (real/virtual, upright/inverted, larger/smaller) is immediately visible without solving an equation.

The equation tells you the numbers. The ray diagram tells you whether you've set the problem up correctly. Do both.

<!-- → [INFOGRAPHIC: Side-by-side ray diagrams for a converging lens — (1) object beyond 2f: three principal rays converging to a real, inverted, reduced image; (2) object between f and 2f: three principal rays converging to a real, inverted, enlarged image (projector geometry); (3) object inside f: three principal rays diverging, traced back to a virtual, upright, enlarged image (magnifying glass); caption: same lens, three qualitatively different outcomes depending only on object position relative to f] -->

---

## A calculation worth doing: Galileo's telescope

Galileo's 1609 telescope used two lenses: a converging objective and a diverging eyepiece. The principle is simple but the consequences were not.

The objective lens had a long focal length — estimates put it around $f_\text{obj} \approx 1.7$ m. Stars and planets are effectively at infinity, so the objective forms a real image at its focal point, 1.7 m behind the lens. The eyepiece — a diverging lens with $f_\text{eye} \approx -5$ cm — is placed just inside that focal point. The eyepiece views the real image as a virtual object and produces a magnified virtual image that the eye then focuses on.

The angular magnification of a telescope in normal adjustment (image at infinity) is

$$M = -\frac{f_\text{obj}}{f_\text{eye}} = -\frac{170 \text{ cm}}{-5 \text{ cm}} = +34.$$

Galileo's best instruments achieved about $30\times$ magnification, consistent with this. The positive sign on a Galilean telescope means the image is upright — which is why it remained popular for terrestrial observation even as Keplerian telescopes (two converging lenses, inverted image) gave sharper astronomical views.

What Galileo saw with those 30 magnified degrees: mountains and craters on the Moon (the celestial sphere is not perfect). Four moons orbiting Jupiter (bodies orbit things other than Earth). Phases of Venus (Venus orbits the Sun, not the Earth). The Milky Way resolving into individual stars. In roughly four months of observation in late 1609 and early 1610, he accumulated enough anomalies to end the Ptolemaic cosmological model. It was two glass lenses, some careful geometry, and intellectual honesty about what the observations meant.

$$M = -\frac{f_\text{obj}}{f_\text{eye}}$$

is not just a formula. It is the equation that opened the heliocentric universe.

<!-- → [INFOGRAPHIC: Galilean telescope ray diagram — parallel rays from a distant star entering the long converging objective (f_obj = 1.7 m), converging toward the focal point; the diverging eyepiece (f_eye = -5 cm) placed just inside that focal point, intercepting the converging rays and redirecting them as a parallel beam into the eye; labels showing f_obj, f_eye, tube length, and the emerging angular magnification M = f_obj/|f_eye| ≈ 34; inset: comparison of angular size of Jupiter's disk as seen naked-eye vs. through the 30× instrument] -->

---

## Where geometric optics comes from, really

There is a deeper reason the two boundary rules take the forms they do. Light, it turns out, travels along the path that takes the *minimum time* between any two points. This is **Fermat's principle of least time**, and from it, both the law of reflection and Snell's law are theorems — not additional assumptions but mathematical consequences of one prior principle.

The derivation of Snell's law from Fermat's principle is a standard piece of calculus-level geometry: set up the total travel time as a function of where the ray crosses the boundary, differentiate with respect to that crossing point, set the derivative to zero, and Snell's law drops out in three lines.

This is not a curiosity. The same philosophical structure — *physical systems take the path that extremizes something* — recurs throughout physics. In classical mechanics, particles follow trajectories that minimize the action (Hamilton's principle). In quantum mechanics, all possible paths contribute to the probability amplitude, and the classical path is the one where the amplitudes constructively interfere (Feynman's path integral). The minimum-time principle of geometric optics is the first and simplest member of a family of extremal principles that eventually encompasses all of fundamental physics.

Geometric optics is not just about lenses and rainbows. It is, in its bones, the same kind of physics as everything else.

<!-- → [INFOGRAPHIC: Fermat's principle derivation sketch — two points A (in medium n₁) and B (in medium n₂) separated by a horizontal boundary; a ray crossing the boundary at point P whose horizontal position x is variable; total travel time T(x) written as sum of two segments; the graph of T(x) showing a minimum; the tangent condition at the minimum labeled as Snell's law n₁sinθ₁ = n₂sinθ₂; caption: the ray bends at the boundary not because it "knows" Snell's law, but because the path of minimum time happens to satisfy it — the same logic as Fermat's principle in every other physical system] -->

---

## A calculation worth doing: the rainbow

![Cross-section of a water droplet showing white sunlight entering and refracting at the front surface, reflecting once off the back, then refracting again on exit. Dispersion separates the colors. Primary rainbow appears at...](../images/25-geometric-optics-fig-01.png)
*Figure 25.1 — Al-Farisi's Rainbow (1276) — Refraction, Internal Reflection, and Dispersion*

Kamal al-Din al-Farisi, working in 14th-century Persia, built a large glass sphere filled with water to simulate a single raindrop, placed it in a darkened room, and traced how sunlight enters, reflects internally, and exits. He had the correct geometric explanation of the rainbow. Let us follow the calculation.

A ray of sunlight enters a spherical raindrop at some height above its center — the impact parameter. At the front surface it refracts into the water; at the back surface it partially reflects internally; at the front surface again it refracts back into air. The total deflection angle of the ray — how much its final direction deviates from its original direction — depends on where it strikes the drop.

For $n_\text{water} = 1.333$ (red light), working through the geometry shows that the deflection angle has a *minimum* at a specific impact parameter. The minimum deflection for red light is about $138°$ from the forward direction, or equivalently $180° - 138° = 42°$ from the antisolar direction (the point directly opposite the Sun in the sky).

For violet light ($n \approx 1.343$), the minimum deflection is about $40°$ from the antisolar direction.

The physical significance of the minimum: near a minimum, many rays of slightly different impact parameters emerge at nearly the same angle. The light *piles up* at that angle. The rainbow is not just a band of refracted light — it is the caustic of refracted light, the edge where intensity concentrates. Every droplet in the sky at $42°$ from the antisolar point sends red light to your eye; every droplet at $40°$ sends violet. The band between them contains the intermediate colors.

The rainbow is always centered on the shadow of your head. If you are standing such that the Sun is behind you, the antisolar point is directly in front of you. The circular arc of the rainbow surrounds that point at $40°$–$42°$. You cannot see more of the arc than the horizon allows. From a plane or a tall waterfall, you can sometimes see the full circle.

One geometric law, applied twice at the surface of a sphere, produces a precise prediction of where in the sky a rainbow must appear, which colors appear where, and why the sky is brighter inside the arc than outside. Farisi had the right picture in the 1270s. Descartes worked out the mathematics in 1637. The numbers match observed rainbows to better than a degree. Geometric optics, and patience.

<!-- → [INFOGRAPHIC: Raindrop diagram showing Farisi/Descartes ray tracing — one ray entering at an impact parameter, refraction at front surface, internal reflection at back, refraction at front surface again; labeled angles at each surface; below the drop, a graph of deflection angle vs. impact parameter showing the minimum near 138° for red light; caption: the rainbow appears at 42° from the antisolar point because that is where the deflection curve has its minimum — many rays concentrate there, producing intense color] -->

---

## Three commitments

**Light bends at boundaries according to two rules.** $\theta_r = \theta_i$ for reflection; $n_1\sin\theta_1 = n_2\sin\theta_2$ for refraction. Angles always from the normal.

![Two panels. Left: below critical angle, light refracts out of glass into air. Right: at angles above θ_c (sin θ_c = n_air/n_glass ≈ 1/1.5, θ_c ≈ 42°), light reflects entirely back into glass. Inset: fiber-optic cable bouncing...](../images/25-geometric-optics-fig-03.png)
*Figure 25.3 — Total Internal Reflection — Above θ_c, Light Stays in the Glass*

**When light tries to go from dense to sparse at too steep an angle, it can't.** Above the critical angle $\theta_c = \sin^{-1}(n_2/n_1)$, total internal reflection is 100% efficient. This is the principle behind fiber optics, the diamond's fire, and the apparent silvering of a glass surface viewed steeply from underwater.

**Curved surfaces focus light.** The thin-lens equation $1/d_o + 1/d_i = 1/f$ describes any lens or spherical mirror. The magnification is $m = -d_i/d_o$. The sign of $f$ tells you converging or diverging; the sign of $d_i$ tells you real or virtual; the sign of $m$ tells you upright or inverted.

The deepest fact: **both boundary laws follow from a single principle — light takes the path of least time.** Geometric optics is a minimum-time theory. The rays we draw are the paths nature has already selected.

---

## Exercises

### Warm-up

**25.1** *(Reflection)* A ray strikes a flat mirror at $35°$ from the surface. What is the angle of incidence measured from the normal? What is the angle of reflection?

**25.2** *(Snell's law — air to glass)* A ray in air ($n = 1.00$) strikes a glass surface ($n = 1.52$) at an angle of incidence of $45°$. Find the angle of refraction inside the glass. Does the ray bend toward or away from the normal?

**25.3** *(Apparent depth)* A goldfish swims $30$ cm below the surface of water ($n = 1.333$) in a tank. How deep does the fish appear to be when viewed from directly above?

**25.4** *(Critical angle)* Find the critical angle for total internal reflection at a glass/air interface, given $n_\text{glass} = 1.50$.

**25.5** *(Thin-lens equation — real image)* A converging lens has focal length $f = 20$ cm. An object is placed $30$ cm from the lens. Find the image distance and the magnification. Is the image real or virtual? Upright or inverted?

### Application

**25.6** *(Snell's law — two boundaries)* A ray of light passes from air through a flat glass plate ($n = 1.5$) and back into air. The angle of incidence at the first surface is $50°$. (a) Find the angle of refraction inside the glass. (b) Find the angle at which the ray exits the second surface (parallel to the first). (c) Why does the ray emerge parallel to the original direction?

**25.7** *(Total internal reflection — fiber core)* A fiber-optic core has $n_\text{core} = 1.62$ and cladding $n_\text{clad} = 1.52$. (a) Find the critical angle at the core/cladding interface. (b) A ray inside the core strikes the interface at $72°$ from the normal. Does it undergo total internal reflection?

**25.8** *(Diverging lens)* A diverging lens has focal length $f = -15$ cm. An object is placed $40$ cm from the lens. (a) Find the image distance. (b) Find the magnification. (c) Characterize the image: real or virtual, upright or inverted, enlarged or reduced.

**25.9** *(Mirror)* A concave mirror has radius of curvature $R = 60$ cm. An object sits $50$ cm from the mirror. (a) What is the focal length? (b) Where is the image? (c) What is the magnification?

### Synthesis

**25.10** *(Snell's law + critical angle + geometry)* You are underwater in a swimming pool ($n = 1.333$) looking up at the surface. (a) At what angle from the vertical does the entire outside world appear compressed into a cone? (b) At angles greater than this, what do you see instead? (c) A fish in an aquarium appears to be $12$ cm from the glass wall when viewed from outside through water. The actual distance is $16$ cm. Use the apparent-depth formula to check this.

**25.11** *(Telescope magnification)* A refracting telescope has an objective lens of focal length $80$ cm and an eyepiece of focal length $4$ cm. (a) What is the angular magnification? (b) For an object at infinity, where does the objective form its intermediate image? (c) What is the total tube length of the telescope from objective to eyepiece in normal adjustment?

**25.12** *(Two-lens system)* A projector uses a converging lens ($f = 10$ cm) to project a slide onto a screen $3.0$ m away. (a) How far from the lens must the slide be placed? (b) What is the magnification? (c) If the slide image is $24$ mm × $36$ mm, how large is the projected image on the screen?

### Challenge

**25.13** *(Rainbow geometry)* The primary rainbow appears at approximately $42°$ from the antisolar point for red light. A secondary rainbow — fainter, with reversed color order — appears at about $51°$. The secondary involves two internal reflections inside the raindrop rather than one. (a) Explain qualitatively why two internal reflections reverse the color order compared to one. (b) Why is the sky noticeably darker between the primary and secondary arcs (Alexander's dark band)? (c) What would you expect for a tertiary rainbow, and why is it almost never seen?

**25.14** *(Lens-maker's equation — beyond chapter)* The thin-lens equation tells you what a lens with a given $f$ does, but not why $f$ has the value it has. The lensmaker's equation connects $f$ to the geometry of the two surfaces:

$$\frac{1}{f} = (n-1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right),$$

where $R_1$ and $R_2$ are the radii of curvature of the two surfaces (positive if the center of curvature is on the outgoing side). (a) For a symmetric biconvex lens of glass ($n = 1.5$) with both radii $R = 10$ cm, compute the focal length. (b) For a plano-convex lens (one flat surface, $R_2 = \infty$) of the same glass with $R_1 = 10$ cm, compute $f$. (c) Why is the biconvex lens more powerful than the plano-convex?

---

## Still puzzling

The one thing geometric optics cannot explain about itself: *why does light travel at $c$ in vacuum and at $c/n$ in a medium?* The $n$ of water is $1.333$. Why not $1.400$? Why not $1.250$? The answer requires a quantum-mechanical treatment of how photons interact with bound electrons in the medium — absorption and re-emission with phase shifts, summed over all atoms in the path. The classical electromagnetic theory gives you $n$ as a parameter whose value it cannot predict from first principles. Quantum mechanics predicts it, in principle; calculating it for a real material requires the full electronic structure of the atoms involved. We use $n$ as a measured input throughout this chapter, and trust that the deeper explanation exists.

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

## Connections forward

Chapter 26 applies this chapter's lens equations to the eye, the camera, the microscope, and the telescope — and to the correction of vision defects with prescription lenses. Chapter 27 returns to the wave nature of light and shows where geometric optics fails: interference, diffraction, and the resolution limit of any optical instrument. Chapter 29 gives the microscopic account of the index of refraction — why $n$ is what it is in each medium — rooted in the quantum mechanics of atomic electrons. The two rules of this chapter are not the whole story of light, but they are the foundation on which everything else is built.

---

**Tags:** geometric-optics, Snell-law, total-internal-reflection, thin-lens-equation, fiber-optics, Feynman-style
