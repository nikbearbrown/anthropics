# Chapter 8 — Uniform Circular Motion and Gravitation

*Sputnik was falling the entire time. It just kept missing.*

---

October 4, 1957. A polished aluminum sphere — roughly the size of a beach ball, weighing 83.6 kg, trailing four whip antennas — lifts off from a remote site in Kazakhstan atop a Soviet R-7 rocket. Ninety-eight minutes later it is in orbit, circling the Earth at roughly 8 kilometers per second, transmitting a simple radio beep on two short-wave frequencies. Its name is *Sputnik 1*. It is the first artificial object to orbit a planet.

Three weeks later it is still up there. People on every continent go outside in the right twilight hours, look at the right part of the sky, and see a small bright dot moving steadily overhead. It does not look like much. Thoughtful people ask the obvious question: why isn't it falling?

The answer is that it *is* falling. At every instant, Earth's gravity pulls *Sputnik 1* toward the planet — exactly as it pulls any other object. But the satellite is also moving sideways, fast enough that as it falls, the Earth curves away beneath it at the same rate it falls. It perpetually falls and perpetually misses. Newton imagined this exact scenario in 1687: a cannonball fired horizontally fast enough that the Earth's surface drops away beneath it as fast as it falls. He predicted, correctly, that such a cannonball would orbit. Three centuries later, the Soviets built the cannon.

This chapter is the physics behind that prediction in two pieces. First: an object moving in a circle at constant speed is accelerating — toward the center, by a specific amount that depends on speed and radius — even though its speed is not changing. Second: gravity is a force between any two masses, falling off with the square of the distance between them. Put those two ideas together and you get orbital mechanics, Kepler's three laws, the architecture of the GPS constellation, and the reason *Sputnik 1* stayed up until the drag of the upper atmosphere finally brought it down in January 1958.

<!-- → IMAGE: photograph of Sputnik 1 — the polished aluminum sphere with four trailing antennas — ideally against a dark background; caption should give the actual dimensions (58 cm diameter, 83.6 kg) and the orbital parameters (250 km perigee, 940 km apogee, 96-minute period) so the student has a concrete object in mind when the calculations later arrive -->

---

## The Acceleration That Changes Only Direction

Here is the thing that trips everyone up at first. Acceleration is a vector. It measures how fast the velocity vector changes — and the velocity vector has both a magnitude (speed) and a direction. An object can accelerate without changing its speed at all, as long as its direction is changing. This is not a technicality. It is the heart of circular motion.

Stand at the edge of a playground merry-go-round while a friend spins it at constant rate. Your feet trace a circle; your head traces a slightly smaller one; the rim of the platform traces the largest. Every part of you moves at a different linear speed, but every part sweeps the same angle per second. The whole platform is a rigid body, and that shared angular rate — call it $\omega$ in radians per second — is the natural way to describe its rotation. The linear speed of any point is then

$$v = r\omega,$$

where $r$ is its distance from the axis. Points farther from the center move faster; points at the center do not move at all.

Now here is the geometric fact. A point on the rim is moving — its velocity vector is tangent to the circle. One moment later, the point has moved to a new position on the circle, and its velocity vector is still tangent — but tangent in a new direction. The velocity has changed direction. Change in velocity divided by time is acceleration. For an object moving at speed $v$ around a circle of radius $r$, the rate at which the velocity vector rotates toward the center works out to

$$a_c = \frac{v^2}{r}.$$

This is the centripetal acceleration — "centripetal" from the Latin for *center-seeking*, because the acceleration always points directly inward, toward the center of the circle. You can also write it as $a_c = r\omega^2$ (substitute $v = r\omega$); both forms are exact and which is more convenient depends on what you are given.

The derivation is worth seeing once. As the object moves through a small angle $\Delta\theta$, its velocity vector — which has constant magnitude $v$ — also rotates through $\Delta\theta$. The change in the velocity vector has magnitude $v \cdot \Delta\theta$ (for small angles) and points toward the center. The time to sweep angle $\Delta\theta$ at angular velocity $\omega$ is $\Delta t = \Delta\theta / \omega$. Dividing the velocity change by the time: $a = v\Delta\theta / (\Delta\theta/\omega) = v\omega = v^2/r$. The geometry forces the result.

<!-- → DIAGRAM: two-panel geometric derivation of centripetal acceleration — left panel: a circle with a point moving from position A to B, velocity vectors v₁ (tangent at A) and v₂ (tangent at B) drawn, the angle Δθ between them labeled; right panel: a vector triangle showing v₁ and v₂ tip-to-tail, the difference vector Δv pointing toward the center of the circle, its magnitude labeled v·Δθ; caption should note that Δv always points inward regardless of where on the circle A and B are, making centripetal acceleration a purely geometric result -->

**A worked example.** A car drives around a curve of radius 500 m at 25 m/s. Its centripetal acceleration is

$$a_c = \frac{v^2}{r} = \frac{625}{500} = 1.25 \text{ m/s}^2.$$

In units of $g$: $1.25 / 9.80 \approx 0.13$. A noticeable sideways push, but not extreme — consistent with what you feel on a fast freeway entrance ramp. Race cars in tight turns reach 2–5 $g$. Fighter jets in combat maneuvers approach 9 $g$, near the limit of human tolerance.

The important scaling: centripetal acceleration grows with the *square* of speed at fixed radius. Doubling your speed quadruples the required centripetal acceleration. Slowing down is four times as effective as it feels.

---

## What Supplies the Centripetal Force

An acceleration requires a force. Newton's second law applied to circular motion gives

$$F_c = ma_c = \frac{mv^2}{r}.$$

This is not a new kind of force. *Centripetal* describes the role — an inward-pointing net force — not the origin. Whatever physical force happens to be pointing toward the center of the circle is acting as the centripetal force. The word labels the geometry; the physics tells you the actor.

For a car on a flat road rounding a curve: the centripetal force is static friction between tires and road. The road pushes the tires inward; the tires push the road outward (Newton's third law); and the inward friction on the tires is what bends the car's path. If the road is icy and friction is insufficient — if the maximum available friction is smaller than $mv^2/r$ — the car cannot bend its path tightly enough and slides outward. That is what skidding on a curve physically means: the required centripetal force exceeded what the surface could provide.

For a stone on a string twirled in a horizontal circle: the centripetal force is string tension. For a roller coaster at the top of a vertical loop: gravity and the normal force from the track combine. For the Moon orbiting Earth: gravity alone.

The recipe is always the same. Identify what physical force points toward the center. Set it equal to $mv^2/r$. Solve for whatever you need.

<!-- → TABLE: four-row table of centripetal-force scenarios — columns: Situation | Object in circular motion | Physical source of centripetal force | Points toward; rows: Car on flat curve (car, static friction from road, center of curve); Stone on string (stone, string tension, pivot point); Roller coaster top of loop (rider, gravity + normal force from track, center of loop); Moon orbiting Earth (Moon, gravity from Earth, Earth's center) — student should see that "centripetal force" is always a label applied to a real force, never a new force in its own right -->

**A worked example.** A 900 kg car takes a flat curve of radius 500 m at 25 m/s. What minimum coefficient of static friction is needed?

The centripetal force is friction: $F_c = \mu_s N = \mu_s mg$ on a flat road.

$$\mu_s mg = \frac{mv^2}{r}.$$

Mass cancels — the required friction coefficient is independent of how heavy the car is. Solving:

$$\mu_s = \frac{v^2}{rg} = \frac{625}{500 \times 9.80} \approx 0.13.$$

Dry concrete on rubber gives $\mu_s \approx 1.0$ — far above 0.13. Wet concrete might give $\mu_s \approx 0.7$ — still fine. Ice at $\mu_s \approx 0.1$ falls below the required value. The calculation tells you precisely where safety fails.

There is a common confusion worth naming. Inside a turning car, you feel pushed outward — toward the door, away from the center of the curve. It feels like a force. It is not. From an inertial frame outside the car, no outward force acts on you. Your body is trying to continue in a straight line (Newton's first law), while the car turns under you. The seat's friction pushes you inward into the curve; you feel that push as pressure from the outside. The apparent outward push — sometimes called centrifugal force — is the felt consequence of inertia in an accelerating frame, not a real force in its own right.

---

## Gravity as the Universal Centripetal Force

Now the second piece of physics. Newton's gravitational insight, stripped to its core: the same force that pulls an apple off a tree also holds the Moon in its orbit. Gravity is not a special surface phenomenon. It is a universal force between any two masses, operating across any distance.

Newton's law of universal gravitation states: between any two point masses $m_1$ and $m_2$ separated by distance $r$, there is an attractive force directed along the line between them with magnitude

$$F = G \frac{m_1 m_2}{r^2}.$$

The universal gravitational constant $G = 6.674 \times 10^{-11} \text{ N}\cdot\text{m}^2/\text{kg}^2$ is very small. The gravitational attraction between two 1 kg masses sitting 1 m apart is about $6.7 \times 10^{-11}$ N — far too small to measure without precision instruments. Gravity only matters when at least one of the masses is planetary or stellar.

<!-- → CHART: log-log plot of gravitational force F vs. distance r for Earth pulling a 1 kg mass — x-axis from Earth's surface (6.4×10⁶ m) to the Moon's distance (3.8×10⁸ m) to Earth-Sun distance (1.5×10¹¹ m); the inverse-square curve slopes down as a straight line on the log-log axes; key points labeled: "surface: F = 9.8 N", "Moon distance: F = 0.003 N", "Sun distance: F = 6×10⁻³ N"; a dashed line showing what 1/r would look like for comparison — student should see the inverse-square drop clearly and how quickly gravity weakens with distance -->

The law does two things immediately. First, it recovers the familiar $g$ near Earth's surface. For an object of mass $m$ at Earth's surface:

$$F = G\frac{M_\oplus m}{R_\oplus^2} = m \cdot \frac{G M_\oplus}{R_\oplus^2} = mg.$$

Plugging in $M_\oplus = 5.97 \times 10^{24}$ kg and $R_\oplus = 6.378 \times 10^6$ m gives $g \approx 9.80 \text{ m/s}^2$ — the value we have been using since Chapter 4. It is not an independent constant. It is a consequence of the Earth's mass and radius.

Second, it predicts orbits. For a satellite of mass $m$ in a circular orbit of radius $r$ around the Earth, gravity provides the centripetal force:

$$G \frac{M_\oplus m}{r^2} = \frac{mv^2}{r}.$$

The satellite's mass cancels. Solving for orbital speed:

$$v = \sqrt{\frac{G M_\oplus}{r}}.$$

Orbital speed depends only on the central mass and the orbital radius — not on what you put into orbit. A feather and a cannonball at the same altitude orbit at the same speed. This is the equivalence of gravitational and inertial mass made orbital: heavier objects feel more gravity, but they also take more force to accelerate, and the two effects cancel exactly.

From the orbital speed, the period follows:

$$T = \frac{2\pi r}{v} = 2\pi \sqrt{\frac{r^3}{GM_\oplus}},$$

or equivalently $T^2 = \frac{4\pi^2}{G M_\oplus} r^3$. This is Kepler's third law: the square of the orbital period is proportional to the cube of the orbital radius. Kepler derived it empirically from decades of planetary observations in the early 17th century. Newton derived it from the inverse-square law of gravity and his three laws of motion. The agreement was not accidental — it was the confirmation that the same physics governs apples and planets.

<!-- → CHART: log-log plot of T² vs. r³ for solar system bodies — points for Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, and optionally the ISS and Moon (orbiting Earth on a separate labeled line); the data fall on a straight line with slope 1 on the log-log axes, confirming T² ∝ r³; the two lines (Sun-centered and Earth-centered) have different y-intercepts corresponding to different values of GM; student should see that Kepler's third law is a straight line on this plot and that the slope is universal while the intercept depends on the central mass -->

**A worked example.** Given Earth's mass and the Moon's orbital radius of $3.84 \times 10^8$ m, what is the Moon's orbital period?

$$T^2 = \frac{4\pi^2}{G M_\oplus} r^3 = \frac{39.48}{(6.674 \times 10^{-11})(5.97 \times 10^{24})} \times (3.84 \times 10^8)^3.$$

$G M_\oplus \approx 3.986 \times 10^{14} \text{ m}^3/\text{s}^2$. $r^3 \approx 5.66 \times 10^{25} \text{ m}^3$.

$$T^2 \approx \frac{39.48 \times 5.66 \times 10^{25}}{3.986 \times 10^{14}} \approx 5.61 \times 10^{12} \text{ s}^2.$$

$$T \approx 2.37 \times 10^6 \text{ s} \approx 27.4 \text{ days.}$$

The actual sidereal month is 27.32 days. Agreement to better than 0.3%. One law, one input (Earth's mass), one measurement (the Moon's distance), reproduces the Moon's orbital period to three significant figures. That is what Newton meant when he said he had discovered a universal law.

---

## *Sputnik* as Synthesis

The opening question — why didn't *Sputnik 1* fall? — now has its complete answer.

*Sputnik 1* orbited at about 250 km altitude. The orbital radius from Earth's center is

$$r = R_\oplus + 250 \text{ km} = 6.378 \times 10^6 + 2.5 \times 10^5 \approx 6.628 \times 10^6 \text{ m.}$$

Orbital speed from the centripetal-gravitational balance:

$$v = \sqrt{\frac{G M_\oplus}{r}} = \sqrt{\frac{3.986 \times 10^{14}}{6.628 \times 10^6}} \approx 7{,}754 \text{ m/s.}$$

About 7.8 km/s — consistent with the reported value.

Orbital period:

$$T = \frac{2\pi r}{v} = \frac{2\pi \times 6.628 \times 10^6}{7{,}754} \approx 5{,}370 \text{ s} \approx 89.5 \text{ min.}$$

The published figure is about 96 minutes. The discrepancy is because *Sputnik 1*'s orbit was not circular — it was elliptical, with a perigee near 250 km and an apogee near 940 km. Our calculation used the perigee radius throughout, which overestimates the average speed and underestimates the period. The elliptical correction would close most of the gap.

What makes the calculation satisfying is not the numerical precision. It is the economy. Three centuries of physics condensed into two equations — centripetal acceleration and Newton's gravitational law — reduce a Cold War engineering achievement to a forty-line calculation. The same two equations give you the GPS constellation at 20,200 km altitude, the geosynchronous satellites at 35,786 km that carry television broadcasts, the orbital parameters of every spacecraft humans have launched, and the periods of every planet in the solar system.

The scale is worth feeling. The same centripetal-force framework describes a child on a merry-go-round ($r \sim 1$ m, $v \sim 1$ m/s), a car on a freeway curve ($r \sim 500$ m, $v \sim 25$ m/s), *Sputnik 1* in low Earth orbit ($r \sim 6.6 \times 10^6$ m, $v \sim 7{,}754$ m/s), and Earth orbiting the Sun ($r \sim 1.5 \times 10^{11}$ m, $v \sim 30{,}000$ m/s). The physics is invariant across eleven orders of magnitude in orbital radius and four orders of magnitude in speed. Same equation, only different numbers.

<!-- → INFOGRAPHIC: vertical logarithmic scale of orbital/circular radii from 1 m to 10¹¹ m — four labeled entries with icons: "merry-go-round rim (~1 m, a_c ~1 m/s²)", "freeway curve (~500 m, a_c ~1.25 m/s²)", "Sputnik 1 orbit (~6.6×10⁶ m, a_c ~9.1 m/s²)", "Earth orbit (~1.5×10¹¹ m, a_c ~0.006 m/s²)"; the equation F_c = mv²/r floats to the side spanning the entire scale; student should feel the eleven-order-of-magnitude span that a single equation covers -->

---

## What Newton's Law Does Not Explain

The law $F = Gm_1 m_2 / r^2$ is spectacularly predictive. It is not explanatory at any fundamental level. It tells you how strong gravity is between two masses. It does not tell you *why* mass attracts mass, or *how* the force is transmitted across empty space — what Newton called "action at a distance" and found philosophically troubling himself. His law is a precise mathematical description of a mystery.

There is also a subtler puzzle embedded in the formula. The $m$ in Newton's second law ($F = ma$) is the inertial mass — a measure of how much a body resists acceleration. The $m$ in Newton's gravity law ($F = Gm_1 m_2/r^2$) is the gravitational mass — a measure of how strongly a body participates in gravity. These are conceptually different things. You could imagine a universe where they are not equal: a body with large gravitational mass but small inertial mass would be pulled hard by gravity but easy to accelerate — it would fall faster than other objects. Experiment shows, to a precision now exceeding one part in $10^{13}$, that the two kinds of mass are identical. All objects fall at the same rate in the same gravitational field. Newton noted the equality and had no explanation for it.

Einstein, in general relativity, elevated the equality to a foundational principle — the equivalence principle — and rebuilt gravity from there, not as a force at all but as the curvature of spacetime. Newton's law emerges as an approximation, exact in the regime of weak fields and slow motion that covers essentially all human-scale and solar-system-scale physics. The approximation is so good that for everything from GPS to interplanetary navigation, relativistic corrections to Newton's gravity are small — present, necessary for precision, but small.

For *Sputnik 1* and for almost everything in this chapter, Newton's law is not merely good enough. It is exact.

---

## What Would Change My Mind

Newton's $1/r^2$ law has been tested to extraordinary precision across solar system scales. The argument would need revision if anomalies at galactic scales — the "dark matter" problem, where galaxy rotation curves do not match Newton's prediction for visible matter — required modifying the law itself rather than invoking unseen mass. Currently the evidence favors unseen mass over modifying gravity, but the question is not fully settled. At solar system scales and below, the law stands.

## Still Puzzling

Why does $F = mv^2/r$ describe circular motion, and why does $F = Gm_1 m_2/r^2$ describe gravity, and why does setting them equal work so cleanly? The answer is that they describe the same physical situation from different angles — one is a kinematic requirement, the other is the force law that provides it. But the deeper puzzle is the inverse-square form. Why $1/r^2$ and not $1/r^{2.001}$ or $1/r^3$? Newton knew that only $1/r^2$ produces closed elliptical orbits (his own proof), and that Kepler's third law implies $1/r^2$. But *why* the universe should choose this particular power of distance is a question general relativity reframes (it emerges naturally from the geometry of spacetime in three spatial dimensions) without fully dissolving. The inverse-square law is what three spatial dimensions of spacetime produce. Why we have three spatial dimensions is a question physics cannot yet answer.

---

## Exercises

### Warm-up

**1.** A bicycle wheel of radius 0.35 m rotates at 8 revolutions per second. (a) What is its angular velocity in rad/s? (b) What is the linear speed of a point on the rim? (c) What is the centripetal acceleration of a point on the rim, in m/s² and in $g$'s?

*Tests: $v = r\omega$, $a_c = v^2/r$, unit conversion between revolutions and radians.*

**2.** A 0.50 kg stone is tied to a 1.2 m string and whirled in a horizontal circle at 6.0 m/s. (a) What is the centripetal acceleration? (b) What is the tension in the string? (c) If the string breaks at 90 N of tension, what is the maximum speed the stone can reach before the string snaps?

*Tests: $F_c = mv^2/r$; identifying string tension as the centripetal force; solving for a maximum.*

**3.** A car rounds a flat curve of radius 80 m. The coefficient of static friction between tires and road is 0.70. What is the maximum speed at which the car can take the curve without sliding?

*Tests: friction as centripetal force; mass cancels; solving for $v$.*

**4.** Compute the gravitational force between Earth ($M_\oplus = 5.97 \times 10^{24}$ kg) and the Moon ($M_\text{Moon} = 7.35 \times 10^{22}$ kg) at a center-to-center distance of $3.84 \times 10^8$ m. Then compute the Moon's centripetal acceleration from this force.

*Tests: $F = Gm_1m_2/r^2$; connecting gravitational force to centripetal acceleration.*

---

### Application

**5.** A 1,000 kg car drives over a hill whose crest has a radius of curvature of 60 m. (a) At what speed would the car just barely leave the road at the top? (b) What is the normal force at the top if the car is traveling at 15 m/s? (c) What happens to the normal force as speed increases, and why?

*Tests: gravity and normal force combining as centripetal force at top of a hill; threshold condition for losing contact.*

**6.** Earth's surface gravitational acceleration can be derived from $g = GM_\oplus / R_\oplus^2$. Using $M_\oplus = 5.97 \times 10^{24}$ kg and $R_\oplus = 6.378 \times 10^6$ m, compute $g$ and compare to 9.80 m/s². Then compute the surface gravity on Mars ($M_\text{Mars} = 6.39 \times 10^{23}$ kg, $R_\text{Mars} = 3.39 \times 10^6$ m).

*Tests: deriving $g$ from universal gravitation; applying the same formula to another planet.*

**7.** The ISS orbits at $r \approx 6{,}778$ km from Earth's center. (a) Compute its orbital speed. (b) Compute its orbital period in minutes. (c) Astronauts aboard the ISS are in free fall — Earth's gravity at that altitude is not zero. Compute $g$ at that altitude and compare to surface $g$.

*Tests: orbital speed from $v = \sqrt{GM/r}$; period from $T = 2\pi r/v$; $g$ as a function of altitude.*

**8.** Mars orbits the Sun at 1.52 AU. Earth orbits at 1.00 AU with period 1.00 year. Use Kepler's third law to compute Mars's orbital period, without knowing the Sun's mass.

*Tests: $T^2 \propto r^3$ applied as a ratio; Kepler's third law without needing $G$ or $M$.*

---

### Synthesis

**9.** A fighter pilot pulls out of a dive, flying in a circular arc of radius 800 m at 300 m/s. (a) Compute the centripetal acceleration in $g$'s. (b) What is the apparent weight the pilot feels (the upward force from the seat), expressed as a multiple of her normal weight? (c) At what speed in this same arc would the centripetal acceleration reach 9 $g$ — near the limit of human tolerance?

*Tests: centripetal acceleration in $g$'s; apparent weight as normal force (gravity plus centripetal contribution); solving for limiting speed.*

**10.** Jupiter's moon Io orbits at $r = 4.22 \times 10^8$ m with period $T = 1.77$ days. Use Kepler's third law to compute the mass of Jupiter. Then use your result to find the orbital speed of Io.

*Tests: inverting Kepler's third law to find the central mass; computing orbital speed from $v = \sqrt{GM/r}$; using one satellite's data to characterize the whole system.*

---

### Challenge

**11.** Compute the orbital radius required for a satellite to have a period of exactly 24 hours (geosynchronous orbit) around Earth. Convert to altitude above Earth's surface. The published altitude is 35,786 km — compare your result. Then compute the orbital speed of a geostationary satellite and explain why, from the ground, it appears stationary.

*Tests: inverting Kepler's third law for $r$ given $T$; connecting the calculation to a real and consequential technology.*

---

## LLM Exercise — Chapter 8: Circular Motion in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A circular-motion or gravitational analysis of one element of your anchor phenomenon.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics
with LLMs. My anchor phenomenon is [paste 1-sentence description].

For Chapter 8, I want to apply uniform circular motion
(centripetal acceleration, a_c = v²/r) and/or Newton's gravitation
to my phenomenon. Please:

1. Identify ONE circular or rotational element in my phenomenon.
   Examples:
   - Bike commute: cornering on the bike — what's the centripetal
     acceleration on a typical curve, and what minimum friction
     does it require?
   - Coffee maker: a centrifugal pump or spinning grinder — what
     centripetal force on a coffee particle?
   - Basketball: spin on the ball during the shot — what's the
     centripetal acceleration of a point on the surface?
   - Marathon: running on a curved track section — what centripetal
     force on the runner?
   - Espresso: the orbit of a coffee particle in a vortex flow
     during extraction. Or the rotation of a milk frother.

2. Compute the relevant quantities (v or ω, r, a_c, F_c). Identify
   what physical force provides F_c.

3. Express a_c in units of g as a sanity check.

4. Identify any gravitational effects in your phenomenon (the most
   common: weight as the dominant downward force, but also
   tidal effects or orbital motion if your phenomenon involves
   space).

5. One Fermi-style sanity check.

6. Identify which assumption (uniform circular motion, neglected
   gravity, neglected drag) is most likely to fail first.

7. One sentence on how this connects to Chapter 9 (work and
   energy) — circular motion at constant speed does no net work;
   why?

Save the output as logbook/chapter-08-circular-and-gravitation.md.
```

### What this produces

A Logbook entry: a circular-motion analysis applied to your phenomenon, often surprising in magnitude — small radii at moderate speeds give large centripetal accelerations.

### How to adapt this prompt

- *For phenomena with no obvious circular component* (a straight-line marathon, a vertical pour): bring in Earth's rotation or the Earth-Sun gravitational force as the gravitational element.
- *For ChatGPT or Gemini:* identical with interface substitutions.
- *For Claude Code:* if you have angular-velocity or RPM data, paste it; ask for centripetal force and required friction.

### Connection to previous chapters

Builds directly on Chapter 6 (force, $F = ma$) and Chapter 7 (friction often provides centripetal force). Newton's law of gravitation is a specific application of the force framework from Chapter 6.

### Preview of next chapter

Chapter 9 introduces work and energy as alternative bookkeeping for mechanical systems. Circular motion at constant speed does no net work — the centripetal force is always perpendicular to the velocity, so the force-times-displacement dot product is zero. Gravity, by contrast, does substantial work when objects move radially toward or away from the central mass.

---

## AI Wayback Machine

**Johannes Kepler** worked out the three laws of planetary motion between 1609 and 1619 — elliptical orbits, equal areas swept in equal times, and the period-radius relation. He did it from Tycho Brahe's painstaking observational records, roughly forty years before Newton supplied the gravitational explanation.

**Run this:**

```
Who was Johannes Kepler, and how do his laws of planetary motion
connect to uniform circular motion and gravitation covered in this
chapter? Keep it to three paragraphs. End with the single most
surprising thing about his career or ideas.
```

→ Search **"Johannes Kepler"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how Newton's universal gravitation actually derives Kepler's three laws.
- Ask it about Kepler's day job casting horoscopes — and how he reconciled that with empirical astronomy.

What changes? What gets better? What gets worse?

---

*Tags: circular-motion; gravitation; Keplers-laws; centripetal-acceleration; orbits; uniform-circular-motion*
