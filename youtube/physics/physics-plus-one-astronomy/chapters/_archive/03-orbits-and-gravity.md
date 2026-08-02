# Chapter 3 — Orbits and Gravity

*What Keeps the Cosmos from Falling Into Itself.*

---

I want to tell you about a question that bothered Newton for years.

He already knew that the Moon was falling. He could calculate the acceleration — the rate at which the Moon's path curves toward Earth's center — and it worked out to about 0.0027 meters per second squared. Small, but not zero. The Moon is definitely being pulled toward Earth. So why doesn't it arrive?

The answer he found is one of those ideas that seems simple once you hear it and then, if you sit with it long enough, becomes strange again. The Moon doesn't arrive because it's also moving sideways. It falls toward Earth, but it's moving fast enough horizontally that Earth's surface curves away beneath it at the same rate. The Moon is always falling. It just keeps missing.

An orbit is not an object being held up. It is an object falling around a curved world. Once you understand that, everything else in this chapter — Kepler's three laws, Newton's law of gravitation, escape velocity, the discovery of Neptune before anyone had seen it — all of it follows from that one geometric fact.

<!-- → [DIAGRAM: the "falling Moon" geometry — a large curved arc of Earth's surface at the bottom, with a satellite moving horizontally to the right at orbital altitude; two annotated arrows: one pointing downward labeled "gravity pulls Moon ~5m downward" and one horizontal labeled "Moon travels ~8km sideways"; show that Earth's curved surface also drops ~5m over that same 8km horizontal distance so the ground always stays the same distance away; this is the single load-bearing visual for the chapter and should appear here, before any Kepler or Newton equation] -->

---

## What Kepler Found Without Knowing Why

Let's start with the data, because that's where the story actually starts.

Johannes Kepler arrived in Prague in 1600 to work for the astronomer Tycho Brahe. Brahe had spent twenty years tracking the positions of planets with obsessive precision — no telescope, just careful sighting instruments and relentless repetition. He had the best observational record in history. What he could not do was find the pattern in it. That was Kepler's job.

The obvious thing to try was circles. Aristotle had declared the heavens perfect, and circles were the perfect shape — no beginning, no end, equal in every direction. Centuries of astronomical tradition agreed. Kepler tried circles. He adjusted their sizes, shifted their centers, combined them in various ways. The data refused to fit. Mars was the worst offender. The predicted positions disagreed with Brahe's measurements by amounts too large to blame on observational error.

Kepler's response to this is worth noticing. He did not adjust his standards downward to make the disagreement acceptable. He accepted that circles were wrong and looked for another shape.

The shape that worked was an ellipse. An ellipse is what you get when you cut a cone at an angle to its axis — elongated, a squashed circle. It has two focal points instead of one center, and its defining property is this: for any point on the ellipse, the sum of the distances to the two focal points is constant. Pick any point, draw lines to each focus, add the lengths — you always get the same number.

When Kepler placed the Sun at one focus of an ellipse — not the center, one focus — Mars fit. Not approximately. Exactly.

<!-- → [DIAGRAM: side-by-side — left: a circle with a single center point; right: an ellipse with two labeled focal points F1 and F2, a point P on the ellipse, lines drawn from P to each focus, and the annotation "F1P + F2P = constant (always the same regardless of where P is)"; a second small callout shows a planetary orbit ellipse with "Sun" at F1 and "empty focus" at F2, perihelion labeled at the closest point and aphelion at the farthest; student should immediately see both why the ellipse is the right shape and why the Sun is off-center] -->

This was his first law: each planet moves in an ellipse with the Sun at one focus. The other focus is empty. Nothing sits there. This is not a minor detail. It means the planet is sometimes closer to the Sun and sometimes farther away. Mercury's distance from the Sun varies between 46 million and 70 million kilometers over a single orbit. At closest approach, it absorbs nearly twice as much solar energy as at its farthest point. The assumption of a constant distance — a circle — was never going to work.

The second law describes what happens to the planet's speed as it moves around this ellipse. As a planet orbits, the line from the planet to the Sun sweeps out equal areas in equal times. This sounds geometric, almost arbitrary. What it actually says is: the planet speeds up when it gets close to the Sun, and slows down when it moves away. At closest approach, gravity is pulling harder — the planet races through the near part of its orbit. Far away, gravity is weaker — the planet coasts through the distant part. The rate of sweeping stays constant throughout.

<!-- → [DIAGRAM: an elliptical orbit with the Sun at one focus; two shaded wedge-shaped areas drawn — one narrow and long near perihelion (planet moves fast, covers a large arc in time Δt), one wide and short near aphelion (planet moves slow, covers a small arc in the same time Δt); both shaded areas are equal in size; label "perihelion: fast", "aphelion: slow", and "A₁ = A₂" with arrows indicating the equal areas; the visual makes the abstract "sweeps equal areas" law into a concrete speed comparison] -->

The third law connects the size of an orbit to the time it takes to complete it. The square of a planet's orbital period equals the cube of its semimajor axis — the "average radius" of the ellipse, half its longest diameter. If you measure the period in Earth-years and the distance in astronomical units (the Earth-Sun distance), the relationship is just:

$$P^2 = a^3$$

Check it on Jupiter. Period: 11.86 years. Distance: 5.2 AU. $(11.86)^2 = 140.7$. $(5.2)^3 = 140.6$. The law holds. Try Pluto: period 248 years, distance 39.5 AU. $(248)^2 = 61{,}504$. $(39.5)^3 = 61{,}630$. The law holds across the entire solar system.

Here is what Kepler could not do: explain why. He had found the geometry of planetary orbits by staring at data until the pattern appeared. He suspected some force from the Sun was responsible — he even used the word "gravity" — but he had no mathematical framework to derive what he had found. The three laws were correct, precise, and deeply mysterious.

That mystery lasted about sixty years.

---

## Newton's Unification

In 1665, plague closed Cambridge University, and Newton went home to Lincolnshire. He was 23 years old. Over the next 18 months, he worked out the mathematics of gravity.

The question he started with was simple to state: if a force is pulling the Moon toward Earth, what is the mathematical form of that force? How does it depend on distance?

<!-- → [DIAGRAM: Newton's cannonball — a tall mountain rising above a curved Earth; four cannonball trajectories fired horizontally at increasing speeds: (1) slow, curves steeply and hits nearby; (2) medium, hits farther away; (3) fast, long arc, hits much farther; (4) orbital speed, the trajectory curves exactly parallel to Earth's surface and closes into a full orbit; annotate "orbital speed ≈ 7.9 km/s" at trajectory 4; this is Newton's own thought experiment from the Principia and the visual that proves the Moon and a cannonball are governed by the same physics] -->

He knew the Moon's orbital period (about 27 days) and its distance from Earth (about 60 Earth-radii). From these, he could calculate the acceleration the Moon needed to stay in its orbit — the centripetal acceleration, directed toward Earth's center. He got $0.0027$ m/s$^2$.

He also knew the acceleration due to gravity at Earth's surface: $9.8$ m/s$^2$.

The ratio is $9.8 / 0.0027 \approx 3{,}600$. And $60^2 = 3{,}600$.

The Moon is 60 Earth-radii away, and the gravitational acceleration is $60^2 = 3{,}600$ times weaker than at the surface. The force falls off as the square of the distance. This is the inverse-square law, and Newton had extracted it from two numbers: the Moon's orbital period and its distance from Earth.

He then wrote down the general law: every object attracts every other object with a force proportional to the product of their masses and inversely proportional to the square of the distance between them:

$$F = G \frac{M_1 M_2}{R^2}$$

The inverse-square part is what matters for the qualitative picture. Double the distance, and the force drops to one quarter. Triple the distance, and it drops to one ninth. The force weakens quickly but never reaches zero. Not at the Moon's distance, not at Pluto's, not across a galaxy.

What Newton then proved — and this is the thing that turned Kepler's empirical laws into theorems — is that if gravity follows the inverse-square law, and if objects obey his three laws of motion, then the only possible orbital shapes are conic sections: circles, ellipses, parabolas, and hyperbolas. Kepler didn't need to extract the ellipse from Brahe's data. Given Newton's one law of gravitation, the ellipse is the only possibility.

Let me be precise about what "unification" means here. It doesn't just mean that the same idea applies to many cases. It means that all those cases turn out to be the same case. Kepler's three separate observational laws — ellipses, equal areas, period-distance relationship — become three consequences of one equation. The mechanism that keeps planets in their orbits is the same mechanism that pulled the apple and accelerates the Moon. Same force, same law, same equation.

Let me show you the law in action with numbers. Earth's mass is $5.97 \times 10^{24}$ kg. Your mass is roughly 70 kg. You are standing on Earth's surface, $6.371 \times 10^6$ m from Earth's center:

$$F = (6.67 \times 10^{-11}) \frac{(5.97 \times 10^{24})(70)}{(6.371 \times 10^6)^2} \approx 686 \text{ N}$$

That is your weight. If Earth had twice its current mass but the same radius, you would weigh twice as much. If Earth had the same mass but twice its radius, you would weigh one quarter as much — because the denominator grows as $R^2$. This is why you would weigh about one sixth as much on the Moon: the Moon is less massive than Earth and smaller, and the ratio of mass to radius-squared works out to roughly one sixth.

Newton's framework also explains Kepler's second law in a way that reveals what's really happening underneath. As a planet orbits, a quantity called angular momentum is conserved — a combination of the planet's mass, speed, and distance from the Sun. When the planet is close to the Sun, it must move faster to keep that product constant. When it's far away, it slows down. The equal-areas law is, at bottom, a statement about conservation of angular momentum. The geometry Kepler discovered from data falls directly out of Newton's dynamics.

---

## The Vocabulary of Falling Around Things

Once you have Newton's law, you can calculate how things actually move in orbits. Three quantities are essential: circular orbital velocity, the relationship between a circular orbit and an elliptical one, and escape velocity.

**Circular orbital velocity.** An object in a circular orbit is continuously accelerating toward the center — this is the centripetal acceleration. Gravity provides it. Set the gravitational acceleration equal to the centripetal acceleration and solve for speed:

$$\frac{v^2}{r} = \frac{GM}{r^2} \implies v = \sqrt{\frac{GM}{r}}$$

For a satellite just above Earth's surface, plug in $r = 6.371 \times 10^6$ m and $M = 5.97 \times 10^{24}$ kg: you get $v \approx 7{,}900$ m/s. That is about 7.9 km/s — Sputnik's speed, roughly. A little slower and you fall. A little faster and your orbit rises.

Here is the counterintuitive thing this equation tells you: higher orbits are slower. The International Space Station, at 400 km altitude, orbits at 7.68 km/s and completes one orbit in 92 minutes. A geostationary satellite, at 36,000 km altitude, moves at only 3 km/s — but it takes exactly 24 hours to complete one orbit, so it appears to hover over the same point on Earth. You might think that maintaining a higher altitude requires moving faster. It doesn't. It requires moving slower, but moving slower in a larger circle whose geometry keeps you aloft.

<!-- → [CHART: x-axis: altitude above Earth's surface (km), logarithmic scale from 0 to 40,000 km; y-axis: orbital velocity (km/s); smooth curve descending from ~7.9 km/s at the surface to ~3.07 km/s at geostationary altitude; annotate three points: (1) surface/Sputnik height: 7.9 km/s; (2) ISS at 400 km: 7.68 km/s, 92-minute orbit; (3) geostationary at 35,786 km: 3.07 km/s, 24-hour orbit; student should see that the curve drops — conclusively settling the "higher orbit = slower speed" counterintuition before it can take root] -->

**Elliptical orbits.** Real orbits are ellipses. An object in an elliptical orbit has the same conserved quantities — angular momentum and total energy — as in a circular orbit, but its speed varies with position. At closest approach (perihelion), it moves fastest. At farthest point (aphelion), it moves slowest. Conservation of angular momentum gives the precise relationship:

$$r_p v_p = r_a v_a$$

The closer you are, the faster you must be moving, in exactly the ratio of the distances. This is Kepler's second law, expressed as an equation.

**Escape velocity.** Now suppose you want to leave a planet entirely — not orbit it, but escape. You need enough kinetic energy to overcome the gravitational potential energy holding you back. Set them equal:

$$\frac{1}{2}mv^2 = \frac{GMm}{R} \implies v_{\text{escape}} = \sqrt{\frac{2GM}{R}}$$

This is exactly $\sqrt{2}$ times the circular orbital speed at the same radius. For Earth, escape velocity is about 11.2 km/s. Notice that the mass of the escaping object cancels completely. A feather and a spacecraft need exactly the same escape velocity from Earth's surface. What matters is only the mass of the body you're escaping and your distance from its center.

The connection between orbital speed and escape speed is not a coincidence. A circular orbit has total mechanical energy equal to negative one half the gravitational potential energy. To escape — to bring total energy from negative to zero — you need to add exactly that much again. Doubling the kinetic energy means multiplying the speed by $\sqrt{2}$. The factor is embedded in the energy structure of gravity itself.

---

## Weighing the Invisible

Newton's version of Kepler's third law has an extra term that Kepler's didn't. When Newton worked through the two-body problem properly — both objects pulling on each other — he got:

$$a^3 = (M_1 + M_2) P^2$$

where the masses are measured in solar masses, the distance in AU, and the period in years. For the planets, the planet's mass is negligible compared to the Sun's, so the sum is essentially $M_\odot = 1$, and you recover Kepler's original law. But when the two masses are comparable — two stars orbiting each other, for instance — both terms matter.

The useful thing about this equation is that you can run it backward. If you observe an orbit — measure its period and its size — the equation tells you the mass. This is how astronomers weigh objects they cannot touch.

In 1846, this technique produced one of the great predictions in the history of science. Astronomers had noticed that Uranus was not following the orbit Newton's theory predicted. The deviations were small but consistent and systematic — not random errors, but a pattern. The hypothesis was an unseen planet pulling on Uranus and perturbing its path. John Couch Adams and Urbain Le Verrier independently used Newton's law to calculate where such a planet would have to be and how massive it would need to be to explain the observations. An astronomer in Berlin pointed a telescope at the predicted position and found Neptune within one degree of the prediction.

The planet had been weighed and located before it was seen.

The same technique is now used to find planets around other stars. A planet orbiting a star pulls the star gravitationally, causing the star to wobble slightly. The wobble is tiny — a few meters per second in the star's velocity — but measurable using Doppler shifts in the star's spectral lines. The period and amplitude of the wobble encode the planet's mass and orbital distance. We have catalogued thousands of exoplanets this way, most invisible even to the largest telescopes, known only through the gravitational signature they leave on their host stars.

Gravity, properly understood, is a measuring instrument. It converts orbital motion into mass.

---

## What Newton Couldn't Explain

Newton's theory is extraordinarily powerful. Given the positions and velocities of the planets today, you can integrate the equations forward or backward and predict where every planet was or will be with high precision. You can design a spacecraft trajectory that reaches Saturn in seven years using a gravity assist from Jupiter, arriving within seconds of schedule. You can predict eclipses centuries in advance.

But Newton himself admitted he could not explain why gravity works. He could say what it does — attract two masses with a force following the inverse-square law — but not what the mechanism was. How does Earth reach across 150 million kilometers of empty space and pull on the Sun? What carries the force?

He wrote, near the end of the *Principia*, the famous admission: *Hypotheses non fingo* — I feign no hypotheses. He was not going to pretend he understood the mechanism when he didn't. The equations worked. The mechanism was unknown.

The answer came with Einstein. Gravity is not a force transmitted across empty space. It is a curvature of spacetime caused by mass. A massive object bends the geometry of space and time around it, and other objects moving through this curved geometry follow paths that look, from the outside, like attraction. From their own frame of reference, they are moving in straight lines through a curved space. This is general relativity, and it gives slightly different predictions than Newton's theory in extreme conditions — near black holes, close to very massive stars, when objects approach the speed of light.

In the solar system, the corrections are small but measurable. The most famous is the precession of Mercury's perihelion — the ellipse itself slowly rotates over time, completing one extra revolution every three million years. Most of this precession was explained by the gravitational pull of the other planets. But 43 arcseconds per century couldn't be accounted for. Newton's theory was off by a small but precise amount that refused to go away regardless of how carefully the calculation was done. Einstein's theory predicted exactly 43 arcseconds per century. The discrepancy closed completely.

<!-- → [DIAGRAM: Mercury's orbital precession — the Sun at center; show five successive Mercury orbits as ellipses, each slightly rotated clockwise from the last, so the perihelion point traces a slow rosette or petal pattern around the Sun; annotate: "total precession: ~574 arcseconds/century", "explained by other planets: ~531 arcseconds/century", "unexplained by Newton: 43 arcseconds/century", "predicted by Einstein: exactly 43 arcseconds/century"; the visual makes the gap between Newton and observation concrete before the resolution is stated] -->

There is still no complete quantum theory of gravity. Quantum mechanics describes how particles interact through force carriers — photons for electromagnetism, gluons for the strong force. For gravity, the hypothetical carrier (the graviton) has never been detected, and the theory describing it hasn't been fully worked out. At the scales of orbits and planetary motion, this doesn't matter — Newton's equations are accurate to many decimal places. But at the center of a black hole, or in the first fraction of a second after the Big Bang, the existing theories break down.

The orbit of Sputnik — a grapefruit-sized sphere moving at 8 kilometers per second around a spherical rock in space — is, at bottom, still not completely understood.

That seems like the right place to stop.

---

## LLM Exercises

**Exercise 1.** Kepler's third law states that $T^2 = a^3$ for objects orbiting the Sun, where $T$ is the orbital period in years and $a$ is the semi-major axis in astronomical units. Prompt an LLM: "Derive Kepler's third law from Newton's law of gravitation and the centripetal force requirement for a circular orbit. Show that the period depends on the central mass — why does this version reduce to $T^2 = a^3$ specifically when the central mass is the Sun?" Evaluate whether the response correctly arrives at $T^2 = (4\pi^2/GM_{\odot}) a^3$ and explains why the units chosen (years and AU) absorb the constant.

**Exercise 2.** Newton famously argued that the Moon is "falling toward Earth" continuously — but never gets closer. Prompt an LLM: "Reconcile this seeming paradox. If the Moon is constantly accelerating toward Earth (which is true — gravity pulls it down at about 0.0027 m/s²), why doesn't it crash? Walk through how the tangential velocity exactly matches the rate of falling such that the Moon traces out an orbit." Evaluate whether the response correctly explains that the Moon's horizontal velocity carries it sideways at the same rate gravity pulls it down, producing a stable closed path.

**Exercise 3.** A geostationary satellite orbits Earth at an altitude of approximately 35,786 km above the surface (radius from Earth's center ≈ 42,164 km). Prompt an LLM to verify this using $T = 2\pi\sqrt{r^3/GM_E}$ where $T = 86,164$ s (sidereal day, not 24 hours), $G = 6.67 \times 10^{-11}$ N m² kg⁻², and $M_E = 5.97 \times 10^{24}$ kg. Compare the LLM's answer to the published value. If it differs, identify whether the LLM used a sidereal day or a solar day. Why does this distinction matter?

**Exercise 4.** Cavendish in 1798 measured the gravitational constant $G$ by directly observing the attraction between two lead spheres. Prompt an LLM: "Why was Cavendish's experiment considered to 'weigh the Earth' even though it directly measured only the force between two small spheres?" The key is that knowing $G$ allows calculating Earth's mass from the surface gravity equation $g = GM_E/R_E^2$. Evaluate whether the LLM understands that Cavendish gave us the constant linking gravity to mass, allowing all gravitational masses to be inferred subsequently.

**Exercise 5 (challenge).** Tidal forces arise because gravity weakens with distance — the side of an object closer to the source experiences stronger gravity than the far side. Prompt an LLM: "Derive the tidal stretching force on a small object of length $L$ at distance $r$ from a mass $M$. Show that this force scales as $M L / r^3$, not $M/r^2$ as gravity itself does." Then ask: "Use this to estimate the Roche limit — the distance at which a moon would be torn apart by tidal forces. For Earth orbiting near a 10-solar-mass black hole, at what distance would a person be ripped apart by tidal stretching ('spaghettification')?" Evaluate whether the LLM correctly identifies the inverse-cube scaling and uses it to estimate the relevant distance scale.

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Émilie du Châtelet** translated Newton's *Principia* into French in the 1740s — and added her own commentary that introduced the concept of *kinetic energy* (mv²) to Continental physics, before Newton's framework was widely accepted on the mainland.

**Run this:**

```
Who was Émilie du Châtelet, and how does her translation and commentary on Newton's Principia connect to the orbital mechanics and gravitation we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.
```

→ Search **"Émilie du Châtelet"** on Wikipedia. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to walk through du Châtelet's mv² argument and contrast it with Newton's momentum-based account — what's at stake in the difference?
- Add a constraint: "Answer as du Châtelet's 1746 letter to a fellow natural philosopher, explaining why Newton needed her edits."

What changes? What gets better? What gets worse?
