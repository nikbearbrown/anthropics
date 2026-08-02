# Circular and Rotational Motion: Why Things Spin and Why They Don't Fall In

**TL;DR:** Circular motion is a puzzle — an object travels at constant speed but is always accelerating. That acceleration points toward the center, and it requires a force. This one observation — that direction matters more than you'd expect — unlocks the whole machinery.

---

## Chapter Opening: A Car and a Curve

You are in a car traveling at exactly 25 meters per second on a highway curve. The road is smooth. Your speed doesn't change. Yet you feel pushed sideways, as if something is shoving you away from the center of the turn. Your body wants to keep moving forward in a straight line. The car, meantime, is turning. That sideways feeling is not a real force — it's your inertia, the tendency to keep doing what you're already doing, colliding with the car's insistence on changing direction.

This is circular motion: motion along a circular path. It is everywhere. A tire spinning. A ball on a string. Earth orbiting the sun. A figure skater pirouetting. A record on a turntable. A merry-go-round. A satellite in orbit. But here's the puzzle that makes it worth understanding: if your speed isn't changing, why is your body screaming that something is being done to you? The answer hinges on a word — *velocity* — and on a precise distinction between speed and velocity that you've met before but may not have internalized yet.

**Learning Objectives**
By the end of this chapter, you will be able to:
- Describe the angle of rotation and its measurement in radians
- Relate angular velocity and angular acceleration to their linear counterparts
- Explain centripetal acceleration as acceleration that points toward the center of motion
- Calculate centripetal force and understand what provides it
- Connect torque to angular acceleration using the rotational analog of Newton's second law
- Distinguish between real centripetal forces and the fictitious centrifugal force

**Prerequisites**
You should be comfortable with Newton's laws of motion, especially the first and second laws. You should understand displacement, velocity, and acceleration as vectors. You should know what a radian is, or be willing to learn.

---

## Concept 1: The Geometry of Rotation — Angles, Radians, and Angular Velocity

### The Mechanism: From Arc Length to Angular Displacement

A compact disc spins on its axis. Watch a single point on the edge of the disc — call it a pit, one of the microscopic marks that holds data. That pit moves in a circle. In a given time, it travels a certain distance along the circular path (we call this the *arc length*). But here's what matters: the pit also rotates through a certain angle.

The angle of rotation is defined as a ratio:

$$\Delta\theta = \frac{\Delta s}{r}$$

where $\Delta s$ is the arc length the pit travels, and $r$ is the radius of the disc. This is not an arbitrary definition. It emerges from a deeper fact: if you know the angle the pit rotates through, and you know the radius, you can calculate how far the pit actually moved along the circle. The angle captures the *pure rotation* — the amount of turning — independent of the disc's size.

Think of it this way: imagine two discs, one with radius 0.5 m and one with radius 1.0 m. If both rotate through the same angle, the pit on the larger disc travels twice as far as the pit on the smaller disc, because it traverses a longer arc. The angle is the same. The arc length is not. The ratio—arc length divided by radius—stays constant. That's why we define the angle as $\Delta\theta = \Delta s / r$.

Now the unit: the radian. When physicists measure angles in rotational motion, we almost always use radians, not degrees. A radian is defined as the angle at which the arc length equals the radius: $\Delta\theta = 1$ rad when $\Delta s = r$. One complete revolution — a full 360° — is $2\pi$ radians, because the circumference of a circle is $2\pi r$. So:

$$1 \text{ revolution} = 2\pi \text{ rad} = 360°$$

From this, we get the conversion:
$$1 \text{ rad} = \frac{360°}{2\pi} \approx 57.3°$$

Some useful conversions for common angles:
- $30° = \pi/6$ rad
- $45° = \pi/4$ rad
- $60° = \pi/3$ rad
- $90° = \pi/2$ rad
- $180° = \pi$ rad

This looks like notation. It's actually a hidden insight: radians make the math simpler because they're dimensionless. The radian is a ratio of two lengths (arc length divided by radius), so when you use it in equations, you can drop it, and your units work out cleanly. Degrees don't have this property. A degree is an arbitrary fraction of a circle (1/360 of a full rotation). Radians are natural. They emerge from the geometry of a circle. Radians are the currency of rotational physics.

### The Trade-Off: Radians Require Conversion, But They Simplify Everything Else

The cost of using radians is small: you need to convert from degrees, or learn to think in terms of $\pi/2$ instead of 90°, $\pi$ instead of 180°, $2\pi$ instead of 360°. In time, these become as natural as 90 and 180. The benefit is large: every equation that relates angular quantities to linear quantities becomes dimensionally transparent. You'll see this in the next section. If you use degrees, you'd need conversion factors scattered throughout your equations. With radians, the math stays clean.

### The Worked Example: How Much Does the Hour Hand Rotate?

The hour hand of a large clock has a radius of 1.0 meter. From 12 p.m. to 3 p.m., the hour hand moves through a quarter of the full 12-hour cycle. What angle does it rotate through, in radians? And what is the arc length at the tip of the hand?

The hour hand covers 1/4 of a full revolution in moving from 12 to 3. A full revolution is $2\pi$ radians, so:

$$\Delta\theta = \frac{1}{4} \times 2\pi \text{ rad} = \frac{\pi}{2} \text{ rad} \approx 1.57 \text{ rad}$$

The arc length follows from the definition:

$$\Delta s = r \, \Delta\theta = (1.0 \text{ m}) \left(\frac{\pi}{2} \text{ rad}\right) = \frac{\pi}{2} \text{ m} \approx 1.57 \text{ m}$$

The radian is dimensionless, so it cancels, and we get meters — the correct unit for distance. Notice: we didn't need a conversion factor. We didn't need to multiply by some weird constant. The equation $\Delta s = r \, \Delta\theta$ works directly because radians are defined the way they are.

### Common Misconception: "Radians Are Just Another Name for Angles"

No. Radians are a specific *measurement* of angles, chosen because they make the mathematics of circular motion work without the need for conversion factors. Degrees are another measurement. They're equal in concept but different in practice. When you use degrees in a physics equation that expects radians, you'll get the wrong answer, sometimes by a factor of 57.3. For example, if you calculate $\omega$ (angular velocity) using degrees per second instead of radians per second, your answer will be off by a factor of $2\pi/360 \approx 0.0175$.

---

## Concept 2: Angular Velocity and the Connection to Linear Velocity

### The Mechanism: How Fast Is the Disc Spinning?

The pit on the compact disc rotates through a certain angle in a certain time. Define the angular speed as:

$$\omega = \frac{\Delta\theta}{\Delta t}$$

The units are radians per second (rad/s). If the angle changes faster, the angular speed is larger. That's the definition. Angular speed is the *rate* at which the angle changes. The Greek letter omega ($\omega$) is standard notation for angular velocity, just as $v$ is standard for linear velocity.

Now here's where it gets interesting. Consider two different pits on the same disc. One sits near the center, the other near the edge. They both rotate through the same angle in the same time — they have the same angular speed. Yet the pit at the edge moves faster along the circular path than the pit at the center. Why? Because it has to travel a longer arc.

The linear distance the pit travels is the arc length: $\Delta s = r \, \Delta\theta$. Divide both sides by the time, $\Delta t$:

$$\frac{\Delta s}{\Delta t} = r \frac{\Delta\theta}{\Delta t}$$

The left side is the linear speed (or tangential speed, because it's the speed in the direction tangent to the circle — the direction the pit is moving at any instant). The right side is the radius times the angular speed:

$$v = r\omega$$

This equation is profound. It says: the tangential speed of a point in circular motion is directly proportional to both its distance from the center and how fast the system is spinning. A point at twice the radius, spinning at the same angular velocity, moves twice as fast. A system spinning at twice the angular velocity, at the same radius, has points moving twice as fast. Neither the distance nor the rotation rate dominates; they multiply.

Here's a concrete way to feel it: stand near the edge of a spinning playground merry-go-round, and then stand near the center. Same rotation rate. Your feet (at the edge) move much faster than your hands (nearer the center) would if you reached inward. The edge moves because the radius is larger.

### The Trade-Off: Angular Velocity Is Independent of Radius, But Tangential Velocity Isn't

This is the conceptual payoff. If you want to describe how fast a system is rotating, use angular velocity — it doesn't depend on which point you're measuring. A spinning record rotates at one $\omega$. All points on the record have the same $\omega$. If you want to know the actual speed of a point in space — how fast it's moving relative to the ground — you need both the angular velocity and the radius. The smaller the radius, the slower the point moves, even though the system is spinning just as fast. This is why angular velocity is useful for describing rotating systems: it's intrinsic to the system, independent of where you measure.

### The Worked Example: A Car Tire

A car travels down the highway at 15.0 m/s (about 54 km/h). The tire has a radius of 0.300 m. How fast is the tire spinning, in rad/s? And in revolutions per second?

The speed of the tire tread — the part touching the road — is the same as the speed of the car (assuming no slipping). So $v = 15.0$ m/s. Rearrange $v = r\omega$ to solve for $\omega$:

$$\omega = \frac{v}{r} = \frac{15.0 \text{ m/s}}{0.300 \text{ m}} = 50.0 \text{ rad/s}$$

To convert to revolutions per second:
$$\omega = 50.0 \text{ rad/s} \times \frac{1 \text{ rev}}{2\pi \text{ rad}} \approx 7.96 \text{ rev/s}$$

So the tire spins about 8 times per second, or 480 revolutions per minute (rpm).

Now consider a larger tire on the same car, with radius 1.20 m:

$$\omega = \frac{15.0 \text{ m/s}}{1.20 \text{ m}} = 12.5 \text{ rad/s} \approx 1.99 \text{ rev/s} \approx 119 \text{ rpm}$$

The larger tire covers more arc length per revolution, so it rotates fewer times per second to maintain the same speed. This is why car manufacturers tune their speedometers to the expected tire size — the dashboard reads the tire's rotation speed and converts it to the car's forward speed using the relationship $v = r\omega$. If you install tires with a significantly different radius, your speedometer will read incorrectly. A driver with oversized tires will see the speedometer reading lower than the actual speed; a driver with undersized tires will see it reading higher.

### Common Misconception: "Angular Velocity and Linear Velocity Are the Same Thing"

Not at all. Angular velocity depends only on how fast the system rotates. Linear (or tangential) velocity depends on both the rotation speed and the distance from the center. For a given rotation speed, points farther out move faster. For a given point, faster rotation means faster motion. The relationship is $v = r\omega$. You can't know one without knowing the other. They're related but distinct.

---

## Concept 3: Centripetal Acceleration and Centripetal Force — The Inward Pull

### The Mechanism: Acceleration Without a Change in Speed

You ride in a car around a smooth, circular curve. Your speed is constant — the speedometer doesn't change. Yet you feel pushed sideways. Here's the insight that resolves the puzzle: acceleration is a change in velocity, and velocity is a vector. Velocity has both magnitude (speed) and direction. In uniform circular motion, the magnitude of velocity (the speed) stays constant, but the direction is constantly changing.

At any instant, the car is moving tangent to the circle. An instant later, it's moving in a slightly different direction — rotated by a small angle. The change in velocity points roughly toward the center of the circle. To see this, draw the velocity vector at one point on the circle, then draw the velocity vector at a nearby point. Both vectors have the same magnitude (same speed), but they point in slightly different directions. The difference between them — the change in velocity — points toward the center of the circle. As the time interval shrinks to zero, the acceleration points *exactly* toward the center.

We call this centripetal acceleration (from Latin, meaning "center-seeking"):

$$a_c = \frac{v^2}{r}$$

where $v$ is the tangential speed and $r$ is the radius. We can also write it in terms of angular velocity:

$$a_c = r\omega^2$$

To see why these two expressions are equivalent, substitute $v = r\omega$ into the first:
$$a_c = \frac{(r\omega)^2}{r} = \frac{r^2\omega^2}{r} = r\omega^2$$

The centripetal acceleration is always perpendicular to the velocity, always pointing toward the center of the circular path. For a given speed $v$, sharper curves (smaller $r$) require larger centripetal acceleration. Higher speeds require larger centripetal acceleration — and notice that it scales with $v^2$. Double your speed, and the required acceleration quadruples. This is why highway curves at high speed are dangerous. The faster you go, the more your body must be accelerated to follow the curve.

### The Trade-Off: Constant Speed but Changing Direction

The cost is subtle: you must distinguish between speed (how fast you're going) and velocity (how fast you're going in what direction). The benefit is that you can now understand circular motion as a consequence of Newton's laws. An object moving in a circle isn't mysteriously "held" by the circle — it's being accelerated toward the center, and something must provide that acceleration.

### The Worked Example: A Car Rounding a Curve

A car travels at 25.0 m/s around a circular curve with radius 500 m. What is the centripetal acceleration? How does it compare to gravitational acceleration? How much force is needed?

$$a_c = \frac{v^2}{r} = \frac{(25.0 \text{ m/s})^2}{500 \text{ m}} = \frac{625 \text{ m}^2/\text{s}^2}{500 \text{ m}} = 1.25 \text{ m/s}^2$$

Gravitational acceleration is $g = 9.80$ m/s². The ratio is:

$$\frac{a_c}{g} = \frac{1.25}{9.80} = 0.128$$

So the centripetal acceleration is about 12.8% of gravitational acceleration, or roughly 1/8 of $g$. You feel a sideways push about 1/8 as strong as the downward pull of gravity. That's noticeable but not extreme.

Now, what force is required? Using Newton's second law, if the car has a mass of 1,200 kg:

$$F_c = m a_c = (1,200 \text{ kg})(1.25 \text{ m/s}^2) = 1,500 \text{ N}$$

This force must come from somewhere. On a dry road, it comes from friction between the tires and the road. If the road is icy, friction is reduced, and the car may not be able to provide enough centripetal force. The car will skid outward — not because of an outward force, but because the inward force (friction) is insufficient.

At higher speeds or sharper curves, the numbers grow quickly. If you double the speed to 50 m/s, the centripetal acceleration quadruples to 5 m/s², which is about 0.5g. If you go around a sharper curve (radius 100 m instead of 500 m) at the original speed of 25 m/s, the acceleration becomes $625/100 = 6.25$ m/s², which is about 0.64g. These are the limits of what a typical car and driver can handle safely.

### From Acceleration to Force

Newton's second law says that acceleration requires a force:

$$F_c = m a_c$$

where $m$ is the mass and $a_c$ is the centripetal acceleration. The centripetal force is the net force pointing toward the center of rotation. It can come from many sources: the friction between a tire and the road, the tension in a rope, the gravitational pull of the sun on a planet, the normal force from a roller coaster track during a loop, the magnetic force on a charged particle in a cyclotron.

The magnitude of centripetal force is:

$$F_c = m\frac{v^2}{r} = m r \omega^2$$

The key insight: centripetal force is not a new kind of force. It's the net force, whatever its source, that points toward the center. Multiple forces can contribute. Friction and the normal force can both help. When the net force points toward the center with the right magnitude, circular motion results. If the centripetal force is too small, the object curves less sharply and moves outward. If the centripetal force is too large, the object curves more sharply and moves inward.

### Common Misconception: "Centrifugal Force Pushes Objects Outward"

This is a trap. Centrifugal force is *not real*. It is a fictitious force that appears only when you stand in a rotating reference frame — like the car going around the curve. From the ground's perspective (an inertial frame), the car is pulling inward on you (via friction with the seat and the normal force), and you accelerate inward toward the center of the curve. From the car's perspective (a rotating frame), there's a mysterious outward force pushing you away from the center. This is not a real force; it's a bookkeeping artifact of using a non-inertial frame.

Here's the physics: your body, by Newton's first law, wants to continue moving in a straight line. The car, turning, is trying to change your direction. The seat pushes inward on you (that's a real force). But from the car's spinning perspective, it looks like you're being pushed outward. In reality, you're being pulled inward, and your inertia makes it feel like you're being pushed outward.

The real force — the centripetal force — points inward. It's what changes your direction and keeps you moving in a circle instead of flying off in a straight line.

---

## Concept 4: Rotational Kinematics and Torque

### The Mechanism: Spinning Faster, Spinning Slower

So far, we've assumed constant angular velocity. But spinning systems often speed up or slow down. A spinning skater pulls in her arms and spins faster. A fan turns on, gradually accelerating. A fishing reel is braked and slows to a stop. In all these cases, angular velocity changes. Define angular acceleration:

$$\alpha = \frac{\Delta\omega}{\Delta t}$$

with units rad/s². If the angular velocity increases, $\alpha$ is positive (by convention, counterclockwise is positive). If it decreases, $\alpha$ is negative. This is completely parallel to linear acceleration: $a = \Delta v / \Delta t$.

The rotational kinematics equations mirror the linear kinematics equations. For constant angular acceleration:

$$\omega = \omega_0 + \alpha t$$

$$\theta = \omega_0 t + \frac{1}{2}\alpha t^2$$

$$\omega^2 = \omega_0^2 + 2\alpha\theta$$

These should look familiar. They're the rotational versions of $v = v_0 + at$, $x = v_0 t + \frac{1}{2}at^2$, and $v^2 = v_0^2 + 2ax$. The symmetry is exact: just replace $x$ with $\theta$, $v$ with $\omega$, and $a$ with $\alpha$. This is not a coincidence. It reveals a deep structure in physics: the mathematics of motion is the same whether you're translating or rotating.

The tangential acceleration at radius $r$ is $a = r\alpha$. The farther from the center, the greater the tangential acceleration for a given angular acceleration. A point on the rim of a spinning wheel accelerates tangentially more than a point near the hub, even though both experience the same angular acceleration.

### Torque: The Rotational Analog of Force

Now we ask: what *causes* angular acceleration? Answer: torque, the rotational analog of force. If you push a merry-go-round at its edge, perpendicular to the radius, you produce a large torque and the merry-go-round accelerates quickly. If you push near the center, the same force produces much less torque, and the acceleration is slower. Torque is defined as:

$$\tau = r F \sin\theta$$

where $r$ is the distance from the pivot point (the lever arm), $F$ is the magnitude of the force, and $\theta$ is the angle between the lever arm and the force. When the force is perpendicular to the lever arm, $\sin\theta = 1$, and the torque is maximized: $\tau = r F$.

The units are newton-meters (N·m). Torque is a vector: it has a direction (determined by the right-hand rule) and points along the axis of rotation. If you curl the fingers of your right hand in the direction of rotation, your thumb points in the direction of the torque vector.

Newton's second law has a rotational analog: a net torque produces angular acceleration:

$$\tau_{net} = I \alpha$$

where $I$ is the *moment of inertia* — the rotational analog of mass. Objects with more mass, especially mass farther from the axis, have larger moments of inertia and are harder to spin up. A thin disc and a thick, dense disc of the same size have different moments of inertia. The denser one is harder to spin. This makes physical sense: inertia is the resistance to acceleration. Rotational inertia is the resistance to angular acceleration.

### The Worked Example: Stopping a Fishing Reel

A deep-sea fisherman's reel spins at an initial angular velocity of 220 rad/s. The fisherman applies a brake, creating an angular acceleration of $\alpha = -300$ rad/s² (negative because it opposes the rotation). How long until the reel stops?

Use the kinematic equation $\omega = \omega_0 + \alpha t$. Set $\omega = 0$ (the reel is stopped) and solve for $t$:

$$0 = 220 + (-300)t$$

$$t = \frac{220}{300} = 0.733 \text{ s}$$

The reel stops in about three-quarters of a second. The large deceleration (300 rad/s²) makes the stopping time short. If the fisherman applied less deceleration — say, 100 rad/s² — the reel would take much longer to stop:

$$t = \frac{220}{100} = 2.2 \text{ s}$$

Fishing lines sometimes snap because of the forces involved during braking. Fishermen often let the fish tire before applying brakes, so the fish is swimming slowly (lower angular velocity of the reel, lower forces). The tension in the line is $T = m a_{\text{tangent}}$, where $m$ is the mass of the fish and $a_{\text{tangent}} = r\alpha$ is the tangential deceleration of the line. A large angular deceleration $\alpha$ produces a large tangential acceleration, which produces a large tension. That's why sudden braking can snap the line.

### Common Misconception: "Torque Is the Same as Force"

No. Torque depends on force, distance from the pivot, and the angle at which the force is applied. The same force applied at different distances produces different torques. The same force applied at different angles produces different torques. A 100 N force applied 1 m from the pivot, perpendicular to the lever arm, produces $\tau = 100$ N·m. The same 100 N force applied 0.5 m from the pivot produces $\tau = 50$ N·m. And the same 100 N force applied at 30° to the lever arm produces $\tau = 100 \sin(30°) = 50$ N·m.

---

## Integration: From Motion to Forces to Energy

We began with a puzzle: an object travels at constant speed in a circle, yet something is being done to it. Now the machinery is visible.

In uniform circular motion, the speed is constant, but the velocity is not — it's constantly changing direction. Velocity is a vector, and the acceleration points toward the center of the circle. That acceleration requires a force, which comes from friction, tension, gravity, or the normal force of a track. The centripetal force is not a new kind of force; it's the net force, whatever its source, pointing toward the center.

When angular velocity is not constant, angular acceleration occurs. Angular acceleration requires a net torque, which depends on the magnitude of the force and its distance from the pivot point. Push farther from the center, and you generate more torque for the same force. The relationship $\tau = r F \sin\theta$ is the rotational analog of $F = ma$.

All of this flows from one principle: Newton's second law applies to rotation just as it applies to linear motion. Change the vocabulary from force to torque, from mass to moment of inertia, from velocity to angular velocity, and the mathematics is identical. This is not coincidence. It's evidence of a deep symmetry in how nature works: the laws of motion don't care whether you're moving in a line or in a circle.

The equations of rotational motion are powerful because they let you predict what will happen. If you know the torque applied to a spinning object and its moment of inertia, you can calculate its angular acceleration. If you know the angular acceleration and the initial angular velocity, you can calculate how long it will take to reach a target speed. All the problems that seemed mysterious — why does a spinning skater speed up when pulling in her arms, why does a heavier wheel spin slower when pushed by the same force — now have clear answers.

The machinery also connects to energy. An object moving in a circle carries kinetic energy, just like an object moving in a straight line. The kinetic energy of a point at radius $r$ with tangential velocity $v$ is $\frac{1}{2}mv^2$. For a spinning object, we sum this over all points and define the rotational kinetic energy as $KE_{\text{rot}} = \frac{1}{2}I\omega^2$, where $I$ is the moment of inertia. The form is identical to the linear case: $\frac{1}{2}m v^2$. The parallel is exact.

Understanding circular motion is the gateway to understanding not just cars on curves and spinning wheels, but also planets in orbit, atoms in molecules, electrons orbiting nuclei (in the Bohr model), and the entire structure of the solar system. The centripetal force that holds your body in a turning car is the same type of force that holds the moon in orbit around Earth and Earth in orbit around the sun.

---

## Graduated Exercises

**Warm-Up**

1. A wheel rotates through $\pi$ radians in 2 seconds. What is its average angular velocity in rad/s?

2. A point on the edge of a spinning disc is 0.5 m from the center and moves at 3.0 m/s. What is the angular velocity of the disc?

3. Convert 45° to radians.

**Application**

4. A cyclist travels at 8.0 m/s around a circular path with radius 25 m. Calculate the centripetal acceleration. Is it larger or smaller than gravitational acceleration?

5. A 1,200 kg car rounds a 400 m radius curve at 20 m/s. The only horizontal force is friction from the tires. How much frictional force is required? If the maximum static friction available is 4,500 N, can the car safely take this curve at this speed?

6. A 0.5 m radius wheel spins at 100 rad/s. What is the tangential velocity at the edge? If the wheel is braked with an angular deceleration of 50 rad/s², how long does it take to stop? How many radians does it rotate through before stopping?

**Synthesis**

7. Two points on a spinning record are at radii 0.10 m and 0.20 m from the center. The record spins at 33 rpm (revolutions per minute). Calculate the tangential velocities at each radius. Why do you think vinyl records can store information reliably even though points at different radii move at different speeds?

8. A merry-go-round has a moment of inertia of 500 kg·m². A force of 200 N is applied at the edge, 2.0 m from the center, perpendicular to the radius. What is the torque? What is the angular acceleration?

**Challenge**

9. A satellite orbits Earth at a constant altitude. Its circular orbit has radius $r$ from Earth's center. The gravitational force provides the centripetal force. Show that the orbital speed is $v = \sqrt{GM/r}$, where $G$ is the gravitational constant and $M$ is Earth's mass. What happens to the orbital speed as the satellite moves to a higher altitude (larger $r$)? Does this match what you know about geostationary satellites?

10. A spinning top has angular momentum. When it is spinning fast, it appears to defy gravity and remains upright. When it slows down, it begins to wobble and eventually falls. Explain qualitatively what is happening. What quantity is changing, and what is causing that change?

---

## Chapter Summary

Circular motion is motion along a circular path. The angle of rotation is measured in radians, a dimensionless ratio of arc length to radius. Radians are preferred in physics because they make equations clean: no conversion factors are needed. Angular velocity $\omega = \Delta\theta / \Delta t$ describes how fast a system rotates, independent of which point on the system you're measuring. Tangential velocity, the linear speed of a point on the circle, is $v = r\omega$ — it depends on both the rotation rate and the distance from the center.

In uniform circular motion, speed is constant but velocity is not — its direction is always changing. This change in direction is acceleration, pointing toward the center: $a_c = v^2/r = r\omega^2$. This centripetal acceleration requires a centripetal force, $F_c = m a_c$, which can originate from friction, tension, gravity, or any other source pointing toward the center. Centrifugal force — the outward push you feel in a turning car — is fictitious; it arises only when you use a rotating reference frame.

When angular velocity changes, angular acceleration $\alpha = \Delta\omega / \Delta t$ occurs. Angular acceleration requires a net torque, $\tau = rF\sin\theta$. The farther the force is applied from the pivot point, and the more perpendicular it is to the lever arm, the greater the torque. The rotational analog of Newton's second law is $\tau = I\alpha$, where $I$ is the moment of inertia.

The language of rotational motion — angle, angular velocity, angular acceleration, torque, moment of inertia — is the rotational analog of the language of linear motion. The mathematics is identical. Newton's laws apply to rotation just as they apply to translation. This deep symmetry is a clue to the fundamental structure of physics.

---

## Connections Forward

In the next chapter, we'll extend these ideas to systems where both translation and rotation happen together — a wheel rolling down a hill, a spinning top precessing. You'll also meet the concept of angular momentum, which relates rotational motion to energy the way linear momentum relates translational motion to energy.

The machinery of circular motion also explains planetary orbits, why a satellite in geostationary orbit stays fixed above the equator, and why the sun doesn't pull the moon away from Earth. Centripetal force, in the guise of gravity, is the thread that holds the solar system together.

Understanding rotational motion also opens the door to oscillation — systems that move back and forth rather than around. A pendulum, a mass on a spring, a vibrating string. All of these can be understood as projections of circular motion onto a line. The connection is subtle but powerful, and we'll explore it in depth.

---

**What Would Change My Mind:**
If I found that the relationship $v = r\omega$ did not hold experimentally — if tangential and angular velocities were not proportional — I would know something fundamental was wrong with this account. But it holds. Every observation of spinning systems confirms it.

**Still Puzzling:**
I don't fully understand why nature chose to make the radian the natural unit of rotational motion. Yes, the mathematics works out, and dimensionless quantities are elegant. But is there a deeper reason? Is there a physical principle that would lead, from first principles, to the radian? I can derive it, but not explain why it's the form nature takes. That gap hints at something not yet clear.

---

**Tags:** circular-motion, rotational-dynamics, centripetal-acceleration, angular-velocity, torque, kinematics, Newton's-laws, mechanics
---

## LLM Exercise — Chapter 6: Circular and Rotational Motion (Physics Demonstrations Notebook Project)

**Project:** Physics Demonstrations Notebook.
**What you're building this chapter:** the bucket-swing demo (centripetal force) plus the spinning-egg-vs-raw-egg demo (moment of inertia).
**Tool:** **Claude Project** for the entry.

---

**The Prompt:**

```
Chapter 6 demo. Notebook in this Claude Project. Chapter 6 taught:
centripetal acceleration (a = v²/r, directed inward); centripetal
force (F = mv²/r) — the force required to keep something moving in
a circle; torque (rotational analog of force); angular velocity;
angular momentum and moment of inertia (different mass distributions
have different I).

Two short demos for this chapter — pick one or both.

**Demo A — The Bucket of Water (Centripetal Force)**

Tie a string handle to a small bucket or sealed container. Half-fill
with water. Swing the bucket in a vertical circle around your shoulder.
At the top of the swing, the water doesn't fall out — provided you're
swinging fast enough.

The physics: at the top of the swing, the water needs a centripetal
acceleration of v²/r toward the swing center (which is downward,
toward you). Gravity provides the centripetal force naturally — but
only if v² ≥ gr. Below that speed, gravity provides MORE downward
force than required, and the water starts to fall out (and spills).

Procedure:
1. Outdoors. Practice swinging at gradually increasing speeds.
2. Find the slowest speed at which the water still stays in.
3. Estimate the radius (your arm + string length) and the period
   of swing.
4. Compute v = 2πr / T.
5. Check: is v² ≥ gr at the threshold? Within measurement error?

The threshold tells you the minimum speed for the centripetal-
force argument to work.

**Demo B — Spinning Egg vs. Raw Egg (Moment of Inertia)**

Take two eggs: one raw, one hard-boiled (cooked). Spin them on
their sides on a smooth surface. Stop each briefly with your finger,
then release.

The hard-boiled egg stops cleanly — its mass is rigidly connected
to the shell, so when you stop the shell, you stop the egg.

The raw egg, when stopped briefly and released, starts spinning
again — the liquid yolk and white have angular momentum that
wasn't transferred when you stopped only the shell.

The physics: moment of inertia depends on mass distribution. The
raw egg has internal degrees of freedom (the liquid); the cooked
egg doesn't.

**Use Claude as a thinking partner:**
- Before A: "Compute the threshold velocity for water-not-spilling
  at the top of a 60-cm-radius vertical swing. How fast is that
  in revolutions per second?"
- After A: "My measured threshold period was T seconds, radius r
  meters. Compute v² and compare to gr. Within error?"
- For B: "Why do the raw and cooked eggs behave so differently
  to a brief stop-and-release?"

**Notebook entry should include:**
- Photo or video of the swing (at safe range from people).
- For A: measured threshold period and radius; computed v²;
  comparison to gr.
- For B: photo of both eggs spinning; description of behavior
  difference.
- Free-body diagram of the bucket at the top of the swing.

End with the question: a fighter pilot in a vertical loop must
maintain a minimum speed to stay in the loop. Why? What would
happen if they slowed below that speed?
```

---

**What this produces:** A demo entry confirming centripetal-force reasoning (Demo A) and moment-of-inertia reasoning (Demo B). The bucket-swing is the most unforgettable physics demo most students ever do.

**How to adapt this prompt:**

- *For your own project:* Outdoors only for the bucket. Start with the bucket weight low (half-full, not full).
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* Optional for video-based period measurement.
- *For a Claude Project:* Append.

**Connection to previous chapters:** Ch 4's free-body-diagram discipline applies; Ch 6 uses centripetal force as a NEW kind of force-balance.

**Preview of next chapter:** Chapter 7 is gravitation. You'll measure g using a pendulum's period, then compare to the chapter's textbook 9.8 m/s².


---

## AI Wayback Machine

**Emmy Noether** proved that every continuous symmetry corresponds to a conservation law — including rotation and angular momentum.

**Run this:**

```
Who is Emmy Noether, and how does their work connect to circular and rotational motion we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Emmy Noether"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Emmy Noether's experiments or arguments in detail.
- Add a constraint: "Answer including criticisms or limits of Emmy Noether's framework."

What changes? What gets better? What gets worse?
