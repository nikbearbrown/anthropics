# Chapter 14 — Gravitation

## Three possible titles

Newton's Law of Universal Gravitation: Inverse Squares and the Machinery of Orbits

Gravity Between All Things: From Lead Spheres in a Garden Shed to Spiraling Black Holes

The Inverse Square Law: How Mass Curves Space and Motion Follows

---

## TL;DR

Gravity is the only force that cannot be shielded. Every mass attracts every other mass with a force proportional to the product of their masses and inversely proportional to the square of the distance between them. From this one law—$F = Gm_1m_2/r^2$—flow orbital mechanics, escape velocities, tidal forces, and the geometry of black holes. This chapter shows the law on the page, derives gravitational potential energy from first principles, and traces the machinery from Cavendish's 1798 garden shed through LIGO's detection of colliding black holes 1.3 billion light-years away.

---

## Cold open: Henry Cavendish weighs the Earth in his garden shed

It is June 1798, and Henry Cavendish is standing in a garden shed in London surrounded by a device that might be the most elegant piece of apparatus ever built to measure something almost impossibly small.

The device is a torsion balance — imagine a thin wooden rod suspended horizontally by a single quartz fiber, fine as hair. At each end of the rod, a small lead sphere is hung, each about 2 centimeters across, each weighing an ounce or so. The whole thing is perhaps a foot long. Below it, and above it, are larger lead spheres, each weighing 175 pounds. The large spheres can be moved closer to or farther from the small ones.

Gravity pulls the small spheres toward the large ones. The pull is absurdly weak — for all the lead there is, the gravitational force is only a millionth of a millinewton. But weak is not zero. When Cavendish brings the large spheres near, the tiny horizontal rods twists slightly — minutely — against the stiffness of the quartz fiber. The rod twists just enough to be measured.

By measuring the twist, Cavendish measured the gravitational force between the masses. With that force, and using the inverse square law that Newton had proposed a century before, he calculated something no one had ever calculated: the mass of the Earth.

The result was $5.97 \times 10^{24}$ kg.

The answer we use now, more than two centuries later, is $5.972 \times 10^{24}$ kg.

Cavendish died in 1810. He never published this work. A colleague found the papers, did the calculations, and presented them to the world. The measurement stands as one of the great achievements in experimental physics: absolute precision on something so small that it slips beneath ordinary perception, and accuracy so close to the truth that modern methods have only fine-tuned it at the third decimal place.

---

## Concept 1 — Newton's Law of Universal Gravitation: The Inverse Square Law from First Principles

### The law and its scope

Every mass attracts every other mass. Newton expressed this in 1687 as a mathematical statement:

$$\vec{F}_{12} = G\frac{m_1 m_2}{r^2}\hat{r}_{12}$$

Read it this way: The force on object 1 due to object 2 is the product of their masses, divided by the square of the distance between them, multiplied by a constant *G*, and pointing from object 1 toward object 2.

The constant *G* is called the universal gravitational constant. Cavendish's experiment measured it: $G = 6.67 \times 10^{-11}$ N·m²/kg².

That is a very small number. To feel its size, calculate the force between two 1-kg masses sitting 1 meter apart: $6.67 \times 10^{-11}$ N. That is roughly the weight of a grain of pollen. Two kilograms of matter, separated by a single meter, pull on each other with the force of a speck.

Yet that speck of force, applied over the vast distances and enormous masses of planets and stars, governs the architecture of the cosmos.

The law applies exactly to point masses — all the mass located at a single point. For spherically symmetric objects (planets, stars, uniform spheres), the law applies if you measure the distance between their centers. For asymmetric objects where the separation is large compared to their size, the law works reasonably well using the center of mass of each object.

### Why inverse square?

The inverse square dependence on distance is not arbitrary. It emerges from geometry.

Imagine a point source of mass — or, think of it as a light source so we can use familiar intuition. The "influence" of that mass spreads outward in all directions equally. At a distance $r$, that influence is spread over the surface of a sphere. The surface area of a sphere is $4\pi r^2$.

If the strength of the influence at the surface is inversely proportional to the area it must cover, then strength is proportional to $1/r^2$.

This is why the same inverse square law shows up in electrostatics, in light intensity, in sound pressure: any influence that spreads radially outward from a point source obeys the inverse square law as a consequence of geometry alone.

### Specification: What the mass *is* in Newton's law

A student once asked: Are the $m_1$ and $m_2$ in Newton's gravitational law the same as the $m$ in $F = ma$?

Newton assumed they were. But this is an assumption that required experimental verification. Suppose the gravitational mass of an object (the mass that determines how strong its gravitational pull) were different from its inertial mass (the mass that resists acceleration). Then the gravitational force on an object would not produce the same acceleration for objects of different composition.

Experiments show, to extraordinary precision, that they are the same. An iron sphere and a wooden sphere, dropped in a vacuum, fall at the same rate. The gravitational mass equals the inertial mass. This is not a theorem that can be proved from first principles; it is an experimental fact, and it is one of the starting points for Einstein's general relativity.

### Worked example — the gravitational force between the ISS and a spacewalking astronaut

The International Space Station has a mass of approximately $370,000$ kg. An astronaut in a spacesuit has a mass of roughly $150$ kg. During a spacewalk, the astronaut is $20$ m from the center of mass of the station. What is the gravitational force between them?

Using the law directly:

$$F = G\frac{m_1 m_2}{r^2} = (6.67 \times 10^{-11}\ \text{N·m}^2/\text{kg}^2)\frac{(370,000\ \text{kg})(150\ \text{kg})}{(20\ \text{m})^2}$$

$$F = (6.67 \times 10^{-11})\frac{55,500,000}{400} = 6.67 \times 10^{-11} \times 138,750 = 9.25 \times 10^{-6}\ \text{N}$$

That is nine micronewtons. Nine millionths of a newton.

For comparison, the astronaut's weight on Earth is roughly $150 \times 9.8 = 1470$ N. The gravitational force pulling the astronaut toward the station is about one-hundred-millionth the astronaut's weight at home.

This is why astronauts must tether themselves during spacewalks. Gravity alone will not save them if they drift away. They would need a gentle push to return, but gravity alone would not provide it.

### Common misconceptions

**Gravity is the weakest of the four fundamental forces.** It is. But do not confuse "weakest" with "negligible." Gravity is so weak that the gravitational attraction between two ordinary objects is imperceptible. Yet gravity is the dominant force on cosmic scales. The reason is that gravity is always attractive and acts on all matter, whereas the other forces (electromagnetic, strong nuclear, weak nuclear) can cancel or require specific properties.

**Heavier objects fall faster.** They do not. In a vacuum, all objects fall at the same rate regardless of mass. The gravitational force on a heavier object is larger, but so is its inertia, and the effects cancel exactly. This was one of the great insights Galileo understood without calculus or careful measurement of free fall. Newton's law shows why: $a = F/m = (Gm_{\text{Earth}}/r^2)$. The mass cancels. The acceleration depends only on the mass of the Earth and the distance, not on the falling object's mass.

---

## Concept 2 — Gravitational Potential Energy and Escape Velocity: Deriving from Work and Force

### The definition of gravitational potential energy over large distances

Near Earth's surface, where the gravitational field is nearly constant, we use $U = mgh$. But when distances are large enough that gravity changes significantly with position, this simple form fails. We need a definition that works anywhere.

Potential energy is defined through work. The change in potential energy is the negative of the work done by the force:

$$\Delta U = -\int_{r_1}^{r_2} \vec{F} \cdot d\vec{r}$$

For gravitational force, $\vec{F}$ points toward the center (inward), and we integrate radially outward. So $\vec{F} \cdot d\vec{r}$ is negative, and the integral is:

$$\Delta U = -\int_{r_1}^{r_2} \left(-\frac{GMm}{r^2}\right) dr = GMm\int_{r_1}^{r_2} \frac{dr}{r^2}$$

Evaluating:

$$\Delta U = GMm\left[-\frac{1}{r}\right]_{r_1}^{r_2} = GMm\left(\frac{1}{r_1} - \frac{1}{r_2}\right)$$

To define $U$ as a function of position, we choose a reference point. By convention, we set $U = 0$ at $r = \infty$. Then:

$$U(r) = -\frac{GMm}{r}$$

This says: at any finite distance, the potential energy is negative. The farther away, the less negative (higher). At infinity, it is zero. This makes physical sense: you must do positive work to pull two masses apart, raising the potential energy (making it less negative).

### Escape velocity: the speed required to leave forever

Escape velocity is the minimum speed an object needs, launched from the surface of a celestial body, to escape to infinity and never return.

The condition is simple: at escape velocity, the object reaches infinity with zero speed. At that point, all its kinetic energy has been converted to potential energy.

Conservation of energy gives:

$$K_{\text{surface}} + U_{\text{surface}} = K_{\infty} + U_{\infty}$$

$$\frac{1}{2}mv_{\text{esc}}^2 - \frac{GMm}{R} = 0 + 0$$

Solving for $v_{\text{esc}}$:

$$v_{\text{esc}} = \sqrt{\frac{2GM}{R}}$$

Note that the escape velocity is independent of the mass of the escaping object. A feather and a boulder have the same escape velocity from the same body. The escape velocity depends only on the mass and radius of the body being escaped from.

### Worked example — escape velocities from Earth and the Sun

From Earth ($M_E = 5.97 \times 10^{24}$ kg, $R_E = 6.37 \times 10^6$ m):

$$v_{\text{esc}} = \sqrt{\frac{2(6.67 \times 10^{-11})(5.97 \times 10^{24})}{6.37 \times 10^6}} = \sqrt{1.25 \times 10^8} = 1.12 \times 10^4\ \text{m/s}$$

That is about 11.2 km/s or 25,000 mph. A rocket launched from the equator (where Earth's rotation helps, adding about 460 m/s) needs only 10.7 km/s of additional velocity.

From the Sun ($M_{\odot} = 1.99 \times 10^{30}$ kg), at Earth's orbital distance ($r = 1.50 \times 10^{11}$ m):

$$v_{\text{esc}} = \sqrt{\frac{2(6.67 \times 10^{-11})(1.99 \times 10^{30})}{1.50 \times 10^{11}}} = \sqrt{1.77 \times 10^8} = 4.21 \times 10^4\ \text{m/s}$$

That is about 42 km/s. To escape the solar system from Earth's position requires roughly four times the speed needed to escape Earth.

But Earth itself orbits at 30 km/s. If you launch in the direction Earth is already moving, you need only $42 - 30 = 12$ km/s of additional velocity. Space agencies use this: probes launched toward the Sun's orbit take advantage of Earth's orbital motion to save fuel.

### Common misconceptions

**Escape velocity is the velocity you need to stay in orbit.** Wrong. Escape velocity is the speed to leave forever. Orbital velocity is different — it is the speed to fall around the body continuously without crashing or escaping. For Earth's surface, orbital velocity is about 7.9 km/s; escape velocity is 11.2 km/s.

**Nothing can escape a black hole because escape velocity exceeds the speed of light.** This is the intuition, and it is right, but the reasoning is incomplete. Escape velocity derived from Newton's mechanics gives the right answer for black holes as a limiting case, but the full story requires general relativity. Inside the event horizon, spacetime itself is so distorted that there is no path to infinity.

---

## Concept 3 — Orbits: Kepler's Laws and the Machinery of Circular and Elliptical Motion

### Circular orbits: velocity and period

A satellite in circular orbit experiences the gravitational force as a centripetal force — the force pointing toward the center that curves its path.

Setting gravitational force equal to the centripetal force:

$$\frac{Gm_1 m_2}{r^2} = m_2 \frac{v_{\text{orbit}}^2}{r}$$

The mass $m_2$ cancels:

$$v_{\text{orbit}} = \sqrt{\frac{GM}{r}}$$

For the International Space Station at $r = 6.77 \times 10^6$ m (400 km above Earth's surface):

$$v_{\text{orbit}} = \sqrt{\frac{(6.67 \times 10^{-11})(5.97 \times 10^{24})}{6.77 \times 10^6}} = 7.67 \times 10^3\ \text{m/s} \approx 7.7\ \text{km/s}$$

That is about 17,000 mph. A complete orbit takes:

$$T = \frac{2\pi r}{v_{\text{orbit}}} = \frac{2\pi(6.77 \times 10^6)}{7.67 \times 10^3} = 5.55 \times 10^3\ \text{s} \approx 92\ \text{minutes}$$

So the ISS circles Earth roughly every 90 minutes, with astronauts experiencing sunrise and sunset every 45 minutes.

To derive the period without calculating velocity first, use $v = 2\pi r / T$:

$$\sqrt{\frac{GM}{r}} = \frac{2\pi r}{T}$$

$$T = 2\pi\sqrt{\frac{r^3}{GM}}$$

Squaring both sides:

$$T^2 = \frac{4\pi^2 r^3}{GM}$$

This is **Kepler's Third Law**: the square of the orbital period is proportional to the cube of the orbital radius. It was empirical observation when Kepler found it in 1609. Newton showed it was a consequence of the inverse square law.

### Elliptical orbits and the conic sections

Not all orbits are circles. An object's trajectory in a gravitational field can be any of the four conic sections: a circle (special case, eccentricity $e = 0$), an ellipse ($0 < e < 1$), a parabola ($e = 1$), or a hyperbola ($e > 1$).

Which path the object follows depends on its total mechanical energy:

- **Negative total energy**: bound orbit (ellipse or circle). The object cannot escape; it will orbit forever.
- **Zero total energy**: parabolic orbit. The object reaches infinity with zero speed, just barely escaping.
- **Positive total energy**: hyperbolic orbit. The object escapes to infinity with speed to spare; it passes by once and never returns.

For elliptical orbits, the period is determined by the semi-major axis $a$ (half the longest diameter):

$$T^2 = \frac{4\pi^2 a^3}{GM}$$

This is the same form as for circular orbits, but with $a$ replacing $r$. This is why Kepler's Third Law holds for all bound orbits.

### Kepler's Second Law: equal areas in equal times

A planet moves faster when closer to the Sun and slower when farther away. Kepler observed that the planet sweeps out equal areas in equal times.

This is a direct consequence of **conservation of angular momentum**. The gravitational force always points toward the Sun (radially inward). Such a force exerts no torque about that center. Thus angular momentum is conserved.

The area swept out in time $dt$ is:

$$dA = \frac{1}{2}r v_{\perp} dt = \frac{1}{2m}r(m v_{\perp}) dt = \frac{L}{2m}dt$$

where $v_{\perp}$ is the component of velocity perpendicular to the radius, and $L = m r v_{\perp}$ is the angular momentum.

Since $L$ is constant:

$$\frac{dA}{dt} = \frac{L}{2m} = \text{constant}$$

The areal velocity is constant. This is Kepler's Second Law emerging from the conservation of angular momentum.

### Worked example — Halley's Comet and Kepler's Third Law

Halley's Comet returns every 75.3 years. What is its semi-major axis? If its perihelion (closest approach to the Sun) is 0.586 AU, what is its aphelion (farthest distance)?

Rearranging Kepler's Third Law:

$$a = \left(\frac{GM_{\odot}}{4\pi^2} T^2\right)^{1/3}$$

Converting 75.3 years to seconds: $(75.3 \times 365.25 \times 24 \times 3600) = 2.376 \times 10^9$ s.

$$a = \left(\frac{(6.67 \times 10^{-11})(1.99 \times 10^{30})}{4\pi^2}(2.376 \times 10^9)^2\right)^{1/3}$$

$$a = (2.67 \times 10^{12}\ \text{m})^{1/3} = 2.67 \times 10^{12}\ \text{m} = 17.8\ \text{AU}$$

The semi-major axis is the average of perihelion and aphelion:

$$a = \frac{\text{perihelion} + \text{aphelion}}{2}$$

$$17.8 = \frac{0.586 + \text{aphelion}}{2}$$

$$\text{aphelion} = 35.0\ \text{AU}$$

Halley's Comet travels from 0.586 AU (inside Venus's orbit) to 35 AU (beyond Neptune). The ellipse is so elongated that the comet spends most of its time in the distant, slow portions of its orbit, racing through the inner solar system in just a few months.

### Common misconceptions

**An orbit is a stable path that objects naturally follow.** No. An orbit is a dynamic balance. Gravity pulls the satellite toward the center; the satellite's velocity pulls it away. The two exactly balance. Slow the satellite down slightly, and gravity wins — the satellite spirals inward. Speed it up, and the satellite moves to a higher orbit. Perfect balance at each radius yields a specific speed, and that speed determines the period.

**Weightlessness in orbit means gravity is not acting.** False. Astronauts in orbit are in free fall. Gravity is pulling them toward Earth at nearly the same strength as at the surface. But they are falling at the same rate as the spacecraft. The spacecraft and the astronaut fall together, so there is no net force between them. The astronaut feels weightless not because gravity is absent but because they are accelerating together with the spacecraft.

---

## Synthesis: From Newton to Einstein, and gravity's place in the cosmos

Newton's law of universal gravitation explains nearly everything in the solar system to a precision of better than one part in ten million. But gravity operates on a spectrum of strength, and at the extremes, the law breaks down.

At weak fields (like Earth's surface or even near the Sun), Newton's law predicts the motion of planets, asteroids, and spacecraft so accurately that every probe we have sent into space was guided by Newtonian gravity. The discrepancies — such as a small excess precession of Mercury's orbit — were invisible until the twentieth century.

At strong fields (near black holes, in the early universe), gravity warps spacetime itself. Einstein's general relativity is required. In that theory, gravity is not a force pulling on masses but a curvature of the fabric of space and time. Massive objects bend spacetime; other objects follow the shortest paths through that bent space, and we perceive these paths as gravitational motion.

The bridge between the two is the principle of equivalence. Imagine you are in an elevator in free fall: you feel weightless. Einstein recognized that free fall and weightlessness are indistinguishable. A uniform gravitational field is locally equivalent to a uniform acceleration. This simple insight led him to a geometric theory of gravity that encompasses Newton's law as a limiting case in weak fields.

And yet here is the unfair advantage Newton had: nearly everything we can see and touch is governed by weak-field gravity. The orbits of planets, the tides in our oceans, the trajectory of a thrown ball — all follow from $F = Gm_1m_2/r^2$. The inverse square law is so successful that we often forget it is an approximation. It is an approximation to a deeper truth about the geometry of space and time. But it is an extraordinarily good one.

---

## Graduated exercises

### Warm-up

1. The Moon orbits Earth at an average distance of $384,400$ km with a period of 27.3 days. Using Kepler's Third Law, estimate the mass of Earth. (Assume the Moon's mass is negligible compared to Earth's.)

2. A satellite is in orbit at altitude 300 km above Earth's surface. Calculate its orbital speed using $v_{\text{orbit}} = \sqrt{GM/r}$, where $r$ includes Earth's radius.

3. Calculate the escape velocity from the surface of Mars. (Mass: $6.42 \times 10^{23}$ kg; radius: $3.39 \times 10^6$ m.)

### Application

4. A geosynchronous satellite remains fixed above a point on Earth's equator. Its orbital period is exactly 24 hours. Calculate the orbital radius (distance from Earth's center) and the altitude above Earth's surface. Does this orbit lie inside or outside the Moon's orbit?

5. Two spacecraft in orbit at the same altitude are separated by 10 m. Using the value of $G$ and Earth's mass, calculate the gravitational force between them. Compare this to the weight of one spacecraft (say, 5,000 kg) on Earth's surface.

### Synthesis

6. A projectile is launched vertically upward from Earth's surface with a speed of 5 km/s (well below escape velocity). How high does it rise before falling back? Use conservation of energy with the full gravitational potential energy function $U = -GMm/r$.

7. A comet is observed 2 AU from the Sun moving at 10 km/s. Is it in a bound or unbound orbit? Justify your answer using the total mechanical energy.

### Challenge

8. Show that the total mechanical energy of a circular orbit is exactly half the potential energy (and negative, the kinetic energy): $E = U/2 = -K$. What does this relationship tell you about the stability of circular orbits?

---

## Chapter summary

The gravitational force between two masses is $F = Gm_1m_2/r^2$, an inverse square law arising from geometry. Cavendish measured the constant $G$ in 1798 by observing the tiny twist of a torsion balance.

Gravitational potential energy far from Earth is $U = -GMm/r$, derived from integrating the gravitational force. The choice to set $U = 0$ at infinity is a matter of convenience; only differences in potential energy are physically meaningful.

Escape velocity from a body of mass $M$ and radius $R$ is $v_{\text{esc}} = \sqrt{2GM/R}$, independent of the mass of the escaping object.

Objects in circular orbit satisfy $v_{\text{orbit}} = \sqrt{GM/r}$, and their orbital period is given by Kepler's Third Law: $T^2 = (4\pi^2/GM)a^3$, where $a$ is the semi-major axis.

Kepler's First Law states orbits are ellipses with the central body (Sun, Earth) at one focus. Kepler's Second Law (equal areas in equal times) follows from conservation of angular momentum. Kepler's Third Law follows from the inverse square law.

The type of orbit—elliptical, parabolic, or hyperbolic—is determined by the total mechanical energy. Negative energy means a bound orbit; zero or positive energy means escape.

---

## What would change my mind

If observations showed that gravitational force depended on anything other than the product of masses and the inverse square of distance, Newton's law would need revision. So far, over more than three centuries and to precision better than one part in $10^7$ in the solar system, the law has held. Only near black holes and neutron stars, where general relativity is required, do we see systematic deviations.

---

## Still puzzling

Why gravity is so weak compared to the other fundamental forces remains a deep mystery. A proton and an electron attract via gravity with a force about $10^{39}$ times weaker than their electromagnetic attraction. Some theoretical physicists suspect that gravity is actually strong but acts in extra spatial dimensions we cannot directly perceive, diluting its strength in the three dimensions we can see. This is still speculative.

---

## Tags

#gravitation #Newton #orbits #Kepler #escape-velocity #torsion-balance #Cavendish #inverse-square-law #potential-energy #elliptical-orbits #mechanics #calculus-on-page



---

## LLM Exercise — Chapter 14: Orbital Mechanics and Kepler's Laws

**Project:** *Physics Simulation Toolkit*.

**What you're building this chapter:** A two-body orbital simulator, empirical verification of all three Kepler's laws, and the satellite-orbit / escape-velocity calculations.

**Tool:** Claude Code.

**The prompt:**

```
Chapter 14 task in the physics-simulation-toolkit. The chapter
derived $F = Gm_1m_2/r^2$ and showed how Kepler's three laws follow.
Verify all three numerically and build the orbital workhorses.

In `chapters/ch14_gravitation/`:

1. `simulations.py`:
   - `GravitationalForce(body_id_a, body_id_b, G=6.67e-11)` — a Force
     subclass: $\vec{F} = -G m_a m_b \hat{r}/r^2$.
   - `two_body_simulate(m1, m2, r0_vec, v0_vec, t_end, dt)` —
     symplectic integration of the two-body problem.
   - `orbital_period(semi_major_axis, central_mass)` —
     $T = 2\pi\sqrt{a^3/(GM)}$ (Kepler's third law).
   - `escape_velocity(M, r)` — $v_{\text{esc}} = \sqrt{2GM/r}$.
   - `vis_viva(M, r, a)` — orbital speed at distance r given semi-
     major axis a: $v^2 = GM(2/r - 1/a)$.
   - `kepler_third_check(simulation_output)` — given a recorded
     orbit, extract a and T, verify $T^2/a^3 = 4\pi^2/(GM)$.

2. `test_simulations.py`:
   - Earth-Sun: 1 AU semi-major axis, eccentricity ~0.017, period
     should come out 365.256 days. Verify to within RK4 integration
     precision.
   - Geostationary orbit: solve for the altitude where T = 24 hours.
     Verify the standard 35,786 km.
   - Kepler's first law (orbits are ellipses): on a generic
     elliptical orbit, verify numerically that the orbit closes (or
     drifts only due to integrator error) and that the geometry
     matches the analytical ellipse.
   - Kepler's second law (equal areas in equal times): compute the
     swept area between several time intervals. The ratios should
     equal the time ratios.
   - Kepler's third law: simulate orbits with several semi-major axes
     and central masses. Plot $T^2$ vs. $a^3$ — should be a straight
     line with slope $4\pi^2/(GM)$.

3. `benchmarks.py` — for a long-duration orbit (1000 periods), compare
   energy drift between explicit Euler, semi-implicit Euler, and RK4.
   The symplectic method should outperform RK4 on long-time accuracy
   for this Hamiltonian system. Quantify the drift.

4. `README.md` — decision cards. "Surprising findings": the symplectic
   advantage on long-time integration — this is why JPL uses
   symplectic integrators for planetary ephemerides, not RK4.

Commit as `ch14: two-body orbital mechanics with Kepler verification`.
```

**What this produces:** A two-body orbital simulator, empirical verification of all three Kepler's laws, geostationary-orbit calculation, and the long-time integrator comparison that justifies symplectic methods for planetary mechanics.

**How to adapt this prompt:**

- *For your own project:* Three-body and N-body integrations are the natural extensions. The chaotic three-body problem is one of physics's foundational results — worth simulating once.
- *For ChatGPT / Gemini:* Both work for the math. Cross-check the orbital period against the AU/year relationship.
- *For Claude Code:* Native fit. Plot the orbits in 2D and 3D.
- *For a Claude Project:* Not the fit.

**Connection to previous chapters:** Uses Ch 6 System, Ch 9 energy conservation, Ch 12 angular momentum (conserved in central-force orbits), and the symplectic-integrator infrastructure built up over Ch 4–9.

**Preview of next chapter:** Chapter 15 implements fluid mechanics — Bernoulli's equation verified, viscous-flow approximations, and the buoyancy/displacement laws.


---

##  AI Wayback Machine
The physics in this chapter didn't appear from nowhere. **Subrahmanyan Chandrasekhar** was the 1930 derivation, on the steamship voyage from India to England, of the upper mass limit for a stable white-dwarf star (the *Chandrasekhar limit*, ≈1.4 solar masses) — the first quantitative prediction that stars more massive than this must end as something more exotic, foundational to neutron stars and black holes — and despite the substance of the work, the name is far less recognized than it deserves. Here's a prompt to find out more — and then make it better.

**Run this:**

```
Who was Subrahmanyan Chandrasekhar, and how does their work on the Chandrasekhar limit and the gravitational collapse of stars connect to gravitation applied to stellar structure and the limit beyond which gravity wins decisively? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Subrahmanyan Chandrasekhar"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to walk through Chandrasekhar's specific 1930 derivation — the relativistic equation of state for degenerate electron gas, the integration that gave 1.4 solar masses, and the implication that more massive stars cannot end as white dwarfs
- Ask: "Arthur Eddington publicly humiliated Chandrasekhar at the 1935 Royal Astronomical Society meeting, calling the limit 'absurd.' Chandrasekhar was 25. What did the dispute cost the field, and how long did the limit take to be accepted?"
- Add the framing: "Answer in the register of Chandrasekhar's prose in *The Mathematical Theory of Black Holes* (1983) — precise, dignified, slightly austere"

What changes? What gets better? What gets worse?
