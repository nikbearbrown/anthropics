# Chapter 12 — Angular Momentum

Three suggested titles:

1. **When Things Spin Faster: How Angular Momentum Shapes the Universe**
2. **The Spinning Universe: From Ice Skaters to Neutron Stars**
3. **Why Spinning Things Resist Being Stopped: The Power of Angular Momentum**

---

## TL;DR

Angular momentum is to rotation what linear momentum is to motion—a quantity that persists when nothing external pushes back. When no external torque acts, a spinning system cannot change its total angular momentum: an ice skater spins faster by pulling arms inward, the Earth keeps rotating, a gyroscope resists being toppled. The mathematics mirrors linear momentum perfectly, but the hidden geometry of the cross product reveals a world where what you spin about matters as much as how fast you spin.

---

## Chapter opening — The Hubble Space Telescope held steady in the void

On April 24, 1990, the Space Shuttle Discovery released the Hubble Space Telescope into orbit above the Earth's atmosphere. Inside that 11-ton barrel, looking outward at the universe, is no bracing struts, no physical anchors, no tether to anything solid. What keeps it pointed exactly at a distant galaxy while Earth rolls beneath it?

Reaction wheels.

A reaction wheel is a spinning flywheel—a disk of lead or tungsten, usually only a few inches in diameter, spinning fast. Inside the Hubble, four of these wheels spin in different directions: one along the roll axis, one along the pitch axis, one along the yaw axis, and one spare. By spinning one wheel slightly faster or slower, the spacecraft trades its angular momentum for rotation in the opposite direction. Speed up the roll wheel, the telescope's body rotates the other way by just the amount needed. The wheels never touch the telescope. No thruster fires. No propellant burns. The telescope moves because angular momentum, like a ledger, must balance.

This is not magic. It is the machinery of angular momentum made visible.

In the previous chapter, you learned that a spinning object has rotational kinetic energy, that torque causes angular acceleration, that the moment of inertia resists rotation. But you might have noticed something puzzling: a spinning ice skater can speed up without any visible force pushing on her. She pulls her arms in, contracts her radius, and suddenly her spin rate increases. No torque. No external force. Just geometry and a law of nature so fundamental it governs everything from ice rinks to neutron stars.

That law is conservation of angular momentum.

This chapter builds on what you know about rotation to introduce angular momentum—the rotational equivalent of linear momentum—and then shows what happens when you really understand what it means for a quantity to be conserved. By the end, you will be able to predict how fast a diver will spin given their body geometry, how the precession of a gyroscope works, and why the Hubble can look straight at a star without firing a thruster.

### Learning objectives

By the end of this chapter you will be able to:

- **Define** angular momentum for a particle and for a rigid body, calculate it from position, momentum, and moment of inertia, and explain what it means physically.
- **Apply** the torque-angular-momentum relation $d\vec{L}/dt = \vec{\tau}$ to find how external forces change a system's rotation.
- **Apply** conservation of angular momentum to predict the behavior of systems where no external torque acts, including collisions, systems with changing moment of inertia, and multi-body systems.
- **Derive** and apply the precession equation for gyroscopes and spinning tops, explaining why a top does not fall when spinning even though gravity pulls on it.

### Prerequisites

You need rotational kinematics and dynamics from Chapter 10: the meaning of angular velocity $\omega$, angular acceleration $\alpha$, moment of inertia $I$, torque $\tau$. You need vectors from Chapter 2, especially the cross product $\vec{A} \times \vec{B}$. You need to be comfortable taking derivatives with respect to time.

### Why this chapter matters

Angular momentum is one of the deepest conservation laws in physics. When no external torque acts, angular momentum is conserved—it does not change. This is not a rule we choose; it emerges from the symmetry of space under rotation. Physicists call this Noether's theorem: every symmetry of space and time produces a conservation law. Rotational symmetry produces conservation of angular momentum.

In engineering, this means gyroscopes can guide spacecraft without physical attachment. In astronomy, it explains why galaxies rotate and why a collapsing star spins faster. In biomechanics, it explains how divers and gymnasts execute complex maneuvers in mid-air. In planetary science, it constrains how tidal forces can transfer energy from one body to another. Master angular momentum and you have the key to understanding why rotating systems behave the way they do.

---

## Concept 1 — Angular momentum of a particle: the cross product makes it real

Consider a small stone being thrown from your hand. At the instant it leaves your fingers, it has position $\vec{r}$ measured from some fixed origin and linear momentum $\vec{p} = m\vec{v}$. Even if the stone is not spinning about that origin, we can ask: how much rotational influence does this stone carry?

The answer is the angular momentum of the particle.

**Angular momentum $\vec{L}$ (or $\vec{l}$ for a single particle) is defined as:**

$$\vec{l} = \vec{r} \times \vec{p} = \vec{r} \times m\vec{v}$$

The cross product is the key. Remember from Chapter 2 that $\vec{A} \times \vec{B}$ produces a vector perpendicular to both $\vec{A}$ and $\vec{B}$, with magnitude $AB\sin\theta$ where $\theta$ is the angle between them. The direction comes from the right-hand rule: fingers along $\vec{r}$, curl toward $\vec{p}$, thumb points in the direction of $\vec{l}$.

The magnitude is:

$$l = rp\sin\theta = rmv\sin\theta$$

This is where intuition meets mathematics. The sine of the angle is the culprit. If the particle moves directly toward or away from the origin ($\theta = 0°$ or $180°$), then $\sin\theta = 0$ and $l = 0$—the particle has no rotational influence about that point. If the particle moves perpendicular to the radius vector ($\theta = 90°$), then $\sin\theta = 1$ and the angular momentum is at maximum.

Another way to think about it: define the **lever arm** $r_\perp$ as the perpendicular distance from the origin to the line of the particle's motion. Then:

$$l = r_\perp \cdot p = r_\perp \cdot mv$$

The lever arm isolates the part of the position that actually matters for rotation.

**The torque-angular momentum relation.** Take the time derivative of $\vec{l}$:

$$\frac{d\vec{l}}{dt} = \frac{d}{dt}(\vec{r} \times \vec{p}) = \frac{d\vec{r}}{dt} \times \vec{p} + \vec{r} \times \frac{d\vec{p}}{dt}$$

The first term is $\vec{v} \times m\vec{v}$, which is zero (a vector crossed with itself is zero). The second term is $\vec{r} \times \frac{d\vec{p}}{dt} = \vec{r} \times \vec{F}$ by Newton's second law. So:

$$\frac{d\vec{l}}{dt} = \vec{\tau}$$

This is the central result. The rate of change of angular momentum equals the torque. It is the rotational version of $\frac{d\vec{p}}{dt} = \vec{F}$. Just as a force changes linear momentum, a torque changes angular momentum.

**Trade-off: coordinate dependence.** Here is the thing about angular momentum: it depends on where you put the origin. A stone moving in a straight line at constant velocity has zero angular momentum about any point on its line of motion, but enormous angular momentum about a point far from its path. This is not a flaw—it is a feature. You choose the origin based on what you want to know. In orbital mechanics, you choose the center of mass. In a spinning-top problem, you choose the pivot point. The choice matters, and you must always declare it.

**Worked example — a meteor's angular momentum about an observer.**

A meteor enters Earth's atmosphere at position $\vec{r} = 25\text{ km}\,\hat{i} + 25\text{ km}\,\hat{j}$ relative to an observer on the ground. At that instant, its velocity is $\vec{v} = -2.0\text{ km/s}\,\hat{j}$ (moving downward at an angle). Its mass is $m = 15\text{ kg}$. What is its angular momentum about the origin at the observer's location?

*Given:* $\vec{r} = (25.0 \times 10^3 \text{ m})\hat{i} + (25.0 \times 10^3 \text{ m})\hat{j}$, $\vec{v} = -(2.0 \times 10^3 \text{ m/s})\hat{j}$, $m = 15\text{ kg}$.

*Calculate momentum:* $\vec{p} = m\vec{v} = 15\text{ kg} \cdot (-(2.0 \times 10^3 \text{ m/s})\hat{j}) = -(3.0 \times 10^4 \text{ kg·m/s})\hat{j}$.

*Cross product:* $\vec{l} = \vec{r} \times \vec{p}$. Only the $\hat{i}$ component of $\vec{r}$ crossed with the $\hat{j}$ component of $\vec{p}$ survives:

$$\vec{l} = (25.0 \times 10^3 \text{ m})\hat{i} \times (-(3.0 \times 10^4 \text{ kg·m/s}))\hat{j} = (25.0 \times 10^3)(3.0 \times 10^4)\hat{k}\text{ kg·m}^2\text{/s}$$

$$\vec{l} = 7.5 \times 10^8 \text{ kg·m}^2\text{/s}\,\hat{k}$$

The magnitude is $7.5 \times 10^8$ kg·m²/s. The direction is out of the page (positive $\hat{k}$), which you can confirm by the right-hand rule: fingers point from the origin toward the first quadrant (along $\vec{r}$), curl downward (along $\vec{p}$), thumb points out of the page.

*Interpretation:* The meteor has substantial angular momentum about the observer because the observer is far from the meteor's line of motion. A different observer standing directly in the meteor's path would measure zero angular momentum.

**Common misconceptions:**

1. *"Angular momentum requires something to be spinning."* Wrong. A particle moving in a straight line has angular momentum about any point not on that line. Spin is not required; all that matters is the geometry of the path relative to the origin.

2. *"Angular momentum and linear momentum are independent."* They are independent in the sense that you can have one without the other. But they both come from the same source: the particle's state of motion. A spinning object has both.

3. *"The lever arm is always less than the radius."* The lever arm $r_\perp$ is the perpendicular distance to the line of motion. For a particle moving perpendicular to $\vec{r}$, the lever arm equals the radius. For other angles, it is smaller.

---

## Concept 2 — Angular momentum of a rigid body: the sum becomes an integral

Now extend from particles to rigid bodies. Imagine a disk rotating about a fixed axis. Every part of that disk has its own angular momentum about the axis. The total angular momentum is the sum of all the individual contributions.

For a system of discrete particles, the total angular momentum is:

$$\vec{L} = \vec{l}_1 + \vec{l}_2 + \cdots + \vec{l}_N = \sum_i \vec{l}_i$$

For a continuous rigid body rotating about a fixed axis with angular velocity $\omega$, this sum becomes an integral. Consider a small mass element $dm$ at distance $R$ from the axis, moving with tangential velocity $v = R\omega$. Its angular momentum magnitude is:

$$dl = R \cdot dm \cdot v = R \cdot dm \cdot R\omega = R^2 \omega \, dm$$

Sum all the elements:

$$L = \int R^2 \omega \, dm = \omega \int R^2 \, dm = \omega I$$

where $I = \int R^2 \, dm$ is the moment of inertia you learned in Chapter 10.

So for a rigid body rotating about a fixed axis:

$$\boxed{L = I\omega}$$

This is the rotational analogue of $p = mv$. Just as mass resists linear acceleration, moment of inertia resists angular acceleration. Just as linear momentum is mass times velocity, angular momentum is moment of inertia times angular velocity.

**The direction matters—it is a vector.** The vector $\vec{L}$ points along the axis of rotation, determined by the right-hand rule. Curl your fingers in the direction of rotation, your thumb points in the direction of $\vec{L}$.

**Trade-off: the simplicity hides the geometry.** The relation $L = I\omega$ is clean and simple for rotation about a fixed axis. But if the axis can reorient itself—if the body tumbles or precesses—then the full vector nature of angular momentum becomes essential, and the mathematics becomes richer. For now, stick to fixed axes and remember that $\vec{L}$ has a direction.

**Worked example — the angular momentum of a spinning disk.**

A uniform disk of mass $m = 2.0\text{ kg}$ and radius $r = 0.25\text{ m}$ spins at $\omega = 100\text{ rad/s}$ about a vertical axis through its center. What is its angular momentum?

*Given:* $m = 2.0\text{ kg}$, $r = 0.25\text{ m}$, $\omega = 100\text{ rad/s}$.

*Moment of inertia of a uniform disk:* $I = \frac{1}{2}mr^2 = \frac{1}{2}(2.0)(0.25)^2 = 0.0625\text{ kg·m}^2$.

*Angular momentum:* $L = I\omega = 0.0625 \times 100 = 6.25\text{ kg·m}^2\text{/s}$.

Direction: vertically upward (using the right-hand rule for counterclockwise rotation viewed from above).

**Common misconceptions:**

1. *"A heavy object has more angular momentum than a light one at the same spin rate."* Not necessarily. A light object far from the axis (large moment of inertia) can have more angular momentum than a heavy object spinning close to its axis. It is the combination of $I$ and $\omega$ that matters.

2. *"Angular momentum is proportional only to how fast something spins."* It is proportional to both how fast it spins and how its mass is distributed. The distribution (moment of inertia) is half the story.

---

## Concept 3 — Conservation of angular momentum: when torque vanishes, the spin adapts

This is where the power emerges.

**The Law of Conservation of Angular Momentum:** If no external torque acts on a system, the total angular momentum does not change.

$$\frac{d\vec{L}}{dt} = \vec{\tau}_{\text{ext}}$$

If $\vec{\tau}_{\text{ext}} = 0$, then $\frac{d\vec{L}}{dt} = 0$, which means $\vec{L} = \text{constant}$.

Why is there no external torque? In many real situations:

- Gravity acts at the center of mass, producing no torque about the center of mass.
- Internal forces (friction, collisions between parts of the system) produce no net external torque—they are internal.
- The system is isolated in space (like a spacecraft or a spinning ice skater).

When angular momentum is conserved, the system cannot simply maintain one configuration. It adapts. If the moment of inertia changes, the angular velocity must change to keep $L$ constant. This is the physical principle behind a hundred phenomena.

**The ice skater—the canonical example.**

An ice skater begins her spin with arms extended. Her moment of inertia is large—mass is far from the axis. She spins at a modest rate, say $\omega_0 = 2\text{ rev/s}$. Total angular momentum: $L = I_0 \omega_0$.

Then she pulls her arms in. Her mass is now concentrated closer to the axis. Her moment of inertia decreases to, say, $I_1 = \frac{1}{4}I_0$. No external torque acts (friction at the skates is negligible; gravity acts at the center of mass). Conservation of angular momentum says:

$$L = I_0 \omega_0 = I_1 \omega_1$$

$$I_0 \omega_0 = \frac{1}{4}I_0 \omega_1$$

$$\omega_1 = 4\omega_0 = 8\text{ rev/s}$$

She spins four times faster without any visible push. The skater did work pulling her arms in—that work comes from her muscles, not from external forces—and that work increases her rotational kinetic energy. Meanwhile, her angular momentum stayed constant. Same ledger, different configuration.

**A pulsar spins down—or does it?**

A pulsar is a neutron star, the remnant of a supernova explosion. It is roughly the mass of the Sun compressed into a sphere the size of a city. Some pulsars rotate hundreds of times per second. The Crab nebula pulsar rotates about 30 times per second, with a radius of roughly 10 km and a mass of roughly $2.8 \times 10^{30}\text{ kg}$ (about 1.4 solar masses).

These objects lose energy by radiating electromagnetic waves. As they radiate, they lose angular momentum slowly. But the loss is so gradual that at any given instant, you can treat angular momentum as approximately conserved. Detailed observations show pulsars slowing down at rates of order $10^{-15}$ rotations per second per second—barely measurable, but real. Over millions of years, the spin accumulates. The pulsar that rotates 30 times per second today rotated faster in the past.

**Trade-off: conserved but not always intuitive.** Conservation of angular momentum is ironclad, but its consequences can surprise. The fact that an ice skater spins faster by pulling arms inward violates our intuition from linear motion: you cannot make yourself move faster forward by rearranging your body. But angular momentum has no such constraint. The constraint is only that the total does not change.

**Worked example — a gymnast on the high bar.**

A gymnast dismounts from a high bar. At the moment he releases the bar, his body is fully extended, with moment of inertia $I_0 = 21.6\text{ kg·m}^2$ and rotation rate $\omega_0 = 1.0\text{ rev/s}$. As he falls, he tucks his body into a ball, reducing his moment of inertia to $I_1 = 5.4\text{ kg·m}^2$. Assume no external torque acts during the fall (gravity and air resistance act on the center of mass, not perpendicular to it, so no torque about the center of mass).

(a) What is his rotation rate while tucked?

*Conservation of angular momentum:*

$$L = I_0 \omega_0 = I_1 \omega_1$$

$$21.6 \times 1.0 = 5.4 \times \omega_1$$

$$\omega_1 = 4.0\text{ rev/s}$$

He spins four times faster.

(b) If he falls for $t = 0.5\text{ s}$ while tucked, how many rotations does he execute before hitting the ground?

At $\omega_1 = 4.0\text{ rev/s}$ for $0.5\text{ s}$:

$$N = \omega_1 \times t = 4.0 \text{ rev/s} \times 0.5\text{ s} = 2.0\text{ revolutions}$$

He completes two full rotations and lands upright.

(c) What if he lands while still fully extended?

If he were to extend again during the fall, angular momentum conservation says his rotation rate would drop back to $1.0\text{ rev/s}$. He would land rotating, but slowly—a much less stylish dismount.

**Common misconceptions:**

1. *"Conservation of angular momentum means the spin rate stays constant."* Wrong. It is the total $L$, not the rate $\omega$, that is conserved. If $I$ changes, $\omega$ must change to compensate.

2. *"Angular momentum conservation requires isolation from all forces."* No. It requires isolation from external torques only. Gravity and air resistance can act; what matters is whether they produce a net torque about the center of mass.

3. *"Once angular momentum is imparted, it cannot be changed."* True for a truly isolated system, but even tiny torques (like air resistance off-center, or friction that is not uniform) accumulate over time. In practice, angular momentum is nearly conserved, not perfectly.

---

## Concept 4 — Precession: when torque is perpendicular to spin, the axis wanders

This is the strangest phenomenon in rotational dynamics, yet it has a simple explanation.

Imagine a spinning top resting on a pivot point on a table. If the top were not spinning, gravity would pull it over immediately—the gravitational force on the top's center of mass produces a torque about the pivot that causes the top to rotate downward. But if the top spins fast enough, something unexpected happens: instead of falling, the top's axis slowly rotates about the vertical. This rotation of the spin axis is called **precession**.

**Why does it happen?** The key is that the torque is perpendicular to the angular momentum vector.

The gravitational force acts downward on the center of mass, at a horizontal distance $r$ from the pivot. The torque is:

$$\vec{\tau} = \vec{r} \times \vec{F}$$

This torque points horizontally (perpendicular to the vertical angular momentum). By the relation $d\vec{L}/dt = \vec{\tau}$, the change in angular momentum is also horizontal, in the direction of the torque. But here is the key insight: a horizontal change to the angular momentum vector means the vector tilts to the side. The tip of the angular momentum vector traces out a cone. The spin axis, which points along $\vec{L}$, traces out the same cone. This is precession.

**The precession rate.** For a top or gyroscope:

The magnitude of the torque is $\tau = mgr\sin\theta$, where $\theta$ is the angle the top makes with the vertical, $m$ is the mass, $r$ is the distance from the pivot to the center of mass, and $g$ is gravitational acceleration.

In time $dt$, the change in angular momentum is $dL = \tau \, dt = mgr\sin\theta \, dt$.

The angle through which the angular momentum vector rotates (and thus the spin axis) is:

$$d\phi = \frac{dL}{L\sin\theta} = \frac{mgr\sin\theta}{L\sin\theta}dt = \frac{mgr}{L}dt$$

The **precession angular velocity** is:

$$\omega_P = \frac{d\phi}{dt} = \frac{mgr}{L} = \frac{mgr}{I\omega}$$

This is the signature equation of precession. Notice what it says: a faster spin ($\omega$) produces slower precession. A heavier top (larger $m$) or larger distance to the center of mass produces faster precession. This matches intuition: spin the top faster and it stands more steadily.

**A concrete example—the Crab pulsar again.**

The Crab pulsar spins 30 times per second. Its magnetic field is not aligned with its spin axis. As it rotates, the magnetic field sweeps through space like a lighthouse beam. If we observe from a particular angle, we see a pulse of radiation each time the beam points at us. The pulsar is also precessing slowly—its spin axis is moving, at a rate of about $0.01$ arcseconds per century. This precession arises from the pulsar's own magnetic field exerting an internal torque (a subtly different mechanism than gravity on a top, but the principle is the same).

**Scale shift—from toy to cosmos.**

A child's top lasts seconds before friction stops it. A gyroscope on a spacecraft maintains its orientation for years. The Earth itself acts as a giant gyroscope, precessing once every 26,000 years due to gravitational torques from the Sun and Moon on Earth's equatorial bulge. The physics is the same: spin axis, torque perpendicular to the spin, slow rotation of the axis around the vertical.

**Trade-off: precession requires spin to be fast.**

The precession equation $\omega_P = \frac{mgr}{I\omega}$ contains a subtle assumption: $\omega_P \ll \omega$. That is, the precession is slow compared to the spin. If the top spins too slowly, the assumption breaks down, and more complex behavior (nutation—a wobble superimposed on the precession) appears. For this chapter, assume the spin is fast enough that precession is the dominant behavior.

**Worked example — a gyroscope in the classroom.**

A gyroscope disk has mass $m = 0.30\text{ kg}$, radius $r_{\text{disk}} = 0.05\text{ m}$, and spins at $f = 20\text{ rev/s}$. Its center of mass is $r = 0.05\text{ m}$ from the pivot. What is its precession period?

*Given:* $m = 0.30\text{ kg}$, $r = 0.05\text{ m}$, $f = 20\text{ rev/s} = 20 \times 2\pi = 125.66\text{ rad/s}$.

*Moment of inertia of the disk:* $I = \frac{1}{2}mr_{\text{disk}}^2 = \frac{1}{2}(0.30)(0.05)^2 = 3.75 \times 10^{-4}\text{ kg·m}^2$.

*Precession angular velocity:*

$$\omega_P = \frac{mgr}{I\omega} = \frac{(0.30)(9.8)(0.05)}{(3.75 \times 10^{-4})(125.66)} = \frac{0.147}{0.0471} = 3.12\text{ rad/s}$$

*Precession period:*

$$T_P = \frac{2\pi}{\omega_P} = \frac{2\pi}{3.12} = 2.0\text{ s}$$

The gyroscope completes one precession cycle every 2 seconds. Watch it in the lab and you will see the spin axis slowly circling around the vertical at this rate. The spin rate of 125.66 rad/s is much larger than the precession rate of 3.12 rad/s, confirming the assumption $\omega_P \ll \omega$ is valid.

**Common misconceptions:**

1. *"Precession means the top is falling slowly."* No. The top is not falling at all if it is precessing steadily. The gravitational torque is continuously changing the direction of the spin axis, not its magnitude.

2. *"A slower spin leads to faster precession, so slow things precess more."* That is true mathematically, but slow-spinning tops also have less kinetic energy and are more easily disrupted by friction. A truly slow-spinning top will not precess steadily; it will wobble and fall.

3. *"The precession axis is the same as the spin axis."* No. The spin axis precesses around a vertical axis. They are different axes, perpendicular to each other.

---

## Integration — the three concepts unified

Angular momentum is the rotational version of linear momentum, but it carries a hidden richness.

**For a particle:** $\vec{l} = \vec{r} \times \vec{p}$. It depends on your choice of origin. It changes when a torque acts: $d\vec{l}/dt = \vec{\tau}$.

**For a rigid body:** $\vec{L} = I\vec{\omega}$. Clean and simple for fixed-axis rotation. The vector nature determines whether the top falls or precesses.

**When no external torque acts:** $L$ is constant. The system cannot increase $L$ internally, but it can redistribute the rotation. An ice skater spins faster by pulling arms in. A neutron star spins faster as it loses energy and contracts. A diver executes three somersaults in 1.4 seconds by changing moment of inertia mid-fall.

**When torque is perpendicular to spin:** the spin axis does not change magnitude, only direction. It traces a cone at a rate given by $\omega_P = \frac{\tau}{L}$. A top precesses. A gyroscope stays pointed in the same direction despite the vehicle rotating around it. Earth's axis slowly circles the north celestial pole.

These are not three separate phenomena. They are one principle—conservation of angular momentum—viewed from different angles.

---

## Exercises

### Warm-up

**Exercise 12.1** *(LO: define and calculate.)* A particle of mass $m = 0.5\text{ kg}$ moves with velocity $\vec{v} = 3.0\text{ m/s}\,\hat{i}$ and at time $t$ is at position $\vec{r} = 4.0\text{ m}\,\hat{j}$. Calculate the angular momentum about the origin and specify its direction using the right-hand rule.

**Exercise 12.2** *(LO: rigid body angular momentum.)* A uniform cylinder of mass $m = 2.0\text{ kg}$ and radius $r = 0.10\text{ m}$ rotates about its central axis at $\omega = 50\text{ rad/s}$. Calculate its moment of inertia and angular momentum.

**Exercise 12.3** *(LO: conservation.)* An ice skater initially spins with arms extended at $\omega_0 = 3.0\text{ rev/s}$ with moment of inertia $I_0 = 4.0\text{ kg·m}^2$. She pulls her arms in, reducing her moment of inertia to $I_1 = 1.0\text{ kg·m}^2$. What is her final spin rate?

### Application

**Exercise 12.4** *(LO: torque-angular momentum relation.)* A disk of moment of inertia $I = 0.5\text{ kg·m}^2$ rotates about a fixed axis. A constant torque $\tau = 2.0\text{ N·m}$ is applied for $t = 3.0\text{ s}$. If the disk starts from rest, what is its final angular velocity and final angular momentum?

**Exercise 12.5** *(LO: conservation in collisions.)* A bullet of mass $m = 0.01\text{ kg}$ moving at $v = 500\text{ m/s}$ strikes and embeds itself at the edge of a disk (mass $M = 2.0\text{ kg}$, radius $R = 0.10\text{ m}$) that is free to rotate about its center. The disk is initially at rest. What is the angular velocity of the disk immediately after the collision?

**Exercise 12.6** *(LO: precession.)* A top has mass $m = 0.2\text{ kg}$, moment of inertia $I = 1.0 \times 10^{-4}\text{ kg·m}^2$, spin rate $\omega = 100\text{ rad/s}$, and distance from pivot to center of mass $r = 0.03\text{ m}$. Calculate its precession angular velocity.

### Synthesis

**Exercise 12.7** *(LO: conservation + changing moment of inertia.)* A diver leaves the board horizontally rotating at $0.8\text{ rev/s}$ with arms extended (moment of inertia $I_0 = 16\text{ kg·m}^2$). She tucks into a ball (moment of inertia $I_1 = 4.0\text{ kg·m}^2$) for 1.5 seconds, then extends again (moment of inertia back to $I_0$) for the final 0.5 seconds before hitting the water. How many complete rotations does she execute?

**Exercise 12.8** *(LO: angular momentum systems.)* A thin rod of mass $m = 1.0\text{ kg}$ and length $L = 1.0\text{ m}$ rotates about its center at $\omega = 10\text{ rad/s}$. A small mass $M = 0.5\text{ kg}$ is attached to one end and initially moves with the rod. The small mass is then released (ejected tangentially). Does the rod's angular velocity increase or decrease? Explain using conservation of angular momentum.

### Challenge

**Exercise 12.9** *(LO: precession of Earth.)* Earth has a moment of inertia $I \approx 8.0 \times 10^{37}\text{ kg·m}^2$ and an angular momentum $L \approx 7.1 \times 10^{33}\text{ kg·m}^2\text{/s}$. It precesses with a period of 26,000 years due to gravitational torques from the Sun and Moon. What is the average external torque?

**Exercise 12.10** *(LO: multi-body system.)* Two identical disks, each with moment of inertia $I = 1.0\text{ kg·m}^2$, are on a frictionless vertical axis. Disk A rotates at $\omega_A = 10\text{ rad/s}$ counterclockwise; disk B rotates at $\omega_B = 5\text{ rad/s}$ clockwise. They are then coupled so they rotate together. What is their final angular velocity, and what fraction of kinetic energy is lost to friction during coupling?

---

## Chapter summary

You opened this chapter watching the Hubble Space Telescope hold its gaze on a distant star using only spinning reaction wheels. You now understand why that is possible.

Angular momentum $\vec{L} = \vec{r} \times \vec{p}$ for a particle and $\vec{L} = I\omega$ for a rigid body captures how much rotational influence a moving or spinning object carries. It is not intuitive—it depends on your choice of origin, and it is tied to the cross product—but it is real, measurable, and conserved when no external torque acts.

Conservation of angular momentum is the key. When no net external torque acts, a system's total angular momentum cannot change. That means an ice skater can spin faster by rearranging her geometry. A diver can execute multiple somersaults by changing body shape mid-fall. A gyroscope can hold its orientation against all forces applied to its housing, because the spacecraft around it must conserve its own angular momentum. The Hubble can reorient without thrusting because the reaction wheels inside exchange angular momentum with the spacecraft's orientation.

Precession—the slow rotation of a spin axis when a perpendicular torque acts—explains why tops do not fall, why Earth's axis slowly points toward different stars, and why gyroscopes precess at rates predictable by $\omega_P = \frac{mgr}{I\omega}$.

The machinery is clear now. Rotation, torque, angular momentum, and conservation are all locked together. Understand one, and the others follow.

---

## Connections forward

The next chapter, on static equilibrium, asks when objects do not rotate at all. You have learned the condition: the net external torque must be zero. That is where equilibrium comes from. Chapter 13 introduces gravity as a force and develops Kepler's laws. Angular momentum, it turns out, is conserved in orbital motion. A satellite moving faster at perigee (close to Earth) than at apogee (far from Earth) is simply conserving angular momentum as its distance from Earth changes. Chapter 15, on oscillations, explores systems where angular momentum plays a subtle role—energy sloshes between rotational and translational forms. And whenever you encounter a system with symmetry, angular momentum will be lurking underneath, a conserved quantity guaranteed by the structure of space itself.

---

## What would change my mind

If someone showed that angular momentum is not conserved in an isolated system—that a top's spin changes without external torque—I would have to reconsider the symmetry foundations of physics. But 300 years of experiments, from Kepler's observations of planetary orbits to modern gyroscope navigation in spacecraft, have confirmed it without exception.

## Still puzzling

Why the cross product? Why not just $L = r \cdot p$? The answer is deep: the cross product encodes the geometry of rotation in three-dimensional space. It is not arbitrary; it is the only operation that captures how a force at one point creates rotation about another. Yet the intuition for why it has to be the cross product—why not some other combination—still deserves a longer meditation.

---

## Tags

angular-momentum, conservation-laws, rotation, gyroscopes, precession, ice-skater, torque, vector-calculus, symmetry, Hubble-Space-Telescope


---

## LLM Exercise — Chapter 12: Angular Momentum and Precession

**Project:** *Physics Simulation Toolkit*.

**What you're building this chapter:** Angular-momentum tracking, conservation verification, and a numerical simulation of gyroscopic precession from the Newton's-law-for-rotation $\vec{\tau} = d\vec{L}/dt$.

**Tool:** Claude Code.

**The prompt:**

```
Chapter 12 task in the physics-simulation-toolkit. The chapter
extended angular kinematics to 3D and introduced $\vec{L} = I\vec{\omega}$
for rigid bodies. Verify conservation and simulate precession.

In `chapters/ch12_angular_momentum/`:

1. `simulations.py`:
   - `angular_momentum_particle(body, axis_point)` — $\vec{L} = \vec{r} \times m\vec{v}$
     about a specified point.
   - `angular_momentum_rigid_body(body, inertia_tensor)` —
     $\vec{L} = I\vec{\omega}$ in the body frame; transform to lab frame.
   - `total_angular_momentum(system, axis_point)` — sum over all bodies.
   - `gyroscope_precession(spin_angular_momentum, applied_torque)` —
     numerical simulation: at each step, $d\vec{L}/dt = \vec{\tau}$
     updates the angular momentum vector, which (for a spinning gyro
     under gravity) precesses.

2. `test_simulations.py`:
   - Figure-skater spin-up: a skater pulling in arms decreases $I$;
     verify $\vec{L}$ stays constant while $\omega$ increases.
   - Particle in central-force orbit (preview Ch 14): angular
     momentum about the central body conserved.
   - Two-body collision: total angular momentum before equals total
     angular momentum after, when external torque is zero. Verify.
   - Gyroscope precession: simulate a spinning disk on a horizontal
     axle, supported at one end. Vertical gravity creates a
     horizontal torque; the angular momentum precesses horizontally.
     Compare numerical precession rate to the analytical
     $\Omega_{\text{prec}} = \tau / L = mgr/(I\omega)$.

3. `benchmarks.py` — vary the spin rate and the lever arm of the
   gyroscope. Plot precession rate vs. spin rate. The inverse
   relationship $\Omega \propto 1/\omega$ should be empirically clear.
   At what spin rate does precession become slow enough to be
   observable to the eye?

4. `README.md` — decision cards. "Surprising findings": the figure-
   skater example produces dramatic spin-up factors (typically 3-5x);
   the gyroscope precession is the "everyone-finds-it-counterintuitive"
   case — the gyro doesn't fall, it precesses, and the math says why.

Commit as `ch12: angular momentum conservation and gyroscopic
precession`.
```

**What this produces:** Angular-momentum bookkeeping, three conservation tests, a working gyroscope-precession simulation, and the precession-rate-vs-spin-rate inverse relationship verified empirically.

**How to adapt this prompt:**

- *For your own project:* The inertia tensor (Ch 11's scalar $I$ generalized to 3D) becomes important for off-axis rotation. If you want full rigid-body dynamics, this is where it lives.
- *For ChatGPT / Gemini:* Both work for the basic cases. Full inertia-tensor handling is subtle (Euler equations); verify against the standard test cases.
- *For Claude Code:* Native fit. The gyroscope precession is a visually compelling test — produce a 3D trajectory plot.
- *For a Claude Project:* Not the fit.

**Connection to previous chapters:** Uses the Ch 11 rotation framework. The Ch 9 conservation-of-energy infrastructure parallels Ch 12's conservation-of-angular-momentum.

**Preview of next chapter:** Chapter 13 implements static equilibrium — sum-of-forces and sum-of-torques solvers — and adds stress and strain calculations for elastic beams.


---

##  AI Wayback Machine
The physics in this chapter didn't appear from nowhere. **Vera Rubin** was the 1970s observations of galactic rotation curves — measuring how orbital velocity varies with distance from a galaxy's center — which showed that galaxies rotate as if they contain far more mass than visible matter accounts for, providing the strongest pre-CMB observational case for dark matter — and despite the substance of the work, the name is far less recognized than it deserves. Here's a prompt to find out more — and then make it better.

**Run this:**

```
Who was Vera Rubin, and how does their work on galactic rotation curves and the evidence for dark matter connect to angular momentum applied to galactic and cosmological systems? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Vera Rubin"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to walk through Rubin's specific 1970 observation of M31 (the Andromeda galaxy) with Kent Ford's image-tube spectrograph — what they measured, what the rotation curve looked like, and why it required dark matter
- Ask: "Rubin was rejected from Princeton's graduate program because of her gender (the policy was reversed in 1975) and was famously never awarded a Nobel Prize despite the dark-matter evidence being foundational. What was the Nobel committee's stated reason — and what was the unstated one?"
- Add the framing: "Answer as if you're writing the catalog essay for a 2026 exhibit on Rubin's career at the Carnegie Institution"

What changes? What gets better? What gets worse?
