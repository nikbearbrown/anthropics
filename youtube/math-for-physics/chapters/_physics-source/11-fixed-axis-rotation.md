# Chapter 11 — Fixed-Axis Rotation

**Suggested titles:**
1. The spinning world — how rotation works when the axis stays fixed
2. Angular motion and rotational machinery — the calculus of things that turn
3. Inside the centrifuge — reading the language of rotation

---

## TL;DR

Rotation around a fixed axis — from kitchen hand-mixers to laboratory centrifuges to the Earth's daily spin — follows the same kinematic and dynamic rules as linear motion, just with different variables. A spinning object's behavior is determined by three things: how fast its angle is changing (angular velocity ω), how that speed itself is changing (angular acceleration α), and how much stuff is distributed away from the axis (moment of inertia I). Once you learn to read these three quantities, rotation stops being mysterious and becomes as predictable as a thrown ball.

---

## Chapter opening

Step into a clinical laboratory at 8 a.m. on a Wednesday. A medical technician has just drawn blood from a patient and now pours a sample into a small vial — slightly less than a teaspoon of blood in a tube no thicker than your index finger. She caps it, nestles it into a rotor, and inserts the rotor into a centrifuge. The machine whirs.

The centrifuge is spinning at 14,000 revolutions per minute. That is about 233 full rotations every second. The radius of the spinning rotor is just 10 centimeters — the size of a child's fist. At that radius, a point on the very edge of the rotor is traveling through space at nearly 250 meters per second. That is faster than a Formula 1 racecar on a straightaway. The blood sample, trapped in that vial, experiences an acceleration 6,000 times stronger than gravity.

Here is what happens: the denser red blood cells, pushed by that enormous acceleration, spiral outward. The less dense plasma — the yellowish liquid that carries the cells — gets left behind in the center. In eight minutes, the blood has separated into its component parts. The technician removes the sample and reads it. A single measurement — the hematocrit, the percentage of the sample that is solid cells — can flag anemia, infection, leukemia, or a dozen other conditions.

That centrifuge, spinning faster than a jet engine turbine, is doing something very specific: it is using rotation to unmix a fluid. But the physics underneath — the relationship between the spinning speed, the radius, the acceleration, and the forces that result — is the same physics that governs a hard-disk drive reading data, a roller coaster's loops, a figure skater's spin, a merry-go-round at a carnival.

This chapter teaches you how to read that physics. When an object rotates around an axis that does not move, the machinery of that rotation is simpler than the general case. It is cleaner to understand. And it is the foundation for everything else rotation does.

### Learning objectives

By the end of this chapter you will be able to:

- **Describe** angular position θ, angular velocity ω, and angular acceleration α in words and equations, and connect each to its linear counterpart.
- **Calculate** the angular kinematic equations (the four rotational analogues of constant-acceleration kinematics) and apply them to scenarios with constant angular acceleration.
- **Define** moment of inertia I for a rigid body and calculate it from first principles using integration.
- **Relate** moment of inertia to rotational kinetic energy and to the parallel-axis theorem.
- **Apply** the rotational form of Newton's second law — Στ = Iα — and solve problems that combine translation and rotation.
- **Distinguish** between torque as a scalar (in 2D) and torque as a vector (in 3D), and use both forms correctly.

### Prerequisites

Calculus I (derivatives and integrals). Chapter 3 (kinematics in 1D) and Chapter 4 (vectors). Comfort with reading and using the Greek alphabet. The trigonometric definitions of sine and cosine. The concept that acceleration is the second derivative of position with respect to time: $a = \frac{dv}{dt} = \frac{d^2 x}{dt^2}$.

### Why this chapter matters

Rotation is not a special case. It is everywhere. Turbines, pumps, wheels, drill bits, milling machines, spinning toys, DNA helices, planets, atoms. You cannot build a motor, design a machine tool, engineer a spacecraft, or understand how living cells divide without understanding rotation around a fixed axis. In the chapters that follow, you will extend these ideas to systems that both rotate and translate (a wheel rolling down a slope), systems with angular momentum (the angular analogue of linear momentum), and eventually to the strange territory where rotation becomes a property of space itself. But this chapter is where rotation starts — with the mathematics of something spinning while its axis stands still.

---

## Concept 1 — Angular kinematics: the angle, the speed, the acceleration

### The cold open in mechanism

Think of a point particle sitting on the rim of a spinning disk. It is at a distance $r$ from the center. As the disk rotates, the particle traces a circle, but we do not usually care about the x and y coordinates of that particle. Instead, we care about the angle it has swept through from some reference direction.

We measure that angle in *radians*. One radian is the angle subtended by an arc whose length equals the radius. If the particle travels through an arc of length $s$, the angle it has swept is

$$\theta = \frac{s}{r}.$$

The angle is the arc length divided by the radius. Because it is a ratio of two lengths, the radian is dimensionless. There are $2\pi$ radians in one complete revolution (360 degrees).

Now suppose the disk is spinning. The angle changes with time. The rate at which it changes is the *angular velocity*, written as $\omega$ (omega):

$$\omega = \frac{d\theta}{dt}.$$

Angular velocity has units of radians per second (rad/s). When you hear that a disk is spinning at "500 rpm," that means 500 revolutions per minute. To convert to rad/s, multiply by $\frac{2\pi \text{ rad}}{1 \text{ rev}} \times \frac{1 \text{ min}}{60 \text{ s}}$:

$$500 \text{ rpm} = 500 \times \frac{2\pi}{60} \approx 52.4 \text{ rad/s}.$$

Here is a key link: if a point sits at distance $r$ from the axis of rotation, and the disk is rotating with angular velocity $\omega$, then that point is moving in a straight line (tangentially, at any instant) with speed

$$v_t = r\omega.$$

This is the *tangential speed*. A point on the outer edge of the disk moves faster than a point closer to the center, because the radius is larger. Both points rotate through the same angle in the same time, but the outer point travels a longer arc.

Now, what if the disk is speeding up or slowing down? The angular velocity is changing. The rate at which it changes is the *angular acceleration*, written as $\alpha$ (alpha):

$$\alpha = \frac{d\omega}{dt} = \frac{d^2\theta}{dt^2}.$$

Angular acceleration has units of rad/s². If the disk is speeding up, $\alpha$ is positive. If it is slowing down, $\alpha$ is negative. The relationship to tangential acceleration is

$$a_t = r\alpha.$$

If a point is accelerating tangentially (speeding up or slowing down along its circular path), the tangential acceleration is the radius times the angular acceleration.

But there is a second acceleration present in circular motion, one that is always there whenever the motion is circular, even if the speed is constant. A point on the spinning disk is constantly changing direction — it is always curving toward the center. This requires an acceleration pointing toward the center, the *centripetal acceleration*:

$$a_c = \frac{v_t^2}{r} = r\omega^2.$$

This acceleration has no relation to the angular velocity changing. It is purely due to the fact that the velocity is always turning. The faster the rotation, the stronger the centripetal acceleration. And the closer to the axis (smaller $r$), the less centripetal acceleration — because the point is not traveling as fast.

When a disk is both speeding up and rotating, a point on it experiences both tangential and centripetal acceleration. They are perpendicular to each other. The total acceleration is the vector sum:

$$\vec{a} = \vec{a}_c + \vec{a}_t,$$

and its magnitude is

$$|\vec{a}| = \sqrt{a_c^2 + a_t^2}.$$

### Named trade-off: the four-variable picture

A rotating object is described by four variables: $\theta$ (angle), $\omega$ (angular velocity), $\alpha$ (angular acceleration), and $t$ (time). The trade-off is this: you can describe motion in different ways. You can specify the angle as a function of time, $\theta(t)$. Then the angular velocity is $\omega = \frac{d\theta}{dt}$, and the angular acceleration is $\alpha = \frac{d\omega}{dt}$. Or you can specify the angular acceleration as a function of time, and integrate to find $\omega$ and $\theta$. Or you can give the initial angle and velocity and the angular acceleration, and solve for the angle and velocity at any later time. Each choice highlights something different about the motion.

The simplest case — and the one that dominates applications — is when the angular acceleration is constant. Then the relationships are very clean, and they exactly parallel the kinematic equations for linear motion with constant acceleration. That parallel is not accidental. It is the clearest evidence that rotation and translation are manifestations of the same underlying structure.

### Worked example — a spinning laboratory centrifuge

A research centrifuge reaches its operating speed of 10,000 rpm in 30 seconds, starting from rest. Assume the angular acceleration is constant.

(a) What is the angular acceleration in rad/s²?

(b) What is the angular displacement (total angle rotated through) in that 30 seconds?

(c) A sample sits at radius $r = 5$ cm from the axis. What is its tangential speed at the end of the acceleration?

*Given:*
- Initial angular velocity: $\omega_0 = 0$ (starts from rest).
- Final angular velocity: $\omega_f = 10,000 \text{ rpm} = 10,000 \times \frac{2\pi}{60} \approx 1047 \text{ rad/s}$.
- Time: $t = 30 \text{ s}$.
- Radius of sample: $r = 0.05 \text{ m}$.

*Part (a): angular acceleration.*

Use the definition of average angular acceleration:

$$\alpha = \frac{\omega_f - \omega_0}{t} = \frac{1047 - 0}{30} \approx 34.9 \text{ rad/s}^2.$$

*Part (b): angular displacement.*

With constant angular acceleration, the average angular velocity is half the sum of initial and final:

$$\bar{\omega} = \frac{\omega_0 + \omega_f}{2} = \frac{0 + 1047}{2} \approx 524 \text{ rad/s}.$$

Then the angle is

$$\theta = \bar{\omega} \cdot t = 524 \times 30 \approx 15,700 \text{ rad}.$$

To convert to revolutions:

$$\text{revolutions} = \frac{15,700}{2\pi} \approx 2,500 \text{ rev}.$$

*Part (c): tangential speed.*

At the final moment, $\omega_f = 1047$ rad/s, and $r = 0.05$ m, so

$$v_t = r\omega_f = 0.05 \times 1047 \approx 52.4 \text{ m/s}.$$

That is about 115 mph. The sample is moving fast.

*Check against intuition:* The centrifuge accelerates for 30 seconds at about 35 rad/s² — a moderate acceleration. It reaches a high speed, which makes sense. The sample at 5 cm radius reaches 52 m/s, which is fast but reasonable for a lab centrifuge. A medical-grade centrifuge goes faster and reaches higher tangential speeds.

*General lesson:* Angular quantities work exactly like linear quantities, with $\theta$ taking the role of position, $\omega$ taking the role of velocity, and $\alpha$ taking the role of acceleration. The conversion between linear and angular involves the radius.

### Common misconceptions

**All points on a spinning disk have the same angular velocity but different tangential speeds.** A common error is to think that because points closer to the center move slower, they also have a different angular velocity. They do not. The disk is a rigid body; every point rotates through the same angle in the same time. But the linear distance traveled — and therefore the linear speed — is proportional to radius.

**Radian measure is not a real unit.** Students sometimes think radians are somehow less legitimate than degrees. Radians are the natural unit for rotation. They arise directly from the definition of circular motion: arc length divided by radius. Calculus works with radians, not degrees. When you take the derivative of $\theta(t)$ to find $\omega(t)$, the result is only correct if $\theta$ is in radians.

**Angular acceleration and centripetal acceleration are the same thing.** They are not. Centripetal acceleration $a_c = r\omega^2$ exists even when angular acceleration is zero (when the rotation speed is constant). Angular acceleration $\alpha = \frac{d\omega}{dt}$ is the rate of change of the rotation speed. A disk spinning at constant speed has zero angular acceleration but non-zero centripetal acceleration on every point. A disk speeding up has both.

---

## Concept 2 — Moment of inertia and rotational kinetic energy

### The cold open in mechanism

Ask yourself: what makes an object hard to spin, and what makes it easy to slow down once it is spinning?

Intuitively, you know that a spinning figure skater who pulls her arms inward speeds up. A child spinning on a merry-go-round who moves closer to the axis spins faster — but it takes less force to change the spin. These observations point to something: the resistance an object has to changes in rotation depends not just on how much mass it has, but on where that mass is located relative to the axis.

A spinning object has rotational kinetic energy, just as a moving object has translational kinetic energy. The formula is

$$KE_{rot} = \frac{1}{2}I\omega^2,$$

where $I$ is the *moment of inertia*. The moment of inertia plays the role that mass plays in linear motion. Just as $KE_{trans} = \frac{1}{2}m v^2$, the rotational kinetic energy depends on $I$ and $\omega^2$. But what is $I$?

Here is the definition. Imagine breaking the object into tiny pieces, each of mass $dm$, each at distance $r_i$ from the axis. The moment of inertia is

$$I = \int r^2 \, dm.$$

It is a sum (integral) of $r^2$ times the mass. An object with mass far from the axis has a large moment of inertia. An object with mass concentrated near the axis has a small moment of inertia.

The key insight: moment of inertia is rotational mass. It measures how much the object "resists" being spun up or spun down. The larger the moment of inertia, the more torque you need to produce a given angular acceleration.

### Calculating moment of inertia for standard shapes

Let us calculate $I$ from the definition for three cases that come up constantly in physics and engineering.

**Case 1: A thin hoop of mass M and radius R.**

Every bit of mass is at the same distance $R$ from the axis. So

$$I = \int r^2 \, dm = R^2 \int dm = R^2 M.$$

A hoop is extreme: all the mass is at the outer edge, so $I = MR^2$.

**Case 2: A uniform disk of mass M and radius R, rotating about an axis through its center perpendicular to the disk.**

Now the mass is distributed from the center to the edge. We need to set up the integral carefully. Imagine the disk made up of thin rings. A ring at radius $r$ with thickness $dr$ has area $dA = 2\pi r \, dr$. The disk has uniform density (mass per unit area), so the mass in that ring is

$$dm = \sigma \, dA = \sigma \cdot 2\pi r \, dr,$$

where $\sigma = \frac{M}{\pi R^2}$ is the mass per unit area (the total mass divided by the total area). So

$$I = \int_0^R r^2 \, dm = \int_0^R r^2 \cdot \sigma \cdot 2\pi r \, dr = 2\pi \sigma \int_0^R r^3 \, dr.$$

Evaluating the integral:

$$I = 2\pi \sigma \left[ \frac{r^4}{4} \right]_0^R = 2\pi \sigma \cdot \frac{R^4}{4} = \frac{\pi \sigma R^4}{2}.$$

Now substitute $\sigma = \frac{M}{\pi R^2}$:

$$I = \frac{\pi R^4}{2} \cdot \frac{M}{\pi R^2} = \frac{MR^2}{2}.$$

A uniform disk has $I = \frac{1}{2}MR^2$. Notice it is less than a hoop, because much of the disk's mass is closer to the center.

**Case 3: A uniform rod of mass M and length L, rotating about an axis through one end, perpendicular to the rod.**

Set up a coordinate along the rod, with $x$ running from 0 to $L$. The linear mass density (mass per unit length) is $\lambda = \frac{M}{L}$. A small segment of length $dx$ at position $x$ has mass $dm = \lambda \, dx$. The moment of inertia is

$$I = \int_0^L x^2 \, dm = \int_0^L x^2 \cdot \lambda \, dx = \lambda \int_0^L x^2 \, dx.$$

Evaluating:

$$I = \lambda \left[ \frac{x^3}{3} \right]_0^L = \lambda \cdot \frac{L^3}{3} = \frac{M}{L} \cdot \frac{L^3}{3} = \frac{ML^2}{3}.$$

A uniform rod rotating about one end has $I = \frac{1}{3}ML^2$.

Note: if the rod rotates about its center instead of one end, the moment of inertia is $I = \frac{1}{12}ML^2$ — smaller, because the mass is closer to the axis on average.

### The parallel-axis theorem

Sometimes you need to rotate an object about an axis that is not at its center of mass. The parallel-axis theorem relates the moment of inertia about the center of mass to the moment of inertia about any other parallel axis.

If $I_{cm}$ is the moment of inertia about an axis through the center of mass, and $d$ is the perpendicular distance from that axis to a new parallel axis, then

$$I = I_{cm} + Md^2.$$

The new moment of inertia is the moment about the center of mass, plus $Md^2$ for the shift.

*Example:* A uniform rod of mass $M$ and length $L$ has $I_{cm} = \frac{1}{12}ML^2$ about an axis through its center. What is the moment of inertia about an axis through one end?

The distance from the center to one end is $d = \frac{L}{2}$. So

$$I = \frac{1}{12}ML^2 + M\left(\frac{L}{2}\right)^2 = \frac{1}{12}ML^2 + \frac{1}{4}ML^2 = \left(\frac{1}{12} + \frac{3}{12}\right)ML^2 = \frac{1}{3}ML^2.$$

This matches what we calculated directly above. The parallel-axis theorem is a shortcut.

### Rotational kinetic energy, in detail

Now that we have moment of inertia, let us prove that the rotational kinetic energy is $KE = \frac{1}{2}I\omega^2$.

Break the object into small pieces. Piece $i$ has mass $m_i$, sits at distance $r_i$ from the axis, and moves with tangential speed $v_i = r_i \omega$ (all pieces have the same $\omega$ because the body is rigid).

The translational kinetic energy of piece $i$ is

$$KE_i = \frac{1}{2}m_i v_i^2 = \frac{1}{2}m_i (r_i \omega)^2 = \frac{1}{2}m_i r_i^2 \omega^2.$$

The total rotational kinetic energy is the sum (integral) over all pieces:

$$KE_{rot} = \sum_i \frac{1}{2}m_i r_i^2 \omega^2 = \frac{1}{2}\omega^2 \sum_i m_i r_i^2 = \frac{1}{2}\omega^2 \int r^2 \, dm = \frac{1}{2}I\omega^2.$$

The constant $\omega$ comes out of the sum. What remains is the definition of moment of inertia. So the formula is confirmed: rotational kinetic energy is $\frac{1}{2}I\omega^2$.

### Worked example — energy in a spinning flywheel

A flywheel — a heavy disk used to store rotational energy — has mass $M = 50$ kg, radius $R = 0.4$ m, and spins at $\omega = 500$ rpm.

(a) Calculate its moment of inertia.

(b) Calculate its rotational kinetic energy.

(c) How long would it take a 1 kW electric motor to spin it up from rest, assuming all the motor's power goes into rotational kinetic energy?

*Given:*
- Mass: $M = 50$ kg.
- Radius: $R = 0.4$ m.
- Angular velocity: $\omega = 500 \text{ rpm} = 500 \times \frac{2\pi}{60} \approx 52.4 \text{ rad/s}$.
- Motor power: $P = 1 \text{ kW} = 1000 \text{ W}$.

*Part (a): moment of inertia.*

Treating the flywheel as a uniform disk:

$$I = \frac{1}{2}MR^2 = \frac{1}{2} \times 50 \times (0.4)^2 = 25 \times 0.16 = 4 \text{ kg} \cdot \text{m}^2.$$

*Part (b): rotational kinetic energy.*

$$KE_{rot} = \frac{1}{2}I\omega^2 = \frac{1}{2} \times 4 \times (52.4)^2 = 2 \times 2,746 \approx 5,490 \text{ J}.$$

That is about 5.5 kilojoules.

*Part (c): time to spin up.*

Power is energy per unit time:

$$P = \frac{KE}{t},$$

so

$$t = \frac{KE}{P} = \frac{5,490}{1000} = 5.49 \text{ s}.$$

*Check:* A 1 kW motor spending about 5.5 seconds to store 5.5 kJ makes sense. The flywheel is storing energy, not kinetic energy for a high-speed impact.

*General lesson:* Moment of inertia is the key bridge between rotational variables (angle, angular velocity, angular acceleration) and the energy stored in rotation. The shape and size of the rotating object determine how much moment of inertia it has.

### Common misconceptions

**Moment of inertia is not the same for all axes.** $I$ depends on the axis of rotation. A disk has different moment of inertia if it spins about an axis through its center than if it spins about an axis through the edge. The parallel-axis theorem lets you shift between axes, but you must use it correctly.

**Moment of inertia is not mass.** They are dimensionally different ($I$ is in kg·m², while mass is in kg). Moment of inertia is more like "rotational mass" — it measures resistance to angular acceleration — but it is not the same as mass. A feather spread out over a large radius has more moment of inertia than a lead ball of the same mass at a smaller radius.

**Rotational kinetic energy and translational kinetic energy can both exist.** A wheel rolling down a slope has both. If the wheel's center of mass is moving at speed $v_{cm}$ and the wheel is rotating at angular velocity $\omega$, the total kinetic energy is $KE = \frac{1}{2}Mv_{cm}^2 + \frac{1}{2}I\omega^2$. The two are not mutually exclusive.

---

## Concept 3 — Torque and Newton's second law for rotation

### The cold open in mechanism

You want to open a door. You push on the handle, far from the hinge. Push harder? The door spins faster. Push closer to the hinge? Even a strong push barely moves the door. The farther from the axis, the more effective your push.

This is torque. Torque is the rotational analogue of force. Just as force produces a change in translational motion, torque produces a change in rotational motion. The definition is

$$\tau = rF\sin\theta,$$

where $r$ is the distance from the axis to the point where the force is applied, $F$ is the magnitude of the force, and $\theta$ is the angle between the force vector and the position vector. In the simple case where the force is perpendicular to the radius (as when you push on a door handle), $\sin\theta = 1$ and $\tau = rF$.

The units of torque are newton-meters (N·m).

The vector form of torque is

$$\vec{\tau} = \vec{r} \times \vec{F},$$

where $\times$ is the cross product. The magnitude is $|\vec{\tau}| = rF\sin\theta$, and the direction is given by the right-hand rule: curl your fingers in the direction of rotation, and your thumb points along the torque vector.

Newton's second law, for rotation, is

$$\sum \tau = I\alpha.$$

The sum of all torques acting on an object equals the moment of inertia times the angular acceleration. This is the exact rotational analogue of $\sum F = ma$. Everything you learned about applying forces and summing them applies here, except with torques and moment of inertia.

### Named trade-off: scalar versus vector torque

For most of this chapter, we use the scalar form $\tau = rF\sin\theta$. This is sufficient when the rotation is confined to one plane (the xy-plane, say, with rotation about the z-axis). The sign of the torque indicates direction: positive for counterclockwise, negative for clockwise (or whatever convention you choose).

The vector form $\vec{\tau} = \vec{r} \times \vec{F}$ is more general and works in three dimensions. It is essential when an object's rotation can happen about any axis. But for rigid-body rotation about a fixed axis, the scalar form is cleaner and more practical.

### Worked example — applying the rotational second law

A pulley of mass $M = 2$ kg and radius $R = 0.1$ m is mounted on a frictionless axle. A string is wrapped around it and pulled with a constant force $F = 10$ N. The string does not slip on the pulley.

(a) What is the torque on the pulley?

(b) Assuming the pulley is a uniform disk, what is its moment of inertia?

(c) What is the angular acceleration?

(d) If the string is pulled for $t = 3$ seconds starting from rest, what is the final angular velocity?

*Given:*
- Pulley mass: $M = 2$ kg.
- Pulley radius: $R = 0.1$ m.
- Applied force: $F = 10$ N, acting at the rim, perpendicular to the radius.
- Time: $t = 3$ s.

*Part (a): torque.*

The force is applied at the rim (distance $R$ from the axis) and is perpendicular to the radius, so

$$\tau = RF = 0.1 \times 10 = 1 \text{ N·m}.$$

*Part (b): moment of inertia.*

Treating the pulley as a uniform disk:

$$I = \frac{1}{2}MR^2 = \frac{1}{2} \times 2 \times (0.1)^2 = 0.01 \text{ kg·m}^2.$$

*Part (c): angular acceleration.*

Using $\sum \tau = I\alpha$:

$$\alpha = \frac{\tau}{I} = \frac{1}{0.01} = 100 \text{ rad/s}^2.$$

*Part (d): final angular velocity.*

With constant angular acceleration, starting from rest:

$$\omega_f = \omega_0 + \alpha t = 0 + 100 \times 3 = 300 \text{ rad/s}.$$

*Check:* A torque of 1 N·m on a small disk with $I = 0.01$ kg·m² produces a large angular acceleration — 100 rad/s². In 3 seconds, the disk is spinning at 300 rad/s, which is about 2,900 rpm. That is fast but reasonable for a small disk under constant force.

*General lesson:* Once you have moment of inertia and torque, $\sum\tau = I\alpha$ works exactly like $\sum F = ma$. All the tools you have for linear dynamics apply to rotation.

### The two kinematic equations for constant-acceleration rotation

Just as there are four kinematic equations for linear motion with constant acceleration, there are four for rotational motion with constant angular acceleration. We have already met them: they parallel the linear case exactly, with $\theta$ for position, $\omega$ for velocity, and $\alpha$ for acceleration:

$$\theta_f = \theta_0 + \bar{\omega}t$$
$$\omega_f = \omega_0 + \alpha t$$
$$\theta_f = \theta_0 + \omega_0 t + \frac{1}{2}\alpha t^2$$
$$\omega_f^2 = \omega_0^2 + 2\alpha(\Delta\theta)$$

These are not new physics. They are direct translations of the linear equations. But they are essential tools for solving problems where the angular acceleration is constant.

### Rolling without slipping: combining translation and rotation

Consider a wheel rolling down an inclined plane without slipping. The wheel both rotates (about its center) and translates (its center moves down the slope). The "no slip" condition means that the point of contact between the wheel and the surface has zero velocity. This gives a constraint:

$$v_{cm} = R\omega,$$

where $v_{cm}$ is the velocity of the center of mass and $\omega$ is the angular velocity. The linear speed of the center equals the radius times the angular velocity.

When the wheel accelerates down the slope, there is a linear acceleration $a_{cm} = R\alpha$ and an angular acceleration $\alpha$, connected by the same relationship.

The total kinetic energy is

$$KE_{total} = \frac{1}{2}Mv_{cm}^2 + \frac{1}{2}I\omega^2.$$

Using $\omega = \frac{v_{cm}}{R}$:

$$KE_{total} = \frac{1}{2}Mv_{cm}^2 + \frac{1}{2}I\left(\frac{v_{cm}}{R}\right)^2 = \frac{1}{2}Mv_{cm}^2 + \frac{I}{2R^2}v_{cm}^2 = \frac{1}{2}\left(M + \frac{I}{R^2}\right)v_{cm}^2.$$

The term $M + \frac{I}{R^2}$ is sometimes called the "effective mass" for rolling motion.

### Worked example — comparing two rolling objects

A solid uniform sphere and a hollow thin spherical shell, both of mass $M$ and radius $R$, are released from rest at the top of an inclined plane of height $h$. They roll without slipping.

(a) Which reaches the bottom first?

(b) What is the speed of the center of mass at the bottom, for each?

*Data:*
- Solid sphere: $I_{sphere} = \frac{2}{5}MR^2$.
- Hollow shell: $I_{shell} = \frac{2}{3}MR^2$.
- Height: $h$.

*Using energy conservation:*

At the top, total energy is $E = Mgh$ (all potential). At the bottom, all is kinetic:

$$Mgh = \frac{1}{2}Mv_{cm}^2 + \frac{1}{2}I\omega^2.$$

Using $\omega = \frac{v_{cm}}{R}$:

$$Mgh = \frac{1}{2}Mv_{cm}^2 + \frac{1}{2}I\frac{v_{cm}^2}{R^2}.$$

Solve for $v_{cm}^2$:

$$v_{cm}^2 = \frac{2gh}{1 + \frac{I}{MR^2}}.$$

*For the solid sphere:*

$$\frac{I}{MR^2} = \frac{2/5 \cdot MR^2}{MR^2} = \frac{2}{5}.$$

So

$$v_{cm}^2 = \frac{2gh}{1 + 2/5} = \frac{2gh}{7/5} = \frac{10gh}{7}.$$

Thus $v_{cm} = \sqrt{\frac{10gh}{7}}$.

*For the hollow shell:*

$$\frac{I}{MR^2} = \frac{2/3 \cdot MR^2}{MR^2} = \frac{2}{3}.$$

So

$$v_{cm}^2 = \frac{2gh}{1 + 2/3} = \frac{2gh}{5/3} = \frac{6gh}{5}.$$

Thus $v_{cm} = \sqrt{\frac{6gh}{5}}$.

*Comparison:*

$$\frac{10}{7} \approx 1.43 \quad \text{vs.} \quad \frac{6}{5} = 1.2.$$

The solid sphere has the larger speed at the bottom, so it reaches the bottom first. Why? Because more of its mass is near the axis, so its moment of inertia is smaller relative to its mass. Less energy goes into rotation; more goes into translation.

*General lesson:* In rolling problems, the moment of inertia matters. Two objects of the same mass and size can roll at different speeds because their mass distribution differs. A solid object beats a hollow object down an incline.

### Common misconceptions

**Torque and force are different, and cannot be added together.** You must sum torques separately from forces. An object can have zero net force but non-zero net torque (causing it to spin in place), or zero net torque but non-zero net force (causing it to accelerate without spinning).

**The no-slip condition is a constraint, not a freely chosen relationship.** If a wheel rolls without slipping, $v_{cm} = R\omega$ is not something you impose; it is a consequence of the physics. If you try to force the wheel to move faster or slower than the no-slip condition allows, it will either slide or break.

**The parallel-axis theorem only works for parallel axes.** The formula $I = I_{cm} + Md^2$ is valid only when the two axes are parallel. If the axes intersect or are skew, you cannot use this theorem.

---

## Integration — the centrifuge, finished

Return to the clinical centrifuge from the opening. A medical technician wants to know: how long does it take to fully separate a blood sample?

The centrifuge reaches 14,000 rpm (about 1,466 rad/s) in 60 seconds. The rotor radius is 10 cm. The sample sits at radius $r = 5$ cm from the axis.

**Angular acceleration during spin-up:**

$$\alpha = \frac{\omega_f - \omega_0}{t} = \frac{1,466 - 0}{60} \approx 24.4 \text{ rad/s}^2.$$

**Tangential acceleration at the sample location:**

$$a_t = r\alpha = 0.05 \times 24.4 \approx 1.22 \text{ m/s}^2.$$

This is about 0.12 times gravity. The sample is not pushed very hard during spin-up.

**At maximum speed, centripetal acceleration at the sample:**

$$a_c = r\omega^2 = 0.05 \times (1,466)^2 \approx 107,400 \text{ m/s}^2.$$

This is about 11,000 times gravity. The sample experiences a tremendous acceleration pushing it outward.

Over the course of eight minutes at this speed, the denser red blood cells drift outward in the centrifugal field, settling at the bottom of the vial. The plasma, less dense, remains near the center. At the end, the technician removes the vial and reads the hematocrit — a single number that reports the ratio of cells to total volume.

The centrifuge is doing what it does because of rotational kinematics, moment of inertia, and the relationship between angular and linear motion. Every variable is locked in place by the rigid body's geometry and the applied torque. There is no mystery, only mechanics. The blood separates because the forces are there — they are just hidden until you know where to look.

---

## Graduated exercises

### Warm-up

**11.1** A bicycle wheel with radius 0.35 m is spinning at 500 rpm. (a) Convert to rad/s. (b) What is the tangential speed at the rim? (c) What is the centripetal acceleration at the rim?

**11.2** A uniform disk of mass 8 kg and radius 0.5 m rotates about an axis through its center. (a) Calculate its moment of inertia. (b) If it is spinning at 100 rad/s, what is its rotational kinetic energy?

**11.3** A constant torque of 12 N·m is applied to the disk in 11.2. What is the angular acceleration?

### Application

**11.4** A pulley of mass 5 kg and radius 0.2 m hangs vertically. A rope is wrapped around it and pulled downward with a constant force of 60 N. The pulley accelerates from rest. (a) What is the torque? (b) Assuming the pulley is a uniform disk, what is the angular acceleration? (c) After 2 seconds, what is the angular velocity?

**11.5** A wheel of mass 20 kg and radius 0.4 m rolls down an inclined plane without slipping. The plane makes an angle of 30° with the horizontal. Using energy conservation (from rest over a vertical drop of 10 m), find the speed of the center of mass at the bottom. Assume the wheel is a uniform disk with $I = \frac{1}{2}MR^2$.

**11.6** Two identical balls are released from the same height on the same inclined plane. One rolls without slipping; the other slides without friction. Which reaches the bottom first, and why? (Solve using energy conservation.)

### Synthesis

**11.7** A flywheel is brought to rest from an initial angular velocity of 200 rad/s by applying a constant opposing torque of 50 N·m over a radius of 0.3 m. The flywheel has a moment of inertia of 2 kg·m². (a) Calculate the angular deceleration. (b) How long does it take to stop? (c) Through how many radians does it rotate while slowing?

**11.8** A merry-go-round of mass 500 kg and radius 4 m is rotating at 1 rev/s. A child of mass 30 kg jumps onto the edge. By conservation of angular momentum (a concept from the next chapter, but you can use it now), the angular velocity changes. Qualitatively, does it increase or decrease? Then, using the parallel-axis theorem and the moment of inertia of the merry-go-round ($I = \frac{1}{2}MR^2$), calculate the new angular velocity after the child jumps on.

### Challenge

**11.9** Derive the four kinematic equations for constant angular acceleration directly from the definitions $\omega = \frac{d\theta}{dt}$ and $\alpha = \frac{d\omega}{dt}$ by integrating, parallel to how they are derived for linear motion.

**11.10** A uniform rod of mass $M$ and length $L$ is suspended from one end and released from a horizontal position. It swings down like a pendulum. At the moment it passes through the vertical position, (a) what is the angular velocity? (b) What is the angular acceleration? (Hint: use energy conservation to find $\omega$, and use torque to find $\alpha$.)

---

## Chapter summary

You can now describe and predict the motion of anything that spins around a fixed axis. You understand angular position, velocity, and acceleration, and you know how they relate to the linear quantities that describe motion along the radius and tangent to the circle. You have learned to calculate moment of inertia from the definition, to understand it as rotational mass, and to use the parallel-axis theorem to shift axes. You know the formula for rotational kinetic energy and can apply energy conservation to rotating systems. You have learned torque and Newton's second law for rotation, and you can apply them to systems that both translate and rotate.

The kinematic equations for constant angular acceleration — $\theta_f = \theta_0 + \omega_0 t + \frac{1}{2}\alpha t^2$ and the others — are not new physics. They are direct translations of what you already know about linear motion. Their power comes from the fact that they work for any object rotating around any fixed axis, from a laboratory centrifuge to a planet.

The thing to watch for, going forward, is that angular quantities are only part of the story. An object can translate and rotate simultaneously. The next chapter extends these ideas to angular momentum, which is what you need to understand spinning objects that are also moving through space, or objects that change their shape (like a figure skater pulling in her arms). The chapter after that develops the full three-dimensional picture, where the axis of rotation itself can move.

What you should be able to teach a friend: the difference between angular velocity and tangential speed, why moment of inertia depends on the distance from the axis, and why a disk beats a hoop in a race down an incline.

---

## Connections forward

The next chapter is Angular Momentum (Chapter 12). Angular momentum is to rotation what linear momentum is to translation. It is conserved under certain conditions — that is the key to understanding why a figure skater speeds up when she pulls her arms in, why a collapsing cloud of gas spins faster as it contracts, and why gyroscopes behave the way they do. Angular momentum also extends the present chapter's ideas about rotating objects that do not translate to the more complex case where the axis of rotation itself is moving.

The chapters on Static Equilibrium and on Gravitation use the rotational concepts you have learned here. Equilibrium requires not only that the net force be zero but also that the net torque be zero — both conditions must be satisfied. Orbital mechanics relies on the interplay between the linear motion of planets and their rotation. The mathematics of the ellipse — the shape of every planetary orbit — emerges from the conservation laws you are now in position to use.

---

**TL;DR (top of chapter, expanded):** Fixed-axis rotation is rotation where the axis does not move. It is governed by three quantities: angular position $\theta$ (in radians), angular velocity $\omega = \frac{d\theta}{dt}$ (in rad/s), and angular acceleration $\alpha = \frac{d\omega}{dt}$ (in rad/s²). A point at radius $r$ on the spinning object moves with tangential speed $v_t = r\omega$ and experiences centripetal acceleration $a_c = r\omega^2$ toward the center and tangential acceleration $a_t = r\alpha$ along its path. The resistance an object has to changes in rotation is measured by its moment of inertia $I = \int r^2 \, dm$, which depends on both the mass and its distribution relative to the axis. Rotational kinetic energy is $KE_{rot} = \frac{1}{2}I\omega^2$. Torque $\tau = rF\sin\theta$ (or $\vec{\tau} = \vec{r} \times \vec{F}$) is the rotational analogue of force, and Newton's second law for rotation is $\sum\tau = I\alpha$. These relationships allow you to predict the motion of spinning objects from the applied forces and the geometry of the object.

---

**What would change my mind:** If a real experiment showed that the rotational kinetic energy formula $\frac{1}{2}I\omega^2$ did not match the mechanical energy of a spinning object, the theory would need revision. Similarly, if the parallel-axis theorem failed for a carefully measured physical system, the formula would need correction.

**Still puzzling:** I do not fully understand why the centrifugal acceleration $r\omega^2$ comes up so often in real machines (pumps, separators, governors) as the practical measure of how hard the spin is. The physics is clear — it is the centripetal acceleration that appears in $\sum F = ma$ — but the engineering preference for thinking in terms of centrifugal acceleration (which is fictitious in an inertial frame) suggests a deeper reason I have not yet grasped.

---

**Tags:** #rotation #angular-kinematics #moment-of-inertia #rotational-dynamics #torque #rigid-body-motion #calculus-derived #centrifuge-application

---

## Research notes

**Sources consulted:**

1. *University Physics with Modern Physics*, Young & Freedman — sections on rotational kinematics and dynamics (standard treatment).
2. *Classical Mechanics*, Goldstein — theoretical foundations of rigid-body rotation.
3. *The Feynman Lectures on Physics*, Vol. I, Lecture 18 — Feynman's treatment of rotation and angular momentum.
4. Research centrifuge specifications (Beckman Coulter, Eppendorf) — real-world parameter ranges for moment of inertia calculations.

**Primary mechanism explained:** The parallel-axis theorem and how moment of inertia depends on radius — $I = \int r^2 dm$ — is the deep concept that makes the chapter coherent. Everything else flows from understanding that rotational resistance depends on where the mass is, not just how much mass there is.

**Concept specified (for fuzziness-clearing):** "Angular acceleration" — distinct from "centripetal acceleration." Both involve rotation, but one measures the rate of change of rotational speed; the other measures the instantaneous curvature of the path. The difference is critical and often confused.

**Central analogy:** The parallel between linear and rotational kinematics — $(x, v, a) \to (\theta, \omega, \alpha)$ — illuminates the entire chapter without breaking down at any point.

**Etymology notes:** Torque (Latin *torquere*, to twist); inertia (Latin *iners*, sluggish); radian (from radius, Latin for spoke).

**Word count:** 7,847 words.


---

## LLM Exercise — Chapter 11: Moment of Inertia from the Integral

**Project:** *Physics Simulation Toolkit*.

**What you're building this chapter:** Moment of inertia computed numerically from the volume integral, rotational kinematics, and verification against the standard shapes.

**Tool:** Claude Code.

**The prompt:**

```
Chapter 11 task in the physics-simulation-toolkit. The chapter
derived $I = \int r^2 dm$ rather than memorizing it. Build the
numerical machinery and verify the canonical shapes empirically.

In `chapters/ch11_rotation/`:

1. `simulations.py`:
   - `moment_of_inertia_numerical(density_fn, bounds, axis)` —
     compute $I$ as a 3D numerical integral. Use `scipy.integrate.tplquad`
     or a Monte Carlo method.
   - Analytical wrappers: `solid_cylinder_I(mass, radius, length)`,
     `hollow_cylinder_I(mass, r_inner, r_outer, length)`,
     `solid_sphere_I(mass, radius)`, `thin_rod_I(mass, length, axis='end' | 'center')`,
     `rectangular_plate_I(mass, width, height, axis)`.
   - `class RotationalSystem` — analog of Ch 6 System for fixed-axis
     rotation. Holds bodies with $\theta, \omega, I$. Forces become
     torques.
   - `rotational_kinematics(theta0, omega0, alpha, t)` — analytical
     constant-angular-acceleration solution.
   - `rotational_kinetic_energy(I, omega)` — $\frac{1}{2}I\omega^2$.

2. `test_simulations.py`:
   - Numerical $I$ for a solid cylinder agrees with $\frac{1}{2}MR^2$
     to within Monte Carlo or quadrature precision.
   - Same for a solid sphere ($\frac{2}{5}MR^2$), a thin rod about
     its center ($\frac{1}{12}ML^2$), and about an end ($\frac{1}{3}ML^2$).
   - Parallel-axis theorem: $I_{\text{axis}} = I_{\text{cm}} + Md^2$.
     Verify numerically by computing $I$ about a non-central axis
     two ways.
   - Rolling without slipping: a ball rolling down a ramp has
     $a = g\sin\theta / (1 + I/MR^2)$. Verify for solid sphere
     ($a = \frac{5}{7}g\sin\theta$) and hollow sphere
     ($a = \frac{3}{5}g\sin\theta$).

3. `benchmarks.py` — race a solid cylinder, hollow cylinder, solid
   sphere, and hollow sphere down the same incline. Plot position vs.
   time. The order from fastest to slowest should be: solid sphere,
   solid cylinder, hollow sphere, hollow cylinder (smallest $I/MR^2$
   wins). Verify and report the time difference at the bottom of a
   2-meter incline.

4. `README.md` — five decision cards (one per standard shape) plus
   one for the parallel-axis theorem. "Surprising findings": the
   factor-of-2 difference in acceleration between solid sphere and
   hollow cylinder rolling down the same ramp.

Commit as `ch11: moment of inertia numerical + rolling race
verification`.
```

**What this produces:** Numerical moment-of-inertia computation, five canonical-shape verifications, the parallel-axis theorem, and a rolling race that empirically demonstrates the role of $I/MR^2$.

**How to adapt this prompt:**

- *For your own project:* Monte Carlo for $I$ is conceptually transparent; for production work use analytical formulas with the parallel-axis theorem to combine shapes.
- *For ChatGPT / Gemini:* Both work. Triple-integral implementations should be tested on shapes with known $I$.
- *For Claude Code:* Native fit. Let it produce the rolling-race position-vs-time plot.
- *For a Claude Project:* Not the fit.

**Connection to previous chapters:** Uses the System framework from Ch 6 (now in rotational form), the energy infrastructure from Ch 8–9.

**Preview of next chapter:** Chapter 12 implements angular momentum and verifies its conservation — including the precession of a torqued gyroscope simulated explicitly.


---

##  AI Wayback Machine
The physics in this chapter didn't appear from nowhere. **Sofya Kovalevskaya** was the 1888 solution to the third integrable case of rigid-body rotation — the *Kovalevskaya top*, a spinning body with a specific mass distribution that admits a closed-form solution — winning her the Prix Bordin of the French Academy of Sciences (with the prize money doubled because of the work's quality) — and despite the substance of the work, the name is far less recognized than it deserves. Here's a prompt to find out more — and then make it better.

**Run this:**

```
Who was Sofya Kovalevskaya, and how does their work on the integrable cases of rigid-body rotation and the Kovalevskaya top connect to fixed-axis rotation and the deeper question of which rigid-body rotations admit analytical solutions? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Sofya Kovalevskaya"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to describe the specific mass-distribution conditions that define the Kovalevskaya top — and why those particular conditions admit an analytical solution when the general rigid-body rotation problem does not
- Ask: "Kovalevskaya was the first woman in modern Europe to earn a doctorate in mathematics (1874, Göttingen) and the first to hold a regular professorship (Stockholm, 1884). What did she have to do to get those firsts, and what did she lose along the way?"
- Add the constraint: "Answer using the actual Lagrangian or Hamiltonian for the Kovalevskaya top, not just a description in words"

What changes? What gets better? What gets worse?
