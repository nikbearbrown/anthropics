# Chapter 5: Motion in Two and Three Dimensions

## TL;DR

Most motion isn't a straight line — it's curved, changing in multiple directions at once. The key is independence: horizontal and vertical motions are separable and unaffected by each other when gravity is the only force. This allows us to treat 2D motion as two simultaneous 1D problems.

## Three title options

1. The Parabola and the Circle: Why most motion splits into perpendicular pieces
2. Motion in the Plane: When up-and-down motion doesn't care what left-and-right is doing
3. Independence and the Path: How to predict where an object goes when it moves in two directions

---

## Chapter Opening: Seven Minutes of Terror

August 5, 2012. Mars. Curiosity rover descending through the thin Martian atmosphere at 5,400 meters per second. The NASA team at the Jet Propulsion Laboratory in Pasadena cannot stop what happens next — the signal from Mars takes 14 minutes to cross the void. For seven minutes, the rover is alone with physics.

It takes a parachute, then fires retrorockets, then drops onto the surface on cables, all while the wind shears sideways, all while velocity must drop from hypersonic to zero, all while the lander must slow not just downward but eastward and northward, decelerating in three dimensions simultaneously. The engineers have computed every second of this motion. They know the position, velocity, and acceleration in each direction. If any of those numbers is wrong — if the upward deceleration is too slow or the sideways compensation isn't quite right — a three-billion-dollar machine becomes wreckage.

The rover lands safely. The mathematics of motion in two and three dimensions works. Which is to say: the mathematics of independence works.

**What you will understand by the end:**

- How position, velocity, and acceleration become vectors, and why treating them separately along different axes makes the problem solvable.
- Why a projectile follows a parabola and how to calculate its range, maximum height, and time in the air from first principles.
- Why circular motion at constant speed still has acceleration, and how to find it.
- How reference frames change what an observer sees, and how to transform velocities between them.

**You will need:**

- Calculus I: derivatives and how they represent rates of change.
- Vectors: components, vector addition, dot and cross products.
- Trigonometry: sine, cosine, angles, the unit circle.
- One-dimensional kinematics: the relationship between position, velocity, and acceleration.

---

## Concept 1: Vector Kinematics — Position, Velocity, Acceleration in Multiple Dimensions

### The Mechanism: Independence of Perpendicular Motions

Imagine you are standing on the deck of a ship, 16.7 meters from home plate at a baseball stadium. You throw a baseball horizontally at 40 meters per second. At that same instant, a second ball is dropped from your hand to the deck. The question sounds simple: which hits first?

The answer is: they hit at the same time. Horizontal velocity has no influence on vertical falling time. This is not intuition. It is a consequence of gravity acting in only one direction.

Here's why it matters. Motion in multiple dimensions is only solvable because we can separate it. The vertical component of motion depends only on the vertical component of velocity and the downward pull of gravity. The horizontal component depends only on the horizontal velocity — gravity doesn't pull sideways, no air resistance, so nothing changes the horizontal motion at all.

We write the position of a particle moving in three dimensions using a vector:

$$\vec{r}(t) = x(t)\hat{i} + y(t)\hat{j} + z(t)\hat{k}$$

This is not three separate equations. It is one statement: the particle's position at time $t$ is a combination of its position along the $x$-axis, the $y$-axis, and the $z$-axis. Each coordinate is a function of time. Each moves independently.

The instantaneous velocity is the derivative of position with respect to time:

$$\vec{v}(t) = \frac{d\vec{r}}{dt} = \frac{dx}{dt}\hat{i} + \frac{dy}{dt}\hat{j} + \frac{dz}{dt}\hat{k}$$

Because we can take the derivative component by component, this becomes:

$$\vec{v}(t) = v_x(t)\hat{i} + v_y(t)\hat{j} + v_z(t)\hat{k}$$

The key: $v_x$ depends only on the motion in the $x$ direction. It tells you nothing about $v_y$ or $v_z$.

Acceleration is the derivative of velocity:

$$\vec{a}(t) = \frac{d\vec{v}}{dt} = a_x(t)\hat{i} + a_y(t)\hat{j} + a_z(t)\hat{k}$$

Again, independence. Each component is separate. If you know the acceleration in $x$ and the initial velocity in $x$, you can calculate the motion in $x$ using exactly the one-dimensional kinematic equations you learned before. Same for $y$ and $z$. The motion is not really three-dimensional — it is three one-dimensional motions happening at the same time, using time as the only variable they share.

### The Trade-off: What This Approach Gains and Loses

The independence assumption works because gravity acts in one direction only (downward). If air resistance coupled the horizontal and vertical motion — if moving faster downward made you move faster sideways — the problem would become unsolvable with elementary mathematics. The system optimizes for simplicity. It works because gravity is simple. It fails the moment you include air drag, wind, or the Magnus force that makes a baseball curve.

In the real world, air resistance kills the independence assumption. A baseball hit by a batter doesn't follow a parabola; it follows a more complex curve, rising less high and traveling less far than the math predicts. This is why home runs are harder at high altitude: thinner air means less drag, less deviation from the ideal parabola, bigger range. When you account for air resistance, the trajectory equations become transcendental — they have no closed-form solution. You need a computer.

For now, we ignore air resistance. Not because it doesn't exist. Because with it, we cannot solve the problem by hand. The independence we gain is worth the trade: we get predictions that work well for thrown balls, fired projectiles, and satellites, as long as the speeds stay subsonic and the altitudes stay below where the atmosphere thickens.

### Worked Example: A Satellite's Displacement

A satellite is in a polar orbit 400 kilometers above Earth's surface. At some moment, it is directly above the North Pole. Three hours later, by Earth's rotation and orbital mechanics, it has moved to a latitude of −45°. What is its displacement — the straight-line distance from start to finish?

**Setup.** We place the origin at Earth's center. The North Pole is on the positive $y$-axis. The radius of Earth is 6,371 kilometers, so the orbital radius is 6,371 + 400 = 6,771 kilometers.

At $t_1$, the satellite position is:
$$\vec{r}_1 = 6,771\,\text{km}\,\hat{j}$$

At $t_2$, the satellite is at −45° latitude. On Earth's surface, that would be 45° south of the equator. But the satellite is in orbit, so we convert to Cartesian coordinates. At −45° latitude and some longitude (let's place it on the meridian where $z = 0$):
$$\vec{r}_2 = 6,771\,\cos(-45°)\hat{i} + 6,771\,\sin(-45°)\hat{j}$$
$$= 4,787\,\hat{i} - 4,787\,\hat{j}\,\text{km}$$

**The displacement** is the vector from $\vec{r}_1$ to $\vec{r}_2$:
$$\Delta\vec{r} = \vec{r}_2 - \vec{r}_1 = 4,787\,\hat{i} - 4,787\,\hat{j} - 6,771\,\hat{j}$$
$$= 4,787\,\hat{i} - 11,558\,\hat{j}\,\text{km}$$

The magnitude of displacement — the straight-line distance — is:
$$|\Delta\vec{r}| = \sqrt{4,787^2 + 11,558^2} = 12,509\,\text{km}$$

The angle this displacement makes with the $x$-axis (east) is:
$$\theta = \arctan\left(\frac{-11,558}{4,787}\right) = -67.5°$$

So the satellite has moved 12,509 kilometers in a direction 67.5° south of due east. The path it took — curved along the orbital arc — was much longer. But the displacement, the shortest line between two points, is 12,509 kilometers. We did not need to know the curved path at all. We only needed the initial and final positions as vectors.

### Common Misconception

Students often confuse displacement with distance traveled. Displacement is a vector — it points from start to finish. Distance is the length of the actual path. For a satellite in orbit, the orbital arc traveled is 4,787 kilometers east plus about 3,000 kilometers south (along the arc), totaling roughly 5,500 kilometers of actual path. The displacement magnitude is 12,509 kilometers. They are not the same. Displacement ignores the path. Velocity and acceleration do not — they are the rates at which position and velocity change, and position changes along whatever path the object follows.

---

## Concept 2: Projectile Motion — The Parabola from Gravity

### The Mechanism: Why Parabolas Appear

We begin with a simple scenario. You stand at the edge of a cliff, 233 meters above the ground. You throw a rock horizontally at 18.1 meters per second. How long until it hits, and how far away does it land?

The $x$ direction (horizontal): no forces except air resistance, which we ignore. No acceleration. Constant velocity:
$$x(t) = v_{0x} t = 18.1\,t$$

The $y$ direction (vertical): gravity pulls downward at 9.8 m/s². Constant acceleration:
$$y(t) = y_0 + v_{0y} t - \frac{1}{2}gt^2 = 233 + 0 - 4.9t^2$$

(We start at 233 meters, with zero initial vertical velocity, and subtract the distance fallen.)

The rock hits when $y(t) = 0$:
$$0 = 233 - 4.9t^2$$
$$t = \sqrt{\frac{233}{4.9}} = 6.9\,\text{s}$$

In 6.9 seconds, how far horizontally?
$$x = 18.1 \times 6.9 = 125\,\text{m}$$

Now, we ask: what is the shape of the trajectory? We eliminate time from the two kinematic equations. From the $x$ equation:
$$t = \frac{x}{v_{0x}}$$

Substitute into the $y$ equation:
$$y = y_0 + v_{0y}\left(\frac{x}{v_{0x}}\right) - \frac{1}{2}g\left(\frac{x}{v_{0x}}\right)^2$$

Rearrange:
$$y = y_0 + \left(\frac{v_{0y}}{v_{0x}}\right)x - \frac{g}{2v_{0x}^2}x^2$$

This is the trajectory equation. It has the form $y = a + bx - cx^2$, where $a$, $b$, and $c$ are constants determined by the initial conditions. The $-cx^2$ term is the signature of a parabola.

Why a parabola? Because vertical acceleration is constant. A constant force produces a trajectory whose curvature is constant, giving a conic section. The parabola is what you get when that force is perpendicular to the initial velocity. Tilt the launch angle, and the shape stays parabolic. Change the launch speed, and the width and height change, but the parabola remains.

The word itself comes from Greek: *para* (beside) + *ballein* (to throw). The parabola is the curve of a thrown object.

### Deriving Range and Maximum Height

For a projectile launched at angle $\theta_0$ with initial speed $v_0$, starting and ending at the same height:

**Maximum height** occurs when vertical velocity becomes zero. Using $v_y^2 = v_{0y}^2 - 2g(y - y_0)$ with $v_y = 0$:
$$h = \frac{(v_0 \sin \theta_0)^2}{2g}$$

Higher launch angle means higher vertical component, so higher maximum height. A projectile launched at 75° reaches much higher than one launched at 15°, even at the same speed.

**Time of flight** for launch and landing at the same height. Set $y - y_0 = 0$:
$$0 = v_{0y} t - \frac{1}{2}gt^2 = (v_0 \sin \theta_0)t - \frac{1}{2}gt^2$$

Factor out $t$:
$$t\left(v_0 \sin \theta_0 - \frac{1}{2}gt\right) = 0$$

The non-trivial solution:
$$T_{\text{tof}} = \frac{2v_0 \sin \theta_0}{g}$$

Notice: time in the air depends only on the vertical component of velocity. A projectile launched horizontally at 15 m/s from a 100-meter cliff spends the same time falling as one launched at 45° — the vertical component differs, but if both fall 100 meters, the time is determined by gravity and height alone.

**Range** — horizontal distance traveled while airborne. Horizontal distance is:
$$R = v_{0x} \times T_{\text{tof}} = (v_0 \cos \theta_0) \times \frac{2v_0 \sin \theta_0}{g}$$

Using the identity $2 \sin \theta \cos \theta = \sin 2\theta$:
$$R = \frac{v_0^2 \sin 2\theta_0}{g}$$

The maximum range occurs when $\sin 2\theta_0 = 1$, which means $2\theta_0 = 90°$, so $\theta_0 = 45°$. At 45°, you get the most horizontal distance for a given launch speed. But here is an important trade-off: two different angles give the same range. Launch at 30° and at 60°, and you travel the same horizontal distance. The 30° shot lands faster and flatter; the 60° shot takes longer and reaches higher. Both cover the same ground.

### The Trade-off: Neglecting Air Resistance

The parabolic trajectory is beautiful and computable. It is also wrong. The moment a projectile is in the air, drag acts on it. For a baseball, drag removes about 10% of the range compared to the ideal parabola. For a rifle bullet, the effect is smaller (higher speed, lower drag relative to momentum). For a golf ball, drag and the Magnus force (from spin) dominate the trajectory completely — a golf ball does not follow a parabola.

Real trajectories are lower and shorter than the mathematics predicts. This is why artillery officers in the field use ballistic tables, not formulas. The formula gets you close, but air resistance wins for any object moving slow enough that we can throw it.

The trade-off is this: the independence assumption (gravity only) buys us a closed-form solution we can compute by hand and understand in its entirety. Air resistance is real, but it costs us the ability to solve the equation. We gain clarity at the expense of accuracy.

### Worked Example: A Tennis Player's Return

A tennis player at the baseline hits a ball at 30 m/s from a height of 2.5 meters, angled 45° above the horizontal. The ball must land inside the opposite baseline, 23.8 meters away. Does it make the shot?

**Initial velocity components:**
$$v_{0x} = 30 \cos(45°) = 21.2\,\text{m/s}$$
$$v_{0y} = 30 \sin(45°) = 21.2\,\text{m/s}$$

**Time to travel 23.8 meters horizontally:**
$$x = v_{0x} t$$
$$23.8 = 21.2 \times t$$
$$t = 1.12\,\text{s}$$

**Height at that time:**
$$y = 2.5 + 21.2(1.12) - \frac{1}{2}(9.8)(1.12)^2$$
$$= 2.5 + 23.7 - 6.15$$
$$= 20.1\,\text{m}$$

The ball is 20.1 meters above the ground when it reaches the baseline. The net is 0.914 meters high at the baseline. The ball clears the net by a huge margin — it's still rising. The serve lands well inside, and likely goes long unless the player has a spin or topspin that brings it down.

### Common Misconception

Students often think that horizontal and vertical motion must somehow "coordinate" — that if a projectile travels a certain horizontal distance, it must land at a certain height. The independence principle says this is false. Horizontal distance depends on time in the air. Time in the air depends only on vertical motion. Vertical motion depends on gravity and initial vertical velocity, not on horizontal velocity at all. This is why a ball dropped from a moving vehicle and a ball thrown from the same vehicle hit the ground at the same time, regardless of the vehicle's speed (ignoring air resistance). The horizontal velocity has no say in when the vertical journey ends.

---

## Concept 3: Circular Motion and Centripetal Acceleration

### The Mechanism: Constant Speed, Changing Velocity

A second hand of a clock moves at constant speed around the clock face. Its velocity is not constant. This seems to contradict the definition: constant velocity means zero acceleration, right?

No. Velocity is a vector. Speed is the magnitude. A second hand has constant speed but its velocity vector is constantly changing direction. Because velocity is changing, there is acceleration — even though the speed never changes.

Here's the geometry. Imagine a particle moving counterclockwise in a circle of radius $r$. At time $t$, it is at angle $\theta = \omega t$, where $\omega$ is the angular frequency (radians per second). Its position is:
$$\vec{r}(t) = r\cos(\omega t)\hat{i} + r\sin(\omega t)\hat{j}$$

The velocity is the derivative:
$$\vec{v}(t) = -r\omega\sin(\omega t)\hat{i} + r\omega\cos(\omega t)\hat{j}$$

The magnitude of velocity is:
$$|\vec{v}| = r\omega\sqrt{\sin^2(\omega t) + \cos^2(\omega t)} = r\omega$$

This is constant. The speed is $v = r\omega$.

But the direction of $\vec{v}$ is constantly rotating. At time $t$, the velocity points in the direction of angle $\omega t + 90°$ — always perpendicular to the radius, always tangent to the circle. As the particle moves, this tangent direction rotates.

The acceleration is the derivative of velocity:
$$\vec{a}(t) = -r\omega^2\cos(\omega t)\hat{i} - r\omega^2\sin(\omega t)\hat{j}$$

Rewrite this:
$$\vec{a}(t) = -\omega^2[r\cos(\omega t)\hat{i} + r\sin(\omega t)\hat{j}] = -\omega^2\vec{r}(t)$$

The acceleration points toward the center (the negative sign) and has magnitude:
$$a_c = r\omega^2$$

But $v = r\omega$, so $\omega = v/r$:
$$a_c = r\left(\frac{v}{r}\right)^2 = \frac{v^2}{r}$$

This is the centripetal acceleration — the center-seeking acceleration. It is always perpendicular to the velocity, always pointing toward the center of the circle, always with magnitude $v^2/r$.

The word *centripetal* comes from Latin: *centrum* (center) + *petere* (to seek). The acceleration seeks the center.

Why does the acceleration have magnitude $v^2/r$? Because a tighter circle (smaller $r$) requires a faster change in direction (larger acceleration for the same speed). And a faster motion (larger $v$) also requires a faster change in direction. The $v^2$ in the numerator captures both effects: you are changing direction at a rate proportional to your speed, and the faster you move, the faster you need to change. The $r$ in the denominator is the tightness of the turn.

### The Trade-off: Uniform vs. Nonuniform Circular Motion

Uniform circular motion — constant speed, circle of fixed radius — has only centripetal acceleration. The speed never changes, so there is no tangential component of acceleration.

Real circular motion is rarely uniform. A car entering a turn slows down. A spinning top speeds up or slows down. When the speed changes, there is tangential acceleration — acceleration along the direction of motion, speeding up or slowing down the object.

The total acceleration in nonuniform circular motion is the vector sum:
$$\vec{a}_{\text{total}} = \vec{a}_c + \vec{a}_T$$

where $a_c$ is centripetal (radial, toward center) and $a_T$ is tangential (along the direction of motion). These are perpendicular to each other. The total acceleration points somewhere between the radial and tangential directions. If you are turning hard and slowing down simultaneously, you feel both accelerations — the sideways push of the turn and the backward push of the brakes.

The trade-off: uniform circular motion is solvable. We know the position at all times, the velocity, the acceleration — everything is predictable. Nonuniform circular motion requires us to know how the speed changes, and then we must solve two coupled differential equations (one for speed change, one for position on the circle). Most real-world circular motion is nonuniform, which is why modern physics problems often specify either that speed is constant (for simplicity) or give the speed as a function of time (so we can compute the motion).

### Worked Example: A Jet in a Barrel Roll

A military jet flying at 134 m/s (about 480 km/h) executes a barrel roll — a maneuver where the jet follows a helical path, turning in a vertical circle. To produce a centripetal acceleration of 1 *g* (9.8 m/s²) on the pilot, what must the radius of the turn be?

**Setup:**
$$a_c = \frac{v^2}{r}$$

We want $a_c = 9.8$ m/s². Solving for $r$:
$$r = \frac{v^2}{a_c} = \frac{(134)^2}{9.8} = \frac{17,956}{9.8} = 1,833\,\text{m}$$

The jet must follow a circle of radius 1,833 meters — nearly 2 kilometers. At this radius and speed, the pilot experiences a centripetal acceleration of 1 *g*, the same as gravity at Earth's surface.

Combat jets can pull 5 to 8 *g* of acceleration. At 8 *g$:
$$r = \frac{17,956}{78.4} = 229\,\text{m}$$

A much tighter turn. The jet follows a circle just 229 meters in radius, so tight that at a speed of 134 m/s, the pilot feels like eight times normal gravity is pushing them sideways into their seat.

The trade-off: flying tighter turns requires less time to circle, but it also requires extreme acceleration. Higher *g* loads damage human tissue and can cause the pilot to black out (blood drains from the brain due to the acceleration). Planes designed for 8 *g* turns carry specialized seating and G-suits that compress the pilot's body to keep blood in the head. Faster speeds at the same radius produce even more centripetal acceleration, so a jet flying at 200 m/s in a 229-meter circle pulls about 18 *g* — lethal without specialized equipment.

### Common Misconception

Students often confuse centripetal force with centrifugal force. In classical mechanics, there is no centrifugal force — it is a fictitious force that appears only in rotating reference frames. In the inertial (non-rotating) reference frame, the only real force is centripetal, pointing toward the center, causing the acceleration toward the center. The object does not want to move outward; it wants to move in a straight line (Newton's first law). The centripetal force constantly curves its path. In a rotating reference frame (the frame of the spinning object), a fictitious centrifugal force appears, pointing outward, to explain why objects seem to press outward. Both descriptions are consistent, but in an inertial frame, centripetal is real and centrifugal is an artifact of the frame choice.

---

## Concept 4: Relative Motion — Velocities Depend on the Observer

### The Mechanism: Velocity Addition in Multiple Frames

You are on a train moving east at 10 m/s relative to the ground. Inside the train, you walk forward (toward the front, which is the direction of motion) at 2 m/s relative to the train. How fast are you moving relative to the ground?

Your velocity relative to the ground is the vector sum of your velocity relative to the train and the train's velocity relative to the ground:
$$\vec{v}_{\text{you, ground}} = \vec{v}_{\text{you, train}} + \vec{v}_{\text{train, ground}}$$
$$= 2 + 10 = 12\,\text{m/s east}$$

Now, another train passes in the opposite direction, moving west at 15 m/s relative to the ground (so its velocity is −15 m/s in the eastward direction). From the perspective of passengers on the other train, how fast is the ground moving? It is:
$$\vec{v}_{\text{ground, other train}} = -\vec{v}_{\text{other train, ground}} = -(-15) = 15\,\text{m/s east}$$

(The negative sign flips the direction when we reverse the reference frame.)

From the perspective of the other train, you on the first train are moving at:
$$\vec{v}_{\text{you, other train}} = \vec{v}_{\text{you, ground}} + \vec{v}_{\text{ground, other train}}$$
$$= 12 + 15 = 27\,\text{m/s east}$$

You appear to be zooming away at 27 m/s — much faster than your ground speed of 12 m/s — because the other train is moving toward you at 15 m/s, adding to your apparent speed.

**The key subscript order.** When we write $\vec{v}_{AB}$, we mean the velocity of object A as measured by observer B. The subscripts tell the story: the first is what is moving, the second is the reference frame. The relative velocity equation always chains: to get $\vec{v}_{AC}$ (A's velocity relative to C), you add $\vec{v}_{AB}$ (A's velocity relative to B) and $\vec{v}_{BC}$ (B's velocity relative to C). The middle subscript disappears when you add:

$$\vec{v}_{AC} = \vec{v}_{AB} + \vec{v}_{BC}$$

This is Galilean relativity. For speeds much slower than the speed of light, velocities add like vectors. (At speeds close to light, Einstein's special relativity replaces this with a more complex rule.)

### Deriving the Two-Frame Velocity Transformation

We have two observers in different reference frames, S and S′, moving relative to each other at velocity $\vec{v}_{S'S}$ (the velocity of frame S′ relative to frame S).

A particle P has velocity $\vec{v}_{PS}$ as measured in frame S, and velocity $\vec{v}_{PS'}$ as measured in frame S′.

The position of P in frame S is related to its position in frame S′ by:
$$\vec{r}_{PS} = \vec{r}_{PS'} + \vec{r}_{S'S}$$

(The position of P in S is the position of P relative to S′, plus the position of S′ relative to S.)

Taking the time derivative:
$$\frac{d\vec{r}_{PS}}{dt} = \frac{d\vec{r}_{PS'}}{dt} + \frac{d\vec{r}_{S'S}}{dt}$$

$$\vec{v}_{PS} = \vec{v}_{PS'} + \vec{v}_{S'S}$$

This is the velocity addition rule for two frames. And taking the derivative again:
$$\vec{a}_{PS} = \vec{a}_{PS'} + \vec{a}_{S'S}$$

Here is something profound: if S′ moves at constant velocity relative to S, then $\vec{a}_{S'S} = 0$, so:
$$\vec{a}_{PS} = \vec{a}_{PS'}$$

Two observers in constant relative motion measure the same accelerations. This is the principle behind inertial frames in classical mechanics. The laws of Newton are the same in any frame moving at constant velocity.

### The Trade-off: Inertial vs. Accelerating Frames

If one frame is accelerating relative to another, the velocities no longer add simply. Worse, physics itself looks different. In an accelerating frame, fictitious forces appear (like centrifugal force in a rotating frame). The equations of motion must be rewritten. Newton's laws are no longer valid without modification.

For simplicity, we restrict ourselves to inertial frames — frames moving at constant velocity relative to each other. Within this restriction, physics is consistent and straightforward. We gain the beauty of Newtonian mechanics. We lose the ability to describe physics in accelerating frames without additional machinery (fictitious forces, or moving to the full General Relativity).

### Worked Example: A Boat Crossing a River

A boat can move at 4.5 m/s in still water. The river flows east at 3.0 m/s. The boat wants to cross due north — to travel perpendicular to the current. In what direction must the boat point its bow?

**Setup.** Let B = boat, W = water, G = ground. We want:
$$\vec{v}_{BG} = \vec{v}_{BW} + \vec{v}_{WG}$$

We know:
- $|\vec{v}_{BW}| = 4.5$ m/s (boat's speed in water)
- $\vec{v}_{WG} = 3.0\,\hat{i}$ m/s (water velocity relative to ground is 3.0 m/s east)
- $\vec{v}_{BG}$ points north: $\vec{v}_{BG} = v_{BG}\,\hat{j}$ (we don't know the magnitude yet)

We need to find the direction of $\vec{v}_{BW}$ such that when we add $\vec{v}_{WG}$, the east component cancels.

Let the boat point at angle $\theta$ west of north. Then:
$$\vec{v}_{BW} = -4.5\sin\theta\,\hat{i} + 4.5\cos\theta\,\hat{j}$$

(Negative $x$ because west is negative, positive $y$ because north is positive.)

The sum must have zero east component:
$$-4.5\sin\theta + 3.0 = 0$$
$$\sin\theta = \frac{3.0}{4.5} = \frac{2}{3}$$
$$\theta = \arcsin(2/3) = 41.8°$$

So the boat must point 41.8° west of north.

The ground velocity (northward only) is:
$$v_{BG} = 4.5\cos\theta = 4.5\cos(41.8°) = 4.5 \times 0.745 = 3.35\,\text{m/s}$$

The boat moves north at 3.35 m/s relative to the ground, while pointing northwest at an angle. The water current carries the boat downstream, but the boat's angle compensates, resulting in a purely northward motion relative to the ground.

---

## Integration: The Picture Emerges

We now understand four layers of motion in multiple dimensions.

The first is the kinematic layer: position, velocity, and acceleration as vectors. These are the raw descriptions of motion. They are separable — we can treat each component independently because forces in different directions don't interfere.

The second is projectile motion: the special case where gravity is the only force, acting downward. This produces parabolic trajectories, and we can compute range, height, and time with closed-form equations.

The third is circular motion: motion along a curved path at constant speed. Even though speed is constant, velocity changes direction, so there is acceleration toward the center. This centripetal acceleration has magnitude $v^2/r$.

The fourth is relative motion: the observation that velocities are frame-dependent. An object moving at one speed relative to one observer may move at a different speed relative to another observer. Velocities add according to Galilean relativity. Accelerations are the same in any two frames moving at constant velocity relative to each other.

Integrated, these ideas let us solve problems like: *A rocket is launched from an aircraft carrier moving northeast at 10 m/s. The rocket is launched at 300 m/s relative to the carrier, at an angle of 30° above horizontal. How long is it in the air, and where does it land relative to the launch point and relative to the carrier?*

You would transform to the carrier frame, compute the parabolic trajectory, find the landing time and position, then transform back to the ground frame using relative motion. Each piece uses one of the four layers. Together, they solve the full three-dimensional problem.

---

## Graduated Exercises

### Warm-up

1. A particle's position is $\vec{r}(t) = (5.0t + 2.0)\hat{i} + (3.0t^2)\hat{j}$ meters. Find its velocity at $t = 1.0$ s and acceleration at all times. Is the acceleration constant?

2. A baseball is thrown horizontally at 20 m/s from a 50-meter-high building. How long is it in the air? How far from the base of the building does it land?

3. A car enters a circular turn of radius 50 meters at a constant speed of 20 m/s. What is the magnitude of the centripetal acceleration?

### Application

4. A projectile is launched at 40 m/s from ground level at an angle of 60°. (a) Find the maximum height. (b) Find the range. (c) Find the time in the air.

5. Two reference frames S and S′ have a relative velocity of $\vec{v}_{S'S} = 5.0\,\hat{i}$ m/s. A particle has velocity $\vec{v}_{PS} = 8.0\,\hat{i} + 3.0\,\hat{j}$ m/s in frame S. Find its velocity in frame S′.

6. A boat heads due north at 6.0 m/s relative to the water. The river current is 2.0 m/s due east. What is the boat's velocity relative to the ground? (Give magnitude and direction.)

### Synthesis

7. A rock is thrown from a cliff 100 meters high at an angle of 37° above the horizontal with an initial speed of 30 m/s. It lands on a slope that descends at 20° below the horizontal. How far along the slope does the rock travel before impact?

8. A satellite orbits Earth at a constant altitude, moving at constant speed $v$ in a circle of radius $r$. Derive the relationship between the period of orbit $T$, the radius $r$, and the speed $v$. If the radius doubles, how does the period change? (You will need the fact that centripetal force equals the gravitational force, which you will study in later chapters.)

### Challenge

9. Two cars approach an intersection. Car A travels east at 20 m/s; Car B travels north at 15 m/s. (a) What is Car B's velocity relative to Car A? (b) At the moment Car A is 40 meters west of the intersection and Car B is 30 meters south, how fast are they approaching each other (rate of change of distance)?

10. A gymnast performs a backflip, leaving the ground at 3.0 m/s, angled 30° above horizontal. The gymnast must land on a mat that starts 0.5 meters away and extends to 2.0 meters away. (a) How long is the gymnast in the air? (b) How far does she travel horizontally? (c) Does she land on the mat? If so, where?

---

## Chapter Summary

Motion in two and three dimensions is governed by the same principles as motion in one dimension, applied to each perpendicular direction independently. Gravity pulls only downward, making horizontal and vertical motions separate one-dimensional problems.

Projectile motion — motion under gravity alone, with no air resistance — produces parabolic trajectories. The range $R$, maximum height $h$, and time of flight $T$ can all be computed from the initial velocity and launch angle using closed-form equations. Real projectiles experience air drag, which reduces range and height compared to predictions.

Circular motion at constant speed has constant velocity magnitude but changing direction, producing a centripetal acceleration of magnitude $a_c = v^2/r$, always pointing toward the center. Nonuniform circular motion adds tangential acceleration, which changes the speed.

Velocities are reference-frame dependent. Two observers in constant relative motion measure different velocities for the same object, but they add according to $\vec{v}_{AC} = \vec{v}_{AB} + \vec{v}_{BC}$. Accelerations are the same in all frames moving at constant velocity relative to each other (inertial frames).

---

## What Would Change My Mind

I have assumed throughout that air resistance is negligible. If a student or colleague presented strong evidence that the parabolic trajectory is fundamentally wrong for all practical projectiles — that drag is so dominant even for low-speed throws that the parabola is useless as a teaching model — I would reconsider the emphasis on the ideal case. But since parabolic trajectories match actual trajectories to within 10–15% for typical sports scenarios (and much better for fast projectiles like bullets), I find the model defensible as a first approximation.

---

## Still Puzzling

I don't fully understand why the independence principle (separation of perpendicular motions) is so robust. It works perfectly for gravity (a uniform field), but I have not yet worked through the mathematics of whether it would hold for other force configurations. What is the deep reason that perpendicular components decouple?

---

## Tags

vector kinematics, projectile motion, circular motion, centripetal acceleration, relative velocity, Galilean relativity, parabola, trajectory, reference frames, two-dimensional motion, three-dimensional motion

---

## Key Equations

**Position, velocity, acceleration vectors:**
$$\vec{r}(t) = x(t)\hat{i} + y(t)\hat{j} + z(t)\hat{k}$$
$$\vec{v}(t) = \frac{d\vec{r}}{dt} = v_x(t)\hat{i} + v_y(t)\hat{j} + v_z(t)\hat{k}$$
$$\vec{a}(t) = \frac{d\vec{v}}{dt} = a_x(t)\hat{i} + a_y(t)\hat{j} + a_z(t)\hat{k}$$

**Projectile motion (with constant acceleration $a_y = -g$, $a_x = 0$):**
$$T_{\text{tof}} = \frac{2v_0\sin\theta_0}{g}$$
$$R = \frac{v_0^2\sin 2\theta_0}{g}$$
$$h = \frac{(v_0\sin\theta_0)^2}{2g}$$
$$y = (x\tan\theta_0) - \frac{gx^2}{2(v_0\cos\theta_0)^2}$$

**Centripetal acceleration (uniform circular motion):**
$$a_c = \frac{v^2}{r} = \omega^2 r$$

**Relative velocity (Galilean):**
$$\vec{v}_{AC} = \vec{v}_{AB} + \vec{v}_{BC}$$
$$\vec{a}_{AC} = \vec{a}_{AB}$$ (if frames S and S′ have constant relative velocity)


---

## LLM Exercise — Chapter 5: Projectile and Circular Motion in 3D

**Project:** *Physics Simulation Toolkit*.

**What you're building this chapter:** Generalize the Ch 4 integrators to 3D vectors, simulate projectile motion (with and without drag) and uniform circular motion, and verify the analytical results.

**Tool:** Claude Code.

**The prompt:**

```
Chapter 5 task in the physics-simulation-toolkit. The chapter
generalized kinematics to vectors and covered projectile motion,
uniform circular motion, and relative motion. Lift the Ch 4
integrators into 3D and verify each canonical case.

In `chapters/ch05_motion_3d/`:

1. `simulations.py`:
   - `projectile_no_drag(v0_vec, angle_rad, mass)` — analytical
     trajectory: range, max height, time of flight.
   - `projectile_with_drag(v0_vec, angle_rad, mass, drag_coeff,
     area, air_density)` — numerical simulation using your Ch 4 RK4,
     drag force = -0.5 * rho * v * |v| * Cd * A.
   - `uniform_circular_motion(radius, angular_velocity, t)` — analytical
     position, velocity, centripetal acceleration; numerical
     verification via RK4 with the centripetal force prescribed.
   - `relative_velocity(v_A_in_ground, v_B_in_ground)` — boat-in-river
     and plane-in-wind frame transforms.

2. `test_simulations.py`:
   - No-drag projectile: 45° launch maximizes range; the analytical
     range $v_0^2 / g$ matches RK4 simulation to high precision.
   - Drag projectile: with realistic baseball parameters (drag coeff
     ~0.3, mass 0.145 kg, diameter 7.4 cm), a 45° launch at 40 m/s
     reaches range ~80% of the no-drag answer (cite the source for
     the typical baseball drag coefficient).
   - Circular motion: period $T = 2\pi/\omega$ measured from
     numerical simulation matches analytical T to better than 0.1%
     for RK4 with dt = T/1000.

3. `benchmarks.py` — for projectile with drag, sweep launch angles
   from 10° to 80° and plot range vs. angle. The optimal angle with
   drag is below 45° (typically 35-40° for baseball-like
   parameters). Verify empirically and report the optimal angle on
   your specific parameter set.

4. `README.md` — three decision cards (projectile, circular,
   relative). "Surprising findings": the optimal-launch-angle shift
   with drag, and how much range is lost compared to no-drag at
   45°.

Commit as `ch05: 3D motion with drag projectile and circular motion
verification`.
```

**What this produces:** Projectile (with/without drag) and circular-motion simulations, the empirical optimal-launch-angle shift due to drag, and conservation-law tests for circular motion.

**How to adapt this prompt:**

- *For your own project:* If you want sport-specific drag, look up Cd as a function of Reynolds number. Baseballs go through a "drag crisis" around 80 mph where Cd drops sharply; modeling this matters.
- *For ChatGPT / Gemini:* Both work. The vector-form drag force $\vec{F}_{\text{drag}} = -\frac{1}{2}\rho C_d A |\vec{v}|\vec{v}$ is easy to mis-sign.
- *For Claude Code:* Native fit. Generate the angle-sweep plot.
- *For a Claude Project:* Not the fit.

**Connection to previous chapters:** Uses Ch 4 integrators (now in 3D), Ch 3 vectors, Ch 2 units.

**Preview of next chapter:** Chapter 6 implements Newton's-laws integrator generically — force functions become first-class, free-body diagrams become testable code structures.


---

## AI Wayback Machine

The physics in this chapter didn't appear from nowhere. **Caroline Herschel** was the systematic comet-hunting program at her brother William's observatory, leading to the discovery of eight comets and dozens of nebulae — and the first salary paid by the British crown to a woman as a scientist (1787, £50/year for her astronomical work) — and despite the substance of the work, the name is far less recognized than it deserves. Here's a prompt to find out more — and then make it better.

**Run this:**

```
Who was Caroline Herschel, and how does their work on the discovery and orbital tracking of comets and their characterization as gravitating bodies connect to motion in two and three dimensions, especially orbital motion? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Caroline Herschel"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to describe Herschel's specific 1786 discovery of her first comet — the observation conditions, the calculation method, the priority dispute (if any) with other comet-hunters
- Ask: "Herschel was the first woman to receive a salary as a scientist in Britain, and the first woman elected to the Royal Astronomical Society (in 1835 alongside Mary Somerville). What did each milestone require of her, and what did each *not* yet open?"
- Add the constraint: "Answer using at least one specific entry from Herschel's 1786–1797 observational notebooks, with the date and the celestial coordinates"

What changes? What gets better? What gets worse?
