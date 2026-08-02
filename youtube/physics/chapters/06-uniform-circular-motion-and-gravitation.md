![Four scales of uniform circular motion with shared equation a_c = v²/r: merry-go-round (r=2 m, T=10 s), freeway curve (r=100 m, v=25 m/s), Sputnik orbit (r=6800 km, T=96 min), Earth around Sun (r=150 Gm, T=1 yr).](../images/06-uniform-circular-motion-and-gravitation-fig-06.png)
*Figure 6.6 — Circular Motion at Every Scale — Merry-Go-Round to Earth's Orbit*

# Chapter 6 — Uniform Circular Motion and Gravitation

*How falling forever becomes staying up.*

---

Here is a question that should bother you. On October 4, 1957, the Soviets put a polished aluminum sphere into orbit at an altitude of $250$ kilometers. Earth's gravity at that altitude is still about $93\%$ of its surface value — roughly $9.1 \text{ m/s}^2$ downward, relentlessly. So why didn't *Sputnik 1* fall?

The answer is that it did fall. It was falling the entire time. Gravity was pulling it toward Earth at every instant, accelerating it downward, bending its path inward. But *Sputnik 1* was also moving sideways — fast enough that as it fell, the Earth curved away beneath it at exactly the rate it fell. The satellite was perpetually dropping toward a surface that perpetually retreated. It was in free fall, continuously, for 57 days.

Newton imagined this in 1687. He pictured a cannon on a very tall mountain, firing horizontally. Fire it gently and it arcs to the ground. Fire it harder and it reaches further. Fire it hard enough — about $7.9 \text{ km/s}$ at Earth's surface — and the ground curves away as fast as the cannonball falls, and it never lands. Newton wrote this down as a thought experiment. Three centuries later, the Soviets did it.

<!-- → [FIGURE: Newton's mountain cannon thought experiment. Curved Earth surface, tall mountain on left. Four trajectories shown: gentle arc landing nearby, longer arc landing further, very long arc landing at the horizon, and a closed orbit that circles the whole Earth. Each labeled with increasing muzzle speed. Caption: As muzzle speed increases, the landing point moves further around the curve of Earth. At about 7.9 km/s, the Earth curves away as fast as the cannonball falls — it orbits continuously.] -->

This chapter is the physics of that prediction. It has two parts that are not obviously related at first and then, suddenly, are completely inseparable.

The first part: an object moving in a circle at constant speed is accelerating. Not because its speed is changing — it isn't — but because its *direction* is. Acceleration is a vector; direction is part of velocity; constantly changing direction at constant speed means constantly changing velocity, which means nonzero acceleration. The acceleration points toward the center of the circle, and its magnitude is $v^2/r$.

The second part: gravity is a force between any two masses, falling off as the inverse square of distance. Newton showed that an inverse-square force, combined with his three laws, produces orbits that are conic sections — ellipses, hyperbolas, parabolas — and that orbital periods scale as the $3/2$ power of orbital radius. These were the patterns Kepler had painstakingly extracted from Tycho Brahe's observations decades earlier. Newton derived them from first principles in a few pages.

Put the two parts together: gravity supplies the centripetal force that bends a satellite's path into a closed curve. That's what an orbit is.

---

## The first part: circular motion is accelerated motion

Let's be careful about what "acceleration" means. From Chapter 2, acceleration is the rate of change of velocity. Velocity is a vector — it has both magnitude (speed) and direction. A change in either constitutes acceleration. Most problems in Chapter 2 involved straight-line motion where only the speed changed. This chapter is the first time changing direction is the whole story.

![Left: circular trajectory with velocity vectors v₁ and v₂ at two nearby points, both tangent and equal in magnitude. Right: vector triangle showing v₂ - v₁ = Δv points toward the center; in the limit Δt→0, a = v²/r toward center.](../images/06-uniform-circular-motion-and-gravitation-fig-02.png)
*Figure 6.2 — Centripetal Acceleration — Δv Points Toward the Center*

Picture a point on the rim of a spinning wheel. Its speed is constant. But every instant, it is moving in a different direction — the velocity vector is rotating. A continuously rotating velocity vector is continuously changing. The rate of that change is the centripetal acceleration, and it points toward the center of the wheel.

The geometry shows us how big it is. As the object moves through a small arc of angle $\Delta\theta$, the velocity vector also rotates by $\Delta\theta$ (the triangles are similar). The change in velocity has magnitude $v\,\Delta\theta$ for small angles. Divide by the time elapsed, $\Delta t = \Delta\theta / \omega$ (where $\omega = v/r$ is the angular speed), and you get:

$$a_c = \frac{v \cdot \Delta\theta}{\Delta t} = v\omega = \frac{v^2}{r}.$$

Two equivalent forms, because $v = r\omega$:

$$a_c = \frac{v^2}{r} = r\omega^2.$$

Use whichever fits the numbers you're given.

The direction of this acceleration is always toward the center of the circle. Not tangent to it, not outward from it — *inward*, toward the center, every instant. The Latin word is centripetal: center-seeking.

<!-- → [FIGURE: Circle with object at one point. Velocity vector shown tangent to circle. Small arc Δθ later, new velocity vector shown. ΔV vector drawn pointing toward center. Caption: As the object moves through angle Δθ, the velocity vector rotates by the same angle. The change in velocity Δv points toward the center — that is the centripetal acceleration.] -->

Now: a real acceleration requires a real force. Newton's second law doesn't care what's causing the acceleration or why it points inward; it says $\mathbf{F}_{\text{net}} = m\mathbf{a}$, so there must be a net inward force of magnitude

$$F_c = \frac{mv^2}{r}.$$

The word "centripetal" describes the *role* of this force — pointing inward, bending the path — not its *source*. You have to identify the source separately for each situation.

![Top-down view of car rounding a curve of radius r. Friction force points inward (toward center of curve) and equals mv²/r. Max safe speed: v_max = √(μ_s g r). For r = 100 m and μ_s = 0.7: v_max = 26 m/s.](../images/06-uniform-circular-motion-and-gravitation-fig-03.png)
*Figure 6.3 — Car on Unbanked Curve — Friction Supplies the Centripetal Force*

For a car rounding a flat curve, the centripetal force is static friction between the tires and the road. For a ball on a string, it's the string tension. For a roller coaster at the top of a loop, it could be gravity, or a combination of gravity and the track's normal force, depending on speed. For *Sputnik 1*, it's gravity. Same algebraic structure in every case; different physical actor.

<!-- → [TABLE: Centripetal force sources. Columns: situation, what provides F_c, formula for F_c. Rows: car on flat curve (static friction, μmg), car on banked curve (horizontal component of N, N sinθ), ball on string (tension, T), satellite in orbit (gravity, GMm/r²), roller coaster at top of loop (gravity + normal force, mg − N). Caption: "Centripetal" names the role, not the physical source. Every row has the same F_c = mv²/r on the right — only the left side changes.] -->

Let's work a flat-curve case to see this concretely. A $900 \text{ kg}$ car rounds a flat curve of radius $500 \text{ m}$ at $25 \text{ m/s}$. What minimum coefficient of static friction keeps the car on the road?

On a flat road, the normal force equals the weight: $N = mg$. Maximum static friction is $\mu_s mg$. That friction is also the only horizontal force, so it's the entire centripetal force:

$$\mu_s mg = \frac{mv^2}{r}.$$

The mass cancels — always does, for the flat-curve case. Solve:

$$\mu_s = \frac{v^2}{rg} = \frac{(25)^2}{(500)(9.80)} = \frac{625}{4900} \approx 0.13.$$

A coefficient of $0.13$ is required. Dry asphalt gives $\mu_s \approx 0.7$: no problem. Ice gives $\mu_s \approx 0.1$: below the threshold. That's what skidding off a wet or icy corner physically means — the required centripetal force exceeded what friction could provide, and the road stopped bending the car's path.

Mass cancels in this calculation. The skid threshold is the same for a truck and a bicycle on the same curve at the same speed. This is not obvious, but it's correct: more mass means more weight which means more available friction, but also more mass requiring more centripetal force, and the two effects cancel exactly.

<!-- → [FIGURE: Free-body diagram of car on flat curve, viewed from behind. Forces: weight (down), normal force (up), friction (horizontal, pointing toward center of curve). Caption: Friction is the only horizontal force. It points toward the center of the curve and supplies the entire centripetal force.] -->

There is one misconception so common it deserves a direct statement: there is no centrifugal force pushing you outward when a car turns. In the car's own (non-inertial, accelerating) frame, it *feels* like there's an outward push. Your body is trying to continue in a straight line while the car turns under you. From any inertial frame on the ground, the real force is the seat pushing you inward — centripetal — and your apparent "outward push" is just your own inertia. There is no outward force. There is an inward force and inertia that resists the change. They are not the same thing.

---

## Angular vocabulary, briefly

The centripetal-force setup needs a small vocabulary of angular quantities. For an object moving along a circular arc of radius $r$:

The arc length $\Delta s$ and the angle swept $\Delta\theta$ (in radians) are related by:

$$\Delta s = r\,\Delta\theta.$$

This is the definition of a radian — the angle that subtends an arc equal in length to the radius.

**Angular velocity** $\omega = \Delta\theta / \Delta t$, in radians per second, is how fast the angle is changing. Every point on a rigid rotating body shares the same $\omega$; they differ in linear speed because $v = r\omega$, and $r$ differs.

**Period** $T = 2\pi/\omega$ is the time for one full revolution.

These three quantities — $\omega$, $r$, $T$ — plus the centripetal formula $a_c = v^2/r = r\omega^2$ are the complete vocabulary for any uniform circular motion problem.

<!-- → [TABLE: Angular vocabulary summary. Columns: quantity, symbol, formula relating it to linear quantities, units. Rows: arc length, angular velocity, linear speed, period, centripetal acceleration. Caption: Every circular-motion problem reduces to identifying r, v (or ω), and the physical source of the centripetal force.] -->

---

## The second part: gravity is universal, and it falls off as $1/r^2$

Newton's question in 1666 was this: the same Earth that pulls an apple to the ground might also pull the Moon. If so, what holds the Moon in its orbit?

An inverse-square law for gravity. If the gravitational force between two masses $m_1$ and $m_2$ falls off as $1/r^2$:

$$F = G\frac{m_1 m_2}{r^2},$$

where $G = 6.674 \times 10^{-11} \text{ N}\cdot\text{m}^2/\text{kg}^2$, then the Moon's orbital acceleration can be predicted from the same $g$ we measure on the surface — just scaled by the ratio of distances squared.

Earth's surface is $R_\oplus \approx 6.38 \times 10^6$ m from its center. The Moon is $r_{\text{Moon}} \approx 3.84 \times 10^8$ m from Earth's center — about 60 times further. An inverse-square law predicts the Moon's gravitational acceleration is $60^2 = 3600$ times weaker than surface $g$:

$$a_{\text{Moon}} \approx \frac{9.80}{3600} \approx 0.0027 \text{ m/s}^2.$$

Newton then calculated what centripetal acceleration the Moon's orbit actually requires. The Moon takes $27.3$ days ($\approx 2.36 \times 10^6$ s) to travel around Earth at radius $3.84 \times 10^8$ m. Its orbital speed is $v = 2\pi r / T \approx 1{,}020 \text{ m/s}$. Centripetal acceleration:

$$a_c = \frac{v^2}{r} = \frac{(1{,}020)^2}{3.84 \times 10^8} \approx 0.0027 \text{ m/s}^2.$$

The two numbers agree. The acceleration the Moon needs to stay in its orbit is *exactly* what the inverse-square law predicts from Earth's surface gravity. The force pulling apples down and the force bending the Moon's path are the same force. Gravity is universal.

<!-- → [FIGURE: Two-panel diagram. Left panel: apple falling near Earth's surface, g = 9.80 m/s² shown. Right panel: Moon in orbit, a_c = 0.0027 m/s² shown. Center: formula showing ratio (R/r_Moon)² = 1/3600 connecting the two. Caption: The same inverse-square gravity that accelerates the apple at 9.80 m/s² accelerates the Moon at 0.0027 m/s². The ratio of accelerations equals the inverse ratio of squared distances.] -->

### What $G$ tells you

The gravitational constant $G = 6.674 \times 10^{-11}$ is tiny. The force between two $1 \text{ kg}$ objects $1 \text{ m}$ apart is $6.674 \times 10^{-11}$ N — a hundred billion times smaller than their weight. Gravity between everyday objects is negligible. Gravity matters when at least one mass is astronomical.

The smallness of $G$ also means we had to measure it very carefully. Henry Cavendish did it in 1798 with a torsion balance — two small lead spheres on a rod, suspended by a wire, attracted toward two large lead spheres. The tiny twist of the wire, measured under a microscope, gave $G$ to within a few percent. The experiment was called "weighing the Earth" at the time, because once you have $G$, you can compute $M_\oplus$ from $g = GM_\oplus/R_\oplus^2$.

<!-- → [FIGURE: Diagram of the Cavendish torsion balance. Top-down view. Two small spheres on a horizontal rod suspended by a thin wire. Two large fixed spheres positioned nearby, attracting the small ones. Twist angle θ labeled. Caption: Cavendish measured G in 1798 by observing the tiny twist of a torsion wire caused by gravitational attraction between small and large lead spheres. The apparatus was so sensitive it had to be enclosed and read by telescope to avoid air currents.] -->

The link between surface gravity and Newton's law is worth making explicit. On Earth's surface, the law gives:

$$F = G\frac{M_\oplus m}{R_\oplus^2} = m \cdot \frac{GM_\oplus}{R_\oplus^2} = mg,$$

so:

$$g = \frac{GM_\oplus}{R_\oplus^2} = \frac{(6.674\times10^{-11})(5.97\times10^{24})}{(6.378\times10^6)^2} \approx 9.80 \text{ m/s}^2.$$

The $g$ we've been using since Chapter 2 falls out of Newton's law of gravitation exactly. There's nothing arbitrary about $9.80 \text{ m/s}^2$ — it's determined by Earth's mass and radius, both of which we can measure.

<!-- → [TABLE: Surface gravity on bodies in the solar system. Columns: body, mass (kg), radius (m), g (m/s²), g relative to Earth. Rows: Moon, Mars, Earth, Jupiter, Sun. Caption: Surface gravity scales as M/R². Larger mass helps; smaller radius helps more, because R appears squared.] -->

---

## Orbital mechanics: centripetal force = gravitational force

For a satellite in circular orbit at radius $r$ around a central mass $M$, setting gravitational force equal to centripetal force:

$$G\frac{Mm}{r^2} = \frac{mv^2}{r}.$$

The satellite's mass $m$ cancels. Solve for orbital speed:

$$v = \sqrt{\frac{GM}{r}}.$$

This is a clean result. The orbital speed depends on the central mass and the radius, and on nothing else. The satellite's own mass is irrelevant.

Period follows from $T = 2\pi r / v$:

$$T = \frac{2\pi r}{\sqrt{GM/r}} = 2\pi\sqrt{\frac{r^3}{GM}},$$

so:

$$T^2 = \frac{4\pi^2}{GM}\, r^3.$$

![Log-log plot of orbital period squared vs orbital radius cubed. All eight planets — Mercury through Neptune — lie on a straight line of slope 1, confirming T² ∝ r³ across three orders of magnitude in radius.](../images/06-uniform-circular-motion-and-gravitation-fig-05.png)
*Figure 6.5 — Kepler's Third Law — T² ∝ r³, Verified by the Eight Planets*

$T^2 \propto r^3$. This is Kepler's third law. Kepler found it empirically in 1619 by looking at the data for the planets. Newton derived it from first principles — from $F = ma$ and $F = GMm/r^2$ — in roughly this many lines of algebra. The derivation is what convinced the scientific community. An empirical pattern, explained from a deeper law, is incomparably more convincing than the pattern alone.

The proportionality constant $4\pi^2/GM$ depends on which central body you're orbiting. For orbits around Earth, $GM_\oplus \approx 3.986 \times 10^{14}$ m³/s². For orbits around the Sun, $GM_\odot \approx 1.327 \times 10^{20}$ m³/s². Once you know which body, Kepler's third law lets you compare *any* two orbits without knowing $G$ or $M$ explicitly.

<!-- → [CHART: Log-log plot of orbital period T² vs. orbital radius r³ for solar system planets. Points: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune. All points fall on a single straight line of slope 1 (since T² ∝ r³). Caption: Kepler's third law on a log-log plot. Every planet falls on the same line — the slope is exactly 1. Newton's derivation explains why: the proportionality constant 4π²/GM_☉ is the same for all bodies orbiting the Sun.] -->

### Worked example: *Sputnik 1*

*Sputnik 1* orbited at about $250 \text{ km}$ altitude. The orbital radius is:

$$r = R_\oplus + 250 \text{ km} = 6.378\times10^6 + 2.5\times10^5 = 6.628\times10^6 \text{ m}.$$

Orbital speed:

$$v = \sqrt{\frac{GM_\oplus}{r}} = \sqrt{\frac{3.986\times10^{14}}{6.628\times10^6}} = \sqrt{6.014\times10^7} \approx 7{,}755 \text{ m/s}.$$

About $7.8 \text{ km/s}$ — twenty times the speed of a commercial aircraft.

Period:

$$T = \frac{2\pi r}{v} = \frac{2\pi \times 6.628\times10^6}{7{,}755} \approx 5{,}368 \text{ s} \approx 89.5 \text{ min}.$$

![Stylized Sputnik with antennas, orbital parameters annotated: mass 83.6 kg, diameter 58 cm, perigee 215 km, apogee 939 km, orbital period 96 minutes. Launched October 4, 1957 from Baikonur.](../images/06-uniform-circular-motion-and-gravitation-fig-01.png)
*Figure 6.1 — Sputnik 1 — First Artificial Satellite, 96-Minute Orbit*

*Sputnik 1*'s actual published period was $96.2$ minutes. We got $89.5$. The discrepancy is real: *Sputnik 1*'s orbit was elliptical, with perigee at $215 \text{ km}$ and apogee at $939 \text{ km}$. We used perigee altitude for a circular calculation. For a circular orbit at the average altitude, the calculation would land closer. The physics is right; the geometry is simplified.

The point is not the precision of this particular number. The point is that from two quantities — Earth's mass and *Sputnik*'s altitude — we can predict the orbital period to within a few percent. Newton wrote this down in 1687. The Soviets confirmed it in 1957.

### The astronaut who is not weightless

Astronauts on the International Space Station float. Everything in the cabin floats. It looks like weightlessness. It is not weightlessness, in the sense that gravity hasn't stopped acting. At $400 \text{ km}$ altitude, Earth's gravitational acceleration is:

$$g_{400} = \frac{GM_\oplus}{(R_\oplus + 400\text{ km})^2} = \frac{3.986\times10^{14}}{(6.778\times10^6)^2} \approx 8.68 \text{ m/s}^2.$$

That's $89\%$ of surface gravity. The astronauts are being pulled toward Earth at $8.68 \text{ m/s}^2$. The station is being pulled toward Earth at $8.68 \text{ m/s}^2$. The astronaut and the station are in free fall together, toward Earth, at the same rate. There is no relative acceleration between astronaut and station — which is exactly what "floating" feels like. The sensation of weight requires a surface pushing back against gravity. In free fall, nothing pushes back.

<!-- → [FIGURE: ISS in orbit with astronaut inside. Two labeled acceleration vectors: one on ISS (8.68 m/s² toward Earth), one on astronaut (8.68 m/s² toward Earth). Both identical. Caption: Both the ISS and the astronaut accelerate toward Earth at the same rate. No relative acceleration, no feeling of a surface pushing back — that's what floating in free fall feels like.] -->

This is the equivalence principle in its simplest form: free fall is locally indistinguishable from the absence of gravity. Einstein elevated this to a foundational principle of general relativity. For now, it explains why every orbital astronaut floats — they are not beyond Earth's gravity; they are in its grasp, falling continuously.

---

## Why this all fits together

The two pieces of this chapter are not actually separate.

Centripetal acceleration is the kinematic description of what any circular path requires: an inward acceleration of $v^2/r$. That acceleration needs a real force to produce it.

![Log-log plot of gravitational acceleration vs distance from Earth's center. Surface (R_E): 9.81 m/s². Moon's orbit (60 R_E): 0.0027 m/s². Sun distance (~23000 R_E): 6×10⁻⁶ m/s². Points fall on a straight line of slope −2.](../images/06-uniform-circular-motion-and-gravitation-fig-04.png)
*Figure 6.4 — Gravity Falls Off as 1/r² — Slope of −2 on Log-Log Axes*

Gravity is an attractive force that falls off as $1/r^2$. For a satellite in orbit, gravity is the inward force supplying the centripetal acceleration. The satellite's mass cancels, and what you get is the formula for orbital speed $v = \sqrt{GM/r}$, which leads directly to Kepler's third law.

The philosophical weight of this is worth pausing on. Kepler's third law was an empirical regularity — a pattern in the data, observed by one of the most meticulous astronomers in history, not explained, just described. Newton looked at the same pattern and said: this follows from an inverse-square force law. He then derived the pattern algebraically from the force law. The explanation is deeper than the observation. We now know *why* Kepler's third law holds — not just that it does.

That kind of thing — a force law that unifies falling apples, the Moon's orbit, the periods of planets, the path of comets, and the orbits of satellites not yet built — is the template for how the deepest physics works. Not just pattern-matching. Derivation from principle.

<!-- → [INFOGRAPHIC: Two-column diagram. Left: "What Kepler found (1619)" — three laws stated empirically, labeled as "pattern in data." Right: "What Newton derived (1687)" — same three laws, each labeled with the step in the derivation from F = GMm/r². Arrow connecting the two sides labeled "explanation from first principles." Caption: Kepler described what planets do. Newton explained why. The move from description to derivation is the signature of a genuine physical theory.] -->

---

## Exercises

### Warm-up

**6.1** *(LO 1)* A bicycle wheel of radius $0.35 \text{ m}$ rotates at $10$ revolutions per second. (a) What is its angular velocity in rad/s? (b) What is the linear speed of a point on the rim?

**6.2** *(LO 2)* A $0.50 \text{ kg}$ stone on a $1.0 \text{ m}$ string is whirled in a horizontal circle at $4.0 \text{ m/s}$. What is the tension in the string?

**6.3** *(LO 3)* A car rounds a flat curve of radius $40 \text{ m}$ at $20 \text{ m/s}$. What is the minimum coefficient of static friction between tires and road?

**6.4** *(LO 4)* Compute the gravitational force between two people ($70 \text{ kg}$ and $60 \text{ kg}$) sitting $1.0 \text{ m}$ apart. Compare to the weight of either person. What does this say about why we don't feel gravity from other people?

### Application

**6.5** *(LO 2, 3)* A $1{,}000 \text{ kg}$ car crests a hill of radius of curvature $50 \text{ m}$ at $15 \text{ m/s}$. (a) Centripetal acceleration at the top? (b) Normal force from the road at the top? (c) Maximum speed at which the car stays in contact with the road?

**6.6** *(LO 4)* Derive Earth's surface gravity $g$ from $G$, $M_\oplus = 5.97\times10^{24} \text{ kg}$, $R_\oplus = 6.378\times10^6 \text{ m}$. Compare to $9.80 \text{ m/s}^2$.

**6.7** *(LO 4, 5)* (a) Compute the ISS orbital speed at $r = 6{,}778 \text{ km}$. (b) Compute its orbital period. (c) The ISS appears to circle Earth about every $90$ minutes — does your answer match?

**6.8** *(LO 5)* Mars orbits the Sun at $1.52$ AU; Earth orbits at $1.00$ AU with period $1$ year. Use Kepler's third law to compute Mars's orbital period.

### Synthesis

**6.9** *(LO 1, 2, 3)* A $60 \text{ kg}$ pilot pulls a tight banked turn of radius $200 \text{ m}$ at $150 \text{ m/s}$. (a) Centripetal acceleration in $\text{m/s}^2$ and in $g$'s. (b) Centripetal force on the pilot. (c) Apparent weight (force from seat).

**6.10** *(LO 4, 5)* Hubble orbits at $r = 6{,}918 \text{ km}$ from Earth's center. (a) Orbital speed. (b) Period in minutes. (c) Distance traveled per orbit in km.

**6.11** *(LO 4, 5)* A planet has twice Earth's mass and the same radius. What is its $g$? Your weight there (if you weigh $700 \text{ N}$ on Earth)? Repeat for Earth's mass but half the radius.

### Challenge

**6.12** *(LO 5, beyond chapter)* Compute the orbital radius for a geosynchronous orbit (period $= 24$ h) around Earth using Kepler's third law. Convert to altitude. Compare to the published $35{,}786 \text{ km}$.

**6.13** *(beyond chapter)* The Sun has mass $M_\odot = 1.989\times10^{30} \text{ kg}$. Pluto orbits at $r = 5.91\times10^{12} \text{ m}$. (a) Pluto's orbital period. (b) Orbital speed. (c) Compare both to Earth's values. (d) Which Kepler scaling dominates the difference?

---

## LLM Exercise — Chapter 6: Circular Motion in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A circular-motion or gravitational analysis of one element of your anchor phenomenon.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste 1-sentence description].

For Chapter 6, I want to apply uniform circular motion (centripetal acceleration, a_c = v²/r) and/or Newton's gravitation to my phenomenon. Please:

1. Identify ONE circular or rotational element in my phenomenon. Examples:
   - Bike commute: cornering on the bike — what's the centripetal acceleration on a typical curve, and what minimum friction does it require?
   - Coffee maker: a centrifugal pump or a spinning grinder — what centripetal force on a coffee particle?
   - Basketball: spin on the ball during the shot — what's the centripetal acceleration of a point on the surface?
   - Marathon: running on a curved track section — what centripetal force on the runner?
   - Espresso: the orbit of a coffee particle in the puck during 9-bar extraction (any vortex flow). Or the rotation of a milk frother.

2. Compute the relevant quantities (v or ω, r, a_c, F_c). Identify what physical force provides F_c.

3. Express a_c in units of g as a sanity check.

4. Identify any gravitational effects in your phenomenon (most commonly: weight as the dominant downward force, but also tidal effects, orbital motion if your phenomenon involves space).

5. One Fermi-style sanity check.

6. Identify which assumption (uniform circular motion, neglected gravity, neglected drag) is most likely to bite.

7. One sentence on how this connects to Chapter 7 (work and energy) — circular motion at constant speed does no net work; why?

Save the output as logbook/chapter-06-circular-and-gravitation.md.
```

### What this produces

A sixth Logbook entry: a circular-motion analysis applied to your phenomenon, often surprising in magnitude (small radii at moderate speeds give large $a_c$).

### How to adapt this prompt

- *For phenomena with no obvious circular component* (a straight-line marathon, a vertical pour): bring in Earth's rotation or the Earth-Sun gravitational force as the gravitational element.
- *For ChatGPT or Gemini:* identical with interface substitutions.
- *For Claude Code:* if you have angular-velocity or RPM data, paste it; ask for centripetal force and required friction.

### Connection to previous chapters

Builds on Chapter 4 (force, $F = ma$) and Chapter 5 (friction often provides centripetal force). Newton's law of gravitation is a specific application of the force framework from Chapter 4.

### Preview of next chapter

Chapter 7 introduces work and energy as alternative bookkeeping for mechanical systems. Circular motion is interesting for energy: at constant speed, no net work is done (force is perpendicular to motion), even though force is applied continuously. Gravity, in contrast, does substantial work when objects fall.

---

**Tags:** circular-motion, gravitation, Keplers-laws, centripetal-acceleration, orbits
