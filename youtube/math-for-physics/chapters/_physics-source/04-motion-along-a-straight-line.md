# Motion Along a Straight Line

## Suggested Titles

1. **How Things Move: From Falling Skydivers to Stopping Cars**
2. **One Dimension, Three Relationships: Position, Velocity, and Acceleration**
3. **Kinematics Without Apology: The Calculus of How Things Move**

## TL;DR

When an object moves in one dimension, its position changes over time. The rate of that change—velocity—is the derivative of position; the rate at which velocity changes—acceleration—is the derivative of velocity. These three quantities are bound together by calculus, not by memorization.

---

On October 14, 2012, Felix Baumgartner stood in a capsule suspended from a weather balloon at 38,969 meters above the New Mexico desert. A few hours' climb—up past the altitude where commercial jets cruise, past where the sky turns dark purple, into air so thin that 99.97 percent of Earth's atmosphere lay below him. When the doors opened, he stepped out.

For the first 30 seconds, Baumgartner was not falling fast. Free fall is not an instant condition; it's a state that builds. He accelerated downward at 9.8 meters per second every second—a constant acceleration that Earth's gravity provides equally to all objects in the absence of air resistance. But Baumgartner was falling from the edge of the thermosphere. The air density around him—what there was of it—was so negligible that he could, mathematically, pretend it wasn't there.

By 34 seconds into the jump, he was moving faster than sound. By 4 minutes 19 seconds, he had completed the jump and deployed his parachute. In that window, we see the entire machinery of one-dimensional kinematics: a starting position, a constant acceleration, a time interval, and an ending position and velocity. The mathematics that describes Baumgartner's descent is the same mathematics that describes a sprinter leaving the starting blocks, a car braking to a stop, or a ball thrown upward returning to the thrower's hand.

Kinematics is the description of motion without concern for what causes it. We will examine the causes—forces—in later chapters. For now, we focus on the description itself: the three quantities that characterize motion in one dimension, the relationships among them, and the equations that connect them.

### Learning Objectives

After working through this chapter, you will be able to:

- Distinguish between position, displacement, distance traveled, and the relationships among them
- Calculate instantaneous velocity from position as a function of time using calculus
- Calculate instantaneous acceleration from velocity as a function of time
- Apply the kinematic equations for motion with constant acceleration
- Solve free-fall problems where gravity provides the constant acceleration
- Use integral calculus to reconstruct position and velocity from an acceleration function

### Prerequisites

- Comfort with algebra: solving for unknowns, working with exponents
- Calculus I: the definitions of derivatives and integrals, the power rule for differentiation
- Geometry and trigonometry: the Pythagorean theorem, basic angle relationships
- Comfort with SI units and dimensional consistency

---

## Concept 1: Position, Velocity, and Acceleration—The Three Pillars

### The Opening Puzzle

Watch a runner leaving the blocks in a 100-meter race. At the instant the gun fires, the runner's position is zero. Tenths of a second later, the runner has moved a few meters and is moving faster than before. A few more tenths of a second, and the runner is slowing down (no longer accelerating at the same rate), coasting toward a maximum speed. The photo finish will be decided by tenths of a second—a difference in *position* at a particular *time*.

But here's the puzzle: How is the runner's position at the finish line connected to how fast the runner was accelerating at the start? Why does a change in acceleration early in the race affect where the runner ends up? To answer these questions, we need three quantities and the relationships among them.

### Specification: What We Actually Mean

**Position** (*x* or *y*) is the location of an object at a particular instant, measured along a line from some chosen origin. Position is a number with a sign: +5 meters means 5 meters to the right of the origin; −5 meters means 5 meters to the left. The choice of origin is arbitrary—we pick it for convenience. A runner's position might be measured from the starting line, the finish line, or any other point we choose.

**Displacement** (Δ*x*) is the *change* in position: the difference between where the object is now and where it was before. If a cyclist starts at position *x*₀ = 0 and ends at position *x* = 15 meters, the displacement is Δ*x* = 15 − 0 = 15 meters, regardless of what path was taken to get there. Displacement has both magnitude and direction, making it a vector. A negative displacement means the object moved in the negative direction.

**Distance traveled** is different from displacement. If that same cyclist rides 10 meters north, then 10 meters south, the displacement is zero (net change from start to finish), but the distance traveled is 20 meters (total length of the path). Displacement cares about *where you end up*; distance cares about *how much ground you covered*.

**Velocity** (*v*) describes how fast something is moving *and* in which direction. We distinguish between **average velocity** and **instantaneous velocity**.

- *Average velocity* is displacement divided by the time interval: $\bar{v} = \frac{\Delta x}{\Delta t}$. Over a 10-second interval, if you cover 50 meters, your average velocity is 5 m/s.
- *Instantaneous velocity* is the velocity at one specific moment. To find it, we take the limit of average velocity as the time interval shrinks to zero—exactly the definition of a derivative:

$$v(t) = \lim_{\Delta t \to 0} \frac{x(t + \Delta t) - x(t)}{\Delta t} = \frac{dx}{dt}$$

This is not just a formula to memorize. It is the statement that velocity is the *rate of change of position*. If you know the position as a function of time, *x*(*t*), you can find velocity by taking its derivative.

**Speed** is the magnitude of velocity. If you're traveling at +7 m/s (eastward) or −7 m/s (westward), your speed is 7 m/s in both cases. Speed is always positive.

**Acceleration** (*a*) is the rate of change of velocity. Just as velocity is the derivative of position, acceleration is the derivative of velocity:

$$a(t) = \frac{dv}{dt} = \frac{d^2x}{dt^2}$$

Acceleration is the second derivative of position. An acceleration of 3 m/s² means the velocity increases by 3 m/s every second. Acceleration has a direction: positive acceleration might mean you're speeding up in the positive direction or slowing down in the negative direction, depending on the sign of the velocity.

Here is the critical insight: these three quantities—position, velocity, acceleration—are not independent. They are related by differentiation and integration. If you know one, you can find the others.

### The Mechanism: Calculus in One Dimension

Let's derive the key relationship. Suppose a particle has a position function:

$$x(t) = 2t^2 + 3t \text{ (in meters, with time in seconds)}$$

Taking the derivative:

$$v(t) = \frac{dx}{dt} = 4t + 3 \text{ (m/s)}$$

At *t* = 0, the particle is at position *x* = 0 with velocity *v* = 3 m/s. At *t* = 1 s, the particle is at *x* = 5 m with velocity *v* = 7 m/s. The position increased by 5 meters, and the velocity increased by 4 m/s.

Taking the derivative of velocity:

$$a(t) = \frac{dv}{dt} = 4 \text{ m/s}^2$$

The acceleration is constant—it does not change with time. This means the velocity is increasing at a steady rate.

Now go backward. Suppose we know only the acceleration: *a*(*t*) = 4 m/s². To find velocity, we integrate:

$$v(t) = \int a(t) \, dt = \int 4 \, dt = 4t + C_1$$

The constant of integration *C₁* is determined by the initial condition. If *v*(0) = 3 m/s, then *C₁* = 3, and:

$$v(t) = 4t + 3 \text{ m/s}$$

To find position, we integrate velocity:

$$x(t) = \int v(t) \, dt = \int (4t + 3) \, dt = 2t^2 + 3t + C_2$$

If *x*(0) = 0, then *C₂* = 0, and:

$$x(t) = 2t^2 + 3t \text{ m}$$

We have reconstructed the original functions. The lesson: differentiation and integration are inverse operations. One describes how position changes (giving velocity); the other reconstructs position from velocity.

### The Trade-Off: Specificity Versus Generality

In one-dimensional kinematics, we simplify by assuming motion along a single axis—call it *x* or *y*. In the real world, objects move in three dimensions. A falling ball, affected by wind, moves not just downward but also sideways. We treat that in a later chapter. For now, the restriction to one dimension allows us to focus on the core relationships without the complication of vector components.

The restriction also assumes that we can treat displacement, velocity, and acceleration as signed scalars. A velocity of −10 m/s is perfectly well-defined—it just means motion in the negative direction. This works as long as we are careful about signs and what they mean in our chosen coordinate system.

A second trade-off appears when we encounter real motion. Real objects do not have constant acceleration indefinitely. A car accelerates to a maximum speed and then maintains that speed, or begins to brake. A falling object encounters air resistance, which increases with speed, so the acceleration decreases over time. When these complications arise, we often break the motion into segments, each with its own (approximately) constant acceleration, and apply the kinematic equations separately to each segment.

### Worked Example: The Skydiver Revisited

Let's model Felix Baumgartner's initial descent from the capsule at 39 km altitude, where air resistance can be neglected (we'll refine this later).

At the moment he steps out:
- Position: *y* = 39,000 m (measured from sea level, with up as positive)
- Velocity: *v₀* = 0 m/s (he steps out, not jumps)
- Acceleration: *a* = −9.8 m/s² (gravity pulls downward)

After 10 seconds:
- Velocity: $v(10) = 0 + (-9.8)(10) = -98$ m/s (moving downward at 98 m/s)
- Position: $y(10) = 39000 + 0(10) + \frac{1}{2}(-9.8)(10)^2 = 39000 - 490 = 38,510$ m

After 30 seconds:
- Velocity: $v(30) = 0 + (-9.8)(30) = -294$ m/s (moving downward at 294 m/s, or about 660 mph)
- Position: $y(30) = 39000 + 0 + \frac{1}{2}(-9.8)(30)^2 = 39000 - 4410 = 34,590$ m

Note the asymmetry: in the first 10 seconds, Baumgartner fell 490 m. In the second 10 seconds (from *t* = 10 to *t* = 20), the fall distance was much larger because the starting velocity was higher. This is the consequence of the $t^2$ term in the position equation.

#### Common Misconception: "Constant Acceleration Means Constant Velocity"

This is false. Constant acceleration means the velocity is *changing at a constant rate*. A car with an acceleration of 3 m/s² is speeding up—its velocity increases by 3 m/s every second. After 1 second, it's moving 3 m/s faster than it was before. The velocity is not constant; the rate of change of velocity is constant.

---

## Concept 2: Deriving Kinematic Equations from Calculus

### The Opening Puzzle

You're driving a car at a constant acceleration. You know your initial velocity, the acceleration, and how long you've been accelerating. What is your final velocity? What distance have you covered? These questions demand equations—but where do they come from? Many textbooks present four "kinematic equations" as though they fell from the sky. We will derive them instead, from the definitions of velocity and acceleration.

### Specification: The Assumptions We Make

All the equations we derive in this section assume **constant acceleration**. This is a powerful assumption because it simplifies the calculus dramatically. Instead of integrating a complex acceleration function *a*(*t*), we integrate a constant: *a*(*t*) = *a*. 

Constant acceleration occurs in several real situations:
- An object in free fall near Earth's surface (gravity provides *a* = −*g*)
- A car with its foot on the accelerator or brake, moving in a straight line
- Any situation where the net force is constant

We also adopt simplified notation. We set the initial time to *t₀* = 0 (start the stopwatch when the motion begins) and denote initial position as *x₀*, initial velocity as *v₀*, final position as *x*, and final velocity as *v*. This removes subscripts clutter and makes the equations cleaner.

### The Mechanism: Building the Four Kinematic Equations

**Equation 1: Final Velocity from Acceleration and Time**

We start with the definition of acceleration:

$$a = \frac{\Delta v}{\Delta t} = \frac{v - v_0}{t}$$

Solving for *v*:

$$\boxed{v = v_0 + at}$$

This is the first kinematic equation. It tells us that final velocity is the initial velocity plus the change in velocity (acceleration times time).

**Equation 2: Average Velocity Under Constant Acceleration**

When acceleration is constant, the velocity increases linearly with time. A graph of *v* versus *t* is a straight line. The average velocity over the time interval is the midpoint of that line:

$$\bar{v} = \frac{v_0 + v}{2}$$

**Equation 3: Displacement from Average Velocity**

We know that displacement is average velocity times time:

$$\Delta x = \bar{v} t = \frac{v_0 + v}{2} t$$

Substituting our expression for average velocity:

$$x - x_0 = \frac{v_0 + v}{2} t$$

$$\boxed{x = x_0 + \frac{v_0 + v}{2} t}$$

This equation relates displacement to the average of the initial and final velocities.

**Equation 4: Displacement from Initial Velocity, Acceleration, and Time**

We can eliminate the final velocity from the previous equation by substituting $v = v_0 + at$:

$$x = x_0 + \frac{v_0 + (v_0 + at)}{2} t = x_0 + \frac{2v_0 + at}{2} t$$

$$x = x_0 + v_0 t + \frac{1}{2} at^2$$

$$\boxed{x = x_0 + v_0 t + \frac{1}{2}at^2}$$

This is perhaps the most frequently used kinematic equation. It tells us displacement without knowing the final velocity.

**Equation 5: Final Velocity from Acceleration and Displacement**

From $v = v_0 + at$, we can solve for time: $t = \frac{v - v_0}{a}$. Substituting into $x - x_0 = \frac{v_0 + v}{2} t$:

$$x - x_0 = \frac{v_0 + v}{2} \cdot \frac{v - v_0}{a} = \frac{v^2 - v_0^2}{2a}$$

Solving for *v*²:

$$\boxed{v^2 = v_0^2 + 2a(x - x_0)}$$

This equation relates final velocity to displacement without needing time. It is invaluable when time is unknown but displacement is known.

### The Trade-Off: When to Use Which Equation

Each kinematic equation connects four of the five variables (*x₀*, *v₀*, *v*, *a*, *t*) and omits one. Choose the equation that:
1. Contains the three quantities you know
2. Contains the one quantity you want to find
3. Does not contain the quantity you don't know

For example, if you know *v₀*, *a*, and *t*, but not *v* or *x*, use $x = x_0 + v_0 t + \frac{1}{2}at^2$ to find *x*. If you then need *v*, use $v = v_0 + at$.

### Worked Example: The Stopping Car

A car is traveling at 30.0 m/s (about 67 mph) when the driver sees a red light 64.3 meters ahead and applies the brakes. Assuming constant deceleration of 7.00 m/s², will the car stop before the light?

**Given:**
- *v₀* = 30.0 m/s
- *x* − *x₀* = 64.3 m (distance to the light)
- *a* = −7.00 m/s² (negative because it opposes motion)
- Find: *v* (final velocity when the car reaches the light)

**Solution:**
The equation that connects *v₀*, *a*, displacement, and *v* without needing time is:

$$v^2 = v_0^2 + 2a(x - x_0)$$

$$v^2 = (30.0)^2 + 2(-7.00)(64.3) = 900 - 900.2 = -0.2 \text{ m}^2/\text{s}^2$$

The result is negative, which is impossible for *v*². This tells us the car comes to a complete stop *before* reaching the light. The car will stop in a distance of:

$$0 = v_0^2 + 2a \Delta x$$

$$\Delta x = -\frac{v_0^2}{2a} = -\frac{900}{2(-7.00)} = 64.3 \text{ m}$$

Wait—that's exactly the distance to the light. Let me recalculate: $-900 / (-14) = 64.3$ m. The car stops exactly at the light (within rounding error). A reaction time of even a fraction of a second would result in a collision.

#### Common Misconception: "The Kinematic Equations Only Work for Constant Acceleration"

This is true. When acceleration changes with time, you must return to the calculus—integration and differentiation. The kinematic equations are not universal; they are specific to the case where *a* is constant. For variable acceleration, you either integrate the acceleration function or break the motion into segments of constant acceleration and apply the equations to each segment separately.

---

## Concept 3: Free Fall and the Special Case of Gravity

### The Opening Puzzle

An astronomer and a feather are dropped from rest on the Moon. Both reach the surface at the same time. On Earth, the feather falls much slower. Why? In the absence of air resistance, all objects fall at the same rate regardless of mass. But the feather falls slowly on Earth because of air resistance, not because of gravity itself. When we remove air resistance—in a vacuum, or over small distances where air resistance is negligible—gravity acts equally on all objects, giving them the same acceleration.

### Specification: Free Fall and Its Conditions

**Free fall** is motion under the influence of gravity alone, with no other forces acting (air resistance and friction are negligible). Near Earth's surface, all free-falling objects experience the same acceleration, downward, due to gravity:

$$g = 9.81 \text{ m/s}^2 \approx 9.8 \text{ m/s}^2$$

(More precisely, *g* varies slightly with latitude and altitude, ranging from 9.78 to 9.83 m/s². We use 9.8 m/s² unless specified otherwise.)

The key statement: **In free fall, acceleration is constant**. This means we can apply the kinematic equations directly to free-fall motion.

### The Mechanism: Setting Up the Free-Fall Equations

When analyzing free fall, we choose a coordinate system. Convention dictates the *y*-axis points upward, so gravity points in the negative *y*-direction. This gives:

$$a = -g = -9.8 \text{ m/s}^2$$

Substituting *a* = −*g* into the kinematic equations:

$$v(t) = v_0 - gt$$

$$y(t) = y_0 + v_0 t - \frac{1}{2}gt^2$$

$$v^2 = v_0^2 - 2g(y - y_0)$$

These three equations describe all one-dimensional motion near Earth's surface where air resistance is negligible.

A critical point: **g is always positive** (9.8 m/s²). The negative sign appears in the equations because we have chosen upward as positive, and gravity pulls downward. If we had chosen downward as positive, we would write *a* = +*g*. The convention matters for getting signs right, but the physics is the same either way.

### Worked Example 1: A Ball Thrown Upward

A baseball player throws a ball straight upward from ground level with an initial velocity of 20.0 m/s. The ball is caught by another player at the same height. 

(a) What is the maximum height the ball reaches?
(b) How long is the ball in the air?
(c) What is the velocity of the ball when it is caught?

**Solution:**

Set up: *y₀* = 0, *v₀* = +20.0 m/s (upward), *a* = −9.8 m/s².

(a) At maximum height, the velocity is zero. Using $v^2 = v_0^2 - 2g(y - y_0)$:

$$0 = (20.0)^2 - 2(9.8)(y - 0)$$

$$y = \frac{400}{19.6} = 20.4 \text{ m}$$

(b) The ball returns to *y* = 0 when caught. Using $y = y_0 + v_0 t - \frac{1}{2}gt^2$:

$$0 = 0 + 20.0 t - \frac{1}{2}(9.8)t^2$$

$$0 = t(20.0 - 4.9t)$$

This gives *t* = 0 (at release) or *t* = 20.0 / 4.9 = 4.08 s.

(c) Using $v = v_0 - gt$:

$$v = 20.0 - 9.8(4.08) = 20.0 - 40.0 = -20.0 \text{ m/s}$$

The ball is moving downward at 20.0 m/s when caught—exactly the speed it was thrown, but in the opposite direction. This is not a coincidence; it follows from the symmetry of the parabolic trajectory.

### Worked Example 2: Baumgartner's 30-Second Descent Revisited

We calculated earlier that after 30 seconds of free fall from rest, Baumgartner has descended 4,410 meters and is moving at 294 m/s downward. But this assumes no air resistance. In reality, Baumgartner encountered denser and denser air as he fell, which provided drag that increased with speed. The acceleration decreased as speed increased, so the real motion is more complex.

However, for the first 10-20 seconds, above 30 km altitude where air is extremely thin, the constant-acceleration model is remarkably accurate. Baumgartner's actual velocity at 34 seconds was about 380 m/s (about 850 mph). Our free-fall model, if we had extended it to 34 seconds, would predict:

$$v = 0 - 9.8(34) = -333 \text{ m/s}$$

The free-fall model underestimates the speed because it ignores air resistance. But it captures the *order of magnitude* correctly, and for the early part of the jump, it gives accurate results.

#### Common Misconception: "Heavier Objects Fall Faster"

This is incorrect. In free fall (no air resistance), all objects fall at the same acceleration regardless of mass. A bowling ball and a feather dropped from the same height reach the ground at the same time (in a vacuum). The reason we observe otherwise on Earth is air resistance: the feather is light and has a large surface area relative to its mass, so air resistance dominates. The bowling ball is dense and reaches a terminal velocity (where air resistance balances weight) at a much higher speed. But the *acceleration* is the same for both at any given moment.

### The Trade-Off: Constant Acceleration Versus Air Resistance

The real world includes air resistance, which we ignore in this chapter. In later chapters, we will examine the effects of drag forces. For now, the trade-off is clear: we gain simplicity and elegance by assuming no air resistance, and we accept that our predictions will overestimate the acceleration of light objects or those falling from great heights.

---

## Integration: What You Now See That You Didn't Before

The opening puzzle was: How is a runner's final position connected to the runner's initial acceleration?

The answer now unfolds across three levels.

**Mechanically**, velocity is the derivative of position, and acceleration is the derivative of velocity. If we know the acceleration, we can integrate it to find velocity:

$$v(t) = v_0 + \int_0^t a \, dt'$$

And we can integrate velocity to find position:

$$x(t) = x_0 + \int_0^t v \, dt'$$

For constant acceleration, these integrals are trivial, and we get the kinematic equations.

**Mathematically**, the equation $x = x_0 + v_0 t + \frac{1}{2}at^2$ shows that position depends on the time to the *second power* when acceleration is nonzero. This is why a small change in acceleration early in a race can produce a large change in final position—the effect is magnified by the $t^2$ term. A dragster with an acceleration of 26 m/s² covers only 26 meters in the first 2 seconds, but 104 meters in the first 4 seconds. The distance covered in the second half of the acceleration period is four times the distance covered in the first half.

**Physically**, what is happening is that the object's velocity is constantly increasing. When acceleration is constant, the average velocity during a time interval is $(v_0 + v_f)/2$, and displacement is that average velocity times time. Since the final velocity is itself proportional to the acceleration, the final displacement ends up depending on the square of time.

This understanding also clarifies why some motion is "easy" to predict and some is not:
- When acceleration is constant (a ball in free fall, a car pressing the accelerator), we can use the kinematic equations, which are exact.
- When acceleration varies with time (a falling object with air resistance, a car accelerating to a maximum speed and then maintaining it), we must either integrate the acceleration function (if we know it) or break the motion into segments.
- When the relationship between force and motion is complex (a fluid flowing around an obstacle, a rocket burning fuel), the equations become much harder, and we often rely on numerical solutions.

The chapter has equipped you to analyze any motion with constant acceleration. In the next chapter, we will extend this to motion in two and three dimensions, where vectors enter the picture. After that, we will ask what *causes* acceleration—the forces that produce it—and how to predict motion when forces are present.

---

## Graduated Exercises

### Warm-Up (Build Fluency)

1. **Position and Displacement**: A dog runs 20 meters east, then 15 meters west along a straight path. 
   - What is the dog's displacement?
   - What is the distance traveled?
   - If the entire motion took 10 seconds, what was the average velocity? The average speed?

2. **Instantaneous Velocity**: The position of a particle is $x(t) = 5t^2 + 3t$ (in meters). 
   - Find the velocity as a function of time, $v(t)$.
   - What is the velocity at $t = 2$ s?
   - At what time is the velocity zero? (If your answer is nonphysical, explain why.)

3. **Kinematic Equations**: A car accelerates from rest at 2.5 m/s². 
   - How long does it take to reach 25 m/s?
   - How far does it travel in that time?

### Application (Connect Concepts)

4. **Stopping Distance**: A car traveling at 20 m/s (about 45 mph) applies the brakes. Assuming constant deceleration of 5.0 m/s², how far does the car travel before coming to a complete stop? (Do not use time as an intermediate step.)

5. **Free Fall from Known Height**: A stone is dropped from the top of a 100-meter cliff.
   - How long does it take to hit the water?
   - What is its velocity when it hits the water?
   - (Neglect air resistance.)

6. **Two-Stage Motion**: An elevator starts from rest at the ground floor and accelerates upward at 2.0 m/s² for 5.0 seconds. It then moves at constant velocity for 10.0 seconds. 
   - What is the maximum velocity reached?
   - What is the total distance traveled?

### Synthesis (Put It Together)

7. **Graphical Integration**: You are given a velocity-versus-time graph where velocity increases linearly from 0 m/s at $t$ = 0 to 10 m/s at $t$ = 5 s, then remains constant at 10 m/s from $t$ = 5 s to $t$ = 10 s.
   - Sketch the corresponding acceleration-versus-time graph.
   - Sketch the corresponding position-versus-time graph (assuming $x_0 = 0$).
   - Calculate the total displacement.

8. **Reverse Engineering**: A particle has position $x(t) = -3t^2 + 12t + 5$ (in meters).
   - Find the velocity and acceleration as functions of time.
   - At what time is the velocity zero?
   - At what time is the acceleration zero? (Explain your answer.)
   - What is the maximum position, and when does it occur?

### Challenge (Extend Your Thinking)

9. **Non-Constant Acceleration**: The acceleration of a motorboat is $a(t) = 6 - 2t$ m/s² for the first 3 seconds (with $a$ = 0 thereafter). 
   - Find the velocity as a function of time for $0 \leq t \leq 3$ s, given $v_0 = 0$.
   - Find the position as a function of time for $0 \leq t \leq 3$ s, given $x_0 = 0$.
   - What is the displacement during the first 3 seconds?

10. **Cheetah and Gazelle**: A gazelle runs at constant velocity 10 m/s. A cheetah, initially at rest, begins accelerating at 4 m/s² at the instant the gazelle passes. 
    - After how long does the cheetah catch the gazelle?
    - How far does each animal travel in that time?
    - (Solve this by setting the position equations equal and solving for time.)

---

## Chapter Summary

Kinematics describes motion without asking what causes it. Three quantities—position, velocity, and acceleration—form the foundation:

- **Position** (*x*) is location; **displacement** (Δ*x*) is change in location. 
- **Velocity** is the derivative of position: $v = dx/dt$. It tells us how fast and in which direction an object is moving.
- **Acceleration** is the derivative of velocity: $a = dv/dt = d^2x/dt^2$. It tells us how fast velocity is changing.

When acceleration is constant, the kinematic equations relate position, velocity, acceleration, and time:

$$v = v_0 + at$$

$$x = x_0 + \frac{v_0 + v}{2}t$$

$$x = x_0 + v_0 t + \frac{1}{2}at^2$$

$$v^2 = v_0^2 + 2a(x - x_0)$$

These equations emerge from calculus—from the definitions of derivatives and the integration of constant functions. They are not laws of nature; they are consequences of how derivatives work.

**Free fall** is motion under gravity alone, with constant acceleration $a = -g = -9.8$ m/s² (taking upward as positive). All objects in free fall have the same acceleration, regardless of mass. The kinematic equations apply directly to free-fall problems.

The motion of objects with constant acceleration is entirely predictable if you know the initial conditions (position and velocity) and the acceleration. In the next chapter, we extend this to two and three dimensions, where vector quantities enter the picture. After that, we will examine forces and Newton's laws, which explain what produces acceleration in the first place.

---

## Connections Forward

**Chapter 5: Motion in Two and Three Dimensions** extends kinematics to vector form. The quantities $\vec{r}$ (position), $\vec{v}$ (velocity), and $\vec{a}$ (acceleration) become vectors, but the relationships between them remain the same: velocity is the derivative of position, and acceleration is the derivative of velocity. Projectile motion—a basketball's trajectory, the path of a bullet, a water fountain—falls naturally from the vector kinematic equations.

**Chapter 6: Newton's Laws of Motion** asks the question we have not asked: *What causes acceleration?* Newton's second law relates acceleration to force: $\vec{F} = m\vec{a}$. Once we understand what forces are present, we can predict the acceleration and use kinematics to predict motion. The separation of kinematics (description of motion) from dynamics (causes of motion) is artificial but pedagogically useful.

**Energy and Momentum Chapters** use the kinematic equations to define work, kinetic energy, and momentum, which turn out to be more fundamental than position and velocity for understanding collisions, oscillations, and many other phenomena.

---

## What Would Change My Mind

The central claims of this chapter—that velocity is the derivative of position, that acceleration is the derivative of velocity, and that these definitions lead to the kinematic equations—are not subject to revision. They follow from calculus, not from observation. However, my confidence in the real-world applicability of these equations would be shaken if we discovered a realm where acceleration is not the rate of change of velocity, or where derivatives do not behave as expected. (We know such realms exist: at subatomic scales, quantum mechanics governs motion, and the classical kinematic equations fail. But in the everyday world, they are trustworthy.)

The assumption of constant acceleration is explicitly an idealization. Real motion often involves varying acceleration. I would refine, not revise, the chapter if we had experimental evidence that the kinematic equations are systematically wrong for any constant-acceleration situation in the everyday world—say, if drag forces turned out to follow a different law than we currently believe. But our experimental confirmation of these equations is strong across a wide range of speeds and contexts.

---

## Still Puzzling

The relationship between kinematics and causality still intrigues me. We have treated position, velocity, and acceleration as mathematical descriptions—derivatives and integrals of each other. But *what in the physical world* corresponds to these derivatives? Why is acceleration the second derivative of position, not something else? The answer will come when we examine forces: acceleration occurs *because* of forces acting on an object. The derivative structure reflects the structure of causality in mechanics. This is deeper than kinematics alone can reveal.

---

## Discoverability Tags

kinematics, motion, calculus, derivative, integral, velocity, acceleration, free-fall, constant-acceleration, one-dimensional-motion



---

## LLM Exercise — Chapter 4: 1D Kinematics Integrator

**Project:** *Physics Simulation Toolkit*.

**What you're building this chapter:** A numerical-integration framework for 1D motion — Euler, semi-implicit Euler, RK4 — with empirical verification of the constant-acceleration kinematics equations and a comparison of integrator accuracy.

**Tool:** Claude Code.

**The prompt:**

```
Chapter 4 task in the physics-simulation-toolkit. The chapter taught
$v(t) = dx/dt$ and $a(t) = dv/dt$ — derivatives and integrals as the
mathematical relations between position, velocity, and acceleration.
Build the numerical machinery and verify it against the analytical
kinematics.

In `chapters/ch04_motion_1d/`:

1. `simulations.py` — implement three integrators for the ODE system
   $\dot{x} = v$, $\dot{v} = a(t, x, v)$:
   - `euler_step(state, dt, accel_fn)` — explicit Euler
   - `semi_implicit_euler_step(state, dt, accel_fn)` — symplectic Euler
   - `rk4_step(state, dt, accel_fn)` — fourth-order Runge–Kutta

   Each takes `state = (x, v)`, a timestep `dt`, and an acceleration
   function. Use the unit-aware vectors from Ch 3 (1D for now; we'll
   generalize in Ch 5).

   Plus utility functions:
   - `simulate(integrator, state0, accel_fn, dt, t_end)` — run the
     simulation from t=0 to t=t_end, return arrays of (t, x, v)
   - `kinematics_const_accel(x0, v0, a, t)` — analytical solution for
     constant acceleration

2. `test_simulations.py`:
   - Free fall: drop a 1 kg ball from 10 m with g = 9.81 m/s^2. The
     analytical time-to-ground is sqrt(2h/g). Verify each integrator
     hits the ground within tolerance proportional to its error order
     (Euler: O(dt), RK4: O(dt^4)).
   - Constant-velocity check: with a=0, all integrators should be exact
     (or within floating-point error).
   - Energy check on free-fall: total mechanical energy should be
     conserved by RK4 to high precision; Euler drifts up; symplectic
     Euler oscillates around the truth.

3. `benchmarks.py` — compare wall time and error for the three
   integrators on free fall, varying dt from 1.0 down to 0.001
   seconds. Produce a log-log plot of error vs. dt for each
   integrator. Verify the slopes match theory: Euler ≈ 1,
   semi-implicit Euler ≈ 1, RK4 ≈ 4.

4. `README.md` — three decision cards (one per integrator) covering
   when each is the right tool. "Surprising findings" section reports
   the energy-drift behavior of explicit Euler on a simple
   pendulum — the canonical motivation for symplectic methods.

Commit as `ch04: 1D kinematics with three integrators and empirical
order verification`.
```

**What this produces:** Three integrators, empirical verification of error-order scaling, free-fall correctness, and a benchmark plot of error vs. dt. The framework all later dynamics chapters use.

**How to adapt this prompt:**

- *For your own project:* The three integrators are the standard pedagogical set. For more sophisticated work add adaptive RK (scipy's `solve_ivp` with `RK45`). Mention this in the README; defer the implementation.
- *For ChatGPT / Gemini:* Both work. The symplectic-Euler subtlety (update velocity first using current position, then update position using new velocity) is easy to get wrong; verify on a pendulum.
- *For Claude Code:* Native fit. Let it run the benchmark and report actual error scaling.
- *For a Claude Project:* Not the fit.

**Connection to previous chapters:** Uses `Vec3` from Ch 3 (in 1D form) and `Units` from Ch 2.

**Preview of next chapter:** Chapter 5 generalizes to 2D and 3D — projectile motion with drag, circular motion with verified period, and relative-motion frame transformations.


---

##  AI Wayback Machine
The physics in this chapter didn't appear from nowhere. **Émilie du Châtelet** was the translation and commentary on Newton's *Principia* into French (published posthumously 1759) — and the experimental and theoretical argument that the measure of motion is *mv²*, not *mv*, anticipating kinetic energy by a half-century — and despite the substance of the work, the name is far less recognized than it deserves. Here's a prompt to find out more — and then make it better.

**Run this:**

```
Who was Émilie du Châtelet, and how does their work on the kinetic-energy ($mv^2$) versus momentum ($mv$) dispute and Newton's *Principia* connect to motion along a straight line and the mathematical objects that describe it? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Émilie du Châtelet"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to describe specifically how du Châtelet's experimental argument (using lead balls dropped onto soft clay) showed that motion's effect scales with $v^2$, not $v$
- Ask: "Du Châtelet died at 42 from complications after childbirth, days after finishing the *Principia* translation. How is her translation viewed today versus other contemporary French versions, and what made hers distinctive?"
- Add the framing: "Answer in the eighteenth-century register of a letter du Châtelet might have written to Voltaire about the Leibniz-Newton dispute"

What changes? What gets better? What gets worse?
