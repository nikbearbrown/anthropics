# Chapter 3 — Orbits and Gravity
*What Keeps the Cosmos from Falling Into Itself.*

A single law of gravity — inverse-square, proportional to mass — unifies Kepler's three laws of planetary motion and Newton's three laws of motion. Once you understand that an orbit is just a controlled fall, you hold the mechanism that keeps the cosmos from collapsing into chaos.

---

Here is a strange fact. On October 4, 1957, a metal sphere the size of a grapefruit was launched into the sky. It carried nothing inside except a radio transmitter that beeped. No passengers, no instruments, no purpose beyond existence. And yet, when it reached a certain altitude and a certain speed — roughly 8 kilometers per second — the rockets shut off, and the sphere simply *stayed there*.

It did not need the rockets anymore. It just coasted.

<!-- → [IMAGE: diagram of Sputnik's orbital trajectory showing the rockets shutting off at altitude, with a dotted arc illustrating the "falling around a curved Earth" geometry — label the 8 km/s velocity vector and the gravitational pull vector pointing toward Earth's center] -->

For the next 92 days, Sputnik fell continuously toward Earth and never once arrived. This is not a paradox. It is a geometric fact. The surface of Earth curves away from you at roughly the same rate that gravity pulls you down. If you move sideways fast enough, you fall and fall and the ground keeps slipping out from under you. You orbit.

Everything in this chapter follows from understanding that one idea. An orbit is not an object being held up. It is an object falling around a curved world. Gravity is not the obstacle to orbit; it is the engine of orbit. And the same force that pulls Sputnik toward Earth pulls the Moon toward Earth, pulls Earth toward the Sun, and pulled an apple toward the ground in Isaac Newton's garden in 1666.

Let's find out why.

---

## Kepler's Clue: The Planets Don't Move in Circles

When Johannes Kepler arrived in Prague in 1600 to work for the astronomer Tycho Brahe, he inherited the most precise observational record in history. For twenty years, Brahe had tracked the positions of planets with obsessive care. He had not invented the telescope — that was still a decade away — but with careful sighting instruments and relentless repetition, he had accumulated data that no one else could match.

Kepler's job was to find the pattern.

He tried circles first. Everyone tried circles. Aristotle had declared the heavens perfect, and circles were the perfect shape — no beginning, no end, the same in every direction. Centuries of tradition backed this up. But no matter how Kepler positioned a circle, no matter how he adjusted its size or shifted its center, Brahe's data refused to fit. Mars was the worst offender. The predicted positions and the observed positions disagreed by amounts that were too large to dismiss as measurement error.

Kepler was not the kind of person who dismissed data to save a theory. He tried another shape: the ellipse.

An ellipse is what you get when you cut a cone at an angle to its axis — elongated, like a squashed circle. It has two focal points instead of one center. And here is the defining property: for any point on the ellipse, the sum of the distances to the two focal points is constant. Always the same. At every point.

<!-- → [INFOGRAPHIC: side-by-side comparison of a circle (one center, constant radius) vs. an ellipse (two foci, constant sum of distances) — show a point P on the ellipse with lines drawn to both foci and label the sum F1+F2=constant; annotate where the Sun sits in a planetary orbit (one focus, not the center)] -->

When Kepler placed the Sun at one focus of the ellipse — not the center, one focus — Mars fit perfectly. Not approximately. *Perfectly*.

This was Kepler's first law: **each planet moves in an ellipse with the Sun at one focus.**

The other focus is empty. There is nothing there. This detail matters enormously, because it means the planet is sometimes closer to the Sun (at perihelion) and sometimes farther away (at aphelion). Mercury's distance from the Sun varies between 46 million and 70 million kilometers over the course of a single orbit. The variation is not small. At perihelion, Mercury absorbs nearly twice as much solar energy as at aphelion.

Kepler's second law describes what happens to the planet's speed as it moves around this ellipse: **as a planet orbits, the line from the planet to the Sun sweeps out equal areas in equal times.**

This sounds like a geometric abstraction. It isn't. It means the planet speeds up when it gets close to the Sun and slows down when it moves away. At perihelion, gravity is pulling harder — the planet accelerates, racing through the near part of its orbit. At aphelion, gravity is weaker — the planet slows, coasting through the far part. The rate at which area is swept out stays constant throughout.

<!-- → [DIAGRAM: elliptical orbit with the Sun at one focus; show two equal-area wedges — one narrow and long near perihelion (planet moves fast, large arc), one wide and short near aphelion (planet moves slow, small arc) — label perihelion, aphelion, and the equal areas A1=A2] -->

The third law connects the size of the orbit to the time it takes to complete: **the square of a planet's orbital period equals the cube of its semimajor axis** (the "average radius" of the ellipse, half its widest diameter):

$$P^2 = a^3$$

where $P$ is measured in Earth-years and $a$ in astronomical units (the Earth-Sun distance).

Check it. Earth: $P = 1$ year, $a = 1$ AU. $(1)^2 = (1)^3$. Trivially true. Jupiter: $P = 11.86$ years, $a = 5.2$ AU. $(11.86)^2 = 140.7$, $(5.2)^3 = 140.6$. The law holds. Pluto: $P = 248$ years, $a = 39.5$ AU. $(248)^2 = 61{,}504$, $(39.5)^3 = 61{,}630$. The law holds across the entire solar system.

<!-- → [CHART: log-log scatter plot of semimajor axis (AU) vs. orbital period (years) for all eight planets plus Pluto — student should see the points fall perfectly on a straight line with slope 3/2, confirming P²=a³; label each planet by name] -->

Here is what Kepler could not do: he could not explain *why*. He had discovered the geometry of planetary orbits from pure data analysis. He suspected that some force from the Sun was responsible — he even used the word "gravity" — but he had no mathematical framework to prove it. The mechanism was still missing.

---

## Newton's Unification: One Law, Everything

In 1665, plague closed Cambridge University, and Isaac Newton went home to Lincolnshire for 18 months. He was 23 years old. During those months, he invented calculus, developed his theory of colors, and began working out the mathematics of gravity.

The central question he was asking was: why doesn't the Moon fall to Earth?

His insight, which he later described through the story of an apple, was that the Moon *does* fall to Earth. Constantly. It just also moves sideways fast enough that it keeps missing. Imagine firing a cannonball horizontally from a very tall mountain. Fire it slowly, and it curves downward and hits the ground. Fire it faster, and it lands farther away. Fire it fast enough, and the ground curves away as fast as the ball drops. The ball orbits. It falls forever without hitting.

<!-- → [DIAGRAM: Newton's cannonball — a tall mountain on a curved Earth with four cannonball trajectories at increasing speeds: slow (hits nearby), medium (hits farther), fast (long arc), orbital speed (curves all the way around) — this is Newton's own thought experiment from the Principia] -->

This is not a metaphor. It is exactly what the Moon is doing. And it meant that the force pulling the apple down and the force keeping the Moon in orbit were the same force.

Newton's universal law of gravitation is this: **every object attracts every other object with a force proportional to the product of their masses and inversely proportional to the square of the distance between them.**

$$F = G \frac{M_1 M_2}{R^2}$$

The inverse-square part is the key. Double the distance and the force drops to one quarter. Triple the distance and it drops to one ninth. The force weakens quickly but never reaches zero — not at the distance of the Moon, not at the distance of Pluto, not across the galaxy.

Newton then proved something extraordinary: if gravity follows the inverse-square law, and if objects obey his three laws of motion, then the only possible orbital shapes are conic sections — circles, ellipses, parabolas, and hyperbolas. Kepler's ellipses don't need to be taken on faith or extracted from data. They fall out of the mathematics as a theorem.

Kepler's three laws became consequences of Newton's one law. That is what physicists mean by unification: not just that the same idea applies to many cases, but that all those cases turn out to be the same case.

Let me show you how to use this. Earth's mass is about $5.97 \times 10^{24}$ kg. You have a mass of about 70 kg. You are standing on Earth's surface, 6,371 km from Earth's center. The gravitational force between you and Earth is:

$$F = (6.67 \times 10^{-11}) \frac{(5.97 \times 10^{24})(70)}{(6.371 \times 10^6)^2} \approx 686 \text{ N}$$

That is your weight. It is the force gravity exerts on you toward Earth's center. If Earth had twice its current mass but the same radius, you would weigh twice as much. If Earth had the same mass but twice its radius, you would weigh one quarter as much — because the denominator in the formula grows as $R^2$.

This is why you would weigh about one sixth as much on the Moon. The Moon is less massive than Earth and has a smaller radius, but the mass-to-radius-squared ratio — what actually determines surface gravity — works out to roughly one sixth.

<!-- → [TABLE: surface gravity comparison across solar system bodies — columns: body, mass (kg), radius (km), surface gravity (m/s²), weight of a 70 kg person (N) — include Earth, Moon, Mars, Jupiter, the Sun, and a white dwarf for dramatic effect] -->

Newton's framework also explains Kepler's second law in a way that reveals what's really happening. The quantity that stays constant as a planet orbits is called angular momentum — a measure combining the planet's mass, speed, and distance from the Sun. In the absence of outside forces, angular momentum is conserved. This is not a coincidence. It is a consequence of Newton's laws. The equal-areas law is, at bottom, a statement about conservation of angular momentum.

---

## Orbital Mechanics: The Vocabulary of Falling Around Things

Once you have Newton's law, you can calculate how things move in orbits. The basic vocabulary has three pieces: circular orbital velocity, elliptical orbits and their energies, and escape velocity.

**Circular orbital velocity.** An object in a circular orbit is continuously accelerating toward the center of the circle (centripetal acceleration). Gravity provides this acceleration. Set them equal:

$$\frac{v^2}{r} = \frac{GM}{r^2}$$

Solve for the orbital speed $v$:

$$v = \sqrt{\frac{GM}{r}}$$

For a satellite just above Earth's surface: $r \approx 6.371 \times 10^6$ m, $M = 5.97 \times 10^{24}$ kg, $G = 6.67 \times 10^{-11}$. Plug in and you get $v \approx 7{,}900$ m/s, or about 7.9 km/s. That is the speed you need to orbit just above the ground. A little less, and you fall. A little more, and your orbit rises.

Notice what this equation says: orbital speed depends only on the mass of the central body and the orbital radius. A more massive central body requires higher orbital speed. A larger orbital radius requires lower orbital speed. This is not intuitive — you might think a higher orbit means you need to go faster to maintain altitude. The opposite is true. Higher orbits are slower. The International Space Station, orbiting at 400 km altitude, completes one orbit in about 92 minutes at 7.68 km/s. A satellite at geostationary orbit, some 36,000 km up, moves at only about 3 km/s — but it takes exactly 24 hours to complete one orbit, so it appears to hover over the same point on Earth.

<!-- → [CHART: altitude (km) vs. orbital velocity (km/s) for Earth satellites — a smooth curve from low Earth orbit (~7.9 km/s) through ISS (~7.68 km/s at 400 km) to geostationary (~3.07 km/s at 35,786 km); annotate each landmark orbit; student should see the inverse-square-root relationship clearly] -->

**Elliptical orbits.** Real orbits are elliptical. An elliptical orbit has the same conserved quantities as a circular orbit — angular momentum and total energy — but the speed varies. At perihelion, the satellite is closest and moving fastest. At aphelion, it is farthest and moving slowest. The relationship between speed at perihelion $v_p$ and at aphelion $v_a$ comes directly from conservation of angular momentum:

$$r_p v_p = r_a v_a$$

The closer you are, the faster you must be moving, in exactly the ratio of the distances. This is Kepler's second law stated as an equation.

**Escape velocity.** Now suppose you want to leave a planet entirely — not orbit it, but escape its gravity. You need enough kinetic energy to overcome the gravitational potential energy that is pulling you back. Set kinetic energy equal to gravitational potential energy and solve:

$$\frac{1}{2}mv^2 = \frac{GMm}{R}$$

$$v_{\text{escape}} = \sqrt{\frac{2GM}{R}}$$

This is exactly $\sqrt{2}$ times the circular orbital velocity at the same radius. For Earth, escape velocity is about 11.2 km/s. Notice that the escaping object's mass $m$ cancels out. A feather and a spacecraft have the same escape velocity from Earth. What matters is only the mass of the body you're escaping and your distance from its center.

If you launch at exactly escape velocity, you will coast outward forever, slowing continuously, approaching zero speed only at infinite distance. If you launch at any speed less than escape velocity, gravity wins — you eventually fall back. If you launch at any speed greater than escape velocity, you escape with leftover velocity that gravity can never fully drain away.

The connection between orbital velocity and escape velocity is not a coincidence. It reflects the structure of energy in gravity. A circular orbit has total mechanical energy equal to negative one half the magnitude of the gravitational potential energy. To escape — to raise the total energy to zero — you must add exactly that much again. This doubles the kinetic energy you need, which means multiplying the speed by $\sqrt{2}$.

<!-- → [INFOGRAPHIC: energy diagram showing three cases side by side — (1) below orbital velocity: object falls back, total energy negative and large; (2) orbital velocity: closed ellipse, total energy negative; (3) escape velocity: open parabolic path, total energy = 0 — label kinetic energy, potential energy, and total energy for each case] -->

---

## Weighing the Invisible: What Orbits Tell Us About Mass

Newton's version of Kepler's third law goes further than Kepler's original. When Newton accounted for the fact that both objects in a two-body system pull on each other, the law became:

$$a^3 = (M_1 + M_2) P^2$$

where $M_1$ and $M_2$ are the masses in units of the Sun's mass, $a$ in AU, and $P$ in years.

For the planets, one mass (the planet) is so much smaller than the other (the Sun) that the planet's contribution is negligible. This is why Kepler's original version worked fine. But when the two masses are comparable — two stars orbiting each other, for instance — you need both terms.

The useful direction to run this equation is backward: observe the orbit, read off the period and separation, and calculate the mass. In 1846, this technique revealed the existence of Neptune. Astronomers noticed that Uranus was not following the orbit that Newton's theory predicted. The deviations were small but consistent. The hypothesis: an unseen planet was pulling on Uranus and disturbing its path. John Couch Adams and Urbain Le Verrier independently calculated where such a planet would have to be and how massive it would need to be to explain the discrepancy. An astronomer in Berlin pointed a telescope at the predicted position and found Neptune within one degree of the prediction. The planet had been weighed and located before anyone had seen it.

<!-- → [DIAGRAM: the discovery of Neptune — show Uranus's observed orbit vs. the predicted Newtonian orbit, with the deviation exaggerated for clarity; then show the inferred position of Neptune and an arrow pointing to where the telescope was aimed; annotate the year 1846 and the names Adams and Le Verrier] -->

The same technique is now used to find planets around other stars. A planet orbiting a star pulls the star slightly, causing the star to wobble. The wobble is tiny — a few meters per second in the star's velocity — but measurable using the Doppler shift of the star's light. The period and amplitude of the wobble encode the planet's mass and orbital distance. We have now catalogued thousands of exoplanets this way, most of them invisible even to the largest telescopes, known only through the gravitational signature they leave on their host stars.

Gravity, properly understood, is a measuring instrument. It converts orbital motion into mass.

---

## What Still Isn't Explained

Newton's theory is extraordinarily powerful. Given the positions and velocities of the planets today, you can integrate Newton's equations forward or backward and tell where every planet was or will be to high precision. You can design a spacecraft trajectory that reaches Saturn in seven years using a gravity assist from Jupiter, arriving within seconds of the predicted time. You can predict eclipses centuries in advance.

But Newton himself admitted he could not explain *why* gravity works. He could say what it does — attract two masses with a force that follows the inverse-square law — but he could not say what the mechanism was. How does Earth reach across 150 million kilometers of empty space and pull on you? What is the carrier of this force?

The answer came with Einstein. Gravity is not a force transmitted through space. It is a curvature of spacetime caused by mass. A massive object bends the geometry of space and time around it. Other objects moving through this curved geometry follow paths that look like attraction — but from their own reference frame, they are simply moving in straight lines through a curved space. This is general relativity, and it gives slightly different predictions than Newton's theory in extreme conditions: near black holes, very close to massive stars, or when objects move near the speed of light. In the solar system, the corrections are small but measurable. The most famous is the precession of Mercury's orbit — a slow rotation of the ellipse itself that Newton's theory cannot fully account for and Einstein's theory predicts exactly.

<!-- → [DIAGRAM: Mercury's orbital precession — show the ellipse slowly rotating over successive orbits, with the perihelion point tracing a rosette pattern; annotate the measured precession rate (43 arcseconds per century) and label "Newton's prediction" vs. "observed" to show the gap Einstein closed] -->

We still do not have a complete quantum theory of gravity. This is one of the major unsolved problems in physics. Quantum mechanics describes how particles interact through force carriers — photons for electromagnetism, gluons for the strong force, W and Z bosons for the weak force. For gravity, the hypothetical force carrier (the graviton) has not been detected, and the theory that describes it has not been fully worked out. At the scales relevant to orbits and planetary motion, this does not matter. Newton's theory is accurate to many decimal places. But at the center of black holes, or in the first fraction of a second after the Big Bang, we are in territory where our current theories break down.

The orbit of Sputnik — a grapefruit-sized sphere moving at 8 kilometers per second around a spherical rock in space — is, at bottom, still not completely understood.

---

## Exercises

The following exercises are designed for use with a language model that can reason through calculations step by step.

**Kepler's third law, worked forward and backward.** Ask the model to calculate the orbital period of an asteroid located at 3.5 AU from the Sun. Then ask it to work the problem in reverse: if you observe a comet with a period of 75 years (like Halley's Comet), what is its average distance from the Sun? Have the model explain at each step what assumption it is making and what Kepler's third law actually says versus what Newton's more general version adds.

**Comparing orbital velocities.** Ask the model to calculate the orbital speed of a satellite at 400 km altitude above Earth (low Earth orbit, approximately where the ISS orbits) and at 36,000 km altitude (geostationary orbit). What is the ratio of the two speeds? Ask it to explain why a higher orbit is *slower*, not faster — and what would need to change (either the planet's mass or the orbital radius) to require a higher speed at a higher altitude.

**Escape from other worlds.** Ask the model to calculate the escape velocity from the surface of Mars (mass $6.39 \times 10^{23}$ kg, radius 3,390 km) and compare it to Earth's. What does this mean for the difficulty of launching a spacecraft from Mars versus Earth? Then extend the problem: how does this connect to why Mars has such a thin atmosphere compared to Earth?

**Discovering mass through orbital motion.** Europa, one of Jupiter's moons, orbits at a distance of 671,100 km with a period of about 3.55 days. Ask the model to use Newton's form of Kepler's third law to calculate Jupiter's mass. Have it compare the answer to Jupiter's known mass ($1.898 \times 10^{27}$ kg) and explain any discrepancy. What does this demonstrate about how astronomers measure the masses of planets and stars?

**The perturbation problem.** Ask the model to explain, in plain language, how astronomers inferred the existence of Neptune before it was observed. What data did they have? What assumption did they make? What would they need to know to narrow down *where* in the sky to look? Have it identify the limits of this method — what kinds of masses or distances would be harder to detect this way?

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
