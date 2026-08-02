# Chapter 9 — Linear Momentum and Collisions

## Suggested titles

1. **Momentum: Quantity of Motion and the Rocket Equation**
2. **Collisions and the Conservation of Momentum**
3. **Why Rocket Science Is Hard: The Tsiolkovsky Equation from Conservation**

## TL;DR

Momentum — the product of mass and velocity — is conserved in closed systems, which is more powerful than energy conservation because you don't need to know internal forces. The rocket equation $\Delta v = v_e \ln(m_0 / m_f)$ shows why getting to orbit requires exponential fuel: every kilogram you eject at 3 km/s pushes the rocket forward by a tiny but precise amount.

---

On April 14, 1970, the Apollo 13 spacecraft was 200,000 miles from Earth when one oxygen tank ruptured. The crew — James Lovell, Fred Haise, Jack Swigert — had four days to return on a crippled ship designed to carry three. The engineers at Mission Control in Houston had a single tool to save them: they pointed the service module's descent engine forward, and they burned it. The question they had to answer was always the same one: How much velocity does this burn buy us? How much fuel are we burning, and how much speed are we gaining?

That question has one answer. It is called the rocket equation. It dates to 1903, when a Russian schoolteacher named Konstantin Tsiolkovsky published a formula deriving from a single principle: conservation of momentum. The formula is $\Delta v = v_e \ln(m_0 / m_f)$. It says the change in velocity depends on the exhaust velocity and the mass ratio — initial mass divided by final mass. There is no other way to gain speed except to throw mass backward. The more mass you throw, the more speed you gain. The faster you throw it, the more speed you gain per unit mass. That's the whole machinery of spaceflight.

Conservation of momentum sounds abstract. But when you watch the Falcon 9 ascending and see the booster flip itself upright and land propulsively two minutes after launch — the first time that ever happened, December 2015 — you are watching momentum conservation at work. The rocket didn't use magic, and it didn't use a hidden thruster. It used the same principle that governs a Newton's cradle clicking back and forth on a desk, or the wreckage of two cars after a collision, or the recoil of a shotgun.

This chapter teaches you three things: momentum and how forces change it; conservation of momentum in closed systems and collisions; and the center of mass, which is where momentum conservation points. By the end of this chapter, you will understand why getting to orbit is not harder than it has to be — it is exactly as hard as physics permits it to be.

---

## Learning Objectives

By the end of this chapter, you will be able to:

- **Define** momentum as a vector quantity and recognize it as the fundamental measure of motion in a system.
- **Apply** the impulse-momentum theorem to predict how forces change motion over time.
- **Identify** closed systems and apply conservation of momentum to collisions and explosions.
- **Distinguish** between elastic and perfectly inelastic collisions and use kinetic-energy conservation to constrain collision analysis.
- **Calculate** the center of mass of a system and explain why external forces act as if all mass is concentrated there.
- **Derive** and apply the rocket equation to compute velocity changes from fuel consumption.

## Prerequisites

- Calculus I (derivatives and integrals), specifically $\int f(x) \, dx$ and basic antiderivatives.
- Vectors: components, vector addition, magnitude.
- Newton's second law in the form $\vec{F} = m\vec{a}$.
- Kinetic energy: $K = \frac{1}{2}mv^2$.

---

## Concept 1: Momentum and Impulse

### The starting point: Why mass and velocity matter separately

You have encountered kinetic energy: $K = \frac{1}{2}mv^2$. It tells you how much work is stored in a moving object. But here is a question kinetic energy cannot answer: If you are standing on frictionless ice and a 10-kg bowling ball rolls toward you at 1 m/s, and separately a 1-kg bullet flies toward you at 10 m/s, which one is harder to stop?

Both have the same kinetic energy: $K_{\text{ball}} = \frac{1}{2}(10)(1)^2 = 5$ J, and $K_{\text{bullet}} = \frac{1}{2}(1)(10)^2 = 50$ J. Wait — the bullet has ten times more kinetic energy. But that misses the point. Kinetic energy tells you about work and energy. The question you are asking is about force and time: What force, applied for how long, stops each one?

That is a different question. The answer lives in momentum.

**Momentum** is defined as
$$\vec{p} = m\vec{v}.$$

It is a vector. It points in the same direction as the velocity. Its units are kg·m/s. An object's momentum is the product of its mass and its velocity — both factors matter equally. A 10-kg ball at 1 m/s has momentum $p = 10$ kg·m/s. A 1-kg bullet at 10 m/s has the same momentum: $p = 10$ kg·m/s. This is why the bowling ball, despite having less kinetic energy, is just as hard to stop in the collision sense: to stop it, you need to change the same amount of momentum.

The deeper point: **Momentum links force and time.** If you apply a force $\vec{F}$ to an object for a time interval $\Delta t$, the change in momentum is not determined by how hard you push. It is determined by the product of force and time.

### The impulse-momentum theorem

Suppose a force $\vec{F}(t)$ acts on an object for a time interval from $t_i$ to $t_f$. The **impulse** is defined as
$$\vec{J} = \int_{t_i}^{t_f} \vec{F}(t) \, dt.$$

This integral has a geometric meaning: it is the area under the force-time curve. If the force is constant, then $\vec{J} = \vec{F} \, \Delta t$.

Now, what does impulse do? Let's find out. Start with Newton's second law:
$$\vec{F} = m\vec{a} = m \frac{d\vec{v}}{dt}.$$

Integrate both sides from $t_i$ to $t_f$:
$$\int_{t_i}^{t_f} \vec{F}(t) \, dt = \int_{t_i}^{t_f} m \frac{d\vec{v}}{dt} \, dt = m \int_{t_i}^{t_f} d\vec{v} = m(\vec{v}_f - \vec{v}_i).$$

The left side is the impulse. The right side is the change in momentum. Therefore:
$$\vec{J} = \Delta \vec{p} = m\vec{v}_f - m\vec{v}_i.$$

**The impulse-momentum theorem:** The impulse delivered to an object equals its change in momentum. This is why it matters that impulse is force times time, not force alone. A small force applied for a long time delivers the same momentum change as a large force applied for a short time.

### Worked example: The Chicxulub crater and the average impact force

Approximately 66 million years ago, an iron-nickel meteorite struck what is now the Yucatan Peninsula in Mexico. The impact was catastrophic. The crater — called Chicxulub — is roughly 180 km in diameter and 900 meters deep. It triggered the extinction event that killed the dinosaurs.

We can estimate the force of the impact using the impulse-momentum theorem. Here is the data:

- Meteorite radius: $R = 6$ km $= 6 \times 10^3$ m
- Meteorite velocity before impact: $v_i = 20$ km/s $= 2 \times 10^4$ m/s (a typical estimate)
- Density of iron-nickel: $\rho = 7970$ kg/m³
- Impact duration: $\Delta t = 10$ s (a rough estimate for the primary shock)

**Step 1: Calculate the mass.**

Assuming the meteorite is roughly spherical,
$$V = \frac{4}{3}\pi R^3 = \frac{4}{3}\pi (6 \times 10^3)^3 = 9.05 \times 10^{11} \text{ m}^3.$$

Mass:
$$m = \rho V = 7970 \times 9.05 \times 10^{11} = 7.2 \times 10^{15} \text{ kg}.$$

(For scale: that is about 1.2 billion billion tons.)

**Step 2: Calculate the impulse.**

The meteorite comes to rest (approximately), so $\vec{v}_f = 0$. Taking downward as positive:
$$\vec{J} = m(\vec{v}_f - \vec{v}_i) = 7.2 \times 10^{15} (0 - 2 \times 10^4) = -1.44 \times 10^{20} \text{ kg·m/s}.$$

The negative sign indicates the impulse is upward (opposite to the meteorite's motion).

**Step 3: Calculate the average force.**

If the impact lasted $\Delta t = 10$ s, the average force is:
$$F_{\text{ave}} = \frac{|\vec{J}|}{\Delta t} = \frac{1.44 \times 10^{20}}{10} = 1.44 \times 10^{19} \text{ N}.$$

For comparison: the weight of all humanity is roughly $7 \times 10^{11}$ N. This force is about 20 million times greater.

**What this teaches us:** The impulse-momentum theorem decouples force from time. The meteorite had an enormous velocity; stopping it required an enormous impulse. Whether that impulse was delivered by a small force over a long time, or a large force over a short time, the result is the same change in momentum. In reality, the impact force was likely far larger than our estimate (the actual collision time was probably milliseconds, not seconds), which is why the resulting crater is so deep.

### Common misconceptions

**"Momentum and kinetic energy are the same thing."**

They are not. A bowling ball at 1 m/s and a bullet at 10 m/s have the same momentum but different kinetic energies. Momentum is about force and time; kinetic energy is about work and force over distance. They answer different questions.

**"Impulse is the same as force."**

Impulse is force times time. A small force applied for a long time can deliver a large impulse. This is why airbags save lives — they increase the time over which the force acts, reducing the peak force on your body.

**"Momentum must be positive."**

Momentum is a vector. It has direction. A car moving east has positive momentum in the eastward direction; a car moving west has negative momentum in the eastward direction (or positive momentum in the westward direction). The choice of sign is up to you; what matters is consistency.

---

## Concept 2: Conservation of Momentum and Collisions

### Momentum in a closed system

Newton's third law says that when two objects interact, they exert equal and opposite forces on each other. Let two objects, with masses $m_1$ and $m_2$, collide. During the collision, let $\vec{F}_{21}$ be the force that object 2 exerts on object 1, and $\vec{F}_{12}$ be the force that object 1 exerts on object 2. Newton's third law says:
$$\vec{F}_{21} = -\vec{F}_{12}.$$

Now apply the impulse-momentum theorem to each object. For object 1:
$$\vec{J}_1 = \int \vec{F}_{21} \, dt = \Delta \vec{p}_1.$$

For object 2:
$$\vec{J}_2 = \int \vec{F}_{12} \, dt = \Delta \vec{p}_2.$$

But $\vec{F}_{21} = -\vec{F}_{12}$, so:
$$\int \vec{F}_{21} \, dt = -\int \vec{F}_{12} \, dt,$$

which means:
$$\Delta \vec{p}_1 = -\Delta \vec{p}_2.$$

The change in momentum of object 1 is equal and opposite to the change in momentum of object 2. Therefore:
$$\Delta \vec{p}_1 + \Delta \vec{p}_2 = 0.$$

The total momentum of the system does not change. This is **conservation of momentum**: In a closed system (no external forces), the total momentum before and after an interaction is the same.

Generalizing to $N$ particles:
$$\sum_{j=1}^{N} \vec{p}_j = \text{constant}.$$

**Two conditions must hold for momentum to be conserved:**

1. **The system must be closed.** No external forces act on it (or the external forces sum to zero). If friction acts, if you push on the system, if gravity acts on one object but not another, the system is not closed and momentum is not conserved.

2. **The mass of the system must be constant.** Objects can exchange momentum (like in a collision) but the total mass must stay the same. A rocket, which ejects mass, is not a closed system in this sense — we will handle it separately.

### Elastic and inelastic collisions

When two objects collide, momentum is always conserved (in a closed system). But kinetic energy may not be. There are two cases:

**Perfectly inelastic collision:** The two objects stick together. This is the maximum loss of kinetic energy consistent with momentum conservation. If the total kinetic energy after the collision is zero — both objects at rest — the loss is absolute.

**Elastic collision:** The objects bounce off each other such that kinetic energy is conserved. In an elastic collision, both momentum *and* kinetic energy are conserved.

Real collisions fall somewhere in between. A billiard ball collision is nearly elastic (most of the kinetic energy is retained). A car crash is nearly perfectly inelastic (the cars stick and most of the kinetic energy is lost as deformation, heat, and sound).

### Worked example: Perfectly inelastic collision in one dimension

Two ice hockey pucks collide on a frictionless rink. The red puck has mass $m_r = 150$ g $= 0.15$ kg and is initially at rest. The blue puck has mass $m_b = 120$ g $= 0.12$ kg and is moving at $v_{b,i} = 2.5$ m/s to the left. After the collision, the two stick together. What is their final velocity?

**Step 1: Identify the system and check closure.**

System: red puck + blue puck. External forces: friction is negligible (the rink is frictionless). The collision happens in a short time, so we can ignore gravity during the impact. The system is closed, so momentum is conserved.

**Step 2: Write conservation of momentum.**

Before collision:
$$\vec{p}_i = m_b \vec{v}_{b,i} + m_r \vec{v}_{r,i} = 0.12 \times (-2.5) + 0.15 \times 0 = -0.30 \text{ kg·m/s}.$$

(Taking leftward as negative.)

After collision, the two pucks move together with velocity $\vec{v}_f$:
$$\vec{p}_f = (m_b + m_r) \vec{v}_f = 0.27 \vec{v}_f.$$

**Step 3: Apply conservation.**

$$\vec{p}_i = \vec{p}_f$$
$$-0.30 = 0.27 \vec{v}_f$$
$$\vec{v}_f = -1.11 \text{ m/s}.$$

The combined puck moves to the left at 1.11 m/s. (The fact that it is slower than the blue puck's original speed illustrates the loss of kinetic energy.)

**Check:** Before collision, $K_i = \frac{1}{2}(0.12)(2.5)^2 = 0.375$ J. After collision, $K_f = \frac{1}{2}(0.27)(1.11)^2 = 0.166$ J. We lost 0.209 J — about 56% of the initial kinetic energy. This is typical for a perfectly inelastic collision.

### Worked example: Elastic collision in one dimension

Now suppose the collision between the two pucks is perfectly elastic. The blue puck, moving at 2.5 m/s, collides with the red puck at rest. What are the final velocities?

For an elastic collision, we have two equations: conservation of momentum and conservation of kinetic energy.

**Momentum:**
$$m_b v_{b,i} = m_b v_{b,f} + m_r v_{r,f}$$
$$0.12 \times 2.5 = 0.12 \times v_{b,f} + 0.15 \times v_{r,f}$$
$$0.30 = 0.12 v_{b,f} + 0.15 v_{r,f} \quad \text{...(1)}$$

**Kinetic energy:**
$$\frac{1}{2} m_b v_{b,i}^2 = \frac{1}{2} m_b v_{b,f}^2 + \frac{1}{2} m_r v_{r,f}^2$$
$$0.12 \times (2.5)^2 = 0.12 v_{b,f}^2 + 0.15 v_{r,f}^2$$
$$0.75 = 0.12 v_{b,f}^2 + 0.15 v_{r,f}^2 \quad \text{...(2)}$$

From equation (1):
$$v_{b,f} = \frac{0.30 - 0.15 v_{r,f}}{0.12} = 2.5 - 1.25 v_{r,f}.$$

Substitute into equation (2):
$$0.75 = 0.12 (2.5 - 1.25 v_{r,f})^2 + 0.15 v_{r,f}^2.$$

Expand:
$$0.75 = 0.12 (6.25 - 6.25 v_{r,f} + 1.5625 v_{r,f}^2) + 0.15 v_{r,f}^2$$
$$0.75 = 0.75 - 0.75 v_{r,f} + 0.1875 v_{r,f}^2 + 0.15 v_{r,f}^2$$
$$0 = -0.75 v_{r,f} + 0.3375 v_{r,f}^2$$
$$0 = v_{r,f} (-0.75 + 0.3375 v_{r,f}).$$

Solutions: $v_{r,f} = 0$ (trivial — no collision) or $v_{r,f} = \frac{0.75}{0.3375} = 2.22$ m/s.

Using $v_{b,f} = 2.5 - 1.25(2.22) = 0.22$ m/s.

**Result:** The blue puck slows to 0.22 m/s and the red puck speeds up to 2.22 m/s. The red puck, being heavier, gains less speed than the blue puck loses. Check kinetic energy: $K_f = \frac{1}{2}(0.12)(0.22)^2 + \frac{1}{2}(0.15)(2.22)^2 = 0.00291 + 0.370 = 0.373$ J. This is approximately 0.375 J — the slight discrepancy is rounding. Kinetic energy is conserved.

### Common misconceptions

**"All collisions conserve energy."**

No. Momentum is always conserved in a closed system. Energy is conserved *overall* (it is just converted to other forms like heat and sound), but mechanical energy — kinetic energy — is only conserved in elastic collisions. Most real collisions are inelastic.

**"The velocity of the center of mass changes during a collision."**

The velocity of the center of mass depends only on the total momentum of the system, which is conserved. If no external forces act, the center of mass moves at constant velocity before, during, and after the collision. (We will develop this further in the next concept.)

---

## Concept 3: Center of Mass and Rocket Propulsion

### Defining the center of mass

An extended object is made of many particles. When you push on it, you don't push on every particle equally. But there is one special point where, if you could push on it, the object would accelerate as a rigid body (without rotating). This point is the **center of mass**.

For a system of $N$ particles with masses $m_j$ and positions $\vec{r}_j$, the center of mass is located at:
$$\vec{r}_{\text{CM}} = \frac{1}{M} \sum_{j=1}^{N} m_j \vec{r}_j,$$

where $M = \sum_{j=1}^{N} m_j$ is the total mass. This is a weighted average of positions, weighted by mass.

The velocity of the center of mass is:
$$\vec{v}_{\text{CM}} = \frac{1}{M} \sum_{j=1}^{N} m_j \vec{v}_j = \frac{\vec{p}_{\text{total}}}{M}.$$

The total momentum of the system is:
$$\vec{p}_{\text{total}} = M \vec{v}_{\text{CM}}.$$

This is a crucial point: **The total momentum of a system is the total mass times the velocity of the center of mass.** If momentum is conserved, the center of mass moves at constant velocity.

### Worked example: Center of mass of a barbell

A barbell consists of two 25-kg weights connected by a 2-meter bar of negligible mass. The left weight is at position $x = 0$ m and the right weight is at $x = 2$ m. Where is the center of mass?

$$x_{\text{CM}} = \frac{m_1 x_1 + m_2 x_2}{m_1 + m_2} = \frac{25 \times 0 + 25 \times 2}{25 + 25} = \frac{50}{50} = 1 \text{ m}.$$

The center of mass is at the midpoint. If the bar is unequal — say one end has a 30-kg weight and the other a 20-kg weight — then:

$$x_{\text{CM}} = \frac{30 \times 0 + 20 \times 2}{30 + 20} = \frac{40}{50} = 0.8 \text{ m}.$$

The center of mass shifts toward the heavier weight.

### The rocket equation: Propulsion through momentum conservation

A rocket works by ejecting mass backward. As the rocket ejects mass (exhaust), the exhaust momentum backward increases, which by conservation of momentum pushes the rocket forward. Let's derive the rocket equation from first principles.

Consider a rocket of initial mass $M_0$ moving with velocity $v$ (in the lab frame). In a small time $dt$, the rocket ejects a small mass $dm$ (so the rocket's mass decreases by $dm$). The exhaust is ejected at speed $v_e$ *relative to the rocket*. In the lab frame, the exhaust has velocity $v - v_e$ (moving backward at speed $v_e$ while the rocket moves forward at speed $v$).

The momentum before ejection is:
$$p_i = M_0 v.$$

After ejection, the rocket has mass $M = M_0 - dm$ and velocity $v + dv$. The ejected mass $dm$ has velocity $v - v_e$ in the lab frame. The total momentum after is:
$$p_f = (M_0 - dm)(v + dv) + dm(v - v_e).$$

By conservation of momentum:
$$M_0 v = (M_0 - dm)(v + dv) + dm(v - v_e).$$

Expand the right side:
$$M_0 v = M_0 v + M_0 dv - dm \cdot v - dm \cdot dv + dm \cdot v - dm \cdot v_e.$$

Simplify (the $M_0 v$ and $dm \cdot v$ terms cancel):
$$0 = M_0 dv - dm \cdot dv - dm \cdot v_e.$$

The term $dm \cdot dv$ is the product of two infinitesimals, which is negligible:
$$0 = M_0 dv - dm \cdot v_e$$
$$M_0 dv = v_e \, dm.$$

Rearrange:
$$dv = \frac{v_e}{M_0} dm.$$

But wait: $M_0$ changes as the rocket burns fuel. Let $m$ be the instantaneous mass of the rocket. Then $dm < 0$ (the mass decreases), and:
$$dv = -v_e \frac{dm}{m}.$$

(The negative sign accounts for the fact that losing mass means $dm < 0$.)

Integrate from initial mass $m_0$ to final mass $m_f$:
$$\int_{v_i}^{v_f} dv = -v_e \int_{m_0}^{m_f} \frac{dm}{m}$$
$$v_f - v_i = -v_e [\ln(m_f) - \ln(m_0)]$$
$$\Delta v = v_e \ln \left( \frac{m_0}{m_f} \right).$$

This is the **Tsiolkovsky rocket equation**. The change in velocity depends on the exhaust velocity and the mass ratio.

### Worked example: The Saturn V and getting to orbit

The Saturn V, which launched the Apollo missions to the Moon, had three stages. We'll consider just the first stage.

- Initial mass: $m_0 = 2.29 \times 10^6$ kg (mostly fuel)
- Final mass: $m_f = 0.13 \times 10^6$ kg (the stage itself plus upper stages)
- Mass ratio: $\frac{m_0}{m_f} = \frac{2.29}{0.13} = 17.6$
- Exhaust velocity: $v_e = 2.6$ km/s $= 2600$ m/s (typical for LOX/kerosene rockets)

The change in velocity delivered by the first stage:
$$\Delta v = v_e \ln \left( \frac{m_0}{m_f} \right) = 2600 \ln(17.6) = 2600 \times 2.87 = 7460 \text{ m/s} \approx 7.5 \text{ km/s}.$$

Orbital velocity at Earth's surface (ignoring atmosphere) is about 7.8 km/s. The first stage alone gets you most of the way. The second and third stages add more $\Delta v$, and after accounting for gravity and drag, you reach orbit.

**Why this matters:** Notice the logarithm. To double your $\Delta v$, you don't double your fuel. You need to square your mass ratio. If you want $\Delta v = 14.9$ km/s (to get to escape velocity), you need:
$$14,900 = 2600 \ln \left( \frac{m_0}{m_f} \right)$$
$$\ln \left( \frac{m_0}{m_f} \right) = 5.73$$
$$\frac{m_0}{m_f} = e^{5.73} = 305.$$

You need 305 times your final mass in fuel. A small rocket can have a mass ratio of 10 or 15 and get into low Earth orbit. Getting to the Moon, Mars, or beyond requires mass ratios of 50, 100, or more. This is why big rockets are so much bigger than their payload.

### Common misconceptions

**"The center of mass is always at the geometric center."**

Only if the mass is uniformly distributed. For an unequal barbell, the center of mass is closer to the heavier end. For a baseball bat, the center of mass is closer to the thicker end, not the midpoint.

**"The rocket equation says the rocket can always reach any velocity."**

No. As the mass ratio approaches infinity, the $\Delta v$ approaches infinity. But there is a practical limit: you can only pack so much fuel into a structure. At some point the rocket's own mass becomes the limiting factor.

**"Momentum and impulse are the same."**

Momentum is the state of motion: $\vec{p} = m\vec{v}$. Impulse is the change in momentum: $\vec{J} = \Delta \vec{p}$. They have the same units but different meanings.

---

## Integration and Synthesis

You began this chapter with the question: Why is rocket science hard? You now have the answer.

Momentum is conserved in closed systems. A rocket in space, with its engines firing, is a closed system. As the rocket ejects mass backward, momentum conservation says the rocket must move forward. The relationship between how much mass you eject, how fast you eject it, and how much velocity you gain is given by the rocket equation: $\Delta v = v_e \ln(m_0 / m_f)$.

The logarithm is the key insight. To reach orbital velocity (about 7.8 km/s from rest), a rocket with an exhaust velocity of 2.6 km/s needs a mass ratio of $e^{7800/2600} \approx 16.5$. It must carry 16 times its final mass in fuel. This is not excessive; it is exact. Physics sets the constraint, and engineering builds the structure that satisfies it.

Momentum conservation also explains collisions. When two cars crash, momentum is conserved, but kinetic energy is not (it is converted to deformation, heat, sound). An accident investigator can work backward from the skid marks on the road to infer the speeds of the cars before collision using the work-energy theorem and momentum conservation together — neither principle alone is sufficient.

The center of mass is the lens through which to see extended objects. When a force acts on a system and the system's total momentum is conserved, the center of mass moves at constant velocity. This is why a cat always lands on its feet even when it is dropped upside down: its center of mass moves at constant velocity (or zero velocity if released from rest), and the cat's body rotates around its center of mass.

Four principles, then, hold this chapter together: impulse-momentum (forces change momentum over time), conservation of momentum (closed systems preserve total momentum), elastic vs. inelastic collisions (kinetic energy may or may not be conserved), and the rocket equation (momentum conservation quantifies how velocity changes when mass is ejected).

---

## Graduated Exercises

### Warm-up (conceptual)

1. **Momentum vs. kinetic energy.** A 1000-kg car and a 1-kg book both have kinetic energy of 100 J. Which has greater momentum? Why might you care about momentum in a car crash, but kinetic energy in a falling book?

2. **Impulse and airbags.** Explain, using the impulse-momentum theorem, why an airbag reduces injuries in a car crash. Does the airbag reduce the change in momentum? Does it reduce the peak force?

3. **Closed systems.** A hockey puck slides on ice and is hit by a stick. Is the system (puck + stick) closed during the impact? Why or why not? Is the system closed immediately after the impact, before friction acts?

### Application (quantitative)

4. **Collision on a frictionless surface.** Two blocks collide head-on on a frictionless table. Block A has mass 2 kg and velocity 3 m/s to the right. Block B has mass 3 kg and velocity 2 m/s to the left. They stick together. What is the velocity and direction of the combined block?

5. **Elastic collision.** A 4-kg block moving at 5 m/s collides elastically with a 2-kg block at rest. Find the final velocities of both blocks. (Hint: Use conservation of momentum and energy.)

6. **Rocket problem.** A 1000-kg spacecraft is at rest in space. It ejects 100 kg of exhaust at a relative velocity of 3000 m/s. What is the final velocity of the spacecraft?

### Synthesis (conceptual and quantitative)

7. **Two-dimensional collision.** A car of mass 1500 kg moving north at 10 m/s collides with a truck of mass 2500 kg moving east at 8 m/s. Immediately after the collision, they are locked together. What is the magnitude and direction of the velocity of the combined wreckage?

8. **Center of mass and motion.** Three balls are arranged on a frictionless surface: a 1-kg ball at $x = 0$ m, a 2-kg ball at $x = 1$ m, and a 3-kg ball at $x = 2$ m. The balls are initially at rest. A force of 10 N is applied to the 1-kg ball in the positive $x$-direction. (Assume the balls do not interact with each other; they are not connected.) Describe the motion of the center of mass. How does this relate to conservation of momentum?

9. **The rocket equation and staging.** A single-stage rocket has a mass ratio of 10 and an exhaust velocity of 4000 m/s. A two-stage rocket has two identical stages, each with a mass ratio of 10 and the same exhaust velocity. Which reaches a higher velocity? By how much? Why do real rockets use multiple stages?

---

## Chapter Summary

- **Momentum** is the product of mass and velocity, a vector quantity with units kg·m/s.
- **The impulse-momentum theorem** relates the impulse (force integrated over time) to the change in momentum: $\vec{J} = \Delta \vec{p}$.
- **Conservation of momentum** holds in closed systems: $\sum \vec{p} = \text{constant}$.
- **Elastic collisions** conserve both momentum and kinetic energy; **inelastic collisions** conserve momentum but not kinetic energy.
- **The center of mass** is the weighted-average position of all particles in a system; its velocity is the total momentum divided by total mass.
- **The rocket equation**, $\Delta v = v_e \ln(m_0 / m_f)$, gives the velocity change from fuel consumption and is a direct consequence of momentum conservation.
- **Etymology:** *Momentum* from Latin *movimentum*, "movement." *Impulse* from Latin *impellere*, "to drive or push." *Collision* from Latin *collidere*, "to strike together."

---

## What Would Change My Mind

If we discovered that momentum is not conserved in some regime — say, at extremely high energies or in quantum systems — it would force a reconsideration of the rocket equation. (In fact, at the quantum level, momentum is still conserved, but the concept of a particle's trajectory becomes ill-defined. The rocket equation, applied to macroscopic objects, remains valid.)

## Still Puzzling

The deep reason *why* momentum is conserved is related to the translational symmetry of space: the laws of physics are the same at every location. By Noether's theorem (a result from 1918), every continuous symmetry in physics corresponds to a conserved quantity. Translational symmetry corresponds to momentum conservation. This is satisfying intellectually, but it pushes the question back: Why is space translationally symmetric? That remains open.

---

## Discoverability Tags

momentum, impulse, collisions, conservation laws, rocket equation, center of mass, Tsiolkovsky, closed systems, elastic vs inelastic, vector quantities



---

## LLM Exercise — Chapter 10: Collisions and the Rocket Equation

**Project:** *Physics Simulation Toolkit*.

**What you're building this chapter:** Momentum tracking, collision simulations (elastic and inelastic), and the rocket equation derived from first principles by simulating fuel ejection.

**Tool:** Claude Code.

**The prompt:**

```
Chapter 10 task in the physics-simulation-toolkit. The chapter
introduced momentum, impulse, and the rocket equation. Add the
momentum bookkeeping and verify the canonical collision results.

In `chapters/ch10_momentum/`:

1. `simulations.py`:
   - `momentum(body)` — $\vec{p} = m\vec{v}$.
   - `total_momentum(system)` — sum over all bodies.
   - `center_of_mass(system)` — $\vec{r}_{\text{cm}} = \sum m_i\vec{r}_i / \sum m_i$.
   - `elastic_collision_1d(m1, v1, m2, v2)` — analytical post-collision
     velocities; verify $\vec{p}$ and $K$ are both conserved.
   - `inelastic_collision_1d(m1, v1, m2, v2)` — perfectly inelastic;
     momentum conserved, kinetic energy *not* conserved.
   - `coefficient_of_restitution(m1, v1, m2, v2, e)` — general 1D
     collision with restitution coefficient e (e=1 elastic, e=0
     perfectly inelastic, 0<e<1 partial).
   - `rocket_simulation(m_initial, m_fuel, exhaust_velocity, burn_rate)`
     — simulate a rocket by ejecting infinitesimal fuel mass over time,
     integrating the body's velocity from the ejected momentum.

2. `test_simulations.py`:
   - 1D elastic head-on: equal masses swap velocities. Verify.
   - 1D elastic with mass ratio: heavy stationary mass + light
     incoming mass → light mass bounces back, heavy mass barely
     moves. Verify the analytical limits.
   - 1D inelastic: two equal masses, one moving — after collision they
     move at half the initial velocity. Verify.
   - Tsiolkovsky rocket equation: $\Delta v = v_{\text{exhaust}}
     \ln(m_0/m_f)$. Run the rocket simulation and verify the final
     velocity matches the analytical Tsiolkovsky equation to within
     numerical precision.

3. `benchmarks.py` — for the rocket, sweep exhaust velocities (1000
   m/s, 4000 m/s, 10000 m/s) and mass ratios. Plot delta-v achieved
   vs. mass-ratio for each exhaust velocity. The logarithmic
   relationship should be empirically visible. Compare to real
   rocket engines: Falcon 9's Merlin (~3000 m/s) versus a chemical-
   ion hybrid (~30000 m/s) — what mass ratio would each need for
   delta-v of 10 km/s?

4. `README.md` — decision cards. "Surprising findings": the rocket-
   equation result is one of the most consequential equations in
   engineering — it's why getting to orbit takes 90% fuel by mass.
   Quote your numerical agreement with Tsiolkovsky.

Commit as `ch10: momentum, collisions, and the rocket equation
verified by simulation`.
```

**What this produces:** Collision simulations across the elastic/inelastic spectrum, a numerical derivation of the Tsiolkovsky rocket equation, and an exploration of mass-ratio implications.

**How to adapt this prompt:**

- *For your own project:* Multi-stage rockets are an extension — each stage drops dry mass and the next stage's Tsiolkovsky kicks in. Worth implementing if your project is aerospace-flavored.
- *For ChatGPT / Gemini:* Both work for the collision math. The rocket simulation is subtle (handle the infinitesimal-mass limit carefully).
- *For Claude Code:* Native fit. Let it generate the delta-v vs. mass-ratio sweep.
- *For a Claude Project:* Not the fit.

**Connection to previous chapters:** Builds on the Ch 6 System framework and the Ch 9 energy-conservation infrastructure.

**Preview of next chapter:** Chapter 11 implements rotational dynamics — moment of inertia from the integral (over shape), rotational kinematics, and the rigid-body Newton's-second-law analogue $\sum \tau = I\alpha$.


---

##  AI Wayback Machine
The physics in this chapter didn't appear from nowhere. **Mary Sherman Morgan** was the development of *hydyne*, the rocket propellant (a UDMH-DETA blend) that gave the Jupiter-C rocket the extra delta-v to launch Explorer 1 in January 1958 — America's first satellite and the response to Sputnik — only declassified as her work in 2008 — and despite the substance of the work, the name is far less recognized than it deserves. Here's a prompt to find out more — and then make it better.

**Run this:**

```
Who was Mary Sherman Morgan, and how does their work on rocket-propellant chemistry and the engineering of high-thrust rocket fuels connect to linear momentum, the rocket equation, and propulsion engineering? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Mary Sherman Morgan"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain what specifically about hydyne (vs. the original Jupiter-C alcohol fuel) gave the extra delta-v that mattered — the rocket-equation arithmetic, the exhaust velocity, the density
- Ask: "Morgan worked in classified rocket-propellant research for North American Aviation, never received public credit during her career, and her son George had to write her biography (*Rocket Girl*, 2013) to surface her work. What was the institutional pattern that kept her invisible?"
- Add the framing: "Answer as a 2026 magazine profile pitching Morgan to readers who have heard of Wernher von Braun but not of her"

What changes? What gets better? What gets worse?
