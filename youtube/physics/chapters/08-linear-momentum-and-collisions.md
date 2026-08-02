# Chapter 8 — Linear Momentum and Collisions

*Why throwing things backward is how you go forward.*

---

Here is something worth thinking about carefully. A rocket engine in vacuum has nothing to push against. No air, no ground, no water — nothing. And yet it accelerates. The engine throws combustion products backward at high speed, and the rocket goes forward. The surrounding medium is irrelevant. The engine doesn't need anything out there. All that matters is what's coming out the back.

This seems mysterious until you realize it isn't a special principle at all. It's the same thing that happens when you throw a ball from a skateboard, or fire a rifle, or push off a wall in a swimming pool. In every case, the thing going backward and the thing going forward are connected by a single bookkeeping rule: total momentum doesn't change.

That's the whole chapter. Let me show you why it's true, what it's good for, and how it combines with energy conservation to give you the machinery for solving virtually any collision.

---

## What momentum is

Chapter 4 gave us force and acceleration. Chapter 7 gave us energy. This chapter gives us a third way to characterize motion: **momentum**.

The momentum of an object is simply its mass times its velocity:

$$\mathbf{p} = m\mathbf{v}.$$

A vector, with the same direction as the velocity, with units of $\text{kg·m/s}$. A $0.057 \text{ kg}$ tennis ball moving at $55 \text{ m/s}$ has momentum $p \approx 3.1 \text{ kg·m/s}$. A $1{,}500 \text{ kg}$ car moving at $30 \text{ m/s}$ has momentum $p = 45{,}000 \text{ kg·m/s}$. The car's momentum is about $15{,}000$ times larger — partly because it's heavier, partly because speed multiplies the effect.

Momentum is not the same as kinetic energy. Energy goes as $v^2$; momentum goes as $v$. Double the speed and you double the momentum, but quadruple the kinetic energy. These are different quantities that account for different things, and you need both.

<!-- → [TABLE: Momentum vs. kinetic energy comparison for three objects. Columns: object, mass (kg), speed (m/s), momentum p = mv (kg·m/s), KE = ½mv² (J). Rows: tennis ball (0.057 kg, 55 m/s), car (1500 kg, 30 m/s), rifle bullet (0.010 kg, 400 m/s). Caption: Momentum scales with v; kinetic energy scales with v². A slow heavy object can have much more momentum than a fast light one while carrying less energy. You need both quantities to fully describe what happens in a collision.] -->

### Impulse: what changes momentum

Newton's second law says $\mathbf{F} = m\mathbf{a}$. Multiply both sides by $\Delta t$:

$$\mathbf{F}\,\Delta t = m\,\Delta\mathbf{v} = \Delta\mathbf{p}.$$

The product $\mathbf{F}\,\Delta t$ is called **impulse**, symbolized $\mathbf{J}$. The impulse-momentum theorem says: impulse equals change in momentum. A force applied over time changes momentum by the product of force and duration.

This is not new physics. It's Newton's second law in different clothing. But the clothing matters, because it reframes what's important. Instead of asking "what's the force?" and "what's the acceleration?", you ask "how much momentum changed?" and "over what time?"

That reframing turns out to be exactly right for understanding collisions and for engineering safety systems. Consider an airbag. A $70 \text{ kg}$ driver crashes at $8.3 \text{ m/s}$ ($30 \text{ km/h}$) and decelerates to zero. The change in momentum is fixed:

$$\Delta p = m\,\Delta v = 70 \times 8.3 = 581 \text{ kg·m/s}.$$

That number is determined by the crash — you can't change it. What you can change is how long the deceleration takes. With an airbag extending the contact to $\Delta t = 0.10 \text{ s}$:

$$F = \frac{\Delta p}{\Delta t} = \frac{581}{0.10} = 5{,}810 \text{ N}.$$

![F vs t curves for a driver decelerating from 30 m/s to 0. Steering column: short tall spike (~100 ms, ~50,000 N). Airbag: low wide plateau (~500 ms, ~10,000 N). Areas equal (same impulse, same Δp), peak heights very different.](../images/08-linear-momentum-and-collisions-fig-02.png)
*Figure 8.2 — Airbag vs Steering Column — Same Impulse, Different Peak Force*

Without an airbag, hitting the steering wheel in $\Delta t = 0.01 \text{ s}$:

$$F = \frac{581}{0.01} = 58{,}100 \text{ N}.$$

Ten times the force, from ten times the shorter contact. The impulse is the same in both cases. The force is not. Airbags work because they trade time for force — extend $\Delta t$ to reduce $F$ for the same $\Delta p$. The momentum bookkeeping is what makes this calculation clean.

<!-- → [CHART: Force-time graph for two crash scenarios. Area under both curves is identical (same impulse = same Δp = 581 kg·m/s). With airbag: broad low peak (~5,800 N over 0.10 s). Without airbag: narrow tall spike (~58,000 N over 0.01 s). Caption: The area under both curves is equal — same impulse, same Δp. The airbag extends time, reducing peak force by a factor of ten.] -->

Newton himself originally wrote his second law in terms of momentum: the rate of change of momentum equals the applied force. In his notation, $\mathbf{F} = d\mathbf{p}/dt$. For constant mass, $d\mathbf{p}/dt = m\,d\mathbf{v}/dt = m\mathbf{a}$, which recovers $F = ma$. But the momentum form is more general — it handles variable-mass situations (rockets burning fuel, water flowing from a tank) where the constant-mass version breaks down.

---

## Why momentum is conserved

Here is the argument. Take any system of objects interacting with each other. By Newton's third law, every force that object A exerts on object B is exactly matched by a force from object B back on object A — equal magnitude, opposite direction. When you sum up all the forces on all the objects inside the system, every internal force pair cancels. The only things left are external forces — forces from outside the system.

So the only thing that can change the total momentum of the system is a net external force. If there is no net external force — if the system is isolated — the total momentum is constant:

$$\mathbf{p}_{\text{total},i} = \mathbf{p}_{\text{total},f}.$$

This is conservation of momentum, and the proof is just Newton's third law applied to the whole system.

<!-- → [FIGURE: System boundary diagram. Circle labeled "system" containing two interacting objects A and B. Internal force arrows between A and B: equal and opposite, labeled F_AB and F_BA. External force arrow entering from outside the circle. Caption: Internal forces cancel in pairs — Newton's third law guarantees it. Only external forces change the system's total momentum. Draw the system boundary around what you care about, then identify what crosses it.] -->

The word "isolated" carries weight. Completely isolated systems are rare — gravity acts everywhere, friction acts on every surface. But *approximately* isolated is enough. During a brief collision, the contact forces between the colliding objects are typically orders of magnitude larger than gravity or friction acting over the same brief interval. A car crash lasts $0.1 \text{ s}$; gravity imparts a tiny impulse compared to the contact forces in that time. The collision approximately conserves momentum, and the approximation is usually excellent.

The deepest reason momentum is conserved is more beautiful than Newton's third law, though they're equivalent for our purposes. In 1918, the mathematician Emmy Noether proved that every continuous symmetry of the laws of physics corresponds to a conservation law. Momentum conservation is a consequence of *translational symmetry* — the fact that the laws of physics are the same here as they are one meter to the left. If the physics depended on where you were, momentum would not be conserved. It does not, so it is.

### Recoil and rockets

A rifle at rest fires a bullet. Before: everything stationary, total momentum zero. After: bullet moving forward, rifle moving backward. Total momentum is still zero — the forward momentum of the bullet equals the backward momentum of the rifle in magnitude.

For a $5.0 \text{ kg}$ rifle firing a $0.020 \text{ kg}$ bullet at $400 \text{ m/s}$:

$$0 = (0.020)(400) + (5.0)v_r \implies v_r = -\frac{8.0}{5.0} = -1.6 \text{ m/s}.$$

![Before: rifle and bullet at rest, p_total = 0. After: bullet (4 g) at 800 m/s; rifle (3.2 kg) recoils at 1 m/s. Same magnitude of momentum, opposite directions, very different speeds because mass ratio = 800.](../images/08-linear-momentum-and-collisions-fig-03.png)
*Figure 8.3 — Rifle Recoil — Equal and Opposite Momentum, Mass Ratio Sets the Speeds*

The rifle recoils at $1.6 \text{ m/s}$ backward. The bullet carries $8.0 \text{ kg·m/s}$ of forward momentum; the rifle carries $8.0 \text{ kg·m/s}$ of backward momentum. The total is zero.

![Cross-section of a turbojet on its test stand: air intake (left), compressor, combustor, turbine, exhaust nozzle (right). Air mass flow ṁ enters at v_in and leaves at v_exhaust; thrust = ṁ (v_exhaust − v_in). Test stand...](../images/08-linear-momentum-and-collisions-fig-01.png)
*Figure 8.1 — GE J47 Turbojet on Test Stand — Thrust as Momentum Exchange*

A rocket is just this, continuously. Instead of one bullet fired once, the rocket fires a continuous stream of exhaust backward. Each bit of exhaust carries backward momentum; the rocket accumulates forward momentum at the same rate. The surrounding medium is irrelevant — there is no wall to push against, no air to push against. The only thing that matters is the exhaust velocity and the rate at which exhaust mass is ejected. This works in air, it works in vacuum, it works anywhere.

<!-- → [FIGURE: Split diagram. Left: rifle recoil — bullet goes right with momentum +mv, rifle goes left with momentum −mv, total = 0. Right: rocket in space — exhaust goes left continuously, rocket goes right continuously. Both labeled: "conservation of momentum, total = 0 throughout." Caption: Recoil and rocket thrust are the same physics. You don't need a wall to push against. You need mass going backward.] -->

![Plot of achievable Δv (km/s) versus initial-to-final mass ratio (log scale) for v_exhaust = 4.5 km/s (typical chemical). Δv = v_e ln(m₀/m_f). Marked: LEO needs 9.4 km/s ⇒ ratio 8.1; Mars transfer needs 12 km/s ⇒ ratio 14. Why...](../images/08-linear-momentum-and-collisions-fig-05.png)
*Figure 8.5 — Tsiolkovsky Rocket Equation — Δv = v_e · ln(m₀ / m_f)*

The quantitative result for a rocket that burns all its fuel — known as the Tsiolkovsky rocket equation — is:

$$\Delta v = v_e \ln\!\left(\frac{m_0}{m_f}\right),$$

where $v_e$ is the exhaust speed relative to the rocket, $m_0$ is the initial mass (full of fuel), and $m_f$ is the final mass (empty). The logarithm means that to double $\Delta v$, you need to square the mass ratio — which is why spacecraft staging (dropping empty fuel tanks) is not an engineering convenience but a physical necessity. A rocket that tried to reach orbit as a single stage would need a mass ratio so large as to be structurally impossible with existing materials.

<!-- → [CHART: Plot of Δv vs. mass ratio m₀/mf for three exhaust velocities: v_e = 2,500 m/s (solid propellant), 3,000 m/s (liquid), 4,500 m/s (hydrogen/oxygen). X-axis: mass ratio 1 to 20. Y-axis: Δv in km/s. Horizontal dashed line at Δv ≈ 9.4 km/s labeled "orbital velocity requirement." Caption: The Tsiolkovsky equation on a linear scale. To reach orbit (~9.4 km/s), a single-stage liquid rocket needs a mass ratio of about 22:1 — 95% of the launch mass must be fuel. Staging breaks the problem into smaller, achievable mass ratios.] -->

---

## Collisions: elastic and inelastic

Momentum is conserved in all collisions in isolated systems. But kinetic energy is a different story.

In an **elastic collision**, kinetic energy is also conserved — nothing is lost to heat, sound, or permanent deformation. The equations are:

$$m_1 v_{1i} + m_2 v_{2i} = m_1 v_{1f} + m_2 v_{2f},$$
$$\tfrac{1}{2}m_1 v_{1i}^2 + \tfrac{1}{2}m_2 v_{2i}^2 = \tfrac{1}{2}m_1 v_{1f}^2 + \tfrac{1}{2}m_2 v_{2f}^2.$$

Two equations, two unknowns. The algebra is manageable and yields, for object 1 hitting stationary object 2:

$$v_{1f} = \frac{m_1 - m_2}{m_1 + m_2}\,v_{1i}, \qquad v_{2f} = \frac{2m_1}{m_1 + m_2}\,v_{1i}.$$

For equal masses: $v_{1f} = 0$, $v_{2f} = v_{1i}$. Object 1 stops dead; object 2 moves off at object 1's original speed. If you've watched billiards — a cue ball hitting another ball squarely — you've seen this. The cue ball stops, the target ball rolls. This is also what Newton's cradle demonstrates with its clicking balls: raise one, release it, only the far ball swings out. Equal masses, elastic collision, complete velocity transfer.

<!-- → [FIGURE: Three snapshots of equal-mass elastic collision. Before: ball 1 moving right, ball 2 stationary. During: contact. After: ball 1 stationary, ball 2 moving right with original speed. Caption: In an elastic head-on collision between equal masses, the moving object stops and the stationary object takes off at the original speed. Newton's cradle is a repeated demonstration of this result.] -->

For unequal masses, the results are less symmetric but equally clean. A very heavy object ($m_1 \gg m_2$) barely changes speed when it hits a light stationary one — the heavy object continues almost unchanged, the light object is launched at twice the original speed: $v_{2f} \approx 2v_{1i}$. A very light object hitting a very heavy stationary one bounces back at nearly its original speed, and the heavy object barely moves. Imagine rolling a marble into a bowling ball.

<!-- → [TABLE: Elastic collision outcomes for limiting mass ratios. Columns: case, v_1f formula, v_2f formula, qualitative description. Rows: equal masses (m1=m2), heavy hits light (m1≫m2), light hits heavy (m1≪m2). Caption: The elastic collision formulas have three illuminating special cases. The equal-mass case is what Newton's cradle and billiards demonstrate. The limiting cases explain why a bat barely slows when it hits a ball, and why a ball bounces off a wall.] -->

In an **inelastic collision**, kinetic energy is not conserved — some goes into deformation, heat, sound. Momentum is still conserved. The simplest case is **perfectly inelastic**: the objects stick together and move as one.

$$m_1 v_{1i} + m_2 v_{2i} = (m_1 + m_2)v_f.$$

One equation, one unknown. Clean, but note: kinetic energy loss can be substantial.

Real elastic collisions are uncommon in everyday life — billiard balls come close, but not exactly. Real inelastic collisions are everywhere: any collision that makes a sound or leaves a dent is inelastic. The categories give us two limiting cases that bracket the range of real behavior.

### A 2D collision worked out

Momentum is a vector. In two dimensions, momentum conservation applies along each axis independently — which turns every 2D collision into two 1D problems.

![Top-down view of a 2D inelastic collision. Truck (3000 kg, 20 m/s east) hits car (1000 kg, 25 m/s north). They stick (total mass 4000 kg). Final velocity = 17 m/s at 51° north of east. Kinetic energy lost to deformation.](../images/08-linear-momentum-and-collisions-fig-04.png)
*Figure 8.4 — Car + Truck at a 90° Intersection — Vector Momentum Conservation*

A $1{,}000 \text{ kg}$ car traveling east at $20 \text{ m/s}$ collides with a $1{,}500 \text{ kg}$ truck traveling north at $15 \text{ m/s}$. They stick together — perfectly inelastic.

Take $x$ east, $y$ north. Initial momenta:

- Car: $p_{x} = 20{,}000 \text{ kg·m/s}$, $p_{y} = 0$.
- Truck: $p_{x} = 0$, $p_{y} = 22{,}500 \text{ kg·m/s}$.

After collision, combined mass $2{,}500 \text{ kg}$:

$$v_x = \frac{20{,}000}{2{,}500} = 8.0 \text{ m/s}, \qquad v_y = \frac{22{,}500}{2{,}500} = 9.0 \text{ m/s}.$$

Magnitude: $v = \sqrt{8.0^2 + 9.0^2} \approx 12.0 \text{ m/s}$. Direction: $\theta = \tan^{-1}(9.0/8.0) \approx 48°$ north of east.

Energy check: initial KE = $\tfrac{1}{2}(1000)(20)^2 + \tfrac{1}{2}(1500)(15)^2 = 368{,}750 \text{ J}$. Final KE = $\tfrac{1}{2}(2500)(12)^2 = 180{,}000 \text{ J}$. Energy lost: about $189{,}000 \text{ J}$ — roughly half. That energy went into crushing metal, generating sound, and producing heat. It's gone from the kinetic account. The momentum account balanced exactly.

<!-- → [FIGURE: Top-down view of car-truck collision. Car arrow pointing east (20 m/s). Truck arrow pointing north (15 m/s). Resultant arrow after collision pointing ~48° north of east (12.0 m/s). Momentum vectors shown as parallelogram. Caption: Conservation of momentum in 2D: treat east and north components independently. The wreckage moves in the direction of the total momentum vector.] -->

---

## Energy and momentum together

These two conservation laws — energy from Chapter 7, momentum from this chapter — are the two-equation system that solves most collision problems.

For any 1D elastic collision: two unknowns (two final velocities), two equations (momentum, kinetic energy). Closed form. The solutions above.

For a perfectly inelastic collision in 1D: one unknown (one final velocity), one equation (momentum). The energy equation becomes a check — it tells you how much was lost, not how much you needed.

For 2D elastic: four unknowns (two speeds, two angles), two momentum equations (one per axis) plus one energy equation — three equations, four unknowns. You need one more piece of information, often one of the angles, from experiment or geometry.

The pattern: momentum gives you one vector equation per dimension; energy gives you one scalar equation; together they close most problems. The cases where they don't close — because kinetic energy was lost and you don't know how much — require additional physical information about the specific inelastic process. Conservation laws are powerful but not omnipotent; they constrain without fully determining when dissipation is involved.

<!-- → [TABLE: Summary of collision types. Columns: collision type, momentum conserved, kinetic energy conserved, number of equations, when to use. Rows: elastic (yes, yes, 2 eqs for 2 unknowns, billiards and atomic collisions), perfectly inelastic (yes, no, 1 eq, objects stick together), inelastic (yes, no, 1 eq + need energy loss, everything in between). Caption: The type of collision determines which equations you have. Momentum conservation always applies in isolated systems; kinetic energy conservation applies only in elastic collisions.] -->

---

## The scale of it

Momentum conservation covers an extraordinary range. A $0.057 \text{ kg}$ tennis ball at $55 \text{ m/s}$: momentum $3.1 \text{ kg·m/s}$. A $1{,}500 \text{ kg}$ car at $30 \text{ m/s}$: momentum $45{,}000 \text{ kg·m/s}$. A $2.9 \times 10^6 \text{ kg}$ Saturn V rocket at liftoff, accelerating at full thrust: momentum growing at a rate of $\sim 33 \times 10^6 \text{ N}$ of thrust. An electron in the Large Hadron Collider: momentum $\sim 10^{-18} \text{ kg·m/s}$. Across roughly 30 orders of magnitude, the same bookkeeping rule holds: in isolated systems, $\mathbf{p}_{\text{total}}$ does not change.

The LHC case is worth pausing on. Particle physicists discover new particles — the Higgs boson, the W and Z bosons, the top quark — not by seeing the particles directly, but by measuring the momenta of everything they can see after a collision and finding a deficit. The missing momentum is attributed to the undetected particle. The neutrino was proposed this way in 1930 by Wolfgang Pauli, years before anyone detected it: the electron in beta decay was coming out with the wrong momentum, and momentum had to go somewhere. The neutrino was Pauli's solution — a particle that carried away the missing momentum invisibly. Two decades later, it was detected. The conservation law was right; the particle was real.

<!-- → [INFOGRAPHIC: Timeline of neutrino discovery via momentum conservation. Three panels: (1) 1914 — beta decay observed, electron momentum doesn't balance; (2) 1930 — Pauli proposes the neutrino to save momentum conservation; (3) 1956 — Cowan and Reines detect the neutrino experimentally. Caption: The neutrino was predicted from a momentum deficit 26 years before it was detected. Conservation laws don't just describe what happens — they can predict what must exist.] -->

---

## Exercises

### Warm-up

**8.1** *(LO 1)* A $2.0 \text{ kg}$ ball moves at $5.0 \text{ m/s}$. (a) What is its momentum? (b) What is its kinetic energy?

**8.2** *(LO 1)* A $0.15 \text{ kg}$ baseball is thrown at $40 \text{ m/s}$, then reversed to $-40 \text{ m/s}$ by the bat in $1.5 \text{ ms}$. What is the average force on the ball?

**8.3** *(LO 2)* A $50 \text{ kg}$ ice skater on frictionless ice throws a $5.0 \text{ kg}$ ball at $10 \text{ m/s}$. What is her recoil velocity?

**8.4** *(LO 4)* A $1{,}500 \text{ kg}$ car at $20 \text{ m/s}$ collides with and sticks to a stationary $1{,}500 \text{ kg}$ car. What is their combined post-collision velocity?

### Application

**8.5** *(LO 3)* A $0.50 \text{ kg}$ ball at $4.0 \text{ m/s}$ collides elastically with a stationary $0.50 \text{ kg}$ ball. Find both velocities after.

**8.6** *(LO 3)* A $2.0 \text{ kg}$ ball at $3.0 \text{ m/s}$ collides elastically with a stationary $1.0 \text{ kg}$ ball. Find both velocities after using the elastic-collision formulas.

**8.7** *(LO 5)* A $4 \text{ kg}$ object at $5 \text{ m/s}$ east collides with and sticks to a $3 \text{ kg}$ object at $4 \text{ m/s}$ north. Find the combined velocity (magnitude and direction).

**8.8** *(LO 6)* A $0.005 \text{ kg}$ bullet at $300 \text{ m/s}$ is fired from a $4.0 \text{ kg}$ rifle. (a) Rifle recoil velocity? (b) If a $70 \text{ kg}$ shooter absorbs the recoil over $0.10 \text{ s}$, what average force does the shooter feel?

### Synthesis

**8.9** *(LO 1, 4)* A $30 \text{ kg}$ child running at $3.0 \text{ m/s}$ jumps onto a stationary $5.0 \text{ kg}$ skateboard. (a) Post-jump velocity? (b) Kinetic energy lost? (c) Where did it go?

**8.10** *(LO 5)* A cue ball ($0.165 \text{ kg}$) moving at $2.0 \text{ m/s}$ hits an identical stationary ball. The cue ball leaves at $30°$ above original at $1.5 \text{ m/s}$. Find the target ball's velocity (magnitude and direction).

**8.11** *(LO 1, 6)* A $50 \text{ kg}$ astronaut at rest in space throws a $5 \text{ kg}$ wrench at $10 \text{ m/s}$. (a) Her velocity afterward? (b) She is $20 \text{ m}$ from her ship — how long to drift back?

### Challenge

**8.12** *(LO 6, beyond chapter)* A rocket with initial mass $10{,}000 \text{ kg}$ (including $8{,}000 \text{ kg}$ of fuel) ejects exhaust at $3{,}000 \text{ m/s}$. Use $\Delta v = v_e \ln(m_0/m_f)$ to find the maximum velocity change if all fuel burns.

**8.13** *(beyond chapter)* A moving particle (mass $m$, velocity $v$) hits a stationary particle (mass $M$). After: two particles at angles $\theta_1$ (above) and $\theta_2$ (below) the original direction. Using momentum conservation only, set up the equations relating the four velocity magnitudes to the angles. State which quantities you'd need to measure to fully solve the system.

---

## LLM Exercise — Chapter 8: Momentum and Collisions in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A momentum-and-impulse analysis of a key collision or transfer event in your anchor phenomenon.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste 1-sentence description].

For Chapter 8, I want to apply momentum conservation and impulse to one event in my phenomenon involving a transfer of motion or a collision. Please:

1. Identify ONE collision, impact, or momentum-transfer event. Examples:
   - Bike commute: pedaling — each pedal stroke transfers momentum from leg to chain to wheels. Or a sudden stop (brake = impulse).
   - Coffee maker: water hitting the puck (impulse on the grounds).
   - Basketball: ball bouncing off the floor (impulse with the floor); ball-rim collision.
   - Marathon: footstrike — each stride is an impulse from the ground.
   - Espresso: water hitting the puck at 9 bar; water exiting the basket as a stream.

2. Set up the momentum conservation. Identify all bodies in the "system." Are external forces negligible during the relevant time?

3. Compute the momentum change and the average force from impulse: F = Δp / Δt.

4. If the event is a collision, classify it: elastic, partially inelastic, or perfectly inelastic. Compute the energy lost.

5. Sanity check with one Fermi estimate.

6. Identify which simplification (negligible external forces, point masses, instantaneous transfer) is most likely to bite.

7. One sentence on how this connects to Chapter 9 (statics) — when momentum is constant at zero, you have static equilibrium.

Save the output as logbook/chapter-08-momentum.md.
```

### What this produces

An eighth Logbook entry: a momentum analysis of one event in your phenomenon, often revealing forces that are bigger than they look.

### How to adapt this prompt

- *For phenomena without obvious collisions* (a steady-state cup of coffee): focus on impulses (the impulse to lift it, the impulse from each sip).
- *For ChatGPT or Gemini:* identical with substitutions.
- *For Claude Code:* if you have force-time data (e.g., from a smart watch's accelerometer), import and integrate to get impulse.

### Connection to previous chapters

Builds on Chapter 4 (force) — impulse is force × time. Builds on Chapter 7 (energy) — collisions can lose energy but always conserve momentum. Vector decomposition from Chapter 3 returns for 2D collisions.

### Preview of next chapter

Chapter 9 introduces statics — the special case where total momentum is zero (nothing is moving) and total angular momentum is zero (nothing is rotating). The analysis that lets us solve dynamic collisions also lets us solve static structures.

---

**Tags:** momentum, conservation, collisions, impulse, recoil
