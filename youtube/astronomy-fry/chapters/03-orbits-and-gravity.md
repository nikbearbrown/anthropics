# Chapter 3 — Orbits and Gravity

Here is a strange fact. On October 4, 1957, a metal sphere the size of a grapefruit was launched into the sky. It carried nothing inside except a radio transmitter that beeped. No passengers, no instruments, no purpose beyond existence. And yet, when it reached a certain altitude and a certain speed — roughly 8 kilometers per second — the rockets shut off, and the sphere simply *stayed there*.

It did not need the rockets anymore. It just coasted.

![Diagram of Sputnik's orbital trajectory showing the rockets](images/03-orbits-and-gravity-fig-01.png)
*Figure 3.1 — Diagram of Sputnik's orbital trajectory showing the rockets*

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

![Comparison of a circle (one center, constant radius)](images/03-orbits-and-gravity-fig-02.png)
*Figure 3.2 — Comparison of a circle (one center, constant radius)*

When Kepler placed the Sun at one focus of the ellipse — not the center, one focus — Mars fit perfectly. Not approximately. *Perfectly*.

This was Kepler's first law: **each planet moves in an ellipse with the Sun at one focus.**

The other focus is empty. There is nothing there. This detail matters enormously, because it means the planet is sometimes closer to the Sun (at perihelion) and sometimes farther away (at aphelion). Mercury's distance from the Sun varies between 46 million and 70 million kilometers over the course of a single orbit. The variation is not small. At perihelion, Mercury absorbs nearly twice as much solar energy as at aphelion.

Kepler's second law describes what happens to the planet's speed as it moves around this ellipse: **as a planet orbits, the line from the planet to the Sun sweeps out equal areas in equal times.**

This sounds like a geometric abstraction. It isn't. It means the planet speeds up when it gets close to the Sun and slows down when it moves away. At perihelion, gravity is pulling harder — the planet accelerates, racing through the near part of its orbit. At aphelion, gravity is weaker — the planet slows, coasting through the far part. The rate at which area is swept out stays constant throughout.

![Elliptical orbit with the Sun at one focus](images/03-orbits-and-gravity-fig-03.png)
*Figure 3.3 — Elliptical orbit with the Sun at one focus*

The third law connects the size of the orbit to the time it takes to complete: **the square of a planet's orbital period equals the cube of its semimajor axis** (the "average radius" of the ellipse, half its widest diameter):

$$P^2 = a^3$$

where $P$ is measured in Earth-years and $a$ in astronomical units (the Earth-Sun distance).

Check it. Earth: $P = 1$ year, $a = 1$ AU. $(1)^2 = (1)^3$. Trivially true. Jupiter: $P = 11.86$ years, $a = 5.2$ AU. $(11.86)^2 = 140.7$, $(5.2)^3 = 140.6$. The law holds. Pluto: $P = 248$ years, $a = 39.5$ AU. $(248)^2 = 61{,}504$, $(39.5)^3 = 61{,}630$. The law holds across the entire solar system.

![Log-log scatter plot of semimajor axis (AU) vs](images/03-orbits-and-gravity-fig-04.png)
*Figure 3.4 — Log-log scatter plot of semimajor axis (AU) vs*

Here is what Kepler could not do: he could not explain *why*. He had discovered the geometry of planetary orbits from pure data analysis. He suspected that some force from the Sun was responsible — he even used the word "gravity" — but he had no mathematical framework to prove it. The mechanism was still missing.

---

## Newton's Unification: One Law, Everything

In 1665, plague closed Cambridge University, and Isaac Newton went home to Lincolnshire for 18 months. He was 23 years old. During those months, he invented calculus, developed his theory of colors, and began working out the mathematics of gravity.

The central question he was asking was: why doesn't the Moon fall to Earth?

His insight, which he later described through the story of an apple, was that the Moon *does* fall to Earth. Constantly. It just also moves sideways fast enough that it keeps missing. Imagine firing a cannonball horizontally from a very tall mountain. Fire it slowly, and it curves downward and hits the ground. Fire it faster, and it lands farther away. Fire it fast enough, and the ground curves away as fast as the ball drops. The ball orbits. It falls forever without hitting.

![Newton's cannonball ](images/03-orbits-and-gravity-fig-05.png)
*Figure 3.5 — Newton's cannonball *

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

| Body | Mass (kg) | Radius (km) | Surface gravity (m/s²) | Relative to Earth |
| --- | --- | --- | --- | --- |
| Earth | 5.97 × 10²⁴ | 6,371 | 9.81 | 1.00 |
| Moon | 7.35 × 10²² | 1,737 | 1.62 | 0.17 |
| Mars | 6.39 × 10²³ | 3,390 | 3.71 | 0.38 |
| Jupiter (cloud tops) | 1.90 × 10²⁷ | 69,911 | 24.8 | 2.53 |
| Sun | 1.99 × 10³⁰ | 696,000 | 274 | 27.9 |

Newton's framework also explains Kepler's second law in a way that reveals what's really happening. The quantity that stays constant as a planet orbits is called angular momentum — a measure combining the planet's mass, speed, and distance from the Sun. In the absence of outside forces, angular momentum is conserved. This is not a coincidence. It is a consequence of Newton's laws. The equal-areas law is, at bottom, a statement about conservation of angular momentum.

Newton wrote in Latin, in England, for a country already half-persuaded he was right. The rest of Europe was not. Getting his framework across the Channel took, among others, Émilie du Châtelet, working through the 1740s in France. She translated the *Principia* into French — a translation begun around 1745, finished in the year she died, and published after her death in 1756; it is still the standard French edition. She did more than translate. In her own physics she championed an idea then fighting for acceptance on the Continent: that the "force" of a moving body scales not with its speed but with the *square* of its speed — what we now call kinetic energy, $mv^2$. The insight was not hers alone; Leibniz had argued for it, and the Dutch experimenter Willem 's Gravesande had measured it by dropping brass balls into soft clay and finding that doubling the speed quadrupled the depth of the dent. Du Châtelet gathered the argument, sharpened it, and carried it into the mainstream of European physics — the work of getting a correct idea taken seriously, which is its own kind of discovery.

---

## Orbital Mechanics: The Vocabulary of Falling Around Things

Once you have Newton's law, you can calculate how things move in orbits. The basic vocabulary has three pieces: circular orbital velocity, elliptical orbits and their energies, and escape velocity.

**Circular orbital velocity.** An object in a circular orbit is continuously accelerating toward the center of the circle (centripetal acceleration). Gravity provides this acceleration. Set them equal:

$$\frac{v^2}{r} = \frac{GM}{r^2}$$

Solve for the orbital speed $v$:

$$v = \sqrt{\frac{GM}{r}}$$

For a satellite just above Earth's surface: $r \approx 6.371 \times 10^6$ m, $M = 5.97 \times 10^{24}$ kg, $G = 6.67 \times 10^{-11}$. Plug in and you get $v \approx 7{,}900$ m/s, or about 7.9 km/s. That is the speed you need to orbit just above the ground. A little less, and you fall. A little more, and your orbit rises.

Notice what this equation says: orbital speed depends only on the mass of the central body and the orbital radius. A more massive central body requires higher orbital speed. A larger orbital radius requires lower orbital speed. This is not intuitive — you might think a higher orbit means you need to go faster to maintain altitude. The opposite is true. Higher orbits are slower. The International Space Station, orbiting at 400 km altitude, completes one orbit in about 92 minutes at 7.68 km/s. A satellite at geostationary orbit, some 36,000 km up, moves at only about 3 km/s — but it takes exactly 24 hours to complete one orbit, so it appears to hover over the same point on Earth.

![Altitude (km) vs](images/03-orbits-and-gravity-fig-06.png)
*Figure 3.6 — Altitude (km) vs*

**Elliptical orbits.** Real orbits are elliptical. An elliptical orbit has the same conserved quantities as a circular orbit — angular momentum and total energy — but the speed varies. At perihelion, the satellite is closest and moving fastest. At aphelion, it is farthest and moving slowest. The relationship between speed at perihelion $v_p$ and at aphelion $v_a$ comes directly from conservation of angular momentum:

$$r_p v_p = r_a v_a$$

The closer you are, the faster you must be moving, in exactly the ratio of the distances. This is Kepler's second law stated as an equation.

**Escape velocity.** Now suppose you want to leave a planet entirely — not orbit it, but escape its gravity. You need enough kinetic energy to overcome the gravitational potential energy that is pulling you back. Set kinetic energy equal to gravitational potential energy and solve:

$$\frac{1}{2}mv^2 = \frac{GMm}{R}$$

$$v_{\text{escape}} = \sqrt{\frac{2GM}{R}}$$

This is exactly $\sqrt{2}$ times the circular orbital velocity at the same radius. For Earth, escape velocity is about 11.2 km/s. Notice that the escaping object's mass $m$ cancels out. A feather and a spacecraft have the same escape velocity from Earth. What matters is only the mass of the body you're escaping and your distance from its center.

If you launch at exactly escape velocity, you will coast outward forever, slowing continuously, approaching zero speed only at infinite distance. If you launch at any speed less than escape velocity, gravity wins — you eventually fall back. If you launch at any speed greater than escape velocity, you escape with leftover velocity that gravity can never fully drain away.

The connection between orbital velocity and escape velocity is not a coincidence. It reflects the structure of energy in gravity. A circular orbit has total mechanical energy equal to negative one half the magnitude of the gravitational potential energy. To escape — to raise the total energy to zero — you must add exactly that much again. This doubles the kinetic energy you need, which means multiplying the speed by $\sqrt{2}$.

![Energy diagram showing three cases side by side](images/03-orbits-and-gravity-fig-07.png)
*Figure 3.7 — Energy diagram showing three cases side by side*

---

## Weighing the Invisible: What Orbits Tell Us About Mass

Newton's version of Kepler's third law goes further than Kepler's original. When Newton accounted for the fact that both objects in a two-body system pull on each other, the law became:

$$a^3 = (M_1 + M_2) P^2$$

where $M_1$ and $M_2$ are the masses in units of the Sun's mass, $a$ in AU, and $P$ in years.

For the planets, one mass (the planet) is so much smaller than the other (the Sun) that the planet's contribution is negligible. This is why Kepler's original version worked fine. But when the two masses are comparable — two stars orbiting each other, for instance — you need both terms.

The useful direction to run this equation is backward: observe the orbit, read off the period and separation, and calculate the mass. In 1846, this technique revealed the existence of Neptune. Astronomers noticed that Uranus was not following the orbit that Newton's theory predicted. The deviations were small but consistent. The hypothesis: an unseen planet was pulling on Uranus and disturbing its path. John Couch Adams and Urbain Le Verrier independently calculated where such a planet would have to be and how massive it would need to be to explain the discrepancy. An astronomer in Berlin pointed a telescope at the predicted position and found Neptune within one degree of the prediction. The planet had been weighed and located before anyone had seen it.

![The discovery of Neptune ](images/03-orbits-and-gravity-fig-08.png)
*Figure 3.8 — The discovery of Neptune *

The same technique is now used to find planets around other stars. A planet orbiting a star pulls the star slightly, causing the star to wobble. The wobble is tiny — a few meters per second in the star's velocity — but measurable using the Doppler shift of the star's light. The period and amplitude of the wobble encode the planet's mass and orbital distance. We have now catalogued thousands of exoplanets this way, most of them invisible even to the largest telescopes, known only through the gravitational signature they leave on their host stars.

Gravity, properly understood, is a measuring instrument. It converts orbital motion into mass.

---

## What Still Isn't Explained

Newton's theory is extraordinarily powerful. Given the positions and velocities of the planets today, you can integrate Newton's equations forward or backward and tell where every planet was or will be to high precision. You can design a spacecraft trajectory that reaches Saturn in seven years using a gravity assist from Jupiter, arriving within seconds of the predicted time. You can predict eclipses centuries in advance.

But Newton himself admitted he could not explain *why* gravity works. He could say what it does — attract two masses with a force that follows the inverse-square law — but he could not say what the mechanism was. How does Earth reach across 150 million kilometers of empty space and pull on you? What is the carrier of this force?

The answer came with Einstein. Gravity is not a force transmitted through space. It is a curvature of spacetime caused by mass. A massive object bends the geometry of space and time around it. Other objects moving through this curved geometry follow paths that look like attraction — but from their own reference frame, they are simply moving in straight lines through a curved space. This is general relativity, and it gives slightly different predictions than Newton's theory in extreme conditions: near black holes, very close to massive stars, or when objects move near the speed of light. In the solar system, the corrections are small but measurable. The most famous is the precession of Mercury's orbit — a slow rotation of the ellipse itself that Newton's theory cannot fully account for and Einstein's theory predicts exactly.

![Mercury's orbital precession ](images/03-orbits-and-gravity-fig-09.png)
*Figure 3.9 — Mercury's orbital precession *

We still do not have a complete quantum theory of gravity. This is one of the major unsolved problems in physics. Quantum mechanics describes how particles interact through force carriers — photons for electromagnetism, gluons for the strong force, W and Z bosons for the weak force. For gravity, the hypothetical force carrier (the graviton) has not been detected, and the theory that describes it has not been fully worked out. At the scales relevant to orbits and planetary motion, this does not matter. Newton's theory is accurate to many decimal places. But at the center of black holes, or in the first fraction of a second after the Big Bang, we are in territory where our current theories break down.

The orbit of Sputnik — a grapefruit-sized sphere moving at 8 kilometers per second around a spherical rock in space — is, at bottom, still not completely understood.

---

## Sources

- OpenStax, *Astronomy*, Chapter 3, "Orbits and Gravity."
- Newton's three laws and his law of universal gravitation, *Philosophiæ Naturalis Principia Mathematica* (1687); Kepler's first two laws, *Astronomia Nova* (1609), and the third law, *Harmonices Mundi* (1619). https://en.wikipedia.org/wiki/Kepler%27s_laws_of_planetary_motion
- The 1846 discovery of Neptune from Adams's and Le Verrier's independent predictions, found by Galle within about one degree of the predicted position.
- The radial-velocity and transit gravity-signatures have now confirmed more than 5,900 exoplanets (NASA Exoplanet Archive). https://exoplanetarchive.ipac.caltech.edu
- The dynamical predictions of general relativity have been confirmed directly by gravitational-wave detections, beginning with GW150914 in 2015 (announced February 2016). https://www.ligo.caltech.edu
- On Émilie du Châtelet's French translation of the *Principia* (begun ~1745, published 1756) and her championing of the $mv^2$ ("vis viva") concept developed earlier by Leibniz and 's Gravesande. https://en.wikipedia.org/wiki/%C3%89milie_du_Ch%C3%A2telet
